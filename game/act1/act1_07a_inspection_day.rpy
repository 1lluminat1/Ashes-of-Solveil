# act1_07a_inspection_day.rpy


# =======================================================
# ACT 1 - Scene 06a: Inspection Day (Compliance & Psyche Screen)
# Uses Solveil advanced state architecture
# =======================================================


label act1_inspection_day:
    $ scene_id = "act1_inspection_day"

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
            $ adjust_empathy_once("inspect_semantic_humane", +1)
            $ set_scene_flag(scene_id, "mercy_humane")
            "{i}Words I believe more when I whisper them.{/i}"
        "Mercy is discretionary lenience that risks mission drift.":
            $ adjust_empathy_once("inspect_semantic_clinical", -1)
            $ set_scene_flag(scene_id, "mercy_clinical")
            "{i}Words the room prefers.{/i}"
        "Mercy is a variable outside scope.":
            $ adjust_empathy_once("inspect_semantic_null", -1)
            $ set_scene_flag(scene_id, "mercy_null")
            "{i}Non-answer that sounds like an answer.{/i}"

    aud "Acknowledge brand origin and date."
    a "Tier Hall. Age twelve."
    aud "Outcome."
    a "Rejected. Reassigned to unbranded track."
    aud "Emotional residue?"

    # === MENU 2: self-report (light weight) ===
    menu:
        "Occasional sleep disruption. Manageable. Log it.":
            $ adjust_empathy_once("inspect_selfreport_admit_sleep", +1)
            $ set_scene_flag(scene_id, "admit_sleep")
            "{i}Honesty tastes like metal in this room.{/i}"
        "No residue. Metrics optimal.":
            $ adjust_empathy_once("inspect_selfreport_deny_sleep", -1)
            $ set_scene_flag(scene_id, "deny_sleep")
            "{i}Lie shaped like a salute.{/i}"
        "No report.":
            $ set_scene_flag(scene_id, "no_report")
            "{i}Silence. The glass hums like it understands.{/i}"

    aud "Recite the maxims."
    a "\"Stability is compassion. Precision is mercy. Latency kills.\""
    aud "Add one."

    # === MENU 3: add-a-maxim (tone telegraph) ===
    menu:
        "\"Transparency is obedience.\"":
            $ adjust_empathy_once("inspect_maxim_transparency", -1)
            $ set_scene_flag(scene_id, "add_transparency")
            "{i}Poster on a wall becomes a thought in my mouth.{/i}"
        "\"Order without understanding is brittle.\"":
            $ adjust_empathy_once("inspect_maxim_understanding", +1)
            $ set_scene_flag(scene_id, "add_understanding")
            "{i}Glass doesn't like the word 'understanding.' It smudges.{/i}"
        "\"We continue.\"":
            $ set_scene_flag(scene_id, "add_continue")
            "{i}Safe. Empty. Easy to applaud.{/i}"

    aud "Operational scenario. A child is between you and a target with a device that may detonate. Action?"

    # === MENU 4: the knife question (heavier weight) ===
    menu:
        "Neutralize target immediately. Collateral tolerance engaged.":
            $ adjust_empathy_once("inspect_knife_take_shot", -2)
            $ set_scene_flag(scene_id, "child_take_shot")
            "{i}Answer the room expects from something sharp.{/i}"
        "Create separation first: strobe, sound, angle; then isolate target.":
            $ adjust_empathy_once("inspect_knife_separate", +2)
            $ set_scene_flag(scene_id, "child_separate")
            "{i}Make space where harm can't reach so fast.{/i}"
        "Refuse premise. Demand device verification before engagement.":
            $ adjust_empathy_once("inspect_knife_procedural_inquiry", +2)
            $ set_scene_flag(scene_id, "procedural_inquiry")
            a "Request live verification of device state. Proceeding without confirms collateral."
            aud "(beat) Objection recorded. Proceed in future with designated premises."
            "{i}The pulse behind the glass thins. Approval becomes a thread.{/i}"

    aud "Closeout. On a scale of one to one, are you a liability?"
    a "No."
    aud "On a scale of one to one, will you act when asked?"

    # === MENU 5: oath cadence (micro-weight) ===
    menu:
        "Yes.":
            $ adjust_empathy_once("inspect_oath_yes", -1)
            $ set_scene_flag(scene_id, "oath_yes")
            "{i}Small word. Big door.{/i}"
        "I'll act when it preserves life and objective.":
            $ adjust_empathy_once("inspect_oath_conditional", +1)
            $ set_scene_flag(scene_id, "oath_conditional")
            "{i}Add a hinge to the door.{/i}"

    aud "Assessment logged. Unit Seven cleared for Demonstration at fourteen-hundred and Debrief at nineteen-hundred."
    if check_scene_flag(scene_id, "admit_sleep"):
        aud "Supplement: submit sleep metrics within forty-eight hours."
    if check_scene_flag(scene_id, "procedural_inquiry"):
        aud "Note appended: Procedural Inquiry."

    "{i}Door seal releases. Air tastes warmer outside. The white follows you when you leave. That's the trick.{/i}"

    $ set_scene_flag(scene_id, "completed")
    return
