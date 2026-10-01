import json
import os
import sys

# Append P01-F40, P01-F41, P01-F42 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F40",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones definen la representación estructurada de este tema?",
        "snapshot_at": "2026-10-01T01:01:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de usuarios en Chile y LatAm se articula mediante: 3 estadios de madurez digital (baja/artesanal, media/estratégica, y avanzada/agéntica AI Lighthouses con brecha de <30% de CommTech según LCM); 3 perfiles organizacionales (grandes conglomerados familiares IPSA, empresas reguladas por Ley 20.730/NCG 461, y sectores territoriales minero/energéticos enfocados en SLO y RCA); relaciones B2B tripartitas (Usuario operativo, Comprador C-Suite y Aprobador con veto CISO/Legal); y condiciones de despliegue local de alta desconfianza institucional y transparencia obligatoria.",
        "findings": [
            {
                "claim_id": "P01-F40-C1",
                "claim": "La madurez digital de asuntos corporativos en América Latina presenta tres estadios: baja/artesanal (monitoreo en PDF y minutas manuales nocturnas), media/estratégica (escucha social activa y microsegmentación) y avanzada/agéntica (AI Lighthouses conectando repositorios internos con el entorno exterior).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "América Latina", "actor": "Gerencias de Comunicación y Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Estadios de Madurez Digital CommTech en LatAm",
                        "excerpt_short": "Tres estadios de madurez digital: artesanal (<30% madurez según LCM), estratégica y agéntica (AI Lighthouses).",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T01:01:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F40-C2",
                "claim": "La dinámica B2B en la región distingue rígidamente al Usuario (CCO/Asuntos Públicos que exige rapidez sin alucinaciones), el Comprador (CEO/CFO enfocado en ROI y protección reputacional) y el Aprobador crítico con poder de veto (CISO y Fiscal Legal que exigen aislamiento privado VPC y cero fuga de datos).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Estructura B2B Corporativa"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Tríada de Personas B2B (Usuario - Comprador - Aprobador)",
                        "excerpt_short": "Tríada B2B: CCO usuario, CEO comprador y CISO/Legal aprobadores con potestad de veto técnico.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T01:01:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            }
        ],
        "operational_model": {
            "inputs": ["Evaluación de madurez digital interna", "Perfil de propiedad corporativa", "Políticas de ciberseguridad del CISO"],
            "actors": ["Usuario Operativo (CCO/Analista)", "Comprador (CEO/Directorio)", "Aprobador Técnico (CISO/Fiscal Legal)"],
            "steps": ["Diagnóstico de madurez CommTech", "Configuración de entorno VPC privado", "Validación legal y de seguridad", "Despliegue de asistentes agénticos"],
            "states": ["Madurez_Evaluada", "VPC_Configurado", "Aprobación_CISO_Otorgada", "Sistema_Operativo"],
            "outputs": ["Matriz de roles B2B regionalizada", "Certificación de aislamiento de datos"],
            "exceptions": ["Objeción de seguridad del CISO ante modelos que retengan datos para entrenamiento"]
        },
        "entities": [
            {"entity_id": "ENT_ESTADIOS_MADUREZ", "type": "modelo_madurez", "name": "Estadios de Madurez Digital CommTech", "aliases": ["Madurez Artesanal, Estratégica y Agéntica"]},
            {"entity_id": "ENT_TRIADA_B2B", "type": "modelo_adopcion", "name": "Tríada B2B (Usuario - Comprador - Aprobador)", "aliases": ["Matriz de Decisión Tecnológica B2B"]}
        ],
        "relations": [
            {"subject_id": "ENT_TRIADA_B2B", "predicate": "condiciona_despliegue_de", "object_id": "Adopción_Tecnología_IA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F40-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Incorporar en BRIDGE la arquitectura multi-persona para separar los accesos operativos del CCO de los controles de auditoría del CISO.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F41", "P01-F42"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F41",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada afirmación de este tema?",
        "snapshot_at": "2026-10-01T01:01:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El tema se sustenta en 12 fuentes primarias catalogadas en 4 niveles epistemológicos: Hechos Documentados (BCN Ley 20.730; CMF NCG 461/519; Dircom ECE 2025; LCM/EUPRERA 2022-2024; ECM Retrospectiva 2023; Cadem Marcas Ciudadanas Jun 2026; Merco Chile 2025/2026; Acción Empresas Sep 2026; ICARE); Evidencia Académica (GCF Global Alliance 2021; Page Society The New CCO); Afirmaciones Comerciales (McKinsey Oct 2025); e Hipótesis de Trabajo (HT-1, HT-2, HT-3). Se reiteran 4 vacíos de evidencia delimitados formalmente.",
        "findings": [
            {
                "claim_id": "P01-F41-C1",
                "claim": "Los estudios longitudinales de EUPRERA (LCM 2022-2024 y ECM retrospectiva 2023) confirman con muestras representativas en América Latina y Europa la brecha estructural de competencias analíticas, donde menos del 30% dispone de CommTech maduro pese a la altísima expectativa teórica.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2024", "region": "América Latina y Europa", "actor": "EUPRERA"},
                "evidence": [
                    {
                        "source_id": "1bc7878d-6979-4674-8b63-0cf41f89bb73",
                        "source_title": "Latin American Communication Monitor (LCM / EUPRERA) - Adopción de Tecnología, Ética y Brecha Digital en Dircoms",
                        "original_url": "https://www.comunicacionpolitica.org/lcm-informe/",
                        "locator": "Estudio cuantitativo longitudinal de competencias digitales",
                        "excerpt_short": "Menos del 30% de los departamentos de comunicación en LatAm cuenta con herramientas maduras de CommTech.",
                        "source_date": "2024-06-15",
                        "retrieved_at": "2026-10-01T01:01:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Investigación académica empírica de EUPRERA."
            },
            {
                "claim_id": "P01-F41-C2",
                "claim": "En Chile, la confluencia entre los programas de 'Territorios Sostenibles' de Acción Empresas (septiembre 2026) y los índices de Merco y Cadem constata que la confianza pública depende directamente del comportamiento ético de los líderes y del cumplimiento fáctico de los acuerdos territoriales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "Acción Empresas / Merco / Cadem"},
                "evidence": [
                    {
                        "source_id": "c2dbae6a-963d-4471-ab12-823eab7384d1",
                        "source_title": "Acción Empresas Chile - Red de Sostenibilidad y Desafíos Ambientales, Sociales y Gobernanza (ASG)",
                        "original_url": "https://accionempresas.cl/",
                        "locator": "Gira Territorios Sostenibles y gestión ASG",
                        "excerpt_short": "Fortaleciendo la gestión territorial y la aplicación de estándares NIIF S1 y S2 en empresas chilenas.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:01:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Red empresarial líder de sostenibilidad en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Bases de datos de estudios empíricos", "Legislación chilena", "Reportes gremiales"],
            "actors": ["Investigador Académico", "Auditor de Normativa"],
            "steps": ["Verificación de registros bibliográficos", "Cotejo de citas textuales", "Mapeo de nivel epistemológico", "Aislamiento de Knowledge Gaps"],
            "states": ["Fuentes_Identificadas", "Citas_Verificadas", "Gaps_Aislados"],
            "outputs": ["Matriz de Trazabilidad de Fuentes Regionales"],
            "exceptions": ["Atribución de hechos empíricos a notas de prensa secundarias"]
        },
        "entities": [
            {"entity_id": "ENT_MATRIZ_FUENTES_REGIONALES", "type": "sistema_documental", "name": "Matriz de Fuentes y Respaldos Regionales P01", "aliases": ["Evidencia de Usuarios en Chile y LatAm"]}
        ],
        "relations": [
            {"subject_id": "ENT_MATRIZ_FUENTES_REGIONALES", "predicate": "respalda_afirmaciones_de", "object_id": "ENT_PERFIL_CCO_LATAM", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F41-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Indexar las 12 fuentes primarias regionales en la base documental canónica de BRIDGE.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F42", "P01-F43"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F42",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto con entradas y resultado esperado ilustra este tema en la práctica?",
        "snapshot_at": "2026-10-01T01:01:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso de una corporación minera/energética en Chile sujeta a la NCG 461 de la CMF y a la Ley N° 20.730 de Lobby que enfrenta simultáneamente una audiencia regulatoria ministerial y protestas comunitarias por recursos hídricos ilustra el tema: contrastando la operación artesanal tradicional (minutas manuales nocturnas en PDF que generan contradicciones fácticas) con la asistencia agéntica en VPC privada (cruce bidireccional de Memoria CMF, RCA y actas de InfoLobby en 12 minutos), el resultado esperado verifica cero discrepancias con los mercados financieros, 100% consistencia testimonial y respuesta oficial blindada en menos de 30 minutos.",
        "findings": [
            {
                "claim_id": "P01-F42-C1",
                "claim": "En una contingencia de alta exposición en Chile (audiencia de Lobby ministerial y movilización comunitaria hídrica simultánea), las entradas operativas ingresadas en entorno VPC seguro integran el capítulo hídrico de la Memoria CMF NCG 461, las RCA de la faena, convenios territoriales y señales de monitoreo en redes sociales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Corporación Minero-Energética"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Caso Práctico Regional de Adopción e Interacción",
                        "excerpt_short": "Entradas del caso: Memoria CMF NCG 461, RCA ambiental, InfoLobby y monitoreo mediático en tiempo real.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T01:01:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso práctico detallado en el dossier P01."
            },
            {
                "claim_id": "P01-F42-C2",
                "claim": "El resultado esperado verifica tres logros: cero contradicciones testimoniales entre lo declarado a la autoridad y lo reportado a la CMF, reducción del tiempo de elaboración de la minuta ejecutiva de 4 horas a 12 minutos, y capacidad de emitir un holding statement en menos de 30 minutos (Golden Hour) preservando la Licencia Social.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "CCO y Vocero Corporativo"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Resultados Esperados del Caso Práctico Regional",
                        "excerpt_short": "Resultados esperados: cero contradicciones con CMF, reducción a 12 minutos y holding statement en <30 min.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T01:01:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación de resultados verificables en el dossier."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria CMF NCG 461", "RCA faena", "InfoLobby histórico", "Monitoreo social regional"],
            "actors": ["CCO / Gerente de Asuntos Públicos", "Gerente General", "Fiscal Legal", "Oficial de Seguridad (CISO)"],
            "steps": [
                "Ingesta en entorno VPC privado aislado",
                "Cruce automatizado entre compromisos CMF/RCA y señales externas en 12 minutos",
                "Emisión de Briefing con Q&A y citas exactas",
                "Validación de CCO y Fiscal Legal",
                "Audiencia ministerial de lobby y respuesta en medios dentro de Golden Hour"
            ],
            "states": ["Crisis_Doble_Detectada", "Briefing_12min_Generado", "Legal_Visado", "Audiencia_Completada", "Holding_Statement_Emitido"],
            "outputs": ["Briefing ejecutivo trazable", "Holding statement fundamentado", "Acta pública InfoLobby consistente"],
            "exceptions": ["Discrepancia no documentada entre datos operacionales de faena y memoria CMF"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_REGIONAL_HIBRIDO", "type": "caso_estudio", "name": "Caso Regional de Contingencia Hídrica y Audiencia Ministerial", "aliases": ["Caso Práctico P01-F42"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_REGIONAL_HIBRIDO", "predicate": "valida_adopcion_de", "object_id": "ENT_ESTADIOS_MADUREZ", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F42-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Tiempo asistido de elaboración de briefing ejecutivo",
                "value": "12 minutos",
                "denominator": "Tiempo previo artesanal de 4 horas",
                "source_claim_id": "P01-F42-C2"
            }
        ],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Incorporar el flujo de resolución de crisis hídrico-regulatorio como plantilla predefinida en BRIDGE para empresas de recursos naturales en Chile.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F43", "P01-F44"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f40_f42.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
