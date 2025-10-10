# act1_09_breaking_point.rpy


# ======================================================
# ACT 1 - Scene 9: Aeron's Breaking Point
# ======================================================


label act1_breaking_point:
    # VISUAL: Aeron’s room, later that night. The city glows cold blue through the window. 
    # A single photo of his brother sits on the desk. The envelope from Marcus still open. 
    # Quiet. Just the low hum of the city outside.
    # Aeron sits at the desk, staring at the photo.
    a "{i}You always smiled like you belonged...{/i}"
    a "{i}Even with the band burning your skin, you smiled.{/i}"
    a "{i}And then one day you just… stopped..{/i}"

    # Camera moves closer on the photo — Aeron’s brother, arm over his shoulder, the band just visible.
    a "{i}I used to hate you for leaving me here.{/i}"
    a "{i}Now... I think I understand why.{/i}"

    # Aeron stands, takes the photo, sets it down gently.
    a "{i}I don’t even know if I’m angry anymore. Just tired.{/i}"
    a "{i}Tired of pretending any of this means something.{/i}"

    # He walks to the balcony door. Opens it. Wind drifts in, cold and metallic.
    "{i}He opens the balcony door. Cold air moves through the room.{/i}"
    "{i}He steps outside. The city sprawls below, endless and uncaring.{/i}"

    # Aeron lights a cigarette. Hands shake. Smoke drifts upward.
    a "{i}One last smoke...{/i}"
    "{i}His hands shake as he lights it. Smoke climbs into the dark.{/i}"

    # He exhales, stares at the edge of the railing.
    a "{i}Maybe if I step over, it’ll finally be quiet.{/i}"
    a "{i}No more missions.{/i}"
    a "{i}No more whispers.{/i}"
    a "{i}No more failure.{/i}"

    # Camera pans low — his foot on the railing, hands gripping cold metal.
    "{i}The wind tugs at his coat. Below, the city stirs — restless, endless, alive.{/i}"

    # --- PLAYER CHOICE ---
    menu:
        "Step forward":
            a "{i}Just one more step...{/i}"
        "Step back":
            a "{i}I can't keep living like this...{/i}"

    # Regardless of choice, knock interrupts.
    # A sharp double knock at the door. Startling. Cigarette trembles between his fingers.
    "{i}A knock at the door. Sharp. Sudden. Like fate itself rapping against the walls.{/i}"

    a "{i}...Lyra?{/i}"  # (optional mutter under his breath)
    # Aeron steps back down from the railing, still shaken.

    "{i}He drops back to the stone. The city noise thins; his heartbeat doesn’t.{/i}"
    # Fade to black or transition to Lyra’s entrance scene.
    return