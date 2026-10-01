# Reglas Locales del Agente - Proyecto BRIDGE

Bienvenido al espacio de trabajo **BRIDGE**. Este archivo define los lineamientos de comportamiento, estándares y flujo operativo persistente para los agentes que colaboren en este repositorio.

---

## 🎯 1. Alcance y Contexto del Proyecto
- **Propósito**: Espacio de desarrollo del proyecto BRIDGE.
- **Respaldo y Versionado**: Todo desarrollo realizado en este repositorio debe mantenerse versionado de forma limpia y sincronizado con GitHub.

---

## 🛡️ 2. Reglas de Operación y Seguridad
- **Error Masking en Python**:
  - En cualquier bloque `except`, usar siempre `type(err).__name__` en lugar de `str(err)`.
  - Nunca exponer stack traces ni mensajes internos en salidas directas a usuario.
  - Formato estándar de logging: `logger.error(f"Error {context}: {type(err).__name__} (detalles omitidos por seguridad)")`.
- **Credenciales y Secretos**:
  - Jamás commitear claves de API, tokens privados ni archivos `.env`.
  - Utilizar `.env.example` para documentar variables de entorno requeridas.
- **Trazabilidad de Archivos**:
  - Al citar archivos o rutas, utilizar siempre enlaces en formato markdown con esquema `file://` (ej. `[archivo](file:///ruta/al/archivo)`).

---

## 📝 3. Mantenimiento Obligatorio de Bitácora (`BITACORA.md`)
- Al finalizar cada sesión de trabajo o tras completar un hito lógico importante, el agente **DEBE** registrar los cambios en `BITACORA.md` ubicado en la raíz del proyecto.
- La entrada debe añadirse en orden cronológico inverso (la más reciente arriba) siguiendo la estructura oficial de `project-workflow-manager`:
  - `## [AAAA-MM-DD] - Sesión de Trabajo: [Nombre]`
  - `**Objetivo:** ...`
  - `### ✅ Cambios Realizados:`
  - `### 🧠 Decisiones y Notas de Diseño:`
  - `### ⏳ Pendientes y Siguientes Pasos:`

---

## 🚀 4. Flujo de Control de Versiones (Git / GitHub)
- Mantener la rama `main` en estado funcional.
- Realizar commits descriptivos y atómicos usando la convención Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, etc.).
- Verificar siempre `git status` y evitar subir archivos temporales, logs o artefactos generados no deseados.
