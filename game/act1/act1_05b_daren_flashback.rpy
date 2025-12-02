# =======================================================
# ACT 1 – Scene 5b: Daren Flashback
# File: act1_05b_daren_flashback.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_daren_flashback"
$ scene_mark(_current_scene_id, "entered")


label act1_daren_flashback:

    # VISUAL: Academy training room – dusk lighting, hard shadow; simulated urban environment.
    # SOUND: Soft electric hum of projectors; distant simulation gunfire.
    athought "The past doesn’t ask permission. It just arrives."

    # VISUAL: A younger Aeron (18) kneels behind cover—simulation weapon in hand, breath held.
    # VISUAL: Daren beside him—more polished, less anxious.
    cadet "Target left, two meters. Civilian profile."
    cadet "(tense) Wrong place, wrong time."
    cadet "Orders are clear. Clean sweep. No exceptions."

    # VISUAL: Aeron hesitates. Crosshairs hover. His finger lingers over the trigger.
    athought "I saw her. Just a girl. Simulation or not... she hesitated too."
    cadet "(sharper) Aeron."

    # VISUAL: Aeron fires. Sim target drops. Silence.
    athought "Scored a hit. Passed the test."
    athought "Daren smiled. The instructor nodded."
    athought "And I looked at my hands, like they’d done it on their own."

    # VISUAL: Cut to instructor clipboard — “PASS: RYLAN, A.”
    athought "They called it decisive. Said I had potential."
    athought "Said hesitation gets soldiers killed."

    # VISUAL: Final image — Aeron alone in the sim room, lights dimming.
    athought "That night, I stared at the wall until the lights went out."
    athought "Trying to remember the girl’s face. I couldn’t."

    $ set_scene_flag(_current_scene_id, "completed")

    return