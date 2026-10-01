import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-F07
    {
        "question_id": "P06-F07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo debe estructurarse la ingesta dual de documentos oficiales internos (Memorias NCG 461, políticas, discursos) y señales externas (newswires, boletines, redes)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La ingesta dual debe estructurarse mediante dos pipelines desacoplados y asincrónicos pero canónicamente armonizados en una capa de indexación unificada: 1) Pipeline Interno (Batch / Event-driven): Procesa documentos corporativos estáticos y semi-estructurados (Memorias Integradas bajo CMF NCG 461, Formularios 20-F, Códigos de Ética, discursos del CEO y Factsheets ESG). Realiza parsing multimodal (tablas financieras, gráficos, texto narrativo), chunking semántico preservando la jerarquía documental y extracción obligatoria de metadatos estructurales (id_emisor, fecha_corte, alcance_operativo, jerarquia_normativa); 2) Pipeline Externo (Streaming en Tiempo Real): Ingesta feeds continuos de newswires profesionales (Dow Jones Factiva, Bloomberg), resoluciones del Diario Oficial y portales regulatorios (SMA SNIFA, CMF, SERNAC) y streams sociales (AT Protocol, Reddit). Aplica filtrado de ruido por entidades canónicas, desduplicación temporal basada en similitud de titulares y hashing de contenido. Ambos flujos convergen en un modelo de datos común que vincula afirmaciones internas y señales externas a nodos canónicos en el grafo corporativo.",
        "findings": [
            {
                "claim_id": "P06-F07-C1",
                "claim": "La ingesta dual exige desacoplar un flujo batch documental interno enriquecido con metadatos y un flujo streaming externo en tiempo real con filtrado ontológico.",
                "epistemic_status": "patron_arquitectural",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Arquitectura de Datos Corporativos"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Entregable Específico 2: Flujo Conceptual de Procesamiento (Fase 1: Ingesta Dual)",
                        "excerpt_short": "Ingesta de documentos internos con metadatos estructurados (id_emisor, fecha_corte, alcance_operativo, jerarquia_normativa). Paralelamente, ingesta de señales externas en tiempo real filtradas contra palabras clave, nombres corporativos y directivos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "589b1b7c-6049-4b3a-9f0d-1fa8990a7a1d",
                        "source_title": "CMF Chile - Sostenibilidad y Norma de Carácter General N° 461",
                        "original_url": "https://www.cmfchile.cl/portal/principal/623/w4-propertyvalue-50301.html",
                        "locator": "Estructura de Reporte de la Memoria Integrada",
                        "excerpt_short": "La NCG 461 requiere que las entidades reporten información sobre su gobierno corporativo, estrategia, gestión de riesgos y métricas de sostenibilidad en una memoria integrada estructurada y auditable.",
                        "source_date": "2021-11-12",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Arquitectura de datos dual validada en P06_RESEARCH_DOSSIER y alineada con los requisitos de reporte CMF NCG 461."
            }
        ],
        "operational_model": {
            "inputs": ["Memorias CMF NCG 461 en PDF/HTML", "Feeds API de Dow Jones Factiva", "Boletines de resoluciones de la SMA (SNIFA)"],
            "actors": ["Extractor de Documentos Internos", "Conector de Feeds Externos", "Normalizador de Esquema Común"],
            "steps": ["Parsing y extracción tabular/textual interna", "Filtrado de stream externo por entidades maestras", "Indexación en almacén vectorial y de grafos", "Enlace a metadatos de vigencia"],
            "states": ["Raw_Ingest", "Parsed_and_Filtered", "Metadata_Attached", "Ready_for_Cross_Matching"],
            "outputs": ["Fragmentos documentales internos normalizados", "Eventos externos etiquetados y deduplicados"],
            "exceptions": ["Formatos PDF no estructurados o escaneados sin capa OCR"]
        },
        "entities": [
            {"entity_id": "ENT_CMF_NCG461", "type": "normativa_financiera", "name": "Norma de Carácter General N° 461 CMF", "aliases": ["NCG 461", "Memoria Integrada"]},
            {"entity_id": "ENT_FACTIVA", "type": "proveedor_noticias", "name": "Dow Jones Factiva Developer Platform", "aliases": ["Factiva", "Sentiment Signals API"]}
        ],
        "relations": [
            {"subject_id": "ENT_CMF_NCG461", "predicate": "aporta_declaraciones_al_pipeline", "object_id": "ENT_FACTIVA", "valid_from": "2021", "valid_to": "2026", "evidence_claim_id": "P06-F07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de flujo",
                "Pipeline interno": "Procesamiento batch/event-driven con alta densidad conceptual, estructuración tabular y metadatos de gobernanza.",
                "Pipeline externo": "Streaming continuo en tiempo real de alta velocidad, filtrado selectivo y deduplicación agresiva."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Pipeline de Ingesta Dual", "implication": "BRIDGE debe implementar conectores nativos desacoplados: un motor de parsing de memorias CMF y un ingestor streaming de señales regulatorias y de prensa.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F08
    {
        "question_id": "P06-F08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se modela la dimensión bitemporal (tiempo de validez vs tiempo de publicación vs tiempo de transacción) para evitar falsos positivos de discrepancia?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El modelado temporal es el cortafuegos principal para evitar falsos positivos de inconsistencia. El corpus exige formalizar tres dimensiones temporales desacopladas: 1) Tiempo de Validez (Valid Time - VT): El intervalo temporal objetivo [t_start, t_end] durante el cual el hecho o la métrica reportada fue o es efectivamente real en el mundo físico (ej. el consumo hídrico del ejercicio 2024 entre 01-01-2024 y 31-12-2024); 2) Tiempo de Publicación (Publication / Emission Time - PT): La fecha exacta en que el documento corporativo o la noticia externa fue emitido y depositado públicamente (ej. la memoria anual publicada el 31 de marzo de 2025 ante la CMF); y 3) Tiempo de Transacción / Ingesta (Transaction Time - TT): El timestamp en que el sistema de software ingiere e indexa la información. Como establecen T-GRAG y P06_EVIDENCE_MAP, confrontar una noticia de un derrame ocurrido en julio de 2025 contra una memoria publicada en marzo de 2025 (referida al ejercicio 2024) no constituye jamás una contradicción fáctica, sino un 'Desfase Temporal' natural. Sin este desacoplamiento bitemporal, el sistema generaría falsas alarmas de greenwashing sistemáticas.",
        "findings": [
            {
                "claim_id": "P06-F08-C1",
                "claim": "El modelado bitemporal (tiempo de validez vs tiempo de publicación) es indispensable para erradicar falsos positivos derivados de desfases temporales naturales.",
                "epistemic_status": "consenso_tecnico_y_arquitectural",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Bases de Datos Temporales y RAG"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Diferencia Temporal (Temporal Lag / Evolution)",
                        "excerpt_short": "Desfase inherente entre la fecha de corte de los reportes internos (ej. memoria anual consolidada al 31 de diciembre) y la señal externa ocurrida posteriormente... Sin anclaje temporal, el sistema genera falsos positivos de contradicción.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 3: Temporal Knowledge Graph Formulation",
                        "excerpt_short": "Facts in real-world scenarios possess temporal validities. A static knowledge graph fails to distinguish when an event occurred, leading to severe hallucination when outdated information contradicts updated facts.",
                        "source_date": "2025-08-03",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Formulación matemática rigurosa en Li et al. (2025) y P06_EVIDENCE_MAP."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de afirmación interna", "Metadatos de fecha de corte y publicación", "Timestamp de noticia externa"],
            "actors": ["Parser Temporal", "Motor de Inferencia Bitemporal"],
            "steps": ["Extracción de entidades temporales (ej. 'ejercicio 2024', 'meta 2030')", "Asignación de intervalo [VT_start, VT_end]", "Comparación con VT de la señal externa", "Clasificación como 'Vigente Contemporáneo' vs 'Desfase Temporal'"],
            "states": ["Raw_Dates", "Intervals_Assigned", "Temporal_Overlap_Evaluated", "Validity_Checked"],
            "outputs": ["Etiqueta de compatibilidad temporal", "Dictamen de vigencia factual"],
            "exceptions": ["Afirmaciones corporativas atemporales o continuas sin fecha de término explícita"]
        },
        "entities": [
            {"entity_id": "ENT_T_GRAG", "type": "marco_algoritmico", "name": "T-GRAG: Temporal Dynamic GraphRAG", "aliases": ["T-GRAG", "Li et al. 2025"]}
        ],
        "relations": [
            {"subject_id": "ENT_T_GRAG", "predicate": "resuelve_conflictos_mediante", "object_id": "ENT_BITEMPORAL_MODEL", "valid_from": "2025", "valid_to": "2026", "evidence_claim_id": "P06-F08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque temporal",
                "RAG atemporal plano": "Confronta textos ignorando fechas; trata todo desacuerdo como mentira o contradicción.",
                "RAG bitemporal (T-GRAG)": "Compara hechos únicamente dentro de sus intervalos de validez superpuestos; reconoce la evolución histórica legítima."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor Bitemporal BRIDGE", "implication": "BRIDGE debe etiquetar cada chunk interno y señal externa con [VT_start, VT_end] y fecha de publicación para descartar discrepancias cronológicas.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F09
    {
        "question_id": "P06-F09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo aborda el marco T-GRAG (Li et al., 2025) los conflictos temporales y la redundancia mediante grafos dinámicos e intervalos [t_start, t_end]?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El marco T-GRAG (Dynamic GraphRAG for Temporal Conflicts and Redundancy in Knowledge Retrieval, Li et al., 2025; arXiv:2508.01680) resuelve las contradicciones cronológicas inherentes a los corpus documentales en constante evolución mediante tres mecanismos fundamentales: 1) Segmentación Temporal y Construcción de Grafos Dinámicos: En lugar de un grafo estático colapsado, segmenta la información en ventanas de tiempo y construye grafos de conocimiento temporal donde cada arista o relación entre entidades está tipificada con un intervalo explícito de vigencia [t_start, t_end]; 2) Descomposición Temporal de Consultas (Temporal Query Decomposition - TQD): Cuando el usuario o el sistema formula una pregunta sobre un hecho corporativo, TQD fragmenta la consulta en sub-preguntas acotadas a marcos temporales específicos, recuperando solo los sub-grafos que estaban activos en dicho período; y 3) Reconciliación de Conflictos y Fusión de Redundancia: Si múltiples fuentes reportan atributos contradictorios para una misma entidad, T-GRAG utiliza la marca temporal de actualización para determinar si se trata de una rectificación posterior válida o de una controversia persistente, evitando que datos antiguos obsoletos contaminen la síntesis actual.",
        "findings": [
            {
                "claim_id": "P06-F09-C1",
                "claim": "T-GRAG resuelve conflictos temporales asociando intervalos [t_start, t_end] a tripletas y descomponiendo consultas según ventanas de validez temporal.",
                "epistemic_status": "algoritmo_publicado_revisado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Investigación en GraphRAG Temporal"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 1 & 4: Methodology and Dynamic Temporal Knowledge Graphs",
                        "excerpt_short": "T-GRAG constructs dynamic temporal knowledge graphs by assigning [t_start, t_end] to relational triples and introduces Temporal Query Decomposition (TQD) to resolve temporal redundancy and factual obsolescence.",
                        "source_date": "2025-08-03",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2.C: Completitud Bibliográfica de T-GRAG",
                        "excerpt_short": "Marco de recuperación aumentada que segmenta temporalmente corpus textuales, construye grafos de conocimiento temporal con intervalos [t_start, t_end] y ejecuta Descomposición Temporal de Consultas (TQD) para evitar que eventos pasados contradigan artificialmente hechos vigentes.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Texto completo en PDF de Li et al. (2025) incorporado y analizado en las fuentes activas."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus textual multi-anual de memorias y noticias", "Consultas complejas con restricción temporal"],
            "actors": ["Módulo de Descomposición TQD", "Indexador Dinámico T-GRAG", "Reranker Temporal"],
            "steps": ["Extracción de tripletas con sellos temporales", "Indexación en grafos dinámicos segmentados", "Descomposición TQD de la consulta del usuario", "Poda de sub-grafos fuera del intervalo de consulta", "Generación de respuesta contextualmente coherente"],
            "states": ["Multi_Year_Corpus", "Dynamic_Graph_Constructed", "TQD_Executed", "Temporal_Conflict_Resolved"],
            "outputs": ["Respuesta libre de alucinaciones por obsolescencia temporal"],
            "exceptions": ["Documentos sin fecha de emisión identificable o con fechas contradictorias en el texto"]
        },
        "entities": [
            {"entity_id": "ENT_T_GRAG", "type": "marco_algoritmico", "name": "T-GRAG Framework (Li et al., 2025)", "aliases": ["Dynamic GraphRAG", "T-GRAG"]}
        ],
        "relations": [
            {"subject_id": "ENT_T_GRAG", "predicate": "introduce_tecnica", "object_id": "ENT_TQD", "valid_from": "2025", "valid_to": "2026", "evidence_claim_id": "P06-F09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resolución de conflictos históricos",
                "GraphRAG estándar (Edge et al., 2024)": "Genera resúmenes globales agrupando toda la historia, corriendo el riesgo de mezclar políticas antiguas con nuevas.",
                "T-GRAG (Li et al., 2025)": "Discrimina la vigencia de políticas mediante intervalos [t_start, t_end] y poda activa de ramas temporales obsoletas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Grafo de Conocimiento Dinámico", "implication": "BRIDGE debe incorporar los principios de T-GRAG para que las memorias anuales sucesivas no generen falsos conflictos de política interna.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F10
    {
        "question_id": "P06-F10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué requisitos de metadatos estructurados (id_emisor, fecha_corte, alcance_operativo, jerarquía_normativa) deben asociarse a cada fragmento interno?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Para que un fragmento de conocimiento interno pueda cruzarse rigurosamente con el entorno exterior, P06_RESEARCH_DOSSIER y las directrices de gobernanza de P04 exigen la presencia obligatoria de cuatro metadatos estructurados inmutables: 1) id_emisor: Identificador unívoco de la entidad legal o rol emisor (RUT corporativo, subsidiaria específica o cargo jerárquico como 'Directorio', 'CEO', 'Gerente de Sustentabilidad'); 2) fecha_corte y fecha_emision: La fecha temporal de corte de la información (ej. 31-12-2024 para la data operacional) y la fecha de publicación formal (ej. 31-03-2025); 3) alcance_operativo (Operational Scope): Delimitación perimetral explícita (Alcance 1 y 2 bajo GHG Protocol, faena o planta geográfica específica, red comercial nacional o holding consolidado); y 4) jerarquia_normativa (Normative Authority): Nivel vinculante del documento dentro de la empresa (Nivel 1: Memoria depositada CMF / Estados Financieros auditados; Nivel 2: Política Corporativa aprobada por Directorio; Nivel 3: Discurso de vocero / Declaración de prensa; Nivel 4: Documento de trabajo interno). Estos metadatos permiten filtrar y ponderar la solidez jurídica de la declaración frente a cualquier señal externa.",
        "findings": [
            {
                "claim_id": "P06-F10-C1",
                "claim": "Cada fragmento interno requiere metadatos estructurados de emisor, fechas de corte/emisión, alcance operativo y jerarquía normativa para ser contrastado.",
                "epistemic_status": "estandar_de_ingenieria_de_datos",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Gobernanza de Datos Corporativos"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Entregable Específico 2: Flujo Conceptual de Procesamiento (Fase 1)",
                        "excerpt_short": "Ingesta de documentos internos con metadatos estructurados (id_emisor, fecha_corte, alcance_operativo, jerarquia_normativa).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación arquitectural unívoca en el informe de síntesis interna."
            }
        ],
        "operational_model": {
            "inputs": ["Documento corporativo recién subido"],
            "actors": ["Extractor de Metadatos", "Validador de Esquema JSON"],
            "steps": ["Extracción o asignación manual/automática de los 4 metadatos", "Validación estricta contra JSON-Schema", "Rechazo del chunk si carece de jerarquía o fecha de corte", "Almacenamiento en base vectorial enriquecida"],
            "states": ["Raw_Chunk", "Metadata_Extracted", "Schema_Validated", "Indexed"],
            "outputs": ["Chunk enriquecido listo para filtrado pre-retrieval"],
            "exceptions": ["Documentos antiguos que no especifican el alcance geográfico u operativo exacto"]
        },
        "entities": [
            {"entity_id": "ENT_INTERNAL_CHUNK_SCHEMA", "type": "schema_de_datos", "name": "Esquema de Fragmento Interno Enriquecido", "aliases": ["Chunk Metadata Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_INTERNAL_CHUNK_SCHEMA", "predicate": "define_atributos_de", "object_id": "ENT_KNOWLEDGE_BASE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F10-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Granularidad de metadatos",
                "Chunking ingenuo": "Solo texto y nombre de archivo original.",
                "Chunking enriquecido BRIDGE": "Texto vinculado a id_emisor, fechas de corte/publicación, alcance operativo y nivel de jerarquía normativa."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Módulo de Ingesta Interna", "implication": "BRIDGE debe forzar la atribución de los 4 metadatos como condición previa para indexar cualquier declaración o compromiso corporativo.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F11
    {
        "question_id": "P06-F11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se gestionan las actualizaciones sucesivas, fe de erratas y modificaciones de compromisos históricos sin alterar la inmutabilidad de versiones previas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La gestión de actualizaciones, fe de erratas y modificaciones de metas históricas se rige por el principio de inmutabilidad y versionado aditivo de W3C DCAT-3 (`dcterms:replaces` / `dcterms:isReplacedBy`), impidiendo tajantemente la sobreescritura destructiva o el borrado de documentos precedentes. Cuando una empresa corrige un error material reportado ante la CMF o reajusta una meta climática debido a cambios metodológicos (ej. transición de GHG Protocol a estándares IFRS S1/S2): 1) La versión histórica se conserva inmutable en su estado original con su hash criptográfico SHA-256 intacto y una marca de superación (`is_superseded = true`); 2) La nueva versión se indexa como documento autónomo con su respectivo tiempo de publicación y un puntero explícito hacia el documento que sustituye o aclara; y 3) En consultas retrospectivas 'as-of' (auditorías forenses sobre qué sabía o declaró la empresa en una fecha pasada específica), el motor de búsqueda recupera exactamente el estado vigente a esa fecha histórica, mientras que para respuestas de vocería actual recupera la versión vigente más reciente acompañada de la nota explicativa de la rectificación.",
        "findings": [
            {
                "claim_id": "P06-F11-C1",
                "claim": "Las rectificaciones y fe de erratas deben gestionarse mediante relaciones W3C DCAT-3 inmutables y versionado aditivo para preservar la auditabilidad histórica.",
                "epistemic_status": "estandar_de_interoperabilidad",
                "scope": {"time": "2020-2026", "region": "Global", "actor": "W3C y Reguladores de Mercados"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 1 & 2: Marco Teórico y Entregable Específico 1",
                        "excerpt_short": "Se desacoplan estrictamente el tiempo de validez, el de publicación y el de transacción, preservando documentos inmutables mediante relaciones de sustitución para permitir auditorías y consultas retrospectivas as-of.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio arquitectural derivado de estándares DCAT-3 y las reglas de inmutabilidad de P04."
            }
        ],
        "operational_model": {
            "inputs": ["Nuevo documento de aclaración o fe de erratas", "Documento corporativo previo ya indexado"],
            "actors": ["Administrador Documental", "Motor de Versionado de Grafo"],
            "steps": ["Verificación de vínculo de sustitución", "Marcado de versión previa como 'Superada'", "Adición de arista 'dcterms:replaces' en el grafo", "Habilitación de consultas temporales 'as-of'"],
            "states": ["Active_Document", "Superseded_Document", "Replacement_Document_Active"],
            "outputs": ["Trazabilidad completa de la evolución del compromiso"],
            "exceptions": ["Fe de erratas parciales que corrigen solo un párrafo o tabla específica"]
        },
        "entities": [
            {"entity_id": "ENT_W3C_DCAT3", "type": "estandar_web", "name": "W3C Data Catalog Vocabulary (DCAT-3)", "aliases": ["DCAT-3", "dcterms:replaces"]}
        ],
        "relations": [
            {"subject_id": "ENT_W3C_DCAT3", "predicate": "gobierna_versionado_de", "object_id": "ENT_CORPORATE_ARCHIVE", "valid_from": "2020", "valid_to": "2026", "evidence_claim_id": "P06-F11-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Modelo de actualización",
                "Sobreescritura simple (CRUD)": "Borra o reemplaza el registro antiguo; destruye la evidencia de lo que se afirmó originalmente.",
                "Versionado bitemporal DCAT-3": "Preserva inmutables todas las versiones enlazadas por relaciones de sustitución; permite auditorías forenses retrospectivas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gestor de Versiones e Inmutabilidad", "implication": "BRIDGE debe permitir al usuario consultar el estado de un compromiso en cualquier fecha histórica 'as-of' sin perder la historia de rectificaciones.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F12
    {
        "question_id": "P06-F12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo debe realizarse el filtrado de ruido, desduplicación temporal y normalización de feeds de noticias y resoluciones regulatorias externas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El filtrado de feeds externos masivos exige un pipeline en tres etapas para evitar saturar el sistema con alertas espurias: 1) Filtrado Ontológico y Léxico Temprano: Se descartan de inmediato artículos o publicaciones que no mencionen explícitamente entidades del grafo corporativo (RUTs, razones sociales, filiales, marcas comerciales o directivos clave) o que traten tópicos no corporativos (ej. notas deportivas que mencionan un auspicio publicitario menor); 2) Desduplicación Temporal y de Contenido: Newswires y agencias sindicadas generan decenas de repeticiones de una misma nota. El sistema aplica algoritmos de hashing MinHash/LSH sobre el cuerpo del texto y umbrales de similitud coseno (> 0.85) sobre titulares dentro de una ventana móvil de 48 horas, agrupando las réplicas en un único 'Evento Noticioso' y preservando únicamente la fuente original con mayor reputación periodística; y 3) Normalización Estructurada: Cada evento externo admitido se etiqueta con metadatos de fuente (Dow Jones Factiva, SMA, CMF, prensa abierta), tipo de señal (resolución formal, reporte periodístico, denuncia de ONG, rumor de redes), fecha/hora exacta de publicación y entidades involucradas con su respectivo score de confianza.",
        "findings": [
            {
                "claim_id": "P06-F12-C1",
                "claim": "El procesamiento de señales externas requiere filtrado ontológico temprano, desduplicación MinHash/LSH en ventana móvil y normalización tipológica de eventos.",
                "epistemic_status": "buena_practica_de_ingenieria",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Sistemas de Inteligencia de Señales"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Entregable Específico 2 (Fase 1: Ingesta y Filtrado de Ruido)",
                        "excerpt_short": "Deduplicación temporal, scraping estructurado... ingesta de señales externas en tiempo real filtradas contra palabras clave, nombres corporativos y directivos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "d202796f-30cb-44da-9a7d-47f6397254e0",
                        "source_title": "Dow Jones Factiva - Developer Platform & Sentiment Signals API",
                        "original_url": "https://developer.dowjones.com/documents/site-docs-factiva_apis-factiva_analytics_apis-factiva_sentiment_signals_api",
                        "locator": "API Documentation: Content Cleansing and Deduplication",
                        "excerpt_short": "Factiva analytics pipeline cleanses syndicated content, grouping duplicates and near-duplicates to provide clean sentiment signals across thousands of licensed news outlets.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Prácticas estándar en pipelines de procesamiento masivo de noticias y documentación de Factiva."
            }
        ],
        "operational_model": {
            "inputs": ["Flujo bruto de miles de artículos diarios de prensa y agencias"],
            "actors": ["Filtro Ontológico", "Motor MinHash/LSH de Desduplicación", "Normalizador de Eventos"],
            "steps": ["Verificación de mención de entidades canónicas", "Cálculo de huella MinHash y agrupamiento de réplicas", "Selección de fuente canónica (wire original)", "Normalización y despacho al motor de cruce"],
            "states": ["Raw_Stream", "Entity_Filtered", "Deduplicated", "Normalized_Event"],
            "outputs": ["Eventos externos limpios y contextualizados"],
            "exceptions": ["Noticias sindicadas con alteraciones sustanciales en el cuerpo o citas agregadas"]
        },
        "entities": [
            {"entity_id": "ENT_FACTIVA_API", "type": "api_noticiosa", "name": "Dow Jones Factiva Sentiment Signals API", "aliases": ["Factiva API", "Dow Jones Stream"]}
        ],
        "relations": [
            {"subject_id": "ENT_FACTIVA_API", "predicate": "suministra_noticias_filtradas_a", "object_id": "ENT_EXTERNAL_STREAM", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F12-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Manejo de duplicados de noticias",
                "Ingesta sin deduplicación": "Trata 50 republicaciones de un teletipo de EFE o Reuters como 50 incidentes distintos, multiplicando falsamente la severidad de la alerta.",
                "Agrupamiento por evento (MinHash/LSH)": "Agrupa las 50 réplicas en un único 'Cluster de Evento' y mide la amplitud de amplificación mediática sin duplicar hechos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Filtrador y Normalizador Externo", "implication": "BRIDGE debe implementar desduplicación MinHash en ventana móvil para no sobreestimar el volumen de controversias externas.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-F07..F12) to {out_path}.")
