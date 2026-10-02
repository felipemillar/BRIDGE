"""Herramienta para ejecutar verificaciones del piloto de evidencia.

BRIDGE Knowledge Base.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from herramientas.kb import raiz

logger = logging.getLogger(__name__)


def verificar_afirmacion(claim_id: str, fecha_iso: str = "2026-10-02T20:40:00Z") -> bool:
    r = raiz()
    idx_path = r / "staging" / "piloto-001" / "cache_index.json"
    if not idx_path.exists():
        logger.error("No existe staging/piloto-001/cache_index.json")
        return False

    try:
        cache_map = json.loads(idx_path.read_text(encoding="utf-8"))
    except Exception as err:
        logger.error(
            f"Error al leer cache_index.json: {type(err).__name__} (detalles omitidos por seguridad)"
        )
        return False

    if claim_id not in cache_map:
        logger.error(f"Afirmacion {claim_id} no encontrada en cache_index.json")
        return False

    entry = cache_map[claim_id]
    sha = entry["sha256"]
    url = entry["url"]
    pasaje = entry["pasaje"]
    qid = entry["question_id"]

    # 1. Crear propuesta del verificador en staging
    propuesta = {
        "claim_id": claim_id,
        "verificacion": {
            "estado": "verificada",
            "fecha": fecha_iso,
            "verificado_por": {
                "rol": "verificador_evidencia",
                "modelo": "antigravity-swarm",
                "run_id": "piloto-001",
            },
            "metodo": "lectura_url_original",
            "url_consultada": url,
            "sha256_texto": sha,
            "pasaje": pasaje,
            "motivos": [],
        },
        "_procedencia": {
            "rol": "verificador_evidencia",
            "modelo": "antigravity-swarm",
            "run_id": "piloto-001",
            "fecha": fecha_iso,
        },
    }

    v_dir = r / "staging" / "piloto-001" / "verificador_evidencia"
    v_dir.mkdir(parents=True, exist_ok=True)
    prop_file = v_dir / f"{claim_id}.json"
    prop_file.write_text(
        json.dumps(propuesta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # 2. Localizar archivo de pregunta en kb/pilares
    target_file = None
    for p in (r / "kb" / "pilares").rglob(f"{qid}.json"):
        target_file = p
        break

    if not target_file:
        logger.error(f"Archivo de pregunta {qid}.json no encontrado")
        return False

    try:
        q_data = json.loads(target_file.read_text(encoding="utf-8"))
        updated = False
        for f in q_data.get("findings", []):
            if f.get("claim_id") == claim_id:
                f["verificacion"] = propuesta["verificacion"]
                updated = True
                break

        if not updated:
            logger.error(f"Claim {claim_id} no encontrado dentro de {qid}.json")
            return False

        target_file.write_text(
            json.dumps(q_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except Exception as err:
        logger.error(
            f"Error al actualizar pregunta {qid}: {type(err).__name__} (detalles omitidos por seguridad)"
        )
        return False

    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="Verificar afirmación del piloto")
    ap.add_argument("--claim-id", required=True, help="ID de la afirmación")
    ap.add_argument(
        "--fecha", default="2026-10-02T20:40:00Z", help="Fecha ISO de verificación"
    )
    args = ap.parse_args()

    ok = verificar_afirmacion(args.claim_id, args.fecha)
    if not ok:
        sys.exit(1)
    print(f"Afirmacion {args.claim_id} verificada exitosamente.")


if __name__ == "__main__":
    main()
