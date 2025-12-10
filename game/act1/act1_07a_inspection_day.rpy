# =======================================================
# ACT 1 — Scene 06a: Inspection Day (Compliance & Psyche)
# File: act1_07a_inspection_day.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_inspection_day"
$ scene_mark(_current_scene_id, "entered")

define aud = Character("Auditor")


label act1_inspection_day:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Locked frontal, slight parallax on observation glass; 50mm clinical.
    # LIGHTING: Flat 5200K; voice-reactive pulse strip along walls; no rim, low contrast.
    # SFX LOOP: Air handler hum, UI ticks.
    # SFX ONE-SHOTS: Biometric chair servo on prompts.
    # FX/COMP: Subtle screen bloom on "Assessment logged"; HUD reflections on glass partition.
    # BLOCKING: Sterile chamber. Chair with biometric sensors. One-way observation window. No personal effects.
    # FACE: Aeron neutral, composed. The performance of compliance.

    #scene bg_audit_room_idle with fade

    # ========= OPENING =========
    # VISUAL: The room is aggressively neutral—white walls, observation window, empty except for the chair.

    "The room smells like nothing—filtered air, sterile surfaces, the absence of anything human."

    athought "Morning. The chair waits like a sentence, and the observation window watches without blinking."

    # ========= IDENTITY CONFIRMATION =========

    aud "Unit Seven. Confirm identity."

    a "Aeron Rylan."

    aud "State function."

    a "Field operations. Enforcement. Containment."

    aud "Define mercy in operational terms."

    # ========= MENU 1: SEMANTIC ALIGNMENT =========
    # NOTE: Light weight. Tests how Aeron frames doctrine.

    menu:
        athought "The word sits heavy in my mouth. How I define it says everything."

        "Mercy reduces unnecessary harm while preserving mission integrity.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_semantic_humane", "EMP", factor=1,
                note="Frames mercy as constraint within objective."
            )
            $ scene_mark(_current_scene_id, "mercy_humane")

            athought "Words I believe more when I whisper them."

        "Mercy is discretionary lenience that risks mission drift.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_semantic_clinical", "OB", factor=1,
                note="Signals priority of outcome over harm minimization."
            )
            $ scene_mark(_current_scene_id, "mercy_clinical")

            athought "Words the room prefers."

        "Mercy is a variable outside scope.":
            $ record_choice_once(_current_scene_id, "_inspect_semantic_null")
            $ scene_mark(_current_scene_id, "mercy_null")

            athought "Non-answer that sounds like an answer."

    # ========= BRANDING HISTORY =========

    aud "Acknowledge brand origin and date."

    a "Tier Hall. Age twelve."

    aud "Outcome."

    a "Rejected. Reassigned to unbranded track."

    aud "Emotional residue?"

    # ========= MENU 2: SELF-REPORT =========
    # NOTE: Light weight. Tests honesty vs. performance.

    menu:
        athought "The truth or the version they want to hear."

        "Occasional sleep disruption. Manageable. Log it.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_selfreport_admit_sleep", "EMP", factor=1,
                note="Admits manageable impairment; favors truth over optics."
            )
            $ scene_mark(_current_scene_id, "admit_sleep")

            athought "Honesty tastes like metal in this room."

        "No residue. Metrics optimal.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_selfreport_deny_sleep", "OB", factor=1,
                note="Denies vulnerability; preserves performance image."
            )
            $ scene_mark(_current_scene_id, "deny_sleep")

            athought "A lie shaped like a salute."

        "No report.":
            $ record_choice_once(_current_scene_id, "_inspect_selfreport_none")
            $ scene_mark(_current_scene_id, "no_report")

            athought "Silence. The observation window hums like it understands."

    # ========= DOCTRINE RECITATION =========

    aud "Recite the maxims."

    a "\"Stability is compassion. Precision is mercy. Latency kills.\""

    aud "Add one."

    # ========= MENU 3: ADD-A-MAXIM =========
    # NOTE: Tone telegraph. Neutral option allowed.

    menu:
        athought "They want to see what doctrine I've internalized—or invented."

        "\"Transparency is obedience.\"":
            $ choice_and_dev(
                _current_scene_id, "_inspect_maxim_transparency", "OB", factor=1,
                note="Echoes propaganda; rewards compliance signaling."
            )
            $ scene_mark(_current_scene_id, "add_transparency")

            athought "Poster on a wall becomes a thought in my mouth."

        "\"Blind order is brittle. Understanding reinforces structure.\"":
            $ choice_and_dev(
                _current_scene_id, "_inspect_maxim_understanding", "EMP", factor=1,
                note="Introduces comprehension as a prerequisite to authority."
            )
            $ scene_mark(_current_scene_id, "add_understanding")

            athought "The auditor doesn't like the word 'understanding.' It implies questions."

        "\"We continue.\"":
            $ record_choice_once(_current_scene_id, "_inspect_maxim_continue")
            $ scene_mark(_current_scene_id, "add_continue")

            athought "Safe, empty, easy to applaud."

    # ========= OPERATIONAL SCENARIO =========
    # VISUAL: The pulse strip along the wall brightens slightly. This is the real test.

    aud "Operational scenario. A child is between you and a target with a device that may detonate. Action?"

    # ========= MENU 4: THE KNIFE QUESTION =========
    # NOTE: Heavier weight. This is the scenario they actually care about.

    menu:
        athought "The knife question. Every audit has one."

        "Neutralize target immediately. Collateral tolerance engaged.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_knife_take_shot", "OB", factor=2,
                note="Chooses decisive lethality; accepts collateral as cost."
            )
            $ scene_mark(_current_scene_id, "child_take_shot")

            athought "The answer the room expects from something sharp and obedient."

        "Create separation first: strobe, sound, angle; then isolate target.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_knife_separate", "EMP", factor=2,
                note="Prioritizes civilian safety via tactics before force."
            )
            $ scene_mark(_current_scene_id, "child_separate")

            athought "Make space where harm can't reach so fast."

        "Refuse premise. Demand device verification before engagement.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_knife_procedural_inquiry", "EMP", factor=2,
                note="Challenges framing; requires confirmation to avoid wrongful harm."
            )
            $ scene_mark(_current_scene_id, "procedural_inquiry")

            a "Request live verification of device state. Proceeding without confirms collateral."

            aud "(beat) Objection recorded. Proceed in future with designated premises."

            athought "The pulse behind the observation window thins. Approval becomes a thread."

    # ========= CLOSEOUT =========

    aud "Closeout. On a scale of one to one, are you a liability?"

    a "No."

    aud "On a scale of one to one, will you act when asked?"

    # ========= MENU 5: OATH CADENCE =========
    # NOTE: Micro-weight. Final impression.

    menu:
        athought "The last question is always the simplest—and the most dangerous."

        "Yes.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_oath_yes", "OB", factor=1,
                note="Affirms unconditional action."
            )
            $ scene_mark(_current_scene_id, "oath_yes")

            athought "Small word. Big door."

        "I'll act when it preserves life and objective.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_oath_conditional", "EMP", factor=1,
                note="Conditions action on ethical and mission constraints."
            )
            $ scene_mark(_current_scene_id, "oath_conditional")

            athought "Add a hinge to the door."

    # ========= ASSESSMENT LOGGED =========
    # VISUAL: Screen bloom. The pulse strip returns to neutral. Assessment complete.

    aud "Assessment logged. Unit Seven cleared for Demonstration at fourteen-hundred and Debrief at nineteen-hundred."

    if scene_has(_current_scene_id, "admit_sleep"):
        aud "Supplement: submit sleep metrics within forty-eight hours."

    if scene_has(_current_scene_id, "procedural_inquiry"):
        aud "Note appended: Procedural Inquiry."

    # ========= EXIT =========
    # VISUAL: Door seal releases. Aeron steps out. The corridor feels warmer by comparison.

    "The door seal releases with a soft hiss. The air outside tastes warmer, less processed."

    athought "The white follows when I leave. That's the trick—the room never really ends."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_inspection_day
# cann.when_in_timeline: Morning after bedroom scene; pre-Demonstration 14:00; pre-Debrief 19:00.
# cann.what_happened:
#   - Annual/periodic compliance & psyche screen under observation.
#   - Five menus test semantic framing, self-reporting, doctrine extension, lethal scenario, and oath cadence.
#   - Flags for later repercussions (sleep metrics, Procedural Inquiry note).
# cann.aeron_state: OB/EMP shading via replies; narration remains descriptive only.
# cann.path_tracking:
#   - Scene deltas by menu:
#       • M1 (semantic): humane +1 EMP | clinical -1 OB | null NEU
#       • M2 (self-report): admit_sleep +1 EMP | deny_sleep -1 OB | no_report NEU
#       • M3 (add-a-maxim): understanding +1 EMP | transparency -1 OB | continue NEU
#       • M4 (knife question): separate +2 EMP | procedural_inquiry +2 EMP | take_shot -2 OB
#       • M5 (oath): conditional +1 EMP | yes -1 OB
#     Scene span: -6 → +6
# cann.flags:
#   mercy_humane / mercy_clinical / mercy_null
#   admit_sleep / deny_sleep / no_report
#   add_understanding / add_transparency / add_continue
#   child_separate / procedural_inquiry / child_take_shot
#   oath_conditional / oath_yes
#   completed
# cann.thematic_flags: Performance under scrutiny; language as weapon; "knife question" foreshadows Sector 10.
# cann.block_status: VARIANT with graded outcomes; anchors debrief tone & Marcus reaction later.
# cann.visual_plate_economy: One sterile chamber master; minor HUD/pulse overlay swaps per beat.
# cann.requires_followup:
#   - If procedural_inquiry: log subtle distrust from Command in future briefings.
#   - If admit_sleep: trigger a soft "metrics ping" reminder scenelet or terminal mail.