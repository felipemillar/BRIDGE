import json
import os
import sys

# Append P01-F16, P01-F17, P01-F18 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F16",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones definen la representación estructurada de este tema?",
        "snapshot_at": "2026-10-01T00:43:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de los JTBD y momentos de presión se define por 3 categorías de trabajos (Funcionales JTBD-F1 a F3, Emocionales JTBD-E1 a E2, y Sociales JTBD-S1 a S2), 6 escenarios de fricción decisional crítica (Comité C-Suite, Directorio/ESG, Audiencia Ley de Lobby, Comité de Crisis Golden Hour, Punto de Prensa, y Mesa Territorial), dependencias temporales estrictas (Golden Hour de 30-60 min y reducción de briefing de 4 horas a <15 min), y condiciones de éxito de cero contradicciones y preservación de la Licencia Social para Operar.",
        "findings": [
            {
                "claim_id": "P01-F16-C1",
                "claim": "Los trabajos por hacer se categorizan formalmente en 3 dimensiones: Funcionales (JTBD-F1 Briefing Ejecutivo, JTBD-F2 Detección Temprana, JTBD-F3 Lines to Take), Emocionales (JTBD-E1 Temple y Control, JTBD-E2 Reducción de Ansiedad de Crisis) y Sociales (JTBD-S1 Posicionamiento en C-Suite, JTBD-S2 Preservación de Licencia Social).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gerencias de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 1: Taxonomía de JTBD Funcionales, Emocionales y Sociales",
                        "excerpt_short": "JTBD-F1 a F3, JTBD-E1 a E2, JTBD-S1 a S2.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Taxonomía consolidada en el dossier de investigación del corpus."
            },
            {
                "claim_id": "P01-F16-C2",
                "claim": "Los seis escenarios de reunión de máxima fricción son: Comité Ejecutivo C-Suite, Sesión de Directorio/Comité ESG, Audiencia de Ley de Lobby N° 20.730, Comité de Crisis en Golden Hour (30-60 min), Punto de Prensa o Entrevista Exclusiva, y Mesa de Diálogo Territorial con comunidades.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "C-Suite y Directores Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Escenarios de Reunión y Fricción Decisional",
                        "excerpt_short": "6 escenarios de reunión: C-Suite, Directorio ESG, Ley de Lobby, Crisis Golden Hour, Prensa y Mesa Territorial.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F16-C3",
                "claim": "La ventana temporal de la Golden Hour de crisis impone fijar la primera postura oficial (holding statement) entre 30 y 60 minutos antes de la viralización pública de la controversia.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Gestores de Crisis y CCOs"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección: Crisis response and Golden Hour window",
                        "excerpt_short": "La ventana de respuesta de 30 a 60 minutos es crítica para contener la narrativa pública.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicación de liderazgo estratégico de McKinsey."
            }
        ],
        "operational_model": {
            "inputs": ["Señales externas de alerta", "Actas y compromisos internos", "Directrices normativas CMF/Lobby"],
            "actors": ["Director de Asuntos Corporativos (CCO)", "Gerente de Asuntos Públicos", "Gerente de Prensa", "Gerente de Sostenibilidad"],
            "steps": ["Identificación del escenario de reunión", "Activación del protocolo temporal", "Generación de briefing asistido", "Control cruzado de contradicciones", "Despliegue de vocería"],
            "states": ["Escenario_Identificado", "Protocolo_Activado", "Briefing_Generado", "Vocería_Alineada"],
            "outputs": ["Briefing asistido en <15 min", "Holding statement en <30 min", "Líneas discursivas alineadas"],
            "exceptions": ["Superación de la ventana de 60 minutos en crisis", "Desalineación entre Gerencia de Prensa y Fiscalía Legal"]
        },
        "entities": [
            {"entity_id": "ENT_JTBD_DIMENSIONS", "type": "marco_metodologico", "name": "Dimensiones de Jobs-to-be-Done en Asuntos Corporativos", "aliases": ["JTBD Funcional, Emocional y Social"]},
            {"entity_id": "ENT_ESCENARIOS_FRICCION", "type": "concepto_operativo", "name": "Escenarios de Reunión y Fricción Decisional", "aliases": ["Matriz de 6 Escenarios"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "gestiona_friccion_en", "object_id": "ENT_ESCENARIOS_FRICCION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F16-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Diseñar flujos de trabajo específicos para los 6 escenarios de reunión identificados, asegurando tiempos de respuesta adaptados a la Golden Hour.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F17", "P01-F18"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F17",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada afirmación de este tema?",
        "snapshot_at": "2026-10-01T00:43:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El tema está respaldado por 11 fuentes estructuradas en 4 niveles epistemológicos: Hechos Documentados (Dircom ECE 2025: 54% reporte a CEO; Ley 20.730 de Lobby; CMF NCG 461; LCM Brecha CommTech <30% adopción madura; Cadem Marcas Ciudadanas 2026; Merco Chile 2025 auditado por KPMG); Evidencia Académica (GCF Global Alliance 2021 sobre Inteligencia Contextual; Page Society 2022/2023 sobre el CCO Integrador; PRSA Code of Ethics); Afirmaciones Comerciales (McKinsey 2025 sobre agentes de IA y briefings); e Hipótesis de Trabajo de diseño (HT-1 y HT-2 sobre reducción de 4 horas a <15 min).",
        "findings": [
            {
                "claim_id": "P01-F17-C1",
                "claim": "Los informes de EUPRERA / Latin American Communication Monitor (LCM 2022-2024) documentan una severa brecha CommTech en América Latina: aunque más del 75% reconoce la relevancia de IA y datos, menos del 30% de los departamentos de comunicación dispone de herramientas maduras de CommTech o formación en algoritmos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2024", "region": "América Latina", "actor": "EUPRERA / LCM"},
                "evidence": [
                    {
                        "source_id": "1bc7878d-6979-4674-8b63-0cf41f89bb73",
                        "source_title": "Latin American Communication Monitor (LCM / EUPRERA) - Adopción de Tecnología, Ética y Brecha Digital en Dircoms",
                        "original_url": "https://www.comunicacionpolitica.org/lcm-informe/",
                        "locator": "Sección: Brecha digital y analítica en departamentos de comunicación",
                        "excerpt_short": "Menos del 30% de los departamentos de comunicación en América Latina cuenta con herramientas maduras de CommTech.",
                        "source_date": "2024-06-15",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio empírico longitudinal académico de EUPRERA."
            },
            {
                "claim_id": "P01-F17-C2",
                "claim": "El Global Capability Framework (GCF 2021) de Global Alliance define como capacidad profesional clave la 'Inteligencia Contextual': habilidad de ver el panorama amplio (social, político, regulatorio, tecnológico) para anticipar amenazas y oportunidades estratégicas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021", "region": "Global", "actor": "Global Alliance / Univ. of Huddersfield"},
                "evidence": [
                    {
                        "source_id": "a904d924-f726-444f-b9f1-320ec2c50dd3",
                        "source_title": "Global Alliance for Public Relations and Communication Management - Global Capability Framework (GCF)",
                        "original_url": "https://www.globalalliancepr.org/global-capability-framework",
                        "locator": "Dimensión de Inteligencia Contextual",
                        "excerpt_short": "To provide contextual intelligence: You see the bigger picture – socially, culturally, politically, technologically and economically.",
                        "source_date": "2021-05-18",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco de referencia profesional global respaldado por universidades y asociaciones internacionales."
            },
            {
                "claim_id": "P01-F17-C3",
                "claim": "En los rankings de reputación en Chile, Merco (auditado por KPMG bajo norma ISAE 3000) y Cadem (Marcas Ciudadanas, 18ª edición 2026) establecen que la evaluación del C-Suite se vincula estrictamente a la conducta ética, transparencia y aporte a la calidad de vida comunitaria.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "Merco Chile / Cadem"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección de Benchmarks Reputacionales: Merco y Cadem",
                        "excerpt_short": "Merco auditado bajo ISAE 3000 y Cadem Marcas Ciudadanas 2026 vinculan la reputación directiva a conducta ética y gobernanza.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Metodologías de auditoría y medición empírica consolidadas en el mercado chileno."
            }
        ],
        "operational_model": {
            "inputs": ["Estudios empíricos ECE y LCM", "Marcos normativos chilenos", "Estándares deontológicos GCF y PRSA"],
            "actors": ["Auditor de Fuentes", "Analista de Investigación"],
            "steps": ["Verificación de afiliación de fuentes", "Extracción de citas con localizador", "Mapeo de nivel epistemológico", "Registro de trazabilidad"],
            "states": ["Fuentes_Identificadas", "Clasificadas", "Trazabilidad_Verificada"],
            "outputs": ["Matriz de Trazabilidad Auditable"],
            "exceptions": ["Identificación de fuentes comerciales sin validación empírica independiente"]
        },
        "entities": [
            {"entity_id": "ENT_EUPRERA_LCM", "type": "organizacion_academica", "name": "Latin American Communication Monitor (LCM / EUPRERA)", "aliases": ["LCM EUPRERA"]},
            {"entity_id": "ENT_GLOBAL_ALLIANCE", "type": "organizacion", "name": "Global Alliance for Public Relations and Communication Management", "aliases": ["Global Alliance"]},
            {"entity_id": "ENT_CADEM", "type": "empresa_investigacion", "name": "Cadem Chile", "aliases": ["Cadem Plaza Pública", "Marcas Ciudadanas"]},
            {"entity_id": "ENT_MERCO", "type": "empresa_investigacion", "name": "Merco Chile", "aliases": ["Monitor Empresarial de Reputación Corporativa"]}
        ],
        "relations": [
            {"subject_id": "ENT_GLOBAL_ALLIANCE", "predicate": "publica_marco", "object_id": "Global Capability Framework", "valid_from": "2021", "valid_to": None, "evidence_claim_id": "P01-F17-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Porcentaje de adopción madura de CommTech en departamentos de comunicación en LatAm",
                "value": "<30%",
                "denominator": "Total de directores de comunicación encuestados por LCM en América Latina",
                "source_claim_id": "P01-F17-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Incorporar la noción de 'Inteligencia Contextual' del GCF como principio rector de la síntesis ejecutiva multivariable en BRIDGE.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F18", "P01-F19"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F18",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto con entradas y resultado esperado ilustra este tema en la práctica?",
        "snapshot_at": "2026-10-01T00:43:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso de una empresa industrial en Chile convocada a audiencia urgente bajo Ley 20.730 de Lobby a 30 minutos de iniciar, en paralelo a un reportaje regional sobre presuntos incumplimientos hídricos de una RCA, ilustra el tema: cruzando actas previas de InfoLobby, la Memoria NCG 461 de la CMF y la RCA ambiental en un entorno VPC privado, el sistema genera un briefing de 1 página con trazabilidad en menos de 15 minutos, logrando cero contradicciones con la Fiscalía Legal y neutralizando la controversia.",
        "findings": [
            {
                "claim_id": "P01-F18-C1",
                "claim": "En un escenario de alta tensión simultánea (audiencia urgente de Lobby bajo Ley 20.730 a 30 minutos de iniciar y reportaje de prensa sobre supuesta infracción de una RCA), las entradas documentadas comprenden actas históricas de InfoLobby, la Memoria Integrada NCG 461 CMF, las resoluciones ambientales y el clipping mediático en tiempo real.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresa Industrial / Minera"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección: Caso Práctico de Fricción Temporal y Escenario de Lobby",
                        "excerpt_short": "Entradas del caso: Actas InfoLobby Ley 20.730, Memoria CMF NCG 461, RCA ambiental y monitoreo en tiempo real.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Flujo de trabajo documentado en el caso práctico del dossier."
            },
            {
                "claim_id": "P01-F18-C2",
                "claim": "El resultado esperado consiste en un briefing ejecutivo de 1 página con 3 bloques clave (postura oficial, datos verificados de RCA y respuestas a preguntas críticas) entregado en menos de 15 minutos con enlaces verificables a las fuentes, logrando consistencia absoluta con la declaración en el registro de agenda pública y la neutralización de la crisis.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "CEO y CCO"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección: Resultados Esperados del Caso Práctico",
                        "excerpt_short": "Briefing de 1 página en menos de 15 minutos, cero contradicciones y registro transparente en InfoLobby.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:43:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación del caso en el dossier P01."
            }
        ],
        "operational_model": {
            "inputs": ["Citación urgente de autoridad sectorial", "Reportaje mediático de presunta infracción RCA", "Repositorio documental interno"],
            "actors": ["Director de Asuntos Corporativos (CCO)", "Gerente General (CEO)", "Fiscal Legal", "Oficial de Seguridad (CISO)"],
            "steps": [
                "Notificación simultánea de audiencia y reportaje mediático",
                "Ingesta en entorno VPC privado de actas de InfoLobby, RCA y Memoria CMF",
                "Generación automatizada de briefing ejecutivo en 15 minutos",
                "Revisión y validación por Fiscalía Legal y CCO",
                "Comparecencia en audiencia y publicación de acta en InfoLobby"
            ],
            "states": ["Crisis_Declarada", "Briefing_Generado", "Legal_Visado", "Audiencia_Concluida", "Aclaración_Mediatica_Publicada"],
            "outputs": ["Briefing ejecutivo con citas verificadas", "Acta pública InfoLobby sin inconsistencias", "Aclaración técnica a medios regionales"],
            "exceptions": ["Imposibilidad de validar datos técnicos de la faena en menos de 15 minutos"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_LOBBY_MINERIA", "type": "caso_estudio", "name": "Caso Práctico: Contingencia Hídrica y Audiencia de Lobby", "aliases": ["Escenario de Crisis P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "aplica_procedimiento_en", "object_id": "ENT_CASO_LOBBY_MINERIA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F18-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Configurar el generador de minutas de BRIDGE para responder en menos de 15 minutos ante audiencias de lobby con respaldo de RCA y memorias CMF.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F19", "P01-F20"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f16_f18.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
