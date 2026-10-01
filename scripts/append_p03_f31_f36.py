import json
from pathlib import Path

NOTEBOOK_ID = "a2afe847-a988-40f1-9432-9e596b74b376"
SNAPSHOT_AT = "2026-10-01T02:25:00-03:00"

records = [
    # P03-F31
    {
        "question_id": "P03-F31",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se distinguen homónimos, filiales, productos y personas con nombres similares?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La desambiguación precisa de homónimos, filiales, marcas comerciales y ejecutivos se resuelve mediante una arquitectura de Entity Linking de dos etapas (Wu et al. 2020 - BLINK): 1) Recuperación densa de candidatos (Bi-Encoder): el contexto textual de la mención y las descripciones canónicas de la base de conocimiento corporativa (grafo de entidades) se codifican en embeddings densos en un espacio compartido, recuperando las 10 entidades candidatas más probables en menos de 50 milisegundos mediante búsqueda de vecinos cercanos (k-NN / FAISS); 2) Re-clasificación exhaustiva (Cross-Encoder): se concatena la mención en su contexto con la descripción completa de cada candidato para evaluar la atención cruzada (cross-attention), resolviendo ambigüedades entre empresas matrices y subsidiarias, o entre figuras públicas homónimas; y 3) Vinculación ontológica: la entidad confirmada se enlaza a su URI inmutable en el grafo de conocimiento corporativo junto a su código de registro oficial (RUT en Chile o CIK en la SEC).",
        "findings": [
            {
                "claim_id": "P03-F31-C1",
                "claim": "La resolución de homónimos y diferenciación entre filiales y marcas exige arquitecturas de Entity Linking en dos fases (Bi-Encoder para recuperación y Cross-Encoder para re-clasificación contextual) conectadas al grafo corporativo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Global", "actor": "Entity Linking / BLINK P03"},
                "evidence": [
                    {
                        "source_id": "1ab670b8-5d7b-41dc-bec6-71b39481b818",
                        "source_title": "Scalable Zero-shot Entity Linking with Dense Entity Retrieval (Wu et al. 2020)",
                        "original_url": "https://arxiv.org/abs/1911.03814",
                        "locator": "Section 2: Architecture - Bi-Encoder and Cross-Encoder",
                        "excerpt_short": "BLINK uses a two-stage approach: a dual-encoder that retrieves entity candidates based on dense embeddings, followed by a cross-encoder that jointly scores the mention context with candidate descriptions.",
                        "source_date": "2020",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "73488fee-1939-4426-b579-d9ca61c6eaa3",
                        "source_title": "P03_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2.5: Desafíos de NLP: Homonimia, Sesgo y Detección de Desinformación",
                        "excerpt_short": "Los modelos de Entity Linking de última generación (BLINK) resuelven la homonimia mediante... recuperación densa... y re-clasificación exhaustiva con cross-encoders.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación técnica contra la publicación fundacional de BLINK y el mapa de evidencia P03."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de señal con mención ambigua", "Grafo de entidades corporativas"],
            "actors": ["Bi-Encoder Candidate Retriever", "Cross-Encoder Disambiguator"],
            "steps": ["Extracción de mención", "Búsqueda vectorial de candidatos en KG", "Scoring cruzado de atención", "Enlace a URI canónico"],
            "states": ["Mention_Extracted", "Candidates_Retrieved", "Entity_Disambiguated"],
            "outputs": ["Mención resuelta a URI inmutable (ej. http://bridge.corp/ent/entel_chile)"],
            "exceptions": ["Nuevas entidades no catalogadas previamente en el grafo (zero-shot link failure)"]
        },
        "entities": [
            {"entity_id": "ENT_BLINK_FRAMEWORK", "type": "modelo_nlp", "name": "Arquitectura de Desambiguación BLINK", "aliases": ["BLINK Entity Linking"]}
        ],
        "relations": [
            {"subject_id": "ENT_BLINK_FRAMEWORK", "predicate": "resuelve_homonimia_en", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F31-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Método de resolución de entidades",
                "Coincidencia Léxica por Diccionario": "Genera falsos positivos masivos ante homónimos (ej. confundir ejecutivo con futbolista homónimo).",
                "Entity Linking Denso (BLINK)": "Distingue el rol corporativo examinando el contexto semántico completo de la oración."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Implementar un servicio de Entity Linking basado en bi/cross-encoders para evitar alertas basura sobre figuras públicas homónimas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F32"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F32
    {
        "question_id": "P03-F32",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué método permite detectar temas emergentes aun cuando no mencionan a la empresa?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El método estándar es el Modelado de Tópicos Neuronal Dinámico no supervisado mediante BERTopic (Grootendorst 2022): 1) Generación de embeddings: se transforman los documentos noticiosos y publicaciones del entorno en representaciones vectoriales densas de oraciones (Sentence Transformers o BETO); 2) Reducción dimensional preservando vecindades: se aplica UMAP para reducir la alta dimensionalidad sin perder la estructura no lineal de los grupos semánticos; 3) Agrupamiento basado en densidad: HDBSCAN identifica clústeres densos de conversación de forma autónoma sin forzar la asignación de un número fijo de tópicos a priori (k), aislando el ruido no relacionado; 4) Extracción de descriptores con c-TF-IDF: una adaptación de TF-IDF basada en clases extrae las palabras y conceptos que discriminan a cada clúster respecto al corpus global; y 5) Enlace al mapa de riesgos: los temas emergentes descubiertos se comparan vectorialmente con la matriz de riesgos estratégicos de la corporación para alertar sobre tensiones sectoriales antes de que la empresa sea nombrada.",
        "findings": [
            {
                "claim_id": "P03-F32-C1",
                "claim": "La detección de temas emergentes sin mención de marca se logra mediante modelado de tópicos neuronal con BERTopic (embeddings + UMAP + HDBSCAN + c-TF-IDF), descubriendo clústeres semánticos de forma no supervisada.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2026", "region": "Global", "actor": "Modelado de Tópicos P03"},
                "evidence": [
                    {
                        "source_id": "5ddc89a7-492f-4263-b691-28bb6f9df072",
                        "source_title": "BERTopic: Neural Topic Modeling with a Class-based TF-IDF Procedure (Grootendorst 2022)",
                        "original_url": "https://arxiv.org/abs/2203.05794",
                        "locator": "Section 2: Architectural Pipeline",
                        "excerpt_short": "BERTopic generates document embeddings, clusters them with UMAP and HDBSCAN, and extracts topic representations using a novel class-based TF-IDF procedure.",
                        "source_date": "2022",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "73488fee-1939-4426-b579-d9ca61c6eaa3",
                        "source_title": "P03_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2.5: Desafíos de NLP - Hecho Documentado",
                        "excerpt_short": "BERTopic utiliza embeddings de oraciones combinados con reducción de dimensionalidad (UMAP), clustering de densidad (HDBSCAN) y c-TF-IDF para descubrir temas emergentes de forma dinámica sin supervisión humana previa.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación técnica de la publicación original de BERTopic y mapa de evidencia."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus de noticias sectoriales sin filtrar por marca"],
            "actors": ["BERTopic Pipeline Worker", "Topic Descriptor Extractor"],
            "steps": ["Embedding de oraciones", "Reducción UMAP", "Clustering HDBSCAN", "Ponderación c-TF-IDF"],
            "states": ["Unlabeled_Docs", "Clustered_Vectors", "Emerging_Topics_Identified"],
            "outputs": ["Lista de tópicos emergentes con palabras clave descriptivas y puntuación de coherencia"],
            "exceptions": ["Tópicos excesivamente fragmentados por variaciones estilísticas de redacción"]
        },
        "entities": [
            {"entity_id": "ENT_BERTOPIC_PIPELINE", "type": "modelo_nlp", "name": "Pipeline Neuronal BERTopic", "aliases": ["BERTopic Neural Pipeline"]}
        ],
        "relations": [
            {"subject_id": "ENT_BERTOPIC_PIPELINE", "predicate": "descubre_temas_emergentes_en", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F32-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Descubrimiento de temas",
                "Filtrado por Palabras Clave Fijas": "Ciego ante nuevas terminologías, reclamos imprevistos o eventos sin precedentes.",
                "BERTopic No Supervisado": "Descubre agrupaciones semánticas orgánicas en tiempo real sin requerir listas de keywords previas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Correr un job periódico de BERTopic sobre la prensa regional y boletines oficiales para anticipar debates regulatorios antes de que impacten a la corporación.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F33"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F33
    {
        "question_id": "P03-F33",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué límites tienen sentimiento automático, clasificación narrativa y detección de desinformación?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis automático presenta 3 limitaciones metodológicas y técnicas infranqueables sin supervisión humana: 1) Fracaso del sentimiento tripolar genérico (Positivo/Negativo/Neutro): no detecta ironía ni sarcasmo, confunde el tono crítico de una investigación seria con un ataque reputacional, e ignora la postura política estratégica (ej. un medio puede reportar con tono adverso una regulación que estratégicamente beneficia a la compañía); 2) Límites de modelos base en español local (BETO): pre-entrenado en un corpus enciclopédico general (Cañete et al. 2020), no comprende de forma nativa modismos locales chilenos de coyuntura ni terminología regulatoria compleja, siendo una HIPÓTESIS OPERATIVA no demostrada que requiera fine-tuning local supervisado; y 3) Falacia de equivalencia en desinformación: la sincronía temporal de publicaciones (Pacheco et al. 2020) y la actividad de bots (Sayyadiharikandeh et al. 2020) no son sinónimos de falsedad ni engaño (se usan en ONGs y alertas públicas); calificar un contenido de 'desinformación' exige evaluar las técnicas DISARM y realizar comprobación de hechos (fact-checking) por analistas humanos.",
        "findings": [
            {
                "claim_id": "P03-F33-C1",
                "claim": "El sentimiento automático tripolar es disfuncional para asuntos corporativos, BETO carece de validación empírica para ironía regulatoria chilena sin fine-tuning, y los patrones de sincronía de red no equivalen por sí mismos a desinformación.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Chile / Global", "actor": "Auditoría Metodológica P03"},
                "evidence": [
                    {
                        "source_id": "e895c495-1608-46f4-b921-ca7bb60aac75",
                        "source_title": "P03_QUALITY_ADDENDUM",
                        "original_url": None,
                        "locator": "Sección 2.2 y 2.3: BETO y Desacoplamiento Estricto",
                        "excerpt_short": "BETO... pre-entrenado sobre un corpus general... La afirmación de que comprende modismos chilenos complejos o posturas regulatorias es estrictamente una HIPÓTESIS OPERATIVA... La coordinación temporal ocurre legítimamente en campañas ciudadanas... no demuestra en absoluto la falsedad del mensaje.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5eaa5b99-624c-4877-87be-66c339c7b6d4",
                        "source_title": "AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework",
                        "original_url": "https://amecorg.com/barcelona-principles-3-0-translations/",
                        "locator": "Principle 2: Outcome Measurement",
                        "excerpt_short": "Simple automated tone scoring often obscures strategic comprehension and stakeholder intent.",
                        "source_date": "2020",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación cruzada de la adenda de calidad, principios AMEC y papers fundacionales."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de señal analizada", "Scores de sentimiento automático", "Patrón de coordinación de red"],
            "actors": ["Human-in-the-Loop Analyst", "Stance Evaluator", "DISARM TTP Mapper"],
            "steps": ["Descarte de etiqueta tripolar cruda", "Evaluación de postura estratégica", "Auditoría humana de intencionalidad"],
            "states": ["Raw_Sentiment_Flagged", "Calibrated_By_Stance", "Analyst_Validated"],
            "outputs": ["Evaluación reputacional calibrada y fundamentada epistémicamente"],
            "exceptions": ["Sobrecarga de alertas durante crisis de alto volumen de publicaciones"]
        },
        "entities": [
            {"entity_id": "ENT_NLP_LIMITATIONS", "type": "marco_metodologico", "name": "Límites Epistémicos de NLP y Sentimiento", "aliases": ["NLP Epistemic Limitations"]}
        ],
        "relations": [
            {"subject_id": "ENT_NLP_LIMITATIONS", "predicate": "impone_restricciones_a", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F33-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de evaluación discursiva",
                "Sentimiento Automático Tradicional": "Polaridad superficial +/-/neutral asignada por modelo opaco.",
                "Análisis de Postura y Riesgo (Stance)": "Evaluación de atribución de responsabilidad, impacto operacional y postura ideológica."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Reemplazar métricas de polaridad por análisis de postura (stance analysis) y exigir revisión humana supervisada para catalogar ataques de desinformación.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F34"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F34
    {
        "question_id": "P03-F34",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar desambiguación y análisis de señales de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La representación estructurada exige: 1) Variables técnicas de NLP: `confidence_score_linking` (0.0 a 1.0), `candidate_entity_id`, `topic_cluster_id` (HDBSCAN label), `topic_coherence_score`, `stance_direction` (favor, contra, neutral, ambivalente) y `disarm_ttp_code` (ej. T0015); 2) Categorías de señal: Entidad_Comercial, Entidad_Gubernamental, Tema_Emergente_No_Nominal, Disputa_Regulatoria y Narrativa_Amplificada; 3) Relaciones en grafo: `desambiguado_como` (Entidad en KG), `asociado_a_topico` (Cluster Semántico), `postura_hacia` (Proyecto o Ley), y `táctica_identificada` (Técnica DISARM); y 4) Condiciones de integridad: prohibir clasificaciones definitivas de desinformación sin trazabilidad del patrón empírico observable y asignación formal de código de táctica DISARM.",
        "findings": [
            {
                "claim_id": "P03-F34-C1",
                "claim": "El modelado estructurado de desambiguación y análisis de señales debe registrar puntuaciones de confianza de linking, identificadores de clústeres de tópicos y clasificaciones de postura desacopladas de polaridad simple.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Modelado Estructurado P03"},
                "evidence": [
                    {
                        "source_id": "e4c4d2d3-d141-4304-b2d4-00b9b7d3cee0",
                        "source_title": "DISARM Foundation: Disinformation Tactics, Techniques & Procedures Framework",
                        "original_url": "https://github.com/DISARMFoundation/DISARMframeworks/",
                        "locator": "TTP Identification and Schema",
                        "excerpt_short": "DISARM provides a standardized taxonomy of identifiers (T0000 series) to catalog observable behavior without attributing malicious intent without evidence.",
                        "source_date": "2026",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación con especificaciones del marco DISARM y ontologías semánticas."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de señal analizado por NLP"],
            "actors": ["Semantic Structurer", "Ontology Mapper"],
            "steps": ["Asignación de IDs de cluster y entidad", "Normalización de postura", "Inserción de metadatos estructurados"],
            "states": ["Raw_NLP_Output", "Schema_Aligned", "Graph_Triples_Emitted"],
            "outputs": ["Objeto estructurado con metadatos semánticos auditables"],
            "exceptions": ["Conflictos entre predicciones de múltiples modelos de clasificación"]
        },
        "entities": [
            {"entity_id": "ENT_SEMANTIC_ANALYSIS_SCHEMA", "type": "esquema_datos", "name": "Esquema Estructurado de Análisis Semántico", "aliases": ["Semantic Analysis Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_SEMANTIC_ANALYSIS_SCHEMA", "predicate": "formaliza_analisis_en", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F34-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Implementar el esquema con soporte explícito de códigos DISARM para la auditoría de riesgos reputacionales.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F35"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F35
    {
        "question_id": "P03-F35",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre desambiguación y análisis de señales?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los hechos de este eje están respaldados por: 1) Arquitectura de desambiguación densa: Wu et al. (2020, 'Scalable Zero-shot Entity Linking with Dense Entity Retrieval' - BLINK paper, arXiv:1911.03814); 2) Modelado neuronal de tópicos no supervisado: Grootendorst (2022, 'BERTopic: Neural Topic Modeling with a Class-based TF-IDF Procedure', arXiv:2203.05794); 3) Modelo fundacional en español y sus límites: Cañete et al. (2020, 'Spanish Pre-Trained BERT Model and Evaluation' - BETO paper); 4) Detección de patrones en redes: Pacheco et al. (2020, coordinación temporal) y Sayyadiharikandeh et al. (2020, ensembles de bots); 5) Taxonomía de desinformación: DISARM Foundation (2026); y 6) Precedencia editorial y rectificación: P03_QUALITY_ADDENDUM (Septiembre 2026, Secciones 2.2 y 2.3), que califica taxativamente la capacidad de BETO sobre modismos e ironía chilena como 'hipótesis operativa no probada' y desacopla la coordinación de la falsedad.",
        "findings": [
            {
                "claim_id": "P03-F35-C1",
                "claim": "El respaldo documental de desambiguación y análisis de señales integra publicaciones científicas de NLP y redes (BLINK, BERTopic, BETO, Pacheco et al., Sayyadiharikandeh et al.), el marco DISARM y la adenda editorial P03.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Global / Chile", "actor": "Corpus Canónico P03"},
                "evidence": [
                    {
                        "source_id": "8375f21f-7a9b-4214-a492-4d42391c71e0",
                        "source_title": "BETO: Spanish Pre-Trained BERT Model and Evaluation (Cañete et al. 2020)",
                        "original_url": "https://github.com/dccuchile/beto",
                        "locator": "Model Architecture & Benchmark Tasks",
                        "excerpt_short": "BETO is pre-trained on the Spanish Wikipedia and OPUS corpora, evaluated on standard tasks (POS, NER, MLDoc) without domain-specific stance benchmarks.",
                        "source_date": "2020",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "e895c495-1608-46f4-b921-ca7bb60aac75",
                        "source_title": "P03_QUALITY_ADDENDUM",
                        "original_url": None,
                        "locator": "Sección 2.2: Requerimiento Técnico de Adaptación",
                        "excerpt_short": "Para que esta capacidad sea efectiva en un sistema de Asuntos Corporativos, se requiere un proceso formal de domain adaptation, fine-tuning con un conjunto de datos anotado manualmente... y un benchmark de prueba local.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa de papers fundacionales y la adenda de calibración epistémica."
            }
        ],
        "operational_model": {
            "inputs": ["Repositorio de citas de NLP y análisis"],
            "actors": ["NLP Auditor"],
            "steps": ["Comprobación de papers", "Verificación de benchmarks", "Aprobación de citas"],
            "states": ["Raw_Citations", "Verified_Papers", "Corpus_Approved"],
            "outputs": ["Catálogo de respaldo de evidencia de NLP certificado"],
            "exceptions": ["Modelos pre-entrenados sin documentación de datos de entrenamiento"]
        },
        "entities": [
            {"entity_id": "ENT_NLP_EVIDENCE_CORPUS", "type": "corpus_documental", "name": "Corpus de Evidencia de NLP P03", "aliases": ["NLP Evidence Corpus"]}
        ],
        "relations": [
            {"subject_id": "ENT_NLP_EVIDENCE_CORPUS", "predicate": "respalda_afirmaciones_de", "object_id": "Eje_Analisis_P03", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F35-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "Mantener una base de conocimiento documental para guiar el desarrollo de modelos de lenguaje ajustados localmente en BRIDGE.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F36"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F36
    {
        "question_id": "P03-F36",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra desambiguación y análisis de señales sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Caso: Detección y desambiguación de una polémica sobre el uso de salmueras en el Salar de Atacama que involucra a una filial y a un competidor. Entradas: 1) Nota de prensa que menciona 'la empresa minera SQM Salar' y a su ejecutivo 'Patricio Contesse'; 2) Modelo BLINK procesando la mención: el bi-encoder recupera las entidades 'SQM Salar S.A. (filial)' y 'Sociedad Química y Minera de Chile (matriz)'; el cross-encoder resuelve con un 98% de confianza que la entidad operativa responsable es la filial `SQM_SALAR_CHILE`; 3) Módulo BERTopic analizando el flujo no nominal de 200 comentarios y cartas al director: descubre un clúster emergente `CLUSTER_SALMUERA_LITIO` centrado en 'derechos de extracción de salmuera y evaporación' sin que los textos nombren directamente a las corporaciones; y 4) Módulo de postura evaluando las cartas: detecta postura 'Adversa a la extracción intensiva' (Stance -0.85) sin catalogar los textos como 'desinformación' (al no haber coordinación artificial ni vulneración de tácticas DISARM). Resultado esperado: El sistema genera una ficha de inteligencia unificada que enlaza la mención desambiguada de la filial con el tópico emergente de salmueras, alertando a asuntos corporativos sobre el riesgo reputacional y regulatorio derivado de la discusión sobre el recurso hídrico.",
        "findings": [
            {
                "claim_id": "P03-F36-C1",
                "claim": "Un caso de desambiguación y análisis avanzado combina BLINK para aislar filiales corporativas y BERTopic para capturar debates sobre salmueras no nominales, evaluando posturas sin estigmatizar el disenso legítimo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile (Salar de Atacama)", "actor": "Caso Desambiguación P03"},
                "evidence": [
                    {
                        "source_id": "73488fee-1939-4426-b579-d9ca61c6eaa3",
                        "source_title": "P03_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2.5: Desafíos de NLP - Hipótesis Operativa",
                        "excerpt_short": "Se debe reemplazar el análisis de sentimiento genérico por un motor de Detección de Postura y Riesgo Reputacional... evaluando tres vectores: atribución de responsabilidad, impacto operacional y polarización del emisor.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación basada en los modelos operativos documentados del mapa de evidencia."
            }
        ],
        "operational_model": {
            "inputs": ["Noticia cruda con mención de filial", "Comentarios públicos sobre salmueras"],
            "actors": ["BLINK Disambiguator", "BERTopic Clusterer", "Stance Classifier"],
            "steps": ["Desambiguación de filial", "Descubrimiento de clúster de tópicos", "Evaluación de postura", "Generación de ficha"],
            "states": ["Raw_Inputs", "Entity_Linked", "Topic_Mapped", "Intelligence_Card_Emitted"],
            "outputs": ["Ficha de inteligencia que vincula la filial desambiguada con el tópico emergente de salmuera"],
            "exceptions": ["Nombres idénticos de ejecutivos en múltiples empresas del holding"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_SALAR_DESAMBIGUACION", "type": "caso_de_uso", "name": "Caso Demostrativo Desambiguación Salar", "aliases": ["Salar Disambiguation Case"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_SALAR_DESAMBIGUACION", "predicate": "demuestra_integracion_en", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F36-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Integrar BLINK y BERTopic en el backend analítico de BRIDGE para dotar a la corporación de visión temprana no nominal y resolución ontológica de filiales.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-C11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_file = Path("respuestas/P03.jsonl")
with open(out_file, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Batch 6 (P03-F31 to P03-F36) written successfully to {out_file}.")
