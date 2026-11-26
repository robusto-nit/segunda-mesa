import os
import json
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

raw_key = os.getenv("GEMINI_API_KEY", "").strip().strip('"').strip("'")
client = genai.Client(api_key=raw_key) if raw_key else None

MODELOS_DISPONIBLES = [
    "gemini-3.8-flash",
    "gemini-2.5-flash-lite",
    "gemini-3.5-flash-lite",
]


class LoteDetectadoIA(BaseModel):
    alimento: str = Field(description="Nombre claro del alimento excedente")
    categoria: str = Field(description="Panadería, Lácteos, Preparados, Frutas/Verduras o Bebidas")
    cantidad: int = Field(description="Cantidad numérica entera disponible")
    unidad: str = Field(description="piezas, litros, porciones, kg, etc.")
    urgencia: str = Field(description="Alta (perecedero rápido/lácteo/carne), Media (panadería/fruta) o Baja")
    consejo_conservacion: str = Field(description="Instrucción breve de conservación o manejo seguro (máx 12 palabras)")
    horas_para_vencer: int = Field(description="Horas estimadas límite para recogerlo hoy (ej. 2 o 3)")


class RespuestaParseoIA(BaseModel):
    lotes: list[LoteDetectadoIA]


def _respaldo_local(texto_libre: str) -> list[dict]:
    return [{
        "alimento": texto_libre[:40],
        "categoria": "General",
        "cantidad": 1,
        "unidad": "lote",
        "urgencia": "Media",
        "consejo_conservacion": "Mantener en lugar fresco y consumir hoy.",
        "hora_limite": (datetime.now() + timedelta(hours=2)).isoformat()
    }]


def parsear_nota_excedente(texto_libre: str) -> list[dict]:
    """Convierte texto informal de cierre de cafetería en lotes estructurados."""
    if not client:
        return _respaldo_local(texto_libre)

    prompt = (
        f"Eres un asistente operativo de una cafetería que registra excedentes al cierre. "
        f"Extrae los alimentos sobrantes de esta nota del encargado: '{texto_libre}'. "
        f"Si no menciona tiempo límite, asume 2 horas para alimentos de urgencia Alta y 4 horas para Media/Baja."
    )

    for modelo in MODELOS_DISPONIBLES:
        try:
            response = client.models.generate_content(
                model=modelo,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=RespuestaParseoIA,
                    temperature=0.2,
                ),
            )
            data = json.loads(response.text)
            resultados = []
            for item in data.get("lotes", []):
                horas = max(1, min(item.get("horas_para_vencer", 2), 24))
                item["hora_limite"] = (datetime.now() + timedelta(hours=horas)).isoformat()
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
    "Analiza estos datos de excedentes de una cafetería y devuelve exactamente 3 observaciones "
    "cortas (máximo 20 palabras cada una), basadas SOLO en los datos dados. "
    "No inventes cifras, metas ni porcentajes que no se desprendan de los datos. "
    "Si hay pocos datos para concluir algo (por ejemplo, un solo lote por producto), "
    "dilo en la observación y sugiere qué dato falta registrar.\n"
    f"{estadisticas_texto}"
)

    for modelo in MODELOS_DISPONIBLES:
        try:
            response = client.models.generate_content(
                model=modelo,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.4),
            )
            lineas = [l.strip("-•*123. ").split("(")[0].strip() for l in response.text.splitlines() if l.strip()]
            if lineas:
                return lineas[:3]
        except Exception as e:
            print(f"[AVISO GEMINI {modelo}]: {e}")

    return ["No se pudieron generar recomendaciones de IA en este momento; revisa la conexión."]