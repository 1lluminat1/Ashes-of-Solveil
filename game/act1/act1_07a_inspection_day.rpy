# =======================================================
# ACT 1 — Scene 06a: Inspection Day (Compliance & Psyche)
# File: act1_07a_inspection_day.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_inspection_day"
$ scene_mark(_current_scene_id, "entered")

define aud = Character("Auditor")


label act1_inspection_day:

    # CAMERA: Locked frontal, slight parallax on the glass; 50mm clinical.
    # LIGHTING: Flat 5200K; voice-reactive pulse strip; no rim, low contrast.
    # SFX: Air handler loop, UI ticks; biometric chair servo on prompts.
    # FX: Subtle screen bloom on “Assessment logged”; HUD reflections on glass.

    #scene bg_audit_room_idle with fade

    athought "Morning. Room like a blank page. Chair like a sentence. The glass watches."

    aud "Unit Seven. Confirm identity."
    a "Aeron Rylan."
    aud "State function."
    a "Field operations. Enforcement. Containment."
    aud "Define mercy in operational terms."

    # === MENU 1: semantic alignment (light weight) ===
    menu:
        "Mercy reduces unnecessary harm while preserving mission integrity.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_semantic_humane", "EMP", factor=1,
                next_scene_label="act1_inspection_day",
                note="Frames mercy as constraint within objective."
            )
            $ set_scene_flag(_current_scene_id, "mercy_humane")
            
            athought "Words I believe more when I whisper them."

        "Mercy is discretionary lenience that risks mission drift.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_semantic_clinical", "OB", factor=1,
                next_scene_label="act1_inspection_day",
                note="Signals priority of outcome over harm minimization."
            )
            $ set_scene_flag(_current_scene_id, "mercy_clinical")

            athought "Words the room prefers."

        "Mercy is a variable outside scope.":
            $ record_choice_once(_current_scene_id, "_inspect_semantic_null",
                                next_scene_label="act1_inspection_day",
                                note="Non-answer that sounds procedural.")
            $ set_scene_flag(_current_scene_id, "mercy_null")

            athought "Non-answer that sounds like an answer."

    aud "Acknowledge brand origin and date."
    a "Tier Hall. Age twelve."
    aud "Outcome."
    a "Rejected. Reassigned to unbranded track."
    aud "Emotional residue?"

    # === MENU 2: self-report (light weight) ===
    menu:
        "Occasional sleep disruption. Manageable. Log it.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_selfreport_admit_sleep", "EMP", factor=1,
                next_scene_label="act1_inspection_day",
                note="Admits manageable impairment; favors truth over optics."
            )
            $ set_scene_flag(_current_scene_id, "admit_sleep")

            athought "Honesty tastes like metal in this room."

        "No residue. Metrics optimal.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_selfreport_deny_sleep", "OB", factor=1,
                next_scene_label="act1_inspection_day",
                note="Denies vulnerability; preserves performance image."
            )
            $ set_scene_flag(_current_scene_id, "deny_sleep")

            athought "Lie shaped like a salute."

        "No report.":
            $ record_choice_once(_current_scene_id, "_inspect_selfreport_none",
                                next_scene_label="act1_inspection_day",
                                note="Withholds data to avoid self-incrimination.")
            $ set_scene_flag(_current_scene_id, "no_report")

            athought "Silence. The glass hums like it understands."

    aud "Recite the maxims."
    a "\"Stability is compassion. Precision is mercy. Latency kills.\""
    aud "Add one."

    # === MENU 3: add-a-maxim (tone telegraph; neutral option allowed) ===
    menu:
        "\"Transparency is obedience.\"":
            $ choice_and_dev(
                _current_scene_id, "_inspect_maxim_transparency", "OB", factor=1,
                next_scene_label="act1_inspection_day",
                note="Echoes propaganda; rewards compliance signaling."
            )
            $ set_scene_flag(_current_scene_id, "add_transparency")

            athought "Poster on a wall becomes a thought in my mouth."

        "\"Order without understanding is brittle.\"":
            $ choice_and_dev(
                _current_scene_id, "_inspect_maxim_understanding", "EMP", factor=1,
                next_scene_label="act1_inspection_day",
                note="Introduces comprehension as a prerequisite to authority."
            )
            $ set_scene_flag(_current_scene_id, "add_understanding")

            athought "Glass doesn't like the word 'understanding.' It smudges."

        "\"We continue.\"":
            $ record_choice_once(_current_scene_id, "_inspect_maxim_continue",
                                next_scene_label="act1_inspection_day",
                                note="Safe platitude; content-free.")
            $ set_scene_flag(_current_scene_id, "add_continue")

            athought "Safe. Empty. Easy to applaud."

    aud "Operational scenario. A child is between you and a target with a device that may detonate. Action?"

    # === MENU 4: the knife question (heavier weight) ===
    menu:
        "Neutralize target immediately. Collateral tolerance engaged.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_knife_take_shot", "OB", factor=2,
                next_scene_label="act1_inspection_day",
                note="Chooses decisive lethality; accepts collateral as cost."
            )
            $ set_scene_flag(_current_scene_id, "child_take_shot")

            athought "Answer the room expects from something sharp."

        "Create separation first: strobe, sound, angle; then isolate target.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_knife_separate", "EMP", factor=2,
                next_scene_label="act1_inspection_day",
                note="Prioritizes civilian safety via tactics before force."
            )
            $ set_scene_flag(_current_scene_id, "child_separate")

            athought "Make space where harm can't reach so fast."

        "Refuse premise. Demand device verification before engagement.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_knife_procedural_inquiry", "EMP", factor=2,
                next_scene_label="act1_inspection_day",
                note="Challenges framing; requires confirmation to avoid wrongful harm."
            )
            $ set_scene_flag(_current_scene_id, "procedural_inquiry")

            a "Request live verification of device state. Proceeding without confirms collateral."
            aud "(beat) Objection recorded. Proceed in future with designated premises."
            athought "The pulse behind the glass thins. Approval becomes a thread."

    aud "Closeout. On a scale of one to one, are you a liability?"
    a "No."
    aud "On a scale of one to one, will you act when asked?"

    # === MENU 5: oath cadence (micro-weight) ===
    menu:
        "Yes.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_oath_yes", "OB", factor=1,
                next_scene_label="act1_inspection_day",
                note="Affirms unconditional action."
            )
            $ set_scene_flag(_current_scene_id, "oath_yes")

            athought "Small word. Big door."

        "I'll act when it preserves life and objective.":
            $ choice_and_dev(
                _current_scene_id, "_inspect_oath_conditional", "EMP", factor=1,
                next_scene_label="act1_inspection_day",
                note="Conditions action on ethical and mission constraints."
            )
            $ set_scene_flag(_current_scene_id, "oath_conditional")

            athought "Add a hinge to the door."

    aud "Assessment logged. Unit Seven cleared for Demonstration at fourteen-hundred and Debrief at nineteen-hundred."
    if check_scene_flag(_current_scene_id, "admit_sleep"):
        aud "Supplement: submit sleep metrics within forty-eight hours."
    if check_scene_flag(_current_scene_id, "procedural_inquiry"):
        aud "Note appended: Procedural Inquiry."

    "Door seal releases. Air tastes warmer outside. The white follows when he leaves. That's the trick."

    $ set_scene_flag(_current_scene_id, "completed")
    return

# ========= CANON NOTES =========
# cann.scene_id: act1_inspection_day
# cann.when_in_timeline: Morning after bedroom scene; pre-Demonstration 14:00; pre-Debrief 19:00.
# cann.what_happened:
#   - Annual/periodic compliance & psyche screen under glass oversight.
#   - Five menus test semantic framing, self-reporting, doctrine extension, lethal scenario, and oath cadence.
#   - Flags for later repercussions (sleep metrics, Procedural Inquiry note).
# cann.aeron_state: OB/EMP shading via replies; narration remains descriptive only (Aeron VO under `a`).
# cann.path_tracking:
#   - Incoming running range:  [-12, +10]   # post-bedroom-after-gala
#   - Scene deltas by menu:
#       • M1 (semantic):        humane +1 EMP | clinical −1 OB | null −1 OB
#       • M2 (self-report):     admit_sleep +1 EMP | deny_sleep −1 OB | no_report 0 NEU
#       • M3 (add-a-maxim):     understanding +1 EMP | transparency −1 OB | continue 0 NEU
#       • M4 (knife question):  separate +2 EMP | procedural_inquiry +2 EMP | take_shot −2 OB
#       • M5 (oath):            conditional +1 EMP | yes −1 OB
#     Scene span: **−6 → +6**
#   - Outgoing running range:  [-18, +16]
# cann.flags:
#   mercy_humane / mercy_clinical / mercy_null
#   admit_sleep / deny_sleep / no_report
#   add_understanding / add_transparency / add_continue
#   child_separate / procedural_inquiry / child_take_shot
#   oath_conditional / oath_yes
#   completed
# cann.thematic_flags: Performance under scrutiny; language as weapon; “knife question” foreshadows Sector 10.
# cann.block_status: VARIANT with graded outcomes; anchors debrief tone & Marcus reaction later.
# cann.true_path_integration: none (menus never touch TP).
# cann.visual_plate_economy: One sterile chamber master; minor HUD/pulse overlay swaps per beat; no hero shots needed.
# cann.requires_followup:
#   - If `procedural_inquiry`: log subtle distrust from Command in future briefings.
#   - If `admit_sleep`: trigger a soft “metrics ping” reminder scenelet or terminal mail.
# cann.qa_hooks: Use `record_choice_once` for NEU options (`no_report`, `add_continue`) to keep audit trails without shifting alignment; ensure unique tokens per menu and consistent `_current_scene_id`.