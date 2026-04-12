# =======================================================
# ACT 4 - Scene 12: Held, Not Fixed (Empathy Path)
# File: a4_s12_held_not_fixed_emp.rpy
# Type: TESSA DEEPENING BEAT — continuation of s05a + s06
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s12_held_not_fixed_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s12_held_not_fixed_emp:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("tessa", to_stage=3, source="a4_s12_held_not_fixed_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm in the corridor — handheld at chest height, following Aeron as he
    #         walks away from the ops room. Tessa enters frame from a side door. The
    #         camera does not turn to her; it catches her in the edge of the frame and
    #         then settles to a two-shot when she falls into step. Cut to 35mm for the
    #         walk to the medbay — lower, wider, the two of them in silhouette against
    #         the corridor wash. In the medbay: 85mm, tight, shoulder-to-shoulder
    #         blocking. Her hand finds his sternum. The camera holds on the hand longer
    #         than it holds on either face. The faces come after — a quiet over-shoulder
    #         exchange, the one line each, and then the hand still there.
    # LIGHTING: The corridor at oh-two-forty: low, cold, the work lights in their
    #           overnight setting. The medbay: her one clinic lamp, same one she uses
    #           for close work. Warm. Soft. The equipment off. The instrument tray
    #           empty. The room's function suspended for the scene.
    # SFX: Corridor — the hum of the base at its quietest, ventilation cycles, the
    #      occasional boot of a guard walking a different floor. Medbay — the clinic's
    #      residual quiet, the small sound of a clean glove coming out of a dispenser
    #      (she will not wear it), the click of a lamp, her breath, his breath. When
    #      her palm settles on his sternum: nothing. No music. No underscore. Silence
    #      as the load-bearing element.
    # FACE: Tessa — the clinical mask half-off. Not absent, but no longer doing the
    #        work of being the room's medic. Something underneath that has been forming
    #        across the Act II and Act III interludes and is, tonight, deciding to be
    #        visible to exactly one person in the building. Aeron — still carrying the
    #        list from s11b. Still carrying Lyra's Seren from s11a. Still carrying the
    #        mercy call from s11. Three layers deep. When her hand finds his sternum,
    #        the bottom layer comes up to meet it.
    # BLOCKING: Corridor encounter outside the ops room. Tessa is on her way somewhere
    #           (she is not specified — she is on a night rotation that lets her be
    #           exactly here). She stops, lets him walk into her field of attention,
    #           turns with him. She walks him to the medbay. In the medbay she does
    #           not put him on the exam table. She sits him on the stool she uses for
    #           close conversations and she stands in front of him — his eye level to
    #           her collarbone — and her hand finds his sternum. Not his heart. His
    #           sternum, the bone, the center line. The flat of her hand, fingers
    #           spread, like a medic checking rise-and-fall and like a woman checking
    #           a center.

    # ========= VOICE BASELINE =========
    # EMP cadence. Tessa's diction is her clinical register slowly unreeling. Her
    # internal thoughts (tthought) are where the shift happens — her spoken lines stay
    # measured, her thinking stops pretending. She says the load-bearing line exactly
    # once. Aeron's reply is one sentence. The scene names what is happening between
    # them without resolving it. No kiss. No escalation. One permission, spoken aloud
    # by her interior and not by her mouth.

    # scene bg_corridor_ops_overnight_emp with dissolve
    # play ambient "sfx/ambient/corridor_overnight_low.ogg" fadein 2.5

    # ========== PHASE 1 — THE CORRIDOR ==========

    "Aeron leaves the ops room at oh-two-forty-three."

    "Selene is still at the cipher table. She did not stand when he stood. She did not say anything when he stood. She watched him — or did not watch him, because the angle she had chosen for her chair was the one that did not face him — and she let him go. The coffee cup is on her side of the table now because she drank the last of it, and the drinking was a thing she did instead of a thing she said."

    "He walks."

    "The corridor outside the ops room is long and cold and has three sealed doors between the ops room and the junction where the medbay wing branches off. He is not going to the medbay. He is going back to his quarters. He is going back to his quarters because his body has decided it is going to attempt sleep for the second time tonight, and if the attempt fails the way the first attempt failed, he will at least have tried."

    athought "I am moving because moving is what I have left. The list is closed. The cipher is in Selene's hand whether she is holding it or not. Lyra is at her altar with three candles and a word. I have said four clusters of names out loud and I cannot say the fifth and my mother is two sayings short of being kept by a rule that was never going to work on her anyway."

    athought "I am going to my quarters because that is the physical place I have been assigned to be in when I am not here."

    "He does not reach his quarters."

    # ========== PHASE 2 — TESSA ENTERS FRAME ==========

    "The medbay wing side door — the one Tessa uses when she is on night rotation and moving between the clinic and the supply cache — opens as he passes it."

    "She does not step out into his path."

    "She steps out into her own corridor and stops when she sees him. She does not say his name. She does not call out. She stands in the doorway with her clinic datapad under her arm and she lets the moment of seeing him be a moment of seeing him before it becomes anything else."

    tthought "He came out of the ops room. I was on my way to the supply cache and I heard the ops room door seal six seconds ago and I already knew who it was. I know his walk. I know his walk the way I know which of my patients take the corridor with a limp even after the limp has visibly healed, because the body remembers limps that the mind has retired."

    tthought "His walk tonight is the walk of a man who is going to his quarters and is going to fail to sleep and knows he is going to fail. I have seen that walk four times in the past three weeks."

    tthought "I am going to stop pretending I am on my way to the supply cache."

    "She steps out. Two steps. Not toward him — perpendicular to his line of travel, the way a person puts themselves into the path of a stream without damming it."

    "He sees her."

    "He stops."

    a "Tessa."

    t "Where are you going."

    "It is not quite a question. It is phrased as a question because Tessa does not tell people things when she can ask them. The asking is the form. The content is that she already knows."

    a "Quarters."

    t "To sleep."

    a "Theoretically."

    "A beat."

    t "Come with me."

    a "Tessa."

    t "Come with me. I am not taking you for sleep. I am not taking you to bandage anything. I am taking you to the medbay and you will understand why when you get there. It is not a long walk."

    "She turns. Not to face him — she has turned one-quarter, so her shoulder is ahead of her hip in the direction of the medbay wing. The turning is an invitation that does not wait for the acceptance. She has calibrated this, he understands, exactly — if she waits, he will say no. If she does not wait, he will follow, because the alternative is standing in the corridor alone at oh-two-forty-four and he has been alone for most of the last two hours and the idea of standing alone in a corridor for even one more minute is the thing his body is least willing to do tonight."

    "He follows her."

    athought "She did not ask me what I have been doing. She did not ask me where I was in the ops room. She did not ask me about the mercy call, which she knows about, because Tessa knows about every call that produces a name on her board. She did not ask me about Lyra, which she may or may not know about, depending on whether the chapel candles have counted as information in the base's informal surveillance tonight."

    athought "She just told me to come with her."

    athought "That is different from the way she has talked to me for the last three weeks."

    # ========== PHASE 3 — THE WALK TO MEDBAY ==========

    "The walk is four doors. Four sealed corridor sections and then the medbay threshold."

    "She does not speak on the walk. He does not speak either. She is one half-step ahead of him — not commanding the pace, indicating it. Her pace is a doctor's pace: the pace of a person who has learned that patients who are about to resist treatment walk slightly slower than people who are choosing it, and her pace is adjusted to keep him inside the envelope of choosing without letting him notice the envelope exists."

    tthought "He is keeping up. He is keeping up without effort, which means his body is willing to walk toward whatever I am walking him toward. That is more consent than I was expecting before I opened my door. That is good information."

    tthought "I have been doing this for three weeks and I have been doing it clinically. I have been telling myself I am doing it clinically. Tonight I am going to stop telling myself that because I saw him leave the ops room and my first thought was not 'that man needs a medical assessment' and it was not 'that man is going to crash in the next six hours if nobody intervenes' — my first thought was the shape of his shoulders and the word I had for the shape was not a medical word."

    tthought "The word was {i}held.{/i}"

    tthought "I thought: that man needs to be held."

    tthought "I have been telling myself for three weeks that my care for him was the same care I give to the base. It is not. It stopped being that care somewhere in the Act III aftermath and I have not been honest with myself about when. Tonight is the night I stop being not-honest. I am not going to tell him I stopped being not-honest. I am going to let my hands tell him and I am going to see if his hands can hear it."

    "The medbay door."

    "She touches the panel. It slides."

    # scene bg_medbay_overnight_lamp_emp with dissolve

    # ========== PHASE 4 — THE MEDBAY ==========

    "The medbay at oh-two-forty-eight is the quietest room in the base."

    "She has set it up that way on purpose — the overnight medbay is not supposed to be the busiest room, and in the weeks since the secondary base became primary she has trained the staff to defer non-urgent intake until morning unless a patient is actively deteriorating. The exam tables are empty. The instrument trays are covered with their sterile cloths. The one clinic lamp at her close-work station is off."

    "She turns it on."

    "It throws warm light over a two-meter radius. The rest of the medbay goes into soft shadow. The room contracts to the space the lamp defines and the space is exactly large enough for a stool, a woman standing, and a man who will sit on the stool."

    "She pats the stool once. Just once."

    t "Here."

    "He sits."

    "The stool is at a height that puts his eye level at her collarbone when she stands in front of him. This is not the exam-table height. This is the close-work height — the height at which she sits to suture, to set a bone, to speak to a frightened patient at eye level without standing over them. Tonight she is standing, and the height differential is reversed, and he looks up at her the way a patient looks up at a doctor who is about to explain something they have been avoiding explaining."

    "She does not explain."

    t "I am not going to treat you."

    a "I know."

    t "Do you."

    a "I think so."

    t "Good. I am going to tell you anyway, because I do not want the scene to be a surprise and I do not want you to misread it when it starts."

    "She sets the clinic datapad down on the tray. It is the first thing she has put down since she picked it up on her way to the supply cache. She sets it face-down. The face-down is an accounting gesture — the instrument is off, the instrument is retired for the duration of the scene, no charting will happen here."

    t "I am not going to ask you what happened in the ops room. I am not going to ask you what happened with Lyra. I am not going to ask you about the mercy call. I am not going to take your pulse. I am not going to ask you when you last ate. I am not going to do the thing I have been doing for three weeks where I make the whole encounter a medical encounter so that neither of us has to call it anything else."

    a "Tessa—"

    t "Let me finish."

    "He lets her finish. Tonight is the second time in four hours a woman has asked him to let her finish a sentence. He is batting one thousand on the letting."

    t "I am going to tell you one thing and then I am going to put my hand on you and then you are going to tell me one thing back. That is the whole scene. It is not a long scene. It does not have more parts than that."

    a "Okay."

    t "The one thing is this."

    "She does not sit down. She stays standing. She breathes once — a measured breath, the one she uses before a difficult procedure — and she says the line."

    t "I cannot fix this."

    "A beat."

    t "I am not going to try."

    "Another beat. The lamp hums very softly. The medbay around them is the room she built. The words she is saying are not the words the room was built for."

    t "But you are held."

    t "That is not nothing."

    # ========== PHASE 5 — THE HAND ==========

    "She lifts her right hand."

    "It does not go to his face. It does not go to his hands. It does not go to his shoulder the way Lyra's hand went to his shoulder an hour and twenty minutes ago, and the difference in trajectory is an intentional difference — Tessa has thought about where her hand goes, and the place her hand goes is a place Lyra's hand did not go tonight, because Tessa is not Lyra and Tessa does not want her hand to be mistaken for Lyra's hand."

    "Her hand finds his sternum."

    "The flat of the palm. Fingers spread. Not pressing — laid. The weight of her hand is the weight of her hand. She is not checking his heart rate — her palm is over the bone, not over the artery, and the bone is where a medic puts a hand when the medic is looking for rise-and-fall. She is looking for rise-and-fall."

    "She is also not looking for rise-and-fall."

    "She is putting her palm on a man's chest in the specific place where the palm becomes a hand of a woman and not a hand of a medic, and she is doing it with the knowledge that the placement is readable as both things and that the readability is the entire point."

    athought "Her palm is warm."

    athought "Her palm is warm and it is on the bone, not on the heart, which is what a medic does, and it is also not doing what a medic does, because the stillness of it is a stillness I have not felt from her hand in three weeks of the way she has been checking in on me."

    menu:
        athought "Her hand on my sternum. Not diagnostic. Not clinical. Something I don't have a file for."

        "Being held by someone who knows how I'm broken — that's everything.":
            $ rel_bump("Tessa", affection=1, trust=1)
            athought "I did not say it out loud. But the way my breathing changed under her palm said it for me."
        "I'm not asking you to fix this. Just stay.":
            $ rel_bump("Tessa", trust=1)
            athought "The asking and the staying are the same sentence tonight."
        "This is the only kind of healing that works.":
            $ rel_bump("Tessa", affection=1)
            athought "The kind that doesn't pretend the breaking goes away."

    tthought "His sternum is warm under my hand. His heart is going faster than I would expect given the way his shoulders read. That is not a diagnostic — I am not charting this. That is a fact I am noticing because the fact is close to the surface of my attention. He is wired tight and he is not going to come down by morning and I am not going to fix the wired-tight."

    tthought "The thing I can do is be here with my hand on his center line. I cannot do the thing I have been telling myself I do for people I care about, which is solve. I am a doctor. I solve. I set bones. I close wounds. I manage protocols. I cannot set this and I cannot close this and there is no protocol because the protocol would require a version of him that was not responsible for the list he was carrying, and the list is not his fault and it is his responsibility and those two things can both be true and neither of them is a thing I can discharge."

    tthought "So I am not going to try."

    tthought "The trying would be a lie I tell him in the language of my profession and the lie would be for me. It would be for me because if I tried, I could pretend that the failure of the trying was a medical failure and not a personal one. I am not going to hide behind my profession tonight."

    tthought "I am going to stand here with my hand on his sternum and I am going to be a woman who has chosen to put her hand on a man's chest because the man is being held in no other way that would hold him."

    tthought "I told him he is held. The held is my hand. My hand is the only held in the room."

    tthought "I am going to let that be the scene."

    # ========== PHASE 6 — THE LINE ==========

    "His hand — not the one on the stool edge, the other one, the one that has been resting on his thigh — comes up. Slowly."

    "It does not take hers."

    "It rests on top of hers."

    "His palm on the back of her hand. Not pressing her hand into his chest — laying his hand over hers the way her hand is laying over his sternum. Mirroring. The placement is the same stillness she used. He is paying her the compliment of using her own grammar."

    "She does not move her hand. Neither does he."

    "The silence in the medbay has a weight now that it did not have thirty seconds ago. The lamp hum is still there. The ventilation tick is still there. The generator is still very far. But between the two of them there is a silence that is not the medbay's silence — it is a silence the two of them are making with their hands, and the silence is doing the work that language would normally do."

    "Then he says the line."

    a "You're right."

    "A beat."

    a "It's not nothing."

    "He says it plainly. No qualifier. The way Lyra said her plain sentences at the desk in s04 and at the altar in s11a. He has been learning the rhythm of plain sentences from two teachers tonight and now he is speaking one himself, to a third."

    tthought "He did not say 'thank you.' He did not say 'I know.' He did not say 'I do not know what to do with this.' He said the exact sentence I was hoping he would say and the sentence he said is the receipt. He received it. The scene has a receipt."

    tthought "I am going to let my hand stay here a little longer."

    tthought "I am going to let my hand stay here until the rise-and-fall under my palm slows the half-percent it needs to slow to be survivable for the rest of the night."

    tthought "That is the reason I can tell myself, in my own interior, for why my hand is staying. The other reason — the reason I was going to pretend for the rest of the scene was not real — is that I do not want to take my hand off his chest, because the taking it off is going to be the end of the scene and I am not ready for the end of the scene."

    tthought "I am choosing not to be ready."

    tthought "That is an attachment word. That is a word I have been not-saying in my interior for three weeks. Tonight I am saying it in my interior exactly once and I am not going to use it again until another scene and I am going to let the single use be the permission I give myself to be in this scene as a woman and not as the base's doctor."

    # ========== PHASE 7 — THE NAMING WITHOUT NAMING ==========

    "She does not remove her hand. He does not remove his."

    "The silence goes another breath. Another. Another. Neither of them is counting. If either of them were counting, they would both be losing count."

    t "I have been telling myself for three weeks that what I am doing for you is clinical."

    "She says it to his sternum, not to his face. Her eyes have stayed on her own hand, which is still on his chest, under his hand, in the warm pool of the lamp."

    t "It has not been clinical for some time."

    t "I am not going to tell you when it stopped being clinical because I do not want to pretend I have the date. It is enough that it stopped. It is also enough that tonight is the first night I am willing to say, in this room, that it is not clinical anymore."

    t "That is the whole thing I am willing to say tonight."

    t "I am not going to ask you for anything. I am not proposing a conversation. I am not putting a pin in your calendar. I am not asking what you want to do with the information."

    t "I am giving it to you because I said I would not hide behind my profession and 'I am not going to tell you what has been happening in me' would be hiding."

    "A small beat."

    t "I have told you. We are even."

    athought "We are not even."

    athought "We are not even because she has just handed me a piece of her interior without asking for a matched piece and I am going to owe her the matched piece and she knows it and she said 'we are even' because if she admitted we are not even, she would be asking, and she is not going to ask."

    athought "That is the part I need to file. She is not asking. The not-asking is what she is giving me. She is telling me her interior has moved and is telling me she is not going to demand that mine move in response and the not-demanding is the thing that makes the information safe to receive."

    athought "I think I have received information like this exactly once tonight, from Lyra, in a different room, with a different hand on a different part of me. I do not know what to do with the pattern yet."

    athought "I am going to do what she said. I am going to not-fix. I am going to let the information sit."

    "He leaves his hand on hers."

    "He leaves his hand on hers for longer than he has left his hand on anything tonight that was not a datapad or a relay console or his own knee. The leaving is the reply."

    # ========== PHASE 8 — THE CLOSE ==========

    "Eventually — minutes, he does not know how many, she does not either — she moves her hand. Slowly. Not withdrawing. Lifting. She puts her hand on his shoulder next, briefly, the way a medic confirms a patient is still with her at the end of a procedure. Then she takes her hand away."

    "He lets his hand drop to his thigh. Not fast. The same pace she used."

    "She steps back. Only a half-step. Still inside the lamp's pool. Still inside the two-meter radius the medbay has contracted to for the duration of the scene."

    t "I am not going to walk you to your quarters."

    a "I know."

    t "You are going to walk there on your own because you can. You are going to sleep if you can and you are not going to if you cannot, and either of those is acceptable tonight. I am not going to chart it in the morning either way."

    a "Thank you, Tessa."

    t "Not the thanking I needed."

    "She says it lightly. There is something in her mouth that is almost the skeletal laugh Lyra did twice tonight. The almost-laugh is the medbay's version of that register and it is, he notices, the same register."

    athought "Both of them. In the same night. An almost-laugh from each of them. I have been in rooms with Tessa where she has cried and I have been in rooms with Tessa where she has shouted and I have never been in a room with Tessa where she was almost-laughing the way she just did. That is an expression I did not know she had."

    athought "She had it and she was keeping it in reserve."

    a "What was the thanking you needed."

    "She looks at him. Her face is back to close-work range — composed, focused, the warmth of her interior now behind the clinical mask but not sealed away. The mask has a door in it now and the door is the scene."

    t "The one you gave me. 'You're right. It's not nothing.'"

    t "That was the whole thanking. I already have it."

    a "Okay."

    t "Go sleep or don't sleep. I am going to the supply cache. I am going to the supply cache because I still need to go to the supply cache and the cache does not know what just happened in this room and I am going to pretend I am walking to it because that is the easiest way to leave this room."

    "She picks up her clinic datapad from the tray. She does not turn it back over. She tucks it under her arm the way she had it in the corridor."

    t "Aeron."

    "He looks up."

    t "I said you are held. I want you to hear it one more time before you leave the room, because I do not want you to have only heard it once. Once is fragile."

    t "You are held."

    a "I am held."

    "He says it back to her, not because she asked him to say it, but because the scene has arrived at the place where saying it is what a person does. He does not say it with conviction. He says it with obedience — the obedience of a man who has been given a sentence by a woman he trusts and who is willing to repeat the sentence in his own mouth because the repetition is a small thing and the small thing is the only accurate reply."

    t "Good."

    t "Now go."

    "He stands."

    "The stool is behind him. The lamp is still on. Her hand is not on him. His hand is not on her. The medbay around them has returned to being a medbay — the instrument trays under their cloths, the exam tables empty, the overnight low-power wash coming up in his peripheral vision the way it does when a room is about to be unoccupied."

    "He walks to the door."

    "At the door he stops. He turns — not his body, his head — just enough to see her."

    "She is standing under the lamp with the datapad under her arm and her right hand at her side, and the right hand is the hand that was on his sternum, and she is looking at the hand the way a person looks at an instrument that has just been used for a procedure that was not in the manual."

    athought "She is going to carry the shape of that hand for the rest of the night. I know because I am going to carry the shape of my hand on top of it for the rest of the night. The hands are going to be the thing we are both thinking about when we try to sleep and fail or try to sleep and succeed."

    athought "That is the scene."

    athought "That is the whole of the scene and I am leaving the room and the scene is not resolving into anything tonight because she said it was not going to and because I believe her."

    a "Goodnight, Tessa."

    t "Goodnight, Aeron."

    "He leaves."

    "The door seals behind him."

    # VISUAL: Hold on Tessa. She does not move for a long moment. Her right hand is still
    # the subject of the frame. She eventually lowers her hand to her side, picks up the
    # lamp's manual dial, dims it one notch — not off, one notch — and stands under the
    # dimmer light alone.

    tthought "I am going to the supply cache now because the supply cache is the place I told him I was going to. I am going to go and I am going to walk past the cache and I am going to come back here. I am going to come back because I have a patient list to check before morning and because if I do not come back now I will not come back at all tonight, and coming back now means I have chosen to come back, and choosing is different from retreating."

    tthought "I said it out loud. In my own interior I said the attachment word once. In the room I said 'it is not clinical anymore.' Those are two sentences I have not said before, in any order, in any interior, in three weeks."

    tthought "I said them to a man who had his hand on top of mine and who said 'you're right, it's not nothing' and who did not say anything else, which is exactly the right amount of anything else for tonight."

    tthought "I am going to sleep badly tonight."

    tthought "I am going to sleep badly tonight and I am going to be okay with sleeping badly, because the reason I am going to sleep badly is not the reason I have been sleeping badly for three weeks. The new reason is not a worse reason. The new reason is that I have stopped pretending, and the stopping of pretending always costs a night's sleep the first night."

    tthought "Tessa Marra. Clinician. Holder. Woman with a hand on a sternum and a decision in her throat."

    tthought "That is who I am tonight."

    tthought "I am going to see who I am tomorrow in the morning, when the lamp is off and the base is awake."

    "She dims the lamp one more notch. The medbay is in near-dark."

    "She leaves."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Tessa", trust=2, attraction=1)
    $ flag("tessa_held_not_fixed_spoken", True)
    $ flag("tessa_clinical_mask_dropped", True)
    $ flag("aeron_received_held_not_fixed", True)
    $ canon_set("tessa.care_is_attachment", True)
    $ canon_set("tessa.hand_on_sternum", True)
    $ npc_remember("Tessa", "said_not_clinical_anymore", tone="chosen_visibility")
    $ npc_remember("Aeron", "received_held_not_fixed", tone="plain_sentence_acknowledged")
    $ tp_seed("a4.tessa.held_not_fixed")
    $ nudge_poly(threshold=1)
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s12_held_not_fixed_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same night as a4_s11a (Lyra prayer) and a4_s11b (the KIA list). Immediately
#     after Aeron leaves the ops room and Selene's silent company. Oh-two-forty-three
#     to approximately oh-three-hundred. Corridor, then medbay.
# cann.what_happened:
#   - Aeron leaves the ops room intending to attempt sleep. Tessa steps out of the
#     medbay wing side door on her ostensible way to the supply cache. She stops
#     him in the corridor. She does not ask what happened — she tells him to come
#     with her. He follows.
#   - She walks him to the medbay at night. The medbay is empty. She sits him on
#     her close-work stool (not the exam table — the stool she uses for
#     eye-to-eye conversations) and stands in front of him under her clinic lamp.
#   - She explicitly names that she is NOT treating him. She enumerates what she
#     will not do (pulse, food history, charting, etc.) and explains that she
#     has been making every encounter with him a medical encounter for three
#     weeks so that neither of them has to call it anything else. Tonight she is
#     stopping.
#   - She delivers the load-bearing line: "I cannot fix this. I am not going to
#     try. But you are held. That is not nothing."
#   - She places her right hand on his sternum. Not his heart — his sternum, the
#     bone, the center line. Flat palm, fingers spread. The scene explicitly
#     frames the placement as medically legible (rise-and-fall check) and
#     non-medically legible (woman's hand on a man's center) simultaneously,
#     and the readability as both is the point.
#   - Aeron lifts his other hand (not the one on the stool edge) and lays it
#     over the back of hers — mirroring her grammar, not pulling.
#   - Aeron delivers the reply: "You're right. It's not nothing." Plain
#     sentence, no qualifier. The reply is the scene's receipt.
#   - Tessa then delivers the second load-bearing statement: "I have been
#     telling myself for three weeks that what I am doing for you is clinical.
#     It has not been clinical for some time." She does not ask Aeron for a
#     matched piece of interior. She explicitly names that she will not ask.
#     The not-asking is the gift.
#   - She says "We are even" as a formal closing of the exchange. Aeron's
#     interior clocks that they are not even and that the not-asking is what
#     makes the information safe to receive.
#   - Closing: Tessa tells him to go. He stands. At the door she makes him
#     say "I am held" aloud — not for conviction, but so the hearing is not
#     just once. He obeys. He says it back.
#   - She dims the lamp one notch and leaves the medbay herself. Her interior
#     monologue names the attachment word exactly once (the actual word is not
#     printed in dialogue; it is held as tthought's single use). She resolves
#     to sleep badly and to be okay with sleeping badly.
# cann.aeron_state:
#   - Arrives from the ops room carrying: the mercy call (s11), Lyra's Seren
#     (s11a), the full KIA list and the rule of three breaking on Liora (s11b),
#     and Selene's silent company at the cipher table.
#   - Three layers deep in grief work and already receiving from two women
#     tonight. This scene is the third woman, in a different register, holding
#     a different part of him.
#   - His reply ("You're right. It's not nothing.") is the plain sentence he
#     has been learning the grammar of tonight from Lyra. This is the first
#     time he speaks a plain sentence of his own out loud to somebody else.
#     Pattern noted in interior: three women, three rooms, three modes of
#     being-with in one night.
#   - He does not resolve anything with Tessa. He receives, he replies, he
#     leaves. The scene is held open.
# cann.tessa_state:
#   - The clinical mask finally drops (half-off, not off). Explicit internal
#     acknowledgement that her care has become attachment and that she has
#     been hiding behind her profession for three weeks.
#   - The single-use attachment word in tthought is deliberately not printed
#     in dialogue. It is her private permission to herself. It authorizes the
#     scene but does not obligate a response.
#   - She does not ask Aeron for reciprocity. She explicitly frames the not-
#     asking as the gift. "We are even" is a formal gesture, not a literal
#     accounting — her interior names that they are not even.
#   - She chooses to return to the medbay after the cache, not retreat for
#     the night. The choosing is the difference.
#   - The scene ends with her dimming the lamp one notch and standing alone
#     under the dimmer light. She is going to sleep badly and be okay with it.
# cann.path_tracking:
#   - EMP path only. Linear. No branching.
#   - rel_bump Tessa trust +2, attraction +1. flag tessa_held_not_fixed_spoken.
#     flag tessa_clinical_mask_dropped. flag aeron_received_held_not_fixed.
#     canon_set tessa.care_is_attachment. canon_set tessa.hand_on_sternum.
#   - tp_seed a4.tessa.held_not_fixed — the thread is open for Act IV/V payoff.
#   - nudge_poly threshold 1 — the scene formally raises the polyamorous
#     configuration reading. No kiss, no escalation, but the configuration is
#     now readable by the state system.
# cann.thematic_flags:
#   - Held, not fixed — the Act IV Tessa thesis in one sentence. Mercy for
#     the commander that does not pretend to solve him.
#   - Three women, three rooms, three touches in one night: Lyra's hand on
#     Aeron's shoulder (s11a), Selene's presence without touch (s11b), Tessa's
#     hand on Aeron's sternum (s12). Three different grammars of being-with,
#     all in one night. Aeron's interior clocks the pattern without naming it.
#   - The clinical mask as a defense — Tessa names it explicitly and stops
#     using it. "Hiding behind the profession." This is her Act IV pivot.
#   - The not-asking as the gift. Tessa refuses to demand reciprocity. This
#     is load-bearing for the poly configuration's ethics — information
#     offered without price.
#   - Plain sentences without qualifiers. Three women are teaching Aeron this
#     grammar tonight (Selene wordlessly, Lyra via Seren, Tessa via "held,
#     not fixed"). Aeron speaks his first plain sentence of the night to
#     Tessa: "You're right. It's not nothing."
#   - The lamp dimmed one notch at the close — not off. The scene is not over;
#     it is suspended. No over-closure.
# cann.character_moments:
#   - Tessa: stepping out of the side door without pretending she was on her
#     way somewhere else. The pat on the stool. The face-down datapad. The
#     enumerated list of things she will not do. The hand on the sternum. The
#     "not clinical anymore" sentence. The single-use attachment word in
#     tthought (not printed in dialogue). The almost-laugh. The dimming of
#     the lamp one notch.
#   - Aeron: following without resistance. Placing his hand over hers, not
#     pulling. The plain-sentence reply. Obeying the instruction to say "I
#     am held" aloud once more before leaving. The interior recognition that
#     they are not even and that the not-asking is the gift.
# cann.callbacks:
#   - a2_int_tessa_torins_name / a3_int_tessa_the_board_emp: Tessa's board
#     and rule of three. This scene is the continuation of her arc from
#     keeper of names to chooser of attachments. Her hand goes from the
#     marker to the sternum.
#   - a4_s05_delegation_test_emp: Aeron borrowed Tessa's rule of three
#     silently. This scene is the first time Tessa has met Aeron since that
#     borrowing without turning the meeting into a check-in.
#   - a4_s05a (Tessa corridor "presence is enough"): the original "your body
#     is not a resource to be spent" line. This scene evolves that care from
#     guidance into explicit attachment.
#   - a4_s06 (silent addition to the board — Batch A): Tessa's quiet authority
#     over the board. Here she exercises a quiet authority over a man instead,
#     and the quiet is the same quiet.
#   - a4_s04_lyra_unbuckled_emp: Lyra's "presence is enough." Tessa's
#     "held, that is not nothing." Same grammar, different women, different
#     touches. Aeron's interior clocks the cross-LI language.
#   - a4_s11a_prayer_after_mercy_emp: Lyra's Seren. Aeron does not think
#     the word Seren during this scene, but the plain-sentence grammar he
#     uses ("You're right. It's not nothing.") is the same grammar Lyra
#     taught him an hour and twenty minutes earlier.
#   - a4_s11b_the_ones_he_lost_emp: the rule of three breaking on Liora.
#     Tessa does not know yet that it broke. Aeron silently resolves earlier
#     in s11b to tell her without a qualifier. This scene is not the telling;
#     the telling is still pending. The hook is preserved.
# cann.block_status:
#   - MAJOR TESSA BEAT. Linear. EMP only. No branching.
#   - Polyamory configuration formally raised by state system (nudge_poly
#     threshold 1). No player-facing declaration yet. The configuration is
#     now readable, not decided.
# cann.requires_followup:
#   - Tessa's single-use attachment word in tthought is a hook. Later Tessa
#     scenes may surface the word explicitly in dialogue or may leave it
#     held. The author's discretion.
#   - The "hand on the sternum" is now a body motif for Tessa. Any later
#     scene that references the sternum, the center line, the flat-of-hand,
#     or "held, not fixed" is referencing this scene.
#   - The plain-sentence grammar is now shared between Aeron and Tessa. The
#     next scene in which Aeron speaks a plain sentence to any LI is reading
#     in a chord with this scene.
#   - Aeron owes Tessa a matched piece of interior. She has said she is not
#     asking for it. The owing is still real, and he will carry it forward.
#   - Aeron still has not told Tessa that the rule of three broke on Liora.
#     The telling is pending. It is a future Tessa/Aeron scene hook.
#   - The three-women-one-night pattern (Lyra, Selene, Tessa) is now on the
#     record. A later scene may collapse the three into an explicit
#     conversation or may let the pattern remain implicit.
#   - Tessa dimming the lamp one notch instead of off is a visual motif for
#     "not-over." Reusable in later Tessa scenes as a closing shorthand.
