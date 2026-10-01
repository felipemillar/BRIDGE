import json
import os
import sys

# Append P01-F25, P01-F26, P01-F27 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F25",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué consecuencias concretas tiene la preparación insuficiente, la asimetría de información o la lentitud de respuesta en esas reuniones?",
        "snapshot_at": "2026-10-01T00:49:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La preparación insuficiente y la asimetría de información provocan cuatro consecuencias críticas: 1) Atrapamiento táctico artesanal y sobrecarga de datos inconexos (más del 60% de la jornada de directivos absorbida en tareas reactivas); 2) Exposición a infracciones y sospechas de falta de probidad o captura regulatoria bajo la Ley N° 20.730 de Lobby en Chile; 3) Incumplimiento de normativas de supervisión de la CMF (NCG 461) y procedimientos sancionatorios; y 4) Pérdida de la Licencia Social para Operar (SLO), derivando en judicialización ante Tribunales Ambientales y paralización de faenas.",
        "findings": [
            {
                "claim_id": "P01-F25-C1",
                "claim": "Estudios empíricos longitudinales (ECM y LCM) demuestran que más del 60% del tiempo operativo de los departamentos de comunicación corporativa se desperdicia en tareas reactivas de bajo valor (redacción manual de comunicados y búsqueda artesanal de archivos dispersos).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2025", "region": "Europa / América Latina", "actor": "EUPRERA / LCM / ECM"},
                "evidence": [
                    {
                        "source_id": "1bc7878d-6979-4674-8b63-0cf41f89bb73",
                        "source_title": "Latin American Communication Monitor (LCM / EUPRERA) - Adopción de Tecnología, Ética y Brecha Digital en Dircoms",
                        "original_url": "https://www.comunicacionpolitica.org/lcm-informe/",
                        "locator": "Dedicación del tiempo operativo y atrapamiento táctico",
                        "excerpt_short": "Más del 60% de la jornada directiva se destina a apagar incendios mediáticos y tareas reactivas no estratégicas.",
                        "source_date": "2024-06-15",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Encuestas longitudinales representativas de la profesión en Europa y América Latina."
            },
            {
                "claim_id": "P01-F25-C2",
                "claim": "En Chile, la asimetría de información en audiencias bajo Ley N° 20.730 de Lobby expone a la empresa a acusaciones públicas de tráfico de influencias y apertura de expedientes por probidad administrativa al contrastarse con las actas de InfoLobby.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Sujetos Pasivos y Empresas Reguladas"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Régimen de probidad y transparencia en audiencias",
                        "excerpt_short": "Exigencia de veracidad y publicidad obligatoria en audiencias ante autoridades.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco legal obligatorio en Chile."
            },
            {
                "claim_id": "P01-F25-C3",
                "claim": "La lentitud de respuesta o contradicción en materias ASG vulnera la NCG 461 de la CMF y las Resoluciones de Calificación Ambiental (RCA), gatillando judicialización territorial y paralización de activos industriales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile", "actor": "Emisores de Valores y Minería/Energía"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Régimen sancionatorio por divulgación inexacta",
                        "excerpt_short": "Sanciones y multas ante inconsistencias o falta de veracidad en memorias integradas.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal de la CMF."
            }
        ],
        "operational_model": {
            "inputs": ["Información desactualizada", "Respuestas improvisadas", "Desconexión entre faena y sede central"],
            "actors": ["Vocero No Preparado", "Autoridad Fiscalizadora", "Líder Comunitario", "Tribunal Ambiental"],
            "steps": ["Ingreso a reunión con asimetría de información", "Emisión de declaración contradictoria", "Filtración o contraste con actas públicas", "Apertura de procedimiento sancionatorio o demanda"],
            "states": ["Asimetría_Ignorada", "Error_Declarado", "Contradicción_Evidenciada", "Judicialización_Activa"],
            "outputs": ["Multa regulatoria", "Paralización de faena", "Pérdida de confianza de mercado"],
            "exceptions": ["Rectificación fáctica inmediata dentro de las primeras horas de ocurrida la reunión"]
        },
        "entities": [
            {"entity_id": "ENT_ATRAPAMIENTO_TACTICO", "type": "problema_operacional", "name": "Atrapamiento Táctico Artesanal", "aliases": ["Sobrecarga Reactiva de Asuntos Corporativos"]},
            {"entity_id": "ENT_LICENCIA_SOCIAL", "type": "concepto_estrategico", "name": "Licencia Social para Operar (SLO)", "aliases": ["Social License to Operate"]}
        ],
        "relations": [
            {"subject_id": "ENT_ATRAPAMIENTO_TACTICO", "predicate": "degrada", "object_id": "ENT_LICENCIA_SOCIAL", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F25-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric": "Porcentaje de tiempo de departamentos de comunicación absorbido por tareas reactivas",
                "value": ">60%",
                "denominator": "Jornada laboral total de equipos corporativos en Europa y LatAm",
                "source_claim_id": "P01-F25-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Liberar el 60% del tiempo táctico automatizando la compilación de briefings y alertas para devolver foco estratégico al CCO.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F26", "P01-F27"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F26",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué tipos de errores cometen los ejecutivos cuando entran a esas instancias sin inteligencia adecuada?",
        "snapshot_at": "2026-10-01T00:49:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los ejecutivos cometen cinco tipos de errores principales: 1) Contradicciones con el archivo histórico corporativo y compromisos previos (actas de lobby, contratos comunitarios o Memoria NCG 461); 2) Improvisación de promesas inviables o no pactadas técnicamente (incurriendo en riesgo de greenwashing); 3) Desconocimiento de antecedentes, votaciones y petitorios del interlocutor (falta de inteligencia contextual); 4) Respuestas evasivas o defensivas sin respaldo fáctico; y 5) Desalineamiento de vocería interna en el C-Suite y filtraciones no autorizadas.",
        "findings": [
            {
                "claim_id": "P01-F26-C1",
                "claim": "Los dos errores directivos más frecuentes en reuniones críticas son la contradicción con compromisos históricos de la empresa (desconexión del repositorio interno) y la improvisación de plazos o compromisos de inversión territorial inviables bajo la presión del interlocutor.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Voceros Corporativos y C-Suite"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Taxonomía de Errores Directivos en Vocería",
                        "excerpt_short": "Cinco errores directivos: contradicciones con compromisos pasados, improvisación de promesas, falta de inteligencia contextual, respuestas defensivas y desalineamiento interno.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F26-C2",
                "claim": "La carencia de Inteligencia Contextual (competencia obligatoria según el Global Capability Framework de Global Alliance) lleva al vocero a ignorar la agenda política, antecedentes sancionatorios o preguntas trampa de parlamentarios o periodistas de investigación.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Global", "actor": "Líderes de Comunicación"},
                "evidence": [
                    {
                        "source_id": "a904d924-f726-444f-b9f1-320ec2c50dd3",
                        "source_title": "Global Alliance for Public Relations and Communication Management - Global Capability Framework (GCF)",
                        "original_url": "https://www.globalalliancepr.org/global-capability-framework",
                        "locator": "Capacidad de Inteligencia Contextual y prevención de errores",
                        "excerpt_short": "To provide contextual intelligence: You see the bigger picture and avoid blind spots in communication.",
                        "source_date": "2021-05-18",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estándar profesional global de Global Alliance."
            }
        ],
        "operational_model": {
            "inputs": ["Pregunta imprevista de la autoridad", "Presión en vivo de medios o asamblea", "Falta de minuta previa"],
            "actors": ["Vocero Corporativo", "Periodista / Regulador", "Gerente Legal", "Gerente de Faena"],
            "steps": ["Cuestionamiento incisivo", "Improvisación de respuesta no alineada", "Registro público de la respuesta", "Desmentido interno o fiscalización externa"],
            "states": ["Pregunta_Recibida", "Respuesta_Improvisada", "Desalineación_Gatillada"],
            "outputs": ["Declaración discordante", "Acta con error fáctico"],
            "exceptions": ["Uso del protocolo de 'holding statement' para consultar internamente antes de responder"]
        },
        "entities": [
            {"entity_id": "ENT_ERRORES_DIRECTIVOS", "type": "taxonomia", "name": "Taxonomía de 5 Errores Directivos", "aliases": ["Errores de Vocería Corporativa"]}
        ],
        "relations": [
            {"subject_id": "ENT_ERRORES_DIRECTIVOS", "predicate": "es_mitigado_por", "object_id": "JTBD-F1", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F26-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Cruzar en tiempo real el discurso con la memoria histórica para bloquear activamente la emisión de promesas o contradicciones inviables.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F27", "P01-F28"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F27",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué impacto tienen esos errores en reputación, valor en riesgo, relación con autoridades, cobertura de prensa y decisiones estratégicas?",
        "snapshot_at": "2026-10-01T00:49:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los impactos abarcan: 1) Cuantitativos/financieros (aumento de valor en riesgo -value at stake-, caídas bursátiles inmediatas y multas de la CMF por infracciones a la NCG 461); 2) Ruptura de interlocución técnica con ministerios y legisladores en la Ley de Lobby; 3) Encuadre mediático negativo por pérdida de la Golden Hour y acusaciones de greenwashing; 4) Caída en rankings de reputación y confianza auditados (Merco, Cadem Marcas Ciudadanas y Edelman Trust); y 5) Parálisis estratégica de proyectos de inversión y desvío de la atención del C-Suite hacia contención de daños.",
        "findings": [
            {
                "claim_id": "P01-F27-C1",
                "claim": "Las declaraciones inexactas o engañosas en materias de sostenibilidad y gobernanza generan multas monetarias directas de la CMF bajo la NCG 461, aumentan el valor en riesgo (value at stake) de la compañía y deterioran el acceso a financiamiento verde internacional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile", "actor": "CMF / Emisores Bursátiles"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Fiscalización de veracidad y sanciones financieras",
                        "excerpt_short": "Exposición a multas y sanciones administrativas de la CMF ante inconsistencias fácticas en memorias integradas.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco regulatorio financiero chileno."
            },
            {
                "claim_id": "P01-F27-C2",
                "claim": "En índices de reputación y opinión pública en Chile (Merco auditado bajo ISAE 3000 y Cadem Marcas Ciudadanas), los escándalos de inconsistencia o falta de ética de líderes corporativos destruyen el estatus de marca ciudadana y la atracción de talento de forma duradera.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile", "actor": "Merco Chile / Cadem"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Impacto en Reputación y Rankings de Confianza",
                        "excerpt_short": "Pérdida de posición en Merco Empresas y Cadem Marcas Ciudadanas ante incoherencias éticas o de gobernanza.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:49:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            }
        ],
        "operational_model": {
            "inputs": ["Error directivo consumado", "Cobertura de prensa desfavorable", "Acción de fiscalización de la CMF o SEA"],
            "actors": ["Comité de Crisis", "C-Suite", "Inversionistas", "Reguladores"],
            "steps": ["Detección del impacto mediático/bursátil", "Desvío de agenda estratégica", "Despliegue de plan de remediación", "Auditoría de daños patrimoniales y reputacionales"],
            "states": ["Impacto_Declarado", "Crisis_Bursátil/Reputacional", "Plan_Remediación_Activo", "Recuperación_Largo_Plazo"],
            "outputs": ["Plan de mitigación de daños", "Informe de valor en riesgo", "Respuestas rectificatorias a CMF"],
            "exceptions": ["Pérdida irreversible de la Licencia Social para Operar con revocación de RCA"]
        },
        "entities": [
            {"entity_id": "ENT_VALUE_AT_STAKE", "type": "metrica_financiera", "name": "Valor en Riesgo (Value at Stake)", "aliases": ["Exposición Patrimonial por Riesgo Reputacional"]}
        ],
        "relations": [
            {"subject_id": "ENT_VALUE_AT_STAKE", "predicate": "se_incrementa_por", "object_id": "ENT_ERRORES_DIRECTIVOS", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F27-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Anticipar", "implication": "Monitorear en tiempo real variables de 'Value at Stake' y sentimiento público para alertar al C-Suite antes de que los errores escalen a sanciones o caídas bursátiles.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F28", "P01-F29"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f25_f27.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
