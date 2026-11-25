# Ficha de trabajo: investigación y validación

**Proyecto:** Segunda Mesa · **Responsable:** Persona 3 (investigación y validación)
**Última actualización:** 24 de noviembre de 2026

## 1. Problema

Al cierre del día, una cafetería puede tener alimentos que sobran y todavía se pueden aprovechar, pero no cuenta con una forma rápida y ordenada de avisar a alguien que los recoja. Si el aviso no llega a tiempo, esos alimentos terminan desperdiciados.

**Por qué importa** (datos secundarios; detalle en [`fuentes.md`](fuentes.md)):

- En 2022 se desperdiciaron en el mundo 1,05 mil millones de toneladas de alimentos (F1).
- Los servicios de alimentos, como restaurantes y cafeterías, generaron 28 % de ese desperdicio, unos 290 millones de toneladas (F1, F2). Los datos de este sector son escasos (F1).
- En México se estiman más de 30 millones de toneladas al año (F4); otra fuente cita 20,4 millones (F5). Las cifras difieren por metodología.

**Alcance del proyecto:**

- **Incluye:** excedentes de alimentos que una cafetería tiene al cierre, y su aprovechamiento por una persona que los reserve y los recoja.
- **No incluye:** el desperdicio en hogares, en la producción agrícola ni en el resto de la cadena de alimentos.

## 2. Usuarios

| Usuario | Qué hace en el flujo | Qué necesitamos saber de él |
|---|---|---|
| Persona de la cafetería | Registra el excedente (alimento, cantidad, unidad y horario) y confirma lo recogido | Qué sobra, a qué hora se sabe y cuánto tiempo puede dedicar a registrarlo |
| Persona que recoge | Consulta lo disponible, reserva una cantidad y lo recoge | Qué información necesita para decidir, qué horarios le sirven y qué le da confianza |

La cafetería del proyecto es **ficticia**. Por eso los dos usuarios se estudian entrevistando a **personas reales** con experiencia parecida, con el guion de [`investigacion/guion-entrevistas.md`](investigacion/guion-entrevistas.md).

## 3. Evidencia

| Tipo de dato | Significado | Qué hay en el proyecto | Dónde está |
|---|---|---|---|
| **Secundario** | Lo publicó otra organización | Cifras de desperdicio mundial y de México | [`fuentes.md`](fuentes.md) |
| **Observado** | Lo vimos o nos lo dijeron directamente | Entrevistas y observaciones de 3 a 5 personas | Carpeta `investigacion/`, una nota por entrevista |
| **Estimado** | Lo calcula alguien con base en otros datos, explicando cómo | Cantidades que las personas entrevistadas calculan de memoria | Notas de `investigacion/`, marcadas como estimadas |
| **Simulado** | Inventado a propósito para la demostración | La cafetería ficticia y sus excedentes de prueba | Base de datos y capturas de la demo, etiquetados como simulados |

**Regla del equipo:** ningún dato simulado se presenta como real, ni en el README ni en la presentación.

## 4. Métrica principal

**Tasa de rescate**

> Tasa de rescate = cantidad recogida y confirmada ÷ cantidad registrada como excedente × 100

- **Qué mide:** qué parte de lo que la cafetería avisa que le sobra realmente llega a una persona que lo aprovecha.
- **Cómo se obtiene:** con los pasos 1 y 4 del flujo (registrar el excedente y confirmar lo recogido), así que la plataforma puede calcularla sola.
- **Unidad:** se calcula con la misma unidad con que se registró (porciones, piezas o kilogramos), sin mezclar unidades distintas.
- **Ejemplo simulado:** si en un día de prueba se registran 20 porciones y se confirman 15 como recogidas, la tasa de rescate es 75 %. Este número es de ejemplo.
- **En la demostración** los valores son simulados y así se indica.

## 5. Coherencia con la página web

| Paso del flujo mínimo | Qué investigación lo respalda |
|---|---|
| 1. La cafetería registra un excedente | Guion A, preguntas 3, 4 y 7: qué sobra, a qué hora y cuánto tiempo toma registrar |
| 2. La persona consulta y reserva | Guion B, preguntas 3 y 7: qué información necesita y si prefiere reservar |
| 3. El sistema actualiza la disponibilidad | [`alternativas.md`](alternativas.md): el criterio de control de lo disponible |
| 4. Se confirma lo recogido y se consulta el resumen | Métrica principal (sección 4) |

## 6. Próxima acción

Realizar de 3 a 5 entrevistas con el guion de [`investigacion/guion-entrevistas.md`](investigacion/guion-entrevistas.md), registrar cada una con [`investigacion/plantilla-nota.md`](investigacion/plantilla-nota.md) y, con lo observado, revisar si cambian el problema, los usuarios, el flujo o la métrica de esta ficha.
