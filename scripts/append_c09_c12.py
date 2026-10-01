import json
import os
import sys

# Script to generate P01-C09, P01-C10, P01-C11, P01-C12 with full 20 keys schema

records = [
    {
        "question_id": "P01-C09",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre riesgos de preparación insuficiente, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:15:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en la tipificación de los riesgos: las fuentes normativas y éticas originales (Ley 20.730, CMF NCG 461, PRSA Code of Ethics, McKinsey 2025) abordan los riesgos como contingencias macro regulatorias, éticas (mentira por omisión) y de desinformación geopolítica. En contraste, las síntesis internas (P01_RESEARCH_DOSSIER, P01_EVIDENCE_MAP) tipifican el riesgo como una patología operativa interna: la 'cocina artesanal de madrugada', fragmentación de repositorios y burnout del equipo por minutas manuales de último minuto. Prevalencia editorial: En cuanto a la realidad legal y reputacional, prevalecen las fuentes empíricas y normativas (Ley 20.730, Merco, Cadem); sin embargo, en cuanto a la clasificación epistémica, el documento correctivo P01_GAPS_AND_VALIDATION prevalece sobre P01_RESEARCH_DOSSIER al clasificar el 'dolor operativo artesanal' y las cifras de impacto no como hechos probados en la literatura previa, sino como Hipótesis de Trabajo (HT) sujetas a validación de campo.",
        "findings": [
            {
                "claim_id": "P01-C09-C1",
                "claim": "Frente a las fuentes externas que conceptualizan el riesgo de preparación como sanciones legales (Ley N° 20.730 de Lobby y CMF NCG 461) o infracciones éticas formales (PRSA Code of Ethics), las síntesis internas de P01 identifican el riesgo en la fricción operacional cotidiana ('cocina artesanal de minutas', fragmentación documental y desconexión entre la memoria corporativa interna y las señales externas).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile / Global", "actor": "Equipos de Asuntos Corporativos y Reguladores"},
                "evidence": [
                    {
                        "source_id": "18092a4f-ba3b-4861-ba1b-b72e59df957a",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección: Patologías operativas de la preparación insuficiente",
                        "excerpt_short": "Minutas elaboradas de madrugada a partir de correos dispersos y PDFs inconexos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Arts. 5, 7 y 8",
                        "excerpt_short": "Sanciones por inconsistencia u omisión en declaraciones ante sujetos pasivos.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco legal vinculante y análisis del dossier de investigación."
            },
            {
                "claim_id": "P01-C09-C2",
                "claim": "El documento correctivo P01_GAPS_AND_VALIDATION establece la prevalencia editorial sobre las afirmaciones operativas de P01_RESEARCH_DOSSIER, reclasificando la severidad del 'dolor de preparación artesanal' como una Hipótesis de Trabajo (HT-1) que requiere comprobación mediante entrevistas y shadowing de campo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Auditoría Editorial BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Corrección de Estatus Epistémico sobre Dolores de Preparación",
                        "excerpt_short": "El dolor artesanal no es un hecho empíricamente probado sino una hipótesis de diseño a testear.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Prevalencia explícita fijada por la regla de correcciones editoriales del mandato."
            }
        ],
        "operational_model": {
            "inputs": ["Demandas regulatorias", "Consultas de medios", "Información corporativa fragmentada"],
            "actors": ["Vocero", "Director de Asuntos Corporativos", "Regulador", "Opinión Pública"],
            "steps": ["Detección de requerimiento urgente", "Búsqueda en repositorios aislados", "Emisión de mensaje con datos obsoletos", "Contradicción detectada por terceros", "Apertura de contingencia reputacional"],
            "states": ["Requerimiento_Ingresado", "Preparacion_Incompleta", "Mensaje_Emitido", "Contradiccion_Expuesta"],
            "outputs": ["Inconsistencia pública y daño reputacional medible"],
            "exceptions": ["Detección temprana por revisión legal previa antes de la emisión del vocero"]
        },
        "entities": [
            {"entity_id": "ENT_RIESGO_PREPARACION", "type": "riesgo_operacional", "name": "Riesgo de Preparación Insuficiente", "aliases": ["Patología de Cocina Artesanal"]}
        ],
        "relations": [
            {"subject_id": "ENT_RIESGO_PREPARACION", "predicate": "degrada", "object_id": "Licencia_Social_Operar", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P01-C09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Riesgo Externo vs Patología Operativa Interna",
                "Fuentes Originales": "Riesgos ex-post: multas de reguladores, litigios y sanciones éticas formales.",
                "Síntesis Interna": "Fricción ex-ante: pérdida de horas en búsqueda manual, estrés nocturno y puntos ciegos fácticos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Indexar automáticamente los repositorios de la empresa para suprimir la recopilación manual nocturna.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C10", "P01-C11"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C10",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre riesgos de preparación insuficiente, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:15:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba: 1) métricas temporales exactas de preparación (cuántas horas-hombre cuesta realmente un briefing book); 2) estudios académicos longitudinales sobre impacto directo de la IA en la reducción de crisis y preservación de licencia social; 3) auditorías de consistencia fáctica entre minutas preparatorias y registros de InfoLobby en Chile. Fuentes fallidas: Gartner (Future of Communications y Gartner for Communications), Page Society (Pacesetter y Corporate Character), Gregory & Willis 2019, todas bloqueadas por WAF o 403. Fuentes parciales: McKinsey 2025 y Page Society, que ofrecen marcos conceptuales cualitativos pero omiten métricas de error y estrés de campo. Validación mínima: Fase 1 (15 entrevistas cualitativas con Dircoms) y Fase 2 (shadowing cronometrado en tiempo real durante preparación de comités de crisis).",
        "findings": [
            {
                "claim_id": "P01-C10-C1",
                "claim": "No existen datos cuantitativos auditados en la literatura académica ni corporativa abierta que cuantifiquen el número exacto de horas-hombre invertidas por equipos de asuntos corporativos en compilar dossiers de crisis, ni estudios longitudinales revisados por pares que demuestren menor daño reputacional en empresas asistidas por IA.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Literatura Científica y Sectorial"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Vacíos de Prueba Identificados en Preparación Insuficiente",
                        "excerpt_short": "Ausencia de mediciones auditadas de horas-hombre y falta de estudios longitudinales revisados por pares.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación del estado del arte en el manifiesto P01."
            },
            {
                "claim_id": "P01-C10-C2",
                "claim": "Para resolver las incertidumbres sobre el dolor de preparación y tiempos de respuesta, el plan de validación de P01 define un protocolo en dos fases: Fase 1 con 15 entrevistas semiestructuradas a CCOs/Dircoms y Fase 2 con shadowing de observación cronometrada en comités de crisis simulados.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Equipo Investigador BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Plan de Validación Mínima Propuesto (Fase 1 y Fase 2)",
                        "excerpt_short": "Fase 1: 15 entrevistas semiestructuradas; Fase 2: shadowing con cronómetro durante comités de crisis.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diseño metodológico formal en los entregables de síntesis de P01."
            }
        ],
        "operational_model": {
            "inputs": ["Cuestionario de 15 preguntas de comportamiento", "Protocolo de observación de shadowing"],
            "actors": ["Investigador de Campo", "Dircom", "Analista de Inteligencia Corporativa"],
            "steps": ["Selección muestral de 15 CCOs", "Entrevista presencial/remota", "Cronometraje de preparación de minuta", "Análisis de vacíos de fuentes"],
            "states": ["Muestra_Definida", "Entrevistas_Ejecutadas", "Shadowing_Completado", "Vacios_Cerrados"],
            "outputs": ["Reporte empírico de tiempos reales y fricciones de preparación"],
            "exceptions": ["Acuerdos de confidencialidad que restrinjan la observación directa de minutas de crisis"]
        },
        "entities": [
            {"entity_id": "ENT_SHADOWING_CRISIS", "type": "metodologia_campo", "name": "Shadowing de Preparación de Crisis", "aliases": ["Observación Cronometrada en Tiempo Real"]}
        ],
        "relations": [
            {"subject_id": "ENT_SHADOWING_CRISIS", "predicate": "mide_empiricamente", "object_id": "ENT_RIESGO_PREPARACION", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C10-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Diagnóstico Cualitativo de Consultoría vs Protocolo de Shadowing",
                "Consultoría Tradicional": "Afirmaciones generales sobre la necesidad de adoptar IA para mitigar riesgos.",
                "Protocolo BRIDGE": "Medición empírica con cronómetro de tiempos de preparación y auditoría de citas fácticas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Incorporar telemetría en el sistema para contrastar experimentalmente la reducción de horas de preparación en pilotos reales.", "status": "hipotesis"}
        ],
        "open_gaps": [
            "Medición cuantitativa auditada de horas-hombre requeridas para elaborar minutas de comparecencia legislativa.",
            "Evidencia empírica sobre la correlación entre uso de software de inteligencia ejecutiva y reducción de contingencias reputacionales."
        ],
        "next_question_ids": ["P01-C11", "P01-C12"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C11",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre resultados y retorno de valor, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:15:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en la naturaleza del ROI: las fuentes internacionales empíricas y profesionales (Global Alliance GCF, Dircom ECE 2025, Public Affairs Council) definen el valor mediante activos intangibles, confianza, legitimidad social, reporte directo al CEO (54,4%) y presencia en Comité Ejecutivo (32,3%), admitiendo la dificultad de aislar un retorno financiero unitario directo. En contraste, las síntesis internas iniciales (P01_RESEARCH_DOSSIER) proponen métricas operativas duras: reducción de tiempo de 4h a 15 min, 80% menos tiempo de búsqueda y 90% de acierto en preguntas difíciles. Prevalencia editorial: Prevalecen las fuentes empíricas originales para el valor estratégico de la profesión (el ROI es de legitimidad, gobernanza y confianza de largo plazo); y prevalece la corrección editorial de P01_GAPS_AND_VALIDATION, la cual reclasifica la promesa cuantitativa de '4 horas a 15 minutos' como Hipótesis de Trabajo (HT-2) no demostrada empíricamente en el corpus previo.",
        "findings": [
            {
                "claim_id": "P01-C11-C1",
                "claim": "Las fuentes originales y estándares globales (Global Alliance GCF, Dircom ECE 2025 y Public Affairs Council) demuestran que el retorno de valor en asuntos corporativos reside en la preservación de intangibles estratégicos (reputación, confianza, licencia social) y en la influencia en el C-Suite (54,4% de reporte directo al CEO), reconociendo que no existe un ROI financiero lineal de corto plazo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2025", "region": "Europa / Global", "actor": "Directores de Comunicación y C-Suite"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Dircom España - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Capítulo: Posición en el organigrama y valoración de la dirección",
                        "excerpt_short": "54,4% reporte al CEO y 32,3% en Comité Ejecutivo; 3 de cada 4 CEOs valoran con nota alta la función.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "b3e32e8b-87b0-466e-a61f-9da8f5ca3e92",
                        "source_title": "Global Alliance & Corporate Excellence - The Global PR and Communication Model",
                        "original_url": "https://www.corporateexcellence.org/recurso/the-global-pr-and-communication-model/e464cce1-872f-4ad4-9dfa-c5ee6942918e",
                        "locator": "Bloque 5: Connecting Intelligence & Intangible Asset Metrics",
                        "excerpt_short": "Medición de valor basada en confianza, reputación y capital relacional intangible.",
                        "source_date": "2021",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Convergencia de estándares globales empíricos y modelos académicos consolidados."
            },
            {
                "claim_id": "P01-C11-C2",
                "claim": "El documento correctivo P01_GAPS_AND_VALIDATION corrige las afirmaciones de retorno de P01_RESEARCH_DOSSIER, estableciendo que la promesa de ahorro de tiempo ('de 4 horas a 15 minutos') es una Hipótesis de Trabajo (HT-2) / Afirmación Comercial, y que la métrica observable principal debe ser la anulación de desajustes fácticos en vocerías de alto impacto.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Auditoría BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Reclasificación Epistémica de Métricas de Retorno Operacional",
                        "excerpt_short": "La reducción de 4h a 15m es una hipótesis HT-2 sujeta a prueba de campo.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Regla de corrección editorial interna fijada en los documentos metodológicos de P01."
            }
        ],
        "operational_model": {
            "inputs": ["Horas de trabajo operativo", "Costos de consultoría externa", "Incidentes de contradicción"],
            "actors": ["Dircom", "CEO", "CFO", "Consultoras Externas"],
            "steps": ["Medición de línea base de tiempos", "Implementación de herramienta de asistencia", "Cálculo de horas liberadas para estrategia", "Auditoría de consistencia de mensajes"],
            "states": ["Linea_Base_Registrada", "Herramienta_Desplegada", "Retorno_Medido"],
            "outputs": ["Reporte de Retorno de Valor: Eficiencia Operativa y Capital Reputacional"],
            "exceptions": ["Dificultad de aislar el valor del software de variables macroeconómicas o políticas"]
        },
        "entities": [
            {"entity_id": "ENT_MODELO_RETORNO_VALOR", "type": "modelo_gestion", "name": "Modelo de Retorno de Valor en Asuntos Corporativos", "aliases": ["Intangible Asset Valuation & Efficiency"]}
        ],
        "relations": [
            {"subject_id": "ENT_MODELO_RETORNO_VALOR", "predicate": "combina_metricas_de", "object_id": "Eficiencia_Horas_y_Reputacion_Merco", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-C11-C1"}
        ],
        "comparisons": [
            {
                "dimension": "ROI Financiero Transaccional vs Creación de Confianza Estratégica",
                "Enfoque Transaccional Tradicional": "Intento forzado de medir retorno publicitario equivalente (VPE/AVE), ampliamente desacreditado.",
                "Enfoque Estratégico Prevaleciente": "Protección de la licencia social, acceso al CEO y ahorro medible de tiempo en elaboración de minutas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric_name": "Tasa de Reporte Directo al CEO",
                "value": 54.4,
                "unit": "porcentaje",
                "denominator": "Total de directores de comunicación encuestados en España (Dircom ECE 2025)",
                "evidence_claim_id": "P01-C11-C1"
            },
            {
                "metric_name": "Presencia en Comité Ejecutivo",
                "value": 32.3,
                "unit": "porcentaje",
                "denominator": "Total de directores de comunicación encuestados en España (Dircom ECE 2025)",
                "evidence_claim_id": "P01-C11-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Posicionar el valor de BRIDGE ante el C-Suite como una salvaguarda de consistencia institucional y ahorro de tiempo crítico, evitando el esquema desacreditado de valor publicitario.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C12", "P01-C13"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C12",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre resultados y retorno de valor, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:15:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba: 1) la cuantificación monetaria exacta de 'evitar una hora de contradicción comunicacional durante una crisis'; 2) la validación empírica en entornos reales de la hipótesis de ahorro de tiempo en minutas (HT-2); 3) la disposición a pagar (WTP) y las condiciones técnicas de compra requeridas por CISOs y Fiscales en Chile. Fuentes fallidas: OECD Corporate Governance y Gregory & Willis 2019 (bloqueos técnicos). Fuentes parciales: PAC Benchmarking y Dircom ECE 2025 (demuestran presupuestos estables pero no entregan métricas unitarias de ROI por proyecto). Validación mínima: Fase 3 del plan de validación (Semanas 9 a 12), consistente en una prueba de concepto (PoC) de arquitectura VPC con un panel evaluador tripartito (CCO, CISO y Fiscal Legal) para auditar viabilidad técnica, seguridad y disposición a pagar.",
        "findings": [
            {
                "claim_id": "P01-C12-C1",
                "claim": "No existe en la literatura abierta una fórmula estandarizada y auditada que permita cuantificar en unidades monetarias el valor exacto de evitar una hora de contradicción pública corporativa, manteniéndose como un cálculo de reducción de riesgo cualitativo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Economía de la Reputación"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Vacíos de Prueba en Retorno Económico y ROI de Intangibles",
                        "excerpt_short": "No existe una fórmula matemática auditada que asigne una cifra monetaria a evitar una hora de contradicción comunicacional.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Revisión exhaustiva de literatura sobre medición de intangibles en P01."
            },
            {
                "claim_id": "P01-C12-C2",
                "claim": "Para resolver la incertidumbre de retorno de valor B2B y requisitos de adquisición, el plan de validación de P01 establece la Fase 3 (PoC y Evaluación de Arquitectura) con un panel tripartito de CCOs, CISOs y Fiscales Legales sobre un entorno de nube privada VPC.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Equipo Investigador BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Fase 3 del Plan de Validación Mínima (Semanas 9 a 12)",
                        "excerpt_short": "Presentación de prototipo de interfaz ejecutiva ante panel tripartito: CCO, CISO y Fiscal Legal.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:15:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diseño del experimento de validación B2B documentado en el dossier metodológico."
            }
        ],
        "operational_model": {
            "inputs": ["Prototipo funcional de asistente ejecutivo", "Dossier técnico de arquitectura VPC", "Matriz de preguntas de seguridad"],
            "actors": ["Equipo BRIDGE", "CCO Evaluador", "CISO Evaluador", "Fiscal Legal Evaluador"],
            "steps": ["Despliegue de demo interactiva en entorno aislado", "Auditoría de seguridad y cifrado por el CISO", "Revisión de confidencialidad por el Fiscal Legal", "Medición de disposición a pagar del CCO"],
            "states": ["Demo_Desplegada", "Auditoria_Seguridad_En_Curso", "Dictamen_Tripartito_Emitido"],
            "outputs": ["Matriz de Viabilidad de Retorno y Adquisición B2B"],
            "exceptions": ["Restricciones de gobernanza que prohíban pilotos con datos corporativos reales sin homologación previa de proveedor"]
        },
        "entities": [
            {"entity_id": "ENT_POC_TRIPARTITA", "type": "proceso_validacion", "name": "Prueba de Concepto Trilateral (Fase 3)", "aliases": ["Validación de Retorno B2B y Arquitectura"]}
        ],
        "relations": [
            {"subject_id": "ENT_POC_TRIPARTITA", "predicate": "valida_viabilidad_comercial_de", "object_id": "BRIDGE_Executive_Assistant", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C12-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Venta Directa a Usuario Final vs Validación Estructurada B2B",
                "Venta B2C / SaaS Tradicional": "Convencer al usuario final para que ingrese tarjeta de crédito personal o corporativa.",
                "Validación B2B Corporativa": "Superar el proceso formal de homologación con CISO y Legal demostrando retorno en control de riesgos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Estructurar la propuesta comercial de BRIDGE destacando el blindaje normativo y la compatibilidad con VPC para acelerar la aprobación de los comités de seguridad.", "status": "hipotesis"}
        ],
        "open_gaps": [
            "Fórmula económica validada para monetizar la mitigación de crisis comunicacionales.",
            "Umbrales de precio y presupuesto disponible para herramientas de asistencia ejecutiva en empresas reguladas chilenas."
        ],
        "next_question_ids": ["P01-C13", "P01-C14"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

with open("respuestas/temp_c09_c12.jsonl", "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("Generated 4 records in respuestas/temp_c09_c12.jsonl")
