# =======================================================
# ACT 2 - Interlude: Noelle — "Variable Name"
# File: a2_int_noelle_variable_name.rpy
# Type: LI THOUGHT INTERLUDE (Noelle)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_int_noelle_variable_name"
$ scene_mark(_current_scene_id, "entered")

label a2_int_noelle_variable_name:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Over the shoulder. The projected data crystal fills the frame — a
    #         standard Echelon research log, its declaration line blinking cursor.
    #         The stylus enters frame, types, deletes. Enters, types, deletes.
    # LIGHTING: Cool white from the crystal. Nothing else. Her face is half in the
    #           projection, half in the dark.
    # SFX: Lab hum. The faint stylus-tap that marks each character committed to the
    #      log. No music.
    # FACE: Noelle — eyes narrowed in the way that means she is troubleshooting. The
    #       troubleshooting is not working. The not-working is the anomaly she is
    #       trying to quantify.

    # scene bg echelon_lab_night with fade
    # show noelle neutral at center
    # play ambient "audio/amb/echelon_lab_hum.ogg" fadein 1.0

    nthought "FILE: unmodeled_variable_TK.log"
    nthought "STATUS: new"
    nthought "DECLARATION: pending"

    nthought "care: str = ?"
    nthought "  — rejected. String requires bounded content. Observed phenomenon has no content, only effect."

    nthought "care: bool = ?"
    nthought "  — rejected. Boolean requires binary state. Observed phenomenon is not binary. Subject T. exhibits it continuously, at varying intensities."

    nthought "care: float = ?"
    nthought "  — rejected. Float requires a scale. No scale has been defined. No scale can be defined without a unit."

    nthought "care: int = ?"
    nthought "care: list = ?"
    nthought "care: dict = ?"
    nthought "care: set = ?"

    nthought "..."

    nthought "Attempt count: seventeen. I have stopped counting."

    nthought "If a variable cannot be typed, the variable does not exist."
    nthought "If the variable does not exist, the observed effect must be attributable to a different variable."
    nthought "Candidate variables: ritual behavior. Emotional affect. Social pressure. Coincidence."
    nthought "None of these match the data."

    nthought "The data is the patient. The clamp. Subject T.'s hands."
    nthought "The clamp was engaged. I watched her engage it. She knew what it was for. She was afraid of it. She used it anyway."
    nthought "Fear plus action is not a string or a boolean or a float."
    nthought "It is a thing I do not have a name for."

    nthought "My existing category for things that cannot be quantified is ERROR."
    nthought "This is not an error."

    nthought "I require a new category."
    nthought "I do not have a name for the new category either."

    nthought "File: still open."
    nthought "Declaration: still pending."

    nthought "I am going to leave it open."

    # stop ambient fadeout 1.2

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a2_int_noelle_variable_name
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.placement: After a2_s18_the_patient. Noelle has witnessed Tessa engage a
#                 surgical clamp in the presence of fear. Later the same evening
#                 in Noelle's lab/workspace. Alone. Data crystal projecting.
# cann.what_happened:
#   - Noelle opens a new research log titled unmodeled_variable_TK.log. The TK is
#     hers — Tessa's first initial used as a placeholder because the variable the
#     file is trying to describe is something Tessa did, and the file refuses to
#     hold any type declaration Noelle attempts.
#   - Seventeen failed attempts at typing the variable. String, boolean, float, int,
#     list, dict, set. She stops counting.
#   - Her thoughts drop out of code format into prose: if a variable cannot be typed,
#     the variable does not exist. If the variable does not exist, the observed effect
#     must be attributable to a different variable. She runs candidates. Ritual
#     behavior, emotional affect, social pressure, coincidence. None match the data.
#   - She recognizes that her existing category for things she cannot quantify is
#     ERROR. This is not an error. She requires a new category.
#   - She does not have a name for the new category. She leaves the file open.
# cann.voice_profile:
#   - Formatted. Code-shaped thought-lines. Declaration syntax. Comment markers. When
#     the formal structure fails, the failure is meaningful — prose only intrudes
#     after code has been tried and rejected.
#   - Precision in the service of insufficiency. Her training is showing her where
#     her training does not reach.
#   - No emotional declaration. The affect is in the formatting.
# cann.reveal:
#   - The failure to quantify care creates a new cognitive category. Noelle's training
#     had exactly one drawer for "things that cannot be measured" and the drawer was
#     labeled ERROR. The drawer is no longer adequate.
#   - She is not naming the new category tonight. She is accepting that the new
#     category must exist. This is the first time in her adult life she has done so.
#   - The unsaved, undeclared file is itself her honesty: she will not close an
#     anomaly she cannot yet type.
# cann.callbacks:
#   - a2_s18_the_patient: the clamp, the fear, Tessa's hands. All drawn directly from
#     the scene this follows.
#   - Future: a3_int_noelle_unmeasurable_emp — the file stays open and the hypothesis
#     "Unmeasurable ≠ Nonexistent" is written into the same framework this scene
#     refuses to close.
#   - Future: a3_int_noelle_aeron — the file is renamed from unmodeled_variable_TK to
#     Aeron. The file does not get closed. It gets claimed.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. Route-agnostic (fires on both EMP and OB).
# cann.requires_followup:
#   - Any later Noelle scene that reaches for a "new category" language should be able
#     to assume this scene established the absence of the name.
#   - The unsaved file is the motif. It does not get saved in this act.
