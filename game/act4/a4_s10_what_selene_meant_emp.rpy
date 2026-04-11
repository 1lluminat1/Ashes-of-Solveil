# =======================================================
# ACT 4 - Scene 10: What Selene Meant (Empathy Path)
# File: a4_s10_what_selene_meant_emp.rpy
# Type: THESIS CENTER — shared authority lesson, Kael story completed
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s10_what_selene_meant_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s10_what_selene_meant_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: One room. Two people. 50mm, locked, patient. This is not a scene with
    #         coverage — it is a scene with held two-shots. The camera moves exactly
    #         twice. Once, early, to find Selene's hands. Once, late, to hold on the
    #         window. Otherwise it stays on the pair of chairs and the small table
    #         between them. The silences get the same length of frame as the lines.
    #         When Selene says the thesis line — "You are still trying to delegate
    #         tasks. I am asking you to delegate the question." — the camera is on
    #         Aeron's face, not hers. The line is a line about him.
    # LIGHTING: The archive annex at the back of the eastern wing. Phoenix does not
    #           use this room for ops. It is a cartography overflow — two walls of
    #           old map rolls, a high narrow window that only clears the horizon
    #           when the lamps are low. Selene has brought a portable work lamp.
    #           One lamp. The room is a low warm amber and a cold blue window at
    #           the far wall. The two chairs sit in the amber. The window is the
    #           cold edge neither of them is sitting in.
    # SFX: Deep base hum, very far. The old heating pipe in the corner ticks twice
    #      at long intervals — the room's only sound other than the voices. The
    #      ticking is not music. It is a body-of-the-building fact. No ambient
    #      score. One held low note enters at the final beat and fades on black.
    # FX/COMP: Two chairs, angled toward each other — the furniture is already in
    #          this configuration when they arrive. Selene did not move it.
    #          Someone else, years ago, had a conversation here. The room remembers.
    #          A pitcher of water and two tin cups on the small table. Selene pours
    #          once for each of them during the scene and does not top up.
    # BLOCKING: Neither of them commands this room. The chairs are equal height.
    #           Selene sits first. Aeron sits second. At the turn, Selene stands and
    #           crosses to the window — not to command the space, to get distance
    #           from what she is about to say. She finishes the Kael story from the
    #           window with her back three-quarters to the room. When she returns to
    #           the chair she is lighter by a specific small amount. She sits again.
    # FACE: Selene — the most stripped-back register she has in this chapter.
    #       Not commander-Selene. Not the Marcus inheritor. The Selene who is
    #       twenty-four in the story and fifty-one in the chair at the same time.
    #       Aeron — open, listening, braced. He does not try to route tonight.
    #       The routing is not an option in this room.

    # ========= VOICE BASELINE =========
    # EMP cadence. Selene drives the scene at a pace slower than her command register.
    # Her diction is cleaner, shorter. She does not use tactical vocabulary. When she
    # uses a word like "command" she uses it the way a person uses the word the second
    # time they have said it that month, not the fortieth. Aeron's lines are short —
    # he is here to hear, not to answer. His internal voice carries most of his side.
    # The silences between exchanges are load-bearing and should be directed as beats,
    # not elided.

    # scene bg_archive_annex_emp with dissolve
    # play ambient "sfx/ambient/deep_base_hum_distant.ogg" fadein 3.0

    # ========== PHASE 1 — THE ROOM NEITHER OF THEM COMMANDS ==========

    "She found him in the corridor outside the war room at 0630, before the morning brief, and said only: 'Come with me.'"

    "He came."

    "She did not take him to the ops table. She did not take him to the cipher room. She did not take him to the war room or the command center or the cartography vault or the planning alcove or any of the rooms in this building where one of them is in authority."

    "She took him to the archive annex."

    "He has not been in this room in nine weeks. He has been in it exactly twice since Phoenix moved to the secondary base — once to pull an old topographic roll, once by accident, looking for a room that turned out to be next door. He does not command this room. Neither does she."

    "That is why they are here."

    "The annex is a narrow space at the back of the eastern wing. Two walls of old map rolls in brass-capped tubes. A high narrow window on the far wall. A low table between two chairs someone had arranged a long time ago for a conversation no one on Phoenix remembers having."

    "A pitcher of water. Two tin cups. A single portable work lamp Selene has carried in with her and set on the table."

    "She sits first."

    "He sits second. He does it slowly — not because the sitting is difficult, because the sitting is the first gesture in a scene whose shape he does not know yet, and he is trying not to ruin the shape by arriving at it too fast."

    "Neither of them speaks for a moment."

    "The old heating pipe in the corner ticks once."

    athought "She chose this room."

    athought "That is the first thing I am going to pay attention to. She did not take me anywhere either of us has authority. She took me to a room where the authority is in the furniture and the furniture is older than both of us."

    athought "I am going to let her lead. I am going to let her lead in a register I have not let her lead in since she walked into the Sector 7 briefing yesterday morning."

    "Selene pours water. One cup for each of them. She does not hand him his — she sets it in front of him so he can reach for it or not."

    "He reaches for it. Sets it down again without drinking."

    sel "Aeron."

    a "Selene."

    sel "I have been deciding whether to finish the Kael story since yesterday in the alcove."

    "She says it flatly. Not cold — measured. The way a person says a sentence they have been carrying in their mouth for hours and have only just decided to set down."

    sel "I started it in the alcove because I needed you to have the beginning. I did not finish it because the finish was not a thing I could give you in front of Noelle's projection."

    sel "I am finishing it now. In a room neither of us runs. That is deliberate. I am not going to pretend it is not."

    a "Okay."

    sel "That is the only context I am giving you before I start. I am not going to preface it further. The story does its own work if I let it."

    # ========== PHASE 2 — THE MORNING HE DIED ==========

    sthought "Start where I stopped."

    sthought "I stopped at Marcus making me count the names of the three the lieutenant lost. I did not tell Aeron the lieutenant's name because in the alcove the lieutenant was the scaffolding. Tonight the lieutenant is the load-bearing wall."

    sthought "His name was Kael."

    sel "The lieutenant's name was Kael."

    "She lets the name sit in the room."

    sel "He was twenty-six. I was twenty-four. He had been under me for nine months. Marcus assigned him to me when he decided I was ready to carry a subordinate — I was not running a wing yet, I was running a six-person cell, and Kael was my second. I had never had a second before. He was the first person I had professional authority over in my life."

    sel "I liked him. I am going to say it that flatly because the scene does not work if I pretend I liked him in the abstract. I liked him the way you like a person you are going to keep — I liked the way he listened in briefings, I liked that his handwriting on intel reports was the cleanest in the cell, I liked that he made me laugh exactly twice in nine months and both times he was not trying to."

    sel "I also thought he was going to be a better commander than I was in about five years. I told Marcus that. Marcus did not disagree."

    "She takes a drink of water. The first one. The cup is down again before she speaks."

    sel "The operation Marcus put him in charge of — the one I would have run differently — was a riverbank extraction in the third district. Six civilians, two Echelon spotters, a window of eleven minutes. Kael's plan was precise. He wrote it with me looking over his shoulder. I did not flag the thing I would have flagged. That is the first failure of the morning and I am not going to hide it."

    a "Selene—"

    sel "Let me get to the end of the sentence. I did not flag the thing I would have flagged because I thought it was my job to let him run his plan and not shape it into my plan with my hands. I had been in command training with Marcus for three years at that point. Marcus was teaching shared authority. This was six weeks after the Tessa-style lesson where Marcus told me I had to let a subordinate make a call I disagreed with because disagreement is not the same as wrong."

    sel "The thing I did not flag was the extraction window. Kael had the window at eleven minutes. I thought it was nine. I did not say so because in command training you do not override the commander's read of the clock. I filed the disagreement and did not speak it."

    sel "The window was nine minutes. The second Echelon spotter arrived on the clock I would have put on the board. Three civilians extracted. Three civilians on the bank. Kael went back for them."

    sel "He got them into the boat."

    sel "He was on the bank when the second spotter opened fire."

    "She is looking at the lamp now. Not at him."

    sel "He was shot twice before he went down. The first round did not kill him. It went through the meat of his shoulder. He was on the ground talking on the comms relay, giving me the rest of the brief with his hand on his shoulder and his voice completely steady, because Kael was the kind of person who gave briefs with his hand on his shoulder and his voice completely steady."

    sel "The second round killed him. I heard it on the comms. I heard the comms go flat."

    "Two seconds. The pipe ticks."

    sel "That is not the part of the story that teaches the lesson. That is the operational part. I am giving it to you because without the operational part the lesson does not make sense."

    athought "She is telling me the operational part because if she did not give it to me my first impulse would be to ask her for it, and asking her for it would collapse the scene back into the register we came in here to avoid."

    athought "She is navigating me. She is navigating me with a care I did not know she knew how to use with me."

    # ========== PHASE 3 — WHAT KAEL SAID ==========

    sel "What Kael said before he died is the part of the story that teaches the lesson."

    sel "I have never told anyone the exact words. I have told three people that he said something before he died. I have never told anyone what it was."

    sel "I am telling you now."

    "She stops. She looks at the water. She does not drink it."

    sel "Between the first round and the second round, he had about ninety seconds. I was on the comms relay from the command post. Marcus was standing behind me with his hand on the back of my chair and he did not say a word during the entire exchange."

    sel "Kael said — and I am quoting him, I have not paraphrased this since — Kael said: 'Selene. I would have taken the nine-minute window if you had told me it was nine.'"

    "The sentence goes into the room and does not move."

    sel "He did not say it as an accusation. He said it the way he said everything — level, with the clean handwriting of his voice, because Kael was even on the ground with a hole in his shoulder. He said it as a data point. He was giving me the thing I needed to carry away from the operation because he was a better second than I deserved and he was giving me the handover before the handover was something he could do from the ground."

    sel "And I said — and this is where the story actually turns, Aeron, this is the part I did not give you in the alcove — I said: 'I am sorry I did not say it. I am going to carry that.'"

    sel "And Kael said: 'No.'"

    sel "He said no. On the comms. With the round in his shoulder and a minute left in his lungs. He said: 'No. You do not get to carry it alone. It was our operation. If you try to carry it alone, you will make the same mistake on the next one, because the mistake was that you thought the clock was only mine to put on the board. Please. Promise me.'"

    sel "And then he said the sentence that has been in my mouth for twenty-seven years."

    sel "He said: 'The weight belongs to more than one person. Agree that it does. That is the promise.'"

    "She finally drinks the water. Just a sip."

    sel "The second round came about thirty seconds after that. I did not answer the promise before the second round. I answered it on the comms into a dead channel."

    sel "I said yes. To the silence."

    sel "Marcus was the only other person who heard me say it. He never asked me what I said. He never acknowledged hearing it. He walked me out of the command post and he put me on leave for two weeks and when I came back he did not bring it up. He never brought it up. He let me have the promise as mine."

    # ========== PHASE 4 — THE LONG QUIET ==========

    "The room is quiet."

    "The pipe ticks. The lamp is a steady warm."

    "Aeron does not speak for a long moment. He has the water cup in his hand. He has not drunk from it since he picked it up."

    athought "Kael said the weight belongs to more than one person. He said it while he was dying. He said it to Selene, who was twenty-four, and Marcus was standing behind her with his hand on the back of her chair, not saying anything, because Marcus knew the lesson was not his to deliver."

    athought "I am inside the lesson now. I am not being delivered it — I am being inherited into it."

    athought "She is the Marcus of this scene in a way the alcove scene did not quite finish making true. Last night she gave me the version of the story that protected her. Tonight she is giving me the version that protects me."

    athought "I am not supposed to thank her for it. I know that already. I am supposed to receive it."

    "Selene does not press the silence. She lets it have its full weight."

    "After a long moment she picks up her own cup. Drinks a second sip. Sets it down."

    sel "I have told you the story. The story is the preamble. I want to say the thing I came in here to say, now that the preamble is in the room."

    "She stands."

    "Not abruptly. She stands the way a person stands when the sitting has done its part of the work and the standing is what is left. She crosses the room to the narrow window. Her back is three-quarters to him. She does not turn all the way."

    "She is looking at the horizon through the cold edge of the frame."

    # ========== PHASE 5 — THE THESIS ==========

    sel "You are still trying to delegate tasks."

    "She says it to the window."

    sel "I am asking you to delegate the question."

    "The sentence enters the room."

    "Aeron does not move."

    sel "Yesterday in the alcove you heard me tell you the beginning of the Kael story and I watched you absorb it as a story about tactical delegation. You took it as a lesson about whose hand is on the plan. That is the tactical layer and it is real and it is not the layer I was pointing at."

    sel "I was pointing at the question the plan serves."

    sel "The question inside the Sector 7 operation was not 'what route do we take to the corridor.' The question was 'what do we owe the corridor.' The question of the plan is always upstream of the plan. It is the thing the plan is trying to answer. A commander who shares the plan but not the question is a commander who has kept the authorship of what the operation is for and has only distributed the authorship of how."

    sel "That is what you have been doing."

    sel "You share the how. You have shared the how beautifully in the last two weeks. You let Lyra run the corridor. You let me overrule you in the briefing. You let Noelle model both plans and refused to use her numbers to break her. You have done the hard tactical work of not being the only hand on the plan."

    sel "But the question is still yours."

    sel "The question of what Phoenix is for, the question of who the next two names belong to, the question of what the grief is supposed to do in the room where Kesa Marin and Joren Hale are going to sit on the board — you took all of those questions onto yourself last night in the alcove. You did it with discipline. You did it the way a commander does it. Zira told me an hour ago that she watched you do it in the mess, and I want you to know I am not using that against her telling me. I am using it because the mess version is the proof the alcove version was not the whole picture."

    "She pauses."

    sel "You listened to the Kael story last night and I watched you turn it into a private promise. You heard Kael say the weight belongs to more than one person and you agreed to share the weight and you went and sat alone in a mess hall at four in the morning taking a name onto your ledger as if the ledger had a single authorized signatory."

    sel "I am going to say the sentence again because it is the whole thing. You are still trying to delegate tasks. I am asking you to delegate the question."

    sel "Kael did not say 'share the plan.' He said 'agree that the weight belongs to more than one person.' Those are different sentences. The first one is a management sentence. The second one is an ontological sentence. Shared command is an ontology before it is a workflow. If you treat it as a workflow, you will run it beautifully and the grief will still be yours alone at the end of it, because you will have distributed the doing and kept the being."

    sel "And the being is the part that kills you."

    # ========== PHASE 6 — THE SENTENCE ABOUT RESPONSIBILITY ==========

    "She is still at the window. She has not turned around."

    sel "Kesa Marin's name sat on you alone last night because you are sharing authority while keeping responsibility singular."

    sel "You let Lyra make the plan. You let Selene set the assignment. You let Noelle run the numbers. You let the command structure redistribute every single task that was redistributable. And then — when the names came in and the projection was running and the alcove was dark — you took the names alone."

    sel "Because the names were the one thing that did not have a task attached."

    sel "The names were a question. Who is responsible for the two Phoenix we lost tonight. And you answered the question the way you have been answering that question since your father's voice was on the comms — you said: I am."

    sel "You said it in the mess hall with a mug of coffee you were not drinking. You said it at the alcove table with a projection you were not looking at. You said it in the cipher room the night of the broadcast and you said it on the balcony after the gala and you have been saying it for every loss Phoenix has absorbed since the Lower Spans."

    sel "I am."

    sel "I am the one who is responsible."

    sel "That is the sentence I am asking you to stop saying."

    "She finally turns. Her face is in three-quarter profile. The lamp catches the side of it and the window light catches the other side. She is in both lights."

    sel "I am not asking you to stop being responsible. I am asking you to stop being the only one who is."

    sel "The rule of three is failing you — Tessa's rule, the one you have been borrowing silently since the alcove, the one you have been performing alone. It is failing you because the rule is not designed for solo performance. The rule of three is a group rule. It belongs to more than one mouth. Tessa's mother gave her the rule, and Tessa said it aloud to her patients for years, and the counter was not alone in the room when the naming happened — the counter was in the room with the person being named."

    sel "You are saying the names alone. That is why the saying is not landing right. That is why you are counting them like a private tax. The rule is not a tax. The rule is a shared ledger and you have been running it as a sole proprietorship."

    sel "I am asking you to let us count."

    sel "Not instead of you. With you."

    # ========== PHASE 7 — HE CANNOT ABSORB IT ==========

    "Aeron does not answer."

    "His hands are on the cup. The water is still in the cup. He has not drunk any of it."

    athought "I heard her."

    athought "I heard her the way a person hears a sentence that is too big for the room the sentence was said in. The sentence is taller than the annex. The annex is going to have to grow to hold the sentence or the sentence is going to have to shrink to fit, and neither of those things is going to happen in the next sixty seconds."

    athought "She just told me that sharing authority is an ontology before it is a workflow. I know what those words mean. I know them the way I know my name."

    athought "I do not know how to do the ontology part. I know how to do the workflow part. I did the workflow part yesterday in the briefing with Lyra and I have been doing the workflow part all week. The workflow part is harder than it used to be and I was proud of myself for doing it and she just told me that the workflow part is the easy part."

    athought "Shared being. She said being. She said the being is the part that kills you. She said it standing at a window with her back three-quarters turned and it is the single most exact sentence anyone has said to me in this chapter."

    athought "I am not going to absorb it tonight."

    athought "I know I am not going to absorb it tonight. I know because I can feel the shape of the sentence in my sternum and the shape is not a shape that fits inside a night of sleep. It is not a shape that fits inside a week. It might be a shape that fits inside a month if I am honest with it and let the month do the work."

    athought "She is not asking me to absorb it tonight."

    athought "She is asking me to let the sentence be in the room between us."

    athought "That is a thing I can do. The letting is the only thing I can do. The letting is smaller than the absorbing and the letting is the part that is mine."

    "He looks up at her. She is still half at the window."

    a "Selene."

    sel "I am listening."

    a "I heard the sentence."

    sel "I know."

    a "I do not know how to answer it."

    sel "I know that too. I am not asking you to answer it tonight."

    a "I am — the shape of it is bigger than anything I know how to do with it tonight. I am not going to pretend it is not."

    sel "Good."

    a "Good?"

    sel "Good because the pretending would be the thing that ended the scene. You not pretending is the reason I brought you to a room neither of us runs. In a room either of us ran you would have felt an obligation to answer and you would have produced an answer that was closer to a plan than a reception. I did not come here for you to plan. I came here for you to hear the sentence and have it in you."

    sel "You are hearing it. That is sufficient for the night."

    # ========== PHASE 8 — THE RETURN TO THE CHAIR ==========

    "She crosses back to the chair. She sits again. She is lighter — not visibly, the way a person who has set down a weight they were not aware they were carrying is lighter. The lightness is inside the posture, not on the surface."

    "She picks up the water. Takes a third sip. Sets the cup down."

    sel "There is one more thing I want to say before we leave this room. It is smaller than the thesis. It is the thing I have been deciding whether to say since I sat down."

    a "Say it."

    sel "Kael's promise was to share. Mine was to inherit the sharing into every commander who came after me. Marcus never made me make that promise. I made it to myself in the command post the morning Kael died, and I made it again about six times over the next ten years to various people who did not know I was making it."

    sel "I made it to you the day we agreed to co-command at the start of this chapter. I did not tell you I was making it. I was making it."

    sel "I am telling you now because I want you to know the shape of the thing I am holding. I am not being your Marcus because Marcus was elegant at this and I am not elegant at this. I am being your Marcus because the inheritance wanted a container and I was the container nearest to the inheritance when the inheritance needed to move."

    sel "You are going to be somebody's Marcus one day. I do not mean Kael's way — I mean the inheritance way. Somebody is going to need the question delegated from you to them, and you are going to have to do it in a room neither of you runs, and you are going to say words that feel too big for the room, and the person is not going to absorb it that night. They are going to take it home and carry it the way you are going to carry this home tonight and I am going to tell you something about the carrying."

    sel "The carrying gets lighter."

    sel "Not because the sentence gets smaller. Because you grow around it. The shape of you gets bigger and the sentence starts to fit. That is the only version of this that I have found in twenty-seven years and I am giving it to you for free because I am done hoarding it."

    "He does not answer right away. The lamp is a steady warm. The pipe ticks."

    athought "The carrying gets lighter. Not because the sentence gets smaller. Because you grow around it."

    athought "That is a thing I am going to keep."

    athought "I am going to keep it the way I keep the names. The names and the sentence are going into the same ledger and the ledger is not mine alone. I do not know how to do the not-mine-alone part yet but I know that is the word for the ledger."

    athought "Shared ledger."

    athought "Shared being."

    athought "I am going to let both of those be in the room tonight. That is the smallest version of the letting that I can do honestly."

    a "Selene."

    sel "Yes."

    a "I do not know how to delegate the question yet. I know the sentence. I do not know the action."

    sel "Nobody does on the first night. The action is not a single gesture. The action is a habit you build by doing it wrong four or five times while someone you trust is in the room with you."

    a "Are you going to be in the room with me while I do it wrong?"

    "Selene pauses. Not because the answer is uncertain. Because the answer is the thing the whole scene has been working toward and she wants to hand it over clean."

    sel "Yes."

    sel "Until I am not. And then Lyra. And then Tessa. And then Zira. And then Noelle. And then the Phoenix fighters I do not know the names of yet, because you are going to build a command culture where the question is plural and the names are plural and the ledger is plural and I am only the first page of the book, Aeron. I am the first page. The book is a long one. I would like very much to not be the only page you read in it."

    "He closes his eyes for a second."

    "When he opens them she is still there."

    sel "That is everything I had."

    a "Okay."

    sel "We can leave the room now."

    a "Not yet."

    "He says it before he decides to."

    a "One more minute in the room."

    "Selene nods. Small. The nod is a yes and a permission at the same time."

    # ========== PHASE 9 — THE MINUTE ==========

    "They sit in the annex for another minute."

    "Neither of them speaks. The pipe ticks twice. The lamp holds. The window at the far wall has the first pale edge of morning on it that was not there when they came in."

    "Aeron's hands are still on the water cup. He has not drunk it."

    "Selene's hands are in her lap. She is not looking at him. She is letting the minute be a minute."

    athought "She brought me to a room neither of us runs because the sentence she was going to give me could not survive the commanders in either of us. She had to strip the commander off. She had to sit in the chair as the twenty-four-year-old and the fifty-one-year-old at the same time and I had to sit in a chair that was not mine to command."

    athought "The minute is her letting the sentence breathe. She is not ending the scene. She is letting the scene end itself by having been what it needed to be."

    athought "I am going to remember this room for the rest of this chapter. I am going to remember the two chairs and the old table and the pitcher and the tin cups and the pipe that ticked twice and the window that turned pale while we were in here."

    athought "The annex is now a room I have been in. I do not know if I will ever come back. I know I have been in it."

    "The minute finishes."

    "Selene stands first. She picks up the tin cups and carries them to the small shelf near the door where someone, years ago, used to stack them. She puts her cup down. She does not put his down — his is still in his hand."

    "She turns at the door."

    sel "I am going to the morning brief. I am going to run it today. You are going to sit in the secondary chair and you are going to listen and you are going to let Lyra lead the Phoenix update and you are going to let Noelle lead the adaptation model and you are going to say the things that are yours to say when they are yours to say and not before. Can you do that?"

    a "Yes."

    sel "Good."

    sel "I am not going to check on you after the brief. I am not going to come find you in the alcove tonight. I am not going to send anyone to the mess hall to watch you not drink coffee. This is the part where the scene becomes a scene you have to carry for a while before anyone checks on you again. I am going to tell you that up front so you do not wonder whether my absence is a judgment."

    sel "It is not a judgment. It is the shape of the lesson."

    sel "You are going to be alone with the sentence for a day or two. When you are ready to say something back to it, there will be a room that is not this one and a person who is not me, and the room and the person will both be in the building, and you will find them when the finding is ready."

    a "Understood."

    sel "Do not understand it yet. Just walk out with me."

    "He stands. He carries the cup with him. He does not put it down on the shelf. He is going to put it down somewhere else — he does not know where yet — and he is not going to pretend the choice of somewhere-else is not part of the scene."

    "They walk out of the annex together."

    "The door closes behind them."

    "The camera holds on the empty annex for a beat. The two chairs, the table, the lamp still on, the pitcher with water in it, the single cup on the shelf, the pale window."

    "Then black."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=1)
    $ flag("selene_finished_kael_story", True)
    $ flag("aeron_received_delegate_the_question", True)
    $ npc_remember("Selene", "gave_aeron_kael_last_words", tone="inherited_promise")
    $ npc_remember("Selene", "delegate_the_question_sentence", tone="thesis_delivered")
    $ npc_remember("Aeron", "heard_kael_weight_belongs_sentence", tone="unabsorbed_but_kept")
    $ npc_remember("Aeron", "cup_in_hand_leaving_annex", tone="ledger_not_yet_placed")
    $ canon_set("aeron.shared_authority_lesson", "in_progress")
    $ canon_set("selene.kael_promise_transmitted", True)
    $ canon_set("room.archive_annex_used_for_thesis", True)
    $ metric("aeron_delegate_the_question", set_to=0)
    $ tp_seed("a4.selene.delegate_the_question")
    $ nudge_poly("authority", "shared")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s10_what_selene_meant_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II) — THESIS CENTER
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after a4_s09a (Zira mess call-out), just before the morning brief.
#     Selene finds Aeron in the corridor outside the war room and takes him to the
#     archive annex — a room neither of them commands. This scene is the Act IV
#     Phase II thesis beat for the Selene thread and for the chapter as a whole.
# cann.what_happened:
#   - Selene takes Aeron to the archive annex at the back of the eastern wing. The
#     room is cartography overflow with two chairs, a small table, a pitcher and
#     two tin cups. Neither of them has authority in this room — the choice of
#     location is deliberate and load-bearing.
#   - Selene finishes the Kael story she started in a4_s05. She tells Aeron the
#     lieutenant's name was Kael. She gives the operational preamble: riverbank
#     extraction, eleven-minute window that was actually nine, Kael shot twice
#     on the bank, ninety seconds between rounds.
#   - Between the rounds, Kael said on the comms: "Selene. I would have taken the
#     nine-minute window if you had told me it was nine." Selene told him she
#     would carry it. Kael said: "No. You do not get to carry it alone. It was
#     our operation. If you try to carry it alone, you will make the same mistake
#     on the next one, because the mistake was that you thought the clock was
#     only mine to put on the board."
#   - Then Kael delivered the line Selene has been carrying for twenty-seven
#     years: "The weight belongs to more than one person. Agree that it does.
#     That is the promise."
#   - Selene tried to answer the promise but the second round came. She said yes
#     into a dead channel. Marcus was standing behind her and heard but never
#     acknowledged it.
#   - Selene crosses to the narrow window (the scene's second and only other
#     camera move) and delivers the THESIS LINE: "You are still trying to
#     delegate tasks. I am asking you to delegate the question."
#   - She elaborates: the question of what the plan is for is upstream of the
#     plan. Aeron has been sharing the how beautifully but keeping the question
#     to himself. She names the diagnostic: "Kesa Marin's name sat on you alone
#     last night because you are sharing authority while keeping responsibility
#     singular."
#   - She names the rule of three as a SHARED rule that Aeron has been
#     performing in sole proprietorship. "Tessa's mother gave her the rule, and
#     the counter was not alone in the room."
#   - She tells him that shared command is an ontology before it is a workflow.
#     "Shared being. The being is the part that kills you."
#   - Returning to the chair, she gives him the consolation form of the thesis:
#     "The carrying gets lighter. Not because the sentence gets smaller. Because
#     you grow around it."
#   - Aeron asks if she will be in the room with him while he does it wrong. She
#     says yes — "Until I am not. And then Lyra. And then Tessa. And then Zira.
#     And then Noelle. And then the Phoenix fighters I do not know the names of
#     yet... I am only the first page of the book."
#   - Aeron requests one more minute in the room. They sit for a full minute in
#     silence. The window at the far wall shows the first pale edge of morning.
#   - Selene stands, puts her cup on the shelf, leaves her instructions for the
#     morning brief (she will run it today, Aeron will sit in the secondary
#     chair), and tells him explicitly that the scene is a scene he must carry
#     alone for a day or two before anyone checks on him. "This is the part
#     where the scene becomes a scene you have to carry for a while before
#     anyone checks on you again... It is not a judgment. It is the shape of
#     the lesson."
#   - They leave the annex together. Aeron carries his cup out — he has not
#     drunk from it. The cup is the load-bearing prop for Aeron's unresolved
#     state. He does not put it down where Selene put hers. He will put it down
#     somewhere else when the scene has had time to settle.
# cann.aeron_state:
#   - Open, listening, braced. He does not try to route the scene once. He
#     knows at the door of the annex that the scene is not his to command and
#     he lets it not be.
#   - He does not absorb the thesis tonight. The scene is explicit that he is
#     not supposed to. The success condition is: the sentence is in the room
#     between them, and Aeron is carrying it out with him in the water cup.
#   - His internal state at close is "shared ledger / shared being" as the two
#     pieces of vocabulary he has to carry. He does not know what the action is
#     yet. That is correct and canonical.
# cann.selene_state:
#   - The most stripped-back register she has had in the chapter. Not
#     commander-Selene, not the Marcus inheritor. The Selene who is twenty-four
#     in the story and fifty-one in the chair at the same time. This is the
#     version of her that has not appeared in the game before.
#   - Her Kael backstory is now fully canonical. The lieutenant's name is Kael.
#     The operation was a riverbank extraction in the third district. The window
#     was nine minutes not eleven. Kael's last words are now canonical quotes:
#     "The weight belongs to more than one person. Agree that it does. That is
#     the promise." Any future reference to Kael must be consistent with this.
#   - Selene's own inheritance — "I made the promise to myself in the command
#     post the morning Kael died" — is now canonical backstory.
#   - "I am only the first page of the book" is Selene's explicit framing of
#     her own role in Aeron's arc. This is load-bearing for any Selene scene
#     where she steps back from the foreground.
# cann.path_tracking:
#   - EMP path. Linear. No branching, no player choice. Thesis scene.
#   - rel_bump Selene +1 trust. She has given Aeron the version of her Kael
#     story that she has not given anyone in twenty-seven years.
#   - flag selene_finished_kael_story True.
#   - flag aeron_received_delegate_the_question True. This is a prerequisite
#     flag for the Act IV Phase III beats.
#   - canon_set aeron.shared_authority_lesson "in_progress". Deliberately NOT
#     "learned" — the scene does not resolve into absorption.
#   - canon_set selene.kael_promise_transmitted True.
#   - canon_set room.archive_annex_used_for_thesis True — the room is now a
#     location with scene history. Future uses should carry this memory.
#   - metric aeron_delegate_the_question initialized at 0. Future scenes where
#     Aeron delegates the question (not just tasks) should increment it.
#   - tp_seed a4.selene.delegate_the_question.
#   - nudge_poly authority toward shared.
# cann.thematic_flags:
#   - THESIS: "You are still trying to delegate tasks. I am asking you to
#     delegate the question." This is the Act IV Phase II thesis line. It is
#     load-bearing for the remainder of the act and for Act V.
#   - Shared command is an ontology before it is a workflow. The chapter's
#     cleanest statement of the distinction.
#   - The rule of three is a SHARED rule. Aeron has been running it as sole
#     proprietorship. Tessa's mother gave it to Tessa, Tessa has been trying
#     to give it to Aeron, Aeron has been receiving it as a private tool. The
#     scene corrects the misunderstanding without saying Tessa's name harshly.
#   - "The carrying gets lighter. Not because the sentence gets smaller.
#     Because you grow around it." Selene's inheritance lesson. A counterweight
#     to the grief discipline of a4_s05's "necessary is not worth it."
#   - The archive annex as a neutral room. The physical form of "somewhere
#     neither of us commands." Future Act IV and Act V scenes may reuse the
#     annex for other conversations that require the same register.
# cann.character_moments:
#   - Selene: turns away from Aeron at the thesis — she delivers the line to
#     the window, not to him. She has never done this in the chapter before.
#     The turning away is the gesture of someone handing over a sentence she
#     does not trust herself to hold while watching the receiver. The scene's
#     single most load-bearing blocking choice.
#   - Selene: quotes Kael's exact last words for the first time in twenty-seven
#     years. The quoting is the gesture that makes the scene a transmission
#     and not a retelling.
#   - Aeron: requests "one more minute in the room" before they leave. The
#     first time in Act IV he has asked for time in an intimate register. This
#     is a small canonical first.
#   - Aeron: carries the water cup out of the annex. He does not drink it. He
#     does not put it down where Selene put hers. The cup is the prop of his
#     unfinished state. Future scenes may return to the cup.
# cann.callbacks:
#   - a4_s05_delegation_test_emp: the Kael story's first half. Selene's Marcus
#     anecdote. "Necessary is not worth it." This scene is the second half of
#     both the Kael story and the lesson.
#   - a4_s05a_you_are_not_a_machine_emp: Tessa's rule of three, used silently.
#     Selene names the misuse here without naming Tessa harshly. The two
#     scenes are in structural dialogue.
#   - a4_s09a_she_calls_him_out_emp: Zira's call-out in the mess. Selene
#     explicitly references it in the thesis — "Zira told me an hour ago that
#     she watched you do it in the mess." The cross-LI intelligence is
#     deliberate: Zira told Selene, Selene is using it to reinforce the
#     diagnosis without undermining Zira's private approach.
#   - a2_int_tessa_torins_name: the origin of the rule of three. Selene is
#     calling back to it structurally, not by name.
#   - a3_int_tessa_the_board_emp: the board that holds names. Selene's "shared
#     ledger" language is a cousin to Tessa's board.
#   - Marcus as Selene's teacher: the full version of the Marcus inheritance
#     is now canonical. Selene's "I am being your Marcus because the
#     inheritance wanted a container" line is the scene's explicit framing.
# cann.block_status:
#   - MAJOR SCENE. Linear. EMP path only. Thesis center of Act IV Phase II.
#     Prerequisite for Phase III beats that assume Aeron has received the
#     delegate-the-question lesson even if he has not yet absorbed it.
# cann.requires_followup:
#   - Aeron's unabsorbed state is deliberate. Phase III scenes should read
#     against aeron.shared_authority_lesson "in_progress" — he is trying, he
#     is failing, he is trying again. The lesson does not resolve into
#     "learned" until a scene that has not been written yet.
#   - The water cup is a recoverable prop. A later scene can have Aeron put
#     it down in a specific room as the physical form of his having settled
#     the sentence into a location. The scene of putting the cup down is not
#     this scene.
#   - Kael's canonical last words must be quoted consistently in any later
#     scene that references them. The operative clause is "The weight belongs
#     to more than one person. Agree that it does."
#   - "I am only the first page of the book" is load-bearing for Selene's own
#     arc. Any later scene where Selene steps back from primary authority
#     should reference this framing.
#   - The archive annex as a location is now canonical. If Phase III needs a
#     second scene in a neutral room, the annex is the first candidate.
#   - The mercy call scene (a4_s11) is the operational test of the lesson.
#     Aeron should carry the unabsorbed sentence into the captured-six
#     scenario. That scene reads against this one directly.
