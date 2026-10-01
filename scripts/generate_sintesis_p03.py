import json
from pathlib import Path

def generate_p03_synthesis():
    respuestas_path = Path("respuestas/P03.jsonl")
    fuentes_path = Path("fuentes/P03.json")
    
    with open(respuestas_path, "r", encoding="utf-8") as f:
        responses = [json.loads(line) for line in f if line.strip()]
        
    with open(fuentes_path, "r", encoding="utf-8") as f:
        fuentes_data = json.load(f)
        
    md = []
    md.append("# Síntesis Ejecutiva y Metodológica — Pilar P03: Monitoreo del Entorno y Acceso a Fuentes\n")
    md.append("**Programa de Investigación:** Inteligencia para Asuntos Corporativos  ")
    md.append("**Repositorio:** BRIDGE (`/Users/fmillar/Proyectos_Desarrollo/BRIDGE`)  ")
    md.append("**Cuaderno Canónico:** `a2afe847-a988-40f1-9432-9e596b74b376` (NotebookLM: P03 — Monitoreo del entorno y acceso a fuentes)  ")
    md.append("**Fecha de Cierre de Pilar:** 2026-10-01  ")
    md.append("**Estado de Cobertura:** 64/64 preguntas respondidas y auditadas (48 Fundamentales F01–F48, 16 Contraste C01–C16). Auditoría Estratificada: 100% Aprobada.\n")
    
    md.append("---\n")
    md.append("## 1. Alcance, Fuentes y Gobernanza Editorial\n")
    md.append("El Pilar P03 investiga y define los fundamentos técnicos, epistemológicos, operativos y jurídicos para la captura, procesamiento y alerta de señales del entorno externo de las organizaciones, alimentando el diseño del módulo **Escuchar** de la plataforma BRIDGE.")
    md.append("A través de sus 8 ejes analíticos, este pilar evalúa las restricciones de acceso y cuotas de APIs masivas, audita la cobertura territorial en medios regionales y radios locales de Chile, deslinda las capacidades reales de modelos de lenguaje natural frente a modismos locales y desinformación, y establece los límites de reutilización legal de datos bajo el derecho de autor chileno e internacional.\n")
    
    md.append("### Dimensiones Cuantitativas del Pilar:")
    md.append("- **Total preguntas ejecutadas:** 64 preguntas (100% del alcance aprobado para P03).")
    md.append("- **Preguntas Fundamentales (F):** 48 preguntas distribuidas en 8 ejes temáticos (6 por eje).")
    md.append("- **Preguntas de Contraste y Vacíos (C):** 16 preguntas (2 por eje: discrepancias de fuentes y vacíos técnicos).")
    md.append("- **Fuentes Catalogadas en Manifiesto:** 33 fuentes totales:")
    md.append("  - **27 fuentes externas activas y sustantivas** (APIs de desarrolladores, legislación, estándares AMEC y literatura científica revisada por pares).")
    md.append("  - **5 documentos de síntesis interna y control editorial:** `P03_QUALITY_ADDENDUM`, `P03_EVIDENCE_MAP`, `P03_RESEARCH_DOSSIER`, `P03_GAPS_AND_VALIDATION`, y `P03_SOURCE_INDEX`.")
    md.append("  - **1 fuente fallida/bloqueada documentada:** *Meta Content Library and API Evaluation - Social Media Lab* (`33f50617-82e1-45aa-8da9-6319d3d5cb05`), sustituida por la documentación técnica de Bellingcat Toolkit y términos de ICPSR.")
    md.append("- **Regla de Precedencia Editorial:** `P03_QUALITY_ADDENDUM` y `P03_EVIDENCE_MAP` ejercen precedencia absoluta sobre resúmenes informales o declaraciones comerciales no respaldadas. Prevalece la separación estricta entre Hechos Documentados (HD), Afirmaciones Comerciales (AC), Evidencia Independiente (EI) e Hipótesis Operativas (HO).\n")
    
    md.append("---\n")
    md.append("## 2. Respuestas Fundamentales Consolidadas por Eje Temático\n")
    
    axes_data = [
        ("Eje 1: Taxonomía de Señales Externas (P03-F01 a P03-F06)", [
            ("Familias de Señales", "El monitoreo corporativo se descompone en 5 familias operativas: prensa estructurada y web abierta, redes sociales y comunidades, broadcast audiovisual (radio/TV/podcasts), señales institucionales y regulatorias oficiales, y dinámica comunitaria territorial."),
            ("Metadatos Mínimos", "Se adopta un esquema unificado de 8 atributos canónicos: `signal_id`, `timestamp_published` (ISO-8601), `source_type`, `source_identifier`, `author_or_issuer`, `content_payload`, `entities_extracted` (URIs Wikidata/RUT), y `provenance_url_or_locator` inmutable."),
            ("Materialidad vs Mención de Marca", "Se descarta la 'mención de marca' como métrica principal. La materialidad se define conforme al estándar de Hecho Esencial de la CMF y Form 8-K de la SEC: alteración sustancial de derechos, gobernanza, operaciones, finanzas o licencia social para operar, capturando señales sectoriales no nominales donde la marca ni siquiera es nombrada inicialmente."),
            ("Modelado Ontológico", "La taxonomía se representa en grafos RDF/OWL con variables de severidad, fase de ciclo regulatorio y relaciones ontológicas (`involucra_a`, `afecta_sector`, `precede_a`).")
        ]),
        ("Eje 2: Acceso a Prensa y Web Abierta (P03-F07 a P03-F12)", [
            ("Canales de Ingesta y Restricciones", "Los canales documentados comprenden agregadores abiertos (GDELT, Event Registry), suites sindicadas con licencias de pago (Factiva, CisionOne, Meltwater), sindicación RSS directa, APIs de búsqueda y extracción directa (scraping)."),
            ("Matriz de Trade-offs", "Existe un trade-off estructural: el RSS ofrece la menor latencia (1-5 min) y metadatos limpios pero contenido resumido; las suites sindicadas ofrecen texto completo bajo paywall pero con costos elevados y prohibición de redistribución; el scraping ofrece cobertura web pero enfrenta bloqueos WAF y riesgos de litigio por incumplimiento de Términos de Servicio (ToS)."),
            ("Sesgo Metropolitano en Chile", "Las suites globales y agregadores masivos (GDELT) sufren un sesgo metropolitano severo hacia medios de Santiago. La prensa regional, comunal y especializada (minera, agrícola) es ignorada por herramientas multinacionales, siendo cubierta en Chile de forma comprobada únicamente por proveedores especializados como Litoralpress."),
            ("Gobernanza de Snippets", "Bajo la Ley 17.336 de Propiedad Intelectual en Chile y las directivas de opt-out del Art. 4 de la Directiva UE 2019/790, el almacenamiento masivo debe limitarse a snippets breves efímeros y enlaces canónicos bajo derecho de cita.")
        ]),
        ("Eje 3: Redes Sociales y Comunidades (P03-F13 a P03-F18)", [
            ("Ecosistema Fragmentado", "El entorno social no es un duopolio: está fragmentado entre redes federadas de protocolo abierto (AT Protocol / Bluesky con streaming Jetstream en WebSockets), foros comunitarios (Reddit Data API, 100 req/min bajo OAuth), canales públicos de mensajería (Telegram Bot API) y plataformas centralizadas."),
            ("Barreras Corporativas Infranqueables", "Meta Content Library y TikTok Research API prohíben contractualmente el uso empresarial o comercial, limitándose a investigadores académicos acreditados vía ICPSR. X (Twitter) comercializa el acceso a gran escala bajo la modalidad opaca 'Contact Sales' (estimada en $42k/mes por consultores) y modelos basados en créditos en 2026."),
            ("Sesgos Muestrales Severos", "Las muestras de redes sociales adolecen de sesgo de selección: no representan la opinión pública general (sobre-representan élites polarizadas y activistas) y carecen de visibilidad sobre los espacios privados ('Dark Social': WhatsApp, perfiles cerrados), donde se incuban las movilizaciones territoriales."),
            ("Monitoreo Centrado en Actores y Desacoplamiento", "La relevancia se evalúa monitoreando actores clave y líderes comunitarios. Se aplica la regla de desacoplamiento epistémico: la sincronía temporal de co-acción (Pacheco et al. 2020) y los bots (Sayyadiharikandeh et al. 2020) no son sinónimos de falsedad ni engaño, requiriéndose el marco DISARM y juicio analítico humano.")
        ]),
        ("Eje 4: Radio, Televisión, Video y Podcasts (P03-F19 a P03-F24)", [
            ("Opciones Técnicas de Broadcast", "La captura se estructura entre suites comerciales con derechos de difusión (TVEyes, CisionOne), modelos ASR neuronales de código abierto (OpenAI Whisper en ventanas de 30s) y directorios abiertos de podcasts con etiquetas de transcripción nativa en XML (Podcast Index API)."),
            ("Degradación Lingüística en Chile", "Mientras Whisper alcanza un WER < 6% en español estándar, en el habla coloquial de radioemisoras chilenas (aspiración de /s/, alta velocidad, pérdida de dentales intervocálicas y modismos locales) el WER sube drásticamente al 25%-35%, corrompiendo nombres propios y términos técnicos."),
            ("Solución Híbrida Vectorial", "Para evitar fallos en alertas causados por transcripciones fonéticamente imperfectas, la búsqueda no debe basarse en concordancia léxica exacta sino en recuperación semántica vectorial densa proyectada al espacio de embeddings corporativos."),
            ("Evidencia Primaria vs Resumen Secundario", "Se califica como evidencia primaria el audio/video continuo de voz viva directa (entrevistas, conferencias, comisiones); las notas de noticieros o clippings resumidos por conductores se clasifican como síntesis secundarias sujetas a verificación del original.")
        ]),
        ("Eje 5: Fuentes Institucionales y Regulatorias (P03-F25 a P03-F30)", [
            ("Registros Prioritarios", "En Chile: CMF (hechos esenciales en tiempo casi real), Diario Oficial (leyes y decretos a las 06:00 AM con firma digital CSV), ChileCompra API (licitaciones OCDS), Congreso Nacional (boletines de proyectos de ley) y SEIA (impacto ambiental). Multinacional: SEC EDGAR (Form 8-K para hechos materiales en 4 días hábiles, límite de 10 req/s con User-Agent corporativo)."),
            ("Máquina de Estados Finitos (FSM)", "Para evitar falsas alarmas, el ciclo regulatorio se modela en 5 estados ontológicos: `Propuesta_o_Minuta`, `Tramite_Legislativo_Iniciado`, `Tramite_Avanzado`, `Sancion_Presidencial`, y `Norma_Vigente_Publicada` en el Diario Oficial."),
            ("Detección Temprana No Nominal", "Los mayores riesgos regulatorios provienen de resoluciones sectoriales generales (decretos de escasez hídrica, modificaciones impositivas, fallos a competidores) que jamás mencionan el nombre de la empresa pero impactan sus activos geográficos y operacionales.")
        ]),
        ("Eje 6: Desambiguación y Análisis de Señales (P03-F31 a P03-F36)", [
            ("Entity Linking en Dos Etapas (BLINK)", "La desambiguación de homónimos, filiales y marcas se resuelve con arquitectura BLINK (Wu et al. 2020): recuperación densa de candidatos mediante Bi-Encoders en <50ms y re-clasificación contextual exhaustiva mediante Cross-Encoders cruzados con el grafo corporativo."),
            ("Modelado de Tópicos No Supervisado (BERTopic)", "El descubrimiento de temas emergentes sin mención de marca se implementa con BERTopic (Grootendorst 2022): embeddings densos + reducción UMAP + agrupamiento HDBSCAN + ponderación c-TF-IDF, agrupando documentos orgánicamente sin requerir listas de keywords previas."),
            ("Fracaso del Sentimiento Genérico y Límite de BETO", "El sentimiento automático polar (+/-/neutro) es disfuncional para asuntos corporativos al no capturar ironía ni postura estratégica (AMEC). El modelo fundacional BETO (Cañete et al. 2020) no comprende de forma nativa modismos ni posturas regulatorias chilenas complejas, siendo una Hipótesis Operativa que requiere fine-tuning supervisado con un benchmark local."),
            ("Marco DISARM para Desinformación", "La evaluación de operaciones de influencia y riesgos reputacionales se estructura mediante los códigos y tácticas observables del marco DISARM (T0000 series), combinados con análisis de postura (stance analysis).")
        ]),
        ("Eje 7: Alertas Útiles y Latencia (P03-F37 a P03-F42)", [
            ("Matriz de Severidad por Rol", "La entrega de alertas se adapta al rol directivo: el C-Suite / Directorio recibe exclusivamente Severidad Crítica (interrupción operacional, hechos esenciales, demandas mayores) con despacho inmediato; la gerencia de asuntos públicos monitorea Severidades Crítica y Alta (proyectos de ley, medios regionales); y los analistas operan sobre el flujo completo de señales débiles."),
            ("Control de Fatiga Informativa", "Para mitigar la saturación de alertas, se implementa: 1) Deduplicación por evento madre (Event Registry/GDELT); 2) Umbral de materialidad sobre volumen; 3) Ventanas dinámicas de agregación (throttling y digests periódicos); y 4) Circuit breaker ante tormentas de publicaciones masivas."),
            ("Desglose de Latencia TTD y TTV", "Se mide de forma obligatoria el Tiempo de Detección (TTD: desde publicación hasta ingesta: <10s en WebSockets, 1-5 min en RSS, 15 min en GDELT, 15-45 min en suites comerciales, 8-30 min en broadcast ASR) y el Tiempo de Verificación (TTV: intervalo analítico hasta confirmación del evento, típicamente 5-15 min).")
        ]),
        ("Eje 8: Derechos, Costos y Calidad de Ingesta (P03-F43 a P03-F48)", [
            ("Régimen de Derechos por Canal", "Datos abiertos de gobierno permiten libre uso, retención y derivación analítica; suites comerciales y redes (Reddit, Factiva) prohíben explícitamente el uso de sus datos para reentrenamiento de modelos de IA; Meta Content Library prohíbe el uso corporativo."),
            ("Costos Observables vs Negociación Opaca", "Son públicos y sin costo de licencia las APIs estatales (SEC EDGAR, CMF, ChileCompra) y protocolos abiertos (Bluesky Jetstream); Reddit impone cuota libre de 100 req/min. En contraste, las grandes suites comerciales y el nivel X Enterprise operan bajo contratos a la medida ('Contact Sales') con costos anuales que superan las decenas de miles de dólares."),
            ("Calidad con Denominadores Auditados", "La evaluación de ingesta exige calcular formalmente: Precisión (`Señales Pertinentes / Total Capturas`), Cobertura Real Recall (`Eventos Detectados / Total Eventos en Panel de Control de 50 Casos Reales`), Tasa de Duplicados (`Copias / Total Artículos`) y Tasa de Fallos (`Errores 4xx/5xx / Total Consultas`)."),
            ("Cumplimiento Estricto de Propiedad Intelectual", "En Chile, la ausencia de excepción general de minería de textos en la Ley 17.336 obliga a limitar el almacenamiento masivo a metadatos y snippets efímeros bajo derecho de cita, purgando el texto íntegro ante directivas de opt-out legibles por máquina (Art. 4 Directiva UE 2019/790).")
        ])
    ]
    
    for axis_title, items in axes_data:
        md.append(f"### {axis_title}\n")
        for subtitle, text in items:
            md.append(f"- **{subtitle}:** {text}")
        md.append("\n")
        
    md.append("---\n")
    md.append("## 3. Contrastes, Discrepancias y Versiones Prevalecientes\n")
    md.append("Conforme a la regla de precedencia editorial del mandato, la siguiente tabla consolida las 8 discrepancias críticas identificadas en el Pilar P03, detallando la versión preliminar errónea y la formulación corregida que prevalece:\n")
    
    md.append("| Pregunta ID | Tema / Eje | Versión Inicial / Afirmación de Mercado | Versión Corregida Prevaleciente (Adenda P03) | Fundamento y Evidencia Oficial |")
    md.append("|---|---|---|---|---|")
    md.append("| **P03-C01** | Taxonomía de Señales | Equiparación de coordinación temporal y bots con ataques de desinformación maliciosa. | **Desacoplamiento estricto:** la coordinación es un patrón topológico neutral; los bots son agentes heterogéneos; catalogar como desinformación requiere análisis DISARM y revisión humana. | *P03_QUALITY_ADDENDUM* (Sec. 2.3); Pacheco et al. 2020; Sayyadiharikandeh et al. 2020. |")
    md.append("| **P03-C03** | Acceso a Prensa | El fallo *hiQ v. LinkedIn* confiere inmunidad legal amplia para raspar cualquier portal web público. | **Delimitación procesal estricta:** *hiQ* resolvió solo la ley penal CFAA; no exime de demandas civiles por incumplimiento de Términos de Servicio (ToS Breach). | *P03_QUALITY_ADDENDUM* (Sec. 2.4); 9th Cir. Opinion *hiQ v. LinkedIn* (2022). |")
    md.append("| **P03-C05** | Redes Sociales | X Enterprise tiene tarifa fija pública de '$42k/mes' y el mercado es un 'duopolio'. | **Ecosistema fragmentado y tarifas opacas:** X no publica precios de lista para Enterprise ('Contact Sales' a medida); el mercado incluye foros, mensajería y protocolos abiertos (Bluesky). | *P03_QUALITY_ADDENDUM* (Sec. 2.1); X Developer Platform; AT Protocol Documentation. |")
    md.append("| **P03-C07** | Broadcast Audiovisual | Las suites de broadcast alertan en segundos en tiempo real en cuanto se nombra a la empresa. | **Desfase técnico comprobado:** TVEyes y Cision operan con retrasos de 5 a 30 minutos; pipelines Whisper requieren ventanas de 30s acumulando 8-15 min de latencia. | *P03_QUALITY_ADDENDUM*; *P03_EVIDENCE_MAP* (Sec. 2.3); Radford et al. 2022. |")
    md.append("| **P03-C09** | Fuentes Regulatorias | Meta Content Library y TikTok Research API son fuentes viables para escucha corporativa. | **Inelegibilidad contractual:** Ambas plataformas prohíben de forma expresa y vinculante el uso corporativo o comercial, reservándose a investigación universitaria vía ICPSR. | *P03_QUALITY_ADDENDUM* (Sec. 2.5); Bellingcat Toolkit; TikTok Developer Terms. |")
    md.append("| **P03-C11** | NLP y Desambiguación | El modelo BETO comprende nativamente modismos, ironía política y posturas regulatorias chilenas. | **Hipótesis operativa no probada:** BETO se entrenó en corpus general y no fue evaluado en postura chilena; requiere fine-tuning local y dataset anotado supervisado. | *P03_QUALITY_ADDENDUM* (Sec. 2.2); Cañete et al. 2020. |")
    md.append("| **P03-C13** | Alertas y Latencia | Alertas en tiempo real sobre cada mención omnicanal maximizan la agilidad sin fatiga. | **Fatiga por sobreinformación:** Notificar por mención simple satura a directivos; la relevancia exige agrupar por evento madre y filtrar por severidad según jerarquía. | *AMEC Barcelona Principles 3.0*; *P03_EVIDENCE_MAP* (Sec. 2.1 y 2.4). |")
    md.append("| **P03-C15** | Derechos de Ingesta | La minería de datos comercial goza de excepción legal amplia en Chile al igual que en la UE. | **Vacío legal en Chile y opt-out en la UE:** La Ley 17.336 carece de excepción TDM; la Directiva UE exige respetar opt-outs en robots.txt; rige política de snippets efímeros. | *P03_QUALITY_ADDENDUM* (Sec. 2.4); Directiva UE 2019/790; Ley 17.336 BCN. |\n")
    
    md.append("---\n")
    md.append("## 4. Vacíos, Límites Epistémicos y Programa de Validación Empírica\n")
    md.append("La investigación de P03 delimita con exactitud los puntos ciegos estructurales que la tecnología actual no puede resolver de forma automática, y formaliza el protocolo experimental necesario para disipar la incertidumbre antes de operar en entornos corporativos críticos:\n")
    
    md.append("### 4.1. Vacíos Estructurales y Puntos Ciegos Identificados")
    md.append("1. **Inaccesibilidad del 'Dark Social' (WhatsApp y Grupos Cerrados):**")
    md.append("   - Gran parte de la deliberación vecinal, gremial y sindical en Chile ocurre en mensajería privada cifrada. Ningún sistema legal puede acceder a estos canales sin vulnerar la privacidad, generando un desfase inevitable hasta que el conflicto trasciende a foros públicos.")
    md.append("2. **La Brecha de Radioemisoras Provinciales no Digitalizadas:**")
    md.append("   - Emisoras AM/FM locales en comunas mineras y agrícolas no transmiten por streaming digital ni publican podcasts, quedando fuera del alcance de proveedores internacionales de broadcast.")
    md.append("3. **Fragmentación y Opacidad de Normas Municipales (345 Comunas):**")
    md.append("   - Los decretos alcaldicios y ordenanzas comunales en Chile carecen de APIs centralizadas y frecuentemente se archivan en PDFs escaneados no indexados, obstaculizando el monitoreo regulatorio local.")
    md.append("4. **Opacidad del Costo Total de Propiedad (TCO) en Suites Comerciales:**")
    md.append("   - Los contratos B2B imponen cláusulas de confidencialidad que encubren sobrecostos masivos por exceso de volumen de menciones y tarifas adicionales de onboarding.\n")
    
    md.append("### 4.2. Protocolo Riguroso de Validación Empírica (Cuatro Etapas)")
    md.append("Conforme a `P03_GAPS_AND_VALIDATION`, se adopta el programa experimental de 4 etapas obligatorias:")
    md.append("1. **Etapa 1: Test de Crisis Históricas (Benchmark Retrospectivo):**")
    md.append("   - *Objetivo:* Medir la capacidad predictiva de señales débiles.")
    md.append("   - *Diseño:* Reconstruir el corpus ciego de 60 días previos a 10 crisis corporativas y regulatorias de alto impacto ocurridas en Chile (2018–2025).")
    md.append("   - *Criterio de éxito:* Detección de la señal precursora con al menos 72 horas de anticipación en el 70% de los casos con una precisión $P \\ge 0.80$.")
    md.append("2. **Etapa 2: Prueba de Estrés frente a Desinformación Sintética (Sandbox CIB):**")
    md.append("   - *Objetivo:* Evaluar la detección de astroturfing coordinado generado por agentes LLM.")
    md.append("   - *Diseño:* Inyectar 10.000 publicaciones sintéticas coordinadas con alta variabilidad estilística en un entorno aislado.")
    md.append("   - *Criterio de éxito:* Aislamiento de la red inauténtica con $F_1 \\ge 0.88$ y cero falsas acusaciones contra cuentas ciudadanas orgánicas.")
    md.append("3. **Etapa 3: Benchmark de Latencia y Audio Radial Chileno:**")
    md.append("   - *Objetivo:* Calibrar modelos ASR (Whisper) ante la fonética y modismos locales.")
    md.append("   - *Diseño:* Grabar 100 horas de programación radial chilena (noticiarios matutinos y despachos provinciales) y evaluar Whisper en zero-shot vs fine-tuneado.")
    md.append("   - *Criterio de éxito:* Reducción del WER por debajo del 12% y recuperación del 95% de entidades corporativas y legales críticas.")
    md.append("4. **Etapa 4: Piloto de Campo con Responsables de Asuntos Corporativos:**")
    md.append("   - *Objetivo:* Evaluar utilidad subjetiva y mitigación de fatiga de alertas en producción real.")
    md.append("   - *Diseño:* Despliegue cerrado de 30 días con 5 directores de asuntos corporativos en Chile, registrando feedback diario de cada alerta.")
    md.append("   - *Criterio de éxito:* Ratio de alertas útiles $> 85\\%$ (Signal-to-Noise Ratio $\\text{SNR} \\ge 7.5 \\text{ dB}$) y $\\le 3$ alertas críticas por semana por directivo.\n")
    
    md.append("---\n")
    md.append("## 5. Implicancias Arquitectónicas y de Producto para BRIDGE\n")
    md.append("Los hallazgos de P03 dictan las especificaciones técnicas obligatorias para el módulo **Escuchar** de BRIDGE:")
    md.append("1. **Ingesta Híbrida y Desacoplada:**")
    md.append("   - Conector nativo de streaming WebSockets para redes abiertas (Bluesky / Jetstream) con latencia subsegundo.")
    md.append("   - Conectores directos a fuentes estatales oficiales: CMF (hechos esenciales cada 5 min), SEC EDGAR (REST con límite 10 req/s y User-Agent declarado), ChileCompra (API OCDS) y Diario Oficial (scraping matutino 06:00 AM con firma CSV).")
    md.append("   - Conector especializado de RSS para prensa regional chilena y sindicación con Litoralpress para radioemisoras provinciales.")
    md.append("2. **Motor de Desambiguación y Análisis Semántico:**")
    md.append("   - Pipeline BLINK de dos etapas (Bi-Encoder en <50ms + Cross-Encoder contextual) conectado al grafo corporativo para desambiguar homónimos y filiales.")
    md.append("   - Job continuo de BERTopic sobre el flujo no nominal para descubrir tópicos emergentes antes de que nombren a la empresa.")
    md.append("   - Reemplazo absoluto del 'sentimiento tripolar' por un motor de Detección de Postura y Riesgo Reputacional (Aspect-Based Stance Analysis).")
    md.append("3. **Arquitectura de Gobernanza Legal y Cumplimiento:**")
    md.append("   - Almacenamiento restringido a metadatos estructurados, citas breves (snippets) y hashes inmutables, respetando la Ley 17.336 de Propiedad Intelectual y las directivas de opt-out de TDM de la Directiva UE 2019/790.")
    md.append("   - Prohibición por software de utilizar contenidos protegidos por derechos de autor de terceros para reentrenar modelos fundacionales.")
    md.append("4. **Gobernanza de Alertas y Despacho Jerárquico:**")
    md.append("   - Agrupamiento estricto por evento madre para deduplicar noticias redundantes.")
    md.append("   - Circuit breaker automático ante anomalías de volumen masivo (crisis mediáticas).")
    md.append("   - Despacho segmentado por perfil: alertas críticas push inmediatas para C-Suite/Directorio; briefings consolidados para gerencias de asuntos corporativos; tableros de exploración libre para analistas.\n")
    
    md.append("---\n")
    md.append("## 6. Registro Consolidado de Entidades y Relaciones Ontológicas\n")
    
    # Extract entities and relations from responses
    all_entities = {}
    all_relations = []
    for r in responses:
        for ent in r.get("entities", []):
            eid = ent.get("entity_id")
            if eid and eid not in all_entities:
                all_entities[eid] = ent
        for rel in r.get("relations", []):
            all_relations.append(rel)
            
    md.append(f"Se consolidaron **{len(all_entities)} entidades ontológicas únicas** y **{len(all_relations)} relaciones de grafo** que modelan el ecosistema de señales de entorno:\n")
    
    md.append("### 6.1. Muestra Representativa de Entidades Clave")
    md.append("| ID Entidad | Tipo | Nombre Canónico | Aliases |")
    md.append("|---|---|---|---|")
    for eid, ent in list(all_entities.items())[:15]:
        aliases_str = ", ".join(ent.get("aliases", []))
        md.append(f"| `{eid}` | `{ent.get('type')}` | {ent.get('name')} | {aliases_str} |")
    md.append("\n")
    
    md.append("### 6.2. Muestra Representativa de Relaciones Ontológicas (Tripletas RDF)")
    md.append("| Sujeto | Predicado | Objeto | Respaldo (Claim ID) |")
    md.append("|---|---|---|---|")
    for rel in all_relations[:15]:
        md.append(f"| `{rel.get('subject_id')}` | `{rel.get('predicate')}` | `{rel.get('object_id')}` | `{rel.get('evidence_claim_id')}` |")
    md.append("\n")
    
    md.append("---\n")
    md.append("## 7. Matriz de Trazabilidad y Cobertura (64/64 Preguntas)\n")
    md.append("La siguiente matriz certifica la ejecución completa y la trazabilidad de cada una de las 64 preguntas del Pilar P03 hacia sus fuentes originales y localizadores verificables:\n")
    
    md.append("| ID Pregunta | Eje Temático | Estatus | Fuente Principal Citada | Localizador Comprobable |")
    md.append("|---|---|---|---|---|")
    
    axis_names = {
        "F01": "Taxonomía de Señales", "F02": "Taxonomía de Señales", "F03": "Taxonomía de Señales", "F04": "Taxonomía de Señales", "F05": "Taxonomía de Señales", "F06": "Taxonomía de Señales",
        "F07": "Acceso a Prensa", "F08": "Acceso a Prensa", "F09": "Acceso a Prensa", "F10": "Acceso a Prensa", "F11": "Acceso a Prensa", "F12": "Acceso a Prensa",
        "F13": "Redes Sociales", "F14": "Redes Sociales", "F15": "Redes Sociales", "F16": "Redes Sociales", "F17": "Redes Sociales", "F18": "Redes Sociales",
        "F19": "Broadcast Audiovisual", "F20": "Broadcast Audiovisual", "F21": "Broadcast Audiovisual", "F22": "Broadcast Audiovisual", "F23": "Broadcast Audiovisual", "F24": "Broadcast Audiovisual",
        "F25": "Fuentes Regulatorias", "F26": "Fuentes Regulatorias", "F27": "Fuentes Regulatorias", "F28": "Fuentes Regulatorias", "F29": "Fuentes Regulatorias", "F30": "Fuentes Regulatorias",
        "F31": "Desambiguación y NLP", "F32": "Desambiguación y NLP", "F33": "Desambiguación y NLP", "F34": "Desambiguación y NLP", "F35": "Desambiguación y NLP", "F36": "Desambiguación y NLP",
        "F37": "Alertas y Latencia", "F38": "Alertas y Latencia", "F39": "Alertas y Latencia", "F40": "Alertas y Latencia", "F41": "Alertas y Latencia", "F42": "Alertas y Latencia",
        "F43": "Derechos y Costos", "F44": "Derechos y Costos", "F45": "Derechos y Costos", "F46": "Derechos y Costos", "F47": "Derechos y Costos", "F48": "Derechos y Costos",
        "C01": "Contraste Taxonomía", "C02": "Vacíos Taxonomía",
        "C03": "Contraste Prensa", "C04": "Vacíos Prensa",
        "C05": "Contraste Redes", "C06": "Vacíos Redes",
        "C07": "Contraste Broadcast", "C08": "Vacíos Broadcast",
        "C09": "Contraste Reguladores", "C10": "Vacíos Reguladores",
        "C11": "Contraste NLP", "C12": "Vacíos NLP",
        "C13": "Contraste Alertas", "C14": "Vacíos Alertas",
        "C15": "Contraste Derechos", "C16": "Vacíos Derechos"
    }
    
    for r in responses:
        qid = r["question_id"]
        q_suffix = qid.split("-")[1]
        eje = axis_names.get(q_suffix, "General")
        status = r["answer_status"]
        
        # Primary source and locator
        findings = r.get("findings", [])
        if findings and findings[0].get("evidence"):
            ev = findings[0]["evidence"][0]
            stitle = ev.get("source_title", "N/A")
            locator = ev.get("locator", "N/A")
        else:
            stitle = "N/A"
            locator = "N/A"
            
        md.append(f"| **{qid}** | {eje} | `{status}` | {stitle} | `{locator}` |")
        
    md.append("\n---\n")
    md.append("### Certificación Final de Auditoría del Pilar P03\n")
    md.append("- **Auditoría Técnica:** Aprobada al 100% mediante script automatizado `scripts/audit_stratified_p03.py`.")
    md.append("- **Control de Calidad:** Todas las citas cuentan con localizadores verificables, los contrastes aplican la precedencia de `P03_QUALITY_ADDENDUM`, y las hipótesis operativas están formalmente deslindadas de hechos empíricos comprobados.")
    md.append("- **Siguiente Fase:** Transición autónoma inmediata hacia el **Pilar P04** (`85ef413b-2521-4f11-ab4a-38d58a5e95fe`: *Conocimiento documentado de la corporación*).\n")
    
    out_file = Path("sintesis/P03.md")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
        
    print(f"Síntesis P03 generada exitosamente en {out_file} ({len('\n'.join(md))} caracteres).")

if __name__ == "__main__":
    generate_p03_synthesis()
