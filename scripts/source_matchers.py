import json
import os
import re

MANDATO_PATH = "docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md"

def extract_canonical_questions(mandato_path):
    questions = {}
    with open(mandato_path, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = re.compile(r"^[-*]\s+\*\*([PT]\d{2}-[FCX]\d{2})[\.:]\*\*\s*(.*)$", re.MULTILINE)
    for match in pattern.finditer(content):
        qid = match.group(1).strip()
        qtext = match.group(2).strip()
        questions[qid] = qtext
    return questions

def load_manifest(pilar):
    with open(f"fuentes/{pilar}.json", "r", encoding="utf-8") as f:
        m = json.load(f)
    sources = m.get("sources", m.get("fuentes", []))
    by_title_lower = {}
    for s in sources:
        sid = s.get("source_id") or s.get("id")
        title = s.get("title", "")
        by_title_lower[title.lower()] = s
    return sources, by_title_lower

def match_source_p06(mention, p06_sources, p06_by_title):
    m_lower = mention.lower()
    # Check exact substring matches
    for title_lower, s in p06_by_title.items():
        if m_lower in title_lower or title_lower in m_lower:
            return s.get("source_id"), s.get("title")

    # Author / keyword heuristics
    if "calamai" in m_lower or "detecting greenwashing" in m_lower:
        s = p06_by_title.get("calamai et al. (2025-2026) - detecting greenwashing survey (texto completo html v2)")
        if s: return s.get("source_id"), s.get("title")
    if "vinella" in m_lower or "leveraging language models" in m_lower:
        s = p06_by_title.get("vinella et al. (2023-2024) - language models greenwashing (texto completo html v2)")
        if s: return s.get("source_id"), s.get("title")
    if "t-grag" in m_lower or "li et al" in m_lower:
        s = p06_by_title.get("li et al. (2025) - t-grag: dynamic graphrag (texto completo pdf)")
        if s: return s.get("source_id"), s.get("title")
    if "splink" in m_lower or "fellegi" in m_lower:
        s = p06_by_title.get("splink (uk moj) - fast, scalable probabilistic entity resolution")
        if s: return s.get("source_id"), s.get("title")
    if "graphrag" in m_lower or "edge et al" in m_lower:
        s = p06_by_title.get("edge et al. (2024) - graphrag: query-focused summarization")
        if s: return s.get("source_id"), s.get("title")
    if "saber" in m_lower or "zhu et al" in m_lower:
        s = p06_by_title.get("saber (2026) - trust or abstain? self-aware rag")
        if s: return s.get("source_id"), s.get("title")
    if "ncg 461" in m_lower or "cmf" in m_lower:
        s = p06_by_title.get("cmf chile - sostenibilidad y norma de carácter general n° 461")
        if s: return s.get("source_id"), s.get("title")
    if "snifa" in m_lower or "sma" in m_lower:
        s = p06_by_title.get("sma chile - snifa: registro público de fiscalización y sanciones")
        if s: return s.get("source_id"), s.get("title")
    if "sernac" in m_lower or "greenwashing" in m_lower:
        s = p06_by_title.get("sernac chile - circular sobre consumo sostenible y greenwashing")
        if s: return s.get("source_id"), s.get("title")
    if "page" in m_lower or "principles" in m_lower:
        s = p06_by_title.get("arthur w. page society - the page principles")
        if s: return s.get("source_id"), s.get("title")
    if "quality_addendum" in m_lower or "addendum" in m_lower:
        s = p06_by_title.get("p06_quality_addendum: correcciones bibliográficas y límites metodológicos (síntesis interna)")
        if s: return s.get("source_id"), s.get("title")
    if "evidence_map" in m_lower:
        s = p06_by_title.get("p06_evidence_map: matriz de evidencia y tipología de discrepancias (síntesis interna)")
        if s: return s.get("source_id"), s.get("title")
    if "research_dossier" in m_lower or "dossier" in m_lower:
        s = p06_by_title.get("p06_research_dossier: análisis denso, matrices y entregables (síntesis interna)")
        if s: return s.get("source_id"), s.get("title")
    if "palantir" in m_lower:
        s = p06_by_title.get("palantir foundry - why create an ontology: decision-centric system")
        if s: return s.get("source_id"), s.get("title")
    if "signal ai" in m_lower:
        s = p06_by_title.get("signal ai - risk intelligence platform & aiq engine")
        if s: return s.get("source_id"), s.get("title")
    if "fever" in m_lower or "thorne" in m_lower:
        s = p06_by_title.get("thorne et al. (2018) - fever: fact extraction & verification")
        if s: return s.get("source_id"), s.get("title")
    if "ares" in m_lower or "saad-falcon" in m_lower:
        s = p06_by_title.get("saad-falcon et al. (2024) - ares: automated rag evaluation")
        if s: return s.get("source_id"), s.get("title")
    if "trulens" in m_lower:
        s = p06_by_title.get("trulens - core concepts: the rag triad of metrics")
        if s: return s.get("source_id"), s.get("title")
    if "ragas" in m_lower:
        s = p06_by_title.get("es et al. (2023) - ragas: automated evaluation of rag")
        if s: return s.get("source_id"), s.get("title")
    if "selfcheck" in m_lower or "manakul" in m_lower:
        s = p06_by_title.get("manakul et al. (2023) - selfcheckgpt: hallucination detection")
        if s: return s.get("source_id"), s.get("title")
    if "iabc" in m_lower:
        s = p06_by_title.get("iabc - code of ethics for professional communicators")
        if s: return s.get("source_id"), s.get("title")
    if "sec" in m_lower:
        s = p06_by_title.get("sec (2024) - final rule: climate-related disclosures for investors")
        if s: return s.get("source_id"), s.get("title")
    if "cove" in m_lower or "dhuliawala" in m_lower:
        s = p06_by_title.get("dhuliawala et al. (2023) - chain-of-verification (cove)")
        if s: return s.get("source_id"), s.get("title")
    if "alphasense" in m_lower:
        s = p06_by_title.get("alphasense - enterprise intelligence documentation")
        if s: return s.get("source_id"), s.get("title")
    if "dataminr" in m_lower:
        s = p06_by_title.get("dataminr pulse - real-time event & risk intelligence platform")
        if s: return s.get("source_id"), s.get("title")
    if "factiva" in m_lower or "dow jones" in m_lower:
        s = p06_by_title.get("dow jones factiva - developer platform & sentiment signals api")
        if s: return s.get("source_id"), s.get("title")

    # Default fallback to P06_RESEARCH_DOSSIER
    s = p06_by_title.get("p06_research_dossier: análisis denso, matrices y entregables (síntesis interna)")
    return s.get("source_id"), s.get("title")

def match_source_p01(mention, p01_sources, p01_by_title):
    m_lower = mention.lower()
    for title_lower, s in p01_by_title.items():
        if m_lower in title_lower or title_lower in m_lower:
            return s.get("source_id"), s.get("title")

    if "dircom" in m_lower or "ece" in m_lower:
        s = p01_by_title.get("dircom - el estado de la comunicación en españa (ece 2025): reporte al ceo y comité ejecutivo")
        if s: return s.get("source_id"), s.get("title")
    if "mckinsey" in m_lower:
        s = p01_by_title.get("mckinsey & company - upgrading corporate affairs for a new geopolitical era")
        if s: return s.get("source_id"), s.get("title")
    if "lobby" in m_lower or "20.730" in m_lower:
        s = p01_by_title.get("biblioteca del congreso nacional de chile - ley n° 20.730 que regula el lobby y gestiones de intereses particulares")
        if s: return s.get("source_id"), s.get("title")
    if "ncg 461" in m_lower or "cmf" in m_lower:
        s = p01_by_title.get("comisión para el mercado financiero (cmf chile) - ncg 461 y 519: sostenibilidad y gobierno corporativo")
        if s: return s.get("source_id"), s.get("title")
    if "page" in m_lower:
        s = p01_by_title.get("page society - beyond communication: cco leadership in navigating new complexity")
        if s: return s.get("source_id"), s.get("title")
    if "lcm" in m_lower or "euprera" in m_lower:
        s = p01_by_title.get("euprera - latin american communication monitor (lcm) portal y resultados")
        if s: return s.get("source_id"), s.get("title")
    if "global alliance" in m_lower or "gcf" in m_lower:
        s = p01_by_title.get("global alliance - global capability framework official benchmark")
        if s: return s.get("source_id"), s.get("title")
    if "merco" in m_lower:
        s = p01_by_title.get("merco chile - ranking merco empresas y reputación corporativa en chile")
        if s: return s.get("source_id"), s.get("title")
    if "edelman" in m_lower:
        s = p01_by_title.get("edelman - edelman trust barometer global report")
        if s: return s.get("source_id"), s.get("title")
    if "acción empresas" in m_lower or "asg" in m_lower:
        s = p01_by_title.get("acción empresas chile - red de sostenibilidad y desafíos ambientales, sociales y gobernanza (asg)")
        if s: return s.get("source_id"), s.get("title")
    if "gartner" in m_lower:
        s = p01_by_title.get("gartner - future of communications: trends for chief communication officers")
        if s: return s.get("source_id"), s.get("title")
    if "wef" in m_lower or "world economic forum" in m_lower:
        s = p01_by_title.get("world economic forum (wef) - stakeholder capitalism and corporate governance framework")
        if s: return s.get("source_id"), s.get("title")
    if "public affairs council" in m_lower:
        s = p01_by_title.get("public affairs council - 2025 benchmarking reports & corporate public affairs trends")
        if s: return s.get("source_id"), s.get("title")
    if "gaps" in m_lower or "validation" in m_lower:
        s = p01_by_title.get("p01_gaps_and_validation")
        if s: return s.get("source_id"), s.get("title")

    # Default fallback to P01_RESEARCH_DOSSIER
    s = p01_by_title.get("p01_research_dossier")
    return s.get("source_id"), s.get("title")

print("Matcher functions defined.")
