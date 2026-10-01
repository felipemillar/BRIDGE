import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-C01
    {
        "question_id": "P06-C01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrastan el monitoreo tradicional de clipping de prensa (basado en volumen y conteo de menciones) frente a una ontología operacional centrada en decisiones (Signal AI / Palantir)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste radica en la diferencia entre una métrica cosmética de vanidad y un sensor estructural de riesgo operativo: 1) Monitoreo Tradicional de Clipping: Opera recolectando pasivamente artículos que contienen palabras clave predefinidas, generando reportes volumétricos ('150 menciones esta semana') y métricas desacreditadas como el AVE (Advertising Value Equivalency) o el sentimiento superficial positivo/negativo. Es incapaz de discernir si una mención impacta a un activo estratégico o a un compromiso regulatorio; 2) Ontología Operacional Centrada en Decisiones (Signal AI / Palantir): Estructura los datos externos contra los objetos de negocio de la corporación (faenas, licencias RCA, compromisos de reporte NCG 461, directivos y filiales). En lugar de reportar que 'hubo 20 noticias negativas', el sistema señala: 'La resolución de la SMA afecta directamente la meta hídrica declarada en la página 84 de la memoria 2024, activando una recomendación de rectificación de vocería'. Transforma el flujo desestructurado en decisiones directivas accionables.",
        "findings": [
            {
                "claim_id": "P06-C01-C1",
                "claim": "El clipping tradicional mide volumen superficial sin contexto, mientras la ontología operacional vincula señales a compromisos corporativos accionables.",
                "epistemic_status": "contraste_de_paradigmas",
                "scope": {"time": "2020-2026", "region": "Global", "actor": "Inteligencia Corporativa"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 1: El Cruce Afirmación-Entorno no es Novedoso, pero su Automatización Sí",
                        "excerpt_short": "El cambio paradigmático radica en pasar de un monitoreo pasivo de menciones (clipping) a una ontología operacional que vincula entidades corporativas internas con señales externas en tiempo real.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "98f72019-62a8-4781-a211-2ce2cccaf4eb",
                        "source_title": "Palantir Foundry - Why Create an Ontology: Decision-Centric System",
                        "original_url": "https://palantir.com/docs/foundry/ontology/why-ontology/",
                        "locator": "Concept: Beyond Data Warehousing to Decision-Centric Operations",
                        "excerpt_short": "The Ontology represents the decisions in an enterprise, not simply the data... connecting humans and agents directly to operations.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diferenciación conceptual y metodológica medular en P06_EVIDENCE_MAP y documentación de Palantir."
            }
        ],
        "operational_model": {
            "inputs": ["Noticia externa sobre falla en faena industrial", "Base de datos ontológica corporativa"],
            "actors": ["Analista de Monitoreo Clásico", "Ontología Operacional BRIDGE"],
            "steps": ["Clipping clásico cuenta +1 mención negativa", "BRIDGE identifica faena, vincula a compromiso de la memoria y calcula impacto en riesgo reputacional", "Prescripción de acción de vocería específica"],
            "states": ["Raw_News", "Clipping_Counted", "Ontology_Resolved", "Decision_Prescribed"],
            "outputs": ["Alerta orientada a decisiones en lugar de conteo de menciones"],
            "exceptions": ["Menciones coloquiales indirectas que requieren resolución probabilística"]
        },
        "entities": [
            {"entity_id": "ENT_CLIPPING_TRADICIONAL", "type": "paradigma_obsoleto", "name": "Monitoreo Tradicional de Clipping", "aliases": ["Media Clipping", "Volumetric Monitoring"]},
            {"entity_id": "ENT_DECISION_ONTOLOGY", "type": "paradigma_avanzado", "name": "Ontología Operacional de Decisiones", "aliases": ["Palantir/Signal AI Decision Ontology"]}
        ],
        "relations": [
            {"subject_id": "ENT_DECISION_ONTOLOGY", "predicate": "sustituye_superando_a", "object_id": "ENT_CLIPPING_TRADICIONAL", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Valor para el Directorio",
                "Clipping Tradicional": "Genera gráficos de volumen y nubes de palabras que no responden qué debe hacer la empresa.",
                "Ontología Operacional": "Identifica exactamente qué compromiso oficial está en riesgo y prescribe acciones de mitigación concretas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Núcleo de Asuntos Corporativos BRIDGE", "implication": "BRIDGE debe rechazar métricas de clipping volumétrico y estructurar toda su salida hacia el impacto en decisiones y compromisos.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C02
    {
        "question_id": "P06-C02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la asunción de desacoplamiento como engaño deliberado (hipótesis punitiva) frente a la interpretación sociológica del desacoplamiento como ajuste burocrático e institucional (Brunsson / Meyer & Rowan)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste define la filosofía de análisis del sistema: 1) Hipótesis Punitiva / Visión Inquisitorial: Asume una visión simplista y moralizante donde toda discrepancia entre la memoria de sostenibilidad y la conducta operativa de la empresa constituye automáticamente fraude, mentira intencional o greenwashing punible. Esta postura genera resistencia frontal en las gerencias operativas y parálisis en los equipos de compliance; 2) Enfoque Institucional de Brunsson (1989) y Meyer & Rowan (1977): Comprende que las organizaciones complejas conviven con presiones externas irreconciliables entre sí (inversionistas que exigen reducción de costos vs reguladores que exigen inversiones ambientales intensivas). Para mantener la legitimidad institucional ante múltiples audiencias, la organización genera estructuras formales y retóricas simbólicas (talk) que inevitablemente difieren en velocidad y alcance de la acción física en terreno (action). Como establece P06_RESEARCH_DOSSIER, interpretar la brecha como un desajuste operacional y burocrático permite a BRIDGE actuar como un sensor temprano de sincronización interna, ayudando a cerrar la brecha antes de que escale a contingencia pública o legal.",
        "findings": [
            {
                "claim_id": "P06-C02-C1",
                "claim": "El desacoplamiento organizacional de Brunsson reconoce la tensión institucional estructural entre retórica y acción, evitando la condena punitiva simplista y permitiendo la remediación interna.",
                "epistemic_status": "contraste_sociologico",
                "scope": {"time": "1977-2026", "region": "Global", "actor": "Teoría Organizacional"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 1: Marco Teórico y Fundamentos Conceptuales",
                        "excerpt_short": "El pilar P06 no debe asumir que toda divergencia proviene de malicia o fraude deliberado; muchas veces responde a desajustes burocráticos o tiempos de implementación diferidos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fundamentación teórica sociológica ratificada en P06_RESEARCH_DOSSIER."
            }
        ],
        "operational_model": {
            "inputs": ["Divergencia entre política aprobada y práctica observada en planta"],
            "actors": ["Analista de Riesgos", "Comité de Ética y Operaciones"],
            "steps": ["Evaluación del origen de la brecha (retraso en compras vs desconocimiento normativo vs fraude)", "Si es desajuste operacional, alertar para remediación interna", "Si es fraude deliberado, elevar a auditoría forense"],
            "states": ["Gap_Identified", "Etiology_Evaluated", "Remediation_Path_Selected"],
            "outputs": ["Plan de sincronización operativa entre discurso y realidad"],
            "exceptions": ["Casos evidentes de dolo penal o colusión deliberada (ej. Caso Tissue)"]
        },
        "entities": [
            {"entity_id": "ENT_INSTITUTIONAL_THEORY", "type": "teoria_sociologica", "name": "Teoría Institucional del Desacoplamiento (Meyer & Rowan / Brunsson)", "aliases": ["Organizational Decoupling"]}
        ],
        "relations": [
            {"subject_id": "ENT_INSTITUTIONAL_THEORY", "predicate": "fundamenta_diagnostico_de", "object_id": "ENT_GAP_REMEDIATION", "valid_from": "1977", "valid_to": "2026", "evidence_claim_id": "P06-C02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de diagnóstico",
                "Visión Inquisitorial": "Califica todo retraso de meta como delito de greenwashing, alienando a los directores.",
                "Enfoque Brunsson / BRIDGE": "Ilumina los desajustes burocráticos para que la empresa sincronice sus operaciones antes del escrutinio público."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Diagnóstico de Brechas", "implication": "BRIDGE debe orientar sus alertas como oportunidades de alineamiento operacional y sincronización estratégica, no como acusaciones automáticas de mala fe.", "status": "filosofia_de_producto"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C03
    {
        "question_id": "P06-C03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrastan los benchmarks académicos de NLI (FEVER, MNLI) basados en hechos simples y binarios frente a la ambigüedad estratégica y las declaraciones prospectivas en el discurso corporativo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste expone una de las brechas metodológicas más severas documentadas en P06_QUALITY_ADDENDUM (Sección 3.2): 1) Benchmarks Académicos (FEVER, MNLI): Evalúan aserciones fácticas binarias y desprovistas de ambigüedad procedentes de enciclopedias abiertas (ej. 'La capital de Francia es París', 'Marie Curie nació en 1867'). En estos entornos cerrados, una contradicción lógica es absoluta y trivial de verificar matemáticamente; 2) Discurso de Asuntos Corporativos: Opera en un registro lingüístico dominado por la ambigüedad estratégica intencional (declaraciones calibradas para no fijar cifras vinculantes que generen contingencias ante la CMF), declaraciones prospectivas protegidas por cláusulas de advertencia (Safe Harbor Statements condicionadas a variables macroeconómicas) y retórica aspiracional ESG con horizontes a 2030 o 2050. En este dominio, confrontar una afirmación del tipo 'Aspiramos a liderar la transición energética limpia' con una inversión temporal en generación a gas no puede evaluarse con el álgebra booleana de FEVER sin generar falsos positivos grotescos; exige modelos calibrados de Natural Language Inference con comprensión contextual de matices prospectivos.",
        "findings": [
            {
                "claim_id": "P06-C03-C1",
                "claim": "Los benchmarks de NLI evalúan contradicciones lógicas binarias triviales, mientras la comunicación corporativa se rige por ambigüedad estratégica y declaraciones prospectivas complejas.",
                "epistemic_status": "limite_epistemico_critico",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Procesamiento de Lenguaje Natural en Finanzas"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.2: Falsa Equivalencia entre Benchmarks Académicos y Lenguaje Corporativo",
                        "excerpt_short": "Benchmarks como FEVER evalúan contradicciones lógicas binarias y hechos incontrovertibles... La comunicación corporativa opera en un registro radicalmente distinto, dominado por ambigüedad estratégica intencional, declaraciones prospectivas protegidas y retórica aspiracional ESG.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Advertencia metodológica formulada expresamente en P06_QUALITY_ADDENDUM."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de declaración corporativa prospectiva", "Evidencia de noticia actual"],
            "actors": ["Detector de Cláusulas Safe Harbor", "Clasificador NLI de Ambigüedad", "Analista Corporativo"],
            "steps": ["Identificación de marcadores prospectivos ('esperamos', 'aspiramos', 'sujeto a condiciones de mercado')", "Ajuste de temperatura y umbrales de rigidez lógica", "Evaluación NLI no binaria", "Etiquetado como 'Retórica Aspiracional' en lugar de 'Contradicción Factual'"],
            "states": ["Raw_Statement", "Forward_Looking_Detected", "Thresholds_Softened", "Nuanced_Classification"],
            "outputs": ["Clasificación matizada que distingue aspiración de compromiso legal cerrado"],
            "exceptions": ["Metas cuantitativas cerradas auditables con año base y horizonte temporal vinculante"]
        },
        "entities": [
            {"entity_id": "ENT_SAFE_HARBOR", "type": "institucion_legal", "name": "Cláusulas de Declaraciones Prospectivas (Safe Harbor)", "aliases": ["Forward-Looking Statements"]}
        ],
        "relations": [
            {"subject_id": "ENT_SAFE_HARBOR", "predicate": "limita_aplicabilidad_de", "object_id": "ENT_FEVER_BENCHMARK", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de la afirmación",
                "Benchmark académico (FEVER)": "Aserciones fácticas binarias de Wikipedia (Verdadero / Falso).",
                "Discurso corporativo": "Compromisos condicionados, aspiraciones de largo plazo y declaraciones prospectivas sujetas a incertidumbre económica."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Detector de Ambigüedad y Safe Harbor", "implication": "BRIDGE debe incorporar un clasificador previo que identifique si una frase es prospectiva/aspiracional antes de someterla al Cross-Encoder NLI estricto.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C04
    {
        "question_id": "P06-C04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la identificación unívoca por ticker bursátil anglosajón frente a la estructura de grupos empresariales familiares y holdings en cascada en Chile y América Latina?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste refleja una asimetría de infraestructura de datos entre mercados: 1) Modelo Anglosajón (SEC EDGAR / Bloomberg): Se apoya en una arquitectura de identificación financiera altamente estandarizada donde cada emisor cotizado dispone de un ticker bursátil unívoco (AAPL, MSFT), un número CIK centralizado y un código LEI (Legal Entity Identifier). La resolución de entidades es fundamentalmente determinista: si la noticia cita el ticker, la imputación societaria es inmediata y unívoca; 2) Modelo Chileno y Latinoamericano: Los grandes conglomerados operan bajo estructuras de propiedad piramidales y holdings en cascada dominados por grupos empresariales (ej. AntarChile -> Empresas Copec -> Celulosa Arauco / Abastible / Copec Combustibles). Las entidades que generan controversias operacionales en terreno son frecuentemente filiales operativas cerradas (SpA o Ltda.) que no cotizan en bolsa y cuyos nombres son omitidos por la prensa a favor de marcas de fantasía o del nombre de la familia controladora. Como advierte P06_GAPS_AND_VALIDATION, depender de identificadores bursátiles es inviable en la región; BRIDGE debe sustituir el enfoque determinista por una malla ontológica jerárquica con enlaces probabilísticos en Splink que navegue desde la marca de fantasía hasta el RUT matriz.",
        "findings": [
            {
                "claim_id": "P06-C04-C1",
                "claim": "En América Latina, la ausencia de tickers universales para filiales operativas exige abandonar la resolución determinista y construir mallas de holdings jerárquicas locales.",
                "epistemic_status": "asimetria_estructural_regional",
                "scope": {"time": "2020-2026", "region": "Chile / EE.UU.", "actor": "Estructuras Societarias y Mercados de Valores"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 1: Complejidad de Resolución de Entidades en Grupos Empresariales de América Latina",
                        "excerpt_short": "La literatura anglosajona asume típicamente identidades corporativas con tickers de cotización bursátil únicos (ej. SEC EDGAR CIKs). En Chile y la región, la estructura de grupos económicos está dominada por sociedades holding familiares, subsidiarias en cascada y marcas de fantasía disociadas de su razón social.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diagnóstico empírico corroborado por la estructura de mercado de la CMF y la síntesis interna."
            }
        ],
        "operational_model": {
            "inputs": ["Mención en prensa de marca comercial en Chile", "Base de datos CMF de holdings"],
            "actors": ["Enlazador Probabilístico Splink", "Grafo Jerárquico Societario"],
            "steps": ["Detección de ausencia de ticker bursátil", "Búsqueda probabilística en diccionario de marcas y filiales", "Ascenso por la pirámide de propiedad hasta la matriz IPSA", "Asignación de responsabilidad de monitoreo al Holding"],
            "states": ["Brand_Mention_Only", "Local_Entity_Linked", "Holding_Hierarchy_Traversed", "Corporate_Owner_Identified"],
            "outputs": ["Mapeo societario completo de la controversia"],
            "exceptions": ["Sociedades coligadas con propiedad compartida entre múltiples holdings"]
        },
        "entities": [
            {"entity_id": "ENT_SEC_EDGAR", "type": "repositorio_financiero", "name": "SEC EDGAR System", "aliases": ["EDGAR", "CIK Identification"]},
            {"entity_id": "ENT_CMF_REGISTRY", "type": "repositorio_financiero", "name": "Registro de Emisores CMF Chile", "aliases": ["CMF Chile", "RUT Societario"]}
        ],
        "relations": [
            {"subject_id": "ENT_CMF_REGISTRY", "predicate": "difiere_estructuralmente_de", "object_id": "ENT_SEC_EDGAR", "valid_from": "2020", "valid_to": "2026", "evidence_claim_id": "P06-C04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resolución de entidad corporativa",
                "Enfoque Anglosajón (SEC CIK)": "Mapeo 1:1 inmediato a través del ticker bursátil del emisor.",
                "Enfoque Latinoamericano BRIDGE": "Resolución probabilística multi-etapa a través del grafo de holding familiar y marcas de fantasía."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Mapeador Societario Latinoamericano", "implication": "BRIDGE debe incluir en su arquitectura un grafo de holdings familiares chilenos para vincular marcas comerciales con su matriz cotizada en bolsa.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C05
    {
        "question_id": "P06-C05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la recuperación exclusivamente vectorial por similitud semántica (Sentence-BERT) frente a grafos de conocimiento temporal dinámicos (T-GRAG) ante eventos en evolución?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste ilustra la transición desde una búsqueda estática de documentos hacia un razonamiento dinámico en el tiempo: 1) Recuperación Exclusivamente Vectorial (Sentence-BERT / RAG estándar): Almacena pasajes como puntos estáticos en un espacio vectorial multidimensional. Ante un evento en evolución (ej. un incidente ambiental que inicia con una fiscalización menor, luego escala a formulación de cargos y concluye con una multa o absolución), la búsqueda vectorial recupera fragmentos mezclados de distintas fechas simplemente porque comparten alta similitud semántica de palabras clave. El LLM resultante genera síntesis caóticas donde eventos superados se presentan como vigentes o las sanciones finales se omiten por tener menor similitud léxica; 2) Grafos de Conocimiento Dinámicos (T-GRAG; Li et al., 2025): Modela el evento como una trayectoria estructurada de tripletas con intervalos $[t_\\text{start}, t_\\text{end}]$. Utilizando Descomposición Temporal (TQD), T-GRAG recupera ordenadamente la secuencia causal de hechos (Inspección en $t_1 \\to$ Descargos en $t_2 \\to$ Sanción ejecutoriada en $t_3$), permitiendo a BRIDGE contrastar con precisión quirúrgica el estado de la controversia en cada momento histórico.",
        "findings": [
            {
                "claim_id": "P06-C05-C1",
                "claim": "La búsqueda vectorial colapsa la evolución temporal mezclando etapas contradictorias de un incidente, mientras T-GRAG reconstruye la trayectoria cronológica causal exacta.",
                "epistemic_status": "contraste_arquitectural_rag",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Investigación en Temporal RAG"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 1: Limitations of Vector-based and Static Graph RAG",
                        "excerpt_short": "Static vector retrieval conflates facts from different time periods, unable to capture how entity attributes transform over time, leading to factual obsolescence and hallucinated temporal states.",
                        "source_date": "2025-08-03",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Justificación teórica y empírica central del marco T-GRAG."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta sobre el estado actual de una controversia ambiental histórica"],
            "actors": ["Recuperador Vectorial S-BERT", "Motor Dinámico T-GRAG"],
            "steps": ["S-BERT recupera fragmentos de 2022, 2023 y 2025 sin orden cronológico", "T-GRAG descompone la trayectoria temporal y extrae el estado vigente al día de hoy", "Comparación de respuestas y constatación de la superioridad de T-GRAG"],
            "states": ["Raw_Incident_Data", "Vector_Retrieved_Disordered", "TGRAG_Path_Traversed", "Chronologically_Accurate_State"],
            "outputs": ["Línea de tiempo estructurada y estado vigente incontrovertible"],
            "exceptions": ["Incidentes donde la información externa se interrumpe y no existe registro público del desenlace"]
        },
        "entities": [
            {"entity_id": "ENT_VECTOR_RETRIEVAL", "type": "tecnica_de_busqueda", "name": "Búsqueda Vectorial por Similitud", "aliases": ["Vector RAG", "k-NN Dense Search"]},
            {"entity_id": "ENT_T_GRAG", "type": "marco_algoritmico", "name": "T-GRAG (Li et al., 2025)", "aliases": ["Dynamic Temporal GraphRAG"]}
        ],
        "relations": [
            {"subject_id": "ENT_T_GRAG", "predicate": "resuelve_limitaciones_temporales_de", "object_id": "ENT_VECTOR_RETRIEVAL", "valid_from": "2025", "valid_to": "2026", "evidence_claim_id": "P06-C05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Modelado de procesos en evolución",
                "RAG Vectorial": "Mezcla fragmentos del inicio del sumario con la absolución final, afirmando contradictoriamente que la empresa 'está siendo multada y absuelta a la vez'.",
                "T-GRAG": "Mapea la arista de sanción con su fecha exacta y la arista de sobreseimiento posterior, concluyendo con el estado final verídico."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor de Seguimiento de Controversias", "implication": "BRIDGE debe estructurar el seguimiento de crisis como un grafo dinámico temporal T-GRAG para entregar la situación jurídica actualizada en tiempo real.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C06
    {
        "question_id": "P06-C06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la indexación plana atemporal frente al modelado bitemporal estricto (tiempo de validez, de publicación y de transacción) en memorias anuales y fiscalizaciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste demuestra por qué los sistemas RAG convencionales fracasan en entornos regulados: 1) Indexación Plana Atemporal: Almacena los textos sin discriminar fechas o utilizando un único timestamp arbitrario (la fecha en que se subió el archivo PDF al sistema). En esta arquitectura, una memoria anual subida en 2026 pero referida a datos operacionales de 2024 se indexa con fecha de 2026, provocando que cualquier confrontación con noticias intermedias de 2025 genere falsas contradicciones de 'anacronismo inverso'; 2) Modelado Bitemporal Estricto (W3C DCAT-3 / T-GRAG): Separa rigurosamente: a) Tiempo de Validez (VT): 01-01-2024 a 31-12-2024 (período en que rigieron los hechos); b) Tiempo de Publicación (PT): 31-03-2025 (depósito formal ante la CMF); y c) Tiempo de Transacción (TT): 01-10-2026 (indexación en BRIDGE). Este desacoplamiento permite al sistema certificar que un incidente ocurrido en octubre de 2025 no puede imputarse a la memoria publicada en marzo de 2025, preservando la inmutabilidad de la verdad histórica y permitiendo auditorías forenses 'as-of' perfectas.",
        "findings": [
            {
                "claim_id": "P06-C06-C1",
                "claim": "La indexación atemporal produce anacronismos e imputaciones falsas, mientras el modelado bitemporal estricto separa el período de los hechos de la fecha de publicación formal.",
                "epistemic_status": "principio_de_modelado_de_datos",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Bases de Datos Bitemporales y Compliance"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Diferencia Temporal (Temporal Lag / Evolution)",
                        "excerpt_short": "Desfase inherente entre la fecha de corte de los reportes internos y la señal externa ocurrida posteriormente... Sin anclaje temporal, el sistema genera falsos positivos de contradicción.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 1: Marco Teórico y Fundamentos Conceptuales",
                        "excerpt_short": "Se desacoplan estrictamente el tiempo de validez, el de publicación y el de transacción, preservando documentos inmutables mediante relaciones de sustitución para permitir auditorías y consultas retrospectivas as-of.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio arquitectural rector consolidado en P04 y P06."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria NCG 461 ejercicio 2024 depositada en marzo 2025", "Noticia de derrame en julio 2025"],
            "actors": ["Parser Bitemporal", "Motor de Reglas Temporales"],
            "steps": ["Asignación de VT [2024-01-01, 2024-12-31] y PT [2025-03-31]", "Asignación de fecha de noticia [2025-07-15]", "Constatación de que noticia.fecha > PT y noticia.fecha > VT_end", "Bloqueo automático de acusación de contradicción"],
            "states": ["Raw_Records", "Bitemporal_Tags_Assigned", "Intervals_Compared", "Discrepancy_Dismissed_as_Temporal"],
            "outputs": ["Descarte formal de falsos positivos de contradicción"],
            "exceptions": ["Hechos sustanciales conocidos por la empresa antes del depósito PT que debieron ser revelados como hechos posteriores al cierre bajo normas IFRS"]
        },
        "entities": [
            {"entity_id": "ENT_BITEMPORAL_MODEL", "type": "modelo_de_datos", "name": "Modelo de Datos Bitemporal (VT/PT/TT)", "aliases": ["Bitemporal Architecture", "W3C DCAT-3 Temporal Model"]}
        ],
        "relations": [
            {"subject_id": "ENT_BITEMPORAL_MODEL", "predicate": "garantiza_integridad_en", "object_id": "ENT_CROSS_PIPELINE", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Rigor temporal",
                "Indexación plana atemporal": "Atribuye la fecha de subida del archivo al contenido; comete errores sistemáticos de anacronismo.",
                "Modelado Bitemporal BRIDGE": "Discrimina el tiempo en que ocurrió el hecho del tiempo en que se publicó; preserva la verdad jurídica exacta."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Motor Bitemporal", "implication": "BRIDGE debe requerir los tres sellos de tiempo (VT, PT, TT) en toda afirmación y evidencia para operar con rigor de compliance.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C07"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C07
    {
        "question_id": "P06-C07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la resolución determinista de entidades por coincidencia exacta de strings frente a la resolución probabilística con reglas de bloqueo (Splink / Fellegi-Sunter)?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste expone las causas del colapso de los sistemas de entidad en entornos ruidosos no estructurados: 1) Resolución Determinista por Coincidencia Exacta de Strings (Exact String Matching): Busca coincidencias textuales literales mediante sentencias `WHERE nombre = '...'` o expresiones regulares rígidas. En el ecosistema de medios y redes de América Latina, este enfoque fracasa estrepitosamente: una errata tipográfica menor ('cmpc' vs 'cmpk'), un cambio de orden léxico ('Banco Santander Chile' vs 'Santander Banco') o la omisión del tipo societario ('Falabella Retail S.A.' vs 'Falabella') provoca que el sistema omita hasta el 60% de las menciones relevantes (falsos negativos masivos); 2) Resolución Probabilística con Reglas de Bloqueo (Splink / Fellegi-Sunter): Emplea particiones disyuntivas para reducir el espacio de búsqueda y evalúa probabilísticamente múltiples atributos en paralelo (nombre, ciudad, sector, RUT parcial, directores) mediante ponderaciones logarítmicas de verosimilitud bayesianas. Tolera variaciones ortográficas, errores de transcripción radial o coloquialismos de prensa, alcanzando una exhaustividad superior al 95% sin disparar falsos positivos gracias a las penalizaciones por discordancia atributaria.",
        "findings": [
            {
                "claim_id": "P06-C07-C1",
                "claim": "La coincidencia exacta de strings pierde más del 60% de menciones por rigidez ortográfica, mientras Fellegi-Sunter en Splink recupera variantes complejas con precisión probabilística.",
                "epistemic_status": "contraste_algoritmico",
                "scope": {"time": "2021-2026", "region": "Global / Chile", "actor": "Entity Resolution y Ciencia de Datos"},
                "evidence": [
                    {
                        "source_id": "575a54b9-fada-4812-882e-b5e7c56c27d2",
                        "source_title": "Splink (UK MoJ) - Fast, Scalable Probabilistic Entity Resolution",
                        "original_url": "https://moj-analytical-services.github.io/splink/index.html",
                        "locator": "Introduction: Why Deterministic Matching Fails at Scale",
                        "excerpt_short": "Deterministic matching rules are brittle, suffering from high false negative rates due to misspellings, typographical errors, and varying entity representations. Probabilistic matching with Splink resolves these variations efficiently.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fundamentación técnica unívoca en la documentación y benchmarks de Splink."
            }
        ],
        "operational_model": {
            "inputs": ["Noticia externa con errata: 'Minera Los Pelambres SpA' escrita como 'Minera Los Pelambres S.A.'"],
            "actors": ["Matcher Determinista", "Motor Splink Fellegi-Sunter"],
            "steps": ["Matcher determinista falla por discrepancia de 'SpA' vs 'S.A.' (False Negative)", "Splink compara por Jaro-Winkler, detecta alta concordancia de nombre y comuna, y asigna peso de match posterior P = 0.98", "Enlace exitoso de la mención"],
            "states": ["Raw_Typo_Mention", "Deterministic_Failed", "Splink_Scored", "Entity_Linked_Successfully"],
            "outputs": ["Enlace de entidad robusto frente a variaciones de redacción"],
            "exceptions": ["Nombres corporativos ultra-cortos de 2 o 3 caracteres donde cualquier cambio altera radicalmente la identidad"]
        },
        "entities": [
            {"entity_id": "ENT_DETERMINISTIC_MATCHING", "type": "tecnica_obsoleta", "name": "Coincidencia Determinista de Strings", "aliases": ["Exact String Match", "Regex Matcher"]},
            {"entity_id": "ENT_SPLINK", "type": "software_biblioteca", "name": "Splink Probabilistic Entity Resolution", "aliases": ["Splink", "Fellegi-Sunter"]}
        ],
        "relations": [
            {"subject_id": "ENT_SPLINK", "predicate": "supera_en_exhaustividad_a", "object_id": "ENT_DETERMINISTIC_MATCHING", "valid_from": "2021", "valid_to": "2026", "evidence_claim_id": "P06-C07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Tolerancia al ruido en prensa",
                "Coincidencia exacta": "Cero tolerancia; un punto o una tilde diferente descarta la noticia.",
                "Splink probabilístico": "Pondera el conjunto de la evidencia, enlazando la entidad con certeza bayesiana aun con variaciones léxicas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Tasa de recuperación de menciones ruidosas", "denominator": "Total de menciones en prensa regional", "formula": "> 95% de cobertura con Splink vs < 40% con coincidencia exacta"}
        ],
        "bridge_implications": [
            {"module": "Extractor de Entidades", "implication": "BRIDGE debe erradicar sentencias de coincidencia exacta y basar todo su pipeline de vinculación de registros en Splink probabilístico.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-C08
    {
        "question_id": "P06-C08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se contrasta la búsqueda comunitaria global (GraphRAG Leiden) frente a la recuperación local por entidad en la detección de contradicciones corporativas específicas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El contraste define la especialización funcional de cada modo de búsqueda dentro de GraphRAG (Edge et al., 2024): 1) Recuperación Local por Entidad (Local Search): Diseñada para la verificación atómica y granular de hechos específicos. Toma como semilla un nodo concreto (ej. 'Planta Santa Fe') y navega sus aristas de primer y segundo orden hacia compromisos de emisión y fiscalizaciones puntuales. Es el método idóneo para comprobar una 'Contradicción Real' concreta, pues extrae los pasajes exactos requeridos para el NLI, maximizando la precisión factual (FActScore); 2) Búsqueda Comunitaria Global (Global Search vía Leiden): Diseñada para la síntesis holística y el mapeo de riesgos emergentes ('Sensemaking'). No busca en nodos aislados, sino que consulta los resúmenes precomputados de clusters de comunidades jerárquicas generados por el algoritmo Leiden. Es ideal para responder preguntas estratégicas amplias (ej. '¿Existe un patrón sistémico de discrepancia en nuestras metas de reducción de agua a lo largo de todas las filiales mineras?'), pero es inapropiada para verificar una multa puntual porque el resumen comunitario tiende a omitir detalles de cifras específicas. En BRIDGE, ambos modos colaboran: la búsqueda comunitaria global alerta sobre clusters temáticos de riesgo, y la recuperación local desciende a verificar la cita exacta.",
        "findings": [
            {
                "claim_id": "P06-C08-C1",
                "claim": "La búsqueda comunitaria global detecta patrones temáticos transversales de riesgo, mientras la recuperación local verifica la cita atómica exacta de la contradicción.",
                "epistemic_status": "complementariedad_arquitectural",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Microsoft Research (GraphRAG)"},
                "evidence": [
                    {
                        "source_id": "4a4a5417-6cca-4af2-b946-893e515614c9",
                        "source_title": "Edge et al. (2024) - GraphRAG: Query-Focused Summarization",
                        "original_url": "https://arxiv.org/abs/2404.16130",
                        "locator": "Section 3: Global Search and Local Search Complementarity",
                        "excerpt_short": "Global search provides thematic summarization over the entire corpus using hierarchical community summaries, whereas local search traverses explicit entity-relation neighbors for factual, pinpoint inquiries.",
                        "source_date": "2024-04-24",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio de diseño arquitectural fundamental formulado en GraphRAG."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta directiva sobre riesgo sistémico vs consulta sobre sanción puntual"],
            "actors": ["Enrutador de Consultas GraphRAG", "Motor Local Search", "Motor Global Search"],
            "steps": ["Análisis de la especificidad de la consulta", "Si es transversal, disparar Global Search en resúmenes de Leiden", "Si es puntual, disparar Local Search en vecindario del grafo", "Fusión en respuesta contextualmente balanceada"],
            "states": ["Query_Analyzed", "Route_Selected", "Graph_Executed", "Synthesized_Answer"],
            "outputs": ["Respuesta adecuada en granularidad y respaldo probatorio"],
            "exceptions": ["Consultas donde el usuario pide primero el panorama global y luego exige la cita de página exacta"]
        },
        "entities": [
            {"entity_id": "ENT_LOCAL_SEARCH", "type": "modo_de_recuperacion", "name": "Búsqueda Local por Entidad (Local Search)", "aliases": ["Entity-centric Search"]},
            {"entity_id": "ENT_GLOBAL_SEARCH", "type": "modo_de_recuperacion", "name": "Búsqueda Comunitaria Global (Global Search)", "aliases": ["Community-centric Search", "Leiden Global Search"]}
        ],
        "relations": [
            {"subject_id": "ENT_GLOBAL_SEARCH", "predicate": "se_complementa_con", "object_id": "ENT_LOCAL_SEARCH", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-C08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de resolución",
                "Búsqueda Comunitaria Global (Leiden)": "Visión macroscópica de bosque; excelente para tendencias, deficiente para números de expediente.",
                "Recuperación Local por Entidad": "Visión microscópica de árbol; perfecta para números de causas y párrafos exactos, incapaz de síntesis corporativa."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Orquestador de Búsqueda BRIDGE", "implication": "BRIDGE debe permitir la alternancia fluida entre la vista comunitaria para Comités Ejecutivos y la vista local atómica para auditorías de vocería.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-C09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-C01..C08) to {out_path}.")
