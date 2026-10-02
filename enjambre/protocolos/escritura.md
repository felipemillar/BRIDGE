# Protocolo de Escritura, Staging e Integración

Este protocolo establece el flujo unificado y obligatorio para cualquier modificación, incorporación o actualización en la base de conocimiento canónica de **The Bridge Intelligence**.

---

## 1. Prohibición Absoluta de Escritura Directa en `kb/`

Ningún agente del enjambre (a excepción exclusiva del rol **integrador**) tiene permitido crear, modificar o eliminar archivos directamente en el directorio `kb/` ni en sus subdirectorios. Cualquier intento de escritura directa constituye una violación crítica de gobernanza y será rechazado por los controles de auditoría.

---

## 2. El Ciclo de Staging

Toda propuesta de cambio debe canalizarse a través del directorio `staging/`, siguiendo la estructura jerárquica:

```text
staging/
└── <run_id>/
    ├── cache/
    │   └── <sha256>.txt                  # Textos primarios descargados
    ├── <rol_productor>/
    │   └── <artefacto>.json              # Propuesta estructurada
    ├── auditor/
    │   └── dictamen.json                 # Dictamen independiente de aprobación o rechazo
    └── integrador/
        └── resultado.json                # Informe final de fusión y validación
```

### Requisitos del Artefacto en Staging:
1. **Unidad Atómica:** Un archivo por unidad de trabajo (pregunta, afirmación, entidad o dictamen).
2. **Conformidad de Esquema:** Debe validar estrictamente contra su JSON Schema en `enjambre/contratos/<rol>.schema.json`.
3. **Bloque de Procedencia Obligatorio:** Todo archivo JSON debe incluir:
   ```json
   "_procedencia": {
     "rol": "<nombre_rol>",
     "modelo": "<identificador_modelo>",
     "run_id": "<identificador_ejecucion>",
     "fecha": "AAAA-MM-DDTHH:MM:SSZ"
   }
   ```

---

## 3. Compuertas de Calidad para la Integración

Para que un lote en staging sea promovido a la base canónica, debe atravesar secuencialmente cuatro compuertas:

1. **Compuerta de Validación Automática:**
   - La propuesta se somete a `herramientas/validar.py`.
   - Se comprueba sintaxis JSON, adhesión a vocabularios canónicos, ausencia de relaciones huérfanas y reglas epistémicas.

2. **Compuerta de Auditoría Independiente:**
   - Un agente con rol **auditor** (preferentemente utilizando una instancia o modelo distinto al productor) examina el lote.
   - En verificaciones de evidencia, el auditor debe inspeccionar el **contenido sustantivo** del pasaje contra el archivo de caché en `staging/<run_id>/cache/<sha256>.txt`.
   - El auditor emite su veredicto en `staging/<run_id>/auditor/dictamen.json`.

3. **Compuerta de Integración y Regeneración:**
   - El rol **integrador** toma los artefactos con dictamen `aprobado` y los aplica en `kb/`.
   - Ejecuta `python3 herramientas/generar_vistas.py` para regenerar de forma determinista `CATALOGO.json`, `TARJETA.md`, `EJE.md`, `afirmaciones.jsonl`, `chunks.jsonl`, `vacios.jsonl` y `README.md`.
   - Ejecuta `python3 herramientas/validar.py` para confirmar que el repositorio completo mantiene cero fallas.

4. **Compuerta de Registro y Trazabilidad:**
   - El integrador genera un commit atómico en Git con la convención Conventional Commits.
   - Registra una entrada formal de bitácora en `gobernanza/bitacora/AAAA-MM-DD-NN-<slug>.md`.

---

## 4. Regla de Idempotencia de Vistas

Las vistas derivadas e índices nunca se editan manualmente. Si se detecta un error en una vista generada (p. ej. `EJE.md` o `README.md`), el error radica exclusivamente en el dato atómico de origen (Nivel L3) o en el script de generación (`herramientas/generar_vistas.py`).
