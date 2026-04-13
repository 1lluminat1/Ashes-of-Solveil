# =======================================================
# ACT 2 - Scene 22: Massive Recruitment
# File: a2_s22_massive_recruitment.rpy
# PATH HARD-LOCK fires in this scene.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s22_massive_recruitment"
$ scene_mark(_current_scene_id, "entered")

label a2_s22_massive_recruitment:
    $ show_timeline("19th of Ember, 385 A.C.", "06:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, starts wide — widest shot we've used in Act 2. The ops room is FULL. Bodies everywhere.
    #         Slowly tightens across the scene until the final Selene moment is intimate two-shot.
    # LIGHTING: Morning overheads buzzing. Too many warm bodies — the light looks different when 500 people breathe in one space.
    #           Status boards casting cold blue on the walls. Map-light amber on the table.
    # SFX: Loop — crowd noise (not bar crowd — organized crowd. Voices overlapping with purpose, not chaos).
    #       One-shots — radio chatter, boot stamps, someone calling headcount down the corridor.
    # BLOCKING/PROPS: Ops room at seven times capacity. People in the corridors. Sleeping shifts visible.
    #                 The map table is the eye of the storm — Selene's command island in a sea of bodies.
    # FACE: Selene exhausted but sharp. Noelle focused, data crystal working overtime.
    #        Zira uncomfortable with the crowd. Tessa counting heads. Lyra tactical.
    #        Aeron looking at 587 faces and seeing 587 names he might lose.

    # ========== CHAPTER TITLE CARD ==========
    scene black with fade
    centered "{size=+20}ACT II{/size}"
    pause 0.5
    centered "{size=+10}Chapter IV — The Cost{/size}"
    pause 2.0
    scene black with fade

    # ========== THE NUMBER — MORNING, OPS ROOM ==========

    "The ops room wasn't built for this."

    "Eighty people, maybe. That was the ceiling when they chose this base. Eighty bodies, eighty cots, eighty mouths. The infrastructure could handle eighty."

    "There are 575 people in the building."

    "Sleeping in shifts. Eating in shifts. Breathing in shifts, practically. The corridors are arteries now — always something moving through them, always someone on the way to somewhere."

    athought "Three weeks ago this was a ruin with a good roof. Now it's an army pretending to be a building."

    # VISUAL: Selene at the map table. The only clear space in the room — people give it a wide berth. Command gravity.
    sel "Aeron. We need to talk about what we've built."

    "She doesn't say it like a celebration."

    a "How many?"

    sel "575 confirmed. Eight arrived during the night. Group of twelve waiting outside from Sector 11."

    n "(from her station) 587 if intake holds. Current rate: 35 per day. Projected: 650 by week's end. 800 by month's end."

    "Noelle's voice carries the numbers the way it always does — precisely, completely, without flinching from what they mean."

    n "That's pre-Purge strength achieved in four months."

    sel "Which brings us to the problem."

    # ========== THE PROBLEM ==========

    n "Echelon patrol density has increased 47%% in two weeks. Correlated directly with our recruitment surge."

    "She projects the data. Heat map on the wall — patrol patterns tightening like a fist closing."

    n "They don't know where we are. But they know something is happening. Someone is organizing."

    z "My contacts confirm. This isn't normal patrol increase. Task force level. Specialized units."
    z "They're calling us 'The Phoenix.' That's powerful branding. It's also a target designation."

    n "Probability models. 73%% chance of base discovery within fourteen days. 89%% within three weeks."

    "The number settles over the room."

    l "Combat readiness?"

    n "Approximately 200 of 587. Thirty-five percent."

    l "So when they hit us — and they will — two-thirds of our people can't fight back."

    t "(quiet) And I'll be treating the ones who try anyway."

    # ========== PATH HARD-LOCK ==========

    # This is where the game evaluates the player's full Act 2 choices and locks the path.
    $ _locked_path = lock_path_act2_massive_recruitment()
    $ log_line("PATH_LOCKED:{}".format(_locked_path))

    "Selene looks around the table. At the people who built this. At what it's becoming."

    sel "We have two parallel missions and fourteen days to execute both."
    sel "Mission one: keep growing, keep training, get to combat-ready. That's offense."
    sel "Mission two: prepare for discovery. Distribute. Decentralize. Survive what's coming. That's defense."

    "She taps four points on the map."

    sel "Four secondary bases. Sectors 7, 9, 11, 13. Each gets a commander from our ranks. If Echelon hits one, the others survive."

    # ========== THE COMMANDERS ==========

    sel "Daven."

    "The young man with the burns steps forward. He's been training recruits for two weeks. The pear vendor who became a drill instructor."

    sel "Sector 7. 120 fighters. Community integration and civilian support. You're good with people. Use that."

    daven "I — yes. I can do that."

    sel "I know you can. That's why I'm asking."

    "Three more appointments. Names Aeron has screened, trained, watched grow from desperate arrivals into something resembling leaders. The resistance has depth now — capability beyond the core team."

    sel "Core team stays here. Central command. Aeron and Lyra on strategic oversight. Noelle on intelligence. Zira on external ops. Tessa on medical coordination across all five locations."

    # ========== THE WEIGHT ==========

    "The assignments disperse. The room thins — slightly. 575 people don't thin much."

    "Selene stays at the table."

    "Aeron stays."

    if _locked_path == "EMP":
        athought "587 people. I recruited half of them. Trained a quarter. Screened almost all of them."
        athought "Elara is out there somewhere. Mila's mother. Learning to hold a weapon because I killed her family and she chose to fight beside me anyway."
        athought "If Echelon comes and she dies — that's mine. That name is mine."
    elif _locked_path == "OB":
        athought "587 fighters at 35%% readiness. 200 effective. 387 liabilities."
        athought "The math isn't good. But the math was never going to be good. You build an army in the cracks of an empire, you fight with what you have."
        athought "The question isn't whether we lose people. It's whether the operation survives the loss."
    else:
        athought "587 people chose to be here. Each one a name. Each one a risk."
        athought "Each one mine, in a way I can't explain and can't shake."

    sel "(quietly, just to Aeron) I've seen this pattern before."

    a "What pattern?"

    sel "Growth that outpaces security. Hope that makes you visible. The weeks before the Purge looked like this."
    sel "Different numbers. Same shape."

    a "You think it happens again."

    sel "I think Echelon can't allow something like us to exist twice."

    "She's staring at the map. The patrol convergence lines. Red threads closing."

    a "Then we make sure it's not the same ending."

    sel "(meeting his eyes) Fourteen days."

    a "Fourteen days."

    sel "Make them count."

    "She rolls the maps. Not because the briefing is over — because she needs her hands to do something that isn't shaking."

    "The ops room hums. 587 voices. 587 choices. 587 names that might end up on Tessa's board."

    "The countdown starts now."

    # ========== STATE UPDATES ==========

    $ stat_inc("resistance_strength", 532)
    $ canon_set("battalion_strength", True)
    $ canon_set("distributed_command", True)
    $ canon_set("echelon_discovery_imminent", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s22_massive_recruitment
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: True
# cann.when_in_timeline:
#   - Approximately Day 30. Two weeks after recruitment wave. Growth milestone + crisis point.
#   - PATH HARD-LOCK fires here: lock_path_act2_massive_recruitment().
# cann.what_happened:
#   - Resistance has grown from 55 to 587 (575 confirmed + 12 incoming). Rate: 35/day.
#   - Noelle's data: 73% discovery in 14 days, 89% in 3 weeks. Patrol density up 47%.
#   - Echelon mobilizing task force level response. "The Phoenix" is now a target designation.
#   - Combat readiness: only 35% (200/587). Two-thirds can't fight.
#   - Distributed command structure established: 4 secondary bases in Sectors 7, 9, 11, 13.
#   - Daven promoted to Sector 7 commander. Three other field commanders appointed.
#   - Core team stays at main base: Aeron/Lyra (strategy), Noelle (intel), Zira (external), Tessa (medical).
#   - Selene's closing: "I've seen this pattern before. The weeks before the Purge looked like this."
#   - 14-day countdown begins.
# cann.aeron_state:
#   - PATH NOW LOCKED. Internal monologue branches on locked path for the first time.
#   - EMP: sees names, sees Elara, carries the personal weight of each recruit.
#   - OB: sees numbers, calculates readiness percentages, frames losses as operational cost.
#   - Both paths feel the gravity. The difference is what they count.
# cann.path_tracking:
#   - lock_path_act2_massive_recruitment() fires — this is the hard lock.
#     OB if ob_ratio >= 0.85. EMP if emp_ratio >= 0.65. Tie-break by momentum.
#   - No player choice in this scene — it's a consequences scene, not a decisions scene.
#   - stat_inc("resistance_strength", 532) — total now 587.
#   - canon flags: battalion_strength, distributed_command, echelon_discovery_imminent.
# cann.thematic_flags:
#   - Growth as danger. Success as visibility. Hope as target.
#   - "The Phoenix" — powerful branding that's also a target designation. Hope weaponized both ways.
#   - Selene's "same shape" — the Purge's pattern repeating. History as warning.
#   - "She needs her hands to do something that isn't shaking." — Selene's composure has a cost.
#   - 587 as both triumph and threat. The number means everything and everything is at risk.
#   - 14-day countdown as structural engine for the remaining Act 2 scenes.
# cann.character_moments:
#   - Selene: Exhausted but sharp. Sees the Purge's shape in the patrol data. Rolling the maps to hide shaking hands.
#   - Noelle: Numbers delivered precisely, without flinching. 73%. 89%. 35%.
#   - Zira: Uncomfortable with the crowd. "The Phoenix" is branding she respects and fears.
#   - Tessa: "And I'll be treating the ones who try anyway." Quiet devastation.
#   - Lyra: Tactical assessment. Two-thirds can't fight. Military reality.
#   - Daven: From pear vendor to base commander. Growth embodied.
# cann.block_status:
#   - ANCHOR (both paths). Path hard-lock scene. Chapter IV opener.
# cann.requires_followup:
#   - 14-day countdown drives pacing for remaining Act 2 scenes.
#   - Distributed command structure pays off during the raid (secondary bases survive).
#   - Daven's Sector 7 base should appear in the raid — his first test as commander.
#   - Selene's "same shape" warning foreshadows the raid and, for OB path, her own death.
#   - EMP Aeron's "that name is mine" about Elara/Mila connects back to recruitment wave.
#   - Tessa's board is about to get much heavier.
