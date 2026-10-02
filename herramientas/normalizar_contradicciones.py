#!/usr/bin/env python3
"""Normaliza kb/grafo/contradicciones.jsonl.

Cumple con la tarea F4.4 del Plan de Migración de Antigravity:
- Normaliza las 93 contradicciones del grafo.
- Guarda el valor anterior en resolution_original.
- Establece resolution en 'resuelta' o 'abierta'.
- Agrega regla_aplicada con el texto libre de resolución previa (o null).
- Separa claim_ids existentes de claim_ids_no_encontrados.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def raiz() -> Path:
    """Retorna la raíz del repositorio de forma portable."""
    return Path(__file__).resolve().parent.parent


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


def normalizar_contradicciones() -> list[dict]:
    """Normaliza todas las filas de kb/grafo/contradicciones.jsonl."""
    r = raiz()
    claims = cargar_claims_existentes(r)
    ruta = r / "kb" / "grafo" / "contradicciones.jsonl"

    filas_normalizadas = []
    with open(ruta, "r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            item = json.loads(line)

            # Conservar o leer resolution_original para idempotencia
            if "resolution_original" in item:
                orig = item["resolution_original"]
            else:
                orig = item.get("resolution")

            if orig == "abierta" or orig is None:
                new_res = "abierta"
                regla = None
            elif orig == "resuelta":
                new_res = "resuelta"
                regla = None
            else:
                new_res = "resuelta"
                regla = orig

            cids = item.get("claim_ids", [])
            # Recombinar con posibles cids no encontrados previos para idempotencia
            prev_no_encontrados = item.get("claim_ids_no_encontrados", [])
            todos_cids = list(dict.fromkeys(cids + prev_no_encontrados))

            found = [c for c in todos_cids if c in claims]
            not_found = [c for c in todos_cids if c not in claims]

            nuevo = dict(item)
            nuevo["resolution_original"] = orig
            nuevo["resolution"] = new_res
            nuevo["regla_aplicada"] = regla
            nuevo["claim_ids"] = found
            nuevo["claim_ids_no_encontrados"] = not_found

            filas_normalizadas.append(nuevo)

    return filas_normalizadas


def guardar(r: Path, filas: list[dict]) -> None:
    """Guarda las filas normalizadas en kb/grafo/contradicciones.jsonl."""
    ruta = r / "kb" / "grafo" / "contradicciones.jsonl"
    with open(ruta, "w", encoding="utf-8") as fh:
        for item in filas:
            fh.write(json.dumps(item, ensure_ascii=False) + "\n")


def main() -> None:
    r = raiz()
    filas = normalizar_contradicciones()
    guardar(r, filas)
    resueltas = sum(1 for x in filas if x["resolution"] == "resuelta")
    abiertas = sum(1 for x in filas if x["resolution"] == "abierta")
    print(f"OK: {len(filas)} contradicciones normalizadas (resueltas: {resueltas}, abiertas: {abiertas})")


if __name__ == "__main__":
    main()
