# =======================================================
# ACT 4 - Scene 19: Lyra Deepening (Empathy Path)
# File: a4_s19_lyra_deepening_erotic_emp.rpy
# Type: LYRA EROTIC DEEPENING — devotion as shared burden
# Phase III (act climax arm). Follows s16 (Rhea Vestin's first
# cut, Davel Ostra KIA). The vigil has just finished. Lyra led
# it. Afterward she goes to her private altar space — not to
# pray, but to find out whether her body is a site of worship
# without needing to be sanctified. The Act 3 Lyra first
# erotic was "devotion as presence." Act 4 is "devotion as
# shared burden." The Band is off tonight and she is not
# putting it back on during the scene — she will put it back
# on in the morning, as a chosen sentence, not a cage.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s19_lyra_deepening_erotic_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s19_lyra_deepening_erotic_emp:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s19_lyra_deepening_erotic_emp")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Four movements.
    #         (1) The small hall after the vigil: 85mm long lens. The
    #             back of Lyra's head, her Band-hand at her side — we
    #             see the wrist and the Band is not on it. The other
    #             celebrants have left. She is the last body in the
    #             hall. A single candle still burning on the low
    #             table. The camera holds on the back of her shoulders
    #             for a long beat.
    #         (2) Corridor to her private altar space: 50mm. Aeron
    #             following three paces behind. Neither speaks. They
    #             walk through the secondary base at oh-one-forty the
    #             way two people walk through a building that has
    #             just lost one of its names.
    #         (3) The altar space: the same space as s11a, but
    #             tonight it is different. The bench is there. The
    #             three candles are there. The back wall is the same
    #             back wall. The difference is Lyra. The difference is
    #             the Band on the bench beside her instead of on her
    #             wrist. The camera frames the Band and Lyra in the
    #             same shot and lets the absence be the subject.
    #         (4) The held beat: macro on Aeron's hand placed on
    #             Lyra's sternum at her direction — callback to
    #             Tessa's medic move in s12, but rewritten. Hand flat.
    #             Palm against the sternum bone. Under the palm: her
    #             heart, her breath, the Old Tongue word she is
    #             about to speak. The camera stays on the hand for a
    #             long count.
    # LIGHTING: Three candles. Same as s11a. No overhead. No work
    #           lamp. The back wall is unlit and recedes into a deep
    #           shadow. The warm low of the candles on Lyra's face
    #           and hands. The candles do not move — the ventilation
    #           is on its long cycle and the room is the most still
    #           room on the base tonight.
    # SFX: The base at its quietest. The generator so far away it is
    #      almost not a sound. Her breath. His breath when he is in
    #      the room. The soft shift of cloth when she moves. No
    #      music at all until the consent gate. After the consent
    #      gate: one held low note — the same cello-or-something-like-
    #      it from s11a, picked up and held, the way a prayer picks
    #      itself up mid-phrase when the voice that started it has
    #      stopped. The note does not resolve.
    # FX/COMP: THE BAND. On the bench. Not on her wrist. Not hidden.
    #          Placed where she placed it before she went to the
    #          vigil and did not put it back on. The Band catches
    #          the candlelight on its seam exactly the way it does
    #          in s04 — the catch is the signature of the Band's
    #          material, and the signature is present tonight even
    #          though the wearer is not wearing it.
    #          THE BENCH. Her low altar bench. A wooden piece she
    #          has had for longer than the secondary base has
    #          existed. Worn at the edges by her knees. The bench
    #          is the place where her worship has happened; tonight
    #          the worship is not going to happen at the bench, the
    #          worship is going to happen a meter in front of the
    #          bench, where there is nothing except two bodies.
    # BLOCKING: Lyra enters the altar space first. She walks to the
    #           bench. She does not kneel. She touches the Band
    #           where it is lying on the bench, once — not picking
    #           it up, confirming. Then she turns, and she walks
    #           one pace out from the bench into the open floor
    #           between the bench and the back wall, and she stops,
    #           and she waits for him. Aeron follows her in. He
    #           stops at the threshold for a beat. He crosses. He
    #           stops a handspan from her. She takes his hand.
    # FACE: Lyra — the face she had in s11a when she said Seren,
    #       plus one new thing: a face that has just led a vigil
    #       for a runner she did not know and is now in a room that
    #       is hers and is looking at a man who came to the vigil
    #       and is now in this room with her. The composure is not
    #       priestly. The composure is the composure of a woman
    #       who has decided, tonight, to be a woman in addition
    #       to being a priest. Aeron — the exhaustion of a man who
    #       signed the operation order that sent Davel Ostra to the
    #       canal. The exhaustion is in his shoulders, not his face.
    #       He has put it in his shoulders on purpose. He does not
    #       want the exhaustion in his face tonight.

    # ========= VOICE BASELINE =========
    # EMP cadence. Very quiet. Lyra's diction is the cleric-clean
    # register, but stripped of liturgy — she is not performing
    # priest tonight, she is being a woman who happens to have
    # been trained as a priest. Old Tongue word used: Anayet,
    # and in the new context. Seren is referenced once by name,
    # not re-glossed. Aeron speaks least. Internal thoughts run
    # on Lyra (lthought) — this is her scene and the scene is a
    # document of a priest arriving at her own body as a site of
    # worship without needing to sanctify it first.

    # scene bg_lyra_private_altar_emp with dissolve
    # play ambient "sfx/ambient/base_deep_night.ogg" fadein 3.0

    # ========== PHASE 1 — AFTER THE VIGIL ==========

    "Zero one thirty-eight. The vigil for Davel Ostra has been over for twenty-three minutes."

    "Lyra led it."

    "It was not a long rite. Davel was twenty-two. He had been with Phoenix for eighteen months. He had a sister in the secondary base kitchen named Kesa who stood in the front row with her hands in fists at her sides and did not cry until the rite was halfway through and then cried silently for the rest of it, her shoulders shaking in a steady rhythm that was its own kind of prayer."

    "Lyra had spoken for eleven minutes. She had said the Academy words that could be said in a room with non-believers in it — the short form, the field form, the form that has been cut down so many times over the centuries that what is left is the bone of the rite and nothing else. She had said his name. She had said his sister's name. She had said the names of the two handlers who had worked with him on the canal rendezvous route. She had said the name of the building he was born in, because Kesa had told her the name an hour before the rite, and Kesa had asked her to say it, because the building was the only thing Davel and Kesa had ever shared besides each other and Kesa wanted the building named into the room."

    "Lyra had said the building into the room."

    "Then she had said the one sentence that was not an Academy sentence, which was: 'Davel Ostra is held.'"

    "She had not said who was holding him. She had not named the god or the field or the priestly attention or the Phoenix network or anything else that could have been the subject of the sentence. She had said the passive and let the passive be the sentence, because a passive without a subject is what you say when the holding is happening and the holder is not the point."

    "Then she had been quiet for the remaining sixty seconds of the rite, and then she had nodded once, and the others had understood that the rite was finished, and they had left."

    "Kesa had left first. Then Tessa, who had been standing in the back with her hand on Kesa's shoulder. Then the two handlers. Then the small group of five or six Phoenix fighters who had known Davel well enough to come but not well enough to stay for the part of the vigil that happens after the formal rite ends."

    "Aeron did not leave."

    "He stood in the back of the small hall and he did not move."

    "Lyra stood in the front of the small hall and she did not move."

    "The candle on the low table at the front continued to burn. The ventilation made a small pass on its long cycle. The hall was otherwise silent."

    "After three minutes Lyra turned her head and looked at him from the front of the hall."

    "She did not say anything."

    "He did not say anything."

    "She walked past the low table, picked up the candle — cupping the flame with her left hand so it would not go out in the corridor draft — and walked the long way down the center of the hall to where he was standing in the back."

    "She stopped in front of him."

    l "Come with me."

    "That is all she said."

    "He came."

    # ========== PHASE 2 — THE CORRIDOR ==========

    "They walked through the secondary base at oh-one-forty in single file — her in front with the candle cupped in her left hand, him three paces behind."

    "The corridors were empty. The base was holding its breath. Somewhere three levels below them a generator was making its small mechanical sound and the sound was the only sound that was not their footfalls."

    "Aeron watched the back of her shoulders as she walked."

    athought "She is not wearing the Band."

    athought "I noticed at the vigil. I did not want to look at her wrist during the rite, because looking at her wrist during the rite would have been the wrong angle of attention — she was being the priest and the priest was not the subject of the attention the priest was directing. But I noticed anyway. The Band is not on her wrist. It is — somewhere. In her quarters. On the altar bench. Somewhere she left it before she came to the rite."

    athought "She led Davel Ostra's vigil without the Band."

    athought "That is a sentence I do not yet know how to finish."

    "She turned the corner into the corridor that runs past her quarters and continued past her quarters to the small space she has cleared behind them. The door to the space is unlatched — she has not been in the habit of latching it since s11a, because nobody except Aeron comes to this space, and he has been at the door twice in the last two weeks, and the not-latching has become the signal."

    "She pushed the door open with her elbow, the candle still cupped in her left hand."

    "She entered."

    # ========== PHASE 3 — THE BAND ON THE BENCH ==========

    # scene bg_lyra_private_altar_emp_night with dissolve

    "The space is the same space as s11a. The low bench. The back wall. The three candles — already lit, the wax below each candle's line measurably deeper than it was eighteen nights ago when he was last in this room. The fourth candle in her hand from the vigil is new. She walks to the low bench and places it there, beside the three, where the three have been making a triangle and the fourth makes the triangle into a small cluster."

    "And the Band is on the bench."

    "It is not on the altar itself. Lyra does not put the Band on her altar — that is not where it lives and never has been. The Band is on the near corner of the bench, coiled loosely, the seam catching the candlelight exactly the way it does in s04. Eleven years of her wrist worn into the leather in a faint darker curve. It is not hidden. It is not displayed. It is present."

    "Aeron stops at the threshold."

    athought "I am not going to cross until she has told me I can."

    athought "The rule for this room has always been: if you come in loudly, you did not come in at all. But tonight the Band is on the bench and the rule might have changed and I am going to wait for her to tell me which rule is in effect."

    "Lyra turns from the bench."

    "She looks at him across the space. The candlelight is on her from one side, her left, because that is where the cluster of candles is. Her face is half in warm and half in the soft shadow of her own hair, which is loose tonight — not braided back, not pinned, just loose at her shoulders."

    l "The Band is on the bench."

    a "I saw."

    l "I took it off before I went to the vigil."

    a "I know."

    l "You do not know why."

    a "No."

    l "Come in, Aeron. I am going to tell you why."

    "He crosses the threshold."

    "He closes the door behind him. The small click of the latch. The room is sealed."

    "He walks across the space and he stops a handspan from her."

    "He is where he was in s11a — not kneeling, not sitting, not matching her height. Standing. The altar-bench beside them. The candles on the bench behind her shoulder. Her face looking up a small distance to meet his."

    # ========== PHASE 4 — THE PRAYER THAT WAS NOT PRAYED ==========

    l "I have been praying for three years."

    "Her voice is the low register from s11a."

    l "For most of those three years I have been praying the shape of prayers I was taught in the Academy. I have been praying them even after I started to notice that the prayers did not fit the mouth I had become, because the prayers were the tool I had been given and the tool is what a priest uses when a priest does not have a better tool."

    l "A year ago I started praying a different prayer. I did not write it down. I did not show it to anyone. I did not even say it out loud — the prayer was the kind of prayer that lives underneath your breath for a year before it surfaces."

    l "I was praying: please, let me be allowed to be a woman and not only a vessel."

    "A long beat."

    l "I have been a vessel for eleven years. The Band on my wrist has been the sign of the vessel-ness. The counting has been the vessel's metric. The cleric's register has been the vessel's voice. The Order trained me to be a vessel because a vessel is useful to an Order, and I was good at vessel-ness because I was a careful girl with a precise mind and the kind of discipline the Order rewards."

    l "Being a vessel has not been a lie. I am not going to tell you tonight that it was a lie. It has been one of the true things about me. I have carried other people's griefs through the vessel-shape and the vessel-shape has held them. The vessel is a real tool. I am not going to apologize for being good at it."

    "A beat."

    l "But a vessel is not the whole of me. I have a body that is not a vessel. I have a body that wants to be in a room with a man I have chosen, and the wanting is not a vessel-function, and the wanting has been pressing against the vessel-walls from the inside for longer than I have been willing to admit."

    l "I have been asking whether the wanting is allowed."

    l "I have been asking in the shape of a prayer because prayer is the shape I have, but the question was not a prayer question. The question was: do I need the vessel-shape to be a woman, or can I put the vessel-shape down for a night and still be a priest in the morning."

    l "I have been afraid of the answer for a year."

    "A beat."

    l "Tonight I led a vigil for a twenty-two-year-old runner whose sister I did not know two hours ago. I said the Academy words. I said his building into the room. I said 'Davel Ostra is held.' I used the passive because the holder was not the point of the sentence."

    l "And I realized, during the silence after the rite, that I had said the prayer I have been asking for a year."

    "Her eyes are on his."

    l "I prayed to be allowed to be a woman and not only a vessel. Tonight is my answer."

    # ========== PHASE 5 — THE OLD TONGUE, AGAIN ==========

    athought "She is not performing. I know the difference now. I know the difference because I watched her perform in the small hall twenty-three minutes ago and the performing was the rite and the rite was a real thing she was doing with her voice and her body, and the performing ended when Kesa left the hall, and what I am watching now is not performing."

    athought "What I am watching is a woman arriving at a decision she has been walking toward for a year, in a room she cleared for arriving at decisions."

    lthought "He is holding very still."

    lthought "He is holding the kind of still a person holds when they know that any movement is going to be the first movement of the scene and they do not want to be the one who starts the scene. He is waiting for me to move."

    lthought "I appreciate the waiting."

    lthought "I am going to move."

    "She takes his right hand in hers."

    "Not to hold it. To place it."

    "She lifts his hand slowly, and with her own hand over the back of his, she guides his palm to her sternum."

    "Flat palm. Fingers spread. The heel of his hand at the hollow where her collarbones meet. The pads of his fingers below her throat. The center of his palm over her sternum — the place where the bone is closest to the surface and where a medic puts a hand to listen for a cracked rib."

    "Tessa's move from s12."

    "Tessa put a palm there when she was teaching Lyra how to check for a fracture. The hand-on-sternum move was clinical. It was diagnostic. It was the hand of a woman with a medic's register placing itself on the structure of another woman's body to read the structure."

    "This is not that."

    "This is the same move rewritten."

    "The move is the move, but the register is not clinical and the register is not diagnostic and the register is not reading the structure. The register is — the register does not have an Academy word yet."

    "The register is the register of a priest placing a man's hand on her own body as the first movement of a sacrament she is making up in real time, in a room she cleared for making up sacraments in real time, in a tradition that she is inheriting from her dead mother and from the Seren priests the Order did not keep and from the part of her that has been underneath the vessel-shape for a year."

    "She keeps her own hand over his for a beat."

    "Her heart is under his palm. Her breath is under his palm. The bone of her sternum is under his palm. The warmth of her skin through the thin cloth of her underlayer is under his palm."

    "She speaks."

    l "{i}Anayet.{/i}"

    "She says it once. The way she said it in s04. The way she said it in s11a. The same word three scenes in a row, but each time in a different register."

    l "In s04 I said {i}Anayet{/i} as a word I had been carrying for a year without a place to put it down. I defined it as: I name the thing that cannot be promised. I said the word and I put the Band back on and I went to sleep and I did not know what I had done except that I had done it."

    l "In s11a I did not say {i}Anayet{/i}. I said {i}Seren{/i}, which is a different word for a different thing — to hold what will break you. I gave you {i}Seren{/i} because you had just made the mercy call and you needed a word for the shape of the call, and the Academy would not give you one."

    l "Tonight I am saying {i}Anayet{/i} again."

    l "Tonight I am saying it as an inheritance I am not leaving in my mother's mouth. Tonight I am saying it as a claim."

    "A beat."

    l "My hand is on your hand on my sternum. Your palm is covering the bone over my heart. I am saying {i}Anayet{/i} while you are feeling my heart against the bone. The word is a word for naming what cannot be promised, and I am not promising anything tonight — I am not promising I will be the woman I am becoming for the rest of my life, and I am not promising I will not be a vessel again tomorrow, and I am not promising that the version of me who prays in this room a year from now will recognize the version of me who is speaking now."

    l "I am naming the thing that cannot be promised, and the thing that cannot be promised is the woman my hand is pressing your palm against tonight."

    l "The word is the claim."

    l "I am claiming my own body as a site where a sacrament can happen without needing to be sanctified by the Order that taught me the word for sacrament in the first place."

    l "The Band is on the bench because tonight the Band is not the interface."

    l "The Band has never been the interface except in the way that an instrument is an interface. I am the interface. The Band was an instrument I used. Tonight I am not using the instrument. Tonight I am using the voice that used the instrument, and the voice is also mine."

    "A beat."

    l "I have prayed to be allowed to be a woman and not only a vessel. Tonight is my answer."

    # ========== PHASE 6 — AERON'S LINE ==========

    "He is holding very still."

    "His palm is on her sternum. Her hand is over his. Her heart is under his palm. Her eyes are on his."

    athought "I am going to say the sentence now."

    athought "I have been rehearsing the sentence since the vigil ended. I did not know I was rehearsing it. I was standing in the back of the small hall watching her speak Davel's building into the room and a sentence was forming somewhere underneath my sternum, and I did not have a conscious register for it, and now the sentence is here."

    athought "The sentence has to meet the word she just said."

    athought "{i}Anayet{/i} is a word for naming what cannot be promised. The sentence has to be a sentence for meeting a thing that refuses to be promised — not by promising it back, not by fixing it, not by containing it, not by classifying it."

    athought "By meeting it where it is."

    athought "The sentence is: I will meet you anywhere."

    athought "The sentence has to do more work than that. The sentence has to acknowledge the both/and she has been living inside — priest and woman, vessel and not-vessel, Band and not-Band. The sentence cannot ask her to choose."

    athought "The sentence is: be both. Or neither. I will meet you anywhere."

    a "Lyra."

    l "Yes."

    a "Then be both. Or neither."

    a "I will meet you anywhere."

    "A beat."

    "Her eyes close."

    "Her hand tightens on the back of his — not to trap, not to press, to acknowledge."

    lthought "He said it without flinching."

    lthought "He said it in the register I said the word in. He did not try to match me by saying an Old Tongue word of his own — that would have been a performance, and the performance would have been an act of respect and would have been the wrong kind of respect. He said it in Aeries. In the language we share. He said the sentence that has been underneath our relationship since the roof of the administrative spire in the fourth year of field training, and he said it tonight, with his palm on the bone over my heart."

    lthought "He has been preparing to say that sentence for eleven years and I did not know he had the words for it and I am not sure he knew he had them either and the words arrived in his mouth the way the Old Tongue arrives in mine — from somewhere he did not put them."

    lthought "This is the answer to the prayer I did not know I was praying."

    lthought "The answer was that the answer existed."

    lthought "I have been asking whether the wanting was allowed. The answer is that a man is standing in my altar room with his palm on the bone over my heart saying 'be both or neither I will meet you anywhere' and the answer is in the saying."

    lthought "The wanting is allowed."

    lthought "It has been allowed for a year. I was the one not allowing it."

    lthought "I am going to allow it now. I am going to allow it by doing it. The curriculum is the body in the room, and I have the body, and he has the body, and we have the room."

    # ========== PHASE 7 — CONSENT GATE ==========

    "She opens her eyes."

    "She does not move her hand from the back of his, does not move his hand from her sternum. The placement is the scene's architecture now. The placement is the interface."

    l "I am going to ask you a question."

    a "Yes."

    l "The question is in three shapes. You can answer any of them and the answer will be the answer. I am giving you three shapes because the shapes are three different things and I want you to know all three exist before you choose."

    a "Lyra."

    l "Yes."

    a "I love the way you say 'exist.'"

    "A very small almost-laugh from her. Not a laugh. The skeletal version of a laugh. The same almost-laugh she made in s11a."

    l "Thank you."

    l "Here are the shapes."

    menu:
        "I have chosen. Stay.":
            $ lyra_consent_route = "chosen_stay"
            jump a4_s19_lyra_route_chosen
        "I need you to choose with me.":
            $ lyra_consent_route = "choose_with_me"
            jump a4_s19_lyra_route_with
        "Just hold me tonight.":
            $ lyra_consent_route = "hold_only"
            jump a4_s19_lyra_route_hold

label a4_s19_lyra_route_chosen:

    a "I have chosen. Stay."

    l "That is the one I thought you were going to choose first."

    a "I am not sure whether that is because I am predictable or because the shape was the closest to me."

    l "I think it is because the shape was the closest to you. You are predictable only in the sense that a person who has learned his own grammar is predictable to the person who taught him half of it."

    a "You taught me half of it."

    l "I taught you the listening half. Selene taught you the deciding half. You are currently the person who listens-and-then-decides, and the combination is a person neither of us taught you to be — you assembled him yourself out of the two halves."

    l "I am glad he is the one in my altar room tonight."

    "She lifts her hand from the back of his. Her hand goes to the side of his face. Her other hand stays at her side — the hand that was over his at her sternum is free now, and his hand is still on her sternum because she has not asked him to move it."

    l "Do not move your hand from my sternum for a while. That is a request, not a command."

    a "It is not leaving."

    l "Good."

    "She rises onto the balls of her feet."

    "She kisses him."

    "The kiss is the first kiss in the scene. It is a priest's kiss — not in the sense that it is chaste, in the sense that it is the kiss of a woman who has decided what the kiss is for, and the what-it-is-for is not the same as the what-it-is-for of a kiss that is not a priest's kiss."

    "His hand stays on her sternum."

    # [INTIMATE CONTENT HERE]
    # (User writes this beat. Lyra erotic deepening — "I have
    # chosen. Stay." variant. The Band stays on the bench. His
    # hand returns again and again to her sternum as the interface
    # callback. The grammar is a woman who has stopped asking
    # whether her body is allowed to be a site of worship without
    # needing to be sanctified first. The altar candles are lit.
    # The room is warm. Do not cut to aftercare until the body of
    # the scene is complete on its own terms.)

    jump a4_s19_lyra_aftercare_intimate

label a4_s19_lyra_route_with:

    a "I need you to choose with me."

    "A beat. Her eyes go soft in a new way."

    l "That is the shape I did not think you would choose."

    l "That is the shape I was hoping you would choose."

    a "Explain."

    l "The first shape — 'I have chosen, stay' — is the shape that asks me to be the active party. It would have been the shape of a scene where I am the one who has chosen and you are the one who is receiving the choice. I would have been willing to be in that scene. I am not the one who chose it tonight."

    l "The third shape — 'just hold me tonight' — is the shape that asks for the non-erotic variant. It is a true variant. I have sat in this room alone many nights and I have known what the shape of being held looks like and I would have accepted it tonight if you had asked for it."

    l "The second shape is the one that asks us to be in the scene together. Not me choosing and you receiving. Not you asking for holding and me giving it. Both of us choosing. Both of us in the choosing. The choosing is the sacrament."

    l "That is the shape I have been learning all year. I taught you how to listen. Tonight I am asking you to choose with me because I am still learning how to choose without the Order telling me what the choice is, and the choosing is easier when there is another person choosing with me."

    l "I did not know you would pick that one."

    l "I am very glad you did."

    "She lifts her hand from the back of his. Her hand goes to his shoulder, then to the back of his neck — fingers in the short hair at his nape, where her hand has been before, where her hand has an address."

    l "We are going to choose together."

    l "The first choice is: we are going to stay in this room. Not in my quarters. Here. The Band is here. The candles are here. The back wall is here. The bench is here. The sacrament is being made in the space where the sacrament is being made."

    a "Agreed."

    l "The second choice is: we are not going to speak in the register of a priest and a commander. We are going to speak in the register of Lyra and Aeron. The registers we have been carrying all night are going to be set down."

    a "Agreed."

    l "The third choice is: my hand stays on the back of your hand at my sternum for as long as I need it to stay there. You are going to know when to let your hand go elsewhere because I am going to tell you with my hand."

    a "Agreed."

    l "The fourth choice is that you can make a choice I have not listed, and I will consider it, and we will decide together."

    a "The fourth choice is: we do not light a fourth candle."

    "A beat. She looks at him."

    l "Why."

    a "Because the fourth candle was the vigil candle. The vigil candle is on the bench with the Band. The vigil candle is Davel's. We are not doing anything tonight that includes Davel's candle as an instrument. Davel's candle gets to be on the bench with the Band and the two of them get to witness the room and we do not get to pull the candle into the sacrament we are making."

    "Her eyes are very steady."

    l "Agreed."

    l "That was a choice I had not thought of. You saw it because you have been watching the room with the attention of a man who is choosing to be in it. That is the register of the night."

    l "Kiss me, Aeron."

    "He kisses her."

    "The kiss is not the first kiss of s04 and it is not the Seren-after kiss of s11a. The kiss is the kiss of two people who have just agreed on four things and the kiss is the fifth thing and the fifth thing is the sacrament they are making together."

    # [INTIMATE CONTENT HERE]
    # (User writes this beat. Lyra erotic deepening — "I need you
    # to choose with me" variant. The scene is built on mutual
    # choosing. Both of them make micro-choices throughout. The
    # Band is on the bench. The vigil candle is on the bench. His
    # hand on her sternum is the interface. The room is warm. The
    # sacrament is the choosing-together. Do not cut to aftercare
    # until the body of the scene is complete on its own terms.)

    jump a4_s19_lyra_aftercare_intimate

label a4_s19_lyra_route_hold:

    a "Just hold me tonight."

    "A beat."

    l "Say it again."

    a "Just hold me tonight, Lyra. That is the shape."

    "She is looking at him with a face he has not seen on her before — not because he has not seen her tender, he has seen her tender many times in eleven years, but because he has not seen her tender in the specific register of a woman receiving a request to hold that is coming from the man who was supposed to be the holder."

    l "You are asking me to be the one who holds tonight."

    a "Yes."

    l "Why."

    a "Because I signed the order that sent Davel Ostra to the canal."

    a "I did not pull the trigger Rhea Vestin pulled. I am not — I am not going to claim the trigger. The trigger is Vestin's and she is going to have to carry it, and we are going to have to stop her from pulling another one, and the stopping is tomorrow morning's work."

    a "But I signed the order. I signed the order knowing the canal rendezvous carried a thirty-one percent probability of interception by a Vestin-class specialist. Noelle's framework had the number. I read the number. I signed anyway because the operational gain was worth the thirty-one percent on the framework I had at the time. The framework was correct. The signing was correct. And Davel is dead."

    a "I have been carrying the signing for six hours. I led operations from the signing forward. I did not put the signing down. I did not know how to put it down. I did not know where to put it down."

    a "I came to the vigil because the vigil was the place where the signing could be put down for eleven minutes and I could stand in a room where you were saying Davel's building into the air."

    a "You asked me what shape I wanted tonight. The shape I want is: you hold me. I will not perform being held. I will just be held. And you will hold me because you are the person I trust to hold a man who signed the order that killed the boy you just led the vigil for."

    a "I am asking you to hold me without asking me to explain the signing."

    "A long beat."

    "Her face has not moved. Her hand is still on the back of his where his palm is on her sternum."

    "Her eyes are wet. She is not crying — the wet is the wet at the lower lid that does not become crying, the same wet Selene had in s12a when a person is holding a thing very precisely and the hold costs water at the edges."

    l "Aeron."

    a "Yes."

    l "Come here."

    "She steps forward — closing the handspan between them to nothing — and she wraps her arms around him."

    "Not ceremonially. Not priestly. She wraps her arms around him the way a woman wraps her arms around a man who has just asked to be held and has specified that he is not going to explain the asking."

    "His face goes to the side of her neck, under the loose weight of her hair."

    "She puts one hand flat on the back of his head and the other flat between his shoulder blades."

    "They stand there."

    "The three altar candles burn. The vigil candle burns. The Band is on the bench. The back wall is in shadow. The ventilation makes its slow pass. The room holds them."

    "He does not speak."

    "She does not speak for a long while. When she does, her voice is against the top of his head, the way Selene's breath was against the top of his head in s17."

    l "I am going to tell you something the Order never told me and the Academy never told me and my mother never told me and I had to find out by doing it."

    l "A priest is not the thing that holds other people."

    l "A priest is a person who has been trained to be a witness to the holding that was already happening before the priest arrived, and will still be happening after the priest leaves, and the priest's job is to be in the room while the holding happens and not to be the holding itself."

    l "I am not the thing holding you tonight."

    l "The room is holding you. The hour is holding you. The fact that you signed a hard order and brought it to the vigil and did not perform your way through the carrying — that is holding you. Davel's sister's tears in the front row are holding you, and they are not her tears for you, they are her tears for her brother, and the tears are holding everyone in the hall, because that is what tears in the front row do."

    l "I am in the room with the holding."

    l "I am a witness to the holding."

    l "My arms are around you because my arms are the witness's arms tonight, and the witness is allowed to have arms, and the arms are allowed to be warm."

    "A beat."

    l "This is what I learned by taking the Band off for the vigil."

    l "I learned that the witness is not the Band. The witness is me. The Band was the instrument of the witness. Tonight I am the witness without the instrument, and the witnessing is still happening, and the witnessing is holding you in my arms without me having to pretend the witnessing is me."

    l "This is the sacrament I did not know existed until I walked into this room twenty minutes ago and decided to do it."

    "She is quiet for a long time after that."

    "He does not say anything. He is crying — not loudly, not theatrically, the silent crying of a man whose shoulders are moving in a small rhythm against her chest, because the asking to be held had been the hard part and the being held is the soft part and the soft part is letting the signing be a thing that is in him and not a thing he is holding in front of him."

    "She holds him for a long time."

    "Fade slow."

    jump a4_s19_lyra_aftercare_intimate

label a4_s19_lyra_aftercare_intimate:

    # ========== PHASE 8 — AFTERCARE ==========

    # CAMERA: 50mm. Lyra's face. The Band in soft focus at the edge
    # of frame, on the bench where it has been all night. The
    # candles are lower now — some of the wax has pooled. Her
    # wrist is still bare.
    # LIGHTING: The candles, lower and softer than at the start.
    # Nothing else.
    # SFX: Her breath. His breath. The small sound of the wax
    # moving as a candle's pool shifts. No music. At the end,
    # the held low note returns — the same note from s11a — and
    # does not resolve.

    "The candles are lower now than when he walked in."

    "Two of them are in their final third. The vigil candle — Davel's candle — is half gone. The space is a little darker than it was at the start of the scene, and the darker version of the space is more forgiving to faces."

    "Lyra is in his arms, or he is in hers, or neither is in the other's and they are just touching along a long line — depending on the route and the room and where the body of the scene landed them. Her hand is resting on his chest near the center of his sternum. His hand is resting on the small of her back. Her wrist is bare. The Band is still on the bench."

    "She has been quiet for a long time."

    "When she speaks, her voice is the register that is underneath the priest register, which is the register that is underneath the woman register, which is the register she has been approaching for a year and has finally arrived at tonight."

    l "I am going to put the Band back on in the morning."

    "A beat."

    l "I am telling you now because I want you to hear the sentence in this room before I say it in the morning. I want the sentence to exist here first."

    l "The sentence is: I am going to put the Band back on, not because I have to, and not because the Order requires it of me, and not because my wrist is incomplete without it, and not because I cannot be a priest without the instrument — I know tonight that I can. I proved it at the vigil. I led Davel Ostra into the room without the Band on my wrist, and the holding still happened, and the Academy words still fit in my mouth, and the naming of the building was still the naming of the building."

    l "I do not need the Band to be the priest."

    l "I am going to put it back on anyway."

    l "Because the Band is not my cage anymore. The Band is my sentence. It has always been my sentence, I just did not know the difference until tonight. The sentence was being spoken through me by the Order for eleven years, and then for three years by me-as-vessel, and tonight, for the first time, I put the sentence down — I set it on the bench, I walked into another room, I said different words in that room, I walked back here, and the sentence was still on the bench, waiting for me to pick it up."

    l "A cage is a thing you cannot put down."

    l "A sentence is a thing you put down and pick up, and the picking up is the choice, and the choice is what makes it your sentence."

    l "Tonight I put the Band down because I was not speaking it."

    l "I was speaking something else in this room. I was speaking {i}Anayet{/i} and {i}Seren{/i} and 'be both or neither I will meet you anywhere' and the whole grammar of a woman who is in her own body on her own terms, and that grammar does not need the Band, and the Band was on the bench because the Band was not the grammar of this room tonight."

    l "In the morning the grammar of the room is going to be different. In the morning the grammar is going to be: the priest goes back into the hall and puts the building names into the air for the next dead runner and the next and the next, because there are going to be more dead runners, and someone is going to have to say their buildings into the air."

    l "The morning-grammar needs the Band."

    l "Not because the Band is the priest. Because the Band is the sentence the priest is choosing to speak."

    l "And I am choosing to speak it."

    l "I am telling you in this bed at oh-three-something in the morning so that when you see the Band on my wrist in the mess hall you will know that the Band is not back on my wrist because I have retreated from what happened in this room tonight."

    l "The Band is back on my wrist because I am going to speak the sentence again, and the sentence is mine now, and the mine-ness of it is what I found here."

    "A long beat."

    "He has been listening. He does not interrupt. He waits to be sure she is done before he says anything, the way he has been waiting all week, the way he has learned to wait, because listening has become the half of him that she taught him and the listening is the gift he has to give her tonight."

    "When she is done, his hand moves slowly up from the small of her back to the place between her shoulder blades. His other hand, the one that has been on her sternum at several different points in the night, finds her wrist — the bare one, the one the Band usually covers — and his fingers circle it gently."

    "He does not count."

    "He does not put his thumb on the place where the Band's seam would be."

    "He just holds her wrist in his hand, bare, the way a person holds a thing that is about to be covered again in the morning and is, for one more hour, uncovered."

    a "I heard you."

    a "I am going to see the Band on your wrist in the mess hall and I am going to know what it is."

    a "And I am going to know what it is not."

    a "And I am going to hold the difference the way you are holding the difference. The sentence is yours. I am going to be the person in the room who heard you say it."

    "A beat."

    a "Lyra."

    l "Yes."

    a "Thank you for the room."

    l "Thank you for meeting me in it."

    "A long beat."

    "The cello-note from s11a returns, very faintly, somewhere under the audio mix. It does not resolve. It holds on the same pitch it held on three scenes ago, as if the prayer that started in s11a has been waiting for the woman to arrive in her own body to match it, and the matching has just happened, and the note is going to keep holding until the next time the scene has an answer for it."

    "Lyra closes her eyes."

    "She does not fall asleep. She is not going to fall asleep tonight — the sleep will come later, in a bed, after the candles are out. Right now she is in the register of a woman who is awake inside a decision she has made and the decision is sitting softly in her chest and she is letting it sit there."

    "His hand stays on her wrist."

    "The Band is on the bench."

    "The candles burn."

    "Fade slow."

    jump a4_s19_lyra_scene_close

label a4_s19_lyra_scene_close:

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=2, attraction=2)
    $ canon_set("lyra.band_as_chosen", True)
    $ canon_set("lyra.woman_and_not_only_vessel", True)
    $ canon_set("lyra.led_vigil_without_band", True)
    $ flag("lyra_band_off_overnight", True)
    $ flag("lyra_erotic_deepening_emp", True)
    $ npc_remember("Lyra", "led_davel_ostra_vigil", tone="without_instrument")
    $ npc_remember("Lyra", "placed_his_hand_on_her_sternum", tone="sacrament_without_sanction")
    $ npc_remember("Lyra", "anayet_as_claim_not_inheritance", tone="arrived")
    $ npc_remember("Aeron", "be_both_or_neither_i_will_meet_you_anywhere", tone="the_sentence")
    $ tp_seed("a4.lyra.woman_and_not_only_vessel")
    $ tp_seed("a4.lyra.band_is_my_sentence")
    $ metric("lyra_sacraments_without_order_sanction", delta=1)
    $ nudge_poly("lyra", "devotion_as_shared_burden", delta=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s19_lyra_deepening_erotic_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Zero one thirty-eight, immediately after Davel Ostra's vigil.
#     Lyra led the vigil without the Band on her wrist. The other
#     celebrants have left. Aeron stayed. She walks him to her
#     private altar space (the same space as s11a).
# cann.what_happened:
#   - Lyra leads the vigil for Davel Ostra, twenty-two, killed on
#     the canal rendezvous by Rhea Vestin. She says the Academy
#     short-form rite and, at the request of Davel's sister Kesa,
#     names the building Davel was born in. She speaks the passive
#     sentence "Davel Ostra is held" and lets the passive be the
#     sentence.
#   - Aeron does not leave after the rite. Lyra walks to the back
#     of the hall, takes the vigil candle, and leads him to her
#     private altar space without speaking except "Come with me."
#   - In the altar space: the Band is on the bench, not on her
#     wrist. She explains that she has been praying for a year to
#     be allowed to be a woman and not only a vessel. She says
#     tonight is her answer.
#   - She guides Aeron's hand to her sternum — the Tessa-from-s12
#     medic move, rewritten as sacrament rather than diagnosis. She
#     speaks Anayet for the third time in the run, explicitly as a
#     claim rather than an inheritance.
#   - Aeron answers with the Act 4 Lyra sentence: "Then be both.
#     Or neither. I will meet you anywhere."
#   - Consent gate: 3 options. "I have chosen. Stay." / "I need you
#     to choose with me." / "Just hold me tonight." First two lead
#     to [INTIMATE CONTENT HERE] placeholders. The second route is
#     a variant in which they explicitly co-choose four things
#     about the scene, including Aeron's observation that the
#     vigil candle should not be an instrument in what they are
#     about to do. The third route is a tender non-erotic hold in
#     which Aeron asks Lyra to hold HIM, because he signed the
#     order that sent Davel to the canal, and she holds him and
#     teaches him that a priest is not the thing that holds but
#     the witness to the holding that was already happening.
#   - Aftercare: Lyra says she will put the Band back on in the
#     morning — not as a cage, as a sentence. "Tonight I put it
#     down because I was not speaking it."
# cann.aeron_state:
#   - "Then be both. Or neither. I will meet you anywhere" is the
#     Act 4 Aeron-to-Lyra sentence. Do not give this phrase to
#     another LI in the same arc. It is the answer to Anayet.
#   - He signed the order that sent Davel Ostra to the canal. The
#     signing is a weight he carries across the scene. In the
#     "just hold me" route he explicitly names it. In the other
#     two routes it is a subtext but not a spoken fact — the user
#     can decide whether to surface it in the intimate content.
#   - The hand-on-sternum move is the new Lyra-Aeron physical
#     vocabulary, replacing the Band as the interface. Cross-
#     reference with Tessa's medic move in s12 — the grammar is
#     inherited but the register is different.
# cann.lyra_state:
#   - First Lyra scene in which the Band is off for the whole scene
#     and stays off. She led a vigil without it for the first time.
#   - Anayet has been used three times in the run: s04 (as a word
#     she carries without a place to put it), s11a (referenced but
#     not spoken, Seren is spoken instead), s19 (as a claim). The
#     progression is the arc.
#   - "A priest is not the thing that holds other people. A priest
#     is a witness to the holding that was already happening." This
#     is the Act 4 Lyra thesis sentence. It appears in the "just
#     hold me" route explicitly; in the other routes it is the
#     operating theory but not the spoken theory.
#   - "The Band is not my cage. It is my sentence." This is the
#     Act 4 Lyra close-of-arc sentence. Do not revert.
# cann.thematic_flags:
#   - Act 4 EMP arm: body as site of worship without sanction.
#     Lyra's arm of the three-LI climax triangle is the arm where
#     the priest arrives at her own body as a sacrament that does
#     not require Order approval. Selene's arm (s17) is witnessing.
#     Noelle's arm (s18) is classification broken.
#   - Devotion as shared burden: Act 3 Lyra was "devotion as
#     presence" — she was with him in the room. Act 4 Lyra is
#     "devotion as shared burden" — she is carrying weight with
#     him, not just being near him. The "just hold me" route is
#     the most literal expression of the shared-burden thesis.
# cann.callbacks:
#   - s04 (the Band unbuckled, Anayet as the word without a place):
#     inverted. The Band is off for a whole scene, not just an
#     hour, and Anayet is the word in a sentence now.
#   - s11a (the Seren prayer after the mercy call): this scene is
#     the mirror image. In s11a Lyra gave Aeron a word for what he
#     had just carried. In s19 Aeron gives Lyra a sentence for
#     what she is claiming. The cello note returns at the end.
#   - s12 (Tessa's medic move — palm on sternum to listen for a
#     cracked rib): the same physical move, rewritten as a priest's
#     sacrament. The physical vocabulary is inherited; the register
#     is different.
#   - a3 Lyra first erotic ("devotion as presence"): this scene is
#     the second step. Devotion as presence was being in the room
#     together. Devotion as shared burden is carrying weight
#     together in the room.
# cann.character_moments:
#   - Lyra: leading the vigil without the Band. Saying "Davel
#     Ostra is held" in the passive. Walking Aeron to the altar
#     space with only "Come with me." Placing his hand on her
#     sternum and saying Anayet as a claim. "The Band is not my
#     cage. It is my sentence." "A priest is a witness to the
#     holding that was already happening."
#   - Aeron: "Be both. Or neither. I will meet you anywhere." In
#     the "choose with me" route: identifying that the vigil
#     candle should not be an instrument in the sacrament. In the
#     "just hold me" route: asking to be held because he signed
#     the order.
# cann.block_status:
#   - BRANCHING at consent gate. Three routes. First two lead to
#     [INTIMATE CONTENT HERE] placeholders. Third is a tender
#     non-erotic variant with Lyra holding Aeron. All three
#     converge on the same aftercare beat (Band-as-sentence) and
#     scene close.
# cann.requires_followup:
#   - tp_seed a4.lyra.woman_and_not_only_vessel — any future Lyra
#     scene that returns to the vessel/woman distinction gains
#     True Path weight. Do not let future scenes collapse the
#     distinction back into vessel-only.
#   - canon_set lyra.band_as_chosen is locked. The Band is no
#     longer a cage in canon. Any future Band scene should pay off
#     the "my sentence" reframing.
#   - canon_set lyra.led_vigil_without_band is a structural marker.
#     Future Lyra rites can be done with or without the Band; the
#     precedent exists.
#   - Cross-reference with a4_s17 (Selene deepening) and a4_s18
#     (Noelle deepening) for the three-LI climax triangle.
