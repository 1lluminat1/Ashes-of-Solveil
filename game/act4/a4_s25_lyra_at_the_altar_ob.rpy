# =======================================================
# ACT 4 - Scene 25: At the Altar (Obedience Path)
# File: a4_s25_lyra_at_the_altar_ob.rpy
# Path: OB
# Type: LYRA FINAL ACT 4 BEAT / DEVOTION CORRUPTION / THE COUNTING RITUAL
# Character Focus: Lyra (primary, interior), Aeron (witness, one exchange, one gesture)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s25_lyra_at_the_altar_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s25_lyra_at_the_altar_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm locked. The altar alcove -- the small room off the base's
    #         secondary corridor that Lyra has been using since the cathedral
    #         fell. The camera is at the back of the alcove, framed past her
    #         right shoulder. It does not move for the first three-quarters
    #         of the scene. When Aeron enters, the frame does not cut. He is
    #         in the reflected light from the alcove's threshold -- we see him
    #         as a half-lit figure behind her while she finishes the ritual.
    #         The camera only shifts when Lyra turns to face him: then one
    #         slow dolly forward, half a meter, no more, and a lock. The
    #         exchange happens in a medium two-shot. For the final gesture --
    #         Aeron kneeling, forehead on her knees -- the camera tightens
    #         to a close-medium that frames his head, her lap, and her hands
    #         held deliberately away from him at her sides. The hands-not-
    #         touching is in frame. The not-touching is the shot.
    # LIGHTING: Three candles. Real candles -- she has moved from base-issue
    #           candle-analogs back to real beeswax for this ritual because
    #           the Old Tongue rite requires the real smoke. The three
    #           candles sit on a folded cloth on the floor of the alcove,
    #           arranged in the triangle formation the rite specifies.
    #           Overhead: the corridor bleed is the only other light, cold
    #           and diffuse, coming in from behind her when the door is
    #           open. The alcove is warmer than any OB Act 4 scene has been.
    #           The warmth is not comforting. The warmth is the rite's
    #           permission to do what the rite is doing. Warmth as tool.
    # SFX: The alcove at oh-five-thirty. The base is beginning to stir
    #      behind the corridor -- distant bootfall, the slow hum of the
    #      morning cycle spinning up. Inside the alcove: the small
    #      constant sound of three real candle flames. The flames have
    #      a different sound than base-issue analogs. The three flames
    #      together make a triangle of small breathing. Lyra's breath
    #      is controlled. No score. When she speaks the Old Tongue
    #      phrases, her voice is pitched lower than her Aerenine voice.
    #      This is the register priests are trained into. It is the
    #      same register from a4_s04.
    # FX/COMP: The alcove. Three real beeswax candles in the triangle
    #          formation. The folded cloth beneath them is grey wool --
    #          not ceremonial color. She has used what she has. The
    #          Band at her wrist: still cinched past comfort, the same
    #          notch as a4_s04 and a4_s14. The buckle is visible in the
    #          candlelight when she lifts her hand. On the cloth beside
    #          the candles: a small clay bowl, empty, the kind of bowl
    #          priests use for the pouring rite. Beside the bowl: a
    #          folded paper with three lines of Old Tongue text copied
    #          in her own hand -- the counting-against-the-priest rite.
    #          She copied it from memory last night. The paper is the
    #          only piece of text in the alcove.
    # BLOCKING: Lyra is kneeling at the folded cloth when the scene
    #           opens. She has been in the alcove for approximately
    #           forty minutes. The ritual has been underway for thirty
    #           of those minutes. She is in the final phase when Aeron
    #           arrives. He enters through the alcove doorway and does
    #           not interrupt. He waits at the threshold. The threshold
    #           is two meters behind her. She does not turn when he
    #           enters -- she knows he is there because her peripheral
    #           field includes the doorway and because Aeron's footfall
    #           is known to her after three months. She finishes the
    #           rite. Then she turns. Then the exchange. Then the
    #           kneeling.
    # CANON: LYRA DEVOTION CORRUPTION APEX. This is the scene where
    #        Lyra's OB Act 4 arc lands its final position. She has
    #        invented a new liturgy (s04, s14). She has accepted the
    #        theology of "being in the room with it" (s14). Tonight
    #        she takes the next step: she volunteers to carry the
    #        counting of a sin that has not yet been committed. The
    #        Old Tongue rite for this is real in the lore -- priests
    #        who cannot prevent a sin being done by an institution
    #        they serve can petition the Six to count the sin
    #        against them personally, not against the act or the
    #        operator. The rite is not secret. It is rare. Lyra is
    #        performing it alone because she cannot perform it with
    #        another priest -- there are no other priests left in
    #        the base. The aloneness is canonical.
    # FACE: Lyra -- the priest's face for the rite. Composed, inward,
    #        not visibly cost-bearing. The cost is in the lthought
    #        and in the Band. When she turns to Aeron: the priest's
    #        face softens half a millimeter. Not into warmth. Into
    #        what she lets him see because he is the reason she is
    #        here. Aeron -- unprepared. He did not know she was going
    #        to be here. He came looking for her because she was not
    #        in her quarters and he wanted to see her once before the
    #        departure. He finds her in the middle of the rite. His
    #        face when he realizes what the rite is: the clinical
    #        precision breaks by half a degree. Half a degree is the
    #        scene.

    # ========= VOICE BASELINE =========
    # Lyra: Heavy lthought. Spoken lines are the Old Tongue closing of
    #        the rite, and the exchange with Aeron. The Old Tongue is
    #        pitched lower than her normal speaking voice -- the rite
    #        register. The Aerenine exchange with Aeron is her normal
    #        voice, but flatter. Flat because she has decided the
    #        decision and is no longer performing it for herself.
    # Aeron: Economic. Four spoken lines. "What just happened." "Why."
    #        "I do not want you to do that." "Lyra." The fourth is
    #        her name, said as the nearest thing OB-Aeron has to a
    #        protest. The athoughts are present but muted -- this is
    #        Lyra's scene and his interior is in service to her
    #        foreground.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ALTAR ALCOVE - PRE-DAWN]
    # 0528. Morning of the assassination-prep departure. Nyra has
    # been gone from the ops room for just under five hours. The
    # base is three minutes away from the morning cycle. Lyra has
    # been in the alcove since 0445. Aeron went looking for her at
    # 0520 when she was not in her quarters and not in the medbay.

    #scene bg_altar_alcove_ob_predawn with dissolve
    #play ambient "sfx/ambient/alcove_three_candles.ogg" fadein 2.0

    # ========== PHASE 1 -- THE RITE IN PROGRESS ==========

    "Three candles on the folded grey wool. The triangle is oriented toward the eastern wall of the alcove -- the wall is not the east of the base, it is the east the rite specifies, which is a different east, a directional convention Lyra was taught in the novitiate and has not had occasion to use professionally until this morning."

    lthought "The three candles are the Six halved."

    lthought "The rite uses three because a priest cannot petition all Six in a counting request. The rite recognizes that a counting is a half-petition. A full petition asks for mercy. A counting asks to carry a weight. You do not ask all the Six to witness a weight-carrying. You ask three. The three are Anayet, Veran, and Solen -- the three whose domains include weights."

    lthought "I have been here for forty minutes. The first ten minutes I spent trying to decide whether to perform the rite at all. The second ten minutes I spent copying the three lines from memory onto the paper because the rite requires a physical text even if the priest knows the text by heart. The text is not for the priest. The text is for the Six to read over the priest's shoulder."

    lthought "The last twenty minutes I have been performing the rite."

    lthought "I am in the closing phase."

    "She is kneeling. Her hands are on her thighs, palms up. Her eyes are on the middle candle. Her breath is slow and deliberate and matched to the cadence the rite specifies -- four in, six out, the priest's cadence for long petitions."

    lthought "The rite has seven phases. I have done six of them. The sixth phase is the naming of the act. I named the act at oh-five-eighteen."

    lthought "I named it out loud, the way the rite requires, into the triangle of candles. I did not soften the naming. I did not use a euphemism. The rite does not accept euphemisms -- the rite recognizes euphemism as a form of lying to the Six, and the Six will not count what they cannot see clearly."

    lthought "The naming was this: 'The blessing of the operation to assassinate Rhea Vestin, which will be performed by Phoenix operators in seven days under the command of Aeron Solveil, which I am going to bless because the operation will go forward whether I bless it or not, and I have chosen to be the priest who is in the room when the blessing happens.'"

    lthought "That is what I said. Every word. The candles received the naming."

    lthought "The seventh phase is the counting request."

    lthought "I am about to do it."

    # ========== PHASE 2 -- THE FINAL WORDS ==========

    "Lyra lifts her hands. Palms still up. Her hands come to chest height. The gesture is the hand-open gesture the Old Tongue uses for offering."

    "She speaks. The voice is lower than her Aerenine voice. It is the rite register."

    l "(Old Tongue, phase seven) Anayet i seren. Veran i thrun. Solen i velh-karn."

    lthought "Anayet who is still becoming. Veran of the steady hand. Solen of the weight between."

    l "(Old Tongue) Sen'a thrun karn velh. Karn'a sen-thrun. Velh'a ka-sen."

    lthought "Count the weight against the hand that asks. Against me, not against the act. Against me, not against the operator."

    "She pauses. The rite permits a pause here. It is the phase where the priest confirms the terms. The three lines of text on the paper beside the bowl are now the text she is reading from, even though she has the text memorized, because the rite requires the reading. She reads the lines. Then she speaks the closing."

    l "(Old Tongue) Ka-sen'al. Sen'al. Sen'al thrun-velh."

    lthought "The counting is mine. It is mine. It is mine as long as the hand is steady."

    "She lowers her hands to her thighs. Palms down now. The gesture closes the offering. The rite specifies that the priest must lower her hands in the same tempo she raised them -- four counts down, matching the four counts up. She counts them inside. Her hands arrive on her thighs at the exact tempo."

    lthought "Done."

    lthought "The rite is done. I have performed the counting request alone in a base alcove at oh-five-twenty-eight in the morning with three real candles and a folded grey wool cloth and one piece of paper with three lines of text on it that I copied from memory last night."

    lthought "I did not have the witnesses the rite prefers. The rite prefers two witnessing priests. I have no priests left. The witnesses the rite accepted are the three candles and the Six themselves and the silence of the alcove and -- now, as of six seconds ago -- the man in the doorway behind me whose footfall I recognized at four-eighteen when he stopped at the threshold."

    lthought "Aeron is behind me. He has been behind me for approximately two minutes. He has not entered. He has not spoken. He waited for me to finish the rite. That is the thing I did not expect from him this morning."

    lthought "Two months ago he would have interrupted. One month ago he would have cleared his throat at the threshold to signal his presence. This morning he stood still. The stillness is the Marcus training operating at a level I have not seen him reach before. He knows, without being told, that a priest in the middle of a rite cannot be interrupted. He knows it the way Marcus knew it."

    lthought "That is the version of him I am performing this rite to protect against."

    lthought "The protection is already too late for some of it. It is not too late for all of it. I am still going to perform the rite even though it is partial protection, because partial is the unit I have."

    # ========== PHASE 3 -- THE TURN ==========

    "She does not stand yet. The rite specifies that the priest may pause for up to one minute after the closing before standing. The pause is for the Six to withdraw. She uses the pause."

    "Thirty seconds."

    lthought "He is still at the threshold. He has not moved. I can feel the shape of him behind me at the edge of my peripheral field. He is in the corridor light, not in the alcove light. The alcove light has not reached him yet."

    lthought "I am going to turn."

    lthought "I am going to turn now, at oh-five-twenty-nine, and I am going to look at him across the three candles, and I am going to tell him what I just did."

    lthought "He will not understand it for the first half of a breath. Then he will understand it. The understanding is going to happen on his face in real time. I am going to watch it happen because I am the priest who was in the room when I made the decision to carry the counting, and I am the priest who is going to be in the room when he learns that I carried it."

    lthought "I do not get to not-watch that. The rite does not let me not-watch."

    "She turns on her knees. Slowly. The wool cloth permits the turning without her having to move her position on it. She comes around to face the doorway. The three candles are now behind her, between her and the eastern wall. Aeron is in front of her, beyond the threshold."

    "She sees him."

    "He is in the corridor bleed. His hands are at his sides. He is not in uniform -- he is in the grey shirt he sleeps in on nights when he is not briefing, and the outer jacket is over it, unbuttoned. The letter pocket is illuminated by nothing tonight because the alcove has no desk lamp. The letter is invisible in the shadow of the jacket's inside, but she knows it is there because she has known since yesterday what his jacket contains."

    lthought "He came here without the commander's jacket."

    lthought "He came looking for me before he dressed for the briefing. That is the scene I am inside. He came to find me in the gap between private-Aeron and Commander-Aeron, and he found me in the middle of a rite, and he is standing in the threshold in his sleep shirt because he did not know he would need the commander's jacket to be in the room with what I am doing."

    lthought "He is underdressed for this scene. That is a kind of mercy I can give him. I can let him stay underdressed. I do not have to demand the jacket."

    # ========== PHASE 4 -- HIS QUESTION ==========

    "Aeron does not step into the alcove. He stays at the threshold. His voice is low -- the alcove volume, not the corridor volume. He is matching her."

    a "What just happened."

    "The sentence is not demanding. It is Aeron asking a priest for a priest's information. The Marcus training lets him know what kind of question to ask. He is not asking 'what were you doing.' He is asking 'what was that.' The distinction is the distinction between observation and participation. He is asking for participation."

    lthought "He asked the right question."

    lthought "The right question is the one that lets me tell him the truth without having to soften it for his consumption. If he had asked 'are you all right' I would have had to perform the answer. If he had asked 'what were you doing' I would have had to explain the mechanics. 'What just happened' lets me tell him what the rite was, and what the rite means, and the telling is the thing the rite requires me to do now."

    lthought "I am going to tell him. I am not going to soften it. I am not going to euphemize it. The rite does not permit euphemism and I am not going to permit it either."

    l "I asked the Six to count the blessing of Rhea's assassination against me, not against the operator, not against you, not against the act. Against me."

    "The sentence goes across the threshold. Aeron receives it. The clinical precision in his face breaks by half a degree. The half degree is the scene."

    lthought "There it is."

    lthought "I watched it happen. His face did the half-degree thing. I know the half-degree thing from Liora's descriptions of Aeron on the balcony in Act 1. Liora told me once that Aeron's face, when something reached the precision-break threshold, would do a very small thing at the corners of his eyes. The something was not a flinch. It was not an expression change. It was the precision yielding a millimeter of bandwidth to a thing the precision could not metabolize."

    lthought "I have never seen it on him before. I am seeing it now. He is receiving the sentence 'I asked the Six to count the blessing against me' and the precision is yielding a millimeter of bandwidth to it."

    lthought "That is the cost of my telling him. I did not know there would be a cost of telling. I thought telling was a procedural report. It was not. It was a strike on the precision."

    lthought "The rite is going to count that strike against me too. That is correct. The rite accepts strikes on the people the priest loves as part of the counting."

    # ========== PHASE 5 -- HIS SECOND QUESTION ==========

    "Aeron does not move from the threshold. His next word is not a sentence. It is a single word. The word is the Marcus idiom's smallest unit of inquiry."

    a "Why."

    "Not angry. Not pleading. The flat register. Why is a legitimate question from a Commander to a priest who has just performed a rite that involves him. He is asking for the reason because the reason is operationally relevant. He is going to walk into the assassination-prep briefing in ninety minutes and the reason is information he needs before the briefing."

    lthought "He is asking for the reason as a Commander. He is also asking for the reason as a man who is in the doorway in his sleep shirt without his commander's jacket and who came here looking for me."

    lthought "Both Aerons are in the question. I am going to answer both."

    l "Because I cannot let it be counted against you."

    "A beat."

    l "You already have more than a ledger can hold."

    "Her voice is steady. She is not performing emotion. She is stating the theology of the rite as the theology of the rite. The theology is also, at another level, her love for him. She is not going to name the love aloud -- the rite does not require the naming and naming it would dilute the theology. She lets the theology carry the love."

    l "I have the capacity. I am volunteering it."

    lthought "The word 'capacity' is the priest's word. The rite uses it. Capacity is what a priest measures when she decides whether she can carry a weight that is not hers. The priest's ledger has a line for capacity. The line is not mercy. It is load-bearing. Priests know the distinction."

    lthought "I have capacity because I have not spent it yet. I have not performed a counting request for any other sin in my fifteen years as a priest of the Order. I have been told twice by senior priests that I should consider performing one, both times for the same reason -- my own devotional practice had produced a surplus they thought was going to waste. I refused both times because I was saving the capacity."

    lthought "I was saving the capacity for this. I did not know I was saving it for this. I thought I was saving it for some other weight in some other decade. The weight arrived this week. I did not make it up. The capacity had been waiting for this exact shape of weight for fifteen years."

    lthought "I am telling him 'I have the capacity' in a sentence that takes fifteen years of my practice to make true. I am not going to explain the fifteen years to him. He does not need the fifteen years. He needs the sentence."

    # ========== PHASE 6 -- HIS REFUSAL ==========

    "Aeron absorbs the answer. The precision-break is still at the corners of his eyes. It has not widened. It has not closed. He is holding it open."

    "He takes one step into the alcove."

    "One step only. He does not cross to her. He is now inside the alcove light -- the three candles reach the toe of his boot. His face is warmer for the first time. The warmth is not on him. The warmth is the alcove's light falling on the half of his face nearest the candles."

    "He speaks."

    a "I do not want you to do that."

    "The sentence is not a command. The sentence is a preference. It is the first preference OB-Aeron has stated in the whole act in the tense of personal desire. 'I do not want' is not a commander's tense. It is a man's tense. He has used the man's tense in front of her once before -- a2_s14, the corridor after the first shrine. He has not used it since. He is using it now."

    lthought "He used the man's tense."

    lthought "I knew he would. That is why I did the rite before he arrived. The rite is complete. The counting is already mine. I am going to tell him it is already mine, so that the man's tense cannot undo the rite the Commander would have permitted."

    lthought "He is trying to protect me from the rite I just performed. I know why. He loves me in the version of love the OB path has not yet foreclosed. The love is in the man's tense. The man's tense is what he came here in the sleep shirt to offer me. I am going to refuse the offer, and the refusal is not going to be cold, because the refusal is the rite's terms and the rite's terms are my terms."

    l "You do not get to stop me."

    "She says it without heat. The sentence is the rite speaking through her, not her speaking over the rite."

    l "The ritual is already done."

    l "I am the one who carries this now. You still have to live with the doing. That is yours. The counting is mine."

    # ========== PHASE 7 -- HIS THIRD WORD ==========

    "Aeron does not speak immediately. His hands are still at his sides. His fingers have not closed. The not-closing is deliberate -- he is keeping his hands open because closing them would be a performance of refusal and he is not going to perform refusal, he is going to say the word and let the word be the refusal."

    "The word is her name."

    a "Lyra."

    "One word. It is the OB path's equivalent of a protest. The whole of what his tense can afford."

    lthought "He said my name."

    lthought "He said my name the way a man says the name of a woman when he is trying to stop her from doing a thing she is already doing and when the stopping has already failed. The stopping fails inside the saying of the name. The name is both the attempt and the concession."

    lthought "I am going to finish the answer. I am going to finish it the way the rite finishes answers. The rite uses a specific phrase in the Aerenine closing register -- not the Old Tongue, the everyday register -- and the phrase is a way of naming that the priest is not leaving and that the naming is not a sacrifice."

    lthought "The phrase exists because priests are accused of sacrifice often enough that the rite had to develop a refusal of the accusation."

    lthought "I am going to use the phrase."

    l "I am not leaving."

    "A beat."

    l "This is not a sacrifice. This is me deciding what my devotion means in a room this dark."

    l "My devotion means that if I cannot stop you, I can take the counting."

    # ========== PHASE 8 -- THE STATEMENT LANDS ==========

    "The alcove holds the sentence."

    "The three candles do not flicker. The corridor behind Aeron has gone silent -- the morning cycle's bootfall paused for the duration of Lyra's line, as if the base itself declined to intrude on the alcove while she was speaking. That is not coincidence. Aeron registers the silence. He registers that the base has given them a window."

    lthought "The base is quiet. The base is quiet because the corridors are empty for a thirty-second window and nobody is coming. I did not arrange it. The rite arranges its own silence around the priest who is performing it. I have seen it before -- once at the cathedral, twice at the Order's retreat house in the hills. The silence is part of the rite's efficacy."

    lthought "The silence is holding the scene while Aeron decides what he is going to do."

    "Aeron looks at her."

    "He does not speak. His face is doing the precision-break thing at the corners still. It is not getting worse and it is not getting better. It is staying at the half-millimeter opening, which is the largest opening his precision has produced in the whole act."

    lthought "He is going to do something."

    lthought "I do not know what. The rite does not specify what a lover does after a counting request. The rite was written for institutions, not for lovers. The lover part is what we are going to have to improvise."

    # ========== PHASE 9 -- THE KNEELING ==========

    "Aeron takes two more steps. He is now at the edge of the wool cloth. The candles are at his feet."

    "He lowers himself to his knees."

    "He does not drop. He kneels the way an operator kneels when the operator has been trained to lower the body slowly so that the body's movement does not reveal the direction of the next action. It is a controlled kneel. The control is the tell -- he is not kneeling out of impulse, he is kneeling out of precision, but the precision has allowed the kneeling to happen, which is the thing the precision has not allowed all act."

    "He does not touch her."

    "He puts his forehead on her knees."

    "The contact is the forehead and the tops of her thighs through the thin fabric of her kneeling robe. His hair against her skirt. The pressure is the pressure of a head that has stopped holding itself up and has agreed to be held by the first surface that accepted the agreement."

    lthought "He is on my knees."

    lthought "His forehead is on my knees and his hands are at his sides and the candles are burning beside us and the rite is already counted against me and he is not saying anything."

    lthought "He is letting the position be the whole of what he is doing. He is not converting the position into a request. He is not converting it into a confession. He is not converting it into a prayer -- he has not prayed in six years, I know because I asked him in Act 1 and he told me the last prayer was the one over his father's field command."

    lthought "He is just kneeling."

    lthought "And I -- I am deciding in real time whether to put my hand on his head."

    lthought "The rite would permit the touch. The rite would permit the touch as a blessing, as a counting-witnessing, as a priest's acknowledgment of a petitioner. The rite has a line for it."

    lthought "I am not going to touch him."

    lthought "I am going to let him kneel without touching him because the not-touching is the shape of the rite's honesty about what is happening. The rite has already claimed the counting. If I touch him now, the touch becomes a trade. I give him the comfort of the hand and he gives the counting back to the rite through the closing of the exchange, and the rite's efficacy decays by the half-millimeter the precision opened."

    lthought "I do not get to have the hand. That is the cost."

    lthought "I am not going to perform the cost as pain. I am going to perform it as stillness."

    # ========== PHASE 10 -- THE HOLDING ==========

    "Lyra does not move her hands from her thighs. Her palms are still down -- she closed the offering at the end of the rite and her palms have remained down since then. Her hands are beside Aeron's head, not on it. The distance between her hands and his head is approximately two centimeters. The two centimeters are the whole of what the rite is asking her to refuse."

    "She does not flinch."

    "She does not touch him."

    "She lets him kneel."

    "The alcove holds them. The three candles continue their triangle breathing. The corridor beyond the threshold has not resumed its bootfall -- the window has not closed yet. The Six, in whatever configuration the rite has invoked them in, are witnessing."

    lthought "The Band is at my wrist."

    lthought "I am aware of the Band because the Band is the physical correlate of the rite. The Band is cinched past comfort and it has been cinched past comfort since a4_s04 and it is not going to be loosened this morning. The rite specifies that the priest who has made a counting request cannot loosen her discipline in the hour following the request. The hour is the Six's consideration window. The Band stays tight through the window."

    lthought "I am not going to loosen it when he stands up. I am not going to loosen it at the departure briefing. I am not going to loosen it until Rhea Vestin is dead and the counting has been delivered to the Six and the Six have confirmed the delivery through some private sign that I will recognize when I receive it."

    lthought "The Band is the shape of the counting on my body."

    lthought "Aeron is on my knees. My hands are at my sides. My palms are down. The Band is at my wrist. The counting is mine. The doing is his. The kneeling is what his body is permitting itself to do inside the permission my refusal-to-touch is giving it."

    lthought "I am being a priest right now in a way I have not been a priest since the novitiate."

    lthought "The novitiate taught me the distinction between compassion and efficacy. Compassion touches. Efficacy withholds. A priest learns, over years of practice, when withholding is the mercy and when touching is the mercy. The novitiate uses the phrase: the hand you do not extend is sometimes the hand the Six require."

    lthought "I have the hand the Six require right now. The hand is at my side. I am keeping it there. The keeping is the priest-work."

    # ========== PHASE 11 -- THE QUIET ==========

    "The kneeling holds for a span the scene does not count."

    "Aeron does not speak. Lyra does not speak. The candles do not speak. The corridor behind them does not speak. The base does not speak."

    "The only thing happening in the alcove is the breath of the man who has put his forehead on the knees of a woman who is not going to touch him, and the breath of the woman whose palms are down at her sides and whose Band is tight at her wrist and whose counting has been accepted."

    "Aeron's breath does something small."

    "It is not a sob. OB-Aeron does not sob. It is a single exhale that is three beats longer than the last exhale was. Three beats. The extension is the entirety of what his body is permitting itself to do in the presence of the rite."

    lthought "Three beats longer."

    lthought "That is the whole of his grief in this scene. Three beats of exhale. I am the only one in the base who would have counted those beats. I am counting them because counting is what I am here to do."

    lthought "I am counting the three beats into the ledger of the counting-request. The rite does not require me to count Aeron's grief inside the petition, but the rite permits it, and I am permitting it myself, because his grief is part of the weight I volunteered to carry, and because refusing to count it would be a separate cruelty."

    lthought "Three beats. I am counting them. The Six are witnessing the count."

    # ========== PHASE 12 -- THE LIFT ==========

    "Aeron lifts his head from her knees. The lift is as controlled as the kneeling was. He does not pull away -- he rises, rocks back on his heels, and stands in one continuous motion that suggests a body that has been drilled in standing-up-from-a-kneel under tactical conditions."

    "He does not meet her eyes yet. He takes a breath -- the normal length this time, not the three-beat one -- and he speaks the fourth and final spoken word of the scene."

    a "All right."

    "Two syllables. Not approval. Not acceptance. An acknowledgment. The acknowledgment is that the rite is done and the counting is hers and he is not going to try to undo what he cannot undo and the not-trying is the last thing he is going to offer her before the departure briefing in seventy-three minutes."

    "He meets her eyes."

    lthought "He is looking at me now."

    lthought "The precision-break at the corners is still at the half-millimeter. He has not closed it. I do not know if he can close it. I do not know if the closing is going to happen during the briefing or during the walk to the vehicle bay or during the first kilometer of the drive to the staging point or during the fifth day of the prep or during the moment of the shot on day seven."

    lthought "I do not know when he will close it and I do not know what closing it will cost him. I know that the closing is going to happen and that whichever day it happens, the cost is going to be metabolized by the counting I volunteered for this morning. That is the arithmetic."

    lthought "He is leaving."

    lthought "He is going to turn and walk out of the alcove and go to the briefing and wear the commander's jacket and the letter in its pocket and the pocket is going to get heavier because the letter is still a gravestone and he refused to convert it last night and I am the priest whose counting is going to catch the weight the pocket can no longer hold."

    lthought "That is the whole of what I am offering him this morning."

    lthought "It is not enough. It is what I have."

    # ========== PHASE 13 -- HE LEAVES ==========

    "Aeron does not say anything else. He turns, not abruptly, and walks out of the alcove. He reaches the threshold. He stops there for a half-second -- the same stop Lyra uses at the end of the sixth-fold sign, the priest's half-beat -- and then he crosses the threshold and is gone into the corridor."

    "His bootfall recedes. Ten steps. Twenty. The corridor silence that the rite had imposed has broken -- bootfall has resumed somewhere further down the corridor, the morning cycle is back in its normal cadence. The base is awake. The window is closed."

    "Lyra is alone in the alcove."

    "The three candles. The folded grey wool. The clay bowl. The paper with the three lines. The Band at her wrist."

    lthought "I did it."

    lthought "I performed a counting rite alone in a base alcove at oh-five-thirty on the morning of the departure for an assassination operation I did not authorize and could not prevent. The rite is accepted. The counting is mine."

    lthought "I am going to stand in one minute. I am going to extinguish the candles in the correct order -- Solen first because Solen is the weight-between, Veran second because Veran is the steady-hand, Anayet last because Anayet is the becoming and the becoming is the last thing the rite releases. The order matters. The rite checks the order."

    lthought "I am going to roll the wool cloth and put the clay bowl in the footlocker beside my cot and burn the paper with the three lines so that the physical text does not persist. The rite requires the text to be burned because a counting-request text is not meant to outlive the request."

    lthought "Then I am going to go to the departure farewell at oh-seven-thirty. I am going to stand at the edge of the base with the other commanders. I am not going to speak. I am not going to bless. The operators have already been blessed for this one in a separate rite that the muster officer performed yesterday -- she did not ask me to do it this time. I am relieved. I am also aware that my not being asked is a kind of demotion inside the base's informal priest hierarchy."

    lthought "I am the priest who carries the counting for the command. I am not the priest who blesses the outgoing weapon. The two roles cannot be held by the same priest. The Order's texts are clear on this. I have moved from one role to the other in the course of Act 4."

    lthought "The demotion is a promotion to a different ledger."

    lthought "I am going to live inside the new ledger now."

    lthought "The Band stays cinched."

    # ========== PHASE 14 -- THE HOLD ==========

    "The camera holds on Lyra alone in the alcove."

    "The three candles in their triangle. The priest on her knees on the grey wool. Her hands at her sides, palms down. The Band at her right wrist, visible above the cuff of the robe, cinched past comfort. The paper with the three lines of Old Tongue text on the cloth beside the clay bowl. The corridor beyond the threshold carrying the distant bootfall of the base's morning cycle."

    "She does not move."

    "She is going to move in a minute. She is going to extinguish the candles and roll the cloth and put the bowl in the footlocker and burn the paper. The scene is not going to follow her into the doing. The scene is going to leave her in the alcove in the held position, because the held position is the thing the scene was for, and the doing afterward is administration."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1, conflict=1)
    $ canon_set("ob.lyra.accepted_the_counting", True)
    $ canon_set("ob.lyra.counting_request_performed_alone", True)
    $ canon_set("ob.lyra.has_moved_from_blessing_to_counting_role", True)
    $ canon_set("ob.aeron.kneeled_once_in_the_alcove", True)
    $ canon_set("ob.aeron.used_mans_tense_second_time_in_ob_path", True)
    $ tp_seed("a4.ob.lyra.counting_is_mine")
    $ flag("ob_lyra_carried_the_counting_for_rhea_assassination", True)
    $ flag("ob_aeron_precision_break_at_half_millimeter", True)
    $ npc_remember("Lyra", "performed_counting_rite_three_candles_alone", tone="devotion_corruption_apex")
    $ npc_remember("Lyra", "refused_to_touch_him_when_he_knelt", tone="priest_withholding_as_mercy")
    $ npc_remember("Lyra", "fifteen_years_of_capacity_spent_on_one_counting", tone="the_weight_she_was_saving")
    $ npc_remember("Aeron", "knelt_forehead_on_her_knees_three_beat_exhale", tone="ob_precision_first_break_of_act")
    $ npc_remember("Aeron", "said_i_do_not_want_you_to_do_that", tone="mans_tense_in_sleep_shirt")
    $ metric("ob.lyra.devotion_corruption_index", set_to=4)
    $ metric("ob_lyra_band_still_cinched_past_comfort", add=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s25_lyra_at_the_altar_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.chapter_end: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Oh-five-twenty-eight on the morning of the assassination-prep departure.
#   - Lyra has been in the alcove since 0445. Aeron arrived at approximately 0518
#     and waited at the threshold without interrupting while she performed the
#     closing of the counting rite.
#   - Seventy-three minutes before the departure farewell (s26).
#   - Just under five hours after the Nyra pitch (s24).
# cann.what_happened:
#   - Lyra performs the Old Tongue counting-against-the-priest rite alone in the
#     altar alcove. The rite is a priest's petition to the Six to count a sin
#     against the priest personally rather than against the act, the operator,
#     or the commander. The sin she is volunteering to carry the count of is
#     the blessing of Rhea Vestin's assassination, which will occur in seven days.
#   - The rite uses three candles (the Six halved -- Anayet, Veran, Solen, the
#     three whose domains include weights), a folded grey wool cloth, a clay
#     bowl, and a paper with three lines of Old Tongue text she copied from
#     memory the night before. The rite has seven phases. Lyra performs all
#     seven alone, without the two witnessing priests the rite prefers, because
#     no other priests are left in the base.
#   - Aeron enters during the closing of the rite. He came looking for her in
#     his sleep shirt and the outer jacket, not the commander's jacket. He waits
#     at the threshold without interrupting -- the Marcus training teaching him
#     when a rite cannot be interrupted.
#   - Lyra turns and tells him what the rite was: "I asked the Six to count the
#     blessing of Rhea's assassination against me, not against the operator,
#     not against you, not against the act. Against me." Aeron's precision
#     breaks by a half-millimeter at the corners of the eyes -- the first
#     precision-break of the OB Act 4 arc.
#   - Aeron asks "Why." Lyra answers "Because I cannot let it be counted
#     against you. You already have more than a ledger can hold. I have the
#     capacity. I am volunteering it." (The capacity is fifteen years of
#     priest-practice she was saving without knowing she was saving it.)
#   - Aeron refuses: "I do not want you to do that." (The man's tense -- only
#     the second time OB-Aeron has used the personal-desire register in the
#     whole act.) Lyra refuses the refusal: "You do not get to stop me. The
#     ritual is already done. I am the one who carries this now. You still
#     have to live with the doing. That is yours. The counting is mine."
#   - Aeron says her name -- "Lyra" -- as the OB path's equivalent of a protest.
#     Lyra finishes the answer: "I am not leaving. This is not a sacrifice.
#     This is me deciding what my devotion means in a room this dark. My
#     devotion means that if I cannot stop you, I can take the counting."
#   - Aeron walks into the alcove and kneels. He puts his forehead on her knees.
#     This is the scene's single moment of physical contact. He does not touch
#     her with his hands -- his hands stay at his sides. She does not touch him
#     with her hands -- her hands stay at her sides, palms down, the distance
#     between her hands and his head approximately two centimeters. The
#     not-touching is canonical. The rite specifies that the priest who has
#     made a counting request cannot convert the rite into a comfort exchange.
#     Lyra is refusing the touch as priest-work.
#   - Aeron's breath does a single three-beat-longer exhale. That is the whole
#     of his grief in the scene. Lyra counts the three beats into the ledger
#     of the counting-request as an additional weight she is carrying.
#   - Aeron stands (controlled operator-kneel reverse), says "All right" (two
#     syllables of acknowledgment, not approval), and leaves the alcove. He
#     does not look back at the threshold half-beat.
#   - Lyra alone. She will extinguish the candles in the correct order (Solen,
#     Veran, Anayet), roll the cloth, burn the paper, and go to the departure
#     farewell at 0730. She is no longer the priest who blesses the outgoing
#     weapon (the muster officer did not ask her this time). She is the priest
#     who carries the counting. The two roles cannot be held by the same
#     priest in the Order's texts. She has moved from one to the other across
#     the course of Act 4.
#   - The Band stays cinched past comfort. She will not loosen it until the
#     assassination is complete and the Six deliver the private sign that
#     confirms the counting has been received.
# cann.lyra_state:
#   - Devotion corruption index set to 4 -- the apex of the Act 4 arc. She has
#     moved from blessing the outgoing weapon (s14) to carrying the counting
#     of the sin (s25). The counting is the maximum load the Order's rite
#     permits a priest to volunteer for without Senior Priest authorization.
#     She does not have Senior Priest authorization. She performed the rite
#     anyway. This is canonical -- it is not a procedural violation per se,
#     but it is the act of a priest operating at the edge of her own
#     authority without institutional oversight.
#   - The capacity she spent this morning is the capacity she has been saving
#     for fifteen years. Two senior priests told her, separately, that her
#     devotional practice had produced a surplus she was not using. She
#     refused both invitations to spend it on other weights. She was saving
#     it without knowing what for. The weight arrived this week.
#   - Refuses the physical touch that would have converted the rite into a
#     comfort exchange. The novitiate taught her: "the hand you do not extend
#     is sometimes the hand the Six require." She has the hand the Six require
#     this morning and she keeps it at her side.
#   - The Band stays cinched. The cinching is now the physical correlate of
#     the counting, not of the earlier blessing-the-outgoing-weapon discipline.
#     The Band has moved with the ledger.
#   - Has been demoted inside the base's informal priest hierarchy (the muster
#     officer did not ask her to bless this strike). The demotion is a
#     promotion to a different ledger.
# cann.aeron_state:
#   - First precision-break of the OB Act 4 arc. The break is at the half-
#     millimeter threshold Liora described in Act 1. It opens at the corners
#     of his eyes when Lyra tells him what the rite was and does not close
#     before he leaves the alcove.
#   - Used the man's tense ("I do not want you to do that") for only the second
#     time in the OB path (the first was a2_s14 corridor after the first
#     shrine). The man's tense is not a commander's tense. It is personal
#     desire. He used it in a sleep shirt, without the commander's jacket,
#     before the briefing.
#   - The controlled operator-kneel. He did not drop. The kneeling was precise.
#     The precision permitted the kneeling to happen, which is the thing the
#     precision had not permitted all act.
#   - The three-beat exhale. Lyra counted it. This is the first ledgered grief
#     of Aeron's OB Act 4 arc. It is counted into the counting-request as an
#     additional weight.
#   - Said "All right" and left. Not approval. Acknowledgment. He is not going
#     to try to undo what he cannot undo.
# cann.path_tracking_mechanics:
#   - rel_bump Lyra trust=1 conflict=1. Trust because she revealed the rite to
#     him. Conflict because the revelation is a weight he did not want her to
#     take on.
#   - canon_set ob.lyra.accepted_the_counting True.
#   - canon_set ob.lyra.counting_request_performed_alone True.
#   - canon_set ob.lyra.has_moved_from_blessing_to_counting_role True.
#   - canon_set ob.aeron.kneeled_once_in_the_alcove True.
#   - canon_set ob.aeron.used_mans_tense_second_time_in_ob_path True.
#   - tp_seed a4.ob.lyra.counting_is_mine.
#   - flag ob_lyra_carried_the_counting_for_rhea_assassination True.
#   - flag ob_aeron_precision_break_at_half_millimeter True.
#   - metric ob.lyra.devotion_corruption_index set to 4 (apex).
# cann.thematic_flags:
#   - The counting ritual as the apex of Lyra's OB arc. She cannot stop the
#     operation. She cannot refuse to be in the room. She can volunteer to
#     carry the ledgered weight of the sin so that Aeron does not have to
#     carry it to the Six. The volunteering is the only form of mercy the
#     rite permits her to offer.
#   - The not-touching. The two-centimeter gap between Lyra's hand and
#     Aeron's head is the physical correlate of the rite's efficacy rule.
#     Touching would decay the rite. Not-touching preserves it. The
#     not-touching is canonical.
#   - The precision-break. OB-Aeron's clarity yielding half a millimeter of
#     bandwidth to the information that Lyra has volunteered to carry his
#     sin. The break does not close inside the scene. It carries forward
#     into s26 (the act close) and into Act 5.
#   - The Band. Still cinched past comfort, now as the physical correlate
#     of the counting rather than of the blessing. The Band has moved
#     ledgers.
#   - The demotion-as-promotion. Lyra has moved out of the blessing role
#     and into the counting role. The two roles cannot be held by the
#     same priest. The move is permanent.
# cann.character_moments:
#   - Lyra: the apex of her OB arc. The counting rite performed alone. The
#     refusal to touch Aeron when he kneels. The statement of her devotional
#     position in the new ledger: "My devotion means that if I cannot stop
#     you, I can take the counting."
#   - Aeron: the kneeling. The forehead on the knees. The three-beat exhale.
#     The "I do not want you to do that" in the man's tense. The "All right"
#     as acknowledgment. The first precision-break of the OB Act 4 arc.
# cann.callbacks:
#   - a4_s04 (Band cinched past comfort): the notch has not been loosened.
#     The Band has persisted across s04, s14, s25.
#   - a4_s14 (blessing the outgoing weapon): s14 was Lyra blessing the going.
#     s25 is Lyra counting against the going. The arc from blessing to
#     counting is the Act 4 OB Lyra arc.
#   - a3_s19 (Anayet / Seren): the Old Tongue register used in the counting
#     rite is the same register Lyra used in s19. The rite-trained voice.
#   - a2_s14 (corridor after the first shrine): first time OB-Aeron used
#     the man's tense. S25 is the second time. The two occurrences are
#     the only occurrences in the OB path to date.
#   - a1_s07 (Liora on the balcony, precision-break description): Liora
#     told Lyra, in Act 1, what Aeron's precision looked like when it
#     yielded a half-millimeter. s25 is the first time Lyra sees it
#     herself. The callback is Lyra's internal identification of the
#     half-millimeter from Liora's description.
#   - a4_s24 (the mirror / Nyra doctrinal offer): Nyra deferred the next
#     conversation via the pocket-weight metric. s25 confirms the pocket
#     is still heavy because Aeron did not take Nyra's framing. The
#     alcove scene is Lyra addressing the same weight Nyra's pitch
#     tried to redistribute.
# cann.block_status:
#   - ANCHOR (OB). State beat / devotion corruption apex. No player choice.
# cann.requires_followup:
#   - Lyra's counting is load-bearing for the rest of the OB path. Any OB
#     scene in Act 5 must account for the fact that Lyra is carrying the
#     counting. Her Band discipline is no longer about the blessing -- it
#     is about the counting, and the counting's resolution is gated on the
#     assassination's completion and the Six's private sign.
#   - The precision-break at the corners of Aeron's eyes is now a canonical
#     state. Act 5 scenes should track whether the break closes, widens,
#     or stabilizes. If it widens, the OB path may become unstable. If
#     it closes, the OB thesis has metabolized the Lyra counting into
#     the clarity. If it stabilizes, Aeron is carrying a half-millimeter
#     of acknowledged cost into every subsequent scene.
#   - The Old Tongue counting rite should be referenced by Lyra, once, in
#     a late Act 5 scene if the assassination succeeds. She will need
#     to perform the receipt rite when the Six deliver their sign. The
#     receipt rite is the rite's closing.
#   - Aeron's "I do not want you to do that" in the man's tense is a
#     carry-forward for any Act 5 scene where the OB Aeron's personal
#     register is permitted to surface.
#   - Lyra has moved out of the blessing role in the base's informal
#     priest hierarchy. Future Act 5 muster scenes must account for this
#     -- she is no longer the priest who blesses outgoing strikes. A
#     different priest will need to be named, or the role will be empty.
