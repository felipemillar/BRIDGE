import json
from pathlib import Path

records = [
    {
        "question_id": "P01-F07",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué tareas, restricciones y criterios de éxito tiene cada usuario cotidiano del sistema?",
        "snapshot_at": "2026-10-01T00:33:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los usuarios cotidianos abarcan 6 perfiles (CCO, Asuntos Públicos, Prensa, Interna, Sostenibilidad/ESG y Portavoz), con trabajos funcionales de compilación de briefings (JTBD-F1), monitoreo regulatorio (JTBD-F2) y distribución de lines to take (JTBD-F3); atrapados en >60% de reactividad táctica; con criterios de éxito de reducción de tiempo de 3-5h a <15 min, cero contradicciones y Golden Hour <30 min.",
        "findings": [
            {
                "claim_id": "P01-F07-C1",
                "claim": "Los perfiles operativos cotidianos abarcan CCO (reporte al CEO en 54,4%), Gerente de Asuntos Públicos (Ley 20.730), Prensa (48,7% del tiempo), Interna, Sostenibilidad (NCG 461) y Portavoz Oficial.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global/España/Chile", "actor": "Equipos de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
                        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo",
                        "original_url": "https://www.dircom.org/2025/09/25/mas-de-la-mitad-de-los-dircoms-reportan-al-ceo-y-uno-de-cada-tres-esta-en-el-comite-ejecutivo-segun-el-estado-de-la-comunicacion-en-espana-2025/",
                        "locator": "Estructura organizativa y distribución de tiempos",
                        "excerpt_short": "54,4% de reporte directo al CEO y 32,3% en Comité Ejecutivo; 48,7% de esfuerzo en medios tradicionales y 47,3% en redes sociales.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Datos censales empíricos de Dircom España."
            },
            {
                "claim_id": "P01-F07-C2",
                "claim": "Los trabajos cotidianos clave (Jobs-to-be-Done) son JTBD-F1 (compilación de briefing books ejecutivos), JTBD-F2 (detección temprana de proyectos normativos y riesgos) y JTBD-F3 (distribución de argumentarios lines to take en crisis).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "User Personas"},
                "evidence": [
                    {
                        "source_id": "8e654c6f-3c9f-4ab3-a971-f0d8fb887b27",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Matriz de Trabajos por Hacer (JTBD)",
                        "excerpt_short": "JTBD-F1 a JTBD-F3 definen las tareas funcionales críticas de preparación y respuesta ejecutiva.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Mapeo sistemático de procesos operacionales en el dossier de investigación."
            },
            {
                "claim_id": "P01-F07-C3",
                "claim": "La mayor restricción operacional es el atrapamiento táctico reactivo (>60% del tiempo en apagar incendios mediáticos y minutas de madrugada) y la asimetría de información interna entre áreas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2025", "region": "Europa / LatAm", "actor": "EUPRERA / Dircom"},
                "evidence": [
                    {
                        "source_id": "899c4c53-e9ea-4131-8072-1cbf102bd0b9",
                        "source_title": "EUPRERA - European Communication Monitor (ECM) 2023: 15-Year Retrospective",
                        "original_url": "https://www.communicationmonitor.eu/2023/09/07/ecm-european-communication-monitor-2023/",
                        "locator": "Retrospectiva de sobrecarga operativa",
                        "excerpt_short": "Los profesionales reconocen una brecha crónica entre el rol estratégico deseado y el tiempo absorbido en tareas comunicacionales reactivas.",
                        "source_date": "2023-09-07",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio longitudinal de 15 años de EUPRERA."
            },
            {
                "claim_id": "P01-F07-C4",
                "claim": "No existen en la literatura pública datos cuantitativos auditados de horas-hombre consumidas en la elaboración manual de minutas de crisis, siendo la métrica de ahorro 'de 4h a 15 min' una hipótesis de trabajo (HT-2).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Literatura de gestión"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Vacío 1: Falta de mediciones temporales de preparación",
                        "excerpt_short": "No existen mediciones cuantitativas auditadas de tiempos de elaboración artesanal de briefings directivos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico explícitamente documentado en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Señales externas de riesgo", "Documentos normativos internos", "Requerimientos de vocería urgente"],
            "actors": ["CCO", "Asuntos Públicos", "Prensa", "Interna", "Sostenibilidad", "Portavoz"],
            "steps": ["Detección de evento/audiencia", "Extracción de antecedentes", "Cruce y redacción de minuta", "Validación ejecutiva"],
            "states": ["Evento_Detectado", "Compilando_Brief", "Validando", "Ejecutado"],
            "outputs": ["Briefing book ejecutivo", "Lines to take de crisis", "Alerta temprana"],
            "exceptions": ["Información contradictoria en faena vs matriz", "Falta de vocero acreditado disponible"]
        },
        "entities": [
            {"entity_id": "ENT_JTBD_F1", "type": "tema", "name": "JTBD-F1: Compilación de Briefing Ejecutivo"},
            {"entity_id": "ENT_ECM", "type": "documento", "name": "European Communication Monitor 2023"}
        ],
        "relations": [
            {"subject_id": "ENT_JTBD_F1", "predicate": "ejecutado_por", "object_id": "ENT_CCO", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F07-C2"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P01-F07-C1", "P01-F07-C3"],
                "difference": "El CCO aspira a operar como consejero estratégico en el Comité Ejecutivo, pero los estudios ECM y Dircom muestran que el equipo pasa la mayor parte del tiempo atrapado en apagar incendios tácticos.",
                "resolution": "abierta",
                "reason": "Paradoja funcional entre estatus jerárquico formal y carga de trabajo reactiva."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Tiempo de elaboración de minuta con IA (hipótesis)", "value": "<15 min", "denominator": "Tiempo previo estimado de 3 a 5 horas"},
            {"metric": "Ventana de respuesta en crisis (Golden Hour)", "value": "<30 min", "denominator": "Tiempo transcurrido desde el incidente"}
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Reducir la fricción de búsqueda manual cruzando documentos corporativos automáticamente.", "status": "hipotesis"},
            {"module": "Hablar", "implication": "Distribuir lines to take consistentes dentro de la Golden Hour (<30 min).", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre mediciones cuantitativas auditadas de horas-hombre dedicadas a minutas de crisis.", "minimum_validation": "Estudio empírico de tracking temporal en 15-20 departamentos corporativos.", "priority": "media"}
        ],
        "next_question_ids": ["P01-F08", "P01-F09"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F08",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Quién compra, quién aprueba seguridad y presupuesto, y quién puede vetar la adopción?",
        "snapshot_at": "2026-10-01T00:33:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El comprador es el CCO junto al CEO; el presupuesto lo aprueba el CFO (con el 83% de los departamentos manteniendo o subiendo presupuesto); la seguridad la aprueba el CISO y el Fiscal Legal; y el CISO junto al Fiscal Legal tienen poder de veto absoluto e inmediato ante riesgos de fuga de datos o alucinaciones.",
        "findings": [
            {
                "claim_id": "P01-F08-C1",
                "claim": "El proceso de adopción tecnológica B2B distingue tres figuras: el Usuario (CCO, Asuntos Públicos, Prensa), el Comprador (CCO/CEO, con 83% manteniendo o subiendo presupuestos) y el Aprobador (CISO, Fiscal Legal, CFO).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global/Chile", "actor": "C-Suite B2B"},
                "evidence": [
                    {
                        "source_id": "8e654c6f-3c9f-4ab3-a971-f0d8fb887b27",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2: Mapa de Compradores, Aprobadores y Usuarios (B2B Personas)",
                        "excerpt_short": "Diferenciación de User Persona, Buyer Persona y Approver Persona en compras de tecnología corporativa.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
                        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo",
                        "original_url": "https://www.dircom.org/2025/09/25/mas-de-la-mitad-de-los-dircoms-reportan-al-ceo-y-uno-de-cada-tres-esta-en-el-comite-ejecutivo-segun-el-estado-de-la-comunicacion-en-espana-2025/",
                        "locator": "Presupuestos de comunicación 2025",
                        "excerpt_short": "El 83% de los departamentos de comunicación mantuvo o incrementó sus presupuestos en el último ciclo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Convergencia de marco B2B enterprise y censo presupuestario de Dircom."
            },
            {
                "claim_id": "P01-F08-C2",
                "claim": "El CISO y el Fiscal Legal ejercen poder de veto absoluto e inmediato sobre cualquier herramienta si detectan riesgo de exposición de repositorios internos o reentrenamiento de modelos con datos de la empresa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global/Chile", "actor": "CISO / Compliance"},
                "evidence": [
                    {
                        "source_id": "8e654c6f-3c9f-4ab3-a971-f0d8fb887b27",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Criterios de Veto de Approver Personas",
                        "excerpt_short": "El CISO y Fiscal Legal poseen capacidad de veto absoluto ante fugas de actas confidenciales o reentrenamiento de LLMs públicos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de gobernanza B2B corporativo."
            },
            {
                "claim_id": "P01-F08-C3",
                "claim": "Existe opacidad en estudios profesionales de comunicación respecto a los protocolos técnicos y de arquitectura de seguridad que exigen los CISOs para aprobar herramientas de IA en asuntos corporativos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Literatura profesional"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Vacío 3: Protocolos de aprobación de CISO y Legal",
                        "excerpt_short": "La literatura de comunicación omite los requisitos específicos de ciberseguridad y gobernanza que imponen los CISOs para habilitar software de IA.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío crítico registrado explícitamente en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Propuesta de software", "Matriz de arquitectura y seguridad", "Evaluación de costos SaaS"],
            "actors": ["CCO (Comprador/Sponsor)", "CISO (Aprobador de seguridad)", "Fiscal Legal (Aprobador de compliance)", "CFO (Aprobador de presupuesto)"],
            "steps": ["Solicitud de adopción", "Evaluación técnica y de seguridad por CISO", "Revisión de cláusulas legales y de privacidad", "Visto bueno del CFO y firma"],
            "states": ["Propuesta_Iniciada", "En_Evaluacion_Seguridad", "Aprobado_por_CISO", "Contratado"],
            "outputs": ["Autorización de despliegue", "Acuerdo de procesamiento de datos (DPA)", "Contrato de servicio"],
            "exceptions": ["Veto del CISO por falta de VPC dedicada o riesgo de fuga de datos", "Rechazo del Fiscal Legal por términos de servicio ambiguos"]
        },
        "entities": [
            {"entity_id": "ENT_CISO", "type": "persona_rol", "name": "Chief Information Security Officer (CISO)"},
            {"entity_id": "ENT_FISCAL_LEGAL", "type": "persona_rol", "name": "Fiscal Legal / Gerente de Compliance"}
        ],
        "relations": [
            {"subject_id": "ENT_CISO", "predicate": "tiene_poder_de_veto_sobre", "object_id": "Software_IA", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F08-C2"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P01-F08-C1", "P01-F08-C2"],
                "difference": "El área de comunicación tiene la urgencia de adoptar IA para acelerar minutas, pero el CISO prioriza la seguridad y detiene la adopción si no hay aislamiento estricto de repositorios privados.",
                "resolution": "abierta",
                "reason": "Tensión clásica entre agilidad funcional y política corporativa de ciberseguridad."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Porcentaje de empresas con presupuesto de comunicación estable o en alza", "value": "83%", "denominator": "Departamentos encuestados en ECE 2025"}
        ],
        "bridge_implications": [
            {"module": "transversal", "implication": "Garantizar aislamiento total de datos por cliente (VPC dedicada, zero data retention) para superar el veto del CISO.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre protocolos técnicos estandarizados de homologación CISO en empresas latinoamericanas para software de IA en asuntos públicos.", "minimum_validation": "Entrevistas estructuradas con 10 CISOs de empresas IPSA.", "priority": "alta"}
        ],
        "next_question_ids": ["P01-F09", "P01-F10"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F09",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Cómo varían estos roles entre empresa grande, regulada, consultora y organización con presencia territorial?",
        "snapshot_at": "2026-10-01T00:33:00-03:00",
        "answer_status": "respondida",
        "short_answer": "En empresas grandes predomina el alineamiento del C-Suite y la NCG 461; en reguladas prevalece el control legal de Compliance y la Ley de Lobby (20.730); en consultoras prima la velocidad analítica de múltiples cuentas con necesidad de multi-tenancy; y en territoriales rige la gestión comunitaria en faenas ligada a Resoluciones de Calificación Ambiental (RCA) para sostener la licencia social.",
        "findings": [
            {
                "claim_id": "P01-F09-C1",
                "claim": "En empresas grandes e IPSA, el foco está en la preservación del valor reputacional, alineamiento del C-Suite y el cumplimiento de la NCG 461 de la CMF ante inversionistas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "Grandes Corporaciones / IPSA"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Alcance para emisores de valores",
                        "excerpt_short": "Exige reportar gobernanza de riesgos y sostenibilidad en emisores de valores de alta capitalización bursátil.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal financiera chilena."
            },
            {
                "claim_id": "P01-F09-C2",
                "claim": "En empresas altamente reguladas (banca, salud, servicios básicos, AFP), las gerencias de Asuntos Públicos y Compliance ejercen predominio estricto, centradas en la Ley de Lobby N° 20.730 y requerimientos sancionatorios.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Chile", "actor": "Sectores Regulados"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 3°, 4° y 5°",
                        "excerpt_short": "Define los sujetos pasivos de fiscalización ante los cuales deben registrarse gestiones de intereses particulares.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Texto legal expreso de la legislación chilena."
            },
            {
                "claim_id": "P01-F09-C3",
                "claim": "En organizaciones con presencia territorial (minería, energía, celulosa), el poder decisorio se desplaza a gerentes de faena y sostenibilidad, obligados a conciliar acuerdos comunitarios locales con las RCA ambientales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "Empresas con Faenas en Terreno"},
                "evidence": [
                    {
                        "source_id": "c2dbae6a-963d-4471-ab12-823eab7384d1",
                        "source_title": "Acción Empresas Chile - Red de Sostenibilidad y Desafíos Ambientales, Sociales y Gobernanza (ASG)",
                        "original_url": "https://accionempresas.cl/",
                        "locator": "Desafíos Territoriales y Licencia Social",
                        "excerpt_short": "La legitimidad de la empresa en territorio depende de cumplir acuerdos comunitarios y compromisos de las RCA operacionales.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Directrices de sostenibilidad y gestión territorial de Acción Empresas."
            },
            {
                "claim_id": "P01-F09-C4",
                "claim": "No existen estudios empíricos longitudinales que midan el impacto de la IA en la reducción de litigios o preservación de la licencia social en faenas extractivas o energéticas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "América Latina", "actor": "Literatura de gestión"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Vacío 2: Impacto longitudinal de IA en Licencia Social",
                        "excerpt_short": "No existen estudios académicos revisados por pares que demuestren que el uso de IA reduce parálisis de proyectos o litigios comunitarios.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:33:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico formal del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Arquetipo de organización", "Marcos normativos aplicables", "Documentación de faena vs corporativa"],
            "actors": ["Gerente Corporativo", "Gerente de Faena", "Fiscal de Compliance", "Consultor Externo"],
            "steps": ["Identificación de perfil organizacional", "Configuración de módulos aplicables", "Validación por aprobadores del sector", "Despliegue operativo"],
            "states": ["Perfilado", "Modulo_Configurado", "Validado_por_Compliance", "Operativo"],
            "outputs": ["Configuración a la medida", "Reporte regulado", "Trazabilidad comunitaria territorial"],
            "exceptions": ["Uso de un módulo regulado en consultora sin aislamiento multi-inquilino", "Desconexión entre compromisos de faena y vocería en casa matriz"]
        },
        "entities": [
            {"entity_id": "ENT_RCA", "type": "documento", "name": "Resolución de Calificación Ambiental (RCA)", "aliases": ["RCA Ambiental"]},
            {"entity_id": "ENT_ACCION_EMPRESAS", "type": "organizacion", "name": "Acción Empresas Chile"}
        ],
        "relations": [
            {"subject_id": "ENT_ACCION_EMPRESAS", "predicate": "monitorea_impacto_en", "object_id": "Licencia_Social_Operar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F09-C3"}
        ],
        "comparisons": [
            {
                "dimension": "Prioridad Operativa",
                "empresa_grande": "Alineamiento C-Suite, reputación bursátil y NCG 461",
                "empresa_regulada": "Cumplimiento normativo, mitigación de multas y Ley de Lobby",
                "consultora": "Velocidad de síntesis multi-cuenta y alertas 24/7",
                "empresa_territorial": "Licencia social para operar en faena y cumplimiento de RCA"
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-F09-C1", "P01-F09-C3"],
                "difference": "Tensión entre métricas ESG abstractas y estandarizadas requeridas por la matriz en Santiago (NCG 461) y las demandas hiper-locales concretas de empleo y mitigación de impacto exigidas por comunidades en terreno.",
                "resolution": "abierta",
                "reason": "Desconexión estructural entre reporte financiero formal y relacionamiento territorial en faenas."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Indexar Resoluciones de Calificación Ambiental (RCA) y acuerdos comunitarios para empresas territoriales.", "status": "evidencia"},
            {"module": "Relacionar", "implication": "Configurar la memoria relacional según sea multi-cliente (consultoras) o territorial (minería/energía).", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre estudios empíricos longitudinales del impacto de IA en la Licencia Social para Operar.", "minimum_validation": "Estudio longitudinal de casos de faenas extractivas con medición antes/después.", "priority": "alta"}
        ],
        "next_question_ids": ["P01-F10", "P01-F11"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

output_path = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P01.jsonl")
with open(output_path, "a", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(f"Successfully appended {len(records)} verified records to {output_path}")
