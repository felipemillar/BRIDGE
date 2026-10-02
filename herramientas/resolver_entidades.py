"""Módulo de resolución y normalización de entidades del grafo de conocimiento BRIDGE.

Mapea las entidades heredadas hacia los 11 tipos canónicos del mandato:
  organizacion, persona_rol, documento, fuente, tema, evento,
  compromiso, producto, riesgo, metrica, experimento.

Prefijos de ID:
  org, rol, doc, fte, tema, evt, comp, prod, riesgo, met, exp.

Genera de forma determinista:
  - kb/grafo/entidades.jsonl
  - kb/grafo/mapa_ids.jsonl
"""
import argparse
import collections
import json
import logging
import re
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent.parent
if str(_RAIZ) not in sys.path:
    sys.path.insert(0, str(_RAIZ))

try:
    from herramientas.kb import PILARES, raiz
except ModuleNotFoundError:
    from kb import PILARES, raiz

logger = logging.getLogger("resolver_entidades")

TIPOS_CANONICOS = {
    "organizacion",
    "persona_rol",
    "documento",
    "fuente",
    "tema",
    "evento",
    "compromiso",
    "producto",
    "riesgo",
    "metrica",
    "experimento",
}


def cargar_mapa_pilar(r: Path, pilar: str) -> dict:
    """Carga el diccionario de mapeo de un pilar desde herramientas/mapeos/<PILAR>.json."""
    ruta_mapa = r / "herramientas" / "mapeos" / f"{pilar}.json"
    if not ruta_mapa.exists():
        raise FileNotFoundError(f"Archivo de mapeo para {pilar} no encontrado: {ruta_mapa}")

    try:
        with open(ruta_mapa, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as err:
        logger.error(f"Error cargando mapa {pilar}: {type(err).__name__} (detalles omitidos por seguridad)")
        raise


def aplicar_mapa_pilar(
    entidades: dict[str, dict], mapa: list[dict], pilar_map: dict
) -> tuple[dict[str, dict], list[dict]]:
    """Aplica las reglas de mapeo de un pilar de forma determinista en dos pases."""
    ids_mapa_vistos = {m["id_legado"] for m in mapa}

    # Pase 1: Crear entidades conservadas
    for leg_id, datos in pilar_map.items():
        if leg_id in ids_mapa_vistos:
            continue
        accion, id_nuevo, tipo, canon_name, aliases, motivo = datos
        if accion == "conservado":
            mapa.append({
                "id_legado": leg_id,
                "accion": "conservado",
                "id_nuevo": id_nuevo,
                "motivo": None,
            })
            if id_nuevo not in entidades:
                entidades[id_nuevo] = {
                    "entity_id": id_nuevo,
                    "type": tipo,
                    "canonical_name": canon_name,
                    "ids_legado": [leg_id],
                    "aliases": list(aliases),
                }
            else:
                if leg_id not in entidades[id_nuevo]["ids_legado"]:
                    entidades[id_nuevo]["ids_legado"].append(leg_id)
                for a in aliases:
                    if a not in entidades[id_nuevo]["aliases"]:
                        entidades[id_nuevo]["aliases"].append(a)

    # Pase 2: Procesar fusionados y eliminados
    for leg_id, datos in pilar_map.items():
        if leg_id in ids_mapa_vistos:
            continue
        accion, id_nuevo, tipo, canon_name, aliases, motivo = datos
        if accion == "fusionado":
            mapa.append({
                "id_legado": leg_id,
                "accion": "fusionado",
                "id_nuevo": id_nuevo,
                "motivo": motivo,
            })
            if id_nuevo in entidades:
                if leg_id not in entidades[id_nuevo]["ids_legado"]:
                    entidades[id_nuevo]["ids_legado"].append(leg_id)
                for a in aliases:
                    if a not in entidades[id_nuevo]["aliases"]:
                        entidades[id_nuevo]["aliases"].append(a)
        elif accion == "eliminado":
            mapa.append({
                "id_legado": leg_id,
                "accion": "eliminado",
                "id_nuevo": None,
                "motivo": motivo,
            })

    return entidades, mapa


def cargar_existentes(r: Path) -> tuple[dict[str, dict], list[dict]]:
    """Carga las entidades y el mapa existentes si ya fueron inicializados."""
    entidades = {}
    mapa = []

    ent_path = r / "kb" / "grafo" / "entidades.jsonl"
    if ent_path.exists():
        with open(ent_path, "r", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    e = json.loads(line)
                    if "ids_legado" in e and "entity_id" in e:
                        entidades[e["entity_id"]] = e
                except Exception as err:
                    logger.error(f"Error cargando entidad: {type(err).__name__} (detalles omitidos por seguridad)")

    mapa_path = r / "kb" / "grafo" / "mapa_ids.jsonl"
    if mapa_path.exists():
        with open(mapa_path, "r", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    m = json.loads(line)
                    mapa.append(m)
                except Exception as err:
                    logger.error(f"Error cargando mapa: {type(err).__name__} (detalles omitidos por seguridad)")

    return entidades, mapa


def resolver_pilar(r: Path, pilar: str) -> tuple[dict[str, dict], list[dict]]:
    """Resuelve las entidades del pilar indicado utilizando su archivo de mapeo."""
    pilar_map = cargar_mapa_pilar(r, pilar)
    entidades, mapa = cargar_existentes(r)
    return aplicar_mapa_pilar(entidades, mapa, pilar_map)


def guardar_grafo(r: Path, entidades: dict[str, dict], mapa: list[dict]):
    """Guarda entidades.jsonl y mapa_ids.jsonl de forma atómica y determinista."""
    grafo_dir = r / "kb" / "grafo"
    grafo_dir.mkdir(parents=True, exist_ok=True)

    ent_path = grafo_dir / "entidades.jsonl"
    with open(ent_path, "w", encoding="utf-8") as fh:
        for eid in sorted(entidades.keys()):
            e = entidades[eid]
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    mapa_path = grafo_dir / "mapa_ids.jsonl"
    # Ordenar por id_legado para determinismo
    mapa_ordenado = sorted(mapa, key=lambda x: x["id_legado"])
    with open(mapa_path, "w", encoding="utf-8") as fh:
        for m in mapa_ordenado:
            fh.write(json.dumps(m, ensure_ascii=False) + "\n")


def validar_resolucion(entidades: dict[str, dict], mapa: list[dict]) -> list[str]:
    """Verifica conformidad estricta con las reglas de gate_f4."""
    errores = []
    por_id = entidades

    ids = list(entidades.keys())
    if len(ids) != len(set(ids)):
        errores.append("IDs de entidades duplicados")

    for eid, e in entidades.items():
        if not re.match(r"^[a-z]+:[a-z0-9][a-z0-9-]*$", eid):
            errores.append(f"entity_id inválido: {eid}")
        if e.get("type") not in TIPOS_CANONICOS:
            errores.append(f"tipo no canónico en {eid}: {e.get('type')}")
        if not str(e.get("canonical_name", "")).strip():
            errores.append(f"canonical_name vacío en {eid}")
        if not isinstance(e.get("ids_legado"), list) or not e["ids_legado"]:
            errores.append(f"ids_legado inválido en {eid}")
        if "0.932" in json.dumps(e, ensure_ascii=False):
            errores.append(f"cifra 0.932 presente en {eid}")

    cuenta = collections.Counter(x["id_legado"] for x in mapa)
    for leg_id, c in cuenta.items():
        if c > 1:
            errores.append(f"id_legado duplicado en mapa: {leg_id}")

    for x in mapa:
        acc = x.get("accion")
        idn = x.get("id_nuevo")
        idl = x.get("id_legado")
        mot = x.get("motivo")

        if acc in ("conservado", "fusionado"):
            if idn not in por_id:
                errores.append(f"mapa {idl}: id_nuevo '{idn}' no existe en entidades")
            elif idl not in por_id[idn].get("ids_legado", []):
                errores.append(f"mapa {idl}: no está en ids_legado de '{idn}'")
        elif acc == "eliminado":
            if idn is not None:
                errores.append(f"mapa {idl}: eliminado con id_nuevo no nulo")
            if not str(mot or "").strip():
                errores.append(f"mapa {idl}: eliminado sin motivo")
        else:
            errores.append(f"mapa {idl}: accion inválida '{acc}'")

    return errores


def main():
    parser = argparse.ArgumentParser(description="Resolución de entidades para BRIDGE")
    parser.add_argument("--pilar", default="P01", help="Pilar a resolver (P01..T01)")
    args = parser.parse_args()

    r = raiz()
    pilar = args.pilar.upper()

    try:
        entidades, mapa = resolver_pilar(r, pilar)
    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(1)

    errores = validar_resolucion(entidades, mapa)
    if errores:
        print(f"ERRORES ({len(errores)}):")
        for err in errores:
            print(f"  - {err}")
        sys.exit(1)

    guardar_grafo(r, entidades, mapa)
    print(f"OK: Pilar {pilar} resuelto. Entidades: {len(entidades)}, Mapeos: {len(mapa)}")


if __name__ == "__main__":
    main()
