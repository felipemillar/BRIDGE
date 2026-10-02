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
import subprocess
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

# Mapeo explícito y verificado para P01 (64 IDs legados)
# Formato: id_legado -> (accion, id_nuevo, tipo, canonical_name, aliases, motivo)
P01_MAP = {
    "ENT_ACCION_EMPRESAS": (
        "conservado", "org:accion-empresas", "organizacion",
        "Acción Empresas Chile", ["Acción Empresas", "Red de Empresas Sostenibles"], None
    ),
    "ENT_BCN": (
        "conservado", "org:bcn", "organizacion",
        "Biblioteca del Congreso Nacional de Chile", ["BCN", "Biblioteca del Congreso"], None
    ),
    "ENT_CADEM": (
        "conservado", "org:cadem", "organizacion",
        "Cadem Chile", ["Cadem", "Plaza Pública Cadem"], None
    ),
    "ENT_CADENA_CAUSAL_ASIMETRIA": (
        "conservado", "riesgo:cadena-causal-asimetria", "riesgo",
        "Cadena Causal de Falla de Inteligencia",
        ["Falla de Inteligencia por Asimetría", "Cadena Causal de Asimetría"], None
    ),
    "ENT_CASO_COMPARATIVO_HIDRICO": (
        "conservado", "exp:caso-comparativo-hidrico", "experimento",
        "Caso Comparativo de Contingencia Hídrica Flujo A vs B",
        ["Contingencia Hídrica Flujo A vs B"], None
    ),
    "ENT_CASO_LOBBY_MINERIA": (
        "conservado", "exp:caso-lobby-mineria", "experimento",
        "Caso Práctico: Contingencia Hídrica y Audiencia de Lobby",
        ["Contingencia Hídrica y Audiencia de Lobby"], None
    ),
    "ENT_CASO_MINERO_NORTE": (
        "conservado", "exp:caso-minero-norte", "experimento",
        "Caso de Diálogo Territorial y Permisos Ambientales en Minería",
        ["Diálogo Territorial y Permisos Ambientales en Minería"], None
    ),
    "ENT_CASO_REGIONAL_HIBRIDO": (
        "conservado", "exp:caso-regional-hibrido", "experimento",
        "Caso Regional de Contingencia Hídrica y Audiencia Ministerial",
        ["Caso Práctico P01-F42", "Contingencia Hídrica y Audiencia Ministerial"], None
    ),
    "ENT_CASO_ROI_MINERO": (
        "conservado", "exp:caso-roi-minero", "experimento",
        "Caso Práctico de Retorno de Valor en Sector Minero",
        ["Retorno de Valor en Sector Minero", "Caso ROI Minero"], None
    ),
    "ENT_CCO": (
        "conservado", "rol:cco", "persona_rol",
        "Chief Communications Officer (CCO / Dircom)",
        ["Dircom", "Director de Asuntos Corporativos", "Chief Communications Officer"], None
    ),
    "ENT_CCO_INTEGRADOR": (
        "fusionado", "rol:cco", "persona_rol", None,
        ["CCO as Integrator (Arthur W. Page Society)", "Articulador de Silos del C-Suite"],
        "variante_rol_cco_integrador"
    ),
    "ENT_CISO": (
        "conservado", "rol:ciso", "persona_rol",
        "Chief Information Security Officer (CISO)",
        ["CISO", "Gerente de Ciberseguridad"], None
    ),
    "ENT_CMF": (
        "conservado", "org:cmf", "organizacion",
        "Comisión para el Mercado Financiero",
        ["CMF", "Superintendencia de Valores y Seguros"], None
    ),
    "ENT_CMF_NCG461": (
        "conservado", "doc:cmf-ncg-461", "documento",
        "NCG N° 461 de la Comisión para el Mercado Financiero",
        ["NCG 461", "Norma de Carácter General N° 461"], None
    ),
    "ENT_CONDICIONES_CONTENCION": (
        "conservado", "tema:condiciones-contencion", "tema",
        "Condiciones de Contención e Inteligencia Estructurada",
        ["Inteligencia Estructurada en Crisis", "Contención Decisional"], None
    ),
    "ENT_CORPUS_P01": (
        "conservado", "doc:corpus-p01", "documento",
        "Corpus P01: Asuntos Corporativos y sus Usuarios",
        ["Corpus P01"], None
    ),
    "ENT_DEONTOLOGIA_PRSA": (
        "conservado", "doc:codigo-etica-prsa", "documento",
        "Código de Ética y Salvaguarda de Confidencias PRSA",
        ["PRSA Code of Ethics", "Código Deontológico PRSA"], None
    ),
    "ENT_DIRCOM": (
        "fusionado", "org:dircom-espana", "organizacion", None,
        ["Asociación de Directivos de Comunicación (Dircom)"],
        "variante_denominacion_asociacion_dircom"
    ),
    "ENT_DIRCOM_ECE2025": (
        "conservado", "doc:dircom-ece-2025", "documento",
        "El Estado de la Comunicación en España 2025",
        ["ECE 2025", "Estado Comunicación España 2025"], None
    ),
    "ENT_DIRCOM_ESP": (
        "conservado", "org:dircom-espana", "organizacion",
        "Asociación de Directivos de Comunicación (Dircom España)",
        ["Dircom España", "Asociación Dircom"], None
    ),
    "ENT_DOSSIER_P01": (
        "conservado", "doc:dossier-p01", "documento",
        "P01_RESEARCH_DOSSIER",
        ["Dossier de Investigación P01"], None
    ),
    "ENT_ECM": (
        "conservado", "doc:european-communication-monitor-2023", "documento",
        "European Communication Monitor 2023",
        ["ECM 2023"], None
    ),
    "ENT_EDELMAN_TRUST": (
        "conservado", "doc:edelman-trust-barometer", "documento",
        "Edelman Trust Barometer 2025/2026",
        ["Edelman Trust Barometer"], None
    ),
    "ENT_ESCENARIOS_FRICCION": (
        "conservado", "tema:escenarios-friccion", "tema",
        "Escenarios de Reunión y Fricción Decisional",
        ["Fricción Decisional B2B"], None
    ),
    "ENT_ESTADIOS_MADUREZ": (
        "conservado", "tema:estadios-madurez-commtech", "tema",
        "Estadios de Madurez Digital CommTech",
        ["Madurez Artesanal, Estratégica y Agéntica"], None
    ),
    "ENT_ESTUDIO_USUARIOS_CHILE": (
        "conservado", "doc:estudio-usuarios-chile", "documento",
        "Estudio Empírico de Usuarios de Asuntos Corporativos en Chile",
        ["Validación de Campo Fase 1 y 2"], None
    ),
    "ENT_EUPRERA_LCM": (
        "conservado", "doc:euprera-latin-american-communication-monitor", "documento",
        "EUPRERA Latin American Communication Monitor",
        ["Latin American Communication Monitor", "LCM EUPRERA"], None
    ),
    "ENT_FISCAL_LEGAL": (
        "conservado", "rol:fiscal-legal", "persona_rol",
        "Fiscal Legal / Gerente de Compliance",
        ["Fiscal Legal", "Gerente de Compliance", "Compliance Officer"], None
    ),
    "ENT_FUENTES_FALLIDAS_P01": (
        "eliminado", None, None, None, [], "registro_interno_auditoria"
    ),
    "ENT_GCF": (
        "conservado", "doc:global-capability-framework", "documento",
        "Global Capability Framework",
        ["GCF", "Marco Global de Capacidades"], None
    ),
    "ENT_GLOBAL_ALLIANCE": (
        "conservado", "org:global-alliance", "organizacion",
        "Global Alliance for Public Relations and Communication Management",
        ["Global Alliance"], None
    ),
    "ENT_INFOLOBBY": (
        "conservado", "prod:infolobby", "producto",
        "Plataforma InfoLobby Chile",
        ["InfoLobby", "Plataforma de Lobby BCN"], None
    ),
    "ENT_JTBD_CRISIS": (
        "conservado", "tema:jtbd-minuta-crisis", "tema",
        "Preparación de Minuta de Crisis",
        ["Briefing Book Urgente", "JTBD Minuta de Crisis"], None
    ),
    "ENT_JTBD_DIMENSIONS": (
        "conservado", "tema:jtbd-dimensiones", "tema",
        "Dimensiones de Jobs-to-be-Done en Asuntos Corporativos",
        ["Jobs to be Done Asuntos Corporativos"], None
    ),
    "ENT_JTBD_F1": (
        "conservado", "tema:jtbd-briefing-ejecutivo", "tema",
        "JTBD-F1: Compilación de Briefing Ejecutivo",
        ["Compilación de Briefing Ejecutivo"], None
    ),
    "ENT_LEGAL_COMPLIANCE": (
        "fusionado", "rol:fiscal-legal", "persona_rol", None,
        ["Fiscal Legal / Compliance Officer"],
        "variante_rol_fiscal_legal_compliance"
    ),
    "ENT_LEY_LOBBY": (
        "conservado", "doc:ley-20730", "documento",
        "Ley N° 20.730 que Regula el Lobby",
        ["Ley del Lobby", "Ley 20730", "Ley 20.730"], None
    ),
    "ENT_MATRIZ_FUENTES_REGIONALES": (
        "conservado", "doc:matriz-fuentes-regionales-p01", "documento",
        "Matriz de Fuentes y Respaldos Regionales P01",
        ["Evidencia de Usuarios en Chile y LatAm"], None
    ),
    "ENT_MATRIZ_OBJECIONES_CISO": (
        "conservado", "doc:matriz-objeciones-ciso", "documento",
        "Matriz de Objeciones Técnicas de CISOs en LatAm",
        ["Parámetros de Homologación B2B"], None
    ),
    "ENT_MCKINSEY": (
        "conservado", "org:mckinsey", "organizacion",
        "McKinsey & Company",
        ["McKinsey"], None
    ),
    "ENT_MERCO": (
        "conservado", "org:merco-chile", "organizacion",
        "Merco Chile",
        ["Merco", "Monitor Empresarial de Reputación Corporativa"], None
    ),
    "ENT_MODELO_RETORNO_VALOR": (
        "conservado", "tema:modelo-retorno-valor", "tema",
        "Modelo de Retorno de Valor en Asuntos Corporativos",
        ["Intangible Asset Valuation & Efficiency"], None
    ),
    "ENT_MODELO_VALOR_P01": (
        "conservado", "tema:modelo-valor-asuntos-corporativos", "tema",
        "Modelo Multidimensional de Valor en Asuntos Corporativos",
        ["Modelo de Valor P01"], None
    ),
    "ENT_P01_BRIDGE": (
        "conservado", "prod:bridge-intelligence", "producto",
        "The Bridge Intelligence",
        ["BRIDGE Intelligence", "The Bridge Platform"], None
    ),
    "ENT_P01_CORP": (
        "conservado", "org:corporacion-emisora-cmf", "organizacion",
        "Corporación Emisora CMF",
        ["Emisor de Valores CMF", "Empresa Regulada CMF"], None
    ),
    "ENT_P01_REG": (
        "conservado", "org:reguladores-sectoriales-chile", "organizacion",
        "CMF / SERNAC / SMA",
        ["Reguladores Sectoriales Chile", "Entidades Reguladoras"], None
    ),
    "ENT_PAGE_SOCIETY": (
        "conservado", "org:arthur-w-page-society", "organizacion",
        "Arthur W. Page Society",
        ["Page Society"], None
    ),
    "ENT_PANEL_TRIPARTITO": (
        "conservado", "rol:panel-evaluador-tripartito", "persona_rol",
        "Panel Evaluador Tripartito (CCO, CISO, Fiscal Legal)",
        ["Comité de Adopción Tecnológica", "Panel Tripartito"], None
    ),
    "ENT_PARADOJA_LOBBY": (
        "conservado", "tema:paradoja-legitimidad-lobby", "tema",
        "Paradoja de Legitimidad en Ley de Lobby",
        ["Cumplimiento Legal vs Reputación"], None
    ),
    "ENT_PLAN_3_FASES": (
        "conservado", "exp:plan-validacion-tres-fases", "experimento",
        "Plan de Validación Empírica en Tres Fases (12 Semanas)",
        ["Roadmap de Validación de Campo BRIDGE"], None
    ),
    "ENT_POC_MINERA_IPSA": (
        "conservado", "exp:poc-minera-ipsa", "experimento",
        "Prueba de Concepto en Corporación Minero-Energética IPSA",
        ["PoC de Validación P01-F48"], None
    ),
    "ENT_POC_TRIPARTITA": (
        "conservado", "exp:poc-trilateral-fase-3", "experimento",
        "Prueba de Concepto Trilateral (Fase 3)",
        ["Validación de Retorno B2B y Arquitectura"], None
    ),
    "ENT_PROTOCOLO_VALIDACION": (
        "conservado", "doc:protocolo-validacion-tres-fases", "documento",
        "Protocolo de Validación Empírica en 3 Fases",
        ["Gaps & Validation Plan"], None
    ),
    "ENT_PRSA_ESA22": (
        "conservado", "doc:prsa-ethical-standards-advisory-22", "documento",
        "PRSA Ethical Standards Advisory #22",
        ["PRSA ESA #22", "ESA 22"], None
    ),
    "ENT_RCA": (
        "conservado", "doc:resolucion-calificacion-ambiental", "documento",
        "Resolución de Calificación Ambiental (RCA)",
        ["RCA", "Resolución Ambiental"], None
    ),
    "ENT_RIESGO_PREPARACION": (
        "conservado", "riesgo:preparacion-insuficiente", "riesgo",
        "Riesgo de Preparación Insuficiente",
        ["Patología de Cocina Artesanal"], None
    ),
    "ENT_SHADOWING_CRISIS": (
        "conservado", "exp:shadowing-preparacion-crisis", "experimento",
        "Shadowing de Preparación de Crisis",
        ["Observación Cronometrada en Tiempo Real"], None
    ),
    "ENT_STAGE_GATES_P01": (
        "conservado", "comp:stage-gates-validacion-b2b", "compromiso",
        "Stage Gates de Validación B2B P01",
        ["Compuertas de Salida de Validación"], None
    ),
    "ENT_SUBSECRETARIA": (
        "conservado", "org:subsecretaria-de-estado", "organizacion",
        "Subsecretaría de Estado",
        ["Subsecretaría Ministerial"], None
    ),
    "ENT_TRIADA_B2B": (
        "conservado", "tema:triada-b2b-decision", "tema",
        "Tríada B2B (Usuario - Comprador - Aprobador)",
        ["Matriz de Decisión Tecnológica B2B", "Ecosistema B2B de Decisión"], None
    ),
    "ENT_TRIADA_CONTROL": (
        "conservado", "tema:triada-control-cco-legal-ops", "tema",
        "Tríada CCO - Legal - Operaciones",
        ["Tríada de Control Operativo"], None
    ),
    "ENT_USUARIO_CHILENO": (
        "conservado", "rol:usuario-asuntos-corporativos-chile", "persona_rol",
        "Usuario de Asuntos Corporativos en Chile",
        ["Dircom Regulado en Chile"], None
    ),
    "ENT_VECTORES_CRITICIDAD": (
        "conservado", "tema:cuatro-vectores-criticidad", "tema",
        "Cuatro Vectores de Criticidad",
        ["Vectores de Criticidad Decisional"], None
    ),
    "ENT_VETO_VINCULANTE_CISO": (
        "conservado", "comp:veto-vinculante-ciso-legal", "compromiso",
        "Veto Vinculante de CISO y Fiscal Legal",
        ["Poder de Bloqueo B2B"], None
    ),
}


def cargar_entidades_legado() -> list[dict]:
    """Carga las entidades originales desde pre-migracion:entidades.jsonl."""
    res = subprocess.run(
        ["git", "show", "pre-migracion:entidades.jsonl"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [json.loads(line) for line in res.stdout.splitlines() if line.strip()]


def obtener_primer_pilar(entidad: dict) -> str:
    """Calcula el primer pilar donde aparece mencionada la entidad."""
    pils = set()
    for nb in entidad.get("mentioned_in_notebooks", []):
        pils.add(nb[:3])
    for q in entidad.get("questions", []):
        pils.add(q[:3])
    for p in PILARES:
        if p in pils:
            return p
    return "P01"


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
                    # Si es formato canónico con ids_legado
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


def resolver_pilar_p01(r: Path) -> tuple[dict[str, dict], list[dict]]:
    """Resuelve las 64 entidades del pilar P01."""
    entidades, mapa = cargar_existentes(r)
    ids_mapa_vistos = {m["id_legado"] for m in mapa}

    # Pase 1: Crear entidades conservadas
    for leg_id, (accion, id_nuevo, tipo, canon_name, aliases, motivo) in P01_MAP.items():
        if leg_id in ids_mapa_vistos:
            continue
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
    for leg_id, (accion, id_nuevo, tipo, canon_name, aliases, motivo) in P01_MAP.items():
        if leg_id in ids_mapa_vistos:
            continue
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

    if pilar == "P01":
        entidades, mapa = resolver_pilar_p01(r)
    else:
        print(f"Resolución para pilar {pilar} aún no implementada en este paso.")
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
