# =======================================================
# ACT 3 - Scene 15: Chain of Two (Obedience Path)
# File: a3_s15_chain_of_two_ob.rpy
# Path: OB
# Type: ZIRA DEEPENING EROTIC
# Character Focus: Zira, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s15_chain_of_two_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s15_chain_of_two_ob:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a3_s15_chain_of_two_ob")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, handheld with controlled drift (6-8%). The instability is Zira's --
    #         the camera moves the way she feels. Opens mid-action: Zira in the signal bay,
    #         throwing something. Not at Aeron. At the wall. He's in the doorway.
    #         Tightens through confrontation. When vulnerability breaks through:
    #         the drift drops. Close-ups. Her hands, not her face -- Zira's truth is in her hands.
    #         Intimacy: handheld but steady. The drift is gone. She's stopped fighting.
    # LIGHTING: Signal bay: magenta/indigo from terminals. Flickering. Unstable.
    #           The light matches her state. When the confrontation cools: the terminals
    #           stabilize. Steadier glow. Not warm -- stable. That's Zira's version of warm.
    #           Intimacy: terminal glow at standby. Purple-dark. Skin as shadow.
    # SFX: Loop -- Ghostline static, terminal hum, structural creak.
    #      One-shots -- thrown object impact (datapad against wall), chair scrape,
    #      her breathing (hard, angry, then slowing), his boots on the grating.
    #      The three-tap ritual: she does it. Then doesn't. Then does it again.
    # FX/COMP: Signal bay equipment. Multiple screens. Zira's tactical overlays.
    #          One screen showing Nyra's patrol route (she's been tracking her).
    #          The thrown datapad: cracked screen, still displaying.
    # BLOCKING: Zira at her station. She hears him and stands. The confrontation
    #           happens across the console -- physical barrier between them.
    #           The barrier comes down when she moves around it. She initiates.
    # CANON: ZIRA DEEPENING EROTIC. Possessiveness vs. Nyra's presence.
    #        Zira chose Aeron BEFORE the execution. That binds her in ways loyalty doesn't.
    #        She's not sharing command OR him. The confrontation is about ownership.
    #        The vulnerability underneath: she's terrified of being replaced.
    #        Callbacks: a3_s04 (Who Commands Now -- Zira's domain), a3_s06 (Zira's hostility to Nyra).
    # CONSENT: 3-gate framework. Zira's gates are aggressive -- she initiates, demands, then
    #          checks. The check is real. Underneath the aggression, she needs permission.
    # FACE: Zira -- rage dissolving into fear dissolving into need.
    #        Aeron -- the mask holds until it doesn't. What breaks it: her hands shaking.

    # ========= VOICE BASELINE =========
    # OB Aeron: Controlled. He lets her burn. Doesn't match her energy.
    #           When he breaks: it's physical, not verbal. A gesture, not a sentence.
    # Zira: Sharp, confrontational, possessive. Contractions. Street cadence.
    #       She argues the way she codes -- direct, no abstractions. When vulnerable:
    #       shorter sentences. More pauses. The rhythm breaks.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - SIGNAL BAY - NIGHT]
    # Zira's territory. She controls this space. The confrontation happens on her ground.

    #scene bg_signal_bay_ob with dissolve
    #play ambient "sfx/ambient/ghostline_static.ogg" fadein 2.0

    # ========== PHASE 1 -- THE CONFRONTATION ==========

    #play sound "sfx/one_shot/datapad_wall_impact.ogg"

    "The datapad hits the wall before he sees it. The screen cracks but holds -- military hardware, built to survive worse."

    "Zira stands at her console. She threw it without turning. She knew he was there."

    z "Don't."

    a "I haven't said anything."

    z "You were going to say something reasonable. I don't want reasonable."

    athought "She's been tracking Nyra's patrol routes. The overlay is still active on her secondary screen. Timestamps, duration, deviation reports."

    athought "She's not surveilling for the rebellion. She's surveilling for herself."

    a "You're monitoring Nyra."

    z "I'm doing what you told me to do. 'Keep watching her. If you see anything, bring it to me.'"

    a "And?"

    z "And I don't like what I see."

    "She turns. Her eyes are red-rimmed. Not crying -- sleep deprivation and anger. The combination that makes Zira most dangerous."

    z "She's in your quarters."

    athought "She knows."

    a "She reported for a debrief."

    z "At 0200. In your personal quarters. With the door sealed."

    z "I know what a debrief looks like, Aeron. That wasn't one."

    athought "She's right. She's been right about Nyra from the start."

    athought "The question is whether that changes anything."

    a "What do you want me to say."

    z "I want you to say it's tactical. I want you to say she's an asset and you're managing her."

    z "I want you to lie to me well enough that I can believe it."

    a "I won't lie to you."

    z "Then tell me the truth."

    "The signal bay hums. The Ghostline static fills the spaces between words."

    a "She offered an oath. I accepted it."

    z "An oath."

    a "Loyalty pledge. Old Order tradition."

    z "And the part where she stayed until 0430?"

    a "Was the seal."

    "Zira's jaw works. Her hands grip the console edge. The knuckles are white."

    z "I chose you."

    athought "There it is."

    z "Before the execution. Before Selene. Before any of this. I chose you because you were the only person in this operation who saw things clearly."

    z "I ran your comms. I covered your signals. I kept you alive on missions where a single intercepted transmission would have ended you."

    z "I chose you first."

    athought "She's not arguing about Nyra. She's arguing about priority."

    athought "Who has the older claim."

    a "I know."

    z "Do you? Because it doesn't feel like you know. It feels like you know I'm useful."

    z "There's a difference between being chosen and being kept."

    # ========== PHASE 2 -- THE VULNERABILITY ==========

    "The confrontation cools. Not because she's calmer -- because she's run out of anger and hit something underneath."

    "Her hands are still on the console. She's gripping hard enough that her fingers tremble."

    athought "Her hands. Zira's hands never shake."

    athought "I've seen her splice Ghostline relays under fire. I've seen her code decryption algorithms during an air raid."

    athought "Her hands don't shake."

    athought "They're shaking now."

    "He moves. Not toward the console. Around it. She tenses but doesn't retreat."

    z "Don't. Don't do the commander thing where you--"

    a "I'm not."

    "He stops two feet from her. Close enough to reach. Not reaching."

    a "You chose me first. I haven't forgotten."

    z "Then act like it."

    a "What does that look like."

    z "It looks like not replacing me with someone who worships you."

    z "Nyra doesn't see you. She sees a projection. The perfect commander. The worthy leader."

    z "I see you. I see the insomnia and the tremor and the way you flinch when Lyra says Selene's name."

    z "I chose that. Not the image. The mess."

    athought "The mess."

    athought "She's the only one who calls me a mess and means it as a compliment."

    a "I'm not replacing you."

    z "Prove it."

    athought "The same demand. Lyra wants proof of humanity. Zira wants proof of priority."

    athought "The requests are different. The verb is the same."

    # ========== PHASE 3 -- CONSENT GATES ==========

    # --- CONSENT GATE A: Zira initiates ---

    "She moves. Not gently -- Zira doesn't do gently. She crosses the two feet like they offended her."

    "Her hands find his collar. She grips it. Pulls him down to her eye level."

    z "I'm not sharing command. And I'm not sharing you."

    z "You can have your oath-keeper for the mission. But this--"

    "She doesn't finish the sentence. Her mouth finds his."

    "The kiss is a claim. Not a question."

    # --- CONSENT GATE B: He reciprocates ---

    athought "She tastes like black coffee and signal-bay ozone."

    athought "Her hands are still shaking. She's gripping my collar to hide it."

    athought "I let her hide it."

    menu:
        "Her hands on his collar. Her mouth on his. The console hums behind her."

        "Pull her closer.":
            $ choice_and_dev(
                _current_scene_id, "_reciprocate", "OB", factor=1,
                next_scene_label=None,
                note="Full reciprocation. Zira's claim accepted physically."
            )
            jump .intimacy_path

        "Hold her hands. Steady them.":
            $ choice_and_dev(
                _current_scene_id, "_steady", "OB", factor=0,
                next_scene_label=None,
                note="Tenderness over passion. Routes to intimacy through care."
            )
            jump .steady_path

    # --- BRANCH: PULL HER CLOSER ---
    label .intimacy_path:

        "His hands find her waist. Pull. The distance collapses."

        z "(against his mouth) There."

        athought "She said 'there' the way soldiers say 'confirmed.' A target hit."

        # --- CONSENT GATE C: Check ---

        "She pulls back. One inch. Her breath on his mouth."

        z "Tell me to stop and I stop. No questions. No grudge."

        a "Don't stop."

        z "Good answer."

        jump .intimate_sequence

    # --- BRANCH: STEADY HER HANDS ---
    label .steady_path:

        "His hands find hers on his collar. He doesn't remove them. He closes his hands around them."

        "Her fingers stop shaking."

        z "..."

        athought "She stares at our hands. Hers inside mine. The tremor gone."

        z "Don't you dare be tender with me."

        a "Too late."

        z "I hate you."

        a "I know."

        "She exhales. Hard. The anger leaving her body like a ventilated airlock."

        z "Fine. Be tender. But do it properly."

        # --- CONSENT GATE C: Check ---

        z "If you don't want this, say so now. I'll survive."

        a "I want this."

        z "Then stop being careful and start being here."

        jump .intimate_sequence

    # ========== PHASE 4 -- INTIMATE SEQUENCE ==========
    label .intimate_sequence:

        # VISUAL: Signal bay. Terminal glow. The Ghostline static fades to background.
        # Her against the console -- she chose the location. Her territory, her terms.
        # CAMERA: Handheld, steady now. The drift is gone. She's stopped fighting.

        "The signal bay is not built for this. The console is hard-edged. The floor is grating."

        "Zira doesn't care. She's never needed comfort to feel safe -- she needs territory."

        "Her hands are steady now. They move with the same precision she uses on her equipment -- knowing exactly where everything goes, how much pressure to apply."

        athought "She doesn't whisper. She doesn't go soft."

        athought "She tells me what she wants with the directness of someone who has no time for ambiguity."

        z "Here."

        athought "I comply."

        athought "That word should bother me. With Nyra, compliance is doctrine."

        athought "With Zira, compliance is partnership. She demands; I choose. The choosing makes it mine."

        # [INTIMATE CONTENT HERE]

    # ========== PHASE 5 -- AFTERCARE ==========

        # VISUAL: After. The signal bay. Purple-dark.
        # Zira sitting on the floor, back against the console. Aeron beside her.
        # Her head on his shoulder -- a concession she'd deny if anyone saw it.
        # The Ghostline static has returned. Low. Musical almost.
        # CAMERA: Wide. Two figures in the glow. The thrown datapad still on the floor.

        "The signal bay settles. Purple glow from standby terminals. The Ghostline static hums -- lower now, almost musical."

        "Zira is on the floor. Back against the console. Her shoulder against his. Her head tilted to rest against his arm."

        athought "She'd murder anyone who saw this."

        athought "That's how I know it's real."

        z "I meant what I said."

        a "I know."

        z "I'm not sharing. She can have your mission. She can have your orders and your command voice and whatever spiritual warfare she's running."

        z "But this -- the signal bay, the 0300 check-ins, the fact that I know your hand tremors before you do--"

        z "That's mine."

        a "That's yours."

        z "Don't make me regret this. Again."

        athought "Again. She's regretting and choosing simultaneously. That's the most Zira thing possible."

        a "I won't."

        z "You will. But I'd rather regret this than wonder about it."

        "She lifts her head. Looks at him. Her expression is stripped -- no anger, no armor, no performance."

        z "You're a mess. You know that."

        a "You've mentioned it."

        z "I like the mess."

        athought "She puts her head back down. I let her."

        athought "In the morning, she'll be sharp again. Hostile to Nyra. Clinical about the mission. Three-tap ritual on the console before every shift."

        athought "But tonight, her head is on my shoulder, and the Ghostline hums, and for the first time in weeks something in my chest unclenches."

        athought "Not because she made me feel."

        athought "Because she didn't ask me to."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("zira_deepening_intimate", True)
    $ rel_bump("Zira", trust=1, affection=1)
    $ metric("zira_intimacy_level", set_to=max(metric("zira_intimacy_level"), 2))
    $ npc_remember("Zira", "chain_of_two_claimed", tone="possessive_vulnerable")
    $ npc_remember("Zira", "i_chose_you_first", tone="territorial_honesty")
    $ npc_remember("Aeron", "zira_didnt_ask_me_to_feel", tone="relief")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s15_chain_of_two_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After "The Oath" (a3_s12). Zira has been tracking Nyra's movements.
#   - She knows about the 0200 visit. She confronts him in her territory.
# cann.what_happened:
#   - Zira confronts Aeron in the signal bay. She knows about Nyra's visit.
#   - Not about love -- about ownership. "I chose you first."
#   - She's been tracking Nyra's patrol routes. Surveillance as emotional expression.
#   - The confrontation: priority, not jealousy. Who has the older claim.
#   - "I see the mess. I chose the mess." vs. Nyra seeing the projection.
#   - Consent gates: she initiates (aggressive), he reciprocates, she checks (genuine).
#   - Intimate in the signal bay. Her territory. Her terms.
#   - Aftercare: "Don't make me regret this. Again." Vulnerability wrapped in warning.
#   - "Because she didn't ask me to feel." -- relief through acceptance, not demand.
# cann.aeron_state:
#   - OB controlled through the confrontation. What breaks the mask: her hands shaking.
#   - "With Nyra, compliance is doctrine. With Zira, compliance is partnership."
#   - Post-intimate: something unclenches. Not emotion -- pressure release.
# cann.path_tracking:
#   - Reciprocate: rel_bump("Zira", trust=1, affection=1). Intimacy level 2.
#   - Steady hands: same destination, different texture. Tenderness instead of claim.
#   - flag("zira_deepening_intimate"). npc_remembers for both.
# cann.thematic_flags:
#   - Ownership vs. worship: Zira sees the mess, Nyra sees the image.
#     Both are projections. Both are partially true.
#   - "Proof" demanded by three LIs now: Lyra (humanity), Zira (priority), Nyra (worthiness).
#   - Signal bay as Zira's territory: she controls the space. The intimacy on her terms.
#   - "I'd rather regret this than wonder about it." -- Zira's emotional calculus.
#   - The thrown datapad: violence as prelude. Zira's anger IS her vulnerability.
# cann.character_moments:
#   - Zira: "There's a difference between being chosen and being kept." Her thesis.
#     Shaking hands. The thing she can't hide. Aeron steadying them is the act.
#   - Aeron: breaks the mask not through words but through gesture (steadying her hands
#     OR pulling her closer). Physical, not verbal. OB-appropriate vulnerability.
#   - "You're a mess." / "I like the mess." -- Zira's love language.
# cann.block_status:
#   - VARIANT (intimacy always occurs, path affects texture).
#   - Zira deepening on OB path. The jealousy/Nyra thread advances.
# cann.requires_followup:
#   - Zira's surveillance of Nyra: does this escalate or get redirected?
#   - "Don't make me regret this. Again." -- what was the first time she regretted?
#   - The ownership claim: how does this affect poly dynamics on OB?
#   - nudge_poly potential: if player pursues both Nyra and Zira, the tension compounds.
