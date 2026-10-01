# The Bridge Intelligence — Programa de Investigación de Asuntos Corporativos

Repositorio central del programa integral de investigación y base de conocimiento canónica de **The Bridge Intelligence** (`thebridgeintelligence.ai`), desarrollado conforme al **Mandato de Extracción Densa de Conocimiento** (v1.0, 30 de septiembre de 2026).

---

## 📌 Resumen Ejecutivo del Programa

El programa consolida la base de conocimiento empírica, técnica y legal sobre los **12 cuadernos canónicos de NotebookLM**, cubriendo el ciclo metodológico cuádruple: **Saber** (memoria corporativa e inteligencia documental), **Escuchar** (monitoreo de señales de entorno y riesgos), **Hablar** (aprobación colegiada y consistencia de vocería) y **Relacionar** (gestión estructurada de compromisos y stakeholders), bajo la arquitectura de gobernanza multi-tenant y compuertas de decisión **Stage-Gate (G0–G3)**.

| Parámetro | Métrica Canónica |
| :--- | :--- |
| **Cuadernos Target** | 12 cuadernos canónicos (P01 a P11 + T01) |
| **Total Preguntas Ejecutadas** | **864 / 864 preguntas (100.0% completitud)** |
| **Desglose de Preguntas** | 576 Fundamentales (F) + 192 Contraste (C) + 96 Profundización (X) |
| **Universo de Fuentes** | 578 fuentes catalogadas y verificadas |
| **Evidencia Científica** | 11 PDFs de texto completo ArXiv incorporados (300k+ tokens científicos) |
| **Auditoría de Calidad** | **100% PASS** en auditorías estratificadas (0 fallas críticas) |
| **Entidades Deduplicadas** | 1.632 entidades en [`entidades.jsonl`](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/entidades.jsonl) |
| **Grafo de Relaciones** | 559 relaciones dirigidas en [`relaciones.jsonl`](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/relaciones.jsonl) |
| **Contradicciones Reconciliadas** | 93 discrepancias catalogadas en [`contradicciones.jsonl`](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/contradicciones.jsonl) |

---

## 📁 Estructura del Repositorio

```text
BRIDGE/
├── .agents/
│   └── AGENTS.md                  # Reglas del agente, seguridad y masking de errores
├── fuentes/                       # 12 manifiestos de fuentes por cuaderno (JSON)
│   ├── P01.json ... P11.json
│   └── T01.json
├── respuestas/                    # 12 archivos con 864 registros schema 20-atributos (JSONL)
│   ├── P01.jsonl ... P11.jsonl
│   └── T01.jsonl
├── sintesis/                      # 12 síntesis ejecutivas y matrices de trazabilidad (MD)
│   ├── P01.md ... P11.md
│   └── T01.md
├── scripts/                       # Scripts de ingesta, auditoría estratificada y compilación
├── BITACORA.md                    # Registro cronológico continuo de sesiones de trabajo (DevLog)
├── REGISTRO_DE_CIERRE.md          # Registro formal de cierre del programa (Mandato Sección 6)
├── indice_global.md               # Índice global de cuadernos y Síntesis Transversal
├── matriz_cobertura.csv           # Matriz exhaustiva de cobertura de las 864 preguntas
├── ejecucion.json                 # Telemetría global de ejecución y estados
├── entidades.jsonl                # Base canónica de 1.632 entidades deduplicadas
├── relaciones.jsonl               # Grafo canónico de 559 relaciones tipadas
├── contradicciones.jsonl          # Inventario de 93 contradicciones reconciliadas
└── README.md                      # Este documento
```

---

## 🧭 Documentos Clave de Consulta

- 📄 **[Índice Global y Síntesis Transversal](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/indice_global.md)**: Visión global de los 12 cuadernos y respuesta a las 6 preguntas estratégicas del mandato.
- 📋 **[Registro Formal de Cierre](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/REGISTRO_DE_CIERRE.md)**: Acta de cierre del programa según Sección 6 del mandato (cuentas, manifiestos, estados, cambios de corpus y certificación).
- 📊 **[Matriz de Cobertura Completa (864 IDs)](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/matriz_cobertura.csv)**: Tabla exhaustiva con IDs, textos exactos, estado de respuesta, confianza y citas.
- ⚙️ **[Telemetría de Ejecución JSON](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/ejecucion.json)**: Estadísticas consolidadas de ejecución y distribución de respuestas.
- 📝 **[Bitácora de Desarrollo](file:///Users/fmillar/Proyectos_Desarrollo/BRIDGE/BITACORA.md)**: Historial detallado de todas las sesiones de trabajo del proyecto.

---

## 🛡️ Principios Rectores y Gobernanza

1. **Prevalencia Canónica de Documentos Rectores:** Supremacía de `VERIFICATION_CORRECTIONS` y `QUALITY_ADDENDUM` sobre fichas preliminares o resúmenes de trabajo.
2. **Descalificación de Entidades Ajenas:** `bridgestudio.mx` queda excluida del corpus; la titular técnica es `thebridgeintelligence.ai`.
3. **Aislamiento Multi-Tenant en 4 Planos:** PostgreSQL Row-Level Security (RLS) forzado, Qdrant payload filters, Redis namespaces y Customer Managed Keys (CMK) en KMS.
4. **Gobernanza Stage-Gate Cuantitativa:** Ningún piloto avanza por afinidad comercial; compuertas G0–G3 basadas en Ragas Faithfulness ($\ge 0.90$), Citation Precision ($\ge 95\%$), WAP ($\ge 70\%$) y reducción de tiempo ($\ge 40\%$).
5. **Mitigación de Complacencia Automatizada:** Exigencia de un Diff Ratio de edición humana de $15\%$ a $30\%$; la aprobación sin revisión ($0.00$) se clasifica como fallo metodológico severo.
6. **Error Masking en Python:** Todo manejador de excepciones implementa `type(err).__name__` para evitar filtraciones de información en salidas directas.
