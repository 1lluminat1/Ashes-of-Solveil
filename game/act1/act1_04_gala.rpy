# act1_04_gala.rpy


# ===================================================
# ACT 1 - Scene 4: The Gala
# ===================================================


label act1_gala:
    define e1 = Character("Elite 1", color="#000000")
    define e2 = Character("Elite 2", color="#000000")
    define e3 = Character("Elite 3", color="#000000")
    define ye1 = Character("Young Elite 1", color="#000000")
    define ye2 = Character("Young Elite 2", color="#000000")
    define ye3 = Character("Young Elite 3", color="#000000")

    # VISUAL: Lavish gold light on marble; strings under a low conversational hum.
    "{i}The ballroom breathes artificial warmth—chandeliers, velvet, and the sweet smell of programmed luxury.{/i}"
    a "{i}All this gold and glass, just to hide the rot underneath.{/i}"

    # A server steps in with a tray.
    # ACTION 1 — Accept or refuse the drink (optics hook)
    menu:
        "The server offers a glass of wine.":
            "Take the glass.":
                $ aeron_has_glass = True
                # SFX: light clink
                a "{i}If I’m a prop tonight, I may as well hold one.{/i}"
            "Refuse with a nod.":
                $ aeron_has_glass = False
                a "{i}No thanks.{/i}"

    # Overhead drone projects live feeds; Aeron’s face flickers on a giant display.
    a "{i}Even here, no escape from surveillance.{/i}"

    # Nearby elites whisper.
    e1 "...That's General Rylan's boy. Unbranded—what a waste."
    e2 "Should've been sent to the Unders like the rest."
    e3 "Another disgrace to the Rylan name."

    # ACTION 3 — Confront or pass by
    menu:
        "Aeron hears the whispers.":
            "Confront them.":
                $ aeron_confronts_elites = True
                a "Funny—I didn’t realize ghosts talked this loud. Problem?"
                with hpunch
                e2 "Of course not, Aeron! Merely... surprised to see you here."
                a "{i}Sick on borrowed power. The Band does all their talking.{/i}"
                a "Surprised to see me breathing, you mean?"
                with hpunch
                e1 "Not at all! You're Marcus Rylan's son—your presence honors Echelon."
                a "Save it."
            "Ignore and move on.":
                $ aeron_confronts_elites = False
    "{i}He walks past. Their voices crisp, brittle—and safely behind him.{/i}"

    # Marcus enters.
    "General Marcus Rylan steps into the light—ceremonial armor gleaming, Enforcers in tow."
    a "{i}The gravity tilts when he arrives. No applause—just fear, dressed as respect.{/i}"
    a "{i}He doesn’t look at me.{/i}"
    a "{i}He doesn’t have to. His shadow knows my name.{/i}"

    # Lyra across the room.
    "Across the hall, Lyra stands with a Councilwoman—composed, precise, unmissable."
    a "{i}They parade her like proof the system still works.{/i}"
    "Her eyes flick to Aeron for a heartbeat—then back."

    a "{i}But I know better. There’s metal under the polish.{/i}"

    # Younger elites nearby.
    ye1 "I heard he wasn't even compatible."
    ye2 "Defect. Or curse. Maybe both."
    ye3 "Sad, really—pretending he belongs."
    ye2 "Marcus still spins it as 'fate.'"
    ye3 "Sure. Fate’s a convenient word for failure."

    a "{i}Used to flinch. Now it’s just another broken chorus.{/i}"

    # If he’s holding the glass, use it; otherwise, a clenched fist beat.
    if aeron_has_glass:
        "{i}The stem creaks in his hand. A hairline crack crawls along the glass.{/i}"
    else:
        "{i}His fist tightens at his side; knuckles pale against the black fabric.{/i}"

    a "{i}They laugh like the world belongs to them.{/i}"
    a "{i}And I’m expected to smile like I believe it.{/i}"

    # ACTION 4 — Approach Lyra now or keep distance (sets a lightweight flag for later)
    menu:
        "Across the room, Lyra is momentarily alone.":
            "Cross the floor toward Lyra.":
                $ aeron_moves_toward_lyra = True
                "{i}He threads through silk and medals, closing the distance.{/i}"
                $ aeron_spoke_to_lyra_gala = False  # flips true once dialogue happens

                # VISUAL: A Councilwoman lingers nearby, then steps aside.
                a "Lyra."
                "{i}She pivots, posture precise, eyes reading him in a single beat.{/i}"

                l "You're on time."
                if aeron_practiced_pledge:
                    a "I remember the lines. Doesn't mean I'll say them."
                else:
                    a "On time isn't the same as willing."

                l "Noted."
                $ aeron_spoke_to_lyra_gala = True

                "{i}A Council attaché leans in with a whisper. Lyra's attention splits—only for a moment.{/i}"
                l "The balcony, in five."
                a "I'll be there."
                "{i}She’s gone before the room notices she moved.{/i}"

            "Keep your distance.":
                $ aeron_moves_toward_lyra = False
                "{i}He holds position. The moment passes.{/i}"
                $ aeron_spoke_to_lyra_gala = False

    # Tiny nod to the pledge practice if present (purely cosmetic, no mood override).
    if aeron_practiced_pledge:
        "{i}A toast rises nearby—\"Order above all.\" The words come easy; he lets them die behind his teeth.{/i}"

    # Exit vector to balcony (keeps your planned flow).
    "{i}He sets the glass down and angles toward the balcony doors.{/i}"
    return