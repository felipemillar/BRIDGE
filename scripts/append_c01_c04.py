import json
import os
import sys

# Append P01-C01, P01-C02, P01-C03, P01-C04 to respuestas/P01.jsonl

records = [
    {
        "question_id": "P01-C01",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre mandato y fronteras de asuntos corporativos, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:09:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La discrepancia central radica en que las fuentes tradicionales reducen la función a un rol táctico de relaciones públicas, notas de prensa y apagado reactivo de incendios mediáticos, mientras que las síntesis internas y la evidencia empírica reciente la elevan a integración estratégica de riesgos ASG/geopolíticos en el C-Suite. Prevalece la versión de integración estratégica en el C-Suite, respaldada por Dircom ECE 2025 (54,4% reporte al CEO y 32,3% en Comité Ejecutivo), Page Society (Foundational, Integrator, Builder), McKinsey (Oct 2025) y los marcos chilenos obligatorios de la Ley 20.730 de Lobby y NCG 461 de la CMF.",
        "findings": [
            {
                "claim_id": "P01-C01-C1",
                "claim": "Frente a la perspectiva histórica que restringía la comunicación a tareas tácticas ejecutoras (notas de prensa y clipping manual), la evidencia empírica contemporánea (Dircom ECE 2025, Page Society y McKinsey 2025) demuestra que el mandato de asuntos corporativos se ha consolidado como un rol estratégico de integración de riesgos ASG y geopolíticos con asiento formal en el C-Suite.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "España / Global / Chile", "actor": "Dircoms y C-Suite"},
                "evidence": [
                    {
                        "source_id": "902d5a37-56ef-46c5-8fdf-97305943b0d2",
                        "source_title": "Asociación de Directivos de Comunicación (Dircom España) - El Estado de la Comunicación en España 2025",
                        "original_url": "https://www.dircom.org/actualidad/mas-de-la-mitad-de-los-dircoms-en-espana-reporta-al-maximo-ejecutivo-de-su-organizacion/",
                        "locator": "Evolución hacia Corporate Affairs e integración directiva",
                        "excerpt_short": "54,4% reporte directo al CEO y 32,3% presencia en Comité Ejecutivo, consolidando la función de Asuntos Corporativos.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "d1607ef8-5777-44bc-9a1b-417c80dffeb4",
                        "source_title": "McKinsey & Company - Upgrading Corporate Affairs for a New Geopolitical Era",
                        "original_url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección: The strategic upgrade of Corporate Affairs",
                        "excerpt_short": "Elevación de la función hacia la gestión geopolítica, regulatoria y estratégica en el C-Suite.",
                        "source_date": "2025-10-29",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Convergencia empírica entre asociaciones profesionales y consultoría de alta dirección."
            },
            {
                "claim_id": "P01-C01-C2",
                "claim": "En Chile, la NCG 461 de la CMF y la Ley N° 20.730 de Lobby institucionalizan por ley la frontera de asuntos corporativos, subordinando las declaraciones públicas a la responsabilidad legal directa ante reguladores bursátiles y de transparencia.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Estado de Chile / CMF"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Arts. 2, 3, 4 y 8",
                        "excerpt_short": "Publicidad y registro mandatorio de audiencias de intereses particulares.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco legal vinculante chileno."
            }
        ],
        "operational_model": {
            "inputs": ["Evolución histórica de la profesión", "Marcos regulatorios vinculantes", "Estructuras jerárquicas C-Suite"],
            "actors": ["CCO Tradicional", "CCO Integrador Estratégico", "Directorio", "Reguladores"],
            "steps": ["Diagnóstico del modelo actual", "Resolución de la discrepancia de rol", "Adopción de precedencia estratégica", "Integración con Legal y ESG"],
            "states": ["Discrepancia_Identificada", "Precedencia_Fijada", "Rol_Estratégico_Operativo"],
            "outputs": ["Definición canónica de fronteras de Asuntos Corporativos"],
            "exceptions": ["Atrapamiento táctico donde el CCO no logra delegar la redacción artesanal de comunicados"]
        },
        "entities": [
            {"entity_id": "ENT_CCO_INTEGRADOR", "type": "rol_estrategico", "name": "CCO as Integrator (Arthur W. Page Society)", "aliases": ["Articulador de Silos del C-Suite"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO_INTEGRADOR", "predicate": "reemplaza_modelo_de", "object_id": "CCO_Táctico_Tradicional", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-C01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque Táctico Tradicional vs Integración Estratégica",
                "Enfoque Tradicional": "Notas de prensa, relaciones con medios, eventos y clipping manual en PDF.",
                "Integración Estratégica (Prevaleciente)": "Consejero del CEO, articulador C-Suite, gestión de riesgos ASG/geopolíticos, Ley 20.730 y NCG 461."
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-C01-C1", "P01-F25-C1"],
                "difference": "Tensión entre la definición del CCO como líder estratégico del Directorio y la realidad de campo donde más del 60% de su jornada sigue atrapada en tareas tácticas reactivas.",
                "resolution": "resuelta",
                "reason": "La solución tecnológica BRIDGE atiende precisamente esta paradoja automatizando las tareas reactivas para permitir el ejercicio efectivo del rol estratégico."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Diseñar los módulos de BRIDGE asumiendo la frontera ampliada de Asuntos Corporativos que integra gestión regulatoria, legal y ASG.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C02", "P01-C03"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C02",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre mandato y fronteras de asuntos corporativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:09:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Siguen sin prueba 3 vacíos críticos: 1) métricas temporales auditadas de horas-hombre en preparación directiva (la reducción de 4h a 15m es HT-2); 2) estudios longitudinales sobre el impacto de IA en la Licencia Social; y 3) consistencia empírica entre minutas internas y actas de InfoLobby en Chile. Siete fuentes fallaron por bloqueos técnicos/paywall (Gartner x2, Global Alliance GCF Release, Gregory & Willis 2019, Page Society x2, OECD) y las fuentes comerciales son parciales al no publicar datos brutos. La validación mínima requerida es un estudio empírico en 3 fases: 15 entrevistas cualitativas (Fase 1), shadowing con cronometraje en tiempo real (Fase 2) y PoC trilateral en VPC (Fase 3).",
        "findings": [
            {
                "claim_id": "P01-C02-C1",
                "claim": "En el inventario de P01, 7 fuentes originales fallaron por bloqueos técnicos, Cloudflare, WAF o HTTP 403 (Gartner Future of Communications, Gartner for Communication Leaders, Global Alliance GCF Release, Gregory & Willis 2019 en ResearchGate, Page Society The CCO as Pacesetter, Page Society Corporate Character, y OECD Corporate Governance), mientras que las fuentes de consultoras son parciales al omitir metodologías reproducibles.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Auditoría de Fuentes del Corpus P01"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Auditoría de Fuentes Fallidas y Fuentes Parciales",
                        "excerpt_short": "Identificación de 7 fuentes fallidas por paywalls y WAF, y delimitación de fuentes comerciales parciales.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Registro exhaustivo de auditoría en el manifiesto P01."
            },
            {
                "claim_id": "P01-C02-C2",
                "claim": "La validación mínima para resolver la incertidumbre epistemológica consiste en un protocolo de campo en 3 fases: 15 entrevistas cualitativas exploratorias, shadowing de preparación cronometrado en tiempo real y despliegue de una PoC en VPC ante un panel de CCOs, CISOs y Fiscales Legales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Protocolo Metodológico"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Protocolo de Validación Mínima Requerida",
                        "excerpt_short": "Protocolo de 3 fases para resolver la incertidumbre empírica sobre tiempos, SLO y trazabilidad en lobby.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diseño metodológico formal en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Registro de fuentes fallidas", "Matriz de Knowledge Gaps", "Protocolo de validación en 3 fases"],
            "actors": ["Auditor Epistemológico", "Investigador de Campo", "Panel Trilateral CCO-CISO-Legal"],
            "steps": ["Aislamiento de fuentes fallidas y parciales", "Ejecución de entrevistas y shadowing", "Medición de tiempos reales", "Cierre de brechas empíricas"],
            "states": ["Fuentes_Auditadas", "Vacíos_Aislados", "Validación_Ejecutada", "Incertidumbre_Resuelta"],
            "outputs": ["Reporte de validación de gaps", "Base de datos de tiempos auditados"],
            "exceptions": ["Imposibilidad de acceder a fuentes corporativas primarias por acuerdos de confidencialidad estrictos"]
        },
        "entities": [
            {"entity_id": "ENT_FUENTES_FALLIDAS_P01", "type": "registro_auditoria", "name": "Registro de 7 Fuentes Fallidas en P01", "aliases": ["Paywalls y Bloqueos Técnicos P01"]}
        ],
        "relations": [
            {"subject_id": "ENT_FUENTES_FALLIDAS_P01", "predicate": "limita_alcance_de", "object_id": "Literatura_Global", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C02-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Validación", "implication": "Ejecutar la validación mínima de 3 fases para generar evidencia empírica propietaria no dependiente de fuentes con paywall.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre mediciones cuantitativas auditadas de horas invertidas en briefings en la literatura pública previa.", "minimum_validation": "Shadowing cronometrado a 10 equipos directivos en Santiago.", "priority": "alta"},
            {"gap": "sin_evidencia sobre impacto longitudinal de IA en Licencia Social.", "minimum_validation": "Estudio multianual de faenas extractivas con asistentes asistidos.", "priority": "media"}
        ],
        "next_question_ids": ["P01-C03", "P01-C04"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C03",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre mapa de usuarios, compradores y aprobadores, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:09:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La discrepancia radica en que las fuentes gremiales tradicionales (Dircom, PRSA, IABC, LCM) asumen que el CCO o Dircom es el decisor único y autosuficiente para adquirir herramientas de software, mientras que la síntesis interna B2B demuestra que la decisión está rígidamente fragmentada en una tríada donde el CCO es solo el Usuario/Comprador y el CISO y Fiscal Legal actúan como Aprobadores con poder de veto vinculante. Prevalece la versión de separación estricta de roles con veto vinculante de CISO y Legal (Hipótesis HT-3), ya que omitir los requisitos de seguridad y cumplimiento normativo conduce al bloqueo inmediato del software en la etapa de homologación.",
        "findings": [
            {
                "claim_id": "P01-C03-C1",
                "claim": "Las fuentes gremiales de comunicación asumen un comprador monolítico (el Dircom), omitiendo las exigencias de ciberseguridad y riesgo normativo; en contraste, la síntesis B2B corporativa demuestra que el CISO y el Fiscal Legal ejercen poder de veto vinculante e insoslayable sobre herramientas de IA corporativa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "C-Suite B2B"},
                "evidence": [
                    {
                        "source_id": "0d63f034-7546-4cb0-9492-f3f2d22a5785",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 7: Discrepancias en el Mapa de Decisión B2B",
                        "excerpt_short": "Discrepancia entre la visión monolítica gremial y la realidad B2B tripartita con veto vinculante del CISO y Fiscal Legal.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Dossier analítico del pilar P01."
            },
            {
                "claim_id": "P01-C03-C2",
                "claim": "Prevalece la versión de la tríada B2B con veto vinculante de CISO y Legal (HT-3): el CISO veta por riesgo de fuga de datos o uso de LLMs públicos de terceros, y el Fiscal Legal veta por responsabilidad administrativa o penal ante alucinaciones que afecten la Ley 20.730 o normativas CMF.",
                "epistemic_status": "hipotesis_diseno",
                "scope": {"time": "2026", "region": "Chile", "actor": "Gobernanza Corporativa B2B"},
                "evidence": [
                    {
                        "source_id": "038bf346-ee24-4f99-a1b7-a30ae3bc68e8",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4: Hipótesis de Trabajo HT-3 y Veto Técnico",
                        "excerpt_short": "Prevalencia de la hipótesis HT-3: CISO y Legal como aprobadores críticos con capacidad de bloqueo unilateral.",
                        "source_date": "2026-09-30",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Hipótesis de diseño B2B corroborada en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Propuesta de valor para el CCO", "Requisitos de seguridad ISO/SOC2 del CISO", "Matriz de cumplimiento de Fiscalía"],
            "actors": ["Usuario (CCO)", "Comprador (CEO/CFO)", "Aprobador Técnico (CISO)", "Aprobador Normativo (Fiscal Legal)"],
            "steps": ["Demostración de eficiencia a CCO", "Presentación de arquitectura privada a CISO", "Revisión de no-fuga y compliance con Fiscal", "Aprobación mancomunada"],
            "states": ["Prospecto_Monolítico_Rechazado", "Estructura_Tripartita_Activada", "CISO_Aprobado", "Venta_B2B_Cerrada"],
            "outputs": ["Acuerdo de nivel de servicio B2B", "Certificado de cumplimiento VPC"],
            "exceptions": ["Intento de venta directa al CCO ignorando el circuito de homologación de ciberseguridad"]
        },
        "entities": [
            {"entity_id": "ENT_VETO_VINCULANTE_CISO", "type": "mecanismo_control", "name": "Veto Vinculante de CISO y Fiscal Legal", "aliases": ["Poder de Bloqueo B2B"]}
        ],
        "relations": [
            {"subject_id": "ENT_VETO_VINCULANTE_CISO", "predicate": "determina_exito_de", "object_id": "Adopción_Tecnología_IA", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C03-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Visión Gremial Tradicional vs Síntesis B2B Corregida",
                "Visión Gremial (PRSA/Dircom/LCM)": "El CCO decide y compra solo; la evaluación se limita a usabilidad y precio.",
                "Síntesis B2B Corregida (P01 Prevaleciente)": "Estructura tripartita rígida: CCO usuario, CEO comprador, y CISO/Legal aprobadores con potestad de veto vinculante."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Construir los paquetes de venta y documentación técnica de BRIDGE dirigidos explícitamente a levantar las objeciones del CISO y Fiscal Legal.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C04", "P01-C05"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C04",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre mapa de usuarios, compradores y aprobadores, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:09:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba la falta de datos cuantitativos sobre las matrices de objeción técnica, requisitos de arquitectura de datos y tasas de rechazo aplicadas por CISOs en América Latina al evaluar herramientas de IA generativa con información confidencial corporativa. Las fuentes gremiales del sector (ECM, LCM, Dircom) son parciales por consultar solo a comunicadores ignorando a TI/Seguridad, y las fuentes de analistas de TI de Gartner fallaron por bloqueos HTTP 403. La validación mínima requiere co-diseñar una Matriz de Viabilidad de Seguridad B2B y ejecutar pruebas con un panel simétrico de CCOs, CISOs y Fiscales Legales de 12-15 corporaciones reguladas e IPSA en Chile.",
        "findings": [
            {
                "claim_id": "P01-C04-C1",
                "claim": "Existe un vacío crítico de evidencia en la literatura pública regional respecto a las políticas y parámetros de homologación técnica que utilizan los CISOs en América Latina ante soluciones de IA generativa en el C-Suite, debido a que las encuestas del sector (LCM/ECM) solo consultan a directores de comunicación.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "América Latina", "actor": "Literatura de Gestión y TI"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Knowledge Gap 3: Opacidad en Criterios de Aprobación de CISO y Legal",
                        "excerpt_short": "Vacío en literatura pública sobre matrices de objeción técnica y tasas de rechazo de CISOs en América Latina.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico formal del corpus."
            },
            {
                "claim_id": "P01-C04-C2",
                "claim": "La validación mínima para destrabar esta incertidumbre exige realizar mesas de trabajo técnicas y aplicar el cuestionario del Módulo 5 con un panel integrado simétricamente por CCOs, CISOs y Fiscales de Compliance en corporaciones chilenas de sectores altamente regulados.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Diseño Experimental B2B"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Protocolo de Validación con CISO y Legal",
                        "excerpt_short": "Validación empírica mediante entrevistas técnicas a CISOs y pruebas de concepto en VPC privada.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:09:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de validación técnica formal en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Cuestionario técnico de ciberseguridad Módulo 5", "Arquitectura de despliegue VPC", "Bases de datos de CISOs corporativos"],
            "actors": ["Arquitecto de Solución BRIDGE", "CISO Evaluador", "Fiscal Legal", "Oficial de Datos"],
            "steps": ["Identificación de CISOs de empresas IPSA", "Aplicación de pauta técnica sobre VPC y encriptación", "Tabulación de objeciones recurrentes", "Ajuste de matriz de cumplimiento"],
            "states": ["Vacío_Identificado", "Mesa_Técnica_Convocada", "Objeciones_Parametrizadas", "Matriz_Validada"],
            "outputs": ["Matriz de Viabilidad de Seguridad B2B para LatAm"],
            "exceptions": ["Confidencialidad bancaria que impida divulgar políticas de seguridad internas"]
        },
        "entities": [
            {"entity_id": "ENT_MATRIZ_OBJECIONES_CISO", "type": "herramienta_analitica", "name": "Matriz de Objeciones Técnicas de CISOs en LatAm", "aliases": ["Parámetros de Homologación B2B"]}
        ],
        "relations": [
            {"subject_id": "ENT_MATRIZ_OBJECIONES_CISO", "predicate": "resuelve_incertidumbre_de", "object_id": "HT-3", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C04-C2"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Gobernanza", "implication": "Desarrollar un whitepaper de seguridad técnica específico para CISOs basado en la Matriz de Viabilidad validada.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre matrices formales de objeción técnica y tasas de rechazo de CISOs en América Latina ante LLMs.", "minimum_validation": "Entrevistas estructuradas a 12 CISOs de grandes corporaciones chilenas.", "priority": "alta"}
        ],
        "next_question_ids": ["P01-C05", "P01-C06"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

temp_path = "respuestas/temp_c01_c04.jsonl"
with open(temp_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written {len(records)} test records to {temp_path}")
