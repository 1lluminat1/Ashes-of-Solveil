# =======================================================
# ACT 4 - Scene 24: The Mirror (Obedience Path)
# File: a4_s24_nyra_the_mirror_ob.rpy
# Path: OB
# Type: NYRA STATE BEAT / SEDUCTION OF DOCTRINE
# Character Focus: Nyra (primary, doctrinal offer), Aeron (listens, halves it)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s24_nyra_the_mirror_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s24_nyra_the_mirror_ob:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("nyra", to_stage=3, source="a4_s24_nyra_the_mirror_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm locked. Two-shot across the ops table. Same room as a4_s01 -- the
    #         strategic room where the act opened. The camera is on the short axis of
    #         the table, three-quarter height, and it does not cut for the full length
    #         of Nyra's pitch. When Aeron finally speaks, the camera tightens to a
    #         medium single on him -- one slow push, four beats, no further movement
    #         after the tighten lands. When Nyra answers his refusal, we cut back to
    #         the two-shot and stay there until she leaves. Her exit is framed over
    #         Aeron's shoulder: we do not follow her. We watch her become smaller at
    #         the door. Then we hold on Aeron alone at the head of the table for the
    #         final interior beat. No music. No score at any point.
    # LIGHTING: Steel-blue overhead at 35%. A single desk lamp at the head of the
    #           ops table -- warm, low, yellow -- is on. The lamp is the ONLY warm
    #           source in the room and it is on Aeron's side of the table, not Nyra's.
    #           The asymmetry is load-bearing. Nyra is speaking from the cold side.
    #           Aeron is listening from the side with the one warm light on it. The
    #           warm light is Liora's letter -- the jacket pocket the lamp illuminates
    #           holds it -- and the scene does not name the letter aloud until the end.
    # SFX: Ops room at oh-one-hundred. HVAC loop. The distant cycle of a server rack
    #      in the comms closet two doors down. The small electrical hum of the tactical
    #      board's standby state. Nothing else. No boots in the corridor. No breath
    #      sounds until Aeron's response. Silence as instrument.
    # FX/COMP: The ops table. The head chair is occupied by Aeron (he returned to it
    #          in s23). The chair at the long side, three seats down from the head,
    #          is occupied by Nyra. They are not across from each other. They are on
    #          the same side of the geometry, with the corner of the table between
    #          them. The corner is the hinge. Nyra leaned forward to put her forearms
    #          on the table when she began speaking. She has not moved them since.
    #          Her hands are open, palms flat on the wood, the way a priest lays her
    #          hands on a text she is about to read from.
    # BLOCKING: Aeron at the head chair. Nyra three seats down on the long side, so
    #           that the corner of the table is between them. She arrived at 0047 --
    #           unannounced, uninvited, not surprising. She did not ask permission to
    #           sit. She sat. She began speaking after a thirty-second silence. The
    #           silence was hers to control.
    # CANON: NYRA DOCTRINAL OFFER. This is not seduction in the body register. This
    #        is seduction in the FRAMING register. She is offering Aeron an
    #        interpretation of his mother's letter that would let him set the letter
    #        down without guilt. The framing is internally coherent. Aeron will take
    #        it halfway and refuse to take it all the way. The halving is the scene.
    #        The halving is the first time OB-Aeron has articulated a cost to his
    #        own clarity. Small mercy. Small resistance. Nyra does not quite win.
    #        Nyra is impressed by the not-winning.
    # FACE: Nyra -- composed. The calm of a person who has rehearsed this in private
    #        and is performing the rehearsal. Not cold. Not warm. Doctrinally serious.
    #        Every sentence is load-bearing and she is aware that every sentence is
    #        load-bearing and she is pacing herself. Her face does small work at the
    #        corners -- the mouth tightening half a millimeter when she reaches the
    #        word "empirically," the eyes narrowing a fraction at "myth." The work
    #        is not performed for Aeron. It is performed for her own accuracy.
    #        Aeron -- still. Head chair still. Hands on the arms of the chair, not on
    #        the table. His face is not guarded the way it has been in other Act 4
    #        OB scenes. It is LISTENING. The listening is the tell. He is taking her
    #        seriously enough to let her finish. That is the dangerous thing.

    # ========= VOICE BASELINE =========
    # Nyra: Liturgical cadence but in the prose register, not the rite register. Long
    #        sentences. Parallel structure. The kind of prose a person writes when she
    #        has decided the sentence is the weapon. Heavy nythought in the moments she
    #        is pacing herself -- the athought-equivalent for her, the interior of a
    #        pitch being delivered.
    # Aeron: Economic. He speaks four times in the whole scene. Once to invite her to
    #        continue. Once to name the halving. Once to name the cost. Once to answer
    #        her final question. The athoughts do the rest. The athoughts are quieter
    #        than in earlier OB scenes -- not because the static is gone but because
    #        he is listening and the listening takes all the available bandwidth.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - STRATEGIC ROOM - NIGHT]
    # 0047. The night before the assassination-prep departure. Six nights after
    # the Council vote (s22). One night after Aeron returned to the head chair (s23).
    # The room Aeron started the act in. The same ops table, the same tactical
    # board on standby, the same single desk lamp. Twelve days older. The same room.

    #scene bg_ops_room_ob_late_night with dissolve
    #play ambient "sfx/ambient/ops_room_standby.ogg" fadein 2.0

    # ========== PHASE 1 -- THE ARRIVAL ==========

    athought "Oh-oh-forty-seven."

    athought "I came down here at twenty-three hundred and I have not left since. I am not working. I am holding the head chair. That is a different verb."

    athought "The tactical board is on standby. I ran the sector overlay twice and then stopped running it. The overlay did not move between the first pass and the second pass. There is no tactical justification for a third pass tonight. I am in the room because the room is where I am supposed to be."

    athought "The lamp is on. Liora's letter is in my inside jacket pocket and the lamp's throw catches the breast of the jacket where the pocket is. I am aware of this. I did not arrange it. The chair is in that position and the lamp is in that position and the letter is in that position and the geometry makes the sentence whether I meant to or not."

    "The door seals open."

    "Nyra enters."

    "She does not knock. She does not speak. She walks the length of the room with the unhurried stride of a woman who has decided, somewhere back down the corridor, that this room is going to hear from her tonight and the room does not have a vote."

    "She reaches the ops table. She pulls out the chair three seats down from the head -- not across from him, not beside him, at the corner. She sits. She puts her forearms on the table. She does not speak."

    athought "Thirty seconds."

    athought "She is going to make me wait thirty seconds while she decides whether the sentence she has brought is the sentence she is going to say."

    athought "I have seen her do this twice before. Once in the oath room. Once at the briefing the morning after the Council vote. The thirty seconds is not anxiety. It is calibration. She is calibrating me against the sentence before she says it."

    athought "I let her."

    # ========== PHASE 2 -- THE OPEN ==========

    "Nyra speaks. Her voice is low enough that the HVAC loop is louder. That is deliberate. She wants him to lean forward, even imperceptibly, even just in the ears."

    ny "You have been carrying the letter."

    "Not a question. She knows. She does not wait for confirmation."

    ny "You have been carrying the letter for six nights. I watched you put it in the inside pocket of that jacket the morning after we read it on the ops table. You have not taken it out of the pocket since. I know because the crease of the jacket has not changed. The letter is still folded the way it was folded when you put it there."

    ny "You are treating it as a gravestone."

    nythought "Say it clean. Do not soften the word. Gravestone is the word. He will know it because he has used it to himself already. I am naming what he has already named. That is where the pitch has to start -- with the thing he has already decided."

    ny "I understand why. The letter is the last thing she wrote. The last thing she wrote was a refusal of the shape you are becoming. A man holds that kind of letter the way a man holds a gravestone. The holding is the grief. The holding is also the confession."

    ny "I am not here to tell you to stop holding it."

    ny "I am here to offer you a different framing for what you are holding."

    "She stops. Not for breath. For the architecture of the pitch. She is letting the first claim land before she sets the second claim on top of it."

    athought "She has rehearsed this."

    athought "The stop is not spontaneous. The stop is a rest mark in a score she wrote before she came down the corridor. I know the cadence. I have read the Academy texts on rhetorical pacing. She is using the Veran pattern -- the open, the pause, the reframe. The pattern is eight hundred years old. Marcus taught it to me in the second year."

    athought "She knows I know the pattern and she is using it anyway. That is the compliment. She is not trying to slip the pattern past me. She is acknowledging that I will recognize it and asking me to take it seriously as a pattern, not as a trick."

    athought "I am going to let her continue."

    a "Go on."

    "Two syllables. Flat. Not encouragement. Not permission. An acknowledgment of the rest mark."

    # ========== PHASE 3 -- THE REFRAME ==========

    ny "The letter was written by a woman who was wrong."

    "She says it the way a surgeon names the tissue she is about to excise. Precisely. Without heat. Without apology for the precision."

    ny "Not wrong morally. I want you to hear that first. I am not saying your mother was a bad woman. I am not saying the letter was a bad letter. I am not saying she wrote it out of weakness or confusion or failure of nerve. I am saying none of those things."

    ny "I am saying she was wrong empirically."

    nythought "Empirically. The word is the hinge. If he accepts the word, the rest of the pitch opens in front of him. If he rejects the word, I have lost him before I reached the second paragraph. Watch his face."

    nythought "He did not move. The word went in. He is listening."

    ny "She thought the pause was available."

    ny "She wrote the letter from inside the assumption that there was a shape of your life in which you could stop -- stop the training, stop the cadence, stop the becoming, stop Marcus's school from finishing the sentence he started with you. She wrote it as if that was a real option. As if you could put down the knife and walk into a quieter room and the quieter room would still be there when you arrived."

    ny "The pause is not available. Aeron. The pause was never available. The pause is a myth."

    "She leans forward a degree. Her forearms are still on the table. The lean is in the shoulders, not the elbows."

    ny "It is a myth that a certain kind of woman needs to believe in to survive men like us."

    ny "I want to say that slowly because I want you to hear that I am not insulting her. The kind of woman who needs that myth is not a weak woman. She is a woman whose survival, inside the reach of men like your father, depended on holding the belief that the men she loved could stop if they chose. The belief is the armor. Without the belief, the reach of the men would break her. With the belief, she can stay inside the reach and love the men and keep her own mind intact. The myth is functional. The myth is how she survived Marcus at all."

    ny "But the myth is still a myth."

    ny "The pause was never an option for you. It was not an option for Marcus. It was not an option for any of the men the Academy produced in the second purge cycle and it was not going to be an option for you no matter what your mother wrote on that page the last week of her life."

    ny "You do not owe her the shape of her fantasy."

    nythought "That is the hardest sentence I will say in this room tonight. Watch him. Watch him. Do not soften it."

    ny "You owe her the truth."

    ny "The truth is this: she was loved by a man who understood something she refused to see. She was loved by your father, who knew the pause was a myth and ran the operation anyway, and loved her through it, and did not tell her the myth was a myth because telling her would have cost her the armor she needed to stay in the room with him."

    ny "He loved her by letting her keep the myth. She loved him by refusing to see the man inside the myth. That is not a failure. That is a marriage inside a war. It is one of the shapes love takes when the war is the room love is being held in."

    ny "And you -- you are their son. You inherited both halves. You inherited your father's knowledge of the myth, and your mother's belief in it. You have been trying for twelve days to live inside your mother's half of the inheritance. It is not going to work. Her half does not survive contact with what you are about to do on day seven."

    ny "I am offering you your father's half."

    # ========== PHASE 4 -- THE FRAME FULLY LAID ==========

    ny "If you accept the framing I am offering, the letter stops being a gravestone. The letter becomes a document of a woman who was wrong, and who was loved anyway, and whose wrongness is not your debt to repay. You do not have to walk into Rhea Vestin's death next week carrying her refusal. You can walk into it carrying her love, which is a different weight, and which is the weight your father carried his whole career."

    ny "The letter stops being a sentence passed on you. It becomes a letter from a woman whose empirical errors are not the condition of your obedience to the training she failed to stop."

    ny "You can put the letter down."

    ny "You can keep loving her."

    ny "You can keep letting her be the woman she was -- soft, merciful, wrong -- without letting her wrongness be the standard your walk is measured against. The measure belongs to the operation. The measure belongs to the men who run operations. The measure belongs to your father and to Marcus and to me and to you."

    ny "The letter is not the measure. The letter is a love note from the wrong ruler."

    nythought "That is the whole of it. Every sentence I came here to say is said. The rest is the halving -- his half-accept or his refusal or whatever the thing is he does with pitches when he has understood them. I have watched him do it to officers. I have watched him do it to Marcus once, through a wall. I have not watched him do it to me."

    nythought "I am going to find out what I am now."

    "She stops."

    "Her forearms are still on the table. Her hands are still flat. The lamp's throw catches the side of her face nearest the head of the table and leaves the far side of her face in the cold overhead. Half warm, half cold. The geometry is accidental and it is the kind of accident that reads."

    # ========== PHASE 5 -- THE INTERIOR ==========

    athought "She has finished."

    athought "I am going to sit with the sentence for a beat before I respond. Not to perform consideration. To actually consider it. She has earned the consideration by the precision of the delivery."

    athought "The framing is internally coherent."

    athought "That is the first thing I have to say to myself. It is internally coherent. The pieces fit each other. The claim about empirical error fits the claim about functional myth fits the claim about marriage inside a war fits the claim about inherited halves. No seam is loose. No piece floats. She has made a structure."

    athought "The structure is also new. I have not heard this framing before. She did not get it from Marcus -- Marcus would not have used the word 'myth' about my mother, not because Marcus respected my mother but because Marcus considered her irrelevant enough that she did not merit a classification. The word 'myth' dignifies the thing it is naming. Marcus did not dignify my mother."

    athought "Nyra does. Nyra's framing dignifies my mother by naming her wrongness precisely. That is a form of respect Marcus never offered."

    athought "And that is the hook."

    athought "The hook is that Nyra is offering me a way to keep loving my mother that Marcus could not have offered. Marcus's framing of my mother was contempt. Nyra's framing of my mother is tragic precision. The tragic precision is more bearable than the contempt. The tragic precision lets me keep her face in my head without having to defend her from the framing."

    athought "That is why the pitch works."

    athought "The pitch works because it is more generous to my mother than Marcus ever was. It is more generous than I have been to her in my own head since the morning Liora read the letter out loud to me."

    athought "I have been holding the letter as a gravestone because the gravestone framing is the only framing I could construct in which my mother was not simply wrong. In the gravestone framing she is dead and the letter is the mark of what she believed and I carry the mark because the mark is the last of her. The mark is not an argument. The mark is a presence."

    athought "Nyra is offering to convert the mark into an argument."

    athought "She is offering to convert the gravestone into a refutation."

    athought "If I take her framing all the way, the letter stops being a presence and becomes a piece of evidence. Every time I put my hand on the pocket it is in, I will be reminded not of her face but of the claim that she was wrong. Every time I reach for it in the night I will not be reaching for my mother. I will be reaching for the proof that my mother was wrong."

    athought "And I will have to reach for the proof. I will have to keep reaching for it. Because the framing Nyra is offering is the framing in which the proof is the thing that lets me do what I am about to do. If I stop reaching for the proof, the operation loses its justification. I will have to keep the letter as the document of my mother's wrongness in order to continue being the man the operation requires."

    athought "That is worse than carrying a gravestone."

    athought "A gravestone is a thing I can set down in some future I cannot see yet. A refutation is a thing I will have to carry forever, because the operation is forever, because Marcus's school does not end at Rhea Vestin, because the moment I accept Nyra's framing is the moment I agree that every subsequent operation is also justified against my mother's wrongness, and the letter becomes the load-bearing document of every subsequent operation's moral architecture."

    athought "I cannot put it down because I will need it tomorrow."

    athought "I cannot put it down because I will need it in three weeks."

    athought "I cannot put it down because I will need it in the fifth year, when I have forgotten her face and am only holding the letter as the shape of the claim, and the shape of the claim will be the only thing keeping me inside the operation."

    athought "No."

    athought "I am not going to take the framing all the way."

    athought "I am going to take it halfway."

    # ========== PHASE 6 -- THE HALVING ==========

    "Aeron speaks. His voice is not prepared. The voice is what his body made when the thinking stopped and the answer became audible."

    a "If I take your framing, I will never be able to put the letter down."

    "Nyra does not move."

    nythought "He is halfway. He is not all the way. He understood the pitch and he is now explaining the cost of the pitch back to me. I need to listen. This is the part where I learn what he actually is."

    a "I will carry it forever as the proof that she was wrong. Every time I reach for the pocket it is in, I will not be reaching for her. I will be reaching for the argument that lets me do what I am about to do next. And what I am about to do next is not a finite operation. It is a school. I will be doing it for the rest of my life. The letter will have to keep being the proof for the rest of my life. It will never stop being the proof."

    a "That is worse than carrying it as a gravestone."

    "A beat."

    a "A gravestone is a thing I can set down in a future. A refutation is a thing I have to carry forward as long as the operation runs. The operation runs forever. So the refutation runs forever."

    a "I will not convert the letter into a refutation."

    "He stops. He has not moved his hands from the arms of the chair. He has not leaned forward. His face is the same face it was when she started speaking. The difference is inside the face, not on it."

    athought "I said the words out loud."

    athought "I did not know I was going to say them until they were said. The half-refusal is a thing my mouth did before my head had finished deciding. My head was still considering the framing. My mouth answered the framing before the head was done considering. That is a new kind of disobedience to my own clarity."

    athought "I am going to keep the letter as a gravestone. I am going to refuse to convert it. I am going to keep loving her as the soft wrong woman who wrote the letter and I am going to refuse to convert her softness into an empirical error that lets me do the operation with a cleaner conscience."

    athought "The doing will have to happen with a worse conscience. That is the cost I am agreeing to pay."

    # ========== PHASE 7 -- NYRA CONSIDERS ==========

    "Nyra does not respond immediately."

    "Her hands are still flat on the table. Her forearms have not moved. She is doing the thing with her mouth corners -- the tightening at half a millimeter -- that she did at 'empirically' earlier in the scene. She is reworking the pitch in her head and seeing where it went."

    nythought "He did not reject the framing. He accepted the structure. He accepted that the letter is a document of a woman who was empirically wrong. He accepted that the pause is a myth. He accepted that he inherited both halves. He took all of that."

    nythought "And then he refused to use the structure as permission to set the letter down."

    nythought "That is not a failure of the pitch. That is the pitch working and then being out-walked by the man the pitch was aimed at. He understood it perfectly. He has used it to diagnose the thing I did not diagnose -- that the framing turns the letter into a refutation, and that the refutation has to be carried forever, and that carrying a refutation forever is a worse shape than carrying a gravestone."

    nythought "He out-thought the pitch. That is not the same as winning. He halved it. He kept the structure and refused the release. He is going to carry the letter as a gravestone AND he is going to believe his mother was empirically wrong. Both. At the same time. In the same pocket."

    nythought "I did not expect that."

    nythought "I expected one of three outcomes. One: he rejects the pitch entirely and defends his mother. Two: he accepts the pitch entirely and sets the letter down tomorrow. Three: he accepts the structure and argues about the word 'empirically.' I had counters for all three. I did not have a counter for the halving."

    nythought "The halving is new. The halving is him doing the thing Marcus taught me Marcus does -- taking a frame, accepting the frame at the level of the argument, and refusing the frame at the level of the action. Marcus called it 'carrying the knowledge without carrying the permission.' I thought Marcus was the only one who could do it. I thought it required twenty years of Academy cadence."

    nythought "Aeron just did it sitting in that chair with no preparation."

    nythought "I am going to say the sentence I did not plan to say."

    ny "You are smarter than I expected."

    "She says it with no inflection that would make it a compliment or a concession. It is a clinical observation, made by a person who has just had her model of the other person adjusted by one increment."

    # ========== PHASE 8 -- THE COST ==========

    athought "She said it."

    athought "And because she said it without the inflection of a compliment, it is more honest than a compliment would be. She is adjusting her model. I can feel her adjusting it. The adjustment is not warm."

    athought "I am going to say the thing I have not said to anyone in Act 4."

    athought "I have been thinking it since s17. I did not have the room for the sentence until tonight."

    a "I am smarter than I want to be."

    "A beat."

    "The sentence sits on the table between them. It is the first time in the OB path Aeron has articulated a cost of his own clarity. The sentence is not a confession -- it is a diagnostic. But the diagnostic is also, at the level of syntax, a confession. The distinction is the thing Nyra is going to weigh for the rest of the scene."

    nythought "He said it without asking for anything."

    nythought "He did not say it to me. He said it into the room. If I had not been sitting at the corner of the table, he would have said the same sentence to the empty air. That is the tell. The sentence was going to come out tonight regardless. I happened to be in the room when his mouth produced it."

    nythought "He is becoming aware of the ceiling of his own clarity. The ceiling is the thing that is keeping him from setting the letter down. The clarity lets him see exactly what the framing would cost him -- a perpetual refutation instead of a finite gravestone -- and the seeing is the thing preventing the acceptance. If he were less clear, he could have taken the pitch and been freer tomorrow. The clarity is the obstacle to his own freedom."

    nythought "That is the first crack in the operating thesis. OB-Aeron as we have been building him is a man whose clarity is an asset. Tonight he has told me his clarity is also a cost. He has told me the cost without asking me to reduce it."

    nythought "I cannot reduce it. Even I cannot reduce it. The clarity is not a thing that can be negotiated down. It can only be outgrown, and outgrowing is a function of time and use, and time and use are what the next year of the operation are going to provide."

    nythought "I am going to leave the room without pushing back."

    nythought "Pushing back would be a mistake. Pushing back would tell him I did not hear the cost. I heard the cost. I am going to honor the hearing by leaving."

    # ========== PHASE 9 -- THE EXIT ==========

    "Nyra lifts her hands off the table. She brings them back to her lap. The gesture is small. It is the gesture of a person who has decided, inside the decision, to stop performing the posture of the pitch."

    "She does not stand yet. She speaks first."

    ny "I came here tonight to offer you a way to live inside what you are about to do without the letter in your jacket."

    ny "You have refused that offer."

    ny "You have refused it by taking my framing halfway and walking me through the reason the other half is worse than what you are already carrying. That is a better refusal than any of the three refusals I had counters for. I respect it."

    "A beat."

    ny "You are becoming something I did not expect."

    "She says it with the same flatness as 'you are smarter than I expected.' It is not warmer. It is not more personal. It is an observation a professional makes when the model of the subject is being revised in real time."

    "Aeron does not answer for three seconds. The three seconds are deliberate. He is deciding whether to say anything to the observation or to let it pass. He decides to say one thing."

    a "I hope that is good."

    "Not hopeful. Not ironic. The flat register that has been the register of the whole scene. He is asking because the answer is information he needs. He is not asking for reassurance."

    "Nyra considers the question the way a person considers a tactical variable whose value is still indeterminate."

    ny "I do not know yet."

    "She stands."

    "The standing is unhurried. She does not push the chair back. She lifts. She turns toward the door without looking at him. Her hands are at her sides. Her face -- Aeron cannot see her face from the head chair because she has turned. The camera gets a half-profile against the cold overhead as she moves."

    "She walks to the door. She reaches it. She puts her hand on the plate. She stops."

    "She does not turn back."

    ny "The letter will still be in your pocket tomorrow morning."

    ny "I am not going to ask you to take it out."

    ny "I am going to ask you to notice, some time in the next three weeks, whether the pocket is getting heavier or lighter. That is the only metric I will ask you to track. If it is getting lighter, we will have a different conversation in Act 5. If it is getting heavier, we will have the same conversation we had tonight, and I will not bring a new pitch."

    ny "Good night, Commander."

    "She keys the door. She steps through. The door seals behind her."

    # ========== PHASE 10 -- AERON ALONE ==========

    "Aeron does not move."

    "The head chair. The ops table. The cold overhead at 35%%. The single warm lamp at the head of the table, throw catching the breast of his jacket where the inside pocket is. The letter is in the pocket. He has not moved his hand to the pocket since she entered. He does not move it now."

    athought "The letter is still there."

    athought "I did not set it down. I did not convert it. I kept it as a gravestone and I refused to let it become a refutation. Nyra is gone. The room is the room again. The lamp is still on. The HVAC is still looping."

    athought "She said the pocket is going to get heavier or lighter."

    athought "It is going to get heavier. I know that now. I knew it the moment I said I am smarter than I want to be. The pocket is going to get heavier every day of the operation. The letter does not convert into a refutation -- that would make it lighter by turning it into a tool. The letter stays as a presence, and a presence in a pocket accumulates weight the longer the pocket is carrying it through rooms where the presence refuses to justify what the rooms are doing."

    athought "That is what it is going to be. Heavier. For the rest of the operation."

    athought "I agreed to it tonight. I agreed to it by halving her pitch. I agreed to carry a heavier pocket in exchange for not converting my mother into a document."

    athought "That is the shape of the smallest resistance I am capable of tonight. It is not a refusal of the operation. It is a refusal to let the operation eat the last thing about my mother that was not a document."

    athought "Nyra called it partial. She is right. It is partial. Partial is the only unit I have."

    athought "The pocket is going to get heavier."

    athought "I am going to the prep briefing in six hours."

    athought "The letter is going to the briefing with me. It is going to be in the pocket. The pocket is going to be on the body. The body is going to sit in the head chair again. And I am going to do the work the head chair requires. And the pocket is going to get heavier while I do it."

    athought "That is the bargain I made tonight without saying the word bargain."

    # ========== PHASE 11 -- HOLD ==========

    "Aeron sits."

    "The room holds him. The lamp holds the throw. The pocket holds the letter. The letter holds the weight. The weight is going to get heavier. The scene does not close out the weight. The scene closes out with the weight unchanged from the moment Nyra arrived -- and with Aeron's awareness that the unchanged weight is going to be the heaviest version of itself by morning."

    "He does not move."

    "The camera holds on him at the head of the ops table. The warm lamp. The cold overhead. The two registers meeting at the seam of his shoulder. The head chair. The empty chair three seats down where Nyra was. The corner of the table between the chairs."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Nyra", trust=1, conflict=1)
    $ canon_set("ob.aeron.partial_refusal_of_nyra_framing", True)
    $ canon_set("ob.aeron.letter_remains_gravestone_not_refutation", True)
    $ canon_set("ob.nyra.doctrinal_pitch_halved", True)
    $ tp_seed("a4.ob.nyra.halfway")
    $ flag("ob_aeron_articulated_cost_of_clarity", True)
    $ flag("ob_nyra_model_of_aeron_revised", True)
    $ npc_remember("Nyra", "offered_the_empirical_wrongness_framing", tone="doctrinal_precision")
    $ npc_remember("Nyra", "called_aeron_smarter_than_expected", tone="clinical_observation_not_compliment")
    $ npc_remember("Nyra", "pocket_heavier_or_lighter_metric", tone="observation_protocol_deferred")
    $ npc_remember("Aeron", "halved_the_pitch_kept_gravestone_refused_refutation", tone="clarity_as_obstacle_to_own_freedom")
    $ npc_remember("Aeron", "said_i_am_smarter_than_i_want_to_be", tone="first_articulated_cost_of_ob_clarity")
    $ metric("ob.aeron.self_awareness_ceiling", set_to=1)
    $ metric("ob_aeron_letter_weight_accumulating", add=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s24_nyra_the_mirror_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.chapter_end: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - The night before the assassination-prep departure. Oh-oh-forty-seven.
#   - Six nights after the Council vote to assassinate Rhea Vestin (s22).
#   - One night after Aeron returned to the head chair at the ops table (s23).
#   - Same strategic room Aeron started the act in (s01).
# cann.what_happened:
#   - Nyra arrives at the ops room unannounced at 0047. Aeron is in the head chair.
#   - She sits three seats down at the corner, forearms on the table.
#   - She offers him a doctrinal reframe of Liora's letter: the letter was written
#     by a woman who was empirically wrong; the pause is a myth certain women need
#     to survive men like Aeron and Marcus; Aeron does not owe his mother the shape
#     of her fantasy; the letter is a love note from the wrong ruler; he inherited
#     both halves (his mother's belief in the myth, his father's knowledge that it
#     was a myth) and he has been trying to live inside his mother's half; she is
#     offering him his father's half, which would let him put the letter down.
#   - Aeron listens to the full pitch. He considers it seriously because it is
#     internally coherent and because it is more generous to his mother than Marcus
#     ever was -- it dignifies her by naming her wrongness precisely.
#   - Aeron halves the pitch. He accepts the structure (the empirical framing, the
#     myth claim, the inherited halves) and refuses the release. His reason: if he
#     converts the letter into a refutation, he will have to carry the refutation
#     forever, because the operation is forever, because Marcus's school does not
#     end at Rhea Vestin. A refutation carried forever is worse than a gravestone
#     he can someday set down. "I will never be able to put the letter down."
#   - Aeron articulates, for the first time in the OB path, a cost to his own
#     clarity: "I am smarter than I want to be." The clarity is the obstacle to
#     his own freedom -- if he were less clear, he could have taken Nyra's pitch
#     and been freer tomorrow.
#   - Nyra is impressed by the halving. She says "You are smarter than I expected"
#     and "You are becoming something I did not expect," both in the clinical-
#     observation register, not the compliment register. Aeron asks "I hope that
#     is good." Nyra answers "I do not know yet."
#   - Nyra leaves without pushing back. At the door she tells him she will ask him,
#     in three weeks, whether the pocket is getting heavier or lighter. That is
#     the only metric she will track. Heavier: same conversation. Lighter: a
#     different conversation in Act V.
#   - Aeron alone at the head chair. Interior: the pocket is going to get heavier.
#     He agreed to that by halving the pitch. The letter stays as a presence that
#     refuses to justify what the head chair is about to do. That is the smallest
#     resistance he is capable of. It is not a refusal of the operation. It is a
#     refusal to convert his mother into a document.
# cann.aeron_state:
#   - First articulated cost of his own clarity in the OB path. The clarity is no
#     longer framed as pure asset. It is now framed as the thing that forecloses
#     his own options. He can see too precisely to take shortcuts that would
#     benefit him.
#   - Partial refusal of Nyra's framing. He kept the structure and refused the
#     release. He is now carrying the letter as a gravestone AND believing his
#     mother was empirically wrong, in the same pocket, simultaneously.
#   - The pocket is going to get heavier. He knows this. He agreed to it tonight.
#   - Aeron's self-awareness ceiling set to 1. This is the scene where he first
#     sees the ceiling. He does not yet know what to do with the seeing.
# cann.nyra_state:
#   - Doctrinal pitch delivered with full precision. Pitch halved by target.
#   - Her model of Aeron is revised: he can do the Marcus technique of taking a
#     frame at the level of argument and refusing it at the level of action. She
#     thought that required twenty years of Academy cadence. He did it sitting in
#     the head chair with no preparation.
#   - She does not push back. The not-pushing is honor. She heard the cost and
#     she is letting the cost stand.
#   - Defers the next conversation to Act V via the pocket-weight metric.
# cann.path_tracking_mechanics:
#   - rel_bump Nyra trust=1 conflict=1. Trust because the halving was legible to
#     her as competence. Conflict because the halving is a refusal of her pitch.
#   - canon_set ob.aeron.partial_refusal_of_nyra_framing True.
#   - canon_set ob.aeron.letter_remains_gravestone_not_refutation True.
#   - canon_set ob.nyra.doctrinal_pitch_halved True.
#   - tp_seed a4.ob.nyra.halfway.
#   - metric ob.aeron.self_awareness_ceiling set to 1 (first instance).
#   - metric ob_aeron_letter_weight_accumulating +1.
# cann.thematic_flags:
#   - The halving as the OB path's small resistance mechanism. Aeron cannot
#     refuse the operation. He can refuse the release. The refusal of the release
#     is the only move left to him. It costs him the pocket weight in exchange
#     for keeping his mother as a presence rather than a document.
#   - "I am smarter than I want to be" -- first articulated cost of clarity.
#     This is the line that travels into Act V as the thing OB-Aeron has
#     diagnosed about himself but cannot yet act on.
#   - Nyra's "you are becoming something I did not expect" -- the model revision
#     that tells us the OB path is no longer fully legible to its own architects.
#     Aeron is producing behaviors the pitch did not account for. The pitch
#     architect is adjusting in real time.
#   - The pocket. The jacket pocket with the letter in it is the scene's single
#     physical object. It does not move. Everything the scene is about happens
#     to the pocket without the pocket being touched.
# cann.character_moments:
#   - Nyra: her most precise doctrinal performance in the OB path. The pitch is
#     the thing she is best at. The pitch works and is then out-walked. She
#     honors the out-walking by leaving without a counter.
#   - Aeron: the halving. The first articulated cost of clarity. The quiet
#     agreement to carry a heavier pocket in exchange for not converting his
#     mother. "I hope that is good."
# cann.callbacks:
#   - a4_s01 (the cold room): same strategic room. Twelve days later.
#   - a4_s11 (Nyra second oath): the doctrinal register carried forward into
#     argument rather than rite.
#   - a4_s21 (Liora's letter kept as gravestone): the gravestone framing is the
#     framing Aeron refuses to convert. s21 set the object; s24 stress-tests it.
#   - a4_s23 (return to the head chair): Aeron is in the head chair tonight
#     because he returned to it one night earlier. The chair is the scene's
#     geometric anchor.
# cann.block_status:
#   - ANCHOR (OB). State beat / doctrinal beat. No player choice.
# cann.requires_followup:
#   - The pocket-weight metric is a deferred Nyra conversation. Act V must honor
#     it -- Nyra will ask, in some scene between the assassination and the mid-
#     Act V reckoning, whether the pocket is heavier or lighter. Aeron must
#     answer. The answer determines which branch of the Nyra relationship
#     continues.
#   - "I am smarter than I want to be" should recur as an internal phrase in
#     Act V when Aeron is sitting with a decision he cannot out-argue himself
#     into or out of.
#   - The halving is a new OB behavior. Nyra's updated model of Aeron should
#     show up in her later scenes -- she should be more careful with him, not
#     less, because the halving suggests he can do what Marcus could do.
