# =======================================================
# ACT 3 - Interlude: Noelle — "Aeron"
# File: a3_int_noelle_aeron.rpy
# Type: LI THOUGHT INTERLUDE (Noelle)
# NOTE: Gates on Name Mechanic activation. Works for both EMP and OB routes.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_noelle_aeron"
$ scene_mark(_current_scene_id, "entered")

label a3_int_noelle_aeron:

    # ========= GATE =========
    if not flag("tp_name_typed"):
        return  # Only fires if player successfully activated the Name Mechanic.

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: The data crystal first, from over her shoulder. The file header visible.
    #         The stylus hovering above the DESIGNATION line. Then a slow pull back to
    #         include her whole profile against the flickering projection. She does
    #         not look at the flicker. We do.
    # LIGHTING: The crystal's projection pulses — a low, irregular flicker on the
    #           DESIGNATION field. It is not a malfunction. She knows it is not a
    #           malfunction. She does not correct it.
    # SFX: Lab hum. The stylus hovering without committing. Her breath once, audible,
    #      when she types the new name. No music.
    # FACE: Noelle — the formal neutrality she wears at her workbench, cracking at one
    #       point. The point is not when she types. The point is when she walks away.

    # scene bg lab_night_late with fade
    # show noelle neutral at center
    # play ambient "audio/amb/lab_crystal_pulse.ogg" fadein 1.0

    nthought "FILE UPDATE: unmodeled_variable_TK.log"
    nthought "FIELD: DESIGNATION"

    nthought "PREVIOUS DESIGNATION: anomaly"
    nthought "PREVIOUS MODEL: Glass. Echelon-trained. High-efficiency operator. Profile consistent at 97%% confidence. Deviations flagged as noise."

    nthought "The 97%% was always the number I was proud of. It meant I was right almost all of the time. It also meant I was dismissing three percent of the data as noise."
    nthought "Three percent of a person."

    nthought "NEW DESIGNATION: Aeron."
    nthought "NEW MODEL: insufficient."

    nthought "..."

    nthought "I am looking at the word insufficient."
    nthought "My training says: refine the model until it fits. Run the variable through more passes. Add parameters. Do not accept insufficiency as a terminal state."

    nthought "My new category says: some things refuse to fit, and the refusal is itself data."
    nthought "I am choosing the new category."

    nthought "The crystal is flickering. The DESIGNATION field — not uniformly, not at the rate of a hardware fault. It is pulsing in a way the diagnostics will flag if I run them."
    nthought "I am not going to run them."

    nthought "The flicker is — "

    nthought "There is no variable in my schema for what the flicker is."
    nthought "It is pretty. That is not a clinical word. I am using it anyway."

    nthought "I have stopped trying to file the absence."

    nthought "Aeron."

    nthought "In my head, where my real variables live. The place I do not submit for peer review."

    nthought "Aeron."

    nthought "The file is open. I am walking away from it open."
    nthought "I have never walked away from an open file."

    nthought "I am walking away from this one."

    # stop ambient fadeout 1.5

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_noelle_aeron
# cann.chapter: Act III, Phase II — Deepening
# cann.placement: After a3_s11_empirical_tenderness_emp (EMP route) or
#                 a3_s16_data_and_doubt_ob (OB route). Gates on the Name Mechanic:
#                 fires only if flag("tp_name_typed") is True — i.e., the player
#                 successfully activated Noelle's name recognition beat.
# cann.what_happened:
#   - Noelle opens the unmodeled_variable_TK.log file — the one that has been open
#     since Act II. She updates the DESIGNATION field.
#   - Previous designation: anomaly. Previous model: Glass. Echelon-trained. 97%
#     profile confidence with flagged noise. She reckons with what the 97% cost her —
#     three percent of a person dismissed as statistical noise.
#   - New designation: Aeron. New model: insufficient.
#   - She stares at the word insufficient. Her training says refine the model until
#     it fits. Her new category — the one established in a3_int_02_noelle_unmeasurable —
#     says some things refuse to fit, and the refusal is itself data. She chooses the
#     new category.
#   - The data crystal flickers on the DESIGNATION field. Not a hardware fault. A
#     pulse. She does not run diagnostics. She does not re-calibrate. She watches.
#   - The flicker is pretty. Pretty is not a clinical word. She uses it anyway. She
#     stops trying to file the absence of a variable for beauty.
#   - She says the name in her head — in the place she does not submit for peer
#     review. Aeron. Twice.
#   - She walks away from the file. Open. For the first time in her career.
# cann.voice_profile:
#   - Formatted thought-lines. Declaration syntax. But the prose intrusions are more
#     frequent and more pliant than in either prior Noelle interlude. The form is
#     yielding on purpose.
#   - She names the clinical failure ("pretty is not a clinical word") and proceeds
#     past it without apology. This is new.
#   - One image per truth. The flicker is the only external object. Everything else
#     is choice.
# cann.reveal:
#   - For the first time in her adult life, Noelle chooses to observe something
#     without documenting it. The act of not taking a measurement is its own
#     measurement. She knows this. She makes the choice anyway.
#   - She walks away from an open file. For Noelle, this is equivalent to a vow.
#   - The Name Mechanic activation is retroactively load-bearing: saying the name
#     out loud in the triggering scene was the thing that unlocked her ability to
#     say it in her head here, in the place her real variables live.
# cann.callbacks:
#   - a2_int_02_noelle_variable_name: the file opened two acts ago. It is the same file.
#     It is still open.
#   - a3_int_02_noelle_unmeasurable_emp: the hypothesis (Unmeasurable ≠ Nonexistent) is
#     the permission this scene cashes in.
#   - a3_s11_empirical_tenderness_emp / a3_s16_data_and_doubt_ob: whichever scene
#     triggered the tp_name_typed flag is the scene this interlude answers.
#   - Name Mechanic canon: saying his name was the binding act. The name lives in her
#     real variable store now.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. Gated on tp_name_typed. Route-agnostic
#     between EMP and OB provided the Name Mechanic was activated.
# cann.requires_followup:
#   - The open file is now the Noelle-side motif equivalent of Tessa's board. Any
#     later Noelle scene that references research discipline should be readable
#     against the fact that this file is still open and she is still walking past it.
#   - Subsequent Noelle intimacy beats can assume the name is canonical in her
#     internal voice without re-earning it.
