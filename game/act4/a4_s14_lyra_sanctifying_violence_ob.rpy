# =======================================================
# ACT 4 - Scene 14: Sanctifying Violence (Obedience Path)
# File: a4_s14_lyra_sanctifying_violence_ob.rpy
# Path: OB
# Type: LYRA STATE BEAT / ARC DARKENING (non-erotic, pre-erotic setup)
# Character Focus: Lyra (primary, interior), Aeron (witness, one exchange)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s14_lyra_sanctifying_violence_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s14_lyra_sanctifying_violence_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm locked. Institutional register. The scene opens three-quarter on the
    #         muster bay -- a long corridor-adjacent staging room where operators kit up
    #         before strike runs. Lyra enters from frame-left. The operators are already
    #         assembled. She walks the line once. The camera dollies with her only until
    #         she stops at the first operator, then the camera locks again and stays locked
    #         for the rest of the blessing. Close-ups only on Lyra's hand making the
    #         six-fold sign. Never on the operators' faces -- they are a line, not a crowd.
    #         Mid-scene: wide on the whole bay with Lyra at the near end and Aeron at the
    #         far wall, hands clasped behind his back, watching. He is in frame but not lit.
    #         After the operators leave: two-shot, locked, Lyra and Aeron facing each other
    #         in the emptied bay. The camera does not move for the closing exchange.
    # LIGHTING: Muster bay is industrial -- 5000K overhead strips, the whole bay washed
    #           cold-white. No warm practicals. No candle. Lyra has brought nothing from the
    #           shrine alcove. This blessing happens in the base's own light.
    #           The floor has the yellow hazard striping of a loading zone. She stands on it.
    #           Aeron at the far wall: back-lit by a corridor bleed, face in shadow until the
    #           two-shot at the end.
    # SFX: Loop -- the muster bay ambient. Low generator hum. The clicks of operators
    #       seating magazines. The velcro check on plate carriers. The institutional sound
    #       of a strike loadout. When Lyra speaks, the kit-up noises do not stop for her.
    #       The bay does not hush. Lyra is not what the bay is pausing for. Lyra is an
    #       added layer.
    #      One-shots -- the hand-sign sweep (no sound). The single breath she takes
    #       before she starts. The operators' boots as they file out. Aeron's footfall
    #       crossing the bay after they are gone.
    # FX/COMP: The bay. Racked kit, strike briefing board with redacted sector numbers,
    #          a wall of ammunition stores behind mesh. The yellow hazard stripe under
    #          Lyra's boots. The Band at her hip -- cinched past comfort, the same notch
    #          as a4_s04. Visible under her vestments when she raises her hand.
    # BLOCKING: Lyra enters the bay. Walks to the head of the formed line. She does NOT
    #           walk the line individually -- she blesses the group. This is the new thing.
    #           Previously (cathedral-side) she blessed the wounded one by one. Here she
    #           blesses a formation as a formation. The difference is the scene.
    #           The operators stand at loose attention. Kit-up is done. They are waiting.
    #           She raises her hand. She makes the six-fold sign. She speaks the short form.
    #           The short form is the one priests use when there is no time for the long form.
    #           The fact that she is using the short form for a departure blessing is a
    #           canonical innovation. She is the one inventing it, in this room, this morning.
    #           When she finishes, the operators turn and file out through the loading door.
    #           Aeron crosses from the far wall. They meet in the center of the emptied bay.
    # CANON: LYRA ARC DARKENING. First time she blesses the departing weapon.
    #        Previously she blessed the returning wounded. The scene is the moment
    #        a priest crosses from tending the hurt to consecrating the hurting.
    #        She does not resolve the crossing. She names it, in her own language, and stays.
    # FACE: Lyra -- composed. This is a professional act. She does it well. The cost
    #        is only visible in her interior and in the final two-shot when Aeron asks
    #        the single question. She does not smile. She does not cry.
    #        Aeron -- present, watching, not approving. He has not asked her to do this.
    #        The muster officer asked. Aeron did not countermand. The not-countermanding
    #        is the pressure.

    # ========= VOICE BASELINE =========
    # Lyra: Heavy lthought. Her spoken lines are: the short-form blessing (Old Tongue
    #        + one Aerenine sentence), and the closing exchange with Aeron. Everything
    #        else is interior.
    # Aeron: Economic. Three spoken lines total in the whole scene. The clinical cadence.
    #        The third line -- "You could refuse." -- is the load-bearing one. He says it
    #        without pressure, not to push her to refuse but to make sure she knows the
    #        option exists. That is the last kindness he knows how to offer.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MUSTER BAY - MORNING]
    # Mid-morning. After the shrine-alcove prayer failed (a4_s04).
    # A strike team is kitting up for the next sector sweep. The muster officer --
    # a woman Lyra does not know by name -- asked her twenty minutes ago whether
    # she would come down and "offer a word" before the team went out.
    # The muster officer did not use the word "blessing." She said "offer a word."
    # Lyra understood what was being asked. She said yes before she had finished
    # understanding it.

    #scene bg_muster_bay_ob_morning with dissolve
    #play ambient "sfx/ambient/muster_bay_loadout.ogg" fadein 2.0

    # ========== PHASE 1 -- THE WALK IN ==========

    "The door to the muster bay slides aside. Lyra steps through. The hazard striping on the floor catches the cold overhead light and holds it."

    lthought "Walk in the way you have walked into cathedrals. The room does not know what to do with the difference."

    "Twelve operators. Kit squared. Plate carriers seated. Rifles slung. They are waiting -- not for her, exactly, but for whatever the muster officer told them would happen before the signal to move out."

    "The muster officer stands at the briefing board, hands clasped behind her back. She catches Lyra's eye once and nods. The nod is brisk. It is the nod of a person delivering a resource to a room that had been told it would get one."

    lthought "I am the resource."

    "Lyra walks to the head of the formation. Her boots cross the yellow hazard line. She stops there -- deliberately there, on the line that marks the edge of the loading zone, because she cannot make herself stand inside it."

    lthought "The hazard line is for crates that are going out. I am standing at the edge of it. That is the most honest coordinate available to me in this bay."

    "The operators register her arrival and return their attention to the middle distance. They are not looking at her. They are not not looking at her either. They are in the state of readiness a soldier enters when the administrative part of the morning is still happening and has not yet become the mission."

    lthought "They do not know what the word is going to be. I do not know what the word is going to be."

    lthought "I have ten seconds to decide before the silence becomes its own speech."

    # ========== PHASE 2 -- THE DECISION THAT HAPPENS ON THE WAY DOWN ==========

    "Her hand is already at her chest. Muscle memory. The six-fold sign begins at the collarbone and ends at the heart."

    lthought "Decide now."

    lthought "The short form or the long form. The cathedral or the battlefield."

    lthought "The long form is for the wounded. The long form is what I said over the cot in the medbay last week -- over the operator with the shrapnel in his thigh, whose hand was cold when I held it and warmer when I let it go. The long form is a prayer for a body that has already been broken and is trying to find its way back."

    lthought "These bodies are not broken. These bodies are going out to break other bodies."

    lthought "The long form does not fit. I would be speaking a prayer for the wounded over twelve people who are not wounded. The mismatch would be its own sermon."

    lthought "The short form exists. The short form is for... what. The short form is for when there is no time. When the cathedral is burning and the priests have to speak the blessing before the roof comes down."

    lthought "This is not a burning cathedral. This is a muster bay. There is time. The muster officer has twenty more minutes in her window."

    lthought "But the short form is the only form whose shape can hold this room."

    lthought "So I am going to use it. And in using it I am adapting a cathedral-emergency prayer to a non-emergency military departure. I am making it a new liturgy. I am inventing a blessing for the outgoing weapon."

    lthought "No one asked me for the inventing. No one will know I did the inventing. I will know."

    # ========== PHASE 3 -- THE ROOM NOTICES ==========

    "She raises her hand. Not high. Just above her shoulder. The gesture a priest makes when she has chosen not to shout."

    "The kit-up sounds do not stop. The operators do not come to full attention. They adjust by a quarter measure -- a subtle squaring, the way a line comes into focus without the order to dress up being given. The shift is too small to call a response. It is also unmistakable."

    lthought "They are used to this."

    lthought "They have been blessed in muster bays before."

    lthought "Not by me. By whatever priest came before. By field chaplains in the first year of the war. This is not new to them. This is new to me."

    lthought "The room knows the shape of what I am about to do. I am catching up to a liturgy the room already has."

    "She sees Aeron at the far wall. She had not been tracking him. He is there now. Hands behind his back, shoulder to the wall, back-lit by the corridor bleed. He is not signaling her. He is not approving. He is watching the way he watches the tactical board."

    lthought "He is not going to stop this."

    lthought "He is not going to ask me to do it harder, either."

    lthought "He is going to watch me make the decision and then he is going to let the decision I made be the decision."

    lthought "That is new, too."

    lthought "Two months ago he would have either pushed or pulled. Now he only witnesses. He is learning precision. Precision includes not touching the thing that is already moving correctly."

    # ========== PHASE 4 -- THE BLESSING ==========

    "Her hand traces the sign. Six points. Collarbone, shoulder, shoulder, sternum, hip, heart. The sign is the same sign priests have made in this language for eight hundred years. The sign does not know what bay it is being made in."

    l "(Old Tongue, the short form) Vel'a sen'irun. Adrun i velh. Sen'al thrun."

    lthought "Go with the steady hand. Return by the road you know. Let your hand be clear."

    lthought "The first phrase was for the wounded. I have said it over people I knew would not live through the next day, and over people who were already on the second breath of their recovery. Go with the steady hand."

    lthought "I am saying it to people whose steady hand is the thing they are going to use to end other hands."

    lthought "The same phrase. Entirely the same phrase. The liturgy does not differentiate."

    lthought "The liturgy is not going to do my differentiating for me."

    "She says the Aerenine closing. The one she added herself, in the walk from the door to the head of the formation. She has never said this phrase before. She is saying it for the first time now."

    l "Go, and come back."

    "Three words. Aerenine. Plain. Not theological. The words a priest might say in a doorway at a wedding, or a mother might say to a child leaving for school, or anyone might say to anyone they cared about who was going somewhere."

    lthought "That is the whole of what I can honestly offer them."

    lthought "Not 'may your mission succeed.' Not 'may the Six bless your strike.' Not 'may the enemy fall before your hand.' I will not speak those sentences. The priest in me refuses them."

    lthought "I can say: go, and come back. That is mercy at the level of the body. Return. Be one of the ones who returns. That is a prayer I can say without lying."

    lthought "It is also a prayer that refuses to bless the going. It only blesses the coming back."

    lthought "I do not know if the operators hear the refusal inside the blessing. I do not think they are listening for it."

    lthought "I think I am the only one in this room who heard what I just did not say."

    # ========== PHASE 5 -- THE ROOM RECEIVES ==========

    "The operators nod. Not in unison. A ripple -- the nearest ones first, then the ones down the line, the small acknowledgment of a ritual completed. A few of them touch their own sternums briefly. One woman closes her eyes for a second and opens them."

    lthought "She is praying too. Independently. She was already praying and the blessing folded into her prayer. I have no claim on her prayer."

    lthought "She may have a better relationship with the Six right now than I do. She is going out to kill and she is still in her own prayer. I am staying in and I have not managed to pray in my own voice in three days."

    lthought "I am going to think about that woman tonight. I do not know her name. I would like to."

    "The muster officer speaks -- not loudly -- the single word that ends the blessing phase and begins the movement phase."

    # (Muster officer line -- not voiced, implied)
    "Load."

    "The operators move. Boots on concrete. The line re-forms as a column. The column moves toward the loading door at the far end of the bay. The door slides aside. They file through. The door slides shut."

    "The muster officer follows them through a side hatch without looking back at Lyra. That is also correct procedure. There is no dismissal for the priest. The priest dismisses herself."

    lthought "They are gone."

    lthought "I am standing in the empty bay with my hand still at half-raise."

    "She lowers her hand."

    # ========== PHASE 6 -- THE INTERIOR COUNT ==========

    "She does not move from the hazard line. Her boots are still on it. The yellow paint is old and the paint flake is visible up close. She is looking at the paint flake."

    lthought "The Six do not weigh mercy. They count it."

    lthought "What did I just count."

    lthought "I counted one departure blessing. I did not count twelve -- I counted one, because I blessed the formation, not the people. I blessed the formation as a unit. A unit is a grammatical thing the priest's ledger does not have a clean category for."

    lthought "So: one act of consecration, performed by a priest in the Order of the Six, applied to a military formation preparing to execute a sector strike in an urban environment with a non-zero civilian proximity."

    lthought "I am saying it clinically because clinical is the only register in which the sentence will fit in my head."

    lthought "If I said it devotionally, it would not fit. It would break the container."

    lthought "The count moves. I am the one moving it."

    "Her free hand goes to the Band. Not to loosen. To confirm. The buckle is still cinched past the notch she usually uses. She set it that way this morning before she knew she was going to do this."

    lthought "The Band cinched past comfort as I blessed the departing weapon."

    lthought "That is the record. That is the sentence a historian would write if a historian were permitted to write the sentence."

    lthought "No historian will write it. This is a classified muster. The muster officer did not use the word blessing. I am the only witness to my own position."

    lthought "Except."

    # ========== PHASE 7 -- THE SECOND WITNESS ==========

    "Bootfall from the far wall. Aeron crossing the empty bay. Measured. Not hurrying. He stops two paces from her. His face is out of the corridor back-light now. She can see him."

    "He does not congratulate her. He does not thank her. He does not say any of the sentences the muster officer would have said if the muster officer had stayed."

    "He says, instead --"

    a "Is this all right."

    "Not a tactical question. Not a procedural check. A question a person asks another person when they have watched something happen and want to know whether the other person is sitting inside the thing that happened or standing outside it."

    lthought "He said 'is this all right.'"

    lthought "Two months ago he would have said 'good work' or 'thank you.' One month ago he would have said nothing. Today he said 'is this all right.'"

    lthought "That is the Marcus idiom. I know it is the Marcus idiom because I was raised by priests who trained me to recognize the cadence of that school -- the precise small check that looks like concern and is actually reconnaissance. Marcus never asked 'is this all right' to ask if the person was all right. He asked it to confirm the person was operational."

    lthought "Aeron is using the same sentence. I do not know yet whether he is using it the way Marcus used it or the way a person who cared about me would use it."

    lthought "I do not know if Aeron knows."

    lthought "I am going to answer as if the question were both at once, because that is the only answer that matches the condition I am in."

    l "No."

    "One word. She lets it sit. Aeron does not flinch. His expression does not change. He waits for the rest."

    l "It is what is available. I am choosing what is available."

    lthought "That is the whole sentence. I cannot say it is all right. It is not. But I also cannot say that I am being coerced, because I am not being coerced. I am choosing. Choosing among available options is a choice. The fact that the options are all bad does not make the choosing not-a-choosing."

    lthought "The priest in me knows that doctrine. The priest in me is citing it to herself to survive the sentence she just said aloud."

    # ========== PHASE 8 -- THE OPTION HE LAYS DOWN ==========

    "Aeron's hands are still behind his back. He has not moved them since he entered the bay. The stillness is not a performance. It is what his body is doing."

    "He speaks the line that will matter."

    a "You could refuse."

    "Flat. Not pushing. Not hoping. The sentence a person puts on the table because it is a real option and someone should name it."

    lthought "He said it."

    lthought "He said it without inflection. He said it the way the muster officer would say 'the ammunition reserve is at seventy percent.' A fact. A fact you can act on."

    lthought "He is giving me the off-ramp. He is not urging me onto it. He is making sure I know it exists."

    lthought "That is more than I expected from him this morning."

    lthought "It is also less than the version of him I am here to save would have done. The version of him I am here to save would not have let me walk into this bay in the first place."

    lthought "The Aeron who lets me walk in and then tells me I could refuse is a different Aeron than the one on the balcony. He is more precise. He is less protective. The precision is the thing I am afraid of and the thing that is keeping me here."

    lthought "Because if the precision is still capable of naming the off-ramp, then the precision is still aware the off-ramp exists. And if the precision is still aware, then there is still a man inside the precision who knows what this room is."

    lthought "And if there is still a man inside the precision, then leaving would leave the man alone with the precision. And the precision would win."

    lthought "I am about to say the sentence that is my whole answer to the route."

    # ========== PHASE 9 -- THE ROUTE ANSWER ==========

    l "I could."

    "She pauses. The pause is deliberate. She is letting him hear that she is taking the off-ramp seriously enough to consider it out loud."

    l "You would do it without me."

    a "Yes."

    "No hesitation. He will not lie to her about that."

    l "It would be worse."

    a "..."

    l "The thing I am blessing would go out unblessed. And then I would be the priest who stood by while it happened. At a distance. In a chapel. Somewhere that was not this bay."

    l "I am not stopping it, Aeron. I am not capable of stopping it. Whatever else I am -- I am not the person who can stop the operation the base has scheduled for this morning. That person is not in this base. That person is perhaps not in this city."

    l "I am not stopping it. I am being in the room with it."

    lthought "The sentence is out."

    lthought "I did not plan to say it that way. The priests in the old texts call it the moment when the position names itself. The position has been sitting under my tongue for three days and it finally used the mouth."

    lthought "Being in the room with it."

    lthought "That is my doctrine now. That is the theology I have made for myself in the last ten days without admitting I was making it. A priest who cannot stop the war can at least refuse to leave the room where the war is being planned. A priest in the room is a priest who can still speak when the plan gets worse. A priest who left is a priest whose voice no longer carries in here."

    lthought "I believe that. I am also aware that it is the rationalization of every priest who has ever been absorbed by a regime. I have read the histories. I taught the histories to novices."

    lthought "I taught them the pattern so they could recognize it when it happened to them."

    lthought "I am now inside the pattern and I am recognizing it correctly. The recognition is not stopping me from being inside it."

    lthought "There are two possibilities. One: I am the priest in the histories who stayed and whose staying mattered, whose voice in the room bent the outcome by one increment, whose presence cost the regime something it would not otherwise have paid. Two: I am the priest in the histories who told herself the first story and was wrong."

    lthought "I do not know which one I am. I am going to find out by living the months."

    # ========== PHASE 10 -- HIS SILENCE ==========

    "Aeron does not disagree."

    "He does not agree, either. He does not say 'you are doing the right thing.' He does not say 'thank you for staying.' He does not say any of the things a man who wanted to keep her here would say."

    "He looks at her. The look is long enough that she knows it is a look and not a glance. His eyes are not soft. They are also not cold in the way she has grown used to. Something is happening behind them that is neither of those things."

    lthought "He is registering what I said."

    lthought "He is not arguing with it. He is not accepting it. He is putting it in the place in his head where he puts information he is going to use later and not examine yet."

    lthought "That is Marcus's habit. Marcus called it the slow drawer. He taught Aeron the slow drawer in the Academy. Aeron is using it now on me."

    lthought "I am in the slow drawer."

    lthought "The thing I just said -- the thing that was my route answer, my whole position -- is going into the slow drawer. He will take it out in three weeks and look at it. He will not tell me when he is looking at it."

    lthought "I cannot stop him from using the slow drawer on me. I also cannot know what he does with what he finds in there."

    "He moves. Not toward her. Not away. He brings one hand from behind his back. Only one. He holds it out to her -- palm up, open, not a gesture of invitation and not a command. A thing he is offering her the option of."

    # ========== PHASE 11 -- THE HAND ==========

    "She looks at the hand."

    lthought "The last time he held his hand out to me like this was three weeks ago. In the corridor outside the war room. I did not take it that time. I had just come from the medbay and my hands were not clean."

    lthought "My hands are not clean now either. They are cleaner in the ordinary sense and dirtier in the other sense."

    lthought "He is asking if I will take the hand of the man I just blessed the outgoing operators for."

    lthought "The honest answer is yes. The honest answer is that I came down to this bay because the muster officer asked and because not coming would have been a refusal and because refusal is not the position I am holding. Staying is the position. Staying includes taking his hand."

    "She takes it."

    "Her hand in his. The same pressure as in the alcove on the morning of a4_s04. Neither of them grips. He meets her exactly. No more. No less."

    lthought "He is still doing the thing where he matches me. He has been doing that for weeks. It used to feel like presence. Now it feels like mirroring. I am aware of the difference. I am aware that awareness of the difference has not caused me to withdraw my hand."

    "The two of them in the center of the emptied bay, hand in hand, not facing each other, both facing the loading door the operators filed through."

    "Neither of them speaks."

    # ========== PHASE 12 -- THE BAND ==========

    "Her free hand does not go to the buckle."

    "She is aware of the buckle. The Band is still cinched past the notch she usually uses. She has been aware of it for every minute of this scene. She has not loosened it since she tightened it in the shrine alcove this morning."

    lthought "I could loosen it now."

    lthought "The blessing is done. The operators are gone. Aeron is holding my hand in the emptied bay. If there were ever a moment to call the hand the occasion and relax the discipline by one notch, this would be the moment."

    lthought "I am not going to."

    lthought "The Band is cinched because the thing it is cinched against has not resolved. It will not resolve at the edge of a hazard line in a muster bay after the operators have left. The resolution, if any, is in some other scene in some other week."

    lthought "The Band stays cinched."

    lthought "This is what it looks like to choose to stay in the room. The body does not get to relax because the mouth said the right sentence."

    # ========== PHASE 13 -- THE NON-EXIT ==========

    "The bay is quiet. Somewhere in the base a door cycles and a set of voices passes the bay entrance without coming in. The generator hum continues. The hazard stripe continues to be yellow."

    "Lyra's breath comes steady. Not peaceful. Not ragged. The breathing of a person whose body has been told what position it is in and has agreed to hold the position."

    a "Come back upstairs."

    "The first thing he has said since 'you could refuse.' A quiet sentence. Not an order. An invitation to move out of the bay and into the rest of the morning."

    lthought "He is letting me know the scene can end whenever I am ready for it to end."

    lthought "I am not ready yet. I need to say one more thing. Not to him. To myself. Out loud, so the bay hears it."

    l "I will come back upstairs in a minute."

    a "All right."

    "He does not release her hand. She does not release his. The hand-holding does not know the conversation has moved on. That is fine. The hand-holding has its own time."

    # ========== PHASE 14 -- THE SENTENCE TO THE BAY ==========

    "Lyra turns her face toward the loading door. The door the operators went through. She speaks to the door. Not loudly. It is the kind of speech priests do when they are witnessing for the absent."

    l "Go, and come back."

    "The second time she has said the phrase this morning. The first time it was part of the blessing. The second time it is separate. It is not doctrine. It is not liturgy. It is a woman saying a sentence to a door."

    lthought "I am counting. I do not know what I am counting toward. I am counting anyway."

    lthought "If any of them come back, I will have said something to them that was a blessing and not a consecration. If none of them come back, I will still have said it. The saying does not depend on the outcome."

    lthought "That is the smallest doctrine I can make from the materials available."

    # ========== PHASE 15 -- HOLD ==========

    "She does not move. Aeron does not move. The bay holds them in its cold overhead light. The hazard stripe is under her boots and the Band is at her hip and the hand in her hand is Aeron's and the operators are gone and the prayer she said was a blessing for a weapon and she is not going to resolve any of those things in this scene."

    "She is going to hold the position."

    "The camera does not move. The lighting does not shift. The loading door stays closed. The hand stays in the hand."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1, conflict=1)
    $ canon_set("ob.lyra.blessing_the_outgoing", True)
    $ tp_seed("a4.ob.lyra.being_in_the_room_with_it")
    $ flag("ob_lyra_sanctified_departing_weapon", True)
    $ flag("ob_lyra_route_answer_articulated", True)
    $ npc_remember("Lyra", "invented_short_form_for_outgoing_strike", tone="rationalization_as_doctrine")
    $ npc_remember("Lyra", "go_and_come_back_refusing_to_bless_the_going", tone="priest_doctrine_innovation")
    $ npc_remember("Aeron", "asked_is_this_all_right_marcus_idiom", tone="precision_inheriting_concern")
    $ npc_remember("Aeron", "named_the_off_ramp_she_could_refuse", tone="last_kindness_available")
    $ metric("lyra_ob_rationalization_index", add=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s14_lyra_sanctifying_violence_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same day as a4_s04 (Lyra prays alone). Late morning. After the prayer failed.
#   - The muster officer has asked Lyra to "offer a word" before the next strike.
#   - Parallel to Sector 12 planning / Nyra second-oath aftermath.
# cann.what_happened:
#   - Lyra walks into a muster bay and blesses an outgoing strike team for the first time.
#   - Previously she blessed the returning wounded. This is new -- she is consecrating
#     the hurting, not tending the hurt.
#   - She invents a short-form liturgy on the walk in. She uses the priest's
#     cathedral-emergency short form and adds an Aerenine closing: "Go, and come back."
#   - The Aerenine closing refuses to bless the going. It only blesses the return.
#     She is the only person in the bay who hears the refusal inside the blessing.
#   - Aeron watches from the far wall. After the operators leave, he crosses the bay
#     and asks "Is this all right." (Marcus idiom -- inherited cadence, ambiguous intent.)
#   - Lyra answers: "No. It is what is available. I am choosing what is available."
#   - Aeron names the off-ramp: "You could refuse." Without pressure.
#   - Lyra articulates the OB route answer in her own language:
#     "You would do it without me. It would be worse... I am not stopping it.
#      I am being in the room with it."
#   - Aeron does not disagree. He does not agree. He puts it in the slow drawer.
#   - He offers his hand. She takes it. The Band stays cinched past comfort.
#   - Non-resolution ending. She stays in the position.
# cann.aeron_state:
#   - Growing more competent in the Marcus idiom. His concern-sentences now mimic
#     Marcus's reconnaissance sentences. He may not know which he is doing.
#   - He did not countermand the muster officer. The not-countermanding is the pressure.
#   - He names the off-ramp without pushing her onto it. Last kindness available.
# cann.lyra_state:
#   - Devotion as rationalization made doctrine. She now has a named theology for staying:
#     "being in the room with it." She knows it is the rationalization pattern from
#     the histories she used to teach. The knowledge does not free her from it.
#   - Band still cinched past comfort. She does not loosen it.
#   - She invents a new liturgy under pressure. She is sanctifying violence in the
#     most delicate form she can, and she knows the delicacy does not absolve it.
# cann.path_tracking:
#   - rel_bump Lyra trust=1 conflict=1.
#   - canon_set ob.lyra.blessing_the_outgoing True.
#   - tp_seed a4.ob.lyra.being_in_the_room_with_it.
# cann.thematic_flags:
#   - The hazard line under her boots. She stands on the edge, not inside the loading zone.
#   - "Go, and come back" -- the priest's refusal folded inside the blessing.
#   - The slow drawer -- Aeron's inherited Marcus habit. Lyra recognizes it.
#   - The route question "why didn't they leave" answered in Lyra's own language:
#     leaving would leave the precision alone with itself, and the precision would win.
#   - The priest doctrine innovation: a blessing that refuses to bless the going.
#     Delicate. Sincere. Still a sanctification. She knows the distinction does not hold.
# cann.character_moments:
#   - Lyra: first consecration of the outgoing weapon. The priest crosses the line
#     from tending the hurt to consecrating the hurting. She crosses it knowingly.
#   - Aeron: "Is this all right" / "You could refuse" -- two sentences, the load-bearing
#     ones for the scene. He is learning Marcus's reconnaissance cadence without yet
#     knowing he is learning it.
# cann.callbacks:
#   - a4_s04 (Band cinched past comfort). The notch is unchanged.
#   - a3_s13 (the gap is bigger). The gap is now Lyra's own rationalization.
#   - a1_s07 (balcony Aeron). She references him as the man she is here to save.
# cann.block_status:
#   - ANCHOR (OB). State beat / arc darkening. No player choice.
# cann.requires_followup:
#   - Sets up a4_s15 (erotic deepening). Lyra decides the physical companion to
#     "being in the room with it" is going to his quarters tonight.
#   - "Go, and come back" -- the refusal-inside-the-blessing phrase should recur.
#   - The slow drawer -- Aeron's use of it on Lyra's sentence should recur when he
#     pulls it out in a later scene (target: mid-late Act 4 or Act 5).
#   - Lyra's inventory of two possibilities (the priest whose staying mattered vs.
#     the priest who told herself the story and was wrong) -- endgame variable.
