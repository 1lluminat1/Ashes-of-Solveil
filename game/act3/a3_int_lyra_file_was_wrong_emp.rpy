# =======================================================
# ACT 3 - Interlude: Lyra — "The File Was Wrong"
# File: a3_int_lyra_file_was_wrong_emp.rpy
# Type: LI THOUGHT INTERLUDE (Lyra, EMP)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_lyra_file_was_wrong_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_lyra_file_was_wrong_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked on the journal and the pen. One cutaway to her hand
    #         hovering over the Band at the end. No full face. The face is not
    #         the subject tonight — the hand is.
    # LIGHTING: Desk lamp only. The page glows. Her fingers are half-lit. Everything
    #           beyond the desk is a held breath of dark.
    # SFX: The scratch of pen starting and stopping. The tap of the pen being set
    #      down. A slow exhale. No base hum tonight — the room is too quiet for it
    #      to register.
    # FACE: Lyra — eyes tracking the three words she wrote. Not reading. Measuring.

    # scene bg lyra_quarters_late with fade
    # show lyra tired at center
    # play ambient "audio/amb/base_quiet.ogg" fadein 1.5

    lthought "Today I saw—"
    lthought "..."

    lthought "Today I saw—"
    lthought "..."

    lthought "Six tries. The pen will not move past three words."

    lthought "Her name was Hana. Her daughter's name was on a form I filed in my third year. Seven-Delta-Eleven-Thirty-Eight. I can still see the routing stamp."
    lthought "I filed it without reading. That was the discipline. Pattern recognition on the structure, not the content. The content was not our work."

    lthought "I was sixteen."

    lthought "The Academy called my pattern recognition a gift. They said it was the reason I was placed in Analytics. The reason they trained me on the bands. The reason I saw Hana tonight before anyone else did — across a room, in a crowd, through the noise."

    lthought "The same gift."
    lthought "The same gift that found her today is the gift that erased her daughter seven years ago."

    lthought "They did not teach me a skill. They took what I was and sharpened it and handed it back to me with a Directorate seal on the handle."

    lthought "My discipline. My precision. The reason I could read a field op from a twenty-second glance."
    lthought "I cannot find the place where the weapon ends and I begin."

    lthought "I keep trying to separate them and the seams are not where I thought they were."

    lthought "My mother trained at the Academy too. If she was still alive I would ask her if she found the seam. I would ask her how old she was when she stopped looking."

    lthought "..."

    lthought "I cannot finish this entry. I cannot start it either."

    # The hand drifts to the Band. Unconsciously.

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_lyra_file_was_wrong_emp
# cann.chapter: Act III, Phase I — Proving Ground
# cann.placement: After a3_s05a_woman_from_sector_7_emp (the Hana encounter).
#                 Private interlude. Lyra alone in quarters. Journal on desk. Pen
#                 in hand. The aftermath is slow and it is hers.
# cann.what_happened:
#   - Lyra attempts the Academy journal practice — structured written reflection on
#     difficult days. She cannot get past three words. Six attempts. Same three words.
#   - Her thoughts spiral into File 7-Delta-11-38: Hana's daughter's name, the form
#     that erased her, the routing stamp. Lyra filed it at sixteen.
#   - She recognizes that her Ethereal pattern recognition — the skill that found
#     Hana today — is the same skill the Academy sharpened to file the disappearance.
#     The gift and the weapon are the same object.
#   - She cannot locate the edge between her training and herself.
#   - She wonders about her mother — same Academy, presumably the same discovery.
#   - She closes the journal without writing. Her hand drifts to the Band.
# cann.voice_profile:
#   - Fragmentary. The measured catalogue is failing. Sentences start and stop.
#     The pattern-recognition she uses as a tool turns on her — she is seeing the
#     connections and cannot unsee them.
#   - Still precise at the object level (routing stamps, form numbers, her age)
#     because precision is the only thing that still works. The precision is itself
#     now evidence against her.
#   - No prayer cadence here — that frame has retreated. She is not trying to file
#     this feeling. She is trying to survive being the one who filed others.
# cann.reveal:
#   - The Ethereal pattern recognition she has been told is a gift was weaponized
#     before she knew what it was. She did not earn the skill — she was shaped into
#     the skill.
#   - The Band-check compulsion from a2_int_lyra_check recurs unconsciously at the
#     end of the scene. It has escalated. She is no longer counting pulses — she is
#     reaching for the Band for the warmth of a thing that cannot leave her wrist.
# cann.callbacks:
#   - a2_int_lyra_check: the Band ritual. Worse now. Automatic rather than intentional.
#   - a3_s05a_woman_from_sector_7_emp: the Hana encounter. The scene that broke this one.
#   - Glass Academy: the pattern-recognition training. Liora's letter (a3_s18a) will
#     later name the suppressants that sealed Aeron's memories — the Academy has form
#     for weaponizing children before the children know what is being taken.
#   - Lyra's mother: first direct internal reference. Seeds Act 4 material.
# cann.block_status:
#   - INTERLUDE. EMP path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - Lyra's mother as an unresolved question: Act 4 thread.
#   - The journal remains unfinished. The practice itself is now in doubt.
#   - Band-check escalation: visible to Aeron in later field scenes?
#   - "I cannot find the place where the weapon ends and I begin" — recurring thematic
#     line for Lyra's Phase II arc.
