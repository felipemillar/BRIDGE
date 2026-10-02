# Índice del repositorio BRIDGE

**Generado:** 2026-10-02 sobre el commit `0e9cf75`. Los índices de máquina se regeneran con `python3 auditoria/construir_indice.py`. El estado de calidad de cada pregunta está en [INFORME_AUDITORIA.md](INFORME_AUDITORIA.md).

> **Para agentes:** no cargues archivos `respuestas/*.jsonl` completos (79k–183k tokens cada uno). Busca la pregunta en [indice_preguntas.jsonl](indice_preguntas.jsonl), lee su `archivo` y `linea`, y extrae solo esa línea (`sed -n '<linea>p' <archivo>`). Revisa `banderas` antes de usar el contenido como hecho.

## 1. Inventario de archivos

Tokens aproximados = caracteres / 3,5.

| Ruta | Qué contiene | Formato / esquema | Tamaño | Tokens | Confiabilidad |
|---|---|---|---:|---:|---|
| [docs_mandato/mandato-…corporativos.md](../docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md) | Mandato rector: objetivo, precedencia editorial, contrato JSON (§3), QA (§4), **banco exacto de 864 preguntas** (§5), cierre (§6) | Markdown | 131 KB | 38k | **Canon** |
| [docs_mandato/auditoria-preliminar-cierre-antigravity.md](../docs_mandato/auditoria-preliminar-cierre-antigravity.md) | Auditoría externa del 2026-10-01 que rechazó la primera certificación | Markdown | 6 KB | 2k | Alta |
| [fuentes/{P01…T01}.json](../fuentes/) | 12 manifiestos de fuentes: `source_id`, `title`, `original_url`, `text_status`, `is_internal_synthesis`, `word_count`, regla de precedencia | JSON `{pilar, notebook_id, total_sources, snapshot_at, editorial_precedence_rule, sources[]}` | 324 KB | 93k | Media (vocabulario `text_status` heterogéneo; P01 sin URLs) |
| [respuestas/{P01…T01}.jsonl](../respuestas/) | 864 respuestas, una por línea, en orden F→C→X | JSONL, contrato del mandato §3 (19 llaves) | 4,6 MB | 1,32M | **Baja–media** (ver banderas) |
| [sintesis/{P01…T01}.md](../sintesis/) | Síntesis por pilar: alcance, hallazgos por eje, matriz Q&A, vacíos, implicaciones, auditoría | Markdown, 7 secciones | 494 KB | 142k | Baja (derivada; hereda defectos) |
| [indice_global.md](../indice_global.md) | Síntesis transversal: mapa de 12 cuadernos y respuestas a las 6 preguntas estratégicas del mandato | Markdown + Mermaid | 14 KB | 4k | Baja (mapa de hipótesis) |
| [entidades.jsonl](../entidades.jsonl) | 1.528 entidades «deduplicadas» | `{entity_id, canonical_name, type, aliases, mentioned_in_notebooks, occurrence_count, questions}` | 331 KB | 95k | Baja (IDs duplicados, tipos libres) |
| [relaciones.jsonl](../relaciones.jsonl) | 477 relaciones | `{subject_id, predicate, object_id, valid_from, valid_to, evidence_claim_ids, notebooks, occurrence_count}` | 113 KB | 32k | Muy baja (71 % aristas colgantes) |
| [contradicciones.jsonl](../contradicciones.jsonl) | 93 contradicciones | `{claim_ids, difference, resolution, reason, pilar, question_id}` | 33 KB | 10k | Media (`resolution` sin enum) |
| [matriz_cobertura.csv](../matriz_cobertura.csv) | 864 filas: ID, texto, estado, confianza, nº de citas, títulos citados | CSV, 9 columnas | 244 KB | 70k | Media (redundante con respuestas) |
| [ejecucion.json](../ejecucion.json) | Telemetría y conteos por pilar | JSON | 12 KB | 3k | Baja (afirma «100 % PASS») |
| [REGISTRO_DE_CIERRE.md](../REGISTRO_DE_CIERRE.md) | Acta de cierre post-reapertura | Markdown | 11 KB | 3k | Baja (ver auditoría §1) |
| [README.md](../README.md) | Portada del programa | Markdown | 6 KB | 2k | Desactualizado (578 fuentes, 1.632 ent., 559 rel.) |
| [BITACORA.md](../BITACORA.md) | 16 sesiones de trabajo, de la más reciente a la más antigua | Markdown | 82 KB | 23k | Registro histórico |
| [.agents/AGENTS.md](../.agents/AGENTS.md) | Reglas de agente: error masking, secretos, bitácora, Git | Markdown | 3 KB | 1k | Vigente (exige rutas `file://` absolutas: no portable) |
| [scripts/](../scripts/) | 193 scripts: 140 `append_*` y 3 `write_*` (**respuestas como literales**), 15 `audit_*`, 12 `generate_sintesis_*`, 12 `build_*manifest`, 10 de reconciliación/remediación | Python | 5,9 MB | ~1,7M | Artefactos de generación; 13 dependen de `~/.gemini/…` |
| [auditoria/](.) | Este índice, informe, propuesta de reorganización e índices de máquina | MD + JSONL | — | — | Generado 2026-10-02 |

## 2. Índices de máquina

| Archivo | Filas | Uso |
|---|---:|---|
| [indice_preguntas.jsonl](indice_preguntas.jsonl) | 864 | Por pregunta: `pilar`, `eje`, `subeje`, `tipo`, `question_text`, `archivo`, `linea`, `tokens_aprox`, `answer_status`, conteo epistémico normalizado, evidencias (totales / sintéticas / síntesis interna), `fuentes_citadas`, **`banderas`** |
| [indice_fuentes.jsonl](indice_fuentes.jsonl) | 551 | Por fuente: `pilar`, `source_id`, `title`, `original_url`, `text_status`, `is_internal_synthesis`, `n_citas`, `preguntas_que_citan` |
| [resumen_indice.json](resumen_indice.json) | 12 | Agregados por pilar |

Banderas posibles: `citas_sinteticas`, `hecho_respaldado_solo_por_sintesis_interna`, `epistemic_status_no_canonico`, `confidence_numerica`, `cita_fuente_no_sustantiva`, `estado_parcial`, `texto_pregunta_distinto_mandato`.

Consultas típicas:

```bash
# Preguntas de un eje
jq -c 'select(.eje=="Alertas útiles y latencia") | {question_id,linea,banderas}' auditoria/indice_preguntas.jsonl
# Respuesta completa de una pregunta
sed -n "$(jq -r 'select(.question_id=="P09-F08").linea' auditoria/indice_preguntas.jsonl)p" respuestas/P09.jsonl | jq .
# Preguntas sin banderas (punto de partida más confiable)
jq -c 'select(.banderas==[]) | .question_id' auditoria/indice_preguntas.jsonl
# Quién cita una fuente
jq -c 'select(.title|test("AMEC")) | {title,n_citas,preguntas_que_citan}' auditoria/indice_fuentes.jsonl
```

## 3. Anatomía de un registro de respuesta

Las 19 llaves, en orden: `question_id`, `notebook_id`, `question_text`, `snapshot_at`*, `answer_status` (`respondida` | `parcial`), `short_answer` (≈1–2k caracteres), `findings[]` → {`claim_id`, `claim`, `epistemic_status`*, `scope{time,region,actor}`, `evidence[]` → {`source_id`, `source_title`, `original_url`, `locator`*, `excerpt_short`*, `source_date`, `retrieved_at`*, `text_status`, `relationship`}, `confidence`*, `confidence_reason`}, `operational_model{inputs,actors,steps,states,outputs,exceptions}`, `entities[]`, `relations[]`, `comparisons[]` (llaves libres), `contradictions[]`, `metrics_and_denominators[]`, `bridge_implications[]` → {`module`, `implication`, `status`}, `open_gaps[]`, `next_question_ids[]`, `quality{…}`*.

\* Campo con defectos documentados en la auditoría (marcas temporales constantes, enums heterogéneos, localizadores y extractos sintéticos, `quality` siempre `true`).

## 4. Taxonomía: 12 pilares, 96 ejes + 12 subejes de profundización, 864 preguntas

Cada eje F tiene 6 preguntas F y 2 C (patrón fijo: F1–F3 sustantivas, F4 representación estructurada, F5 fuentes y pasajes, F6 caso concreto, C1 discrepancias y C2 vacíos). Las X (solo P02, P06 y T01) siguen el mismo patrón en grupos de 8. Las líneas indican la posición en el JSONL del pilar.

### P01 — Asuntos corporativos y sus usuarios

Módulo propuesto: `transversal_usuarios` · 64 preguntas · ~117k tokens · 39 fuentes · preguntas sin bandera: 8/64

| Eje | F | C | X | Líneas en `respuestas/P01.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Mandato y fronteras de asuntos corporativos | F01–F06 | C01–C02 | — | 1–6, 49–50 | 5/8 |
| Mapa de usuarios, compradores y aprobadores | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Trabajos por hacer y momentos de presión | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| Reuniones y decisiones críticas | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Riesgos de preparación insuficiente | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Resultados y retorno de valor | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Usuarios de asuntos corporativos en Chile y Latinoamérica | F37–F42 | C13–C14 | — | 37–42, 61–62 | 2/8 |
| Descubrimiento y validación de usuarios | F43–F48 | C15–C16 | — | 43–48, 63–64 | 1/8 |

### P02 — Empresas y soluciones existentes

Módulo propuesto: `transversal_mercado` · 96 preguntas · ~132k tokens · 80 fuentes · preguntas sin bandera: 26/96

| Eje | F | C | X | Líneas en `respuestas/P02.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Universo comercial y deduplicación | F01–F06 | C01–C02 | — | 1–6, 49–50 | 2/8 |
| Competidores cercanos a los cuatro módulos | F07–F12 | C03–C04 | — | 7–12, 51–52 | 3/8 |
| Plataformas de escucha y reputación | F13–F18 | C05–C06 | — | 13–18, 53–54 | 4/8 |
| Asuntos públicos y memoria de actores | F19–F24 | C07–C08 | — | 19–24, 55–56 | 1/8 |
| Conocimiento interno y cruce de fuentes | F25–F30 | C09–C10 | — | 25–30, 57–58 | 5/8 |
| Flujo editorial y servicios expertos | F31–F36 | C11–C12 | — | 31–36, 59–60 | 5/8 |
| Mapa mundial y diferencias regionales | F37–F42 | C13–C14 | — | 37–42, 61–62 | 3/8 |
| Posicionamiento y alianzas | F43–F48 | C15–C16 | — | 43–48, 63–64 | 2/8 |
| Profundización · Adquisiciones y estructura de grupos | — | — | X01–X08 | 65–72 | 0/8 |
| Profundización · Proximidad funcional verificable | — | — | X09–X16 | 73–80 | 0/8 |
| Profundización · Cobertura territorial y derechos | — | — | X17–X24 | 81–88 | 1/8 |
| Profundización · Certeza comercial y madurez | — | — | X25–X32 | 89–96 | 0/8 |

### P03 — Monitoreo del entorno y acceso a fuentes

Módulo propuesto: `Escuchar` · 64 preguntas · ~78k tokens · 33 fuentes · preguntas sin bandera: 34/64

| Eje | F | C | X | Líneas en `respuestas/P03.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Taxonomía de señales externas | F01–F06 | C01–C02 | — | 1–6, 49–50 | 3/8 |
| Acceso a prensa y web abierta | F07–F12 | C03–C04 | — | 7–12, 51–52 | 4/8 |
| Redes sociales y comunidades | F13–F18 | C05–C06 | — | 13–18, 53–54 | 5/8 |
| Radio, televisión, video y podcasts | F19–F24 | C07–C08 | — | 19–24, 55–56 | 4/8 |
| Fuentes institucionales y regulatorias | F25–F30 | C09–C10 | — | 25–30, 57–58 | 3/8 |
| Desambiguación y análisis de señales | F31–F36 | C11–C12 | — | 31–36, 59–60 | 5/8 |
| Alertas útiles y latencia | F37–F42 | C13–C14 | — | 37–42, 61–62 | 5/8 |
| Derechos, costos y calidad de ingesta | F43–F48 | C15–C16 | — | 43–48, 63–64 | 5/8 |

### P04 — Conocimiento documentado de la corporación

Módulo propuesto: `Saber` · 64 preguntas · ~83k tokens · 34 fuentes · preguntas sin bandera: 45/64

| Eje | F | C | X | Líneas en `respuestas/P04.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Inventario de documentos corporativos | F01–F06 | C01–C02 | — | 1–6, 49–50 | 6/8 |
| Afirmaciones y compromisos | F07–F12 | C03–C04 | — | 7–12, 51–52 | 4/8 |
| Ontología y relaciones | F13–F18 | C05–C06 | — | 13–18, 53–54 | 6/8 |
| Versiones y temporalidad | F19–F24 | C07–C08 | — | 19–24, 55–56 | 7/8 |
| Ingesta y extracción | F25–F30 | C09–C10 | — | 25–30, 57–58 | 5/8 |
| Gobierno y permisos | F31–F36 | C11–C12 | — | 31–36, 59–60 | 6/8 |
| Búsqueda y respuesta fundada | F37–F42 | C13–C14 | — | 37–42, 61–62 | 6/8 |
| Evaluación de calidad documental | F43–F48 | C15–C16 | — | 43–48, 63–64 | 5/8 |

### P05 — Reputación, narrativas y actores

Módulo propuesto: `Escuchar` · 64 preguntas · ~94k tokens · 36 fuentes · preguntas sin bandera: 47/64

| Eje | F | C | X | Líneas en `respuestas/P05.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Identidad, imagen y reputación | F01–F06 | C01–C02 | — | 1–6, 49–50 | 7/8 |
| Modelos de medición y calidad | F07–F12 | C03–C04 | — | 7–12, 51–52 | 4/8 |
| Niveles de métricas de comunicación | F13–F18 | C05–C06 | — | 13–18, 53–54 | 7/8 |
| Narrativas y temas emergentes | F19–F24 | C07–C08 | — | 19–24, 55–56 | 5/8 |
| Actores y prominencia | F25–F30 | C09–C10 | — | 25–30, 57–58 | 6/8 |
| Crisis, controversias y casos | F31–F36 | C11–C12 | — | 31–36, 59–60 | 7/8 |
| Doble materialidad y regulación | F37–F42 | C13–C14 | — | 37–42, 61–62 | 7/8 |
| Decisiones de producto y evaluación | F43–F48 | C15–C16 | — | 43–48, 63–64 | 4/8 |

### P06 — Cruce de conocimiento interno y señales externas

Módulo propuesto: `Saber+Escuchar` · 96 preguntas · ~183k tokens · 38 fuentes · preguntas sin bandera: 4/96

| Eje | F | C | X | Líneas en `respuestas/P06.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Modelo de afirmación y evidencia | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Fuentes internas y externas | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Identidad de entidades y acontecimientos | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| Temporalidad y versiones | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Arquitectura de procesamiento | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Tipos de discrepancia y respuesta | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Evaluación con casos de referencia | F37–F42 | C13–C14 | — | 37–42, 61–62 | 0/8 |
| Privacidad y límites epistémicos | F43–F48 | C15–C16 | — | 43–48, 63–64 | 0/8 |
| Profundización · Grafo de afirmaciones | — | — | X01–X08 | 65–72 | 1/8 |
| Profundización · Resolución de contradicciones complejas | — | — | X09–X16 | 73–80 | 1/8 |
| Profundización · Seguridad en recuperación combinada | — | — | X17–X24 | 81–88 | 1/8 |
| Profundización · Ablación y valor del cruce | — | — | X25–X32 | 89–96 | 1/8 |

### P07 — Preparación ejecutiva y apoyo estratégico

Módulo propuesto: `Hablar` · 64 preguntas · ~87k tokens · 39 fuentes · preguntas sin bandera: 0/64

| Eje | F | C | X | Líneas en `respuestas/P07.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Objetivo del brief ejecutivo | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Preguntas difíciles y escenarios | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Mensajes y líneas aprobadas | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| Simulación y práctica de vocería | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Apoyo estratégico y límites | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Flujo de revisión humana | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Viabilidad comercial en Chile y Latinoamérica | F37–F42 | C13–C14 | — | 37–42, 61–62 | 0/8 |
| Calidad y evaluación de briefs | F43–F48 | C15–C16 | — | 43–48, 63–64 | 0/8 |

### P08 — Viabilidad, modelos de negocio y oportunidades

Módulo propuesto: `transversal_negocio` · 64 preguntas · ~92k tokens · 40 fuentes · preguntas sin bandera: 0/64

| Eje | F | C | X | Líneas en `respuestas/P08.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Problema, segmento y disposición a pagar | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Tamaño y límites del mercado | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Alternativas y sustitutos | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| Modelos de entrega | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Construir, comprar e integrar | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Costos y economía unitaria | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Diferenciación como hipótesis | F37–F42 | C13–C14 | — | 37–42, 61–62 | 0/8 |
| Experimentos comerciales | F43–F48 | C15–C16 | — | 43–48, 63–64 | 0/8 |

### P09 — Memoria de relaciones y gestión de compromisos

Módulo propuesto: `Relacionar` · 64 preguntas · ~90k tokens · 45 fuentes · preguntas sin bandera: 0/64

| Eje | F | C | X | Líneas en `respuestas/P09.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Mapa de actores y relaciones | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Historial de interacción | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Ficha de compromiso | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| Ciclo de vida y seguimiento | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Territorio y participación | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Registros públicos y obligaciones | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Herramientas existentes | F37–F42 | C13–C14 | — | 37–42, 61–62 | 0/8 |
| Calidad, acceso y correcciones | F43–F48 | C15–C16 | — | 43–48, 63–64 | 0/8 |

### P10 — Gestión y aprobación de la comunicación corporativa

Módulo propuesto: `Hablar` · 64 preguntas · ~99k tokens · 41 fuentes · preguntas sin bandera: 0/64

| Eje | F | C | X | Líneas en `respuestas/P10.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Origen de solicitudes y señales | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Verificación de hechos y cifras | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Redacción y adaptación de mensajes | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| RACI, DACI y cadena de aprobación | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Estados, versiones y auditoría | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Reglas para automatizar o abstenerse | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Canales y escenarios | F37–F42 | C13–C14 | — | 37–42, 61–62 | 0/8 |
| Indicadores y límites normativos | F43–F48 | C15–C16 | — | 43–48, 63–64 | 0/8 |

### P11 — Gobernanza de información y operación entre clientes

Módulo propuesto: `transversal_gobernanza` · 64 preguntas · ~115k tokens · 51 fuentes · preguntas sin bandera: 0/64

| Eje | F | C | X | Líneas en `respuestas/P11.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Inventario y clasificación de datos | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Separación entre clientes | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Matriz dato, actor, acción y permiso | F13–F18 | C05–C06 | — | 13–18, 53–54 | 0/8 |
| Ciclo de vida y retención | F19–F24 | C07–C08 | — | 19–24, 55–56 | 0/8 |
| Proveedores y procesamiento externo | F25–F30 | C09–C10 | — | 25–30, 57–58 | 0/8 |
| Controles comprobables | F31–F36 | C11–C12 | — | 31–36, 59–60 | 0/8 |
| Incidentes y post-mortems | F37–F42 | C13–C14 | — | 37–42, 61–62 | 0/8 |
| Jurisdicciones y rectificaciones | F43–F48 | C15–C16 | — | 43–48, 63–64 | 0/8 |

### T01 — Evaluación y pilotos

Módulo propuesto: `transversal_evaluacion` · 96 preguntas · ~141k tokens · 75 fuentes · preguntas sin bandera: 52/96

| Eje | F | C | X | Líneas en `respuestas/T01.jsonl` | Sin bandera |
|---|---|---|---|---|---:|
| Hipótesis y compuertas del piloto | F01–F06 | C01–C02 | — | 1–6, 49–50 | 0/8 |
| Base manual y alternativas simples | F07–F12 | C03–C04 | — | 7–12, 51–52 | 0/8 |
| Casos de prueba y conjunto de referencia | F13–F18 | C05–C06 | — | 13–18, 53–54 | 5/8 |
| Rúbricas humanas | F19–F24 | C07–C08 | — | 19–24, 55–56 | 5/8 |
| Métricas y denominadores | F25–F30 | C09–C10 | — | 25–30, 57–58 | 5/8 |
| Atribución de valor e impacto | F31–F36 | C11–C12 | — | 31–36, 59–60 | 5/8 |
| Entrevistas y disposición a pagar | F37–F42 | C13–C14 | — | 37–42, 61–62 | 7/8 |
| Costos y continuidad operacional | F43–F48 | C15–C16 | — | 43–48, 63–64 | 4/8 |
| Profundización · Diseño estadístico y tamaño de muestra | — | — | X01–X08 | 65–72 | 6/8 |
| Profundización · Pruebas adversariales y seguridad | — | — | X09–X16 | 73–80 | 4/8 |
| Profundización · Adopción, confianza y trabajo humano | — | — | X17–X24 | 81–88 | 6/8 |
| Profundización · Reproducción y seguimiento | — | — | X25–X32 | 89–96 | 5/8 |

