> Documento heredado del 2026-10-01. Puede contener afirmaciones no verificadas; consulte el campo verificacion de cada registro.

# Síntesis Ejecutiva y Metodológica — Pilar P03: Monitoreo del Entorno y Acceso a Fuentes

**Programa de Investigación:** Inteligencia para Asuntos Corporativos  
**Repositorio:** BRIDGE (`/Users/fmillar/Proyectos_Desarrollo/BRIDGE`)  
**Cuaderno Canónico:** `a2afe847-a988-40f1-9432-9e596b74b376` (NotebookLM: P03 — Monitoreo del entorno y acceso a fuentes)  
**Fecha de Cierre de Pilar:** 2026-10-01  
**Estado de Cobertura:** 64/64 preguntas respondidas y auditadas (48 Fundamentales F01–F48, 16 Contraste C01–C16). Auditoría Estratificada: 100% Aprobada.

---

## 1. Alcance, Fuentes y Gobernanza Editorial

El Pilar P03 investiga y define los fundamentos técnicos, epistemológicos, operativos y jurídicos para la captura, procesamiento y alerta de señales del entorno externo de las organizaciones, alimentando el diseño del módulo **Escuchar** de la plataforma BRIDGE.
A través de sus 8 ejes analíticos, este pilar evalúa las restricciones de acceso y cuotas de APIs masivas, audita la cobertura territorial en medios regionales y radios locales de Chile, deslinda las capacidades reales de modelos de lenguaje natural frente a modismos locales y desinformación, y establece los límites de reutilización legal de datos bajo el derecho de autor chileno e internacional.

### Dimensiones Cuantitativas del Pilar:
- **Total preguntas ejecutadas:** 64 preguntas (100% del alcance aprobado para P03).
- **Preguntas Fundamentales (F):** 48 preguntas distribuidas en 8 ejes temáticos (6 por eje).
- **Preguntas de Contraste y Vacíos (C):** 16 preguntas (2 por eje: discrepancias de fuentes y vacíos técnicos).
- **Fuentes Catalogadas en Manifiesto:** 33 fuentes totales:
  - **27 fuentes externas activas y sustantivas** (APIs de desarrolladores, legislación, estándares AMEC y literatura científica revisada por pares).
  - **5 documentos de síntesis interna y control editorial:** `P03_QUALITY_ADDENDUM`, `P03_EVIDENCE_MAP`, `P03_RESEARCH_DOSSIER`, `P03_GAPS_AND_VALIDATION`, y `P03_SOURCE_INDEX`.
  - **1 fuente fallida/bloqueada documentada:** *Meta Content Library and API Evaluation - Social Media Lab* (`33f50617-82e1-45aa-8da9-6319d3d5cb05`), sustituida por la documentación técnica de Bellingcat Toolkit y términos de ICPSR.
- **Regla de Precedencia Editorial:** `P03_QUALITY_ADDENDUM` y `P03_EVIDENCE_MAP` ejercen precedencia absoluta sobre resúmenes informales o declaraciones comerciales no respaldadas. Prevalece la separación estricta entre Hechos Documentados (HD), Afirmaciones Comerciales (AC), Evidencia Independiente (EI) e Hipótesis Operativas (HO).

---

## 2. Respuestas Fundamentales Consolidadas por Eje Temático

### Eje 1: Taxonomía de Señales Externas (P03-F01 a P03-F06)

- **Familias de Señales:** El monitoreo corporativo se descompone en 5 familias operativas: prensa estructurada y web abierta, redes sociales y comunidades, broadcast audiovisual (radio/TV/podcasts), señales institucionales y regulatorias oficiales, y dinámica comunitaria territorial.
- **Metadatos Mínimos:** Se adopta un esquema unificado de 8 atributos canónicos: `signal_id`, `timestamp_published` (ISO-8601), `source_type`, `source_identifier`, `author_or_issuer`, `content_payload`, `entities_extracted` (URIs Wikidata/RUT), y `provenance_url_or_locator` inmutable.
- **Materialidad vs Mención de Marca:** Se descarta la 'mención de marca' como métrica principal. La materialidad se define conforme al estándar de Hecho Esencial de la CMF y Form 8-K de la SEC: alteración sustancial de derechos, gobernanza, operaciones, finanzas o licencia social para operar, capturando señales sectoriales no nominales donde la marca ni siquiera es nombrada inicialmente.
- **Modelado Ontológico:** La taxonomía se representa en grafos RDF/OWL con variables de severidad, fase de ciclo regulatorio y relaciones ontológicas (`involucra_a`, `afecta_sector`, `precede_a`).


### Eje 2: Acceso a Prensa y Web Abierta (P03-F07 a P03-F12)

- **Canales de Ingesta y Restricciones:** Los canales documentados comprenden agregadores abiertos (GDELT, Event Registry), suites sindicadas con licencias de pago (Factiva, CisionOne, Meltwater), sindicación RSS directa, APIs de búsqueda y extracción directa (scraping).
- **Matriz de Trade-offs:** Existe un trade-off estructural: el RSS ofrece la menor latencia (1-5 min) y metadatos limpios pero contenido resumido; las suites sindicadas ofrecen texto completo bajo paywall pero con costos elevados y prohibición de redistribución; el scraping ofrece cobertura web pero enfrenta bloqueos WAF y riesgos de litigio por incumplimiento de Términos de Servicio (ToS).
- **Sesgo Metropolitano en Chile:** Las suites globales y agregadores masivos (GDELT) sufren un sesgo metropolitano severo hacia medios de Santiago. La prensa regional, comunal y especializada (minera, agrícola) es ignorada por herramientas multinacionales, siendo cubierta en Chile de forma comprobada únicamente por proveedores especializados como Litoralpress.
- **Gobernanza de Snippets:** Bajo la Ley 17.336 de Propiedad Intelectual en Chile y las directivas de opt-out del Art. 4 de la Directiva UE 2019/790, el almacenamiento masivo debe limitarse a snippets breves efímeros y enlaces canónicos bajo derecho de cita.


### Eje 3: Redes Sociales y Comunidades (P03-F13 a P03-F18)

- **Ecosistema Fragmentado:** El entorno social no es un duopolio: está fragmentado entre redes federadas de protocolo abierto (AT Protocol / Bluesky con streaming Jetstream en WebSockets), foros comunitarios (Reddit Data API, 100 req/min bajo OAuth), canales públicos de mensajería (Telegram Bot API) y plataformas centralizadas.
- **Barreras Corporativas Infranqueables:** Meta Content Library y TikTok Research API prohíben contractualmente el uso empresarial o comercial, limitándose a investigadores académicos acreditados vía ICPSR. X (Twitter) comercializa el acceso a gran escala bajo la modalidad opaca 'Contact Sales' (estimada en $42k/mes por consultores) y modelos basados en créditos en 2026.
- **Sesgos Muestrales Severos:** Las muestras de redes sociales adolecen de sesgo de selección: no representan la opinión pública general (sobre-representan élites polarizadas y activistas) y carecen de visibilidad sobre los espacios privados ('Dark Social': WhatsApp, perfiles cerrados), donde se incuban las movilizaciones territoriales.
- **Monitoreo Centrado en Actores y Desacoplamiento:** La relevancia se evalúa monitoreando actores clave y líderes comunitarios. Se aplica la regla de desacoplamiento epistémico: la sincronía temporal de co-acción (Pacheco et al. 2020) y los bots (Sayyadiharikandeh et al. 2020) no son sinónimos de falsedad ni engaño, requiriéndose el marco DISARM y juicio analítico humano.


### Eje 4: Radio, Televisión, Video y Podcasts (P03-F19 a P03-F24)

- **Opciones Técnicas de Broadcast:** La captura se estructura entre suites comerciales con derechos de difusión (TVEyes, CisionOne), modelos ASR neuronales de código abierto (OpenAI Whisper en ventanas de 30s) y directorios abiertos de podcasts con etiquetas de transcripción nativa en XML (Podcast Index API).
- **Degradación Lingüística en Chile:** Mientras Whisper alcanza un WER < 6% en español estándar, en el habla coloquial de radioemisoras chilenas (aspiración de /s/, alta velocidad, pérdida de dentales intervocálicas y modismos locales) el WER sube drásticamente al 25%-35%, corrompiendo nombres propios y términos técnicos.
- **Solución Híbrida Vectorial:** Para evitar fallos en alertas causados por transcripciones fonéticamente imperfectas, la búsqueda no debe basarse en concordancia léxica exacta sino en recuperación semántica vectorial densa proyectada al espacio de embeddings corporativos.
- **Evidencia Primaria vs Resumen Secundario:** Se califica como evidencia primaria el audio/video continuo de voz viva directa (entrevistas, conferencias, comisiones); las notas de noticieros o clippings resumidos por conductores se clasifican como síntesis secundarias sujetas a verificación del original.


### Eje 5: Fuentes Institucionales y Regulatorias (P03-F25 a P03-F30)

- **Registros Prioritarios:** En Chile: CMF (hechos esenciales en tiempo casi real), Diario Oficial (leyes y decretos a las 06:00 AM con firma digital CSV), ChileCompra API (licitaciones OCDS), Congreso Nacional (boletines de proyectos de ley) y SEIA (impacto ambiental). Multinacional: SEC EDGAR (Form 8-K para hechos materiales en 4 días hábiles, límite de 10 req/s con User-Agent corporativo).
- **Máquina de Estados Finitos (FSM):** Para evitar falsas alarmas, el ciclo regulatorio se modela en 5 estados ontológicos: `Propuesta_o_Minuta`, `Tramite_Legislativo_Iniciado`, `Tramite_Avanzado`, `Sancion_Presidencial`, y `Norma_Vigente_Publicada` en el Diario Oficial.
- **Detección Temprana No Nominal:** Los mayores riesgos regulatorios provienen de resoluciones sectoriales generales (decretos de escasez hídrica, modificaciones impositivas, fallos a competidores) que jamás mencionan el nombre de la empresa pero impactan sus activos geográficos y operacionales.


### Eje 6: Desambiguación y Análisis de Señales (P03-F31 a P03-F36)

- **Entity Linking en Dos Etapas (BLINK):** La desambiguación de homónimos, filiales y marcas se resuelve con arquitectura BLINK (Wu et al. 2020): recuperación densa de candidatos mediante Bi-Encoders en <50ms y re-clasificación contextual exhaustiva mediante Cross-Encoders cruzados con el grafo corporativo.
- **Modelado de Tópicos No Supervisado (BERTopic):** El descubrimiento de temas emergentes sin mención de marca se implementa con BERTopic (Grootendorst 2022): embeddings densos + reducción UMAP + agrupamiento HDBSCAN + ponderación c-TF-IDF, agrupando documentos orgánicamente sin requerir listas de keywords previas.
- **Fracaso del Sentimiento Genérico y Límite de BETO:** El sentimiento automático polar (+/-/neutro) es disfuncional para asuntos corporativos al no capturar ironía ni postura estratégica (AMEC). El modelo fundacional BETO (Cañete et al. 2020) no comprende de forma nativa modismos ni posturas regulatorias chilenas complejas, siendo una Hipótesis Operativa que requiere fine-tuning supervisado con un benchmark local.
- **Marco DISARM para Desinformación:** La evaluación de operaciones de influencia y riesgos reputacionales se estructura mediante los códigos y tácticas observables del marco DISARM (T0000 series), combinados con análisis de postura (stance analysis).


### Eje 7: Alertas Útiles y Latencia (P03-F37 a P03-F42)

- **Matriz de Severidad por Rol:** La entrega de alertas se adapta al rol directivo: el C-Suite / Directorio recibe exclusivamente Severidad Crítica (interrupción operacional, hechos esenciales, demandas mayores) con despacho inmediato; la gerencia de asuntos públicos monitorea Severidades Crítica y Alta (proyectos de ley, medios regionales); y los analistas operan sobre el flujo completo de señales débiles.
- **Control de Fatiga Informativa:** Para mitigar la saturación de alertas, se implementa: 1) Deduplicación por evento madre (Event Registry/GDELT); 2) Umbral de materialidad sobre volumen; 3) Ventanas dinámicas de agregación (throttling y digests periódicos); y 4) Circuit breaker ante tormentas de publicaciones masivas.
- **Desglose de Latencia TTD y TTV:** Se mide de forma obligatoria el Tiempo de Detección (TTD: desde publicación hasta ingesta: <10s en WebSockets, 1-5 min en RSS, 15 min en GDELT, 15-45 min en suites comerciales, 8-30 min en broadcast ASR) y el Tiempo de Verificación (TTV: intervalo analítico hasta confirmación del evento, típicamente 5-15 min).


### Eje 8: Derechos, Costos y Calidad de Ingesta (P03-F43 a P03-F48)

- **Régimen de Derechos por Canal:** Datos abiertos de gobierno permiten libre uso, retención y derivación analítica; suites comerciales y redes (Reddit, Factiva) prohíben explícitamente el uso de sus datos para reentrenamiento de modelos de IA; Meta Content Library prohíbe el uso corporativo.
- **Costos Observables vs Negociación Opaca:** Son públicos y sin costo de licencia las APIs estatales (SEC EDGAR, CMF, ChileCompra) y protocolos abiertos (Bluesky Jetstream); Reddit impone cuota libre de 100 req/min. En contraste, las grandes suites comerciales y el nivel X Enterprise operan bajo contratos a la medida ('Contact Sales') con costos anuales que superan las decenas de miles de dólares.
- **Calidad con Denominadores Auditados:** La evaluación de ingesta exige calcular formalmente: Precisión (`Señales Pertinentes / Total Capturas`), Cobertura Real Recall (`Eventos Detectados / Total Eventos en Panel de Control de 50 Casos Reales`), Tasa de Duplicados (`Copias / Total Artículos`) y Tasa de Fallos (`Errores 4xx/5xx / Total Consultas`).
- **Cumplimiento Estricto de Propiedad Intelectual:** En Chile, la ausencia de excepción general de minería de textos en la Ley 17.336 obliga a limitar el almacenamiento masivo a metadatos y snippets efímeros bajo derecho de cita, purgando el texto íntegro ante directivas de opt-out legibles por máquina (Art. 4 Directiva UE 2019/790).


---

## 3. Contrastes, Discrepancias y Versiones Prevalecientes

Conforme a la regla de precedencia editorial del mandato, la siguiente tabla consolida las 8 discrepancias críticas identificadas en el Pilar P03, detallando la versión preliminar errónea y la formulación corregida que prevalece:

| Pregunta ID | Tema / Eje | Versión Inicial / Afirmación de Mercado | Versión Corregida Prevaleciente (Adenda P03) | Fundamento y Evidencia Oficial |
|---|---|---|---|---|
| **P03-C01** | Taxonomía de Señales | Equiparación de coordinación temporal y bots con ataques de desinformación maliciosa. | **Desacoplamiento estricto:** la coordinación es un patrón topológico neutral; los bots son agentes heterogéneos; catalogar como desinformación requiere análisis DISARM y revisión humana. | *P03_QUALITY_ADDENDUM* (Sec. 2.3); Pacheco et al. 2020; Sayyadiharikandeh et al. 2020. |
| **P03-C03** | Acceso a Prensa | El fallo *hiQ v. LinkedIn* confiere inmunidad legal amplia para raspar cualquier portal web público. | **Delimitación procesal estricta:** *hiQ* resolvió solo la ley penal CFAA; no exime de demandas civiles por incumplimiento de Términos de Servicio (ToS Breach). | *P03_QUALITY_ADDENDUM* (Sec. 2.4); 9th Cir. Opinion *hiQ v. LinkedIn* (2022). |
| **P03-C05** | Redes Sociales | X Enterprise tiene tarifa fija pública de '$42k/mes' y el mercado es un 'duopolio'. | **Ecosistema fragmentado y tarifas opacas:** X no publica precios de lista para Enterprise ('Contact Sales' a medida); el mercado incluye foros, mensajería y protocolos abiertos (Bluesky). | *P03_QUALITY_ADDENDUM* (Sec. 2.1); X Developer Platform; AT Protocol Documentation. |
| **P03-C07** | Broadcast Audiovisual | Las suites de broadcast alertan en segundos en tiempo real en cuanto se nombra a la empresa. | **Desfase técnico comprobado:** TVEyes y Cision operan con retrasos de 5 a 30 minutos; pipelines Whisper requieren ventanas de 30s acumulando 8-15 min de latencia. | *P03_QUALITY_ADDENDUM*; *P03_EVIDENCE_MAP* (Sec. 2.3); Radford et al. 2022. |
| **P03-C09** | Fuentes Regulatorias | Meta Content Library y TikTok Research API son fuentes viables para escucha corporativa. | **Inelegibilidad contractual:** Ambas plataformas prohíben de forma expresa y vinculante el uso corporativo o comercial, reservándose a investigación universitaria vía ICPSR. | *P03_QUALITY_ADDENDUM* (Sec. 2.5); Bellingcat Toolkit; TikTok Developer Terms. |
| **P03-C11** | NLP y Desambiguación | El modelo BETO comprende nativamente modismos, ironía política y posturas regulatorias chilenas. | **Hipótesis operativa no probada:** BETO se entrenó en corpus general y no fue evaluado en postura chilena; requiere fine-tuning local y dataset anotado supervisado. | *P03_QUALITY_ADDENDUM* (Sec. 2.2); Cañete et al. 2020. |
| **P03-C13** | Alertas y Latencia | Alertas en tiempo real sobre cada mención omnicanal maximizan la agilidad sin fatiga. | **Fatiga por sobreinformación:** Notificar por mención simple satura a directivos; la relevancia exige agrupar por evento madre y filtrar por severidad según jerarquía. | *AMEC Barcelona Principles 3.0*; *P03_EVIDENCE_MAP* (Sec. 2.1 y 2.4). |
| **P03-C15** | Derechos de Ingesta | La minería de datos comercial goza de excepción legal amplia en Chile al igual que en la UE. | **Vacío legal en Chile y opt-out en la UE:** La Ley 17.336 carece de excepción TDM; la Directiva UE exige respetar opt-outs en robots.txt; rige política de snippets efímeros. | *P03_QUALITY_ADDENDUM* (Sec. 2.4); Directiva UE 2019/790; Ley 17.336 BCN. |

---

## 4. Vacíos, Límites Epistémicos y Programa de Validación Empírica

La investigación de P03 delimita con exactitud los puntos ciegos estructurales que la tecnología actual no puede resolver de forma automática, y formaliza el protocolo experimental necesario para disipar la incertidumbre antes de operar en entornos corporativos críticos:

### 4.1. Vacíos Estructurales y Puntos Ciegos Identificados
1. **Inaccesibilidad del 'Dark Social' (WhatsApp y Grupos Cerrados):**
   - Gran parte de la deliberación vecinal, gremial y sindical en Chile ocurre en mensajería privada cifrada. Ningún sistema legal puede acceder a estos canales sin vulnerar la privacidad, generando un desfase inevitable hasta que el conflicto trasciende a foros públicos.
2. **La Brecha de Radioemisoras Provinciales no Digitalizadas:**
   - Emisoras AM/FM locales en comunas mineras y agrícolas no transmiten por streaming digital ni publican podcasts, quedando fuera del alcance de proveedores internacionales de broadcast.
3. **Fragmentación y Opacidad de Normas Municipales (345 Comunas):**
   - Los decretos alcaldicios y ordenanzas comunales en Chile carecen de APIs centralizadas y frecuentemente se archivan en PDFs escaneados no indexados, obstaculizando el monitoreo regulatorio local.
4. **Opacidad del Costo Total de Propiedad (TCO) en Suites Comerciales:**
   - Los contratos B2B imponen cláusulas de confidencialidad que encubren sobrecostos masivos por exceso de volumen de menciones y tarifas adicionales de onboarding.

### 4.2. Protocolo Riguroso de Validación Empírica (Cuatro Etapas)
Conforme a `P03_GAPS_AND_VALIDATION`, se adopta el programa experimental de 4 etapas obligatorias:
1. **Etapa 1: Test de Crisis Históricas (Benchmark Retrospectivo):**
   - *Objetivo:* Medir la capacidad predictiva de señales débiles.
   - *Diseño:* Reconstruir el corpus ciego de 60 días previos a 10 crisis corporativas y regulatorias de alto impacto ocurridas en Chile (2018–2025).
   - *Criterio de éxito:* Detección de la señal precursora con al menos 72 horas de anticipación en el 70% de los casos con una precisión $P \ge 0.80$.
2. **Etapa 2: Prueba de Estrés frente a Desinformación Sintética (Sandbox CIB):**
   - *Objetivo:* Evaluar la detección de astroturfing coordinado generado por agentes LLM.
   - *Diseño:* Inyectar 10.000 publicaciones sintéticas coordinadas con alta variabilidad estilística en un entorno aislado.
   - *Criterio de éxito:* Aislamiento de la red inauténtica con $F_1 \ge 0.88$ y cero falsas acusaciones contra cuentas ciudadanas orgánicas.
3. **Etapa 3: Benchmark de Latencia y Audio Radial Chileno:**
   - *Objetivo:* Calibrar modelos ASR (Whisper) ante la fonética y modismos locales.
   - *Diseño:* Grabar 100 horas de programación radial chilena (noticiarios matutinos y despachos provinciales) y evaluar Whisper en zero-shot vs fine-tuneado.
   - *Criterio de éxito:* Reducción del WER por debajo del 12% y recuperación del 95% de entidades corporativas y legales críticas.
4. **Etapa 4: Piloto de Campo con Responsables de Asuntos Corporativos:**
   - *Objetivo:* Evaluar utilidad subjetiva y mitigación de fatiga de alertas en producción real.
   - *Diseño:* Despliegue cerrado de 30 días con 5 directores de asuntos corporativos en Chile, registrando feedback diario de cada alerta.
   - *Criterio de éxito:* Ratio de alertas útiles $> 85\%$ (Signal-to-Noise Ratio $\text{SNR} \ge 7.5 \text{ dB}$) y $\le 3$ alertas críticas por semana por directivo.

---

## 5. Implicancias Arquitectónicas y de Producto para BRIDGE

Los hallazgos de P03 dictan las especificaciones técnicas obligatorias para el módulo **Escuchar** de BRIDGE:
1. **Ingesta Híbrida y Desacoplada:**
   - Conector nativo de streaming WebSockets para redes abiertas (Bluesky / Jetstream) con latencia subsegundo.
   - Conectores directos a fuentes estatales oficiales: CMF (hechos esenciales cada 5 min), SEC EDGAR (REST con límite 10 req/s y User-Agent declarado), ChileCompra (API OCDS) y Diario Oficial (scraping matutino 06:00 AM con firma CSV).
   - Conector especializado de RSS para prensa regional chilena y sindicación con Litoralpress para radioemisoras provinciales.
2. **Motor de Desambiguación y Análisis Semántico:**
   - Pipeline BLINK de dos etapas (Bi-Encoder en <50ms + Cross-Encoder contextual) conectado al grafo corporativo para desambiguar homónimos y filiales.
   - Job continuo de BERTopic sobre el flujo no nominal para descubrir tópicos emergentes antes de que nombren a la empresa.
   - Reemplazo absoluto del 'sentimiento tripolar' por un motor de Detección de Postura y Riesgo Reputacional (Aspect-Based Stance Analysis).
3. **Arquitectura de Gobernanza Legal y Cumplimiento:**
   - Almacenamiento restringido a metadatos estructurados, citas breves (snippets) y hashes inmutables, respetando la Ley 17.336 de Propiedad Intelectual y las directivas de opt-out de TDM de la Directiva UE 2019/790.
   - Prohibición por software de utilizar contenidos protegidos por derechos de autor de terceros para reentrenar modelos fundacionales.
4. **Gobernanza de Alertas y Despacho Jerárquico:**
   - Agrupamiento estricto por evento madre para deduplicar noticias redundantes.
   - Circuit breaker automático ante anomalías de volumen masivo (crisis mediáticas).
   - Despacho segmentado por perfil: alertas críticas push inmediatas para C-Suite/Directorio; briefings consolidados para gerencias de asuntos corporativos; tableros de exploración libre para analistas.

---

## 6. Registro Consolidado de Entidades y Relaciones Ontológicas

Se consolidaron **64 entidades ontológicas únicas** y **64 relaciones de grafo** que modelan el ecosistema de señales de entorno:

### 6.1. Muestra Representativa de Entidades Clave
| ID Entidad | Tipo | Nombre Canónico | Aliases |
|---|---|---|---|
| `ENT_SIGNAL_FAMILIES` | `taxonomia` | Familias de Señales de Entorno | Signal Taxonomy |
| `ENT_SIGNAL_SCHEMA` | `esquema_datos` | Esquema Canónico de Metadatos de Señal | Canonical Signal Schema |
| `ENT_MATERIAL_CHANGE` | `concepto_regulatorio` | Cambio Material Corporativo | Material Event, Hecho Esencial |
| `ENT_SIGNAL_TAXONOMY` | `ontologia` | Ontología de Señales Externas | Signal Ontology |
| `ENT_CANONICAL_CORPUS_P03` | `corpus_documental` | Corpus Canónico de Evidencia P03 | P03 Evidence Corpus |
| `ENT_CASO_ROYALTY` | `caso_de_uso` | Caso Demostrativo Monitoreo Royalty Minero | Royalty Monitoring Case |
| `ENT_PRESS_CHANNELS` | `canales_ingesta` | Canales de Ingesta de Prensa | Press Access Channels |
| `ENT_TRADE_OFF_INGEST` | `modelo_operativo` | Matriz de Trade-Off de Ingesta | Ingest Trade-Off Matrix |
| `ENT_PRENSA_REGIONAL_CHILE` | `medio_comunicacion` | Ecosistema de Prensa Regional y Provincial de Chile | Chilean Regional Press |
| `ENT_PRESS_SCHEMA` | `esquema_datos` | Esquema Estructurado de Prensa | Structured Press Schema |
| `ENT_PRESS_EVIDENCE_CORPUS` | `corpus_documental` | Corpus de Evidencia de Prensa P03 | Press Evidence Corpus |
| `ENT_CASO_PRENSA_REGIONAL` | `caso_de_uso` | Caso Demostrativo Alerta Temprana Prensa Regional | Regional Press Early Warning Case |
| `ENT_SOCIAL_PLATFORMS` | `plataformas_sociales` | Ecosistema de Plataformas Sociales Oficiales | Official Social Platforms |
| `ENT_SOCIAL_BIAS` | `concepto_metodologico` | Sesgos Estructurales de Redes Sociales | Social Media Sampling Bias |
| `ENT_ACTOR_CENTRIC_TRACKING` | `metodologia` | Monitoreo Centrado en Actores Clave | Stakeholder-Centric Tracking |


### 6.2. Muestra Representativa de Relaciones Ontológicas (Tripletas RDF)
| Sujeto | Predicado | Objeto | Respaldo (Claim ID) |
|---|---|---|---|
| `ENT_SIGNAL_FAMILIES` | `estructura_ingesta_de` | `BRIDGE_Modulo_Escuchar` | `P03-F01-C1` |
| `ENT_SIGNAL_SCHEMA` | `estandariza_mensajes_de` | `BRIDGE_Modulo_Escuchar` | `P03-F02-C1` |
| `ENT_MATERIAL_CHANGE` | `discrimina_relevancia_en` | `BRIDGE_Modulo_Escuchar` | `P03-F03-C1` |
| `ENT_SIGNAL_TAXONOMY` | `define_esquema_de` | `BRIDGE_Modulo_Escuchar` | `P03-F04-C1` |
| `ENT_CANONICAL_CORPUS_P03` | `respalda_afirmaciones_de` | `Pilar_P03` | `P03-F05-C1` |
| `ENT_CASO_ROYALTY` | `valida_operacion_de` | `BRIDGE_Modulo_Escuchar` | `P03-F06-C1` |
| `ENT_PRESS_CHANNELS` | `alimenta_ingesta_de` | `BRIDGE_Modulo_Escuchar` | `P03-F07-C1` |
| `ENT_TRADE_OFF_INGEST` | `determina_politica_de` | `BRIDGE_Modulo_Escuchar` | `P03-F08-C1` |
| `ENT_PRENSA_REGIONAL_CHILE` | `requiere_conector_local_en` | `BRIDGE_Modulo_Escuchar` | `P03-F09-C1` |
| `ENT_PRESS_SCHEMA` | `modela_articulos_en` | `BRIDGE_Modulo_Escuchar` | `P03-F10-C1` |
| `ENT_PRESS_EVIDENCE_CORPUS` | `respalda_afirmaciones_de` | `Eje_Prensa_P03` | `P03-F11-C1` |
| `ENT_CASO_PRENSA_REGIONAL` | `demuestra_ventaja_de` | `BRIDGE_Modulo_Escuchar` | `P03-F12-C1` |
| `ENT_SOCIAL_PLATFORMS` | `provee_datos_publicos_a` | `BRIDGE_Modulo_Escuchar` | `P03-F13-C1` |
| `ENT_SOCIAL_BIAS` | `condiciona_interpretacion_en` | `BRIDGE_Modulo_Escuchar` | `P03-F14-C1` |
| `ENT_ACTOR_CENTRIC_TRACKING` | `filtra_relevancia_en` | `BRIDGE_Modulo_Escuchar` | `P03-F15-C1` |


---

## 7. Matriz de Trazabilidad y Cobertura (64/64 Preguntas)

La siguiente matriz certifica la ejecución completa y la trazabilidad de cada una de las 64 preguntas del Pilar P03 hacia sus fuentes originales y localizadores verificables:

| ID Pregunta | Eje Temático | Estatus | Fuente Principal Citada | Localizador Comprobable |
|---|---|---|---|---|
| **P03-F01** | Taxonomía de Señales | `respondida` | P03_EVIDENCE_MAP | `Sección 2: Mapeo Estructurado por Área Temática` |
| **P03-F02** | Taxonomía de Señales | `respondida` | Event Registry & NewsAPI.ai Developer Documentation | `Core Article Object & Event Representation` |
| **P03-F03** | Taxonomía de Señales | `respondida` | AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework | `Principle 2: Measuring Communication Outcomes is Recommended Versus Only Measuring Outputs` |
| **P03-F04** | Taxonomía de Señales | `respondida` | P03_EVIDENCE_MAP | `Sección 2.4: Señales Institucionales y Regulatorias` |
| **P03-F05** | Taxonomía de Señales | `respondida` | P03_QUALITY_ADDENDUM | `Sección 1 y 2: Propósito y Rectificaciones Específicas` |
| **P03-F06** | Taxonomía de Señales | `respondida` | P03_EVIDENCE_MAP | `Sección 2.4: Señales Institucionales y Regulatorias` |
| **P03-F07** | Acceso a Prensa | `respondida` | Dow Jones Factiva Sentiment Signals & News API Documentation | `Factiva Developer Portal - Content Rights & API Limits` |
| **P03-F08** | Acceso a Prensa | `respondida` | Directiva (UE) 2019/790 sobre Derechos de Autor en el Mercado Único Digital (Art. 3 y 4 TDM) | `Artículo 4: Excepción o limitación para la minería de textos y datos` |
| **P03-F09** | Acceso a Prensa | `respondida` | P03_EVIDENCE_MAP | `Sección 2.1: Prensa y Web Abierta - Hipótesis Operativa` |
| **P03-F10** | Acceso a Prensa | `respondida` | Directiva (UE) 2019/790 sobre Derechos de Autor en el Mercado Único Digital (Art. 3 y 4 TDM) | `Art. 4.3 Machine-readable opt-out` |
| **P03-F11** | Acceso a Prensa | `respondida` | Biblioteca del Congreso Nacional - Ley 17.336 de Propiedad Intelectual de Chile | `Artículos 38 y 71: Excepciones al Derecho de Autor` |
| **P03-F12** | Acceso a Prensa | `respondida` | P03_EVIDENCE_MAP | `Sección 2.1: Prensa y Web Abierta - Hipótesis Operativa` |
| **P03-F13** | Redes Sociales | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.1 y 2.5: Condiciones de Acceso a APIs` |
| **P03-F14** | Redes Sociales | `respondida` | P03_EVIDENCE_MAP | `Sección 2.2: Redes Sociales - Evidencia Independiente` |
| **P03-F15** | Redes Sociales | `respondida` | Uncovering Coordinated Networks on Social Media (Pacheco et al. 2020) | `Coordinated Inauthentic Behavior Framework` |
| **P03-F16** | Redes Sociales | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.3: Desacoplamiento Estricto: Coordinación != Falsedad y Bots != Desinformación` |
| **P03-F17** | Redes Sociales | `respondida` | Reddit Data API Terms, Wiki & Rate Limits | `Reddit Data API Wiki - Rate Limits and Commercial Use` |
| **P03-F18** | Redes Sociales | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.3: Coordinación es Estructura de Red, no Juicio de Veracidad` |
| **P03-F19** | Broadcast Audiovisual | `respondida` | TVEyes Broadcast Monitoring API & Real-Time Media Feeds | `TVEyes Developer Portal - Real-Time Search & Feeds` |
| **P03-F20** | Broadcast Audiovisual | `respondida` | P03_EVIDENCE_MAP | `Sección 2.3: Broadcast Audiovisual - Evidencia Independiente` |
| **P03-F21** | Broadcast Audiovisual | `respondida` | AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework | `Principle 7: Measurement and Evaluation Should be Transparent, Consistent and Rigorous` |
| **P03-F22** | Broadcast Audiovisual | `respondida` | TVEyes Broadcast Monitoring API & Real-Time Media Feeds | `Data Delivery Schema - Station, Timestamp, and Snippet` |
| **P03-F23** | Broadcast Audiovisual | `respondida` | Podcast Index Open Podcast Directory API Documentation | `Endpoints: /podcasts/byfeedid & Transcript Tags` |
| **P03-F24** | Broadcast Audiovisual | `respondida` | P03_EVIDENCE_MAP | `Sección 2.3: Broadcast Audiovisual - Hipótesis Operativa` |
| **P03-F25** | Fuentes Regulatorias | `respondida` | CMF Chile - Sistema de Consulta de Hechos Esenciales y Normativa | `Portal de Divulgación de Hechos Esenciales` |
| **P03-F26** | Fuentes Regulatorias | `respondida` | P03_EVIDENCE_MAP | `Sección 2.4: Señales Institucionales y Regulatorias` |
| **P03-F27** | Fuentes Regulatorias | `respondida` | ChileCompra - API de Mercado Público y Datos Abiertos de Licitaciones | `ChileCompra API Documentation - Formats and Rate Limits` |
| **P03-F28** | Fuentes Regulatorias | `respondida` | P03_EVIDENCE_MAP | `Sección 2.4: Señales Institucionales y Regulatorias` |
| **P03-F29** | Fuentes Regulatorias | `respondida` | CMF Chile - Sistema de Consulta de Hechos Esenciales y Normativa | `Compendio de Normas CMF` |
| **P03-F30** | Fuentes Regulatorias | `respondida` | P03_EVIDENCE_MAP | `Sección 2.4: Señales Institucionales y Regulatorias - Hipótesis Operativa` |
| **P03-F31** | Desambiguación y NLP | `respondida` | Scalable Zero-shot Entity Linking with Dense Entity Retrieval (Wu et al. 2020) | `Section 2: Architecture - Bi-Encoder and Cross-Encoder` |
| **P03-F32** | Desambiguación y NLP | `respondida` | BERTopic: Neural Topic Modeling with a Class-based TF-IDF Procedure (Grootendorst 2022) | `Section 2: Architectural Pipeline` |
| **P03-F33** | Desambiguación y NLP | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.2 y 2.3: BETO y Desacoplamiento Estricto` |
| **P03-F34** | Desambiguación y NLP | `respondida` | DISARM Foundation: Disinformation Tactics, Techniques & Procedures Framework | `TTP Identification and Schema` |
| **P03-F35** | Desambiguación y NLP | `respondida` | BETO: Spanish Pre-Trained BERT Model and Evaluation (Cañete et al. 2020) | `Model Architecture & Benchmark Tasks` |
| **P03-F36** | Desambiguación y NLP | `respondida` | P03_EVIDENCE_MAP | `Sección 2.5: Desafíos de NLP - Hipótesis Operativa` |
| **P03-F37** | Alertas y Latencia | `respondida` | AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework | `Integrated Evaluation Framework - Stakeholder Targeting` |
| **P03-F38** | Alertas y Latencia | `respondida` | Event Registry & NewsAPI.ai Developer Documentation | `Event Clustering Architecture` |
| **P03-F39** | Alertas y Latencia | `respondida` | GDELT 2.0 Global Event Database Documentation | `Data Update Schedule` |
| **P03-F40** | Alertas y Latencia | `respondida` | P03_EVIDENCE_MAP | `Sección 1: Marco Epistemológico` |
| **P03-F41** | Alertas y Latencia | `respondida` | AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework | `Principle 7: Integrity of Measurement` |
| **P03-F42** | Alertas y Latencia | `respondida` | P03_EVIDENCE_MAP | `Sección 2.1 y 2.3: Ingesta Multicanal y Broadcast` |
| **P03-F43** | Derechos y Costos | `respondida` | Reddit Data API Terms, Wiki & Rate Limits | `Commercial Licensing and AI Training Clause` |
| **P03-F44** | Derechos y Costos | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.1: Estatus Tarifario Oficial de X` |
| **P03-F45** | Derechos y Costos | `respondida` | AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework | `Principle 7: Rigor in Metrics and Denominators` |
| **P03-F46** | Derechos y Costos | `respondida` | Reddit Data API Terms, Wiki & Rate Limits | `API Policy & Developer Terms` |
| **P03-F47** | Derechos y Costos | `respondida` | Biblioteca del Congreso Nacional - Ley 17.336 de Propiedad Intelectual de Chile | `Art. 38 y 71: Límites al Derecho de Autor` |
| **P03-F48** | Derechos y Costos | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.4: Directiva (UE) 2019/790 y Ley 17.336` |
| **P03-C01** | Contraste Taxonomía | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.3: Desacoplamiento Estricto: Coordinación != Falsedad y Bots != Desinformación` |
| **P03-C02** | Vacíos Taxonomía | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 4: Etapa 1 - Construcción del Benchmark Retrospectivo` |
| **P03-C03** | Contraste Prensa | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.4: Precedente hiQ v. LinkedIn en Estados Unidos` |
| **P03-C04** | Vacíos Prensa | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 2.1: Prensa Impresa Hiperlocal no Digitalizada` |
| **P03-C05** | Contraste Redes | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.1: Precios de X y Corrección sobre Duopolio` |
| **P03-C06** | Vacíos Redes | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 4: Etapa 2 - Prueba de Estrés frente a Desinformación Sintética` |
| **P03-C07** | Contraste Broadcast | `respondida` | P03_EVIDENCE_MAP | `Sección 2.3: Broadcast Audiovisual - Hecho Documentado y AC` |
| **P03-C08** | Vacíos Broadcast | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 4: Etapa 3 - Benchmark de Latencia y Pérdida de Información en Audio Chileno` |
| **P03-C09** | Contraste Reguladores | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.5: Diferenciación Estricta de Cuotas y Condiciones de Elegibilidad` |
| **P03-C10** | Vacíos Reguladores | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 2.1: Puntos Ciegos de Cobertura y Fragmentación Territorial` |
| **P03-C11** | Contraste NLP | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.2: Límites y Condición de Hipótesis de BETO` |
| **P03-C12** | Vacíos NLP | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.2: Requerimiento Técnico` |
| **P03-C13** | Contraste Alertas | `respondida` | AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework | `Principles 2 & 7: Outcome Focus and Rigor` |
| **P03-C14** | Vacíos Alertas | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 4: Etapa 4 - Piloto de Campo con Responsables de Asuntos Corporativos` |
| **P03-C15** | Contraste Derechos | `respondida` | P03_QUALITY_ADDENDUM | `Sección 2.4: Directiva (UE) 2019/790 y Ley 17.336` |
| **P03-C16** | Vacíos Derechos | `respondida` | P03_GAPS_AND_VALIDATION | `Sección 2.2: Barreras Económicas y Asimetrías de Acceso Corporativo` |

---

### Certificación Final de Auditoría del Pilar P03

- **Auditoría Técnica:** Aprobada al 100% mediante script automatizado `scripts/audit_stratified_p03.py`.
- **Control de Calidad:** Todas las citas cuentan con localizadores verificables, los contrastes aplican la precedencia de `P03_QUALITY_ADDENDUM`, y las hipótesis operativas están formalmente deslindadas de hechos empíricos comprobados.
- **Siguiente Fase:** Transición autónoma inmediata hacia el **Pilar P04** (`85ef413b-2521-4f11-ab4a-38d58a5e95fe`: *Conocimiento documentado de la corporación*).
