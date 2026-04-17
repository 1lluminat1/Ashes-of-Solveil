# =======================================================
# ACT 3 - Interlude: Nyra — "Before the Mirror"
# File: a3_int_02_nyra_before_the_mirror_ob.rpy
# Type: LI THOUGHT INTERLUDE (Nyra, OB)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_02_nyra_before_the_mirror_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_int_02_nyra_before_the_mirror_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Locked medium. The cloth, the blade, the steady passes. Her hands only.
    #         One final cut to the window at the end — her back, the transport lane
    #         beyond, the pre-op stillness.
    # LIGHTING: Clean, cold morning light. No lamp. No shadows worth tracking. Every-
    #           thing in the frame is exactly the brightness it claims to be. The
    #           light is as certain as she is.
    # SFX: Cloth on steel. Even passes. Unbroken rhythm. The faint signal of a distant
    #      transport lane. No music.
    # FACE: Nyra — composed to the millimeter. She looks like a woman who has already
    #       won and is waiting for the world to confirm it.

    # scene bg nyra_chambers_morning with fade
    # show nyra composed at center
    # play ambient "audio/amb/morning_clean.ogg" fadein 1.5

    nythought "Cloth. Blade. Cloth. Blade."

    nythought "The motion is older than the reason for the motion. The blade does not need polishing. I need the polishing."

    nythought "Liora Rylan."

    nythought "A woman who abandoned her family and called the abandonment a principle. A woman who ran and named the running virtue. The disciplined are always accused of being the liars by the liars. The committed are always called the cowards by the cowards."

    nythought "I have seen the shape of this scene before. I know how it ends."

    nythought "She will look at him and she will see herself. She will see the shape of the mother she failed to be, standing across the room as a grown man, and she will flinch."

    nythought "He will see the flinch."

    nythought "The flinch is the whole scene."

    nythought "I am not worried for him. I am preparing the aftermath. What a son needs after a mother has confirmed herself a coward in front of him is structure. I will be the structure."

    nythought "Through precision, peace. Through peace, obedience. Through obedience, order eternal."

    # The cloth passes over the blade one more time. She sheathes it without looking.

    nythought "There is nothing she can say that he has not already heard from inside his own skull and recognized as the enemy. That is the gift of being trained into a shape that holds. The shape holds."

    nythought "He will be confirmed. The doctrine will be validated. The scene will end on the word."

    # Her hand drifts, unconsciously, to the silvered scar at the base of her palm.
    # The scar is not glowing. She notices the absence. She does not understand it.
    # She files it as a sensor anomaly and moves to the window.

    nythought "A transport on the horizon. Right on schedule. Even the sky is ceremonial today."

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_02_nyra_before_the_mirror_ob
# cann.chapter: Act III, Phase III — Mirror & Rejection
# cann.placement: Before a3_s24_liora_ob (the Liora confrontation — OB Act 3 finale).
#                 Nyra's chambers. Pre-op calm. Polishing Veilbreaker. Alone. This
#                 is the last moment of her complete, unshaken certainty.
# cann.what_happened:
#   - Nyra is in the pre-operation ritual she always uses before a ceremonial moment:
#     polishing Veilbreaker. The blade is clean. The motion is the point.
#   - She files Liora in her head: abandonment dressed as virtue, running dressed as
#     principle. The classification is complete and complete in tone — she is not
#     arguing with an opponent, she is categorizing a known quantity.
#   - She predicts the scene in full: Liora will see herself in Aeron and flinch. He
#     will see the flinch. The flinch will confirm the doctrine. The scene will end
#     on the word. She is so certain of the shape that she is already planning
#     the aftermath.
#   - The liturgical refrain returns in the middle of the thought-sequence — not
#     because she needs it, but because it is how she breathes.
#   - Her hand drifts to the silvered scar at the base of her palm. The scar is not
#     glowing. She has never seen it not glow before a ceremonial moment. She files
#     the absence as a sensor error.
# cann.voice_profile:
#   - Absolute certainty. The liturgical rhythm is still operating but it is now the
#     carrier wave, not the foreground. The foreground is strategic pre-judgment.
#   - She catalogues Liora in categorical phrases. The catalogue is neat. The
#     neatness is the tell — she has already decided the outcome of a meeting that
#     has not yet occurred.
#   - The "sensor anomaly" line is the deepest crack in the certainty that the scene
#     permits. She cannot feel the crack. The reader feels it for her.
# cann.reveal:
#   - Nyra is going to be wrong. Completely. Her certainty is so total that the
#     wrongness will not be an argument she loses — it will be a revelation she did
#     not know the universe was capable of issuing. That is what makes the Liora
#     scene work as a finale: not villain-defeat but devotee-dislocation.
#   - The scar not glowing is the reader's advance warning. Something is already
#     withdrawing from her. She cannot perceive it because her framework does not
#     admit the possibility of withdrawal. She files the absence as malfunction.
#   - She is not evil in this scene. She is a woman who has never been betrayed by
#     her own conviction preparing to be betrayed by her own conviction, one scene
#     before it happens, unable to see it.
# cann.callbacks:
#   - a3_int_01_nyra_the_oath_ob: the ritual and the scar. The scar was glowing at the
#     end of that scene. The contrast is the content of this scene.
#   - a3_s12_the_oath_ob: the fractured-crest ritual, the silvered scars. Established.
#   - a3_s23_bookend_before_mirror_ob: the bookend this interlude lives inside.
#   - a3_s24_liora_ob: the confrontation this scene is the false prophecy of.
#   - "The shape holds" — will recur in Phase III as the line that does not hold.
#   - Veilbreaker: polished, sheathed, will be drawn in the Liora scene.
# cann.block_status:
#   - INTERLUDE. OB path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - The scar glow state as an ongoing sensor for Nyra's theological alignment.
#     Phase III should track it. Its absence here is setup.
#   - The "sensor anomaly" filing as Nyra's coping signature going forward: when
#     reality contradicts her doctrine, her first move is to classify reality as
#     malfunctioning. This becomes load-bearing for her Act 4 arc.
#   - The pre-judged scene: Aeron's behavior in a3_s24_liora_ob will land differently
#     against the prediction laid out here. Play the contrast.
