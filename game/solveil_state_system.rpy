# solveil_state_system.rpy
# Ashes of Solveil – Advanced State Architecture
# This file defines all core data structures and utilities for state management

init python:

    # ========== CHARACTERS ==========
    characters = {
        "Lyra": {
            "met": True,
            "trust": 1,
            "affection": 0,
            "romance_path": False,
            "lewd_scene_unlocked": False,
            "lewd_scene_completed": False,
            "notes": []
        },
        "Zira": {
            "met": False,
            "trust": 0,
            "loyalty": 0,
            "romance_path": False,
            "lewd_scene_unlocked": False,
            "lewd_scene_completed": False,
            "vulnerability_scene_completed": False,
            "backstory_revealed": False,
            "knows_about_kai": False,
            "contacted_in_scene1": False
        },
        "Tessa": {
            "met": False,
            "trust": 0,
            "affection": 0,
            "romance_path": False,
            "names_saved": [],
            "mercy_death_scene": False
        },
        "Noelle": {
            "met": False,
            "trust": 0,
            "affection": 0,
            "romance_path": False,
            "discovery_scene_completed": False,
            "knows_glass": False,
            "aeron_honest": False,
            "no_unit_scene": False
        },
        "Selene": {
            "met": False,
            "trust": 0,
            "affection": 0,
            "romance_path": False
        },
        "doc_mara": {
            "met": False,
            "trust": 0,
            "skills": ["medical", "intel"],
            "favor_owed": False
        }
    }

    # ========== SCENE STATE ==========
    scenes = {
        "act1_05_gala": {
            "acknowledge_daren": False
        },
        "act1_17_sweep": {
            "choice": 0,
            "civilians_saved": 0,
            "player_hesitated": False
        },
        "act2_activity": {
            "work": False,
            "weapons": False,
            "intel": False,
            "medical": False,
            "reputation": False,
            "skills": False,
            "past": False,
            "count_completed": 0,
            "required": 7
        },
        "special_scenes": {
            "lyra_rooftop": {
                "visited": False,
                "romance_attempted": False
            },
            "selene_meeting": {
                "triggered": False
            }
        }
    }

    # ========== INVENTORY ==========
    inventory = {
        "credits": 150,
        "scrip": 0,
        "favors_owed": [],
        "debts_owed": [],
        "supplies": {
            "medkits": 0,
            "stims": 0,
            "food": 3,
            "water": 3,
            "cigs": 0,
            "alcohol": 0
        },
        "weapons": [],
        "tools": {
            "lockpicks": False,
            "hacking_device": False,
            "binoculars": False
        },
        "disguises": {
            "under_clothes": False,
            "mid_disguise": False,
            "echelon_uniform": False
        },
        "intel": {
            "documents": [],
            "maps": [],
            "secrets": []
        }
    }

    # ========== REPUTATION ==========
    reputation = {
        "unders": -5,
        "resistance": 0,
        "echelon": -100
    }

    # ========== SKILLS ==========
    skills = {
        "unders_disguise": False,
        "pattern_recognition": False
    }

    # ========== PLAYER STATE ==========
    player_state = {
        "fake_names": {
            "aeron": "Kade Voss",
            "lyra": "Mira Chen"
        },
        "days_remaining": 7,
        "bounty": {
            "aeron": 50000,
            "lyra": 50000
        },
        "echelon_alert": 0,
        "empathy_score": -5
    }

    # ========== CANON FLAGS ==========
    canon = {
        "act1_complete": False,
        "purge_witnessed": False,
        "glass_shattered": False,
        "defected": False,
        "met_selene": False,
        "resistance_joined": False
    }

    # ========== STATS ==========
    stats = {
        "people_saved": 0,
        "people_killed": 600,
        "resistance_strength": 0,
        "major_victories": 0,
        "major_losses": 0
    }

    # ========== SYSTEM FLAGS ==========
    system_flags = {
        "debug_mode": False,
        "skip_activities": False,
        "show_activity_hub": False,
        "show_inventory": False,
        "show_map": False
    }

    # ========== SHORT UTILITY FUNCTIONS ==========
    def add_trust(name, amount):
        characters[name]["trust"] += amount

    def add_affection(name, amount):
        characters[name]["affection"] += amount

    def unlock_romance(name):
        characters[name]["romance_path"] = True

    def is_met(name):
        return characters[name]["met"]

    def relationship_state(name):
        t = characters[name].get("trust", 0)
        a = characters[name].get("affection", 0)
        if t < 0: return "hostile"
        if a >= 3 and t >= 2: return "romantic"
        if a >= 2 and t >= 1: return "friend"
        return "neutral"

    def add_item(category, item, qty=1):
        if item in inventory[category]:
            inventory[category][item] += qty
        else:
            inventory[category][item] = qty

    def has_item(category, item):
        return inventory[category].get(item, 0) > 0

    def add_favor(person):
        inventory["favors_owed"].append(person)

    def pay_debt(person):
        if person in inventory["debts_owed"]:
            inventory["debts_owed"].remove(person)

    def set_scene_flag(group, key):
        scenes[group] = scenes.get(group, {})
        scenes[group][key] = True

    def check_scene_flag(group, key):
        return scenes.get(group, {}).get(key, False)

    def aeron_alignment():
    score = player_state["empathy_score"]
    if score >= 2:
        return "empathy"
    elif score <= -2:
        return "obedience"
    else:
        return "conflicted"



# ========== MINIMAL DEBUG OVERLAY ==========
screen solveil_debug_overlay():
    if system_flags["debug_mode"]:
        frame:
            style "default"
            xalign 0.01
            yalign 0.01
            has vbox
            text "DEBUG MODE: ON" size 16 color "#00ff00"
            text "Aeron Trust: [characters['lyra']['trust']]" size 12
            text "Zira Loyalty: [characters['zira']['loyalty']]" size 12
            text "Reputation (Unders): [reputation['unders']]" size 12
            text "Credits: [inventory['credits']]" size 12
            text "Days Remaining: [player_state['days_remaining']]" size 12

# Enable overlay globally
init python:
    config.overlay_screens.append("solveil_debug_overlay")
