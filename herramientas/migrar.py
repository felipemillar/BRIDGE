"""Herramienta de migración y reestructuración física determinista de BRIDGE.

Implementa las tareas de la Fase F2 según auditoria/PLAN_MIGRACION_ANTIGRAVITY.md:
- F2.2: Migración de datos (banco_preguntas.jsonl, <QID>.json, pilar.json, fuentes.jsonl).
- F2.3: Reubicación de archivos heredados según Anexo C.
- F2.4: División de BITACORA.md en gobernanza/bitacora/AAAA-MM-DD-NN-<slug>.md.
- F2.5: Conversión de enlaces absolutos file:/// a rutas relativas y reemplazo de enlaces a scripts retirados.
- F2.6: Limpieza de carpetas heredadas y configuración de staging/.
"""
import glob
import json
import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent.parent
if str(_RAIZ) not in sys.path:
    sys.path.insert(0, str(_RAIZ))

try:
    from herramientas.kb import (
        PILARES,
        cargar_banco,
        cargar_manifiestos,
        cargar_respuestas,
        raiz,
        slug,
    )
except ModuleNotFoundError:
    from kb import (
        PILARES,
        cargar_banco,
        cargar_manifiestos,
        cargar_respuestas,
        raiz,
        slug,
    )

logger = logging.getLogger("migrar")

CABECERA_LEGADO = (
    "> Documento heredado del 2026-10-01. Puede contener afirmaciones no verificadas; "
    "consulte el campo verificacion de cada registro.\n\n"
)


def pilar_dir(p: str, titulos: dict[str, str]) -> str:
    """Calcula el nombre del directorio para un pilar dado."""
    return f"{p}-{slug(titulos[p])}"


def migrar_datos() -> None:
    """Ejecuta la tarea F2.2: migración de registros y manifiestos a kb/pilares/ y kb/canon/."""
    r = raiz()
    banco, titulos = cargar_banco()
    respuestas = cargar_respuestas()
    manifiestos = cargar_manifiestos()

    # 1. Crear kb/canon/banco_preguntas.jsonl
    canon_dir = r / "kb" / "canon"
    canon_dir.mkdir(parents=True, exist_ok=True)
    banco_path = canon_dir / "banco_preguntas.jsonl"
    with open(banco_path, "w", encoding="utf-8") as fh:
        for qid, b in banco.items():
            fila = {
                "question_id": qid,
                "pilar": b["pilar"],
                "eje": b["eje"],
                "eje_n": b["eje_n"],
                "subeje": b["subeje"],
                "tipo": b["tipo"],
                "question_text": b["question_text"],
            }
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")

    # 2. Migrar registros de respuestas individuales
    for reg in respuestas:
        qid = reg["question_id"]
        b = banco[qid]
        p_dir = pilar_dir(b["pilar"], titulos)
        eje_dir = b["eje_dir"]
        dest_dir = r / "kb" / "pilares" / p_dir / "ejes" / eje_dir
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / f"{qid}.json"

        # Reordenar llaves: question_id, luego los 5 campos de ubicación, luego el resto
        nuevo_reg = {"question_id": qid}
        nuevo_reg["pilar"] = b["pilar"]
        nuevo_reg["eje"] = b["eje"]
        nuevo_reg["eje_n"] = b["eje_n"]
        nuevo_reg["subeje"] = b["subeje"]
        nuevo_reg["tipo"] = b["tipo"]

        for k, v in reg.items():
            if k not in ("question_id", "pilar", "eje", "eje_n", "subeje", "tipo", "__ruta"):
                nuevo_reg[k] = v

        with open(dest_file, "w", encoding="utf-8") as fh:
            json.dump(nuevo_reg, fh, indent=2, ensure_ascii=False)
            fh.write("\n")

    # 3. Migrar manifiestos de fuentes a pilar.json y fuentes.jsonl
    for p, data in manifiestos.items():
        p_dir = pilar_dir(p, titulos)
        p_dest = r / "kb" / "pilares" / p_dir
        p_dest.mkdir(parents=True, exist_ok=True)

        meta_file = p_dest / "pilar.json"
        with open(meta_file, "w", encoding="utf-8") as fh:
            json.dump(data["meta"], fh, indent=2, ensure_ascii=False)
            fh.write("\n")

        src_file = p_dest / "fuentes.jsonl"
        with open(src_file, "w", encoding="utf-8") as fh:
            for s in data["sources"]:
                fh.write(json.dumps(s, ensure_ascii=False) + "\n")


def reubicar_archivos() -> None:
    """Ejecuta la tarea F2.3: reubicación de archivos heredados según Anexo C."""
    r = raiz()
    banco, titulos = cargar_banco()

    def run_git_mv(origen: Path, destino: Path):
        if origen.exists():
            destino.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "mv", str(origen), str(destino)], cwd=r, check=True)

    # Mandato canónico
    run_git_mv(
        r / "docs_mandato" / "mandato-antigravity-investigacion-asuntos-corporativos.md",
        r / "kb" / "canon" / "mandato.md",
    )

    # Auditoría preliminar
    run_git_mv(
        r / "docs_mandato" / "auditoria-preliminar-cierre-antigravity.md",
        r / "gobernanza" / "auditorias" / "2026-10-01-auditoria-preliminar.md",
    )

    # Síntesis por pilar
    for p in PILARES:
        run_git_mv(
            r / "sintesis" / f"{p}.md",
            r / "kb" / "pilares" / pilar_dir(p, titulos) / "SINTESIS_LEGADO.md",
        )

    # Síntesis transversal
    run_git_mv(
        r / "indice_global.md",
        r / "kb" / "transversal" / "SINTESIS_LEGADO.md",
    )

    # Archivos de grafo
    for gfile in ("entidades.jsonl", "relaciones.jsonl", "contradicciones.jsonl"):
        run_git_mv(r / gfile, r / "kb" / "grafo" / gfile)

    # Archivos de cierre
    for cfile in ("REGISTRO_DE_CIERRE.md", "ejecucion.json", "matriz_cobertura.csv"):
        run_git_mv(r / cfile, r / "gobernanza" / "cierre" / cfile)

    # Agregar aviso de documento heredado
    archivos_aviso = [
        r / "kb" / "transversal" / "SINTESIS_LEGADO.md",
        r / "gobernanza" / "cierre" / "REGISTRO_DE_CIERRE.md",
    ] + [r / "kb" / "pilares" / pilar_dir(p, titulos) / "SINTESIS_LEGADO.md" for p in PILARES]

    for af in archivos_aviso:
        if af.exists():
            txt = af.read_text(encoding="utf-8")
            if not txt.startswith("> Documento heredado"):
                af.write_text(CABECERA_LEGADO + txt, encoding="utf-8")


def dividir_bitacora() -> None:
    """Ejecuta la tarea F2.4: división de BITACORA.md en gobernanza/bitacora/."""
    r = raiz()
    bitacora_path = r / "BITACORA.md"
    if not bitacora_path.exists():
        return

    dest_dir = r / "gobernanza" / "bitacora"
    dest_dir.mkdir(parents=True, exist_ok=True)

    contenido = bitacora_path.read_text(encoding="utf-8")
    lineas = contenido.splitlines()

    entradas = []
    entrada_actual = []
    for l in lineas:
        if l.startswith("## ["):
            if entrada_actual:
                entradas.append(entrada_actual)
            entrada_actual = [l]
        elif entrada_actual:
            entrada_actual.append(l)
    if entrada_actual:
        entradas.append(entrada_actual)

    # Agrupar por fecha. Como en BITACORA.md están en orden cronológico inverso (la más reciente arriba),
    # revertimos para procesar en orden cronológico directo y asignar 01 a la más antigua del día.
    entradas_cronologicas = list(reversed(entradas))
    por_dia = {}
    for ent in entradas_cronologicas:
        primera = ent[0]
        m = re.match(r"^## \[(\d{4}-\d{2}-\d{2})\]\s*-\s*Sesión de Trabajo:\s*(.+)$", primera)
        if not m:
            continue
        fecha = m.group(1)
        titulo = m.group(2).strip()
        por_dia.setdefault(fecha, []).append((titulo, ent))

    for fecha, lista in por_dia.items():
        for idx, (titulo, ent) in enumerate(lista, start=1):
            s_titulo = slug(titulo)
            nombre_archivo = f"{fecha}-{idx:02d}-{s_titulo}.md"
            dest_file = dest_dir / nombre_archivo
            dest_file.write_text("\n".join(ent).rstrip() + "\n", encoding="utf-8")

    # Eliminar BITACORA.md mediante git rm
    subprocess.run(["git", "rm", "BITACORA.md"], cwd=r, check=True)


def convertir_enlaces() -> None:
    """Ejecuta la tarea F2.5: conversión de enlaces file:/// a relativos y manejo de scripts retirados."""
    r = raiz()
    banco, titulos = cargar_banco()

    # Mapeo de rutas heredadas a nuevas rutas relativas desde la raíz
    mapa_rutas = {
        "docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md": "kb/canon/mandato.md",
        "docs_mandato/auditoria-preliminar-cierre-antigravity.md": "gobernanza/auditorias/2026-10-01-auditoria-preliminar.md",
        "indice_global.md": "kb/transversal/SINTESIS_LEGADO.md",
        "entidades.jsonl": "kb/grafo/entidades.jsonl",
        "relaciones.jsonl": "kb/grafo/relaciones.jsonl",
        "contradicciones.jsonl": "kb/grafo/contradicciones.jsonl",
        "REGISTRO_DE_CIERRE.md": "gobernanza/cierre/REGISTRO_DE_CIERRE.md",
        "ejecucion.json": "gobernanza/cierre/ejecucion.json",
        "matriz_cobertura.csv": "gobernanza/cierre/matriz_cobertura.csv",
        "BITACORA.md": "gobernanza/bitacora/",
    }
    for p in PILARES:
        mapa_rutas[f"sintesis/{p}.md"] = f"kb/pilares/{pilar_dir(p, titulos)}/SINTESIS_LEGADO.md"
        mapa_rutas[f"fuentes/{p}.json"] = f"kb/pilares/{pilar_dir(p, titulos)}/pilar.json"
        mapa_rutas[f"respuestas/{p}.jsonl"] = f"kb/pilares/{pilar_dir(p, titulos)}/"

    # Regex genérico para enlaces file:/// hacia BRIDGE (sin incluir rutas absolutas fijas)
    patron_file = re.compile(r"\[([^\]]+)\]\(file://[^\)]*?/BRIDGE/([^\)]+)\)")

    # Procesar todos los archivos markdown fuera de auditoria/ y kb/canon/
    for root, dirs, files in os.walk(r):
        rel_root = os.path.relpath(root, r)
        if any(rel_root.startswith(excl) for excl in ("auditoria", "kb/canon", ".git")):
            continue

        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = Path(root) / f
            doc_dir = fpath.parent
            contenido = fpath.read_text(encoding="utf-8")
            modificado = False

            def repl_file(match):
                nonlocal modificado
                texto = match.group(1)
                subruta = match.group(2)
                # Separar ancla si existe
                if "#" in subruta:
                    subruta_sin_ancla, ancla = subruta.split("#", 1)
                    ancla_str = f"#{ancla}"
                else:
                    subruta_sin_ancla, ancla_str = subruta, ""

                # Verificar si es un script que se retira
                if subruta_sin_ancla.startswith("scripts/"):
                    modificado = True
                    return f"{texto} (retirado; ver tag pre-migracion)"

                # Reubicar destino si está en mapa_rutas
                nueva_subruta = mapa_rutas.get(subruta_sin_ancla, subruta_sin_ancla)
                dest_abs = r / nueva_subruta
                dest_rel = os.path.relpath(dest_abs, doc_dir)
                modificado = True
                return f"[{texto}]({dest_rel}{ancla_str})"

            nuevo_contenido = patron_file.sub(repl_file, contenido)

            # Reparar enlaces relativos existentes que apuntaban a archivos que cambiaron de lugar
            def repl_rel(match):
                nonlocal modificado
                texto = match.group(1)
                destino = match.group(2)
                if re.match(r"^(https?:|mailto:|#)", destino):
                    return match.group(0)
                if "#" in destino:
                    dest_path, ancla = destino.split("#", 1)
                    ancla_str = f"#{ancla}"
                else:
                    dest_path, ancla_str = destino, ""

                # Resolver respecto a doc_dir
                target_abs = (doc_dir / dest_path).resolve()
                try:
                    rel_to_r = os.path.relpath(target_abs, r)
                except ValueError:
                    return match.group(0)

                if rel_to_r in mapa_rutas:
                    nueva_rel = os.path.relpath(r / mapa_rutas[rel_to_r], doc_dir)
                    modificado = True
                    return f"[{texto}]({nueva_rel}{ancla_str})"
                elif rel_to_r.startswith("scripts/"):
                    modificado = True
                    return f"{texto} (retirado; ver tag pre-migracion)"

                return match.group(0)

            patron_rel = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
            nuevo_contenido = patron_rel.sub(repl_rel, nuevo_contenido)

            if modificado:
                fpath.write_text(nuevo_contenido, encoding="utf-8")


def limpiar_legado() -> None:
    """Ejecuta la tarea F2.6: eliminar carpetas heredadas y configurar staging/."""
    r = raiz()

    # Eliminar carpetas heredadas
    carpetas_a_eliminar = ["respuestas", "fuentes", "sintesis", "scripts", "docs_mandato"]
    for carp in carpetas_a_eliminar:
        cdir = r / carp
        if cdir.exists():
            subprocess.run(["git", "rm", "-rf", carp], cwd=r, check=False)
            if cdir.exists():
                shutil.rmtree(cdir, ignore_errors=True)

    # Configurar staging/
    staging_dir = r / "staging"
    staging_dir.mkdir(parents=True, exist_ok=True)
    gitkeep = staging_dir / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.touch()

    # Actualizar .gitignore si no contiene staging/
    gi_path = r / ".gitignore"
    gi_txt = gi_path.read_text(encoding="utf-8") if gi_path.exists() else ""
    if "staging/" not in gi_txt:
        if gi_txt and not gi_txt.endswith("\n"):
            gi_txt += "\n"
        gi_txt += "staging/\n"
        gi_path.write_text(gi_txt, encoding="utf-8")


def main():
    """Punto de entrada CLI de migrar.py."""
    try:
        print("Iniciando migración determinista F2...")
        migrar_datos()
        print("F2.2 migrar_datos: OK")
        reubicar_archivos()
        print("F2.3 reubicar_archivos: OK")
        dividir_bitacora()
        print("F2.4 dividir_bitacora: OK")
        convertir_enlaces()
        print("F2.5 convertir_enlaces: OK")
        limpiar_legado()
        print("F2.6 limpiar_legado: OK")
        print("Reestructuración física F2 completada con éxito.")
    except Exception as err:
        logger.error(f"Error en migración: {type(err).__name__} (detalles omitidos por seguridad)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
