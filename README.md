# Segunda Mesa

Plataforma web para que una cafetería avise a tiempo sus excedentes de alimentos al cierre y alguien que pueda aprovecharlos los reserve y los recoja. Proyecto del Taller de Hackathon (Reto 1: desperdicio de alimentos).

> **Estado:** prototipo funcional (MVP) con datos de prueba. El flujo principal se ejecuta de principio a fin; todavía no se ha validado con una cafetería ni con usuarios reales (ver [Limitaciones y próximos pasos](#limitaciones-y-próximos-pasos)).

## Reto y problema

**Pregunta del reto:** ¿cómo lograr que el alimento que hoy se tira llegue, a tiempo y sin fricción, a quien sí puede aprovecharlo?

**Problema que abordamos:** en una cafetería, la persona encargada del cierre detecta los sobrantes tarde y tiene poco tiempo para encontrar quién los recoja; el aviso suele llegar incompleto (sin cantidad ni horario de recogida).

**Cómo tratamos esta información.** Siguiendo la guía del taller, separamos lo que sabemos de lo que suponemos:

| Tipo | Qué es en este proyecto |
|---|---|
| Dato secundario | La estimación nacional de desperdicio (abajo), tomada de una fuente externa. |
| Supuesto / hipótesis | Que el aviso tardío o incompleto es la causa principal de que el excedente no se aproveche. Es el punto de partida del diseño, no un hallazgo. |
| Dato simulado | Todos los lotes, reservas y nombres que aparecen al probar el sistema. |
| Dato observado propio | Ninguno todavía: no hemos hecho observaciones de cierres ni entrevistas formales. |

Contexto nacional (no es una medición de nuestra comunidad): una nota de Expansión del 30 de septiembre de 2025 atribuye a la FAO una estimación de 20.4 millones de toneladas de alimentos desperdiciados al año en México.

## Usuarios objetivo

- **Usuario principal:** persona encargada del cierre de la cafetería, que publica el excedente. Es quien detecta el sobrante y necesita avisar rápido, con cantidad y hora límite.
- **Segundo usuario:** persona o grupo que recoge el excedente y lo reserva. Necesita saber qué hay, cuánto y hasta cuándo.
- **Quién sostendría la operación (por validar):** el propio negocio, una institución que quiera ofrecer la herramienta a su comunidad o una organización que reciba los excedentes.

**Cómo los identificamos:** los definimos a partir del escenario propuesto en la guía del taller (cafetería y grupo cercano que recoge al cierre). Es una definición de partida; validarla con personas reales es el primer paso pendiente del plan de pruebas.

## Solución

Flujo principal que se puede ejecutar de principio a fin:

1. La cafetería **publica un excedente** (alimento, cantidad, unidad, lugar, responsable y hora límite de recogida). Puede escribir una nota libre y la IA propone los campos del formulario; la persona los revisa y confirma antes de publicar.
2. La persona que recoge consulta **lo disponible**, con cuenta regresiva, y **reserva** una cantidad.
3. El sistema actualiza la disponibilidad y **no permite reservar más de lo existente**.
4. Se **confirma la cantidad realmente recogida**; si fue menor a la reservada, la diferencia vuelve a estar disponible mientras el aviso siga vigente. Una **cancelación libera** la reserva y un aviso **vencido** deja de aceptar solicitudes.
5. El **resumen** separa lo publicado, lo reservado sin recoger, lo recogido y lo expirado sin rescate, **por cada unidad** (no se suman piezas con litros).

**Propuesta de valor:** un aviso estructurado (qué, cuánto, dónde y hasta cuándo) y una reserva visible, en lugar de mensajes sueltos que llegan incompletos.

### Decisiones clave

- La IA solo **propone**; nunca guarda ni decide por sí sola. El formulario manual siempre funciona.
- La hora límite la **calcula el código** a partir de la hora que extrae la IA, en lugar de pedirle a la IA que haga la cuenta.
- La IA **no evalúa si un alimento es apto para consumo**. Eso corresponde a la persona responsable y a las condiciones de manejo acordadas con el negocio.
- Las métricas se calculan **por unidad**, para no mezclar cantidades que no son comparables.
- El control de cantidad se valida en el servidor, no solo en la interfaz: cada reserva se compara con la cantidad disponible en ese momento, así que reservas consecutivas nunca exceden el total del lote.

### Alternativas que comparamos

Una misma dificultad puede abordarse de varias formas. Comparamos cuatro enfoques con los criterios que sugiere la guía: utilidad para el usuario, facilidad de adopción, acceso a datos, esfuerzo y viabilidad.

| Alternativa | Qué haría | Por qué la descartamos o la elegimos |
|---|---|---|
| **Proceso actual** (llamadas, mensajes o una hoja de cálculo) | Avisar a mano a quien pueda recoger. | Es el punto de comparación. Depende de que alguien recuerde avisar y no controla cuánto queda disponible ni hasta cuándo; el aviso puede llegar incompleto. |
| **Registro de mermas** | Anotar qué se pierde, cuánto y por qué, con un tablero. | Hace visible el desperdicio, pero no hace que el alimento llegue a alguien a tiempo. Necesita un periodo largo de registros antes de ser útil y no encaja con una prueba corta. |
| **Planeación de producción** | Sugerir cuánto preparar según el historial de demanda. | Reduciría el excedente en el origen, pero requiere historial de ventas que no tenemos y no resuelve qué hacer con el sobrante que igual se genera. |
| **Coordinación de excedentes** (elegida) | Publicar, reservar, confirmar la recogida y resumir. | Ataca directamente el problema planteado (aviso tardío o incompleto), se puede construir como flujo mínimo ejecutable y su parte crítica se puede probar: reservas simultáneas, cancelaciones y cantidades inválidas. |

La alternativa elegida podría cambiar si la validación con usuarios muestra que el obstáculo real es otro (por ejemplo, la falta de transporte para recoger). En ese caso el enfoque debería ajustarse a coordinación de recogidas.

## Tecnologías

| Componente | Tecnología | Por qué |
|---|---|---|
| Backend / API | Python + FastAPI | Endpoints claros y documentación automática en `/docs` |
| Base de datos | SQLite | Sin instalación; suficiente para un prototipo |
| Frontend | HTML, CSS y JavaScript sin frameworks | Se ejecuta sin compilar y es fácil de explicar |
| IA | API de Gemini (Google) | Convierte una nota libre en un registro estructurado y redacta observaciones del resumen |

## Instalación y ejecución

**Requisitos:** Python 3 (probado con 3.15) y Git.

```bash
git clone https://github.com/robusto-nit/segunda-mesa.git
cd segunda-mesa
```

### 1. Variables de entorno

Copia `.env.example` a `.env` **en la raíz del repositorio** y completa tu clave de Gemini. **Nunca subas `.env` al repositorio.**

```bash
cp .env.example .env
# edita .env y escribe: GEMINI_API_KEY=tu_clave
```

La clave se obtiene en [Google AI Studio](https://aistudio.google.com/apikey). Sin clave, el sistema funciona igual, pero "Completar con IA" devuelve un borrador de respaldo sin interpretar la nota.

### 2. Backend

```bash
cd backend
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash). En Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Queda en http://127.0.0.1:8000. La documentación de la API y sus ejemplos están en http://127.0.0.1:8000/docs.

### 3. Frontend

En otra terminal:

```bash
cd frontend
python -m http.server 5500
```

Abre http://localhost:5500.

### Prueba rápida

1. En **Publicar**, escribe `sobraron 12 tortas de jamón y 3 litros de café, recoger antes de las 8`, pulsa **Completar con IA**, escribe tu nombre en **Responsable** y publica.
2. En **Disponibles**, escribe tu nombre arriba y reserva una cantidad.
3. En **Mis reservas**, confirma la recogida con una cantidad menor a la reservada.
4. En **Resumen**, revisa los números por unidad y las observaciones.

**Datos de prueba listos:** si prefieres no capturar nada a mano, desde `backend/` con el entorno activo ejecuta `python seed_simulado.py` (o `python seed_simulado.py --reset` para borrar y volver a cargar). Crea lotes y reservas ficticios, marcados como "(simulado)". La base `segunda_mesa.db` se crea sola en `backend/` y no se sube al repositorio.

### Casos de borde a probar

Son los que más fácilmente fallan en un sistema de reservas:

- Dos reservas seguidas sobre el mismo lote que juntas superan lo disponible: la segunda se rechaza con el mensaje "Stock insuficiente".
- Una cantidad inválida (cero, negativa o mayor a lo disponible).
- Una cancelación: la cantidad vuelve a estar disponible.
- Un lote con hora límite vencida: ya no acepta reservas.
- Confirmar una recogida menor a lo reservado: la diferencia vuelve a estar disponible si el aviso sigue vigente; si ya venció, cuenta como expirada sin rescate.

### Endpoints principales

| Método | Ruta | Qué hace |
|---|---|---|
| POST | `/lotes` | Publica un excedente |
| GET | `/lotes` | Lista excedentes (`solo_activos`) |
| POST | `/lotes/parse-ia` | Interpreta una nota libre y propone los campos |
| POST | `/reservas` | Reserva una cantidad de un lote |
| GET | `/reservas` | Lista reservas |
| PATCH | `/reservas/{id}/confirmar` | Confirma la cantidad recogida |
| PATCH | `/reservas/{id}/cancelar` | Cancela y libera la cantidad |
| GET | `/resumen` | Métricas por unidad; con `incluir_ia=true` agrega observaciones |

## Evidencia y partes simuladas

**Funciona de verdad (código ejecutable):** publicación, listado, reservas con control de cantidad, cancelación, confirmación de recogida, vencimiento de lotes, resumen por unidad e interpretación de notas con Gemini.

**Simulado o de prueba:**
- Los lotes, reservas y nombres que se ven al probar el sistema son **datos de prueba** creados por el equipo. **No son resultados de una cafetería real** ni demuestran reducción de desperdicio.
- No hay avisos reales (mensajes, correos ni notificaciones) ni recolección real: las reservas se registran en el sistema, pero no se entrega ningún alimento.
- Las tasas del resumen (por ejemplo, la proporción recogida) describen únicamente esos datos de prueba.

**Qué demuestra y qué no:** que una reserva funcione demuestra el flujo técnico. Por sí sola no demuestra que se evitó desperdicio real: una reserva no equivale a una entrega, ni una entrega a que el alimento se consumiera.

**Métrica del resumen y su limitación:** la proporción recogida (cantidad recogida sobre cantidad publicada, por unidad) mide qué tan bien se coordina la recogida dentro del sistema. Se calcula por unidad y no mide desperdicio evitado.

## Equipo

| Integrante | Rol | Perfil |
|---|---|---|
| Roberto Reza | Frontend (interfaz web) | [robusto-nit](https://github.com/robusto-nit) |
| Adrian Alba | Backend (API y base de datos) | [ADRIAN ALBA MIRANDA](https://github.com/AlbaYS11) |
| Jorge | Documentación | [OrphanDrake](https://github.com/OrphanDrake) |
| Erik Rivera | Documentación | [Erick Ri](https://github.com/Luz-siceda) |

## Viabilidad y plan de negocios

El análisis completo, con fuentes y el cálculo de cada cifra, está en [`docs/plan-negocios.md`](docs/plan-negocios.md). Resumen:

- **Mercado de dos lados:** oferta (encargada o encargado del cierre de una cafetería) y demanda (estudiantes, vecinos y organizaciones cercanas). El segmento inicial es una cafetería piloto y un grupo de recolección.
- **Competidores y alternativas:** Cheaf (marketplace de paquetes sorpresa con presencia en varias ciudades de México), Too Good To Go (mismo modelo; no encontramos evidencia de que opere en México), Olio y Geev (compartir comida entre particulares), la Red de Bancos de Alimentos de México (rescate institucional) y los avisos informales por mensajería. Cheaf es el competidor directo más fuerte; Segunda Mesa se diferencia por publicar un lote específico con cantidad exacta y hora límite, y por apuntar a zonas donde ese competidor no reporta presencia.
- **Modelo de ingresos:** suscripción mensual de la cafetería; quien recoge no paga. La tarifa propuesta de **$199 MXN al mes** es una decisión de diseño del equipo y **todavía no se ha probado con cafeterías**.
- **Costos (tipo de cambio de referencia $19.70 MXN por dólar):** costo fijo de **$873.75 MXN al mes**: infraestructura ($142.83), dominio ($22.08), tiempo de visitas para conseguir usuarios ($315.04) y tiempo del equipo ($393.80). Estos dos últimos se valoran a salario mínimo y no son gasto en efectivo en un proyecto académico. Se suma la IA, de **$4.43 MXN al mes por cafetería**, con parámetros de uso supuestos que se muestran en el plan.
- **Punto de equilibrio:** cada cafetería deja $194.57 MXN después de su costo de IA. Una sola cubre infraestructura y dominio ($164.91 / $194.57 = 0.85); para cubrir todo el costo fijo, incluido el tiempo del equipo, hacen falta 5 cafeterías ($873.75 / $194.57 = 4.49).
- **Escenarios:** de 5 a 50 cafeterías, el margen mensual va de $99 a $8,855 MXN. Con 5 cafeterías el margen es mínimo. Es aritmética de la fórmula, no un pronóstico de ventas. Equivalen a entre 0.007% y 0.066% de las 75,497 cafeterías que reporta el INEGI según Milenio.
- **Riesgos principales:** competidor consolidado, que la cafetería no tenga suficiente excedente o no quiera publicarlo, que no haya quien recoja, inocuidad del alimento y dependencia del servicio de IA.
- **Siguiente paso:** elegir cafetería y grupo piloto, y medir lotes publicados y recogidos antes de cobrar.

## Fuentes

- Expansión Política. "FAO: México desperdicia cada año 20.4 millones de toneladas de alimentos", 30 de septiembre de 2025. Fuente secundaria que atribuye la cifra a la FAO. Consulta: 14 de octubre de 2026.
- PNUMA. "El mundo desperdicia más de 1.000 millones de platos de comida al día", comunicado sobre el Índice de Desperdicio de Alimentos 2024. Consulta: 14 de octubre de 2026.
- Las 15 fuentes del plan de negocios (precios, competidores y mercado), con enlace y fecha de consulta, están en [`docs/plan-negocios.md`](docs/plan-negocios.md#fuentes).
- Taller de Hackathon, 5 de octubre de 2026. Reto Segunda Mesa: entregables, criterios y rúbrica.

## Limitaciones y próximos pasos

**Limitaciones actuales**
- No hay inicio de sesión: el nombre de quien reserva se escribe a mano.
- Un solo lugar de publicación por defecto y sin notificaciones.
- Las unidades se agrupan por el texto escrito, sin distinguir mayúsculas ("piezas" y "pieza" cuentan como unidades distintas).
- La reserva compara contra la cantidad disponible y luego actualiza, sin bloqueo de base de datos: dos solicitudes exactamente simultáneas sobre el mismo lote podrían exceder la cantidad. Para el prototipo no se probó concurrencia real.
- La base SQLite es local: sin disco persistente en un servidor, los datos no sobreviven a un redespliegue.
- La IA depende de un servicio externo que puede estar saturado; en ese caso se muestra un aviso y se usa el formulario manual.
- El sistema no valida la inocuidad del alimento ni sustituye las condiciones de manejo acordadas con el negocio.
- Todavía no se ha probado con una cafetería ni con usuarios reales, y no contamos con observaciones ni entrevistas propias que respalden la hipótesis.

**Próximos pasos**
- Observar cierres reales y entrevistar a 3 a 5 personas con distintos roles para validar o corregir la hipótesis.
- Probar con personas que publiquen y reserven sin instrucciones, y medir tiempo, errores y tareas completadas.
- Registrar el motivo por el que un lote no se recoge, para poder analizar causas.
- Definir con la cafetería y con quien recoge las condiciones de manejo y aceptación del alimento.
- Normalizar las unidades (por ejemplo, "pieza" y "piezas") para que el resumen no las separe.
