## [2026-10-02] - Sesión de Trabajo: Despliegue Público del Grafo en Vercel
**Objetivo:** Publicar el visualizador interactivo del grafo de conocimiento en Vercel con acceso público irrestricto mediante link.

### ✅ Cambios Realizados:
- **Configuración de hosting estático:** Creación de [`index.html`](../../index.html), [`vercel.json`](../../vercel.json) y [`.vercelignore`](../../.vercelignore) para desplegar el visualizador estático como SPA liviano.
- **Creación de proyecto en Vercel:** Registro del proyecto `bridge-knowledge-graph` en el equipo activo `qrt-s-projects`.
- **Despliegue a Producción:** Despliegue exitoso en producción mediante `vercel deploy --prod`.
- **Apertura de Acceso Público:** Desactivación de la protección SSO (`vercel project protection disable bridge-knowledge-graph --sso`) para permitir el acceso público a cualquier persona con el enlace sin requerir login.
- **Verificación end-to-end:** Validación exitosa mediante navegador headless comprobando la carga de los 102 nodos, 76 relaciones y el panel de interacción.

### 🌐 URLs Canónicas del Despliegue:
- **Producción:** `https://bridge-knowledge-graph.vercel.app`
- **Ruta alternativa:** `https://bridge-knowledge-graph.vercel.app/grafo`
