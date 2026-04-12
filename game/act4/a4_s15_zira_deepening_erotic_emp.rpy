# =======================================================
# ACT 4 - Scene 15: Zira Deepening (Empathy Path)
# File: a4_s15_zira_deepening_erotic_emp.rpy
# Type: ZIRA EROTIC DEEPENING — consent-gated, three-variant
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s15_zira_deepening_erotic_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s15_zira_deepening_erotic_emp:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s15_zira_deepening_erotic_emp")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Five movements.
    #         (1) The doorway. 35mm, locked, from inside the workshop looking
    #             at the door. The door opens. Aeron is in the frame as a
    #             silhouette against the corridor spill. He does not step in.
    #             The camera does not find Zira yet. The camera finds her
    #             voice before it finds her face — a rule this workshop has
    #             enforced in every scene since s08 and enforces here.
    #         (2) The bench. 35mm, slow pivot — the camera moves off the
    #             doorway and finds Zira at the bench with a small object
    #             under the clip lamp. She is not forging a plan tonight. She
    #             is working on something Aeron has never seen her work on
    #             before. Her hands are in frame before her face, as always.
    #             The object between her hands is a clock mechanism — brass,
    #             the size of a palm, half-assembled, the gears visible.
    #         (3) The turn. She sets the tool down. She turns. She does not
    #             stand. The turn is small. Her face comes fully into the
    #             clip lamp for the first time in the scene and the camera
    #             medium-tights on her at the end of the turn.
    #         (4) The close. Aeron crosses to the bench. The camera tracks
    #             with him but does not cut — a single move that ends in a
    #             two-shot close across the bench, Zira seated on the high
    #             stool, Aeron standing at the bench edge. The distance
    #             between them is the width of the clock mechanism. Then the
    #             distance is not the width of the clock mechanism anymore.
    #             His hand on her jaw. Her hand in the front of his shirt.
    #             The breath where they stop pretending. The camera holds
    #             the close two-shot through the consent gate.
    #         (5) The aftercare. Different camera vocabulary. Low, the floor
    #             of the workshop, the two of them against the bench, the
    #             clock mechanism on the table above them. Warm, slow, no
    #             push. The scene rests in the low shot until the clock line
    #             lands. After the clock line: tight on the mechanism. Hold.
    #             Hold. The scene ends on the mechanism running backwards by
    #             one second every minute and neither of them explaining it.
    # LIGHTING: Workshop at late-night. The three-lamp configuration from
    #           s08 — bench lamp, forge lamp over the banked forge, clip
    #           lamp on the left edge of the bench pointed down at the
    #           work. The clock mechanism is in the pool of the clip lamp.
    #           Zira's hands are in that pool. Her face is half in the
    #           bench lamp and half in the shadow of her own shoulder until
    #           she turns. When she turns, the bench lamp catches her
    #           fully. Aeron is in the edge of the bench lamp — half in it,
    #           half in the warm darkness between the lamps. At the turn
    #           into close two-shot, the light on both of them is warmer
    #           than the light on the bench. At aftercare, the light is
    #           lower — the clip lamp is still on, the bench lamp has been
    #           clicked off by Zira at some point between the intimate
    #           block and the floor, the workshop is mostly the forge lamp
    #           and the clip lamp. The clock is still in the clip lamp's
    #           pool.
    # SFX: Workshop at night. Forge banked. The distant drip from the pipe
    #      she still hasn't fixed. The small precise sounds of clock tools
    #      — a tweezer, a small driver, the click of a gear being seated.
    #      Her breath. His breath. The door closing behind him at the
    #      start. No music bed until the turn — a single low held cello
    #      note enters at the breath-stop and holds through the consent
    #      gate. At aftercare: silence, then the tiny repeating tick of
    #      the clock mechanism — except the tick is not a normal tick, it
    #      has a faint backstep in it, and the backstep is audible if the
    #      listener is close enough, and Aeron is close enough.
    # FX/COMP: THE CLOCK MECHANISM. A palm-sized brass clock mechanism,
    #          half-assembled on a small felt pad on the bench. Exposed
    #          gears, a small escapement, a single hand. It is not a
    #          production piece. It has the look of a private project —
    #          Zira's tools laid out around it in the particular
    #          arrangement she uses for personal work, which Aeron has
    #          never seen before because Zira has never had a personal
    #          project on this bench in his presence. The clock is the
    #          scene's secondary prop. The primary prop is the two of
    #          them. The clock is the object that tells the audience the
    #          scene is not about the exit plan from s08.
    # BLOCKING: Zira at the high stool at the bench, bent over the clock
    #           mechanism, small tweezer in her right hand, a gear in her
    #           left. She hears him come in. She does not turn. She
    #           speaks the line that opens the scene — the line she has
    #           been carrying since s09a. Then she turns. She does not
    #           stand. She stays on the stool through the jaw-hand and
    #           the shirt-fist. She stands at the consent gate — or she
    #           stays on the stool, depending on which choice the player
    #           takes. The aftercare block is on the floor. The floor is
    #           deliberate. The floor is the opposite of the bench. The
    #           bench is where Zira works. The floor is where Zira is a
    #           person who has to sit down.
    # FACE: Zira — the full register of s08 and s09a present, but not in
    #       order. She is not the Zira of the exit plan and she is not
    #       the Zira of the mess. She is the third Zira, the one she has
    #       not let Aeron see before — the Zira of the clock. The Ash-
    #       market edge is still on her diction but it is pointed inward
    #       tonight. She sharpens into tenderness rather than going soft.
    #       The sharpening is the scene's signature move. Aeron — he
    #       entered the workshop because s14 cost him something and the
    #       cost has no other room. He knows he is not here for
    #       operational reasons. He knows Zira knows. He does not rehearse
    #       what he is going to say because he did not come here to say
    #       anything.

    # ========= VOICE BASELINE =========
    # EMP cadence. Zira drives the diction and the scene's physical tempo.
    # Aeron is sparse through the first two phases and opens up in the
    # aftercare block. The intimate block itself is bracketed — no explicit
    # writing — and the scene exists to produce the aftercare, which is the
    # load-bearing register. Zira's thought voice runs in the intimate
    # bracket region as zthought to carry the emotional continuity. The
    # clock line at the end is hers to deliver. Aeron's answer is the
    # shortest sentence in the scene.

    # scene bg_zira_workshop_night_late with dissolve
    # play ambient "sfx/ambient/workshop_forge_banked.ogg" fadein 2.5

    # ========== PHASE 1 — THE DOORWAY ==========

    "Twenty-three-forty. Eleven and a half hours after the ops wing scene. Aeron has spent the intervening hours at the ops wing side chair through a full shift rotation and then at the mess and then at the corridor outside quarters where he stood for ninety seconds without going in."

    "He did not go to quarters because quarters was the room Tessa had prescribed forty-eight hours ago and the prescription had served its purpose. He did not go to the mess because the mess was where Zira had found him in s09a and the mess had already been spent on her that way. He did not go to the command center because the command center was running without him and his hands on a tactical layer at midnight would have been a demand the room did not need to field."

    "He is at Zira's workshop door."

    "He is at Zira's workshop door because the workshop is the room she goes to when the problem she is working on is not a Ghostline problem, and the problem he is carrying tonight is not a Ghostline problem, and the geometry he is trying to figure out about the rest of his life is being figured out in a register Zira is the only person in this building who speaks."

    athought "I have not been in this workshop since s08. I walked out of s08 with the unlocked drawer and the knowledge that she had built an exit plan for me and the knowledge that she was not going to use it on me unless I asked. The knowledge has been sitting in my sternum for two months."

    athought "I did not come down here to ask for the drawer."

    athought "I do not know exactly what I came down here to ask for. I came down here because the workshop was the only door in this building I was going to open tonight."

    "He knocks once. The s08 knock. The door-knock protocol she keeps because the workshop is a room where she is often holding something she cannot drop."

    "A beat."

    "She does not say 'it's open' the way she did in s08."

    "She says something else."

    z "Did you come to use the door, or did you come to stay."

    "Her voice is at working volume. Not raised for him. She is saying the line to the bench she is bent over and the door is catching the edges of the sound. The line has been prepared — she prepared it on the walk down to the workshop at the end of the day shift and has been holding it since. He can hear the holding in the way the syllables land."

    athought "She is gating the scene at the door. She is not going to let me come in under any other grammar."

    athought "I came down here for the stay."

    "He opens the door."

    "He does not step in yet. He stands in the doorway — one boot across the threshold, one not — the doorway a frame around his silhouette against the corridor spill behind him."

    a "Stay."

    "He says it short. The shortest true sentence he has tonight. The way he said 'I hear you asking' in s09a — with the second-time aim."

    "A beat in the workshop."

    "Zira's hands stop. The tweezer in her right hand pauses above the gear. The gear in her left hand is flat against the felt pad."

    "She does not turn yet."

    zthought "He said stay."

    zthought "He said stay on the first pass. He did not hedge the sentence into a longer sentence. He did not route it through an operational reason. He said stay the way a man says yes to a question he has been answering in his body for two months and only just found the word for in the corridor."

    zthought "I have been preparing for three different answers and the three different answers did not include the clean one."

    zthought "I am going to have to be braver than I prepared to be."

    # ========== PHASE 2 — THE BENCH ==========

    "She sets the tweezer down in the tool groove. She sets the gear down next to the felt pad. Her hands come off the bench in the particular slow way she has when she is letting herself decide one movement at a time rather than doing the whole thing at once."

    "She turns on the high stool. Half-turn. Her body pivots on the stool and she faces him across the workshop."

    "The clock mechanism is still on the bench. The clip lamp is still on it. The mechanism is brass and half-assembled and the size of a palm, and he sees it for the first time, and does not recognize it."

    "He comes in. He closes the door behind him. He crosses the workshop at a pace that is neither fast nor slow — the walking pace of a man who has already decided he is going to be in this room for the rest of the night."

    "He stops at the bench edge across from her."

    "The clock mechanism is between them."

    "He looks at the clock mechanism first because the clock mechanism is a thing he has never seen and the thing he has never seen is easier to look at than the woman who has been watching him from doorways for two months. He looks at the mechanism for three full seconds. Then he looks at her."

    a "You never told me you had a clock."

    "The sentence is a sentence about the bench. It is also an acknowledgement — the soft version, the one that says I see the thing on the bench is new and I am not going to pretend it is not new."

    z "I have not had a clock in this room in your presence before."

    "She does not say more than that about the clock. The clock is not the scene yet. The clock is the scene later. She knows which scene is which."

    z "I have been working on it for a while. I will tell you about it after."

    a "After."

    z "After we find out whether after is a word we are going to have tonight."

    "She says it without the Ashmarket edge — her diction is flat, careful, the volume low. This is the third Zira. The one Aeron has heard at volume maybe twice. She sharpens the words rather than softens them. She is not making the scene easier by saying the things in a softer voice. She is saying them in a more precise voice, which is harder on both of them, which is Zira's gift when she is giving you the gift on purpose."

    zthought "Do not go soft. He came here for the stay. Stay is not a soft word. Stay is a hard word said quietly."

    "She reaches across the bench. Her hand is steady the way her hands are steady when she is holding a forge-tool — the particular steadiness of a woman who has not let her hands shake in a room that mattered since she was eighteen."

    "She takes his hand."

    "Not the whole hand. Two fingers from the back — a light hold, the kind a jeweler takes with a client's hand when she is going to show them a ring. The touch is a small thing. The touch is also the first time Zira has taken his hand on purpose in five months."

    "She draws his hand to her face."

    "She puts his hand on her jaw."

    "His palm along the line of her jaw, his thumb at the hinge, his fingers against the soft space under her ear. She holds his hand there with her own hand — not pressing, not pinning, just confirming the position. Then her hand comes away from his, and his hand stays where she put it, and the confirmation is complete."

    athought "She put my hand on her face. She did not let me put my hand on her face. There is a difference between those two things and the difference is that she is going to be the one setting the shape of this tonight because she has been carrying the shape since s09a and the shape is hers to spend."

    athought "I am going to let her spend it."

    "Her left hand comes up to the front of his shirt. Not a fist — not yet. A flat open press of the palm at the center of his sternum. She finds the breath in him. She waits for the breath to come out. She finds it going in on the next cycle."

    "Then the palm closes. Her fingers curl into the fabric. The fist is small — half a handful of shirt. The knuckle of her index finger is against his collarbone through the cloth."

    "They both stop pretending."

    "They have been pretending — in the workshop doorway, in the mess, in the war room, at the ops table, on a Ghostline relay alcove sometime in Act II, at the edge of the Lower Spans in Act I — that the thing between them was tactical. The pretending has been load-bearing for both of them. The pretending has been a scaffolding both of them used to build two years of trust."

    "The scaffolding is not needed for the building anymore."

    "The breath where they stop pretending is a single breath — his, drawn in and held — and Zira hears the hold and does not let him ride the hold out."

    z "I have never been this scared of anything I wanted."

    "The sentence is said at close range. The close range is maybe six inches between their faces. She is looking up at him from the stool. Her eyes are clear. Her voice is not. Her voice is the voice she uses once every eighteen months when the thing she has to say has to be said by a person instead of a blade."

    zthought "Say it. Do not route it. Do not let it become a line you can carry back out of the workshop as a sentence you delivered."

    zthought "Make it a sentence you gave."

    z "I am not saying it so you will answer it. I am saying it because I promised myself on the walk down here that if you came in and said stay I was going to say one true thing before I did anything with my hands, because my hands know how to do the rest of this without needing a true sentence and I wanted the true sentence to exist anyway."

    z "The true sentence exists now."

    z "You do not have to carry it. I am carrying it."

    "Aeron's hand on her jaw does not move. His thumb is at the hinge. The small pulse in her neck is against his fingertips. He can count it if he wants to. He does not count it. He does not count it because counting it would be Aeron-in-the-mug-scene and the mug-scene is not the scene they are in anymore."

    a "Zira."

    z "I am listening."

    a "I am not walking out of this workshop tonight."

    "He says it the way she said the stay line at the door. Short. Flat. True."

    "Not a contract. Not a promise for tomorrow. A statement about the room he is in at the moment."

    zthought "He said not walking out. That is the sentence. That is the sentence he has tonight. It is the sentence I asked for in a different form in the mess — I am not going to pretend it isn't. It is the sentence that makes the rest of the scene possible."

    zthought "I am going to take it."

    zthought "I am going to take it and I am going to be brave about what I do with my hands next, because what I do with my hands next is the part I have been preparing for and the part the preparation is not going to save me from."

    # ========== PHASE 3 — THE CONSENT GATE ==========

    "Zira's hand on his shirt does not release."

    "Her other hand — the one that put his palm on her jaw and then came away — goes to the back of his wrist. Not to guide him. To be there. The touch is a permission being offered and a permission being waited for in the same gesture."

    z "Tell me which room we are in."

    z "I am going to give you three rooms. All three of them end with you not walking out of this workshop tonight. That is not the question. The question is which room."

    z "You can say all three of them out loud and I will hear all of them as real answers. There is no wrong one."

    "She waits."

    "The clip lamp hums faintly. The forge ticks as a small ember shifts. The drip from the pipe she has not fixed does its slow quarter-time. Aeron's hand is still on her jaw. Her fist is still in his shirt. The clock mechanism is still in the pool of clip-lamp light on the bench to his left."

    "He lets the room settle on him. He lets the decision settle on him. He does not rush. She has given him the room to not rush and he takes it."

    menu:
        "Yes. Now.":
            jump a4_s15_zira_yes_now

        "Slower. I want to remember this.":
            jump a4_s15_zira_slower

        "Not tonight — but don't leave.":
            jump a4_s15_zira_not_tonight


    # ========== PHASE 4A — YES NOW ==========

label a4_s15_zira_yes_now:

    a "Yes."

    a "Now."

    "Two words. Said at the close range. His thumb at her jaw-hinge presses a fraction of a millimeter — not to pull her toward him, to tell her he has heard the question and the answer is aligned with his hand."

    "Zira's fist in his shirt closes one more notch."

    zthought "He said yes now. He said it in the register of a man who has been waiting to say yes now for longer than either of us is going to admit tonight. I am not going to admit it either. Not out loud. Not now. Later, maybe, when we are on the floor and the clock is on the table above us."

    zthought "Not now."

    zthought "Now is the yes."

    "She stands."

    "The stool scrapes back. Her hand in his shirt pulls him a quarter-step forward. The bench is at her hip. The clock mechanism is an inch from the edge of her left elbow and she is aware of the clock mechanism because she has been aware of the clock mechanism every second of the last eleven months and she reaches without looking and slides the felt pad with the mechanism on it two inches deeper into the bench, out of the way of any motion that might knock it."

    "The mechanism stays lit under the clip lamp."

    "She does not click the clip lamp off."

    "She clicks the bench lamp off. The workshop dims into the forge lamp and the clip lamp. The clip lamp is on the mechanism. The mechanism is behind them now."

    "She turns back to him."

    z "I am not going to be soft about this."

    a "I know."

    z "I am going to be exact."

    a "I know."

    z "I have been exact about you for two years and tonight is not going to be the night I stop."

    "Her hand comes off his shirt. Her hand goes to his jaw — the mirror gesture. Her thumb at his hinge, the way his thumb is at hers. The two hands are a bracket around both their faces."

    "She kisses him."

    "The kiss is not a first kiss in the grammar of first kisses. It is a first kiss in the grammar of two people who have been in the same rooms together for two years and have been keeping their mouths on the other side of a wall the whole time and have finally decided to walk through the wall. The kiss is not about exploration. It is about arrival."

    "The first kiss lasts as long as it lasts."

    "When she pulls back, her hand does not leave his jaw. Her other hand is at the buckle of his belt — not undoing it, resting on it, a question with her fingers."

    z "Bench or floor."

    a "Floor."

    z "Floor."

    # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
    # [INTIMATE CONTENT HERE]
    # Yes-Now variant. Tempo: direct, exact, unhurried in the specific way
    # that is not the same as slow. Zira drives. She does not go soft. She
    # sharpens into tenderness — the sharpening is the register. The
    # location resolves to the workshop floor with his jacket under her
    # shoulders at some point, the bench at their side, the clip lamp still
    # lit on the clock mechanism above them. Aeron is present in a way he
    # has not been present in Act IV — the exhaustion is not in his body
    # tonight because the exhaustion is the other room and this is not that
    # room. Zira stays in her diction throughout. The Ashmarket edge does
    # not leave; it is pointed inward rather than outward. She does not
    # lose her voice. She does not want to lose her voice. She wants him to
    # hear her. Closing beat: both of them on the floor, breath settling,
    # the bench overhead, the clock mechanism's faint backwards-tick
    # audible in the quiet between them.
    # ---------- [ END INTIMATE BLOCK ] ----------

    jump a4_s15_zira_aftercare


    # ========== PHASE 4B — SLOWER ==========

label a4_s15_zira_slower:

    a "Slower."

    "One word. Said at the close range. His thumb at her jaw-hinge does not move. His hand does not press. The word is the whole message."

    a "I want to remember this."

    "A second sentence. He did not plan to add the second sentence. He adds it because Zira's face at close range is a thing he wants to be accurate about in his memory and he is telling her that in advance so she knows what tempo the scene is running at."

    "Zira's fist in his shirt does not close further. Her knuckle against his collarbone flattens. Her palm goes flat against his sternum — the open press of her palm from the s09a sentence made physical."

    zthought "He said slower. He said I want to remember this. He said the second sentence because he did not want the first sentence to be mistaken for hedging."

    zthought "He is not hedging. He is asking for the shape of the night to be a shape he can carry as a memory intact. He is asking to be able to close his eyes two years from now and find this room exactly as it was tonight."

    zthought "I can give him that. I can give him that better than I can give him any other version of this, because slow is the register I have been working at on the clock mechanism for eleven months and slow is a thing my hands know."

    zthought "Do not go soft. Slow is not soft. Slow is exact."

    z "Slower."

    z "Then slower is what we are doing."

    "She stands, but she stands the way she straightened in s08 — the small pain-wince, the decision to let him see the small pain-wince, the intimacy of not hiding it. The stool scrapes back an inch, not a whole length."

    "Her hand on his shirt releases. Both her hands come up to his face — one at each jaw, the mirror bracket. She holds him. She does not kiss him yet."

    "She looks at him."

    "The look is long. The look is the thing the tempo is being set by. Her eyes move from his left eye to his right eye to his mouth to the small notch at the top of his sternum where his shirt is unbuttoned to the hollow of his throat, and she is not performing the look, she is cataloguing him, which is a Zira-at-work gesture redirected at a scene that is not operational."

    z "I am going to look at you for a minute."

    a "Okay."

    z "I am going to look at you and I am going to tell you what I am looking at, because if slow is the register then the register has to include the naming. I do not want you to spend the next twenty years wondering what I was thinking while I was looking. I am going to tell you while I am doing it."

    athought "She is going to narrate."

    athought "She is going to narrate because narration is a slow-tempo discipline and because Zira's version of slow is a version where the words do not let the body rush."

    athought "I am going to let her narrate."

    z "Your mouth is not quite symmetric. The left side of your upper lip has a half-millimeter lift that runs when you are about to say something you have not rehearsed. I have been watching that lift in ops briefings for two years. I am looking at it now because the lift is there right now. I am going to kiss you on the lift in a minute. Not yet."

    z "Your eyes are tired but they are not the eyes of the mess hall in s09a. The tired is a different tired. The tired is the tired of a man who has been sitting in a chair he did not used to sit in and is learning the shape of the new chair. I saw you take the side chair at the ops wing today. I did not comment on it. I am commenting on it now, because slow is the register where the things that did not get said earlier get said now."

    z "Your hand on my face has been on my face for four minutes. I am not going to tell you to move it."

    "She moves her face into his palm — a small pivot. Her cheek settles against the meat of his thumb. The hand is no longer holding her jaw. The hand is being held by her face."

    z "Bench or floor."

    a "Floor."

    z "Floor. Slowly."

    # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
    # [INTIMATE CONTENT HERE]
    # Slower variant. Tempo: deliberate, narrated where natural, exact. The
    # tempo is set by Zira's cataloguing in phase 4B — she is giving him a
    # memory to carry, and the register of the scene is the register of two
    # people who have decided the only way they are going to do this is to
    # do it where the details survive. Zira narrates in places without
    # letting the narration become a performance — the narration is the
    # slow-register discipline, not a show. Aeron answers her narration
    # with his own quiet attention. The floor, the jacket, the bench at
    # their side, the clip lamp still lit on the clock mechanism above
    # them. At the close, he returns the narration briefly — one or two
    # lines of Aeron-noticing-Zira, because the exchange of noticing is
    # what the slower register earns. Closing beat: both of them on the
    # floor, the clock mechanism's backwards-tick faintly audible, her
    # hand on his sternum where the palm-press was.
    # ---------- [ END INTIMATE BLOCK ] ----------

    jump a4_s15_zira_aftercare


    # ========== PHASE 4C — NOT TONIGHT ==========

label a4_s15_zira_not_tonight:

    a "Not tonight."

    "He says it at the close range. His thumb at her jaw-hinge does not move. His hand does not press. The word is not a rejection — the tempo of the word tells her that before the word is even finished."

    a "But don't leave."

    "Second sentence. The full stay."

    "Zira's fist in his shirt does not close further. Her knuckles against his collarbone flatten and then slowly relax. Her other hand — the one at the back of his wrist — stays there."

    zthought "He said not tonight."

    zthought "He said not tonight and followed it with don't leave in the same breath, which means the not-tonight is not a no, it is a rain-check on a tempo. He is not walking out of the workshop. He is asking me to be in the workshop with him tonight in a register that is not the intimate register."

    zthought "I can give him that. That register is the s09a register and I have been in it before. The preparation I did on the walk down was for three registers and this is one of the three. I am not disappointed."

    zthought "I am not disappointed because disappointment is the grammar of a scene where the ask was for a deliverable. The ask was not for a deliverable. The ask was for the stay. He is staying. I got the ask."

    zthought "Do not go soft. Soft would be the grammar of disappointment dressed up. I am not going to dress up a disappointment I do not have."

    z "Not tonight."

    z "Then not tonight is what we are doing."

    z "Don't leave is also what we are doing. Those two things fit in the same night."

    "Her hand on his shirt releases — all the way this time. Both her hands go to his wrist where her one hand had been. She holds his wrist between her two hands for a beat. The hold is a non-erotic hold. It is a holding of his wrist in the way a surgeon holds a wrist — firm, attentive, without heat."

    "She brings his hand down from her jaw. Not away from her. Down. She presses the back of his hand against the bench beside the clock mechanism and keeps her palm over his knuckles."

    z "Sit down."

    a "Sit down where."

    z "I do not have another stool. Sit down on the floor. I am going to sit down on the floor with you. The floor is the register for not-tonight-but-don't-leave and the floor is where I was going to end up tonight anyway. I am just going to end up there a different way."

    "She comes off the stool."

    "She comes off the stool with the same slow decision-per-movement she used to set the tweezer and the gear down. She is down on the workshop floor before he is, in the space between the bench and the wall, her back against the bench leg, her legs crossed. She pats the stone next to her."

    z "Here."

    "He sits."

    "His back is against the bench leg on her right side. Their shoulders are touching. Her hand finds his hand on the stone between them and holds it. Not the two-fingers jeweler hold. The full palm hold — hand in hand, a handshake resting on the floor."

    z "We are going to be here for a while."

    a "Good."

    # ---------- [ NO INTIMATE BLOCK IN THIS VARIANT ] ----------
    # Not-tonight variant: the scene proceeds directly to aftercare with
    # the intimate block replaced by a non-erotic hold on the workshop
    # floor. The hold is deliberate. The hold is the physical realization
    # of "see that I am asking" (s09a) in the register where the seeing is
    # enough for the night. The clock mechanism is still lit under the clip
    # lamp on the bench above them. Her thumb strokes the back of his hand
    # once — the small precise Ashmarket tell of a woman who has decided
    # the hand she is holding is going to stay held.
    # ---------- [ END NON-EROTIC HOLD ] ----------

    jump a4_s15_zira_aftercare_not_tonight


    # ========== PHASE 5 — AFTERCARE (YES NOW / SLOWER) ==========

label a4_s15_zira_aftercare:

    "Later."

    "The clip lamp is still on the clock mechanism. The forge lamp is banked to its lowest setting. The bench lamp is off. The workshop is in the particular warm darkness that Zira's workshop gets when the bench lamp is off and the clip lamp is doing all the work at the bench."

    "They are on the floor."

    "Zira is against the bench leg — the nearer one, the one she has been leaning against for most of a decade when she has had to sit down in her own workshop. Aeron is on the floor next to her. His jacket is under her shoulders. Her head is against the bench leg through the folded jacket. His arm is around her shoulders. Her hand is on his thigh, flat, not moving."

    "The clock mechanism is on the table above them."

    "They have not spoken for a while."

    "The drip from the pipe she has not fixed does its slow quarter-time. The forge makes a small settling noise as an ember moves. There is another sound in the room — smaller, more regular — that Aeron has been hearing for about two minutes without identifying."

    "He identifies it now."

    "It is the clock mechanism."

    "The clock mechanism is ticking. It is ticking on the felt pad on the bench above them, in the pool of clip-lamp light. The tick is small. The tick is also — and this is the thing Aeron's ear has been catching without naming — not quite a normal tick."

    "The tick has a half-beat in it. A backstep."

    "Every tick, in the interval between the tick and the next tick, there is a small rewind. A quarter of a tick's worth of going back before the next tick goes forward."

    "He listens to the tick for a full minute."

    athought "The tick is not a normal tick. The tick has a rewind."

    athought "She is working on a clock that rewinds."

    "He does not ask. He waits. Zira is the one who is going to name the clock and he has learned, in s08, not to rush her toward the naming of a thing she built."

    "After the minute, Zira stirs. She does not sit up. She turns her face against his arm and speaks to the underside of his sleeve."

    z "You have been listening to the tick for a minute."

    a "Yes."

    z "You noticed the rewind."

    a "Yes."

    "A beat."

    z "It runs backwards by one second every minute."

    a "I can hear that."

    z "I have been building it for eleven months."

    "Another beat. Her thumb on his thigh moves once — the small precise Ashmarket tell, redirected as a pulse of her attention against his skin through the cloth."

    z "I do not know why."

    "She says it without the edge. The diction is flat. The flatness is the flatness of a woman telling a truth she has not told anyone out loud including herself."

    z "I started it in the week after the Lower Spans. I had a piece of brass from a thing I stripped in the Ashmarket in Act II and I was turning it over in my hand at the bench one night and I thought: I am going to build a clock. I had never built a clock. I had built Ghostline relays and I had built lock-picks and I had built one forge hammer and I had built the thing you and I do not talk about because you have been too gentle to ask about it. I had not built a clock."

    z "I started building one. I got to the escapement and I realized I did not want the escapement to run forward the way escapements run. I re-worked the escapement so that the balance wheel has a short counter-motion on every cycle. One-sixtieth of a cycle backwards per cycle. That works out to one second every minute in the forward direction of time being reclaimed by the backward direction."

    z "It does not keep time. It loses time. It loses time on purpose at a precise rate. One second a minute. Sixty seconds an hour. Twenty-four minutes a day."

    z "I have been building it for eleven months and I do not know why I am building it."

    z "That is not a phrase I use about my own work often. Usually I know why. Usually the why is loud. This one is quiet. This one is a thing I come down here in the middle of the night and work on because the work is the thing I can do when my hands need to be doing something and the Ghostline is running without me and the exit plan is folded in the drawer and there is no other work I can do that is not an operational work."

    z "It is not an operational work. It is the clock."

    "She stops."

    "Aeron listens to the tick-rewind-tick-rewind-tick for another few seconds."

    athought "She is building a clock that runs backwards by one second every minute. She has been building it for eleven months. She does not know why."

    athought "I know why."

    athought "I know why and I am not going to explain it and she is not going to ask me to explain it because the naming would cheapen the thing. The thing is a grief she has been metabolizing in brass for eleven months and the grief is not mine to name on her behalf."

    athought "The grief is — the grief is the thing she has been doing with her hands instead of saying out loud. Zira does not have a language for the losses she has taken. Zira has hands. The hands have been building a clock that gives back one second every minute as a private reparation for a debt Zira has not named to anyone, maybe not even to herself. The clock is a prayer the way Lyra has prayers. Lyra prays to Seren. Zira prays to brass."

    athought "The prayer is: the seconds come back. Not all of them. Not enough of them. Just one. Every minute. A precise unpayable amount. That is all a clock like this can give."

    athought "I know what it is because I have been trying to give back seconds in the ops wing for three months and the seconds I am trying to give back are the seconds of my own command, and the giving-back is not working. The clock works. The clock gives back a second a minute without fail. The clock is better at giving back the seconds than I am."

    athought "She does not know why she is building it and I am not going to tell her."

    athought "I am going to tell her I know why. Not more than that."

    "He turns his face against the top of her hair. His mouth is at her temple. He speaks into her temple because the volume of the answer is the volume of something said into a temple."

    a "I know why."

    "She does not ask him to explain."

    "She does not ask him to explain because she heard the sentence and she heard the second thing in the sentence, which was the not-explaining, and the not-explaining is the respect she needed him to hold."

    zthought "He said I know why."

    zthought "He did not explain. He is not going to explain. He is going to let the clock be the clock and let me find out what the why is on my own time and he is going to know the why in the meantime and not take it from me."

    zthought "That is the thing I did not prepare for on the walk down here. I prepared for three registers of being touched. I did not prepare for being heard about the clock."

    zthought "I am not going to cry. I am not going to cry because I am Zira and Zira does not cry on the workshop floor in front of Aeron. I am going to instead do the small precise Ashmarket tell I do when I am not crying and I am going to let him feel the tell through the cloth of his trouser leg where my thumb is, and he is going to notice it, and he is going to know what the tell means."

    "Her thumb on his thigh does the small precise Ashmarket tell. Three short pulses and a long one. The tell is a private vocabulary. Aeron has seen her do it twice before in the workshop and once at the Lower Spans and he does not have a translation for the four-pulse version. The four-pulse version is new. Zira is adding a glyph to her private vocabulary in real-time and giving it to him in the same gesture."

    athought "That is the fourth pulse. I do not know what the four-pulse version means and I am not going to ask and she is not going to say. The four-pulse is a glyph she is adding to her vocabulary tonight and she is adding it in a room where I am the witness. That is the whole transaction."

    "He does not move his arm off her shoulders."

    "They sit on the workshop floor with the clock running backwards by one second every minute on the bench above them for another long quiet interval. Neither of them speaks. The silence is not the silence of a scene that has ended. The silence is the silence of a scene that is still happening and does not need dialogue to keep happening."

    "At some point — not immediately, not soon, but at some point — the clip lamp on the clock will be clicked off by Zira and the clock will tick in the dark of the workshop without anyone watching it. At some point after that — not immediately, not soon — the two of them will get off the floor."

    "For now they are on the floor."

    "The clock gives back one second a minute."

    "Aeron's hand on her shoulder does not move."

    "The scene holds on the clock mechanism in the clip-lamp pool. The clip-lamp pool is the only light in the frame. The tick is the only sound. Fade."

    jump a4_s15_zira_state_updates


    # ========== PHASE 5 (ALT) — AFTERCARE (NOT TONIGHT) ==========

label a4_s15_zira_aftercare_not_tonight:

    "Later."

    "The bench lamp has been clicked off at some point in the intervening minutes. The clip lamp is still on the clock mechanism. The forge lamp is banked low. The workshop is in the warm darkness."

    "They are on the floor."

    "His back is against the bench leg. Her back is against the bench leg on his left. Their shoulders are touching. Her hand is still holding his — the full-palm hold, not the two-finger jeweler hold, settled on the stone between their hips. His thumb is at the base of her thumb. Her thumb is over his knuckle."

    "They have not moved in a while."

    "Aeron has been listening to the clock mechanism for about two minutes without identifying the sound. The sound is the tick, but the tick has a small half-beat in it — a rewind, a quarter of a tick's worth of going back before the next tick goes forward."

    "He identifies it now."

    athought "The tick is not a normal tick. The tick has a rewind. She is working on a clock that rewinds."

    "He does not ask. He waits."

    "Zira speaks first."

    z "You hear the tick."

    a "Yes."

    z "You hear the rewind."

    a "Yes."

    z "It runs backwards by one second every minute."

    a "I can hear that."

    z "I have been building it for eleven months."

    "A beat. Her thumb over his knuckle stays still."

    z "I do not know why."

    z "I started it in the week after the Lower Spans. I had a piece of brass from a thing I stripped in the Ashmarket in Act II and I was turning it over in my hand at the bench one night and I thought: I am going to build a clock. I had never built a clock. I had built Ghostline relays and I had built lock-picks. I had not built a clock."

    z "I started building one. I got to the escapement and I realized I did not want the escapement to run forward the way escapements run. I re-worked it. The balance wheel has a counter-motion on every cycle. One-sixtieth of a cycle backwards per cycle. One second every minute in the forward direction being reclaimed by the backward direction."

    z "It does not keep time. It loses time. It loses time on purpose at a precise rate. One second a minute. Sixty seconds an hour. Twenty-four minutes a day."

    z "I come down here in the middle of the night and work on it because the work is the thing I can do when my hands need to be doing something and there is no other work that is not an operational work."

    z "I do not know why I am building it."

    "She stops."

    "Aeron listens to the tick-rewind-tick-rewind for another few seconds."

    athought "I know why. I know why because I have been trying to give back seconds in the ops wing for three months and the giving-back is not working. The clock works. The clock gives back a second a minute without fail. The clock is a grief Zira has been metabolizing in brass for eleven months and the grief is not mine to name on her behalf."

    athought "I am going to tell her I know why. Not more than that."

    "He turns his face toward her. Her temple is against the bench leg. He speaks into the warm dark between them at the volume of a thing said between two people on a workshop floor at midnight."

    a "I know why."

    "She does not ask him to explain."

    zthought "He said I know why. He did not explain. He is going to let the clock be the clock. He is going to know the why in the meantime and not take it from me."

    zthought "I prepared for three registers of touch tonight and one of them was the not-tonight register and I prepared for the not-tonight to be a small bitter thing I would swallow cleanly. It is not a small bitter thing. It is the register where he is on the workshop floor with my hand in his hand listening to my clock and telling me he knows why. There is nothing about this that is bitter."

    zthought "I am not going to cry. I am going to do the tell instead."

    "Her thumb over his knuckle does the small precise Ashmarket tell. Three short pulses and a long one. The four-pulse version. Aeron does not have a translation for the four-pulse version."

    athought "The four-pulse is new. Zira is adding a glyph to her private vocabulary in real-time. I am the witness. I do not know what it means. I am not going to ask. She is not going to say."

    "He does not move his hand. He does not speak again. The silence is the same silence as the other variants of this scene — the silence of a scene that is still happening and does not need dialogue to keep happening."

    "The clock gives back one second a minute on the bench above them."

    "They sit on the workshop floor with the clock running backwards. Neither of them speaks. The scene fades on the clock mechanism in the clip-lamp pool. The clip-lamp pool is the only light in the frame. Fade."

    jump a4_s15_zira_state_updates


    # ========== STATE UPDATES (CONVERGENCE) ==========

label a4_s15_zira_state_updates:

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=2, attraction=2)
    $ flag("zira_erotic_deepening_scene_complete", True)
    $ flag("zira_clock_shown", True)
    $ flag("aeron_said_stay_in_doorway", True)
    $ canon_set("zira.clock_mechanism", "brass_palm_sized_runs_backwards_one_second_per_minute_eleven_months_in_progress")
    $ canon_set("zira.ashmarket_tell", "four_pulse_glyph_new_at_a4_s15")
    $ canon_set("aeron.zira.intimacy_stage", "deepened")
    $ npc_remember("Zira", "said_i_have_never_been_this_scared_of_anything_i_wanted", weight=3)
    $ npc_remember("Zira", "showed_the_clock_to_aeron", weight=3)
    $ npc_remember("Aeron", "said_stay_at_the_doorway", weight=3)
    $ npc_remember("Aeron", "i_know_why_about_the_clock", weight=3)
    $ nudge_poly("Zira", +1)
    $ tp_seed("a4.zira.stayed")
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s15_zira_deepening_erotic_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Twenty-three-forty the night of a4_s14. Aeron has spent the day's
#     ops-wing shift in the side chair. He has stood in the corridor
#     outside quarters without going in. He has walked to the workshop
#     because the workshop is the only door in the building he was going
#     to open tonight.
# cann.what_happened:
#   - Aeron at the workshop door. Zira at the bench, working on a small
#     personal project — a palm-sized brass clock mechanism. Zira speaks
#     without turning: "Did you come to use the door, or did you come to
#     stay." Aeron answers from the doorway: "Stay."
#   - Aeron enters. The clock mechanism is between them on the bench.
#     Aeron acknowledges the clock in one line. Zira tells him the clock
#     is the scene later, not now.
#   - Physical buildup: Zira places Aeron's hand on her jaw. Her hand
#     goes to the front of his shirt — first flat palm, then a small
#     fist. They stop pretending. Zira delivers the load-bearing sentence:
#     "I have never been this scared of anything I wanted." She frames it
#     as a sentence she is carrying so he does not have to.
#   - Aeron's single spoken anchor: "I am not walking out of this
#     workshop tonight." This is his answer to the frame Zira set at the
#     door. It is not a contract for tomorrow — it is a statement about
#     the room he is in at the moment.
#   - Consent gate. Three-choice Ren'Py menu. All three branches end with
#     Aeron not walking out of the workshop. The branches select the
#     tempo and the register, not the outcome.
#     - "Yes. Now." — erotic, direct, bracketed as [INTIMATE CONTENT
#       HERE] for player authoring. Zira sharpens into tenderness, does
#       not go soft. Bench-to-floor. Tempo: exact, unhurried-but-not-slow.
#     - "Slower. I want to remember this." — erotic, deliberate, bracketed
#       as [INTIMATE CONTENT HERE]. Zira narrates the cataloguing as a
#       slow-register discipline. She tells him what she is looking at
#       while she is looking at it. Bench-to-floor.
#     - "Not tonight — but don't leave." — non-erotic variant. Aeron
#       holds the not-tonight as a rain-check on a tempo, not a refusal.
#       Zira hears it that way immediately. She comes off the stool, sits
#       on the workshop floor with him, takes his hand in a full-palm
#       hold. No intimate block. The physical realization of s09a's "see
#       that I am asking" in the register where the seeing is the whole
#       gift.
#   - Aftercare (all variants converge on the clock beat with minor
#     variant-specific framing):
#     - Both of them on the workshop floor. Clip lamp still on the clock
#       mechanism on the bench above them. Aeron listens to the clock
#       tick for two minutes before identifying the rewind in the tick.
#     - Zira names the clock. She tells him she has been building it for
#       eleven months since the week after the Lower Spans, that she
#       re-worked the escapement so the balance wheel has a counter-
#       motion on every cycle, that the clock runs backwards by one
#       second every minute (sixty seconds an hour, twenty-four minutes
#       a day), and that she does not know why she is building it.
#     - Aeron's answer, said into her temple (yes-now/slower) or into the
#       warm dark between them (not-tonight): "I know why." He does not
#       explain. The not-explaining is the respect the moment needs him
#       to hold.
#     - Zira does not cry. She does the small precise Ashmarket tell with
#       her thumb — three short pulses and a long one, the four-pulse
#       version, which is a new glyph in her private vocabulary. She is
#       adding a glyph to her vocabulary in real-time with Aeron as the
#       witness.
#     - Scene fades on the clock mechanism in the clip-lamp pool. The
#       clip lamp is the only light. The tick is the only sound.
# cann.aeron_state:
#   - Post-s14. Exhaustion is still in his body but this workshop is the
#     other room — it is not the room the exhaustion belongs to. He came
#     to the workshop because the workshop is the only door in the
#     building he was going to open. He did not rehearse what he was
#     going to say because he did not come to say anything.
#   - The "stay" answer at the doorway is the cleanest sentence he has
#     said to Zira in Act IV. It is the answer he has been answering in
#     his body for two months and only just found the word for in the
#     corridor. The doorway is where he says it because Zira gated the
#     scene at the door.
#   - In the aftercare, he holds the grief-respect line on the clock. He
#     knows why she is building it. He does not tell her why. The not-
#     telling is the gift. He has learned that register from s08, s09a,
#     and Tessa's "held, not fixed."
# cann.thematic_flags:
#   - The doorway gate. Zira refuses to let the scene happen on any
#     grammar except "stay." The gate is the Act IV version of the
#     "see that I am asking" move in s09a — the gate is the physical
#     realization of the ask.
#   - Sharpening into tenderness. Zira's signature register move. She
#     does not go soft. The Ashmarket edge is pointed inward rather than
#     outward. Slow is exact, not soft.
#   - The clock. Primary new symbol. The clock is grief metabolized in
#     brass. The clock is Zira's version of a prayer. Lyra prays to
#     Seren; Zira prays to the escapement. The clock gives back one
#     second a minute — a precise unpayable reparation for a debt Zira
#     has not named to anyone, maybe not even to herself. The clock is
#     the scene's primary symbol and it is entirely new — Zira has
#     never been shown working on a clock before this scene.
#   - "I know why" without explanation. The respect register. Aeron has
#     learned that the naming would cheapen the thing. He holds the
#     knowing in a room where Zira is the one who gets to find the
#     naming on her own time.
#   - The four-pulse Ashmarket tell. Zira adding a glyph to her private
#     vocabulary in real-time. The witness is Aeron. Aeron does not have
#     a translation for the four-pulse version. He is not going to ask.
#     She is not going to say. The addition of the glyph is the whole
#     transaction.
# cann.character_moments:
#   - Zira: "Did you come to use the door, or did you come to stay."
#     The line is prepared — she rehearsed it on the walk down — but
#     the preparation does not diminish it. Zira, sharpening into
#     tenderness on the stool. Zira naming the clock. Zira doing the
#     four-pulse tell instead of crying.
#   - Aeron: "Stay" at the doorway as the single-syllable answer. "I am
#     not walking out of this workshop tonight" as the only contract he
#     is willing to sign and the exact contract Zira was willing to
#     accept. "I know why" as the grief-respect line for the clock.
# cann.callbacks:
#   - a4_s08_zira_exit_plan_emp: the unlocked drawer. The clock is the
#     private project Zira has been working on in the same workshop
#     since before the drawer was built. The drawer is the operational
#     project; the clock is the personal one. Two drafts of the same
#     activity. The scene in s15 is the second drawer finally being
#     opened.
#   - a4_s09a_she_calls_him_out_emp: "See that I am asking" — the pre-
#     erotic emotional opening. s15 is the physical realization of that
#     ask. The "I hear you asking" sentence from s09a is not repeated
#     here because the hearing is now the being-in-the-workshop. The
#     gate at the door is the s09a ask rephrased as a tempo decision.
#   - a1_s20_lower_spans_emp: "on your six" — the origin of the Zira-
#     Aeron trust line. Zira started building the clock "the week after
#     the Lower Spans." That is not a coincidence. That is the week the
#     relationship that made this scene possible began.
#   - a4_s14_return_to_the_table_emp: Aeron taking the side chair. Zira
#     at the foot of the ops table, seeing the side chair choice and not
#     commenting on it. The not-commenting in s14 is a down payment on
#     the scene in s15 — Zira let the seating choice be private in the
#     ops wing so that the private thing could be the thing the two of
#     them spent together later. The two scenes are a single geometry
#     decision split across two rooms.
#   - a4_s10_what_selene_meant_emp: "delegate the question." Zira's
#     version of the delegation here is that she delegates the reason
#     for the clock. She has been building it for eleven months and
#     does not know why. She is delegating the question to the clock
#     itself. Aeron's "I know why" is the received delegation — he is
#     holding the answer so she doesn't have to.
#   - a4_s04_lyra_unbuckled_emp: Lyra's "Anayet" scene — the other Act
#     IV LI intimacy beat. Cross-LI note: Lyra's register is prayer
#     language, Zira's register is escapement language. Both are
#     prayers. Both pray at a precise rate. The parallel is deliberate.
# cann.block_status: drafted, consent-gated, three-branch
# cann.requires_followup:
#   - The clock is now canon. Any downstream Zira scene can reference
#     the clock. The clock should not be explained further on-page — the
#     "eleven months without knowing why" should remain the clock's
#     canonical register until at least late Act V, if ever.
#   - The four-pulse Ashmarket tell is now canon. Future Zira scenes can
#     use the three-pulse version as established and the four-pulse
#     version as Aeron-specific. Aeron does not get a translation for
#     the four-pulse version at any point in Act IV.
#   - The three-variant branching should converge on tp_seed
#     a4.zira.stayed for all downstream Act IV and Act V EMP scenes.
#     Downstream scenes should not branch again on the yes-now/slower/
#     not-tonight distinction — the distinction is a tempo memory for
#     the player, not a state the later game branches on.
#   - Aeron "I am not walking out of this workshop tonight" is a Zira-
#     specific token. A later Zira scene can reference it as the
#     sentence that opened the intimate phase of the Act IV Zira arc.
#   - Selene/Zira cross-reference: Zira's clock is the analog of
#     Selene's sister Ilene framework (a4_s12a) — both women are
#     metabolizing an unreachable loss through a private discipline
#     (teaching, clock-making). The parallel is load-bearing for the
#     Act IV thematic bed but should not be named in dialogue.
