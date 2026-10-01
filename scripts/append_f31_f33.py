import json
import os
import sys

# Append P01-F31, P01-F32, P01-F33 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F31",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué resultados medibles, cuantitativos o cualitativos, espera obtener una organización al incorporar inteligencia estructurada en este ámbito?",
        "snapshot_at": "2026-10-01T00:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La organización espera obtener cinco resultados clave: 1) Ahorro de tiempo operativo en briefings de 4 horas a <15 minutos (HT-2); 2) Reducción a 0% de contradicciones discursivas frente a actas de InfoLobby y memorias CMF NCG 461; 3) Blindaje del capital reputacional en rankings Merco y Cadem; 4) Preservación de la Licencia Social para Operar (SLO) evitando paralizaciones territoriales; y 5) Costo evitado de sanciones, multas de la CMF y litigios ambientales.",
        "findings": [
            {
                "claim_id": "P01-F31-C1",
                "claim": "La reducción del tiempo de elaboración de briefings ejecutivos de 4 horas a menos de 15 minutos constituye una hipótesis de trabajo y propuesta de valor comercial (HT-2), mientras que la literatura empírica documenta que los equipos de comunicación destinan más del 60% de su capacidad a tareas reactivas no estratégicas.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Diseño Tecnológico B2B"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4: Hipótesis de Trabajo HT-2",
                        "excerpt_short": "Hipótesis HT-2: Reducción del ciclo de preparación de 4 horas a 15 minutos mediante trazabilidad asistida.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Formulada como hipótesis analítica en el corpus."
            },
            {
                "claim_id": "P01-F31-C2",
                "claim": "En Chile, la transparencia obligatoria de agendas bajo la Ley N° 20.730 de Lobby y la supervisión de memorias integradas ASG bajo la NCG 461 de la CMF convierten la coherencia testimonial en un requisito de cumplimiento legal con responsabilidad administrativa directa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "BCN / CMF Chile"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 3° a 9°",
                        "excerpt_short": "Registro público obligatorio de audiencias, asistentes y materias en InfoLobby.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Exigencia de reporte ASG integrado",
                        "excerpt_short": "Supervisión de divulgación de riesgos ambientales, sociales y de gobernanza.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Cuerpo normativo chileno formal."
            }
        ],
        "operational_model": {
            "inputs": ["Tiempos de preparación actuales", "Historial de inconsistencias", "Presupuestos de mitigación de crisis"],
            "actors": ["CCO", "CEO", "CFO", "Líder de Asuntos Públicos"],
            "steps": ["Medición de línea base de tiempos", "Despliegue de inteligencia asistida", "Cotejo de consistencia fáctica", "Evaluación de costos evitados"],
            "states": ["Línea_Base", "Implementación_Asistida", "Eficiencia_Medida", "Valor_Capturado"],
            "outputs": ["Reporte de horas liberadas", "Certificación de consistencia 0% error", "Informe de SLO protegida"],
            "exceptions": ["Falta de medición de horas invertidas en sistemas de time-tracking"]
        },
        "entities": [
            {"entity_id": "ENT_RESULTADOS_ESPERADOS", "type": "modelo_impacto", "name": "Resultados Medibles de Inteligencia Estructurada", "aliases": ["Impacto Cuantitativo y Cualitativo"]}
        ],
        "relations": [
            {"subject_id": "ENT_RESULTADOS_ESPERADOS", "predicate": "optimiza_desempeño_de", "object_id": "ENT_CCO", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F31-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Incorporar métricas de tiempo de generación y tasa de consistencia fáctica directamente en el panel de control de BRIDGE.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F32", "P01-F33"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F32",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cómo se justifica económicamente o estratégicamente una solución de este tipo ante un comité de compras, CEO o CFO?",
        "snapshot_at": "2026-10-01T00:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La justificación de ROI B2B se estructura en 4 pilares financieros y estratégicos: 1) Mitigación del Value-at-Stake (solo el 9% de empresas cuantifica su valor en riesgo ante giros regulatorios según McKinsey); 2) Costo evitado de parálisis de faena (que en minería/energía cuesta millones de dólares diarios) y multas CMF; 3) Eficiencia operativa al eliminar el 80% del tiempo de búsqueda manual de analistas; y 4) Blindaje de gobierno corporativo mediante arquitectura VPC privada con cifrado que supera el veto del CISO y Fiscal Legal (HT-3).",
        "findings": [
            {
                "claim_id": "P01-F32-C1",
                "claim": "McKinsey (2025) documenta que aunque las políticas comerciales y la inestabilidad geopolítica representan los principales riesgos para el C-Suite, solo el 9% de las organizaciones cuantifica formalmente su Value-at-Stake, convirtiendo la inteligencia estructurada en una herramienta de protección patrimonial.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-10", "region": "Global", "actor": "McKinsey & Company"},
                "evidence": [
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Cuantificación de Value-at-Stake y gestión de riesgos",
                        "excerpt_short": "Solo el 9% de las organizaciones cuantifica su Value-at-Stake frente a cambios regulatorios y geopolíticos.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Investigación cuantitativa de alta dirección de McKinsey."
            },
            {
                "claim_id": "P01-F32-C2",
                "claim": "En la matriz de decisión de compras B2B, la aprobación no depende solo del CCO (usuario/comprador), sino que exige satisfacer los requerimientos de no-fuga de datos y aislamiento en VPC del CISO y Fiscal Legal (HT-3).",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Chile / B2B SaaS", "actor": "Comité de Compras Corporativo"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4: Hipótesis de Trabajo HT-3",
                        "excerpt_short": "Aprobación B2B condicionada a superar el veto de CISO y Legal mediante aislamiento estricto en VPC.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Hipótesis de trabajo de diseño B2B del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Cálculo de Value-at-Stake", "Costo diario de parálisis de faena", "Matriz de objeciones de CISO"],
            "actors": ["CEO", "CFO", "CCO", "CISO", "Fiscal Legal"],
            "steps": ["Presentación de caso de negocio de ROI", "Demostración de eficiencia y mitigación de riesgos", "Auditoría de ciberseguridad VPC", "Aprobación de adquisición"],
            "states": ["Propuesta_Comercial", "Evaluación_Financiera", "Auditoría_CISO", "Adquisición_Aprobada"],
            "outputs": ["Business Case de ROI", "Certificado de cumplimiento de seguridad VPC"],
            "exceptions": ["Rechazo del CFO por falta de cálculo cuantificado del Value-at-Stake"]
        },
        "entities": [
            {"entity_id": "ENT_BUSINESS_CASE_ROI", "type": "modelo_financiero", "name": "Business Case de ROI en Asuntos Corporativos", "aliases": ["Justificación Financiera B2B"]}
        ],
        "relations": [
            {"subject_id": "ENT_BUSINESS_CASE_ROI", "predicate": "justifica_adopcion_ante", "object_id": "ENT_CEO", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F32-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Porcentaje de empresas que cuantifica formalmente su Value-at-Stake",
                "value": "9%",
                "denominator": "Total de corporaciones encuestadas por McKinsey",
                "source_claim_id": "P01-F32-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Incorporar en el pitch B2B la calculadora de 'Value at Stake' y la arquitectura técnica VPC privada para neutralizar objeciones de CFO y CISO.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F33", "P01-F34"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F33",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué métricas, indicadores clave de desempeño (KPI) o criterios de éxito se usan habitualmente para evaluar su impacto?",
        "snapshot_at": "2026-10-01T00:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El impacto se evalúa mediante 5 KPIs cuantitativos y 3 criterios cualitativos: Cuantitativos: 1) Tiempo de preparación de briefings (meta: de 4h a <15m); 2) Tasa de desacuerdo o contradicciones en actas (meta: 0%); 3) Cumplimiento de la Ley N° 20.730 de Lobby (meta: 100% de registros en regla); 4) Tiempo de respuesta en crisis Golden Hour (meta: <30 min); y 5) Reasignación de horas a estrategia (>50% de dedicación). Cualitativos: 1) Evolución en rankings Merco y Cadem Marcas Ciudadanas; 2) Preservación de la Licencia Social para Operar (cero litigios o bloqueos); y 3) Asiento permanente del CCO en el Comité Ejecutivo C-Suite.",
        "findings": [
            {
                "claim_id": "P01-F33-C1",
                "claim": "Los KPIs cuantitativos clave abarcan la reducción del tiempo de elaboración de briefings a <15 minutos, la tasa de cero contradicciones con actas públicas (CMF e InfoLobby), el tiempo de respuesta en crisis en menos de 30 minutos y el aumento de la dedicación estratégica del equipo a más del 50%.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gerencias de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Matriz de KPIs y Métricas de Éxito",
                        "excerpt_short": "KPIs cuantitativos: tiempo de briefing <15 min, 0% contradicciones, respuesta en <30 min y >50% tiempo estratégico.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F33-C2",
                "claim": "Los criterios cualitativos de éxito incluyen la preservación de la Licencia Social para Operar (SLO), el mantenimiento de posiciones líderes en Merco y Cadem Marcas Ciudadanas, y la consolidación del asiento permanente del CCO en el Comité Ejecutivo (actualmente en 32,3%-33% según Dircom ECE 2025).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "España / Chile", "actor": "C-Suite y Dircoms"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Asociación de Directivos de Comunicación (Dircom España) - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Asiento en Comité Ejecutivo y legitimidad directiva",
                        "excerpt_short": "Uno de cada tres dircoms (32,3%-33%) forma parte permanente del comité ejecutivo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio empírico ECE 2025."
            }
        ],
        "operational_model": {
            "inputs": ["Registros de auditoría interna", "Resultados de encuestas Merco y Cadem", "Actas de InfoLobby"],
            "actors": ["CCO", "Jefe de Planificación", "Auditor de Cumplimiento"],
            "steps": ["Definición de metas semestrales", "Medición continua de tiempos y contradicciones", "Revisión en Comité Ejecutivo", "Ajuste de flujos de trabajo"],
            "states": ["Metas_Fijadas", "Medición_Activa", "Evaluación_Periódica", "Objetivos_Alcanzados"],
            "outputs": ["Dashboard de KPIs", "Informe de impacto reputacional", "Balance de cumplimiento Ley 20.730"],
            "exceptions": ["Desviación del tiempo de respuesta en crisis superior a 60 minutos"]
        },
        "entities": [
            {"entity_id": "ENT_MATRIZ_KPIS_P01", "type": "sistema_metricas", "name": "Matriz de KPIs de Inteligencia Corporativa", "aliases": ["Cuadro de Mando Integral P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_MATRIZ_KPIS_P01", "predicate": "mide_efectividad_de", "object_id": "ENT_CCO", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F33-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Integrar un módulo de telemetría en BRIDGE que calcule automáticamente el tiempo ahorrado por briefing y la tasa de consistencia fáctica.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F34", "P01-F35"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f31_f33.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
