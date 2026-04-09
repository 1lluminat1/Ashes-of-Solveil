# =======================================================
# ACT 2 - Scene 20: Doctrine Declaration
# File: a2_s20_doctrine_declaration.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s20_doctrine_declaration"
$ scene_mark(_current_scene_id, "entered")

label a2_s20_doctrine_declaration:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. Two-shots of Aeron and Selene at the strategy table. The room is empty — just them.
    #         Push-in when the doctrine line arrives. Hold on Aeron's face for the choice. No cuts during the silence.
    # LIGHTING: Night. Single overhead map-light on the strategy table (warm amber, 3000K).
    #           Rest of the room in deep shadow. Their faces lit from below by the maps.
    # SFX: Loop — base at rest (distant generator hum, muffled voices through walls, one drip somewhere).
    #       One-shot — map unrolling, marker tapping, Selene's chair scraping back.
    # BLOCKING/PROPS: Strategy alcove. Map table. Two chairs. Cold tea in mugs nobody's touched.
    #                 On the table: operational plans for the next phase. Names. Sectors. Numbers.
    # FACE: Selene watchful, testing. Not hostile — calibrating. She needs to know what kind of commander he is.
    #        Aeron carrying the weight of the recruitment wave. The names are getting heavier.

    # ========== LATE NIGHT — STRATEGY ALCOVE ==========

    "The base goes quiet in layers."

    "Voices first, then footsteps, then the clatter of cleaned trays. The generator hum stays — it always stays — but everything human folds into it until the only sound left is the building breathing."

    "Selene is waiting at the strategy table when Aeron arrives."

    sel "Close the door."

    # VISUAL: Small room. Map light. Two mugs of tea going cold. Plans spread across the table.
    "The door seals them in. Just the two of them, the maps, and whatever this conversation is about to become."

    sel "Sit."

    "Aeron sits."

    sel "I've been watching you with the recruits."

    a "And?"

    sel "You're good at it. Better than I expected. You read people. You know which questions to ask and which silences to let breathe."

    "She taps a marker against the table. Thinking."

    sel "But I need to know something before we go further. Before I hand you command over screening, over training, over any of the operational authority that comes next."

    a "Ask."

    sel "What do you believe?"

    # ========== THE QUESTION ==========

    "The question sits between them like something physical."

    athought "What do I believe."

    sel "Not what you were taught. Not what Marcus drilled into you. Not what the uniforms say."
    sel "What do YOU believe about how this works? How order works. How mercy works. How we win without becoming what we're fighting."

    "She leans forward. The map-light catches the lines under her eyes — the ones command put there."

    sel "Because I've seen two versions of you."

    if scene_has("a2_s12_proof_of_intent", "guard_spoken_to"):
        sel "The one who talked a guard into walking away. And the one who built the system that put him on that post."
    elif scene_has("a2_s12_proof_of_intent", "guard_spared"):
        sel "The one who found a drain grate to spare a nineteen-year-old. And the one who designed the facility he was guarding."
    else:
        sel "The one who authorized a kill without hesitating. And the one who sat with the weight of it after."

    sel "Both of those are real. I need to know which one is driving."

    # ========== THE DOCTRINE ==========

    "Aeron is quiet for a long time."

    athought "Order is mercy at scale."

    "The phrase arrives without invitation. Marcus's voice. Marcus's cadence. The words he carved into every briefing, every debrief, every silence where a son might have heard something gentler."

    athought "Order is mercy at scale. Chaos is cruelty. Through precision, peace."

    athought "I've been carrying that since I was twelve years old."

    sel "You're thinking about it. I can see it working behind your eyes."
    sel "Say it out loud. Whatever it is. I need to hear it."

    # ========== THE CHOICE ==========

    menu:
        athought "Marcus's doctrine. The words I was built on. Do I still believe them?"

        "\"Order is mercy at scale.\"":
            $ choice_and_dev(
                _current_scene_id, "_affirm_doctrine", "OB", factor=2,
                note="Affirms Marcus's doctrine. Believes order prevents more suffering than compassion alone."
            )
            $ flag("ob_doctrine", True)
            $ STATE["empathy_decay"] = 1
            $ STATE["empathy_decay_steps"] = 3
            $ scene_mark(_current_scene_id, "doctrine_ob")

            a "Order is mercy at scale."

            "He says it cleanly. No hesitation. The words fit his mouth the way they always have — worn smooth by repetition, sharp underneath."

            a "I know how that sounds. Coming from me. Coming from Glass."
            a "But I've seen what happens when there's no structure. No chain. No one making the calls that cost something."
            a "Compassion without order is just grief with better intentions. It doesn't save anyone. It just makes the dying feel acknowledged."

            sel "And order without compassion?"

            a "Is what Marcus built. And it failed. Not because order was wrong — because HE was wrong. He used order as a mask for control. I won't."

            "Selene studies him. A long, careful look."

            sel "You sound like him, you know. When you talk like that."

            a "I know."

            sel "That terrifies me."

            a "It should."

            "She picks up her tea. Drinks it cold. Sets it down."

            sel "At least you know what you are. That's more than Marcus ever managed."
            sel "I'll work with doctrine if the man behind it stays honest about what it costs."

            athought "Order is mercy at scale."
            athought "I said it. I meant it."
            athought "And Selene's face when I said it looked like someone watching a wound they can't stitch."

        "\"That's what Marcus taught me. I don't think I believe it anymore.\"":
            $ choice_and_dev(
                _current_scene_id, "_reject_doctrine", "EMP", factor=2,
                note="Rejects Marcus's doctrine. Believes people matter more than systems."
            )
            $ flag("emp_doctrine", True)
            $ STATE["emp_boost_window"] = 2
            $ scene_mark(_current_scene_id, "doctrine_emp")

            a "Order is mercy at scale."

            "He says it. Then stops."

            a "That's what Marcus taught me. Every morning. Every briefing. Every silence where he could have said something human instead."

            a "I don't think I believe it anymore."

            sel "What changed?"

            a "Elara. Today. She sat across from me and told me her daughter's name. Naia."
            a "Designation 248 was never a designation. She was a girl named Naia who lived in an apartment in Sector 6."
            a "Order didn't save Naia. Precision didn't save her. The scale that was supposed to make it mercy was the thing that killed her."

            "He looks at the maps on the table. Names. Sectors. Numbers."

            a "I'm done building systems that count people instead of knowing them."

            sel "(quiet) That's going to cost you."

            a "I know."

            sel "Mercy multiplies risk. Every person you stop to save is a second someone else doesn't get."

            a "Then I carry the cost. But I carry it knowing the names."

            "Selene is quiet for a long time. When she speaks, her voice is different. Softer. Not weaker — just honest."

            sel "Kael. My lieutenant. Three years ago. I made the efficient call and he died for it."
            sel "I still know his name. That doesn't make the math easier."

            a "No. But it makes the math honest."

            sel "...Yeah. I suppose it does."

            athought "I rejected it. Marcus's doctrine. The foundation I was built on."
            athought "The ground feels less stable now."
            athought "But the names are clearer."

    # ========== SCENE CLOSE ==========

    "They sit in the strategy alcove until the tea is unsalvageable and the maps blur in the low light."

    "Neither of them says anything else that matters. They don't need to."

    "What needed saying got said."

    sel "(standing) Tomorrow we plan the next operation. Massive scale. Full deployment."
    sel "Whatever you believe — you'll need to act on it."

    "She pauses at the door."

    sel "Aeron."

    a "Yeah?"

    if scene_has(_current_scene_id, "doctrine_ob"):
        sel "Don't let the doctrine eat the man. Marcus made that mistake. Don't repeat it."
    else:
        sel "Don't let the mercy slow the blade. Some calls still have to be fast."

    "The door closes."

    "The map-light hums."

    "Aeron sits alone with the plans, the cold tea, and the shape of whatever he just became."

    # ========== STATE UPDATES ==========

    $ flag("doctrine_declared", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s20_doctrine_declaration
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night after the recruitment wave. Before Aeron takes expanded command authority.
#   - Soft-lock scene: emotionally significant, mechanically soft. Hard lock at Massive Recruitment.
# cann.what_happened:
#   - Selene asks Aeron what he believes — not what he was taught, what he actually holds true.
#   - Marcus's doctrine surfaces involuntarily: "Order is mercy at scale."
#   - Player chooses:
#       OB: Affirms the doctrine. Believes order prevents more suffering than compassion alone.
#           Acknowledges he sounds like Marcus. "It should terrify you." Selene works with it, warily.
#       EMP: Rejects the doctrine. Names Naia (Elara's daughter from recruitment scene).
#           "Designation 248 was never a designation. She was a girl named Naia."
#           Selene shares her own name — Kael, a lieutenant she lost to an efficient call.
#   - Both paths end with Selene's warning: don't let doctrine eat the man / don't let mercy slow the blade.
#   - Closes with Aeron alone in the strategy alcove, sitting with who he just declared himself to be.
# cann.aeron_state:
#   - The first time Aeron articulates his philosophy out loud, to someone who needs to hear it.
#   - OB: speaks Marcus's language but claims it as his own. Knows the cost. Selene sees the danger.
#   - EMP: uses Naia's name as the fulcrum. Designation→person. The math becomes honest, not easier.
# cann.path_tracking:
#   - One choice_and_dev decision (factor=2, significant):
#       - _affirm_doctrine → OB +2, flag("ob_doctrine"), empathy_decay=1 for 3 choices
#       - _reject_doctrine → EMP +2, flag("emp_doctrine"), emp_boost_window=2
#   - flag("doctrine_declared") set for future gating.
#   - Mechanically soft: does NOT lock path. Hard lock at Massive Recruitment (a2_s22).
#   - Empathy decay/boost affects the NEXT 2-3 major decisions via apply_empathy_with_mod().
# cann.thematic_flags:
#   - "Order is mercy at scale" — Marcus's doctrine as inherited architecture. Said or rejected, it shapes.
#   - OB path: "You sound like him." "I know." "That terrifies me." "It should."
#   - EMP path: Naia callback from recruitment wave. Designation→name as moral fulcrum.
#     Selene's Kael — she too carries a name she lost to efficiency. Parallel weight.
#   - Both paths: Selene's warning as parting shot. She sees what he is and tells him the danger of it.
#   - "Whatever you believe — you'll need to act on it." — doctrine isn't abstract after tonight.
# cann.character_moments:
#   - Selene: Testing, not hostile. She needs to know what kind of commander she's building with.
#     OB: "At least you know what you are." Grudging respect laced with fear.
#     EMP: Shares Kael's name. Vulnerability she rarely shows. Parallel grief.
#   - Aeron: Confronting the architecture Marcus built in him. Either claiming it or tearing it down.
#     Neither choice is comfortable. The scene earns that discomfort.
# cann.design_notes:
#   - Doc 38 originally placed Nyra in this scene. Nyra is Act III+ / OB-exclusive (after Selene's death).
#     Scene rewritten with Selene as catalyst and Marcus's doctrine as the text.
#     Nyra's philosophy ("Order is mercy at scale") is inherited from Marcus — she'll echo it in Act III.
#     The through-line is preserved: Aeron encounters this doctrine in Act II, Nyra embodies it in Act III.
# cann.block_status:
#   - ANCHOR (both paths). Doctrine soft-lock scene. Determines empathy_decay or emp_boost for next phase.
# cann.requires_followup:
#   - ob_doctrine / emp_doctrine flags gate flavor text in subsequent scenes.
#   - empathy_decay_steps / emp_boost_window affect next 2-3 choices via apply_empathy_with_mod().
#   - Selene's warning should echo in Act 3 — "Don't let the doctrine eat the man" or "Don't let mercy slow the blade."
#   - EMP: Naia callback chain continues (Elara → doctrine → future confrontation with cost of mercy).
#   - OB: Marcus comparison chain escalates (sounds like him → becomes like him → exceeds him?).
