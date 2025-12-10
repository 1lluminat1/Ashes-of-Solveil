# =======================================================
# ACT 2 - Scene 10: Static Faith
# File: act2_10_static_faith.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_10_static_faith"
$ scene_mark(_current_scene_id, "entered")

label act2_10_static_faith:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Alternating medium shots and close-ups. Two-shot framing emphasizes the gap/tension between Lyra and Zira. Aeron enters frame late, observing from threshold.
    # LIGHTING: Pre-dawn gray through safehouse window. Cool tones throughout—no amber warmth yet. Zira lit by terminal glow. Lyra silhouetted against the window.
    # SFX: Loop — distant Unders hum, terminal processing sounds, early morning quiet. One-shots — Zira typing, Lyra's pendant chain, footsteps.
    # FX/COMP: Terminal displays scrolling data. Dawn light slowly warming the frame toward scene end.
    # BLOCKING/PROPS: Safehouse interior, Zira's terminal, window with bars, Lyra standing/pacing, two different "zones" of the space.
    # FACE: Zira defensive, sharp humor masking fear. Lyra earnest, frustrated, searching. Both gradually softening.

    # ========== A2_P06 — LYRA×ZIRA PAIR SCENE ==========
    # Function: Faith vs cynicism anchor. Soldier's faith vs hacker's nihilism.
    # Aeron present briefly at end—witnesses the dynamic without interrupting.

    # ========== SAFEHOUSE — EARLY MORNING, DAY 5 ==========

    "Aeron wakes to voices. Low. Tense."

    athought "The kind of conversation that's been building pressure for days."

    if scene_has("act2_09_armor_down", "intimacy_chosen"):
        "The space beside him is empty. Lyra's already up."
        "He can still feel the ghost of her warmth against his skin."
    else:
        "He's on his bedroll, alone. The gap between where he sleeps and where Lyra sleeps feels wider than it should."

    # VISUAL: Lyra by the window. Zira at her terminal. They're not looking at each other.
    "Through the dim light, he can make out the shapes: Lyra at the window, arms crossed. Zira hunched over her terminal, typing in sharp bursts."

    "They're talking."

    athought "Or arguing. The difference is subtle with these two."

    athought "I should let them work this out. Or I should intervene before it gets worse."
    athought "Either way, I should know what's happening."

    "He stays still. Listens."

    # --- LYRA AND ZIRA'S CONVERSATION (AERON OBSERVING) ---

    l "You don't actually believe that."

    z "I believe exactly that. Hope is a vulnerability. Echelon weaponizes it every day."

    l "Hope is the only thing that keeps people moving. Without it—"

    z "Without it, they stop getting killed chasing impossible dreams."
    z "I've seen what happens when people believe too hard, Lyra. They march into bullets because someone told them divinity was on the other side."

    "Zira's voice is sharp."

    athought "But there's something raw underneath it."

    l "That's not faith. That's manipulation."

    z "And the difference is what, exactly?"
    z "Someone tells you the Cores are gods, you bow your head and pray. Someone tells you the resistance will win, you pick up a weapon and die."
    z "Same mechanism. Different costume."

    "Lyra turns from the window. Even in the low light, Aeron can see the tension in her shoulders."

    l "You're conflating belief with obedience. They're not the same thing."

    z "Aren't they? You believed in the Order. You obeyed the Order. How'd that work out?"

    "Zira's typing stops."

    athought "The words landed like a slap. She knows it."

    z "(quieter) That was too far. Sorry."

    l "(controlled) No. You're right."
    l "I believed, and I obeyed, and I signed a report that called my dead mentor a heretic."
    l "But that doesn't mean belief itself is the problem."

    z "Then what is?"

    l "Belief without questioning. Faith without... without the willingness to be wrong."

    # VISUAL: Zira swivels in her chair. First time she's actually facing Lyra.
    "Zira turns. Really looks at Lyra for the first time in this conversation."

    z "And you think you've learned that? The willingness to be wrong?"

    l "I'm trying."
    l "I believed the Order was divine. I was wrong."
    l "I believed Marcus was salvation. I was wrong."
    l "But I'm still here. Still believing in something. That has to count."

    z "Believing in what?"

    l "(long pause) ...Him. Us. This."

    z "(snorting) That's not faith, princess. That's attachment."

    l "What's the difference?"

    "Zira doesn't answer immediately. Her hand goes to her ear—the left one, the one she lost hearing in during the breach."

    z "Attachment hurts when it ends. Faith just leaves you empty."

    l "You sound like you're speaking from experience."

    z "I'm speaking from eleven dead runners and a brother who got his head broadcast on every screen in the Unders."
    z "I'm speaking from having faith in a security system I built, watching it fail, and listening to my enclave die through a blown-out eardrum."

    "Silence stretches between them."

    l "(soft) Zira..."

    z "Don't. I don't want pity. I want you to understand why I can't just... believe."
    z "Every time I've believed in something, it's gotten people killed."
    z "So now I believe in data. Patterns. Things I can verify."
    z "The Ghostline doesn't require faith. It requires maintenance."

    l "And Aeron? You brought him into the Ghostline."

    z "That's not faith. That's calculated risk."

    l "You gave him access to six years of your life. You told him about Sera."

    z "(sharp) How do you know about Sera?"

    l "He told me. Last night."

    "Zira's quiet for a long moment."

    athought "Processing."

    z "He told you."

    l "He tells me things. That's how trust works."

    z "(muttering) Great. Now I'm a story."

    l "You're not a story. You're a person who took a risk on someone."
    l "That's faith, Zira. Whether you call it that or not."

    # VISUAL: Zira's posture shifts. Defensive walls cracking slightly.
    "Zira leans back in her chair. Something in her posture loosens."

    athought "Not surrender. Just exhaustion."

    z "Fine. Maybe it's a little bit faith."
    z "But it's faith in him. Not in... I don't know. The universe. Destiny. Some hum in a Core chamber."

    l "That's all I'm asking."
    l "Not that you believe in the gods I grew up with. Just that you believe in something worth fighting for."

    z "I believe in not dying. Does that count?"

    l "(small smile) It's a start."

    z "And people. I believe in some people. A very short list."

    l "How short?"

    z "Counting you? Four."

    l "I made the list?"

    z "Don't let it go to your head. The bar is extremely low."

    "Lyra laughs—soft, surprised. Zira's mouth twitches. Almost a smile."

    l "You know, you're not as cynical as you pretend to be."

    z "And you're not as serene as you pretend to be. We all have our masks."

    l "Maybe that's why he trusts us both."
    l "We're both pretending to be something we're not."

    z "Or we're both trying to become something we're not yet."

    "The words hang in the air. Heavier than Zira probably intended."

    l "(quiet) That might be the most hopeful thing you've ever said."

    z "Don't get used to it. I have a reputation to maintain."

    # ========== AERON ENTERS ==========

    # VISUAL: Aeron at the threshold. He's been listening. They both notice at the same time.
    "He shifts. The bedroll creaks."

    "Both women turn. Caught."

    z "How long have you been awake?"

    a "Long enough."

    l "(flushing slightly) We didn't mean to wake you."

    a "You didn't. I was already awake."

    "He gets up. Moves to join them in the common area of the safehouse."

    if scene_has("act2_09_armor_down", "intimacy_chosen"):
        "Lyra's eyes find his. Something soft passes between them. Zira notices, rolls her eyes."
        z "(muttering) Great. As if being a third wheel wasn't awkward enough."
    else:
        "The space between him and Lyra is still careful. Healing, maybe. But careful."

    a "For the record, I agree with both of you."

    z "That's diplomatically useless."

    a "Faith without data is dangerous. But data without something to fight for is just... numbers."

    l "So which are you?"

    "He thinks about it. Really thinks."

    if empathy_band() == "obedience":
        a "I'm data trying to remember what it was fighting for."
        z "(snorting) Poetic. Tragic. Very on-brand."
    elif empathy_band() == "empathy":
        a "I'm faith trying to learn how to verify itself."
        l "(soft smile) That's more honest than I expected."
    else:
        a "I'm a work in progress."
        z "Aren't we all."

    # ========== CLOSING — DAWN BREAKING ==========

    # VISUAL: First light coming through the window. The gray shifting to pale gold.
    "The light through the window is changing. Gray bleeding into gold."

    "Day five. Sixty-something hours left on the clock Noelle gave them."

    z "Speaking of data—I got a message from Noelle overnight."
    z "She's found a lead on a potential base location. Someone who might be willing to help."

    l "Who?"

    z "Selene Ward. Runs what's left of the organized resistance in the lower sectors."
    z "She's agreed to a meeting. Tomorrow night."

    "The name lands heavy. Selene. The woman who's been fighting while they've been hiding."

    a "What does she want?"

    z "To evaluate you, apparently. See if you're worth the risk."
    z "Noelle vouched for you. Partially. Said you were 'an anomaly worth investigating.'"

    l "That's... almost a compliment."

    z "From Noelle, it's practically a marriage proposal."

    "Aeron looks at Lyra. Then at Zira. Two people who shouldn't trust him, who do anyway."

    athought "Faith and data. Both pointing in the same direction."
    athought "Maybe that's the only proof I'm going to get."

    a "Then we meet Selene. And we see what happens next."

    z "Spoken like a man with no better options."

    a "That too."

    # VISUAL: The three of them, together in the dawn light. Not quite a team yet. But closer.
    "The sun rises over the Unders. Hidden behind kilometers of city, it still finds a way to reach them."

    "Tomorrow, Selene. Tomorrow, the real test."

    "Today, there's just this: three people in a concrete room, learning to trust each other."

    "It's not much. But it's a start."

    # --- SCENE WRAP ---
    $ flag_on("Zira", "lyra_confrontation_resolved")
    $ flag_on("Lyra", "zira_confrontation_resolved")
    $ scene_mark(_current_scene_id, "chapter_2_complete")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_10_static_faith
# cann.chapter: Act II, Chapter II — Constellation
# cann.chapter_start: False
# cann.chapter_end: True — This closes Chapter II
# cann.when_in_timeline:
#   - Early morning, Day 5. Final scene of Chapter II (Constellation).
# cann.what_happened:
#   - Aeron wakes to Lyra and Zira having a tense conversation about faith vs cynicism.
#   - Zira argues hope is vulnerability, weaponized by systems like Echelon and the Order.
#   - Lyra counters that belief without questioning is the problem, not belief itself.
#   - Zira reveals her trauma: the breach, her brother Renn, eleven dead runners.
#   - "Every time I've believed in something, it's gotten people killed."
#   - Lyra points out that giving Aeron Ghostline access was an act of faith.
#   - Zira admits she believes in "some people. A very short list. Counting you? Four."
#   - They reach tentative understanding: both are "trying to become something we're not yet."
#   - Aeron enters, acknowledges both perspectives, defines himself by current path lean.
#   - Zira reveals: Noelle has arranged a meeting with Selene Ward tomorrow night.
#   - Scene closes with dawn light, Chapter II complete.
# cann.aeron_state:
#   - Observer role in this scene—witnesses the Lyra/Zira dynamic.
#   - Brief interaction at end where he positions himself between faith and data based on empathy lean.
# cann.path_tracking:
#   - No empathy choices in this scene—it's a pair scene, Aeron is peripheral.
#   - Callbacks to A2_09 outcome (intimacy chosen or not).
#   - Flags set for Lyra and Zira indicating confrontation resolved.
#   - Running empathy range at scene end: -13 to +3 (unchanged from A2_09).
# cann.thematic_flags:
#   - Core pair dynamic: Faith vs Static (soldier's faith vs hacker's nihilism).
#   - Zira's armor: cynicism as protection after too many losses.
#   - Lyra's evolution: "belief without questioning" was the problem, not belief itself.
#   - "Trying to become something we're not yet" — shared growth thesis.
#   - The "four people" list: Zira's short list of trusted people (including Lyra now).
# cann.alignment_flavor_points:
#   - Aeron's self-definition at end varies by empathy band.
#   - OB: "Data trying to remember what it was fighting for."
#   - EMP: "Faith trying to learn how to verify itself."
#   - Conflicted: "A work in progress."
# cann.character_moments:
#   - Zira: Reveals depth of trauma (breach, Renn, eleven runners). Admits to faith-in-people.
#   - Lyra: Confronts her own history with false belief. Argues for faith that questions itself.
#   - Both: Move from antagonism to mutual recognition. "We all have our masks."
#   - The "four people" list moment is key Zira vulnerability.
# cann.worldbuilding:
#   - Selene Ward mentioned—meeting arranged for tomorrow night.
#   - Noelle vouched for Aeron as "anomaly worth investigating."
#   - Sets up Movement III: Proving Ground.
# cann.block_status:
#   - A2_P06 pair anchor complete. Chapter II (Constellation) complete.
#   - All Act 2 LIs now introduced (Tessa, Zira in depth, Noelle via voice, Selene teased).
# cann.requires_followup:
#   - A2_11: First real operation—Selene meeting or precursor mission.
#   - Lyra/Zira dynamic should reflect this conversation going forward (less tension, more banter).
#   - Zira's "four people" list can be referenced later (who's on it?).
#   - Selene meeting is major next beat—player must prove themselves.
