# Segunda Mesa

Plataforma web para que una cafetería avise a tiempo sus excedentes de alimentos al cierre y alguien que pueda aprovecharlos los reserve y los recoja. Proyecto del Taller de Hackathon (Reto 1: desperdicio de alimentos).

> **Estado:** prototipo funcional (MVP). La investigación con usuarios reales y el plan de viabilidad se documentan en `docs/` y siguen en curso.

## Reto y problema

**Pregunta del reto:** ¿cómo lograr que el alimento que hoy se tira llegue, a tiempo y sin fricción, a quien sí puede aprovecharlo?

**Hipótesis que probamos (todavía por verificar con evidencia propia):** en una cafetería, la persona encargada del cierre detecta los sobrantes tarde y tiene poco tiempo para encontrar quién los recoja; el aviso suele llegar incompleto (sin cantidad ni horario de recogida).

> _Pendiente: observaciones de cierres, entrevistas y fuentes que respaldan o corrigen esta hipótesis. Separar lo observado, lo interpretado y lo supuesto. Guardar las notas en `docs/investigacion.md`._

Contexto nacional (no es una medición de nuestra comunidad): una nota de Expansión del 30 de septiembre de 2025 atribuye a la FAO una estimación de 20.4 millones de toneladas de alimentos desperdiciados al año en México.

## Usuarios objetivo

- **Usuario principal:** persona encargada del cierre de la cafetería, que publica el excedente.
- **Segundo usuario:** persona o grupo que recoge el excedente y lo reserva.

> _Pendiente: cómo identificamos a estos usuarios, con quién hablamos y qué aprendimos._

## Solución

Flujo principal que se puede ejecutar de principio a fin:

1. La cafetería **publica un excedente** (alimento, cantidad, unidad, lugar, responsable y hora límite de recogida). Puede escribir una nota libre y la IA propone los campos del formulario; la persona los revisa y confirma antes de publicar.
2. La persona que recoge consulta **lo disponible**, con cuenta regresiva, y **reserva** una cantidad.
3. El sistema actualiza la disponibilidad y **no permite reservar más de lo existente**.
4. Se **confirma la cantidad realmente recogida**; si fue menor a la reservada, la diferencia vuelve a estar disponible. Una **cancelación libera** la reserva y un aviso **vencido** deja de aceptar solicitudes.
5. El **resumen** separa lo publicado, lo reservado sin recoger, lo recogido y lo expirado sin rescate, **por cada unidad** (no se suman piezas con litros).

**Decisiones clave:**
- La IA solo **propone**; nunca guarda ni decide por sí sola. El formulario manual siempre funciona.
- La hora límite la **calcula el código** a partir de la hora que extrae la IA, en lugar de pedirle a la IA que haga la cuenta.
- La IA **no evalúa si un alimento es apto para consumo**. Eso corresponde a la persona responsable y a las condiciones de manejo acordadas con el negocio.
- Las métricas se calculan **por unidad**, para no mezclar cantidades que no son comparables.

> _Pendiente: alternativas que comparamos y por qué las descartamos (mínimo tres). Documentarlas en `docs/decisiones.md`._

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

> _Pendiente: capturas del flujo en `docs/evidencia/` y, si se hace, resultados de pruebas con usuarios (tarea, tiempo y errores observados)._

## Equipo

| Integrante | Rol | Perfil |
|---|---|---|
| Roberto Reza | Frontend (interfaz web) | [robusto-nit](https://github.com/robusto-nit) |
| _Nombre_ | Backend (API y base de datos) | _Enlace a GitHub_ |
| _Nombre_ | _Rol_ | [OrphanDrake](https://github.com/OrphanDrake) |
| _Nombre_ | _Rol_ | _Enlace a GitHub_ |

## Plan de negocios y fuentes

> _Pendiente: enlace al plan de viabilidad (`docs/plan-negocios.md`). Toda cifra de mercado, costos o ingresos debe tener fuente o mostrar su cálculo y supuestos; no se permiten cifras inventadas._

Fuentes de contexto:
- Expansión Política. "FAO: México desperdicia cada año 20.4 millones de toneladas de alimentos", 30 de septiembre de 2025.
- PNUMA. Comunicado sobre el Índice de Desperdicio de Alimentos 2024.

## Limitaciones y próximos pasos

**Limitaciones actuales**
- No hay inicio de sesión: el nombre de quien reserva se escribe a mano.
- Un solo lugar de publicación por defecto y sin notificaciones.
- Las unidades se agrupan por el texto escrito ("piezas" y "pieza" cuentan como unidades distintas).
- La IA depende de un servicio externo que puede estar saturado; en ese caso se muestra un aviso y se usa el formulario manual.
- El sistema no valida la inocuidad del alimento ni sustituye las condiciones de manejo acordadas con el negocio.
- Todavía no se ha probado con una cafetería ni con usuarios reales.

**Próximos pasos**
- Observar cierres reales y entrevistar a 3 a 5 personas con distintos roles para validar o corregir la hipótesis.
- Probar con personas que publiquen y reserven sin instrucciones, y medir tiempo, errores y tareas completadas.
- Registrar el motivo por el que un lote no se recoge, para poder analizar causas.
- Definir con la cafetería y con quien recoge las condiciones de manejo y aceptación del alimento.
