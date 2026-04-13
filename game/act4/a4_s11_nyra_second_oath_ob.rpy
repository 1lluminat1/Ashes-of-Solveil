# =======================================================
# ACT 4 - Scene 11: The Second Oath (Obedience Path)
# File: a4_s11_nyra_second_oath_ob.rpy
# Path: OB
# Type: NYRA EROTIC DEEPENING (SECOND RITUAL -- THE SEALING)
# Character Focus: Nyra, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s11_nyra_second_oath_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s11_nyra_second_oath_ob:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s11_nyra_second_oath_ob")
    $ show_timeline("29th of Forge, 390 A.C.", "22:00", "Phoenix Base — Nyra's Quarters")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Same lens grammar as a3_s12 -- formal distance,
    #         composed framing, no drift. But the room is different. This is HER
    #         quarters now, not his. The camera is a guest in a temple it does not
    #         understand. Opens wide on the quarters: sparse, ordered, the bed made
    #         with hospital corners, a single candle-analog, the lacquered box on
    #         the desk. Tightens across the ritual: medium singles, then an over-shoulder
    #         on her hands when she opens the box. The ash shot is a clean macro.
    #         When she marks his forehead: close-up, her thumb, his skin, the dark
    #         streak of ash. The camera does not editorialize. It records a liturgy.
    #         Consent gates: medium two-shot -- she does not kneel tonight. They
    #         face each other standing. The symmetry is the point. By the intimacy:
    #         same palette as a3_s12. Bodies as architecture. No warmth bloom.
    # LIGHTING: Steel-blue overhead at 30% -- lower than a3_s12, closer to dusk inside.
    #           The candle-analog (same military-issue, battery, warm but functional)
    #           sits on the desk beside the lacquered box. The box is older than
    #           anything else in the room -- dark wood, Order insignia worn half off
    #           the lid. Blue dominates. The amber is a witness, not a mood.
    # SFX: Loop -- quarters ambient: HVAC, distant watch change, the structural creak
    #      of a fortified corridor. One-shots -- the lacquered box opening (a dry
    #      wooden click, old hinge), the brush of her thumb in ash, the rustle of
    #      her uniform, the seal of the door when he enters. Breath: hers measured,
    #      his uneven. The uneven breath is the only disobedience the scene permits.
    # FX/COMP: The lacquered box: small, 15cm square, black wood. Inside: ash, fine,
    #          pale grey, compacted into one corner. She does not volunteer its origin.
    #          Nyra's quarters: cot, desk, two chairs, a single framed paper on the wall
    #          (the oath text, hand-copied in her script). The fractured Echelon crest
    #          from a3_s12 is NOT present. She has graduated past it. Tonight is a
    #          newer ceremony.
    # BLOCKING: Aeron enters. She is already standing at the desk, facing the box.
    #           She does not turn for several seconds. She turns when she is ready.
    #           The ritual is performed in the center of the room. She brings the
    #           box and the candle to a low table she has placed between them.
    #           She does not kneel tonight. The posture is new: they stand facing
    #           each other, the box between them, her hands over it the way a priest's
    #           hands hover over a chalice. Physical contact: her thumb, his forehead,
    #           the ash. Then the consent gate. Then the second contact.
    # CANON: NYRA SECOND EROTIC. The SEALING of the first oath (a3_s12). That one was
    #        the door (her word). Tonight she closes it. The first was about OFFERING.
    #        Tonight is about LOCKING. The ceremony has moved from asking to confirming.
    #        She is not seducing him; she is ordaining him. And she is performing the
    #        control the ritual requires -- she is in charge, and the performance of
    #        being in charge is itself part of the rite. Callbacks: a3_s12 (oath),
    #        a3_s20 (Zira's "you don't get to break"), a4_s07 (Aeron and Nyra cold),
    #        a4_s10 (Noelle's blank authorization -- the night BEFORE tonight).
    # CONSENT: 3-choice framework, OB-mode. Choice 3 is the "out" -- but Nyra's
    #          response forces a reselection. If the player selects choice 3 twice
    #          in a row, Nyra dismisses him and the scene ends in the corridor.
    #          Otherwise all paths lead to # [INTIMATE CONTENT HERE].
    # FACE: Nyra -- composed liturgy. Every muscle in her face is doing work.
    #        That is the tell: she is PERFORMING stillness for him. Because the rite
    #        demands it, and because she demands the rite of herself.
    #        Aeron -- mask. Beneath the mask: not hunger, not fear. Something colder.
    #        He is here because she called. The obedience is no longer novel.

    # ========= VOICE BASELINE =========
    # OB Aeron: Clinical. Short sentences. The Marcus idiom has deepened -- he speaks
    #           in verbs of process now. "Permit." "Confirm." "Proceed." The athoughts
    #           are where the fracture lives, but they are quieter than a3_s12.
    #           The static is steadier. He is not surprised by any of this.
    # Nyra: Calm. Liturgical. The cadence has shifted from declaration to invocation.
    #       She speaks less. The silences do more of the work. Her words have the
    #       weight of text that has been written down somewhere and is being recited
    #       by someone who copied it into her own hand.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - NYRA'S QUARTERS - NIGHT]
    # Steel-blue. Sparse. The room of a soldier who has made her cot into an altar.
    # 0130. Base on night-shift skeleton crew. The corridor outside is empty.

    #scene bg_nyra_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_cold_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE SUMMONS ==========

    athought "The note came at 2340."

    athought "One line. No name. No greeting. No sign-off."

    athought "'Tonight.'"

    athought "I knew the hand before I read the word."

    athought "I also knew I would go."

    athought "The knowing came before the deciding. That is the part I am trying not to examine."

    "He walks the corridor at 0128. The base is running skeleton. He passes two sentries. Neither looks at him."

    athought "They know where I am going. They have been instructed not to register it."

    athought "Nyra's doing. She does not like her rites observed."

    "He reaches her door. Sector C. Officer's block. The door is unmarked -- she has had the name-plate removed."

    athought "The name-plate came off last week. I did not ask why."

    athought "She told me anyway: 'A name is a handle. Handles are how the wrong people carry you.'"

    athought "I remember thinking: that is not about security."

    athought "I was right. It was about what tonight is about."

    #play sound "sfx/door_knock_single.ogg"

    "He knocks once. One knock is the cadence she prefers. He learned it by being corrected, twice."

    "The door unseals from the inside. No voice. The door opens a hand's breadth and waits for him."

    athought "She does not say 'enter.' The door opening IS the permission."

    athought "I enter."

    # ========== PHASE 2 -- THE ROOM ==========

    #scene bg_nyra_quarters_interior_ob with dissolve

    "The quarters are arranged as if for inspection."

    "The cot: hospital corners, grey blanket squared to the frame. The desk: empty except for the candle-analog (lit) and the lacquered box (closed)."

    "The single chair has been moved to the wall. A low table -- standard base issue, 40cm tall -- has been placed in the center of the room, equidistant from cot and door."

    "One framed paper hangs on the wall above the desk. He has seen it before: the oath text, in her handwriting, copied clean. The frame is pewter. The paper is white. There is no other decoration in the room."

    athought "The crest is not here."

    athought "The fractured Echelon crest that she brought to my quarters the first night. The copper wire, the broken faces, the weight of it in her palms."

    athought "It is not in this room."

    athought "That is a message. I am not sure yet what the message is."

    "Nyra stands at the desk, facing the box. Her back is to him. Her uniform is pressed. Her hair is pinned -- a tight bun, the way she wears it for formal inspection, not the way she wears it for duty."

    "She does not turn when the door reseals behind him."

    "She is waiting for something."

    athought "She is waiting for the room to settle. For the air to acknowledge I am in it."

    athought "I have watched her do this before every briefing. It is not superstition. It is a way of telling time without a clock."

    "She turns."

    # ========== PHASE 3 -- THE ARRIVAL ==========

    ny "Commander."

    a "Nyra."

    "She does not correct him. Not yet. The correction is part of the rite, and the rite has not started."

    ny "Thank you for coming."

    a "You did not ask."

    ny "No. I did not."

    ny "I told you tonight. That is different from asking."

    ny "I wanted to see whether you would come to a word that was not a request."

    a "You already knew I would."

    ny "I did. I wanted to see it anyway."

    athought "She wanted the confirmation. That is the pattern now. Every certainty she holds, she has me prove to her a second time, in the flesh."

    athought "I am her scripture. And scripture requires re-reading."

    "He steps into the room. Three paces. He stops at the far side of the low table. She is on the near side. The box is between them. The candle is on her side of the desk, not on the table. That will change."

    # ========== PHASE 4 -- THE BOX ==========

    ny "Come closer."

    "He does. Two more paces. Now the table is between them at hip distance. She can reach him across it. She does not, yet."

    "She places her hands flat on the desk on either side of the box. Palms down. Her fingers are long and still."

    ny "The first oath was the door."

    ny "You walked through the door. I was there. You know what happened there."

    ny "Tonight you close the door."

    athought "Tonight you close the door. Tonight YOU close the door."

    athought "The verb is mine. She is giving me the action. That is the asymmetry she wants me to notice."

    athought "She controls the rite. But the final motion in the rite has to be mine. Otherwise it does not seal."

    a "What is in the box."

    ny "Ash."

    a "Ash of what."

    "A pause. The HVAC cycles. The candle flame holds."

    ny "I will not tell you tonight."

    ny "If I tell you tonight, you will be sealing to a thing you understand. The oath does not permit that. The oath is the act of sealing to what you do not need to see."

    ny "If you need to see, the oath is not ready, and I send you away."

    athought "She means it. She is not bluffing. If I ask for the word I will leave."

    athought "I almost ask."

    athought "I do not ask."

    a "Proceed."

    "The word is clinical. The Marcus idiom has deepened. Six weeks ago I might have said 'go on.' Tonight it is 'proceed.' She hears the difference. The corner of her mouth does not move. The quiet attention in her eyes adjusts."

    athought "She noticed the word choice. She approves of it. The approval is the warmest thing in this room and it is not warm."

    # ========== PHASE 5 -- THE OPENING ==========

    "Nyra lifts the box with both hands. She carries it to the low table. She sets it down. The wood touches the metal with a small dry sound."

    "She brings the candle next. Places it beside the box. The flame leans slightly toward the box and recovers."

    "Then she steps back from the table and looks at him across it."

    ny "I am going to open it. When I open it, you will see what is inside. You have already agreed to see it without knowing what it is. That is the first seal."

    a "I agreed."

    ny "Say it."

    a "I agreed to see it without knowing what it is."

    ny "Good."

    athought "Good. The word is so small. It lands in me like doctrine."

    "She opens the box."

    #play sound "sfx/one_shot/lacquer_box_open.ogg"

    "The hinge gives a single dry click. The lid lifts. He looks down."

    "Ash. Fine, pale grey, compacted into one corner of the box. It has been carried. It has been carried for a long time."

    athought "I have seen ash like this twice. Once on the hands of a cremation officer in the Academy infirmary. Once on Lyra's fingers the night she burned her mother's letters in the chapel brazier."

    athought "This is the second kind."

    "He does not ask again."

    # ========== PHASE 6 -- THE MARKING ==========

    "Nyra takes a pinch of the ash between her thumb and forefinger. The motion is practiced. She has done it before, for herself, in private. He can tell because her hand does not hesitate over the quantity."

    ny "Nyra is not a name tonight."

    "She steps around the low table. Not far -- she stops at arm's reach. The candle throws her face half in amber, half in blue. The blue dominates."

    ny "She is a temperature."

    athought "She is a temperature."

    athought "I do not know what to do with that sentence. I know what it means, and I do not know what to do with it."

    "She lifts her hand. Her thumb, darkened with ash. She does not touch him yet."

    ny "May I."

    a "Yes."

    "Her thumb settles on his forehead, above the left eye, below the hairline. She draws a short vertical line downward. Clean. Precise. The ash is dry. It does not smear."

    "She lifts her thumb away. She looks at her own work and is satisfied."

    ny "The door has been walked through."

    ny "Tonight it is closed."

    ny "There are three ways you can close it. I will offer them. You choose one."

    athought "My forehead is cold where the ash is. Or my skin is warm and the ash is the cold thing. I cannot tell which. It does not matter. The fact that I am thinking about it is the proof that she has already gotten into me."

    # ========== CONSENT GATE ==========

    ny "The first way is the cleanest. You say: seal it. You do not ask. You do not qualify. The rite takes us through."

    ny "The second way is slower. You say: let me understand what I am sealing first. We do not break the rite. We pause inside it. I will tell you what I can. What I cannot tell you, you must still accept, or the rite fails and you leave."

    ny "The third way."

    "A breath."

    ny "You say: I want this, but not as a ritual. As a woman and a man."

    ny "I will answer the third way. Then you will have to choose again. So choose."

    menu:
        "Her thumb is clean now. She wiped it on the cloth at her belt. She is waiting."

        "Seal it.":
            $ choice_and_dev(
                _current_scene_id, "_seal_it", "OB", factor=1,
                next_scene_label=None,
                note="Pure ceremony. Full submission to the ritual frame. Fastest path to sealing."
            )
            jump .seal_it

        "Let me understand what I am sealing first.":
            $ choice_and_dev(
                _current_scene_id, "_understand", "OB", factor=0,
                next_scene_label=None,
                note="Doubt acknowledged inside the frame. Ritual continues; she answers what she can."
            )
            jump .understand

        "I want this, but not as a ritual. As a woman and a man.":
            $ choice_and_dev(
                _current_scene_id, "_not_ritual", "OB", factor=-1,
                next_scene_label=None,
                note="Third-way attempt. Nyra refuses and forces reselection. Twice = dismissal."
            )
            jump .not_ritual

    # ========== BRANCH: NOT A RITUAL ==========
    label .not_ritual:

        a "I want this. But not as a ritual. As a woman and a man."

        "The room does not move. Nyra does not flinch. Her eyes do not even narrow. What happens in her face is quieter than that: a slight lowering of the lids, a very small tightening at the corner of the jaw. The face of someone correcting a student who has answered in the wrong language."

        ny "There is no woman and man in this room."

        ny "There is only the oath."

        ny "Choose again."

        athought "She did not raise her voice. She did not need to."

        athought "I can choose the third way again. I can walk out."

        athought "Or I can stay in the frame she has built for me."

        menu:
            "The candle flame is steady. The ash on his forehead is still cold."

            "Seal it.":
                $ choice_and_dev(
                    _current_scene_id, "_seal_it_after_defiance", "OB", factor=1,
                    next_scene_label=None,
                    note="Defied once, then submitted. She notes it."
                )
                jump .seal_it

            "Let me understand what I am sealing first.":
                $ choice_and_dev(
                    _current_scene_id, "_understand_after_defiance", "OB", factor=0,
                    next_scene_label=None,
                    note="Defied once, then asked to stay in frame with doubt. She notes it."
                )
                jump .understand

            "As a woman and a man. That is what I want.":
                $ choice_and_dev(
                    _current_scene_id, "_dismissed", "OB", factor=-2,
                    next_scene_label=None,
                    note="Dismissal path. She sends him away. Scene ends in the corridor."
                )
                jump .dismissed

    # ========== BRANCH: DISMISSED ==========
    label .dismissed:

        a "As a woman and a man. That is what I want."

        "Nyra closes the lacquered box."

        "She closes it with the same attention she used to open it. The hinge click is the same small dry sound, going in reverse."

        "She lifts the box from the low table. Carries it back to the desk. Sets it down. She does not look at him while she does this."

        ny "Then the oath does not seal tonight."

        ny "I will not be angry with you. Anger is not a thing I allow for this."

        ny "You will go to your quarters. You will wash your forehead. In the morning you will come to the ops table at 0700 and neither of us will mention tonight. Do you understand."

        a "I understand."

        ny "Go."

        "The door unseals. He turns and steps through it into the corridor. The door reseals behind him with the same small mechanical click it always makes."

        # --- CORRIDOR ---

        #scene bg_officers_corridor_ob_night with dissolve

        "The corridor is empty. The overhead strips hum at 30%%. He stands in the middle of the corridor with a line of ash on his forehead and no rite to attach it to."

        athought "My left hand is tremoring."

        athought "I press it flat against the corridor wall. The metal is cold. The tremor does not stop."

        athought "I wanted a woman. She offered me a temperature."

        athought "I do not yet know which of us was wrong."

        athought "I know that I am going to come back."

        athought "I know I will come back in a way that lets her finish what she started."

        athought "That is the thing I am going to have to examine later. Not tonight."

        "He walks the corridor back toward his own quarters. The sentries do not look at him. The base continues its skeleton shift. In Nyra's quarters, behind the sealed door, there is no sound."

        $ rel_bump("Nyra", respect=-1)
        $ flag("nyra_second_oath_refused", True)
        $ canon_set("ob.nyra.second_oath_sealed", False)
        $ canon_set("ob.nyra.second_oath_deferred", True)
        $ tp_seed("a4.ob.nyra.dismissed_in_corridor")
        $ npc_remember("Nyra", "sent_him_away_ash_on_forehead", tone="cold_patience")
        $ npc_remember("Aeron", "stood_in_corridor_with_ash", tone="unfinished")
        $ scene_mark(_current_scene_id, "completed")

        return

    # ========== BRANCH: UNDERSTAND ==========
    label .understand:

        a "Let me understand what I am sealing first."

        "Nyra tilts her head half a degree. It is her listening gesture. She permits the question."

        ny "You may ask what the rite permits."

        ny "What it does not permit, I will mark, and you will accept the mark."

        a "The ash. Where did it come from."

        ny "I told you I would not tell you tonight."

        ny "That is the mark. Accept it or we do not proceed."

        "A long silence. The candle flame holds."

        a "I accept it."

        ny "Good."

        a "The second oath. What does it bind that the first did not."

        "This question she answers."

        ny "The first oath bound service to the commander. Tonight binds the commander to the service."

        ny "In the first rite, I said: I follow you. My soldiers follow me. The chain is unbroken from this moment."

        ny "Tonight the chain closes. You are no longer a man who accepts service. You are the thing service is owed to. That is not the same sentence. It looks like the same sentence. It is not."

        athought "She is telling me the rite turns me into an institution."

        athought "Or confirms that I am already one and the ceremony is the admission."

        athought "I do not know which frightens me more. That is not true. I know which. I am not going to let myself name it tonight."

        a "One more."

        ny "One more."

        a "What happens if I fail the oath."

        "A silence longer than the first."

        ny "You cannot fail the oath tonight."

        ny "You can only fail to take it. Taking it is final. After tonight there is no place in the rite where failure is a door. You walk through rooms. The rooms do not have doors anymore."

        ny "Do you accept that."

        a "I accept it."

        ny "Then you have asked what the rite permits. What remains is the sealing. Do you seal it."

        athought "This is where the first way and the second way rejoin."

        athought "She gave me the doubt room. She let me speak the doubt. And now the doubt has been honored and the rite resumes."

        athought "That is more seductive than certainty. That is the thing I should have been afraid of."

        a "I seal it."

        $ rel_bump("Nyra", trust=1, respect=1)
        $ canon_set("ob.nyra.second_oath_doubt_acknowledged", True)

        jump .ritual_sealing

    # ========== BRANCH: SEAL IT ==========
    label .seal_it:

        a "Seal it."

        "Her eyes close for half a second. Not relief. Confirmation. When they open again there is something very quiet and very satisfied behind them."

        ny "Good."

        athought "Good. That word again. It is the only warm word she will give me tonight and it is not warm."

        $ rel_bump("Nyra", trust=2)
        $ canon_set("ob.nyra.second_oath_pure_ceremony", True)

        jump .ritual_sealing

    # ========== PHASE 7 -- THE RITUAL SEALING ==========
    label .ritual_sealing:

        "Nyra steps around the low table."

        "Not quickly. She moves the way she speaks -- in measured intervals, with the suggestion that each step has been approved by some authority older than either of them."

        "She stops in front of him. Her hand lifts to his collar. Her fingers find the top clasp the way her fingers found it the first night, in his quarters, weeks ago. But the gesture is different now. The first night her hand trembled at the moment of contact. Tonight there is no tremor. There is no gesture of arrival. There is only the work."

        ny "Permit me."

        a "Permitted."

        "The first clasp opens. A small metallic sound. She moves to the second."

        athought "My hand is not tremoring. That is the second thing I notice. The first is the ash on my forehead."

        athought "Her proximity is doing the thing it does. The static quiets. The edge of the world stops buzzing."

        athought "It is not relief. Relief is warm. This is the absence of friction."

        athought "I cannot tell anymore whether the absence of friction is mercy or erosion."

        "The second clasp. Third. The top of his uniform opens. Her hand rests, briefly, on the bare skin at the base of his throat. Not a caress. A palm-check. The way a medic confirms a pulse before deciding what the body is going to need."

        ny "The temperature is correct."

        athought "She says it the way she would call a range on a firing drill."

        athought "I am a temperature too. Tonight we are both temperatures."

        athought "I do not know when she erased the last of the personhood from this, or whether I was the one who permitted the erasure by showing up at 0128 to a one-word note."

        "Her other hand rises to his face. Her thumb touches the ash on his forehead. Not disturbing the line -- confirming it is still there. Then her palm settles on his cheek. The only warmth in the room is her hand, and the warmth is ritual warmth, the warmth of a tool that has been held."

        ny "Do you know why I am not kneeling tonight."

        a "No."

        ny "Because the first oath I knelt. Offering."

        ny "Tonight we stand. Confirming."

        ny "An offering is made by the lower to the higher. A confirmation is made between two who have agreed on what the higher is. That is the seal."

        athought "She is telling me I am not above her tonight. Nor she above me. Tonight we are both below the thing we have made, and the thing we have made is an institution with an altar in this room."

        athought "The altar is the low table. The candle. The box of ash."

        athought "The institution has no name yet. That is what tonight is for. To give it one."

        ny "Say my name."

        a "Nyra."

        ny "Say it correctly."

        athought "Correctly. She means the way she told me at the beginning. The thing that is not a name tonight."

        a "Temperature."

        ny "Yes."

        ny "You are also a temperature tonight. Say it."

        a "I am a temperature tonight."

        ny "Good."

        # ========== PHASE 8 -- THE INTIMATE SEQUENCE ==========

        # VISUAL: The low table is moved aside -- she moves it, one-handed, without
        # looking. The candle stays. The box of ash stays. Her hair comes down --
        # she pulls one pin, sets it on the desk, and the bun releases in three
        # sections. She does not shake her hair loose. She lets it fall.
        # The cot is made. It does not get unmade. The intimacy does not happen on
        # the cot. It happens standing at first, at the wall where the framed oath
        # text hangs, then against the desk. She chose those two surfaces because
        # they are the surfaces the room was built around. Everywhere else is
        # furniture. These two are the rite.
        # CAMERA: Same lens. Same color palette. No handheld. No drift. Close singles
        # during the physical exchange: her hand on his chest, her mouth against his
        # throat (the same placement as a3_s12, but tonight it is a confirmation,
        # not a discovery), his palm flat against the desk behind her. The shot
        # composition emphasizes right angles. The bodies make right angles against
        # the architecture of the room. That is the visual thesis of the scene.
        # BODIES AS ARCHITECTURE. Not heat. Not hunger. Geometry.

        "She moves the low table aside with her left hand. She does not look at it while she does it. The candle, the box, and the framed oath text are now the only objects the room admits."

        "She pulls one pin from her hair. Sets it beside the candle. Her hair releases in three sections and falls to her shoulders. She does not fix it. It is part of the rite now that it is down."

        "Her hand returns to his collar. The fourth clasp. The fifth."

        ny "I am going to touch you now. The touch is the sealing. After the touch there is no unsealing. Do you understand."

        a "I understand."

        ny "Say it the way the rite wants."

        a "After the touch there is no unsealing."

        ny "Yes."

        "Her mouth finds the side of his throat. Not a kiss. A placement. The same placement as the first night. Six weeks ago this was discovery. Tonight it is a signature in a place where her signature has been before."

        "His breath does not catch. That is the change. Six weeks ago the breath caught. Tonight his breathing stays even, because the evenness is the proof of the sealing, and the rite requires proof."

        athought "I did not let my breath catch. I am not sure whether I suppressed it or whether the thing in me that used to catch is not there anymore."

        athought "I will not know until much later whether the catch was the last piece of me that had not yet been copied into her handwriting."

        "Her hand flattens on his chest, between the opened clasps, palm to sternum. Her other hand stays on his face. She is touching him in two places, symmetrically. The symmetry is the point. The body as architecture. Right angles. Geometry."

        ny "The oath is closing."

        ny "Close it with me."

        # [INTIMATE CONTENT HERE]

    # ========== PHASE 9 -- AFTERCARE (COLD) ==========

        # VISUAL: Later. Same quarters. The candle-analog has burned lower but not
        # out. The low table has been returned to its position. The box of ash is
        # closed and back on the desk. Nyra is dressed again -- uniform re-clasped
        # to the collar, hair pinned back into the tight bun. She is not fixing
        # it in front of a mirror. She fixed it in the dark without looking. The
        # rite has taught her how to restore her own surface by touch.
        # Aeron stands in the middle of the room. His uniform is re-clasped to the
        # third clasp. Not the top. He has not re-fastened the top two. He is not
        # sure why. The ash is still on his forehead. He has not touched it.
        # CAMERA: Wide. Two figures in the blue. Nyra is at the window -- a small
        # reinforced port that looks onto the base yard below. She stands with her
        # back to him, one palm flat against the steel beside the window. She
        # does not look at the yard. She looks at her own palm against the steel.
        # She is back in command posture. The intimacy did not decommission her.
        # She has been restored to her function.

        "The candle flame has shrunk. The box on the desk is closed. The low table is back where it was when he entered. Nyra has pinned her hair back up. She is at the window now, her back to him."

        "Her palm is flat against the steel beside the reinforced port. She is not looking out. She is looking at the point where her hand meets the wall."

        athought "She does not look at me. That is the aftercare."

        athought "I did not expect her to. I am not disappointed. I am not relieved. I am cataloging."

        "She speaks without turning."

        ny "You will not come here again unless I call."

        ny "That is how this is."

        a "I know."

        ny "If you come here without being called, the door will not open for you. I will not punish you. The door simply will not open."

        ny "That is not a threat. That is the rite's edge. You are inside the rite or you are outside the rite. There is no casual inside."

        a "Understood."

        "A pause. Her palm adjusts a fraction of an inch against the steel -- a recalibration, the way a soldier resettles her grip on a rifle between drills."

        ny "You have questions you are not asking."

        a "I have. I will not ask them tonight."

        ny "Good."

        ny "Ask them at the next call. I may answer. I may mark the question and we will proceed."

        athought "She has already scheduled the next call. Tonight's call is not yet finished and the next one exists in her mind with a time attached."

        athought "I find this steadying. I find the steadiness alarming."

        athought "I am going to let the alarm stay unexamined until I am back in my own quarters, and then I am going to let it stay unexamined there also."

        ny "The ash on your forehead will stay there until 0500. At 0500 you will wash it off with water, not cloth. The cloth is a hand motion. The water is a dissolution. The rite prefers dissolution."

        a "At 0500. Water, not cloth."

        ny "Yes."

        "A longer pause. Her palm on the steel. The candle. The box of ash."

        ny "Go."

        "He does not speak again. He turns. He crosses the room. The door unseals for him on the way out -- she has released it by some control he does not see. The door closes behind him."

        # --- CORRIDOR BEAT (BRIEF) ---

        "In the corridor, at the first turn, he stops."

        athought "My left hand is not tremoring."

        athought "My forehead is cold where the ash is."

        athought "I can still feel the placement of her mouth on the side of my throat. The shape is precise. I could draw it."

        athought "Six weeks ago I would have called this weakness and suppressed the sensation."

        athought "Tonight I am permitted to feel it because feeling it is part of what the rite requires me to carry back through the corridors."

        athought "The rite is in me now. It walks me back to my quarters. I do not walk it."

        # --- NYRA ALONE ---

        # VISUAL: Return to her quarters. She is still at the window. The camera,
        # which has been with Aeron, returns to her for one shot. She has not moved.
        # Her palm is still flat against the steel. The candle has burned a little
        # lower. The box of ash sits closed on the desk. The framed oath text is
        # visible in the corner of the frame.

        #scene bg_nyra_quarters_window_alone_ob with dissolve

        "She stands at the window. The corridor outside her door is empty again. The base continues its skeleton shift."

        "She does not light a second candle. She does not sit. She does not re-open the box. She stays at the window, palm flat against steel, for a long time."

        nythought "He took the seal."

        nythought "He took it the way I needed him to take it. Not with faith -- with obedience. Faith would have been a weakness in him. Obedience is the stronger material."

        nythought "I performed the control. I performed it for him and I performed it for me. The performance is not a lie. The performance is the rite. The rite is the mechanism by which control becomes real."

        nythought "I am alone in the room again. The rite does not let me be less controlled alone than I was with him. That is the other seal. The seal on me."

        nythought "The ash was not who he thinks it was."

        nythought "I will tell him when the third rite is ready. Not before."

        nythought "Tonight the door is closed. Tonight I am a temperature. Tonight we are both temperatures."

        nythought "In the morning I will be a name again and he will be a commander again and neither of us will mention the ash and neither of us will need to."

        nythought "This is how it is now."

        "She lifts her palm from the steel. She walks to the desk. She extinguishes the candle-analog -- a single deliberate press of the switch, not a breath, not a pinch. The flame goes."

        "She sits at the desk in the dark. She does not turn on another light. She does not lie down. She sits."

        "Outside, the base keeps its night."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("nyra_second_oath_sealed", True)
    $ rel_bump("Nyra", trust=1, attraction=2)
    $ metric("nyra_intimacy_level", set_to=max(metric("nyra_intimacy_level"), 2))
    $ canon_set("ob.nyra.second_oath_sealed", True)
    $ canon_set("ob.nyra.temperature_not_name", True)
    $ tp_seed("a4.ob.nyra.temperature_not_name")
    $ npc_remember("Nyra", "second_oath_sealed_aeron_obeyed", tone="cold_satisfaction")
    $ npc_remember("Nyra", "the_ash_origin_withheld", tone="held_in_reserve")
    $ npc_remember("Aeron", "ash_on_forehead_tremor_stopped_again", tone="alarming_steadiness")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s11_nyra_second_oath_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Phase I of Act 4 OB. The night after a4_s10 (Noelle's blank authorization
#     drafting the civilian targeting doctrine). 0128 -- 0330 base time.
#   - Direct sequel to a3_s12 (first oath -- the door). This is the sealing.
# cann.what_happened:
#   - Nyra summons Aeron to her quarters with a one-line note: "Tonight."
#   - He comes. The arrival is part of the rite -- the one-word summons as a test
#     of his obedience, pre-rite.
#   - Her quarters are arranged as an altar: low table, candle, lacquered box.
#     The fractured Echelon crest from a3_s12 is ABSENT. She has graduated past it.
#   - Ritual: she opens the box. Inside: ash. She does not say of what.
#   - She marks his forehead with a streak of ash. "Nyra is not a name tonight.
#     She is a temperature."
#   - Consent gate, 3 OB-mode choices:
#       1. "Seal it." (pure ceremony; full submission to the frame)
#       2. "Let me understand what I am sealing first." (doubt inside the frame;
#          she answers some questions, marks others as non-negotiable)
#       3. "I want this, but not as a ritual. As a woman and a man." (Nyra refuses;
#          "There is no woman and man in this room. There is only the oath. Choose
#          again." Player must reselect. If they pick option 3 a second time, Nyra
#          dismisses him and the scene ends in the corridor with ash on his forehead.)
#   - All other paths lead to the ritual sealing and # [INTIMATE CONTENT HERE].
#   - Intimacy frame: bodies as architecture. Right angles. No heat. The touch
#     is a signature confirming a signature from six weeks ago (a3_s12).
#   - Aeron's breath does NOT catch -- the change from a3_s12 is the tell.
#   - Aftercare: Nyra re-dressed, hair re-pinned, standing at the window with her
#     back to him. "You will not come here again unless I call. That is how this is."
#     He agrees. She sends him out. Ash stays on his forehead until 0500 (water,
#     not cloth).
#   - Nyra alone: final beat. nythoughts reveal she performed the control for him
#     AND for herself. The rite makes control real. The ash was not who he thinks
#     it was. She will tell him at the third rite.
#   - Aeron in the corridor: the rite walks him back; he does not walk it.
# cann.aeron_state:
#   - OB deepened. Marcus idiom sharpened ("Proceed." "Permit." "Understood.").
#   - Tremor suppression is now PREDICTABLE in Nyra's presence -- no longer novel.
#     That predictability is the alarming thing, not the suppression itself.
#   - He is cataloging his own erosion in real time without intervening in it.
#   - The rite has begun to walk him. He has stopped walking the rite.
# cann.path_tracking_flags:
#   - Seal it: rel_bump("Nyra", trust=2), canon_set("ob.nyra.second_oath_pure_ceremony").
#   - Understand: rel_bump("Nyra", trust=1, respect=1),
#     canon_set("ob.nyra.second_oath_doubt_acknowledged").
#   - Not ritual x1 then reselect: factor=-1 on the first, then the chosen branch.
#   - Not ritual x2 (dismissal): rel_bump("Nyra", respect=-1),
#     flag("nyra_second_oath_refused"), canon_set("ob.nyra.second_oath_deferred").
#     The scene ends in the corridor with ash on his forehead.
#   - All sealing branches: flag("nyra_second_oath_sealed"),
#     rel_bump("Nyra", trust=1, attraction=2),
#     canon_set("ob.nyra.second_oath_sealed"), canon_set("ob.nyra.temperature_not_name"),
#     tp_seed("a4.ob.nyra.temperature_not_name").
# cann.thematic_flags:
#   - The lacquered box and the withheld ash: mystery planted for Phase II / Act 5.
#     Nyra knows whose ash it is. She is reserving the telling for a third rite.
#   - "She is a temperature." -- the erasure of personhood as the condition of
#     intimacy. OB intimacy as geometry, not encounter.
#   - The absent fractured crest: ritual escalation. She has moved past the first
#     altar to a new one.
#   - "After the touch there is no unsealing." -- the rite forbids retreat. This
#     is the rule Aeron will try to break later, and fail to.
#   - Nyra performing control for Aeron AND herself: the rite is also a cage on her.
#     She is not free. She is an instrument of an order she is also building.
#   - Aeron's non-catching breath: six weeks ago the catch was the last honest thing
#     in him during intimacy. Tonight there is no catch. Something has been copied.
# cann.character_moments:
#   - Nyra: "Nyra is not a name tonight. She is a temperature."
#   - Nyra: "There is no woman and man in this room. There is only the oath."
#   - Nyra: "You will not come here again unless I call. That is how this is."
#   - Aeron: "I am a temperature tonight." (said correctly, per the rite)
#   - Aeron (thought): "The rite walks me back. I do not walk it."
#   - Nyra (thought, alone): "The ash was not who he thinks it was."
# cann.block_status:
#   - VARIANT. Three consent-gate paths (+1 dismissal branch). Second Nyra erotic
#     on OB path. Sealing of the oath established in a3_s12.
# cann.requires_followup:
#   - The ash origin: Nyra's deferred reveal. Candidate: Act 5 third rite.
#   - Zira will learn about tonight by morning (a4_s12). The confrontation is
#     NOT about sex -- it is about the ritual, which is what Zira cannot compete with.
#   - "After the touch there is no unsealing" -- Aeron testing this rule later.
#   - Aeron's tremor suppression as Nyra-dependence: track for addiction arc.
#   - The dismissal branch (rare): if taken, Phase II opens on a different footing --
#     Aeron and Nyra cold without the second seal. Tracked by
#     canon_set("ob.nyra.second_oath_deferred").
