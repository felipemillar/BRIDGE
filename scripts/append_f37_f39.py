import json
import os
import sys

# Append P01-F37, P01-F38, P01-F39 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F37",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué especificidades presentan los usuarios de asuntos corporativos en Chile y América Latina respecto de la literatura global?",
        "snapshot_at": "2026-10-01T00:58:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los usuarios en Chile y LatAm presentan tres especificidades críticas frente a la literatura anglosajona: 1) Concentración en conglomerados y grupos familiares controladores (supeditando la vocería al patrimonio y prudencia política de la familia en vez de accionistas anónimos dispersos); 2) Peso determinante de la Licencia Social para Operar (SLO) y gestión territorial en minería/energía (donde una falla detona litigios ambientales o parálisis de faena en terreno); y 3) Régimen regulatorio punitivo de transparencia activa en Chile (Ley N° 20.730 de Lobby y NCG 461 de la CMF) que vincula legal y contablemente las declaraciones del vocero con la responsabilidad administrativa directa.",
        "findings": [
            {
                "claim_id": "P01-F37-C1",
                "claim": "A diferencia de la literatura anglosajona que modela corporaciones de propiedad accionaria dispersa, en Chile y América Latina predomina la concentración en grandes conglomerados económicos y grupos familiares controladores (ej. Quiñenco, Copec, CAP, Cencosud), donde el CCO responde a directorios orientados a la preservación del patrimonio y reputación familiar.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Grupos Económicos Familiares"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Especificidades de Usuarios en Chile y América Latina",
                        "excerpt_short": "Estructura corporativa dominada por conglomerados familiares y grupos controladores en contraste con la literatura anglosajona.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F37-C2",
                "claim": "En Chile y la región, la prioridad de asuntos corporativos es la Licencia Social para Operar (SLO) en activos territoriales críticos (minería, energía, agroindustria), donde las fallas comunitarias acarrean la paralización física de faenas y litigios en Tribunales Ambientales, a diferencia del enfoque meramente mediático de la literatura anglosajona.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "Empresas con Faenas en Terreno"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Licencia Social y Gestión Territorial",
                        "excerpt_short": "La Licencia Social para Operar determina la continuidad física de las faenas en sectores de recursos naturales.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico y directrices territoriales en el corpus."
            },
            {
                "claim_id": "P01-F37-C3",
                "claim": "En Chile, la Ley N° 20.730 de Lobby (2014) y la NCG 461 de la CMF fijan un marco de transparencia activa obligatoria y fiscalización financiera directa que prohíbe las prácticas opacas de lobby indirecto o front groups habituales en Estados Unidos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Estado de Chile / CMF"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Obligación de publicidad de agenda pública",
                        "excerpt_short": "Publicidad activa obligatoria sobre audiencias, viajes y donativos ante autoridades.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal chilena vigente."
            }
        ],
        "operational_model": {
            "inputs": ["Estructura accionaria familiar", "Acuerdos territoriales en faena", "Exigencias de la Ley 20.730"],
            "actors": ["Director de Asuntos Corporativos (Chile)", "Directorio Familiar", "Comunidades Locales", "Regulador CMF"],
            "steps": ["Diagnóstico de gobernanza y control patrimonial", "Mapeo territorial comunitario", "Alineamiento con Ley de Lobby y CMF", "Ejecución de vocería con respaldo fáctico"],
            "states": ["Contexto_Regionalizado", "Gobernanza_Alineada", "Faena_Protegida", "Cumplimiento_Verificado"],
            "outputs": ["Estrategia de asuntos públicos adaptada a grupos familiares", "Protocolo de relacionamiento territorial"],
            "exceptions": ["Aplicación de recetas anglosajonas de activismo digital desconectadas de la faena en terreno"]
        },
        "entities": [
            {"entity_id": "ENT_GRUPOS_FAMILIARES_CHILE", "type": "estructura_corporativa", "name": "Conglomerados y Grupos Económicos Familiares en Chile", "aliases": ["Grupos Controladores Familiares"]},
            {"entity_id": "ENT_PERFIL_CCO_LATAM", "type": "perfil_profesional", "name": "Perfil del CCO en Chile y América Latina", "aliases": ["Gestor de Riesgos Normativos y Territoriales"]}
        ],
        "relations": [
            {"subject_id": "ENT_PERFIL_CCO_LATAM", "predicate": "gestiona_riesgos_para", "object_id": "ENT_GRUPOS_FAMILIARES_CHILE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F37-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Chile/LatAm vs Literatura Global Anglosajona",
                "Propiedad": "LatAm: Conglomerados y familias controladoras | Global: Propiedad accionaria dispersa.",
                "Prioridad": "LatAm: Licencia Social para Operar y faenas territoriales | Global: Activismo de stakeholders y marca digital.",
                "Regulación": "LatAm (Chile): Transparencia activa obligatoria (Ley 20.730 y CMF) | Global: PACs, advocacy y lobby indirecto."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "Adaptar el mapeo de actores de BRIDGE a la estructura de propiedad familiar y a las comunidades territoriales chilenas.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F38", "P01-F39"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F38",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cuáles son las brechas de madurez digital, capacidades analíticas o adopción tecnológica documentadas en la región?",
        "snapshot_at": "2026-10-01T00:58:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Las investigaciones empíricas de EUPRERA / LCM documentan tres brechas severas: 1) Baja adopción de CommTech (<30% de los departamentos de comunicación en LatAm cuenta con herramientas maduras de analítica o escucha activa, pese a que >75% reconoce su importancia); 2) Predominio de procesos artesanales reactivos (revisión manual de prensa y Excel sin analítica predictiva); y 3) La 'Paradoja de la IA', donde a pesar de la alta expectativa (80% prioridad según ECE), la adopción real en la alta dirección está frenada por el temor racional al riesgo de alucinación fáctica y fuga de datos en plataformas públicas.",
        "findings": [
            {
                "claim_id": "P01-F38-C1",
                "claim": "Los estudios cuantitativos longitudinales del Latin American Communication Monitor (LCM / EUPRERA) demuestran que menos del 30% de los departamentos de comunicación corporativa en América Latina dispone de herramientas maduras de CommTech o escucha digital, persistiendo el trabajo manual artesanal.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2024", "region": "América Latina (hasta 20 países)", "actor": "EUPRERA / LCM"},
                "evidence": [
                    {
                        "source_id": "1bc7878d-6979-4674-8b63-0cf41f89bb73",
                        "source_title": "Latin American Communication Monitor (LCM / EUPRERA) - Adopción de Tecnología, Ética y Brecha Digital en Dircoms",
                        "original_url": "https://www.comunicacionpolitica.org/lcm-informe/",
                        "locator": "Estadística de adopción tecnológica <30%",
                        "excerpt_short": "Menos del 30% de los departamentos de comunicación en LatAm utiliza CommTech maduro, pese a que >75% reconoce su relevancia.",
                        "source_date": "2024-06-15",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Investigación cuantitativa académica formal de EUPRERA."
            },
            {
                "claim_id": "P01-F38-C2",
                "claim": "La 'Paradoja de la IA' en América Latina radica en que el temor a alucinaciones o fuga de secretos corporativos paraliza la adopción en la alta dirección, dado que el Código de Ética de la PRSA (ESA #22, julio 2026) y las leyes chilenas responsabilizan legal y deontológicamente a los humanos por las declaraciones emitidas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Dircoms y C-Suite"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: La Paradoja de la IA y el Riesgo de Alucinación",
                        "excerpt_short": "Paradoja de la IA: alta expectativa teórica frenada por el temor justificado a alucinaciones y fuga de datos en el C-Suite.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            }
        ],
        "operational_model": {
            "inputs": ["Encuestas LCM/ECM", "Planes de capacitación corporativa", "Directrices deontológicas PRSA"],
            "actors": ["Dircom", "Analista de Inteligencia", "CISO", "Docente Universitario"],
            "steps": ["Evaluación de madurez CommTech", "Identificación de déficit analítico", "Diseño de salvaguardas anti-alucinación", "Capacitación en criterio humano sobre IA"],
            "states": ["Operación_Artesanal", "Brecha_Identificada", "Salvaguardas_Definidas", "Adopción_Segura"],
            "outputs": ["Diagnóstico de madurez CommTech", "Matriz de mitigación de alucinaciones"],
            "exceptions": ["Uso informal de LLMs públicos gratuitos por analistas sin conocimiento del CISO"]
        },
        "entities": [
            {"entity_id": "ENT_PARADOJA_IA", "type": "fenomeno_adopcion", "name": "Paradoja de la IA en Asuntos Corporativos", "aliases": ["Brecha entre Expectativa y Adopción Segura de IA"]}
        ],
        "relations": [
            {"subject_id": "ENT_PARADOJA_IA", "predicate": "frena_adopcion_en", "object_id": "ENT_PERFIL_CCO_LATAM", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F38-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Porcentaje de adopción madura de CommTech en departamentos de comunicación en LatAm",
                "value": "<30%",
                "denominator": "Total encuestados en monitor LCM",
                "source_claim_id": "P01-F38-C1"
            },
            {
                "metric": "Porcentaje de comunicadores que reconoce la relevancia de Big Data e IA",
                "value": ">75%",
                "denominator": "Total encuestados en monitor LCM",
                "source_claim_id": "P01-F38-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Superar la Paradoja de la IA proveyendo en BRIDGE verificación documental garantizada con cero alucinaciones y despliegue privado VPC.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F39", "P01-F40"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F39",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué factores culturales, regulatorios o de estructura organizacional explican esas diferencias?",
        "snapshot_at": "2026-10-01T00:58:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Cuatro factores estructurales explican las brechas: 1) Jerarquías tradicionales y subordinación funcional de la comunicación (aislando al CCO del directorio y absorbiendo >60% de su jornada en apagado de incendios tácticos); 2) Marcado centralismo geográfico en Santiago (casas matrices en Las Condes/Providencia desconectadas de las realidades territoriales de faenas en el norte y sur); 3) Desconfianza institucional estructural y escepticismo ciudadano (Cadem Marcas Ciudadanas 2026 y Merco) que castiga duramente cualquier inconsistencia como greenwashing; y 4) Aversión al riesgo regulatorio con potestad de veto técnico de CISO y Fiscal Legal ante herramientas no privadas.",
        "findings": [
            {
                "claim_id": "P01-F39-C1",
                "claim": "En Chile existe una disociación espacial crítica: los centros de decisión corporativa y los equipos de asuntos públicos se concentran físicamente en comunas del oriente de Santiago, mientras que los activos productivos y los conflictos socioambientales operan en faenas del norte y sur, generando minutas desconectadas de la realidad en terreno.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Corporaciones y Empresas Minero-Energéticas"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Centralismo Institucional en Santiago vs Territorio",
                        "excerpt_short": "Centralismo geográfico en Santiago frente a la realidad territorial de los activos en faenas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F39-C2",
                "claim": "Las mediciones de Cadem Marcas Ciudadanas (18ª ed., junio 2026, 385 marcas) y Merco Chile documentan una desconfianza estructural hacia las grandes empresas, imponiendo al vocero la obligación de verificar rigurosamente cada afirmación ante el riesgo de acusaciones inmediatas de greenwashing.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-06", "region": "Chile", "actor": "Cadem / Merco Chile"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Desconfianza Estructural y Marcas Ciudadanas Cadem 2026",
                        "excerpt_short": "Desconfianza institucional documentada por Cadem Marcas Ciudadanas 2026 y Merco, que exige verificación fáctica estricta.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:58:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Encuesta empírica nacional de Cadem y ranking Merco."
            }
        ],
        "operational_model": {
            "inputs": ["Estructura organizacional jerárquica", "Mapa geográfico de faenas vs casa matriz", "Indicadores de desconfianza pública"],
            "actors": ["Comité Ejecutivo", "CCO en Santiago", "Gerente de Faena Regional", "CISO", "Fiscal Legal"],
            "steps": ["Identificación de sesgos centralistas", "Conexión de telemetría de faenas en tiempo real", "Auditoría de ciberseguridad VPC", "Verificación fáctica anti-greenwashing"],
            "states": ["Sesgo_Centralista_Detectado", "Conexión_Territorial_Establecida", "Seguridad_VPC_Auditada", "Discurso_Blindado"],
            "outputs": ["Protocolo de descentralización de información", "Certificado de cumplimiento de ciberseguridad VPC"],
            "exceptions": ["Veto unilateral del CISO por riesgo de fuga de datos en modelos públicos"]
        },
        "entities": [
            {"entity_id": "ENT_CENTRALISMO_SANTIAGO", "type": "factor_estructural", "name": "Centralismo Institucional en Santiago", "aliases": ["Brecha Casa Matriz vs Faena Regional"]},
            {"entity_id": "ENT_DESCONFIANZA_ESTRUCTURAL", "type": "factor_cultural", "name": "Desconfianza Institucional Estructural en Chile", "aliases": ["Escepticismo Ciudadano"]}
        ],
        "relations": [
            {"subject_id": "ENT_CENTRALISMO_SANTIAGO", "predicate": "incrementa_asimetria_de", "object_id": "ENT_PERFIL_CCO_LATAM", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F39-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "Conectar digitalmente a los gerentes de faena en regiones con la casa matriz en Santiago para eliminar el sesgo centralista.", "status": "evidencia"},
            {"module": "Gobernanza", "implication": "Cumplir con las exigencias del CISO mediante VPC y encriptación local para neutralizar el veto de seguridad en compras B2B.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F40", "P01-F41"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f37_f39.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
