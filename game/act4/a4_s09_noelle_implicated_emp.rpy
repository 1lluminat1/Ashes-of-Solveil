# =======================================================
# ACT 4 - Scene 09: Noelle Signs (Empathy Path)
# File: a4_s09_noelle_implicated_emp.rpy
# Type: NOELLE ARC BEAT — the analyst becomes a strategist.
# Matrix: Noelle's counter-framework requires her to place people. Aeron witnesses.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s09_noelle_implicated_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s09_noelle_implicated_emp:
    $ show_timeline("28th of Forge, 390 A.C.", "09:00", "Phoenix Secondary Base — Noelle's Workspace")


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("noelle_korr", to_stage=3, source="a4_s09_noelle_implicated_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked, the same discipline as the a4_s03 Noelle workspace
    #         scene. Noelle's rooms are always shot steady. The frame is her
    #         authority and the authority is what she is about to change the
    #         meaning of, so the camera gives her the steadiness she needs.
    #         Open on the workspace in its now-familiar configuration — the
    #         console, the crystal stand, the three task lamps. Noelle is at
    #         the console. Aeron enters alone this time. No Selene. This is
    #         deliberate: the scene needs to be two people.
    #         When Noelle activates the crystal and the counter-framework
    #         resolves above the stand: hold wide on the projection with
    #         both figures in the frame. Do not push in on the projection.
    #         Push in instead on Noelle's face as she begins to explain,
    #         slowly, over the length of her explanation, until by the end
    #         of the explanation the camera is tight on her and the
    #         projection is blurred at the edges of the frame.
    #         When she asks for permission: hold the tight. Do not cut away.
    #         The scene is about her face during the asking.
    #         When Aeron answers: do not cut to him. Hold the frame on her.
    #         His voice enters the frame without his face. This is the scene's
    #         refusal — Noelle is asking him to be the one who answers, and
    #         the camera refuses to offer her the comfort of looking at him
    #         while he does. She has to stay in her own frame.
    #         The signing beat: macro on the stylus tip touching the document
    #         pad. Macro on the signature resolving. Macro on the small
    #         haptic confirmation at the corner of the pad. Cut to wide —
    #         Noelle seated, the signed document floating as a holographic
    #         echo above the pad, Aeron standing a meter behind her, not
    #         touching her. Hold the wide for the final beat.
    # LIGHTING: Noelle's workspace. Three task lamps at full. The crystal's
    #           pale blue wash when the projection is active. When the
    #           signing happens: the ambient task-lamp light is dominant,
    #           the crystal is dimmed, the pad has its own small white
    #           light under Noelle's stylus. The pad light is the hottest
    #           small light in the frame at the moment of the signature.
    # SFX: Workspace ambient as established in a4_s03 — ozone smell you
    #      cannot hear, ventilation, the console's low standby tone, her
    #      keyboard. Her keyboard is active when Aeron enters and stops
    #      when she begins to explain. It does not resume at any point in
    #      the scene. Her hands have a different job tonight.
    #      One-shots: crystal activation (low chime), the counter-framework
    #      layer resolving (a second chime, steadier than a4_s03's), the
    #      stylus touch on the pad (a small mechanical click), the
    #      signature-confirm haptic (a single soft pulse, the kind you feel
    #      more than hear), the pad closing.
    #      No music bed until the moment of the signature. One sustained
    #      low chord beginning at the stylus-touch and continuing through
    #      the final wide. The chord does not resolve.
    # FACE: Noelle — this is the first scene in Act IV where Noelle's face
    #        does what it is going to do rather than what she has trained
    #        it to do. She is not composed in the Noelle way. She is
    #        composed in a way that is choosing to be composed against a
    #        pressure that is winning by the end. The pressure wins by
    #        inches. The winning is the scene.
    #        Aeron — receptive. He came here to receive. He is not here to
    #        solve and the scene is about whether he can hold the line of
    #        not-solving for the duration of what she is asking.
    # BLOCKING: Noelle at the console. Aeron enters and stops three steps
    #           in — not at the console, not at the doorway, in the
    #           middle of the room. He stands there for most of the scene
    #           because walking closer would be a gesture the scene does
    #           not want and walking back would be a gesture the scene
    #           cannot afford. He comes forward once, at the end, for the
    #           signing. He does not touch her. He stands a meter behind
    #           her left shoulder. She knows he is there. Neither of them
    #           acknowledges the proximity.

    # ========= VOICE BASELINE =========
    # EMP cadence. Noelle's voice is technical for the first half of the
    # scene — the framework presentation is pure instrument. The instrument
    # cracks twice, briefly, and she does not stop to patch either crack.
    # By the time she asks for permission, the instrument is gone and the
    # voice is plain. Aeron has fewer lines than usual. The scene wants
    # him quiet. The scene wants the quiet to be the answer he is giving.

    # scene bg_noelle_workspace_night with dissolve
    # play ambient "sfx/ambient/workspace_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE SUMMONS ==========

    "Noelle's message reaches Aeron at twenty-two-fifty on a small console in the war room where he has been reviewing Lyra's after-action for the Sector 7 interdiction for the fourth time. The message is two lines. Noelle's messages are always two lines or fewer."

    "'I have the counter-framework drafted. I would like you to come to the workspace. Alone, if possible.'"

    "He reads it twice. The second time because the word 'alone' is doing a thing in the sentence he wants to be sure of."

    athought "She has not asked me to come to the workspace alone since before the broadcast. She has been asking me to bring Selene. Shared command. Two in every room that matters."

    athought "She is not asking me to bring Selene tonight."

    athought "That is a piece of information before I have any other piece of information."

    "He sends one line back. 'On my way.'"

    "He walks the three corridors between the war room and Noelle's workspace. At this hour the base is in its second-shift rhythm — quiet, sparse, the care-system Tessa and Selene and the clinic medics run overnight. The weather of the base that Marcus's cell cannot read. He notices that he notices it. He is going to keep noticing it for as many scenes as it takes for the noticing to become habit."

    "He reaches the workspace door."

    "He does not knock. Noelle and he have had the no-knock understanding since a3 — Noelle's door is always available to him because the door is not Noelle, the door is a transition, and Noelle does not need to perform the transition. He opens the door."

    # ========== PHASE 2 — THE WORKSPACE ==========

    "The workspace is in its now-familiar configuration. Three task lamps. The console along the back wall. The crystal stand in the center. Noelle at the console, back to him, finishing a keystroke sequence — the way she always finishes keystroke sequences before she turns, the Noelle rule about not being interrupted in the middle of a line of code."

    "He stops three steps into the room."

    "He does not cross to the console."

    "He waits."

    "She finishes the sequence. She does not turn right away."

    n "Thank you for coming alone."

    "The voice is technical. The voice is Noelle-doing-intake."

    n "I want to be precise about why I asked that. This is not a decision I have taken to conceal from Selene. This is a decision I am going to brief Selene on at oh-seven-hundred tomorrow. I asked for you alone tonight because there is a conversation attached to the framework and the conversation is a two-person conversation and I could not figure out how to have it with three."

    "She turns."

    "She is in the workspace chair, not standing. Her hands are on her knees. Her hands are still, and he has learned in a4_s03 that still hands on Noelle are the tell, but the stillness tonight is a different kind of stillness. It is not the stillness of exhaustion. It is the stillness of a person who has been sitting at a desk for a long time preparing to say a sentence and is now at the moment of saying it."

    n "I drafted the counter-framework in the eleven hours after we located the analyst cell yesterday afternoon. I have been testing it against Marcus's historical signature data and against my own broadcast propagation model running in reverse. It works."

    n "I need to show it to you before we continue the conversation. It will not make sense in the abstract. The mechanism is the point."

    a "Show me."

    # ========== PHASE 3 — THE FRAMEWORK ==========

    "She stands. She walks to the crystal stand. She activates it."

    "The pale blue wash fills the room. The projection resolves above the stand — not the continental map this time. A dimensional lattice of decision nodes, each node a small labeled marker, the markers connected by time-weighted lines that show which decision-state feeds which next state and at what temporal lag."

    "It is the most abstract visual Noelle has ever shown him. It is also, he recognizes after two seconds of reading, a concrete object."

    athought "Each node is a person."

    athought "Not a unit. Not an operation. A person. She has labeled every node with a name."

    "The names resolve as he reads. Phoenix fighters. Phoenix medics. Phoenix analysts. The names he knows. The names he has been learning. Kesa Marin is not in the lattice — Noelle has removed the dead. Joren Hale is not in the lattice. Liora Rylan is not in the lattice. The lattice is the living."

    "The living, arranged as a graph of decisions they have not yet made."

    n "The framework is a predictive placement model. It takes as input: the twelve-to-thirty-six-hour adaptation window of Marcus's analyst cell, the known signatures of his field commanders, the historical pattern of Echelon counter-responses to Phoenix operations, and the personnel roster of the secondary base, Ghostline included."

    n "It produces as output: a placement recommendation for every Phoenix operational decision Phoenix is anticipating in the next six days. The recommendation is specific to the person. Fighter Three should be on the northern ridge for the Sector 12 supply run. Fighter Three should not be on the ridge for the Sector 14 cache extraction. The model knows the difference."

    n "The model knows the difference because the model is optimizing against Marcus's adaptation window. Every placement is selected to land outside the window Marcus has been reading from. Every placement is designed to be the one Marcus's analysts will not have seen coming because Marcus's analysts have been reading our historical outputs and my model's recommendations are selected to fall in the regions of the decision space our historical outputs have not explored."

    n "It stays ahead of the window."

    n "I have tested it. It stays ahead of the window with ninety-one percent confidence over a six-day horizon. Above ninety-four percent for the first three days. Degrades from there as Marcus's cell adapts to the adapted pattern, but by the time it degrades we will have generated new historical outputs that feed the next iteration of the model."

    n "It works, Aeron. It works the way I wanted it to work. It is the thing I was trying to build."

    "She stops."

    "She is looking at the lattice, not at him."

    n "It has one requirement."

    a "Tell me."

    n "The recommendations are not suggestions. The model works only if I am the one making the placements. Not Selene, not you, not Lyra as field commander — me. Because the model's optimization depends on the person running it being the same person who built the propagation data set the model is reading against. I am the variable. My judgment is the variable. If I hand you a list and you choose which recommendations to apply, you are introducing a secondary variable the model has not been trained on, and the confidence interval collapses inside twenty-four hours."

    n "The model requires me to be the one placing people."

    n "Specifically: me telling you, every twelve hours, which fighters go where. And you moving them there."

    # ========== PHASE 4 — THE COST ==========

    "A silence."

    "Aeron has not moved from his spot three steps into the room."

    athought "Placement. She is asking to do placement. Placement is what command does. Placement is what I do when I sit at the war table with Selene and we push markers around the tactical display and decide which fighter sleeps and which fighter walks out the door at oh-four-hundred."

    athought "Placement is how people die."

    athought "Not primarily. Not in the proximate sense — the proximate cause is always the Echelon bullet or the collapsing wall or the bad ground on the extract route. But in the ledger-sense, placement is the upstream cause, because placement is the decision about who is standing where when the bullet comes through."

    athought "She is asking to hold the ledger."

    "He waits. He does not speak yet. Noelle is not finished. Noelle's silences are load-bearing and he is not going to step on one."

    "She is still looking at the lattice."

    n "I have run the counterfactuals. At ninety-one percent confidence, the model saves an average of four Phoenix lives per six-day horizon relative to the decision framework you and Selene are currently running. That is the expected value. The variance on the expected value is high. In the best-case runs the model saves eleven. In the worst-case runs the model kills two who would have lived under your framework — because the model is wrong about Marcus's adaptation in the specific instance, because ninety-one percent is not one hundred percent, because I am also a variable and my variable has failure modes."

    n "The expected value is plus four."

    n "The two in the worst case are not abstract. They have names in my lattice. I have looked at the names. I know which names are in the worst-case zone. I am not going to tell you which names because the knowing is not useful to you, and the knowing is the thing I have to hold in my hands if I run the model."

    n "I will be the one telling you to put a specific fighter in a specific place on a specific night, and some of those placements will be the wrong placement, and some of those wrong placements will kill the fighter I placed. I will know the name before you do, because I will have written the name on the placement brief. I will know it in the frame and I will know it when the body comes back. The lag between knowing it in the frame and knowing it in the body is the thing I have been trying to prepare myself for for the last eleven hours and I do not know if I have prepared."

    n "I think I cannot prepare. I think the preparation is a category error the way my neutral-observer position was a category error."

    "Her voice cracks."

    "Not much. A quarter-inch of crack in a Noelle voice is an earthquake in any other voice and the scene holds the quarter-inch without trying to make it bigger."

    n "The name I cannot stop looking at in the worst-case zone is Lyra's."

    "A beat."

    n "Lyra is in the worst-case zone because Lyra is the field commander whose signature is most visible in our historical outputs — the ridge flank call from Sector 7 is the largest new data point in Marcus's cell's analytical window. The model wants to place Lyra where the ridge-flank instinct is load-bearing. The model is asking me to put Lyra somewhere in the next four days where her ridge-flank instinct is the entire point."

    n "If I am wrong about Marcus's next adaptation, the ridge-flank placement is the placement that kills her."

    n "I have looked at the name in the worst-case zone for two hours. I did not close the file on the name. I kept it open on a secondary display while I ran the rest of the tests. I wanted to know what it would be like to keep her name visible while I worked the model, because if I was going to be able to run the model at all, I had to be able to run it with her name in the room."

    "She looks at him now."

    n "I could run it with her name in the room."

    n "I am telling you that last sentence as a fact I do not want to have about myself, Aeron. I could run the model with Lyra's name in the worst-case zone because the model's math is larger than the name, and I am the kind of mind that can hold the math larger than the name, and I have been the kind of mind that can hold the math larger than the name since I was eleven years old and I found out that the math was the only thing in the room that did not lie to me."

    n "I did not choose to be that kind of mind. It is the shape I am. I used to think the shape was an asset. I am beginning to suspect the shape is a question I have been refusing to ask for twenty years."

    # ========== PHASE 5 — THE ASK ==========

    "Aeron does not speak."

    "He does not speak because she is not at the sentence yet. The sentence is still two beats out. He knows the geometry of Noelle's sentences by now and he is going to wait for the geometry to finish."

    "Noelle closes her eyes for exactly one second. Not more. Then opens them."

    n "Here is what I have to ask you."

    n "In a4_s03 I told you I am not a neutral observer anymore. I said it once, I asked you to witness it once, and you kept the question open. You said 'You are not a neutral observer anymore. I don't know what you are either. I am not going to pretend I do.'"

    n "I am asking you to stop pretending with me tonight. Not because the pretending was wrong. Because the pretending has an expiration date and the expiration date is a line on the lattice I am about to give you, and if I continue to hold the pretending through the expiration date I will be dishonest in a way that will make me dangerous."

    n "I am asking you for permission to stop being an analyst."

    n "The word for the thing I would become is strategist. It is a word I do not like. It is a word that has my father in it. My father was a strategist for the old empire's intelligence directorate and my father is the reason I do not use the word lightly. I spent my entire adolescence cataloguing the ways in which my father's strategic decisions had consequences that did not reach his desk, and I built my career on being the person who sees the consequences that do not reach the desk, and becoming the person at the desk is the exact betrayal of the eleven-year-old who decided to be an analyst in the first place."

    n "I am telling you that so you understand what I am giving up by asking."

    n "I am asking for permission because I cannot do this without you knowing what it costs me, and I cannot do this without you agreeing that the costing is worth the gaining, and I cannot do this alone because the thing I built in a3 that I call 'not alone' is the only part of my life in the last decade that has not ended in me sitting in a room at midnight with a finished model and no one to tell what the model said."

    n "You are the no-one-to-tell that I have. You and Selene. Tonight I am asking you."

    "A beat."

    n "Aeron. May I stop pretending to be a neutral observer and become a strategist. May I sign a document I wrote. May I put my name on a placement brief that places people. May I be the one who knows the name before you do."

    n "May I be the one who does this."

    # ========== PHASE 6 — THE WITNESS ==========

    "Aeron takes a breath he has been holding for two sentences."

    athought "She is asking me for absolution."

    athought "She is not asking for absolution. She is asking for permission. Those are two different things and I am going to be very careful about the difference."

    athought "Absolution would be me saying: it is okay, you will not be a monster, the math will hold, the names will be fewer, you are allowed to do this and the cost will not damage you."

    athought "I cannot say any of those sentences. Every one of those sentences is a lie. The math might not hold. The names might not be fewer. She might become a kind of person she does not want to be, and the becoming might not be reversible, and I cannot promise her the reversibility because I do not have the authority to promise the reversibility. Nobody does. Reversibility is not a thing a person can give another person about a decision of this size."

    athought "Permission is different."

    athought "Permission is me saying: I see you. I see the thing you are asking. I am not going to pretend I can give you absolution. I am also not going to refuse to be in the room while you decide. The refusal to absolve does not have to be a refusal to witness."

    athought "Witness is what she is asking for. Permission to be witnessed. The word 'permission' is a slightly wrong word for it — she does not actually need my permission to do anything, she is an adult and a Phoenix command-tier analyst and she could run the model tomorrow without my approval — but the ritual of asking is load-bearing for her, and I am going to honor the ritual by giving her the exact answer the ritual is designed to receive."

    "He speaks."

    "His voice is quiet and he does not move from his spot three steps into the room."

    a "Noelle."

    "She looks at him."

    a "I cannot give you absolution. You are not asking for it. I can tell this because if you were asking for it you would have asked me to tell you the costing was worth the gaining, and you did not ask me that. You asked me to be the one who knew what it cost you."

    a "I can be that."

    a "I am not going to tell you the model is right. I am not going to tell you Lyra will not be in the worst-case zone. I am not going to tell you that becoming a strategist will not cost you the eleven-year-old who decided to be an analyst. The eleven-year-old is going to lose something tonight. I cannot stop that from happening."

    a "What I can do is stay in the room."

    a "I am going to stay in the room while you sign. I am going to stay in the room on every placement brief for the next six days. I am going to read the names before you hand them to me and I am going to let you hand them to me, because the handing is part of what you are asking me to witness, and I am not going to reach around you to take the brief off the pad. The brief is yours. You sign it and hand it to me. I take it from your hand."

    a "That is the only shape of permission I have available."

    a "If that is not enough, tell me what is."

    "Noelle is quiet for a long moment."

    n "It is enough."

    n "It is enough and I am going to tell you, with the last of my analyst training before I put the analyst training down, that 'enough' is a precise word when I use it. I do not round 'enough' up or down. 'Enough' means the thing the sentence was asking for has been provided."

    n "You provided it."

    n "Thank you for being the no-one-to-tell."

    "A beat."

    n "I am going to sign now."

    # ========== PHASE 7 — THE SIGNING ==========

    "She turns to the console. She opens the document pad — the small haptic-input pad she has been using for draft acknowledgements since the beginning of her Phoenix tenure. The pad has never before carried a document Aeron has seen her sign."

    "Noelle does not sign documents in Aeron's presence. Noelle delivers briefings, reports, and analyses, and the delivery has always been in the form of projection and voice. The written artifact lives in Noelle's files and Selene's files and has never needed a handshake. The strategist framework is the first document Noelle is delivering that requires a signature — because placement briefs are command documents, and command documents in Phoenix are signed, and signing is the act that makes a piece of paper into a thing the Phoenix command structure treats as an order."

    "Aeron walks forward."

    "He walks the three additional steps to the console. He stops one meter behind her left shoulder. Not touching. Close enough to read the pad over her shoulder."

    "He reads the pad."

    "The pad shows the counter-framework document — a six-page technical specification condensed into a cover sheet and an attachment. The cover sheet has the framework name (the name is Noelle's internal working title, not a formal Phoenix designation — 'ADAPTIVE PLACEMENT MODEL v1'), the version number (v1), the date, and a signature field. The signature field is blank."

    "Noelle picks up the stylus."

    "Her hand is not shaking. Her hands have been still for the whole scene and they are still now."

    "She touches the stylus tip to the pad at the signature field."

    "The pad makes the small mechanical click — the contact confirmation. A small white light comes up under the stylus tip."

    "She writes her name."

    "The name resolves on the pad in her hand — the technical-regular hand she uses for official documents, not the looser hand she uses for personal notes. NOELLE VANCE. Two words. She does not write a middle initial. She has never used a middle initial in his presence and he does not know if she has one."

    "The signature resolves."

    "The pad pulses once — the soft haptic that confirms a signed command document has been committed to the Phoenix records."

    "Noelle does not lift the stylus immediately."

    "She holds the stylus against the pad for an extra second. It is not hesitation. It is a punctuation — the same small deliberate pause Tessa uses after writing the last letter of a name on the board. Noelle's pause is not a borrowing from Tessa because Noelle did not know about Tessa's pause when she developed her own, but the two pauses are the same shape and Aeron sees the shape and does not say anything about it."

    "She lifts the stylus."

    "She sets it in its groove."

    "The document pad closes itself with a small automated fold. The signed document goes into the Phoenix command records and also floats, for the next thirty seconds, as a small holographic echo above the pad — a Phoenix command convention, the echo-display for freshly signed documents that lets the signing room see what was signed for a brief confirmation window before the document moves fully into the records."

    "The echo hovers."

    "Noelle looks at it."

    n "That is the first document I have signed in front of you."

    a "I know."

    n "I want to say a thing about it before the echo fades."

    a "Go ahead."

    "Her voice is the plain-quiet voice she has used maybe twice in the conversation. It is the voice that is left when the instrument has been put down."

    n "When I was eleven I found my father's desk unlocked and I read three pages of a strategic assessment he had drafted on a population displacement project. The assessment contained a sentence I have remembered word-for-word ever since. The sentence was 'the projected civilian cost is within acceptable margins.'"

    n "I did not know at eleven what civilian cost meant. I learned over the next year. The year I learned was the year I decided I would be an analyst and never a strategist, because I wanted to be the one who wrote 'the projected civilian cost is within acceptable margins' in a way that forced the strategist at the next desk to read it and see the projected civilian cost as people rather than margins."

    n "I have just signed a document that, if it works, will write the sentence the other way. If my model runs for six days at ninety-one percent confidence, I will produce a report at the end of the six days that says 'the projected Phoenix cost was within acceptable margins, and the margin was four lives, and the lives were names, and I knew the names.'"

    n "I did not think I would be the person who wrote that sentence. I thought I had defended against being that person by choosing the analyst category at eleven. I was wrong. I was wrong because the category was not a defense; the category was a delay. I have been delaying this decision for twenty years and it has arrived anyway. The decision is always going to arrive for the people who have been working at this level for this long in this kind of war. The only question is whether you meet the decision as a person or as a category, and I cannot meet it as a category anymore because the category did not survive the broadcast."

    n "I am meeting it as a person."

    n "I am signing as a person. I am going to place people as a person. I am going to write the next sentence my father wrote on the other side of the desk from him, and I am going to write it with my name on it, and I am going to read my name on the sentence every time I sign a placement brief, and I am going to pay attention to what reading my name does to me, because the paying-attention is the only thing I have left from the eleven-year-old."

    n "The eleven-year-old is not gone. The eleven-year-old is the part of me that knows to pay attention. The strategist is the part of me that has to do the paying-attention inside a document that places people. Both exist. Both are me. I am going to let both exist and not resolve which one is more me, because the resolving would be another category mistake."

    "A beat."

    n "That is the thing about the signing I wanted to say before the echo faded."

    "The echo fades."

    "The signed document is in the Phoenix records. The pad is closed. The crystal is dimmed. The counter-framework lattice is still hovering above the stand, but the colors are cooler now, the projection running in its low-power maintenance mode."

    "Noelle does not turn around."

    "Aeron is still a meter behind her left shoulder."

    "Neither of them moves for a count of ten."

    # ========== PHASE 8 — THE CLOSE ==========

    "Eventually Noelle speaks. Her voice is the technical voice again — she has picked the instrument back up because the scene is over and the instrument is how she walks out of scenes."

    n "First placement brief at oh-six-hundred. I will have it on the pad when you come in for the shared-command briefing with Selene. I will brief Selene at oh-seven-hundred as I said I would. I will tell her I signed the framework tonight and I will tell her I signed it in your presence."

    n "I would like to tell her that you stayed in the room."

    a "Tell her that."

    n "Thank you."

    "She turns in the chair."

    "She looks up at him. Her eyes are clear. She is not crying and she has not been crying and the scene has not asked for crying — the scene has asked for something else, and the something else is finished now, and the face she has at the end of the scene is the face of a person who has just become something she did not intend to become and is choosing to carry the becoming with her eyes open."

    n "Go get sleep, Aeron. I still have the second phase of the locator work to do on Marcus's cell. I will be here for another three hours and then I will go to the cot in the annex. I will not run the first placement brief on no sleep. I need the sleep to be the kind of strategist I just agreed to be."

    a "Okay."

    "He does not say anything else."

    "He does not tell her he is proud of her, because 'proud' is the wrong instrument and she would reject it politely and both of them would feel the scene shift in a direction neither of them wanted. He does not tell her she did the right thing, because he does not know yet whether it is the right thing and lying to her about the not-knowing would be a violation of the witnessing she just asked him to do. He does not say 'I will see you at oh-six-hundred,' because the logistics are the instrument and the instrument has been put down for the scene and picking it back up would be small."

    "He puts his hand flat on the console, just for a second. Not on her hand. On the console. A meter from her. Present."

    "He takes his hand off."

    "He walks to the door."

    "At the door he stops. He does not look back. Looking back would be a gesture the scene does not want. He speaks without turning."

    a "Noelle."

    n "Yes."

    a "I saw you sign it."

    n "I know."

    a "I am going to carry that. You did not ask me to carry it. I am telling you I am going to, because the carrying is what the witnessing turns into after the room closes, and I want you to know the room does not close in my head the way it closes on the pad."

    n "Okay."

    n "Aeron."

    "He waits."

    n "If the model is wrong about Lyra, I am going to need you to come here and sit in this workspace with me while I write the brief that explains it. I cannot ask you for that in advance — I do not know how to ask for a thing I do not know will be needed. I am noting the possibility. You can decide whether to agree to it when it arrives."

    a "I will come."

    n "You did not have to say that so fast."

    a "I did."

    "A beat."

    n "Go."

    "He goes."

    "The door closes behind him."

    "The scene holds on Noelle at the console for four beats after the door closes. She looks at the space where the echo used to hover. Then she looks at the counter-framework lattice still running in its low-power maintenance mode. Then she looks at her own hands on her knees. Her hands are still. The stillness tonight is a different stillness than the a4_s03 stillness — the a4_s03 stillness was exhaustion and a category error. Tonight's stillness is the stillness of a person who has just done a thing and is letting her hands tell her what the thing was."

    "She says one sentence to the empty workspace. The sentence is not for Aeron and is not for Selene and is not for Marcus and is not for the model. The sentence is for the eleven-year-old at her father's desk."

    n "I am paying attention."

    "She turns back to the console."

    "She gets back to work."

    "Fade."

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("noelle_signed_framework", True)
    $ flag("noelle_role_strategist", True)
    $ canon_set("noelle.role", "strategist")
    $ canon_set("noelle.framework.adaptive_placement_v1.signed", True)
    $ canon_set("noelle.framework.confidence_6day", "0.91")
    $ canon_set("noelle.worst_case_zone_includes_lyra", True)
    $ rel_bump("Noelle", trust=3)
    $ npc_remember("Noelle", "signed_framework_in_aerons_presence", weight=3)
    $ npc_remember("Noelle", "named_eleven_year_old_at_fathers_desk", tone="origin_revealed")
    $ npc_remember("Noelle", "kept_lyras_name_visible_while_testing", tone="chosen_discipline")
    $ npc_remember("Aeron", "witnessed_noelle_sign_no_absolution", tone="permission_without_absolution")
    $ npc_remember("Aeron", "put_hand_on_console_not_on_noelle", tone="present_not_touching")
    $ tp_seed("a4.noelle.signs")
    $ tp_seed("a4.noelle.pay_attention")
    $ tp_seed("a4.lyra.worst_case_zone")
    $ metric("noelle_framework_confidence", 91)
    $ nudge_poly("witness", "held")
    $ scene_mark(_current_scene_id, "exited")
    call li_lore_check("Noelle") from _a4_s09_lore
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s09_noelle_implicated_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Twenty-two-fifty on the same day as a4_s03, a4_s05, a4_s06,
#     a4_s07, a4_s08. The long day that refuses to end. Noelle has
#     had eleven hours with the located analyst cell to draft her
#     counter-framework. Aeron gets her message while reviewing the
#     Lyra Sector 7 after-action for the fourth time.
# cann.what_happened:
#   - Noelle summons Aeron to her workspace ALONE — deliberately not
#     with Selene. The alone-ness is the first signal. Noelle has not
#     asked Aeron to come alone since before the broadcast.
#   - Noelle presents ADAPTIVE PLACEMENT MODEL v1. A predictive
#     framework that takes as input Marcus's 12-36 hour adaptation
#     window, Echelon field signatures, historical counter-response
#     patterns, and the Phoenix personnel roster, and produces
#     placement recommendations designed to stay outside the window
#     Marcus's cell is reading from. Confidence: 91% over six-day
#     horizon, 94%+ for first three days.
#   - The framework's lattice is a graph of Phoenix living personnel,
#     each a labeled node. Noelle has removed the dead from the
#     lattice — Kesa Marin, Joren Hale, Liora Rylan are not in the
#     visualization. The lattice is the living.
#   - The framework has a fatal requirement: Noelle must be the one
#     making the placements. Not Selene, not Aeron — Noelle. Her
#     judgment is the variable the model is optimizing against. If
#     Aeron filters the recommendations, the confidence interval
#     collapses inside 24 hours.
#   - Noelle has run counterfactuals: expected value is +4 Phoenix
#     lives per six-day horizon relative to current framework. Best
#     case +11. Worst case -2 — two Phoenix who would have lived
#     under Aeron's framework die under hers because the model is
#     wrong in a specific instance.
#   - Noelle reveals Lyra is in the worst-case zone. Lyra's ridge-
#     flank signature from Sector 7 is the largest new data point in
#     Marcus's cell's analytical window and the model wants to place
#     Lyra where that instinct is load-bearing. If the model is wrong
#     about Marcus's next adaptation, the ridge-flank placement
#     kills Lyra.
#   - Noelle kept Lyra's name open on a secondary display for two
#     hours while running the rest of the tests. She wanted to know
#     what it would be like to run the model with Lyra's name visible.
#     She could do it. She is telling Aeron this as a fact she does
#     not want to have about herself.
#   - Noelle names her origin: at eleven, she found her father's
#     unlocked desk and read "the projected civilian cost is within
#     acceptable margins." Her father was a strategist for the old
#     empire's intelligence directorate. Her choice to be an analyst
#     was a twenty-year delay, not a defense. The category did not
#     survive the broadcast.
#   - Noelle asks Aeron for permission to stop pretending to be an
#     analyst and become a strategist. She is explicit that she is
#     not asking for absolution — absolution would require Aeron to
#     say the costing was worth the gaining, and she did not ask that.
#     She is asking to be witnessed.
#   - Aeron does not move from three steps into the room until the
#     signing. He gives her permission without absolution: he will
#     stay in the room, he will read names before she hands them to
#     him, he will not reach around her to take briefs off the pad.
#     That is the only shape of permission he has available. Noelle
#     says "It is enough."
#   - Aeron walks forward. Stops one meter behind Noelle's left
#     shoulder. Does not touch her. Noelle signs ADAPTIVE PLACEMENT
#     MODEL v1 on the document pad. Her signature: NOELLE VANCE, two
#     words, technical-regular hand. The pad pulses the soft haptic
#     confirmation. The holographic echo of the signed document
#     hovers for thirty seconds.
#   - During the echo, Noelle says the eleven-year-old speech —
#     naming her father, the sentence, the delay, the arrival of the
#     decision. She is going to meet the decision as a person, not
#     as a category. She is going to let both the eleven-year-old
#     and the strategist exist and not resolve which is more her.
#   - Noelle asks Aeron to tell Selene that Aeron stayed in the room
#     during the signing. Aeron agrees.
#   - Aeron puts his hand flat on the console for a second, a meter
#     from Noelle, present but not touching. Walks to the door.
#     Without turning, tells Noelle he saw her sign it and is going
#     to carry that. Noelle asks — for a future contingency, not now
#     — that if the model is wrong about Lyra, Aeron come back to
#     the workspace and sit with her while she writes the brief
#     explaining it. Aeron agrees immediately.
#   - Scene ends on Noelle alone after the door closes, saying to
#     the empty workspace: "I am paying attention." The sentence is
#     for the eleven-year-old at her father's desk. Then she gets
#     back to work on the analyst-cell locator.
# cann.aeron_state:
#   - Receives Noelle's ask as permission-without-absolution and
#     finds the grammar of witnessing that the scene requires. He
#     refuses to lie to her in any of the directions she might want
#     to be lied to. He stays in the room. He reads the pad. He
#     does not touch her. He puts his hand on the console a meter
#     from her instead. The hand on the console echoes Tessa's flat
#     palm on the board (a4_s06) and Zira's hand on the drawer
#     (a4_s08) — a third instance in Act IV of the same private
#     gesture. He is building a vocabulary of presence without
#     touch that he did not plan and did not name.
#   - Agrees in advance to come back if the worst case arrives. The
#     too-fast answer is the character moment — he refused to make
#     Noelle wait for a thing she needed to know she could ask for.
# cann.noelle_state:
#   - Becomes a strategist on-screen. The a4_s03 implication escalates
#     into an operational commitment. Her role is now canon_set to
#     "strategist." First signed document Aeron has seen from her.
#   - Names her origin story for the first time: the eleven-year-old
#     at her father's desk, the sentence about acceptable margins,
#     the twenty-year delay framed as category defense. Reveals the
#     analyst-not-strategist choice as a deferral rather than a
#     refusal.
#   - Keeps Lyra's name visible in the worst-case zone as a chosen
#     discipline. Demonstrates the shape of mind the strategist role
#     requires and does not pretend she is not already the shape.
#   - "I am paying attention" — her post-door private sentence. The
#     eleven-year-old's rule, repurposed for the strategist. Paying
#     attention is the thread the eleven-year-old gives the
#     strategist so the strategist does not become the father.
# cann.path_tracking: EMP
# cann.thematic_flags:
#   - Permission without absolution. The Act IV grammar for command-
#     accountable relationships. Aeron's a4_s03 line "the question
#     stays open" is now operationalized: the open question requires
#     Aeron to stay in the room during the costs, not to resolve the
#     question by naming it good.
#   - Category collapse. Noelle's analyst/strategist dichotomy was a
#     false defense. The war is making her name the thing she has
#     been. The naming does not destroy the eleven-year-old; the
#     naming is what lets the eleven-year-old keep her job
#     (paying attention).
#   - The worst-case name visible. Running the model with Lyra's
#     name open on a secondary display is the character discipline
#     of a strategist who refuses to let the math abstract the name.
#     This is the Noelle version of Aeron's a4_s05 "hand that did
#     not touch the relay."
#   - The private gesture vocabulary: hand on board (Tessa), hand on
#     drawer (Zira), hand on console (Aeron for Noelle). All three
#     gestures are presence-without-touch and all three happen in
#     the same chapter of Act IV. Aeron is the connecting figure.
#     He is not inventing the vocabulary; he is learning it from
#     the women and then extending it back to them. The vocabulary
#     is the shape of shared authority when shared authority is
#     real.
#   - The ledger of Act IV women's sentences: Tessa's "the rule is
#     for the living," Selene's "necessary is not worth it," Noelle's
#     "on whose record," Lyra's Band unbuckled, Zira's "I needed to
#     know the door existed," Noelle's "I am paying attention." Aeron
#     is keeping the ledger in the part of his head Marcus cannot
#     read. The ledger is the care weather system that is unreadable
#     from the Echelon side.
# cann.character_moments:
#   - Noelle: the quarter-inch voice crack at "The name I cannot stop
#     looking at in the worst-case zone is Lyra's." The eleven-year-
#     old father's-desk speech. The stylus-touch pause at the signature
#     (structurally matched to Tessa's pen-pause on the board). The
#     technical-regular hand, no middle initial. "I am paying
#     attention" to the empty workspace.
#   - Aeron: three steps into the room and not advancing. Refusing
#     absolution. Naming witnessing as the only shape of permission
#     he has. The hand on the console a meter from her. The door-
#     threshold speech without turning. "I will come" (too fast, on
#     purpose). Reading the pad over her shoulder without touching her.
# cann.callbacks:
#   - a4_s03_marcus_adapts_emp: "I am not a neutral observer anymore"
#     is the sentence this scene escalates. Noelle's asking Aeron to
#     "stop pretending with me tonight" is the direct sequel move.
#     Aeron's a4_s03 line "the question stays open" is operationalized
#     here as permission-without-absolution.
#   - a4_s05_delegation_test_emp: "necessary is not worth it" is
#     running in Aeron's head during Noelle's ask. The scene
#     structurally mirrors a4_s05 — Aeron again receiving a cost he
#     cannot refuse without refusing the whole shape of shared
#     command, and again keeping the names rather than the math.
#   - a4_s06_tessa_counts_different_emp: the pen-pause on the last
#     letter of a name on the board is the structural twin of
#     Noelle's stylus-pause at the signature. Scene notes the twin
#     explicitly from Aeron's POV.
#   - a4_s08_zira_exit_plan_emp: the hand-on-drawer/hand-on-console
#     parallel. Both scenes build the Act IV presence-without-touch
#     vocabulary. Aeron carries the a4_s08 gesture into a4_s09 without
#     planning to.
#   - a3_int_noelle_unmeasurable_emp: the category error Noelle
#     committed alone. This scene is the category error's second half
#     — she is no longer committing it alone, and the category is no
#     longer a category she can live inside.
#   - Noelle's father as strategist for the old empire's intelligence
#     directorate — backstory plant. Her father has not been named
#     directly in Phoenix canon before this scene. Future Noelle beats
#     can develop or leave this.
# cann.block_status: drafted
# cann.requires_followup:
#   - ADAPTIVE PLACEMENT MODEL v1 is now running. The first placement
#     brief arrives at oh-six-hundred the next day. Any Act IV scene
#     that involves Phoenix field operations inside the next six days
#     must treat the placements as coming from Noelle's brief, not
#     from Aeron/Selene's direct order.
#   - Lyra in the worst-case zone is a live plot plant. The model
#     wants to place Lyra on a ridge-flank assignment in the next four
#     days. If the model is wrong, Lyra dies. This is the primary
#     tension hook for the rest of Chapter I. The author may:
#       (1) run the placement, model is correct, Lyra survives;
#       (2) run the placement, model is wrong, Lyra dies (and
#           Noelle writes the brief with Aeron in the room);
#       (3) run the placement, model is wrong, Lyra is gravely
#           injured but lives; or
#       (4) Aeron/Selene override Noelle's specific Lyra placement
#           against her advice, which collapses the model's
#           confidence interval and breaks the framework.
#     All four are live. The tp_seed a4.lyra.worst_case_zone flags
#     the decision.
#   - Noelle's contingency ask — Aeron sitting with her while she
#     writes the wrong-about-Lyra brief — is a scene seed that
#     either fires or does not fire in the next four days. If it
#     does not fire, the non-firing is also canon-significant: it
#     means Lyra survived the placement and the contingency is
#     released.
#   - Noelle's role as strategist now canon-set. Any later scene
#     that shows her running pure analysis must be read as her
#     carrying both the eleven-year-old and the strategist
#     simultaneously, not as a return to the prior role.
#   - Her father's backstory (old empire intelligence directorate
#     strategist, the unlocked desk, the acceptable-margins sentence)
#     is now planted. Future development optional.
#   - "I am paying attention" is a new Noelle self-address. It may
#     become a recurring private sentence for her the way Tessa's
#     rule of three is a recurring Tessa practice. tp_seed
#     a4.noelle.pay_attention flags the possibility.
#   - The hand-on-console gesture is Aeron's third presence-without-
#     touch in Act IV. The vocabulary is now tracked. Any later
#     shared-authority scene that requires the gesture should use it
#     rather than inventing a new one.
