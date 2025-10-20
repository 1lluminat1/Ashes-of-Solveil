# variables.rpy


# =======================================================
# Ashes of Solveil - COMPLETE VARIABLE DEFINITIONS
# =======================================================


# ===== CORE STORY TRACKING =====
default current_act = 1
default current_scene = 0
default year = 385  # Current year in Solveil (founded Year 0)

# ===== ACT 1 VARIABLES =====

## Choice Flags (Act 1)
default aeron_practiced_pledge = False
default aeron_wears_medals = False
default aeron_hides_wrist = False
default aeron_masks_emotion = False
default aeron_avoids_marcus = False
default aeron_acknowledged_lyra = False
default aeron_moves_toward_lyra = False
default aeron_spoke_to_lyra_gala = False
default aeron_has_glass = False  # Drink at gala

## Sweep Mission Variables (Act 1 Scene 17)
default aeron_warned_civilians = False
default aeron_saved_child = False
default aeron_saved_vendor = False
default aeron_saved_shelter = False
default civilians_saved = 0  # 0-200+
default civilians_killed = 600  # 600-800
default evidence_of_mercy = 0  # 0-3+ (tracks mercy choices)
default team_suspicion = 0  # 0-4+ (how suspicious team is of Aeron)

## Morning After Confession (Act 1 Scene 18b)
default aeron_hugged_lyra_morning = False  # Empathy-gated hug choice

## Relationship Variables (Act 1 End State)
default lyra_rel = 0  # -5 to +5
default lyra_trust = 5  # 0-10 (starts moderate, gates lewd scene at 7+)
default lyra_attraction = 0  # 0-10 (builds through activities)
default zira_rel = 0  # -5 to +5
default zira_trusts_aeron = False
default aeron_empathy = 0  # 0-5+ (gates intimate moments, 2+ for hug)

# ===== ACT 2 VARIABLES =====

## Timeline Tracking
default days_remaining = 7  # Days until Selene meeting
default activities_completed = 0  # Track completion (0-7)
default required_activities = 7  # Total activities needed

## Fake Identities
default fake_name_aeron = "Kade Voss"
default fake_name_lyra = "Mira Chen"

## Currency System
default credit = 150  # Aeries credits (limited use in Unders)
default scrip = 0  # Unders currency (earned through work)
default favors_owed = 0  # People owe YOU favors (most valuable)
default favors_owed_list = []  # Track who owes what
default debts_owed = 0  # YOU owe people (dangerous)
default debts_owed_list = []  # Track who you owe

## Inventory - Equipment
default inventory = []  # General inventory list
default weapons = []  # Specific weapons owned
default medkits = 0  # Healing items (start 0, Tessa gives 2)
default stims = 0  # Combat stims
default food_rations = 3  # Prevent starvation
default water_bottles = 3  # Prevent dehydration
default cigs = 0  # Trade item, stress relief
default alcohol = 0  # Trade item, social lubricant

## Inventory - Tools
default lockpicks = False
default hacking_device = False  # Kai's device (from Zira Activity 6)
default binoculars = False

## Inventory - Disguises
default under_clothes = False  # Blend in Unders (from Zira)
default mid_disguise = False  # Pass as Mid-Level worker
default echelon_uniform = False  # Risky but useful

## Inventory - Intel & Documents
default intel_documents = []  # Maps, patrol routes, etc.
default maps = []  # Territory maps, building layouts
default secrets = []  # Blackmail, leverage material

## Reputation System
default reputation_unders = -5  # -10 (hated) to +10 (honored)
default reputation_resistance = 0  # Neutral with rebels
default reputation_echelon = -100  # They want you dead

# Reputation thresholds:
# -10 to -6: Hostile (refused service, may attack)
# -5 to -1: Distrusted (higher prices, limited access)
# 0 to +3: Neutral (normal interactions)
# +4 to +7: Respected (discounts, insider info)
# +8 to +10: Honored (free help, protective)

## Skills & Abilities
default skill_unders_disguise = False  # From Activity 6 (Zira)
default skill_pattern_recognition = False  # From Activity 3 (Noelle)

## Activity Completion Flags
default activity_work_done = False  # Activity 1
default activity_weapons_done = False  # Activity 2
default activity_intel_done = False  # Activity 3
default activity_medical_done = False  # Activity 4
default activity_reputation_done = False  # Activity 5
default activity_skills_done = False  # Activity 6
default activity_past_done = False  # Activity 7

## Philosophy Flags
default tessa_count_the_living = False  # "Count the living" philosophy learned

## Contacts Database
default contacts = {
    "kren": {
        "name": "Kren the Vendor",
        "location": "Market, Sector 6",
        "trust": 0,  # -5 to +5
        "skills": ["supplies", "gossip"],
        "favor_owed": False,
        "met": False
    },
    "vex": {
        "name": "Vex",
        "location": "Black Market, Sector 5",
        "trust": 0,
        "skills": ["weapons", "smuggling"],
        "favor_owed": False,
        "met": False
    },
    "noelle": {
        "name": "Noelle Korr",
        "location": "Sector 6 (mobile)",
        "trust": 0,  # Set by Activity 3 choice (0 or 1)
        "skills": ["analysis", "prediction", "neural_research"],
        "favor_owed": False,
        "met": False
    },
    "tessa": {
        "name": "Tessa Kael",
        "location": "Sector 7 Clinic",
        "trust": 0,  # Set to 3 by Activity 4
        "skills": ["healing", "empathy", "bio_mechanics"],
        "favor_owed": False,
        "met": False
    },
    "zira": {
        "name": "Zira",
        "location": "Safe House",
        "trust": 3,  # Starts low, increases through story
        "loyalty": 5,  # Separate from trust, tracks devotion
        "skills": ["survival", "contacts", "tech"],
        "favor_owed": False,
        "met": True  # Met in Act 1
    },
    "selene": {
        "name": "Selene",
        "location": "Sector 10 Stronghold",
        "trust": 0,
        "skills": ["leadership", "tactics", "resistance"],
        "favor_owed": False,
        "met": False
    },
    "doc_mara": {
        "name": "Doc Mara",
        "location": "Clinic, Sector 7",
        "trust": 0,
        "skills": ["medical", "intel"],
        "favor_owed": False,
        "met": False
    }
}

## Character-Specific Relationship Variables

# Lyra
default lyra_lewd_scene_unlocked = False  # Gates lewd scene availability
default lyra_romance_path = False  # Romance vs platonic path

# Noelle
default noelle_trust = 0  # 0-10 (separate from contacts dict for easier access)
default aeron_honest_with_noelle = False  # Did he tell truth in Activity 3?
default noelle_knows_glass = False  # Discovery scene flag

# Tessa
default tessa_names_saved = []  # List of names of people Aeron saved (returns to tell her)

# Zira
default zira_trust = 3  # 0-10 (separate tracking, starts at 3)
default zira_loyalty = 5  # 0-10 (starts at 5, maxes at 10 after Activity 6)
default zira_backstory_revealed = False  # Kai story revealed in Activity 6
default aeron_knows_about_kai = False  # Knows about her brother
default aeron_contacted_zira = False  # Used device in Scene 1?

## Act 2 Special Scenes
default lyra_lewd_scene_completed = False
default noelle_discovery_scene_completed = False
default zira_vulnerability_scene_completed = False

## Bounty & Threats
default bounty_on_aeron = 50000  # Credits
default bounty_on_lyra = 50000  # Credits
default echelon_alert_level = 0  # 0-10 (how hard they're hunting)

# ===== ACT 3+ VARIABLES (Placeholder) =====

## Long-term Tracking
default people_saved_count = 0  # Track for "Count the Living"
default people_killed_count = 600  # Starts with Sweep deaths
default resistance_strength = 0  # 0-100 (how strong resistance is)
default major_victories = 0  # Count significant wins against Echelon
default major_losses = 0  # Count significant defeats

## Future Key Items
default kais_hacking_device_used = False  # Track if used in infiltration

## Future Relationship Milestones
default zira_sacrifice_scene = False  # Act 3 Scene 18 (takes bullet)
default noelle_no_unit_scene = False  # Realizes she has feelings
default tessa_mercy_death_scene = False  # Trauma arc climax

# ===== DEBUG & TESTING =====
default debug_mode = False  # Enable for testing
default skip_activities = False  # Skip directly to Scene 7 (Selene meeting)

# ===== VISUAL/UI FLAGS =====
default show_activity_hub = False  # Display activity selection screen
default show_inventory = False  # Display inventory screen
default show_map = False  # Display territory map

# ===== CANON TRACKING (For Reference) =====
# These don't affect gameplay but track canonical story beats for reference

default canon_notes = {
    "act1_complete": False,
    "purge_witnessed": False,
    "glass_shattered": False,
    "defected_from_echelon": False,
    "met_selene": False,
    "resistance_joined": False
}

# ===== END OF VARIABLES =====