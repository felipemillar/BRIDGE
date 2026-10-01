import json
import os
import sys

# Append P01-F22, P01-F23, P01-F24 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F22",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones definen la representación estructurada de este tema?",
        "snapshot_at": "2026-10-01T00:47:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de reuniones críticas se define mediante 4 variables de criticidad (regulatoria Ley 20.730/NCG 461, reputacional/SLO, temporal Golden Hour <30-60 min, y operacional/financiera); 4 categorías de participantes (C-Suite interno, Reguladores/autoridades, Comunidades/gremios, y Medios/analistas); 3 relaciones interfuncionales clave (Tríada CCO-Legal-Sostenibilidad, Binomio CCO-CEO, y Filtro de Gobernanza CISO/Compliance); y condiciones normativas y temporales de éxito de registro oportuno y cero inconsistencias.",
        "findings": [
            {
                "claim_id": "P01-F22-C1",
                "claim": "La criticidad de una instancia decisional en Asuntos Corporativos se define a través de cuatro vectores: criticidad regulatoria (Ley 20.730 de Lobby y NCG 461 CMF), criticidad reputacional (Licencia Social para Operar), criticidad temporal (Golden Hour <30 a 60 minutos) y criticidad operacional/financiera.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gerencias de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Vectores de Criticidad en Decisiones Corporativas",
                        "excerpt_short": "Cuatro vectores de criticidad: regulatoria, reputacional, temporal y operacional/financiera.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F22-C2",
                "claim": "Las relaciones interfuncionales críticas exigen la coordinación inquebrantable de la Tríada CCO-Legal-Operaciones/Sostenibilidad para asegurar que lo declarado a medios y reguladores coincida con lo comprometido en RCA y memorias financieras.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "C-Suite Interfuncional"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Articulación Interfuncional y Tríada de Control",
                        "excerpt_short": "Tríada CCO - Legal - Operaciones: consistencia entre prensa, contratos y compromisos en terreno.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F22-C3",
                "claim": "Los CEOs de alto desempeño dedican aproximadamente el 30% de su tiempo laboral a relacionamiento con stakeholders externos, requiriendo del CCO inteligencia contextual sintetizada y lines to take directas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "Global", "actor": "CEOs de Alto Desempeño"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Dedicación del CEO a stakeholders externos",
                        "excerpt_short": "CEOs de alto desempeño dedican alrededor del 30% de su tiempo a la gestión externa de grupos de interés.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicación de McKinsey en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Vectores de criticidad ponderados", "Mapas de participantes", "Restricciones temporales"],
            "actors": ["CCO", "CEO", "Fiscal Legal", "CISO", "Líder Comunitario"],
            "steps": ["Ponderación de criticidad", "Convocatoria y preparación interfuncional", "Validación de entorno seguro", "Ejecución y registro de compromisos"],
            "states": ["Evaluación_Criticidad", "Alineamiento_Tríada", "Reunión_Ejecutada", "Registro_InfoLobby"],
            "outputs": ["Matriz de criticidad", "Briefing de 1 página", "Registro de cumplimiento"],
            "exceptions": ["Objeción de seguridad del CISO ante transferencia indebida de datos"]
        },
        "entities": [
            {"entity_id": "ENT_TRIADA_CONTROL", "type": "concepto_operativo", "name": "Tríada CCO - Legal - Operaciones", "aliases": ["Tríada de Consistencia Corporativa"]},
            {"entity_id": "ENT_VECTORES_CRITICIDAD", "type": "modelo_analisis", "name": "Cuatro Vectores de Criticidad", "aliases": ["Dimensiones de Criticidad Decisional"]}
        ],
        "relations": [
            {"subject_id": "ENT_TRIADA_CONTROL", "predicate": "asegura_coherencia_en", "object_id": "ENT_AUDIENCIA_LOBBY", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F22-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Porcentaje de tiempo dedicado por CEOs de alto desempeño a stakeholders externos",
                "value": "30%",
                "denominator": "Jornada laboral total del CEO",
                "source_claim_id": "P01-F22-C3"
            }
        ],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Incorporar la Tríada CCO-Legal-Operaciones como workflow de aprobación obligatorio en BRIDGE para declaraciones públicas y briefings.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F23", "P01-F24"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F23",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada afirmación de este tema?",
        "snapshot_at": "2026-10-01T00:47:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El tema está respaldado por 8 fuentes primarias estructuradas: Ley N° 20.730 de Lobby (BCN Chile 2014-2026); NCG 461 y 519 de la CMF (26-NOV-2025 sobre memorias integradas ASG); Dircom ECE 2025 (Sep 2025, 54,4% reporte a CEO y 32,3% en Comité); Page Society (2022-2024 sobre el CCO Integrador); McKinsey (Oct 2025, 30% tiempo CEO a stakeholders externos); GCF Global Alliance (2021 sobre inteligencia contextual); Cadem Marcas Ciudadanas (Jun 2026); y Merco Chile auditado por KPMG. Se identifican 4 vacíos críticos de evidencia (métricas de tiempo, estudios longitudinales de IA en SLO, criterios de CISO y trazabilidad empírica en InfoLobby).",
        "findings": [
            {
                "claim_id": "P01-F23-C1",
                "claim": "La regulación chilena (Ley 20.730 y NCG 461 de la CMF) fija responsabilidades legales ineludibles sobre la transparencia de reuniones con autoridades y la divulgación de factores ASG en memorias anuales de emisores bursátiles.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "BCN / CMF Chile"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Marco general de registro de lobby",
                        "excerpt_short": "Regula la publicidad en la actividad de lobby y gestiones de intereses particulares en Chile.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Supervisión de divulgación de sostenibilidad",
                        "excerpt_short": "Exigencia de reporte de sostenibilidad y gobierno corporativo en memorias integradas.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa oficial chilena vigente."
            },
            {
                "claim_id": "P01-F23-C2",
                "claim": "Existen 4 vacíos críticos de evidencia documentados formalmente en P01_GAPS_AND_VALIDATION: falta de métricas temporales auditadas sobre horas-hombre de briefings; carencia de estudios longitudinales de IA en Licencia Social; opacidad en criterios de aprobación de CISOs; y ausencia de literatura empírica que coteje minutas internas con registros de InfoLobby.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Literatura de Investigación"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Knowledge Gaps 1 a 4",
                        "excerpt_short": "Identificación de los 4 vacíos críticos de evidencia: métricas de tiempo, impacto en SLO, objeciones CISO y trazabilidad en lobby.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Matriz formal de vacíos del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Fuentes regulatorias", "Benchmarks profesionales", "Matriz de vacíos"],
            "actors": ["Auditor Epistemológico", "Investigador Legal"],
            "steps": ["Cotejo normativo", "Verificación cruzada de fuentes", "Mapeo de vacíos"],
            "states": ["Fuentes_Verificadas", "Vacíos_Delimitados"],
            "outputs": ["Matriz de fuentes y pasajes", "Registro de Knowledge Gaps"],
            "exceptions": ["Cita sin localizador exacto o fuente desactualizada"]
        },
        "entities": [
            {"entity_id": "ENT_CORPUS_P01", "type": "corpus_investigacion", "name": "Corpus P01: Asuntos Corporativos y sus Usuarios", "aliases": ["Cuaderno P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_CORPUS_P01", "predicate": "identifica_vacios_en", "object_id": "ENT_GAP_HORAS_HOMBRE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F23-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Validación", "implication": "Diseñar pruebas piloto para resolver empíricamente los 4 Knowledge Gaps identificados en empresas chilenas.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre estudios empíricos que comparen minutas internas de empresas chilenas con sus actas publicadas en InfoLobby.", "minimum_validation": "Muestreo comparativo de 50 audiencias públicas en InfoLobby contra minutas de preparación.", "priority": "alta"}
        ],
        "next_question_ids": ["P01-F24", "P01-F25"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F24",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto con entradas y resultado esperado ilustra este tema en la práctica?",
        "snapshot_at": "2026-10-01T00:47:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso de un conglomerado minero-energético en el norte de Chile que enfrenta una revisión de permisos ambientales y protestas territoriales ilustra el tema: con entradas de RCA vigentes, reportes CMF NCG 461, actas previas de InfoLobby y petitorios comunitarios, el CCO y Asuntos Públicos sostienen la audiencia de lobby con la autoridad ambiental mientras Sostenibilidad atiende la mesa comunitaria; las decisiones se adoptan con cero contradicciones intergerenciales, logrando registrar el acta en InfoLobby en menos de 24 horas y preservando la continuidad operacional.",
        "findings": [
            {
                "claim_id": "P01-F24-C1",
                "claim": "En un conflicto territorial minero-energético en Chile, las entradas operativas integran las RCA vigentes, la Memoria Integrada CMF NCG 461, el historial de InfoLobby y el monitoreo de recursos judiciales y demandas comunitarias en tiempo real.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Conglomerado Minero-Energético"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Caso Práctico Minero-Energético en Chile",
                        "excerpt_short": "Entradas del caso: RCA ambiental, compromisos CMF NCG 461, InfoLobby y demandas territoriales.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso práctico detallado en el dossier P01."
            },
            {
                "claim_id": "P01-F24-C2",
                "claim": "El resultado esperado verifica tres logros: inscripción de la audiencia en InfoLobby en <24 horas, consistencia fáctica del 100% con la Memoria CMF NCG 461, y preservación de la Licencia Social para Operar evitando la paralización de la faena.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Gerencia General y Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Resultados Verificables del Caso Minero",
                        "excerpt_short": "Registro en InfoLobby en <24 horas, 100% consistencia con CMF y continuidad de faena sin paralizaciones.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:47:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación de resultados verificables en el dossier."
            }
        ],
        "operational_model": {
            "inputs": ["RCA operacional", "Memoria CMF NCG 461", "Actas InfoLobby", "Petitorios comunitarios"],
            "actors": ["CCO", "Gerente de Asuntos Públicos", "Gerente de Sostenibilidad", "Autoridad Ambiental", "Comunidad Local"],
            "steps": ["Preparación de briefing cruzado", "Audiencia de lobby ante autoridad ambiental", "Mesa de diálogo comunitaria simultánea", "Firma de adenda socioambiental", "Inscripción en InfoLobby"],
            "states": ["Conflicto_Detectado", "Briefing_Consolidado", "Negociación_Paralela", "Acuerdos_Suscritos", "Cumplimiento_Registrado"],
            "outputs": ["Briefing ejecutivo trazable", "Adenda comunitaria", "Acta oficial InfoLobby"],
            "exceptions": ["Oferta económica informal del vocero en terreno que contradice el presupuesto aprobado por el Directorio"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_MINERO_NORTE", "type": "caso_estudio", "name": "Caso de Diálogo Territorial y Permisos Ambientales en Minería", "aliases": ["Conflicto Minero Norte de Chile"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "lidera_respuesta_en", "object_id": "ENT_CASO_MINERO_NORTE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F24-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "Conectar en tiempo real las demandas territoriales con las restricciones financieras y normativas de la sede central.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F25", "P01-F26"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f22_f24.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
