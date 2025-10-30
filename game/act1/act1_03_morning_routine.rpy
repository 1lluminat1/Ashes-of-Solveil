# ===================================================
# ACT 1 - Scene 3: Morning Routine
# ===================================================

label act1_morning_routine:

    # VISUAL: FADE IN — Aeron’s quarters, morning.
    # CAMERA: 40mm static mid-shot toward window; white morning glare bleeds through glass.
    # COLOR: cold, neutral; slight bloom from exterior light.
    # SOUND: faint ventilation hum; city drone below; soft ticking clock somewhere off-screen.

    "{i}Morning arrives like a schedule — punctual, indifferent.{/i}"
    pause 0.7

    "{i}The mission is logged. Filed. Forgotten.{/i}"
    pause 0.8
    "{i}Today, a different performance awaits.{/i}"
    pause 0.8

    # VISUAL: Bathroom mirror; condensation fading; Aeron off-screen silhouette.
    # CAMERA: Shoulder-level, soft reflection only; he’s indistinct.
    # SOUND: dripping tap; faint echo.

    a "{i}Morning feels mechanical. Wake. Wash. Dress. Repeat.{/i}"
    pause 0.7

    a "{i}Last night: soldier. Tonight: son.{/i}"
    pause 0.7
    a "{i}Same uniform. Different lies.{/i}"
    pause 0.8

    # VISUAL: Cut — uniform folded on bed, soft ambient light streaks across medals.
    # PROP DETAIL: Black fabric with silver piping; Echelon insignia inset in chrome.
    a "{i}The mirror shows what I'm supposed to be. The uniform makes it official.{/i}"
    pause 0.8

    "{i}The dress uniform hangs like a costume. Every crease pressed. Every medal aligned.{/i}"
    # FX: subtle glint on medal edges; 5600K light.
    pause 0.9

    # MEMORY — KAEL CALLBACK
    # VISUAL: Quick white flash; insert frame — Kael in same uniform, younger, confident.
    # COLOR: warmer, nostalgic; flicker back to cold present.
    a "{i}Kael wore his like armor. Stood taller. Smiled wider.{/i}"
    pause 0.7
    a "{i}I wear mine like a screen. Reflecting what they want to see. Hiding the rest.{/i}"
    pause 0.8
    a "{i}His didn't save him either.{/i}"
    pause 1.0

    # PLAYER CHOICE — early empathy micro-weight
    menu:
        "In the mirror, you're alone. But not empty. Something lingers beneath the surface...":

        "Let yourself remember":
            $ adjust_empathy_once("act1_03_let_remember", 1)
            a "{i}His smile. His silence. The way he still stood tall after they marked him broken.{/i}"
            pause 0.8
            a "{i}He wore this same collar — but never let it define him.{/i}"
            pause 0.7
            a "{i}He was human to the end. Can I still be?{/i}"
            pause 1.0

        "Bury it":
            $ adjust_empathy_once("act1_03_bury_it", -1)
            a "{i}This isn't the time for ghosts. You're not a boy grieving.{/i}"
            pause 0.7
            a "{i}You're what they built — efficient, trained, necessary.{/i}"
            pause 0.7
            a "{i}Let the memory stay buried. You have a job to do.{/i}"
            pause 0.9

    # VISUAL: Automated wardrobe assistant powers on.
    # PROP: Blue scan grid passes over uniform; small text overlay “CONFIG: CEREMONIAL”.
    # SFX: soft chime → system voice, sterile feminine tone.

    "Wardrobe Assistant" "Good morning, Aeron. Dress uniform prepared for Gala attendance. Estimated departure: 18:47."
    pause 0.6
    "Wardrobe Assistant" "Would you like the full ceremonial configuration?"
    pause 0.6

    a "{i}Full ceremonial. Medals and all. The whole performance.{/i}"
    pause 0.7
    a "{i}I don’t need decorations. But the audience expects the illusion.{/i}"
    pause 0.9

    # COLLAR MOMENT
    # VISUAL: Close-up — Aeron fastening collar; subtle constriction at throat.
    # CAMERA: Macro 85mm lens equivalent; focus rack from fabric to Adam’s apple.
    # LIGHT: cold overhead LED; rim light from left.
    a "{i}The collar sits tight.{/i}"
    pause 0.7
    a "{i}Just tight enough to remind me who this uniform belongs to.{/i}"
    pause 0.7
    a "{i}Breathing’s optional at these events anyway.{/i}"
    pause 0.8

    # MIRROR REVEAL
    # VISUAL: Aeron fully dressed, posture rigid, expression neutral.
    # CAMERA: mirror POV; faint distortion lines in glass to echo "Glass" motif.
    a "{i}There. General Rylan’s son. Ready for inspection.{/i}"
    pause 0.7

    a "{i}Exactly what they expect.{/i}"
    pause 0.6
    a "{i}Polished. Presentable. Perfect.{/i}"
    pause 0.6
    a "{i}Empty.{/i}"
    pause 0.9

    # DEPARTURE
    # VISUAL: Door slides open; cold daylight floods hall; he steps out.
    # SOUND: Pneumatic hiss, then ambient city tone.
    a "{i}The mirror shows the uniform. Not the blood from last night.{/i}"
    pause 0.7
    a "{i}Not the family. Not the metrics. Not the ninety-nine point seven.{/i}"
    pause 0.8
    a "{i}Just another uniform, ready to perform.{/i}"
    pause 0.8
    a "{i}Time to face the world.{/i}"
    pause 1.0

    return


    # cann: ===============================
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
    #
    # cann.true_path_integration:
    #   - “Let yourself remember” increments early True Path resonance trigger by +1.
    #   - True Path tracks accumulation of *unrepressed empathy moments* across both branches.
    #   - This scene’s memory acceptance counts toward that invisible meter (resonance > 3 by Act 2 = unlock).
    # cann: ===============================
