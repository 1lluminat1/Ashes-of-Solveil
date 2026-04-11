# =======================================================
# ACT 4 - Scene 18: Rhea Arrives (Obedience Path)
# File: a4_s18_rhea_arrives_ob.rpy
# Path: OB
# Type: OPERATION / ANTAGONIST INTRODUCTION -- THE FIRST STRIKE
# Character Focus: Aeron, Nyra, Rhea Vestin (comms intercept)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s18_rhea_arrives_ob"
$ scene_mark(_current_scene_id, "entered")

# Local speaker for Rhea's comms intercept. Filter-coded -- clean, cold,
# unaffected. Same color as a4_s08 (8a95a4) for continuity.
define rhe = Character("Commander Rhea Vestin", color="#8a95a4")

label a4_s18_rhea_arrives_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, locked tripod for the ops-room coverage. The scene runs in
    #         a cold institutional register: symmetrical two-shots across the
    #         ops table, slow push-ins on the tac display when the strike
    #         reports come in, tight singles on Aeron and Nyra's faces during
    #         the moments of non-reaction. The comms intercept of Rhea is
    #         audio-only -- her voice enters the room from the intercept
    #         speaker; the camera does not leave the room to find her. She is
    #         a voice in the walls for this scene. The operation is watched,
    #         not participated in. Coverage stays inside the ops room for the
    #         entire duration of the strike. The helplessness is the coverage.
    # LIGHTING: Ops room at operational luminance. Tac display dominant --
    #           blue-white, the kind of light that does not flatter faces.
    #           Overhead strips at 60%. The room has the specific flat light
    #           of a command space that is currently observing an operation
    #           it cannot influence. No warm source anywhere in the frame.
    # SFX: Loop -- ops room ambient, low. Cooling fans, the tac display's
    #      processing sub-bass, the comms panel's carrier hiss. One-shots --
    #      the forward base priority ping (three tones, descending), the
    #      tac display update chimes as casualty reports land, the intercept
    #      click when Rhea's voice comes through, the moment of silence
    #      after she stops speaking, the chair Aeron does not take.
    # FX/COMP: Tac display shows the forward base at Sector 9-North -- the
    #          base Nyra authorized in a4_s02 as part of the sector
    #          consolidation. Seventeen assets deployed. The display updates
    #          in real time as the strike unfolds. Casualty markers appear
    #          one by one. The seven dead are tracked on the operational
    #          board that overwrote the medical board in a4_s06. Their names
    #          populate the OPERATIONAL-WITHDRAWN column. Jara Neese's name
    #          populates with a cross-reference tag: her name was on the
    #          Sector 12 operator roster from a4_s09. The cross-reference is
    #          not commented on in dialogue. The cross-reference is there.
    # BLOCKING: Phase 1 -- Aeron at the head of the ops table, standing.
    #           Nyra at the tac display, facing it. The room is otherwise
    #           empty. The priority ping arrives. Phase 2 -- both turn to
    #           the display. They watch. Phase 3 -- the comms intercept of
    #           Rhea. They listen. Phase 4 -- Aeron gives the pull-back
    #           order. Phase 5 -- the final casualty report. Phase 6 --
    #           the post-mortem line exchange between Aeron and Nyra. Phase
    #           7 -- Aeron alone at the ops table. Nyra has left. The tac
    #           display still showing the forward base footprint going dark.
    # CANON: Day after a4_s10 / concurrent with a4_s16-s17 Tessa beats.
    #        The 6-day Marcus clock from a4_s03 / a4_s08 has just closed
    #        early. Rhea Vestin makes her first strike. Unlike the EMP
    #        variant (a4_s16_rhea_strikes_emp) this is not a precision
    #        decapitation. This is a hard-mass kill against a forward base
    #        that Phoenix had just stood up as part of Nyra's Act 4
    #        consolidation schema. Seven dead. Clean Echelon win.
    # FACE: Aeron -- institutional face. The fracture under it is visible
    #        only to someone who has been watching the fracture. The face
    #        does not show the fracture, but the face does not move either.
    #        The non-movement is the fracture.
    #        Nyra -- operational face. The face of a woman who recognizes
    #        competence in an opposing force and is annotating the
    #        recognition in real time. Not frightened. Not impressed.
    #        Assessing. The assessment is its own register.

    # ========= VOICE BASELINE =========
    # OB Aeron: Minimal. Institutional. The pull-back order is issued in
    #           the same register he used to authorize the Sector 12 sweep.
    #           The voice does not change. The voice not changing is the
    #           thing the scene is holding.
    # Nyra: Co-commander. She reads the strike as a teaching moment. She
    #       names Marcus. Aeron corrects her. The correction is the scene's
    #       hinge.
    # Rhea Vestin (comms intercept): Clinical. Unbothered. No gloating.
    #       No acknowledgment of the dead. A window closed. A list executed.
    #       An instrument awaiting reassignment. The voice is the voice
    #       from a4_s08: "I do not require a briefing."

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE -- OPS ROOM -- 0417]
    # Four days after a4_s10. The 6-day Marcus clock has closed on day four.
    # Aeron has been in the ops room since 0402. Nyra has been at the tac
    # display since 0355. The forward base at Sector 9-North has been
    # operational for eleven days.

    #scene bg_ops_room_predawn with dissolve
    #play ambient "sfx/ambient/ops_room_low.ogg" fadein 2.0

    # ========== PHASE 1 -- THE PRIORITY PING ==========

    "The ops room is colder than the corridor. It has been colder than the corridor since Nyra's Act 4 restructure authorized the cooling increase on the crystal arrays that feed the tac display. The colder room produces cleaner readings. The cleaner readings produce cleaner decisions. The decisions are cleaner. The room is cold."

    "Aeron is standing at the head of the ops table. He has been standing at the head of the ops table for fifteen minutes. He has not yet sat."

    "Nyra is at the tac display. She is standing at a forty-degree angle to the display, the angle she uses when she is tracking two sub-sectors at once. Her left hand is on the edge of the display frame. Her right hand is at her hip, three fingers curled -- her standby posture."

    athought "She has not moved her right hand in eleven minutes."

    athought "That is the posture she goes to when the operational intuition she is not yet saying aloud is telling her the shift will not end quietly."

    athought "I have been watching her posture more than the display for six minutes."

    athought "The display has not shown anything yet."

    "The display shows the forward base at Sector 9-North at steady-state. Seventeen operator markers, green. Four perimeter arcs, clean. The forward base is the base Nyra authorized in the restructure. It is eleven days old. It is functioning."

    "It is 0417:04."

    #play sound "sfx/ops_priority_ping.ogg"

    "The priority ping arrives."

    "Three descending tones. The ops room's tonal signature for a forward-base priority event. The tones are loud enough to fill the room and short enough that the silence after them is louder."

    "Nyra's right hand leaves her hip."

    "Aeron walks three paces to the tac display."

    "Both of them are now in front of it."

    # ========== PHASE 2 -- THE DISPLAY UPDATES ==========

    # CAMERA: over-shoulder two-shot looking into the display. The display's
    # blue-white light on both faces. The casualty markers appearing one at
    # a time, small red dots replacing small green ones.

    "The display shows the forward base at Sector 9-North no longer at steady-state."

    "Perimeter arc three has gone dark."

    "Two operator markers at the eastern quadrant have gone from green to amber -- amber is the color the ops display uses for status-unknown, which in the forward base context is the color it uses for status-probably-dead. The amber state persists for an average of four seconds before the state resolves to either green or red."

    "The two amber markers resolve to red."

    athought "Two."

    "Nyra touches the tac display at the eastern quadrant. The touch brings up the operator manifest for the quadrant. Names appear in a column at the edge of the display."

    "The two red markers have names beside them."

    "HAREL VOST -- RUNNER."

    "DREN KALE -- SAPPER."

    nthought "(terse) Two."

    "Nyra does not speak. She is annotating internally. The annotation is her working register."

    "Perimeter arc two goes dark."

    "Three more operator markers at the central quadrant go amber."

    "Resolve to red."

    "SIRI ONDEL -- MEDIC TRAINEE."

    "TOMAS REILL -- LOGISTICS."

    "ELO VARIC -- COMMS."

    athought "Five."

    athought "Siri Ondel is the medic trainee Tessa has been mentoring."

    athought "Siri Ondel is on the board Tessa has been refusing to touch."

    athought "Siri Ondel is -- was -- nineteen. The roster has her age."

    athought "I am going to hold that detail for later. I am going to hold it because the operational surface of this room does not have room for it right now."

    athought "The holding is the thing I am now doing in my body. The face does not show the holding."

    "The face does not show the holding."

    "Perimeter arc one goes dark."

    "Two more operator markers resolve to red at the western quadrant."

    "MIRA TEV -- SCOUT."

    "JARA NEESE -- OPERATOR."

    athought "Seven."

    athought "Jara Neese."

    athought "Jara Neese was on the Sector 12 sweep roster. The sweep we signed off on last week. The three civilians on the list that Noelle's schema flagged as tertiary-confirmed."

    athought "Jara Neese was one of the three operators who executed the sweep."

    athought "Jara Neese killed three civilians on our order a week ago."

    athought "Jara Neese has just been killed."

    athought "The symmetry is not accidental. Rhea Vestin reads rosters the way Noelle reads rosters. Rhea Vestin has selected a strike team whose kill list has a specific overlap with our recent operations."

    athought "The overlap is a message."

    athought "The message is: I know who your operators are and I know which of them have been inside civilian kill radius this month."

    athought "The message is addressed to me."

    athought "The message arrives on my face exactly once, for a duration of approximately one-fifth of a second, and then the face stops receiving the message."

    "The face stops receiving the message."

    "Aeron does not look at Nyra."

    "Nyra does not look at Aeron."

    "Both of them are looking at the display."

    # ========== PHASE 3 -- THE INTERCEPT ==========

    # CAMERA: tight single on the comms panel's intercept indicator. The
    # indicator clicks from amber to green. The click is the only sound.

    #play sound "sfx/comms_intercept_click.ogg"

    "The comms panel's Ghostline intercept indicator clicks from amber to green."

    "Ghostline has pulled a clear audio frame from the opposing-force comms lattice. The frame is approximately eleven seconds long. The intercept software has tagged it as priority-one because the voice signature on the frame matches a voice signature the Ghostline database has flagged as operational-interest."

    "The voice signature matches Commander Rhea Vestin."

    "Aeron walks two paces to the comms panel."

    "Nyra does not move from the tac display."

    "Aeron touches the playback control."

    #play sound "sfx/comms_playback_start.ogg"

    # --- RHEA ON THE INTERCEPT ---

    "The intercept plays."

    "The voice that comes out of the speaker is the voice from a4_s08. Flat. Unbothered. Professional at a depth that does not require professionalism to sustain it."

    rhe "Window closed."

    rhe "Target list executed."

    rhe "Awaiting reassignment."

    "Eleven seconds in three sentences."

    "There is approximately two seconds of carrier hiss after the third sentence. The hiss is followed by a command-channel acknowledgment tone from whoever received the message on the Echelon side. The acknowledgment tone is the only evidence that the message was received."

    "The intercept ends."

    "The comms panel indicator clicks from green back to amber."

    #play sound "sfx/comms_intercept_end.ogg"

    athought "She did not gloat."

    athought "She did not acknowledge the dead. Not hers. Not ours."

    athought "Target list executed. The target list is the seven names that have just resolved to red on the display. The list is not a hypothesis for her. The list is a task she has completed. The completion is the only register she is deploying."

    athought "Awaiting reassignment. She is done with us. We are the item before the next item on her queue."

    athought "I am watching a woman whose relationship with killing is the relationship I have been trying to construct for myself for the last four weeks."

    athought "She has it. I am constructing it. The gap between having and constructing is the gap between her and me."

    athought "The gap is the gap Marcus has been trying to show me for four weeks."

    athought "Marcus was not trying to show me that I needed to become Rhea."

    athought "Marcus was trying to show me that Rhea exists."

    # --- NYRA HEARS THE INTERCEPT ---

    nthought "She is cleaner than we are."

    nthought "The cleanness is not a compliment. The cleanness is a diagnostic."

    nthought "Her operational voice has no residue. No residue means no processing. No processing means the kills do not sit in her body in any of the places kills sit in the bodies of people who have spent years developing the capacity to metabolize them."

    nthought "I have the residue. I am proud of the residue. The residue is the thing that separates me from what Rhea Vestin is."

    nthought "The residue does not help me reinforce the forward base."

    nthought "The residue is a thing I carry. The residue is not a thing I win with."

    nthought "I would trade the residue for reinforcement capacity."

    nthought "I notice that I would trade the residue."

    nthought "I do not tell Aeron that I would trade it."

    # ========== PHASE 4 -- THE PULL-BACK ORDER ==========

    # CAMERA: return to the tac display two-shot. The forward base is now
    # at eight operator markers -- green, amber, and ghost-grey for unknown
    # but presumed still in theater. The display's geometry has gone from
    # defensive posture to collapsing posture in under three minutes.

    "The tac display now shows eight operator markers at the forward base. Seven red, and the eight greens and ambers of the surviving assets. The geometry is no longer a defensive posture. The geometry is a collapsing posture. The ops room's tac software has begun to draw the collapse vectors in thin yellow lines."

    "Nyra looks at Aeron."

    "Aeron looks at the display."

    ny "Commander. The forward base cannot be reinforced in time."

    a "How long to extract the survivors."

    ny "Eleven minutes if we commit the quick-reaction force at Sector 9-South. Fourteen minutes if we commit the secondary QRF from the base."

    ny "The opposing force's disengagement window is approximately nine minutes."

    a "Nine."

    ny "Nine."

    a "The disengagement window is tight to the extraction window."

    ny "The disengagement window is shorter than the extraction window by two minutes minimum. Any QRF we commit arrives after Rhea Vestin has already left theater. They arrive to a site we do not hold, to recover assets we do not have eyes on, with no opposing force present to engage."

    ny "They arrive to collect bodies. And to be ambushed by any secondary element Rhea Vestin has left in place as a follow-up trap."

    a "Has she left a secondary element."

    ny "Probability estimate: sixty-two percent. I am basing the estimate on the three Ghostline pattern matches we have of her previous engagements. She uses secondary elements as ambush in approximately two out of three operations."

    a "The QRF would walk into an ambush."

    ny "The QRF would walk into a probable ambush for no recoverable operational gain."

    "Aeron is quiet for three seconds."

    athought "The three seconds are the three seconds I owe the seven dead."

    athought "I am giving them three seconds and then I am going to give the order."

    athought "The order is going to preserve the surviving assets at the cost of the dead not being recovered in the window."

    athought "The dead will be recovered later. The dead will be recovered when Rhea Vestin has been out of theater for long enough that a recovery team can enter without walking into her secondary element."

    athought "Later is an operational category. Later means the families do not see the bodies for three days minimum."

    athought "Siri Ondel's family will not see her body for three days."

    athought "The three days are the operational cost of not losing the QRF."

    athought "I am going to pay the three days."

    "The three seconds end."

    a "Pull the survivors back."

    ny "Route."

    a "East ridge corridor. Use the secondary extraction path from the a4_s02 schema. Do not commit the quick-reaction force from Sector 9-South. The QRF stays at Sector 9-South and holds position for any secondary Echelon element that follows this strike into our territory."

    ny "Understood."

    a "Bodies to be recovered on a forty-eight to seventy-two hour window after theater clears. Intelligence team to start pattern analysis on the Ghostline intercept immediately."

    ny "Understood."

    a "Comms silence with the survivors until they clear the east ridge. No heroics. No turnaround for recovery. They leave the dead."

    ny "Understood."

    "Nyra touches the tac display. The orders transmit. The display shows the survivors beginning the east ridge extraction route. The collapse vectors re-render in green."

    "The seven red markers remain where they are. The display does not remove the red. The red stays on the forward base footprint as the forward base footprint begins to dim. The red is a record."

    "The forward base at Sector 9-North goes dark at 0423:41."

    "Approximately six minutes from the priority ping to the going-dark."

    "Seven dead."

    # ========== PHASE 5 -- THE POST-MORTEM LINE ==========

    # CAMERA: symmetrical two-shot at the ops table. Aeron has walked back
    # to the head of the table. Nyra has walked from the display to the
    # long side. They are both standing. The table between them. The tac
    # display in the background, showing the dark footprint of the forward
    # base.

    "Nyra walks from the tac display to the ops table. Aeron walks from the comms panel to the head of the table. They arrive at the table within two seconds of each other. Neither of them sits."

    "The tac display is in the background of the shot. It is still showing the dark footprint of the forward base. The footprint is not going to be updated again until the survivors clear the east ridge or until a secondary element engages them, whichever comes first."

    "Nyra places her hands flat on the ops table. Fingers spread. The posture she uses when she is about to say a sentence she does not want to say softly."

    ny "This is Marcus telling us what happens when the student outpaces the teacher."

    "The sentence arrives at the ops table in the register Nyra uses for operational diagnostics. The register is not angry. The register is the register of a woman naming a thing correctly so that the thing can be worked with."

    "Aeron does not respond immediately."

    athought "She is wrong."

    athought "She is not wrong in the broad strokes -- Marcus is indeed telling us something. She is wrong about what he is telling us."

    athought "The student outpacing the teacher is the framing in which Marcus is the teacher and I am the student and the arc between us is a generational transmission of violence competence."

    athought "That framing has been my framing for four weeks. The framing is flattering to me because it places me on the upward slope of a curve that ends at Marcus."

    athought "The framing is wrong. Rhea Vestin is not on the curve between me and Marcus. Rhea Vestin is on a different curve entirely."

    athought "Marcus is not showing me that I am becoming him."

    athought "Marcus is showing me that there is a register of operational violence I have not yet touched. A register in which there is no residue. A register in which the dead do not sit in the body. A register in which the operator receives the reassignment on an eleven-second intercept and takes it."

    athought "Rhea has that register. Marcus does not. Marcus did once. Marcus can recognize the register when he sees it. Marcus has sent Rhea here because Rhea is the register he could not sustain past his own fortieth year."

    athought "Rhea is the register I cannot sustain at all. Not because I am better than Rhea. Because the register requires a construction I do not have the material for."

    athought "Marcus is telling me he has someone who is better than both of us."

    athought "That is the correction I am about to make to Nyra's diagnostic."

    athought "I am making the correction out loud because the correction is the thing I need the ops room to have on the record."

    a "No."

    "One word. The ops room's ambient hum is louder than the word for a half-second."

    ny "No."

    "Nyra's no is an acknowledgment. It is not a contradiction. It is the sound she makes when she is receiving a correction from Aeron and is about to hear the correction fully."

    a "This is not Marcus telling us what happens when the student outpaces the teacher."

    a "This is Marcus telling us he has someone who is better than both of us."

    "Twelve words."

    "The sentence lands on the ops table with the specific weight of a sentence that has been held in the body for the four weeks since Marcus's a4_s03 briefing and has only just now found the ops room to be said in."

    "Nyra does not respond for two seconds."

    nthought "He is right."

    nthought "I have been running the Rhea Vestin profile through my operational instinct for four days. The profile does not reconcile with the generational-transmission model. The profile reconciles with a different model. The different model is the one Aeron just named."

    nthought "There is a register of operational violence that does not carry residue. I have never met an operator who sustains that register past year five. I have heard rumors. I have read after-action reports. I have never seen one."

    nthought "I am watching the intercept of one tonight."

    nthought "Aeron is right."

    nthought "I am not going to tell him how right."

    nthought "I am going to hold the diagnostic for the after-action."

    ny "Acknowledged."

    "Not agreed. Acknowledged. The word Noelle used in the data alcove yesterday."

    "The ops room is quiet. The tac display's dark footprint. The seven red markers. The survivors moving on the east ridge."

    # --- TP SEED ---

    tp_seed("a4.ob.rhea.someone_better")

    # ========== PHASE 6 -- NYRA LEAVES ==========

    "Nyra looks at the tac display once more. The survivors are approximately two minutes into the east ridge extraction. The secondary QRF at Sector 9-South is at hold. The forward base footprint is not going to update again in this session."

    ny "I am going to Sector 9-South to coordinate the secondary element response if Rhea Vestin commits a follow-up."

    a "Go."

    ny "I will report at 0500."

    a "0500."

    "Nyra walks to the ops room door. She does not look back at the table. She does not look back at the display. The walk is the walk she uses when she is closing a thing off so that the thing does not follow her into the next room."

    "The door opens. The door closes."

    "Aeron is alone at the ops table."

    # ========== PHASE 7 -- AERON ALONE ==========

    # CAMERA: slow push-in. The tac display's dark forward-base footprint
    # behind Aeron's left shoulder. The head of the ops table. His hands
    # flat on the surface. Fingers spread. The same posture Nyra used.

    "Aeron walks from the head of the table to the long side -- the side Nyra was standing on. He places his hands flat on the ops table. Fingers spread. The posture."

    "He is standing where Nyra was standing. His hands are in the position her hands were in. He has not thought about this choice. The body has arranged itself into a posture the body knew how to arrive at from watching her."

    athought "Seven names."

    athought "Harel Vost. Dren Kale. Siri Ondel. Tomas Reill. Elo Varic. Mira Tev. Jara Neese."

    athought "The names are a list. The list is a thing I will not write down anywhere the ops room can see. The list is going to go on Tessa's board whether Tessa wants it there or not."

    athought "Tessa is going to know about Siri Ondel within an hour."

    athought "I will not be the one who tells her. The operational channel will tell her. Tessa is on the medical wing's duty roster at 0500. The casualty report will have been delivered to her station by 0445."

    athought "Tessa is going to know Siri Ondel was nineteen."

    athought "I already know Siri Ondel was nineteen."

    athought "I am holding the knowing in the way the ops room permits the knowing to be held, which is the way that does not show on the face."

    athought "The face does not show."

    athought "The face has been not-showing for four weeks."

    athought "The face is the thing Rhea Vestin has had longer than I have."

    athought "The face is not the register. The face is the surface of the register. Rhea has the register underneath the face. I have the face without the register. That is the gap."

    athought "I am going to have to decide what to do about the gap."

    athought "I am not going to decide it in the ops room at 0425."

    athought "I am going to decide it in the silence between now and when the survivors reach the east ridge waypoint."

    "The ops room is quiet except for the vent and the tac display's low hum."

    "The tac display shows the east ridge corridor. The survivors are progressing. Eight markers, green and amber, moving east."

    "Behind them, on the dark footprint of the forward base, the seven red markers remain. The display does not remove them."

    "The display keeps the record."

    # --- THE INSTITUTIONAL COLD ---

    athought "There is a line Marcus used in a4_s03 that I did not parse fully when he said it."

    athought "The line was: 'the long way home is a distance measured in what you have to not feel in order to make the trip.'"

    athought "I did not parse the 'in order to make the trip' clause."

    athought "I am parsing it now."

    athought "The clause is: there is a specific quantity of feeling you have to not-feel in order for the trip to continue to be makeable. The quantity is not a constant. The quantity increases with the length of the trip. The trip to the long way home requires a larger not-feeling than I had budgeted for when I started the trip."

    athought "Rhea Vestin is the not-feeling at its full quantity. Marcus is the not-feeling at the quantity he can sustain in his sixth decade. I am the not-feeling at the quantity I can sustain in the current week."

    athought "The quantity I can sustain is going to need to be larger tomorrow than it was today."

    athought "I am noticing that I have begun to think about the not-feeling as a capacity I am building, rather than a cost I am paying."

    athought "The framing shift is the corruption Noelle named in her author's note yesterday. She wrote the shift as a property of her own categories. The shift is also a property of mine."

    athought "The framing shift is the shift Marcus was disappointed by when he wrote me off in his library and called Rhea Vestin in early."

    athought "I am the student Marcus stopped teaching four days ago."

    athought "Rhea Vestin is the replacement instrument."

    athought "The replacement is better than I am."

    athought "The replacement does not mean I am withdrawn from the field. The replacement means Marcus now has two operators in his ops theater. One that he is currently teaching and one that he is currently overseeing from an honorific remove."

    athought "I am the one he is overseeing from a remove."

    athought "The remove is the thing that just killed seven of mine."

    athought "The remove is a distance measurable in seven names."

    "The tac display shows the east ridge survivors passing the first waypoint. The green and amber markers continue east. The forward base footprint remains dark. The seven red markers remain where they are."

    "Aeron does not move from the ops table."

    "The vent runs."

    # --- THE FINAL BEAT ---

    "Aeron reaches up to his collar. Adjusts the collar. The adjustment is a small deliberate motion. The collar did not need adjusting. The motion is the motion of a man whose body requires a small deliberate act to be performed by the body in order for the body to confirm that the body is still operating."

    "The collar is adjusted."

    "The hands return to the ops table. Flat. Fingers spread."

    athought "The question Marcus asked in a4_s03 was: 'what kind of commander are you willing to become.'"

    athought "The question the forward base at Sector 9-North just asked is: 'what kind of commander have you already become.'"

    athought "The two questions are not the same question."

    athought "The first question was about capacity. The second question is about inventory."

    athought "The inventory is: I am the commander who just gave a pull-back order, watched seven of mine resolve to red, and did not feel the second of the seven."

    athought "The first of the seven I felt -- Harel Vost, because I had not started counting yet."

    athought "I started counting at the second. Counting is the register that replaces feeling."

    athought "By the seventh I was not counting the dead. I was counting the gap between the disengagement window and the extraction window."

    athought "The gap is a number. The gap is nine minus eleven. The gap is negative two minutes."

    athought "I moved from the seven to the negative two in under forty seconds."

    athought "Rhea Vestin moves from seven to zero in no seconds at all."

    athought "I am on a curve. The curve has an endpoint. The endpoint is Rhea Vestin's zero."

    athought "Marcus wanted me to know the curve exists. Marcus wanted me to know the endpoint is a person who lives in the world, breathes the air, takes reassignments on eleven-second intercepts."

    athought "The lesson has been delivered."

    athought "The lesson cost seven."

    athought "The lesson is operational."

    athought "I am operational."

    "The tac display updates. The east ridge survivors pass the second waypoint. The markers are still green and amber. No secondary element has engaged. Rhea Vestin's disengagement window has closed cleanly."

    "The ops room ambient continues."

    "Aeron stays at the ops table."

    "The camera pulls back slowly through the ops room door. The door is closed. The camera is leaving the room through the closed door in the institutional coverage convention the scene has been using throughout. The ops room with the dark forward base footprint, the east ridge survivors, and the commander standing at the long side of the table with his hands flat, recedes. The vent runs. The tac display hums. The collar adjustment has already passed."

    "The base functions."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.rhea.first_strike", True)
    $ canon_set("ob.rhea.first_strike.dead", 7)
    $ canon_set("ob.rhea.first_strike.target", "forward_base_sector_9_north")
    $ canon_set("ob.rhea.named_dead", "Harel Vost, Dren Kale, Siri Ondel, Tomas Reill, Elo Varic, Mira Tev, Jara Neese")
    $ canon_set("ob.rhea.intercept_line", "Window closed. Target list executed. Awaiting reassignment.")
    $ canon_set("ob.aeron.pull_back_ordered", True)
    $ canon_set("ob.aeron.qrf_held_for_ambush_risk", True)
    $ canon_set("ob.jara_neese.dead", True)
    $ canon_set("ob.jara_neese.killed_sector_12_civilians", True)
    $ canon_set("ob.siri_ondel.dead", True)
    $ canon_set("ob.siri_ondel.age", 19)
    $ canon_set("ob.siri_ondel.was_tessa_mentee", True)
    $ metric("ob.marcus_clock", set_to=2)
    $ metric("ob.aeron.operator_death_count", add=7)
    $ rel_bump("Nyra", complicity=1)
    $ flag("a4_ob_rhea_first_strike", True)
    $ flag("forward_base_sector_9_north_lost", True)
    $ tp_seed("a4.ob.rhea.someone_better")
    $ npc_remember("Nyra", "student_outpaces_teacher_correction", tone="operational_diagnostic_acknowledged")
    $ npc_remember("Aeron", "seven_names_forward_base_loss", tone="counting_as_register")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s18_rhea_arrives_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - 0417 to 0430. Four days after the a4_s03/a4_s08 Marcus clock opens.
#   - Day after a4_s10 (Noelle doctrine drafting, blank signature).
#   - Concurrent with / immediately before a4_s19 Tessa state beat.
# cann.what_happened:
#   - The 6-day Marcus clock closes on day four. Rhea Vestin executes her
#     first strike against the Phoenix forward base at Sector 9-North --
#     the base Nyra authorized in the a4_s02 consolidation schema, eleven
#     days old. Seven dead in approximately six minutes.
#   - The seven: Harel Vost (runner), Dren Kale (sapper), Siri Ondel
#     (medic trainee, nineteen, Tessa's mentee), Tomas Reill (logistics),
#     Elo Varic (comms), Mira Tev (scout), Jara Neese (operator --
#     cross-referenced as one of the three operators from the a4_s09
#     Sector 12 sweep who killed the three civilians on Noelle's list).
#   - Ghostline intercepts eleven-second audio frame of Rhea Vestin:
#     "Window closed. Target list executed. Awaiting reassignment."
#     No gloating. No acknowledgment of the dead. The Rhea voice from
#     a4_s08 ("I do not require a briefing") extended into the field.
#   - Aeron cannot reinforce in time. Extraction window is eleven minutes;
#     disengagement window is nine. Nyra reports 62 percent probability of
#     a Rhea secondary ambush element. Aeron orders pull-back on the east
#     ridge corridor, holds the secondary QRF at Sector 9-South, leaves
#     the seven dead to be recovered in a 48-72 hour window. Bodies are
#     operational cost.
#   - Post-mortem exchange:
#     Nyra: "This is Marcus telling us what happens when the student
#           outpaces the teacher."
#     Aeron: "No. This is Marcus telling us he has someone who is better
#            than both of us."
#   - Nyra acknowledges (not agrees). She leaves for Sector 9-South to
#     coordinate secondary element response. Aeron alone at the ops table.
#     The tac display holds the dark forward-base footprint with the seven
#     red markers. The display keeps the record.
# cann.aeron_state:
#   - The face does not move. The not-moving is the fracture. He counts
#     the dead to the second, then switches registers from counting dead
#     to counting the disengagement/extraction gap. He moves from seven
#     to negative two (minutes) in under forty seconds.
#   - He notices mid-scene that he has begun to think about the not-feeling
#     as a capacity he is building rather than a cost he is paying. The
#     framing shift is the corruption Noelle named in her author's note.
#   - He recognizes Rhea Vestin as the register endpoint -- the operator
#     who moves from seven to zero in no seconds at all. He is on a curve;
#     Rhea is the curve's endpoint; Marcus is a waypoint.
#   - "I am the student Marcus stopped teaching four days ago. Rhea Vestin
#     is the replacement instrument. The replacement is better than I am."
#   - He holds the knowing about Siri Ondel but will not tell Tessa. The
#     operational channel will tell her. Sets up a4_s19.
# cann.nyra_state:
#   - Standby posture held for eleven minutes before the priority ping --
#     operational instinct detected the shift before the display did.
#   - Her interior acknowledges privately that Rhea has a register Nyra
#     has never seen sustained past year five. "I would trade the residue
#     for reinforcement capacity." She does not tell Aeron this.
#   - She delivers the "student outpaces the teacher" diagnostic. When
#     Aeron corrects her to "someone better than both of us" she receives
#     the correction with "Acknowledged" -- Noelle's word from a4_s10.
# cann.rhea_voice:
#   - Comms intercept only. Audio. Eleven seconds, three sentences, no
#     residue. "Window closed. Target list executed. Awaiting reassignment."
#   - She does not gloat. She does not acknowledge the dead. Her register
#     is the register Aeron is building toward and cannot sustain.
#   - First field appearance in OB. Continues the voice from a4_s08.
# cann.thematic_flags:
#   - THE GAP. Between having the register (Rhea) and constructing the
#     register (Aeron). The gap is measurable in seven names and in the
#     forty seconds it takes Aeron to switch from counting dead to counting
#     the extraction gap.
#   - SOMEONE BETTER THAN BOTH OF US. Aeron's correction of Nyra's
#     diagnostic. Marcus is not showing Aeron that Aeron is becoming him.
#     Marcus is showing Aeron that there exists a register he cannot reach
#     and that the register has a practitioner in the field.
#   - THE NON-RECOVERY. The bodies are left for 48-72 hours. The operational
#     cost is the families waiting three days. Aeron is paying the three
#     days. The payment is the register.
#   - THE JARA NEESE SYMMETRY. The operator who killed three civilians on
#     Aeron's order a week ago is dead on Rhea's order tonight. The
#     symmetry is a message. The message is addressed to Aeron. The message
#     is not commented on in dialogue.
#   - THE COUNTING REGISTER. Aeron moves from counting the dead (seven) to
#     counting the gap (negative two minutes). The register change is the
#     internal correlate of Noelle's author's note: the category is
#     expanding in order to cover the action.
# cann.character_moments:
#   - Aeron: standing at the long side of the ops table in Nyra's posture,
#     hands flat, fingers spread, body arranging itself into a shape the
#     body learned from watching her. The collar adjustment.
#   - Nyra: the eleven-minute standby posture before the ping. The
#     "Acknowledged" rather than "Agreed." The trade she would make for
#     reinforcement capacity that she does not tell Aeron about.
#   - Rhea: voice in the walls. Eleven seconds. No residue.
# cann.callbacks:
#   - a4_s02: Nyra's consolidation schema authorized the forward base.
#     The base is now lost.
#   - a4_s03: Marcus's briefing opens the 6-day clock. Rhea closes it on
#     day four. "The long way home" line is re-parsed interior.
#   - a4_s06: the operational board overwrote the medical board. The seven
#     dead populate the OPERATIONAL-WITHDRAWN column. Siri Ondel lands
#     on Tessa's board.
#   - a4_s08: Rhea's voice from the aeries spire ("I do not require a
#     briefing") extended into the field intercept.
#   - a4_s09: Jara Neese was on the Sector 12 sweep roster. The
#     cross-reference is not named in dialogue but is the scene's quiet
#     ironic doubling.
#   - a4_s10: Noelle's author's note on expanding categories. Aeron's
#     interior here explicitly names the framing shift as the same shift
#     Noelle named in her doctrine.
# cann.requires_followup:
#   - a4_s19: Tessa learns about Siri Ondel at 0445 through the casualty
#     report. Branches on ob.tessa.choice.
#   - a4_s20: Noelle's model failure and the second Noelle erotic. Her
#     doctrine was supposed to prevent this kind of loss. It did not.
#   - Nyra's trade-the-residue admission is sealed for Act 5.
#   - Rhea's "awaiting reassignment" is operational. She will be
#     re-tasked. The re-tasking is future scene material.
# cann.block_status:
#   - ANCHOR. Always plays on OB path. The Marcus clock closes here. The
#     replacement instrument is named here.
