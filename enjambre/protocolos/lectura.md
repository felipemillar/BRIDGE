# Protocolo de Lectura y Divulgación Progresiva

Este protocolo rige el acceso a la base de conocimiento canónica de **The Bridge Intelligence** para todos los agentes humanos y sintéticos del enjambre.

---

## 1. Principio Fundamental de Divulgación Progresiva

Para garantizar la máxima economía de tokens y permitir la interoperabilidad con modelos de cualquier ventana de contexto, ningún agente debe acceder a niveles profundos de detalle documental sin antes haber transitado y evaluado los niveles superiores de síntesis.

---

## 2. Los Cinco Niveles de Granularidad

| Nivel | Componente Canónico | Presupuesto Aprox. | Quién lo Lee y Cuándo |
| :--- | :--- | :--- | :--- |
| **L0** | `AGENTS.md` y `kb/CATALOGO.json` | ≤ 3.000 tokens | **Todos los agentes**, siempre como punto de entrada inicial. Contiene el mapa de navegación, vocabularios, totales globales y huellas criptográficas. |
| **L1** | `kb/pilares/<pilar>/TARJETA.md` y `kb/transversal/SINTESIS.md` | ≤ 3.000 tokens | **Especialistas de pilar** y **Sintetizador transversal**. Resume el alcance temático, fuentes rectoras, precedencia editorial y vacíos críticos. |
| **L2** | `kb/pilares/<pilar>/ejes/<eje>/EJE.md` | ≤ 2.000 tokens | Agentes asignados a un eje temático concreto. Proporciona las respuestas breves y banderas de calidad de las 8 preguntas del eje. |
| **L3** | `kb/pilares/<pilar>/ejes/<eje>/<qid>.json` | ~1.500 – 3.600 tokens | Agentes que requieren el detalle completo de hallazgos, evidencias, entidades y vacíos de una pregunta específica. |
| **L4** | `kb/pilares/<pilar>/fuentes.jsonl` y URL original | Variable / Documental | **Verificador de evidencia** y **Auditor**. Contiene los metadatos de las fuentes primarias y el texto documental recuperado. |

---

## 3. Rutas de Lectura Permitidas por Rol

1. **Enrutador / Orquestador:**
   - Lee exclusivamente L0 (`AGENTS.md`, `kb/CATALOGO.json`) y `enjambre/rutas.json`.
   - Prohibido descender a L2, L3 o L4 durante la fase de enrutamiento.

2. **Especialista de Pilar:**
   - Lee L1 (`TARJETA.md`), L2 (`EJE.md`) y los registros L3 (`<qid>.json`) de su pilar correspondiente.
   - Puede consultar el manifiesto L4 (`fuentes.jsonl`) para contextualizar citas.

3. **Verificador de Evidencia:**
   - Lee el registro L3 atómico de la afirmación (`claim_id`), el manifiesto L4 (`fuentes.jsonl`) y el documento primario original (o su copia en caché local).

4. **Curador de Grafo:**
   - Lee L0 (`kb/grafo/entidades.jsonl`, `relaciones.jsonl`, `mapa_ids.jsonl`), `kb/afirmaciones.jsonl` y `kb/esquemas/vocabularios.json`.

5. **Analista de Contradicciones:**
   - Lee L0 (`kb/grafo/contradicciones.jsonl`, `kb/afirmaciones.jsonl`, `kb/canon/mandato.md`) y L1 (`TARJETA.md`).

6. **Sintetizador Transversal:**
   - Lee L0 (`AGENTS.md`, `kb/CATALOGO.json`), L1 (`TARJETA.md`, `SINTESIS.md`), L2 (`EJE.md`) y afirmaciones L0 (`kb/afirmaciones.jsonl`) filtradas por verificación.

7. **Auditor:**
   - Lee artefactos en `staging/<run_id>/`, esquemas JSON en `kb/esquemas/` y `enjambre/contratos/`, y textos de caché en `staging/<run_id>/cache/`.

8. **Integrador:**
   - Lee artefactos aprobados en `staging/<run_id>/` y scripts de validación en `herramientas/`.

---

## 4. Prohibiciones Estrictas de Lectura

- Prohibido realizar lecturas directas masivas de todos los archivos JSON de un pilar de forma simultánea.
- Prohibido ignorar el estado de verificación al leer afirmaciones en L3 o `afirmaciones.jsonl`.
- Prohibido asumir que una fuente es primaria si figura clasificada como `solo_sintesis_interna` o `cita_sintetica`.
