"""Biblioteca común de lectura y escritura para la base de conocimiento BRIDGE.

Soporta transparentemente el layout heredado (respuestas/*.jsonl, fuentes/*.json)
y el layout nuevo (kb/pilares/<pilar>/ejes/<eje>/<qid>.json, fuentes.jsonl).
"""
import glob
import json
import logging
import os
import re
import unicodedata
from pathlib import Path

logger = logging.getLogger("kb")

PILARES = ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10", "P11", "T01"]


def raiz() -> Path:
    """Retorna la raíz del repositorio resuelta desde la ubicación de este archivo."""
    return Path(__file__).resolve().parent.parent


def slug(texto: str) -> str:
    """Genera un slug normalizado ASCII seguro para nombres de directorio y archivo."""
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].rstrip("-")


def layout_nuevo() -> bool:
    """Indica si el repositorio ya ha migrado al layout nuevo en kb/pilares/."""
    return (raiz() / "kb" / "pilares").exists()


def ruta_mandato() -> Path | None:
    """Ubica el archivo canónico del mandato en kb/canon/ o en docs_mandato/."""
    r = raiz()
    for p in ("kb/canon/mandato.md", "docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md"):
        cand = r / p
        if cand.exists():
            return cand
    return None


def parse_banco(texto: str):
    """Parsea el mandato y retorna (banco, titulos).

    banco: dict con clave QID -> {pilar, eje, subeje, eje_n, eje_dir, tipo, question_text}
    titulos: dict con clave pilar -> título oficial del pilar
    """
    banco = {}
    titulos = {}
    pilar = None
    eje = None
    subeje = None
    orden = {}

    for line in texto.splitlines():
        m = re.match(r"^### ((?:P\d\d|T01)) — (.+)$", line)
        if m:
            pilar, eje, subeje = m.group(1), None, None
            titulos[pilar] = m.group(2).strip()
            orden[pilar] = []
            continue
        m = re.match(r"^\*\*Eje: (.+)\*\*$", line)
        if m:
            eje, subeje = m.group(1).strip(), None
            continue
        if line.startswith("**Profundización"):
            eje = "Profundización especializada"
            continue
        m = re.match(r"^\*([^*].+)\*$", line)
        if m and pilar:
            subeje = m.group(1).strip()
            continue
        m = re.match(r"^- \*\*((?:P\d\d|T01)-([FCX])\d\d)\.\*\* (.+)$", line)
        if m:
            grupo = subeje or eje
            if grupo not in orden[pilar]:
                orden[pilar].append(grupo)
            idx = orden[pilar].index(grupo) + 1
            banco[m.group(1)] = {
                "pilar": pilar,
                "eje": eje,
                "subeje": subeje,
                "eje_n": idx,
                "eje_dir": f"{idx:02d}-{slug(grupo)}",
                "tipo": m.group(2),
                "question_text": m.group(3).strip(),
            }
    return banco, titulos


def cargar_banco():
    """Carga y parsea el banco de preguntas canónico."""
    p = ruta_mandato()
    if not p or not p.exists():
        raise FileNotFoundError("Mandato canónico no encontrado")
    try:
        texto = p.read_text(encoding="utf-8")
        return parse_banco(texto)
    except Exception as err:
        logger.error(f"Error al cargar banco: {type(err).__name__} (detalles omitidos por seguridad)")
        raise


def cargar_respuestas() -> list[dict]:
    """Carga los 864 registros ordenados por question_id según el layout activo."""
    r = raiz()
    rows = []
    try:
        if layout_nuevo():
            pattern = str(r / "kb/pilares/*/ejes/*/*.json")
            for f in glob.glob(pattern):
                base = os.path.basename(f)
                if re.match(r"^(P\d\d|T01)-[FCX]\d\d\.json$", base):
                    with open(f, "r", encoding="utf-8") as fh:
                        data = json.load(fh)
                    data["__ruta"] = os.path.relpath(f, r)
                    rows.append(data)
        else:
            for p in PILARES:
                path = r / "respuestas" / f"{p}.jsonl"
                if path.exists():
                    with open(path, "r", encoding="utf-8") as fh:
                        for line in fh:
                            line_str = line.strip()
                            if line_str:
                                rows.append(json.loads(line_str))
    except Exception as err:
        logger.error(f"Error al cargar respuestas: {type(err).__name__} (detalles omitidos por seguridad)")
        raise
    return sorted(rows, key=lambda item: item["question_id"])


def guardar_respuestas(respuestas: list[dict]) -> None:
    """Guarda las respuestas según el layout activo."""
    r = raiz()
    try:
        if layout_nuevo():
            for row in respuestas:
                ruta_rel = row.get("__ruta")
                if not ruta_rel:
                    continue
                dest = r / ruta_rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                clean_row = {k: v for k, v in row.items() if k != "__ruta"}
                with open(dest, "w", encoding="utf-8") as fh:
                    json.dump(clean_row, fh, indent=2, ensure_ascii=False)
                    fh.write("\n")
        else:
            por_pilar = {p: [] for p in PILARES}
            for row in respuestas:
                p = row["question_id"][:3]
                if p in por_pilar:
                    por_pilar[p].append(row)
            for p, rows in por_pilar.items():
                dest = r / "respuestas" / f"{p}.jsonl"
                dest.parent.mkdir(parents=True, exist_ok=True)
                with open(dest, "w", encoding="utf-8") as fh:
                    for row in rows:
                        clean_row = {k: v for k, v in row.items() if k != "__ruta"}
                        fh.write(json.dumps(clean_row, ensure_ascii=False) + "\n")
    except Exception as err:
        logger.error(f"Error al guardar respuestas: {type(err).__name__} (detalles omitidos por seguridad)")
        raise


def cargar_manifiestos() -> dict[str, dict]:
    """Retorna {pilar: {'meta': dict, 'sources': list[dict]}} según el layout activo."""
    r = raiz()
    out = {}
    try:
        if layout_nuevo():
            for d in sorted(glob.glob(str(r / "kb/pilares/*"))):
                if not os.path.isdir(d):
                    continue
                p = os.path.basename(d)[:3]
                meta_p = Path(d) / "pilar.json"
                src_p = Path(d) / "fuentes.jsonl"
                if meta_p.exists() and src_p.exists():
                    with open(meta_p, "r", encoding="utf-8") as fh:
                        meta = json.load(fh)
                    sources = []
                    with open(src_p, "r", encoding="utf-8") as fh:
                        for line in fh:
                            line_str = line.strip()
                            if line_str:
                                sources.append(json.loads(line_str))
                    out[p] = {"meta": meta, "sources": sources}
        else:
            for p in PILARES:
                path = r / "fuentes" / f"{p}.json"
                if path.exists():
                    with open(path, "r", encoding="utf-8") as fh:
                        m = json.load(fh)
                    meta = {k: v for k, v in m.items() if k != "sources"}
                    sources = m.get("sources", [])
                    out[p] = {"meta": meta, "sources": sources}
    except Exception as err:
        logger.error(f"Error al cargar manifiestos: {type(err).__name__} (detalles omitidos por seguridad)")
        raise
    return out


def guardar_manifiestos(manifiestos: dict[str, dict]) -> None:
    """Guarda los manifiestos según el layout activo."""
    r = raiz()
    try:
        if layout_nuevo():
            dirs_map = {}
            for d in glob.glob(str(r / "kb/pilares/*")):
                if os.path.isdir(d):
                    dirs_map[os.path.basename(d)[:3]] = Path(d)
            for p, data in manifiestos.items():
                pdir = dirs_map.get(p)
                if not pdir:
                    continue
                meta_p = pdir / "pilar.json"
                src_p = pdir / "fuentes.jsonl"
                with open(meta_p, "w", encoding="utf-8") as fh:
                    json.dump(data["meta"], fh, indent=2, ensure_ascii=False)
                    fh.write("\n")
                with open(src_p, "w", encoding="utf-8") as fh:
                    for src in data["sources"]:
                        fh.write(json.dumps(src, ensure_ascii=False) + "\n")
        else:
            for p, data in manifiestos.items():
                dest = r / "fuentes" / f"{p}.json"
                dest.parent.mkdir(parents=True, exist_ok=True)
                full = dict(data["meta"])
                full["sources"] = data["sources"]
                with open(dest, "w", encoding="utf-8") as fh:
                    json.dump(full, fh, indent=2, ensure_ascii=False)
                    fh.write("\n")
    except Exception as err:
        logger.error(f"Error al guardar manifiestos: {type(err).__name__} (detalles omitidos por seguridad)")
        raise
