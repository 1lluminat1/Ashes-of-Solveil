# =======================================================
# ACT 4 - Scene 16: Tessa Fracture Point (Obedience Path)
# File: a4_s16_tessa_fracture_point_ob.rpy
# Path: OB
# Type: TESSA STATE BEAT (non-erotic, conditional on Act 3 s10 apology flag)
# Character Focus: Tessa, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s16_tessa_fracture_point_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s16_tessa_fracture_point_ob:
    $ show_timeline("33rd of Forge, 390 A.C.", "02:47", "Phoenix Base — Ops Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. OB economic register. No handheld.
    #         Opens on the ops table in close-up -- an empty surface, tactical
    #         displays cycling in the background, blue light on dull metal.
    #         Tessa's hand enters the frame first. She sets the OPERATIONAL
    #         header down on the table. The camera holds on the strip of
    #         adhesive plastic. It stays there the entire scene.
    #         Cut to a two-shot only once, at the question. Tessa standing.
    #         Aeron seated. The header between them.
    #         The camera does not track Tessa's exit. It holds on Aeron
    #         and the strip of plastic. The last beat is the plastic, not the face.
    # LIGHTING: Ops room after hours. Blue-cold. Nyra's display wall cycling
    #           patrol grids in a slow loop. One desk lamp at Aeron's station.
    #           The strip of adhesive plastic catches the blue from the
    #           displays -- the word OPERATIONAL reads cold regardless of angle.
    #           No practicals warm. No amber. The ops room has been scrubbed
    #           of the old base's warmth the way the medwing was built to be.
    # SFX: Loop -- display wall hum, HVAC in a lower register than the new
    #      medwing, distant boot traffic in the corridor. The ops room is
    #      never fully silent.
    #      One-shots -- the plastic strip landing on metal (a small click,
    #      clean, definitive). Tessa's boots (quiet, controlled). The chair
    #      under Aeron (no creak -- the ops chairs are new). The door
    #      seal on her exit. The HVAC re-balancing once after the door closes.
    # FX/COMP: Ops room, 0247. Displays cycling. An empty coffee mug on
    #          Aeron's station. A closed tactical binder. The OPERATIONAL
    #          header -- a three-inch strip of adhesive plastic, the underside
    #          still tacky from the board. The marker ink reads clean on the
    #          front; the back is dusted with fragments of THE LIVING in
    #          Tessa's hand, pulled off with the overwrite.
    # BLOCKING: Tessa enters the ops room through the main door. She does not
    #           pause. She walks the length of the room to Aeron's station.
    #           She does not sit. She sets the plastic strip on the table
    #           six inches from his hand. She does not let go of it until
    #           it is flat on the surface. Then she steps back to a standing
    #           position at the short end of the table. The table is now
    #           between them. The header is between them.
    #           At the end of the scene: she leaves by the same door. She
    #           does not look back. Aeron does not stand. He does not move
    #           the header. He does not reach for it. He does not wipe it
    #           off the table. The scene ends with the strip of plastic
    #           where Tessa set it down.
    # CANON: Three nights after s06 board overwrite. Tessa has not slept.
    #        She went back to the medwing tonight, peeled the OPERATIONAL
    #        strip off the board (it was adhesive plastic -- intentionally
    #        removable by whoever put it there), and walked it to the ops
    #        room. Aeron is working late on Stelker's intake logs.
    #        The scene is the confrontation he has been bracing for since
    #        she left the bag on the supply cart.
    # FACE: Tessa -- no sleep shadows performed for effect; the exhaustion
    #        is structural. Her voice steady. Her hands steady. She has
    #        made the decision before entering the room and the decision
    #        is what the scene delivers, not the argument.
    #        Aeron -- does not flinch at the header. Does not reach to
    #        move it. Marcus-idiom stillness. His answer to her question
    #        is unflinching because flinching would be a lie he has run
    #        out of stamina to tell.

    # ========= VOICE BASELINE =========
    # Tessa: direct, no preamble. The voice of someone who has already
    #        finished the internal argument and is now reporting the result.
    #        Declarative. The cadence of triage completed.
    # OB Aeron: competent in Marcus idiom. He does not soften. He does not
    #           explain. He answers the question she asked with the answer
    #           that is true.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - OPERATIONS ROOM - 0247]
    # Ops room after hours. Nyra's display wall cycling patrol grids.
    # One desk lamp at Aeron's station. Blue-cold.

    #scene bg_ops_room_ob_night with dissolve
    #play ambient "sfx/ambient/ops_room_hvac.ogg" fadein 2.0

    # ========== PHASE 1 -- ENTRY ==========

    "0247. The ops room runs cool at this hour. The display wall cycles patrol grids in a slow blue loop. Aeron is at his station, working Stelker's rotation conflict into a formatted intake reconciliation."

    "The main door seals."

    athought "Someone came in. I do not look up. I do not have to."

    "Tessa walks the length of the ops room. Her boots make the sound of boots that have been on for nineteen hours. She does not pause at the threshold and she does not pause at the table edge."

    "She stops at his station. She does not sit."

    "Her right hand comes up. There is a strip of adhesive plastic in it, three inches long, black marker on the front face. She sets it on the table six inches from his hand. She does not let go until it is flat on the surface. Then she steps back to the short end of the table."

    "The plastic strip reads OPERATIONAL."

    "The underside is tacky. The edges are feathered with tiny fragments of another handwriting -- the residue of THE LIVING, which came up with the overwrite when she peeled it."

    tthought "I peeled it with my fingernail. I started at the upper right corner and I worked the strip off in one piece. It came up cleaner than I expected. Whoever put it there used a removable adhesive. That was their kindness to themselves. They wanted to be able to revise."

    # ========== PHASE 2 -- NO PREAMBLE ==========

    "She does not say hello. She does not say she has not slept. She does not say the wing was quiet when she went back for it. She has prepared exactly one sentence and she says it once."

    t "Someone did this."

    a "I see it."

    t "I do not need you to say who."

    "A beat. His eyes on the strip. Not on her."

    t "I need you to tell me whether you are the one who authorized it."

    athought "She came here with one question."

    athought "She is not going to ask it twice."

    athought "The honest answer has two parts."

    # ========== PHASE 3 -- THE BRANCH ==========

    if flag("tessa_thread_open"):
        jump a4_s16_tessa_fracture_point_ob_stayed
    else:
        jump a4_s16_tessa_fracture_point_ob_withdrew


# ==================================================================
# BRANCH A -- STAYED / APOLOGIZED IN ACT 3 S10
# ==================================================================
label a4_s16_tessa_fracture_point_ob_stayed:

    # ========== PHASE 4A -- THE ANSWER ==========

    "Aeron looks up. The eye contact is the first thing he has given her since she walked in."

    a "I did not write it."

    "She does not react. She is waiting for the rest."

    a "I did not stop it. I knew it was there. I walked into the wing three nights ago and I saw it. I read it once. I chose not to correct it. That is the same thing as authorizing it. I will not pretend it is not."

    "He does not look away."

    a "The answer to your question is yes. I authorized it by not stopping it. The shorter answer would be a lie."

    tthought "He did not flinch when he said that."

    tthought "A month ago he would have flinched. I would have seen the tremor. I am watching his hand right now. It is flat on the table next to the strip. It is not shaking."

    tthought "That is information."

    # ========== PHASE 5A -- ABSORB ==========

    "Tessa holds the answer in her body for six seconds. She does not sit. She does not soften her posture. She does not move her hands."

    "She is running the triage the way she ran it at the board three nights ago. The same interior procedure. The same refusal to rush a calculation that needs to be slow."

    tthought "He told me the truth. I asked for it. He gave it to me. I have no grievance about the answer. The answer was honest."

    tthought "The problem is not the answer. The problem is that the man who gave me the answer is not the man I apologized my way back to in the medbay."

    tthought "That man would have flinched."

    tthought "This man is competent in a vocabulary I do not recognize and he is telling me the truth inside that vocabulary and the truth fits the vocabulary exactly."

    tthought "I am not going to save him from this room tonight. I could not save him from this room on any night. That was always the wrong question."

    tthought "The right question is what I do now that I know."

    # ========== PHASE 6A -- THE ONE QUESTION ==========

    "She exhales once. It is not a sigh. It is the small adjustment a triage nurse makes before the next step in a protocol."

    t "I need to ask you one question."

    "He does not speak. He waits."

    t "If I stop counting tomorrow, will anyone else count?"

    athought "She is asking whether the board continues without her."

    athought "She is asking whether the ritual has an heir."

    athought "I have known the answer to this for weeks."

    a "No."

    "He says it flat. No softening. The word is the word."

    a "No one else is keeping a board. No one else has the training to read the count the way you read it. No one else has the standing to write the names. If you stop, the count stops."

    a "Nyra's coordinators will take the board down inside the month. They will cite the fire inspection. They will be technically correct."

    a "The names will disappear from the wall. Some of them will be in the intake logs. Some of them will not. The ones that are not in the logs will disappear from the record entirely."

    a "If you stop counting, no one else counts."

    tthought "He said it without flinching. He said it the way he gave me the other answer. He is not trying to keep me on the board. He is telling me what is true."

    tthought "That is worse than if he had tried to keep me."

    tthought "It is also the thing I needed to hear."

    # ========== PHASE 7A -- THE DECISION ==========

    "Tessa's hands are at her sides. Her coat is still on. She has not taken it off since she walked in."

    "She takes three seconds to assemble the sentence. It is not a speech. It is a protocol she is writing into the air so that she will hear it in her own voice and be bound by it."

    t "Then I will keep counting."

    "Pause."

    t "I will not let them make it easy."

    "She looks at the plastic strip on the table. Her eyes go to it and back to his face. The look is a citation."

    t "I will write LIVING back on my board every morning that they write OPERATIONAL. I will write it in my hand. I will write it in marker they cannot peel. I will write it above the overwrite if I have to. I will write it under the overwrite if they take marker off the supply cart. I will write it on the flat of my own hand if they take the board down."

    t "I will keep leaving the lamp in the room when I go. Every shift. On my way out. I will click it off and I will leave it clipped to the top of the board. If they move the lamp, I will bring a new lamp. If they take the lamp, I will leave my coat. If they take the coat, I will leave a chart with my handwriting on it. There will always be something of mine in that wing that they did not authorize and that they cannot paperwork into OPERATIONAL."

    t "They will not make me quiet. I am going to be inconvenient in the shape my care can take. That is the shape I have left."

    tthought "I am not going to cry. I am not going to ask him to be different. I am not going to argue the word OPERATIONAL. I am going to write LIVING on my board every morning they write OPERATIONAL on top of it and I am going to outlast the ink."

    tthought "The calculation I ran at the board three nights ago had three options. Option three was stopping. I picked option three for one night only. Tonight I am revising the protocol. Tonight I am picking option four."

    tthought "Option four is the option that did not exist three nights ago. Option four is that I count anyway, out loud, on a board that is not mine, inside a wing that is not mine, under a header that is not mine. I count anyway. That is the fourth option. I did not have it three nights ago because I was trying to pick an option that would not cost me anything. This one will cost me everything and I am going to pick it on purpose."

    # ========== PHASE 8A -- AERON'S RESPONSE ==========

    "Aeron has not moved. His hand is still flat on the table next to the strip."

    athought "She is telling me what she is going to do."

    athought "She is not asking my permission. She is not negotiating. She is not requesting resources or protection or cover."

    athought "She is reporting the decision. The way a medic reports a triage outcome to command. That is the cadence of it."

    athought "A month ago I would have said 'thank you.'"

    athought "I am not going to say 'thank you.'"

    athought "'Thank you' from me, in this room, at this hour, with that strip on the table, would be the worst thing I could do to her."

    athought "She did not come here to be thanked. She came here to tell me the thing she needed me to hear. If I thank her I am converting her resistance into service to me, and that is the exact conversion the word OPERATIONAL has been performing on everything else in this base for two months. I will not do it to her with my own mouth."

    "He says nothing."

    "Tessa reads the silence. Correctly. She nods, once. Barely a nod -- the small acknowledgment a medic gives a patient whose vitals are stable enough to release."

    t "Good."

    "One word. It is not warm. It is not cold. It is an operational report."

    # ========== PHASE 9A -- THE EXIT ==========

    "She does not take the strip back. The strip stays where she put it."

    "She does not touch his hand. She does not reach across the table. She does not give him the benefit of a closing gesture."

    "She turns."

    "Her boots on the ops room floor. Nineteen hours on her feet and the gait is still controlled. She walks to the main door. Badge tap. Seal breath."

    "She does not look back."

    "The door closes."

    athought "She walked out of my ops room on her own terms, using my ops room door, with my ops room badge access, past my ops room display wall, after reading me the protocol she intends to run inside the institution I built."

    athought "She did not leave angry. She left decided. Those are different."

    athought "If she had left angry I could have done something with it. Decided gives me nothing to do."

    athought "Decided is what I used to be."

    # ========== PHASE 10A -- THE HEADER STAYS ==========

    "Aeron does not move the strip of plastic. He does not pick it up. He does not fold it. He does not slide it into a drawer. He does not wipe the tacky underside off the table."

    "He looks at it for a long time."

    athought "She brought it to me on purpose. She did not bring it to Nyra. She did not bring it to the coordinator who wrote it. She did not bring it to Lyra. She brought it here and she set it down between us and she asked me the one question that made the answer matter and I gave her the answer and she made her decision in front of me."

    athought "She is counting LIVING tomorrow."

    athought "The strip stays on my table tonight."

    athought "If I move it I am doing her the favor of tidying after her. I am not going to do her that favor. She did not ask for it. She came here to leave it with me and it is going to stay where she left it."

    "The display wall cycles another patrol grid. Blue light on the strip of plastic. The word OPERATIONAL catches it clean. The ghost of THE LIVING in the feathered edge is not visible from this angle."

    "Aeron looks at the strip. He does not look at the display wall. He does not look at the door she walked out of. He looks at the strip."

    athought "The header stays."

    athought "I do not move it."

    athought "I do not remove it."

    athought "I sit here with it in front of me until shift change."

    "He does."

    # ========== STATE UPDATES -- BRANCH A ==========

    $ canon_set("ob.tessa.choice", "stay_and_resist")
    $ tp_seed("a4.ob.tessa.write_living_every_morning")
    $ flag("tessa_fracture_point_stayed_and_resisted", True)
    $ rel_bump("Tessa", trust=-1, conflict=1)
    $ npc_remember("Tessa", "fracture_point_confrontation", tone="decided_not_angry")
    $ npc_remember("Aeron", "header_left_on_table", tone="unflinching_receipt")
    $ metric("ob.intimacy.cold", +1)
    $ metric("ob.ritual.corrupted", +1)

    jump a4_s16_tessa_fracture_point_ob_close


# ==================================================================
# BRANCH B -- WITHDREW / DISMISSED IN ACT 3 S10
# ==================================================================
label a4_s16_tessa_fracture_point_ob_withdrew:

    # ========== PHASE 4B -- THE UNMET EYES ==========

    "Aeron does not look up. His eyes stay on the intake logs on his screen. The strip of plastic is in his peripheral vision and he is leaving it there."

    athought "She is waiting for me to look at her."

    athought "I am going to look at her. I am not going to look at her yet."

    athought "The delay is a tell. She will read it."

    "Tessa reads it. Her posture does not change. She has already finished deciding before she walked in and the delay does not cost her anything."

    tthought "He did not look up. That is the answer to the question I came to ask. I did not actually need him to say anything."

    tthought "I needed to see whether he would meet my eyes. He did not. I have the information."

    tthought "The rest of this conversation is a formality I am running because the formality is owed to the room, not to him."

    "He looks up. A few seconds late. The eye contact is clinical on his side and something older on hers."

    a "I did not write it."

    "She does not react."

    a "Someone mid-rank. I can guess which coordinator. I have not asked."

    "Her face does not move."

    a "I saw it three nights ago when I went to the wing on an errand. I read it once. I did not correct it. I left the wing without speaking to you about it because I did not know you were there."

    "She takes that in. She does not comment."

    tthought "He is telling me a version that gives him plausible distance. It is not a lie. It is also not enough."

    tthought "Three nights ago and he did not come find me. Three nights ago and he did not write it back. Three nights ago and he did not ask the coordinator who wrote it. Three nights. That is the answer to the question I came to ask."

    # ========== PHASE 5B -- ALREADY DECIDED ==========

    "Tessa does not shift her weight. Her hands are still at her sides. Her coat is still buttoned."

    t "I have been listening to the rooms I am not in."

    "Aeron's eyes on her. He does not speak."

    t "I have been standing in corridors outside meetings I was not invited to, and I have been reading intake logs I am not cleared to read, and I have been watching which coordinators walk the medical wing at which hours and taking notes in a folder I keep in my coat."

    t "I did that because I thought the room might be better than it looked from inside the medwing. I thought if I paid attention from outside the meetings I would find a counter-narrative. I thought I would find one person in command who was saying no."

    "She pauses. Not for effect. To be accurate."

    t "The room is worse than I thought."

    t "There is no one saying no."

    t "There is you, and there is Nyra, and there is a row of coordinators who are using the word OPERATIONAL without noticing that they are using it, and there is Noelle writing targeting doctrine in a folder she will not let me read, and there is Lyra blessing operators in a chapel I do not go to anymore. There is no one saying no. The rooms I have been listening to are one room and the one room does not contain a no."

    athought "She has been running her own surveillance on us."

    athought "For weeks. Quietly. She has notes in a folder in her coat. I did not know. Nyra did not know. No one knew."

    athought "That is the most competent piece of intelligence work anyone has done in this base in the last month and it was done by a medic who reports to no one."

    athought "I should be impressed. I am not. I am scared in the small, tidy way the mask lets me be scared."

    # ========== PHASE 6B -- THE REQUEST ==========

    "Tessa's voice does not rise. She is not pleading. She is placing a formal request on a table in a room that keeps formal records."

    t "I am going to ask you to let me leave."

    "Four-second silence."

    "Aeron's hand is on the table. The tremor is a small thing now. It was larger a month ago. Now it is small. It is not gone. It is trained."

    a "I cannot let you go."

    "He says it flat. No softening. No explanation clause. The sentence is the sentence."

    tthought "I knew he was going to say that. I asked the question so he would say it out loud. I needed to hear the sentence in his voice in this room so that I would not be able to pretend to myself later that I had not asked."

    tthought "Now I have asked. Now he has refused. Now I know."

    # ========== PHASE 7B -- THE DARK PROTOCOL ==========

    "She does not argue the refusal. She absorbs it the way she absorbed the answer about the header -- as data, not as injury. Her posture has not changed since she walked in."

    t "Then I will stay."

    "Pause."

    t "And I will do nothing."

    "His hand on the table is still. Not trembling now. Arrested."

    t "I will not touch the board. I will not write the names. I will not read the names. I will not add anyone to either column. I will not move anyone from one column to the other. I will not maintain the count."

    t "I will not leave the lamp. The lamp is already in the wing from three nights ago. I will not go back for it and I will not bring another one. If the lamp runs out of battery I will let it run out of battery. If someone takes the lamp I will not notice. If the clip breaks and the lamp falls I will not pick it up."

    t "I will not stop anyone from writing OPERATIONAL. If they write it again, I will see it and I will not peel it. If they print a label and bolt it to the wall, I will see it and I will not comment. If they change the word to something worse, I will see it and I will not comment. I will process the new word the way I process the new wing's HVAC. An environmental condition."

    "She is not performing this. Her voice is the voice of someone reading a triage protocol aloud because the protocol has been decided and reading it aloud is the administrative step that makes it binding."

    t "And the next time you bring me a body, I will fix it."

    "Pause."

    t "I will do the work. The bones and the blood. I will set the fracture and I will close the wound and I will monitor the vitals and I will write the chart."

    t "I will do it with hands that belong to no one in this room anymore."

    "A longer pause. She is giving him the last phrase on purpose. She wants him to hear it with all of the space it needs."

    t "Including me."

    # ========== PHASE 8B -- NO RESPONSE ==========

    athought "She has described a form of staying that is closer to abandonment than abandonment would be."

    athought "If she left the base I would lose a medic."

    athought "She is not leaving the base. She is extracting the part of her that was the medic from the body of the medic and leaving the body in the medwing to do the procedural work."

    athought "That is worse than losing her. That is the version of losing her that I cannot log as a departure and cannot log as a loss and cannot log at all."

    athought "She is giving me the administrative version of a medic who has stopped existing and whose hands still function."

    athought "I should say something."

    athought "I am not going to say anything. There is nothing I can say that does not immediately become the thing I have been doing to her for two months in a new tone."

    "Aeron does not speak."

    "Tessa does not wait for him to speak. She did not come here to receive a response. She came here to deliver the protocol and she has delivered it."

    tthought "I am not going to thank him for listening. He did not listen. He received. There is a difference."

    tthought "The room has the protocol now. The room is a witness. The plastic strip on the table is a witness. The display wall is a witness. That is enough witnesses for what I needed to establish."

    # ========== PHASE 9B -- THE EXIT ==========

    "She does not take the strip back. The strip stays where she put it."

    "She turns. Her boots on the floor. The gait is the gait of nineteen hours without sleep, controlled down to the heel strike, because control is the only resource she has left and she is rationing it."

    "Main door. Badge tap. Seal breath."

    "She does not look back."

    "The door closes."

    athought "She walked out of my ops room after telling me she was going to remain in my medwing as a pair of hands with no one inside them."

    athought "She is not leaving. She has left."

    athought "The body stays. The medic is gone. The staffing roster will not reflect the distinction."

    athought "Nyra will not notice. The coordinators will not notice. Stelker will not notice. The intake logs will not notice."

    athought "I will notice. I am noting it now."

    athought "I am noting it the way she just noted that I did not look up when she walked in. The same kind of note. The kind a medic keeps in a folder in her coat."

    # ========== PHASE 10B -- THE HEADER STAYS ==========

    "Aeron does not move the strip of plastic. He does not pick it up. He does not fold it. He does not slide it into a drawer."

    "He looks at it for a long time."

    athought "The header stays."

    athought "I do not move it."

    athought "I do not remove it."

    athought "She left it on the table and I am leaving it on the table because the table is the only place where the thing she said is a fact and if I move the strip I am moving the fact with it and I am not going to move the fact."

    "The display wall cycles another patrol grid. Blue light on the strip of plastic. The word OPERATIONAL catches it clean."

    "Aeron looks at the strip. He does not look at the display wall. He does not look at the door she walked out of."

    athought "I sit here with it in front of me until shift change."

    "He does."

    # ========== STATE UPDATES -- BRANCH B ==========

    $ canon_set("ob.tessa.choice", "stay_but_withdraw")
    $ tp_seed("a4.ob.tessa.hands_belong_to_no_one")
    $ flag("tessa_fracture_point_stayed_but_withdrew", True)
    $ rel_bump("Tessa", trust=-1, conflict=1)
    $ npc_remember("Tessa", "fracture_point_confrontation", tone="withdrawal_protocol")
    $ npc_remember("Aeron", "header_left_on_table", tone="receipt_without_response")
    $ metric("ob.intimacy.cold", +2)
    $ metric("ob.ritual.corrupted", +2)

    jump a4_s16_tessa_fracture_point_ob_close


# ==================================================================
# SHARED CLOSE
# ==================================================================
label a4_s16_tessa_fracture_point_ob_close:

    "The ops room holds at 0247. The HVAC in its lower register. The display wall cycling the same grid for the fourth time tonight. The strip of adhesive plastic on Aeron's table, exactly where Tessa set it down."

    "Aeron does not move."

    "The header stays."

    # ========== SCENE CLOSE ==========

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= SHARED STATE UPDATES =========
    $ flag("tessa_confronted_aeron_a4_fracture_point", True)
    $ canon_set("ob.aeron.header_on_table_until_shift_change", True)
    $ tp_seed("a4.ob.aeron.did_not_move_the_header")

    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s16_tessa_fracture_point_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Act 4 OB. 0247. Three nights after s06 board overwrite. Tessa has
#     not slept. She went back to the medwing tonight, peeled the
#     OPERATIONAL strip off the board, and carried it to the ops room.
# cann.what_happened:
#   - Tessa enters Aeron's ops room at 0247. No preamble. She sets the
#     OPERATIONAL plastic strip on his table and asks the one question:
#     whether he authorized it.
#   - CONDITIONAL on Act 3 s10 apology flag ("tessa_thread_open"):
#     * BRANCH A (stayed / apologized): Aeron tells the truth -- he did
#       not write it but did not stop it, and that is the same thing.
#       Tessa asks if anyone else will count if she stops. He says no.
#       She decides to keep counting. She will write LIVING back on the
#       board every morning they write OPERATIONAL. She will keep leaving
#       the lamp. She is not leaving angry -- she is leaving decided.
#     * BRANCH B (withdrew / dismissed): Aeron does not meet her eyes at
#       first. Tessa has been running her own quiet surveillance on the
#       command room for weeks. She asks to leave. He refuses. She
#       declares the withdrawal protocol: she will stay, she will do
#       nothing, she will not touch the board, she will not leave the
#       lamp, she will fix the next body with hands that belong to no
#       one in the room anymore, including her.
#   - Both branches end with Tessa walking out of the ops room and
#     Aeron alone with the OPERATIONAL header on the table in front of
#     him. He does not move it. He does not remove it. The header stays.
# cann.tessa_state:
#   - BRANCH A: decided, not angry. She has picked option four (count
#     anyway, on a board that is not hers, under a header that is not
#     hers). Her resistance takes the shape her care can take.
#   - BRANCH B: withdrawn as protocol. The darkest version. She is not
#     leaving the base because Aeron will not let her. She is leaving
#     the work, internally, while the body stays. "Hands that belong
#     to no one in this room anymore, including me."
# cann.aeron_state:
#   - No flinch. Marcus-idiom competent. Unflinching receipt of the
#     confrontation. The tremor is trained now -- smaller than it was.
#   - BRANCH A: gives her the true answer without softening. Does not
#     thank her. Will not convert her resistance into service to him.
#   - BRANCH B: does not meet her eyes at the start (the tell). Refuses
#     her request to leave. Does not respond to the withdrawal protocol
#     because any response would repeat the damage in a new tone.
#   - Both branches: leaves the header on the table. Does not move it.
#     The header stays until shift change.
# cann.thematic_flags:
#   - OB Act 4 thesis: "Violence Normalized." The header on the table
#     is the normalization made physical -- a strip of adhesive plastic
#     with a word on it, sitting on a table, because no one moves it.
#   - Route question: "Why didn't they leave?"
#     BRANCH A answer: she tried to; the alternative was the count
#     disappearing entirely; she chose inconvenience over silence.
#     BRANCH B answer: she asked and was refused; she extracted herself
#     from the work without physically leaving the room.
#   - The header stays. Aeron not moving the strip is the scene's
#     gesture equivalent of the sleeve-wipe in s06. Normalization
#     is performed by the small refusal to act.
#   - "Decided, not angry" (A) vs "withdrawn, not gone" (B) -- both
#     are forms of cold. OB aftercare register: no tenderness.
# cann.character_moments:
#   - Tessa (A): "I will write LIVING back on my board every morning
#     that they write OPERATIONAL. I will not let them make it easy."
#   - Tessa (B): "The room is worse than I thought. There is no one
#     saying no." / "Hands that belong to no one in this room
#     anymore, including me."
#   - Aeron (A): "No one else is keeping a board. If you stop counting,
#     no one else counts." Truth without softening.
#   - Aeron (B): "I cannot let you go." The refusal as sentence,
#     not as explanation.
# cann.callbacks:
#   - a3_s10_tessa_friction_ob: the apology/dismissal gate; tessa_thread_open
#     flag is the branch driver.
#   - a3_s17_count_the_cost_ob: BRANCH A echoes the quiet intimacy
#     established there; in BRANCH B that thread is absent and the
#     scene is harder because of the absence.
#   - a3_s19_the_weight_ob: Tessa's board methodology, her counting
#     ritual. Here the ritual has been corrupted and she is revising
#     (A) or abandoning (B) the protocol.
#   - a4_s06_tessa_at_the_board_ob: the lamp, the bag, the overwrite.
#     She has gone back for the strip. In BRANCH A she will continue
#     the lamp ritual. In BRANCH B she will let the lamp run out.
#   - s09 Sector 12 strike (three civilian deaths). The context under
#     which the overwrite was written and the room got worse.
#   - s10 Noelle drafting civilian targeting doctrine. The folder
#     Tessa cites in BRANCH B as one of the rooms she has been
#     listening to.
#   - s14 Lyra blessing operators. Cited in BRANCH B as the chapel
#     Tessa no longer attends.
# cann.block_status:
#   - STATE BEAT (OB). Conditional branching on Act 3 s10 apology flag.
#     No player choice in this scene -- the branch is already decided
#     by prior choice. The scene delivers the consequence.
#   - Sets up a4_s17 conditional beat: BRANCH A gates erotic grief-sex;
#     BRANCH B gates doorway-turn-away.
# cann.requires_followup:
#   - a4_s17: the conditional intimacy/withdrawal beat. Both branches
#     of this scene feed directly into the two branches of s17.
#   - The header on the table: who finds it at shift change? Does
#     Nyra see it? Does Aeron move it when she walks in, or does he
#     let her see it?
#   - BRANCH A: the LIVING-every-morning ritual -- does Tessa sustain
#     it? Does Aeron watch her sustain it? Does someone take the
#     marker from her?
#   - BRANCH B: the withdrawal protocol -- when does the first body
#     come in? Does she fix it with the described hands? Does the
#     fix read differently than before?
