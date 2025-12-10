# =======================================================
# ACT 2 - Scene 8: The Analyst
# File: act2_08_the_analyst.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_08_the_analyst"
$ scene_mark(_current_scene_id, "entered")

label act2_08_the_analyst:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35–50mm; alternating between group shots and singles. When Noelle speaks, camera holds on the terminal/holo—we don't see her face clearly. Push-in on Aeron when she dissects him.
    # LIGHTING: Safehouse amber + cold blue glow from the terminal. Noelle's voice comes from shadow. Her holo-presence is deliberately low-res, obscured.
    # SFX: Loop — terminal hum, data processing whispers, distant Unders ambient. One-shots — keyboard clicks through the audio feed, Noelle's voice slightly compressed/filtered.
    # FX/COMP: Holographic display showing patrol routes, data streams, Marcus's broadcast fragments. Noelle's silhouette visible but face obscured by interference.
    # BLOCKING/PROPS: Safehouse interior, Zira's portable terminal setup, crates as seats, the Ghostline relay Aeron received.
    # FACE: Zira focused and slightly protective of her connection to Noelle. Lyra wary of the disembodied voice. Aeron trying to read someone he can't see.

    # ========== SAFEHOUSE - MORNING, DAY 4 ==========

    "Day four in the Unders."

    athought "The safehouse has become routine—wake, check the door, check the window, check each other."

    if scene_has("act2_07_quiet_night", "held_space"):
        athought "Lyra slept better last night. Or at least she stopped pretending to sleep before dawn."
        athought "Something shifted between us in the dark. I'm not sure what to call it yet."
    else:
        athought "Lyra's been quiet since last night—professional and distant."
        athought "I said the wrong thing. I know it. Don't know how to fix it."

    # VISUAL: Zira setting up a portable terminal on a crate. Cables running to a wall node.
    "Zira's crouched over a portable terminal, fingers moving across a cracked interface."

    athought "Cables snake from the device to a node in the wall—Ghostline access."

    z "Okay, she's patching through. Give it a second."

    a "Who?"

    z "My analyst. The one who's been tracking Echelon movements since we pulled you out of the fire."
    z "She wants to talk to you."

    l "(wary) You have an analyst?"

    z "I have a lot of things, princess. You've met maybe ten percent of my operation."

    if empathy_band() == "obedience":
        athought "Another asset, another variable I didn't know about."
        athought "Zira's been running a parallel operation this whole time—smart, but also concerning."
    else:
        athought "She's been protecting us with resources we didn't know existed."
        athought "That's either trust or control. Maybe both."

    # VISUAL: Terminal flickers. Audio crackle. Then a voice—calm, precise, slightly compressed.
    "The terminal flickers."

    athought "Static resolves into a low hum, then a voice."
    athought "Not warm, not cold—clinical, the kind of voice that measures every word before releasing it."

    n "(through terminal) Zira. Connection stable?"

    z "Stable enough. I've got them both here."

    n "Good. I have approximately eleven minutes before I need to relocate. Let's be efficient."

    # VISUAL: A holographic silhouette appears above the terminal—female form, but the face is obscured by deliberate interference. Silver-blue tint.
    "A holographic silhouette materializes above the terminal—female, slender."

    athought "But the face is lost in static. Deliberate interference, not technical failure."
    athought "She doesn't want to be seen. Not yet."

    n "Aeron Rylan. Formerly Captain Rylan, Echelon Order Division, call sign 'Glass.'"
    n "Thirty-seven confirmed operations. Ninety-four percent mission success rate."
    n "Responsible for the coordination of the Sector 10 Sweep that preceded the Purge."

    athought "The words land like bullets—precise, each one drawing blood."

    if empathy_band() == "obedience":
        athought "She's reading my file. Or she has it memorized."
        athought "Either way, she knows exactly who I was."
    else:
        athought "Ninety-four percent. I never counted. She did."
        athought "She knows me better than I know myself. That's... unsettling."

    a "You've done your research."

    n "I don't do research, Captain. I do analysis."
    n "Research implies uncertainty. I have none."

    l "(stepping forward) Who are you?"

    n "Irrelevant to this conversation. What's relevant is what I know about your companion."
    n "And what I know suggests he's either the most valuable defector in Echelon history, or the most sophisticated infiltration asset they've ever deployed."

    z "Noelle—"

    n "I'm not finished."

    "The silhouette shifts. Hands moving."

    athought "She's pulling up data on her end."

    n "The Sector 10 Sweep was textbook Glass. Minimal casualties during the operation itself. Clean containment. Efficient processing."
    n "But the Purge that followed—that wasn't your signature. Too chaotic. Too wasteful."
    n "You don't waste resources. You never have."

    if pass_tier("OB2", "OB3"):
        athought "She's right. The Purge was Marcus's escalation, not mine."
        athought "I set the table. He burned the house down."
    elif pass_tier("EMP2", "EMP3"):
        athought "She's separating my actions from the consequences. Trying to give me an out."
        athought "I'm not sure I deserve one."
    else:
        athought "She's profiling me in real-time. Dissecting my patterns."
        athought "And she's not wrong. That's the worst part."

    n "The Purge was General Rylan's signature. Overwhelming force. Acceptable losses measured in districts, not individuals."
    n "Which means one of two things happened on that rooftop."

    a "What rooftop?"

    n "The one where you watched the Purge begin. Ghostline has seventeen angles on your position that night."
    n "You stood there for four minutes and thirty-seven seconds before Zira made contact."
    n "In that time, you didn't move. Didn't signal. Didn't attempt to rejoin your command structure."
    n "You just... watched."

    "The silhouette pauses. When she speaks again, her voice has shifted—still clinical, but with something underneath."

    athought "Curiosity, maybe."

    n "What happened in those four minutes, Captain?"

    # --- PLAYER CHOICE: How does Aeron explain his break? ---
    menu:
        "She's asking what broke him. What does he tell her?"

        "Tell her the truth—something shattered.":
            $ choice_and_dev(
                _current_scene_id, "_truth_shattered", "EMP", factor=1,
                note="Aeron admits vulnerability to a stranger. Honesty over protection."
            )
            $ npc_remember("Noelle", "aeron_admitted_shattering", tone="intrigued")
            $ scene_mark(_current_scene_id, "admitted_break")
            $ rel_bump("Noelle", trust=1)

            athought "I don't look at Lyra. Don't look at Zira. Just stare at the silhouette I can't read."

            a "I watched it start. The fires. The screaming."
            a "I'd seen operations before. Contained violence. Surgical."
            a "This was... different. This was my father turning everything I'd done into a slaughter."

            "Silence from the terminal."

            athought "I can hear her breathing. Soft. Measured."

            a "Something broke. I don't have a better word for it."
            a "I stopped being Glass. I'm not sure what I am now."

            n "(long pause) ...Interesting."

            z "(quiet) Told you he wasn't a plant.

            n "I didn't say he wasn't a plant. I said his response was interesting."
            n "But I'll note: that's the first time your vocal patterns have shown genuine distress markers since we connected."
            n "Either you're an exceptional actor, or you're telling the truth."

            a "Which do you think?"

            n "I think you're an anomaly, Captain. And I've built my career on eliminating anomalies."
            n "The fact that I'm talking to you instead of flagging your location to Echelon should tell you something."

        "Deflect—it's not her business.":
            $ choice_and_dev(
                _current_scene_id, "_deflect_question", "OB", factor=1,
                note="Aeron protects himself, maintains walls with the unknown analyst."
            )
            $ npc_remember("Noelle", "aeron_deflected_break_question", tone="noted")
            $ scene_mark(_current_scene_id, "deflected_break")

            a "That's not relevant to this conversation."

            n "Everything is relevant to analysis. But I'll note your deflection pattern."
            n "Subjects who refuse to discuss moments of crisis are either protecting trauma or protecting deception."
            n "I'll determine which as we continue."

            z "Noelle, ease off. He's not a lab rat."

            n "Everyone is a lab rat, Zira. Some just haven't noticed the maze yet."

            if pass_tier("EMP1", "EMP2", "EMP3"):
                athought "She's probing. Looking for cracks."
                athought "I gave her a wall instead. Not sure if that was the right call."
            else:
                athought "She wanted vulnerability. I gave her nothing."
                athought "That's how you survive interrogation. Even friendly ones."

    # ========== NOELLE'S ASSESSMENT ==========

    n "Let me tell you what I see, Captain."
    n "Echelon's narrative says you're a traitor who joined terrorists after a mental break."
    n "General Rylan has personally signed three execution orders with your name on them. Publicly, he calls you 'compromised.' Privately, the language is... less clinical."

    a "He's my father."

    n "Biology is irrelevant. Behavioral patterns are not."
    n "And his patterns suggest he's not hunting a traitor. He's hunting a threat."
    n "There's a difference."

    l "What difference?"

    n "Traitors are examples. You execute them publicly, make speeches, move on."
    n "Threats require containment. Erasure. The kind of resources he's deploying to find you aren't proportional to a simple defection."
    n "He's afraid of something."

    if empathy_band() == "obedience":
        athought "She's right. The heat on us is too high for a standard manhunt."
        athought "Marcus is scared. Of what I know, or what I might become."
    else:
        athought "Marcus is afraid. Of me."
        athought "I'm not sure how to feel about that."

    z "What's he afraid of?"

    n "Unknown. But the data suggests Captain Rylan represents something beyond a personnel loss."
    n "Possibly ideological. Possibly operational. Possibly..."

    "She trails off. The silhouette tilts."

    athought "She's looking at something off-screen."

    n "Possibly personal. Family dynamics introduce variables I can't fully model."

    a "You can't model everything."

    n "(sharp) That's a limitation I'm aware of, Captain. You don't need to remind me."

    "Something in her voice cracks—just for a moment. Then it smooths back out."

    athought "The clinical mask returning."

    n "I have four minutes remaining. Let me give you something useful."

    # VISUAL: The holographic display shifts—patrol routes, resource caches, a pulsing node that represents their safehouse.
    "The display shifts. Patrol routes appear in red, weaving through the Unders. Resource caches in green. Their safehouse pulses amber at the center."

    n "Echelon has increased patrols in Sectors 5 and 6 by forty-three percent since your arrival."
    n "They're not searching randomly. They're closing a net."
    n "Within seventy-two hours, your current position will be inside an active sweep zone."

    z "(cursing) Shit. That's faster than I projected."

    n "Your projections were based on standard response protocols. General Rylan isn't using standard protocols."
    n "He's using Glass protocols. The same ones Captain Rylan designed."

    athought "The irony lands like a punch."

    a "He's hunting me with my own tactics."

    n "Correct. Which means you have an advantage: you know the flaws in your own designs."
    n "Exploit them."

    if empathy_band() == "obedience":
        athought "She's right. I know where the blind spots are. The assumptions I built into the system."
        athought "I can break my own cage. If I'm fast enough."
    else:
        athought "My tactics, turned against me. Poetic."
        athought "But she's also handing me a weapon. The same patterns that made me effective could make me invisible."

    # ========== THE HOOK ==========

    n "One more thing, Captain."

    a "What?"

    n "I've been analyzing General Rylan's internal memos. There are references to something called 'Protocol Verdant.' Your name appears in seventeen of them."

    a "Never heard of it."

    n "Neither has anyone else. The files are heavily redacted—more so than standard classified material."
    n "I'll keep digging."

    # ========== CLOSING ==========

    n "Zira. Keep them alive. They're more interesting than I expected."

    z "That's high praise coming from you."

    n "It's accurate assessment. Praise is an emotional construct I don't indulge in."

    "The silhouette flickers."

    athought "She's preparing to disconnect."

    n "Captain Rylan. One final observation."

    a "What?"

    n "You've made three choices since we began talking. Each one deviated from your established Echelon patterns."
    n "Deviation is either evolution or deception. I'll be watching to determine which."

    "The terminal cuts to static. The silhouette dissolves. She's gone."

    # VISUAL: The three of them standing around the dead terminal. The weight of what just happened settling.
    "Silence fills the safehouse. The terminal hums softly, empty now."

    z "(exhaling) That's Noelle."

    l "She's... intense."

    z "She's the reason half the Unders is still alive. Her data keeps us one step ahead of the sweeps."
    z "But yeah. Intense is one word for it."

    if empathy_band() == "obedience":
        a "She's good. Clinical, but good."
        a "How much does she actually know about our position?"

        z "Everything I know. Which means everything the Ghostline sees."
        z "She's my eyes. I'm her hands. It works."

        athought "Another variable. But a useful one."
        athought "If she's as good as Zira says, we might actually survive this."
    elif empathy_band() == "empathy":
        a "Is she always like that? The whole 'everyone is data' thing?"

        z "(softer) She's been through things. Echelon things. The way she talks—it's armor, not personality."
        z "Underneath all that analysis, she's just trying to make sense of a world that stopped making sense."

        athought "Armor. I know something about that."
        athought "Maybe that's why she's interested in me. One broken thing recognizing another."
    else:
        a "She mentioned Protocol Verdant."

        z "I caught that. She'll dig until she finds something. She always does."

    # VISUAL: Aeron looking at the dead terminal. Thinking about the silhouette. The voice. The things she knows.
    if scene_has(_current_scene_id, "admitted_break"):
        athought "She called me an anomaly. Something that shouldn't exist in her models."
        athought "I'm not sure if that's an insult or a compliment."
        athought "But she's going to keep watching. Keep analyzing."
        athought "And eventually, she's going to want to see what I am up close."

        $ scene_mark(_current_scene_id, "noelle_intrigued")
    else:
        athought "She wanted more than I gave her. She'll keep digging."
        athought "That's fine. Let her dig."
        athought "When we meet in person, I'll decide how much she gets to know."

        $ scene_mark(_current_scene_id, "noelle_suspicious")

    "The terminal sits dark and quiet."

    athought "But somewhere out there, through the static and the cables and the hidden nodes, Noelle Korr is still watching."
    athought "Still analyzing."
    athought "Still waiting to see what I become."

    # --- SCENE WRAP ---
    $ flag_on("Noelle", "first_contact_made")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_08_the_analyst
# cann.chapter: Act II, Chapter II — Constellation
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning of Day 4, after Quiet Night (A2_07).
# cann.what_happened:
#   - Zira patches through a connection to her analyst, Noelle Korr.
#   - Noelle appears as an obscured holographic silhouette—deliberate anonymity.
#   - She dissects Aeron's Echelon record: 37 operations, 94% success rate, the Sector 10 Sweep.
#   - She reveals Ghostline had 17 angles on him during the Purge—watched him stand frozen for 4:37.
#   - Core choice: Aeron admits something broke (EMP) or deflects the question (OB).
#   - Noelle provides tactical intel: patrols increasing, 72-hour window before their position is compromised.
#   - She mentions "Protocol Verdant"—encrypted references to bloodlines, Aeron's name in 17 entries.
#   - She cuts the connection, promising to keep watching.
# cann.aeron_state:
#   - Being analyzed by someone who knows his patterns better than he does.
#   - EMP branch: Admits vulnerability, earns Noelle's "intrigued" status.
#   - OB branch: Maintains walls, earns Noelle's "suspicious" status—she'll dig harder.
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_truth_shattered` → EMP +1 weight, trust +1 with Noelle, "noelle_intrigued" flag.
#       • `_deflect_question` → OB +1 weight, "noelle_suspicious" flag.
#   - Scene flags: `admitted_break` vs `deflected_break` for future Noelle interactions.
#   - NPC memories stored via `npc_remember()`.
#   - Running empathy range at scene end: -13 to +3.
# cann.thematic_flags:
#   - Motifs: Analysis as armor, anomaly as hope/threat, data vs humanity.
#   - Noelle's voice as scalpel—clinical but "shaking slightly when it touches something alive."
#   - Protocol Verdant seed planted—will pay off in later acts.
#   - Marcus using Glass protocols against Aeron—poetic irony.
#   - "Deviation is either evolution or deception"—her thesis on Aeron.
# cann.alignment_flavor_points:
#   - Opening: callbacks to A2_07 outcome (held space vs distance)
#   - Noelle reading his file: different internal reactions
#   - The rooftop question: admit break vs deflect
#   - Noelle's tactical intel: different processing by band
#   - Closing assessment: different reactions to being called "interesting"
# cann.character_moments:
#   - Noelle: Introduced as voice/silhouette only. Clinical, precise, but cracks when Aeron points out her limitations.
#   - Zira: Protective of her connection to Noelle, explains her value to the team.
#   - Lyra: Wary of the disembodied voice, wants explanation about Verdant.
#   - The "everyone is a lab rat" line establishes Noelle's worldview.
# cann.worldbuilding:
#   - Echelon using Glass protocols to hunt Aeron—his own tactics against him.
#   - 72-hour window before sweep zone closes.
#   - Protocol Verdant: PURE SEED. Encrypted codename. Phrases: "bloodline integrity,"
#     "resonance compatibility," "last viable candidate." Aeron's name in 17 entries.
#   - CRITICAL: Aeron has NO reaction. The word means nothing. No speculation.
#   - First-time player: "What's Verdant? Weird. Moving on."
#   - Replay after Act 3: "OH. It was right there."
#   - Noelle will keep decrypting—payoff comes later.
# cann.block_status:
#   - Noelle soft intro complete. She remains voice/holo only until A2_13 (Intel Den, in-person meeting).
# cann.requires_followup:
#   - Protocol Verdant will need explanation to Lyra (can be A2_09 or later).
#   - 72-hour deadline creates urgency for movement—ties to base scouting.
#   - Noelle's in-person meeting (A2_13) should reflect `noelle_intrigued` vs `noelle_suspicious`.
#   - "I'll find the answers myself" (OB path) means she'll have more intel by A2_13.
