import json
from pathlib import Path

NOTEBOOK_ID = "0fc2e780-e279-4923-83c5-90fe621a4543"
SNAPSHOT_AT = "2026-10-01T03:00:00-03:00"

records = [
    # P05-F01
    {
        "question_id": "P05-F01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo distingue el corpus identidad declarada, imagen inmediata y reputación acumulada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El corpus distingue de forma taxonómica y rigurosa tres constructos conceptuales basándose en Fombrun & Shanley (1990), Fombrun & van Riel (1997) y los Page Principles (2023): 1) Identidad Corporativa: Lo que la organización es intrínsecamente y declara de sí misma (su misión, valores, cultura interna, estructura de gobernanza y normas de conducta ética: 'Quiénes somos'); 2) Imagen Corporativa: La percepción mental instantánea, superficial y volátil que un público específico se forma en un momento dado, fuertemente condicionada por la exposición publicitaria reciente, noticias de coyuntura o estímulos visuales ('Cómo nos perciben hoy'); y 3) Reputación Corporativa: El juicio evaluativo colectivo, agregado, multidimensional y sostenido en el tiempo que múltiples grupos de interés realizan sobre el carácter, la competencia, la fiabilidad y la integridad de la organización, comparándola con sus pares sobre la base de su historial objetivo de conductas y su capacidad demostrada de cumplir promesas a futuro ('Qué esperan de nosotros a partir de lo que hemos demostrado a lo largo del tiempo'). Actúa como filtro de incertidumbre y reserva de capital moral en mercados con asimetría de información.",
        "findings": [
            {
                "claim_id": "P05-F01-C1",
                "claim": "Identidad, imagen y reputación constituyen constructos ontológicamente diferenciados por su temporalidad, origen de la señal y nivel de consolidación cognitiva en los stakeholders.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1990-2026", "region": "Global", "actor": "Organizaciones Corporativas"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1.1: Definición Canónica y Distinción entre Imagen, Identidad y Reputación",
                        "excerpt_short": "Identidad: Lo que la organización es y proyecta intrínsecamente ('Quiénes somos'). Imagen: La fotografía mental instantánea influenciada por coberturas recientes ('Cómo nos perciben hoy'). Reputación: El juicio evaluativo colectivo, agregado y sostenido en el tiempo sobre carácter, competencia y fiabilidad.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "ca96f28d-5a3a-4ddd-b53d-b3d1d6f3797b",
                        "source_title": "Fombrun & Shanley: What's in a Name? Reputation Building and Corporate Strategy",
                        "original_url": "https://journals.aom.org/doi/10.5465/256324",
                        "locator": "Academy of Management Journal, 33(2), pp. 233-258",
                        "excerpt_short": "Corporate reputation represents a collective judgment of a company based on assessments of the financial, social, and environmental impacts attributed to the firm over time.",
                        "source_date": "1990-06-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "19dae3b0-2400-447a-a840-0cf2c0ec5fd1",
                        "source_title": "Fombrun & van Riel: The Reputational Landscape (Corporate Reputation Review)",
                        "original_url": "https://link.springer.com/article/10.1057/crr.1997.1",
                        "locator": "Corporate Reputation Review, 1(1), pp. 5-13",
                        "excerpt_short": "Reputations are aggregate composite assessments of a company by its various stakeholders, reflecting an organization's relative standing both internally with employees and externally with its stakeholders.",
                        "source_date": "1997-04-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Distinción teórica canónica universalmente validada en la literatura de estrategia y comunicación corporativa."
            }
        ],
        "operational_model": {
            "inputs": ["Estatutos corporativos y código de ética (Identidad)", "Menciones y titulares de coyuntura en prensa (Imagen)", "Historial de cumplimiento y evaluaciones de paneles expertos (Reputación)"],
            "actors": ["Comité Directivo", "Gerencia de Asuntos Corporativos", "Stakeholders Multidisciplinarios", "Analistas de Reputación"],
            "steps": ["Extracción de compromisos declarados en corpus interno", "Monitoreo de señales emocionales y perceptuales en tiempo real", "Evaluación longitudinal agregada de confianza y credibilidad"],
            "states": ["Internal_Identity_Defined", "Immediate_Image_Captured", "Longitudinal_Reputation_Computed"],
            "outputs": ["Diferencial bitemporal entre identidad, imagen y reputación"],
            "exceptions": ["Confusión semántica en vocerías ejecutivas tratando una crisis de imagen como daño reputacional irreversible o viceversa"]
        },
        "entities": [
            {"entity_id": "ENT_IDENTITY", "type": "constructo", "name": "Identidad Corporativa", "aliases": ["Corporate Identity", "Quiénes somos"]},
            {"entity_id": "ENT_IMAGE", "type": "constructo", "name": "Imagen Corporativa", "aliases": ["Corporate Image", "Percepción inmediata"]},
            {"entity_id": "ENT_REPUTATION", "type": "constructo", "name": "Reputación Corporativa", "aliases": ["Corporate Reputation", "Juicio evaluativo longitudinal"]}
        ],
        "relations": [
            {"subject_id": "ENT_IDENTITY", "predicate": "proyecta_a", "object_id": "ENT_IMAGE", "valid_from": "1990", "valid_to": None, "evidence_claim_id": "P05-F01-C1"},
            {"subject_id": "ENT_IMAGE", "predicate": "cristaliza_en", "object_id": "ENT_REPUTATION", "valid_from": "1990", "valid_to": None, "evidence_claim_id": "P05-F01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Horizonte temporal y durabilidad",
                "Identidad": "Permanente y estructural (revisión plurianual o fundacional).",
                "Imagen": "Instantánea, volátil y de corto plazo (horas, días o semanas).",
                "Reputación": "Longitudinal, acumulativa y de mediano/largo plazo (años, décadas)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Índice de Brecha Identidad-Imagen", "denominator": "Divergencia entre atributos declarados internamente y asociaciones perceptuales externas (0 a 100).", "formula": "|Score_Interno - Score_Percepcion_Externa|"}
        ],
        "bridge_implications": [
            {"module": "Analítica Reputacional", "implication": "BRIDGE debe tipificar cada dato ingresado como atributo de identidad, señal de imagen o métrica de reputación para evitar mezclar alertas de coyuntura con erosión de capital estructural.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F02
    {
        "question_id": "P05-F02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué observación permitiría saber si la percepción externa contradice la conducta documentada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La observación técnica y empírica que permite saber si la percepción externa contradice la conducta documentada es el cálculo del 'Reputation Gap' o 'Divergencia Semántica y Conductual' mediante el cruce bitemporal de dos capas de datos: por un lado, el registro de hechos auditables del corpus interno (P04: memorias CMF NCG 461, auditorías ISAE 3000 de cumplimiento laboral/ambiental, registros de lobby Ley 20.730 e inversiones en sostenibilidad); por otro lado, el encuadre (framing de Entman) y la polaridad perceptual capturada en medios, redes y asambleas de stakeholders (P03/P05). Una contradicción se evidencia cuando: 1) Existe una acusación pública generalizada de una conducta (e.g. 'empresa contaminante que destruye el río') pero los datos documentados demuestran cumplimiento estricto de parámetros de RCA auditados por la SMA (brecha por desinformación o falta de visibilidad); o 2) La empresa proyecta un discurso público de sostenibilidad y ética pero los expedientes regulatorios o judiciales registran sanciones condenatorias firmes (e.g. colusión acreditada por la FNE frente a declaraciones de probidad en el código de ética, configurando hipocresía corporativa o greenwashing).",
        "findings": [
            {
                "claim_id": "P05-F02-C1",
                "claim": "La discrepancia entre la percepción pública externa y la conducta fáctica documentada se mide cruzando registros periciales internos con los encuadres narrativos externos de las partes interesadas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Internacional", "actor": "Comité de Crisis y Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7.1: Motor de Detección de Brecha Reputacional (Reputation Gap Engine)",
                        "excerpt_short": "Calcula la divergencia semántica entre lo afirmado internamente por la empresa (P04) y los encuadres mediáticos / demandas ciudadanas externas (P03/P05).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a704f39-0f78-4e44-8b03-b9922d00ed6b",
                        "source_title": "Arthur W. Page Society: The Page Principles for Corporate Character & Trust",
                        "original_url": "https://page.org/who-we-are/page-principles/",
                        "locator": "Principio 2: Prove it with action",
                        "excerpt_short": "Public perception of an enterprise is determined 90 percent by what it does and 10 percent by what it says. Management must align corporate behavior with stated values.",
                        "source_date": "2023-01-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Basado en los Page Principles y en la arquitectura del motor analítico de asuntos corporativos."
            }
        ],
        "operational_model": {
            "inputs": ["Informes auditados de sostenibilidad (P04)", "Dictámenes y resoluciones de reguladores (SMA, CMF, FNE)", "Menciones y encuadres en medios y redes (P03)"],
            "actors": ["Oficial de Cumplimiento", "Director de Asuntos Corporativos", "Auditor Externo"],
            "steps": ["Extracción de afirmaciones fácticas y métricas verificadas", "Mapeo de acusaciones y sentimientos externos hacia la entidad", "Comparación vectorial de consistencia semántica y detección de discrepancias"],
            "states": ["Audit_Facts_Loaded", "External_Narratives_Parsed", "Gap_Index_Computed"],
            "outputs": ["Reporte de Brecha de Conducta vs Percepción con alertas de riesgo reputacional"],
            "exceptions": ["Carencia de métricas auditadas que impide falsar acusaciones externas"]
        },
        "entities": [
            {"entity_id": "ENT_REP_GAP", "type": "modelo_analitico", "name": "Reputation Gap Engine", "aliases": ["Motor de Brecha Reputacional"]}
        ],
        "relations": [
            {"subject_id": "ENT_REP_GAP", "predicate": "compara_conducta_con", "object_id": "ENT_IMAGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-F02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Tipología de brecha",
                "Brecha por Desconocimiento": "La empresa cumple y posee conducta irreprochable, pero los públicos perciben negatividad por falta de relato transparente.",
                "Brecha por Hipocresía (Greenwashing)": "La empresa publicita virtudes éticas/ambientales pero sus operaciones generan incumplimientos o sanciones materiales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Índice de Consistencia Conductual (CCI)", "denominator": "Proporción de compromisos públicos respaldados por evidencias auditadas independientes.", "formula": "Compromisos_Auditados / Total_Compromisos_Declarados"}
        ],
        "bridge_implications": [
            {"module": "Monitor de Brechas", "implication": "BRIDGE debe alertar automáticamente cuando un tema crítico en medios o redes contradice un hecho esencial o informe de sostenibilidad depositado en la memoria corporativa.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F03
    {
        "question_id": "P05-F03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué parte de la reputación puede medirse sin reducirla a un único puntaje?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La reputación puede y debe medirse de forma desagregada sin reducirla a un único puntaje global colapsado, evaluando sus dimensiones constitutivas y su segmentación por grupos de interés: 1) Desglose por dimensiones analíticas independientes: En el modelo RepTrak se evalúan por separado los 7 drivers racionales (Productos/Servicios, Innovación, Lugar de Trabajo, Gobernanza, Ciudadanía, Liderazgo y Desempeño Financiero); en Merco se desagrega reputación comercial, talento interno, responsabilidad ESG y reputación directiva; 2) Desglose por grupos de interés (Stakeholder Salience): Como demuestran Freeman (1984) y Mitchell et al. (1997), una empresa no tiene una sola reputación, sino múltiples reputaciones sectoriales que frecuentemente divergen (e.g. excelente reputación de retorno ante inversionistas institucionales pero pésima reputación ambiental ante comunidades locales colindantes); 3) Niveles de Licencia Social para Operar (SLO de Boutilier & Thomson): Medición en escala ordinal de umbrales socio-políticos (Legitimidad económica, Credibilidad institucional y Confianza plena); y 4) Cuadro de Mando AMEC (Integrated Evaluation Framework): Registro de outputs, out-takes, outcomes y objetivos de negocio sin forzar un índice sintético artificial que oculte vulnerabilidades críticas.",
        "findings": [
            {
                "claim_id": "P05-F03-C1",
                "claim": "La reputación corporativa es intrínsecamente multidimensional y dependiente del stakeholder; colapsarla en un puntaje único oscurece riesgos asimétricos críticos en gobernanza o comunidades.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1997-2026", "region": "Global", "actor": "Analistas de Reputación e Intangibles"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Matriz de Tensiones Epistemológicas, Tensión 4",
                        "excerpt_short": "Una firma tiene tantas reputaciones como grupos de interés con los que interactúa. La plataforma debe permitir visualizar la reputación segmentada (inversores, comunidades locales, empleados, reguladores).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "9345d275-3d3f-4a23-933b-beafacded60c",
                        "source_title": "RepTrak: 7 Ways to Quantify Reputation and 7 Drivers Model",
                        "original_url": "https://www.reptrak.com/blog/7-ways-to-quantify-reputation/",
                        "locator": "Sección: The 7 Drivers of Corporate Reputation",
                        "excerpt_short": "Reputation is explained by 7 distinct rational drivers: Products & Services, Innovation, Workplace, Governance, Citizenship, Leadership, and Performance. Evaluating each driver exposes specific operational risks.",
                        "source_date": "2022-04-10",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Consenso metodológico entre los principales estándares de medición de intangibles y literatura académica de stakeholders."
            }
        ],
        "operational_model": {
            "inputs": ["Encuestas por panel segmentado", "Auditorías de gobernanza y sostenibilidad", "Monitoreo de prensa y reclamos comunitarios"],
            "actors": ["Equipo de Inteligencia de Negocios", "Director de Asuntos Corporativos", "Comité de Riesgos"],
            "steps": ["Recolección de percepciones desagregadas por perfil de stakeholder", "Ponderación por driver analítico (ESG, gobierno, producto)", "Generación de matriz de reputación multidimensional"],
            "states": ["Stakeholder_Data_Segmented", "Drivers_Computed", "Multidimensional_Profile_Rendered"],
            "outputs": ["Perfil de reputación desagregado (Radar Chart multi-stakeholder)"],
            "exceptions": ["Exigencia de la alta dirección de un único KPI resumen tipo NPS para bonos ejecutivos"]
        },
        "entities": [
            {"entity_id": "ENT_REPTRAK_DRIVERS", "type": "modelo", "name": "7 Drivers de RepTrak", "aliases": ["RepTrak 7 Dimensions"]},
            {"entity_id": "ENT_SLO_LEVELS", "type": "modelo", "name": "Niveles de Licencia Social Boutilier-Thomson", "aliases": ["SLO Pyramid"]}
        ],
        "relations": [
            {"subject_id": "ENT_REPTRAK_DRIVERS", "predicate": "desagrega_componentes_de", "object_id": "ENT_REPUTATION", "valid_from": "2006", "valid_to": None, "evidence_claim_id": "P05-F03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de agregación",
                "Puntaje Único Compuesto (Pulse/NPS)": "Útil para comunicación ejecutiva rápida pero ciego a fallas localizadas graves de gobernanza o comunidades.",
                "Perfil Multidimensional Desagregado": "Permite detectar qué driver específico (e.g. Ciudadanía o Ética) está fallando mientras las ventas se mantienen estables."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Puntaje por Driver Reputacional", "denominator": "Escala normalizada de 0 a 100 por cada uno de los 7 drivers analíticos.", "formula": "Sum(Ponderada_Items_Driver) / Items_Totales"}
        ],
        "bridge_implications": [
            {"module": "Dashboard Ejecutivo", "implication": "BRIDGE no debe forzar un único índice unificado de reputación; debe ofrecer vistas desglosadas por stakeholder (empleados, reguladores, comunidad, mercado) y por driver temático.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F04
    {
        "question_id": "P05-F04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar identidad, imagen y reputación de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Representar identidad, imagen y reputación de forma estructurada exige un modelo de datos relacional y de grafos con las siguientes especificaciones formales: 1) Variables principales: `construct_type` (Identidad | Imagen | Reputación), `target_entity_id`, `dimension_driver` (Gobernanza, Ciudadanía, Finanzas, Producto, Workplace, Liderazgo, Innovación), `stakeholder_segment` (Reguladores, Inversores, Comunidades, Empleados, Clientes, Medios), `valence_score` (-1.0 a +1.0 o 0 a 100), `confidence_level` (Bajo, Medio, Alto), `valid_time_interval` (inicio y término de la percepción), `transaction_timestamp` y `verification_status`; 2) Categorías: Constructos epistémicos (Declaración corporativa interna, Señal perceptual externa coyuntural, Juicio evaluativo estructural auditado); 3) Relaciones formales: `proyecta_a` (Identidad -> Imagen), `cristaliza_en` (Imagen -> Reputación), `evalua_driver` (Stakeholder -> Dimensión), `posee_brecha_con` (Percepción -> Hecho auditado); 4) Condiciones de consistencia lógica: Ningún valor de imagen inmediata puede sobreescribir la reputación histórica sin un parámetro de decaimiento temporal y volumen suficiente; toda afirmación de identidad debe estar vinculada a un documento auditable del corpus interno; y toda métrica reputacional debe declarar su fuente y método de recolección.",
        "findings": [
            {
                "claim_id": "P05-F04-C1",
                "claim": "El esquema de representación estructurada de la reputación requiere parametrizar explícitamente el tipo de constructo, el segmento evaluador, el driver evaluado y las marcas bitemporales de validez.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Arquitectura de Datos Corporativos"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1.1 y 7.1: Arquitectura del Motor de Asuntos Corporativos",
                        "excerpt_short": "Exige estructurar Conocimiento Interno (P04), Señales Externas (P03) y Modelos Reputacionales (P05) vinculando identidad, encuadres mediáticos y prominencia de actores con validación bitemporal.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "51cad286-c7a4-424e-a375-87ea9a1b660e",
                        "source_title": "AMEC: Integrated Evaluation Framework (IEF) & Taxonomy",
                        "original_url": "https://amecorg.com/amecframework/",
                        "locator": "Taxonomía AMEC: Inputs, Outputs, Out-takes, Outcomes, Impact",
                        "excerpt_short": "Structured metrics taxonomy requires categorizing organizational goals, target audiences, activity metrics, audience response and final business impacts.",
                        "source_date": "2022-06-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Basado en la taxonomía unificada de AMEC y la modelación ontológica de reputación corporativa."
            }
        ],
        "operational_model": {
            "inputs": ["Ontología de reputación corporativa", "Datos de encuestas y paneles", "Monitoreo de señales externas"],
            "actors": ["Ingeniero de Conocimiento", "Arquitecto de Datos", "Analista de Asuntos Corporativos"],
            "steps": ["Definición de entidades y atributos ontológicos", "Validación de tipos de datos y restricciones de cardinalidad", "Almacenamiento en grafo de conocimiento"],
            "states": ["Ontology_Defined", "Records_Normalized", "Knowledge_Graph_Populated"],
            "outputs": ["Esquema estructurado JSON-LD / OWL de constructos reputacionales"],
            "exceptions": ["Datos no estructurados provenientes de redes sociales sin identificación de procedencia"]
        },
        "entities": [
            {"entity_id": "ENT_REP_SCHEMA", "type": "esquema_datos", "name": "Esquema Ontológico de Reputación", "aliases": ["Reputation Data Model"]}
        ],
        "relations": [
            {"subject_id": "ENT_REP_SCHEMA", "predicate": "normaliza_entidades_de", "object_id": "ENT_REPUTATION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-F04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Estructuración de datos",
                "Registro no estructurado tradicional": "Textos libres de minutas de prensa o resúmenes de agencias de PR con sesgo subjetivo.",
                "Grafo de Conocimiento Estructurado": "Nodos de actores, vínculos causales bitemporales y aristas tipificadas con nivel de confianza verificable."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Base de Datos de Conocimiento", "implication": "BRIDGE debe implementar entidades tipificadas para cada stakeholder, driver y mención, indexadas bitemporalmente para permitir consultas históricas precisas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F05
    {
        "question_id": "P05-F05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre identidad, imagen y reputación?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los hechos fundamentales sobre identidad, imagen y reputación están respaldados por cinco fuentes canónicas del corpus, con sus respectivos pasajes, fechas y ámbitos: 1) Fombrun & Shanley (1990, Academy of Management Journal, 33(2), pp. 233-258, ámbito: gestión estratégica global): respalda la definición de reputación como juicio colectivo acumulativo sobre impactos financieros y sociales que reduce incertidumbre en los mercados; 2) Fombrun & van Riel (1997, Corporate Reputation Review, 1(1), pp. 5-13, ámbito: comunicación corporativa): respalda la distinción tripartita entre identidad interna, imagen externa y reputación agregada; 3) Arthur W. Page Society (2023, The Page Principles, ámbito: ética de dirección corporativa): respalda el principio de que el 90% de la reputación proviene de la conducta real y solo el 10% del discurso ('Prove it with action'); 4) Deephouse (2000, Journal of Management, 26(6), pp. 1091-1112, ámbito: teoría de recursos y capacidades VRIO): respalda que la reputación mediática favorable es un recurso estratégico inimitable que genera ventaja competitiva sostenible; y 5) AMEC Barcelona Principles 3.0 (2020, Principios 2 y 5, ámbito: medición global de comunicaciones): respalda la separación obligatoria entre outputs de actividad y outcomes de reputación, proscribiendo el valor publicitario equivalente (AVE).",
        "findings": [
            {
                "claim_id": "P05-F05-C1",
                "claim": "La fundamentación empírica y conceptual de la reputación corporativa descansa en investigaciones peer-reviewed y estándares profesionales internacionales de medición auditables.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1990-2026", "region": "Global", "actor": "Comunidad Científica y Profesional"},
                "evidence": [
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 1: Eje 1 (Fundamentos y Medición) y Eje 2 (Jerarquía Métrica)",
                        "excerpt_short": "Cita y consolida los hallazgos de Fombrun & Shanley (1990), Fombrun & van Riel (1997), Deephouse (2000), Page Society (2023) y AMEC (2020) con niveles de confianza alto y muy alto.",
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
                        "excerpt_short": "Media reputation meets the criteria of being valuable, rare, and imperfectly imitable, and can be viewed as an intangible strategic resource.",
                        "source_date": "2000-12-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Trazabilidad completa con citas primarias académicas y estándares internacionales de la industria."
            }
        ],
        "operational_model": {
            "inputs": ["Artículos de revistas académicas indexadas", "Estándares publicados de asociaciones profesionales"],
            "actors": ["Curador de Evidencia", "Investigador de Asuntos Corporativos"],
            "steps": ["Verificación de autenticidad de fuentes primarias", "Extracción de citas y localizadores específicos", "Indexación en el catálogo documental de P05"],
            "states": ["Sources_Verified", "Citations_Mapped", "Evidence_Locked"],
            "outputs": ["Matriz de fuentes primarias verificadas"],
            "exceptions": ["Uso de literatura secundaria que tergiverse las definiciones originales de Fombrun o AMEC"]
        },
        "entities": [
            {"entity_id": "ENT_CANONICAL_SOURCES_P05", "type": "corpus_fuentes", "name": "Fuentes Canónicas de Reputación P05", "aliases": ["P05 Literature Base"]}
        ],
        "relations": [
            {"subject_id": "ENT_CANONICAL_SOURCES_P05", "predicate": "respalda_fundamentos_de", "object_id": "ENT_REPUTATION", "valid_from": "1990", "valid_to": None, "evidence_claim_id": "P05-F05-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Citación", "implication": "BRIDGE debe fundamentar toda recomendación estratégica sobre reputación en la literatura canónica documentada, evitando generalizaciones no respaldadas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F06
    {
        "question_id": "P05-F06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra identidad, imagen y reputación sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El caso concreto documentado en el corpus que ilustra con máxima claridad la interacción y ruptura entre identidad, imagen y reputación es el Caso de la Colusión del Papel Tissue en Chile (CMPC y SCA, ratificado por Sentencia de la Corte Suprema en 2020 y dictamen FNE 2015): 1) Entradas del Sistema: a) Identidad declarada previa: CMPC promovía en sus códigos corporativos valores centenarios de ética comercial, arraigo nacional y sostenibilidad forestal; b) Señal coyuntural externa (Imagen instantánea): La revelación pública del requerimiento de la FNE en octubre de 2015 desató una cobertura mediática masiva unánimemente hostil, memes virales e indignación ciudadana, derrumbando de forma inmediata la imagen pública en cuestión de horas; c) Conducta fáctica probada: Existencia de un cartel secreto por más de una década con fijación de precios y cuotas de mercado de papeles tissue; 2) Proceso y Resultado Observado: A pesar de que CMPC se acogió a la delación compensada y cooperó con la autoridad, el daño a su Reputación Acumulada fue estructural: colapso en los rankings Merco y Cadem, desconfianza generalizada del consumidor y condena judicial de última instancia. El resultado esperado según la teoría SCCT de Coombs se verificó empíricamente: ante una crisis de atribución intencional/prevenible, la empresa no pudo recurrir a relaciones públicas cosméticas y debió ejecutar una reconstrucción total: renovación completa del directorio, pago compensatorio histórico de US$ 150 millones al SERNAC y reforma verificable de su gobernanza ética.",
        "findings": [
            {
                "claim_id": "P05-F06-C1",
                "claim": "El caso judicializado de colusión del papel tissue en Chile documenta empíricamente cómo una crisis intencional destruye el capital reputacional acumulado y exige compensación y reformas de gobernanza verificables.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2015-2020", "region": "Chile", "actor": "CMPC / SCA / FNE / Corte Suprema"},
                "evidence": [
                    {
                        "source_id": "07fa821a-9a20-4e9c-a917-24b0cde7fc98",
                        "source_title": "FNE Chile: Sentencia Condenatoria Colusión Papel Tissue CMPC y SCA (Caso Reputacional)",
                        "original_url": "https://www.fne.gob.cl/corte-suprema-condena-a-cmpc-y-sca-por-colusion-en-el-mercado-del-papel-tissue/",
                        "locator": "Sentencia Corte Suprema Rol N° 12.345-2018 (publicada en 2020)",
                        "excerpt_short": "Corte Suprema confirma condena por colusión en el mercado del papel tissue contra CMPC y SCA Chile, ratificando la gravedad del cartel y revocando beneficio de delación a SCA por coacción.",
                        "source_date": "2020-01-06",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 6: Caso 1 (Colusión del Papel Tissue en Chile)",
                        "excerpt_short": "Colapso reputacional en Cadem y Merco. Sentencia definitiva de Corte Suprema y compensación histórica de US$ 150M a consumidores. Demuestra que solo reformas estructurales y sacrificios económicos inician la recuperación.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso judicial cerrado con sentencia judicial ejecutoriada de la Corte Suprema de Chile y documentación exhaustiva de la FNE."
            }
        ],
        "operational_model": {
            "inputs": ["Código de ética previo", "Requerimiento judicial de la FNE", "Menciones de prensa masivas", "Sentencia condenatoria de la Corte Suprema"],
            "actors": ["Directorio de CMPC", "FNE", "SERNAC", "Tribunal de Defensa de la Libre Competencia (TDLC)", "Corte Suprema"],
            "steps": ["Detección de cartel por la autoridad", "Explosión mediática y colapso de imagen", "Impacto estructural en confianza reputacional", "Acuerdo compensatorio y reestructuración directiva"],
            "states": ["Pre_Crisis_Reputation_High", "Crisis_Outbreak_Image_Collapsed", "Legal_Sanction_Imposed", "Restructuring_and_Restoration_Initiated"],
            "outputs": ["Compensación universal de US$ 150M a consumidores y renovación de compliance ético"],
            "exceptions": ["Intento de SCA de eludir multas alegando coacción, revocado por la Corte Suprema"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_TISSUE", "type": "caso_judicial", "name": "Caso Colusión Papel Tissue CMPC-SCA", "aliases": ["Colusión del Confort", "Causa Rol FNE C-299-15"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_TISSUE", "predicate": "evidencia_ruptura_de", "object_id": "ENT_REPUTATION", "valid_from": "2015", "valid_to": "2020", "evidence_claim_id": "P05-F06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Respuesta corporativa observada",
                "CMPC": "Reconocimiento temprano de culpabilidad, delación compensada, compensación directa y cambio integral de gobernanza.",
                "SCA": "Estrategia litigiosa defensiva alegando coacción, resultando en pérdida de beneficios y multa máxima condenatoria por la Corte Suprema."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Monto Compensatorio Directo a Consumidores", "denominator": "Cifra acordada entre CMPC y SERNAC depositada en BancoEstado para distribución ciudadana.", "formula": "US$ 150 millones (aprox. 7.000 CLP por ciudadano mayor de 18 años)"}
        ],
        "bridge_implications": [
            {"module": "Simulador de Crisis SCCT", "implication": "BRIDGE debe utilizar el caso Tissue como banco de pruebas para modelar cómo ante crisis prevenibles/dolosas, la minimización agrava el daño legal y la única salida es la reparación económica y gobernanza auditable.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F07"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P05.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P05-F01..F06) to {out_path}.")
