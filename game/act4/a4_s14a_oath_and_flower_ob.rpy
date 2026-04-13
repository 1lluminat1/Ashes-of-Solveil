# =======================================================
# ACT 4 - Scene 14a: Oath and Flower (Obedience Path)
# File: a4_s14a_oath_and_flower_ob.rpy
# Path: OB
# Type: POLY BEAT -- NYRA + ZIRA + AERON
# Character Focus: Nyra, Zira, Aeron
# Placement: after a4_s14 (Lyra sanctifying violence)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s14a_oath_and_flower_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s14a_oath_and_flower_ob:


    # Gallery -- unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s14a_oath_and_flower_ob")
    $ show_timeline("DAY 49", "22:00", "Phoenix Base — Aeron's Quarters")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Institutional coverage. The lens grammar of
    #         a4_s11 (Nyra's quarters) crossed with the a4_s13 workshop coverage.
    #         Neither woman's camera vocabulary dominates. The tripod is the
    #         compromise -- neither handheld (Zira's territory) nor fully static
    #         (Nyra's temple). Opens wide on Aeron's quarters: the door, the cot,
    #         the desk, the window showing the base exterior at 2340. Tightens to
    #         a medium two-shot when Nyra is revealed already inside. Widens to
    #         a three-shot when Zira enters. The three-shot holds for the
    #         negotiation. During the consent gate: medium singles cycling between
    #         all three, never resting on one for more than three seconds. The
    #         composition is triangular, unstable, load-bearing. After the gate:
    #         the camera retreats to medium wide and does not follow them. The
    #         aftercare is wide and still.
    # LIGHTING: Aeron's quarters at night-cycle. Overhead at 20% -- the dimmer
    #           setting he uses when he is not working. The desk lamp (amber,
    #           military-issue) is on. One window: the exterior blue of the base's
    #           night lighting. Amber from the desk, blue from the window, the
    #           overhead at 20%. The three light sources never mix warmly. Skin
    #           reads cold. The amber is functional, not romantic. The blue is
    #           institutional, not atmospheric. This is the room of a man who did
    #           not arrange it for company.
    # SFX: Loop -- quarters ambient: HVAC at low cycle, the structural hum of
    #      the base's night-shift systems, a distant bootfall that passes and
    #      does not return. One-shots -- the door unsealing (mechanical click),
    #      Zira's entry (a second mechanical click, the re-seal), the scrape of
    #      a chair on the deck when Nyra adjusts her position, Zira's boot on
    #      the threshold. Breath: three distinct registers when all three are in
    #      the room. Nyra's measured. Zira's held. Aeron's the shallowest of the
    #      three because he is dividing his attention between two different
    #      gravitational centers and neither one is letting him settle.
    # FX/COMP: Aeron's quarters: standard officer's room. Cot, desk, chair, wall
    #          locker, the window. On the desk: a datapad (dark), an empty mug,
    #          the desk lamp. The ash mark from a4_s11 is NOT on his forehead
    #          tonight -- he washed it at 0500 as instructed. But the ghost of it
    #          is in the room because Nyra is in the room and Nyra IS the ash.
    #          Zira: her left hand is closed around something small in her jacket
    #          pocket. The camera catches the fist-in-pocket in the wide shot. The
    #          pressed flower from a4_s05 / a4_s13 is in that fist. She brought
    #          it without deciding to. The flower does not leave her palm for the
    #          entire scene.
    # BLOCKING: Phase 1 -- Aeron enters his own quarters to find Nyra already
    #           seated at his desk chair. She has the chair turned to face the
    #           door. She is waiting. Phase 2 -- Aeron processes. Phase 3 --
    #           the door chimes again. Zira is in the corridor. She enters.
    #           Sees Nyra. The triangle forms. Phase 4 -- negotiation. None of
    #           them sit. Nyra stands from the chair. All three standing.
    #           Phase 5 -- poly gate check. Phase 6 -- consent gate (3 options).
    #           Phase 7 -- intimate marker. Phase 8 -- aftercare.
    # CANON: POLY BEAT. Nyra + Zira + Aeron. The first time two of Aeron's
    #        OB-path women are in the same room with him for reasons that are
    #        not operational. NOT planned. NOT staged. Nyra came because the
    #        oath's rhythm requires periodic confirmation (her word: "maintenance").
    #        Zira came because the workshop was too small tonight and her body
    #        walked her here before her mind signed off on the destination.
    #        The accidental convergence is the scene. The negotiation is what
    #        they do with the accident. The negotiation is cold, institutional,
    #        and load-bearing. Neither woman is competing for him. Both women
    #        are competing for the terms on which the room operates.
    #        Callbacks: a4_s11 (Nyra's second oath -- "temperature not name"),
    #        a4_s12 (Zira's corridor confrontation -- "make me feel it"),
    #        a4_s13 (Zira's pressed flower -- "something from before"),
    #        a4_s14 (Lyra sanctifying violence -- same night).
    # CONSENT: 3-choice framework, OB-mode. All three cold. Ceremonial /
    #          Possessive / Transactional. Poly gate check: metric("poly_pressure")
    #          >= 3 required for escalation. Below threshold -> cold emotional
    #          resolution without intimacy.
    # FACE: Nyra -- the liturgical composure from a4_s11, but with a new layer:
    #        awareness of another woman in the room. The composure holds. The
    #        awareness is in the peripheral attention, not the face.
    #        Zira -- the workshop jaw-set from a4_s13, but sharper. She is in
    #        someone else's territory (Aeron's quarters, not her workshop) and
    #        she did not expect to share it. The sharpness is territorial
    #        instinct translated into stillness.
    #        Aeron -- the institutional face. Beneath it: the mathematics of
    #        two women who have different claims on the same body and neither
    #        claim has a vocabulary that includes the other.

    # ========= VOICE BASELINE =========
    # OB Aeron: Minimal. Shorter than either woman tonight. He is the fulcrum
    #           of the triangle and the fulcrum does not speak much. The
    #           athoughts are where the weight lives. The Marcus idiom is present
    #           but neither woman lets him deploy it uncorrected.
    # Nyra: Liturgical. Cold. She speaks in declarations. She does not negotiate
    #       in the common sense -- she states terms. The terms are the negotiation.
    #       The nythoughts reveal the cost of sharing the rite's space with a
    #       woman who holds a flower instead of an oath.
    # Zira: Direct. Angular. She speaks in short, precise sentences that land
    #       harder than Nyra's because Nyra's have ritual padding and Zira's
    #       do not. The zthoughts carry the scene's emotional weight. She is the
    #       one counting what things cost tonight.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - 2338]
    # Night cycle. Overhead at 20%. Desk lamp amber. Window blue.
    # The room is arranged for one person who was not expecting visitors.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_night_cycle.ogg" fadein 2.0

    # ========== PHASE 1 -- THE ROOM IS NOT EMPTY ==========

    athought "I have been in the corridor for ninety seconds."

    athought "I am standing outside my own quarters. The door indicator reads OCCUPIED. That is my own indicator. I am the one who is supposed to be inside."

    athought "Someone is in my room."

    athought "I know who it is before I open the door because at 2315 I received a note from Nyra that said 'I am conducting maintenance tonight' and I did not process it until now and now I am standing in a corridor outside a door that has someone in it who considers my room an extension of the rite."

    athought "Maintenance. Her word for the periodic reconfirmation of what the second oath sealed."

    athought "I open the door."

    #play sound "sfx/door_unseal_quarters.ogg"

    "The door unseals. He steps through."

    "Nyra is seated in his desk chair. She has turned the chair to face the door. Her back is to the desk lamp. The amber outlines her from behind. Her face is in the blue from the window. She is not in uniform. She is wearing the off-duty fatigues she wears in her own quarters -- pressed, clean, the collar straight. She has brought nothing with her. Her hands are folded in her lap."

    "She looks at him. She does not speak."

    athought "She has been in this room long enough to rearrange the chair. The chair was facing the desk when I left. She turned it. The turning was part of the preparation. She prepared my room the way she prepared hers at a4_s11 -- by converting it into a space the rite can use."

    athought "I notice I am not surprised."

    athought "I notice that the not-surprised is the diagnostic."

    ny "Commander."

    a "Nyra."

    ny "I told you I was conducting maintenance."

    a "I read the note."

    ny "You did not respond."

    a "No."

    ny "The non-response was also received. You do not respond to the rite. The rite does not require your RSVP. It requires your presence."

    athought "She is right. The non-response was not rudeness. The non-response was the correct protocol for a summons that does not ask."

    "He closes the door behind him. It reseals. He stands three paces inside the room. She is four paces from him. The desk lamp between them throws her shadow long across the deck."

    nythought "He came with the face. The institutional face. I have seen it at the ops table and in the corridor and in his quarters at a4_s11. The face is the same face. What has changed is that I no longer read the face as an obstacle. I read it as a surface I have written on. The writing is the rite's signature. The signature is not visible to anyone who does not know what was sealed."

    nythought "I know what was sealed."

    nythought "Tonight I am confirming the seal holds."

    # ========== PHASE 2 -- THE SECOND ARRIVAL ==========

    "Nyra opens her mouth to speak. The sentence she is about to deliver is part of the maintenance protocol she has constructed for the oath's periodic reconfirmation."

    "The door chimes."

    "Both of them turn toward the sound."

    athought "The door indicator. Someone in the corridor. The door chime is the proximity register -- not a knock. Someone is standing at the threshold close enough to trigger the chime."

    athought "I know who it is before the chime finishes its half-second pulse."

    athought "I know because at 2330 I saw Zira leave the workshop bay corridor walking in a direction that was not toward her cot and was not toward the mess and was toward this sector."

    athought "I did not process it. I am processing it now."

    ny "Are you expecting someone."

    a "No."

    nythought "He is not lying. I can hear the un-lying in the word. He is genuinely not expecting the chime. He is also not surprised by it. The not-surprised-but-not-expecting is a register I have learned to read in him. It means his body has predicted something his command layer has not confirmed."

    nythought "I know whose body is in the corridor."

    nythought "I know because the base manifest shows three women with Sector C corridor access after 2200 and one of them is me and one of them is the doctor who is asleep and one of them is the signal officer who does not sleep."

    "Aeron walks to the door. He opens it."

    #play sound "sfx/door_unseal_quarters.ogg"

    "Zira is in the threshold."

    "Her jacket is on. Her hands are in her pockets. Her left hand is closed around something inside the left pocket. Her face is the workshop jaw-set, sharpened by the corridor's cold light."

    "She looks at Aeron. She looks past Aeron. She sees Nyra."

    "Her jaw tightens one increment."

    zthought "She is here."

    zthought "The oath officer is in his quarters at 2340 sitting in his chair with the amber behind her like a painting of a saint who has not been canonized yet."

    zthought "I did not expect her. I did not plan for her. I walked here from the workshop because the workshop was the wrong size tonight and I needed a different room and the only different room my boots knew how to find was this one."

    zthought "My boots found a room that is already occupied by a woman who holds an oath I will never hold."

    zthought "I am going to step inside anyway."

    zthought "If she objects, the objection will be the data point I needed to collect."

    "Zira steps through the threshold. The door reseals behind her."

    #play sound "sfx/door_reseal_soft.ogg"

    "The triangle forms. Aeron at the center of the room, equidistant from both women. Nyra at the desk. Zira at the door. The geometry is accidental and load-bearing."

    # ========== PHASE 3 -- THE RECOGNITION ==========

    "Nyra stands from the chair. The standing is slow, deliberate. She does not cede the chair. She vacates it because the negotiation requires everyone standing. The asymmetry of a seated woman and a standing woman is a power grammar Nyra will not permit tonight."

    ny "Signal Officer."

    z "Doctrine Officer."

    "The titles are weapons. They are also shields. The titles establish that neither woman is here as a woman. Both are here as holders of institutional roles that happen to have led them to the same room on the same night."

    athought "They are using titles. Not names. The titles are the formal distance they are constructing between each other in real time."

    athought "I am the room they are constructing the distance inside."

    "A silence. Six seconds. The HVAC cycles. The desk lamp flickers once and holds."

    ny "I did not schedule a joint appointment."

    z "Neither did I."

    ny "Then this is an accident."

    z "It is an accident."

    ny "Accidents in this room require negotiation."

    z "I agree."

    nythought "She agrees. That is the first correct thing. She could have left. She did not leave. She agreed to negotiate. The agreeing is the first data point and I am cataloging it the way I catalog every deviation from the rite's expected pattern."

    nythought "The rite did not expect her tonight."

    nythought "The rite will have to accommodate her or dismiss her."

    nythought "I am not ready to dismiss her."

    nythought "I am not ready because dismissing her would require acknowledging that she is a threat to the rite, and she is not a threat to the rite. She is a parallel force. The rite has no clause for parallel forces. Tonight I will have to write one."

    # ========== PHASE 4 -- THE NEGOTIATION ==========

    "Nyra steps to the center of the room. Aeron moves aside. The movement is instinctive -- he is making space for the negotiation that is not his to conduct."

    "Nyra faces Zira across four feet of deck."

    ny "You are here because he owes you."

    ny "I am here because I own the oath."

    "The two sentences land in the room like survey stakes. She is marking the territory."

    z "You own nothing."

    "Zira's voice is flat. The workshop register. No anger in it -- the anger has been compressed past the audible range."

    z "You hold a position and I hold a memory. Tonight neither of those things is enough on its own."

    nythought "She is correct. I do not like that she is correct. The not-liking does not change the correctness."

    ny "What are you proposing."

    z "I am not proposing. I am naming what is already true."

    z "We are both in this room. He did not summon either of us. We both walked here on our own volition for our own reasons. Your reason has a ceremony. My reason has a pressed flower. Neither ceremony nor flower brought us to the same room at the same time. The room did."

    ny "The room is his."

    z "The room is where he sleeps. It is not his in the way your quarters are yours or my workshop is mine. It is a room a man collapses into at the end of a shift. We are both here because the room has no ritual of its own, which means we can build one."

    athought "She said 'we.' She is including Nyra in the we. The inclusion is strategic and it is also honest. Zira does not include people she does not recognize as structurally necessary."

    athought "I am standing beside my own cot listening to two women negotiate the terms of a room I sleep in."

    athought "The negotiation does not include me yet. That is the point. They will include me when they are finished with each other."

    nythought "She said 'build one.' A ritual. She is offering to co-construct a ritual with me in the territory of a man who does not own the territory in the way either of us owns our own."

    nythought "The offer is institutional. The offer is also the most honest thing a non-oath-holder has said to me since the second sealing."

    nythought "I am going to accept the offer. I am going to accept it on my terms."

    ny "I do not share command."

    "The sentence is granite."

    z "I know."

    ny "I do not share the rite."

    z "I am not asking for the rite."

    ny "What are you asking for."

    z "The same room. The same night. Different reasons. No pretense that the reasons are the same."

    "Nyra considers this. Her jaw does not move. Her eyes do not narrow. What happens in her face is the thing that happened at a4_s11 when she was deciding whether to open the lacquered box: a very small settling of the features, as if the face has decided something the mouth has not yet been informed of."

    ny "I do not share command."

    ny "But tonight I am not commanding."

    zthought "She said it."

    zthought "Tonight I am not commanding. Six words. The six words are a door I did not build and do not own and have just been invited to walk through."

    zthought "The invitation is not warm. The invitation is the coldest thing anyone has said to me since the corridor demand at 0714. The coldness is what makes it trustable. Warm invitations from doctrine officers are performances. Cold invitations are structural."

    zthought "I am going to walk through the door."

    # ========== PHASE 5 -- POLY PRESSURE CHECK ==========

    $ nudge_poly("ob", "nyra_zira_convergence", 1)

    if metric("poly_pressure") >= 3:

        # --- ABOVE THRESHOLD: THE GATE OPENS ---

        "The room settles into a new configuration. The three of them are standing in a triangle that has stopped being accidental and has become architectural."

        "Nyra turns to Aeron."

        ny "You have been silent."

        a "This was not my negotiation."

        ny "It was about you."

        a "It was about the room. I am in the room. That is not the same as being about me."

        z "He is right."

        nythought "He is right and she confirmed it before I could. That is the second data point. She is not here for him in the way I am here for the oath. She is here for the room. The room is the thing they share and I am the one who has been treating the room as an extension of the rite. She is treating the room as a room."

        nythought "The room-as-room is a frame I had not considered."

        nythought "The rite has to accommodate the frame or the rite is too narrow."

        nythought "The rite is too narrow. Tonight I widen it."

        ny "Then the room speaks. I am going to offer three terms. You each accept or you each leave. The terms are not negotiable after they are spoken."

        z "Speak them."

        # ========== CONSENT GATE ==========

        ny "The first term. Ceremony. The room becomes a rite. I lead it. You are both participants. The rite has rules. The rules are mine. Inside the rules, what happens between the three of us is governed by the oath's grammar. No improvisation. No deviation. The rite proceeds and the rite concludes and the rite is not discussed afterward."

        ny "The second term. Possession. The room becomes a territory. No one leads. Each of us holds what we brought. The oath stays mine. The flower stays hers."

        "Zira's left hand tightens in her pocket. She does not speak."

        ny "What happens is between three bodies that have each chosen to stay for their own reasons. No grammar. No ritual. Only the fact of the room and the fact of the choosing."

        ny "The third term. Transaction. The room becomes an exchange. Each of us states what we came for. Each of us states what we are willing to give. The statements are explicit. The exchange proceeds on the explicit terms. No ambiguity. No ceremony. No warmth."

        ny "Choose."

        "She looks at Aeron. She looks at Zira. She waits."

        z "You said the terms are not negotiable. You did not say who chooses."

        ny "He does."

        "Zira looks at Aeron. The look is the corridor-demand look from a4_s12 -- clear-eyed, angular, waiting."

        ny "He has always been the one who chooses which door to walk through. I offer the doors. You hold the memory. He walks."

        athought "She is right. The architecture of every intimate hour I have spent on this path has been: a woman offers the frame, a woman holds the feeling, and I choose which frame the feeling enters."

        athought "Tonight there are two women. Two frames. One choice."

        athought "The choice will tell me which of the three costs I am willing to pay tonight."

        menu:
            "The room holds. Amber from the desk. Blue from the window. Three bodies in a triangle. The HVAC breathes."

            "Ceremony. Nyra leads.":
                $ choice_and_dev(
                    _current_scene_id, "_ceremony", "OB", factor=1,
                    next_scene_label=None,
                    note="OB ceremonial. Nyra's grammar governs. Zira submits to the rite's rules. Cold, structured, liturgical."
                )
                jump .ceremony

            "Possession. No one leads.":
                $ choice_and_dev(
                    _current_scene_id, "_possession", "OB", factor=0,
                    next_scene_label=None,
                    note="OB possessive. Each holds what they brought. No grammar. Bodies and choosing."
                )
                jump .possession

            "Transaction. We state terms.":
                $ choice_and_dev(
                    _current_scene_id, "_transaction", "OB", factor=-1,
                    next_scene_label=None,
                    note="OB transactional. Explicit exchange. No ambiguity. The coldest of the three."
                )
                jump .transaction

        # ========== BRANCH: CEREMONY ==========
        label .ceremony:

            a "Ceremony. Nyra leads."

            "Nyra's chin lifts half a degree. The satisfaction is not in her mouth. It is in the angle of her neck."

            nythought "He chose the rite. In front of her. She heard him choose the rite. She is still in the room. She did not leave when he chose the thing that is mine."

            nythought "That is the third data point. She is willing to enter the grammar I built. She is not conceding. She is translating."

            "Zira exhales. Not a sigh. A recalibration."

            z "I am entering your grammar. I am not converting to your religion."

            ny "I did not ask you to convert. I asked you to participate."

            z "Noted."

            ny "The rite begins now."

            $ canon_set("ob.poly.oath_and_flower_mode_ceremony", True)

            jump .intimate_sequence

        # ========== BRANCH: POSSESSION ==========
        label .possession:

            a "Possession. No one leads."

            "Nyra's jaw tightens. Not displeasure. Adjustment. She is recalculating the room without her leadership as the structural center."

            ny "Then I hold the oath and she holds the flower and you hold the room."

            z "That is the first thing you have said tonight that sounded like a person instead of a doctrine."

            ny "It will be the last."

            zthought "She gave me one sentence of person and took it back in the next breath. That is not cruelty. That is maintenance. She maintains herself the way she maintains the rite."

            zthought "I can work inside that. I have worked inside harder architectures."

            $ canon_set("ob.poly.oath_and_flower_mode_possession", True)

            jump .intimate_sequence

        # ========== BRANCH: TRANSACTION ==========
        label .transaction:

            a "Transaction. We state terms."

            ny "Then state."

            a "I came to this room because it is where I sleep. I did not summon either of you. I am willing to stay because both of you chose to be here and I am not willing to be the man who sends two women away on the same night for different reasons."

            z "I came because the workshop was the wrong size tonight and my body brought me here. I am willing to stay because she is in the room and I want to know what it feels like to be in the same room with the oath and not be the one holding it."

            ny "I came because the rite requires periodic maintenance and tonight was scheduled for maintenance. I am willing to stay because she named a thing I had not considered: the room-as-room. The room is not the rite's territory. The room is the room. I am adapting."

            athought "Three statements. Three different architectures of staying. None of them are about desire. All of them are about structural necessity."

            athought "This is OB intimacy. The structural necessity IS the desire. The desire has been so thoroughly processed through institutional language that it no longer registers as desire. It registers as logistics."

            $ canon_set("ob.poly.oath_and_flower_mode_transaction", True)

            jump .intimate_sequence

        # ========== INTIMATE SEQUENCE ==========
        label .intimate_sequence:

            # VISUAL: The room does not transform. The desk lamp stays amber.
            # The window stays blue. The cot is a cot. The quarters do not
            # become a temple or a workshop. They become a room in which three
            # people who chose to stay are doing the thing that staying means
            # when the staying has been negotiated in the cold register.
            # CAMERA: Medium wide, static. The composition is triangular. The
            # camera does not privilege any body over the others. The triangle
            # shifts and holds and shifts again. The amber and blue mix on
            # skin without warming. No close-ups. The wide shot is the respect.
            # AUDIO: Ambient hum. Three sets of breathing. No music.

            "The room holds the three of them. Aeron's cot. Nyra's stillness. Zira's closed fist in her pocket."

            "Whatever mode they are in -- ceremony, possession, transaction -- the mode is held by all three in different grips. Nyra holds it like a chalice. Zira holds it like a tool. Aeron holds it like a surface he is pressing his hand against to stop a tremor."

            "Zira's left hand comes out of her pocket. The fist stays closed. She does not open it. She does not show what is inside. Her fist rests at her side, closed, throughout."

            nythought "She is holding something. I have not asked what it is. I am not going to ask. The not-asking is the clause I wrote into the rite tonight for parallel forces. The parallel force has its own sacrament. The parallel sacrament is not mine to examine."

            zthought "My hand is closed around the flower. The flower has been in my fist since I left the workshop. I brought it because the flower is the thing I have from before him and from before the oath and from before the corridor demand. The flower is mine."

            zthought "Nyra has not looked at my fist. She has not asked. The not-asking is the thing that makes tonight possible."

            $ rel_bump("Nyra", trust=1, attraction=1)
            $ rel_bump("Zira", trust=1, attraction=1)
            $ nudge_poly("ob", "oath_and_flower_intimate", 2)

            # [INTIMATE CONTENT HERE]

        # ========== AFTERCARE (COLD) ==========

            # VISUAL: After. The room is the same room. The desk lamp is still
            # amber. The window is still blue. The cot has been used. The three
            # of them are arranged in a new triangle: Nyra at the desk, re-dressed,
            # standing with one hand on the chair back. Zira on the deck beside the
            # cot, her back against the cot frame, her legs stretched out. Aeron
            # on the cot, sitting, his shirt re-fastened to the third clasp.
            # The distance between them is the aftercare. The silence is the
            # aftercare. What they do NOT say is the aftercare.
            # CAMERA: Wide. Still. The widest shot of the scene. The three bodies
            # in the room, each in their own gravity.

            "The room settles."

            "Nyra is at the desk. She has re-dressed. Her fatigues are pressed again -- she smoothed the collar with two fingers and the collar obeyed. Her hand rests on the back of the desk chair. She is not sitting in it. She is holding it the way you hold a lectern after a sermon."

            "Zira is on the deck beside the cot. Her back is against the cot frame. Her legs stretch out across the deck. Her uniform is pulled back together with the field-splice precision from a4_s13. Her left hand is in her lap. Closed. The fist has not opened since she arrived."

            "Aeron is on the cot. Sitting. His shirt re-fastened to the third clasp. The number is becoming a pattern he does not recognize in himself."

            "The silence is forty seconds long. The HVAC cycles. The desk lamp flickers once and holds."

            athought "Two women in my quarters. Neither of them is looking at me. Neither of them is looking at each other. All three of us are looking at our own piece of the silence."

            athought "The silence has three textures. Nyra's silence is the silence of a rite concluded. Zira's silence is the silence of a woman holding something that predates me. My silence is the silence of a man who has just been the room in which two different architectures of staying agreed to coexist for one hour."

            "Nyra speaks first."

            ny "The maintenance is complete."

            "The sentence is institutional. The sentence is also the only sentence she has for what just happened. The rite's vocabulary is the only vocabulary she brought tonight, and the rite's vocabulary ends at 'maintenance complete.'"

            "Zira does not respond to the sentence. She looks at her closed fist in her lap. She opens the fist one centimeter. She looks at what is inside. She closes the fist."

            zthought "The flower is still here. It did not leave. It did not fall out during the hour. It stayed in my palm the way it has stayed in my palm through every version of this."

            zthought "Nyra did not touch it. She did not ask to see it. She did not look at it."

            zthought "The not-looking is the only grace I am going to credit her with tonight. The grace is enough."

            "Nyra turns toward the door. She does not look at Zira's fist. She does not look at Aeron."

            ny "I will be at the ops table at 0700."

            "She walks to the door. The door unseals. She steps through."

            #play sound "sfx/door_unseal_quarters.ogg"

            "The door reseals. The room is two people now."

            "Zira does not move. Aeron does not move."

            "Twenty seconds."

            z "She did not ask about the flower."

            a "No."

            z "You did not ask either. At the workshop you did not ask. Tonight you did not ask."

            a "No."

            z "The not-asking is the only thing either of you has given me that I can keep."

            athought "She said 'keep.' Not 'use.' Not 'hold.' Keep. The word is the word of a woman who has been calculating what is survivable and what is not, and the not-asking has been sorted into survivable."

            "Zira opens her fist in her lap. The pressed flower. Browner at the edges than at a4_s13. The center still holding color in the way pressed things do, for a while."

            "She does not show it to him. She looks at it herself. She closes her fist."

            z "Go to sleep, Commander."

            "She stands. The motion is the workshop motion -- clean, no wasted effort. She walks to the door. She does not look back."

            z "If she comes back before I come back, tell her the flower is still mine."

            "The door unseals. She steps through. The door reseals."

            "Aeron is alone in his quarters."

            athought "Two women. Two exits. Two different silences left behind."

            athought "Nyra left the silence of a rite concluded. Zira left the silence of a reservation confirmed."

            athought "I am sitting on my cot with my shirt at the third clasp and both silences in the room and neither silence requires me to fill it."

            athought "I am not going to fill either of them."

            athought "I am going to turn off the desk lamp and lie down and let the blue from the window be the only light and I am going to not think about what it means that two women walked to the same room on the same night for different reasons and neither of them left angry."

            athought "I am going to fail at not thinking about it."

            athought "I am going to fail at not thinking about it for exactly the amount of time it takes me to fall asleep."

            "He turns off the desk lamp. The amber goes. The blue from the window holds. He lies back on the cot. The quarters are his again and they are also not his in a way that will not resolve tonight."

            #stop ambient fadeout 2.0
            #scene black with fade

            jump .state_updates

    else:
        # --- BELOW THRESHOLD: COLD EMOTIONAL RESOLUTION ---

        "The room holds the three of them in the triangle. The negotiation has happened. The terms have been spoken. The terms are real."

        "But the room does not move past the terms."

        "Nyra looks at Aeron. She looks at Zira. She reads the room the way she reads an operational situation -- by the weight of what is present and the weight of what is absent."

        ny "The pressure is not sufficient."

        "She means it structurally, not emotionally. The room does not have the accumulated weight required for three people to cross the threshold together. The weight exists in pieces. The pieces have not yet been compounded into one mass."

        ny "Tonight is the negotiation. Tonight is not the conclusion."

        z "I agree."

        zthought "She is right. I can feel it in the room. The flower is in my fist and the oath is in her posture and neither of those things has enough mass tonight to pull the room past the speaking and into the body."

        zthought "That is not failure. That is timing."

        a "Then what is tonight."

        ny "Tonight is the night we were in the same room. The record of the room is sufficient."

        z "The record is sufficient."

        "Nyra turns to the door. She walks to it. She stops."

        ny "Signal Officer."

        z "Doctrine Officer."

        ny "You are holding something in your left hand."

        "Zira's fist tightens."

        ny "I am not asking what it is. I am acknowledging that it exists."

        z "Acknowledged."

        "Nyra opens the door and leaves. The door reseals."

        "Zira looks at Aeron."

        z "She noticed the fist."

        a "Everyone notices the fist."

        z "You have never asked about it."

        a "No."

        z "Keep not asking."

        "She walks to the door. She stops."

        z "If the pressure is sufficient next time, I will be here."

        "She leaves."

        "Aeron stands alone in his quarters."

        athought "Two women. Two exits. The same room. The pressure was not sufficient and I am relieved and I am also not relieved and the not-relieved is the thing that tells me the pressure will be sufficient eventually."

        athought "Eventually is a word I do not use in the command register. Eventually is a word for the corridor at 2355 when the base is running skeleton and two women have just walked out of my quarters having negotiated something I do not have a name for."

        $ nudge_poly("ob", "oath_and_flower_deferred", 1)
        $ canon_set("ob.poly.oath_and_flower_deferred", True)
        $ tp_seed("a4.ob.poly.pressure_not_sufficient_yet")

        #stop ambient fadeout 2.0
        #scene black with fade

        jump .state_updates

    # ========== STATE UPDATES ==========
    label .state_updates:

        $ flag("ob_poly_nyra_zira_oath_and_flower", True)
        $ canon_set("ob.poly.nyra_zira_first_shared_room", True)
        $ canon_set("ob.poly.flower_stayed_in_fist", True)
        $ canon_set("ob.poly.nyra_did_not_ask_about_flower", True)
        $ npc_remember("Nyra", "shared_room_with_zira_oath_intact", tone="cold_accommodation")
        $ npc_remember("Zira", "shared_room_with_nyra_flower_in_fist", tone="parallel_force")
        $ npc_remember("Aeron", "two_women_two_exits_two_silences", tone="fulcrum")
        $ scene_mark(_current_scene_id, "exited")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s14a_oath_and_flower_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same night as a4_s14 (Lyra sanctifying violence). 2338 -- approximately
#     0030. Nyra arrived at Aeron's quarters at ~2315 for oath maintenance.
#     Zira walked from the workshop at ~2335 without conscious destination.
#     The convergence is accidental.
#   - Three days after a4_s11 (Nyra's second oath). Two days after a4_s13
#     (Zira's deepening erotic). One day after a4_s14 (Lyra sanctifying
#     violence on OB).
# cann.what_happened:
#   - Aeron returns to his quarters to find Nyra already inside, conducting
#     oath "maintenance" -- her word for periodic reconfirmation of the
#     second sealing. Nyra has turned the desk chair to face the door.
#   - Before the maintenance begins, the door chimes. Zira is in the
#     corridor. She enters. Sees Nyra. The triangle forms.
#   - NEGOTIATION: Nyra: "You are here because he owes you. I am here
#     because I own the oath." Zira: "You own nothing. You hold a position
#     and I hold a memory. Tonight neither of those things is enough on
#     its own." The negotiation is cold, institutional, not competitive.
#     They are not fighting over him. They are negotiating the terms of
#     the room.
#   - Key exchange: Nyra: "I do not share command. But tonight I am not
#     commanding." This opens the consent gate.
#   - POLY GATE: metric("poly_pressure") >= 3 required.
#     ABOVE: 3-choice consent gate. Aeron chooses.
#       1. "Ceremony. Nyra leads." -- Rite's grammar governs. Zira enters
#          the grammar without converting. ("I am entering your grammar.
#          I am not converting to your religion.")
#       2. "Possession. No one leads." -- Each holds what they brought.
#          Oath, flower, room. No grammar.
#       3. "Transaction. We state terms." -- Explicit exchange. Three
#          architectures of staying. The coldest.
#     All three lead to # [INTIMATE CONTENT HERE].
#     BELOW: Cold emotional resolution. Nyra: "The pressure is not
#       sufficient. Tonight is the negotiation. Tonight is not the
#       conclusion." Both women leave separately. The negotiation is
#       the record. nudge_poly() for future pressure accrual.
#   - THE FLOWER: Zira keeps the pressed flower in her closed palm the
#     entire scene. Nyra does not touch it. Does not ask. The not-asking
#     is the scene's emotional center. The flower stays hers.
#   - Aftercare: Three separate silences. Nyra leaves first ("The
#     maintenance is complete."). Zira leaves second ("If she comes back
#     before I come back, tell her the flower is still mine."). Aeron
#     alone with two silences in the room.
# cann.aeron_state:
#   - Fulcrum. Minimal speech. The two women negotiate the room; he is
#     the room. Chooses the mode at the consent gate. Does not attempt
#     to reconcile the two architectures. The not-reconciling is the
#     only correct move.
#   - Third-clasp pattern continues from a4_s11 / a4_s13 -- a body
#     organizing itself along rhythms the mind has not confirmed.
# cann.path_tracking_flags:
#   - Ceremony: canon_set("ob.poly.oath_and_flower_mode_ceremony").
#   - Possession: canon_set("ob.poly.oath_and_flower_mode_possession").
#   - Transaction: canon_set("ob.poly.oath_and_flower_mode_transaction").
#   - All escalation paths: flag("ob_poly_nyra_zira_oath_and_flower"),
#     rel_bump("Nyra", trust=1, attraction=1),
#     rel_bump("Zira", trust=1, attraction=1),
#     nudge_poly("ob", "oath_and_flower_intimate", 2),
#     canon_set("ob.poly.nyra_zira_first_shared_room"),
#     canon_set("ob.poly.flower_stayed_in_fist"),
#     canon_set("ob.poly.nyra_did_not_ask_about_flower").
#   - Below threshold: canon_set("ob.poly.oath_and_flower_deferred"),
#     nudge_poly("ob", "oath_and_flower_deferred", 1),
#     tp_seed("a4.ob.poly.pressure_not_sufficient_yet").
# cann.thematic_flags:
#   - OATH VS FLOWER. The scene's structural thesis. Nyra holds an oath
#     (ceremony, doctrine, institutional claim). Zira holds a flower
#     (memory, the personal, the thing from before). Neither is sufficient
#     on its own. The coexistence is the scene.
#   - PARALLEL FORCES. Nyra recognizes Zira not as a rival but as a
#     parallel force. The rite has no clause for parallel forces. Tonight
#     she writes one. The clause is: the parallel force has its own
#     sacrament, and the parallel sacrament is not hers to examine.
#   - THE NOT-ASKING. Nyra does not ask about the flower. Aeron does not
#     ask about the flower. The not-asking is what Zira keeps. The
#     not-asking is the only currency that works across both architectures.
#   - ACCIDENTAL CONVERGENCE. Neither woman planned this. The accident is
#     the scene's engine. What they do with the accident -- negotiate it
#     into cold institutional terms -- is the OB path's definition of
#     poly intimacy: power negotiation, not warmth.
#   - ROOM-AS-ROOM. Zira's contribution to the negotiation: the room is
#     not the rite's territory, it is the room. The room-as-room is the
#     neutral ground on which the rite and the flower can coexist.
# cann.character_moments:
#   - Nyra: "I do not share command. But tonight I am not commanding."
#   - Nyra: "I did not schedule a joint appointment."
#   - Zira: "You own nothing. You hold a position and I hold a memory."
#   - Zira: "If she comes back before I come back, tell her the flower
#     is still mine."
#   - Aeron (thought): "I am the room they are constructing the distance
#     inside."
#   - Zira (thought): "The not-asking is the only thing either of you
#     has given me that I can keep."
# cann.block_status:
#   - VARIANT. Poly beat with poly_pressure gate. Escalation: 3 consent
#     paths. Below threshold: cold resolution with pressure accrual.
#     First Nyra + Zira shared-room scene on OB.
# cann.requires_followup:
#   - The "clause for parallel forces" Nyra writes tonight: track in
#     Phase II. The clause will be tested when the parallel force
#     demands more than coexistence.
#   - Zira's "if the pressure is sufficient next time": the below-threshold
#     branch plants the return. The pressure will be sufficient.
#   - The flower-in-fist as a through-line: the flower has now survived
#     a4_s05, a4_s13 aftercare, and a4_s14a. Each appearance it is
#     browner. Track the decay as metaphor.
#   - Aeron's "two exits, two silences" pattern: the fulcrum role will
#     strain in Phase II when the silences start contradicting each other.
