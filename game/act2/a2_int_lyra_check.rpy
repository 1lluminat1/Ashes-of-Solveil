# =======================================================
# ACT 2 - Interlude: Lyra — "Check"
# File: a2_int_lyra_check.rpy
# Type: LI THOUGHT INTERLUDE (Lyra)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_int_lyra_check"
$ scene_mark(_current_scene_id, "entered")

label a2_int_lyra_check:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 85mm macro. Held close on the hands and the Band. The face only once —
    #         when she loses count. Shallow focus. The room is a blur of amber.
    # LIGHTING: One lamp. Warm. The Aether Band catches the light on the seam.
    #           Everything outside a two-foot radius is dark.
    # SFX: Base hum beneath everything — low, structural, distant. The faint tick of
    #      the Band's internal pulse against her fingertip. Her breath, slow, counted.
    #      No music.
    # FACE: Lyra — lips parted, eyes down, the small muscles at the jaw working.
    #       One moment where her mouth shapes a word it doesn't say.

    # scene bg lyra_quarters_night with fade
    # show lyra neutral at center
    # play ambient "audio/amb/phoenix_base_hum.ogg" fadein 1.5

    lthought "Six."
    lthought "Seven."
    lthought "..."

    lthought "Lost it on eight."

    lthought "He said my name in the corridor today. That was all. My name."
    lthought "And my thumb found the seam of the Band the way a prayer finds a rosary."

    lthought "Devotion. Union. Mission-attachment."
    lthought "The catechism has a drawer for every feeling a cleric can have. I was taught to file."

    lthought "None of the drawers fit this."

    lthought "Breath count: shallow. Four beats short of calm."
    lthought "Wrist temperature: warmer than the Band."
    lthought "Jaw: locked, but I knew that without checking."

    lthought "Start again. Six. Seven. Eight. Nine."
    lthought "The pulses are steady. I'm the one who isn't."

    lthought "I checked the Band three times before dinner. I checked it twice after. I am checking it now and I could not tell you why except that stopping is the frightening part."

    lthought "Holy Order, receive the breath of your servant—"
    lthought "..."

    lthought "I don't know how the rest of that sentence ends tonight."

    lthought "Six. Seven. Eight."

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a2_int_lyra_check
# cann.chapter: Act II, Chapter IV — The Cost
# cann.placement: After a2_s22_massive_recruitment (Phoenix growth milestone).
#                 Private interlude. Night. Lyra alone in assigned quarters.
# cann.what_happened:
#   - Lyra cannot sleep. She runs the Aether Band diagnostic ritual — the Academy
#     practice for settling the body when the mind will not settle.
#   - She counts pulses, loses count on eight, remembers Aeron saying her name earlier
#     in the day. She tries to file the feeling under Order doctrinal categories
#     (devotion, union, mission-attachment). None fit.
#   - She runs sensation checks — breath, wrist, jaw — the way she was trained.
#   - She begins a prayer and cannot finish it. She does not finish it.
#   - The ritual used to calm her. Tonight it is the only thing holding the room still.
# cann.voice_profile:
#   - Prayer cadence. Itemized. Short sentences. The rhythm of someone who organizes
#     herself by inventory. Physical checks interleave with internal sentences because
#     that is how Glass Academy clerics were taught to pray — body and mind tracked
#     simultaneously, like dual diagnostics.
#   - No sarcasm. No deflection. Lyra alone is Lyra at her most precise and her most
#     frightened — the two states now indistinguishable.
# cann.reveal:
#   - The Band-checking has become compulsion. She has not told anyone. She is not sure
#     she could stop if she tried. The ritual has migrated from practice to need.
#   - Her Order frameworks do not name what she feels for Aeron. The absence of the
#     name is worse than a forbidden name would be. A forbidden thing can be confessed.
#     An unnamed thing has no liturgy.
# cann.callbacks:
#   - Glass Academy sensation-check training: inherited discipline turning against her.
#   - Future: a3_int_lyra_file_was_wrong_emp — the pattern of compulsive checking
#     worsens after the Hana encounter.
#   - Future: a3_int_lyra_field_sync_emp — the same Band carries a warmth her training
#     has no word for.
#   - Liora's letter (a3_s18a): "brave enough to be soft when softness is the most
#     dangerous thing." Lyra is not brave yet. She is still trying to file softness.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. Scene runs as a quiet transition.
# cann.requires_followup:
#   - The Band-checking compulsion escalates across Act 3 interludes.
#   - Unfinished prayer recurs. The sentence she cannot end becomes a motif.
#   - Lyra has not told Aeron about the ritual. When/if she does is a later scene.
