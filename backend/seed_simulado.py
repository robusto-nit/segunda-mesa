"""
Carga DATOS SIMULADOS de prueba en la base de datos del backend (segunda_mesa.db).

Todo lo que crea este script es ficticio: sirve para probar y demostrar el sistema,
NO son resultados de una cafetería real ni demuestran reducción de desperdicio.
Los registros llevan "(simulado)" en el responsable y "Receptor simulado" en las reservas.

Uso (desde la carpeta backend/, con el entorno virtual activo):
    python seed_simulado.py            # carga los datos si la base está vacía
    python seed_simulado.py --reset    # borra lo que haya y vuelve a cargar
"""
import os
import sys
import sqlite3
from datetime import datetime, timedelta

# La base se crea en backend/, igual que cuando se enciende uvicorn desde esa carpeta
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from database import DB_PATH, init_db  # noqa: E402

AHORA = datetime.now().replace(microsecond=0)
RESPONSABLE = "Encargado (simulado)"
LUGAR = "Cafetería Principal"


def desde_ahora(horas):
    return (AHORA + timedelta(hours=horas)).isoformat()


# alimento, categoría, total, disponible, unidad, urgencia, consejo, estado,
# hora límite (horas desde ahora), reservas [(receptor, reservada, recogida, estado)]
LOTES = [
    # --- Cierres de días anteriores (ya vencidos o agotados) ---
    ("Tortas de jamón", "Preparados", 12, 4, "piezas", "Alta",
     "Mantener refrigeradas y consumir el mismo día.", "vencido", -72,
     [("Receptor simulado A", 8, 8, "confirmado")]),
    ("Café", "Bebidas", 6, 3, "litros", "Media",
     "Mantener en recipiente cerrado y consumir fresco.", "vencido", -71,
     [("Receptor simulado B", 4, 3, "confirmado")]),
    ("Pan dulce", "Panadería", 20, 10, "piezas", "Media",
     "Guardar en bolsa de papel a temperatura ambiente.", "vencido", -48,
     [("Receptor simulado A", 10, 10, "confirmado"), ("Receptor simulado C", 5, 0, "cancelado")]),
    ("Sándwiches", "Preparados", 15, 15, "piezas", "Alta",
     "Mantener refrigerados.", "vencido", -47, []),
    ("Fruta picada", "Frutas", 4, 0, "kg", "Alta",
     "Mantener en frío y consumir el mismo día.", "agotado", -24,
     [("Receptor simulado B", 4, 4, "confirmado")]),
    ("Sopa del día", "Preparados", 8, 3, "litros", "Media",
     "Mantener caliente o refrigerar de inmediato.", "vencido", -23,
     [("Receptor simulado C", 5, 5, "confirmado")]),
    # --- Cierre de hoy (activos, para reservar durante la demo) ---
    ("Tortas de jamón", "Preparados", 12, 12, "piezas", "Alta",
     "Mantener refrigeradas y consumir el mismo día.", "activo", 2.3, []),
    ("Café", "Bebidas", 3, 2, "litros", "Media",
     "Mantener en recipiente cerrado y consumir fresco.", "activo", 2.3,
     [("Receptor simulado A", 1, 0, "reservado")]),
    ("Pan", "Panadería", 5, 5, "piezas", "Alta",
     "Guardar en bolsa de papel a temperatura ambiente.", "activo", 1, []),
    ("Ensalada", "Verduras", 3, 3, "kg", "Media",
     "Mantener refrigerada.", "activo", 4, []),
]


def main():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    existentes = cur.execute("SELECT COUNT(*) FROM lotes_excedentes").fetchone()[0]
    if existentes and "--reset" not in sys.argv:
        print(f"La base ya tiene {existentes} lotes y no se tocó nada.")
        print("Para borrarlos y cargar los datos simulados: python seed_simulado.py --reset")
        sys.exit(1)
    if "--reset" in sys.argv:
        cur.execute("DELETE FROM reservas")
        cur.execute("DELETE FROM lotes_excedentes")
        cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('reservas', 'lotes_excedentes')")

    n_reservas = 0
    for (alimento, categoria, total, disp, unidad, urgencia, consejo,
         estado, h_limite, reservas) in LOTES:
        creado = desde_ahora(h_limite - 6)
        cur.execute(
            """INSERT INTO lotes_excedentes
               (alimento, categoria, cantidad_total, cantidad_disponible, unidad, lugar,
                responsable, hora_limite, urgencia, consejo_conservacion, estado, creado_en)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (alimento, categoria, total, disp, unidad, LUGAR, RESPONSABLE,
             desde_ahora(h_limite), urgencia, consejo, estado, creado),
        )
        lote_id = cur.lastrowid
        for receptor, reservada, recogida, est in reservas:
            cur.execute(
                """INSERT INTO reservas
                   (lote_id, receptor_nombre, cantidad_reservada, cantidad_recogida, estado, creado_en)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (lote_id, receptor, reservada, recogida, est, desde_ahora(h_limite - 5)),
            )
            n_reservas += 1

    conn.commit()
    conn.close()
    print(f"Listo: {len(LOTES)} lotes y {n_reservas} reservas SIMULADAS cargados en {DB_PATH}.")
    print("Recuerda presentarlos como datos de prueba, no como resultados reales.")


if __name__ == "__main__":
    main()
