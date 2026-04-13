# =======================================================
# ACT 2 - Scene 25: Echelon Raid Defense
# File: a2_s25_echelon_raid_defense.rpy
# Action climax of Act 2.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s25_echelon_raid_defense"
$ scene_mark(_current_scene_id, "entered")
$ op_start("raid_defense", note="Echelon assault on main base")

label a2_s25_echelon_raid_defense:
    $ show_timeline("21st of Ember, 385 A.C.", "02:00", "Phoenix Base — Perimeter")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Shifts per phase. Wide for alarm. Tight handheld for Zira's sabotage. Military precision for Lyra.
    #         Data overlay for Noelle. Intimate for Tessa. Back to wide for evacuation.
    #         The camera gets MORE controlled as the chaos increases — Aeron's training taking over.
    # LIGHTING: Red emergency wash for alarm. Exterior: dawn gray + muzzle flash. Medbay: harsh surgical white.
    #           Aftermath: amber practicals in the secondary base. Exhaustion light.
    # SFX: Alarm. Gunfire. Explosions (Zira). Radio chatter. The breathing stopping (Tessa's patients).
    #       The silence after evacuation — the loudest sound in the scene.
    # FACE: Everyone afraid. Everyone functioning anyway. That's the scene's thesis.

    # ========== THE ALARM — DAWN, DAY 12 ==========

    "The alarm doesn't build. It arrives."

    # SOUND: ALARM — continuous, cutting through sleep, through walls, through everything.

    athought "That sound. You never forget it. You never get used to it."

    "The base erupts. 587 people moving simultaneously — some to weapons, some to positions, some to evacuation routes. Organized chaos. Training replacing thought."

    # VISUAL: Noelle at command station. Data streaming. Multiple screens. The 72-hour audit just expired.
    n "(over comms, urgent but controlled) Echelon task force detected. Six blocks north. Fifty-two Banded soldiers. Specialized assault configuration. ETA eight minutes."

    n "This is confirmed hostile contact. All personnel to defensive positions."

    # VISUAL: Selene at the command table. Already there. Map displayed. She doesn't look surprised.
    sel "This is what we prepared for. Staged defense. Hold, bleed, retreat, survive."

    "She assigns without hesitation."

    sel "Zira — sabotage. Slow them before they reach us."
    sel "Lyra — north perimeter. Fifty fighters. Hold the line."
    sel "Noelle — coordination. You're our brain. Keep everyone connected."
    sel "Tessa — triage. Casualties are coming."
    sel "Aeron — with me. We direct the defense."

    # ========== ZIRA — SABOTAGE ==========

    "Zira is already outside."

    z "(over comms, calm) Charges set. Approach route. Support columns. Street barriers. When they walk through, I welcome them."

    "Fifty-two soldiers advance through the streets. Banded. Enhanced. Confident."

    "They don't know Zira's watching."

    # SOUND: Multiple explosions. Overlapping. Street erupting. Dust and chaos.

    "Five go down before they fire a shot."

    z "(over comms) Five confirmed. Forty-seven remaining. They're slowed. They're angry. You have three extra minutes. Use them."

    "She disappears. Shadows swallow her like she was never there."

    # ========== LYRA — NORTH PERIMETER ==========

    "North perimeter. Fifty fighters behind makeshift cover. Some veterans. Mostly recruits."

    "Lyra stands in the center. Visible. Exposed. Deliberate."

    l "Hold fire until they're in range. Controlled bursts. Center mass. No heroes. When I give the fallback order, you move. Together."

    "The enemy appears. Forty-seven soldiers advancing through the dust."

    l "FIRE!"

    "Fifty weapons open simultaneously."

    "The enemy takes hits. Five down. Seven. Ten. But they keep coming. Bands keep them moving. Enhancement keeps them fighting."

    "Return fire. Three of Lyra's fighters drop. Then five. Then eight."

    "Discipline fractures. Some recruits break. Start retreating without orders."

    l "(over the gunfire) HOLD! You break now, everyone behind us dies! HOLD!"

    "They see her standing. Not behind cover — standing. Fighting. Not breaking."

    "They hold."

    # ========== NOELLE — COORDINATION ==========

    n "(over comms, rapid) Lyra — flanking movement, east side. Redirect second squad."
    n "Zira — secondary window opening, thirty-seven seconds, northwest."
    n "Tessa — casualty surge incoming. Twelve wounded."
    n "Selene — ammunition rate exceeds projection. Resupply north in four minutes."

    "Twenty simultaneous conversations. Every fighter an instrument. Noelle conducting."

    n "Enemy adapting. Three-vector assault. North perimeter breach probability: 78%%. Recommend staged fallback in ninety seconds."

    sel "(over comms) Confirmed. Lyra — fallback on my mark."

    # ========== TESSA — TRIAGE ==========

    "The medbay fills."

    "Gunshot wounds. Blast injuries. Burns. The human cost of everything they built arriving on stretchers and in arms."

    "Tessa's hands move without stopping. Tourniquet. Pressure. Suture. Triage tag. Next."

    "She saves fifteen who should have died."

    "She loses others."

    "Two ask her the same question Torin asked."

    "She answers the same way."

    "Her hands don't shake until after."

    # ========== FALLBACK — EVACUATION ==========

    l "(over comms) FALLBACK! All squads to secondary positions! Covering fire! MOVE!"

    "The retreat is controlled. Covered. Professional. Training holding where courage frays."

    "Secondary positions. Five minutes. Bleed them more. Then go."

    sel "(final order) EVACUATE! All personnel to east tunnels! Disperse to secondary bases!"

    "The base empties. Not in panic — in waves. Wounded first. Then support. Then fighters covering the retreat."

    "Echelon takes the building."

    "The resistance takes itself."

    # ========== AFTERMATH — SECONDARY BASE, HOURS LATER ==========

    "Sector 9. Secondary base. The one they prepared for this exact scenario."

    "Counting."

    "Always counting."

    sel "Forty dead. Thirty-five wounded. Seventy-five total casualties."

    "The numbers land in the room like stones in water."

    sel "Enemy casualties: twenty-two of fifty-two. Forty-two percent."

    n "Casualty rate 13%% in defensive action against a superior force. Within acceptable parameters."

    "Noelle says 'acceptable parameters' and her voice doesn't crack, but she looks at the wall instead of at anyone."

    sel "Main base lost. But secondary bases intact. Distributed command operational. We survived what they built to destroy us."

    "Selene pauses."

    sel "That's not nothing."

    if canon_get("path_state") == "EMP":
        athought "Forty people died because they joined us. Because I recruited them. Because I told them fighting meant something."
        athought "Daven's out there in Sector 7 with 120 people who trusted us. Elara is somewhere learning that the cost of resistance isn't theoretical."
        athought "Mila's name. Torin's name. Now forty more."
        athought "I'll carry them."

    elif canon_get("path_state") == "OB":
        athought "Forty dead. 547 operational. 13%% casualty rate. We inflicted 42%% on their force."
        athought "The math works. The distributed structure held. The operation survived."
        athought "Forty names on Tessa's board that weren't there yesterday."
        athought "The math works. It just costs."

    else:
        athought "Forty dead. Forty names."
        athought "We survived. That has to mean something."
        athought "It has to."

    # VISUAL: Tessa at a bare wall in the secondary base. Marker in hand. Starting the board over.
    # Left side: 547. Right side: 41. Both sides count.

    "Tessa finds a bare wall."

    "She doesn't have her board. She has a marker."

    "Left side: the living. Right side: the dead."

    "She starts writing. Both sides."

    "Nobody tells her to stop."

    # ========== SCENE CLOSE ==========

    "The secondary base settles into something that isn't peace."

    "It's aftermath."

    "The space where the gunfire stops echoing and the silence starts."

    sel "(to Aeron, quiet) Selene is wounded. She took a round during evacuation. Through-and-through, left shoulder."

    if canon_get("path_state") == "EMP":
        athought "She's hurt. She's still giving orders. She's still standing."
        athought "She shouldn't be standing."

    "Tessa has already seen her. Bandaged. Functional. Refusing to lie down."

    sel "I've survived worse."

    "She hasn't. But she says it like she has, and nobody contradicts her."

    pause 1.0

    "Outside, the city hums the way it always does. Indifferent to what happened in its guts."

    "587 became 547."

    "The resistance survived."

    "The cost is forty names that Tessa is writing on a wall in a building they moved into three hours ago."

    "Tomorrow they rebuild."

    "Tonight they count."

    # ========== STATE UPDATES ==========

    $ op_end("raid_defense", tag="Echelon Raid — Main Base Lost")
    $ civ_killed(40)
    $ stat_inc("people_killed", 0)  # These are resistance fighters, not civilians Aeron killed
    $ stat_inc("resistance_strength", -40)
    $ canon_set("first_major_battle", True)
    $ canon_set("main_base_lost", True)
    $ canon_set("dispersed_to_secondary", True)
    $ flag("selene_wounded_raid", True)
    $ npc_remember("Lyra", "held_north_perimeter", tone="proven")
    $ npc_remember("Zira", "sabotage_five_kills", tone="professional")
    $ npc_remember("Noelle", "coordinated_defense", tone="critical")
    $ npc_remember("Tessa", "triage_forty_dead", tone="carrying")
    $ npc_remember("Selene", "wounded_in_evacuation", tone="enduring")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s25_echelon_raid_defense
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Day 12 of 14-day countdown. Dawn. The 72-hour Echelon audit (from Interlude 2) expired.
#   - Raid arrives 2 days early — the audit accelerated the timeline.
# cann.what_happened:
#   - 52 Banded assault soldiers attack main base. Targeted strike, not a patrol.
#   - Character synergy showcase:
#       Zira: Sabotage — 5 kills before engagement. "Charges set. Welcome."
#       Lyra: North perimeter — held the line, rallied breaking recruits, ordered controlled retreat.
#       Noelle: Coordination — 20 simultaneous conversations, predicted breach, managed evacuation timing.
#       Tessa: Triage — saved 15, lost 40, delivered 2 more mercy deaths, started new board at secondary base.
#       Selene: Command — staged defense, evacuation order, wounded during withdrawal.
#   - Staged defense: hold perimeter → bleed → fallback → evacuate.
#   - Casualties: 40 resistance dead, 35 wounded (13% casualty rate). Enemy: 22/52 killed (42%).
#   - Main base lost. Dispersed to secondary bases. Distributed command operational.
#   - Selene wounded: through-and-through, left shoulder. Functional. Refusing to rest.
# cann.aeron_state:
#   - Command role during the defense. Co-directing with Selene.
#   - EMP: carries the names. "Forty people died because I recruited them."
#   - OB: carries the math. "13% casualty rate. The operation survived."
#   - Both feel the weight. The difference is the unit of measurement.
# cann.path_tracking:
#   - No player choice — this is an action scene, not a decisions scene.
#   - op_start/op_end fires for operations snapshot.
#   - stat_inc("resistance_strength", -40).
#   - flag("selene_wounded_raid") gates the carry scene (a2_s26).
# cann.thematic_flags:
#   - "The alarm doesn't build. It arrives." — war's lack of ceremony.
#   - Each character's contribution is distinct and irreplaceable. The team functions as a system.
#   - Tessa starting a new board at the secondary base — "Both sides count" becomes operational.
#   - "Echelon takes the building. The resistance takes itself." — survival thesis.
#   - "587 became 547." — the number shrinking is the scene's quiet devastation.
#   - "Tonight they count." — closing line.
# cann.character_moments:
#   - Zira: Five kills before engagement. Professional. Disappears into shadows. Economy of violence.
#   - Lyra: Stands exposed to rally breaking fighters. "You break now, everyone behind us dies."
#     Military leadership under fire. This is what she was trained for.
#   - Noelle: "Acceptable parameters" while looking at the wall. The data holds. The person underneath it hurts.
#   - Tessa: Saves 15, loses 40, delivers 2 mercy deaths. Starts writing on a bare wall in a new building.
#     "Nobody tells her to stop."
#   - Selene: Wounded, refusing to lie down. "I've survived worse." She hasn't.
# cann.block_status:
#   - ANCHOR (both paths). Action climax of Act 2.
# cann.requires_followup:
#   - flag("selene_wounded_raid") gates carry scene (a2_s26, EMP only).
#   - Selene's wound affects the finale — she's weakened when she offers command (EMP) or confronts Aeron (OB).
#   - Tessa's board at secondary base should be visible in all subsequent scenes there.
#   - Lyra's perimeter command earns respect from fighters — she's proven as field commander.
#   - The 42% enemy casualty rate means Echelon knows the resistance fights back. Next response will be harder.
#   - Daven's Sector 7 base survived (distributed command worked). Should be confirmed.
