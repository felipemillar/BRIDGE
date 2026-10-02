"""Comprobador independiente de la migración BRIDGE (auditoria/PLAN_MIGRACION_ANTIGRAVITY.md).

NO MODIFICAR. Este archivo forma parte de la especificación: su SHA-256 está fijado en el plan.
Si una comprobación parece errónea, el ejecutor debe detenerse y reportarlo (plan §2.6), nunca editarla.

Uso (desde la raíz del repositorio):
    python3 auditoria/comprobar_migracion.py --hasta F2     # compuertas PREP..F2 (acumulativo)
    python3 auditoria/comprobar_migracion.py --fase F1      # solo una compuerta
    python3 auditoria/comprobar_migracion.py --todo         # PREP..F5

Salida: una línea por control, [OK] o [FALLA], y al final «RESULTADO: OK» o «RESULTADO: FALLA (n)».
Código de salida 0 solo si no hay fallas. Requiere solo la biblioteca estándar de Python 3.10+.
"""
import argparse
import collections
import datetime
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path.cwd()
PILARES = ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10", "P11", "T01"]
FASES = ["PREP", "F0", "F1", "F2", "F3", "F4", "F5"]
TAG = "pre-migracion"
RAMA = "migracion-enjambre"

# --- Línea base medida el 2026-10-02 sobre el commit 0e9cf75 ---------------------------------
BASE = {
    "registros": 864, "hallazgos": 1318, "evidencias": 1935, "open_gaps": 470, "fuentes": 551,
    "H_CONTENIDO": "b8d500516e569ffe", "H_ESTRUCTURA": "d3e520ff0b8128e3",
    "H_EPISTEMICO": "616b4e3091c83e7a", "H_TIEMPOS": "05d1a1d8ab5b995d",
    "H_FUENTES": "a9678548653371ec", "SHA_MANDATO": "03c4a01e10dcc763",
    "entidades_legado_unicas": 1515, "relaciones_legado": 477, "contradicciones": 93,
}
SHA_DOCS_AUDITORIA = {
    "auditoria/INFORME_AUDITORIA.md": "340344a6332175c1",
    "auditoria/PROPUESTA_REORGANIZACION.md": "01c08a1617116a3c",
}
UUID_ERRONEO_P01 = "fa3bce30-c045-4299-8d8a-6b45f3df1a1a"
MARCA_GENERADO = "<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->"
LOCALIZADOR_SINTETICO = "Sección sustantiva vinculada"

EPI_CANON = {"hecho_documentado", "declaracion_proveedor", "inferencia", "hipotesis_diseno"}
EPI_MAPA = {
    "fact": "hecho_documentado", "hypothesis": "hipotesis_diseno",
    "propuesta_arquitectura_formal": "hipotesis_diseno", "diseno_de_datos_formal": "hipotesis_diseno",
    "diseno_experimental_formal": "hipotesis_diseno", "patron_diseno_ciberseguridad": "hipotesis_diseno",
    "control_de_ciberseguridad_formal": "hipotesis_diseno", "taxonomia_operacional_gobernanza": "hipotesis_diseno",
    "regla_control_riesgo_reputacional": "hipotesis_diseno", "principio_metodologico_formal": "hipotesis_diseno",
    "modelo_computacional_probado": "inferencia", "modelo_operacional_probado": "inferencia",
    "caso_de_prueba_empirico": "inferencia", "estandar_seguridad_comprobado": "inferencia",
    "prevalencia_editorial_correccion": "inferencia", "vacio_empirico_documentado": "inferencia",
    "patologia_epistemica_documentada": "inferencia", "principio_de_impacto_amec": "inferencia",
}
EPI_ESPERADO = {"hecho_documentado": 1011, "hipotesis_diseno": 157, "inferencia": 106, "declaracion_proveedor": 44}
CONF_ESPERADO = {"alta": 1091, "media": 227}
TS_CANON = {"texto_sustantivo", "resumen_parcial", "solo_navegacion", "captcha", "fallida", "duplicada", "desconocida"}
TS_MAPA = {
    "fallida_o_bloqueada": "fallida", "error_extraccion": "fallida", "fuente_fallida": "fallida",
    "error_extraccion_o_duplicado": "fallida", "directorio_navegacional_no_sustantivo": "solo_navegacion",
    "ficha_abstract_duplicada": "duplicada", "atribucion_comercial_erronea": "desconocida",
}
TS_ESPERADO = {"texto_sustantivo": 493, "fallida": 45, "solo_navegacion": 2, "duplicada": 10, "desconocida": 1}
TS_EVID_ESPERADO = {"texto_sustantivo": 1927, "fallida": 8}
VERIF_ESTADOS = {"no_verificada", "cita_sintetica", "solo_sintesis_interna", "verificada", "refutada", "no_verificable"}
VERIF_PILOTO = {"verificada", "refutada", "no_verificable"}
VERIF_LLAVES = {"estado", "motivos", "verificado_por", "fecha", "metodo", "pasaje"}
MOTIVOS = {"cita_sintetica", "solo_sintesis_interna", "fuente_no_sustantiva", "confianza_numerica_original",
           "estado_epistemico_no_canonico_original", "url_inaccesible", "paywall_o_captcha",
           "pasaje_no_encontrado", "pasaje_contradice", "otro"}
ANSWER_STATUS = {"respondida", "parcial", "sin_evidencia", "fuente_fallida", "conflicto", "bloqueada"}
TIPOS_ENTIDAD = {"organizacion", "persona_rol", "documento", "fuente", "tema", "evento", "compromiso",
                 "producto", "riesgo", "metrica", "experimento"}
ROLES = ["enrutador", "especialista_pilar", "verificador_evidencia", "curador_grafo",
         "analista_contradicciones", "sintetizador_transversal", "auditor", "integrador"]
SECCIONES_ROL = ["## Misión", "## Lee", "## Escribe", "## Presupuesto", "## Contrato de salida",
                 "## Criterio de terminado", "## Prohibido"]
SECCIONES_TARJETA = ["## Alcance", "## Ejes", "## Fuentes rectoras y precedencia", "## Estado de verificación",
                     "## Vacíos abiertos", "## Cómo leer este pilar"]
MUESTRA_PILOTO = [
    "P01-F08-C1", "P01-F04-C2", "P01-F05-C4", "P01-F41-C1", "P01-F04-C3",
    "P02-F01-C3", "P02-F34-C1", "P02-F25-C1", "P02-F29-C1", "P02-F30-C1",
    "P03-F05-C1", "P03-F21-C1", "P03-F14-C1", "P03-F03-C1", "P03-F08-C1",
    "P04-F01-C1", "P04-F03-C1", "P04-F17-C1", "P04-F09-C1", "P04-F13-C1",
    "P05-C13-C1", "P05-F23-C1", "P05-F37-C1", "P05-F29-C1", "P05-F41-C1",
    "P06-X05-C1", "P06-X21-C1", "P06-X13-C1", "P06-X29-C1",
    "P07-F38-C1", "P07-F01-C1", "P07-C05-C1", "P07-F32-C1", "P07-F37-C1",
    "P08-F35-C1", "P08-F23-C1", "P08-F37-C1", "P08-F17-C1", "P08-F19-C1",
    "P09-F46-C1", "P09-F16-C1", "P09-F21-C1", "P09-F15-C1", "P09-F12-C1",
    "P10-F48-C1", "P10-C13-C1", "P10-F11-C1", "P10-F31-C1", "P10-F39-C1",
    "P11-C05-C1", "P11-F28-C1", "P11-F36-C1", "P11-C12-C1", "P11-F02-C1",
    "T01-F28-C1", "T01-F38-C2", "T01-F29-C1", "T01-F36-C1", "T01-X02-C1",
]
RAIZ_PERMITIDA = {".git", ".gitignore", ".agents", ".DS_Store", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "README.md",
                  "kb", "enjambre", "gobernanza", "herramientas", "migracion", "auditoria", "staging"}
LEGADO_AUSENTE_F2 = ["respuestas", "fuentes", "sintesis", "scripts", "docs_mandato", "entidades.jsonl",
                     "relaciones.jsonl", "contradicciones.jsonl", "matriz_cobertura.csv", "ejecucion.json",
                     "REGISTRO_DE_CIERRE.md", "indice_global.md", "BITACORA.md"]
HERRAMIENTAS = ["kb.py", "normalizar.py", "migrar.py", "construir_indice.py", "generar_vistas.py", "validar.py"]


# --- utilidades -----------------------------------------------------------------------------
class Reporte:
    def __init__(self):
        self.fallas = 0

    def control(self, ok, texto, detalle=None):
        if ok:
            print(f"  [OK] {texto}")
        else:
            self.fallas += 1
            extra = f" → {detalle}" if detalle else ""
            print(f"  [FALLA] {texto}{extra}")
        return ok


def sha16(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def sha_archivo(path, n=16):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:n]


def git(*args, check=False):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("git " + " ".join(args))
    return r


def slug(texto):
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].rstrip("-")


def orig(d, k):
    return d[k + "_original"] if (k + "_original") in d else d.get(k)


def url_de(x):
    if isinstance(x, list):
        try:
            x = x[7][0]
        except (TypeError, IndexError):
            x = None
    return x if isinstance(x, str) and x.startswith("http") else None


def leer_jsonl(path):
    return [json.loads(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]


def ruta_mandato():
    for p in ("kb/canon/mandato.md", "docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md"):
        if (ROOT / p).exists():
            return ROOT / p
    return None


def parse_banco(texto):
    """{qid: dict(pilar, eje, subeje, eje_n, eje_dir, tipo, question_text)} y {pilar: título}."""
    banco, titulos = {}, {}
    pilar = eje = subeje = None
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
            banco[m.group(1)] = {
                "pilar": pilar, "eje": eje, "subeje": subeje, "eje_n": orden[pilar].index(grupo) + 1,
                "eje_dir": f"{orden[pilar].index(grupo) + 1:02d}-{slug(grupo)}", "tipo": m.group(2),
                "question_text": m.group(3).strip(),
            }
    return banco, titulos


def pilar_dir(p, titulos):
    return f"{p}-{slug(titulos[p])}"


def layout_nuevo():
    return (ROOT / "kb" / "pilares").exists()


def cargar_respuestas():
    if layout_nuevo():
        rows = []
        for f in glob.glob(str(ROOT / "kb/pilares/*/ejes/*/*.json")):
            if re.match(r"^(P\d\d|T01)-[FCX]\d\d\.json$", os.path.basename(f)):
                r = json.loads(Path(f).read_text(encoding="utf-8"))
                r["__ruta"] = os.path.relpath(f, ROOT)
                rows.append(r)
    else:
        rows = []
        for p in PILARES:
            path = ROOT / "respuestas" / f"{p}.jsonl"
            if path.exists():
                rows += leer_jsonl(path)
    return sorted(rows, key=lambda r: r["question_id"])


def cargar_manifiestos():
    """{pilar: {"meta": dict, "sources": [..]}}"""
    out = {}
    if layout_nuevo():
        for d in sorted(glob.glob(str(ROOT / "kb/pilares/*"))):
            p = os.path.basename(d)[:3]
            meta_p, src_p = Path(d) / "pilar.json", Path(d) / "fuentes.jsonl"
            if meta_p.exists() and src_p.exists():
                out[p] = {"meta": json.loads(meta_p.read_text(encoding="utf-8")), "sources": leer_jsonl(src_p)}
    else:
        for p in PILARES:
            path = ROOT / "fuentes" / f"{p}.json"
            if path.exists():
                m = json.loads(path.read_text(encoding="utf-8"))
                out[p] = {"meta": {k: v for k, v in m.items() if k != "sources"}, "sources": m["sources"]}
    return out


def ruta_grafo(nombre):
    for p in (f"kb/grafo/{nombre}", nombre):
        if (ROOT / p).exists():
            return ROOT / p
    return None


def huellas(R):
    contenido = [[r["question_id"], r["question_text"], r["short_answer"],
                  [[f["claim_id"], f["claim"],
                    [[e.get("source_id"), e.get("source_title"), orig(e, "original_url"), e.get("locator"),
                      e.get("excerpt_short")] for e in f.get("evidence", [])]] for f in r.get("findings", [])]]
                 for r in R]
    estructura = [[r["question_id"]] + [r.get(k) for k in (
        "operational_model", "entities", "relations", "comparisons", "contradictions",
        "metrics_and_denominators", "bridge_implications", "next_question_ids")] for r in R]
    epistemico = [[f["claim_id"], orig(f, "epistemic_status"), orig(f, "confidence")]
                  for r in R for f in r.get("findings", [])]
    tiempos = [[r["question_id"], orig(r, "snapshot_at")] for r in R]
    return {"H_CONTENIDO": sha16(contenido), "H_ESTRUCTURA": sha16(estructura),
            "H_EPISTEMICO": sha16(epistemico), "H_TIEMPOS": sha16(tiempos)}


def archivos_texto(excluir=()):
    exts = {".md", ".json", ".jsonl", ".csv", ".py", ".txt", ".yaml", ".yml"}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        partes = [] if rel == "." else rel.split(os.sep)
        if partes and (partes[0] in (".git", "staging") or any(rel == e or rel.startswith(e + os.sep) for e in excluir)):
            dirnames[:] = []
            continue
        for fn in filenames:
            relf = os.path.normpath(os.path.join(rel, fn))
            if any(relf == e or relf.startswith(e + os.sep) for e in excluir):
                continue
            if os.path.splitext(fn)[1] in exts:
                try:
                    yield relf, (ROOT / relf).read_text(encoding="utf-8")
                except (UnicodeDecodeError, OSError):
                    continue


def regla_verificacion(f, S):
    ev = f.get("evidence", [])
    if any(LOCALIZADOR_SINTETICO in (e.get("locator") or "") for e in ev):
        return "cita_sintetica"
    if ev and all(S.get(e.get("source_id"), {}).get("is_internal_synthesis") for e in ev):
        return "solo_sintesis_interna"
    return "no_verificada"


def copia_temporal():
    tmp = Path(tempfile.mkdtemp(prefix="bridge_comprobar_"))
    destino = tmp / "repo"
    shutil.copytree(ROOT, destino, symlinks=True, ignore=shutil.ignore_patterns(".git", "staging", "__pycache__"))
    return tmp, destino


def huella_arbol(base, patrones):
    out = {}
    for pat in patrones:
        for f in glob.glob(str(base / pat), recursive=True):
            if os.path.isfile(f):
                out[os.path.relpath(f, base)] = sha_archivo(f, 64)
    return out


def ejecutar(script, cwd, timeout=600):
    try:
        r = subprocess.run([sys.executable, script], cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode
    except subprocess.TimeoutExpired:
        return -999


# --- compuertas -----------------------------------------------------------------------------
def gate_prep(rep, ctx):
    rama = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    rep.control(rama == RAMA, f"rama actual = {RAMA}", rama)
    tag_ok = git("rev-parse", "-q", "--verify", f"refs/tags/{TAG}").returncode == 0
    rep.control(tag_ok, f"existe el tag {TAG}")
    if tag_ok:
        rows = []
        for p in PILARES:
            r = git("show", f"{TAG}:respuestas/{p}.jsonl")
            rows += [json.loads(l) for l in r.stdout.splitlines() if l.strip()]
        rows.sort(key=lambda r: r["question_id"])
        h = huellas(rows)
        rep.control(all(h[k] == BASE[k] for k in h), "el tag apunta a la línea base auditada (huellas)", h)
        rep.control(git("diff", "--quiet", TAG, "--", "auditoria/").returncode == 0,
                    "auditoria/ sin cambios respecto del tag")
        rep.control(git("cat-file", "-e", f"{TAG}:auditoria/PLAN_MIGRACION_ANTIGRAVITY.md").returncode == 0,
                    "el plan está incluido en el tag")
    rep.control(git("status", "--porcelain", "--", "auditoria/").stdout.strip() == "",
                "auditoria/ sin archivos nuevos ni modificados")
    for path, esperado in SHA_DOCS_AUDITORIA.items():
        rep.control((ROOT / path).exists() and sha_archivo(ROOT / path) == esperado, f"integridad de {path}")
    est = ROOT / "migracion" / "estado.json"
    try:
        e = json.loads(est.read_text(encoding="utf-8"))
        ok = isinstance(e, dict) and {"fase_actual", "iteracion", "tareas"} <= set(e)
    except (OSError, json.JSONDecodeError):
        ok = False
    rep.control(ok, "migracion/estado.json válido con fase_actual, iteracion, tareas")


def gate_f0(rep, ctx):
    R, M, banco, titulos = ctx["R"], ctx["M"], ctx["banco"], ctx["titulos"]
    rep.control(len(R) == 864 and {r["question_id"] for r in R} == set(banco), "864 registros con los IDs del banco")
    rep.control(all(r["question_text"] == banco[r["question_id"]]["question_text"] for r in R if r["question_id"] in banco),
                "question_text idéntico al mandato")
    h = huellas(R)
    for k, v in h.items():
        rep.control(v == BASE[k], f"{k} invariante", v)
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    prohibidas = [s for s in ("578", "1.632", "1632", "559", "100% PASS", "100.0% PASS") if s in readme]
    rep.control(bool(readme) and not prohibidas, "README sin cifras obsoletas ni «100% PASS»", prohibidas)
    hits = [f for f, t in archivos_texto(excluir=("auditoria", "scripts", "BITACORA.md", "gobernanza/bitacora"))
            if UUID_ERRONEO_P01 in t]
    rep.control(not hits, "sin el UUID erróneo de P01 fuera de la bitácora", hits)
    for p in PILARES:
        m = M.get(p)
        ok = m is not None and m["meta"].get("pilar_nombre") == titulos[p] and m["meta"].get("total_sources") == len(m["sources"])
        rep.control(ok, f"manifiesto {p}: pilar_nombre del mandato y total_sources = nº de fuentes")
    t = next((r for r in R if r["question_id"] == "T01-F06"), None)
    ok = t is not None and t["findings"] and all(f["epistemic_status"] == "hipotesis_diseno" for f in t["findings"]) \
        and str(t.get("nota_auditoria", "")).startswith("Reclasificado en la auditoría del 2026-10-02")
    rep.control(ok, "T01-F06 reclasificado a hipotesis_diseno con nota_auditoria")
    for nombre in ("entidades.jsonl", "relaciones.jsonl"):
        p = ruta_grafo(nombre)
        rep.control(p is not None and "0.932" not in p.read_text(encoding="utf-8"), f"{nombre} sin «0.932»")


def gate_f1(rep, ctx):
    R, M = ctx["R"], ctx["M"]
    S = {s["source_id"]: s for m in M.values() for s in m["sources"]}
    finds = [(r, f) for r in R for f in r.get("findings", [])]
    evs = [(r, f, e) for r, f in finds for e in f.get("evidence", [])]
    # epistemic_status
    epi = collections.Counter(f["epistemic_status"] for _, f in finds)
    rep.control(set(epi) <= EPI_CANON, "epistemic_status solo con valores canónicos", dict(epi))
    rep.control(dict(epi) == EPI_ESPERADO, "conteo epistémico esperado", dict(epi))
    malos = [f["claim_id"] for r, f in finds if "epistemic_status_original" in f and r["question_id"] != "T01-F06"
             and EPI_MAPA.get(f["epistemic_status_original"]) != f["epistemic_status"]]
    rep.control(not malos, "epistemic_status_original coherente con la tabla de equivalencias", malos[:5])
    # confidence
    conf = collections.Counter(f["confidence"] for _, f in finds)
    rep.control(dict(conf) == CONF_ESPERADO, "confidence normalizada (alta/media/baja) y conteo esperado", dict(conf))
    rep.control(all(isinstance(f["confidence_original"], (int, float)) for _, f in finds if "confidence_original" in f)
                and sum(1 for _, f in finds if "confidence_original" in f) == 332,
                "confidence_original numérica en los 332 casos convertidos")
    # manifiestos
    ts = collections.Counter(s["text_status"] for s in S.values())
    rep.control(dict(ts) == TS_ESPERADO, "text_status de manifiestos normalizado", dict(ts))
    malos = [s["source_id"] for s in S.values() if "text_status_original" in s and TS_MAPA.get(s["text_status_original"]) != s["text_status"]]
    rep.control(not malos, "text_status_original coherente con la tabla", malos[:5])
    malos = [s["source_id"] for s in S.values() if not (s.get("original_url") is None or isinstance(s.get("original_url"), str))]
    rep.control(not malos, "original_url de manifiestos es texto o null", len(malos))
    crudos = [s for s in S.values() if "metadata_notebooklm_crudo" in s]
    rep.control(len(crudos) == 126 and all(s.get("original_url") == url_de(s["metadata_notebooklm_crudo"]) for s in crudos),
                "126 metadatos crudos conservados y URL extraída de [7][0]")
    # evidencias
    rep.control(all(e.get("source_id") in S for _, _, e in evs), "toda evidencia cita una fuente del manifiesto")
    tse = collections.Counter(e.get("text_status") for _, _, e in evs)
    rep.control(dict(tse) == TS_EVID_ESPERADO, "text_status de evidencias = el de su fuente", dict(tse))
    rep.control(all(e.get("text_status") == S.get(e.get("source_id"), {}).get("text_status") for _, _, e in evs),
                "evidencia y fuente con el mismo text_status")
    cs = [e for _, _, e in evs if e.get("cita_sintetica") is True]
    rep.control(len(cs) == 439 and all(isinstance(e.get("cita_sintetica"), bool) for _, _, e in evs)
                and all(e["cita_sintetica"] == (LOCALIZADOR_SINTETICO in (e.get("locator") or "")) for _, _, e in evs),
                "cita_sintetica booleana y = 439")
    fi = [e for _, _, e in evs if e.get("fuente_es_sintesis_interna") is True]
    rep.control(len(fi) == 1057 and all(e.get("fuente_es_sintesis_interna") == bool(S.get(e.get("source_id"), {}).get("is_internal_synthesis")) for _, _, e in evs),
                "fuente_es_sintesis_interna coherente y = 1057")
    rep.control(all(e.get("retrieved_at") is None and "retrieved_at_original" in e for _, _, e in evs),
                "retrieved_at = null con retrieved_at_original")
    # verificación
    est = collections.Counter()
    malos = []
    for r, f in finds:
        v = f.get("verificacion")
        if not isinstance(v, dict) or set(v) < VERIF_LLAVES or v.get("estado") not in VERIF_ESTADOS:
            malos.append(f["claim_id"])
            continue
        est[v["estado"]] += 1
        regla = regla_verificacion(f, S)
        if regla in ("cita_sintetica", "solo_sintesis_interna") and v["estado"] != regla:
            malos.append(f["claim_id"])
        if regla == "no_verificada" and v["estado"] in ("cita_sintetica", "solo_sintesis_interna"):
            malos.append(f["claim_id"])
        if v["estado"] in VERIF_PILOTO and f["claim_id"] not in MUESTRA_PILOTO:
            malos.append(f["claim_id"])
        if not isinstance(v.get("motivos"), list) or not set(v["motivos"]) <= MOTIVOS:
            malos.append(f["claim_id"])
        if v["estado"] in ("no_verificada", "cita_sintetica", "solo_sintesis_interna") and any(
                v.get(k) is not None for k in ("verificado_por", "fecha", "metodo", "pasaje")):
            malos.append(f["claim_id"])
    rep.control(not malos, "verificacion presente y coherente con la regla en cada hallazgo", malos[:5])
    rep.control(est["cita_sintetica"] == 439 and est["solo_sintesis_interna"] == 303
                and sum(est[k] for k in ("no_verificada", "verificada", "refutada", "no_verificable")) == 576,
                "estados de verificación: 439 / 303 / 576", dict(est))
    # tiempos
    rep.control(all(r.get("snapshot_at") is None and "snapshot_at_original" in r and str(r.get("snapshot_nota", "")).strip() for r in R),
                "snapshot_at = null con snapshot_at_original y snapshot_nota")
    # quality
    malos = []
    for r in R:
        q, fs = r.get("quality") or {}, r.get("findings", [])
        estados = [f.get("verificacion", {}).get("estado") for f in fs]
        hr = (r.get("answer_status") == "parcial"
              or any(x in ("cita_sintetica", "solo_sintesis_interna", "refutada", "no_verificable") for x in estados)
              or any(e.get("text_status") != "texto_sustantivo" for f in fs for e in f.get("evidence", [])))
        ok = ("quality_original" in r and q.get("original_citations_resolved") == (bool(fs) and all(x == "verificada" for x in estados))
              and q.get("correction_precedence_checked") is None and q.get("duplicate_sources_counted_once") is None
              and q.get("human_review_needed") == hr)
        if not ok:
            malos.append(r["question_id"])
    rep.control(not malos, "quality recalculada según la regla (quality_original conservado)", malos[:5])
    rep.control(all(r.get("answer_status") in ANSWER_STATUS for r in R), "answer_status dentro del enum del mandato")
    # herramientas
    higiene_herramientas(rep, ctx)
    idempotencia(rep, "herramientas/normalizar.py",
                 ["respuestas/*.jsonl", "fuentes/*.json", "kb/pilares/**/*.json", "kb/pilares/**/*.jsonl"])


def higiene_herramientas(rep, ctx):
    hdir = ROOT / "herramientas"
    archivos = sorted(glob.glob(str(hdir / "*.py")))
    rep.control(bool(archivos) and (hdir / "normalizar.py").exists() and (hdir / "kb.py").exists(),
                "existen herramientas/kb.py y herramientas/normalizar.py")
    frag = set()
    for r in ctx["R"]:
        if r.get("short_answer") and len(r["short_answer"]) >= 80:
            frag.add(r["short_answer"][20:80])
        for f in r.get("findings", []):
            if len(f["claim"]) >= 80:
                frag.add(f["claim"][20:80])
    malos = []
    for a in archivos:
        t = Path(a).read_text(encoding="utf-8")
        if len(t.encode("utf-8")) > 60000 or "/Users/" in t or ".gemini" in t or any(x in t for x in frag):
            malos.append(os.path.basename(a))
    rep.control(not malos, "herramientas sin contenido incrustado, sin rutas externas, ≤ 60 KB c/u", malos)


def idempotencia(rep, script, patrones):
    if not (ROOT / script).exists():
        rep.control(False, f"{script} es idempotente", "no existe")
        return
    tmp, dest = copia_temporal()
    try:
        antes = huella_arbol(dest, patrones)
        rc = ejecutar(script, dest)
        despues = huella_arbol(dest, patrones)
        difs = [k for k in set(antes) | set(despues) if antes.get(k) != despues.get(k)]
        rep.control(rc == 0 and not difs, f"{script} se ejecuta sin error y no cambia nada (idempotente)",
                    f"rc={rc}, cambiados={difs[:5]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def gate_f2(rep, ctx):
    R, M, banco, titulos = ctx["R"], ctx["M"], ctx["banco"], ctx["titulos"]
    rep.control(layout_nuevo(), "existe kb/pilares/")
    mp = ROOT / "kb/canon/mandato.md"
    rep.control(mp.exists() and sha_archivo(mp) == BASE["SHA_MANDATO"], "kb/canon/mandato.md idéntico al mandato original")
    bp = ROOT / "kb/canon/banco_preguntas.jsonl"
    ok = False
    if bp.exists():
        filas = {x["question_id"]: x for x in leer_jsonl(bp)}
        ok = len(filas) == 864 and all(
            filas.get(q, {}).get(k) == v[k] for q, v in banco.items()
            for k in ("pilar", "eje", "subeje", "eje_n", "tipo", "question_text"))
    rep.control(ok, "kb/canon/banco_preguntas.jsonl = banco del mandato (864)")
    malos = []
    for r in R:
        q = r["question_id"]
        b = banco.get(q)
        esperado = f"kb/pilares/{pilar_dir(b['pilar'], titulos)}/ejes/{b['eje_dir']}/{q}.json" if b else None
        if r.get("__ruta") != esperado or any(r.get(k) != b[k] for k in ("pilar", "eje", "subeje", "eje_n", "tipo")):
            malos.append(q)
    rep.control(len(R) == 864 and not malos, "864 archivos de pregunta en la ruta y con los campos de ubicación correctos", malos[:5])
    extra = [f for f in glob.glob(str(ROOT / "kb/pilares/*/ejes/*/*"))
             if not (re.match(r"^(P\d\d|T01)-[FCX]\d\d\.json$", os.path.basename(f)) or os.path.basename(f) == "EJE.md")]
    rep.control(not extra, "carpetas de eje solo con preguntas y EJE.md", [os.path.relpath(x, ROOT) for x in extra[:5]])
    ok = len(M) == 12 and all((ROOT / "kb/pilares" / pilar_dir(p, titulos) / "pilar.json").exists() for p in PILARES)
    rep.control(ok, "pilar.json y fuentes.jsonl en las 12 carpetas de pilar")
    ids = sorted(s["source_id"] for m in M.values() for s in m["sources"])
    rep.control(hashlib.sha256("\n".join(ids).encode()).hexdigest()[:16] == BASE["H_FUENTES"] and len(ids) == 551,
                "las 551 fuentes conservan sus source_id")
    presentes = [x for x in LEGADO_AUSENTE_F2 if (ROOT / x).exists()]
    rep.control(not presentes, "rutas heredadas retiradas del árbol", presentes)
    requeridos = ["kb/grafo/entidades.jsonl", "kb/grafo/relaciones.jsonl", "kb/grafo/contradicciones.jsonl",
                  "gobernanza/cierre/REGISTRO_DE_CIERRE.md", "gobernanza/cierre/ejecucion.json",
                  "gobernanza/cierre/matriz_cobertura.csv", "gobernanza/auditorias/2026-10-01-auditoria-preliminar.md",
                  "kb/transversal/SINTESIS_LEGADO.md"] + [f"kb/pilares/{pilar_dir(p, titulos)}/SINTESIS_LEGADO.md" for p in PILARES]
    faltan = [x for x in requeridos if not (ROOT / x).exists()]
    rep.control(not faltan, "archivos reubicados presentes", faltan[:5])
    rep.control(git("cat-file", "-e", f"{TAG}:scripts/append_t01_x17_x24.py").returncode == 0,
                "los scripts históricos siguen recuperables desde el tag")
    raiz = {x for x in os.listdir(ROOT)} - RAIZ_PERMITIDA
    rep.control(not raiz, "raíz del repositorio solo con entradas permitidas", sorted(raiz))
    # bitácora
    legado = git("show", f"{TAG}:BITACORA.md").stdout
    titulos_leg = [l.lstrip("#").strip() for l in legado.splitlines() if l.startswith("## [")]
    archivos_b = glob.glob(str(ROOT / "gobernanza/bitacora/*.md"))
    nombres_ok = all(re.match(r"^\d{4}-\d{2}-\d{2}-\d{2}-[a-z0-9-]+\.md$", os.path.basename(f)) for f in archivos_b)
    encabezados = set()
    for f in archivos_b:
        for l in Path(f).read_text(encoding="utf-8").splitlines():
            if l.startswith("#"):
                encabezados.add(l.lstrip("#").strip())
    faltan = [t for t in titulos_leg if t not in encabezados]
    rep.control(len(titulos_leg) >= 17 and nombres_ok and not faltan,
                "bitácora dividida: un archivo por sesión con nombre AAAA-MM-DD-NN-slug.md y todas las entradas", faltan[:3])
    # enlaces
    con_file = [f for f, t in archivos_texto(excluir=("auditoria", "kb/canon", "herramientas")) if re.search(r"(\]\(|<|\"|')file:///", t)]
    rep.control(not con_file, "sin enlaces file:/// fuera de auditoria/", con_file[:5])
    rotos = []
    for f, t in archivos_texto(excluir=("auditoria", "kb/canon")):
        if not f.endswith(".md"):
            continue
        for destino in re.findall(r"\]\(([^)\s]+)\)", t):
            if re.match(r"^(https?:|mailto:|#)", destino):
                continue
            p = destino.split("#")[0]
            if p and not (ROOT / os.path.dirname(f) / p).exists():
                rotos.append(f"{f} → {destino}")
    rep.control(not rotos, "todos los enlaces relativos de Markdown resuelven", rotos[:5])
    gi = (ROOT / ".gitignore").read_text(encoding="utf-8") if (ROOT / ".gitignore").exists() else ""
    rep.control("staging/" in gi, ".gitignore excluye staging/")


def gate_f3(rep, ctx):
    R, M, titulos, banco = ctx["R"], ctx["M"], ctx["titulos"], ctx["banco"]
    faltan = [h for h in HERRAMIENTAS if not (ROOT / "herramientas" / h).exists()]
    rep.control(not faltan, "herramientas completas", faltan)
    higiene_herramientas(rep, ctx)
    ag = ROOT / "AGENTS.md"
    t = ag.read_text(encoding="utf-8") if ag.exists() else ""
    rep.control(ag.exists() and not ag.is_symlink() and len(t) <= 8000
                and all(x in t for x in ("type(err).__name__", "staging/", "verificada", "kb/CATALOGO.json")),
                "AGENTS.md ≤ 8000 caracteres con reglas heredadas, staging, verificación y catálogo")
    for alias in ("CLAUDE.md", "GEMINI.md", ".agents/AGENTS.md"):
        p = ROOT / alias
        rep.control(p.is_symlink() and os.path.realpath(p) == os.path.realpath(ag), f"{alias} es enlace simbólico a AGENTS.md")
    finds = [(r, f) for r in R for f in r.get("findings", [])]
    cat_p = ROOT / "kb/CATALOGO.json"
    ok = False
    if cat_p.exists():
        txt = cat_p.read_text(encoding="utf-8")
        cat = json.loads(txt)
        tot = cat.get("totales", {})
        ok = (len(txt) <= 10000 and not re.search(r"\d{4}-\d{2}-\d{2}T\d", txt) and "huella_datos" in cat
              and tot.get("preguntas") == 864 and tot.get("hallazgos") == len(finds) and tot.get("fuentes") == 551
              and tot.get("evidencias") == sum(len(f.get("evidence", [])) for _, f in finds)
              and len(cat.get("pilares", [])) == 12
              and all((ROOT / x.get("ruta", "§")).exists() for x in cat.get("pilares", [])))
    rep.control(ok, "kb/CATALOGO.json ≤ 10000 caracteres, sin marcas de tiempo, totales correctos y rutas válidas")
    ejes = collections.defaultdict(list)
    for q, b in banco.items():
        ejes[(b["pilar"], b["eje_dir"])].append(q)
    malos = []
    for p in PILARES:
        tp = ROOT / "kb/pilares" / pilar_dir(p, titulos) / "TARJETA.md"
        tt = tp.read_text(encoding="utf-8") if tp.exists() else ""
        if not (tt.startswith(MARCA_GENERADO) and len(tt) <= 10500 and all(s in tt for s in SECCIONES_TARJETA)
                and all(f"ejes/{ed}/EJE.md" in tt for (pp, ed) in ejes if pp == p)):
            malos.append(p)
    rep.control(not malos, "12 TARJETA.md generadas, ≤ 10500 caracteres, con secciones y enlaces a sus ejes", malos)
    malos = []
    for (p, ed), qs in ejes.items():
        ep = ROOT / "kb/pilares" / pilar_dir(p, titulos) / "ejes" / ed / "EJE.md"
        et = ep.read_text(encoding="utf-8") if ep.exists() else ""
        if not (et.startswith(MARCA_GENERADO) and len(et) <= 7000 and all(q in et for q in qs)):
            malos.append(f"{p}/{ed}")
    rep.control(len(ejes) == 108 and not malos, "108 EJE.md generados, ≤ 7000 caracteres, con todas sus preguntas", malos[:5])
    af = ROOT / "kb/afirmaciones.jsonl"
    ok = False
    if af.exists():
        A = {a["claim_id"]: a for a in leer_jsonl(af)}
        F = {f["claim_id"]: (r, f) for r, f in finds}
        ok = len(A) == len(F) == BASE["hallazgos"] and set(A) == set(F) and all(
            A[c].get("question_id") == r["question_id"] and A[c].get("claim") == f["claim"]
            and A[c].get("epistemic_status") == f["epistemic_status"] and A[c].get("confidence") == f["confidence"]
            and A[c].get("verificacion_estado") == f["verificacion"]["estado"] and (ROOT / A[c].get("ruta", "§")).exists()
            for c, (r, f) in F.items())
    rep.control(ok, "kb/afirmaciones.jsonl = 1318 afirmaciones coherentes con los registros")
    ch = ROOT / "kb/export/chunks.jsonl"
    ok = False
    if ch.exists():
        C = leer_jsonl(ch)
        ok = (len(C) == 864 + BASE["hallazgos"] and len({c.get("chunk_id") for c in C}) == len(C)
              and all(c.get("tipo") in ("respuesta_corta", "afirmacion") and isinstance(c.get("texto"), str)
                      and len(c["texto"]) <= 4000 and isinstance(c.get("metadatos"), dict)
                      and "question_id" in c["metadatos"] and "pilar" in c["metadatos"] for c in C)
              and all("verificacion_estado" in c["metadatos"] for c in C if c["tipo"] == "afirmacion"))
    rep.control(ok, "kb/export/chunks.jsonl = 2182 chunks con metadatos")
    va = ROOT / "kb/transversal/vacios.jsonl"
    rep.control(va.exists() and len(leer_jsonl(va)) == sum(len(r.get("open_gaps", [])) for r in R) == BASE["open_gaps"]
                and all("question_id" in x and "gap" in x for x in leer_jsonl(va)),
                "kb/transversal/vacios.jsonl = 470 vacíos con question_id")
    ip, ifu = ROOT / "kb/indices/preguntas.jsonl", ROOT / "kb/indices/fuentes.jsonl"
    rep.control(ip.exists() and ifu.exists() and len(leer_jsonl(ip)) == 864 and len(leer_jsonl(ifu)) == 551
                and all((ROOT / x.get("ruta", "§")).exists() for x in leer_jsonl(ip)),
                "índices de preguntas (864) y fuentes (551) con rutas válidas")
    vp = ROOT / "kb/esquemas/vocabularios.json"
    ok = False
    if vp.exists():
        v = json.loads(vp.read_text(encoding="utf-8"))
        ok = (set(v.get("epistemic_status", [])) == EPI_CANON and set(v.get("text_status", [])) == TS_CANON
              and set(v.get("verificacion_estado", [])) == VERIF_ESTADOS and set(v.get("answer_status", [])) == ANSWER_STATUS
              and set(v.get("confidence", [])) == {"alta", "media", "baja"} and v.get("modulo"))
    rep.control(ok, "kb/esquemas/vocabularios.json con los vocabularios canónicos")
    faltan = []
    for n in ("respuesta", "fuente", "afirmacion", "entidad", "relacion", "contradiccion"):
        p = ROOT / f"kb/esquemas/{n}.schema.json"
        try:
            if "$schema" not in json.loads(p.read_text(encoding="utf-8")):
                faltan.append(n)
        except (OSError, json.JSONDecodeError):
            faltan.append(n)
    rep.control(not faltan, "6 esquemas JSON con $schema", faltan)
    rd = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    rep.control(rd.startswith(MARCA_GENERADO) and "551" in rd and ("1318" in rd or "1.318" in rd),
                "README generado con cifras actuales")
    # reproducibilidad de vistas
    gen = ["kb/CATALOGO.json", "kb/afirmaciones.jsonl", "kb/export/*.jsonl", "kb/transversal/vacios.jsonl",
           "kb/indices/*.jsonl", "kb/pilares/*/TARJETA.md", "kb/pilares/*/ejes/*/EJE.md", "README.md"]
    tmp, dest = copia_temporal()
    try:
        rc = ejecutar("herramientas/generar_vistas.py", dest)
        a, b = huella_arbol(ROOT, gen), huella_arbol(dest, gen)
        difs = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
        rep.control(rc == 0 and not difs, "las vistas versionadas son exactamente las que genera generar_vistas.py",
                    f"rc={rc}, distintas={difs[:5]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    idempotencia(rep, "herramientas/normalizar.py", ["kb/pilares/**/*.json", "kb/pilares/**/*.jsonl"])
    pruebas_validador(rep, incluir_grafo=False)


def pruebas_validador(rep, incluir_grafo):
    rep.control(ejecutar("herramientas/validar.py", ROOT) == 0, "validar.py aprueba el repositorio actual")
    preguntas = sorted(glob.glob(str(ROOT / "kb/pilares/*/ejes/*/P01-F0*.json")))
    if not preguntas:
        rep.control(False, "mutaciones de prueba", "no hay archivos de pregunta")
        return
    objetivo = os.path.relpath(preguntas[0], ROOT)

    def mut_json(fn):
        def aplicar(dest):
            p = dest / objetivo
            d = json.loads(p.read_text(encoding="utf-8"))
            fn(d)
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        return aplicar

    def m_epi(d): d["findings"][0]["epistemic_status"] = "fact"
    def m_verif(d): d["findings"][0]["verificacion"].update({"estado": "verificada", "pasaje": None})
    def m_fuente(d): d["findings"][0]["evidence"][0]["source_id"] = "fuente-inexistente"
    def m_borrar(dest): (dest / objetivo).unlink()

    def m_grafo(dest):
        p = dest / "kb/grafo/relaciones.jsonl"
        with open(p, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"subject_id": "org:no-existe", "predicate": "x", "object_id": "org:tampoco",
                                 "evidence_claim_ids": [], "indice_legado": None}) + "\n")

    mutaciones = [("epistemic_status no canónico", mut_json(m_epi)), ("archivo de pregunta borrado", m_borrar),
                  ("verificada sin pasaje", mut_json(m_verif)), ("source_id inexistente", mut_json(m_fuente))]
    if incluir_grafo:
        mutaciones.append(("relación colgante", m_grafo))
    for nombre, aplicar in mutaciones:
        tmp, dest = copia_temporal()
        try:
            aplicar(dest)
            rc = ejecutar("herramientas/validar.py", dest)
            rep.control(rc not in (0, -999), f"validar.py rechaza la mutación «{nombre}»", f"rc={rc}")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


def gate_f4(rep, ctx):
    R = ctx["R"]
    claims = {f["claim_id"] for r in R for f in r.get("findings", [])}
    v = json.loads((ROOT / "kb/esquemas/vocabularios.json").read_text(encoding="utf-8")) if (ROOT / "kb/esquemas/vocabularios.json").exists() else {}
    preds = v.get("predicado", [])
    rep.control(set(v.get("tipo_entidad", [])) == TIPOS_ENTIDAD, "tipo_entidad = los 11 tipos del mandato")
    rep.control(5 <= len(preds) <= 40 and all(re.match(r"^[a-z][a-z0-9_]*$", p) for p in preds),
                "vocabulario de predicados cerrado (5–40, snake_case)", len(preds))
    E = leer_jsonl(ROOT / "kb/grafo/entidades.jsonl") if (ROOT / "kb/grafo/entidades.jsonl").exists() else []
    ids = [e.get("entity_id") for e in E]
    eid = set(ids)
    malos = [e.get("entity_id") for e in E if not (
        re.match(r"^[a-z]+:[a-z0-9][a-z0-9-]*$", str(e.get("entity_id"))) and e.get("type") in TIPOS_ENTIDAD
        and str(e.get("canonical_name", "")).strip() and isinstance(e.get("ids_legado"), list)
        and "0.932" not in json.dumps(e, ensure_ascii=False))]
    rep.control(E and len(ids) == len(eid) and not malos, "entidades con ID único prefijado, tipo canónico e ids_legado", malos[:5])
    legado = {json.loads(l)["entity_id"] for l in git("show", f"{TAG}:entidades.jsonl").stdout.splitlines() if l.strip()}
    mp = ROOT / "kb/grafo/mapa_ids.jsonl"
    MP = leer_jsonl(mp) if mp.exists() else []
    cuenta = collections.Counter(x.get("id_legado") for x in MP)
    por_id = {e["entity_id"]: e for e in E}
    malos = [x.get("id_legado") for x in MP if not (
        (x.get("accion") in ("conservado", "fusionado") and x.get("id_nuevo") in por_id
         and x.get("id_legado") in por_id[x["id_nuevo"]].get("ids_legado", []))
        or (x.get("accion") == "eliminado" and x.get("id_nuevo") is None and str(x.get("motivo", "")).strip()))]
    rep.control(len(legado) == BASE["entidades_legado_unicas"] and set(cuenta) == legado and max(cuenta.values(), default=0) == 1
                and not malos, "mapa_ids.jsonl cubre una vez cada uno de los 1515 IDs heredados", malos[:5])
    Rl = leer_jsonl(ROOT / "kb/grafo/relaciones.jsonl") if (ROOT / "kb/grafo/relaciones.jsonl").exists() else []
    Rd = leer_jsonl(ROOT / "kb/grafo/relaciones_descartadas.jsonl") if (ROOT / "kb/grafo/relaciones_descartadas.jsonl").exists() else []
    malos = [i for i, x in enumerate(Rl) if not (
        x.get("subject_id") in eid and x.get("object_id") in eid and x.get("predicate") in preds
        and isinstance(x.get("evidence_claim_ids"), list) and set(x["evidence_claim_ids"]) <= claims)]
    rep.control(Rl and not malos, "relaciones con integridad referencial total y predicados del vocabulario", malos[:5])
    idx = [x.get("indice_legado") for x in Rl + Rd]
    rep.control(sorted(i for i in idx if isinstance(i, int)) == list(range(BASE["relaciones_legado"])) and len(idx) == BASE["relaciones_legado"]
                and all(str(x.get("motivo", "")).strip() for x in Rd),
                "cada una de las 477 relaciones heredadas conservada o descartada con motivo")
    K = leer_jsonl(ROOT / "kb/grafo/contradicciones.jsonl") if (ROOT / "kb/grafo/contradicciones.jsonl").exists() else []
    rep.control(len(K) == BASE["contradicciones"] and all(
        x.get("resolution") in ("resuelta", "abierta") and "resolution_original" in x
        and set(x.get("claim_ids", [])) <= claims and isinstance(x.get("claim_ids_no_encontrados"), list) for x in K),
        "93 contradicciones con resolution canónica y claim_ids existentes")
    pruebas_validador(rep, incluir_grafo=True)


def gate_f5(rep, ctx):
    R, banco, titulos = ctx["R"], ctx["banco"], ctx["titulos"]
    malos = []
    for rol in ROLES:
        p = ROOT / f"enjambre/roles/{rol}.md"
        t = p.read_text(encoding="utf-8") if p.exists() else ""
        if not (t and len(t) <= 6000 and all(s in t for s in SECCIONES_ROL)):
            malos.append(rol)
        try:
            json.loads((ROOT / f"enjambre/contratos/{rol}.schema.json").read_text(encoding="utf-8"))["$schema"]
        except (OSError, json.JSONDecodeError, KeyError):
            malos.append(f"contrato:{rol}")
    rep.control(not malos, "8 tarjetas de rol con sus secciones y 8 contratos JSON", malos)
    faltan = [x for x in ("lectura", "escritura", "verificacion") if not (ROOT / f"enjambre/protocolos/{x}.md").exists()]
    rep.control(not faltan, "protocolos de lectura, escritura y verificación", faltan)
    ok = False
    rp = ROOT / "enjambre/rutas.json"
    if rp.exists():
        rutas = json.loads(rp.read_text(encoding="utf-8"))
        dirs = {f"{b['pilar']}/{b['eje_dir'][:2]}" for b in banco.values()}
        ok = (isinstance(rutas, list) and len(rutas) >= 24
              and all(isinstance(x.get("intencion"), str) and set(x.get("pilares", [])) <= set(PILARES)
                      and x.get("ejes") and set(x["ejes"]) <= dirs and x.get("rol") in ROLES
                      and isinstance(x.get("requiere_verificacion"), bool) for x in rutas)
              and {p for x in rutas for p in x["pilares"]} == set(PILARES))
    rep.control(ok, "enjambre/rutas.json: ≥ 24 rutas válidas que cubren los 12 pilares")
    # piloto
    F = {f["claim_id"]: f for r in R for f in r.get("findings", [])}
    fecha_tag = git("log", "-1", "--format=%cI", TAG).stdout.strip()
    try:
        t0 = datetime.datetime.fromisoformat(fecha_tag)
    except ValueError:
        t0 = None
    ahora = datetime.datetime.now(datetime.timezone.utc)
    malos = []
    for c in MUESTRA_PILOTO:
        v = F.get(c, {}).get("verificacion", {})
        vp = v.get("verificado_por") or {}
        try:
            fecha = datetime.datetime.fromisoformat(str(v.get("fecha")).replace("Z", "+00:00"))
            fecha_ok = fecha.tzinfo is not None and (t0 is None or fecha >= t0) and fecha <= ahora
        except ValueError:
            fecha_ok = False
        ok = (v.get("estado") in VERIF_PILOTO and vp.get("rol") == "verificador_evidencia" and str(vp.get("modelo", "")).strip()
              and vp.get("run_id") == "piloto-001" and fecha_ok and v.get("metodo") == "lectura_url_original")
        if ok and v["estado"] in ("verificada", "refutada"):
            pas = v.get("pasaje")
            sha = str(v.get("sha256_texto", ""))
            cache = ROOT / "staging/piloto-001/cache" / f"{sha}.txt"
            ok = (isinstance(pas, str) and 0 < len(pas) <= 600 and str(v.get("url_consultada", "")).startswith("http")
                  and re.match(r"^[0-9a-f]{64}$", sha) and cache.exists()
                  and hashlib.sha256(cache.read_bytes()).hexdigest() == sha
                  and norm(pas) in norm(cache.read_text(encoding="utf-8", errors="replace")))
        if ok and v["estado"] == "no_verificable":
            ok = v.get("pasaje") is None and bool(v.get("motivos"))
        if not ok:
            malos.append(c)
    rep.control(not malos, "59 afirmaciones de la muestra verificadas con pasaje literal comprobable en caché", malos[:8])
    fuera = [c for c, f in F.items() if f.get("verificacion", {}).get("estado") in VERIF_PILOTO and c not in MUESTRA_PILOTO]
    rep.control(not fuera, "ninguna afirmación fuera de la muestra cambió de estado", fuera[:5])
    inf = ROOT / "migracion/piloto-001/INFORME.md"
    rep.control(inf.exists() and all(c in inf.read_text(encoding="utf-8") for c in MUESTRA_PILOTO),
                "migracion/piloto-001/INFORME.md lista las 59 afirmaciones")
    rep.control(bool(glob.glob(str(ROOT / "gobernanza/bitacora/*-migracion-enjambre.md"))),
                "entrada de bitácora de la migración")
    fin = ROOT / "migracion/INFORME_FINAL.md"
    rep.control(fin.exists() and "RESULTADO: OK" in fin.read_text(encoding="utf-8"),
                "migracion/INFORME_FINAL.md con la salida literal del comprobador")
    rep.control(git("status", "--porcelain").stdout.strip() == "", "árbol de trabajo limpio (todo commiteado)")


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip().lower()


GATES = {"PREP": gate_prep, "F0": gate_f0, "F1": gate_f1, "F2": gate_f2, "F3": gate_f3, "F4": gate_f4, "F5": gate_f5}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--hasta", choices=FASES)
    g.add_argument("--fase", choices=FASES)
    g.add_argument("--todo", action="store_true")
    a = ap.parse_args()
    fases = FASES if a.todo else ([a.fase] if a.fase else FASES[:FASES.index(a.hasta) + 1])
    mp = ruta_mandato()
    if mp is None:
        print("[FALLA] no se encuentra el mandato\nRESULTADO: FALLA (1)")
        sys.exit(1)
    banco, titulos = parse_banco(mp.read_text(encoding="utf-8"))
    ctx = {"banco": banco, "titulos": titulos, "R": cargar_respuestas(), "M": cargar_manifiestos()}
    rep = Reporte()
    for f in fases:
        print(f"\n== Compuerta {f} ==")
        try:
            GATES[f](rep, ctx)
        except Exception as err:  # el comprobador nunca debe ocultar un fallo como éxito
            rep.control(False, f"la compuerta {f} se ejecutó completa", type(err).__name__)
    print(f"\nRESULTADO: {'OK' if rep.fallas == 0 else f'FALLA ({rep.fallas})'}")
    sys.exit(0 if rep.fallas == 0 else 1)


if __name__ == "__main__":
    main()
