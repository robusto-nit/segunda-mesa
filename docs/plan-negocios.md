# Plan de negocios y análisis de viabilidad: Segunda Mesa

> **Estado del documento:** borrador v1. Fuentes consultadas el 26 de noviembre de 2026.
>
> **Regla de este documento:** toda cifra tiene una fuente citada o muestra su cálculo y supuestos. Donde todavía no hay dato, dice **[POR COMPLETAR]** y explica cómo obtenerlo. No hay cifras estimadas "a ojo".
>
> **Qué es real y qué es simulado:** el prototipo funciona de verdad, pero todos los lotes, reservas y nombres que muestra son datos de prueba. Nada aquí demuestra reducción de desperdicio en una cafetería real.

---

## 1. Problema

Al cierre, una cafetería suele tener alimento que no se vendió. Nuestra hipótesis (aún por verificar con evidencia propia, ver `investigacion.md`) es que la persona encargada del cierre detecta los sobrantes tarde, tiene poco tiempo para encontrar quién los recoja y el aviso llega incompleto, sin cantidad ni horario.

**Contexto con fuente (no es medición de nuestra comunidad):**

| Dato | Fuente | Nota importante |
|---|---|---|
| Se desperdician alrededor de 20.4 millones de toneladas de alimentos al año en México, equivalentes al 34% de la producción nacional. | Expansión Política, 30-sep-2025, que lo atribuye a la FAO [F1]. | Otras fuentes atribuyen esta misma cifra a un estudio del Banco Mundial de 2017 [F2][F3]. Conviene citarla como "20.4 millones de toneladas, según Expansión citando a la FAO; cifra que también se rastrea al Banco Mundial (2017)". |
| En 2022 el mundo desperdició 1,050 millones de toneladas de alimentos, cerca del 19% de los alimentos disponibles para consumidores. | PNUMA, Índice de Desperdicio de Alimentos 2024 [F4]. | Dato mundial, no de México. |
| De ese total, 60% vino de hogares, 28% de servicios de alimentación y 12% del comercio minorista. | PNUMA 2024 [F4][F5]. | El 28% de "servicios de alimentación" es el segmento más cercano a una cafetería. |

**Lo que estas cifras NO dicen:** cuánto sobra en una cafetería concreta ni cuánto de eso sería recuperable. Ese dato lo tiene que producir el equipo (ver sección 9).

## 2. Mercado objetivo y segmentos

Es un mercado de dos lados:

| Lado | Quién es | Qué ganaría | Estado |
|---|---|---|---|
| **Oferta (quien publica)** | Encargada o encargado del cierre de una cafetería. | Colocar el excedente en minutos, con cantidad y hora límite claras. | Hipótesis. **[POR COMPLETAR]** entrevistas. |
| **Demanda (quien recoge)** | Persona o grupo que aprovecha el excedente. Segmentos candidatos: estudiantes, comedores o fundaciones, vecinos. | Acceder a alimento disponible, a tiempo y sin intermediarios. | Hipótesis. **[POR COMPLETAR]** definir cuál segmento priorizar y por qué. |

**Segmento inicial propuesto:** una sola cafetería piloto y un solo grupo de recolección, para aprender antes de escalar. **[POR COMPLETAR]** nombre del tipo de cafetería y cómo se eligió.

## 3. Propuesta de valor

- **Para la cafetería:** pasar de un aviso informal e incompleto a una publicación estructurada (alimento, cantidad, unidad, lugar, responsable, hora límite). La IA propone los campos desde una nota libre y la persona confirma antes de publicar.
- **Para quien recoge:** ver lo disponible con cuenta regresiva, reservar una cantidad y que el sistema no permita reservar más de lo que existe.
- **Para ambos:** la diferencia no recogida vuelve a estar disponible, y el resumen mide por unidad (no suma piezas con litros).

## 4. Competidores y alternativas existentes

Verificado en fuentes públicas el 26-nov-2026. **[POR COMPLETAR]** confirmar cuáles operan en la ciudad del equipo.

| Alternativa | Qué hace | Lo que se sabe (con fuente) | Diferencia frente a Segunda Mesa |
|---|---|---|---|
| **Cheaf** (app mexicana de rescate de excedentes) | Marketplace de "paquetes sorpresa" de panaderías, cafeterías, restaurantes y supermercados, con pago en la app. | Una nota de El Cronista reporta presencia en CDMX, Guadalajara, Monterrey, Puebla, Querétaro y Toluca, y unos 2.7 millones de usuarios en México [F6]. Reporta descuentos de 50% a 65% [F7]. | Es el competidor directo más fuerte. Su modelo es venta de paquete sorpresa con pago; el nuestro es publicar un lote específico con cantidad exacta y recolección coordinada. **[POR COMPLETAR]** si opera en nuestra ciudad. |
| **Too Good To Go** | Marketplace global de "Packs Sorpresa" con excedentes de negocios. | Opera en varios países y tiene sitio en español [F8]. **No pude confirmar que opere en México**; verificar en la app. | Mismo modelo de paquete sorpresa con pago. |
| **Apps de intercambio entre personas (Olio, Geev)** | Compartir o regalar comida entre particulares, con mensajería. | Listadas como apps contra el desperdicio en una nota de Grupo Animal [F9]. | Orientadas a particulares, no al cierre de un negocio con hora límite. |
| **Red de Bancos de Alimentos de México (BAMX)** | Rescate institucional de alimento para distribuirlo a poblaciones en necesidad. | Tiene alcance nacional; su reporte anual y su sitio están en bamx.org.mx [F10]. | Es una red institucional con logística propia. Segunda Mesa apunta a un excedente pequeño y del mismo día, que a una red grande puede no convenirle recoger. **[POR VERIFICAR]** con entrevista. |
| **Grupos de WhatsApp o redes sociales (informal)** | Avisar "sobró esto" en un grupo. | Es una hipótesis nuestra, sin fuente. **[POR COMPLETAR]** confirmarla en entrevistas. | Sin estructura: no controla cantidades, ni reservas, ni vencimiento. |

## 5. Diferenciador (a validar, no asumir)

Lo que hoy distingue al prototipo, según lo que sí está construido:

1. Publicar desde una **nota libre** con IA que solo propone; la persona confirma.
2. **Hora límite calculada por código**, no por la IA.
3. **Reserva con control de cantidad** y devolución de la diferencia no recogida.
4. **Métricas por unidad** y distinción entre publicado, reservado sin recoger, recogido y expirado sin rescate.
5. Pendiente de construir: registrar el **motivo por el que un lote no se recoge**.

**Riesgo honesto:** estas ventajas son de proceso, no de mercado. Ante un competidor con millones de usuarios y presencia en varias ciudades, el diferenciador solo se sostiene si las entrevistas muestran un hueco real (por ejemplo, ciudades donde no operan, o negocios que prefieren donar o coordinar en lugar de vender paquetes). **[POR COMPLETAR]**

## 6. Modelo de ingresos (opciones, aún sin decidir)

El prototipo **no tiene precios ni pagos**, así que hoy no genera ingresos. Opciones a evaluar; ninguna lleva cifra hasta tener respaldo:

| Opción | Cómo cobraría | Qué hay que averiguar antes de poner un número |
|---|---|---|
| A. Suscripción de la cafetería | Cuota periódica por usar la plataforma. | Disposición a pagar de las cafeterías (entrevistas). |
| B. Comisión por lote recuperado | Porcentaje sobre ventas. Requiere incorporar pagos, que hoy no existen. | Que el modelo sea de venta y no de donación; costo de pasarela de pagos. |
| C. Patrocinio o convenio institucional | Universidad, municipio o fundación financia la operación. | Quién tiene presupuesto y qué métrica de impacto le pediría. |
| D. Modelo social sin cobro | Operación subsidiada, impacto como objetivo principal. | Quién cubre los costos. |

**Cómo se calculará cualquier ingreso** (fórmula; las variables se llenan solo con datos con fuente):

```
Ingreso mensual = N_cafeterías_activas × tarifa_mensual
N_cafeterías_activas = N_cafeterías_en_la_zona × tasa_de_adopción
```

- `N_cafeterías_en_la_zona`: conteo del DENUE de INEGI para la zona, con fecha de consulta. **[POR COMPLETAR]**
- `tasa_de_adopción` y `tarifa_mensual`: salen de entrevistas o de una prueba piloto, no de supuestos. **[POR COMPLETAR]**

## 7. Costos principales

Categorías identificadas a partir de la arquitectura real. Los montos se toman de las páginas oficiales de precios y se anota la fecha de consulta.

| Costo | Por qué existe | Cómo se calculará | Estado |
|---|---|---|---|
| Uso de la API de Gemini | Interpretar notas y redactar observaciones del resumen. | Costo por llamada según precio oficial de Google AI × publicaciones esperadas por mes. | **[POR COMPLETAR]** con precio oficial vigente. |
| Hosting del backend y la base de datos | Hoy corre en local con SQLite; en producción necesitaría servidor. | Precio oficial del proveedor elegido. | **[POR COMPLETAR]** |
| Dominio y mantenimiento | Operar de forma continua. | Precio del proveedor. | **[POR COMPLETAR]** |
| Pagos (solo si se elige la opción B) | Pasarela de cobro. | Comisión publicada por el proveedor. | No aplica en el MVP. |
| Adquisición de usuarios | Llegar a cafeterías y a quien recoge. | Según canal elegido (sección 8). | **[POR COMPLETAR]** |
| Tiempo del equipo | Desarrollo y operación. | Horas × tarifa; declarar el supuesto. | **[POR COMPLETAR]** |

## 8. Adquisición de usuarios

Enfoque: empezar con una cafetería piloto y expandir solo con evidencia.

1. **Oferta:** acercamiento directo a una cafetería (la misma donde se observe el cierre). Medir cuánto tardó en publicar sin instrucciones.
2. **Demanda:** un grupo concreto de recolección, definido en la sección 2.
3. **Canal de crecimiento:** boca a boca entre cafeterías cercanas, solo si el piloto funciona. **[POR COMPLETAR]** qué canal usarán y cómo medirán si funciona.

## 9. Tamaño de mercado y crecimiento

**Lo que se puede afirmar con fuente:** el desperdicio en México y en el mundo es grande (sección 1). Eso justifica el problema, **no mide nuestro mercado**.

**Cómo se estimará nuestro mercado (método):**

| Nivel | Definición | Cómo se obtiene |
|---|---|---|
| Mercado total | Cafeterías en la zona de interés. | Conteo DENUE (INEGI), con fecha de consulta. **[POR COMPLETAR]** |
| Mercado alcanzable | Cafeterías que tienen excedente al cierre. | Proporción observada en visitas y entrevistas; no suponerla. **[POR COMPLETAR]** |
| Mercado obtenible | Las que podamos atender en el primer año. | Capacidad real del equipo para visitar y dar soporte. **[POR COMPLETAR]** |

**Crecimiento por etapas, ligado a evidencia (no a porcentajes):**

1. Piloto con una cafetería y un grupo de recolección. Se pasa a la etapa 2 solo si hay publicaciones y recogidas reales.
2. Pocas cafeterías de la misma zona.
3. Otras zonas o tipos de negocio (panaderías, comedores), si la etapa 2 funciona.

## 10. Viabilidad

| Dimensión | Evaluación hoy | Respaldo |
|---|---|---|
| **Técnica** | Alta para un prototipo: el flujo principal funciona de principio a fin. | Código del repositorio y prueba rápida del README. |
| **De uso** | Desconocida. No se ha probado con usuarios reales. | README, sección de limitaciones. **[POR COMPLETAR]** pruebas de tarea, tiempo y errores. |
| **Económica** | Desconocida. No hay precios ni costos validados. | Secciones 6 y 7. |
| **Competitiva** | Incierta: hay un competidor consolidado en México. | Sección 4. |
| **Legal y de inocuidad** | Pendiente. El sistema no valida que el alimento sea apto; eso queda en la persona responsable y en las condiciones acordadas con el negocio. | README. Existen leyes estatales de recuperación de alimentos, por ejemplo en el Estado de México [F11]. **[POR COMPLETAR]** revisar si hay norma aplicable en el estado del equipo. |

## 11. Riesgos y mitigación

| Riesgo | Mitigación propuesta |
|---|---|
| Competidor consolidado (Cheaf) con muchos usuarios. | Validar un hueco concreto (zona o tipo de negocio) antes de invertir; no competir de frente. |
| La cafetería no tiene suficiente excedente o no quiere publicarlo. Una nota periodística menciona la oferta "finita" de excedentes como reto del sector [F6]. | Medir excedente real en el piloto antes de proyectar. |
| Dos lados del mercado: sin quien recoja, no hay valor para quien publica, y viceversa. | Comenzar con un grupo de recolección ya identificado. |
| Riesgo de inocuidad: alguien consume un alimento en mal estado. | Definir por escrito condiciones de manejo con la cafetería; mensajes claros de responsabilidad. |
| Dependencia de un servicio externo de IA. | El formulario manual siempre funciona; la IA es opcional. |
| Datos personales (nombres escritos a mano, sin inicio de sesión). | No recolectar más de lo necesario; definir política antes de operar con usuarios reales. |
| Conclusiones basadas en datos de prueba. | Mantener la advertencia de que las tasas del resumen describen solo datos simulados. |

## 12. Próximos pasos

1. Observar cierres reales y entrevistar a 3 a 5 personas con distintos roles. Guardar en `investigacion.md`.
2. Confirmar qué competidores operan en la ciudad del equipo y actualizar la sección 4.
3. Decidir el modelo de ingresos (sección 6) con base en las entrevistas.
4. Cotizar costos con precios oficiales y fecha de consulta (sección 7).
5. Obtener el conteo DENUE y completar el método de la sección 9.
6. Probar el flujo con usuarios sin instrucciones y registrar tiempo, errores y tareas completadas.
7. Revisar la norma aplicable de recuperación de alimentos en el estado.

---

## Fuentes

Consultadas el 26 de noviembre de 2026.

- **[F1]** Expansión Política, "FAO: México desperdicia cada año 20.4 millones de toneladas de alimentos", 30-sep-2025. https://politica.expansion.mx/mexico/2025/09/30/fao-mexico-desperdicia-cada-ano-20-4-millones-de-toneladas-de-alimentos
- **[F2]** Publimetro, "Desperdicio de alimentos en México: costo y consecuencias", 9-nov-2026. Atribuye la cifra a un estudio del Banco Mundial de 2017. https://www.publimetro.com.mx/nacional/2026/11/09/desperdicio-de-alimentos-mexico-costo-consecuencias/
- **[F3]** Blog del BID, atribuye la misma cifra al Banco Mundial. https://blogs.iadb.org/innovacion/es/?p=3035
- **[F4]** PNUMA, "Informe sobre el Índice de Desperdicio de Alimentos 2024", mensajes clave. https://wedocs.unep.org/bitstream/handle/20.500.11822/45275/Food-Waste-Index-2024-key-messages_SP.pdf?sequence=2
- **[F5]** PNUMA, comunicado de prensa, 27-mar-2024. https://www.unep.org/es/noticias-y-reportajes/comunicado-de-prensa/el-mundo-desperdicia-mas-de-1000-millones-de-platos-de
- **[F6]** El Cronista, "El plan de Cheaf para dominar el rescate de alimentos en México". https://www.cronista.com/mexico/finanzas-economia/el-plan-de-cheaf-para-dominar-el-rescate-de-alimentos-en-mexico-supermercados-y-el-reto-de-la-oferta-finita/
- **[F7]** Forbes Argentina, "Qué es Cheaf, la app de rescate de alimentos que desembarca en la Argentina". https://www.forbesargentina.com/negocios/que-cheaf-app-rescate-alimentos-desembarca-argentina-n67383/amp
- **[F8]** Too Good To Go, sitio oficial en español. https://toogoodtogo.com/es
- **[F9]** Grupo Animal, "Las mejores apps para evitar el desperdicio de comida". https://grupoanimal.mx/gastronomia/tips/las-mejores-apps-para-evitar-el-desperdicio-de-comida
- **[F10]** Red BAMX, sitio oficial: https://bamx.org.mx/
- **[F11]** Documento de la Ley para la Recuperación y Aprovechamiento de Alimentos del Estado de México (texto de referencia). https://www.ecatepec.gob.mx/websiteecatepec/public/documents/ley_reglamento/mRWgDCwfIyt9tLuv.pdf

## Registro de verificación de cifras

| Cifra usada | Dónde aparece | Fuente | ¿Verificada? |
|---|---|---|---|
| 20.4 millones de toneladas, 34% de la producción | Sección 1 | F1, y F2/F3 sobre el origen | Sí, con la salvedad de atribución |
| 1,050 millones de toneladas, 19%, 60/28/12% | Sección 1 | F4, F5 | Sí |
| 2.7 millones de usuarios de Cheaf en México; ciudades | Sección 4 | F6 | Sí, es dato reportado por la empresa vía prensa |
| Descuentos de 50% a 65% | Sección 4 | F7 | Sí, en el contexto de una nota sobre Argentina |
| Cualquier otra cifra de mercado, ingreso o costo | — | — | **No hay.** Se completan con las fórmulas de las secciones 6, 7 y 9. |
