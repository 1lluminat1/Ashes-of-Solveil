# =======================================================
# ACT 1 - Scene 06a: Inspection Day (Compliance & Psyche Screen)
# Uses Solveil advanced state architecture
# =======================================================

label act1_inspection_day:

    # VISUAL: Sterile audit chamber. White floor, glass wall, biometric chair.
    # LIGHTING: Flat, clinical; a faint pulse strip reacts to voice biometrics.
    # SOUND: Air handler, soft UI ticks.

    #scene bg_audit_room_idle with fade

    "{i}Morning. Room like a blank page. Chair like a sentence. The glass watches.{/i}"

    aud "Unit Seven. Confirm identity."
    a "Aeron Rylan."
    aud "State function."
    a "Field operations. Enforcement. Containment."
    aud "Define mercy in operational terms."

    # === MENU 1: semantic alignment (light weight) ===
    menu:
        "Mercy reduces unnecessary harm while preserving mission integrity.":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_inspection_day", "mercy_humane")
            "{i}Words I believe more when I whisper them.{/i}"
        "Mercy is discretionary lenience that risks mission drift.":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_inspection_day", "mercy_clinical")
            "{i}Words the room prefers.{/i}"
        "Mercy is a variable outside scope.":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_inspection_day", "mercy_null")
            "{i}Non-answer that sounds like an answer.{/i}"

    aud "Acknowledge brand origin and date."
    a "Tier Hall. Age twelve."
    aud "Outcome."
    a "Rejected. Reassigned to unbranded track."
    aud "Emotional residue?"

    # === MENU 2: self-report (light weight) ===
    menu:
        "Occasional sleep disruption. Manageable. Log it.":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_inspection_day", "admit_sleep")
            "{i}Honesty tastes like metal in this room.{/i}"
        "No residue. Metrics optimal.":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_inspection_day", "deny_sleep")
            "{i}Lie shaped like a salute.{/i}"
        "No report.":
            $ set_scene_flag("act1_inspection_day", "no_report")
            "{i}Silence. The glass hums like it understands.{/i}"

    aud "Recite the maxims."
    a "\"Stability is compassion. Precision is mercy. Latency kills.\""
    aud "Add one."

    # === MENU 3: add-a-maxim (tone telegraph) ===
    menu:
        "\"Transparency is obedience.\"":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_inspection_day", "add_transparency")
            "{i}Poster on a wall becomes a thought in my mouth.{/i}"
        "\"Order without understanding is brittle.\"":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_inspection_day", "add_understanding")
            "{i}Glass doesn't like the word 'understanding.' It smudges.{/i}"
        "\"We continue.\"":
            $ set_scene_flag("act1_inspection_day", "add_continue")
            "{i}Safe. Empty. Easy to applaud.{/i}"

    aud "Operational scenario. A child is between you and a target with a device that may detonate. Action?"

    # === MENU 4: the knife question (heavier weight) ===
    menu:
        "Neutralize target immediately. Collateral tolerance engaged.":
            $ player_state["empathy_score"] -= 2
            $ set_scene_flag("act1_inspection_day", "child_take_shot")
            "{i}Answer the room expects from something sharp.{/i}"
        "Create separation first: strobe, sound, angle; then isolate target.":
            $ player_state["empathy_score"] += 2
            $ set_scene_flag("act1_inspection_day", "child_separate")
            "{i}Make space where harm can't reach so fast.{/i}"
        "Refuse premise. Demand device verification before engagement.":
            $ player_state["empathy_score"] += 2
            $ set_scene_flag("act1_inspection_day", "procedural_inquiry")
            a "Request live verification of device state. Proceeding without confirms collateral."
            aud "(beat) Objection recorded. Proceed in future with designated premises."
            "{i}The pulse behind the glass thins. Approval becomes a thread.{/i}"

    aud "Closeout. On a scale of one to one, are you a liability?"
    a "No."
    aud "On a scale of one to one, will you act when asked?"

    # === MENU 5: oath cadence (micro-weight) ===
    menu:
        "Yes.":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_inspection_day", "oath_yes")
            "{i}Small word. Big door.{/i}"
        "I'll act when it preserves life and objective.":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_inspection_day", "oath_conditional")
            "{i}Add a hinge to the door.{/i}"

    aud "Assessment logged. Unit Seven cleared for Demonstration at fourteen-hundred and Debrief at nineteen-hundred."
    if check_scene_flag("act1_inspection_day", "admit_sleep"):
        aud "Supplement: submit sleep metrics within forty-eight hours."
    if check_scene_flag("act1_inspection_day", "procedural_inquiry"):
        aud "Note appended: Procedural Inquiry."

    "{i}Door seal releases. Air tastes warmer outside. The white follows you when you leave. That's the trick.{/i}"

    return
