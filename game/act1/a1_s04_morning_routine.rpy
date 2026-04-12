# ===================================================
# ACT 1 - Scene 3: Morning Routine
# File: act1_03_morning_routing.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a1_s04_morning_routine"
$ scene_mark(_current_scene_id, "entered")


label a1_s04_morning_routine:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: 40mm static mid-shot toward window; white morning glare bleeds through glass.
    # LIGHTING: Cold, neutral; slight bloom from exterior light. Overexposed window.
    # SFX: Faint ventilation hum; city drone below; soft ticking clock off-screen.
    # BLOCKING: Aeron's quarters. Bed made with military precision. Uniform laid out.
    # TIME: Morning after Operation 390. Gala is tonight.

    "Morning arrives on schedule—punctual, indifferent, already too bright."

    athought "Four hours of sleep. Not enough to wash the 99.7%% out of my head."

    athought "The mission is logged, filed, supposedly forgotten. Today, a different performance awaits."

    # ========= BATHROOM — MIRROR =========
    # CAMERA: Shoulder-level, soft reflection only; Aeron's silhouette indistinct in condensation.
    # LIGHTING: Cool overhead LED; steam diffusing the edges.
    # SFX: Dripping tap; faint echo off tile.
    # SYMBOL: Identity obscured—he's not fully formed yet in this scene.

    "Condensation clings to the mirror, blurring the edges of everything."

    # [OVER-CLOSURE TRIM] was: athought "Morning feels mechanical—wake, wash, dress, repeat."
    # [OVER-CLOSURE TRIM] was: athought "Last night: soldier. Tonight: son. Same uniform, different lies."
    # Both lines diagnose the scene's thesis before it earns it. Let the routine show the mechanical.

    "The tap drips. He counts three drops before turning it off."

    # ========= UNIFORM ON BED =========
    # CAMERA: Cut to uniform folded on bed; soft ambient light streaks across medals.
    # PROP DETAIL: Black fabric with silver piping; Echelon insignia inset in chrome.
    # FX: Subtle glint on medal edges; 5600K light.

    "The dress uniform hangs like a costume—every crease pressed, every medal aligned to the millimeter."

    # [OVER-CLOSURE TRIM] was: athought "The mirror shows what I'm supposed to be. The uniform makes it official."
    # Mirror + uniform + identity already established in s02. This line re-states. Cut.

    # ========= MEMORY — KAEL CALLBACK =========
    # VISUAL: Quick white flash; insert frame—Kael in same uniform, younger, confident.
    # COLOR: Warmer, nostalgic tone; flicker back to cold present.
    # NOTE: Keep insert brief (0.3s). The warmth should feel intrusive.

    athought "Kael wore his like armor—stood taller, smiled wider."

    # [OVER-CLOSURE TRIM] was: athought "I wear mine like a screen, reflecting what they want to see, hiding the rest. His didn't save him either."
    # "Kael wore his like armor" is the strong image. The contrast line over-explains. Replace with the gut punch:

    athought "His didn't save him either."

    # ========= PLAYER CHOICE — KAEL MEMORY =========
    # NOTE: Early empathy micro-weight. Affects True Path resonance tracking.

    # [OVER-CLOSURE TRIM] was: athought "In the mirror, I'm alone. But not empty. Something lingers beneath the surface."
    # Too interpretive as a choice prompt. The Kael flash is the prompt.
    menu:

        "Let yourself remember":
            $ choice_and_dev(_current_scene_id, "_remember_it", "EMP", factor=1,
                    next_scene_label="a1_s05_hallway",
                    note="Remembers the memory")
            $ tp_seed("a1.morning.kael_memory")

            athought "His smile, his silence, the way he still stood tall after they marked him broken."

            # [OVER-CLOSURE TRIM] was: athought "He wore this same collar but never let it define him. He was human to the end."
            # "collar" and "define" re-state what the smile/silence image already carried. Keep only the question:

            athought "Can I still be?"

        "Bury it":
            $ choice_and_dev(_current_scene_id, "_buries_it", "OB", factor=1,
                    next_scene_label="a1_s05_hallway",
                    note="Buries the memory")

            athought "This isn't the time for ghosts. I'm not a boy grieving anymore."

            # [OVER-CLOSURE TRIM] was: athought "I'm what they built—efficient, trained, necessary. Let the memory stay buried. There's a job to do."
            # "This isn't the time for ghosts" already carries the suppression. The second line is thesis delivery.

            "He straightens. The condensation on the mirror is already clearing."

    # ========= WARDROBE ASSISTANT =========
    # VISUAL: Automated wardrobe unit powers on; blue scan grid passes over uniform.
    # PROP: Small text overlay "CONFIG: CEREMONIAL" on display panel.
    # SFX: Soft chime → system voice, sterile feminine tone.

    "The wardrobe unit hums to life—a scan grid washing blue across the fabric."

    "Wardrobe Assistant" "Good morning, Aeron. Dress uniform prepared for Gala attendance. Estimated departure: 18:47."
    "Wardrobe Assistant" "Would you like the full ceremonial configuration?"

    athought "Full ceremonial. Medals and all."

    # [OVER-CLOSURE TRIM] was: athought "The whole performance."
    # [OVER-CLOSURE TRIM] was: athought "I don't need decorations, but the audience expects the illusion."
    # "Performance" and "illusion" restate what s02 already established. One beat is enough.

    # ========= COLLAR MOMENT =========
    # CAMERA: Macro 85mm equivalent; close-up on collar fastening. Focus rack from fabric to throat.
    # LIGHTING: Cold overhead LED; rim light from left catches the insignia.
    # SOUND: Soft click of clasp. Fabric tension.
    # SYMBOL: Collar = control. Recurring motif throughout Act I.

    "The clasp clicks into place—fabric pressing flush against the throat."

    athought "The collar sits tight, just tight enough to remind me who this uniform belongs to."

    athought "Breathing's optional at these events anyway."

    # ========= MIRROR REVEAL =========
    # CAMERA: Mirror POV; Aeron fully dressed, posture rigid, expression neutral.
    # VISUAL: Faint distortion lines in mirror surface—imperfection in the reflection.
    # LIGHTING: Even, clinical. No shadows on face.

    "The mirror holds a finished product—posture rigid, expression calibrated, every element in place."

    athought "There. General Rylan's son, ready for inspection."

    # [OVER-CLOSURE TRIM] was: athought "Exactly what they expect—polished, presentable, perfect, empty."
    # "Ready for inspection" is the image. "Polished, presentable, perfect, empty" is the author securing it.
    # Replace with a physical detail that carries the emptiness without naming it:

    "The distortion lines in the mirror make his jawline waver. He doesn't adjust them."

    # ========= DEPARTURE =========
    # VISUAL: Door slides open; cold daylight floods the hallway beyond.
    # SFX: Pneumatic hiss, then ambient city tone bleeds in.
    # CAMERA: Hold on Aeron's back as he steps through threshold.

    "The door hisses open. Daylight spills in—harsh and white, already too warm."

    # [OVER-CLOSURE TRIM] was: athought "The mirror shows the uniform, not the blood from last night—not the family, not the metrics, not the 99.7."
    # [OVER-CLOSURE TRIM] was: athought "Just another uniform, ready to perform. Time to face the world."
    # The scene already carried all of this. The exit should be physical, not summary.

    athought "99.7."

    "The door hisses shut behind him."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id:
#   a1_s04_morning_routine  (Act I — Scene 3)
# cann.when_in_timeline:
#   Morning following Operation 390; pre-gala preparation; Aeron resumes civilian-facing persona.
# cann.what_happened (objective canon summary):
#   - Aeron completes ritualized morning routine in aftermath of Sector 7 mission.
#   - Mirrors, uniforms, and automation reinforce performance vs identity motif.
#   - Kael memory resurfaces; player decides whether to indulge or suppress it.
#   - Wardrobe Assistant configures ceremonial attire for gala (departure 18:47).
#   - Sleep deprivation noted (4 hours); 99.7% efficiency haunts him.
# cann.aeron_state:
#   OB-lean read:
#     Rigid composure; channels grief into precision; defines self entirely by constructed role.
#   EMP-lean read:
#     The Kael memory opens a wound; awareness of humanity flickers beneath obedience.
#   Neutral summary:
#     Transitioning from soldier mindset to public façade; compartmentalization near total.
# cann.path_tracking:
#   empathy_score_range_so_far:
#     min_emp_possible: -3   # from earlier obedience choices + bury_it
#     max_emp_possible:  3   # from earlier empathy choices + remember
#   notes:
#     - Choice maintains micro-weight path_pressure (×1).
#     - "remember" increases early True Path resonance seed potential.
# cann.thematic_flags:
#   motifs_used:
#     - Reflection / Collar Constraint / Automation / Performance
#   recurring_lines_seeded:
#     - "Same uniform, different lies." / "Polished, presentable, perfect, empty."
#   continuity_asserts:
#     - Operation 390 occurred previous night (99.7% efficiency reference).
#     - Collar tightness = recurring control motif.
#     - Aeron wears medals flag affects elite reactions during Act I Gala.
# cann.block_status:
#   anchor_or_variant:
#     ANCHOR   # core narrative bridge from mission identity to gala performance
#   requires_followup:
#     - a1_s05_hallway → a1_s06_gala
# cann.true_path_integration:
#   - "Let yourself remember" increments early True Path resonance trigger by +1.
#   - True Path tracks accumulation of *unrepressed empathy moments* across both branches.
#   - This scene's memory acceptance counts toward that invisible meter (resonance > 3 by Act 2 = unlock).