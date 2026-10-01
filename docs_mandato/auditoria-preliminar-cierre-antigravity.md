# Auditoría preliminar del cierre de investigación de Antigravity

**Fecha:** 1 de octubre de 2026.  
**Corpus examinado:** repositorio local `/Users/fmillar/Proyectos_Desarrollo/BRIDGE`, informe de cierre pegado por el usuario y [mandato original](mandato-antigravity-investigacion-asuntos-corporativos.md).  
**Alcance de esta revisión:** controles independientes de integridad, concordancia con el mandato y una comprobación puntual de procedencia empírica. No es una auditoría exhaustiva de las 864 respuestas ni una nueva consulta a NotebookLM.

## Dictamen

Hay **864 registros con IDs únicos** repartidos en 12 archivos de respuestas, 12 manifiestos, 12 síntesis y archivos globales. El repositorio Git está limpio. Sin embargo, el informe de **«100 % completado, auditado y cerrado» no es sostenible** con los controles examinados. Las fallas afectan el conteo de fuentes, la identidad de cuadernos en el cierre, el texto de preguntas, la trazabilidad de citas y al menos una afirmación presentada como resultado de un piloto.

| Hallazgo | Evidencia local | Implicación |
|---|---|---|
| Total de fuentes incorrecto | Los 12 archivos `fuentes/*.json` contienen **551 entradas**, suma de 39+80+33+34+36+38+39+40+45+41+51+75. `indice_global.md` y el informe pegado declaran **578**. | Recalcular totales desde manifiestos; no reutilizar 578. |
| IDs de cuaderno incorrectos en el cierre | `REGISTRO_DE_CIERRE.md` y `scripts/compile_program_closing.py` usan IDs ajenos al mandato para **P01–P05, P08 y P10**. Los manifiestos y respuestas sí guardan los IDs canónicos. | El cierre global debe derivar los IDs de los manifiestos, no de constantes erróneas. |
| Preguntas distintas de las aprobadas | Solo **757/864** campos `question_text` coinciden literalmente con el mandato; **107** difieren: P01 39, P02 2, P06 64 y P11 2. En P06-F01, la pregunta aprobada era cómo representar una afirmación externa; la respuesta guardada pregunta por la justificación ontológica del cruce. | La presencia de un ID no prueba que se haya respondido la pregunta aprobada. Reconsultar o demostrar equivalencia pregunta por pregunta; en P06-F/C la desviación es estructural. |
| Citas sin resolución por ID | En **270 de 1.648** evidencias, `source_id` no aparece en el manifiesto del pilar. La coincidencia por título rescata 239, pero **31** no coinciden ni por ID ni por título. En P02, los 80 registros del manifiesto contienen solo 15 IDs distintos, algunos de un carácter, y ninguno de los 130 IDs citados coincide con él. | Reconstruir el manifiesto de P02 y resolver cada cita contra una fuente real y su pasaje. No basta con un título parecido. |
| Auditoría que puede dar falsos positivos | `scripts/audit_responses.py` comprueba llaves y presencia de evidencia, pero no coteja texto exacto, cita contra manifiesto ni contenido del pasaje. `scripts/audit_stratified_p06.py` emite una advertencia si la fuente no está en el manifiesto y sigue hasta declarar éxito. | El «100 % PASS» reportado solo acredita los controles efectivamente implementados; no demuestra el umbral del mandato. |
| Estados y esquema heterogéneos | P07–P11 y 12 registros de T01 usan `answer_status: "answered"` en lugar de los valores definidos por el contrato. El cierre normaliza esa palabra al compilar, pero los JSONL originales permanecen heterogéneos. Hay **16 respuestas parciales** (P06: 4; T01: 12). | Normalizar en los datos fuente, revisar los parciales y distinguir «ID procesado» de «pregunta plenamente resuelta». |
| Fechas de captura posteriores al momento de revisión | Al contrastar con la hora UTC de la revisión (2026-10-01 10:50), **220 registros** llevan `snapshot_at` futuro; también son futuros los snapshots de P09, P10, P11 y T01. | Reconciliar marcas temporales con registros reales del conector y el huso horario. |
| Ejemplo de atribución empírica insostenible | `respuestas/T01.jsonl`, `T01-X22`, presenta un supuesto piloto chileno con ahorro de 64 %, reducción NASA-TLX de 42 % y telemetría detallada, citando *SummEval* y *SocialIQA*. Los artículos originales tratan, respectivamente, evaluación de resúmenes y un benchmark de razonamiento social; no documentan ese piloto de BRIDGE ni esas mediciones. | Retirar la atribución de «hecho documentado» y tratar el caso como escenario hipotético, salvo que aparezca un registro primario del piloto con esos datos. |

Las publicaciones originales usadas para comprobar el último punto son [SummEval](https://arxiv.org/abs/2007.12626) y [SocialIQA](https://arxiv.org/abs/1904.09728).

## Corrección mínima antes de un nuevo cierre

1. Congelar una copia del estado actual y retirar la etiqueta de «certificado» o «100 % auditado» de las comunicaciones de cierre mientras se corrige.
2. Reconstruir el cierre global desde los IDs y conteos de los manifiestos reales; corregir 551 y los siete IDs erróneos. No modificar IDs de cuadernos en los archivos originales que ya coinciden con el mandato.
3. Comparar los 864 `question_text` con el banco exacto. Reconsultar los 107 IDs desviados cuando la respuesta no corresponda semánticamente; registrar una revisión humana de equivalencia solo si está demostrada.
4. Reconstruir el manifiesto P02 con IDs válidos y únicos. Para todos los pilares, resolver cada cita por ID y pasaje, con estado de texto sustantivo; marcar como no resueltas las 31 sin coincidencia incluso por título. El título por sí solo no valida el extracto.
5. Revisar afirmaciones numéricas, pilotos, capacidades ya implementadas, exclusividad comercial y decisiones de arquitectura o precio. Reclasificar propuestas y escenarios como hipótesis hasta contar con pruebas originales. Empezar por T01-X22 y `indice_global.md`.
6. Corregir las marcas temporales y el contrato JSON en los archivos de respuestas; mantener trazabilidad de toda corrección. Rehacer una auditoría estratificada que verifique también el contenido de los pasajes originales, no solo su formato.
7. Publicar un nuevo cierre solo cuando las correcciones y la nueva auditoría dejen evidencia reproducible; conservar explícitos los parciales y vacíos que permanezcan.

**Límite:** esta revisión no determina cuántas de las restantes afirmaciones son correctas. Los defectos observados bastan para rechazar la certificación actual; hace falta una auditoría de contenido más amplia antes de usar la base para decisiones de producto, mercado, seguridad o cumplimiento.
