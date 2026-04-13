# ================================================================
# CHARACTER PROFILES — data layer for the Characters screen
# File: game/data/character_profiles.rpy
# ----------------------------------------------------------------
# Canonical profile data for every character that gets a card on
# the Characters screen. Consumed by:
#
#   - game/ui/character_screens.rpy   (card grid + detail view)
#   - game/codex/codex_system.rpy     (cross-link to codex entries)
#   - game/systems/scene_gallery.rpy  (scene list per character)
#
# Each profile has:
#   - display_name       shown on the card header
#   - tab                "love_interests" | "supporting"
#   - order              sort index within the tab
#   - accent             hex color for the card border / name tint
#   - tagline            one-line flavor under the name
#   - portrait           image path (Solid fallback if not loadable)
#   - basic_info         list of (label, value) tuples for the card
#   - codex_entries      list of codex IDs that expand this character
#   - scenes             list of scene dicts for the replay gallery
#
# Scene dict shape:
#   id            unique scene key (usually same as Ren'Py label)
#   label         Ren'Py label to call_replay
#   title         short player-facing name
#   act           integer act number
#   path          "EMP" | "OB" | "ANY"
#   thumbnail     image path (optional; Solid fallback if missing)
#   description   one-line description
#
# Replace placeholder portraits/thumbnails with real renders by
# dropping PNGs into images/ui/portraits/<id>.png and
# images/ui/gallery/<scene_id>.png. The helpers below auto-detect
# the files and fall back cleanly when they're missing.
# ================================================================

init 2 python:

    # -------------------------------
    # Card accent colors (pulled from ui_solveil.rpy character palette)
    # -------------------------------
    _CA_LYRA   = "#C8A2FF"
    _CA_ZIRA   = "#5FE3FF"
    _CA_TESSA  = "#80C37A"
    _CA_NOELLE = "#9C87C9"
    _CA_SELENE = "#C1B8A8"
    _CA_NYRA   = "#7A9EC0"
    _CA_MARCUS = "#7A3B3F"
    _CA_KAEL   = "#A48E8A"
    _CA_LIORA  = "#B8A8D4"
    _CA_RHEA   = "#8A95A4"

    CHARACTER_PROFILES = {

        # =========================================================
        # LOVE INTERESTS — main tab
        # =========================================================

        "lyra_vashar": {
            "display_name":   "Lyra Vashar",
            "tab":            "love_interests",
            "order":          1,
            "accent":         _CA_LYRA,
            "tagline":        "Ethereal priest — devotion made flesh.",
            "portrait":       "images/ui/portraits/lyra.png",
            "basic_info": [
                ("Age",         "23"),
                ("Born",        "Third of Ember, A.C. 360"),
                ("Birthplace",  "Aeries — Cathedral Quarter"),
                ("Lineage",     "Ethereal"),
                ("Affiliation", "Cathedral of Harmony / Phoenix"),
                ("Status",      "Active"),
            ],
            "codex_entries": ["lyra_vashar", "lineages", "bands"],
            "scenes": [
                { "id": "a3_s03_breath_of_faith_emp",   "label": "a3_s03_breath_of_faith_emp",
                  "title": "Breath of Faith",          "act": 3, "path": "EMP",
                  "description": "The cathedral, the Band, the first prayer that was a promise." },
                { "id": "a3_s13_proof_of_life_ob",      "label": "a3_s13_proof_of_life_ob",
                  "title": "Proof of Life",            "act": 3, "path": "OB",
                  "description": "Devotion under dread. \"I need to know you're still in there.\"" },
                { "id": "a3_s17_faith_in_flaws_emp",    "label": "a3_s17_faith_in_flaws_emp",
                  "title": "Faith in Flaws",           "act": 3, "path": "EMP",
                  "description": "The hands that taught her stillness learning a different quiet." },
                { "id": "a4_s19_lyra_deepening_erotic_emp", "label": "a4_s19_lyra_deepening_erotic_emp",
                  "title": "Anayet",                   "act": 4, "path": "EMP",
                  "description": "The Band unbuckled, the word spoken, the claim she makes as a woman." },
                { "id": "a4_s15_lyra_deepening_erotic_ob",  "label": "a4_s15_lyra_deepening_erotic_ob",
                  "title": "Recognize Me",             "act": 4, "path": "OB",
                  "description": "Body as the last place she can pray honestly." },
            ],
        },

        "zira": {
            "display_name":   "Zira",
            "tab":            "love_interests",
            "order":          2,
            "accent":         _CA_ZIRA,
            "tagline":        "Ghostline runner — the door-keeper.",
            "portrait":       "images/ui/portraits/zira.png",
            "basic_info": [
                ("Age",         "25"),
                ("Born",        "Sixth of Rain, A.C. 358"),
                ("Birthplace",  "Unders — Ashmarket (claimed)"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Ghostline / Phoenix"),
                ("Status",      "Active"),
            ],
            "codex_entries": ["zira", "ghostline", "beacon_chip", "obsidian_bridge", "carrier_hiss", "ghost_hop"],
            "scenes": [
                { "id": "a3_s15_signal_under_fire_emp", "label": "a3_s15_signal_under_fire_emp",
                  "title": "Signal Under Fire",        "act": 3, "path": "EMP",
                  "description": "Adrenaline that became something else. A kiss in the static." },
                { "id": "a3_s15_chain_of_two_ob",       "label": "a3_s15_chain_of_two_ob",
                  "title": "Chain of Two",             "act": 3, "path": "OB",
                  "description": "Possessiveness versus the iron-blue woman. \"Don't make me regret this. Again.\"" },
                { "id": "a4_s15_zira_deepening_erotic_emp", "label": "a4_s15_zira_deepening_erotic_emp",
                  "title": "The Clock Runs Back",      "act": 4, "path": "EMP",
                  "description": "She builds an exit plan with only his name on it. He chooses to stay." },
                { "id": "a4_s13_zira_deepening_erotic_ob",  "label": "a4_s13_zira_deepening_erotic_ob",
                  "title": "Something From Before",    "act": 4, "path": "OB",
                  "description": "Anger converted into heat. The pressed flower stays hers." },
                # --- POLY scenes (Zira is the common thread in all pairings) ---
                { "id": "a4_s14a_familiar_ground_emp",  "label": "a4_s14a_familiar_ground_emp",
                  "title": "Familiar Ground",          "act": 4, "path": "EMP",
                  "description": "Lyra + Zira + Aeron. Tea and data. Two shapes of care." },
                { "id": "a4_s16a_door_and_data_emp",    "label": "a4_s16a_door_and_data_emp",
                  "title": "Door and Data",            "act": 4, "path": "EMP",
                  "description": "Zira + Noelle + Aeron. Recalibration after Rhea." },
                { "id": "a4_s20a_command_and_the_door_emp", "label": "a4_s20a_command_and_the_door_emp",
                  "title": "Command and the Door",     "act": 4, "path": "EMP",
                  "description": "Selene + Zira + Aeron. \"I delegate the question to both of you.\"" },
                { "id": "a4_s14a_oath_and_flower_ob",   "label": "a4_s14a_oath_and_flower_ob",
                  "title": "Oath and Flower",          "act": 4, "path": "OB",
                  "description": "Nyra + Zira + Aeron. Ceremony vs pressed flower." },
                { "id": "a4_s20a_doctrine_and_weapon_ob", "label": "a4_s20a_doctrine_and_weapon_ob",
                  "title": "Doctrine and Weapon",      "act": 4, "path": "OB",
                  "description": "Nyra + Noelle + Aeron. \"You are documenting this.\"" },
            ],
        },

        "tessa": {
            "display_name":   "Tessa",
            "tab":            "love_interests",
            "order":          3,
            "accent":         _CA_TESSA,
            "tagline":        "Field medic — plain as teeth.",
            "portrait":       "images/ui/portraits/tessa.png",
            "basic_info": [
                ("Age",         "23"),
                ("Born",        "Ninth of Kiln, A.C. 360"),
                ("Birthplace",  "Middle Levels — Foundry Wards"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Phoenix Clinic"),
                ("Status",      "Active"),
            ],
            "codex_entries": ["tessa", "rule_of_three", "phoenix_rebellion"],
            "scenes": [
                { "id": "a3_s13_scar_and_steady_emp",   "label": "a3_s13_scar_and_steady_emp",
                  "title": "Scar and Steady",          "act": 3, "path": "EMP",
                  "description": "Her hands on his wounds — care as desire, diagnosis as devotion." },
                { "id": "a3_s17_count_the_cost_ob",     "label": "a3_s17_count_the_cost_ob",
                  "title": "Count the Cost",           "act": 3, "path": "OB",
                  "description": "The quietest OB scene — the one where the apology is the key that opens the door." },
                { "id": "a4_s20_tessa_deepening_erotic_emp", "label": "a4_s20_tessa_deepening_erotic_emp",
                  "title": "Not a Medic Tonight",      "act": 4, "path": "EMP",
                  "description": "The jacket folded aside. The body that is not, for one hour, healing anything." },
                { "id": "a4_s17_tessa_conditional_beat_ob",  "label": "a4_s17_tessa_conditional_beat_ob",
                  "title": "Remember Who I Am Writing It For", "act": 4, "path": "OB",
                  "description": "Grief-sex of remembering — or a doorway turned away from. (Conditional.)" },
            ],
        },

        "noelle_korr": {
            "display_name":   "Noelle Korr",
            "tab":            "love_interests",
            "order":          4,
            "accent":         _CA_NOELLE,
            "tagline":        "Echelon defector — the analyst who loves.",
            "portrait":       "images/ui/portraits/noelle.png",
            "basic_info": [
                ("Age",         "28"),
                ("Born",        "First of Cipher, A.C. 355"),
                ("Birthplace",  "Aeries — Cognitive Institute"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Phoenix Strategic Analysis"),
                ("Status",      "Active (defected)"),
            ],
            "codex_entries": ["noelle_korr", "phoenix_rebellion"],
            "scenes": [
                { "id": "a3_s11_empirical_tenderness_emp", "label": "a3_s11_empirical_tenderness_emp",
                  "title": "Empirical Tenderness",     "act": 3, "path": "EMP",
                  "description": "The Name Mechanic turned inward. \"I have no unit for this.\"" },
                { "id": "a3_s16_data_and_doubt_ob",     "label": "a3_s16_data_and_doubt_ob",
                  "title": "Data and Doubt",           "act": 3, "path": "OB",
                  "description": "The analyst's first erotic encounter as an equation she cannot close." },
                { "id": "a4_s18_noelle_deepening_erotic_emp", "label": "a4_s18_noelle_deepening_erotic_emp",
                  "title": "As a Sentence Now",        "act": 4, "path": "EMP",
                  "description": "\"I said it as a variable before. I am saying it as a sentence now.\"" },
                { "id": "a4_s20_noelle_deepening_erotic_ob",  "label": "a4_s20_noelle_deepening_erotic_ob",
                  "title": "A Hand I Cannot Predict",  "act": 4, "path": "OB",
                  "description": "The weapon declaration. \"Close the door on your way out.\"" },
            ],
        },

        "selene_valen": {
            "display_name":   "Selene Valen",
            "tab":            "love_interests",
            "order":          5,
            "accent":         _CA_SELENE,
            "tagline":        "Phoenix commander — delegate the question.",
            "portrait":       "images/ui/portraits/selene.png",
            "basic_info": [
                ("Age",         "30"),
                ("Born",        "Twelfth of Ember, A.C. 353"),
                ("Birthplace",  "Middle Levels — Transit 9"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Phoenix (Commander)"),
                ("Status",      "Active / EMP only"),
            ],
            "codex_entries": ["selene_valen", "phoenix_rebellion", "kael_rylan"],
            "scenes": [
                { "id": "a3_s16_command_and_surrender_emp", "label": "a3_s16_command_and_surrender_emp",
                  "title": "Command and Surrender",    "act": 3, "path": "EMP",
                  "description": "The first time she is a woman across the table instead of a commander." },
                { "id": "a4_s17_selene_deepening_erotic_emp", "label": "a4_s17_selene_deepening_erotic_emp",
                  "title": "Held as Woman",            "act": 4, "path": "EMP",
                  "description": "The letter face-down. \"I don't know how to be held by a student.\"" },
            ],
        },

        "nyra": {
            "display_name":   "Nyra",
            "tab":            "love_interests",
            "order":          6,
            "accent":         _CA_NYRA,
            "tagline":        "Iron-blue oath — OB exclusive.",
            "portrait":       "images/ui/portraits/nyra.png",
            "basic_info": [
                ("Age",         "30"),
                ("Born",        "Fifth of Silence, A.C. 353"),
                ("Birthplace",  "Aeries — Warden Academy"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Former Echelon / OB Co-Command"),
                ("Status",      "Active (OB path only)"),
            ],
            "codex_entries": ["nyra", "echelon"],
            "scenes": [
                { "id": "a3_s12_the_oath_ob",           "label": "a3_s12_the_oath_ob",
                  "title": "The Oath",                 "act": 3, "path": "OB",
                  "description": "The fractured crest. The ritual that binds intimacy to doctrine." },
                { "id": "a4_s11_nyra_second_oath_ob",   "label": "a4_s11_nyra_second_oath_ob",
                  "title": "The Second Oath",          "act": 4, "path": "OB",
                  "description": "\"Nyra is not a name tonight. She is a temperature.\"" },
            ],
        },

        # =========================================================
        # SUPPORTING — family + antagonists tab
        # =========================================================

        "marcus_rylan": {
            "display_name":   "General Marcus Rylan",
            "tab":            "supporting",
            "order":          1,
            "accent":         _CA_MARCUS,
            "tagline":        "Father. Echelon general. The door he built.",
            "portrait":       "images/ui/portraits/marcus.png",
            "basic_info": [
                ("Age",         "50"),
                ("Born",        "Eighth of Forge, A.C. 333"),
                ("Birthplace",  "Aeries — Military Quarter"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Echelon — High Command"),
                ("Status",      "Active"),
            ],
            "codex_entries": ["marcus_rylan", "echelon", "tier_hall_branding"],
            "scenes": [],  # Antagonist — no gallery scenes
        },

        "kael_rylan": {
            "display_name":   "Kael Rylan",
            "tab":            "supporting",
            "order":          2,
            "accent":         _CA_KAEL,
            "tagline":        "Brother. Band-failed. The reliable witness.",
            "portrait":       "images/ui/portraits/kael.png",
            "basic_info": [
                ("Age",         "24 (deceased)"),
                ("Born",        "Second of Ember, A.C. 353"),
                ("Birthplace",  "Aeries — Rylan Estate"),
                ("Lineage",     "Unlineaged (Band-rejected)"),
                ("Affiliation", "—"),
                ("Status",      "Deceased (pre-story)"),
            ],
            "codex_entries": ["kael_rylan", "tier_hall_branding", "bands"],
            "scenes": [],
        },

        "liora_rylan": {
            "display_name":   "Liora Rylan",
            "tab":            "supporting",
            "order":          3,
            "accent":         _CA_LIORA,
            "tagline":        "Mother. Story-keeper. The pause.",
            "portrait":       "images/ui/portraits/liora.png",
            "basic_info": [
                ("Age",         "48"),
                ("Born",        "Seventh of Rain, A.C. 335"),
                ("Birthplace",  "Border Sector — Old Registry"),
                ("Lineage",     "Ethereal"),
                ("Affiliation", "Outlands / courier networks"),
                ("Status",      "Route-dependent"),
            ],
            "codex_entries": ["liora_rylan", "lineages"],
            "scenes": [],
        },

        "rhea_vestin": {
            "display_name":   "Commander Rhea Vestin",
            "tab":            "supporting",
            "order":          4,
            "accent":         _CA_RHEA,
            "tagline":        "Echelon's scalpel — Fourteenth Exigency.",
            "portrait":       "images/ui/portraits/rhea.png",
            "basic_info": [
                ("Age",         "28"),
                ("Born",        "Fourth of Cipher, A.C. 355"),
                ("Birthplace",  "Aeries — War College"),
                ("Lineage",     "Unlineaged"),
                ("Affiliation", "Echelon — Surgical Ops"),
                ("Status",      "Active (antagonist)"),
            ],
            "codex_entries": ["rhea_vestin", "echelon"],
            "scenes": [],
        },
    }

    # -------------------------------
    # Helpers
    # -------------------------------
    def profile_get(char_id):
        """Return the profile dict for a character, or None."""
        return CHARACTER_PROFILES.get(char_id)

    def profiles_in_tab(tab):
        """Return a list of (char_id, profile) tuples for the given
        tab, sorted by the profile's `order` field."""
        items = [
            (k, v) for k, v in CHARACTER_PROFILES.items()
            if v.get("tab") == tab
        ]
        items.sort(key=lambda kv: kv[1].get("order", 99))
        return items

    def profile_portrait(char_id):
        """Return a Ren'Py displayable for the character's portrait.
        Falls back to a color Solid keyed off the profile accent if
        the image file hasn't been dropped in yet."""
        prof = profile_get(char_id)
        if not prof:
            return Solid("#222")
        path = prof.get("portrait")
        if path and renpy.loadable(path):
            return path
        return Solid(prof.get("accent", "#444") + "55")

    def profile_scene_thumbnail(char_id, scene_id):
        """Return a displayable for a gallery scene thumbnail.
        Convention: images/ui/gallery/<scene_id>.png — falls back
        to a color tile with a soft border if not present."""
        prof = profile_get(char_id)
        path = "images/ui/gallery/" + scene_id + ".png"
        if renpy.loadable(path):
            return path
        accent = prof.get("accent", "#444") if prof else "#444"
        return Solid(accent + "33")

    def profile_codex_ids(char_id):
        """Return the list of codex entry IDs linked to this character."""
        prof = profile_get(char_id)
        return list(prof.get("codex_entries", [])) if prof else []

    def profile_unlocked_codex_ids(char_id):
        """Return only the codex entries that are currently unlocked
        in STATE['codex']['unlocked'] — the detail screen uses this
        so locked entries are hidden by default."""
        unlocked = STATE.get("codex", {}).get("unlocked", set())
        return [cid for cid in profile_codex_ids(char_id) if cid in unlocked]
