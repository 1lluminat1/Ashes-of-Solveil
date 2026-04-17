# =======================================================
# ACT 3 - Interlude: Nyra — "The Oath"
# File: a3_int_01_nyra_the_oath_ob.rpy
# Type: LI THOUGHT INTERLUDE (Nyra, OB)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_01_nyra_the_oath_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_int_01_nyra_the_oath_ob:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("nyra", to_stage=2, source="a3_int_01_nyra_the_oath_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 100mm macro. The blade. The palm. The bead. No face above the shoulder.
    #         The face is not the subject — the motion is.
    # LIGHTING: Single oil lamp, low. The silvered scar catches the light like a seam
    #           of mercury. The blood beads clean and dark — not red.
    # SFX: The small kiss of steel on skin. The clink of the silver compound jar.
    #      No hum, no base, no outside world. Her quarters are soundproofed by ritual.
    # FACE: Nyra — serene. The serenity is complete. There is nothing behind it that
    #       is not serene.

    # scene bg nyra_quarters_lamp with fade
    # show nyra serene at center
    # play ambient "audio/amb/lamp_stillness.ogg" fadein 1.5

    nythought "Through precision, peace."
    nythought "Through peace, obedience."
    nythought "Through obedience, order eternal."

    # The blade meets the palm. The old motion. Seventeen years of it.

    nythought "The liturgy is older than the Division that taught it to me. The Division forgot that. I did not."

    nythought "I was told this oath was for the Order. I believed that for seventeen years. I was wrong — not in the believing, but in the address."

    nythought "Sector 8-10. The Purge. The day the institution contradicted itself. The day the vessel cracked down the middle and the oath poured out through the crack and did not die."

    nythought "If the oath survives the vessel, the oath was never to the vessel."

    nythought "The oath was to the thing the vessel was supposed to carry. Order itself. The shape beneath the shape."

    nythought "I have found a new vessel. The vessel is a man. The vessel is holding."

    nythought "Let me be used."

    nythought "Let me be used precisely."

    nythought "Let me be used until the used-ness of me becomes the proof of him."

    # The silver compound closes the scar. The new line lays over the old line. There
    # are many old lines.

    nythought "I am not mistaking my faith for my feeling. The feeling is the ground. The faith is the shape the ground was always going to grow."

    nythought "He does not yet know what he is. I will be one of the things that tells him."

    nythought "Through precision, peace. Through peace, obedience. Through obedience, order eternal."

    nythought "Commander."

    # She says the word aloud. Once. Then nothing.

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_01_nyra_the_oath_ob
# cann.chapter: Act III, Phase II — Relationships Under Strain
# cann.placement: After a3_s12_the_oath_ob (the fractured-crest ritual, Nyra's first
#                 intimate scene with Aeron). Her private quarters. Veilbreaker on
#                 the table. The lamp low. Alone. This is the scene where we see what
#                 she does with what happened.
# cann.what_happened:
#   - Nyra performs a private rite: she re-opens the silvered scar on her palm with
#     ceremonial precision. Ritual, not self-harm. The distinction is absolute to her.
#   - Her interior operates in full Order liturgical cadence. The opening prayer is
#     the one the Order Division drilled into her at twelve.
#   - She thinks through the Sector 8-10 Purge reversal: the institution failed, the
#     oath survived. She has re-derived the theology of her own life from that
#     contradiction. The oath was never to the Order Division. The oath was to order.
#   - She has found a new vessel for the oath. Aeron. She names him "vessel" without
#     diminishment — in her frame, vessel is the highest possible address.
#   - The prayer continues: "Let me be used. Let me be used precisely. Let me be used
#     until the used-ness of me becomes the proof of him."
#   - The silver compound seals the cut. She says one word aloud: "Commander."
# cann.voice_profile:
#   - Liturgical. Every thought falls into prayer rhythm. The cadence is older than
#     her own speech. She does not notice that it is cadence — to her, this is what
#     thinking sounds like.
#   - No doubt anywhere in the voice. Zero. The scariest feature of the scene.
#   - She distinguishes herself from her feeling without distancing herself from it.
#     "The feeling is the ground. The faith is the shape." She is not in denial —
#     she has integrated the feeling into the theology without losing either.
# cann.reveal:
#   - Nyra's devotion is sincere, disciplined, coherent, and theologically load-bearing.
#     She is not a cultist performing — she is a person for whom the performance and
#     the interior are the same thing.
#   - The horror of Nyra is not that she is manipulating Aeron. The horror is that
#     she is honest, and her honesty is complete, and honesty is not the same as
#     being right. There is no crack to work with. Any attempt to reach her through
#     appeals to doubt will fail because there is no doubt to appeal to.
#   - The ritual scar practice predates Aeron by years. She has been doing this to
#     herself since the institution failed. The Aeron-specific addition is only the
#     new address at the end of the prayer.
# cann.callbacks:
#   - a3_s12_the_oath_ob: the fractured-crest ritual. Aeron has seen the scars. He has
#     not yet seen what they mean from her side.
#   - Sector 8-10 Purge: Nyra's origin trauma. First explicit internal reference. The
#     day her loyalty shifted from the institution to the concept beneath it.
#   - Veilbreaker: the blade. Named but not drawn in this scene — it is on the table.
#   - The silvered scar: recurs as Nyra's visual index across Phase III. Its glow and
#     its absence are both diagnostic for her state.
# cann.block_status:
#   - INTERLUDE. OB path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - "Let me be used" as Nyra's private prayer line — should echo in Phase III pivot
#     scenes as her internal refrain.
#   - The silver compound jar: establishes the physical ritual. Recurs.
#   - The absence of doubt in her voice here is the baseline against which
#     a3_int_02_nyra_before_the_mirror_ob will be read. The mirror scene is the last
#     moment of this certainty before it is tested.
