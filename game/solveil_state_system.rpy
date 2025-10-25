# solveil_state_system.rpy
# Ashes of Solveil – Consolidated State Architecture (BC-safe)

init python:
    # =========================
    # CORE DICTS (kept + extended)
    # =========================

    # ---- CHARACTERS ----
    # Keep original keys (trust/affection/etc.) to avoid breaking old scripts.
    # Add "flags" (toggle), "milestones" (one-way), and keep "notes".
    characters = {
        "Lyra": {
            "met": True, "trust": 1, "affection": 0,
            "romance_path": False, "lewd_scene_unlocked": False, "lewd_scene_completed": False,
            "notes": [], "flags": set(), "milestones": set()
        },
        "Zira": {
            "met": False, "trust": 0, "loyalty": 0,
            "romance_path": False, "lewd_scene_unlocked": False, "lewd_scene_completed": False,
            "vulnerability_scene_completed": False, "backstory_revealed": False,
            "knows_about_kai": False, "contacted_in_scene1": False,
            "notes": [], "flags": set(), "milestones": set()
        },
        "Tessa": {
            "met": False, "trust": 0, "affection": 0, "romance_path": False,
            "names_saved": [], "mercy_death_scene": False,
            "notes": [], "flags": set(), "milestones": set()
        },
        "Noelle": {
            "met": False, "trust": 0, "affection": 0, "romance_path": False,
            "discovery_scene_completed": False, "knows_glass": False, "aeron_honest": False, "no_unit_scene": False,
            "notes": [], "flags": set(), "milestones": set()
        },
        "Selene": { "met": False, "trust": 0, "affection": 0, "romance_path": False, "notes": [], "flags": set(), "milestones": set() },
        "doc_mara": { "met": False, "trust": 0, "skills": ["medical","intel"], "favor_owed": False, "notes": [], "flags": set(), "milestones": set() },
    }

    # ---- SCENES ----
    # Keep original structure for safety, but prefer scene_flags (set per scene_id).
    scenes = {
        "act1_05_gala": { "acknowledge_daren": False },
        "act1_17_sweep": { "choice": 0, "civilians_saved": 0, "player_hesitated": False },
        "act2_activity": { "work": False,"weapons": False,"intel": False,"medical": False,"reputation": False,"skills": False,"past": False,"count_completed": 0,"required": 7 },
        "special_scenes": {
            "lyra_rooftop": { "visited": False, "romance_attempted": False },
            "selene_meeting": { "triggered": False }
        }
    }
    scene_flags = {}  # New: e.g., scene_flags["act1_18b_morning"] = {"hugged_lyra","completed"}

    # ---- INVENTORY ----
    # Keep originals; also add presence-sets for tools/disguises and a counters bucket.
    inventory = {
        "credits": 150, "scrip": 0,
        "favors_owed": [], "debts_owed": [],
        "supplies": { "medkits":0, "stims":0, "food":3, "water":3, "cigs":0, "alcohol":0 },
        "weapons": [],
        "tools": { "lockpicks": False, "hacking_device": False, "binoculars": False },
        "disguises": { "under_clothes": False, "mid_disguise": False, "echelon_uniform": False },
        "intel": { "documents": [], "maps": [], "secrets": [] },

        # New normalized mirrors
        "counters": { "medkits":0, "stims":0, "food":3, "water":3, "cigs":0, "alcohol":0 },
        "tools_set": set(),        # e.g., {"lockpicks","hacking_device"}
        "disguises_set": set(),    # e.g., {"unders","mid","echelon"}
    }
    # Migrate booleans to sets at boot:
    for k,v in list(inventory["tools"].items()):
        if v: inventory["tools_set"].add(k)
    d = inventory["disguises"]
    if d.get("under_clothes"):   inventory["disguises_set"].add("unders")
    if d.get("mid_disguise"):    inventory["disguises_set"].add("mid")
    if d.get("echelon_uniform"): inventory["disguises_set"].add("echelon")

    # ---- REPUTATION / SKILLS / PLAYER / CANON / STATS / SYSTEM ----
    reputation = { "unders": -5, "resistance": 0, "echelon": -100 }
    skills = { "unders_disguise": False, "pattern_recognition": False }   # legacy dict
    skills_set = set(k for k,v in skills.items() if v)                    # normalized set

    player_state = {
        "fake_names": { "aeron":"Kade Voss", "lyra":"Mira Chen" },
        "days_remaining": 7,
        "bounty": { "aeron":50000, "lyra":50000 },
        "echelon_alert": 0,
        "empathy_score": -5,
        "evidence_of_mercy": 0,
        "team_suspicion": 0,
        "civilians_saved": 0,
        "civilians_killed": 0,
        # momentum tracker
        "recent_empathy": [],
    }

    canon = { "act1_complete": False, "purge_witnessed": False, "glass_shattered": False, "defected": False, "met_selene": False, "resistance_joined": False }
    stats = { "people_saved": 0, "people_killed": 600, "resistance_strength": 0, "major_victories": 0, "major_losses": 0 }
    system_flags = { "debug_mode": False, "skip_activities": False, "show_activity_hub": False, "show_inventory": False, "show_map": False }

    # =========================
    # HELPERS (BC-safe)
    # =========================
    # Character metrics
    def add_trust(name, amount):     characters[name]["trust"] += amount
    def add_affection(name, amount): characters[name]["affection"] += amount
    def add_loyalty(name, amount):   characters[name]["loyalty"] = characters[name].get("loyalty",0) + amount
    def unlock_romance(name):        characters[name]["romance_path"] = True
    def is_met(name):                return characters[name]["met"]
    def relationship_state(name):
        t = characters[name].get("trust", 0); a = characters[name].get("affection", 0)
        if t < 0: return "hostile"
        if a >= 3 and t >= 2: return "romantic"
        if a >= 2 and t >= 1: return "friend"
        return "neutral"

    # Character flags/milestones/notes
    def char_flag_on(name, key):  characters[name]["flags"].add(key)
    def char_flag_has(name, key): return key in characters[name]["flags"]
    def char_ms_add(name, key):   characters[name]["milestones"].add(key)
    def char_ms_has(name, key):   return key in characters[name]["milestones"]
    def char_note(name, text):    characters[name]["notes"].append(text)

    # Scenes (new unified) + BC wrappers
    def set_scene_flag(scene_id, key):
        scene_flags.setdefault(scene_id, set()).add(key)
        # Also mirror to legacy scenes dict if the group exists
        if scene_id in scenes and isinstance(scenes[scene_id], dict):
            scenes[scene_id][key] = True
    def check_scene_flag(scene_id, key):
        if key in scene_flags.get(scene_id, set()): return True
        return scenes.get(scene_id, {}).get(key, False)

    # Inventory
    def add_item(category, item, qty=1):
        # BC: support old categories
        if category == "supplies":
            inventory["supplies"][item] = inventory["supplies"].get(item, 0) + qty
            inventory["counters"][item] = inventory["counters"].get(item, 0) + qty
        elif category == "tools":
            inventory["tools"][item] = True
            inventory["tools_set"].add(item)
        elif category == "disguises":
            inventory["disguises"][item] = True
            # map legacy names to set names
            alias = {"under_clothes":"unders","mid_disguise":"mid","echelon_uniform":"echelon"}.get(item, item)
            inventory["disguises_set"].add(alias)
        else:
            inventory.setdefault(category, [])
            inventory[category].append(item)
    def has_item(category, item):
        if category == "supplies": return inventory["supplies"].get(item,0) > 0
        if category == "tools":    return item in inventory["tools_set"] or inventory["tools"].get(item, False)
        if category == "disguises":
            alias = {"under_clothes":"unders","mid_disguise":"mid","echelon_uniform":"echelon"}.get(item, item)
            return alias in inventory["disguises_set"] or inventory["disguises"].get(item, False)
        return item in inventory.get(category, [])
    def add_item_counter(item, qty=1):
        inventory["counters"][item] = inventory["counters"].get(item, 0) + qty
        inventory["supplies"][item] = inventory["supplies"].get(item, 0) + qty
    def grant_tool(tool):     inventory["tools"][tool] = True; inventory["tools_set"].add(tool)
    def has_tool(tool):       return tool in inventory["tools_set"]
    def grant_disguise(k):    inventory["disguises_set"].add(k)
    def has_disguise(k):      return k in inventory["disguises_set"]
    def add_favor(person):    inventory["favors_owed"].append(person)
    def pay_debt(person):
        if person in inventory["debts_owed"]:
            inventory["debts_owed"].remove(person)

    # Reputation / Stats / Skills
    def inc_rep(faction, amt): reputation[faction] = reputation.get(faction, 0) + amt
    def inc_stat(key, amt=1): stats[key] = stats.get(key, 0) + amt
    def learn_skill(key):     skills_set.add(key)
    def has_skill(key):       return key in skills_set

    # Player counters
    def add_evidence_of_mercy(amount=1): player_state["evidence_of_mercy"] += amount
    def add_team_suspicion(amount=1):    player_state["team_suspicion"] += amount
    def add_civilians_saved(amount=1):   player_state["civilians_saved"] += amount
    def add_civilians_killed(amount=1):  player_state["civilians_killed"] += amount

    # =========================
    # ALIGNMENT / EMP–OB
    # =========================
    EMPATHY_MIN = -12; EMPATHY_MAX = 12; EMP_EDGE = 3
    RECENT_N = 6

    def _push_recent(delta):
        arr = player_state["recent_empathy"]
        arr.append(int(delta))
        if len(arr) > RECENT_N:
            del arr[0:len(arr)-RECENT_N]

    def adjust_empathy(amount):
        # basic, BC-safe adjust (no softcap math to keep deterministic unless you add it)
        _push_recent(amount)
        player_state["empathy_score"] = max(EMPATHY_MIN, min(EMPATHY_MAX, player_state.get("empathy_score",0) + amount))

    # Once-only award registry (session)
    once_registry = set()
    def adjust_empathy_once(event_id, amount):
        if event_id in once_registry: return
        once_registry.add(event_id)
        adjust_empathy(amount)

    # Reads
    def get_alignment_score_norm():
        s = float(max(EMPATHY_MIN, min(EMPATHY_MAX, player_state.get("empathy_score",0))))
        return s / float(EMPATHY_MAX)
    def get_empathy_band():
        s = player_state.get("empathy_score",0)
        if s >= EMP_EDGE: return "empathy"
        if s <= -EMP_EDGE: return "obedience"
        return "conflicted"
    def aeron_alignment(): return get_empathy_band()
    def get_alignment_tier():
        s = int(player_state.get("empathy_score",0))
        if s <= -9: return "OB3"
        if s <= -5: return "OB2"
        if s <= -1: return "OB1"
        if s == 0:  return "C"
        if s <= 4:  return "EMP1"
        if s <= 8:  return "EMP2"
        return "EMP3"
    def get_alignment_descriptor():
        return {
            "OB3":"Iron Obedience","OB2":"Hard Obedience","OB1":"Leaning Obedience",
            "C":"Conflicted","EMP1":"Leaning Empathy","EMP2":"Strong Empathy","EMP3":"Conviction Empathy"
        }[get_alignment_tier()]
    def get_alignment_momentum():
        arr = player_state.get("recent_empathy", [])
        if not arr: return 0.0
        total = sum(arr); max_sum = max(1.0, RECENT_N * 3.0)
        return max(-1.0, min(1.0, total / max_sum))
    def pass_emp_gate(min_edge=EM_EDGE if 'EM_EDGE' in globals() else EMP_EDGE):
        return player_state.get("empathy_score",0) >= EMP_EDGE
    def pass_ob_gate(max_edge=-EM_EDGE if 'EM_EDGE' in globals() else -EMPATHY_MAX):
        return player_state.get("empathy_score",0) <= -EM_EDGE if 'EM_EDGE' in globals() else player_state.get("empathy_score",0) <= -EMPATHY_MAX
    def pass_tier(*tiers): return get_alignment_tier() in tiers

    # Convenience sugar
    def mark_flag(name, key):    characters[name]["flags"].add(key)
    def mark_ms(name, key):      characters[name]["milestones"].add(key)
    def mark_scene(scene_id, key): set_scene_flag(scene_id, key)
    def rel(name, trust=0, affection=0, loyalty=0):
        if trust: add_trust(name, trust)
        if affection: add_affection(name, affection)
        if loyalty: add_loyalty(name, loyalty)

    # =============================
    # OPERATION RECONCILIATION KIT
    # =============================

    # Where we store start-of-scene snapshots
    if "op_snapshots" not in scenes:
        scenes["op_snapshots"] = {}

    def start_operation(op_id, note=None):
        """
        Snapshot current counters at the start of a mission/scene.
        op_id: unique string, e.g. "op391_sector10"
        """
        scenes["op_snapshots"][op_id] = {
            "note": note or "",
            "civ_saved0": player_state.get("civilians_saved", 0),
            "civ_killed0": player_state.get("civilians_killed", 0),
            "mercy0":      player_state.get("evidence_of_mercy", 0),
            "sus0":        player_state.get("team_suspicion", 0),
            "emp0":        player_state.get("empathy_score", 0),
        }

    def _clamp_empathy():
        # Use your global EMPATHY_MIN/MAX if present; else soft defaults
        lo = globals().get("EMPATHY_MIN", -12)
        hi = globals().get("EMPATHY_MAX",  12)
        s = player_state.get("empathy_score", 0)
        player_state["empathy_score"] = max(lo, min(hi, s))

    def _apply_reputation(saved_delta, killed_delta, mercy_delta, suspicion_delta, auto=True):
        """
        Simple, tunable reputation model. Tweak to taste.
        """
        if not auto:
            return

        # Baselines
        rep = reputation
        # Help Unders when you save + show mercy; hurt when you massacre
        rep["unders"]     += (saved_delta // 10) + (1 if mercy_delta >= 2 else 0) - (killed_delta // 50)
        # Resistance likes mercy; dislikes mass-kill claims
        rep["resistance"] += (mercy_delta // 1) + (saved_delta // 25) - (killed_delta // 100)
        # Echelon dislikes visible deviation; likes ruthless efficiency
        rep["echelon"]    += (killed_delta // 25) - (suspicion_delta // 2) - (mercy_delta // 2)

        # Very simple alert coupling (optional)
        player_state["echelon_alert"] = max(0, player_state.get("echelon_alert", 0) + suspicion_delta // 3)

    def _push_stats(saved_delta, killed_delta):
        stats["people_saved"]  = stats.get("people_saved", 0)  + max(0, saved_delta)
        stats["people_killed"] = stats.get("people_killed", 0) + max(0, killed_delta)

    def _canon_touches(op_id, saved_delta, killed_delta):
        # Example auto-canon flip; adjust to your story beats
        if "sector10" in op_id and killed_delta >= 200:
            canon["purge_witnessed"] = True

    def end_operation(
        op_id,
        tag=None,
        auto_stats=True,
        auto_repute=True,
        clamp_empathy=True,
        mark_canon=True
    ):
        """
        Reconcile post-scene totals vs. snapshot and return a one-line summary.
        Call this ONCE at the end of a mission/scene that manipulated counts.

        Returns: summary string, and also stores it in scenes['op_snapshots'][op_id]['summary'].
        """
        snap = scenes["op_snapshots"].get(op_id)
        if not snap:
            # If start_operation wasn't called, treat all as delta from zero.
            snap = {
                "civ_saved0": 0, "civ_killed0": 0, "mercy0": 0, "sus0": 0, "emp0": player_state.get("empathy_score",0)
            }

        # Compute deltas
        saved_now = player_state.get("civilians_saved", 0)
        killed_now= player_state.get("civilians_killed", 0)
        mercy_now = player_state.get("evidence_of_mercy", 0)
        sus_now   = player_state.get("team_suspicion", 0)

        d_saved   = max(0, saved_now - snap["civ_saved0"])
        d_killed  = max(0, killed_now - snap["civ_killed0"])
        d_mercy   = max(0, mercy_now - snap["mercy0"])
        d_sus     = max(0, sus_now   - snap["sus0"])

        if auto_stats:  _push_stats(d_saved, d_killed)
        if auto_repute: _apply_reputation(d_saved, d_killed, d_mercy, d_sus, auto=True)
        if clamp_empathy: _clamp_empathy()
        if mark_canon:  _canon_touches(op_id, d_saved, d_killed)

        # Friendly label
        label = tag or snap.get("note") or op_id

        # Compose summary
        band = get_empathy_band()
        tier = get_alignment_tier()
        summary = (
            f"[{label}] saved +{d_saved}, killed +{d_killed}, mercy +{d_mercy}, sus +{d_sus} "
            f"→ Band:{band} Tier:{tier}  | Totals S:{saved_now} K:{killed_now}"
        )

        # Store & return
        scenes["op_snapshots"][op_id] = { **snap, "summary": summary }
        return summary

    # Optional: quick logger to your debug overlay queue (if you have one)
    if "logs" not in system_flags:
        system_flags["logs"] = []

    def log_line(text):
        system_flags["logs"].append(str(text))
        # keep last ~12 lines
        if len(system_flags["logs"]) > 12:
            del system_flags["logs"][:len(system_flags["logs"]) - 12]

# ========== DEBUG OVERLAY ==========
screen solveil_debug_overlay():
    if system_flags["debug_mode"]:
        frame:
            style "default"
            xalign 0.01
            yalign 0.01
            has vbox
            text "DEBUG MODE: ON" size 16 color "#00ff00"
            text "Lyra Trust: [characters['Lyra']['trust']]" size 12
            text "Zira Loyalty: [characters['Zira'].get('loyalty',0)]" size 12
            text "Reputation (Unders): [reputation['unders']]" size 12
            text "Credits: [inventory['credits']]" size 12
            text "Days Remaining: [player_state['days_remaining']]" size 12
            $ s  = player_state['empathy_score']
            $ b  = get_empathy_band()
            $ t  = get_alignment_tier()
            $ m  = round(get_alignment_momentum(), 2)
            text "Empathy: [s]  Band: [b]  Tier: [t]  Momentum: [m]" size 12

# Enable overlay globally
init python:
    if "solveil_debug_overlay" not in config.overlay_screens:
        config.overlay_screens.append("solveil_debug_overlay")
