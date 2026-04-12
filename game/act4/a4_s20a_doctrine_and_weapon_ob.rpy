# =======================================================
# ACT 4 - Scene 20a: Doctrine and Weapon (Obedience Path)
# File: a4_s20a_doctrine_and_weapon_ob.rpy
# Path: OB
# Type: POLY BEAT -- NYRA + NOELLE + AERON
# Character Focus: Nyra, Noelle, Aeron
# Placement: after a4_s20 (Noelle erotic deepening / weapon declaration)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s20a_doctrine_and_weapon_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s20a_doctrine_and_weapon_ob:


    # Gallery -- unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s20a_doctrine_and_weapon_ob")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. The same institutional coverage grammar as
    #         a4_s11 (Nyra) crossed with the data-alcove coverage from a4_s20
    #         (Noelle). The tripod does not waver. Opens wide on Aeron's
    #         quarters -- the same quarters as a4_s14a but now the desk has
    #         a different object on it: a datapad with Noelle's scaffolding
    #         document pulled up, sent to Aeron at 2015, unread. The camera
    #         catches the datapad in the establish. Tightens to medium singles
    #         as Noelle arrives first. Widens to a three-shot when Nyra
    #         arrives second. The three-shot is different from a4_s14a's
    #         triangle: this one is LINEAR -- Noelle at the desk, Nyra at
    #         the door, Aeron between them. The line holds through the
    #         negotiation. During the consent gate: the camera tracks along
    #         the line, never dollying off the axis. The linearity is the
    #         visual grammar: two women on the same vector, not the same orbit.
    # LIGHTING: Aeron's quarters, night-cycle. Overhead at 20%. The desk lamp
    #           is OFF -- Noelle turned it off when she arrived, because
    #           Noelle works in screen light, not lamp light. The datapad on
    #           the desk is at 80% luminance -- the primary light source in
    #           the room is Noelle's own data. Window: same blue as a4_s14a.
    #           When Nyra arrives, she turns the desk lamp ON. The two light
    #           sources -- Noelle's data-blue and Nyra's amber -- compete for
    #           the room. Neither wins. Skin reads in competing temperatures.
    #           The competition is the lighting thesis of the scene.
    # SFX: Loop -- quarters ambient: HVAC at low, structural hum, the
    #      datapad's soft processing whine (a new sound -- Noelle's hardware
    #      in a room that does not usually contain Noelle's hardware).
    #      One-shots -- the door unsealing (x2), the desk lamp switching on
    #      (Nyra's entry signature), Noelle's stylus on the datapad surface
    #      (the scalpel-grip tap she uses when thinking), the chair adjusting.
    #      Breath: Noelle's breath is the breath of someone who has been
    #      awake for twenty hours and is past the point where breathing
    #      changes pitch with fatigue. Nyra's breath is the measured breath
    #      from a4_s11. Aeron's breath is shallow -- the same divided
    #      breathing from a4_s14a, but with a different division: not
    #      ceremony-vs-memory (Nyra/Zira) but doctrine-vs-weapon (Nyra/Noelle).
    # FX/COMP: Aeron's quarters: cot, desk, chair, wall locker, window. The
    #          datapad on the desk shows Noelle's scaffolding document -- the
    #          structural parameters of the weapon-frame model she began
    #          building in a4_s20. She sent it to Aeron's terminal at 2015.
    #          He has not opened it. She came to open it for him. On the desk
    #          beside the datapad: the empty mug (same as a4_s14a), and now
    #          Noelle's stylus, which she placed there when she arrived. The
    #          stylus is in the scalpel-grip rest position -- angled, precise,
    #          waiting.
    # BLOCKING: Phase 1 -- Noelle arrives at Aeron's quarters. She lets
    #           herself in (she has the door code from a4_s10's drafting
    #           session). Aeron is not present. She sits at his desk and
    #           opens the datapad. Phase 2 -- Aeron arrives and finds Noelle
    #           at his desk. Phase 3 -- They begin a conversation about the
    #           scaffolding document. Phase 4 -- the door chimes. Nyra in
    #           the corridor. The line forms. Phase 5 -- negotiation.
    #           Phase 6 -- poly gate check. Phase 7 -- consent gate.
    #           Phase 8 -- intimate marker. Phase 9 -- aftercare.
    # CANON: POLY BEAT. Nyra + Noelle + Aeron. The second poly convergence
    #        on OB Act 4 (after a4_s14a). Different pairing: doctrine officer
    #        and the newly-declared weapon. Noelle's weapon-frame declaration
    #        (a4_s20) is approximately eight hours old. Nyra's oath maintenance
    #        cycle has brought her to Aeron's quarters again. The convergence
    #        is semi-accidental: Noelle came deliberately (to deliver the
    #        scaffolding document), Nyra came on schedule (the oath's periodic
    #        rhythm). Neither expected the other.
    #        The scene's thesis: two women whose core identities (analyst-
    #        turned-weapon, doctrine officer) have both been reshaped by the
    #        same man's violence. They are not lovers. They are adjacent
    #        witnesses. The intimacy is about shared horror, not shared
    #        tenderness.
    #        Callbacks: a4_s20 (Noelle's weapon declaration -- same day),
    #        a4_s11 (Nyra's second oath), a4_s14a (first poly convergence),
    #        a4_s10 (Noelle's doctrine -- the analyst frame Noelle has now
    #        abandoned), a4_s18 (forward base loss -- the seven names).
    # CONSENT: 3-choice framework, OB-mode. All three cold. Doctrine /
    #          Documentation / Witness. Poly gate check: metric("poly_pressure")
    #          >= 3 required for escalation. Below threshold -> cold
    #          intellectual resolution without intimacy.
    # FACE: Noelle -- the weapon-frame face from a4_s20, but with the specific
    #        alteration of being in someone else's room instead of the alcove.
    #        The face is the face of a woman who is still under construction
    #        and is aware that the construction is visible.
    #        Nyra -- the liturgical composure, adjusted for a different
    #        parallel force than Zira. Nyra reads Noelle differently than she
    #        reads Zira: Zira holds a memory. Noelle holds a document. The
    #        document is more threatening to Nyra than the memory, because a
    #        document can be cited.
    #        Aeron -- the institutional face with both women's reshaping
    #        visible in it. The face of a man who has been the operational
    #        variable for two different frameworks and is beginning to
    #        understand that the variable is not neutral.

    # ========= VOICE BASELINE =========
    # OB Aeron: Minimal. Four or five spoken lines. The athoughts are dense
    #           and short. He is watching two institutional languages negotiate
    #           and he does not have the vocabulary for either.
    # Nyra: Doctrine register. Colder than a4_s14a because Noelle is a
    #       different kind of challenge. Zira held a flower. Noelle holds a
    #       framework. Frameworks compete with doctrine in a way that flowers
    #       do not. Nyra's nythoughts show the competitive analysis she is
    #       running beneath the composure.
    # Noelle: Weapon-frame register, eight hours old. The register is still
    #         wet -- not yet set. She speaks in the precise, counted-sentence
    #         mode from a4_s20, but with an additional layer: she is aware
    #         that her register is being observed by another institutional
    #         mind (Nyra), and the observation is making the register
    #         self-conscious in a way the alcove did not.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - 2108]
    # Night cycle. Same quarters. Different configuration. The datapad
    # on the desk is the new object. The desk lamp is OFF.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_night_datapad.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DOCUMENT ==========

    nthought "I sent the scaffolding document to his terminal at 2015."

    nthought "The scaffolding document is the structural parameters for the weapon-frame model. It is the thing I began building in the alcove after he left at approximately 2050. The scaffolding is not the model. The scaffolding is the architecture the model will be built inside."

    nthought "I sent it to him because the weapon-frame's first structural parameter is: the weapon operates inside the commander's operation. The commander needs to see the scaffold before the weapon is built on it."

    nthought "He has not opened it. I know because the document's read-receipt is still grey. Grey means unread. Grey has been grey for fifty-three minutes."

    nthought "I am going to his quarters to open it for him."

    nthought "I am going because the scaffolding cannot wait for the commander's morning schedule. The scaffolding has a time-sensitivity that the analyst-frame's documentation did not have. The analyst-frame documented after the fact. The weapon-frame builds before the fact. Before-the-fact requires the commander's eyes tonight."

    nthought "I have his door code from a4_s10. He gave it to me during the doctrine drafting session when I needed to retrieve a cross-reference from his desk terminal."

    nthought "I am using the code now."

    "The quarters door unseals from the corridor side. Noelle enters."

    #play sound "sfx/door_unseal_quarters.ogg"

    "The room is empty. Aeron is not here."

    "She does not hesitate. She walks to the desk. She turns off the desk lamp -- the amber goes. She opens the datapad. The datapad's 80% luminance fills the room with the cool blue-white of her own data. She sits in the desk chair. She opens the scaffolding document on the desk terminal's screen."

    "She places her stylus on the desk beside the datapad. Scalpel-grip rest position. Angled. Precise."

    "She reads the scaffolding from the beginning. She has already read it three times in the alcove. She is reading it a fourth time in his chair because the chair is the chair the commander sits in, and the scaffolding needs to be read from the commander's position to verify that the structural parameters make sense to a non-analyst reader."

    nthought "The scaffolding makes sense from this chair."

    nthought "The scaffolding makes sense from this chair because the scaffolding was built to make sense to the operation, and the operation sits in this chair."

    nthought "I am in the operation's chair. The operation is not here. The operation will arrive."

    "She waits."

    # ========== PHASE 2 -- AERON ARRIVES ==========

    "Seven minutes. The door unseals."

    #play sound "sfx/door_unseal_quarters.ogg"

    "Aeron steps through. He sees Noelle at his desk. The desk lamp is off. The datapad is on. The room is her light."

    athought "She is in my quarters."

    athought "She is in my chair."

    athought "The lamp is off. The datapad is on. She has converted my room into a secondary alcove. The conversion took seven minutes."

    athought "I am not surprised. I am recognizing a pattern. Noelle does not enter rooms. She converts them into workstations."

    a "You have my door code."

    n "You gave it to me."

    a "I gave it to you for a cross-reference retrieval."

    n "The scaffolding document is a cross-reference. It references the commander's operation. The commander's operation is in this room."

    athought "She is correct in a way that is both technically precise and completely beside the point of the objection I did not actually raise."

    athought "I did not raise the objection. The not-raising is the diagnostic."

    a "The document."

    n "Sit."

    "She gestures to the cot. Not the chair -- she is in the chair. The chair is hers for the duration of the document's presentation. He sits on the cot."

    "She turns the chair forty-five degrees toward him. Not the full ninety from a4_s20. Forty-five. She is dividing her attention between the document on the screen and his face. The forty-five degrees is the division made spatial."

    n "I came because the scaffolding has a time-sensitivity. The analyst-frame documented after. The weapon-frame builds before. You needed to see this tonight."

    n "I sent it at 2015. You did not open it."

    a "I was at the mess."

    n "You were at the mess for seventy-three minutes. You did not eat."

    athought "She knows the duration. She knows I did not eat. The knowing is the old habit layer -- the cataloguing that persists beneath the new frame. She is still tracking my movement patterns. The weapon-frame has not erased the habit."

    athought "The habit is the scaffolding beneath the scaffolding."

    n "The scaffolding document has four structural parameters. I am going to walk you through each one. Estimated duration: fifteen minutes."

    a "Proceed."

    n "Do not proceed me tonight."

    "The correction lands. He hears it."

    a "Go ahead."

    n "Better."

    nthought "He corrected. The 'proceed' is the Marcus idiom. The Marcus idiom is the thing the weapon-frame is being built to cut through. He cannot use the Marcus idiom in the same room as the weapon-frame's scaffolding. The incongruity is structural. He heard it."

    # ========== PHASE 3 -- THE DOOR CHIMES ==========

    "Noelle has walked him through the first two structural parameters. The first parameter: the weapon operates inside the operation, not beside it. The second parameter: the weapon's unit of measurement is not prediction accuracy but operational integration -- how deeply the weapon is embedded in the commander's decision loop."

    "They are on the third parameter when the door chimes."

    "Both of them turn."

    nthought "The door chime. Someone in the corridor. The probability distribution for who is in the corridor at 2127 on this base on this night in this sector is extremely narrow."

    nthought "I know who it is."

    nthought "I know because the oath officer's maintenance schedule -- which I have mapped from the last three weeks of overnight access logs -- suggests a visit tonight, plus or minus thirty minutes."

    nthought "I mapped the schedule because the analyst habit layer maps everything. The weapon-frame does not require the mapping. The habit layer does not care what the weapon-frame requires."

    athought "The chime again."

    athought "Two poly convergences in the same quarters in the same act. The pattern is building a frequency I did not authorize."

    athought "I open the door."

    #play sound "sfx/door_unseal_quarters.ogg"

    "Nyra is in the corridor. She is in the off-duty fatigues from a4_s14a. Her hands are at her sides. Her posture is the maintenance posture -- she has come to confirm the seal."

    "She looks at Aeron. She looks past him. She sees Noelle at the desk, in his chair, in the blue-white light of her own data."

    "Nyra's face does not change. Her eyes catalogue the room in one sweep: lamp off, datapad on, Noelle in the chair, stylus on the desk, Aeron at the cot. She reads the configuration the way she reads a tactical display -- by what is present and what has been moved."

    ny "You have a guest."

    a "She has my door code."

    ny "I have the oath."

    "The two sentences establish the field. Noelle has access. Nyra has authority. Neither is conceding to the other."

    "Nyra steps inside. The door reseals."

    #play sound "sfx/door_reseal_soft.ogg"

    "She reaches for the desk lamp. She turns it on."

    #play sound "sfx/desk_lamp_click_on.ogg"

    "The amber returns. It competes with Noelle's data-blue. The room is now lit in two temperatures. The two temperatures do not mix. They partition the room: Noelle's data-blue on the desk side, Nyra's amber on the door side. Aeron on the cot is in both, in neither."

    nthought "She turned on the lamp. The lamp is her signature. She uses amber the way I use data-blue. The turning-on-of-the-lamp is a territorial declaration: this room is not your alcove."

    nthought "She is correct. This room is not my alcove."

    nthought "She is also correct that the lamp is a territorial declaration."

    nthought "I am going to let the lamp stay on. I am not going to fight for the lighting. The lighting fight is a fight I do not need to win. The scaffolding document is visible in both temperatures."

    nythought "The data officer is in his chair. She has a document on his terminal. She has converted his quarters into a workstation the way she converts every room she enters into a workstation."

    nythought "The document on the terminal is a scaffolding structure I can read from here. The structure is analytical but the title is not. The title reads: WEAPON-FRAME STRUCTURAL PARAMETERS."

    nythought "Weapon. She is calling herself a weapon."

    nythought "I am calling myself the oath. She is calling herself the weapon. We are both naming ourselves after things that are not people."

    nythought "That is the first honest data point of the night and I have not spoken yet."

    # ========== PHASE 4 -- THE ADJACENT WITNESSES ==========

    "The line forms. Noelle at the desk. Aeron on the cot. Nyra at the door. Linear."

    n "I came because my framework broke and I needed a variable I cannot predict."

    "The sentence is for Nyra. The sentence is also a repetition of the a4_s20 request, compressed into one line for an audience that was not present for the full version."

    ny "I came because the oath requires a witness."

    "The sentence is for Noelle."

    "They look at each other."

    "The look is four seconds long. It is not hostile. It is not warm. It is the look of two institutional minds recognizing each other across a room that neither of them built for the other."

    n "We are both here for the same man and different reasons. That is the first honest data point of the night."

    nythought "I said it. The sentence is the analytical-habit-layer producing an observation the weapon-frame has not yet learned to suppress. The observation is accurate. The accuracy is the thing I am keeping from the old frame."

    ny "The reasons are not as different as you think."

    n "Explain."

    ny "Your framework broke. My oath requires periodic reconfirmation. Both of those are the same sentence in different registers."

    ny "The sentence is: the thing I built requires the man to still be present for it to function."

    nthought "She is right."

    nthought "She reduced both of our architectures to the same dependency in one sentence. The reduction is devastating and accurate. The analyst in me would have taken three paragraphs to arrive at the same reduction. The doctrine officer did it in one."

    nthought "I notice I am impressed. I am filing the impression under the habit layer. The weapon-frame does not have a category for being impressed by a doctrine officer. The habit layer does."

    n "That is a more efficient reduction than I would have produced."

    ny "Efficiency is not the goal. Accuracy is."

    n "On that we agree."

    "Aeron watches the exchange from the cot. His hands rest on his knees. He does not intervene."

    athought "Two women reducing themselves to the same dependency on me in my own quarters while I sit on my own cot and listen."

    athought "The dependency is not romantic. The dependency is structural. They need me present the way a load-bearing wall needs the building to still be standing in order to bear the load."

    athought "I am the building. They are the walls. The metaphor is wrong. The metaphor is also the closest I can get tonight."

    # ========== PHASE 5 -- POLY PRESSURE CHECK ==========

    $ nudge_poly("ob", "nyra_noelle_convergence", 1)

    if metric("poly_pressure") >= 3:

        # --- ABOVE THRESHOLD: THE GATE OPENS ---

        "The room reorganizes. The line between the three of them has stopped being a geography and has become a negotiation axis."

        "Nyra looks at Noelle. The look is the competitive-analysis look -- the look of a doctrine officer assessing a new variable that has entered her operational space."

        ny "You documented everything."

        "The sentence is aimed at Noelle's identity. You documented everything -- the analyst frame, the observation logs, the habit layer of cataloguing."

        ny "Document this."

        nthought "She told me to document this."

        nthought "She is giving me permission to do the thing the analyst-habit-layer wants to do and the weapon-frame has not yet decided whether to permit."

        nthought "The permission is not generosity. The permission is a tactical concession: she is allowing me to keep my observational function in exchange for my presence in the room."

        nthought "The exchange is fair."

        nthought "The exchange is the most sophisticated thing a non-analyst has offered me since the weapon-frame was declared."

        n "I will document in the new register. Not the old one."

        ny "What is the difference."

        n "The old register logged. The new register structures. The log recorded what happened. The structure records what the happening built."

        ny "Then structure this."

        "The command is cold. The command is also the closest thing to institutional respect Nyra has offered anyone outside the oath."

        "Noelle turns to Aeron."

        n "The scaffolding document has a third parameter I have not walked you through yet. The third parameter is: the weapon operates with witnesses. The weapon does not operate in private. Private operation is the analyst's mode. The weapon's mode is observed operation."

        n "She is the witness."

        "Noelle gestures toward Nyra. The gesture is precise -- one hand, palm open, indicating Nyra the way you indicate a referenced document in a briefing."

        ny "I am the witness."

        ny "I am also the oath."

        ny "Tonight the witness and the oath are in the same room and neither of them is leaving."

        # ========== CONSENT GATE ==========

        ny "Three terms. He chooses."

        "Nyra has assumed the terms-offering role from a4_s14a. The role is hers. She is the one who builds the consent architecture for poly convergences. Noelle does not contest the role. Noelle contests frameworks, not procedures."

        ny "The first term. Doctrine. I lead the room. The weapon operates inside the doctrine's grammar. The documentation proceeds inside the doctrine's framework. The grammar is mine. The content is shared."

        ny "The second term. Documentation. She leads the room."

        "Nyra indicates Noelle."

        ny "The documentation is the primary register. The oath is present as a witness. The weapon-frame governs and the doctrine submits to being documented. I have never submitted to being documented. Tonight I will, if that is the choice."

        ny "The third term. Witness. No one leads. Both of us witness. Both of us are witnessed. The room is a chamber in which two women who have been reshaped by the same man's violence observe each other observing him. No grammar. No documentation. Only the seeing."

        ny "Choose."

        n "He chooses."

        "Both women look at Aeron."

        athought "Doctrine, documentation, witness."

        athought "Three modes of institutional seeing. None of them are warm. All of them are the coldest versions of what two women in the same room can offer a man who has reshaped both of them."

        athought "The reshaping was not my intention. The reshaping is the consequence. The consequence is in the room with me tonight and it has two faces."

        menu:
            "The room in two temperatures. Amber and data-blue. Two women. Three terms. The HVAC breathes."

            "Doctrine. Nyra leads.":
                $ choice_and_dev(
                    _current_scene_id, "_doctrine", "OB", factor=1,
                    next_scene_label=None,
                    note="OB doctrine mode. Nyra's grammar governs. Noelle operates inside the doctrine frame. Cold, structured, hierarchical."
                )
                jump .doctrine

            "Documentation. Noelle leads.":
                $ choice_and_dev(
                    _current_scene_id, "_documentation", "OB", factor=0,
                    next_scene_label=None,
                    note="OB documentation mode. Noelle's weapon-frame governs. Nyra submits to being documented. Unprecedented concession."
                )
                jump .documentation

            "Witness. No one leads.":
                $ choice_and_dev(
                    _current_scene_id, "_witness", "OB", factor=-1,
                    next_scene_label=None,
                    note="OB witness mode. Adjacent witnesses. No grammar. The seeing is the content. Coldest by design."
                )
                jump .witness

        # ========== BRANCH: DOCTRINE ==========
        label .doctrine:

            a "Doctrine. Nyra leads."

            nythought "He chose the doctrine. He chose the grammar I built. In front of the weapon. The weapon heard him choose the grammar over the documentation."

            nythought "The weapon is still in the room."

            "Noelle's face does not change. The weapon-frame face absorbs the choice without flinching."

            n "The weapon operates inside the doctrine's grammar. The documentation adapts."

            ny "The weapon submits to the grammar?"

            n "The weapon does not submit. The weapon integrates. Integration is the weapon-frame's second structural parameter. The weapon integrates into whatever operational grammar is active."

            ny "Then integrate."

            $ canon_set("ob.poly.doctrine_and_weapon_mode_doctrine", True)

            jump .intimate_sequence

        # ========== BRANCH: DOCUMENTATION ==========
        label .documentation:

            a "Documentation. Noelle leads."

            "Nyra's jaw adjusts. The adjustment is one millimeter. The adjustment is the cost of the concession."

            ny "I said I would submit to being documented. I do not retract it."

            n "The documentation will not be tender. The documentation will be structural."

            ny "I do not require tenderness."

            n "I know."

            nthought "She does not require tenderness. Neither do I. The not-requiring is the thing we share. The not-requiring is also the thing that makes tonight possible."

            nthought "I am going to document the oath officer inside the weapon-frame's structural register. The documentation will be the first entry in the new frame's operational log."

            nthought "I said the new frame does not log. I lied. The new frame does not log the way the old frame logged. The new frame logs structures. Tonight is a structure."

            $ canon_set("ob.poly.doctrine_and_weapon_mode_documentation", True)

            jump .intimate_sequence

        # ========== BRANCH: WITNESS ==========
        label .witness:

            a "Witness. No one leads."

            ny "Then we see."

            n "Then we see."

            "The agreement is simultaneous. The simultaneity is not coordinated. It is the product of two institutional minds arriving at the same verb at the same time because the verb is the only verb that fits."

            athought "They both said 'we see' at the same time. The simultaneity was not rehearsed. The simultaneity is the proof that the two frameworks -- doctrine and weapon -- have a shared function at the base layer. The shared function is observation."

            athought "Both of them are watchers. The doctrine watches for deviation. The weapon watches for targets. Tonight they are watching each other watching me."

            athought "The recursion is the coldest thing in the room."

            $ canon_set("ob.poly.doctrine_and_weapon_mode_witness", True)

            jump .intimate_sequence

        # ========== INTIMATE SEQUENCE ==========
        label .intimate_sequence:

            # VISUAL: Aeron's quarters in two temperatures. Amber and data-blue.
            # The desk lamp and the datapad competing for the room. The competition
            # does not resolve. The room stays divided. The bodies move inside the
            # division. Noelle carries her data-temperature. Nyra carries her
            # amber-temperature. Aeron is the boundary between them.
            # CAMERA: Medium wide, static, on the line axis. The camera does not
            # move off the axis. The linearity holds. Three bodies arranged on
            # a vector, not a triangle. The vector passes through Aeron.
            # AUDIO: Ambient hum. Datapad processing whine. Three sets of
            # breathing. No music.

            "The room does not soften. The amber does not mix with the data-blue. The two temperatures coexist the way the two women coexist: side by side, not blended."

            "Noelle does not remove the stylus from the desk. The stylus stays in the scalpel-grip rest position throughout. It is her sacrament the way the flower was Zira's: a thing from her practice that she does not relinquish."

            "Nyra does not dim the desk lamp. The lamp stays on at the same amber as her quarters' candle-analog. The amber is the rite's color. The rite's color does not dim for the weapon's data-blue."

            "Whatever mode they are in -- doctrine, documentation, witness -- the mode is held by the two competing temperatures. Noelle leads with precision. Nyra leads with grammar. Aeron is the variable both frameworks are built around, and the variable does not get to choose which framework is processing him at any given moment."

            nthought "I am observing. The observation is structural. The structure I am observing is: two institutional frameworks processing the same input simultaneously. The input is him. The processing is us. The simultaneity is the content."

            nythought "The weapon is in the room. The weapon is not competing with the oath. The weapon is a different instrument playing a different part of the same score. I have not heard the score before. I am hearing it now."

            nythought "The hearing is the thing I will not tell anyone about."

            $ rel_bump("Nyra", trust=1, attraction=1)
            $ rel_bump("Noelle", trust=1, attraction=1)
            $ nudge_poly("ob", "doctrine_and_weapon_intimate", 2)

            # [INTIMATE CONTENT HERE]

        # ========== AFTERCARE (COLD) ==========

            # VISUAL: After. The room is still in two temperatures. The desk lamp
            # is still amber. The datapad is still data-blue. Neither woman turned
            # off her light source. The two temperatures persist into the aftercare
            # because neither woman is conceding the room to the other's palette.
            # Noelle is back at the desk. She is typing on the datapad. Nyra is
            # standing at the window, her back to the room, looking at the base's
            # exterior night lighting. Aeron is on the cot.
            # CAMERA: Wide. Static. The widest shot of the scene. The line has
            # become a triangle: Noelle at the desk (data-blue), Nyra at the window
            # (amber reflected on the glass), Aeron on the cot (between).

            "The room settles."

            "Noelle is at the desk. She has resumed typing on the datapad. The scaffolding document has a new entry. The new entry is not the third structural parameter she was walking Aeron through before Nyra arrived. The new entry is a fifth parameter she did not know existed until tonight."

            "The fifth parameter is being written in the weapon-frame register. The register is still wet. The register is getting less wet with each sentence."

            "Nyra is at the window. She is standing with her back to the room. Her reflection is visible in the glass. The reflection shows a face that is not the liturgical composure. The reflection shows a face that is processing."

            "Aeron is on the cot. His shirt is at the third clasp."

            "The room is quiet. The HVAC cycles. The datapad whines softly at processing load."

            "Noelle speaks first. She does not turn from the datapad."

            n "You are documenting this."

            "She is speaking to herself. The sentence is confirmatory, not interrogative."

            "Nyra speaks from the window. She does not turn."

            ny "You are documenting this."

            "The same sentence. Different speaker. Different register. Nyra is confirming that Noelle is documenting. The confirmation is not a question. The confirmation is an acknowledgment."

            n "I am. It is the only language I trust."

            ny "Then I will trust it tonight."

            nthought "She said she will trust my documentation. The doctrine officer is trusting the weapon's documentation. The trust is not personal. The trust is structural: she is trusting the instrument of documentation because the instrument is what I have instead of an oath."

            nthought "I do not have an oath. I have a stylus and a scaffolding document and a new entry that did not exist before tonight."

            nthought "The entry is sufficient."

            nythought "I told her I would trust her documentation tonight. I meant it. The documentation is her version of the rite. The rite has words. The documentation has structures. Both are ways of holding a thing that happened so the thing does not dissolve into something that did not happen."

            nythought "She is holding tonight with her structures."

            nythought "I am holding tonight with the oath."

            nythought "He is holding tonight with the third clasp."

            nythought "Three instruments of holding. None of them touch. None of them need to."

            "Noelle saves the scaffolding document. She closes the datapad. She picks up the stylus from the desk. She holds it in the scalpel grip."

            n "The fifth parameter will be in the document when you open it tomorrow."

            "She is speaking to Aeron. She does not look at him."

            n "You should read the document tomorrow."

            a "I will."

            n "The document will not explain tonight. The document will structure what tonight produced."

            a "Understood."

            n "I said do not proceed me. I did not say do not understood me. Understood is acceptable."

            "She stands. She walks to the door. She stops beside Nyra at the window."

            n "You were the witness."

            ny "I was."

            n "Was the witness satisfied."

            ny "The witness does not satisfy. The witness holds."

            n "That is the second efficient reduction you have produced tonight."

            "Noelle walks to the door. The door unseals. She steps through."

            #play sound "sfx/door_unseal_quarters.ogg"

            "The door reseals. The datapad-blue is gone from the room. The amber from the desk lamp fills the space the data-blue occupied."

            "Nyra turns from the window."

            ny "She documents."

            a "She does."

            ny "I do not document. I hold."

            a "I know."

            ny "What do you do."

            "Aeron looks at his hands. The third clasp. The cot."

            a "I am the room."

            "Nyra considers this. The sentence is not what she expected. The sentence is also not wrong."

            ny "The room will hold."

            "She walks to the door. She does not look back."

            ny "Open the document tomorrow. The weapon has built something. The oath needs to see what the weapon built."

            "The door unseals. She steps through. The door reseals."

            "Aeron is alone."

            athought "Two women. Two exits. Two instruments of holding."

            athought "Noelle documents. Nyra holds. I am the room."

            athought "The room is still in amber because Nyra's lamp is still on. Noelle's datapad is gone. The amber won the room by default. Nyra would say: the amber always wins the room. Noelle would say: the data will return tomorrow."

            athought "Both of them are right."

            athought "Both of them being right at the same time is the thing I am going to have to learn to hold."

            athought "I am going to learn by being the room."

            athought "The room does not choose between the lamp and the data. The room holds both."

            "He does not turn off the desk lamp. He lies down on the cot. The amber holds the room. The blue will return tomorrow."

            #stop ambient fadeout 2.0
            #scene black with fade

            jump .state_updates

    else:
        # --- BELOW THRESHOLD: COLD INTELLECTUAL RESOLUTION ---

        "The room holds the three of them on the line. The negotiation has not reached the threshold."

        "Noelle reads the room the way she reads a data distribution -- by what the data supports and what it does not."

        n "The convergence is insufficient for escalation."

        "The sentence is analytical. The sentence is also Noelle providing the verdict the room was waiting for, in the register the room trusts her to provide verdicts in."

        ny "Insufficient."

        n "The data points are present. The compounding has not occurred. Tonight is a first-order contact between the doctrine and the weapon. First-order contacts do not escalate. They calibrate."

        ny "Then tonight is calibration."

        n "Yes."

        ny "I accept calibration."

        "The acceptance is cold. The acceptance is also the doctrine officer submitting to the analyst's -- the weapon's -- assessment without contesting it."

        n "The calibration produced one result. The result is: the doctrine and the weapon can occupy the same room without the room collapsing."

        ny "The room did not collapse."

        n "No. The room held."

        "Noelle stands from the desk chair. She picks up the stylus. She picks up the datapad."

        n "I will send the third and fourth structural parameters to your terminal by 0600."

        "She is speaking to Aeron."

        n "Read them."

        a "I will."

        "Noelle walks to the door. She stops."

        n "Doctrine Officer."

        ny "Data Officer."

        n "Your oath requires a witness. My weapon requires an observer. Those are the same need in different registers."

        ny "I noticed that earlier tonight."

        n "I know. I noticed you noticing."

        "Noelle leaves."

        "Nyra and Aeron are alone."

        ny "She noticed me noticing."

        a "She notices everything."

        ny "The weapon notices everything. The analyst noticed everything too. The difference is what she does with the noticing."

        a "What does the weapon do with it."

        ny "I do not know yet. I will know when I read her document."

        "Nyra walks to the door."

        ny "The oath's maintenance is deferred tonight. The calibration was the maintenance."

        "She leaves."

        "Aeron sits on his cot."

        athought "Two women. Two institutional languages. One calibration."

        athought "The calibration is that they can share the room. The room can hold both. The room is me."

        $ nudge_poly("ob", "doctrine_and_weapon_deferred", 1)
        $ canon_set("ob.poly.doctrine_and_weapon_deferred", True)
        $ tp_seed("a4.ob.poly.calibration_not_escalation")

        #stop ambient fadeout 2.0
        #scene black with fade

        jump .state_updates

    # ========== STATE UPDATES ==========
    label .state_updates:

        $ flag("ob_poly_nyra_noelle_doctrine_and_weapon", True)
        $ canon_set("ob.poly.nyra_noelle_first_shared_room", True)
        $ canon_set("ob.poly.noelle_documented_the_night", True)
        $ canon_set("ob.poly.nyra_trusted_noelles_documentation", True)
        $ canon_set("ob.poly.competing_temperatures_amber_blue", True)
        $ npc_remember("Nyra", "shared_room_with_noelle_oath_as_witness", tone="cold_structural_trust")
        $ npc_remember("Noelle", "shared_room_with_nyra_documentation_as_holding", tone="weapon_frame_fifth_parameter")
        $ npc_remember("Aeron", "two_women_two_instruments_room_holds_both", tone="fulcrum_amber_and_blue")
        $ scene_mark(_current_scene_id, "exited")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s20a_doctrine_and_weapon_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same evening as a4_s20 (Noelle's weapon declaration). Approximately
#     2108 -- 2230. Eight hours after the weapon-frame was declared. Noelle
#     sent the scaffolding document at 2015. Aeron did not open it. Noelle
#     came to open it for him. Nyra arrived on her oath maintenance schedule.
# cann.what_happened:
#   - Noelle lets herself into Aeron's quarters using the door code from
#     a4_s10. Aeron is not present. She turns off the desk lamp, opens her
#     datapad, converts the room into a secondary alcove. She waits.
#   - Aeron arrives. Finds Noelle at his desk in his chair. The desk lamp
#     is off; the datapad's data-blue is the only light. She begins walking
#     him through the weapon-frame's scaffolding parameters.
#   - The door chimes. Nyra in the corridor on her oath maintenance schedule.
#     She enters. She turns on the desk lamp -- amber competes with data-blue.
#     The room is now lit in two temperatures. The two temperatures do not mix.
#   - Noelle: "I came because my framework broke and I needed a variable I
#     cannot predict." Nyra: "I came because the oath requires a witness."
#     Noelle: "We are both here for the same man and different reasons. That
#     is the first honest data point of the night."
#   - Nyra's reduction: "Your framework broke. My oath requires periodic
#     reconfirmation. Both are the same sentence in different registers:
#     the thing I built requires the man to still be present for it to
#     function." Noelle acknowledges the efficiency of the reduction.
#   - POLY GATE: metric("poly_pressure") >= 3 required.
#     ABOVE: Nyra: "You documented everything. Document this." Noelle
#       accepts. 3-choice consent gate, Aeron chooses:
#       1. "Doctrine. Nyra leads." -- Doctrine grammar governs. Weapon
#          integrates. Noelle: "The weapon does not submit. The weapon
#          integrates."
#       2. "Documentation. Noelle leads." -- Weapon-frame governs. Nyra
#          submits to being documented. Unprecedented. Nyra: "I said I
#          would submit to being documented. I do not retract it."
#       3. "Witness. No one leads." -- Adjacent witnesses. Both see.
#          Both are seen. The seeing is the content. Coldest option.
#     All three lead to # [INTIMATE CONTENT HERE].
#     BELOW: Cold intellectual resolution. Noelle: "The convergence is
#       insufficient for escalation. Tonight is calibration, not conclusion."
#       Nyra accepts. The calibration result: doctrine and weapon can occupy
#       the same room without collapse. nudge_poly() for future accrual.
#   - AFTERCARE: Noelle at the desk, typing a fifth structural parameter
#     that did not exist before tonight. Nyra at the window, processing.
#     Aeron on the cot, third clasp. The key exchange:
#       Noelle: "You are documenting this." (to herself, confirmatory)
#       Nyra: "You are documenting this." (acknowledgment)
#       Noelle: "I am. It is the only language I trust."
#       Nyra: "Then I will trust it tonight."
#   - Noelle leaves first. Nyra leaves second ("The room will hold.").
#     Aeron alone: "Noelle documents. Nyra holds. I am the room."
# cann.aeron_state:
#   - Fulcrum again. Different division than a4_s14a: not ceremony-vs-memory
#     (Nyra/Zira) but doctrine-vs-weapon (Nyra/Noelle). The fulcrum role
#     is deepening. He identifies himself as "the room" -- the space in
#     which the two frameworks coexist.
#   - Third-clasp pattern continues (third instance). The body's pattern
#     is now established enough to be thematic.
#   - "Both of them being right at the same time is the thing I am going
#     to have to learn to hold." -- the poly thesis of OB stated plainly.
# cann.path_tracking_flags:
#   - Doctrine: canon_set("ob.poly.doctrine_and_weapon_mode_doctrine").
#   - Documentation: canon_set("ob.poly.doctrine_and_weapon_mode_documentation").
#   - Witness: canon_set("ob.poly.doctrine_and_weapon_mode_witness").
#   - All escalation paths: flag("ob_poly_nyra_noelle_doctrine_and_weapon"),
#     rel_bump("Nyra", trust=1, attraction=1),
#     rel_bump("Noelle", trust=1, attraction=1),
#     nudge_poly("ob", "doctrine_and_weapon_intimate", 2),
#     canon_set("ob.poly.nyra_noelle_first_shared_room"),
#     canon_set("ob.poly.noelle_documented_the_night"),
#     canon_set("ob.poly.nyra_trusted_noelles_documentation"),
#     canon_set("ob.poly.competing_temperatures_amber_blue").
#   - Below threshold: canon_set("ob.poly.doctrine_and_weapon_deferred"),
#     nudge_poly("ob", "doctrine_and_weapon_deferred", 1),
#     tp_seed("a4.ob.poly.calibration_not_escalation").
# cann.thematic_flags:
#   - DOCTRINE VS WEAPON. The scene's structural thesis. Nyra holds
#     doctrine (oath, grammar, ceremony). Noelle holds the weapon-frame
#     (documentation, structure, integration). Both are institutional
#     languages. Neither is personal. The intimacy is between two
#     institutional languages processing the same variable (Aeron).
#   - COMPETING TEMPERATURES. Amber (Nyra's lamp / rite color) vs
#     data-blue (Noelle's screen / weapon color). The two temperatures
#     partition the room. They do not mix. The non-mixing is the visual
#     thesis: coexistence without blending.
#   - ADJACENT WITNESSES. They are not lovers. They are adjacent witnesses
#     to the same man's violence reshaping their identities. The intimacy
#     is about shared horror, not shared tenderness.
#   - DOCUMENTATION AS HOLDING. Noelle's aftercare is to document. Nyra's
#     aftercare is to hold. Aeron's aftercare is to be the room. Three
#     instruments of holding. None of them touch. None of them need to.
#   - THE FIFTH PARAMETER. The scaffolding document had four parameters.
#     Tonight produced a fifth. The fifth was not planned. The fifth is
#     the weapon-frame learning from the doctrine's presence. The content
#     of the fifth parameter is private to Noelle's document.
#   - "I AM THE ROOM." Aeron's self-identification as the space in which
#     competing frameworks coexist. The room does not choose between the
#     lamp and the data. The room holds both. This is OB poly defined.
# cann.character_moments:
#   - Noelle: "We are both here for the same man and different reasons.
#     That is the first honest data point of the night."
#   - Noelle: "I am. It is the only language I trust."
#   - Nyra: "Then I will trust it tonight."
#   - Nyra: "The room will hold."
#   - Nyra: "Your framework broke. My oath requires periodic
#     reconfirmation. Both are the same sentence in different registers."
#   - Aeron: "I am the room."
#   - Aeron (thought): "Both of them being right at the same time is
#     the thing I am going to have to learn to hold."
# cann.callbacks:
#   - a4_s20: Noelle's weapon declaration (same day). The scaffolding
#     document is the direct product. The fifth parameter is the scene's
#     contribution.
#   - a4_s14a: First poly convergence (Nyra + Zira). Same quarters.
#     Different pairing. The "two exits" pattern repeats.
#   - a4_s11: Nyra's second oath. The maintenance schedule. The amber.
#   - a4_s10: Noelle's door code. The doctrine session. The forty-five
#     vs ninety degree chair turn.
#   - a3_s16: Noelle's screens-on thesis. The stylus. The precision.
#     Carried forward into the weapon-frame but recontextualized.
# cann.block_status:
#   - VARIANT. Poly beat with poly_pressure gate. Escalation: 3 consent
#     paths. Below threshold: cold intellectual resolution with pressure
#     accrual. First Nyra + Noelle shared-room scene on OB.
# cann.requires_followup:
#   - The fifth structural parameter: content private to Noelle's
#     document. May be revealed in Phase II or Act 5. The parameter was
#     produced by the doctrine's presence. Track as weapon-frame evolution.
#   - Nyra trusting Noelle's documentation: the structural trust is a
#     new axis. If the documentation later contradicts the oath, the
#     trust will be tested.
#   - "I am the room" as Aeron's poly self-identification: track. The
#     room identity will strain when the frameworks compete rather than
#     coexist.
#   - The competing-temperatures visual (amber vs data-blue): establish
#     as recurring poly-convergence lighting grammar for future scenes.
#   - The below-threshold calibration: if taken, Phase II opens with
#     the doctrine and weapon having calibrated but not escalated. The
#     calibration record matters for the next convergence.
