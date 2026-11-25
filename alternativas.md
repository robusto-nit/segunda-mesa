# Alternativas de solución

Este documento compara cuatro formas de resolver el problema de los excedentes de una cafetería al cierre y explica por qué se eligió una. Contexto y fuentes en [`ficha-de-trabajo.md`](ficha-de-trabajo.md) y [`fuentes.md`](fuentes.md).

**Nota sobre las valoraciones:** la tabla comparativa es un análisis cualitativo del equipo (Alta, Media o Baja), no una medición.

## Criterios de comparación

1. **Rapidez del aviso:** qué tan fácil es avisar antes del cierre.
2. **Esfuerzo para la cafetería:** cuánto tiempo extra pide al personal.
3. **Control de lo disponible:** si se sabe qué hay, cuánto queda y quién lo reservó.
4. **Seguimiento y medición:** si se puede confirmar lo recogido y calcular la tasa de rescate.
5. **Viabilidad en el semestre:** si el equipo puede construirlo y demostrarlo.

## Alternativas

### A. Plataforma web de registro, reserva y recogida (Segunda Mesa)

La cafetería registra el excedente; quien recoge consulta, reserva y confirma.

- **A favor:** controla cantidades en tiempo real, evita que dos personas reserven lo mismo y permite confirmar lo recogido para calcular la métrica.
- **En contra:** exige que ambas partes usen una herramienta nueva, y el equipo debe construirla.

### B. Aviso informal por grupo de mensajería

La cafetería escribe en un grupo lo que sobra y quien llega primero lo recoge.

- **A favor:** no requiere desarrollo y mucha gente ya usa estas herramientas.
- **En contra:** no controla cantidades ni reservas, los mensajes se pierden en el chat y no deja un registro ordenado para medir resultados.

### C. Entrega regular a un banco de alimentos u organización aliada

La cafetería acuerda con una organización que recoja sus excedentes.

- **A favor:** puede dar salida constante a mayor volumen.
- **En contra:** depende de acuerdos y horarios de terceros, no resuelve el aviso de último momento y no es un producto web que el equipo pueda demostrar en el semestre.

### D. Descuento de última hora en el mostrador

La cafetería vende más barato lo que sobra al final del día, sin plataforma.

- **A favor:** no requiere tecnología y genera algo de ingreso.
- **En contra:** solo llega a quienes están presentes y no deja registro ni reserva, por lo que no permite medir lo rescatado.

## Comparación

| Criterio | A. Plataforma web | B. Grupo de mensajería | C. Banco de alimentos | D. Descuento en mostrador |
|---|---|---|---|---|
| Rapidez del aviso | Alta | Alta | Baja | Media |
| Esfuerzo para la cafetería | Medio | Bajo | Medio | Bajo |
| Control de lo disponible | Alta | Baja | Media | Baja |
| Seguimiento y medición | Alta | Baja | Media | Baja |
| Viabilidad en el semestre | Media | Alta | Baja | Alta |

## Decisión y razones

**Se elige la alternativa A.**

- Es la que mejor cumple los criterios de control de lo disponible y de seguimiento y medición, que son los que permiten calcular la **tasa de rescate**, la métrica principal del proyecto.
- Corresponde al flujo mínimo definido en el README del repositorio: registrar, reservar, actualizar disponibilidad y confirmar lo recogido.
- Su dificultad (construirla y lograr que se use) es manejable dentro del alcance del semestre.

**Se descartan como solución principal:**

- **B:** no controla cantidades ni reservas, y no permite medir.
- **C:** depende de terceros y no resuelve el aviso inmediato.
- **D:** solo llega a quien está en el local y no deja registro.

## Qué podría hacer cambiar esta decisión

- Si las personas de cafetería entrevistadas dicen que registrar un excedente toma demasiado tiempo, se simplificaría el formulario de registro o se acercaría la solución a la alternativa B.
- Si quienes recogerían prefieren enterarse por mensajería, se combinaría la plataforma con avisos por ese medio.

Estas condiciones se revisan con las notas de [`investigacion/`](investigacion/).
