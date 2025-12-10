# =======================================================
# ACT 2 - Scene 11: Selene's Judgment
# File: act2_11_selenes_judgment.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_11_selenes_judgment"
$ scene_mark(_current_scene_id, "entered")

label act2_11_selenes_judgment:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Wide establishing shot, then medium shots that emphasize Selene's control of the space. Push-ins on her during confrontational beats. Aeron often shot slightly lower—she has the high ground here.
    # LIGHTING: Ember glow from tactical displays, bronze-red undertones. Cold spots where Selene stands. Her gloves catch the light.
    # SFX: Loop — distant generator hum, radio static undertone, dripping water. One-shots — map rustling, boot steps on metal grating, her gloves creaking when she grips things.
    # FX/COMP: Tactical displays showing Unders maps, resource flows, casualty counts. Ember light on Selene's face during key moments.
    # BLOCKING/PROPS: Abandoned transit control room repurposed as command post. Central table with maps. Selene's mother's gloves (scorched, copper-stitched). Armed resistance members at the periphery.
    # FACE: Selene reads cold authority, exhaustion underneath, occasional flashes of the empathy she guards. Aeron controlled but uncertain—this is her territory. Lyra and Zira watchful.

    # ========== CHAPTER TITLE CARD ==========
    scene black with fade
    centered "{size=+20}ACT II{/size}"
    pause 0.5
    centered "{size=+10}Chapter III — Proving Ground{/size}"
    pause 2.0
    scene black with fade

    # ========== TRANSIT TO MEETING POINT — NIGHT, DAY 5 ==========

    "The route to Selene's command post takes them through parts of the Unders Aeron hasn't seen."

    "Narrower. Older. The kind of tunnels that predate Echelon—remnants of a city that existed before the tiers were stacked."

    # VISUAL: Zira leading, Aeron and Lyra following. Two resistance escorts flanking them—armed, silent.
    "Zira navigates by memory, not light. The escorts Selene sent don't speak, don't make eye contact. They move like soldiers."

    z "(low) When we get there, let me do the introductions. Selene doesn't like surprises."

    a "What should I expect?"

    z "Hostility. Questions. Probably some variation of 'why shouldn't I kill you right now.'"

    l "Encouraging."

    z "She lost thirty-seven people in the Purge. People she'd kept alive for years."
    z "And then she found out Glass coordinated the Sweep that made it possible."
    z "So yeah. Expect hostility."

    if empathy_band() == "obedience":
        athought "Thirty-seven casualties attributable to my operation. I've read worse numbers in morning briefings."
        athought "But those were numbers. These were her people."
    else:
        athought "Thirty-seven. I keep hearing body counts attached to my name."
        athought "At some point, I need to stop being surprised."

    # VISUAL: They approach a heavy door—reinforced, guarded. Old transit authority markings barely visible under rebellion graffiti.
    "The door ahead is reinforced steel, scarred with age and violence. Two guards flank it, weapons ready but not raised."

    "One of them nods to Zira. The door grinds open."

    z "Remember: she's testing you from the moment you walk in. Every word, every gesture."
    z "Don't try to impress her. Just be honest."

    a "And if honest isn't enough?"

    z "Then we're all in trouble."

    # ========== SELENE'S COMMAND POST ==========

    # VISUAL: Abandoned transit control room. Tactical displays, maps on every surface. Ember lighting. Selene at the center, back to them, studying a map.
    "The room was a transit control center once. Now it's a war room."

    "Maps cover every surface—some holographic, most paper, all annotated in tight handwriting. Tactical displays flicker with patrol routes and resource flows."

    "And at the center, back turned, stands Selene Ward."

    # VISUAL: Selene in profile. The gloves—scorched leather, copper stitching—visible on her hands. She doesn't turn.
    "She's smaller than he expected. Compact. Every line of her body speaks of compressed force—a spring wound tight enough to kill."

    "Her hands rest on the map table. The gloves catch the ember light—old leather, scorched at the edges, repaired with copper thread."

    "She doesn't turn around."

    sel "Zira. You're four minutes early."

    z "Patrols were lighter than expected."

    sel "Or you were faster. Either way, noted."

    "Still not turning. Still studying the map."

    sel "Captain Rylan. Formerly Glass. Echelon Order Division, specialized in population control and containment operations."
    sel "Responsible for the coordination of the Sector 10 Sweep, which directly enabled the Purge that killed thirty-seven of my people."

    "Now she turns."

    # VISUAL: Selene facing them. Bronze eyes, sharp features, exhaustion worn like armor. The gloves never leave the table—she's grounded herself.
    "Her eyes are bronze in the ember light. Sharp. Measuring."

    "She's younger than he expected—maybe thirty, maybe less. But her face carries decades of weight."

    sel "Tell me why I shouldn't have you shot."

    "The question lands flat. Not theatrical. Genuine."

    if empathy_band() == "obedience":
        athought "Direct. Efficient. She's not performing—she's evaluating."
        athought "I've done the same thing in a hundred interrogations."
    elif empathy_band() == "empathy":
        athought "She's not threatening. She's asking."
        athought "That's worse, somehow. Threats I know how to handle."
    else:
        athought "She's giving me a chance to answer. That's more than I probably deserve."

    # --- PLAYER CHOICE: How does Aeron respond to her challenge? ---
    menu:
        "She's asked a direct question. How does he answer?"

        "Acknowledge the debt—he owes her people.":
            $ choice_and_dev(
                _current_scene_id, "_acknowledge_debt", "EMP", factor=1,
                note="Aeron admits moral responsibility without deflection or tactical framing."
            )
            $ npc_remember("Selene", "aeron_acknowledged_debt", tone="assessing")
            $ scene_mark(_current_scene_id, "acknowledged_debt")

            a "You shouldn't."

            "The room goes still. Even Zira looks surprised."

            a "I coordinated the Sweep. I drew the lines, set the parameters, identified the targets."
            a "I didn't order the Purge, but I made it possible. That's not a distinction that matters to the people who died."

            sel "(flat) No. It isn't."

            a "I can't give you back what you lost. I can't undo what I did."
            a "But I can tell you that the man who planned that operation doesn't exist anymore."
            a "And the man standing here is trying to figure out what he owes."

            sel "And what do you think you owe?"

            a "More than I can pay. But I'm going to try anyway."

            "Selene's expression doesn't change. But something shifts behind her eyes."

            sel "That's the first honest thing an Echelon officer has ever said to me."

        "Make the tactical case—his skills are valuable.":
            $ choice_and_dev(
                _current_scene_id, "_tactical_case", "OB", factor=1,
                note="Aeron frames his value in terms of utility rather than addressing the moral weight."
            )
            $ npc_remember("Selene", "aeron_made_tactical_case", tone="wary")
            $ scene_mark(_current_scene_id, "made_tactical_case")

            a "Because I know how Echelon hunts."

            sel "So does Noelle."

            a "Noelle knows the patterns. I know the people."
            a "I know how Marcus thinks, how Order Division deploys, where the blind spots are in their doctrine."
            a "You can use that. Or you can shoot me and lose the only insider perspective you're going to get."

            sel "You think your knowledge makes you valuable enough to overlook thirty-seven deaths?"

            a "I think you're too smart to let emotion override tactical advantage."

            "Selene's jaw tightens. Wrong move."

            sel "Emotion."
            sel "You think I want you dead because of emotion?"

            a "I think—"

            sel "I want you dead because you're a threat. Because every Echelon asset who's ever 'defected' has been a plant."
            sel "And because the last time I trusted someone from your world, I had to scrape their bomb fragments off my command table."

            if pass_tier("EMP1", "EMP2", "EMP3"):
                athought "I miscalculated. Badly."
                athought "She's not looking for utility. She's looking for something real."
            else:
                athought "She's harder than I expected. The tactical approach isn't landing."
                athought "Need to adjust."

            a "...I'm not a plant."

            sel "Convince me."

    # ========== THE EVALUATION CONTINUES ==========

    "Selene moves around the table. Slow. Deliberate. A commander surveying terrain."

    sel "Noelle vouched for you. Called you an 'anomaly worth investigating.'"
    sel "Zira vouched for you. Gave you access to her Ghostline network."
    sel "That's two people I trust telling me you might be real."

    "She stops directly in front of him. Close enough that he can see the scorch marks on her gloves."

    sel "But trust is earned. Not inherited."

    a "What do you need?"

    sel "Proof. Not words—actions."
    sel "There's an Echelon supply depot in Sector 4. Medical supplies, ration packs, communication equipment."
    sel "Lightly guarded, but the patrol routes are designed by someone who knew what they were doing."

    "Her eyes bore into his."

    sel "Designed by Glass, actually. Two years ago."

    a "You want me to break my own security protocols."

    sel "I want to see if you can. And I want to see how you do it."
    sel "Noelle will provide overwatch. Zira will run communications. You lead the ground team."

    l "And me?"

    sel "(glancing at Lyra) You stay here."

    l "I'm not—"

    sel "You're a liability in the field right now. Unders terrain, Echelon training that hasn't adapted."
    sel "More importantly, you're leverage. If this is a trap, having you both in the same place makes extraction easy."
    sel "Separated, we have options."

    "Lyra bristles, but she doesn't argue. The logic is sound."

    if scene_has(_current_scene_id, "acknowledged_debt"):
        sel "(to Aeron) You admitted you owe a debt. Here's your chance to start paying it."
        sel "Succeed, and we talk about what comes next."
        sel "Fail, and..."

        a "And?"

        sel "Let's hope you don't fail."
    else:
        sel "(to Aeron) You said your knowledge makes you valuable. Prove it."
        sel "Succeed, and maybe I'll believe you're more than a walking security breach."
        sel "Fail, and I'll know exactly what you are."

    # ========== PRIVATE MOMENT — SELENE'S GLOVES ==========

    "Zira pulls Lyra aside to discuss logistics. For a moment, Aeron and Selene are alone at the map table."

    "She's looking at the depot schematics, but her attention is elsewhere."

    sel "You noticed the gloves."

    a "They're distinctive."

    sel "They were my mother's."
    sel "She died buying time for me to escape during the Siege of Tier 5. I was twelve."
    sel "These are the last things she touched."

    "Her voice is flat. Recitation, not confession."

    sel "I wear them to remember what command costs."
    sel "Every decision I make, I make with her hands."

    if empathy_band() == "obedience":
        athought "She's telling me something important. Establishing context for how she leads."
        athought "Or testing to see how I respond to vulnerability."
    else:
        athought "She's not sharing. She's warning."
        athought "This is what leadership looks like here. This is the weight."

    a "I'm sorry."

    sel "Don't be sorry. Be useful."
    sel "Sorry doesn't bring anyone back. Results might keep more people alive."

    "She turns back to the map."

    sel "The operation is tomorrow night. Zira will brief you on the specifics."
    sel "Get some rest. You'll need it."

    # ========== CLOSING — THE WEIGHT OF JUDGMENT ==========

    # VISUAL: Aeron, Lyra, and Zira leaving the command post. The door closing behind them.
    "The door grinds shut behind them. The Unders swallows them back into its dark."

    z "(exhaling) That went... better than I expected."

    l "She wants to use him as a test subject."

    z "She wants to see what he's made of. There's a difference."

    a "She's right to be suspicious."

    l "Aeron—"

    a "I designed those patrol routes. Two years ago, sitting in a climate-controlled office, moving pins on a map."
    a "I never thought about what those pins meant. Who would have to live with the patterns I created."

    if empathy_band() == "obedience":
        athought "Now I have to break them. Use my own work against Echelon."
        athought "There's a certain symmetry to it. Poetic, almost."
    elif empathy_band() == "empathy":
        athought "Every system I built is a cage someone else is trapped in."
        athought "Maybe breaking them is the only way to start paying the debt."
    else:
        athought "My patterns. My protocols. My responsibility to undo them."

    z "Can you do it? Break your own security?"

    a "I designed it to be unbreakable."
    a "But I also designed it two years ago. I know what I was thinking then."
    a "I know where I got lazy. Where I made assumptions."

    l "And if you can't find the flaw?"

    a "Then Selene was right not to trust me."

    # VISUAL: The three of them walking through the dark tunnels. Tomorrow weighing on them.
    "They walk back through the ancient tunnels. Tomorrow, the test."

    "Tomorrow, Aeron finds out if he can destroy what he built."

    "And Selene finds out if he's worth the risk of keeping alive."

    # --- SCENE WRAP ---
    $ encounter_inc("Selene")
    $ flag_on("Selene", "first_meeting_complete")
    $ scene_mark(_current_scene_id, "operation_assigned")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_11_selenes_judgment
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: True
# cann.when_in_timeline:
#   - Night of Day 5. First meeting with Selene Ward.
# cann.what_happened:
#   - Transit to Selene's command post with Zira and resistance escorts.
#   - Selene confronts Aeron immediately: "Tell me why I shouldn't have you shot."
#   - She names the debt: 37 of her people died because of his Sweep coordination.
#   - Core choice: Aeron acknowledges the debt (EMP) or makes the tactical case (OB).
#   - OB path: Selene pushes back hard on "emotion" framing—"the last defector left bomb fragments on my command table."
#   - She assigns a test: raid an Echelon supply depot in Sector 4.
#   - The depot's patrol routes were designed by Glass two years ago—he must break his own security.
#   - Lyra ordered to stay behind as leverage/separated assets.
#   - Private moment: Selene explains her mother's gloves (Aris Ward, Siege of Tier 5).
#   - "I wear them to remember what command costs."
#   - Scene ends with operation assigned for tomorrow night.
# cann.aeron_state:
#   - Being evaluated by someone who has every reason to kill him.
#   - EMP path: Admits moral debt, earns "first honest thing from Echelon."
#   - OB path: Tactical framing backfires; Selene challenges his dismissal of "emotion."
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_acknowledge_debt` → EMP +1 weight, Selene notes "first honest thing."
#       • `_tactical_case` → OB +1 weight, Selene pushes back, wary tone.
#   - Scene flags: `acknowledged_debt` vs `made_tactical_case` for future Selene interactions.
#   - NPC memories stored via `npc_remember()`.
#   - Running empathy range at scene end: -14 to +4.
# cann.thematic_flags:
#   - Motifs: The gloves as inherited burden, breaking what you built, debt as driver.
#   - Selene's doctrine: "Trust is earned. Not inherited."
#   - The depot test: Aeron must literally dismantle his own security design.
#   - Aris Ward's gloves: "Every decision I make, I make with her hands."
#   - "Don't be sorry. Be useful." — Selene's philosophy.
# cann.alignment_flavor_points:
#   - Opening: Different internal framing of the 37 casualties
#   - Response to "why shouldn't I shoot you": debt vs utility
#   - Selene's gloves revelation: tactical read vs emotional weight
#   - Closing: Different internal processing of the assignment
# cann.character_moments:
#   - Selene: Cold authority masking exhaustion. The gloves story is warning, not vulnerability.
#   - The "bomb fragments" line reveals past betrayal by defector—explains her suspicion.
#   - Lyra being separated is tactical, and she recognizes it.
#   - Zira's "better than expected" shows this was a real risk.
# cann.worldbuilding:
#   - Selene's command post: old transit control room repurposed.
#   - Supply depot in Sector 4—medical supplies, rations, comms equipment.
#   - The depot's security was designed by Glass two years ago.
# cann.block_status:
#   - Selene intro complete. Test operation assigned.
#   - Next scene (A2_12) should be the operation itself.
# cann.requires_followup:
#   - A2_12: The depot raid—Aeron breaking his own security.
#   - Lyra's separation could have its own beat (what she does while waiting).
#   - Selene's assessment of the operation will determine next steps.
#   - `acknowledged_debt` vs `made_tactical_case` affects Selene's warming arc.
#   - The gloves should return in later Selene scenes (especially EMP intimacy arc).
