# =======================================================
# ACT 4 - Scene 16: Rhea Strikes (Empathy Path)
# File: a4_s16_rhea_strikes_emp.rpy
# Type: OPERATION / MARCUS-CLOCK HIT — first Rhea Vestin cut
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s16_rhea_strikes_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s16_rhea_strikes_emp:
    $ show_timeline("34th of Forge, 390 A.C.", "04:00", "Phoenix Secondary Base — Ops Wing")


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("rhea_vestin", to_stage=2, source="a4_s16_rhea_strikes_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Six movements. The scene has three rooms and three cameras.
    #         ROOM A — the ops wing at oh-six-twelve.
    #         (1) Open on the ops table from a low angle, almost floor-level,
    #             looking up at the underside of the holo-table's green wash.
    #             A single alert tick goes from one ping a minute to two pings
    #             a minute to four pings a minute in the thirty-second interval
    #             at the top of the scene. Lyra is at the table. Only Lyra.
    #             The rest of the ops wing is in fourth-shift skeleton
    #             configuration — two analysts at the back bench, Noelle's
    #             pad on the main table face-down where she left it four hours
    #             ago when she went to lie down in the analyst alcove for the
    #             first time in six days.
    #         (2) Medium on Lyra's face as the alert tick goes to four. She
    #             is the one at the table because Lyra has pulled the early
    #             shift this rotation. Her face does the small thing it does
    #             when the signal she is reading is not consistent with any
    #             signal she has read before. The camera does not push. Lyra
    #             at the table is the calmest body in the room.
    #         (3) Tracking shot of Aeron arriving. Not at the pace of s14 and
    #             not at the pace of s13. At the pace of a man who was woken
    #             up in the medbay alcove by a runner whose message was
    #             routed through three people in the middle of the night and
    #             arrived at his face without anybody trying to soften it.
    #             He comes into the ops wing and goes directly to the side
    #             chair from s14 — the chair is an established posture now,
    #             one night in, and the body goes to it before he thinks
    #             about going to it. The camera notices the automatic nature
    #             of the choice.
    #         ROOM B — a glimpse of an Echelon intercept window.
    #         (4) Cut, briefly, to a tight shot of an intercepted Echelon
    #             back-channel transcript on Noelle's screen. One sender. One
    #             recipient. Five lines of text. The text is attached to a
    #             scrubbed signal metadata header that identifies the source
    #             as a Western Industrial Theater relay that Marcus uses for
    #             command-chain communications. The transcript is the only
    #             visual of Marcus in the scene. He is a signal, not a body.
    #             Hold on the transcript long enough for the player to read
    #             it and then cut back to the ops wing.
    #         ROOM C — the ops wing again, once Noelle has been pulled up.
    #         (5) Wide of the ops table. Aeron at the side chair. Lyra at
    #             her position. Zira at the foot — Zira came up from the
    #             relay alcove when the alert went to four. Noelle entering
    #             from the analyst alcove, hair flat on one side, the two
    #             hours of sleep visible in her face. Selene is not in the
    #             scene. Selene is at the secondary base perimeter running
    #             a Rhea-contingency perimeter sweep that Zira drafted at
    #             the end of s15's aftercare, which means Selene is on
    #             comms but not at the table. The room is the younger four
    #             of the five-chair geometry.
    #         (6) The sustained close on Noelle through the middle third of
    #             the scene as she reads Rhea's cut and finds the shape.
    #             Then the pull back to the wide when she reaches the
    #             conclusion about her own framework. Close again on
    #             Aeron's response. Cut to Noelle when she asks for six
    #             hours. Cut to Aeron when he answers with twelve. Then
    #             the scene fades on the ops table with all four working
    #             chairs still running and the empty head chair still
    #             functioning as a working surface from s14.
    # LIGHTING: Ops wing at early morning. Fourth-shift ambient. Overhead
    #           strips are on half-rotation — the room saves power on the
    #           fourth shift and the lighting is cooler than the day shift
    #           by a clean degree or two. The holo-table's green wash is
    #           the warmest light in the room. Noelle comes in from the
    #           analyst alcove with hallway lighting on her face and the
    #           change in temperature when she crosses the threshold is
    #           visible in the frame.
    # SFX: Ops ambient at fourth-shift volume — tactical tick, comms relay
    #      subdued, the low hum of the overhead strips. The alert tick
    #      starts at one ping a minute and escalates. A runner's boots in
    #      the corridor when Aeron is fetched. The soft close of the ops
    #      wing door. Comms chatter from Selene's channel at low volume.
    #      No music bed until the Noelle realization — one low held
    #      string enters under her and holds through Aeron's twelve-hour
    #      answer. Drops at the fade.
    # FX/COMP: THE HOLO-TABLE. A tactical display layer showing the
    #          Western Industrial Theater corridor where Rhea's cut
    #          occurred. A single red mark where a Phoenix asset has gone
    #          off the board. The asset's call sign reads initially as a
    #          number. The number resolves, as the scene proceeds, into a
    #          name — Davel Ostra, senior runner, third-ring logistics.
    #          Davel Ostra is unnamed on-page before this scene. Davel
    #          Ostra stays unseen. Davel Ostra is a red mark going grey.
    #          THE INTERCEPT. Noelle's screen. Five lines of text from an
    #          Echelon back-channel, one sender, one recipient, identified
    #          by metadata as Rhea Vestin's operational command. The
    #          transcript is not decrypted cleanly — parts are redacted,
    #          parts are plaintext. The plaintext lines are what the
    #          scene needs the player to see.
    #          THE EMPTY HEAD CHAIR. Still with a face-down working pad
    #          on its arm. Nobody has moved the pad. Nobody has moved the
    #          chair. The chair is the same chair it was at the end of
    #          s14 — a surface, not a throne.
    # BLOCKING: Lyra at the ops table, position from s13. Aeron arrives
    #           from the corridor, crosses to the side chair three down
    #           from the head-adjacent position Selene would be in if
    #           Selene were here. Sits. Hands on arms of chair. Zira
    #           arrives from the corridor — from the workshop side, not
    #           from the comm alcove, and Aeron notes which direction she
    #           came from and does not react. Noelle arrives from the
    #           analyst alcove. Selene is absent — on comms. The four in
    #           the room for the bulk of the scene are Aeron, Lyra,
    #           Noelle, and Zira. Noelle takes the station beside her own
    #           pad. She reads the alert. She reads the intercept. She
    #           turns toward the table halfway through, pen down, and
    #           stops.
    # FACE: Lyra — calm at the table, the Marcus-clock being hit is the
    #       kind of event Lyra's body was built to metabolize. Zira —
    #       came up from the workshop, does not want to be here tonight
    #       but is here tonight. Noelle — she will go from analytic
    #       focus to a specific private collapse and back again, in the
    #       span of four minutes, and the scene is going to watch her
    #       make the return trip. Aeron — the s14 posture holds. The
    #       posture is not being tested by his own hands tonight. The
    #       posture is being tested by the question of whether he will
    #       protect Noelle's framework against the version of Noelle
    #       that has just realized the framework is a vulnerability.

    # ========= VOICE BASELINE =========
    # EMP cadence. Four speakers in the ops wing. Selene on comms only —
    # appears briefly at the top of the scene as (sel offscreen) and at
    # the end as the comms line closes. Marcus appears only as the
    # intercept transcript, five lines, voice tagged m. No Marcus dialogue
    # in the ops wing — he is a signal. Noelle drives the scene's middle
    # third. Aeron speaks sparingly; his line count is under a dozen. The
    # scene is a Noelle beat more than a Rhea beat — the cut is the
    # occasion, the framework is the subject.

    # scene bg_ops_wing_table_predawn with dissolve
    # play ambient "sfx/ambient/ops_wing_fourth_shift.ogg" fadein 2.0

    # ========== PHASE 1 — THE ALERT ==========

    # CAMERA: ROOM A — ops wing at oh-four-hundred. Open
    #         on the ops table from a LOW angle, almost
    #         floor-level, looking up at the underside of
    #         the holo-table's green wash. Lyra is the
    #         only one at the table. The rest of the ops
    #         wing is in fourth-shift skeleton — two
    #         analysts at the back bench, Noelle's pad
    #         face-down where she left it. Hold the low
    #         angle for the alert tick escalation.
    # SFX: the alert tick is the scene's opening audio
    #      event. One ping per minute to two to four
    #      within a thirty-second interval at the top of
    #      the scene. Mark each tick. The rising cadence
    #      is the beat.

    # CAMERA: open on the ops table from a LOW angle,
    #         almost floor-level, looking up at the
    #         underside of the holo-table's green wash.
    #         Unusual framing for this room. Lyra is at
    #         the table; only Lyra. The alert tick is
    #         audible — one ping a minute, then two,
    #         then four in the thirty-second interval at
    #         the top of the scene. Hold the low angle.
    # SFX: the alert tick is the scene's opening rhythm.
    #      Distinct, dry, machine-bright. Mark each
    #      acceleration step. The accelerating tick is
    #      the first Marcus-clock hit of Act 4 made
    #      audible.
    # FACE: Lyra — the calmest body in the room reading
    #        a signal that is not consistent with any
    #        signal she has read before. The face does
    #        its small thing. The camera does not push.

    "Oh-six-twelve. The morning after the workshop scene. Six days and eleven hours after Marcus signed the Rhea Vestin dispatch in a4_s07."

    "The ops wing is in its fourth-shift skeleton configuration. Two analysts at the back bench are running a Ghostline relay sweep on the eastern corridor. The ops table is in a low-power reading mode — the holo-table at half-depth, the alert bed running at one ping a minute, the way it runs when the night is quiet and the quiet is the kind of quiet that gets reported as 'routine' at the oh-seven-hundred."

    "Lyra is at the table."

    "Lyra is at the table because Lyra pulled the early shift this rotation and because somebody has to be at the table at oh-six-twelve and Lyra's rotation turn was the rotation turn. That is the only reason. There is no Lyra-specific reason for Lyra to be the one who is at the table when the Marcus clock hits. Lyra has a different relationship to coincidence than some of the other Phoenix command staff and the coincidence does not land on her as ominous. Coincidence is the register the shift runs in."

    "She is reading the eastern corridor layer with a cup of tea at her elbow. Her note-pad is out but the pen is capped."

    "At oh-six-twelve and thirty-nine seconds, the alert tick goes from one ping a minute to two pings a minute."

    "Lyra registers the change. Uncap the pen. Does not write yet. Watches."

    "At oh-six-thirteen and twelve seconds, the alert tick goes from two pings a minute to four pings a minute. That is an escalation rate that is not consistent with a routine signal-quality change and is not consistent with a patrol-refresh event. It is consistent with a developing incident."

    "Lyra writes a single line in the note-pad. The line is not a tactical note — it is a timestamp, which is the note-protocol for Lyra's shift when she does not know yet whether she is reading an event worth a tactical note."

    "At oh-six-thirteen and forty-one seconds, the alert tick goes to six pings a minute and the ops wing's incident bell goes off. The bell is not the emergency alarm. The bell is the incident bell. The distinction matters because the incident bell is the one that tells the shift there is a developing situation; the emergency alarm is the one that tells the shift there is a situation that has already developed past the point of containment."

    "Lyra touches the comms relay."

    l "Lyra at ops table, fourth shift. Incident bell on the Western Industrial Theater layer. Escalating tick. Need Aeron, Noelle, and a Ghostline reader at the table. Tessa in medbay can stay in medbay. Selene on comms — Selene, where are you."

    "A beat on the comms. Selene's voice comes back, low and tight — she is in the field, not the war room. She is on the Rhea-contingency perimeter sweep that Zira drafted at the aftercare end of s15."

    sel "Selene, secondary base perimeter, sector three. Rhea-contingency sweep. Hearing you, Lyra. What is on the layer."

    l "Cannot say yet. Reading signal metadata. Stay on comms."

    sel "Holding."

    "Lyra reads the signal metadata for six seconds. Then she says one more line into the relay."

    l "Make that a Ghostline reader and Zira. I want Zira at the table for this one."

    # ========== PHASE 2 — AERON ARRIVES ==========

    # CAMERA: tracking shot of Aeron arriving. Not at the
    #         pace of s14 and not at the pace of s13. The
    #         pace of a man WOKEN by a runner whose
    #         message was not softened. He comes into the
    #         ops wing and goes directly to the side chair
    #         from s14. The chair is an established posture
    #         now — one night in — and the body goes to it
    #         automatically. The camera NOTICES the
    #         automatic nature of the choice and holds on
    #         the sit for a beat.
    # FACE: Aeron — the pre-coffee face of a man who has
    #        been dragged out of the medbay alcove at four
    #        in the morning. Not commanding. Receiving.
    #        The side chair is already his register.

    # CAMERA: tracking shot of Aeron arriving. Not at the
    #         pace of s14, not at the pace of s13. At the
    #         pace of a man who was woken up by a runner
    #         whose message arrived at his face without
    #         anybody trying to soften it. He comes into
    #         the ops wing and goes directly to the side
    #         chair from s14 — the chair is an established
    #         posture now, one night in. The camera
    #         NOTICES the automatic nature of the choice.
    #         Catch the automatic beat and do not italicize.

    "Aeron was asleep in the analyst alcove's auxiliary cot — not the one Noelle collapsed on, the one beside it — because the analyst alcove is the nearest sleeping surface to the ops wing and because Tessa told him at the end of s15's night to sleep where the ops wing could reach him. He had not taken the instruction until the workshop ended at oh-two-forty. He had taken it after."

    "The runner reaches the cot at oh-six-fourteen and nineteen seconds. The runner does not soften the message."

    "Aeron is on his feet inside ten seconds of waking up. He is at the ops wing door inside thirty seconds of waking up. He does not stop at the threshold."

    "He walks into the ops wing and his body goes directly to the side chair."

    athought "My body went to the side chair. My body did not check with me."

    athought "That is one day of side-chair geometry and the body is already beginning to default to it. The development-of-the-posture is happening on the timeline Tessa predicted — the muscle is learning faster than the mind. The mind will be the one that has to catch up to the body, not the other way around."

    athought "Good. That is the timeline I want."

    "He sits. Hands on the arms of the chair. He does not reach for a tactical layer."

    a "Lyra. Report."

    l "Incident bell on the Western Industrial Theater layer. Signal metadata consistent with a Phoenix asset going off the board at zero-five-fifty-seven. Asset identifier is still resolving. I am not going to name the asset until the resolution hits the second confirmation, because the first confirmation is reading single-point and the single-point could be a faulty relay in the western corridor that we have been watching for three weeks."

    a "What is the likelihood it is the faulty relay."

    l "Under ten percent. I am giving you the ten percent because I want you to know the ten percent exists. It is not the faulty relay. The signal shape is wrong for the faulty relay. The faulty relay misfires as a clean signal drop. This is a dirty signal drop with four follow-on signatures in the surrounding layer."

    a "Four follow-on signatures."

    l "Yes. I am reading them as Echelon operational cleanup — a team on the ground confirming the asset status, clearing the engagement, and moving out of the footprint in under three minutes. That is not patrol cadence. That is a surgical team cadence."

    "A beat."

    l "That is a Rhea Vestin cadence."

    "The sentence drops. Lyra does not inflect it. Lyra is not dramatic. Lyra is naming the shape because the shape needs a name and the name on the ledger is Rhea Vestin because Selene and Aeron and Zira have been working a Rhea-contingency protocol since s07 and Lyra has been trained on the protocol for two days now and the shape matches the protocol's predicted signature."

    athought "Rhea arrived."

    athought "The six-day clock hit. Marcus signed the dispatch in the Aeries spire six days and eleven hours ago and Rhea has had enough time to read the terrain and enough time to make her first cut. The cut is on the table. The asset is off the board."

    athought "I do not know who the asset is yet."

    athought "I am going to know in a minute."

    # ========== PHASE 3 — ZIRA ARRIVES ==========

    "Zira comes through the ops wing door at oh-six-sixteen. She is in the workshop jacket she was wearing four hours ago and the workshop jacket is unmistakable — the sleeves have the particular wear of the forge corner. She has come up directly from the workshop. Aeron notes the direction and does not react. The direction is its own private thing and the scene they are in is not a private thing."

    z "Lyra."

    l "Zira. Western theater incident. Signal drop with Rhea cadence. Take the Ghostline layer."

    "Zira crosses to the ops table. She takes the position at the foot — her s13 position, her s14 position, the position at the foot that has become hers by repetition and now by protocol. She opens the Ghostline layer on the holo-table and begins reading."

    "Her hands move fast. The workshop is not in her hands anymore. The operational mode is in her hands. The switch from one mode to the other is a one-second transition for Zira and has been for years — it is the thing that makes her a Phoenix asset at all."

    z "I have a back-channel confirmation from the Ghostline western relay at oh-five-fifty-eight — one-minute lag on the incident. A name is coming through on the relay."

    "A beat. Zira reads the relay. Her hand pauses above the layer."

    z "Davel Ostra."

    "She says the name flat."

    z "Senior runner, third-ring logistics, western industrial corridor. He was the runner who ran the mid-corridor Ghostline relay for the second pass of Noelle's Phase II distribution framework two weeks ago. He has been running the western logistics line for eleven months. He is — he was — the primary human node between the central Phoenix command structure and the western industrial cell."

    "A beat."

    z "I have not briefed Noelle on Davel Ostra by name. He has been a call-sign in her framework — DO-7. DO-7 is a node identifier she has been building predictive-behavior models around for six days."

    athought "DO-7 is Davel Ostra. Noelle does not know that yet. Noelle is in the analyst alcove and she has been running a predictive-behavior model on a call-sign for six days and the call-sign is a man who went off the board forty-five minutes ago."

    athought "Noelle is going to find out the call-sign is a man in the next two minutes. Somebody has to go get her. Somebody has to go get her carefully."

    a "Lyra."

    l "Yes."

    a "Go get Noelle. Bring her up. Do not tell her what the incident is in the corridor. Let her find the layer at the table. The finding is going to matter more than the telling."

    l "Understood."

    "Lyra stands from the table and crosses to the analyst alcove door. Her pace is the measured pace she uses when she is going to wake somebody up carefully. Aeron watches her go."

    athought "Lyra is the right person to wake Noelle up. Lyra is the person whose hand on your shoulder when you are asleep is a hand you wake up trusting. Lyra's entire presence at Phoenix is the presence of a person whose hand on your shoulder at oh-six-seventeen is a safe hand. I am not underselling the specific skill by naming it. The skill is load-bearing for what is about to happen to Noelle."

    # ========== PHASE 4 — THE INTERCEPT ==========

    # CAMERA: ROOM B. Hard cut to a tight shot of an
    #         intercepted Echelon back-channel transcript
    #         on Noelle's screen. One sender. One
    #         recipient. Five lines of text. Attached to
    #         a scrubbed signal metadata header identifying
    #         source as a Western Industrial Theater relay
    #         Marcus uses for command-chain comms. The
    #         transcript is the ONLY visual of Marcus in
    #         the scene. He is a signal, not a body. Hold
    #         on the transcript long enough for the player
    #         to read it — every line legible. Then hard
    #         cut back to Room A.
    # FX/COMP: the transcript on the screen must be
    #          rendered as legible text, not placeholder
    #          lorem. The five lines are load-bearing.
    #          The metadata header frames them as
    #          authentic Marcus.

    # CAMERA: HARD CUT to a tight shot of an intercepted
    #         Echelon back-channel transcript on Noelle's
    #         screen. The only visual of Marcus in the
    #         scene — he is a SIGNAL, not a body. Hold
    #         the transcript long enough for the player
    #         to read the five lines. Do not animate the
    #         scroll. Static shot. Institutional typeface.
    #         The header identifies the source as a
    #         Western Industrial Theater relay. That
    #         theater name is the single most important
    #         piece of information in the scene and the
    #         camera gives it the static hold it needs.
    # SFX: cut the ops ambient to near-silence during the
    #      transcript read. The room holds its breath.
    #      One digital tick marks the header coming up.
    #      Then the ambient returns at half.

    "While Lyra is in the analyst alcove, the Ghostline layer on the holo-table pulls up a second signal."

    "It is not a Phoenix signal. It is an Echelon back-channel intercept — the kind of thing Zira's relays pick up maybe three times a month, when an Echelon commander uses a back-channel that Phoenix has partially mapped. The intercept resolves into plaintext inside thirty seconds. Five lines of text. One sender, one recipient."

    "Zira reads it."

    "Zira's face does the small thing it does when she is reading a piece of text that is about her work."

    z "Aeron."

    a "Show me."

    "She slides the intercept panel across the holo-table. Aeron reads it at his side chair. The transcript is tagged to an Echelon back-channel metadata header identifying the sender as the Western Industrial Theater command relay — the relay Marcus uses for command-chain communications with field commanders. The sender is tagged m for the command encryption signature. The recipient is tagged rv — Rhea Vestin's operational command."

    "Five lines. Three of them are plaintext. Two are redacted — not because Zira failed to decrypt them, because Marcus's tier is high enough that parts of his back-channel are running on a key Phoenix has never held."

    "The three plaintext lines read as follows."

    m "First cut clean. Node DO-7 off the board per the pattern we discussed. Congratulations on the shape of it."

    m "Pattern-matching on the subject's framework is holding. The next three cuts will read the framework's second and third derivatives at rates of two, four, and eight. Maintain the cadence you set today. Maintain the geometry."

    m "The subject is going to know inside the hour that the cut was shaped around her own work. I want her to know. That is part of the shape."

    "Silence in the ops wing for a beat."

    athought "The subject is Noelle."

    athought "Marcus signed a dispatch to Rhea Vestin that names Noelle as 'the subject' and tells Rhea that the cut was shaped around Noelle's framework and that he wants Noelle to know it was shaped around her framework. He wants Noelle to know inside the hour. The intercept is the hour. The intercept is a thing Marcus wanted us to pick up."

    athought "Marcus has acquired a specialist who studies how Phoenix thinks and cuts at the seams. The specialist is Rhea and the cuts are going to come at rates of two, four, and eight — two in the next cut, four in the one after, eight in the one after that. That is not a random escalation. That is a mathematical shape being fit to Noelle's framework's own derivatives. Marcus is using Noelle's predictive framework as the target template for Rhea's cadence. Noelle's framework has become a vulnerability Marcus can pattern-match against."

    athought "Noelle does not know this yet. Noelle is on her way up the corridor with Lyra. Noelle is going to walk into this room and look at the Ghostline layer and see a node-identifier she has been building a model around go grey on the board and she is going to see her own work turned into a target template in the same minute."

    athought "I am not going to hide the intercept from her. Hiding it would be the version of protecting-her that Tessa and Zira and Selene have collectively trained me out of for six weeks now. I am going to let her see it and I am going to let her have the minute of it and I am going to be in the room while she has the minute."

    a "Zira. Leave the intercept open on the layer. Noelle is going to need to see it when she gets to the table."

    z "Leaving it open."

    a "And close the other three Ghostline subwindows. Give her a clean read. I do not want her navigating the layer while she is reading this."

    z "Closing them."

    "Zira closes the subwindows. The holo-table now has two elements on its western theater layer: the red mark where Davel Ostra went off the board, and the intercept panel with the three plaintext lines from Marcus."

    "The geometry is as clean as Zira can make it."

    # ========== PHASE 5 — NOELLE ARRIVES ==========

    "Lyra and Noelle come through the ops wing door at oh-six-eighteen and thirty seconds."

    "Noelle's hair is flat on one side from the cot. Her analyst jacket is on. Her eyes are the eyes of a person who has had two hours of sleep in the first stretch of rest she has had in six days and who knows that the two hours was a gift and knows that the gift has just been taken back by the incident bell she heard through the alcove wall while Lyra was waking her up."

    "She does not ask what the incident is while she walks to the table. She has been trained not to ask while she walks. The asking is for when she gets to the layer."

    "She gets to the layer."

    "She takes her station — her standing position at Selene's left, except Selene is not here, so she takes the standing position alone at the head-adjacent side of the table. She looks down at the Western Industrial Theater layer."

    "She reads the red mark first. Then the intercept panel."

    "The reading takes her about eighteen seconds."

    "She reads the red mark's resolution identifier. She reads the call-sign. DO-7. She looks at the call-sign for a beat. She looks at the intercept. She reads the three plaintext lines. She reads them again. She reads them a third time."

    "Her hand goes to the edge of the table. Flat palm. The palm-press is the thing her hand does when she is holding a body on the floor. The flatness is a way of not making a fist."

    "She does not speak for another beat."

    n "DO-7 is Davel Ostra."

    "She says it not as a question. She says it as a confirmation she is delivering to the room. She is telling the room what the room already knows in case anyone in the room has missed it."

    z "Davel Ostra. Senior runner. Western industrial corridor. Confirmed off the board at zero-five-fifty-seven."

    n "I have a file on DO-7. I have had a file on DO-7 for six days. I built a predictive-behavior model on DO-7 four days ago. The model was clean — he was running a stable pattern in the western corridor and I was using his movement cadence as a calibration baseline for three other nodes in the same ring. His pattern was load-bearing in my framework for the entire third-ring logistics layer."

    "She stops."

    "She reads the three plaintext lines again."

    n "Marcus says the cut was shaped around my framework."

    "She says it flat."

    n "He says the next three cuts will come at rates of two, four, and eight. Those are my framework's second and third derivatives read as escalation coefficients. Marcus is fitting Rhea's cadence to my predictive model's rate-of-change curves."

    "Another beat."

    n "My framework is the target template."

    "She looks up from the table. Not at Aeron. At the ceiling of the ops wing — a one-second upward glance that is not a plea to anything and is not a prayer in the Lyra register. It is the glance of an analyst whose body has to do a small thing so that her mind can do the next thing. The glance is her version of Zira's three-pulse tell. Nobody at the table performs the glance back. Lyra sees it. Zira sees it. Aeron sees it. Nobody says anything."

    "Noelle's eyes come back to the table."

    nthought "My framework is the target template. My framework — the thing I signed my hand onto at Batch A, the thing I spent eight weeks building with the specific aim of protecting this rebellion's decision-making infrastructure from exactly the kind of cadence-acceleration attack Marcus is now running against it — is the tool Marcus is using to target the attack."

    nthought "The framework is a map. Any map is a target if the wrong person reads it. I built the map with a protection protocol and the protocol includes a self-invalidation clause — the framework was supposed to rotate its predictive parameters every seventy-two hours to prevent exactly this — and the rotation has not happened because the framework has not been up for seventy-two hours yet. It has been up for ninety-six hours on the Batch A version and the Batch A version is what Rhea is reading. The Batch A version is what Rhea is reading because I signed it and placed it on the ops table in s13 and it has been the room's operating framework for ninety-six hours without me re-signing it or rotating it because I have been running an ops-wing shift for that whole time and I have not had the four hours I would need to rotate the parameters."

    nthought "The ninety-six hours was exactly the window Marcus needed. Rhea read the framework off the Batch A signature and fit her cadence to it."

    nthought "Six days of work on my framework is the thing Rhea used to target Davel Ostra."

    nthought "I built Davel Ostra's kill template with my own hand four days ago."

    "Her palm on the table edge presses harder. The press is the press she is doing instead of allowing the body to do a different, louder thing."

    "She does not speak for three seconds."

    "Then she does."

    n "I need to take the framework down."

    # ========== PHASE 6 — THE QUESTION ==========

    # CAMERA: pull back to a wide three-shot of the ops
    #         table. Lyra, Noelle, Aeron. Zira has also
    #         arrived by this point. Four-shot. The
    #         composition is crowded because the table is
    #         the only lit surface in the room and
    #         everyone who matters is pulling toward it.
    #         Do NOT cut to singles for the question. Hold
    #         the wide. The frame is reading the shape of
    #         a decision that is already being made by the
    #         four of them together and is not going to be
    #         a commander's call.

    "The sentence lands on the table."

    "Aeron does not move."

    athought "She said she needs to take the framework down."

    athought "This is the decision point. The decision point is whether I overrule her. The decision point is whether I dismiss the framework. The decision point is whether I — the commander of this rebellion, who has just spent one and a half days developing the posture of not-overruling and not-dismissing — will hold the posture when the posture is being tested by a question I do not have an answer to."

    athought "I do not have an answer to whether the framework should come down. I do not have the analytic capacity to make that decision on my own. Noelle has the analytic capacity and Noelle is the one asking the question, which means the question is not actually 'should the framework come down.' The question is what I do in the next ninety seconds."

    athought "What I do in the next ninety seconds is: I do not overrule her and I do not dismiss the framework and I ask her what the next version looks like."

    athought "That is the posture. That is the thing I decided yesterday at the side chair and the thing I am deciding again tonight with Noelle asking me to take a tool off the table that I need on the table to fight Rhea Vestin."

    athought "I am going to trust the posture."

    "He speaks."

    a "Noelle."

    n "Aeron."

    a "I am not going to overrule you on the framework. I am not going to dismiss the framework. Either of those moves would be the wrong move for a reason I can say out loud if you need me to and I do not think you need me to."

    "A beat."

    a "What does the next version look like."

    "The question is asked at the working volume of a side chair. It is not the command volume. It is the volume of a peer at the table asking a peer at the table a question the peer is the only person in the building qualified to answer."

    "Noelle looks at him."

    "The look is the Noelle look — the one that runs a sub-second scan on the room to make sure the room she is reading is the room she is in. The scan confirms the room. The room is the room. The question is the question."

    "Noelle does not have the answer."

    "Noelle is not going to pretend she has the answer."

    n "I do not have an answer to that yet."

    a "Okay."

    n "I do not have an answer because the framework was built on a ninety-six-hour rotation assumption that Rhea has just invalidated. The next version has to be built on a rotation assumption that treats Rhea's cadence as a moving target that adapts to the framework's own derivatives. That is a harder math problem than the one I solved for the Batch A version. I have not solved it before. I am not sure I can solve it in less than — "

    "She stops. She is doing the math on the time estimate in her head. The math is visible in the angle of her jaw."

    n "I need six hours."

    "She says it as a request. Not as a demand. The request is sized to the actual problem and sized to the operational tempo the room is running in and sized to the grief she is going to have to metabolize in parallel with the math. The sizing is Noelle's best honest estimate."

    "Aeron does not overrule the estimate."

    "He does not accept the estimate either."

    a "Take twelve."

    "Two words. He says them flat."

    "A beat."

    n "Twelve."

    a "Twelve. I am not going to let you do a math problem this size in six hours after you have had two hours of sleep in six days and after you have just found out that Davel Ostra's kill template was built with your hand. You are going to take twelve and you are going to take the first four of them in the analyst alcove cot you just came off of and you are going to take the next eight of them at the framework once you have eaten and once Tessa has looked at you."

    "A beat."

    a "The Rhea clock is running at rates of two, four, and eight according to the intercept. We have enough window on the two-rate cut to absorb a twelve-hour framework pause. We do not have enough window on the four-rate cut to absorb a six-hour framework pause that turns into a twenty-hour framework pause because you collapsed halfway through the six. Twelve with sleep is faster than six without."

    "Another beat."

    a "I am not overruling you on the framework. I am overruling you on the sleep estimate. That is a different overrule and I am going to make it explicit because I do not want to hide behind the word."

    "Noelle is looking at him. Her palm is still flat on the table edge."

    nthought "He overruled my sleep estimate and he named it. He did not overrule the framework. He did not dismiss the framework. He asked me what the next version looks like and I told him I did not know and he held the not-knowing in the room without flinching. And then he overruled my sleep estimate because the sleep estimate was a thing I was sizing wrong in the direction of not taking care of myself, and he named the overrule as an overrule, and he gave me twelve hours with the twelve-hour reasoning laid out."

    nthought "I can work with twelve hours."

    nthought "I cannot work with six."

    nthought "He was right about the collapse math and I am grateful he was."

    n "Twelve."

    a "Twelve."

    n "I will take the first four in the alcove. I will come back at the table at ten-eighteen with a v0.5 draft."

    a "Ten-eighteen."

    # ========== PHASE 7 — THE SECOND DECISION ==========

    "Aeron turns to Zira."

    a "Zira. While Noelle is at the framework, we need to hold the western industrial theater layer with the Batch A version running. Rhea is going to make the two-rate cut inside the next twelve to eighteen hours and I do not want her to make it without us having a pre-positioned response on the board. Can the Batch A framework run for twelve more hours as a static defense without rotation?"

    z "It can run as a static defense. It cannot run as a predictive defense. The predictive side of the framework is what Rhea is pattern-matching against. The static side of the framework is the tactical-layer baseline and the baseline is still good for twelve hours. I can hold the static side from the foot of the table while Noelle rebuilds the predictive side."

    a "Hold it."

    z "Holding."

    a "Lyra."

    l "Aeron."

    a "Run the western industrial theater medical rotation backup for the next twelve hours. If Rhea makes a second cut inside the window, the medical side needs to be pre-staged. I want the backup rotation running without Tessa having to be woken up. Can you do that from your station at the table?"

    l "I can. I will draft the backup rotation at the table and co-sign it with Tessa at oh-eight-hundred when she comes on shift. That keeps the backup running and keeps Tessa's sleep intact."

    a "Thank you."

    "Aeron turns to the comms."

    a "Selene on comms. Did you get the intercept."

    sel "Got it. Reading now."

    a "The Rhea-contingency perimeter sweep — hold it at its current cadence. Do not accelerate. If Rhea has modeled us to accelerate under pressure, the acceleration is a thing she will have priced in. Hold the cadence Zira drafted last night. Do not give Rhea a new rate."

    sel "Holding cadence."

    a "Come off the sweep at oh-eight-hundred and come to the table. We are going to have a full-table meeting at oh-eight-thirty. Bring Tessa. Bring the eastern corridor analyst. We are going to reset the working assumptions on the framework in the presence of the five of us plus the two additionals. We are not going to reset the framework yet — that is Noelle's work in the alcove — but we are going to reset the working assumptions the framework has been operating under."

    sel "Oh-eight-thirty. Full table. Bringing Tessa and the eastern corridor analyst."

    a "Comms closed."

    "The comms click off."

    # ========== PHASE 8 — THE SIDE CHAIR HOLDS ==========

    # CAMERA: final composition of the scene. Wide on the
    #         ops table. The four women and Aeron are at
    #         the table. Aeron is still in the side chair.
    #         He has not moved to the head chair. The head
    #         chair is still empty — the datapad face-down
    #         on its arm has been moved (someone picked it
    #         up during the scene) but the chair itself is
    #         still empty. Hold the wide. Fade on the
    #         five-at-the-table composition with the empty
    #         head chair at the end of the frame.
    # FX/COMP: the side chair holding is the scene's
    #          thesis. Even in a crisis, the shape that
    #          was set up in s13 and reinforced in s14
    #          holds. Command geometry can survive a
    #          Marcus strike.

    "Aeron's hands have been on the arms of the side chair the entire scene."

    "He has not moved them. He has not reached for a tactical layer. He has asked questions, issued two small holds, and overruled a sleep estimate. That is the whole span of his command action in the scene."

    "The scene is the scene his s14 posture was being tested by, and the posture has held."

    athought "The posture held. The test was not what I was expecting. I was expecting the test to be whether I could sit in the side chair while Selene ran the table. The test was whether I could sit in the side chair while Noelle's framework — the framework I signed off on at Batch A and let run for ninety-six hours without re-signing — became the vulnerability Rhea is pattern-matching against. The test was whether I would overrule Noelle on the framework because the framework had become dangerous."

    athought "I did not overrule her on the framework. I overruled her on her sleep estimate. That is a different overrule and it is the correct overrule. The correct overrule is the overrule that takes care of the analyst and leaves the analytic work in the analyst's hands."

    athought "That is the posture. That is the thing Selene tried to teach me in a4_s10 and a4_s02 and a4_s12a. That is the thing Tessa tried to teach me in a4_s05a and a4_s12. That is the thing Zira asked me to see in a4_s09a. That is the thing Lyra has been giving me in silence all Act IV. That is the thing Noelle is asking me to hold tonight by trusting her with six hours that are actually twelve."

    athought "They have all been teaching me the same thing in different registers for the whole act. The act's question is: can I lead without turning leadership into a weapon. Tonight I answered the question in a room where the weapon was my own decision about Noelle's framework. The answer was no, I am not going to turn the framework into a weapon, and I am also not going to turn Noelle into a weapon by letting her do the rebuild without sleep."

    athought "The answer is the answer the act has been preparing me to give."

    athought "The answer is costing me the same thing the side chair costs me. The cost is the muscle of wanting to decide on my own for her. The muscle is still there. The muscle is not going away. The posture is a way of holding the muscle still while the muscle complains."

    "Noelle picks up her pad from the table. She does not say anything else. She nods once at Aeron — the analyst nod, the acknowledgement nod — and walks back toward the analyst alcove."

    "Lyra at the table. Zira at the foot. Aeron at the side chair. The empty head chair with its face-down datapad on its arm. Three working chairs and a surface."

    l "I am going to draft the backup rotation now. Zira, I am going to need a Ghostline relay key for the rotation's comms thread."

    z "Keying you."

    "Zira keys the Ghostline relay. Lyra pulls her tactical layer up and starts drafting the backup rotation. Zira returns to the static side of the Batch A framework and begins holding the western industrial theater layer."

    "Aeron stays in the side chair."

    "His hands are on the arms of the chair."

    "The scene holds on the ops table in the fourth-shift ambient — the low overhead hum, the tactical tick of the holo-table, the small precise sounds of Lyra's drafting, Zira's hands at the Ghostline. The empty head chair in the corner of the frame with its face-down pad. The western industrial theater layer on the holo-table with the red mark where Davel Ostra went off the board and the intercept panel with Marcus's three plaintext lines still on the display."

    "The scene holds for a beat."

    "Fade."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("rhea_first_cut_landed", True)
    $ flag("noelle_framework_compromised_as_target_template", True)
    $ flag("aeron_did_not_overrule_framework", True)
    $ flag("aeron_overruled_sleep_estimate_only", True)
    $ canon_set("phoenix.kia.davel_ostra", "Act IV s16")
    $ canon_set("echelon.rhea_vestin", "active")
    $ canon_set("echelon.rhea_cadence_rates", "2_4_8_derivative_fit")
    $ canon_set("noelle.framework_version", "v0.4_taken_down_for_v0.5_rebuild")
    $ canon_set("noelle.framework_next_draft_eta", "10:18_twelve_hours_from_strike")
    $ npc_remember("Noelle", "realized_framework_is_target_template", weight=3)
    $ npc_remember("Noelle", "built_davel_ostra_kill_template_with_her_own_hand", weight=3)
    $ npc_remember("Aeron", "asked_what_next_version_looks_like", weight=3)
    $ npc_remember("Aeron", "overruled_sleep_estimate_six_to_twelve", weight=2)
    $ npc_remember("Zira", "holding_static_side_of_batch_a", weight=2)
    $ npc_remember("Lyra", "drafting_western_medical_rotation_backup", weight=2)
    $ rel_bump("Noelle", trust=2, conflict=1)
    $ metric("marcus_clock_hit", set_to=1)
    $ metric("phoenix_kia_act4", add=1)
    $ tp_seed("a4.rhea.first_cut")
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s16_rhea_strikes_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Oh-six-twelve the morning after a4_s15. Six days and eleven hours
#     after Marcus signed the Rhea Vestin dispatch in a4_s07. The Marcus
#     six-day adaptation clock (established in a4_s03) hits here — the
#     first Rhea Vestin cut lands at zero-five-fifty-seven, fifteen
#     minutes before the ops wing alert tick escalates.
#   - Aeron was asleep in the analyst alcove auxiliary cot, having been
#     told by Tessa at the end of s15's night to sleep where the ops
#     wing could reach him. Noelle was asleep in the analyst alcove's
#     primary cot, the first sleep she has had in six days.
#   - Selene is absent from the ops wing scene — she is running the
#     Rhea-contingency perimeter sweep Zira drafted at the aftercare
#     end of s15. Selene appears on comms only.
# cann.what_happened:
#   - Lyra at the ops table at fourth-shift skeleton. Incident bell on
#     the Western Industrial Theater layer. Alert tick escalates from
#     one ping to six pings a minute inside sixty-four seconds. Lyra
#     reads the signal metadata and recognizes a surgical team cadence
#     rather than a patrol event. Names the cadence as a Rhea Vestin
#     shape. Calls Aeron, Noelle, a Ghostline reader, and Zira up.
#   - Aeron arrives. His body goes automatically to the s14 side chair
#     — the first confirmation that the posture is beginning to
#     default in his muscle memory. He notes it internally and accepts
#     the timeline.
#   - Zira arrives from the workshop direction. Takes the foot of the
#     table. Opens the Ghostline layer. Reads a back-channel
#     confirmation that the Phoenix asset off the board is Davel Ostra
#     — senior runner, third-ring logistics, western industrial
#     corridor. Davel Ostra is introduced here as a name and canonized
#     as the first named KIA of Act IV.
#   - Zira also notes that in Noelle's framework, Davel Ostra is
#     call-sign DO-7, and that Noelle has been building predictive-
#     behavior models around DO-7 for six days without knowing the
#     call-sign is a man.
#   - Aeron asks Lyra to go get Noelle from the analyst alcove and
#     bring her up carefully — not to tell her the incident in the
#     corridor, to let her find the layer at the table. The finding
#     will matter more than the telling.
#   - While Lyra is in the alcove, the Ghostline picks up an Echelon
#     back-channel intercept. Five lines, three plaintext, two
#     redacted. Sender tagged as Marcus (m), recipient tagged as Rhea
#     Vestin (rv). The three plaintext lines:
#       (1) "First cut clean. Node DO-7 off the board per the pattern
#            we discussed. Congratulations on the shape of it."
#       (2) "Pattern-matching on the subject's framework is holding.
#            The next three cuts will read the framework's second and
#            third derivatives at rates of two, four, and eight.
#            Maintain the cadence you set today. Maintain the geometry."
#       (3) "The subject is going to know inside the hour that the cut
#            was shaped around her own work. I want her to know. That
#            is part of the shape."
#   - Aeron recognizes that the subject is Noelle and that Marcus
#     wanted Phoenix to pick up the intercept. He refuses to hide the
#     intercept from Noelle. Tells Zira to leave it open on the layer
#     and close the surrounding subwindows for a clean read.
#   - Noelle arrives with Lyra. Takes the head-adjacent standing
#     position (Selene is absent). Reads the red mark, reads the
#     intercept, reads the plaintext lines three times. Palm flat on
#     the table edge — the palm-press is her version of "not making a
#     fist." Names the situation out loud: DO-7 is Davel Ostra. Her
#     framework is the target template. She built Davel Ostra's kill
#     template with her own hand four days ago.
#   - Realization: the Batch A framework has been running for ninety-
#     six hours without rotation because Noelle has been in ops-shift
#     mode rather than framework-maintenance mode. The seventy-two-
#     hour self-invalidation clause never fired. Rhea read the Batch A
#     signature and fit her cadence to it. The ninety-six hours was
#     exactly the window Marcus needed.
#   - Noelle: "I need to take the framework down."
#   - Aeron's load-bearing decision: he does not overrule her on the
#     framework, he does not dismiss the framework, he asks her what
#     the next version looks like. She does not have the answer. He
#     holds the not-knowing in the room.
#   - Noelle: "I need six hours." Aeron: "Take twelve." He explicitly
#     names that he is overruling the sleep estimate, not the
#     framework decision. The twelve-hour reasoning: four hours
#     forced sleep in the analyst alcove cot, then eight hours at
#     the framework after eating and after Tessa has looked at her.
#     Twelve-with-sleep is faster than six-without because a
#     six-hour estimate from a two-hours-in-six-days analyst turns
#     into a twenty-hour pause when the analyst collapses halfway
#     through. Aeron lays out the collapse math.
#   - Noelle accepts twelve. Commits to a v0.5 draft at ten-eighteen.
#   - Aeron issues two static-holds to preserve the Batch A framework
#     as a static defense for twelve hours: Zira holds the static
#     side of the framework from the foot of the table; Lyra drafts
#     a western theater medical rotation backup and co-signs it with
#     Tessa at oh-eight-hundred so Tessa's sleep stays intact.
#   - Aeron speaks to Selene on comms. Tells her to hold the Rhea-
#     contingency perimeter sweep at current cadence — do not
#     accelerate. The reasoning: Rhea has probably priced in
#     Phoenix's acceleration curve, and giving her a new rate is
#     giving her new data. Selene holds cadence. Aeron calls a full-
#     table meeting at oh-eight-thirty (Selene, Tessa, eastern
#     corridor analyst, plus the four in the room). Framework is not
#     reset at oh-eight-thirty; working assumptions are reset.
#   - Scene closes on the ops table running with Lyra drafting, Zira
#     holding the static side, Aeron at the side chair with his
#     hands on the arms of the chair and the empty head chair still
#     a working surface in the corner of the frame.
# cann.aeron_state:
#   - The s14 side-chair posture is now body memory. His body goes
#     to the side chair automatically on entry. Internal thought
#     notes this and accepts it as on-timeline.
#   - The posture is tested in the scene's most difficult possible
#     direction: the analytic tool Aeron needs on the table has just
#     become a vulnerability, and the analyst asking him the question
#     is the person whose work Marcus is pattern-matching against.
#     The posture holds. He does not overrule the framework decision.
#     He overrules the sleep estimate and names the overrule as
#     explicit. The named overrule is the scene's signature move.
#   - Internal answer to Act IV's central question: "Can I lead
#     without turning leadership into a weapon?" — the answer
#     delivered tonight is: I will not turn Noelle's framework into
#     a weapon and I will not turn Noelle into a weapon by letting
#     her do the rebuild on inadequate sleep. The answer is the
#     answer the act has been preparing him to give in all five LI
#     registers (Selene's teacher-inheritance, Tessa's rule-of-three,
#     Zira's "see that I am asking," Lyra's presence-is-enough,
#     Noelle's framework trust).
# cann.noelle_state:
#   - Two hours of sleep in six days before the scene. Ops-shift
#     mode rather than framework-maintenance mode has kept her from
#     rotating the framework at seventy-two hours. The ninety-six-
#     hour window is entirely her own work schedule and Aeron's
#     lack of enforcement, and Noelle will carry that as a private
#     weight.
#   - She realizes in real-time that the Batch A framework has
#     become the target template Marcus is pattern-matching Rhea's
#     cadence against. She says out loud: "I built Davel Ostra's
#     kill template with my own hand four days ago." This is the
#     scene's load-bearing Noelle line and seeds the rest of her
#     Act IV arc.
#   - The palm-press on the table edge — the flat palm used as a
#     physical discipline to prevent the fist — is her signature
#     body tell for this scene and should appear in downstream
#     Noelle scenes when the framework is under discussion.
#   - The ceiling-glance at the ops wing ceiling is her version of
#     the Zira three-pulse tell — a small private discipline the
#     body does so the mind can proceed. Nobody performs it back
#     at her. This is deliberate.
#   - She accepts twelve hours instead of six. The acceptance is
#     her trust in the collapse math. She does not argue. She does
#     not apologize for the six-hour estimate. She sizes to twelve
#     and commits to a v0.5 draft at ten-eighteen.
# cann.thematic_flags:
#   - Marcus's weaponization of Noelle's framework. The scene's
#     central thematic move. The framework is not broken — the
#     framework is being used by the wrong reader. A map is a
#     target if the wrong person reads it. This is the Act IV
#     dramatic realization of Marcus's a4_s07 "shared command is a
#     surface with seams" framing. Marcus has found a seam and is
#     pattern-matching it.
#   - The 2-4-8 derivative cadence. New Echelon operational tempo
#     canonized here. Rhea will make three more cuts at rates of
#     two, four, and eight before the framework rebuild lands.
#     Downstream Act IV scenes must honor the escalation curve.
#   - Aeron's overrule of the sleep estimate as the correct
#     overrule. This is the chapter-level teaching about command —
#     the correct overrule is the overrule that takes care of the
#     worker and leaves the work in the worker's hands. The
#     incorrect overrule is the overrule that takes over the work.
#     Aeron has been trained in the incorrect overrule his whole
#     life and the correct overrule is the act's lesson.
#   - The named overrule. Aeron explicitly tells Noelle he is
#     overruling her sleep estimate and names it as an overrule.
#     The naming is the Act IV discipline — do not hide an
#     overrule behind a softer word. "Take twelve" is an overrule.
#     Calling it that out loud is the work.
#   - Side-chair body memory. One day in, the posture defaults in
#     the muscle. The development-of-the-posture is on the
#     timeline Tessa predicted in her oh-three-hundred medbay
#     visit (referenced in s14's internal thought).
#   - Davel Ostra as the first named Act IV KIA. The name is
#     load-bearing on Noelle's framework-as-target-template
#     realization, not on Aeron's personal ledger. Davel Ostra is
#     not on Aeron's rule-of-three, because the rule-of-three
#     broke on Liora Rylan's name in a4_s11b and has not been
#     rebuilt. Davel Ostra goes on the Noelle-ledger instead.
# cann.character_moments:
#   - Lyra: reads the signal metadata first and names the Rhea
#     cadence. Goes to wake Noelle up because Lyra's hand on a
#     shoulder at oh-six-seventeen is the correct hand. Drafts
#     the medical rotation backup at the table and co-signs with
#     Tessa at oh-eight-hundred to protect Tessa's sleep. Lyra's
#     role in the scene is the Lyra role — the person whose
#     presence is a non-performative kindness. She is the calmest
#     body in the room for the whole scene.
#   - Zira: comes up from the workshop in the workshop jacket.
#     Aeron notes the direction (continuity with s15) without
#     commenting. She operates in the one-second switch from
#     personal mode to operational mode. Names Davel Ostra from
#     the Ghostline relay. Holds the static side of the Batch A
#     framework as a twelve-hour bridge while Noelle rebuilds.
#   - Noelle: palm-press, ceiling-glance, "I built Davel Ostra's
#     kill template with my own hand four days ago," takes
#     twelve hours when she asked for six.
#   - Aeron: the s14 posture now in body memory. Does not overrule
#     the framework. Asks what the next version looks like. Holds
#     the not-knowing. Names the sleep-overrule explicitly. Lays
#     out the collapse math. Issues two holds and a comms
#     instruction. Calls a full-table meeting at oh-eight-thirty.
#   - Selene (comms only): "Selene, secondary base perimeter,
#     sector three. Rhea-contingency sweep. Hearing you." Then at
#     scene end: accepts the hold-cadence instruction and the
#     oh-eight-thirty full-table meeting. Scene does not bring
#     her into the room. She is the field commander on the
#     perimeter and the scene honors her absence.
#   - Marcus (intercept transcript only): three plaintext lines.
#     No body. No in-room dialogue. His voice tagged m on the
#     Ghostline layer. The fifth Marcus scene of Act IV where he
#     is a signal rather than a body, in parallel to the
#     s07 empty-chair address where he was a body speaking to
#     a signal.
# cann.callbacks:
#   - a4_s03_marcus_adapts_emp: the six-day adaptation clock. The
#     clock hits here. The scene is the chapter's payoff for the
#     clock.
#   - a4_s07_echelon_interlude_4_emp: Rhea Vestin dispatch, signed
#     without hesitation. The yellow line on Marcus's analyst
#     panel. "Doubt is the lever." This scene is the first lever
#     insertion. Rhea read the framework shape and cut a seam.
#   - a4_s09_noelle_implicated_emp: Noelle's signed framework.
#     The framework she has been protecting since Batch A is the
#     framework that Rhea pattern-matched against. The payoff for
#     s09's "I love you as data" move is s16's "I built Davel
#     Ostra's kill template with my own hand four days ago."
#     Same diction, same discipline, applied to grief rather than
#     love.
#   - a4_s13_protecting_exhaustion_emp: the framework sheet placed
#     on the ops table for its first operational use. s13 is the
#     framework's birth. s16 is the framework's first wound.
#   - a4_s13a_quiet_after_failure_emp: if this scene exists as a
#     Noelle-aftermath beat, it runs after a4_s16 and addresses
#     the Davel Ostra realization in a quieter room.
#   - a4_s14_return_to_the_table_emp: the side chair posture. One
#     day in, the posture is body memory. The scene is the
#     posture's first stress test and the posture holds.
#   - a4_s11b_the_ones_he_lost_emp: Aeron's rule of three broke on
#     Liora Rylan's name. Davel Ostra does not go on Aeron's
#     ledger because the ledger is not functional. Davel Ostra
#     goes on Noelle's ledger instead. The scene quietly honors
#     the s11b break by not reusing the broken structure.
#   - a4_s10_what_selene_meant_emp: "delegate the question." The
#     "what does the next version look like" move is the most
#     direct s10 callback in Act IV — Aeron delegates the
#     analytic question to the analyst even when the answer is
#     "I do not have an answer to that yet." The delegation is
#     the point.
#   - a4_s12a_she_is_not_just_tactical_emp: Selene's Ilene
#     teaching-as-survival framework. Noelle's framework-rebuild
#     as her version of Ilene-work. Both women are metabolizing a
#     loss they cannot undo by continuing the discipline that
#     failed to prevent the loss. Parallel is not named in
#     dialogue.
#   - a4_s15_zira_deepening_erotic_emp: Zira's workshop jacket.
#     The direction Zira comes from. Aeron's noting and not-
#     reacting. The Rhea-contingency perimeter sweep mentioned at
#     the s15 aftercare end — this scene is the scene where the
#     sweep becomes load-bearing.
# cann.block_status: drafted
# cann.requires_followup:
#   - Oh-eight-thirty full-table meeting — next scene or beat after
#     s16 should either be the meeting or a medbay interlude with
#     Tessa before the meeting. The meeting should not reset the
#     framework; it should reset the working assumptions.
#   - Noelle's twelve-hour framework rebuild lands at ten-eighteen.
#     A v0.5 draft scene should fire in the Act IV Phase III
#     window. The rebuild needs to address the ninety-six-hour
#     rotation failure and the pattern-matching vulnerability.
#   - Rhea Vestin's second cut is coming at the two-rate within
#     twelve to eighteen hours. The scene where she lands it is
#     the next Rhea beat. Phoenix should have the pre-positioned
#     response on the board from this scene's static-hold.
#   - Davel Ostra is canonical KIA. His name can appear on a
#     Phoenix memorial layer or in a Zira-Ghostline scene later,
#     but should not reappear on Aeron's rule-of-three because
#     Aeron's rule-of-three broke in s11b.
#   - Marcus intercept transcript lines are canonized as Marcus's
#     voice for Phase III. Future Marcus scenes in Act IV can
#     reference the 2-4-8 cadence and the "subject's framework"
#     framing.
#   - Aeron's "named overrule" move is canonical command-geometry
#     vocabulary for the rest of Act IV and Act V. Future scenes
#     where Aeron needs to overrule a teammate should use the
#     explicit-naming protocol — do not hide the overrule.
#   - tp_seed a4.rhea.first_cut is the branch point for Phase III
#     Echelon scenes. All downstream Rhea scenes in Act IV should
#     reference this scene as the first cut landing.
