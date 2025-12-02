# ===================================================
# ACT 1 - Scene 3: Morning Routine
# File: act1_03_morning_routing.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_03_morning_routine"
$ scene_mark(_current_scene_id, "entered")


label act1_morning_routine:

    # VISUAL: FADE IN — Aeron’s quarters, morning.
    # CAMERA: 40mm static mid-shot toward window; white morning glare bleeds through glass.
    # COLOR: cold, neutral; slight bloom from exterior light.
    # SOUND: faint ventilation hum; city drone below; soft ticking clock somewhere off-screen.

    "Morning arrives like a schedule — punctual, indifferent."

    "The mission is logged. Filed. Forgotten."
    "Today, a different performance awaits."

    # VISUAL: Bathroom mirror; condensation fading; Aeron off-screen silhouette.
    # CAMERA: Shoulder-level, soft reflection only; he’s indistinct.
    # SOUND: dripping tap; faint echo.

    athought "Morning feels mechanical. Wake. Wash. Dress. Repeat."

    athought "Last night: soldier. Tonight: son."
    athought "Same uniform. Different lies."

    # VISUAL: Cut — uniform folded on bed, soft ambient light streaks across medals.
    # PROP DETAIL: Black fabric with silver piping; Echelon insignia inset in chrome.
    athought "The mirror shows what I'm supposed to be. The uniform makes it official."

    "The dress uniform hangs like a costume. Every crease pressed. Every medal aligned."
    # FX: subtle glint on medal edges; 5600K light.

    # MEMORY — KAEL CALLBACK
    # VISUAL: Quick white flash; insert frame — Kael in same uniform, younger, confident.
    # COLOR: warmer, nostalgic; flicker back to cold present.
    athought "Kael wore his like armor. Stood taller. Smiled wider."
    athought "I wear mine like a screen. Reflecting what they want to see. Hiding the rest."
    athought "His didn't save him either."

    # PLAYER CHOICE — early empathy micro-weight
    menu:
        "In the mirror, you're alone. But not empty. Something lingers beneath the surface..."
        "Let yourself remember":
            $ choice_and_dev(_current_scene_id, "_remember_it", "EMP", factor=1,
                    next_scene_label="act1_04_hallway",
                    note="Remembers the memory")

            athought "His smile. His silence. The way he still stood tall after they marked him broken."
            athought "He wore this same collar — but never let it define him."
            athought "He was human to the end. Can I still be?"

        "Bury it":
            $ choice_and_dev(_current_scene_id, "_buries_it", "OB", factor=1,
                    next_scene_label="act1_04_hallway",
                    note="Buries the memory")

            athought "This isn't the time for ghosts. You're not a boy grieving."
            athought "You're what they built — efficient, trained, necessary."
            athought "Let the memory stay buried. You have a job to do."

    # VISUAL: Automated wardrobe assistant powers on.
    # PROP: Blue scan grid passes over uniform; small text overlay “CONFIG: CEREMONIAL”.
    # SFX: soft chime → system voice, sterile feminine tone.

    "Wardrobe Assistant" "Good morning, Aeron. Dress uniform prepared for Gala attendance. Estimated departure: 18:47."
    "Wardrobe Assistant" "Would you like the full ceremonial configuration?"

    athought "Full ceremonial. Medals and all. The whole performance."
    athought "I don’t need decorations. But the audience expects the illusion."

    # COLLAR MOMENT
    # VISUAL: Close-up — Aeron fastening collar; subtle constriction at throat.
    # CAMERA: Macro 85mm lens equivalent; focus rack from fabric to Adam’s apple.
    # LIGHT: cold overhead LED; rim light from left.
    athought "The collar sits tight."
    athought "Just tight enough to remind me who this uniform belongs to."
    athought "Breathing’s optional at these events anyway."

    # MIRROR REVEAL
    # VISUAL: Aeron fully dressed, posture rigid, expression neutral.
    # CAMERA: mirror POV; faint distortion lines in glass to echo "Glass" motif.
    athought "There. General Rylan’s son. Ready for inspection."
    athought "Exactly what they expect."
    athought "Polished. Presentable. Perfect."
    athought "Empty."

    # DEPARTURE
    # VISUAL: Door slides open; cold daylight floods hall; he steps out.
    # SOUND: Pneumatic hiss, then ambient city tone.
    athought "The mirror shows the uniform. Not the blood from last night."
    athought "Not the family. Not the metrics. Not the ninety-nine point seven."
    athought "Just another uniform, ready to perform."
    athought "Time to face the world."

    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id:
#   act1_03_morning_routine  (Act I — Scene 3)
# cann.when_in_timeline:
#   Morning following Operation 390; pre-gala preparation; Aeron resumes civilian-facing persona.
# cann.what_happened (objective canon summary):
#   - Aeron completes ritualized morning routine in aftermath of Sector 7 mission.
#   - Mirrors, uniforms, and automation reinforce performance vs identity motif.
#   - Kael memory resurfaces; player decides whether to indulge or suppress it.
#   - Wardrobe Assistant configures ceremonial attire for gala (departure 18:47).
#   - Reinforces theme: “Glass as reflection” — function obeying image.
# cann.aeron_state:
#   OB-lean read:
#     Rigid composure; channels grief into precision; defines self entirely by constructed role.
#   EMP-lean read:
#     The Kael memory opens a wound; awareness of humanity flickers beneath obedience.
#   Neutral summary:
#     Transitioning from soldier mindset to public façade; compartmentalization near total.
# cann.path_tracking:
#   empathy_score_range_so_far:
#     min_emp_possible: -2   # from earlier obedience + bury_it
#     max_emp_possible:  3   # from earlier empathy + remember
#   notes:
#     - Choice maintains micro-weight path_pressure (×1).
#     - “remember” increases early True Path resonance seed potential (see note below).
# cann.thematic_flags:
#   motifs_used:
#     - Glass / Reflection / Collar Constraint / Automation
#   recurring_lines_seeded:
#     - “Same uniform. Different lies.” / “Polished. Presentable. Perfect. Empty.”
#   continuity_asserts:
#     - Operation 390 occurred previous night (reference 99.7% efficiency).
#     - Collar tightness = recurring control motif.
#     - Aeron wears medals flag affects elite reactions during Act I Gala.
# cann.block_status:
#   anchor_or_variant:
#     ANCHOR   # core narrative bridge from mission identity to gala performance
#   requires_followup:
#     - act1_04_gala (Aeron’s reintroduction into public / elite sphere)
# cann.true_path_integration:
#   - “Let yourself remember” increments early True Path resonance trigger by +1.
#   - True Path tracks accumulation of *unrepressed empathy moments* across both branches.
#   - This scene’s memory acceptance counts toward that invisible meter (resonance > 3 by Act 2 = unlock).