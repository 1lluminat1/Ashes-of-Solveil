#!/usr/bin/env python3
# solveil_graphgen_utf8.py — auto-wires choices to any gate whose label mentions the changed variable
import sys, csv, yaml
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python solveil_graphgen_utf8.py spec.yaml out_dir")
        sys.exit(1)

    spec_path = Path(sys.argv[1])
    out_dir   = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    spec   = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    lines  = []
    meta   = spec.get("meta", {})
    title  = meta.get("title", "Influence Graph")
    note   = meta.get("notes", "")

    lines.append("%% " + title)
    if note: lines.append("%% " + note)
    lines.append("flowchart TD")

    scenes   = spec.get("scenes", [])
    gates    = spec.get("gates", {})
    defaults = spec.get("defaults", {})
    d_scope  = defaults.get("scope", {})
    d_expiry = defaults.get("expiry", {})
    d_tags   = defaults.get("tags", {})

    # --- index: which gates read which variables (by label text) ---
    var_to_gates = {}
    # add any other variables you care about here:
    tracked_vars = ("empathy_score", "Lyra.affection")
    for gid, glabel in gates.items():
        glabel_s = str(glabel)
        for v in tracked_vars:
            if v in glabel_s:
                var_to_gates.setdefault(v, []).append((gid, glabel))

    # --- fixed scene order ---
    lines.append("  %% === Fixed scene order ===")
    for s in scenes:
        sid, sname = s["id"], s.get("name", s["id"])
        lines.append(f'  {sid}("{sname}")')
    for s in scenes:
        if s.get("next"):
            lines.append(f'  {s["id"]} --> {s["next"]}')

    # --- choices and auto-wired influences ---
    lines.append("\n  %% === Choices inside scenes ===")
    csv_rows = []

    for s in scenes:
        sid = s["id"]
        for ch in (s.get("choices", []) or []):
            cid   = ch["id"]
            label = ch.get("label", cid)
            node  = f'C_{cid.replace(".","_").replace("@","_")}'
            lines.append(f'  {node}["Choice: {label}"]:::choice')
            lines.append(f'  {sid} --> {node}')

            deltas = ch.get("deltas", []) or []
            infls  = ch.get("influences", []) or []

            # stringify deltas for labels
            var_deltas = []
            changed_vars = []
            for d in deltas:
                if "var" in d:
                    changed_vars.append(d["var"])
                if "delta" in d:
                    var_deltas.append(f'{d["var"]} {d["delta"]:+d}')
                elif "set" in d:
                    var_deltas.append(f'{d["var"]}={"True" if d["set"] else "False"}')

            # auto-wire: if no explicit influences, connect to all gates that read the changed vars
            gates_list = []
            if infls:
                # honor explicit influences from YAML (if you add any by hand)
                for inf in infls:
                    gid    = inf["gate"]
                    glabel = inf.get("label", gates.get(gid, gid))
                    gates_list.append(f'Gate: {glabel}')
                    lines.append(f'  {node} -. "{("; ".join(var_deltas))}" .-> {gid}{{"{glabel}"}}:::gate')
            else:
                seen = set()
                for v in changed_vars:
                    for gid, glabel in var_to_gates.get(v, []):
                        key = (gid, glabel)
                        if key in seen: 
                            continue
                        seen.add(key)
                        gates_list.append(f'Gate: {glabel}')
                        lines.append(f'  {node} -. "{("; ".join(var_deltas))}" .-> {gid}{{"{glabel}"}}:::gate')

            # write CSV row
            csv_rows.append({
                "Choice ID": cid,
                "Scene": sid,
                "Variable Delta": "; ".join(var_deltas),
                "Scope":  d_scope.get(deltas[0]["var"], "") if deltas else "",
                "Expiry": d_expiry.get(deltas[0]["var"], "") if deltas else "",
                "Gate(s) that read it": "; ".join(gates_list),
                "Outcome tags": d_tags.get(cid, ""),
                "Notes": ""
            })

    # --- where gates are read later ---
    lines.append("\n  %% === Where gates are read later ===")
    for s in scenes:
        sid = s["id"]
        for gr in (s.get("reads_gates", []) or []):
            gid    = gr["gate"]
            glabel = gates.get(gid, gid)
            lines.append(f'  {sid} --> {gid}')
            if "yes" in gr:
                yes = gr["yes"]
                lines.append(f'  {gid} -->|Yes| {yes.get("id","Y_"+gid)}("{yes.get("name","Alt Yes")}"):::optional')
            if "no" in gr:
                no = gr["no"]
                lines.append(f'  {gid} -->|No| {no.get("id","N_"+gid)}("{no.get("name","Alt No")}"):::optional')

    # --- styling ---
    lines.append("\n  %% === Styling ===")
    lines.append("  classDef choice fill:#222,stroke:#666,color:#fff;")
    lines.append("  classDef gate fill:#111,stroke:#bbb,color:#fff;")
    lines.append("  classDef optional fill:#1b2838,stroke:#76a1ff,color:#fff;")

    # write files (UTF-8)
    mmd_path = out_dir / "auto_influence.mmd"
    mmd_path.write_text("\n".join(lines), encoding="utf-8")

    csv_path = out_dir / "auto_choice_state_gate.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Choice ID","Scene","Variable Delta","Scope","Expiry",
            "Gate(s) that read it","Outcome tags","Notes"
        ])
        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)

    print("Generated:", mmd_path, "and", csv_path)

if __name__ == "__main__":
    main()
