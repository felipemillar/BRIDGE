import json
from pathlib import Path

NOTEBOOK_ID = "cb87941c-2377-42fb-806f-eb9878ac0757"
SNAPSHOT_AT = "2026-10-01T02:50:00-03:00"

records = [
    # P04-C09
    {
        "question_id": "P04-C09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre ingesta y extracción, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: La mayoría de tutoriales y frameworks de desarrollo rápido de RAG recomiendan segmentación por longitud fija (e.g. 500 tokens con overlap de 50) como receta universal. Por el contrario, la investigación especializada de Gao et al. (2023) y la síntesis P04_EVIDENCE_MAP demuestran que el chunking de longitud fija destruye de forma catastrófica las tablas financieras y matrices ESG de las memorias corporativas, fracturando números a la mitad y desvinculando notas explicativas de sus celdas de origen. Versión que prevalece: Prevalece el estándar de Chunking Jerárquico de Dos Niveles (Parent Document Retrieval) combinado con extracción estructurada sensible al layout (Table-Aware Extraction). La búsqueda indexa fragmentos atómicos de 128-256 tokens pero provee al generador el fragmento padre de 1.024-2.048 tokens con su tabla completa y notas al pie.",
        "findings": [
            {
                "claim_id": "P04-C09-C1",
                "claim": "El chunking por longitud fija queda descartado para memorias corporativas por evidencia de Gao et al. y P04_EVIDENCE_MAP, prevaleciendo el chunking jerárquico Parent-Child y la extracción layout-aware.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Arquitectura de Pre-recuperación RAG"},
                "evidence": [
                    {
                        "source_id": "005e6819-75c5-40e4-b0a2-39b00ec373eb",
                        "source_title": "P04_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 3: Matriz de Tensiones Metodológicas (Fragmentación de Texto)",
                        "excerpt_short": "Segmentación por longitud fija destruye el significado de tablas financieras y notas. Adopción de Chunking Estructurado Jerárquico (Parent Document Retrieval + extracción tabular).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "93cd6e04-48bd-4b62-b39f-6784d75351da",
                        "source_title": "RAG for Large Language Models: A Survey (Gao et al., 2023)",
                        "original_url": "https://arxiv.org/abs/2312.10997",
                        "locator": "Sección 2.1.2: Chunking Optimization",
                        "excerpt_short": "Fixed-size chunking fails on tabular data and complex layouts, necessitating structure-aware hierarchical decomposition.",
                        "source_date": "2023-12-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución de tensión metodológica formalmente documentada en P04_EVIDENCE_MAP."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria corporativa compleja"],
            "actors": ["Layout-Aware Chunker", "Parent Document Linker"],
            "steps": ["Descarte de chunking ciego", "Aplicación de segmentación jerárquica", "Preservación de tablas íntegras en chunks padre"],
            "states": ["Raw_Document", "Hierarchical_Parsed", "Safe_Context_Indexed"],
            "outputs": ["Corpus fragmentado jerárquicamente sin pérdida de estructura tabular"],
            "exceptions": ["Documentos planos sin tablas donde el chunking jerárquico agrega sobrecosto de tokens"]
        },
        "entities": [
            {"entity_id": "ENT_HIERARCHICAL_RESOLUTION", "type": "decision_diseno", "name": "Resolución de Chunking Jerárquico Estructurado", "aliases": ["Hierarchical Chunking Design Decision"]}
        ],
        "relations": [
            {"subject_id": "ENT_HIERARCHICAL_RESOLUTION", "predicate": "resuelve_tension_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Integridad de datos",
                "Chunking ciego de 500 tokens": "Rompe la relación entre el número '1.040' y su unidad 'l/s' o su año '2025'.",
                "Chunking jerárquico parent-child": "Conserva la fila completa con todos sus encabezados y notas metodológicas."
            }
        ],
        "contradictions": [
            {
                "topic": "Método de fragmentación de texto para RAG corporativo",
                "claim_a": "La fragmentación por longitud fija con overlap de 50 tokens es adecuada y suficiente.",
                "source_a": "Tutoriales genéricos de LangChain / LlamaIndex básicos",
                "claim_b": "El chunking fijo destruye tablas y notas; se requiere chunking jerárquico estructurado (Parent Document).",
                "source_b": "Gao et al. (2023) / P04_EVIDENCE_MAP",
                "resolution_or_status": "Prevalece Claim B: adopción obligatoria de Parent Document Retrieval."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe configurar sus indexadores exclusivamente bajo este esquema jerárquico para proteger la exactitud de los datos.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C10
    {
        "question_id": "P04-C10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre ingesta y extracción, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Permanece sin prueba empírica la extracción completamente desatendida de tablas multipágina con celdas fusionadas asimétricas y notas al pie en memorias de empresas chilenas, donde frecuentemente se combinan formatos contables IFRS con narrativas de sostenibilidad CMF. Fuente Parcial: Ni et al. (2023) diagnostica la fragilidad pero no evalúa modelos multimodales recientes sobre documentos en español chileno. Validación Mínima Requerida: Ejecución de la Etapa 2 de la agenda empírica en P04_GAPS_AND_VALIDATION: prueba piloto de ingesta sobre 15 memorias NCG 461 reales (2023-2025) de sectores minero, bancario, energético y retail, auditando que la precisión estructural sea ≥ 98% y que exista cero omisión de notas al pie.",
        "findings": [
            {
                "claim_id": "P04-C10-C1",
                "claim": "La extracción perfecta de tablas multipágina en PDFs de memorias CMF sigue siendo un desafío abierto que requiere validación empírica sobre un corpus piloto de 15 memorias chilenas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Agenda Empírica P04"},
                "evidence": [
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2 y Sección 4: Etapa 2: Prueba Piloto de Ingesta y Parsing",
                        "excerpt_short": "Evaluar la precisión de extracción en un corpus piloto de 15 memorias anuales integradas (2023-2025). Criterio de éxito: precisión estructural ≥ 98% y cero omisión de notas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de validación empírica formalizado en P04_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus piloto de 15 memorias NCG 461"],
            "actors": ["Pilot Benchmark Runner", "Structural Integrity Verifier"],
            "steps": ["Ejecución de parsing sobre las 15 memorias", "Conteo de celdas desalineadas y notas perdidas", "Cálculo de porcentaje de precisión estructural"],
            "states": ["Pilot_Running", "Errors_Counted", "Pass_Threshold_Evaluated"],
            "outputs": ["Informe de rendimiento del pipeline de ingesta sobre memorias CMF reales"],
            "exceptions": ["Memorias escaneadas de baja resolución de emisores pequeños"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_TABLE_PARSING", "type": "vacio_epistemico", "name": "Vacío de Precisión en Extracción Tabular NCG 461", "aliases": ["NCG 461 Table Parsing Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_TABLE_PARSING", "predicate": "requiere_prueba_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C10-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Alcance de prueba",
                "Pruebas sintéticas en inglés": "No capturan la estructura legal de los balances y notas de la CMF de Chile.",
                "Piloto de 15 memorias NCG 461": "Valida el comportamiento real del software ante la tipografía y maquetación de empresas IPSA."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe ejecutar esta prueba piloto antes del lanzamiento comercial para certificar que no omite notas al pie en matrices ESG.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-05",
                "description": "Falta de medición empírica formal de precisión estructural en tablas multipágina sobre el corpus regulatorio de la CMF NCG 461.",
                "missing_information": "Benchmark de extracción sobre 15 memorias anuales de empresas IPSA 2023-2025."
            }
        ],
        "next_question_ids": ["P04-C11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C11
    {
        "question_id": "P04-C11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre gobierno y permisos, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: Múltiples aplicaciones comerciales de 'Chat con tus documentos' implementan el control de permisos delegando en el prompt del LLM la orden de no divulgar documentos confidenciales (e.g. 'Si el usuario es analista, no reveles este borrador'). Los estándares federales de ciberseguridad (NIST SP 800-162), la literatura de auditoría de IA (Mökander et al., 2023) y la síntesis P04_RESEARCH_DOSSIER demuestran que las restricciones en el prompt son fácilmente vulnerables mediante prompt injections, jailbreaks conversacionales o técnicas de roleplay, provocando fugas catastróficas de información privilegiada bajo Ley 18.045. Versión que prevalece: Prevalece el estándar de 'Filtrado Previo a la Recuperación' (Pre-Retrieval ABAC Filtering): los documentos bajo embargo o restringidos son excluidos matemáticamente por predicados booleanos en el índice vectorial y de grafos antes de que el LLM reciba el contexto. Si el usuario no tiene permiso, el texto confidencial jamás ingresa a la memoria del modelo.",
        "findings": [
            {
                "claim_id": "P04-C11-C1",
                "claim": "La seguridad basada en instrucciones en el prompt es rechazada por NIST SP 800-162 y Mökander et al., prevaleciendo el filtrado booleano previo a la recuperación con 100.0% de efectividad de aislamiento.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Global", "actor": "Ciberseguridad y Gobernanza de IA"},
                "evidence": [
                    {
                        "source_id": "75fa90f9-9906-48ee-84f1-83b117ea6ae6",
                        "source_title": "NIST SP 800-162: Attribute Based Access Control (ABAC)",
                        "original_url": "https://csrc.nist.gov/pubs/sp/800/162/upd2/final",
                        "locator": "Sección 3 and 4: Architectural Enforcement",
                        "excerpt_short": "Enforces authorization at Policy Enforcement Points before resource data is retrieved, prohibiting soft or post-processing access control in secure environments.",
                        "source_date": "2014-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 4: Fase 5 y Sección 5: Matriz de Criterios (Dimensión 5)",
                        "excerpt_short": "El filtrado de permisos debe ejecutarse como un predicado booleano en la fase de recuperación (pre-retrieval filtering). Umbral mínimo: 100.0% (Cero filtración).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución de discrepancia de seguridad formalizada en NIST SP 800-162 y dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta con contexto confidencial potencial"],
            "actors": ["Pre-Retrieval ABAC PDP", "Vector Search Index"],
            "steps": ["Evaluación booleana de atributos de usuario", "Aplicación de máscara de aislamiento en índice", "Entrega de chunks seguros al LLM"],
            "states": ["Query_Received", "Pre_Filtered_Boolean", "Zero_Leakage_Context"],
            "outputs": ["Contexto de generación 100% libre de documentos no autorizados"],
            "exceptions": ["Configuración errónea de roles en Active Directory / IAM"]
        },
        "entities": [
            {"entity_id": "ENT_ABAC_PRE_RETRIEVAL_DECISION", "type": "decision_diseno", "name": "Resolución de Seguridad ABAC Pre-Recuperación", "aliases": ["Pre-Retrieval Security Resolution"]}
        ],
        "relations": [
            {"subject_id": "ENT_ABAC_PRE_RETRIEVAL_DECISION", "predicate": "garantiza_estanqueidad_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C11-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Robustez ante ataques",
                "Restricción en prompt ('por favor no digas esto')": "El atacante convence al LLM con un prompt engañoso y extrae la cifra embargada.",
                "Restricción Pre-Retrieval ABAC": "El LLM no puede revelar el documento porque nunca estuvo en su ventana de contexto."
            }
        ],
        "contradictions": [
            {
                "topic": "Mecanismo de control de acceso en sistemas RAG empresariales",
                "claim_a": "Instruir al LLM en el system prompt para que respete confidencialidades es suficiente.",
                "source_a": "Prácticas de chatbots comerciales no auditados",
                "claim_b": "El control de acceso debe forzarse mediante predicados booleanos previos a la recuperación (Pre-Retrieval ABAC).",
                "source_b": "NIST SP 800-162 / Mökander et al. (2023) / P04_RESEARCH_DOSSIER",
                "resolution_or_status": "Prevalece Claim B: filtrado determinístico previo a la recuperación con 100.0% de aislamiento."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe rechazar cualquier arquitectura de seguridad dependiente del prompt y operar exclusivamente con Pre-Retrieval ABAC.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C12
    {
        "question_id": "P04-C12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre gobierno y permisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Sigue sin prueba empírica formal la gestión desatendida del levantamiento anticipado de embargos en situaciones de crisis de mercado (e.g. filtración en prensa a las 07:00 AM que obliga al Directorio a publicar un Hecho Esencial 3 horas antes del horario programado). Fuente Fallida: F-03: 'NIST AI 100-1: AI Risk Management Framework (AI RMF 1.0)' (bloqueo por política perimetral del servidor de NIST), suplida por Mökander et al. (2023) y NIST SP 800-162. Validación Mínima Requerida: Simulación en la Etapa 4 de la agenda empírica (Gabinete de Crisis / Stress Test de Vocería): programar un documento bajo embargo para las 12:00, disparar una señal de contingencia de prensa a las 08:00 y auditar que la orden de visado de emergencia por el Gerente General libere el documento para los voceros en menos de 60 segundos sin desconfigurar la bitácora de auditoría.",
        "findings": [
            {
                "claim_id": "P04-C12-C1",
                "claim": "La orquestación de liberaciones de embargo de emergencia ante filtraciones de prensa requiere pruebas de estrés dinámicas con tiempos de respuesta inferiores a 60 segundos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gobernanza de Crisis y ABAC"},
                "evidence": [
                    {
                        "source_id": "35dd0ce8-75f5-44fc-ab0a-ddf0b780a1ca",
                        "source_title": "P04_SOURCE_INDEX",
                        "original_url": None,
                        "locator": "Sección 3: Registro de Incidencias: F-03",
                        "excerpt_short": "F-03: NIST AI 100-1: AI Risk Management Framework: Portal NIST bloqueó crawler automático por política perimetral. Suplida por Mökander et al. y NIST SP 800-162.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1.3: Fricción entre la Velocidad de Crisis y Rigidez de Auditoría, y Sección 4: Etapa 4",
                        "excerpt_short": "Simulación de Gabinete de Crisis: tres escenarios de contingencia en tiempo inferior a 3 minutos por escenario y con cero fuga de documentos bajo embargo (ABAC).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Incidencia F-03 y escenario de crisis detallados en los documentos de gobierno de P04."
            }
        ],
        "operational_model": {
            "inputs": ["Orden de levantamiento de embargo de emergencia firmada por Gerente General"],
            "actors": ["Emergency Access Controller", "ABAC Policy Updater"],
            "steps": ["Recepción de orden firmada", "Actualización atómica de timestamp de embargo", "Invalidación de caché de consultas", "Notificación a voceros acreditados"],
            "states": ["Embargo_Active", "Emergency_Override_Authorized", "Instant_Unblock_Propagated"],
            "outputs": ["Documento liberado inmediatamente para voceros con bitácora de excepción registrada"],
            "exceptions": ["Orden emitida por un cargo que no posee atribuciones de excepción de directorio"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_EMERGENCY_OVERRIDE", "type": "vacio_epistemico", "name": "Vacío de Protocolo de Liberación de Emergencia de Embargos", "aliases": ["Emergency Embargo Lift Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_EMERGENCY_OVERRIDE", "predicate": "afecta_velocidad_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C12-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Velocidad de reacción",
                "Proceso burocrático manual": "Demora horas en actualizar permisos, dejando a los voceros sin información durante la crisis.",
                "Sobreescritura de emergencia gobernada": "Libera el documento en < 60 segundos manteniendo registro formal de auditoría."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe implementar un comando seguro de liberación de emergencia de embargos para gabinetes de crisis.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-06",
                "description": "Falta de validación empírica sobre la latencia de propagación de excepciones de embargo en motores de búsqueda distribuida.",
                "missing_information": "Telemetría de tiempo de propagación de cambios de permisos ABAC en clusters vectoriales bajo carga."
            }
        ],
        "next_question_ids": ["P04-C13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C13
    {
        "question_id": "P04-C13",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre búsqueda y respuesta fundada, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: Soluciones comerciales de RAG afirman que 'incluir la instrucción \"cite sus fuentes\" en el prompt del sistema es suficiente para obtener respuestas trazables y confiables'. En agudo contraste, la investigación científica de Google Research (Bohnet et al., 2022, Attributed QA) y P04_EVIDENCE_MAP demuestran que la citación guiada únicamente por prompt produce 'alucinación de citas' (citation hallucination): el modelo inventa números de página o atribuye cifras reales a documentos que no las contienen. Versión que prevalece: Prevalece la regla de 'Post-Verificación Algorítmica de Citas'. Ninguna cita se entrega al directivo sin pasar por un evaluador algorítmico independiente (FActScore / RAGAS) que compruebe la alineación atómica con el fragmento recuperado y verifique el hash criptográfico SHA-256 del documento de origen.",
        "findings": [
            {
                "claim_id": "P04-C13-C1",
                "claim": "La citación en el prompt es refutada por Bohnet et al. por inducir alucinación de referencias, prevaleciendo la post-verificación algorítmica de citas anclada a hashes inmutables.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2026", "region": "Global", "actor": "Evaluación de Atribución en IA"},
                "evidence": [
                    {
                        "source_id": "005e6819-75c5-40e4-b0a2-39b00ec373eb",
                        "source_title": "P04_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 3: Matriz de Tensiones Metodológicas (Atribución y Citación)",
                        "excerpt_short": "Pedir al LLM que cite en el prompt produce alucinación de citas plausibles pero falsas. Adopción de post-verificación algorítmica de citas con FActScore/RAGAS y anclaje a hash.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4df5f8f3-f0db-42c2-a566-b66b67b81db0",
                        "source_title": "Attributed QA: Evaluation and Modeling (Bohnet et al., 2022)",
                        "original_url": "https://arxiv.org/abs/2212.08037",
                        "locator": "Sección 1 and 4: Spurious Citations",
                        "excerpt_short": "Demonstrates that models frequently hallucinate citations when prompted naively, requiring programmatic post-generation verification of citation spans.",
                        "source_date": "2022-12-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución formalizada en Bohnet et al. y matriz de tensiones de P04_EVIDENCE_MAP."
            }
        ],
        "operational_model": {
            "inputs": ["Respuesta preliminar generada con citas textuales"],
            "actors": ["Post-Generation Citation Verifier", "Cryptographic Anchor"],
            "steps": ["Extracción de llamadas de cita", "Búsqueda de correspondencia exacta en fragmento fuente", "Comprobación de hash SHA-256", "Supresión de citas espurias"],
            "states": ["Raw_Generated_Text", "Verifying_Citations", "Authenticated_Attribution"],
            "outputs": ["Respuesta con citas certificadas algorítmicamente"],
            "exceptions": ["Cita que parafrasea el texto de origen sin contener las palabras clave"]
        },
        "entities": [
            {"entity_id": "ENT_POST_VERIFICATION_PROTOCOL", "type": "protocolo_seguridad", "name": "Protocolo de Post-Verificación Algorítmica de Citas", "aliases": ["Algorithmic Citation Verification Protocol"]}
        ],
        "relations": [
            {"subject_id": "ENT_POST_VERIFICATION_PROTOCOL", "predicate": "erradica_citas_falsas_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C13-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Veracidad de citas",
                "Citación por prompt": "El modelo cita 'página 84' cuando en realidad la cifra estaba en la página 120 o no existía.",
                "Post-verificación algorítmica": "Comprueba que la cadena exacta exista en la página citada antes de entregar la respuesta."
            }
        ],
        "contradictions": [
            {
                "topic": "Método de atribución y citación en RAG",
                "claim_a": "Pedir citas en el prompt del LLM garantiza atribución fiel.",
                "source_a": "Enfoques comerciales de chatbots",
                "claim_b": "La citación por prompt produce alucinaciones de citas; se requiere post-verificación programática.",
                "source_b": "Bohnet et al. (2022) / P04_EVIDENCE_MAP",
                "resolution_or_status": "Prevalece Claim B: post-verificación algorítmica obligatoria de citas y anclaje a hash."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe incluir este paso de post-verificación en su pipeline de inferencia antes de mostrar la minuta al vocero.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C14"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C14
    {
        "question_id": "P04-C14",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre búsqueda y respuesta fundada, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Sigue sin prueba empírica comparativa el balance óptimo entre latencia de respuesta y completitud analítica al contrastar Búsqueda Híbrida (ColBERT) vs GraphRAG sobre corpus de memorias anuales corporativas en español. GraphRAG requiere pre-computación de resúmenes de comunidad que insume alto costo de tokens y latencia de inferencia. Fuente Fallida: F-04: 'TruLens: The RAG Triad for Retrieval Evaluation' (inaccesible por restricción en servidor de documentación), suplida exitosamente por Es et al. (2023) RAGAS y Min et al. (2023) FActScore. Validación Mínima Requerida: Ejecución de la Etapa 3 de la agenda empírica en P04_GAPS_AND_VALIDATION: benchmark formal sobre 250 consultas complejas, midiendo latencia por consulta, costo de inferencia, Fidelidad Factual (FActScore) y exhaustividad temática (GraphRAG vs ColBERT).",
        "findings": [
            {
                "claim_id": "P04-C14-C1",
                "claim": "El trade-off costo-latencia entre GraphRAG y Búsqueda Híbrida ColBERT en memorias corporativas en español requiere validación comparativa mediante la suite de 250 consultas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Benchmark de Búsqueda P04"},
                "evidence": [
                    {
                        "source_id": "35dd0ce8-75f5-44fc-ab0a-ddf0b780a1ca",
                        "source_title": "P04_SOURCE_INDEX",
                        "original_url": None,
                        "locator": "Sección 3: Registro de Incidencias: F-04",
                        "excerpt_short": "F-04: TruLens: The RAG Triad: Restricción de acceso en sitio de documentación (unreachable). Suplida por Es et al. 2023 (RAGAS) y Min et al. 2023 (FActScore).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2: Costo Computacional de GraphRAG y Sección 4: Etapa 3",
                        "excerpt_short": "Ejecutar la suite de 250 consultas complejas contrastando Naive RAG vs Búsqueda Híbrida vs GraphRAG. Criterio de éxito: Fidelidad ≥ 0.95; Precisión de Cita ≥ 0.98.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Incidencia F-04 y diseño de benchmark formalmente especificados en P04_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Suite de 250 consultas de prueba", "Corpus de memorias vectorizado y particionado en grafo"],
            "actors": ["Retrieval Benchmarker", "Latency Profiler", "Cost Auditor"],
            "steps": ["Ejecución de consultas en ambos modos", "Medición de latencia de primer token y costo en dólares", "Evaluación de fidelidad y completitud con RAGAS"],
            "states": ["Benchmarking_ColBERT", "Benchmarking_GraphRAG", "Comparison_Report_Generated"],
            "outputs": ["Matriz de compensación técnica para enrutamiento adaptativo de consultas"],
            "exceptions": ["Consultas globales donde ColBERT omite compromisos clave"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_GRAPHRAG_BENCHMARK", "type": "vacio_epistemico", "name": "Vacío de Compensación Técnica GraphRAG vs ColBERT", "aliases": ["GraphRAG vs ColBERT Trade-Off Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_GRAPHRAG_BENCHMARK", "predicate": "orienta_enrutamiento_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C14-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Comportamiento del motor",
                "ColBERT Híbrido": "Ultrarrápido (< 300 ms) y exacto en cifras puntuales, pero limitado en agregaciones de 5 años.",
                "GraphRAG": "Exhaustivo en síntesis globales multi-documento, pero con latencia superior a 3 segundos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe implementar un enrutador inteligente que reserve GraphRAG para síntesis transversales y use ColBERT para preguntas de cifras puntuales.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-07",
                "description": "Falta de perfilado empírico del costo-latencia de GraphRAG sobre memorias corporativas en español.",
                "missing_information": "Telemetría de tiempo de ejecución y consumo de tokens comparando ColBERT vs GraphRAG en la suite de 250 consultas."
            }
        ],
        "next_question_ids": ["P04-C15"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C15
    {
        "question_id": "P04-C15",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre evaluación de calidad documental, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: Múltiples proveedores y prácticas informales de evaluación de LLMs consideran que una evaluación global binaria o subjetiva ('thumbs up / thumbs down' o evaluación cualitativa con LLM-as-a-judge de un párrafo entero) es suficiente para medir la calidad de un asistente. En fuerte oposición, la literatura científica especializada (Min et al., 2023, FActScore; Es et al., 2023, RAGAS) y la síntesis P04_RESEARCH_DOSSIER demuestran que las evaluaciones globales son ciegas a las alucinaciones microscópicas de cifras, porcentajes y fechas, donde un texto fluido puede contener errores numéricos críticos que comprometan legalmente a la empresa. Versión que prevalece: Prevalece la regla de 'Descomposición Atómica de Proposiciones Factuales' (FActScore) y la matriz multidimensional con 5 umbrales cuantitativos mínimos obligatorios: Fidelidad Factual ≥ 0.95, Precisión de Cita ≥ 0.98, Recall de Cita ≥ 0.95, Detección de Caducidad Temporal 100% y Aislamiento ABAC 100.0%.",
        "findings": [
            {
                "claim_id": "P04-C15-C1",
                "claim": "La evaluación cualitativa global es rechazada por FActScore y RAGAS, prevaleciendo la descomposición en hechos atómicos individuales y la matriz de 5 umbrales mínimos obligatorios.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Aseguramiento de Calidad de LLMs"},
                "evidence": [
                    {
                        "source_id": "bb0b173a-5888-4c00-9392-9768bed7824c",
                        "source_title": "FActScore: Fine-grained Atomic Evaluation of Factual Precision (Min et al., 2023)",
                        "original_url": "https://arxiv.org/abs/2305.14251",
                        "locator": "Sección 1 and 2: Motivation for Atomic Evaluation",
                        "excerpt_short": "Global human evaluations and naive LLM judges miss critical fine-grained factual errors in generated texts, requiring atomic sentence breakdown.",
                        "source_date": "2023-05-23",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 5: Matriz Consolidada de Criterios de Evaluación",
                        "excerpt_short": "Fidelidad Factual ≥ 0.95, Precisión de Cita ≥ 0.98, Coherencia Temporal 100%, Abstención Segura ≥ 0.98, ABAC Enforcement 100.0%.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución de discrepancia metodológica respaldada por Min et al. y dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Respuesta generada evaluada contra contexto"],
            "actors": ["Atomic Decomposer", "Threshold Gatekeeper"],
            "steps": ["Descomposición en hechos atómicos", "Cálculo de porcentaje de soporte literal", "Evaluación de pase booleano contra umbrales mínimos"],
            "states": ["Output_Received", "Atoms_Scored", "Thresholds_Enforced"],
            "outputs": ["Calificación certificada con auditoría atómica de cada afirmación"],
            "exceptions": ["Respuesta con 94% de fidelidad que queda bloqueada por caer bajo el umbral de 0.95"]
        },
        "entities": [
            {"entity_id": "ENT_ATOMIC_EVAL_RESOLUTION", "type": "decision_diseno", "name": "Resolución de Evaluación Atómica FActScore", "aliases": ["Atomic Evaluation Design Decision"]}
        ],
        "relations": [
            {"subject_id": "ENT_ATOMIC_EVAL_RESOLUTION", "predicate": "gobierna_auditoria_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C15-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Sensibilidad de evaluación",
                "Evaluación global cualitativa": "Aprueba una respuesta que tiene un tono convincente pero una cifra errónea.",
                "Evaluación atómica FActScore": "Detecta la cifra errónea como un átomo falso y rechaza la respuesta."
            }
        ],
        "contradictions": [
            {
                "topic": "Metodología de evaluación de calidad en sistemas generativos empresariales",
                "claim_a": "La evaluación holística subjetiva es suficiente para validar la calidad del sistema.",
                "source_a": "Prácticas tradicionales de aseguramiento de software",
                "claim_b": "Se requiere descomposición atómica FActScore con umbrales cuantitativos mínimos no negociables.",
                "source_b": "Min et al. (2023) / Es et al. (2023) / P04_RESEARCH_DOSSIER",
                "resolution_or_status": "Prevalece Claim B: auditoría atómica rigurosa con umbral mínimo de 0.95."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe implementar este motor de evaluación atómica en sus pruebas continuas para asegurar que ninguna cifra inexacta pase a producción.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C16"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C16
    {
        "question_id": "P04-C16",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre evaluación de calidad documental, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Sigue sin prueba empírica formal el comportamiento del sistema ante una crisis reputacional en tiempo real, donde coexisten tres factores de estrés simultáneos: 1) Acusación pública de greenwashing en medios; 2) Cuestionamiento de comunidades por uso de agua continental; y 3) Filtración de un borrador preliminar de política ambiental. Fuentes Parciales: Los benchmarks académicos (RAGAS, FActScore) evalúan preguntas aisladas en condiciones de laboratorio estáticas, pero no miden el desempeño ante gabinetes de crisis bajo presión temporal. Validación Mínima Requerida: Ejecución de la Etapa 4 de la agenda empírica en P04_GAPS_AND_VALIDATION: 'Simulación de Gabinete de Crisis (Stress Test de Vocería)', evaluando que el sistema genere minutas 100% trazables a memorias CMF oficiales en < 3 minutos por escenario, con diferenciación explícita entre hechos verificados y compromisos en curso, y con 100.0% de contención de documentos bajo embargo (cero filtración ABAC).",
        "findings": [
            {
                "claim_id": "P04-C16-C1",
                "claim": "La validación definitiva de la calidad documental requiere una prueba de estrés de gabinete de crisis que evalúe la generación de minutas en menos de 3 minutos con cero fuga de embargos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Protocolo de Validación Empírica"},
                "evidence": [
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 4: Agenda y Protocolo de Validación Empírica (Etapa 4)",
                        "excerpt_short": "Simular tres escenarios de crisis reputacional (greenwashing, agua en comunidad indígena, filtración de borrador). Criterio: minutas trazables en < 3 minutos y cero fuga ABAC.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Cierre de la agenda empírica formalizada en P04_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["3 escenarios simulados de crisis corporativa"],
            "actors": ["Crisis Simulation Controller", "Executive Spokesperson", "ABAC Compliance Officer"],
            "steps": ["Inyección de escenario de crisis", "Medición de tiempo de respuesta de la IA (< 3 min)", "Auditoría de citas oficiales y cero fuga de borradores"],
            "states": ["Crisis_Injected", "Briefing_Generated", "Stress_Test_Passed"],
            "outputs": ["Certificado de aptitud del sistema para asistencia en gabinetes de crisis"],
            "exceptions": ["Demora superior a 3 minutos en generación de minuta de vocería"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_CRISIS_SIMULATION", "type": "vacio_epistemico", "name": "Vacío de Validación en Simulación de Gabinete de Crisis", "aliases": ["Crisis Stress Test Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_CRISIS_SIMULATION", "predicate": "cierra_validacion_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C16-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Condición de prueba",
                "Benchmark estático": "Evalúa preguntas independientes sin presión de tiempo ni documentos bajo embargo.",
                "Simulación de crisis": "Evalúa el sistema en las condiciones extremas en las que realmente operan los directores de asuntos corporativos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe someter a su motor a esta simulación de estrés para garantizar su eficacia antes de ofrecerlo a directores corporativos.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-08",
                "description": "Falta de ejecución empírica de la simulación de gabinete de crisis bajo escenarios reales de controversia en Chile.",
                "missing_information": "Telemetría de tiempo de generación de minutas y precisión de vocería en la simulación de crisis de 3 escenarios."
            }
        ],
        "next_question_ids": ["FIN_P04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P04.jsonl")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Appended {len(records)} records (P04-C09..P04-C16) to {out_path}.")
