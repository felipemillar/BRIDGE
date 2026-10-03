#!/usr/bin/env python3
"""Generador del visualizador interactivo del grafo de conocimiento BRIDGE.

Lee kb/grafo/entidades.jsonl, kb/grafo/relaciones.jsonl y kb/grafo/contradicciones.jsonl
y genera visualizador_grafo.html con un explorador interactivo basado en vis-network.
"""
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("generar_grafo_html")

RAIZ = Path(__file__).resolve().parent.parent

COLORES_TIPO = {
    "persona_rol": {"background": "#8b5cf6", "border": "#6d28d9", "highlight": "#a78bfa"},
    "rol": {"background": "#8b5cf6", "border": "#6d28d9", "highlight": "#a78bfa"},
    "organizacion": {"background": "#3b82f6", "border": "#1d4ed8", "highlight": "#60a5fa"},
    "org": {"background": "#3b82f6", "border": "#1d4ed8", "highlight": "#60a5fa"},
    "riesgo": {"background": "#ef4444", "border": "#b91c1c", "highlight": "#f87171"},
    "tema": {"background": "#10b981", "border": "#047857", "highlight": "#34d399"},
    "documento": {"background": "#f59e0b", "border": "#b45309", "highlight": "#fbbf24"},
    "doc": {"background": "#f59e0b", "border": "#b45309", "highlight": "#fbbf24"},
    "compromiso": {"background": "#6366f1", "border": "#4338ca", "highlight": "#818cf8"},
    "comp": {"background": "#6366f1", "border": "#4338ca", "highlight": "#818cf8"},
    "producto": {"background": "#06b6d4", "border": "#0e7490", "highlight": "#22d3ee"},
    "prod": {"background": "#06b6d4", "border": "#0e7490", "highlight": "#22d3ee"},
    "experimento": {"background": "#ec4899", "border": "#be185d", "highlight": "#f472b6"},
    "exp": {"background": "#ec4899", "border": "#be185d", "highlight": "#f472b6"},
    "metrica": {"background": "#14b8a6", "border": "#0f766e", "highlight": "#2dd4bf"},
    "met": {"background": "#14b8a6", "border": "#0f766e", "highlight": "#2dd4bf"},
    "evento": {"background": "#f43f5e", "border": "#be123c", "highlight": "#fb7185"},
    "evt": {"background": "#f43f5e", "border": "#be123c", "highlight": "#fb7185"},
    "entidad": {"background": "#64748b", "border": "#334155", "highlight": "#94a3b8"}
}


def cargar_datos():
    entidades_path = RAIZ / "kb/grafo/entidades.jsonl"
    relaciones_path = RAIZ / "kb/grafo/relaciones.jsonl"
    contradicciones_path = RAIZ / "kb/grafo/contradicciones.jsonl"

    entidades = {}
    with open(entidades_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                entidades[item["entity_id"]] = item

    relaciones = []
    with open(relaciones_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                relaciones.append(json.loads(line))

    contradicciones = []
    with open(contradicciones_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                contradicciones.append(json.loads(line))

    return entidades, relaciones, contradicciones


def construir_html(entidades, relaciones, contradicciones):
    # Nodos conectados en relaciones
    nodos_conectados = set()
    for r in relaciones:
        nodos_conectados.add(r["subject_id"])
        nodos_conectados.add(r["object_id"])

    nodes_data = []
    for nid in sorted(nodos_conectados):
        ent = entidades.get(nid, {})
        tipo = ent.get("type", nid.split(":")[0] if ":" in nid else "entidad")
        color = COLORES_TIPO.get(tipo, COLORES_TIPO["entidad"])
        label = ent.get("canonical_name", nid)
        if len(label) > 28:
            label_disp = label[:26] + "…"
        else:
            label_disp = label

        tooltip = f"<b>{ent.get('canonical_name', nid)}</b><br>ID: {nid}<br>Tipo: <code>{tipo}</code>"
        if ent.get("aliases"):
            tooltip += f"<br>Aliases: {', '.join(ent['aliases'][:3])}"

        nodes_data.append({
            "id": nid,
            "label": label_disp,
            "title": tooltip,
            "group": tipo,
            "color": color,
            "font": {"color": "#f8fafc", "size": 13, "face": "Inter, system-ui, sans-serif"},
            "shape": "dot",
            "size": 18,
            "tipo": tipo,
            "canonical_name": ent.get("canonical_name", nid)
        })

    edges_data = []
    for i, r in enumerate(relaciones):
        evidencias = ", ".join(r.get("evidence_claim_ids", []))
        cuadernos = ", ".join(r.get("notebooks", []))
        tooltip = (
            f"<b>{r['predicate']}</b><br>"
            f"Origen: {r['subject_id']}<br>"
            f"Destino: {r['object_id']}<br>"
            f"Evidencias: {evidencias or 'N/A'}<br>"
            f"Cuadernos: {cuadernos or 'N/A'}"
        )
        edges_data.append({
            "id": f"e_{i}",
            "from": r["subject_id"],
            "to": r["object_id"],
            "label": r["predicate"],
            "title": tooltip,
            "arrows": "to",
            "font": {"size": 10, "align": "middle", "color": "#94a3b8", "strokeWidth": 0},
            "color": {"color": "#475569", "highlight": "#38bdf8", "hover": "#38bdf8"},
            "smooth": {"type": "curvedCW", "roundness": 0.15}
        })

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Bridge Intelligence — Grafo de Conocimiento Canónico</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/standalone/umd/vis-network.min.js"></script>
  <script>
    if (typeof vis === 'undefined') {{
      document.write('<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"><\\/script>');
    }}
  </script>
  <style>
    :root {{
      --bg: #090d16;
      --panel-bg: rgba(15, 23, 42, 0.88);
      --border: rgba(51, 65, 85, 0.65);
      --text: #f1f5f9;
      --muted: #94a3b8;
      --accent: #38bdf8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
    }}
    body {{
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 10;
      flex-shrink: 0;
      height: 56px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .brand h1 {{
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
    }}
    .badge {{
      font-size: 0.75rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}
    .stats {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--muted);
    }}
    .stats span strong {{
      color: #fff;
    }}
    #app {{
      display: flex;
      flex: 1;
      height: calc(100vh - 56px);
      min-height: 0;
      position: relative;
      overflow: hidden;
    }}
    #network {{
      flex: 1;
      height: 100%;
      min-height: 0;
      width: 100%;
      position: relative;
      background: radial-gradient(circle at center, #111827 0%, #090d16 100%);
    }}
    .sidebar {{
      width: 330px;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      border-left: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      padding: 16px;
      gap: 16px;
      z-index: 10;
      height: 100%;
      overflow-y: auto;
      flex-shrink: 0;
    }}
    .search-box input {{
      width: 100%;
      padding: 10px 14px;
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: #fff;
      font-size: 0.88rem;
      outline: none;
      transition: all 0.2s;
    }}
    .search-box input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }}
    .legend {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .legend-title {{
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--muted);
    }}
    .legend-items {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(30, 41, 59, 0.5);
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      cursor: pointer;
      border: 1px solid transparent;
      user-select: none;
      transition: background 0.15s, border-color 0.15s;
    }}
    .legend-item:hover, .legend-item.active {{
      border-color: var(--border);
      background: rgba(51, 65, 85, 0.7);
    }}
    .dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .detail-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      font-size: 0.82rem;
      line-height: 1.5;
    }}
    .detail-card h3 {{
      font-size: 0.95rem;
      color: var(--accent);
      margin-bottom: 6px;
      word-break: break-word;
    }}
    .detail-card code {{
      background: rgba(15, 23, 42, 0.7);
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 0.78rem;
      word-break: break-all;
    }}
    .controls {{
      margin-top: auto;
      display: flex;
      gap: 8px;
    }}
    .btn {{
      flex: 1;
      padding: 8px 12px;
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid var(--border);
      color: #fff;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
      font-weight: 500;
      transition: background 0.15s;
      text-align: center;
    }}
    .btn:hover {{
      background: rgba(51, 65, 85, 0.9);
      border-color: var(--accent);
    }}
  </style>
</head>
<body>
  <header>
    <div class="brand">
      <h1>BRIDGE — Grafo de Conocimiento</h1>
      <span class="badge">Canónico v1.0</span>
    </div>
    <div class="stats">
      <span>Nodos: <strong>{len(nodes_data)}</strong></span>
      <span>Relaciones: <strong>{len(edges_data)}</strong></span>
      <span>Predicados: <strong>18</strong></span>
    </div>
  </header>

  <div id="app">
    <div id="network"></div>

    <aside class="sidebar">
      <div class="search-box">
        <input type="text" id="searchInput" placeholder="Buscar entidad (ej. CCO, CMF, Reputación)...">
      </div>

      <div class="legend">
        <div class="legend-title">Tipos de Entidad</div>
        <div class="legend-items" id="legendContainer"></div>
      </div>

      <div class="detail-card" id="detailCard">
        <h3>Detalles de Selección</h3>
        <p style="color: var(--muted);">Haz clic en un nodo o relación para inspeccionar sus atributos, predicados y evidencias de respaldo.</p>
      </div>

      <div class="controls">
        <button class="btn" id="btnFit">Centrar Grafo</button>
        <button class="btn" id="btnPhysics">Pausar Física</button>
      </div>
    </aside>
  </div>

  <script>
    const rawNodes = {json.dumps(nodes_data, ensure_ascii=False)};
    const rawEdges = {json.dumps(edges_data, ensure_ascii=False)};
    const coloresTipo = {json.dumps(COLORES_TIPO, ensure_ascii=False)};

    const nodes = new vis.DataSet(rawNodes);
    const edges = new vis.DataSet(rawEdges);

    const container = document.getElementById('network');
    const data = {{ nodes: nodes, edges: edges }};
    const options = {{
      nodes: {{
        borderWidth: 2,
        shadow: {{ enabled: true, color: 'rgba(0,0,0,0.5)', size: 8 }}
      }},
      edges: {{
        width: 1.5,
        shadow: {{ enabled: false }},
        selectionWidth: 3
      }},
      physics: {{
        solver: 'forceAtlas2Based',
        forceAtlas2Based: {{
          gravitationalConstant: -40,
          centralGravity: 0.008,
          springLength: 95,
          springConstant: 0.08,
          damping: 0.4
        }},
        stabilization: {{ iterations: 120, updateInterval: 25 }}
      }},
      interaction: {{
        hover: true,
        tooltipDelay: 100,
        navigationButtons: true,
        keyboard: true
      }}
    }};

    const network = new vis.Network(container, data, options);
    window.network = network;

    // Ajustar vista tras renderizado inicial
    network.once('stabilizationIterationsDone', function() {{
      network.fit({{ animation: true }});
    }});
    window.addEventListener('resize', () => {{
      network.redraw();
      network.fit();
    }});

    // Poblar leyenda
    const legendContainer = document.getElementById('legendContainer');
    const tipos = [...new Set(rawNodes.map(n => n.tipo))].sort();
    tipos.forEach(tipo => {{
      const color = coloresTipo[tipo] || coloresTipo['entidad'];
      const item = document.createElement('div');
      item.className = 'legend-item';
      item.innerHTML = `<span class="dot" style="background:${{color.background}}"></span> ${{tipo}}`;
      item.onclick = () => {{
        const matchingIds = rawNodes.filter(n => n.tipo === tipo).map(n => n.id);
        network.selectNodes(matchingIds);
        detailCard.innerHTML = `
          <h3>Filtro: ${{tipo}}</h3>
          <p><strong>Entidades seleccionadas:</strong> ${{matchingIds.length}}</p>
          <ul style="padding-left:16px; margin-top:6px; font-size:0.75rem; color:var(--muted); max-height:160px; overflow-y:auto;">
            ${{matchingIds.map(id => `<li>${{id}}</li>`).join('')}}
          </ul>
        `;
      }};
      legendContainer.appendChild(item);
    }});

    // Detalle al hacer clic
    const detailCard = document.getElementById('detailCard');
    network.on('click', function(params) {{
      if (params.nodes.length > 0) {{
        const nid = params.nodes[0];
        const n = rawNodes.find(item => item.id === nid);
        const connectedEdges = rawEdges.filter(e => e.from === nid || e.to === nid);
        detailCard.innerHTML = `
          <h3>${{n.canonical_name}}</h3>
          <p><strong>ID:</strong> <code>${{n.id}}</code></p>
          <p><strong>Tipo:</strong> <span class="badge" style="background:${{n.color.background}}; color:#fff">${{n.tipo}}</span></p>
          <p style="margin-top:8px;"><strong>Relaciones conectadas (${{connectedEdges.length}}):</strong></p>
          <ul style="padding-left:16px; margin-top:4px; font-size:0.75rem; color:var(--muted)">
            ${{connectedEdges.map(e => `<li><strong>${{e.label}}</strong>: ${{e.from === nid ? e.to : e.from}}</li>`).join('')}}
          </ul>
        `;
      }} else if (params.edges.length > 0) {{
        const eid = params.edges[0];
        const e = rawEdges.find(item => item.id === eid);
        detailCard.innerHTML = `
          <h3>Relación: ${{e.label}}</h3>
          <p><strong>Sujeto:</strong> <code>${{e.from}}</code></p>
          <p><strong>Objeto:</strong> <code>${{e.to}}</code></p>
          <div style="margin-top:8px; font-size:0.75rem; color:var(--muted)">${{e.title}}</div>
        `;
      }}
    }});

    // Búsqueda
    document.getElementById('searchInput').addEventListener('input', function(e) {{
      const query = e.target.value.toLowerCase().trim();
      if (!query) {{
        network.unselectAll();
        return;
      }}
      const match = rawNodes.find(n => n.canonical_name.toLowerCase().includes(query) || n.id.toLowerCase().includes(query));
      if (match) {{
        network.selectNodes([match.id]);
        network.focus(match.id, {{ scale: 1.2, animation: true }});
      }}
    }});

    // Controles
    document.getElementById('btnFit').onclick = () => network.fit({{ animation: true }});
    let physicsActive = true;
    document.getElementById('btnPhysics').onclick = (e) => {{
      physicsActive = !physicsActive;
      network.setOptions({{ physics: {{ enabled: physicsActive }} }});
      e.target.innerText = physicsActive ? 'Pausar Física' : 'Activar Física';
    }};
  </script>
</body>
</html>
"""
    return html_template


def main():
    try:
        entidades, relaciones, contradicciones = cargar_datos()
        html = construir_html(entidades, relaciones, contradicciones)
        out_path = RAIZ / "visualizador_grafo.html"
        out_path.write_text(html, encoding="utf-8")
        index_path = RAIZ / "index.html"
        index_path.write_text(html, encoding="utf-8")
        logger.info(f"Visualizador generado exitosamente en: {out_path} e {index_path}")
        print(f"OK: Visualizador generado en {out_path.name} e {index_path.name}")
    except Exception as err:
        logger.error(f"Error al generar visualizador: {type(err).__name__} (detalles omitidos por seguridad)")
        raise


if __name__ == "__main__":
    main()
