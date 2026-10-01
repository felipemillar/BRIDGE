import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-F37
    {
        "question_id": "P06-F37",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Por qué la abstención algorítmica activa es un imperativo ético y de negocio en un sistema de inteligencia para asuntos corporativos?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "En un sistema de inteligencia para asuntos corporativos, una alucinación o una afirmación errónea generada por el modelo de IA no es un error cosmético de laboratorio, sino una contingencia legal y reputacional de altísima gravedad. Si el sistema imputa falsamente una sanción ambiental inexistente, confunde una multa de un competidor homónimo o inventa una contradicción en las memorias de la empresa, induce al Directorio a admitir culpas improcedentes, activa falsas alarmas de crisis y deteriora la credibilidad interna del área de comunicaciones. Por ende, la 'Abstención Algorítmica Activa' (Selective Prediction / Abstention) es un imperativo innegociable: el sistema debe poseer autoconsciencia epistemológica para callar cuando la evidencia recuperada sea insuficiente, ambigua o contradictoria, emitiendo un dictamen formal de 'Abstención por Evidencia Insuficiente' en lugar de adivinar o forzar una respuesta verosímil pero infundada. Como establece SABER (Zhu et al., 2026) y P06_RESEARCH_DOSSIER, un sistema corporativo confiable debe operar bajo una curva de riesgo-cobertura calibrada donde el error ante respuestas emitidas sea inferior al 3%, prefiriendo la abstención oportuna antes que el error lesivo.",
        "findings": [
            {
                "claim_id": "P06-F37-C1",
                "claim": "La abstención algorítmica activa es un imperativo para evitar que las alucinaciones del modelo induzcan decisiones corporativas erróneas o crisis reputacionales artificiales.",
                "epistemic_status": "principio_etico_y_de_negocio",
                "scope": {"time": "2023-2026", "region": "Global / Chile", "actor": "Inteligencia Artificial Confiable en Corporaciones"},
                "evidence": [
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 1: Motivation and the Necessity of Abstention in RAG",
                        "excerpt_short": "When retrieved contexts are noisy or conflicting, hallucination risks escalate. Enabling models to abstain selectively when confidence falls below calibrated thresholds is vital for high-stakes enterprise applications.",
                        "source_date": "2026-05-11",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Fase 5: Clasificador de Discrepancias y Filtro de Abstención",
                        "excerpt_short": "Si la evidencia es incompleta o ambigua, el sistema se abstiene (política SABER), impidiendo que el motor de IA invente respuestas o genere falsas alarmas de crisis.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio fundacional del marco SABER y directriz obligatoria del sistema BRIDGE."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta del usuario sobre controversia o compromiso corporativo", "Contexto recuperado con puntaje de confianza"],
            "actors": ["Módulo de Autoconsciencia Epistémica", "Filtro de Abstención SABER", "Usuario Corporativo"],
            "steps": ["Evaluación de completitud y veracidad del contexto", "Medición de incertidumbre epistémica", "Si confianza < umbral de aceptación, detonar abstención", "Presentación de mensaje explicativo: 'Información insuficiente para emitir veredicto'"],
            "states": ["Query_Received", "Uncertainty_Evaluated", "Threshold_Not_Met", "Abstention_Executed"],
            "outputs": ["Respuesta de abstención transparente con solicitud de datos adicionales"],
            "exceptions": ["Consultas donde el usuario fuerza explícitamente una hipótesis exploratoria asumiendo el riesgo"]
        },
        "entities": [
            {"entity_id": "ENT_SABER_FRAMEWORK", "type": "marco_algoritmico", "name": "SABER: Self-Aware Belief Estimator for RAG", "aliases": ["SABER", "Zhu et al. 2026"]}
        ],
        "relations": [
            {"subject_id": "ENT_SABER_FRAMEWORK", "predicate": "formaliza_mecanismo_de", "object_id": "ENT_ALGORITHMIC_ABSTENTION", "valid_from": "2026", "valid_to": "2026", "evidence_claim_id": "P06-F37-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Comportamiento del sistema ante incertidumbre",
                "LLM convencional": "Siempre responde con tono asertivo y seguro, alucinando datos o atribuciones falsas si el contexto es débil.",
                "BRIDGE con SABER": "Reconoce activamente los límites de su conocimiento y se abstiene explícitamente, manteniendo la confianza del usuario."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Tasa máxima de error tolerada ante respuestas emitidas", "denominator": "Total de veredictos no abstenidos", "formula": "Error Rate <= 3% con cobertura >= 70%"}
        ],
        "bridge_implications": [
            {"module": "Compuerta de Abstención Epistémica", "implication": "BRIDGE debe incorporar un botón y política nativa de abstención: preferir responder 'Sin evidencia concluyente' antes que conjeturar sobre hechos jurídicos.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F38"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F38
    {
        "question_id": "P06-F38",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo formaliza el marco SABER (Zhu et al., 2026) el arbitraje de creencias entre Conocimiento Paramétrico (PK) y Conocimiento Contextual (CK) en cuatro cuadrantes?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El marco SABER (Self-Aware Belief Estimator for RAG; Zhu et al., 2026; arXiv:2605.18792) formaliza el conflicto inherente en los sistemas RAG cuando el Conocimiento Paramétrico del modelo preentrenado (Parametric Knowledge - PK, memorizado en sus pesos neuronales) entra en tensión o contradicción con el Conocimiento Contextual recuperado de los documentos externos (Contextual Knowledge - CK). SABER arbitra esta relación evaluando independientemente la confiabilidad estimada de PK y CK, proyectando la decisión en una matriz de cuatro cuadrantes operativos: 1) Cuadrante I (Confiar en CK / Trust CK): La evidencia documental recuperada es de alta solidez y frescura probatoria mientras que PK es incierto o genérico; el sistema responde estrictamente anclado en el documento corporativo; 2) Cuadrante II (Confiar en PK / Trust PK): El contexto recuperado es ruidoso, manipulado o desinformativo mientras que PK posee alta certeza en hechos axiomáticos; el sistema advierte sobre la anomalía del contexto; 3) Cuadrante III (Confiar en Cualquiera / Trust Either): Tanto PK como CK convergen en la misma verdad fáctica de forma robusta; el sistema emite la respuesta con máxima certeza; y 4) Cuadrante IV (Abstención Activa / Abstain): Tanto el conocimiento paramétrico como el contexto documental son altamente inciertos o se contradicen sin sustento suficiente; el sistema rechaza generar una respuesta y declara formalmente su abstención.",
        "findings": [
            {
                "claim_id": "P06-F38-C1",
                "claim": "SABER formaliza el arbitraje entre conocimiento paramétrico y contextual en cuatro cuadrantes: confiar en CK, confiar en PK, confiar en ambos o abstenerse.",
                "epistemic_status": "modelo_teorico_y_algoritmico",
                "scope": {"time": "2026", "region": "Global", "actor": "Zhu et al. (Investigación en RAG Autoconsciente)"},
                "evidence": [
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 3: SABER Framework and the Four-Quadrant Decision Matrix",
                        "excerpt_short": "SABER models self-awareness by estimating parametric belief (PK) and contextual belief (CK), categorizing knowledge states into four quadrants: Trust PK, Trust CK, Trust Either, and Abstain.",
                        "source_date": "2026-05-11",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2.D: Completitud Bibliográfica de SABER",
                        "excerpt_short": "SABER formaliza la decisión en 4 cuadrantes: confiar en PK, confiar en CK, confiar en cualquiera o abstenerse.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Texto completo en HTML de Zhu et al. (2026) verificado y analizado en fuentes activas."
            }
        ],
        "operational_model": {
            "inputs": ["Pregunta corporativa", "Contexto recuperado de base de datos"],
            "actors": ["Estimador de Creencia Paramétrica (PK)", "Estimador de Creencia Contextual (CK)", "Arbitrador de Cuadrantes SABER"],
            "steps": ["Inferencia multi-traza para estimar certeza de PK", "Evaluación de consistencia y autoridad de CK", "Mapeo a coordenadas (PK, CK) en la matriz 2D", "Selección de política: Generar con CK, Generar con PK, Fusión o Abstención"],
            "states": ["Raw_Inputs", "Beliefs_Estimated", "Quadrant_Mapped", "Decision_Enforced"],
            "outputs": ["Respuesta fundamentada o dictamen de abstención fundamentado"],
            "exceptions": ["Consultas donde el contexto documental contiene ataques adversariales de inyección de prompt"]
        },
        "entities": [
            {"entity_id": "ENT_SABER_QUADRANTS", "type": "matriz_decision", "name": "Matriz de Cuatro Cuadrantes SABER", "aliases": ["PK-CK Decision Quadrants"]}
        ],
        "relations": [
            {"subject_id": "ENT_SABER_FRAMEWORK", "predicate": "aplica_matriz", "object_id": "ENT_SABER_QUADRANTS", "valid_from": "2026", "valid_to": "2026", "evidence_claim_id": "P06-F38-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Arbitraje de conocimiento",
                "RAG ingenuo": "Asume ciegamente que el contexto recuperado es siempre verdadero; vulnerable a poisoning y fake news.",
                "SABER": "Compara la plausibilidad paramétrica con la solidez documental; si ambos son débiles o chocan sin base, se abstiene."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Arbitrador Epistémico SABER", "implication": "BRIDGE debe emplear la matriz de 4 cuadrantes de SABER para priorizar el contexto corporativo interno validado sobre los sesgos paramétricos del modelo base.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F39"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F39
    {
        "question_id": "P06-F39",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué requerimientos de entrenamiento y calibración de dominio exigen los predictores de confiabilidad auxiliares de SABER en el contexto corporativo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Como advierte taxativamente P06_QUALITY_ADDENDUM (Sección 3.1), una de las limitaciones críticas del marco SABER es que, aunque no requiere realizar ajuste fino (fine-tuning) de los pesos del modelo fundacional (LLM backbone) —preservando su capacidad de razonamiento general y abaratando el cómputo—, sí exige entrenar dos predictores de confiabilidad auxiliares ligeros (un predictor para la creencia paramétrica $f_\\text{PK}$ y otro para la creencia contextual $f_\\text{CK}$). En un entorno de producción corporativo, estos predictores no pueden tratarse como un módulo plug-and-play de 'cero esfuerzo de supervisión': 1) Inferencia Multi-Traza (Multi-Trace Reasoning): Requieren procesar múltiples trayectorias de razonamiento muestreadas con decodificación estocástica para estimar la entropía del modelo; 2) Calibración con Datos de Dominio Corporativo: Si los predictores fueron entrenados sobre benchmarks generales (TriviaQA o PopQA), sus fronteras de calibración fallarán estrepitosamente al evaluar contratos complejos, balances NCG 461 o resoluciones de la SMA. Por ende, BRIDGE debe calibrar estos predictores auxiliares utilizando un conjunto representativo de pares de preguntas y respuestas corporativas auditadas, asegurando que el umbral de abstención refleje la tolerancia al riesgo real de la empresa.",
        "findings": [
            {
                "claim_id": "P06-F39-C1",
                "claim": "Los predictores de confiabilidad auxiliares de SABER exigen calibración con datos de dominio corporativo (memorias, contratos) para que la frontera de abstención sea válida.",
                "epistemic_status": "requerimiento_de_calibracion_empirica",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Ingeniería de Confiabilidad de IA"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.1: Límites de SABER y el Mecanismo de Abstención Algorítmica",
                        "excerpt_short": "Aunque SABER no realiza ajuste fino de los pesos del modelo fundacional, sí requiere entrenar dos predictores de confiabilidad auxiliares ligeros... En un entorno de producción corporativo, deben calibrarse con datos alineados con el dominio de la empresa (contratos, memorias, regulaciones) y no pueden considerarse un módulo de 'cero esfuerzo de supervisión'.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 4: Auxiliary Reliability Predictor Architecture",
                        "excerpt_short": "The lightweight predictors are trained on internal hidden state representations and multi-trace agreement to estimate belief reliability before response generation.",
                        "source_date": "2026-05-11",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Advertencia crítica y requerimiento de implementación formulado expresamente en P06_QUALITY_ADDENDUM."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus anotado de preguntas corporativas de memorias y regulaciones", "Hidden states de inferencia del LLM base"],
            "actors": ["Ingeniero de ML de BRIDGE", "Entrenador de Predictores Auxiliares"],
            "steps": ["Generación de trazas de razonamiento multi-sample", "Extracción de vectores de confianza", "Entrenamiento de regresores logísticos ligeros para PK y CK", "Calibración de umbrales de abstención con curva de riesgo-cobertura corporativa"],
            "states": ["Raw_Corporate_Dataset", "Hidden_States_Extracted", "Predictors_Trained", "Calibrated_Thresholds_Set"],
            "outputs": ["Módulos auxiliares de confiabilidad calibrados para el dominio"],
            "exceptions": ["Cambios drásticos de versión del LLM base que invalidan las representaciones ocultas y exigen reentrenar predictores"]
        },
        "entities": [
            {"entity_id": "ENT_AUXILIARY_PREDICTORS", "type": "modulo_ml", "name": "Predictores de Confiabilidad Auxiliares SABER", "aliases": ["SABER Auxiliary Predictors"]}
        ],
        "relations": [
            {"subject_id": "ENT_AUXILIARY_PREDICTORS", "predicate": "requiere_calibracion_con", "object_id": "ENT_CORPORATE_DATASET", "valid_from": "2026", "valid_to": "2026", "evidence_claim_id": "P06-F39-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Esfuerzo de supervisión",
                "Fine-tuning completo de LLM": "Costos de cómputo astronómicos (decenas de miles de USD) y riesgo de olvido catastrófico.",
                "Predictores auxiliares SABER": "Entrenamiento ultraligero de clasificadores sobre hidden states, pero requiere curaduría de datos del dominio corporativo."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Calibrador de Dominio BRIDGE", "implication": "BRIDGE debe incluir en su fase de onboarding de nuevos clientes un proceso de calibración de los predictores SABER con las memorias históricas de la empresa.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F40"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F40
    {
        "question_id": "P06-F40",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo opera SelfCheckGPT (Manakul et al., 2023) para la detección de alucinaciones en respuestas generativas mediante muestreo de consistencia estocástica?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "SelfCheckGPT (Manakul et al., 2023; Cambridge University) es un marco pionero de detección de alucinaciones zero-resource (sin necesidad de bases de conocimiento externas ni reentrenamiento) aplicable cuando el modelo genera explicaciones sintéticas. Su fundamento probabilístico radica en que cuando un modelo de lenguaje conoce un hecho de manera sólida, el muestreo estocástico a temperatura no nula produce respuestas conceptualmente idénticas y consistentes; por el contrario, cuando alucina, genera afirmaciones divergentes e internamente contradictorias en cada pasada. El protocolo opera en tres etapas: 1) Generación de Muestras Estocásticas (Stochastic Sampling): Para una respuesta preliminar compuesta por $N$ oraciones, se generan $S$ respuestas alternativas (típicamente $S = 5$ a $10$) con muestreo de temperatura; 2) Medición de Consistencia Sentencia a Sentencia: Cada oración de la respuesta original se evalúa contra las $S$ muestras alternativas utilizando múltiples detectores (consistencia BERTScore, clasificadores NLI o perplejidad MQAG); y 3) Cálculo del Score de Alucinación: Si una oración original es contradicha o no respaldada por la mayoría de las muestras alternativas, recibe un score de alucinación alto ($S_\\text{hallucination} > 0.70$). En BRIDGE, SelfCheckGPT actúa como un filtro de salida (Guardrail Post-Generación): si el score de alucinación supera el umbral, la síntesis se bloquea y se envía a revisión humana.",
        "findings": [
            {
                "claim_id": "P06-F40-C1",
                "claim": "SelfCheckGPT detecta alucinaciones evaluando la consistencia estocástica inter-muestras sentencia por sentencia sin requerir recursos externos adicionales.",
                "epistemic_status": "metodologia_de_deteccion_validada",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Cambridge University (Manakul et al.)"},
                "evidence": [
                    {
                        "source_id": "92983245-75c6-4329-8435-2691fe869f81",
                        "source_title": "Manakul et al. (2023) - SelfCheckGPT: Hallucination Detection",
                        "original_url": "https://arxiv.org/abs/2303.08896",
                        "locator": "Section 2 & 3: Methodology and Stochastic Sampling Consistency",
                        "excerpt_short": "SelfCheckGPT is a zero-resource hallucination detection approach that measures the consistency between multiple stochastic samples drawn from the LLM, flagging sentences with high disagreement as likely hallucinations.",
                        "source_date": "2023-03-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Metodología de detección de alucinaciones formalizada en Manakul et al. (2023)."
            }
        ],
        "operational_model": {
            "inputs": ["Borrador de minuta ejecutiva de crisis generada por el LLM"],
            "actors": ["Sampler Estocástico", "Evaluador de Consistencia NLI SelfCheck", "Guardrail de Salida"],
            "steps": ["Generación de 5 muestras con temperatura 0.7", "Evaluación de concordancia de cada frase del borrador contra las 5 muestras", "Cálculo de probabilidad de alucinación por oración", "Aprobación si todas las oraciones tienen score < 0.25; Bloqueo si alguna supera 0.70"],
            "states": ["Draft_Generated", "5_Samples_Drawn", "Consistency_Scored", "Guardrail_Passed_or_Blocked"],
            "outputs": ["Minuta certificada libre de alucinaciones o alerta de bloqueo"],
            "exceptions": ["Respuestas muy breves donde el muestreo alternativo no exhibe variabilidad suficiente"]
        },
        "entities": [
            {"entity_id": "ENT_SELFCHECKGPT", "type": "marco_de_seguridad_ia", "name": "SelfCheckGPT (Manakul et al., 2023)", "aliases": ["SelfCheckGPT", "Stochastic Hallucination Detection"]}
        ],
        "relations": [
            {"subject_id": "ENT_SELFCHECKGPT", "predicate": "mitiga_alucinaciones_mediante", "object_id": "ENT_STOCHASTIC_CONSISTENCY", "valid_from": "2023", "valid_to": "2026", "evidence_claim_id": "P06-F40-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Método de detección de alucinación",
                "Verificación basada en bases externas": "Exige tener una enciclopedia completa estructurada; falla si el tema es confidencial interno.",
                "SelfCheckGPT": "Funciona en modo caja negra examinando únicamente las distribuciones internas de verosimilitud del propio modelo."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Número de muestras estocásticas en SelfCheckGPT", "denominator": "Tamaño del conjunto de muestreo", "formula": "S = 5 a 10 muestras con temperatura T = 0.7"}
        ],
        "bridge_implications": [
            {"module": "Guardrail de Salida Post-Generación", "implication": "BRIDGE debe aplicar SelfCheckGPT a toda minuta o análisis generado antes de mostrarlo en pantalla al Director de Comunicaciones.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F41"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F41
    {
        "question_id": "P06-F41",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se evalúa la solidez del RAG mediante la Tríada de Métricas de TruLens (Context Relevance, Groundedness, Answer Relevance) y el framework Ragas (Es et al., 2023)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La evaluación rigurosa y continua del pipeline de recuperación y respuesta se formaliza mediante la Tríada de Métricas RAG (RAG Triad) de TruLens y el framework Ragas (Es et al., 2023), midiendo tres dimensiones independientes y complementarias: 1) Relevancia del Contexto (Context Relevance): Evalúa qué porcentaje del texto recuperado por el buscador es estrictamente relevante para verificar la afirmación o responder la consulta, penalizando la contaminación con texto superfluo (Meta de aceptación en P06_RESEARCH_DOSSIER: $\\ge 0.85$); 2) Anclaje Factual y Fidelidad (Groundedness / Faithfulness): Mide si cada aseveración contenida en la respuesta final puede rastrearse directamente y sustentarse en el contexto documental recuperado, impidiendo que el LLM agregue afirmaciones de memoria que no están en el texto (Meta en P06: $\\ge 0.95$, tolerancia cero a alucinaciones de cargos o sanciones inexistentes); y 3) Relevancia de la Respuesta (Answer Relevance): Mide si la respuesta generada aborda de forma directa y completa la pregunta formulada por el usuario corporativo sin evasivas retóricas. Ragas formaliza además el 'Context Precision' y 'Context Recall' contra datasets anotados de referencia, permitiendo una observabilidad algorítmica matemática de todo el pipeline.",
        "findings": [
            {
                "claim_id": "P06-F41-C1",
                "claim": "La calidad del RAG se audita mediante la Tríada de TruLens y Ragas exigiendo Context Relevance >= 0.85 y Groundedness >= 0.95 como metas obligatorias.",
                "epistemic_status": "estandar_de_evaluacion_de_ia",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "TruLens y Ragas (Exploding Gradients)"},
                "evidence": [
                    {
                        "source_id": "f2d23e89-f6fb-42e9-ab4a-88315de31e0d",
                        "source_title": "TruLens - Core Concepts: The RAG Triad of Metrics",
                        "original_url": "https://www.trulens.org/getting_started/core_concepts/rag_triad/",
                        "locator": "The RAG Triad: Context Relevance, Groundedness, and Answer Relevance",
                        "excerpt_short": "TruLens establishes the RAG Triad to isolate failures in retrieval and generation: Context Relevance measures retrieval quality, Groundedness measures hallucination risk, and Answer Relevance measures utility.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7b706c54-6b44-48fe-a0ba-be07e722be6b",
                        "source_title": "Es et al. (2023) - Ragas: Automated Evaluation of RAG",
                        "original_url": "https://arxiv.org/abs/2309.15217",
                        "locator": "Section 2 & 3: Framework Metrics for RAG Evaluation",
                        "excerpt_short": "Ragas introduces reference-free evaluation metrics including faithfulness, answer relevance, and context precision, correlating strongly with human judgment.",
                        "source_date": "2023-09-27",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 4: Entregable Específico 3: Protocolo de Evaluación Sistemática (Métricas Técnicas)",
                        "excerpt_short": "Relevancia del Contexto: Meta >= 0,85. Fidelidad y Anclaje Factual (Groundedness): Meta >= 0,95 (Tolerancia cero a alucinaciones de cargos o multas inexistentes).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Metodología y metas cuantitativas coincidentes en TruLens, Ragas y el Dossier interno."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta de usuario", "Contexto documental recuperado", "Respuesta final generada"],
            "actors": ["Evaluador TruLens", "Motor Ragas", "Dashboard de Calidad de IA de BRIDGE"],
            "steps": ["Cálculo automatizado de Context Relevance", "Cálculo de Groundedness sentencia a sentencia", "Cálculo de Answer Relevance", "Registro de telemetría y alarma si Groundedness < 0.95"],
            "states": ["Interaction_Logged", "Triad_Calculated", "Thresholds_Audited", "Quality_Telemetry_Stored"],
            "outputs": ["Scores cuantitativos de la Tríada RAG por cada respuesta"],
            "exceptions": ["Respuestas legítimamente negativas ('No existe información en las memorias') que afectan Answer Relevance si no se parametriza"]
        },
        "entities": [
            {"entity_id": "ENT_TRULENS", "type": "framework_evaluacion", "name": "TruLens RAG Triad", "aliases": ["TruLens", "RAG Triad"]},
            {"entity_id": "ENT_RAGAS", "type": "framework_evaluacion", "name": "Ragas (Es et al., 2023)", "aliases": ["Ragas Framework", "Exploding Gradients Ragas"]}
        ],
        "relations": [
            {"subject_id": "ENT_TRULENS", "predicate": "define_metricas_replicadas_en", "object_id": "ENT_RAGAS", "valid_from": "2023", "valid_to": "2026", "evidence_claim_id": "P06-F41-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Diagnóstico de fallas en RAG",
                "Baja Context Relevance con alto Groundedness": "El buscador recuperó basura, pero el LLM se ancló fielmente a esa basura.",
                "Alto Context Relevance con bajo Groundedness": "El buscador recuperó el documento perfecto, pero el LLM alucinó y agregó hechos inexistentes.",
                "Tríada TruLens/Ragas": "Permite aislar exactamente si el componente defectuoso es el retriever o el generator."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Context Relevance mínimo aceptable en BRIDGE", "denominator": "Sentencias útiles sobre sentencias recuperadas", "formula": "Context Relevance >= 0.85"},
            {"metric": "Groundedness mínimo aceptable en BRIDGE", "denominator": "Afirmaciones sustentadas sobre afirmaciones emitidas", "formula": "Groundedness >= 0.95"}
        ],
        "bridge_implications": [
            {"module": "Observabilidad y Telemetría RAG", "implication": "BRIDGE debe instrumentar cada llamada RAG con la Tríada TruLens, alertando automáticamente a los administradores si el Groundedness cae de 0.95.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F42"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F42
    {
        "question_id": "P06-F42",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué metodologías propone ARES (Saad-Falcon et al., 2024) para la evaluación automatizada y eficiente de RAG con garantías de significancia estadística?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El marco ARES (Automated RAG Evaluation System; Saad-Falcon et al., 2024; Stanford University) aborda el problema de que evaluar sistemas RAG mediante jueces LLM costosos o anotación humana masiva es económicamente insostenible y carece de rigor estadístico formal. ARES propone una metodología en tres fases que entrega evaluaciones automatizadas con garantías matemáticas de significancia: 1) Generación de Datos Sintéticos y Filtrado Adversarial: Genera pares sintéticos de consultas, documentos y respuestas que cubren intencionalmente escenarios difíciles (pasajes irrelevantes pero léxicamente similares, respuestas engañosas); 2) Entrenamiento de Jueces Ligeros de Dominio (Fine-tuned LLM Judges): Ajusta modelos clasificadores pequeños especializados en Context Relevance, Answer Faithfulness y Answer Relevance utilizando unos pocos cientos de ejemplos anotados del dominio; y 3) Estimación con Intervalos de Confianza (Prediction-Powered Inference - PPI): ARES aplica la inferencia potenciada por predicción (PPI), un método estadístico que combina las predicciones automáticas de los jueces ligeros con una pequeña muestra aleatoria de validación humana para calcular intervalos de confianza rigurosos (ej. 95% CI) sobre las métricas del sistema. Esto permite a BRIDGE certificar su tasa de fidelidad factual con validez estadística auditable sin incurrir en costos exorbitantes de supervisión.",
        "findings": [
            {
                "claim_id": "P06-F42-C1",
                "claim": "ARES implementa jueces especializados ligeros y Prediction-Powered Inference (PPI) para evaluar sistemas RAG con intervalos de confianza estadísticamente garantizados.",
                "epistemic_status": "metodologia_estadistica_avanzada",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Stanford University (Saad-Falcon et al.)"},
                "evidence": [
                    {
                        "source_id": "0de1a4ce-7e57-4bf4-84bd-b30a81f6d963",
                        "source_title": "Saad-Falcon et al. (2024) - ARES: Automated RAG Evaluation",
                        "original_url": "https://arxiv.org/abs/2311.09476",
                        "locator": "Section 1 & 3: Methodology and Prediction-Powered Inference",
                        "excerpt_short": "ARES utilizes synthetic data generation, fine-tuned lightweight judges, and prediction-powered inference (PPI) to provide statistically rigorous evaluations of RAG systems while minimizing human annotation costs.",
                        "source_date": "2023-11-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Formulación matemática rigurosa documentada en Saad-Falcon et al. (2024)."
            }
        ],
        "operational_model": {
            "inputs": ["Log de 10.000 consultas RAG ejecutadas en BRIDGE", "Muestra de validación humana de 150 casos"],
            "actors": ["Generador Sintético ARES", "Jueces Especializados Ligeros", "Optimizador Estadístico PPI"],
            "steps": ["Evaluación masiva con jueces especializados", "Cálculo de concordancia en la muestra humana", "Aplicación de corrección PPI", "Generación de métricas finales con intervalo de confianza al 95%"],
            "states": ["Execution_Logs", "Judges_Evaluated", "Human_Subsample_Compared", "PPI_Confidence_Intervals_Bound"],
            "outputs": ["Certificación estadística auditable de fidelidad RAG"],
            "exceptions": ["Drift de datos donde el tipo de preguntas de los usuarios cambia radicalmente y descalibra los jueces ARES"]
        },
        "entities": [
            {"entity_id": "ENT_ARES_FRAMEWORK", "type": "metodologia_estadistica", "name": "ARES: Automated RAG Evaluation System", "aliases": ["ARES", "Saad-Falcon et al. 2024"]}
        ],
        "relations": [
            {"subject_id": "ENT_ARES_FRAMEWORK", "predicate": "aplica_metodo_estadistico", "object_id": "ENT_PPI_INFERENCE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F42-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de auditoría de calidad",
                "Evaluación informal con LLM-as-a-Judge": "Produce un número puntual arbitrario sin margen de error; susceptible a sesgos del modelo juez.",
                "ARES con PPI": "Produce una métrica acotada matemáticamente con intervalos de confianza al 95%, válida para comités de auditoría y compliance corporativo."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Garantía estadística de evaluación ARES", "denominator": "Nivel de confianza en PPI", "formula": "Intervalo de confianza al 95% (95% CI) con corrección no paramétrica"}
        ],
        "bridge_implications": [
            {"module": "Certificador Estadístico de Calidad", "implication": "BRIDGE debe incorporar ARES en sus pipelines de CI/CD para certificar que cualquier actualización del motor RAG mantiene la fidelidad estadística.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F43"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-F37..F42) to {out_path}.")
