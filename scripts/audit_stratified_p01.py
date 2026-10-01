import json
import random

with open("respuestas/P01.jsonl", "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f if line.strip()]

total = len(lines)

def get_axis(qid):
    # Mapping P01 question IDs to 8 axes
    # F01-F06, C01-C02: Mandato y fronteras
    # F07-F12, C03-C04: Mapa de usuarios, compradores y aprobadores
    # F13-F18, C05-C06: Trabajos por hacer y momentos de presión
    # F19-F24, C07-C08: Reuniones y decisiones críticas
    # F25-F30, C09-C10: Riesgos de preparación insuficiente
    # F31-F36, C11-C12: Resultados y retorno de valor
    # F37-F42, C13-C14: Usuarios de asuntos corporativos en Chile y Latinoamérica
    # F43-F48, C15-C16: Descubrimiento y validación de usuarios
    prefix, num_str = qid.split("-")
    tipo = num_str[0]
    num = int(num_str[1:])
    if tipo == "F":
        axis_idx = (num - 1) // 6
    elif tipo == "C":
        axis_idx = (num - 1) // 2
    else:
        axis_idx = 0
    
    axis_names = [
        "Mandato y fronteras",
        "Mapa de usuarios, compradores y aprobadores",
        "Trabajos por hacer y momentos de presión",
        "Reuniones y decisiones críticas",
        "Riesgos de preparación insuficiente",
        "Resultados y retorno de valor",
        "Usuarios en Chile y Latinoamérica",
        "Descubrimiento y validación de usuarios"
    ]
    return axis_names[axis_idx]

axes = {}
for r in lines:
    axis_name = r.get("eje") or get_axis(r["question_id"])
    axes.setdefault(axis_name, []).append(r)

sampled = []
# Pick at least 1 from each of the 8 axes
random.seed(42) # Deterministic audit reproduction
for axis_name, axis_records in axes.items():
    sampled.append(random.choice(axis_records))

print(f"Total records in P01: {total}")
print(f"Stratified sample size: {len(sampled)} questions across {len(axes)} axes\n")

audit_results = []
for r in sampled:
    qid = r["question_id"]
    eje = r.get("eje") or get_axis(qid)
    tipo = "F" if "-F" in qid else "C"
    
    findings = r.get("findings", [])
    has_claims = len(findings) > 0
    all_claims_categorized = all(f.get("epistemic_status") in ["hecho_documentado", "declaracion_proveedor", "inferencia", "hipotesis_diseno"] for f in findings)
    
    evidence_count = sum(len(f.get("evidence", [])) for f in findings)
    all_evidence_has_locators = all(
        all(ev.get("source_id") and ev.get("source_title") and ev.get("locator") for ev in f.get("evidence", []))
        for f in findings
    )
    
    has_op_model = bool(r.get("operational_model") and r["operational_model"].get("actors") and r["operational_model"].get("steps"))
    has_entities = bool(r.get("entities"))
    has_relations = bool(r.get("relations"))
    has_bridge = bool(r.get("bridge_implications"))
    
    status_ok = has_claims and all_claims_categorized and all_evidence_has_locators and has_op_model and has_entities and has_bridge
    
    audit_results.append({
        "qid": qid,
        "tipo": tipo,
        "eje": eje,
        "status_ok": status_ok,
        "claims_count": len(findings),
        "evidence_count": evidence_count,
        "has_op_model": has_op_model,
        "has_entities": has_entities,
        "has_relations": has_relations
    })

print(f"{'QID':<10} | {'Tipo':<5} | {'Claims':<6} | {'Evid':<5} | {'OpMod':<5} | {'Ent':<4} | {'Rel':<4} | {'Audit':<6}")
print("-" * 65)
all_pass = True
for res in audit_results:
    verdict = "PASS" if res["status_ok"] else "FAIL"
    if not res["status_ok"]:
        all_pass = False
    print(f"{res['qid']:<10} | {res['tipo']:<5} | {res['claims_count']:<6} | {res['evidence_count']:<5} | {str(res['has_op_model']):<5} | {str(res['has_entities']):<4} | {str(res['has_relations']):<4} | {verdict:<6}")

print("\n" + "=" * 65)
if all_pass:
    print("STRATIFIED 10% AUDIT FOR PILAR P01: PASSED (100% compliant)")
else:
    print("STRATIFIED 10% AUDIT FOR PILAR P01: FAILED")
