# =======================================================
# ACT 4 - Scene 21: The Second Cut (Empathy Path)
# File: a4_s21_marcus_second_cut_emp.rpy
# Type: OPERATION / ESCALATION — Phase III council, the thesis under its hardest test
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s21_marcus_second_cut_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s21_marcus_second_cut_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Four movements.
    #         (1) Open on the Rhea Vestin operation. Cold, procedural. The package
    #             on the safehouse threshold. Static 35mm. The civilians finding it.
    #             No score. The whole sequence is ambient and diegetic until the
    #             moment the first civilian opens the envelope.
    #         (2) Zira's interdiction. Handheld, running. The one civilian who
    #             tries to turn the list over. Zira catches him at a checkpoint
    #             two blocks out. Not a fight — a redirect. The camera is at her
    #             shoulder. Short sequence. She returns the man and the list.
    #         (3) Marcus intercept. 85mm on Marcus. Single shot, no coverage. He
    #             is in a grey room with a grey desk and no visible Echelon
    #             insignia. A pale grey-blue wash. He is looking at a tablet with
    #             a feed of the safehouse. He has one line. The line is for the
    #             audience, not for anyone in the room with him.
    #         (4) Phoenix council. 40mm, wide, the council room at the secondary
    #             base. Five principals around the table — Aeron, Selene, Noelle,
    #             Lyra, Tessa. Zira joins from a field station by voice-only comm
    #             partway through — her icon at the center of the table's comms
    #             plate, her voice in the room. There is a sixth chair at the
    #             head of the table. Nobody is in it. Nobody moves it. The sixth
    #             chair is the scene's load-bearing blocking element.
    # LIGHTING: Safehouse — grey daylight through dirty windows. Rhea's grey room
    #           — pale grey-blue wash, no practicals. The council room — morning
    #           light through the eastern window, cold and honest. The council
    #           room is brighter than any other room in Act IV so far. The scene
    #           is not playing hide-the-ball. It wants the decisions to be visible.
    # SFX: Safehouse — children's voices in the next room, a pot on a stove, the
    #      sound of a piece of paper being unfolded. The envelope-opening is the
    #      scene's first load-bearing sound. Rhea's room — silence. The council
    #      room — the small sounds of a council room in the morning. A cipher
    #      plate humming, a datapad settling, the cap of a water flask. No score
    #      until the decision is made. One held string at the "move the network"
    #      beat. Low.
    # FACE: Aeron — the test face. The thesis is on the table in front of him
    #       and he is not going to perform the thesis — he is going to apply it.
    #       Selene — recognizing. She has seen this face before. She is letting
    #       him have it.
    #       Noelle — the framework face. She is already thinking in sectors and
    #       in hours and in hand-to-hand civilian moves. She is ahead of the
    #       decision and is going to slow herself down to the decision's pace.
    #       Lyra — the blessing face. Not religious. The face of a woman who
    #       knows how to name when a decision is a correct decision and a face
    #       she uses for that naming.
    #       Tessa — the field-clinic face. She is thinking in triage from the
    #       moment the briefing starts. She is counting beds.
    #       Zira — voice only. Her voice does the face-work.
    #       Marcus — the student-teacher face. The face of a man watching his
    #       teacher make a move he did not think the teacher still had in them.
    # BLOCKING: Safehouse — interior. Rhea's room — interior. Council room —
    #           five around the table, sixth chair empty. Aeron takes a side seat
    #           as in s14. He does not take the head. Nobody takes the head.

    # ========= VOICE BASELINE =========
    # EMP cadence. The council room is the densest dialogue scene in Phase III.
    # Every principal speaks. The cadence is not rushed — it is council cadence,
    # which means the silences between speakers are as load-bearing as the
    # speech. Aeron speaks less than anyone might expect. The delegation is
    # written in. Marcus's one line is written for the audience.

    # scene bg_safehouse_sector11_morning with dissolve
    # play ambient "sfx/ambient/safehouse_kitchen_morning.ogg" fadein 2.5

    # ========== PHASE 1 — THE SAFEHOUSE ==========

    "The safehouse is in Sector 11."

    "It is a second-floor flat above a shuttered tailor shop, set up by Phoenix's civilian network six weeks before Act I opened. It houses fourteen civilians tonight — nine adults and five children, none of them Phoenix operatives, all of them people whose names are in Echelon's watch-list because of a family member or a neighbor or a cousin's political affiliation."

    "The Phoenix runner assigned to the safehouse is a nineteen-year-old named Paela Venn. Paela has been running the safehouse for eight days. She has been doing a good job."

    "At oh-seven-forty in the morning, Paela Venn opens the front door to take out the trash and finds an envelope on the threshold."

    "The envelope is manila. Letter-sized. Unmarked on the front except for one word in black ink, printed in block capitals by a steady hand:"

    "SOON."

    "Paela stares at the word."

    athought "(Paela's internal voice, the scene's one non-principal interiority.) I am looking at the word SOON on an envelope on the threshold of a safehouse Echelon is not supposed to know exists, and I am a nineteen-year-old runner, and I do not know what the correct shape of the next sixty seconds is."

    "She picks up the envelope. She closes the door behind her. She goes back up the stairs."

    "She does not open the envelope in the stairwell because the stairwell is not a room where you open an envelope that has SOON on it. She takes it into the kitchen and she sets it on the table and she sends a three-word text to her cell lead: {i}package on door.{/i}"

    "The cell lead replies in six seconds: {i}open it. i am on my way.{/i}"

    "Paela opens the envelope."

    "The envelope contains three sheets of plain paper. The three sheets are a printed list. The list is names. The list is names and operational callsigns and ID numbers and last-known addresses, and at the top of the list is a header she reads before she reads any of the names themselves:"

    "PHOENIX CELL — SECONDARY BASE OPERATIONS — REAL IDENTITIES — COMPILED AS OF YESTERDAY."

    "Paela reads the first name on the list."

    "The first name is her own real name."

    "The second name is Paela's sister's name — her sister, who is not a runner, who is not in Phoenix, who runs a bakery in Sector 3."

    "The third name is the runner who replaced Paela on the night shift two nights ago, a man named Kerrin Vel."

    "The fourth name is Kerrin Vel's infant son's name."

    "Paela sits down at the kitchen table because her knees have decided sitting down is the correct physical response to the list."

    "In the other room, two of the safehouse's children are arguing over a plastic cup."

    "The kitchen smells like last night's stew."

    "Paela puts the list face-down on the table and she is not going to cry because crying is not the correct shape of the next sixty seconds either. She is going to wait for her cell lead and she is going to do the next thing her cell lead tells her to do."

    # ========== PHASE 2 — THE CIVILIAN WHO BREAKS ==========

    "One of the nine adults in the safehouse is a man named Oris Telm."

    "Oris Telm is fifty-seven years old. He is not a Phoenix operative. He is in the safehouse because his daughter's husband was named on an Echelon detention list three weeks ago, and the extended family was pulled into the Phoenix civilian network as a protection measure. Oris has a weak heart. He has been on the safehouse's anxiety-adjacent medication since day two."

    "Oris sees Paela sit down at the table."

    "Oris sees the three sheets of paper."

    "Oris, who has not been eating well for six days, picks up the three sheets of paper from the table before Paela thinks to grab them back."

    "He reads the header. He reads four names. He drops the sheets back on the table."

    "Oris Telm turns and walks out of the kitchen and down the stairs and out the front door of the safehouse."

    "Paela is up from her chair a second too late."

    "She is halfway down the stairs when Oris is already around the corner."

    athought "(Paela again, one beat.) He is going to take the list to Echelon. He is going to try to give them the list first so his family's names are the names they did not need to read. He is going to do it because he thinks giving them the list is how you buy mercy out of a system that has the list in the first place."

    "Paela sends a second text to her cell lead: {i}runner out — oris telm — list — sector 11 toward east checkpoint.{/i}"

    "The cell lead forwards the text."

    "It lands in Zira's earpiece ninety seconds later."

    # ========== PHASE 3 — ZIRA'S INTERDICTION ==========

    # scene bg_sector11_checkpoint_morning with dissolve
    # play ambient "sfx/ambient/sector11_street_morning.ogg" fadein 1.5

    "Zira is at a runner station four blocks from the safehouse when the text comes through."

    "She does not say anything into her comm. She hands her coffee to the runner beside her and she goes."

    "She is not running fast. Runners do not run fast in the open in the daytime — that is the kind of running that makes you the subject of a silhouette file. She is walking fast enough to cover four blocks in two and a half minutes and she is holding her face in the configuration of a woman who is late to work."

    "She catches Oris at the corner of Third and the east checkpoint avenue. He is eight steps from the checkpoint line. The checkpoint line has two Echelon guards on it at this hour and one of them is already looking at Oris because a fifty-seven-year-old man walking toward a checkpoint with paper in his hand and his face the wrong color is a thing Echelon guards are trained to look at."

    "Zira does not run."

    "She walks up behind Oris and she puts her hand on his shoulder — not hard — and she says two words loud enough for the guard to hear:"

    z "Dad. Stop."

    "The guard's eyes move off Oris."

    "Oris freezes. Zira puts her arm around his shoulders the way a daughter puts her arm around a father who is wandering. She turns him a full one-eighty. She walks him back up the avenue. Her voice is small and close to his ear."

    z "I know what you are holding. I know why you are walking. I am not going to take it from you on the street. You are going to walk with me two blocks and we are going to take a left and we are going to be inside a door that is not the checkpoint and you are going to sit down and I am going to make you a cup of tea and then we are going to talk."

    o "They are going to use my family's names."

    z "I know."

    o "If I bring them this they might not."

    z "They are going to use your family's names whether or not you bring them this. That is the part you did not know when you left the safehouse. I have watched them do it to seven families this year who brought them things trying to buy mercy. The mercy never comes. The list comes and the names get used and the families find out afterward that the bringing was the thing that told Echelon which names were the important ones."

    o "Then what do I do."

    z "You come back with me. You come back with me and we move the safehouse before sundown and we move your family's names off every list we can move them off of. The moving is the thing that works. The bringing is the thing that does not work. That is all I know. I have known it for ten years and I am not going to know it differently today."

    "Oris Telm stops walking."

    "Zira does not push him. She stands at his shoulder with her hand on his upper arm and she lets him be still. He is crying. He is trying not to cry in public and he is not succeeding and Zira is not narrating his failure to succeed."

    o "Okay."

    z "Okay. Give me the list."

    "He gives her the list."

    "She folds the three sheets into quarters and puts them inside her jacket against her ribs where the fold is safe. She walks Oris back to the safehouse. She does not leave him at the door — she goes up the stairs with him and she hands Paela the list and she looks at Paela for the length of one breath and the look is the look of a runner telling a runner {i}you did the thing right, you sent the text, you are nineteen and you did not let this get worse than it had to get.{/i}"

    "Paela's shoulders drop one inch."

    "Zira says one sentence to the whole room."

    z "We are moving. Everybody. Forty-eight hours. Start packing the things you can carry and leave the things you cannot."

    "Then she goes back out the door to call the council."

    # ========== PHASE 4 — THE INTERCEPT ==========

    # scene bg_marcus_grey_room_morning with dissolve
    # play ambient "sfx/ambient/grey_room_silence.ogg" fadein 2.0

    "Cut to Marcus."

    "The grey room has no window. Marcus is at a grey desk with a tablet in front of him. The tablet is showing a low-resolution feed of the safehouse interior — Paela at the table, Oris at the table, the children in the next room, the unopened envelope now opened and the list in a small fold on the table."

    "The feed is not from inside the safehouse. The feed is from a building across the street. The camera has been in place for three days, installed by a surveillance team that had no orders other than to watch."

    "Marcus is watching Paela's shoulders."

    "He is not watching her face. He is watching the posture of a nineteen-year-old runner at a kitchen table with a list on it. He has watched postures at kitchen tables before. He has watched postures at kitchen tables for twenty years."

    "Rhea Vestin is in the room with him, standing one step back from the desk. She is not speaking. She knows this part of the operation is not hers."

    "Marcus speaks without turning to Rhea. His voice is quiet and carries the shape of a sentence he is saying more to himself than to her."

    m "He is learning."

    "A beat."

    m "I wonder if he will learn the rest of it."

    "Rhea does not ask what {i}the rest of it{/i} is. Rhea has worked with Marcus for long enough to know that when Marcus says a sentence with that kind of shape, the sentence is not for her — it is a sentence Marcus is filing for himself. She stands at her step and she watches the tablet with him."

    "The feed holds on Paela's shoulders."

    "Then the feed cuts to the street, to Zira walking Oris back toward the safehouse with her hand on his arm. Marcus watches that too. He does not frown. He does not smile. He is cataloguing."

    m "The runner is good."

    m "She walked him. She did not tackle him."

    m "She is going to move the network before sundown and she is going to do it by hand because the network has been told not to use a lot of comm traffic and she is the kind of runner who remembers the instruction."

    "Another beat."

    m "I would have liked to work with her. In a different life. In a different life I would have run an operation and she would have been on the team and I would have trusted her to walk people back from checkpoints, and the operation would have been the kind that you could tell your sister about."

    "He sets the tablet down."

    m "That is not this life."

    "He turns off the feed. The grey room goes quiet."

    # ========== PHASE 5 — THE COUNCIL CONVENES ==========

    # scene bg_council_room_secondary_base_morning with dissolve
    # play ambient "sfx/ambient/council_room_morning_low.ogg" fadein 2.5

    "Cut to the council room at the secondary base."

    "The council room is a long room with a long table. The table has six chairs at it — five chairs along the sides and one chair at the head. Aeron has been in this room twice before in Act IV. The first time he sat at the head because nobody had told him not to. The second time he sat at a side chair because Selene had rearranged the cipher plate to be in the center of the table instead of at the head and Aeron had taken the cue."

    "This morning Aeron walks in and the cipher plate is in the center of the table, and the chair at the head is empty, and nobody has moved the chair."

    "He takes a side seat."

    "Selene takes the side seat across from him."

    "Noelle takes the seat to Aeron's left. She has a datapad and a hand-log and the hand-log is already open to a blank page."

    "Lyra takes the seat to Selene's right. Lyra does not bring papers to council meetings. Lyra brings her hands."

    "Tessa takes the seat beside Lyra. Tessa has her clinic datapad and a folded piece of paper on which she has written the current bed count in the secondary base's medical area. The count is in her own hand and she does not show it to the room yet. It is a reference for when the room gets to her question."

    "The fifth seat — at the far end of the side opposite Selene — stays empty. It is Zira's seat. Zira is in Sector 11."

    "The chair at the head of the table stays empty."

    "Aeron looks at the empty chair at the head for exactly one beat."

    athought "The chair is empty."

    athought "Nobody is going to sit in it. I am not going to sit in it. Selene is not going to sit in it. The chair is the shape of a piece of shared authority I am still learning how to hold and the chair being empty is the pedagogy of the morning."

    athought "Okay."

    "He turns to Noelle."

    a "Brief the room."

    # ========== PHASE 6 — THE BRIEFING ==========

    "Noelle activates the cipher plate. The plate projects a low-res pattern onto the center of the table — not a map, not a schematic, just a framework graph showing the civilian network's current distribution across the sectors. Eleven green nodes. The eleventh node is Sector 11's safehouse. It is blinking."

    n "At oh-seven-forty this morning, a package was delivered to the Sector 11 safehouse. The package contained three printed sheets of plain paper. The sheets were a list of Phoenix operative real names, operational callsigns, ID numbers, and last-known addresses, current as of yesterday. The header of the list read: Phoenix cell — secondary base operations — real identities — compiled as of yesterday."

    n "The envelope had one word on the front. The word was SOON."

    "A beat. Tessa's breath goes out of her in a controlled exhale. Lyra's hands, which have been in her lap, move to the surface of the table, palms down, fingers spread. Selene does not move."

    n "The package was not a weapon. The package was a message. The message's recipients were the civilians in the safehouse — nine adults, five children, none of them Phoenix operatives. The message's author is Rhea Vestin, operating on Marcus's authority. I have confirmed the authorship by signal triangulation from the surveillance camera installed across the street from the safehouse three days ago."

    n "Rhea has known about the safehouse for three days. She did not raid it. She allowed it to continue operating under surveillance for three days. Then she delivered a list of Phoenix real names to it."

    n "One civilian — Oris Telm, fifty-seven — panicked when he saw the list and tried to turn it over to Echelon at the east checkpoint. Zira intercepted him at the corner of Third and the checkpoint avenue. She walked him back to the safehouse without incident. The list is now in Zira's possession. The civilians are still in the safehouse. No raid has occurred. No shot has been fired."

    n "Operationally, this is a draw."

    n "Tactically, it is worse than a draw. The fact that Rhea has our real names means the next strike will be surgical on humans, not on infrastructure. Rhea is telling us she can choose which of our people she deletes and when, and the one word on the envelope is telling us she is choosing her window."

    "Noelle closes the briefing projection. The plate's projection fades. The room's light is just the morning light again."

    n "That is the briefing."

    # ========== PHASE 7 — THE TEMPTATION ==========

    "A long beat."

    "The first person to speak is not Aeron. The first person to speak is Selene."

    sel "There is a version of the next twelve hours where we strike Rhea Vestin's personnel first."

    sel "I want it on the table because if I do not put it on the table we will pretend it was not on the table later and I do not run rooms that pretend."

    sel "Rhea's field team is eleven people. Seven of them are at locations we already know. The other four can be located inside six hours. We have precision assets that can take out all eleven in a synchronized window. The operation is within our capability. It will not save the network in Sector 11 — we will still have to move the network — but it will remove Rhea's ability to run the next list and it will give us ten days before Echelon regenerates a comparable capability."

    sel "The cost is ten days. The price is eleven lives that are not Echelon command — they are Echelon personnel. Some of them are career operators. Some of them are young. The seven I have locations on, I do not have ages on four of them."

    sel "I am putting it on the table. I am not recommending it. I am putting it on the table because the room has to see the option in order to refuse the option and the refusing has to be a refusing we own."

    "Selene sets her hand flat on the table beside the cipher plate."

    "Aeron looks at the hand."

    athought "That is the delegation-pattern from s05. That is Selene showing me the shape of a call she could have made unilaterally and bringing it into the room instead because the room is supposed to be where the call gets made. That is her lesson and she is running it on herself in front of me."

    athought "I am going to match her."

    # ========== PHASE 8 — AERON DELEGATES THE QUESTION ==========

    a "Thank you."

    a "I am not going to take the option off the table with an answer. I am going to take it off with a question."

    "Aeron looks around the room. At Noelle. At Lyra. At Tessa. At Selene. At the empty chair at the head of the table for one beat and then back to the room."

    a "What does mercy look like when the enemy has your family's names."

    "He lets the question sit."

    "Nobody answers immediately."

    "Noelle is the first to try. She is Noelle. She tries to answer every question."

    n "I have three framework answers. I am going to say all three out loud and I am going to say out loud that I do not trust any of them to be the answer."

    n "One: mercy is the refusal to escalate. We do not strike Rhea's personnel. We move the network. We absorb the cost. The frame is: mercy is the shape the enemy's hand does not dictate."

    n "Two: mercy is the surgical removal of the hand that is holding the names. We strike Rhea's personnel because removing Rhea's hand is the only way to give our family's names a future that is not the future Rhea is currently writing. The frame is: mercy is sometimes the knife, because the knife is the thing that stops the writing."

    n "Three: mercy is the decision that there is no answer to the question. Mercy is the act of sitting in the room with the question and refusing to let the question become a tactical problem, because the moment the question becomes a tactical problem it stops being the question."

    n "I do not trust any of the three. I am offering them because the room asked for framework."

    "A beat."

    "Lyra speaks next. Lyra is always next. Lyra's voice is the voice that makes a room stop performing and start listening."

    l "The room does not have an answer to the question."

    l "That is the correct outcome of the question."

    l "The question is not a question whose job is to be answered. The question is a question whose job is to be carried."

    l "Aeron asked us what mercy looks like when the enemy has your family's names and the room does not have an answer because there is no room anywhere that has an answer. There are rooms that pretend to have answers. Those rooms pretend by answering quickly. This room is not going to pretend."

    l "We are going to sit with the question for the rest of the act. We are going to sit with it while we move the network. We are going to sit with it while we hold the safehouses. We are going to sit with it while we write Davel Ostra on the board and any name that comes next. The question is going to be in the room with us the whole time and the question is going to make every decision a little harder and a little slower and a little more expensive."

    l "That is what mercy looks like when the enemy has your family's names. It looks like a question we refuse to convert into a problem we can solve."

    "Lyra lifts her hands off the table."

    "She folds them back in her lap."

    "That is the whole of her turn."

    "Tessa speaks third."

    t "I have the field-clinic question."

    t "Noelle's frame one says {i}we move the network and absorb the cost.{/i} I am the person who is going to absorb the cost on my side of the building. I want to say out loud what the cost is so the room does not approve the move without knowing what it is approving."

    t "Moving fourteen civilians in forty-eight hours by hand through three sectors is going to produce injuries. Elderly patients with pre-existing conditions are going to decompensate. I have one civilian with a weak heart on medication and I do not know if his medication is going to be in the new location in time. I have a pregnant woman in the Sector 6 safehouse at thirty-one weeks and I am going to have to move her and I am going to be one paramedic with a field kit and a good prayer."

    t "I am not saying do not move them. I am saying: if you approve the move, you are approving injuries and a non-zero number of non-combat deaths. I want the room to know what it is approving."

    t "I am going to run the field clinic for the move. I will set up three staging points — one per sector — and I will run triage across them. I need two runners assigned to each staging point and I need medical priority on any supply I flag. I am writing the list now."

    "Tessa unfolds her piece of paper and sets it on the table. The list is already started. She was writing the list in her head on the walk over."

    "Selene takes the list. Reads it. Nods once."

    sel "Approved on my authority. I will assign the runners."

    # ========== PHASE 9 — ZIRA JOINS BY COMM ==========

    "Noelle taps the comms plate. The icon at the center of the table activates."

    "Zira's voice comes into the room."

    z "I am here. I have been on the comm for the last six minutes."

    a "Status."

    z "The Sector 11 safehouse is packing. Fourteen civilians. I have Paela running the floor because Paela is nineteen and competent and the civilians trust her. I have the list in my jacket. Oris Telm is sitting on a chair in the kitchen and he is ashamed and he is not in a state to move himself. I will carry him if I have to."

    z "I heard Tessa's list. I can run the three-sector move. I am going to need runners and I am going to need the medical priority. I am going to need somebody to bless the decision before I start moving, because I am not going to move fourteen civilians and leave a trail Rhea can follow without the whole room being on the decision."

    z "I am asking the room to say the decision out loud so I can quote the room to my runners."

    "A beat."

    "Aeron looks at Selene."

    "Selene looks back."

    "Aeron nods once."

    # ========== PHASE 10 — THE DECISION ==========

    a "The decision is: we move."

    a "We do not strike Rhea's personnel."

    a "We do not take the ten days. We take the question."

    a "We take the question because the question is the shape mercy has when the enemy has our family's names, and the question is the thing we are going to carry, and the carrying is the work."

    a "Noelle will write the move-framework. Lyra will bless it before we execute. Zira will run it on the ground. Tessa will run the field clinic across the three staging points. Selene will command alongside me."

    a "We move at oh-eight-hundred. We finish by oh-eight-hundred in forty-eight hours."

    a "That is the decision."

    "Another beat."

    "Selene speaks."

    sel "Approved on command authority, joint, both signatures."

    "Noelle speaks."

    n "Framework drafting now. I will have the first version in ninety minutes."

    "Lyra speaks."

    l "I bless the move. I will bless it again in the chapel before the first civilian leaves the first door. I will bless it a third time at the last door. That is the shape of my blessing."

    "Tessa speaks."

    t "Field clinic is standing up now."

    "Zira speaks, from the comm."

    z "Copy. Moving."

    "Aeron looks around the table."

    "Five principals. One voice on the comm. A sixth chair empty at the head of the table."

    "He is not at the head. Nobody is at the head. The chair at the head has been empty for the entire scene."

    athought "This is the room."

    athought "The room with no head. The shape of the thing this act was supposed to build."

    athought "I did not build it alone. I did not build it from the head of a table. I built it by not taking the head of the table for enough mornings in a row that the head of the table stopped being the shape the room took."

    athought "That is the pedagogy. That is what delegating the question looks like in a room. You ask a question that does not have an answer and you sit at a side chair and you let the room carry the question with you, and nobody is at the head because the question is at the head."

    athought "The question is at the head of the table."

    athought "Mercy is what we do while the question is at the head of the table."

    "He reaches for his water flask. He uncaps it. He drinks."

    "Nobody says anything for a long beat."

    "Then Selene stands up."

    sel "Move."

    "The room moves."

    # ========== PHASE 11 — THE CLOSE ==========

    # scene bg_council_room_emptying_late_morning with fade
    # play ambient "sfx/ambient/council_room_after_low.ogg" fadein 3.0

    "The council room empties in the order the room's work requires."

    "Noelle first — she has a framework to draft and the framework is going to take ninety minutes and Noelle does not delay work she has a clock on. She leaves the room with her hand-log under her arm and a shape of the next ninety minutes already unfolding in her head."

    "Tessa second — she has a field clinic to stand up across three sectors and she is going to start by making a supply list and then moving to the main medical area to brief the medics on her shift. The clip lamp over the board is going to be on when she gets there. She is going to cap the marker before she leaves because the board has its own rule and the rule does not pause for an operation."

    "Lyra third — she goes to the chapel because Lyra's work begins in the chapel. Her blessing is going to be the shape her hands make over the framework when Noelle brings the framework to her, and her hands are going to be ready in the chapel when the framework arrives."

    "Zira does not leave the room because Zira is not in the room. Her voice disconnects from the comm with a small click and the icon at the center of the cipher plate goes dark."

    "Selene is the last to stand beside Aeron. She is halfway to the door when she pauses and turns."

    sel "Aeron."

    a "Yes."

    sel "You delegated the question."

    a "I did."

    sel "That is the lesson I have been waiting to see you learn."

    sel "You learned it by not taking the head of the table and by asking a question that did not have an answer. You did not learn it by solving the problem. You learned it by refusing to let the problem be a problem."

    sel "Chapter four. We are inside it now. Not just the name."

    "Aeron does not answer."

    "Selene does not wait for an answer. She turns and leaves the room."

    "Aeron is alone at the side chair."

    "The cipher plate is still on the center of the table, dim. The empty chair at the head of the table is still empty. The morning light through the eastern window has moved a hand-width across the table since the briefing began."

    athought "I am going to sit here for one more minute."

    athought "I am going to sit here for one more minute and I am going to say the question to myself in my head and I am going to not try to answer it."

    athought "What does mercy look like when the enemy has your family's names."

    athought "I am not going to answer."

    athought "The question is at the head of the table."

    athought "I am at a side chair."

    athought "That is the shape the act has built. That is the shape I am going to carry into the next hour and the next hour and the next one until the question is either answered by something that is not me, or the question has been carried long enough that the carrying is the answer."

    "He stands up."

    "He leaves the room."

    "The camera holds on the empty council room for three beats. The cipher plate, dim. The empty chair at the head of the table. Five side chairs pushed back. The sixth side chair — Zira's — never occupied this morning."

    "The morning light moves another inch."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=1)
    $ rel_bump("Noelle", trust=1)
    $ rel_bump("Lyra", trust=1)
    $ rel_bump("Tessa", trust=1)
    $ rel_bump("Zira", trust=1)
    $ canon_set("echelon.rhea.second_cut", "names_delivered")
    $ canon_set("phoenix.civilian_move", "in_progress")
    $ canon_set("council.empty_head_chair", True)
    $ canon_set("aeron.delegated_the_question", True)
    $ flag("a4_council_room_with_no_head", True)
    $ flag("oris_telm_intercepted", True)
    $ flag("paela_venn_holding", True)
    $ npc_remember("Selene", "named_the_lesson_after_the_council", tone="witnessed_it_happen")
    $ npc_remember("Marcus", "watched_paela_shoulders", tone="in_a_different_life")
    $ tp_seed("a4.aeron.room_with_no_head")
    $ metric("marcus_clock_hit", add=1)
    $ metric("aeron_delegate_the_question", add=1)
    $ metric("phoenix_civilians_in_motion", set_to=14)
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s21_marcus_second_cut_emp
# cann.chapter: Act IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Morning after the Phase III night of erotic beats. Oh-seven-forty, the
#     Sector 11 safehouse. Council convenes at approximately oh-eight-thirty
#     at the secondary base. Decision is executed at oh-nine-hundred, with a
#     forty-eight-hour window for the civilian move.
# cann.what_happened:
#   - Rhea Vestin delivers a printed list of Phoenix operative real names,
#     callsigns, IDs, and addresses to the Sector 11 safehouse. Envelope has
#     one word on the front: SOON. The package is not a weapon. It is a
#     message.
#   - Paela Venn (19, runner) opens the envelope. Oris Telm (57, civilian,
#     weak heart, extended-family asylum) panics and tries to turn the list
#     over to Echelon at an east checkpoint. Zira intercepts him, walks him
#     back, takes the list. No shot fired. No raid. Tactically a draw;
#     strategically worse — Rhea has the real names.
#   - Marcus intercept: a grey room, Marcus watching Paela's shoulders on a
#     feed, one line for the audience — "He is learning. I wonder if he
#     will learn the rest of it." — and a secondary beat where Marcus
#     catalogues Zira as "the kind of runner I would have worked with in a
#     different life."
#   - Phoenix council at the secondary base. Five principals around the
#     table: Aeron, Selene, Noelle, Lyra, Tessa. Zira joins by comm.
#     The chair at the head of the table is empty. Nobody takes it. Nobody
#     moves it. Aeron takes a side seat.
#   - Selene puts the revenge option on the table: strike Rhea's personnel
#     first, eleven lives, ten days of Echelon regeneration. She does not
#     recommend it. She puts it on the table so the room can refuse it
#     explicitly — delegation-pattern from s05 running on herself.
#   - Aeron refuses the option by delegating the question: "What does mercy
#     look like when the enemy has your family's names?" Noelle offers three
#     framework answers and says she does not trust any of them. Lyra names
#     the correct outcome: the room does not have an answer, and that is
#     the correct outcome of the question, because the question's job is
#     not to be answered — its job is to be carried. Tessa names the
#     field-clinic cost of the move.
#   - Decision: move the civilian network across three sectors in 48 hours
#     by hand. Noelle drafts the framework. Lyra blesses it. Zira runs it.
#     Tessa runs field clinic. Selene commands alongside Aeron.
#   - Selene names the lesson after the council empties: "You learned it by
#     not taking the head of the table and by asking a question that did
#     not have an answer. You did not learn it by solving the problem. You
#     learned it by refusing to let the problem be a problem. Chapter four.
#     We are inside it now. Not just the name."
# cann.aeron_state:
#   - Test passed. The thesis holds under its hardest Phase III pressure.
#     Aeron does not take the head of the table, does not approve the
#     revenge strike, and delegates the question to the room. The room
#     does not give him an answer. That is the correct outcome and he
#     accepts the correctness of the non-answer.
#   - Internal articulation: "The question is at the head of the table.
#     Mercy is what we do while the question is at the head of the table."
#     This is the Act IV thesis in load-bearing form and Aeron says it to
#     himself for the first time in this scene.
# cann.path_tracking_mechanics:
#   - EMP. No player choice. Linear.
#   - rel_bump for all five LIs +1 trust. The council room is relationship-
#     load-bearing for every principal.
#   - canon_set echelon.rhea.second_cut "names_delivered" — Rhea's second
#     operation's outcome is now canon. Future Act IV/V beats read against
#     this state (Rhea has the real names, the surgical human option is on
#     the table for Echelon).
#   - canon_set phoenix.civilian_move "in_progress" — the move is the Act
#     IV close's foreground. s22 will foreground it.
#   - canon_set council.empty_head_chair True — the empty chair is now a
#     canonical piece of council-room blocking. Any later council scene
#     that puts someone in the head chair must do so on purpose.
#   - canon_set aeron.delegated_the_question True — the pedagogical state
#     Selene was waiting for him to reach.
#   - tp_seed a4.aeron.room_with_no_head — True Path seed. The refusal of
#     the head-of-table blocking is a Shared-Authority-family True Path
#     beat mirroring s14's side chair.
#   - metric marcus_clock_hit +1 — Marcus has now hit the clock twice in
#     Phase III (adaptation in s03, second cut in s21).
#   - metric aeron_delegate_the_question +1 — new metric. Should accrue on
#     any later scene where Aeron delegates a structurally similar question.
#   - metric phoenix_civilians_in_motion set to 14 — the headcount for the
#     move. May decrement across Act V as civilians are delivered or lost.
# cann.thematic_flags:
#   - Thesis under pressure. "Can I lead without turning leadership into a
#     weapon?" The revenge option is the weaponization pressure and the
#     refusal of it is the answer. The cost is the forty-eight-hour move
#     and the injuries and the non-zero non-combat deaths Tessa has named.
#     The thesis does not survive cheaply.
#   - The room with no head. The empty chair at the head of the table as
#     the Act IV shared-authority blocking. Callback-ready for Act V.
#   - Delegating the question. Aeron applies Selene's s10 lesson. The
#     delegation is not tactical — it is epistemological. The room is
#     asked to carry a question that has no answer.
#   - Mercy as the decision made today against a future we do not get to
#     pick. (The line is not said in this scene. It is Aeron's internal
#     in s22 as the act's last line. This scene sets up that callback.)
#   - Relay, not choir. Every LI is doing distinct work on the decision —
#     Selene the option on the table, Noelle the framework, Lyra the
#     blessing and the naming of the question's job, Tessa the cost, Zira
#     the ground. No two of them are doing the same work. The shared
#     authority is distributed, not centralized.
# cann.character_moments:
#   - Aeron: side chair. The nod to Selene. The question. The silence
#     after the question. The final internal: "The question is at the
#     head of the table."
#   - Selene: putting the revenge option on the table explicitly, the
#     delegation-pattern run on herself. The post-council naming of the
#     lesson. "Chapter four. We are inside it now. Not just the name."
#   - Noelle: three framework answers offered with the explicit
#     declaration that she does not trust any of them. The first Noelle
#     beat where she offers analysis and names the analysis's limit.
#   - Lyra: the correct outcome of the question is that the room does
#     not have an answer. The question's job is to be carried, not
#     answered. Hands on the table, then back in her lap.
#   - Tessa: the field-clinic cost named out loud so the room is
#     approving injuries and non-combat deaths knowingly. The folded
#     paper list she had been writing on the walk over.
#   - Zira: the checkpoint interdiction. "Dad. Stop." The walking-back.
#     The comm presence in council. "I am asking the room to say the
#     decision out loud so I can quote the room to my runners."
#   - Marcus: one line for the audience. The grey room. The cataloguing
#     of Zira as the kind of runner he would have worked with in a
#     different life. The "different life" beat is the scene's small
#     concession to Marcus's interiority.
#   - Paela Venn: nineteen-year-old runner, the scene's one non-principal
#     interiority. Her list opening is the scene's first load-bearing
#     beat. She is a canonical new NPC as of this scene.
#   - Oris Telm: the civilian who breaks. His daughter's husband is on
#     an Echelon detention list. He walks to the checkpoint out of fear.
#     Zira walks him back. He is a canonical new NPC as of this scene
#     and may recur in Act V.
# cann.callbacks:
#   - a4_s03_marcus_adapts_emp: Marcus's operational adaptation. This
#     scene is Marcus hitting the clock a second time with a different
#     weapon (the list, not the strike). The matching line from s03 was
#     "Eleven hours of darkness. Not enough." This scene's counterpart
#     is "He is learning. I wonder if he will learn the rest of it."
#   - a4_s10 / a4_s05: Selene's delegation pattern. The lesson she has
#     been teaching Aeron across the act — that delegation is the shape
#     of shared authority — is named by her explicitly after the
#     council empties.
#   - a4_s14 (parallel batch): Aeron taking a side chair, not the head.
#     The council in s21 completes the blocking lesson by making the
#     head chair empty and leaving it empty for the whole scene.
#   - a4_s16 (parallel batch): Davel Ostra's KIA and the Marcus clock.
#     Referenced by the board state in s20 and by the Marcus intercept.
#   - a3_s07: Marcus using Aeron's counter-strike methodology against
#     Phoenix. This scene extends that reversal into the civilian-
#     targeting register. Marcus has moved from tactical adaptation to
#     strategic terror.
# cann.requires_followup:
#   - The civilian move is in progress as of scene end. s22 (Act IV
#     close) foregrounds the convoy. Act V must account for the
#     fourteen civilians, the three sectors, the forty-eight-hour
#     window, and Tessa's field-clinic outcomes.
#   - The list is in Zira's possession. It is a physical object that
#     Act V can reference. The list contains fourteen civilian names
#     and an unspecified larger number of Phoenix operative real
#     names. Rhea has a copy. Rhea has it on a tablet.
#   - The empty head chair is now a canonical piece of council
#     blocking. Any later council that violates this blocking must
#     do so on purpose.
#   - Paela Venn and Oris Telm are new canonical NPCs. Both are
#     available for Act V reappearance.
#   - Marcus's "different life" beat is a small aperture into Marcus's
#     interiority. Should be respected in Act V — Marcus is not a
#     monster, he is a man who is on the wrong side of the thesis
#     and knows it.
