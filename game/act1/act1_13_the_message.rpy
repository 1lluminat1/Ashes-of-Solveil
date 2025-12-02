# ======================================================
# ACT 1 - Scene 13: The Message
# File: act1_13_the_message.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_13_the_message"
$ scene_mark(_current_scene_id, "entered")


label act1_the_message:

    # Alignment reads (light flavor only; no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    $ band = get_empathy_band()                   # "obedience" | "conflicted" | "empathy"

    # VISUAL: Aeron's apartment after Lyra leaves; door closed, room dim.
    # LIGHTING: Blue-grey ambient; terminal idle glow at desk; skyline spill cool.
    # SFX: Building ventilation; high-tier wind pressure ticking facade fins; distant city drone.
    # CAMERA: Slow push from door to desk.

    "The door seals behind her. The room exhales."

    athought "She came back. Twice now."
    athought "Glass recognizes glass. Maybe that's all we need."
    athought "Maybe breaking together is better than shattering alone."

    "He moves to the desk. The weight of the night settles."

    # --- Marcus's mission order arrives ---
    # UI: Terminal notification pulse; crest watermark bloom.
    "The terminal chimes. Urgent. Command priority."
    "Marcus's seal. Another mission."

    athought "Of course. Glass doesn’t get to rest."
    athought "Operation 391."

    # --- PLAYER CHOICE: open or hesitate (neutral vs EMP +1) ---
    menu:
        "The notification blinks. Insistent. Command priority."
        "Open the message.":
            $ record_choice_once(
                _current_scene_id, "message_opened_immediately",
                next_scene_label="act1_13_the_message",
                note="Opened Marcus order without hesitation."
            )
            $ set_scene_flag(scene_id, "opened_order")

            "He taps the screen. Marcus’s orders unfold."

        "Hesitate.":
            $ choice_and_dev(
                _current_scene_id, "message_hesitated_order", "EMP", factor=1,
                next_scene_label="act1_13_the_message",
                note="Aeron pauses before opening Marcus order."
            )
            $ set_scene_flag(scene_id, "hesitated_order")

            "His hand hovers. For a moment, he considers walking away."

            athought "Glass hesitating. Again."

            "The chime repeats. Command priority. He opens it."

    # Alignment echo — one breath after opening Marcus's order
    # LIGHTING: Terminal white lifts a notch on his face.
    $ band = get_empathy_band()
    if band == "obedience":
        athought "Orders feel like oxygen. Simple. Clean."
    elif band == "conflicted":
        athought "Orders feel like weight. Easier to lift than to understand."
    else:  # empathy
        athought "Orders feel heavier than they used to. Names hide inside them."

    # --- Mission contents ---
    # UI: Directive text scroll, subtle vignette.
    "OPERATION DIRECTIVE - PRIORITY ALPHA"
    "CLASSIFICATION: SECTOR STABILIZATION"
    "AUTHORIZATION: HIGH MARSHAL MARCUS RYLAN"

    athought "(reading) 'Sector 10 – Lower Spans. Comprehensive sweep operation.'"
    athought "'Objective: Eliminate all hostile elements. Zero tolerance protocol.'"

    "Zero tolerance. No survivors. Total sweep."

    athought "'Expected civilian collateral: Acceptable within mission parameters.'"

    athought "Acceptable collateral."
    athought "200 to 500 people. Reduced to numbers. To metrics."
    athought "Operation 391. The count continues."

    # --- Empathy-tone reflection ---
    if is_ob_hard:
        athought "Collateral is efficiency. Efficiency is mercy in scale."
        athought "Marcus taught me that. I believed him once. Still do, mostly."
    elif is_mid:
        athought "Collateral. The word tastes wrong now."
        athought "Maybe it always did. I just stopped tasting anything for a while."
    else:
        athought "Collateral. A word to hide the bodies under metrics."
        athought "I see their faces already. And I haven’t even left yet."

    # --- Second message appears ---
    # UI: Off-pattern chime; envelope icon glitches; header masked.
    "A second chime cuts through his thoughts. Different tone."
    "Unmarked sender. Encrypted."

    athought "Unmarked means encrypted. Encrypted means trouble."
    athought "Or answers."

    # --- PLAYER CHOICE: open or ignore (record-only variants) ---
    menu:
        "Two messages. One from Father. One from... unknown."
        "Open the unmarked message.":
            $ record_choice_once(
                _current_scene_id, "zira_open_immediate",
                next_scene_label="act1_13_the_message",
                note="Opened the anonymous message immediately."
            )
            $ set_scene_flag(scene_id, "opened_zira")

            "He swipes Marcus’s order aside. The encrypted message decrypts."

        "Ignore it and read Marcus’s order again.":
            $ record_choice_once(
                _current_scene_id, "zira_ignored_then_opened",
                next_scene_label="act1_13_the_message",
                note="Ignored the anonymous ping at first, then opened after repeats."
            )

            "He tries to focus on the mission parameters."
            
            athought "Orders first. Distractions later."

            "But the chime repeats. Again. Again."

            athought "Persistent bastard."

            "He opens it."

            $ set_scene_flag(scene_id, "opened_zira")
            $ set_scene_flag(scene_id, "hesitated_zira")

    # --- Zira’s message text (cps reveal) ---
    # CAMERA: Tight on terminal; reflection of Aeron eyes in glass.
    "{cps=30}SECTOR 10. LOWER SPANS.{/cps}"
    "{cps=30}NORTHEAST EDGE. GRID SIX-TWO.{/cps}"
    "{cps=30}TONIGHT. COME ALONE.{/cps}"
    "{cps=30}THEY’RE WATCHING YOU.{/cps}"
    "{cps=30}I CAN SHOW YOU WHY.{/cps}"
    "{cps=30}THE TRUTH IS IN THE SHADOWS.{/cps}"

    "The text dissolves. Gone before he can capture it."

    athought "Self-deleting. Professional. Or paranoid."

    "His eyes move between the two messages."

    athought "Sector 10. Same coordinates."
    athought "Father orders me to sweep it at dawn."
    athought "Someone else wants me there tonight."

    # --- Empathy-tone internal response ---
    if is_ob_hard:
        athought "Coincidence is noise. But protocol says confirm anomalies."
        athought "I’ll go. Verify. Report. Order in chaos."
    elif is_mid:
        athought "It feels deliberate. Like someone’s testing me."
        athought "But curiosity’s a kind of defiance now, isn’t it?"
    else:
        athought "It feels deliberate. Like someone’s giving me a chance to see what I’m part of."
        athought "Before I make it worse."

    "No trace. No proof it ever existed except memory."

    a "Who the hell are you?"
    athought "And why do you want me to see Sector 10 before I destroy it?"

    # WEATHER GRAMMAR: High-tier—no rain; facade pressure + condensation.
    "Wind ticks against the facade fins. Condensation halos the glass edge."

    # --- PLAYER CHOICE: act now or wait (record vs conditional EMP +1) ---
    menu:
        "The coordinates burn in his memory. Sector 10. Tonight or tomorrow."
        "Go to the Lower Spans now.":
            $ set_scene_flag(scene_id, "goes_early")
            if band == "empathy":
                $ choice_and_dev(
                    _current_scene_id, "message_go_early_emp", "EMP", factor=1,
                    next_scene_label="act1_13_the_message",
                    note="Chooses to go early; empathy-lean nudge."
                )
            else:
                $ record_choice_once(
                    _current_scene_id, "message_go_early_neutral",
                    next_scene_label="act1_13_the_message",
                    note="Goes early without empathy nudge."
                )

            athought "If someone’s watching me, I’d rather meet them on my terms."
            athought "Before dawn. Before the sweep. Before Glass follows orders again."

            "He grabs his coat. Marcus’s mission order stays on screen, unanswered."

            athought "Glass hesitates. Glass questions. Glass disobeys."

        "Wait and think it through.":
            $ record_choice_once(
                _current_scene_id, "message_waited",
                next_scene_label="act1_13_the_message",
                note="Waits to plan; goes later anyway."
            )
            $ set_scene_flag(scene_id, "waited")

            athought "Rushing into traps is how people disappear."

            "He sits. The wind fills the silence."

            athought "What would you do, Kael? Walk into the dark or wait for dawn?"
            athought "'Don’t let Father turn you into a weapon,' you said."
            athought "But staying here, following orders... that’s exactly what Glass does."

            "He grabs his coat."

            athought "Maybe it’s time to stop being Glass."

    # EXIT: Corridor + elevator
    # VISUAL: Hallway empty; security lenses blink.
    # SFX: Elevator cable hum; distant service drone.
    "The hallway is empty. Cameras blink red in the corners."

    athought "They’re always watching. Question is—who else is?"

    "The elevator descends into the dark."

    athought "Operation 391 starts at dawn. But tonight..."
    athought "Tonight, Glass decides to see what it’s really cutting."

    $ set_scene_flag(scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_13_the_message
# cann.when_in_timeline: Same night as Lyra visit; pre–Sector 10 departure; Op391 at dawn.
# cann.what_happened:
#   - Marcus issues Priority Alpha sweep (zero-tolerance; “acceptable collateral”).
#   - Anonymous ping (Zira) invites a night visit to Sector 10 (“truth in the shadows”).
#   - Player: (A) Hesitate Marcus order (EMP+1) vs open (NEU); (B) Open Zira now vs ignore-first (NEU);
#     (C) Go now (conditional EMP+1 if already in empathy band) vs Wait (NEU).
# cann.aeron_state: OB treats anomaly as protocol check; EMP reads it as moral prompt; VO tint only.
# cann.path_tracking:
#   - Delta by menu:
#       • A: Hesitate → EMP(+1) | Open → NEU (record_choice_only)
#       • B: Zira open style → NEU (record_choice_only)
#       • C: Go now → EMP(+1) only if band == "empathy"; else NEU | Wait → NEU
#   - Scene empathy delta range: **0 → +2**
#   - Running window BEFORE:  **≈ [-29, +27]**
#       # derivation chain (max spread):
#       # 07_Bedroom [-16,+14] → +Inspection (±6) → [-22,+20] → +Barracks (±2) → [-24,+22]
#       # → +Demo Floor (±2) → [-26,+24] → +Archive (±2) → [-28,+26]
#       # → +Debrief (±1) → [-29,+27] → +Breaking Point (0) → +Lyra Visit (0)
#   - Running window AFTER:   **≈ [-29, +29]**  (no negative outs this scene; max +2 on EMP)
#   - Flags: opened_order / hesitated_order; opened_zira / hesitated_zira; goes_early / waited; completed.
# cann.thematic_flags: Orders-as-oxygen vs weight; metrics hiding bodies; anomaly as invitation to truth.
# cann.block_status: ANCHOR (kicks Sector 10 arc) with VARIANT timing + recorded intent.
# cann.true_path_integration: none (menu-free TP rule holds).
# cann.visual_plate_economy:
#   - REUSE: Bedroom/desk master; terminal UI overlay; corridor lens blink; elevator cab.
#   - HERO: Crest macro; decrypt text crawl; over-glass eye reflection on message.
# cann.requires_followup:
#   - If `goes_early`: route to night approach in Sector 10 (Zira meet seed).
#   - If `waited`: route to dawn staging; alter/delay Zira contact.
# cann.consistency_asserts:
#   - Aeries weather grammar only (wind/pressure/condensation; no rain).
#   - Count integrity: Aeron 22; next op number = 391.