# Solveil State System — Developer Guide

*Version: Consolidated architecture (BC-safe)*

This guide explains what each section of `solveil_state_system.rpy` does and how to use it in scenes. It follows the file top‑to‑bottom so you can skim or copy/paste snippets as needed.

---

## 1) Core Dictionaries (state buckets)
These are the single sources of truth that everything else reads/writes.

### 1.1 Characters (`characters`)
- **What:** Per‑character data (relationship meters, romance toggles) plus two normalized sets:
  - `flags`: reversible toggles for small facts ("opened_up", "kissed_once").
  - `milestones`: one‑way achievements you never un‑set ("first_kiss", "revealed_backstory").
- **Why:** Keeps legacy keys (`trust`, `affection`, etc.) for backward compatibility (BC) while allowing cleaner, set‑based reads.
- **Use:**
```renpy
$ add_trust("Lyra", +1)
$ add_affection("Lyra", +1)
$ char_flag_on("Lyra", "opened_up")
$ if char_flag_has("Lyra", "opened_up"): ...
$ char_ms_add("Lyra", "first_kiss")
```

### 1.2 Scenes (`scenes`) and `scene_flags`
- **What:** `scenes` keeps your legacy per‑scene dicts. `scene_flags` is the modern set‑based mirror (by `scene_id`).
- **Why:** You can migrate gradually; both read paths work.
- **Use:**
```renpy
$ scene_id = "act1_05_gala"
$ set_scene_flag(scene_id, "acknowledge_lyra")
if check_scene_flag(scene_id, "acknowledge_lyra"): ...
```

### 1.3 Inventory (`inventory`)
- **What:** Keeps original nested dicts (supplies/tools/disguises/intel) and adds normalized mirrors:
  - `counters`: for numeric consumables
  - `tools_set`: presence set for tools
  - `disguises_set`: presence set for disguises ("unders", "mid", "echelon")
- **Why:** Reads become simple (`has_tool("hacking_device")`) while BC with old dicts remains.
- **Use:**
```renpy
$ add_item("supplies", "food", +1)            # counters + legacy kept in sync
$ add_item("tools", "hacking_device")          # also adds to tools_set
$ grant_disguise("echelon")
if has_tool("hacking_device"): ...
```

### 1.4 Reputation / Skills / Player / Canon / Stats / System
- **reputation**: simple faction meters (`unders`, `resistance`, `echelon`).
- **skills_set**: normalized presence of learned skills (built from legacy `skills`).
- **player_state**: global run‑wide counters (empathy, civilians saved/killed, suspicion, etc.).
- **canon**: story‑wide locks (chapter gates, witnessed events).
- **stats**: aggregate counters for credits, people saved/killed, etc.
- **system_flags**: debug UI, shortcuts, overlay log buffer.

Use helpers:
```renpy
$ inc_rep("unders", +1)
$ learn_skill("pattern_recognition")
$ add_civilians_saved(3)
$ add_team_suspicion(1)
```

---

## 2) Helpers (BC‑safe API)
Small wrappers so scenes never poke dicts directly.

- **Relationship**: `add_trust`, `add_affection`, `add_loyalty`, `unlock_romance`, `relationship_state(name)`.
- **Character facts**: `char_flag_on/has`, `char_ms_add/has`, `char_note`.
- **Scenes**: `set_scene_flag(scene_id, key)`, `check_scene_flag(scene_id, key)` (writes both new and legacy locations).
- **Inventory**: `add_item`, `add_item_counter`, `has_item`, `grant_tool`, `has_tool`, `grant_disguise`, `has_disguise`, `add_favor`, `pay_debt`.
- **Reputation/Stats/Skills**: `inc_rep`, `inc_stat`, `learn_skill`, `has_skill`.
- **Player counters**: `add_evidence_of_mercy`, `add_team_suspicion`, `add_civilians_saved`, `add_civilians_killed`.

**Rule of thumb:** Always call a helper; never mutate the dicts in scenes. This keeps migration painless.

---

## 3) Alignment (Empathy ↔ Obedience)
A single axis with robust reads and simple writes.

### 3.1 Core knobs
- `EMPATHY_MIN = -12`, `EMPATHY_MAX = 12`, `EMP_EDGE = 3` (band thresholds)
- Recent momentum: last 6 empathy deltas for micro‑tone.

### 3.2 Writing alignment
```renpy
$ adjust_empathy(+1)                       # common nudge
$ adjust_empathy_once("act1_gala_hand", +1)  # award once per unique id
```
*Guidance:* ±1 for flavor beats, ±2 for scene‑defining choices, avoid >±3 early.

### 3.3 Reading alignment
- **Bands** (coarse): `get_empathy_band()` → `"obedience" | "conflicted" | "empathy"`
- **Tiers** (fine): `get_alignment_tier()` → `OB3 / OB2 / OB1 / C / EMP1 / EMP2 / EMP3`
- **Normalized**: `get_alignment_score_norm()` → float −1.0..+1.0
- **Momentum**: `get_alignment_momentum()` → float −1..+1 (recent direction)
- **Gates**: `pass_emp_gate(min_edge=EMP_EDGE)`, `pass_ob_gate()`, `pass_tier("EMP2", "EMP3")`

**Typical usage:**
```renpy
$ band = get_empathy_band()
if band == "obedience":
    # colder variant
elif band == "empathy":
    # warmer variant
else:
    # conflicted
```

---

## 4) Operation Reconciliation Kit
Track mission deltas reliably and auto‑propagate consequences.

### 4.1 Start/End
```renpy
$ start_operation("op391_sector10", note="Sector 10 Sweep")
# ... your scene modifies saved/killed/mercy/suspicion/empathy ...
$ summary = end_operation("op391_sector10")
# Optionally log it
$ log_line(summary)
```

### 4.2 What `end_operation` does
- Computes deltas vs. the snapshot (saved/killed/mercy/suspicion).
- Updates aggregate `stats` (if `auto_stats=True`).
- Applies a simple faction model (`_apply_reputation`) if `auto_repute=True`.
- Clamps empathy to safe bounds.
- Flips basic canon hints via `_canon_touches` (customize per project).
- Returns a one‑line human summary and stores it alongside the snapshot.

**Tuning points:**
- `_apply_reputation(...)` → adjust faction math.
- `_canon_touches(op_id, ...)` → branch story beats by outcome scale.

---

## 5) Debug Overlay (`screen solveil_debug_overlay`)
A minimal always‑on overlay (when `system_flags["debug_mode"]` is `True`).

**Shows:** empathy score, band, tier, momentum; select resource lines (credits/days); a couple trust/loyalty snippets.

**Enable:**
```renpy
$ system_flags["debug_mode"] = True
```
The file auto‑registers the overlay if it isn’t already in `config.overlay_screens`.

**Optional log:**
```renpy
$ log_line("entered act1_05_gala")
# Last ~12 lines are kept in system_flags["logs"] (render in your own debug UI if desired)
```

---

## 6) Patterns & Best Practices

### 6.1 Branching on alignment
Prefer bands/tiers over raw numbers.
```renpy
$ tier = get_alignment_tier()
if tier in ("OB3","OB2"):
    # very cold
elif tier in ("OB1","C"):
    # measured
else:
    # EMP1/EMP2/EMP3
```

### 6.2 Safe empathy awards
- Micro: ±1 for flavor.
- Medium: ±2 for scene‑defining.
- Use `adjust_empathy_once(id, amt)` for any beat that could repeat via re‑entry.

### 6.3 Scene flags
Always set a local id at the top and use the helper:
```renpy
$ scene_id = "act1_05_gala"
$ set_scene_flag(scene_id, "acknowledge_lyra")
if check_scene_flag(scene_id, "acknowledge_lyra"): ...
```

### 6.4 Inventory
- For consumables use: `add_item("supplies", "food", +1)` **or** `add_item_counter("food", +1)` (both keep legacy+normalized in sync).
- For presence items use: `grant_tool("hacking_device")` and `has_tool("hacking_device")`.
- Disguises (normalized): `grant_disguise("echelon")`; `has_disguise("echelon")`.

### 6.5 Relationships
- **Trust** drives reliability/gating.
- **Affection** drives warmth/intimacy pacing.
- Keep romance flows gated by trust **and** affection when appropriate:
```renpy
if pass_tier("EMP1","EMP2","EMP3") and characters["Lyra"]["trust"] >= 2 and characters["Lyra"]["affection"] >= 1:
    # allow softer option
```

---

## 7) Quick Reference (copy/paste)

**Award empathy once**
```renpy
$ adjust_empathy_once("act1_18_confession_space", +1)
```

**Gate by band**
```renpy
if get_empathy_band() == "obedience":
    ...
```

**Gate by tier**
```renpy
if pass_tier("EMP2","EMP3"): ...
```

**Start / end a mission**
```renpy
$ start_operation("op392_bridge", note="Obsidian Bridge")
# ... do things ...
$ summary = end_operation("op392_bridge")
$ log_line(summary)
```

**Set & read a scene flag**
```renpy
$ set_scene_flag("act1_12_lyra_visit", "let_her_stay")
if check_scene_flag("act1_12_lyra_visit", "let_her_stay"): ...
```

**Inventory presence**
```renpy
$ grant_tool("binoculars")
if has_tool("binoculars"): ...
```

---

## 8) Migration notes
- Old reads like `scenes["act1_05_gala"]["foo"]` still work, but prefer `scene_flags` helpers going forward.
- Avoid writing raw numbers directly (empathy, rep, stats); always go through helpers.
- You can prune unused legacy keys over time—the helpers isolate you from structure churn.

---

**That’s it.** Keep scenes thin and expressive; let helpers do the bookkeeping. When in doubt: set a flag, award empathy via a helper, and branch by band/tier—not raw numbers.

