# =======================================================
# ACT 4 - Scene 14a: Familiar Ground (Empathy Path)
# File: a4_s14a_familiar_ground_emp.rpy
# Type: POLY BEAT — LYRA + ZIRA + AERON
# Placement: after s14 (return to the table). Late night.
# Lyra and Zira do not usually overlap alone without the
# group. Both know different versions of Aeron. Here they
# meet the third version — the one in between. Lyra brings
# tea (callback to Act 3). Zira brings the updated relay
# map. They are working on the civilian move logistics
# together when Aeron walks in to find them already
# collaborating. The emotional core: the two women are not
# competing. They are recognizing that their care for the
# same man has different shapes and both shapes are needed.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s14a_familiar_ground_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s14a_familiar_ground_emp:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s14a_familiar_ground_emp")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Five movements.
    #         (1) The mapping station from outside. 50mm, locked. The door
    #             is open by about six inches. Light from inside — warm,
    #             practical, two lamps. Two voices inside the room that
    #             Aeron hears before he rounds the corner. The camera is
    #             in the corridor and it finds the voices before it finds
    #             the women.
    #         (2) Inside: 35mm, slow pan. Lyra is at the eastern end of
    #             the mapping table with two cups of tea — one in front of
    #             her, one in front of the chair where Zira is sitting.
    #             The tea is the same tea from Act 3. Zira is at the
    #             western end of the mapping table with the updated relay
    #             map unrolled across the surface, a stylus behind her
    #             ear, her hand flat on the northern corridor of the map.
    #             They are working. The camera lets the work be the
    #             subject for a full beat before it finds either face.
    #         (3) The doorway — Aeron. 35mm, locked from inside. He
    #             appears in the six-inch gap of the door the way he
    #             appeared in Zira's workshop doorway in s15. But this
    #             time two women look up instead of one. The two-look is
    #             the scene's thesis image. Two faces, one man in a
    #             doorway, and the man does not know what to do with the
    #             geometry of two faces looking at him with different
    #             versions of the same attention.
    #         (4) The table — three-shot. Wide, low. The mapping table
    #             is the central object. The relay map is the surface.
    #             Lyra at one end, Zira at the other, Aeron between them
    #             at the side of the table where the chair is not. He is
    #             standing because there are two chairs and they are both
    #             taken. The standing is the scene's structural joke and
    #             the structural joke is load-bearing.
    #         (5) The close — aftercare. Different camera vocabulary. The
    #             table from above, birdseye — three pairs of hands on
    #             the map. Lyra's at the northern edge, Zira's at the
    #             western corridors, Aeron's at the center where the
    #             civilian routes converge. The three sets of hands are
    #             the last image. Hold. Fade.
    # LIGHTING: Mapping station at late-night. Two practical lamps: a desk
    #           lamp at the eastern end (Lyra's end — she brought it from
    #           the small hall because the mapping station's overhead is
    #           too harsh for her at this hour) and the station's built-in
    #           task light at the western end (Zira's end — she prefers
    #           the task light because it is the same color temperature
    #           as the clip lamp in her workshop). The overhead is off.
    #           The corridor light comes through the six-inch gap of the
    #           door. When Aeron opens the door fully, the corridor light
    #           floods in for a beat and then he closes the door behind
    #           him and the room returns to the two practicals.
    # SFX: Late-night base ambient. The distant generator. The small
    #      sounds of two women working — a stylus on paper, the ceramic
    #      sound of a tea cup being set down on the mapping table's
    #      metal surface, Zira's particular habit of tapping her index
    #      finger once on a route before she traces it. Lyra's breath
    #      when she is reading a distance figure. The small silence
    #      between the sounds. No music bed until the poly gate. At the
    #      poly gate, if it opens: a single low held note — not the
    #      cello from the Zira scenes, not the prayer-note from the
    #      Lyra scenes, something between the two that has not existed
    #      in the score before. A third instrument for a third geometry.
    # FX/COMP: THE RELAY MAP. Unrolled across the full width of the
    #          mapping table. Zira's hand-drawn updates in her particular
    #          charcoal-on-vellum style from s08. Lyra's annotations in
    #          a different hand — the clean liturgical print she uses for
    #          census notes when she is tracking civilian movement for
    #          the vigil lists. The two handwritings on the same map is
    #          the prop that tells the audience these women have been
    #          working together before Aeron arrived.
    #          THE TEA. Two cups. The same blend from Lyra's Act 3 tea
    #          scenes. One cup in front of Lyra, one in front of Zira.
    #          Zira's cup is half-empty. The half-empty cup is how the
    #          audience knows they have been here for a while.
    # BLOCKING: Lyra seated at the eastern end. Zira seated at the
    #           western end. Aeron enters and stands at the side of the
    #           table. He does not take a seat because there is no seat.
    #           He leans on the table edge. Later — if the poly gate
    #           opens — the blocking shifts from the table to the space
    #           beside the table where there is a low bench against the
    #           wall. The bench is not for working. The bench is for
    #           people who have stopped working and have not left the
    #           room yet.
    # FACE: Lyra — the post-vigil composure from s19. The Band is on her
    #       wrist tonight (she put it back on the morning after s19, as
    #       a chosen sentence). The priest is present but not performing.
    #       She is a woman working with another woman on logistics, and
    #       the logistics are holy because the civilians are holy, and
    #       the holiness does not require a rite tonight.
    #       Zira — the Ashmarket efficiency from s08 and s15, directed
    #       at the map. She is in operational mode but her operational
    #       mode has been calibrated by s15 and the calibration shows
    #       in the way she holds the stylus — looser than before, the
    #       grip of a woman whose hands have done something besides
    #       operational work in the last forty-eight hours.
    #       Aeron — the face of a man who walked into a room expecting
    #       to find it empty and instead found two women he loves
    #       sitting at a table with tea and a map and his name nowhere
    #       in the sentence they were building without him.

    # ========= VOICE BASELINE =========
    # EMP cadence. Three-voice scene. Lyra speaks in the cleric-clean
    # register from s19, but tonight the register is warmer because the
    # room is warm and the woman across the table from her is Zira, and
    # Zira is a person Lyra has been respecting from a distance for
    # months and is now respecting from across a table with tea. Zira
    # speaks in the Ashmarket precision from s15, but the precision is
    # aimed at Lyra's annotations tonight rather than at Aeron's face,
    # and the aiming-at-Lyra is new territory. Aeron is sparse. He
    # speaks least. His thoughts carry the scene's interior.

    # scene bg_mapping_station_night_late_emp with dissolve
    # play ambient "sfx/ambient/base_night_late_mapping.ogg" fadein 2.5

    # ========== PHASE 1 — TWO VOICES ==========

    "Zero one fifteen. The base is in its deep-night register. Most of the corridors are empty. The shift rotation happened at twenty-three hundred and the overnight crew is at their stations and the people who are not on overnight are in whatever version of rest the base is offering tonight."

    "Aeron is not resting."

    "He has been at the ops table for the four hours since s14 finished. He took the side chair. He did not take the head. He worked the logistics of the civilian move — the move that is going to happen in forty-eight hours if Marcus does not accelerate the sweep — and he worked them until his eyes stopped resolving the distance figures on the datapads and then he stopped."

    "He is walking the secondary base at oh-one-fifteen because walking is the thing he does when the chair has done all it can for the night."

    "He turns the corner into the corridor that runs past the mapping station."

    "He hears two voices."

    athought "There are two people in the mapping station."

    athought "I was not expecting anyone in the mapping station at this hour. The mapping station is an ancillary room — used during day shifts for route planning, locked by the overnight duty officer after twenty-three hundred, except when someone with access leaves it open because the work is not finished and the room does not care about the hour."

    "He slows. The voices are coming through the door, which is open by about six inches. He can hear the content of the voices before he can see the speakers."

    "The first voice is Lyra's."

    l "The northern corridor clears into the service road at this junction. The census count from last week puts sixty-three civilians in the buildings along that stretch. Forty of them can walk. The other twenty-three will need transport or assist."

    "The second voice is Zira's."

    z "The service road is the relay I updated yesterday. There is a dead spot between the junction and the first cutover — forty meters without cover. I can get a team to bridge it but it costs two runners for the duration of the move."

    l "Two runners for forty meters."

    z "Two runners for forty meters for the duration. Which is — how long is the civilian column going to take to clear forty meters if twenty-three of them cannot walk at pace."

    l "At the estimates Noelle gave us, eleven minutes."

    z "Eleven minutes of two runners exposed. That is the cost. I am writing it on the map."

    "The small sound of a stylus on vellum."

    athought "They are working the civilian move."

    athought "They are working the civilian move together. Lyra and Zira. In the mapping station. At oh-one-fifteen. Without me."

    athought "I do not know when they started. I do not know who invited whom. I do not know whether this is the first time they have done this or the fourth. I am standing in the corridor outside the mapping station listening to two women I — listening to two women doing the work that needs doing without being asked to do it by me."

    athought "I am going to stand here for another ten seconds and listen to them be competent together before I open the door."

    "He listens."

    z "The western route has a different problem. The relay is intact but the building at the midpoint — Lyra, you have the census for that building?"

    l "Seventeen. All ambulatory. One child under five."

    z "The child under five changes the noise discipline."

    l "Yes."

    z "I am noting that on the map. The note says 'child — noise variance.' Noelle can factor it into the timing model."

    l "Good."

    "A beat. The small sound of a tea cup being set down on the metal surface of the mapping table."

    l "Your tea is getting cold."

    z "I know. I have been letting it get cold because I have been working."

    l "The tea does not improve cold."

    z "The tea does not improve at all. It is a kind thing you brought and I am going to drink it when I stop tracing this route."

    l "That is a specific kind of gratitude."

    z "It is the only kind I have at this hour."

    "A beat. Aeron can hear the precision in Zira's voice and the warmth in Lyra's and the two registers are not competing. The two registers are doing different work on the same problem."

    athought "They are not here because of me."

    athought "I need to understand that. They are not here because of me. They are here because the civilian move requires the relay map and the census to be in the same room, and Zira has the map and Lyra has the census, and neither of them needed me to tell them that the two things had to meet. They figured that out themselves. They are here because the work demanded the meeting and they answered the demand."

    athought "I am the man who is in love with both of them and I am standing outside the room where they are doing a thing that has nothing to do with being loved by the same man and everything to do with being two women who are good at two different kinds of work that the same civilians need."

    athought "I am going to open the door now."

    # ========== PHASE 2 — THE DOORWAY ==========

    "He pushes the door open."

    "The corridor light floods into the mapping station for a beat — a wash of cooler overhead that disrupts the warm practical-lamp arrangement inside."

    "Two faces look up."

    "Lyra looks up from the eastern end of the mapping table. Her right hand is on a census sheet. Her left hand is near the tea cup. The Band is on her left wrist, catching the task light. Her face is the post-vigil composure — calm, present, a priest who is doing logistics because logistics are how you keep the people you prayed for alive."

    "Zira looks up from the western end of the mapping table. Her right hand is on the relay map with a stylus between her fingers. Her left hand is flat on the table. The stylus has charcoal on its tip. Her face is the Ashmarket efficiency — sharp, warm underneath the sharp, a woman who has been doing this kind of work since she was eighteen and does not need overhead light to do it."

    "They both look at him."

    "The two-look is the thing Aeron is not prepared for."

    athought "They are both looking at me."

    athought "They are both looking at me and the looking is not surprise. They are not surprised I am here. They are looking at me the way two people look up from work when the third person walks in and the third person is the person the work is for."

    athought "The work is for the civilians. The work is not for me. But the two-look says: you are here, and we are here, and the room has a third chair problem that the room solved by not having a third chair."

    "He steps in. He closes the door behind him. The corridor light is cut off and the room returns to the two practicals."

    a "I did not know you were in here."

    z "We have been here since twenty-three thirty."

    l "I brought tea."

    a "I can see that."

    z "She brought me tea. She did not have to bring me tea. I was going to work the map by myself and she came in with two cups and said 'I have the census and I have tea' and I said 'sit down' and she sat down and we have been working for an hour and forty-five minutes."

    l "It was not an hour and forty-five minutes. It was an hour and forty."

    z "The five minutes are the tea."

    "Lyra's mouth does the small thing it does when she is not smiling but the not-smiling has a shape that is close to a smile. Aeron has seen that shape before — at the vigil, at the altar space, at the edge of moments that are quieter than the rites they follow."

    a "Is there a chair."

    z "There are two chairs and they are both taken."

    l "You can stand. Or you can sit on the bench against the wall."

    "The bench against the wall. Not a work surface. A bench that exists in the mapping station because someone put it there during the original setup and nobody moved it."

    "Aeron does not sit on the bench. He walks to the side of the mapping table — the long edge between Lyra and Zira — and he leans against the table edge. His hands go to the map. He looks at the work."

    athought "They have done more than I expected. The relay map has Zira's updated routes and Lyra's census annotations. The two handwritings are on the same surface. Zira's charcoal and Lyra's liturgical print. The combination is a document I have never seen before because these two women have never been in the same room doing the same work on the same surface before."

    "He reads the map for a full minute."

    a "The northern corridor route is good. The dead spot at the junction — Zira, you noted two runners for eleven minutes."

    z "Yes."

    a "I can find the runners. Noelle's timing model can absorb the cost."

    z "Good."

    a "The western route with the child under five. Lyra, the noise variance note — that is going to matter."

    l "I know. Noelle can model it. I spoke with Tessa about the child's family earlier today. The mother is capable. The child is not an infant. She can be carried quiet for forty meters if the mother is briefed."

    a "Good."

    "He is quiet for a beat. He is reading the map and he is also reading the room — the shape of two women who have been doing this work without him and have been doing it well and have not needed him to do it well and are now letting him look at the result."

    a "This is better than what I had at the ops table."

    z "We know."

    l "That is why we did it."

    "A beat."

    # ========== PHASE 3 — THE RECOGNITION ==========

    "They work."

    "For the next twenty minutes they work the civilian move in the three-body configuration the room has settled into — Zira on the routes, Lyra on the census, Aeron on the operational bridge between them. The work is not performative. The work is three people solving a problem that is going to save or lose sixty-three lives in forty-eight hours."

    "During the work, Aeron notices things."

    "He notices that Lyra defers to Zira on route security without being asked to defer. He notices that Zira defers to Lyra on civilian capacity without being asked to defer. He notices that neither of them defers to him unless the question is operational command, and the operational command questions are the minority of the questions on the table tonight."

    "He notices that Zira drinks the tea."

    "He notices that Lyra watches Zira drink the tea and does not comment on it and does not need to comment on it."

    "He notices that the two women have a working rhythm that did not exist ninety minutes ago and now exists and he had nothing to do with it."

    athought "They built this in an hour and forty minutes without me in the room."

    athought "They built a working collaboration out of a census and a relay map and two cups of tea and they built it because the work demanded it and they answered the demand. I am the man in the middle of this and the middle is not the center. The center is the map. The center is the sixty-three civilians. I am a third body in a room that already had a geometry."

    "The work reaches a natural pause. The major routes are marked. The census figures are annotated. The timing gaps are flagged for Noelle's model."

    "Zira sets the stylus down on the table. She leans back in her chair."

    "Lyra sets her census sheet down. She picks up her tea cup and holds it in both hands."

    "Aeron stays at the table edge."

    "The room is quiet."

    z "We should talk about the thing we are not talking about."

    "Lyra's cup pauses at her lips."

    "Aeron's hands on the table do not move."

    z "I am not talking about the map."

    l "I know what you are talking about."

    z "Good."

    "Zira looks at Lyra across the width of the mapping table. The look is direct. Not confrontational — direct in the way a woman who has spent her adult life reading rooms looks at another woman when the room has shifted and the shift needs naming."

    z "You and I have not been in the same room without the group before tonight."

    l "No."

    z "We have been in adjacent rooms. We have been in the same corridor at different times. We have been at the same briefing table with four other people between us. We have not been here."

    l "No. We have not."

    z "And the reason we have not been here is not logistics. The reason we have not been here is that neither of us knew what the room was going to be if we were in it together."

    "Lyra sets her tea cup down. She sets it down with the particular care she uses for objects that are standing in for other objects."

    l "You are right."

    z "I am usually right about rooms. I am less right about people. People are harder to read than rooms because rooms do not have feelings about being read."

    l "You are reading me now."

    z "I am."

    l "What do you see."

    z "I see a woman who has been praying for the same man I have been building doors for."

    "A beat. The mapping station is very quiet."

    l "I have been praying for him for fifteen years."

    "She says it without the liturgical register. She says it the way she said Seren at the altar — in the register of a woman who has stopped performing the prayer and is simply telling you the prayer exists."

    z "I have been building doors for him for three months."

    "She says it in the Ashmarket flat. No edge. The flat is the register she uses for true sentences she has not decorated."

    z "The time difference is the least interesting thing about us."

    "Lyra looks at Zira for a long count."

    lthought "She said the least interesting thing about us. She did not say the least important. She said the least interesting. Zira's diction is precise. She is telling me that the fact I have been carrying this for fifteen years and she has been carrying it for three months is not the comparison she is interested in. She is interested in a different comparison."

    lthought "She is interested in the shape. She is interested in the fact that my shape and her shape are both shapes and both shapes are real and both shapes are aimed at the same man and the man is in the room."

    l "The Six do not count the number. They count the honesty."

    "She says it to Zira, not to Aeron."

    "She is quoting something. The something is not an Academy text. The something is an older text — the text that the Academy was built on top of, the text that the Six carried before the Six were six, when the Six were just a woman and a woman and a man at a fire and the fire was the first thing they agreed to share."

    zthought "She is quoting scripture at me. She is quoting scripture at me in a mapping station at oh-one-forty and the scripture is not about God. The scripture is about honesty. The scripture is about the number not mattering if the honesty is real."

    zthought "I do not have scripture. I have the Ashmarket. The Ashmarket does not have a text about three people sharing something. The Ashmarket has a practical about three people dividing a profit, which is not the same thing, and is the closest thing I have."

    zthought "I am going to answer her scripture with my own language."

    z "I do not have a text for this."

    z "I have a bench in a workshop where I built a man an exit plan and then I built him a clock that runs backwards and then I sat on the floor with him and he said stay and I said stay and neither of us has said the next word yet."

    z "I do not know what the next word is."

    z "But I think you might."

    "She is looking at Lyra."

    "Lyra is looking at Zira."

    "Aeron is at the side of the table watching two women look at each other across a relay map that has both their handwriting on it, and the looking is a conversation he is not part of, and the not-being-part-of-it is the first time in Act IV that being outside a conversation has not cost him something. Being outside this conversation is giving him something."

    athought "They are talking to each other."

    athought "They are not talking to me. They are not routing through me. They are talking to each other about me and I am in the room and the talking-to-each-other is a thing I have never seen these two women do."

    athought "The thing they are doing is recognizing each other. Not as rivals. Not as positions on a grid. As two women who care about the same man in different shapes and are deciding, in real time, that the different shapes do not cancel each other out."

    "A beat."

    l "The next word is not mine to say alone."

    "She looks at Aeron."

    l "It is yours too."

    "Zira looks at Aeron."

    "He is being looked at by two women again. The two-look. The look he was not prepared for at the door and is not prepared for now and is going to have to answer without preparation."

    a "I am standing at a table with two women who have been doing the work I could not do tonight. I am standing here and I am looking at both of you and the looking is the same looking. I do not have two different kinds of looking for the two of you. I have one. The one has two directions."

    a "I do not know if that is an answer. But it is the true sentence."

    "A beat."

    $ nudge_poly("lyra_zira_recognized", delta=1)

    # ========== PHASE 4 — POLY GATE ==========

    if metric("poly_pressure") >= 3:

        "Zira is the one who says it."

        "She is the one who says it because Zira is the one who names the rooms. Lyra names the prayers. Aeron names the operations. Zira names the rooms."

        z "Is this what we are doing."

        "She says it at the table. Her hands are flat on the relay map. Her voice is at working volume — not raised, not lowered, the volume of a question that is being asked as a real question rather than a rhetorical one."

        z "All three of us. In the same room."

        "A beat."

        "Lyra answers first."

        l "The Six do not count the number. They count the honesty."

        "She said it before, to Zira. She says it again now, to the room. The repetition is not a repetition — it is a confirmation. The first time was a quotation. This time is an answer."

        z "That is a scripture answer. I am asking for a person answer."

        l "The person answer is: I thought I would be afraid of this room. I am not afraid of this room. I am in this room. You are in this room. He is in this room. The room has us. I do not need the scripture to tell me the room is allowed."

        "Zira looks at Aeron."

        z "And you."

        a "I said I have one looking with two directions."

        z "I know what you said. I am asking if you know what it means at oh-one-forty with both of us in the room."

        "A beat."

        a "It means I am going to be honest about the fact that I am looking at both of you and the looking is not divided. It is not half for one and half for the other. It is whole for both."

        a "I do not know how that works. I do not have a geometry for it. I am telling you it is what is true tonight."

        z "Good."

        z "Then we are in the room."

        "She stands."

        "She comes around the end of the mapping table — not toward Aeron, toward Lyra. She stops at Lyra's end of the table and she looks down at Lyra in the chair and Lyra looks up at Zira standing above her."

        z "I have been building doors for the same man you have been praying for. The doors and the prayers are not the same thing. But they are aimed at the same man. And the man is standing at the table behind me and he is watching both of us and I am going to ask you something I have never asked anyone."

        z "Is this room a room you want to be in. With me. With him. With the three of us being three instead of two-plus-one."

        "Lyra's hand comes up from the tea cup. She takes Zira's hand — the one that was on the relay map, the one that has charcoal on the fingertips. She holds Zira's charcoal-stained fingers in her clean liturgical hand."

        l "Yes."

        l "This is a room I want to be in."

        "Zira's breath does a small thing — not a catch, a release. The release of a woman who has been holding a question in her chest for longer than three months and shorter than fifteen years."

        "She turns to Aeron."

        z "The bench."

        "The bench against the wall. Not a work surface. Not a table. A bench for people who have stopped working and have not left the room yet."

        "Aeron looks at the bench. He looks at Lyra. He looks at Zira."

        # ========== CONSENT GATE ==========

        "Zira is still holding Lyra's hand. Lyra is still looking up at Zira. Aeron is still at the table edge."

        z "I am going to say three things. One of them is tonight. You pick which one."

        z "All three of them end with the three of us in this room. That is not the question. The question is the register."

        menu:
            "All of us. Now. The full room.":
                jump a4_s14a_familiar_full

            "Slowly. I want both of you to remember this.":
                jump a4_s14a_familiar_slow

            "Just this tonight. The three of us on the bench. Hands and quiet.":
                jump a4_s14a_familiar_bench

        # ========== VARIANT A — FULL ==========

label a4_s14a_familiar_full:

        a "All of us. Now."

        "He says it at the table. His hands come off the relay map. He says it the way he said stay in the workshop doorway in s15 — short, flat, true."

        "Zira's hand in Lyra's hand tightens a fraction."

        z "Now."

        "She looks at Lyra."

        l "Now."

        "Lyra says it in the voice she used when she said come with me after the vigil in s19. The voice of a woman who is not performing priest and is not performing prayer and is being a body in a room that has decided what the room is going to hold tonight."

        "Zira pulls Lyra up from the chair by the hand she is holding. Lyra rises. The tea cup stays on the table. The census sheet stays on the table. The relay map stays on the table."

        "The three of them move to the bench."

        "The bench is narrow. The bench is not built for three people. The bench is built for one person who is tired and needs to sit down for a minute before going back to the map. The three of them are going to be closer on this bench than they have ever been in any room."

        "Zira sits first. Lyra sits beside her. Aeron sits on Lyra's other side."

        "Zira's hand is still in Lyra's hand. Lyra's other hand finds Aeron's. Aeron's other hand goes to Zira's knee — the gesture of a man whose body is solving the geometry the mind has not named yet."

        "Three people on a bench. Two lamps. A relay map with two handwritings on it. A room that has decided what it is holding."

        # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
        # [INTIMATE CONTENT HERE]
        # Full variant. Three-body intimacy. Lyra and Zira drive as a
        # pair — they have been building their own rhythm at the table
        # for ninety minutes and that rhythm carries into the physical
        # register. Aeron is present but is not directing. He is the
        # man in between who is being held by two different shapes of
        # attention. Zira is exact. Lyra is steady. The bench becomes
        # the floor at some point — the bench is too narrow. The relay
        # map is visible on the table above them the way the clock was
        # visible on the bench in s15. The two lamps stay on. Nothing
        # in the room goes dark.
        # ---------- [ END INTIMATE BLOCK ] ----------

        jump a4_s14a_familiar_aftercare

        # ========== VARIANT B — SLOW ==========

label a4_s14a_familiar_slow:

        a "Slowly."

        a "I want both of you to remember this."

        "He says it at the table. The second sentence is for both of them. The second sentence is a man telling two women that the pace of the room is going to be the pace that lets memory form."

        "Zira looks at Lyra."

        z "Slowly is a register I know. I catalogued it for him two nights ago in the workshop."

        "She says it to Lyra. Not to Aeron. She is telling Lyra about the workshop the way one woman tells another woman about a room they have both been in with the same man at different times."

        l "Slowly is a register I know too. I held his hand to my sternum and I told him where to put his palm."

        "She says it to Zira. The symmetry of the two disclosures is the women's version of the scene — they are giving each other the information that makes the room possible."

        z "Then we both know slowly."

        z "And he knows that we know."

        "Zira pulls Lyra up from the chair. They move to the bench. Aeron follows."

        "The bench. Zira on one end. Lyra in the middle. Aeron on the other end. The order is different from the full variant — Lyra is in the center because slowly is Lyra's tempo as much as it is Zira's, and the center is where the tempo lives."

        "Zira's hand finds Lyra's wrist — the wrist with the Band. She holds the wrist without touching the Band. The not-touching-the-Band is a respect Lyra does not have to name."

        "Lyra's other hand finds Aeron's jaw — the palm-to-jaw from s19. She places his hand where she wants it: on the flat of her sternum, the callback."

        "Aeron's other hand finds Zira's hand on Lyra's wrist. Three hands in a chain."

        # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
        # [INTIMATE CONTENT HERE]
        # Slow variant. Lyra in the center. The tempo is set by the
        # two women's working rhythm from the table — deliberate,
        # annotated in the way that Zira annotated the map and Lyra
        # annotated the census. The annotations are physical now. Zira
        # narrates as she did in the slow variant of s15. Lyra prays
        # as she did in s19 — not aloud, but in the placement of her
        # hands. Aeron is the surface they are both writing on. The
        # bench becomes the floor. The lamps stay on.
        # ---------- [ END INTIMATE BLOCK ] ----------

        jump a4_s14a_familiar_aftercare

        # ========== VARIANT C — BENCH ==========

label a4_s14a_familiar_bench:

        a "Just this tonight."

        a "The three of us on the bench. Hands and quiet."

        "He says it at the table. He says it with the fullness of a man who has been in the not-tonight variant of s15 and knows what the not-tonight holds and is asking for the same register with one more body in the room."

        "Zira does not let go of Lyra's hand. She nods."

        z "The bench. Hands and quiet. That is a room I can be in."

        "Lyra looks at Aeron with the face she had after the vigil — the face that has just led a rite for a dead runner and is now in a room where three people are deciding what the room is going to hold."

        l "The bench is enough. The bench is the room tonight."

        "They move to the bench."

        "Zira sits first. Lyra sits in the middle. Aeron sits on the other end. The bench is narrow. Their shoulders are touching — all three, a chain of warmth from Zira through Lyra to Aeron."

        "Zira's hand in Lyra's hand. Lyra's hand in Aeron's hand. A chain on the bench."

        "Nobody speaks for a long time."

        "The two lamps make the room warm. The relay map is on the table with both their handwritings on it. The tea cups are where they were left. The room holds three people in the simplest register available."

        # ---------- [ NO INTIMATE BLOCK IN THIS VARIANT ] ----------
        # Bench variant: the scene proceeds directly to aftercare with
        # the intimate block replaced by a non-erotic hold on the
        # bench. Three bodies, hands linked, the mapping station at
        # oh-two-hundred. The hold is the physical realization of
        # "one looking with two directions" in the register where the
        # looking is the whole gift. Lyra's thumb strokes Zira's
        # knuckle once. Zira's shoulder presses Lyra's shoulder once.
        # Aeron's hand holds Lyra's hand without moving.
        # ---------- [ END NON-EROTIC HOLD ] ----------

        jump a4_s14a_familiar_aftercare

label a4_s14a_familiar_ground_emp_below_threshold:

    # ========== BELOW THRESHOLD — TENDER NON-ESCALATION ==========

    "The room holds the three sentences — Zira's naming, Lyra's scripture, Aeron's one-looking — and the three sentences are enough for the night."

    "Nobody moves toward the bench."

    "Instead, Zira sits back down in her chair. Lyra picks up her tea cup. Aeron stays at the table edge."

    "They work for another twenty minutes."

    "The twenty minutes are different from the first ninety. The difference is: the room has been named. The room knows what it is now. The work on the relay map continues but the work is happening inside a room that has acknowledged itself, and the acknowledgment changes the temperature of the work without changing the content."

    "Zira's stylus traces a route and her hand passes close to Lyra's hand on the census sheet, and neither of them flinches and neither of them comments."

    "Lyra passes Aeron a distance figure and their fingers touch on the paper, and the touch lasts half a second longer than a paper-pass touch lasts."

    "Aeron reads a route annotation in Zira's handwriting and then reads a census annotation in Lyra's handwriting and the two handwritings on the same map are a sentence he is going to carry out of this room."

    athought "They are not competing. I have been waiting — without knowing I was waiting — for two of them to be in the same room and for the room to cost something. The room does not cost something. The room is free. The room is free because neither of them is asking me to choose and neither of them is asking the other to leave and the work they are doing is the work the civilians need and the work is the ground they share."

    athought "Familiar ground."

    "At oh-two-hundred Zira rolls the relay map. Lyra collects the census sheets. Aeron pushes off the table edge."

    "They stand in the mapping station in the two-lamp light."

    z "We should do this again."

    l "Tomorrow night. Same time. I will bring tea."

    z "Bring three cups."

    "She says it without looking at Aeron. The sentence does not need Aeron to be its audience. The sentence is for Lyra. The three cups is Zira's way of saying: the third body is welcome at the table."

    l "Three cups."

    "Lyra says it back. The echo is a confirmation."

    "Aeron says nothing. He does not need to say anything. The three-cups sentence was not for him and the fact that it was not for him is the gift."

    $ nudge_poly("lyra_zira_three_cups", delta=1)

    jump a4_s14a_familiar_state_updates

    # ========== PHASE 5 — AFTERCARE ==========

label a4_s14a_familiar_aftercare:

    "Later."

    "The two lamps are still on. The relay map is on the table. The tea cups are where they were left — Lyra's nearly empty, Zira's half-empty, no third cup because Aeron arrived after the tea and did not ask for one."

    "The three of them are on the bench."

    "Zira is on one end. Lyra is in the middle. Aeron is on the other end. Their shoulders are in a line. The bench is too narrow for three people to sit without touching and they are touching at every point the bench allows."

    "Nobody has spoken for a while."

    "The first sentence of the aftercare comes from Lyra."

    "She is not speaking to Aeron. She is speaking to Zira."

    l "I thought I would be jealous."

    "A beat. Zira's head turns toward Lyra. Not all the way — a quarter-turn, the angle of a woman listening from the side."

    l "I have been carrying the possibility of jealousy for — I do not know how long. Since I realized that his attention had a direction that was not only mine. I carried it the way I carry a prayer that I do not know the ending of. I held the possibility that the ending was jealousy and I held the possibility that it was not and I did not open either possibility because opening either one would have made the other one impossible."

    l "I opened it tonight."

    l "I am not jealous."

    l "I am relieved."

    "She says relieved the way she said Seren. In the voice that is not performing the word but is being inside the word."

    "A beat."

    "Zira is quiet for a long count."

    zthought "She said relieved. She said she thought she would be jealous and she is not jealous. She said she is relieved."

    zthought "That is a sentence no one has ever said to me about anything."

    zthought "People have said many things to me. People have said I am useful. People have said I am sharp. People have said I build good doors and I run good routes and I have steady hands. Nobody has ever said that the experience of sharing something with me produced relief."

    zthought "Relief is the word of a woman who has been holding a weight alone and has discovered that the weight is lighter when another person is under it."

    zthought "I am the other person."

    z "That is the first time anyone has said that to me about anything."

    "She says it in the Ashmarket flat. No edge. The flat is the flattest register she has — the register that does not have room for performance because the sentence is taking up all the room."

    "Lyra turns her head toward Zira. The quarter-turn to match Zira's quarter-turn. Their faces are close. Aeron is on the other side of Lyra and he can see both profiles — Lyra's cleric-calm and Zira's Ashmarket-flat — and the two profiles are looking at each other over the space where his shoulder is."

    l "Get used to it."

    "She says it gently. With the warmth of a woman who has been a priest for eleven years and knows that the sentence get used to it is the hardest sentence a person can receive because it requires them to believe the thing will happen again."

    "Zira's mouth does a thing Aeron has never seen. It is not a smile. It is the shape her mouth makes when it has been holding a particular tightness for a long time and the tightness is released by a sentence she did not expect."

    z "I will try."

    "A beat."

    "Lyra puts her head on Zira's shoulder."

    "The gesture is simple. It is the gesture from the vigil — the head-on-shoulder of a woman who is tired and is allowing herself to rest against another body. But the body is Zira's, not Aeron's. The gesture is Lyra choosing to rest on the woman in the room, not the man."

    "Zira does not move for a beat. Then her hand — the charcoal-stained one — comes up and rests on the side of Lyra's head. Not holding. Resting. The way a person rests a hand on a thing they have just discovered they are allowed to touch."

    "Aeron watches."

    athought "They are holding each other."

    athought "I am on the bench with them and they are holding each other and I am not between them. I am beside them. The geometry is not a triangle with me at the center. The geometry is a line with Lyra in the middle and Zira on one end and me on the other and the line is warm the whole way through."

    athought "This is what it looks like when two people who love the same man discover they also have something that is not about the man."

    athought "Familiar ground."

    "Lyra's hand — the one not in Zira's — reaches behind her and finds Aeron's hand on the bench. She takes it without turning. She holds it."

    "The three of them on the bench. Lyra's head on Zira's shoulder. Zira's hand on Lyra's head. Lyra's hand in Aeron's hand. Three bodies in a line."

    "The two lamps make the room warm."

    "The relay map on the table has both their handwritings on it."

    "The scene holds on the three pairs of hands. Lyra's on Zira's. Zira's on Lyra's. Lyra's on Aeron's. Three people on a bench in a mapping station at oh-two-hundred with the civilian move forty-eight hours away and the work done and the room named."

    "Fade."

    $ nudge_poly("lyra_zira_aeron_triad", delta=1)

    jump a4_s14a_familiar_state_updates


    # ========== STATE UPDATES (CONVERGENCE) ==========

label a4_s14a_familiar_state_updates:

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1, attraction=1)
    $ rel_bump("Zira", trust=1, attraction=1)
    $ flag("lyra_zira_poly_recognized", True)
    $ flag("familiar_ground_scene_complete", True)
    $ canon_set("lyra_zira.working_rhythm", "civilian_move_mapping_station")
    $ canon_set("aeron.poly_geometry", "one_looking_two_directions")
    $ npc_remember("Lyra", "said_i_am_relieved_not_jealous", weight=3)
    $ npc_remember("Zira", "said_first_time_anyone_said_that_to_me", weight=3)
    $ npc_remember("Lyra", "quoted_the_six_do_not_count_the_number", weight=2)
    $ npc_remember("Zira", "said_three_cups", weight=2)
    $ npc_remember("Aeron", "said_one_looking_two_directions", weight=3)
    $ tp_seed("a4.lyra_zira.familiar_ground")
    $ tp_seed("a4.poly.three_body_recognized")
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s14a_familiar_ground_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Zero one fifteen the night after s14 (return to the table). Aeron
#     has been at the ops table for four hours. He is walking the base.
#     He turns the corner toward the mapping station and hears two
#     voices: Lyra and Zira, working the civilian move logistics
#     together without him.
# cann.what_happened:
#   - Lyra and Zira have been in the mapping station since 23:30,
#     working the civilian move. Lyra has the census and brought tea.
#     Zira has the relay map. Their handwritings are on the same
#     surface — the first time these two women have collaborated
#     directly without the full group present.
#   - Aeron arrives in the doorway. Two faces look up. The two-look
#     is the scene's thesis image. He enters and stands at the table
#     edge (no third chair). They work the civilian move in a three-
#     body configuration for twenty minutes.
#   - Recognition beat: Zira names the room. "Is this what we are
#     doing. All three of us in the same room." Lyra quotes the text
#     of the Six: "The Six do not count the number. They count the
#     honesty." Aeron: "I have one looking with two directions."
#   - Poly gate: if metric("poly_pressure") >= 3, Zira asks the
#     question directly. Consent gate: three choices (full / slow /
#     bench-only). All three end with the three of them on the bench.
#     Two lead to [INTIMATE CONTENT HERE] blocks, one to a non-erotic
#     hold.
#   - If poly_pressure below threshold: the room is named but not
#     escalated. They work another twenty minutes. Zira says "bring
#     three cups." The three-cups sentence is the below-threshold
#     version of the room's acknowledgment.
#   - Aftercare (escalated variants): Lyra speaks to Zira (not to
#     Aeron): "I thought I would be jealous. I am not jealous. I am
#     relieved." Zira: "That is the first time anyone has said that
#     to me about anything." Lyra puts her head on Zira's shoulder.
#     Zira's hand on Lyra's head. Lyra's hand in Aeron's hand. The
#     geometry is a line, not a triangle.
# cann.aeron_state:
#   - First time in Act IV that being outside a conversation has not
#     cost him something. The two-look at the doorway is the thesis
#     image of the poly configuration: two women, one man, and the
#     man's centrality is not the point. The work is the point.
#   - "One looking with two directions" is his honest sentence for
#     the poly geometry. Do not give this phrasing to another scene.
# cann.lyra_state:
#   - The Band is on her wrist (she put it back on after s19). She
#     is not performing priest tonight. She is doing logistics that
#     are holy because the civilians are holy. The scripture she
#     quotes ("The Six do not count the number") is pre-Academy,
#     from the oldest layer of the tradition.
#   - "I am relieved" is her Act 4 poly thesis sentence. The relief
#     is the discovery that the weight is lighter when another person
#     is under it.
# cann.zira_state:
#   - Post-s15. The clock scene is behind her. She is in operational
#     mode at the mapping table but the operational mode has been
#     recalibrated by s15. The stylus grip is looser. The charcoal
#     on her fingertips is the scene's physical marker.
#   - "The time difference is the least interesting thing about us"
#     is her Act 4 poly thesis sentence. The Ashmarket flat register.
#   - "That is the first time anyone has said that to me about
#     anything" is the load-bearing aftercare line. Cross-reference
#     with the four-pulse Ashmarket tell from s15.
# cann.thematic_flags:
#   - Act 4 EMP arm: poly configuration formally surfaced in a scene
#     between two LIs and Aeron. The scene is structured so the
#     women's relationship to each other is the primary subject;
#     Aeron's presence is the tertiary subject.
#   - The "familiar ground" title is Aeron's internal phrase for the
#     discovery that the room between Lyra and Zira is not contested
#     territory but shared ground.
#   - Relay map with two handwritings = visual thesis of the poly
#     configuration. Two different kinds of competence on the same
#     surface, aimed at the same civilians.
