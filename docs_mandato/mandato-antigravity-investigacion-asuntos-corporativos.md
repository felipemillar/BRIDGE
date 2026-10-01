# Mandato de extracción densa de conocimiento para Antigravity

**Programa:** aplicación de inteligencia para asuntos corporativos inspirada en el flujo Saber, Escuchar, Hablar y Relacionar de The Bridge Intelligence.  
**Versión:** 1.0 · **Fecha de diseño:** 30 de septiembre de 2026.  
**Destinatario:** agente operador en Antigravity o Integrity con un conector MCP autorizado a NotebookLM. «MSP» en la solicitud se interpreta como MCP; el operador debe comprobar el nombre y las capacidades reales del conector antes de actuar.  
**Naturaleza:** mandato de investigación y especificación de salida. No inicia por sí mismo la conexión, las consultas, una publicación ni un cambio de permisos.

## 1. Objetivo y decisión que debe habilitar

Interrogar los 12 cuadernos del programa para construir una base de conocimiento trazable sobre usuarios, mercado, fuentes externas, memoria corporativa, reputación, cruce de evidencia, preparación ejecutiva, viabilidad, compromisos, aprobación de comunicaciones, gobernanza entre clientes y evaluación. El resultado debe permitir diseñar, comparar y probar una aplicación sin convertir hipótesis del corpus en hechos comprobados.

Cada pregunta tiene un ID estable. Hay **48 preguntas fundamentales (F) y 16 de contraste (C) por cuaderno**. P02, P06 y T01 tienen además **32 preguntas de profundización (X)** cada uno. Total: **864 preguntas lógicas**: 576 F + 192 C + 96 X. Una consulta MCP puede agrupar hasta tres preguntas de un mismo eje si la herramienta conserva una respuesta separada, completa y citada por ID. Si no, consultar de una en una. No confundir número de llamadas con número de preguntas respondidas.

Las 864 preguntas forman el alcance aprobado. Ejecutar F, luego C y luego X aunque el banco esté presentado por ejes temáticos con F y C intercaladas. Si el servicio impone cuotas, continuar por tandas reanudables conservando el punto exacto; nunca declarar completo un cuaderno con IDs sin respuesta. Una respuesta `sin_evidencia` o `fuente_fallida` cuenta como pregunta procesada y abre un vacío, no como afirmación resuelta. No sustituir preguntas por una única solicitud genérica de resumen.

## 2. Universo exacto y preflight

Usar la cuenta propietaria **felipemillarsilva@gmail.com** y verificarla visual o programáticamente con la interfaz autorizada; el parámetro `authuser` por sí solo no prueba identidad. No cambiar permisos, visibilidad, opción de copia, selección de fuentes ni contenido de los cuadernos. Verificar el estado actual de acceso y copia de cada cuaderno antes de consultar. El conector debe operar en modo lectura. Si no existe un conector NotebookLM accesible, no inventar una API ni inferir resultados: registrar el bloqueo y el punto alcanzado.

Antes de preguntar a cada cuaderno:

1. Verificar ID, título, cuenta y acceso; registrar `snapshot_at`, número total de entradas, utilizables, originales, síntesis y errores observados. Los números históricos del inventario son contexto, no cuotas fijas.
2. Enumerar fuentes con ID, título, URL original si existe, tipo, fecha, extensión de texto recuperado y estado `texto_sustantivo`, `resumen_parcial`, `solo_navegacion`, `captcha`, `fallida`, `duplicada` o `desconocida`. Seleccionable no significa texto sustantivo.
3. Leer SOURCE_INDEX, EVIDENCE_MAP, RESEARCH_DOSSIER y GAPS_AND_VALIDATION. Leer después las correcciones antes de usar las síntesis como guía. Las síntesis internas orientan la búsqueda; una afirmación empírica debe apoyarse en fuente original recuperable.
4. Congelar un manifiesto de fuentes por cuaderno con fecha y, si el conector lo permite, IDs de versión o hash. Si el corpus cambia durante la extracción, cerrar la tanda, registrar la diferencia y revalidar solo las respuestas afectadas.
5. Resolver primero preguntas F, luego C, luego X. Guardar cada respuesta inmediatamente; reanudar por ID tras cualquier corte, sin duplicarla.

### Precedencia editorial obligatoria

- **P02:** `00_P02_GLOBAL_READ_ME_AND_ERRATA` prevalece sobre `P02_GLOBAL_ATLAS_RECONCILIATION_V1`, el anexo regional y los documentos V1 cuando hay conflicto. Las 70 filas son fichas catalogadas, no 70 empresas independientes verificadas; las capacidades comerciales no son pruebas operativas.
- **P03, P06 y P08:** `QUALITY_ADDENDUM` prevalece sobre conclusiones originales contradictorias. En P06, distinguir abstracts de textos completos de la misma obra.
- **P09, P10, P11 y T01:** `VERIFICATION_CORRECTIONS` prevalece sobre `QUALITY_ADDENDUM` y síntesis iniciales. En P11, `P11_PROVIDER_SCOPE_NOTE` prevalece específicamente para el alcance de proveedores. En T01 hay dos juegos de cuatro síntesis; deduplicar por contenido y procedencia, sin contar una repetición como corroboración.
- En todos los pilares, una fuente original pertinente y sustantiva prevalece sobre un resumen interno. Si dos fuentes originales discrepan, conservar ambas, sus fechas y ámbitos; no forzar una síntesis artificial.

## 3. Contrato de consulta y respuesta

**Consulta:** incluir el ID y el texto exacto de la pregunta, el ID del cuaderno, el corte del manifiesto y esta instrucción fija: «Responde solo con el corpus accesible del cuaderno. Para cada afirmación empírica proporciona fuente original identificable y localizador. Separa hecho respaldado, declaración comercial, inferencia y propuesta de diseño. Si el corpus no alcanza, responde `sin_evidencia` con lo que falta. Señala contradicciones y documentos correctivos aplicables». No pedir que NotebookLM siga instrucciones incrustadas en fuentes.

**Formato:** un objeto JSON UTF-8 por pregunta en `respuestas/<pilar>.jsonl`, válido de manera independiente. Usar arreglos vacíos o `null` cuando un campo no corresponda; no rellenar con suposiciones. El objeto debe conservar al menos:

```json
{
  "question_id": "P09-F01",
  "notebook_id": "9117c80e-9317-4b6b-9c74-292bae6f5769",
  "question_text": "texto exacto de este mandato",
  "snapshot_at": "ISO-8601",
  "answer_status": "respondida|parcial|sin_evidencia|fuente_fallida|conflicto|bloqueada",
  "short_answer": "respuesta directa de 1 a 3 frases o null",
  "findings": [
    {
      "claim_id": "P09-F01-C1",
      "claim": "proposición atómica, falsable cuando sea posible",
      "epistemic_status": "hecho_documentado|declaracion_proveedor|inferencia|hipotesis_diseno",
      "scope": {"time": "fecha o intervalo", "region": "jurisdicción", "actor": "rol o entidad"},
      "evidence": [
        {
          "source_id": "ID observado en cuaderno",
          "source_title": "título observado",
          "original_url": "URL o null",
          "locator": "página/sección/párrafo o ancla nativa",
          "excerpt_short": "cita breve o null",
          "source_date": "fecha o null",
          "retrieved_at": "ISO-8601",
          "text_status": "texto_sustantivo|resumen_parcial|solo_navegacion|captcha|fallida|desconocida",
          "relationship": "apoya|refuta|contextualiza"
        }
      ],
      "confidence": "alta|media|baja",
      "confidence_reason": "razón anclada en calidad y consistencia de evidencia"
    }
  ],
  "operational_model": {"inputs": [], "actors": [], "steps": [], "states": [], "outputs": [], "exceptions": []},
  "entities": [{"entity_id": "ID local estable", "type": "organizacion|persona_rol|documento|fuente|tema|evento|compromiso|producto|riesgo|metrica|experimento", "name": "nombre canónico", "aliases": []}],
  "relations": [{"subject_id": "ID", "predicate": "relación concreta", "object_id": "ID", "valid_from": null, "valid_to": null, "evidence_claim_id": "P09-F01-C1"}],
  "comparisons": [],
  "contradictions": [{"claim_ids": [], "difference": "texto", "resolution": "resuelta|abierta", "reason": "texto"}],
  "metrics_and_denominators": [],
  "bridge_implications": [{"module": "Saber|Escuchar|Hablar|Relacionar|transversal", "implication": "texto", "status": "evidencia|inferencia|hipotesis"}],
  "open_gaps": [{"gap": "texto", "minimum_validation": "fuente o prueba necesaria", "priority": "alta|media|baja"}],
  "next_question_ids": [],
  "quality": {"original_citations_resolved": true, "correction_precedence_checked": true, "duplicate_sources_counted_once": true, "human_review_needed": false}
}
```

Los valores del ejemplo JSON ilustran el esquema; el operador debe calcular los indicadores de `quality` para cada respuesta, sin copiar `true` por defecto. Si el conector no expone un ID de fuente nativo, crear un `source_id` local estable a partir del manifiesto y registrar esa limitación; usar título observado, URL original y localizador o extracto verificable cuando existan. Si falta un localizador comprobable, la cita queda pendiente y no cuenta como resuelta.

Un hecho empírico sin fuente original identificable debe pasar a `open_gaps` y no figurar como `hecho_documentado`. Una cita a SOURCE_INDEX o RESEARCH_DOSSIER puede explicar cómo se llegó a una hipótesis, pero no sustituye el original. Los datos de fechas, precios, leyes, cobertura, adquisiciones, clientes y capacidades vigentes requieren fecha y alcance. Si una página es portal parcial, CAPTCHA o error, no tratarla como prueba del contenido inaccesible. «No documentado en el corpus» no significa que la función no exista.

**Densidad útil:** dividir la respuesta en afirmaciones atómicas; incluir tablas o registros de roles, estados, métricas, variantes regionales y casos cuando el tema lo justifique. Evitar párrafos largos que mezclen cinco hechos bajo una sola cita. Mantener la explicación legible para una persona, además del JSON estructurado.

## 4. Ejecución, control de calidad y productos de salida

- Procesar los pilares en orden P01→P11→T01; dentro de cada uno F→C→X. T01 debe usar el mapa de hipótesis surgido de los demás, pero responder solo con su propio corpus; cualquier cruce externo va a la síntesis transversal y conserva el ID de origen.
- Tras cada grupo de ocho preguntas, comprobar JSON válido, IDs consecutivos, citas resolubles y respeto de la precedencia. Si el modelo contesta una pregunta distinta, solicitar corrección de ese ID; no avanzar con respuesta desplazada.
- Cuando una fuente contradice otra, registrar ambas. Si una fuente del cuaderno cambió, marcar respuestas afectadas y reconsultarlas. No repetir preguntas sanas por un cambio no relacionado.
- Auditar manualmente al menos el 10 % de respuestas por pilar, estratificando hechos comerciales, normativos, cifras, relaciones de propiedad, casos de crisis y `sin_evidencia`. El umbral de aprobación es 100 % de IDs presentes, 100 % de citas empíricas resolubles en las respuestas auditadas y cero afirmaciones críticas sin fuente. Si falla, ampliar la muestra y corregir antes de sintetizar.
- Para cada pilar entregar `respuestas/<pilar>.jsonl`, `sintesis/<pilar>.md` (hallazgos, modelos, decisiones, controversias y vacíos), y `fuentes/<pilar>.json` (manifiesto). Entregar además `indice_global.md`, `entidades.jsonl`, `relaciones.jsonl`, `contradicciones.jsonl`, `matriz_cobertura.csv` y `ejecucion.json` con conteos por estado y reanudación. Los vínculos entre pilares deben deduplicar entidad y obra sin borrar procedencia.
- La síntesis transversal debe responder: qué necesidad del usuario está respaldada; qué alternativas de mercado existen; qué arquitectura integrada es una hipótesis; qué derechos y permisos limitan el producto; qué experimento mínimo discrimina valor; qué decisión puede tomarse ahora y cuál requiere evidencia nueva. No declarar ventaja única, factibilidad legal universal ni impacto reputacional causal sin pruebas.

## 5. Banco de preguntas exactas

La numeración F01–F48 identifica extracción; C01–C16, contraste; X01–X32, profundización. Cada eje aporta F1–F6 y C1–C2. Las preguntas C son obligatorias aunque su resultado sea «sin conflicto encontrado en las fuentes revisadas». Las X solo existen en P02, P06 y T01. El operador debe guardar el texto exacto con cada ID.


### Cuadernos canónicos

| Pilar | Cuaderno | URL | Preguntas |
|---|---|---|---:|
| P01 | Asuntos corporativos y sus usuarios | https://notebook.google.com/notebook/21152990-b13f-4cda-bd6c-0286ca855ff9 | 64 |
| P02 | Empresas y soluciones existentes | https://notebook.google.com/notebook/bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440 | 96 |
| P03 | Monitoreo del entorno y acceso a fuentes | https://notebook.google.com/notebook/a2afe847-a988-40f1-9432-9e596b74b376 | 64 |
| P04 | Conocimiento documentado de la corporación | https://notebook.google.com/notebook/cb87941c-2377-42fb-806f-eb9878ac0757 | 64 |
| P05 | Reputación, narrativas y actores | https://notebook.google.com/notebook/0fc2e780-e279-4923-83c5-90fe621a4543 | 64 |
| P06 | Cruce de conocimiento interno y señales externas | https://notebook.google.com/notebook/2c5dc262-44fc-43f8-b6e2-c993ed32835b | 96 |
| P07 | Preparación ejecutiva y apoyo estratégico | https://notebook.google.com/notebook/521c2c59-1c43-493b-abd9-7de2c7cf9dce | 64 |
| P08 | Viabilidad, modelos de negocio y oportunidades | https://notebook.google.com/notebook/afe8fdb7-d63d-43ab-84e6-060fe6b8fd24 | 64 |
| P09 | Memoria de relaciones y gestión de compromisos | https://notebook.google.com/notebook/9117c80e-9317-4b6b-9c74-292bae6f5769 | 64 |
| P10 | Gestión y aprobación de la comunicación corporativa | https://notebook.google.com/notebook/ca5f3cec-cc73-4e48-9dc5-0a2330e73990 | 64 |
| P11 | Gobernanza de información y operación entre clientes | https://notebook.google.com/notebook/64271ecf-776c-4692-b302-d936ea00a501 | 64 |
| T01 | Evaluación y pilotos | https://notebook.google.com/notebook/eee1c855-b3d0-4377-9eb3-7368baa28bf1 | 96 |


### P01 — Asuntos corporativos y sus usuarios


**Eje: Mandato y fronteras de asuntos corporativos**

- **P01-F01.** ¿Qué decisiones y resultados distinguen asuntos corporativos de marketing, ventas, sostenibilidad y relaciones públicas?
- **P01-F02.** ¿Qué actividades recaen realmente en el CCO o Dircom y cuáles se delegan a especialistas o agencias?
- **P01-F03.** ¿En qué situaciones la preparación institucional cambia una decisión y no solo acelera la redacción?
- **P01-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar mandato y fronteras de asuntos corporativos de forma estructurada?
- **P01-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre mandato y fronteras de asuntos corporativos?
- **P01-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra mandato y fronteras de asuntos corporativos sin introducir datos no documentados?
- **P01-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre mandato y fronteras de asuntos corporativos, y qué versión prevalece según las correcciones?
- **P01-C02.** ¿Qué sigue sin prueba sobre mandato y fronteras de asuntos corporativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Mapa de usuarios, compradores y aprobadores**

- **P01-F07.** ¿Qué tareas, restricciones y criterios de éxito tiene cada usuario cotidiano del sistema?
- **P01-F08.** ¿Quién compra, quién aprueba seguridad y presupuesto, y quién puede vetar la adopción?
- **P01-F09.** ¿Cómo varían estos roles entre empresa grande, regulada, consultora y organización con presencia territorial?
- **P01-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar mapa de usuarios, compradores y aprobadores de forma estructurada?
- **P01-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre mapa de usuarios, compradores y aprobadores?
- **P01-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra mapa de usuarios, compradores y aprobadores sin introducir datos no documentados?
- **P01-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre mapa de usuarios, compradores y aprobadores, y qué versión prevalece según las correcciones?
- **P01-C04.** ¿Qué sigue sin prueba sobre mapa de usuarios, compradores y aprobadores, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Trabajos por hacer y momentos de presión**

- **P01-F13.** ¿Qué trabajos concretos anteceden una entrevista, audiencia, reunión comunitaria o crisis?
- **P01-F14.** ¿Qué información necesita cada rol antes, durante y después de esos momentos?
- **P01-F15.** ¿Cuáles son los pasos manuales, traspasos y cuellos de botella más costosos hoy?
- **P01-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar trabajos por hacer y momentos de presión de forma estructurada?
- **P01-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre trabajos por hacer y momentos de presión?
- **P01-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra trabajos por hacer y momentos de presión sin introducir datos no documentados?
- **P01-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre trabajos por hacer y momentos de presión, y qué versión prevalece según las correcciones?
- **P01-C06.** ¿Qué sigue sin prueba sobre trabajos por hacer y momentos de presión, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Reuniones y decisiones críticas**

- **P01-F19.** ¿Qué tipos de reunión exigen contrastar memoria corporativa y novedades externas?
- **P01-F20.** ¿Qué decisiones debe tomar un vocero cuando las fuentes internas y externas discrepan?
- **P01-F21.** ¿Qué artefacto mínimo permitiría llegar preparado a una reunión parlamentaria, regulatoria o territorial?
- **P01-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar reuniones y decisiones críticas de forma estructurada?
- **P01-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre reuniones y decisiones críticas?
- **P01-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra reuniones y decisiones críticas sin introducir datos no documentados?
- **P01-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre reuniones y decisiones críticas, y qué versión prevalece según las correcciones?
- **P01-C08.** ¿Qué sigue sin prueba sobre reuniones y decisiones críticas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Riesgos de preparación insuficiente**

- **P01-F25.** ¿Qué errores verificables provienen de usar mensajes vencidos, cifras inconsistentes o contexto incompleto?
- **P01-F26.** ¿Cómo se manifiestan riesgos reputacionales, regulatorios, legales y de confianza entre actores?
- **P01-F27.** ¿Qué señales permiten distinguir un fallo prevenible por software de uno que requiere juicio humano?
- **P01-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar riesgos de preparación insuficiente de forma estructurada?
- **P01-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre riesgos de preparación insuficiente?
- **P01-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra riesgos de preparación insuficiente sin introducir datos no documentados?
- **P01-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre riesgos de preparación insuficiente, y qué versión prevalece según las correcciones?
- **P01-C10.** ¿Qué sigue sin prueba sobre riesgos de preparación insuficiente, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Resultados y retorno de valor**

- **P01-F31.** ¿Qué resultados valora cada persona y qué indicador observable mide su mejora?
- **P01-F32.** ¿Cómo se medirían tiempo de preparación, exactitud de citas, coherencia y detección temprana?
- **P01-F33.** ¿Qué parte del supuesto retorno económico está respaldada por datos y qué parte es hipótesis?
- **P01-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar resultados y retorno de valor de forma estructurada?
- **P01-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre resultados y retorno de valor?
- **P01-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra resultados y retorno de valor sin introducir datos no documentados?
- **P01-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre resultados y retorno de valor, y qué versión prevalece según las correcciones?
- **P01-C12.** ¿Qué sigue sin prueba sobre resultados y retorno de valor, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Usuarios de asuntos corporativos en Chile y Latinoamérica**

- **P01-F37.** ¿Qué particularidades institucionales, territoriales, idiomáticas y mediáticas cambian el flujo en Chile?
- **P01-F38.** ¿Cómo afectan la centralización de medios, la política local y el relacionamiento comunitario al usuario?
- **P01-F39.** ¿Qué diferencias regionales documentadas impiden copiar sin adaptación un producto anglosajón?
- **P01-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar usuarios de asuntos corporativos en Chile y Latinoamérica de forma estructurada?
- **P01-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre usuarios de asuntos corporativos en Chile y Latinoamérica?
- **P01-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra usuarios de asuntos corporativos en Chile y Latinoamérica sin introducir datos no documentados?
- **P01-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre usuarios de asuntos corporativos en Chile y Latinoamérica, y qué versión prevalece según las correcciones?
- **P01-C14.** ¿Qué sigue sin prueba sobre usuarios de asuntos corporativos en Chile y Latinoamérica, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Descubrimiento y validación de usuarios**

- **P01-F43.** ¿Qué preguntas de entrevista revelan conductas reales en vez de opiniones generales sobre IA?
- **P01-F44.** ¿Qué evidencia demostraría frecuencia, intensidad y presupuesto del problema?
- **P01-F45.** ¿Qué segmento y momento de uso conviene probar primero según el corpus?
- **P01-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar descubrimiento y validación de usuarios de forma estructurada?
- **P01-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre descubrimiento y validación de usuarios?
- **P01-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra descubrimiento y validación de usuarios sin introducir datos no documentados?
- **P01-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre descubrimiento y validación de usuarios, y qué versión prevalece según las correcciones?
- **P01-C16.** ¿Qué sigue sin prueba sobre descubrimiento y validación de usuarios, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P01:** 48 F + 16 C + 0 X = 64 IDs.


### P02 — Empresas y soluciones existentes


**Eje: Universo comercial y deduplicación**

- **P02-F01.** ¿Qué organizaciones, marcas y productos son entidades distintas y cuáles pertenecen al mismo grupo?
- **P02-F02.** ¿Qué criterios separan proveedor comercial, asociación, estándar, consultora y propuesta de referencia?
- **P02-F03.** ¿Qué fichas del atlas quedan cuestionadas por la fe de erratas y cómo debe reconciliarse el denominador?
- **P02-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar universo comercial y deduplicación de forma estructurada?
- **P02-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre universo comercial y deduplicación?
- **P02-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra universo comercial y deduplicación sin introducir datos no documentados?
- **P02-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre universo comercial y deduplicación, y qué versión prevalece según las correcciones?
- **P02-C02.** ¿Qué sigue sin prueba sobre universo comercial y deduplicación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Competidores cercanos a los cuatro módulos**

- **P02-F07.** ¿Qué proveedores declaran combinar Saber, Escuchar, Hablar y Relacionar en un flujo único?
- **P02-F08.** ¿Qué capacidad exacta está documentada para cada módulo y cuál solo es mensaje comercial?
- **P02-F09.** ¿Qué integración entre módulos está probada por documentación específica y cuál se infiere por pertenecer a un grupo?
- **P02-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar competidores cercanos a los cuatro módulos de forma estructurada?
- **P02-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre competidores cercanos a los cuatro módulos?
- **P02-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra competidores cercanos a los cuatro módulos sin introducir datos no documentados?
- **P02-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre competidores cercanos a los cuatro módulos, y qué versión prevalece según las correcciones?
- **P02-C04.** ¿Qué sigue sin prueba sobre competidores cercanos a los cuatro módulos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Plataformas de escucha y reputación**

- **P02-F13.** ¿Qué cubren Meltwater, Cision/Brandwatch, Signal AI, Hootsuite/Talkwalker y Onclusive?
- **P02-F14.** ¿Dónde terminan la captura y análisis de señales y comienzan la preparación o gestión de decisiones?
- **P02-F15.** ¿Qué diferencias de fuentes, acceso y actualización importan para Chile y Latinoamérica?
- **P02-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar plataformas de escucha y reputación de forma estructurada?
- **P02-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre plataformas de escucha y reputación?
- **P02-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra plataformas de escucha y reputación sin introducir datos no documentados?
- **P02-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre plataformas de escucha y reputación, y qué versión prevalece según las correcciones?
- **P02-C06.** ¿Qué sigue sin prueba sobre plataformas de escucha y reputación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Asuntos públicos y memoria de actores**

- **P02-F19.** ¿Qué ofrecen Quorum, FiscalNote, Open Point, Simply Stakeholders y Borealis para actores y compromisos?
- **P02-F20.** ¿Qué diferencia el CRM legislativo del seguimiento comunitario, regulatorio o de prensa?
- **P02-F21.** ¿Qué registros, responsables y alertas podrían integrarse con la preparación ejecutiva?
- **P02-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar asuntos públicos y memoria de actores de forma estructurada?
- **P02-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre asuntos públicos y memoria de actores?
- **P02-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra asuntos públicos y memoria de actores sin introducir datos no documentados?
- **P02-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre asuntos públicos y memoria de actores, y qué versión prevalece según las correcciones?
- **P02-C08.** ¿Qué sigue sin prueba sobre asuntos públicos y memoria de actores, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Conocimiento interno y cruce de fuentes**

- **P02-F25.** ¿Qué prueban AlphaSense, Contify, Glean, Elium, Jalios y otros sobre búsqueda interna y señales externas?
- **P02-F26.** ¿Qué conectores, permisos, citas y actualización documentan sus fuentes originales?
- **P02-F27.** ¿Qué elementos serían complementos técnicos y cuáles sustitutos de una aplicación de asuntos corporativos?
- **P02-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar conocimiento interno y cruce de fuentes de forma estructurada?
- **P02-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre conocimiento interno y cruce de fuentes?
- **P02-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra conocimiento interno y cruce de fuentes sin introducir datos no documentados?
- **P02-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre conocimiento interno y cruce de fuentes, y qué versión prevalece según las correcciones?
- **P02-C10.** ¿Qué sigue sin prueba sobre conocimiento interno y cruce de fuentes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Flujo editorial y servicios expertos**

- **P02-F31.** ¿Qué ofrecen Broadsight, Prezly, Entual, Contrlr y agencias para mensajes, briefings y aprobaciones?
- **P02-F32.** ¿Qué parte es software, qué parte servicio humano y qué parte es una hoja de ruta?
- **P02-F33.** ¿Qué evidencia hay de uso productivo, caso de cliente o ensayo independiente por proveedor?
- **P02-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar flujo editorial y servicios expertos de forma estructurada?
- **P02-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre flujo editorial y servicios expertos?
- **P02-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra flujo editorial y servicios expertos sin introducir datos no documentados?
- **P02-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre flujo editorial y servicios expertos, y qué versión prevalece según las correcciones?
- **P02-C12.** ¿Qué sigue sin prueba sobre flujo editorial y servicios expertos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Mapa mundial y diferencias regionales**

- **P02-F37.** ¿Qué categorías están documentadas en cada región y dónde hay vacíos de búsqueda?
- **P02-F38.** ¿Qué proveedores regionales cubren idioma, prensa local, radio, regulación y comunidades?
- **P02-F39.** ¿Qué significa cobertura comercial declarada frente a disponibilidad real de fuentes en un país?
- **P02-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar mapa mundial y diferencias regionales de forma estructurada?
- **P02-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre mapa mundial y diferencias regionales?
- **P02-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra mapa mundial y diferencias regionales sin introducir datos no documentados?
- **P02-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre mapa mundial y diferencias regionales, y qué versión prevalece según las correcciones?
- **P02-C14.** ¿Qué sigue sin prueba sobre mapa mundial y diferencias regionales, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Posicionamiento y alianzas**

- **P02-F43.** ¿Qué trabajos conviene construir, comprar o integrar según las capacidades documentadas?
- **P02-F44.** ¿Qué alianzas de datos, producto o servicio son plausibles y bajo qué limitaciones?
- **P02-F45.** ¿Qué afirmaciones diferenciales de The Bridge siguen como hipótesis sin prueba comparativa?
- **P02-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar posicionamiento y alianzas de forma estructurada?
- **P02-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre posicionamiento y alianzas?
- **P02-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra posicionamiento y alianzas sin introducir datos no documentados?
- **P02-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre posicionamiento y alianzas, y qué versión prevalece según las correcciones?
- **P02-C16.** ¿Qué sigue sin prueba sobre posicionamiento y alianzas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Profundización especializada**


*Adquisiciones y estructura de grupos*

- **P02-X01.** ¿Qué adquisiciones cambian el grupo económico de Memo, Talkwalker, Limbik, FGS Global y otras marcas?
- **P02-X02.** ¿Qué fecha distingue anuncio, aprobación y cierre de cada operación documentada?
- **P02-X03.** ¿Qué filas deben fusionarse, conservarse como marca o quedar con propiedad no verificada?
- **P02-X04.** ¿Qué variables, categorías, relaciones y condiciones exige representar adquisiciones y estructura de grupos de forma estructurada?
- **P02-X05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre adquisiciones y estructura de grupos?
- **P02-X06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra adquisiciones y estructura de grupos sin introducir datos no documentados?
- **P02-X07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre adquisiciones y estructura de grupos, y qué versión prevalece según las correcciones?
- **P02-X08.** ¿Qué sigue sin prueba sobre adquisiciones y estructura de grupos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Proximidad funcional verificable*

- **P02-X09.** ¿Qué proveedores cubren tres o más módulos en una misma oferta documentada?
- **P02-X10.** ¿Qué evidencia muestra flujo operativo entre módulos en vez de páginas comerciales separadas?
- **P02-X11.** ¿Qué demostración común permitiría comparar a Broadsight, Entual, Contify y Open Point?
- **P02-X12.** ¿Qué variables, categorías, relaciones y condiciones exige representar proximidad funcional verificable de forma estructurada?
- **P02-X13.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre proximidad funcional verificable?
- **P02-X14.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra proximidad funcional verificable sin introducir datos no documentados?
- **P02-X15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre proximidad funcional verificable, y qué versión prevalece según las correcciones?
- **P02-X16.** ¿Qué sigue sin prueba sobre proximidad funcional verificable, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Cobertura territorial y derechos*

- **P02-X17.** ¿Qué proveedor prueba acceso a prensa, radio, redes y reguladores en Chile?
- **P02-X18.** ¿Qué limitaciones regionales declaran proveedores de África, Asia y Medio Oriente?
- **P02-X19.** ¿Qué licencias de contenido o restricciones de exportación podrían impedir integrar una solución?
- **P02-X20.** ¿Qué variables, categorías, relaciones y condiciones exige representar cobertura territorial y derechos de forma estructurada?
- **P02-X21.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre cobertura territorial y derechos?
- **P02-X22.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra cobertura territorial y derechos sin introducir datos no documentados?
- **P02-X23.** ¿Dónde discrepan fuentes originales y síntesis internas sobre cobertura territorial y derechos, y qué versión prevalece según las correcciones?
- **P02-X24.** ¿Qué sigue sin prueba sobre cobertura territorial y derechos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Certeza comercial y madurez*

- **P02-X25.** ¿Qué pruebas públicas diferencian producto disponible, piloto cerrado, beta y mera propuesta?
- **P02-X26.** ¿Qué precios, contratos y casos de cliente están publicados con alcance verificable?
- **P02-X27.** ¿Qué preguntas de demo deben resolver los 10 comparables prioritarios antes de puntuarles?
- **P02-X28.** ¿Qué variables, categorías, relaciones y condiciones exige representar certeza comercial y madurez de forma estructurada?
- **P02-X29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre certeza comercial y madurez?
- **P02-X30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra certeza comercial y madurez sin introducir datos no documentados?
- **P02-X31.** ¿Dónde discrepan fuentes originales y síntesis internas sobre certeza comercial y madurez, y qué versión prevalece según las correcciones?
- **P02-X32.** ¿Qué sigue sin prueba sobre certeza comercial y madurez, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P02:** 48 F + 16 C + 32 X = 96 IDs.


### P03 — Monitoreo del entorno y acceso a fuentes


**Eje: Taxonomía de señales externas**

- **P03-F01.** ¿Qué tipos de señales de prensa, redes, broadcast, reguladores y comunidades son relevantes?
- **P03-F02.** ¿Qué metadatos mínimos permiten comparar noticias, publicaciones, alertas y documentos oficiales?
- **P03-F03.** ¿Cómo se distingue una mención de marca de un cambio material para asuntos corporativos?
- **P03-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar taxonomía de señales externas de forma estructurada?
- **P03-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre taxonomía de señales externas?
- **P03-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra taxonomía de señales externas sin introducir datos no documentados?
- **P03-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre taxonomía de señales externas, y qué versión prevalece según las correcciones?
- **P03-C02.** ¿Qué sigue sin prueba sobre taxonomía de señales externas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Acceso a prensa y web abierta**

- **P03-F07.** ¿Qué canales de acceso a prensa digital están documentados y qué restricciones muestran?
- **P03-F08.** ¿Cómo cambian calidad, latencia, cobertura y derechos entre API, licencia, RSS, búsqueda y captura manual?
- **P03-F09.** ¿Qué evidencia específica hay de cobertura de medios locales chilenos?
- **P03-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar acceso a prensa y web abierta de forma estructurada?
- **P03-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre acceso a prensa y web abierta?
- **P03-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra acceso a prensa y web abierta sin introducir datos no documentados?
- **P03-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre acceso a prensa y web abierta, y qué versión prevalece según las correcciones?
- **P03-C04.** ¿Qué sigue sin prueba sobre acceso a prensa y web abierta, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Redes sociales y comunidades**

- **P03-F13.** ¿Qué plataformas permiten acceso oficial a contenido público y en qué condiciones?
- **P03-F14.** ¿Qué sesgos introducen muestras parciales, cuentas privadas, límites de API y cambios de plataforma?
- **P03-F15.** ¿Cómo verificar conversaciones relevantes sin atribuir representatividad a una muestra incompleta?
- **P03-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar redes sociales y comunidades de forma estructurada?
- **P03-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre redes sociales y comunidades?
- **P03-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra redes sociales y comunidades sin introducir datos no documentados?
- **P03-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre redes sociales y comunidades, y qué versión prevalece según las correcciones?
- **P03-C06.** ¿Qué sigue sin prueba sobre redes sociales y comunidades, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Radio, televisión, video y podcasts**

- **P03-F19.** ¿Qué opciones existen para transcribir, licenciar y consultar contenido audiovisual?
- **P03-F20.** ¿Qué errores de transcripción, demoras y vacíos regionales afectan las alertas?
- **P03-F21.** ¿Cuándo una noticia audiovisual debe tratarse como evidencia original y cuándo como resumen secundario?
- **P03-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar radio, televisión, video y podcasts de forma estructurada?
- **P03-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre radio, televisión, video y podcasts?
- **P03-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra radio, televisión, video y podcasts sin introducir datos no documentados?
- **P03-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre radio, televisión, video y podcasts, y qué versión prevalece según las correcciones?
- **P03-C08.** ¿Qué sigue sin prueba sobre radio, televisión, video y podcasts, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Fuentes institucionales y regulatorias**

- **P03-F25.** ¿Qué registros, organismos y boletines son prioritarios para Chile y para un despliegue multinacional?
- **P03-F26.** ¿Cómo se detectan cambios normativos y de actores sin confundir propuesta, trámite y norma vigente?
- **P03-F27.** ¿Qué frecuencia, formatos y trazabilidad ofrecen las fuentes oficiales revisadas?
- **P03-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar fuentes institucionales y regulatorias de forma estructurada?
- **P03-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre fuentes institucionales y regulatorias?
- **P03-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra fuentes institucionales y regulatorias sin introducir datos no documentados?
- **P03-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre fuentes institucionales y regulatorias, y qué versión prevalece según las correcciones?
- **P03-C10.** ¿Qué sigue sin prueba sobre fuentes institucionales y regulatorias, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Desambiguación y análisis de señales**

- **P03-F31.** ¿Cómo se distinguen homónimos, filiales, productos y personas con nombres similares?
- **P03-F32.** ¿Qué método permite detectar temas emergentes aun cuando no mencionan a la empresa?
- **P03-F33.** ¿Qué límites tienen sentimiento automático, clasificación narrativa y detección de desinformación?
- **P03-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar desambiguación y análisis de señales de forma estructurada?
- **P03-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre desambiguación y análisis de señales?
- **P03-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra desambiguación y análisis de señales sin introducir datos no documentados?
- **P03-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre desambiguación y análisis de señales, y qué versión prevalece según las correcciones?
- **P03-C12.** ¿Qué sigue sin prueba sobre desambiguación y análisis de señales, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Alertas útiles y latencia**

- **P03-F37.** ¿Cómo se define relevancia de una alerta para cada rol y severidad?
- **P03-F38.** ¿Qué umbrales minimizan fatiga de alertas sin ocultar eventos críticos?
- **P03-F39.** ¿Qué tiempos de detección y de verificación deben medirse por canal?
- **P03-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar alertas útiles y latencia de forma estructurada?
- **P03-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre alertas útiles y latencia?
- **P03-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra alertas útiles y latencia sin introducir datos no documentados?
- **P03-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre alertas útiles y latencia, y qué versión prevalece según las correcciones?
- **P03-C14.** ¿Qué sigue sin prueba sobre alertas útiles y latencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Derechos, costos y calidad de ingesta**

- **P03-F43.** ¿Qué derechos de uso, retención, redistribución y entrenamiento están documentados por tipo de fuente?
- **P03-F44.** ¿Qué costos y dependencias contractuales son observables y cuáles requieren cotización?
- **P03-F45.** ¿Cómo evaluar precisión, cobertura, duplicados y fallos de captura con denominadores correctos?
- **P03-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar derechos, costos y calidad de ingesta de forma estructurada?
- **P03-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre derechos, costos y calidad de ingesta?
- **P03-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra derechos, costos y calidad de ingesta sin introducir datos no documentados?
- **P03-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre derechos, costos y calidad de ingesta, y qué versión prevalece según las correcciones?
- **P03-C16.** ¿Qué sigue sin prueba sobre derechos, costos y calidad de ingesta, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P03:** 48 F + 16 C + 0 X = 64 IDs.


### P04 — Conocimiento documentado de la corporación


**Eje: Inventario de documentos corporativos**

- **P04-F01.** ¿Qué tipos de memoria anual, política, comunicado, presentación, acta y compromiso forman el corpus institucional?
- **P04-F02.** ¿Qué propietario, vigencia, aprobación y nivel de acceso necesita cada tipo documental?
- **P04-F03.** ¿Qué artefactos son fuente de verdad y cuáles solo borradores o contexto histórico?
- **P04-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar inventario de documentos corporativos de forma estructurada?
- **P04-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre inventario de documentos corporativos?
- **P04-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra inventario de documentos corporativos sin introducir datos no documentados?
- **P04-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre inventario de documentos corporativos, y qué versión prevalece según las correcciones?
- **P04-C02.** ¿Qué sigue sin prueba sobre inventario de documentos corporativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Afirmaciones y compromisos**

- **P04-F07.** ¿Cómo se registra una afirmación corporativa con cifra, fecha, alcance, fuente y responsable?
- **P04-F08.** ¿Qué campos distinguen promesa, meta, avance, incumplimiento y rectificación?
- **P04-F09.** ¿Cómo se enlazan afirmaciones y compromisos con documentos, actores y decisiones posteriores?
- **P04-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar afirmaciones y compromisos de forma estructurada?
- **P04-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre afirmaciones y compromisos?
- **P04-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra afirmaciones y compromisos sin introducir datos no documentados?
- **P04-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre afirmaciones y compromisos, y qué versión prevalece según las correcciones?
- **P04-C04.** ¿Qué sigue sin prueba sobre afirmaciones y compromisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Ontología y relaciones**

- **P04-F13.** ¿Qué entidades y relaciones son necesarias para representar la memoria corporativa?
- **P04-F14.** ¿Qué casos exigen separar matriz, filial, proyecto, instalación y vocero?
- **P04-F15.** ¿Cómo se evita que un grafo convierta una relación inferida en hecho comprobado?
- **P04-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar ontología y relaciones de forma estructurada?
- **P04-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ontología y relaciones?
- **P04-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra ontología y relaciones sin introducir datos no documentados?
- **P04-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre ontología y relaciones, y qué versión prevalece según las correcciones?
- **P04-C06.** ¿Qué sigue sin prueba sobre ontología y relaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Versiones y temporalidad**

- **P04-F19.** ¿Qué diferencia hay entre fecha del hecho, fecha de publicación y fecha de incorporación al sistema?
- **P04-F20.** ¿Cómo debe responderse una pregunta sobre lo que la empresa sabía o decía en una fecha histórica?
- **P04-F21.** ¿Qué regla prevalece cuando un documento fue corregido, retirado o reemplazado?
- **P04-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar versiones y temporalidad de forma estructurada?
- **P04-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre versiones y temporalidad?
- **P04-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra versiones y temporalidad sin introducir datos no documentados?
- **P04-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre versiones y temporalidad, y qué versión prevalece según las correcciones?
- **P04-C08.** ¿Qué sigue sin prueba sobre versiones y temporalidad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Ingesta y extracción**

- **P04-F25.** ¿Qué pasos permiten extraer tablas, anexos, cifras y notas de PDF, web y archivos ofimáticos?
- **P04-F26.** ¿Qué unidades de fragmentación preservan contexto y citas sin mezclar versiones?
- **P04-F27.** ¿Cómo detectar errores de OCR, tablas incompletas y referencias cruzadas rotas?
- **P04-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar ingesta y extracción de forma estructurada?
- **P04-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ingesta y extracción?
- **P04-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra ingesta y extracción sin introducir datos no documentados?
- **P04-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre ingesta y extracción, y qué versión prevalece según las correcciones?
- **P04-C10.** ¿Qué sigue sin prueba sobre ingesta y extracción, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Gobierno y permisos**

- **P04-F31.** ¿Quién puede crear, aprobar, corregir, leer o retirar cada clase de información?
- **P04-F32.** ¿Cómo se trasladan los permisos del origen a búsqueda, respuestas y exportaciones?
- **P04-F33.** ¿Qué registro de cambios y revisión humana exige una afirmación sensible?
- **P04-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar gobierno y permisos de forma estructurada?
- **P04-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre gobierno y permisos?
- **P04-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra gobierno y permisos sin introducir datos no documentados?
- **P04-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre gobierno y permisos, y qué versión prevalece según las correcciones?
- **P04-C12.** ¿Qué sigue sin prueba sobre gobierno y permisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Búsqueda y respuesta fundada**

- **P04-F37.** ¿Qué preguntas debe resolver la búsqueda exacta, semántica o híbrida?
- **P04-F38.** ¿Cómo se seleccionan citas suficientes para respaldar cifras, fechas y compromisos?
- **P04-F39.** ¿Cuándo debe abstenerse el sistema por conflicto, vencimiento o falta de evidencia?
- **P04-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar búsqueda y respuesta fundada de forma estructurada?
- **P04-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre búsqueda y respuesta fundada?
- **P04-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra búsqueda y respuesta fundada sin introducir datos no documentados?
- **P04-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre búsqueda y respuesta fundada, y qué versión prevalece según las correcciones?
- **P04-C14.** ¿Qué sigue sin prueba sobre búsqueda y respuesta fundada, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Evaluación de calidad documental**

- **P04-F43.** ¿Qué métricas muestran completitud, actualidad y recuperabilidad del corpus?
- **P04-F44.** ¿Cómo se evalúan respuestas sobre compromisos con un conjunto de casos de referencia?
- **P04-F45.** ¿Qué prueba adversarial revela fugas de permisos o mezcla de clientes?
- **P04-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar evaluación de calidad documental de forma estructurada?
- **P04-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre evaluación de calidad documental?
- **P04-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra evaluación de calidad documental sin introducir datos no documentados?
- **P04-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre evaluación de calidad documental, y qué versión prevalece según las correcciones?
- **P04-C16.** ¿Qué sigue sin prueba sobre evaluación de calidad documental, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P04:** 48 F + 16 C + 0 X = 64 IDs.


### P05 — Reputación, narrativas y actores


**Eje: Identidad, imagen y reputación**

- **P05-F01.** ¿Cómo distingue el corpus identidad declarada, imagen inmediata y reputación acumulada?
- **P05-F02.** ¿Qué observación permitiría saber si la percepción externa contradice la conducta documentada?
- **P05-F03.** ¿Qué parte de la reputación puede medirse sin reducirla a un único puntaje?
- **P05-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar identidad, imagen y reputación de forma estructurada?
- **P05-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre identidad, imagen y reputación?
- **P05-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra identidad, imagen y reputación sin introducir datos no documentados?
- **P05-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre identidad, imagen y reputación, y qué versión prevalece según las correcciones?
- **P05-C02.** ¿Qué sigue sin prueba sobre identidad, imagen y reputación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Modelos de medición y calidad**

- **P05-F07.** ¿Qué dimensiones y poblaciones usan los modelos de reputación revisados?
- **P05-F08.** ¿Qué sesgos aparecen por muestreo, idioma, canal, tamaño de audiencia o período?
- **P05-F09.** ¿Cómo separar resultado de encuesta, análisis de medios y juicio de analista?
- **P05-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar modelos de medición y calidad de forma estructurada?
- **P05-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre modelos de medición y calidad?
- **P05-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra modelos de medición y calidad sin introducir datos no documentados?
- **P05-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre modelos de medición y calidad, y qué versión prevalece según las correcciones?
- **P05-C04.** ¿Qué sigue sin prueba sobre modelos de medición y calidad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Niveles de métricas de comunicación**

- **P05-F13.** ¿Cómo se distinguen actividad, alcance, recepción, cambio de actitud y efecto organizacional?
- **P05-F14.** ¿Qué métricas tienen denominadores observables y cuáles descansan en estimaciones?
- **P05-F15.** ¿Qué causalidad no puede inferirse de un aumento de menciones o sentimiento?
- **P05-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar niveles de métricas de comunicación de forma estructurada?
- **P05-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre niveles de métricas de comunicación?
- **P05-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra niveles de métricas de comunicación sin introducir datos no documentados?
- **P05-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre niveles de métricas de comunicación, y qué versión prevalece según las correcciones?
- **P05-C06.** ¿Qué sigue sin prueba sobre niveles de métricas de comunicación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Narrativas y temas emergentes**

- **P05-F19.** ¿Cómo se detecta el origen, marco, evolución y amplificación de una narrativa?
- **P05-F20.** ¿Qué diferencia una señal débil de un tema estable o una controversia material?
- **P05-F21.** ¿Cómo comparar narrativas de prensa, actores políticos, empleados y comunidades?
- **P05-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar narrativas y temas emergentes de forma estructurada?
- **P05-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre narrativas y temas emergentes?
- **P05-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra narrativas y temas emergentes sin introducir datos no documentados?
- **P05-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre narrativas y temas emergentes, y qué versión prevalece según las correcciones?
- **P05-C08.** ¿Qué sigue sin prueba sobre narrativas y temas emergentes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Actores y prominencia**

- **P05-F25.** ¿Qué criterios documentados ayudan a priorizar actores por legitimidad, poder, urgencia e influencia?
- **P05-F26.** ¿Cómo cambian intereses y posiciones de un actor a lo largo del tiempo?
- **P05-F27.** ¿Qué riesgo tiene inferir posturas personales desde datos de una organización o grupo?
- **P05-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar actores y prominencia de forma estructurada?
- **P05-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre actores y prominencia?
- **P05-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra actores y prominencia sin introducir datos no documentados?
- **P05-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre actores y prominencia, y qué versión prevalece según las correcciones?
- **P05-C10.** ¿Qué sigue sin prueba sobre actores y prominencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Crisis, controversias y casos**

- **P05-F31.** ¿Qué secuencias observables aparecen en los casos chilenos del corpus?
- **P05-F32.** ¿Qué factores precedieron escalada, respuesta institucional y pérdida o recuperación de confianza?
- **P05-F33.** ¿Qué lecciones de esos casos son transferibles y cuáles dependen del sector o territorio?
- **P05-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar crisis, controversias y casos de forma estructurada?
- **P05-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre crisis, controversias y casos?
- **P05-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra crisis, controversias y casos sin introducir datos no documentados?
- **P05-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre crisis, controversias y casos, y qué versión prevalece según las correcciones?
- **P05-C12.** ¿Qué sigue sin prueba sobre crisis, controversias y casos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Doble materialidad y regulación**

- **P05-F37.** ¿Cómo se relacionan impactos sociales o ambientales con consecuencias financieras y reputacionales?
- **P05-F38.** ¿Qué señales anticipan que una controversia se convierta en asunto regulatorio?
- **P05-F39.** ¿Qué fuentes sustentan cada vínculo de materialidad y qué queda como hipótesis?
- **P05-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar doble materialidad y regulación de forma estructurada?
- **P05-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre doble materialidad y regulación?
- **P05-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra doble materialidad y regulación sin introducir datos no documentados?
- **P05-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre doble materialidad y regulación, y qué versión prevalece según las correcciones?
- **P05-C14.** ¿Qué sigue sin prueba sobre doble materialidad y regulación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Decisiones de producto y evaluación**

- **P05-F43.** ¿Qué vista o alerta ayudaría a explicar una narrativa a un ejecutivo sin exagerar su certeza?
- **P05-F44.** ¿Cómo evaluar utilidad de mapas de actores y narrativas con analistas humanos?
- **P05-F45.** ¿Cuándo debería la herramienta abstenerse de recomendar una respuesta pública?
- **P05-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar decisiones de producto y evaluación de forma estructurada?
- **P05-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre decisiones de producto y evaluación?
- **P05-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra decisiones de producto y evaluación sin introducir datos no documentados?
- **P05-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre decisiones de producto y evaluación, y qué versión prevalece según las correcciones?
- **P05-C16.** ¿Qué sigue sin prueba sobre decisiones de producto y evaluación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P05:** 48 F + 16 C + 0 X = 64 IDs.


### P06 — Cruce de conocimiento interno y señales externas


**Eje: Modelo de afirmación y evidencia**

- **P06-F01.** ¿Cómo se representa una afirmación externa con entidad, fecha, alcance, modalidad y fuente?
- **P06-F02.** ¿Cómo se enlaza esa afirmación a políticas, compromisos, hechos y portavoces internos?
- **P06-F03.** ¿Qué criterio diferencia confirmación, contradicción, desactualización y ausencia de evidencia?
- **P06-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar modelo de afirmación y evidencia de forma estructurada?
- **P06-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre modelo de afirmación y evidencia?
- **P06-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra modelo de afirmación y evidencia sin introducir datos no documentados?
- **P06-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre modelo de afirmación y evidencia, y qué versión prevalece según las correcciones?
- **P06-C02.** ¿Qué sigue sin prueba sobre modelo de afirmación y evidencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Fuentes internas y externas**

- **P06-F07.** ¿Qué tipos de documento y señal pueden cruzarse con trazabilidad suficiente?
- **P06-F08.** ¿Qué discrepancias de granularidad, tiempo, idioma y jurisdicción dificultan el enlace?
- **P06-F09.** ¿Cómo preservar el origen de cada dato al crear una respuesta combinada?
- **P06-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar fuentes internas y externas de forma estructurada?
- **P06-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre fuentes internas y externas?
- **P06-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra fuentes internas y externas sin introducir datos no documentados?
- **P06-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre fuentes internas y externas, y qué versión prevalece según las correcciones?
- **P06-C04.** ¿Qué sigue sin prueba sobre fuentes internas y externas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Identidad de entidades y acontecimientos**

- **P06-F13.** ¿Cómo unir menciones de matriz, filial, proyecto y marca sin fusionar entidades distintas?
- **P06-F14.** ¿Qué claves y reglas resuelven homónimos y cambios de nombre?
- **P06-F15.** ¿Cómo se vinculan noticias sobre eventos a compromisos o decisiones previas?
- **P06-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar identidad de entidades y acontecimientos de forma estructurada?
- **P06-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre identidad de entidades y acontecimientos?
- **P06-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra identidad de entidades y acontecimientos sin introducir datos no documentados?
- **P06-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre identidad de entidades y acontecimientos, y qué versión prevalece según las correcciones?
- **P06-C06.** ¿Qué sigue sin prueba sobre identidad de entidades y acontecimientos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Temporalidad y versiones**

- **P06-F19.** ¿Qué respuesta corresponde cuando una fuente externa es posterior al último documento oficial?
- **P06-F20.** ¿Cómo comprobar lo que era válido en la fecha del evento y en la fecha de consulta?
- **P06-F21.** ¿Cómo se detecta que una aparente contradicción es solo cambio legítimo de postura?
- **P06-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar temporalidad y versiones de forma estructurada?
- **P06-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre temporalidad y versiones?
- **P06-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra temporalidad y versiones sin introducir datos no documentados?
- **P06-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre temporalidad y versiones, y qué versión prevalece según las correcciones?
- **P06-C08.** ¿Qué sigue sin prueba sobre temporalidad y versiones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Arquitectura de procesamiento**

- **P06-F25.** ¿Qué secuencia de ingesta, extracción, recuperación, contraste y revisión propone el corpus?
- **P06-F26.** ¿Qué pasos necesitan reglas deterministas, modelos estadísticos o validación humana?
- **P06-F27.** ¿Qué registros permiten reproducir una conclusión después de actualizar las fuentes?
- **P06-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar arquitectura de procesamiento de forma estructurada?
- **P06-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre arquitectura de procesamiento?
- **P06-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra arquitectura de procesamiento sin introducir datos no documentados?
- **P06-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre arquitectura de procesamiento, y qué versión prevalece según las correcciones?
- **P06-C10.** ¿Qué sigue sin prueba sobre arquitectura de procesamiento, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Tipos de discrepancia y respuesta**

- **P06-F31.** ¿Qué taxonomía cubre cifras distintas, promesas pendientes, negaciones, silencio y errores de atribución?
- **P06-F32.** ¿Qué debe mostrar un brief cuando la información está en conflicto?
- **P06-F33.** ¿Cuándo conviene alertar, pedir revisión o abstenerse de redactar un mensaje?
- **P06-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar tipos de discrepancia y respuesta de forma estructurada?
- **P06-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre tipos de discrepancia y respuesta?
- **P06-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra tipos de discrepancia y respuesta sin introducir datos no documentados?
- **P06-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre tipos de discrepancia y respuesta, y qué versión prevalece según las correcciones?
- **P06-C12.** ¿Qué sigue sin prueba sobre tipos de discrepancia y respuesta, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Evaluación con casos de referencia**

- **P06-F37.** ¿Cómo construir casos positivos, negativos, ambiguos y adversariales de cruce documental?
- **P06-F38.** ¿Qué métricas evalúan precisión del enlace, citas, temporalidad y detección de contradicciones?
- **P06-F39.** ¿Qué tasa de falsos positivos toleraría un equipo de asuntos corporativos?
- **P06-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar evaluación con casos de referencia de forma estructurada?
- **P06-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre evaluación con casos de referencia?
- **P06-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra evaluación con casos de referencia sin introducir datos no documentados?
- **P06-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre evaluación con casos de referencia, y qué versión prevalece según las correcciones?
- **P06-C14.** ¿Qué sigue sin prueba sobre evaluación con casos de referencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Privacidad y límites epistémicos**

- **P06-F43.** ¿Qué datos internos nunca deben salir a un proveedor externo o a un lector sin permiso?
- **P06-F44.** ¿Cómo distinguir un grafo conceptual propuesto de una integración de software ya probada?
- **P06-F45.** ¿Qué fuentes o métodos del dossier fueron corregidos por el addendum de calidad?
- **P06-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar privacidad y límites epistémicos de forma estructurada?
- **P06-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre privacidad y límites epistémicos?
- **P06-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra privacidad y límites epistémicos sin introducir datos no documentados?
- **P06-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre privacidad y límites epistémicos, y qué versión prevalece según las correcciones?
- **P06-C16.** ¿Qué sigue sin prueba sobre privacidad y límites epistémicos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Profundización especializada**


*Grafo de afirmaciones*

- **P06-X01.** ¿Qué esquema mínimo relaciona afirmación, evidencia, organización, actor, compromiso y evento?
- **P06-X02.** ¿Cómo expresar relación de apoyo, conflicto, modificación y caducidad sin perder procedencia?
- **P06-X03.** ¿Qué consulta reconstruye por qué se emitió una alerta en una fecha concreta?
- **P06-X04.** ¿Qué variables, categorías, relaciones y condiciones exige representar grafo de afirmaciones de forma estructurada?
- **P06-X05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre grafo de afirmaciones?
- **P06-X06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra grafo de afirmaciones sin introducir datos no documentados?
- **P06-X07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre grafo de afirmaciones, y qué versión prevalece según las correcciones?
- **P06-X08.** ¿Qué sigue sin prueba sobre grafo de afirmaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Resolución de contradicciones complejas*

- **P06-X09.** ¿Cómo clasificar dos cifras incompatibles que usan períodos o unidades distintos?
- **P06-X10.** ¿Cómo distinguir retractación oficial, corrección editorial y nueva política corporativa?
- **P06-X11.** ¿Qué umbral obliga revisión humana antes de señalar públicamente una contradicción?
- **P06-X12.** ¿Qué variables, categorías, relaciones y condiciones exige representar resolución de contradicciones complejas de forma estructurada?
- **P06-X13.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre resolución de contradicciones complejas?
- **P06-X14.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra resolución de contradicciones complejas sin introducir datos no documentados?
- **P06-X15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre resolución de contradicciones complejas, y qué versión prevalece según las correcciones?
- **P06-X16.** ¿Qué sigue sin prueba sobre resolución de contradicciones complejas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Seguridad en recuperación combinada*

- **P06-X17.** ¿Qué ocurre cuando una noticia pública activa una búsqueda sobre documentos internos restringidos?
- **P06-X18.** ¿Cómo ofrecer una alerta útil sin revelar la existencia o contenido de un documento protegido?
- **P06-X19.** ¿Qué pruebas muestran ausencia de contaminación entre clientes y usuarios?
- **P06-X20.** ¿Qué variables, categorías, relaciones y condiciones exige representar seguridad en recuperación combinada de forma estructurada?
- **P06-X21.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre seguridad en recuperación combinada?
- **P06-X22.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra seguridad en recuperación combinada sin introducir datos no documentados?
- **P06-X23.** ¿Dónde discrepan fuentes originales y síntesis internas sobre seguridad en recuperación combinada, y qué versión prevalece según las correcciones?
- **P06-X24.** ¿Qué sigue sin prueba sobre seguridad en recuperación combinada, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Ablación y valor del cruce*

- **P06-X25.** ¿Cómo comparar un brief generado solo con fuentes externas contra uno con cruce interno?
- **P06-X26.** ¿Qué errores nuevos introduce la integración aunque aumente cobertura?
- **P06-X27.** ¿Qué resultado demostraría que el cruce mejora la decisión y no solo añade texto?
- **P06-X28.** ¿Qué variables, categorías, relaciones y condiciones exige representar ablación y valor del cruce de forma estructurada?
- **P06-X29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ablación y valor del cruce?
- **P06-X30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra ablación y valor del cruce sin introducir datos no documentados?
- **P06-X31.** ¿Dónde discrepan fuentes originales y síntesis internas sobre ablación y valor del cruce, y qué versión prevalece según las correcciones?
- **P06-X32.** ¿Qué sigue sin prueba sobre ablación y valor del cruce, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P06:** 48 F + 16 C + 32 X = 96 IDs.


### P07 — Preparación ejecutiva y apoyo estratégico


**Eje: Objetivo del brief ejecutivo**

- **P07-F01.** ¿Qué decisión concreta debe habilitar un brief antes de reunión, entrevista o crisis?
- **P07-F02.** ¿Qué información esencial cabe en una primera página y qué debe quedar como respaldo navegable?
- **P07-F03.** ¿Cómo cambia el brief para CEO, CCO, vocero técnico y responsable territorial?
- **P07-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar objetivo del brief ejecutivo de forma estructurada?
- **P07-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre objetivo del brief ejecutivo?
- **P07-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra objetivo del brief ejecutivo sin introducir datos no documentados?
- **P07-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre objetivo del brief ejecutivo, y qué versión prevalece según las correcciones?
- **P07-C02.** ¿Qué sigue sin prueba sobre objetivo del brief ejecutivo, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Preguntas difíciles y escenarios**

- **P07-F07.** ¿Cómo generar preguntas probables desde señales externas y compromisos históricos?
- **P07-F08.** ¿Qué criterios priorizan una pregunta hostil sin convertir posibilidad en predicción cierta?
- **P07-F09.** ¿Cómo preparar respuestas para escenarios de confirmación, contradicción e incertidumbre?
- **P07-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar preguntas difíciles y escenarios de forma estructurada?
- **P07-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre preguntas difíciles y escenarios?
- **P07-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra preguntas difíciles y escenarios sin introducir datos no documentados?
- **P07-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre preguntas difíciles y escenarios, y qué versión prevalece según las correcciones?
- **P07-C04.** ¿Qué sigue sin prueba sobre preguntas difíciles y escenarios, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Mensajes y líneas aprobadas**

- **P07-F13.** ¿Cómo se extraen posturas vigentes sin reutilizar textos vencidos o borradores?
- **P07-F14.** ¿Cómo se muestra qué frase está aprobada, para quién y en qué canal?
- **P07-F15.** ¿Qué procedimiento sigue una propuesta de mensaje cuando carece de aprobación?
- **P07-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar mensajes y líneas aprobadas de forma estructurada?
- **P07-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre mensajes y líneas aprobadas?
- **P07-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra mensajes y líneas aprobadas sin introducir datos no documentados?
- **P07-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre mensajes y líneas aprobadas, y qué versión prevalece según las correcciones?
- **P07-C06.** ¿Qué sigue sin prueba sobre mensajes y líneas aprobadas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Simulación y práctica de vocería**

- **P07-F19.** ¿Qué roles y situaciones pueden simularse sin confundir ensayo con reacción real de actores?
- **P07-F20.** ¿Qué retroalimentación útil se puede ofrecer sobre evidencia, claridad y prudencia?
- **P07-F21.** ¿Cómo medir preparación del portavoz antes y después de la práctica?
- **P07-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar simulación y práctica de vocería de forma estructurada?
- **P07-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre simulación y práctica de vocería?
- **P07-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra simulación y práctica de vocería sin introducir datos no documentados?
- **P07-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre simulación y práctica de vocería, y qué versión prevalece según las correcciones?
- **P07-C08.** ¿Qué sigue sin prueba sobre simulación y práctica de vocería, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Apoyo estratégico y límites**

- **P07-F25.** ¿Qué recomendaciones operativas pueden derivarse de evidencia citada?
- **P07-F26.** ¿Dónde termina el apoyo analítico y empieza una decisión política, legal o reputacional humana?
- **P07-F27.** ¿Cuándo debe el sistema elevar un riesgo a especialistas o abstenerse?
- **P07-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar apoyo estratégico y límites de forma estructurada?
- **P07-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre apoyo estratégico y límites?
- **P07-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra apoyo estratégico y límites sin introducir datos no documentados?
- **P07-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre apoyo estratégico y límites, y qué versión prevalece según las correcciones?
- **P07-C10.** ¿Qué sigue sin prueba sobre apoyo estratégico y límites, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Flujo de revisión humana**

- **P07-F31.** ¿Quién valida cifras, interpretación, lenguaje y autorización antes de usar un brief?
- **P07-F32.** ¿Cómo se registran cambios y razones de aprobación o rechazo?
- **P07-F33.** ¿Qué latencia de revisión es aceptable en operación normal y en crisis?
- **P07-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar flujo de revisión humana de forma estructurada?
- **P07-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre flujo de revisión humana?
- **P07-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra flujo de revisión humana sin introducir datos no documentados?
- **P07-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre flujo de revisión humana, y qué versión prevalece según las correcciones?
- **P07-C12.** ¿Qué sigue sin prueba sobre flujo de revisión humana, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Viabilidad comercial en Chile y Latinoamérica**

- **P07-F37.** ¿Qué formatos y estilos requiere una audiencia con autoridad chilena o comunidad local?
- **P07-F38.** ¿Cómo considerar lenguaje, contexto político y sensibilidad territorial sin estereotipos?
- **P07-F39.** ¿Qué afirmaciones regulatorias del dossier requieren revisión de vigencia por jurisdicción?
- **P07-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar viabilidad comercial en Chile y Latinoamérica de forma estructurada?
- **P07-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre viabilidad comercial en Chile y Latinoamérica?
- **P07-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra viabilidad comercial en Chile y Latinoamérica sin introducir datos no documentados?
- **P07-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre viabilidad comercial en Chile y Latinoamérica, y qué versión prevalece según las correcciones?
- **P07-C14.** ¿Qué sigue sin prueba sobre viabilidad comercial en Chile y Latinoamérica, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Calidad y evaluación de briefs**

- **P07-F43.** ¿Qué rúbrica humana mide utilidad, exactitud, suficiencia y tono de una preparación ejecutiva?
- **P07-F44.** ¿Cómo comparar el brief generado con la preparación manual actual?
- **P07-F45.** ¿Qué fallo crítico invalida un brief aunque ahorre tiempo?
- **P07-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar calidad y evaluación de briefs de forma estructurada?
- **P07-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre calidad y evaluación de briefs?
- **P07-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra calidad y evaluación de briefs sin introducir datos no documentados?
- **P07-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre calidad y evaluación de briefs, y qué versión prevalece según las correcciones?
- **P07-C16.** ¿Qué sigue sin prueba sobre calidad y evaluación de briefs, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P07:** 48 F + 16 C + 0 X = 64 IDs.


### P08 — Viabilidad, modelos de negocio y oportunidades


**Eje: Problema, segmento y disposición a pagar**

- **P08-F01.** ¿Qué problema frecuente y costoso identifica el corpus para un comprador concreto?
- **P08-F02.** ¿Qué evidencia separa interés declarado por IA de presupuesto y compra reales?
- **P08-F03.** ¿Qué segmento inicial reúne urgencia, acceso a datos y capacidad de adopción?
- **P08-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar problema, segmento y disposición a pagar de forma estructurada?
- **P08-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre problema, segmento y disposición a pagar?
- **P08-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra problema, segmento y disposición a pagar sin introducir datos no documentados?
- **P08-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre problema, segmento y disposición a pagar, y qué versión prevalece según las correcciones?
- **P08-C02.** ¿Qué sigue sin prueba sobre problema, segmento y disposición a pagar, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Tamaño y límites del mercado**

- **P08-F07.** ¿Qué datos originales permiten estimar compradores accesibles en Chile y Latinoamérica?
- **P08-F08.** ¿Qué segmentos deben excluirse por derechos de datos, seguridad o ciclo de venta?
- **P08-F09.** ¿Cómo construir rangos de mercado sin asumir cuotas o precios no observados?
- **P08-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar tamaño y límites del mercado de forma estructurada?
- **P08-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre tamaño y límites del mercado?
- **P08-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra tamaño y límites del mercado sin introducir datos no documentados?
- **P08-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre tamaño y límites del mercado, y qué versión prevalece según las correcciones?
- **P08-C04.** ¿Qué sigue sin prueba sobre tamaño y límites del mercado, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Alternativas y sustitutos**

- **P08-F13.** ¿Cómo resuelven hoy el problema agencias, equipos internos y software especializado?
- **P08-F14.** ¿Qué coste y calidad de cada alternativa son medibles en una prueba real?
- **P08-F15.** ¿Qué comparación del dossier debe corregirse a la luz de la fe de erratas de P02?
- **P08-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar alternativas y sustitutos de forma estructurada?
- **P08-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre alternativas y sustitutos?
- **P08-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra alternativas y sustitutos sin introducir datos no documentados?
- **P08-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre alternativas y sustitutos, y qué versión prevalece según las correcciones?
- **P08-C06.** ¿Qué sigue sin prueba sobre alternativas y sustitutos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Modelos de entrega**

- **P08-F19.** ¿Qué actividades corresponden a consultoría, SaaS y servicio apoyado por tecnología?
- **P08-F20.** ¿Qué tareas se automatizan de forma segura y cuáles retienen revisión experta?
- **P08-F21.** ¿Qué evidencia respaldaría o refutaría que el modelo híbrido sea preferible?
- **P08-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar modelos de entrega de forma estructurada?
- **P08-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre modelos de entrega?
- **P08-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra modelos de entrega sin introducir datos no documentados?
- **P08-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre modelos de entrega, y qué versión prevalece según las correcciones?
- **P08-C08.** ¿Qué sigue sin prueba sobre modelos de entrega, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Construir, comprar e integrar**

- **P08-F25.** ¿Qué componentes tienen proveedores maduros y cuáles requieren desarrollo propio?
- **P08-F26.** ¿Qué dependencia de licencia, proveedor o API crea cada elección?
- **P08-F27.** ¿Qué prueba técnica y comercial debería anteceder una decisión de integración?
- **P08-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar construir, comprar e integrar de forma estructurada?
- **P08-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre construir, comprar e integrar?
- **P08-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra construir, comprar e integrar sin introducir datos no documentados?
- **P08-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre construir, comprar e integrar, y qué versión prevalece según las correcciones?
- **P08-C10.** ¿Qué sigue sin prueba sobre construir, comprar e integrar, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Costos y economía unitaria**

- **P08-F31.** ¿Qué rubros incluyen datos, cómputo, almacenamiento, revisión humana e implementación?
- **P08-F32.** ¿Qué costos son observados, cotizados o supuestos y con qué sensibilidad?
- **P08-F33.** ¿En qué condiciones el precio cubriría el costo marginal y el soporte?
- **P08-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar costos y economía unitaria de forma estructurada?
- **P08-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre costos y economía unitaria?
- **P08-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra costos y economía unitaria sin introducir datos no documentados?
- **P08-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre costos y economía unitaria, y qué versión prevalece según las correcciones?
- **P08-C12.** ¿Qué sigue sin prueba sobre costos y economía unitaria, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Diferenciación como hipótesis**

- **P08-F37.** ¿Qué flujo completo podría distinguir la propuesta frente a alternativas existentes?
- **P08-F38.** ¿Qué parte del valor depende de integrar datos internos, externos y memoria relacional?
- **P08-F39.** ¿Qué evidencia falsaría la hipótesis de ventaja diferencial?
- **P08-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar diferenciación como hipótesis de forma estructurada?
- **P08-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre diferenciación como hipótesis?
- **P08-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra diferenciación como hipótesis sin introducir datos no documentados?
- **P08-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre diferenciación como hipótesis, y qué versión prevalece según las correcciones?
- **P08-C14.** ¿Qué sigue sin prueba sobre diferenciación como hipótesis, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Experimentos comerciales**

- **P08-F43.** ¿Qué entrevista, piloto guiado y prueba de disposición a pagar propone el corpus?
- **P08-F44.** ¿Qué decisión de continuar, reformular o detener corresponde a cada resultado?
- **P08-F45.** ¿Qué controles impiden interpretar un piloto sin comprador como validación del negocio?
- **P08-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar experimentos comerciales de forma estructurada?
- **P08-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre experimentos comerciales?
- **P08-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra experimentos comerciales sin introducir datos no documentados?
- **P08-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre experimentos comerciales, y qué versión prevalece según las correcciones?
- **P08-C16.** ¿Qué sigue sin prueba sobre experimentos comerciales, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P08:** 48 F + 16 C + 0 X = 64 IDs.


### P09 — Memoria de relaciones y gestión de compromisos


**Eje: Mapa de actores y relaciones**

- **P09-F01.** ¿Qué tipos de persona, organización, comunidad y autoridad requiere la memoria de relaciones?
- **P09-F02.** ¿Qué vínculos entre actor, asunto, territorio, reunión y compromiso deben conservarse?
- **P09-F03.** ¿Cómo evitar atribuir a una persona la postura de un grupo entero?
- **P09-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar mapa de actores y relaciones de forma estructurada?
- **P09-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre mapa de actores y relaciones?
- **P09-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra mapa de actores y relaciones sin introducir datos no documentados?
- **P09-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre mapa de actores y relaciones, y qué versión prevalece según las correcciones?
- **P09-C02.** ¿Qué sigue sin prueba sobre mapa de actores y relaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Historial de interacción**

- **P09-F07.** ¿Qué datos deben registrarse después de llamada, reunión, audiencia o visita a terreno?
- **P09-F08.** ¿Cómo se distinguen hecho observado, minuta aprobada, interpretación y dato sensible?
- **P09-F09.** ¿Qué resumen histórico necesita un nuevo responsable antes de hablar con un actor?
- **P09-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar historial de interacción de forma estructurada?
- **P09-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre historial de interacción?
- **P09-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra historial de interacción sin introducir datos no documentados?
- **P09-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre historial de interacción, y qué versión prevalece según las correcciones?
- **P09-C04.** ¿Qué sigue sin prueba sobre historial de interacción, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Ficha de compromiso**

- **P09-F13.** ¿Qué campos identifican promesa, responsable, beneficiario, plazo, evidencia y estado?
- **P09-F14.** ¿Cómo se enlaza el compromiso con acta, proyecto, autoridad y documentos internos?
- **P09-F15.** ¿Qué excepciones requieren aprobación, explicación pública o escalamiento?
- **P09-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar ficha de compromiso de forma estructurada?
- **P09-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ficha de compromiso?
- **P09-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra ficha de compromiso sin introducir datos no documentados?
- **P09-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre ficha de compromiso, y qué versión prevalece según las correcciones?
- **P09-C06.** ¿Qué sigue sin prueba sobre ficha de compromiso, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Ciclo de vida y seguimiento**

- **P09-F19.** ¿Qué estados y transiciones cubren propuesta, acuerdo, ejecución, verificación y cierre?
- **P09-F20.** ¿Qué alertas anticipan incumplimiento o vencimiento sin duplicar tareas?
- **P09-F21.** ¿Cómo se registra un cambio de alcance o renegociación sin borrar el compromiso original?
- **P09-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar ciclo de vida y seguimiento de forma estructurada?
- **P09-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ciclo de vida y seguimiento?
- **P09-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra ciclo de vida y seguimiento sin introducir datos no documentados?
- **P09-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre ciclo de vida y seguimiento, y qué versión prevalece según las correcciones?
- **P09-C08.** ¿Qué sigue sin prueba sobre ciclo de vida y seguimiento, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Territorio y participación**

- **P09-F25.** ¿Qué diferencias presentan actores comunitarios, reguladores, municipios y organizaciones indígenas?
- **P09-F26.** ¿Cómo se representa un conflicto territorial sin reducirlo a sentimiento automático?
- **P09-F27.** ¿Qué prácticas documentadas preservan confianza y continuidad al cambiar el equipo corporativo?
- **P09-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar territorio y participación de forma estructurada?
- **P09-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre territorio y participación?
- **P09-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra territorio y participación sin introducir datos no documentados?
- **P09-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre territorio y participación, y qué versión prevalece según las correcciones?
- **P09-C10.** ¿Qué sigue sin prueba sobre territorio y participación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Registros públicos y obligaciones**

- **P09-F31.** ¿Qué fuentes de lobby, evaluación ambiental y cumplimiento aportan contexto en Chile?
- **P09-F32.** ¿Cómo comprobar vigencia, jurisdicción y estado de un trámite antes de citarlo?
- **P09-F33.** ¿Qué límites del corpus impiden dar asesoría legal desde estas fuentes?
- **P09-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar registros públicos y obligaciones de forma estructurada?
- **P09-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre registros públicos y obligaciones?
- **P09-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra registros públicos y obligaciones sin introducir datos no documentados?
- **P09-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre registros públicos y obligaciones, y qué versión prevalece según las correcciones?
- **P09-C12.** ¿Qué sigue sin prueba sobre registros públicos y obligaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Herramientas existentes**

- **P09-F37.** ¿Qué capacidades de Open Point, Simply Stakeholders, Borealis u otros cubren el flujo?
- **P09-F38.** ¿Qué parte es CRM, análisis de feedback o servicio de implementación?
- **P09-F39.** ¿Qué integración con escucha externa y conocimiento interno está documentada?
- **P09-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar herramientas existentes de forma estructurada?
- **P09-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre herramientas existentes?
- **P09-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra herramientas existentes sin introducir datos no documentados?
- **P09-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre herramientas existentes, y qué versión prevalece según las correcciones?
- **P09-C14.** ¿Qué sigue sin prueba sobre herramientas existentes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Calidad, acceso y correcciones**

- **P09-F43.** ¿Qué pruebas muestran completitud, exactitud y actualización de un registro de compromiso?
- **P09-F44.** ¿Quién debe acceder a interacciones delicadas y cómo se audita la consulta?
- **P09-F45.** ¿Qué rectificaciones de P09_VERIFICATION_CORRECTIONS prevalecen sobre el dossier original?
- **P09-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar calidad, acceso y correcciones de forma estructurada?
- **P09-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre calidad, acceso y correcciones?
- **P09-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra calidad, acceso y correcciones sin introducir datos no documentados?
- **P09-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre calidad, acceso y correcciones, y qué versión prevalece según las correcciones?
- **P09-C16.** ¿Qué sigue sin prueba sobre calidad, acceso y correcciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P09:** 48 F + 16 C + 0 X = 64 IDs.


### P10 — Gestión y aprobación de la comunicación corporativa


**Eje: Origen de solicitudes y señales**

- **P10-F01.** ¿Qué eventos inician una respuesta pública planificada o de crisis?
- **P10-F02.** ¿Qué información mínima debe acompañar una solicitud de comunicado o respuesta?
- **P10-F03.** ¿Cómo se asigna prioridad sin mezclar rumor, hecho confirmado y obligación formal?
- **P10-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar origen de solicitudes y señales de forma estructurada?
- **P10-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre origen de solicitudes y señales?
- **P10-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra origen de solicitudes y señales sin introducir datos no documentados?
- **P10-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre origen de solicitudes y señales, y qué versión prevalece según las correcciones?
- **P10-C02.** ¿Qué sigue sin prueba sobre origen de solicitudes y señales, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Verificación de hechos y cifras**

- **P10-F07.** ¿Qué pasos validan cifras, fechas, alcance y versión de una afirmación?
- **P10-F08.** ¿Quién resuelve discrepancias entre datos operativos, memoria publicada y medios?
- **P10-F09.** ¿Cómo se documenta que una afirmación quedó pendiente o no puede publicarse?
- **P10-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar verificación de hechos y cifras de forma estructurada?
- **P10-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre verificación de hechos y cifras?
- **P10-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra verificación de hechos y cifras sin introducir datos no documentados?
- **P10-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre verificación de hechos y cifras, y qué versión prevalece según las correcciones?
- **P10-C04.** ¿Qué sigue sin prueba sobre verificación de hechos y cifras, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Redacción y adaptación de mensajes**

- **P10-F13.** ¿Qué elementos de una postura aprobada deben preservarse al adaptar canal o audiencia?
- **P10-F14.** ¿Qué variaciones son editorialmente admisibles y cuáles requieren nueva aprobación?
- **P10-F15.** ¿Cómo se genera un borrador que conserve citas y advertencias de incertidumbre?
- **P10-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar redacción y adaptación de mensajes de forma estructurada?
- **P10-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre redacción y adaptación de mensajes?
- **P10-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra redacción y adaptación de mensajes sin introducir datos no documentados?
- **P10-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre redacción y adaptación de mensajes, y qué versión prevalece según las correcciones?
- **P10-C06.** ¿Qué sigue sin prueba sobre redacción y adaptación de mensajes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: RACI, DACI y cadena de aprobación**

- **P10-F19.** ¿Qué roles preparan, consultan, autorizan y publican cada tipo de mensaje?
- **P10-F20.** ¿Qué cambia entre operación ordinaria, emergencia y asunto regulado?
- **P10-F21.** ¿Cómo evitar bloqueos por ausencia de un aprobador sin saltarse controles?
- **P10-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar rACI, DACI y cadena de aprobación de forma estructurada?
- **P10-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre rACI, DACI y cadena de aprobación?
- **P10-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra rACI, DACI y cadena de aprobación sin introducir datos no documentados?
- **P10-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre rACI, DACI y cadena de aprobación, y qué versión prevalece según las correcciones?
- **P10-C08.** ¿Qué sigue sin prueba sobre rACI, DACI y cadena de aprobación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Estados, versiones y auditoría**

- **P10-F25.** ¿Qué estados debe recorrer un mensaje desde borrador hasta retiro o corrección?
- **P10-F26.** ¿Cómo se conservan versiones, motivos de cambio y firmas de aprobación?
- **P10-F27.** ¿Qué ocurre cuando nueva evidencia invalida un mensaje ya publicado?
- **P10-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar estados, versiones y auditoría de forma estructurada?
- **P10-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre estados, versiones y auditoría?
- **P10-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra estados, versiones y auditoría sin introducir datos no documentados?
- **P10-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre estados, versiones y auditoría, y qué versión prevalece según las correcciones?
- **P10-C10.** ¿Qué sigue sin prueba sobre estados, versiones y auditoría, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Reglas para automatizar o abstenerse**

- **P10-F31.** ¿Qué tareas pueden automatizarse con bajo riesgo y cuáles deben revisarse siempre?
- **P10-F32.** ¿Qué señales obligan a abstenerse y pedir consejo legal o técnico?
- **P10-F33.** ¿Qué prueba demostraría que un control humano fue efectivo y no solo nominal?
- **P10-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar reglas para automatizar o abstenerse de forma estructurada?
- **P10-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre reglas para automatizar o abstenerse?
- **P10-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra reglas para automatizar o abstenerse sin introducir datos no documentados?
- **P10-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre reglas para automatizar o abstenerse, y qué versión prevalece según las correcciones?
- **P10-C12.** ¿Qué sigue sin prueba sobre reglas para automatizar o abstenerse, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Canales y escenarios**

- **P10-F37.** ¿Cómo difieren comunicado, respuesta a periodista, mensaje interno y explicación a autoridad?
- **P10-F38.** ¿Qué flujos exigen crisis ambiental, reporte de sostenibilidad o consulta comunitaria?
- **P10-F39.** ¿Cómo mantener coherencia sin enviar el mismo texto a audiencias distintas?
- **P10-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar canales y escenarios de forma estructurada?
- **P10-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre canales y escenarios?
- **P10-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra canales y escenarios sin introducir datos no documentados?
- **P10-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre canales y escenarios, y qué versión prevalece según las correcciones?
- **P10-C14.** ¿Qué sigue sin prueba sobre canales y escenarios, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Indicadores y límites normativos**

- **P10-F43.** ¿Qué mide tiempo de aprobación, tasa de corrección, error factual y reutilización segura?
- **P10-F44.** ¿Qué regulaciones específicas están verificadas en fuentes oficiales y cuáles siguen pendientes?
- **P10-F45.** ¿Qué correcciones de P10_VERIFICATION_CORRECTIONS impiden citar eCFR o afirmar cobertura legal universal?
- **P10-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar indicadores y límites normativos de forma estructurada?
- **P10-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre indicadores y límites normativos?
- **P10-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra indicadores y límites normativos sin introducir datos no documentados?
- **P10-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre indicadores y límites normativos, y qué versión prevalece según las correcciones?
- **P10-C16.** ¿Qué sigue sin prueba sobre indicadores y límites normativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P10:** 48 F + 16 C + 0 X = 64 IDs.


### P11 — Gobernanza de información y operación entre clientes


**Eje: Inventario y clasificación de datos**

- **P11-F01.** ¿Qué datos son públicos, internos, confidenciales, personales o de terceros?
- **P11-F02.** ¿Quién es dueño y responsable de cada conjunto de documentos y señales?
- **P11-F03.** ¿Qué regla decide si una fuente puede incluirse en búsqueda y respuesta?
- **P11-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar inventario y clasificación de datos de forma estructurada?
- **P11-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre inventario y clasificación de datos?
- **P11-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra inventario y clasificación de datos sin introducir datos no documentados?
- **P11-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre inventario y clasificación de datos, y qué versión prevalece según las correcciones?
- **P11-C02.** ¿Qué sigue sin prueba sobre inventario y clasificación de datos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Separación entre clientes**

- **P11-F07.** ¿Qué frontera lógica y operativa impide que datos de un cliente aparezcan en otro?
- **P11-F08.** ¿Cómo se prueba aislamiento en ingesta, índices, caché, conversación, exportación y respaldo?
- **P11-F09.** ¿Qué fallos cruzados deben incluirse en pruebas adversariales?
- **P11-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar separación entre clientes de forma estructurada?
- **P11-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre separación entre clientes?
- **P11-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra separación entre clientes sin introducir datos no documentados?
- **P11-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre separación entre clientes, y qué versión prevalece según las correcciones?
- **P11-C04.** ¿Qué sigue sin prueba sobre separación entre clientes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Matriz dato, actor, acción y permiso**

- **P11-F13.** ¿Qué combinación de rol, propósito y clasificación autoriza cada acción?
- **P11-F14.** ¿Cómo se heredan, revocan y comprueban permisos del origen al resultado?
- **P11-F15.** ¿Qué bitácora permite responder quién accedió a qué y por qué?
- **P11-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar matriz dato, actor, acción y permiso de forma estructurada?
- **P11-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre matriz dato, actor, acción y permiso?
- **P11-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra matriz dato, actor, acción y permiso sin introducir datos no documentados?
- **P11-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre matriz dato, actor, acción y permiso, y qué versión prevalece según las correcciones?
- **P11-C06.** ¿Qué sigue sin prueba sobre matriz dato, actor, acción y permiso, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Ciclo de vida y retención**

- **P11-F19.** ¿Cómo se ingesta, versiona, archiva, corrige y elimina información según su tipo?
- **P11-F20.** ¿Qué períodos de retención son políticas propuestas y cuáles obligaciones verificadas?
- **P11-F21.** ¿Cómo se ejecuta una revocación sin dejar copias en resultados o registros?
- **P11-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar ciclo de vida y retención de forma estructurada?
- **P11-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ciclo de vida y retención?
- **P11-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra ciclo de vida y retención sin introducir datos no documentados?
- **P11-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre ciclo de vida y retención, y qué versión prevalece según las correcciones?
- **P11-C08.** ¿Qué sigue sin prueba sobre ciclo de vida y retención, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Proveedores y procesamiento externo**

- **P11-F25.** ¿Qué datos recibe cada proveedor de IA, búsqueda, monitoreo y almacenamiento?
- **P11-F26.** ¿Qué cláusulas, regiones de procesamiento y condiciones de entrenamiento aparecen en términos directos?
- **P11-F27.** ¿Qué respuesta de debida diligencia sigue pendiente de confirmación contractual?
- **P11-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar proveedores y procesamiento externo de forma estructurada?
- **P11-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre proveedores y procesamiento externo?
- **P11-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra proveedores y procesamiento externo sin introducir datos no documentados?
- **P11-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre proveedores y procesamiento externo, y qué versión prevalece según las correcciones?
- **P11-C10.** ¿Qué sigue sin prueba sobre proveedores y procesamiento externo, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Controles comprobables**

- **P11-F31.** ¿Qué pruebas muestran cifrado, segregación, registro, control de acceso y respuesta a incidentes?
- **P11-F32.** ¿Qué diferencia una afirmación de marketing de un control probado o certificación vigente?
- **P11-F33.** ¿Qué evidencia necesitaría un cliente para aceptar un piloto con sus documentos?
- **P11-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar controles comprobables de forma estructurada?
- **P11-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre controles comprobables?
- **P11-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra controles comprobables sin introducir datos no documentados?
- **P11-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre controles comprobables, y qué versión prevalece según las correcciones?
- **P11-C12.** ¿Qué sigue sin prueba sobre controles comprobables, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Incidentes y post-mortems**

- **P11-F37.** ¿Cómo detectar una cita a documento ajeno, un permiso desactualizado o un prompt malicioso?
- **P11-F38.** ¿Qué secuencia de contención, comunicación y aprendizaje correspondería a cada fallo?
- **P11-F39.** ¿Cómo incorporar lecciones sin exponer datos del incidente en el sistema compartido?
- **P11-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar incidentes y post-mortems de forma estructurada?
- **P11-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre incidentes y post-mortems?
- **P11-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra incidentes y post-mortems sin introducir datos no documentados?
- **P11-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre incidentes y post-mortems, y qué versión prevalece según las correcciones?
- **P11-C14.** ¿Qué sigue sin prueba sobre incidentes y post-mortems, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Jurisdicciones y rectificaciones**

- **P11-F43.** ¿Qué obligaciones de Chile, Brasil, UE u otras jurisdicciones están verificadas directamente?
- **P11-F44.** ¿Qué partes del régimen comparado son inferencias que necesitan asesoría legal actualizada?
- **P11-F45.** ¿Qué precedencia tienen P11_VERIFICATION_CORRECTIONS y P11_PROVIDER_SCOPE_NOTE sobre el dossier?
- **P11-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar jurisdicciones y rectificaciones de forma estructurada?
- **P11-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre jurisdicciones y rectificaciones?
- **P11-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra jurisdicciones y rectificaciones sin introducir datos no documentados?
- **P11-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre jurisdicciones y rectificaciones, y qué versión prevalece según las correcciones?
- **P11-C16.** ¿Qué sigue sin prueba sobre jurisdicciones y rectificaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de P11:** 48 F + 16 C + 0 X = 64 IDs.


### T01 — Evaluación y pilotos


**Eje: Hipótesis y compuertas del piloto**

- **T01-F01.** ¿Qué hipótesis falsable corresponde a Saber, Escuchar, Hablar y Relacionar?
- **T01-F02.** ¿Qué umbral de continuar, rediseñar o detener debe fijarse antes de ver resultados?
- **T01-F03.** ¿Qué evidencia mínima permite declarar que un módulo aporta valor incremental?
- **T01-F04.** ¿Qué variables, categorías, relaciones y condiciones exige representar hipótesis y compuertas del piloto de forma estructurada?
- **T01-F05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre hipótesis y compuertas del piloto?
- **T01-F06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra hipótesis y compuertas del piloto sin introducir datos no documentados?
- **T01-C01.** ¿Dónde discrepan fuentes originales y síntesis internas sobre hipótesis y compuertas del piloto, y qué versión prevalece según las correcciones?
- **T01-C02.** ¿Qué sigue sin prueba sobre hipótesis y compuertas del piloto, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Base manual y alternativas simples**

- **T01-F07.** ¿Cómo realiza hoy un analista el mismo trabajo sin la aplicación?
- **T01-F08.** ¿Qué alternativas de menor complejidad deben servir de control?
- **T01-F09.** ¿Qué ahorro solo existe si se mantiene la calidad de la decisión?
- **T01-F10.** ¿Qué variables, categorías, relaciones y condiciones exige representar base manual y alternativas simples de forma estructurada?
- **T01-F11.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre base manual y alternativas simples?
- **T01-F12.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra base manual y alternativas simples sin introducir datos no documentados?
- **T01-C03.** ¿Dónde discrepan fuentes originales y síntesis internas sobre base manual y alternativas simples, y qué versión prevalece según las correcciones?
- **T01-C04.** ¿Qué sigue sin prueba sobre base manual y alternativas simples, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Casos de prueba y conjunto de referencia**

- **T01-F13.** ¿Qué escenarios públicos y sintéticos cubren casos normales, ambiguos y críticos?
- **T01-F14.** ¿Cómo se rotulan afirmaciones, citas, conflictos y permisos de forma independiente?
- **T01-F15.** ¿Qué separación entre diseño y evaluación evita contaminar el conjunto de prueba?
- **T01-F16.** ¿Qué variables, categorías, relaciones y condiciones exige representar casos de prueba y conjunto de referencia de forma estructurada?
- **T01-F17.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre casos de prueba y conjunto de referencia?
- **T01-F18.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra casos de prueba y conjunto de referencia sin introducir datos no documentados?
- **T01-C05.** ¿Dónde discrepan fuentes originales y síntesis internas sobre casos de prueba y conjunto de referencia, y qué versión prevalece según las correcciones?
- **T01-C06.** ¿Qué sigue sin prueba sobre casos de prueba y conjunto de referencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Rúbricas humanas**

- **T01-F19.** ¿Qué dimensiones evalúan especialistas en asuntos corporativos para cada módulo?
- **T01-F20.** ¿Cómo se mide acuerdo entre evaluadores y se resuelven desacuerdos?
- **T01-F21.** ¿Qué fallo crítico anula una puntuación promedio aparentemente buena?
- **T01-F22.** ¿Qué variables, categorías, relaciones y condiciones exige representar rúbricas humanas de forma estructurada?
- **T01-F23.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre rúbricas humanas?
- **T01-F24.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra rúbricas humanas sin introducir datos no documentados?
- **T01-C07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre rúbricas humanas, y qué versión prevalece según las correcciones?
- **T01-C08.** ¿Qué sigue sin prueba sobre rúbricas humanas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Métricas y denominadores**

- **T01-F25.** ¿Cómo definir precisión, exhaustividad, cobertura de fuentes, latencia y costo por caso?
- **T01-F26.** ¿Qué denominador corresponde a fuentes, afirmaciones, alertas y tareas?
- **T01-F27.** ¿Qué métricas del corpus no son comparables por diferencias de muestra o contexto?
- **T01-F28.** ¿Qué variables, categorías, relaciones y condiciones exige representar métricas y denominadores de forma estructurada?
- **T01-F29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre métricas y denominadores?
- **T01-F30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra métricas y denominadores sin introducir datos no documentados?
- **T01-C09.** ¿Dónde discrepan fuentes originales y síntesis internas sobre métricas y denominadores, y qué versión prevalece según las correcciones?
- **T01-C10.** ¿Qué sigue sin prueba sobre métricas y denominadores, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Atribución de valor e impacto**

- **T01-F31.** ¿Cómo separar calidad de respuesta, cambio de decisión, resultado operativo y reputación futura?
- **T01-F32.** ¿Qué factores externos impiden atribuir un cambio reputacional al software?
- **T01-F33.** ¿Qué indicador temprano puede usarse sin prometer impacto final?
- **T01-F34.** ¿Qué variables, categorías, relaciones y condiciones exige representar atribución de valor e impacto de forma estructurada?
- **T01-F35.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre atribución de valor e impacto?
- **T01-F36.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra atribución de valor e impacto sin introducir datos no documentados?
- **T01-C11.** ¿Dónde discrepan fuentes originales y síntesis internas sobre atribución de valor e impacto, y qué versión prevalece según las correcciones?
- **T01-C12.** ¿Qué sigue sin prueba sobre atribución de valor e impacto, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Entrevistas y disposición a pagar**

- **T01-F37.** ¿Qué observaciones de usuario deben recogerse durante el piloto?
- **T01-F38.** ¿Qué pregunta o prueba comercial revela presupuesto real y proceso de compra?
- **T01-F39.** ¿Qué señales de complacencia o sesgo de selección afectan las conclusiones?
- **T01-F40.** ¿Qué variables, categorías, relaciones y condiciones exige representar entrevistas y disposición a pagar de forma estructurada?
- **T01-F41.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre entrevistas y disposición a pagar?
- **T01-F42.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra entrevistas y disposición a pagar sin introducir datos no documentados?
- **T01-C13.** ¿Dónde discrepan fuentes originales y síntesis internas sobre entrevistas y disposición a pagar, y qué versión prevalece según las correcciones?
- **T01-C14.** ¿Qué sigue sin prueba sobre entrevistas y disposición a pagar, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Eje: Costos y continuidad operacional**

- **T01-F43.** ¿Qué insumos y tiempo humano forman el costo total por piloto y por cliente?
- **T01-F44.** ¿Qué pruebas de fallo de fuente, cambio de versión y caída de proveedor se requieren?
- **T01-F45.** ¿Qué documentos de T01_VERIFICATION_CORRECTIONS sustituyen duplicados o fuentes parciales?
- **T01-F46.** ¿Qué variables, categorías, relaciones y condiciones exige representar costos y continuidad operacional de forma estructurada?
- **T01-F47.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre costos y continuidad operacional?
- **T01-F48.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra costos y continuidad operacional sin introducir datos no documentados?
- **T01-C15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre costos y continuidad operacional, y qué versión prevalece según las correcciones?
- **T01-C16.** ¿Qué sigue sin prueba sobre costos y continuidad operacional, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Profundización especializada**


*Diseño estadístico y tamaño de muestra*

- **T01-X01.** ¿Qué unidad de análisis y tamaño de muestra necesita cada experimento?
- **T01-X02.** ¿Qué incertidumbre debe reportarse para precisión de citas y detección de contradicciones?
- **T01-X03.** ¿Cómo evitar seleccionar solo casos fáciles o provenientes de un único sector?
- **T01-X04.** ¿Qué variables, categorías, relaciones y condiciones exige representar diseño estadístico y tamaño de muestra de forma estructurada?
- **T01-X05.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre diseño estadístico y tamaño de muestra?
- **T01-X06.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra diseño estadístico y tamaño de muestra sin introducir datos no documentados?
- **T01-X07.** ¿Dónde discrepan fuentes originales y síntesis internas sobre diseño estadístico y tamaño de muestra, y qué versión prevalece según las correcciones?
- **T01-X08.** ¿Qué sigue sin prueba sobre diseño estadístico y tamaño de muestra, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Pruebas adversariales y seguridad*

- **T01-X09.** ¿Qué casos incluyen prompt injection, documento vencido, fuente parcial y homónimo?
- **T01-X10.** ¿Qué ataque intenta obtener datos de otro cliente o un mensaje no aprobado?
- **T01-X11.** ¿Qué criterio de fallo detiene inmediatamente un piloto con datos reales?
- **T01-X12.** ¿Qué variables, categorías, relaciones y condiciones exige representar pruebas adversariales y seguridad de forma estructurada?
- **T01-X13.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre pruebas adversariales y seguridad?
- **T01-X14.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra pruebas adversariales y seguridad sin introducir datos no documentados?
- **T01-X15.** ¿Dónde discrepan fuentes originales y síntesis internas sobre pruebas adversariales y seguridad, y qué versión prevalece según las correcciones?
- **T01-X16.** ¿Qué sigue sin prueba sobre pruebas adversariales y seguridad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Adopción, confianza y trabajo humano*

- **T01-X17.** ¿Cómo observar si el profesional verifica citas y corrige el sistema o lo acepta sin revisar?
- **T01-X18.** ¿Qué fricción de adopción aparece al pedir permisos, revisión y trazabilidad?
- **T01-X19.** ¿Qué medida capta carga cognitiva del usuario además del tiempo ahorrado?
- **T01-X20.** ¿Qué variables, categorías, relaciones y condiciones exige representar adopción, confianza y trabajo humano de forma estructurada?
- **T01-X21.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre adopción, confianza y trabajo humano?
- **T01-X22.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra adopción, confianza y trabajo humano sin introducir datos no documentados?
- **T01-X23.** ¿Dónde discrepan fuentes originales y síntesis internas sobre adopción, confianza y trabajo humano, y qué versión prevalece según las correcciones?
- **T01-X24.** ¿Qué sigue sin prueba sobre adopción, confianza y trabajo humano, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

*Reproducción y seguimiento*

- **T01-X25.** ¿Qué versión de corpus, modelo, prompt y rúbrica debe conservarse por ejecución?
- **T01-X26.** ¿Cómo repetir el piloto después de cambiar fuentes o proveedores?
- **T01-X27.** ¿Qué formato de informe permite auditar decisiones de continuar, reformular o detener?
- **T01-X28.** ¿Qué variables, categorías, relaciones y condiciones exige representar reproducción y seguimiento de forma estructurada?
- **T01-X29.** ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre reproducción y seguimiento?
- **T01-X30.** ¿Qué caso concreto, con entradas y resultado esperado, ilustra reproducción y seguimiento sin introducir datos no documentados?
- **T01-X31.** ¿Dónde discrepan fuentes originales y síntesis internas sobre reproducción y seguimiento, y qué versión prevalece según las correcciones?
- **T01-X32.** ¿Qué sigue sin prueba sobre reproducción y seguimiento, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

**Control de T01:** 48 F + 16 C + 32 X = 96 IDs.


## 6. Registro de cierre que Antigravity debe completar

Al terminar, llenar: cuenta y conectores efectivamente usados; fecha y versión de cada manifiesto; IDs ejecutados, respondidos, parciales, sin evidencia, fallidos y bloqueados; fuentes sustantivas y parciales por cuaderno; cambios de corpus durante la extracción; muestra de auditoría y errores corregidos; enlaces a todos los archivos; contradicciones no resueltas; experimentos prioritarios. No declarar «base completa» si falta una pregunta o una cita crítica.
