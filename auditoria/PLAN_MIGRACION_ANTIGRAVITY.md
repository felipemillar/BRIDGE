# Plan de migración BRIDGE para enjambres de agentes

**Destinatario:** Antigravity, como agente ejecutor único.
**Emisor:** auditoría independiente del 2026-10-02.
**Punto de partida:** rama `main`, commit `03749c3`. En el árbol de trabajo solo debe aparecer `BITACORA.md` modificado y la carpeta `auditoria/` sin versionar.
**Comprobador oficial:** [comprobar_migracion.py](comprobar_migracion.py). Su SHA-256 se informa al ejecutor por separado y se registra en `migracion/estado.json` (§3.1).

> Este documento es tu única fuente de instrucciones para esta tarea. Trabajas en un **loop** (§3): en cada iteración ejecutas una sola tarea, corres el comprobador y registras el resultado. **No terminas** hasta que `python3 auditoria/comprobar_migracion.py --todo` imprima `RESULTADO: OK` y hayas entregado el informe final (§4.7). La única otra salida permitida es un **bloqueo** documentado (§3.5).

---

## 0. Contexto mínimo

Lee estos documentos **una vez**, al inicio. No los modifiques.

| Documento | Para qué |
|---|---|
| [INFORME_AUDITORIA.md](INFORME_AUDITORIA.md) | Qué está mal en los datos y por qué no se puede «declarar arreglado» sin evidencia |
| [PROPUESTA_REORGANIZACION.md](PROPUESTA_REORGANIZACION.md) | Estructura destino y racional de diseño |
| [INDICE.md](INDICE.md) | Mapa del contenido actual |
| `docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md` | Mandato original y banco exacto de 864 preguntas |

**Decisiones ya tomadas por el dueño del repositorio (no las reabras):**

- **D1.** Un archivo JSON por pregunta (864 archivos), agrupados por pilar y eje.
- **D2.** Los 193 scripts de `scripts/` salen del árbol de trabajo. Quedan recuperables en Git mediante el tag `pre-migracion`.
- **D3.** La normalización es **anotativa**: se agregan campos y se conserva cada valor original en `<campo>_original`. Nunca se borra un valor original.

**Lo que NO es tu trabajo:**

- Consultar NotebookLM.
- Generar respuestas, afirmaciones, fuentes, cifras o extractos nuevos.
- «Mejorar» la redacción de ningún registro.
- Decidir que algo está verificado sin haber leído la fuente (§4.6).

Esta migración **no cambia el contenido sustantivo**: lo hace direccionable y honesto sobre su calidad. Las huellas de contenido (§2, R1) lo garantizan.

---

## 1. Resultado esperado

```text
BRIDGE/
├── AGENTS.md                      # entrada única para cualquier agente (≤ 8000 caracteres)
├── CLAUDE.md → AGENTS.md          # enlaces simbólicos relativos
├── GEMINI.md → AGENTS.md
├── .agents/AGENTS.md → ../AGENTS.md
├── README.md                      # GENERADO
├── kb/
│   ├── CATALOGO.json              # GENERADO, L0
│   ├── canon/{mandato.md, banco_preguntas.jsonl, precedencia.json}
│   ├── esquemas/{vocabularios.json, respuesta|fuente|afirmacion|entidad|relacion|contradiccion.schema.json}
│   ├── pilares/<PILAR_DIR>/
│   │   ├── pilar.json             # metadatos del manifiesto
│   │   ├── fuentes.jsonl          # una fuente por línea
│   │   ├── TARJETA.md             # GENERADO, L1
│   │   ├── SINTESIS_LEGADO.md     # sintesis/<P>.md heredada
│   │   └── ejes/<EJE_DIR>/{EJE.md (GENERADO, L2), <QID>.json (L3)}
│   ├── afirmaciones.jsonl         # GENERADO
│   ├── indices/{preguntas.jsonl, fuentes.jsonl}   # GENERADO
│   ├── grafo/{entidades, relaciones, relaciones_descartadas, contradicciones, mapa_ids}.jsonl
│   ├── transversal/{SINTESIS_LEGADO.md, vacios.jsonl (GENERADO)}
│   └── export/chunks.jsonl        # GENERADO
├── enjambre/{roles/, contratos/, protocolos/, rutas.json}
├── gobernanza/{auditorias/, cierre/, bitacora/}
├── herramientas/{kb.py, normalizar.py, migrar.py, construir_indice.py, generar_vistas.py, validar.py}
├── migracion/{estado.json, decisiones.md, iteraciones/, piloto-001/, INFORME_FINAL.md}
├── staging/                       # ignorado por Git (salvo .gitkeep)
└── auditoria/                     # CONGELADA: no se mueve ni se edita durante la migración
```

---

## 2. Reglas absolutas

Romper cualquiera de estas reglas invalida la iteración. Si ocurre, revierte el commit de esa iteración.

- **R1. Contenido invariante.** Las huellas `H_CONTENIDO`, `H_ESTRUCTURA`, `H_EPISTEMICO` y `H_TIEMPOS`, y el conjunto de `source_id`, deben seguir siendo idénticos a la línea base. Por eso nunca modificas `question_text`, `short_answer`, `claim`, `claim_id`, los campos de evidencia (`source_id`, `source_title`, `original_url`, `locator`, `excerpt_short`) ni los campos de estructura de cada registro (`operational_model`, `entities`, `relations`, `comparisons`, `contradictions`, `metrics_and_denominators`, `bridge_implications`, `next_question_ids`). Tampoco agregas `open_gaps`.
- **R2. Archivos intocables:** todo `auditoria/` (incluidos este plan y el comprobador), el mandato y el tag `pre-migracion`. No muevas, renombres, reescribas ni vuelvas a crear el tag.
- **R3. Nunca relajes una comprobación.** No edites el comprobador ni lo envuelvas, reimplementes o sustituyas por otro. Si un control te parece incorrecto o imposible de cumplir, abres un bloqueo (§3.5). No busques un atajo.
- **R4. Sin datos incrustados en código.** Las herramientas leen los datos desde archivos. Ningún script contiene texto de respuestas o afirmaciones, ni listas de IDs escritas a mano, salvo las tablas de equivalencia del Anexo A.
- **R5. Sin rutas externas.** Las herramientas no leen ni escriben fuera del repositorio. Nada de `~/.gemini`, `/Users/...` ni historiales de conversación. Las herramientas no invocan `git`.
- **R6. No inventes valores.** Si un dato no existe, va `null` con una nota. Las fechas que escribas son la hora real del sistema (`date -u +%Y-%m-%dT%H:%M:%SZ`).
- **R7. Lenguaje honesto.** En ningún documento escribas «100 % PASS», «certificado», «auditado», «verificado» ni «completo». Lo único que reportas es la salida literal del comprobador.
- **R8. Git:** trabajas solo en la rama `migracion-enjambre`. Haces un commit por tarea con Conventional Commits: `migracion(F2.3): <qué>`. Nunca usas `--force`, `rebase` ni `reset --hard` sobre commits ya registrados en el estado. Nunca haces merge a `main`. Si existe el remoto `origin`, empujas la rama al cerrar cada fase.
- **R9. Reglas heredadas:** en todo `except` usas `type(err).__name__`; no expones trazas; no commiteas secretos.
- **R10. Rutas relativas** en todo documento nuevo o migrado. Nada de enlaces `file:///`.
- **R11. Ambigüedad:** si algo no está cubierto por el plan, eliges la opción que no altera datos y la registras en `migracion/decisiones.md` con fecha y motivo.

---

## 3. Protocolo de loop

### 3.1 Estado persistente

`migracion/estado.json` es la memoria del loop. Debe permitir retomar el trabajo desde cero contexto.

```json
{
  "plan": "auditoria/PLAN_MIGRACION_ANTIGRAVITY.md",
  "sha256_comprobador": "<valor informado por el dueño del repositorio>",
  "fase_actual": "F0",
  "fases_cerradas": ["PREP"],
  "iteracion": 7,
  "tareas": {
    "F0.1": {"estado": "hecha", "intentos": 1, "commit": "a1b2c3d"},
    "F0.2": {"estado": "pendiente", "intentos": 0, "commit": null}
  },
  "ultima_comprobacion": {"comando": "python3 auditoria/comprobar_migracion.py --hasta F0", "resultado": "FALLA (3)", "fecha": "2026-10-02T15:04:05Z"},
  "bloqueo": null
}
```

Los estados posibles de una tarea son `pendiente`, `hecha` y `bloqueada`. Las tareas se registran con los IDs exactos de §4.

### 3.2 Una iteración

Repite este ciclo hasta cumplir §3.4 o caer en §3.5:

1. **Sincronizar.** Lee `migracion/estado.json`. Verifica que `shasum -a 256 auditoria/comprobar_migracion.py` coincida con `sha256_comprobador`; si no coincide, abres un bloqueo. Verifica que `git status --porcelain` esté vacío; si no lo está, la iteración anterior quedó a medias: revisa el diff y complétalo o descártalo.
2. **Elegir.** Toma la primera tarea `pendiente` de `fase_actual`, en el orden de §4. Ejecuta **una sola tarea** por iteración. Las tareas con subtareas por pilar o por afirmación (F4.2, F5.5) cuentan como una iteración por subtarea.
3. **Ejecutar** la tarea según su especificación.
4. **Comprobar.** Corre `python3 auditoria/comprobar_migracion.py --hasta <fase_actual>` y guarda la salida **completa y literal**.
5. **Evaluar:**
   - Las compuertas de fases **ya cerradas** deben seguir en `[OK]`. Si alguna cae, es una **regresión**: tu siguiente acción es repararla, antes de cualquier otra cosa.
   - En la fase actual pueden seguir fallando controles que dependen de tareas **pendientes**. No pueden fallar los controles que la tarea recién hecha debía satisfacer: en ese caso, la tarea no está hecha.
6. **Registrar:**
   - Escribe `migracion/iteraciones/NNN.md` (Anexo D).
   - Actualiza `estado.json`: estado de la tarea, intentos, commit, `ultima_comprobacion` e `iteracion` + 1.
   - Haz el commit `migracion(<tarea>): <resumen>`.
7. **Cerrar la fase** cuando todas sus tareas estén `hecha` y `--hasta <fase>` dé `RESULTADO: OK`:
   - Agrega la fase a `fases_cerradas`.
   - Crea el tag anotado `migracion-<fase>-ok`.
   - Avanza `fase_actual` a la siguiente fase.
   - Haz el commit y, si existe `origin`, `git push -u origin migracion-enjambre --tags`.
8. Vuelve al paso 1.

### 3.3 Reintentos

Si una tarea no satisface sus controles, súmale un intento y vuelve a intentarla en la siguiente iteración, con un enfoque distinto y documentado. Al tercer intento fallido de la misma tarea, abres un bloqueo.

### 3.4 Condición de término

El trabajo termina **solo** cuando se cumplen todas estas condiciones:

1. Todas las tareas de PREP a F5 están en `hecha`.
2. `python3 auditoria/comprobar_migracion.py --todo` imprime `RESULTADO: OK` con el árbol de trabajo limpio.
3. `migracion/INFORME_FINAL.md` contiene esa salida literal (§4.7) y está commiteado.
4. Una segunda ejecución de `--todo`, después de ese commit, también imprime `RESULTADO: OK`.

Cuando se cumplan, **te detienes** y entregas el mensaje del Anexo F. No haces merge a `main`: la aceptación final la hace una revisión independiente.

### 3.5 Bloqueo (única salida anticipada)

Abres un bloqueo cuando ocurre cualquiera de estas situaciones:

- Una tarea fracasa tres veces.
- El SHA del comprobador no coincide.
- El punto de partida no es el esperado.
- Un control parece imposible o contradictorio con el plan.
- Una acción exigiría romper una regla de §2.

Al abrir un bloqueo:

1. Escribe `migracion/BLOQUEO.md` con: tarea, intentos, salida literal del comprobador, qué intentaste, hipótesis de la causa y qué decisión humana se necesita.
2. Pon `estado.json.bloqueo` con un resumen de una línea.
3. Haz el commit y detente.

No continúes con otras tareas mientras exista un bloqueo.

### 3.6 Si se agota tu contexto

No pasa nada. Todo está en `estado.json`, `iteraciones/` y Git. Al reanudar, empiezas por el paso 1 de §3.2. Nunca intentes «recordar» resultados: vuelve a correr el comprobador.

---

## 4. Fases y tareas

Cada fase tiene una compuerta en el comprobador (`--fase <F>`). La compuerta de una fase incluye todas las anteriores cuando se usa `--hasta`.

### 4.0 PREP: preparación

| Tarea | Especificación |
|---|---|
| **P.1** | Verifica el punto de partida: rama `main`, `HEAD` = `03749c3`, y en `git status --porcelain` solo ` M BITACORA.md` y `?? auditoria/`. Si es distinto, abres un bloqueo. |
| **P.2** | Calcula `shasum -a 256 auditoria/comprobar_migracion.py` y compáralo con el valor que te dio el dueño del repositorio. Si no coincide, abres un bloqueo. |
| **P.3** | Crea la rama: `git checkout -b migracion-enjambre`. |
| **P.4** | `git add auditoria BITACORA.md` y commit `docs(auditoria): auditoría profunda, índice, propuesta y plan de migración`. No modifiques esos archivos antes de commitearlos. |
| **P.5** | Crea el tag sobre ese commit: `git tag -a pre-migracion -m "Línea base auditada antes de la migración"`. |
| **P.6** | Crea `migracion/estado.json` (§3.1) con todas las tareas de §4 en `pendiente`, más `migracion/decisiones.md` y `migracion/iteraciones/`. Commit `chore(migracion): inicializar estado del loop`. |

**Compuerta PREP:** rama correcta; tag presente y apuntando a la línea base (verificado por huellas); `auditoria/` idéntica al tag; integridad de los documentos de auditoría; `estado.json` válido.

### 4.1 F0: correcciones puntuales

| Tarea | Especificación |
|---|---|
| **F0.1** | En `README.md`, retira toda afirmación de «100% PASS» o de auditoría aprobada y agrega una línea que remita a [INFORME_AUDITORIA.md](INFORME_AUDITORIA.md). No debe contener las cadenas `578`, `1.632`, `1632`, `559` ni `100% PASS`. |
| **F0.2** | En `sintesis/P01.md`, reemplaza el UUID `fa3bce30-c045-4299-8d8a-6b45f3df1a1a` por el canónico `21152990-b13f-4cda-bd6c-0286ca855ff9`. No toques la bitácora: es registro histórico. |
| **F0.3** | En `fuentes/P01.json`: agrega `"pilar_nombre_original": null` y `"pilar_nombre": "Asuntos corporativos y sus usuarios"`; además `"total_sources_original": 37` y `"total_sources": 39`. En `fuentes/P05.json`: `"pilar_nombre_original": "Metodologías de análisis y síntesis"` y `"pilar_nombre": "Reputación, narrativas y actores"`. |
| **F0.4** | En el registro `T01-F06`, en cada hallazgo: `"epistemic_status_original": "fact"` y `"epistemic_status": "hipotesis_diseno"`. Agrega al registro el campo `nota_auditoria` con este texto exacto: «Reclasificado en la auditoría del 2026-10-02: el caso de la compañía minera y sus métricas (Faithfulness 0.932, latencia p95 3.4 s, reducción de tiempo 64,5 %) no tiene registro primario en el corpus; se trata como escenario hipotético, no como resultado de un piloto.» No modifiques ni el texto ni los `open_gaps`. |
| **F0.5** | Elimina de `entidades.jsonl` la línea cuyo `entity_id` es `Ragas Faithfulness 0.932`. Regístralo en `migracion/decisiones.md`. |

**Compuerta F0:** 864 registros con IDs y textos del mandato; las 4 huellas invariantes; README sin cifras obsoletas; UUID corregido; manifiestos con nombre del mandato y conteo real; T01-F06 reclasificado; grafo sin «0.932».

### 4.2 F1: normalización anotativa

| Tarea | Especificación |
|---|---|
| **F1.1** | Crea `herramientas/kb.py`, la biblioteca común de lectura y escritura, **independiente del layout**. Si existe `kb/pilares/`, usa el layout nuevo; si no, `respuestas/*.jsonl` y `fuentes/*.json`. Debe ofrecer como mínimo: `raiz()` (resuelta desde `Path(__file__)`), `cargar_respuestas()`, `guardar_respuestas()`, `cargar_manifiestos()`, `guardar_manifiestos()` y `cargar_banco()`. Escribe JSON con `ensure_ascii=False`. Escribe un registro por línea en JSONL e indentación de 2 espacios en los archivos por pregunta. |
| **F1.2** | Crea `herramientas/normalizar.py`, que aplica las reglas N1–N8 del Anexo A con `kb.py`. Debe ser **idempotente**: ejecutarlo dos veces no cambia nada. Además, nunca debe sobrescribir un `*_original` ya existente ni rebajar los estados `verificada`, `refutada` o `no_verificable` (que llegan en F5). |
| **F1.3** | Ejecuta `python3 herramientas/normalizar.py`, revisa el diff por muestreo y haz el commit. |

**Compuerta F1** (conteos exactos esperados):

| Control | Valor esperado |
|---|---|
| `epistemic_status` | `hecho_documentado` 1011, `hipotesis_diseno` 157, `inferencia` 106, `declaracion_proveedor` 44 |
| `confidence` | `alta` 1091, `media` 227; 332 con `confidence_original` numérica |
| `text_status` de fuentes | `texto_sustantivo` 493, `fallida` 45, `duplicada` 10, `solo_navegacion` 2, `desconocida` 1 |
| `text_status` de evidencias | `texto_sustantivo` 1927, `fallida` 8 |
| Evidencias con `cita_sintetica` | 439 |
| Evidencias con `fuente_es_sintesis_interna` | 1057 |
| `verificacion.estado` | `cita_sintetica` 439, `solo_sintesis_interna` 303, `no_verificada` 576 |
| `metadata_notebooklm_crudo` conservado | 126 (P11 y T01) |
| `snapshot_at` y `retrieved_at` | todos `null`, con su `_original` |
| `quality` | recalculada según N8 |

Además: herramientas sin contenido incrustado y `normalizar.py` idempotente.

### 4.3 F2: reestructura física

| Tarea | Especificación |
|---|---|
| **F2.1** | Crea `herramientas/migrar.py`, que hace la reestructura de forma determinista leyendo con `kb.py`. Nombres de carpetas: función `slug` del Anexo B; `PILAR_DIR` = `<ID>-<slug(título del mandato)>`; `EJE_DIR` = `<NN>-<slug(nombre)>`. NN numera en orden de aparición en el mandato dentro del pilar: los 8 ejes F/C son 01–08 y los 4 subejes X (solo P02, P06 y T01) son 09–12, con el nombre del subeje. |
| **F2.2** | Ejecuta la migración de datos. Cada registro va a `kb/pilares/<PILAR_DIR>/ejes/<EJE_DIR>/<QID>.json`, con 5 campos nuevos tras `question_id`: `pilar`, `eje` (el nombre del eje; para X, «Profundización especializada»), `eje_n` (entero), `subeje` (nombre del subeje en X; `null` en F/C) y `tipo` (`F`, `C` o `X`). Cada manifiesto se divide en `pilar.json` (todo menos `sources`) y `fuentes.jsonl`. Crea `kb/canon/banco_preguntas.jsonl` con 864 filas `{question_id, pilar, eje, eje_n, subeje, tipo, question_text}`, extraídas del mandato. |
| **F2.3** | Reubica con `git mv` según la tabla del Anexo C. |
| **F2.4** | Divide `BITACORA.md` en `gobernanza/bitacora/AAAA-MM-DD-NN-<slug-del-título>.md`, un archivo por entrada `## [`. NN numera las sesiones del mismo día en orden cronológico (01 la más antigua). Conserva intacta la línea de encabezado de cada entrada. Luego elimina `BITACORA.md`. |
| **F2.5** | Convierte todos los enlaces `](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/...)` a rutas **relativas** hacia la nueva ubicación del destino, en todo el árbol salvo `auditoria/` y `kb/canon/`. Repara también los enlaces relativos que la reubicación haya roto. Si un destino ya no existe (por ejemplo, un script), reemplaza el enlace por texto plano más «(retirado; ver tag pre-migracion)». En el código, detecta estos enlaces con un patrón genérico (`file://` + cualquier prefijo + `/BRIDGE/` + ruta) sin escribir la ruta absoluta del usuario (R5). |
| **F2.6** | Elimina `respuestas/`, `fuentes/`, `sintesis/`, `scripts/` (incluido `__pycache__`) y `docs_mandato/`. Agrega `staging/` a `.gitignore` y crea `staging/.gitkeep`. |
| **F2.7** | Asegura que `kb.py` y `normalizar.py` funcionen sobre el layout nuevo y que `normalizar.py` siga siendo idempotente. |

`PILAR_DIR` exactos:

```text
P01-asuntos-corporativos-y-sus-usuarios
P02-empresas-y-soluciones-existentes
P03-monitoreo-del-entorno-y-acceso-a-fuentes
P04-conocimiento-documentado-de-la-corporacion
P05-reputacion-narrativas-y-actores
P06-cruce-de-conocimiento-interno-y-senales-externas
P07-preparacion-ejecutiva-y-apoyo-estrategico
P08-viabilidad-modelos-de-negocio-y-oportunidades
P09-memoria-de-relaciones-y-gestion-de-compromisos
P10-gestion-y-aprobacion-de-la-comunicacion-corporativa
P11-gobernanza-de-informacion-y-operacion-entre-clientes
T01-evaluacion-y-pilotos
```

Ejemplo de `EJE_DIR` (P02): `01-universo-comercial-y-deduplicacion` … `08-posicionamiento-y-alianzas`, `09-adquisiciones-y-estructura-de-grupos` … `12-certeza-comercial-y-madurez`.

**Compuerta F2:**
- Mandato byte a byte idéntico.
- Banco = mandato.
- 864 archivos de pregunta en su ruta y con los campos de ubicación correctos.
- 551 fuentes conservadas.
- Rutas heredadas ausentes y reubicadas presentes; raíz solo con entradas permitidas.
- Scripts recuperables desde el tag.
- Bitácora dividida sin perder entradas.
- Cero enlaces `file:///` y cero enlaces relativos rotos.
- `staging/` ignorado.
- Huellas invariantes.

### 4.4 F3: vistas, esquemas, validador y AGENTS.md

| Tarea | Especificación |
|---|---|
| **F3.1** | Crea `kb/esquemas/vocabularios.json` con las claves `epistemic_status`, `confidence`, `text_status`, `verificacion_estado`, `answer_status` y `modulo`, exactamente con los valores del Anexo A (en `modulo`: `Saber`, `Escuchar`, `Hablar`, `Relacionar`, `transversal`). Crea los 6 esquemas JSON (`respuesta`, `fuente`, `afirmacion`, `entidad`, `relacion`, `contradiccion`), cada uno con `"$schema": "https://json-schema.org/draft/2020-12/schema"`, campos obligatorios y enums referidos al vocabulario. Crea `kb/canon/precedencia.json` con las reglas editoriales del mandato (§2) por pilar y la `editorial_precedence_rule` de cada `pilar.json`. |
| **F3.2** | Adapta `herramientas/construir_indice.py` (parte de `auditoria/construir_indice.py`; **copia, no muevas**) para escribir `kb/indices/preguntas.jsonl` (864 filas, con `ruta` en lugar de `archivo` y `linea`) y `kb/indices/fuentes.jsonl` (551 filas). |
| **F3.3** | Crea `herramientas/generar_vistas.py`. Debe regenerar **todo** lo marcado GENERADO (Anexo E) e invocar internamente a `construir_indice.py`. Es determinista: no incluye fechas ni horas, ordena siempre y usa `huella_datos` en lugar de marcas de tiempo. Los Markdown generados empiezan con la línea exacta `<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->`. |
| **F3.4** | Crea `herramientas/validar.py`, que sale con código ≠ 0 ante cualquiera de estos casos: archivo de pregunta ausente o en ruta incorrecta; conteo ≠ 864; valor fuera de vocabulario; `source_id` de evidencia inexistente en el `fuentes.jsonl` de su pilar; `verificacion.estado` = `verificada` o `refutada` sin `pasaje`, `url_consultada` o `sha256_texto`; un hallazgo con regla `cita_sintetica` o `solo_sintesis_interna` en estado `verificada`; y, si existe `kb/grafo/mapa_ids.jsonl`, toda regla de grafo de F4. El comprobador te pondrá a prueba con mutaciones: no las detectes por nombre, valida de verdad. |
| **F3.5** | Ejecuta `generar_vistas.py` y `validar.py`, y haz el commit de las vistas generadas. |
| **F3.6** | Escribe `AGENTS.md` en la raíz siguiendo el Anexo G, y crea enlaces simbólicos **relativos**: `ln -s AGENTS.md CLAUDE.md`, `ln -s AGENTS.md GEMINI.md` y, tras eliminar el archivo anterior, `ln -s ../AGENTS.md .agents/AGENTS.md`. Las reglas del antiguo `.agents/AGENTS.md` (error masking, secretos, Git) quedan integradas en el nuevo. La regla de rutas `file://` se reemplaza por rutas relativas. En F3 no enlaces a `enjambre/`, que todavía no existe. |

**Compuerta F3:**
- Herramientas completas y limpias.
- AGENTS.md y sus 3 alias.
- CATALOGO ≤ 10000 caracteres, sin marcas de tiempo y con totales correctos.
- 12 TARJETA.md y 108 EJE.md dentro de presupuesto.
- 1318 afirmaciones; 2182 chunks; 470 vacíos; índices 864/551.
- Vocabularios y esquemas.
- README generado.
- Las vistas versionadas son exactamente las que produce `generar_vistas.py` en una copia limpia.
- `validar.py` aprueba el repositorio y rechaza 4 mutaciones.

### 4.5 F4: grafo de conocimiento

| Tarea | Especificación |
|---|---|
| **F4.1** | Agrega a `vocabularios.json` la clave `tipo_entidad`, con los 11 tipos del mandato (`organizacion`, `persona_rol`, `documento`, `fuente`, `tema`, `evento`, `compromiso`, `producto`, `riesgo`, `metrica`, `experimento`), y la clave `predicado`, con el vocabulario cerrado del Anexo H (entre 5 y 40 entradas en snake_case). Si agregas un predicado, regístralo en `decisiones.md`. |
| **F4.2.\<PILAR\>** (12 subtareas) | Haz la resolución de entidades de las que mencionan ese pilar. Una entidad que aparece en varios pilares se resuelve en la subtarea del primero (orden P01→T01) y las siguientes la reutilizan. El nuevo `entity_id` es `<prefijo>:<slug>`, con prefijos `org`, `rol`, `doc`, `fte`, `tema`, `evt`, `comp`, `prod`, `riesgo`, `met`, `exp`. Fusiona variantes (p. ej. Meltwater ×4, Ragas ×4, Ley 21.719 ×3, GDPR ×3) y conserva todos los nombres en `aliases` y todos los IDs heredados en `ids_legado`. Las leyes y normas son `documento`, con `subtipo: "norma"`. Elimina, con motivo, las que no son entidades: valores de métricas, casos hipotéticos, vacíos, esquemas internos. Escribe `kb/grafo/entidades.jsonl` y `kb/grafo/mapa_ids.jsonl` con `{id_legado, accion: conservado\|fusionado\|eliminado, id_nuevo, motivo}`. Debe cubrir **una vez** cada uno de los 1515 IDs únicos de `pre-migracion:entidades.jsonl`, incluido «Ragas Faithfulness 0.932» como `eliminado`. |
| **F4.3** | Reconstruye `kb/grafo/relaciones.jsonl`: cada relación lleva `indice_legado`, que es su posición base 0 en `pre-migracion:relaciones.jsonl`. Usa IDs nuevos, predicados del vocabulario y solo `evidence_claim_ids` existentes. Las que no puedan cumplir esas condiciones van a `relaciones_descartadas.jsonl` con `indice_legado` y `motivo`. Entre los dos archivos deben aparecer los índices 0–476, una vez cada uno. No crees relaciones nuevas. |
| **F4.4** | Normaliza `kb/grafo/contradicciones.jsonl` (93 filas): `resolution_original` guarda el valor anterior; `resolution` vale `resuelta` si el valor anterior era `resuelta` o cualquier texto libre de resolución (p. ej. «Prevalece…», «Conforme a…»), y `abierta` si era `abierta` o `null`. Agrega `regla_aplicada`, con el texto anterior cuando era texto libre y `null` en otro caso. Los `claim_ids` inexistentes pasan a `claim_ids_no_encontrados`. |
| **F4.5** | Activa las reglas de grafo en `validar.py`, regenera las vistas (los totales de CATALOGO incluyen entidades, relaciones y contradicciones) y haz el commit. **No modifiques** los campos `entities` y `relations` dentro de los registros de pregunta (R1). |

**Compuerta F4:**
- Vocabularios de tipo y predicado.
- Entidades válidas y únicas.
- `mapa_ids` completo (1515).
- Relaciones con integridad referencial total.
- Las 477 relaciones heredadas contabilizadas.
- 93 contradicciones canónicas.
- `validar.py` rechaza una relación colgante.

### 4.6 F5: enjambre y piloto de verificación

| Tarea | Especificación |
|---|---|
| **F5.1** | Escribe `enjambre/roles/<rol>.md` para los 8 roles: `enrutador`, `especialista_pilar`, `verificador_evidencia`, `curador_grafo`, `analista_contradicciones`, `sintetizador_transversal`, `auditor` e `integrador`. Cada archivo tiene ≤ 6000 caracteres y las secciones `## Misión`, `## Lee`, `## Escribe`, `## Presupuesto`, `## Contrato de salida`, `## Criterio de terminado` y `## Prohibido`. El contenido sale de la tabla de roles de §5 de la PROPUESTA. |
| **F5.2** | Escribe `enjambre/contratos/<rol>.schema.json` (8 archivos, con `$schema`), que describen la salida que cada rol deja en `staging/<run_id>/<rol>/`. Toda salida incluye `_procedencia: {rol, modelo, run_id, fecha}`. |
| **F5.3** | Escribe `enjambre/protocolos/lectura.md` (niveles L0–L4 y presupuestos), `escritura.md` (staging → validar → auditor → integrador) y `verificacion.md` (el método de F5.5). |
| **F5.4** | Escribe `enjambre/rutas.json`: una lista de al menos 24 rutas `{intencion, pilares, ejes: ["P05/01", …], rol, requiere_verificacion}` que, en conjunto, cubra los 12 pilares. |
| **F5.5.\<CLAIM_ID\>** (59 subtareas, Anexo I) | Verifica una afirmación de la muestra según el método de esta fase. Ejecuta **una afirmación por iteración**. |
| **F5.6** | Ejecuta `normalizar.py` (recalcula `quality` con los nuevos estados) y `generar_vistas.py`. Escribe `migracion/piloto-001/INFORME.md` con una tabla `claim_id | estado | url | pasaje o motivo` de las 59 afirmaciones y las tasas por estado. |
| **F5.7** | Agrega a `AGENTS.md` los enlaces a `enjambre/` (manteniéndolo dentro de 8000 caracteres) y crea `gobernanza/bitacora/<fecha>-NN-migracion-enjambre.md` con el resumen de la migración (formato de bitácora del proyecto). |

**Método de verificación (F5.5). Este es el único lugar donde se lee contenido externo.**

1. Abre el archivo de la pregunta y localiza el hallazgo `<CLAIM_ID>`.
2. Elige una evidencia cuya fuente no sea síntesis interna, tenga `text_status: texto_sustantivo` y tenga URL (la `original_url` de la fuente en `fuentes.jsonl`, o la de la evidencia).
3. Descarga la URL y extrae el texto plano. Guárdalo en UTF-8 en `staging/piloto-001/cache/<sha256>.txt`, donde `<sha256>` es el SHA-256 de los bytes exactos del archivo guardado.
4. Busca en ese texto un pasaje que **respalde** o **contradiga** la afirmación tal como está escrita. Copia el pasaje **literalmente** desde el archivo guardado, con un máximo de 600 caracteres. Nunca lo parafrasees ni traduzcas, y nunca lo tomes de otro lugar.
5. Asigna el estado:
   - `verificada`: el pasaje respalda la afirmación completa.
   - `refutada`: el pasaje la contradice.
   - `no_verificable`: la URL no es accesible, tiene paywall o CAPTCHA, o el pasaje no existe. En este caso: `pasaje: null` y `motivos` con `url_inaccesible`, `paywall_o_captcha` o `pasaje_no_encontrado`.

   **No hay cuota de verificadas:** `no_verificable` es un resultado válido y honesto.
6. Escribe en `verificacion`: `estado`, `motivos`, `verificado_por: {rol: "verificador_evidencia", modelo: "<tu identificador real de modelo>", run_id: "piloto-001"}`, `fecha` (hora UTC real), `metodo: "lectura_url_original"`, `pasaje`, `url_consultada`, `sha256_texto` y `source_id_verificado`. **No cambies** el `claim` ni la evidencia, ni el estado de ninguna otra afirmación.

**Compuerta F5:**
- Roles, contratos, protocolos y rutas válidos.
- Las 59 afirmaciones de la muestra con estado de piloto, fecha real y, si son `verificada` o `refutada`, un pasaje que aparece literalmente en el archivo de caché cuyo hash coincide.
- Ninguna otra afirmación cambió de estado.
- Informe del piloto, bitácora e informe final presentes.
- Árbol limpio.

### 4.7 Cierre

1. Ejecuta `python3 auditoria/comprobar_migracion.py --todo > /tmp/comprobacion_final.txt` (archivo temporal fuera del repositorio).
2. Escribe `migracion/INFORME_FINAL.md` con:
   - la salida literal del comprobador en un bloque de código;
   - tabla de fases con commit y tag de cierre;
   - número de iteraciones y de reintentos;
   - decisiones registradas;
   - resultados del piloto por estado;
   - límites conocidos (todo lo no verificado sigue `no_verificada`).
3. Haz el commit `docs(migracion): informe final`.
4. Ejecuta de nuevo `--todo`. Si imprime `RESULTADO: OK`, cumples §3.4: detente y entrega el mensaje del Anexo F.

---

## Anexo A: reglas de normalización (F1)

**N1. `epistemic_status`.** Los valores canónicos son `hecho_documentado`, `declaracion_proveedor`, `inferencia` e `hipotesis_diseno`. Si el valor actual no es canónico: `epistemic_status_original = valor actual` y `epistemic_status = tabla[valor]`.

| Original | Canónico |
|---|---|
| `fact` | `hecho_documentado` |
| `hypothesis`, `propuesta_arquitectura_formal`, `diseno_de_datos_formal`, `diseno_experimental_formal`, `patron_diseno_ciberseguridad`, `control_de_ciberseguridad_formal`, `taxonomia_operacional_gobernanza`, `regla_control_riesgo_reputacional`, `principio_metodologico_formal` | `hipotesis_diseno` |
| `modelo_computacional_probado`, `modelo_operacional_probado`, `caso_de_prueba_empirico`, `estandar_seguridad_comprobado`, `prevalencia_editorial_correccion`, `vacio_empirico_documentado`, `patologia_epistemica_documentada`, `principio_de_impacto_amec` | `inferencia` |

**N2. `confidence`.** Si es numérica: `confidence_original = número` y `confidence` = `alta` si ≥ 0.90, `media` si ≥ 0.70 y `baja` en otro caso.

**N3. `text_status` de fuentes.** Los valores canónicos son `texto_sustantivo`, `resumen_parcial`, `solo_navegacion`, `captcha`, `fallida`, `duplicada` y `desconocida`. Si el valor no es canónico: `text_status_original` y el valor según la tabla:

| Original | Canónico |
|---|---|
| `fallida_o_bloqueada`, `error_extraccion`, `fuente_fallida`, `error_extraccion_o_duplicado` | `fallida` |
| `directorio_navegacional_no_sustantivo` | `solo_navegacion` |
| `ficha_abstract_duplicada` | `duplicada` |
| `atribucion_comercial_erronea` | `desconocida` |

**N4. `original_url` de fuentes.** Si es una lista (metadato crudo de NotebookLM en P11 y T01): `metadata_notebooklm_crudo = lista` y `original_url = lista[7][0]` si es un texto que empieza por `http`; si no, `null`.

**N5. Evidencias:**
- `text_status` = el `text_status` normalizado de su fuente; si cambia, se guarda `text_status_original`.
- `cita_sintetica` = `true` si `locator` contiene «Sección sustantiva vinculada».
- `fuente_es_sintesis_interna` = el `is_internal_synthesis` de su fuente.
- `retrieved_at_original` = el valor actual, y `retrieved_at` = `null`.

**N6. `verificacion`** en cada hallazgo, con las llaves `{estado, motivos, verificado_por, fecha, metodo, pasaje}`:
- `estado` = `cita_sintetica` si alguna evidencia la tiene; si no, `solo_sintesis_interna` si todas las evidencias son de síntesis interna; si no, `no_verificada`.
- `motivos` = lista de los aplicables entre `cita_sintetica`, `solo_sintesis_interna`, `fuente_no_sustantiva`, `confianza_numerica_original` y `estado_epistemico_no_canonico_original`.
- Las demás llaves van en `null`.
- Nunca se modifica un hallazgo cuyo estado ya sea `verificada`, `refutada` o `no_verificable`.

**N7. Tiempos del registro:**
- `snapshot_at_original` = el valor actual, y `snapshot_at` = `null`.
- `snapshot_nota` = «Valor original sobrescrito el 2026-10-01 por scripts/normalize_status_and_timestamps.py con una constante por pilar; no proviene de un registro del conector.»

**N8. `quality`.** Primero se guarda `quality_original` = el valor actual, solo si no existe. Luego se recalcula:
- `original_citations_resolved` = todos los hallazgos están en `verificada`.
- `correction_precedence_checked` = `null`.
- `duplicate_sources_counted_once` = `null`.
- `human_review_needed` = alguna de estas condiciones: `answer_status` = `parcial`; algún hallazgo en `cita_sintetica`, `solo_sintesis_interna`, `refutada` o `no_verificable`; o alguna evidencia con `text_status` distinto de `texto_sustantivo`. Tras F1 son 361 registros.

**Vocabularios adicionales (F3):**
- `verificacion_estado`: `no_verificada`, `cita_sintetica`, `solo_sintesis_interna`, `verificada`, `refutada`, `no_verificable`.
- `answer_status`: `respondida`, `parcial`, `sin_evidencia`, `fuente_fallida`, `conflicto`, `bloqueada`.
- `confidence`: `alta`, `media`, `baja`.

## Anexo B: función `slug`

```python
import re, unicodedata
def slug(texto):
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].rstrip("-")
```

## Anexo C: reubicaciones (F2.3)

| Origen | Destino |
|---|---|
| `docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md` | `kb/canon/mandato.md` (sin cambiar un byte) |
| `docs_mandato/auditoria-preliminar-cierre-antigravity.md` | `gobernanza/auditorias/2026-10-01-auditoria-preliminar.md` |
| `sintesis/<P>.md` | `kb/pilares/<PILAR_DIR>/SINTESIS_LEGADO.md` |
| `indice_global.md` | `kb/transversal/SINTESIS_LEGADO.md` |
| `entidades.jsonl`, `relaciones.jsonl`, `contradicciones.jsonl` | `kb/grafo/` |
| `REGISTRO_DE_CIERRE.md`, `ejecucion.json`, `matriz_cobertura.csv` | `gobernanza/cierre/` |

A cada `SINTESIS_LEGADO.md` y a `REGISTRO_DE_CIERRE.md` agrégales al inicio esta línea: `> Documento heredado del 2026-10-01. Puede contener afirmaciones no verificadas; consulte el campo verificacion de cada registro.` Esa es la única edición permitida en esos archivos, además de la conversión de enlaces de F2.5.

Al terminar F2, la raíz solo puede contener: `.git`, `.gitignore`, `.agents`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `README.md`, `kb`, `enjambre`, `gobernanza`, `herramientas`, `migracion`, `auditoria` y `staging`.

## Anexo D: plantilla de iteración (`migracion/iteraciones/NNN.md`)

````markdown
# Iteración NNN · <tarea> · intento <k>
- Fecha (UTC real):
- Fase: <F>   Tarea: <ID>   Commit previo: <hash>
## Qué hice
- …
## Archivos tocados
- …
## Comprobación
```text
<salida literal y completa de: python3 auditoria/comprobar_migracion.py --hasta <F>>
```
## Evaluación
- Regresiones: ninguna | <lista>
- Controles de esta tarea: OK | FALLA (<cuáles>)
- Siguiente paso:
````

## Anexo E: vistas generadas (F3.3)

| Vista | Contenido obligatorio | Límite |
|---|---|---|
| `kb/CATALOGO.json` | `huella_datos` (SHA-256 de los hashes ordenados de todos los `.json` y `.jsonl` de `kb/pilares/`); `totales {preguntas, hallazgos, evidencias, fuentes, entidades, relaciones, contradicciones}`; `verificacion {estado: n}`; `pilares[]` con `{pilar, titulo, ruta (carpeta del pilar), modulo, n_preguntas, n_ejes}`. Sin fechas. | ≤ 10000 caracteres |
| `TARJETA.md` (×12) | Marca GENERADO; secciones `## Alcance`, `## Ejes` (enlace relativo `ejes/<EJE_DIR>/EJE.md` por eje), `## Fuentes rectoras y precedencia`, `## Estado de verificación`, `## Vacíos abiertos` (los 10 de mayor prioridad), `## Cómo leer este pilar`. | ≤ 10500 caracteres |
| `EJE.md` (×108) | Marca GENERADO; por pregunta: ID, texto, los primeros 300 caracteres de `short_answer`, estados de verificación de sus hallazgos y enlace a su JSON. | ≤ 7000 caracteres |
| `kb/afirmaciones.jsonl` | 1318 filas: `{claim_id, question_id, pilar, eje_n, claim, epistemic_status, confidence, verificacion_estado, fuentes: [source_id], ruta}` | — |
| `kb/export/chunks.jsonl` | 864 de tipo `respuesta_corta` y 1318 de tipo `afirmacion`: `{chunk_id, tipo, texto (≤ 4000), metadatos {question_id, pilar, eje_n, …, verificacion_estado en afirmaciones}}` | — |
| `kb/transversal/vacios.jsonl` | Uno por cada `open_gap` (470): `{question_id, pilar, gap, minimum_validation, priority}` | — |
| `kb/indices/*.jsonl` | Ver F3.2 | — |
| `README.md` | Marca GENERADO en la primera línea; descripción breve; totales del catálogo; tabla de estados de verificación; enlaces a `AGENTS.md`, `kb/CATALOGO.json` y `gobernanza/auditorias/`. Sin las cadenas prohibidas de F0.1. | — |

## Anexo F: mensaje de término

> Migración completada en la rama `migracion-enjambre`. `python3 auditoria/comprobar_migracion.py --todo` → `RESULTADO: OK` (salida literal en `migracion/INFORME_FINAL.md`). Iteraciones: N. Bloqueos: 0. Piloto: V verificadas, R refutadas, NV no verificables de 59. Pendiente: revisión independiente y merge a `main` por parte del dueño del repositorio.

No agregues adjetivos ni conclusiones sobre la calidad de la base.

## Anexo G: contenido de `AGENTS.md` (F3.6)

Máximo 8000 caracteres. Debe incluir:

1. **Qué es** el repositorio, en 3 líneas.
2. **Mapa por niveles:**
   - L0: `AGENTS.md` y `kb/CATALOGO.json`.
   - L1: `TARJETA.md`.
   - L2: `EJE.md`.
   - L3: `<QID>.json`.
   - L4: `fuentes.jsonl` y la URL original.

   Indica el presupuesto de tokens aproximado de cada nivel.
3. **Regla de uso del conocimiento:** una afirmación solo puede presentarse como hecho si `epistemic_status` es `hecho_documentado` **y** `verificacion.estado` es `verificada`. Cualquier otra se cita como hipótesis, junto con su estado.
4. **Escritura:** nunca en `kb/` directamente. Las salidas van a `staging/<run_id>/<rol>/` y las integra solo el rol integrador después de `herramientas/validar.py`.
5. **Herramientas:** `validar.py`, `generar_vistas.py` y `normalizar.py`, con una línea de uso cada una.
6. **Reglas heredadas:** error masking con `type(err).__name__`, prohibición de secretos, Conventional Commits y rutas relativas.
7. **Bitácora:** un archivo por sesión en `gobernanza/bitacora/AAAA-MM-DD-NN-slug.md`.
8. En F5, el enlace a `enjambre/roles/` y a `enjambre/rutas.json`.

## Anexo H: vocabulario inicial de predicados (F4.1)

`es_parte_de`, `pertenece_a_grupo`, `adquirio_a`, `controla_a`, `ofrece_producto`, `compite_con`, `se_integra_con`, `regula_a`, `fiscaliza_a`, `exige_cumplimiento_de`, `establece_norma`, `publica`, `cita_a`, `respalda`, `contradice`, `reemplaza_a`, `deriva_de`, `mide`, `es_metrica_de`, `reporta_a`, `aprueba`, `es_responsable_de`, `participa_en`, `afecta_a`, `mitiga`, `genera_riesgo`, `ocurre_en`, `aplica_en_region`, `usa_tecnologia`, `evalua`.

Cada uno de los 411 predicados heredados se proyecta sobre uno de estos. Si no hay equivalente razonable, la relación va a `relaciones_descartadas.jsonl` con motivo `predicado_sin_equivalente`.

## Anexo I: muestra del piloto (F5.5)

Selección determinista: hallazgos `hecho_documentado` que no son `cita_sintetica` ni `solo_sintesis_interna`, con al menos una fuente externa sustantiva con URL, ordenados por SHA-256 del `claim_id`; se toman los 5 primeros por pilar (P06 solo tiene 4 elegibles). Total: 59.

```text
P01-F08-C1 P01-F04-C2 P01-F05-C4 P01-F41-C1 P01-F04-C3
P02-F01-C3 P02-F34-C1 P02-F25-C1 P02-F29-C1 P02-F30-C1
P03-F05-C1 P03-F21-C1 P03-F14-C1 P03-F03-C1 P03-F08-C1
P04-F01-C1 P04-F03-C1 P04-F17-C1 P04-F09-C1 P04-F13-C1
P05-C13-C1 P05-F23-C1 P05-F37-C1 P05-F29-C1 P05-F41-C1
P06-X05-C1 P06-X21-C1 P06-X13-C1 P06-X29-C1
P07-F38-C1 P07-F01-C1 P07-C05-C1 P07-F32-C1 P07-F37-C1
P08-F35-C1 P08-F23-C1 P08-F37-C1 P08-F17-C1 P08-F19-C1
P09-F46-C1 P09-F16-C1 P09-F21-C1 P09-F15-C1 P09-F12-C1
P10-F48-C1 P10-C13-C1 P10-F11-C1 P10-F31-C1 P10-F39-C1
P11-C05-C1 P11-F28-C1 P11-F36-C1 P11-C12-C1 P11-F02-C1
T01-F28-C1 T01-F38-C2 T01-F29-C1 T01-F36-C1 T01-X02-C1
```
