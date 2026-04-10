# =======================================================
# ACT 3 - Interlude: Selene — "Nineteen Years"
# File: a3_int_selene_nineteen_years_emp.rpy
# Type: LI THOUGHT INTERLUDE (Selene, EMP)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_selene_nineteen_years_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_selene_nineteen_years_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 85mm. Tight on the cipher in her palm. One slow pull to her hand and
    #         the edge of the nightstand. No face until the final beat, and even then
    #         only from the jaw down.
    # LIGHTING: Single low lamp. The cipher catches the light and holds it. Everything
    #           past her wrist is soft dark.
    # SFX: The small metallic shift of the cipher turning between her fingers. One
    #      slow exhale. The hum of the base at the threshold of hearing.
    # FACE: Selene — jaw set, then not set. A thing loosening without permission.

    # scene bg selene_quarters_night with fade
    # show selene tired at center
    # play ambient "audio/amb/base_quiet.ogg" fadein 1.5

    sthought "OPERATION: Rylan integration."
    sthought "OBJECTIVE: Evaluate subject for shared-command viability."
    sthought "CURRENT STATUS: compromised."

    sthought "RECOMMENDATION—"
    sthought "..."

    sthought "The recommending party is the party being compromised. The briefing cannot file itself."

    sthought "The metal is warm. It should not still be warm. I have been holding it for too long."

    sthought "Nineteen years. Nineteen years of the cipher in a drawer. Nineteen years of every operation begun and ended by one signature. Mine."

    sthought "I."

    sthought "Kael."

    sthought "I have not said his name in fifteen months. I have not thought it tonight until this second. It arrived without being filed."

    sthought "Lieutenant. Efficient call. Operation Verdant. The language I built for him so the weight would stack cleanly in the drawer with the cipher."

    sthought "Kael held his coffee cup with both hands."

    sthought "That is not on any form I ever signed."

    sthought "Tonight was the first time in a decade I was not the only person in the room planning the next move. I do not know where to file that. The drawer is full."

    sthought "OPERATION: Rylan integration. Continue. Monitor subject."

    sthought "Monitor self."

    sthought "..."

    sthought "I am leaving that last line in the briefing."

    # She sets the cipher down. She does not close the drawer.

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_selene_nineteen_years_emp
# cann.chapter: Act III, Phase II — Deepening
# cann.placement: After a3_s14_cipher_and_skin_emp (the first kiss scene). Selene
#                 alone in her quarters, late night. The command cipher on the
#                 nightstand. She picks it up. The weight is old. The weight is hers.
# cann.what_happened:
#   - Selene attempts to process the evening in her default register: the operational
#     briefing. The briefing format is how she has thought about herself for nineteen
#     years — not "I," but "the commander."
#   - She files Aeron as an operation. Status: compromised. She tries to continue to
#     the recommendation line and cannot — the recommending party is also the
#     compromised party.
#   - The briefing breaks. The first-person pronoun surfaces for the first time in
#     the scene: "I."
#   - Kael — her lieutenant, lost to her own efficient call three years ago — arrives
#     in her thoughts without warning. She has not said his name in fifteen months.
#   - A specific, non-operational detail returns: he held his coffee cup with both
#     hands. Nothing she ever had to file. Nothing the briefing format could hold.
#   - She reasserts the briefing as protection, but adds a new line: "Monitor self."
#     She notices the new line and does not delete it.
# cann.voice_profile:
#   - Tactical even in solitude. The briefing format is not performance — it is how
#     her interior actually runs. It is the scaffolding of nineteen years of solo
#     command and the trained management of every loss.
#   - Suppression of the first-person pronoun is the tell. When "I" appears, it is
#     the first crack. When "Kael" appears, the crack has already spread.
#   - Precision of object detail (the coffee cup, the warmth of the metal) because
#     precision is what survived the grief triage.
# cann.reveal:
#   - The pragmatism Aeron has been reading as emotional distance is actually trained
#     grief management. The briefing format is how she has kept Kael and every other
#     name in the drawer from flooding the room.
#   - Tonight — the kiss — is the first time in nineteen years she has voluntarily
#     allowed another human past the edge of that drawer. The cost is that the drawer
#     does not stay closed on command anymore.
# cann.callbacks:
#   - a3_s14_cipher_and_skin_emp: the kiss. The cipher on the nightstand in this
#     interlude is the one from that scene. The metal warmth is the continuity.
#   - Kael: first direct name. Will return in a3_int_selene_kael_emp and seeds Phase III.
#   - "Monitor self" — new internal line. Recurs as Selene's private shorthand for
#     the thing the briefing format cannot contain.
# cann.block_status:
#   - INTERLUDE. EMP path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - Kael as unresolved thread: a3_int_selene_kael_emp goes deeper into the grief.
#   - The drawer as recurring image for Selene's suppression architecture.
#   - "The recommending party is the party being compromised" — her Phase III problem
#     in one line. Her command self cannot objectively evaluate her compromised self.
