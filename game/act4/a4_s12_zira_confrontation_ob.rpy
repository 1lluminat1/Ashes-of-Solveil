# =======================================================
# ACT 4 - Scene 12: Zira Confrontation (Obedience Path)
# File: a4_s12_zira_confrontation_ob.rpy
# Path: OB
# Type: ZIRA STATE BEAT / CRISIS (NON-EROTIC -- PRE-EROTIC SETUP)
# Character Focus: Zira, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s12_zira_confrontation_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s12_zira_confrontation_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked for the setup, then handheld with restrained drift
    #         (4-5%, less than a3_s15) when Zira begins speaking. The drift is
    #         Zira's but she is holding it in. She is deliberately not throwing
    #         anything tonight. That restraint IS the scene. Opens on the corridor
    #         between the ops table and the mess -- a wider section where two
    #         people can stand without blocking traffic. Tightens to a two-shot
    #         when Zira steps into his path. Close-ups are reserved: Zira's jaw,
    #         Zira's hands (steady, unnaturally so -- she is making them stay),
    #         Aeron's eyes when the word "terms" lands. Final shot: Zira walking
    #         past him. The camera stays on Aeron's back. The corridor around him.
    #         We do not follow her. We watch him absorb what she deposited.
    # LIGHTING: Corridor overhead strips at 60% (morning operational, brighter than
    #           a3_s20's "unflattering" corridor). The light is functional. Neither
    #           of them is trying to look good. Both of them are awake, having not
    #           slept well, and the light shows it. No warm practicals. No accent.
    # SFX: Loop -- corridor ambient: HVAC, distant ops chatter (voices indistinct),
    #      boot traffic at the far end of the corridor, a comm click every 40 seconds
    #      from some unseen station. One-shots -- Zira's boots stopping (two paces,
    #      planted), Aeron's boots stopping (one pace, clean), the scrape of a mug
    #      somewhere distant that does not relate to the scene but reminds the room
    #      it is morning and the base is working. No thrown object tonight. The
    #      absence of a thrown object is load-bearing.
    # FX/COMP: Zira is carrying a datapad. She does not use it. She is carrying it
    #          because she had to bring a reason to be in this part of the corridor.
    #          The datapad is the prop that justifies her presence. Aeron is
    #          carrying nothing. He has just come from the ops table. His hands
    #          are empty. That asymmetry matters: she brought a reason, he did not.
    # BLOCKING: Aeron walks the corridor from ops toward the mess. Zira steps out
    #           of a side alcove -- she has been waiting in the alcove for the
    #           sound of his footfall. She steps into his path. He stops. They
    #           face each other in the middle of the corridor. Neither leans.
    #           Neither sits. The conversation happens on their feet. At the end
    #           she walks past him in the direction he was headed. She goes to
    #           the mess. He does not follow. He stands in the corridor.
    # CANON: ZIRA CRISIS / TERMS DEPOSITED. This is the scene where Zira converts
    #        the private realization of a4_s05 ("I cannot leave") into a PUBLIC,
    #        ACTIVE demand. She is not leaving. Therefore she is claiming the
    #        ground she is staying on. The terms: presence at decisions, argument
    #        when argument is needed, acknowledgment that she is a person rather
    #        than a body Aeron reaches for between ceremonies. Ritual is what she
    #        cannot compete with, so she is demanding terms on the thing ritual
    #        cannot hold -- the daily command work, the arguments, the silences.
    #        She does not ask him to stop going to Nyra. She does not ask him to
    #        share everything. She asks him to make her feel like she is not
    #        nothing. Callbacks: a4_s05 (I cannot leave), a3_s15 (I chose you first),
    #        a3_s20 (you don't get to break), a4_s09 (Sector 12 strike -- civilians).
    # FACE: Zira -- angrier than a4_s05 and colder than a3_s15. She is not crying.
    #        She is not shaking. She is doing the opposite: she has locked her body
    #        still on purpose because she has learned that throwing things does not
    #        work anymore with THIS version of Aeron.
    #        Aeron -- Marcus-idiom competent. He listens. He calculates what he can
    #        give. What he cannot give, he does not promise. The fracture under the
    #        mask is not in his voice. It is in the fact that he is willing to be
    #        stopped in a corridor at all.
    # CONSENT / FRAME: No player choice in this scene. The demand IS the scene.
    #        The player choices live in the next scene (a4_s13) where Aeron has to
    #        answer in the body what he cannot answer in words here.

    # ========= VOICE BASELINE =========
    # OB Aeron (Phase I late): Clinical. Short sentences. Marcus idiom deepened.
    #         He uses "noted" and "acknowledged" the way he used to use "okay."
    #         Internal voice: drier, sparer. The athoughts that survive are the ones
    #         that cost him to suppress.
    # Zira (a4 mid-Phase I): Anger still street-cadenced, but compressed. She is
    #         rationing her contractions. She is not using her tactical jargon --
    #         she is stripping to the personal, but from a colder platform. Where
    #         a3_s15 was rage-vulnerable, this is demand-vulnerable. She has moved
    #         from confrontation to claim.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - OPS CORRIDOR (MESS WING) - MORNING]
    # 0712. Base on normal-shift daylight cycle. Operational light.
    # The corridor is a connector: ops table behind him, mess ahead, side alcoves
    # for storage and equipment lockers.

    #scene bg_ops_corridor_morning_ob with dissolve
    #play ambient "sfx/ambient/corridor_morning_ops.ogg" fadein 2.0

    # ========== PHASE 1 -- THE INTERCEPT ==========

    athought "0712. The ops table cleared at 0705. Noelle's doctrine draft is queued for revision at 1100. The Sector 12 metrics from yesterday are logged in the morning report. Three civilians. I signed the box."

    athought "I signed the box at 0638 yesterday morning. I have not thought about it since in any way I would call thinking. The box is closed. The metric is logged."

    athought "I am walking to the mess to drink something I will not taste and return to the table at 0800."

    athought "The corridor is louder this morning than it was yesterday. The base is pretending yesterday didn't happen. I am also pretending."

    "Aeron walks the corridor. Boots on grate. He passes two techs going the other way. Neither acknowledges him. He prefers it that way this week."

    "A side alcove at the corridor bend -- an equipment storage recess big enough for one person standing. Zira steps out of it."

    "She does not speak. She steps into his path. Two paces ahead of him. She stops. Her boots plant."

    #play sound "sfx/one_shot/boots_plant_two.ogg"

    "He stops one pace short of her. The distance is deliberate. Close enough to hear a low voice. Not close enough to touch."

    athought "She was waiting."

    athought "She has a datapad in her left hand. She is not using it. She brought it so the corridor would have a reason for her to be in it."

    athought "That is Zira when she is about to do something that costs her."

    a "Zira."

    z "Don't."

    z "Not 'Zira' like I'm a line item on your morning report. Stand there for a minute."

    "He stands."

    athought "Her hands are not shaking."

    athought "That is the first abnormality. The second is that she is not yelling. The third is that she is looking at my eyes and not through them."

    athought "Zira looks through me when she is angry and at me when she is afraid. Right now she is doing the wrong one for the situation. That means I am reading the situation wrong."

    # ========== PHASE 2 -- THE OPENING ==========

    z "You went to her last night."

    "The statement is flat. No question mark. No inflection that would let him answer it like a question."

    athought "She knows."

    athought "Of course she knows. She runs comms. She runs door telemetry as a side routine. She probably knew before my boot hit the second corridor turn."

    a "I did."

    z "I'm not asking you to confirm it. I'm telling you I know it. That's different."

    z "I did not come to stop you from going. I had all night to do that and I didn't. I came to stop something else."

    a "What."

    z "Give me a second."

    "She takes the second. Her jaw works once. Her hand -- the one not holding the datapad -- opens and closes. She is making herself slow down."

    athought "She is rationing. She does not usually ration. Ration-mode Zira is a more frightening operator than throw-mode Zira. I did not learn this quickly enough."

    z "I am not going to let you pretend I am a tool in your pocket."

    z "Either I am in this with you -- all of it, including what happened in Sector 12 yesterday -- or I am not."

    z "Nyra can have the ritual. I am not fighting about the ritual. I do not know what she does in that room and I am not asking. That is not a concession. That is a category."

    z "I will not have the silence."

    a "The silence."

    z "The signing at 0638. The metric at 0805. The way you came out of the ops room yesterday at 0812 and did not speak to me or to anyone with a face until 1400 because you were running numbers in your head that I should have been in the room with you running."

    z "That silence."

    # ========== PHASE 3 -- THE TERMS ==========

    athought "She said silence like it was a weapon she had been shot with."

    athought "The tremor is trying to come up in my left hand. I have been in this corridor for forty seconds and the tremor is trying to come up. Last night in Nyra's quarters it did not come up for two hours."

    athought "I flatten my hand against my thigh. The tremor sinks."

    a "Say what you want."

    z "I want terms."

    "A beat."

    z "Not concessions. Not promises. Terms. Three of them. I've had since 0300 to get them down to three, so listen."

    z "One. I am at the table when the decisions are made. Not in the next room. Not on comms from signal bay. At the table with a chair that has my name on it, not a chair I borrowed from the wall."

    z "I am already there. Informally. I am telling you I am not accepting informally anymore."

    z "Two. When an argument is needed, I am the one who makes it. I am not going to shut up so the room stays smooth. Noelle will tell you the room should stay smooth. Noelle is wrong. I will be the one who says so out loud when she is."

    z "Three."

    "She stops. She takes a breath. The breath is the tell -- the first uncontrolled intake of the morning."

    z "I will not be a body you reach for between ceremonies."

    z "I don't care what kind of ceremony it is. Nyra's rite, your own head, a briefing you didn't enjoy, a metric you signed. I am not the thing you come to when the ritual drops you off."

    z "If I am with you, I am with you in rooms, not in recoveries."

    athought "The three things she has asked for are the three things I have been giving her less of since Selene died. She has been keeping a ledger."

    athought "She did not come to the corridor with a datapad because she needed a reason. She came with a datapad because she wanted her hands to be holding something other than my shoulders."

    # ========== PHASE 4 -- HIS ANSWER ==========

    "He considers her. Twelve seconds of considering. The corridor HVAC cycles twice in that span. She waits. She does not fill the silence. She has learned -- from him -- how to hold a silence and wait for a decision to finish cooking."

    a "One. Granted. You have a chair at the tactical table. Formally. I will tell the ops staff at 0800. It is not a gesture. It is a structural change."

    a "Two. Granted. You will be the voice that breaks the smoothness. I will not shut you down. I may disagree with you. I will not silence you. There is a difference between those two things and I will keep track of the difference."

    "He stops. Zira waits. She does not lean forward. She does not exhale. She waits for him to say three."

    "He does not say three."

    athought "I cannot grant three the way she asked for it. The truth under three is that I will go to Nyra again. The truth under three is that I do reach between ceremonies, and that the reach is the thing that keeps the static down, and that I do not yet have another mechanism for the static."

    athought "I can give her half of three. The half she can live on. The half that is not a lie."

    a "Three. I will not promise to stop going to her."

    a "I will not promise to tell you everything."

    a "What I will promise. When you are the one I reach for, the reach will not be between. It will be at. You will not be the aftercare station for a rite. If I come to you, it will be because I am coming to you."

    a "That is the half I can give you. It is not the whole half. If you take it I will not pretend it is more than it is."

    # ========== PHASE 5 -- THE LANDING ==========

    "Zira does not move for three seconds."

    "Then she adjusts the datapad in her left hand -- a tiny repositioning, the kind of motion a person makes when she is making herself present in her own body. Her grip on the datapad is white at the knuckles. He sees it. She knows he sees it. She does not adjust her grip to hide it."

    z "That is less than I asked for."

    a "It is."

    z "It is more than I expected you to give me."

    a "It is."

    z "Did you rehearse it."

    a "I didn't know you would ask. I rehearsed it two weeks ago in case someone asked. You are the someone."

    athought "That is the most honest sentence I have produced in this corridor."

    "She absorbs it. A small bitter something at the corner of her mouth that is almost a smile and is not a smile."

    z "Fine."

    z "I take the half. I am logging it. If the half becomes a quarter I will not come to this corridor again. I will come to a different corridor and I will have a different conversation and neither of us will like it."

    a "Understood."

    z "Do not say understood. Say you heard me."

    a "I heard you."

    z "Better."

    "She shifts her weight. She is about to walk past him. She has one more thing to say and she is putting it at the end on purpose."

    z "I am not asking you to be mine."

    z "I am asking you not to make me feel like I am nothing."

    "The corridor ventilation cycles. Two techs pass at the far end. Neither looks at them."

    a "You are not nothing."

    z "Make me feel it, then."

    "She walks past him."

    "Her shoulder almost brushes his. It does not. The almost is the point. She is telling him -- in the body rather than the mouth -- that the demand lives on the skin and not only in the words. The body is where the answer has to come from. That is a message for tonight, not this morning."

    "She passes him. The datapad in her left hand. Her boots clean on the grating. She does not look back."

    # ========== PHASE 6 -- THE CORRIDOR AFTER ==========

    # VISUAL: Camera holds on Aeron's back. He does not turn to watch her go. He
    # stays facing the direction he was walking. The corridor around him is ordinary.
    # The techs at the far end have passed through. The HVAC cycles. The comm click
    # from the unseen station pulses once.
    # CAMERA: Slow push in on his shoulders. His left hand, hanging at his side.
    # The fingers contract once, slowly, and release. Not a tremor. A choice.

    athought "She is behind me now. I do not turn. I do not watch her go."

    athought "My left hand is steady. The flatten-against-the-thigh maneuver worked. The tremor did not come up."

    athought "That is not the achievement I am cataloging."

    athought "The achievement I am cataloging is that she walked past me without touching me. Six months ago she would have touched me. Three months ago she would have touched me and regretted it by 0900. Today she chose not to and regretted nothing."

    athought "That is the cost of two promises I did not make her."

    athought "She will come to me tonight, or I will come to her tonight. One of the two is going to happen. She is not asking me to decide which."

    athought "She deposited the demand. I am holding it now. I cannot carry it through the morning as a memory. She would not have wanted me to. She wanted me to carry it as a temperature in the body. That is the Zira version of Nyra's rite and I do not know how to tell whether the parallel is ironic or structural."

    athought "I think it is structural. I think three women are teaching me three different versions of how obedience gets written into the flesh, and I am not resisting any of the three of them because I no longer know what resistance would look like that does not cost the base a tactical outcome."

    athought "The Marcus idiom would call that a constrained optimization. Marcus would also say that the man running the optimization stopped being the man who objected to being the one running it approximately two weeks ago, and that the objection is a cost, and that the cost has been booked."

    athought "I book the cost. I walk the corridor."

    "He walks. The mess is at the far end. He does not go to it. He turns left at the next intersection and returns toward ops. He will get coffee from the ops pot instead. The taste is the same taste. The location saves him nine minutes and spares him the possibility of seeing Zira in the mess, where she would ignore him across the room and that ignoring would be the thing that finished him for the day."

    athought "I route around her. I would have routed around her a week ago too. The routing is not new."

    athought "What is new is that she routed me on purpose this time. She chose the corridor where I could not route around her until after the conversation. That is command-level movement from someone who has stopped being my subordinate in any way that matters."

    athought "She has promoted herself. I am the last person in the base to acknowledge the promotion. The acknowledgment is what she came to the corridor to extract."

    athought "I gave it to her. I will be giving it to her again tonight in a different form."

    # ========== PHASE 7 -- ZIRA IN THE MESS (BRIEF) ==========

    # VISUAL: Cut to the mess. Brief. 12-15 seconds of screen time. Zira at a corner
    # table, one mug, the datapad flat beside the mug (still unused). She is not
    # reading it. She is staring at the far wall -- the kind of stare that means
    # she is going through the conversation she just had in the corridor in a loop,
    # editing what she wishes she had said, noticing she wouldn't actually change
    # any of it. The mess is half-full at 0720. Techs. A medic. Two sentries off
    # night shift. Nobody sits with her. Nobody sits with her is what nobody has
    # done for weeks now. She prefers it that way. The preference is also a cost.

    #scene bg_mess_morning_ob with dissolve

    "The mess. Corner table. Zira alone. A mug of something black. The datapad she never opened."

    "She is not reading. She is not eating. She is replaying."

    zthought "I asked for three things. He gave me two and a half. The half he gave me is the hardest half to live with and the hardest half to respect and I respect it."

    zthought "That is the trap. I came to the corridor expecting to either get what I wanted or find the wall I could climb out on. He gave me the middle thing. The middle thing is the thing that keeps me in this."

    zthought "I told him I am not sharing command and I am not sharing him. At s15 I told him that. I have not unwritten that sentence. Today I added terms to it. Terms are what you add when the sharing has become a fact and you are deciding what you will and will not be shared out of."

    zthought "I am deciding what I will and will not be shared out of."

    zthought "The one he will not share me out of is the daily. The mornings, the arguments, the silences. I will take the daily. Nyra can have the ritual. The ritual does not touch the daily unless he lets it, and if he lets it, that is when I come to a different corridor."

    zthought "This is the scariest math I have ever done because I am doing it about whether to stay somewhere I already cannot leave."

    zthought "I cannot leave. That was s05. I have said it to myself in the dark. I am not repeating it in the corridor where he can see it."

    zthought "Tonight he will come to me. Or I will come to him. I have not decided yet. The decision is in the body. I will know which when my boots turn."

    zthought "I did not touch him this morning. That was on purpose. I need him to come to me with the weight of the not-touching still on him, because if he comes to me without that weight, the night is a transaction and I said in the corridor that I will not be a body he reaches for and I meant it."

    zthought "I meant it when I said it at 0714 and I mean it now at 0721 and I will still mean it at 2200 and I will still mean it at 2201 when I hear his boots at my workshop door."

    zthought "Will I still mean it at 2210 when the door opens."

    zthought "I will mean it. I will also want him. Those are not the same sentence. I am learning to hold them as two sentences."

    zthought "The pressed flower is still in the drawer under the bench. I have not looked at it this week. I will not look at it tonight. I will keep it in the drawer. It is mine. It was mine before him. It will be mine after him if there is an after."

    zthought "Something from before. I get to have something from before. He does not get to know what it is."

    "She lifts the mug. Drinks. The coffee is ordinary and terrible. She drinks it anyway."

    "She does not look at the datapad. She does not open it. At 0730 she will stand and go to signal bay and run Ghostline telemetry for two hours and nobody in the bay will know she had this morning because she is not going to tell anyone and she is not going to show it on her face."

    "The morning continues around her."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("zira_terms_deposited", True)
    $ rel_bump("Zira", conflict=2)
    $ rel_bump("Zira", respect=1)
    $ canon_set("ob.zira.terms_deposited", True)
    $ canon_set("ob.zira.chair_at_table_formal", True)
    $ canon_set("ob.zira.will_break_smoothness", True)
    $ canon_set("ob.zira.half_of_three", True)
    $ tp_seed("a4.ob.zira.make_me_feel_it")
    $ npc_remember("Zira", "deposited_terms_half_of_three", tone="cold_claim")
    $ npc_remember("Zira", "did_not_touch_him_on_purpose", tone="held_in_reserve")
    $ npc_remember("Aeron", "rehearsed_the_half_answer_two_weeks_ago", tone="booked_cost")
    $ metric("zira_patience", adjust=-1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s12_zira_confrontation_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after a4_s11 (Nyra's second oath). 0712 -- 0721 base time.
#   - One day after a4_s09 (Sector 12 strike, three civilians killed with Aeron's
#     approval) and a4_s10 (Noelle's blank authorization for targeting doctrine).
#   - Direct sequel to a4_s05 (Zira realizes she cannot leave -- she converts
#     that realization into an active demand here).
# cann.what_happened:
#   - Zira intercepts Aeron in the corridor between ops and the mess. She has
#     waited in a side alcove. She brought a datapad as her "reason" to be there.
#   - She confirms she knows he went to Nyra last night. She does not ask him to
#     stop. She says "Nyra can have the ritual. I will not have the silence."
#   - She lays out three terms: (1) formal seat at the tactical table, (2) she
#     will be the voice that breaks the smoothness in command decisions, (3) she
#     will not be a body Aeron reaches for between ceremonies.
#   - Aeron grants #1 (structural change -- he will tell ops staff at 0800).
#     Aeron grants #2 (he will not silence her). Aeron can only grant HALF of #3:
#     he will not promise to stop going to Nyra, will not promise to tell her
#     everything, but promises that when he comes to Zira it will be AT her, not
#     between ceremonies. The "half answer" was rehearsed two weeks ago in case.
#   - Zira takes the half. She logs it. She deposits the final line: "I am not
#     asking you to be mine. I am asking you not to make me feel like I am nothing."
#     Aeron: "You are not nothing." Zira: "Make me feel it, then."
#   - She walks past him without touching him -- deliberate. The non-touch is a
#     message to the body: the answer must come tonight, in the flesh.
#   - Brief mess-beat: Zira alone with the mug and unused datapad, zthought
#     monologue cataloging the math she has just done. Mentions the pressed flower
#     ("something from before") is still in the drawer and will not be looked at
#     tonight. Reaffirms the s05 realization privately: she cannot leave.
# cann.aeron_state:
#   - OB Phase I late. Marcus idiom deepened. He uses "understood" and "noted."
#   - Tremor suppression now consciously managed -- flatten-the-hand maneuver.
#     Nyra's presence suppresses it without effort; in the corridor with Zira
#     the tremor tries to come up and he has to work it down.
#   - He rehearsed the half-answer to Zira two weeks ago. He has been anticipating
#     this conversation and booking its cost. That is the scene's most honest beat.
#   - He routes around Zira after the confrontation to avoid the mess. Routing
#     around her is not new. Being routed BY her IS new.
# cann.path_tracking_flags:
#   - No player choice in this scene. The demand is the scene.
#   - flag("zira_terms_deposited"), rel_bump("Zira", conflict=2), rel_bump("Zira", respect=1).
#   - canon_set("ob.zira.terms_deposited"), canon_set("ob.zira.chair_at_table_formal"),
#     canon_set("ob.zira.will_break_smoothness"), canon_set("ob.zira.half_of_three").
#   - tp_seed("a4.ob.zira.make_me_feel_it").
#   - metric("zira_patience", adjust=-1) -- her patience ledger narrows.
# cann.thematic_flags:
#   - Terms, not concessions. Zira has graduated from confrontation (a3_s15) and
#     from private realization (a4_s05) to public, active claim-staking.
#   - Ritual vs. daily: Zira explicitly cedes the ritual category to Nyra and
#     claims the daily. This is the thematic division Act 4 OB will track.
#   - The half-answer: Aeron's Marcus-idiom competence now includes the capacity
#     to give half-truths that are more honest than whole-truth alternatives. The
#     danger is that the capacity is growing.
#   - The non-touch in the corridor: Zira using the body as a message system the
#     way Nyra uses ritual. Parallel mechanisms. Both women are teaching Aeron that
#     obedience writes into flesh. Aeron recognizes the parallel and calls it
#     structural, not ironic.
#   - "Make me feel it, then." -- the line that becomes the fuse for a4_s13.
#   - "I am not sharing command and I am not sharing him" (a3_s15) has evolved
#     into "I will take the daily. Nyra can have the ritual." That is a contract
#     Zira has written for herself. Aeron has co-signed half of it.
# cann.character_moments:
#   - Zira: "Either I am in this with you -- all of it, including what happened
#     in Sector 12 yesterday -- or I am not."
#   - Zira: "Nyra can have the ritual. I will not have the silence."
#   - Zira: "I will not be a body you reach for between ceremonies."
#   - Zira: "I am not asking you to be mine. I am asking you not to make me feel
#     like I am nothing."
#   - Aeron: "I rehearsed it two weeks ago in case someone asked. You are the
#     someone." (the most honest line in the scene)
#   - Aeron (thought): "She has promoted herself. I am the last person in the
#     base to acknowledge the promotion. I gave it to her. I will be giving it
#     to her again tonight in a different form."
#   - Zira (thought): "I will mean it. I will also want him. Those are not the
#     same sentence. I am learning to hold them as two sentences."
# cann.block_status:
#   - LINEAR. Non-erotic setup scene. The erotic answer lives in a4_s13.
# cann.requires_followup:
#   - a4_s13: Zira deepening erotic. The body answer to the corridor demand.
#   - Formal tactical-table chair for Zira: announced at 0800 ops staff meeting.
#     Track whether Noelle registers this as a rebuke of her smooth-room preference.
#   - "If the half becomes a quarter" -- Zira's exit condition. Track in Phase II.
#   - Pressed flower in the workshop drawer: the "something from before" seed for
#     a4_s13 aftercare.
