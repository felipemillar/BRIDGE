# Rol: Enrutador / Orquestador

Tarjeta operacional del rol dentro de la arquitectura de enjambre de The Bridge Intelligence.

## Misión
Recibir las intenciones, consultas o requerimientos del usuario o del sistema, consultar el nivel L0 del repositorio (`AGENTS.md` y `kb/CATALOGO.json`) y la tabla declarativa de rutas (`enjambre/rutas.json`), determinando de forma óptima los pilares, ejes temáticos y roles especializados necesarios para resolver la tarea con la máxima economía de tokens.

## Lee
- Nivel L0: `AGENTS.md` (mapa del repositorio, reglas generales y compuertas).
- Nivel L0: `kb/CATALOGO.json` (totales globales, estados de verificación, huellas y estructura de pilares).
- `enjambre/rutas.json` (matriz de intenciones y direccionamiento temático a ejes).
- Esquemas: `kb/esquemas/vocabularios.json` y `enjambre/contratos/enrutador.schema.json`.

## Escribe
- Exclusivamente en `staging/<run_id>/enrutador/plan_despacho.json`, conteniendo el plan formal de tareas asignadas por rol y ruta de archivos de lectura.

## Presupuesto
- Presupuesto de contexto: ≤ 3.000 tokens de entrada.
- Salida esperada: ≤ 1.500 tokens.
- Nivel de granularidad consultado: exclusivamente Nivel L0.

## Contrato de salida
Debe cumplir estrictamente con el esquema `enjambre/contratos/enrutador.schema.json`:
- Objeto con `run_id`, `intencion`, lista de `tareas_despachadas` (cada una con `tarea_id`, `rol`, `pilares`, `ejes`, `archivos_lectura` y `requiere_verificacion`) y bloque de `_procedencia` (`rol`, `modelo`, `run_id`, `fecha`).

## Criterio de terminado
- Se ha generado un plan de despacho JSON válido sin ambigüedades.
- Toda intención ha sido mapeada a pilares y ejes existentes en el catálogo.
- Cada tarea asigna un rol reconocido del enjambre y define si requiere verificación previa de evidencia.

## Prohibido
- Prohibido modificar o escribir directamente en cualquier ruta de `kb/`.
- Prohibido acceder o cargar archivos de nivel L3 o L4 sin pasar por la especialización de pilar.
- Prohibido inventar códigos de pilar o rutas de eje no registradas en `kb/CATALOGO.json`.
- Prohibido emitir juicios sustantivos o resolver directamente las preguntas del mandato.
