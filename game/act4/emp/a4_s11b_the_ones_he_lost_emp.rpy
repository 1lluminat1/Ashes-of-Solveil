# =======================================================
# ACT 4 - Scene 11b: The Ones He Lost (Empathy Path)
# File: a4_s11b_the_ones_he_lost_emp.rpy
# Type: NEW AERON PROCESSING INSERT — KIA ledger alone
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s11b_the_ones_he_lost_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s11b_the_ones_he_lost_emp:
    $ show_timeline("30th of Forge, 390 A.C.", "02:17", "Phoenix Secondary Base — Ops Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. The ops room at night. Locked mids on Aeron at the cipher table. No
    #         drift. Two locked angles alternating: the three-quarter on his face as he
    #         reads, and the over-shoulder on the datapad screen as the names scroll.
    #         The name list must be legible in the over-shoulder shot. The camera holds
    #         on Liora Rylan's entry longer than any other. When Selene enters, the camera
    #         does not cut — it is already wide enough to hold two chairs. She becomes
    #         present at the edge of the frame and the frame does not adjust. It recognizes.
    # LIGHTING: The ops room at oh-two-hundred. Two lamps. One at the cipher table. One
    #           at the far end, left on from whoever was here last. The feed screens are
    #           on but muted, throwing soft grey wash across the far wall. Aeron's face is
    #           lit by the datapad — underlit, the way a face is lit by a held screen in
    #           a dark room. The underlight is the one visual rule of the scene.
    # SFX: Generator hum, very far. The ventilation tick. The muted feed, one notch below
    #      intelligible. Aeron's breath. A datapad haptic when he scrolls. When he starts
    #      saying names aloud, the base sounds thin out — not cut, just distant, because
    #      the names become the only thing the microphone is listening for. No music at
    #      any point in the scene. The silence is the music.
    # FACE: Aeron — composed at the surface, unraveling underneath. The discipline of the
    #        rule of three trying to hold a list that will not fit. The moment his hand
    #        stops on Liora Rylan's entry is the face beat of the scene. Selene — when she
    #        arrives, she does not show concern. She shows recognition. That distinction
    #        is load-bearing.
    # BLOCKING: Aeron at the cipher table. Datapad propped against a stack of reports.
    #           His coffee cup beside his right hand. Chair angled slightly — he has been
    #           shifting in it for an hour. When Selene enters, she crosses the room
    #           without speaking. She takes the other chair. She does not move it — she
    #           sits in it where it already is. She borrows the coffee after she sits.

    # ========= VOICE BASELINE =========
    # EMP cadence. This is an interior scene. Aeron's voice runs in athought. Spoken lines
    # exist only for the names he reads aloud. Nobody speaks to him. Selene does not speak
    # at all in this scene. Her presence is what closes it. The naming is what fills it.

    # scene bg_ops_room_night_emp with dissolve
    # play ambient "sfx/ambient/ops_room_deep_night.ogg" fadein 3.0

    # ========== PHASE 1 — THE LIST ==========

    # CAMERA: 50mm, locked mid. The ops room at oh-two-
    #         hundred. Wide enough to show Aeron at the
    #         cipher table with the datapad propped against
    #         a stack of reports, the coffee cup beside his
    #         right hand, the far-end lamp someone forgot
    #         to cap burning in the background. The frame
    #         is already wide enough to hold two chairs
    #         even though only one is occupied. This is
    #         deliberate — the composition is waiting for
    #         Selene without telling you it is waiting.
    # LIGHTING: two lamps. One at the cipher table, one at
    #           the far end. The feed screens muted, soft
    #           grey wash across the far wall. Aeron's face
    #           is UNDERLIT by the datapad — the one visual
    #           rule of the scene. The underlight is the
    #           rule and it does not break.

    "The ops room has one person in it."

    "The feed screens are muted. The lamp at the far end is on because whoever left it on forgot to cap it, and nobody has come back to fix the small carelessness. The cipher table is where he always ends up at this hour — not because the cipher is there, but because the table is the largest flat surface in a room otherwise full of consoles. When you need to read something long, you come to the flat surface."

    "He has the datapad."

    "On the datapad: the full Phoenix KIA list. Not Act 4. Not the week. Not the month. All of it. Every name Phoenix has lost since he took command of the rebellion from his father's body."

    "He has been scrolling for twenty-two minutes."

    athought "I came in here after Lyra's. I was going to read one scene's worth of debrief and go to sleep. I opened the wrong file."

    athought "That is a lie."

    athought "I opened the file I came in here to open. I just did not tell myself that was the plan until the file was open."

    "He scrolls to the top."

    "The top of the list is not where it starts. The top of the list is where the command log starts — the day Marcus died and command transferred. Everyone on this list is on this list because a decision Aeron made, or did not make, or made too late, or made too fast, put their name in the column that does not have living people in it."

    athought "That is not fair to the list. That is the version of the list my head writes at two in the morning. The real list is more complicated. Some of these people died because Echelon killed them. Some of them died because the mission required them to take a risk and the risk was theirs to take. Some of them died because somebody else made the wrong call and I was not in the room."

    athought "The head writes the simplified version because the simplified version is easier to hold. The simplified version is a lie that lets me hold the list at all."

    athought "Tonight I do not want the simplified version. I want to try to hold the real one."

    "He starts at the top."

    # ========== PHASE 2 — THE RULE OF THREE ==========

    # CAMERA: alternate between the two locked angles — the
    #         three-quarter on his face as he reads, and the
    #         over-shoulder on the datapad screen as the
    #         names scroll. The names MUST be legible in
    #         the over-shoulder. Do not stylize them. The
    #         camera is treating the names as documents and
    #         the documents as subjects. The alternation
    #         cadence is set by his breath — one angle, one
    #         breath, then the other. Slow.
    # SFX: the datapad haptic when he scrolls. Soft. A
    #      small fleshly sound. When he starts saying names
    #      aloud, the base ambient thins — not cut, just
    #      distant. The names become the only thing the
    #      microphone is listening for. That thinning is
    #      the scene's moral acoustic.

    "Tessa taught him the rule four months ago, standing in front of her board in the clinic annex at the old base. She had her uncapped marker in her hand and a name was on her tongue, and she was waiting to write it, and she was saying it out loud, and she said it three times."

    "He had asked her why three."

    "She had said: {i}Once to hear. Twice to mean. Three times to keep. Anything less and the name is a noise. Anything more and the name is a ritual and the ritual replaces the name. Three is the place where the saying becomes a keeping.{/i}"

    "He had nodded and not used the rule. He had been too full of the operational demands of the week to use the rule. He had thought: {i}that is a nice thing Tessa does.{/i}"

    "He had also thought: {i}I will use it when I have the time.{/i}"

    "He has the time. It is oh-two-seventeen and there is no operational demand in the room and the rule is finally the thing he is here for."

    athought "I am going to say each of them three times. That is the rule. I am going to do it quietly. I am going to do it in my own mouth and not in a log and not on a feed. I am going to do it because Tessa said it is the way the saying becomes a keeping and I have been not-keeping for too long."

    athought "I am starting at the top because the top is where I have to start. If I start in the middle I am choosing. I am not going to choose. The list is the list."

    # Callback: a1_s23_the_sweep / a1_s08_bedroom — "Operation 391"
    athought "The Academy's counter stopped at 391. This list is six times that. The Academy's counter does not have enough digits for this ledger."

    "He scrolls to the first name."

    "He drinks his coffee. He sets the cup down. He looks at the screen."

    a "Selene Valen."

    "He says it out loud. Just above a whisper. The ventilation tick covers it at the far end of the room."

    "His hand is steady."

    a "Selene Valen."

    a "Selene Valen."

    athought "Three. Once to hear, twice to mean, three times to keep. Tessa's rule. She died in the opening week of Act IV, in the Kael corridor, because an ambush I did not see coming came for the wrong person. She is on the list because of a mistake of mine and a cascade of somebody else's. She is also on the list because she put herself between the ambush and Kael and that put-herself-between is what killed her."

    athought "I did not learn that last detail until three days after. I am still learning pieces of the scene from people who were there."

    athought "That is the first name."

    athought "I am going to keep going."

    "He scrolls."

    # ========== PHASE 3 — THE GALA ==========

    # CAMERA: stay in the alternating coverage. Do not
    #         introduce new angles for the Gala names. The
    #         camera is not visualizing the Gala — it is
    #         reading names from a list and the reading is
    #         the scene. Let the names do the work.

    "The next entries come in a cluster. The gala casualties. Seven names on one night. Act I, late. The explosion that killed them was not something Aeron ordered and was not something he could have prevented by any ordinary calculus, but the seven names sit on his list anyway because he was the reason Echelon brought the payload into the room that night, and the brought-payload is what detonated, and the seven were in the room because they were in the room because the aristocracy of Solveil went to the gala because Solveil had galas."

    "He reads the first name."

    a "Harel Voss."

    a "Harel Voss."

    a "Harel Voss."

    athought "He was an under-minister for trade. He was fifty-four. He had a daughter. He had been at the same gala every year for twelve years and he was not supposed to die on the floor of a ballroom. Nobody in that ballroom was supposed to die on the floor of a ballroom. The ballroom was built so that nobody would die on the floor of it, which is one of the reasons ballrooms were built."

    athought "I did not know him personally. I know his name because Tessa put it on her list and because the gala dossier had all of them and because I read the dossier three times the week after."

    "The second gala name."

    a "Ilia Marken."

    a "Ilia Marken."

    a "Ilia Marken."

    athought "She was the daughter of the ambassador from Cresthollow. She was twenty-seven. She had gone to the gala with a friend she had not seen in two years. Her friend survived. Her friend wrote me a letter three weeks later that I have not answered because I did not have an answer she would have wanted to receive."

    athought "I am going to answer the letter this week. I am going to answer it because saying the name three times is not the same as answering the letter and the letter is a separate obligation the list does not discharge."

    "The third gala name."

    a "Domek Hale."

    a "Domek Hale."

    a "Domek Hale."

    athought "Retired admiral. Seventy-one. He had published a memoir the year before. I read the memoir the week after the gala because I wanted to know what kind of man had died in the room my operation pulled the roof down on. The memoir was worse than I expected — which is to say, better. He was a good man who had done three bad things in his career and had tried to be honest about all three."

    athought "The fourth and fifth and sixth and seventh. I am not going to pretend I knew them all. I know their names because the list has their names. I am going to say their names because the list has their names."

    "He says them. Each three times. His hand is still steady."

    a "Ana Pell. Ana Pell. Ana Pell."

    a "Joran Tev— "

    athought "No. Not Joran Tev. Joran Tev is one of the three Lyra saved in Sector 7. Joran Tev is breakfast tomorrow. Joran Tev is not on this list. I almost put him on it because I am tired and the two names start with J."

    athought "I am going to be more careful."

    "He corrects."

    a "Jerem Osale. Jerem Osale. Jerem Osale."

    a "Tova Rell. Tova Rell. Tova Rell."

    "Seven gala names. Twenty-one sayings. He has been at the list for fourteen minutes and the rule of three is working the way Tessa said it would — the names are not a noise anymore. They have begun to have weight."

    athought "She was right about the rule."

    athought "She was right and I did not believe she was right until I was sitting here watching the names stop being noise. That is something I am going to tell her at some point and I am going to tell her without a qualifier the way Lyra told me the sentence without a qualifier."

    athought "Not tonight. Tonight I am keeping the names."

    # ========== PHASE 4 — ELARA'S SISTER ==========

    "He scrolls."

    "A name he knows the story of. Not a name he had personal contact with. A name he has been carrying since Elara told him the story in a corridor three months ago, her voice flat, her hands wrapped around a cup she had not drunk from."

    a "Mira Venn."

    a "Mira Venn."

    a "Mira Venn."

    athought "Elara's sister. Nineteen years old. She was at the wrong intersection at the wrong minute. A Phoenix raid three streets away pushed Echelon response vehicles onto her route. One of the vehicles hit her. She was not a target. She was not anywhere near the operation. The operation that pushed the vehicles was one of mine."

    athought "Elara told me the story in a corridor and she did not cry when she told me. She had done the crying in the months before. She told me because she wanted me to know the name of a person I had not known I had killed. She was not accusing me. That was the thing about Elara — she was not accusing me, and the not-accusing was heavier than accusation would have been."

    athought "I told her I would carry the name. I have been carrying the name. I have not said it out loud until tonight."

    "He says it once more, even though he has already said it three times. A fourth. He permits the fourth — it is the first name on the list he has said four of, and the permission is an accounting error the rule does not allow."

    a "Mira Venn."

    athought "The rule is three. The fourth is for me, not for her. The fourth is because I owe a separate debt to Elara that the list cannot hold."

    athought "Tessa would say the fourth is wrong. Tessa would cap the marker."

    athought "I am going to let the fourth stand. Tessa is not in the room."

    # ========== PHASE 5 — KESA AND JOREN ==========

    "He scrolls further down. Two names in proximity. Fresh ink in the canonical sense — added in the last week, the Sector 7 interdiction."

    a "Kesa Marin."

    a "Kesa Marin."

    a "Kesa Marin."

    athought "She asked for extra rations for a week because she was recovering from a field injury. She had a brother who watched Liora's execution. That is why she came in. That is what Lyra told me in the command center when she delivered the names with the civilian still under her arm."

    a "Joren Hale."

    a "Joren Hale."

    a "Joren Hale."

    athought "His grandmother used to say my mother's name the way people say a prayer. He was quiet about it. He told Lyra once. He stood too close to the board the day after his first operation because the dead column was the only thing in the room not moving."

    athought "He was moving that day. He was moving because he needed to be moving. And then a week later, he was on the column that was not moving, and I was not in the command center when his indicator went dark — I was in the command center, I was at the relay console, my hand was on the relay console and I did not move it. That is the thing I was not supposed to do. That is the whole of Selene's lesson."

    athought "I have said their names now. Out loud. In a room alone. Three times each. That is the keeping."

    # ========== PHASE 6 — THE RULE BREAKS ==========

    # CAMERA: push in on the three-quarter angle — first
    #         camera movement of the scene. Slow, short
    #         push. Land on a tight close when his hand
    #         stops scrolling and the screen settles on
    #         LIORA RYLAN. Hold the tight. The pause on
    #         her entry is the longest single hold in the
    #         scene. His hand does not move for the full
    #         rule-of-three attempt and the collapse of it.
    # FACE: Aeron — the surface composure cracks first in
    #        the eyes, then in the mouth. The discipline of
    #        the rule tries to hold and fails. Do not cut
    #        away during the failure. The face is the beat.
    # SFX: the thinned base ambient drops one more step.
    #      Nothing in the room is audible except the
    #      datapad under his hand and his breath.

    "He scrolls."

    "The next name on the list is the one he has been scrolling toward since he opened the file and has been pretending he was not."

    "His hand stops."

    # VISUAL: Hold on the screen. Let her name sit there, legible in the shot, for three
    # seconds. Then rack focus to Aeron's hand on the datapad. Then to his face.

    "Liora Rylan."

    "He does not say it out loud. Not yet."

    athought "She is on the list because she is on the list. She is on Tessa's board on both columns because that is the rule Tessa made for her. Living because of what she saved. Dead because of what was done to her. Tessa is the only person who has the authority to put a name in both columns and it is because Tessa invented the authority the night before the execution when she realized she was going to have to hold a woman on a column that could not hold her."

    athought "I have been thinking about that both-sides rule since the day after the broadcast. I have been thinking about it the way you think about a pebble in a boot you cannot stop to take off."

    athought "The rule of three is not going to hold her name."

    athought "I do not know how I know that. I know it the way you know a door is stuck before you have tried the handle."

    "He tries the handle anyway."

    a "Liora Rylan."

    "He says it once. The room does not move."

    a "Liora Rylan."

    "He says it twice. The room does not move, and something in him does."

    "He cannot say it a third time."

    "He opens his mouth. The shape of the word is there. His tongue is in the position for the {i}L{/i}. The air is in his lungs. He has said her name out loud every week of his life for thirty-one years and he cannot say it a third time tonight because the third time is the one that is supposed to make the keeping, and the keeping does not work on a name that is already kept."

    athought "She is not a name I am trying to hold. She is the person I learned to hold names from. She is the one who taught me what a name was by having one. She is the person whose hand was in my hair when I was six and who read my first intelligence brief over my shoulder when I was nineteen and who took my wrist three weeks ago and told me she was going to the platform because the platform was the only surface left where the names could be spoken loud enough."

    athought "The rule of three is for names I am trying to move from noise into keeping. She has never been noise. She has been the opposite of noise for every minute of my life."

    athought "The rule does not apply."

    athought "The rule does not apply and the list does not know that. The list is a list. The list has her name in the dead column because the dead column is where the datapad puts names. The datapad does not have a both-sides category. Only Tessa's board does. Tessa's board is a wooden thing she carved by hand because she knew the datapad could not hold a name on two sides at once."

    athought "The datapad cannot hold Liora."

    athought "I cannot hold Liora using the datapad."

    athought "I cannot hold Liora using the rule of three, because the rule of three is for keeping noise into meaning, and my mother has never been noise."

    "His hand is not steady anymore."

    "The datapad is braced against the stack of reports, and that is the only reason it does not move — he is not holding it, his hand has come off the screen and is flat on the table, and the heel of the hand is pressing down into the grain of the wood hard enough that the tendons in his wrist are visible under the lamp."

    athought "This is the rule breaking."

    athought "Tessa told me the rule would hold because the rule has held for twenty-seven years of her practice. She did not tell me the rule would hold for every name. She did not tell me the rule would hold for the name that had taught me what a name was. That part she did not tell me because I did not ask. I did not ask because I did not know the question was a question."

    athought "The rule is a tool. Tools have scopes. Tessa's rule has a scope and the scope is: names that need to move from the category of noise into the category of kept. My mother was already kept. The rule has nothing to do. The rule runs on her name and the rule produces nothing because there is no work for it."

    athought "That is not the rule failing. That is the rule being correct about its scope. The failure is mine for thinking the rule was the whole of the practice."

    athought "Tessa did not give me the whole of the practice. She gave me the part of the practice I could use. The rest of the practice is the part where you sit with a name that the rule cannot hold and you do not pretend the rule held it."

    athought "I am sitting with her name."

    athought "I am sitting with her name and the rule of three did not work and that is the scene."

    # ========== PHASE 7 — THE LEDGER THAT IS TOO LARGE ==========

    "He scrolls once more, by reflex. He does not read the names after hers. The scroll is a motion the hand is making because the hand has been scrolling for twenty-four minutes and it wants to keep scrolling."

    "The list continues below her. More names. Dozens. Eventually hundreds, if he scrolls far enough — the Phoenix rebellion has been at this for longer than he likes to count, and the count is the entire problem."

    "He stops scrolling."

    athought "I got through four."

    athought "Selene. The gala. Elara's sister. Kesa and Joren. That is four — I am counting clusters, not names. If I count names, it is thirteen. Thirteen kept and one that does not fit and the list under her is a column I have not reached."

    athought "The rule does not scale."

    athought "That is the second thing the scene is teaching me tonight. The first thing was that the rule has a scope and the scope does not include my mother. The second thing is that the rule has a capacity and the capacity is smaller than the list. Tessa's rule was designed for a triage medic's list. It was designed for the names of the week. It was not designed for the names of a war."

    athought "I have been trying to use a triage tool on a war ledger."

    athought "The tool is good. The tool is not going to become a bad tool because the ledger is too large. The ledger is too large and the tool and the ledger are not the same object and I have been treating them as if they were the same object."

    athought "I do not have a tool for a war ledger. Nobody does. Tessa does not have one. Lyra does not have one. Selene does not have one. I am looking at the list and there is no tool anywhere in this building that holds the list whole."

    athought "That is the actual thing I came in here tonight to find out. I did not know it was the thing I came in here to find out until I found it out."

    athought "The list is past any mind's capacity to hold. That is not a failure. That is the weight. {i}Seren{/i} was about six faces. The list is a quantity of faces {i}Seren{/i} does not have a number for."

    "He closes his eyes. Not to stop looking — to let the inside of his eyelids be the screen for a second, so the datapad's underlight is not doing the work."

    athought "I am going to have to find a practice that is not the rule of three and not the Academy's grading and not the Aeries priests' {i}Seren{/i} and not any of the tools I have been given, because none of the tools are shaped for the full list."

    athought "I am going to have to build a tool."

    athought "That is an Act V problem. Tonight is an Act IV night and tonight I am just going to sit with the list and with the fact that the rule broke on her name and that the breaking is the accurate thing and not a failure."

    athought "The breaking is the accurate thing."

    "He opens his eyes."

    "The datapad is still on her name. The cursor is blinking in the line where a note would go."

    "He types, very slowly, four letters — then a space — then four more. He is not typing a note. He is not typing her name. He is typing something else."

    athought "I do not have a word for what I am putting in the note field. I am putting it there anyway. The field does not care what the word is."

    "He closes the datapad. He does not save."

    "The screen goes dark."

    # ========== PHASE 8 — SELENE ==========

    # CAMERA: Selene enters without a cut. She becomes
    #         present at the edge of the frame because the
    #         frame has been wide enough the whole scene to
    #         hold two chairs. She crosses the room without
    #         speaking and takes the other chair — the chair
    #         that has been in the frame the entire scene.
    #         She does not move it. She sits in it where it
    #         already is. The composition has become a
    #         two-shot without a cut. The camera has not
    #         re-framed. It has recognized.
    # FACE: Selene — recognition, not concern. The opening
    #        block calls out the distinction as load-
    #        bearing. Her face is the face of a woman who
    #        has been at a cipher table at oh-two-hundred
    #        before and is not surprised to find somebody
    #        else here. She reaches for his coffee. She
    #        borrows it without asking because the borrowing
    #        is the message.
    # SFX: no music enters. Ever. The silence is the music
    #      per the opening block. The scene fades on the
    #      two-shot with the ops room's deep quiet
    #      continuing.

    "He does not know how long he sits there after the screen goes dark. The lamp at the far end of the room has been on for longer than anyone tracks. The feed screens are still muted. The cipher table is the same cipher table it was when he came in, and the flat surface is still a flat surface, and the list is a file that has been closed but not archived."

    "He hears her before he sees her."

    "Not her boots — Selene walks quietly when she is walking for someone. Her voice through the far door — a single word to the overnight ops tech that he does not catch, the rhythm of her voice softened by the space between. Then the ops tech's voice, short, and then the door closing. Then quiet."

    "Then Selene at the threshold of the ops room."

    "She does not say his name. She does not ask what he is doing. She does not ask if he is alright. She does not do any of the things a person who is doing this wrong would do."

    "She crosses the room."

    "She comes to the cipher table. She pulls the other chair out — the one angled away from his — and she sits in it. She does not move it to face him. She sits in the angle it already has, which puts her shoulder in his peripheral vision and her body at a diagonal to his and her face turned two-thirds toward the far wall."

    "It is the angle of a person who is here to be beside, not to look at."

    "She does not speak."

    athought "She came here because someone told her I was in here. Or she came here because the overnight ops tech reported the ops room light to her. Or she came here because she has a mental map of the building at oh-two-hundred and my ending up at this table at this hour was not a surprise to the map."

    athought "Probably the third."

    "Her hand moves. Not to him."

    "Her hand moves to his coffee cup."

    "It is a cold cup now — he has not drunk from it in twenty-five minutes and the ops room is not a warm room and the coffee has given up being coffee in any useful sense. She picks it up anyway. She drinks the last quarter of it in one swallow."

    "She sets the cup back down on his side of the table, where it was."

    "She is looking at the far wall."

    athought "She drank the cold coffee. That is the thing she just did. She did not offer to get me a new cup. She did not ask if I wanted one. She drank the last of the old one because the last of the old one was what was on the table and drinking it was a thing to do with her hands that was not nothing and also not an event."

    athought "Marcus taught her this. I know he did. I know he did because this is exactly the move a person makes who has learned how to be beside somebody in a room without colonizing the room."

    athought "She is the Marcus of this scene too. She is aware of it. She is not flagging it. She is just doing it."

    "The lamp hums."

    "The feed wash moves along the far wall by one degree, because the ventilation passed and the feed screen flickered once."

    "Neither of them speaks."

    "He does not move to pick up the datapad again. She does not look at the datapad at all. The datapad is a closed device on a table and the closed device is not what she is here for."

    athought "I am not going to tell her the rule broke on my mother's name."

    athought "I am going to tell her eventually. Not tonight. Tonight the telling would turn the scene into a debrief and this scene is not a debrief. This scene is the scene where the rule broke and she came and she drank the coffee and neither of us said a word about any of it."

    athought "That is the scene."

    "The ops room is quieter than it was an hour ago. The base is three hours from shift change. The list on the closed datapad is the list it was. Liora Rylan is in the dead column of the datapad and in both columns of Tessa's board and in the one column of him that does not have a name because he is the column."

    "Selene's shoulder does not move."

    "His shoulder does not move."

    "The scene ends there."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("aeron_read_full_kia_list_alone", True)
    $ flag("rule_of_three_broke_on_liora", True)
    $ canon_set("aeron.ledger_exceeds_rule_of_three", True)
    $ canon_set("aeron.needs_act5_practice", True)
    $ npc_remember("Aeron", "kept_four_names_cluster", tone="rule_applied")
    $ npc_remember("Aeron", "could_not_say_liora_third", tone="rule_broke")
    $ npc_remember("Selene", "drank_cold_coffee_beside_him", tone="marcus_inheritance")
    $ rel_bump("Selene", trust=1)
    $ metric("aeron_grief_ledger", add=1)
    $ tp_seed("a4.aeron.rule_of_three_fails")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s11b_the_ones_he_lost_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same night as a4_s11a. After Aeron leaves Lyra's altar space. Oh-two-hundred.
#     Ops room. Alone with the Phoenix KIA list in full (not Act 4, not the week —
#     all of it, since he took command from Marcus).
# cann.what_happened:
#   - Aeron opens the full Phoenix KIA list on a datapad at the cipher table. He
#     has been scrolling for 22 minutes before the scene's first action. He decides
#     to apply Tessa's rule of three to the names from the top.
#   - He gets through four name clusters (13 names):
#       * Selene Valen (not the Selene — a prior Phoenix named Selene Valen,
#         killed early Act IV in an ambush; she put herself between the ambush
#         and Kael)
#       * The gala casualties: Harel Voss, Ilia Marken, Domek Hale, Ana Pell,
#         Jerem Osale, Tova Rell (one more implied but not named — 7 total).
#         He almost confuses Joran Tev (the living fighter Lyra saved in s05)
#         with a gala name because fatigue.
#       * Elara's sister: Mira Venn. He permits a FOURTH saying because he owes
#         Elara a separate debt the list cannot hold. Notes that Tessa would cap
#         the marker at four. Tessa is not in the room.
#       * Kesa Marin and Joren Hale (Sector 7 — a4_s05).
#   - He scrolls to Liora Rylan. He tries the rule of three. He gets TWO sayings
#     out — "Liora Rylan. Liora Rylan." He cannot say the third. The rule breaks
#     on her name.
#   - He realizes WHY it breaks: the rule of three is for moving names from noise
#     into keeping. Liora has never been noise. She is the person who taught him
#     what a name was. The rule's scope does not include her. The rule did not
#     fail — it was correct about its scope. The failure was his assumption that
#     the rule was the whole practice.
#   - Second realization: the rule has a CAPACITY. It was designed as a triage
#     medic's tool. The full war ledger exceeds the rule's capacity. He does not
#     have a tool — nobody in the building has a tool — for a ledger of this size.
#     This is an Act V problem. Tonight he names it and leaves it named.
#   - He types four letters, a space, four more letters in the note field of
#     Liora's entry. The content is intentionally not specified in the text. He
#     does not save. He closes the datapad.
#   - Selene enters. She does not speak. She crosses the room, pulls the other
#     chair out in the angle it already has, sits beside him without moving it
#     to face him. She drinks the last quarter of his cold coffee. She sets the
#     cup back where it was. She does not look at the datapad. The scene ends
#     with neither of them moving or speaking.
# cann.aeron_state:
#   - Applying Tessa's rule of three for the first time in full discipline. The
#     rule works on 13 names and then fails in a specific, instructive way on
#     the 14th.
#   - The scene is the first time Aeron names aloud that the Phoenix ledger
#     exceeds any tool he currently has. He is not despairing — he is
#     recognizing scope.
#   - The "fourth" saying on Mira Venn is a small break of the rule that he
#     permits for a reason the rule does not accommodate (personal debt to
#     Elara). Foreshadows his Act V practice-building.
#   - Mother's name: the rule's silent failure on Liora Rylan is load-bearing.
#     He cannot say it a third time. He sits with that. The inability is not
#     failure — it is accurate information about the scope of the tool and the
#     category Liora occupies in him.
# cann.selene_state:
#   - She arrives without being summoned. Her appearance is the scene's closing
#     gesture. She does not speak a single line. She borrows his cold coffee,
#     drinks the last quarter, sets the cup back. This is explicitly framed in
#     Aeron's internal monologue as a Marcus-taught gesture: "be beside somebody
#     in a room without colonizing the room."
#   - She is the Marcus of this scene (again). Aeron notices and does not speak
#     the noticing out loud.
# cann.path_tracking:
#   - EMP path. Linear. No branching. Solo processing scene with one silent
#     companion at the close.
#   - flag aeron_read_full_kia_list_alone. flag rule_of_three_broke_on_liora.
#     canon_set aeron.ledger_exceeds_rule_of_three. canon_set
#     aeron.needs_act5_practice (the seed that he will have to build a new tool
#     in Act V).
#   - rel_bump Selene trust +1 — the unspoken companionship registers.
#   - metric aeron_grief_ledger add 1. tp_seed a4.aeron.rule_of_three_fails.
# cann.thematic_flags:
#   - Tools have scopes. Borrowed practices work inside their scope and fail
#     outside it. The failure-outside is not corruption — it is information.
#   - The Phoenix ledger is past any mind's capacity. Aeron names this. He
#     does not have a practice yet. The naming is the scene's main operational
#     product.
#   - Liora as a category rather than a name. She is not on the list to be kept;
#     she is the one who taught him what keeping was. The rule cannot operate
#     on its own origin.
#   - Rule of three vs. Seren: two tools, two scopes. Seren holds six faces.
#     Rule of three holds triage names. Neither holds a war ledger. The gap is
#     where the Act V practice will be.
#   - Presence without speech (Selene drinking the cold coffee). The opposite
#     register from the mercy-call scene and the Lyra prayer scene. Three
#     different modes of being-with in one night: Lyra (naming), the list (solo
#     discipline), Selene (silent company).
# cann.character_moments:
#   - Aeron: the four-cluster discipline. The almost-Joran-Tev slip. The
#     permitted fourth saying for Mira Venn. The two-saying stall on Liora.
#     The four-letter-space-four-letter note he types and does not save. The
#     unsteady hand pressed flat on the wood.
#   - Selene: wordless entrance, angle of the chair, drinking the cold coffee.
#     The scene is an economy of gesture and her gestures are load-bearing.
#   - Named dead surfaced: Selene Valen, Harel Voss, Ilia Marken, Domek Hale,
#     Ana Pell, Jerem Osale, Tova Rell, Mira Venn, Kesa Marin, Joren Hale,
#     Liora Rylan. Previously known names plus several new gala-name entries
#     elaborated here to give the list texture.
# cann.callbacks:
#   - a2_int_04_tessa_torins_name: Tessa's rule of three. The rule is invoked
#     explicitly by name ("once to hear, twice to mean, three times to keep").
#     This scene is the first time Aeron has applied the rule at scale.
#   - a3_int_08_tessa_the_board_emp: the both-sides rule for Liora. Referenced as
#     the only authority that can hold her in both columns and the reason the
#     datapad cannot hold her the same way.
#   - a4_s05_delegation_test_emp: Kesa Marin and Joren Hale. Aeron applied the
#     rule on them silently in s05; here he applies it openly and aloud.
#   - a4_s11a_prayer_after_mercy_emp: Seren. Referenced as a tool whose scope is
#     six faces and does not scale to the full list. Three tools now
#     distinguished by scope: rule of three, Seren, full-ledger (not-yet-built).
#   - a4_s01_morning_after_broadcast_emp: the cipher table as the recurring
#     place where Aeron ends up at odd hours. Selene again at the cipher table
#     without being summoned.
#   - a3_s22 Liora's execution: the reason her name is in the list at all.
#   - Elara sister backstory: referenced in earlier interludes, invoked here by
#     Mira Venn's full name entering canon.
# cann.block_status:
#   - MAJOR PROCESSING BEAT. Linear. EMP only. No branching. Solo interior with
#     silent-company closer.
# cann.requires_followup:
#   - Aeron WILL have to build an Act V practice for a ledger that exceeds the
#     rule of three. The need is now named on record.
#   - The four-letter-space-four-letter note in Liora's entry is deliberately
#     opaque. A later Act IV or Act V scene may reveal what he typed. The
#     blank is a hook.
#   - The almost-confused Joran Tev / gala-name slip is a fatigue detail that
#     could be called back in a later mistake scene.
#   - Selene drinking the cold coffee is a body motif. It can be referenced
#     wordlessly in any later Selene-with-Aeron scene as a shorthand for this
#     night.
#   - Mira Venn's full name is now canon. Elara's sister has a name on record.
#   - Aeron has not told Tessa that the rule of three was good enough to apply
#     at scale. He resolves silently that he will tell her, without a qualifier,
#     not tonight. This is a hook for a later Tessa scene.
