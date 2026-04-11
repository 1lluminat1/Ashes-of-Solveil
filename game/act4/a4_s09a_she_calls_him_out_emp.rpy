# =======================================================
# ACT 4 - Scene 09a: She Calls Him Out (Empathy Path)
# File: a4_s09a_she_calls_him_out_emp.rpy
# Type: ZIRA NEW INTIMACY INSERT — pre-erotic emotional opening
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s09a_she_calls_him_out_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s09a_she_calls_him_out_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, handheld but held still. The mess at the back-end of third shift —
    #         four tables, one on, three dark. Aeron at the dark one in the corner with
    #         a mug. The camera finds him over his left shoulder so we see the mug and
    #         his hands before we see his face. Zira enters from the doorway — the shot
    #         does not cut to her entry, it catches her already in the frame when
    #         Aeron looks up. She stands for three lines. She sits for the rest. When
    #         she leans forward at the turn, the focus rolls with her — a slow pull
    #         that leaves Aeron soft in the background for a single beat.
    # LIGHTING: Mess at low-rotation: one strip overhead, the kitchen pass-through at
    #           half, a spill of warmer light from the corridor that does not reach the
    #           table. Aeron is sitting inside the coldest part of the room on purpose.
    #           When Zira sits, half her face is in the corridor spill and half is in
    #           the cold. It is not a metaphor she is performing. It is where the chair
    #           is.
    # SFX: The low hum of the mess ventilation. Distant kitchen — one cook prepping
    #      for breakfast, a pan set down, a faucet. No music. A single held low note
    #      enters under the last exchange and fades through her exit.
    # FX/COMP: Aeron's mug: half-full, cold. The steam stopped happening about fifteen
    #          minutes ago. Zira does not bring a mug of her own. She comes with empty
    #          hands because her hands are the subject tonight.
    # BLOCKING: Aeron seated, angled toward the wall — the posture of someone who
    #           chose a table that does not face the door. Zira enters, walks directly
    #           to his table, stands across from him for three lines, then sits. She
    #           does not ask to sit. She sits the way a soldier takes a position she
    #           has scouted. At the turn, she leans her forearms on the table. She
    #           does not touch him. She leaves standing — she pushes back, stands, and
    #           crosses to the door. The scene does not cut before she clears the
    #           doorway. We watch her walk the full length of the mess.
    # FACE: Aeron — under-rested, the grief still sitting on him from s05 and the
    #       cipher alcove. He is not hiding it; he is filing it. Zira — clear-eyed,
    #       precise, under-read. She is making a decision she has already made, the
    #       way she makes operational decisions. The register is not operational.
    #       That is the scene's friction.

    # ========= VOICE BASELINE =========
    # EMP cadence. Zira drives the scene. Her diction is clipped field-Zira with the
    # edges sanded because this is not a field conversation. Aeron speaks less than
    # she does. He tries twice to reroute the scene into an operational register and
    # she will not let him. When he finally gives her a real sentence it is short.
    # The scene's win condition is not him accepting her invitation cleanly — it is
    # him looking at her.

    # scene bg_mess_hall_third_shift_emp with dissolve
    # play ambient "sfx/ambient/mess_night_low.ogg" fadein 2.0

    # ========== PHASE 1 — THE MUG ==========

    "The mess at the back-end of third shift."

    "Aeron has found the table in the corner — the one that does not face the door, the one that is a quarter-turn from the pass-through so the kitchen noise stays kitchen noise and does not become part of the room he is sitting in."

    "There is a mug in front of him. It was coffee. It stopped being coffee about fifteen minutes ago when the steam quit and the liquid became a temperature Aeron has not decided on yet."

    "He has not drunk any of it."

    athought "I came down here to drink coffee. I came down here because the cipher alcove was wrong and quarters were wrong and the war room was running a planning session I was not inside of, and the mess is the room a commander goes to when there is no room left."

    athought "I am not drinking the coffee. I am holding the mug. There is a difference between those two actions and the difference is most of why I am sitting here."

    "The mess is not empty. It is three-quarters empty. Two Phoenix fighters at the far table eating something Aeron cannot identify from across the room — leftovers, the shape of leftovers, the universal shape of leftovers at four in the morning. The cook is at the pass-through doing tomorrow's prep. The ventilation hums."

    "Aeron is in the corner with the mug and the weight he carried out of Selene's story about Kael and the two names that arrived on his ledger tonight — Kesa Marin, Joren Hale — and the sentence Selene left him with in the cipher alcove, which was not a sentence of comfort and was not supposed to be, and which he has been holding since the alcove the same way he is holding the mug."

    athought "Necessary is not worth it."

    athought "I am counting that sentence the way Lyra counts pulses. I am trying to see if the count ruins it. I am finding that the count does not ruin it. The count does not ruin it because the sentence is not an artifact the counting was supposed to preserve. The sentence is the counting."

    "He lifts the mug. Does not drink. Sets it down."

    "He does not hear her come in."

    "He hears the chair."

    # ========== PHASE 2 — THE CHAIR ==========

    "Zira is standing across the table from him. She must have crossed the mess at a walking pace that did not register because Aeron is not tracking doorways tonight and Zira moves through rooms the way she moves through terrain — in the part of the frame you are not watching."

    "He looks up."

    z "Aeron."

    a "Zira."

    "Her hands are empty. No mug. No datapad. No file. She is standing across from him the way a soldier stands at a table she has decided to claim."

    z "I am going to sit down. I am not going to ask."

    a "Sit down."

    "She pulls the chair out. The scrape of metal on concrete is loud in the mess at this hour. The two fighters at the far table do not look up — Phoenix is good at not looking up at commanders in the mess."

    "She sits."

    "For a moment she does not say anything. Her forearms are on the table. Her hands are flat — not folded, not fidgeting, the specific flatness of hands that have decided to be still because stillness is a discipline she is choosing."

    zthought "Start with the mug."

    zthought "Start with the mug because the mug is the thing he came down here to lie to himself about, and if I start anywhere else he is going to route me through an operational conversation in ninety seconds and I am not going to let him do that tonight."

    z "You are not drinking the coffee."

    a "It went cold."

    z "It went cold because you have been staring at it for a half hour. I watched you from the doorway for the last four minutes of that. The ventilation hum is louder than you are."

    athought "She was in the doorway for four minutes."

    athought "I did not see her. I was staring at a mug that was cold by the time she arrived."

    athought "Two months ago I would have clocked the doorway inside the first thirty seconds. Tonight I did not clock anyone. That is not data I like having."

    a "I did not see you."

    z "I know. That is part of why I am sitting down."

    "Her voice is very even. It is not the field voice. It is the version of her voice she uses when she is not on comms and not in front of a briefing — the voice Aeron has heard exactly three times and has not named to himself."

    # ========== PHASE 3 — THE ROUTE ==========

    a "What do you need."

    "He says it the way a commander says it when a fighter comes to him at four in the morning — alert, ready to fix the thing, operational."

    "It is the wrong register and he knows it is the wrong register before he finishes saying it."

    "Zira does not take the wrong register."

    z "No."

    a "No what."

    z "No, I am not here to tell you what I need. That is the first thing I am doing tonight. I am refusing the opening line. You are not going to route me through a report."

    "She does not move her hands."

    z "I am not here in a logistical capacity. I am not here to flag an operational concern. I am not here to brief you on Marcus's adaptation window or the compromise probability Noelle is running or the Lyra-band rotation for tomorrow's sweep. I came down to the mess because I saw you leave the cipher alcove an hour ago and I watched you not go to quarters and I watched you not go to the medbay and I watched you walk straight past the war room and come down here instead and sit at the table that does not face the door."

    z "I am here in a personal capacity."

    "The sentence is so flat it sounds rehearsed. It is rehearsed. She has been turning it over on the walk down."

    z "I am telling you that up front so you do not have to waste three lines trying to figure out what kind of scene this is."

    athought "She is telling me what kind of scene this is because she has been watching me try to route women in this building into operational scenes since we got to the secondary base. She is tired of it. She is more tired of it than I thought she was."

    athought "Or she is exactly as tired of it as I should have assumed and I have been failing to notice a thing that has been visible from across a mess hall for some length of time I am not going to calculate right now."

    a "Okay."

    z "Okay is a start."

    # ========== PHASE 4 — THE CALL OUT ==========

    z "You are doing it again."

    a "Doing—"

    z "You listened to Selene's story about Kael."

    "She says it without heat. The way she would say a coordinate."

    z "You listened to Selene's story about Kael and then you sat alone in the mess with your coffee and took Kesa Marin's name like it was a private tax."

    "The sentence lands across the table and does not move."

    z "I am going to say it again because I want you to hear the whole shape of it before you start answering."

    z "You listened to Selene tell you the story of the lieutenant she lost when she was twenty-four. You listened to her say that Marcus walked her into the room where the names were and made her count them. You listened to her tell you that necessary is not the same word as worth it. And then you — you, Aeron, who have been trying to learn the chapter's lesson at the speed a commander learns it and not the speed a person learns it — you stood up from the alcove and walked down here and sat in the corner with a mug and took the names onto your own ledger as a private line item. As if the names are yours alone to file. As if the grief has a single authorized signatory and the signatory is you."

    athought "I did not hear her come in."

    athought "I did not hear her come in because I was busy doing exactly what she is describing. The mug is the evidence. The mug is also the alibi. I have been holding it so that the holding is the answer I could give anyone who asked me what I was doing in the mess hall at four in the morning."

    athought "Nobody asked me until now."

    athought "She is asking."

    a "Zira—"

    z "Not yet."

    a "Zira."

    z "I am not finished. You interrupting me is the thing I am calling you out for, and I am not going to let the interruption be the way we get out of the scene."

    "He stops."

    zthought "He stopped. He does not usually stop. I am going to hold that in my pocket and take it out later."

    z "Selene gave you a story because the story was the version of the lesson that she could give. She was twenty-four. Her name was on a ledger. Marcus made her count and she hated him for it and she gave it back to you tonight because the giving was the inheritance. She was being generous. She was being the kind of generous where the generosity is also a rebuke. I watched her do it from the doorway of the command center and I thought: he is going to take this the wrong way."

    z "And then I watched you take it the wrong way."

    z "The wrong way is not that you heard her. You heard her. I was in the alcove corridor when you said the names out loud. I am not going to pretend I wasn't."

    "That is a confession. She lets it sit for a second."

    z "The wrong way is that you heard her story about sharing command and went straight to the mess hall alone. You heard 'necessary is not worth it' and turned it into a sentence you could carry by yourself. That is not what she gave you. She did not give you a private sentence. She gave you a shared one. You are doing the sharing in the wrong direction."

    # ========== PHASE 5 — THE TURN ==========

    "She leans forward. Not far — a few inches. Her forearms stay on the table. The lean is the whole gesture."

    z "I am not asking you to let me run operations with you. I already run operations with you. I have run them since the Lower Spans. You trust me with ops. You trust me with the field. You trust me with the thing that happens when the plan dies — you have told me that in three different ways in the last six weeks and I have been counting, which you should know, because I count everything, including the number of times the commander of this rebellion uses the word 'trust' at me in a room where there is no audience."

    "She does not smile."

    z "I am not asking for more of that. I have enough of that. I am the best-trusted blade in this building and I know it."

    z "I am telling you that the operational trust is not the thing I came down here about."

    z "I came down here because I have been watching you grieve alone in rooms for two weeks and I decided tonight — not yesterday, tonight — that I am not going to keep watching. I am not going to stand at doorways and count the minutes you spend with a mug. That is a way of keeping track of someone from a distance I am not willing to keep."

    z "I am telling you that I am asking to be let in."

    "The word lands in the room."

    z "Not into the ops. Into the other thing. The thing the mug is standing in for. The thing that sent you down here instead of to quarters. The thing you would rather carry in a corner than hand to any of us."

    z "I am asking to be in that room."

    "She is looking at him straight on. Her hands have not moved."

    z "I know you cannot accept the invitation cleanly tonight. I know that. I am not stupid and I am not pretending I am offering a simple thing. I watched you come out of the alcove and I know what that alcove held. I am not asking you to walk out of the grief into a conversation I have rehearsed on the walk down and make it tidy for me."

    z "I am asking you to see that I am asking."

    z "That is the whole ask. Tonight that is the whole ask. See that I am asking."

    "She stops."

    "The mess hum is the loudest thing in the room for four seconds."

    # ========== PHASE 6 — THE ANSWER HE CANNOT GIVE ==========

    athought "I am going to fail this."

    athought "I am going to fail this because she has come down here with a sentence she rehearsed on the walk and I have come down here with a mug and a ledger and the wrong register and the specific brand of night where every word I have is a word I have already spent on somebody else."

    athought "I spent a sentence on Selene. I spent a sentence on Lyra last week. I spent a sentence on Tessa the night she overruled me and I still owe her the one I promised to say in the morning. There is a running account of sentences I owe women in this building and the account does not balance."

    athought "Zira is not asking me to balance it. Zira is asking me to look at her while I am not balancing it."

    athought "I do not know if I can do the looking."

    athought "I know I cannot do the accepting."

    "He looks up from the mug."

    "Not all the way up. First at her forearms on the table. Then at her hands. Then at her face."

    "He makes it to her face."

    a "Zira."

    z "I am listening."

    a "I cannot—"

    "He stops. Tries the sentence again."

    a "I am not going to pretend I can walk out of this table into the other room you are asking about."

    z "I know."

    a "I hear you asking."

    "The sentence is very short. It does not do what he wants it to do. It does not say any of the things he would say if he had slept in the last forty-eight hours. It says one thing — the one thing he can give her without lying."

    a "I hear you asking."

    "He says it a second time because the first time was not quite aimed at her. The second time is."

    "Zira does not answer immediately."

    zthought "He said it twice. The second time was the real one. I am not going to file that. I am going to keep it."

    zthought "He did not say yes. He did not say I will try. He did not say a single sentence that could be mistaken for a contract. Aeron's word is the kind of currency where a contract is the thing that drains value out of the word, and he knows it, and I know he knows it, and the sentence I got is the one he has tonight."

    zthought "I will take it."

    zthought "I am not going to take it happily. I am going to take it the way I take a position I have scouted and decided is good enough for the night."

    z "Okay."

    a "Okay."

    z "That is not a dismissal. Okay is a word I am going to let mean what it means tonight. I am not going to make you translate it."

    # ========== PHASE 7 — SHE DOES NOT LEAVE ANGRY ==========

    "She does not stand up right away."

    "She looks at him. Not through him — at him. The look is long enough that Aeron feels it in his sternum, which is a sensation he has not felt from Zira before and does not know what to do with."

    athought "She is making me look at her and she is not going to stop until the looking is the thing that has happened."

    athought "I think that is the whole scene."

    athought "I think the scene was her making sure the looking happened."

    "She stands."

    "Not abruptly. She stands the way she sat — with decision, without haste. Her hands come off the table. She does not push the chair in. Pushing the chair in would be a grace note she is not going to spend on a scene that has earned a different kind of care."

    z "I am going to walk out of the mess now."

    a "Zira."

    z "I am not leaving angry. I want you to know that. I am leaving because I have said what I came to say and staying any longer would be asking you for something you do not have tonight."

    z "I am not asking you for something you do not have tonight."

    z "I came down here to do one thing and I did it. That is enough for the scene I came for."

    "She pauses at the edge of the table. Her eyes go to the mug."

    z "Drink the coffee or do not drink the coffee. It does not matter. The mug is not the point."

    z "But if you want a sentence from me that is operational — the only operational thing I will say tonight — it is this: you are not as alone in the room as you keep making yourself in it. I am on your six. I have been on your six since the Lower Spans. On-six is a position I know how to hold and I am holding it whether or not you look up tonight."

    z "I looked up tonight. That is my version of the message."

    "She does not wait for him to answer."

    "She turns."

    "She walks the full length of the mess to the door. Not quickly — at her own pace. The two fighters at the far table do not look up as she passes. Zira is good at leaving a room in a way that does not collect witnesses."

    "At the door she stops. She does not turn back. She says it to the doorway."

    z "See you in the war room at oh-seven."

    "Then she is gone."

    # ========== PHASE 8 — THE MUG AFTER ==========

    "Aeron does not move for a long moment."

    "He looks at the mug. He looks at the chair she was in. He looks at the doorway she walked through."

    "He looks at his hands."

    athought "I heard her ask. That is the only thing I said out loud that was true. Everything else was the mug and the ledger and the wrong register."

    athought "She did not leave angry. She said she was not leaving angry. She said it twice — once on the way out and once in the sentence about on-six. She said it because Zira does not leave a field she intends to return to without marking the perimeter."

    athought "She was marking the perimeter. The perimeter is me. She was telling me she intends to come back."

    athought "I did not tell her to come back. I did not tell her not to."

    athought "The thing I am supposed to do with this is not decide right now. The thing I am supposed to do with this is sit in the chair for another five minutes with the knowledge that I was seen tonight by a woman who has been watching me from doorways for weeks and is not going to stop watching from doorways now that the doorway has become a chair across a table."

    athought "I looked at her."

    athought "I did the looking."

    athought "The looking was the scene."

    "He reaches for the mug. Picks it up. Takes a drink."

    "The coffee is cold. It tastes like coffee that has been sitting too long."

    athought "It tastes terrible."

    athought "I am going to drink it anyway."

    athought "Not because it tastes good. Because I came down here to drink coffee and I did not drink it and she noticed that I did not drink it and I am going to drink it now as a small private penance for the fact that she noticed before I did."

    "He takes a second drink. Sets the mug down."

    "He does not get up yet."

    "He is sitting in a mess hall chair at four in the morning looking at the place Zira was sitting until ninety seconds ago and he is not alone in the room anymore in a way that is structurally different from the way he was not alone in the room before she arrived."

    athought "The difference is that somebody now knows I am in the room."

    athought "That is the whole difference."

    athought "That is most of what she came down here to produce."

    "He stays for another two minutes. Then he stands. He puts the mug on the pass-through counter on his way out. The cook at the pass-through nods at him — Phoenix nod, night-shift nod, the nod that does not require eye contact."

    "Aeron nods back."

    "He walks out of the mess toward quarters. Not toward the war room. Not toward the alcove."

    "Quarters is where he was supposed to go an hour ago."

    "It is where Zira — by the specific shape of her refusal to follow him into any other room — has just pointed him."

    athought "She is going to see me at oh-seven."

    athought "I have six hours to figure out what the looking was."

    athought "I am not going to figure it out. I am going to sleep instead, because sleep is the answer Tessa would give and the answer Zira just implied and the answer I have been refusing to give myself since the cipher alcove."

    athought "Two women have told me to sleep tonight, in different words, from different rooms."

    athought "I am going to listen to both of them by listening to one of them."

    "He does not look back at the mess."

    "The corridor is empty."

    "He walks to quarters."

    "The scene ends at the door."

    # stop ambient fadeout 2.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=1, conflict=1)
    $ flag("zira_called_aeron_out_mess", True)
    $ flag("zira_asked_to_be_let_in", True)
    $ npc_remember("Zira", "asked_to_be_let_into_grief", tone="deliberate_invitation")
    $ npc_remember("Zira", "left_without_anger", tone="perimeter_marked")
    $ npc_remember("Aeron", "zira_watched_from_doorway", tone="noticed_too_late")
    $ npc_remember("Aeron", "i_hear_you_asking", tone="smallest_true_sentence")
    $ canon_set("zira.invitation_issued", "pre_erotic_emotional_opening")
    $ canon_set("aeron.seen_by_zira_in_grief", True)
    $ tp_seed("a4.zira.let_me_in")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s09a_she_calls_him_out_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Later the same night as a4_s05 (Delegation) and a4_s05a (Tessa medbay).
#     Aeron has left the cipher alcove after Selene's Kael story and has walked
#     past quarters, past the war room, past the medbay, and ended up in the mess
#     at the tail of third shift with a mug of coffee he is not drinking.
#   - This scene does not replace the Tessa medbay scene — it runs on a different
#     night, or implicitly on the next night after Aeron has come out of Tessa's
#     cot and re-entered the same grief pattern in a new room. Either reading is
#     canonical; the implementation choice is narrative discretion.
# cann.what_happened:
#   - Aeron in the corner table of the mess. Mug of cold coffee. He is holding it,
#     not drinking it. Sitting with the weight of Selene's "necessary is not worth
#     it" and the two Phoenix names (Kesa Marin, Joren Hale) from the Sector 7
#     operation.
#   - Zira enters. She has been watching him from the doorway for four minutes.
#     She walks directly to his table, stands across from him for three lines,
#     and sits without asking.
#   - She refuses the operational register twice when Aeron tries to route her
#     into it. She announces explicitly: "I am here in a personal capacity."
#   - She delivers the call-out: "You are doing it again. You listened to Selene's
#     story about Kael and then you sat alone in the mess with your coffee and
#     took Kesa Marin's name like it was a private tax." She extends it to a full
#     paragraph about Aeron taking shared sentences and turning them into private
#     line items.
#   - She leans in for the turn and issues the invitation: "I am telling you that
#     I am asking to be let in. Not into the ops. Into the other thing. The thing
#     the mug is standing in for." She names the whole point: "I am asking you to
#     see that I am asking. That is the whole ask. Tonight that is the whole ask.
#     See that I am asking."
#   - She names explicitly that she knows he cannot accept the invitation cleanly
#     tonight and she is not asking him to.
#   - Aeron gives her one small true sentence twice: "I hear you asking." The
#     second time lands as the real one.
#   - Zira stands to leave. She is explicit about not leaving angry. She tells him
#     she has been on his six since the Lower Spans and that looking up tonight is
#     her version of the message. She walks the full length of the mess out the
#     door. At the doorway she tells him she will see him in the war room at 0700.
#   - Aeron drinks the cold coffee as a private penance for not noticing. He walks
#     to quarters — the first time in the scene he chooses the room he has been
#     avoiding.
# cann.aeron_state:
#   - Grieving, under-rested, running on the same endurance pattern Tessa diagnosed.
#     Trying to route every woman in the building into an operational register
#     because the operational register is the room where he still thinks he has
#     authorized vocabulary.
#   - His specific failure tonight is that he did not see Zira enter. Four minutes
#     of her in the doorway registered zero. He files this as evidence against
#     himself. The unguarded doorway is a motif that will recur.
#   - He cannot accept Zira's invitation. He gives her the smallest true sentence
#     he has. The scene does not treat this as a failure — it treats it as the
#     correct outcome for the pre-erotic stage of the Zira arc. The invitation is
#     issued. The response is looking-at-her. That is the payload.
# cann.zira_state:
#   - The scene is her first explicit personal-capacity approach to Aeron in Act IV.
#     Her operational trust is a settled canon by this point (Lower Spans, s21,
#     the Act III arc). Tonight is not about ops.
#   - Her refusal of the operational register is load-bearing. She has been watching
#     Aeron route intimate scenes into ops for weeks and she is explicitly
#     interrupting the pattern. This is the scene's primary character move.
#   - "I am on your six" is her vocabulary for intimate witness. The call-back to
#     the Lower Spans frames the continuity of her position while insisting the
#     position's meaning is expanding.
#   - She does not leave angry. The not-leaving-angry is announced twice on purpose
#     because Zira-left-angry would end the arc. Zira-left-with-perimeter-marked
#     is the arc continuing.
# cann.path_tracking:
#   - EMP path. Linear. No player choice. Relationship-gated entry — requires
#     Zira trust threshold from Act III (Lower Spans through Zira first contact).
#   - rel_bump Zira trust +1, conflict +1 — both are deliberate. Trust because she
#     has chosen to show him something of herself. Conflict because the scene does
#     not resolve into mutual ease; it resolves into a debt Aeron now owes her and
#     she owes the scene.
#   - canon_set zira.invitation_issued — downstream Zira scenes should read against
#     this state. The pre-erotic emotional opening is now canonical.
#   - canon_set aeron.seen_by_zira_in_grief — the looking is the canonical payload.
#   - tp_seed a4.zira.let_me_in — seeds the Zira erotic scene and any future Zira
#     intimacy beat. The payoff is not tonight.
# cann.thematic_flags:
#   - "You are doing it again" — the diagnostic call that shared sentences have to
#     be shared in the correct direction. Aeron keeps receiving shared language
#     (Selene's Kael story, Tessa's rule of three, Lyra's presence-is-enough) and
#     privatizing it. Zira is the first LI to name the privatization pattern out
#     loud directly to his face.
#   - The mug as the scene's physical alibi. A body prop that stands in for the
#     grief. Zira punctures the alibi without touching the mug. She makes him
#     notice that the mug is an alibi by telling him the mug is not the point.
#   - "See that I am asking" — the Act IV Zira thesis in compressed form. Not
#     acceptance, not resolution. Witness of the ask.
#   - On-six as intimate vocabulary. Zira is migrating a field term into the
#     personal register. This is Zira's version of the Act IV chapter-wide move
#     where each LI is learning to use operational language for intimate truth.
# cann.character_moments:
#   - Aeron: did not see Zira in the doorway for four minutes (evidence of
#     depletion). Said "I hear you asking" twice, with the second one aimed.
#     Drank the cold coffee as penance. Walked to quarters — the room he had
#     been avoiding — because Zira pointed him there without telling him to.
#   - Zira: walked directly to the table without asking. Refused operational
#     register twice. Issued the invitation as a prepared sentence rehearsed on
#     the walk down. Left without anger and announced the not-leaving-angry
#     twice. Said "See you in the war room at oh-seven" to the doorway as a
#     promise of return.
# cann.callbacks:
#   - a1_s20_lower_spans: "on your six" is where the phrase originated between
#     Aeron and Zira. She migrates it here into a non-operational register.
#   - a1_s21_zira_first_contact: the original moment of Zira choosing Aeron. This
#     scene is the Act IV version of that choice — personal instead of political.
#   - a4_s05_delegation_test_emp: Selene's Kael story and "necessary is not worth
#     it." Zira invokes both explicitly. She is the first LI to hear about Kael
#     indirectly (she was in the alcove corridor and heard Aeron say the names).
#   - a4_s05a_you_are_not_a_machine_emp: Tessa's overrule. Zira's approach here
#     is a different shape of the same lesson: love as the right to interrupt.
#     The two scenes run in counterpoint.
#   - a4_s04_lyra_unbuckled_emp: "presence is enough" as cross-LI language. Zira
#     does not use the word presence — she uses witness and looking. Aeron is
#     meant to note the variation in the Zira erotic follow-up.
# cann.block_status:
#   - LINEAR. EMP path only. Relationship-gated entry. Pre-erotic setup for the
#     Zira intimacy arc. The erotic scene is separate and does not occur here.
# cann.requires_followup:
#   - The Zira erotic scene is seeded by tp_seed a4.zira.let_me_in. It should not
#     fire immediately after this scene. There needs to be at least one additional
#     beat — a shared operation, a second private moment, a decision from Aeron to
#     seek Zira out rather than be found — before the payoff scene.
#   - Aeron walking to quarters is a small recoverable move. If the next scene
#     begins with him in quarters it reads continuously. If it begins elsewhere,
#     the implication is that quarters was the resting state and sleep happened.
#   - "See you in the war room at oh-seven" is an operational callback. Any 0700
#     war room scene that follows should reference the mess exchange silently —
#     a look across the table, a held beat, not a spoken callback.
#   - The "I hear you asking" sentence is a Zira-specific token. Future Zira
#     scenes can reference it as the first true sentence he gave her in Act IV.
