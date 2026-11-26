# Plan de negocios y análisis de viabilidad: Segunda Mesa

> Borrador v2. Fuentes y precios consultados el 26 de noviembre de 2026. Todas las cifras tienen fuente citada o cálculo mostrado.
>
> **Qué es real y qué es simulado:** el prototipo funciona de verdad, pero los lotes, reservas y nombres que muestra son datos de prueba. Nada aquí demuestra reducción de desperdicio en una cafetería real.

---

## 1. Problema

Al cierre, una cafetería suele tener alimento que no se vendió. La persona encargada del cierre detecta los sobrantes tarde, tiene poco tiempo para encontrar quién los recoja y el aviso suele llegar incompleto, sin cantidad ni horario de recogida.

**Contexto con fuente (no es medición de nuestra comunidad):**

| Dato | Fuente | Nota |
|---|---|---|
| Se desperdician alrededor de 20.4 millones de toneladas de alimentos al año en México, equivalentes al 34% de la producción nacional. | Expansión Política, 30-sep-2025, que lo atribuye a la FAO [F1]. | Otras fuentes atribuyen la misma cifra a un estudio del Banco Mundial de 2017 [F2][F3]. |
| En 2022 el mundo desperdició 1,050 millones de toneladas de alimentos, cerca del 19% de los disponibles para consumidores. | PNUMA, Índice de Desperdicio de Alimentos 2024 [F4]. | Dato mundial. |
| De ese total, 60% vino de hogares, 28% de servicios de alimentación y 12% del comercio minorista. | PNUMA 2024 [F4][F5]. | El 28% de servicios de alimentación es el segmento más cercano a una cafetería. |

## 2. Mercado objetivo y segmentos

Es un mercado de dos lados:

| Lado | Quién es | Qué gana |
|---|---|---|
| **Oferta** (quien publica) | Encargada o encargado del cierre de una cafetería. | Colocar el excedente en minutos, con cantidad y hora límite claras. |
| **Demanda** (quien recoge) | Personas y grupos cercanos a la cafetería: estudiantes, vecinos y organizaciones comunitarias. | Acceder a alimento disponible, a tiempo y sin intermediarios. |

**Segmento inicial:** una cafetería piloto y un grupo de recolección cercano, para operar el flujo completo antes de sumar más negocios.

## 3. Propuesta de valor

- **Para la cafetería:** pasar de un aviso informal e incompleto a una publicación estructurada (alimento, cantidad, unidad, lugar, responsable, hora límite). La IA propone los campos desde una nota libre y la persona confirma antes de publicar.
- **Para quien recoge:** ver lo disponible con cuenta regresiva, reservar una cantidad y que el sistema no permita reservar más de lo que existe.
- **Para ambos:** la diferencia no recogida vuelve a estar disponible, y el resumen mide por unidad (no suma piezas con litros).

## 4. Competidores y alternativas existentes

| Alternativa | Qué hace | Lo que se sabe (con fuente) | Diferencia frente a Segunda Mesa |
|---|---|---|---|
| **Cheaf** (app mexicana) | Marketplace de "paquetes sorpresa" de panaderías, cafeterías, restaurantes y supermercados, con pago en la app. | El Cronista reporta presencia consolidada en ciudades como CDMX, Guadalajara, Monterrey, Puebla, Querétaro y Toluca, y unos 2.7 millones de usuarios en México [F6]. Forbes Argentina reporta descuentos de 50% a 65% [F7]. | Competidor directo más fuerte. Vende un paquete sorpresa con pago; Segunda Mesa publica un lote específico con cantidad exacta y recolección coordinada, y puede operar en zonas fuera de las ciudades que Cheaf lista. |
| **Too Good To Go** | Marketplace global de "Packs Sorpresa" con excedentes. | Sitio oficial en español [F8]. En la consulta de fuentes no encontré evidencia de que opere en México. | Mismo modelo de paquete sorpresa con pago. |
| **Olio y Geev** | Compartir o regalar comida entre particulares, con mensajería. | Listadas como apps contra el desperdicio por Grupo Animal [F9]. | Orientadas a particulares, no al cierre de un negocio con hora límite. |
| **Red de Bancos de Alimentos de México (BAMX)** | Rescate institucional de alimento para poblaciones en necesidad. | Alcance nacional [F10]. | Red institucional con logística propia; Segunda Mesa cubre el excedente pequeño del mismo día. |
| **Avisos informales por mensajería** | Avisar "sobró esto" en un grupo. | Alternativa habitual; no hay fuente que mida su uso. | Sin control de cantidades, reservas ni vencimiento. |

## 5. Diferenciador

Lo que distingue al prototipo, según lo que está construido:

1. Publicar desde una **nota libre** con IA que solo propone; la persona confirma.
2. **Hora límite calculada por código**, no por la IA.
3. **Reserva con control de cantidad** y devolución de la diferencia no recogida.
4. **Métricas por unidad**, separando publicado, reservado sin recoger, recogido y expirado sin rescate.
5. **Costo de operación mínimo** (sección 7), que permite una tarifa baja para el negocio.

Estas ventajas son de proceso, no de escala. Frente a un competidor con millones de usuarios, la estrategia es operar donde ese competidor no reporta presencia y con un modelo de lote específico en lugar de paquete sorpresa.

## 6. Modelo de ingresos

**Modelo elegido: suscripción mensual de la cafetería.** La persona que recoge no paga. El prototipo hoy no cobra; este modelo no requiere pasarela de pagos, así que se puede activar sin cambiar el flujo.

**Tarifa propuesta: $199 MXN por cafetería al mes.** Es una decisión de diseño del equipo, calculada para quedar muy por encima del costo de servir a una cafetería ($4.43 MXN al mes, sección 7).

**Fórmula:**

```
Ingreso mensual = N_cafeterías × $199
Margen mensual  = Ingreso mensual − costos (sección 7)
```

**Punto de equilibrio:** el costo fijo es $143 MXN al mes y cada cafetería deja $199 − $4.43 = $194.57. Entonces $143 / $194.57 = 0.73, es decir, **una sola cafetería cubre la infraestructura**.

**Escenarios (aritmética de la fórmula, no pronósticos):**

| Cafeterías | Ingreso mensual | Costo mensual | Margen mensual | Porcentaje de las 75,497 cafeterías del país [F14] |
|---|---|---|---|---|
| 5 | $995 | $165 | $830 | 0.007% |
| 10 | $1,990 | $187 | $1,803 | 0.013% |
| 25 | $4,975 | $254 | $4,721 | 0.033% |
| 50 | $9,950 | $364 | $9,586 | 0.066% |

Cifras en pesos mexicanos, redondeadas al peso.

## 7. Costos principales

Tipo de cambio de referencia: **$19.70 MXN por dólar**, del 26-nov-2026 [F15]. Si el tipo de cambio cambia, se recalcula multiplicando los montos en dólares.

| Costo | Precio oficial | Cálculo | Costo mensual |
|---|---|---|---|
| **Hosting del backend** (Render, plan Starter, 512 MB, siempre activo) | $7 USD al mes [F12] | $7 × 19.70 | $137.90 MXN |
| **Disco persistente** para la base SQLite (1 GB) | $0.25 USD por GB al mes [F12] | $0.25 × 19.70 | $4.93 MXN |
| **Subtotal de infraestructura fija** | | | **$142.83 MXN** |
| **IA (Gemini), por cafetería** | $1.50 USD por millón de tokens de entrada y $7.50 por millón de salida (precio estándar desde el 1-ene-2027) [F13] | Ver abajo | **$4.43 MXN** |
| **Dominio** | La URL gratuita del hosting alcanza para el piloto | | $0 |
| **Adquisición de usuarios** | Visitas en persona y boca a boca en el piloto | | $0 |
| **Tiempo del equipo** | Proyecto académico, sin facturación | | $0 |

**Por qué el plan Starter:** el plan gratuito de Render no permite adjuntar disco persistente y se apaga tras 15 minutos de inactividad [F12], lo que borraría la base SQLite y haría lenta la demo.

**Cálculo del costo de IA** (parámetros: una llamada usa 1,000 tokens de entrada y 300 de salida; una cafetería hace 30 interpretaciones de nota y 30 resúmenes al mes, es decir, 60 llamadas):

```
Costo por llamada = (1,000 / 1,000,000 × $1.50) + (300 / 1,000,000 × $7.50)
                  = $0.0015 + $0.00225 = $0.00375 USD
Costo mensual     = 60 × $0.00375 = $0.225 USD = $4.43 MXN
```

Hasta el 31-dic-2026 el precio introductorio es la mitad ($0.75 y $3.75) [F13], así que el cálculo anterior es el escenario más caro. Además, la API tiene un nivel gratuito para desarrollo; en ese nivel Google puede usar los datos para mejorar sus productos [F13], por eso en operación con usuarios reales conviene el nivel de pago.

**Costo de infraestructura al año:** $142.83 × 12 = $1,714 MXN.

## 8. Adquisición de usuarios

1. **Oferta:** visita directa a una cafetería cercana, mostrando el flujo en vivo con la nota libre y la publicación en minutos.
2. **Demanda:** un grupo de recolección cercano a esa cafetería (estudiantes, vecinos u organización comunitaria).
3. **Crecimiento:** recomendación entre cafeterías de la misma zona, una vez que el piloto muestre lotes publicados y recogidos.

Costo monetario en el piloto: $0 (sección 7).

## 9. Tamaño de mercado y crecimiento

**Mercado total:** Milenio, citando datos del INEGI, reporta **75,497 cafeterías o establecimientos con café como producto principal** en México [F14]. Los estados con más son Estado de México (10,840), Ciudad de México (9,166), Jalisco (5,687), Guanajuato (4,262) y Puebla (3,970) [F14].

**Mercado inicial:** la zona del piloto, con una cafetería y un grupo de recolección. Los escenarios de la sección 6 muestran el ingreso de 5 a 50 cafeterías, que representan entre 0.007% y 0.066% del total nacional.

**Crecimiento por etapas:**

1. Piloto con una cafetería y un grupo de recolección.
2. Cinco a diez cafeterías de la misma zona.
3. Otras zonas y otros negocios con excedente diario (panaderías, comedores).

## 10. Viabilidad

| Dimensión | Evaluación | Respaldo |
|---|---|---|
| **Técnica** | Viable: el flujo principal funciona de principio a fin. | Repositorio y prueba rápida del README. |
| **Económica** | Viable en costos: una cafetería cubre la infraestructura. | Secciones 6 y 7. |
| **Competitiva** | Exigente: hay un competidor consolidado, por eso se apunta a zonas sin cobertura reportada. | Sección 4. |
| **De uso** | Se valida en el piloto con tarea, tiempo y errores. | README, limitaciones. |
| **Legal y de inocuidad** | El sistema no valida que el alimento sea apto; eso queda en la persona responsable y en las condiciones de manejo acordadas con el negocio. Existen leyes estatales de recuperación de alimentos, por ejemplo en el Estado de México [F11]. | README. |

## 11. Riesgos y mitigación

| Riesgo | Mitigación |
|---|---|
| Competidor consolidado (Cheaf). | Operar en zonas sin cobertura reportada y con lote específico. |
| La cafetería no tiene suficiente excedente o no quiere publicarlo; una nota periodística llama "finita" a la oferta de excedentes en el sector [F6]. | Empezar con una cafetería y medir lotes reales antes de sumar más. |
| Dos lados del mercado: sin quien recoja no hay valor para quien publica. | Comenzar con un grupo de recolección definido. |
| Inocuidad del alimento. | Condiciones de manejo por escrito con la cafetería y aviso de responsabilidad. |
| La tarifa de $199 es una propuesta de diseño aún no probada con cafeterías. | Ajustarla con la operación del piloto; el punto de equilibrio con una cafetería deja margen amplio. |
| Dependencia del servicio de IA. | El formulario manual siempre funciona. |
| Datos personales (nombres escritos a mano, sin inicio de sesión). | Recolectar solo lo necesario y usar el nivel de pago de la API [F13]. |
| Tipo de cambio y cambios de precio de proveedores. | Recalcular con el factor de la sección 7. |

## 12. Próximos pasos

1. Elegir la cafetería piloto y el grupo de recolección.
2. Desplegar el backend en el plan Starter con disco de 1 GB (sección 7).
3. Probar el flujo con personas nuevas, sin instrucciones, y registrar tiempo, errores y tareas completadas.
4. Registrar el motivo por el que un lote no se recoge.
5. Revisar la norma de recuperación de alimentos aplicable en el estado.
6. Activar la suscripción cuando el piloto tenga lotes publicados y recogidos.

---

## Fuentes

Consultadas el 26 de noviembre de 2026.

- **[F1]** Expansión Política, "FAO: México desperdicia cada año 20.4 millones de toneladas de alimentos", 30-sep-2025. https://politica.expansion.mx/mexico/2025/09/30/fao-mexico-desperdicia-cada-ano-20-4-millones-de-toneladas-de-alimentos
- **[F2]** Publimetro, "Desperdicio de alimentos en México: costo y consecuencias", 9-nov-2026 (atribuye la cifra al Banco Mundial, 2017). https://www.publimetro.com.mx/nacional/2026/11/09/desperdicio-de-alimentos-mexico-costo-consecuencias/
- **[F3]** Blog del BID (misma cifra, atribuida al Banco Mundial). https://blogs.iadb.org/innovacion/es/?p=3035
- **[F4]** PNUMA, Informe sobre el Índice de Desperdicio de Alimentos 2024, mensajes clave. https://wedocs.unep.org/bitstream/handle/20.500.11822/45275/Food-Waste-Index-2024-key-messages_SP.pdf?sequence=2
- **[F5]** PNUMA, comunicado de prensa, 27-mar-2024. https://www.unep.org/es/noticias-y-reportajes/comunicado-de-prensa/el-mundo-desperdicia-mas-de-1000-millones-de-platos-de
- **[F6]** El Cronista, "El plan de Cheaf para dominar el rescate de alimentos en México". https://www.cronista.com/mexico/finanzas-economia/el-plan-de-cheaf-para-dominar-el-rescate-de-alimentos-en-mexico-supermercados-y-el-reto-de-la-oferta-finita/
- **[F7]** Forbes Argentina, "Qué es Cheaf, la app de rescate de alimentos que desembarca en la Argentina". https://www.forbesargentina.com/negocios/que-cheaf-app-rescate-alimentos-desembarca-argentina-n67383/amp
- **[F8]** Too Good To Go, sitio oficial en español. https://toogoodtogo.com/es
- **[F9]** Grupo Animal, "Las mejores apps para evitar el desperdicio de comida". https://grupoanimal.mx/gastronomia/tips/las-mejores-apps-para-evitar-el-desperdicio-de-comida
- **[F10]** Red BAMX. https://bamx.org.mx/
- **[F11]** Ley para la Recuperación y Aprovechamiento de Alimentos del Estado de México. https://www.ecatepec.gob.mx/websiteecatepec/public/documents/ley_reglamento/mRWgDCwfIyt9tLuv.pdf
- **[F12]** Render, precios oficiales: plan Starter $7 al mes, discos a $0.25 por GB al mes, plan gratuito sin disco y con apagado por inactividad. https://render.com/pricing.md · https://docs.render.com/free
- **[F13]** Google, precios de la API de Gemini y de modelos Flash: $0.75 y $3.75 por millón de tokens (entrada y salida) hasta el 31-dic-2026, y $1.50 y $7.50 desde el 1-ene-2027; nivel gratuito con uso de datos para mejorar productos. https://ai.google.dev/gemini-api/docs/pricing · https://cloud.google.com/model-garden/pricing
- **[F14]** Milenio, "Cafeterías, opción de emprendedores en pospandemia" (datos del INEGI). https://www.milenio.com/negocios/cafeterias-opcion-de-emprendedores-en-pospandemia
- **[F15]** El Comercio, "Precio del dólar en México hoy, jueves 26 de noviembre de 2026" (cita a Banxico: $19.7040 por dólar). https://elcomercio.pe/mag/respuestas/mx/precio-del-dolar-en-mexico-hoy-jueves-26-de-noviembre-de-2026-tipo-de-cambio-usd-a-mxn-cuanto-vale-y-cotizacion-de-banxico-fix-nnda-nnrt-noticia/

## Registro de cálculo de cifras

| Cifra | Cálculo o fuente |
|---|---|
| $137.90 MXN de hosting | $7 USD × 19.70 [F12][F15] |
| $4.93 MXN de disco | $0.25 USD × 19.70 [F12][F15] |
| $142.83 MXN de infraestructura fija | 137.90 + 4.93 |
| $0.00375 USD por llamada de IA | 1,000/1,000,000 × 1.50 + 300/1,000,000 × 7.50 [F13] |
| $4.43 MXN de IA por cafetería al mes | 60 × 0.00375 × 19.70 |
| $194.57 MXN de contribución por cafetería | 199 − 4.43 |
| 0.73 cafeterías de equilibrio | 142.83 / 194.57 |
| $1,714 MXN de infraestructura al año | 142.83 × 12 |
| Costo mensual con N cafeterías | 142.83 + 4.43 × N |
| Porcentaje del mercado | N / 75,497 [F14] |
