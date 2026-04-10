# =======================================================
# ACT 3 - Interlude: Lyra — "Untrained Prayer"
# File: a3_int_lyra_field_sync_emp.rpy
# Type: LI THOUGHT INTERLUDE (Lyra, EMP)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_lyra_field_sync_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_lyra_field_sync_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 85mm, held on her hand closed around her own wrist. Not the Band —
    #         the wrist. The Band is incidental. The hand is the subject.
    #         One slow pull to her face at the end. Nothing else moves.
    # LIGHTING: Late. Blue hour bleeding through one narrow window. Her lamp is off.
    #           The Band catches the window light on the seam. Everything else is
    #           the color of a held breath.
    # SFX: Her breath. The very faint tone of the Band cooling. Outside, someone's
    #      footsteps pass the corridor once and do not return. No music.
    # FACE: Lyra — wonder and terror holding the same expression. Open-mouthed, not
    #       speaking. Her eyes are the softest they have ever been on camera.

    # scene bg lyra_quarters_late2 with fade
    # show lyra quiet_awe at center
    # play ambient "audio/amb/base_low_deep.ogg" fadein 2.0

    lthought "The Band is still warm."

    lthought "Post-op warmth fades within three minutes. That's the documented range. I've checked it against my own wrist eleven times across four years. Three minutes, plus or minus twenty seconds."

    lthought "It has been closer to an hour."

    lthought "My breath matched his in the field. No count, no cue, no instruction. The Academy teaches sync through rhythm training — six weeks of paired breathing drills in my third year. This did not feel like a drill."

    lthought "It felt like a tide coming in to a shore that had been waiting."

    lthought "Sacramental union. Harmonic resonance. Sanctified proximity."
    lthought "I am saying the words out of habit. They are the right shape and the wrong size."

    lthought "The Order taught me that its language was complete. That any legitimate experience of the spirit had a name in the liturgy, and anything unnamed was suspect by virtue of being unnamed."

    lthought "This has no name I was given."

    lthought "Which means one of two things is true. Either what happened in the field today was not a legitimate experience of the spirit — or the Order's language was never complete."

    lthought "I was told the first was impossible. I was told the second was heresy."

    lthought "My hand is on my own wrist. I have never done this. I grew up being told the body was scaffolding for the work. I am learning tonight that scaffolding can warm."

    # A word rises — unasked, in the Old Tongue. She does not recognize the liturgy.

    lthought "{i}Anayet.{/i}"

    lthought "I don't know where that came from."
    lthought "I don't know what it means."
    lthought "I only know that my mouth knew it before I did."

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_lyra_field_sync_emp
# cann.chapter: Act III, Phase II — Deepening
# cann.placement: After a3_s10_field_sync_emp (the bloodline resonance scene).
#                 Night. Private. Lyra in quarters. The post-op warmth of the
#                 Aether Band has not faded.
# cann.what_happened:
#   - Lyra notices that her Band is still warm an hour after sync — far outside
#     the three-minute documented window.
#   - She tries to name what happened in the field using Order doctrine: sacramental
#     union, harmonic resonance, sanctified proximity. None of the terms fit.
#   - She recalls being taught that the Order's language was complete — that any
#     legitimate experience had a liturgical name. The logical consequence of her
#     experience is that either she is illegitimate or the Order is incomplete.
#   - She is holding her own wrist — not the Band, the wrist. The body as something
#     she is aware of rather than something she uses.
#   - A word rises in the Old Tongue — {i}Anayet{/i} — from a liturgy she was never
#     taught. Her mouth knows the word before she does.
# cann.voice_profile:
#   - Quieter than Lyra has been on screen. The fragmentation of the previous
#     interlude has steadied into something more like awe. Not resolution — stillness.
#   - The Academy instinct to catalogue is present but is now serving a different
#     purpose: measuring the distance between what she was taught and what is
#     happening to her body.
#   - The Old Tongue word is the first time Lyra produces spiritual language that
#     is not Academy-authorized. It is load-bearing.
# cann.reveal:
#   - What Lyra feels for Aeron may not have a name in the Order's liturgy. The
#     Order is smaller than Lyra was told it was.
#   - Bloodline/inherited knowledge: the word {i}Anayet{/i} comes from nowhere she
#     can identify. It suggests a layer of her inheritance the Academy sealed.
#     Mirror for Aeron's suppressed memories — both had something taken they are
#     only now discovering was ever theirs.
#   - Her mother is in the subtext again. Lyra does not name her here. The word in
#     her mouth may be her mother's.
# cann.callbacks:
#   - a2_int_lyra_check: the Band ritual, the prayer she couldn't finish. The same
#     Band. A different warmth.
#   - a3_int_lyra_file_was_wrong_emp: the weapon-skill realization. This scene is
#     the counter-image: the part of her that was not trained is the part still
#     alive.
#   - a3_s10_field_sync_emp: the resonance scene itself.
#   - Glass Academy as incomplete institution: thematic through-line for Lyra
#     Phase II and III.
#   - Aeron's suppressed memories (Liora's letter): parallel arcs of sealed
#     inheritance.
# cann.block_status:
#   - INTERLUDE. EMP path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - {i}Anayet{/i} — the word. Its translation, its source liturgy, who taught it
#     to Lyra's mother. Quest thread.
#   - Lyra's mother as Old Tongue speaker — Act 4 thread.
#   - The Order as incomplete: doctrinal crisis arc.
#   - The Band temperature anomaly: does it fade? Does it recur on every sync?
