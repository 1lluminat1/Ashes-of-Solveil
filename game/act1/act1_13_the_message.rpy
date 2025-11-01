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

    "{i}The door seals behind her. The room exhales.{/i}"

    a "{i}She came back. Twice now.{/i}"
    a "{i}Glass recognizes glass. Maybe that's all we need.{/i}"
    a "{i}Maybe breaking together is better than shattering alone.{/i}"

    "{i}He moves to the desk. The weight of the night settles.{/i}"

    # --- Marcus's mission order arrives ---
    # UI: Terminal notification pulse; crest watermark bloom.
    "{i}The terminal chimes. Urgent. Command priority.{/i}"
    "{i}Marcus's seal. Another mission.{/i}"

    a "{i}Of course. Glass doesn’t get to rest.{/i}"
    a "{i}Operation 391.{/i}"

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

            "{i}He taps the screen. Marcus’s orders unfold.{/i}"

        "Hesitate.":
            $ apply_choice_once(
                _current_scene_id, "message_hesitated_order", "EMP", factor=1,
                next_scene_label="act1_13_the_message",
                note="Aeron pauses before opening Marcus order."
            )
            $ set_scene_flag(scene_id, "hesitated_order")

            "{i}His hand hovers. For a moment, he considers walking away.{/i}"

            a "{i}Glass hesitating. Again.{/i}"

            "{i}The chime repeats. Command priority. He opens it.{/i}"

    # Alignment echo — one breath after opening Marcus's order
    # LIGHTING: Terminal white lifts a notch on his face.
    $ band = get_empathy_band()
    if band == "obedience":
        a "{i}Orders feel like oxygen. Simple. Clean.{/i}"
    elif band == "conflicted":
        a "{i}Orders feel like weight. Easier to lift than to understand.{/i}"
    else:  # empathy
        a "{i}Orders feel heavier than they used to. Names hide inside them.{/i}"

    # --- Mission contents ---
    # UI: Directive text scroll, subtle vignette.
    "{i}OPERATION DIRECTIVE - PRIORITY ALPHA{/i}"
    "{i}CLASSIFICATION: SECTOR STABILIZATION{/i}"
    "{i}AUTHORIZATION: HIGH MARSHAL MARCUS RYLAN{/i}"

    a "{i}(reading) 'Sector 10 – Lower Spans. Comprehensive sweep operation.'{/i}"
    a "{i}'Objective: Eliminate all hostile elements. Zero tolerance protocol.'{/i}"

    "{i}Zero tolerance. No survivors. Total sweep.{/i}"

    a "{i}'Expected civilian collateral: Acceptable within mission parameters.'{/i}"

    a "{i}Acceptable collateral.{/i}"
    a "{i}200 to 500 people. Reduced to numbers. To metrics.{/i}"
    a "{i}Operation 391. The count continues.{/i}"

    # --- Empathy-tone reflection ---
    if is_ob_hard:
        a "{i}Collateral is efficiency. Efficiency is mercy in scale.{/i}"
        a "{i}Marcus taught me that. I believed him once. Still do, mostly.{/i}"
    elif is_mid:
        a "{i}Collateral. The word tastes wrong now.{/i}"
        a "{i}Maybe it always did. I just stopped tasting anything for a while.{/i}"
    else:
        a "{i}Collateral. A word to hide the bodies under metrics.{/i}"
        a "{i}I see their faces already. And I haven’t even left yet.{/i}"

    # --- Second message appears ---
    # UI: Off-pattern chime; envelope icon glitches; header masked.
    "{i}A second chime cuts through his thoughts. Different tone.{/i}"
    "{i}Unmarked sender. Encrypted.{/i}"

    a "{i}Unmarked means encrypted. Encrypted means trouble.{/i}"
    a "{i}Or answers.{/i}"

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

            "{i}He swipes Marcus’s order aside. The encrypted message decrypts.{/i}"

        "Ignore it and read Marcus’s order again.":
            $ record_choice_once(
                _current_scene_id, "zira_ignored_then_opened",
                next_scene_label="act1_13_the_message",
                note="Ignored the anonymous ping at first, then opened after repeats."
            )

            "{i}He tries to focus on the mission parameters.{/i}"
            
            a "{i}Orders first. Distractions later.{/i}"

            "{i}But the chime repeats. Again. Again.{/i}"

            a "{i}Persistent bastard.{/i}"

            "{i}He opens it.{/i}"

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

    "{i}The text dissolves. Gone before he can capture it.{/i}"

    a "{i}Self-deleting. Professional. Or paranoid.{/i}"

    "{i}His eyes move between the two messages.{/i}"

    a "{i}Sector 10. Same coordinates.{/i}"
    a "{i}Father orders me to sweep it at dawn.{/i}"
    a "{i}Someone else wants me there tonight.{/i}"

    # --- Empathy-tone internal response ---
    if is_ob_hard:
        a "{i}Coincidence is noise. But protocol says confirm anomalies.{/i}"
        a "{i}I’ll go. Verify. Report. Order in chaos.{/i}"
    elif is_mid:
        a "{i}It feels deliberate. Like someone’s testing me.{/i}"
        a "{i}But curiosity’s a kind of defiance now, isn’t it?{/i}"
    else:
        a "{i}It feels deliberate. Like someone’s giving me a chance to see what I’m part of.{/i}"
        a "{i}Before I make it worse.{/i}"

    "{i}No trace. No proof it ever existed except memory.{/i}"

    a "Who the hell are you?"
    a "{i}And why do you want me to see Sector 10 before I destroy it?{/i}"

    # WEATHER GRAMMAR: High-tier—no rain; facade pressure + condensation.
    "{i}Wind ticks against the facade fins. Condensation halos the glass edge.{/i}"

    # --- PLAYER CHOICE: act now or wait (record vs conditional EMP +1) ---
    menu:
        "The coordinates burn in his memory. Sector 10. Tonight or tomorrow."
        "Go to the Lower Spans now.":
            $ set_scene_flag(scene_id, "goes_early")
            if band == "empathy":
                $ apply_choice_once(
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

            a "{i}If someone’s watching me, I’d rather meet them on my terms.{/i}"
            a "{i}Before dawn. Before the sweep. Before Glass follows orders again.{/i}"

            "{i}He grabs his coat. Marcus’s mission order stays on screen, unanswered.{/i}"

            a "{i}Glass hesitates. Glass questions. Glass disobeys.{/i}"

        "Wait and think it through.":
            $ record_choice_once(
                _current_scene_id, "message_waited",
                next_scene_label="act1_13_the_message",
                note="Waits to plan; goes later anyway."
            )
            $ set_scene_flag(scene_id, "waited")

            a "{i}Rushing into traps is how people disappear.{/i}"

            "{i}He sits. The wind fills the silence.{/i}"

            a "{i}What would you do, Kael? Walk into the dark or wait for dawn?{/i}"
            a "{i}'Don’t let Father turn you into a weapon,' you said.{/i}"
            a "{i}But staying here, following orders... that’s exactly what Glass does.{/i}"

            "{i}He grabs his coat.{/i}"

            a "{i}Maybe it’s time to stop being Glass.{/i}"

    # EXIT: Corridor + elevator
    # VISUAL: Hallway empty; security lenses blink.
    # SFX: Elevator cable hum; distant service drone.
    "{i}The hallway is empty. Cameras blink red in the corners.{/i}"

    a "{i}They’re always watching. Question is—who else is?{/i}"

    "{i}The elevator descends into the dark.{/i}"

    a "{i}Operation 391 starts at dawn. But tonight...{/i}"
    a "{i}Tonight, Glass decides to see what it’s really cutting.{/i}"

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