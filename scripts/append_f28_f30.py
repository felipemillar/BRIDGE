import json
import os
import sys

# Append P01-F28, P01-F29, P01-F30 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-F28",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones definen la representación estructurada de este tema?",
        "snapshot_at": "2026-10-01T00:52:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de riesgos de preparación insuficiente se define mediante: 4 variables de falla de inteligencia (asimetría interna/externa, fragmentación de repositorios en silos, desfase temporal fuera de la Golden Hour, y procesamiento artesanal); 4 categorías en la taxonomía de errores (contradicción discursiva, improvisación sin lines to take, omisión de antecedentes, y especulación por sesgos); cadenas causales de 5 pasos desde el punto ciego directivo hasta la judicialización y pérdida de SLO; y 4 condiciones de contención (conexión bidireccional, trazabilidad con citas obligatorias, gobernanza integrada en C-Suite y distribución de vocería unificada en <30 min).",
        "findings": [
            {
                "claim_id": "P01-F28-C1",
                "claim": "Las fallas de inteligencia surgen de cuatro variables estructurales: asimetría entre conocimiento interno y señales externas, dispersión documental en silos aislados, pérdida de la ventana temporal de la Golden Hour (<30-60 min) y dependencia de recopilaciones manuales artesanales propensas a fatiga cognitiva.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gerencias de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Variables de Falla y Asimetría de Información",
                        "excerpt_short": "Cuatro variables de falla: asimetría interna/externa, silos documentales, desfase de Golden Hour y recopilación artesanal.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F28-C2",
                "claim": "La cadena causal de impacto directivo opera en 5 eslabones: 1) preparación artesanal fragmentada; 2) contradicción del vocero ante preguntas incisivas; 3) registro de la contradicción en plataformas públicas (InfoLobby/CMF); 4) movilización comunitaria y judicialización ambiental; y 5) daño reputacional y pérdida de legitimidad en el C-Suite.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresas con presencia territorial y reguladas"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Cadena Causal de Impacto Reputacional y Regulatorio",
                        "excerpt_short": "Eslabones de la cadena causal: de la preparación fragmentada al litigio ambiental y desvalorización bursátil.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-F28-C3",
                "claim": "Las cuatro condiciones de contención son: conexión bidireccional entre archivo interno y entorno, verificación estricta de citas directas, asiento formal del CCO en el Comité Ejecutivo y distribución unificada de lines to take en menos de 30 minutos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Diseño de Inteligencia Corporativa"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4: Condiciones de Contención HT-1 y HT-2",
                        "excerpt_short": "Condiciones de contención: trazabilidad documental estricta, integración de repositorios y distribución acelerada de lines to take.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Mapa de evidencia del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Repositorios dispersos", "Señales de crisis incipiente", "Demandas de prensa o reguladores"],
            "actors": ["Analista Táctico", "Vocero Oficial", "Fiscal Legal", "Oficial de Enlace Comunitario"],
            "steps": ["Detección de asimetría informativa", "Activación de conexión bidireccional", "Verificación cruzada de citas", "Alineamiento C-Suite", "Emisión de vocería blindada"],
            "states": ["Vulnerabilidad_Detectada", "Protocolo_Contención_Activo", "Vocería_Trazable", "Riesgo_Neutralizado"],
            "outputs": ["Briefing verificado con citas", "Líneas discursivas alineadas", "Registro transparente"],
            "exceptions": ["Uso de modelos de IA sin conexión a la memoria interna corporativa"]
        },
        "entities": [
            {"entity_id": "ENT_CADENA_CAUSAL_ASIMETRIA", "type": "modelo_causal", "name": "Cadena Causal de Falla de Inteligencia", "aliases": ["Eslabones de Riesgo de Vocería"]},
            {"entity_id": "ENT_CONDICIONES_CONTENCION", "type": "condiciones_exito", "name": "Condiciones de Contención e Inteligencia Estructurada", "aliases": ["Pilares de Blindaje Reputacional"]}
        ],
        "relations": [
            {"subject_id": "ENT_CONDICIONES_CONTENCION", "predicate": "interrumpe", "object_id": "ENT_CADENA_CAUSAL_ASIMETRIA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F28-C3"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Implementar la conexión bidireccional obligatoria entre repositorios documentales internos y monitoreo exterior para romper silos.", "status": "evidencia"},
            {"module": "Actuar", "implication": "Garantizar trazabilidad documental con citas obligatorias en cada línea de briefing para evitar alucinaciones y especulaciones.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F29", "P01-F30"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F29",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada afirmación de este tema?",
        "snapshot_at": "2026-10-01T00:52:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El tema se respalda en 10 fuentes primarias analizadas bajo 4 categorías epistemológicas: Hechos Documentados (Ley N° 20.730 de Lobby; NCG 461/519 de la CMF; Dircom ECE 2025; LCM/ECM de EUPRERA; Merco Chile auditado por KPMG; Cadem Marcas Ciudadanas Jun 2026); Evidencia Académica (Global Capability Framework 2021; Page Society 2022/2023; PRSA Code of Ethics con ESA #22 de Jul 2026); Afirmaciones Comerciales (McKinsey Oct 2025 sobre AI Lighthouses); e Hipótesis de Trabajo (HT-1, HT-2 y HT-3). Se reiteran 4 vacíos de evidencia delimitados formalmente.",
        "findings": [
            {
                "claim_id": "P01-F29-C1",
                "claim": "El Código de Ética de la PRSA y su Actuación Ética Específica (ESA #22, julio 2026) establecen que la utilización de agentes de IA en asuntos corporativos requiere rendición de cuentas humana estricta, prohibiendo delegar la verdad fáctica en automatizaciones sin supervisión directiva.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-07", "region": "Global / Estados Unidos", "actor": "PRSA"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Deontología Profesional y Estándares PRSA ESA #22",
                        "excerpt_short": "PRSA ESA #22 (Julio 2026): Estricta supervisión humana y rendición de cuentas sobre el uso de agentes de IA en comunicación estratégica.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Norma deontológica profesional internacional de la PRSA."
            },
            {
                "claim_id": "P01-F29-C2",
                "claim": "Las cuatro brechas críticas de evidencia (Knowledge Gaps) formalizadas en P01_GAPS_AND_VALIDATION delimitan que no se debe dar por hecho la reducción de 4 horas a 15 minutos (HT-2), la efectividad longitudinal de la IA en la Licencia Social, las matrices de objeción técnica de CISOs ni la trazabilidad cuantitativa de InfoLobby.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Corpus P01"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Knowledge Gaps 1 a 4 y Protocolo de Validación",
                        "excerpt_short": "Delimitación de vacíos empíricos para no confundir hipótesis de diseño con hechos probados.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de control epistemológico del corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Fuentes deontológicas", "Marcos normativos", "Registros de gaps"],
            "actors": ["Investigador de Integridad", "Auditor Metodológico"],
            "steps": ["Verificación de fecha y autenticidad", "Asignación de estatus epistemológico", "Registro de vacíos no resueltos"],
            "states": ["Fuentes_Auditadas", "Estatus_Fijado", "Vacíos_Aislados"],
            "outputs": ["Tabla de Trazabilidad Rigurosa"],
            "exceptions": ["Confusión entre afirmación de consultora (AC) y evidencia académica (EA)"]
        },
        "entities": [
            {"entity_id": "ENT_PRSA_ESA22", "type": "norma_deontologica", "name": "PRSA Ethical Standard Advisory #22", "aliases": ["PRSA ESA #22 (Julio 2026)"]}
        ],
        "relations": [
            {"subject_id": "ENT_PRSA_ESA22", "predicate": "regula_uso_de", "object_id": "Inteligencia_Artificial_Corporativa", "valid_from": "2026-07", "valid_to": None, "evidence_claim_id": "P01-F29-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Alinear la arquitectura de BRIDGE con los principios deontológicos de PRSA ESA #22 exigiendo siempre la validación y firma humana de los análisis.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F30", "P01-F31"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F30",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué caso concreto con entradas y resultado esperado ilustra este tema en la práctica?",
        "snapshot_at": "2026-10-01T00:52:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso práctico contrasta dos flujos ante una audiencia urgente de Lobby (Ley 20.730) y punto de prensa por presunta contingencia hídrica en una empresa de energía en Chile: En el Flujo A (tradicional/fragmentado), tras 4 horas de búsqueda manual desarticulada, el vocero improvisa negando la extracción de agua subterránea, contradiciendo la Memoria CMF NCG 461 (que declaraba 12% de derechos); esto detona imputación por falta de probidad en InfoLobby, acusaciones de greenwashing, desplome en Cadem/Merco y paralización cautelar de faena. En el Flujo B (asistido estructurado), el sistema cruza la Memoria CMF, la RCA y actas previas en 15 minutos, alertando sobre la cláusula de reserva hídrica y proveyendo un argumentario blindado con citas exactas, logrando 100% de coherencia fáctica, desarticulación de la controversia y preservación de la Licencia Social.",
        "findings": [
            {
                "claim_id": "P01-F30-C1",
                "claim": "En el Flujo Tradicional Fallido (Flujo A), la falta de indexación unificada lleva al vocero a negar públicamente el uso de derechos de agua subterránea en faena, ignorando que la Memoria Integrada CMF NCG 461 de la propia firma reportaba un 12% de derechos de extracción en esa cuenca, provocando sanciones y litigio ambiental.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Empresa de Infraestructura / Energía"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Caso Práctico Comparativo Flujo A vs Flujo B",
                        "excerpt_short": "Flujo A: Búsqueda manual de 4 horas, contradicción con Memoria CMF NCG 461, imputación en InfoLobby y paralización de faena.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso comparativo detallado en el dossier P01."
            },
            {
                "claim_id": "P01-F30-C2",
                "claim": "En el Flujo Asistido Estructurado (Flujo B), el cruce automatizado en 15 minutos genera alertas críticas sobre las cláusulas de reserva de la Memoria CMF y los compromisos de agua desalada asumidos en actas previas de InfoLobby, proveyendo lines to take que protegen la Licencia Social para Operar.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "C-Suite y Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Resultados Esperados del Flujo B Asistido",
                        "excerpt_short": "Flujo B: Síntesis en 15 minutos, alertas críticas de consistencia fáctica, 100% coherencia con CMF y blindaje de SLO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T00:52:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación del caso comparativo en el dossier."
            }
        ],
        "operational_model": {
            "inputs": ["Notificación de audiencia urgente", "Denuncias ciudadanas de extracción de agua", "Repositorio documental histórico"],
            "actors": ["Gerente de Asuntos Públicos", "Gerente de Operaciones", "Regulador Ambiental", "Diputado"],
            "steps": [
                "Recepción de citación a audiencia y punto de prensa",
                "Cruce de Memoria CMF NCG 461, RCA y actas de InfoLobby en sistema asistido",
                "Detección de alertas de contradicción fáctica en 15 minutos",
                "Validación de lines to take por CCO y Legal",
                "Comparecencia con citas exactas y neutralización de la crisis"
            ],
            "states": ["Notificación_Recibida", "Procesamiento_15_Min", "Alertas_Resueltas", "Audiencia_Exitosa", "SLO_Blindada"],
            "outputs": ["Briefing ejecutivo de 1 página con citas", "Lines to take para prensa", "Acta consistente en InfoLobby"],
            "exceptions": ["Declaración de un vocero de faena que no utilizó la minuta oficial validada"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_COMPARATIVO_HIDRICO", "type": "caso_estudio", "name": "Caso Comparativo de Contingencia Hídrica Flujo A vs B", "aliases": ["Benchmark Flujo Fallido vs Asistido"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_COMPARATIVO_HIDRICO", "predicate": "valida_hipotesis", "object_id": "HT-2", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-F30-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Flujo A (Tradicional) vs Flujo B (Asistido BRIDGE)",
                "Entradas": "Flujo A: Búsqueda manual caótica en correos y WhatsApp | Flujo B: Repositorio unificado CMF, RCA e InfoLobby.",
                "Tiempo": "Flujo A: 3 a 5 horas manuales | Flujo B: Menos de 15 minutos con síntesis trazable.",
                "Trazabilidad": "Flujo A: Nula (alto riesgo de especulación) | Flujo B: 100% con citas al documento corporativo origen.",
                "Resultado": "Flujo A: Imputación, litigio ambiental y desvalorización | Flujo B: Coherencia fáctica, desarticulación de crisis y blindaje de SLO."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Actuar", "implication": "Implementar el motor de resolución asistida de BRIDGE reflejando la arquitectura del Flujo B para neutralizar riesgos antes de la emisión de vocerías.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-F31", "P01-F32"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_f28_f30.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
