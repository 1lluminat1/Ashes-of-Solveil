# =======================================================
# ACT 1 - Scene 07: Aeron's Bedroom (After the Gala)
# File: act1_07_bedroom.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_07_bedroom"
$ scene_mark(_current_scene_id, "entered")


label act1_07_bedroom:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Static 35–40mm; gentle 2% push on envelope reveal and on “mask slipped.”
    # LIGHTING: Night interior; cold city spill (5200K) through glass, warm desk practical (3000K) on orders.
    # SFX: Low HVAC hum, distant wind pressure against glass (Aeries altitude), terminal soft beeps.
    # FX/COMP: Window condensation/rim highlights; envelope wax glint; subtle screen bloom.
    # BLOCKING/PROPS: Sealed order with Echelon crest, powered terminal, opaque glass wall; keep face in partial silhouette early.
    # VOICE BASELINE: OB cadence (clipped/procedural); warmth only on EMP branches.

    # ========= ALIGNMENT SNAPSHOT =========
    $ tier = get_alignment_tier()           # OB3, OB2, OB1, C, EMP1, EMP2, EMP3
    $ band = get_empathy_band()             # "obedience" | "conflicted" | "empathy"
    $ norm = get_alignment_score_norm()     # -1.0 .. +1.0
    $ mom  = get_alignment_momentum()       # -1 .. +1

    # Convenience buckets
    $ is_ob_hard = pass_tier("OB3","OB2")           # ≤ -4
    $ is_mid     = pass_tier("OB1","C")             # -3 .. +1
    $ is_emp     = pass_tier("EMP1","EMP2","EMP3")  # ≥ +2

    scene bg_aeron_room_night with fade
    "Later that night..."

    athought "She didn’t say goodbye."
    athought "Just gone. Like she was never there."

    # --- Balcony callback ------------------------------------------------
    if check_scene_flag("act1_05_gala", "approach_lyra"):
        if check_scene_flag("act1_06_balcony", "shared_light") and check_scene_flag("act1_06_balcony", "held_gaze"):
            athought "But I can still feel the space between us. Close enough to matter."
            athought "Glass leaning toward glass. Almost touching. Almost shattering."
        elif check_scene_flag("act1_06_balcony", "shared_light"):
            athought "The flame. Her eyes. For a moment, we were just... us."
            athought "Not Glass. Not performance. Just two people remembering what that felt like."

    athought "Still... something was different in her eyes tonight."
    athought "Not duty. Not protocol. Something real."
    athought "She sees Glass. And she sees what’s underneath."
    athought "Maybe I’m not the only one tired of pretending."

    # VISUAL: On the desk—sealed mission order with Echelon crest; faint terminal glow.
    "A sealed mission order waits on the desk. The Echelon crest bleeds crimson in the light."

    # --- Empathy-based flavor --------------------------------------------
    if is_ob_hard:
        athought "Silence is clarity. The hum beneath everything. The system breathing through me."
    elif is_mid:
        athought "It’s quiet. Too quiet to tell if it’s peace or pressure."
    else:
        athought "The room feels heavier than before. Every order adds weight. Even silence sounds like expectation."

    # --- PLAYER CHOICE: Break or hesitate before opening the order -------
    menu:
        "The seal catches the light—Marcus’s insignia pressed into wax."
        "Break it immediately.":
            # Neutral (no OB/EMP delta) — record only
            $ record_choice_once(_current_scene_id, "_open_now",
                                next_scene_label="act1_07_bedroom",
                                note="No hesitation; performance reflex.")
            $ set_scene_flag(_current_scene_id, "opened_immediately")

            "The seal snaps. Orders are always easier than silence."
            athought "Glass doesn’t hesitate. Glass obeys."

        "Hesitate for a breath.":
            # EMP nudge
            $ choice_and_dev(
                _current_scene_id, "_hesitate_open", "EMP", factor=1,
                next_scene_label="act1_07_bedroom",
                note="Allows feeling to interrupt procedure."
            )
            $ set_scene_flag(_current_scene_id, "hesitated_order")

            "I hold it between my fingers, as if delay could change the words inside."
            "Then the seal breaks with a soft crack."

            athought "Glass hesitating. That’s new."
            athought "Or maybe the cracks are spreading faster than I thought."
    # ---------------------------------------------------------------------

    "The words are clean. Precise. Impersonal."
    athought "(reading) 'Sector 10 breach confirmed. Possible rebel intel leaks within Unders comm-grid.'"
    athought "'Sweep. Secure. Eliminate. Prove your worth.'"
    "Prove your worth. Always the same."

    athought "Sweep. Secure. Eliminate. Like I’m a task to complete, not a person."
    athought "Sector 10 makes 391."
    athought "Different orders. Same result. Same words. Same emptiness."

    if is_ob_hard:
        athought "They call it progress. They’re right. Every mission cleaner than the last."
    elif is_mid:
        athought "Progress, repetition—same thing after enough cycles."
    else:
        athought "They call it progress. I call it perfected apathy."

    athought "Still wearing the mask. Even alone."
    athought "But tonight... the mask slipped."
    athought "Lyra saw through Glass. And I let her."
    athought "That’s not what Glass does. Glass doesn’t let anyone see."

    # --- PLAYER CHOICE: Acknowledge Marcus or not ------------------------
    menu:
        "A blank message cursor blinks on the terminal."
        "Send a single-word acknowledgment: 'Received.'":
            $ choice_and_dev(
                _current_scene_id, "_ack_marcus", "OB", factor=1,
                next_scene_label="act1_07_bedroom",
                note="Confirms command without delay; reaffirms performance reflex."
            )
            $ set_scene_flag(_current_scene_id, "acknowledged_marcus")

            "The message leaves without ceremony."

            athought "Glass confirms. Glass complies. Glass continues."
            athought "391 operations. The count continues."

        "Say nothing.":
            $ choice_and_dev(
                _current_scene_id, "_ignore_marcus", "EMP", factor=1,
                next_scene_label="act1_07_bedroom",
                note="Withholds ritual confirmation; first visible noncompliance."
            )
            $ set_scene_flag(_current_scene_id, "ignored_marcus")

            "The cursor keeps blinking until the screen sleeps."

            athought "Glass doesn’t respond. First time in 390 operations."
            athought "The silence feels like rebellion. Or just exhaustion."
    # ---------------------------------------------------------------------

    # VISUAL: Window reflection—Unders glowing like embers far below.
    athought "The Unders stay the same. The rest of us just pretend we’re different."

    # --- Closing reflection ----------------------------------------------
    if is_ob_hard:
        athought "Tonight changed nothing. Connection is noise. I can’t afford noise."
        athought "'Glass recognizes glass'—and still chooses to hold form."
        athought "Wholeness is a myth for those who hesitate."
    elif is_mid:
        athought "She said, 'Glass recognizes glass.' Maybe she was right. Maybe she was wrong."
        athought "But the thought won’t leave me."
    else:
        athought "But tonight felt different. Lyra made it different."
        athought "'Glass recognizes glass,' she said. Two polished surfaces. Both cracking. Both wondering if breaking means freedom or falling."
        athought "Maybe breaking is the only way back to being whole."

    "The mission waits. It always does."
    "But tonight, the past won’t stay buried."

    athought "She asked if I remembered what wholeness felt like."
    athought "I don’t. But for a moment on that balcony, I almost did."

    scene black with fade

    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_07_bedroom
# cann.when_in_timeline: Night after Gala/Balcony; pre–Sector 10 deployment.
# cann.what_happened:
#   - Aeron processes Balcony micro-intimacy; acknowledges mask slippage.
#   - Orders arrive: Sector 10 sweep/secure/eliminate; “Prove your worth.”
#   - Player chooses (1) immediate open (NEU) vs hesitation (EMP +1), and (2) acknowledgment to Marcus (OB −1) vs silence (EMP +1).
# cann.aeron_state: OB baseline voice; branches show first explicit, visible hesitation.
# cann.path_tracking:
#   - Incoming running range:  [-11, +8]   # post-Gala (A1_05) + Balcony (A1_06 no change)
#   - Scene deltas:
#       • M1 (order seal):     opened_immediately 0 NEU | hesitated_order +1 EMP
#       • M2 (terminal reply): acknowledged_marcus −1 OB | ignored_marcus +1 EMP
#     Net per-scene span: **−1 → +2** (OB counted as −).
#   - Outgoing running range: [-12, +10]
# cann.flags: opened_immediately | hesitated_order | acknowledged_marcus | ignored_marcus
# cann.thematic_flags:
#   - Motifs: Mask/Performance, Glass/Cracks, Orders-as-Identity, Worth/Counting (“391”).
#   - Recurring lines: “Prove your worth.” “Glass doesn’t hesitate / let anyone see.”
# cann.block_status: ANCHOR scene with light VARIANTS (two menus).
# cann.true_path_integration: none (menus never touch TP).
# cann.visual_plate_economy:
#   - REUSE: Bedroom night master (city spill on glass); desk close-up with order; monitor glow plate.
#   - HERO: Wax-seal macro; window reflection of Aeron on “mask slipped.”
# cann.requires_followup:
#   - Route to **Sector 10 departure/setup**; branch tone via flags:
#       • `opened_immediately` + `acknowledged_marcus` → colder prep VO.
#       • `hesitated_order` or `ignored_marcus` → introspective prep VO.
# cann.consistency_asserts:
#   - Aeries altitude: no rain-on-glass; use wind pressure/condensation language only.
#   - Keep Marcus phrasing (“Prove your worth”) aligned to doctrine diction.
# cann.qa_hooks:
#   - Log NEU choice with `record_choice_once` (for `opened_immediately`) to preserve audit without shifting alignment.
#   - Ensure `_current_scene_id` and label match (consider renaming `label act1_bedroom_after_gala` → `label act1_07_bedroom` for 1:1 log correlation).