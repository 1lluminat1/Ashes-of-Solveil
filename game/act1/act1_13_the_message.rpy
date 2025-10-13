# act1_13_the_message.rpy


# ======================================================
# ACT 1 - Scene 13: The Message
# ======================================================


label act1_the_message:

    # VISUAL: Aeron's apartment after Lyra leaves; door closed, room dim.
    # LIGHTING: Blue-grey ambient; terminal glow from desk.
    # SOUND: Ventilation hum; distant city drone; rain starting outside.

    "{i}The door seals behind her. The room exhales.{/i}"
    a "{i}She came back. Twice now.{/i}"
    a "{i}Maybe I'm not as invisible as I thought.{/i}"

    # VISUAL: He moves to the desk; mission envelope still there, half-forgotten.
    "{i}The mission waits. It always waits.{/i}"

    # VISUAL: Terminal screen flickers—notification pulse in the corner.
    # SOUND: Soft chime; message alert.
    "{i}The terminal chimes. New message. Unmarked sender.{/i}"

    # VISUAL: Aeron hesitates; hand hovers over the interface.
    a "{i}Unmarked means encrypted. Encrypted means trouble.{/i}"

    # ACTION: Player choice—open it or ignore it.
    menu:
        "The notification blinks. Insistent."
        "Open the message.":
            $ aeron_opened_message = True
            "{i}He taps the screen. The message decrypts.{/i}"
        "Ignore it.":
            $ aeron_opened_message = False
            "{i}He turns away. But the chime repeats. Again. Again.{/i}"
            a "{i}Persistent bastard.{/i}"
            "{i}He sighs and opens it anyway.{/i}"
            $ aeron_opened_message = True  # Opens either way, but hesitation noted

    # VISUAL: Text renders on screen—plain, no signature, deliberate spacing.
    # SOUND: Faint static crackle as text appears.

    "{cps=30}SECTOR 10. LOWER SPANS.{/cps}"
    "{cps=30}NORTHEAST EDGE. GRID SIX-TWO.{/cps}"
    "{cps=30}TONIGHT. COME ALONE.{/cps}"
    "{cps=30}THEY'RE WATCHING YOU.{/cps}"
    "{cps=30}I CAN SHOW YOU WHY.{/cps}"
    "{cps=30}THE TRUTH IS IN THE SHADOWS.{/cps}"

    # VISUAL: Message deletes itself—lines dissolve from bottom to top.
    # SOUND: Digital distortion; screen flickers, then clears.
    "{i}The text dissolves. Gone before he can screenshot it.{/i}"

    a "{i}Self-deleting. Professional.{/i}"
    a "{i}Or paranoid.{/i}"

    # NEW/REVISED: More physical reaction
    # VISUAL: He leans back; considers the empty screen.
    # VISUAL: His hand hovers over the terminal, then pulls back.
    "{i}No trace. No evidence. No proof it ever existed except memory.{/i}"
    a "Who the hell are you?"

    # VISUAL: Rain intensifies outside; droplets streak the window in the background.
    "{i}Rain taps the glass. The city hums below.{/i}"

    # NEW/REVISED: Sharper Sector 10 connection
    # VISUAL: He glances at the mission envelope—Sector 10 sweep orders.
    "{i}His eyes move to the mission envelope. Sector 10. Same coordinates.{/i}"
    a "{i}Father wants me to sweep Sector 10 tomorrow.{/i}"
    a "{i}Someone wants me there tonight.{/i}"
    a "{i}Coincidence? No such thing.{/i}"

    # ACTION: Player choice—investigate or stay.
    menu:
        "The coordinates burn in his memory."
        "Go to the Lower Spans now.":
            $ aeron_goes_early = True
            a "{i}If someone's watching me, I'd rather meet them on my terms.{/i}"
            "{i}He grabs his coat. The mission envelope stays behind.{/i}"
        "Wait and think it through.":
            $ aeron_goes_early = False
            a "{i}Rushing into traps is how people disappear.{/i}"
            "{i}He sits. Thinks. The rain fills the silence.{/i}"
            # NEW: Kael photo deliberation
            # VISUAL: He looks at Kael's photo on the desk.
            a "{i}What would you do, Kael? Walk into the dark or wait for dawn?{/i}"
            a "{i}But staying here won't answer anything.{/i}"
            "{i}He grabs his coat.{/i}"

    # VISUAL: Door opens; corridor light spills in; Aeron's silhouette in the frame.
    "{i}The hallway is empty. Cameras blink red in the corners.{/i}"
    a "{i}They're always watching. Question is—who else is?{/i}"

    # VISUAL: He steps into the corridor; door seals behind him.
    # SOUND: Pneumatic hiss; lock engaging; footsteps on marble.

    "{i}The elevator descends into the dark.{/i}"

    # TRANSITION: Fade to Lower Spans (act1_14_lower_spans begins).
    return