# =======================================================
# ACT 1 — Scene 07b: Barracks Morning (Ritual, Rations, Rank)
# File: act1_07b_barracks_morning.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_07b_barracks_morning"
$ scene_mark(_current_scene_id, "entered")


label act1_07b_barracks_morning:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Lateral track through barracks aisle (35–40mm), waist-up silhouettes; keep Aeron face off-screen.
    # LIGHTING: Morning Aeries fluorescents, 5200K flat; green/red status LEDs read clearly.
    # SFX LOOP: Distant boots, ventilation hum.
    # SFX ONE-SHOTS: Intercom mantra, card scanners beeping.
    # FX/COMP: Soft bloom on green/red scanners; subtle HUD reflection off visor glass where visible.
    # BLOCKING: Ration gate, scanner, "priority queue" stanchion, Quartermaster window, ticket console.
    # CANON: Aeries above cloudline—no rain language.

    #scene bg_barracks_corridor_morning with fade

    # ========= OPENING — INTERCOM RITUAL =========
    # VISUAL: Barracks corridor. Bodies in motion. The intercom speaks and everyone listens without hearing.

    "The barracks breathe in unison—bodies moving through routine while the intercom teaches the day how to speak."

    voice "Stability is compassion. Precision is mercy. Latency kills."

    # ========= RATION LINE — WORKER INCIDENT =========
    # VISUAL: Ration queue. Green lights for ranks, red for everyone else.
    # BLOCKING: A worker near the front holds a chipped card. Guard approaching.

    "The ration line stretches back into fluorescent haze—green lights snapping for ranks, red for everyone else."

    "A worker holds a chipped card like an apology, knuckles white around the plastic."

    guard "Priority queue. Step aside."

    worker "My child—"

    guard "Step. Aside."

    # ========= PLAYER CHOICE — WORKER INCIDENT =========

    menu:
        athought "The worker's card faults red while the guard looks away."

        "Quietly restore the worker's ration chip.":
            $ choice_and_dev(
                _current_scene_id, "_worker_help", "EMP", factor=1,
                note="Micro-intervention; reduce harm without confrontation."
            )
            $ scene_mark(_current_scene_id, "helped_worker")

            athought "I tilt the card under the scanner—a green blink, and the system pretends nothing happened."

            worker "(whisper) Thank you."

        "Ignore it and move forward in line.":
            $ record_choice_once(_current_scene_id, "_worker_ignore")

            "Green opens for me. Red stays red. The line learns its lesson."

        "Tell the guard to advance priority flow per protocol.":
            $ choice_and_dev(
                _current_scene_id, "_worker_endorse_priority", "OB", factor=1,
                note="Reasserts hierarchy; protects throughput over individual need."
            )
            $ scene_mark(_current_scene_id, "endorsed_priority")

            guard "(approving) Copy. Keep the lane clean."

            athought "Order is a broom. People are dust."

    # ========= RATION INCIDENT — PATH FLAVOR =========

    if scene_has(_current_scene_id, "helped_worker"):
        if empathy_band() == "obedience":
            athought "Anomalous gesture. File under throughput optimization and keep moving."
        elif empathy_band() == "empathy":
            athought "One green light where it mattered. The system won't notice. I will."
        else:
            athought "Small fix in a broken queue—not nothing, not enough."

    elif scene_has(_current_scene_id, "endorsed_priority"):
        if empathy_band() == "obedience":
            athought "Flow restored, metrics satisfied, silence resumes."
        elif empathy_band() == "empathy":
            athought "The lane is clean. My conscience isn't."
        else:
            athought "Protocol holds. Something in my chest doesn't."

    # ========= QUARTERMASTER — JUNIOR RECRUIT =========
    # VISUAL: Quartermaster window. A junior recruit hovers nearby, nervous.
    # BLOCKING: Aeron signs for ammunition. The recruit approaches.

    qm "Unit Seven. Pull ticket, sign. Ammunition allotment registered."

    jr "Sir—how do you polish a reputation report? They flag my 'latency' on simulations."

    # ========= PLAYER CHOICE — MENTOR THE RECRUIT =========

    menu:
        athought "The recruit waits for phrasing that will keep him alive."

        "Teach a humane frame: 'Stabilize civilians first; then pursue objective.'":
            $ choice_and_dev(
                _current_scene_id, "_mentor_humane", "EMP", factor=1,
                note="Centers civilian stability as primary constraint."
            )
            $ scene_mark(_current_scene_id, "mentored_humane")

            jr "(relieved) Stabilize first. Then objective. Got it."

            athought "He writes it down like a prayer that might pass for policy."

        "Teach the clinical script: 'Neutralize; collateral within tolerance.'":
            $ choice_and_dev(
                _current_scene_id, "_mentor_clinical", "OB", factor=1,
                note="Optimizes outcome language for audits; normalizes collateral."
            )
            $ scene_mark(_current_scene_id, "mentored_clinical")

            jr "(grim) Neutralize. Tolerance."

            athought "He looks smaller repeating it."

        "Tell him to keep his head down and copy senior phrasing.":
            $ record_choice_once(_current_scene_id, "_mentor_survival")

            athought "He nods. Survival as grammar."

    # ========= RECRUIT ADVICE — PATH FLAVOR =========

    if scene_has(_current_scene_id, "mentored_humane"):
        if empathy_band() == "obedience":
            athought "Language won't save him. Maybe it buys him a breath."
        elif empathy_band() == "empathy":
            athought "If he remembers people first, maybe the report won't have to lie for him."
        else:
            athought "The right words can tilt a trigger finger. Sometimes that's enough."

    elif scene_has(_current_scene_id, "mentored_clinical"):
        if empathy_band() == "obedience":
            athought "He'll pass the audit. Passing keeps you alive here."
        elif empathy_band() == "empathy":
            athought "I put the weight in his mouth and told him to carry it. The system calls that training."
        else:
            athought "I handed him the script that hollows you out. I know how it ends."

    # ========= EXIT — DEMONSTRATION CALL =========
    # VISUAL: Intercom crackles. Bodies begin moving toward exits.
    # SOUND: Boot steps intensifying, then fading as corridor empties.

    voice "Units scheduled for demonstration: report at 14:00."

    "The hallway empties like a throat clearing—bodies filing out, leaving only echoes and fluorescent hum."

    athought "Fourteen-hundred. The demonstration writes itself behind my eyes."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_07b_barracks_morning
# cann.when_in_timeline: Morning barracks cycle; same day as Inspection scene; pre-Demonstration 14:00.
# cann.what_happened:
#   - Ration-line micro-incident (help / ignore / endorse priority).
#   - Junior recruit advice (humane / clinical / survival).
#   - Path flavor reflects current alignment band.
# cann.aeron_state: OB-lean baseline voice; band tint via flavor stingers.
# cann.path_tracking:
#   - Scene deltas:
#       • M1 (ration): help +1 EMP | ignore NEU | endorse -1 OB
#       • M2 (mentor): humane +1 EMP | survival NEU | clinical -1 OB
#     Scene span: -2 → +2
# cann.flags:
#   - Set: helped_worker | endorsed_priority | mentored_humane | mentored_clinical | completed
# cann.thematic_flags: Performance ritual; hierarchy optics; language as compliance UI; micro-mercy vs throughput.
# cann.block_status: VARIANT (micro-outcomes only); may feed light reputation/cred if tracking.
# cann.visual_plate_economy: One corridor master; toggle LED state + crowd density for both incidents.
# cann.requires_followup:
#   - If helped_worker: tiny goodwill ping from Unders contact much later (optional).
#   - If mentored_clinical: recruit shows up in a later op repeating the phrasing (echo).