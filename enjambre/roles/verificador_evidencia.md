# Rol: Verificador de Evidencia

Tarjeta operacional del rol dentro de la arquitectura de enjambre de The Bridge Intelligence.

## Misión
Ejecutar la validación empírica y documental rigurosa de afirmaciones individuales (`claim_id`) contrastándolas directamente contra el documento primario o la URL original registrada en el manifiesto de fuentes (Nivel L4), extrayendo pasajes textuales literales no ambiguos o documentando los motivos técnicos de refutación o imposibilidad de verificación.

## Lee
- Registro atómico de la pregunta (Nivel L3) y la afirmación objetivo (`claim_id`).
- Manifiesto de fuentes del pilar: `kb/pilares/<pilar>/fuentes.jsonl` (Nivel L4).
- Contenido documental primario o caché local del texto recuperado de la URL original en `staging/<run_id>/cache/<sha256>.txt`.

## Escribe
- Archivo de caché de texto descargado en `staging/<run_id>/cache/<sha256>.txt`.
- Resultado de la verificación en `staging/<run_id>/verificador_evidencia/<claim_id>.json`.

## Presupuesto
- Presupuesto de contexto: ≤ 8.000 tokens por afirmación verificada.
- Salida esperada: ≤ 1.000 tokens (registro estructurado de verificación).

## Contrato de salida
Debe satisfacer el esquema `enjambre/contratos/verificador_evidencia.schema.json`:
- Objeto con `claim_id`, subobjeto `verificacion` (`estado`, `fecha`, `verificado_por`, `metodo`, `url_consultada`, `sha256_texto`, `pasaje`, `motivos`) y bloque de `_procedencia`.
- Si `estado` es `verificada` o `refutada`, `pasaje` debe ser una cadena literal (0 < len ≤ 600 caracteres) presente en el texto de caché cuyo hash SHA-256 coincida exactamente.
- Si `estado` es `no_verificable`, `pasaje` debe ser `null` y `motivos` debe incluir explicaciones explícitas.

## Criterio de terminado
- Se ha contrastado el claim contra el texto primario recuperado y verificado.
- El pasaje literal respalda o refuta de manera inequívoca la afirmación auditada.
- El archivo de caché existe con la huella SHA-256 exacta y el resultado cumple el esquema.

## Prohibido
- Prohibido marcar `verificada` sin disponer del texto recuperado en caché ni del pasaje literal exacto.
- Prohibido parafrasear o alterar caracteres en el pasaje literal citado.
- Prohibido modificar directamente archivos en `kb/`.
- Prohibido emplear motores de búsqueda para sustituir la URL canónica del manifiesto sin registro explícito.
