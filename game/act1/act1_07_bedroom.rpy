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
    "{i}Later that night...{/i}"

    a "{i}She didn’t say goodbye.{/i}"
    a "{i}Just gone. Like she was never there.{/i}"

    # --- Balcony callback ------------------------------------------------
    if check_scene_flag("act1_05_gala", "approach_lyra"):
        if check_scene_flag("act1_06_balcony", "shared_light") and check_scene_flag("act1_06_balcony", "held_gaze"):
            a "{i}But I can still feel the space between us. Close enough to matter.{/i}"
            a "{i}Glass leaning toward glass. Almost touching. Almost shattering.{/i}"
        elif check_scene_flag("act1_06_balcony", "shared_light"):
            a "{i}The flame. Her eyes. For a moment, we were just... us.{/i}"
            a "{i}Not Glass. Not performance. Just two people remembering what that felt like.{/i}"

    a "{i}Still... something was different in her eyes tonight.{/i}"
    a "{i}Not duty. Not protocol. Something real.{/i}"
    a "{i}She sees Glass. And she sees what’s underneath.{/i}"
    a "{i}Maybe I’m not the only one tired of pretending.{/i}"

    # VISUAL: On the desk—sealed mission order with Echelon crest; faint terminal glow.
    "{i}A sealed mission order waits on the desk. The Echelon crest bleeds crimson in the light.{/i}"

    # --- Empathy-based flavor --------------------------------------------
    if is_ob_hard:
        a "{i}Silence is clarity. The hum beneath everything. The system breathing through me.{/i}"
    elif is_mid:
        a "{i}It’s quiet. Too quiet to tell if it’s peace or pressure.{/i}"
    else:
        a "{i}The room feels heavier than before. Every order adds weight. Even silence sounds like expectation.{/i}"

    # --- PLAYER CHOICE: Break or hesitate before opening the order -------
    menu:
        "The seal catches the light—Marcus’s insignia pressed into wax."
        "Break it immediately.":
            # Neutral (no OB/EMP delta) — record only
            $ record_choice_once(_current_scene_id, "_open_now",
                                next_scene_label="act1_07_bedroom",
                                note="No hesitation; performance reflex.")
            $ set_scene_flag(_current_scene_id, "opened_immediately")

            "{i}The seal snaps. Orders are always easier than silence.{/i}"
            a "{i}Glass doesn’t hesitate. Glass obeys.{/i}"

        "Hesitate for a breath.":
            # EMP nudge
            $ apply_choice_once(
                _current_scene_id, "_hesitate_open", "EMP", factor=1,
                next_scene_label="act1_07_bedroom",
                note="Allows feeling to interrupt procedure."
            )
            $ set_scene_flag(_current_scene_id, "hesitated_order")

            "{i}I hold it between my fingers, as if delay could change the words inside.{/i}"
            "{i}Then the seal breaks with a soft crack.{/i}"

            a "{i}Glass hesitating. That’s new.{/i}"
            a "{i}Or maybe the cracks are spreading faster than I thought.{/i}"
    # ---------------------------------------------------------------------

    "{i}The words are clean. Precise. Impersonal.{/i}"
    a "{i}(reading) 'Sector 10 breach confirmed. Possible rebel intel leaks within Unders comm-grid.'{/i}"
    a "{i}'Sweep. Secure. Eliminate. Prove your worth.'{/i}"
    "{i}Prove your worth. Always the same.{/i}"

    a "{i}Sweep. Secure. Eliminate. Like I’m a task to complete, not a person.{/i}"
    a "{i}Sector 10 makes 391.{/i}"
    a "{i}Different orders. Same result. Same words. Same emptiness.{/i}"

    if is_ob_hard:
        a "{i}They call it progress. They’re right. Every mission cleaner than the last.{/i}"
    elif is_mid:
        a "{i}Progress, repetition—same thing after enough cycles.{/i}"
    else:
        a "{i}They call it progress. I call it perfected apathy.{/i}"

    a "{i}Still wearing the mask. Even alone.{/i}"
    a "{i}But tonight... the mask slipped.{/i}"
    a "{i}Lyra saw through Glass. And I let her.{/i}"
    a "{i}That’s not what Glass does. Glass doesn’t let anyone see.{/i}"

    # --- PLAYER CHOICE: Acknowledge Marcus or not ------------------------
    menu:
        "A blank message cursor blinks on the terminal."
        "Send a single-word acknowledgment: 'Received.'":
            $ apply_choice_once(
                _current_scene_id, "_ack_marcus", "OB", factor=1,
                next_scene_label="act1_07_bedroom",
                note="Confirms command without delay; reaffirms performance reflex."
            )
            $ set_scene_flag(_current_scene_id, "acknowledged_marcus")

            "{i}The message leaves without ceremony.{/i}"

            a "{i}Glass confirms. Glass complies. Glass continues.{/i}"
            a "{i}391 operations. The count continues.{/i}"

        "Say nothing.":
            $ apply_choice_once(
                _current_scene_id, "_ignore_marcus", "EMP", factor=1,
                next_scene_label="act1_07_bedroom",
                note="Withholds ritual confirmation; first visible noncompliance."
            )
            $ set_scene_flag(_current_scene_id, "ignored_marcus")

            "{i}The cursor keeps blinking until the screen sleeps.{/i}"

            a "{i}Glass doesn’t respond. First time in 390 operations.{/i}"
            a "{i}The silence feels like rebellion. Or just exhaustion.{/i}"
    # ---------------------------------------------------------------------

    # VISUAL: Window reflection—Unders glowing like embers far below.
    a "{i}The Unders stay the same. The rest of us just pretend we’re different.{/i}"

    # --- Closing reflection ----------------------------------------------
    if is_ob_hard:
        a "{i}Tonight changed nothing. Connection is noise. I can’t afford noise.{/i}"
        a "{i}'Glass recognizes glass'—and still chooses to hold form.{/i}"
        a "{i}Wholeness is a myth for those who hesitate.{/i}"
    elif is_mid:
        a "{i}She said, 'Glass recognizes glass.' Maybe she was right. Maybe she was wrong.{/i}"
        a "{i}But the thought won’t leave me.{/i}"
    else:
        a "{i}But tonight felt different. Lyra made it different.{/i}"
        a "{i}'Glass recognizes glass,' she said. Two polished surfaces. Both cracking. Both wondering if breaking means freedom or falling.{/i}"
        a "{i}Maybe breaking is the only way back to being whole.{/i}"

    "{i}The mission waits. It always does.{/i}"
    "{i}But tonight, the past won’t stay buried.{/i}"

    a "{i}She asked if I remembered what wholeness felt like.{/i}"
    a "{i}I don’t. But for a moment on that balcony, I almost did.{/i}"

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