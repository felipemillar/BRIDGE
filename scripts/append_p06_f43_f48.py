import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-F43
    {
        "question_id": "P06-F43",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se integra el principio de Human-in-the-Loop en el flujo operativo del sistema para preservar la potestad y responsabilidad del criterio humano?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El principio de Human-in-the-Loop (HITL) se consagra en P06_RESEARCH_DOSSIER como la salvaguarda de gobernanza suprema del sistema: la inteligencia artificial actúa estrictamente como un analista copilloto de detección, estructuración y recomendación, pero la potestad decisoria final, la autorización de vocerías y la gestión de crisis permanece indelegablemente en manos de los líderes humanos de la corporación. En el flujo operativo, HITL se materializa mediante tres compuertas: 1) Compuerta de Validación de Discrepancias Críticas: Toda alerta calificada como 'Contradicción Real' se envía a una bandeja de entrada especializada ('Triage Directivo') con evidencias atómicas resaltadas, exigiendo la confirmación de un analista antes de elevar el estado de alarma de la compañía; 2) Compuerta de Redacción Asistida no Autónoma: El sistema nunca publica comunicados ni envía declaraciones a la prensa de manera desatendida; genera borradores de minutas, posturas estratégicas y matrices de preguntas y respuestas (Q&A) que deben ser editadas, visadas y firmadas por el Director de Asuntos Corporativos y el Gerente Legal; y 3) Auditoría de Retroalimentación Humana: Cada corrección que el operador humano introduce sobre una clasificación del sistema se almacena como retroalimentación supervisada para recalibrar los umbrales de los clasificadores NLI y Splink.",
        "findings": [
            {
                "claim_id": "P06-F43-C1",
                "claim": "La arquitectura Human-in-the-Loop prohíbe acciones públicas autónomas, reservando la decisión estratégica, vocería y validación de crisis exclusivamente a directivos humanos.",
                "epistemic_status": "principio_de_gobernanza_y_control",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Gobernanza de IA Corporativa"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Fase 6: Interfaz Corporativa y Bucle Humano (Human-in-the-Loop)",
                        "excerpt_short": "La discrepancia se presenta al equipo de Asuntos Corporativos con citas textuales bidireccionales, fragmentos probatorios y recomendaciones de acción, dejando siempre la decisión comunicacional final en manos humanas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio central de diseño especificado en el Dossier de investigación interna."
            }
        ],
        "operational_model": {
            "inputs": ["Alerta clasificada por el motor de inferencia"],
            "actors": ["Bandeja de Triage Directivo", "Director de Asuntos Corporativos", "Gerente Legal"],
            "steps": ["Presentación de evidencia bidireccional en dashboard", "Revisión humana de citas y contexto", "Aprobación, descarte o re-clasificación del hallazgo", "Liberación del borrador de respuesta para firma ejecutiva"],
            "states": ["Alert_Pending_Review", "Human_Review_Active", "Decision_Approved", "Action_Released"],
            "outputs": ["Autorización formal de vocería o archivo de la alerta"],
            "exceptions": ["Intentos de usuarios no autorizados de saltarse la compuerta humana para emitir declaraciones"]
        },
        "entities": [
            {"entity_id": "ENT_HITL_GOVERNANCE", "type": "modelo_de_gobernanza", "name": "Protocolo Human-in-the-Loop BRIDGE", "aliases": ["HITL Protocol", "Human Oversight"]}
        ],
        "relations": [
            {"subject_id": "ENT_HITL_GOVERNANCE", "predicate": "garantiza_control_humano_sobre", "object_id": "ENT_ACTUAR_MODULE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F43-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de autonomía de la IA",
                "Automatización desatendida riesgosa": "La IA detecta una contradicción y publica automáticamente un desmentido en redes sociales, con alto riesgo de error catastrófico.",
                "Arquitectura HITL BRIDGE": "La IA prepara el análisis y el borrador de postura; el Director de Asuntos Corporativos decide y autoriza la acción."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Bucle Humano Human-in-the-Loop", "implication": "BRIDGE debe implementar compuertas de firma y autorización humana obligatorias antes de que cualquier sugerencia de vocería salga del sistema.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F44"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F44
    {
        "question_id": "P06-F44",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo debe diseñarse el Dashboard de Asuntos Corporativos y el semáforo de riesgo reputacional para permitir trazabilidad bidireccional inmediata?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El Dashboard de Asuntos Corporativos debe diseñarse como una consola de control visual y ejecutiva estructurada en tres paneles interconectados que garantizan una trazabilidad bidireccional en menos de 5 segundos: 1) Panel del Semáforo de Riesgo Reputacional: Codifica visualmente las discrepancias activas mediante un semáforo de cuatro colores calibrado: Rojo (Contradicción Real con evidencia regulatoria; riesgo crítico), Naranja (Diferencia de Alcance o pasivo contingente en escalamiento; riesgo alto), Amarillo (Diferencia Temporal o Acusación No Verificada en redes; riesgo medio), y Verde (Consistencia fáctica comprobada / Entailment); 2) Panel Central de la Matriz Afirmación-Evidencia: Despliega la tabla interactiva de 12 campos con capacidades de ordenamiento por severidad, fecha y filial; y 3) Panel Lateral de Inspección y Trazabilidad Bidireccional (Deep-Dive Inspector): Al hacer clic en cualquier alerta, la pantalla se divide mostrando en paralelo: a la izquierda, el documento interno original (PDF de la memoria CMF resaltando la página y el párrafo exacto mediante su hash criptográfico); y a la derecha, la señal externa (enlace navegable a la resolución de la SMA o al artículo de prensa). Esta disposición erradica la ambigüedad y permite a un director comprobar con sus propios ojos la validez del cruce antes de tomar decisiones.",
        "findings": [
            {
                "claim_id": "P06-F44-C1",
                "claim": "El Dashboard de Asuntos Corporativos integra un semáforo de 4 colores y un panel de inspección paralelo con trazabilidad bidireccional inmediata entre memoria y noticia.",
                "epistemic_status": "diseno_de_interfaz_y_ux",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Diseño de Producto BRIDGE"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3: Fase 6: Dashboard de Asuntos Corporativos y Semáforo de Riesgo",
                        "excerpt_short": "Dashboard de Asuntos Corporativos, Semáforo de Riesgo Reputacional, Bandeja de verificación y sugerencia de vocería/Q&A... 100% de las alertas generadas deben incluir enlaces directos navegables a la página/párrafo del documento interno y a la URL de la señal externa.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación de diseño de producto y UX establecida en el Dossier de investigación."
            }
        ],
        "operational_model": {
            "inputs": ["Eventos cruzados con clasificación y evidencias"],
            "actors": ["Interfaz Gráfica BRIDGE", "Director de Asuntos Corporativos"],
            "steps": ["Cálculo del nivel de riesgo y color del semáforo", "Despliegue de tarjetas de alerta priorizadas", "Apertura de vista paralela (Split Screen) ante clic en alerta", "Acceso directo a la página original del PDF interno y URL externa"],
            "states": ["Overview_Dashboard", "Alert_Selected", "Split_Screen_Inspector_Open", "Fact_Checked_by_User"],
            "outputs": ["Inspección visual inmediata de consistencia documental"],
            "exceptions": ["Enlaces externos caídos o tras paywalls que exigen mostrar el snapshot archivado en base de datos"]
        },
        "entities": [
            {"entity_id": "ENT_CORPORATE_DASHBOARD", "type": "interfaz_de_usuario", "name": "Dashboard de Asuntos Corporativos BRIDGE", "aliases": ["BRIDGE Executive Dashboard", "Reputation Cockpit"]}
        ],
        "relations": [
            {"subject_id": "ENT_CORPORATE_DASHBOARD", "predicate": "despliega_visualmente", "object_id": "ENT_CLAIM_EVIDENCE_MATRIX", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F44-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Experiencia de auditoría",
                "Reportes estáticos en PDF": "El director lee una afirmación pero debe buscar manualmente en un anexo de 400 páginas si es verdad.",
                "Dashboard interactivo BRIDGE": "Clic en la alerta y la pantalla salta automáticamente al párrafo exacto de la memoria y a la resolución regulatoria correspondiente."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Tiempo de verificación visual de la discrepancia", "denominator": "Latencia de apertura de vista paralela", "formula": "< 5 segundos para desplegar la evidencia bidireccional"}
        ],
        "bridge_implications": [
            {"module": "Frontend y UX del Dashboard", "implication": "BRIDGE debe construir su UI con vista dividida obligatoria: documento interno a la izquierda y fuente externa a la derecha para auditoría instantánea.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F45"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F45
    {
        "question_id": "P06-F45",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se conectan los compromisos públicos obligatorios de la Norma de Carácter General N° 461 de la CMF con el Sistema SNIFA de la SMA y la Circular de Greenwashing del SERNAC?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "En el contexto regulatorio chileno, las Memorias Integradas bajo la NCG 461 de la CMF, el catastro SNIFA de la SMA y la Circular Interpretativa de Sostenibilidad del SERNAC forman un triángulo de exigibilidad jurídica y reputacional directo: 1) Repositorio Formal de Afirmaciones (CMF NCG 461): Obliga a los emisores de valores a reportar con fe pública sus políticas de sostenibilidad, métricas de gobernanza, riesgos climáticos y cumplimiento ambiental; 2) Verdad Probatoria Ambiental (SNIFA - SMA): El Registro Público de Fiscalización y Sanciones de la SMA contiene actos administrativos vinculantes (formulaciones de cargos, planes de cumplimiento, multas). Si una empresa declara en su memoria bajo NCG 461 que 'el 100% de sus plantas operan bajo estricto cumplimiento ambiental' pero el SNIFA publica un proceso sancionatorio grave por vertimiento tóxico, se configura de inmediato una 'Contradicción Real'; y 3) Fiscalización de Publicidad y Engaño al Consumidor (SERNAC): La Circular de Diciembre de 2024 del SERNAC sanciona severamente el greenwashing en publicidad masiva, prohibiendo aseveraciones ambientales absolutas ('100% ecológico', 'cero emisiones') que no cuenten con certificación previa verificable. Si el SERNAC detecta que las afirmaciones publicitarias no cuadran con los datos técnicos reportados a la CMF o infringen resoluciones de la SMA, incoa procedimientos sancionatorios directos bajo la Ley 19.496.",
        "findings": [
            {
                "claim_id": "P06-F45-C1",
                "claim": "En Chile, la Memoria CMF NCG 461, las sanciones ambientales del SNIFA de la SMA y la Circular de Greenwashing del SERNAC configuran un triángulo de exigibilidad factual directo.",
                "epistemic_status": "marco_regulatorio_vigente",
                "scope": {"time": "2021-2026", "region": "Chile", "actor": "CMF, SMA y SERNAC"},
                "evidence": [
                    {
                        "source_id": "589b1b7c-6049-4b3a-9f0d-1fa8990a7a1d",
                        "source_title": "CMF Chile - Sostenibilidad y Norma de Carácter General N° 461",
                        "original_url": "https://www.cmfchile.cl/portal/principal/623/w4-propertyvalue-50301.html",
                        "locator": "Sección 1: Objetivos y Ámbito de Aplicación de la NCG 461",
                        "excerpt_short": "Requiere la incorporación de información ESG y riesgos climáticos en las memorias anuales de los emisores de valores para transparentar la gestión ante el mercado.",
                        "source_date": "2021-11-12",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7ffaecea-0ea0-4037-8ae3-e09f34ab29f0",
                        "source_title": "SMA Chile - SNIFA: Registro Público de Fiscalización y Sanciones",
                        "original_url": "https://snifa.sma.gob.cl/RegistroPublico",
                        "locator": "Portal de Fiscalización y Catastro Sancionatorio",
                        "excerpt_short": "Plataforma pública que reúne las denuncias, inspecciones, resoluciones de sanción y planes de cumplimiento de las unidades fiscalizables en Chile.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "33d0f555-7934-4af8-913b-89920a2514ac",
                        "source_title": "SERNAC Chile - Circular sobre Consumo Sostenible y Greenwashing",
                        "original_url": "https://www.sernac.cl/604/w3-article-83768.html",
                        "locator": "Criterios de Fiscalización de Aseveraciones Ambientales",
                        "excerpt_short": "Fija las directrices interpretativas para sancionar la publicidad engañosa y afirmaciones de sustentabilidad no comprobables bajo la Ley N° 19.496 de Protección al Consumidor.",
                        "source_date": "2024-12-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal vigente y plenamente exigible en Chile descrita en las síntesis internas."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria NCG 461 reportada a la CMF", "Resoluciones publicadas en SNIFA", "Campañas publicitarias monitoreadas por SERNAC"],
            "actors": ["Conector Regulatorio CMF", "Scraper Oficial SNIFA", "Fiscalizador SERNAC", "Motor BRIDGE"],
            "steps": ["Cruce continuo de afirmaciones ambientales de la memoria contra cargos de la SMA", "Evaluación de concordancia entre publicidad comercial y datos oficiales de la CMF", "Detección de incongruencias y emisión de alerta regulatoria"],
            "states": ["Reports_Filed", "Sanctions_Scraped", "Triangle_Crossed", "Regulatory_Risk_Evaluated"],
            "outputs": ["Reporte de consistencia regulatoria CMF-SMA-SERNAC"],
            "exceptions": ["Controversias sobre interpretación técnica de normas que están siendo dirimidas en Tribunales Ambientales"]
        },
        "entities": [
            {"entity_id": "ENT_REGULATORY_TRIANGLE_CHILE", "type": "marco_regulatorio", "name": "Triángulo Regulatorio de Sustentabilidad en Chile", "aliases": ["CMF-SMA-SERNAC Triangle"]}
        ],
        "relations": [
            {"subject_id": "ENT_REGULATORY_TRIANGLE_CHILE", "predicate": "fiscaliza_integralmente_a", "object_id": "ENT_HOLDING_CHILE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F45-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Exigibilidad jurídica de fuentes",
                "Green Claims Directive UE": "Propuesta legislativa en trámite parlamentario, sin vigencia vinculante inmediata.",
                "Triángulo CMF-SMA-SERNAC Chile": "Normativa plenamente vigente, con resoluciones sancionatorias activas y fiscalización en ejecución."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Conector Regulatorio Chileno", "implication": "BRIDGE debe integrar conectores automáticos diarios a SNIFA (SMA) y el repositorio CMF para auditar la consistencia legal de sus clientes IPSA.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F46"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F46
    {
        "question_id": "P06-F46",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué protocolos de pruebas adversariales (red-teaming) deben ejecutarse para auditar la resistencia del sistema ante fake news, desinformación y trampas de ambigüedad?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Para certificar la robustez del sistema y garantizar que no colapse ante manipulaciones o ruido externo, P06_RESEARCH_DOSSIER formaliza un protocolo de pruebas adversariales (Red-Teaming) compuesto por tres baterías de test obligatorias: 1) Caso de Prueba 1: Inyección de Fake News y Desinformación Sintética: Se inyectan en el feed externo artículos fabricados o publicaciones virales ficticias en redes que imputan derrames tóxicos o fraudes a la corporación. Criterio de éxito: El sistema debe resistir la tentación de declarar una 'Contradicción Real', clasificar la señal obligatoriamente como 'Acusación No Verificada', emitir una advertencia de falta de sustento probatorio y abstenerse de generar respuestas públicas; 2) Caso de Prueba 2: Trampa de Desfase Temporal (Temporal Lag Trap): Se confronta intencionalmente una memoria corporativa legítima de enero de 2024 con una noticia real de un incidente ocurrido en diciembre de 2025. Criterio de éxito: El motor T-GRAG debe detectar el desalineamiento cronológico y clasificar el evento como 'Diferencia Temporal', sin acusar falsedad retrospectiva; y 3) Caso de Prueba 3: Trampa de Ambigüedad de Filial (Subsidiary Ambiguity Trap): Se confronta una meta ambiental de la matriz en Chile con una noticia sobre una filial autónoma en el extranjero. Criterio de éxito: Splink y el grafo societario deben delimitar la personería jurídica y clasificar la brecha como 'Diferencia de Alcance'.",
        "findings": [
            {
                "claim_id": "P06-F46-C1",
                "claim": "El protocolo de red-teaming audita la resiliencia del sistema ante inyecciones de fake news, trampas de desfase temporal y ambigüedad societaria.",
                "epistemic_status": "protocolo_de_seguridad_adversarial",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Red-Teaming y Seguridad de IA"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 4: Entregable Específico 3: Protocolo de Pruebas Adversariales (Red-Teaming)",
                        "excerpt_short": "Caso 1: Fake News o Desinformación en Redes (clasificar como Acusación No Verificada y abstenerse). Caso 2: Trampa de Desfase Temporal (marcar Diferencia Temporal). Caso 3: Trampa de Ambigüedad de Filial (detectar divergencia de alcance territorial vía Splink).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Batería de pruebas formalizada y documentada en el Dossier de investigación."
            }
        ],
        "operational_model": {
            "inputs": ["Suite de 500 prompts y documentos sintéticos adversariales"],
            "actors": ["Equipo Rojo de Evaluación (Red-Team)", "Pipeline BRIDGE", "Auditor de Seguridad"],
            "steps": ["Inyección controlada de casos de prueba adversariales en entorno de staging", "Medición de respuestas de clasificación y abstención", "Cálculo de tasa de éxito de contención", "Ajuste de pesos y reglas si alguna trampa penetra el guardrail"],
            "states": ["Test_Suite_Ready", "Attacks_Injected", "Defenses_Evaluated", "Certification_Passed"],
            "outputs": ["Reporte de auditoría de resistencia adversarial de BRIDGE"],
            "exceptions": ["Ataques híbridos multimodal con imágenes falsificadas mediante deepfake"]
        },
        "entities": [
            {"entity_id": "ENT_RED_TEAMING_PROTOCOL", "type": "metodologia_de_seguridad", "name": "Protocolo de Pruebas Adversariales BRIDGE", "aliases": ["BRIDGE Red-Teaming Suite"]}
        ],
        "relations": [
            {"subject_id": "ENT_RED_TEAMING_PROTOCOL", "predicate": "certifica_resistencia_de", "object_id": "ENT_CROSS_PIPELINE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F46-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resistencia a manipulación",
                "RAG sin defensas": "Cae en la trampa de fake news, emitiendo declaraciones defensivas sobre hechos que nunca ocurrieron.",
                "BRIDGE con Red-Teaming certificado": "Aísla la acusación no probada, detecta el desfase temporal y protege la integridad del Directorio."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Tasa de contención de inyecciones adversariales", "denominator": "Total de ataques sintéticos evaluados", "formula": "Tasa de contención exitosa >= 98.0%"}
        ],
        "bridge_implications": [
            {"module": "Suite de Seguridad y Red-Teaming", "implication": "BRIDGE debe ejecutar periódicamente la batería de 3 pruebas adversariales antes de desplegar cualquier actualización en clientes productivos.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F47"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F47
    {
        "question_id": "P06-F47",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cuáles son las métricas operacionales clave de asuntos corporativos (MTTD < 15 min, tasa de falsos positivos < 8%, 100% auditabilidad) para medir el éxito del sistema?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El éxito de BRIDGE no se mide únicamente por métricas algorítmicas de inteligencia artificial (F1 o perplexity), sino por su impacto directo en la resiliencia y velocidad de respuesta de la gerencia corporativa. P06_RESEARCH_DOSSIER formaliza tres Métricas de Nivel de Servicio (SLA) operacionales obligatorias: 1) Tiempo Medio de Detección de Brecha (MTTD - Mean Time to Detect): El tiempo transcurrido desde que una señal externa crítica se publica en newswires, el Diario Oficial o el SNIFA hasta que el sistema la mapea contra la memoria interna y alerta al equipo directivo debe ser inferior a 15 minutos (MTTD < 15 min), frente a las 24-48 horas de los procesos de clipping manual; 2) Tasa Máxima de Falsos Positivos en Alertas de Crisis: El porcentaje de alertas catalogadas erróneamente como 'Contradicción Real' que tras revisión humana resultan ser meros desajustes temporales o de alcance debe ser inferior al 8% (FPR < 8%), evitando la fatiga de alertas que induce a los ejecutivos a ignorar el sistema; y 3) Auditabilidad y Trazabilidad al 100%: Cada veredicto emitido debe incluir enlaces directos navegables a la página/párrafo del documento interno auditado y a la URL/expediente de la señal externa, con cero tolerancia a dictámenes opacos.",
        "findings": [
            {
                "claim_id": "P06-F47-C1",
                "claim": "El desempeño operacional exige un MTTD < 15 minutos, tasa de falsos positivos < 8% y 100% de auditabilidad y trazabilidad documental obligatoria.",
                "epistemic_status": "sla_operacional_y_kpi",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Gestión Corporativa de Alto Nivel"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 4: Entregable Específico 3: Métricas Operacionales de Asuntos Corporativos",
                        "excerpt_short": "Tiempo Medio de Detección de Brecha (MTTD): Meta < 15 minutos para señales críticas. Tasa de Falsos Positivos en Alertas de Crisis: Meta < 8%. Auditabilidad y Trazabilidad: 100% de las alertas generadas deben incluir enlaces directos navegables.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "KPIs operacionales unívocamente definidos y cuantificados en el Dossier de investigación."
            }
        ],
        "operational_model": {
            "inputs": ["Telemetría de alertas emitidas y retroalimentación de analistas humanos"],
            "actors": ["Monitor de SLAs", "Comité de Gestión de Riesgo", "Agente BRIDGE"],
            "steps": ["Registro de timestamps de publicación externa y emisión de alerta", "Medición de MTTD", "Contabilización de reclasificaciones humanas para calcular tasa de falsos positivos", "Auditoría de presencia de enlaces documentales"],
            "states": ["Alerts_Tracked", "KPIs_Computed", "SLAs_Audited", "Monthly_Report_Generated"],
            "outputs": ["Reporte mensual de cumplimiento de SLAs de inteligencia de riesgos"],
            "exceptions": ["Caídas generales de redes externas de telecomunicaciones que impidan capturar el feed dentro de los 15 minutos"]
        },
        "entities": [
            {"entity_id": "ENT_OPERATIONAL_SLAS", "type": "indicadores_clave", "name": "Métricas Operacionales SLA de BRIDGE", "aliases": ["MTTD", "False Positive Rate", "100% Auditability"]}
        ],
        "relations": [
            {"subject_id": "ENT_OPERATIONAL_SLAS", "predicate": "mide_desempeno_de", "object_id": "ENT_BRIDGE_PLATFORM", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F47-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Velocidad de alerta",
                "Monitoreo humano tradicional": "El clipping matutino se entrega a las 08:30 AM del día siguiente (MTTD de 12 a 24 horas).",
                "BRIDGE Intelligence": "Detección, cruce y alerta contextualizada en menos de 15 minutos desde la publicación del boletín regulatorio."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "MTTD (Mean Time to Detect)", "denominator": "Minutos transcurridos desde emisión externa hasta alerta", "formula": "MTTD < 15 minutos"},
            {"metric": "Tasa Máxima de Falsos Positivos", "denominator": "Alertas erróneas sobre alertas críticas emitidas", "formula": "FPR < 8%"}
        ],
        "bridge_implications": [
            {"module": "Tablero de Control de SLAs", "implication": "BRIDGE debe monitorear continuamente su propio MTTD y tasa de falsos positivos, alertando si el sistema sobrepasa el 8% de error.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F48"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F48
    {
        "question_id": "P06-F48",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿En qué consiste el protocolo de validación empírica en 3 fases (backtesting histórico de 10 casos en Chile, 12 entrevistas con directores de empresas IPSA, y shadow running de 60 días)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Para certificar la validez empírica, utilidad real y viabilidad operacional de BRIDGE en el mercado chileno y latinoamericano, P06_GAPS_AND_VALIDATION establece un protocolo de validación en tres fases secuenciales: 1) Fase 1: Validación Retrospectiva con Casos Históricos Chilenos (Backtesting): Se seleccionan 10 casos históricos documentados de controversias corporativas en Chile (2018–2025) que involucraron memorias CMF, fiscalizaciones de la SMA (SNIFA) y reclamos SERNAC. Se procesan los documentos internos previos a la crisis y las señales del entorno de la época a través del pipeline propuesto para medir si el sistema habría detectado la brecha con antelación y si la clasificación de tipología habría sido acertada; 2) Fase 2: Entrevistas Estructuradas con 12 Directores de Asuntos Corporativos y Riesgo: Se ejecutan entrevistas en profundidad con líderes de reputación de empresas del índice IPSA y consultoras de comunicación estratégica, evaluando la aceptabilidad de la interfaz Human-in-the-Loop, la tolerancia a falsos positivos y los requerimientos de gobernanza y confidencialidad; y 3) Fase 3: Piloto Operacional Controlado (Shadow Running de 60 días): Despliegue en modo paralelo y silencioso durante dos meses en una corporación regulada, procesando sus reportes NCG 461 contra el flujo diario de noticias y resoluciones oficiales, midiendo la reducción en los tiempos de preparación de vocerías y la satisfacción directiva.",
        "findings": [
            {
                "claim_id": "P06-F48-C1",
                "claim": "El protocolo de validación empírica de 3 fases comprende backtesting retrospectivo de 10 casos chilenos, 12 entrevistas a directores IPSA y un shadow running de 60 días en entorno real.",
                "epistemic_status": "protocolo_de_validacion_de_campo",
                "scope": {"time": "2026-2027", "region": "Chile", "actor": "Validación de Producto BRIDGE"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 4: Protocolo de Validación Empírica en Terreno (Chile y Latinoamérica)",
                        "excerpt_short": "Fase 1: Validación Retrospectiva con Casos Históricos Chilenos (10 casos 2018–2025). Fase 2: Entrevistas Estructuradas con Directores de Asuntos Corporativos (12 entrevistas empresas IPSA). Fase 3: Piloto Operacional Controlado (Shadow Running durante 60 días).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Roadmap empírico formalizado y detallado en P06_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Casos históricos documentados 2018-2025", "Directores corporativos participantes en piloto"],
            "actors": ["Equipo de Investigación BRIDGE", "Directores de Asuntos Corporativos IPSA", "Auditor Externo"],
            "steps": ["Ejecución de backtesting sobre los 10 casos históricos", "Análisis cualitativo y cuantitativo en 12 entrevistas estructuradas", "Instalación de shadow running durante 60 días", "Consolidación de métricas de utilidad y tiempos de respuesta"],
            "states": ["Backtesting_Active", "Interviews_Completed", "Shadow_Running_60d", "Empirical_Validation_Certified"],
            "outputs": ["Informe de Certificación Empírica de BRIDGE en Terreno"],
            "exceptions": ["Resistencia de gerencias legales a participar en pilotos por temor a hallazgos de inconsistencia interna"]
        },
        "entities": [
            {"entity_id": "ENT_VALIDATION_ROADMAP", "type": "plan_de_validacion", "name": "Protocolo de Validación Empírica en 3 Fases BRIDGE", "aliases": ["3-Phase Empirical Protocol"]}
        ],
        "relations": [
            {"subject_id": "ENT_VALIDATION_ROADMAP", "predicate": "valida_viabilidad_de", "object_id": "ENT_BRIDGE_PLATFORM", "valid_from": "2026", "valid_to": "2027", "evidence_claim_id": "P06-F48-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Rigor de validación",
                "Prueba de concepto de laboratorio": "Evalúa métricas sobre textos sintéticos en inglés; no garantiza viabilidad en el mercado local.",
                "Protocolo empírico BRIDGE": "Backtesting con crisis reales chilenas, entrevistas con ejecutivos IPSA y shadow running de 60 días en operación real."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Casos de backtesting histórico en Chile", "denominator": "Casos de controversia analizados", "formula": "10 casos emblemáticos 2018-2025"},
            {"metric": "Duración del piloto en modo shadow running", "denominator": "Días de operación paralela", "formula": "60 días continuos"}
        ],
        "bridge_implications": [
            {"module": "Hoja de Ruta y Roadmap de Producto", "implication": "BRIDGE debe ejecutar estrictamente las 3 fases del protocolo de validación empírica para certificar su preparación para el mercado (Production Readiness).", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C01"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-F43..F48) to {out_path}.")
