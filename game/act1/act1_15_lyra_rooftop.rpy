# act1_15_lyra_rooftop.rpy


# =======================================================
# ACT 1 - Scene 12: Rooftop Introspection
# =======================================================

label act1_rooftop:    
    # FADE IN: Rooftop – night sky above Solveil, faint hum of the city.
    "{i}The rooftop is quiet. Just wind and distant engines. The city doesn’t sleep... but tonight, he needs silence.{/i}"

    a "{i}I used to think the stars looked brighter from up here.{/i}"
    a "{i}But maybe that was just when we stood here together...{/i}"

    # He looks out. Camera pans slowly. Memory floods in.

    # VISUAL: Fade to monochrome or desaturated palette – rooftop memory.
    # SFX: distant echo filter on dialogue to signal flashback.

    "{i}A memory, uninvited, rises from the dark...{/i}"
    "{i}His brother, hands on the same railing. The same city stretching beyond them. The silence between them was always comfortable... until it wasn’t.{/i}"

    b "You ever think about just... jumping?"
    ya "(caught off guard) What?"

    b "Not seriously. Just... wonder what it’d be like. Letting go. Freefalling."
    ya "You sound like a lunatic."

    b "(smiling) Maybe. Or maybe I just see things clearly."

    # VISUAL: Colors return slowly, hum of the present swells back in.

    a "{i}I thought you were joking. Maybe I was just too afraid to ask.{/i}"
    a "{i}I just let you go, like everything else.{/i}"

    # He exhales smoke. Wind tugs at his coat. The door behind him opens gently.
    # Lyra Enters.
    # VISUAL: Door slides open softly behind him; silhouette framed by neon.
    l "(softly) You think the city ever gets tired of listening to us?"
    a "(without turning) Thought you left hours ago."

    l "(approaches slowly) I did. Came back."
    a "Why?"

    l "(shrugs) Something told me you’d be up here."

    # She walks beside him. Silence. They both stare out at the city.

    l "We used to come up here, remember?"
    a "I remember everything."

    l "Even the good parts?"
    a "(quiet) Especially the good parts."
    l "(barely audible) Then maybe they're not gone."

    # -- PLAYER CHOICE: Relationship Intimacy --

    menu:
        "Open up to Lyra (Warm)":
            $ lyra_affection += 1
            a "I almost followed him, you know."
            l "(surprised) ...Your brother?"

            a "Tonight. Earlier. I was right there on the edge."
            l "(pain in her voice) Aeron—"

            a "(cuts in) But then you knocked. Like the world decided I didn’t get to make that choice."
            l "(softly) Maybe because it wasn’t yours to make alone."
        "Stay guarded (Cold)":
            a "(lights another cigarette) Doesn’t matter now."
            l "(eyes him) I think it does."

            a "You came back to say that?"
            l "I came back to make sure you’re still breathing."

            a "That’s not your job anymore."
            l "(quietly hurt) Maybe it never was."

            "{i}She turns slightly, staring out at the city again. The silence between them stretches... but doesn’t break.{/i}"

    l "(after a long pause) You scare me sometimes, Aeron."
    a "Why? Because I think too much?"

    l "No. Because you feel too much and act like you don’t."

    "{i}They stand close. Closer than before. The past between them flickers like a fading light.{/i}"

    a "(quietly) I'm still here."
    l "For now. Just... don’t disappear again."
    
    "{i}The camera pulls back. The city fades behind them. Two souls sharing a moment that neither of them fully understands.{/i}"

    "{i}Dawn crawls up the towers, painting the glass in ghostlight. Somewhere below, the city prepares for something it can’t name.{/i}"

    return
