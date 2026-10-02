# Propuesta de reorganización: BRIDGE como insumo para enjambres de agentes

**Fecha:** 2026-10-02 · **Estado:** propuesta, no ejecutada · **Base:** [INFORME_AUDITORIA.md](INFORME_AUDITORIA.md) e [INDICE.md](INDICE.md)

## 1. Problemas que la estructura actual impone a un enjambre

| Problema actual | Efecto en agentes |
|---|---|
| Respuestas en 12 JSONL de 79k–183k tokens | Un agente con contexto de 32k no puede abrir ni un pilar. Uno de 200k gasta su presupuesto en una sola lectura |
| JSONL compartidos y `BITACORA.md` antepuesta | Dos agentes que escriben a la vez generan conflictos o se pisan |
| 5,9 MB de scripts con las respuestas como literales | `grep` devuelve cada dato dos veces; hay ruido de 1,7M tokens |
| Calidad invisible dentro del dato | Nada distingue en el registro un `hecho_documentado` real de uno con cita sintética, así que el agente lo repite como hecho |
| Enums heterogéneos y grafo roto | Filtrar por `epistemic_status` o recorrer relaciones da resultados falsos |
| Rutas `file:///Users/fmillar/...` | Se rompen en cualquier otra máquina, contenedor o agente remoto |
| Instrucciones en `.agents/AGENTS.md` | Solo las encuentra Antigravity. Claude, Codex, Cursor o Gemini CLI buscan otros nombres |
| Derivados (síntesis, matriz, índice) mezclados con fuentes en la raíz | El agente no sabe qué es canon, qué es dato y qué es vista regenerable |

## 2. Principios de diseño

1. **Divulgación progresiva por niveles con presupuesto fijo.** Todo agente entra por un archivo ≤ 3k tokens y baja de nivel solo si lo necesita. Cada nivel cabe en el contexto de un modelo pequeño.
2. **Una unidad, un archivo, un ID.** La pregunta es la unidad de almacenamiento y la afirmación (`claim`) es la unidad de razonamiento. Así, los IDs estables se pueden direccionar por ruta sin parsing.
3. **Calidad como dato de primera clase.** Cada afirmación lleva su estado de verificación. Ningún agente necesita leer el informe de auditoría para saber si puede usarla.
4. **Separación por nivel de confianza:** `canon` (inmutable) → `kb` (datos curados) → vistas derivadas (regenerables) → `staging` (propuestas de agentes).
5. **Lectura libre, escritura canalizada.** Los agentes trabajadores nunca editan `kb/`: escriben en `staging/<run_id>/`. Solo un integrador valida y fusiona.
6. **Agnóstico de modelo:** archivos planos (Markdown, JSON y JSONL), JSON Schema, rutas relativas, un único `AGENTS.md` con alias por herramienta, sin dependencia obligatoria de una base vectorial. La exportación para RAG es opcional y se genera.
7. **Procedencia del agente.** Toda salida registra `{rol, modelo, run_id, fecha}`. Esto permite comparar modelos y auditar quién afirmó qué.

## 3. Estructura propuesta

```text
BRIDGE/
├── AGENTS.md                         # L0 · entrada única (≤2k tokens): mapa, reglas, rutas de lectura por rol
├── CLAUDE.md → AGENTS.md             # alias (symlink) para cada herramienta
├── GEMINI.md → AGENTS.md
├── .agents/AGENTS.md → ../AGENTS.md  # compatibilidad con Antigravity
├── README.md                         # portada para humanos, con cifras generadas (no escritas a mano)
│
├── kb/                               # BASE DE CONOCIMIENTO — solo lectura para trabajadores
│   ├── CATALOGO.json                 # L0 · pilares, ejes, conteos, estado de verificación, hashes, versión
│   ├── canon/
│   │   ├── mandato.md                # mandato original, intacto
│   │   ├── banco_preguntas.jsonl     # 864 × {id, pilar, eje, subeje, tipo, texto}
│   │   └── precedencia.yaml          # reglas editoriales por pilar, estructuradas
│   ├── esquemas/
│   │   ├── vocabularios.yaml         # enums únicos: epistemic_status, confidence, text_status, verificacion, módulos, tipos de entidad, predicados
│   │   ├── respuesta.schema.json
│   │   ├── afirmacion.schema.json
│   │   ├── fuente.schema.json
│   │   └── grafo.schema.json
│   ├── pilares/
│   │   └── P05-reputacion-narrativas-actores/
│   │       ├── TARJETA.md            # L1 · ≤3k tokens: alcance, ejes, fuentes rectoras, precedencia, estado de calidad, vacíos
│   │       ├── fuentes.jsonl         # manifiesto normalizado (L4 · índice de fuentes)
│   │       └── ejes/
│   │           └── 01-identidad-imagen-reputacion/
│   │               ├── EJE.md        # L2 · ≤2k tokens: respuestas cortas + banderas de las 8 preguntas (generado)
│   │               ├── P05-F01.json  # L3 · ~1,5k tokens: registro completo de una pregunta
│   │               └── …             # 8 archivos por eje
│   ├── afirmaciones.jsonl            # vista plana: 1.318 claims + evidencia + verificación (unidad para RAG y verificación)
│   ├── grafo/
│   │   ├── entidades.jsonl           # IDs únicos, tipos del vocabulario
│   │   ├── relaciones.jsonl          # 100 % integridad referencial, predicados controlados
│   │   └── contradicciones.jsonl     # resolution ∈ {resuelta, abierta} + regla_aplicada
│   ├── transversal/
│   │   ├── SINTESIS.md               # hoy indice_global.md (L1 transversal)
│   │   └── vacios.jsonl              # open_gaps consolidados → backlog de experimentos
│   └── export/                       # GENERADO, opcional
│       └── chunks.jsonl              # 1 chunk por claim y por short_answer, con metadatos para cualquier RAG
│
├── enjambre/                         # definición operacional del enjambre
│   ├── roles/                        # una tarjeta por rol (ver §5)
│   ├── rutas.yaml                    # intención → pilares/ejes → archivos a leer
│   ├── protocolos/
│   │   ├── lectura.md                # orden de niveles y presupuestos
│   │   ├── escritura.md              # staging, formato de propuesta, integración
│   │   └── verificacion.md           # cómo se promueve una afirmación a «verificada»
│   └── contratos/                    # JSON Schema de la salida de cada rol
│
├── staging/                          # salidas de agentes: staging/<run_id>/<rol>/…  (gitignored o rama propia)
│
├── gobernanza/
│   ├── auditorias/                   # 2026-10-01-preliminar.md, 2026-10-02-profunda.md, …
│   ├── cierre/                       # REGISTRO_DE_CIERRE.md, ejecucion.json (históricos)
│   └── bitacora/                     # un archivo por sesión: 2026-10-01-p05.md (sin conflictos)
│
├── herramientas/                     # código vivo y mínimo
│   ├── construir_indice.py           # hoy auditoria/construir_indice.py
│   ├── migrar.py                     # migración única actual → nueva estructura
│   ├── normalizar.py                 # enums + banderas de verificación
│   ├── validar.py                    # JSON Schema + integridad del grafo + conteos (gate de CI)
│   └── generar_vistas.py             # CATALOGO, TARJETA, EJE, afirmaciones, chunks, README
│
└── archivo/                          # o solo en el historial de Git (recomendado)
    └── scripts_generacion_2026-10-01/  # los 193 scripts actuales, fuera del camino de búsqueda
```

### Presupuesto por nivel

| Nivel | Archivo | Tokens | Quién lo lee |
|---|---|---:|---|
| L0 | `AGENTS.md` + `kb/CATALOGO.json` | ≤ 3k | Todos, siempre |
| L1 | `TARJETA.md` del pilar o `transversal/SINTESIS.md` | ≤ 3k | Especialistas y sintetizador |
| L2 | `EJE.md` | ≤ 2k | Quien trabaja un tema |
| L3 | `P05-F01.json` | ~1,5k (máx. ~3,6k) | Quien necesita el detalle |
| L4 | `fuentes.jsonl` → `original_url` | variable | Verificador |

Un agente con un contexto de 32k puede recorrer L0 → L1 → L2 → 8 × L3 de un eje completo (≈ 20k) y aún le queda margen para razonar.

## 4. Cambios en los datos (no solo en carpetas)

**Registro de pregunta (L3):** se conserva el contrato del mandato y se añaden campos sin borrar los originales.

```json
{
  "question_id": "P05-F04",
  "pilar": "P05", "eje": "Identidad, imagen y reputación", "eje_n": 1, "tipo": "F",
  "...": "llaves originales del mandato §3",
  "findings": [{
    "claim_id": "P05-F04-C1",
    "epistemic_status": "hecho_documentado",
    "epistemic_status_original": "fact",
    "confidence": "alta",
    "confidence_original": 0.95,
    "verificacion": {
      "estado": "no_verificada",
      "motivo": ["solo_sintesis_interna"],
      "verificado_por": null, "fecha": null, "metodo": null
    },
    "evidence": [{ "...": "...", "cita_sintetica": false }]
  }],
  "snapshot_at": null,
  "snapshot_nota": "valor original sobrescrito por normalize_status_and_timestamps.py; no proviene del conector",
  "_procedencia": { "generado_por": "append_p05_f01_f06.py", "migrado": "2026-10-xx" }
}
```

**Vocabulario de `verificacion.estado`:** `verificada` (pasaje original leído y concordante), `no_verificada`, `cita_sintetica` (las 439), `solo_sintesis_interna`, `refutada`. **Regla del enjambre:** solo las afirmaciones `verificada` pueden presentarse como hechos en una síntesis. Las demás se citan como hipótesis.

**Grafo:** IDs con prefijo por tipo (`org:meltwater`, `ley:cl-21719`, `rol:cco`, `met:ragas-faithfulness`), alias fusionados, predicados de un vocabulario cerrado de unas 30 relaciones y aristas colgantes eliminadas o convertidas en nodos. Una entidad que no es entidad (p. ej. «Ragas Faithfulness 0.932») se elimina.

## 5. Roles del enjambre

Cada rol tiene una tarjeta en `enjambre/roles/` con: misión, archivos que puede leer (por nivel), presupuesto, contrato de salida y criterio de terminado.

| Rol | Lee | Escribe en staging | Paralelismo |
|---|---|---|---|
| **Enrutador / orquestador** | L0 + `rutas.yaml` | Plan de tareas `{tarea, rol, archivos}` | 1 |
| **Especialista de pilar** | L1 + L2 + L3 de su pilar | Respuestas, análisis por eje | hasta 12 (o 5 por módulo) |
| **Verificador de evidencia** | 1 afirmación + su fuente L4 (URL) | `verificacion` + pasaje literal + localizador real | masivo: 1 afirmación por tarea |
| **Curador de grafo** | `grafo/` + afirmaciones de un pilar | Fusiones, aristas y tipos | por pilar |
| **Analista de contradicciones** | `contradicciones.jsonl` + claims citados | Resolución con regla de precedencia aplicada | por pilar |
| **Sintetizador transversal** | Solo L1, L2 y afirmaciones `verificada` | `SINTESIS.md` y respuestas a las 6 preguntas estratégicas | 1 |
| **Auditor** | Diff de staging + esquemas | Aprobado o rechazado con motivo | 1 por lote; idealmente **otro modelo** que el productor |
| **Integrador** | staging aprobado | Única escritura en `kb/` + regenera vistas | 1 (serializado) |

**Ejemplo de ruta (`enjambre/rutas.yaml`):**

```yaml
- intencion: "capacidades de competidores en escucha de medios en Chile"
  pilares: [P02, P03]
  ejes: ["P02/Plataformas de escucha y reputación", "P02/Profundización · Cobertura territorial y derechos", "P03/Acceso a prensa y web abierta"]
  rol: especialista_pilar
  requiere_verificacion: true
```

## 6. Protocolo de escritura

1. El agente recibe `run_id` y escribe solo en `staging/<run_id>/<rol>/`, un archivo por unidad (pregunta, afirmación o entidad), con `_procedencia: {rol, modelo, run_id, fecha}`.
2. `herramientas/validar.py` revisa el esquema, los vocabularios, la integridad referencial y que no haya `hecho_documentado` sin `verificada`.
3. El auditor revisa una muestra estratificada del lote y debe leer el **contenido del pasaje**, no solo su forma.
4. El integrador fusiona, regenera las vistas (CATALOGO, TARJETA, EJE, afirmaciones, chunks, README) y registra la sesión en `gobernanza/bitacora/<fecha>-<run_id>.md`.
5. Las vistas generadas nunca se editan a mano. Si una está mal, se corrige el dato o el generador.

## 7. Plan de migración

| Fase | Qué | Riesgo | Reversible |
|---|---|---|---|
| **0. Correcciones puntuales** | README, UUID en `sintesis/P01.md`, título de `fuentes/P05.json`, conteo de `fuentes/P01.json`, reclasificar T01-F06 | Bajo | Sí |
| **1. Normalización anotativa** | `normalizar.py`: enums canónicos + `*_original` + `verificacion` + `cita_sintetica`. No borra nada | Bajo | Sí |
| **2. Reestructura física** | `migrar.py` determinista con `git mv`: dividir los JSONL en 864 archivos por eje, mover canon/gobernanza y sacar scripts del árbol. Un commit | Medio (rutas) | Sí (un revert) |
| **3. Vistas y AGENTS.md** | Generar L0–L2, `afirmaciones.jsonl`, `chunks.jsonl`, `AGENTS.md` con alias y rutas relativas | Bajo | Sí |
| **4. Grafo** | Rehacer entidades y relaciones con integridad y vocabulario cerrado | Medio | Sí |
| **5. Enjambre piloto** | Roles + `rutas.yaml` + validador en CI. Primer trabajo real: **verificador de evidencia** sobre las afirmaciones de mayor riesgo (cifras, leyes, propiedad, capacidades de proveedores) | Medio | — |

Las fases 0–3 no requieren nuevas consultas a NotebookLM ni cambian el contenido sustantivo: solo lo hacen direccionable y honesto sobre su calidad. La fase 5 es la que convierte el corpus de hipótesis en base de hechos.

## 8. Decisiones abiertas

1. **Granularidad L3:** recomiendo un archivo por pregunta (864 archivos) por la escritura concurrente y el direccionamiento directo. La alternativa es un archivo por eje (108 archivos de ~12k tokens): menos archivos, pero más conflictos de escritura.
2. **Scripts históricos:** recomiendo retirarlos del árbol (quedan en Git con un tag `pre-migracion`). La alternativa es moverlos a `archivo/` y excluirlos con `.ignore`/`.rgignore`.
3. **Datos fuente:** recomiendo normalización anotativa (añadir campos y conservar los originales). La alternativa es reescribir los valores, lo que es más limpio pero pierde la evidencia de los defectos.
