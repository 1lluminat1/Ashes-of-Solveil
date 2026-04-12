# =======================================================
# ACT 3 - Interlude: Selene — "Kael"
# File: a3_int_selene_kael_emp.rpy
# Type: LI THOUGHT INTERLUDE (Selene, EMP)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_selene_kael_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_selene_kael_emp:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("selene_valen", to_stage=2, source="a3_int_selene_kael_emp")
    $ codex_reveal("kael_rylan", to_stage=2, source="a3_int_selene_kael_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm from the foot of the bed. Her profile against pre-dawn grey. The
    #         plant on the windowsill in soft focus behind her. Aeron only as a shape
    #         of breathing under the sheet. One slow push-in on the one hand she has
    #         placed on the sheet between them.
    # LIGHTING: First dawn. Cold at first, then — on the plant — warm. The warmth
    #           reaches the plant before it reaches her.
    # SFX: Two people breathing. One asleep. One not. The base hum gone entirely.
    # FACE: Selene — unguarded. For the first time in the scene there is nothing
    #       watching the face from inside the face.

    # scene bg selene_quarters_predawn with fade
    # show selene soft at center
    # play ambient "audio/amb/dawn_quiet.ogg" fadein 2.0

    sthought "He's still asleep."

    sthought "I am trying to decide if watching counts as touching. I do not have a form for this."

    sthought "I am not filing this one."

    sthought "Kael held his coffee cup with both hands. Both hands, around a standard-issue mug, like it was a small bird he did not want to crush."

    sthought "I had forgotten that. Three years. I was so careful to forget it."

    sthought "The morning he told me about his daughter. He said her name twice because the first time he was testing it in his mouth and the second time he was giving it to me."

    sthought "His laugh. I have not heard his laugh in my head in so long I thought the file had degraded. It has not. I was holding it shut."

    sthought "I made the efficient call. I am still the person who made the efficient call. That does not go away because I am crying in the dark beside a man who cannot see my face."

    sthought "I am afraid I will make the call again."

    sthought "I am more afraid I will not make it when I should."

    sthought "Neither of those is the reason for the crying."

    sthought "The plant."

    sthought "Eleven years. I have kept that plant alive for eleven years. It is the only thing in these quarters that was never tactical. I bought it because the window was empty and I could not stand the emptiness on a Tuesday."

    sthought "I did not know that was what I was doing. I thought I was buying a plant."

    sthought "The first light is on its leaves. Not on me yet. On the plant first."

    sthought "I have been keeping things alive for a long time."

    sthought "I am, I think, trying to be one of them."

    # She wipes her face with the back of her hand before he can stir.

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_selene_kael_emp
# cann.chapter: Act III, Phase II — Deepening
# cann.placement: After a3_s16_command_and_surrender_emp (the first erotic scene).
#                 Pre-dawn. Her quarters. Aeron asleep beside her. The plant on the
#                 windowsill taking the first light. Selene watching him breathe and
#                 not touching him, on purpose.
# cann.what_happened:
#   - For the first time in the interlude sequence, Selene's briefing format does not
#     engage. The voice is uncalibrated. The voice is her.
#   - She remembers Kael not as a file but as a man. His laugh. The coffee cup. His
#     daughter's name, said twice. The morning-of details the briefing never had room for.
#   - She names her two operational fears (making the call again / not making it when
#     she should) and then names them both insufficient. Neither is the reason for
#     the tears.
#   - The plant on the windowsill surfaces as the scene's actual subject. She has kept
#     it alive for eleven years without understanding that the keeping was the point.
#   - The recognition: she has been keeping things alive professionally and privately
#     her whole life, and has never counted herself as one of the things.
#   - She wipes her face before Aeron wakes. The discipline holds the face. The
#     discipline does not hold the interior anymore.
# cann.voice_profile:
#   - Briefing format gone. Sentences are short because the interior is exposed, not
#     because it is being managed.
#   - Precision survives, but it is the precision of private memory (a mug, a laugh,
#     a morning), not the precision of tactical objects.
#   - First-person pronoun unrestricted. This is the first Selene interlude where
#     "I" is the default voice.
# cann.reveal:
#   - Kael's file was never filed. It was sealed. Her forgetting was deliberate labor
#     for three years, and Aeron's arrival has broken the seal.
#   - She is grieving Kael for the first time tonight. The briefing format was never
#     processing the grief — it was quarantining it.
#   - The plant is the quiet confession: she has always known how to tend a life. She
#     just never included her own.
# cann.callbacks:
#   - a3_int_selene_nineteen_years_emp: the briefing format and the first crack. This
#     scene is the crack opening all the way. The coffee cup detail recurs because
#     it was the first image that did not fit the briefing.
#   - a3_s16_command_and_surrender_emp: the erotic scene. The sheet, the sleeping
#     figure, the held breath of the body beside her.
#   - The plant: establishes Selene-private-life visual. Recurs across Phase III as
#     an index of her interior state. Watering the plant in later scenes is not
#     decorative blocking.
#   - Kael's daughter: seeds Phase III / Act 4 material. Selene has carried a name
#     for three years that she has never said aloud.
# cann.block_status:
#   - INTERLUDE. EMP path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - Kael's daughter's name: held back deliberately in this scene. Available for
#     later reveal when the emotional ground is earned.
#   - The plant as recurring image across Phase III.
#   - "I am trying to be one of them" — Selene's Phase III through-line, private,
#     never said aloud to Aeron until the Act closer.
