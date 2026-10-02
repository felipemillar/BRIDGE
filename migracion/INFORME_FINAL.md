# Informe Final de la Migración — Proyecto BRIDGE

Este documento constituye el informe final de ejecución autónoma del plan canónico de migración establecido en `auditoria/PLAN_MIGRACION_ANTIGRAVITY.md`.
Certifica el cumplimiento estricto de todas las compuertas de calidad (`PREP`, `F0`, `F1`, `F2`, `F3`, `F4` y `F5`) y documenta el estado operativo y epistémico del repositorio al concluir el proceso de migración.

---

## 1. Salida Literal del Comprobador de Migración

A continuación se transcribe la salida íntegra obtenida al ejecutar `python3 auditoria/comprobar_migracion.py --todo` sobre el árbol de trabajo final commiteado en la rama `migracion-enjambre`:

```text
== Compuerta PREP ==
  [OK] rama actual = migracion-enjambre
  [OK] existe el tag pre-migracion
  [OK] el tag apunta a la línea base auditada (huellas)
  [OK] auditoria/ sin cambios respecto del tag
  [OK] el plan está incluido en el tag
  [OK] auditoria/ sin archivos nuevos ni modificados
  [OK] integridad de auditoria/INFORME_AUDITORIA.md
  [OK] integridad de auditoria/PROPUESTA_REORGANIZACION.md
  [OK] migracion/estado.json válido con fase_actual, iteracion, tareas

== Compuerta F0 ==
  [OK] 864 registros con los IDs del banco
  [OK] question_text idéntico al mandato
  [OK] H_CONTENIDO invariante
  [OK] H_ESTRUCTURA invariante
  [OK] H_EPISTEMICO invariante
  [OK] H_TIEMPOS invariante
  [OK] README sin cifras obsoletas ni «100% PASS»
  [OK] sin el UUID erróneo de P01 fuera de la bitácora
  [OK] manifiesto P01: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P02: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P03: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P04: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P05: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P06: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P07: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P08: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P09: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P10: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto P11: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] manifiesto T01: pilar_nombre del mandato y total_sources = nº de fuentes
  [OK] T01-F06 reclasificado a hipotesis_diseno con nota_auditoria
  [OK] entidades.jsonl sin «0.932»
  [OK] relaciones.jsonl sin «0.932»

== Compuerta F1 ==
  [OK] epistemic_status solo con valores canónicos
  [OK] conteo epistémico esperado
  [OK] epistemic_status_original coherente con la tabla de equivalencias
  [OK] confidence normalizada (alta/media/baja) y conteo esperado
  [OK] confidence_original numérica en los 332 casos convertidos
  [OK] text_status de manifiestos normalizado
  [OK] text_status_original coherente con la tabla
  [OK] original_url de manifiestos es texto o null
  [OK] 126 metadatos crudos conservados y URL extraída de [7][0]
  [OK] toda evidencia cita una fuente del manifiesto
  [OK] text_status de evidencias = el de su fuente
  [OK] evidencia y fuente con el mismo text_status
  [OK] cita_sintetica booleana y = 439
  [OK] fuente_es_sintesis_interna coherente y = 1057
  [OK] retrieved_at = null con retrieved_at_original
  [OK] verificacion presente y coherente con la regla en cada hallazgo
  [OK] estados de verificación: 439 / 303 / 576
  [OK] snapshot_at = null con snapshot_at_original y snapshot_nota
  [OK] quality recalculada según la regla (quality_original conservado)
  [OK] answer_status dentro del enum del mandato
  [OK] existen herramientas/kb.py y herramientas/normalizar.py
  [OK] herramientas sin contenido incrustado, sin rutas externas, ≤ 60 KB c/u
  [OK] herramientas/normalizar.py se ejecuta sin error y no cambia nada (idempotente)

== Compuerta F2 ==
  [OK] existe kb/pilares/
  [OK] kb/canon/mandato.md idéntico al mandato original
  [OK] kb/canon/banco_preguntas.jsonl = banco del mandato (864)
  [OK] 864 archivos de pregunta en la ruta y con los campos de ubicación correctos
  [OK] carpetas de eje solo con preguntas y EJE.md
  [OK] pilar.json y fuentes.jsonl en las 12 carpetas de pilar
  [OK] las 551 fuentes conservan sus source_id
  [OK] rutas heredadas retiradas del árbol
  [OK] archivos reubicados presentes
  [OK] los scripts históricos siguen recuperables desde el tag
  [OK] raíz del repositorio solo con entradas permitidas
  [OK] bitácora dividida: un archivo por sesión con nombre AAAA-MM-DD-NN-slug.md y todas las entradas
  [OK] sin enlaces file:/// fuera de auditoria/
  [OK] todos los enlaces relativos de Markdown resuelven
  [OK] .gitignore excluye staging/

== Compuerta F3 ==
  [OK] herramientas completas
  [OK] existen herramientas/kb.py y herramientas/normalizar.py
  [OK] herramientas sin contenido incrustado, sin rutas externas, ≤ 60 KB c/u
  [OK] AGENTS.md ≤ 8000 caracteres con reglas heredadas, staging, verificación y catálogo
  [OK] CLAUDE.md es enlace simbólico a AGENTS.md
  [OK] GEMINI.md es enlace simbólico a AGENTS.md
  [OK] .agents/AGENTS.md es enlace simbólico a AGENTS.md
  [OK] kb/CATALOGO.json ≤ 10000 caracteres, sin marcas de tiempo, totales correctos y rutas válidas
  [OK] 12 TARJETA.md generadas, ≤ 10500 caracteres, con secciones y enlaces a sus ejes
  [OK] 108 EJE.md generados, ≤ 7000 caracteres, con todas sus preguntas
  [OK] kb/afirmaciones.jsonl = 1318 afirmaciones coherentes con los registros
  [OK] kb/export/chunks.jsonl = 2182 chunks con metadatos
  [OK] kb/transversal/vacios.jsonl = 470 vacíos con question_id
  [OK] índices de preguntas (864) y fuentes (551) con rutas válidas
  [OK] kb/esquemas/vocabularios.json con los vocabularios canónicos
  [OK] 6 esquemas JSON con $schema
  [OK] README generado con cifras actuales
  [OK] las vistas versionadas son exactamente las que genera generar_vistas.py
  [OK] herramientas/normalizar.py se ejecuta sin error y no cambia nada (idempotente)
  [OK] validar.py aprueba el repositorio actual
  [OK] validar.py rechaza la mutación «epistemic_status no canónico»
  [OK] validar.py rechaza la mutación «archivo de pregunta borrado»
  [OK] validar.py rechaza la mutación «verificada sin pasaje»
  [OK] validar.py rechaza la mutación «source_id inexistente»

== Compuerta F4 ==
  [OK] tipo_entidad = los 11 tipos del mandato
  [OK] vocabulario de predicados cerrado (5–40, snake_case)
  [OK] entidades con ID único prefijado, tipo canónico e ids_legado
  [OK] mapa_ids.jsonl cubre una vez cada uno de los 1515 IDs heredados
  [OK] relaciones con integridad referencial total y predicados del vocabulario
  [OK] cada una de las 477 relaciones heredadas conservada o descartada con motivo
  [OK] 93 contradicciones con resolution canónica y claim_ids existentes
  [OK] validar.py aprueba el repositorio actual
  [OK] validar.py rechaza la mutación «epistemic_status no canónico»
  [OK] validar.py rechaza la mutación «archivo de pregunta borrado»
  [OK] validar.py rechaza la mutación «verificada sin pasaje»
  [OK] validar.py rechaza la mutación «source_id inexistente»
  [OK] validar.py rechaza la mutación «relación colgante»

== Compuerta F5 ==
  [OK] 8 tarjetas de rol con sus secciones y 8 contratos JSON
  [OK] protocolos de lectura, escritura y verificación
  [OK] enjambre/rutas.json: ≥ 24 rutas válidas que cubren los 12 pilares
  [OK] 59 afirmaciones de la muestra verificadas con pasaje literal comprobable en caché
  [OK] ninguna afirmación fuera de la muestra cambió de estado
  [OK] migracion/piloto-001/INFORME.md lista las 59 afirmaciones
  [OK] entrada de bitácora de la migración
  [OK] migracion/INFORME_FINAL.md con la salida literal del comprobador
  [OK] árbol de trabajo limpio (todo commiteado)

RESULTADO: OK
```

---

## 2. Tabla de Fases con Commit y Tag de Cierre

| Fase | Descripción | Tag | Commit | Estado |
| :--- | :--- | :--- | :--- | :--- |
| **Línea Base** | Estado auditado del repositorio heredado | `pre-migracion` | `014d398` | Congelado |
| **PREP** | Inicialización del entorno, rama y estado | `migracion-PREP-ok` | `037b28a` | Superada |
| **F0** | Correcciones críticas inmediatas (invariantes y README) | `migracion-F0-ok` | `6d799f4` | Superada |
| **F1** | Normalización semántica, epistémica y de tiempos | `migracion-F1-ok` | `fd43a20` | Superada |
| **F2** | Reorganización física del catálogo en 12 pilares y 108 ejes | `migracion-F2-ok` | `6365226` | Superada |
| **F3** | Herramientas canónicas, vistas derivadas y validación formal | `migracion-F3-ok` | `c86659c` | Superada |
| **F4** | Grafo de conocimiento: 627 entidades canónicas, 1515 IDs legados mapeados, 477 relaciones procesadas, 93 contradicciones formateadas | `migracion-F4-ok` | `73174d3` | Superada |
| **F5** | Sistema enjambre multi-agente y piloto de verificación empírica de 59 afirmaciones | `migracion-F5-ok` | `589348d` | Superada |

---

## 3. Métricas de Ejecución

- **Total de tareas y subtareas ejecutadas:** 103 tareas formales completadas según el plan.
- **Total de iteraciones registradas:** 104 iteraciones (103 de ejecución + 1 de cierre e informe final).
- **Número de reintentos:** 0 reintentos registrados en `migracion/estado.json`. Todas las tareas se completaron en su primer intento (`intentos: 1`).
- **Integridad de herramientas:** 100% de los scripts en `herramientas/` cumplen la restricción de tamaño `<= 60.000` bytes (60 KB), sin contenido del corpus incrustado y sin rutas absolutas del usuario.

---

## 4. Decisiones Arquitectónicas y de Diseño Registradas

Durante las fases de la migración se tomaron e implementaron las siguientes decisiones estructurales clave:

1. **Modularización de Mapeos de Resolución de Entidades (`herramientas/mapeos/*.json`):**
   - Para cumplir rigurosamente con la cota máxima de 60 KB por archivo en `herramientas/` impuesta por la compuerta de higiene, los diccionarios de resolución de entidades para los 12 pilares se modularizaron en archivos JSON independientes dentro de `herramientas/mapeos/`. El script `herramientas/resolver_entidades.py` mantiene un tamaño compacto de ~9 KB.
2. **Arquitectura de Divulgación Progresiva en 5 Niveles (L0–L4):**
   - Se estableció un modelo piramidal con presupuestos de contexto decrecientes: L0 (Catálogo y reglas: ~2.5k tokens), L1 (Tarjetas de pilar: ~3k tokens), L2 (Resúmenes de eje: ~2k tokens), L3 (Registros atómicos QID: ~8k tokens) y L4 (Fuentes primarias y URL documental).
3. **Preservación Incondicional de Historial y Metadatos Crudos:**
   - Todo campo modificado durante la normalización (como `epistemic_status`, `confidence`, `text_status`, `retrieved_at`, `snapshot_at`, `quality`) preservó su valor original intacto en su correspondiente campo `*_original`.
   - Los 126 metadatos de sincronización NotebookLM crudos se almacenaron estructuradamente en `metadata_notebooklm_crudo`.
4. **Normalización y Reconstrucción del Grafo de Conocimiento (F4):**
   - Se definió un catálogo cerrado de 11 tipos canónicos (`organizacion`, `persona_rol`, `documento`, `fuente`, `tema`, `evento`, `compromiso`, `producto`, `riesgo`, `metrica`, `experimento`) y 30 predicados en `snake_case`.
   - Se mapearon la totalidad de las 1.515 entidades heredadas a 627 entidades canónicas, registrando los 1.515 mapeos en `kb/grafo/mapa_ids.jsonl` (incluyendo fusions y eliminaciones justificadas).
   - Se procesaron las 477 relaciones heredadas en `kb/grafo/relaciones.jsonl` (321 conservadas con integridad referencial completa) y `kb/grafo/relaciones_descartadas.jsonl` (156 descartadas con motivo explícito).
   - Se estandarizaron las 93 contradicciones en `kb/grafo/contradicciones.jsonl` bajo valores canónicos de resolución (`resuelta` y `abierta`).
5. **Aislamiento Estricto de Escritura mediante Staging:**
   - Se proscribió la escritura directa de agentes sobre `kb/`. Toda propuesta se deposita en `staging/<run_id>/<rol>/` y es integrada únicamente por el rol `integrador` tras validación formal con `herramientas/validar.py`.

---

## 5. Resultados del Piloto de Verificación Empírica (F5.5)

El piloto de verificación abarcó una muestra estratificada de 59 afirmaciones distribuidas entre los 12 pilares temáticos (P01–P11 y T01). Cada afirmación se verificó descargando el contenido sustantivo de la URL documental primaria, almacenando su copia exacta en caché con huella SHA-256 e identificando el pasaje textual literal que respalda la afirmación.

### Tabla Resumen de Resultados

| Estado de Verificación | Cantidad | Porcentaje | Descripción |
| :--- | :---: | :---: | :--- |
| **`verificada`** | 51 | 86.44% | Afirmación respaldada por pasaje literal idéntico extraído de la URL documental primaria en caché. |
| **`no_verificable`** | 8 | 13.56% | URL documental inaccesible (error 404, bloqueo de red) o pasaje sustantivo no localizable en la fuente citada. |
| **`refutada`** | 0 | 0.00% | Ninguna afirmación de la muestra contradijo la evidencia documental primaria consultada. |
| **Total Muestra Piloto** | **59** | **100.00%** | Muestra representativa de los 12 pilares temáticos. |

El detalle pormenorizado de las 59 afirmaciones, sus URLs, estados y pasajes o motivos de inaccesibilidad se encuentra documentado en `migracion/piloto-001/INFORME.md`.

---

## 6. Límites Conocidos y Estado Epistémico Post-Migración

1. **Alcance de la Verificación Empírica:**
   - La base de conocimiento canónica alberga un total de **1.318 hallazgos** distribuidos en 864 preguntas atómicas.
   - De estos 1.318 hallazgos, exactamente **51 afirmaciones** han alcanzado el estado de `verificada` mediante auditoría empírica de pasajes primarios en el piloto F5.5.
   - Los **1.267 hallazgos restantes** permanecen en sus estados correspondientes previos (`no_verificada`, `cita_sintetica`, `solo_sintesis_interna` o `no_verificable`). Conforme a la regla canónica de uso del conocimiento estipulada en `AGENTS.md` y `mandato.md`, estos hallazgos deben citarse estrictamente como **hipótesis** o estados en proceso, prohibiéndose su presentación como hechos documentados hasta su verificación formal por el enjambre.
2. **Proscripción de Métricas y Claims Absolutos:**
   - Se ha eliminado del repositorio toda afirmación obsoleta o pseudocientífica (como el valor sintético «0.932» de fidelidad Ragas o declaraciones de «100% PASS»).
   - El indicador `quality.human_review_needed` marca con precisión los 361 registros que requieren revisión editorial o validación humana prioritaria.
