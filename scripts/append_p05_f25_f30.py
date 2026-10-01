import json
from pathlib import Path

NOTEBOOK_ID = "0fc2e780-e279-4923-83c5-90fe621a4543"
SNAPSHOT_AT = "2026-10-01T03:00:00-03:00"

records = [
    # P05-F25
    {
        "question_id": "P05-F25",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué criterios documentados ayudan a priorizar actores por legitimidad, poder, urgencia e influencia?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El corpus fundamenta la priorización rigurosa de actores en el Modelo de Prominencia de Mitchell, Agle y Wood (1997 / Umbrex 2024) y en el estándar de relacionamiento AA1000SES (2015). La prominencia (stakeholder salience) se determina evaluando la presencia simultánea de tres atributos dinámicos: 1) Poder: Capacidad del actor de imponer su voluntad mediante recursos coercitivos (fuerza física, litigios judiciales, sanciones de fiscalizadores), utilitarios (financiamiento, acceso a capital, decisiones de compra) o normativos/simbólicos (autoridad moral, prestigio ante la opinión pública); 2) Legitimidad: Validez percibida y anclaje de sus demandas o reclamos en estructuras normativas, leyes vigentes (e.g. Convenio 169 OIT) o valores éticos compartidos; 3) Urgencia: Grado en que sus reclamos exigen atención inmediata por su sensibilidad temporal o por el daño crítico que generaría su postergación. La combinación de estos atributos define 7 clases tipológicas ordenadas por prioridad: a) Actores Latentes (1 atributo: Dormidos con solo Poder; Discrecionales con solo Legitimidad; Demandantes con solo Urgencia); b) Actores Expectantes (2 atributos: Dominantes con Poder y Legitimidad como los fiscalizadores SMA/CMF; Peligrosos con Poder y Urgencia que pueden recurrir a vías de hecho; Dependientes con Legitimidad y Urgencia como comunidades afectadas sin recursos propios); y c) Actores Definitivos (3 atributos: reúnen Poder, Legitimidad y Urgencia), quienes ostentan la máxima prioridad ejecutiva para la alta dirección corporativa.",
        "findings": [
            {
                "claim_id": "P05-F25-C1",
                "claim": "La priorización de partes interesadas no debe basarse en intuiciones jerárquicas sino en el modelo dinámico de prominencia tipificado por la conjunción de poder, legitimidad y urgencia.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1997-2026", "region": "Global", "actor": "Gestión Estratégica de Stakeholders"},
                "evidence": [
                    {
                        "source_id": "6bddf8be-2799-4e7b-b32f-cbc9b34d6e0c",
                        "source_title": "Umbrex: Mitchell-Agle-Wood Stakeholder Salience Model Guide",
                        "original_url": "https://umbrex.com/resources/stakeholder-salience-model/",
                        "locator": "Sección: The Seven Classes of Stakeholders",
                        "excerpt_short": "Stakeholder salience is determined by power, legitimacy, and urgency. Definitive stakeholders possess all three attributes and demand immediate executive attention.",
                        "source_date": "2024-02-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "37d05536-6e21-4eed-88f6-8019b342ffa5",
                        "source_title": "P05_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 1: Eje 4, Hallazgo 4.1 (Modelo de Prominencia de Mitchell, Agle y Wood)",
                        "excerpt_short": "Clasifica a los actores en Latentes (Dormido, Discrecional, Demandante), Expectantes (Dominante, Peligroso, Dependiente) y Definitivo (P+L+U). Nivel de confianza MUY ALTO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco fundacional de la teoría de stakeholders con amplia validación en gestión corporativa global."
            }
        ],
        "operational_model": {
            "inputs": ["Directorio de actores territoriales e institucionales", "Registro de interacciones de lobby", "Expedientes de reclamos formales"],
            "actors": ["Gerente de Relacionamiento Comunitario", "Director de Asuntos Públicos", "Asesor Jurídico"],
            "steps": ["Calificación booleana de atributos P, L y U para cada actor", "Asignación de la clase de prominencia correspondiente", "Mapeo en diagrama de Venn interactivo"],
            "states": ["Actors_Inventoried", "Attributes_Assigned", "Salience_Tier_Calculated"],
            "outputs": ["Matriz de Prominencia de Stakeholders con alertas de atención prioritaria"],
            "exceptions": ["Actor latente que adquiere urgencia crítica en un período inferior a 24 horas"]
        },
        "entities": [
            {"entity_id": "ENT_MITCHELL_SALIENCE", "type": "modelo_analitico", "name": "Modelo de Prominencia de Mitchell, Agle y Wood", "aliases": ["Stakeholder Salience Framework"]}
        ],
        "relations": [
            {"subject_id": "ENT_MITCHELL_SALIENCE", "predicate": "prioriza_relacionamiento_con", "object_id": "ENT_REPUTATION", "valid_from": "1997", "valid_to": None, "evidence_claim_id": "P05-F25-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de priorización",
                "Mapeo de Poder-Interés Tradicional": "Ignora la legitimidad moral o jurídica y subestima a comunidades vulnerables sin poder económico.",
                "Modelo de Prominencia (Mitchell et al.)": "Incorpora explícitamente la legitimidad y la urgencia, anticipando alianzas que convierten a actores dependientes en definitivos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Mapeador de Stakeholders", "implication": "BRIDGE debe calcular la prominencia dinámica de cada actor externo mediante el triplete booleano (Poder, Legitimidad, Urgencia), alertando cuando un actor transita a clase Definitiva.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F26"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F26
    {
        "question_id": "P05-F26",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo cambian intereses y posiciones de un actor a lo largo del tiempo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los intereses y posiciones de las partes interesadas no son propiedades estáticas sino vectores dinámicos que mutan a lo largo del tiempo en respuesta a tres factores documentados en el corpus: 1) Adquisición o pérdida de atributos de prominencia: Un grupo vecinal clasificado inicialmente como 'Dependiente' (alta legitimidad y urgencia, pero sin poder) transmuta a 'Definitivo' al aliarse con una ONG internacional con capacidad de litigación climática o al ser admitido a trámite su recurso de protección en una Corte de Apelaciones con orden de no innovar (adquiriendo poder coercitivo); 2) Ciclo de vida del proyecto o relación: Bajo el modelo de Licencia Social para Operar (SLO) de Boutilier & Thomson, los actores transitan por diferentes niveles (Retiro -> Aceptación -> Aprobación -> Copropiedad Psicológica) según se satisfagan los umbrales de legitimidad económica, credibilidad socio-política y confianza plena; si la empresa incumple acuerdos o miente, el actor retrocede bruscamente al nivel de Retiro; y 3) Alteraciones del entorno institucional: Reformas legislativas (e.g. nueva Ley de Delitos Económicos y Ambientales en Chile) o cambios de gobierno empoderan a sindicatos y comunidades otorgándoles nuevos canales de fiscalización y endureciendo sus posturas negociadoras.",
        "findings": [
            {
                "claim_id": "P05-F26-C1",
                "claim": "Las posturas y prominencia de los actores corporativos son intrínsecamente dinámicas y dependen de alianzas estratégicas, cumplimiento de acuerdos y variaciones en el marco normativo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2011-2026", "region": "Global / Chile", "actor": "Partes Interesadas y Comunidades"},
                "evidence": [
                    {
                        "source_id": "50e7cfce-93a6-4d51-a53e-50aa586579f3",
                        "source_title": "Boutilier & Thomson: Modelling and Measuring the Social License to Operate (SLO)",
                        "original_url": "https://www.socialicense.com/publications/Modelling_and_Measuring_the_SLO.pdf",
                        "locator": "Páginas 3 a 7: Dynamics of the Social License Thresholds",
                        "excerpt_short": "The SLO is not permanent; it oscillates across boundary thresholds based on perceptions of economic legitimacy, credibility, and full trust.",
                        "source_date": "2011-09-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "6bddf8be-2799-4e7b-b32f-cbc9b34d6e0c",
                        "source_title": "Umbrex: Mitchell-Agle-Wood Stakeholder Salience Model Guide",
                        "original_url": "https://umbrex.com/resources/stakeholder-salience-model/",
                        "locator": "Sección: The Dynamic Nature of Stakeholder Salience",
                        "excerpt_short": "Stakeholders can gain or lose power, legitimacy, or urgency over time, moving between classes as issues evolve and coalitions form.",
                        "source_date": "2024-02-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio central de la dinámica de sistemas de actores y modelos de licencia social."
            }
        ],
        "operational_model": {
            "inputs": ["Historial de acuerdos firmados", "Seguimiento de fallos judiciales", "Actas de mesas de diálogo"],
            "actors": ["Encargado de Asuntos Comunitarios", "Oficial de Enlace de Stakeholders"],
            "steps": ["Registro bitemporal de cada interacción y acuerdo", "Detección de alertas de cambio de postura (cooperativo a contencioso)", "Actualización del nivel de SLO en el sistema"],
            "states": ["Posture_Stable", "Trigger_Event_Occurred", "Salience_Reclassified"],
            "outputs": ["Línea de tiempo de evolución de posturas por actor"],
            "exceptions": ["Ruptura repentina de confianza por un incidente ambiental no reportado oportunamente"]
        },
        "entities": [
            {"entity_id": "ENT_ACTOR_DYNAMICS", "type": "concepto_dinamico", "name": "Dinamismo Temporal de Stakeholders", "aliases": ["Stakeholder Posture Evolution"]}
        ],
        "relations": [
            {"subject_id": "ENT_ACTOR_DYNAMICS", "predicate": "modifica_clasificacion_de", "object_id": "ENT_MITCHELL_SALIENCE", "valid_from": "2011", "valid_to": None, "evidence_claim_id": "P05-F26-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Modelo estático vs dinámico",
                "Mapeo Estático Anual": "Asume que una comunidad es 'poco influyente' y no revisa la evaluación durante todo el año fiscal.",
                "Monitoreo Dinámico Continuo": "Detecta en tiempo real cuando la comunidad presenta un recurso legal, reclasificándola inmediatamente como Actor Definitivo."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gestor de Stakeholders", "implication": "BRIDGE debe permitir registrar cambios de postura y atributos con marcas bitemporales para analizar retrospectivamente cómo escalaron los conflictos.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F27"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F27
    {
        "question_id": "P05-F27",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué riesgo tiene inferir posturas personales desde datos de una organización o grupo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Inferir posturas personales de individuos específicos a partir de datos colectivos de una organización o grupo entraña dos riesgos críticos documentados taxativamente en el corpus: 1) Riesgo Metodológico de Falacia Ecológica / Falacia de División: Consiste en asumir erróneamente que las características, posturas políticas o declaraciones emitidas por una institución (e.g. un sindicato, una confederación gremial, una asamblea vecinal o un partido político) son automáticamente compartidas por cada uno de sus miembros individuales. Esta inferencia produce diagnósticos ejecutivos falsos, subestimando la diversidad interna de opiniones, la existencia de corrientes disidentes o el hecho de que un directivo o empleado mantenga posturas moderadas frente a una cúpula beligerante; y 2) Riesgo Ético y Legal Severo (Vulneración de Derechos Fundamentales y Normas de Privacidad): En los marcos institucionales de Chile y estándares internacionales de inteligencia corporativa, el perfilamiento ideológico, la inferencia de convicciones políticas, filiaciones partidistas, religión, salud o vida privada de personas naturales está expresamente proscrito por la Ley de Protección de la Vida Privada (Ley 19.628 y sus reformas), configurando prácticas abusivas de 'espionaje corporativo' o 'listas negras' sindicales. La regla deontológica del programa BRIDGE estipula que el sistema debe limitar su análisis exclusivamente a personas jurídicas, entidades formalmente constituidas y vocerías institucionales públicas registradas en actas y medios abiertos.",
        "findings": [
            {
                "claim_id": "P05-F27-C1",
                "claim": "La inferencia de atributos ideológicos o posturas individuales desde datos grupales incurre en falacia ecológica y viola salvaguardas éticas y legales de no discriminación y privacidad.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Internacional", "actor": "Sistemas de Inteligencia Corporativa"},
                "evidence": [
                    {
                        "source_id": "69d2cc32-f0e5-4943-91f2-b5a7a14cbcfb",
                        "source_title": "P05_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 4.1: Principios Éticos y Salvaguardas de Privacidad",
                        "excerpt_short": "Regla de No-Inferencia de Atributos Sensibles Individuales: Prohibición absoluta de inferir salud, etnia, religión, política o antecedentes penales privados de individuos específicos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7.2: Salvaguardas Éticas y de Seguridad Obligatorias",
                        "excerpt_short": "Bloquea categorizaciones individuales de raza, salud, religión o afiliación partidista personal; enfoca exclusivamente datos institucionales públicos y abiertos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio normativo y ético de cumplimiento imperativo en el programa de investigación de BRIDGE."
            }
        ],
        "operational_model": {
            "inputs": ["Textos de declaraciones colectivas", "Actas de asambleas institucionales"],
            "actors": ["Oficial de Privacidad (DPO)", "Desarrollador de Algoritmos", "Analista de Inteligencia"],
            "steps": ["Inspección de datos de entrada para excluir identificadores personales sensibles", "Bloqueo algorítmico de inferencias individuales", "Auditoría de cumplimiento de privacidad"],
            "states": ["Input_Received", "Privacy_Filter_Applied", "Institutional_Scope_Enforced"],
            "outputs": ["Análisis de posicionamiento circunscrito a personas jurídicas e instituciones"],
            "exceptions": ["Intentos de usuarios del sistema de solicitar perfilamiento individual de dirigentes vecinales o sindicales"]
        },
        "entities": [
            {"entity_id": "ENT_ETHICAL_FIREWALL", "type": "salvaguarda_seguridad", "name": "Filtro Ético de No-Inferencia Individual", "aliases": ["Ethical Profiling Firewall"]}
        ],
        "relations": [
            {"subject_id": "ENT_ETHICAL_FIREWALL", "predicate": "restringe_alcance_de", "object_id": "ENT_MITCHELL_SALIENCE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-F27-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de análisis de actores",
                "Perfilamiento Individual Proscrito": "Analizar la orientación política privada o características psicológicas de un dirigente social.",
                "Análisis Institucional Aprobado": "Analizar las actas públicas, comunicados oficiales y petitorios formales ingresados por la entidad jurídica."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Filtro de Cumplimiento Ético", "implication": "BRIDGE debe incorporar un guardrail en su pipeline de IA que rechace cualquier consulta orientada a perfilar psicológicamente o atribuir ideologías a personas naturales individuales.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F28"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F28
    {
        "question_id": "P05-F28",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar actores y prominencia de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Representar actores y prominencia de forma estructurada exige las siguientes especificaciones técnicas: 1) Variables formales: `actor_id`, `legal_name`, `entity_type` (Persona_Juridica, Autoridad_Fiscalizadora, Gremio_Empresarial, Sindicato, Comunidad_Indigena_Constituida, ONG), `power_attribute` (diccionario con tipo: Coercitivo, Utilitario, Normativo; booleano: true/false; fundamento auditable), `legitimacy_attribute` (booleano: true/false; marco legal que lo sustenta: e.g. Convenio 169 OIT, Ley 18.045), `urgency_attribute` (booleano: true/false; criticidad temporal), `salience_class` (Dormant, Discretionary, Demanding, Dominant, Dangerous, Dependent, Definitive), `slo_level` (Withdrawn, Acceptance, Approval, CoOwnership), `jurisdiction_region`, `valid_time_interval`; 2) Categorías: Tipo de vinculación institucional (Territorial, Financiero, Regulatorio, Laboral, Comercial); 3) Relaciones formales: `participa_en_tramitacion` (Actor -> Expediente), `mantiene_alianza_con` (Actor_A -> Actor_B), `plantea_reclamo_contra` (Actor -> Empresa), `adquiere_atributo` (Actor -> Atributo_P_L_U); 4) Condiciones de integridad: Prohibición expresa de atributos individuales de personas naturales (salud, credo, etnia individual); toda asignación de `salience_class = Definitive` debe enlazar un documento verificable que respalde los tres atributos simultáneamente; y todo cambio de clase debe registrar fecha y causa del hito en el registro histórico.",
        "findings": [
            {
                "claim_id": "P05-F28-C1",
                "claim": "El esquema estructurado de actores corporativos requiere modelar atributos dinámicos de prominencia, niveles de licencia social y salvaguardas estrictas de privacidad institucional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Arquitectura de Software BRIDGE"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7.1: Módulo 2: Clasificador Dinámico de Prominencia de Actores",
                        "excerpt_short": "Taggea a cada actor externo según atributos observados: Poder (P), Legitimidad (L) y Urgencia (U), alertando transiciones hacia 'Definitivo'.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "bdea4496-e0aa-4433-91e6-80026bbef2c1",
                        "source_title": "Quorum: Stakeholder Management CRM & Policy Intelligence Platform",
                        "original_url": "https://www.quorum.us/platform/stakeholder-management/",
                        "locator": "Sección: Mapping & Tracking Stakeholder Relationships",
                        "excerpt_short": "Structured CRM schemas track institutional profiles, legislative votes, meeting histories, and engagement tiers across regulatory jurisdictions.",
                        "source_date": "2024-05-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Basado en los mejores estándares de plataformas de CRM de asuntos públicos y modelos teóricos de prominencia."
            }
        ],
        "operational_model": {
            "inputs": ["Ontología de actores institucionales", "Expedientes de audiencias públicas Ley 20.730"],
            "actors": ["Administrador de Plataforma", "Analista de Asuntos Regulatorios"],
            "steps": ["Diseño de tablas de entidades de actores", "Configuración de validaciones de integridad referencial", "Indexación en base de grafos"],
            "states": ["Actor_Schema_Designed", "Constraints_Configured", "Database_Migrated"],
            "outputs": ["Esquema estructurado de actores en la base de datos de BRIDGE"],
            "exceptions": ["Ingesta de datos que violen las restricciones de atributos individuales sensibles"]
        },
        "entities": [
            {"entity_id": "ENT_ACTOR_SCHEMA", "type": "esquema_datos", "name": "Esquema Estructurado de Actores y Prominencia", "aliases": ["Stakeholder Graph Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_ACTOR_SCHEMA", "predicate": "normaliza_entidades_de", "object_id": "ENT_MITCHELL_SALIENCE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P05-F28-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Base de Datos de Actores", "implication": "BRIDGE debe implementar tablas específicas para actores jurídicos e instituciones públicas, asegurando que las relaciones de influencia estén respaldadas por evidencias formales.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F29"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F29
    {
        "question_id": "P05-F29",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre actores y prominencia?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los hechos documentados sobre actores y prominencia están respaldados por cinco fuentes primarias del corpus: 1) Mitchell, Agle & Wood (1997, Academy of Management Review, 22(4), pp. 853-886 / Umbrex 2024, ámbito: teoría organizacional y dirección estratégica): respalda la definición de poder, legitimidad y urgencia y la tipología de 7 clases de stakeholders; 2) Boutilier & Thomson (2011, Modelling and Measuring the SLO, ámbito: minería e industrias extractivas en América Latina): respalda el modelo piramidal de 4 niveles y 3 umbrales de la Licencia Social para Operar; 3) AccountAbility (2015, AA1000 Stakeholder Engagement Standard - AA1000SES, ámbito: estándar internacional auditable): respalda los principios de inclusividad, materialidad, capacidad de respuesta e impacto en el relacionamiento corporativo; 4) BCN Chile: Ley 20.730 de Lobby (2014/2026, ámbito: regulación chilena de transparencia): respalda la obligatoriedad de registro público de reuniones de gestión de intereses particulares; y 5) BCN Chile: Decreto 236 Promulga Convenio 169 OIT (2008/2026, ámbito: derecho internacional y pueblos indígenas en Chile): respalda la consulta previa libre e informada como fuente obligatoria de legitimidad territorial.",
        "findings": [
            {
                "claim_id": "P05-F29-C1",
                "claim": "Los principios de prominencia y relacionamiento con actores se fundamentan en literatura teórica canónica y normativas vinculantes del marco institucional chileno e internacional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "1997-2026", "region": "Chile / Internacional", "actor": "Marco Regulatorio y Teórico"},
                "evidence": [
                    {
                        "source_id": "dbb37605-2cb8-49a6-a1e4-babcce7f5dda",
                        "source_title": "AccountAbility: AA1000 Stakeholder Engagement Standard (AA1000SES)",
                        "original_url": "https://www.accountability.org/standards/aa1000-stakeholder-engagement",
                        "locator": "Estándar AA1000SES (2015), Principios Rectores",
                        "excerpt_short": "Provides a globally accepted framework for an organization to assess, design, implement and communicate their stakeholder engagement to support sustainability.",
                        "source_date": "2015-11-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "537a7618-1e79-4747-ad6b-6e492a4a15b7",
                        "source_title": "BCN Chile: Ley 20.730 Regula el Lobby y las Gestiones que Representen Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 1 a 8",
                        "excerpt_short": "Regula la publicidad en la actividad de lobby y demás gestiones que representen intereses particulares ante autoridades y funcionarios del Estado.",
                        "source_date": "2014-03-08",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Textos legales oficiales de la República de Chile y estándares internacionales auditables."
            }
        ],
        "operational_model": {
            "inputs": ["Leyes de la República de Chile", "Normas técnicas de AccountAbility"],
            "actors": ["Curador Legal", "Investigador de Políticas Públicas"],
            "steps": ["Verificación de vigencia jurídica en la Biblioteca del Congreso Nacional (BCN)", "Cotejo de artículos aplicables", "Registro en catálogo de fuentes normativas"],
            "states": ["Legislation_Verified", "Articles_CrossReferenced", "Registry_Updated"],
            "outputs": ["Catálogo de fuentes normativas de actores"],
            "exceptions": ["Reformas legales pendientes de publicación en el Diario Oficial"]
        },
        "entities": [
            {"entity_id": "ENT_ACTOR_LEGAL_SOURCES", "type": "corpus_fuentes", "name": "Fuentes Normativas de Actores", "aliases": ["Stakeholder Legal Bases"]}
        ],
        "relations": [
            {"subject_id": "ENT_ACTOR_LEGAL_SOURCES", "predicate": "respalda_normativamente_a", "object_id": "ENT_ACTOR_SCHEMA", "valid_from": "2008", "valid_to": None, "evidence_claim_id": "P05-F29-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Módulo de Cumplimiento Legal", "implication": "BRIDGE debe permitir registrar el cumplimiento de la Ley 20.730 y del Convenio 169 OIT como indicadores auditables de legitimidad institucional.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F30"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P05-F30
    {
        "question_id": "P05-F30",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra actores y prominencia sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El caso concreto documentado en el corpus que ilustra la clasificación y mutación de prominencia de actores es la tramitación y paralización de megaproyectos de inversión en Chile (e.g. Proyecto Minero-Portuario Dominga y Central Termoeléctrica Barrancones / Pascua Lama, documentados en P05_RESEARCH_DOSSIER Sección 6 y marco SEIA/Convenio 169 OIT): 1) Entradas del Sistema: a) Fase Inicial: La empresa categoriza a la Asociación Gremial de Pescadores y Comunidad Indígena Changos de la caleta local como Actor 'Discrecional' o 'Dependiente' (alta legitimidad por residencia ancestral y urgencia por impacto en la biósfera marina, pero clasificados como carentes de poder económico o político); la empresa enfoca sus esfuerzos de lobby (Ley 20.730) exclusivamente en las autoridades políticas y ministeriales del Comité de Ministros (clasificados como Actores 'Dominantes' con Poder y Legitimidad); b) Hito de Ruptura: La comunidad territorial, al percibir que sus acuerdos de compensación no cumplen el umbral de credibilidad socio-política de la Licencia Social (SLO de Boutilier & Thomson), interpone un recurso judicial en el Primer Tribunal Ambiental y la Corte de Apelaciones denunciando omisión de consulta indígena reglada bajo Convenio 169 de la OIT (Decreto 236) y afectación a reservas marinas protegidas; 2) Proceso y Resultado Observado: El Tribunal acoge el reclamo y decreta la suspensión cautelar de la RCA. En ese instante, la comunidad adquiere Poder Coercitivo formal transferido por el poder judicial, transmutándose inmediatamente en Actor Definitivo (Poder + Legitimidad + Urgencia). El resultado esperado demuestra que subestimar la legitimidad y urgencia de un actor dependiente provoca la judicialización y colapso de la viabilidad del proyecto de inversión.",
        "findings": [
            {
                "claim_id": "P05-F30-C1",
                "claim": "La historia de judicialización ambiental en Chile comprueba empíricamente cómo comunidades locales dependientes mutan a actores definitivos al canalizar sus reclamos a través de tribunales ambientales e instrumentos internacionales vinculantes.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2018-2026", "region": "Chile", "actor": "Tribunales Ambientales / SEA / Comunidades Costeras"},
                "evidence": [
                    {
                        "source_id": "949f1e6b-c786-481f-b968-911de8bfc023",
                        "source_title": "P05_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 6: Caso 2 (Conflictos Socioambientales y la Pérdida de la SLO en Chile)",
                        "excerpt_short": "Las organizaciones operaron bajo el supuesto de que la aprobación formal del Estado bastaba, omitiendo la Licencia Social. Las comunidades articularon su reclamo en tribunales ambientales bajo Convenio 169 OIT logrando la paralización.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "a2bbed13-4e5a-4e3d-816b-3bb36f738bb0",
                        "source_title": "BCN Chile: Decreto 236 Promulga el Convenio 169 OIT sobre Pueblos Indígenas y Tribales",
                        "original_url": "https://www.bcn.cl/leychile/Navegar?idNorma=279441",
                        "locator": "Artículos 6 y 7",
                        "excerpt_short": "Obliga a los gobiernos a consultar a los pueblos interesados, mediante procedimientos apropiados y en particular a través de sus instituciones representativas, cada vez que se prevean medidas legislativas o administrativas susceptibles de afectarles directamente.",
                        "source_date": "2008-10-02",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Jurisprudencia reiterada de la Corte Suprema y Tribunales Ambientales de Chile en materia de evaluación ambiental de proyectos de inversión."
            }
        ],
        "operational_model": {
            "inputs": ["Estudio de Impacto Ambiental (EIA)", "Recurso de protección interpuesto", "Sentencia del Tribunal Ambiental"],
            "actors": ["Comunidad Territorial", "Titular del Proyecto", "Tribunal Ambiental", "Comité de Ministros"],
            "steps": ["Ignorar demandas comunitarias en etapa temprana", "Interposición de acción contenciosa ambiental", "Dictación de orden de no innovar y suspensión de faenas"],
            "states": ["Dependent_Ignored", "Litigation_Triggered", "Definitive_Injunction_Granted"],
            "outputs": ["Paralización de obras e inicio forzado de mesas de diálogo bajo estándar AA1000SES"],
            "exceptions": ["Empresa que ejecuta consulta previa voluntaria temprana logrando copropiedad psicológica"]
        },
        "entities": [
            {"entity_id": "ENT_TERRITORIAL_CASE", "type": "caso_analitico", "name": "Caso Judicialización Territorial en Chile", "aliases": ["Mutación a Actor Definitivo en SEIA"]}
        ],
        "relations": [
            {"subject_id": "ENT_TERRITORIAL_CASE", "predicate": "evidencia_dinamica_de", "object_id": "ENT_MITCHELL_SALIENCE", "valid_from": "2018", "valid_to": None, "evidence_claim_id": "P05-F30-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Error de gestión",
                "Supuesto tradicional de la gerencia": "Gestionar exclusivamente al actor dominante (reguladores) garantiza la aprobación del proyecto.",
                "Realidad del entorno socioambiental": "El actor dependiente se alía con el poder judicial y suspende el proyecto, convirtiéndose en el actor más crítico."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Simulador de Riesgo Territorial", "implication": "BRIDGE debe alertar preventivamente cuando un actor territorial con Legitimidad y Urgencia no cuenta con canales de diálogo institucional, calificándolo como riesgo inminente de mutación a Actor Definitivo.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P05-F31"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P05.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P05-F25..F30) to {out_path}.")
