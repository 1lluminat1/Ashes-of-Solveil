# =======================================================
# ACT 4 - Scene 23: Aeron Alone (Obedience Path)
# File: a4_s23_aeron_alone_ob.rpy
# Path: OB
# Type: AERON STATE BEAT / SOLO SCENE (non-erotic, internal)
# Character Focus: Aeron (alone, entire scene)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s23_aeron_alone_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s23_aeron_alone_ob:
    $ show_timeline("DAY 55", "03:30", "Phoenix Base — Aeron's Quarters")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. The locked-ness is the whole aesthetic. No drift.
    #         No handheld. Open wide on Aeron's quarters: bed made (never
    #         slept in for three nights in a row), the small desk by the far
    #         wall, the single chair pushed back from the desk, the tactical
    #         terminal on standby, the small mirror on a stand at the desk's
    #         left edge. Aeron enters from the war room door in his day coat.
    #         The camera does not follow him to the bed. He does not go to
    #         the bed. He walks to the desk. He sits. That is the establishing
    #         geography.
    #         Then: a locked medium on Aeron at the desk, three-quarter
    #         profile, the mirror at frame-left. When he picks up the letter
    #         the camera cuts to an insert top-down on his hands unfolding
    #         the page. Then it returns to the locked medium. Then, when he
    #         looks into the mirror, the camera cuts to a locked frontal from
    #         inside the mirror's plane -- the viewer sees the reflection
    #         directly. Aeron's face fills the frame. The reflection holds for
    #         a long beat. The scene's only "camera move" is this substitution
    #         of the camera for the mirror.
    #         End: the scene returns to the locked medium as he refolds the
    #         letter, closes the jacket, stands, and leaves the quarters. The
    #         camera does not follow him to the ops table. It holds on the
    #         empty desk. Then it cuts to the empty war room at 0500 with
    #         Aeron entering and taking the head chair. That is the final
    #         frame of the act.
    # LIGHTING: Aeron's quarters at 0330. One desk lamp. Everything outside
    #           the desk lamp's circle is dark. The bed is in dark. The door
    #           is in dark. The mirror is half in the lamp's circle, half
    #           outside. His reflection in the mirror is lit only by what the
    #           lamp spills sideways. It is not flattering light. It is
    #           enough light to see a face by.
    #           The war room at 0500: overheads at 40%. Same cold working
    #           light as the ops room in a4_s21. The head chair is empty.
    #           Aeron enters and sits. The lighting does not change.
    # SFX: Loop -- quarters ambient. The HVAC. The low hum of the standby
    #      terminal on the desk. No corridor footfalls. Everyone else is
    #      asleep. One-shots -- the jacket unbuttoning at the top (a single
    #      fabric click). The waxed paper envelope leaving the inner pocket
    #      (dry whisper). The page unfolding. The page refolding. The jacket
    #      closing. The chair pushed back. The quarters door cycling. The
    #      war room door cycling at 0500. The head chair when he sits in it
    #      (a small leather creak). No music. No score. The scene's score is
    #      absence.
    # FX/COMP: The desk: a clean working surface. A dormant terminal. A small
    #          mirror on a stand at the left edge of the desk. A single pen.
    #          A glass of water he has not drunk. The jacket on his back, not
    #          on a chair. He has not taken it off in twenty-one hours.
    #          The mirror: small. Eight inches by six inches. Steel frame.
    #          Not decorative. A field mirror, the kind you use to check a
    #          seal on a gasket or to signal across a corridor. He bought it
    #          in Sector 9 two years ago and has not used it for its intended
    #          purpose in at least eleven months. He has not looked into it
    #          in four months.
    # BLOCKING: Aeron sits at the desk. He does not stand during the solo
    #           except at the very end when he leaves. The scene is entirely
    #           a man sitting in a chair with a page in his hand and a
    #           mirror at his left. The stillness is the event.
    # CANON: AERON SOLO STATE BEAT. OB soliloquy. The third read of the letter.
    #        The first look into the mirror in four months. The scene is
    #        almost entirely athought. The spoken lines are minimal -- one or
    #        two to himself, barely audible. The scene ends with Aeron
    #        arriving at the ops table at 0500 and taking the head chair
    #        (not the side chair). This is the structural mirror of the EMP
    #        track, where EMP-Aeron at the end of a4 takes the side chair.
    #        OB-Aeron takes the head. The head chair is the final image of
    #        Act 4 on the OB track.
    # FACE: Aeron. Only Aeron for the whole scene. The mask is off because
    #        there is nobody to wear it for. What is under the mask is not
    #        softer. It is the same face, now not performing. That is the
    #        scene's quiet horror: the private face and the public face are
    #        the same face. The mask and the man have converged.

    # ========= VOICE BASELINE =========
    # Almost entirely athought. Internal. Low, flat, accurate. The voice of
    # a man doing inventory on his own participation in the last year.
    # Two spoken lines, each at whisper volume, each a single sentence or two.
    # They are not addressed to anyone. They are not confessions. They are
    # small audible confirmations of thoughts that needed to become sound
    # for one second to be real. Then silence returns.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - 0330]
    # Late. The council ended at 0630 the previous morning. Aeron spent the
    # day in the war room, the corridor, the intelligence cell, the relay
    # room. He ate once -- a ration bar at 1400. He has been back in the
    # quarters for twelve minutes. He has not taken the jacket off. He will
    # not take the jacket off.

    #scene bg_aeron_quarters_ob_latenight with dissolve
    #play ambient "sfx/ambient/quarters_latenight.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DESK ==========

    "Aeron sits. He does not sit heavily. He sits the way he does everything now, which is with the exact amount of force required for the action and no more."

    "The desk lamp is already on. He left it on when he went out this morning because he knew he would come back after dark. The desk lamp's circle holds the mirror and his right hand and a patch of the desk surface. Everything else is out."

    "He places his hands on the desk, flat, the way he placed them on the war room table at the council. He holds the position for a beat."

    athought "Twelve minutes in this room. Twenty-one hours in this jacket. The letter has been against my chest for twenty-two hours and forty minutes."

    athought "I am going to take it out now. I am not going to put it back on the desk overnight. I am going to read it a third time and put it back inside the jacket and go to the ops table at 0500. That is the shape of the next ninety minutes."

    # ========== PHASE 2 -- THE ENVELOPE ==========

    "He unbuttons the top button of his day coat. He reaches inside with his right hand. The envelope comes out. The waxed paper has warmed against his body temperature. The paper is a small pocket of heat against the cold of the desk."

    "He sets the envelope on the desk in the circle of the lamp. He looks at it for a beat without opening it."

    athought "The envelope is not heavier than it was at 0500 yesterday morning. Nothing has been added. Nothing has been subtracted. The page is still the page my mother wrote when I was six. The sentence in the middle is still the sentence in the middle."

    athought "What has changed is the day I am reading it on. The first read was yesterday pre-council. The second read was yesterday pre-council. The third read is now, on the other side of a council that authorized the assassination of Rhea Vestin. The page is the same. The reader is not."

    # ========== PHASE 3 -- THE UNFOLD ==========

    "He opens the envelope. The page comes out. The creases are set. He unfolds along the creases and places the page flat on the desk."

    "He reads. Third time. Slower than the first. Slower than the second."

    athought "'My dear Marcus.' The greeting he has already read three times now."

    athought "'I am writing you a letter I will not send because if I send it you will read it at the war room table and you will find three reasons to set it aside. I am writing it for myself because I need the sentence to exist on paper.'"

    athought "'The boy is asleep. The boy is six tonight. He can hear me breathing through two walls -- I can hear him breathing through two walls. I do not know what that means for how you and I will go on from here but I know it means the room has one more person in it than the room had before we had him, and the person has not yet been shaped, and my work at this table from this point forward is shaping.'"

    athought "The boy. I am the boy. I am the person in the other room who was breathing through two walls when she wrote the sentence."

    # ========== PHASE 4 -- THE CENTRAL LINE ==========

    athought "Then the center of the letter. The part I already know by heart after two reads and will know by heart after this one."

    athought "'I fell in love with the pause. The moment between the decision and the execution. The moment you used to have, and the moment you have stopped having. I can no longer love a man who does not pause.'"

    "His eyes move across the sentence. He does not look up. He does not look at the mirror. Not yet."

    athought "She is not describing the pause as a theological object. She is not calling it the hand of God or the soul speaking or any of the things Lyra would call it if Lyra wrote this sentence. She is calling it a moment. A moment between the decision and the execution. A gap. A breath. A small piece of time the operator does not use for anything and which she loved because it was the small piece of time that revealed that the man she had married contained a second person."

    athought "Marcus used to have a second person inside him. A person who paused. She fell in love with the second person. Then the second person stopped appearing. Then she fell out of love with the first person because the first person was all that was left."

    athought "The letter is a grief document for a second self."

    athought "The second self is the self that had a pause."

    # ========== PHASE 5 -- THE INVENTORY BEGINS ==========

    athought "Now apply it."

    athought "Apply the letter to me. The way Lyra applies a scripture to an operational decision. Read the text. Apply the text. See what the text reveals about the ground truth the text is now being read against."

    athought "Inventory."

    # ========== PHASE 6 -- THE INVENTORY (ITEM 1) ==========

    athought "I have killed Selene."

    athought "Not with my hands. With a decision I made in a corridor that I did not pause inside. The Sector 9 operation that killed her had a beat inside it where I could have authorized a different insertion angle. I did not pause on that beat. I picked the angle that was fastest. The angle that was fastest was the angle that put Selene in the sightline of the Echelon response unit that killed her. My decision-to-execution gap on that angle was under two seconds. My mother would have said that under-two-seconds is the absence of a pause."

    athought "I have killed Selene."

    # ========== PHASE 7 -- THE INVENTORY (ITEM 2) ==========

    athought "I have killed three civilians in Sector 12 last week because they were on a list I signed."

    athought "I signed the list at 0447 one morning. I read the list once. I did not read the list twice. A pause would have been the second read. I knew there might be names on the list I did not want to have signed. I decided that the cost of the second read was higher than the cost of the signatures. I decided it in under five seconds. The signature was flat and clean. Nobody in the room contested it because nobody in the room had time to contest it -- the speed of my signature set the tempo of the room."

    athought "Three civilians died because I signed a list I did not read twice. The math of that is the math of a man who has replaced his pause with a tempo."

    # ========== PHASE 8 -- THE INVENTORY (ITEM 3) ==========

    athought "I have watched seven Phoenix operators die because I was slower than Rhea Vestin's Echelon specialist."

    athought "Siri Ondel. Aman Kesh. Tove Rainer. Parth Oren. Mina Vael. Dalen Huo. Iris Serrano."

    athought "Slowness in the operator's sense is not the same as pausing. I was slower at the prediction task because Noelle's model had not been retrained yet and I was running the previous confidence. I authorized an exposure with the previous confidence and the exposure was exposed. Seven people I had named by name were killed in six minutes."

    athought "I did not pause before the authorization. If I had paused I would have asked whether the previous confidence was still current after Rhea's last movement trace. I did not ask. I authorized."

    athought "The failure was not slowness. The failure was the absence of a pause. My operational speed is high. My operational pause is gone. These two facts are not the same fact."

    # ========== PHASE 9 -- THE INVENTORY (ITEM 4) ==========

    athought "I am going to kill Rhea Vestin in seven days."

    athought "The mission was authorized this morning. The council did not deliberate. I watched it happen. I confirmed it. Zira pushed for six days. I held at seven because the rotation point at dawn on day seven is the thinnest detail window. The reason I know the thinnest detail window is that I have been reading Zira's Ghostline traces on Rhea for a month and I never told anyone I was reading them. I have been planning my half of this operation at a distance from the other half of this operation for the same month Zira has been planning her half. We converged in the council because we had both been pre-staging. Noelle had been pre-staging. Lyra had been pre-staging at the altar. Nyra had been pre-staging at the ritual level. The council was five operators arriving at the same assassination from five angles by independent work."

    athought "Nobody in that room paused."

    athought "Nobody in that room proposed. Everybody in that room confirmed."

    athought "The pause she is describing in the letter is the pause we did not take as a room. We have become a room that does not pause. I am at the head of that room."

    # ========== PHASE 10 -- THE INVENTORY (ITEM 5) ==========

    athought "I have sealed a second oath with Nyra."

    athought "The first oath was at the funeral. The second oath was six days ago in the chapel. Nyra sealed it with the ritual language she has been refining since Selene died. I participated. I consented to the language. I let her name me co-sovereign of the return state of the operations we run from this base."

    athought "A pause would have been the beat between the first oath and the second oath where I asked whether the second oath was a necessary addition to the first or a replacement for something else. I did not ask. I signed the ritual with my body in the chapel."

    athought "Nyra is not a mistake. Nyra is a structural response to the absence of the pause. She has built herself into the operational geometry because the operational geometry needed a function nobody else was providing. The function is: holding the return state of the operator so the operator can return."

    athought "The return state is the thing I have stopped being able to manage for myself. Nyra is managing it. I am letting her. The letting is a form of pause-substitute -- I am paying Nyra to hold the space a pause would have held."

    athought "She said my mother's name at the door of the war room today. She did it because I would not. That was also a pause-substitute. She is spending the words I am no longer capable of spending."

    # ========== PHASE 11 -- THE INVENTORY (ITEM 6) ==========

    athought "I have taken Zira's body after she demanded I make her feel like something."

    athought "She came to me in the corridor last week and she said make me feel it. Not make me feel good. Make me feel it. Meaning: I am inside an operation that is costing me my membership in my own body and I need you to come to the workshop and give me back a small piece of the body through the specific channel we have been using for a year."

    athought "I went. I did what she asked. I do not know if I did it well. I do not know if she felt like something afterward. She was angry with me at the start of the session and she was angry with me at the end. The anger was not about me. The anger was about what she had to ask for and the shape of who had to ask for it and the arithmetic of being a woman who did not leave the building and is not going to leave the building."

    athought "I did not pause between her asking and my going. I do not know if the absence of the pause was part of what she needed -- come when summoned, no beat between the summons and the arrival -- or whether the absence of the pause is the same absence I am now cataloguing from my mother's letter."

    athought "I am not sure I am capable of distinguishing between what my consenting partners need from me and what I have simply stopped being able to do. That is a diagnostic failure. A year ago I could tell the difference. Tonight I cannot reliably tell the difference."

    # ========== PHASE 12 -- THE INVENTORY (ITEM 7) ==========

    athought "I have let Noelle declare herself a weapon in front of me and I did not stop her."

    athought "The word was hers. I did not introduce the word. I heard the word. I received it. I did not say 'Noelle, you are a person with a model, you are not the model.' I did not pause on the word. The word entered the room and became the new operational description and I moved on to the next thing."

    athought "At the council today she said 'I will not fail again.' The 'I' in that sentence was the weapon, not the person. I did not hear the 'I' as a person's 'I' at the council. I heard it as the weapon's 'I'. I did not correct it. I authorized the weapon's 'I' with a nod."

    athought "Noelle walked into this base with a mathematical model and a careful mouth. She is now a mathematical model that the mouth serves. The transition happened on my watch. I did not cause it. I also did not pause it."

    # ========== PHASE 13 -- THE INVENTORY (ITEM 8) ==========

    athought "I have watched Lyra bless a strike team and I did not release her from it."

    athought "Not tomorrow's strike team -- previous strike teams. Three prior missions. Each time Lyra did the altar rite. Each time I could have said 'Lyra, you do not have to do this.' Each time I knew the release would have cost us operationally because the blessing is now a tactical requirement for the operator's return state. Each time I calculated that the cost of releasing her was higher than the cost of making her carry the blessing."

    athought "Today at the council she told me she needs to do it at the altar specifically because the altar is the institutional venue that permits her to continue to pray afterward. She is protecting her prayer practice by taking the blessing out of her private voice and putting it into the voice of the building. The building is now the thing that blesses the strike team. Lyra is the mouth the building is using."

    athought "She said it with no tremor. She has already done the ethical arithmetic. I watched her say it. I did not pause. I acknowledged the altar blessing for the record and moved to Zira."

    athought "I am not supposed to release her. She is not asking to be released. She is asking to be permitted to preserve a small corner of her interior by specifying the venue. I can do that for her. I am doing it. I am also noting that releasing her is the move a man with a pause would have considered and I did not consider it."

    # ========== PHASE 14 -- THE INVENTORY (ITEM 9) ==========

    athought "I have told Tessa to try harder to know that a girl was nineteen."

    athought "Her name was Siri Ondel. She was nineteen. She was on the list Rhea killed yesterday. Tessa lost her. Tessa knew her -- Tessa had done the intake physical and Tessa had signed the medical clearance for the operational role Siri was running when she died."

    athought "After the loss I said one sentence to Tessa. The sentence was 'Try harder to know that a girl was nineteen.' I do not remember the exact context. I remember saying it. I remember Tessa not responding."

    athought "The sentence is a cruelty. Not a deliberate cruelty -- a cruelty that exists because I did not pause before speaking. A pause before that sentence would have resulted in a different sentence. Probably 'I know you knew her' or 'Nineteen is too young and I know you knew it was too young.' Either of those sentences would have been a functional condolence. The sentence I said was a demand: you, Tessa, try harder. It put the burden of Siri's nineteen on the doctor who lost her."

    athought "I said it and Tessa took it. She did not argue. She did not come back to me and say the sentence was wrong. She has not mentioned it since. The fact that she has not mentioned it is part of why her chair was empty at the council this morning. I did not put her in the chair because I knew what sentence she would have said -- 'I will receive the wounded' -- and I knew I would have heard it as a withdrawal and I would have had to acknowledge the withdrawal."

    athought "Excluding her from the council was easier than acknowledging the withdrawal. Easier is the tempo without the pause."

    # ========== PHASE 15 -- THE INVENTORY (ITEM 10) ==========

    athought "I am reading a letter my mother wrote before I was old enough to read."

    athought "I am the only person in this room."

    athought "I am keeping this letter against my chest because I want to remember that my mother thought a pause was possible."

    athought "My mother thinks a pause is no longer possible for me. She walked out of our house last week because she saw that it was no longer possible and she could not watch the impossibility at close range. She sent me no message afterward. The message was the walking."

    athought "I think my mother is right."

    "He is looking at the letter. He has not looked at the mirror yet."

    # ========== PHASE 16 -- THE MIRROR ==========

    "He lifts his eyes from the letter."

    "The mirror is at his left. The small steel-framed field mirror. He has not looked into it in four months. There is a fine layer of dust on the top edge of the frame. The glass is clean."

    "He turns his head. He looks at his face in the mirror."

    "He does not look away."

    "The camera cuts to the locked frontal from inside the mirror's plane. Aeron's face fills the frame. He is exactly the way he looks in the council and the way he looks in the workshop and the way he looks at the altar and the way he looks when he is alone at 0330 in his quarters with his mother's handwriting on the desk."

    "The face is the same face in every venue. That is the thing he sees."

    athought "The mask is the face."

    athought "I have been telling myself for a year that there is the public face and under it the private face. At the council the public face. In the quarters the private face. At the altar the ritual face. With Zira the adjacent face. With Nyra the co-command face."

    athought "They are all the same face."

    athought "The mask and the man converged. I do not know when they converged. Probably gradually. I notice it now because I am looking in the mirror after four months and the face I am seeing is the face I would bring to the war room at 0600."

    athought "My mother wrote that she fell out of love with a man who stopped pausing. I am the man my mother wrote about. Not Marcus. Both of us. The letter was written for Marcus and it applies to me by inheritance. The inheritance is visible in the mirror."

    athought "Marcus had a face he wore and under it the private self she had married. The pause was the seam between the two. The seam dissolved. She fell out of love with the dissolution."

    athought "I have already dissolved. The seam is gone for me and I do not remember when it was there. I am what Marcus became, at the age Marcus became it. I am arriving at Marcus on schedule."

    # Callback: a1_s26_obsidian_bridge (Zira called him "Glass");
    # a2_s08_the_analyst (Noelle's "textbook Glass")
    athought "Zira called me Glass. Noelle called the Sweep textbook Glass. I am not Glass tonight. Glass implies something brittle underneath. There is nothing brittle underneath. There is only more of the surface."

    "He is still looking at the face. The face does not react to the observation. The observation is not news to the face. The face has known."

    # ========== PHASE 17 -- THE ONE SPOKEN LINE ==========

    "He speaks for the first time in the scene. The line is low, almost inaudible. It is not a declaration. It is a confirmation spoken aloud because the thought needed to be sound for one second to be real."

    a "I am the man my mother wrote about."

    "That is the whole line. The quarters absorb it. The HVAC absorbs it. The desk lamp does not flicker. The mirror does not change."

    "He does not say it again. Saying it twice would dilute it. Once is the operational dose."

    # ========== PHASE 18 -- THE SECOND INVENTORY ==========

    athought "The letter does not exit this."

    athought "I want to be precise with myself about that because the letter is the only object in this room that has any capacity to change the trajectory of the next seven days and I need to know if it is changing the trajectory."

    athought "It is not."

    athought "The mission is authorized. The corridor is pre-staged. The model is retraining. The blessing is on the altar's calendar for day six at 2100. The return ritual is five-branch ready. The surgical suite is primed or the surgical suite is primed and the surgeon was not in the room this morning -- either way it is primed."

    athought "I am going to kill Rhea Vestin at dawn in six days."

    athought "The letter is not going to stop me. The mirror is not going to stop me. The third read is not going to stop me. Nothing in this room at 0330 is going to stop me. The operation has crossed the line at which individual recognition can reverse it. That line was crossed somewhere between the council opening and the chime of the calendar commit. I did not notice the line being crossed. The line was already behind me when the chime sounded."

    athought "So the letter is not doing what a letter would have done if I were a man a letter could still change. The letter is doing something different. The letter is functioning as proof. Proof for my own ledger that my mother thought a pause was possible. Proof that there existed, at one point in one person's mind, the conviction that the thing I have become was not inevitable."

    athought "That proof is the only mercy available in this room tonight. It is not a mercy that excuses me. It is a mercy that accurately describes what I could have been, according to a witness who knew me before I was this, who did not live to see this, and who walked out of our house a week ago because she cannot witness this up close."

    athought "The letter is not a door."

    athought "The letter is a gravestone."

    athought "I am carrying the gravestone inside my jacket. The man I could have been is buried in the pocket against my chest. When I die the letter will be recovered from my jacket and whoever finds it will think it meant something more than it meant. The meaning will be theirs to assign. For me, here, tonight, it means what I just said it means."

    # ========== PHASE 19 -- THE SECOND SPOKEN LINE ==========

    "He speaks the second line. Lower than the first. Barely audible. Aimed not at the mirror and not at the letter but at the small square of desk between them."

    a "A pause is not possible for me. Not now."

    "The line is a restatement of what he told Zira yesterday at 0500. He is saying it to himself alone because saying it to himself alone is a different operation from saying it to Zira. Zira heard it as witness. He is hearing it as owner. The words sit differently in the mouth of the owner."

    "The desk lamp holds. The mirror holds. The letter holds."

    # ========== PHASE 20 -- THE REFOLD ==========

    "He looks back at the letter. He reads the central sentence one more time -- the eye-path only, no subvocalization."

    "Then he folds the page along its existing creases. He slides the page back into the envelope. He presses the envelope flat."

    "He looks down at his own jacket. The inner chest pocket is waiting. The warmth of his body is waiting."

    "He opens the inner pocket and slides the envelope back in. Flat. Against the skin side of the pocket. The jacket closes."

    athought "Back against the chest. That is where it lives now. Until the jacket is destroyed or I am."

    # ========== PHASE 21 -- THE MIRROR, ONCE MORE ==========

    "He looks into the mirror one more time. The locked frontal holds."

    athought "The face I am going to bring to the ops table in ninety minutes is this face. I am going to sit at the head of the table -- not the side chair. The head. The head is where the man who runs the assassination sits on day one of day seven. I have been taking the side chair for three weeks because the side chair is easier to leave. On day one of day seven I am going to take the head chair and I am not going to leave it until the mission is executed or I am replaced."

    athought "The head chair is the visible structural commitment. Every person who walks into the ops room at 0600 is going to see me in the head chair and understand, without a word, that the assassination is under my hand from this morning until the rotation point."

    athought "I could still take the side chair. The side chair would be a false pause. A pretend pause. A performance of consideration I do not possess. I am not going to perform the pause I do not have."

    athought "I am going to take the head chair. That is the honest posture. My mother's letter is against my chest. My own face is in the mirror. Nobody in the base is awake yet except the night rotation."

    athought "The head chair is waiting."

    # ========== PHASE 22 -- THE STAND ==========

    "He closes his jacket button. He stands. The chair creaks back a fraction from the desk."

    "He does not look at the bed. He does not look at the standby terminal. He does not look at the mirror again. The mirror has served its function. The face has been met."

    "He walks to the quarters door. At the door he pauses -- not the pause his mother described, a different pause, the small habitual pause of a man confirming that a room can be left alone behind him. He turns off the desk lamp. The mirror goes dark with the rest of the desk."

    "He opens the door. The corridor is empty. The night rotation is two corridors over. The pressure seal cycles behind him. His quarters are sealed. He is in the corridor."

    # ========== PHASE 23 -- THE WALK ==========

    "The walk to the war room is six minutes. He walks it without notes, without a packet, without a terminal. He walks it in his jacket with the letter against his chest and the morning's target list in his head and the names of the seven dead in his head and the seven-day schedule in his head."

    "He does not pass anyone. The corridor is his."

    athought "Six minutes of corridor. Six minutes is not a pause. Six minutes is transit. Transit is not the same as a pause. A pause is a beat inside an action. Transit is the action itself."

    athought "I am on schedule."

    # ========== PHASE 24 -- THE WAR ROOM AT 0500 ==========

    "He arrives at the war room at 0500 sharp. The pressure seal cycles once. He enters."

    "The war room is exactly the way he left it the previous morning after the council. The map overlay dormant. The packet stack at the head of the table where he left it. The chair at the foot of the table empty -- or empty in a way that depends on the previous branch."

    "He walks to the head of the table. He does not go around to the side chair. He does not hesitate at the head chair. He pulls it back. The leather creaks once, low. He sits."

    "The camera cuts to a wide from the back of the room. The war room is held in the 40%% overheads. Aeron is alone at the head chair. The letter is inside the jacket. The morning's pre-shift work is at his hand."

    athought "The head chair. The honest posture. The mirror of the EMP-Aeron at the side chair. Both acts of weight are decisions about where a man with a specific kind of interior is going to put his body for the next hour."

    athought "My interior is now compatible with the head chair. The compatibility is not a victory. It is a measurement."

    athought "I am the man my mother wrote about and I am sitting at the head of the table in the war room of the base my father commanded. I am doing it without anyone watching because the people who will walk in at 0600 are not going to see this moment -- they are going to see me already seated. The head chair is the first thing they will see. The act of sitting in it is mine alone."

    athought "That is the private beat of the OB track. The moment nobody witnesses. The moment I take the chair because the chair has already been taken in every previous morning of this month and the taking is now simply the body completing the routine the mind has surrendered to."

    # ========== PHASE 25 -- THE FINAL FRAME ==========

    "He opens the packet stack. The Ghostline relay log is on top. He begins to read."

    "The camera holds on the wide shot for three full beats. The war room. The head chair. The man. The jacket. The letter no one else knows is there."

    "The night rotation outside the door cycles once, very faint, a door two corridors over opening and closing. He does not look up."

    athought "Act 4 ends here for me. Tomorrow is day one of day seven. The council reconvenes at 0600. I will still be in this chair when they arrive. I will still be in this chair at 0900 tonight when the day's operations close. I will still be in this chair for the next six mornings. On the seventh morning I will rise from the chair and go to the forward position and give the execution order."

    athought "The head chair is where I am."

    athought "Pause is not possible for me. Not now. The letter is against my chest. The mirror is off. The quarters are sealed. The war room is mine."

    athought "The building is ready. I am ready. The mission is ready."

    athought "Begin."

    "The camera holds one final beat. The head chair. The man. The packet stack. The cold white light."

    "Fade, very slow."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Aeron", trust=0, conflict=0)
    $ tp_seed("a4.ob.aeron.pause_is_not_possible_for_me")
    $ canon_set("ob.aeron.takes_head_chair", True)
    $ canon_set("ob.aeron.mirror_after_four_months", True)
    $ canon_set("ob.aeron.mask_and_man_converged", True)
    $ canon_set("ob.aeron.third_read_of_letter", True)
    $ canon_set("ob.aeron.letter_is_gravestone_not_door", True)
    $ flag("ob_aeron_said_aloud_i_am_the_man_my_mother_wrote_about", True)
    $ flag("ob_aeron_said_aloud_pause_is_not_possible_for_me_private", True)
    $ npc_remember("Aeron", "third_read_letter_alone_at_0330", tone="ownership_of_impossibility")
    $ npc_remember("Aeron", "inventory_of_ten_items_against_the_letter", tone="honest_accounting")
    $ npc_remember("Aeron", "head_chair_at_0500_alone", tone="structural_commitment_private")
    $ metric("ob_aeron_solitude_index", set_to=5)
    $ metric("ob_aeron_self_awareness_reservoir", add=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s23_aeron_alone_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - 0330 the morning after a4_s22 (council of attrition). Day one of the
#     seven-day countdown to the Rhea Vestin assassination.
#   - Aeron alone in his quarters, then at the war room head chair at 0500.
#   - This is the FINAL SCENE of Act 4 on the OB track.
# cann.what_happened:
#   - Aeron returns to his quarters at 0330 after a day in the war room.
#     He still has Liora's letter against his chest (from a4_s21).
#   - He removes the letter, unfolds it, and reads it for the third time.
#   - He runs an inventory of ten items against the letter's central sentence:
#     (1) killed Selene by not pausing on an insertion angle
#     (2) killed three civilians by signing a list he did not read twice
#     (3) watched seven operators die because he was slower than Rhea's specialist
#     (4) is going to kill Rhea in seven days
#     (5) sealed a second oath with Nyra
#     (6) took Zira after she demanded to feel like something
#     (7) let Noelle declare herself a weapon and did not stop her
#     (8) let Lyra bless strike teams and did not release her
#     (9) told Tessa to try harder to know that a girl was nineteen
#     (10) is reading a letter his mother wrote before he was old enough to read
#   - He looks in a small field mirror he has not used in four months. Sees
#     that the public face and private face are the same face. The mask and
#     the man have converged.
#   - He speaks two lines aloud, both low and nearly inaudible:
#     "I am the man my mother wrote about."
#     "A pause is not possible for me. Not now."
#   - He refolds the letter and returns it to the jacket.
#   - He walks to the war room at 0500 and takes the HEAD chair, not the
#     side chair. This is the structural mirror of the EMP-Aeron who takes
#     the side chair at the end of Act 4 on the EMP track.
#   - He opens the packet stack and begins reading. Act 4 ends on the wide
#     shot of the war room with one man at the head chair.
# cann.aeron_state:
#   - Soliloquy scene. Entire arc is internal except for two whispered lines.
#   - Ownership rather than recognition: he names the impossibility of the
#     pause as his own, not as an external diagnosis.
#   - The mirror scene is the scene's quiet horror: the private face and the
#     public face are the same. No seam remains. He has arrived at Marcus.
#   - He explicitly declines the side chair. The head chair is the honest
#     posture. He is not performing the pause he does not have.
#   - solitude_index set to 5 (max for Act 4 OB).
# cann.path_tracking:
#   - tp_seed a4.ob.aeron.pause_is_not_possible_for_me
#   - canon_set ob.aeron.takes_head_chair True
#   - canon_set ob.aeron.mirror_after_four_months True
#   - canon_set ob.aeron.mask_and_man_converged True
#   - canon_set ob.aeron.letter_is_gravestone_not_door True
#   - metric ob_aeron_solitude_index set_to 5
# cann.thematic_flags:
#   - "I am the man my mother wrote about" as the private confirmation.
#   - The ten-item inventory as Aeron's OB self-audit.
#   - The mirror as the moment the mask stops being a mask.
#   - The head chair vs. the side chair as structural mirror of EMP a4 ending.
#   - The letter finalized as gravestone: proof of the self that was once
#     possible, carried inside the jacket through the seven-day countdown.
# cann.character_moments:
#   - Aeron's first look in a mirror in four months.
#   - The two spoken lines, each one sentence, each at whisper volume.
#   - Taking the head chair alone at 0500 with nobody watching.
#   - Reading the Ghostline relay log while sitting in the head chair with the
#     letter against his chest.
# cann.callbacks:
#   - a4_s21_the_letter_ob (the delivery; letter first against his chest)
#   - a4_s22_council_of_attrition_ob (the assassination authorization)
#   - a4_s20 (Noelle weapon-track)
#   - a4_s18 (seven named dead)
#   - a4_s13 (Zira workshop, "make me feel it")
#   - a4_s11 (Nyra sealed oath)
#   - a4_s09 (Sector 12 list signature)
#   - a3_s21 (OB Aeron learns Liora is alive)
#   - a3_s24 (Liora walks out)
#   - Early a4 EMP scenes where Aeron takes the side chair -- explicit
#     structural inversion.
# cann.block_status:
#   - ANCHOR (OB). Solo soliloquy. No player choice. No branching.
#   - FINAL SCENE OF ACT 4 ON OB TRACK.
# cann.requires_followup:
#   - Act 5 opens on day two of day seven with Aeron already in the head chair.
#   - The letter remains against his chest throughout Act 5.
#   - The mirror at the desk is now a tracked object. Future OB scenes may
#     reference whether he looks into it again and when.
