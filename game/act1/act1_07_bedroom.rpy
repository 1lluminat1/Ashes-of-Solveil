# act1_07_bedroom.rpy


# ===================================================
# ACT 1 - Scene 7: Aeron's Bedroom After the Gala
# ===================================================

label act1_bedroom_after_gala:

    # VISUAL: Aeron's quarters in shadow; city light stutters across the tall window.
    "{i}Later that night...{/i}"

    a "{i}She didn't say goodbye.{/i}"
    a "{i}Just gone. Like she was never there.{/i}"
    
    # NEW: Callback to balcony choices
    if aeron_shares_light and aeron_holds_her_gaze:
        a "{i}But I can still feel the space between us. Close enough to matter.{/i}"
    elif aeron_shares_light:
        a "{i}The flame. Her eyes. For a moment, we were just... us.{/i}"
    
    a "{i}Still... something was different in her eyes tonight.{/i}"
    a "{i}Not duty. Not protocol. Something real.{/i}"
    a "{i}Maybe I'm not the only one tired of pretending.{/i}"

    # VISUAL: On the desk—sealed mission order with Echelon crest; faint terminal glow.
    "{i}A sealed mission order waits on the desk. The Echelon crest bleeds crimson in the light.{/i}"

    if aeron_confronts_elites:
        a "{i}They will have heard about the whispers by morning. Let them.{/i}"

    if aeron_practiced_pledge:
        a "{i}\"Order above all.\" The line sits on my tongue like metal.{/i}"

    # --- PLAYER CHOICE: Hesitate before opening the order ---
    menu:
        "The seal catches the light—Marcus's insignia pressed into wax."
        "Break it immediately.":
            $ aeron_hesitated_order = False
            "{i}The seal snaps. Orders are always easier than silence.{/i}"
        "Hesitate for a breath.":
            $ aeron_hesitated_order = True
            "{i}I hold it between my fingers, as if delay could change the words inside.{/i}"
            "{i}Then the seal breaks with a soft crack.{/i}"
    # --------------------------------------------------------

    # NEW: More visceral order reading
    # VISUAL: He unfolds the document; crisp paper, perfect typography.
    "{i}The words are clean. Precise. Impersonal.{/i}"
    a "{i}(reading) 'Sector 10 breach confirmed. Possible rebel intel leaks within Unders comm-grid.'{/i}"
    a "{i}'Sweep. Secure. Eliminate. Prove your worth.'{/i}"
    # VISUAL: His finger stops on the last line.
    "{i}Prove your worth. Always the same.{/i}"

    a "{i}Sweep. Secure. Eliminate. Like I'm a task to complete, not a person.{/i}"
    a "{i}Different orders, same result.{/i}"
    a "{i}They call it progress. I call it standing still.{/i}"

    # VISUAL: He glances at his bare wrist; city reflection crosses his face.
    # FIXED: Clearer phrasing
    a "{i}Still wearing the mask. Even alone.{/i}"

    # --- PLAYER CHOICE: Acknowledge Marcus or not ---
    menu:
        "A blank message cursor blinks on the terminal."
        "Send a single-word acknowledgment: \"Received.\"":
            $ aeron_acknowledged_marcus = True
            "{i}The message leaves without ceremony.{/i}"
        "Say nothing.":
            $ aeron_acknowledged_marcus = False
            "{i}The cursor keeps blinking until the screen sleeps.{/i}"
    # ------------------------------------------------

    # VISUAL: Window reflection—Unders glowing like embers far below.
    a "{i}The Unders stay the same. The rest of us just pretend we are different.{/i}"
    a "{i}If repetition is a cure, it has not worked yet.{/i}"
    a "{i}Wearing the uniform is easy. Remembering why is not.{/i}"
    a "{i}It used to feel simpler.{/i}"
    a "{i}Before I became whatever this is.{/i}"

    # NEW: Physical closing beat
    # VISUAL: He sets the orders down; doesn't look at them again.
    "{i}The mission waits. It always does.{/i}"
    "{i}But tonight, the past won't stay buried.{/i}"
    "{i}He closes his eyes. And remembers.{/i}"
    # VISUAL: Fade to black; city hum fades with it.

    # canon_note: The hesitation flag (aeron_hesitated_order) can color later dialogue—
    # e.g., Zira teasing him for "pausing before obedience."
    # canon_note: Lighting should shift from gala gold → cold blue; Marcus's insignia glow = dominance motif.

    return