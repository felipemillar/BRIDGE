import json
import os
import sys

# Append P01-F10, P01-F11, P01-F12 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F10",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones definen la representación estructurada de este tema?",
        "snapshot_at": "2026-10-01T00:37:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La representación estructurada del mapa B2B se define mediante 5 variables (jerarquía C-Suite, rol funcional B2B, horizonte temporal, métricas de éxito JTBD y potestad de veto), 3 categorías de roles (Usuario, Comprador y Aprobador), relaciones de fricción operativa y veto unilateral, y condiciones de trazabilidad con citas y despliegue privado VPC sin re-entrenamiento público.",
        "findings": [
            {
                "claim_id": "P01-F10-C1",
                "claim": "El mapa de adopción B2B se estructura en tres categorías funcionales no coincidentes: Usuario (CCO, Asuntos Públicos, Prensa, ESG), Comprador (CEO, CCO / VP Asuntos Corporativos) y Aprobador técnico (CISO, Fiscal Legal, CFO).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Organizaciones Corporativas B2B"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7: Mapa de Usuarios, Compradores y Aprobadores",
                        "excerpt_short": "El Usuario: CCO, Asuntos Públicos... El Comprador: CEO, CCO... El Aprobador: CISO, Fiscal Legal, Compliance.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier consolidado del pilar P01."
            },
            {
                "claim_id": "P01-F10-C2",
                "claim": "El CISO y el Fiscal Legal operan como aprobadores obligatorios dotados de potestad de veto unilateral sobre herramientas de inteligencia basada en IA que ingieran información corporativa sensible.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Global / B2B SaaS", "actor": "CISO / Compliance"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4, HT-3 (Hipótesis de Trabajo 3)",
                        "excerpt_short": "CISO y Legal actúan como aprobadores críticos con poder de veto si se vulnera la privacidad o confidencialidad de la información corporativa.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Formulada formalmente como Hipótesis de Trabajo HT-3 en el mapa de evidencia del corpus."
            },
            {
                "claim_id": "P01-F10-C3",
                "claim": "El CCO reporta directamente al CEO en el 53,6% de los casos y participa de forma permanente en el Comité Ejecutivo en el 33% de las organizaciones.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "España / Benchmark Habla Hispana", "actor": "Dircoms y C-Suite"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Asociación de Directivos de Comunicación (Dircom España) - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Reporte de resultados ECE 2025",
                        "excerpt_short": "Más de la mitad de los dircoms reportan al CEO (53,6%) y uno de cada tres está en el comité ejecutivo (33%).",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio empírico ECE 2025 de Dircom España."
            },
            {
                "claim_id": "P01-F10-C4",
                "claim": "Las condiciones no negociables para la representación estructurada exigen trazabilidad con citas directas al repositorio corporativo y aislamiento de datos en nube privada (VPC) sin re-entrenamiento público.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / B2B", "actor": "Arquitectura de Software"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7: Requerimientos de Seguridad y Privacidad",
                        "excerpt_short": "Aislamiento VPC y prohibición de reutilizar prompts o documentos corporativos para entrenamiento de modelos públicos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Condición arquitectónica documentada en el dossier."
            }
        ],
        "operational_model": {
            "inputs": ["Perfiles funcionales B2B", "Matriz de objeciones de seguridad", "Políticas de gobernanza corporativa"],
            "actors": ["Usuario (CCO / Asuntos Públicos)", "Comprador (CEO)", "Aprobador (CISO / Fiscal Legal)"],
            "steps": ["Mapeo de necesidades de usuario", "Evaluación de ROI y valor reputacional", "Auditoría de ciberseguridad y compliance", "Decisión colegiada de adquisición"],
            "states": ["Prospecto", "Demostración_Usuario", "Evaluación_CISO_Legal", "Veto_Técnico", "Aprobado"],
            "outputs": ["Matriz de roles B2B", "Protocolo de objeciones técnicas", "Configuración de entorno seguro VPC"],
            "exceptions": ["Veto de CISO por riesgo de fuga de datos hacia LLMs públicos", "Falta de justificación de ROI reputacional ante el CEO"]
        },
        "entities": [
            {"entity_id": "ENT_CISO", "type": "rol", "name": "Chief Information Security Officer (CISO)", "aliases": ["Oficial de Seguridad de la Información"]},
            {"entity_id": "ENT_LEGAL_COMPLIANCE", "type": "rol", "name": "Fiscal Legal / Compliance Officer", "aliases": ["Fiscal Corporativo", "Oficial de Cumplimiento"]}
        ],
        "relations": [
            {"subject_id": "ENT_CISO", "predicate": "ejerce_potestad_de_veto_sobre", "object_id": "Adopción_Tecnología_IA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F10-C2"},
            {"subject_id": "ENT_CCO", "predicate": "reporta_jerarquicamente_a", "object_id": "ENT_CEO", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F10-C3"}
        ],
        "comparisons": [
            {
                "dimension": "Rol B2B en la Decisión",
                "Usuario": "Exige velocidad analítica, minutas ejecutivas y trazabilidad con citas a fuentes internas.",
                "Comprador": "Busca mitigar riesgos reputacionales y proteger la licencia social con relato unificado.",
                "Aprobador": "Exige aislamiento estricto en nube privada VPC, cifrado y cumplimiento normativo estricto."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Porcentaje de CCOs que reportan directamente al CEO",
                "value": "53.6%",
                "denominator": "Total de directivos de comunicación encuestados en ECE 2025 (España)",
                "source_claim_id": "P01-F10-C3"
            },
            {
                "metric": "Porcentaje de CCOs que integran el Comité Ejecutivo",
                "value": "33%",
                "denominator": "Total de directivos de comunicación encuestados en ECE 2025 (España)",
                "source_claim_id": "P01-F10-C3"
            }
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Incorporar trazabilidad documental obligatoria con citas exactas para satisfacer al Usuario y al Fiscal Legal.", "status": "evidencia"},
            {"module": "Gobernanza", "implication": "Desplegar BRIDGE en arquitectura VPC aislada para neutralizar el veto del CISO.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap": "sin_evidencia sobre matrices formales de objeciones técnicas de CISOs en América Latina ante herramientas de IA corporativa.",
                "minimum_validation": "Entrevistas a 5 CISOs de empresas reguladas e IPSA en Chile.",
                "priority": "alta"
            }
        ],
        "next_question_ids": ["P01-F11", "P01-F12"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F11",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada afirmación del mapa?",
        "snapshot_at": "2026-10-01T00:37:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El mapa está respaldado por encuestas gremiales de directivos (ECE 2025 de Dircom España: 53,6% reporte a CEO), marcos conceptuales globales (GCF de Global Alliance 2021; Page Society 2022/2023), consultoría estratégica de alta dirección (McKinsey 2025), marcos regulatorios chilenos vinculantes (Ley 20.730 de Lobby y NCG 461 de la CMF) y los dossiers de síntesis interna P01.",
        "findings": [
            {
                "claim_id": "P01-F11-C1",
                "claim": "El estudio ECE 2025 de Dircom España (campo Ene-Mar 2025, publicado Sep 2025) documenta que el 53,6% de los directores de comunicación reporta al máximo ejecutivo (CEO) y el 33% forma parte del comité de dirección.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "España", "actor": "Dircom España"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Asociación de Directivos de Comunicación (Dircom España) - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Pasaje: Más de la mitad de los dircoms reportan al CEO (53,6%) y uno de cada tres está en el comité ejecutivo",
                        "excerpt_short": "53,6% reporta al CEO y uno de cada tres está en el comité ejecutivo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Encuesta empírica cuantitativa de la principal asociación gremial de comunicación de habla hispana."
            },
            {
                "claim_id": "P01-F11-C2",
                "claim": "McKinsey & Company (octubre 2025) concluye que a medida que la inteligencia recopilada por IA se convierte en un commodity, los equipos corporativos requieren conocimiento y criterio humano para contextualizar decisiones.",
                "epistemic_status": "declaracion_proveedor",
                "scope": {"time": "2025-10", "region": "Global", "actor": "McKinsey & Company"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección: The human element in corporate affairs intelligence",
                        "excerpt_short": "...as AI-gathered intelligence becomes commoditized, teams need human knowledge and judgment to interpret strategic implications.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicación de liderazgo de pensamiento de consultora estratégica global."
            },
            {
                "claim_id": "P01-F11-C3",
                "claim": "En Chile, la Ley N° 20.730 de Lobby (2014-2026) y la NCG 461 de la CMF (2021-2025) constituyen el marco regulatorio legal obligatorio que fija la responsabilidad fáctica sobre las declaraciones corporativas de sujetos pasivos y emisores de valores.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile", "actor": "Congreso Nacional / CMF Chile"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 3°, 4° y 5°",
                        "excerpt_short": "Establece los sujetos pasivos y el registro público de audiencias y viajes.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Requisitos de Memoria Integrada ASG",
                        "excerpt_short": "Supervisa la divulgación de sostenibilidad y gobierno corporativo en memorias anuales integradas.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Cuerpo normativo chileno oficial y vigente."
            },
            {
                "claim_id": "P01-F11-C4",
                "claim": "No existen mediciones cuantitativas auditadas e independientes sobre las horas-hombre exactas invertidas en preparar un briefing book ni matrices de objeción técnica de CISOs en la literatura gremial de PR.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Literatura de Gestión Corporativa"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección de Vacíos: Falta de auditorías de tiempo y criterios CISO",
                        "excerpt_short": "Falta de medición cuantitativa de horas-hombre en briefing books y vacíos en matrices de objeción de CISOs.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico explícitamente delimitado en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Fuentes primarias y secundarias", "Leyes de la República", "Informes gremiales"],
            "actors": ["Investigador Corporativo", "Auditor de Evidencia"],
            "steps": ["Verificación de autenticidad de fuentes", "Extracción de citas y localizadores", "Identificación de vacíos epistemológicos"],
            "states": ["Fuentes_Reunidas", "Analizadas", "Auditadas", "Trazables"],
            "outputs": ["Matriz de Trazabilidad Documental", "Registro de Vacíos de Evidencia"],
            "exceptions": ["Uso de enlaces rotos o fuentes sin fecha", "Atribución de hechos empíricos a declaraciones comerciales"]
        },
        "entities": [
            {"entity_id": "ENT_DIRCOM_ESP", "type": "organizacion", "name": "Asociación de Directivos de Comunicación (Dircom España)"},
            {"entity_id": "ENT_MCKINSEY", "type": "empresa", "name": "McKinsey & Company"}
        ],
        "relations": [
            {"subject_id": "ENT_DIRCOM_ESP", "predicate": "publica_estudio", "object_id": "El Estado de la Comunicación en España 2025", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F11-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Mantener tabla de metadatos estricta con URL, fecha y localizador para cada insumo indexado en BRIDGE.", "status": "evidencia"}
        ],
        "open_gaps": [
            {
                "gap": "sin_evidencia sobre mediciones auditadas de horas invertidas en preparación de briefings en empresas chilenas.",
                "minimum_validation": "Estudio de tiempos y movimientos con 10 equipos de asuntos corporativos en Santiago.",
                "priority": "alta"
            }
        ],
        "next_question_ids": ["P01-F12", "P01-F13"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F12",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto con entradas y resultado esperado ilustra este mapa en la práctica?",
        "snapshot_at": "2026-10-01T00:37:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso de un conglomerado industrial e IPSA en Chile convocado por un Subsecretario a audiencia urgente bajo Ley 20.730 ilustra la interacción: el CCO (Usuario) elabora un briefing en 15 minutos cruzando compromisos de la Memoria NCG 461 CMF con audiencias previas; el CEO (Comprador) valida la coherencia reputacional; y el CISO/Legal (Aprobador) audita el entorno VPC aislado autorizando el uso sin vetos.",
        "findings": [
            {
                "claim_id": "P01-F12-C1",
                "claim": "En un escenario de contingencia regulatoria en Chile, las entradas operativas incluyen la Memoria Integrada NCG 461 CMF, el historial de audiencias en InfoLobby (Ley 20.730), la RCA ambiental y las señales exteriores de clipping mediático.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresa Minera / Industrial IPSA"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7: Caso Práctico de Adopción e Interacción B2B",
                        "excerpt_short": "Entradas del caso: Memoria NCG 461, actas InfoLobby Ley 20.730, RCA operacional y clipping en tiempo real.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Flujo de trabajo documentado en el caso práctico del dossier."
            },
            {
                "claim_id": "P01-F12-C2",
                "claim": "La interacción de los roles B2B resuelve la tensión entre la demanda de velocidad del CCO (minuta en 15 minutos) y las exigencias de ciberseguridad del CISO y el Fiscal Legal mediante el despliegue en nube privada (VPC) con cifrado.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Chile", "actor": "C-Suite y Soporte Técnico"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4, HT-2 y HT-3",
                        "excerpt_short": "Adopción viable condicionada a VPC que evita el veto del CISO garantizando reducción de tiempo de preparación de 4 horas a 15 minutos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Hipótesis operacionales HT-2 y HT-3 del mapa de evidencia."
            },
            {
                "claim_id": "P01-F12-C3",
                "claim": "El resultado esperado consiste en un briefing ejecutivo de 2 páginas con 3 líneas argumentales hipervinculadas a fuentes oficiales, consistencia fáctica total entre el acta de lobby y la memoria CMF, y aprobación de despliegue sin riesgo de veto.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresa Regulada"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7: Resultados Esperados del Caso Concreto",
                        "excerpt_short": "Briefing de 2 páginas con citas exactas, cero discrepancias con InfoLobby y validación técnica del CISO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:37:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación de entrega del caso documentada en el dossier."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria NCG 461 CMF", "Actas InfoLobby Ley 20.730", "RCA ambiental", "Clipping mediático"],
            "actors": ["CCO / Gerente de Asuntos Públicos (Usuario)", "CEO (Comprador)", "CISO (Aprobador)", "Fiscal Legal (Aprobador)"],
            "steps": [
                "Notificación de audiencia urgente por Subsecretario",
                "Generación de briefing por CCO cruzando NCG 461 y actas de lobby previas",
                "Revisión de consistencia reputacional por CEO",
                "Auditoría técnica de VPC por CISO y revisión legal por Fiscal",
                "Emisión de vocería y registro posterior en InfoLobby"
            ],
            "states": ["Alerta_Recibida", "Briefing_Generado", "Revisión_C_Suite", "VPC_Auditado", "Audiencia_Completada"],
            "outputs": ["Briefing ejecutivo con citas trazables", "Acta pública InfoLobby sin inconsistencias", "Certificación de seguridad VPC"],
            "exceptions": ["Detección de vulnerabilidad de fuga de datos hacia LLM público (Veto CISO)", "Contradicción entre declaración y Memoria CMF (Veto Fiscal)"]
        },
        "entities": [
            {"entity_id": "ENT_INFOLOBBY", "type": "plataforma", "name": "InfoLobby (Consejo para la Transparencia)", "aliases": ["Plataforma Ley de Lobby"]},
            {"entity_id": "ENT_SUBSECRETARIA", "type": "institucion_publica", "name": "Subsecretaría de Estado", "aliases": ["Autoridad Sectorial"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "elabora_briefing_para", "object_id": "ENT_SUBSECRETARIA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F12-C1"},
            {"subject_id": "ENT_CISO", "predicate": "audita_entorno", "object_id": "Nube_Privada_VPC", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F12-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Generar minutas ejecutivas estructuradas con formato de 2 páginas y citas trazables en menos de 15 minutos.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F13", "P01-F14"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

# Write records to a temp file and test with audit_responses.py
temp_path = "respuestas/temp_f10_f12.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
