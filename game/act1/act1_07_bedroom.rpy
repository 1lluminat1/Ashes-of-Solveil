# =======================================================
# ACT 1 - Scene 07: Aeron's Bedroom (After the Gala)
# =======================================================
# PURPOSE:
# Quiet aftermath of the gala and balcony scene.
# Aeron processes what just happened with Lyra and faces new orders.
# First visible hesitation in obedience → emotional split seed.
# =======================================================

label act1_07_bedroom:

    scene bg_aeron_room_night with fade
    "{i}Later that night...{/i}"

    a "{i}She didn’t say goodbye.{/i}"
    a "{i}Just gone. Like she was never there.{/i}"

    # --- Balcony callback ------------------------------------------------
    if check_scene_flag("act1_05_gala", "approach_lyra"):
        if check_scene_flag("act1_05_gala", "shares_light") and check_scene_flag("act1_05_gala", "holds_gaze"):
            a "{i}But I can still feel the space between us. Close enough to matter.{/i}"
            a "{i}Glass leaning toward glass. Almost touching. Almost shattering.{/i}"
        elif check_scene_flag("act1_05_gala", "shares_light"):
            a "{i}The flame. Her eyes. For a moment, we were just... us.{/i}"
            a "{i}Not Glass. Not performance. Just two people remembering what that felt like.{/i}"

    a "{i}Still... something was different in her eyes tonight.{/i}"
    a "{i}Not duty. Not protocol. Something real.{/i}"
    a "{i}She sees Glass. And she sees what’s underneath.{/i}"
    a "{i}Maybe I’m not the only one tired of pretending.{/i}"

    # VISUAL: On the desk—sealed mission order with Echelon crest; faint terminal glow.
    "{i}A sealed mission order waits on the desk. The Echelon crest bleeds crimson in the light.{/i}"

    # --- Empathy-based flavor --------------------------------------------
    $ score = player_state["empathy_score"]

    if score <= -4:
        a "{i}Silence is clarity. The hum beneath everything. The system breathing through me.{/i}"
    elif -3 <= score <= 1:
        a "{i}It’s quiet. Too quiet to tell if it’s peace or pressure.{/i}"
    else:
        a "{i}The room feels heavier than before. Every order adds weight. Even silence sounds like expectation.{/i}"

    # --- PLAYER CHOICE: Break or hesitate before opening the order -------
    menu:
        "The seal catches the light—Marcus’s insignia pressed into wax."
        "Break it immediately.":
            $ set_scene_flag("act1_07_bedroom", "hesitated_order")
            $ scenes["act1_07_bedroom"]["hesitated_order"] = False
            "{i}The seal snaps. Orders are always easier than silence.{/i}"
            a "{i}Glass doesn’t hesitate. Glass obeys.{/i}"

        "Hesitate for a breath.":
            $ set_scene_flag("act1_07_bedroom", "hesitated_order")
            $ player_state["empathy_score"] += 1
            $ score += 1
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

    if score <= -4:
        a "{i}They call it progress. They’re right. Every mission cleaner than the last.{/i}"
    elif -3 <= score <= 1:
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
            $ set_scene_flag("act1_07_bedroom", "acknowledged_marcus")
            "{i}The message leaves without ceremony.{/i}"
            a "{i}Glass confirms. Glass complies. Glass continues.{/i}"
            a "{i}391 operations. The count continues.{/i}"

        "Say nothing.":
            $ player_state["empathy_score"] += 1
            "{i}The cursor keeps blinking until the screen sleeps.{/i}"
            a "{i}Glass doesn’t respond. First time in 390 operations.{/i}"
            a "{i}The silence feels like rebellion. Or just exhaustion.{/i}"
    # ---------------------------------------------------------------------

    # VISUAL: Window reflection—Unders glowing like embers far below.
    a "{i}The Unders stay the same. The rest of us just pretend we’re different.{/i}"

    # --- Closing reflection ----------------------------------------------
    $ score = player_state["empathy_score"]

    if score <= -4:
        a "{i}Tonight changed nothing. Connection is noise. I can’t afford noise.{/i}"
        a "{i}'Glass recognizes glass'—and still chooses to hold form.{/i}"
        a "{i}Wholeness is a myth for those who hesitate.{/i}"
    elif -3 <= score <= 1:
        a "{i}She said, 'Glass recognizes glass.' Maybe she was right. Maybe she was wrong.{/i}"
        a "{i}But the thought won’t leave me.{/i}"
    else:
        a "{i}But tonight felt different. Lyra made it different.{/i}"
        a "{i}'Glass recognizes glass,' she said. Two polished surfaces. Both cracking. Both wondering if breaking means freedom or falling.{/i}"
        a "{i}Maybe breaking is the only way back to being whole.{/i}"

    "{i}The mission waits. It always does.{/i}"
    "{i}But tonight, the past won’t stay buried.{/i}"
    "{i}She asked if I remembered what wholeness felt like.{/i}"
    "{i}I don’t. But for a moment on that balcony, I almost did.{/i}"

    scene black with fade
    return
