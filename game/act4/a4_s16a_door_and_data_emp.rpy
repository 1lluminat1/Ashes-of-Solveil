# =======================================================
# ACT 4 - Scene 16a: Door and Data (Empathy Path)
# File: a4_s16a_door_and_data_emp.rpy
# Type: POLY BEAT — ZIRA + NOELLE + AERON
# Placement: after s16 (Rhea strikes). Post-Rhea strike.
# Noelle's predictive framework just got Davel Ostra killed.
# Zira's runner network is exposed. Both women converge on
# Aeron not for comfort but for RECALIBRATION. The intimacy
# here is two competent women who respect each other's
# intelligence solving a problem with a man they both love.
# The work becomes the connection.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s16a_door_and_data_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s16a_door_and_data_emp:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s16a_door_and_data_emp")
    $ show_timeline("DAY 52", "16:00", "Phoenix Secondary Base — Noelle's Workspace")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Five movements.
    #         (1) Noelle's workspace from outside. 50mm, locked. The door
    #             is open. The overhead strip is at full — she has not
    #             adjusted the lighting tonight because the lighting is
    #             not the point. The datapad is on the desk. A second
    #             datapad is open beside it. Paper is on the floor — not
    #             dropped, placed. She has been laying out the framework
    #             failure in physical space because the screen is too
    #             small for the shape of the mistake.
    #         (2) Zira arriving. 35mm, tracking. Zira comes down the
    #             corridor at operational pace — the pace of a woman
    #             whose runner network was just exposed and who has done
    #             the triage and is now looking for the person who built
    #             the model that sent Davel to the canal. She is not
    #             angry. She is carrying the thing that comes after anger
    #             when the person you are angry at is also the person
    #             whose work you need to survive the next forty-eight
    #             hours.
    #         (3) Inside — two-shot. 35mm. Zira enters Noelle's workspace
    #             without knocking. Noelle does not look up. The camera
    #             holds the two of them in a wide two-shot — Noelle at
    #             the desk, Zira in the doorframe. The two-shot is the
    #             thesis image: two women who have not been in a room
    #             together for this purpose before.
    #         (4) The work. 35mm, slow push. They work. The camera moves
    #             in over the course of the work sequence — from the wide
    #             two-shot to a close two-shot to an almost-close three-
    #             shot when Aeron arrives and takes the third position at
    #             the desk. The push is gradual. The audience does not
    #             notice the camera closing until the three-shot is tight.
    #         (5) The held beat. 50mm, still. Three faces at the desk.
    #             The datapads between them. The paper on the floor. The
    #             moment when the work stops being work and becomes the
    #             other thing. Fade.
    # LIGHTING: Noelle's workspace overhead at full. Harsh. She has not
    #           softened it. The harshness is the register — she is not
    #           making the room comfortable because the room is not about
    #           comfort. When Aeron arrives, nobody adjusts the lighting.
    #           The harsh light stays harsh through the poly gate. If the
    #           scene escalates: at some point the overhead gets clicked
    #           off and the desk lamp (which has been on underneath the
    #           overhead this whole time, invisible under the stronger
    #           light) becomes the only source. The desk lamp is the
    #           Noelle lamp — the warm practical from s18. The shift from
    #           overhead to desk lamp is the scene's visual consent.
    # SFX: Workspace ambient. The hum of the overhead strip at full
    #      power. The datapad's faint electronic tick when Noelle scrolls.
    #      Zira's boots on the floor — she does not take them off in
    #      Noelle's workspace the way she would in her own. Paper
    #      shifting. The stylus on the datapad surface. The small
    #      clicking sound Noelle's jaw makes when she is clenching
    #      without realizing she is clenching — Aeron notices this,
    #      Zira notices this. No music at any point. The scene is scored
    #      by work sounds.
    # FX/COMP: THE PAPER ON THE FLOOR. The framework failure laid out in
    #          physical space. Noelle has printed the probability chains
    #          and the route assessments and has placed them on the floor
    #          in the particular spatial arrangement she uses when a model
    #          has failed and she needs to see the failure with her whole
    #          body rather than through a screen. The paper is the scene's
    #          primary prop. It is the thing Zira steps over when she
    #          enters. It is the thing Aeron does not step on when he
    #          arrives. It is the map of the mistake that killed Davel
    #          Ostra.
    #          THE TWO DATAPADS. Noelle's primary and her secondary. The
    #          secondary is the one she carries to meetings. The primary
    #          is the one that lives on this desk. Both are open. Both
    #          are showing the same model from different angles.
    # BLOCKING: Noelle at the desk. Zira in the doorframe, then at the
    #           edge of the desk. Aeron arrives later and stands behind
    #           the desk — not at it, behind it, the position of a man
    #           who is here to listen to two women work rather than to
    #           lead. Later he moves to the desk edge. The three of them
    #           end up close at the desk — closer than any operational
    #           briefing has put them.
    # FACE: Noelle — the face from s18 but colder. Not the cold of
    #       detachment — the cold of a woman who has run the numbers
    #       on a dead man and found herself in the variance. She is
    #       not crying. She has not cried. She has printed the failure
    #       on paper and laid it on the floor and the laying-out is
    #       her version of crying.
    #       Zira — the Ashmarket operational. The same face she wears
    #       when a relay has been burned and the network needs
    #       rebuilding. But there is a second thing in her face: the
    #       recognition that the woman at the desk is a woman whose
    #       work she has been relying on for three months and the
    #       reliance is about to be spoken aloud.
    #       Aeron — arriving later. The face of a man who has spent
    #       the last two hours in the war room and has come to Noelle's
    #       workspace to check on her and has found two women already
    #       in the process of rebuilding the thing that broke.

    # ========= VOICE BASELINE =========
    # EMP cadence. Noelle and Zira drive. The register is operational
    # for the first two phases — these are two analysts working a
    # problem. The operational register cracks in phase 3 when the
    # work stops being about the model and starts being about the
    # women doing the model. Aeron speaks least in the first half
    # and more in the aftercare. Internal thoughts on all three:
    # nthought (Noelle processing the failure), zthought (Zira
    # processing the reliance), athought (Aeron processing the
    # geometry of two women who are better together at this work
    # than either is alone or either is with him).

    # scene bg_noelle_workspace_overhead_full_emp with dissolve
    # play ambient "sfx/ambient/workspace_overhead_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE FAILURE ON THE FLOOR ==========

    "Twenty-two forty. Six hours since Davel Ostra. Four hours since the vigil."

    "Noelle has been in her workspace for three of those four hours."

    "She has not left. She has not gone to the corridor with the window. That was last time — the time she needed to be in a place that did not have her framework in it. Tonight she needs to be in the place that has the framework, because the framework is the thing that failed and the failure needs to be inside the room where the framework lives."

    "The paper is on the floor."

    "She has printed the probability chains. She has printed the route assessments. She has printed the canal rendezvous model — the model that said the rendezvous point had a fourteen percent chance of interdiction and the fourteen percent came up and the fourteen percent killed Davel Ostra."

    "The paper is on the floor in the spatial arrangement she uses for catastrophic model failure. Not scattered. Placed. Each sheet at a specific angle to the others. The arrangement is the model of the failure seen from above, the way a cartographer maps a flood after the water has receded."

    nthought "Fourteen percent."

    nthought "The model said fourteen percent. The model was correct. Fourteen percent is not zero. Fourteen percent is one in seven. I sent a man into a one-in-seven field and the seven came up wrong."

    nthought "The model did not fail. The model was accurate. The model said fourteen percent and the fourteen percent happened. The failure is not the model. The failure is that I treated fourteen percent as a number instead of as a name. The name of the fourteen percent was Davel Ostra and I did not put his name into the model because the model does not have a field for names."

    nthought "I need to rebuild the model with a field for names."

    nthought "I do not know how to do that. A model with a field for names is not a model. A model with a field for names is a prayer."

    nthought "I do not know how to pray."

    "The workspace door is open. The overhead is at full. The datapad is on the desk with the secondary beside it, both open, both showing the canal rendezvous model from different angles."

    "Noelle is sitting at the desk with her hands flat on the surface, not touching the datapads. She is looking at the paper on the floor."

    "Footsteps in the corridor."

    "She does not look up."

    # ========== PHASE 2 — ZIRA ARRIVES ==========

    "Zira walks into the workspace without knocking."

    "She does not knock because the door is open and the open door is Noelle's grammar for I am working and the door is not a barrier, and Zira reads doors the way she reads relay networks — by the grammar of the opening."

    "She stops in the doorframe."

    "She looks at the paper on the floor."

    "She looks at Noelle at the desk."

    "She does not say anything for a beat."

    zthought "She has printed it. She has taken the model that killed my runner and she has printed it and laid it on the floor of her workspace in the pattern I have seen her use twice before — once after the Sector 7 miscalculation and once after the logistics failure in the supply chain two months ago. The pattern means: the model has failed and I am going to look at it until I can see where the failure lives."

    zthought "I came here to say: your framework just got a runner killed."

    zthought "I am looking at the paper on the floor and I am looking at her hands flat on the desk and I am going to say it anyway, because the sentence needs to be in the room, and then I am going to do the thing I came here to do, which is not to blame her."

    z "Your framework just got a runner killed."

    "She says it from the doorframe. She says it in the Ashmarket flat — no edge, no accusation, the flat of a sentence that is true and needs to be said before the next sentence can exist."

    "Noelle does not look up."

    n "I know."

    "Two words. The lowest register Zira has heard from Noelle. Lower than the analytic register. Lower than the register from the corridor window in s18. This is the register of a woman who has been sitting with the knowledge for six hours and the knowledge has settled into the bottom of her voice."

    n "I need to rebuild it."

    "A beat."

    n "I need to rebuild it with you."

    "Zira steps over the paper on the floor. She steps over it carefully — not stepping on any sheet, placing her boots in the gaps between the probability chains, because the paper on the floor is Noelle's work and Zira does not step on another woman's work even when the work has failed."

    "She reaches the desk."

    z "Then sit down."

    n "I am sitting down."

    z "Then I will stand."

    "She stands at the edge of the desk. She looks at the datapads. She looks at the model on the primary screen."

    z "Show me where the fourteen percent lives."

    "Noelle turns the primary datapad toward Zira. Her hand is steady. The steadiness is not the steadiness of a woman who is in control — it is the steadiness of a woman whose hands have been steady on datapads for so long that the steadiness is involuntary, a residue of competence that outlasts the competence itself."

    n "The fourteen percent is here."

    "She points. Zira leans in."

    "They work."

    # ========== PHASE 3 — THE WORK BECOMES THE CONNECTION ==========

    "For the next thirty-five minutes they work the failure."

    "Noelle walks Zira through the probability chains. Zira walks Noelle through the relay network — the real network, the one that exists in Zira's head and in her charcoal maps, the network of runners and dead drops and cutover points that the model was supposed to protect."

    "They do not agree on everything. They disagree on the weighting of the canal approach — Noelle's model weighted the canal as low-risk based on patrol frequency; Zira's network assessment weighted it as medium-risk based on the line of sight from the bridge. The disagreement is productive. The disagreement is two forms of intelligence meeting on the surface of a dead man's route."

    n "Your network assessment puts the canal at medium risk."

    z "Yes."

    n "My model puts it at low. The difference is the line of sight from the bridge."

    z "Yes. Your model does not account for the line of sight because the line of sight is a physical variable and your model is a statistical one."

    n "I know."

    z "I am not saying that to assign blame."

    n "I know what you are not saying. You are not saying it because you came in here and said the blame sentence first and the blame sentence is finished and now we are in the rebuild."

    z "Yes."

    n "Good."

    "A beat."

    n "I need the line of sight in the model. I need the physical variables. I need the things your runners see with their bodies that my numbers do not see."

    z "I can give you that."

    n "I know you can give me that. I am asking you to give me that."

    z "Then I am giving it to you."

    "They work. The work changes shape. It is no longer Noelle walking Zira through the model. It is two women building a new model together — Noelle's statistical framework with Zira's physical intelligence layered into the probability chains."

    "Zira picks up the stylus from the desk. She draws on the secondary datapad — a route diagram in her charcoal-line style, the same style as the relay map. She draws the canal approach with the line of sight from the bridge marked in red."

    "Noelle watches Zira draw. She watches the way Zira's hand moves on the surface — the steady deliberate strokes of a woman who has been drawing routes since she was eighteen."

    nthought "She draws the way I calculate. With the full weight of the thing she knows behind every stroke. There is no excess in her line. There is no decoration. The line is the route and the route is the thing that keeps people alive and the line knows that."

    nthought "I have been relying on her network for three months and I have never watched her draw."

    nthought "I should have watched her draw."

    "Zira finishes the canal diagram. She turns the datapad back to Noelle."

    z "The red line is the line of sight. Everything inside the red line is visible from the bridge at any time of day. Your model needs to treat the red zone as a different probability field from the rest of the approach."

    n "I can do that."

    n "I should have done that three months ago."

    z "Three months ago I was not in this room."

    "A beat. The sentence lands in the workspace the way a tool lands on a bench — with the weight of a thing that was picked up for a purpose."

    "The door is still open."

    "Aeron appears in the doorway."

    # ========== PHASE 4 — AERON ARRIVES ==========

    "He has been in the war room. He has been in the war room for two hours since the vigil and he has come to Noelle's workspace because Tessa told him Noelle had been in her workspace since nineteen hundred and had not left."

    "He stops in the doorway."

    "He sees Noelle at the desk. He sees Zira at the desk edge. He sees the paper on the floor. He sees the two datapads with the canal model and Zira's route diagram. He sees two women working the failure together."

    athought "They are already here."

    athought "I came to check on Noelle and Zira is already here. Zira is at Noelle's desk with a stylus in her hand drawing a route diagram on Noelle's secondary datapad. They are rebuilding the model. They are rebuilding the model together."

    athought "I do not need to be in this room for this work to happen. The work is happening without me. The work has been happening for — I do not know how long, but the two datapads and the route diagram say thirty minutes at least."

    "Noelle looks up."

    "Zira looks up."

    "Two faces. The two-look. The same two-look from the mapping station with Lyra — but different. This two-look is not the look of two women working logistics who are pleased to see a third body. This two-look is the look of two women who are in the middle of rebuilding a thing that broke and the man who signed the operation that broke it is standing in the doorway."

    n "Come in."

    z "Close the door."

    "He comes in. He closes the door. The workspace is sealed — Noelle at the desk, Zira at the desk edge, Aeron behind the desk."

    "He does not move to the desk. He stays behind it. The position of a man who is here to listen."

    a "How far are you."

    n "We have the canal failure mapped. Zira has the line-of-sight variable isolated. I need to rebuild the probability chains with her physical data layered in."

    a "How long."

    n "If she stays — two hours. If she does not stay — a week."

    z "I am staying."

    "Aeron looks at Zira. Zira looks at Aeron. The look between them is the workshop look — the look from s15, the look of two people who have been on a floor together and are now in a different room doing a different thing and the floor is still between them."

    "He looks at Noelle. Noelle looks at Aeron. The look between them is the corridor look — the look from s18, the look of a woman who walked to a window without her datapad and is now back at the desk with the datapad and the man who found her at the window is in the room."

    athought "I am looking at two women. The same looking. The one looking with two directions."

    athought "But this room is not the mapping station. This room is a workspace where a model failed and a runner died and two women are rebuilding the model with their combined intelligence and I am the man who signed the order. The geometry is not warm. The geometry is sharp. And the sharpness is the thing that is going to save the next runner."

    a "I will work with you."

    "He moves to the desk. He takes the position between Noelle and Zira — not at the chair, standing, because the chair is Noelle's and the desk edge is Zira's and the standing position is the position of a man who is bridging two forms of intelligence."

    "They work."

    "They work for an hour."

    "The hour changes the room."

    "The paper on the floor gets reorganized — Zira picks up three sheets and places them in a new configuration based on her network knowledge. Noelle does not object. She watches Zira move the paper and she integrates the new configuration into the model in real time."

    "Aeron reads the model as it evolves. He asks questions. His questions are the questions of a commander who needs to send people into the field in forty-eight hours and needs the model to be the model that does not produce another Davel Ostra."

    "At some point in the hour, Noelle's hand and Zira's hand are on the same datapad at the same time. Their fingers are close. Neither moves. The proximity is the proximity of two women whose intelligence has been adjacent for three months and is now touching."

    nthought "Her hand is next to mine on the datapad."

    nthought "Her hand is the hand that draws routes. My hand is the hand that calculates probabilities. The two hands on the same surface is a sentence I have not seen before and the sentence is: we should have been doing this from the beginning."

    "Zira notices Noelle noticing."

    zthought "She is looking at our hands on the datapad. She is looking at the proximity. She is not moving her hand away. I am not moving my hand away. The not-moving is a mutual sentence."

    "They finish the first rebuild pass at twenty-three fifty."

    "Noelle saves the model. She sets the datapad down."

    "Zira sets the stylus down."

    "Aeron leans back from the desk."

    "The room is quiet for the first time in an hour."

    $ nudge_poly("zira_noelle_rebuild", delta=1)

    # ========== PHASE 5 — POLY GATE ==========

    if metric("poly_pressure") >= 3:

        "The quiet in the workspace is different from the quiet of the mapping station. The mapping station quiet was the quiet of work completed. This quiet is the quiet of three people who have been working at a pitch of intensity that has burned through the professional register and left something underneath."

        "Noelle looks up from the datapad."

        "She looks at Zira."

        "She looks at Aeron."

        "She looks at the two of them."

        "The two-look from the other side."

        nthought "I am looking at two faces."

        nthought "I am looking at two faces that are reading me the way I read models. Zira is reading the small tension in my jaw that I was not aware of until I saw her see it. Aeron is reading the angle of my shoulders that changed at some point in the last hour from the angle-of-working to the angle-of-something-else."

        nthought "They are both reading me. They are reading me with different instruments — Zira reads bodies, Aeron reads faces — and they are arriving at the same reading."

        nthought "I do not know what to do with that."

        n "I am looking at two faces that are reading me the way I read models."

        "She says it out loud. She says it at the desk, in the overhead light, in the register of a woman who has been stripping the analytic voice all night and has arrived at the register underneath."

        n "I do not know what to do with that."

        "Zira does not look away from Noelle."

        z "Then stop modeling."

        "Two words. The Ashmarket flat. The same register Zira used to say sit down at the beginning of the scene. The register that does not have room for anything except the sentence."

        "Aeron does not speak. He watches. He is the third body in a room where two women are having a conversation that is not about the model anymore."

        n "I do not know how to stop modeling."

        z "You stopped for ten minutes in a corridor two weeks ago. You stood at a window without your datapad. You were not modeling. You were being a person."

        n "You know about the window."

        z "Aeron told me about the window."

        "Noelle looks at Aeron."

        a "I told her about the window."

        n "Why."

        a "Because the window was a thing that mattered about you and she is a person who matters to me and the two things-that-matter were going to meet eventually."

        "A beat. Noelle processes the sentence. The processing is visible — her eyes move from Aeron to Zira and back, the movement of a woman running a computation that does not have a framework."

        n "You told her about the window. She told you about — what did she tell you about?"

        z "I told him about the clock."

        n "The clock."

        z "I built a clock that runs backwards. He sat on the floor of my workshop and listened to it. That is the version of the window I have."

        "Noelle looks at Aeron."

        n "You have been sitting on floors and standing at windows with both of us."

        a "Yes."

        n "And the sitting and the standing are — you are not doing different things. You are doing the same thing in two rooms."

        a "Yes."

        "A long beat."

        n "I am a woman who reads models. I am looking at a model right now. The model has three variables. The three variables are in this room. The model says —"

        "She stops."

        n "The model says something I do not have a unit for."

        z "You had a unit for it two weeks ago. In the corridor. You called it want."

        n "Want was a framework."

        z "Want is a framework. Use it."

        "Noelle closes her eyes. She opens them."

        n "I want to be in this room with both of you and I want the room to not be about the model."

        # ========== CONSENT GATE ==========

        z "Then we are going to ask you a question."

        z "Aeron and I are going to ask you a question and you are going to answer it in the register you have, whatever that register is, and we are going to hear the answer."

        n "Ask."

        z "What do you want tonight. All of it. In the room with us. Not the rebuild. Not the model. The thing underneath."

        "Noelle looks at Aeron. She looks at Zira. The overhead light is harsh on all three faces."

        menu:
            "I want both of you. Here. With the data still on the desk.":
                jump a4_s16a_door_data_full

            "I want this slowly. I want to learn how to be read.":
                jump a4_s16a_door_data_slow

            "I want to sit with this. The three of us. The model on the desk and our hands near it.":
                jump a4_s16a_door_data_sit

        # ========== VARIANT A — FULL ==========

label a4_s16a_door_data_full:

        n "Both of you."

        n "Here. With the data still on the desk."

        "She says it in a register Zira and Aeron have not heard — the register that is neither analytic nor stripped-of-analytic. The register that is a woman who has named what she wants and is letting the naming be the framework."

        "Zira reaches over and clicks the overhead off."

        "The workspace drops into the desk lamp. The warm practical. The Noelle lamp. The paper on the floor is still visible but the edges are soft now. The datapads glow."

        z "The overhead was too much."

        n "I know. I did not know how to turn it off."

        z "I did."

        "Aeron moves from behind the desk to beside it. The three of them are close now — closer than operational. Noelle in the chair. Zira at the desk edge. Aeron at the desk edge on the other side. The desk between them has the model on it. The model is going to stay on the desk."

        "Zira's hand finds Noelle's hand on the desk surface. The touch is deliberate — not the accidental proximity from earlier, a chosen contact. Her fingers over Noelle's fingers."

        "Aeron's hand finds the other side of Noelle's hand. Two hands on one hand."

        "Noelle looks at the three hands on the desk."

        n "I am going to document this."

        z "I know."

        n "Not now. After. I am going to log it. It is the only language I trust."

        z "Then trust it."

        # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
        # [INTIMATE CONTENT HERE]
        # Full variant. Three-body intimacy in Noelle's workspace. The
        # desk lamp is the only light. The data is still on the desk.
        # The paper is still on the floor. Zira drives the physical
        # register — she is the one who turned off the overhead, she
        # is the one who is going to set the pace. Noelle is present in
        # a new register — the register of a woman who has named her
        # want and is letting two people read her. Aeron is the bridge
        # between two forms of intelligence. The workspace does not
        # become romantic. The workspace stays a workspace. The intimacy
        # happens on the floor beside the desk, on the paper that maps
        # the failure, the failure underneath them like a ground they
        # have agreed to rebuild together. The data stays on the desk.
        # ---------- [ END INTIMATE BLOCK ] ----------

        jump a4_s16a_door_data_aftercare

        # ========== VARIANT B — SLOW ==========

label a4_s16a_door_data_slow:

        n "Slowly."

        n "I want to learn how to be read."

        "She says it at the desk. She says it in the register of a woman who has spent her life reading and has never learned how to be the text."

        "Zira reaches over and clicks the overhead off. The desk lamp."

        z "Slowly is a thing I know how to do."

        "She looks at Aeron."

        z "Tell her what you see."

        a "I see a woman who has printed her failure on paper and laid it on the floor because the screen was too small for the shape of the mistake. I see a woman whose jaw has been clenching for six hours without her knowing. I see a woman whose hand on the datapad was next to Zira's hand for thirty seconds and neither of them moved."

        "Noelle's jaw unclenches. She did not know it was clenched. She knows now because he named it."

        n "You can see the clenching."

        a "I have been watching the clenching for a year and a half."

        z "I have been watching it for three months."

        n "You have both been reading me."

        z "Yes."

        a "Yes."

        n "Then read me now. Slowly."

        "Zira's hand finds Noelle's hand on the desk. Aeron's hand finds the other side. Two hands on one hand. The three of them at the desk."

        # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
        # [INTIMATE CONTENT HERE]
        # Slow variant. The reading is the grammar. Zira reads Noelle's
        # body with the precision of a woman who draws routes. Aeron
        # reads Noelle's face with the attention of a man who has been
        # watching the jaw-clench for eighteen months. Noelle lets
        # herself be read. The desk lamp. The paper on the floor. The
        # data on the desk. The room stays a workspace. The intimacy
        # is the intimacy of being seen by two different instruments
        # at the same time and letting the seeing be the text.
        # ---------- [ END INTIMATE BLOCK ] ----------

        jump a4_s16a_door_data_aftercare

        # ========== VARIANT C — SIT ==========

label a4_s16a_door_data_sit:

        n "I want to sit with this."

        n "The three of us. The model on the desk. Our hands near it."

        "She says it in the register that is closest to the analytic register but is not the analytic register. It is the register of a woman who is choosing to hold the shape of the room as it is rather than changing the shape into something the room has not prepared for."

        "Zira nods."

        z "Sitting is a room I can be in."

        "She does not turn off the overhead. The overhead stays harsh. The harshness is the right light for sitting — the light of a workspace that is still a workspace, where three people are not pretending the workspace is something else."

        "Aeron moves from behind the desk to beside it."

        "The three of them settle. Noelle in the chair. Zira pulling a second chair from the corner of the workspace — there is one, pushed against the wall, the chair for the occasional visitor who never comes because Noelle does not have occasional visitors. She pulls it to the desk. She sits."

        "Aeron sits on the floor."

        "He sits on the floor because the two chairs are taken and because the floor is where the paper is and the paper is the failure and sitting with the failure is the thing he signed when he signed the operation."

        "The three of them in Noelle's workspace. Two at the desk. One on the floor. The paper between them."

        "Noelle's hand is on the desk. Zira's hand is on the desk near Noelle's. Aeron's hand is on the paper on the floor — not on a probability chain, in the gap between two sheets, his palm flat on the workspace floor."

        "Nobody speaks for a long time."

        "The quiet is the quiet of three people who have worked a failure together and are now sitting in the room where the failure lives and the sitting is enough."

        # ---------- [ NO INTIMATE BLOCK IN THIS VARIANT ] ----------
        # Sit variant: the scene proceeds directly to aftercare with
        # the intimate block replaced by a non-erotic hold in the
        # workspace. The overhead is still on. The data is on the desk.
        # The paper is on the floor. Three people sitting with the
        # model that killed a runner, not pretending the model is not
        # there, not pretending the room is anything other than a
        # workspace where a failure is being rebuilt. Noelle's hand
        # on the desk edge closest to Zira's hand. Zira's thumb
        # against the edge of Noelle's little finger. Aeron's hand
        # on the floor among the paper.
        # ---------- [ END NON-EROTIC HOLD ] ----------

        jump a4_s16a_door_data_aftercare

label a4_s16a_door_and_data_emp_below_threshold:

    # ========== BELOW THRESHOLD — TENDER NON-ESCALATION ==========

    "The quiet in the workspace settles."

    "Noelle looks at Aeron. She looks at Zira. She looks at the two of them and the looking has the thing in it — the recognition from the model, the awareness that three variables are in the room — but the looking does not tip over into the naming."

    "Instead she says something else."

    n "We should do this again."

    z "The rebuild."

    n "The rebuild. And the — the being in the same room while we do it."

    "She does not name the other thing. The other thing is in the room. The other thing does not need naming tonight. The other thing needs the two hours of work that just happened to exist first, and the two hours exist now."

    z "Tomorrow night. Same time. I will bring the western relay update."

    n "I will have the rebuilt model ready for a first pass."

    "Noelle looks at Aeron."

    n "Will you be here."

    a "I will be here."

    n "Good."

    "She picks up the primary datapad. She does not turn it off. She holds it the way she held it in every scene before s18 — like a part of herself. But she holds it with a different grip tonight. The grip is the grip of a woman who printed her framework failure on paper and laid it on the floor and a woman she has been relying on for three months came in and stepped over the paper carefully and said sit down."

    "Zira stands at the desk edge for another beat."

    z "Noelle."

    n "Yes."

    z "The model is not the thing that killed Davel. The gap in the model is the thing that killed Davel. You did not put the gap there. The gap was the place where my information and your information had not met yet."

    z "Now they have met."

    n "Yes."

    z "Then the next model is the model we build together."

    n "Yes."

    "A beat."

    z "Good."

    "Zira leaves."

    "Aeron stays for another minute. He does not speak. He looks at Noelle at her desk with her datapad and her paper on the floor and the rebuilt model on the screen."

    a "The model is good, Noelle."

    n "The model is better. The model is not good yet. Good takes another two days."

    a "Then I will be here for the two days."

    n "Okay."

    "He leaves."

    "Noelle sits at her desk in the overhead light with the paper on the floor and the rebuilt model on the screen and the memory of Zira's hand next to her hand on the datapad surface. She does not turn off the overhead. She does not close the datapad."

    "She works."

    $ nudge_poly("zira_noelle_model_shared", delta=1)

    jump a4_s16a_door_data_state_updates

    # ========== PHASE 6 — AFTERCARE ==========

label a4_s16a_door_data_aftercare:

    "Later."

    "The desk lamp is the only light. The overhead is off. The paper on the floor is in the warm edge of the desk lamp's pool. The datapads are still on the desk — one showing the rebuilt model, one showing Zira's route diagram."

    "The three of them are on the floor of Noelle's workspace."

    "Noelle is against the desk leg — the same way Zira was against the bench leg in s15. Her back to the wood. Her hands in her lap. Zira is beside her, shoulder to shoulder, on Noelle's right side. Aeron is on Noelle's left side. Three bodies on the floor of a workspace that has paper on it."

    "Nobody has spoken for a while."

    "Noelle speaks first."

    "She speaks to Zira. Not to Aeron."

    n "You are not going to believe what I am about to do."

    z "I might."

    "Noelle reaches to the desk. She pulls the secondary datapad down to the floor. She opens a new file."

    "She begins typing."

    "Zira watches."

    z "You are documenting this."

    n "I am."

    z "You are logging what just happened."

    n "I am logging what just happened. I am logging the time stamp and the location and the fact that there were three people in this room and the fact that the model on the desk was the model we rebuilt together and the fact that what happened after the rebuild is a thing I do not have a classification for and I am going to log it as unclassified because unclassified is the most honest category I have."

    z "You are logging the three of us."

    n "I am logging the three of us."

    "Zira does not stop her."

    "Zira does not stop her because Zira understands that this is Noelle's version of the four-pulse Ashmarket tell — a private vocabulary, expressed in the only language the speaker trusts, offered in a room where the other person is the witness."

    z "It is the only language I trust."

    "She says it about Noelle's language. She says it as a woman recognizing another woman's language as legitimate."

    n "It is the only language I trust."

    "She says it about her own language. The repetition is not an echo. The repetition is a confirmation — the same sentence from two mouths meaning two different things and both meanings being true."

    z "Then I will trust it tonight."

    "A beat."

    "Noelle types for another thirty seconds. She saves the file. She sets the datapad on the floor between them."

    "Aeron has been quiet through the exchange. He has been watching two women find a shared grammar and the watching is the third form of intelligence in the room — not the statistical, not the physical, but the witnessing."

    athought "They are talking to each other."

    athought "They are talking to each other about the documentation and the documentation is not about me. The documentation is about them — about the thing they found on the floor of this workspace when the model stopped being the subject and they became the subject."

    athought "I am in the room. I was in the room for the thing they are documenting. But the documentation is theirs. The log entry is theirs. I am a variable in a model that two women are building together and the model is not mine to read unless they show it to me."

    "Noelle looks at Aeron."

    n "You can read it if you want."

    a "Do you want me to read it."

    n "I want you to know it exists. Whether you read it is your variable."

    "Aeron looks at the datapad on the floor between them. He does not pick it up."

    a "It exists. That is enough for tonight."

    "Noelle nods."

    "Zira's hand finds Noelle's hand on the floor. Not the datapad hand — the other hand, the free one, the hand that is not holding any language at all. She holds it the way she held the two-finger jeweler hold in s15 — light, precise, the touch of a woman who has been touching relay mechanisms for a decade and is now touching a person."

    "Noelle's other hand — the datapad hand — finds Aeron's hand on the floor on her other side. She holds it the way she held his hand in s18 — both hands on his chest transposed to one hand in his, the pressure of a woman who has stopped classifying the pressure."

    "Three people on the floor of a workspace. Paper around them. The desk lamp above them. The model on the desk. The log entry on the datapad between them."

    "Noelle closes her eyes."

    "Zira does not close her eyes. She looks at the model on the desk above them with the eyes of a woman who rebuilds things."

    "Aeron looks at the paper on the floor. Davel Ostra's name is not on the paper. Davel Ostra's name is in the fourteen percent. The fourteen percent is in the model. The model is on the desk. The model has been rebuilt."

    "The scene holds on the three of them on the floor."

    "Fade."

    $ nudge_poly("zira_noelle_aeron_triad", delta=1)

    jump a4_s16a_door_data_state_updates


    # ========== STATE UPDATES (CONVERGENCE) ==========

label a4_s16a_door_data_state_updates:

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Noelle", trust=1, attraction=1)
    $ rel_bump("Zira", trust=1, attraction=1)
    $ flag("zira_noelle_poly_recognized", True)
    $ flag("door_and_data_scene_complete", True)
    $ flag("noelle_framework_rebuilt_with_zira", True)
    $ canon_set("noelle_zira.working_rhythm", "statistical_plus_physical_intelligence")
    $ canon_set("noelle.documentation_language", "log_entry_as_private_vocabulary")
    $ npc_remember("Noelle", "said_i_do_not_know_what_to_do_with_that", weight=3)
    $ npc_remember("Zira", "said_then_stop_modeling", weight=3)
    $ npc_remember("Noelle", "logged_the_three_of_us_unclassified", weight=3)
    $ npc_remember("Zira", "said_then_i_will_trust_it_tonight", weight=3)
    $ npc_remember("Zira", "said_your_framework_just_got_a_runner_killed", weight=2)
    $ npc_remember("Noelle", "said_i_need_to_rebuild_it_with_you", weight=3)
    $ tp_seed("a4.zira_noelle.door_and_data")
    $ tp_seed("a4.poly.intelligence_as_intimacy")
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s16a_door_and_data_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Twenty-two forty the night of s16. Six hours after Davel Ostra.
#     Four hours after the vigil. Noelle has been in her workspace for
#     three hours. Zira arrives at twenty-two forty. Aeron arrives
#     approximately thirty-five minutes later.
# cann.what_happened:
#   - Noelle has printed the framework failure on paper and laid it on
#     the floor. The canal rendezvous model — fourteen percent chance of
#     interdiction — is the model that sent Davel Ostra to his death.
#   - Zira arrives without knocking. She says the sentence: "Your
#     framework just got a runner killed." Noelle: "I know. I need to
#     rebuild it. I need to rebuild it with you." Zira: "Then sit
#     down." They work the failure together for thirty-five minutes.
#   - The work changes shape: from Noelle walking Zira through the
#     model to two women building a new model together. Zira draws the
#     canal line-of-sight on Noelle's secondary datapad. Noelle watches
#     Zira draw and recognizes the shared grammar of precision.
#   - Aeron arrives, finds them working. The three of them rebuild the
#     model for an hour. At the end, the quiet in the room is the
#     quiet that has burned through the professional register.
#   - Noelle's thesis moment: "I am looking at two faces that are
#     reading me the way I read models. I do not know what to do with
#     that." Zira: "Then stop modeling."
#   - Poly gate: if metric("poly_pressure") >= 3, the scene escalates.
#     Consent gate: three choices (full / slow / sit). All three end
#     with the three of them in the workspace. Two lead to [INTIMATE
#     CONTENT HERE] blocks, one to a non-erotic hold on the floor
#     among the paper.
#   - If poly_pressure below threshold: the room is acknowledged but
#     not escalated. Noelle says "we should do this again." Zira
#     names the gap: "The gap was the place where my information and
#     your information had not met yet. Now they have met."
#   - Aftercare (escalated variants): Noelle logs the event on her
#     datapad. Zira: "You are documenting this." Noelle: "I am. It
#     is the only language I trust." Zira: "Then I will trust it
#     tonight." The documentation is Noelle's version of the four-
#     pulse Ashmarket tell — private vocabulary in the only language
#     the speaker trusts.
# cann.aeron_state:
#   - Second time in Act IV that arriving at a room and finding two
#     women already working has given rather than cost him something.
#     The geometry of being the third variable in a model that two
#     women are building together. His role is witnessing, not leading.
# cann.noelle_state:
#   - Post-s18. The datapad is back in her hand but the grip is
#     different. The model failure is the catalyst for a new form:
#     the model that includes Zira's physical intelligence. "I need
#     to rebuild it with you" is her Act 4 poly thesis sentence.
#   - "I do not know what to do with that" is the poly-gate line —
#     the moment her analytic register fails and the failure is the
#     opening. Cross-reference with "I have no unit for this" from
#     Act 3 and "want is a framework" from s18.
#   - The log entry is her version of the Ashmarket tell — private
#     vocabulary in the only language she trusts. "Unclassified" is
#     the most honest category she has.
# cann.zira_state:
#   - Post-s15. The clock is behind her. The workshop floor is behind
#     her. She is in operational mode in Noelle's workspace and the
#     operational mode has absorbed the s15 recalibration.
#   - "Then stop modeling" is the Ashmarket directive — two words that
#     function as a door. Cross-reference with "sit down" at the
#     scene opening and "Then sit down" from s15.
#   - "Then I will trust it tonight" is the aftercare thesis. She is
#     trusting Noelle's documentation language the way Aeron trusted
#     the clock — by not asking it to be a language she already knows.
# cann.thematic_flags:
#   - Act 4 EMP arm: intelligence as intimacy. The scene is structured
#     so the work IS the connection — the rebuild of the model is the
#     register in which the poly dynamic emerges.
#   - The paper on the floor = the failure made physical. The three of
#     them sitting among the paper in the aftercare = three people who
#     have agreed to sit with the failure rather than above it.
#   - Noelle's documentation and Zira's route-drawing = two forms of
#     precision aimed at the same problem. The datapads with both
#     women's work on the same screen = visual thesis of the poly
#     configuration (cf. the relay map with two handwritings in s14a).
