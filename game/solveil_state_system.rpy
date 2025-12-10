# solveil_state_system.rpy
# Ashes of Solveil — New State Architecture (BC-free)
# Notes:
# - Use apply_choice_once(...) for ALL player choices (idempotent + logs + ratios).
# - Empathy score is for flavor/momentum/UI; path candidate/lock use ratios.
# - Telemetry (Mermaid/JSONL) only writes when config.developer and telemetry_on = True.

init python:
    # Dev hook: default no-op; dev_tools.rpy will install a real one in dev.
    DEV_AFTER_CHOICE = None

    def _set_dev_after_choice(fn):
        global DEV_AFTER_CHOICE
        DEV_AFTER_CHOICE = fn

init python:
    import os, re, json, datetime

    # =========================
    # CANONICAL STATE (no legacy)
    # =========================
    STATE = {
        "chars": {
            # Example seeds (adjust to your actual starts)
            "Lyra":    {"rel":{"trust":1,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
            "Zira":    {"rel":{"trust":0,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
            "Tessa":   {"rel":{"trust":0,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
            "Noelle":  {"rel":{"trust":0,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
            "Selene":  {"rel":{"trust":0,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
            "Nero":    {"rel":{"trust":0,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
            "doc_mara":{"rel":{"trust":0,"affection":0,"loyalty":0}, "flags":set(), "ms":set(), "notes":[]},
        },

        "scenes": {
            # scene flags are sets keyed by scene_id
            "flags": {},        # e.g. flags["act2_15"] = {"completed","kiss_happened"}
            "snapshots": {},    # op snapshots by id (see ops helpers)
        },

        "inv": {
            "credits": 150, "scrip": 0,
            "counters": { "medkits":0, "stims":0, "food":3, "water":3, "cigs":0, "alcohol":0 },
            "tools": set(),         # {"lockpicks","hacking_device","binoculars"}
            "disguises": set(),     # {"unders","mid","echelon"}
            "weapons": [],          # freeform
            "intel":   { "documents": [], "maps": [], "secrets": [] },
            "favors_owed": [], "debts_owed": []
        },

        "rep": { "unders": -5, "resistance": 0, "echelon": -100 },

        "skills": set(),  # {"unders_disguise","pattern_recognition", ...}

        "player": {
            "fake_names": { "aeron":"Kade Voss", "lyra":"Mira Chen" },
            "days_remaining": 7,
            "bounty": { "aeron":50000, "lyra":50000 },
            "echelon_alert": 0,

            # --- Empathy axis (flavor/momentum/UI) ---
            "empathy_score": -5,
            "recent_empathy": [],

            # --- Mission conduct ---
            "evidence_of_mercy": 0,
            "team_suspicion": 0,
            "civilians_saved": 0,
            "civilians_killed": 0,

            # --- Ratio pathing (candidate/lock) ---
            "opp_emp": 0,
            "opp_ob": 0,
            "took_emp": 0,     # <-- fixed colon
            "took_ob": 0,
        },

        "canon": {
            "act1_complete": False, "purge_witnessed": False, "glass_shattered": False,
            "defected": False, "met_selene": False, "resistance_joined": False,
            "base_location": None,  # "subway/clinic/warehouse/apartment/tunnels"
            # add any global one-offs you want here
        },

        "stats": { "people_saved": 0, "people_killed": 600, "resistance_strength": 0, "major_victories": 0, "major_losses": 0 },

        "codex": {},

        "sys":   {
            "debug_mode": False,
            "logs": [],
            "telemetry_on": True,     # gate file writes in release builds
            "edges_seen": set(),      # Mermaid edge dedup
        },
    }

    # After-load migration guard (old saves)
    def ensure_choice_counters():
        p = STATE["player"]
        for k in ("opp_emp","opp_ob","took_emp","took_ob"):
            if k not in p: p[k] = 0
        sys = STATE.get("sys", {})
        if "edges_seen" not in sys:
            sys["edges_seen"] = set()
        if "telemetry_on" not in sys:
            sys["telemetry_on"] = True
        STATE["sys"] = sys

    if not hasattr(config, "after_load_callbacks"):
        config.after_load_callbacks = []
    if ensure_choice_counters not in config.after_load_callbacks:
        config.after_load_callbacks.append(ensure_choice_counters)

    # =========================
    # SMALL INTERNALS
    # =========================
    def _c(name): return name if name in STATE["chars"] else name.title()
    def _ensure_scene(scene_id):
        flags = STATE["scenes"]["flags"]
        if scene_id not in flags: flags[scene_id] = set()
        return flags[scene_id]

    # =========================
    # CHARACTER RELATIONS API
    # =========================
    def rel_get(name, key):        return int(STATE["chars"][_c(name)]["rel"].get(key, 0))
    def rel_set(name, **vals):
        r = STATE["chars"][_c(name)]["rel"]
        for k,v in vals.items(): r[k] = int(v)

    def rel_add(name, **deltas):
        r = STATE["chars"][_c(name)]["rel"]
        for k,dv in deltas.items(): r[k] = int(r.get(k,0)) + int(dv)

    def trust(name):     return rel_get(name, "trust")
    def affection(name): return rel_get(name, "affection")
    def loyalty(name):   return rel_get(name, "loyalty")

    # common sugar you can keep using in scenes
    def rel_bump(name, trust=0, affection=0, loyalty=0):
        d={}
        if trust: d["trust"]=trust
        if affection: d["affection"]=affection
        if loyalty: d["loyalty"]=loyalty
        if d: rel_add(name, **d)

    # Flags / milestones / notes
    def flag_on(name, key):  STATE["chars"][_c(name)]["flags"].add(key)
    def flag_has(name, key): return key in STATE["chars"][_c(name)]["flags"]
    def ms_add(name, key):   STATE["chars"][_c(name)]["ms"].add(key)
    def ms_has(name, key):   return key in STATE["chars"][_c(name)]["ms"]
    def note(name, text):    STATE["chars"][_c(name)]["notes"].append(str(text))

    # =========================
    # SCENE FLAGS
    # =========================
    def scene_mark(scene_id, *keys):
        s = _ensure_scene(scene_id)
        for k in keys: s.add(k)

    def scene_has(scene_id, key):
        return key in STATE["scenes"]["flags"].get(scene_id, set())

    # =========================
    # INVENTORY
    # =========================
    def add_item_counter(key, qty=1):
        c = STATE["inv"]["counters"]; c[key] = c.get(key,0) + qty
    def grant_tool(k):      STATE["inv"]["tools"].add(k)
    def has_tool(k):        return k in STATE["inv"]["tools"]
    def grant_disguise(k):  STATE["inv"]["disguises"].add(k)
    def has_disguise(k):    return k in STATE["inv"]["disguises"]
    def add_weapon(w):      STATE["inv"]["weapons"].append(w)
    def add_favor(p):       STATE["inv"]["favors_owed"].append(p)
    def pay_debt(p):
        if p in STATE["inv"]["debts_owed"]: STATE["inv"]["debts_owed"].remove(p)

    # =========================
    # REPUTATION / STATS / SKILLS
    # =========================
    def rep_inc(faction, amt): STATE["rep"][faction] = STATE["rep"].get(faction,0)+amt
    def stat_inc(key, amt=1):  STATE["stats"][key] = STATE["stats"].get(key,0)+amt
    def learn(skill):          STATE["skills"].add(skill)
    def knows(skill):          return skill in STATE["skills"]

    # =========================
    # PLAYER COUNTERS
    # =========================
    def civ_saved(n=1):   STATE["player"]["civilians_saved"] += n
    def civ_killed(n=1):  STATE["player"]["civilians_killed"] += n
    def add_mercy(n=1):   STATE["player"]["evidence_of_mercy"] += n
    def add_susp(n=1):    STATE["player"]["team_suspicion"] += n

    # =========================
    # PLAYER VALUE GETTERS
    # =========================
    def get_saved() -> int:      return max(0, STATE["player"].get("civilians_saved", 0))
    def get_killed() -> int:     return max(0, STATE["player"].get("civilians_killed", 0))
    def get_mercy() -> int:      return max(0, STATE["player"].get("evidence_of_mercy", 0))
    def get_suspicion() -> int:  return max(0, STATE["player"].get("team_suspicion", 0))
    def mercy_ge(n: int) -> bool:    return get_mercy() >= n
    def mercy_any() -> bool:         return get_mercy() >= 1
    def mercy_heavy() -> bool:       return get_mercy() >= 3
    def saved_str() -> str:          return str(get_saved())
    def killed_str() -> str:         return str(get_killed())

    # =========================
    # PATHING (RATIO-BASED) — Candidate & Lock
    # =========================
    ACT1_OB_RATIO  = 0.80   # feel OB in Act I if >=80% of OB opportunities were taken
    ACT2_OB_RATIO  = 0.85   # hard OB lock
    ACT2_EMP_RATIO = 0.65   # hard EMP lock

    def evaluate_path_candidate_act1():
        # Chip acceptance overrides to EMP candidate
        if STATE["canon"].get("chip_accepted", False):
            STATE["canon"]["path_candidate"] = "EMP"
            return "EMP"
        ob_opp = max(1, STATE["player"]["opp_ob"])   # avoid div by zero
        ob_ratio = float(STATE["player"]["took_ob"]) / float(ob_opp)
        STATE["canon"]["path_candidate"] = "OB" if ob_ratio >= ACT1_OB_RATIO else "EMP"
        return STATE["canon"]["path_candidate"]

    def lock_path_act2_massive_recruitment():
        # Already locked?
        if STATE["canon"].get("path_state") in ("OB","EMP"):
            return STATE["canon"]["path_state"]

        # Chip acceptance forces EMP lock
        if STATE["canon"].get("chip_accepted", False):
            STATE["canon"]["path_state"] = "EMP"
            return "EMP"

        ob_opp  = max(1, STATE["player"]["opp_ob"])
        emp_opp = max(1, STATE["player"]["opp_emp"])
        ob_ratio  = float(STATE["player"]["took_ob"])  / float(ob_opp)
        emp_ratio = float(STATE["player"]["took_emp"]) / float(emp_opp)

        if ob_ratio  >= ACT2_OB_RATIO:
            STATE["canon"]["path_state"] = "OB"
        elif emp_ratio >= ACT2_EMP_RATIO:
            STATE["canon"]["path_state"] = "EMP"
        else:
            # tie-breaker by momentum; default OB if perfectly neutral
            STATE["canon"]["path_state"] = "EMP" if alignment_momentum() > 0 else "OB"
        return STATE["canon"]["path_state"]

    # =========================
    # GHOSTLINE CHIP (Act I symbol)
    # =========================
    def give_ghostline_chip(accepted: bool):
        STATE["inv"]["tools"].add("ghostline_chip")
        STATE["canon"]["got_chip"] = True
        STATE["canon"]["chip_accepted"] = bool(accepted)

    # =========================
    # ALIGNMENT / EMP–OB
    # =========================
    USE_EMPATHY_CLAMP = False     # Toggle: set True to enforce rails
    EMPATHY_MIN = -12
    EMPATHY_MAX =  12
    EMP_EDGE = 3
    RECENT_N = 6

    def empathy_norm():
        # 0..1 normalized for UI (clamped)
        rng = float(EMPATHY_MAX - EMPATHY_MIN)
        s = float(STATE["player"]["empathy_score"])
        v = (s - EMPATHY_MIN) / rng
        return max(0.0, min(1.0, v))

    def empathy_band():
        s = STATE["player"]["empathy_score"]
        if s >= EMP_EDGE: return "empathy"
        if s <= -EMP_EDGE: return "obedience"
        return "conflicted"

    def alignment_tier():
        s = int(STATE["player"]["empathy_score"])
        if s <= -9: return "OB3"
        if s <= -5: return "OB2"
        if s <= -1: return "OB1"
        if s == 0:  return "C"
        if s <= 4:  return "EMP1"
        if s <= 8:  return "EMP2"
        return "EMP3"

    def alignment_desc():
        return {
            "OB3":"Iron Obedience","OB2":"Hard Obedience","OB1":"Leaning Obedience",
            "C":"Conflicted","EMP1":"Leaning Empathy","EMP2":"Strong Empathy","EMP3":"Conviction Empathy"
        }[alignment_tier()]

    def alignment_momentum():
        arr = STATE["player"]["recent_empathy"]
        if not arr: return 0.0
        total = sum(arr); max_sum = max(1.0, RECENT_N * 3.0)
        return max(-1.0, min(1.0, total / max_sum))

    def pass_tier(*tiers): return alignment_tier() in tiers
    def pass_emp(): return STATE["player"]["empathy_score"] >= EMP_EDGE
    def pass_ob():  return STATE["player"]["empathy_score"] <= -EMP_EDGE

    # Flavor gate helper (kept for convenience)
    def align_flavor():
        tier = alignment_tier()
        is_ob_hard = pass_tier("OB3","OB2")
        is_mid     = pass_tier("OB1","C")
        return tier, is_ob_hard, is_mid

    def flavor(ob=None, mid=None, emp=None):
        _, is_ob_hard, is_mid = align_flavor()
        if is_ob_hard: return ob
        if is_mid:     return mid
        return emp

    def _push_recent(delta):
        arr = STATE["player"]["recent_empathy"]
        arr.append(int(delta))
        if len(arr) > RECENT_N:
            del arr[0:len(arr)-RECENT_N]

    def clamp_empathy():
        if not USE_EMPATHY_CLAMP:
            return
        s = STATE["player"]["empathy_score"]
        STATE["player"]["empathy_score"] = max(EMPATHY_MIN, min(EMPATHY_MAX, s))

    # Optional, used by your doctrine soft-lock scene
    def apply_empathy_with_mod(base_delta: int) -> int:
        """
        Apply per-scene empathy with temporary decay/boost windows (if you've set them).
        Returns the actual applied delta (for UI flavor if needed).
        """
        mod = 0
        if STATE.get("empathy_decay_steps", 0) > 0:
            mod -= STATE.get("empathy_decay", 0)
            STATE["empathy_decay_steps"] -= 1
        if STATE.get("emp_boost_window", 0) > 0:
            mod += 1
            STATE["emp_boost_window"] -= 1

        actual = base_delta + mod
        if actual != 0:
            adjust_empathy(actual)
        return actual

    def adjust_empathy(amount):
        _push_recent(amount)
        STATE["player"]["empathy_score"] += int(amount)
        clamp_empathy()

    def _mark_once(scene_id: str, prefix: str, token: str) -> bool:
        """
        Idempotent scene marker. Returns True if we're marking this now (first time).
        """
        key = f"{prefix}:{token}"
        if scene_has(scene_id, key): return False
        scene_mark(scene_id, key)
        return True

    def adjust_empathy_once(scene_id: str, token: str, amount: int) -> bool:
        key = f"emp_once:{token}"
        if scene_has(scene_id, key):
            return False
        adjust_empathy(amount)
        scene_mark(scene_id, key)
        return True

    # =========================
    # ONE-CALL CHOICE (idempotent + ratios + logged)
    # =========================
    def apply_choice_once(scene_id: str,
                        token: str,
                        weight: str,              # "EMP" | "OB" | "NEU"
                        factor: int = 1,
                        next_scene_label: str = "",   # kept for caller convenience; no dev I/O here
                        echelon_delta: int = 0,
                        resistance_delta: int = 0,
                        note: str = None) -> bool:
        """
        RUNTIME ONLY: adjust empathy once, update ratio counters (with idempotent opportunity),
        apply optional reputation deltas. Returns True if the empathy/taken mark applied now.
        No files, no mermaid, no dev logs.
        """
        w = (weight or "NEU").upper()
        # -- 1 Mark the opportunity exactly once --
        if w in ("EMP", "OB"):
            if _mark_once(scene_id, "opp", token):
                if w == "EMP": STATE["player"]["opp_emp"] += 1
                else:          STATE["player"]["opp_ob"]  += 1

        # -- 2 Idempotent empathy/taken mark --
        delta = 0
        if w == "EMP": delta = +abs(int(factor))
        elif w == "OB": delta = -abs(int(factor))

        applied = False
        if delta != 0:
            applied = adjust_empathy_once(scene_id, token, delta)
            if applied:
                if w == "EMP": STATE["player"]["took_emp"] += 1
                else:          STATE["player"]["took_ob"]  += 1
        else:
            # NEU choice recorded once (for flow analytics / gates if you need)
            applied = _mark_once(scene_id, "choice", token)

        # -- 3 Optional rep deltas --
        if echelon_delta:    STATE["rep"]["echelon"]    += int(echelon_delta)
        if resistance_delta: STATE["rep"]["resistance"] += int(resistance_delta)

        # Keep any quick overlay note in memory only (no file I/O)
        if note:
            log_line(f"{scene_id}:{token} -> {w} x{factor} | ΔECH {echelon_delta} ΔRES {resistance_delta} | applied={applied}")

        return applied

    def record_choice_once(scene_id: str, token: str, next_scene_label: str = "", note: str = None) -> bool:
        """
        RUNTIME ONLY: record a neutral branch selection exactly once. No dev I/O.
        """
        return apply_choice_once(scene_id, token, "NEU", factor=0,
                                next_scene_label=next_scene_label, note=note)

    def choice_and_dev(scene_id, token, weight, factor=1,
                    next_scene_label="", echelon_delta=0, resistance_delta=0, note=None):
        """
            Story-safe wrapper:
            1 applies state via apply_choice_once(...)
            2 if a dev hook is installed, mirrors to JSONL/Mermaid (dev only)
        """
        applied = apply_choice_once(scene_id, token, weight, factor=factor,
                                    next_scene_label=next_scene_label,
                                    echelon_delta=echelon_delta, resistance_delta=resistance_delta,
                                    note=note)
        fn = DEV_AFTER_CHOICE
        if fn:
            fn(scene_id, token, weight, factor, applied,
            next_scene_label=next_scene_label,
            echelon_delta=echelon_delta, resistance_delta=resistance_delta)
        return applied

    # =========================
    # NPC MEMORY SYSTEM
    # =========================
    # NPCs remember specific events they witnessed or experienced.
    # Memories have: event key, emotional tone, source scene, optional details.

    def npc_remember(name, event, tone="neutral", detail=None):
        """
        Mark that an NPC experienced/witnessed something.
        
        Args:
            name: Character name (will be normalized)
            event: String key for the event (e.g., "saw_aeron_help_worker")
            tone: Emotional context - "grateful", "suspicious", "angry", "grudging_respect", etc.
            detail: Optional string with extra context
        """
        c = STATE["chars"].get(_c(name))
        if not c:
            return False
        
        if "memory" not in c:
            c["memory"] = []
        
        # Don't duplicate the same event
        if any(m["event"] == event for m in c["memory"]):
            return False
        
        c["memory"].append({
            "event": event,
            "tone": tone,
            "detail": detail,
            "scene": globals().get("_current_scene_id", "unknown")
        })
        return True

    def npc_recalls(name, event):
        """Check if NPC remembers a specific event."""
        c = STATE["chars"].get(_c(name))
        if c and "memory" in c:
            return any(m["event"] == event for m in c["memory"])
        return False

    def npc_recall_tone(name, event):
        """Get the emotional tone of a specific memory. Returns None if not found."""
        c = STATE["chars"].get(_c(name))
        if c and "memory" in c:
            for m in c["memory"]:
                if m["event"] == event:
                    return m.get("tone", "neutral")
        return None

    def npc_memories(name):
        """Get all memories for an NPC. Returns empty list if none."""
        c = STATE["chars"].get(_c(name))
        if c and "memory" in c:
            return list(c["memory"])
        return []

    def npc_has_any_memory(name, *events):
        """Check if NPC remembers ANY of the listed events."""
        for event in events:
            if npc_recalls(name, event):
                return True
        return False

    def npc_has_all_memories(name, *events):
        """Check if NPC remembers ALL of the listed events."""
        for event in events:
            if not npc_recalls(name, event):
                return False
        return True

    def npc_memory_count(name):
        """How many memories does this NPC have of the player?"""
        c = STATE["chars"].get(_c(name))
        if c and "memory" in c:
            return len(c["memory"])
        return 0

    def npc_last_tone(name):
        """Get the tone of the NPC's most recent memory. Useful for 'how did we leave things?'"""
        c = STATE["chars"].get(_c(name))
        if c and "memory" in c and len(c["memory"]) > 0:
            return c["memory"][-1].get("tone", "neutral")
        return "neutral"


    # =========================
    # WORLD STATE SYSTEM
    # =========================
    # Environmental conditions based on aggregate state.
    # Returns tags that scenes can check for descriptive and mechanical changes.

    def world_state():
        """
        Returns a set of environmental condition tags based on current state.
        Scenes can check these for flavor text and content gating.
        """
        tags = set()
        
        # --- Reputation-based ---
        ur = STATE["rep"].get("unders", 0)
        if ur >= 15:
            tags.add("unders_trusted")      # People vouch for you, doors open
        elif ur >= 5:
            tags.add("unders_known")        # Recognized positively, small courtesies
        elif ur >= -5:
            tags.add("unders_neutral")      # Nobody cares, which is fine
        elif ur >= -15:
            tags.add("unders_disliked")     # Cold shoulders, worse prices
        else:
            tags.add("unders_hated")        # Active hostility, some refuse service
        
        rr = STATE["rep"].get("resistance", 0)
        if rr >= 20:
            tags.add("resistance_hero")
        elif rr >= 10:
            tags.add("resistance_trusted")
        elif rr >= 0:
            tags.add("resistance_probation")
        else:
            tags.add("resistance_suspect")
        
        # --- Heat / Danger ---
        alert = STATE["player"].get("echelon_alert", 0)
        if alert >= 10:
            tags.add("heat_critical")       # Lockdowns, constant patrols
        elif alert >= 7:
            tags.add("heat_high")           # Extra drones, checkpoints
        elif alert >= 4:
            tags.add("heat_elevated")       # Noticeable increase in patrols
        else:
            tags.add("heat_normal")
        
        # --- Resource scarcity ---
        food = STATE["inv"]["counters"].get("food", 0)
        water = STATE["inv"]["counters"].get("water", 0)
        
        if food <= 0:
            tags.add("starving")
        elif food <= 1:
            tags.add("hungry")
        
        if water <= 0:
            tags.add("dehydrated")
        elif water <= 1:
            tags.add("thirsty")
        
        if food <= 0 and water <= 0:
            tags.add("desperate")
        
        # --- Alignment visibility ---
        # How others perceive Aeron based on recent behavior
        mom = alignment_momentum()
        if mom > 0.6:
            tags.add("visibly_softening")   # People notice he's different
        elif mom < -0.6:
            tags.add("visibly_hardening")   # People notice the cold
        
        tier = alignment_tier()
        if tier in ("EMP2", "EMP3"):
            tags.add("reputation_compassionate")
        elif tier in ("OB2", "OB3"):
            tags.add("reputation_ruthless")
        
        # --- Time pressure ---
        days = STATE["player"].get("days_remaining", 7)
        if days <= 1:
            tags.add("time_critical")
        elif days <= 3:
            tags.add("time_pressure")
        
        # --- Bounty awareness ---
        bounty = STATE["player"]["bounty"].get("aeron", 0)
        if bounty >= 100000:
            tags.add("bounty_massive")
        elif bounty >= 50000:
            tags.add("bounty_high")
        elif bounty >= 25000:
            tags.add("bounty_moderate")
        
        return tags

    def world_has(*conditions):
        """Check if ANY of the listed world conditions are active."""
        ws = world_state()
        for c in conditions:
            if c in ws:
                return True
        return False

    def world_has_all(*conditions):
        """Check if ALL of the listed world conditions are active."""
        ws = world_state()
        for c in conditions:
            if c not in ws:
                return False
        return True


    # =========================
    # CONTENT GATING SYSTEM
    # =========================
    # Unified checks for whether content is available/locked.
    # Combines reputation, flags, relationships, and world state.

    def can_access(gate_type, target=None, threshold=None):
        """
        Unified content gate check.
        
        Args:
            gate_type: What kind of gate - "vendor", "info", "location", "mission", "dialogue"
            target: Specific target (vendor name, location name, etc.)
            threshold: Optional override for default thresholds
        
        Returns:
            tuple: (allowed: bool, reason: str or None)
        """
        ws = world_state()
        
        if gate_type == "vendor":
            # Vendors may refuse service based on reputation
            if "unders_hated" in ws:
                return (False, "hated")
            if target and npc_recalls(target, "cheated_by_player"):
                return (False, "personal_grudge")
            if target and npc_recalls(target, "threatened_by_player"):
                return (False, "threatened")
            return (True, None)
        
        elif gate_type == "info":
            # Information availability based on trust/reputation
            if "unders_hated" in ws:
                return (False, "no_one_talks")
            if "unders_disliked" in ws:
                # Can get info but it costs more or is unreliable
                return (True, "costs_extra")
            return (True, None)
        
        elif gate_type == "safehouse":
            # Can you use resistance safehouses?
            if "resistance_suspect" in ws:
                return (False, "not_trusted")
            return (True, None)
        
        elif gate_type == "mission":
            # Mission availability often depends on multiple factors
            if target:
                # Check if specific mission is locked by flags
                if scene_has("missions", f"{target}_locked"):
                    return (False, "locked")
                if scene_has("missions", f"{target}_completed"):
                    return (False, "completed")
            return (True, None)
        
        # Default: allowed
        return (True, None)

    def gate_check(gate_type, target=None):
        """Simple boolean version of can_access."""
        allowed, _ = can_access(gate_type, target)
        return allowed

    def gate_reason(gate_type, target=None):
        """Get just the reason string (or None if allowed)."""
        _, reason = can_access(gate_type, target)
        return reason


    # =========================
    # ENCOUNTER TRACKING
    # =========================
    # Track how many times player has interacted with an NPC.

    def encounter_inc(name):
        """Increment encounter count with an NPC."""
        c = STATE["chars"].get(_c(name))
        if c:
            if "encounters" not in c:
                c["encounters"] = 0
            c["encounters"] += 1
            return c["encounters"]
        return 0

    def encounter_count(name):
        """Get number of encounters with an NPC."""
        c = STATE["chars"].get(_c(name))
        if c:
            return c.get("encounters", 0)
        return 0

    def first_encounter(name):
        """Is this the first time meeting this NPC?"""
        return encounter_count(name) == 0

    def met_before(name):
        """Have we met this NPC before?"""
        return encounter_count(name) > 0


    # =========================
    # REACTIVE FLAVOR HELPERS
    # =========================
    # Shorthand for common reactive patterns.

    def react_if(condition, text_true, text_false=""):
        """
        Simple conditional text helper.
        Returns text_true if condition is truthy, else text_false.
        """
        return text_true if condition else text_false

    def react_rep(faction, high_text, mid_text, low_text):
        """
        Return text based on faction reputation tier.
        High: >= 10, Mid: -5 to 9, Low: < -5
        """
        r = STATE["rep"].get(faction, 0)
        if r >= 10:
            return high_text
        elif r >= -5:
            return mid_text
        else:
            return low_text

    def react_trust(name, high_text, mid_text, low_text):
        """
        Return text based on NPC trust level.
        High: >= 7, Mid: 3-6, Low: < 3
        """
        t = trust(name)
        if t >= 7:
            return high_text
        elif t >= 3:
            return mid_text
        else:
            return low_text


    # =========================
    # EXAMPLE USAGE PATTERNS
    # =========================
    #
    # --- NPC Memory ---
    # When something happens:
    #   $ npc_remember("foreman_rusk", "stopped_line_for_worker", tone="grudging_respect")
    #   $ npc_remember("vendor_marta", "bought_at_fair_price", tone="neutral")
    #   $ npc_remember("vendor_marta", "haggled_aggressively", tone="annoyed")
    #
    # Later, checking:
    #   if npc_recalls("foreman_rusk", "stopped_line_for_worker"):
    #       foreman "Still playing hero, Voss?"
    #
    #   if npc_last_tone("vendor_marta") == "annoyed":
    #       "She doesn't smile when she sees you."
    #
    # --- World State ---
    # At scene moments where environment matters:
    #   if world_has("unders_hated"):
    #       "The vendor's hand moves under the counter. Not a greeting."
    #
    #   if world_has("heat_high"):
    #       "Drone shadows pass overhead twice as often as yesterday."
    #
    #   if world_has("hungry", "thirsty"):
    #       "His stomach cramps. They've been rationing for two days."
    #
    # --- Content Gating ---
    # Before offering content:
    #   if gate_check("vendor", "marta"):
    #       menu:
    #           "Buy supplies":
    #               ...
    #   else:
    #       vendor "I don't sell to your kind."
    #
    #   $ allowed, reason = can_access("info")
    #   if not allowed:
    #       "Nobody here will talk to you."
    #   elif reason == "costs_extra":
    #       "Information costs double when nobody trusts you."
    #
    # --- Encounter Tracking ---
    # Scene start:
    #   $ encounter_inc("doc_mara")
    #   if first_encounter("doc_mara"):
    #       "A woman in a stained coat looks up from her work."
    #   else:
    #       "Doc Mara nods when she sees you. She remembers."
    #


    # =========================
    # OPERATIONS SNAPSHOT (start/end)
    # =========================
    def op_start(op_id, note=None):
        p = STATE["player"]; snaps = STATE["scenes"]["snapshots"]
        snaps[op_id] = {
            "note": note or "",
            "civ_saved0": p["civilians_saved"],
            "civ_killed0": p["civilians_killed"],
            "mercy0":      p["evidence_of_mercy"],
            "sus0":        p["team_suspicion"],
            "emp0":        p["empathy_score"],
        }

    def _apply_rep(saved_d, killed_d, mercy_d, sus_d):
        rep = STATE["rep"]
        rep["unders"]     += (saved_d // 10) + (1 if mercy_d >= 2 else 0) - (killed_d // 50)
        rep["resistance"] += (mercy_d // 1)  + (saved_d // 25) - (killed_d // 100)
        rep["echelon"]    += (killed_d // 25) - (sus_d // 2) - (mercy_d // 2)
        STATE["player"]["echelon_alert"] = max(0, STATE["player"]["echelon_alert"] + sus_d // 3)

    def _push_stats(saved_d, killed_d):
        STATE["stats"]["people_saved"]  += max(0, saved_d)
        STATE["stats"]["people_killed"] += max(0, killed_d)

    def op_end(op_id, tag=None, apply_stats=True, apply_rep=True):
        snaps = STATE["scenes"]["snapshots"]; snap = snaps.get(op_id, None)
        p = STATE["player"]
        if not snap:
            snap = {"civ_saved0":0, "civ_killed0":0, "mercy0":0, "sus0":0, "emp0":p["empathy_score"]}

        d_saved = max(0, p["civilians_saved"] - snap["civ_saved0"])
        d_kill  = max(0, p["civilians_killed"] - snap["civ_killed0"])
        d_mercy = max(0, p["evidence_of_mercy"] - snap["mercy0"])
        d_sus   = max(0, p["team_suspicion"] - snap["sus0"])

        if apply_stats: _push_stats(d_saved, d_kill)
        if apply_rep:   _apply_rep(d_saved, d_kill, d_mercy, d_sus)

        label = tag or snap.get("note") or op_id
        band = empathy_band(); tier = alignment_tier()
        summary = f"[{label}] +saved {d_saved}, +killed {d_kill}, +mercy {d_mercy}, +sus {d_sus} → {band}/{tier}"
        snaps[op_id] = { **snap, "summary": summary }
        return summary

    # =========================
    # CANON GLUE
    # =========================
    def set_base_location(loc): STATE["canon"]["base_location"] = loc
    def base_location():        return STATE["canon"]["base_location"]
    def canon_set(k, v=True):   STATE["canon"][k] = v
    def canon_get(k, d=False):  return STATE["canon"].get(k, d)

    # =========================
    # COMMON STORY PREDICATES
    # =========================
    def zira_ready_for_kiss():
        return (trust("Zira") >= 6 and
                loyalty("Zira") >= 8 and
                flag_has("Zira","vulnerability_scene_completed") and
                STATE["canon"].get("empathy_shown", False))

    def zira_kiss_happened(): return flag_has("Zira","kiss_happened")
    def lyra_lewd_done():     return flag_has("Lyra","lewd_scene_completed")

    # =========================
    # LOGGING (for quick overlay)
    # =========================
    def log_line(text):
        q = STATE["sys"]["logs"]
        q.append(str(text))
        if len(q) > 12: del q[:len(q)-12]
    
    # ---------- Foundations / schema ----------
    STATE_SCHEMA_VERSION = 2  # bump if you change structure

    def is_dev_build() -> bool:
        # True ONLY when Ren'Py developer mode is on
        return bool(getattr(config, "developer", False))

    # Top-level, author-friendly facades (doesn't change your existing shape)
    STATE.setdefault("flags", {})     # generic story flags (soft/one-off)
    STATE.setdefault("metrics", {})   # counters that aren't "stats"

    def flag(k, v=None):
        if v is None:
            return bool(STATE["flags"].get(k, False))
        STATE["flags"][k] = bool(v)

    def metric(k, delta=0, set_to=None):
        if set_to is not None:
            STATE["metrics"][k] = int(set_to)
        else:
            STATE["metrics"][k] = int(STATE["metrics"].get(k, 0)) + int(delta)
        return STATE["metrics"][k]

    def ensure_schema_migrations():
        # Example guard expansion; add real migrations as you evolve
        STATE.setdefault("flags", {})
        STATE.setdefault("metrics", {})
        sys = STATE.setdefault("sys", {})
        sys.setdefault("edges_seen", set())
        sys.setdefault("telemetry_on", True)

    if ensure_schema_migrations not in config.after_load_callbacks:
        config.after_load_callbacks.append(ensure_schema_migrations)