# Registro de Decisiones de Migración

Registro de decisiones tomadas durante el proceso de migración agéntica del repositorio BRIDGE conforme a la regla R11 del plan (`auditoria/PLAN_MIGRACION_ANTIGRAVITY.md`).

---

## 2026-10-02 - Decisión D-001: Resolución del Bloqueo en Tarea P.1

- **Fecha (UTC):** 2026-10-02T14:12:08Z
- **Fase / Tarea:** PREP / P.1
- **Situación:** En el primer intento de inicio de la fase PREP, el árbol de trabajo presentaba `README.md` modificado sin commitear respecto a `HEAD` (`03749c3`), habiendo sido revertido al contenido del commit previo `0e9cf75` (restaurando cifras desactualizadas de 578 fuentes, 1.632 entidades, 559 relaciones y la declaración «100% PASS»). Conforme a la regla de P.1 («Si es distinto, abres un bloqueo»), se documentó el bloqueo en `migracion/BLOQUEO.md` y se registró en el commit `ac2157f`.
- **Decisión:** Resuelto por decisión humana mediante la Opción A: descartar la regresión no confirmada de `README.md` (`git checkout -- README.md`) para retornar al estado canónico de `03749c3`.
- **Acción y Trazabilidad:** La rama del intento bloqueado fue renombrada a `migracion-intento-0` preservando el commit `ac2157f` para trazabilidad completa. La rama `migracion-enjambre` fue recreada limpiamente desde `main` (`03749c3`) para continuar con la ejecución de P.1 a P.6.

---

## 2026-10-02 - Decisión D-002: Eliminación de Entidad Espuria «Ragas Faithfulness 0.932»

- **Fecha (UTC):** 2026-10-02T14:23:05Z
- **Fase / Tarea:** F0 / F0.5
- **Situación:** En el inventario de entidades (`entidades.jsonl`), la línea 1376 contenía `entity_id: "Ragas Faithfulness 0.932"`, correspondiente a un valor de métrica generado a partir del escenario hipotético no documentado de T01-F06.
- **Decisión:** Conforme a la especificación de la tarea F0.5 y al hallazgo §2.4 del informe de auditoría independiente, se elimina dicha línea de `entidades.jsonl` ya que un valor métrico no constituye una entidad corporativa ni de conocimiento válida.
- **Acción:** Registro eliminado de `entidades.jsonl`.

