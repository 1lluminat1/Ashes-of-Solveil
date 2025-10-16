# act1_07_bedroom.rpy


# ===================================================
# ACT 1 - Scene 7: Aeron's Bedroom After the Gala
# ===================================================

label act1_bedroom_after_gala:

    # VISUAL: Aeron's quarters in shadow; city light stutters across the tall window.
    "{i}Later that night...{/i}"

    a "{i}She didn't say goodbye.{/i}"
    a "{i}Just gone. Like she was never there.{/i}"
    
    # NEW: Callback to balcony choices with Glass metaphor
    if aeron_shares_light and aeron_holds_her_gaze:
        a "{i}But I can still feel the space between us. Close enough to matter.{/i}"
        a "{i}Glass leaning toward glass. Almost touching. Almost shattering.{/i}"
    elif aeron_shares_light:
        a "{i}The flame. Her eyes. For a moment, we were just... us.{/i}"
        a "{i}Not Glass. Not performance. Just two people remembering what that felt like.{/i}"
    
    a "{i}Still... something was different in her eyes tonight.{/i}"
    a "{i}Not duty. Not protocol. Something real.{/i}"
    # NEW: Recognition
    a "{i}She sees Glass. And she sees what's underneath.{/i}"
    a "{i}Maybe I'm not the only one tired of pretending.{/i}"

    # VISUAL: On the desk—sealed mission order with Echelon crest; faint terminal glow.
    "{i}A sealed mission order waits on the desk. The Echelon crest bleeds crimson in the light.{/i}"

    if aeron_confronts_elites:
        a "{i}They will have heard about the whispers by morning. Let them.{/i}"
        a "{i}Glass makes them nervous. Good.{/i}"

    if aeron_practiced_pledge:
        a "{i}\"Order above all.\" The line sits on my tongue like metal.{/i}"
        a "{i}390 operations reciting those words. Still don't believe them.{/i}"

    # --- PLAYER CHOICE: Hesitate before opening the order ---
    menu:
        "The seal catches the light—Marcus's insignia pressed into wax."
        "Break it immediately.":
            $ aeron_hesitated_order = False
            "{i}The seal snaps. Orders are always easier than silence.{/i}"
            a "{i}Glass doesn't hesitate. Glass obeys.{/i}"
            
        "Hesitate for a breath.":
            $ aeron_hesitated_order = True
            "{i}I hold it between my fingers, as if delay could change the words inside.{/i}"
            "{i}Then the seal breaks with a soft crack.{/i}"
            a "{i}Glass hesitating. That's new.{/i}"
            a "{i}Or maybe the cracks are spreading faster than I thought.{/i}"
    # --------------------------------------------------------

    # NEW: More visceral order reading with mission count
    # VISUAL: He unfolds the document; crisp paper, perfect typography.
    "{i}The words are clean. Precise. Impersonal.{/i}"
    a "{i}(reading) 'Sector 10 breach confirmed. Possible rebel intel leaks within Unders comm-grid.'{/i}"
    a "{i}'Sweep. Secure. Eliminate. Prove your worth.'{/i}"
    # VISUAL: His finger stops on the last line.
    "{i}Prove your worth. Always the same.{/i}"

    # NEW: Mission count and pattern recognition
    a "{i}Sweep. Secure. Eliminate. Like I'm a task to complete, not a person.{/i}"
    a "{i}Sector 10 makes 391.{/i}"
    a "{i}Different orders, same result. Same words. Same emptiness.{/i}"
    a "{i}They call it progress. I call it standing still.{/i}"

    # VISUAL: He glances at his bare wrist; city reflection crosses his face.
    # NEW: Glass reflection on what changed
    a "{i}Still wearing the mask. Even alone.{/i}"
    a "{i}But tonight... tonight the mask slipped.{/i}"
    a "{i}Lyra saw through Glass. And I let her.{/i}"
    a "{i}That's not what Glass does. Glass doesn't let anyone see.{/i}"

    # --- PLAYER CHOICE: Acknowledge Marcus or not ---
    menu:
        "A blank message cursor blinks on the terminal."
        "Send a single-word acknowledgment: \"Received.\"":
            $ aeron_acknowledged_marcus = True
            "{i}The message leaves without ceremony.{/i}"
            a "{i}Glass confirms. Glass complies. Glass continues.{/i}"
            a "{i}391 operations. The count continues.{/i}"
            
        "Say nothing.":
            $ aeron_acknowledged_marcus = False
            "{i}The cursor keeps blinking until the screen sleeps.{/i}"
            a "{i}Glass doesn't respond. First time in 390 operations.{/i}"
            a "{i}The silence feels like rebellion. Or just exhaustion.{/i}"
    # ------------------------------------------------

    # VISUAL: Window reflection—Unders glowing like embers far below.
    a "{i}The Unders stay the same. The rest of us just pretend we are different.{/i}"
    # NEW: What changed tonight
    a "{i}But tonight felt different. Lyra made it different.{/i}"
    a "{i}'Glass recognizes glass,' she said.{/i}"
    a "{i}Two polished surfaces. Both cracking. Both wondering if breaking means freedom or falling.{/i}"
    
    a "{i}If repetition is a cure, it hasn't worked yet.{/i}"
    a "{i}Wearing the uniform is easy. Remembering why is not.{/i}"
    a "{i}It used to feel simpler.{/i}"
    # NEW: Before and after
    a "{i}Before I became Glass. Before 390 operations made me see-through.{/i}"
    a "{i}Before I forgot what it felt like to be whole.{/i}"

    # NEW: Physical closing beat with balcony callback
    # VISUAL: He sets the orders down; doesn't look at them again.
    "{i}The mission waits. It always does.{/i}"
    "{i}But tonight, the past won't stay buried.{/i}"
    # NEW: Lyra's impact
    "{i}She asked if I remembered what wholeness felt like.{/i}"
    "{i}I don't. But for a moment on that balcony, I almost did.{/i}"
    "{i}Two pieces of glass, leaning close. Almost touching. Almost shattering.{/i}"
    
    # VISUAL: He closes his eyes. And remembers.
    a "{i}He closes his eyes. And remembers.{/i}"
    # VISUAL: Fade to black; city hum fades with it.

    # canon_note: The hesitation flag (aeron_hesitated_order) can color later dialogue—
    # e.g., Zira teasing him for "pausing before obedience."
    # canon_note: Lighting should shift from gala gold → cold blue; Marcus's insignia glow = dominance motif.
    # canon_note: First time Aeron doesn't automatically acknowledge orders (if player chooses)
    # canon_note: Lyra's impact is tangible - he's thinking about wholeness, about being more than Glass
    # canon_note: "391 operations" - consistent mission count tracking
    # canon_note: "Glass hesitating" - first concrete sign of breakdown beginning
    # canon_note: Balcony memory is what he holds onto - human connection breaking through emptiness

    return