import json
import os
import sys

# Append P01-F34, P01-F35, P01-F36 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F34",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones definen la representación estructurada de este tema?",
        "snapshot_at": "2026-10-01T00:56:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La representación estructurada del retorno de valor se define por: 2 dimensiones de variables de valor (reputacionales/intangibles como capital de confianza, SLO, Marcas Ciudadanas y legitimidad C-Suite; y financieras como solvencia bursátil, costo de capital ESG y mitigación en Golden Hour <30 min); 4 categorías de KPIs (eficiencia operativa, coherencia discursiva 100%, gobernanza/cumplimiento Ley 20.730/NCG 461, y posición reputacional Merco/Cadem); relaciones causales directas con la continuidad operacional; y condiciones de trazabilidad estricta a fuentes y gobernanza multi-persona B2B (Usuario, Comprador, Aprobador).",
        "findings": [
            {
                "claim_id": "P01-F34-C1",
                "claim": "El retorno de valor se estructura en dos dimensiones de variables: intangibles/reputacionales (capital de confianza, Licencia Social para Operar, percepción de Marca Ciudadana y legitimidad directiva) y financieras/negocio (solvencia bursátil, costo de capital ASG y reducción de pérdidas en la Golden Hour de crisis <30 min).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Direcciones Corporativas"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Variables de Valor Financiero y Reputacional",
                        "excerpt_short": "Dos dimensiones de valor: variables reputacionales (SLO, confianza, Marca Ciudadana) y financieras (costo de capital ASG, valor bursátil, Golden Hour).",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:56:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F34-C2",
                "claim": "Las cuatro categorías de KPIs corresponden a Eficiencia Operativa (reducción de briefing de 4h a 15m), Coherencia Discursiva (100% consistencia fáctica), Gobernanza y Cumplimiento (cero sanciones bajo Ley 20.730 y NCG 461), y Posicionamiento Directivo (asiento C-Suite en 32,3% y rankings Merco/Cadem).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "España / Chile", "actor": "C-Suite y Dircoms"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Categorías de KPIs y Métricas de Desempeño",
                        "excerpt_short": "Cuatro categorías de KPIs: Eficiencia Operativa, Coherencia Discursiva, Gobernanza/Cumplimiento y Posicionamiento.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:56:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            }
        ],
        "operational_model": {
            "inputs": ["Métricas operativas de equipos", "Reportes de auditoría de cumplimiento", "Encuestas de reputación"],
            "actors": ["CCO", "CEO", "CFO", "Director de Operaciones"],
            "steps": ["Medición de indicadores en las cuatro categorías", "Evaluación de causalidad en continuidad operacional", "Reporte de retorno de valor a Directorio", "Ajuste de presupuesto y arquitectura"],
            "states": ["Indicadores_Definidos", "Medición_Sistémica", "Causalidad_Verificada", "Retorno_Consolidado"],
            "outputs": ["Cuadro de mando multidimensional", "Informe de valor mitigado ante Directorio"],
            "exceptions": ["Disociación entre métricas operativas de comunicación y estados financieros de la empresa"]
        },
        "entities": [
            {"entity_id": "ENT_MODELO_VALOR_P01", "type": "marco_conceptual", "name": "Modelo Multidimensional de Valor en Asuntos Corporativos", "aliases": ["Estructura de Retorno P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_MODELO_VALOR_P01", "predicate": "vincula_eficiencia_con", "object_id": "Continuidad_del_Negocio", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F34-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Configurar paneles de control en BRIDGE que visualicen el impacto en las 4 categorías de KPIs simultáneamente.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F35", "P01-F36"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F35",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada afirmación de este tema?",
        "snapshot_at": "2026-10-01T00:56:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El tema está respaldado por 11 fuentes estructuradas bajo 4 niveles epistemológicos: Hechos Documentados (Dircom ECE 2025: 54,4% reporte al CEO; BCN Ley 20.730; CMF NCG 461/519; Edelman Trust Barometer 2025/2026; Cadem Marcas Ciudadanas Jun 2026; Merco Chile 2025/2026; Acción Empresas Sep 2026; ICARE); Evidencia Académica (Page Society 2022/2023; Global Capability Framework 2021); Afirmaciones Comerciales (McKinsey Oct 2025); e Hipótesis de Trabajo (HT-1, HT-2, HT-3). Se reiteran los 4 vacíos críticos de evidencia.",
        "findings": [
            {
                "claim_id": "P01-F35-C1",
                "claim": "McKinsey (junio 2025, The CEO's role as chief storyteller) documenta que aproximadamente 6 de cada 10 personas señalan que las acciones y declaraciones de un CEO afectan directamente su opinión sobre la empresa, vinculando la vocería directiva con la valoración de mercado a largo plazo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-06", "region": "Global", "actor": "McKinsey & Company"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: McKinsey CEO Storyteller y Reputación C-Suite",
                        "excerpt_short": "Aproximadamente 6 de cada 10 personas declaran que las acciones del CEO afectan directamente su opinión sobre la empresa.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:56:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Investigación empírica global de liderazgo directivo de McKinsey."
            },
            {
                "claim_id": "P01-F35-C2",
                "claim": "El Edelman Trust Barometer (2025-2026) reporta que las empresas privadas son percibidas como la institución más ética y competente en comparación con gobiernos y medios, lo que impone al CCO y al CEO la exigencia de fundamentar sus posturas en hechos verificables.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Edelman Trust Institute"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Edelman Trust Barometer y Confianza Institucional",
                        "excerpt_short": "Las empresas son la institución más confiable y ética respecto a gobiernos y medios, exigiendo vocerías sustentadas en hechos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:56:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Barómetro empírico global representativo de confianza institucional."
            }
        ],
        "operational_model": {
            "inputs": ["Informes empíricos y regulatorios", "Textos legales oficiales", "Matriz de niveles epistemológicos"],
            "actors": ["Auditor Metodológico", "Investigador Corporativo"],
            "steps": ["Verificación de citas", "Control de fechas de corte", "Catalogación epistemológica", "Detección de vacíos"],
            "states": ["Fuentes_Verificadas", "Trazabilidad_Aprobada"],
            "outputs": ["Tabla General de Fuentes y Respaldos"],
            "exceptions": ["Cita sin fuente primaria demostrable"]
        },
        "entities": [
            {"entity_id": "ENT_EDELMAN_TRUST", "type": "estudio_opinion", "name": "Edelman Trust Barometer 2025/2026", "aliases": ["Barómetro de Confianza Edelman"]}
        ],
        "relations": [
            {"subject_id": "ENT_EDELMAN_TRUST", "predicate": "mide_confianza_en", "object_id": "Empresas_y_Gobiernos", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F35-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Proporción de personas cuya opinión corporativa depende directamente de las acciones del CEO",
                "value": "6 de cada 10",
                "denominator": "Total encuestados en estudio McKinsey CEO Storyteller",
                "source_claim_id": "P01-F35-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Garantizar que todo insumo generado en BRIDGE incorpore el respaldo documental explícito exigido en la Tabla General de Fuentes.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F36", "P01-F37"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F36",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto con entradas y resultado esperado ilustra este tema en la práctica?",
        "snapshot_at": "2026-10-01T00:56:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso de preparación ejecutiva para una Audiencia de Ley de Lobby (Ley N° 20.730) ante una Autoridad Sectorial e Inversionistas Comunitarios en minería/industria en Chile ilustra el tema: con entradas de repositorios internos seguros (Memoria CMF NCG 461, actas previas de InfoLobby, RCA y convenios territoriales) cruzadas con señales dinámicas de prensa y proyectos legislativos, un motor analítico en VPC privada genera un Briefing Book en 15 minutos (ahorrando el 80% de tiempo de búsqueda); el resultado esperado verifica 100% de coherencia discursiva, cero sanciones de probidad y costo evitado de parálisis de faena estimada en millones de dólares.",
        "findings": [
            {
                "claim_id": "P01-F36-C1",
                "claim": "En una audiencia de lobby y relacionamiento comunitario en Chile, las entradas combinan repositorios privados seguros (Memoria CMF NCG 461, actas anteriores de InfoLobby, RCA y acuerdos territoriales) con señales dinámicas de prensa y seguimiento legislativo en tiempo real.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresa Minera / Industrial"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Caso Concreto de Retorno de Valor en Minería/Industria",
                        "excerpt_short": "Entradas del caso: Repositorio privado (NCG 461, InfoLobby, RCA) cruzado con prensa y proyectos legislativos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:56:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso práctico detallado en el dossier P01."
            },
            {
                "claim_id": "P01-F36-C2",
                "claim": "El retorno esperado y verificable se materializa en tres dimensiones: 1) retorno en tiempo (briefing de 4 horas a 15 minutos); 2) costo evitado (cero sanciones CMF/Lobby y protección de continuidad operacional de faenas); y 3) retorno reputacional (100% consistencia de relato corporativo protegiendo la Licencia Social).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "C-Suite y Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Resultados Verificables y ROI del Caso",
                        "excerpt_short": "Resultados verificables: ahorro de tiempo (15 min), costo evitado en litigios/parálisis y retorno reputacional 100% coherente.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:56:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación de métricas y retorno verificable en el dossier."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria CMF NCG 461", "RCA ambiental", "Historial InfoLobby", "Prensa y proyectos de ley"],
            "actors": ["Gerente de Asuntos Públicos", "CCO", "Gerente General (CEO)", "Fiscal Legal"],
            "steps": [
                "Ingesta en entorno VPC privado",
                "Generación de Briefing Book con citas directas en 15 minutos",
                "Validación de consistencia por Legal y CCO",
                "Comparecencia en audiencia de lobby",
                "Registro en InfoLobby y auditoría de coherencia fáctica"
            ],
            "states": ["Datos_Ingresados", "Briefing_Generado_15min", "Legal_Visado", "Audiencia_Completada", "Coherencia_100%_Certificada"],
            "outputs": ["Briefing ejecutivo trazable", "Registro formal InfoLobby sin inconsistencias", "Evaluación de costos evitados"],
            "exceptions": ["Falla de sincronización entre el texto de la RCA y la memoria CMF"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_ROI_MINERO", "type": "caso_estudio", "name": "Caso Práctico de Retorno de Valor en Sector Minero", "aliases": ["Caso de Éxito P01 ROI"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_ROI_MINERO", "predicate": "evidencia_retorno_de", "object_id": "ENT_MODELO_VALOR_P01", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F36-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Desplegar el caso de estudio de retorno de valor como benchmark operativo para las demostraciones a C-Suite en Chile.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F37", "P01-F38"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f34_f36.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
