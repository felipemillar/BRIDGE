import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-F01
    {
        "question_id": "P06-F01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo fundamenta el corpus la necesidad ontológica y estratégica de cruzar el conocimiento interno de la corporación con las señales del entorno exterior?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El corpus fundamenta que el cruce sistemático entre el conocimiento corporativo documentado (memorias CMF NCG 461, políticas, discursos, compromisos ESG) y las señales del entorno exterior (prensa, boletines judiciales/regulatorios, redes sociales) responde a una necesidad ontológica y estratégica ineludible: superar la asimetría de información y el monitoreo pasivo tradicional para construir una ontología operacional centrada en la toma de decisiones. Según P06_EVIDENCE_MAP y P06_RESEARCH_DOSSIER, la reputación y la licencia social no se gestionan midiendo menciones o sentimientos aislados, sino contrastando las afirmaciones y compromisos que la empresa formula contra los hechos objetivos verificados en el entorno (Arthur W. Page Principles: 'Tell the truth and prove it with action'). Soluciones como Signal AI (2.600M documentos anuales indexados) y Palantir Foundry demuestran que conectar la malla de entidades internas con feeds externos en tiempo real permite detectar vulnerabilidades operacionales, brechas de cumplimiento regulatorio y riesgos reputacionales de forma temprana y accionable.",
        "findings": [
            {
                "claim_id": "P06-F01-C1",
                "claim": "El cruce de afirmaciones internas y señales del entorno supera el monitoreo pasivo transformando datos dispersos en una ontología operacional para la gestión de riesgos.",
                "epistemic_status": "consenso_analitico",
                "scope": {"time": "2020-2026", "region": "Global", "actor": "Corporaciones y Reguladores"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 1: El Cruce Afirmación-Entorno no es Novedoso, pero su Automatización Sí",
                        "excerpt_short": "El cambio paradigmático radica en pasar de un monitoreo pasivo de menciones (clipping) a una ontología operacional que vincula entidades corporativas internas (metas de descarbonización, políticas laborales, subsidios, contratos) con señales externas en tiempo real.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 1: Marco Teórico y Fundamentos Conceptuales",
                        "excerpt_short": "El 90% de la reputación corporativa depende de la conducta operativa de la empresa y solo el 10% de lo que la empresa dice de sí misma. Por ende, cualquier aplicación tecnológica en este campo debe actuar como un sensor de consistencia operativa y no como una herramienta de propaganda.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fundamentación conceptual respaldada por las síntesis internas y literatura de gobernanza y estrategia corporativa."
            }
        ],
        "operational_model": {
            "inputs": ["Repositorio documental corporativo (Memorias NCG 461, discursos, políticas)", "Feeds externos de noticias (Factiva), boletines regulatorios (SMA, CMF, SERNAC)"],
            "actors": ["Comité de Asuntos Corporativos", "Dirección de Riesgos y Compliance", "Motor de IA (BRIDGE)"],
            "steps": ["Extracción de afirmaciones/compromisos internos", "Recuperación de señales externas contextuales", "Resolución de entidades y contraste NLI", "Detección de brechas e inconsistencias"],
            "states": ["Raw_Inputs", "Entities_Resolved", "Cross_Referenced", "Inconsistencies_Alerted"],
            "outputs": ["Matriz Afirmación-Evidencia", "Alertas tempranas de inconsistencia"],
            "exceptions": ["Feeds externos inaccesibles o bloqueados por paywall"]
        },
        "entities": [
            {"entity_id": "ENT_SIGNAL_AI", "type": "plataforma_comercial", "name": "Signal AI Platform", "aliases": ["Signal AI", "AIQ Engine"]},
            {"entity_id": "ENT_PALANTIR", "type": "plataforma_comercial", "name": "Palantir Foundry / AIP", "aliases": ["Palantir AIP", "Foundry Ontology"]}
        ],
        "relations": [
            {"subject_id": "ENT_SIGNAL_AI", "predicate": "indexa_señales_externas_contra", "object_id": "ENT_PALANTIR", "valid_from": "2020", "valid_to": "2026", "evidence_claim_id": "P06-F01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de monitoreo",
                "Clipping tradicional": "Monitoreo reactivo de volumen de menciones y sentimiento genérico.",
                "Ontología operacional de cruce": "Vinculación directa de entidades y compromisos internos con hechos externos verificados."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Documentos externos indexados por Signal AI", "denominator": "Volumen anual de procesamiento en feeds globales", "formula": "2.600 millones de documentos anuales"}
        ],
        "bridge_implications": [
            {"module": "Núcleo de Cruce Epistémico", "implication": "BRIDGE debe implementar una arquitectura ontológica que una afirmaciones internas con evidencias externas, descartando el clipping superficial.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F02
    {
        "question_id": "P06-F02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se aplica la Teoría de la Hipocresía y Desacoplamiento Organizacional (Brunsson, 1989; Meyer & Rowan) a la divergencia entre compromisos corporativos y conducta externa?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La Teoría del Desacoplamiento (Meyer & Rowan, 1977) y la Hipocresía Organizacional (Brunsson, 1989) postula que las empresas enfrentan demandas y presiones contradictorias de múltiples grupos de interés (accionistas que exigen retornos inmediatos, reguladores que exigen cumplimiento normativo, comunidades que exigen protección ambiental). Para sobrevivir a estas tensiones, las organizaciones generan frecuentemente un 'desacoplamiento' entre las declaraciones formales (talk), las decisiones gerenciales colegiadas (decisions) y la acción material operativa en terreno (action). Como establece P06_RESEARCH_DOSSIER, el sistema no debe cometer el error de atribuir automáticamente toda divergencia detectada a malicia, dolo o fraude deliberado (greenwashing intencional); en muchos casos, la divergencia surge de desajustes burocráticos, tiempos de implementación diferidos o asimetrías operacionales entre subsidiarias. El valor del cruce es iluminar estas brechas para que la dirección corporativa alinee la conducta operativa antes de que el entorno la penalice.",
        "findings": [
            {
                "claim_id": "P06-F02-C1",
                "claim": "El desacoplamiento organizacional entre retórica y acción es frecuentemente una respuesta a demandas institucionales en conflicto y no siempre dolo deliberado.",
                "epistemic_status": "teoria_academica_consolidada",
                "scope": {"time": "1977-2026", "region": "Global", "actor": "Organizaciones Complejas"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 1: Marco Teórico y Fundamentos Conceptuales",
                        "excerpt_short": "Las organizaciones operan bajo demandas institucionales contradictorias, lo que genera frecuentemente 'desacoplamiento' (decoupling) entre la retórica corporativa (hablar), las decisiones formales y la acción real operativa. El pilar P06 no debe asumir que toda divergencia proviene de malicia o fraude deliberado; muchas veces responde a desajustes burocráticos o tiempos de implementación diferidos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco sociológico e institucional canónico de Brunsson y Meyer & Rowan ratificado en las síntesis del pilar."
            }
        ],
        "operational_model": {
            "inputs": ["Metas declaradas en memorias", "Reportes de incidentes operativos o quejas en terreno"],
            "actors": ["Línea operativa", "Área de Sostenibilidad", "Comité de Dirección"],
            "steps": ["Detección de brecha entre compromiso formal y avance físico", "Evaluación de causas (inercia burocrática vs contingencia externa vs retraso presupuestario)", "Ajuste de narrativa o remediación de operaciones"],
            "states": ["Target_Declared", "Implementation_Lag_Detected", "Remediation_Triggered", "Aligned"],
            "outputs": ["Informe de consistencia interna-operativa", "Plan de remediación de brecha"],
            "exceptions": ["Ocultamiento deliberado de información por jefaturas operativas intermedias"]
        },
        "entities": [
            {"entity_id": "ENT_BRUNSSON", "type": "marco_teorico", "name": "Teoría de la Hipocresía Organizacional (Nils Brunsson)", "aliases": ["Brunsson Decoupling", "Talk-Action Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_BRUNSSON", "predicate": "explica_origen_de", "object_id": "ENT_DECOUPLING", "valid_from": "1989", "valid_to": "2026", "evidence_claim_id": "P06-F02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Interpretación de la divergencia",
                "Enfoque simplista": "Toda divergencia entre memoria y realidad es fraude/greenwashing.",
                "Enfoque de Brunsson": "La divergencia refleja frecuentemente tensiones institucionales y desfases de implementación que requieren sincronización."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Diagnóstico de Discrepancias", "implication": "BRIDGE debe tipificar el desacoplamiento distinguiendo entre retrasos de ejecución operacional y contradicciones fácticas insostenibles.", "status": "diseno_logica"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F03
    {
        "question_id": "P06-F03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo sustentan los Page Principles de la Arthur W. Page Society el principio de consistencia entre la conducta corporativa y la narrativa externa ('Tell the truth and prove it with action')?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los Page Principles de la Arthur W. Page Society establecen como regla suprema de la profesión corporativa: 1) 'Tell the truth' (decir la verdad sin ambigüedades calculadas ni omisiones dolosas) y 2) 'Prove it with action' (demostrarlo con hechos concretos), consagrando que el 90% de la reputación corporativa proviene de lo que la organización hace en sus operaciones diarias y solo el 10% de lo que comunica públicamente. En el contexto de P06, esta premisa impone que cualquier sistema de inteligencia artificial aplicado a asuntos corporativos debe funcionar prioritariamente como un sensor de consistencia operativa y un auditor de veracidad fáctica, y jamás como un generador de retórica evasiva o 'spin doctoring'. Si la conducta operativa de la empresa no respalda sus compromisos públicos, la comunicación masiva no solo fracasará en proteger la reputación, sino que agravará la crisis al evidenciar falsedad o cinismo institucional.",
        "findings": [
            {
                "claim_id": "P06-F03-C1",
                "claim": "Los Page Principles consagran que la reputación depende en un 90% de la acción operativa comprobable y solo un 10% de la comunicación declarada.",
                "epistemic_status": "estandar_profesional_global",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Chief Communication Officers (Arthur W. Page Society)"},
                "evidence": [
                    {
                        "source_id": "7cd9051b-dbba-48eb-878c-a17631e47d3d",
                        "source_title": "Arthur W. Page Society - The Page Principles",
                        "original_url": "https://page.org/who-we-are/page-principles/",
                        "locator": "Principle 1 & 2: Tell the Truth and Prove It with Action",
                        "excerpt_short": "Tell the truth: Let the public know what's even when the news is bad. Prove it with action: Public perception of an organization is determined 90 percent by what it does and 10 percent by what it says.",
                        "source_date": "2023-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "ea19c0ed-88be-4eff-8870-54c8217fa513",
                        "source_title": "IABC - Code of Ethics for Professional Communicators",
                        "original_url": "https://www.iabc.com/about/what-we-do/standards/code-of-ethics",
                        "locator": "Articles 1 & 2: Professional Communication and Truth",
                        "excerpt_short": "Professional communicators encourage open communication and practice honesty, accuracy, and clear communication to foster credibility and trust.",
                        "source_date": "2023-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Declaración expresa y literal de los estándares éticos mundiales de Page Society e IABC."
            }
        ],
        "operational_model": {
            "inputs": ["Borrador de comunicado corporativo", "Evidencia de desempeño operativo en base de datos interna"],
            "actors": ["Director de Asuntos Corporativos (CCO)", "Vocero Corporativo", "Agente BRIDGE"],
            "steps": ["Análisis de consistencia del borrador contra hechos operativos", "Evaluación de cumplimiento de 'Prove it with action'", "Rechazo o modificación si la afirmación carece de sustento en hechos"],
            "states": ["Draft_Statement", "Fact_Checked", "Action_Verified", "Approved_or_Flagged"],
            "outputs": ["Dictamen de veracidad y respaldo factual del comunicado"],
            "exceptions": ["Presión de gerencias comerciales para emitir declaraciones sin respaldo comprobado"]
        },
        "entities": [
            {"entity_id": "ENT_PAGE_SOCIETY", "type": "asociacion_profesional", "name": "Arthur W. Page Society", "aliases": ["Page Society", "Page Principles"]},
            {"entity_id": "ENT_IABC", "type": "asociacion_profesional", "name": "International Association of Business Communicators", "aliases": ["IABC"]}
        ],
        "relations": [
            {"subject_id": "ENT_PAGE_SOCIETY", "predicate": "define_principio_reputacional", "object_id": "ENT_PROVE_WITH_ACTION", "valid_from": "2023", "valid_to": "2026", "evidence_claim_id": "P06-F03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Peso en la reputación corporativa",
                "Acción operativa de la empresa": "90% de la percepción y confianza pública según los Page Principles.",
                "Comunicación y relaciones públicas": "10% de la percepción pública según los Page Principles."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Regla 90/10 de Arthur W. Page", "denominator": "Composición de la percepción pública", "formula": "90% Conducta Operativa + 10% Comunicación Declarada"}
        ],
        "bridge_implications": [
            {"module": "Compuertas de Abstención Estratégica (Módulo Actuar)", "implication": "BRIDGE debe prohibir la generación de comunicados defensivos o comerciales si el módulo de cruce detecta que los hechos operativos contradicen la declaración.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F04
    {
        "question_id": "P06-F04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué lecciones aportan plataformas líderes de inteligencia de riesgo externa como Signal AI, AlphaSense y Dataminr Pulse al diseño de un sistema de cruce corporativo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de las soluciones de mercado líderes (Signal AI, AlphaSense, Dataminr Pulse y Dow Jones Factiva) aporta tres lecciones arquitecturales críticas: 1) Estructuración ontológica previa: Signal AI procesa más de 2.600 millones de documentos anuales aplicando grafos de conocimiento para vincular noticias no a meras palabras clave, sino a entidades legales, directivos y tópicos de riesgo reputacional predefinidos (AIQ Engine); 2) Búsqueda federada y análisis semántico profundo: AlphaSense demuestra la necesidad de combinar motores de búsqueda sintáctica y vectorial sobre transcripciones de conferencias de resultados (earnings calls), memorias financieras y reportes de analistas, permitiendo contrastar afirmaciones de ejecutivos con el consenso del mercado; 3) Detección de anomalías en tiempo real y micro-señales: Dataminr Pulse evidencia que los primeros indicios de un incidente operacional o controversia socioambiental surgen como señales débiles multimodales (redes sociales locales, radiofrecuencias, reportes de primeros respondedores) antes de consolidarse en la prensa formal. No obstante, como advierte P06_QUALITY_ADDENDUM, estas suites comerciales exponen capacidades declaradas por fabricantes sin auditorías independientes de falsos positivos, por lo que su valor reside en sus patrones de diseño y no en garantías infalibles.",
        "findings": [
            {
                "claim_id": "P06-F04-C1",
                "claim": "Las plataformas líderes demuestran que la inteligencia de riesgo exige estructuración ontológica, búsqueda federada profunda y captura de micro-señales en tiempo real.",
                "epistemic_status": "estado_del_arte_tecnologico",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Proveedores Comerciales de Inteligencia"},
                "evidence": [
                    {
                        "source_id": "622d9c7c-2cdd-46f4-bd8d-10f8e8b26cee",
                        "source_title": "Signal AI - Risk Intelligence Platform & AIQ Engine",
                        "original_url": "https://signal-ai.com/products-services/risk-intelligence-platform",
                        "locator": "Platform Overview: AIQ Engine and Risk Signals",
                        "excerpt_short": "Signal AI structures external unstructured data into quantifiable risk metrics, mapping real-time signals against corporate entities, leadership reputations, and regulatory compliance frameworks.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "0103956c-7952-4ebc-bc74-db2a18cddc7c",
                        "source_title": "AlphaSense - Enterprise Intelligence Documentation",
                        "original_url": "https://developer.alpha-sense.com/enterprise",
                        "locator": "API & Enterprise Content Integration",
                        "excerpt_short": "Enables corporate users to search and analyze premium external content alongside internal research, extracting structured facts and sentiment from broker research, filings, and news.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "35ae6612-0e2a-4025-abc3-f8ec24c282e1",
                        "source_title": "Dataminr Pulse - Real-Time Event & Risk Intelligence Platform",
                        "original_url": "https://www.dataminr.com/products/pulse/financial-services-sector/",
                        "locator": "Real-Time Event Detection for Corporate Risk",
                        "excerpt_short": "Detects high-impact events and critical breaking information from public data signals, providing real-time alerts before traditional news outlets report them.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Evidencia directa de la documentación técnica y portales de producto de Signal AI, AlphaSense y Dataminr."
            }
        ],
        "operational_model": {
            "inputs": ["Feed estructurado de noticias globales", "Flujo de redes sociales y alertas tempranas", "Ontología corporativa de tópicos y ejecutivos"],
            "actors": ["Motores de procesamiento de lenguaje natural (NLP)", "Grafos de entidades", "Analistas de Inteligencia Corporativa"],
            "steps": ["Ingesta y desduplicación de feeds masivos", "Extracción de entidades y sentimiento", "Vínculo contra la ontología corporativa", "Disparo de alertas por umbrales de riesgo"],
            "states": ["Raw_Stream", "Extracted_Entities", "Mapped_to_Ontology", "Alert_Generated"],
            "outputs": ["Alertas de riesgo en tiempo real", "Métricas agregadas de exposición mediática"],
            "exceptions": ["Riesgo de falsos positivos por homonimia o ambigüedad geográfica"]
        },
        "entities": [
            {"entity_id": "ENT_SIGNAL_AI", "type": "plataforma_comercial", "name": "Signal AI Platform", "aliases": ["Signal AI", "AIQ Engine"]},
            {"entity_id": "ENT_ALPHASENSE", "type": "plataforma_comercial", "name": "AlphaSense", "aliases": ["AlphaSense Enterprise Intelligence"]},
            {"entity_id": "ENT_DATAMINR", "type": "plataforma_comercial", "name": "Dataminr Pulse", "aliases": ["Dataminr"]}
        ],
        "relations": [
            {"subject_id": "ENT_SIGNAL_AI", "predicate": "aplica_grafo_a", "object_id": "ENT_NEWS_STREAM", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de valor",
                "AlphaSense": "Búsqueda densa y federada en filings corporativos, earnings calls y reportes de analistas.",
                "Dataminr Pulse": "Detección ultra-temprana de eventos críticos en micro-señales y redes.",
                "Signal AI": "Estructuración de millones de noticias sobre ontologías de riesgo y reputación."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Sensor Multimodal de Entorno", "implication": "BRIDGE debe combinar búsqueda federada profunda en memorias y reportes oficiales con detección temprana de eventos en señales locales.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F05
    {
        "question_id": "P06-F05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo modela Palantir Foundry/AIP la creación de una ontología operacional centrada en decisiones para conectar datos internos y dinámicas externas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Palantir Foundry y su plataforma de inteligencia artificial (Palantir AIP) modelan la ontología operacional no como un esquema abstracto de almacenamiento de datos, sino como una representación digital viva del negocio centrada en las decisiones ('The Ontology represents the decisions in an enterprise, not simply the data'). En esta arquitectura, la ontología se compone de tres estratos: 1) Objetos semánticos (entidades del mundo real como 'Faena Minera', 'Línea de Crédito', 'Compromiso de Reducción de Emisiones', 'Sindicato'); 2) Relaciones lógicas y temporales que vinculan los objetos entre sí; y 3) Acciones operacionales y funciones de negocio (Action Types) que permiten tanto a operadores humanos como a agentes de IA interactuar con los sistemas corporativos subyacentes bajo estrictas políticas de gobernanza, seguridad y control de acceso. Al vincular los feeds de señales externas con estos objetos ontológicos, Palantir permite evaluar al instante qué compromisos internos o activos se ven impactados por una controversia externa y qué acciones remediadoras deben activarse.",
        "findings": [
            {
                "claim_id": "P06-F05-C1",
                "claim": "Palantir concibe la ontología operacional como un sistema centrado en decisiones que enlaza datos internos y señales externas a objetos de negocio y acciones concretas.",
                "epistemic_status": "patron_arquitectural_comercial",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Palantir Technologies"},
                "evidence": [
                    {
                        "source_id": "98f72019-62a8-4781-a211-2ce2cccaf4eb",
                        "source_title": "Palantir Foundry - Why Create an Ontology: Decision-Centric System",
                        "original_url": "https://palantir.com/docs/foundry/ontology/why-ontology/",
                        "locator": "Concept: The Decision-Centric Organization",
                        "excerpt_short": "The Ontology represents the decisions in an enterprise, not simply the data... connecting humans and agents directly to operations to face and overcome an organization's toughest challenges.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5168f7d7-3499-40e3-afc8-c6b216843f19",
                        "source_title": "Palantir AIP - Architecture Overview & Context Engineering",
                        "original_url": "https://palantir.com/docs/foundry/architecture-center/aip-architecture/",
                        "locator": "AIP Architecture: Context Engineering and Action Binding",
                        "excerpt_short": "Palantir AIP binds Large Language Models directly to the enterprise ontology, ensuring that AI reasoning operates over verified objects, relations, and secured business actions.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Documentación oficial de arquitectura de Palantir Foundry y AIP."
            }
        ],
        "operational_model": {
            "inputs": ["Datos maestros corporativos (ERP, CRM, memorias)", "Reglas de gobierno y roles ABAC", "Eventos externos indexados"],
            "actors": ["Administrador de Ontología", "Agentes AIP", "Comité de Operaciones"],
            "steps": ["Definición de Object Types y Link Types", "Mapeo de señales externas a objetos ontológicos", "Inferencia de impacto sobre compromisos", "Ejecución de Action Types autorizados"],
            "states": ["Raw_Sources", "Ontology_Mapped", "Impact_Assessed", "Action_Executed"],
            "outputs": ["Grafo ontológico enriquecido", "Trazabilidad de decisiones tomadas"],
            "exceptions": ["Intentos de acción de IA que violan los privilegios de seguridad ABAC"]
        },
        "entities": [
            {"entity_id": "ENT_PALANTIR_FOUNDRY", "type": "plataforma_comercial", "name": "Palantir Foundry Ontology", "aliases": ["Foundry", "Palantir Ontology"]},
            {"entity_id": "ENT_PALANTIR_AIP", "type": "plataforma_comercial", "name": "Palantir AIP", "aliases": ["AIP Core"]}
        ],
        "relations": [
            {"subject_id": "ENT_PALANTIR_AIP", "predicate": "ejecuta_razonamiento_sobre", "object_id": "ENT_PALANTIR_FOUNDRY", "valid_from": "2023", "valid_to": "2026", "evidence_claim_id": "P06-F05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de la ontología",
                "Ontología tradicional (W3C OWL/RDF)": "Modelo formal de clases y axiomas lógicos para inferencia académica.",
                "Ontología operacional (Palantir)": "Mapeo directo de objetos de negocio con enlace a acciones ejecutables y permisos de seguridad."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Ontología de Decisiones BRIDGE", "implication": "BRIDGE debe construir su grafo de conocimiento vinculando no solo textos, sino 'Objetos de Compromiso' corporativo con 'Acciones Recomendadas' de respuesta.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F06
    {
        "question_id": "P06-F06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo deben diferenciarse conceptualmente las señales de hechos comprobados de las meras acusaciones o narrativas hostiles no verificadas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El corpus exige una demarcación epistemológica taxativa entre: 1) Hechos comprobados (Verified Facts): Eventos respaldados por resoluciones administrativas formales (ej. formulación de cargos de la SMA en SNIFA, sanciones de la CMF), sentencias judiciales firmes, auditorías técnicas de terceros independientes (dictámenes ISAE 3000) o peritajes forenses con trazabilidad documental plena; y 2) Acusaciones no verificadas (Unsubstantiated Allegations) y narrativas hostiles: Afirmaciones difundidas en redes sociales, comunicados de activistas, columnas de opinión o filtraciones de prensa que carecen de expediente probatorio o corroboración oficial. Como establecen P06_EVIDENCE_MAP y el código ético de la IABC, tratar una imputación no verificada como si fuera un hecho objetivo induce a la organización a emitir respuestas prematuras, admitir responsabilidades inexistentes o provocar el temido efecto Streisand. El sistema debe clasificar tales señales como 'Acusación No Verificada' y activar protocolos de monitoreo silencioso y verificación interna, impidiendo declaraciones reactivas automáticas.",
        "findings": [
            {
                "claim_id": "P06-F06-C1",
                "claim": "Es imperativo distinguir epistemológicamente entre hechos comprobados por resoluciones oficiales y acusaciones no verificadas para evitar respuestas reactivas lesivas.",
                "epistemic_status": "principio_epistemico_y_etico",
                "scope": {"time": "2023-2026", "region": "Global / Chile", "actor": "Gobernanza de Comunicaciones"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Acusación No Verificada (Unsubstantiated Allegation / Narrative)",
                        "excerpt_short": "Señal externa originada en redes sociales, comunicados de ONG o filtraciones de prensa que carece de respaldo documental probatorio o resolución administrativa/judicial... Tratar una imputación no comprobada como hecho distorsiona la respuesta de asuntos corporativos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "ea19c0ed-88be-4eff-8870-54c8217fa513",
                        "source_title": "IABC - Code of Ethics for Professional Communicators",
                        "original_url": "https://www.iabc.com/about/what-we-do/standards/code-of-ethics",
                        "locator": "Article 1 & 3: Accuracy, Truth, and Credibility",
                        "excerpt_short": "IABC communicators adhere to principles of accuracy, verifying facts before dissemination and refusing to disseminate false or misleading information or unverified rumors.",
                        "source_date": "2023-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio epistemológico y ético central de la gestión corporativa y de crisis."
            }
        ],
        "operational_model": {
            "inputs": ["Publicación en redes sociales", "Comunicado de ONG", "Base de datos SNIFA de la SMA", "Poder Judicial de Chile"],
            "actors": ["Analista de Monitoreo", "Asesor Legal Corporativo", "Clasificador Epistémico de BRIDGE"],
            "steps": ["Verificación de fuente y trazabilidad documental", "Cruce contra registros públicos y regulatorios", "Asignación de etiqueta 'Hecho Verificado' vs 'Acusación No Verificada'", "Recomendación de acción (Aclaración vs Monitoreo silencioso)"],
            "states": ["Raw_Signal", "Evidence_Checked", "Classified_Allegation_vs_Fact", "Policy_Triggered"],
            "outputs": ["Clasificación de tipología de señal", "Guía de conducta estratégica"],
            "exceptions": ["Acusaciones no verificadas que se viralizan masivamente forzando intervención pública"]
        },
        "entities": [
            {"entity_id": "ENT_SMA_SNIFA", "type": "organismo_regulador", "name": "Superintendencia del Medio Ambiente (SNIFA)", "aliases": ["SMA Chile", "SNIFA"]},
            {"entity_id": "ENT_IABC", "type": "asociacion_profesional", "name": "International Association of Business Communicators", "aliases": ["IABC"]}
        ],
        "relations": [
            {"subject_id": "ENT_SMA_SNIFA", "predicate": "emite_resoluciones_de_tipo", "object_id": "ENT_HECHO_VERIFICADO", "valid_from": "2020", "valid_to": "2026", "evidence_claim_id": "P06-F06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de la señal",
                "Hecho comprobado": "Resolución sancionatoria ejecutoriada, peritaje técnico o sentencia judicial firme.",
                "Acusación no verificada": "Denuncia en redes o rumor sin sustento probatorio ni resolución oficial."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Filtro de Ruido y Clasificación Epistémica", "implication": "BRIDGE debe etiquetar automáticamente las señales de redes como 'Acusación No Verificada' hasta que exista corroboración administrativa o documental probatoria.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F07"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-F01..F06) to {out_path}.")
