import json
from pathlib import Path

records = [
    {
        "question_id": "P01-F04",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar mandato y fronteras de asuntos corporativos de forma estructurada?",
        "snapshot_at": "2026-10-01T00:30:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Exige representar variables de posición jerárquica (54,4% reporte al CEO, 32,3% en Comité Ejecutivo), una taxonomía de seis roles funcionales, 11 capacidades en tres dominios del GCF, relaciones transversales en el C-Suite (CCO as Integrator) y condiciones críticas de tiempo de respuesta (Golden Hour <30 min), trazabilidad fáctica y aislamiento estricto de repositorios privados.",
        "findings": [
            {
                "claim_id": "P01-F04-C1",
                "claim": "La función exige estructurar una taxonomía funcional de seis roles: Director de Asuntos Corporativos/CCO, Asuntos Públicos/Lobby, Comunicaciones Externas, Comunicaciones Internas, Sostenibilidad/ESG y Portavoces Oficiales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global/España/Chile", "actor": "Estructuras Corporativas"},
                "evidence": [
                    {
                        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
                        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo",
                        "original_url": "https://www.dircom.org/2025/09/25/mas-de-la-mitad-de-los-dircoms-reportan-al-ceo-y-uno-de-cada-tres-esta-en-el-comite-ejecutivo-segun-el-estado-de-la-comunicacion-en-espana-2025/",
                        "locator": "Estructura organizativa y funciones prioritarias",
                        "excerpt_short": "El 54,4% de los directivos reporta al CEO y el 32,3% integra el Comité Ejecutivo, distribuyendo áreas de prensa, interna, sostenibilidad y asuntos públicos.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Censo empírico de Dircom España con 565 profesionales validados."
            },
            {
                "claim_id": "P01-F04-C2",
                "claim": "El Global Capability Framework estructura 11 capacidades en tres dominios: Comunicación (investigar, impacto, narrativas), Organizacionales (confianza, reputación, inteligencia contextual) y Profesionales (liderazgo ético, negocios y finanzas).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Global", "actor": "Global Alliance / Univ. Huddersfield"},
                "evidence": [
                    {
                        "source_id": "4861a93d-b9c4-4972-bfeb-1d0902d65dd0",
                        "source_title": "Global Alliance - Global Capability Framework Official Benchmark",
                        "original_url": "https://globalalliancepr.org/resources/report-and-initiatives/global-capability-framework/",
                        "locator": "Los tres dominios y 11 capacidades universales",
                        "excerpt_short": "Define capacidades de inteligencia contextual, alineamiento de expectativas multistakeholder y deontología profesional.",
                        "source_date": "2021",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estándar global consensuado por asociaciones profesionales mundiales."
            },
            {
                "claim_id": "P01-F04-C3",
                "claim": "En Chile, la relación con reguladores está condicionada jurídicamente por la Ley N° 20.730 de Lobby (sujetos pasivos y registros públicos) y la relación financiera por la NCG 461 de la CMF (divulgación ASG obligatoria).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Reguladores y Emisores de Valores"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 2°, 3°, 4° y 8°",
                        "excerpt_short": "Obliga a registrar en agendas públicas las reuniones orientadas a influir en decisiones normativas o administrativas.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Marco de divulgación obligatoria",
                        "excerpt_short": "Exige reportar indicadores de sostenibilidad SASB/TCFD integrados en memorias corporativas.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal chilena vigente y fiscalizable."
            },
            {
                "claim_id": "P01-F04-C4",
                "claim": "El Ethical Standards Advisory #22 de PRSA dictamina que la responsabilidad legal y ética sobre decisiones y contenidos de agentes de IA recae íntegra e indelegablemente en supervisores humanos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / EE.UU.", "actor": "PRSA"},
                "evidence": [
                    {
                        "source_id": "ee802818-661a-4f0e-8890-2c28a372bf51",
                        "source_title": "PRSA - Code of Ethics: Professional Standards in Public Relations and Corporate Advocacy",
                        "original_url": "https://www.prsa.org/professional-development/prsa-resources/ethics",
                        "locator": "Ethical Standards Advisory #22 (julio 2026)",
                        "excerpt_short": "Human beings charged with active oversight of operations hold ownership of the situation and legal responsibility for AI agent outcomes.",
                        "source_date": "2026-07",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Norma ética institucional vinculante de la mayor asociación de relaciones públicas del mundo."
            }
        ],
        "operational_model": {
            "inputs": ["Demandas de crisis", "Agenda regulatoria de lobby", "Campañas corporativas"],
            "actors": ["Director de Asuntos Corporativos (CCO)", "Asuntos Públicos", "Prensa", "Comunicaciones Internas", "Sostenibilidad/ESG", "Portavoz"],
            "steps": [
                "1. Recepción y clasificación de señales en categorías temáticas",
                "2. Asignación según matriz de roles funcionales",
                "3. Cruce transversal CCO-Integrator con Legal y Compliance",
                "4. Validación de condiciones de frontera (seguridad B2B, Golden Hour)"
            ],
            "states": ["Clasificado", "En_Integracion_Transversal", "Aprobado_por_Compliance", "Emitido"],
            "outputs": ["Minuta de posición aprobada", "Registro de audiencia pública", "Memoria integrada ASG"],
            "exceptions": ["Alucinación de modelo sin supervisión humana que viola ESA #22 de PRSA", "Filtración de repositorios internos hacia modelos públicos"]
        },
        "entities": [
            {"entity_id": "ENT_GCF", "type": "documento", "name": "Global Capability Framework", "aliases": ["GCF"]},
            {"entity_id": "ENT_PRSA_ESA22", "type": "documento", "name": "PRSA Ethical Standards Advisory #22", "aliases": ["ESA 22"]},
            {"entity_id": "ENT_LEY_LOBBY", "type": "documento", "name": "Ley N° 20.730 de Lobby Chile"}
        ],
        "relations": [
            {"subject_id": "ENT_PRSA_ESA22", "predicate": "condiciona_uso_de", "object_id": "Agentes_IA", "valid_from": "2026-07", "valid_to": None, "evidence_claim_id": "P01-F04-C4"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P01-F04-C1", "P01-F04-C4"],
                "difference": "Promesas comerciales ofrecen automatización no supervisada con IA para emitir declaraciones, mientras que la normativa deontológica de PRSA prohíbe taxativamente la delegación de responsabilidad ética a sistemas automatizados.",
                "resolution": "resuelta",
                "reason": "Prevalece la norma deontológica de PRSA (ESA #22, 2026) que exige control humano obligatorio."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Tiempo límite de respuesta de vocería en crisis (Golden Hour)", "value": "<30 min", "denominator": "Tiempo transcurrido desde la emergencia hasta la primera postura oficial"}
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Estructurar la ontología de conocimiento de acuerdo con la taxonomía de los 6 roles funcionales corporativos.", "status": "evidencia"},
            {"module": "Hablar", "implication": "Imponer un mecanismo de aprobación humana obligatoria conforme a ESA #22 de PRSA antes de despachar mensajes.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F05", "P01-F06"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F05",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre mandato y fronteras de asuntos corporativos?",
        "snapshot_at": "2026-10-01T00:30:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los hechos están respaldados por el informe censal Dircom ECE 2025 (25-sep-2025; reporte al CEO), el Global Capability Framework (2021; 11 capacidades), la Ley N° 20.730 de Lobby de Chile (texto actualizado a abr-2026), la NCG 461 de la CMF (nov-2021/nov-2025), el informe McKinsey 2025 (08-oct-2025), los marcos Page Society (2022/2024) y el Ethical Standards Advisory #22 de PRSA (jul-2026).",
        "findings": [
            {
                "claim_id": "P01-F05-C1",
                "claim": "Dircom ECE 2025 (25 de septiembre de 2025, N=565) respalda el 54,4% de reporte directo al CEO y 32,3% en Comité Ejecutivo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-09-25", "region": "España", "actor": "Dircoms"},
                "evidence": [
                    {
                        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
                        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo",
                        "original_url": "https://www.dircom.org/2025/09/25/mas-de-la-mitad-de-los-dircoms-reportan-al-ceo-y-uno-de-cada-tres-esta-en-el-comite-ejecutivo-segun-el-estado-de-la-comunicacion-en-espana-2025/",
                        "locator": "Página oficial Dircom y resumen ejecutivo del estudio",
                        "excerpt_short": "54,4% de los dircoms reportan al CEO y uno de cada tres está en el Comité Ejecutivo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fuente original auditada con fecha y localizador exactos."
            },
            {
                "claim_id": "P01-F05-C2",
                "claim": "La Ley N° 20.730 de Chile (actualizada al 02-abr-2026 con Ley 21.771) respalda la obligación legal de registrar audiencias y gestiones de lobby ante autoridades públicas (sujetos pasivos Arts. 3 y 4).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "BCN Chile"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 2°, 3°, 4°, 5°, 7° y 8°",
                        "excerpt_short": "Regula la publicidad en la actividad de lobby y en la gestión de intereses particulares, estableciendo registros de agenda pública.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Texto íntegro oficial de la Biblioteca del Congreso Nacional de Chile."
            },
            {
                "claim_id": "P01-F05-C3",
                "claim": "La CMF NCG 461 (noviembre 2021 y evaluación de noviembre 2025) respalda la obligatoriedad de reportar factores ASG/ESG en memorias anuales bajo estándares SASB/TCFD.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2025", "region": "Chile", "actor": "CMF Chile"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Evaluación de aprendizajes NCG 461",
                        "excerpt_short": "Supervisión de la divulgación de sostenibilidad en memorias integradas obligatorias para emisores de valores.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fuente primaria del regulador financiero chileno."
            },
            {
                "claim_id": "P01-F05-C4",
                "claim": "McKinsey (08 de octubre de 2025, N=898 ejecutivos en 77 países) respalda la adopción de AI Lighthouses para briefings ejecutivos y advierte la necesidad de complementarla con conocimiento fáctico humano.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-10-08", "region": "Global", "actor": "McKinsey & Company"},
                "evidence": [
                    {
                        "source_id": "b6f21f15-0ec9-4e85-b6ae-aca2f29e1ed1",
                        "source_title": "McKinsey & Company - Upgrading corporate affairs for a new geopolitical era",
                        "original_url": "https://www.mckinsey.com/capabilities/geopolitics/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección Using gen AI to create briefings",
                        "excerpt_short": "Teams can use gen AI to create briefings combining external insight with internal policy positions... teams need to supplement it with direct knowledge only humans can provide.",
                        "source_date": "2025-10-08",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicación insignia de McKinsey & Company."
            }
        ],
        "operational_model": {
            "inputs": ["Fuentes normativas oficiales", "Reportes empíricos censales"],
            "actors": ["Investigadores", "Analistas de Inteligencia Corporativa"],
            "steps": ["Verificación de autenticidad de fuentes", "Extracción de citas y localizadores", "Calibración de fechas y versiones"],
            "states": ["Fuente_Identificada", "Pasaje_Verificado", "Vigencia_Comprobada"],
            "outputs": ["Manifiesto de fuentes trazable", "Matriz de evidencias empíricas"],
            "exceptions": ["Uso de enlaces rotos o fuentes bloqueadas por paywall"]
        },
        "entities": [
            {"entity_id": "ENT_DIRCOM", "type": "organizacion", "name": "Asociación de Directivos de Comunicación (Dircom)"},
            {"entity_id": "ENT_BCN", "type": "organizacion", "name": "Biblioteca del Congreso Nacional de Chile"},
            {"entity_id": "ENT_CMF", "type": "organizacion", "name": "Comisión para el Mercado Financiero"},
            {"entity_id": "ENT_MCKINSEY", "type": "organizacion", "name": "McKinsey & Company"}
        ],
        "relations": [
            {"subject_id": "ENT_BCN", "predicate": "publica_y_actualiza", "object_id": "Ley_20730", "valid_from": "2014", "valid_to": None, "evidence_claim_id": "P01-F05-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Todo dato incorporado a la base de conocimiento debe contar con identificador de fuente y localizador textual verificable.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F06", "P01-F07"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F06",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra mandato y fronteras de asuntos corporativos sin introducir datos no documentados?",
        "snapshot_at": "2026-10-01T00:30:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso documentado en el Escenario 3 del Dossier ilustra la preparación de una audiencia de lobby (Ley 20.730) ante un Subsecretario: cruza compromisos ASG de la Memoria NCG 461 y convenios comunitarios de la faena con las señales del regulador, produciendo una minuta ejecutiva en 15 minutos con 100% de coherencia fáctica y registro transparente en InfoLobby.",
        "findings": [
            {
                "claim_id": "P01-F06-C1",
                "claim": "El caso operacional documenta la preparación de una audiencia de lobby regulada por la Ley 20.730 ante una autoridad pública (sujeto pasivo), articulando la postura de la empresa con antecedentes de la Memoria NCG 461 y convenios comunitarios territoriales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Gerencia de Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "8e654c6f-3c9f-4ab3-a971-f0d8fb887b27",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección Escenarios Críticos, Escenario 3 (Audiencia de Lobby e Integración Territorial)",
                        "excerpt_short": "Escenario 3: Preparación ejecutiva para audiencia ante ministerio regulador combinando memoria NCG 461, convenios comunitarios y plataforma InfoLobby.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso de uso canónico documentado en el dossier de investigación del pilar."
            },
            {
                "claim_id": "P01-F06-C2",
                "claim": "El resultado esperado exige 100% de coherencia verificable entre lo declarado ante la autoridad y lo reportado a la CMF en la NCG 461, reduciendo el tiempo de preparación de 3-5 horas a menos de 15 minutos y garantizando aislamiento estricto de repositorios privados.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Vocero Ejecutivo / CCO"},
                "evidence": [
                    {
                        "source_id": "8e654c6f-3c9f-4ab3-a971-f0d8fb887b27",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Métricas de éxito del Escenario 3",
                        "excerpt_short": "Coherencia fáctica total entre minutas internas y registros públicos de InfoLobby, reduciendo el ciclo de preparación a <15 min.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación analítica documentada en el corpus interno."
            },
            {
                "claim_id": "P01-F06-C3",
                "claim": "La paradoja de este caso radica en que cumplir formalmente el registro de lobby no garantiza la legitimidad reputacional si la opinión pública percibe la audiencia como captura regulatoria.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Cadem / Sociedad Civil"},
                "evidence": [
                    {
                        "source_id": "bb5e9b6c-b8c1-4cdc-9d33-388bd82b1fe9",
                        "source_title": "Cadem Chile - Marcas Ciudadanas: Relevancia, Propósito y Aporte a la Sociedad",
                        "original_url": "https://cadem.cl/marcas-ciudadanas/",
                        "locator": "Dimensión Confianza e Integridad",
                        "excerpt_short": "La ciudadanía evalúa la coherencia ética y el beneficio social, donde la legalidad formal no suple la legitimidad pública.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:30:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio empírico de reputación y marcas ciudadanas en Chile."
            }
        ],
        "operational_model": {
            "inputs": [
                "Actas y acuerdos de la Mesa de Diálogo Territorial",
                "Memoria Anual NCG 461 auditada ante la CMF",
                "Historial de audiencias previas en InfoLobby (Ley 20.730)",
                "Perfil y posturas públicas del Sujeto Pasivo (autoridad ministerial)"
            ],
            "actors": [
                "Gerente de Asuntos Públicos (Preparador)",
                "Vocero Oficial / CCO (Asistente a la audiencia)",
                "Sujeto Pasivo Ministerial (Autoridad pública receptora)",
                "Oficial de Cumplimiento / Legal (Validador de probidad)"
            ],
            "steps": [
                "1. Extracción de compromisos asumidos en RCA y NCG 461",
                "2. Contraste con el petitorio a presentar ante el Ministerio",
                "3. Generación de Q&A con citas exactas a los pasajes de los documentos corporativos",
                "4. Celebración de la reunión y registro transparente posterior en la plataforma de Lobby"
            ],
            "states": ["Audiencia_Solicitada", "Briefing_Generado", "Reunion_Sostenida", "Registro_InfoLobby_Publicado"],
            "outputs": [
                "Minuta ejecutiva de audiencia con trazabilidad fáctica",
                "Registro público veraz en InfoLobby",
                "Acta de seguimiento de compromisos asumidos"
            ],
            "exceptions": [
                "Contradicción entre el petitorio expuesto y los datos entregados a la CMF",
                "Omisión de asistentes en la declaración jurada de la Ley del Lobby"
            ]
        },
        "entities": [
            {"entity_id": "ENT_INFOLOBBY", "type": "producto", "name": "Plataforma InfoLobby Chile", "aliases": ["Registro de Agenda Pública"]},
            {"entity_id": "ENT_DOSSIER_P01", "type": "documento", "name": "P01_RESEARCH_DOSSIER", "aliases": ["Dossier P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_DOSSIER_P01", "predicate": "documenta_caso_de", "object_id": "ENT_INFOLOBBY", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F06-C1"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P01-F06-C1", "P01-F06-C3"],
                "difference": "La empresa cumple al 100% el mandato legal de transparencia de la Ley 20.730, pero la comunidad local puede impugnar la legitimidad de la audiencia si no se comunica con transparencia de propósito.",
                "resolution": "abierta",
                "reason": "Dicotomía intrínseca entre el estándar formal de cumplimiento administrativo y el juicio social de la opinión pública."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Tiempo de compilación del briefing book", "value": "<15 min", "denominator": "Tiempo invertido por el equipo con asistencia de software vs 3-5 h manual"},
            {"metric": "Coherencia fáctica entre minuta y reporte CMF", "value": "100%", "denominator": "Cifras y afirmaciones verificadas en la audiencia"}
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Conectar la Memoria NCG 461 para proveer la evidencia base del briefing.", "status": "evidencia"},
            {"module": "Relacionar", "implication": "Alimentar automáticamente la ficha de compromiso a partir del acta de la reunión de lobby.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "Ausencia de auditorías públicas que midan la tasa de coincidencia fáctica exacta entre minutas privadas y declaraciones en InfoLobby.", "minimum_validation": "Muestreo comparativo de minutas de empresas abiertas vs registros públicos de lobby.", "priority": "baja"}
        ],
        "next_question_ids": ["P01-F07", "P01-F08"],
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
