# Protocolo de Verificación Epistémica y Promoción de Evidencia

Este protocolo define las reglas, métodos y estándares de rigor necesarios para auditar afirmaciones (`claims`) y promoverlas a hechos documentados verificados dentro de **The Bridge Intelligence**.

---

## 1. La Regla Canónica de Distinción Epistémica

Una aseveración solo puede ser presentada, comunicada o citada como un **hecho** si y solo si cumple copulativamente dos condiciones:
1. Su atributo `epistemic_status` es exactamente `hecho_documentado`.
2. Su atributo `verificacion.estado` es exactamente `verificada`.

Cualquier afirmación que no cumpla ambas condiciones de manera simultánea debe ser tratada y citada estrictamente como una **hipótesis** o hallazgo no verificado, explicitando su estado de verificación actual (`no_verificada`, `cita_sintetica`, `solo_sintesis_interna`, `refutada` o `no_verificable`).

---

## 2. Estados de Verificación Canónicos

El vocabulario cerrado de `verificacion.estado` consta de los siguientes estados:

| Estado | Significado Epistémico | Requisitos para Promoción |
| :--- | :--- | :--- |
| `no_verificada` | Hallazgo original del corpus pendiente de contraste documental. | Estado basal por defecto. |
| `verificada` | Hallazgo contrastado exitosamente contra el documento primario original. | URL consultada válida, texto descargado en caché con SHA-256 coincidente, pasaje literal idéntico (0 < len ≤ 600 caracteres) y concordancia sustantiva. |
| `refutada` | Hallazgo contradicho objetivamente por la evidencia primaria. | Pasaje literal que desmiente la afirmación, texto en caché y motivos documentados. |
| `no_verificable` | Imposibilidad técnica o material de verificar el claim (URL caída, paywall estricto, recurso inexistente). | `pasaje` fijado en `null`, y lista explícita de `motivos` técnicos. |

---

## 3. Protocolo de Ejecución de Verificación

Para cada afirmación a verificar, el **verificador de evidencia** debe seguir el siguiente procedimiento algorítmico:

1. **Localización de Fuente Primaria:**
   - Extraer el `source_id` de la evidencia del claim.
   - Consultar el manifiesto de fuentes (`fuentes.jsonl`) del pilar correspondiente.
   - Extraer la `original_url` sustantiva.

2. **Descarga y Caché Criptográfica:**
   - Recuperar el texto íntegro de la URL o documento primario.
   - Calcular su huella SHA-256 (`<sha256>`).
   - Almacenar el texto plano exacto en `staging/<run_id>/cache/<sha256>.txt`.

3. **Extracción del Pasaje Literal:**
   - Localizar en el texto de caché el fragmento exacto que sustenta o refuta la afirmación.
   - Extraer dicho pasaje literal con longitud entre 1 y 600 caracteres.
   - Verificar computacionalmente que `norm(pasaje) in norm(cache.read_text())`.

4. **Estructuración del Registro de Verificación:**
   - Asignar la estructura en el objeto `verificacion`:
     ```json
     {
       "estado": "verificada",
       "fecha": "AAAA-MM-DDTHH:MM:SSZ",
       "verificado_por": {
         "rol": "verificador_evidencia",
         "modelo": "<modelo_utilizado>",
         "run_id": "<run_id>"
       },
       "metodo": "lectura_url_original",
       "url_consultada": "<url_primaria>",
       "sha256_texto": "<sha256_del_archivo_en_cache>",
       "pasaje": "<pasaje_literal_exacto>",
       "motivos": null
     }
     ```

5. **Casos Negativos o Excepcionales:**
   - Si la URL no es accesible tras reintentos, o el contenido fue retirado:
     - `estado`: `"no_verificable"`
     - `pasaje`: `null`
     - `motivos`: `["error_conexion_404", "documento_no_disponible"]`

---

## 4. Prohibiciones Críticas

- Prohibido inventar, truncar erróneamente o alterar palabras dentro del pasaje literal.
- Prohibido citar una URL genérica (ej. home page de un ministerio) si el hallazgo requiere un decreto específico.
- Prohibido promover a `verificada` afirmaciones cuya evidencia primaria proceda exclusivamente de síntesis internas (`solo_sintesis_interna`) sin auditar la fuente original citada por dicha síntesis.
