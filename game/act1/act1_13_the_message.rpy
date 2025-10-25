# act1_13_the_message.rpy


# ======================================================
# ACT 1 - Scene 13: The Message
# ======================================================


label act1_the_message:
    $ scene_id = "act1_13_the_message"

    # Alignment reads (light flavor only; no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    $ band = get_empathy_band()                   # "obedience" | "conflicted" | "empathy"

    # VISUAL: Aeron's apartment after Lyra leaves; door closed, room dim.
    # LIGHTING: Blue-grey ambient; terminal glow from desk.
    # SOUND: Ventilation hum; distant city drone; rain starting outside.

    "{i}The door seals behind her. The room exhales.{/i}"
    a "{i}She came back. Twice now.{/i}"
    a "{i}Glass recognizes glass. Maybe that's all we need.{/i}"
    a "{i}Maybe breaking together is better than shattering alone.{/i}"

    "{i}He moves to the desk. The weight of the night settles.{/i}"

    # --- Marcus's mission order arrives ---
    "{i}The terminal chimes. Urgent. Command priority.{/i}"
    "{i}Marcus's seal. Another mission.{/i}"
    a "{i}Of course. Glass doesn’t get to rest.{/i}"
    a "{i}Operation 391.{/i}"

    # --- PLAYER CHOICE: open or hesitate ---
    menu:
        "The notification blinks. Insistent. Command priority."
        "Open the message.":
            $ set_scene_flag(scene_id, "opened_order")
            "{i}He taps the screen. Marcus’s orders unfold.{/i}"

        "Hesitate.":
            "{i}His hand hovers. For a moment, he considers walking away.{/i}"
            a "{i}Glass hesitating. Again.{/i}"
            "{i}But the chime repeats. Command priority. Disobedience isn’t an option.{/i}"
            "{i}He opens it.{/i}"
            $ adjust_empathy_once("message_hesitated_order", +1)
            $ set_scene_flag(scene_id, "hesitated_order")

    # Alignment echo — one breath after opening Marcus's order
    $ band = get_empathy_band()
    if band == "obedience":
        a "{i}Orders feel like oxygen. Simple. Clean.{/i}"
    elif band == "conflicted":
        a "{i}Orders feel like weight. Easier to lift than to understand.{/i}"
    else:  # empathy
        a "{i}Orders feel heavier than they used to. Names hide inside them.{/i}"

    # --- Mission contents ---
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
    "{i}A second chime cuts through his thoughts. Different tone.{/i}"
    "{i}Unmarked sender. Encrypted.{/i}"
    a "{i}Unmarked means encrypted. Encrypted means trouble.{/i}"
    a "{i}Or answers.{/i}"

    # --- PLAYER CHOICE: open or ignore ---
    menu:
        "Two messages. One from Father. One from... unknown."
        "Open the unmarked message.":
            $ set_scene_flag(scene_id, "opened_zira")
            "{i}He swipes Marcus’s order aside. The encrypted message decrypts.{/i}"

        "Ignore it and read Marcus’s order again.":
            "{i}He tries to focus on the mission parameters.{/i}"
            a "{i}Orders first. Distractions later.{/i}"
            "{i}But the chime repeats. Again. Again.{/i}"
            a "{i}Persistent bastard.{/i}"
            "{i}He opens it.{/i}"
            $ set_scene_flag(scene_id, "opened_zira")
            $ set_scene_flag(scene_id, "hesitated_zira")

    # --- Zira’s message text ---
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

    "{i}Rain taps the glass. The city hums below.{/i}"

    # --- PLAYER CHOICE: act now or wait ---
    menu:
        "The coordinates burn in his memory. Sector 10. Tonight or tomorrow."
        "Go to the Lower Spans now.":
            $ set_scene_flag(scene_id, "goes_early")
            # small nudge only if clearly on the empathy side
            if band == "empathy":
                $ adjust_empathy_once("message_go_early_emp", +1)
            a "{i}If someone’s watching me, I’d rather meet them on my terms.{/i}"
            a "{i}Before dawn. Before the sweep. Before Glass follows orders again.{/i}"
            "{i}He grabs his coat. Marcus’s mission order stays on screen, unanswered.{/i}"
            a "{i}Glass hesitates. Glass questions. Glass disobeys.{/i}"

        "Wait and think it through.":
            $ set_scene_flag(scene_id, "waited")
            a "{i}Rushing into traps is how people disappear.{/i}"
            "{i}He sits. The rain fills the silence.{/i}"
            a "{i}What would you do, Kael? Walk into the dark or wait for dawn?{/i}"
            a "{i}'Don’t let Father turn you into a weapon,' you said.{/i}"
            a "{i}But staying here, following orders... that’s exactly what Glass does.{/i}"
            "{i}He grabs his coat.{/i}"
            a "{i}Maybe it’s time to stop being Glass.{/i}"

    "{i}The hallway is empty. Cameras blink red in the corners.{/i}"
    a "{i}They’re always watching. Question is—who else is?{/i}"

    "{i}The elevator descends into the dark.{/i}"
    a "{i}Operation 391 starts at dawn. But tonight...{/i}"
    a "{i}Tonight, Glass decides to see what it’s really cutting.{/i}"

    $ set_scene_flag(scene_id, "completed")
    return
