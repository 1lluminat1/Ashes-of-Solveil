# =======================================================
# ACT 1 — Scene 07b: Barracks Morning (Ritual, Rations, Rank)
# File: act1_07b_barracks_morning.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_07b_barracks_morning"
$ scene_mark(_current_scene_id, "entered")


label act1_07b_barracks_morning:

    # ---------- Stage directions ----------
    # CAMERA: Lateral track through barracks aisle (35–40mm), waist-up silhouettes; keep Aeron face off-screen.
    # LIGHTING: Morning Aeries fluorescents, 5200K flat; green/red status LEDs read clearly.
    # SFX: Intercom mantra, card scanners beeping, distant boots; no rain (Aeries above cloudline).
    # FX/COMP: Soft bloom on green/red scanners; subtle HUD reflection off visor glass where visible.
    # BLOCKING/PROPS: Ration gate, scanner, “priority queue” stanchion, Quartermaster window, ticket console.
    # --------------------------------------

    #scene bg_barracks_corridor_morning with fade

    "{i}Barracks breathing in unison. Intercom teaches the day how to speak.{/i}"

    voice "Stability is compassion. Precision is mercy. Latency kills."

    # RATION LINE — WORKER INCIDENT
    "{i}Ration line. Green lights snap for ranks. Red for everyone else. A worker holds a chipped card like an apology.{/i}"
    guard "Priority queue. Step aside."
    worker "My child—"
    guard "Step. Aside."

    menu:
        "Worker’s card faults red while the guard looks away."
        "Quietly restore the worker's ration chip.":
            $ apply_choice_once(
                _current_scene_id, "_worker_help", "EMP", factor=1,
                next_scene_label="act1_07b_barracks_morning",
                note="Micro-intervention; reduce harm without confrontation."
            )
            $ set_scene_flag(_current_scene_id, "helped_worker")
            $ add_item("supplies", "food", 1)
            a "{i}I tilt the card under the scanner. A green blink pretends nothing happened.{/i}"
            worker "(whisper) Thank you."

        "Ignore it and move forward in line.":
            $ record_choice_once(_current_scene_id, "_worker_ignore",
                                next_scene_label="act1_07b_barracks_morning",
                                note="Flavor-only; maintains flow without engagement.")
            "{i}Green opens for me. Red stays red. The line learns its lesson.{/i}"

        "Tell the guard to advance priority flow per protocol.":
            $ apply_choice_once(
                _current_scene_id, "_worker_endorse_priority", "OB", factor=1,
                next_scene_label="act1_07b_barracks_morning",
                note="Reasserts hierarchy; protects throughput over individual need."
            )
            $ set_scene_flag(_current_scene_id, "endorsed_priority")
            guard "(approving) Copy. Keep the lane clean."
            "{i}Order is a broom. People are dust.{/i}"

    # Alignment flavor: ration incident
    $ band = get_empathy_band()
    if check_scene_flag(_current_scene_id, "helped_worker"):
        if band == "obedience":
            a "{i}Anomalous gesture. File under throughput optimization and keep moving.{/i}"
        elif band == "conflicted":
            a "{i}Small fix in a broken queue. Not nothing. Not enough.{/i}"
        else:
            a "{i}One green light where it mattered. The system won’t notice. I will.{/i}"
    elif check_scene_flag(_current_scene_id, "endorsed_priority"):
        if band == "obedience":
            a "{i}Flow restored. Metrics satisfied. Silence resumes.{/i}"
        elif band == "conflicted":
            a "{i}Protocol holds. Something in my chest doesn’t.{/i}"
        else:
            a "{i}The lane is clean. My conscience isn’t.{/i}"

    # Momentum whisper (ration)
    $ mom = get_alignment_momentum()  # -1..+1 recent trend
    if mom >= 0.5:
        a "{i}Lately the choices lean human. Maybe that’s the point.{/i}"
    elif mom <= -0.5:
        a "{i}Lately the edge comes easier. Habit wearing a uniform.{/i}"

    # QUARTERMASTER / JUNIOR RECRUIT — REPUTATION POLISH
    qm "Unit Seven. Pull ticket, sign. Ammunition allotment registered."
    jr "Sir—how do you polish a reputation report? They flag my 'latency' on simulations."

    menu:
        "The recruit waits for phrasing that will keep him alive."
        "Teach a humane frame: 'Stabilize civilians first; then pursue objective.'":
            $ apply_choice_once(
                _current_scene_id, "_mentor_humane", "EMP", factor=1,
                next_scene_label="act1_07b_barracks_morning",
                note="Centers civilian stability as primary constraint."
            )
            $ set_scene_flag(_current_scene_id, "mentored_humane")
            jr "(relieved) Stabilize first. Then objective. Got it."
            "{i}He writes it like a prayer that might pass for policy.{/i}"

        "Teach the clinical script: 'Neutralize; collateral within tolerance.'":
            $ apply_choice_once(
                _current_scene_id, "_mentor_clinical", "OB", factor=1,
                next_scene_label="act1_07b_barracks_morning",
                note="Optimizes outcome language for audits; normalizes collateral."
            )
            $ set_scene_flag(_current_scene_id, "mentored_clinical")
            jr "(grim) Neutralize. Tolerance."
            "{i}He looks smaller repeating it.{/i}"

        "Tell him to keep his head down and copy senior phrasing.":
            $ record_choice_once(_current_scene_id, "_mentor_survival",
                                next_scene_label="act1_07b_barracks_morning",
                                note="Neutral survival advice; no alignment delta.")
            "{i}He nods. Survival as grammar.{/i}"

    # Alignment flavor: recruit advice
    $ band = get_empathy_band()
    if check_scene_flag(_current_scene_id, "mentored_humane"):
        if band == "obedience":
            a "{i}Language won’t save him. Maybe it buys him a breath.{/i}"
        elif band == "conflicted":
            a "{i}The right words can tilt a trigger finger. Sometimes that’s enough.{/i}"
        else:
            a "{i}If he remembers people first, maybe the report won’t have to lie for him.{/i}"
    elif check_scene_flag(_current_scene_id, "mentored_clinical"):
        if band == "obedience":
            a "{i}He’ll pass the audit. Passing keeps you alive here.{/i}"
        elif band == "conflicted":
            a "{i}I handed him the script that hollows you out. I know how it ends.{/i}"
        else:
            a "{i}I put the weight in his mouth and told him to carry it. The system calls that training.{/i}"

    # Momentum whisper (recruit)
    $ mom = get_alignment_momentum()
    if mom >= 0.5:
        a "{i}The trend’s been softer. Maybe I’m teaching myself as much as him.{/i}"
    elif mom <= -0.5:
        a "{i}The trend’s been colder. Easier to hand out the mask than take it off.{/i}"

    # EXIT
    voice "Units scheduled for demonstration: report at 14:00."
    "{i}The hallway empties like a throat clearing. Fourteen-hundred writes itself behind his eyes.{/i}"

    $ set_scene_flag(_current_scene_id, "completed")
    
    return

# ========= CANON NOTES =========
# cann.scene_id: act1_07b_barracks_morning
# cann.when_in_timeline: Morning barracks cycle; same day as Inspection scene; pre-Demonstration 14:00.
# cann.what_happened:
#   - Ration-line micro-incident (help / ignore / endorse priority).
#   - Junior recruit advice (humane / clinical / survival).
#   - Momentum whispers reflect recent alignment trend.
# cann.aeron_state: OB-lean baseline voice; tier/momentum tint via flavor stingers.
# cann.path_tracking:
#   - Incoming running range:  [-18, +16]   # post-Inspection Day (act1_07a)
#   - Scene deltas:
#       • M1 (ration):  help +1 EMP  | ignore 0 NEU  | endorse +1 OB
#       • M2 (mentor):  humane +1 EMP | survival 0 NEU | clinical +1 OB
#     Scene span: **−2 → +2** (max OB path = +2; max EMP path = +2).
#   - Outgoing running range: [-20, +18]
# cann.flags:
#   - Set:   helped_worker | endorsed_priority | mentored_humane | mentored_clinical | completed
#   - Suggested NEU logging (use record_choice_once):
#       barracks_worker_ignore, barracks_mentor_survival
# cann.thematic_flags: Performance ritual; hierarchy optics; language as compliance UI; micro-mercy vs throughput.
# cann.block_status: VARIANT (micro-outcomes only); may feed light reputation/cred if you’re tracking it.
# cann.true_path_integration: none (menus never touch TP).
# cann.visual_plate_economy: One corridor master; toggle LED state + crowd density for both incidents; no hero shot.
# cann.requires_followup:
#   - If `helped_worker`: tiny goodwill ping from Unders contact much later (optional).
#   - If `mentored_clinical`: recruit shows up in a later op repeating the phrasing (echo).
# cann.qa_hooks: Ensure `_current_scene_id` consistency; unique tokens for M1/M2; add `record_choice_once` for the two neutral options.