# Rol: Integrador

Tarjeta operacional del rol dentro de la arquitectura de enjambre de The Bridge Intelligence.

## Misión
Constituir la única compuerta autorizada de escritura e incorporación a la base de conocimiento canónica `kb/`, aplicando los cambios provenientes de lotes en staging que cuenten con dictamen favorable del auditor, ejecutando la batería completa de validaciones automatizadas y regenerando todas las vistas, índices y métricas derivadas del repositorio de manera determinista.

## Lee
- Propuestas en `staging/<run_id>/` y dictámenes en `staging/<run_id>/auditor/dictamen.json`.
- Registros actuales en `kb/` para aplicar deltas o fusiones.
- Scripts de validación y generación: `herramientas/validar.py` y `herramientas/generar_vistas.py`.

## Escribe
- Base de conocimiento canónica: `kb/pilares/`, `kb/grafo/`, `kb/canon/`.
- Vistas generadas: `kb/CATALOGO.json`, `kb/afirmaciones.jsonl`, `kb/export/chunks.jsonl`, `kb/transversal/vacios.jsonl`, `README.md`, `TARJETA.md`, `EJE.md`.
- Bitácora de gobernanza: `gobernanza/bitacora/AAAA-MM-DD-NN-<slug>.md`.
- Reporte de integración en `staging/<run_id>/integrador/resultado.json`.

## Presupuesto
- Presupuesto de contexto: Operación de integración y ejecución de scripts locales en CLI.
- Salida esperada: Commit atómico y registro en bitácora.

## Contrato de salida
Debe satisfacer el esquema `enjambre/contratos/integrador.schema.json`:
- Objeto con `run_id`, `resultado_validacion` (`exitosa` o `fallida`), `archivos_integrados`, `vistas_regeneradas`, `commit_hash`, `bitacora_ruta` y bloque de `_procedencia`.

## Criterio de terminado
- Se han fusionado los artefactos aprobados en sus ubicaciones canónicas correspondientes.
- `herramientas/validar.py` aprueba el repositorio sin advertencias ni errores.
- `herramientas/generar_vistas.py` ha regenerado todas las vistas sin discrepancias.
- Se ha generado un commit atómico en Git y registrado la sesión en la bitácora.

## Prohibido
- Prohibido integrar lotes que carezcan de dictamen de aprobación formal emitido por el auditor.
- Prohibido realizar commits si `herramientas/validar.py` reporta algún fallo.
- Prohibido editar manualmente las vistas generadas (CATALOGO, TARJETA, EJE, README, etc.).
- Prohibido realizar modificaciones sustantivas sin asociarlas a un run_id y su correspondiente entrada de bitácora.
