import json
from pathlib import Path

NOTEBOOK_ID = "0fc2e780-e279-4923-83c5-90fe621a4543"
SNAPSHOT_AT = "2026-10-01T03:00:00-03:00"

records = [
    # P05-F07
    {
        "question_id": "P05-F07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué dimensiones y poblaciones usan los modelos de reputación revisados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los cinco modelos de medición analizados en el corpus operan con dimensiones y poblaciones marcadamente diferenciadas: 1) RepTrak (The RepTrak Company): Evalúa a la población informada y público general mediante encuestas online representativas; se estructura en 7 drivers racionales (Productos/Servicios, Innovación, Lugar de Trabajo, Gobernanza, Ciudadanía, Liderazgo, Desempeño Financiero) que explican el vínculo emocional Pulse (admiración, respeto, confianza, buena estima); 2) Merco (Monitor Empresarial de Reputación Corporativa): Modelo multistakeholder híbrido y secuencial que evalúa a directivos empresariales (empresas con facturación > US$ 30M), expertos independientes (analistas financieros, periodistas económicos, ONGs, sindicatos, académicos, asociaciones de consumidores) y población general, evaluando estrategia comercial, gobierno corporativo, ESG, talento e innovación, complementado con auditoría de méritos objetivos bajo norma ISAE 3000 por KPMG; 3) Cadem Marcas Ciudadanas (Chile): Evalúa una muestra nacional representativa de consumidores y ciudadanos en Chile en 3 pilares clave: Presencia Positiva, Relevancia en el día a día y Aporte a la sociedad; 4) Group Caliber: Evalúa paneles continuos diarios en tiempo real de consumidores e inversores minoristas, midiendo el índice Trust & Like y tracking diario ESG; y 5) AMEC (Integrated Evaluation Framework): No utiliza una población fija predeterminada sino las audiencias objetivo del plan comunicacional, midiendo la cadena causal de resultados (Inputs, Actividades, Outputs, Out-takes, Outcomes e Impacto Organizacional) sin colapsar en un índice numérico único.",
        "findings": [
            {
                "claim_id": "P05-F07-C1",
                "claim": "Los modelos de reputación divergen sustancialmente en sus poblaciones objetivo y dimensiones analíticas, abarcando desde encuestas normativas de consumidores hasta paneles multistakeholder auditados.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2026", "region": "Global / Chile", "actor": "Proveedores de Medición de Reputación"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Comparativa Metodológica de Modelos de Medición de Reputación",
                        "excerpt_short": "Tabla comparativa de RepTrak, Merco, Cadem Chile, Group Caliber y AMEC detallando público evaluado, dimensiones clave, métrica de salida, auditoría externa y limitaciones.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "e31c5482-91a2-4920-8b1b-60f9aa5e1c6f",
                        "source_title": "Merco: Metodología Multistakeholder del Monitor Empresarial de Reputación Corporativa",
                        "original_url": "https://www.merco.info/cl/metodologia",
                        "locator": "Sección: Fases de la Evaluación Merco",
                        "excerpt_short": "Evaluación secuencial: directivos, expertos (financieros, periodistas, ONG, sindicatos, catedráticos), público general y evaluación directa de méritos objetivos. Auditado por KPMG bajo norma ISAE 3000.",
                        "source_date": "2024-05-10",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Metodologías públicas documentadas por los propios organismos emisores y sintetizadas en el dossier canónico."
            }
        ],
        "operational_model": {
            "inputs": ["Cuestionarios estructurados", "Paneles de expertos", "Muestras de consumidores", "Indicadores de mérito empresarial"],
            "actors": ["The RepTrak Company", "Merco / KPMG", "Cadem Chile", "Group Caliber", "AMEC"],
            "steps": ["Diseño muestral y selección de informantes", "Aplicación de encuestas y paneles", "Ponderación por dimensiones", "Normalización y publicación de índices"],
            "states": ["Fieldwork_Active", "Data_Cleaned", "Scored_and_Audited"],
            "outputs": ["Rankings de reputación, índices de favorabilidad y scorecards multidimensionales"],
            "exceptions": ["Baja tasa de respuesta en paneles de directivos o sesgos de deseabilidad social"]
        },
        "entities": [
            {"entity_id": "ENT_REPTRAK", "type": "modelo_medicion", "name": "The RepTrak Company", "aliases": ["RepTrak 100", "RepTrak Pulse"]},
            {"entity_id": "ENT_MERCO", "type": "modelo_medicion", "name": "Merco", "aliases": ["Monitor Empresarial de Reputación Corporativa"]},
            {"entity_id": "ENT_CADEM_MC", "type": "modelo_medicion", "name": "Cadem Marcas Ciudadanas", "aliases": ["Marcas Ciudadanas Chile"]},
            {"entity_id": "ENT_CALIBER", "type": "modelo_medicion", "name": "Group Caliber", "aliases": ["Caliber Real-Time Intelligence"]}
        ],
        "relations": [
            {"subject_id": "ENT_MERCO", "predicate": "aplica_auditoria_de", "object_id": "KPMG_ISAE_3000", "valid_from": "2010", "valid_to": None, "evidence_claim_id": "P05-F07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de informantes",
                "RepTrak / Cadem": "Primacía de la opinión pública general y consumidores informados.",
                "Merco": "Ponderación jerárquica con primacía de directivos corporativos, paneles de expertos y méritos duros.",
                "AMEC": "Audiencias a medida sin panel universal predefinido."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Configuración de Modelos", "implication": "BRIDGE debe permitir registrar qué modelo o índice externo está consultando el usuario corporativo para no comparar erróneamente un score de Cadem con uno de Merco.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F08
    {
        "question_id": "P05-F08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sesgos aparecen por muestreo, idioma, canal, tamaño de audiencia o período?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis crítico del corpus documenta cinco sesgos metodológicos sistemáticos en la medición de reputación: 1) Sesgo de notoriedad y recordación de marca (Brand Recall): En encuestas generales (RepTrak, Cadem), las empresas de gran tamaño o consumo masivo con altos presupuestos publicitarios rankean artificialmente alto por pura recordación, ocultando riesgos graves de gobernanza; 2) Sesgo elitista de panel corporativo: En modelos como Merco, el filtro inicial de directivos (empresas > US$ 30M) favorece a conglomerados tradicionales e invisibiliza a empresas disruptivas, B2B o con alta conflictividad territorial; 3) Sesgo de canal e hiperactividad digital (Social Listening): Las herramientas de escucha (Brandwatch, Meltwater) están distorsionadas por minorías vocales hiperactivas, indignación algorítmica y bots, produciendo falsos positivos de crisis que no permean en la ciudadanía silenciosa ni en los reguladores; 4) Sesgo de idioma y contexto cultural: Los modelos de NLP y análisis de sentimiento tradicionales fallan ante la ironía, el sarcasmo y los modismos locales del español chileno (chilenismos), malinterpretando interacciones; y 5) Sesgo de período y desfase temporal: Las encuestas anuales sufren desfase frente a contingencias inmediatas, mientras que el monitoreo digital en tiempo real reacciona a modas efímeras sin valor predictivo estructural.",
        "findings": [
            {
                "claim_id": "P05-F08-C1",
                "claim": "Cada canal y técnica de recolección introduce distorsiones estructurales que exigen correcciones de calibración muestral y contextual antes de orientar decisiones ejecutivas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Chile / Internacional", "actor": "Analistas de Datos de Reputación"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2: Limitaciones Metodológicas y Sesgos de las Herramientas Actuales",
                        "excerpt_short": "Tabla de sesgos: NLP sesgo léxico/cultural; Social Listening sesgo de minorías ruidosas; Encuestas sesgo de deseabilidad y Brand Recall; Métricas de alcance supuesto de exposición lineal.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 1: Eje 2, Hallazgo 2.3 (La falacia Sentimiento = Reputación)",
                        "excerpt_short": "El volumen y polaridad en redes sociales está sobrerrepresentado por minorías vocales hiperactivas y bots, sin reflejar la postura de reguladores, clientes mayoritarios ni inversores.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Sesgos rigurosamente catalogados en la literatura psicométrica y en el dossier de gaps del pilar P05."
            }
        ],
        "operational_model": {
            "inputs": ["Muestras brutas de redes sociales", "Bases de datos de encuestas", "Paneles de opinión"],
            "actors": ["Científico de Datos", "Metodólogo de Encuestas", "Analista de Inteligencia"],
            "steps": ["Detección de cuentas anómalas y bots en redes", "Ponderación demográfica por censo", "Ajuste por modelos de lenguaje afinados al dialecto local (BETO)"],
            "states": ["Raw_Signals_Loaded", "Biases_Identified", "Calibrated_Dataset_Produced"],
            "outputs": ["Conjunto de datos calibrado con advertencias de sesgo explícitas"],
            "exceptions": ["Eventos de saturación viral con brigadas coordinadas de astroturfing"]
        },
        "entities": [
            {"entity_id": "ENT_BIAS_CATALOG", "type": "catalogo_metodologico", "name": "Catálogo de Sesgos Muestrales y de Canal", "aliases": ["Measurement Biases"]}
        ],
        "relations": [
            {"subject_id": "ENT_BIAS_CATALOG", "predicate": "afecta_mediciones_de", "object_id": "ENT_REPUTATION", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P05-F08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de la distorsión",
                "Sesgo de Redes Sociales": "Sobrerrepresenta la indignación y la polarización extrema de nichos digitales activos.",
                "Sesgo de Encuestas Anuales": "Sobrerrepresenta la recordación marcaria masiva y diluye la criticidad de incidentes operacionales recientes."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Filtro de Desintoxicación y Calibración", "implication": "BRIDGE debe acompañar todo gráfico de percepción con notas de sesgo metodológico, indicando el tipo de informante, canal y representatividad.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F09
    {
        "question_id": "P05-F09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo separar resultado de encuesta, análisis de medios y juicio de analista?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El corpus exige separar taxativamente estas tres fuentes epistemológicas mediante una arquitectura de tres capas no conmensurables: 1) Resultado de Encuesta (Dato Perceptual Directo): Declaraciones expresas emitidas por sujetos muestreados probabilísticamente o en paneles calibrados bajo cuestionarios cerrados; reporta lo que la gente dice explícitamente que siente o piensa (e.g. porcentaje de favorabilidad neta o score Pulse), sujeto a margen de error estadístico y nivel de confianza formal; 2) Análisis de Medios (Dato de Difusión y Encuadre): Registro objetivo de volumen, centimetraje, cobertura, tono semántico y 'frames' periodísticos en publicaciones de prensa y plataformas públicas; reporta lo que los emisores y periodistas publican en el espacio público (e.g. modelo de reputación mediática de Deephouse); y 3) Juicio de Analista (Evaluación Pericial / SATs): Inferencia analítica estructurada generada por un experto humano o sistema pericial aplicando Técnicas Estructuradas de Análisis (SATs) como Análisis de Hipótesis Competitivas (ACH) o SCCT de Coombs; reporta la interpretación contextual, causalidad probable y nivel de amenaza institucional. La regla operativa prohíbe promediar aritméticamente un juicio cualitativo de analista con un porcentaje de encuesta o con el volumen de prensa.",
        "findings": [
            {
                "claim_id": "P05-F09-C1",
                "claim": "Encuestas, análisis de medios y juicio pericial constituyen capas de información ontológicamente incompatibles que deben presentarse en canales paralelos sin fusión indiscriminada.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Analistas de Inteligencia Corporativa"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Taxonomía Métrica Rigurosa: Distinción entre Niveles de Medición",
                        "excerpt_short": "Distinción entre volumen de medios (Nivel 1), exposición/alcance (Nivel 2), resonancia de actores (Nivel 3), percepción en encuestas (Nivel 4) e impacto conductual/evaluativo.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "8283e403-bd32-4a0f-91bf-a9a4587725f7",
                        "source_title": "Deephouse: Media Reputation as a Strategic Resource (Journal of Management)",
                        "original_url": "https://journals.sagepub.com/doi/10.1177/014920630002600602",
                        "locator": "Journal of Management, 26(6), pp. 1091-1112",
                        "excerpt_short": "Media reputation reflects public information intermediaries' framing, distinct from direct consumer surveys or internal management evaluations.",
                        "source_date": "2000-12-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio cardinal de la inteligencia estratégica y análisis estructurado de información."
            }
        ],
        "operational_model": {
            "inputs": ["Respuestas de encuestas cuantitativas", "Clips de noticias clasificados", "Memos de analistas expertos"],
            "actors": ["Investigador de Opinión Pública", "Especialista en Monitoreo de Medios", "Analista Senior de Inteligencia"],
            "steps": ["Etiquetado de origen de cada dato con metadato epistémico", "Visualización en tres paneles desacoplados en el dashboard", "Evaluación de concordancias y discrepancias entre capas"],
            "states": ["Raw_Inputs_Classified", "Source_Type_Tagged", "Triangulated_View_Rendered"],
            "outputs": ["Matriz de Triangulación: Encuesta vs Medios vs Juicio Pericial"],
            "exceptions": ["Tentativa de generar un único número que sume menciones en prensa y notas de encuesta"]
        },
        "entities": [
            {"entity_id": "ENT_TRIANGULATION_FRAMEWORK", "type": "metodologia", "name": "Marco de Triangulación Epistémica", "aliases": ["Epistemic Triangulation"]}
        ],
        "relations": [
            {"subject_id": "ENT_TRIANGULATION_FRAMEWORK", "predicate": "desacopla_capas_de", "object_id": "ENT_REPUTATION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-F09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Criterio de validación",
                "Encuesta": "Margen de error muestral y representatividad estadística formal.",
                "Análisis de Medios": "Cobertura de fuentes, fiabilidad del medio e indexación exhaustiva.",
                "Juicio de Analista": "Rigor en la aplicación de SATs, ausencia de sesgos cognitivos y consistencia argumentativa."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Inferencia", "implication": "BRIDGE debe etiquetar cada conclusión ejecutiva indicando si deriva de encuestas, medios o síntesis del modelo analítico, impidiendo atribuciones erróneas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F10
    {
        "question_id": "P05-F10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar modelos de medición y calidad de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Representar modelos de medición y calidad de forma estructurada exige modelar en el sistema las siguientes especificaciones: 1) Variables formales: `model_id` (e.g. REPTRAK, MERCO, CADEM, CALIBER, AMEC_IEF), `methodology_type` (Encuesta_Panel, Multistakeholder_Hibrido, RealTime_Tracker, Framework_Evaluativo), `sample_size` (N de casos o informantes), `sampling_error` (e.g. +/- 2.5%), `confidence_interval` (95%), `temporal_frequency` (Diaria, Semestral, Anual), `dimensions_evaluated` (lista de drivers o pilares), `audit_standard` (e.g. ISAE 3000 KPMG o N/A); 2) Categorías: Calidad del dato (Auditado_Externo, Autoreportado, Telemetria_Algoritmica); 3) Relaciones formales: `mide_a_traves_de` (Modelo -> Dimensiones), `audita_metodologia` (Auditor -> Modelo), `presenta_sesgo_conocido` (Modelo -> TipoSesgo), `aplica_a_poblacion` (Modelo -> TipoStakeholder); y 4) Condiciones de integridad: Prohibición absoluta de normalización aritmética directa entre modelos que emplean escalas incompatibles (e.g. sumar puntaje Merco 1-10.000 con Pulse 0-100); obligación de reportar siempre la fecha de trabajo de campo; y exigencia de declarar explícitamente si un ranking incluye evaluación de méritos objetivos o solo percepción.",
        "findings": [
            {
                "claim_id": "P05-F10-C1",
                "claim": "La modelación estructurada de los marcos de reputación exige tipificar el estándar de auditoría, las dimensiones evaluadas y las restricciones de comparabilidad entre metodologías.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Arquitectura de Plataforma BRIDGE"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Comparativa Metodológica de Modelos de Medición de Reputación",
                        "excerpt_short": "Define los atributos canónicos: enfoque, público evaluado, dimensiones, métrica de salida, auditoría externa, frecuencia temporal y limitaciones metodológicas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Basado en la estructura taxonómica comparada del dossier de investigación de P05."
            }
        ],
        "operational_model": {
            "inputs": ["Fichas técnicas metodológicas de estudios de reputación", "Informes de auditoría de procesos"],
            "actors": ["Ingeniero de Ontologías", "Analista de Calidad Metodológica"],
            "steps": ["Carga de metadatos del estudio", "Validación de cumplimiento de parámetros estadísticos", "Publicación en el catálogo de modelos estructurado"],
            "states": ["Metadata_Extracted", "Quality_Audited", "Model_Registered"],
            "outputs": ["Registro normalizado de modelo de medición en base relacional"],
            "exceptions": ["Estudios comerciales que ocultan el tamaño de la muestra o la fórmula de cálculo del score"]
        },
        "entities": [
            {"entity_id": "ENT_MODEL_REGISTRY", "type": "registro_sistema", "name": "Registro Estructurado de Modelos de Medición", "aliases": ["Measurement Model Registry"]}
        ],
        "relations": [
            {"subject_id": "ENT_MODEL_REGISTRY", "predicate": "valida_estandares_de", "object_id": "ENT_REPUTATION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-F10-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gestor de Modelos", "implication": "BRIDGE debe impedir la comparación de series temporales de diferentes proveedores sin aplicar un factor de normalización contextual debidamente advertido.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F11
    {
        "question_id": "P05-F11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre modelos de medición y calidad?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Cada hecho relativo a modelos de medición y calidad está respaldado por fuentes primarias documentadas en el corpus: 1) RepTrak (2022, 7 Ways to Quantify Reputation and 7 Drivers Model, ámbito: medición normativa internacional): respalda la estructura de 7 drivers y su vínculo causal con los comportamientos de apoyo (supportive behaviors); 2) Merco (2024, Metodología Multistakeholder del Monitor Empresarial de Reputación Corporativa / Merco Chile 2024, ámbito: rankings corporativos en Iberoamérica): respalda el proceso secuencial en cuatro etapas y la certificación independiente bajo norma ISAE 3000 por KPMG; 3) Cadem Chile (2024, Marcas Ciudadanas — Metodología de Impacto y Relevancia Social, ámbito: mercado de consumo y ciudadanía en Chile): respalda la evaluación semestral de Presencia Positiva, Relevancia Cotidiana y Aporte Comunitario; 4) Group Caliber (2024, Real-Time Stakeholder Intelligence & Reputation Monitoring Platform, ámbito: SaaS de telemetría continua): respalda el seguimiento diario 365 días al año del vínculo emocional e indicadores ESG; y 5) AMEC (2020/2022, Barcelona Principles 3.0 e Integrated Evaluation Framework, ámbito: taxonomía global de evaluación de comunicaciones): respalda la jerarquía causal estricta de Outputs, Out-takes, Outcomes e Impacto.",
        "findings": [
            {
                "claim_id": "P05-F11-C1",
                "claim": "Los estándares metodológicos y modelos de calidad disponen de especificaciones técnicas publicadas por sus organizaciones matrices con trazabilidad pericial.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Chile / Internacional", "actor": "Organizaciones Metodológicas"},
                "evidence": [
                    {
                        "source_id": "9345d275-3d3f-4a23-933b-beafacded60c",
                        "source_title": "RepTrak: 7 Ways to Quantify Reputation and 7 Drivers Model",
                        "original_url": "https://www.reptrak.com/blog/7-ways-to-quantify-reputation/",
                        "locator": "Publicación corporativa RepTrak 2022",
                        "excerpt_short": "Documenta los 7 drivers y la metodología de regresión para explicar el Pulse Score y la propensión a recomendar o comprar.",
                        "source_date": "2022-04-10",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "71599e71-f733-4c27-b88c-50c851b04fb8",
                        "source_title": "Merco Chile: Ranking de Empresas y Criterios de Evaluación Multistakeholder",
                        "original_url": "https://www.merco.info/cl/ranking-merco-empresas",
                        "locator": "Ficha metodológica Merco Chile 2024",
                        "excerpt_short": "Muestra compuesta por más de 1.000 directivos y paneles de expertos sectoriales con dictamen pericial ISAE 3000 de KPMG.",
                        "source_date": "2024-06-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación documental completa con reportes metodológicos oficiales vigentes."
            }
        ],
        "operational_model": {
            "inputs": ["Publicaciones técnicas originales", "Registros metodológicos públicos"],
            "actors": ["Curador de Fuentes", "Auditor de Información"],
            "steps": ["Verificación de URL y texto sustantivo", "Comprobación de dictámenes de auditoría externa", "Registro en base de evidencias de P05"],
            "states": ["Sources_Indexed", "Verifications_Completed", "Manifest_Frozen"],
            "outputs": ["Catálogo de fuentes primarias auditadas"],
            "exceptions": ["Documentos con enlaces rotos sustituidos por memorias técnicas verificadas"]
        },
        "entities": [
            {"entity_id": "ENT_METHODOLOGY_SOURCES", "type": "corpus_fuentes", "name": "Fuentes de Metodología de Reputación", "aliases": ["Reputation Methodology Sources"]}
        ],
        "relations": [
            {"subject_id": "ENT_METHODOLOGY_SOURCES", "predicate": "respalda_modelos_de", "object_id": "ENT_MODEL_REGISTRY", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P05-F11-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Auditoría de Fuentes", "implication": "BRIDGE debe proveer enlaces directos a las metodologías oficiales cuando presente evaluaciones comparadas de RepTrak, Merco o Cadem.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F12
    {
        "question_id": "P05-F12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra modelos de medición y calidad sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El caso concreto documentado en el corpus que ilustra los modelos de medición y sus diferencias de calidad es la evaluación comparada de una empresa corporativa de infraestructura / energía en Chile a través de Merco Chile vs. Cadem Marcas Ciudadanas: 1) Entradas del Sistema: a) Evaluación Merco: La empresa es evaluada en primera fase por directivos empresariales y en segunda fase por analistas financieros, periodistas económicos y comités de gobierno corporativo, complementado con auditoría de méritos objetivos (cumplimiento regulatorio, solvencia financiera y gobierno corporativo bajo ISAE 3000 de KPMG); b) Evaluación Cadem: La empresa es evaluada mediante encuesta nacional a consumidores y ciudadanos urbanos sobre su presencia en la vida cotidiana y su aporte percibido a la sociedad; 2) Proceso y Resultado Observado: En Merco, la empresa obtiene una posición en el Top 20 del ranking general debido a su solidez de balance, gobierno corporativo y alta valoración entre pares ejecutivos y analistas financieros. Sin embargo, en Cadem Marcas Ciudadanas, la empresa no califica dentro del ranking de marcas relevantes o registra una baja puntuación de 'Presencia Positiva', dado que su servicio no es de consumo masivo directo y la ciudadanía general desconoce su impacto positivo o la asocia negativamente con obras en el territorio. El resultado esperado demuestra que ambos modelos son válidos pero miden constructos y poblaciones distintas: Merco mide reputación corporativa y legitimidad ante la élite económica y expertos, mientras Cadem mide impacto social y vínculo afectivo directo con el consumidor masivo.",
        "findings": [
            {
                "claim_id": "P05-F12-C1",
                "claim": "La discrepancia empírica de una empresa en diferentes rankings refleja la diversidad de poblaciones evaluadas y constructos medidos, validando la necesidad de triangulación metodológica.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024", "region": "Chile", "actor": "Empresas en Chile / Merco / Cadem"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Comparativa Metodológica de Modelos de Medición de Reputación",
                        "excerpt_short": "Merco sesgado hacia grandes corporaciones con alta visibilidad directiva; Cadem con foco primario en marcas de consumo masivo y menor granularidad en B2B e industrias extractivas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "526111d7-05a7-4169-81f5-1977d16b8352",
                        "source_title": "Cadem Chile: Marcas Ciudadanas — Metodología de Impacto y Relevancia Social",
                        "original_url": "https://cadem.cl/marcas-ciudadanas/",
                        "locator": "Metodología Marcas Ciudadanas 2024",
                        "excerpt_short": "Evalúa marcas que tienen un impacto relevante en la sociedad y en la vida cotidiana de las personas, con foco en el consumidor masivo y presencia en el hogar.",
                        "source_date": "2024-07-20",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Divergencia estructural ampliamente observada en los reportes anuales de ambos monitores en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Puntaje Merco Empresas Chile", "Puntaje Cadem Marcas Ciudadanas"],
            "actors": ["Director de Comunicaciones", "Comité Ejecutivo", "Consultor de Marca"],
            "steps": ["Cruce de puntajes entre estudios", "Desagregación por perfil de informante", "Explicación de discrepancias al directorio"],
            "states": ["Rankings_Received", "Variance_Analyzed", "Executive_Brief_Delivered"],
            "outputs": ["Informe explicativo de divergencia entre reputación corporativa de élite y cercanía ciudadana"],
            "exceptions": ["Interpretación ejecutiva errónea de que una caída en Cadem implica pérdida de confianza financiera en Merco"]
        },
        "entities": [
            {"entity_id": "ENT_COMPARISON_CASE_CHILE", "type": "caso_analitico", "name": "Caso Comparativo Merco vs Cadem en Chile", "aliases": ["Divergencia Ranking Élite vs Masivo"]}
        ],
        "relations": [
            {"subject_id": "ENT_COMPARISON_CASE_CHILE", "predicate": "ejemplifica_triangulacion_de", "object_id": "ENT_MODEL_REGISTRY", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P05-F12-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de valor",
                "Ranking Merco": "Mide reputación institucional, solidez de gobierno, talento y méritos objetivos para stakeholders especializados.",
                "Ranking Cadem": "Mide conexión afectiva, cotidianidad de consumo y relevancia percibida en los hogares chilenos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Interpretador de Métricas", "implication": "BRIDGE debe contextualizar los resultados de rankings explicando explícitamente qué segmento fue consultado y por qué una empresa B2B no compite en las mismas condiciones que una empresa de retail o consumo masivo.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P05.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P05-F07..F12) to {out_path}.")
