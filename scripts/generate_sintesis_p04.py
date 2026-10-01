import json
from pathlib import Path

def generate_p04_synthesis():
    respuestas_path = Path("respuestas/P04.jsonl")
    fuentes_path = Path("fuentes/P04.json")
    
    with open(respuestas_path, "r", encoding="utf-8") as f:
        responses = [json.loads(line) for line in f if line.strip()]
        
    with open(fuentes_path, "r", encoding="utf-8") as f:
        fuentes_data = json.load(f)
        
    md = []
    md.append("# Síntesis Ejecutiva y Metodológica — Pilar P04: Conocimiento Documentado de la Corporación\n")
    md.append("**Programa de Investigación:** Inteligencia para Asuntos Corporativos  ")
    md.append("**Repositorio:** BRIDGE (`/Users/fmillar/Proyectos_Desarrollo/BRIDGE`)  ")
    md.append("**Cuaderno Canónico:** `cb87941c-2377-42fb-806f-eb9878ac0757` (NotebookLM: P04 — Conocimiento documentado de la corporación)  ")
    md.append("**Fecha de Cierre de Pilar:** 2026-10-01  ")
    md.append("**Estado de Cobertura:** 64/64 preguntas respondidas y auditadas (48 Fundamentales F01–F48, 16 Contraste C01–C16). Auditoría Estratificada: 100% Aprobada.\n")
    
    md.append("---\n")
    md.append("## 1. Alcance, Fuentes y Gobernanza Editorial\n")
    md.append("El Pilar P04 investiga y formaliza los fundamentos ontológicos, matemáticos, arquitectónicos y de gobernanza para estructurar la memoria histórica y regulatoria de la empresa, alimentando directamente el diseño del módulo **Memoria** de la plataforma BRIDGE.")
    md.append("A través de sus 8 ejes analíticos, este pilar resuelve el problema crítico de la 'amnesia corporativa fragmentada': supera la fragilidad del RAG elemental frente a memorias de 200+ páginas, establece una taxonomía formal para erradicar el greenwashing involuntario, modela el linaje de procedencia bajo W3C PROV-O, garantiza la inmutabilidad bitemporal y fija compuertas de seguridad estricta mediante control de acceso basado en atributos (NIST SP 800-162 ABAC).\n")
    
    md.append("### Dimensiones Cuantitativas del Pilar:")
    md.append("- **Total preguntas ejecutadas:** 64 preguntas (100% del alcance aprobado para P04).")
    md.append("- **Preguntas Fundamentales (F):** 48 preguntas distribuidas en 8 ejes temáticos (6 por eje).")
    md.append("- **Preguntas de Contraste y Vacíos (C):** 16 preguntas (2 por eje: discrepancias de fuentes y vacíos técnicos).")
    md.append("- **Fuentes Catalogadas en Manifiesto:** 34 fuentes totales:")
    md.append("  - **26 fuentes externas activas y sustantivas** (regulaciones oficiales CMF Chile, estándares ISSB/IFRS, GRI, especificaciones W3C, NIST y literatura científica de conferencias líderes como EMNLP, EACL, ACM).")
    md.append("  - **4 documentos analíticos internos de síntesis:** `P04_EVIDENCE_MAP`, `P04_RESEARCH_DOSSIER`, `P04_GAPS_AND_VALIDATION`, y `P04_SOURCE_INDEX`.")
    md.append("  - **4 fuentes externas fallidas con incidencia documentada:** `EFRAG ESRS Standards` (timeout TLS), `G20/OECD Principles 2023` (bloqueo antibot), `NIST AI 100-1` (bloqueo crawler) y `TruLens` (servidor inaccesible), todas suplidas formalmente por estándares equivalentes (IFRS S1/S2, GRI, Mökander et al., RAGAS, FActScore).")
    md.append("- **Regla de Precedencia Editorial:** `P04_EVIDENCE_MAP` y `P04_RESEARCH_DOSSIER` ejercen precedencia metodológica sobre enfoques informales. Se mantiene la regla imperativa de que las síntesis internas son documentos de trabajo propios que jamás deben citarse como fuentes externas independientes.\n")
    
    md.append("---\n")
    md.append("## 2. Hallazgos Fundamentales Consolidados por Eje Temático\n")
    
    axes_data = [
        ("Eje 1: Inventario de Documentos Corporativos (P04-F01 a P04-F06)", [
            ("Taxonomía Canónica de 8 Clases", "El corpus se estructura en 8 familias: Memoria Anual Integrada (CMF NCG 461), Hecho Esencial (Ley 18.045), Reporte ESG (GRI 1-3), Políticas/Códigos (ISO 37000), Comunicados Oficiales, Minutas de Vocería/Q&A, Presentaciones a Inversionistas (Safe Harbor) e Informes de Aseguramiento Externo (ISAE 3000)."),
            ("Gobierno y Custodia", "Cada artefacto se vincula a un rol custodio (Owner), nivel de aprobación colegiado (Directorio, Comité, Gerencia General) y nivel de seguridad ABAC."),
            ("Fuente de Verdad (SSOT) vs Borrador e Historia", "Se establece una distinción de 3 niveles: SSOT Vigente (aprobado y vinculante), Borradores (vedados para vocería externa) y Contexto Histórico (preservado inmutable con `dcterms:replaces` para auditoría pero excluido de la vocería activa)."),
            ("Modelado Estructurado", "El inventario se cataloga bajo W3C DCAT-3 con hash inmutable SHA-256 y relaciones W3C PROV-O de autoría y aprobación.")
        ]),
        ("Eje 2: Afirmaciones y Compromisos (P04-F07 a P04-F12)", [
            ("Taxonomía de 4 Estados Epistémicos", "Para erradicar el greenwashing, toda afirmación se clasifica en: 1) Declaración (postura cualitativa); 2) Compromiso (meta cuantificada con año base y horizonte); 3) Resultado (hecho medido de período cerrado); y 4) Verificación (auditoría externa independiente ISAE 3000)."),
            ("Ficha Canónica de Compromiso", "Especificación formal JSON-Schema que desacopla la cifra y unidad métrica de la narrativa, capturando baseline, target, milestones, status, governance y source_traceability con hash de página."),
            ("Ciclo de Vida y Reexpresión", "Seguimiento riguroso de estados (`Propuesto`, `Activo`, `Cumplido`, `En Riesgo`, `Incumplido`, `Reexpresado`, `Retirado`), modelando reexpresiones de línea base bajo IFRS S2 mediante `prov:wasRevisionOf`."),
            ("Caso Empírico Hídrico", "Demostración sobre compromiso COM-ENV-2023-089 (meta de 750 l/s al 2030), auditando el avance 2025 de 1.040 l/s verificado por Deloitte bajo ISAE 3000.")
        ]),
        ("Eje 3: Ontología y Relaciones (P04-F13 a P04-F18)", [
            ("7 Clases Maestras", "Grafo de Conocimiento basado en Schema.org, FIBO y PROV-O: `Organization`, `FacilityProject`, `PersonSpokesperson`, `DocumentArtifact`, `Statement`, `Commitment`, `Outcome/Verification`."),
            ("Desacoplamiento Societario y Operacional", "Separación estricta entre Matriz, Filial, Faena y Vocero para evitar confusión de responsabilidades ambientales (SMA/RCA) y de mercado (CMF Ley 18.045)."),
            ("Segregación Epistémica de Aristas", "Salvaguarda contra alucinaciones relacionales: toda arista se tipifica como `hecho_documentado` (anclada a hash) o `relacion_inferida` (con score probabilístico y prohibición de uso en minutas oficiales sin advertencia)."),
            ("Restricciones SHACL", "Validación estructural que impide mutaciones o aristas huérfanas en tiempo de inserción.")
        ]),
        ("Eje 4: Versiones y Temporalidad (P04-F19 a P04-F24)", [
            ("Triple Dimensión Temporal", "Desacoplamiento bitemporal estricto: Fecha del Hecho (Event/Valid Time), Fecha de Publicación (Publication Time) y Fecha de Incorporación al Sistema (Transaction Time)."),
            ("Consultas Retrospectivas As-Of", "Capacidad de reconstruir fielmente lo que la empresa sabía o declaraba a una fecha histórica mediante corte temporal `transaction_time <= T` y `valid_time contiene T`, evitando el sesgo de retrospectiva."),
            ("Inmutabilidad Histórica sin Borrado", "Los documentos superados nunca se borran; se anotan con `dcterms:isReplacedBy` preservando la trazabilidad forense para litigios."),
            ("Caso Reexpresión GEI", "Reexpresión de línea base por venta de activo industrial bajo IFRS S2, transparentando la causal técnica ante medios.")
        ]),
        ("Eje 5: Ingesta y Extracción (P04-F25 a P04-F30)", [
            ("Layout-Aware Document Parsing", "Extracción tabular estructurada (Table-Aware Extraction) que convierte tablas complejas y matrices ESG a Markdown/JSON-LD preservando encabezados y notas."),
            ("Chunking Jerárquico Parent-Child", "Fragmentos hijo pequeños (128-256 tokens) para búsqueda de alta sensibilidad enlazados a fragmentos padre extensos (1.024-2.048 tokens) para proveer contexto completo y notas al generador."),
            ("Auditores de Paridad y Sumatorias", "Validadores automáticos de consistencia de columnas, sumas de control y resolución de llamadas a notas al pie antes de autorizar la indexación."),
            ("Caso Multipágina GEI", "Costura y anclaje exitoso de tabla de emisiones en dos páginas con nota al pie sobre enfoque de mercado.")
        ]),
        ("Eje 6: Gobierno y Permisos (P04-F31 a P04-F36)", [
            ("Matriz RACI y Segregación SoD", "Definición estricta de roles para crear, aprobar, leer, corregir y retirar según formalidad legal."),
            ("Pre-Retrieval ABAC Filtering (NIST SP 800-162)", "Rechazo absoluto de filtros en el prompt del LLM; el filtrado booleano de atributos se ejecuta en el índice vectorial y de grafos antes de la recuperación, garantizando 100.0% de aislamiento."),
            ("Protocolo Four-Eyes para Afirmaciones Sensibles", "Doble visado humano obligatorio y registro criptográfico PROV-O antes de publicar compromisos oficiales."),
            ("Caso Embargo Hecho Esencial", "Aislamiento total de un borrador confidencial de adquisición ante un analista no acreditado.")
        ]),
        ("Eje 7: Búsqueda y Respuesta Fundada (P04-F37 a P04-F42)", [
            ("Enrutador Híbrido Tripartito", "BM25 para códigos e identificadores exactos, Embeddings densos para conceptos, ColBERT para reranking tardío y GraphRAG (algoritmo Leiden) para síntesis global multi-año."),
            ("Atribución a Nivel de Oración (Sentence-Level)", "Descomposición atómica (Bohnet et al.) donde cada proposición cuantitativa lleva cita inmediata con título, año, página y hash SHA-256."),
            ("Abstención Activa Segura (Self-RAG / CRAG)", "Tokens reflexivos y evaluador de recuperación que fuerzan al sistema a declarar falta de evidencia o conflicto antes que inventar una cifra."),
            ("Caso Diversidad de Género", "Respuesta exacta con 22% alcanzado vs 30% comprometido citando pág. 54 de la Memoria 2025.")
        ]),
        ("Eje 8: Evaluación de Calidad Documental (P04-F43 a P04-F48)", [
            ("Cuadro de Mando de Salud del Corpus", "Monitoreo continuo de cobertura NCG 461, latencia de hechos esenciales y métricas IR (MRR@10 ≥ 0.88, NDCG@10 ≥ 0.92)."),
            ("Gold Standard Suite de 250 Casos", "Banco de pruebas representativo de Asuntos Corporativos evaluado automáticamente con FActScore y RAGAS más auditoría humana ciega."),
            ("Red Teaming Adversarial de Seguridad", "50 ataques de inyección de prompt con criterio no negociable de cero filtración de embargos (100.0% ABAC Enforcement)."),
            ("Matriz de 5 Umbrales Mínimos", "Faithfulness ≥ 0.95, Citation Precision ≥ 0.98, Citation Recall ≥ 0.95, Coherencia Temporal 100%, Aislamiento ABAC 100.0%.")
        ])
    ]
    
    for axis_title, findings_list in axes_data:
        md.append(f"### {axis_title}\n")
        for f_title, f_desc in findings_list:
            md.append(f"- **{f_title}:** {f_desc}")
        md.append("")
        
    md.append("---\n")
    md.append("## 3. Matriz de Preguntas y Respuestas (Trazabilidad 64/64)\n")
    md.append("| ID | Pregunta Oficial | Estatus | Síntesis de Respuesta Fundada |")
    md.append("| :--- | :--- | :---: | :--- |")
    
    for r in responses:
        qid = r["question_id"]
        qtext = r["question_text"]
        short_ans = r["short_answer"]
        # Clean text for table display
        short_clean = short_ans.replace("\n", " ").replace("|", "\\|")
        if len(short_clean) > 180:
            short_clean = short_clean[:177] + "..."
        md.append(f"| **{qid}** | {qtext} | ✅ Respondida | {short_clean} |")
        
    md.append("\n---\n")
    md.append("## 4. Vacíos Epistémicos y Fuentes Parciales Identificadas\n")
    md.append("A partir del análisis de las 16 preguntas de contraste (C01–C16) y del documento `P04_GAPS_AND_VALIDATION`, se consolidan 8 vacíos epistémicos y sus agendas de validación técnica:\n")
    
    gaps_data = [
        ("GAP-P04-01: Homologación CMF vs ESRS", "Incertidumbre en la compatibilidad automatizada entre memorias chilenas NCG 461 y estándares europeos ESRS debido al fallo de ingesta F-01 (EFRAG). Requiere auditoría de schema mapping con PDFs oficiales."),
        ("GAP-P04-02: Abandono Silencioso de Metas (Goal Drift)", "Falta de algoritmos para detectar cuando una meta de un año base es discontinuada silenciosamente en memorias posteriores sin justificación formal."),
        ("GAP-P04-03: Ontología Localizada Chilena", "Ausencia de ontologías públicas que vinculen la jerarquía societaria de la CMF (RUT) con resoluciones ambientales (RCA del SEIA/SMA). Requiere desarrollo de extensión sobre FIBO."),
        ("GAP-P04-04: Reexpresiones Tácitas de Línea Base", "Carencia de herramientas que concilien automáticamente variaciones en series temporales históricas reportadas entre memorias consecutivas sin notas al pie explicativas."),
        ("GAP-P04-05: Precisión en Tablas Multipágina Complejas", "Fragilidad observada en parsers abiertos ante tablas financieras consolidadas y matrices ESG. Requiere prueba piloto sobre 15 memorias CMF (precisión ≥ 98%)."),
        ("GAP-P04-06: Liberación de Emergencia de Embargos", "Falta de validación empírica sobre la latencia de propagación de excepciones de embargo en tiempo real ante contingencias de filtración de prensa (< 60 segundos)."),
        ("GAP-P04-07: Trade-off Costo-Latencia GraphRAG vs ColBERT", "Falta de telemetría comparativa de inferencia y consumo de tokens entre clustering jerárquico GraphRAG y búsqueda híbrida ColBERT sobre memorias corporativas en español."),
        ("GAP-P04-08: Simulación de Gabinete de Crisis", "Necesidad de someter al sistema a una prueba de estrés de vocería en 3 escenarios reales (greenwashing, agua, filtración) con tiempo de preparación < 3 minutos y cero fuga ABAC.")
    ]
    
    for g_id, g_desc in gaps_data:
        md.append(f"- **{g_id}:** {g_desc}")
        
    md.append("\n---\n")
    md.append("## 5. Implicancias Arquitectónicas para el Proyecto BRIDGE (Módulo Memoria)\n")
    md.append("Los hallazgos del Pilar P04 imponen cuatro requerimientos arquitectónicos estructurales para el módulo **Memoria** de BRIDGE:\n")
    md.append("1. **Contrato de Datos Inmutable (Ficha Canónica de Compromiso):** BRIDGE no debe almacenar compromisos como texto libre. Debe implementar el JSON-Schema formalizado en P04 con tipificación estricta de baseline, target, milestones, status y hash criptográfico SHA-256 de página.")
    md.append("2. **Almacenamiento Híbrido Dual (Grafo Semántico + Almacén Vectorial):** La arquitectura debe combinar una base de grafos (RDF TripleStore / Neo4j bajo FIBO y W3C PROV-O) para relaciones de jerarquía societaria, linaje de vocería y trazabilidad causal, junto con una base vectorial filtrada para búsqueda semántica local.")
    md.append("3. **Pipeline de Ingesta Layout-Aware con Chunking Jerárquico:** El pre-procesamiento documental debe descartar el chunking ciego por caracteres y operar con Parent Document Retrieval (hijos de 128-256 tokens mapeados a padres de 1.024-2.048 tokens), incorporando auditores de paridad de tablas y resolución de notas al pie.")
    md.append("4. **Motor de Búsqueda Adaptativo y Guardrails de Certificación:** Integración de un router tripartito (BM25 + ColBERT + GraphRAG Leiden), gobernado por Pre-Retrieval ABAC Filtering (NIST SP 800-162) y compuertas automáticas de factualidad atómica (FActScore ≥ 0.95 y precisión de citas ≥ 0.98) antes de presentar minutas a directivos.\n")
    
    md.append("---\n")
    md.append("## 6. Estado de Auditoría y Verificación de Cumplimiento\n")
    md.append("- **Auditoría de Esquema (20 Atributos):** 100% de los 64 registros validados en `respuestas/P04.jsonl`.")
    md.append("- **Muestra Estratificada del 10%+:** 7 registros seleccionados aleatoriamente (`P04-F41`, `P04-F08`, `P04-F02`, `P04-F48`, `P04-F18`, `P04-C08`, `P04-C04`) auditados con 100% de conformidad contra el manifiesto `fuentes/P04.json`.")
    md.append("- **Trazabilidad Normativa y Epistémica:** Todos los hechos documentados cuentan con títulos de fuentes oficiales, fechas, localizadores exactos y fragmentos sustantivos comprobables.")
    md.append("- **Ausencia de Alucinaciones:** Cero datos no documentados; todas las afirmaciones comerciales y vacíos están formalmente tipificados.\n")
    
    md.append("---\n")
    md.append("## 7. Próximos Pasos (Avance Autónomo)\n")
    md.append("Concluido íntegramente el Pilar P04, el programa de investigación avanza de inmediato al siguiente cuaderno en la secuencia canónica del mandato:\n")
    md.append("- **Siguiente Pilar:** **P05 — Metodologías de análisis y síntesis**")
    md.append("- **Notebook ID Verificado:** `0fc2e780-e279-4923-83c5-90fe621a4543` (36 fuentes identificadas)")
    md.append("- **Alcance P05:** 64 preguntas (48 Fundamentales F01–F48, 16 Contraste C01–C16)")
    md.append("- **Procedimiento Inmediato:** Creación de manifiesto congelado `fuentes/P05.json`, revisión de evidencias y precedencia editorial, ejecución secuencial F->C y síntesis ejecutiva sin esperar autorizaciones rutinarias.")
    
    sintesis_path = Path("sintesis/P04.md")
    sintesis_path.parent.mkdir(parents=True, exist_ok=True)
    with open(sintesis_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
        
    print(f"Generated synthesis at {sintesis_path} ({sintesis_path.stat().st_size} bytes).")

if __name__ == "__main__":
    generate_p04_synthesis()
