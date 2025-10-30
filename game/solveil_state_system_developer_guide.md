# Solveil State System — Explainer & Usage Guide (v1)

> Canon: **BC‑free** architecture. Use **`apply_choice_once`** as the *only* mutator at player choice time. Empathy score is for **flavor/momentum/UI**, while OB/EMP *locking* uses **ratio thresholds**.

---

## 0) Mental model

* **`STATE`** is the single source of truth.
* **Writers** (mutators): `apply_choice_once`, `adjust_empathy` (rare outside choices), `op_start/op_end`, `rel_bump`, inventory/reputation helpers, `canon_set`.
* **Readers** (gates/UI): `empathy_band`, `alignment_tier/desc`, `alignment_momentum`, `pass_emp/ob/tier`, predicates (`zira_ready_for_kiss` …), and any scene gating.
* **Ratios, not caps** decide pathing: `opp_emp/opp_ob` + `took_emp/took_ob`.

---

## 1) Characters

**Keys:** `STATE["chars"][name] = { rel:{trust,affection,loyalty}, flags:set(), ms:set(), notes:list }`

**Helpers:**

* `rel_get/rel_set/rel_add`, shorthand: `trust(name)`, `affection(name)`, `loyalty(name)`, and `rel_bump(name, trust=1, affection=0, loyalty=0)`
* `flag_on/flag_has` — character‑scoped booleans (e.g., `"kiss_happened"`).
* `ms_add/ms_has` — **milestones**: larger arc beats.
* `note(name, text)` — dev notes per character.

**Usage example:**

```renpy
$ rel_bump("Lyra", trust=+1)
$ flag_on("Zira", "vulnerability_scene_completed")
```

---

## 2) Scenes

**Keys:**

* `STATE["scenes"]["flags"][scene_id] -> set()`
* `STATE["scenes"]["snapshots"][op_id] -> dict`

**Helpers:** `scene_mark(scene_id, *keys)`, `scene_has(scene_id, key)`

**Pattern:** At scene entry, set a unique variable and mark it:

```renpy
$ _current_scene_id = "act1_12_lyra_visit"
$ scene_mark(_current_scene_id, "entered")
```

---

## 3) Inventory & Reputation

**Inventory:** `STATE["inv"] = { counters, tools:set, disguises:set, weapons:list, intel:{...}, favors_owed, debts_owed }`

**Helpers:** `add_item_counter`, `grant_tool/has_tool`, `grant_disguise/has_disguise`, `add_weapon`, `add_favor`, `pay_debt`.

**Reputation:** `STATE["rep"] = { unders, resistance, echelon }`

* **Use small per‑choice deltas** for *optics*: `echelon_delta/resistance_delta` in `apply_choice_once`.
* **Use `op_end`** for *outcomes* (saved/killed/mercy/suspicion)

---

## 4) Player metrics

**Keys (core):** `empathy_score`, `recent_empathy[]`, `echelon_alert`, `evidence_of_mercy`, `team_suspicion`, `civilians_saved/killed`.

**Ratio pathing keys:** `opp_emp`, `opp_ob`, `took_emp`, `took_ob`.

* *Meaning:* how many opportunities the player saw of each leaning (opp_*), and how many they chose (took_*).
* *Purpose:* drive **candidate/lock** decisions independent of raw empathy caps.

**Helpers:**

* `civ_saved/civ_killed`, `add_mercy`, `add_susp`.
* `adjust_empathy(amount)` — pushes momentum, clamps by your rails.
* `adjust_empathy_once(scene_id, token, amount)` — idempotent grant.
* `alignment*` readers: `empathy_band()` → `"empathy"|"conflicted"|"obedience"`, `alignment_tier()`, `alignment_desc()`, `alignment_momentum()`.
* `pass_emp/ob/tier` — clean scene gates.

**UI Use:**

```renpy
$ s=STATE['player']['empathy_score']
$ text "Empathy: [s]  Band: [empathy_band()]  Tier: [alignment_tier()]  Momentum: [round(alignment_momentum(),2)]"
```

---

## 5) Single‑call choice API (use everywhere)

`apply_choice_once(scene_id, token, weight, factor=1, next_scene_label="", echelon_delta=0, resistance_delta=0, note=None)`

* **Idempotent:** empathy per `(scene_id, token)` applied at most once.
* **Weight:** `"EMP" | "OB" | "NEU"` → auto computes ±delta (or 0).
* **Ratios:** increments `opp_*` for the **opportunity** and `took_*` if it actually applied.
* **Rep optics:** optional small deltas per choice.
* **Telemetry:** appends JSONL and Mermaid edge (per‑act files).

**Neutral helper:** `record_choice_once(scene_id, token, next_scene_label="", note=None)` (alias with `weight="NEU"`).

**Example:**

```renpy
menu:
    "Toast with officers":
        $ apply_choice_once(_current_scene_id, "toast_officers", "OB", factor=1,
                            next_scene_label="act1_07_bedroom",
                            echelon_delta=+1,
                            note="Protocol optics at gala")
        jump act1_07_bedroom

    "Check on the servant":
        $ apply_choice_once(_current_scene_id, "check_servant", "EMP", factor=1,
                            next_scene_label="act1_07_bedroom",
                            resistance_delta=+1,
                            note="Quiet kindness")
        jump act1_07_bedroom

    "Pick up the lantern (neutral)":
        $ record_choice_once(_current_scene_id, "pick_lantern", "act1_15_zira_first_contact", note="Good optics")
        jump act1_15_zira_first_contact
```

---

## 6) Candidate & Lock (ratio‑based)

**Thresholds (tune):**

* `ACT1_OB_RATIO = 0.80` → feel OB in Act I if ≥80% of OB opportunities were taken.
* `ACT2_OB_RATIO = 0.85` → hard OB lock.
* `ACT2_EMP_RATIO = 0.65` → hard EMP lock.
* **Chip acceptance** forces EMP candidate/lock.

**Candidate (Act I):** sets `STATE["canon"]["path_candidate"]` to `"EMP"|"OB"`.
**Lock (Act II – massive_recruitment):** sets `STATE["canon"]["path_state"]`.

**Usage:**

```renpy
$ evaluate_path_candidate_act1()  # call at the end of Bridge scene
$ lock_path_act2_massive_recruitment()  # inside massive_recruitment scene
```

---

## 7) Operations snapshots

Use these around multi‑step set pieces to accumulate outcomes and apply rep once.

```renpy
$ op_start("S10_sweep", note="Sector 10 Sweep")
...
$ civ_saved(3); add_mercy(1)
...
$ summary = op_end("S10_sweep", tag="S10 Sweep Outcome")
"{i}[summary]{/i}"
```

* `op_end` pushes **stats** and (optionally) **rep** via `_apply_rep`.
* Keep per‑choice rep deltas small to avoid double‑counting with op outcomes.

---

## 8) Canon glue

Global story booleans and one‑offs.

* `canon_set/ canon_get` — set & read flags like `"purge_witnessed"`, `"act1_complete"`.
* `set_base_location/base_location` — shared hub.

**Example:**

```renpy
$ canon_set("purge_witnessed")
if canon_get("purge_witnessed"):
    # unlock a memory beat
```

---

## 9) Predicates (examples)

* `zira_ready_for_kiss()` — showcases how to combine rel + flags + canon.
* Add more for your gating hotspots (e.g., `lyra_first_lewd_ready()`).

---

## 10) Debug overlay

Togglable HUD. Enable via `STATE["sys"]["debug_mode"] = True` during dev.
Shows trust/loyalty, rep, credits, days remaining, empathy metrics.

---

## 11) Mermaid & JSONL telemetry

* **Files:** `dev_graph_act1.mmd`, `devlog_act1.jsonl` (swap per act if preferred).
* Each call to `apply_choice_once` graphs `scene_id → next_scene_label` with a labeled edge.
* Use the JSONL file for analytics, QA, or regression tests.

**Tip:** In release builds, guard the file writes behind `if config.developer:` or a custom flag.

---

## 12) Best practices & gotchas

* **One writer at choice time:** only call `apply_choice_once` (or `record_choice_once`).
* **Do not farm:** Every empathy beat is keyed by `(scene_id, token)`.
* **Ratios over caps:** Empathy score can be wide‑railed. Locks use ratios.
* **Avoid double‑counting rep:** Use per‑choice deltas for optics; use `op_end` for outcomes.
* **Stable naming:** File/label/SCENE_ID must correspond (see naming standard below).
* **Scene header:**

```
# SCENE_ID: A1_12_LyraVisit | TYPE: VARIANT | ORDER: 12
# LABEL: act1_12_lyra_visit
```

* **Tokens:** `{slug}__{verb_noun}` (e.g., `breaking_point__refuse_order`).

---

## 13) Scene naming standard (authoritative)

* **File:** `act{A}_{NN}_{slug}.rpy`  → `act1_12_lyra_visit.rpy`
* **Label:** `act{A}_{NN}_{slug}`  → `act1_12_lyra_visit`
* **SCENE_ID:** `A{A}_{NN}_{SlugTitleCase}` → `A1_12_LyraVisit`
* **Insertions:** letter suffixes → `act1_07a_inspection_day`
* **Variant blocks:** in‑file `_emp` / `_ob` sublabels if absolutely necessary; prefer gates.

---

## 14) Quick reference (copy/paste)

```renpy
# Entering a scene
$ _current_scene_id = "act1_12_lyra_visit"
$ scene_mark(_current_scene_id, "entered")

# Choice (OB)
$ apply_choice_once(_current_scene_id, "toast_officers", "OB", factor=1,
                    next_scene_label="act1_07_bedroom",
                    echelon_delta=+1, note="Protocol optics")

# Choice (EMP)
$ apply_choice_once(_current_scene_id, "check_servant", "EMP", factor=1,
                    next_scene_label="act1_07_bedroom",
                    resistance_delta=+1, note="Quiet kindness")

# Choice (NEU)
$ record_choice_once(_current_scene_id, "inspect_room",
                     next_scene_label="act1_XX_next",
                     note="Surveyed area")

# Act I candidate (end of Bridge)
$ evaluate_path_candidate_act1()

# Act II lock (massive recruitment)
$ lock_path_act2_massive_recruitment()
```

---

## 15) Future extensions (optional)

* **Schema versioning:** `STATE["sys"]["schema"] = 1` plus a small migration runner in `after_load_callbacks`.
* **Global once‑tokens:** `STATE["canon"]["once"] = set()` + `adjust_empathy_once_global(token, amount)`.
* **Edge dedup for Mermaid:** keep an in‑memory `_edges_seen` or a small `STATE["sys"]["edges_seen"] = set()`.
* **Release gates:** wrap file I/O in `if config.developer:`.

---

**End of v1.** Keep this doc alongside `solveil_state_system.rpy` for quick reference.
