#!/usr/bin/env python3
"""Reconstruye kb/grafo/relaciones.jsonl y kb/grafo/relaciones_descartadas.jsonl.

Cumple con la tarea F4.3 del Plan de Migración de Antigravity:
- Proyecta las 477 relaciones heredadas de pre-migracion:relaciones.jsonl (índices 0..476).
- Mapea subject_id y object_id a los nuevos entity_id canónicos usando kb/grafo/mapa_ids.jsonl.
- Proyecta los predicados sobre el vocabulario cerrado canónico usando herramientas/mapeos/predicados.json.
- Mantiene solo evidence_claim_ids existentes en el banco canónico.
- Envía las relaciones con entidades eliminadas o sin equivalente a relaciones_descartadas.jsonl con motivo.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
import subprocess
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def raiz() -> Path:
    """Retorna la raíz del repositorio de forma portable."""
    return Path(__file__).resolve().parent.parent


def cargar_mapa_ids(r: Path) -> dict[str, dict]:
    """Carga kb/grafo/mapa_ids.jsonl indexado por id_legado."""
    ruta = r / "kb" / "grafo" / "mapa_ids.jsonl"
    mapa = {}
    with open(ruta, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                item = json.loads(line)
                mapa[item["id_legado"]] = item
    return mapa


def cargar_entidades(r: Path) -> dict[str, dict]:
    """Carga kb/grafo/entidades.jsonl indexado por entity_id."""
    ruta = r / "kb" / "grafo" / "entidades.jsonl"
    entidades = {}
    with open(ruta, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                item = json.loads(line)
                entidades[item["entity_id"]] = item
    return entidades


def cargar_predicados_vocabulario(r: Path) -> set[str]:
    """Carga el vocabulario canónico de predicados de kb/esquemas/vocabularios.json."""
    ruta = r / "kb" / "esquemas" / "vocabularios.json"
    data = json.loads(ruta.read_text(encoding="utf-8"))
    return set(data.get("predicado", []))


def cargar_mapa_predicados(r: Path) -> dict[str, str]:
    """Carga la proyección de predicados heredados desde herramientas/mapeos/predicados.json."""
    ruta = r / "herramientas" / "mapeos" / "predicados.json"
    return json.loads(ruta.read_text(encoding="utf-8"))


def cargar_claims_existentes(r: Path) -> set[str]:
    """Extrae todos los claim_id válidos de los hallazgos en kb/pilares/."""
    claims = set()
    pilares_dir = r / "kb" / "pilares"
    for p in pilares_dir.rglob("*.json"):
        if p.name == "pilar.json":
            continue
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
            for finding in doc.get("findings", []):
                cid = finding.get("claim_id")
                if cid:
                    claims.add(cid)
        except Exception as err:
            logger.error("Error al leer hallazgos: %s (detalles omitidos por seguridad)", type(err).__name__)
    return claims


def cargar_relaciones_legado(r: Path) -> list[dict]:
    """Recupera las 477 relaciones heredadas directamente de la línea base pre-migración."""
    try:
        raw = subprocess.check_output(
            ["git", "show", "pre-migracion:relaciones.jsonl"],
            cwd=r,
        ).decode("utf-8")
        return [json.loads(line) for line in raw.splitlines() if line.strip()]
    except Exception as err:
        logger.error("Error al obtener relaciones heredadas: %s (detalles omitidos por seguridad)", type(err).__name__)
        sys.exit(1)


def reconstruir() -> tuple[list[dict], list[dict]]:
    """Procesa y clasifica las 477 relaciones en canónicas y descartadas."""
    r = raiz()
    mapa_ids = cargar_mapa_ids(r)
    entidades = cargar_entidades(r)
    pred_vocab = cargar_predicados_vocabulario(r)
    pred_map = cargar_mapa_predicados(r)
    claims_existentes = cargar_claims_existentes(r)
    relaciones_legado = cargar_relaciones_legado(r)

    relaciones_canonicas = []
    relaciones_descartadas = []

    for indice, rel in enumerate(relaciones_legado):
        s_leg = rel.get("subject_id")
        o_leg = rel.get("object_id")
        p_leg = rel.get("predicate")
        cids = rel.get("evidence_claim_ids", [])

        s_entry = mapa_ids.get(s_leg)
        o_entry = mapa_ids.get(o_leg)

        # 1. Validación de sujeto
        if not s_entry or s_entry.get("accion") == "eliminado":
            relaciones_descartadas.append({
                "indice_legado": indice,
                "subject_id_legado": s_leg,
                "predicate_legado": p_leg,
                "object_id_legado": o_leg,
                "motivo": f"sujeto_eliminado: {s_leg}",
            })
            continue

        # 2. Validación de objeto
        if not o_entry or o_entry.get("accion") == "eliminado":
            relaciones_descartadas.append({
                "indice_legado": indice,
                "subject_id_legado": s_leg,
                "predicate_legado": p_leg,
                "object_id_legado": o_leg,
                "motivo": f"objeto_eliminado: {o_leg}",
            })
            continue

        new_sub = s_entry.get("id_nuevo")
        new_obj = o_entry.get("id_nuevo")

        if new_sub not in entidades:
            relaciones_descartadas.append({
                "indice_legado": indice,
                "subject_id_legado": s_leg,
                "predicate_legado": p_leg,
                "object_id_legado": o_leg,
                "motivo": f"sujeto_no_encontrado_en_entidades: {new_sub}",
            })
            continue

        if new_obj not in entidades:
            relaciones_descartadas.append({
                "indice_legado": indice,
                "subject_id_legado": s_leg,
                "predicate_legado": p_leg,
                "object_id_legado": o_leg,
                "motivo": f"objeto_no_encontrado_en_entidades: {new_obj}",
            })
            continue

        if new_sub == new_obj:
            relaciones_descartadas.append({
                "indice_legado": indice,
                "subject_id_legado": s_leg,
                "predicate_legado": p_leg,
                "object_id_legado": o_leg,
                "motivo": "sujeto_y_objeto_fusionados_en_misma_entidad",
            })
            continue

        # 3. Validación de predicado
        new_pred = pred_map.get(p_leg)
        if not new_pred or new_pred not in pred_vocab:
            relaciones_descartadas.append({
                "indice_legado": indice,
                "subject_id_legado": s_leg,
                "predicate_legado": p_leg,
                "object_id_legado": o_leg,
                "motivo": f"predicado_sin_equivalente: {p_leg}",
            })
            continue

        # 4. Filtrado de claims válidos
        valid_cids = [c for c in cids if c in claims_existentes]

        rel_obj = {
            "indice_legado": indice,
            "subject_id": new_sub,
            "predicate": new_pred,
            "object_id": new_obj,
            "evidence_claim_ids": valid_cids,
        }
        if "valid_from" in rel:
            rel_obj["valid_from"] = rel["valid_from"]
        if "valid_to" in rel:
            rel_obj["valid_to"] = rel["valid_to"]
        if "notebooks" in rel:
            rel_obj["notebooks"] = rel["notebooks"]
        if "occurrence_count" in rel:
            rel_obj["occurrence_count"] = rel["occurrence_count"]

        relaciones_canonicas.append(rel_obj)

    return relaciones_canonicas, relaciones_descartadas


def guardar_resultados(r: Path, canonicas: list[dict], descartadas: list[dict]) -> None:
    """Escribe los archivos JSONL en kb/grafo/."""
    ruta_canon = r / "kb" / "grafo" / "relaciones.jsonl"
    ruta_desc = r / "kb" / "grafo" / "relaciones_descartadas.jsonl"

    with open(ruta_canon, "w", encoding="utf-8") as fh:
        for item in canonicas:
            fh.write(json.dumps(item, ensure_ascii=False) + "\n")

    with open(ruta_desc, "w", encoding="utf-8") as fh:
        for item in descartadas:
            fh.write(json.dumps(item, ensure_ascii=False) + "\n")


def main() -> None:
    r = raiz()
    canonicas, descartadas = reconstruir()
    guardar_resultados(r, canonicas, descartadas)
    print(f"OK: Relaciones reconstruidas. Canónicas: {len(canonicas)}, Descartadas: {len(descartadas)}, Total: {len(canonicas) + len(descartadas)}")


if __name__ == "__main__":
    main()
