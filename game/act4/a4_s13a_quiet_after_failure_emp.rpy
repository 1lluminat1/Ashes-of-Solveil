# =======================================================
# ACT 4 - Scene 13a: Quiet After Failure (Empathy Path)
# File: a4_s13a_quiet_after_failure_emp.rpy
# Type: NOELLE NEW INTIMACY INSERT — data that does not fit
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s13a_quiet_after_failure_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s13a_quiet_after_failure_emp:
    $ show_timeline("30th of Forge, 390 A.C.", "21:00", "Phoenix Secondary Base — Aeron's Quarters")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Three movements, all still.
    #         (1) Quarters, Aeron alone: 50mm, locked, wide enough to see
    #             the bunk, the desk chair, and the door. Aeron on the edge
    #             of the bunk. The camera does not move for the first two
    #             minutes of the scene.
    #         (2) The knock and the entry: same frame. Noelle enters, does
    #             not cross the room. The camera widens by a fraction — a
    #             breath of extra air on the right-hand side of the frame
    #             where Noelle stops against the back of the door.
    #         (3) The floor: both of them seated on the floor. Aeron with
    #             his back against the bunk frame. Noelle with her back
    #             against the closed door. The wall they are not sharing
    #             is the wall behind the desk. The camera frames the two
    #             of them on opposite sides of the room with the open floor
    #             between them — the chosen distance is the subject. No
    #             cuts. No push-ins. The scene lets the distance hold.
    # LIGHTING: Aeron's quarters, late afternoon into early evening. The
    #           water stain on the ceiling in the upper-left, visible in
    #           the opening shot. The single overhead is at half — Aeron
    #           dimmed it on entering. The room is warmer than the
    #           corridor by one stop. When Noelle enters, the corridor
    #           light is briefly visible around her shoulder and then the
    #           door closes and that light is gone.
    # SFX: Quarters ambient — distant generator hum, the small tick of
    #      the base vent every forty seconds. His breath. Her breath once
    #      she is in the room and seated. No music for the first eighty
    #      percent of the scene. A single held low string under her
    #      second use of the word 'love,' and only there. The string does
    #      not resolve. It is cut at the end of the scene on a continuing
    #      pitch.
    # FX/COMP: THE DATAPAD on Noelle's lap. She carries it into the room
    #          and sets it on the floor beside her. It is not active. It
    #          is a token of her ordinary register. She does not pick it
    #          up at any point in the scene. The tactile detail is that
    #          she brought it and did not need it.
    #          THE WATER STAIN on the ceiling is the scene's visual
    #          anchor. Aeron looks at it three times. Noelle looks at it
    #          once, at the end, after he tells her what it looks like.
    # BLOCKING: Aeron on the edge of the bunk when she arrives. When she
    #           sits on the floor, he moves from the bunk to the floor
    #           opposite her — his back against the bunk frame. Neither
    #           crosses the open space between them. They do not touch.
    #           The wall between them is a wall made of floor.
    # FACE: Aeron — the face of a man on hour six of a forty-eight-hour
    #       stand-down who has not slept and has been looking at a water
    #       stain. The operational mask is gone; the intimate mask is not
    #       yet on. The face is unarmored by exhaustion. Noelle — the
    #       analytic face, but with the small tell at the corner of her
    #       mouth that she cannot quite close. The tell that means the
    #       framework has failed on a variable and she has carried the
    #       failure to the variable's door.

    # ========= VOICE BASELINE =========
    # EMP cadence, slowest of the three scenes. Noelle drives. Her voice
    # is analytic-register for the entirety of the scene — she does not
    # modulate into the romantic register, and that refusal is the
    # character beat. Aeron speaks less than she does. His few lines are
    # short, unornamented, and mostly questions. Internal thoughts run
    # heavy on Noelle (nthought) — this is her scene, she is inside it,
    # and the scene is a document of a framework failing in real time.

    # scene bg_aeron_quarters_late_day with dissolve
    # play ambient "sfx/ambient/quarters_quiet_low.ogg" fadein 2.0

    # ========== PHASE 1 — AERON ALONE ==========

    "Sixteen-fifty. Six hours and five minutes into the forty-eight-hour stand-down."

    "Aeron has not slept."

    "He has lain on the bunk, looking at the water stain on the ceiling, for approximately three hours and forty minutes. He has gotten up twice — once to drink water, once to use the head. He has not opened the datapad on the desk. He has not left his quarters. He has kept the letter and the spirit of the decision by sheer discipline, which is a thing he is aware is a kind of obedience he is not proud of and is doing anyway because there is nothing else left to do."

    athought "The water stain is the shape of a pangolin, or a small ferret, or a field mouse curled around its own tail. I cannot settle on which. I have been looking at it and it keeps switching. That is what Tessa calls the 'default-mode fidget' — a brain that is not tasked with a problem will start running pattern recognition on the nearest ambiguous surface and cannot stop."

    athought "I have defaulted to pattern recognition on a ceiling stain."

    athought "I have not been alone with my own brain for — I do not know how long. I cannot do the calculation right now because doing the calculation would be tasking the brain, and I have been instructed not to task it for another forty-one and a half hours."

    athought "I am sitting in a room with no task."

    athought "I am not good at that."

    "He is on the edge of the bunk now, not lying on it. The boots he unlaced earlier are on the floor. His feet are on the floor. His hands are on his knees. He is in the posture a man finds when he does not know which posture to occupy and has ruled out lying down."

    "There is a knock at the door."

    "Quiet. One knuckle. Not two. The knock of a person who does not want to be mistaken for an emergency."

    # ========== PHASE 2 — NOELLE ARRIVES ==========

    athought "Not Tessa. Tessa's knock is a two-knuckle diagonal with a half-beat between. That is one knuckle."

    athought "Not Lyra. Lyra does not knock, she says my name outside the door."

    athought "Not Selene. Selene is not coming to this room during the stand-down — her presence would change the architecture she drafted."

    athought "Not Zira. Zira is at the door in the ops wing sense today and the door here is not her door."

    athought "Noelle."

    "He does not say come in. He stands up from the bunk. He walks the three steps to the door. He opens it."

    "Noelle is in the corridor. She has her datapad tucked under her left arm and her right hand is at her side and her jacket is zipped to the collar, which is what she does when she is cold or trying to hold a shape. She looks at him."

    "She does not say anything."

    "He steps back and lets her in."

    "She crosses the threshold. She does not move further. She stops against the back of the door when it swings shut behind her — her back flat to the door, as if the door is a wall she is holding up."

    n "I am going to sit on the floor."

    "It is not a question. It is a statement of intent, because Noelle needs to say what she is about to do before she does it, so that the doing does not catch her in an unplanned posture."

    a "Okay."

    "She slides down the door to a seated position. Knees up. Back against the door. Datapad on the floor beside her. Right hand flat on the floor beside the datapad, as if anchoring to the plane."

    "Aeron looks at her for a second. He does not go back to the bunk. He crosses the floor to the opposite side of the room and sits down with his back against the bunk frame. The bunk is hard against his spine at the lumbar — he can feel the metal edge through his shirt. The wall behind Noelle is steel plate. The floor is cold."

    "The distance between them is about two and a half meters of open floor."

    "Neither of them moves to close it."

    # ========== PHASE 3 — THE SILENCE THAT IS NOT A SILENCE ==========

    "For a minute, neither of them speaks."

    "Noelle's eyes are on the floor about halfway between them. Her right hand stays flat on the floor beside the datapad. Her left is on her knee. She is not fidgeting. Noelle does not fidget — she is one of the few people in the building who does not have a body habit under pressure. The stillness is her habit."

    athought "She is waiting for something."

    athought "No — she is not waiting. She is the kind of still a person is when they are inside a decision they have made and the decision has not yet provided them with the next sentence."

    athought "She came here with the decision and without the sentence."

    "Aeron does not fill the silence."

    "He has learned, in the last week, which silences are load-bearing. The silence at Tessa's board at oh-five-thirty. The silence in Selene's quarters last night with the letter on her lap. The silence on Lyra's couch when Lyra was not going to defuse. This is a new silence — he does not know its shape yet — but he recognizes the family. He does not fill silences that belong to the family."

    "Noelle speaks."

    n "I have come to observe you."

    "A beat."

    n "That is the frame I am going to use. I am telling you the frame up front because otherwise I am going to drift into a different frame and you will not know which frame I am operating in, and you are owed the frame."

    a "Okay."

    "He says it the same way he said the other okay. Flat. Not confused. Not welcoming. The tone a person uses when they are accepting a frame without editing it."

    n "I am going to say some things. Most of them are going to be things I have said in some form before. The one that is new is going to be unambiguous when I say it. I am flagging that now so that you do not have to spend the scene trying to figure out which sentence is the new one."

    "Another beat."

    n "I am also not going to ask you to do anything with what I say. That is part of the frame. I have come to the room to put data on the floor, not to ask for a response to the data."

    a "Noelle."

    "He says her name gently. Not interrupting — acknowledging."

    a "I am listening."

    n "I know you are. I am not worried about whether you are listening. I am setting the frame because the frame is the only part of this I trust myself to hold."

    "She looks up from the floor, briefly. Her eyes find his, hold for maybe two seconds, then drop back to the floor. The floor is her safe angle tonight. He is not going to demand she look at him."

    # ========== PHASE 4 — THE FRAMEWORK ENTERS THE ROOM ==========

    n "The framework worked."

    "She says it in the flat analytic voice she used in the ops wing at ten-forty-five."

    n "I want to say that out loud, to you, before I say anything else, because I need us both to be in possession of the same finding: the tool I built predicted the failure and produced an intervention the right size. The intervention was executed. As of ninety minutes ago, your resting heart rate — I am reading it from the medbay feed Tessa set up — has come down from one-oh-four to ninety-three. That is not yet recovery. That is not the recovery signal. But it is the direction of recovery, and the direction is new, and the direction is the framework's output."

    n "The framework worked."

    n "I need you to know that I know it worked, so that what I am about to say next does not get read as doubt about the framework. The framework is fine. The framework did the thing. The framework did what I built it to do."

    "A beat."

    n "The problem is not the framework."

    nthought "He is going to ask what the problem is."

    nthought "No, he is not. He is not going to ask. He has learned in the last week that the right move in rooms like this is to let the other person construct the sentence without a prompt. Aeron has learned not to prompt silences. I did not expect the learning to have progressed this far this fast. I am going to log that observation and move on because logging it is a way of not saying the next sentence."

    nthought "I am stalling."

    nthought "I came here to not stall."

    "She draws in a breath. Small. Measured."

    n "The problem is that I was sitting in the ops wing at ten-forty-five holding a framework I had tuned for six days and watching it produce a scalar for a man I am —"

    "She stops."

    "It is the kind of stopping that happens when a speaker has arrived at a word and has decided, in the last fraction of a second, that the word is the one word they are not yet willing to use, and they are going to route around it and come back for it later."

    n "— watching it produce a scalar for a man, and I realized, while the scalar was producing, that my framework did not have a field for the thing I was feeling about the man."

    n "That is the problem."

    n "The problem is not a framework error. The problem is a categorization error. I have a framework that models Aeron Velarin as a command unit under load, and the framework's variables are all continuous and all measurable, and the framework does not have a column for the kind of weight that the observer of a command unit has when the observer has — "

    "She stops again. This time she does not route around."

    "She finishes the sentence."

    n "— when the observer has stopped being a neutral observer."

    # ========== PHASE 5 — THE STALLING OF THE FLAG ==========

    "Aeron does not move."

    "He does not fill. He does not encourage. He does not ask her to keep going."

    "He is doing, exactly, the thing Selene told him in a4_s02 that shared command required — letting the other person in the room construct their sentence at their own pace without overwriting them. It is a small, perfect act of discipline, and in this room, at this distance, it is a gift."

    "Noelle registers it."

    nthought "He is letting me take as long as I need."

    nthought "That is a thing I did not have a variable for either."

    nthought "The framework assumes that the observer is in a controlled relationship to the system and that the system's responses do not reflect back on the observer's state. In the real room, the system is a man and the man is paying attention to the observer and the observer is being modified by the attention."

    nthought "I am modified. I am sitting on the floor in his quarters on hour six of a stand-down I engineered, and I am modified."

    nthought "The flag I am trying to raise is not a romantic flag. I am not here to ask him for anything. The analytic frame I announced at the door is real. I am going to raise the flag and leave it on the floor between us and walk out of the room without the flag having been picked up."

    nthought "I need to raise it now."

    nthought "I am going to."

    nthought "Say it."

    # ========== PHASE 6 — THE WORD ==========

    n "Aeron."

    a "Yes."

    n "I am going to put a piece of data on the floor. I am framing it as data because that is the only way I can say it. I am aware that the framing is partly a defense and I am choosing to use the defense anyway because I am not here to be raw — I am here to be accurate, and accurate is the closest thing I have to raw."

    n "Here is the data."

    "A beat. Her right hand, flat on the floor, presses down a fraction — the tiny physical anchoring gesture she uses when she is about to say a sentence she has been holding."

    n "I love you."

    "The sentence lands on the floor between them."

    # SFX: a single held low string enters under the silence.

    n "That is the data."

    n "I am telling you because my framework did not include what I am supposed to do with the fact that I love you. I have the variable labeled. I have the variable's current magnitude. I have a noisy estimate of its rate of change over the last six weeks. I do not have a place in the framework to put the variable and I do not have a rule for how to weight it against the other variables and I do not know what decision the framework produces when I include it."

    n "I am sitting on your floor because I do not know what to do with a variable I cannot weight."

    n "I am not asking you to help me weight it. I am not asking you to respond to it. I am not asking you to say it back and I am not asking you to not say it back. I am putting the data on the floor in the room where it belongs and I am going to leave it there and I am going to get up eventually and walk out of this room and I am going to try to keep running the framework on the other variables I can weight, and the data I am leaving here is going to be here whether you touch it or not."

    "She stops."

    "She looks up from the floor, briefly, and her eyes are wet at the lower lid in a way that is not quite crying — the wetness of a woman who has just spent a sentence she had been saving and is now registering the cost of spending it. She is not performing the cost. The cost is simply present in her face because she does not have a routine for hiding it in this room."

    n "That is all. That is the whole thing. Do not respond."

    # ========== PHASE 7 — THE DO NOT RESPOND ==========

    "Aeron does not respond."

    "He heard the instruction. He is going to honor it."

    # --- PLAYER CHOICE: how to honor (or not) her "do not respond" ---
    menu:
        athought "She said do not respond. That is an instruction."

        "Honor it. Be exactly as still as she is.":
            $ rel_bump("Noelle", trust=2)
            athought "The honest move is to be exactly as still as she is. I am going to hold the data on the floor by not picking it up."

        "Say nothing — but sit down on the floor opposite her.":
            $ rel_bump("Noelle", trust=1, affection=1)
            "He does not say a word. He sits down on the floor on his side of the door. The wall between them stays."
            athought "I did not respond. I arrived. Those are not the same thing and she will know the difference."

        "Break the instruction. Say it back.":
            $ rel_bump("Noelle", affection=2)
            a "I love you."
            n "(sharp breath) I said do not."
            a "I know."
            n "(very quietly) ...Thank you for not listening."
            athought "She needed the instruction to be real. She also needed it to be breakable. I chose the breakable."

    athought "I can be still. I have been sitting in this room for three hours and forty minutes. Stillness is the one thing I have in reserve right now."

    "He breathes."

    "He does not speak."

    "The silence after the sentence is not empty. It is the silence of a sentence that is sitting on the floor and being looked at by two people who are not touching it."

    # ========== PHASE 8 — THE LONG QUIET ==========

    "They sit."

    "Noelle keeps her right hand flat on the floor. Her left hand comes up to her knee, then down to her shin, then back to her knee. It is the closest thing she has to a fidget and she is allowing it tonight."

    "Aeron's hands stay on his knees."

    "The vent ticks."

    "The generator hums, low, somewhere under the building."

    "The water stain on the ceiling is doing its thing — he cannot see it from the floor without leaning back, and he is not going to lean back. He knows where it is."

    "Outside the door, the corridor is quiet at this hour. The stand-down has removed him from the ops tempo entirely and the room knows it. Normally his quarters are the destination end-point of a dozen runners a day — someone coming to hand off a datapad, someone with a question, someone with the next thing. Tonight the corridor is empty because the architecture has routed everyone around him. The absence of corridor traffic is the stand-down's signature on the environment."

    "Neither of them speaks."

    "Two minutes. Three. Five."

    nthought "I am not going to leave."

    nthought "I said I was going to leave eventually. I am going to correct that to myself: I am going to leave when it is structurally correct to leave. Leaving right now would be a performance of leaving. Leaving right now would be punctuating the data I just put on the floor with a period, and the data is not supposed to have a period yet — it is supposed to be a sentence that is still in the room after the sentence-speaker has gone. I will leave when the silence has held long enough that my leaving does not cancel the holding."

    nthought "I am going to have to learn to tell when that is."

    nthought "My framework does not have a variable for that either."

    nthought "I am going to note that for the framework's next revision."

    nthought "I am going to note it silently because writing it on the datapad right now would be another performance and the thing I am running away from tonight is performance."

    "She breathes."

    athought "She is not going to leave."

    athought "I was wrong about the eventual. She is going to stay as long as the room needs her to stay, and the room is going to tell her when. That is a different discipline than the one I have been running on. That is Tessa's discipline, in a Noelle shape."

    athought "I did not know Noelle had that discipline."

    athought "That is a thing I am learning about her tonight."

    # ========== PHASE 9 — THE WATER STAIN ==========

    "Another three minutes."

    "Eventually — not suddenly, not punctuated, just eventually — Aeron speaks."

    a "There is a water stain on my ceiling."

    "Noelle's head moves a fraction. She is looking at him, not at the ceiling. She has not seen the stain yet."

    a "Upper-left corner. I have been looking at it for three and a half hours. It keeps shifting shapes. Pangolin. Ferret. A small animal curled around its own tail. I cannot pick which."

    nthought "This is not a subject change. He is not deflecting. He is giving me a piece of his three-and-a-half hours on the floor as a way of making sure the floor has more than one piece of data on it tonight. The water stain is his equivalent of my sentence — the shape of what he has been holding, offered into the room, to stand beside what I put down."

    nthought "He is matching the frame."

    nthought "He is not responding. He is offering."

    n "Where is it."

    a "Above the door. Where the wall meets the ceiling."

    "Noelle tilts her head up."

    "She looks at the ceiling for a long moment."

    n "It is a small mammal of some kind."

    n "I agree that it is small and that it is curled. I do not have enough biological knowledge of mammals to pick a species. The outline has a faint tapering that could be a tail. There is no clear limb definition, which is why I cannot rule between the three candidates you proposed."

    n "If I were logging the stain as a data point for a non-parametric shape classifier, I would label it 'small curled mammal, species uncertain.'"

    "A beat."

    n "That is also, incidentally, the shape of most of the variables I am struggling with tonight."

    "A beat."

    n "Small. Curled. Species uncertain."

    "Aeron makes a sound that is almost a laugh. It is not a laugh. It is the half-exhale of a man who has been holding his face still for a long time and has just been given a reason to let one muscle release. The release is involuntary and small."

    a "Noelle."

    n "Yes."

    a "Thank you for the classification."

    n "You are welcome."

    "A beat."

    n "Thank you for the stain."

    # ========== PHASE 10 — THE STANDING UP ==========

    "They sit with the exchange for another two minutes."

    "The silence after the small-mammal classification is different from the silence after the word. The first silence was heavy and the heaviness was the point. The second silence is lighter — not because the first silence's weight has gone, but because they have both learned, inside of the two-and-a-half meters of floor, that the two silences can coexist in the same room without one of them cancelling the other."

    "Eventually Noelle shifts."

    "She picks up the datapad from the floor beside her. She does not turn it on. She tucks it under her left arm. She does not stand immediately — she sits for another thirty seconds with the datapad under her arm and her right hand still flat on the floor."

    nthought "Thirty more seconds. I am giving us thirty more seconds of the scene's real time before I stand up, because thirty seconds is approximately the time it would take a person to finish a thought they were not performing and had not said out loud, and I want the air in the room to reflect that I am not cutting the scene off, I am reaching the end of it."

    "She counts to thirty."

    "Then she stands."

    "The standing is not graceful. She is stiff from the cold floor. Her right knee makes a small audible click. She does not apologize for the click."

    "Aeron starts to stand."

    n "No."

    "Gently. Not an order — a request."

    n "Stay where you are. Please."

    "He stays."

    "She walks to the door. She puts her left hand on the handle. She does not turn it yet."

    "She speaks without turning."

    n "The data is on the floor. I am leaving the data where I put it. I am not taking it with me. If you do not touch it, it will still be there tomorrow. If you touch it at any point — not tonight — I would like you to tell me, so that my framework's next revision has the information it needs."

    n "I am not going to ask for that again."

    n "I am not going to mention this scene again unless you mention it first."

    n "Those are not rules I am trying to enforce on you. Those are rules I am trying to enforce on myself so that I do not contaminate the measurement I just took by continuing to measure it."

    "A beat."

    n "Aeron."

    a "Yes."

    n "The water stain is a vole. I decided while I was looking at it. Volea. Small rodent. I am logging it."

    "She opens the door. Corridor light — cold blue — falls briefly across the floor of his quarters and lights the place where the datapad was resting ten seconds ago."

    "She steps into the corridor."

    "She closes the door behind her."

    "The latch catches."

    # ========== PHASE 11 — AFTER ==========

    "Aeron sits on the floor with his back against the bunk frame."

    "The room holds exactly the shape it held when she walked in, plus one sentence on the floor that is going to be on the floor for as long as the architecture of the stand-down requires it to be on the floor, plus one word — vole — that he did not know he had been waiting to hear."

    athought "She came here to put a word on the floor and she put two."

    athought "The first word was the one she flagged in advance and spent the scene approaching."

    athought "The second word was the one she chose for my ceiling while she was looking at the stain she had never seen before."

    athought "The second word was given without a flag, freely, at the door, on her way out, as a gift to the room she was leaving."

    athought "I am going to remember that the second word was given without a flag. I am going to remember it because I am trying to learn, this week, the difference between the things people hand me on purpose and the things they hand me by accident, and the thing Noelle just handed me by accident is — she likes me enough to classify my water stain for me on her way out of a scene in which she told me she loves me, and the second classification was not a performance and was not part of the scene's announced frame."

    athought "The framework she brought tonight did not have a field for the variable she was feeling."

    athought "The framework she did not bring — the one that lives under the framework, the one that is not on paper, the one that calls a water stain a vole because she is looking at it and wants it classified — that framework has a field."

    athought "That framework is the one that is in the room with her. The one on the datapad is the one she carries for other people. The one under the datapad is the one she did not know how to make legible to herself until it failed on me."

    athought "She told me that the framework does not work on the man she loves. She did not tell me the other framework. She told me it silently by naming a vole on her way out of the room."

    athought "I am going to hold both frameworks in my head. I am going to hold the silent one more carefully than the spoken one. That is the opposite of the way I used to hold frameworks."

    athought "I am learning."

    "He does not get up from the floor."

    "He stays on the floor with his back against the bunk frame, and the water stain is above him and out of his line of sight from this angle, and the door across the room is closed with the latch caught, and the two and a half meters of floor between where he is sitting and where Noelle was sitting are just floor now, and the sentence she left on the floor is just a sentence, and the vole is a vole, and the stand-down has forty-one and a half hours left to run."

    "He closes his eyes."

    "He does not go to sleep. He closes them because closing them is the smallest correct move in a room that no longer has a task for him, and because his quiet voice — the voice under Marcus's voice, the one he has been getting better at hearing — is saying, very low and very plain:"

    athought "I am going to be very careful with her."

    athought "Not tonight. Not tomorrow. For a long time."

    athought "She brought a framework into a room and the framework failed on me and she did not ask me to fix the framework and she did not ask me to fix her and she did not ask me to fix anything. She put a word on my floor and she named my ceiling and she walked out of my room without asking for anything and that is the most carefully held piece of love anyone has ever handed me in a room."

    athought "I am going to be very careful with it."

    athought "I am going to be careful in the way Selene was careful with the inch of the door, and in the way Tessa is careful with the silent three-times rule, and in the way Lyra was careful with the a3_s23 promise. I am learning these kinds of carefulness from all of them at once."

    athought "Noelle just taught me one I did not have yet."

    athought "The carefulness of data that is too heavy for the framework it is in."

    athought "I am going to make a field for it."

    athought "Not tonight. Tonight I am going to sit on the floor and breathe."

    "He breathes."

    "The water stain — above him, out of sight — stays a vole."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Noelle", trust=1, attraction=2)
    $ flag("a4_noelle_said_love", True)
    $ flag("a4_noelle_framed_love_as_data", True)
    $ flag("a4_aeron_did_not_respond", True)
    $ flag("a4_aeron_and_noelle_shared_floor", True)
    $ canon_set("noelle.framework.known_failure_on_aeron", True)
    $ canon_set("aeron_quarters.water_stain.noelle_classification", "vole")
    $ canon_set("noelle.silent_framework_acknowledged", True)
    $ npc_remember("Noelle", "said_love_framed_as_data", tone="analytic_vulnerability")
    $ npc_remember("Noelle", "named_the_vole_on_the_way_out", tone="love_under_the_framework")
    $ npc_remember("Aeron", "held_the_data_on_the_floor_without_touching_it", tone="discipline_as_care")
    $ tp_seed("a4.noelle.says_love")
    $ tp_seed("a4.noelle.silent_framework")
    $ metric("noelle_intimate_disclosures", delta=1)
    $ scene_mark(_current_scene_id, "exited")
    call li_lore_check("Noelle") from _a4_s13a_lore

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s13a_quiet_after_failure_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Sixteen-fifty. Six hours and five minutes into the forty-eight-hour
#     stand-down established in a4_s13. Aeron has been in his quarters
#     since the ops-wing scene. He has not slept. Noelle comes to him.
# cann.what_happened:
#   - Aeron is alone in his quarters, six hours into the stand-down. He
#     has been lying on the bunk looking at a water stain on the ceiling
#     for three and a half hours — the stain from the closing beat of
#     a4_s13. He cannot settle on what animal it resembles.
#   - Noelle knocks — one knuckle, the knock of a person not wanting to
#     be mistaken for an emergency. He opens the door. She enters,
#     carries her datapad under her left arm, and stops against the
#     inside of the door.
#   - She announces she is going to sit on the floor — she has to
#     narrate the intent because she needs the doing not to catch her
#     in an unplanned posture. She sits with her back against the door.
#     Aeron moves from the bunk to the floor opposite, back against the
#     bunk frame. The distance between them — roughly two and a half
#     meters of open floor — is the scene's chosen distance. Neither
#     closes it.
#   - She declares her frame up front: "I have come to observe you."
#     Analytic register. She tells him she is going to say things, one
#     of which is new, and that she is flagging the frame so he does not
#     have to guess which sentence is the new one.
#   - She reports that the framework worked. Aeron's resting heart rate
#     has dropped from 104 to 93 as of ninety minutes ago — she has
#     been reading the medbay feed Tessa set up. The framework is fine.
#     The framework did the thing it was built to do.
#   - She names the real problem: a categorization error. The framework
#     has no field for the variable she has been feeling about the man
#     it was modelling. She routes around the word on her first approach
#     and then comes back to it.
#   - She says the word. "I love you." Framed as data, as she warned:
#     she has the variable labeled, has its current magnitude, has a
#     noisy estimate of its rate of change over the last six weeks, but
#     does not have a place in the framework to put it and does not
#     know how to weight it. She is telling him because her framework
#     does not include what she is supposed to do with the fact. First
#     time Noelle has used the word 'love' to Aeron.
#   - She explicitly does not ask for a response. "Do not respond."
#     Aeron honors the instruction — exactly. He does not speak. He
#     does not perform refusal. He holds the stillness.
#   - They sit in silence for several minutes. Neither moves to close
#     the distance. The scene's thesis beat: two people in the same
#     room, two and a half meters apart, not speaking, neither of them
#     asking the other to do anything with the fact that one of them
#     just said the word.
#   - Aeron eventually speaks — not about the word, about the water
#     stain. He describes it. Noelle looks up at it for the first time.
#     She classifies it, in analytic voice, as "small curled mammal,
#     species uncertain."
#   - Noelle stands to leave. She asks Aeron to stay seated. At the
#     door, turned away from him, she sets her own rules: the data is
#     on the floor, she is not taking it with her, she will not mention
#     this scene again unless he mentions it first, and she is not
#     going to ask for this again. The rules are to prevent her from
#     contaminating the measurement she just took.
#   - On her way out, without a flag, without announcement, she gives
#     the scene its second word. "The water stain is a vole. I decided
#     while I was looking at it. Volea. Small rodent. I am logging it."
#     This second classification is the scene's structural twin of the
#     first — given without a flag, given as a gift, given to the room.
#   - Aeron, after she is gone, holds both framings in his head. The
#     spoken framework that failed and the unspoken framework that
#     named a vole on its way out. He concludes he is going to hold
#     the silent one more carefully than the spoken one. He does not
#     go to sleep. He closes his eyes.
# cann.aeron_state:
#   - Six hours into a forty-eight-hour stand-down. Unarmored by
#     exhaustion. The intimate mask is not on. He is maximally
#     available to be seen.
#   - He honors Noelle's 'do not respond' with perfect discipline. This
#     is the structural payoff of the Selene-corrected silence-holding
#     he has been learning since a4_s02. He is using the discipline in
#     the register of care rather than the register of command for the
#     first time.
#   - Internal articulation: "The carefulness of data that is too heavy
#     for the framework it is in." Explicit thesis beat. He adds this
#     to a running catalog of the carefulness registers he has been
#     learning from each LI this act (Selene's inch, Tessa's silent
#     three-times, Lyra's cashed promise, now Noelle's unspoken
#     framework).
# cann.noelle_state:
#   - First use of 'love' to Aeron. Framed explicitly as data, not as
#     confession. The framing is a defensive routing she announces in
#     advance and then uses deliberately.
#   - The scene is a document of her framework failing in real time on
#     the one subject she built it for. She acknowledges the failure
#     to him, names it as a categorization error, and puts the failed
#     variable on the floor between them.
#   - The 'vole' on her way out is her giving him the unspoken
#     framework — the one that is not on the datapad, the one that
#     classifies a water stain because she is looking at it and the
#     looking is itself a kind of attention she did not have a word for
#     until tonight. The vole is the love the announced framework
#     could not hold.
#   - Stillness as her fidget-tell. She does not have a body habit
#     under pressure — the stillness IS the tell. The hand flat on the
#     floor beside the datapad is the only anchoring gesture she allows
#     herself.
#   - Self-protective rules at the door: she will not mention the scene
#     again unless he does, she will not ask again. These rules are
#     framed as self-enforcement to preserve the measurement, which is
#     simultaneously (a) emotionally true and (b) in-character for an
#     analyst who is terrified of contaminating her data. The double
#     reading is deliberate.
# cann.thematic_flags:
#   - Data as a register of vulnerability. Noelle can say things in
#     analytic voice that she could not say in any other voice. The
#     analytic register is not distance — it is the armor that lets
#     her be honest.
#   - Two frameworks in one scene: the framework on the datapad that
#     failed, and the framework under it that named a vole. The scene's
#     structural thesis is that the second framework is the real one
#     and she is handing it to him silently.
#   - The chosen distance. Two and a half meters of open floor. Neither
#     closes it. The refusal to close the distance is the care. The
#     scene is Act 4's clearest statement of "presence is enough" in
#     the Noelle register.
#   - Silence as a shared discipline. Aeron's learned silence-holding
#     from a4_s02 is used here in an intimate rather than operational
#     register for the first time. The discipline is the care.
#   - Love framed as a problem the lover is bringing to the beloved to
#     hold together, not a problem the lover is bringing to the beloved
#     to solve. Noelle is not asking to be reciprocated. She is asking
#     him to be in the room with data that has become too heavy to
#     carry alone.
# cann.callbacks:
#   - a4_s13 (the council scene): The 57-hour scalar, the framework's
#     first operational use, Noelle's moment of stillness when Lyra
#     cashed the a3_s23 promise. This scene is the direct psychic
#     aftermath of a4_s13 on its architect. The water stain on the
#     ceiling is a direct visual carryover from a4_s13's closing beat.
#   - a4_s12a (the letter scene): Selene's inch of the door as a
#     carefulness register. Aeron explicitly adds Noelle's register to
#     the running catalog that began with Selene's inch.
#   - a4_s06 (Tessa's silent board): Tessa's discipline of staying as
#     long as the room needs her to stay. Aeron notes internally that
#     Noelle is using a Tessa-shaped discipline for the first time.
#   - a4_s05a (Tessa care-as-command): the medbay feed Tessa set up is
#     the data source Noelle references. The cross-LI plumbing of the
#     stand-down architecture is tightened here.
#   - a4_s04 (Lyra unbuckled) and a4_s12 (Tessa held-not-fixed):
#     'presence is enough' / 'held not fixed' as the Act 4 vocabulary
#     convergence. This scene is the Noelle-register entry in that
#     convergence.
#   - a4_s02 (first cracks): Selene's correction of Aeron's tempo. The
#     silence-holding Aeron learned from that scene is used here for
#     the first time in an intimate rather than operational register.
# cann.character_moments:
#   - Noelle: one knuckle on the door. The announced frame. The
#     rerouting and return to the word. "I love you. That is the data."
#     The 'do not respond.' The hand flat on the floor as her one
#     anchor. The thirty seconds she counts after sitting with the
#     datapad under her arm. The vole on the way out. The closed door.
#   - Aeron: opening the door without speaking. The perfect silence-
#     honor. "Thank you for the classification." The almost-laugh at
#     'small curled mammal, species uncertain.' The internal thesis
#     beat on two frameworks. "I am going to be very careful with her.
#     Not tonight. Not tomorrow. For a long time."
#   - The shared moment: the refusal to close the two-and-a-half meters
#     of floor. The water stain as the room's visual anchor and the
#     vehicle of the scene's second gift.
# cann.block_status:
#   - LINEAR. No branching. No player choice. EMP path only. Intimacy
#     insert during the a4_s13 forced stand-down window.
# cann.requires_followup:
#   - The scene sets up Noelle's later erotic scene. The "I am not
#     going to ask for this again" is a load-bearing promise that the
#     later scene must negotiate against — she is not going to mention
#     it unless Aeron does. Any later Noelle intimacy beat requires
#     Aeron to be the one who opens the subject.
#   - tp_seed a4.noelle.says_love and a4.noelle.silent_framework are
#     True Path markers. The latter accrues only if Aeron's later
#     behavior treats the 'vole on the way out' as meaningful — i.e.,
#     if he begins to operate on the second framework rather than the
#     first.
#   - canon_set aeron_quarters.water_stain.noelle_classification = "vole"
#     is a locked state. Any later scene in Aeron's quarters should
#     respect the vole as a shared private joke / shared private
#     grammar. The stain is Noelle's to have named.
#   - flag a4_noelle_said_love is a one-time canonical first. Downstream
#     Noelle scenes in Act 4 Phase II and Act 5 should read against it.
#   - The 'do not respond' instruction is canonical — Aeron's honor of
#     it is a flagged behavior (a4_aeron_did_not_respond) and any
#     future Noelle dialogue that references the stand-down scene
#     should acknowledge that the honor happened.
