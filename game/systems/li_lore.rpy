# ================================================================
# LI LORE DIALOGUE SYSTEM — optional "ask about..." menus
# File: game/systems/li_lore.rpy
# ----------------------------------------------------------------
# At the end of certain emotional/quiet scenes, the player can
# optionally ask an LI about a lore topic. Each answer is a short
# dialogue exchange (5-15 lines) that advances a codex stage.
#
# Usage in scene files (before `return`):
#     call li_lore_check("Lyra") from _a3_s03_lore
#
# The check function looks up which topics are available for that
# LI at the current scene, filters out topics already asked, and
# shows a looping menu if any remain. If none remain, it passes
# through silently.
# ================================================================

init python:

    # ---------------------------------------------------------------
    # TOPIC REGISTRY
    # ---------------------------------------------------------------
    # Each topic maps to:
    #   li         — which LI offers this topic
    #   label      — short name used in the menu prompt
    #   dialogue   — Ren'Py label to call for the exchange
    #   codex_id   — codex entry to reveal/advance
    #   codex_stage— target stage for codex_reveal
    #   flag       — flag key set after asking (prevents re-offering)
    #   scenes     — list of scene_id prefixes where this topic is
    #                available (matched via startswith so "a3_s03"
    #                matches "a3_s03_breath_of_faith_emp")
    # ---------------------------------------------------------------

    LI_LORE_TOPICS = {
        # === LYRA (4 topics) ===
        "lyra_old_tongue": {
            "li": "Lyra", "label": "the Old Tongue",
            "dialogue": "lore_lyra_old_tongue",
            "codex_id": "lineages", "codex_stage": 1,
            "flag": "lore_lyra_old_tongue",
            "scenes": ["a3_s03", "a3_s17", "a4_s04", "a4_s11a"],
        },
        "lyra_the_six": {
            "li": "Lyra", "label": "the Six",
            "dialogue": "lore_lyra_the_six",
            "codex_id": "bands", "codex_stage": 1,
            "flag": "lore_lyra_the_six",
            "scenes": ["a3_s05", "a3_s08", "a4_s04", "a4_s19"],
        },
        "lyra_the_band": {
            "li": "Lyra", "label": "the Band",
            "dialogue": "lore_lyra_the_band",
            "codex_id": "tier_hall_branding", "codex_stage": 2,
            "flag": "lore_lyra_the_band",
            "scenes": ["a3_s17", "a4_s04", "a4_s11a"],
        },
        "lyra_cathedral": {
            "li": "Lyra", "label": "the Cathedral",
            "dialogue": "lore_lyra_cathedral",
            "codex_id": "harmony_cores", "codex_stage": 1,
            "flag": "lore_lyra_cathedral",
            "scenes": ["a3_s05", "a3_s08", "a4_s19"],
        },

        # === ZIRA (4 topics) ===
        "zira_ghostline": {
            "li": "Zira", "label": "the Ghostline",
            "dialogue": "lore_zira_ghostline",
            "codex_id": "ghostline", "codex_stage": 1,
            "flag": "lore_zira_ghostline",
            "scenes": ["a3_s15", "a4_s08", "a4_s09a"],
        },
        "zira_unders": {
            "li": "Zira", "label": "the Unders",
            "dialogue": "lore_zira_unders",
            "codex_id": "solveil_tiers", "codex_stage": 1,
            "flag": "lore_zira_unders",
            "scenes": ["a3_s04", "a3_s15", "a4_s08"],
        },
        "zira_beacon_chip": {
            "li": "Zira", "label": "the Beacon Chip",
            "dialogue": "lore_zira_beacon_chip",
            "codex_id": "beacon_chip", "codex_stage": 1,
            "flag": "lore_zira_beacon_chip",
            "scenes": ["a3_s15", "a4_s08"],
        },
        "zira_couriers": {
            "li": "Zira", "label": "courier networks",
            "dialogue": "lore_zira_couriers",
            "codex_id": "ghost_hop", "codex_stage": 1,
            "flag": "lore_zira_couriers",
            "scenes": ["a3_s18b", "a3_s20", "a4_s08"],
        },

        # === TESSA (3 topics) ===
        "tessa_the_board": {
            "li": "Tessa", "label": "the Board",
            "dialogue": "lore_tessa_the_board",
            "codex_id": "rule_of_three", "codex_stage": 1,
            "flag": "lore_tessa_the_board",
            "scenes": ["a3_s13", "a3_s18", "a4_s06", "a4_s12"],
        },
        "tessa_foundry_wards": {
            "li": "Tessa", "label": "the Foundry Wards",
            "dialogue": "lore_tessa_foundry_wards",
            "codex_id": "solveil_tiers", "codex_stage": 2,
            "flag": "lore_tessa_foundry_wards",
            "scenes": ["a3_s05", "a3_s13", "a4_s05a"],
        },
        "tessa_field_medicine": {
            "li": "Tessa", "label": "field medicine",
            "dialogue": "lore_tessa_field_medicine",
            "codex_id": "phoenix_rebellion", "codex_stage": 1,
            "flag": "lore_tessa_field_medicine",
            "scenes": ["a3_s13", "a4_s05a", "a4_s12"],
        },

        # === NOELLE (3 topics) ===
        "noelle_cognitive_arch": {
            "li": "Noelle", "label": "Echelon's cognitive architecture",
            "dialogue": "lore_noelle_cognitive_arch",
            "codex_id": "echelon", "codex_stage": 1,
            "flag": "lore_noelle_cognitive_arch",
            "scenes": ["a3_s08", "a3_s11", "a4_s09"],
        },
        "noelle_compliance": {
            "li": "Noelle", "label": "the compliance framework",
            "dialogue": "lore_noelle_compliance",
            "codex_id": "echelon", "codex_stage": 2,
            "flag": "lore_noelle_compliance",
            "scenes": ["a3_s11", "a3_s19", "a4_s09"],
        },
        "noelle_name_mechanic": {
            "li": "Noelle", "label": "the Name Mechanic",
            "dialogue": "lore_noelle_name_mechanic",
            "codex_id": "noelle_korr", "codex_stage": 2,
            "flag": "lore_noelle_name_mechanic",
            "scenes": ["a3_s11", "a4_s13a", "a4_s18"],
        },

        # === SELENE (3 topics, EMP only) ===
        "selene_kael": {
            "li": "Selene", "label": "Kael",
            "dialogue": "lore_selene_kael",
            "codex_id": "kael_rylan", "codex_stage": 2,
            "flag": "lore_selene_kael",
            "scenes": ["a3_s14", "a3_s16", "a4_s10", "a4_s12a"],
        },
        "selene_nineteen_years": {
            "li": "Selene", "label": "the nineteen-year war",
            "dialogue": "lore_selene_nineteen_years",
            "codex_id": "phoenix_rebellion", "codex_stage": 2,
            "flag": "lore_selene_nineteen_years",
            "scenes": ["a3_s06", "a3_s14", "a4_s10"],
        },
        "selene_shared_command": {
            "li": "Selene", "label": "shared command",
            "dialogue": "lore_selene_shared_command",
            "codex_id": "selene_valen", "codex_stage": 2,
            "flag": "lore_selene_shared_command",
            "scenes": ["a3_s14", "a4_s10", "a4_s12a"],
        },

        # === NYRA (3 topics, OB only) ===
        "nyra_order_division": {
            "li": "Nyra", "label": "Order Division",
            "dialogue": "lore_nyra_order_division",
            "codex_id": "echelon", "codex_stage": 3,
            "flag": "lore_nyra_order_division",
            "scenes": ["a3_s06", "a3_s07", "a4_s07"],
        },
        "nyra_purge_inside": {
            "li": "Nyra", "label": "the Purge from the inside",
            "dialogue": "lore_nyra_purge_inside",
            "codex_id": "purge_8_10", "codex_stage": 1,
            "flag": "lore_nyra_purge_inside",
            "scenes": ["a3_s07", "a3_s12", "a4_s07"],
        },
        "nyra_doctrine": {
            "li": "Nyra", "label": "doctrine",
            "dialogue": "lore_nyra_doctrine",
            "codex_id": "nyra", "codex_stage": 2,
            "flag": "lore_nyra_doctrine",
            "scenes": ["a3_s12", "a4_s07", "a4_s11"],
        },
    }

    # ---------------------------------------------------------------
    # HELPERS
    # ---------------------------------------------------------------

    def _lore_topics_for(li_name, scene_id):
        """Return list of topic dicts available for `li_name` at the
        current scene. Filters out already-asked topics."""
        available = []
        for tid, t in LI_LORE_TOPICS.items():
            if t["li"] != li_name:
                continue
            # Already asked?
            if flag(t["flag"]):
                continue
            # Available at this scene? (prefix match)
            if not any(scene_id.startswith(prefix) for prefix in t["scenes"]):
                continue
            available.append(t)
        return available

    def _has_lore_topics(li_name, scene_id):
        """True if at least one lore topic is available."""
        return len(_lore_topics_for(li_name, scene_id)) > 0


# ----------------------------------------------------------------
# LORE CHECK LABEL — called from scene files
# ----------------------------------------------------------------
# Usage: call li_lore_check("Lyra") from _a3_s03_lore
# Passes through silently if no topics are available.

label li_lore_check(li_name):
    $ _scene = _current_scene_id
    $ _topics = _lore_topics_for(li_name, _scene)
    if not _topics:
        return

    # Show the lore menu — loops until player picks "Continue"
    label .lore_loop:
        $ _topics = _lore_topics_for(li_name, _scene)
        if not _topics:
            return

        menu:
            "Before you go..."

            "Ask [li_name] about [_topics[0]['label']]." if len(_topics) >= 1:
                $ _t = _topics[0]
                call expression _t["dialogue"] from _lore_d0
                $ flag(_t["flag"], True)
                $ codex_reveal(_t["codex_id"], to_stage=_t["codex_stage"], source="lore_dialogue")
                jump .lore_loop

            "Ask [li_name] about [_topics[1]['label']]." if len(_topics) >= 2:
                $ _t = _topics[1]
                call expression _t["dialogue"] from _lore_d1
                $ flag(_t["flag"], True)
                $ codex_reveal(_t["codex_id"], to_stage=_t["codex_stage"], source="lore_dialogue")
                jump .lore_loop

            "Ask [li_name] about [_topics[2]['label']]." if len(_topics) >= 3:
                $ _t = _topics[2]
                call expression _t["dialogue"] from _lore_d2
                $ flag(_t["flag"], True)
                $ codex_reveal(_t["codex_id"], to_stage=_t["codex_stage"], source="lore_dialogue")
                jump .lore_loop

            "Continue.":
                return
