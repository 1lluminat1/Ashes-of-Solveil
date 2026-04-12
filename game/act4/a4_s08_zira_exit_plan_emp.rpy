# =======================================================
# ACT 4 - Scene 08: Zira's Exit Plan (Empathy Path)
# File: a4_s08_zira_exit_plan_emp.rpy
# Type: ZIRA INTIMACY BEAT — non-erotic, deepening.
# Matrix: Zira has built an exit plan for Aeron. He finds it. Neither hides.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s08_zira_exit_plan_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s08_zira_exit_plan_emp:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("zira", to_stage=3, source="a4_s08_zira_exit_plan_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, closer than the war room scenes. The workshop is a room of
    #         hands, and hands are the scene. Open on the bench — wide enough
    #         to read the objects laid out on it without naming any of them.
    #         Zira's hands are in frame before Zira's face. That is a rule for
    #         every Zira-in-the-workshop scene and the rule holds here.
    #         When Aeron enters: the camera pivots to follow him to the bench.
    #         It does not cut to his face yet. His face enters the scene at the
    #         same moment the objects on the bench enter his understanding.
    #         Two-shot across the bench once they are both standing at it. Zira
    #         on the left. Aeron on the right. The exit plan between them. Hold
    #         the two-shot through the first exchange. The scene earns closer
    #         coverage slowly — she does not look up until she chooses to.
    #         When she does: tight on her. Not tight-tight. The kind of medium
    #         tight that respects her without pinning her. Zira is a woman who
    #         has not let a camera pin her since the Ashmarket, and the scene
    #         does not try.
    #         Closing beat: tight on her hands folding the papers. The drawer
    #         opening. The papers going in. Her hand on the drawer — closing
    #         it, but not locking it. The unlocked drawer is the scene's final
    #         image. Hold on the drawer. The rest of the room is out of focus.
    # LIGHTING: Zira's workshop, late. Three pools of warm light — the bench
    #           lamp, the lamp over the forge corner, the small clip lamp
    #           she uses for close work. The rest of the workshop is in
    #           warm darkness. Zira's face is half in the bench lamp and
    #           half in the shadow of her own shoulder when she is bent
    #           over her work. When she straightens, she comes fully into
    #           the light. The coming-into-the-light is not dramatic. It is
    #           the rhythm of a woman who has worked in half-light for a
    #           decade.
    # SFX: Workshop at night. The forge banked. A distant drip from the
    #      pipe in the north corner she has been meaning to fix for a
    #      month. Her hands on paper — a particular sound. The sound of
    #      smooth forgery paper being pressed flat under a thumb. The
    #      scratch of a fine pen. The scrape of a weight being moved from
    #      one corner of a document to another. Her breath. Aeron's boots
    #      on the workshop stone. The door closing behind him.
    #      No music bed until the final beat. One low cello note at the
    #      folding. Then silence.
    # FX/COMP: THE EXIT PLAN. Physical description of the objects on the
    #          bench:
    #          - Three sheets of forged identity papers. Different aliases.
    #            Different hands. Zira has forged all three herself and the
    #            hands are not the same hand. She has been trained.
    #          - A hand-drawn chain map of safehouses, four stops, running
    #            from the secondary base out through the western passes
    #            and then north along a route Aeron does not recognize.
    #            The fourth stop is not named. The fourth stop is marked
    #            with a single character in Old Tongue — a character Zira
    #            has written in a different ink from the rest.
    #          - A small oilskin wrap containing two pieces of pre-paid
    #            Ashmarket currency, a cipher key for Ghostline quiet-route
    #            access, and a knife Aeron has not seen before.
    #          - A folded letter sealed with wax — Zira's seal. No address
    #            on the outside. The letter is the part Aeron is not
    #            supposed to read and she will tell him not to.
    # BLOCKING: Zira is at the bench, bent over the chain map, when Aeron
    #           enters. She hears him come in. She does not look up for
    #           two full beats. When she does, she puts the pen down and
    #           straightens. She does not move to cover the bench. She
    #           does not move anything on the bench. She lets him see it.
    #           Aeron crosses to the bench. Stops at the opposite side.
    #           Looks at the objects. Then looks at her. They hold a long
    #           look across the bench. Then he moves around to her side.
    #           Not to close the distance, but to stand on the same side
    #           of the work with her. This is the physical gesture of the
    #           scene — the move to her side.
    # FACE: Zira — the edge on for the first third, sarcastic armor up, but
    #        thinner than it usually is. The armor is not a performance
    #        tonight; the armor is the only grammar she has for the thing
    #        she is doing. The armor cracks in two specific places and she
    #        does not try to patch it either time.
    #        Aeron — he enters looking for her and finds a gift shaped like
    #        a grief. His face takes the full length of the first three
    #        lines to catch up to what he is seeing. He does not try to
    #        hide the catching-up. Showing her his face is part of what he
    #        owes her for the work on the bench.

    # ========= VOICE BASELINE =========
    # EMP cadence. Zira's voice: the Ashmarket edge is native and does not
    # leave, but the volume of it varies with how exposed she is letting
    # herself be. The scene has three registers — tactical (the plan), sardonic
    # (the armor), and the plain quiet she has used with him maybe twice
    # before. The plain quiet is the rarest of the three and the scene earns
    # it exactly once. Aeron is spare. He lets her do the work of naming
    # things because she is the one who built the thing that is being
    # named.

    # scene bg_zira_workshop_night with dissolve
    # play ambient "sfx/ambient/workshop_forge_banked.ogg" fadein 2.5

    # ========== PHASE 1 — THE DOOR ==========

    "Aeron's day does not end."

    "Aeron's day has been ending for four hours — ever since Noelle closed her phase-two briefing with a locked location on the analyst cell and Selene dismissed the command team with the instruction to eat and sleep in that order. The day has been ending and refusing to end. The day is the day he saw his own counter-strike framework running on the Echelon side of a projection and watched Noelle ask him whether she was still a neutral observer and told her the question stayed open."

    "He is looking for Zira because Zira is the person he looks for when a day refuses to end."

    "Zira is not in the command center, not in the war room, not in the Ghostline relay alcove, not in the commissary. Aeron checks all four in the order Zira is most likely to be in each of them at this hour, and in the fourth he is already walking toward the workshop because the workshop is where Zira goes when the problem she is working on is not a Ghostline problem."

    "He has not been in Zira's workshop in nine days."

    "He knocks once, because Zira keeps a door-knock protocol in the workshop that has nothing to do with ceremony and everything to do with the fact that in the workshop she is often holding something that would be dangerous to drop."

    "A beat."

    z "It's open."

    "He opens it."

    # ========== PHASE 2 — THE BENCH ==========

    "The workshop is in its usual three-lamp configuration. The bench lamp. The forge lamp over the banked forge in the far corner. The small clip lamp Zira uses for close work, clamped tonight to the left edge of the bench and pointed down at a surface Aeron cannot yet see because Zira's shoulder is in the way."

    "Zira is bent over the bench. She has a fine pen in her right hand. Her left hand is holding down a corner of something on the bench with the kind of flat-thumb pressure that says she has been holding the corner down long enough to feel it in her wrist."

    "She hears him come in. She does not look up."

    "Two beats. Three."

    "He does not say anything. She is finishing a line, and finishing a line is a Zira thing, and he has learned over four years of Zira-in-the-workshop scenes not to speak during the finishing of a line because the line is always load-bearing."

    "She finishes the line."

    "She sets the pen down in the groove of the pen tray without taking her eyes off the work."

    "Then she straightens."

    "She straightens in the way of a woman whose back has been bent for longer than her back wants to be bent. The small pain-wince is a fact she does not hide because she has long since given up hiding the small pain-wince from him specifically. That is a form of intimacy. It is the intimacy that made him notice her before any of the rest of it."

    "She turns to look at him."

    "She does not move to cover the bench."

    "She does not move anything on the bench."

    "She lets him see it."

    # ========== PHASE 3 — THE OBJECTS ==========

    athought "The bench is full."

    athought "The bench is full of paper and the paper is not Ghostline work and the paper is not supply manifests and the paper is not schematic drafts for the new quiet-route cipher."

    athought "The paper is me."

    "He crosses to the bench."

    "He stops at the opposite edge. He looks down at what is laid out in the pool of the clip lamp."

    "Three sheets of identity papers. Three different names. Three different hands — because Zira has been trained, and because Zira has always taken seriously the rule that a forger who is willing to be caught by a handwriting analyst is not a forger, she is a decorator."

    "A hand-drawn chain map. Four stops. From the secondary base through the western passes and then north along a route he does not recognize into a country he is not sure whether to call a country. The fourth stop is not named. The fourth stop is marked with a single character in Old Tongue, written in a different ink from the rest of the map."

    athought "Anayet's character for 'threshold.' Not 'home.' 'Threshold.' The fourth stop is a threshold, not a destination. She is not naming the destination because the destination is not the point. The destination is whatever is on the far side of the threshold."

    "A small oilskin wrap. He can see from the way it is folded that the wrap contains currency and something with a weight-profile that is not currency. He does not need to unwrap it to identify a knife. Zira wraps knives in a particular way."

    "And a letter. Folded. Sealed with wax. Her seal. No address on the outside."

    "He looks at the letter for longer than he looks at the other objects combined. He does not pick it up."

    "Then he looks up at Zira."

    "She is watching him read the bench. She has not moved. Her arms are at her sides. Her right hand is still slightly curled from the pen. She is letting her face do whatever her face is going to do, which, in Zira's case, is a controlled amount of nothing until she chooses a sentence."

    "She chooses a sentence."

    z "Go ahead."

    a "Go ahead what."

    z "Go ahead and ask the question. We'll save a half-hour."

    "He does not ask the question. He is not ready to ask the question because the question has more than one shape and he does not yet know which shape to ask in."

    "He asks a different one."

    a "How long."

    z "Three weeks."

    "She says it flat. She does not add a clause. The three weeks are not offered with context. The three weeks are a fact, the same way the letter on the bench is a fact, the same way his name is a fact."

    a "You started three weeks ago."

    z "I started the night you came back from the Obsidian Bridge. I had been thinking about starting for longer. I started that night."

    athought "The Obsidian Bridge was Act I. She has been thinking about this since Act I and building it since Act III. She has been carrying this for as long as she has been carrying the forgery of my codebooks for the Ghostline. In the same hands."

    a "You have been building me an exit."

    z "Yes."

    a "Forged papers. Three aliases. A safehouse chain. An extract currency kit. Ghostline quiet-route key. A knife I have not seen before."

    z "That knife is from the Ashmarket. It is not Phoenix kit. It has no Phoenix fingerprints on it. If you ever need to use the knife, you will not need Phoenix to have been in the room."

    "He does not touch the knife."

    a "The fourth stop on the map is not named."

    z "No."

    a "You are not going to name it for me."

    z "No."

    "She takes a single small breath that is not quite a sigh."

    z "I will tell you this much. I know the person at the fourth stop. I knew her before the Ashmarket. She owes me two favors of the kind of weight that does not get called in unless the caller has nowhere else to go. She does not know your name. She will know it when she sees the letter."

    "His eyes go to the letter on the bench."

    z "Do not open it."

    a "I was not going to."

    z "I know. I am saying it anyway. The letter is not for you to read. The letter is the thing the woman at the fourth stop reads when you give it to her, and what it says to her is not something I am willing to have you carrying in your head while you are still in Solveil."

    z "Carry the letter. Do not read it."

    a "Okay."

    # ========== PHASE 4 — THE EDGE ==========

    "A silence."

    "Aeron is still on his side of the bench. The bench is a narrow thing and the silence is very loud in the narrowness. He is aware, in the peripheral part of his attention, that the correct move in the physical vocabulary of this room is to go around to her side of the bench."

    "He does not go yet."

    "He is not going yet because he has to say something on his own side first."

    a "Zira."

    z "Yes."

    a "I am not going to take this."

    "A small thing happens in her face."

    "The small thing is not hurt. Zira has been hurt in worse ways than this and the ways do not appear on her face the way hurt appears on ordinary faces. The small thing is the sardonic armor coming up in the particular way she uses it when she is about to say something she has rehearsed and does not want him to notice she rehearsed."

    z "Oh, good. I was worried we were going to have to do the scene where the big commander takes the escape bag from his girlfriend and rides off into the sunset with the forged papers. I was mentally drafting the eyeroll."

    a "Zira."

    z "I know, Aeron."

    "Her voice has shed one skin of its sarcasm in the second sentence. She hears herself and makes a small mouth-movement at her own armor — not quite a grimace, a small private acknowledgement."

    z "I know you are not going to take it. I knew you were not going to take it when I started."

    athought "That is the sentence."

    athought "That is the sentence and I am not going to step on it by answering it too fast."

    "He does not answer it too fast."

    "He goes around the bench."

    "He walks the narrow gap between the bench and the wall, past the forge-side lamp, and comes up on her side. He stops beside her — not in front of her, not facing her, at her shoulder on the work side. From here, the bench is the same bench but the angle on the objects is her angle. He is looking at the papers the way she has been looking at them for three weeks."

    "She does not turn to him. She keeps her eyes on the bench."

    z "There it is."

    "The sarcasm is gone from the two words."

    z "That is the move I was waiting for."

    a "What move."

    z "The move to my side of the bench. I did not know I was waiting for it until you made it. I have been standing on this side of the bench alone for three weeks and I have been telling myself the aloneness is the cost of the work. The aloneness was the cost of the work. And I was going to be fine with it, because the work was the point, and the work required me to be alone with it, and fine is what I have been since I was fifteen."

    z "Then you walked around the bench and my throat did a thing I was not expecting."

    a "Zira."

    z "Don't."

    a "What did your throat do."

    "She laughs a small laugh. The laugh is one note and it does not have much voice behind it, but it is a laugh."

    z "It closed about a quarter of the way. That is the clinical description. The non-clinical description is that I have been building a door for someone I love and pretending to myself that building the door was the love, and then you walked around the bench and I realized the love was bigger than the door and the door was not going to hold all of it."

    "She says the word love the way she says ordinary workshop nouns. Pen. Wax. Love. She has always done this. It is the Ashmarket in her voice — the refusal to let a big word strut."

    "He does not say it back."

    "Not because he does not feel it. Because saying it back in this moment would be the wrong instrument for the sentence she just handed him. The sentence she handed him does not want an echo. It wants a witness."

    a "I see it."

    z "Good."

    # ========== PHASE 5 — THE GIFT IS A GRIEF ==========

    "A long quiet."

    "She is looking at the chain map. Her right hand — the pen hand — is at her side again, but her left hand has come up to rest on the bench, flat, near the edge of the map. Not on the map. Near it."

    athought "She built this knowing I would not take it."

    athought "She built this because she needed the door to exist."

    athought "The gift is not the plan. The gift is the fact that she did the work."

    athought "And the grief is also the fact that she did the work, because doing the work was the only way she could love me through the thing that is happening to me, and she knows the door is not going to open, and she built it anyway, and the building was the love."

    athought "I cannot take the papers because taking the papers would be the ending Zira and I are both refusing to write. But I also cannot refuse the work she did. The work is not the papers. The work is the three weeks."

    athought "I have to hold the three weeks without holding the papers."

    "He speaks slowly, because he is finding the sentence as he says it."

    a "You built this in the only way you know how to love me through what I am in the middle of."

    z "Yes."

    a "And I am not going to take it."

    z "I know."

    a "And you built it anyway."

    z "I needed to know the door existed. Even if you never open it."

    "The sentence is quiet. She is not performing the sentence. The sentence came out the way her pen draws a line — one continuous motion, no re-inking."

    "He takes a breath."

    athought "Write that down. Not on paper. In the part of my head Marcus cannot read. 'I needed to know the door existed. Even if you never open it.' That is a sentence I am going to carry the rest of my life. That is the kind of sentence that sits next to 'necessary is not worth it' and 'the rule is for the living' and 'I am not a neutral observer anymore.' These are the sentences the women in this war are giving me and I am going to keep every one of them."

    a "Zira."

    z "Don't say thank you. It is not a thank-you situation."

    a "I was not going to say thank you."

    z "What were you going to say."

    a "I was going to say — this is a gift and it is also a grief. Both. Not one and then the other. Both at the same time. I do not know how to hold it other than to stand here with you and not lie about either half."

    "She is quiet for three beats."

    z "That will do."

    # ========== PHASE 6 — ONE DOOR WITH MY NAME ==========

    "She does not look away from the bench yet. She has not looked directly at him in two minutes. The not-looking is not avoidance; the not-looking is how she is keeping her voice steady."

    z "Ask me one more question."

    a "Tell me the question."

    z "Ask me if I built one for myself."

    athought "Oh."

    a "Did you."

    z "No."

    "She finally looks at him. Her face is not the workshop face. Her face is the face from the one quiet conversation they had in the Ghostline alcove at the end of Act II and have not had again since."

    z "I did not build an exit for me, Aeron. I was building this for three weeks and it never once occurred to me to build a second chain with my own papers in it. There is one door in this plan. The door has your name on it. I am not in the chain. I am the woman at the first stop who hands you the packet and goes back to the workshop and rebanks the forge."

    z "And I am telling you that because I do not want you walking out of this room thinking I was building a door for both of us and decided to give you mine. That is a different story. That is not this story. I was building a door for you and I did not even notice that I was not in the plan until I drafted the chain map yesterday and realized the map stopped being a plural two stops in."

    z "That is the part I wanted you to hear out loud. Not because I am asking you to fix it. You cannot fix it. I am not sure I want it fixed. I am telling you because the scene would be a lie if I did not."

    "He does not move."

    "He does not move because moving would force the scene to be about his move, and the scene is not about his move. The scene is about her sentence."

    athought "She did not build one for herself. She did not build one for herself because she has not believed in a door with her name on it since she was fifteen. And the thing the Ashmarket did to her at fifteen is the thing she has never told me directly, and the thing that has been hiding under every 'fine' she has ever said to me, and the reason 'fine' is the word she lets do the most work in her whole vocabulary."

    athought "She is showing me the shape of the thing right now. Not the thing itself. The shape."

    athought "I am going to look at the shape. I am not going to ask her to hand me the thing."

    a "Zira."

    z "I know."

    a "I am not going to fix it."

    z "I know."

    a "I am also not going to pretend I did not hear it."

    z "I know. That is all I am asking."

    "A beat."

    a "The next time you are in the workshop drafting a chain map, I want you to leave two spaces for names."

    z "Aeron."

    a "I am not saying put my name in one and yours in the other. I am saying leave the spaces. They do not have to be filled. They have to exist on the page."

    "She looks at him for a long moment."

    z "That is a sentence I was not prepared for."

    a "I was not prepared for it either. It arrived the way your sentence about the door arrived. I did not know I had it until it was out."

    z "I am going to think about it."

    a "That is all I am asking."

    # ========== PHASE 7 — THE FOLD ==========

    "She looks down at the bench."

    "She reaches for the three sheets of identity papers. She picks them up — not roughly, not reverently, with the hands of a woman who has handled forgery paper enough times to know exactly how it wants to be held."

    "She folds them along the creases she left in them earlier. The creases remember. The papers fold clean."

    "She wraps the folded papers with the chain map. She takes the oilskin wrap and nests it against the papers. She takes the folded letter and places it on top of the stack, not inside it — the letter rides on top because the letter is the thing that gets handed over first at the fourth stop and Zira has thought about this."

    "She picks up the whole stack in one hand."

    "She opens the small drawer built into the left side of the bench — the drawer she keeps her finished work in, the drawer that in any other forger's workshop would be locked at all times and in Zira's workshop is locked only when she is not in the building."

    "She places the stack in the drawer."

    "She closes the drawer."

    "She does not lock it."

    "Her hand rests on the drawer handle for a second after the drawer is closed. Not pushing. Not pulling. Just present on the handle — the same kind of present that Tessa's flat palm on the board was, the day Aeron watched her do that and did not know yet that he was going to see the gesture twice in the same chapter."

    "Her hand comes off the handle."

    z "The drawer stays unlocked."

    z "Not because I think you are going to change your mind about taking the papers. I do not think you are going to change your mind. I think the papers are going to live in that drawer for the rest of this chapter and probably the rest of this war, and I think that is the correct home for them."

    z "The drawer is unlocked because the door is not going to be a secret from you. You know where it is. You know how to open it. I am not going to pretend the building was a decorative exercise. I built a working door."

    z "And the working door has an unlocked handle on the inside."

    z "That is the last thing I am going to say about it for the rest of tonight."

    athought "She said 'tonight.' She left the rest of the nights open. She is telling me we may come back to this and she is also telling me not now. Both things at the same time. In one word."

    # ========== PHASE 8 — THE CLOSE ==========

    "They stand at the bench for a count of twenty. Neither of them speaks."

    "Aeron does not touch her and she does not touch him. The scene is not a scene for touching. Touching would be the wrong instrument. They are standing on the same side of a bench where one of them has been alone for three weeks and the being-on-the-same-side is the gesture the scene is asking them to make."

    "Eventually Zira moves."

    "She goes to the banked forge in the corner. She picks up the small iron hook she uses to open the forge door. She opens the door a finger-width — just enough to let the banked heat out into the room for another hour — and closes it again. The motion is practiced and unnecessary. She is giving her hands something to do so that her hands do not do something else."

    "Aeron watches her do it and does not comment."

    "When she comes back to the bench, she picks up the pen she was using earlier and puts it in the pen tray properly, which means she has decided the work session is over. Zira does not put pens in the tray properly unless she has decided she is done."

    a "Are you going to sleep."

    z "I am going to sit in the workshop for another hour and drink the tea I have not had since this afternoon and then I am going to sleep."

    a "Okay."

    z "Do you want to sit for the hour."

    a "Yes."

    "She gestures at the second stool, the one she keeps near the forge side of the bench for the rare occasions when she has a visitor who will not leave."

    "He sits."

    "She pours two cups of the tea from the kettle that has been on the small warming stone beside the forge. The tea is not ceremonial tea. The tea is the thing Zira drinks when she has been at the workshop too long to make a second pot from scratch."

    "She hands him one cup. She takes the other."

    "They sit."

    "Neither of them looks at the drawer."

    "Both of them are aware of the drawer."

    "The drawer is not going away. The drawer is the new thing in the workshop. The drawer has a room in it now, and the room has a door, and the door is unlocked, and Zira and Aeron are sitting in the outer room of a relationship that has grown a door they are both going to live around for the rest of the war."

    "That is the scene."

    "Aeron drinks the tea."

    athought "I am going to carry this the way I carry Tessa's rule and Noelle's hands going still and Lyra's Band unbuckled and Selene's necessary-is-not-worth-it. I am going to carry it as a sentence. 'I needed to know the door existed. Even if you never open it.'"

    athought "That is Zira's sentence. I am going to hold it in the part of my head Marcus cannot read."

    "The forge ticks as it cools."

    "Fade."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=2)
    $ canon_set("zira.exit_plan.built", True)
    $ canon_set("zira.exit_plan.drawer_unlocked", True)
    $ canon_set("zira.no_exit_for_herself", True)
    $ flag("aeron_saw_the_door", True)
    $ flag("aeron_refused_the_door", True)
    $ npc_remember("Zira", "door_existed_even_if_never_opened", tone="named_aloud")
    $ npc_remember("Zira", "did_not_build_one_for_herself", tone="shape_shown")
    $ npc_remember("Aeron", "asked_for_two_spaces_on_the_next_map", tone="witnessed_without_fixing")
    $ npc_remember("Aeron", "walked_around_the_bench", tone="physical_gesture")
    $ tp_seed("a4.zira.door_exists")
    $ tp_seed("a4.zira.two_spaces")
    $ metric("zira_exit_plan_days_building", 21)
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s08_zira_exit_plan_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Late in the same day as a4_s03 and a4_s07. Aeron's day has been
#     ending for four hours and refusing to end. He goes looking for
#     Zira because Zira is the person he looks for when a day refuses
#     to end. He finds her in the workshop.
# cann.what_happened:
#   - Aeron enters Zira's workshop for the first time in nine days.
#     Zira is bent over the bench finishing a line on a forged document.
#     She hears him, finishes the line, sets the pen down, straightens,
#     turns. She does not move to cover the bench or the objects on it.
#   - On the bench: three sheets of forged identity papers (three
#     different aliases in three different hands — Zira is trained), a
#     hand-drawn chain map of four safehouses running from the secondary
#     base through the western passes and then north to an unnamed
#     fourth stop marked with the Old Tongue character for "threshold,"
#     an oilskin wrap containing Ashmarket currency and a Ghostline
#     quiet-route cipher key and a non-Phoenix knife, and a wax-sealed
#     letter with no address.
#   - Aeron asks how long. Zira says three weeks — she started the night
#     he came back from the Obsidian Bridge. Aeron names the objects.
#     Zira names the knife as Ashmarket-kit with no Phoenix fingerprints.
#     Zira names the fourth stop as someone she knew before the
#     Ashmarket who owes her two favors of terminal weight. Zira tells
#     Aeron not to open the letter and gives the reason: what the letter
#     says is not something Zira wants him carrying in his head while he
#     is still in Solveil.
#   - Aeron tells her he is not going to take the plan. Zira's sardonic
#     armor comes up once, briefly, then she sheds it and tells him she
#     knew he was not going to take it when she started.
#   - Aeron walks around the bench to stand on her side. Zira names this
#     as the move she was waiting for and did not know she was waiting
#     for. She says her throat closed a quarter of the way. She says she
#     had been telling herself the aloneness of the work was the cost of
#     the work and the aloneness of the work has been what fine means
#     since she was fifteen. She says the word love flat, the Ashmarket
#     way.
#   - Aeron does not say it back. He witnesses it instead. He names
#     that this is a gift and a grief simultaneously and that he does
#     not know how to hold it other than to stand with her and not lie
#     about either half. Zira says "that will do."
#   - Zira asks Aeron to ask her one more question. The question is
#     whether she built one for herself. The answer is no. She did not
#     build a second chain with her own papers in it. There is one door
#     in the plan and it has his name on it. She is the woman at the
#     first stop who hands him the packet and goes back to the workshop
#     and rebanks the forge. She tells him this not because she is
#     asking him to fix it but because the scene would be a lie if she
#     did not say it out loud.
#   - Aeron asks her, the next time she is drafting a chain map, to
#     leave two spaces for names. Not to put names in them — just leave
#     the spaces. Zira says she was not prepared for the sentence. She
#     will think about it.
#   - Zira folds the identity papers, wraps them with the chain map and
#     oilskin packet, places the letter on top of the stack, puts the
#     whole stack in the small bench drawer, closes the drawer, and
#     leaves it unlocked. She names the drawer-stays-unlocked as
#     deliberate — the door is not going to be a secret from him. The
#     building was a working door. The working door has an unlocked
#     handle on the inside. She says that is the last thing she will
#     say about it for the rest of tonight.
#   - They sit at the bench for an hour. Zira hands Aeron a cup of tea
#     from the warming stone. Neither of them looks at the drawer.
#     Both of them are aware of the drawer. Scene closes on the forge
#     ticking as it cools.
# cann.aeron_state:
#   - Receives the exit plan as a gift and a grief simultaneously and
#     does not try to collapse the two. Walks around the bench to stand
#     on Zira's side of the work — the physical gesture of the scene.
#     Does not take the papers. Does not ask Zira to close the door.
#     Asks for two spaces on the next map. Adds Zira's sentence ("I
#     needed to know the door existed") to his running ledger of the
#     Act IV women's sentences.
# cann.zira_state:
#   - First sustained vulnerability scene with Aeron in Act 4. Names
#     the exit plan aloud. Names "love" without strut. Cracks the
#     armor twice — once at "there it is" when Aeron moves to her
#     side, once at "I did not build one for myself." Does not
#     apologize for either crack.
#   - Shows Aeron the shape of the Ashmarket wound without handing him
#     the wound itself. The "fine since I was fifteen" line is the
#     shape-without-thing.
#   - Leaves the drawer unlocked as a deliberate refusal of secret-
#     keeping inside the relationship. The plan is not a secret. The
#     plan is an acknowledged room.
# cann.path_tracking: EMP
# cann.thematic_flags:
#   - Love as infrastructure. Zira's love for Aeron in Act IV is
#     physical labor on a document he will not use. The labor is the
#     love; the papers are the artifact.
#   - The door that exists because someone needed it to exist, not
#     because it will be used. The refusal to collapse "useful" into
#     "real."
#   - Gift as grief. The two registers hold at the same time; Aeron
#     explicitly refuses to pick one.
#   - The unlocked drawer as anti-secrecy. In a war of coded messages
#     and forged identities, the drawer that stays unlocked is the
#     room's ethic. Parallel to Tessa's board being visible in the
#     main medical area, parallel to Noelle leaving her projections
#     running in a4_s03.
#   - Walking around the bench. Physical gesture of joining a person
#     on her side of a work she has been alone with. First explicit
#     Aeron-Zira intimacy physicalization in Act 4 that is not erotic.
#   - Zira's Ashmarket shape. Scene refuses to open the wound
#     directly. Shows the shape only. The refusal is the intimacy —
#     the scene treats Zira's unspoken fifteen-year-old self as a room
#     in the workshop the lamp does not light.
#   - The shape-without-thing method mirrors Tessa's flat-palm
#     benediction in a4_s06 and Noelle's "on whose record" in a4_s03.
#     Act IV is rehearsing a grammar of private gestures the
#     characters refuse to translate for anyone, including Aeron.
# cann.character_moments:
#   - Zira: finishing the line before turning. Letting the bench be
#     seen without covering it. Saying "love" flat. "There it is."
#     Naming the not-building-one-for-herself without being asked.
#     Folding the papers and placing them in the unlocked drawer.
#     "The drawer is unlocked because the door is not going to be a
#     secret from you."
#   - Aeron: walking around the bench. Not saying "I love you" back —
#     witnessing instead. Asking for two spaces on the next map
#     without asking for the spaces to be filled. Sitting for the
#     hour with tea. The refusal to touch during the scene — the
#     understanding that touch would be the wrong instrument for the
#     sentences being exchanged.
# cann.callbacks:
#   - a1_s26_obsidian_bridge: the night Zira names as the start of the
#     three-week build window. The Obsidian Bridge is canonically the
#     moment Zira's exit plan begins to exist in her head. Future
#     Zira scenes can reference the bridge as origin.
#   - a3 ghostline work: Zira's forgery hands are the same hands that
#     have been doing Ghostline work. The scene treats the dual use
#     of the hands as a single fact.
#   - a4_s03_marcus_adapts_emp: "I am not a neutral observer anymore"
#     echoes structurally here as "I did not build one for myself."
#     Both women in Act IV are naming a position they did not
#     intend to occupy and refusing to pretend they are still in the
#     role they started in.
#   - a4_s05_delegation_test_emp: "necessary is not worth it" is
#     running in Aeron's head as he stands at the bench. Zira's
#     sentence enters the same internal ledger.
#   - a4_s06_tessa_counts_different_emp: Tessa's flat palm on the
#     dead column and Zira's hand on the drawer handle are matched
#     gestures. Aeron explicitly recognizes the parallel.
# cann.block_status: drafted
# cann.requires_followup:
#   - tp_seed a4.zira.door_exists — the drawer is canon. Any future
#     Act IV or Act V scene that revisits Zira's workshop must
#     acknowledge the drawer. The drawer may be opened (Aeron takes
#     the papers), replaced (a second chain drafted with two names),
#     or left exactly as it is. All three options are live.
#   - tp_seed a4.zira.two_spaces — Aeron's request for two spaces on
#     the next map is a thread Zira said she would think about. A
#     later Zira scene may return with a drafted map that honors
#     the request, refuses it, or reshapes it into something neither
#     character anticipated.
#   - Zira's "fine since I was fifteen" is the first Act 4 reference
#     to the Ashmarket origin wound. The scene refuses to open it
#     and that refusal is now canon. Any future Zira backstory beat
#     that touches fifteen must honor the refusal this scene
#     established — the shape is shown, the thing is not.
#   - The woman at the fourth stop is an unnamed plant. She may
#     become an actual character in a later act or remain a latent
#     offscreen node. Either is supportable from this scene.
#   - The non-Phoenix knife is a plant. It may be used or left in
#     the drawer. Either is supportable.
#   - The wax-sealed letter is a plant Aeron has promised not to
#     open. If the letter is ever opened, the opening must be a
#     breach of promise with full narrative weight. The letter is
#     not to be used casually.
