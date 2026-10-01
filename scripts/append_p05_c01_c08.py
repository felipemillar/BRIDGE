import json
from pathlib import Path

NOTEBOOK_ID = "0fc2e780-e279-4923-83c5-90fe621a4543"
SNAPSHOT_AT = "2026-10-01T03:00:00-03:00"

records = [
    # P05-C01
    {
        "question_id": "P05-C01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre identidad, imagen y reputación, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia central identificada entre la práctica comercial tradicional y la literatura científica rigurosa radica en la equiparación errónea entre imagen de corto plazo y reputación acumulada. Ciertas fuentes comerciales y agencias de relaciones públicas promueven que una ráfaga de menciones favorables o una campaña publicitaria de imagen en redes sociales equivale a construir reputación corporativa. En contraste, las fuentes canónicas académicas (Fombrun & Shanley 1990; Fombrun & van Riel 1997; Deephouse 2000; Page Society 2023) y las síntesis internas canónicas (P05_EVIDENCE_MAP Eje 1 y P05_RESEARCH_DOSSIER Sección 1.1) demuestran que la imagen es efímera, superficial y altamente volátil ante cualquier estímulo de coyuntura, mientras que la reputación es un juicio evaluativo colectivo, agregado y sostenido en el tiempo que actúa como reserva de capital moral en mercados con asimetría de información. De acuerdo con las reglas de precedencia editorial del mandato, prevalece de forma absoluta la versión rigurosa de P05_EVIDENCE_MAP y Fombrun: la plataforma BRIDGE debe tratar la identidad como atributo intrínseco documentado, la imagen como señal de coyuntura y la reputación como activo estructural duradero.",
        "findings": [
            {
                "claim_id": "P05-C01-C1",
                "claim": "Prevalece la distinción canónica que rechaza la equivalencia entre imagen de redes sociales y reputación estructural acumulada, conforme a la regla de precedencia editorial de P05.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1990-2026", "region": "Global", "actor": "Curaduría Epistémica P05"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Matriz de Tensiones Epistemológicas, Tensión 2",
                        "excerpt_short": "Separar analíticamente Sentimiento de Reputación. Tratar el sentimiento como señal de alerta temprana (out-take) y la reputación como activo acumulado (outcome/impact).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "19dae3b0-2400-447a-a840-0cf2c0ec5fd1",
                        "source_title": "Fombrun & van Riel: The Reputational Landscape (Corporate Reputation Review)",
                        "original_url": "https://link.springer.com/article/10.1057/crr.1997.1",
                        "locator": "Corporate Reputation Review, 1(1), pp. 5-13",
                        "excerpt_short": "Image is what is perceived immediately; reputation is the historical accumulation of images and experiences over time.",
                        "source_date": "1997-04-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución explícita de tensión epistemológica consagrada en la síntesis interna rectora de P05."
            }
        ],
        "operational_model": {
            "inputs": ["Monitoreo de imagen coyuntural", "Series históricas de reputación"],
            "actors": ["Comité Editorial", "Arquitecto de BRIDGE"],
            "steps": ["Detección de afirmaciones comerciales que confunden imagen con reputación", "Aplicación de la regla de precedencia editorial", "Configuración de algoritmos desacoplados"],
            "states": ["Discrepancy_Identified", "Precedence_Applied", "Standard_Enforced"],
            "outputs": ["Arquitectura analítica conforme a la regla rectora de P05"],
            "exceptions": ["Campañas publicitarias que pretenden adjudicarse incrementos estructurales de reputación"]
        },
        "entities": [
            {"entity_id": "ENT_PRECEDENCE_P05", "type": "regla_editorial", "name": "Regla de Precedencia Editorial P05", "aliases": ["P05 Editorial Precedence"]}
        ],
        "relations": [
            {"subject_id": "ENT_PRECEDENCE_P05", "predicate": "resuelve_discrepancia_de", "object_id": "ENT_REPUTATION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resolución de discrepancia",
                "Versión Comercial Desestimada": "Campañas de imagen equivalen a construir reputación.",
                "Versión Canónica Prevaleciente": "La reputación requiere conducta fáctica verificada sostenida en el tiempo y no se altera por meras campañas de relaciones públicas."
            }
        ],
        "contradictions": [
            {"issue": "Equiparación de imagen y reputación", "source_a": "Agencias de marketing digital", "source_b": "P05_EVIDENCE_MAP / Fombrun & Shanley", "resolution": "Prevalece P05_EVIDENCE_MAP: la reputación es un constructo evaluativo longitudinal no reducible a imagen inmediata."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor Analítico", "implication": "BRIDGE debe rechazar interfaces que colapsen el monitoreo de redes sociales con la evaluación estructural de reputación.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C02
    {
        "question_id": "P05-C02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre identidad, imagen y reputación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de gaps documentado en P05_GAPS_AND_VALIDATION Sección 1 revela lo siguiente: 1) Lo que sigue sin prueba rigurosa: La relación de causalidad estricta y cuantificable entre una mejora en la reputación corporativa y el incremento del desempeño financiero o bursátil de una empresa. Aunque existe correlación econométrica positiva comprobada (Deephouse 2000; Fombrun & Shanley 1990), la literatura científica no ha logrado resolver si una mayor reputación genera mayores utilidades, o si las corporaciones más rentables cuentan con mayores recursos para comunicar su identidad y blindar su reputación; 2) Qué fuente falló o es parcial: Fallan los estudios comerciales que prometen 'fórmulas de ROI directo de relaciones públicas', ya que omiten factores macroeconómicos, dinámicas de mercado y estacionalidad; asimismo, la fuente OECD Due Diligence Guidance falló en su ingesta automática en el cuaderno y debió sustituirse por estándares homólogos (AA1000SES y NCG 461); 3) Validación mínima que resolvería la incertidumbre: Aplicar diseños de investigación cuasi-experimentales en empresas con múltiples unidades de negocio comparables o adoptar el estándar AMEC Framework, midiendo la reputación no como generador de ventas directas sino como reductor de costos de fricción institucional (disminución de multas, celeridad en obtención de licencias ambientales y retención de talento clave).",
        "findings": [
            {
                "claim_id": "P05-C02-C1",
                "claim": "La atribución causal directa de la reputación sobre el retorno financiero permanece como un vacío empírico que exige reenfocar la medición hacia la reducción de costos de fricción institucional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Investigación Empírica P05"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1: La Caja Negra de la Atribución Causal en Reputación Corporativa",
                        "excerpt_short": "Casi ningún estudio logra aislar la causalidad estricta entre comunicación y desempeño financiero. La plataforma debe enfocarse en mitigación de riesgos y reducción de fricción.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico formalmente identificado y respaldado en la literatura científica de economía y gestión."
            }
        ],
        "operational_model": {
            "inputs": ["Literatura sobre ROI en relaciones públicas", "Estudios econométricos de panel"],
            "actors": ["Investigador de Métricas", "Auditor Metodológico"],
            "steps": ["Revisión sistemática de literatura de causalidad", "Identificación de variables de confusión", "Formulación de protocolo cuasi-experimental"],
            "states": ["Literature_Reviewed", "Causality_Gap_Mapped", "Validation_Protocol_Defined"],
            "outputs": ["Definición de protocolo de validación mínima para reducción de fricción"],
            "exceptions": ["Afirmaciones infundadas de consultoras que aseguran poder medir el ROI exacto de un comunicado"]
        },
        "entities": [
            {"entity_id": "ENT_CAUSALITY_GAP", "type": "vacio_metodologico", "name": "Brecha de Atribución Causal en Reputación", "aliases": ["Reputation ROI Causality Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_CAUSALITY_GAP", "predicate": "limita_inferencia_de", "object_id": "ENT_REPUTATION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de valor financiero",
                "Promesa Comercial Inválida": "'Nuestra estrategia de reputación aumentó las ventas de la compañía en un 12%'.",
                "Enfoque Basado en Evidencia": "'La estrategia de relacionamiento redujo los recursos contenciosos en el SEIA a cero, ahorrando 18 meses de paralización de obras'."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Reporte de Valor", "implication": "BRIDGE debe medir el valor de los asuntos corporativos a través de indicadores de evitación de costos de litigación, celeridad en permisos y estabilidad de la licencia social.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_REP_CAUSALITY", "description": "Falta de aislamiento econométrico estricto entre comunicación y valor bursátil directo.", "severity": "alta", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C03
    {
        "question_id": "P05-C03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre modelos de medición y calidad, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia metodológica radica en la pugna entre los modelos que persiguen un 'Score Único Global' de la firma (estilo Net Promoter Score - NPS agregado o índice Pulse colapsado) y los modelos multidimensionales y multistakeholder respaldados por la evidencia científica. Fuentes comerciales promueven el uso de un solo número para facilitar comparaciones en rankings públicos. En contraste, las síntesis internas canónicas (P05_EVIDENCE_MAP Tensión 4 y P05_RESEARCH_DOSSIER Sección 2) y la literatura de stakeholders (Freeman 1984; Mitchell et al. 1997; Boutilier & Thomson 2011) dictaminan que una corporación no posee una sola reputación, sino múltiples reputaciones sectoriales que divergen según el grupo evaluador: una empresa puede ostentar una reputación sobresaliente entre inversionistas institucionales por su rentabilidad financiera, pero simultáneamente sufrir una reputación crítica en comunidades territoriales por contaminación o falta de diálogo. De acuerdo con las correcciones del mandato, prevalece la versión de P05_EVIDENCE_MAP: la plataforma BRIDGE debe prohibir la reducción forzada a un índice único y debe representar la reputación de forma desagregada por stakeholder y por driver analítico.",
        "findings": [
            {
                "claim_id": "P05-C03-C1",
                "claim": "Prevalece el principio de desagregación multidimensional de la reputación por grupos de interés, proscribiendo el colapso en un índice único que invisibilice riesgos asimétricos críticos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Diseño Metodológico BRIDGE"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Matriz de Tensiones Epistemológicas, Tensión 4",
                        "excerpt_short": "Una firma tiene tantas reputaciones como grupos de interés con los que interactúa. Desagregar por stakeholder. La plataforma debe permitir visualizar la reputación segmentada.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución normativa expresa en el mapa de evidencias de P05."
            }
        ],
        "operational_model": {
            "inputs": ["Datos de encuestas generales", "Evaluaciones por panel segmentado"],
            "actors": ["Metodólogo de BRIDGE", "Comité de Riesgos"],
            "steps": ["Verificación de la estructura de reporte de los modelos", "Desagregación de índices en vectores por stakeholder", "Construcción de gráficos radiales de reputación segmentada"],
            "states": ["Aggregated_Data_Parsed", "Disaggregation_Rules_Applied", "Segmented_Profile_Generated"],
            "outputs": ["Perfil de reputación multidimensional no colapsado"],
            "exceptions": ["Exigencia de clientes de disponer de un único número para bonos ejecutivos, que debe acompañarse de advertencia de riesgo"]
        },
        "entities": [
            {"entity_id": "ENT_DISAGGREGATION_RULE", "type": "regla_metodologica", "name": "Regla de Desagregación Multistakeholder", "aliases": ["Multidimensional Stakeholder Rule"]}
        ],
        "relations": [
            {"subject_id": "ENT_DISAGGREGATION_RULE", "predicate": "gobierna_visualizacion_de", "object_id": "ENT_REPUTATION", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P05-C03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de reporte",
                "Score Único Comercial": "Puntaje 72/100 (oculta que en comunidades locales la calificación es 20/100).",
                "Reporte Desagregado BRIDGE": "Inversionistas: 85/100; Empleados: 78/100; Reguladores: 70/100; Comunidades Locales: 20/100 (Alerta Crítica)."
            }
        ],
        "contradictions": [
            {"issue": "Puntaje único vs reputaciones múltiples", "source_a": "Rankings comerciales de score sintético", "source_b": "P05_EVIDENCE_MAP / Freeman / Mitchell", "resolution": "Prevalece P05_EVIDENCE_MAP: la reputación es inherentemente plural y debe desagregarse por grupo de interés."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Dashboard de Métricas", "implication": "BRIDGE debe estructurar sus tableros permitiendo filtrar la reputación según el tipo de público consultado, evitando un promedio aritmético ciego.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C04
    {
        "question_id": "P05-C04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre modelos de medición y calidad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El diagnóstico de limitaciones metodológicas documentado en P05_GAPS_AND_VALIDATION Sección 1 y 2 establece: 1) Lo que sigue sin prueba: La capacidad real de las plataformas de telemetría en tiempo real basadas en paneles digitales (como Group Caliber) para capturar las posturas de actores clave no digitalizados en territorios rurales de América Latina y Chile (comunidades indígenas, pescadores artesanales, pirquineros o agricultores de subsistencia). Estos actores no participan en paneles web comerciales, por lo que sus percepciones permanecen invisibles en la analítica continua; 2) Qué fuente es parcial o falló: Fallan las herramientas de social listening y paneles online masivos, que sufren de sesgo urbano y digital severo; Merco es parcial porque su panel inicial elitista de directivos (> US$ 30M) tiende a sobre-representar a conglomerados tradicionales; 3) Validación mínima para resolver la incertidumbre: Implementar un modelo de 'Doble Velocidad' que combine la telemetría algorítmica continua de medios y redes con la ingesta estructurada de fuentes no digitales: actas de participación ciudadana temprana del SEA, transcripciones de asambleas territoriales, audios de radios comunitarias locales y registros de diálogo bajo estándar AA1000SES.",
        "findings": [
            {
                "claim_id": "P05-C04-C1",
                "claim": "Los paneles de opinión digital presentan un punto ciego territorial en comunidades rurales, exigiendo protocolos híbridos que integren fuentes presenciales e institucionales del SEIA.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Monitoreo de Licencia Social"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1: Sub-representación y Sesgo Tecnológico en la Captura de Señales Territoriales",
                        "excerpt_short": "Los actores comunitarios raramente canalizan sus demandas en redes sociales masivas. Si la plataforma solo rastrea medios masivos y redes principales, sufrirá ceguera territorial respecto de la SLO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Limitación empírica demostrada en la gestión de proyectos de infraestructura en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Paneles de escucha digital", "Actas del SEIA", "Informes de relacionamiento comunitario presencial"],
            "actors": ["Analista Territorial", "Ingeniero de Datos"],
            "steps": ["Detección de zonas de baja cobertura digital", "Carga manual o asistida de actas de asambleas comunitarias", "Ponderación del indicador de Licencia Social territorial"],
            "states": ["Digital_Signals_Loaded", "Territorial_Gap_Flagged", "Hybrid_Model_Computed"],
            "outputs": ["Índice de Licencia Social para Operar calibrado territorialmente"],
            "exceptions": ["Falta de personal en terreno para registrar actas de reuniones comunitarias"]
        },
        "entities": [
            {"entity_id": "ENT_TERRITORIAL_GAP", "type": "vacio_metodologico", "name": "Punto Ciego Territorial Digital", "aliases": ["Territorial Offline Blindspot"]}
        ],
        "relations": [
            {"subject_id": "ENT_TERRITORIAL_GAP", "predicate": "afecta_representatividad_de", "object_id": "ENT_CALIBER", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P05-C04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Representatividad de la muestra",
                "Panel Digital Masivo": "Muestra urbana de Santiago con acceso a internet de alta velocidad.",
                "Realidad Territorial de Faena": "Comunidad rural colindante al relave minero que delibera en la sede social comunal."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Pipeline de Ingesta Territorial", "implication": "BRIDGE debe permitir la ingesta y vectorización de expedientes PDF del SEIA y minutas de terreno para cerrar la brecha de las comunidades no digitalizadas.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_OFFLINE_COMMUNITIES", "description": "Sub-representación sistemática de comunidades territoriales rurales en paneles de opinión online.", "severity": "alta", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C05
    {
        "question_id": "P05-C05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre niveles de métricas de comunicación, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia más severa en este eje radica en la persistencia del Valor Publicitario Equivalente (AVE / VPE) en reportes de agencias de relaciones públicas tradicionales frente al consenso científico global. Agencias comerciales siguen comercializando el AVE asignando el costo de una tarifa publicitaria al espacio editorial obtenido en prensa, vendiéndolo a clientes corporativos como 'retorno de inversión de comunicaciones'. En contraste, los Principios de Barcelona 3.0 de AMEC (Principio 5: 'AVEs are not the value of communication') y las síntesis canónicas de P05 (P05_EVIDENCE_MAP Eje 2, Hallazgo 2.2 y P05_RESEARCH_DOSSIER Sección 3) dictaminan que el AVE carece de validez científica, confunde costo publicitario con valor de las relaciones públicas y no mide comprensión, cambio de actitud ni impacto en el negocio. De acuerdo con las correcciones del mandato, prevalece de forma categórica y definitiva el estándar AMEC: el AVE queda proscrito de la arquitectura analítica de BRIDGE, debiendo medirse la efectividad comunicacional exclusivamente a través de la cadena causal de Outputs, Out-takes, Outcomes e Impacto Organizacional.",
        "findings": [
            {
                "claim_id": "P05-C05-C1",
                "claim": "Prevalece la proscripción definitiva del AVE dictaminada por los Principios de Barcelona 3.0 de AMEC, exigiendo la adopción exclusiva de la cadena causal de resultados organizacionales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Global", "actor": "Estándar Global AMEC"},
                "evidence": [
                    {
                        "source_id": "c8249017-0397-4799-aacc-c1c53ee4662d",
                        "source_title": "AMEC: Barcelona Principles 3.0 (Global Standard for PR & Comms Measurement)",
                        "original_url": "https://amecorg.com/barcelona-principles-3-0-translations/",
                        "locator": "Principio 5: AVEs are not the value of communication",
                        "excerpt_short": "Advertising Value Equivalents (AVEs) do not measure the value of communications. AMEC reconfirms that AVEs should not be used in any measurement program.",
                        "source_date": "2020-07-08",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Matriz de Tensiones Epistemológicas, Tensión 1",
                        "excerpt_short": "Adoptar AMEC IEF de forma exclusiva. La aplicación debe prohibir el AVE y medir outputs, out-takes, outcomes y valor de negocio. Nivel de confianza DEFINITIVO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Consenso internacional unánime consagrado en los estándares profesionales de AMEC."
            }
        ],
        "operational_model": {
            "inputs": ["Reportes de clippings con tarifas publicitarias", "Directrices AMEC"],
            "actors": ["Comité Metodológico", "Auditor de Comunicaciones"],
            "steps": ["Detección de métricas no conformes tipo AVE en archivos de agencias", "Eliminación automática de campos AVE en el pipeline de datos", "Sustitución por métricas de out-takes y outcomes"],
            "states": ["Clips_Scanned", "AVE_Detected_and_Purged", "AMEC_Tiers_Enforced"],
            "outputs": ["Reporte conforme a Principios de Barcelona 3.0"],
            "exceptions": ["Agencias proveedoras que se nieguen a reportar outcomes, requiriendo revisión de contrato"]
        },
        "entities": [
            {"entity_id": "ENT_AVE_BAN", "type": "regla_exclusiva", "name": "Proscripción Definitiva del AVE", "aliases": ["AMEC AVE Ban"]}
        ],
        "relations": [
            {"subject_id": "ENT_AVE_BAN", "predicate": "elimina_metrica_de", "object_id": "ENT_AMEC_TAXONOMY", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P05-C05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Validez epistemológica",
                "Valor Publicitario Equivalente (AVE)": "Cálculo ficticio que inventa un supuesto ahorro publicitario en textos periodísticos.",
                "Marco AMEC IEF": "Evaluación científica rigurosa que demuestra cambios en la confianza y reducción de multas regulatorias."
            }
        ],
        "contradictions": [
            {"issue": "Uso de AVE como métrica de PR", "source_a": "Agencias tradicionales de relaciones públicas", "source_b": "AMEC Barcelona Principles 3.0 / P05_EVIDENCE_MAP", "resolution": "Prevalece AMEC: el AVE está formal y definitivamente proscrito por carecer de rigor científico."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gestor de KPIs", "implication": "BRIDGE debe excluir de su modelo relacional el campo AVE, impidiendo que los usuarios generen gráficos basados en equivalencias publicitarias.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C06
    {
        "question_id": "P05-C06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre niveles de métricas de comunicación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de brechas de medición de comunicaciones documentado en P05_GAPS_AND_VALIDATION establece: 1) Lo que sigue sin prueba rigurosa: La precisión de los algoritmos de análisis de sentimiento automatizado mediante modelos de lenguaje genéricos cuando se aplican a textos informales cargados de ironía, sarcasmo o giros idiomáticos locales chilenos (chilenismos). La tasa de error en la asignación de polaridad en español coloquial oscila entre el 20% y el 35%, produciendo falsos positivos de hostilidad o ignorando descalificaciones sutiles muy dañinas; 2) Qué fuente falló o es parcial: Fallan los clasificadores comerciales de sentimiento estándar incluidos en plataformas como Brandwatch y Meltwater al no estar calibrados lingüísticamente para las particularidades dialectales de Chile y América Latina; 3) Validación mínima que resolvería la incertidumbre: Incorporar modelos de lenguaje pre-entrenados y afinados territorialmente en español chileno (como BETO o modelos fine-tuneados con prensa y foros locales), contrastados periódicamente con una muestra ciega del 10%+ de menciones críticas auditada por lingüistas y sociólogos humanos con cálculo formal del coeficiente Kappa de concordancia inter-evaluador.",
        "findings": [
            {
                "claim_id": "P05-C06-C1",
                "claim": "El análisis automatizado de sentimiento en español local mantiene una tasa de error relevante ante el sarcasmo y la ironía, exigiendo modelos afinados territorialmente y auditorías humanas continuas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Chile / América Latina", "actor": "Tecnología NLP y Analítica"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2: Análisis de Sentimiento Automatizado (NLP/LLMs)",
                        "excerpt_short": "Sesgo léxico y de contexto cultural; incapacidad de procesar ironía, sarcasmo o modismos locales chilenos. Mecanismo de atenuación: modelos afinados territorialmente y análisis cualitativo humano.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Limitación ampliamente documentada en la literatura de procesamiento de lenguaje natural en español."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus de menciones en español chileno", "Modelos BETO fine-tuneados", "Muestra de control humano"],
            "actors": ["Ingeniero de NLP", "Auditor Lingüístico"],
            "steps": ["Clasificación automática con modelo afinado", "Extracción de muestra estratificada del 10%", "Revisión humana y cálculo de matriz de confusión"],
            "states": ["Raw_Text_Classified", "Sample_Audited", "Kappa_Calculated"],
            "outputs": ["Métricas de precisión y calibración del clasificador de sentimiento"],
            "exceptions": ["Uso de modelos en inglés con traducción automática previa que altere el sentido coloquial"]
        },
        "entities": [
            {"entity_id": "ENT_NLP_CULTURAL_GAP", "type": "vacio_metodologico", "name": "Sesgo Cultural en Análisis de Sentimiento", "aliases": ["Local Dialect Sentiment Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_NLP_CULTURAL_GAP", "predicate": "limita_efectividad_de", "object_id": "ENT_AMEC_TAXONOMY", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P05-C06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de procesamiento",
                "NLP Estándar Global": "Clasifica 'la raja' o 'harto penca' con diccionarios genéricos generando errores groseros.",
                "Modelo Afinado Territorial (BETO Chile)": "Reconoce el significado pragmático exacto de modismos y sarcasmos chilenos en el contexto de la noticia."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Clasificador Semántico Local", "implication": "BRIDGE debe utilizar modelos adaptados al español de Chile y mostrar una advertencia de confiabilidad en menciones que presenten indicios de ironía.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_SENTIMENT_DIALECT", "description": "Tasa de error de NLP genérico ante modismos locales y sarcasmo en español latinoamericano.", "severity": "media", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C07"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C07
    {
        "question_id": "P05-C07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre narrativas y temas emergentes, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia central radica en la concepción del origen y evolución de las narrativas corporativas. Enfoques reactivos tradicionales sostienen que las crisis y narrativas hostiles son eventos fortuitos, caóticos e impredecibles que estallan de forma súbita ('cisnes negros') y que deben gestionarse únicamente con control de daños cuando ya copan las portadas de la prensa. En contraste, las síntesis canónicas (P05_RESEARCH_DOSSIER Sección 4.1 y P05_EVIDENCE_MAP Eje 3) y la literatura de gestión estratégica de temas (Entman 1993; Shiller 2017; MDPI 2026) demuestran que las narrativas corporativas siguen una dinámica evolutiva estructurada: transitan por fases predecibles (Señales Débiles -> Emergente -> Mainstream -> Cristalización Regulatoria) y su viralización obedece a modelos de contagio epidemiológico SIR gobernados por arquetipos morales y funciones de encuadre (Framing). De acuerdo con las correcciones del mandato, prevalece la versión científica de P05: las controversias no son eventos fortuitos sino procesos que pueden detectarse en fase de señal débil, permitiendo intervenir tempranamente antes de que adquieran fuerza regulatoria o judicial irreversible.",
        "findings": [
            {
                "claim_id": "P05-C07-C1",
                "claim": "Prevalece la concepción evolutiva y predecible del ciclo de vida de temas y encuadres de Entman frente a la creencia reactiva de que las crisis narrativas son eventos caóticos impredecibles.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1993-2026", "region": "Global", "actor": "Gestión Estratégica de Temas"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 1: Eje 3, Hallazgo 3.3 (Ciclo de Vida de los Temas Emergentes)",
                        "excerpt_short": "Los temas corporativos evolucionan a través de fases predictibles desde señales débiles hasta cristalización regulatoria e institucionalización. Nivel de confianza ALTO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco teórico consolidado respaldado por la teoría del framing y economía narrativa."
            }
        ],
        "operational_model": {
            "inputs": ["Monitoreo de señales tempranas", "Registros legislativos y mediáticos"],
            "actors": ["Analista de Temas Emergentes", "Director de Asuntos Públicos"],
            "steps": ["Mapeo del tema en la curva del ciclo de vida", "Detección de aceleración de contagio SIR", "Diseño de intervención preventiva"],
            "states": ["Signal_Tracked", "Stage_Diagnosed", "Preventive_Strategy_Executed"],
            "outputs": ["Plan de Gestión Proactiva de Asuntos Críticos"],
            "exceptions": ["Desastres naturales o accidentes de fuerza mayor no precedidos por incubación"]
        },
        "entities": [
            {"entity_id": "ENT_PREDICTABLE_LIFECYCLE", "type": "principio_teorico", "name": "Principio de Predictibilidad del Ciclo de Vida de Temas", "aliases": ["Issue Life Cycle Predictability"]}
        ],
        "relations": [
            {"subject_id": "ENT_PREDICTABLE_LIFECYCLE", "predicate": "reemplaza_modelo_reactivo_de", "object_id": "ENT_NARRATIVE_SCHEMA", "valid_from": "1993", "valid_to": None, "evidence_claim_id": "P05-C07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de gestión de temas",
                "Paradigma Reactivo Tradicional": "Esperar a que el tema esté en la portada del diario para llamar a una agencia de gestión de crisis.",
                "Paradigma Predictivo BRIDGE": "Detectar la señal débil en el SEIA o foros locales y resolver operativamente la causa 12 meses antes del salto mediático."
            }
        ],
        "contradictions": [
            {"issue": "Predecibilidad de las controversias", "source_a": "Práctica corporativa tradicional reactiva", "source_b": "P05_RESEARCH_DOSSIER / Entman / Shiller", "resolution": "Prevalece P05: los temas siguen un ciclo de vida reconocible que admite detección y gestión preventiva."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Rastreador de Ciclo de Vida", "implication": "BRIDGE debe alertar visualmente cuando un tema transite de Señal Débil a Emergente para activar planes de mitigación temprana.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C08
    {
        "question_id": "P05-C08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre narrativas y temas emergentes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de gaps documentado en P05_GAPS_AND_VALIDATION Sección 1 y 3 establece: 1) Lo que sigue sin prueba formal: La estandarización matemática universal de los parámetros del modelo epidemiológico SIR de Shiller (tasa de contagio beta, tasa de recuperación gamma y número de reproducción básica R0) aplicados a las narrativas corporativas. No existen benchmarks normalizados que definan el valor umbral exacto en que una historia pasará indefectiblemente de un foro especializado a forzar la intervención de una comisión parlamentaria; 2) Qué fuente es parcial o falló: Fallan las plataformas de analítica digital comercial (Signal AI, Meltwater) al proveer indicadores propietarios cerrados de 'virulencia' o 'impacto' sin transparentar las fórmulas matemáticas ni permitir la calibración con variables institucionales del marco chileno; 3) Validación mínima que resolvería la incertidumbre: Conducir un estudio de validación retrospectiva (backtesting) sobre un corpus histórico de 50 casos de controversias socioambientales y de libre competencia en Chile en los últimos 10 años, midiendo la correlación entre la velocidad de propagación intercanal y la posterior presentación de mociones legislativas o formulación de cargos de superintendencias, calibrando umbrales empíricos de R0 específicos para el entorno institucional local.",
        "findings": [
            {
                "claim_id": "P05-C08-C1",
                "claim": "La cuantificación matemática precisa de la tasa de contagio narrativo R0 en asuntos públicos carece de benchmarks estandarizados, requiriendo validación mediante backtesting en series históricas locales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Modelación de Economía Narrativa"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1: Falta de Benchmarks Estandarizados de Resonancia Narrativa",
                        "excerpt_short": "No existen unidades de medida consensuadas para cuantificar la virulencia o mutación de un frame. Pregunta abierta: variables matemáticas mínimas para el Índice de Riesgo de Contagio Narrativo.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío científico formalmente documentado en el dossier de gaps de P05."
            }
        ],
        "operational_model": {
            "inputs": ["Series históricas de cobertura de controversias", "Fechas de hitos parlamentarios y regulatorios"],
            "actors": ["Científico de Datos", "Modelador Econométrico"],
            "steps": ["Ajuste de curvas de difusión SIR sobre casos históricos", "Cálculo de parámetros beta y gamma para el ecosistema chileno", "Definición de rangos de alerta de R0"],
            "states": ["Historical_Data_Fitted", "Parameters_Calibrated", "Empirical_Thresholds_Set"],
            "outputs": ["Módulo de Alerta Temprana de R0 Narrativo calibrado"],
            "exceptions": ["Controversias impulsadas artificialmente por granjas de bots con decaimiento instantáneo"]
        },
        "entities": [
            {"entity_id": "ENT_R0_STANDARDIZATION_GAP", "type": "vacio_metodologico", "name": "Brecha de Calibración Matemática de R0 Narrativo", "aliases": ["Narrative R0 Benchmark Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_R0_STANDARDIZATION_GAP", "predicate": "limita_cuantificacion_de", "object_id": "ENT_SHILLER_SIR", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de modelado de virulencia",
                "Herramientas Comerciales": "Puntaje opaco de 'Engagement Score' sin fundamento epidemiológico.",
                "Modelo Calibrado BRIDGE": "Cálculo de R0 basado en la velocidad de salto entre canales periféricos y medios regulados con umbral empírico auditado."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Calculador de R0", "implication": "BRIDGE debe acompañar todo indicador de virulencia narrativa con la indicación de que se trata de una estimación epidemiológica modelada y no de una certeza determinista.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_R0_BENCHMARK", "description": "Ausencia de estándares cuantitativos universales para calibrar la tasa de reproducción R0 en narrativas corporativas.", "severity": "media", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P05.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P05-C01..C08) to {out_path}.")
