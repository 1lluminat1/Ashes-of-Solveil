# =======================================================
# ACT 4 - Scene 11: Mercy Call Costs (Empathy Path)
# File: a4_s11_mercy_call_costs_emp.rpy
# Type: OPERATION SCENE — mercy against strategic cost
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s11_mercy_call_costs_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s11_mercy_call_costs_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Four registers. (1) Field — handheld, tight, low light. The column
    #         of six captured Echelon in the ravine, Phoenix fighters on the edges
    #         of the frame. The camera stays inside the circle. (2) Decision — a
    #         medium hold on Aeron at the edge of the ravine, the six behind him
    #         in soft focus. Selene's comms voice over. (3) Transit to containment —
    #         Zira walking the lifer Vess Kallan through the secondary base corridor
    #         with her rifle on her back and a grip on his elbow that is the
    #         professional grip of a Phoenix officer who has done this exactly twice
    #         before and is counting it. (4) Command post after — Aeron alone at
    #         Noelle's board, looking at 38% in red paint. No music until this last
    #         beat; one low note, fadeout on black.
    # LIGHTING: Field — pre-dawn, gray-blue, the horizon about thirty minutes from
    #           morning. Flashlight beams cutting through low mist. The six captives
    #           on their knees in the mist. (2) Decision — the same light, colder.
    #           (3) Corridor — standard secondary-base amber, overhead strips, the
    #           particular flatness of a corridor at shift change. (4) Command post —
    #           one work lamp on Noelle's board, the 38% drawn in red marker by her
    #           own hand. Everything else dim.
    # SFX: Field — boots in gravel, breath in the cold, the low hum of the Phoenix
    #      comms relay Kael — no. The Phoenix comms relay. Scratch that memory.
    #      The relay hum. Distant hoots of a Sector 12 owl. (2) Decision — wind.
    #      (3) Corridor — footsteps, amber hum, a door opening ahead and closing
    #      behind. (4) Command post — Noelle's crystal at a low register, a single
    #      fan on the ventilation. Silence otherwise.
    # FX/COMP: The 38% on Noelle's board is drawn large. Not projected. Noelle
    #          uses the projection for models; she uses the marker when she wants
    #          a number to be a physical artifact in the room. That choice is
    #          visible and deliberate. The marker is red.
    # BLOCKING: Field — Aeron at the ravine edge, Phoenix cordon around the six,
    #           Lyra on the overwatch ridge, Zira at Aeron's right shoulder, Noelle
    #           on comms from base. The six are arranged in a half-circle on their
    #           knees. Vess Kallan is third from the left. His posture is different.
    #           Decision — Aeron turns from the six to look at Zira. They trade a
    #           line. Aeron turns back. Transit — Zira walking Kallan. Command post —
    #           Aeron at the board alone.
    # FACE: Aeron — carrying the unabsorbed Selene sentence from a4_s10. He is
    #       running an operation with the shape of the thesis sentence in his
    #       chest and no action protocol yet. Selene — on comms, dry, tactical,
    #       the voice she uses when she is not giving a speech. Zira — field-Zira,
    #       precise. Lyra — overwatch voice, comms-clean. Noelle — data, with one
    #       held pause that lands like a mercy.

    # ========= VOICE BASELINE =========
    # EMP cadence. The operation itself is tactically fast. The scene has two slow
    # beats: (1) Aeron's mercy call at the ravine edge, (2) the command post after.
    # Everything between is clipped field voice. Selene is voice-only on comms.
    # Lyra is voice-only on comms. Zira is in the field with Aeron physically. Noelle
    # is at base comms with the probability work.

    # scene bg_sector_12_ravine_predawn_emp with dissolve
    # play ambient "sfx/ambient/predawn_ravine_cold.ogg" fadein 2.0

    # ========== PHASE 1 — THE CAPTURED SIX ==========

    "Pre-dawn. Sector 12. A ravine the Phoenix scouts have been mapping for a week."

    "The operation was supposed to be an intel pull — an Echelon patrol passing through the corridor with field reports Noelle wanted for the Marcus adaptation model. The scouts had the patrol on a loop. Aeron's team was in position to take them silent if the window opened. The window opened."

    "The take was clean. Not effortless — clean. No Phoenix down. No shots fired that did not need to be fired. The tranq rounds did what tranq rounds do when the plan is the plan and the plan is running."

    "Six Echelon soldiers on their knees in the mist on the floor of the ravine."

    "Aeron is standing at the edge of the ravine with Zira at his right shoulder. Lyra is up on the overwatch ridge — one hundred meters above them, the long gun at rest, her voice on the comms."

    l "Overwatch clear. No additional patrols inbound. We have a window of approximately forty-three minutes before Echelon realizes this patrol missed check-in. I will hold the ridge until you clear."

    a "Copy, overwatch."

    "He looks at the six."

    "Noelle is running identifications through the comms link. Her voice in his ear is clean and level."

    n "Identifying captives. Working off facial against Echelon personnel database. Give me thirty seconds."

    "Thirty seconds. Aeron uses them."

    athought "Six kneeling."

    athought "Pre-dawn gray. The mist is still in the ravine. The ravine floor is gravel over old riverbed. In about three minutes somebody is going to have to decide what the next forty-three minutes look like."

    athought "I am going to be the one who decides. That is the part of the scene I do not get to delegate. I can delegate the ops and I can delegate the question — I am trying to learn how to delegate the question — but the decision at the ravine edge is the decision that has to be made right now and I am the commander on the ground."

    athought "Selene would say the question is still pluralizable. She would say the decision is the task, the question is what we owe the six, and the what-we-owe is a sentence with more than one signer."

    athought "I am going to try it. I am going to try it in the forty-three-minute window and I am going to fail at it or succeed at it and the failure and the success are both going to be part of the scene."

    "Noelle's voice returns."

    n "Identifications complete. Five of the six are conscripts. Draft classifications ranging from eight weeks to fourteen months of service. Three Sector 12 locals — two from the same village, one from a relocation camp. One from Central. The fifth is a cook's assistant."

    a "The sixth."

    n "The sixth is Officer Vess Kallan. Lifer. Seventeen years Echelon service. Rank equivalent to captain. On a fast-track adaptation team. Noelle flags — his duty history is in the Central Command classification ring for internal security."

    "Silence on comms for one second."

    n "Aeron. He is exactly the kind of officer who maps the inside of any organization he is inside of long enough to map it."

    athought "Noelle is flagging. Noelle flags things when she wants the flag in the record. She is not telling me what to do — she is making sure the flag is on the log so that nobody in the command culture gets to say later that the flag was not raised."

    athought "I am hearing the flag."

    "He walks down the ravine slope to the six."

    "Gravel under boots. The six do not move — tranq is wearing off, they are waking up but not yet coordinated. One of the conscripts — the cook's assistant, Aeron is going to learn later — is crying without making any noise. One of the Sector 12 locals is staring at the ground and breathing through his mouth. The other is looking at Aeron with the blank face of a person who has decided the blank face is the only available register."

    "Vess Kallan is third from the left."

    "His posture is different from the other five. He is kneeling with his back straight. His hands are bound in front of him — Phoenix standard restraint — and his eyes are on Aeron from the moment Aeron is in line of sight."

    "He does not look afraid."

    "He looks curious."

    # ========== PHASE 2 — THE LIFER ==========

    athought "He is not afraid because he has decided he is not going to be afraid. That is a discipline. I recognize it the way you recognize handwriting."

    athought "He is watching me to see what kind of commander I am. He is cataloguing. He is doing the thing Noelle said he would do — mapping me from the ground in the minute he has to do it."

    "Aeron stops at a professional distance. Not close. Not across the ravine. Three meters."

    a "Officer Kallan."

    "Kallan does not answer for a beat."

    "Then he speaks in the measured voice of a person who has been in rooms like this before, on the other side of them."

    # Note: Vess Kallan is a new speaker. Using direct string dialogue for him
    # in this first appearance — tag 'vk' can be registered in the characters
    # file if he recurs. For this scene we use the string form.

    "'Commander Solveil.'"

    "'You know my name.'"

    a "Your database entry is in my comms officer's ear. That is all I know about you right now."

    "'You know enough to know what I am. I know what you are. That is enough of a conversation for the two of us. If you would like to finish the scene, I will kneel for it and I will not make it difficult.'"

    athought "He is offering me the clean version. He is offering me the execution right now because he has seen the rebel doctrine before and he expects rebel doctrine and he is a lifer and he is not going to ask me for anything."

    athought "He has just saved me a sentence by giving me his expectation at the outset. I am going to file that. I am going to file it the way Noelle flags things — not as a reason to do what he expects, as a reason to know what my own deviation costs."

    "Aeron does not answer him right away."

    "He turns his head — not much, just enough for Zira in his peripheral."

    a "Zira."

    z "Here."

    a "What does the field protocol say."

    "Zira does not hesitate. This is not her first time in a ravine with this exact decision tree."

    z "Rebel doctrine standard in this scenario: execute the lifer, hold the conscripts for turning, move in eighteen minutes. The doctrine assumes the lifer is operational liability and the conscripts are recoverable. It assumes the window is finite and the distance to containment is too far for the lifer to be moved without cost."

    z "That is the doctrine. I am giving it to you because you asked. I am not giving it to you as a recommendation."

    "She says the last sentence at a specific volume — low enough that the six cannot hear it, high enough that the comms relay picks it up for the log."

    athought "She is flagging too. She is flagging in a register Selene and Noelle will both hear when they review the audit. Zira is making sure the command culture gets the record of what the doctrine says and the record of her not recommending it."

    athought "That is the whole thing. That is the 'I am on your six' from last night, in operational register, on comms, in a ravine. She is doing with a radio exactly what she did across a table in the mess."

    a "Selene. Are you on this channel."

    sel "I am on this channel. I have been on this channel since the ID pinged."

    a "What do you say."

    "There is a half-second pause. Selene does not pause often. The pause lands."

    sel "I say this is your ravine."

    sel "I say the doctrine is the doctrine and the doctrine is not the question. I say Noelle's flag is in the log and my flag is in the log now too. I say I am not going to override you at the ravine edge because the ravine edge is where the question I asked you to delegate lives, and I am asking you to delegate it to a table that includes me and does not include me as an order-giver."

    sel "Make the call, commander. I will carry it with you. That is the whole inheritance I have for you this morning."

    "The wind picks up in the ravine. The mist shifts half a meter and shows the six a little more clearly."

    # ========== PHASE 3 — THE MERCY CALL ==========

    athought "Delegate the question."

    athought "I do not know the action yet. She told me last night I would not know the action and she was right. I do not know the action. I know the sentence."

    athought "The sentence in this ravine is: what do we owe the six."

    athought "Not: what does the doctrine owe the six. Not: what does tactical efficiency owe the six. Not: what does Marcus's adaptation window owe the six. What do we — the we that is Phoenix, the we that includes Selene in overwatch and Noelle at comms and Lyra on the ridge and Zira at my shoulder and the fighters back at base who have not slept properly in a month and the Phoenix KIA we added to the board three days ago — owe these six kneeling people whose faces I can see in the mist at pre-dawn."

    athought "Mercy is a decision made today against a future we do not get to pick. Lyra said something like that once. Or will say it. Or is about to say it in the next ten minutes because she is on the comms and she is the Phoenix cleric and she will not let the decision pass without a sentence around it."

    athought "I am going to hold all six. I am going to refuse the execution. I am going to refuse the turning of the conscripts — they can be turned with consent at a safer time, not in a pre-dawn ravine while they are still coming off tranq. I am going to hold all six in containment until we have time to do this more carefully."

    athought "I am going to do it knowing Kallan will map the base. I am going to do it knowing Noelle's probability number is going to be a number I am going to have to sit with. I am going to do it because the sentence in my chest from the annex last night said the being is the part that kills you and the being that would kill me this morning is the being of a commander who executes a man at a ravine edge in a pre-dawn mist because the doctrine said so and I did not have any other sentence in my mouth."

    athought "I have another sentence."

    athought "The sentence is: I would like Phoenix to be the rebellion that holds six."

    "He turns back to Kallan."

    a "Officer Kallan. I am going to tell you what is going to happen. I am going to tell you because you have asked for the scene to be finished and I am going to give you the finish in the form it is going to take."

    a "You are going to be moved to Phoenix containment. You and the other five. You are going to be held. The conditions will be humane. You will not be executed. You will not be immediately separated from the other five. You will be interviewed by one of my officers at a time that is not now and in a place that is not this ravine."

    a "I am not taking you because I think you are recoverable. I am not taking you because I think I have a use for you beyond the intelligence you carry in your head that you will or will not volunteer. I am taking you because I am not going to execute you in a ravine."

    "Kallan does not speak for a moment."

    "'That is a more expensive decision than you are admitting, commander.'"

    a "I am admitting it."

    a "I am going to admit it twice, in fact, because you are the sixth person in this ravine and I want the log to have both admissions. I am admitting the tactical cost. I am admitting the strategic cost. I am admitting that my comms officer has flagged you as an officer who will map the inside of any organization you are in long enough to map, and that I am taking the cost of that mapping onto Phoenix's ledger with my eyes open."

    a "I am not doing this because I think it is cheaper. I am doing this because it is what I owe the six."

    "Kallan tilts his head half a centimeter."

    "'The doctrine you are breaking is older than you, Commander Solveil.'"

    a "I know."

    "'You are going to regret it.'"

    a "I may. That is not a reason to execute you this morning. That is a reason to be careful about how I hold you for the length of time I am going to hold you."

    "Kallan looks at him for another beat. Then his posture changes a fraction — he lowers his chin a millimeter. Not deference. Acknowledgment. The Echelon officer version of acknowledgment."

    "'Understood.'"

    # ========== PHASE 4 — THE COST LANDS ==========

    "Aeron steps back from the six."

    "Selene's voice in his ear."

    sel "Aeron."

    a "Here."

    sel "I accept the call. For the log — commander Solveil has directed full capture and detention of six Echelon personnel including one senior lifer. The mercy is logged. The call is mine to accept on behalf of the command structure. I accept it."

    sel "And now I am going to ask you the question you knew I was going to ask."

    a "Ask it."

    sel "What happens in three weeks when Kallan has been in our system long enough to map it."

    "The question lands the way a clean shot lands. Not cruel — precise."

    sel "I am not asking to shame the decision. I am asking because the decision has a downstream and the downstream has to be part of the decision. You made a call that saved six lives at the ravine edge this morning. The call is good at the ravine edge. The call is also a decision we are going to be living inside of for the next three to six weeks until we solve the containment problem or the containment problem solves us."

    sel "I am going to ask Noelle to run the probability."

    sel "Noelle, run it."

    "A half-second."

    "Then Noelle's voice, careful and level."

    n "Probability of Echelon compromise of secondary base perimeter inside twenty-one days, given retention of Officer Vess Kallan under standard Phoenix containment protocols: thirty-eight percent."

    "The number is in the ravine now. The number is on the comms log. The number is also, Aeron knows without having to see it, about to be drawn on Noelle's physical board back at base in red marker."

    n "I want to flag that the probability is load-bearing on the word 'standard.' If we adapt containment protocols specifically for Kallan, the probability drops. How much it drops depends on which protocols we adapt and how much resource we spend on adapting them. I do not have a point estimate for the adapted case yet. I will have one by tonight."

    n "I also want to flag — for the log — that I am not running this probability as an argument against the call. I am running it because it is my job to run it. The call is made. The probability is a thing the command culture has to hold in the same room as the call."

    athought "Noelle is flagging the same way Zira flagged the same way Selene flagged. All three of them are flagging in the log. All three of them are flagging in a way that makes the decision collective without taking the decision away from me."

    athought "This is what shared authority feels like when it is working. This is what Selene was telling me last night at the window of the annex. The question is plural. The answer is mine at the ravine edge but the holding of the answer is plural."

    athought "I am going to feel the thirty-eight percent all day. The thirty-eight percent is the shape of the cost."

    athought "I knew there was a cost. I did not know the cost had a decimal place."

    # ========== PHASE 5 — ZIRA CARRIES THE LIFER ==========

    "The six are brought up the ravine slope under Phoenix escort. The five conscripts move as a group with two Phoenix fighters on each flank. Kallan is moved separately. Not because Aeron ordered the separation — because Zira walked up to him before Aeron finished the comms exchange with Noelle and said, in the flat command voice she uses when the command voice is the point:"

    z "I will move the lifer. Directly. I want my hand on his elbow for the entire transit."

    "Aeron looks at her."

    athought "She is offering to carry the physical weight of the call that is going to cost me thirty-eight percent. She is not offering it as a favor. She is offering it because she is on my six and because the word for 'on my six' in this particular operation is 'I will put my hand on this man's elbow from here to containment and I will not let go until the door closes.'"

    athought "I am going to accept it."

    a "Accepted. Zira — direct transit, no stops, full comms the whole way."

    z "Copy."

    "She moves to Kallan. She does not say anything to him. She takes his elbow in the grip of a Phoenix officer who has done this exactly twice before in her life and is counting it tonight."

    zthought "Third time."

    zthought "First time was in the Lower Spans with a Rex agent who died on the transit. Second time was in the broadcast aftermath with a communications officer who turned at the door of containment and told me everything. Third time is this morning with a lifer who is watching me and cataloguing my grip and writing my biography in his head."

    zthought "I am going to walk this man the full transit and I am going to not hurt him and I am going to not let my grip slacken and I am going to not speak to him and I am going to log the minute I take him and the minute I put him down."

    zthought "I am also going to add him to the personal ledger I have been running since the Lower Spans, because the ledger is the thing I carry instead of the thing I say, and Aeron would understand that if he knew I had a ledger."

    zthought "He does not know I have a ledger."

    zthought "He does not know because I have not told him and because last night at the mess I was asking him to see me asking and not asking him to see the ledger. The ledger is a separate thing. I will show him the ledger when the ledger is the thing he needs to see."

    zthought "Not today. Today I carry the lifer."

    "Zira walks Kallan up the ravine slope. Her grip on his elbow is steady. Kallan does not resist. He walks at her pace. The transit is silent."

    "Aeron watches her do it."

    athought "She is carrying my mercy call in a physical form right now. Her hand on his elbow is the body version of the sentence I just said at the ravine edge. She is making the sentence into a thing with weight by walking the weight of it through a ravine at pre-dawn."

    athought "This is what 'I will carry it with you' looks like when it is not a metaphor."

    athought "Selene said it on comms ten minutes ago. Zira is doing it with her hands right now."

    athought "The sentence Selene said was 'I will carry it with you.' The sentence Zira is enacting is the same sentence in a body verb. I need to remember that these are not different sentences. They are one sentence performed by different mouths and hands."

    # ========== PHASE 6 — LYRA'S BENEDICTION ==========

    "Aeron stops at the top of the ravine slope before moving to the extract vehicles. Lyra's voice comes down from the ridge on the comms."

    l "Overwatch. I have the ravine clear for another twenty-nine minutes. I am going to come down to you in about six."

    a "Acknowledged."

    l "Aeron."

    a "Yes."

    l "I want to say a sentence for the log before I leave the ridge. I am saying it now because the ravine is still in earshot of the comms and because the sentence belongs in the place the decision was made."

    a "Say it."

    "A breath on comms. Lyra's comms voice — the clean cleric voice she uses when she has decided a sentence is load-bearing."

    l "Mercy is a decision made today against a future we do not get to pick."

    "The sentence goes into the comms log."

    l "I am saying that because you made the call and the call is the call. I am not softening it. I do not think mercy is always correct and I do not think you think it is always correct either. I think this morning you made the correct call against a probability that the next three weeks may prove was wrong, and I think the correctness does not depend on the probability."

    l "The correctness is that we are the rebellion that held six."

    l "If the three weeks go badly, we will still have been the rebellion that held six this morning. That cannot be unmade by whatever Kallan does or does not do. The ravine is in the log. The mercy is in the log. The log is a thing that survives the next three weeks."

    l "I wanted that on the record before I left the ridge."

    sel "Logged, overwatch."

    l "Copy, command."

    athought "She did not soften it. She was explicit that she did not soften it. She is blessing the call and not pretending the blessing is a clearance. That is the cleanest benediction I have ever heard her give on comms."

    athought "I am going to remember that sentence. 'Mercy is a decision made today against a future we do not get to pick.' That is going next to Selene's sentence from last night. The two of them are going into the same ledger."

    athought "The ledger is starting to have entries. Last night it had Kael's line and Selene's line. This morning it has Lyra's line and Noelle's number. Zira's whole body is on the ledger right now in the form of the grip on Kallan's elbow."

    athought "The ledger is not mine alone anymore."

    athought "The ledger has co-signers."

    athought "I did not know until this sentence that the ledger was the thing I was trying to learn how to share."

    # ========== PHASE 7 — EXTRACT ==========

    "Phoenix clears the ravine in seventeen minutes. The captured six are loaded into the extract vehicles — the five conscripts in one, Kallan and Zira in the second. Noelle monitors the comms. Selene monitors from overwatch. Lyra comes down from the ridge and rides in the overwatch vehicle with the long gun across her knees."

    "The operation is tactically a clean success. The intel pull was complete. The Phoenix team is unharmed. The six captured. The mercy call logged. The cost logged next to it."

    "The ride back to base is forty minutes."

    "Aeron rides in the forward vehicle. He does not speak during the ride. He has the comms on low so he can hear any alert Noelle puts through. Zira's vehicle stays in his peripheral. He checks for its running lights twice. He does not talk to her on comms — Zira is working and he does not interrupt Zira when she is working, especially not when Zira is working with her hand on the elbow of a seventeen-year Echelon lifer."

    athought "The ride is quiet. The operation is over and the thing the operation was for is in the vehicles and the thing the operation cost is sitting in Noelle's comms at a decimal I cannot unknow."

    athought "I keep wanting to replay the ravine edge. I keep wanting to test the decision against the doctrine. I am not going to do it on the ride. Selene said I would be alone with the sentence for a day or two. The sentence from last night was 'delegate the question.' The sentence from this morning is 'thirty-eight percent.' The two sentences are going to live in the same part of my chest for as long as it takes them to find a shape."

    athought "I am not going to hurry the shape."

    # ========== PHASE 8 — THE COMMAND POST AND THE NUMBER ==========

    # scene bg_command_post_noelle_board_emp with dissolve

    "Back at base. The command post. Noelle's board."

    "Her board is the one physical artifact in the command post that is not projected. A tall standing whiteboard, magnet-strapped to the support column. Noelle uses the projection for models. She uses the board for numbers that need to be a physical thing in the room for the command culture to sit with."

    "The 38%% is on the board."

    "She has drawn it large. Red marker. Her own handwriting. Centered."

    "Below the number, in smaller marker, she has written: 'Compromise of secondary base perimeter, 21d, Kallan retained, standard protocols.' Below that, in a different color — blue — she has written: 'Adapted protocols: estimate pending by 21:00 tonight.'"

    "The board is lit by one work lamp. Everything else in the command post is dim. Noelle is not there — she has gone to her quarters for an hour to work on the adapted-protocol estimate and eat something, because Selene ordered her to."

    "Aeron is alone with the board."

    "He came here from the extract debrief. He did not stop at quarters. He did not stop at the mess. He came to the command post the way a person goes to the thing that is going to tell them the next sentence they have to hear."

    "He stands in front of the number."

    "He does not sit."

    athought "Thirty-eight percent."

    athought "That is almost two in five. It is better than half. It is worse than a third. It is a probability with a decimal place that Noelle drew in red marker on a physical board because Noelle wanted me to stand in front of it and not be able to minimize it and not be able to collapse it into a projection I could dismiss by walking out of the room."

    athought "She drew it because she wanted me to look at the number in the same way I looked at Kesa Marin and Joren Hale on the cipher alcove projection. She drew it because the number has a weight and the weight is the thing the command culture is holding."

    athought "She is not alone in drawing it. She is not alone in the holding. That is the thing I am going to say to myself out loud in about thirty seconds because Selene told me last night that the saying is part of the being."

    "He looks at the number for a long moment."

    "Then he says it."

    a "Thirty-eight percent."

    a "The cost of holding Vess Kallan for the first three weeks under standard protocol. A number Noelle drew on a board so I could see it as a thing in the room."

    a "I am not going to minimize it. I am not going to project it onto a model and look at it through a distance. I am going to stand in front of the number and let the number be a number."

    a "I am not alone in the number."

    a "That is the sentence."

    athought "I am not alone in the number."

    athought "That is the first time I have said any version of that sentence about a cost since the chapter started. I have said 'I will carry this' about a dozen times. I have said 'that is on me' about six times. I have said 'I am responsible' in the privacy of my own head about a hundred times."

    athought "This is the first time I have said 'I am not alone.'"

    athought "I said it out loud. I said it to an empty command post. I said it to a board with red marker on it."

    athought "Selene is going to know I said it, because the comms in the command post are on a live log, and Selene reviews the command-post log every morning at 0830. She is going to know. She is not going to bring it up. She is going to let the saying be mine."

    "He stays in front of the board for another two minutes."

    "He does not sit. He does not leave."

    "He puts his hand flat on the cool face of the board next to the 38%%. Not on the number — beside it."

    athought "My hand is on the board next to the number. The number is in my handwriting now in the sense that a hand next to a number is a form of handwriting."

    athought "I am going to leave my hand there for ten seconds and then I am going to walk out of the command post and I am going to go to quarters and I am going to sleep. That is the protocol I owe myself after this morning. That is the protocol Tessa would prescribe and the protocol Zira would endorse and the protocol Selene would expect and the protocol Lyra would bless."

    athought "Four women in this building and one cleric on a ridge would all tell me the same thing about the next six hours. I am going to listen to them without needing any of them to come find me to say it."

    "He holds his hand on the board."

    "Ten seconds."

    "He takes his hand off."

    "He walks out of the command post."

    "The work lamp stays on behind him. The board stays up. The 38%% stays red. The command post waits for Noelle's return at 2100 and the adapted-protocol estimate she will put in blue below the red."

    "Scene ends on the board."

    "The camera holds on the red number for three seconds before the fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("aeron_mercy_call_captured_six", True)
    $ flag("vess_kallan_captured", True)
    $ canon_set("captive.vess_kallan", "held")
    $ canon_set("echelon_capture.sector_12_six", "held_full")
    $ canon_set("aeron.said_not_alone_in_command_post", True)
    $ npc_remember("Aeron", "refused_execution_at_ravine_edge", tone="mercy_with_open_eyes")
    $ npc_remember("Aeron", "said_i_am_not_alone_aloud", tone="first_time_in_chapter")
    $ npc_remember("Selene", "accepted_mercy_call_on_comms", tone="delegate_the_question_in_practice")
    $ npc_remember("Zira", "walked_lifer_to_containment", tone="body_verb_of_shared_authority")
    $ npc_remember("Lyra", "mercy_benediction_from_the_ridge", tone="cleric_logged")
    $ npc_remember("Noelle", "drew_38_percent_in_red_marker", tone="physical_artifact_in_the_room")
    $ metric("aeron_mercy_cost", set_to=1)
    $ metric("aeron_delegate_the_question", add=1)
    $ tp_seed("a4.mercy.captured_six")
    $ rel_bump("Zira", trust=1)
    $ rel_bump("Lyra", trust=1)
    $ rel_bump("Noelle", trust=1)
    $ rel_bump("Selene", trust=1)
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s11_mercy_call_costs_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Pre-dawn, Sector 12, the morning after a4_s10 (Selene's thesis in the
#     archive annex). Aeron is running an operation for the first time since
#     receiving the delegate-the-question sentence. He is carrying the sentence
#     into the field without having absorbed it and the scene is the operational
#     test of whether the unabsorbed sentence can still shape a decision.
# cann.what_happened:
#   - Clean intel pull in a Sector 12 ravine. Six Echelon soldiers captured
#     alive with no Phoenix casualties and no shots fired that did not need to
#     be fired. The operation is tactically a success before the scene starts.
#   - Noelle identifies the six: five conscripts (three Sector 12 locals, one
#     from Central, one cook's assistant) and one lifer — Officer Vess Kallan,
#     seventeen years Echelon service, rank equivalent to captain, fast-track
#     adaptation team, Central Command internal security classification ring.
#   - Noelle flags Kallan as an officer who will map the inside of any
#     organization he is in long enough to map. The flag is deliberately put
#     on the log for the command culture to hold.
#   - Standard rebel doctrine in this scenario: execute the lifer, turn the
#     conscripts. Zira states the doctrine for the log without recommending it.
#     Her flag is also deliberate.
#   - Selene is on comms from overwatch. She is asked for her call and refuses
#     to give an order. "This is your ravine." She delegates the question
#     (Selene's delegate-the-question sentence from a4_s10 in practice). She
#     says she will carry it with Aeron but will not override him. The
#     inheritance is operational now.
#   - Aeron makes the mercy call at the ravine edge. He refuses the execution.
#     He refuses the turning of the conscripts in the ravine at pre-dawn. He
#     will hold all six in Phoenix containment for humane interview at a later
#     time. He admits the tactical cost AND the strategic cost explicitly for
#     the log, twice. The key sentence: "I am not doing this because I think
#     it is cheaper. I am doing this because it is what I owe the six."
#   - Vess Kallan acknowledges the call with a half-centimeter chin drop.
#     Echelon officer acknowledgment. He tells Aeron "You are going to regret
#     it." Aeron answers "I may. That is not a reason to execute you this
#     morning. That is a reason to be careful about how I hold you."
#   - Selene asks the downstream question on comms: "What happens in three
#     weeks when Kallan has been in our system long enough to map it." She is
#     explicit that she is not asking to shame the decision.
#   - Noelle runs the probability: 38% Echelon compromise of secondary base
#     perimeter inside 21 days, given retention of Kallan under standard
#     Phoenix containment protocols. She flags that the number is load-bearing
#     on "standard" and offers to run an adapted-protocol estimate by 2100.
#   - Zira walks up to Aeron and offers to personally walk Kallan to
#     containment — hand on his elbow, direct transit, no stops, full comms.
#     Aeron accepts. The scene frames her hand on Kallan's elbow as the body
#     verb of shared authority — the physical form of "I will carry it with
#     you." Zira's internal monologue reveals she has a private ledger of
#     transits she has not told Aeron about; today is the third entry.
#   - Lyra, from the overwatch ridge on comms, delivers the benediction for
#     the log: "Mercy is a decision made today against a future we do not get
#     to pick." She is explicit that she is not softening it. "The correctness
#     is that we are the rebellion that held six."
#   - Aeron rides back to base with the comms on low. He does not speak on
#     the ride. He checks Zira's vehicle running lights twice.
#   - At the command post he stands in front of Noelle's physical board where
#     she has drawn the 38% in red marker — her own handwriting, centered,
#     large. She is not in the room; she is in quarters working on the
#     adapted-protocol estimate under Selene's order.
#   - Aeron stands in front of the number and says out loud: "I am not alone
#     in the number. That is the sentence." It is the first time in the
#     chapter he has said any version of "I am not alone" about a cost out
#     loud. The command post comms are on live log. Selene will read the log
#     at 0830. She will not bring it up.
#   - He puts his hand flat on the board beside the number — not on it — for
#     ten seconds. Then he walks to quarters.
# cann.aeron_state:
#   - Carrying the unabsorbed "delegate the question" sentence from the annex.
#     The scene is the operational test. He does not execute the thesis in
#     polished form — he executes it in the specific small ways available at
#     a ravine edge: asking Zira for the doctrine on the log, asking Selene
#     for her position and receiving her refusal to order, admitting the cost
#     explicitly twice for the log, saying "not alone in the number" out loud
#     in the command post.
#   - The scene shows the unabsorbed lesson working BEFORE it is absorbed.
#     This is deliberate. Selene's sentence from a4_s10 ("you do not know the
#     action on the first night") is validated: Aeron does not know the
#     action, but the sentence is shaping his decisions anyway.
#   - "I am not alone in the number" is a canonical first. All future cost
#     scenes should read against this line. It is the earliest version of
#     Aeron actually practicing the Act IV lesson rather than receiving it.
#   - He does not resolve the 38% tonight. The scene is explicit that the
#     number is a shape he is going to carry. The shape does not close.
# cann.selene_state:
#   - Selene's refusal to order on comms is the scene's structural pivot.
#     "This is your ravine" is the Marcus-inheritance lesson in operational
#     form. She is delegating the question in real time while the question is
#     being asked. This is what the annex scene was for.
#   - She reads the command-post log in the morning. She will know Aeron
#     said the line. She will not bring it up. That is the same discipline
#     Marcus used with her. The inheritance is inherited.
# cann.zira_state:
#   - Zira's transit of Kallan is the scene's physical thesis. "I will carry
#     it with you" performed as a body verb. The scene's cleanest example of
#     shared authority as an ontology before a workflow.
#   - Her internal ledger is flagged here for the first time in Act IV. Three
#     transits: Lower Spans Rex agent, broadcast-aftermath comms officer,
#     Kallan today. She has not told Aeron she has a ledger. The ledger is a
#     future scene's payload.
#   - The scene reinforces the a4_s09a opening: Zira is on Aeron's six in a
#     way that is not operational even when it is operational.
# cann.lyra_state:
#   - Lyra's benediction on comms from the ridge is the cleric-voice version
#     of her Act IV work. She is not softening. She is logging a sentence for
#     the record. "We are the rebellion that held six" is the scene's clean
#     theological anchor.
#   - The benediction is future-quotable. Subsequent scenes where Phoenix's
#     self-definition is at stake should be able to reference the sentence.
# cann.noelle_state:
#   - Noelle flags twice: once at the identification (flagging Kallan's
#     mapping capacity), once at the probability (flagging that she is not
#     running the probability as an argument). Both flags are deliberate and
#     in the log.
#   - Her decision to draw the 38% in red marker on a physical board instead
#     of on the projection is the scene's most underlined character moment.
#     She is making the number a thing in the room. This is her Act IV way
#     of participating in shared authority — she can do math that becomes
#     furniture.
# cann.path_tracking:
#   - EMP path. Linear. No player choice — the mercy call is canonical to the
#     EMP Act 4 path. Players on other paths receive a different version of
#     this scene or skip it entirely.
#   - flag aeron_mercy_call_captured_six True. flag vess_kallan_captured True.
#   - canon_set captive.vess_kallan "held". canon_set echelon_capture.sector_12_six
#     "held_full". canon_set aeron.said_not_alone_in_command_post True.
#   - metric aeron_mercy_cost set to 1. This is the opening of the mercy-cost
#     metric; subsequent scenes may accumulate it.
#   - metric aeron_delegate_the_question +1 — first increment. Tracks Aeron
#     practicing the lesson, not just receiving it.
#   - tp_seed a4.mercy.captured_six. This seeds the Kallan downstream arc.
#   - rel_bump Zira, Lyra, Noelle, Selene all +1 trust. Every LI and command
#     ally in the scene gave Aeron a flag or a verb that made the scene
#     workable. The bumps reflect collective performance of shared authority.
# cann.thematic_flags:
#   - The ravine edge as the Act IV operational thesis location. The pre-dawn
#     mist, the gravel, the kneeling six. Future operational decision scenes
#     may reference the ravine as a body-memory space.
#   - "I am not alone in the number" — Aeron's first operational performance
#     of shared ledger. The sentence is quotable and callback-ready.
#   - "We are the rebellion that held six" — Lyra's theological anchor.
#     Callback-ready for Phoenix self-definition scenes.
#   - The 38% as a physical artifact. The choice to put a number on a board
#     in marker instead of on a projection is Noelle's Act IV gesture of
#     shared being. The board is a location that can be returned to.
#   - Mercy as a decision made today against a future you do not get to pick.
#     Lyra's version of Selene's "necessary is not worth it." The two
#     sentences are sibling inheritance lines and should be quoted together
#     in any later scene that is about the cost of Phoenix's ethics.
# cann.character_moments:
#   - Aeron: refused execution at the ravine edge with explicit double
#     admission of cost on the log. Said "I am not alone in the number" out
#     loud in an empty command post. Put his hand flat on the board beside
#     the 38% for ten seconds. These are the three trifecta moments.
#   - Selene: refused to order on comms. "This is your ravine." Said "I will
#     carry it with you" into the comms log as inheritance in practice.
#   - Zira: offered to walk the lifer to containment with her hand on his
#     elbow. The internal ledger of three transits is seeded.
#   - Lyra: benediction from the ridge on comms. "The correctness is that we
#     are the rebellion that held six." Logged.
#   - Noelle: drew 38% in red marker on a physical board. Flagged twice with
#     explicit "for the log" framing. Offered adapted-protocol estimate by
#     2100.
#   - Vess Kallan: offered the clean execution expectation and was refused.
#     Tilted his chin half a centimeter in Echelon acknowledgment. Told Aeron
#     "You are going to regret it." The character is now canonical and held.
# cann.callbacks:
#   - a4_s05_delegation_test_emp: Plan A vs Plan B. This scene is the Act IV
#     follow-up where the plan is Aeron's and the question is Selene's.
#   - a4_s10_what_selene_meant_emp: the thesis sentence. "Delegate the
#     question." This scene is the operational test of the unabsorbed lesson.
#     The thesis is working before it is understood.
#   - a4_s09a_she_calls_him_out_emp: "I am on your six." Zira's version of
#     the same sentence performed here as a grip on Kallan's elbow.
#   - a4_s04_lyra_unbuckled_emp: Anayet — "I name the thing that cannot be
#     promised." Lyra's benediction from the ridge is in the same register.
#     The Order's cleric vocabulary is bleeding into Phoenix's command log.
#   - a4_s05a_you_are_not_a_machine_emp: Tessa's rule of three. Aeron has not
#     said the six names out loud in this scene — that is next. The ravine
#     is where the rule gets its operational test in Act IV.
#   - a1_s20_lower_spans: Zira's first transit. She is counting this as her
#     third. The ledger is a future scene's payload.
# cann.block_status:
#   - MAJOR SCENE. Linear. EMP path only. Operational follow-up to the thesis
#     scene. Prerequisite for the Kallan downstream arc.
# cann.requires_followup:
#   - Vess Kallan is now a canonical captive held in Phoenix containment.
#     The 21-day compromise window is a ticking clock. Later Act IV scenes
#     may play the countdown explicitly.
#   - Noelle's adapted-protocol estimate is due at 2100 tonight. A later scene
#     may show her delivering it. The blue annotation on the board is set up.
#   - Zira's private transit ledger is seeded. A later Zira scene should
#     reveal the ledger to Aeron when the revelation is ready.
#   - Lyra's ridge benediction is quotable. Any Phoenix self-definition
#     scene should be able to reach for the line.
#   - Aeron's hand on the board next to the number is a body-memory gesture.
#     Future delegation/cost scenes should reference or evolve it.
#   - "I am not alone in the number" is the first delta of the Act IV lesson.
#     Future cost scenes should escalate the line: from "not alone in the
#     number" to "not alone in the question" to "not alone in the being."
#     That escalation is the remainder of the arc.
