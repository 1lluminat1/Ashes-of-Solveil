# =======================================================
# ACT 4 - Scene 03: Marcus Adapts (Empathy Path)
# File: a4_s03_marcus_adapts_emp.rpy
# Type: PLOT SCENE — Noelle presents intelligence. Plot hinge.
# Matrix: Noelle "analysis as commitment" phase 1 + Marcus counter-learning reveal.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s03_marcus_adapts_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s03_marcus_adapts_emp:
    $ show_timeline("25th of Forge, 390 A.C.", "15:00", "Phoenix Secondary Base — Noelle's Workspace")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked for the opening on Noelle's workspace — the stillness of
    #         eighteen straight hours of work. No handheld drift here. Noelle's rooms
    #         are always shot steady. Her frame is her authority.
    #         When Noelle activates the data crystal: the camera pushes slowly in
    #         on the projection. Aeron and Selene framed on either side of it,
    #         equidistant, the projection between them like a map at a summit.
    #         The pattern overlay reveal: lock on the hologram. Hold. Let the overlay
    #         happen inside the frame, not the camera.
    #         When Aeron reacts: tight on his face. Not on his hands. His face.
    #         The grief enters through the eyes, not the mouth.
    #         Noelle's final beat: medium on her. Not tight. She is small in the frame.
    #         She is being honest about being small.
    # LIGHTING: Noelle's workspace: the overhead off. Three task lamps on the console.
    #           The data crystal is the primary light source when activated — a pale
    #           blue wash that cools every face. Noelle looks colder than she is.
    #           Aeron's face under the projection light: the edges hard, the center
    #           soft. Selene: half-lit. Listening light.
    # SFX: Loop — data crystal hum (pale, sine wave), ventilation, Noelle's keyboard
    #      at her own pace. The keyboard stops when she begins to speak.
    #      One-shots — data crystal activation (a low chime), pattern overlay (a second
    #      chime, softer), a datapad closing, the silence after the overlay.
    # FACE: Noelle — eighteen hours in. Not tired in a visible way. Noelle's tired
    #        shows in the stillness of her hands. Her hands are too still. That is the tell.
    #        Aeron — bracing for information. Then absorbing it. Then grieving.
    #        The grief is quiet. It is not for the plot. It is for Marcus.
    #        Selene — recognizing. The face of someone seeing something she has seen
    #        before and never names aloud.
    # BLOCKING: Noelle's workspace. Console along the back wall. Data crystal stand
    #           central. Noelle seated at the console. Aeron enters and stands to her
    #           left. Selene enters and stands to her right. They do not sit. This is
    #           a briefing delivered to two co-commanders.
    #           At the end: Aeron moves one step closer to Noelle. Not to comfort.
    #           To acknowledge.
    # CANON: PLOT HINGE. Marcus is operational, consolidating, and has learned to use
    #        Aeron's own counter-strike methodology against Phoenix. This reverses the
    #        a3_s07 dynamic: the student has taught the teacher. Noelle's arc begins
    #        moving from "documenting" to "implicated."
    #        Callbacks: a3_s07 (Aeron recognizing his own handwriting in Echelon's strike),
    #        a3_s14 (cipher and the shape emerging — Noelle's projection architecture),
    #        a3_int_noelle_unmeasurable_emp (the category error Noelle committed alone),
    #        a3_s22 (the execution and the 2.3 million witness feed routing), a4_s01
    #        (the morning after — still running the broadcast), a4_s02 (the hand-log
    #        Noelle kept, which this scene retroactively explains).

    # ========= VOICE BASELINE =========
    # EMP cadence. Noelle's voice: technical, precise, and — new in Act 4 — starting
    # to carry something her voice has not carried before: uncertainty about her own
    # position in the system she is measuring. Aeron: spare. Listening hard. When he
    # speaks, short. Selene: two sentences total in the scene. She is here to witness
    # and to hold the shape.

    # --- VISUAL SETUP ---
    # [INT. SECONDARY BASE — NOELLE'S WORKSPACE — LATE MORNING]
    # Late morning of the same day as a4_s02. Noelle has been running signal analysis
    # for eighteen hours. She has asked Aeron to come. He has brought Selene, because
    # the shape of shared command is what he is building now.

    #scene bg_noelle_workspace_data_crystal with dissolve
    #play ambient "sfx/ambient/workspace_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE WORKSPACE ==========

    "Noelle's workspace smells like ozone."

    "It always smells like ozone. Three task lamps run at full brightness, the data crystal on its stand cycles through a low standby hum, and the console behind her carries eight active windows of signal traffic she has been parsing since yesterday afternoon."

    "Aeron enters first. Selene enters second."

    athought "She asked for me specifically. I brought Selene because the shape of this is supposed to have two of us in every room that matters."

    athought "This room matters."

    "Noelle does not turn around when they enter. She is finishing a line. That is a Noelle thing. She finishes lines the way Tessa caps markers. It is not rudeness. It is respect for the thing she is working on."

    "When she does turn, her hands go still. That is the tell."

    athought "Her hands are too still."

    athought "Noelle's hands are too still when she is at the edge of what she can measure."

    n "Thank you for coming."

    n "I have been running signal analysis for eighteen hours. The first ten on the broadcast propagation model — how many nodes, how many witnesses, how Echelon is attempting to scrub and where the scrubbing has failed. The second eight on something I was not expecting to find."

    n "I would like to show it to you on the crystal. I need the projection. The patterns are too dense for a flat display."

    sel "Go ahead."

    # ========== PHASE 2 — MARCUS IS OPERATIONAL ==========

    # CAMERA: slow push-in on the crystal stand as Noelle's hand reaches for
    #         it. The pale blue wash enters the frame before the projection
    #         resolves — we see the light change on the three faces first,
    #         then the dimensional map blooms above the stand. Hold the
    #         push. Let the overlay bloom inside the frame, not the camera.
    # LIGHTING: Crystal activation. The three task lamps drop to background.
    #           The pale blue wash becomes primary key. Every face shifts
    #           from warm lamp light to cold projection light in the same
    #           breath. Aeron's edges harden. Noelle's softens. Selene's
    #           goes half-dark.
    # SFX: One-shot — the low chime of the crystal activation. The loop
    #      gains one layer: the pale sine-wave hum of the projection field.
    #      The keyboard at the console stops for the duration of Noelle's
    #      first finding.

    "Noelle activates the data crystal."

    "The pale blue wash fills the room. The projection resolves above the stand — a dimensional map of the city's signal grid, with Echelon's command network overlaid in hot red."

    "The red is fractured."

    n "First finding. Marcus is still operational."

    n "The broadcast exposure dispersed his primary command network. The feeds showing him on the platform, the voice signature matching his public orders, the routing of the execution through Echelon's own infrastructure — all of it forced a defensive reconfiguration. His command nodes went dark for a window of eleven hours."

    n "He is rebuilding. He is rebuilding fast. And I do not yet know where the new nucleus is."

    athought "Eleven hours of darkness. Not enough."

    athought "We had eleven hours when we should have had a dismantling."

    a "Consolidation pattern. You flagged it this morning to Selene."

    n "Yes. Three patrol battalions pulled off the outer rings, moving toward a center I cannot resolve. The signal pattern suggests a fortified command bunker, not a mobile headquarters. He is burrowing, not running."

    n "That is the first finding. It is the less significant one."

    # ========== PHASE 3 — THE SECOND FINDING ==========

    # CAMERA: over-shoulder from Aeron's side as Noelle touches the console.
    #         The second and third overlays land inside the projection; the
    #         camera does not cut to them, the camera waits for them. Rack
    #         focus from Noelle's hand to the hologram as the green layer
    #         fades in. Land the rack on the moment the shapes align —
    #         not before, not after.
    # VISUAL: The layers read in order: red (Marcus's command network),
    #         green (Echelon field ops, last 36 hours), white (Aeron's own
    #         post-defection counter-strike framework). The white and the
    #         green are the same shape. The green is lagged behind the
    #         white by a consistent window. The beat is the recognition.

    "Noelle touches the console."

    "A second layer overlays the first. Green this time. Operational signatures — the pattern analysis of Echelon field tactics over the last thirty-six hours."

    n "Second finding. Marcus has adapted."

    n "Since the broadcast, Echelon field operations have shifted signature. The old pattern — the one you identified in a3_s07 as your own handwriting — has been partially retired. The new signature is different."

    n "I want to show you the difference."

    "She touches the console again."

    "A third layer overlays the second. White. Aeron's own historical counter-strike patterns — the tactics he ran in the weeks after the main base fell, the patterns he and Zira built against Echelon supply chains, the improvisation framework he developed when the standard Aeries curriculum stopped applying to guerrilla work."

    "The white layer and the green layer are the same shape."

    "Exactly the same shape."

    athought "No."

    "The green is slightly behind the white. Lagged. Noelle has time-aligned them so the lag is visible. Every move in the white layer is followed, within twelve to thirty-six hours, by a corresponding move in the green layer."

    athought "He is using my counter-strike framework back against us."

    athought "Not the Aeries curriculum. Not the patrol patterns from the Academy. The guerrilla framework. The thing I built AFTER I defected. The thing I built because the Aeries curriculum was not going to save us."

    athought "He is running my improvisations."

    n "The lag window is consistent with a cell of analysts studying our operational outputs in near-real-time and feeding pattern summaries to Marcus's field commanders."

    n "I need to be precise about what I am saying. I am not saying Marcus is guessing. I am saying Marcus has deployed analysts to read our tactics the way I read his, and then he is deploying the results as doctrine."

    n "The student has taught the teacher."

    # ========== PHASE 4 — AERON RECEIVES IT ==========

    # CAMERA: tight single on Aeron. Not on his hands — his face. Noelle
    #         and Selene drop out of focus in the pale blue wash. Hold
    #         the tight for the full inheritance monologue. This is the
    #         longest close in the scene; do not cut away from it.
    # FACE: Aeron — the bracing face gives way. Not to tears. To the
    #        recognition that cannot be said out loud. The mouth does
    #        nothing while the eyes do all the work. The grief is quiet.
    #        It is not for the plot. It is for Marcus.

    "Aeron does not move."

    "Selene looks at him once — a brief glance, not concerned, just confirming he is still on his feet — and then returns her attention to the projection."

    athought "In a3_s07, I walked into a base that had been destroyed with my own methodology. The Aeries curriculum turned into a weapon against the people I loved."

    athought "I spent the weeks after telling myself: the Academy is behind me. The training is behind me. I can build something new, and what I build will not have his fingerprints."

    athought "Then I built it."

    athought "And he read it."

    athought "And now what I built — the thing that was supposed to be mine — is a weapon against the people I love."

    athought "There is a word for this and I do not want to say it out loud."

    athought "Inheritance."

    "He looks at the overlay for a long moment."

    "He is not tactical. He is grieving."

    athought "Marcus is still my father."

    athought "Marcus killed my mother."

    athought "Marcus is now learning from me."

    athought "All three sentences are true. They cannot be true at the same time. They are."

    # BLOCKING: Selene's hand moves flat onto the console near Aeron's.
    #           Not touching. Present. Frame the two hands in the lower
    #           third of the two-shot, the projection still running above
    #           them. This is the cipher-table gesture from a4_s02
    #           redeployed for a room that does not know what the cipher
    #           table means. The camera knows. Aeron knows. Noelle does
    #           not — and the frame does not tell her.

    "Selene, without looking at him, puts her hand flat on the console near his. Not touching. Present. The gesture from the cipher table this morning, redeployed for a room that does not know what the cipher table means."

    athought "She sees it. She is not going to say it in front of Noelle. She is just going to stand there and be the thing that keeps me from stepping back from the projection."

    athought "I am not going to step back."

    a "How long have they had this."

    n "The adaptation window opens approximately six days ago. Consistent with an intelligence cell spun up in response to the first Phoenix counter-strike success — when we hit the northern corridor route Marcus was using for the internal transport of the Sector Seven prisoners. He noticed the hit. He built the cell. The cell has been reading us ever since."

    n "I did not see it until today because I was running broadcast propagation models and not field operation pattern analysis. I found it by accident. I was checking the propagation model against the field data and the field data was carrying a shape the propagation model could not explain."

    athought "She found it by looking sideways at the wrong thing and noticing the right thing."

    athought "That is the Noelle I have come to trust."

    a "The cell. Can we locate it."

    n "I have signatures. I do not yet have a location. Locating it is a fourteen-to-twenty-hour task that I have not started yet because I wanted you to see the finding before I moved to phase two."

    sel "Start phase two."

    sel "Full priority. Anything else on your queue gets reassigned or deferred."

    n "Understood."

    # ========== PHASE 5 — NOELLE BREAKS CATEGORY ==========

    # CAMERA: medium on Noelle. Not tight. She is small in the frame.
    #         She is being honest about being small. The projection
    #         continues behind her, the three layers still hanging. She
    #         does not turn to look at them. She is looking at Aeron.
    #         Selene drops into the soft edge of the frame — present,
    #         not witness-ing.
    # FACE: Noelle — the observer face gives way. First time in the
    #        series she uses "I" about herself as subject and not as
    #        instrument. The stillness in her hands holds. The stillness
    #        is now a different stillness — no longer the tell of a
    #        woman working; the tell of a woman who has stopped being
    #        able to separate herself from the work.

    "Noelle does not deactivate the crystal."

    "She leaves the overlay running. The three layers — red, green, white — hanging in the pale blue wash above the stand."

    "She looks at Aeron. Not at Selene. At Aeron."

    n "I have to say something that is not part of the briefing."

    n "I would like to say it on the record but I do not know whose record."

    athought "That is an odd sentence. Noelle does not speak in odd sentences."

    athought "That IS the sentence. The oddness is the content."

    n "When I began working for Phoenix, I described my role to myself as 'analysis.' A neutral function. I built models. The models were instruments. Instruments do not choose sides. They produce readings."

    n "I am telling you now that the model I built — the broadcast propagation model, the pattern analysis framework, the Ghostline signal architecture I helped refine for Zira — is being read from the other side."

    n "Marcus's analysts are reading my outputs backwards. Not because I gave them access. Because the broadcast itself is a dataset. Every time we push content through the Ghostline to reach witnesses, we are also producing a pattern Marcus's cell can reverse-engineer."

    n "I built a model that tells us how truth propagates through a populace. Marcus's cell is using that same model to tell Marcus how to propagate suppression."

    n "My instrument is running for both of us."

    n "And I do not know what that makes me."

    "A silence."

    athought "She is not asking me to absolve her."

    athought "She is asking me to acknowledge that she is no longer what she thought she was."

    athought "In a3_int_noelle_unmeasurable she wrote a log entry with herself as the subject and did not submit it for peer review. That was the first crack. This is the second."

    athought "She is becoming something that does not fit inside the category 'observer.' She is becoming a participant. A participant on both sides, whether she wants to be or not."

    # ========== PHASE 6 — THE ACKNOWLEDGEMENT ==========

    # CAMERA: hold. The camera does not push. Aeron enters the medium-
    #         on-Noelle frame from off-screen left as he takes the step.
    #         They are now both in the same shot at the same distance,
    #         the projection still running between them. This is the
    #         first time in the scene Aeron and Noelle share a frame
    #         at the same scale.
    # BLOCKING: One step. Not to comfort. To acknowledge. This is the
    #           first physical move Aeron has made since the opening.
    #           Let the step register as the beat before he speaks.

    "Aeron takes one step closer to her."

    "Not to comfort. To acknowledge. To stand in the same frame as the person who is saying this thing."

    a "You are not a neutral observer anymore."

    a "I don't know what you are either."

    a "I am not going to pretend I do. I am also not going to tell you the thing you already know — that you being implicated does not mean you have done something wrong."

    a "You already know that. Saying it would be me trying to close a question that does not close yet."

    "A beat."

    a "So. The question stays open."

    a "You keep running the model. Because the model is what tells us where Marcus is going. And we will keep asking what it makes you, together, until we have an answer that is honest enough to live with."

    n "Together."

    n "That is a word I did not expect to hear in response to what I just said."

    a "It is the only word I have."

    athought "She is nodding. Small. Once. The way Selene nodded at the cipher table this morning. The way I nodded back."

    athought "I am starting to see that the nod is our shared grammar now. A signal we are making up together because the old signals were built by my father."

    # ========== PHASE 7 — THE PROJECTION HOLDS ==========

    # CAMERA: slow push-in on the projection itself. Pull the human faces
    #         out of the frame entirely. Hold on the three-layer overlay:
    #         red, green, white. The trajectories extrapolating forward.
    #         The convergence point in the western industrial corridor
    #         resolves inside the frame as a single bright meeting of
    #         lines. Let the math do the speaking the characters will not.
    # VISUAL: The two shapes — white and green — meeting at a point six
    #         days from now. Nobody says it. The frame says it. This is
    #         the closest the scene gets to a thesis shot, and it is the
    #         scene's one hero plate: the projection alone, humans
    #         excluded, the collision geometry lit by itself.

    "Nobody deactivates the crystal."

    "The three layers keep running. Red, green, white. Marcus consolidating. Marcus learning. Aeron's own framework turned back on the people Aeron built it for."

    "At the center of the projection, the two shapes — the white and the green — are converging. Noelle has not spoken this part aloud, but the projection does the speaking. The projected trajectories of both patterns, extrapolated forward, meet at a point in the city's western industrial corridor roughly six days from now."

    "They are going to collide. The collision is not hypothetical. It is scheduled by the math."

    athought "Six days."

    athought "Six days until the thing I built and the thing he learned meet in the same physical space, both moving at full speed."

    athought "I am not going to say that out loud either. Not yet. It is the kind of sentence that changes the shape of a room if you say it wrong."

    "Selene sees it. Noelle sees it. Aeron sees it. None of them say it."

    "The silence is the acknowledgement."

    # ========== PHASE 8 — CLOSING ==========

    # CAMERA: pull back to a three-shot including all three figures and
    #         the projection. Selene speaks from the edge of the frame.
    #         The care protocol is quiet; the composition is flat.
    # FACE: Selene — the face of a woman running Tessa's rule on somebody
    #        who does not yet know what the rule is. Gentle. Unhesitating.
    #        The care moves through her without ceremony.

    sel "Noelle. Eighteen hours in. When did you last eat."

    n "I do not remember."

    sel "Before phase two. Eat something. That is not a suggestion."

    athought "She is running the same protocol Tessa ran on me this morning."

    athought "Food as infrastructure. The basic maintenance that keeps people upright for the work. Tessa teaches Selene. Selene teaches me. Selene teaches Noelle. The care moves through the base like a weather system."

    athought "Marcus's cell cannot read that pattern. The care pattern is not on our operational feeds. It is in the places the Ghostline does not route."

    athought "That is something. It is a small thing. I am going to hold it anyway."

    n "Understood."

    "Noelle turns back to the console. Her hands are already moving — phase two opening, the cell-location queries spinning up, the task sequence building."

    # CAMERA: empty-workspace plate for the closing coda. Crystal still
    #         running. Pale blue wash on empty walls. Three task lamps
    #         still lit at the console where Noelle has returned to work.
    #         Aeron and Selene leaving frame-right; hold on the room
    #         after they exit. The projection is the only motion in the
    #         shot. This is the "quiet stitch" plate per the Cinematography
    #         Bible §3 — negative space for introspection before the cut.

    "Aeron and Selene leave the workspace together. They walk the corridor without speaking. The projection stays behind them, running in the empty room, casting pale blue light on the walls."

    "Outside, the base continues its morning. Intake is being run by Tessa now. The clinic run is moving on schedule. Zira is back on the Ghostline. Lyra is somewhere with candles and a new name."

    "And six days away, at a point in the western industrial corridor that nobody has visited yet, two shapes are traveling toward each other on the trajectories math has already drawn."

    "The day is not going to be kind."

    "Aeron already knew that at the cipher table this morning."

    "He knows it differently now."

    # stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("marcus_operational_confirmed", True)
    $ flag("marcus_adapted_counter_strike", True)
    $ flag("marcus_analyst_cell_identified", True)
    $ flag("noelle_implicated_admission", True)
    $ canon_set("marcus_status_a4", "operational_consolidating")
    $ canon_set("marcus_intel_cell", "active_reading_phoenix_outputs")
    $ canon_set("noelle_arc_phase", "implicated")
    $ rel_bump("noelle", 2)
    $ npc_remember("noelle", "asked_to_say_it_on_no_record", weight=3)
    $ npc_remember("noelle", "aeron_kept_the_question_open", weight=3)
    $ npc_remember("selene", "watched_without_interrupting", weight=2)
    $ tp_seed("a4.marcus.counter_learning")
    $ tp_seed("a4.noelle.implicated")
    $ tp_seed("a4.collision.western_corridor.six_days")
    $ metric("marcus_network_state", "consolidating_bunker")
    $ metric("noelle_analyst_hours", 18)
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s03_marcus_adapts_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Late morning of the same day as a4_s02. Approximately 40 hours after Liora's
#     execution. Noelle has been running signal analysis for 18 uninterrupted hours.
# cann.what_happened:
#   - Noelle summons Aeron to her workspace. Aeron brings Selene — the shared command
#     shape made physical. Noelle presents a two-part briefing on the data crystal.
#   - FINDING 1: Marcus is still operational. Broadcast exposure forced a defensive
#     reconfiguration but did not destroy his command network. He is consolidating
#     into a fortified bunker. Three patrol battalions pulled from the outer rings.
#     Location not yet resolved.
#   - FINDING 2: Marcus has adapted. Echelon field operations over the last 36 hours
#     have shifted signature. The new signature exactly matches Aeron's post-defection
#     counter-strike framework (the guerrilla improvisation work, NOT the old Aeries
#     curriculum that was used in a3_s07). Time-aligned overlay confirms a consistent
#     12-36 hour lag. Marcus has deployed an analyst cell reading Phoenix operational
#     outputs in near-real-time. "The student has taught the teacher."
#   - Noelle reveals the cell has been active for approximately six days — spun up
#     after the first Phoenix counter-strike success (northern corridor / Sector Seven
#     prisoners). She found it by accident while cross-checking the broadcast propagation
#     model against the field data.
#   - Selene authorizes phase two (full-priority cell location) immediately.
#   - NOELLE BREAKS CATEGORY: On her own initiative, Noelle tells Aeron that her
#     model — the broadcast propagation / pattern analysis / Ghostline signal architecture
#     — is being read from the other side. Every Ghostline push is producing a dataset
#     Marcus's cell reverse-engineers. "My instrument is running for both of us. And I
#     do not know what that makes me."
#   - Aeron does not offer absolution. He keeps the question open explicitly: "You
#     keep running the model. We will keep asking what it makes you, together, until
#     we have an answer that is honest enough to live with."
#   - The projection shows the two pattern trajectories converging at a point in the
#     western industrial corridor in approximately six days. Nobody says this aloud.
#     The silence is the acknowledgement.
#   - Closing: Selene runs the same care protocol on Noelle that Tessa ran on Aeron
#     this morning. Eat before phase two. Care as infrastructure. The weather system
#     Marcus's cell cannot read.
# cann.aeron_state:
#   - Receives the finding as grief, not tactics. The inheritance frame enters his
#     internal voice for the first time in Act 4: "Marcus is still my father. Marcus
#     killed my mother. Marcus is now learning from me."
#   - Begins to see the care pattern — food, presence, the shared nod — as the thing
#     Marcus's analyst cell cannot map. Small. He holds it anyway.
#   - Does NOT step back from the projection. Shared command holds in the room.
# cann.path_tracking:
#   - Empathy path. No player choice — pure plot advancement.
#   - Flags: marcus_operational_confirmed, marcus_adapted_counter_strike,
#     marcus_analyst_cell_identified, noelle_implicated_admission
#   - canon_set: marcus_status_a4="operational_consolidating",
#     marcus_intel_cell="active_reading_phoenix_outputs",
#     noelle_arc_phase="implicated"
#   - rel_bump("noelle", 2) — Aeron kept the question open instead of closing it.
#   - tp_seed: a4.marcus.counter_learning (plot), a4.noelle.implicated (character arc),
#     a4.collision.western_corridor.six_days (plot clock)
#   - metric: marcus_network_state="consolidating_bunker", noelle_analyst_hours=18
# cann.thematic_flags:
#   - Inheritance — Aeron's post-defection work is now Marcus's doctrine. The thing
#     he built to NOT be his father is now teaching his father.
#   - The student has taught the teacher (inversion of a3_s07 "I know this handwriting").
#   - Noelle's arc movement: observer → implicated → participant. Category collapse.
#   - The care pattern (food, presence, the nod) as the unreadable weather system —
#     Marcus's cell can only read operational outputs, not the private grammar Phoenix
#     is building in the spaces between operations.
#   - The six-day collision clock — the math has drawn a scheduled meeting.
# cann.character_moments:
#   - Noelle: "I have to say something that is not part of the briefing. I would like
#     to say it on the record but I do not know whose record." This sentence reopens
#     the category error from a3_int_noelle_unmeasurable. She is asking Aeron to
#     witness her becoming uncategorizable to herself.
#   - Aeron: "You are not a neutral observer anymore. I don't know what you are either.
#     I am not going to pretend I do." Explicit refusal of premature closure. The
#     accountability-promise shape from a3_s01 redeployed as epistemic honesty.
#   - Selene: two sentences total in the scene. Presence without interruption. Then
#     redeploys the Tessa care protocol on Noelle. The weather-system of care moves
#     through her unasked.
# cann.block_status:
#   - Act 4 Chapter I, Scene 3. Plot hinge for Act 4's Marcus arc. Noelle arc phase 1.
#     The six-day collision clock is the structural spine of Chapter I.
# cann.requires_followup:
#   - Noelle phase two: locate the analyst cell. This is a scene seed — the cell
#     location reveal.
#   - The six-day collision in the western industrial corridor becomes the Chapter I
#     climax hinge.
#   - Aeron's "inheritance" frame must surface in a later private scene — possibly
#     with Lyra (devotion partner), who can receive the grief without trying to solve it.
#   - Noelle's implication arc escalates: phase 2 is "what does she do when her model
#     could be weaponized against Phoenix if she continues running it." This is the
#     Act 4 Noelle moral hinge.
#   - Marcus's bunker location — the consolidation target — becomes another scene seed.
#   - The care-as-unreadable-pattern thesis should echo in a later Tessa burden scene.
