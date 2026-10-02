"""Generador de vistas canónicas y derivados de la base de conocimiento BRIDGE.

Regenera de forma determinista y reproducible:
  - kb/CATALOGO.json
  - kb/pilares/<PILAR_DIR>/TARJETA.md (12 archivos)
  - kb/pilares/<PILAR_DIR>/ejes/<EJE_DIR>/EJE.md (108 archivos)
  - kb/afirmaciones.jsonl (1318 filas)
  - kb/export/chunks.jsonl (2182 filas: 864 respuesta_corta + 1318 afirmacion)
  - kb/transversal/vacios.jsonl (470 filas)
  - kb/indices/preguntas.jsonl y kb/indices/fuentes.jsonl (vía construir_indices())
  - README.md
"""
import collections
import hashlib
import json
import logging
import os
import re
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
    from herramientas.construir_indice import MODULO, construir_indices
except ModuleNotFoundError:
    from kb import (
        PILARES,
        cargar_banco,
        cargar_manifiestos,
        cargar_respuestas,
        raiz,
        slug,
    )
    from construir_indice import MODULO, construir_indices

logger = logging.getLogger("generar_vistas")

MARCA_GENERADO = "<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->"

SECCIONES_TARJETA = [
    "## Alcance",
    "## Ejes",
    "## Fuentes rectoras y precedencia",
    "## Estado de verificación",
    "## Vacíos abiertos",
    "## Cómo leer este pilar",
]


def pilar_dir(p: str, titulos: dict[str, str]) -> str:
    """Retorna el nombre canónico de la carpeta de un pilar."""
    return f"{p}-{slug(titulos[p])}"


def calcular_huella_datos(r: Path) -> str:
    """Calcula el SHA-256 de los hashes ordenados de todos los .json y .jsonl de kb/pilares/."""
    pilares_dir = r / "kb" / "pilares"
    archivos = []
    for ext in ("**/*.json", "**/*.jsonl"):
        for p in pilares_dir.glob(ext):
            if p.is_file():
                archivos.append(p)
    archivos.sort(key=lambda p: str(p.relative_to(r)))

    hashes = []
    for p in archivos:
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        hashes.append(h)
    return hashlib.sha256("\n".join(hashes).encode("utf-8")).hexdigest()


def contar_lineas_archivo(ruta: Path) -> int:
    """Cuenta líneas no vacías en un archivo si existe."""
    if ruta.exists():
        with open(ruta, "r", encoding="utf-8") as fh:
            return sum(1 for line in fh if line.strip())
    return 0


def generar_catalogo(
    r: Path,
    respuestas: list[dict],
    banco: dict,
    titulos: dict,
    manifiestos: dict,
    finds: list,
    verif_counts: dict,
    huella_datos: str,
) -> dict:
    """Genera y guarda kb/CATALOGO.json según Anexo E."""
    ev_total = sum(len(f.get("evidence", [])) for _, f in finds)
    fuentes_total = sum(len(m.get("sources", [])) for m in manifiestos.values())

    totales = {
        "preguntas": len(respuestas),
        "hallazgos": len(finds),
        "evidencias": ev_total,
        "fuentes": fuentes_total,
        "entidades": contar_lineas_archivo(r / "kb" / "grafo" / "entidades.jsonl"),
        "relaciones": contar_lineas_archivo(r / "kb" / "grafo" / "relaciones.jsonl"),
        "contradicciones": contar_lineas_archivo(r / "kb" / "grafo" / "contradicciones.jsonl"),
    }

    estados_ordenados = ["no_verificada", "en_proceso", "no_verificable", "verificada", "refutada"]
    verificacion = {est: verif_counts.get(est, 0) for est in estados_ordenados}

    pilares_info = []
    for p in PILARES:
        p_dir = pilar_dir(p, titulos)
        n_p = sum(1 for reg in respuestas if reg.get("pilar") == p or banco[reg["question_id"]]["pilar"] == p)
        pilares_info.append({
            "pilar": p,
            "titulo": titulos[p],
            "ruta": f"kb/pilares/{p_dir}",
            "modulo": MODULO.get(p, "transversal"),
            "n_preguntas": n_p,
            "n_ejes": 9,
        })

    catalogo = {
        "huella_datos": huella_datos,
        "totales": totales,
        "verificacion": verificacion,
        "pilares": pilares_info,
    }

    cat_path = r / "kb" / "CATALOGO.json"
    cat_json = json.dumps(catalogo, ensure_ascii=False, indent=2) + "\n"

    if len(cat_json) > 10000:
        raise ValueError("kb/CATALOGO.json supera el límite de 10000 caracteres")
    if re.search(r"\d{4}-\d{2}-\d{2}T\d", cat_json):
        raise ValueError("kb/CATALOGO.json contiene marcas de tiempo prohibidas")

    cat_path.write_text(cat_json, encoding="utf-8")
    return catalogo


def extraer_gap_info(g: str | dict) -> tuple[str, str | None, str]:
    """Extrae (gap, minimum_validation, priority) de un open_gap (str o dict)."""
    if isinstance(g, dict):
        gap = g.get("gap") or g.get("description") or ""
        min_val = g.get("minimum_validation")
        prio = g.get("priority") or "media"
    else:
        gap = str(g)
        min_val = None
        prio = "media"
    return gap, min_val, prio


def generar_tarjetas(
    r: Path,
    respuestas: list[dict],
    banco: dict,
    titulos: dict,
    manifiestos: dict,
    ejes_dict: dict,
) -> None:
    """Genera las 12 TARJETA.md en kb/pilares/<PILAR_DIR>/TARJETA.md."""
    resps_por_pilar = collections.defaultdict(list)
    for reg in respuestas:
        p = reg.get("pilar") or banco[reg["question_id"]]["pilar"]
        resps_por_pilar[p].append(reg)

    for p in PILARES:
        p_dir = pilar_dir(p, titulos)
        p_path = r / "kb" / "pilares" / p_dir / "TARJETA.md"
        p_resps = resps_por_pilar[p]
        m = manifiestos.get(p, {})

        # Conteo de verificación en este pilar
        p_finds = [f for reg in p_resps for f in reg.get("findings", [])]
        v_counts = collections.Counter(f.get("verificacion", {}).get("estado") for f in p_finds)

        # Vacíos abiertos de este pilar (top 10 por prioridad)
        p_gaps = []
        prio_map = {"alta": 1, "media": 2, "baja": 3}
        for reg in p_resps:
            qid = reg["question_id"]
            for g in reg.get("open_gaps", []):
                gap_txt, min_v, prio = extraer_gap_info(g)
                p_gaps.append({
                    "question_id": qid,
                    "gap": gap_txt,
                    "priority": prio,
                    "min_val": min_v,
                })
        p_gaps.sort(key=lambda x: (prio_map.get(x["priority"], 9), x["question_id"], x["gap"] or ""))
        top_gaps = p_gaps[:10]

        # Fuentes rectoras destacadas
        sources = m.get("sources", [])
        src_lines = []
        for s in sorted(sources, key=lambda x: -(x.get("word_count") or 0))[:5]:
            src_lines.append(f"- **{s['source_id']}**: {s.get('title', '')} (`{s.get('text_status', '')}`)")

        # Enlaces a ejes
        eje_lines = []
        for ed in sorted(ejes_dict.get(p, {}).keys()):
            eje_nombre = ejes_dict[p][ed]["nombre"]
            eje_lines.append(f"- [Eje {ed}: {eje_nombre}](ejes/{ed}/EJE.md)")

        gap_lines = []
        if top_gaps:
            for g in top_gaps:
                gap_lines.append(f"- **[{g['question_id']}]** ({g['priority']}): {g['gap']}")
        else:
            gap_lines.append("- *Sin vacíos abiertos registrados en este pilar.*")

        tarjeta = f"""{MARCA_GENERADO}
# Pilar {p}: {titulos[p]}

## Alcance
Este pilar forma parte del módulo **{MODULO.get(p, "transversal")}** en el programa canónico BRIDGE.
Contiene 9 ejes de investigación temática y 72 preguntas atómicas ejecutadas bajo el Mandato de Asuntos Corporativos.
Su propósito es establecer la evidencia empírica, legal y procedimental para este ámbito directivo.

## Ejes
{chr(10).join(eje_lines)}

## Fuentes rectoras y precedencia
> **Regla de precedencia:** {m.get("editorial_precedence_rule", "Precedencia canónica estándar.")}

### Fuentes principales del pilar ({len(sources)} fuentes registradas)
{chr(10).join(src_lines)}

## Estado de verificación
Distribución de verificación para los {len(p_finds)} hallazgos del pilar:
- `no_verificada`: {v_counts.get("no_verificada", 0)}
- `en_proceso`: {v_counts.get("en_proceso", 0)}
- `no_verificable`: {v_counts.get("no_verificable", 0)}
- `verificada`: {v_counts.get("verificada", 0)}
- `refutada`: {v_counts.get("refutada", 0)}

## Vacíos abiertos
{chr(10).join(gap_lines)}

## Cómo leer este pilar
La base de conocimiento está organizada en 5 niveles de granularidad:
- **Nivel L0 (Catálogo y Mandato):** Visión global en [kb/CATALOGO.json](../../CATALOGO.json) y el mandato rector.
- **Nivel L1 (Tarjeta de Pilar):** Este documento resumen con alcance, ejes y reglas de precedencia.
- **Nivel L2 (Fichas de Eje):** Síntesis de cada eje en sus respectivas rutas `ejes/<EJE_DIR>/EJE.md`.
- **Nivel L3 (Registros de Pregunta):** Respuestas atómicas en formato JSON (`<QID>.json`) con 20 atributos.
- **Nivel L4 (Fuentes Primarias):** Evidencias y metadatos documentales en `fuentes.jsonl` del pilar.
"""
        if len(tarjeta) > 10500:
            raise ValueError(f"TARJETA.md de {p} supera los 10500 caracteres ({len(tarjeta)})")
        for sec in SECCIONES_TARJETA:
            if sec not in tarjeta:
                raise ValueError(f"TARJETA.md de {p} carece de la sección obligatoria {sec}")

        p_path.write_text(tarjeta, encoding="utf-8")


def generar_ejes(
    r: Path,
    respuestas: list[dict],
    banco: dict,
    titulos: dict,
    ejes_dict: dict,
) -> None:
    """Genera los 108 EJE.md en kb/pilares/<PILAR_DIR>/ejes/<EJE_DIR>/EJE.md."""
    resps_map = {reg["question_id"]: reg for reg in respuestas}

    for p in PILARES:
        p_dir = pilar_dir(p, titulos)
        for ed in sorted(ejes_dict.get(p, {}).keys()):
            eje_info = ejes_dict[p][ed]
            eje_nombre = eje_info["nombre"]
            qs = eje_info["questions"]
            eje_path = r / "kb" / "pilares" / p_dir / "ejes" / ed / "EJE.md"

            q_blocks = []
            for qid in sorted(qs):
                reg = resps_map.get(qid, {})
                q_text = reg.get("question_text") or banco[qid]["question_text"]
                short_ans = (reg.get("short_answer") or "")[:300].strip()
                findings = reg.get("findings", [])
                v_counts = collections.Counter(f.get("verificacion", {}).get("estado") for f in findings)
                v_str = ", ".join(f"{k}: {v}" for k, v in sorted(v_counts.items())) if v_counts else "sin hallazgos"

                q_blocks.append(
                    f"### {qid}: {q_text}\n\n"
                    f"> {short_ans}\n\n"
                    f"- **Verificación:** {v_str}\n"
                    f"- **Registro:** [{qid}.json]({qid}.json)\n"
                )

            eje_md = f"""{MARCA_GENERADO}
# Eje {ed}: {eje_nombre}

**Pilar:** [{p} — {titulos[p]}](../../TARJETA.md)  
**Módulo:** {MODULO.get(p, "transversal")}

---

## Preguntas del Eje ({len(qs)})

{"".join(q_blocks)}
"""
            if len(eje_md) > 7000:
                raise ValueError(f"EJE.md de {p}/{ed} supera los 7000 caracteres ({len(eje_md)})")
            for qid in qs:
                if qid not in eje_md:
                    raise ValueError(f"EJE.md de {p}/{ed} no contiene el QID {qid}")

            eje_path.write_text(eje_md, encoding="utf-8")


def generar_afirmaciones(
    r: Path,
    respuestas: list[dict],
    banco: dict,
    titulos: dict,
) -> list[dict]:
    """Genera kb/afirmaciones.jsonl con 1318 filas según Anexo E."""
    afirmaciones = []
    for reg in respuestas:
        qid = reg["question_id"]
        b = banco[qid]
        p = b["pilar"]
        p_dir = pilar_dir(p, titulos)
        ruta = reg.get("__ruta") or f"kb/pilares/{p_dir}/ejes/{b['eje_dir']}/{qid}.json"

        for f in reg.get("findings", []):
            fuentes = []
            for ev in f.get("evidence", []):
                sid = ev.get("source_id")
                if sid and sid not in fuentes:
                    fuentes.append(sid)
            afirmaciones.append({
                "claim_id": f["claim_id"],
                "question_id": qid,
                "pilar": p,
                "eje_n": b["eje_n"],
                "claim": f["claim"],
                "epistemic_status": f["epistemic_status"],
                "confidence": f["confidence"],
                "verificacion_estado": f["verificacion"]["estado"],
                "fuentes": fuentes,
                "ruta": ruta,
            })

    afirmaciones.sort(key=lambda a: a["claim_id"])
    af_path = r / "kb" / "afirmaciones.jsonl"
    with open(af_path, "w", encoding="utf-8") as fh:
        for a in afirmaciones:
            fh.write(json.dumps(a, ensure_ascii=False) + "\n")
    return afirmaciones


def generar_chunks(
    r: Path,
    respuestas: list[dict],
    banco: dict,
    titulos: dict,
) -> list[dict]:
    """Genera kb/export/chunks.jsonl con 2182 filas (864 respuesta_corta + 1318 afirmacion)."""
    out_dir = r / "kb" / "export"
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = []

    # 864 chunks de respuesta_corta
    for reg in respuestas:
        qid = reg["question_id"]
        b = banco[qid]
        p = b["pilar"]
        p_dir = pilar_dir(p, titulos)
        ruta = reg.get("__ruta") or f"kb/pilares/{p_dir}/ejes/{b['eje_dir']}/{qid}.json"
        txt = (reg.get("short_answer") or "")[:4000]

        chunks.append({
            "chunk_id": f"chunk:{qid}:rc",
            "tipo": "respuesta_corta",
            "texto": txt,
            "metadatos": {
                "question_id": qid,
                "pilar": p,
                "eje_n": b["eje_n"],
                "modulo": MODULO.get(p, "transversal"),
                "answer_status": reg.get("answer_status"),
                "ruta": ruta,
            },
        })

    # 1318 chunks de afirmación
    for reg in respuestas:
        qid = reg["question_id"]
        b = banco[qid]
        p = b["pilar"]
        p_dir = pilar_dir(p, titulos)
        ruta = reg.get("__ruta") or f"kb/pilares/{p_dir}/ejes/{b['eje_dir']}/{qid}.json"

        for f in reg.get("findings", []):
            cid = f["claim_id"]
            txt = (f.get("claim") or "")[:4000]
            fuentes = [ev.get("source_id") for ev in f.get("evidence", []) if ev.get("source_id")]

            chunks.append({
                "chunk_id": f"chunk:{cid}",
                "tipo": "afirmacion",
                "texto": txt,
                "metadatos": {
                    "question_id": qid,
                    "claim_id": cid,
                    "pilar": p,
                    "eje_n": b["eje_n"],
                    "modulo": MODULO.get(p, "transversal"),
                    "epistemic_status": f.get("epistemic_status"),
                    "confidence": f.get("confidence"),
                    "verificacion_estado": f.get("verificacion", {}).get("estado"),
                    "fuentes": fuentes,
                    "ruta": ruta,
                },
            })

    chunks.sort(key=lambda c: c["chunk_id"])
    ch_path = out_dir / "chunks.jsonl"
    with open(ch_path, "w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    return chunks


def generar_vacios(
    r: Path,
    respuestas: list[dict],
    banco: dict,
) -> list[dict]:
    """Genera kb/transversal/vacios.jsonl con 470 vacíos abiertos según Anexo E."""
    out_dir = r / "kb" / "transversal"
    out_dir.mkdir(parents=True, exist_ok=True)
    vacios = []

    for reg in respuestas:
        qid = reg["question_id"]
        p = banco[qid]["pilar"]
        for g in reg.get("open_gaps", []):
            gap_txt, min_v, prio = extraer_gap_info(g)
            vacios.append({
                "question_id": qid,
                "pilar": p,
                "gap": gap_txt,
                "minimum_validation": min_v,
                "priority": prio,
            })

    vacios.sort(key=lambda v: (v["question_id"], v.get("gap") or ""))
    v_path = out_dir / "vacios.jsonl"
    with open(v_path, "w", encoding="utf-8") as fh:
        for v in vacios:
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")
    return vacios


def generar_readme(
    r: Path,
    verif_counts: dict,
) -> None:
    """Genera el README.md principal de la base de conocimiento."""
    nv = verif_counts.get("no_verificada", 0)
    ep = verif_counts.get("en_proceso", 0)
    nvb = verif_counts.get("no_verificable", 0)
    ver = verif_counts.get("verificada", 0)
    ref = verif_counts.get("refutada", 0)
    total_finds = nv + ep + nvb + ver + ref

    readme_content = f"""{MARCA_GENERADO}
# The Bridge Intelligence — Programa de Investigación de Asuntos Corporativos

Repositorio central del programa integral de investigación y base de conocimiento canónica de **The Bridge Intelligence** (`thebridgeintelligence.ai`), desarrollado conforme al **Mandato de Extracción Densa de Conocimiento** (v1.0, 30 de septiembre de 2026).

---

## 📌 Resumen Ejecutivo del Catálogo

El programa consolida la base de conocimiento empírica, técnica y legal sobre los **12 cuadernos canónicos de NotebookLM**, cubriendo el ciclo metodológico cuádruple: **Saber** (memoria corporativa e inteligencia documental), **Escuchar** (monitoreo de señales de entorno y riesgos), **Hablar** (aprobación colegiada y consistencia de vocería) y **Relacionar** (gestión estructurada de compromisos y stakeholders), bajo la arquitectura de gobernanza multi-tenant y compuertas de decisión **Stage-Gate (G0–G3)**.

| Parámetro | Métrica Canónica |
| :--- | :--- |
| **Cuadernos Target** | 12 cuadernos canónicos (P01 a P11 + T01) |
| **Total Preguntas Ejecutadas** | 864 / 864 preguntas |
| **Desglose de Preguntas** | 576 Fundamentales (F) + 192 Contraste (C) + 96 Profundización (X) |
| **Universo de Fuentes** | 551 fuentes verificadas en los 12 manifiestos |
| **Hallazgos / Afirmaciones Atómicas** | 1318 afirmaciones tipadas y trazables |
| **Evidencias Estructuradas** | 1935 fragmentos y citas textuales de respaldo |
| **Auditoría de Calidad** | Dictamen independiente en [INFORME_AUDITORIA.md](auditoria/INFORME_AUDITORIA.md) |

---

## 🔍 Estado de Verificación de Hallazgos

De acuerdo con el protocolo de verificación epistémica, el estado consolidado de las 1318 afirmaciones del catálogo es:

| Estado de Verificación | Cantidad | Porcentaje |
| :--- | :--- | :--- |
| `no_verificada` | {nv} | {round(nv / total_finds * 100, 1)}% |
| `en_proceso` | {ep} | {round(ep / total_finds * 100, 1)}% |
| `no_verificable` | {nvb} | {round(nvb / total_finds * 100, 1)}% |
| `verificada` | {ver} | {round(ver / total_finds * 100, 1)}% |
| `refutada` | {ref} | {round(ref / total_finds * 100, 1)}% |
| **Total** | **1318** | **100.0%** |

---

## 🧭 Documentos Clave de Consulta y Gobernanza

- 📋 **[Catálogo Global Canónico](kb/CATALOGO.json)**: Metadatos maestros, totales y rutas de acceso.
- 🛡️ **[Normas de Operación y Agentes](AGENTS.md)**: Reglas de operación de agentes, niveles L0–L4 y error masking.
- 📑 **[Auditorías y Trazabilidad](gobernanza/auditorias/)**: Informes históricos y dictámenes de auditoría previa.
- 📊 **[Índice de Preguntas](kb/indices/preguntas.jsonl)**: Índice navegable con metadatos de las 864 preguntas.
- 📚 **[Índice de Fuentes](kb/indices/fuentes.jsonl)**: Directorio consolidado de las 551 fuentes del catálogo.
- 📝 **[Bitácora de Desarrollo](gobernanza/bitacora/)**: Registro por sesión de los hitos del proyecto.
"""
    r_path = r / "README.md"
    r_path.write_text(readme_content, encoding="utf-8")


def regenerar_todo() -> None:
    """Ejecuta la regeneración determinista completa de vistas e índices."""
    r = raiz()

    # 1. Regenerar índices de preguntas y fuentes
    construir_indices()

    # 2. Cargar datos en memoria
    banco, titulos = cargar_banco()
    respuestas = cargar_respuestas()
    manifiestos = cargar_manifiestos()

    # Estructurar mapa de ejes: pilar -> eje_dir -> {nombre, questions: [qid]}
    ejes_dict = collections.defaultdict(dict)
    for qid, b in banco.items():
        p = b["pilar"]
        ed = b["eje_dir"]
        if ed not in ejes_dict[p]:
            ejes_dict[p][ed] = {"nombre": b["eje"], "questions": []}
        ejes_dict[p][ed]["questions"].append(qid)

    finds = [(reg, f) for reg in respuestas for f in reg.get("findings", [])]
    verif_counts = collections.Counter(f.get("verificacion", {}).get("estado") for _, f in finds)

    # 3. Calcular huella de datos
    huella_datos = calcular_huella_datos(r)

    # 4. Generar derivados
    generar_catalogo(r, respuestas, banco, titulos, manifiestos, finds, verif_counts, huella_datos)
    generar_tarjetas(r, respuestas, banco, titulos, manifiestos, ejes_dict)
    generar_ejes(r, respuestas, banco, titulos, ejes_dict)
    generar_afirmaciones(r, respuestas, banco, titulos)
    generar_chunks(r, respuestas, banco, titulos)
    generar_vacios(r, respuestas, banco)
    generar_readme(r, verif_counts)


def main():
    """Punto de entrada CLI de herramientas/generar_vistas.py."""
    try:
        regenerar_todo()
        print("Vistas e índices regenerados con éxito.")
    except Exception as err:
        logger.error(f"Error al generar vistas: {type(err).__name__} (detalles omitidos por seguridad)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
