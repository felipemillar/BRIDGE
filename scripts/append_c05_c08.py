import json
import os
import sys

# Script to generate P01-C05, P01-C06, P01-C07, P01-C08 with full 20 keys schema

records = [
    {
        "question_id": "P01-C05",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre trabajos por hacer y momentos de presión, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:13:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en dos frentes: 1) Las fuentes originales de consultoría (Page Society, McKinsey) retratan al CCO como un consejero estratégico de alto nivel enfocado en narrativa e integración geopolítica, mientras que la síntesis interna (P01_EVIDENCE_MAP, P01_RESEARCH_DOSSIER), respaldada por ECM 2023 y LCM, demuestra la Tensión 1: más del 60% de la jornada está absorbida por tareas tácticas reactivas y redacción artesanal bajo presión de madrugada. 2) Reportes comerciales promueven la confección desatendida de briefings con IA, pero la síntesis interna advierte la Tensión 2: una alucinación fáctica ante un regulador o tribunal destruye irreversiblemente la credibilidad corporativa. Prevalece la síntesis interna: el software debe reducir la carga táctica pero exigir validación humana y trazabilidad documental estricta.",
        "findings": [
            {
                "claim_id": "P01-C05-C1",
                "claim": "Existe una discrepancia estructural entre la aspiración estratégica declarada en reportes de consultoría y el atrapamiento táctico real: estudios empíricos (ECM 2023 y LCM EUPRERA) demuestran que más del 60% del tiempo operativo del equipo de asuntos corporativos se gasta en labores reactivas de bajo valor analítico (redacción manual de comunicados, monitoreo de redes y minutas urgentes).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2025", "region": "Europa / América Latina", "actor": "Equipos de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "80d4fcba-ae0d-4a1d-a36c-2f3b925b4fa2",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Tensión 1: Discurso Estratégico vs. Atrapamiento Táctico",
                        "excerpt_short": "Más del 60% de la jornada se consume en tareas operativas reactivas de bajo valor agregado.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "18092a4f-ba3b-4861-ba1b-b72e59df957a",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección: Taxonomía de JTBD y flujos bajo presión",
                        "excerpt_short": "Fricciones en la preparación artesanal de minutas en horarios nocturnos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Convergencia entre encuestas empíricas internacionales y síntesis crítica de los dossiers de investigación."
            },
            {
                "claim_id": "P01-C05-C2",
                "claim": "Frente a la promoción comercial de automatización total de briefings mediante IA generativa, la síntesis interna corrige que una imprecisión fáctica o alucinación de un modelo de lenguaje reproducida por un vocero ante un fiscalizador destruye la reputación institucional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "C-Suite y Reguladores"},
                "evidence": [
                    {
                        "source_id": "80d4fcba-ae0d-4a1d-a36c-2f3b925b4fa2",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Tensión 2: Promesa de Automatización IA vs. Riesgo de Crisis Alucinatoria",
                        "excerpt_short": "El valor del conocimiento recopilado por IA exige validación humana y respaldo en hechos verificables.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Prevalencia editorial de los documentos de síntesis y corrección de P01."
            }
        ],
        "operational_model": {
            "inputs": ["Demandas urgentes de información", "Monitoreo de prensa y redes", "Peticiones del C-Suite"],
            "actors": ["Vocero", "Equipo de Prensa", "Analista de Asuntos Corporativos"],
            "steps": ["Recepción de requerimiento", "Recopilación manual de antecedentes", "Redacción bajo presión", "Validación jerárquica", "Entrega de minuta"],
            "states": ["Emergencia_Activada", "Recopilacion_Manual", "Minuta_Liberada"],
            "outputs": ["Briefing ejecutivo para reunión o comparecencia"],
            "exceptions": ["Alucinación o inconsistencia detectada en vivo durante la reunión"]
        },
        "entities": [
            {"entity_id": "ENT_JTBD_CRISIS", "type": "trabajo_operativo", "name": "Preparación de Minuta de Crisis", "aliases": ["Briefing Book Urgente"]}
        ],
        "relations": [
            {"subject_id": "ENT_JTBD_CRISIS", "predicate": "consume_tiempo_de", "object_id": "Equipo_Asuntos_Corporativos", "valid_from": "2023", "valid_to": None, "evidence_claim_id": "P01-C05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Visión de Fuentes Originales vs Síntesis Interna en JTBD",
                "Fuentes Originales": "CCO como estratega de alto nivel que delega todo lo operativo y lidera la narrativa global.",
                "Síntesis Interna (Prevaleciente)": "CCO y equipo atrapados operativamente en más de un 60% en tareas reactivas urgentes."
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-C05-C1", "P01-C05-C2"],
                "difference": "Discrepancia entre la promesa comercial de automatización total por IA y el imperativo operativo de evitar alucinaciones en momentos de crisis.",
                "resolution": "resuelta",
                "reason": "Prevalece la versión de síntesis interna: automatización asistida con trazabilidad estricta y supervisión humana."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Implementar plantillas de briefing con verificación estricta de citas internas y cálculo de coherencia antes de emisión.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C06", "P01-C07"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C06",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre trabajos por hacer y momentos de presión, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:13:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba: 1) la medición auditada con cronómetro del tiempo real invertido en confeccionar dossiers de crisis (la meta 'de 4h a 15 min' es la hipótesis HT-2); 2) estudios empíricos longitudinales sobre el impacto de la IA en la preservación de la Licencia Social. Fuentes fallidas: Gartner (Future of Communications y Gartner for Communications), Global Alliance GCF Release, Gregory & Willis 2019, Page Society (Pacesetter y Corporate Character) y OECD Corporate Governance, todas por paywall, Cloudflare o WAF. Las fuentes comerciales son parciales al carecer de metodología abierta. Validación mínima: Fase 1 (15 entrevistas cualitativas con Dircoms) y Fase 2 (shadowing cronometrado en vivo durante la preparación de un comité de crisis).",
        "findings": [
            {
                "claim_id": "P01-C06-C1",
                "claim": "Siete fuentes del corpus P01 fallaron por barreras perimetrales técnicas y paywalls (Gartner x2, Global Alliance GCF Release, Gregory & Willis 2019, Page Society x2, OECD), lo que obligó a sustituirlas por literatura empírica de acceso abierto (ECM, Dircom ECE 2025, McKinsey 2025 y CMF NCG 461).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Auditoría de Manifiesto P01"},
                "evidence": [
                    {
                        "source_id": "9d107817-26eb-44c0-84cf-d5448ce9287a",
                        "source_title": "P01_SOURCE_INDEX",
                        "original_url": None,
                        "locator": "Tabla: Registro de Fuentes Fallidas Técnicamente y Fuentes Sustitutas",
                        "excerpt_short": "Identificación de 7 fuentes fallidas por paywalls y WAF, y delimitación de fuentes comerciales parciales.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación exhaustiva del índice de fuentes del cuaderno P01."
            },
            {
                "claim_id": "P01-C06-C2",
                "claim": "La afirmación de que un software de asistencia ejecutiva reduce el tiempo de preparación de minutas de 4 horas a 15 minutos carece de respaldo empírico en la literatura y constituye una hipótesis de diseño (HT-2) sujeta a validación experimental.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Chile", "actor": "Equipo BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Vacíos de Prueba y Fase 2 del Plan de Validación",
                        "excerpt_short": "La reducción de 4h a 15m es una hipótesis de trabajo HT-2 que requiere validación mediante shadowing.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Hipótesis analítica pendiente de validación empírica en terreno."
            }
        ],
        "operational_model": {
            "inputs": ["Protocolo de shadowing", "Cronómetro", "Muestra de 15 CCOs"],
            "actors": ["Investigador", "CCO Entrevistado", "Equipo Operativo"],
            "steps": ["Diseño de guía de entrevista", "Entrevistas en profundidad (Fase 1)", "Observación no participante de crisis simulada (Fase 2)", "Tabulación de tiempos"],
            "states": ["Protocolo_Aprobado", "Campo_En_Ejecucion", "Datos_Tabulados"],
            "outputs": ["Matriz de Tiempos Reales de Preparación y Puntos de Dolor"],
            "exceptions": ["Confidencialidad corporativa que impida presenciar comités de crisis en vivo"]
        },
        "entities": [
            {"entity_id": "ENT_PROTOCOLO_VALIDACION", "type": "metodologia_investigacion", "name": "Protocolo de Validación Empírica en 3 Fases", "aliases": ["Gaps & Validation Plan"]}
        ],
        "relations": [
            {"subject_id": "ENT_PROTOCOLO_VALIDACION", "predicate": "resuelve_incertidumbre_de", "object_id": "Hipotesis_HT2_Tiempo_Briefing", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C06-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Promesa de Ahorro de Tiempo vs Evidencia Disponible",
                "Afirmación Teórica / Comercial": "Reducción de 4 horas a 15 minutos en la confección de dossiers ejecutivos.",
                "Evidencia Empírica Disponible": "Cero mediciones cuantitativas auditadas en fuentes abiertas; catalogado como HT-2."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Incorporar telemetría de tiempos de uso y revisión de minutas en los pilotos de BRIDGE para contrastar la hipótesis HT-2.", "status": "hipotesis"}
        ],
        "open_gaps": [
            "Medición cuantitativa auditada de horas-hombre invertidas en la elaboración de dossiers de crisis en empresas de Chile y Latinoamérica.",
            "Impacto medible en reputación derivado del uso de herramientas de IA generativa en asuntos corporativos."
        ],
        "next_question_ids": ["P01-C07", "P01-C08"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C07",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre reuniones y decisiones críticas, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:13:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en dos paradojas: 1) Legalidad vs Legitimidad en Ley del Lobby: las fuentes originales (Ley 20.730, InfoLobby) tratan la audiencia como un mero cumplimiento registral administrativo ex-post, mientras la síntesis interna (P01_EVIDENCE_MAP, Paradoja 4) demuestra que cumplir la ley no blinda a la empresa si el vocero sostiene una postura contradictoria con los compromisos de sostenibilidad, transformando el registro en prueba de inconsistencia pública. 2) Estandarización Global ESG vs Hiper-localismo: normas como CMF NCG 461/519 y WEF promueven reportes contables globales (SASB/TCFD), mientras la síntesis interna (Paradoja 3, basada en Acción Empresas e ICARE) prueba que en mesas de diálogo territorial las comunidades exigen cumplimiento de compromisos locales concretos y RCA. Prevalece la síntesis interna: la legalidad formal no asegura legitimidad reputacional sin consistencia factual con la memoria histórica de la corporación.",
        "findings": [
            {
                "claim_id": "P01-C07-C1",
                "claim": "Frente a la concepción de la Ley N° 20.730 de Lobby como un trámite formal registral ex-post, la síntesis interna demuestra que si el discurso del vocero en la audiencia contradice los compromisos declarados en reportes de sostenibilidad o actas internas, el registro público en InfoLobby actúa como detonante de crisis mediáticas y regulatorias.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Sujetos Pasivos y Reguladores"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 de Lobby",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Arts. 5, 7 y 8",
                        "excerpt_short": "Registro público de materias, lobbistas y sujetos pasivos.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "80d4fcba-ae0d-4a1d-a36c-2f3b925b4fa2",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Paradoja 4: Cumplimiento Legal Formal vs. Confianza Real Ciudadana",
                        "excerpt_short": "La legalidad del acto no garantiza su legitimidad reputacional.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Prevalencia de la síntesis interna basada en casos chilenos y normativa de transparencia."
            },
            {
                "claim_id": "P01-C07-C2",
                "claim": "En mesas territoriales comunitarias, la estandarización contable global ESG (CMF NCG 461/519 y WEF) pierde eficacia frente a las demandas de cumplimiento de acuerdos locales concretos, empleo regional y resoluciones de calificación ambiental (RCA).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2026", "region": "Chile (Zonas Operacionales)", "actor": "Comunidades y Empresas"},
                "evidence": [
                    {
                        "source_id": "80d4fcba-ae0d-4a1d-a36c-2f3b925b4fa2",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Paradoja 3: Estandarización Global ESG vs. Hiper-Localismo Territorial",
                        "excerpt_short": "Las comunidades no evalúan a la empresa por un informe corporativo en PDF sino por el cumplimiento de compromisos locales.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Convergencia de reportes territoriales locales de Acción Empresas e ICARE."
            }
        ],
        "operational_model": {
            "inputs": ["Antecedentes normativos", "Agenda pública de autoridades", "Compromisos territoriales previos"],
            "actors": ["Lobbista Corporativo", "Sujeto Pasivo", "Dircom", "Comunidades"],
            "steps": ["Solicitud de audiencia", "Confección de minuta de posición", "Comparecencia", "Registro en InfoLobby", "Seguimiento comunitario"],
            "states": ["Audiencia_Solicitada", "Posicion_Contrastada", "Audiencia_Realizada", "Acta_Publicada"],
            "outputs": ["Registro fidedigno en InfoLobby y acta de compromisos"],
            "exceptions": ["Divergencia entre postura sostenida en reunión y discurso público de sostenibilidad"]
        },
        "entities": [
            {"entity_id": "ENT_PARADOJA_LOBBY", "type": "concepto_regulatorio", "name": "Paradoja de Legitimidad en Ley de Lobby", "aliases": ["Cumplimiento Legal vs Reputación"]}
        ],
        "relations": [
            {"subject_id": "ENT_PARADOJA_LOBBY", "predicate": "impacta_negativamente_en", "object_id": "Licencia_Social_Operar", "valid_from": "2014", "valid_to": None, "evidence_claim_id": "P01-C07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque Formal Registral vs Gestión de Consistencia Fáctica",
                "Enfoque Registral Formal (Fuentes Originales)": "Publicar en InfoLobby la fecha, sujeto pasivo y materia general.",
                "Enfoque de Consistencia (Síntesis Prevaleciente)": "Auditar que la postura sostenida en la reunión no contradiga compromisos históricos ni reportes ESG."
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-C07-C1", "P01-C07-C2"],
                "difference": "Tensión entre reportar métricas abstractas globales ESG y responder por compromisos operativos hiper-locales en territorio.",
                "resolution": "resuelta",
                "reason": "Prevalece la síntesis interna que exige cruzar los datos globales con el expediente territorial de cada faena."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "Estructurar la memoria de actores y compromisos territoriales con trazabilidad a expedientes RCA y actas de diálogo.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C08", "P01-C09"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C08",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre reuniones y decisiones críticas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:13:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba: 1) los criterios técnicos de objeción que imponen los CISOs y Fiscales de grandes empresas chilenas para autorizar la ingesta de actas confidenciales en herramientas analíticas; 2) la consistencia fáctica real entre minutas preparatorias internas y lo declarado en audiencias de la Ley de Lobby; 3) la disposición a pagar y preferencia por VPC on-premise en empresas del IPSA. Fuentes fallidas: OECD Corporate Governance (bloqueo scripts) y Page Society Pacesetter (Cloudflare WAF). Fuentes parciales: Ley 20.730 y CMF NCG 461 son parciales al limitarse al reporte administrativo ex-post sin registrar la preparación directiva interna. Validación mínima: Fase 3 del plan de investigación: prueba de concepto técnica con un panel evaluador tripartito (CCO, CISO y Fiscal Legal) para evaluar la arquitectura VPC.",
        "findings": [
            {
                "claim_id": "P01-C08-C1",
                "claim": "Los repositorios regulatorios oficiales de la CMF y la plataforma de Ley de Lobby son fuentes parciales de información, dado que se restringen a la declaración administrativa pública ex-post y no documentan la trastienda de deliberación, preparación de minutas y alineamiento de voceros.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "CMF e InfoLobby"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Evaluación de Fuentes Parciales y Vacíos de Trastienda Directiva",
                        "excerpt_short": "Las fuentes oficiales regulan el registro externo pero omiten el flujo interno de preparación.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Naturaleza jurídica y documental de los portales regulatorios."
            },
            {
                "claim_id": "P01-C08-C2",
                "claim": "La hipótesis de poder de veto del CISO y Fiscal Legal (HT-3) establece que la adopción de herramientas para preparar reuniones críticas depende de ofrecer despliegues en nube privada (VPC) con cifrado en reposo y garantía de no uso de datos para reentrenamiento de modelos.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Chile", "actor": "CISOs y Fiscalías Legales"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Fase 3 del Plan de Validación - Panel Tripartito CCO, CISO, Legal",
                        "excerpt_short": "La viabilidad B2B requiere sortear el veto de seguridad y cumplimiento mediante arquitectura VPC.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:13:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Formulación de arquitectura en el plan de validación de P01."
            }
        ],
        "operational_model": {
            "inputs": ["Requisitos de ciberseguridad corporativa", "Arquitectura VPC propuesta", "Políticas de retención de datos"],
            "actors": ["CCO (Comprador)", "CISO (Aprobador Seguridad)", "Fiscal Legal (Aprobador Compliance)"],
            "steps": ["Presentación de prototipo", "Revisión técnica de encriptación", "Auditoría de cumplimiento legal", "Dictamen de aprobación o veto"],
            "states": ["Revision_Iniciada", "Observaciones_Emitidas", "Dictamen_VPC_Aprobado"],
            "outputs": ["Matriz de Viabilidad de Seguridad y Compras B2B"],
            "exceptions": ["Veto definitivo por exigencia de almacenamiento local on-premise estricto"]
        },
        "entities": [
            {"entity_id": "ENT_PANEL_TRIPARTITO", "type": "proceso_adopcion_b2b", "name": "Panel Evaluador Tripartito (CCO, CISO, Fiscal Legal)", "aliases": ["Comité de Adopción Tecnológica"]}
        ],
        "relations": [
            {"subject_id": "ENT_PANEL_TRIPARTITO", "predicate": "condiciona_adopcion_de", "object_id": "BRIDGE_Executive_Assistant", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C08-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Modelo B2C/SaaS Abierto vs Requerimientos B2B Hiper-Regulados",
                "Modelo SaaS Genérico": "Suscripción directa por tarjeta de crédito usada por el Dircom en nube pública.",
                "Requerimiento Corporativo": "Aprobación de CISO/Legal, tenant aislado VPC, acuerdos de confidencialidad y no reentrenamiento."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Diseñar la ingesta de documentos reservados con opciones de aislamiento en VPC privada para neutralizar el veto de CISO y Legal.", "status": "hipotesis"}
        ],
        "open_gaps": [
            "Requisitos técnicos formales de encriptación exigidos por CISOs del sector financiero y minero en Chile para ingesta de documentos confidenciales.",
            "Consistencia documental entre minutas preparatorias y transcripciones de audiencias de lobby en ministerios clave."
        ],
        "next_question_ids": ["P01-C09", "P01-C10"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

with open("respuestas/temp_c05_c08.jsonl", "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("Generated 4 records in respuestas/temp_c05_c08.jsonl")
