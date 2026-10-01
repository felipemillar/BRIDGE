import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-F31
    {
        "question_id": "P06-F31",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cuáles son las cuatro categorías fundamentales de discrepancia entre conocimiento interno y señales externas y por qué no toda brecha es una mentira?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El corpus consagra que la principal patología de los sistemas de monitoreo y RAG ingenuos es asumir que cualquier divergencia entre el reporte corporativo y una noticia externa constituye un engaño deliberado, fraude o mentira (greenwashing). Como fundamentan P06_EVIDENCE_MAP y P06_RESEARCH_DOSSIER, es imperativo clasificar rigurosamente las discrepancias en cuatro categorías epistémicas mutuamente excluyentes: 1) Contradicción Real (Direct Fact Incoherence): Conflicto fáctico directo e irreconciliable para un mismo marco temporal y geográfico con evidencia oficial vinculante; 2) Diferencia Temporal (Temporal Lag / Evolution): Desfase cronológico natural entre la fecha de corte de la memoria anual y eventos posteriores, o metas de largo plazo evaluadas con hitos parciales; 3) Diferencia de Alcance (Scope / Boundary Divergence): La declaración abarca un perímetro legal u operativo distinto al de la señal externa (Alcance 1 y 2 directos vs Alcance 3 de contratistas, o filial local vs matriz holding); y 4) Acusación No Verificada (Unsubstantiated Allegation): Señal externa procedente de redes sociales o declaraciones de activistas que carece de expediente probatorio o resolución administrativa/judicial. Reconocer estas diferencias evita generar falsas alarmas de crisis interna y protege a la empresa de sobrerreacciones lesivas.",
        "findings": [
            {
                "claim_id": "P06-F31-C1",
                "claim": "Las discrepancias entre reportes internos y señales del entorno se clasifican obligatoriamente en 4 categorías: Contradicción Real, Diferencia Temporal, Diferencia de Alcance y Acusación No Verificada.",
                "epistemic_status": "taxonomia_epistemica_central",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Gestión de Asuntos Corporativos y Riesgo"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Taxonomía Epistémica de Discrepancias",
                        "excerpt_short": "La principal falla de los sistemas RAG tradicionales es tratar cualquier discrepancia entre documento interno y noticia externa como una 'contradicción o mentira'. Se deben separar formalmente cuatro fenómenos: Contradicción Real, Diferencia Temporal, Diferencia de Alcance y Acusación No Verificada.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Entregable Específico 1: Matriz Afirmación-Evidencia",
                        "excerpt_short": "Tipología de Discrepancia: Clasificación entre: (1) Contradicción Real, (2) Desfase Temporal, (3) Desfase de Alcance, (4) Acusación No Verificada.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Taxonomía analítica central y obligatoria del pilar P06 ratificada en todas las síntesis internas."
            }
        ],
        "operational_model": {
            "inputs": ["Divergencia detectada entre afirmación interna y señal externa"],
            "actors": ["Clasificador de Discrepancias BRIDGE", "Analista de Asuntos Corporativos"],
            "steps": ["Verificación de concordancia temporal", "Verificación de coincidencia de alcance perimetral", "Verificación de estatus probatorio de la fuente externa", "Asignación de una de las 4 clases de discrepancia"],
            "states": ["Raw_Discrepancy", "Temporal_Evaluated", "Scope_Evaluated", "Proof_Status_Evaluated", "Typology_Assigned"],
            "outputs": ["Clasificación unívoca de tipología y recomendación de acción"],
            "exceptions": ["Controversias híbridas que involucran simultáneamente desfase temporal y desalineación de alcance"]
        },
        "entities": [
            {"entity_id": "ENT_DISCREPANCY_TYPOLOGY", "type": "taxonomia_operacional", "name": "Tipología Epistémica de 4 Discrepancias BRIDGE", "aliases": ["4-Class Discrepancy Framework"]}
        ],
        "relations": [
            {"subject_id": "ENT_DISCREPANCY_TYPOLOGY", "predicate": "gobierna_clasificacion_de", "object_id": "ENT_CLAIM_EVIDENCE_MATRIX", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F31-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de discrepancia",
                "Visión binaria ingenua": "Si el texto externo no coincide palabra por palabra con la memoria, es greenwashing o mentira corporativa.",
                "Marco epistémico BRIDGE": "Discrimina si la divergencia responde a evolución temporal, perímetro legal o denuncia sin pruebas, asignando la respuesta adecuada."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Clasificador Epistémico BRIDGE", "implication": "BRIDGE debe codificar como lógica central las 4 tipologías para no alertar de crisis cuando solo existe una evolución temporal o diferencia de alcance.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F32"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F32
    {
        "question_id": "P06-F32",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se define, detecta y comprueba una 'Contradicción Real' (Direct Fact Incoherence) y qué umbrales probatorios exige?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Una 'Contradicción Real' (Direct Fact Incoherence) se define como un conflicto fáctico directo, sustancial e irreconciliable entre una afirmación corporativa oficial y un hecho verificado en el entorno para exactamente el mismo marco temporal, alcance geográfico y entidad legal. Para catalogar una discrepancia bajo esta categoría de máxima severidad, el sistema exige umbrales probatorios rigurosos: 1) Identidad Temporal y Espacial Exacta: El intervalo de validez de la afirmación $[VT_{\\text{start}}, VT_{\\text{end}}]$ debe coincidir con la fecha del hecho externo, y el activo físico o personería jurídica debe ser exactamente el mismo; 2) Fuente de Alta Autoridad y Fe Pública: La evidencia externa debe provenir de un organismo regulador facultado por ley (ej. resolución sancionatoria de la SMA en SNIFA, dictamen sancionatorio de la CMF, resolución de SERNAC), una sentencia ejecutoriada de tribunales de justicia o un dictamen de auditoría forense independiente con trazabilidad probatoria; y 3) Certeza NLI Estricta: El clasificador Cross-Encoder NLI debe asignar una probabilidad a la clase `Contradiction` $P \\ge 0.90$. Ante una Contradicción Real comprobada (ej. Caso CLM-01 de P06_RESEARCH_DOSSIER: declarar 100% agua desalinizada cuando la SMA formuló cargos por extracción no autorizada de 45 L/s en acuífero), el sistema eleva inmediatamente el semáforo a 'Riesgo Crítico' y recomienda activar el Gabinete de Crisis.",
        "findings": [
            {
                "claim_id": "P06-F32-C1",
                "claim": "Una Contradicción Real exige coincidencia estricta de tiempo y alcance, evidencia oficial respaldada por autoridad regulatoria y certeza NLI P >= 0.90.",
                "epistemic_status": "protocolo_de_deteccion_de_crisis",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Compliance y Gestión de Crisis"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Contradicción Real (Direct Fact Incoherence)",
                        "excerpt_short": "Conflicto directo e irreconciliable entre un hecho verificado en el entorno y una afirmación oficial de la empresa para un mismo marco temporal y geográfico... Por ejemplo, reportar cero litigios laborales activos ante la CMF cuando existen demandas colectivas con sentencia firme.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7ffaecea-0ea0-4037-8ae3-e09f34ab29f0",
                        "source_title": "SMA Chile - SNIFA: Registro Público de Fiscalización y Sanciones",
                        "original_url": "https://snifa.sma.gob.cl/RegistroPublico",
                        "locator": "Efectos Jurídicos de los Procedimientos Sancionatorios",
                        "excerpt_short": "Los actos administrativos sancionatorios de la Superintendencia del Medio Ambiente contenidos en el SNIFA constituyen actos públicos vinculantes que constatan infracciones a la normativa ambiental.",
                        "source_date": "2024-01-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Definición canónica probatoria respaldada en P06_EVIDENCE_MAP y la validez legal del SNIFA."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de compromiso oficial", "Resolución regulatoria de la SMA / CMF"],
            "actors": ["Motor NLI de Alta Precisión", "Comprobador de Identidad Temporal y Espacial", "Director de Crisis"],
            "steps": ["Verificación de coincidencia de período [t_start, t_end]", "Verificación de entidad jurídica y faena", "Evaluación de validez legal de la fuente (resolución formal)", "Disparo de alerta roja de crisis corporativa"],
            "states": ["Candidate_Discrepancy", "Temporal_Identity_Confirmed", "Regulatory_Proof_Verified", "Contradiction_Real_Flagged"],
            "outputs": ["Alerta roja en Dashboard", "Ficha de preparación de vocería y mitigación legal"],
            "exceptions": ["Resolución regulatoria que se encuentra suspendida o anulada judicialmente por un recurso de protección"]
        },
        "entities": [
            {"entity_id": "ENT_CONTRADICCION_REAL", "type": "tipo_de_discrepancia", "name": "Contradicción Real (Direct Fact Incoherence)", "aliases": ["Direct Incoherence", "Factual Refutation"]}
        ],
        "relations": [
            {"subject_id": "ENT_CONTRADICCION_REAL", "predicate": "detona_alerta_en", "object_id": "ENT_GABINETE_CRISIS", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F32-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de gravedad",
                "Diferencia de alcance": "Riesgo medio; requiere aclaración técnica de perímetro.",
                "Contradicción real": "Riesgo crítico; evidencia que la empresa afirmó algo manifiestamente falso o infringió la ley.",
                "Acusación no verificada": "Riesgo reputacional potencial; requiere monitoreo y no admisión de culpa."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Umbral de certeza NLI para Contradicción Real", "denominator": "Probabilidad condicional del Cross-Encoder", "formula": "P(Contradiction | Evidencia) >= 0.90"}
        ],
        "bridge_implications": [
            {"module": "Gestor de Alertas Críticas", "implication": "BRIDGE debe reservar la alerta roja de 'Contradicción Real' exclusivamente para casos con evidencia oficial probatoria irrefutable.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F33"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F33
    {
        "question_id": "P06-F33",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se tipifica y gestiona una 'Diferencia Temporal' (Temporal Lag / Evolution) para evitar falsas alarmas ante eventos posteriores al cierre del reporte?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Una 'Diferencia Temporal' (Temporal Lag / Evolution) se tipifica cuando los hechos reportados internamente eran verídicos y precisos durante el intervalo de validez original del reporte, pero un incidente operacional, cambio regulatorio o fluctuación económica posterior al cierre del período genera una discordancia aparente. Casos típicos: 1) Fecha de Corte de Memoria Anual: La memoria integrada se cierra al 31 de diciembre del año previo; un incidente en febrero del año en curso no contradice la afirmación de que el año previo cerró sin accidentes; 2) Metas de Largo Plazo (Trayectorias ESG 2030): Una meta de reducir 50% de emisiones para 2030 no se ve refutada porque en 2025 las emisiones hayan subido temporalmente un 2% por un aumento puntual de demanda operativa (ej. Caso CLM-02 en P06_RESEARCH_DOSSIER). Para gestionar esta brecha, el sistema: 1) Extrae el diferencial de fechas $\\Delta t$; 2) Etiqueta la relación como 'Desfase Temporal'; 3) Asigna nivel de riesgo reputacional 'Medio' (evitando pánico de crisis); y 4) Recomienda al equipo de asuntos corporativos publicar una minuta contextualizadora que ratifique la curva de largo plazo y aclare que los reportes de cierre no pueden incorporar eventos sobrevinientes.",
        "findings": [
            {
                "claim_id": "P06-F33-C1",
                "claim": "La Diferencia Temporal se tipifica por discordancia cronológica legítima entre fecha de corte de reporte y eventos sobrevinientes, requiriendo aclaración contextual y no alerta de crisis.",
                "epistemic_status": "buena_practica_de_gestion",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Asuntos Corporativos y Relaciones con Inversionistas"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Diferencia Temporal (Temporal Lag / Evolution)",
                        "excerpt_short": "Desfase inherente entre la fecha de corte de los reportes internos (ej. memoria anual consolidada al 31 de diciembre) y la señal externa ocurrida posteriormente... Sin anclaje temporal, el sistema genera falsos positivos de contradicción.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Caso CLM-02: Meta de reducción de emisiones vs fluctuación puntual",
                        "excerpt_short": "Diferencia Temporal / Alcance... Acción recomendada: Publicar nota explicativa contextualizando el incremento temporal por aumento de producción y ratificando la curva de descarbonización 2030.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Patrón analítico consolidado en el Dossier y Evidence Map de P06."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria con fecha de corte cerrada (ej. 31-12-2024)", "Noticia de incidente en fecha posterior (ej. 15-03-2025)"],
            "actors": ["Evaluador de Línea Temporal", "Motor de Recomendaciones Estratégicas", "Vocero Corporativo"],
            "steps": ["Detección de que la fecha del evento es posterior al cierre del reporte", "Descarte automático de la etiqueta 'Contradicción Real'", "Asignación de 'Diferencia Temporal'", "Generación de minuta explicativa de vocería"],
            "states": ["Discrepancy_Detected", "Chronology_Checked", "Classified_Temporal_Lag", "Action_Brief_Generated"],
            "outputs": ["Minuta de contextualización temporal para prensa"],
            "exceptions": ["Eventos ocurridos antes del cierre pero descubiertos u ocultados deliberadamente"]
        },
        "entities": [
            {"entity_id": "ENT_DIFERENCIA_TEMPORAL", "type": "tipo_de_discrepancia", "name": "Diferencia Temporal (Temporal Lag / Evolution)", "aliases": ["Temporal Lag", "Chronological Mismatch"]}
        ],
        "relations": [
            {"subject_id": "ENT_DIFERENCIA_TEMPORAL", "predicate": "desencadena_accion", "object_id": "ENT_MINUTA_CONTEXTUALIZACION", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F33-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Respuesta corporativa",
                "Ante Contradicción Real": "Admitir falta, rectificar información, suspender vocería y compensar.",
                "Ante Diferencia Temporal": "Explicar la fecha de corte del reporte, aportar datos del período en curso y reafirmar la meta global."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Detector de Diferencias Temporales", "implication": "BRIDGE debe redactar borradores de respuesta que enfaticen la fecha de corte del documento corporativo para desactivar acusaciones de ocultamiento.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F34"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F34
    {
        "question_id": "P06-F34",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se tipifica y gestiona una 'Diferencia de Alcance' (Scope / Boundary Divergence), particularmente en materias de huella de carbono (Alcances 1/2 vs 3) o ámbito geográfico?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Una 'Diferencia de Alcance' (Scope / Boundary Divergence) ocurre cuando la declaración de la empresa y la imputación externa abordan entidades legales, activos geográficos o perímetros operacionales diferentes. En el ámbito corporativo y ESG, esto se manifiesta en tres ejes principales: 1) Perímetros del GHG Protocol (Alcances 1, 2 y 3): Una empresa reporta legítimamente que sus 'emisiones directas de combustión y consumo eléctrico (Scope 1 y 2) se redujeron 25%', mientras un reportaje ambiental acusa que la firma 'aumentó su contaminación' aludiendo a las emisiones indirectas de la cadena de suministro y transporte de proveedores (Scope 3); 2) Perímetro Geográfico y Societario: Un compromiso formulado para las faenas en Chile no aplica automáticamente a operaciones de subsidiarias en Perú o Brasil; y 3) Relaciones Laborales Directas vs Subcontratadas: Afirmar 'cero huelgas' en plantilla interna mientras contratistas externos de transporte paralizan operaciones (ej. Caso CLM-05 en P06_RESEARCH_DOSSIER). Para gestionar esta brecha, el sistema: 1) Identifica la discrepancia de perímetros; 2) Etiqueta como 'Diferencia de Alcance'; 3) Asigna riesgo reputacional 'Medio-Alto'; y 4) Recomienda un plan de comunicación que aclare los límites formales del compromiso e informe las políticas de debida diligencia sobre proveedores.",
        "findings": [
            {
                "claim_id": "P06-F34-C1",
                "claim": "La Diferencia de Alcance surge de discrepancias en perímetros de reporte (Scope 1/2 vs Scope 3, límites societarios o faenas geográficas) y exige clarificación perimetral.",
                "epistemic_status": "estandar_de_reporte_esg",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "GHG Protocol, SEC y CMF"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Diferencia de Alcance (Scope / Boundary Divergence)",
                        "excerpt_short": "La declaración corporativa abarca una entidad legal o alcance operativo distinto al objeto de la señal externa... compromisos de emisiones directas (Alcance 1 y 2) versus controversias por emisiones de proveedores (Alcance 3).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "63b1de09-9f1d-41a5-9330-66204a40f355",
                        "source_title": "SEC (2024) - Final Rule: Climate-Related Disclosures for Investors",
                        "original_url": "https://www.sec.gov/news/press-release/2024-31",
                        "locator": "Scope Demarcation and Materiality Thresholds",
                        "excerpt_short": "The SEC final rules distinguish between direct emissions under operational control and indirect value chain impacts, reflecting the strict boundary demarcations required in corporate reporting.",
                        "source_date": "2024-03-06",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Criterio perimetral unificado en GHG Protocol, SEC Climate Disclosures y CMF NCG 461."
            }
        ],
        "operational_model": {
            "inputs": ["Compromiso interno con delimitación de alcance", "Noticia o informe externo sobre contratistas/filiales"],
            "actors": ["Extractor de Perímetro", "Mapeador Ontológico de Alcance", "Analista de Sustentabilidad"],
            "steps": ["Verificación de concordancia de Scope (1/2 vs 3)", "Verificación de coincidencia de entidad jurídica y geográfica", "Clasificación como 'Diferencia de Alcance'", "Generación de Q&A precisando los límites de responsabilidad operacional"],
            "states": ["Raw_Inputs", "Perimeter_Evaluated", "Divergence_Flagged", "Scope_Clarification_Ready"],
            "outputs": ["Documento Q&A de aclaración perimetral"],
            "exceptions": ["Regulaciones emergentes que responsabilizan a la matriz por abusos de derechos humanos en su cadena de suministro (Due Diligence)"]
        },
        "entities": [
            {"entity_id": "ENT_DIFERENCIA_ALCANCE", "type": "tipo_de_discrepancia", "name": "Diferencia de Alcance (Scope Divergence)", "aliases": ["Scope Divergence", "Boundary Mismatch"]}
        ],
        "relations": [
            {"subject_id": "ENT_DIFERENCIA_ALCANCE", "predicate": "requiere_clarificacion_en", "object_id": "ENT_QA_ESTRATEGICO", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F34-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Delimitación perimetral",
                "Perímetro de control operacional directo": "Faenas, plantas y empleados contratados directamente por la sociedad emisora.",
                "Perímetro de cadena de valor extendida": "Contratistas de transporte, proveedores de insumos y clientes finales (Alcance 3)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Analizador de Perímetro y Alcance", "implication": "BRIDGE debe desglosar las afirmaciones identificando si aplican a Alcance 1/2 o 3, impidiendo que noticias sobre terceros no controlados disparen alarmas de incumplimiento interno.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F35"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F35
    {
        "question_id": "P06-F35",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se tipifica y procesa una 'Acusación No Verificada' (Unsubstantiated Allegation) originada en redes sociales o denuncias sin sustento judicial/administrativo?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Una 'Acusación No Verificada' (Unsubstantiated Allegation) se tipifica cuando una señal externa imputa a la corporación conductas ilícitas, malas prácticas o incumplimientos, pero la fuente de origen carece de sustento documental probatorio, peritaje técnico o resolución de una autoridad competente (ej. publicaciones virales en X/TikTok, comunicados de ONG sin datos de respaldo, denuncias anónimas en blogs). El procesamiento de esta tipología es de máxima sensibilidad para evitar caer en provocaciones lesivas: 1) Clasificación y Registro Silencioso: El sistema etiqueta la señal como 'Acusación No Verificada', score de confianza bajo ($P < 0.60$) y nivel de riesgo 'Medio'; 2) Activación de Compuertas de Abstención Estratégica: Siguiendo las directrices éticas de IABC y Page Society, se prohíbe terminantemente la generación automática de respuestas públicas o comunicados reactivos desmentidores, previniendo el efecto Streisand y la legitimación involuntaria de la acusación; y 3) Monitoreo de Tracción y Verificación Interna: El sistema inicia una escucha pasiva para monitorear si la narrativa adquiere velocidad de propagación ($R_0 > 1$) o si es recogida por actores con legitimidad institucional (diputados, fiscales, prensa formal de investigación). Paralelamente, emite una orden de verificación interna silenciosa hacia el área legal/operativa para comprobar si existe alguna base fáctica real en la acusación.",
        "findings": [
            {
                "claim_id": "P06-F35-C1",
                "claim": "Las acusaciones no verificadas exigen abstención pública inmediata, registro silencioso, monitoreo de propagación viral y verificación interna de antecedentes.",
                "epistemic_status": "protocolo_de_gestion_de_crisis",
                "scope": {"time": "2023-2026", "region": "Global / Chile", "actor": "Estrategia de Comunicaciones y Redes Sociales"},
                "evidence": [
                    {
                        "source_id": "826a1243-63cc-4494-9c16-f2f910b539ff",
                        "source_title": "P06_EVIDENCE_MAP: Matriz de Evidencia y Tipología de Discrepancias (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Dimensión 2: Acusación No Verificada (Unsubstantiated Allegation / Narrative)",
                        "excerpt_short": "Distinguir entre 'rumor de mercado' y 'hecho verificado'. Tratar una imputación no comprobada como hecho distorsiona la respuesta de asuntos corporativos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Caso CLM-05: Denuncia de Sindicato en redes sociales",
                        "excerpt_short": "Acusación No Verificada / Desfase de Alcance... Acción recomendada: Abstenerse de respuesta pública reactiva inmediata; investigar internamente el registro de contratistas; preparar Q&A interno.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio ético y estratégico canónico de gestión de crisis en redes."
            }
        ],
        "operational_model": {
            "inputs": ["Tuit o post viral denunciando vertimientos de una planta corporativa"],
            "actors": ["Detector de Rumores", "Compuerta de Abstención de BRIDGE", "Monitor de Viralidad"],
            "steps": ["Constatación de ausencia de expediente oficial probatorio", "Etiquetado como 'Acusación No Verificada'", "Bloqueo de redacción de comunicados externos", "Apertura de ticket de verificación técnica interna", "Monitoreo del índice de reproducción SIR"],
            "states": ["Viral_Post_Ingested", "Classified_Unsubstantiated", "Public_Response_Blocked", "Internal_Inquiry_Opened"],
            "outputs": ["Ticket de verificación interna y radar de viralidad"],
            "exceptions": ["Acusaciones que escalan a medios nacionales o requerimientos del Ministerio Público"]
        },
        "entities": [
            {"entity_id": "ENT_ACUSACION_NO_VERIFICADA", "type": "tipo_de_discrepancia", "name": "Acusación No Verificada (Unsubstantiated Allegation)", "aliases": ["Unsubstantiated Narrative", "Rumor"]}
        ],
        "relations": [
            {"subject_id": "ENT_ACUSACION_NO_VERIFICADA", "predicate": "activa_politica_de", "object_id": "ENT_ABSTENCION_ESTRATEGICA", "valid_from": "2023", "valid_to": "2026", "evidence_claim_id": "P06-F35-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Estrategia comunicacional",
                "Reacción impulsiva": "Responder públicamente en Twitter desmintiendo la acusación, alimentando a los trolls y multiplicando la visibilidad del ataque por 10x.",
                "Protocolo BRIDGE de abstención": "Silencio público, investigación de hechos en terreno y preparación de Q&A bajo llave solo si la prensa seria toma el tema."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Compuertas de Abstención Módulo Actuar", "implication": "BRIDGE debe bloquear la generación de respuestas externas ante 'Acusaciones No Verificadas', instruyendo monitoreo pasivo y verificación interna.", "status": "regla_mandatoria"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F36"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-F36
    {
        "question_id": "P06-F36",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se formaliza la Matriz Afirmación-Evidencia (Claim-Evidence Matrix) de 12 campos y cómo orienta las acciones del equipo de Asuntos Corporativos?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La Matriz Afirmación-Evidencia (Claim-Evidence Matrix) se formaliza en P06_RESEARCH_DOSSIER como el artefacto analítico unificador de 12 campos estructurados que vincula la inteligencia interna con la acción estratégica: 1) ID_Afirmacion; 2) Fuente_Interna (Memoria CMF, Discurso CEO, Política); 3) Fecha_Compromiso; 4) Alcance_Declarado (Scope 1/2, filial, faena); 5) Compromiso_Texto; 6) Senal_Externa_Fuente (Resolución SMA, Newswire Factiva, ONG); 7) Fecha_Senal; 8) Entidad_Resolucion (ID canónico resuelto por Splink); 9) Tipologia_Discrepancia (Contradicción Real, Diferencia Temporal, Diferencia de Alcance, Acusación No Verificada); 10) Nivel_Confianza (Score 0.0 a 1.0); 11) Nivel_Riesgo_Reputacional (Bajo, Medio, Alto, Crítico); y 12) Accion_Recomendada_Asuntos_Corp (Aclaración proactiva, Rectificación de meta, Preparación de Q&A de crisis, o Monitoreo pasivo con abstención pública). Esta matriz no es un simple informe estático, sino una tabla operativa interactiva donde cada fila prescribe la conducta exacta que el Director de Asuntos Corporativos debe asumir para proteger la licencia social de la empresa.",
        "findings": [
            {
                "claim_id": "P06-F36-C1",
                "claim": "La Matriz Afirmación-Evidencia de 12 campos unifica la trazabilidad interna y externa prescribiendo acciones de asuntos corporativos proporcionales al riesgo.",
                "epistemic_status": "artefacto_operacional_core",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "BRIDGE Platform Architecture"},
                "evidence": [
                    {
                        "source_id": "4a9f7263-e49f-4ced-ab57-ec76ece8cc0c",
                        "source_title": "P06_RESEARCH_DOSSIER: Análisis Denso, Matrices y Entregables (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2: Entregable Específico 1: Matriz Afirmación-Evidencia (Claim-Evidence Matrix)",
                        "excerpt_short": "La Matriz Afirmación-Evidencia es el instrumento analítico central para evaluar la solidez de las posiciones corporativas frente al entorno. Se compone de 12 campos clave... orientando la acción recomendada de asuntos corporativos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Entregable específico 1 formalizado y ejemplificado en P06_RESEARCH_DOSSIER."
            }
        ],
        "operational_model": {
            "inputs": ["Base de compromisos internos", "Base de señales externas procesadas"],
            "actors": ["Motor de Cruce NLI", "Generador de Matriz BRIDGE", "Comité de Asuntos Corporativos"],
            "steps": ["Población de los 12 atributos por cada par cruzado", "Cálculo de scores de confianza y riesgo", "Prescripción de la acción comunicacional recomendada", "Despliegue interactivo en el dashboard directivo"],
            "states": ["Raw_Inputs", "Cross_Analyzed", "Matrix_Populated", "Action_Assigned"],
            "outputs": ["Matriz Afirmación-Evidencia actualizada en tiempo real"],
            "exceptions": ["Conflictos donde la evidencia externa es contradictoria entre dos medios formales"]
        },
        "entities": [
            {"entity_id": "ENT_CLAIM_EVIDENCE_MATRIX", "type": "artefacto_de_software", "name": "Matriz Afirmación-Evidencia BRIDGE de 12 Campos", "aliases": ["Claim-Evidence Matrix", "Matriz de 12 Campos"]}
        ],
        "relations": [
            {"subject_id": "ENT_CLAIM_EVIDENCE_MATRIX", "predicate": "prescribe_acciones_a", "object_id": "ENT_COMITE_ASUNTOS_CORP", "valid_from": "2024", "valid_to": "2026", "evidence_claim_id": "P06-F36-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de gestión de riesgos",
                "Reporte de clipping clásico": "Lista de titulares con sentimiento positivo/negativo sin conexión con compromisos de la empresa ni recomendación de acción.",
                "Matriz Afirmación-Evidencia BRIDGE": "Mapeo exhaustivo de 12 campos que conecta cada noticia con la frase exacta de la memoria interna y prescribe la acción directiva requerida."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric": "Campos obligatorios de la Matriz de Cruce", "denominator": "Total de atributos estructurados", "formula": "12 campos formales estandarizados"}
        ],
        "bridge_implications": [
            {"module": "Tablero Central de Cruce BRIDGE", "implication": "BRIDGE debe exponer la Matriz de 12 Campos como la interfaz principal donde los directores corporativos auditan el estado de sus compromisos.", "status": "arquitectura_core"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-F37"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P06.jsonl")
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(records)} records (P06-F31..F36) to {out_path}.")
