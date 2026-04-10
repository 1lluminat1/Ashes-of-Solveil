# =======================================================
# ACT 3 - Scene 16: Data and Doubt (Obedience Path)
# File: a3_s16_data_and_doubt_ob.rpy
# Path: OB
# Type: NOELLE FIRST EROTIC + TRUE PATH NAME MECHANIC
# Character Focus: Noelle, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s16_data_and_doubt_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s16_data_and_doubt_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, tripod, micro-adjustments. Opens on the data alcove -- same framing
    #         as EMP s11. But the lamp is off. Screens at full luminance. No concessions.
    #         Tightens through the contradiction logs: Noelle's data projected.
    #         The Name Mechanic: medium close-up, both in frame. Same as EMP.
    #         Consent gates: close-up singles. The camera earns proximity through her logic.
    #         Intimacy: the camera stays analytical. Two people observed under blue light.
    #         The difference from EMP: in EMP, the screens dim. Here, they stay on.
    #         She doesn't turn them off. She wants the record.
    # LIGHTING: Data alcove. Full screen luminance -- blue-white, clinical. No amber lamp.
    #           The lamp is in the alcove but unplugged. Deliberate.
    #           Intimacy: same clinical blue. She doesn't soften the light. The light is data.
    #           She wants to see everything clearly because clarity IS her intimacy.
    #           Aftercare: screens at standby. The blue dims. Not warm -- dimmer. Resting.
    # SFX: Loop -- data alcove ambient at full: crystal resonance, cooling fans, keystrokes.
    #      The hum doesn't fade. She keeps the machines running.
    #      One-shots -- stylus set down, chair shift, the silence when she stops typing.
    #      The silence when she stops typing is the loudest sound in the scene.
    # FX/COMP: Noelle's screens: contradiction logs. Behavioral analysis. His stated doctrine
    #          vs. his observed behavior. Variance charts. The data is about HIM.
    #          The amber lamp unplugged but present. She brought it and didn't use it.
    # BLOCKING: Data alcove. Same two chairs. Same supply crate.
    #           But Noelle has repositioned them -- closer together. An inch. Maybe two.
    #           She measured the optimal distance for data presentation. It happens to be
    #           the distance at which she can reach his wrist.
    # CANON: NOELLE FIRST EROTIC (OB) + TRUE PATH NAME MECHANIC.
    #        OB texture: she's fascinated by the fracture between his doctrine and behavior.
    #        She treats him as her final experiment. The experiment becomes mutual.
    #        Callbacks: a3_s14 (Noelle's Calculus -- the non-reaction), a3_s06 (Noelle's assessment),
    #        EMP s11 (parallel structure -- same beats, different temperature).
    # CONSENT: 3-gate framework. Noelle's OB gates: (A) she frames desire as hypothesis,
    #          (B) he validates the methodology, (C) explicit termination clause.
    # FACE: Noelle -- analytical composure. But the eyes are tracking something the models missed.
    #        Aeron -- the mask. Noelle's presence creates a different kind of crack than the others'.
    #        Not emotional (Lyra). Not possessive (Zira). Not devotional (Nyra).
    #        Intellectual. She sees through the mask by measuring its edges.

    # ========= VOICE BASELINE =========
    # OB Aeron: Clinical. But Noelle's precision creates a resonance with his own.
    #           Two clinical voices in dialogue. The warmth, when it comes, is in the math.
    # Noelle: Full analytical mode. She presents contradiction data the way she presents
    #         any dataset. But the pauses are different. The pauses are where she lives.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - DATA ALCOVE - LATE EVENING]
    # Noelle's workspace. Screens at full luminance. Door closed.
    # The amber lamp is present but unplugged. She brought it. She didn't use it.

    #scene bg_data_alcove_evening with dissolve
    #play ambient "sfx/ambient/data_alcove_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE CONTRADICTION LOGS ==========

    "The door to the data alcove is closed. He knocks."

    n "(from inside) You may enter."

    athought "Not 'identification unnecessary.' Not the familiar shorthand."

    athought "'You may enter.' Formal. She's presenting."

    "The alcove is bright. Every screen active. Crystal arrays at processing load. Noelle in her chair, stylus held like a scalpel."

    "The supply crate is positioned beside her. Closer than usual. He sits."

    n "I've been compiling behavioral variance logs."

    a "On what?"

    n "On you."

    athought "Of course."

    "She activates the projection. Data fills the space between them."

    n "Your stated command doctrine since assuming leadership: efficiency, order, minimal emotional expenditure. Consistent with Glass Academy behavioral conditioning profiles."

    n "Your observed behavior: fourteen documented instances of deviation from stated doctrine in the last thirty days."

    a "Deviation."

    n "Instance one: you approved extended medical leave for Dren when tactical efficiency recommended reassignment. Instance four: you countermanded your own order to restrict civilian access to the east wing after speaking with the children there."

    n "Instance seven: you visited Tessa's medbay at 0400 and sat in the corridor for eleven minutes without entering."

    athought "She knows about that."

    n "Instance twelve: you held the Purge data for two weeks without acting on it. Stated reason: awaiting confirmation. Observed behavioral indicators: elevated resting heart rate, sleep disruption pattern consistent with moral processing, not strategic deliberation."

    athought "Moral processing."

    athought "She's telling me I felt something about my father's signature."

    athought "And that my body registered it even though my face didn't."

    n "You're inefficient in ways you don't acknowledge."

    a "I'm effective."

    n "Yes. But effectiveness and efficiency are not synonyms. You are effective because of the inefficiencies, not despite them."

    n "Your stated doctrine doesn't match your behavioral output. The variance is consistent, measurable, and -- crucially -- always in the direction of human consideration over pure optimization."

    athought "She's building a case. Not against me. For something."

    athought "I'm not sure what yet."

    n "My conclusion: the Glass identity is an operational framework, not a psychological truth. The person underneath deviates from the framework at consistent intervals."

    n "The deviations are what make you functional. Not the doctrine."

    a "That's your analysis."

    n "That's my data."

    # ========== PHASE 2 -- THE NAME MECHANIC ==========

    "She sets her stylus down. The click against the desk is precise."

    n "Which brings me to nomenclature."

    athought "The same word. The same starting point."

    athought "In the other-- in a different context, this would be warm. A threshold."

    athought "Here it's a scalpel. She's excising something."

    n "My data calls you Glass. Echelon calls you traitor. Nyra calls you Commander. Zira calls you useful."

    n "Your behavioral output doesn't match any of these labels."

    n "What are you?"

    # NAME MECHANIC: Invisible text field below menu choices.
    # IMPLEMENTATION: Identical to EMP s11.
    # No border, no background, no visible cursor until hovered.
    # Cursor changes to I-beam on hover (ONLY hint).
    # Field accepts only A/a, E/e, R/r, O/o, N/n in sequence.
    # When "aeron" (case-insensitive) is complete, menu dissolves.
    # $ tp_name_typed(_current_scene_id)
    # $ flag("tp_name_typed", True)

    menu:
        "She waits. The screens hum. The data about him floats in the air between them."

        "I'm Glass. I'm what they made me.":
            $ choice_and_dev(
                _current_scene_id, "_glass_identity", "OB", factor=1,
                next_scene_label=None,
                note="OB-coded: accepts inherited identity. Noelle rejects the label."
            )
            $ record_choice_once(_current_scene_id, "_glass_identity")
            jump .glass_response

        "I'm trying to be something better.":
            $ choice_and_dev(
                _current_scene_id, "_becoming_better", "EMP", factor=1,
                next_scene_label=None,
                note="EMP-coded: identity as process. Noelle interrogates the metric."
            )
            $ record_choice_once(_current_scene_id, "_becoming_better")
            jump .better_response

    # --- TRUE PATH: NAME TYPED ---
    label .name_typed:

        $ tp_name_typed(_current_scene_id)
        $ flag("tp_name_typed", True)

        a "I'm Aeron."

        "The name in the alcove. Among the data. Between the screens."

        n "(pause) That designation isn't in any of my behavioral models."

        a "I know."

        n "It doesn't correspond to Glass conditioning, rebellion identity frameworks, or any operational alias in my records."

        a "I know."

        n "(longer pause) It does, however, correlate with the deviation pattern."

        athought "She's processing. Not the word -- the act. That I chose a name that isn't assigned."

        n "The deviations in your behavior -- the inefficiencies that make you functional -- those are consistent with someone named Aeron."

        n "They are not consistent with someone named Glass."

        athought "She just validated it. Not emotionally. Through data."

        athought "That's worth more than any declaration."

        n "(very quiet) Aeron."

        "She says it like she's integrating a new variable into every model she's ever built."

        jump .post_identity

    # --- BRANCH: GLASS IDENTITY ---
    label .glass_response:

        a "I'm Glass. I'm what they made me."

        n "Incorrect."

        a "That's not a hypothesis you can reject."

        n "It's a claim that contradicts the evidence. I've just shown you fourteen instances of behavioral deviation from Glass conditioning."

        n "You're not what they made you. You're what you do when the conditioning fails."

        athought "She says 'conditioning fails' the way mechanics say 'the part wore out.' Factual. Inevitable."

        athought "Not a criticism. A description."

        jump .post_identity

    # --- BRANCH: BECOMING BETTER ---
    label .better_response:

        a "I'm trying to be something better."

        n "Define your metric."

        a "I don't have one."

        n "Then how do you measure progress?"

        athought "She's not being rhetorical. She genuinely wants the methodology."

        a "I don't."

        n "Interesting. You're pursuing improvement without a measurement framework. That's the most human thing I've ever observed you do."

        n "Most human processes don't have metrics. They have direction."

        athought "Direction without measurement. She makes it sound almost sustainable."

        jump .post_identity

    # ========== PHASE 3 -- THE SHIFT ==========
    label .post_identity:

        "The data still floats between them. Fourteen deviations charted in blue light."

        "Noelle's hand moves. Toward the projection. She dismisses it."

        "The data disappears. The alcove is darker. Just the screen ambient and two people."

        n "I have one more observation."

        a "Go ahead."

        n "You fascinate me."

        athought "She says it without emphasis. The way she says 'the variance is three percent' or 'the signal integrity is degraded.'"

        athought "A data point. Delivered as one."

        athought "Except her pulse is visible at her throat. Slightly elevated."

        n "I've analyzed two hundred and fourteen individuals since joining Phoenix. I've modeled their behavioral patterns with an average accuracy of ninety-one percent."

        n "Your accuracy is sixty-three percent. The lowest in my dataset."

        n "You are my largest prediction error."

        n "I want to understand why."

        athought "She's framing desire as scientific inquiry."

        athought "The framing is genuine. That's what makes it Noelle."

        n "I want to observe every variable."

        "Her hand moves. From the dismissed projection space to the edge of his wrist. Her fingertips rest on his pulse point."

        athought "Same gesture as-- as another version of this."

        athought "But the pressure is different. She's not gathering data. She's confirming a hypothesis she already formed."

        n "Elevated. Twelve beats above your current baseline."

        a "You're measuring."

        n "I'm always measuring."

        n "The difference is that I'm currently aware the measurement is contaminated by the observer."

        athought "The observer effect. Again. Her framework for intimacy."

        athought "Except on OB, the contamination isn't a bug. It's the experiment."

    # ========== PHASE 4 -- CONSENT GATES ==========

        # --- CONSENT GATE A: Hypothesis framed ---

        n "I would like to conduct an extended observation."

        a "Clarify."

        n "Physical proximity. Reduced distance. The variables I can't model from across the alcove."

        n "The technical term for what I'm proposing is -- is --"

        "She stops. Her stylus hand flexes. The nervous gesture of someone whose vocabulary has failed."

        n "I don't have a clinical term for it. That's the first time that's happened."

        athought "Noelle without a term. The world tilts."

        # --- CONSENT GATE B: Methodology validated ---

        a "You don't need a term."

        "He turns his wrist. Her fingers slide from the pulse point to his palm. His hand closes around hers."

        n "You're validating the methodology."

        a "I'm holding your hand."

        n "Those are the same thing."

        # --- CONSENT GATE C: Termination clause ---

        n "If the results are uncomfortable for either subject, the observation terminates. No data loss. No consequence."

        a "Agreed."

        n "And you should know -- I will remember everything. I remember everything."

        a "I'm counting on it."

        "She stands. The space closes. Her forehead against his chin. She's shorter than him by four inches -- she calculated that once."

        n "The screens are staying on."

        a "I know."

        n "I want to see clearly."

        athought "Clarity IS her intimacy."

        athought "She doesn't want darkness or softness or ritual."

        athought "She wants data. She wants to observe and be observed."

        athought "She wants evidence that this is happening."

        # NAME-TYPED VARIANT
        if flag("tp_name_typed"):
            n "(very quiet) Aeron."
            a "Yes."
            n "That name has a better phonetic correlation with elevated heart rate response than any alias."
            athought "That's Noelle for 'I like saying it.'"

        # [INTIMATE CONTENT HERE]

    # ========== PHASE 5 -- AFTERCARE ==========

        # VISUAL: Later. The alcove. Screens at standby -- dim, not dark.
        # Noelle on the floor, back against the wall. Aeron beside her.
        # Her shoulder against his arm. Her hand holding his wrist -- still measuring.
        # The lamp is still unplugged. She didn't need it.
        # CAMERA: Wide. Blue-dim. Two figures at the base of the machines.

        "The screens pulse at standby. The crystal arrays have cooled. The alcove is blue-dim."

        "They're on the floor. Her back against the wall, his beside hers. Her fingers on his wrist. Still there."

        athought "She hasn't let go. She's still reading my pulse."

        athought "I don't think she's doing it for data anymore."

        n "I should document this."

        a "Will you?"

        n "Yes."

        athought "Different from EMP. There, she wouldn't. Here, she will."

        athought "Because on this path, the record is the relationship. Observation is how she loves."

        n "I'll document it accurately. Which means I'll document the part where my prediction models failed completely."

        a "How completely?"

        n "I predicted a sixty-three percent behavioral accuracy for you. Tonight's data brings it to forty-one."

        n "You are my final experiment. I intend to observe every variable."

        athought "Final experiment."

        athought "She's not saying 'only.' She's saying 'last.' The experiment after which the methodology changes."

        athought "The experiment that changes the experimenter."

        # NAME-TYPED AFTERCARE VARIANT
        if flag("tp_name_typed"):

            "She lifts her head."

            n "Aeron."

            athought "The third time she's said it. Each time with less analysis and more ownership."

            n "Your name functions as a superior identifier. It distinguishes you from the models."

            athought "That's Noelle for 'you're more than what I can measure.'"

            athought "Which is the most she's ever said to anyone."

        "The screens pulse. Standby rhythm. Machine breathing."

        "Her fingers on his wrist. His pulse settling. Hers alongside it."

        "Two rhythms. Not synchronized -- parallel. Running the same direction at their own speeds."

        athought "She'll document everything. That's her version of keeping."

        athought "And I'll let her. Because being measured by Noelle is the closest thing to being known that this path allows."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Noelle", trust=1, affection=2)
    $ flag("noelle_first_intimate", True)
    $ metric("noelle_intimacy_level", set_to=max(metric("noelle_intimacy_level"), 1))
    $ npc_remember("Noelle", "first_intimate_data_alcove_ob", tone="experimental_fascination")
    $ npc_remember("Noelle", "screens_stayed_on", tone="deliberate_clarity")
    $ npc_remember("Noelle", "prediction_accuracy_forty_one_percent", tone="thrilled_failure")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s16_data_and_doubt_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After "Noelle's Calculus" (a3_s14). She's been compiling contradiction data.
#   - Late evening. Data alcove. Door closed.
# cann.what_happened:
#   - Noelle presents contradiction logs: 14 instances where OB Aeron deviated from doctrine.
#   - "You're inefficient in ways you don't acknowledge." The inefficiencies make him functional.
#   - Name Mechanic embedded: same as EMP s11.
#     "I'm Glass" -- she rejects: the data contradicts the label.
#     "Trying to be better" -- she interrogates: what's the metric?
#     TRUE PATH: "I'm Aeron" -- she integrates: the deviations correlate with the name.
#   - "You are my largest prediction error." -- 63% accuracy, her lowest.
#   - Consent gates: hypothesis (proximity observation), methodology (he holds her hand),
#     termination clause (explicit exit). "The screens are staying on."
#   - Intimacy in blue light. Screens on. She wants clarity, not softness.
#   - Aftercare: "You are my final experiment. I intend to observe every variable."
#     She WILL document this (unlike EMP). The record IS the relationship.
# cann.aeron_state:
#   - OB clinical, but Noelle's precision resonates with his own. Two clinical voices.
#   - The data about his deviations: he didn't know about some of them (the 0400 medbay visit).
#   - "Being measured by Noelle is the closest thing to being known that this path allows."
# cann.path_tracking:
#   - Glass identity: OB factor=1. Noelle corrects: label vs. evidence.
#   - Becoming better: EMP factor=1. Noelle interrogates: direction without metric.
#   - TRUE PATH: tp_name_typed(). "The deviations correlate with the name."
#   - All paths: rel_bump("Noelle", trust=1, affection=2). flag("noelle_first_intimate").
# cann.thematic_flags:
#   - EMP s11 parallel: same beats, different temperature. Screens on vs. off.
#     EMP: she goes off-record. OB: she keeps the record. Both are Noelle.
#   - "You're inefficient in ways you don't acknowledge" -- the OB version of "I see you."
#   - The contradiction logs as love letter: she documented his humanity.
#   - "Clarity IS her intimacy" -- the OB Noelle thesis.
#   - Prediction accuracy dropping from 63% to 41%: she's thrilled by failure.
#     The failure means he's more complex than her models. That's her desire.
#   - The unplugged lamp: she brought warmth and didn't use it. The gesture of having it matters.
# cann.character_moments:
#   - Noelle: "I don't have a clinical term for it." -- vocabulary failure as threshold.
#     "The screens are staying on. I want to see clearly." -- Noelle's consent language.
#     She'll document everything. Documentation IS her keeping.
#   - Aeron: "I'm counting on it." -- accepts being observed. On OB, this is intimate.
#   - TP variant: "That name has a better phonetic correlation with elevated heart rate response."
#     Noelle's body responds to his real name. The data doesn't lie.
# cann.block_status:
#   - MAJOR SCENE. Noelle first erotic (OB) + True Path Name Mechanic.
#   - The Name Mechanic is a REQUIRED TP moment (1 of 3 mandatory).
# cann.requires_followup:
#   - Noelle's documentation: what does the log say? How does she frame it?
#   - The 14 deviations: do they increase or decrease as OB deepens?
#   - "Final experiment" -- when does the methodology actually change?
#   - Prediction accuracy as tracking metric: does it keep dropping?
#   - The unplugged lamp: does she plug it in eventually? That's the arc.
