import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-C09
    {
        "question_id": "P06-C09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la función de los modelos de detección de greenwashing (Calamai et al. 2025/2026; Vinella et al. 2023/2024) como detectores de riesgo lingüístico frente a una imputación fáctica o prueba legal de fraude corporativo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste establece una distinción legal y metodológica cardinal subrayada en P06_QUALITY_ADDENDUM (Sección 3.3): 1) Detectores de Riesgo Lingüístico (Calamai et al., 2025/2026; Vinella et al., 2023/2024): Modelos de procesamiento de lenguaje natural entrenados para estimar la probabilidad estadística de que una afirmación ambiental adolezca de divulgación selectiva (destacar atributos positivos menores omitiendo impactos negativos sustantivos) o generalizaciones no respaldadas. Emitir un score de 'Riesgo Alto de Greenwashing' es estrictamente una señal de alerta lingüística preventiva que indica vulnerabilidad ante el escrutinio de ONG o reguladores; 2) Imputación Fáctica o Prueba Legal de Fraude: Exige un estándar probatorio de sede administrativa o judicial (SERNAC, Tribunales de Justicia, SMA) donde se acredite mediante peritajes técnicos independientes, libros contables y auditorías de emisiones que la corporación mintió a sabiendas o engañó al consumidor. Confundir un score de probabilidad algorítmica con una prueba de engaño legal expondría a la empresa a acusaciones internas infundadas, parálisis en sus vocerías y graves contingencias corporativas.",
        "findings": [
            {
                "claim_id": "P06-C09-C1",
                "claim": "Los modelos de lenguaje detectan vulnerabilidades lingüísticas de greenwashing pero jamás constituyen prueba fáctica ni legal de engaño o fraude corporativo.",
                "epistemic_status": "limite_epistemico_y_juridico",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "NLP y Derecho del Consumidor"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.3: Vinella et al. es Prueba de Concepto de Riesgo Potencial, NO Prueba Concluyente de Greenwashing",
                        "excerpt_short": "Un puntaje alto de 'riesgo de greenwashing' emitido por este modelo es una señal de alerta lingüística sobre potencial vulnerabilidad comunicacional... pero bajo ninguna circunstancia constituye prueba concluyente, fáctica o legal de engaño corporativo.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "599d47e4-07ba-4ae2-9ec3-ae05a7cc4557",
                        "source_title": "Vinella et al. (2023-2024) - Language Models Greenwashing (Texto Completo HTML v2)",
                        "original_url": "https://arxiv.org/html/2311.01469v2",
                        "locator": "Section 1 & 6: Linguistic Risk Modeling vs Legal Adjudication",
                        "excerpt_short": "Our models measure linguistic patterns indicative of selective disclosure and greenwashing risk in corporate reports, serving as exploratory screening tools rather than deterministic adjudicators of fraud.",
                        "source_date": "2024-11-24",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio explicitado con total claridad en el Addendum de Calidad y en Vinella et al."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de declaración ambiental", "Score del modelo de Vinella / Calamai"],
            "actors": ["Detector de Riesgo de Greenwashing", "Consejero Legal Corporativo", "Director de Comunicaciones"],
            "steps": ["Cálculo del score de vulnerabilidad lingüística", "Si el score es alto, clasificar como 'Vulnerabilidad Comunicacional Potencial'", "Prohibición explícita de etiquetar como 'Fraude Comprobado'", "Recomendación de blindar la aseveración con auditoría externa previa"],
            "states": ["Raw_Claim", "Linguistic_Risk_Scored", "Flagged_as_Vulnerability", "Review_Recommended"],
            "outputs": ["Alerta interna de vulnerabilidad lingüística"],
            "exceptions": ["Casos donde existe sentencia judicial firme condenatoria por greenwashing"]
        },
        "entities": [
            {"entity_id": "ENT_GREENWASHING_NLP", "type": "modelo_nlp", "name": "Modelos NLP de Greenwashing (Calamai / Vinella)", "aliases": ["Greenwashing Risk Scorer", "ClimateBERT Extensions"]}
        ],
        "relations": [
            {"subject_id": "ENT_GREENWASHING_NLP", "predicate": "mide_riesgo_linguistico_sin_constituir", "object_id": "ENT_LEGAL_FRAUD_PROOF", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza del dictamen",
                "Score de modelo NLP": "Probabilidad estadística de vaguedad léxica u omisión selectiva de impactos negativos.",
                "Sanción del SERNAC / SMA": "Resolución jurídica vinculante con expediente probatorio, descargos y multa formal."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Detector de Vulnerabilidad ESG", "implication": "BRIDGE debe etiquetar los hallazgos de greenwashing como 'Riesgo de Cuestionamiento Comunicacional' y nunca como imputación fáctica de culpabilidad.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C10
    {
        "question_id": "P06-C10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta el estatus vinculante de las normas vigentes en Chile (CMF NCG 461, Circular SERNAC 2024, SMA SNIFA) frente a propuestas normativas o suspendidas internacionalmente (EU Green Claims Directive, SEC Climate Disclosures)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste exige una rigurosa demarcación de la exigibilidad jurídica real de las fuentes al 30 de septiembre de 2026 (P06_QUALITY_ADDENDUM, Sección 3.4): 1) Propuestas Normativas Inciertas e Inexigibles: La Directiva de Aseveraciones Ecológicas de la UE (Green Claims Directive, COM(2023) 166 final) es una propuesta legislativa de la Comisión Europea en trámite de trílogo parlamentario, sujeta a revisiones, dilaciones o enmiendas; no es norma aplicable; 2) Normas Aprobadas pero Suspendidas Judicialmente: La Norma de Divulgación Climática de la SEC (Release 33-11275 de marzo de 2024) fue aprobada en EE.UU., pero la propia SEC emitió una suspensión administrativa voluntaria debido a los litigios consolidados en el Tribunal de Apelaciones del Octavo Circuito; no puede asumirse como estándar obligatorio inmediato; y 3) Normas Plenamente Vigentes y Vinculantes en Chile: La Norma de Carácter General N° 461 de la CMF está plenamente vigente para emisores de valores; la Circular Interpretativa del SERNAC de Diciembre de 2024 sanciona de inmediato el greenwashing en publicidad comercial; y el catastro SNIFA de la SMA emite actos administrativos que constituyen verdad pública probatoria ejecutoriada. BRIDGE debe ponderar con máxima prioridad legal el bloque regulatorio chileno frente a referencias internacionales aspiracionales.",
        "findings": [
            {
                "claim_id": "P06-C10-C1",
                "claim": "Las normas chilenas (CMF NCG 461, Circular SERNAC, SMA SNIFA) tienen vigencia y exigibilidad plena, a diferencia de la propuesta UE Green Claims o la norma SEC suspendida por litigios.",
                "epistemic_status": "estado_regulatorio_verificado",
                "scope": {"time": "2024-2026", "region": "Chile / EE.UU. / UE", "actor": "Reguladores de Mercados y Consumo"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.4: Distinción Estricta del Estatus Regulatorio: Propuestas vs. Normas Vigentes",
                        "excerpt_short": "Directiva UE Green Claims: propuesta legislativa no aprobada ni exigible. SEC Climate Disclosures: suspensión administrativa voluntaria a la espera de resolución judicial en el Octavo Circuito. CMF NCG 461, Circular SERNAC 2024 y SMA SNIFA: normas con vigencia plena, efectiva y comprobada en Chile.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7c48e149-7bf9-4675-9c18-cd676d9461bb",
                        "source_title": "European Commission - Green Claims Directive Proposal",
                        "original_url": "https://environment.ec.europa.eu/topics/circular-economy-topics/green-claims_en",
                        "locator": "Legislative Status: Commission Proposal COM(2023) 166",
                        "excerpt_short": "Proposal for a Directive on substantiation and communication of explicit environmental claims (Green Claims Directive) pending ordinary legislative procedure.",
                        "source_date": "2023-03-22",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "63b1de09-9f1d-41a5-9330-66204a40f355",
                        "source_title": "SEC (2024) - Final Rule: Climate-Related Disclosures for Investors",
                        "original_url": "https://www.sec.gov/news/press-release/2024-31",
                        "locator": "Administrative Stay Notice",
                        "excerpt_short": "The Commission issued a stay of the final rules pending completion of judicial review of the consolidated Eighth Circuit petitions.",
                        "source_date": "2024-04-04",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación legal exhaustiva documentada en P06_QUALITY_ADDENDUM."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta sobre exigibilidad de un estándar ambiental"],
            "actors": ["Clasificador de Estatus Jurídico", "Motor Normativo de BRIDGE"],
            "steps": ["Verificación de jurisdicción territorial", "Comprobación de vigencia formal al corte (30-09-2026)", "Asignación de etiqueta: 'Norma Vigente Exigible' vs 'Propuesta Legislativa en Trámite' vs 'Norma Suspendida por Litigio'", "Ponderación en la matriz de riesgo"],
            "states": ["Raw_Standard", "Jurisdiction_Checked", "Enforceability_Determined", "Risk_Pondered"],
            "outputs": ["Calificación jurídica rigurosa del requerimiento de reporte"],
            "exceptions": ["Empresas chilenas con ADRs en Wall Street que deben monitorear activamente el desenlace judicial de la SEC"]
        },
        "entities": [
            {"entity_id": "ENT_EU_GREEN_CLAIMS", "type": "propuesta_legislativa", "name": "EU Green Claims Directive Proposal COM(2023) 166", "aliases": ["Directiva Green Claims UE"]},
            {"entity_id": "ENT_SEC_STAY", "type": "resolucion_judicial", "name": "Suspensión Administrativa SEC Climate Rules (8th Circuit)", "aliases": ["SEC Administrative Stay"]}
        ],
        "relations": [
            {"subject_id": "ENT_REGULATORY_TRIANGLE_CHILE", "predicate": "posee_mayor_exigibilidad_que", "object_id": "ENT_EU_GREEN_CLAIMS", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C10-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Estatus de exigibilidad",
                "Propuesta UE Green Claims": "Documento político en discusión; no acarrea sanciones inmediatas.",
                "Norma SEC Clima": "Aprobada formalmente pero suspendida por tribunales; reporte en pausa.",
                "CMF NCG 461 y Circular SERNAC Chile": "Plena vigencia legal; acarrea formulación de cargos y sanciones inmediatas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Filtro de Exigibilidad Jurídica", "implication": "BRIDGE debe priorizar en su motor de riesgo las normas con vigencia ejecutoria comprobada en Chile antes que borradores internacionales no vinculantes.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C11
    {
        "question_id": "P06-C11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la abstención algorítmica conservadora (SABER) frente al riesgo de omitir alertas tempranas de crisis reputacional de alta velocidad (breaking news)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste plantea una tensión operacional crítica advertida en P06_GAPS_AND_VALIDATION (Sección 2.1): 1) Riesgo de Sobre-Abstención (Over-Abstention): Marcos como SABER están calibrados para maximizar la fidelidad y anclaje factual (Groundedness $\\ge 0.95$), ordenando la abstención activa cuando la evidencia externa es ruidosa o fragmentaria. Sin embargo, en el inicio de una crisis de reputación de alta velocidad (un accidente en planta, una protesta o una filtración en redes), la información inicial siempre es caótica, incompleta y no verificada. Si el sistema se abstiene silenciosamente en esta fase por falta de certezas probatorias, el Director de Asuntos Corporativos se queda a ciegas durante las primeras horas críticas ('Golden Hour'), perdiendo la oportunidad de preparar la contención; 2) Solución Arquitectural Dual de BRIDGE: Para resolver esta tensión, BRIDGE desdobla el flujo ante incertidumbre: ante señales ruidosas pero con alta velocidad de viralización ($R_0 > 1$), el sistema se abstiene de dictaminar una 'Contradicción Factual' (no emite juicios infundados), pero emite una 'Alerta de Detección Temprana de Narrativa Hostil' indicando expresamente que se trata de una acusación no verificada en desarrollo. Así protege la veracidad del sistema sin sacrificar la velocidad de alerta situacional.",
        "findings": [
            {
                "claim_id": "P06-C11-C1",
                "claim": "La sobre-abstención de SABER puede cegar al equipo de crisis ante breaking news; se resuelve absteniéndose de emitir dictamen factual pero alertando sobre la narrativa emergente.",
                "epistemic_status": "solucion_arquitectural_a_tension_operativa",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Gestión de Crisis en Tiempo Real"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Riesgo de Sobre-Abstención vs. Falsa Certeza en Situaciones de Crisis",
                        "excerpt_short": "Los marcos de abstención algorítmica como SABER son esenciales para evitar alucinaciones, pero en el contexto de una crisis de reputación de alta velocidad, la abstención del sistema puede privar a los directores de comunicación de alertas tempranas sobre narrativas emergentes hostiles.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Tensión identificada y resuelta en P06_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Señal externa ruidosa en redes con rápida aceleración temporal"],
            "actors": ["Detector de Viralidad", "Arbitrador SABER", "Despachador de Alertas Duales"],
            "steps": ["SABER detecta baja certeza en la evidencia documental", "SABER se abstiene de declarar 'Contradicción Real'", "Detector de viralidad constata aceleración de menciones", "Emisión de 'Alerta de Tracción de Narrativa' con advertencia de hecho no verificado"],
            "states": ["Raw_Noisy_Spike", "Fact_Check_Abstained", "Narrative_Spike_Confirmed", "Situational_Alert_Fired"],
            "outputs": ["Alerta situacional sin juicio factual erróneo"],
            "exceptions": ["Campañas artificiales de bots sin tracción orgánica que son descartadas por el filtro de spam"]
        },
        "entities": [
            {"entity_id": "ENT_DUAL_ALERT_POLICY", "type": "politica_operativa", "name": "Política de Alerta Dual BRIDGE (Hecho vs Narrativa)", "aliases": ["Dual Alert Policy"]}
        ],
        "relations": [
            {"subject_id": "ENT_DUAL_ALERT_POLICY", "predicate": "equilibra_tension_entre", "object_id": "ENT_SABER_FRAMEWORK", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C11-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Respuesta ante señal ruidosa inicial",
                "SABER puro sin matiz": "Silencio absoluto (Abstención); el director se entera por el llamado indignado del Presidente del Directorio.",
                "Política Dual BRIDGE": "Se abstiene de juzgar la verdad, pero avisa al director que hay una narrativa hostil ganando tracción en redes."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Despachador de Alertas Tempranas", "implication": "BRIDGE debe implementar la alerta dual: separar la 'Alerta de Consistencia Factual' (rigurosa y conservadora) de la 'Alerta de Volumen de Narrativa' (sensible y veloz).", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C12
    {
        "question_id": "P06-C12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la automatización total de respuestas corporativas vía LLM frente a la arquitectura Human-in-the-Loop con compuertas de abstención estratégica en el módulo Actuar de BRIDGE?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste representa la línea divisoria entre la irresponsabilidad operativa y la IA corporativa madura: 1) Automatización Total Desatendida: Arquitecturas ingenuas donde un agente LLM autónomo detecta una noticia negativa y procede inmediatamente a redactar y publicar comunicados de prensa, respuestas en redes o cartas al director sin intervención humana. Este enfoque introduce riesgos corporativos letales: alucinaciones jurídicas, admisión inadvertida de culpas penales, promesas comerciales inviables y escalamiento innecesario de controversias menores (efecto Streisand); 2) Human-in-the-Loop con Compuertas de Abstención Estratégica (BRIDGE): En el módulo Actuar de BRIDGE, la IA tiene prohibido por diseño emitir comunicaciones hacia el exterior. Su rol se restringe a estructurar la información interna, mapear las opciones estratégicas (Opción A: Aclaración técnica; Opción B: Rectificación proactiva; Opción C: Silencio y abstención estratégica) y redactar borradores internos de Q&A para los voceros. La decisión de responder, el tono y el momento son potestad exclusiva y no delegable del Director de Asuntos Corporativos y el Gerente Legal.",
        "findings": [
            {
                "claim_id": "P06-C12-C1",
                "claim": "La automatización total de respuestas corporativas por LLM acarrea riesgos letales; BRIDGE impone supervisión humana obligatoria y compuertas de abstención estratégica.",
                "epistemic_status": "principio_de_seguridad_operacional",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Gobernanza de Inteligencia Artificial"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Fase 6: Interfaz Corporativa y Bucle Humano (Human-in-the-Loop)",
                        "excerpt_short": "Dejando siempre la decisión comunicacional final en manos humanas... Compuertas de abstención estratégica ante provocaciones sin tracción en actores legítimos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "ea19c0ed-88be-4eff-8870-54c8217fa513",
                        "source_title": "IABC - Code of Ethics for Professional Communicators",
                        "original_url": "https://www.iabc.com/about/what-we-do/standards/code-of-ethics",
                        "locator": "Professional Responsibility and Accountability",
                        "excerpt_short": "Communicators take personal responsibility for the accuracy and consequences of corporate communications, adhering to professional judgment.",
                        "source_date": "2023-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio medular de arquitectura de software y ética corporativa."
            }
        ],
        "operational_model": {
            "inputs": ["Escenario de crisis o contradicción confirmada"],
            "actors": ["Módulo Actuar BRIDGE", "Director de Asuntos Corporativos (Humano)", "Gerente General"],
            "steps": ["Generación de 3 cursos de acción alternativos con sus respectivos pros y contras", "Redacción de minuta borrador confidencial bajo llave", "Presentación al Director en interfaz segura", "Firma y liberación externa ejecutada por el humano"],
            "states": ["Scenario_Analyzed", "Options_Generated", "Human_Review_Pending", "Human_Executed_External"],
            "outputs": ["Estrategia de vocería validada y autorizada por la alta dirección"],
            "exceptions": ["Intentos de automatización mediante scripts de terceros bloqueados a nivel de API"]
        },
        "entities": [
            {"entity_id": "ENT_ACTUAR_MODULE", "type": "modulo_de_software", "name": "Módulo Actuar BRIDGE", "aliases": ["BRIDGE Act Module", "Response Strategy Engine"]}
        ],
        "relations": [
            {"subject_id": "ENT_ACTUAR_MODULE", "predicate": "restringe_acciones_a_borradores_internos_con", "object_id": "ENT_HITL_GOVERNANCE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C12-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Emisión de declaraciones",
                "Agente LLM totalmente autónomo": "Escribe y publica tweets o notas de prensa desatendidas; riesgo infinito de crisis autoinfligida.",
                "Módulo Actuar BRIDGE": "Nunca publica nada hacia afuera; prepara minutas y deja la pluma y la voz en los ejecutivos responsables."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Seguridad del Módulo Actuar", "implication": "BRIDGE debe carecer intencionalmente de integraciones de publicación directa en redes o newswires; solo exporta minutas internas seguras.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C13
    {
        "question_id": "P06-C13",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la evaluación con ground truth estático en datasets abiertos frente a la evaluación continua con la tríada RAG de TruLens y calibración de dominio en ARES?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste define la diferencia entre una validación de laboratorio académica y la observabilidad de un sistema en producción real: 1) Evaluación con Ground Truth Estático (Enfoque Tradicional): Mide el desempeño del sistema calculando métricas clásicas (Exact Match, BLEU, ROUGE) sobre un conjunto congelado de preguntas y respuestas predefinidas (ej. SQuAD, HotpotQA). Este enfoque se vuelve obsoleto al día siguiente del despliegue: en producción corporativa, los documentos cambian continuamente con cada nueva memoria, las noticias del entorno son impredecibles y no existe un 'ground truth' humano prefabricado para cada evento emergente; 2) Evaluación Continua con Tríada TruLens y ARES: No requiere respuestas humanas canónicas preexistentes. TruLens evalúa en tiempo real cada interacción midiendo la coherencia geométrica y atencional entre Query, Context y Answer (Relevancia del Contexto, Groundedness y Relevancia de la Respuesta). Complementariamente, ARES utiliza Prediction-Powered Inference (PPI) para certificar estadísticamente con intervalos de confianza al 95% si el sistema mantiene su rendimiento a lo largo del tiempo, detectando el 'drift' de datos corporativos antes de que impacte a los usuarios.",
        "findings": [
            {
                "claim_id": "P06-C13-C1",
                "claim": "Los datasets estáticos no capturan la evolución de datos corporativos; la tríada TruLens y ARES habilitan evaluación continua sin referencia previa y con significancia estadística.",
                "epistemic_status": "contraste_de_metodologias_de_evaluacion",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Observabilidad y Monitoreo de IA"},
                "evidence": [
                    {
                        "source_id": "f2d23e89-f6fb-42e9-ab4a-88315de31e0d",
                        "source_title": "TruLens - Core Concepts: The RAG Triad of Metrics",
                        "original_url": "https://www.trulens.org/getting_started/core_concepts/rag_triad/",
                        "locator": "Section: Reference-free Continuous Evaluation",
                        "excerpt_short": "The RAG Triad provides reference-free evaluation for live systems in production, continuously auditing retrieval quality and hallucination without requiring golden ground truth datasets.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "0de1a4ce-7e57-4bf4-84bd-b30a81f6d963",
                        "source_title": "Saad-Falcon et al. (2024) - ARES: Automated RAG Evaluation",
                        "original_url": "https://arxiv.org/abs/2311.09476",
                        "locator": "Section 1: Automated Evaluation in Dynamic Environments",
                        "excerpt_short": "ARES addresses domain shifts and evolving knowledge bases by dynamically generating synthetic validation sets and calibrating judges using statistical prediction-powered inference.",
                        "source_date": "2023-11-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Metodologías de observabilidad de vanguardia en TruLens y Stanford ARES."
            }
        ],
        "operational_model": {
            "inputs": ["Flujo de consultas y respuestas en producción corporativa"],
            "actors": ["Telemetría TruLens", "Optimizador PPI ARES", "Panel de Calidad de BRIDGE"],
            "steps": ["Cálculo online de la Tríada RAG por cada llamada", "Muestreo semanal de 50 casos para validación humana", "Ajuste PPI en ARES y generación de intervalos de confianza al 95%", "Alerta si la métrica de fidelidad cae de la meta operacional"],
            "states": ["Live_Inference", "Triad_Computed_Online", "PPI_Calibrated_Weekly", "SLAs_Certified"],
            "outputs": ["Monitoreo continuo de salud y confiabilidad del sistema"],
            "exceptions": ["Corrupciones en logs de auditoría que son subsanadas con almacenamiento redundante"]
        },
        "entities": [
            {"entity_id": "ENT_CONTINUOUS_EVALUATION", "type": "paradigma_de_calidad", "name": "Evaluación Continua Reference-Free", "aliases": ["Live RAG Observability"]}
        ],
        "relations": [
            {"subject_id": "ENT_CONTINUOUS_EVALUATION", "predicate": "supera_a", "object_id": "ENT_STATIC_GROUND_TRUTH", "valid_from": "2023", "valid_to": "2026", "evidence_claim_id": "P06-C13-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Monitoreo en producción",
                "Dataset estático congelado": "Se evalúa una vez en el laboratorio y se ignora qué ocurre cuando entran nuevos documentos.",
                "Tríada TruLens + ARES": "Audita matemáticamente cada respuesta entregada en vivo a los ejecutivos de la empresa."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Telemetría Continua de Calidad", "implication": "BRIDGE debe incorporar TruLens como middleware de telemetría para evaluar cada interacción en producción sin depender de ground truth manual.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C14"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C14
    {
        "question_id": "P06-C14",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrastan las afirmaciones ambientales absolutas ('100% ecológico', 'cero residuos') frente a compromisos condicionales con metas intermedias bajo el escrutinio de la Circular de Greenwashing del SERNAC?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste refleja el núcleo sancionatorio de la Circular Interpretativa de Sostenibilidad del SERNAC (Diciembre 2024, Chile; Ley 19.496): 1) Afirmaciones Ambientales Absolutas o Categóricas ('100% ecológico', 'cero impacto', 'plástico biodegradable en 90 días', 'cero huella de carbono'): Son calificadas por el SERNAC como de altísimo riesgo infraccional y presunción de engaño al consumidor. La Circular establece que las empresas no pueden utilizar términos absolutos a menos que cuenten con certificación científica previa, verificable, independiente e integral de todo el ciclo de vida del producto; la falta de dicha acreditación técnica acarrea denuncias inmediatas y multas de hasta 1.500 UTM; 2) Compromisos Condicionales con Metas Intermedias: Declaraciones rigurosas que explicitan el año base, el alcance metodológico y la trayectoria gradual (ej. 'En 2024 logramos un 65% de contenido reciclado en nuestra línea de envases, avanzando hacia la meta de 80% en 2028 bajo certificación ISO 14021'). Este tipo de formulación cumple con las directrices del SERNAC, permite auditoría externa y protege a la empresa de cargos por greenwashing. BRIDGE debe advertir proactivamente a los equipos de asuntos corporativos ante cualquier afirmación absoluta no demostrada.",
        "findings": [
            {
                "claim_id": "P06-C14-C1",
                "claim": "La Circular del SERNAC sanciona afirmaciones absolutas no acreditadas científicamente ('100% ecológico'), avalando en cambio metas intermedias verificables con año base y alcance explícito.",
                "epistemic_status": "criterio_administrativo_vigente",
                "scope": {"time": "2024-2026", "region": "Chile", "actor": "SERNAC y Derecho del Consumidor"},
                "evidence": [
                    {
                        "source_id": "33d0f555-7934-4af8-913b-89920a2514ac",
                        "source_title": "SERNAC Chile - Circular sobre Consumo Sostenible y Greenwashing",
                        "original_url": "https://www.sernac.cl/604/w3-article-83768.html",
                        "locator": "Criterios Generales: Prohibición de Afirmaciones Absolutas No Acreditadas",
                        "excerpt_short": "Las aseveraciones categóricas o absolutas como '100% verde' o 'libre de impacto' no pueden ser empleadas sin sustento técnico comprobable en todo el ciclo de vida, constituyendo infracción a la exigencia de información veraz y oportuna.",
                        "source_date": "2024-12-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Caso CLM-03: Envases 100% biodegradables vs Oficio SERNAC",
                        "excerpt_short": "Retirar afirmación absoluta de la publicidad conforme a Circular SERNAC 2024; publicar fe de erratas con las condiciones técnicas reales de compostaje industrial.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Criterio normativo expreso de la Circular Interpretativa de Sostenibilidad del SERNAC."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de campaña publicitaria o memoria con aseveraciones ambientales"],
            "actors": ["Detector de Términos Absolutos", "Verificador de Certificación Técnica", "Compliance de Publicidad"],
            "steps": ["Escaneo de términos de riesgo ('100%', 'cero emisiones', 'eco-friendly', 'totalmente verde')", "Verificación de presencia de certificado técnico o dictamen de ciclo de vida", "Si carece de certificado, disparar alerta de alto riesgo SERNAC", "Sugerir reformulación con métricas intermedias condicionadas"],
            "states": ["Raw_Campaign", "Absolute_Terms_Flagged", "Certification_Missing", "SERNAC_Warning_Issued"],
            "outputs": ["Alerta preventiva de riesgo de greenwashing SERNAC"],
            "exceptions": ["Productos que efectivamente cuentan con certificación oficial de residuo cero o carbono neutro de alcance completo"]
        },
        "entities": [
            {"entity_id": "ENT_SERNAC_CIRCULAR", "type": "normativa_consumo", "name": "Circular Interpretativa de Sostenibilidad SERNAC 2024", "aliases": ["Circular Greenwashing SERNAC", "Criterio SERNAC Sostenible"]}
        ],
        "relations": [
            {"subject_id": "ENT_SERNAC_CIRCULAR", "predicate": "prohibe_afirmaciones_de_tipo", "object_id": "ENT_ABSOLUTE_GREEN_CLAIMS", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C14-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Redacción de la aseveración",
                "Afirmación absoluta de alto riesgo": "'Nuestra empresa es 100% verde y no contamina el planeta'.",
                "Compromiso condicionado conforme a SERNAC": "'Hemos reducido un 35% las emisiones de Alcance 1 y 2 al 2024, con meta auditada de 50% al 2030 bajo estándar GHG Protocol'."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Auditor de Declaraciones Ambientales", "implication": "BRIDGE debe incluir una compuerta que detecte adjetivos absolutos en textos comerciales y recomiende reemplazarlos por metas condicionadas y respaldadas.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C15"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C15
    {
        "question_id": "P06-C15",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la sensibilidad legal de registrar hallazgos de inconsistencia interna en bases de datos corporativas (riesgo de exhibición judicial / discovery) frente a la necesidad de inteligencia de asuntos corporativos?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste expone una severa tensión organizacional entre el área de Asuntos Corporativos y la Gerencia Legal (Compliance/Litigios), analizada en P06_GAPS_AND_VALIDATION (Sección 2.2): 1) El Riesgo Legal de Exhibición Judicial (Discovery): Si un software de inteligencia artificial etiqueta formalmente en una base de datos corporativa persistente que 'Existe una Contradicción Real entre la memoria y la realidad operacional', dicho registro digital puede ser sujeto a exhibición forzosa de documentos (Discovery en cortes anglosajonas o medidas para mejor resolver / requerimientos de la fiscalía y tribunales ambientales en Chile), transformando una herramienta de alerta en una prueba autoincriminatoria contra la propia empresa; 2) La Necesidad de Inteligencia y Anticipación: Si el sistema no registra las brechas por miedo legal, la alta dirección opera a ciegas y es sorprendida por la prensa y los reguladores; y 3) Solución de Gobernanza y Privilegio Legal en BRIDGE: BRIDGE resuelve esta tensión mediante dos salvaguardas: a) Arquitectura bajo Secreto Profesional y Asesoría Legal (Attorney-Client Privilege): Los análisis profundos de contradicciones se configuran como borradores de trabajo solicitados por la Fiscalía Corporativa para evaluación de riesgos jurídicos, gozando de reserva legal; y b) Trazabilidad Epistémica Neutral: El sistema no califica jurídicamente la conducta como 'delito' o 'fraude', sino como 'Discrepancia Atributaria Requiriendo Verificación Humana', protegiendo a la corporación.",
        "findings": [
            {
                "claim_id": "P06-C15-C1",
                "claim": "El registro de inconsistencias genera riesgos de exhibición judicial (discovery); BRIDGE mitiga esto mediante lenguaje técnico neutral y amparo bajo privilegio de asesoría legal.",
                "epistemic_status": "diseno_de_gobernanza_y_seguridad_juridica",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Fiscalía Corporativa y Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Tensión Organizacional entre Áreas Legales y de Asuntos Corporativos",
                        "excerpt_short": "La identificación algorítmica de una 'contradicción real' genera inmediata sensibilidad legal. Si los hallazgos quedan registrados en bases de datos internas, podrían ser sujetos a exhibición judicial (discovery). Esto exige políticas estrictas de gobierno de datos y permisos de acceso.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Tensión corporativa real identificada en P06_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Detección de inconsistencia documental severa"],
            "actors": ["Motor BRIDGE", "Fiscalía Corporativa", "Comité de Riesgos"],
            "steps": ["Registro del hallazgo con terminología epistemológica neutral", "Aplicación de políticas de acceso restringido ABAC (solo fiscalía y CCO)", "Protección del repositorio bajo privilegio de asesoría legal", "Remediación interna sin emisión de dictámenes autoincriminatorios públicos"],
            "states": ["Discrepancy_Detected", "Legal_Privilege_Applied", "Restricted_Access_Enforced", "Remediated_Internally"],
            "outputs": ["Informe de riesgo jurídicamente protegido"],
            "exceptions": ["Requerimientos perentorios del Ministerio Público bajo orden de allanamiento judicial"]
        },
        "entities": [
            {"entity_id": "ENT_LEGAL_DISCOVERY_RISK", "type": "riesgo_juridico", "name": "Riesgo de Exhibición Judicial (Legal Discovery Risk)", "aliases": ["Discovery Risk", "Autoincriminación Documental"]}
        ],
        "relations": [
            {"subject_id": "ENT_LEGAL_DISCOVERY_RISK", "predicate": "es_mitigado_por", "object_id": "ENT_ABAC_GOVERNANCE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C15-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Registro de hallazgos",
                "Sistema ingenuo sin asesoría legal": "Guarda registros abiertos que dicen 'Nuestra empresa cometió greenwashing deliberado', facilitando demandas judiciales.",
                "Protocolo BRIDGE": "Registra 'Discrepancia técnica perimetral bajo revisión de fiscalía corporativa', amparado por reserva profesional."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gobernanza de Acceso y Redacción Neutral", "implication": "BRIDGE debe utilizar taxonomías descriptivas neutras y control de acceso ABAC estricto para no generar contingencias de discovery a las empresas clientes.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C16"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C16
    {
        "question_id": "P06-C16",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrastan las capacidades declaradas por proveedores comerciales (Signal AI, AlphaSense, Dataminr) frente a la necesidad de validación empírica independiente en terreno mediante pruebas de concepto (PoC)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste refleja el imperativo de escepticismo metodológico formalizado en P06_QUALITY_ADDENDUM (Sección 3.5): 1) Capacidades Declaradas por Fabricantes Comerciales (Vendor Marketing / Commercial Documentation): Suites globales como Signal AI (AIQ Engine), AlphaSense Enterprise Intelligence y Dataminr Pulse promocionan capacidades sobresalientes en folletos comerciales (indexación de miles de millones de documentos, taxonomías automatizadas de ESG, análisis de riesgo en tiempo real). Sin embargo, su material técnico describe lo que el fabricante afirma que el sistema hace, sin auditorías independientes revisadas por pares que certifiquen su tasa real de falsos positivos en jurisdicciones no anglosajonas ni su efectividad sobre estructuras complejas de holdings familiares en Chile; 2) Necesidad de Validación Empírica Independiente: Para una corporación o para el diseño de BRIDGE, es un error metodológico asumir la infalibilidad de estas herramientas sin pruebas de concepto (PoC) rigurosas. Como prescribe P06_GAPS_AND_VALIDATION, la eficacia real debe medirse en terreno mediante un protocolo empírico de 3 fases: backtesting con casos históricos locales de la SMA y CMF, entrevistas estructuradas con directores de empresas IPSA y shadow running de 60 días en operación paralela real.",
        "findings": [
            {
                "claim_id": "P06-C16-C1",
                "claim": "Las capacidades comerciales de Signal AI, AlphaSense y Dataminr describen afirmaciones de fabricantes; la efectividad real en América Latina exige validación empírica independiente mediante PoCs.",
                "epistemic_status": "principio_de_escepticismo_empirico",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Evaluación de Software Corporativo"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.5: Soluciones Comerciales: Capacidades Declaradas vs. Eficacia Independiente",
                        "excerpt_short": "No existen hasta la fecha estudios de auditoría independientes, públicos y revisados por pares que midan la tasa real de falsos positivos en la detección de controversias corporativas... la efectividad en terreno debe ser validada mediante pruebas de concepto empíricas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 4: Protocolo de Validación Empírica en Terreno (Chile y Latinoamérica)",
                        "excerpt_short": "Validación Retrospectiva con Casos Históricos Chilenos (10 casos), 12 entrevistas estructuradas con directores de asuntos corporativos y Shadow Running de 60 días.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio metodológico y ético establecido unívocamente en las síntesis del pilar P06."
            }
        ],
        "operational_model": {
            "inputs": ["Promesas comerciales de software de inteligencia", "Datos reales de memorias NCG 461 y causas SMA"],
            "actors": ["Comité de Evaluación de Tecnología", "Equipo de Producto BRIDGE", "Usuarios Piloto IPSA"],
            "steps": ["Diseño de PoC empírica con datos históricos locales", "Medición de latencia real, precisión y tasa de falsos positivos", "Comparación de costo-beneficio", "Certificación empírica antes de adquisición o despliegue a gran escala"],
            "states": ["Vendor_Claims_Reviewed", "PoC_Designed", "Pilot_Executed_in_Field", "Empirical_Verdict_Delivered"],
            "outputs": ["Dictamen empírico de viabilidad técnica e idoneidad regional"],
            "exceptions": ["Proveedores comerciales que imponen cláusulas contractuales restrictivas impidiendo publicar benchmarks comparativos"]
        },
        "entities": [
            {"entity_id": "ENT_COMMERCIAL_VENDORS", "type": "conglomerado_proveedores", "name": "Suites Comerciales de Inteligencia (Signal AI, AlphaSense, Dataminr)", "aliases": ["Commercial Risk Intelligence Platforms"]}
        ],
        "relations": [
            {"subject_id": "ENT_VALIDATION_ROADMAP", "predicate": "certifica_empiricamente_superioridad_sobre", "object_id": "ENT_COMMERCIAL_VENDORS", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C16-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Fundamento de adopción",
                "Confianza ciega en marketing de proveedores": "Adopta plataformas internacionales que fracasan al intentar mapear RUTs o entender resoluciones del Diario Oficial chileno.",
                "Validación empírica en terreno BRIDGE": "Certifica con backtesting y pilotos reales que el software resuelve las complejidades jurídicas y societarias locales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Estrategia de Go-to-Market y Validación", "implication": "BRIDGE debe utilizar los resultados de su protocolo de validación empírica en 3 fases como el diferenciador competitivo definitivo frente a suites comerciales anglosajonas.", "status": "estrategia_comercial"}
        ],
        "open_gaps": [],
        "next_question_ids": ["FIN_P06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-C09..C16) to {out_path}.")
