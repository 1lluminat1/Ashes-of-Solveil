# =======================================================
# ACT 2 - Scene 21: Command Temperature
# File: a2_s21_command_temperature.rpy
# Pair Anchor: A2_P04 (Aeron x Selene)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s21_command_temperature"
$ scene_mark(_current_scene_id, "entered")

label a2_s21_command_temperature:
    $ show_timeline("DAY 18", "14:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, steady. Two-shots across the ops table — Selene and Aeron on opposite sides.
    #         The table is the power object. Whoever controls the table controls the room.
    #         Push-in when Aeron challenges. Hold wide when Selene lets the silence work.
    # LIGHTING: Tactical amber from the map display. Cold blue from wall-mounted status boards.
    #           Their faces split between the two sources — warm below, cold above.
    # SFX: Loop — ops room at working volume (muffled radio, distant footsteps, someone typing).
    #       One-shots — map marker clicks, chair shift, Selene's gloves creaking on the table edge.
    # BLOCKING/PROPS: Ops table (same from Selene's Judgment, but the base version — cleaner, more organized).
    #                 Maps. Markers. Sector grids. Noelle's data projections on one wall.
    #                 Three other resistance members seated at the edges — Zira, Cade, one lieutenant.
    # FACE: Selene in command mode — mask on, reading the room. Aeron watching the plan, seeing the flaw.
    #        Zira casual but alert. Cade deferential to Selene. The lieutenant nervous.

    # ========== OPERATIONS BRIEFING — MORNING ==========

    "The ops room smells like cold coffee and overnight decisions."

    "Selene is already at the table when Aeron arrives. Maps spread. Markers placed. The plan laid out in colored pins and hand-drawn sector grids."

    "Zira leans against the back wall, arms crossed. Cade sits at the far end, cleaning a blade with methodical boredom."

    sel "Good. Everyone's here."

    "She taps the map."

    sel "Supply corridor between Sectors 5 and 8. Echelon runs a weekly convoy — medical surplus, rations, ammunition. Lightly armored. Six-vehicle column, twelve-soldier escort."

    sel "We hit it here."

    "She places a red marker at a choke point where two tunnels converge."

    sel "Tunnel junction. Narrow approach, no room to maneuver. Zira's team blocks the rear. Cade's team handles the escort. We strip the vehicles and disperse before their response unit arrives."

    cade "Timeline?"

    sel "Fourteen minutes from first contact to extraction. Noelle's models give us a seventeen-minute window before the nearest QRF can deploy."

    z "Three-minute margin. Tight but doable."

    sel "It's enough. We've run tighter."

    "She looks around the table."

    sel "Questions?"

    # ========== THE FLAW ==========

    "Aeron is studying the map. Not the plan — the map. The terrain. The sightlines."

    "He's been quiet since he sat down."

    athought "The junction is good. Selene's right about the choke point. Limited escape routes for the convoy, clean extraction angles for our teams."

    athought "But."

    "There's something wrong. He can see it the way he used to see it — from the other side of the table. From the side that designs convoys."

    athought "The approach route passes within two hundred meters of a residential block. Sector 5, lower tier. Civilians."

    athought "If the escort breaks formation and pushes into the residential zone — which is standard Echelon doctrine when ambushed in tight quarters — our people will be chasing armed soldiers through an occupied building."

    athought "Selene's plan assumes the escort stays in the kill zone. But Echelon trains them to scatter into civilian cover. I know because I wrote that training module."

    menu:
        athought "She missed it. Or she accepted the risk. Either way, I can see it."

        "Challenge the plan.":
            $ choice_and_dev(
                _current_scene_id, "_challenged_plan", "EMP", factor=1,
                note="Challenges Selene's plan on civilian risk. Prioritizes non-combatant safety over operational simplicity."
            )
            $ scene_mark(_current_scene_id, "challenged_plan")

            a "One problem."

            "The room shifts. Zira's arms uncross. Cade's blade stops moving."

            sel "Go ahead."

            a "Your approach route passes a residential block. Sector 5, lower tier. If the escort breaks formation — and they will, that's standard Echelon scatter doctrine — they push into civilian cover."

            a "Your fourteen-minute window becomes a hostage scenario. Our people chasing armed soldiers through someone's home."

            "Selene doesn't flinch. But her jaw tightens — the tell Aeron's learning to read."

            sel "The residential block is two hundred meters from the junction. That's outside effective scatter range."

            a "For standard infantry. Not for Banded soldiers running threat-response conditioning. They'll cover two hundred meters in under ninety seconds. I know because I designed that conditioning."

            "Silence."

            cade "(low) He's got a point."

            sel "I didn't ask you."

            "She's looking at Aeron. Not angry — measuring. Testing the temperature of what he just did."

            sel "You're telling me my plan has a civilian exposure problem."

            a "I'm telling you I've been on the other side of this ambush. And I know what the escort will do when the shooting starts. They won't stay in your kill zone."

            sel "Then what do you propose?"

        "Accept the plan — suggest a contingency.":
            $ choice_and_dev(
                _current_scene_id, "_accepted_with_contingency", "OB", factor=1,
                note="Accepts plan's framework but adds tactical contingency. Respects chain of command while demonstrating competence."
            )
            $ scene_mark(_current_scene_id, "accepted_with_contingency")

            a "The plan is sound. One addition."

            "Selene's eyebrow rises. Not much — a millimeter. Permission."

            a "The approach route passes a residential block. Standard Echelon scatter doctrine pushes the escort into civilian cover when ambushed in tight quarters."

            a "I'd add a secondary blocking team at the residential corridor entrance. Two people, non-lethal deterrent. If the escort tries to scatter, they hit a wall before they reach the building."

            sel "That's two more bodies committed. We're already stretched."

            a "Two bodies to prevent a hostage scenario. The math works."

            "Selene studies him."

            sel "You designed their scatter doctrine, didn't you?"

            a "I wrote the training module."

            sel "And now you're using it against them."

            a "That's the whole point of me being here."

    # ========== THE TEST ==========

    "The room holds its breath."

    "Selene picks up a marker. Rolls it between her fingers. Thinking."

    "This isn't about the plan. Aeron can feel it. The plan is fine — Selene's plans are always fine. This is about whether the man across the table can hold line when the commander pushes back."

    if scene_has(_current_scene_id, "challenged_plan"):
        sel "You just contradicted me in front of my team."

        a "I identified a risk in front of OUR team."
        $ tp_seed("a2.command.our_team")

        "The correction lands. Selene registers it. Zira registers it. Even Cade looks up."

        sel "Our team."

        a "If I'm screening recruits, planning operations, and sitting at this table — then yes. Ours."

    else:
        sel "You didn't challenge the plan. You improved it."

        a "The plan didn't need challenging. It needed one adjustment."

        sel "And you made it without undermining command authority in front of the room."

        a "That matters to you."

        sel "It matters to everyone in this room. They need to see command that functions, not command that fractures."

    "She puts the marker down."

    sel "Alright."

    # ========== THE SHIFT ==========

    "She addresses the room."

    sel "Aeron's modification is in. Secondary blocking team at the residential corridor."

    if scene_has(_current_scene_id, "challenged_plan"):
        sel "Two volunteers for the blocking position. Aeron, you select them. You identified the problem — you own the solution."
    else:
        sel "Aeron, assign the blocking team from your screening pool. Pick people who can hold a line without escalating."

    cade "(quiet, impressed) Huh."

    z "(from the wall, the faintest smirk) Look at that. Junior command."

    sel "(to Zira) Don't call it that."

    z "What should I call it?"

    sel "Operational integration."

    z "Sure. That."

    "Selene turns to Aeron. The room is watching — all of them. This is the moment it shifts."

    sel "From now on, you sit at this table for every operational briefing. You review every plan before it deploys."

    if scene_has(_current_scene_id, "challenged_plan"):
        sel "If you see something wrong, you say it. I'd rather fight with you in this room than bury people in the field because nobody spoke up."
    else:
        sel "You improve what needs improving. Quietly, efficiently, without breaking the chain."

    sel "Clear?"

    a "Clear."

    sel "Good."

    "She rolls the maps. Briefing over."

    "But before the room empties —"

    sel "(low, just to Aeron) One more thing."

    "The others file out. Zira lingers at the door, catches Aeron's eye, taps two fingers against her temple — her shorthand for 'not bad' — and leaves."

    sel "You were right about the scatter doctrine. I knew about the residential block."

    a "You knew?"

    sel "I wanted to see if you'd catch it. And what you'd do when you did."

    if scene_has(_current_scene_id, "challenged_plan"):
        sel "You challenged me. In front of my people. That took nerve."
        sel "Do it again if you need to. But pick your moments. Not everything is a test."
        sel "Some of them are just plans."
    else:
        sel "You corrected without confronting. That's harder than it looks."
        sel "Some people think command means the loudest voice. It doesn't."
        sel "It means the one that adjusts the fastest."

    athought "She tested me."
    athought "She placed the flaw. She waited. She watched what I'd do with it."

    if empathy_band() == "obedience":
        athought "Selene operates the way I was trained to operate. Test. Evaluate. Promote or discard."
        athought "I passed. But the test isn't over. It's never over with her."
    elif empathy_band() == "empathy":
        athought "She didn't need me to find the flaw. She needed to know I'd protect the people it threatened."
        athought "That's what she was measuring. Not my tactics. My temperature."
    else:
        athought "Commander who tests her officers by planting flaws in her own plans."
        athought "Either she's brilliant or she's dangerous. Probably both."

    sel "Welcome to the table, Aeron."

    "She extends her hand. Not warmth — recognition. The kind of handshake that means you've been weighed and not discarded."

    "Aeron takes it."

    "The gloves creak."

    # ========== STATE UPDATES ==========

    $ scene_mark(_current_scene_id, "anchor_seen")
    $ npc_remember("Selene", "command_temperature_passed", tone="respect")
    $ rel_bump("Selene", trust=1)
    $ canon_set("junior_command", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s21_command_temperature
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Day after Doctrine Declaration. Morning operations briefing.
#   - Pair Anchor A2_P04 (Aeron x Selene) — "Command Temperature."
# cann.what_happened:
#   - Selene briefs a supply corridor ambush. The plan has a deliberate flaw — a residential block
#     in the escort's scatter path that Selene planted as a test.
#   - Player choice: challenge the plan openly (EMP) or accept the framework and add a contingency (OB).
#   - Both paths identify the civilian risk. EMP confronts; OB adjusts quietly.
#   - Selene reveals the test after the room clears. She planted the flaw. She was measuring Aeron.
#   - Outcome: Aeron is promoted to junior command. Sits at every briefing. Reviews every plan.
#   - Zira's two-finger tap: "not bad."
#   - Selene's handshake: recognition, not warmth.
# cann.aeron_state:
#   - Using Echelon knowledge against Echelon. "I designed that conditioning."
#   - EMP: prioritizes civilian safety, challenges openly, claims "our team" ownership.
#   - OB: respects command chain, makes surgical improvements, demonstrates tactical value.
#   - Both paths earn the same promotion — but the way it's earned shapes the command dynamic going forward.
# cann.path_tracking:
#   - One choice_and_dev decision (factor=1):
#       - _challenged_plan → EMP +1 (confrontation for civilian safety, claims team ownership)
#       - _accepted_with_contingency → OB +1 (tactical improvement within chain of command)
#   - trust +1 for Selene on both paths.
#   - canon_set("junior_command") for future gating.
#   - Pair anchor A2_P04 marked as seen.
# cann.thematic_flags:
#   - "Command Temperature" — Selene testing the heat of Aeron's convictions under pressure.
#   - Aeron's Echelon expertise as double-edged: he knows the enemy because he WAS the enemy.
#   - "I identified a risk in front of OUR team." — EMP claiming ownership. "Ours" not "yours."
#   - "You corrected without confronting. That's harder than it looks." — OB as discipline, not cowardice.
#   - The planted flaw: Selene doesn't need better plans. She needs to know who catches the problems.
#   - Gloves creaking on the handshake. Selene's physicality as command language.
# cann.character_moments:
#   - Selene: Planted a flaw in her own plan to test a subordinate. That's either brilliant or dangerous.
#     She reveals the test privately — respects Aeron enough to not humiliate or over-praise in public.
#     The handshake is recognition, not friendship. She's building a command structure, not a bond.
#   - Zira: Two-finger tap at the door. Shorthand for approval. Economy of gesture.
#   - Cade: "He's got a point." (EMP path) — quiet validation from someone who follows Selene without question.
#     His acknowledgment of Aeron's competence matters because Cade doesn't give it easily.
# cann.block_status:
#   - ANCHOR (Pair Anchor A2_P04, both paths). Junior command promotion scene.
# cann.requires_followup:
#   - junior_command flag gates Aeron's presence at future briefings.
#   - EMP: Selene's "pick your moments" warning should echo — Aeron can't challenge every plan.
#   - OB: "adjusts the fastest" establishes the command style Selene expects.
#   - The supply corridor operation should be referenced later (did it succeed? were there complications?).
#   - Selene testing her officers becomes a pattern — she does this. It's how she builds trust.
