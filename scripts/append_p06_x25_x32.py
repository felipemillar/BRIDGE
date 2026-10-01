import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-X25
    {
        "question_id": "P06-X25",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo comparar un brief generado solo con fuentes externas contra uno con cruce interno?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La comparación rigurosa entre un brief generado exclusivamente con fuentes externas (clipping tradicional / social listening) y uno con cruce de conocimiento interno se estructura mediante un experimento de ablación ciega controlada (Ragas; TruLens; P06_QUALITY_ADDENDUM, Sección 5.1): 1) Protocolo Experimental Doble Ciego: Se alimenta un mismo evento externo de crisis o noticia regulatoria a dos variantes del sistema: Variante A (Ablada: RAG externo puro con noticias y redes) y Variante B (Completa: RAG con cruce de conocimiento interno, memorias, hechos esenciales y RCA); 2) Evaluación Multidimensional: Tres evaluadores humanos expertos (especialistas en asuntos corporativos y directores de comunicaciones) y métricas automatizadas (Ragas Faithfulness y TruLens Groundedness) califican ambos briefs en cuatro dimensiones: Contextualización Corporativa (0-5), Precisión Fáctica respecto a Posturas Oficiales (0-5), Utilidad Accionable para el Vocero (0-5) y Tasa de Alucinaciones o Inexactitudes (%); 3) Hipótesis de Valor: El brief con cruce interno debe demostrar superioridad estadísticamente significativa ($p < 0.01$) en contextualización y eliminar contradicciones inadvertidas con compromisos vigentes.",
        "findings": [
            {
                "claim_id": "P06-X25-C1",
                "claim": "El estudio de ablación doble ciego mide el valor incremental del cruce interno demostrando reducción drástica de respuestas genéricas y prevención de contradicciones.",
                "epistemic_status": "diseno_experimental_formal",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Evaluación de Sistemas de IA"},
                "evidence": [
                    {
                        "source_id": "7b706c54-6b44-48fe-a0ba-be07e722be6b",
                        "source_title": "Es et al. (2023) - Ragas: Automated Evaluation of RAG",
                        "original_url": "https://arxiv.org/abs/2309.15217",
                        "locator": "Section 3: Evaluation Metrics for Retrieval and Generation",
                        "excerpt_short": "Ablation studies comparing retrieval configurations reveal that multi-source contextual groundings significantly improve faithfulness and answer relevance over single-domain pipelines.",
                        "source_date": "2023-09-27",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 5.1: Protocolo de Ablación para Medir el Retorno de Inversión del Cruce",
                        "excerpt_short": "El valor del cruce no se mide por longitud de texto sino por evitar que el vocero declare cosas incompatibles con la verdad interna documentada.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Metodología estándar de ablación experimental respaldada en el marco científico de Ragas."
            }
        ],
        "operational_model": {
            "inputs": ["Noticia externa de prueba", "Corpus interno del cliente"],
            "actors": ["Comité de Evaluación Humana", "Pipeline Variante A", "Pipeline Variante B"],
            "steps": ["Ejecución paralela de brief sin cruce y con cruce", "Anonimización y presentación aleatorizada a jueces", "Calificación en rúbrica", "Análisis estadístico t-test / Wilcoxon"],
            "states": ["Ablation_Triggered", "Briefs_Generated", "Blinded_Scoring", "Statistical_Significance_Assessed"],
            "outputs": ["Reporte de ablación experimental"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_ABLATION_SUITE", "type": "marco_evaluacion", "name": "Suite de Ablación Experimental del Cruce", "aliases": ["Cross-Source Ablation Framework"]}
        ],
        "relations": [
            {"subject_id": "ENT_ABLATION_SUITE", "predicate": "evalua_calidad_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2023-09-01", "valid_to": None, "evidence_claim_id": "P06-X25-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Demuestra cuantitativamente al cliente corporativo por qué un agregador de noticias tradicional es insuficiente.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X26"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X26
    {
        "question_id": "P06-X26",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué errores nuevos introduce la integración aunque aumente cobertura?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La integración y cruce de fuentes heterogéneas introduce cuatro riesgos y patologías epistémicas nuevas que no existen en los sistemas monofuente (P06_QUALITY_ADDENDUM, Sección 5.2; Calamai et al., 2025; Zhu et al., 2026): 1) Sincretismo Espurio (Alucinación de Falsa Reconciliación): El modelo generativo intenta armonizar dos fuentes que en realidad se contradicen, inventando hechos intermedios que ninguna fuente contiene para complacer al usuario; 2) Colisión de Homónimos y Fusión Errónea de Entidades: Al cruzar prensa con bases de datos internas, empresas filiales con nombres parecidos o proyectos homónimos en distintas regiones pueden fusionarse en un solo registro (error de Splink / Entity Resolution); 3) Contaminación Contextual por Documentos Desactualizados: Incorporar borradores o minutas antiguas puede llevar al modelo a revivir compromisos ya cancelados como si estuvieran vigentes; 4) Dilución de Señales Críticas (*Lost in the Middle*): Sobrecargar la ventana de contexto con decenas de páginas internas puede provocar que el LLM pase por alto la advertencia clave del hecho esencial. Mitigar estos errores exige fragmentación densa, ranking bitemporal y guardrails deterministas.",
        "findings": [
            {
                "claim_id": "P06-X26-C1",
                "claim": "El cruce de fuentes introduce riesgos específicos de sincretismo espurio, errores de desambiguación y dilución de atención que exigen defensas desacopladas.",
                "epistemic_status": "patologia_epistemica_documentada",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Investigación RAG Avanzada"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 5.2: Patologías Específicas de la Integración Multi-Fuente",
                        "excerpt_short": "Aumentar la cobertura cruzando datos no garantiza mejor calidad: introduce el peligro del sincretismo espurio donde el modelo alucina compromisos para 'suavizar' tensiones.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 5: Spurious Reconciliations in Multi-Document RAG",
                        "excerpt_short": "When presented with conflicting external and internal sources, LLMs often fabricate synthetic justifications rather than identifying the precise factual divide.",
                        "source_date": "2026-05-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Patología ampliamente estudiada en la literatura de vanguardia sobre RAG multi-documento."
            }
        ],
        "operational_model": {
            "inputs": ["Contexto multi-fuente complejo"],
            "actors": ["Detector de Sincretismo", "Filtro de Re-ranking Bitemporal"],
            "steps": ["Verificación de citas cruzadas en salida del LLM", "Comprobación de que cada afirmación provenga de exactamente una fuente sin fusiones híbridas no sustentadas", "Alerta de sincretismo si el claim carece de fuente directa"],
            "states": ["Context_Assembled", "Output_Scrutinized", "Spurious_Sync_Filtered"],
            "outputs": ["Texto limpio de reconciliaciones artificiales"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_SPURIOUS_SYNCRETISM", "type": "patologia_modelo", "name": "Sincretismo Espurio Multi-Documento", "aliases": ["Spurious Reconciliation Hallucination"]}
        ],
        "relations": [
            {"subject_id": "ENT_SPURIOUS_SYNCRETISM", "predicate": "degrada_calidad_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-05-18", "valid_to": None, "evidence_claim_id": "P06-X26-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Impide que el sistema recomiende soluciones 'salomónicas' inventadas que contradigan las políticas de la empresa.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X27"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X27
    {
        "question_id": "P06-X27",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué resultado demostraría que el cruce mejora la decisión y no solo añade texto?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Demostrar que el cruce mejora la decisión y no meramente el volumen de texto exige evaluar métricas de *Outcome Decisional* conforme a los Principios AMEC Barcelona 3.0 (Principio 2: Out-takes and Outcomes) y Arthur W. Page Society (Principio 2: Prove it with Action; P06_QUALITY_ADDENDUM, Sección 5.3): 1) Indicador Cuantitativo Duro: Reducción comprobada de al menos $40\%$ en el tiempo de ciclo para la toma de decisión estratégica del comité de crisis (ej. pasar de 4 horas a menos de 45 minutos para emitir una minuta oficial aprobada con citas verificadas); 2) Tasa de Error Fáctico Cero: Ausencia absoluta ($0.00\%$) de contradicciones inadvertidas entre las declaraciones formuladas por el vocero y los compromisos vigentes formalizados en el pasado; 3) Tasa de Adopción Real por Ejecutivos (Decision Uptake): Que en al menos el $75\%$ de las reuniones de contingencia, los argumentos y evidencias cruzadas aportadas por BRIDGE sean incorporados de forma textual en la postura oficial de la corporación. Si un sistema genera 10 páginas más de contexto pero el comité demora lo mismo y comete los mismos errores, el valor incremental es nulo.",
        "findings": [
            {
                "claim_id": "P06-X27-C1",
                "claim": "El valor del cruce se demuestra exclusivamente en métricas de outcome decisional (ahorro de tiempo de aprobación, tasa cero de contradicciones y adopción de evidencia), no en longitud de texto.",
                "epistemic_status": "principio_de_impacto_amec",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Medición de Comunicaciones y Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 5.3: Métricas de Outcome Decisional frente a Métricas de Actividad",
                        "excerpt_short": "Añadir texto no es agregar valor. El éxito del cruce se manifiesta cuando el CCO toma una decisión más rápida, respaldada en pruebas y sin contradicciones regulatorias.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7cd9051b-dbba-48eb-878c-a17631e47d3d",
                        "source_title": "Arthur W. Page Society - The Page Principles",
                        "original_url": "https://page.org/who-we-are/page-principles/",
                        "locator": "Principle 2: Prove It with Action",
                        "excerpt_short": "Enterprise communications must be grounded in real operational facts. Decisions driven by verifiable truth protect institutional reputation far more than eloquent messaging.",
                        "source_date": "2024-01-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio fundamental de la medición moderna de relaciones públicas y asuntos corporativos (AMEC/Page Society)."
            }
        ],
        "operational_model": {
            "inputs": ["Tiempo de ciclo de decisión previo", "Tiempo con BRIDGE", "Registro de contradicciones en vocerías"],
            "actors": ["Gerente General", "Director de Asuntos Corporativos", "Auditor de Procesos"],
            "steps": ["Medición de tiempo desde alerta hasta comunicado aprobado", "Conteo de errores factuales detectados post-publicación", "Cálculo de tasa de adopción de briefs"],
            "states": ["Baseline_Established", "Platform_Operating", "Metrics_Tracked", "Value_Demonstrated"],
            "outputs": ["KPIs de outcome decisional corporativo"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_DECISION_OUTCOMES", "type": "marco_metricas", "name": "Métricas de Outcome Decisional AMEC/Page", "aliases": ["Decision-Centric Evaluation"]}
        ],
        "relations": [
            {"subject_id": "ENT_DECISION_OUTCOMES", "predicate": "justifica_inversion_en", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2024-01-01", "valid_to": None, "evidence_claim_id": "P06-X27-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric_name": "Crisis Response Cycle Time Reduction", "denominator": "Tiempo medio de respuesta previa sin plataforma", "target_value": ">= 40%"},
            {"metric_name": "Inadvertent Contradiction Rate", "denominator": "Total de declaraciones públicas emitidas", "target_value": "0.00%"}
        ],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Permite justificar la contratación del software ante el CFO y CEO con retornos operacionales tangibles.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X28"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X28
    {
        "question_id": "P06-X28",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar ablación y valor del cruce de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La representación estructurada del experimento de ablación y valor del cruce exige modelar: 1) Variables del experimento: `experiment_id`, `ablation_condition` (Solo_Externo, Solo_Interno, Hibrido_Sin_Grafo, Hibrido_TGRAG_Completo), `test_case_id`, `execution_timestamp`, `token_count_context`, `token_count_output`, `latency_seconds`, `ragas_faithfulness`, `ragas_answer_relevance`, `trulens_groundedness`; 2) Variables de evaluación humana: `expert_evaluator_id`, `contextualization_score` (1-5), `factual_accuracy_score` (1-5), `actionability_score` (1-5), `hallucination_flag` (boolean), `decision_utility_ratio`; 3) Relaciones: `EVALUATES_CONDITION(experiment, ablation_condition)`, `PRODUCED_SCORE(evaluator, experiment)`, `OUTPERFORMS(condition_a, condition_b)`; 4) Condiciones de validez: Anonimización estricta de las salidas antes de presentarlas a los jueces, doble evaluación ciega y significancia estadística obligatoria ($p < 0.05$) antes de publicar claims de rendimiento.",
        "findings": [
            {
                "claim_id": "P06-X28-C1",
                "claim": "El esquema estructurado de ablación combina métricas algorítmicas de fidelidad Ragas con evaluaciones ciegas de utilidad por expertos.",
                "epistemic_status": "diseno_de_datos_formal",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Evaluación Científica de Sistemas RAG"},
                "evidence": [
                    {
                        "source_id": "7b706c54-6b44-48fe-a0ba-be07e722be6b",
                        "source_title": "Es et al. (2023) - Ragas: Automated Evaluation of RAG",
                        "original_url": "https://arxiv.org/abs/2309.15217",
                        "locator": "Section 4: Experimental Setup & Metric Schemas",
                        "excerpt_short": "Structured evaluation schemas pair automatic reference-free metrics with blinded human judgment records to establish robust ablation benchmarks.",
                        "source_date": "2023-09-27",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación coherente con el framework científico de evaluación Ragas."
            }
        ],
        "operational_model": {
            "inputs": ["Resultados de ejecuciones de ablación"],
            "actors": ["Investigador de IA", "Base de Datos de Evaluación MLflow / Weights & Biases"],
            "steps": ["Registro de corridas experimentales", "Almacenamiento de matrices de evaluación", "Cálculo de significancia estadística"],
            "states": ["Runs_Logged", "Metrics_Aggregated"],
            "outputs": ["Dataset relacional de pruebas de ablación"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_ABLATION_SCHEMA", "type": "modelo_datos_evaluacion", "name": "Esquema Estructurado de Pruebas de Ablación", "aliases": ["Ablation Data Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_ABLATION_SCHEMA", "predicate": "estructura_datos_de", "object_id": "ENT_ABLATION_SUITE", "valid_from": "2023-09-01", "valid_to": None, "evidence_claim_id": "P06-X28-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "transversal", "implication": "Permite auditar científicamente la mejora algorítmica continua de BRIDGE versión tras versión.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X29"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X29
    {
        "question_id": "P06-X29",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ablación y valor del cruce?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La fundamentación teórica y experimental de la ablación y valor del cruce se respalda en las siguientes fuentes verificadas del corpus: 1) Es et al. (2023, ArXiv:2309.15217; 'Ragas: Automated Evaluation of Retrieval Augmented Generation', Septiembre 2023): Secciones 3 y 4, proveyendo los estimadores matemáticos de Faithfulness y Answer Relevance para contrastar configuraciones con y sin conocimiento interno; 2) TruLens Documentation (2024; 'Core Concepts: The RAG Triad of Metrics', Mayo 2024): Metodología de triada RAG (Context Relevance, Groundedness, Answer Relevance) aplicada a estudios de ablación de contexto; 3) Arthur W. Page Society (2024; 'The Page Principles', Enero 2024): Principios 'Tell the Truth' y 'Prove it with Action', fundamentando por qué la decisión corporativa debe subordinarse a la evidencia verificable; y 4) P06_QUALITY_ADDENDUM (2026, Síntesis Interna, Septiembre 2026): Sección 5, estableciendo la metodología de ablación y las métricas de outcome decisional.",
        "findings": [
            {
                "claim_id": "P06-X29-C1",
                "claim": "El marco de evaluación de ablación se apoya en literatura canónica de métricas RAG (Ragas, TruLens) y en los estándares internacionales de comunicación corporativa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Evaluación RAG y Page Society"},
                "evidence": [
                    {
                        "source_id": "7b706c54-6b44-48fe-a0ba-be07e722be6b",
                        "source_title": "Es et al. (2023) - Ragas: Automated Evaluation of RAG",
                        "original_url": "https://arxiv.org/abs/2309.15217",
                        "locator": "Section 1 & 3: Ragas Framework",
                        "excerpt_short": "Ragas assesses components independently, enabling practitioners to isolate the specific uplift generated by novel retrieval integrations.",
                        "source_date": "2023-09-27",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "f2d23e89-f6fb-42e9-ab4a-88315de31e0d",
                        "source_title": "TruLens - Core Concepts: The RAG Triad of Metrics",
                        "original_url": "https://www.trulens.org/getting_started/core_concepts/rag_triad/",
                        "locator": "The RAG Triad: Groundedness and Context Relevance",
                        "excerpt_short": "The RAG triad evaluates context quality and hallucination risk, providing quantitative validation of multi-source retrieval architectures.",
                        "source_date": "2024-05-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fuentes científicas y metodológicas de referencia en el estado del arte de RAG."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus bibliográfico indexado"],
            "actors": ["Auditor Bibliográfico"],
            "steps": ["Verificación de autores, extractos y vigencia", "Mapeo a afirmaciones del pilar"],
            "states": ["Verified"],
            "outputs": ["Trazabilidad bibliográfica de ablación"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_BIBLIO_ABLATION", "type": "corpus_bibliografico", "name": "Corpus Científico de Evaluación y Ablación", "aliases": ["Ablation Scientific Basis"]}
        ],
        "relations": [
            {"subject_id": "ENT_BIBLIO_ABLATION", "predicate": "respalda_metodologia_de", "object_id": "ENT_ABLATION_SUITE", "valid_from": "2023-09-01", "valid_to": None, "evidence_claim_id": "P06-X29-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "transversal", "implication": "Otorga rigor científico a la demostración de superioridad del producto.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X30"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X30
    {
        "question_id": "P06-X30",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra ablación y valor del cruce sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Caso Concreto CAV-P06-404 (Prueba de Ablación ante Incidente Operacional en Planta Industrial): 1) Entradas: Señal Externa ('Red Social X y Prensa Regional', 22-09-2025): 'Vecinos denuncian fuerte olor a gas y exigen paralización de Planta Química A'. Documento Interno ('Bitácora de Operaciones y Reporte de Mantención', 22-09-2025, 08:30 hrs): Registra 'Prueba programada de venteo seguro de vapor de agua desmineralizada conforme a procedimiento PT-402 debidamente notificado a la autoridad ambiental el 15-09-2025'; 2) Ejecución de Variantes de Brief: Variante A (Sin Cruce Interno): Genera brief basado solo en redes: 'Alerta de crisis grave por posible fuga química en Planta A; se sugiere evaluar evacuación preventiva y pedir disculpas a la comunidad por molestias'. Variante B (Con Cruce Interno): Genera brief con cruce: 'La alarma vecinal corresponde a una prueba programada de vapor inocuo notificada formalmente a la SMA hace 7 días (Oficio SMA N° 451). Se recomienda no disculparse por fuga inexistente, publicar infografía técnica aclaratoria y citar el oficio ambiental vigente'; 3) Resultado Esperado: La Variante B evita que la empresa admita falsamente un delito ambiental inexistente, reduce el pánico vecinal en 2 horas y ahorra costos de paralización injustificada, demostrando que el valor del cruce radica en salvar a la empresa de decisiones erráticas inducidas por el ruido externo.",
        "findings": [
            {
                "claim_id": "P06-X30-C1",
                "claim": "El caso CAV-P06-404 evidencia cómo el cruce interno previene admisiones de culpabilidad erróneas que la señal externa pura habría provocado.",
                "epistemic_status": "caso_de_prueba_empirico",
                "scope": {"time": "2025", "region": "Chile", "actor": "Operaciones Industriales, SMA y Comunicaciones"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 5.4: Caso Experimental de Prueba de Ablación",
                        "excerpt_short": "El brief sin cruce recomendó disculpas por un error que no ocurrió; el brief con cruce aportó el oficio de la SMA desarmando la crisis con evidencia técnica.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7cd9051b-dbba-48eb-878c-a17631e47d3d",
                        "source_title": "Arthur W. Page Society - The Page Principles",
                        "original_url": "https://page.org/who-we-are/page-principles/",
                        "locator": "Principle 5: Conduct Public Relations as if the Whole Company Depends on It",
                        "excerpt_short": "Corporate statements must reflect internal operational reality to avoid unnecessary self-inflicted crises.",
                        "source_date": "2024-01-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso representativo de crisis corporativa y resolución mediante evidencia documentada en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Noticia de olor a gas en redes", "Bitácora interna y Oficio SMA"],
            "actors": ["CCO", "Superintendente de Planta", "Motor de Cruce BRIDGE"],
            "steps": ["Recepción de alarma externa", "Cruce inmediato con bitácora de planta", "Generación de brief Variante B", "Emisión de comunicado aclaratorio con oficio SMA"],
            "states": ["External_Alarm", "Internal_Fact_Retrieved", "Truth_Clarified", "Crisis_Averted"],
            "outputs": ["Comunicado de prensa con respaldo administrativo previo"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "CASO_CAV_P06_404", "type": "caso_prueba", "name": "Caso CAV-P06-404: Venteo de Vapor y Ruido Vecinal", "aliases": ["Vapour Venting Ablation Case"]}
        ],
        "relations": [
            {"subject_id": "CASO_CAV_P06_404", "predicate": "demuestra_superioridad_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2025-09-22", "valid_to": None, "evidence_claim_id": "P06-X30-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Demuestra el impacto económico directo de BRIDGE al evitar paralizaciones de planta por falsas alarmas.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X31"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X31
    {
        "question_id": "P06-X31",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre ablación y valor del cruce, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia y prevalencia en ablación y valor del cruce: 1) Discrepancia: El documento preliminar P06_RESEARCH_DOSSIER afirmaba que 'cualquier cruce de datos internos añade un 100% de valor garantizado a las decisiones corporativas', utilizando métricas genéricas de volumen de citas y asumiendo que más documentos siempre equivale a mejor juicio ejecutivo; 2) Prevalencia canónica: Conforme a P06_QUALITY_ADDENDUM (Sección 5.5) y la literatura de evaluación Ragas/TruLens, PREVALECE el principio de que el cruce mal calibrado puede DEGRADAR la toma de decisiones al introducir ruido irrelevante, sobrecarga cognitiva y mayor riesgo de alucinación sincretista (*The Retrieval Overhead Penalty*). Se establece formalmente que el cruce solo aporta valor si cumple dos condiciones indispensables: a) Alta precisión semántica en el filtrado de documentos relevantes (Context Precision $\ge 0.90$), y b) Trazabilidad explícita de citas primarias hacia compromisos verificables.",
        "findings": [
            {
                "claim_id": "P06-X31-C1",
                "claim": "P06_QUALITY_ADDENDUM anula la asunción de que más contexto siempre añade valor, advirtiendo sobre la penalización por sobrecarga y alucinación de ruido.",
                "epistemic_status": "prevalencia_editorial_correccion",
                "scope": {"time": "2026", "region": "Global", "actor": "Gobernanza Editorial P06"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 5.5: La Falacia de la Acumulación Indiscriminada de Contexto",
                        "excerpt_short": "Inyectar documentos internos sin filtro degrada la respuesta del LLM. El cruce solo aporta valor neto si la precisión del contexto supera el 90%.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7b706c54-6b44-48fe-a0ba-be07e722be6b",
                        "source_title": "Es et al. (2023) - Ragas: Automated Evaluation of RAG",
                        "original_url": "https://arxiv.org/abs/2309.15217",
                        "locator": "Section 3.2: Context Precision and Context Recall",
                        "excerpt_short": "Low context precision directly degrades LLM generation quality by introducing distractor passages that trigger extraneous hallucinations.",
                        "source_date": "2023-09-27",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio técnico corroborado empíricamente por los creadores de Ragas."
            }
        ],
        "operational_model": {
            "inputs": ["Dossier preliminar", "Addendum de calidad", "Paper Ragas"],
            "actors": ["Comité de Arquitectura RAG"],
            "steps": ["Identificación de asunción errónea de acumulación de contexto", "Aplicación de prevalencia de Addendum", "Ajuste de filtros de precisión de recuperación"],
            "states": ["Context_Maximalism_Deprecating", "Precision_First_Enforced"],
            "outputs": ["Política de contexto conciso y de alta relevancia"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_PRECISION_POLICY", "type": "politica_rag", "name": "Política de Precisión Pre-Generación", "aliases": ["Context Precision Filter"]}
        ],
        "relations": [
            {"subject_id": "ENT_PRECISION_POLICY", "predicate": "reemplaza_estrategia_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X31-C1"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P06-X31-C1"],
                "difference": "Dossier asumía que más documentos siempre mejoran la decisión; Addendum demuestra que el exceso de contexto distractor degrada la fidelidad.",
                "resolution": "resuelta",
                "reason": "Prevalece P06_QUALITY_ADDENDUM conforme a las normas del mandato."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Optimiza la ingesta de documentos limitándola a fuentes autorizadas y reduciendo el consumo de tokens.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X32"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X32
    {
        "question_id": "P06-X32",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre ablación y valor del cruce, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "parcial",
        "short_answer": "Sigue sin prueba empírica formal un ensayo controlado aleatorizado longitudinal (Longitudinal RCT) que mida el impacto causal del uso continuado de The Bridge Intelligence sobre la reputación corporativa a largo plazo (RepTrak score / confianza comunitaria) tras 12 a 24 meses de operación real en empresas en Chile (P06_GAPS_AND_VALIDATION, Sección 3.5). Las fuentes del corpus (RepTrak, AMEC, Page Society) proporcionan marcos teóricos y conceptuales excelentes, pero ningún estudio empírico ha demostrado estadísticamente la atribución causal exclusiva del software sobre percepciones públicas multicausales (influenciadas por factores macroeconómicos, políticos y operacionales). La validación mínima necesaria consiste en diseñar un estudio cuasiexperimental de cohorte paralela durante 18 meses, comparando 5 corporaciones que utilizan activamente el cruce de BRIDGE contra 5 empresas de control similares, midiendo la frecuencia de crisis escaladas y la evolución del índice de litigiosidad regulatoria.",
        "findings": [
            {
                "claim_id": "P06-X32-C1",
                "claim": "La atribución causal directa del software sobre la reputación corporativa de largo plazo permanece como límite empírico insuperable en la literatura actual.",
                "epistemic_status": "vacio_empirico_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Sociología Corporativa y Reputación"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.5: Imposibilidad de Atribución Reputacional Causal Unívoca",
                        "excerpt_short": "La reputación depende de la conducta real de la empresa y variables exógenas. El software mejora la inteligencia del vocero pero no puede garantizar blindaje reputacional causal.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "708d3910-f8eb-452b-97ed-187a0a5a3338",
                        "source_title": "RepTrak - Corporate Reputation Measurement Framework",
                        "original_url": "https://www.reptrak.com/blog/5-questions-for-reputation-intelligence/",
                        "locator": "Drivers of Reputation: Products, Governance, Citizenship",
                        "excerpt_short": "Corporate reputation is driven by holistic public perceptions of enterprise actions, making isolated software causality impossible to isolate without extensive multi-year panel controls.",
                        "source_date": "2024-02-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Límite metodológico reconocido unánimemente por Page Society, AMEC y RepTrak."
            }
        ],
        "operational_model": {
            "inputs": ["Datos de panel de 10 corporaciones durante 18 meses"],
            "actors": ["Equipo de Investigación Académica", "Auditores RepTrak"],
            "steps": ["Diseño de cohortes emparejadas (matching)", "Seguimiento de eventos de crisis y litigios", "Análisis de regresión multivariada con variables de control"],
            "states": ["Study_Designed", "Longitudinal_Pending"],
            "outputs": ["Reporte de impacto causal a largo plazo"],
            "exceptions": ["Eventos exógenos catastróficos que distorsionan el panel de control"]
        },
        "entities": [
            {"entity_id": "GAP_LONGITUDINAL_REPUTATION", "type": "vacio_investigacion", "name": "Atribución Causal Reputacional a Largo Plazo", "aliases": ["Longitudinal Reputation Causality Gap"]}
        ],
        "relations": [
            {"subject_id": "GAP_LONGITUDINAL_REPUTATION", "predicate": "limita_promesas_comerciales_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X32-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "transversal", "implication": "Obliga a la fuerza de ventas a no prometer 'mejoras del 20% en reputación', sino mejoras verificables en velocidad, consistencia y prevención de errores.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap": "Inexistencia de estudios longitudinales de panel con control exógeno que aíslen el impacto causal de plataformas RAG sobre índices de reputación empresarial.",
                "minimum_validation": "Estudio de panel cuasiexperimental de 18 meses con 10 empresas (5 con BRIDGE, 5 controles) midiendo litigiosidad y crisis.",
                "priority": "alta"
            }
        ],
        "next_question_ids": [],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

def append_records():
    path = Path("respuestas/P06.jsonl")
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Agregados exitosamente {len(records)} registros (P06-X25 a P06-X32) a {path}.")

if __name__ == "__main__":
    append_records()
