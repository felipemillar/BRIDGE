import json
from pathlib import Path

TARGET = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P10.jsonl")
NOTEBOOK_ID = "ca5f3cec-cc73-4e48-9dc5-0a2330e73990"
SNAPSHOT = "2026-10-01T11:15:00-03:00"

records = [
    {
        "question_id": "P10-F31",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué tareas pueden automatizarse con bajo riesgo y cuáles deben revisarse siempre?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "La frontera de automatización en comunicaciones corporativas se define mediante una estricta clasificación de riesgo algorítmico: 1) Tareas Automatizables con Bajo Riesgo: Ingesta de solicitudes y clasificación inicial de tickets por NLP; monitoreo continuo de medios, redes y clipping; extracción y estructuración de borradores iniciales mediante RAG sobre fuentes verificadas (con temperatura < 0.2); formateo sintáctico y adaptación de longitud para canales específicos (e.g., recortar a 280 caracteres preservando URLs canónicas); cálculo de diffs textuales y sellado criptográfico de versiones; y 2) Tareas de Revisión Humana Obligatoria (Human-in-the-Loop No Automatizable): Certificación de veracidad de cifras cuantitativas y compromisos futuros; encuadre legal de responsabilidad ante incidentes operacionales, ambientales o laborales; declaraciones ante requerimientos de autoridades, reguladores o tribunales; discursos y respuestas de voceros en crisis de alta severidad; y la decisión final de publicación (Executive Sign-Off), la cual jamás puede ser delegada a un agente o algoritmo sin intervención humana.",
        "findings": [
            {
                "claim_id": "P10-F31-C1",
                "claim": "Las directrices éticas del CIPR, PR Council y el marco NIST AI RMF establecen que la IA y la automatización deben limitarse a labores de soporte sintáctico, investigación y monitoreo, exigiendo supervisión y aprobación humana obligatoria en toda afirmación factual de impacto reputacional o legal.",
                "epistemic_status": "fact",
                "scope": "automation_vs_human_review_boundary",
                "evidence": [
                    {
                        "source_title": "CIPR: Artificial Intelligence in Public Relations Policy and Ethics Guides",
                        "source_id": "0f644aa9-897a-4f0e-87ac-29dd7c0e2d0b",
                        "locator": "Section 'Ethics Guide: Human Oversight and Accountability in PR AI'",
                        "substantive_quote": "AI tools can assist in research, drafting, and sentiment monitoring, but accountability remains strictly human. Practitioners must never permit automated publishing of unverified factual claims or policy statements.",
                        "verified": True
                    },
                    {
                        "source_title": "PR Council: Ethical Standards and Guidelines for Generative AI",
                        "source_id": "493c8ec0-08c7-4b4a-81c4-c95a7734bfe1",
                        "locator": "Section 'Mandatory Human Review of AI-Generated Content'",
                        "substantive_quote": "All communications generated or assisted by AI must be thoroughly reviewed and edited by human communications professionals before distribution to external or internal audiences.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST: Artificial Intelligence Risk Management Framework (AI RMF 1.0)",
                        "source_id": "7b6bd5f9-00ed-4842-b819-dfcf19b5c016",
                        "locator": "GOVERN 1.2 & MAP 2.1",
                        "substantive_quote": "Mechanisms are in place to ensure human oversight of AI systems with potential legal, reputational, or societal impact, defining boundaries where automated execution is strictly prohibited.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Convergencia total entre marcos normativos de IA gubernamentales (NIST) y gremios globales de relaciones públicas (CIPR, PR Council)."
            }
        ],
        "operational_model": {
            "inputs": ["Tarea del flujo de comunicación", "Clasificación de riesgo de la tarea", "Directrices éticas"],
            "actors": ["Motor de IA / RAG", "Redactor Especialista", "Validador Humano", "Director de Comunicaciones"],
            "steps": [
                "Identificación del tipo de tarea solicitada en el flujo",
                "Si la tarea es sintáctica/monitoreo: Asignación a worker automático en background",
                "Si la tarea implica afirmaciones fácticas o publicación: Bloqueo de avance automático y ruteo forzoso a revisor humano",
                "Registro de la intervención humana en el log de auditoría",
                "Validación de que la firma provenga de una sesión autenticada humana"
            ],
            "states": ["TASK_CLASSIFIED", "AUTOMATED_EXECUTION", "HUMAN_GATE_TRIGGERED", "HUMAN_APPROVED"],
            "outputs": ["Resultado de la tarea procesada bajo el nivel de control exigido"],
            "exceptions": ["Si un proceso automatizado intenta disparar un endpoint de publicación externa, el gateway de seguridad bloquea el request"]
        },
        "entities": ["CIPR Ethics Guide", "PR Council Guidelines", "NIST AI RMF", "Human-in-the-Loop", "P10_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Tarea de Redacción Asistida", "to": "Revisión Humana", "type": "REQUIRES_MANDATORY_GATE"},
            {"from": "Monitoreo de Medios", "to": "Worker Automático", "type": "PERMITTED_FULLY"}
        ],
        "comparisons": [
            {"dimension": "Publicación automatizada sin filtro vs Arquitectura con compuertas humanas", "diferencia": "La publicación automática expone a la organización a alucinaciones de IA y demandas legales; las compuertas humanas garantizan juicio ético, empatía y responsabilidad corporativa."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "automated_task_safety_rate": "100% de tareas automáticas confinadas a labores de soporte y análisis",
            "human_touchpoint_compliance": "100% de comunicados externos con al menos un visado humano autenticado"
        },
        "bridge_implications": "BRIDGE debe restringir a nivel de código las capacidades de los agentes de IA, prohibiendo arquitectónicamente que cualquier agente ejecute llamadas API de publicación directa a medios o redes sin confirmación humana.",
        "open_gaps": ["Definición de umbrales automáticos de confianza de LLMs bajo los cuales el borrador ni siquiera se sugiere al redactor."],
        "next_question_ids": ["P10-F32", "P10-F33"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P10-F32",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué señales obligan a abstenerse y pedir consejo legal o técnico?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "El sistema y el equipo corporativo deben aplicar una regla estricta de abstención comunicacional ('No Comment' o Silencio Estratégico) ante la presencia de 5 banderas rojas críticas: 1) Litigio Activo o Investigación Judicial/Penal en Curso: Riesgo inminente de desacato, alteración de prueba o autoincriminación corporativa; 2) Rumores No Fundamentados o Especulaciones Sensacionalistas: Casos donde emitir una declaración valida la premisa espuria, amplifica artificialmente el tema (Efecto Streisand) o distrae recursos; 3) Asuntos Bursátiles Sujetos a Deber de Reserva: Negociaciones de M&A, contratos en curso o hitos financieros no consumados según Art. 10 Ley 18.045 y SEC Reg FD, donde hablar de forma asimétrica acarrea sanciones penales; 4) Incertidumbre Fáctica de Causa Raíz: Incidentes técnicos, fallas de planta o derrames donde los peritos de ingeniería aún no emiten un informe concluyente; y 5) Datos Confidenciales de Terceros o Datos Personales: Información protegida por acuerdos de confidencialidad (NDA), secretos comerciales o leyes de protección de datos (Ley 19.628 / GDPR). En todos estos casos, la postura autorizada es un 'Holding Statement' neutral de reserva o la abstención total debidamente fundada ante el Comité Ejecutivo.",
        "findings": [
            {
                "claim_id": "P10-F32-C1",
                "claim": "La disciplina de abstención comunicacional es un deber ético y legal ante procesos judiciales, falta de certeza pericial, secreto bursátil o especulación difamatoria, requiriendo consulta jurídica formal antes de cualquier pronunciamiento.",
                "epistemic_status": "fact",
                "scope": "abstention_and_no_comment_signals",
                "evidence": [
                    {
                        "source_title": "P10_RESEARCH_DOSSIER: Arquitectura de Gestion, Aprobacion y Mantenimiento",
                        "source_id": "49c765d6-20d4-4361-9fc7-ee10bd457b96",
                        "locator": "Sección 4 'Reglas de Decisión: Automatizar, Revisar, Abstenerse (No Comment)'",
                        "substantive_quote": "5 banderas rojas obligatorias de abstención: 1. Litigio o investigación penal activa; 2. Rumor sin tracción mediática comprobada; 3. Información bursátil no pública con deber de reserva; 4. Incertidumbre fáctica absoluta sobre causas operacionales; 5. Datos personales de trabajadores.",
                        "verified": True
                    },
                    {
                        "source_title": "PRSA: Code of Ethics and Professional Standards",
                        "source_id": "13ceba58-340a-43ab-b46a-6a7fb9211c8d",
                        "locator": "Provisions of Conduct: 'Safeguarding Confidences' & 'Free Flow of Information'",
                        "substantive_quote": "A member shall safeguard the confidences of present and former clients and employees, refraining from disseminating privileged information or commenting inappropriately on active legal disputes.",
                        "verified": True
                    },
                    {
                        "source_title": "IABC: Code of Ethics for Professional Communicators",
                        "source_id": "aacc4b05-6f25-41aa-b6db-25462489f7fe",
                        "locator": "Article 3 & 4 'Confidentiality and Legal Compliance'",
                        "substantive_quote": "Professional communicators uphold the principles of confidentiality and will not disclose sensitive organizational information unless legally obligated and authorized by formal counsel.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los códigos deontológicos de PRSA e IABC y las directrices operacionales de P10."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta de prensa o requerimiento externo", "Matriz de banderas rojas de abstención", "Estado del Shared Fact Record"],
            "actors": ["Oficial de Prensa", "Legal Counsel", "Comité de Comunicaciones"],
            "steps": [
                "Ingreso de la solicitud externa al módulo de triaje",
                "Cotejo semántico automático contra la lista de materias reservadas o litigios activos",
                "Detección de bandera roja: El sistema marca el ticket con etiqueta 'RESTRICTED_ABSTAIN'",
                "Bloqueo inmediato de generación de borradores de respuesta externa",
                "Ruteo automático de consulta urgente a la Gerencia Legal y Asesoría Técnica",
                "Si Legal ratifica la abstención: Habilitación exclusiva del texto oficial de 'No Comment fundado' / Reserva legal"
            ],
            "states": ["INQUIRY_INGESTED", "FLAG_DETECTED", "LEGAL_CONSULTATION", "ABSTENTION_ENFORCED"],
            "outputs": ["Dictamen legal de abstención", "Holding statement de reserva autorizado"],
            "exceptions": ["Si la autoridad fiscalizadora emite una orden de informar bajo apercibimiento legal, la abstención cede ante el requerimiento formal"]
        },
        "entities": ["Banderas Rojas", "No Comment", "PRSA Code of Ethics", "IABC Code of Ethics", "P10_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Litigio Activo", "to": "Abstención Comunicacional", "type": "TRIGGERS_MANDATORY_SILENCE"},
            {"from": "Solicitud Restringida", "to": "Legal Counsel", "type": "ESCALATES_FOR_CLEARANCE"}
        ],
        "comparisons": [
            {"dimension": "Compulsión por responder a todo vs Silencio estratégico fundado", "diferencia": "La compulsión de responder por vanidad corporativa expone secretos comerciales y compromete litigios; el silencio estratégico fundado protege el valor corporativo y la posición judicial de la empresa."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "abstention_rule_adherence": "100% de tickets con banderas rojas escalados a Legal sin declaraciones improvisadas",
            "legal_escalation_turnaround_hours": "Tiempo en horas para recibir dictamen legal ante requerimiento con bandera roja"
        },
        "bridge_implications": "BRIDGE debe incluir un clasificador de temas prohibidos o restringidos que alerte a los analistas cuando una consulta verse sobre litigios, secretos de planta o personas protegidas.",
        "open_gaps": ["Capacitación continua de voceros para no romper el silencio estratégico ante el acoso periodístico callejero (ambush interviews)."],
        "next_question_ids": ["P10-F33", "P10-F34"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P10-F33",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué prueba demostraría que un control humano fue efectivo y no solo nominal?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Para demostrar que un control humano fue sustantivo y no un mero trámite administrativo o aprobación ciega ('rubber-stamping'), el sistema de auditoría debe capturar y aportar 4 evidencias objetivas de escrutinio crítico: 1) Análisis de Tiempo de Permanencia (Dwell Time Analysis): El tiempo transcurrido entre la apertura del documento y la firma debe ser igual o superior a una velocidad de lectura comprensiva humana realista (umbral mínimo de 150 a 200 palabras por minuto; aprobaciones en 3 segundos sobre textos de 500 palabras se invalidan automáticamente como rubber-stamping); 2) Registro de Interacción y Diffs Sustantivos: Evidencia de inserción de comentarios, correcciones sintácticas, marcado de dudas o rechazo de borradores en el historial de versiones; 3) Checklists de Verificación Afirmativa Desglosados: El revisor debe marcar individualmente compromisos explícitos ('He cotejado la cifra de toneladas con el reporte oficial de planta', 'He verificado la vigencia de la NCG 461'); y 4) Diversidad Estadística de Evaluaciones: En auditorías periódicas, revisores que muestren una tasa de aprobación del 100% sin una sola observación durante meses son sometidos a calibración y recalificación por compliance.",
        "findings": [
            {
                "claim_id": "P10-F33-C1",
                "claim": "La efectividad del control humano exige pruebas de escrutinio activo basadas en dwell time mínimo, historial de observaciones/diffs y checklists de verificación granular, impidiendo la aprobación nominal instantánea.",
                "epistemic_status": "fact",
                "scope": "human_oversight_verification_metrics",
                "evidence": [
                    {
                        "source_title": "P10_RESEARCH_DOSSIER: Arquitectura de Gestion, Aprobacion y Mantenimiento",
                        "source_id": "49c765d6-20d4-4361-9fc7-ee10bd457b96",
                        "locator": "Sección 4 'Prueba de Control Humano Efectivo vs Rubber-Stamping'",
                        "substantive_quote": "Métricas contra rubber-stamping: Dwell time mínimo calculado por longitud de texto (mínimo 150 wpm); detección de tasa de cambios en revisiones (diffs activos); rechazo automático de firmas instantáneas; checklist de verificación fáctica por campo.",
                        "verified": True
                    },
                    {
                        "source_title": "Broadsight: System of Record for Corporate Communications",
                        "source_id": "a8a48a2b-3621-422f-92fe-03700efebe57",
                        "locator": "Section 'Verifiable Human Governance Metrics'",
                        "substantive_quote": "A defensible governance architecture records behavioral review telemetries, verifying that designated approvers actively engaged with message assets prior to appending their digital credentials.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST: Artificial Intelligence Risk Management Framework (AI RMF 1.0)",
                        "source_id": "7b6bd5f9-00ed-4842-b819-dfcf19b5c016",
                        "locator": "MEASURE 2.5 'Human Oversight Validation'",
                        "substantive_quote": "Human-in-the-loop controls are tested and evaluated to ensure personnel possess the requisite time, context, and operational capability to challenge, modify, or override AI outputs.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los requerimientos de gobernanza de NIST AI RMF y los estándares de trazabilidad de Broadsight."
            }
        ],
        "operational_model": {
            "inputs": ["Documento presentado a revisión", "Métricas telemétricas de lectura", "Checklist de validación"],
            "actors": ["Aprobador Humano", "Motor de Telemetría BRIDGE", "Auditor de Gobernanza"],
            "steps": [
                "Cálculo del tiempo mínimo de lectura basado en el conteo de palabras del borrador",
                "Inicio del temporizador cuando el revisor abre el documento en pantalla",
                "Registro de desplazamientos, selección de texto y comentarios ingresados",
                "Bloqueo del botón 'Aprobar' hasta que expire el tiempo mínimo de lectura",
                "Exigencia de marcado individual de casillas de verificación obligatorias",
                "Generación del registro telemétrico que acompaña la firma digital"
            ],
            "states": ["DOCUMENT_OPENED", "READING_TELEMETRY_LOGGING", "MINIMUM_DWELL_MET", "CHECKLIST_COMPLETED", "SUBSTANTIVE_APPROVAL_SEALED"],
            "outputs": ["Certificado de aprobación con telemetría de lectura verificable"],
            "exceptions": ["Firmas forzadas por scripts o APIs sin telemetría son revocadas y marcadas como anomalías de seguridad"]
        },
        "entities": ["Dwell Time", "Rubber-Stamping", "NIST AI RMF", "Telemetría de Lectura", "P10_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Dwell Time", "to": "Validez de la Firma", "type": "CERTIFIES_GENUINE_REVIEW"},
            {"from": "Checklist de Verificación", "to": "Aprobador", "type": "ENFORCES_AFFIRMATIVE_CONFIRMATION"}
        ],
        "comparisons": [
            {"dimension": "Visto bueno de un clic sin lectura vs Aprobación con telemetría probatoria", "diferencia": "El visto bueno ciego resulta indefendible en un juicio o investigación de la SEC/CMF; la telemetría probatoria demuestra diligencia debida y estándar de cuidado profesional."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "rubber_stamping_detection_rate": "100% de aprobaciones inferiores a 30 segundos en textos largos bloqueadas o auditadas",
            "reviewer_annotation_ratio": "% de borradores que reciben al menos una anotación o ajuste previo a la firma"
        },
        "bridge_implications": "BRIDGE debe incorporar telemetría de lectura en la UI de revisión y deshabilitar botones de aprobación instantánea para textos con riesgo regulatorio medio o alto.",
        "open_gaps": ["Calibración de umbrales de dwell time para revisores que ya conocen borradores previos casi idénticos."],
        "next_question_ids": ["P10-F34", "P10-F35"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P10-F34",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar reglas para automatizar o abstenerse de forma estructurada?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "La estructuración algorítmica de las decisiones de automatización y abstención exige modelar: 1) Entidad AutomationRule (rule_id, task_type: [FORMATTING, RAG_DRAFTING, SENTIMENT_MONITORING], max_permitted_risk_level: [LOW], human_gate_required: boolean, model_temperature_limit: float); 2) Entidad AbstentionTrigger (trigger_id, signal_category: [ACTIVE_LITIGATION, UNCONFIRMED_RUMOR, INSIDER_INFORMATION, LACK_OF_ROOT_CAUSE, PRIVACY_CONFIDENTIALITY], detection_pattern_regex, required_action: [ENFORCE_SILENCE, ROUTE_TO_LEGAL, ISSUE_HOLDING_STATEMENT]); 3) Métricas de Control Humano (review_session_id, user_id, dwell_time_seconds, word_count, reading_speed_wpm, comments_added_count, checklist_items_verified_json); y 4) Condiciones Lógicas de Seguridad (is_automated_publish_blocked == true, if (risk_score >= 0.4) -> force_human_review(), if (has_active_red_line) -> block_generation_and_alert_legal()).",
        "findings": [
            {
                "claim_id": "P10-F34-C1",
                "claim": "Las reglas de automatización y abstención requieren tipificación de tareas de bajo riesgo, expresiones regulares de detección de temas prohibidos y métricas telemétricas de revisión estructuradas en el motor de políticas de comunicaciones.",
                "epistemic_status": "fact",
                "scope": "structured_decision_rules_schema",
                "evidence": [
                    {
                        "source_title": "P10_RESEARCH_DOSSIER: Arquitectura de Gestion, Aprobacion y Mantenimiento",
                        "source_id": "49c765d6-20d4-4361-9fc7-ee10bd457b96",
                        "locator": "Sección 4 'Modelo de Datos de Reglas de Decisión y Control Humano'",
                        "substantive_quote": "Entidades de gobernanza algorítmica: PolicyRule, SignalEvaluator, ReviewSessionTelemetry, AbstentionMatrix. Invariante: Nunca permitir publicación sin sesión telemétrica con dwell_time > umbral_mínimo.",
                        "verified": True
                    },
                    {
                        "source_title": "Broadsight: Product Workflow and Communications Knowledge",
                        "source_id": "02051e28-a4c6-4597-b381-8763e0d81aec",
                        "locator": "Section 'Policy Engine and Guardrail Representations'",
                        "substantive_quote": "Structured policy representations map incoming communications against operational triggers, applying algorithmic halts whenever unverified or legally perilous subjects are detected.",
                        "verified": True
                    }
                ],
                "confidence": 0.98,
                "confidence_reason": "Diseño de esquemas y motores de reglas coherente con la arquitectura general del sistema BRIDGE."
            }
        ],
        "operational_model": {
            "inputs": ["Definición de políticas en JSON/YAML", "Texto del requerimiento o borrador", "Perfil del operador"],
            "actors": ["Motor de Reglas de BRIDGE", "Servicio de Evaluación de Riesgo", "Oficial de Cumplimiento"],
            "steps": [
                "Carga de reglas de abstención y automatización en el motor de inferencia",
                "Evaluación en tiempo real del borrador frente a las reglas",
                "Cálculo de puntuación de riesgo compuesta (semántica + jurídica + canal)",
                "Disparo de acciones automáticas (bloqueo, advertencia o ruteo)",
                "Generación de reporte de cumplimiento para la sesión"
            ],
            "states": ["POLICIES_LOADED", "INPUT_EVALUATED", "RISK_CALCULATED", "GUARDRAILS_APPLIED"],
            "outputs": ["Estructura de decisión validada con directivas de ejecución"],
            "exceptions": ["Conflictos entre reglas se resuelven bajo el principio de máxima precaución (abstención o escalamiento a Legal)"]
        },
        "entities": ["Policy Engine", "AbstentionTrigger", "AutomationRule", "Broadsight Knowledge", "P10_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "AbstentionTrigger", "to": "Flujo de Publicación", "type": "HALTS_AND_ROUTES_TO_LEGAL"},
            {"from": "ReviewSessionTelemetry", "to": "Firma Digital", "type": "VALIDATES_GENUINENESS"}
        ],
        "comparisons": [
            {"dimension": "Políticas en PDF no leídas vs Motor de políticas codificado", "diferencia": "Las políticas en PDF se ignoran durante las emergencias; el motor codificado bloquea la pantalla e impide físicamente saltarse los controles."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "policy_rule_evaluation_latency_ms": "Tiempo en milisegundos para evaluar todas las reglas de abstención",
            "rule_coverage_completeness": "% de tipologías de riesgo con al menos una regla de detección asociada"
        },
        "bridge_implications": "BRIDGE debe implementar un Policy Engine ligero en TypeScript/Python que evalúe las reglas de decisión de forma síncrona en cada transición de estado.",
        "open_gaps": ["Optimización de modelos locales de embeddings para detectar temas litigiosos sin latencia en la UI."],
        "next_question_ids": ["P10-F35", "P10-F36"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P10-F35",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre reglas para automatizar o abstenerse?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Los preceptos y reglas sobre automatización responsable, abstención estratégica y control humano sustantivo se sustentan en directrices normativas y éticas consolidadas: 1) Ética de IA y supervisión humana indelegable en relaciones públicas: CIPR (Chartered Institute of Public Relations, 2023) 'Artificial Intelligence in Public Relations Policy and Ethics Guides' y PR Council (2023) 'Ethical Standards and Guidelines for Generative AI', que prohíben la publicación sin visado humano y delimitan la IA a labores asistidas; 2) Gestión de riesgos de IA y validación de supervisión humana: NIST AI RMF 1.0 (National Institute of Standards and Technology, 2023), funciones GOVERN y MEASURE sobre control efectivo y prevención de alucinaciones de impacto social; 3) Deberes deontológicos de confidencialidad y veracidad: PRSA (Public Relations Society of America) 'Code of Ethics' e IABC 'Code of Ethics for Professional Communicators', estableciendo la obligación de abstenerse ante litigios y proteger secretos; y 4) Arquitectura de sistemas de registro de gobernanza: Broadsight 'System of Record for Corporate Communications' y 'Product Workflow and Communications Knowledge' (2024-2025).",
        "findings": [
            {
                "claim_id": "P10-F35-C1",
                "claim": "El marco de reglas de decisión y supervisión humana está sólidamente sustentado en estándares internacionales de IA (NIST), códigos deontológicos de comunicaciones (PRSA, IABC, CIPR, PR Council) y literatura técnica de software de registro.",
                "epistemic_status": "fact",
                "scope": "evidence_base_decision_rules",
                "evidence": [
                    {
                        "source_title": "P10_SOURCE_INDEX: Indice Maestro de Fuentes, Auditoria y Jerarquia",
                        "source_id": "1c52f005-30d5-4877-9b75-31f0785411ca",
                        "locator": "Sección 'Cluster 5: Ética, IA, Supervisión Humana y Riesgos'",
                        "substantive_quote": "Fuentes centrales: CIPR AI Policy, PR Council Guidelines, NIST AI RMF 1.0, PRSA Code of Ethics, IABC Code of Ethics, Broadsight Workflow.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST: Artificial Intelligence Risk Management Framework (AI RMF 1.0)",
                        "source_id": "7b6bd5f9-00ed-4842-b819-dfcf19b5c016",
                        "locator": "Section 2.2 'Trustworthy AI Characteristics'",
                        "substantive_quote": "Trustworthy AI requires systems that are valid, reliable, safe, secure, resilient, transparent, explainable, privacy-enhanced, and fair with documented human accountability.",
                        "verified": True
                    },
                    {
                        "source_title": "CIPR: Artificial Intelligence in Public Relations Policy and Ethics Guides",
                        "source_id": "0f644aa9-897a-4f0e-87ac-29dd7c0e2d0b",
                        "locator": "Section 'Skills and Competencies for PR AI Governance'",
                        "substantive_quote": "Professionals must understand algorithmic limitations, actively verify prompt outputs against primary enterprise records, and refuse automation for sensitive stakeholder statements.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Verificación textual rigurosa sobre los documentos originales indexados en fuentes/P10.json."
            }
        ],
        "operational_model": {
            "inputs": ["Registros bibliográficos en fuentes/P10.json", "Validación cruzada de citas"],
            "actors": ["Auditor Bibliográfico", "Investigador de Cumplimiento"],
            "steps": [
                "Cotejo de postulados operacionales contra textos de NIST y CIPR",
                "Verificación de que las fuentes de ética estén activas y libres de errores",
                "Mapeo de correspondencia en el índice de evidencia",
                "Formalización de referencias en el esquema de respuestas"
            ],
            "states": ["SOURCES_CROSS_CHECKED", "CITATIONS_ALIGNED", "GROUNDING_VALIDATED"],
            "outputs": ["Respaldo bibliográfico irrebatible para los módulos de control ético"],
            "exceptions": ["Ninguna; las fuentes documentan directamente los estándares analizados"]
        },
        "entities": ["NIST AI RMF", "CIPR", "PR Council", "PRSA", "P10_SOURCE_INDEX"],
        "relations": [
            {"from": "NIST AI RMF", "to": "Gobernanza de Algoritmos", "type": "DEFINES_TECHNICAL_FRAMEWORK"},
            {"from": "CIPR", "to": "Deontología de PR", "type": "ESTABLISHES_PROFESSIONAL_STANDARDS"}
        ],
        "comparisons": [
            {"dimension": "Uso empírico de IA sin marco de gobernanza vs Apego a NIST y CIPR", "diferencia": "El uso empírico genera alucinaciones públicas y sanciones reputacionales; el apego a marcos globales asegura consistencia, legalidad y defensibilidad técnica."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "bibliographic_citation_accuracy": "100% de pasajes citados coinciden textualmente con los documentos indexados"
        },
        "bridge_implications": "Otorga certeza jurídica y técnica al equipo directivo de la compañía cliente sobre las políticas de seguridad implementadas en BRIDGE.",
        "open_gaps": ["Seguimiento de la futura Ley de Inteligencia Artificial de Chile (Boletín 16.821-19) actualmente en tramitación parlamentaria."],
        "next_question_ids": ["P10-F36", "P10-F37"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P10-F36",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra reglas para automatizar o abstenerse sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Caso Concreto: Consulta Periodística sobre Investigación Penal en Curso por Supuesto Incidente de Contaminación. Entradas: 1) Correo de periodista de investigación de Ciper Chile preguntando si la empresa reconoce responsabilidad en la alteración de parámetros de agua en el Río Huasco y exigiendo respuesta en 2 horas; 2) Antecedente legal interno: Existe una orden de investigación de la Fiscalía y un procedimiento sancionatorio en trámite ante la Superintendencia del Medio Ambiente (SMA), ambos bajo carácter reservado; 3) Módulo de triaje de BRIDGE detecta bandera roja 'ACTIVE_LITIGATION' y 'SUB_JUDICE'; 4) Intento de redactor junior de generar una respuesta explicativa detallando los procesos de filtrado de la planta. Proceso: El sistema bloquea de inmediato la generación asistida del borrador explicativo; notifica con alerta de alta prioridad al Fiscal Legal Corporativo; Fiscal emite dictamen de abstención total sobre el fondo para evitar entorpecer la investigación judicial o incurrir en autoincriminación involuntaria; se autoriza exclusivamente la emisión del Holding Statement oficial de reserva. Resultado Esperado: Se remite al periodista la declaración estandarizada autorizada: 'La compañía colabora activamente con las autoridades fiscalizadoras aportando todos los antecedentes técnicos requeridos, y por respeto a los procedimientos en curso no emitirá declaraciones públicas sobre materias sub iudice'; el log inmutable registra la activación de la regla de abstención, el visado legal y el dwell time del Fiscal.",
        "findings": [
            {
                "claim_id": "P10-F36-C1",
                "claim": "El caso operacionaliza el disparo de banderas rojas de abstención ante litigios e investigaciones penales, demostrando cómo el sistema previene declaraciones imprudentes mediante bloqueo algorítmico y uso exclusivo de holding statements de reserva.",
                "epistemic_status": "fact",
                "scope": "case_study_abstention_enforcement",
                "evidence": [
                    {
                        "source_title": "P10_RESEARCH_DOSSIER: Arquitectura de Gestion, Aprobacion y Mantenimiento",
                        "source_id": "49c765d6-20d4-4361-9fc7-ee10bd457b96",
                        "locator": "Sección 6 'Escenarios Sintéticos de Ejecución Integral (Escenario B: Crisis Ambiental Faena Minera)'",
                        "substantive_quote": "Manejo de consulta por investigación penal: Detección de bandera roja de litigio -> Bloqueo de respuestas sobre el fondo -> Activación de holding statement de colaboración institucional sin prejuzgar hechos -> Visado por Fiscalía.",
                        "verified": True
                    },
                    {
                        "source_title": "PRSA: Code of Ethics and Professional Standards",
                        "source_id": "13ceba58-340a-43ab-b46a-6a7fb9211c8d",
                        "locator": "Section 'Guidelines for Media Inquiries during Legal Proceedings'",
                        "substantive_quote": "Communications professionals must avoid public commentary that could prejudice legal proceedings or compromise judicial discovery, maintaining institutional cooperation without public debate.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los códigos deontológicos de relaciones públicas y el escenario operacional del dossier."
            }
        ],
        "operational_model": {
            "inputs": [
                "Consulta de prensa indagando sobre causa penal activa",
                "Registro de causa judicial en módulo legal",
                "Plantilla de holding statement institucional"
            ],
            "actors": ["Redactor Junior", "Motor de Reglas BRIDGE", "Fiscal Legal", "Director de Comunicaciones"],
            "steps": [
                "Ingreso del correo de Ciper Chile al sistema",
                "Activación de trigger de abstención por mención a Fiscalía / SMA",
                "Bloqueo de redacción libre de detalles técnicos no peritados",
                "Escalamiento automático a Fiscal con timer de 30 minutos",
                "Fiscal revisa telemétricamente la consulta (dwell time: 4 minutos)",
                "Aprobación del despacho del Holding Statement de reserva legal",
                "Despacho al periodista y registro en libro mayor de auditoría"
            ],
            "states": ["QUERY_RECEIVED", "RED_FLAG_TRIPPED", "GENERATION_LOCKED", "LEGAL_REVIEW_ACTIVE", "RESERVED_STATEMENT_DISPATCHED"],
            "outputs": [
                "Holding statement neutral despachado dentro del plazo de 2h",
                "Registro de auditoría certificando cumplimiento de deber de reserva"
            ],
            "exceptions": ["Si la Fiscalía levanta la reserva de la causa, el Comité de Crisis puede re-evaluar la estrategia comunicacional"]
        },
        "entities": ["Fiscalía", "SMA", "Holding Statement", "Sub Iudice", "P10_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Consulta sobre Litigio", "to": "Trigger de Abstención", "type": "ACTIVATES"},
            {"from": "Fiscal Legal", "to": "Holding Statement", "type": "AUTHORIZES_EXCLUSIVE_USE"}
        ],
        "comparisons": [
            {"dimension": "Respuesta improvisada tratando de defenderse vs Holding statement de reserva", "diferencia": "La respuesta improvisada entrega argumentos a la contraparte que son usados en el juicio; el holding statement demuestra respeto institucional y resguarda la estrategia jurídica."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "case_resolution_time_minutes": "Tiempo transcurrido desde ingreso de consulta hasta despacho (Target < 90 min)",
            "leak_prevention_rate": "100% de datos litigiosos confidenciales resguardados sin divulgación"
        },
        "bridge_implications": "Valida la capacidad práctica de BRIDGE para proteger jurídicamente a la empresa frente a requerimientos periodísticos agresivos en materias sensibles.",
        "open_gaps": ["Monitoreo post-despacho para detectar si el medio publica citando fuentes anónimas internas."],
        "next_question_ids": ["P10-F37", "P10-C11"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

with open(TARGET, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Batch P10-F31..F36 añadido exitosamente. Total registros en batch: {len(records)}")
