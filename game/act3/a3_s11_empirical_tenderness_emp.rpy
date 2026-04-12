# =======================================================
# ACT 3 - Scene 11: Empirical Tenderness (Empathy Path)
# File: a3_s11_empirical_tenderness_emp.rpy
# Type: NOELLE FIRST EROTIC + TRUE PATH NAME MECHANIC
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s11_empirical_tenderness_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s11_empirical_tenderness_emp:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("noelle_korr", to_stage=2, source="a3_s11_empirical_tenderness_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, tripod, micro-adjustments only. Opens wide on the data alcove —
    #         Noelle's domain, her screens and crystal arrays — then slowly tightens
    #         across the scene. By the name mechanic: medium close-up, both in frame.
    #         By the consent gates: close-up singles, alternating. The camera EARNS
    #         proximity the way the characters do.
    # LIGHTING: Cool data-blue from screens as base layer. A single warm practical
    #           (amber desk lamp, 2700K) that Noelle turns on "for the unrecorded minute."
    #           The warm light grows dominant as the scene progresses — data-blue receding.
    #           By intimacy: the screens have dimmed to standby. Only the lamp.
    # SFX: Loop — data alcove ambient: crystal resonance hum, cooling fans, soft keystrokes.
    #       The hum FADES as the scene deepens. By the name mechanic, near silence.
    #       One-shots — chair shift, stylus set down, breath catch, fabric rustle.
    # FX/COMP: Noelle's screens showing analysis patterns — predictive models, behavioral
    #          maps. They go to standby one by one as she stops working. The last screen
    #          dims when she reaches for his hand.
    # BLOCKING: Data alcove. Two chairs. Close quarters by design — it's a workspace,
    #           not a bedroom. The intimacy of small spaces. Noelle in her chair, turned
    #           to face him. Aeron on the supply crate she cleared for him.
    # CANON: MAJOR SCENE. Noelle's first erotic + True Path Name Mechanic.
    #        Callback: A2_P05 "unrecorded minute" — Noelle turned off logging for 60 seconds.
    #        The Name Mechanic is the single most important TP moment in the game.
    # FACE: Noelle — analytical composure dissolving at the edges. The moment her hand
    #        moves to his is the moment the model breaks. She knows it. She does it anyway.
    #        Aeron — still. Watchful. The particular tension of someone being SEEN by
    #        a person who sees everything.

    # ========= VOICE BASELINE =========
    # EMP cadence. Noelle's analytical precision is the surface; the emotional current
    # runs underneath and breaks through in the pauses, not the words.
    # Aeron is quieter here than in any other LI scene. Noelle needs space to arrive.
    # The shift from data-language to body-language is the scene's spine.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - DATA ALCOVE - LATE EVENING]
    # Noelle's workspace. Screens in soft blue standby. One amber lamp.
    # The door is closed. That's unusual — Noelle works with the door open.

    #scene bg_data_alcove_evening with dissolve
    #play ambient "sfx/ambient/data_alcove_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE INVITATION ==========

    "The door to the data alcove is closed. Aeron almost doesn't knock."

    athought "Noelle works with the door open. Always. She says closed doors create informational bottlenecks."

    athought "So either something is wrong, or something is different."

    "He knocks."

    n "(from inside) Identification unnecessary. Your cadence is distinctive."

    athought "She can identify me by the rhythm of my knock."

    athought "I don't know whether to be flattered or unsettled."

    "The door opens. Noelle is seated at her workstation, but the screens are dimmed. Not off — dimmed. Standby mode. The amber desk lamp is on."

    n "Come in. Close the door."

    "He does."

    n "Sit."

    "She gestures to the supply crate beside her chair. The one she cleared of data crystals two weeks ago and never refilled."

    athought "She's been keeping a seat for me."

    athought "That's not a data point she'd want me to notice. So I don't mention it."

    "He sits. The alcove is small. His knee is six inches from hers."

    n "I have a proposal."

    a "I'm listening."

    n "During our initial extended interaction — the A2 behavioral assessment — I implemented an unrecorded minute. Sixty seconds of unlogged interaction."

    a "I remember."

    n "I would like to repeat the protocol."

    "She pauses. Her stylus taps the desk once. Twice. A rhythm he's learned to read as Noelle processing something that doesn't fit her models."

    n "But this time, I would like to extend it."

    a "How long?"

    n "Indefinitely."

    athought "She says it the way she reports data margins. Flat. Precise."

    athought "But her stylus has stopped tapping."

    a "You want to go off the record."

    n "I want to go off the record."

    "She reaches for the last active screen. Her finger hovers over the standby toggle."

    n "All of it. Every sensor in this alcove. Every log. Every passive recording subroutine."

    n "I want there to be no data between us. Just observation."

    "She presses the toggle. The screen dims. The ambient hum drops — the cooling fans spinning down, the crystal resonance fading to nothing."

    "Silence. The lamp. Two people in a small room."

    n "There. We're unrecorded."

    # ========== PHASE 2 — THE NAME MECHANIC ==========

    athought "The silence is different without the machines. Fuller. The way a room sounds when you remove the white noise you didn't know was there."

    "She turns her chair to face him fully. Her knees are close to his now. Not touching. Close."

    n "I've been thinking about nomenclature."

    a "Nomenclature."

    n "What we call things. The gap between a label and an identity."

    "She looks at him with the focus she usually reserves for anomalous datasets."

    n "My data calls you Glass. Echelon calls you traitor. Zira calls you useful."

    "A pause. She tilts her head."

    n "What are you?"

    # NAME MECHANIC: Invisible text field below menu choices.
    # No border, no background, no visible cursor until hovered.
    # Cursor changes to I-beam on hover (ONLY hint).
    # Field accepts only A/a, E/e, R/r, O/o, N/n in sequence.
    # When "aeron" (case-insensitive) is complete, menu dissolves.
    # $ tp_name_typed(_current_scene_id)
    # $ flag("tp_name_typed", True)

    menu:
        "She waits. The lamp flickers once. The room holds its breath."

        "I'm Glass. I'm what they made me.":
            $ choice_and_dev(
                _current_scene_id, "_glass_identity", "OB", factor=1,
                next_scene_label=None,
                note="OB-coded: accepts inherited identity. The label as the self."
            )
            $ record_choice_once(_current_scene_id, "_glass_identity")
            jump .glass_response

        "I'm trying to be something better.":
            $ choice_and_dev(
                _current_scene_id, "_becoming_better", "EMP", factor=1,
                next_scene_label=None,
                note="EMP-coded: identity as process rather than assignment."
            )
            $ record_choice_once(_current_scene_id, "_becoming_better")
            jump .better_response

    # --- TRUE PATH: NAME TYPED ---
    # This label is jumped to by the custom screen when "aeron" is typed
    # in the invisible text field, dissolving the menu.
    label .name_typed:

        $ tp_name_typed(_current_scene_id)
        $ flag("tp_name_typed", True)

        a "I'm Aeron."

        "The name sits in the air between them."

        "Not a rank. Not a callsign. Not a label someone else applied."

        n "(long pause) ...That's not in any of my models."

        a "Good."

        athought "It's the first time I've said it like it means something."

        athought "Not a fact. An act."

        n "(very quiet) Aeron."

        "She says it like she's running it through every framework she has and finding that none of them contain it."

        n "That's... a much better variable name than 'anomaly.'"

        athought "She almost smiles. Not quite. But the architecture of her face shifts — the analytical mask relaxing at the jaw, the eyes softening by fractions."

        athought "She heard it. Not the word. The weight."

        jump .post_identity

    # --- BRANCH: GLASS IDENTITY ---
    label .glass_response:

        a "I'm Glass. I'm what they made me."

        "She studies him. The analytical focus sharpening."

        n "That's a label, not an answer."

        a "Maybe that's all I have."

        n "Insufficient data. I've observed you make fourteen decisions in the last month that directly contradict Glass Academy behavioral conditioning."

        n "You are not what they made you. You are what you are making yourself."

        athought "She says it like a correction on a technical paper."

        athought "It lands like something else entirely."

        jump .post_identity

    # --- BRANCH: BECOMING BETTER ---
    label .better_response:

        a "I'm trying to be something better."

        n "Better than what?"

        a "Than what they designed me to be."

        n "'Better' implies a metric. A scale with endpoints."

        "She pauses."

        n "I think what you mean is 'different.' Not on the same axis. A new variable entirely."

        athought "She's right. She usually is."

        athought "The precision of it should feel clinical. It doesn't."

        athought "It feels like being understood in a language I didn't know I was speaking."

        jump .post_identity

    # ========== PHASE 3 — THE SHIFT ==========
    label .post_identity:

        "The silence settles. The lamp hums."

        "Noelle's hand moves. Not toward her keyboard. Not toward her stylus."

        "Toward him."

        "Her fingers find the edge of his wrist. Rest there. The contact is light — data-gathering pressure, the touch of someone who reads the world through measurement."

        athought "Her fingertips are on my pulse point."

        athought "She knows exactly what she's doing. She's reading my heart rate through skin contact."

        athought "What she doesn't know — what I can see in the slight widening of her eyes — is that hers just spiked too."

        n "Your resting pulse is elevated."

        a "I noticed."

        n "By approximately twelve beats per minute above your baseline."

        a "You have my baseline memorized?"

        n "I have everyone's baseline memorized. Yours was the most difficult to establish because it fluctuates with proximity to—"

        "She stops."

        athought "She was about to say 'me.'"

        athought "Noelle, who has a model for everything, just ran into the edge of one."

        "Her fingers are still on his wrist. She hasn't pulled away."

        n "I'm experiencing a modeling failure."

        a "What kind?"

        n "The kind where the observer's presence alters the data she's trying to collect."

        n "I can't measure your response to me without my own response contaminating the sample."

        athought "She's describing the observer effect. The quantum mechanical principle that measurement changes the thing being measured."

        athought "She's also describing something much simpler than that."

        a "Noelle."

        n "Yes."

        a "You can stop measuring."

        "Her breath catches. Small. The kind of involuntary response her models would flag as statistically significant."

        n "I don't know how to do that."

        a "I know."

        "He turns his wrist. Slowly. So that her fingers slide from his pulse point into his palm."

        "Her hand in his."

        athought "She looks at our hands like they're a dataset she's never encountered."

        athought "Then she looks at me."

        athought "And for the first time since I've known her, Noelle stops processing."

        n "This is the part I don't have a model for."

        a "This is the part where you don't need one."

    # ========== PHASE 4 — CONSENT GATES ==========

        # CONSENT GATE A: Noelle's verbal cue (intellectual frame for physical desire)

        "She exhales. Controlled. The analyst's breath — four counts in, six counts out."

        "It doesn't work. Her breathing stays uneven."

        n "I would like to gather empirical data on something."

        a "On what?"

        n "Proximity. The effect of reduced spatial distance on — on —"

        "She falters. Noelle, who has never faltered on a sentence in his presence."

        n "On this. Whatever this variable is."

        athought "She's asking. In her language. With her framework."

        athought "I hear it."

        # CONSENT GATE B: Aeron's reciprocal (matching intent)

        "He leans forward. Not far. An inch. Enough to halve the distance between them."

        a "I'd like that too."

        "Her eyes track the movement. Calculating distance. Then stopping mid-calculation."

        n "You would?"

        a "I would."

        athought "Her hand tightens in mine. Not much. The pressure of someone holding on to something she's decided to trust."

        # CONSENT GATE C: Explicit exit acknowledged

        n "If this is uncomfortable for either of us—"

        a "Then we stop. No data required."

        n "No data required."

        "She repeats it like she's testing the shape of the words. A sentence that shouldn't make sense in her framework."

        "It does anyway."

        n "Aeron — or, Glass — or—"

        # NAME-TYPED VARIANT: If the True Path name was given
        if flag("tp_name_typed"):
            a "(quiet) Aeron. You can use it."
            n "Aeron."
            "She says it carefully. Like a hypothesis she's committing to."

        a "Come here."

        "She stands from her chair. The space between them closes. Not rushed. Deliberate. The way she does everything — with full awareness of each variable, each consequence."

        "Except this time the variables have stopped mattering."

        "Her hands find his shoulders. His find her waist. The lamp throws their shadows long against the far wall."

        athought "Her forehead against mine. Her breath on my mouth."

        athought "She smells like crystal coolant and black tea and something underneath that's just her."

        "She kisses him first. Precise. Brief. Testing."

        "Then again. Less precise. Longer."

        athought "The analysis breaks down. I can feel it happening — the moment where her body stops consulting her brain and starts making its own decisions."

        athought "Mine did the same thing two minutes ago. I just didn't tell her."

        # [INTIMATE CONTENT HERE]

    # ========== PHASE 5 — AFTERCARE ==========

        # VISUAL: Later. The lamp still on. Both seated on the floor of the alcove,
        # backs against the wall. Her shoulder against his. His hand around her wrist —
        # not gripping. Resting. Two pulse points touching.
        # CAMERA: Wide enough to hold them both. Still. No movement.

        "The floor of the data alcove is not comfortable. Neither of them moves."

        "Her shoulder against his. His thumb tracing slow circles on the inside of her wrist."

        athought "Her pulse has settled. Mine hasn't. Not quite."

        n "I should document this."

        a "Please don't."

        n "I wasn't going to. That's the problem."

        athought "She says 'problem' the way other people say 'miracle.'"

        "She's quiet for a while. Her breathing evens out. The screens stay dark."

        n "I have no unit for this."

        "He waits."

        n "Every significant experience I've had can be quantified. Catalogued. Cross-referenced against a model."

        n "This one refuses to be measured."

        "She turns her head. Her cheek against his shoulder."

        n "I don't need one."

        athought "Four words. The most unscientific thing Noelle has ever said."

        athought "They mean more than anything in her database."

        # NAME-TYPED AFTERCARE VARIANT
        if flag("tp_name_typed"):

            "She lifts her head. Looks at him."

            n "Aeron."

            athought "Not 'Captain.' Not 'Glass.' Not the clinical distance of a label."

            athought "Just my name. Said like it belongs to someone she wants to keep saying it to."

            a "Yeah?"

            n "Your name has a better phonetic profile than any of your aliases."

            athought "That's Noelle for 'I like saying it.'"

            a "Say it again."

            n "Aeron."

            "Quieter this time. Almost private. A word she's folding into her permanent vocabulary."

        "The lamp flickers. Steadies."

        "Neither of them reaches for the screens."

        #stop ambient fadeout 3.0
        #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Noelle", trust=1, affection=2)
    $ flag("noelle_first_intimate", True)
    $ metric("noelle_intimacy_level", set_to=max(metric("noelle_intimacy_level"), 1))
    $ npc_remember("Noelle", "first_intimate_data_alcove", tone="unmodeled_warmth")
    $ npc_remember("Noelle", "went_off_record_for_aeron", tone="deliberate_vulnerability")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s11_empirical_tenderness_emp
# cann.chapter: Act III, Phase II — Deepening (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase II. After corridor operation and Echelon strikes back.
#   - Noelle invites Aeron to the data alcove. Door closed — unprecedented.
#   - Callback: A2_P05 "unrecorded minute" — extended to indefinite.
# cann.what_happened:
#   - Phase 1 (Invitation): Noelle proposes repeating the "unrecorded minute" but
#     extending it indefinitely. She shuts down all logging. "No data between us."
#   - Phase 2 (Name Mechanic): Noelle asks "What are you?" Three paths:
#       "I'm Glass" (OB-coded) — she corrects him: label vs. identity.
#       "I'm trying to be something better" (EMP-coded) — she reframes: better vs. different.
#       TRUE PATH: Player types "aeron" in invisible field. "That's not in any of my models."
#       "That's a much better variable name than 'anomaly.'"
#   - Phase 3 (The Shift): Noelle reaches for his hand. Pulse-point contact.
#     "I'm experiencing a modeling failure." Observer effect as intimacy metaphor.
#     "You can stop measuring." / "I don't know how to do that."
#   - Phase 4 (Consent Gates):
#       Gate A: "I would like to gather empirical data on proximity."
#       Gate B: Aeron halves the distance. "I'd like that too."
#       Gate C: "If this is uncomfortable..." / "Then we stop. No data required."
#   - Phase 5 (Aftercare): Floor of the alcove. Pulse-point to pulse-point.
#     "I have no unit for this. I don't need one."
#     TP variant: She uses his name. "Aeron." First non-clinical address.
# cann.aeron_state:
#   - Quieter than in any other LI scene. Noelle needs space to arrive at her own pace.
#   - "You can stop measuring." — He understands her framework well enough to speak inside it.
#   - The name mechanic: saying "I'm Aeron" is an act, not a fact.
# cann.path_tracking:
#   - Glass identity: OB factor=1, record_choice_once.
#   - Becoming better: EMP factor=1, record_choice_once.
#   - TRUE PATH: tp_name_typed() fires. flag("tp_name_typed"). Aftercare variant unlocked.
#   - All paths: rel_bump("Noelle", trust=1, affection=2). flag("noelle_first_intimate").
#   - metric("noelle_intimacy_level") set to at least 1.
# cann.thematic_flags:
#   - "Unrecorded minute" callback — intimacy as the absence of surveillance.
#   - Observer effect: measurement changes the thing being measured.
#     Applied to relationships: you can't study someone without being changed by them.
#   - "I have no unit for this. I don't need one." — Noelle's thesis.
#     The most unscientific sentence she's ever spoken. The truest thing she's said.
#   - The Name Mechanic as identity-as-act: not discovered but declared.
#   - Data-blue receding, amber growing: visual metaphor for analysis yielding to feeling.
# cann.character_moments:
#   - Noelle: "Modeling failure" as the moment she lets herself feel.
#     Her consent language is her own — "empirical data on proximity" IS desire,
#     expressed in the only framework she trusts. The framework breaks. She stays.
#   - Aeron: "You can stop measuring" — meeting her where she is and opening the door.
#     He doesn't push. He waits. The patience learned from being patient with himself.
#   - TP variant: "Aeron" replacing "Glass" or "Captain" in Noelle's vocabulary.
#     A phonetic preference that is actually a declaration of intimacy.
# cann.callbacks:
#   - A2_P05: Unrecorded minute — the precedent. Extended here to indefinite.
#   - a3_s07: Noelle's "6% prediction error" — "the parts of you that aren't Glass."
#     Here: the parts of HER that aren't analyst.
#   - a3_s04a: The Silence — Aeron finding his own voice.
#     Here: Aeron finding his own NAME.
# cann.block_status:
#   - MAJOR SCENE. Noelle first erotic + True Path Name Mechanic.
#   - The Name Mechanic is a REQUIRED TP moment (1 of 3 mandatory for activation).
# cann.requires_followup:
#   - Noelle using "Aeron" vs. "Glass" in future scenes (if TP name typed).
#   - The "off-record" state of the alcove — does she turn logging back on?
#   - "No unit" as a recurring Noelle intimacy marker.
#   - Intimacy level progression in subsequent scenes.
#   - Observer effect as ongoing metaphor for their relationship.
