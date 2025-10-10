# act1_06_balcony.rpy


# ===================================================
# ACT 1 - Scene 6: Aeron's Bedroom After the Gala
# ===================================================

label act1_bedroom_after_gala:
    "{i}Later that night...{/i}"

    # VISUAL: Aeron's room in shadow; city light stutters across the tall window.

    a "{i}She didn't say goodbye.{/i}"
    a "{i}Just gone. Like she was never there.{/i}"

    a "{i}Still... something was different in her eyes tonight.{/i}"
    a "{i}Not duty. Not protocol. Something real.{/i}"
    a "{i}Maybe I'm not the only one tired of pretending.{/i}"

    # VISUAL: On the desk—sealed mission order with Echelon crest; terminal glow.
    "{i}On the desk: a sealed mission order. Echelon’s crest pressed in crimson wax.{/i}"

    if aeron_confronts_elites:
        a "{i}They’ll have heard about the whispers by morning. Let them.{/i}"

    if aeron_practiced_pledge:
        a "{i}\"Order above all.\" The line sits on my tongue like metal.{/i}"

    "{i}He turns to the glass. The Unders glow like coals far below.{/i}"
    "{i}After a beat, the seal breaks with a soft snap.{/i}"

    a "{i}(reading) 'Sector 10 breach confirmed. Possible rebel intel leaks from within Unders comm-grid.'{/i}"
    a "{i}'Sweep, secure, eliminate. Prove your worth.'{/i}"
    a "{i}Always the same. Sweep, secure, eliminate. Like I’m a task to complete, not a person{/i}"

    a "{i}Different orders, same result.{/i}"
    a "{i}They call it progress. I call it standing still.{/i}"

    # VISUAL: He looks at his bare wrist.
    a "{i}Smile for a mask I never asked to wear.{/i}"

    # Optional one-line ping to Marcus (acknowledgment only; no mood implications).
    menu:
        "A blank message cursor blinks on the terminal.":
            "Send a single-word acknowledgment to Marcus: \"Received.\"":
                $ aeron_acknowledged_marcus = True
                "{i}The message leaves without ceremony.{/i}"
            "Say nothing.":
                $ aeron_acknowledged_marcus = False
                "{i}The cursor keeps blinking until the screen sleeps.{/i}"

    # Quiet reflection near the window.
    a "{i}The Unders stay the same. The rest of us just pretend we’re different.{/i}"
    a "{i}If repetition is a cure, it hasn’t worked yet.{/i}"
    a "{i}Wearing the uniform’s easy. Remembering why isn’t.{/i}"

    a "{i}It used to feel simpler.{/i}"
    a "{i}Before I became whatever this is.{/i}"
    return