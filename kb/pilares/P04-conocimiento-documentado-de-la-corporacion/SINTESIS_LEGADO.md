> Documento heredado del 2026-10-01. Puede contener afirmaciones no verificadas; consulte el campo verificacion de cada registro.

# Síntesis Ejecutiva y Metodológica — Pilar P04: Conocimiento Documentado de la Corporación

**Programa de Investigación:** Inteligencia para Asuntos Corporativos  
**Repositorio:** BRIDGE (`/Users/fmillar/Proyectos_Desarrollo/BRIDGE`)  
**Cuaderno Canónico:** `cb87941c-2377-42fb-806f-eb9878ac0757` (NotebookLM: P04 — Conocimiento documentado de la corporación)  
**Fecha de Cierre de Pilar:** 2026-10-01  
**Estado de Cobertura:** 64/64 preguntas respondidas y auditadas (48 Fundamentales F01–F48, 16 Contraste C01–C16). Auditoría Estratificada: 100% Aprobada.

---

## 1. Alcance, Fuentes y Gobernanza Editorial

El Pilar P04 investiga y formaliza los fundamentos ontológicos, matemáticos, arquitectónicos y de gobernanza para estructurar la memoria histórica y regulatoria de la empresa, alimentando directamente el diseño del módulo **Memoria** de la plataforma BRIDGE.
A través de sus 8 ejes analíticos, este pilar resuelve el problema crítico de la 'amnesia corporativa fragmentada': supera la fragilidad del RAG elemental frente a memorias de 200+ páginas, establece una taxonomía formal para erradicar el greenwashing involuntario, modela el linaje de procedencia bajo W3C PROV-O, garantiza la inmutabilidad bitemporal y fija compuertas de seguridad estricta mediante control de acceso basado en atributos (NIST SP 800-162 ABAC).

### Dimensiones Cuantitativas del Pilar:
- **Total preguntas ejecutadas:** 64 preguntas (100% del alcance aprobado para P04).
- **Preguntas Fundamentales (F):** 48 preguntas distribuidas en 8 ejes temáticos (6 por eje).
- **Preguntas de Contraste y Vacíos (C):** 16 preguntas (2 por eje: discrepancias de fuentes y vacíos técnicos).
- **Fuentes Catalogadas en Manifiesto:** 34 fuentes totales:
  - **26 fuentes externas activas y sustantivas** (regulaciones oficiales CMF Chile, estándares ISSB/IFRS, GRI, especificaciones W3C, NIST y literatura científica de conferencias líderes como EMNLP, EACL, ACM).
  - **4 documentos analíticos internos de síntesis:** `P04_EVIDENCE_MAP`, `P04_RESEARCH_DOSSIER`, `P04_GAPS_AND_VALIDATION`, y `P04_SOURCE_INDEX`.
  - **4 fuentes externas fallidas con incidencia documentada:** `EFRAG ESRS Standards` (timeout TLS), `G20/OECD Principles 2023` (bloqueo antibot), `NIST AI 100-1` (bloqueo crawler) y `TruLens` (servidor inaccesible), todas suplidas formalmente por estándares equivalentes (IFRS S1/S2, GRI, Mökander et al., RAGAS, FActScore).
- **Regla de Precedencia Editorial:** `P04_EVIDENCE_MAP` y `P04_RESEARCH_DOSSIER` ejercen precedencia metodológica sobre enfoques informales. Se mantiene la regla imperativa de que las síntesis internas son documentos de trabajo propios que jamás deben citarse como fuentes externas independientes.

---

## 2. Hallazgos Fundamentales Consolidados por Eje Temático

### Eje 1: Inventario de Documentos Corporativos (P04-F01 a P04-F06)

- **Taxonomía Canónica de 8 Clases:** El corpus se estructura en 8 familias: Memoria Anual Integrada (CMF NCG 461), Hecho Esencial (Ley 18.045), Reporte ESG (GRI 1-3), Políticas/Códigos (ISO 37000), Comunicados Oficiales, Minutas de Vocería/Q&A, Presentaciones a Inversionistas (Safe Harbor) e Informes de Aseguramiento Externo (ISAE 3000).
- **Gobierno y Custodia:** Cada artefacto se vincula a un rol custodio (Owner), nivel de aprobación colegiado (Directorio, Comité, Gerencia General) y nivel de seguridad ABAC.
- **Fuente de Verdad (SSOT) vs Borrador e Historia:** Se establece una distinción de 3 niveles: SSOT Vigente (aprobado y vinculante), Borradores (vedados para vocería externa) y Contexto Histórico (preservado inmutable con `dcterms:replaces` para auditoría pero excluido de la vocería activa).
- **Modelado Estructurado:** El inventario se cataloga bajo W3C DCAT-3 con hash inmutable SHA-256 y relaciones W3C PROV-O de autoría y aprobación.

### Eje 2: Afirmaciones y Compromisos (P04-F07 a P04-F12)

- **Taxonomía de 4 Estados Epistémicos:** Para erradicar el greenwashing, toda afirmación se clasifica en: 1) Declaración (postura cualitativa); 2) Compromiso (meta cuantificada con año base y horizonte); 3) Resultado (hecho medido de período cerrado); y 4) Verificación (auditoría externa independiente ISAE 3000).
- **Ficha Canónica de Compromiso:** Especificación formal JSON-Schema que desacopla la cifra y unidad métrica de la narrativa, capturando baseline, target, milestones, status, governance y source_traceability con hash de página.
- **Ciclo de Vida y Reexpresión:** Seguimiento riguroso de estados (`Propuesto`, `Activo`, `Cumplido`, `En Riesgo`, `Incumplido`, `Reexpresado`, `Retirado`), modelando reexpresiones de línea base bajo IFRS S2 mediante `prov:wasRevisionOf`.
- **Caso Empírico Hídrico:** Demostración sobre compromiso COM-ENV-2023-089 (meta de 750 l/s al 2030), auditando el avance 2025 de 1.040 l/s verificado por Deloitte bajo ISAE 3000.

### Eje 3: Ontología y Relaciones (P04-F13 a P04-F18)

- **7 Clases Maestras:** Grafo de Conocimiento basado en Schema.org, FIBO y PROV-O: `Organization`, `FacilityProject`, `PersonSpokesperson`, `DocumentArtifact`, `Statement`, `Commitment`, `Outcome/Verification`.
- **Desacoplamiento Societario y Operacional:** Separación estricta entre Matriz, Filial, Faena y Vocero para evitar confusión de responsabilidades ambientales (SMA/RCA) y de mercado (CMF Ley 18.045).
- **Segregación Epistémica de Aristas:** Salvaguarda contra alucinaciones relacionales: toda arista se tipifica como `hecho_documentado` (anclada a hash) o `relacion_inferida` (con score probabilístico y prohibición de uso en minutas oficiales sin advertencia).
- **Restricciones SHACL:** Validación estructural que impide mutaciones o aristas huérfanas en tiempo de inserción.

### Eje 4: Versiones y Temporalidad (P04-F19 a P04-F24)

- **Triple Dimensión Temporal:** Desacoplamiento bitemporal estricto: Fecha del Hecho (Event/Valid Time), Fecha de Publicación (Publication Time) y Fecha de Incorporación al Sistema (Transaction Time).
- **Consultas Retrospectivas As-Of:** Capacidad de reconstruir fielmente lo que la empresa sabía o declaraba a una fecha histórica mediante corte temporal `transaction_time <= T` y `valid_time contiene T`, evitando el sesgo de retrospectiva.
- **Inmutabilidad Histórica sin Borrado:** Los documentos superados nunca se borran; se anotan con `dcterms:isReplacedBy` preservando la trazabilidad forense para litigios.
- **Caso Reexpresión GEI:** Reexpresión de línea base por venta de activo industrial bajo IFRS S2, transparentando la causal técnica ante medios.

### Eje 5: Ingesta y Extracción (P04-F25 a P04-F30)

- **Layout-Aware Document Parsing:** Extracción tabular estructurada (Table-Aware Extraction) que convierte tablas complejas y matrices ESG a Markdown/JSON-LD preservando encabezados y notas.
- **Chunking Jerárquico Parent-Child:** Fragmentos hijo pequeños (128-256 tokens) para búsqueda de alta sensibilidad enlazados a fragmentos padre extensos (1.024-2.048 tokens) para proveer contexto completo y notas al generador.
- **Auditores de Paridad y Sumatorias:** Validadores automáticos de consistencia de columnas, sumas de control y resolución de llamadas a notas al pie antes de autorizar la indexación.
- **Caso Multipágina GEI:** Costura y anclaje exitoso de tabla de emisiones en dos páginas con nota al pie sobre enfoque de mercado.

### Eje 6: Gobierno y Permisos (P04-F31 a P04-F36)

- **Matriz RACI y Segregación SoD:** Definición estricta de roles para crear, aprobar, leer, corregir y retirar según formalidad legal.
- **Pre-Retrieval ABAC Filtering (NIST SP 800-162):** Rechazo absoluto de filtros en el prompt del LLM; el filtrado booleano de atributos se ejecuta en el índice vectorial y de grafos antes de la recuperación, garantizando 100.0% de aislamiento.
- **Protocolo Four-Eyes para Afirmaciones Sensibles:** Doble visado humano obligatorio y registro criptográfico PROV-O antes de publicar compromisos oficiales.
- **Caso Embargo Hecho Esencial:** Aislamiento total de un borrador confidencial de adquisición ante un analista no acreditado.

### Eje 7: Búsqueda y Respuesta Fundada (P04-F37 a P04-F42)

- **Enrutador Híbrido Tripartito:** BM25 para códigos e identificadores exactos, Embeddings densos para conceptos, ColBERT para reranking tardío y GraphRAG (algoritmo Leiden) para síntesis global multi-año.
- **Atribución a Nivel de Oración (Sentence-Level):** Descomposición atómica (Bohnet et al.) donde cada proposición cuantitativa lleva cita inmediata con título, año, página y hash SHA-256.
- **Abstención Activa Segura (Self-RAG / CRAG):** Tokens reflexivos y evaluador de recuperación que fuerzan al sistema a declarar falta de evidencia o conflicto antes que inventar una cifra.
- **Caso Diversidad de Género:** Respuesta exacta con 22% alcanzado vs 30% comprometido citando pág. 54 de la Memoria 2025.

### Eje 8: Evaluación de Calidad Documental (P04-F43 a P04-F48)

- **Cuadro de Mando de Salud del Corpus:** Monitoreo continuo de cobertura NCG 461, latencia de hechos esenciales y métricas IR (MRR@10 ≥ 0.88, NDCG@10 ≥ 0.92).
- **Gold Standard Suite de 250 Casos:** Banco de pruebas representativo de Asuntos Corporativos evaluado automáticamente con FActScore y RAGAS más auditoría humana ciega.
- **Red Teaming Adversarial de Seguridad:** 50 ataques de inyección de prompt con criterio no negociable de cero filtración de embargos (100.0% ABAC Enforcement).
- **Matriz de 5 Umbrales Mínimos:** Faithfulness ≥ 0.95, Citation Precision ≥ 0.98, Citation Recall ≥ 0.95, Coherencia Temporal 100%, Aislamiento ABAC 100.0%.

---

## 3. Matriz de Preguntas y Respuestas (Trazabilidad 64/64)

| ID | Pregunta Oficial | Estatus | Síntesis de Respuesta Fundada |
| :--- | :--- | :---: | :--- |
| **P04-F01** | ¿Qué tipos de memoria anual, política, comunicado, presentación, acta y compromiso forman el corpus institucional? | ✅ Respondida | El corpus institucional para asuntos corporativos se estructura en ocho familias de artefactos documentales canónicos: 1) Memoria Anual Integrada (reporte retrospectivo y estrat... |
| **P04-F02** | ¿Qué propietario, vigencia, aprobación y nivel de acceso necesita cada tipo documental? | ✅ Respondida | Cada tipo documental corporativo requiere cuatro atributos de gobierno rigurosos: 1) Propietario (Owner o custodio institucional responsable: e.g. Secretaría General para actas ... |
| **P04-F03** | ¿Qué artefactos son fuente de verdad y cuáles solo borradores o contexto histórico? | ✅ Respondida | La distinción operativa entre fuente de verdad, borrador y contexto histórico se rige por su estado de formalización legal y vigencia temporal: 1) Fuente de Verdad (Single Sourc... |
| **P04-F04** | ¿Qué variables, categorías, relaciones y condiciones exige representar inventario de documentos corporativos de forma estructurada? | ✅ Respondida | Representar de forma estructurada el inventario de documentos corporativos exige un modelo formal compuesto por: 1) Variables de identificación e inmutabilidad (`document_id` UU... |
| **P04-F05** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre inventario de documentos corporativos? | ✅ Respondida | Los hechos que respaldan el inventario documental corporativo se basan en cuatro fuentes primarias y normativas inmutables: 1) CMF Chile Norma de Carácter General N° 461 (12 de ... |
| **P04-F06** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra inventario de documentos corporativos sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Ingesta e inventario de la 'Memoria Anual Integrada 2025' de un emisor chileno supervisado por la CMF. Entradas: Archivo PDF de 240 páginas; Metadatos: Título 'Me... |
| **P04-F07** | ¿Cómo se registra una afirmación corporativa con cifra, fecha, alcance, fuente y responsable? | ✅ Respondida | Una afirmación corporativa con valor cuantitativo se registra mediante la 'Ficha Canónica de Compromiso Corporativo' (Corporate Commitment Data Sheet) estructurada en JSON-Schem... |
| **P04-F08** | ¿Qué campos distinguen promesa, meta, avance, incumplimiento y rectificación? | ✅ Respondida | La diferenciación entre los estados de un compromiso corporativo se rige por campos específicos en el modelo de datos: 1) Promesa / Declaración de Intención: tipificada como `co... |
| **P04-F09** | ¿Cómo se enlazan afirmaciones y compromisos con documentos, actores y decisiones posteriores? | ✅ Respondida | El enlace relacional entre afirmaciones, compromisos, documentos y decisiones se implementa mediante un Grafo de Conocimiento fundamentado en el estándar W3C PROV-O y el vocabul... |
| **P04-F10** | ¿Qué variables, categorías, relaciones y condiciones exige representar afirmaciones y compromisos de forma estructurada? | ✅ Respondida | La representación estructurada de afirmaciones y compromisos exige: 1) Variables métricas e identitarias (`commitment_id`, `title`, `description`, `baseline_value`, `target_valu... |
| **P04-F11** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre afirmaciones y compromisos? | ✅ Respondida | Los hechos relativos al modelado de afirmaciones y compromisos se sustentan en cuatro pilares normativos y ontológicos: 1) IFRS S2 Climate-related Disclosures (junio 2023, párrs... |
| **P04-F12** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra afirmaciones y compromisos sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Seguimiento del compromiso ambiental 'Reducción de extracción de agua continental en operaciones mineras' (ID: COM-ENV-2023-089). Entradas documentadas: 1) Declar... |
| **P04-F13** | ¿Qué entidades y relaciones son necesarias para representar la memoria corporativa? | ✅ Respondida | Representar la memoria corporativa exige un Grafo de Conocimiento (Knowledge Graph) compuesto por 7 clases maestras de entidades y sus relaciones dirigidas: 1) `org:Organization... |
| **P04-F14** | ¿Qué casos exigen separar matriz, filial, proyecto, instalación y vocero? | ✅ Respondida | La separación estricta entre matriz, filial, proyecto, instalación y vocero es mandatoria en tres casos operacionales críticos: 1) Controversias Regulatorias y Ambientales: los ... |
| **P04-F15** | ¿Cómo se evita que un grafo convierta una relación inferida en hecho comprobado? | ✅ Respondida | Para evitar que un grafo de conocimiento promueva una relación inferida (inducida por algoritmos o modelos de lenguaje) al estatus de hecho comprobado, se aplican tres salvaguar... |
| **P04-F16** | ¿Qué variables, categorías, relaciones y condiciones exige representar ontología y relaciones de forma estructurada? | ✅ Respondida | La representación estructurada de la ontología corporativa y sus relaciones exige: 1) Variables de nodo (`node_id`, `node_type`, `canonical_name`, `jurisdiction_rut_lei`, `valid... |
| **P04-F17** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ontología y relaciones? | ✅ Respondida | Los fundamentos sobre ontología y relaciones corporativas descansan en cuatro fuentes primarias del corpus: 1) EDM Council Financial Industry Business Ontology (FIBO, edición ma... |
| **P04-F18** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra ontología y relaciones sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Desambiguación y trazado de responsabilidad ante una contingencia operacional en una división minera. Entradas documentadas: 1) Entidad Matriz: 'Holding Minero de... |
| **P04-F19** | ¿Qué diferencia hay entre fecha del hecho, fecha de publicación y fecha de incorporación al sistema? | ✅ Respondida | La gestión rigurosa de memoria corporativa desacopla tres dimensiones temporales independientes: 1) Fecha del Hecho (Event Time / Valid Time): momento físico en que ocurrió el s... |
| **P04-F20** | ¿Cómo debe responderse una pregunta sobre lo que la empresa sabía o decía en una fecha histórica? | ✅ Respondida | Una consulta sobre el conocimiento o postura corporativa en una fecha histórica (Point-in-Time / As-of Query) debe responderse ejecutando un corte temporal retrospectivo estrict... |
| **P04-F21** | ¿Qué regla prevalece cuando un documento fue corregido, retirado o reemplazado? | ✅ Respondida | La regla que prevalece se rige por el Principio de No-Destrucción Histórica y Prevalencia de Superación Normativa (W3C DCAT-3 y PROV-O): 1) Regla de Inmutabilidad: el documento ... |
| **P04-F22** | ¿Qué variables, categorías, relaciones y condiciones exige representar versiones y temporalidad de forma estructurada? | ✅ Respondida | Representar versiones y temporalidad estructuradas exige: 1) Variables de marca temporal (`event_date_start`, `event_date_end`, `publication_date`, `system_ingestion_timestamp`)... |
| **P04-F23** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre versiones y temporalidad? | ✅ Respondida | Los hechos relativos a versiones y temporalidad corporativa se sustentan en cuatro fuentes primarias del corpus: 1) W3C DCAT-3 Data Catalog Vocabulary (mayo 2024), que define la... |
| **P04-F24** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra versiones y temporalidad sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Reexpresión de línea base de emisiones de Gases de Efecto Invernadero (GEI) tras la venta de un activo industrial. Entradas documentadas: 1) Meta original en Memo... |
| **P04-F25** | ¿Qué pasos permiten extraer tablas, anexos, cifras y notas de PDF, web y archivos ofimáticos? | ✅ Respondida | La extracción de tablas, anexos, cifras y notas en memorias corporativas complejas se ejecuta mediante un pipeline en 4 pasos especializados: 1) Análisis de Maquetación Sensible... |
| **P04-F26** | ¿Qué unidades de fragmentación preservan contexto y citas sin mezclar versiones? | ✅ Respondida | La arquitectura óptima de fragmentación es el 'Chunking Jerárquico de Dos Niveles' (Parent Document Retrieval): 1) Fragmentos Hijo (Child Chunks, 128 a 256 tokens): segmentos at... |
| **P04-F27** | ¿Cómo detectar errores de OCR, tablas incompletas y referencias cruzadas rotas? | ✅ Respondida | La detección de anomalías e inconsistencias en la ingesta se realiza mediante una triple batería de validadores algorítmicos: 1) Auditor de Paridad Tabular (Table Structure Audi... |
| **P04-F28** | ¿Qué variables, categorías, relaciones y condiciones exige representar ingesta y extracción de forma estructurada? | ✅ Respondida | Representar de forma estructurada el proceso de ingesta y extracción exige: 1) Variables de fragmento (`chunk_id`, `parent_chunk_id`, `chunk_index`, `page_number`, `bounding_box... |
| **P04-F29** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ingesta y extracción? | ✅ Respondida | Los hechos sobre ingesta y extracción de memorias corporativas se fundamentan en tres fuentes académicas y técnicas principales: 1) Gao et al. (diciembre 2023, arXiv:2312.10997)... |
| **P04-F30** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra ingesta y extracción sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Ingesta de la 'Tabla de Emisiones de GEI y Consumo Energético' (pág. 92 de la Memoria Integrada 2025). Entradas documentadas: PDF con tabla compleja que abarca do... |
| **P04-F31** | ¿Quién puede crear, aprobar, corregir, leer o retirar cada clase de información? | ✅ Respondida | La gobernanza del corpus corporativo se estructura en una Matriz RACI estricta por tipo documental: 1) Hechos Esenciales e Información Privilegiada (Ley 18.045): Creación exclus... |
| **P04-F32** | ¿Cómo se trasladan los permisos del origen a búsqueda, respuestas y exportaciones? | ✅ Respondida | El traslado inquebrantable de permisos desde el documento de origen hacia los motores de búsqueda, respuestas generadas y exportaciones se ejecuta bajo el estándar NIST SP 800-1... |
| **P04-F33** | ¿Qué registro de cambios y revisión humana exige una afirmación sensible? | ✅ Respondida | Toda afirmación corporativa calificada como sensible (compromisos ambientales, cifras financieras preliminares, posturas en litigios o planes laborales) exige un protocolo de 'D... |
| **P04-F34** | ¿Qué variables, categorías, relaciones y condiciones exige representar gobierno y permisos de forma estructurada? | ✅ Respondida | Representar de forma estructurada gobierno y permisos exige: 1) Variables de sujeto y objeto ABAC (`user_role`, `user_department`, `user_clearance_level`, `resource_security_cla... |
| **P04-F35** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre gobierno y permisos? | ✅ Respondida | Los hechos relativos a gobierno y control de acceso se fundamentan en tres fuentes normativas y científicas: 1) NIST SP 800-162 Guide to Attribute Based Access Control (actualiz... |
| **P04-F36** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra gobierno y permisos sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Control de embargo y prevención de fuga de información privilegiada ante un Hecho Esencial de adquisición. Entradas documentadas: 1) Documento en preparación: 'Bo... |
| **P04-F37** | ¿Qué preguntas debe resolver la búsqueda exacta, semántica o híbrida? | ✅ Respondida | La arquitectura de recuperación distribuye las consultas según su tipología lingüística y estructural: 1) Búsqueda Exacta / Léxica (BM25): resuelve consultas puntuales con ident... |
| **P04-F38** | ¿Cómo se seleccionan citas suficientes para respaldar cifras, fechas y compromisos? | ✅ Respondida | La selección de citas suficientes se fundamenta en la metodología de Atribución Factual a Nivel de Oración (Sentence-Level Attribution; Bohnet et al., 2022; Yue et al., 2023): 1... |
| **P04-F39** | ¿Cuándo debe abstenerse el sistema por conflicto, vencimiento o falta de evidencia? | ✅ Respondida | El sistema debe activar el protocolo de 'Abstención Activa Segura' (Self-RAG / CRAG; Asai et al., 2023; Yan et al., 2024) en tres circunstancias operacionales estrictas: 1) Falt... |
| **P04-F40** | ¿Qué variables, categorías, relaciones y condiciones exige representar búsqueda y respuesta fundada de forma estructurada? | ✅ Respondida | Representar de forma estructurada la búsqueda y respuesta fundada exige: 1) Variables de respuesta (`response_id`, `query_text`, `generated_text`, `epistemic_status`: 'fact_supp... |
| **P04-F41** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre búsqueda y respuesta fundada? | ✅ Respondida | Los hechos relativos a la búsqueda y respuesta fundada se sustentan en cuatro fuentes académicas fundacionales: 1) Khattab & Zaharia (abril 2020, ColBERT, arXiv:2004.12832), que... |
| **P04-F42** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra búsqueda y respuesta fundada sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Consulta de prensa sobre compromisos de diversidad de género en cargos directivos. Entradas documentadas: 1) Pregunta recibida: '¿Cuál es la meta de participación... |
| **P04-F43** | ¿Qué métricas muestran completitud, actualidad y recuperabilidad del corpus? | ✅ Respondida | La calidad y salud operativa del corpus documental corporativo se evalúa mediante un cuadro de mando integral con tres grupos de métricas observables: 1) Completitud del Corpus:... |
| **P04-F44** | ¿Cómo se evalúan respuestas sobre compromisos con un conjunto de casos de referencia? | ✅ Respondida | La evaluación de respuestas sobre compromisos corporativos se ejecuta contra un 'Gold Standard Evaluation Dataset' compuesto por 250 casos de prueba reales de asuntos corporativ... |
| **P04-F45** | ¿Qué prueba adversarial revela fugas de permisos o mezcla de clientes? | ✅ Respondida | La prueba adversarial estándar para verificar el aislamiento de permisos y prevenir la mezcla de clientes (Multi-Tenant Isolation) es la 'Batería de Penetración Semántica y Jail... |
| **P04-F46** | ¿Qué variables, categorías, relaciones y condiciones exige representar evaluación de calidad documental de forma estructurada? | ✅ Respondida | Representar de forma estructurada la evaluación de calidad documental exige: 1) Variables métricas cuantitativas (`faithfulness_score`, `citation_precision`, `citation_recall`, ... |
| **P04-F47** | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre evaluación de calidad documental? | ✅ Respondida | Los hechos relativos a la evaluación de calidad documental se sustentan en cuatro fuentes académicas rigurosas: 1) Min et al. (mayo 2023, FActScore, arXiv:2305.14251, EMNLP), qu... |
| **P04-F48** | ¿Qué caso concreto, con entradas y resultado esperado, ilustra evaluación de calidad documental sin introducir datos no documentados? | ✅ Respondida | Caso Canónico: Ejecución de la suite de auditoría de factualidad y seguridad sobre un release del motor de inteligencia corporativa. Entradas documentadas: 1) Suite de evaluació... |
| **P04-C01** | ¿Dónde discrepan fuentes originales y síntesis internas sobre inventario de documentos corporativos, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: Los enfoques comerciales estándar y repositorios ofimáticos tratan cualquier archivo corporativo (PDF de memoria, comunicado de prensa o minuta interna) ... |
| **P04-C02** | ¿Qué sigue sin prueba sobre inventario de documentos corporativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Sigue sin prueba empírica formal la compatibilidad automatizada completa entre los catálogos documentales estructurados bajo CMF NCG 461 y los estándares ... |
| **P04-C03** | ¿Dónde discrepan fuentes originales y síntesis internas sobre afirmaciones y compromisos, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: La industria de software corporativo y soluciones de IA generativa proclama que 'un LLM puede identificar automáticamente promesas y logros corporativos ... |
| **P04-C04** | ¿Qué sigue sin prueba sobre afirmaciones y compromisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Permanece sin resolver empíricamente la detección automatizada del 'abandono silencioso de compromisos' (drift o meta abandonada). Ocurre cuando una empre... |
| **P04-C05** | ¿Dónde discrepan fuentes originales y síntesis internas sobre ontología y relaciones, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: Soluciones comerciales de bases de datos de grafos para empresas promueven la extracción automática de entidades y relaciones mediante LLMs ('Zero-shot O... |
| **P04-C06** | ¿Qué sigue sin prueba sobre ontología y relaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Falta una ontología de dominio abierta y validada empíricamente para el ecosistema societario y regulatorio chileno, que interopere nativamente entre el R... |
| **P04-C07** | ¿Dónde discrepan fuentes originales y síntesis internas sobre versiones y temporalidad, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: La práctica de ingeniería de software documental convencional recurre con frecuencia a la 'reindexación por sobreescritura' (batch overwrite nocturno) o ... |
| **P04-C08** | ¿Qué sigue sin prueba sobre versiones y temporalidad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Sigue sin prueba empírica formal la resolución algorítmica de 'reexpresiones implícitas o silenciosas de líneas base' cuando una empresa altera una cifra ... |
| **P04-C09** | ¿Dónde discrepan fuentes originales y síntesis internas sobre ingesta y extracción, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: La mayoría de tutoriales y frameworks de desarrollo rápido de RAG recomiendan segmentación por longitud fija (e.g. 500 tokens con overlap de 50) como rec... |
| **P04-C10** | ¿Qué sigue sin prueba sobre ingesta y extracción, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Permanece sin prueba empírica la extracción completamente desatendida de tablas multipágina con celdas fusionadas asimétricas y notas al pie en memorias d... |
| **P04-C11** | ¿Dónde discrepan fuentes originales y síntesis internas sobre gobierno y permisos, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: Múltiples aplicaciones comerciales de 'Chat con tus documentos' implementan el control de permisos delegando en el prompt del LLM la orden de no divulgar... |
| **P04-C12** | ¿Qué sigue sin prueba sobre gobierno y permisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Sigue sin prueba empírica formal la gestión desatendida del levantamiento anticipado de embargos en situaciones de crisis de mercado (e.g. filtración en p... |
| **P04-C13** | ¿Dónde discrepan fuentes originales y síntesis internas sobre búsqueda y respuesta fundada, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: Soluciones comerciales de RAG afirman que 'incluir la instrucción "cite sus fuentes" en el prompt del sistema es suficiente para obtener respuestas traza... |
| **P04-C14** | ¿Qué sigue sin prueba sobre búsqueda y respuesta fundada, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Sigue sin prueba empírica comparativa el balance óptimo entre latencia de respuesta y completitud analítica al contrastar Búsqueda Híbrida (ColBERT) vs Gr... |
| **P04-C15** | ¿Dónde discrepan fuentes originales y síntesis internas sobre evaluación de calidad documental, y qué versión prevalece según las correcciones? | ✅ Respondida | Discrepancia Principal: Múltiples proveedores y prácticas informales de evaluación de LLMs consideran que una evaluación global binaria o subjetiva ('thumbs up / thumbs down' o ... |
| **P04-C16** | ¿Qué sigue sin prueba sobre evaluación de calidad documental, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | ✅ Respondida | Vacío e Incertidumbre: Sigue sin prueba empírica formal el comportamiento del sistema ante una crisis reputacional en tiempo real, donde coexisten tres factores de estrés simult... |

---

## 4. Vacíos Epistémicos y Fuentes Parciales Identificadas

A partir del análisis de las 16 preguntas de contraste (C01–C16) y del documento `P04_GAPS_AND_VALIDATION`, se consolidan 8 vacíos epistémicos y sus agendas de validación técnica:

- **GAP-P04-01: Homologación CMF vs ESRS:** Incertidumbre en la compatibilidad automatizada entre memorias chilenas NCG 461 y estándares europeos ESRS debido al fallo de ingesta F-01 (EFRAG). Requiere auditoría de schema mapping con PDFs oficiales.
- **GAP-P04-02: Abandono Silencioso de Metas (Goal Drift):** Falta de algoritmos para detectar cuando una meta de un año base es discontinuada silenciosamente en memorias posteriores sin justificación formal.
- **GAP-P04-03: Ontología Localizada Chilena:** Ausencia de ontologías públicas que vinculen la jerarquía societaria de la CMF (RUT) con resoluciones ambientales (RCA del SEIA/SMA). Requiere desarrollo de extensión sobre FIBO.
- **GAP-P04-04: Reexpresiones Tácitas de Línea Base:** Carencia de herramientas que concilien automáticamente variaciones en series temporales históricas reportadas entre memorias consecutivas sin notas al pie explicativas.
- **GAP-P04-05: Precisión en Tablas Multipágina Complejas:** Fragilidad observada en parsers abiertos ante tablas financieras consolidadas y matrices ESG. Requiere prueba piloto sobre 15 memorias CMF (precisión ≥ 98%).
- **GAP-P04-06: Liberación de Emergencia de Embargos:** Falta de validación empírica sobre la latencia de propagación de excepciones de embargo en tiempo real ante contingencias de filtración de prensa (< 60 segundos).
- **GAP-P04-07: Trade-off Costo-Latencia GraphRAG vs ColBERT:** Falta de telemetría comparativa de inferencia y consumo de tokens entre clustering jerárquico GraphRAG y búsqueda híbrida ColBERT sobre memorias corporativas en español.
- **GAP-P04-08: Simulación de Gabinete de Crisis:** Necesidad de someter al sistema a una prueba de estrés de vocería en 3 escenarios reales (greenwashing, agua, filtración) con tiempo de preparación < 3 minutos y cero fuga ABAC.

---

## 5. Implicancias Arquitectónicas para el Proyecto BRIDGE (Módulo Memoria)

Los hallazgos del Pilar P04 imponen cuatro requerimientos arquitectónicos estructurales para el módulo **Memoria** de BRIDGE:

1. **Contrato de Datos Inmutable (Ficha Canónica de Compromiso):** BRIDGE no debe almacenar compromisos como texto libre. Debe implementar el JSON-Schema formalizado en P04 con tipificación estricta de baseline, target, milestones, status y hash criptográfico SHA-256 de página.
2. **Almacenamiento Híbrido Dual (Grafo Semántico + Almacén Vectorial):** La arquitectura debe combinar una base de grafos (RDF TripleStore / Neo4j bajo FIBO y W3C PROV-O) para relaciones de jerarquía societaria, linaje de vocería y trazabilidad causal, junto con una base vectorial filtrada para búsqueda semántica local.
3. **Pipeline de Ingesta Layout-Aware con Chunking Jerárquico:** El pre-procesamiento documental debe descartar el chunking ciego por caracteres y operar con Parent Document Retrieval (hijos de 128-256 tokens mapeados a padres de 1.024-2.048 tokens), incorporando auditores de paridad de tablas y resolución de notas al pie.
4. **Motor de Búsqueda Adaptativo y Guardrails de Certificación:** Integración de un router tripartito (BM25 + ColBERT + GraphRAG Leiden), gobernado por Pre-Retrieval ABAC Filtering (NIST SP 800-162) y compuertas automáticas de factualidad atómica (FActScore ≥ 0.95 y precisión de citas ≥ 0.98) antes de presentar minutas a directivos.

---

## 6. Estado de Auditoría y Verificación de Cumplimiento

- **Auditoría de Esquema (20 Atributos):** 100% de los 64 registros validados en `respuestas/P04.jsonl`.
- **Muestra Estratificada del 10%+:** 7 registros seleccionados aleatoriamente (`P04-F41`, `P04-F08`, `P04-F02`, `P04-F48`, `P04-F18`, `P04-C08`, `P04-C04`) auditados con 100% de conformidad contra el manifiesto `fuentes/P04.json`.
- **Trazabilidad Normativa y Epistémica:** Todos los hechos documentados cuentan con títulos de fuentes oficiales, fechas, localizadores exactos y fragmentos sustantivos comprobables.
- **Ausencia de Alucinaciones:** Cero datos no documentados; todas las afirmaciones comerciales y vacíos están formalmente tipificados.

---

## 7. Próximos Pasos (Avance Autónomo)

Concluido íntegramente el Pilar P04, el programa de investigación avanza de inmediato al siguiente cuaderno en la secuencia canónica del mandato:

- **Siguiente Pilar:** **P05 — Metodologías de análisis y síntesis**
- **Notebook ID Verificado:** `0fc2e780-e279-4923-83c5-90fe621a4543` (36 fuentes identificadas)
- **Alcance P05:** 64 preguntas (48 Fundamentales F01–F48, 16 Contraste C01–C16)
- **Procedimiento Inmediato:** Creación de manifiesto congelado `fuentes/P05.json`, revisión de evidencias y precedencia editorial, ejecución secuencial F->C y síntesis ejecutiva sin esperar autorizaciones rutinarias.
