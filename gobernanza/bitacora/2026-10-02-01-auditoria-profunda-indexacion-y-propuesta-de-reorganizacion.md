## [2026-10-02] - Sesión de Trabajo: Auditoría Profunda, Indexación y Propuesta de Reorganización para Enjambres Agénticos
**Objetivo:** Auditar de forma independiente el estado real del repositorio tras el cierre reconciliado, generar un índice navegable de todo el contenido y proponer una estructura que permita a agentes de cualquier modelo consumir la base de forma eficiente.

### ✅ Cambios Realizados:
- Creada la carpeta [`auditoria/`](../../auditoria) con [`INFORME_AUDITORIA.md`](../../auditoria/INFORME_AUDITORIA.md), [`INDICE.md`](../../auditoria/INDICE.md), [`PROPUESTA_REORGANIZACION.md`](../../auditoria/PROPUESTA_REORGANIZACION.md) y el generador reproducible [`construir_indice.py`](../../auditoria/construir_indice.py).
- Generados `indice_preguntas.jsonl` (864 filas con archivo, línea, eje y banderas de calidad), `indice_fuentes.jsonl` (551 fuentes con sus citas) y `resumen_indice.json`.
- No se modificó ningún dato existente.

### 🧠 Decisiones y Notas de Diseño:
- La auditoría confirma forma completa (864/864 textos literales, 1.935/1.935 citas resuelven por ID), pero detecta 439 evidencias sintéticas (P01/P06, asignadas por heurística de subcadenas), 447 `hecho_documentado` respaldados solo por síntesis internas, marcas temporales sobrescritas con constantes, enums sin normalizar en 352 registros, un piloto ficticio vigente en T01-F06 y un grafo con 71 % de aristas colgantes. Solo 216/864 preguntas no tienen banderas.
- Se usan rutas relativas en los nuevos documentos, en lugar de `file:///Users/...`, para que funcionen en cualquier entorno de agente; la propuesta recomienda adoptarlo como regla.

### ⏳ Pendientes y Siguientes Pasos:
- Decidir la granularidad L3, el destino de los scripts históricos y si la normalización será anotativa o destructiva (ver §8 de la propuesta).
- Ejecutar las fases 0–3 de migración y luego un piloto de verificador de evidencia.
