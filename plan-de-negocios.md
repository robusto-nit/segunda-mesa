# Plan de negocios: Segunda Mesa

**Última actualización:** 24 de noviembre de 2026

> **Sobre los datos de este documento:** el mercado, los competidores y el problema se respaldan con fuentes secundarias de [`fuentes.md`](fuentes.md). La cafetería del proyecto es ficticia, por eso **todas las cifras de ingresos, costos y volumen de la sección 7 son supuestos simulados** y están marcadas así. No son datos reales ni predicciones.

## 1. Resumen

**Segunda Mesa** es una plataforma web donde una cafetería avisa los alimentos que le sobran al cierre y otra persona los consulta, los reserva por cantidad y los recoge. La plataforma confirma lo recogido y calcula la **tasa de rescate** (cantidad recogida ÷ cantidad registrada).

- **Problema:** los servicios de alimentos generan 28 % del desperdicio mundial, unos 290 millones de toneladas en 2022 (F1, F2).
- **Modelo de ingresos propuesto:** comisión por cada porción reservada y recogida.
- **Reto principal:** ya existen apps de rescate de alimentos en México, como Cheaf, con crecimiento y presencia en varias ciudades (F6).

## 2. Problema y oportunidad

El detalle del problema está en [`ficha-de-trabajo.md`](ficha-de-trabajo.md). En resumen:

- En 2022 se desperdiciaron en el mundo 1,05 mil millones de toneladas de alimentos (F1).
- En México se estiman más de 30 millones de toneladas al año según BAMX (F4), y otra fuente cita 20,4 millones (F5).
- Los datos de los servicios de alimentos son escasos (F1), por lo que medir lo que se rescata tiene valor en sí mismo.

**Oportunidad:** una cafetería puede recuperar algo de ingreso o evitar tirar alimentos aprovechables si tiene una forma rápida de avisar y de saber quién los recogerá.

## 3. Segmento de mercado

| Segmento | Quién es | Dato de respaldo |
|---|---|---|
| **Oferta (clientes que pagan)** | Cafeterías y pequeños negocios de comida que tienen excedentes al cierre, empezando por la región de La Laguna | En México hay 776 895 unidades económicas de preparación de alimentos y bebidas (F12). La Canirac de Torreón tenía 280 agremiados en 2022 (F13) |
| **Demanda (quienes recogen)** | Personas del entorno de la cafetería que quieren comida a menor precio: estudiantes universitarios, personal de oficinas cercanas y vecinos | La cantidad de personas de este grupo en Torreón no está medida con datos verificados |

**Segmento inicial recomendado:** cafeterías cercanas a escuelas y universidades, porque el comprador y el vendedor están en el mismo lugar y los horarios de cierre coinciden con la salida de clases. Esta elección es una hipótesis del equipo; las entrevistas de [`investigacion/`](investigacion/) la confirman o la corrigen.

## 4. Propuesta de valor

| Para quién | Qué gana |
|---|---|
| **Cafetería** | Avisa un excedente en pocos pasos, evita que se pierda, puede recuperar parte del costo y ve cuánto de lo registrado se rescató |
| **Persona que recoge** | Ve qué hay, cuánto queda y hasta qué hora; reserva la cantidad que quiere; recibe confirmación |

**En qué se diferencia de lo que ya existe (propuesta de diseño):**

1. **Reserva por cantidad visible.** El flujo del proyecto muestra lo disponible y la persona reserva una cantidad. Las apps comparadas más abajo funcionan sobre "paquetes sorpresa".
2. **Medición de resultados.** La tasa de rescate se calcula por cafetería y en total.
3. **Enfoque local.** La nota de F6 no menciona Torreón entre las ciudades donde Cheaf tiene presencia consolidada.

## 5. Competidores y alternativas

| Competidor | Qué ofrece | Fuente | Qué implica para Segunda Mesa |
|---|---|---|---|
| **Cheaf** (México) | App de excedentes en "paquetes sorpresa" de panaderías, cafeterías, restaurantes y supermercados, con descuentos de 50 % a 65 %. Se reserva en la app y se recoge en el negocio. Reportó crecimiento de 40 % en facturación en México en 2025 | F6, F7, F8 | Es el competidor más directo: mismo problema y mismo tipo de negocio |
| **Too Good To Go** (Dinamarca, global) | Marketplace de "Packs Sorpresa": se reserva y paga en la app y se recoge en un horario indicado. Su página en español dice tener más de 120 millones de usuarios | F10, F11 | Muestra que el modelo funciona a gran escala. No se confirmó su operación en Torreón |
| **Kigüi** (Argentina, con operación en México) | App para rescatar productos próximos a caducar, como lácteos, panadería y fiambres | F9 | Se enfoca en productos de anaquel y no en comida preparada de una cafetería |
| **Bancos de alimentos** (alternativa C de [`alternativas.md`](alternativas.md)) | Recogen alimentos para redistribuirlos | F4 (cita a BAMX) | No resuelven el aviso inmediato de excedentes al cierre; podrían ser un destino para lo que no se reserve |

**Conclusión sobre la competencia:** el mercado no está vacío. Un proyecto nuevo debe apoyarse en un nicho local y en una experiencia más simple, no en ser el primero.

## 6. Modelo de negocio

**Modelo propuesto:** comisión del **15 %** sobre cada porción reservada y recogida (supuesto simulado).

| Opción considerada | Ventaja | Desventaja |
|---|---|---|
| **Comisión por porción rescatada (elegida)** | La cafetería solo paga cuando recupera algo; baja la barrera para empezar | El ingreso depende de que se recoja lo registrado |
| Suscripción mensual a la cafetería | Ingreso predecible | La cafetería paga aunque no venda; frena que se anime a probar |
| Gratis con anuncios o patrocinios | Sin costo para nadie | Requiere mucho tráfico para generar ingreso |

Para alimentos que se regalan, el sistema puede registrar un precio de $0 y no cobrar comisión.

## 7. Ingresos y costos (cifras simuladas)

**Todo lo de esta sección es un escenario ilustrativo.** Los supuestos son inventados para la demostración y deben cambiarse cuando el equipo tenga datos reales.

### Supuestos simulados

| Supuesto | Valor simulado |
|---|---|
| Cafeterías participantes (escenario base) | 10 |
| Porciones registradas por cafetería al día | 15 |
| Días de operación al mes | 25 |
| Tasa de rescate (escenario base) | 60 % |
| Precio promedio por porción rescatada | $35 MXN |
| Comisión de Segunda Mesa | 15 % |
| Comisión de la pasarela de pago | 4 % de lo cobrado |

### Costos mensuales simulados

| Concepto | Monto simulado (MXN) |
|---|---|
| Alojamiento web y base de datos | $600 |
| Dominio y correo | $150 |
| Difusión local (carteles y redes) | $1 500 |
| **Costos fijos** | **$2 250** |
| Comisión de la pasarela de pago (4 % de las ventas) | Variable |

El trabajo del equipo no se cuenta como costo porque es un proyecto escolar.

### Resultado del escenario base (simulado)

- Porciones registradas: 10 cafeterías × 15 × 25 = 3 750 al mes.
- Porciones recogidas: 3 750 × 60 % = 2 250.
- Ventas rescatadas: 2 250 × $35 = $78 750.
- Ingreso de Segunda Mesa (15 %): **$11 812.50**.
- Comisión de pasarela (4 %): $3 150.
- Costos fijos: $2 250.
- **Resultado mensual simulado: $6 412.50.**

### Sensibilidad: resultado mensual simulado según cafeterías y tasa de rescate (MXN)

| Cafeterías | Tasa de rescate 40 % | 60 % | 80 % |
|---|---|---|---|
| 5 | $637.50 | $2 081.25 | $3 525.00 |
| 10 | $3 525.00 | $6 412.50 | $9 300.00 |
| 20 | $9 300.00 | $15 075.00 | $20 850.00 |

**Punto de equilibrio simulado:** con 3 cafeterías y 60 % de tasa de rescate ya se cubren los costos fijos. Esto cambia por completo si el precio por porción o la comisión son distintos.

## 8. Riesgos

| Riesgo | Por qué importa | Cómo se reduce |
|---|---|---|
| **Competencia establecida** | Cheaf ya opera con crecimiento y presencia en varias ciudades (F6) | Enfocarse en un nicho local y en una experiencia más simple |
| **La cafetería no tiene tiempo de registrar** | Si registrar lleva más de un par de minutos, dejará de hacerlo | Formulario corto; se prueba en las entrevistas del guion A |
| **Desconfianza sobre la comida** | Quien recoge puede dudar de la calidad | Mostrar con claridad qué es, cuándo se preparó y hasta qué hora; se explora en el guion B |
| **Poca gente que recoja** | Sin demanda, el excedente no se rescata y la métrica baja | Empezar en un solo punto donde coincidan oferta y demanda, como una zona universitaria |
| **Normativa sanitaria** | Vender o regalar comida preparada puede tener reglas | El equipo no ha investigado la normativa aplicable; hay que consultarla antes de operar con comida real |
| **Datos simulados mal interpretados** | Las cifras de la sección 7 podrían confundirse con reales | Se rotulan como simuladas en todo el repositorio y en la presentación |

## 9. Coherencia con el resto del proyecto

| Parte del plan | Se relaciona con |
|---|---|
| Problema y métrica | [`ficha-de-trabajo.md`](ficha-de-trabajo.md) |
| Alternativas descartadas | [`alternativas.md`](alternativas.md) |
| Fuentes F1 a F13 | [`fuentes.md`](fuentes.md) |
| Supuestos de uso de cafeterías y de quien recoge | Entrevistas de [`investigacion/`](investigacion/) |
