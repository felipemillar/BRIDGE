import json
import os
import sys

# Append P01-F43, P01-F44, P01-F45 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F43",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cómo se estructuraría un plan de descubrimiento de clientes (customer discovery) para validar o refutar empíricamente las hipótesis de este ámbito?",
        "snapshot_at": "2026-10-01T01:04:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El plan de customer discovery se estructura en 4 fases secuenciales: Fase 1 (Semanas 1-4) Entrevistas en profundidad con 12-15 CCOs/Asuntos Públicos de empresas IPSA para mapear atrapamiento táctico y JTBD; Fase 2 (Semanas 5-8) Auditoría de artefactos, tiempos y shadowing operativo para medir la línea base real de horas-hombre y cerrar el Knowledge Gap 1; Fase 3 (Semanas 9-12) Pruebas de Concepto (PoC) en VPC privada cruzando repositorios internos confidenciales (NCG 461/RCA) con señales externas para validar la reducción a 15 min (HT-2); y Fase 4 (Semanas 11-12+) Validación técnica con aprobadores B2B (CISO y Fiscal Legal) para evaluar pruebas de penetración y políticas de no-fuga (HT-3).",
        "findings": [
            {
                "claim_id": "P01-F43-C1",
                "claim": "El plan de validación en cuatro fases permite cerrar empíricamente los vacíos críticos del corpus (Knowledge Gaps 1 a 4) mediante entrevistas a 12-15 directores corporativos, cronometraje en tiempo real (shadowing) de preparación de briefings y pruebas piloto de software en nube privada (VPC).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Diseño Experimental B2B"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2: Plan de Validación Empírica en 4 Fases",
                        "excerpt_short": "Fase 1 Entrevistas cualitativas, Fase 2 Auditoría y shadowing de tiempos, Fase 3 PoCs en VPC y Fase 4 Aprobación CISO/Legal.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:04:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo metodológico formal de validación del corpus."
            },
            {
                "claim_id": "P01-F43-C2",
                "claim": "La Fase 4 del plan de descubrimiento atiende específicamente la opacidad en criterios de ciberseguridad, sometiendo la arquitectura a la auditoría técnica de CISOs y Fiscales de Compliance para asegurar cumplimiento de ISO 27001, SOC2 y prohibición de re-entrenamiento en LLMs.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "CISOs y Fiscales Legales"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Fase 4: Validación con Aprobadores CISO y Legal",
                        "excerpt_short": "Mesas de evaluación con CISOs y Fiscales de Compliance para auditar VPC, penetración y aislamiento de datos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:04:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de validación técnica del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Protocolo de entrevistas", "Guion de shadowing", "Entorno VPC piloto"],
            "actors": ["Investigador Principal", "CCO Entrevistado", "CISO Corporativo", "Fiscal Legal"],
            "steps": ["Ejecución de entrevistas en profundidad", "Shadowing de preparación directiva", "Despliegue de PoC en VPC", "Auditoría de ciberseguridad y compliance"],
            "states": ["Fase1_Entrevistas", "Fase2_Shadowing", "Fase3_PoC_VPC", "Fase4_Validación_CISO"],
            "outputs": ["Informe de línea base de tiempos", "Matriz de objeciones CISO resuelta", "Validación empírica de HT-2 y HT-3"],
            "exceptions": ["Negativa de CISO a permitir ingesta de documentos sin certificación SOC2 previa"]
        },
        "entities": [
            {"entity_id": "ENT_PLAN_CUSTOMER_DISCOVERY", "type": "plan_validacion", "name": "Plan de Validación Empírica en 4 Fases", "aliases": ["Customer Discovery P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_PLAN_CUSTOMER_DISCOVERY", "predicate": "resuelve", "object_id": "ENT_GAP_HORAS_HOMBRE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F43-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Validación", "implication": "Ejecutar el plan de 4 fases con empresas piloto en Chile para calibrar los algoritmos de BRIDGE sobre datos reales.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F44", "P01-F45"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F44",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué preguntas abiertas, pruebas de concepto o experimentos permitirían verificar la necesidad real, la disposición a pagar y las barreras de adopción?",
        "snapshot_at": "2026-10-01T01:04:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El protocolo comprende: 1) Preguntas abiertas segmentadas por perfil (CCO: horas invertidas y riesgo de contradicción con NCG 461; Asuntos Públicos: cruce de actas previas bajo Ley 20.730; CISO: arquitectura VPC y certificaciones no negociables; Fiscal Legal: trazabilidad estricta y responsabilidad por imprecisiones); 2) Experimento A/B controlado de medición de tiempos comparando elaboración tradicional manual vs asistida trazable (midiendo minutos totales, tasa de citación y coherencia 0% error); y 3) Métricas de Willingness-to-Pay (WTP) basadas en costo evitado de horas de alta gerencia, sensibilidad de Van Westendorp y diferencial de precio por despliegue privado VPC (Gabor-Granger).",
        "findings": [
            {
                "claim_id": "P01-F44-C1",
                "claim": "El diseño de experimentos A/B permite comparar de forma controlada el grupo manual (búsqueda dispersa en SharePoint y correos) frente al asistido en VPC, midiendo tres indicadores objetivos: tiempo total hasta la entrega, porcentaje de afirmaciones con cita verificable y tasa de errores fácticos auditada por un comité legal.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Diseño Experimental"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 3: Experimentos A/B de Medición de Tiempos y Trazabilidad",
                        "excerpt_short": "Diseño experimental A/B: grupo control manual vs grupo asistido en VPC, midiendo tiempos, citación y tasa de error.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:04:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diseño experimental formal del corpus."
            },
            {
                "claim_id": "P01-F44-C2",
                "claim": "La disposición a pagar (WTP) se evalúa mediante tres metodologías: costo evitado de horas-hombre de alta gerencia y reducción de la Golden Hour a <30 min; modelo de sensibilidad de precios de Van Westendorp; y diferencial de precio de Gabor-Granger (30%-50% premium por VPC dedicada con certificación de CISO).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / B2B", "actor": "Compradores Corporativos"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 3: Métricas de Disposición a Pagar (WTP-1 a WTP-3)",
                        "excerpt_short": "Métricas WTP: costo evitado en Golden Hour, Van Westendorp y premium de 30-50% por VPC privada segura.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:04:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Métricas formales de monetización del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Guion de preguntas cualitativas", "Escenario de simulación de crisis A/B", "Encuesta de precios Van Westendorp"],
            "actors": ["Evaluador de Producto", "Equipo Analista (Grupo Control)", "Equipo Analista (Grupo Test)", "CISO Evaluador"],
            "steps": ["Aplicación de entrevistas por rol", "Ejecución de prueba A/B cronometrada", "Auditoría legal ciega de minutas", "Medición de elasticidad de precio WTP"],
            "states": ["Preguntas_Realizadas", "Experimento_Ejecutado", "Datos_Tabulados", "WTP_Calculada"],
            "outputs": ["Reporte estadístico de prueba A/B", "Curva de sensibilidad de precios", "Matriz de objeciones resueltas"],
            "exceptions": ["Sesgo de participantes por conocimiento previo del escenario de crisis"]
        },
        "entities": [
            {"entity_id": "ENT_EXPERIMENTO_AB_TIEMPOS", "type": "diseño_experimental", "name": "Experimento A/B de Medición de Tiempos y Trazabilidad", "aliases": ["Prueba A/B Briefings"]},
            {"entity_id": "ENT_MODELO_WTP", "type": "modelo_precios", "name": "Modelo de Disposición a Pagar B2B (WTP)", "aliases": ["WTP Van Westendorp y Gabor-Granger"]}
        ],
        "relations": [
            {"subject_id": "ENT_EXPERIMENTO_AB_TIEMPOS", "predicate": "cuantifica_eficiencia_de", "object_id": "HT-2", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F44-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Premium de precio aceptable por despliegue en nube privada dedicada (VPC)",
                "value": "30% a 50%",
                "denominator": "Sobre la tarifa de licencia SaaS multi-tenant base",
                "source_claim_id": "P01-F44-C2"
            }
        ],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Tarificar el módulo VPC dedicado con un diferencial premium del 30-50% respaldado por la certificación técnica del CISO.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F45", "P01-F46"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F45",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué segmentos de usuarios deberían abordarse primero y con qué criterios de selección?",
        "snapshot_at": "2026-10-01T01:04:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La secuencia priorizada comprende: 1) Segmento 1 Early Adopters (Empresas con Faenas Territoriales Críticas y Emisores IPSA en minería, energía, celulosa y servicios básicos); 2) Segmento 2 (Empresas Altamente Reguladas, Financieras y Retail masivo con alto volumen de lobby bajo Ley 20.730 y exposición en Merco/Cadem); y 3) Segmento 3 (Consultoras y Agencias de Asuntos Públicos como canal multiplicador). Los criterios de selección son: severidad del riesgo de Licencia Social (SLO), carga de transparencia activa obligatoria, exigencia CMF NCG 461 y presencia de CISO con presupuesto para VPC privada.",
        "findings": [
            {
                "claim_id": "P01-F45-C1",
                "claim": "El Segmento 1 (Early Adopters) está compuesto por grandes corporaciones con faenas territoriales críticas y emisores IPSA (ej. Codelco, Antofagasta Minerals, BHP, Copec, Enel, CMPC, Colbún), debido a que una contradicción o incumplimiento territorial puede paralizar la faena industrial generando pérdidas millonarias inmediatas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresas Minero-Energéticas e IPSA"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 4: Segmentación Priorizada de Mercado y Criterios de Entrada",
                        "excerpt_short": "Segmento 1 prioritario: empresas con faenas territoriales críticas y emisores IPSA (minería, energía, celulosa).",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:04:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estrategia de go-to-market fundamentada en el corpus."
            },
            {
                "claim_id": "P01-F45-C2",
                "claim": "Los cuatro criterios fundamentados de selección de cuentas iniciales son: 1) Severidad del riesgo de pérdida de Licencia Social para Operar; 2) Carga de transparencia activa mandatoria bajo Ley 20.730; 3) Obligatoriedad de reporte CMF NCG 461 / NIIF S1-S2; y 4) Madurez de gobernanza con CISO y presupuesto estructurado para entornos VPC dedicados.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Comité de Selección B2B"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 4: Criterios Técnicos y Regulatorios de Selección",
                        "excerpt_short": "Cuatro criterios de selección: riesgo de SLO, carga de Ley 20.730, reporte CMF NCG 461 y capacidad de aprobación CISO.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:04:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Criterios técnicos consolidados en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Ranking IPSA de capitalización", "Registro de faenas con RCA ambiental", "Historial de audiencias en InfoLobby"],
            "actors": ["Líder de Desarrollo de Negocio", "CCO Prospecto", "CISO Prospecto"],
            "steps": ["Filtrado de cuentas por los 4 criterios", "Prospección directa en Segmento 1", "Demostración de PoC en entorno seguro", "Expansión hacia Segmentos 2 y 3"],
            "states": ["Cuentas_Filtradas", "Contacto_Establecido", "PoC_En_Curso", "Cuenta_Validada"],
            "outputs": ["Pipeline priorizado de 20 cuentas corporativas en Chile"],
            "exceptions": ["Selección de una empresa sin activos territoriales que diluya la propuesta de valor de SLO"]
        },
        "entities": [
            {"entity_id": "ENT_SEGMENTO_1_IPSA", "type": "segmento_mercado", "name": "Segmento 1: Faenas Territoriales Críticas y Emisores IPSA", "aliases": ["Early Adopters P01"]},
            {"entity_id": "ENT_CRITERIOS_SELECCION", "type": "criterios_evaluacion", "name": "Cuatro Criterios de Selección de Cuentas B2B", "aliases": ["Filtros de Entrada al Mercado"]}
        ],
        "relations": [
            {"subject_id": "ENT_CRITERIOS_SELECCION", "predicate": "prioriza_ingreso_a", "object_id": "ENT_SEGMENTO_1_IPSA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F45-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Secuencia de Segmentos B2B",
                "Segmento 1": "Faenas territoriales críticas y emisores IPSA (Minería, Energía, Celulosa) | Máxima severidad de riesgo.",
                "Segmento 2": "Empresas reguladas y retail (Banca, Seguros, Salud) | Alto volumen de lobby y sensibilidad Merco.",
                "Segmento 3": "Consultoras y agencias de asuntos públicos | Rol multiplicador y aumento de margen operativo."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Enfocar el go-to-market inicial de BRIDGE en las 20 principales corporaciones del Segmento 1 minero/energético de Chile.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F46", "P01-F47"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f43_f45.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
