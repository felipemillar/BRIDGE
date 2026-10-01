import json
import os
import sys

# Append P01-F13, P01-F14, P01-F15 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F13",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cuáles son los 5 a 10 trabajos por hacer (jobs-to-be-done) principales del usuario de inteligencia en asuntos corporativos, diferenciando funcionales, emocionales y sociales?",
        "snapshot_at": "2026-10-01T00:40:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los 7 JTBD clave del usuario se estructuran en tres dimensiones: 3 Funcionales (JTBD-F1 Briefing Ejecutivo Asistido, JTBD-F2 Detección Temprana de Señales e Issue Management, JTBD-F3 Alineamiento de Vocería e Inteligencia Interna); 2 Emocionales (JTBD-E1 Seguridad y Temple ante audiencias críticas, JTBD-E2 Reducción de fatiga cognitiva y ansiedad de crisis 24/7); y 2 Sociales (JTBD-S1 Legitimidad y asiento estratégico en el Comité Ejecutivo ante el CEO, JTBD-S2 Preservación de la Licencia Social para Operar y reputación fáctica).",
        "findings": [
            {
                "claim_id": "P01-F13-C1",
                "claim": "Los trabajos funcionales primarios son JTBD-F1 (preparación de briefing ejecutivo asistido cruzando posturas oficiales previas con controversias del interlocutor para evitar contradicciones), JTBD-F2 (detección temprana de señales regulatorias y de prensa para calcular value-at-stake) y JTBD-F3 (alineamiento de vocería e inteligencia interna mediante lines-to-take corporativos).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "CCOs y Gerentes de Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1: Taxonomía de Jobs-to-be-Done (JTBD-F1 a JTBD-F3)",
                        "excerpt_short": "JTBD-F1: Briefing Ejecutivo Asistido... JTBD-F2: Detección Temprana de Señales... JTBD-F3: Alineamiento de Vocería.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F13-C2",
                "claim": "Los trabajos emocionales son JTBD-E1 (control técnico, temple y tranquilidad subjetiva al no enfrentar preguntas trampa sin respaldo fáctico ante reguladores o prensa) y JTBD-E2 (reducción de sobrecarga mental y ansiedad operativa durante contingencias 24/7 y la primera hora de crisis).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Portavoces Corporativos y CCOs"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1: Taxonomía de JTBD Emocionales (JTBD-E1 y JTBD-E2)",
                        "excerpt_short": "JTBD-E1: Seguridad y Confianza Personal... JTBD-E2: Reducción de la Ansiedad de Crisis y Fatiga Cognitiva.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F13-C3",
                "claim": "Los trabajos sociales y organizacionales son JTBD-S1 (ser reconocido por el CEO y Directorio como un socio estratégico de gobernanza con asiento en el Comité Ejecutivo) y JTBD-S2 (construir y preservar la Licencia Social para Operar y credibilidad de largo plazo).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "España / Chile", "actor": "Dircoms y C-Suite"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Asociación de Directivos de Comunicación (Dircom España) - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Posicionamiento estratégico y pertenencia al Comité Ejecutivo (33%)",
                        "excerpt_short": "El 53,6% reporta al CEO y el 33% forma parte permanente del comité ejecutivo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio empírico ECE 2025."
            }
        ],
        "operational_model": {
            "inputs": ["Demandas informativas de stakeholders", "Señales regulatorias y de prensa", "Documentos corporativos históricos"],
            "actors": ["CCO / Dircom", "Gerente de Asuntos Públicos", "Portavoz Corporativo / CEO", "Gerente de Sostenibilidad"],
            "steps": ["Detección de señal o solicitud de reunión", "Activación del JTBD correspondiente", "Generación de insumo o briefing", "Validación interfuncional", "Comparecencia o vocería"],
            "states": ["Señal_Detectada", "Procesamiento_JTBD", "Insumo_Generado", "Vocería_Ejecutada"],
            "outputs": ["Briefing ejecutivo sin contradicciones", "Alerta temprana con cálculo de value-at-stake", "Lines-to-take unificados", "Blindaje de SLO"],
            "exceptions": ["Contradicción inadvertida con declaraciones históricas en InfoLobby", "Falta de validación técnica de Operaciones o Legal"]
        },
        "entities": [
            {"entity_id": "ENT_JTBD_F1", "type": "trabajo_por_hacer", "name": "JTBD-F1: Briefing Ejecutivo Asistido", "aliases": ["Preparación de Minuta Ejecutiva"]},
            {"entity_id": "ENT_JTBD_F2", "type": "trabajo_por_hacer", "name": "JTBD-F2: Detección Temprana e Issue Management", "aliases": ["Gestión de Asuntos Críticos"]},
            {"entity_id": "ENT_JTBD_S1", "type": "trabajo_por_hacer", "name": "JTBD-S1: Posicionamiento Estratégico en C-Suite", "aliases": ["Asiento en Comité Ejecutivo"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "ejecuta_trabajo", "object_id": "ENT_JTBD_F1", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F13-C1"},
            {"subject_id": "ENT_CCO", "predicate": "persigue_objetivo", "object_id": "ENT_JTBD_S1", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F13-C3"}
        ],
        "comparisons": [
            {
                "dimension": "Dimensión del Trabajo por Hacer",
                "Funcional": "Cruzar datos, redactar minutas en minutos y unificar lines-to-take para evitar contradicciones.",
                "Emocional": "Disminuir fatiga cognitiva, evitar el pánico escénico y sentir temple y control técnico.",
                "Social": "Validar su rol estratégico ante el CEO y Directorio y blindar la licencia social institucional."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Estructurar los motores de búsqueda para resolver directamente el JTBD-F1 (briefings trazables) y JTBD-F2 (alertas de issue management).", "status": "evidencia"},
            {"module": "Actuar", "implication": "Proveer plantillas de lines-to-take automáticas para responder al JTBD-F3.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F14", "P01-F15"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F14",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cuáles son los momentos de mayor presión, riesgo o fricción en el flujo de trabajo de estos usuarios?",
        "snapshot_at": "2026-10-01T00:40:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los 7 momentos de máxima presión son: 1) Audiencias de Lobby bajo Ley 20.730 (riesgo de discrepancia pública entre lo hablado y memorias CMF); 2) Comités de crisis y Golden Hour (riesgo de emitir posturas sin causa raíz confirmada); 3) Comparecencias en comisiones parlamentarias (asimetría de información y preguntas trampa); 4) Reportabilidad ASG de la NCG 461 de la CMF (riesgo de greenwashing o multas); 5) Entrevistas de investigación financiera; 6) Mesas de diálogo territorial (tensión entre compromisos de faena y RCA); y 7) Sesiones de Directorio bajo la paradoja del atrapamiento táctico artesanal.",
        "findings": [
            {
                "claim_id": "P01-F14-C1",
                "claim": "En Chile, las audiencias bajo Ley N° 20.730 de Lobby son momentos de fricción legal crítica debido a la obligación de publicar el acta en InfoLobby, arriesgando sanciones o crisis reputacionales si existen contradicciones con declaraciones financieras o compromisos ambientales previos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Sujetos Pasivos y Empresas Reguladas"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Obligaciones de registro de audiencias y materias tratadas",
                        "excerpt_short": "Publicación obligatoria de agenda pública, sujetos activos, mandante y materia.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Ley de la República vigente en Chile."
            },
            {
                "claim_id": "P01-F14-C2",
                "claim": "Durante la primera hora de una emergencia operacional o ambiental (Golden Hour), la sobrecarga de rumores en redes frente a la lentitud de confirmación técnica genera una fricción crítica entre emitir un holding statement inmediato o esperar verificación fáctica completa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Comités de Crisis y CCOs"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Gestión de crisis y velocidad de respuesta",
                        "excerpt_short": "Tensión entre velocidad de contención en la primera hora y verificación fáctica para evitar daños irreversibles de reputación.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicación de McKinsey en el corpus."
            },
            {
                "claim_id": "P01-F14-C3",
                "claim": "La divulgación obligatoria de memorias ASG según la NCG 461 de la CMF expone a los directivos a severos riesgos de cargos sancionatorios o acusaciones de greenwashing si la narrativa comunicacional de sostenibilidad no coincide con las métricas contables y de auditoría.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2025", "region": "Chile", "actor": "Sociedades Anónimas Abiertas"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Fiscalización de la Memoria Integrada ASG",
                        "excerpt_short": "Fiscalización de la veracidad y consistencia de los reportes integrados frente a riesgos de manipulación informativa o greenwashing.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal financiera CMF."
            }
        ],
        "operational_model": {
            "inputs": ["Incidentes operacionales", "Citaciones de comisiones parlamentarias o reguladores", "Plazos de entrega NCG 461"],
            "actors": ["Comité de Crisis", "Vocero Oficial", "Fiscal de Compliance", "Director de Comunicaciones"],
            "steps": ["Ocurrencia del evento crítico", "Convocatoria urgente de comité", "Cotejo de datos operacionales e históricos", "Elaboración de postura oficial", "Despliegue y registro regulatorio"],
            "states": ["Incidente_Declarado", "Comité_Activo", "Borrador_En_Revisión", "Respuesta_Emitida"],
            "outputs": ["Holding statement verificado", "Briefing de contingencia", "Acta oficial InfoLobby"],
            "exceptions": ["Declaración discordante entre vocero y gerente de faena", "Filtración a prensa de borradores no auditados"]
        },
        "entities": [
            {"entity_id": "ENT_GOLDEN_HOUR", "type": "concepto_operativo", "name": "Golden Hour de Crisis", "aliases": ["Primera Hora de Contingencia"]},
            {"entity_id": "ENT_GREENWASHING", "type": "riesgo", "name": "Riesgo de Greenwashing / Falseamiento ASG", "aliases": ["Inconsistencia de Sostenibilidad"]}
        ],
        "relations": [
            {"subject_id": "ENT_GOLDEN_HOUR", "predicate": "determina_impacto_en", "object_id": "Reputacion_Corporativa", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F14-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Anticipar", "implication": "Crear alertas en tiempo real durante la Golden Hour para mitigar el pánico escénico y consolidar hechos en menos de 15 minutos.", "status": "hipotesis"},
            {"module": "Saber", "implication": "Cruzar automáticamente borradores de memorias ASG con la NCG 461 de la CMF para prevenir riesgos de greenwashing.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F15", "P01-F16"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F15",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué artefactos, entregables o salidas intermedias producen actualmente para responder a esos trabajos?",
        "snapshot_at": "2026-10-01T00:40:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los equipos corporativos producen actualmente 7 artefactos principales: 1) Briefing Books Ejecutivos (3 a 5 horas manuales); 2) Minutas Ejecutivas de 1-2 páginas (30 a 60 minutos); 3) Lines to Take y Q&A ejecutivos (2 a 4 horas); 4) Holding Statements de crisis (15 a 30 minutos); 5) Reportes de clipping y monitoreo matutino (diario, 06:00-08:00 AM); 6) Matrices de riesgo y Stakeholder Mapping (mensual/trimestral, 1-2 semanas); y 7) Memorias Integradas NCG 461 CMF (proceso intergerencial continuo de 3 a 5 meses).",
        "findings": [
            {
                "claim_id": "P01-F15-C1",
                "claim": "Los artefactos tácticos de respuesta rápida comprenden: Briefing Books ejecutivos (3 a 5 horas de producción manual), Minutas ejecutivas de 1 a 2 páginas (30 a 60 minutos), Lines to Take con Q&A (2 a 4 horas) y Holding Statements para contingencias (15 a 30 minutos).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gerencias de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1: Artefactos y Entregables del Flujo Corporativo",
                        "excerpt_short": "Briefing books (3 a 5 horas), minutas (30-60 min), lines to take (2-4 hrs), holding statements (15-30 min).",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier consolidado del corpus."
            },
            {
                "claim_id": "P01-F15-C2",
                "claim": "Los artefactos estratégicos y de gobernanza comprenden: Reportes diarios de clipping y monitoreo (elaborados entre 06:00 y 08:00 AM), Matrices de Stakeholder Mapping / Valor en Riesgo (actualización trimestral) y Memorias Integradas NCG 461 de la CMF (proceso continuo de 3 a 5 meses).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile / Global", "actor": "Equipos de Asuntos Públicos y ESG"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1: Artefactos Estratégicos y Regulatorios",
                        "excerpt_short": "Clipping diario matutino, matrices de stakeholders y reportes de memorias integradas NCG 461 (3 a 5 meses).",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier consolidado del corpus."
            },
            {
                "claim_id": "P01-F15-C3",
                "claim": "La reducción del tiempo de elaboración de un briefing book de 4 horas a menos de 15 minutos mediante inteligencia asistida es formalmente una Hipótesis de Trabajo (HT-2) sujeta a validación en campo.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Chile", "actor": "Diseño de Solución BRIDGE"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4: Hipótesis de Trabajo HT-2",
                        "excerpt_short": "Hipótesis HT-2: Reducción del tiempo de elaboración de briefings de 4 horas a 15 minutos mediante automatización y trazabilidad.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:40:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Formulada como hipótesis experimental en el mapa de evidencia."
            }
        ],
        "operational_model": {
            "inputs": ["Información de medios", "Bases regulatorias", "Acuerdos previos de stakeholders"],
            "actors": ["Analista de Asuntos Corporativos", "Jefe de Prensa", "Gerente de Asuntos Públicos", "CCO"],
            "steps": ["Recopilación de información", "Estructuración de contenido en plantilla", "Revisión cruzada con Legal", "Aprobación ejecutiva", "Distribución a voceros"],
            "states": ["Recopilación", "Borrador", "Revisión_Intergerencial", "Aprobado_para_Distribución"],
            "outputs": ["Briefing Book", "Minuta Ejecutiva", "Holding Statement", "Memoria NCG 461"],
            "exceptions": ["Demora superior a 4 horas en la consolidación de datos", "Omisión de antecedentes históricos de faena"]
        },
        "entities": [
            {"entity_id": "ENT_BRIEFING_BOOK", "type": "artefacto", "name": "Briefing Book Ejecutivo", "aliases": ["Dossier de Preparación de Vocero"]},
            {"entity_id": "ENT_LINES_TO_TAKE", "type": "artefacto", "name": "Lines to Take y Q&A", "aliases": ["Argumentario Corporativo"]},
            {"entity_id": "ENT_MEMORIA_NCG461", "type": "artefacto_regulatorio", "name": "Memoria Anual Integrada NCG 461 CMF", "aliases": ["Reporte ASG Integrado"]}
        ],
        "relations": [
            {"subject_id": "ENT_BRIEFING_BOOK", "predicate": "apoya_ejecucion_de", "object_id": "JTBD-F1", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F15-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Tiempo de Elaboración Tradicional vs Objetivo BRIDGE",
                "Briefing Book": "Tradicional: 3 a 5 horas manuales. Objetivo BRIDGE (HT-2): 15 minutos.",
                "Holding Statement": "Tradicional: 15 a 30 minutos bajo alta tensión.",
                "Memoria NCG 461": "Tradicional: 3 a 5 meses de proceso intergerencial."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Tiempo manual tradicional de elaboración de un Briefing Book",
                "value": "3 a 5 horas",
                "denominator": "Por cada reunión o audiencia ejecutiva de alto nivel",
                "source_claim_id": "P01-F15-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Implementar plantillas preconfiguradas de Briefing Books y Lines to Take para reducir tiempos a menos de 15 minutos (HT-2).", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F16", "P01-F17"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f13_f15.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
