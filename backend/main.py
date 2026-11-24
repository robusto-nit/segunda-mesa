from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel, Field
from datetime import datetime

from database import get_db, init_db
from ai_service import parsear_nota_excedente, generar_recomendaciones_merma

# Crea las tablas en segunda_mesa.db al arrancar
init_db()

app = FastAPI(
    title="Segunda Mesa API",
    description="Backend para gestión y rescate de excedentes en cafeterías",
    version="1.0.0"
)

# Habilita CORS para conectar con el frontend web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- ESQUEMAS DE VALIDACIÓN (DTOs) ---

class LoteCreate(BaseModel):
    alimento: str = Field(..., min_length=2)
    categoria: str = "General"
    cantidad_total: int = Field(..., gt=0)
    unidad: str = Field(..., min_length=1)
    lugar: str = "Cafetería Principal"
    responsable: str = Field(..., min_length=2)
    hora_limite: datetime
    urgencia: str = "Media"
    consejo_conservacion: str = ""


class NotaIARequest(BaseModel):
    texto_libre: str = Field(..., min_length=4)
    responsable: str = "Encargado de Cierre"
    lugar: str = "Cafetería Principal"
    publicar_automaticamente: bool = False


class ReservaCreate(BaseModel):
    lote_id: int
    receptor_nombre: str = Field(..., min_length=2)
    cantidad_reservada: int = Field(..., gt=0)


class ConfirmarRecogidaRequest(BaseModel):
    cantidad_recogida: int = Field(..., ge=0)


# --- FUNCIÓN AUXILIAR DE EXPIRACIÓN ---

def actualizar_lotes_vencidos(db: sqlite3.Connection):
    ahora = datetime.now().isoformat()
    db.execute(
        "UPDATE lotes_excedentes SET estado = 'vencido' WHERE estado = 'activo' AND hora_limite < ?",
        (ahora,)
    )
    db.commit()


# --- ENDPOINTS ---

@app.get("/")
def health_check():
    return {"status": "ok", "servicio": "Segunda Mesa Backend corriendo"}


@app.post("/lotes", status_code=201)
def crear_lote(lote: LoteCreate, db: sqlite3.Connection = Depends(get_db)):
    if lote.hora_limite <= datetime.now():
        raise HTTPException(status_code=400, detail="La hora límite debe ser futura.")

    cursor = db.execute(
        """
        INSERT INTO lotes_excedentes
        (alimento, categoria, cantidad_total, cantidad_disponible, unidad, lugar, responsable, hora_limite, urgencia, consejo_conservacion, estado, creado_en)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'activo', ?)
        """,
        (
            lote.alimento, lote.categoria, lote.cantidad_total, lote.cantidad_total,
            lote.unidad, lote.lugar, lote.responsable, lote.hora_limite.isoformat(),
            lote.urgencia, lote.consejo_conservacion, datetime.now().isoformat()
        )
    )
    db.commit()
    nuevo = db.execute("SELECT * FROM lotes_excedentes WHERE id = ?", (cursor.lastrowid,)).fetchone()
    return dict(nuevo)


@app.post("/lotes/parse-ia")
def parsear_y_crear_con_ia(req: NotaIARequest, db: sqlite3.Connection = Depends(get_db)):
    lotes_detectados = parsear_nota_excedente(req.texto_libre)

    if not req.publicar_automaticamente:
        return {"vista_previa": lotes_detectados}

    creados = []
    for item in lotes_detectados:
        cursor = db.execute(
            """
            INSERT INTO lotes_excedentes
            (alimento, categoria, cantidad_total, cantidad_disponible, unidad, lugar, responsable, hora_limite, urgencia, consejo_conservacion, estado, creado_en)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'activo', ?)
            """,
            (
                item["alimento"], item.get("categoria", "General"),
                item["cantidad"], item["cantidad"], item["unidad"],
                req.lugar, req.responsable, item["hora_limite"],
                item.get("urgencia", "Media"), item.get("consejo_conservacion", ""),
                datetime.now().isoformat()
            )
        )
        fila = db.execute("SELECT * FROM lotes_excedentes WHERE id = ?", (cursor.lastrowid,)).fetchone()
        creados.append(dict(fila))

    db.commit()
    return {"publicados": creados}


@app.get("/lotes")
def listar_lotes(solo_activos: bool = True, db: sqlite3.Connection = Depends(get_db)):
    actualizar_lotes_vencidos(db)
    if solo_activos:
        filas = db.execute(
            "SELECT * FROM lotes_excedentes WHERE estado = 'activo' AND cantidad_disponible > 0 ORDER BY hora_limite ASC"
        ).fetchall()
    else:
        filas = db.execute("SELECT * FROM lotes_excedentes ORDER BY hora_limite ASC").fetchall()
    return [dict(f) for f in filas]


@app.post("/reservas", status_code=201)
def crear_reserva(reserva: ReservaCreate, db: sqlite3.Connection = Depends(get_db)):
    actualizar_lotes_vencidos(db)
    lote = db.execute("SELECT * FROM lotes_excedentes WHERE id = ?", (reserva.lote_id,)).fetchone()

    if not lote:
        raise HTTPException(status_code=404, detail="Lote no encontrado.")
    if lote["estado"] != "activo":
        raise HTTPException(status_code=400, detail=f"El lote no acepta reservas (estado: {lote['estado']}).")
    if reserva.cantidad_reservada > lote["cantidad_disponible"]:
        raise HTTPException(
            status_code=400,
            detail=f"Stock insuficiente. Solo quedan {lote['cantidad_disponible']} {lote['unidad']}."
        )

    nueva_disp = lote["cantidad_disponible"] - reserva.cantidad_reservada
    nuevo_estado = "agotado" if nueva_disp == 0 else "activo"

    db.execute(
        "UPDATE lotes_excedentes SET cantidad_disponible = ?, estado = ? WHERE id = ?",
        (nueva_disp, nuevo_estado, lote["id"])
    )
    cursor = db.execute(
        """
        INSERT INTO reservas (lote_id, receptor_nombre, cantidad_reservada, cantidad_recogida, estado, creado_en)
        VALUES (?, ?, ?, 0, 'reservado', ?)
        """,
        (lote["id"], reserva.receptor_nombre, reserva.cantidad_reservada, datetime.now().isoformat())
    )
    db.commit()
    nueva = db.execute("SELECT * FROM reservas WHERE id = ?", (cursor.lastrowid,)).fetchone()
    return dict(nueva)


@app.patch("/reservas/{reserva_id}/confirmar")
def confirmar_recogida(reserva_id: int, body: ConfirmarRecogidaRequest, db: sqlite3.Connection = Depends(get_db)):
    reserva = db.execute("SELECT * FROM reservas WHERE id = ?", (reserva_id,)).fetchone()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada.")
    if reserva["estado"] != "reservado":
        raise HTTPException(status_code=400, detail=f"No se puede confirmar una reserva en estado '{reserva['estado']}'.")
    if body.cantidad_recogida > reserva["cantidad_reservada"]:
        raise HTTPException(status_code=400, detail="No puedes confirmar más unidades de las que reservaste.")

    diferencia = reserva["cantidad_reservada"] - body.cantidad_recogida
    if diferencia > 0:
        lote = db.execute("SELECT * FROM lotes_excedentes WHERE id = ?", (reserva["lote_id"],)).fetchone()
        if lote and lote["hora_limite"] > datetime.now().isoformat():
            nueva_disp = lote["cantidad_disponible"] + diferencia
            nuevo_estado = "activo" if lote["estado"] == "agotado" else lote["estado"]
            db.execute(
                "UPDATE lotes_excedentes SET cantidad_disponible = ?, estado = ? WHERE id = ?",
                (nueva_disp, nuevo_estado, lote["id"])
            )

    db.execute(
        "UPDATE reservas SET cantidad_recogida = ?, estado = 'confirmado' WHERE id = ?",
        (body.cantidad_recogida, reserva_id)
    )
    db.commit()
    actualizada = db.execute("SELECT * FROM reservas WHERE id = ?", (reserva_id,)).fetchone()
    return dict(actualizada)


@app.patch("/reservas/{reserva_id}/cancelar")
def cancelar_reserva(reserva_id: int, db: sqlite3.Connection = Depends(get_db)):
    reserva = db.execute("SELECT * FROM reservas WHERE id = ?", (reserva_id,)).fetchone()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada.")
    if reserva["estado"] != "reservado":
        raise HTTPException(status_code=400, detail="Solo se pueden cancelar reservas activas.")

    lote = db.execute("SELECT * FROM lotes_excedentes WHERE id = ?", (reserva["lote_id"],)).fetchone()
    if lote:
        nueva_disp = lote["cantidad_disponible"] + reserva["cantidad_reservada"]
        nuevo_estado = "activo" if (lote["estado"] == "agotado" and lote["hora_limite"] > datetime.now().isoformat()) else lote["estado"]
        db.execute(
            "UPDATE lotes_excedentes SET cantidad_disponible = ?, estado = ? WHERE id = ?",
            (nueva_disp, nuevo_estado, lote["id"])
        )

    db.execute("UPDATE reservas SET estado = 'cancelado' WHERE id = ?", (reserva_id,))
    db.commit()
    return {"mensaje": "Reserva cancelada e inventario liberado.", "reserva_id": reserva_id}


@app.get("/reservas")
def listar_reservas(db: sqlite3.Connection = Depends(get_db)):
    filas = db.execute("SELECT * FROM reservas ORDER BY creado_en DESC").fetchall()
    return [dict(f) for f in filas]


@app.get("/resumen")
def obtener_resumen(incluir_ia: bool = False, db: sqlite3.Connection = Depends(get_db)):
    actualizar_lotes_vencidos(db)
    lotes = [dict(f) for f in db.execute("SELECT * FROM lotes_excedentes").fetchall()]
    reservas = [dict(f) for f in db.execute("SELECT * FROM reservas").fetchall()]

    total_publicado = sum(l["cantidad_total"] for l in lotes)
    total_reservado_activo = sum(r["cantidad_reservada"] for r in reservas if r["estado"] == "reservado")
    total_recogido = sum(r["cantidad_recogida"] for r in reservas if r["estado"] == "confirmado")
    total_vencido_sin_recoger = sum(l["cantidad_disponible"] for l in lotes if l["estado"] == "vencido")

    tasa_rescate = round((total_recogido / total_publicado * 100), 1) if total_publicado > 0 else 0.0

    respuesta = {
        "metricas": {
            "total_publicado": total_publicado,
            "reservado_pendiente": total_reservado_activo,
            "efectivamente_recogido": total_recogido,
            "expirado_sin_rescate": total_vencido_sin_recoger,
            "tasa_rescate_porcentaje": tasa_rescate
        }
    }

    if incluir_ia and lotes:
        detalle = "\n".join([
            f"- {l['alimento']} ({l['categoria']}): publicados {l['cantidad_total']} {l['unidad']}, disponibles sin recoger {l['cantidad_disponible']}, estado {l['estado']}"
            for l in lotes[-15:]
        ])
        respuesta["recomendaciones_ia"] = generar_recomendaciones_merma(detalle)

    return respuesta