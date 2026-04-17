# =======================================================
# ACT 3 - Interlude: Noelle — "The Unmeasurable"  (EMP)
# File: a3_int_02_noelle_unmeasurable_emp.rpy
# Type: LI THOUGHT INTERLUDE (Noelle)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_02_noelle_unmeasurable_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_02_noelle_unmeasurable_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: The log projection at a shallow angle. Noelle's hand enters frame with
    #         the stylus. The biometric sensor on her wrist breathes a slow green.
    #         One beat on her face when she writes the final line.
    # LIGHTING: Lab under-glow from the workbench. The biometric sensor pulses in her
    #           peripheral vision — we see it pulse even if she has stopped noticing.
    # SFX: Lab hum. The passive tick of the sensor's sync-beep, slower than her pulse.
    #      The stylus-tap. No music.
    # FACE: Noelle — absolutely still. The stillness is not composure. It is the
    #       stillness of someone watching a number that should not exist.

    # scene bg phoenix_lab_night with fade
    # show noelle neutral at center
    # play ambient "audio/amb/lab_low_hum.ogg" fadein 1.0

    nthought "LOG: self_experimental_01.log"
    nthought "SUBJECT: self"
    nthought "PROTOCOL: guided respiratory meditation. Instructor: L. Althea (cleric, Phoenix base)."
    nthought "DURATION: 00:04:12"

    nthought "OBSERVED, by timestamp:"
    nthought "  00:00:00 — baseline. Respiration 16/min. HRV nominal. Neural coherence nominal."
    nthought "  00:00:47 — respiration rate converges with subject L from 16/min to 12/min. Convergence was not instructed. It happened."
    nthought "  00:01:33 — HRV increases beyond nominal range. Sensor flagged the reading for review. I dismissed the flag."
    nthought "  00:02:18 — neural coherence (EEG proxy) drops to zero for 1.4 seconds."

    nthought "Critical observation — restate for the record:"
    nthought "  During the 1.4-second window, the sensor was operating within specification. The sensor was detecting nothing."
    nthought "  I, subject self, was experiencing something."

    nthought "The sensors were working."
    nthought "The sensors detected nothing."
    nthought "I felt something."

    nthought "Three statements. They cannot all be true in the framework I was trained in."
    nthought "They are all true."

    nthought "Therefore the framework is wrong."

    nthought "Recalculating backwards through the archive in my head:"
    nthought "  Every experiment I have ever run has assumed sensor adequacy. Every null result I have ever recorded has assumed that the absence of signal is the absence of phenomenon. Every paper I have written has operated on this assumption."
    nthought "  The assumption is wrong."

    nthought "Not wrong in every case. Wrong in a class of cases. A class I have no name for and no reliable boundary for."

    nthought "I need to write the new axiom before I lose my nerve."

    nthought "HYPOTHESIS: Unmeasurable ≠ Nonexistent."

    nthought "I am saving the file."
    nthought "I am not submitting it for peer review."

    nthought "For me, that is the same as a confession."

    # stop ambient fadeout 1.2

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_02_noelle_unmeasurable_emp
# cann.chapter: Act III, Phase I — Proving Ground
# cann.placement: After a3_s08_the_unmeasurable_emp. Lyra has led Noelle through a
#                 breathing meditation. Later, the same night. Noelle alone at her
#                 lab workspace with the passive biometric sensor still logging her
#                 vitals from the experiment.
# cann.what_happened:
#   - Noelle opens an experimental log in standard Echelon format. Subject: self.
#     Protocol: guided respiratory meditation. Instructor: L. Althea.
#   - She documents the observations by timestamp. Respiration converged with Lyra's
#     from 16/min to 12/min over 47 seconds — convergence not instructed, it happened.
#     HRV increased beyond nominal. Neural coherence dropped to zero for 1.4 seconds.
#   - The critical observation is the 1.4-second window. During the window, the
#     sensors were operating within spec and detecting nothing. She was experiencing
#     something.
#   - She runs the three-statement test: the sensors were working, the sensors
#     detected nothing, I felt something. All three cannot be true in her framework.
#     All three are true. Therefore the framework is wrong.
#   - She runs a backwards recalculation: every experiment she has ever done has
#     assumed sensor adequacy. Every null result. Every paper. The assumption is
#     wrong — not in every case, but in a class of cases she cannot yet define.
#   - She writes the new axiom: HYPOTHESIS: Unmeasurable ≠ Nonexistent.
#   - She saves the file. She does not submit it for peer review. For Noelle, the
#     absence of peer review is itself the confession.
# cann.voice_profile:
#   - Experimental log format. Timestamped observations. The structure holds longer
#     than it did in the Act II interlude because she has had more time to practice
#     with it. When the structure breaks, it breaks cleaner and more deliberately.
#   - Restatement "for the record" as the rhetorical device — she is performing
#     rigor at the exact moment her rigor is being turned on itself.
#   - No emotional language. The scene's weight is the backwards-recalculation.
# cann.reveal:
#   - Noelle is about to commit a category error her entire training was designed to
#     prevent. She is going to start trusting something she cannot measure. She knows
#     this and she proceeds.
#   - The refusal to submit the file for peer review is the load-bearing action. For
#     Noelle, peer review is the mechanism by which a claim becomes real. Keeping this
#     file private makes the claim hers in a way nothing else in her career has been.
# cann.callbacks:
#   - a2_int_02_noelle_variable_name: the unsaved file that stayed open. This is the
#     second file that will stay unclosed, and the hypothesis is written into the
#     same moral framework that scene refused to close.
#   - a3_s08_the_unmeasurable_emp: the breathing protocol with Lyra. All sensor
#     readings are drawn from that scene's established apparatus.
#   - Future: a3_int_noelle_aeron — the hypothesis established here is the permission
#     slip for that interlude's central choice.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. EMP-route only.
# cann.requires_followup:
#   - The phrase "Unmeasurable ≠ Nonexistent" is now canonical Noelle vocabulary.
#     Later scenes may call back to it but should not re-derive it.
