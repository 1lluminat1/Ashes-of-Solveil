# =======================================================
# ACT 3 - Interlude: Tessa — "Hands Remember"  (EMP)
# File: a3_int_tessa_hands_remember_emp.rpy
# Type: LI THOUGHT INTERLUDE (Tessa)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_tessa_hands_remember_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_tessa_hands_remember_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Close on the forceps and the cloth. The hands move in slow, practiced
    #         circles. The face is seen once, in profile — the corner of a mouth that
    #         is almost but not quite smiling.
    # LIGHTING: One overhead panel at half power. The tray of instruments catches it.
    #           Everything outside the table is soft and dim.
    # SFX: The hum of the medbay at off-hours. The small metallic sound of instruments
    #      being set down and picked up. Her own breath, even. No music.
    # FACE: Tessa — mouth soft. The small muscles around her eyes relaxed in a way
    #       they have not been in months.

    # scene bg phoenix_medbay_late with fade
    # show tessa neutral at center
    # play ambient "audio/amb/medbay_low_hum.ogg" fadein 1.2

    tthought "These were clean an hour ago. I cleaned them. I watched myself clean them."
    tthought "I am cleaning them again."

    tthought "This is not that kind of washing."

    tthought "The gash on his forearm — three inches, ragged edge, the one I stitched in the corridor after the sweep. My thumb knew the shape of the edge before my eyes found it tonight."
    tthought "The scar under his sleeve. The Brand. I did not look at it. My fingers looked at it. They found the raised line and went around it the way water goes around a stone."
    tthought "The line of his jaw when I tilted his head. The small give at the hinge. He let me move him. He has never let anyone move him."
    tthought "The pulse in his wrist — under my first two fingers, where I take a pulse on a stranger. It slowed under my hand."
    tthought "Mine slowed first. I felt the handoff."

    tthought "I was not analyzing him. I was taking inventory. I do that with the dying. I did not know I did it with the living."

    tthought "I have been doing it for months."

    tthought "Every time he came in bleeding I was cataloguing more than the wound. I did not let myself know I was cataloguing more than the wound."
    tthought "I was holding it. Not pushing it down. Holding it — the way I hold a hand that is cold and trying to stop being cold."

    tthought "The difference matters."
    tthought "Holding keeps a thing alive. Pushing down does not."

    tthought "Tonight was the first night I was allowed to set it down."
    tthought "I did not realize how heavy it was until my arms were empty."

    tthought "My hands are steady."

    tthought "I will file that under observations in the morning. I will not notice that the observation is the whole thing."

    # stop ambient fadeout 1.2

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_tessa_hands_remember_emp
# cann.chapter: Act III, Phase II — Deepening
# cann.placement: After a3_s13_scar_and_steady_emp. Tessa's first erotic scene with
#                 Aeron has concluded. Later the same night. She is alone in the
#                 medbay, cleaning forceps that were already clean.
# cann.what_happened:
#   - Tessa cleans instruments as a way of staying in her body. The gesture is private,
#     meditative, and involuntary.
#   - Her thoughts do not analyze the sex. They catalogue touch the way she catalogues
#     patients — by specific physical contact. The gash. The Brand scar. The jaw. The
#     pulse in his wrist.
#   - The pulse-handoff moment is the one she notices: his pulse slowed under her
#     fingers because hers slowed first.
#   - She realizes she has been holding her desire for him — not suppressing it,
#     holding it — for months. The distinction is load-bearing. Suppression pushes a
#     thing down and kills it. Holding keeps it alive at cost.
#   - Tonight was the first night she was allowed to put the weight down. She did not
#     know how heavy it was until her arms were empty.
#   - She notices her hands are steady. She files the observation. She does not yet
#     understand that the steadiness is the whole point.
# cann.voice_profile:
#   - Same gentle present-tense. Same physical inventory. The difference from the
#     a2 "Torin's Name" interlude is the texture of the list — warm instead of raw,
#     lived instead of lost. The form is unchanged. The content is the first good
#     thing the form has been asked to hold in a long time.
#   - No semantic looping. No declarations of love. One image per truth.
# cann.reveal:
#   - Tessa's care for Aeron is not new. It is sustained, months-old, and held with the
#     same discipline she uses for dying patients. The intimacy scene did not create
#     the feeling. It let her set the weight down.
#   - The grief discipline from "Torin's Name" is the same faculty she has been using
#     to love him. She does not have two systems. She only has one.
# cann.callbacks:
#   - a2_int_tessa_torins_name: the hands shaking over the sink. The hands are steady
#     now. The scene is structured as a quiet answer to that one.
#   - a3_s13_scar_and_steady_emp: the scene this follows directly. The Brand scar, the
#     gash, the pulse in the wrist — all drawn from that scene's physical vocabulary.
#   - Future: a3_int_tessa_the_board_emp — the observation she does not yet understand
#     returns under pressure when the board can no longer hold what it used to hold.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. EMP-route only.
# cann.requires_followup:
#   - The steadiness noted here is the baseline the Liora-execution interlude breaks
#     against. Do not waste it in intervening scenes.
