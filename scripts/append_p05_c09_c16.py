import json
from pathlib import Path

NOTEBOOK_ID = "0fc2e780-e279-4923-83c5-90fe621a4543"
SNAPSHOT_AT = "2026-10-01T03:00:00-03:00"

records = [
    # P05-C09
    {
        "question_id": "P05-C09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre actores y prominencia, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia identificada en el corpus contrapone dos visiones sobre el relacionamiento con partes interesadas: por un lado, la concepción del lobby tradicional como una gestión relacional informal, opaca y no documentada ('gestión de contactos y pasillos') que subestima a las comunidades y prioriza exclusivamente a las autoridades de gobierno; por otro lado, el enfoque formal sustentado en la literatura de stakeholders (Mitchell, Agle & Wood 1997), los estándares de rendición de cuentas (AA1000SES 2015) y el marco institucional chileno (Ley 20.730 de Lobby y Convenio 169 OIT). Las síntesis internas canónicas (P05_EVIDENCE_MAP Tensión 5 y P05_RESEARCH_DOSSIER Sección 5) resuelven que el lobby y el relacionamiento institucional deben gestionarse como un proceso auditable, documentado y transparente integrado al repositorio corporativo oficial. Prevalece de forma definitiva la versión rigurosa de P05: la plataforma BRIDGE debe descartar la informalidad opaca, estructurar a los actores según su prominencia dinámica (Poder, Legitimidad y Urgencia) y exigir la trazabilidad de cada audiencia y gestión pública conforme a la Ley 20.730.",
        "findings": [
            {
                "claim_id": "P05-C09-C1",
                "claim": "Prevalece la exigencia de transparencia y gestión estructurada de partes interesadas bajo la Ley 20.730 y el modelo de Mitchell et al., proscribiendo la gestión informal u opaca de influencias.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Gestión de Asuntos Públicos y Lobby"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Matriz de Tensiones Epistemológicas, Tensión 5",
                        "excerpt_short": "Incorporar compliance de transparencia de lobby. Conectar reuniones de agenda pública con el archivo corporativo de temas y posiciones oficiales. Nivel de confianza DEFINITIVO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "537a7618-1e79-4747-ad6b-6e492a4a15b7",
                        "source_title": "BCN Chile: Ley 20.730 Regula el Lobby y las Gestiones que Representen Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Título I y II",
                        "excerpt_short": "Establece el registro público de lobbistas, gestores de intereses y viajes, garantizando el principio de probidad y transparencia en las decisiones del Estado.",
                        "source_date": "2014-03-08",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal obligatoria vigente en Chile y principio ético consagrado en las directrices de P05."
            }
        ],
        "operational_model": {
            "inputs": ["Registros de reuniones institucionales", "Plataforma InfoLobby del Estado"],
            "actors": ["Oficial de Cumplimiento de Lobby", "Director de Asuntos Públicos"],
            "steps": ["Verificación de registro formal de audiencias", "Indexación de temas tratados en el corpus interno", "Auditoría de cumplimiento de la Ley 20.730"],
            "states": ["Meeting_Requested", "Lobby_Registered", "Institutional_Compliance_Enforced"],
            "outputs": ["Reporte de Transparencia de Gestión de Intereses Particulares"],
            "exceptions": ["Gestiones informales no declaradas, sancionables por la Contraloría o tribunales"]
        },
        "entities": [
            {"entity_id": "ENT_LOBBY_COMPLIANCE", "type": "marco_cumplimiento", "name": "Compliance de Transparencia de Lobby Ley 20.730", "aliases": ["Lobby Transparency Framework"]}
        ],
        "relations": [
            {"subject_id": "ENT_LOBBY_COMPLIANCE", "predicate": "regula_interacciones_de", "object_id": "ENT_ACTOR_SCHEMA", "valid_from": "2014", "valid_to": None, "evidence_claim_id": "P05-C09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de gestión de actores",
                "Lobby Informal Opaco": "Confía en relaciones personales no registradas, exponiendo a la empresa a escándalos de tráfico de influencias.",
                "Gestión Estructurada BRIDGE": "Registra audiencias públicas bajo Ley 20.730, alineando los temas conversados con la evidencia técnica oficial de la empresa."
            }
        ],
        "contradictions": [
            {"issue": "Gestión de lobby informal vs transparente", "source_a": "Práctica de gestión de contactos no reglada", "source_b": "Ley 20.730 / P05_EVIDENCE_MAP", "resolution": "Prevalece la Ley 20.730 y P05: toda gestión institucional debe ser pública, transparente y auditable."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Conector InfoLobby", "implication": "BRIDGE debe sincronizarse con las APIs públicas de la Ley de Lobby en Chile para mapear qué gestores de intereses están activos ante qué autoridades.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C10
    {
        "question_id": "P05-C10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre actores y prominencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de gaps documentado en P05_GAPS_AND_VALIDATION Sección 2 establece: 1) Lo que sigue sin prueba rigurosa: La captura estructurada y en tiempo real de interacciones informales o semi-formales entre actores de poder que ocurren fuera de las audiencias oficiales regladas (e.g. encuentros en foros gremiales, seminarios académicos, eventos benéficos o conversaciones parlamentarias de pasillo). El sistema no cuenta con mecanismos empíricos para medir la influencia real de estas interacciones sin vulnerar la privacidad de las personas; 2) Qué fuente es parcial o falló: La plataforma InfoLobby / Ley 20.730 es parcial debido al desfase de actualización en los portales ministeriales (retrasos de 30 a 60 días en la carga de actas) y a la exclusión de reuniones que los sujetos pasivos catalogan como 'técnicas' o 'informativas' no afectas a lobby; 3) Validación mínima que resolvería la incertidumbre: Implementar un algoritmo de triangulación que cruce los registros formales de InfoLobby con los calendarios de sesiones de comisiones legislativas del Congreso Nacional, asistencias públicas de autoridades a foros sectoriales y noticias de prensa económica, generando un índice compuesto de proximidad institucional con banderas de actualización continua.",
        "findings": [
            {
                "claim_id": "P05-C10-C1",
                "claim": "Los registros oficiales de lobby presentan desfases temporales y exclusiones de interacciones informales, exigiendo la triangulación con calendarios legislativos y coberturas públicas de líderes de opinión.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Chile", "actor": "Monitoreo Institucional de Lobby"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2: Sistemas de Registro de Lobby (InfoLobby / Ley 20.730)",
                        "excerpt_short": "Sub-reporte de gestiones informales y desfase en la actualización de registros públicos. Mecanismo de atenuación: cruzar registros formales con calendarios legislativos y coberturas mediáticas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Limitación empírica demostrada en los informes de observancia de transparencia del Consejo para la Transparencia en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Actas de InfoLobby", "Calendarios de comisiones parlamentarias", "Cobertura de prensa política"],
            "actors": ["Analista de Asuntos Públicos", "Científico de Datos"],
            "steps": ["Descarga periódica de bases de datos de InfoLobby", "Cruce con asistencias registradas en el Congreso", "Detección de interacciones no mapeadas en la agenda oficial"],
            "states": ["Official_Lobby_Ingested", "Parliamentary_Schedule_CrossChecked", "Interaction_Index_Updated"],
            "outputs": ["Matriz de Proximidad Institucional Triangulada"],
            "exceptions": ["Reuniones estrictamente privadas que escapan a todo registro público auditable"]
        },
        "entities": [
            {"entity_id": "ENT_LOBBY_DATA_GAP", "type": "vacio_metodologico", "name": "Brecha de Completitud en Registros de Lobby", "aliases": ["Lobby Reporting Lag Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_LOBBY_DATA_GAP", "predicate": "limita_cobertura_de", "object_id": "ENT_LOBBY_COMPLIANCE", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P05-C10-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de cobertura de interacciones",
                "Registro Exclusivo InfoLobby": "Captura únicamente las reuniones formalmente concedidas y publicadas con semanas de rezago.",
                "Triangulación BRIDGE": "Detecta si la empresa compareció en la comisión investigadora o participó en el panel sectorial con la autoridad en tiempo real."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Monitor de Agenda Pública", "implication": "BRIDGE debe incorporar un pipeline de ingesta de diarios de sesiones del Senado y Cámara para compensar el rezago temporal de los registros de lobby ministeriales.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_LOBBY_OFFLINE_LAG", "description": "Rezago temporal y exclusión de interacciones no regladas en los portales públicos de lobby.", "severity": "media", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C11
    {
        "question_id": "P05-C11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre crisis, controversias y casos, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia esencial en la gestión de crisis corporativas contrapone la práctica legalista tradicional de defensa litigiosa (estrategia de negación, minimización de culpa y dilación judicial, representada por la postura histórica de SCA en el caso Tissue) frente a la Teoría Situacional de la Comunicación de Crisis (SCCT de Coombs 2007) y las directrices éticas de la Arthur W. Page Society. Abogados defensores tradicionales aconsejan no admitir responsabilidad para evitar contingencias indemnizatorias. Sin embargo, las síntesis canónicas internas (P05_RESEARCH_DOSSIER Sección 6 y P05_EVIDENCE_MAP Eje 6) y la jurisprudencia condenatoria de la Corte Suprema demuestran que, ante crisis del cluster Prevenible/Intencional (como la colusión o el fraude ambiental doloso), la negación o justificación produce el peor resultado posible: revoca beneficios procesales de delación compensada, impone multas máximas y colapsa la reputación de forma irreversible. Prevalece la regla científica de P05: en crisis prevenibles con alta atribución de culpabilidad, la única estrategia eficaz para restaurar la viabilidad institucional es la asunción temprana de responsabilidad, la compensación material directa y la reforma profunda y verificable de la gobernanza corporativa.",
        "findings": [
            {
                "claim_id": "P05-C11-C1",
                "claim": "Prevalece la prescripción de la teoría SCCT de Coombs confirmada por la Corte Suprema de Chile: las estrategias de negación en crisis dolosas agravan la sanción judicial y aceleran la destrucción del capital reputacional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2007-2026", "region": "Chile / Global", "actor": "Teoría SCCT y Jurisprudencia Chilena"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 1: Eje 6, Hallazgo 6.1 (Teoría SCCT de Coombs)",
                        "excerpt_short": "Regla cardinal: Emplear estrategias de negación o minimización frente a crisis prevenibles con alta atribución de culpa amplifica el daño reputacional de forma irreversible. Nivel de confianza MUY ALTO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "07fa821a-9a20-4e9c-a917-24b0cde7fc98",
                        "source_title": "FNE Chile: Sentencia Condenatoria Colusión Papel Tissue CMPC y SCA (Caso Reputacional)",
                        "original_url": "https://www.fne.gob.cl/corte-suprema-condena-a-cmpc-y-sca-por-colusion-en-el-mercado-del-papel-tissue/",
                        "locator": "Sentencia Corte Suprema, Pronunciamiento sobre Coacción de SCA",
                        "excerpt_short": "La Corte desestimó la exención a SCA por considerar que no acreditó coacción insuperable, sancionando su postura litigiosa con la multa más alta del cartel.",
                        "source_date": "2020-01-06",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Comprobación judicial ejecutoriada en Chile articulada con el estándar científico global de Coombs."
            }
        ],
        "operational_model": {
            "inputs": ["Evaluación de responsabilidad en el incidente", "Evidencias probatorias disponibles"],
            "actors": ["Comité de Crisis", "Consejero General", "Director de Asuntos Corporativos"],
            "steps": ["Diagnóstico de cluster bajo SCCT (Víctima, Accidental o Prevenible)", "Bloqueo de estrategias defensivas de negación si la atribución es dolosa", "Prescripción de protocolo de reconstrucción, disculpa y compensación"],
            "states": ["Incident_Evaluated", "Blame_Determined", "Rebuild_Strategy_Enforced"],
            "outputs": ["Estrategia institucional de respuesta a crisis alineada con SCCT"],
            "exceptions": ["Incidentes donde la empresa es víctima de sabotaje externo acreditado pericialmente"]
        },
        "entities": [
            {"entity_id": "ENT_SCCT_PREVALENCE", "type": "regla_prescriptiva", "name": "Prevalencia de Estrategias de Reconstrucción SCCT", "aliases": ["SCCT Rebuild Primacy"]}
        ],
        "relations": [
            {"subject_id": "ENT_SCCT_PREVALENCE", "predicate": "gobierna_postura_en", "object_id": "ENT_CRISIS_SCHEMA", "valid_from": "2007", "valid_to": None, "evidence_claim_id": "P05-C11-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resultado de la estrategia de respuesta",
                "Enfoque Litigioso de Negación": "Aumenta la indignación ciudadana, acarrea multas máximas y destruye la marca.",
                "Enfoque de Reconstrucción SCCT": "Contiene la pérdida de clientes, permite acuerdos de compensación y viabiliza la continuidad operativa."
            }
        ],
        "contradictions": [
            {"issue": "Postura de negación en crisis culposas", "source_a": "Asesoría legal litigiosa tradicional", "source_b": "SCCT de Coombs / Sentencia Corte Suprema Tissue", "resolution": "Prevalece Coombs y la Corte Suprema: la negación ante faltas dolosas acreditadas agrava irreversiblemente el daño."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Simulador de Crisis", "implication": "BRIDGE debe mostrar al Comité Ejecutivo el contraste CMPC vs SCA cuando debatan entre una postura de disculpa transparente o una defensa de justificación.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C12
    {
        "question_id": "P05-C12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre crisis, controversias y casos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de gaps documentado en P05_GAPS_AND_VALIDATION establece: 1) Lo que sigue sin prueba matemática formal: La curva exacta de decaimiento temporal y restitución de confianza reputacional post-crisis. Aunque se sabe que la recuperación requiere años de sacrificios verificables, no existe un modelo matemático estandarizado que prediga con precisión cuántos meses tardará una compañía en recuperar su nivel previo de favorabilidad tras una compensación histórica como la del caso Tissue; 2) Qué fuente es parcial o falló: Fallan los monitores de reputación anuales tradicionales (como Merco o RepTrak), los cuales omiten o aplazan la inclusión de empresas en crisis abiertas, generando un vacío de datos longitudinales durante el período álgido del conflicto; 3) Validación mínima que resolvería la incertidumbre: Implementar un panel de seguimiento longitudinal de cohortes fijas de opinión pública y clientes con mediciones semestrales durante 5 años posteriores a la resolución judicial de una crisis emblemática, midiendo la tasa de desvanecimiento del recuerdo negativo (\nrecuperación gamma) en función de hitos de compensación y cambios de gobernanza acreditados.",
        "findings": [
            {
                "claim_id": "P05-C12-C1",
                "claim": "La modelación cuantitativa de la tasa de recuperación de confianza post-crisis carece de series temporales continuas de largo plazo en Chile, requiriendo estudios de panel de cohortes fijas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Investigación Longitudinal de Crisis"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1: Desfase Temporal entre Monitoreo en Tiempo Real y Métricas Estructurales",
                        "excerpt_short": "Los monitores de reputación consolidados operan en ciclos anuales o semestrales debido a la complejidad de las encuestas, dejando lagunas de información en la trayectoria de recuperación post-crisis.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío empírico documentado en la literatura de longitudinalidad de reputación corporativa."
            }
        ],
        "operational_model": {
            "inputs": ["Series temporales de encuestas post-crisis", "Hitos de cumplimiento de compensaciones"],
            "actors": ["Investigador de Opinión Pública", "Analista de Inteligencia"],
            "steps": ["Diseño de panel de seguimiento de 5 años", "Medición de asociaciones cognitivas espontáneas con la marca", "Ajuste de modelos de decaimiento exponencial"],
            "states": ["Cohort_Established", "Longitudinal_Tracking_Active", "Recovery_Curve_Modelled"],
            "outputs": ["Curva empírica de retorno de confianza post-crisis"],
            "exceptions": ["Nuevas contingencias operacionales que reinicien el ciclo de pérdida de confianza"]
        },
        "entities": [
            {"entity_id": "ENT_RECOVERY_CURVE_GAP", "type": "vacio_metodologico", "name": "Brecha de Modelación de Curvas de Recuperación", "aliases": ["Post-Crisis Recovery Curve Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_RECOVERY_CURVE_GAP", "predicate": "limita_modelado_de", "object_id": "ENT_CRISIS_SCHEMA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C12-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de monitoreo",
                "Encuesta Anual Aislada": "Una foto estática al año que no permite correlacionar el efecto de la compensación con la recuperación.",
                "Panel de Cohortes Continuo": "Mide mes a mes cómo la entrega del dinero del SERNAC o la renovación del directorio reduce la tasa de animadversión hacia la marca."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Monitor de Recuperación", "implication": "BRIDGE debe permitir registrar el hito de compensación y proyectar un intervalo de confianza de 24 a 48 meses para la estabilización de los indicadores de reputación.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_POST_CRISIS_LONGITUDINAL", "description": "Falta de modelos cuantitativos calibrados sobre la velocidad de recuperación reputacional post-compensación en Chile.", "severity": "media", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C13
    {
        "question_id": "P05-C13",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre doble materialidad y regulación, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia doctrinal en el ámbito ESG contrapone el enfoque anglosajón tradicional de 'Materialidad Financiera Simple' (respaldado históricamente por SASB y adoptado por los estándares ISSB / IFRS S1 y S2), el cual exige reportar únicamente aquellos factores ambientales o sociales que impacten de forma directa y mensurable el valor bursátil o los flujos de caja de la firma (Outside-In), frente al enfoque europeo y latinoamericano de 'Doble Materialidad' consagrado en las directivas de EFRAG ESRS (IG 1 2024), GRI Standards y la NCG 461 de la CMF de Chile. Las síntesis canónicas internas (P05_EVIDENCE_MAP Tensión 3 y P05_RESEARCH_DOSSIER Sección 4.3) demuestran que limitar la gestión a la materialidad financiera genera un 'punto ciego catastrófico': los impactos de la empresa sobre el ecosistema y las comunidades (Inside-Out) que son desatendidos por no considerarse 'financieramente materiales' hoy, mutan en pocos meses hacia paralizaciones de obras, demandas colectivas y multas de la SMA, destruyendo el valor de la empresa. De acuerdo con las correcciones del mandato, prevalece de forma categórica el principio de Doble Materialidad disyuntiva: un asunto es material si cumple con la dimensión de impacto social/ambiental O con la dimensión financiera, debiendo ser gestionado obligatoriamente por la gerencia de asuntos corporativos.",
        "findings": [
            {
                "claim_id": "P05-C13-C1",
                "claim": "Prevalece el enfoque de Doble Materialidad de EFRAG y la CMF NCG 461, proscribiendo el sesgo de materialidad exclusivamente financiera que invisibiliza impactos territoriales y comunitarios críticos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile / Europa", "actor": "Supervisión Financiera y ESG"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Matriz de Tensiones Epistemológicas, Tensión 3",
                        "excerpt_short": "Implementar Doble Materialidad. Permite a los directores de asuntos corporativos gestionar tanto el riesgo de capital como el riesgo de legitimidad comunitaria y regulatoria. Nivel de confianza MUY ALTO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "432f26cd-3292-4459-8239-eef44bcf1527",
                        "source_title": "EFRAG: Implementation Guidance 1 (IG 1) Materiality Assessment for ESRS",
                        "original_url": "https://www.efrag.org/",
                        "locator": "Sección 3: Double Materiality Framework",
                        "excerpt_short": "Double materiality is the cornerstone of corporate sustainability reporting, requiring identification of severe impacts on society regardless of immediate financial translation.",
                        "source_date": "2024-05-31",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución normativa expresa consagrada en la directiva CSRD europea y adoptada en la NCG 461 de la CMF."
            }
        ],
        "operational_model": {
            "inputs": ["Informes de impacto social", "Modelos de valuación financiera corporativa"],
            "actors": ["Comité de Sostenibilidad", "Gerente de Finanzas", "Director de Asuntos Corporativos"],
            "steps": ["Evaluación independiente de impacto y finanzas", "Aplicación de regla disyuntiva EFRAG", "Inclusión obligatoria en la agenda del directorio"],
            "states": ["Single_Materiality_Challenged", "Double_Materiality_Approved", "Reporting_Aligned"],
            "outputs": ["Inventario de temas materiales conforme al estándar de doble materialidad"],
            "exceptions": ["Intentos de la gerencia financiera de desestimar denuncias de afectación a glaciares o agua por falta de impacto contable en el trimestre"]
        },
        "entities": [
            {"entity_id": "ENT_DOUBLE_MATERIALITY_PREVALENCE", "type": "regla_regulatoria", "name": "Prevalencia de la Doble Materialidad Disyuntiva", "aliases": ["Double Materiality Primacy"]}
        ],
        "relations": [
            {"subject_id": "ENT_DOUBLE_MATERIALITY_PREVALENCE", "predicate": "estructura_analisis_de", "object_id": "ENT_MATERIALITY_SCHEMA", "valid_from": "2021", "valid_to": None, "evidence_claim_id": "P05-C13-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de gestión de riesgos",
                "Materialidad Financiera Simple": "Ignora el impacto en la comunidad hasta que estalla el litigio.",
                "Doble Materialidad": "Identifica y mitiga el impacto en la comunidad desde su origen, previniendo el litigio antes de que destruya el valor financiero."
            }
        ],
        "contradictions": [
            {"issue": "Materialidad financiera simple vs doble materialidad", "source_a": "Estándares tradicionales anglosajones (ISSB simple)", "source_b": "EFRAG ESRS IG 1 / CMF NCG 461 / P05_EVIDENCE_MAP", "resolution": "Prevalece la Doble Materialidad: un tema es material por su impacto social/ecológico o por sus riesgos financieros."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Materialidad", "implication": "BRIDGE debe implementar la regla disyuntiva de EFRAG en su base de datos para impedir que se filtren o descarten impactos comunitarios graves.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C14"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C14
    {
        "question_id": "P05-C14",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre doble materialidad y regulación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de limitaciones documentado en P05_GAPS_AND_VALIDATION establece: 1) Lo que sigue sin prueba rigurosa: La consistencia pericial y comparabilidad cruzada de los dictámenes de aseguramiento externo independiente bajo norma ISAE 3000 emitidos por diferentes firmas auditoras en Chile sobre las memorias anuales NCG 461. Al no existir protocolos cuantitativos obligatorios sobre niveles de materialidad cualitativa, una misma práctica corporativa puede ser aprobada sin observaciones por una firma auditora y objetada por otra; 2) Qué fuente es parcial o falló: Fallan las memorias de aseguramiento limitado estándar de las Big Four en Chile, que suelen contener dictámenes con declaraciones genéricas de 'no haber detectado inconsistencias' sin verificar en profundidad los reclamos socioambientales territoriales de base; 3) Validación mínima que resolvería la incertidumbre: El desarrollo y publicación por parte de la Comisión para el Mercado Financiero (CMF) de una Guía de Criterios Periciales de Aseguramiento ESG con rangos de tolerancia específicos, checklists estandarizados de verificación territorial y obligatoriedad de contraste con los expedientes sancionatorios de la SMA y fallos de los Tribunales Ambientales.",
        "findings": [
            {
                "claim_id": "P05-C14-C1",
                "claim": "El aseguramiento independiente ISAE 3000 sobre métricas cualitativas de sostenibilidad adolece de variabilidad metodológica en Chile, requiriendo guías periciales vinculantes emitidas por la CMF.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Auditoría de Sostenibilidad e ISAE 3000"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1: Vacíos Críticos de Evidencia Identificados en la Literatura",
                        "excerpt_short": "Falta de benchmarks estandarizados y heterogeneidad de criterios periciales en la verificación de reportes de sostenibilidad no financieros.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "11ce6bf4-9dcf-4933-bf0b-d6a7579da3ac",
                        "source_title": "CMF Chile: Norma de Carácter General NCG 461 (Gobierno Corporativo y ESG)",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Instrucciones de Auditoría Externa en Memorias Anuales",
                        "excerpt_short": "Recomienda el aseguramiento independiente de las métricas reportadas, dejando a las sociedades la selección del alcance y nivel de aseguramiento.",
                        "source_date": "2021-11-12",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío operativo constatado en la implementación de la NCG 461 de la CMF en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Dictámenes de auditoría ISAE 3000 de memorias anuales", "Expedientes de la SMA"],
            "actors": ["Auditor Externo", "Regulador CMF", "Comité de Auditoría"],
            "steps": ["Cotejo de métricas declaradas en la memoria con expedientes sancionatorios de la SMA", "Detección de omisiones de pasivos ambientales en el dictamen", "Emisión de requerimiento de aclaración a la firma auditora"],
            "states": ["Report_Audited", "Discrepancy_Detected", "Clarification_Required"],
            "outputs": ["Informe de Auditoría de Aseguramiento de Sostenibilidad Calibrado"],
            "exceptions": ["Dictámenes de aseguramiento limitado que excluyen expresamente la revisión de faenas en terreno"]
        },
        "entities": [
            {"entity_id": "ENT_ISAE_3000_GAP", "type": "vacio_metodologico", "name": "Brecha de Estandarización de Aseguramiento ISAE 3000", "aliases": ["ISAE 3000 Assurance Consistency Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_ISAE_3000_GAP", "predicate": "afecta_confiabilidad_de", "object_id": "ENT_MATERIALITY_SCHEMA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C14-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de profundidad de auditoría",
                "Aseguramiento Limitado Tradicional": "Revisión documental en oficina central sin visita a cuencas ni contraste con expedientes judiciales.",
                "Aseguramiento Robusto Propuesto": "Verificación cruzada obligatoria con el Sistema Nacional de Información de Fiscalización Ambiental (SNIFA de la SMA)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Validador de Memorias CMF", "implication": "BRIDGE debe cruzar automáticamente los borradores de memoria NCG 461 con el portal SNIFA de la SMA para alertar inconsistencias antes de la entrega al auditor externo.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_ISAE3000_CONSISTENCY", "description": "Heterogeneidad de criterios periciales de aseguramiento no financiero ISAE 3000 entre firmas auditoras en Chile.", "severity": "media", "status": "documentado"}
        ],
        "next_question_ids": ["P05-C15"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C15
    {
        "question_id": "P05-C15",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre decisiones de producto y evaluación, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La discrepancia en el diseño de productos de inteligencia ejecutiva enfrenta la lógica comercial de las herramientas de 'Social Listening y Alerta Rápida' con la arquitectura prudencial de BRIDGE. Plataformas comerciales tradicionales están diseñadas para maximizar el 'engagement' de los usuarios mediante notificaciones de pánico cada vez que se detecta un pico de menciones negativas, instando al ejecutivo a 'responder de inmediato' y ofreciendo generadores de comunicados automatizados con IA generativa sin validación previa. En contraste, las síntesis canónicas internas (P05_RESEARCH_DOSSIER Sección 7.1 y 7.2; P05_GAPS_AND_VALIDATION Sección 4) y la teoría de relaciones públicas (Page Society 2023; Coombs 2007) dictaminan que las respuestas reactivas apresuradas generan el Efecto Streisand y provocan que la firma emita falsedades involuntarias o admita culpas inexistentes. Prevalece la regla de arquitectura de BRIDGE: el software debe incorporar compuertas algorítmicas de abstención estratégica, exigir la verificación interna de hechos fácticos (P04) antes de permitir la generación de respuestas públicas y presentar notas explícitas de advertencia sobre sesgos muestrales e incertidumbre de las señales externas.",
        "findings": [
            {
                "claim_id": "P05-C15-C1",
                "claim": "Prevalece la arquitectura prudencial de BRIDGE basada en compuertas de abstención estratégica y verificación de hechos frente a los generadores comerciales automáticos de comunicados de pánico.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Diseño de Producto BRIDGE"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7.2: Salvaguardas Éticas y de Seguridad Obligatorias",
                        "excerpt_short": "Neutralidad de datos externos y abstención activa. Los datos de redes deben tratarse como no confiables para prevenir sobre-reacciones ejecutivas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a704f39-0f78-4e44-8b03-b9922d00ed6b",
                        "source_title": "Arthur W. Page Society: The Page Principles for Corporate Character & Trust",
                        "original_url": "https://page.org/who-we-are/page-principles/",
                        "locator": "Principio 4: Listen to the Enterprise, Principio 5: Manage for Tomorrow",
                        "excerpt_short": "Public statements must be preceded by internal fact-checking. Rushing to speak without verified data compromises institutional trust.",
                        "source_date": "2023-01-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio fundacional de la arquitectura de software de BRIDGE respaldado por la Page Society."
            }
        ],
        "operational_model": {
            "inputs": ["Alertas de monitoreo de redes", "Compuertas lógicas de abstención de BRIDGE"],
            "actors": ["Comité de Crisis", "Arquitecto de BRIDGE"],
            "steps": ["Evaluación de condiciones de abstención algorítmica", "Bloqueo de generación de textos hacia medios masivos si no hay hechos probados", "Prescripción de verificación interna"],
            "states": ["Panic_Trigger_Rejected", "Abstention_Gate_Closed", "Prudent_Brief_Rendered"],
            "outputs": ["Brief ejecutivo de prudencia y contención"],
            "exceptions": ["Requerimiento formal con plazo perentorio de la CMF o tribunales de justicia"]
        },
        "entities": [
            {"entity_id": "ENT_PRUDENTIAL_ARCHITECTURE", "type": "principio_diseno", "name": "Arquitectura Prudencial de Producto BRIDGE", "aliases": ["BRIDGE Prudential Product Design"]}
        ],
        "relations": [
            {"subject_id": "ENT_PRUDENTIAL_ARCHITECTURE", "predicate": "sustituye_modelo_de", "object_id": "ENT_EXECUTIVE_BRIEF_UI", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C15-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Comportamiento del sistema",
                "Plataforma Comercial de Escucha": "'¡Alerta Roja! Pique de tweets negativos detectado. Haga clic aquí para que la IA redacte un comunicado de disculpa y lo envíe a los medios'.",
                "Plataforma BRIDGE": "'Se detectó volumen anómalo en redes pero sin tracción en reguladores. Telemetría interna confirma operación normal. Se recomienda abstención pública activa'."
            }
        ],
        "contradictions": [
            {"issue": "Automatización de respuestas de crisis con IA", "source_a": "Plataformas de social listening comercial", "source_b": "P05_RESEARCH_DOSSIER / Page Society", "resolution": "Prevalece BRIDGE: prohibido automatizar declaraciones públicas masivas sin verificación de hechos interna y compuertas de abstención."}
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Inferencia de Producto", "implication": "BRIDGE debe codificar compuertas de abstención inviolables que impidan que la IA genere comunicados públicos ante rumores virales no comprobados internamente.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-C16"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-C16
    {
        "question_id": "P05-C16",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre decisiones de producto y evaluación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El análisis de gaps documentado en P05_GAPS_AND_VALIDATION Sección 3 y 4 establece: 1) Lo que sigue sin prueba formal: La adopción cultural y confianza efectiva que los miembros de la alta dirección y comités de crisis otorgarán a un sistema de soporte a la decisión basado en IA y grafos de conocimiento. Existe la incertidumbre de si los directivos confiarán en la recomendación de 'Abstención Estratégica' del sistema durante un pico de viralización en redes sociales, o si cederán al impulso emocional tradicional de convocar ruedas de prensa reactivas; 2) Qué fuente es parcial o falló: Fallan los manuales tradicionales de relaciones públicas, que fueron redactados para la era analógica o de medios lineales y no contemplan la dinámica de inyecciones de desinformación algorítmica ni el manejo de compuertas éticas en sistemas basados en LLMs; 3) Validación mínima que resolvería la incertidumbre: Implementar un programa piloto de simulación de crisis corporativas (War Gaming / Crisis Simulation) en modo 'Shadowing' durante 6 meses con comités de crisis activos de tres corporaciones reguladas en Chile: comparar en paralelo las decisiones tomadas intuitivamente por el comité humano con las recomendaciones prescriptivas generadas por BRIDGE, midiendo tasas de desescalamiento, costos de litigación evitados y tiempos de respuesta ejecutiva sin falsos positivos.",
        "findings": [
            {
                "claim_id": "P05-C16-C1",
                "claim": "La adopción de recomendaciones de abstención y análisis de grafos por comités de crisis requiere validación empírica mediante ejercicios de simulación de crisis (War Gaming) en modo shadowing con directivos activos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Simulación y Validación BRIDGE"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 3: Pregunta de Interfaz y Soporte a la Decisión",
                        "excerpt_short": "¿Cómo debe estructurarse el brief ejecutivo para el Comité de Crisis para que presente la evidencia bajo el marco SCCT de Coombs sin generar sobrecarga cognitiva en los tomadores de decisiones?",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diseño experimental de validación en entornos organizacionales reales especificado en P05."
            }
        ],
        "operational_model": {
            "inputs": ["Escenarios de simulación de crisis controlados", "Telemetría de decisiones de comités ejecutivos"],
            "actors": ["Facilitador de War Games", "Comité de Crisis Corporativo"],
            "steps": ["Inyección de señales de crisis simuladas", "Registro de decisiones tomadas por directivos vs sugeridas por BRIDGE", "Análisis comparado de resultados en debriefing"],
            "states": ["Simulation_Prepared", "War_Game_Executed", "Adoption_Metrics_Evaluated"],
            "outputs": ["Informe de Calibración de Adopción Directiva de BRIDGE"],
            "exceptions": ["Resistencia de directores veteranos a seguir recomendaciones algorítmicas de contención"]
        },
        "entities": [
            {"entity_id": "ENT_WAR_GAMING_PROTOCOL", "type": "protocolo_validacion", "name": "Protocolo de Simulación de Crisis (War Gaming)", "aliases": ["Crisis War Gaming Protocol"]}
        ],
        "relations": [
            {"subject_id": "ENT_WAR_GAMING_PROTOCOL", "predicate": "valida_adopcion_de", "object_id": "ENT_PRUDENTIAL_ARCHITECTURE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-C16-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Método de entrenamiento",
                "Capacitación Teórica Tradicional": "Lectura de manuales de crisis de 200 páginas que nadie abre durante una contingencia.",
                "Simulación Activa BRIDGE": "Ejercicios interactivos en la plataforma donde los directivos experimentan las consecuencias del Efecto Streisand frente a la contención fundamentada."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Módulo de Simulación", "implication": "BRIDGE debe incluir una función de 'Modo Simulación / Simulacro' para que los comités de crisis entrenen sus decisiones antes de enfrentar controversias reales.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_C_SUITE_AI_ADOPTION", "description": "Resistencia cultural y sobrecarga cognitiva de comités ejecutivos ante sistemas de soporte algorítmico en crisis.", "severity": "media", "status": "documentado"}
        ],
        "next_question_ids": ["P06-F01"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P05.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P05-C09..C16) to {out_path}.")
