# =======================================================
# ACT 1 - Scene 07a: Barracks Morning (Ritual, Rations, Rank)
# =======================================================

label act1_barracks_morning:

    # VISUAL: Barracks corridor → ration line → armory corridor
    # LIGHTING: Cool morning fluorescents. Even, unforgiving.
    # SOUND: Intercom cadence. ID gates beeping. Distant drill calls.

    #scene bg_barracks_corridor_morning with fade

    "{i}Barracks breathing in unison. Intercom teaches the day how to speak.{/i}"

    # INTERCOM
    voice "Stability is compassion. Precision is mercy. Latency kills."

    # RATION LINE — WORKER INCIDENT
    #scene bg_ration_line with dissolve

    "{i}Ration line. Green lights snap for ranks. Red for everyone else. A worker holds a chipped card like an apology.{/i}"
    guard "Priority queue. Step aside."
    worker "My child—"
    guard "Step. Aside."

    # CHOICE: intervene vs ignore vs endorse
    menu:
        "Quietly restore the worker's ration chip while the guard looks away.":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_barracks_morning", "helped_worker")
            $ add_item("supplies", "food", 1)
            "{i}I tilt the worker's card under the scanner. A green blink pretends nothing happened. The guard doesn't turn.{/i}"
            worker "(whisper) Thank you."
        "Ignore it and move forward in line.":
            "{i}Green opens for me. Red stays red. The line learns its lesson.{/i}"
        "Tell the guard to advance priority flow per protocol.":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_barracks_morning", "endorsed_priority")
            guard "(approving) Copy. Keep the lane clean."
            "{i}Order is a broom. People are dust.{/i}"

    # QUARTERMASTER / JUNIOR RECRUIT — REPUTATION POLISH
    #scene bg_armory_counter with fade

    qm "Unit Seven. Pull ticket, sign. Ammunition allotment registered."
    jr "Sir—how do you polish a reputation report? They flag my 'latency' on simulations."

    menu:
        "Teach him a humane frame: 'Stabilize civilians first; then pursue objective.'":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_barracks_morning", "mentored_humane")
            jr "(relieved) Stabilize first. Then objective. Got it."
            "{i}He writes it like a prayer that might pass for policy.{/i}"
        "Teach him the clinical script: 'Neutralize; collateral within tolerance.'":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_barracks_morning", "mentored_clinical")
            jr "(grim) Neutralize. Tolerance."
            "{i}He looks smaller repeating it.{/i}"
        "Tell him to keep his head down and copy senior phrasing.":
            "{i}He nods. Survival as grammar.{/i}"

    # EXIT
    voice "Units scheduled for demonstration: report at 14:00."
    "{i}The hallway empties like a throat clearing. Fourteen-hundred writes itself behind my eyes.{/i}"

    return
