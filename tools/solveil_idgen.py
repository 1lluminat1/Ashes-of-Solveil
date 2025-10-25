
#!/usr/bin/env python3
"""
solveil_idgen_patched.py (Solveil-tuned, filename fallback, UTF-8 writes)
Auto-assigns stable Choice IDs by scanning Ren'Py .rpy files.
Tracks Act1 variables: empathy_score, Lyra.affection.
Understands helper calls: adjust_empathy(N), add_affection("Lyra", N).

Usage:
  python solveil_idgen_patched.py /path/to/repo/game /path/to/out/auto_spec.yaml
"""
import sys, re, json, hashlib
from pathlib import Path
import yaml

# ==========================
# Scene ID from label or filename
# Supports: act{act}_{num}{optLetter}_{tail}
# Examples: act1_13_the_message, act1_02b_sector7_mission
# ==========================
def stable_scene_id(label_name: str, filename: str = "") -> str:
    m = re.match(r'act(\d+)_(\d+)([a-z])?_([a-z0-9_]+)', label_name)
    if not m and filename:
        base = filename.rsplit('.',1)[0]
        m = re.match(r'act(\d+)_(\d+)([a-z])?_([a-z0-9_]+)', base)
    if m:
        act = int(m.group(1))
        s = int(m.group(2))
        suffix = (m.group(3) or "").upper()     # e.g., 'B'
        tail = re.sub(r'[^A-Z0-9]+','_', m.group(4).upper()).strip('_')
        tail = tail[:4] if len(tail) >= 4 else tail
        return f"A{act}_S{s:02d}{suffix}_{tail}"
    h = hashlib.md5((label_name or filename).encode()).hexdigest()[:4].upper()
    return f"AX_SXX_{h}"

# ==========================
# Variables we track (Act 1)
# ==========================
VAR_CANON = {
    "empathy_score": r'player_state\[\s*["\']empathy_score["\']\s*\]',
    "Lyra.affection": r'characters\[\s*["\']lyra["\']\s*\]\s*\[\s*["\']affection["\']\s*\]|characters\[\s*["\']Lyra["\']\s*\]\s*\[\s*["\']affection["\']\s*\]'
}
VAR_PAT = re.compile(
    rf'(?P<match>{VAR_CANON["empathy_score"]}|{VAR_CANON["Lyra.affection"]})',
    re.IGNORECASE
)

def normalize_var(lhs: str) -> str:
    lhs = lhs.strip()
    if re.search(VAR_CANON["empathy_score"], lhs, flags=re.IGNORECASE):
        return "empathy_score"
    if re.search(VAR_CANON["Lyra.affection"], lhs, flags=re.IGNORECASE):
        return "Lyra.affection"
    return lhs

# ==========================
# Delta patterns
# ==========================
DELTA_ARITH = re.compile(
    r'\$\s*(?P<lhs>[^#\n]+?)\s*(?P<op>\+=|-=|=)\s*(?P<rhs>True|False|-?\d+)\s*$'
)
DELTA_FUNC_ADJUST_EMPATHY = re.compile(
    r'\$\s*adjust_empathy\s*\(\s*(?P<num>[-+]?\d+)\s*\)\s*$', re.IGNORECASE
)
DELTA_FUNC_ADD_AFFECTION = re.compile(
    r'\$\s*add_affection\s*\(\s*["\']\s*lyra\s*["\']\s*,\s*(?P<num>[-+]?\d+)\s*\)\s*$', re.IGNORECASE
)

# ==========================
# Gate detection
# ==========================
IF_GATE_PAT = re.compile(r'^\s*if\s+(?P<cond>.+):\s*$')

def gate_label_from_cond(cond: str) -> str:
    norm = cond
    norm = re.sub(VAR_CANON["empathy_score"], "empathy_score", norm, flags=re.IGNORECASE)
    norm = re.sub(VAR_CANON["Lyra.affection"], "Lyra.affection", norm, flags=re.IGNORECASE)
    norm = re.sub(r'\s+', ' ', norm).strip()
    return norm

def gate_id_from_label(label: str) -> str:
    return "G_" + re.sub(r'[^A-Za-z0-9]+', '_', label).upper()[:24]

# ==========================
# Choice ID assignment (stable via registry)
# ==========================
def slug_choice(text: str) -> str:
    s = re.sub(r'\W+', ' ', text).strip().split()
    base = ''.join(w.capitalize() for w in s[:3]) or "Choice"
    return base

def assign_choice_id(scene_sid: str, registry: dict, choice_text: str) -> str:
    key = f"{scene_sid}::{choice_text.strip()}"
    if key in registry:
        return registry[key]
    m = re.match(r'A(\d+)_S(\d+)[A-Z]?_', scene_sid)
    if m:
        act = int(m.group(1)); s = int(m.group(2))
    else:
        act, s = 0, 0
    slug = slug_choice(choice_text)
    cid = f"A{act}.S{s:02d}.{slug}"
    used = set(registry.values())
    base = cid; k = 2
    while cid in used:
        cid = f"{base}{k}"; k += 1
    registry[key] = cid
    return cid

# ==========================
# Scanner
# ==========================
def parse_files(game_dir: Path):
    scenes = []
    registry = {}
    reg_path = game_dir / "ids_registry.json"
    if reg_path.exists():
        try: registry = json.loads(reg_path.read_text(encoding="utf-8"))
        except Exception: registry = {}

    files = sorted(game_dir.rglob("*.rpy"))
    for fp in files:
        try:
            raw = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        lines = raw.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            ml = re.match(r'\s*label\s+([A-Za-z0-9_]+)\s*:\s*', line)
            if ml:
                label_name = ml.group(1)
                sid = stable_scene_id(label_name, fp.name)
                scene = {"id": sid, "name": f"{label_name}", "choices": []}
                scenes.append(scene)

                i += 1
                menu_mode = False
                current_choice = None

                while i < len(lines):
                    l = lines[i]

                    # next label ends this scene scan
                    if re.match(r'\s*label\s+[A-Za-z0-9_]+\s*:\s*', l):
                        i -= 1; break

                    # menu start
                    if re.match(r'\s*menu\s*:\s*', l):
                        menu_mode = True; i += 1; continue

                    if menu_mode:
                        mc = re.match(r'(\s*)"([^"]+)"\s*(?:if\s+[^:]+)?\s*:\s*', l)
                        if mc:
                            choice_text = mc.group(2)
                            cid = assign_choice_id(scene["id"], registry, choice_text)
                            current_choice = {"id": cid, "label": choice_text, "deltas": [], "influences": []}
                            scene["choices"].append(current_choice)
                            i += 1; continue

                        # --- Deltas ---
                        mA = DELTA_ARITH.search(l)
                        if mA and current_choice is not None:
                            lhs = mA.group("lhs"); op = mA.group("op"); rhs = mA.group("rhs")
                            var = normalize_var(lhs)
                            if var in ("empathy_score", "Lyra.affection"):
                                if op == "+=":
                                    current_choice["deltas"].append({"var": var, "delta": int(rhs)})
                                elif op == "-=":
                                    current_choice["deltas"].append({"var": var, "delta": -int(rhs)})
                                elif op == "=":
                                    if rhs in ("True","False"):
                                        val = True if rhs == "True" else False
                                        current_choice["deltas"].append({"var": var, "set": val})
                                    else:
                                        current_choice["deltas"].append({"var": var, "set": int(rhs)})

                        mB1 = DELTA_FUNC_ADJUST_EMPATHY.search(l)
                        if mB1 and current_choice is not None:
                            n = int(mB1.group("num"))
                            current_choice["deltas"].append({"var": "empathy_score", "delta": n})

                        mB2 = DELTA_FUNC_ADD_AFFECTION.search(l)
                        if mB2 and current_choice is not None:
                            n = int(mB2.group("num"))
                            current_choice["deltas"].append({"var": "Lyra.affection", "delta": n})

                    # --- Gates ---
                    mi = IF_GATE_PAT.search(l)
                    if mi:
                        cond = gate_label_from_cond(mi.group("cond"))
                        if "empathy_score" in cond or "Lyra.affection" in cond:
                            gid = gate_id_from_label(cond)
                            scene.setdefault("reads_gates", [])
                            if not any(rg.get("gate")==gid for rg in scene["reads_gates"]):
                                scene["reads_gates"].append({"gate": gid, "label": cond})

                    i += 1
            i += 1

    # Linear next pointers by discovery order
    for idx in range(len(scenes)-1):
        scenes[idx]["next"] = scenes[idx+1]["id"]

    # Gates dict from collected reads (use their human labels)
    gates = {}
    for s in scenes:
        for rg in s.get("reads_gates", []) or []:
            gid = rg["gate"]
            gates[gid] = rg.get("label", gid.replace("G_", "").replace("_", " "))

    # Persist registry
    try:
        reg_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass

    return scenes, gates

def main():
    if len(sys.argv) < 3:
        print("Usage: python solveil_idgen_patched.py /path/to/repo/game /path/to/out/auto_spec.yaml")
        sys.exit(1)
    game_dir = Path(sys.argv[1])
    out_yaml = Path(sys.argv[2])
    scenes, gates = parse_files(game_dir)
    spec = {
        "meta": {"title": "Auto-extracted Influence Spec", "notes": "Solveil-tuned (empathy_score, Lyra.affection)"},
        "scenes": scenes,
        "gates": gates,
        "defaults": {
            "scope": {"empathy_score":"Global","Lyra.affection":"Lyra"},
            "expiry": {"empathy_score":"Until A2 Split","Lyra.affection":"Act 1"}
        }
    }
    out_yaml.write_text(yaml.dump(spec, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Wrote spec: {out_yaml}")

if __name__ == "__main__":
    main()
