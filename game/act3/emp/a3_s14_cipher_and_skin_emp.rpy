# =======================================================
# ACT 3 - Scene 14: Cipher and Skin (Empathy Path)
# File: a3_s14_cipher_and_skin_emp.rpy
# Type: SELENE FIRST KISS (relationship building)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s14_cipher_and_skin_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s14_cipher_and_skin_emp:

    $ show_timeline("25th of Cipher, 388 A.C.", "01:00", "Phoenix Base — Ops Table")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm lens, locked tripod for the opening wide shot — stability that matches command routine.
    #         As the conversation turns personal, shift to handheld 32mm — the frame loosens with them.
    #         Two-shot bias throughout. Never shoot one without the other in peripheral frame.
    #         The cipher on the table is always visible. It anchors every composition.
    #         The kiss: single take. No cutting. Hold the frame and let it happen.
    # LIGHTING: War room practicals — amber strip lights along the walls, green glow from the holo-table (powered down).
    #           The cipher catches lamplight — metal glint, warm. As the scene turns intimate,
    #           the green fades and the amber dominates. Rim light on Selene's jawline. Warmth on hands.
    # SFX: Loop — base ambient low hum, ventilation tick, distant night sounds. Quiet base.
    #      One-shots — paper rustle, chair creak, cipher slide on table, breath catch.
    #      The silence is the dominant texture. Two people who are comfortable in it.
    # FX/COMP: Maps spread across the table. Datapad glow dying as it powers down. The cipher —
    #          a palm-sized metal disk, command authentication token — catching amber light.
    # BLOCKING: Ops table. Selene seated, Aeron across from her. Maps between them.
    #           The distance closes through the scene — chairs angle, elbows on the table, leaning in.
    #           The handshake happens standing. The kiss happens standing. The cipher stays on the table.
    # CANON: FIRST KISS scene for Selene. Not erotic — the line crosses from professional to personal.
    #        Selene initiates. She's the one crossing her own rule.
    #        The cipher is their partnership's physical symbol — it stays present through the kiss.
    #        Callbacks: a3_s04 shared command, a3_s06 guardrails negotiation, a3_s07 "He didn't plan for you to stay."
    # CONSENT: No formal gate framework — this is a kiss, not intimacy. But the emotional consent
    #          is built into the scene structure: she initiates, he reciprocates, both acknowledge.
    # FACE: Selene — controlled until she isn't. The crack is in her eyes before her mouth.
    #        Aeron — reading her. The moment he stops reading and starts feeling.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, warmth, but Selene's voice carries military precision even in softness.
    # Selene: Direct. Spare. Says exactly what she means. Vulnerable only through what she doesn't say.
    # Aeron: Attentive. His internal voice tracks the shift before the dialogue catches up.
    # The tactical discussion is their native language. The personal disclosure is foreign territory.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - LATE NIGHT]
    # The war room after hours. Maps spread across the ops table. Two chairs.
    # Everyone else cleared out an hour ago. The base is quiet.

    #scene bg_war_room_night_emp with dissolve
    #play ambient "sfx/ambient/base_night_quiet.ogg" fadein 2.0

    # --- OPENING: WORKING LATE ---

    "The holo-table is dark. They switched to paper two hours ago when the projector started flickering — Dren's rebuilt power junction still temperamental."

    "Maps cover the ops table. Patrol routes in blue pencil. Supply lines in red. Civilian density in orange crosshatch. Selene's handwriting is sharp and economical. Aeron's is looser, faster."

    athought "We've been at this since dinner. The Sector 11 approach has fourteen viable entry points and none of them are good enough."

    sel "The southern corridor is too exposed. Thirty meters of open ground before the first hard cover."

    a "And the northern route puts us inside their drone sweep radius for six minutes."

    sel "Which leaves the subsurface access. Tight. Single-file. But covered."

    a "If we can get the grating off without triggering the vibration sensors."

    sel "Zira says she can."

    a "Zira says a lot of things."

    "Selene almost smiles. The expression lives in her eyes, not her mouth."

    sel "She delivers on most of them."

    athought "The cipher sits between us on the table. Palm-sized metal disk, command authentication paired to both our biosignatures."

    athought "I've started thinking of it as ours. That's dangerous."

    # --- THE DISCUSSION TURNS ---

    "He reaches for the Sector 11 overlay. His hand brushes the cipher. He moves it aside without thinking."

    "Selene watches him do it."

    sel "You handle it differently now."

    a "Handle what?"

    sel "The cipher. When I first gave it to you, you picked it up like it might detonate."

    athought "She's right. I did."

    a "It felt heavy."

    sel "It's forty grams."

    a "That's not what I meant."

    "She leans back. The chair creaks. Her fingers find the edge of a map and fold it absently — a habit he's noticed. Something to do with her hands while her mind works."

    sel "I know what you meant."

    "A silence. Not empty — the kind that sits between two people who've spent enough hours in a room together that the quiet has its own grammar."

    athought "She looks tired. Not the operational fatigue that shows in posture — something older. Something she carries when she thinks no one's reading her."

    athought "I'm always reading her. That's the problem."

    a "When did you last sleep?"

    sel "Define sleep."

    a "More than three hours. Horizontal. Eyes closed."

    sel "Bold of you to assume I close my eyes."

    athought "There it is. The deflection. She's good at it — better than Zira, who uses humor. Selene uses precision."

    athought "But I've learned the difference between Selene being direct and Selene directing the conversation away from herself."

    a "Selene."

    "She looks at him. The deflection dies."

    sel "Tuesday. I think."

    a "It's Friday."

    sel "I'm aware."

    # --- THE PERSONAL ---

    "He sets down the pencil. She notices."

    athought "When I stop working, she pays attention. It means I'm about to say something she won't want to hear."

    a "You carry this like it's only yours."

    sel "That's because for nineteen years, it was."

    athought "Nineteen years. Before the rebellion. Before Phoenix. Before me."

    athought "She was running operations alone for nineteen years. Building networks, placing assets, mapping Echelon's blind spots."

    athought "Nineteen years of planning a revolution with no one to check her math."

    a "That's a long time to hold the table by yourself."

    sel "I had people."

    a "You had assets. Contacts. Sources."

    "He pauses."

    a "Did you have anyone who told you to sleep?"

    "The question lands differently than he expected. She doesn't deflect. Doesn't redirect. Just looks at the maps spread between them like the answer is somewhere in the topography."

    sel "There was someone. Early on. Before I understood what nineteen years would cost."

    athought "She's never talked about this. Not in briefings, not in the quiet after operations, not in the hundred small conversations that have built this thing between us."

    sel "He was a sector coordinator. Galan District. Good instincts. Better heart."

    a "What happened?"

    sel "What happens to good hearts in Echelon's territory."

    "Her hand rests on the table. The fingers aren't folded now. Just flat. Still."

    sel "I learned to carry things alone because the alternative was watching someone else break under the weight."

    sel "So I decided the weight was mine. And I held it."

    athought "She says it without self-pity. Without performance. The way you describe weather — factual, finished."

    athought "That's what makes it land."

    a "You don't have to hold it alone anymore."

    sel "I know."

    "She says it simply. But her hand moves — just slightly — toward the cipher on the table."

    sel "That's what this is, isn't it?"

    "She means the cipher. She means the table, the maps, the late nights."

    "She means more than any of those things."

    # --- THE HANDSHAKE ---

    "The maps are done. Nothing left to plan tonight that won't keep until morning."

    "They stand. The routine: papers stacked, pencils gathered, datapads powered down."

    "The handshake."

    athought "We started this after the first shared briefing. Her idea. Formal enough to honor the partnership. Human enough to admit it's personal."

    athought "Every session ends with it. Grip, hold, release. Two seconds."

    "She extends her hand across the table. He takes it."

    "Grip. Hold."

    athought "Two seconds pass."

    athought "Neither of us lets go."

    "Three seconds. Four."

    "Her grip doesn't loosen. His thumb shifts — barely — against her knuckle. A question neither of them is asking out loud."

    athought "Her pulse is in her palm. I can feel it. Steady. Faster than it should be."

    athought "Mine too."

    sel "Aeron."

    a "Yeah."

    sel "We should let go."

    a "We should."

    "Five seconds. Six."

    athought "I'm watching her face. The composure is intact — jaw set, eyes level. Military bearing so deep it's bone structure."

    athought "But her eyes. Something in her eyes has changed, and I don't think she can take it back."

    # --- THE LINE ---

    sel "I've commanded operations across four sectors. I've held a revolution together with spit and wire for two decades."

    "Her voice is low. Controlled. But the control is costing her."

    sel "I have never been uncertain about a tactical decision in the field."

    a "And now?"

    sel "This isn't a tactical decision."

    athought "She steps around the table. Her hand is still in mine. The cipher is behind her now — on the table between the maps, catching amber light."

    athought "She's close enough that I can see the scar at her temple — the one from the Echelon raid. The stitches are gone but the line remains."

    a "Selene, I've never said this to a commanding officer."

    sel "I've never done this with someone under my command."

    a "What are you doing?"

    sel "Making a decision that isn't tactical."

    "She doesn't hesitate. That's who she is."

    "Her free hand comes up to his jaw. Steady. Certain. The same hands that moved maps and planned operations and carried nineteen years of solitary weight."

    "She kisses him."

    # VISUAL: The kiss. Brief. Firm. Not tentative — decided. The way Selene does everything.
    # CAMERA: Hold the two-shot. Don't cut. The cipher visible on the table behind them.

    athought "It's not soft. Not careful. It's the kiss of someone who made a decision and executed it."

    athought "Brief. The pressure of her mouth against mine is a statement, not a question."

    athought "She pulls back. Not far. An inch. Her hand still on my jaw."

    athought "Her eyes are open. She's reading me the way she reads a battlefield — every detail, no margin for error."

    a "Selene."

    sel "Don't say something you'll regret in the morning."

    a "I don't regret things in the morning. I regret the things I didn't do."

    "He closes the inch. Kisses her back."

    "This one is slower. Still not soft — they're not soft people. But it takes its time."

    athought "Her hand slides from my jaw to the back of my neck. Fingers in my hair. Not pulling — holding."

    athought "I put my hand on the small of her back and feel the tension she carries there. The permanent architecture of twenty years' vigilance."

    athought "For a moment, it eases."

    # --- AFTERMATH ---

    "They step apart. Not far. The distance is honest — close enough to have made a choice, far enough to think about it."

    "Selene's hand drops to her side. She exhales. Once. The breath she's been holding since she stepped around the table."

    sel "This changes things."

    a "It already changed."

    sel "When?"

    athought "I think about it. The first shared briefing. The Sector 4 convoy. The fourteen-second window. The way she said 'Agreed' without questioning my math."

    athought "Or maybe earlier. Maybe it changed the first time she looked at me like I was someone worth trusting with the weight."

    a "I don't know. Before tonight."

    sel "Before tonight."

    "She nods. Processing. The analyst in her filing this alongside everything else."

    sel "I'm not going to pretend this didn't happen."

    a "Good. Neither am I."

    sel "And I'm not going to resolve it tonight."

    a "I'm not asking you to."

    "Her eyes move to the table. The cipher. Sitting between the maps."

    sel "The cipher is still ours."

    a "It was always ours."

    sel "I mean — this doesn't change the command structure. The partnership comes first."

    a "Agreed."

    athought "She's setting parameters. Of course she is. This is how Selene processes — build the framework, then figure out what lives inside it."

    athought "I don't mind. I've lived inside enough frameworks to know that some of them keep you standing."

    sel "Goodnight, Aeron."

    a "Goodnight, Selene."

    "She picks up the cipher. Turns it in her fingers. Sets it down again — in the center of the table, equidistant from both chairs."

    "She walks out. Her footsteps are steady. The door closes behind her."

    athought "I stand in the war room."

    athought "The maps are still on the table. The cipher is still warm from her hand."

    athought "Something crossed a line tonight that can't be uncrossed."

    athought "She knows it. I know it."

    athought "We didn't resolve it. We acknowledged it."

    athought "That's enough for tonight."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=1, affection=2)
    $ flag("selene_first_kiss", True)
    $ scene_mark(_current_scene_id, "completed")

    call li_lore_check("Selene") from _a3_s14_lore

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s14_cipher_and_skin_emp
# cann.chapter: Act III, Phase II - Deepening (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase II. After the counter-strike recovery and base rebuild.
#   - Late night planning session. The team has been operational for weeks.
#   - The command partnership is mature — this is the night it crosses the line.
# cann.what_happened:
#   - Aeron and Selene work late planning the Sector 11 approach. Everyone else has left.
#   - Tactical discussion turns personal when Aeron asks when she last slept.
#   - Selene reveals fragment of her past — nineteen years carrying the rebellion alone.
#     A sector coordinator she lost early on. "Good instincts. Better heart."
#   - Aeron: "You don't have to hold it alone anymore."
#   - The handshake — their routine end-of-session ritual — lasts too long. Neither lets go.
#   - Selene crosses her own line. She initiates the kiss. Brief, firm, decided.
#   - Aeron reciprocates. The second kiss is slower.
#   - Aftermath is honest, not awkward. "This changes things." / "It already changed."
#   - They don't resolve it. They acknowledge it. The cipher stays on the table.
# cann.aeron_state:
#   - EMP present, attentive. Reads Selene's shifts before the dialogue catches up.
#   - "I don't regret things in the morning. I regret the things I didn't do."
#   - The partnership was already personal. This just made it legible.
# cann.path_tracking:
#   - rel_bump("Selene", trust=1, affection=2). flag("selene_first_kiss").
#   - No player choice — earned through prior scene accumulation.
#   - Gates a3_s16 (Command and Surrender, first erotic).
# cann.thematic_flags:
#   - Motifs: The cipher (partnership made physical), the handshake (ritual that breaks its own boundary),
#     the maps (professional surface over personal depth), amber light (warmth bleeding through control).
#   - "This changes things." / "It already changed." — the thesis.
#   - Selene initiates because she's the one crossing her own rule. That's who she is — decisive.
#   - The kiss is not tentative. Selene doesn't do tentative.
#   - Nineteen years alone. The weight she carried. The someone she lost.
#   - "The cipher is still ours." — reassurance that the personal doesn't overwrite the professional.
# cann.character_moments:
#   - Selene: Vulnerability through disclosure, not softness. She shares the past factually.
#     Initiates the kiss as a command decision — not impulsive, decided.
#     Sets parameters immediately after. Builds the framework, then lives inside it.
#   - Aeron: Reads her tells. Knows the difference between Selene being direct and Selene redirecting.
#     Reciprocates without hesitation. Doesn't push for resolution.
# cann.callbacks:
#   - a3_s04: Shared command field-tested. "Agreed" without questioning the math.
#   - a3_s06: Guardrails negotiation — the professional framework that makes this crossing possible.
#   - a3_s07: "He didn't plan for you to stay." Selene's strategic clarity.
#   - The Echelon raid scar at her temple — physical reminder of the cost.
# cann.block_status:
#   - RELATIONSHIP MILESTONE (EMP). No branching. The kiss is earned through prior accumulation.
# cann.requires_followup:
#   - a3_s16 (Command and Surrender) — first erotic, builds on this emotional foundation.
#   - The cipher as recurring symbol — present in their intimate scenes, their command scenes.
#   - "Nineteen years" and the lost coordinator — can be referenced in later Selene vulnerability.
#   - The framework she sets ("partnership comes first") will be tested under pressure.
