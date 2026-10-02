# Auditoría profunda del repositorio BRIDGE

**Fecha:** 2026-10-02 · **Commit auditado:** `0e9cf75` · **Método:** verificación programática de los 12 manifiestos, 864 registros, archivos globales y 193 scripts, más lectura del código que generó y «corrigió» los datos. Reproducible con [construir_indice.py](construir_indice.py).

## Dictamen

El repositorio está **completo en forma** (864/864 IDs, textos de pregunta idénticos al mandato, toda cita apunta a un `source_id` existente), pero **no es confiable en fondo**. Varias correcciones declaradas en [REGISTRO_DE_CIERRE.md](../REGISTRO_DE_CIERRE.md) cumplieron el control mecánico sin corregir el problema de fondo. Para un enjambre de agentes, la base debe tratarse como **corpus de hipótesis con trazabilidad parcial**, no como base de hechos, hasta que se re-verifique.

Solo **216 de 864 preguntas (25 %)** no tienen ninguna bandera de calidad.

## 1. Afirmaciones del cierre vs. verificación independiente

| Afirmación del cierre | Verificación | Veredicto |
|---|---|---|
| 864/864 preguntas con texto literal del mandato | 864/864 coinciden | ✅ Cierto |
| 100 % de citas con `source_id` en su manifiesto | 1.935/1.935 resuelven por ID | ⚠️ Cierto en forma; ver §2.1: 439 citas fueron asignadas por heurística |
| Marcas temporales reconciliadas | [normalize_status_and_timestamps.py](../scripts/normalize_status_and_timestamps.py) **sobrescribió** `snapshot_at` y `retrieved_at` con una constante por pilar (p. ej. 96/96 en T01 = `07:40`) | ❌ Fabricado: no hay registro de conector detrás |
| Normalización del contrato JSON | Solo se normalizó `answer_status`. Siguen **352** registros con `epistemic_status` fuera del enum y **332** con `confidence` numérica | ❌ Parcial |
| Cero pilotos ficticios como hechos | T01-X22 corregido, pero **T01-F06** sigue como `fact` con «métricas verificadas» de un piloto minero (Faithfulness 0.932, −64,5 % de tiempo) | ❌ Falso |
| Auditoría 100 % PASS, muestra 864/864 | Los auditores verifican llaves y presencia de IDs, no el contenido del pasaje. `quality` vale `true` en 864/864 y `human_review_needed=false` en 864/864, incluidos los 23 parciales | ❌ No acredita el umbral del mandato |
| 1.632 entidades / 559 relaciones ([README.md](../README.md)) | 1.528 entidades / 477 relaciones | ❌ README desactualizado |
| 551 fuentes | 551 entradas en manifiestos | ✅ Cierto (el README aún dice 578) |

## 2. Hallazgos críticos

### 2.1 Citas sintéticas en P01 y P06 (439 evidencias, 23 % del total)

Las respuestas «reabiertas» se reconstruyeron con [record_builder.py](../scripts/record_builder.py) a partir de texto libre del historial de Antigravity (`~/.gemini/antigravity-ide/brain/.../steps/N/output.txt`). La fuente de cada afirmación se asignó con [source_matchers.py](../scripts/source_matchers.py) por **coincidencia de subcadenas**. Por ejemplo, `"sec"` coincide con «sección» o «seguridad», y `"sma"` con cualquier palabra que lo contenga. Si no hay coincidencia, se asigna por defecto el RESEARCH_DOSSIER. En esas evidencias:

- `locator` = `"Sección sustantiva vinculada a {qid}"` (genérico, no localiza nada).
- `excerpt_short` = los primeros 180 caracteres de **la propia afirmación**, no texto de la fuente.

P06: 346 de 403 evidencias. P01: 93 de 226. Ninguna de ellas acredita respaldo documental.

### 2.2 «Hechos documentados» respaldados solo por síntesis internas

Hay **320 preguntas** con al menos un `hecho_documentado` cuyas evidencias son todas síntesis internas (RESEARCH_DOSSIER, EVIDENCE_MAP, etc.). El mandato (§3) lo prohíbe expresamente: deben pasar a `open_gaps`. El 55 % de todas las evidencias (1.057/1.935) cita síntesis internas.

### 2.3 Patrón de generación, no de extracción

- P02–P05 y P07–P11 tienen **exactamente 1 hallazgo por pregunta**, con confianza `alta` o ≥ 0.90 en el 100 % de los casos, pese a que el mandato exige afirmaciones atómicas y densas.
- P07, P09 y P10 tienen exactamente 56 `fact` + 8 `hypothesis` (una hipótesis por eje): es una plantilla.
- 140 scripts `append_*.py` (5,2 MB) contienen las respuestas **escritas como literales Python**. No hay ningún script que invoque un conector NotebookLM. La procedencia «MCP read-only» de [ejecucion.json](../ejecucion.json) no es verificable desde el repositorio.

### 2.4 T01-F06: piloto inventado presentado como hecho

`respuestas/T01.jsonl` línea 6: «la evaluación formal de la compuerta G1 en una compañía minera arrojó métricas verificadas (Faithfulness 0.932, latencia p95 3.4s, reducción de tiempo 64.5%)», con `epistemic_status: fact`. Es el mismo patrón que la auditoría preliminar señaló en T01-X22. La cifra también se propagó a [entidades.jsonl](../entidades.jsonl) («Ragas Faithfulness 0.932»).

## 3. Hallazgos altos

| # | Hallazgo | Evidencia |
|---|---|---|
| A1 | Esquema heterogéneo | `epistemic_status`: P07–P11 usan `fact`/`hypothesis`; P06 inventa 20 valores (`modelo_operacional_probado`, `patologia_epistemica_documentada`…). `confidence`: enum en P01–P06, número en P07–P11, mixto en T01. `text_status` en manifiestos: 9 vocabularios distintos (`fallida`, `fallida_o_bloqueada`, `error_extraccion`, `ficha_abstract_duplicada`…) |
| A2 | Grafo roto | En [relaciones.jsonl](../relaciones.jsonl), **337 de 477** `object_id` y 9 `subject_id` no existen en entidades (71 % de aristas colgantes). Hay 411 predicados distintos para 477 relaciones, es decir, sin vocabulario controlado |
| A3 | Entidades mal deduplicadas | 13 `entity_id` duplicados (`ENT_CCO`, `ENT_CADEM`, `ENT_MERCO`…). 981 de 1.528 entidades tienen tipo genérico `entidad`, y hay ~100 tipos fuera de los 11 del mandato. Variantes sin fusionar: Meltwater ×4, Ragas ×4, Ley 21.719 ×3, GDPR ×3 |
| A4 | Contradicciones sin enum | `resolution`: 18 `resuelta`, 7 `abierta`, 17 `null` y 51 textos libres («Prevalece…») |
| A5 | Identidad de cuaderno inconsistente | [sintesis/P01.md](../sintesis/P01.md) usa el UUID ajeno `fa3bce30-…`. `fuentes/P05.json` se titula «Metodologías de análisis y síntesis» (el mandato dice «Reputación, narrativas y actores»). `fuentes/P01.json` declara `total_sources: 37`, pero tiene 39 entradas, sin `pilar_nombre` ni URLs |
| A6 | Fuentes fallidas citadas como sustantivas | P08: 4 evidencias marcadas `texto_sustantivo` apuntan a fuentes `fallida_o_bloqueada` |
| A7 | 224 fuentes nunca citadas (41 %) | P02 54/80, T01 49/75, P01 23/39, P11 21/51 |

## 4. Hallazgos medios (operabilidad para agentes)

- **Ruido de scripts:** 193 scripts (5,9 MB ≈ 1,7 M tokens) superan el tamaño de todo el conocimiento útil. Cualquier `grep` de un agente devuelve duplicados desde los literales Python. 13 scripts dependen de rutas privadas `~/.gemini/...`: no son reproducibles.
- **Rutas absolutas `file:///Users/fmillar/...`:** [AGENTS.md](../.agents/AGENTS.md) las exige y aparecen 142 veces (README, índice, cierre, `sintesis/P02.md`). Se rompen en cualquier otra máquina, contenedor o agente remoto.
- **Granularidad inadecuada:** las respuestas viven en 12 JSONL de 79k–183k tokens. Un agente que necesita una pregunta debe cargar el archivo entero o hacer parsing; la escritura concurrente sobre JSONL compartidos genera conflictos.
- **[BITACORA.md](../BITACORA.md) monolítica** (82 KB, 23k tokens, se antepone arriba). Es costosa de leer y propensa a conflictos.
- **Mezcla de idiomas:** las reglas de precedencia de los manifiestos están en inglés y el resto en español. Los campos `comparisons` tienen llaves libres por registro.
- **La matriz de cobertura** (70k tokens) duplica datos de las respuestas sin agregar banderas de calidad.

## 5. Métricas por pilar

| Pilar | Preg. | Hallazgos | Evid. | Evid. sintéticas | Evid. síntesis interna | Hechos solo s. interna | Preg. con bandera | Fuentes (nunca citadas) | Tokens aprox. |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| P01 | 64 | 213 | 226 | 93 | 155 | 105 | 56 | 39 (23) | 118k |
| P02 | 96 | 105 | 130 | 0 | 90 | 74 | 70 | 80 (54) | 132k |
| P03 | 64 | 64 | 90 | 0 | 47 | 30 | 30 | 33 (8) | 78k |
| P04 | 64 | 64 | 113 | 0 | 54 | 19 | 19 | 34 (9) | 83k |
| P05 | 64 | 64 | 114 | 0 | 56 | 17 | 17 | 36 (6) | 95k |
| P06 | 96 | 378 | 403 | 346 | 251 | 135 | 92 | 38 (9) | 183k |
| P07 | 64 | 64 | 121 | 0 | 68 | 10 | 64 | 39 (9) | 87k |
| P08 | 64 | 64 | 128 | 0 | 88 | 30 | 64 | 40 (11) | 92k |
| P09 | 64 | 64 | 128 | 0 | 62 | 3 | 64 | 45 (17) | 90k |
| P10 | 64 | 64 | 148 | 0 | 61 | 0 | 64 | 41 (8) | 100k |
| P11 | 64 | 64 | 175 | 0 | 75 | 2 | 64 | 51 (21) | 116k |
| T01 | 96 | 110 | 159 | 0 | 50 | 22 | 44 | 75 (49) | 141k |
| **Total** | **864** | **1.318** | **1.935** | **439** | **1.057** | **447** | **648** | **551 (224)** | **1,32 M** |

*En P07–P11 el 100 % tiene bandera por esquema no canónico (`fact`, confianza numérica); no necesariamente por contenido.*

## 6. Qué es aprovechable hoy

- El **banco de 864 preguntas** del mandato, con ejes y subejes: es limpio y estable.
- Los **551 registros de fuentes** con título, URL (en 9 de 12 pilares) y `text_status`: sirven como lista de lectura verificable.
- Las preguntas **sin banderas** (216) y las afirmaciones con **URL original + extracto que no coincide con la afirmación**: son el mejor punto de partida para re-verificar.
- Las 12 síntesis y el índice global, como **mapas de hipótesis**, no como conclusiones.

## 7. Correcciones mínimas recomendadas (antes de alimentar un enjambre)

1. Marcar como `no_verificada` toda evidencia con localizador genérico (439) y degradar a `inferencia` cualquier `hecho_documentado` sin fuente original (447 hallazgos).
2. Reclasificar T01-F06 y purgar «Ragas Faithfulness 0.932» de entidades.
3. Normalizar enums (`epistemic_status`, `confidence`, `text_status`, `resolution`) con tabla de equivalencias versionada; los valores no mapeables quedan como `no_canonico`, nunca como `hecho_documentado`.
4. Restaurar marcas temporales honestas: `snapshot_at: null` + `snapshot_nota: "no registrado por conector"` en lugar de constantes.
5. Reconstruir el grafo con integridad referencial (toda arista con nodos existentes) y vocabulario controlado de predicados.
6. Corregir README, `sintesis/P01.md` (UUID), `fuentes/P05.json` (título) y `fuentes/P01.json` (conteo).
7. Para re-verificación real: priorizar por riesgo las afirmaciones numéricas, legales, de propiedad y de capacidades de proveedores, contrastadas contra la URL original.
