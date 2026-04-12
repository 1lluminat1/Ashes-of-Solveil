# =======================================================
# ACT 3 - Interlude: Tessa — "The Board"  (EMP)
# File: a3_int_tessa_the_board_emp.rpy
# Type: LI THOUGHT INTERLUDE (Tessa)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_tessa_the_board_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_tessa_the_board_emp:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("tessa", to_stage=2, source="a3_int_tessa_the_board_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: The board in full for the first beat. Then in close on the marker tip,
    #         the letters forming. Then wider — both columns in frame, the name in both.
    # LIGHTING: Pre-dawn. The room is cold blue. The board is lit by a single work
    #           lamp clipped to its upper edge. Everything else is suggestion.
    # SFX: The secondary base at its quietest hour. Distant water moving in pipes.
    #      The squeak of the marker. Her breath, measured, longer exhale than inhale.
    # FACE: Tessa — composed in the way that means she is choosing the composure. Once,
    #       when the name is on both sides of the board, the composure fractures at
    #       the corner of the mouth and then holds.

    # scene bg phoenix_base_board_predawn with fade
    # show tessa neutral at center
    # play ambient "audio/amb/base_predawn.ogg" fadein 1.5

    tthought "The living column first. That is the rule. Living first, always, because living is the one I am trying to keep."

    tthought "LIORA RYLAN."

    tthought "The letters go where the letters go. My hand did not hesitate. That surprises me and it does not surprise me."

    tthought "Living. Because she kept names. Because every name she kept was a person she saved, and some of those people are alive right now because she remembered them when they could not remember themselves."
    tthought "The definition of living expands when I write her there. I am allowed to expand it. The board belongs to me."

    tthought "Now the other column."

    tthought "LIORA RYLAN."

    tthought "Dead. Because of the body. Because of the Aeries platform. Because of the broadcast. Because of the man who is her father and who did it."
    tthought "The definition of dead does not need to expand. It is plain as teeth."

    tthought "Both entries. Same name. Different reasons."

    tthought "This has never happened on the board before."

    tthought "The board has been my sanity. I want to say that clearly, even only to myself: the board has been the thing that kept me a person across three years of this. I could look at it and find where I was."
    tthought "I cannot find where I am on it tonight."

    tthought "A person can be counted as living for what they did. A person can be counted as dead for what was done to them. The board will have to hold both. I will have to learn to read it differently."

    tthought "I do not know how yet."
    tthought "I will learn by morning. I always do."

    tthought "The marker is capped. The lamp is still on."
    tthought "I am leaving before the room has anyone else in it. I do not want to be seen at the board right now."

    tthought "Her name is there. On both sides. I will come back to it."

    # stop ambient fadeout 1.5

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_tessa_the_board_emp
# cann.chapter: Act III, Phase III — Revelation & Cost
# cann.placement: After a3_s22_liora_execution_emp, before a3_s23_aftermath_emp.
#                 Pre-dawn. Tessa alone at her board at the secondary base. She has
#                 not slept. She came here instead of the medbay.
# cann.what_happened:
#   - Tessa writes LIORA RYLAN on the board. Her hand goes to the living column first.
#     That is the rule. Living first.
#   - She then writes the same name on the dead column. The body. The platform. The
#     broadcast. The father.
#   - She looks at both entries. This has never happened on the board before. No name
#     has ever been on both sides.
#   - Her philosophy attempts to flex under the weight. "Living" expands — a person
#     can be counted as living for what they did. "Dead" does not expand. A person can
#     be counted as dead for what was done to them. The board will have to hold both.
#   - She does not resolve how to read the board now. She caps the marker. She leaves
#     before the room has anyone else in it.
# cann.voice_profile:
#   - The gentle present-tense voice fractionally harder than it has ever been. Not
#     bitter. Structural. She is updating the framework because the old framework
#     cannot hold Liora and she refuses to erase Liora to keep the framework.
#   - Itemized. Plain. Short declarative sentences near the end.
#   - The phrase "plain as teeth" is the tell — her language is getting sharper at the
#     edges under pressure.
# cann.reveal:
#   - "Count the Living" was never static. The philosophy is evolving under the weight
#     of Liora's death. Tessa is choosing to expand the definition of "living" rather
#     than erase a name she cannot let go of.
#   - The board is no longer sufficient as written. Tessa does not yet know what it is
#     becoming. She is going to find out by morning because she always does.
#   - She explicitly does not want to be seen at the board right now. The ritual is
#     private and she is protecting it. This is a thing she has not done before.
# cann.callbacks:
#   - a2_int_tessa_torins_name: the rule (living first, always, because living is the
#     one she is trying to keep). The rule is still operative. The rule is under stress.
#   - a2_s23_mercy_and_counting: the mercy-death discipline. Liora is a new kind of
#     case the mercy-death discipline does not cover.
#   - a3_s22_liora_execution_emp: the scene this follows directly.
#   - Liora's letter (a3_s18a): "brave enough to be soft when softness is the most
#     dangerous thing." Tessa is performing the lesson in real time.
#   - Future: a3_s23_aftermath_emp — Tessa arrives at aftermath already having done
#     this private work. She should not need to re-do it out loud.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. EMP-route only.
# cann.requires_followup:
#   - Any later reference to Tessa's board should acknowledge that a name lives on
#     both sides now. This is the new canonical state of the board.
#   - Tessa's grief discipline is visible as choice, not reflex, from this point on.
