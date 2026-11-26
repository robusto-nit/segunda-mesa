import re
import os
import json
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv
import time

load_dotenv(dotenv_path="../.env")

raw_key = os.getenv("GEMINI_API_KEY", "").strip().strip('"').strip("'")
client = genai.Client(
    api_key=raw_key,
    http_options=types.HttpOptions(timeout=15000),
) if raw_key else None

MODELOS_DISPONIBLES = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash"
]


class LoteDetectadoIA(BaseModel):
    alimento: str = Field(description="Nombre claro del alimento excedente")
    categoria: str = Field(description="Panadería, Lácteos, Preparados, Frutas/Verduras o Bebidas")
    cantidad: int = Field(description="Cantidad numérica entera disponible")
    unidad: str = Field(description="piezas, litros, porciones, kg, etc.")
    urgencia: str = Field(description="Alta (perecedero rápido/lácteo/carne), Media (panadería/fruta) o Baja")
    consejo_conservacion: str = Field(description="Instrucción breve de conservación o manejo seguro (máx 12 palabras)")
    horas_para_vencer: int = Field(description="Horas estimadas límite para recogerlo hoy (ej. 2 o 3)")
    hora_limite_reloj: str = Field(description="Hora del reloj que menciona la nota, en formato HH:MM de 24 horas (ej. 08:00). Cadena vacía si no menciona ninguna")
    hora_ambigua: bool = Field(description="true si la nota da la hora sin decir mañana, tarde o noche (ej. 'antes de las 8')")


class RespuestaParseoIA(BaseModel):
    lotes: list[LoteDetectadoIA]


def _respaldo_local(texto_libre: str) -> list[dict]:
    return [{
        "alimento": texto_libre[:40],
        "categoria": "General",
        "cantidad": 1,
        "unidad": "lote",
        "urgencia": "Media",
        "respaldo": True,
        "consejo_conservacion": "Mantener en lugar fresco y consumir hoy.",
        "hora_limite": (datetime.now() + timedelta(hours=2)).isoformat()
    }]

def _calcular_limite(item: dict) -> datetime:
    """Calcula la hora límite en código. Si la hora es ambigua, prueba mañana y tarde y toma la más próxima."""
    ahora = datetime.now()
    reloj = (item.get("hora_limite_reloj") or "").strip()
    if reloj:
        try:
            h, m = (int(x) for x in reloj.split(":"))
            horas = [h, h + 12] if item.get("hora_ambigua") and 1 <= h < 12 else [h]
            candidatos = []
            for hh in horas:
                for dias in (0, 1):
                    c = (ahora + timedelta(days=dias)).replace(hour=hh, minute=m, second=0, microsecond=0)
                    if c > ahora:
                        candidatos.append(c)
            if candidatos:
                return min(candidatos)
        except (ValueError, TypeError):
            pass
    horas = max(1, min(item.get("horas_para_vencer", 2), 24))
    return ahora + timedelta(hours=horas)    

def _llamar_gemini(modelo, prompt, config):
    """Llama a Gemini; si el modelo está saturado (503), reintenta una vez."""
    for intento in range(2):
        try:
            return client.models.generate_content(model=modelo, contents=prompt, config=config)
        except Exception as e:
            saturado = "503" in str(e) or "UNAVAILABLE" in str(e)
            if saturado and intento == 0:
                time.sleep(1.5)
                continue
            raise


def parsear_nota_excedente(texto_libre: str) -> list[dict]:
    """Convierte texto informal de cierre de cafetería en lotes estructurados."""
    if not client:
        return _respaldo_local(texto_libre)

    prompt = (
    f"Eres un asistente operativo de una cafetería que registra excedentes al cierre. "
    f"Extrae los alimentos sobrantes de esta nota del encargado: '{texto_libre}'. "
    f"Si la nota menciona una hora del reloj (por ejemplo 'antes de las 8'), ponla en hora_limite_reloj "
    f"en formato HH:MM de 24 horas y marca hora_ambigua en true si no dice mañana, tarde o noche. "
    f"Si no menciona ninguna hora, deja hora_limite_reloj vacío y estima horas_para_vencer: "
    f"2 horas para urgencia Alta y 4 para Media o Baja."
    )   

    for modelo in MODELOS_DISPONIBLES:
        try:
            response = _llamar_gemini(
            modelo,
            prompt,
            types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=RespuestaParseoIA,
                    temperature=0.2,
                ),
            )
            data = json.loads(response.text)
            resultados = []
            for item in data.get("lotes", []):
                item["hora_limite"] = _calcular_limite(item).isoformat()
                resultados.append(item)
            if resultados:
                return resultados
        except Exception as e:
            print(f"[AVISO GEMINI {modelo}]: {e}")

    return _respaldo_local(texto_libre)


def generar_recomendaciones_merma(estadisticas_texto: str) -> list[str]:
    """Analiza historial de excedentes y sugiere ajustes de producción/compra."""
    if not client:
        return [
            "Configura GEMINI_API_KEY en .env para activar recomendaciones inteligentes.",
            "Revisa los productos con mayor tasa de expiración para reducir su preparación."
        ]

    prompt = (
        "Analiza estos datos de excedentes de una cafetería y devuelve exactamente 3 observaciones, "
        "una por línea, sin introducción ni numeración y de máximo 20 palabras cada una. "
        "Básate SOLO en los datos dados. No inventes cifras, metas ni porcentajes que no se desprendan de ellos. "
        "Cuando un lote venza sin recogerse, escribe que expiró sin recogerse y no digas que se desperdició "
        "ni que se tiró, porque no sabemos qué pasó con el alimento. "
        "El sistema ya registra la hora de publicación, el responsable y las cantidades recogidas: "
        "no sugieras registrar eso. Si hace falta pedir un dato nuevo, pide solo el motivo por el que no se recogió un lote. "
        "No sugieras precios. Distingue los lotes que expiraron con unidades sin recoger "
        "de los que no tuvieron ninguna recogida. "
        "Si hay pocos datos para concluir algo, dilo.\n"
        f"{estadisticas_texto}"
    )

    for modelo in MODELOS_DISPONIBLES:
        try:
            response = _llamar_gemini(
            modelo,
            prompt,
            types.GenerateContentConfig(temperature=0.4),
            )
            lineas = [re.sub(r"^\s*(?:[-•*]|\d+[.)])\s*", "", l).strip() for l in response.text.splitlines() if l.strip()]
            if lineas:
                return lineas[:3]
        except Exception as e:
            print(f"[AVISO GEMINI {modelo}]: {e}")

    return ["No se pudieron generar recomendaciones de IA en este momento; revisa la conexión."]