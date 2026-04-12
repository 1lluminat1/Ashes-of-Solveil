# =======================================================
# ACT 2 - Interlude: Tessa — "Torin's Name"
# File: a2_int_tessa_torins_name.rpy
# Type: LI THOUGHT INTERLUDE (Tessa)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_int_tessa_torins_name"
$ scene_mark(_current_scene_id, "entered")

label a2_int_tessa_torins_name:

    # Codex — first scene where the rule of three is actually NAMED
    # as a rule. Unlock the motif entry.
    $ codex_mention("rule_of_three", source="a2_int_tessa_torins_name")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Waist-level. Locked on the hands and the water. The face stays out of
    #         frame until the third repetition of the name. One quiet push in. Then out.
    # LIGHTING: Single bulb over the sink. Cold white. The mirror behind her is dark —
    #           she is not looking at it, so we do not look at it either.
    # SFX: Running water. Only running water. No music. The medbay door behind her is
    #      closed. The world is the sound of the tap and the sound of her breath.
    # FACE: Tessa — eyes on her own hands. Mouth working around a word that will not
    #       come out. Jaw set in the way that means she is counting in her head.

    # scene bg phoenix_washroom_night with fade
    # show tessa neutral at center
    # play ambient "audio/amb/washroom_tap.ogg" fadein 1.0

    tthought "The water is clean."
    tthought "My hands are clean."
    tthought "I can't tell."

    tthought "Eleven minutes by the clock above the door. I counted the first minute. The other ten counted themselves."

    tthought "Start the list. That's the thing to do. Start the list and the list will hold."

    tthought "Mira Donal. Kesh Arden. The boy from the lower spans — Toma, Toma Rellik. The woman with the cough. The woman with the burn. The man whose name I learned after I saved him and then forgot and then learned again."
    tthought "All of them. Both sides of the board. The living where I can keep them. The dead where I can find them."

    tthought "I am at the end of the list now."
    tthought "I know what comes next."

    tthought "Torin Vell."

    tthought "Say it. Three times. That was her rule."

    tthought "Torin Vell."
    tthought "Torin Vell."
    tthought "..."

    tthought "My throat won't."

    tthought "Torin Vell. Torin Vell. Torin Vell."

    tthought "The third time is the one that counts. She told me that when I was seven, the winter my father didn't come back. She said: say it three times, sweet thing, and you are still here."
    tthought "Not the dead one. Me. The rule was for me."

    tthought "That is what the board has been. That is what the counting has been."

    tthought "It isn't optimism. It was never optimism."
    tthought "It is the only rule I have for staying alive in a room full of people I couldn't save."

    tthought "The water is cold now. My hands haven't been unclean for ten minutes."

    tthought "There are other living names in the room behind me. I have to go keep them."

    # stop ambient fadeout 1.2

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a2_int_tessa_torins_name
# cann.chapter: Act II, Chapter IV — The Cost
# cann.placement: Immediately after a2_s23_mercy_and_counting. Tessa has just delivered
#                 the mercy death to Torin Vell. She steps into the washroom adjacent
#                 to the medbay. Closes the door. Turns on the tap. Does not leave for
#                 eleven minutes.
# cann.what_happened:
#   - Tessa washes her hands past the point of cleanliness. The gesture is not hygiene.
#     It is the only motion available to her.
#   - She runs the name inventory she has been running since Act I — every patient,
#     every name, both sides of the board — and reaches the end of it for the first
#     time in a long time.
#   - The end of the list is Torin Vell. She adds him.
#   - She tries to say his name aloud. Her voice fails. She says it three times in her
#     head. The third repetition is the one that takes.
#   - She recognizes, without saying it aloud, that her mother's rule was never "say it
#     three times and the dead are real." Her mother's rule was "say it three times and
#     you are still here." The counting is for the counter.
#   - She turns off the water. She goes back to the medbay. There are other living
#     names to keep.
# cann.voice_profile:
#   - Gentle present-tense. Physical anchoring. Breath, pulse, water temperature, the
#     clock above the door. Tessa's voice inside her own head is the same voice she
#     uses with dying patients — soft, itemized, quietly stubborn.
#   - Names are load-bearing. Three repetitions. The rule from her mother.
#   - No declarations. The grief is in the list and the list is in the hands.
# cann.reveal:
#   - The "Count the Living" philosophy is not optimism. It is grief discipline — a
#     survival ritual Tessa inherited from her mother, the rule a seven-year-old was
#     given the winter her father did not come back.
#   - Tessa has been using it on herself the entire time. Every living name she counts
#     is a small argument for her own continued existence.
#   - She knows the math does not work. She is doing it anyway. That is what the
#     counting is.
# cann.callbacks:
#   - a2_s23_mercy_and_counting: the mercy death that precedes this.
#   - Her mother (referenced earliest in a1_s07_balcony): the rule-giver. The rule has
#     not been stated aloud in the script before this scene. This is where it lands.
#   - The board (established in a2_s14_the_intel_den and a2_s16_finding_home): the
#     structural object the philosophy is named after.
#   - Future: a3_int_tessa_hands_remember_emp — the same hands, now steady for a
#     different reason.
#   - Future: a3_int_tessa_the_board_emp — the same board, now forced to hold Liora
#     Rylan on both sides.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. Scene runs as a quiet transition into the
#     next medbay beat.
# cann.requires_followup:
#   - Tessa's counting philosophy is now visible to the player as ritual-as-survival.
#     Subsequent Tessa beats should read against this rather than re-declaring it.
