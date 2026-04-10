# =======================================================
# ACT 3 - Scene 08: The Unmeasurable (Empathy Path)
# File: a3_s08_the_unmeasurable_emp.rpy
# Type: PAIR ANCHOR (A3_P09: Lyra x Noelle)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s08_the_unmeasurable_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s08_the_unmeasurable_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, steady dolly. Opens from Aeron's POV in the doorway — wide on the analysis
    #         alcove. Tightens to two-shots of Lyra and Noelle as the experiment begins.
    #         During the breathing exercise: slow push on Noelle's face. Her expressions are
    #         the seismograph. Lyra stays in soft focus — felt, not studied.
    #         Aeron never enters the frame during the core sequence.
    #         Returns to his POV only at the bookend close.
    # LIGHTING: Noelle's alcove: cool blue from crystal displays, silver instrument glow.
    #           When Lyra begins the exercise: a gradual warmth intrudes — amber from the
    #           corridor behind her, catching dust motes. The two temperatures coexist.
    #           During the unmeasurable moment: instruments flicker. The crystal dims 2%.
    #           Not failure — absence of signal where signal should be.
    # SFX: Loop — crystal hum, data processing ticks, ventilation. Clinical.
    #      During exercise: breath. Two sets. Lyra's leading, Noelle's following.
    #      The crystal ticks slow, stutter, pause. Resume at a different rhythm.
    #      One-shots — stylus set down, chair creak, Noelle's sharp inhale.
    # FX/COMP: Crystal displays showing biometric overlays — heart rate, galvanic response,
    #          neural coherence estimation. During the exercise, one readout flatlines
    #          then returns. Not death — the sensor losing the thread.
    # BLOCKING: Noelle's analysis alcove. Noelle in her chair, instruments arrayed.
    #           Lyra standing, then kneeling in front of her. Close proximity.
    #           Aeron in the doorway. He leans against the frame. Doesn't cross the threshold.
    # CANON: PAIR ANCHOR (Lyra x Noelle). This is their scene. Aeron peripheral.
    #        Callbacks: a3_s05 (Two Healers — Lyra's ritual precision established),
    #        a2_s08 (The Analyst — Noelle's data-first epistemology),
    #        a3_s07 (Echelon Strikes Back — Noelle's "6% he missed" insight).
    # FACE: Noelle — clinical composure fracturing into bewilderment. Not distress — wonder
    #        she doesn't have a category for. Her eyes widen once during the exercise.
    #        Lyra — still. Centered. The focus of someone who has done this ten thousand times.
    #        Aeron — quiet recognition. He sees what's happening before they name it.

    # ========= VOICE BASELINE =========
    # EMP cadence: present, sensory, contractions allowed.
    # Noelle: precise, data-rich. Her sentences shorten as the experiment unsettles her.
    # Lyra: measured, warm, deliberate. The cadence of practiced stillness.
    # Aeron: peripheral. Observes. His athoughts are the audience's guide.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - NOELLE'S ANALYSIS ALCOVE - LATE EVENING]
    # The alcove is Noelle's kingdom — crystal arrays, biometric displays, data logs
    # stacked in precise columns. Everything has a place. Everything is measured.

    #scene bg_analysis_alcove_emp with dissolve
    #play ambient "sfx/ambient/crystal_hum_low.ogg" fadein 2.0

    # ========== PHASE 1 -- THE PROPOSITION ==========

    athought "I hear them before I see them."

    athought "Lyra's voice. Low. Patient. The tone she uses when she's asking for something she knows will be refused."

    athought "Noelle's voice. Clipped. The tone she uses when she's already composing a rebuttal."

    "Noelle's alcove. The crystal arrays throw pale blue light across the walls. Biometric displays cycle through their idle patterns — heart rate baselines, neural coherence graphs, galvanic response curves. The language of the body, translated into numbers."

    "Lyra stands beside the primary display. Her arms are at her sides. Open posture. No defense."

    "Noelle sits in her analysis chair, stylus suspended over a data crystal. Not writing. Waiting."

    l "I'm not asking you to believe anything. I'm asking you to observe."

    n "I observe professionally. That's the concern."

    l "Then observe professionally. Run your instruments. Log everything. I'm not asking you to turn them off."

    n "You're asking me to participate in a ritual I can't verify."

    l "I'm asking you to breathe with me for three minutes."

    "A pause. Noelle's stylus rotates between her fingers — the unconscious fidget of a mind processing faster than speech."

    n "Breathing is a physiological function. I already do it."

    l "You regulate it. That's different."

    athought "I lean against the doorframe. Neither of them has noticed me."

    athought "Or they've noticed and decided I'm irrelevant. Same result."

    n "Define what you expect to happen."

    l "I don't expect anything. That's the point."

    n "Everything has a point. You're proposing an experiment. Experiments have hypotheses."

    l "The Order didn't call them hypotheses. We called them invitations."

    n "An invitation without a defined outcome is noise."

    l "An invitation without a defined outcome is faith."

    "Noelle's stylus stops spinning."

    n "I don't have faith."

    l "I know. That's why I'm asking you."

    athought "That lands differently than Noelle expected. I can see it — the recalculation behind her eyes."

    athought "Lyra didn't say 'I know, and that's a problem.' She said 'I know, and that's why you're the right person.'"

    athought "Noelle has no framework for being chosen because of her skepticism, not despite it."

    # ========== PHASE 2 -- THE PROTOCOL ==========

    # VISUAL: Noelle activating instruments. Methodical. Every sensor calibrated.
    # She's building the scaffold that will make this tolerable to her.

    n "If I agree — and I haven't agreed — I'll need full biometric logging. Heart rate. Galvanic skin response. Neural coherence estimation via the crystal array. Respiratory pattern mapping."

    l "Fine."

    n "I'll also need a baseline. Three minutes of silence before we begin. Control condition."

    l "Fine."

    n "And I reserve the right to terminate at any point if the data becomes—"

    l "Noelle."

    n "What?"

    l "You can stop whenever you want. You don't need a data justification."

    "Another pause. Longer."

    n "That's... noted."

    "She activates the instruments. Each display blooms into readiness — heart rate at sixty-two, galvanic baseline low, respiratory rate fourteen. The numbers of a person at clinical rest."

    n "Baseline recording. Three minutes. Don't speak."

    "Three minutes of crystal hum and breathing. Noelle watches her own numbers with the detachment of someone reading weather data."

    athought "Her heart rate doesn't change during the baseline. Sixty-two. Steady."

    athought "That's control. Or it's armor. Hard to tell the difference from the doorway."

    #play sound "sfx/one_shot/crystal_chime_soft.ogg"

    n "Baseline recorded. Proceed."

    # ========== PHASE 3 -- THE EXERCISE ==========

    # VISUAL: Lyra kneels in front of Noelle's chair. Not supplication — proximity.
    # Her hands rest palm-up on her knees. The posture of the Order's breathing discipline.
    # CAMERA: Slow push on Noelle's face. Lyra in soft focus.

    "Lyra kneels. Not in front of the instruments — in front of Noelle. Close enough that their knees almost touch."

    "Her hands settle palm-up on her thighs. The gesture is ancient. Unhurried."

    l "Close your eyes if you want. Or don't. Whatever feels right."

    n "I'll keep them open. I need to monitor—"

    l "Then keep them open."

    "Lyra breathes. Slow. Deep. Not exaggerated — just present. The kind of breath that fills the room because it doesn't try to."

    athought "The first breath. Lyra's rhythm is four counts in, six counts out. She's not counting aloud. The cadence is in her body."

    athought "Noelle is watching the displays. Her own respiratory rate: fourteen."

    "Second breath. Lyra's exhale settles into the alcove like heat from a low fire."

    athought "Noelle's respiratory rate: thirteen."

    "Third breath."

    athought "Twelve."

    "By the fifth breath, Noelle's respiration has matched Lyra's. Four in. Six out. She hasn't looked away from the displays, but her shoulders have dropped two inches."

    athought "She doesn't notice. Her eyes are on the numbers. The numbers are telling her one thing. Her body is telling her another."

    #play sound "sfx/one_shot/breath_deep_soft.ogg"

    l "(barely a whisper) Good. Don't try to do anything. Just let the breath be what it is."

    "Noelle's galvanic response dips. Heart rate: fifty-eight. The crystal array's neural coherence readout climbs — not dramatically, but the graph bends upward in a smooth, steady curve."

    athought "She's synchronizing. Not to a command. To a presence."

    athought "I've seen Lyra do this with patients. With Tessa. With frightened people in the corridors."

    athought "But this is different. Noelle isn't frightened. She's armed. Every instrument in this alcove is a weapon against uncertainty."

    athought "And the breathing is disarming her anyway."

    # --- THE MOMENT ---

    # VISUAL: The crystal array flickers. One readout — neural coherence — spikes,
    # then drops to zero for 1.4 seconds before resuming. Not a crash. A gap.
    # CAMERA: Tight on Noelle's face. Her eyes widen. Once.

    "Minute two. The crystal array flickers."

    "The neural coherence graph — the smooth upward curve — spikes. Then drops. Not to baseline. To nothing."

    "Zero. For one and a half seconds, the display reads zero."

    athought "Not flatline. Not failure. The instrument is running. The sensor is active."

    athought "There's just nothing to measure."

    "Noelle's eyes widen. Her breath catches — half a beat, then resumes. Four in. Six out. The rhythm holds even as her mind scrambles for the readout."

    "The coherence graph returns. Higher than before. A clean, smooth line, as if the gap was a held note between movements."

    athought "Noelle's hand twitches toward the crystal. She doesn't touch it."

    athought "Her heart rate: fifty-four. Lower than her baseline. Lower than I've ever seen it."

    "Lyra's eyes are closed. She doesn't know the graph dropped. She doesn't need to."

    "The third minute ends. Lyra's breathing returns to normal, gently, the way a tide recedes."

    l "That's it."

    "Noelle doesn't move."

    # ========== PHASE 4 -- THE AFTERMATH ==========

    # VISUAL: Noelle staring at her displays. Lyra standing, brushing off her knees.
    # The alcove is the same temperature but feels different.

    n "The coherence readout dropped to zero."

    l "Is that unusual?"

    n "It's impossible. Zero coherence means no neural activity. I was conscious. I was breathing. I was monitoring the display."

    l "What were you feeling when it dropped?"

    "Noelle opens her mouth. Closes it. Opens it again."

    n "I don't— I felt—"

    "She stops. The analyst who speaks in complete sentences, who maps every variable, who never begins a statement she can't finish."

    n "Warm."

    l "Warm?"

    n "Not temperature. Not galvanic. Something— else."

    athought "Lyra doesn't press. She stands. Waits."

    n "My instruments were running. Every sensor was active. The crystal array has a diagnostic confidence of ninety-seven percent."

    n "And for one point four seconds, it couldn't find me."

    l "Maybe it wasn't looking for the right thing."

    "Noelle stares at her."

    n "I designed the coherence metric. It captures everything."

    l "Everything you built it to capture."

    "The silence is long. Noelle's stylus lies untouched on the console."

    n "That's a tautology."

    l "Yes."

    n "You're saying the instrument failed because it was measuring the wrong variable."

    l "I'm saying there might be variables your instruments weren't designed to see. Not because they're broken. Because the thing that happened isn't made of the stuff they measure."

    athought "Noelle turns back to the display. Replays the readout. The gap stares back at her — a clean, precise absence."

    n "One point four seconds of unmeasurable data."

    n "I don't have a category for that."

    l "You don't need one yet."

    # --- NOELLE LOGS ---

    # VISUAL: Noelle's stylus moving across a data crystal. Writing. Not analysis — notation.
    # The handwriting is smaller than usual. More careful.

    "Noelle picks up her stylus. Writes."

    athought "I can't see the words from the doorway. But the motion is different from her usual notation — slower, the strokes deliberate, as if each letter costs something."

    n "I'm logging this as anomalous. I'll need to run secondary diagnostics on the crystal array."

    l "Of course."

    n "And I'll need to— I should—"

    "She pauses. Looks at the readout again."

    n "I'm creating a new variable placeholder. For the gap."

    l "What are you calling it?"

    "Noelle's stylus hovers. The analyst who names everything, categorizes everything, maps everything to its proper coordinate."

    n "The Unmeasurable."

    "Lyra blinks."

    l "That's not very scientific."

    n "No. It isn't."

    athought "She says it like a concession. And a beginning."

    athought "The woman who lives in data just named a thing that data can't hold. She didn't throw it away. She gave it a placeholder."

    athought "A placeholder is a promise to come back."

    # ========== PHASE 5 -- AERON PERIPHERAL CLOSE ==========

    athought "Lyra turns to leave. She sees me in the doorway."

    athought "A look passes between us. Not words — recognition. She knows I saw it."

    athought "She doesn't need me to say anything about it."

    "Lyra passes him in the doorway. Her hand brushes his arm. Brief. Warm. Then she's gone."

    athought "In the alcove, Noelle is replaying the readout. The gap. One point four seconds of nothing."

    athought "She'll run the diagnostics. She'll check every sensor. She'll verify the crystal calibration."

    athought "And when all of it comes back clean, she'll sit with that placeholder and stare at it."

    athought "The Unmeasurable."

    athought "Noelle doesn't do faith. But she does rigor. And rigor just forced her to admit that her map has an edge."

    athought "That's not conversion. It's something harder."

    athought "It's a scientist discovering a blank space on her own chart and choosing not to fill it with noise."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "anchor_seen")
    $ npc_remember("Noelle", "unmeasurable_variable_created", tone="unsettled_wonder")
    $ npc_remember("Lyra", "breathing_exercise_with_noelle", tone="quiet_patience")
    $ npc_remember("Noelle", "coherence_gap_1.4_seconds", tone="analytical_bewilderment")
    $ npc_remember("Lyra", "noelle_felt_warm", tone="gentle_recognition")
    $ rel_bump("Lyra", trust=1)
    $ rel_bump("Noelle", trust=1)
    $ nudge_poly(1)
    $ flag("unmeasurable_logged", True)
    $ flag("noelle_coherence_gap", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s08_the_unmeasurable_emp
# cann.chapter: Act III, Phase I -- Proving Ground (Empathy Path)
# cann.chapter_start: False
# cann.pair_anchor: A3_P09 (Lyra x Noelle)
# cann.when_in_timeline:
#   - Act III Phase I. After Echelon Strikes Back (s07). Base rebuilding underway.
#   - Late evening. Noelle working alone. Lyra seeks her out.
# cann.what_happened:
#   - Lyra proposes a breathing exercise as an experiential test. Noelle resists, then
#     agrees on condition of full biometric logging.
#   - Three-minute exercise. Noelle's respiration synchronizes with Lyra's involuntarily.
#   - At minute two: neural coherence readout drops to zero for 1.4 seconds. All sensors active.
#     The instrument didn't fail. It couldn't find what was happening.
#   - Noelle reports feeling "warm" -- not temperature, not galvanic. Something unmapped.
#   - She creates a new variable placeholder: "The Unmeasurable."
#   - She will run diagnostics. They will come back clean. The gap will remain.
#   - Aeron peripheral throughout. Observes from the doorway. Does not intervene.
# cann.aeron_state:
#   - Peripheral observer. Recognized the significance before they named it.
#   - "A scientist discovering a blank space on her own chart and choosing not to fill it with noise."
# cann.path_tracking:
#   - EMP baseline. No player choice -- pair anchor (observational for Aeron).
#   - scene_mark("anchor_seen") for pair anchor tracking.
#   - rel_bump: trust+1 for both Lyra and Noelle.
#   - nudge_poly(1) fires on the synchronization moment.
#   - flag("unmeasurable_logged"), flag("noelle_coherence_gap") for callbacks.
#   - EMP push: Noelle moved toward emotional understanding (placeholder, not rejection).
#   - OB-lean alternate: Noelle would file the gap as instrument error. Here she doesn't.
# cann.thematic_flags:
#   - "The Unmeasurable" -- the scene thesis. A name for the space between data and experience.
#   - Noelle's tautology: "It captures everything." / "Everything you built it to capture."
#   - The gap as held note -- not silence but a frequency outside the instrument's range.
#   - Faith vs rigor: Lyra's "invitation" vs Noelle's "hypothesis." Both arrive at the same gap.
#   - The placeholder as promise: naming something unmeasurable is the first step toward respect.
#   - Mirror of a3_s05 (Two Healers): tradition as unrecognized medicine.
#     Here: experience as unmeasurable variable.
#   - Mirror of a3_s07 (Echelon Strikes Back): Noelle's "6% he missed was the human parts."
#     Here: Noelle confronts the unmeasurable in herself.
# cann.character_moments:
#   - Noelle: "I don't have faith." / "I know. That's why I'm asking you."
#     Chosen FOR her skepticism. Her instruments fail not from error but from limitation.
#     Creates the placeholder instead of dismissing the data. That's character growth.
#   - Lyra: Patient. Precise in her own way. Doesn't proselytize.
#     "You don't need one yet." -- grants Noelle time without pressure.
#     The breathing exercise is two hundred years of Order discipline, applied with care.
#   - Aeron: Sees the significance. Doesn't narrate it to them. Peripheral respect.
#     "A placeholder is a promise to come back." -- his read on what Noelle just did.
# cann.block_status:
#   - PAIR ANCHOR (Lyra x Noelle). Both paths compatible.
# cann.requires_followup:
#   - "The Unmeasurable" as recurring term through Act 3 EMP. Noelle will reference it.
#   - Noelle's diagnostics will come back clean -- she needs a scene where she sits with that.
#   - The 1.4-second gap may correspond to a bloodline resonance event (see BR_III_03).
#   - Lyra and Noelle's dynamic: the skeptic and the ritualist building shared vocabulary.
#   - nudge_poly(2 total now with s05). Future scenes should increment.
#   - Noelle's "warm" sensation -- an EMP milestone. Should be referenced if she resists
#     emotional language later ("You said warm. You said it yourself.").
