# act1_07b_barracks_morning.rpy


# =======================================================
# ACT 1 - Scene 07a: Barracks Morning (Ritual, Rations, Rank)
# with momentum flavor (subtle)
# =======================================================


label act1_barracks_morning:
    $ scene_id = "act1_barracks_morning"

    #scene bg_barracks_corridor_morning with fade

    "{i}Barracks breathing in unison. Intercom teaches the day how to speak.{/i}"

    voice "Stability is compassion. Precision is mercy. Latency kills."

    # RATION LINE — WORKER INCIDENT
    "{i}Ration line. Green lights snap for ranks. Red for everyone else. A worker holds a chipped card like an apology.{/i}"
    guard "Priority queue. Step aside."
    worker "My child—"
    guard "Step. Aside."

    menu:
        "Quietly restore the worker's ration chip while the guard looks away.":
            $ adjust_empathy_once("barracks_worker_help", +1)
            $ set_scene_flag(scene_id, "helped_worker")
            $ add_item("supplies", "food", 1)
            "{i}I tilt the worker's card under the scanner. A green blink pretends nothing happened. The guard doesn't turn.{/i}"
            worker "(whisper) Thank you."
        "Ignore it and move forward in line.":
            "{i}Green opens for me. Red stays red. The line learns its lesson.{/i}"
        "Tell the guard to advance priority flow per protocol.":
            $ adjust_empathy_once("barracks_worker_endorse_priority", -1)
            $ set_scene_flag(scene_id, "endorsed_priority")
            guard "(approving) Copy. Keep the lane clean."
            "{i}Order is a broom. People are dust.{/i}"

    # Alignment flavor: ration incident
    $ band = get_empathy_band()
    if check_scene_flag(scene_id, "helped_worker"):
        if band == "obedience":
            a "{i}Anomalous gesture. I file it under throughput optimization and keep moving.{/i}"
        elif band == "conflicted":
            a "{i}Small fix in a broken queue. Not nothing. Not enough.{/i}"
        else:
            a "{i}One green light where it mattered. The system will never notice. I will.{/i}"
    elif check_scene_flag(scene_id, "endorsed_priority"):
        if band == "obedience":
            a "{i}Flow restored. Metrics satisfied. Silence resumes.{/i}"
        elif band == "conflicted":
            a "{i}Protocol holds. Something in my chest doesn’t.{/i}"
        else:
            a "{i}The lane is clean. My conscience isn’t.{/i}"

    # Momentum whisper (ration)
    $ mom = get_alignment_momentum()  # -1..+1 recent trend
    if mom >= 0.5:
        a "{i}Lately the choices are leaning human. Maybe that’s the point.{/i}"
    elif mom <= -0.5:
        a "{i}Lately the edge comes easier. Habit wearing a uniform.{/i}"

    # QUARTERMASTER / JUNIOR RECRUIT — REPUTATION POLISH
    qm "Unit Seven. Pull ticket, sign. Ammunition allotment registered."
    jr "Sir—how do you polish a reputation report? They flag my 'latency' on simulations."

    menu:
        "Teach him a humane frame: 'Stabilize civilians first; then pursue objective.'":
            $ adjust_empathy_once("barracks_mentor_humane", +1)
            $ set_scene_flag(scene_id, "mentored_humane")
            jr "(relieved) Stabilize first. Then objective. Got it."
            "{i}He writes it like a prayer that might pass for policy.{/i}"
        "Teach him the clinical script: 'Neutralize; collateral within tolerance.'":
            $ adjust_empathy_once("barracks_mentor_clinical", -1)
            $ set_scene_flag(scene_id, "mentored_clinical")
            jr "(grim) Neutralize. Tolerance."
            "{i}He looks smaller repeating it.{/i}"
        "Tell him to keep his head down and copy senior phrasing.":
            "{i}He nods. Survival as grammar.{/i}"

    # Alignment flavor: recruit advice
    $ band = get_empathy_band()
    if check_scene_flag(scene_id, "mentored_humane"):
        if band == "obedience":
            a "{i}Language won’t save him. Maybe it buys him a breath.{/i}"
        elif band == "conflicted":
            a "{i}The right words can tilt a trigger-finger. Sometimes that’s enough.{/i}"
        else:
            a "{i}If he remembers the people first, maybe the report won’t have to lie for him.{/i}"
    elif check_scene_flag(scene_id, "mentored_clinical"):
        if band == "obedience":
            a "{i}He’ll pass the audit. Passing is what keeps you alive here.{/i}"
        elif band == "conflicted":
            a "{i}I handed him the script that hollows you out. I know how it ends.{/i}"
        else:
            a "{i}I put the weight in his mouth and told him to carry it. The system calls that training.{/i}"

    # Momentum whisper (recruit)
    $ mom = get_alignment_momentum()
    if mom >= 0.5:
        a "{i}The trend’s been softer. Maybe I’m teaching myself as much as him.{/i}"
    elif mom <= -0.5:
        a "{i}The trend’s been colder. Easier to hand out the mask than take it off.{/i}"

    # EXIT
    voice "Units scheduled for demonstration: report at 14:00."
    "{i}The hallway empties like a throat clearing. Fourteen-hundred writes itself behind my eyes.{/i}"

    $ set_scene_flag(scene_id, "completed")
    return
