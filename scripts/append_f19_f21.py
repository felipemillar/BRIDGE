import json
import os
import sys

# Append P01-F19, P01-F20, P01-F21 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F19",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cuáles son las 3 a 5 reuniones o instancias de decisión más críticas donde un usuario de asuntos corporativos necesita inteligencia rápida y confiable?",
        "snapshot_at": "2026-10-01T00:45:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Las 6 instancias de decisión más críticas son: 1) Comité Ejecutivo C-Suite (fijación de posturas corporativas ante reformas y alineamiento interfuncional); 2) Sesión de Directorio y Comité ESG (aprobación de Memorias NCG 461 de la CMF y gobernanza); 3) Audiencias de Ley de Lobby N° 20.730 en Chile (negociación técnica transparente ante sujetos pasivos); 4) Comités de Crisis (emergencias operacionales en Golden Hour); 5) Comparecencias parlamentarias y puntos de prensa (resguardo fáctico y bursátil); y 6) Mesas de diálogo territorial (gestión de compromisos comunitarios y licencias sociales).",
        "findings": [
            {
                "claim_id": "P01-F19-C1",
                "claim": "En el Comité Ejecutivo semanal, el CCO actúa como articulador interfuncional (54,4% reporte al CEO y 32,3% en Comité de Dirección según Dircom ECE 2025) para definir posturas corporativas y resolver discrepancias entre Legal, Regulatorio y Operaciones.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "España / Habla Hispana", "actor": "Dircoms y C-Suite"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Asociación de Directivos de Comunicación (Dircom España) - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Resultados de gobernanza ECE 2025",
                        "excerpt_short": "54,4% de los dircoms reporta al CEO y el 32,3% forma parte permanente del comité ejecutivo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Encuesta cuantitativa formal de Dircom España."
            },
            {
                "claim_id": "P01-F19-C2",
                "claim": "En Chile, las Audiencias bajo la Ley N° 20.730 de Lobby son instancias críticas obligatorias de transparencia activa ante autoridades y legisladores, con riesgo de sanciones por inconsistencias testimoniales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Sujetos Pasivos y Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 3°, 4° y 8°",
                        "excerpt_short": "Obligación de registrar audiencias, asistentes, mandante y materia tratada en la plataforma InfoLobby.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Ley de la República vigente en Chile."
            },
            {
                "claim_id": "P01-F19-C3",
                "claim": "En Directorios y Comités ESG rige la fiscalización de la Memoria Anual Integrada bajo la NCG 461 de la CMF, mientras que en Mesas Territoriales rige la preservación de la Licencia Social para Operar vinculada a resoluciones ambientales (RCA).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile", "actor": "Directorios y Comunidades"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Marco de memorias integradas obligatorias",
                        "excerpt_short": "Supervisión de divulgación de riesgos ASG y gobierno corporativo ante el directorio y la CMF.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Regulación formal CMF y directrices territoriales en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Agendas regulatorias", "Planes de inversión", "Hechos esenciales", "Demandas de partes interesadas"],
            "actors": ["CEO", "CCO / Dircom", "Fiscal Legal", "Gerente de Asuntos Públicos", "Directorio"],
            "steps": ["Convocatoria formal", "Levantamiento de inteligencia estratégica", "Deliberación y fijación de postura", "Votación o aprobación", "Seguimiento y reporte público"],
            "states": ["Convocada", "En_Preparación", "En_Sesión", "Acuerdos_Formalizados"],
            "outputs": ["Actas de Directorio", "Actas InfoLobby", "Lines to take ejecutivos"],
            "exceptions": ["Desacuerdo entre Legal y Asuntos Públicos sobre interpretación normativa"]
        },
        "entities": [
            {"entity_id": "ENT_C_SUITE", "type": "organo_gobierno", "name": "Comité Ejecutivo C-Suite", "aliases": ["Comité de Dirección"]},
            {"entity_id": "ENT_AUDIENCIA_LOBBY", "type": "instancia_regulatoria", "name": "Audiencia Ley de Lobby N° 20.730", "aliases": ["Audiencia InfoLobby"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "participa_en", "object_id": "ENT_C_SUITE", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F19-C1"},
            {"subject_id": "ENT_ASUNTOS_PUBLICOS", "predicate": "gestiona", "object_id": "ENT_AUDIENCIA_LOBBY", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F19-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Crear vistas y artefactos específicos para las 6 instancias de decisión clave, facilitando la preparación en los tiempos de corte requeridos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F20", "P01-F21"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F20",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué información específica necesita antes, durante y después de cada una de esas reuniones?",
        "snapshot_at": "2026-10-01T00:45:00-03:00",
        "answer_status": "respondida",
        "short_answer": "En la fase ANTES necesita briefings con cruce fáctico de posturas históricas (NCG 461, actas previas), detección de inconsistencias intergerenciales y minutas de Q&A con citas; DURANTE requiere monitoreo de sentimiento y datos del entorno en tiempo real con estricta adherencia a holding statements aprobados para evitar improvisaciones; y DESPUÉS exige registros regulatorios obligatorios (inscripción en InfoLobby bajo Ley 20.730), actas de compromisos operativos y actualización de la memoria ASG.",
        "findings": [
            {
                "claim_id": "P01-F20-C1",
                "claim": "Antes de una reunión crítica o audiencia de lobby, el usuario necesita un briefing que cruce el repositorio interno (memorias CMF NCG 461, actas anteriores de InfoLobby, RCA ambientales) con el perfil y votaciones del interlocutor para detectar contradicciones.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Asuntos Corporativos y CCOs"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Requerimientos de Información Antes, Durante y Después",
                        "excerpt_short": "Fase Antes: cruce de memorias CMF, actas de InfoLobby y perfiles de autoridades para evitar contradicciones.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F20-C2",
                "claim": "Durante la reunión, el vocero requiere dashboards de señales en tiempo real y soporte inmediato para adherir estrictamente a los argumentarios (lines to take) sin caer en improvisaciones que comprometan judicial o reputacionalmente a la empresa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Portavoces Corporativos"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección: Real-time decision support in executive meetings",
                        "excerpt_short": "Adherencia estricta a posturas validadas para evitar riesgos en reuniones de alta tensión geopolítica o regulatoria.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicación estratégica de McKinsey."
            },
            {
                "claim_id": "P01-F20-C3",
                "claim": "Después de la reunión, la Ley N° 20.730 en Chile exige el registro obligatorio y transparente en la plataforma de agenda pública (InfoLobby) detallando asistentes, mandante y materia tratada, además de la protocolización de compromisos operativos internos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Sujetos Pasivos y Gestores de Intereses"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 8° y 9°",
                        "excerpt_short": "Ingreso obligatorio en el Registro de Agenda Pública de las materias tratadas y asistentes dentro de los plazos legales.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Ley de la República vigente en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Bases de datos de lobby", "Reportes CMF", "Transcripciones y minutas previas"],
            "actors": ["Preparador de Briefing", "Vocero Oficial", "Oficial de Registro de Lobby"],
            "steps": ["Generación de briefing previo", "Soporte táctico durante la reunión", "Redacción de minuta posterior", "Inscripción en registro legal público"],
            "states": ["Fase_Previa", "Fase_Durante", "Fase_Posterior", "Completada_y_Auditada"],
            "outputs": ["Briefing pre-reunión", "Monitoreo en vivo", "Acta oficial InfoLobby"],
            "exceptions": ["Omisión del registro de materias tratadas en los plazos fijados por la Ley 20.730"]
        },
        "entities": [
            {"entity_id": "ENT_FASE_PREVIA", "type": "fase_operativa", "name": "Fase Antes: Preparación de Briefing"},
            {"entity_id": "ENT_FASE_POSTERIOR", "type": "fase_operativa", "name": "Fase Después: Registro y Trazabilidad"}
        ],
        "relations": [
            {"subject_id": "ENT_FASE_PREVIA", "predicate": "previene_errores_en", "object_id": "Voceria_Corporativa", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F20-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Estructurar la extracción de información en tres etapas (Antes-Durante-Después), automatizando la generación de actas de seguimiento.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F21", "P01-F22"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F21",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Con qué frecuencia ocurren esas reuniones y con qué anticipación se preparan habitualmente?",
        "snapshot_at": "2026-10-01T00:45:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La periodicidad y anticipación documentadas son: Comité Ejecutivo (semanal, preparado con 24-48 horas de anticipación); Sesión de Directorio / ESG (mensual/trimestral, preparada con 1-2 semanas); Audiencias de Lobby (quincenal o a requerimiento, preparadas con 3-7 días); Comparecencias parlamentarias (ad-hoc, 3-5 días); Mesas territoriales (mensual/bimensual, 1-2 semanas); y Comités de Crisis (ad-hoc 24/7 reactivo, con ventana de Golden Hour de <30 a 60 minutos). Sin embargo, existe un vacío empírico auditado sobre las horas-hombre exactas invertidas en preparar briefings (Knowledge Gap 1).",
        "findings": [
            {
                "claim_id": "P01-F21-C1",
                "claim": "Las reuniones planificadas operan con cadencias predecibles: Comités Ejecutivos con frecuencia semanal y 24 a 48 horas de preparación previa; Sesiones de Directorio y Comités ESG con frecuencia mensual o trimestral y 1 a 2 semanas de anticipación.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global / Chile", "actor": "C-Suite y Directorios"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Frecuencia y Cadencia de Reuniones Corporativas",
                        "excerpt_short": "Comité Ejecutivo semanal (24-48 hrs de preparación) y Directorio mensual/trimestral (1-2 semanas).",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Cadencias estándar documentadas en el dossier P01."
            },
            {
                "claim_id": "P01-F21-C2",
                "claim": "En contingencias y comités de crisis, la periodicidad es ad-hoc 24/7 y la preparación es inmediata, operando bajo la restricción extrema de la Golden Hour de 30 a 60 minutos para formular la postura inicial.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Gestores de Crisis"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Respuesta inmediata ante permacrisis",
                        "excerpt_short": "Ventana de respuesta inmediata dentro de la primera hora de crisis para evitar captura de narrativa.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Literatura de gestión de crisis de McKinsey."
            },
            {
                "claim_id": "P01-F21-C3",
                "claim": "Existe una brecha crítica de evidencia (Knowledge Gap 1): no existen en la literatura pública datos cuantitativos auditados por ERP sobre las horas-hombre exactas invertidas en preparar un briefing book, tratándose internamente como una hipótesis de trabajo (HT-2: de 3-5 horas a <15 minutos).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Literatura de Gestión de PR"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Knowledge Gap 1: Falta de auditorías de horas-hombre en preparación de briefings",
                        "excerpt_short": "No existen mediciones auditadas de horas-hombre en elaboración de briefings en la literatura gremial pública.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:45:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico formal documentado en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Calendario anual de directorio", "Solicitudes de audiencias", "Alertas operacionales 24/7"],
            "actors": ["Secretario de Directorio", "Jefe de Asuntos Públicos", "Comité de Crisis"],
            "steps": ["Planificación de calendario", "Fijación de hitos de entrega de briefings", "Monitoreo de horas de dedicación", "Ajuste de tiempos según urgencia"],
            "states": ["Programada", "En_Preparación", "Urgente_Golden_Hour", "Cerrada"],
            "outputs": ["Cronograma de reuniones", "Briefing de contingencia"],
            "exceptions": ["Convocatoria intempestiva de comisión investigadora parlamentaria con menos de 24 horas de aviso"]
        },
        "entities": [
            {"entity_id": "ENT_CADENCIA_REUNIONES", "type": "concepto_operativo", "name": "Cadencia y Frecuencia de Reuniones Corporativas", "aliases": ["Calendario de Gobernanza"]},
            {"entity_id": "ENT_GAP_HORAS_HOMBRE", "type": "vacio_evidencia", "name": "Knowledge Gap 1: Horas-Hombre en Briefings", "aliases": ["Vacío de Métricas de Tiempo"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_HORAS_HOMBRE", "predicate": "limita_validacion_de", "object_id": "HT-2", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F21-C3"}
        ],
        "comparisons": [
            {
                "dimension": "Frecuencia y Tiempo de Preparación por Instancia",
                "Comité Ejecutivo": "Semanal | Preparación: 24 a 48 horas previas.",
                "Directorio / ESG": "Mensual o Trimestral | Preparación: 1 a 2 semanas previas.",
                "Audiencia Ley de Lobby": "Quincenal / A requerimiento | Preparación: 3 a 7 días hábiles.",
                "Comité de Crisis": "Reactiva 24/7 | Preparación: <30 a 60 minutos (Golden Hour)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Anticipar", "implication": "Automatizar alertas según la cadencia de cada reunión y ofrecer flujos de preparación inmediata para la Golden Hour.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap": "sin_evidencia sobre mediciones auditadas de horas-hombre en preparación de briefings ejecutivos en grandes empresas.",
                "minimum_validation": "Medición empírica mediante registro de tiempos en 10 gerencias de asuntos corporativos en Santiago.",
                "priority": "alta"
            }
        ],
        "next_question_ids": ["P01-F22", "P01-F23"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f19_f21.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
