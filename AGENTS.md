# Reglas del Repositorio y Guía del Agente — BRIDGE

Repositorio central de la base de conocimiento canónica de **The Bridge Intelligence** (`thebridgeintelligence.ai`).
Consolida la investigación estratégica, empírica y legal sobre asuntos corporativos estructurada en 12 pilares temáticos.
Implementa un catálogo navegable de 864 preguntas atómicas y 1318 hallazgos verificables bajo compuertas estrictas de calidad.

---

## 🗺️ Mapa de Navegación por Niveles de Granularidad

La base de conocimiento opera bajo una arquitectura de divulgación progresiva en 5 niveles:

| Nivel | Componente | Presupuesto Aprox. | Propósito |
| :--- | :--- | :--- | :--- |
| **L0** | `AGENTS.md` y `kb/CATALOGO.json` | ~1.000 – 2.500 tokens | Índice maestro, totales globales, huella criptográfica de datos y metadatos. |
| **L1** | `TARJETA.md` en cada pilar | ~2.000 – 3.000 tokens | Visión de síntesis del pilar, alcance, reglas editoriales y top 10 vacíos. |
| **L2** | `EJE.md` en cada subcarpeta de eje | ~1.500 – 2.000 tokens | Resumen ejecutivo de las 8 preguntas del eje y estados de verificación. |
| **L3** | `<QID>.json` (ej. `P01-F01.json`) | ~3.000 – 8.000 tokens | Registro atómico estructurado en esquema canónico de 20 atributos. |
| **L4** | `fuentes.jsonl` y URL original | Variable / Documental | Evidencia documental primaria, pasajes auditados y trazabilidad externa. |

---

## ⚖️ Regla Canónica de Uso del Conocimiento

- **Hecho Documentado:** Una afirmación solo puede presentarse como un **hecho** si su `epistemic_status` es `hecho_documentado` **y** su `verificacion.estado` es exactamente `verificada`.
- **Hipótesis o Estado en Proceso:** Cualquier afirmación que no cumpla copulativamente ambas condiciones debe citarse estrictamente como **hipótesis** o hallazgo no verificado, explicitando su estado de verificación actual (`no_verificada`, `en_proceso`, `no_verificable` o `refutada`).

---

## ✍️ Protocolo de Escritura y Staging

- **Prohibición de Escritura Directa:** Ningún agente puede escribir ni modificar directamente archivos en la carpeta `kb/`.
- **Flujo de Staging:** Toda propuesta o resultado de ejecución debe depositarse exclusivamente en:
  `staging/<run_id>/<rol>/`
- **Integración Controlada:** Los artefactos depositados en staging son procesados e incorporados a la base canónica únicamente por el rol **integrador**, previa validación formal sin errores con `herramientas/validar.py`.

---

## 🛠️ Herramientas Canónicas del Repositorio

- **`herramientas/validar.py`**: Valida integridad referencial, conformidad de vocabularios, reglas epistémicas y estructura física (`python3 herramientas/validar.py`).
- **`herramientas/generar_vistas.py`**: Regenera de forma determinista y reproducible todos los derivados, catálogos, índices y vistas (`python3 herramientas/generar_vistas.py`).
- **`herramientas/normalizar.py`**: Aplica reglas de normalización anotativa e idempotente sobre el catálogo (`python3 herramientas/normalizar.py`).

---

## 🛡️ Reglas de Operación y Seguridad

- **Error Masking en Python:** En cualquier bloque `except`, usar siempre `type(err).__name__` en lugar de `str(err)`. Nunca exponer stack traces ni mensajes internos en salidas directas al usuario. Formato estándar:
  `logger.error(f"Error {context}: {type(err).__name__} (detalles omitidos por seguridad)")`
- **Credenciales y Secretos:** Jamás commitear claves de API, tokens privados ni archivos `.env`. Utilizar `.env.example` para documentar variables de entorno requeridas.
- **Trazabilidad y Rutas Relativas:** Al citar archivos o rutas en documentación Markdown, utilizar siempre enlaces relativos resolubles en el árbol de trabajo (ej. `kb/canon/mandato.md`), prohibiendo enlaces `file:///` absolutos.
- **Control de Versiones (Git):** Mantener la rama principal en estado funcional y realizar commits descriptivos y atómicos siguiendo la convención Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `migracion:`, etc.).

---

## 📝 Mantenimiento de Bitácora

- Toda sesión de trabajo o hito operativo debe registrarse en un archivo individual por sesión en:
  `gobernanza/bitacora/AAAA-MM-DD-NN-slug.md`
- Debe documentar el objetivo, cambios realizados, decisiones de diseño y pendientes.
