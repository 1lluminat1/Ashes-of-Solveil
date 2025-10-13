# act1_17_suiting_up.rpy


# =======================================================
# ACT 1 - Scene 17: Suiting Up
# =======================================================


label act1_suiting_up:

    # VISUAL: Fade in from black; morning light through narrow windows.
    "{i}Morning. Military prep room.{/i}"
    a "{i}The Obsidian Bridge feels like a dream. Or a warning.{/i}"
    a "{i}Now comes the reckoning.{/i}"

    # VISUAL: Military prep room—lockers, weapon racks, harsh overhead lighting.
    # SOUND: Ventilation hum; distant boots on metal; weapon mechanisms clicking.
    # LIGHTING: Cold white fluorescent; shadows sharp and unforgiving.

    "{i}The prep room smells like oil and ozone. Clean violence.{/i}"

    # VISUAL: Aeron stands before an open locker; tactical gear laid out with precision.
    "{i}Everything in its place. Boots. Vest. Rifle. Like the uniform makes the soldier.{/i}"

    # VISUAL: He picks up the tactical vest—heavy, plated, black.
    "{i}He lifts the vest. Weight settles across his shoulders like expectation.{/i}"
    a "{i}Forty pounds of Kevlar and ceramic. Lighter than Father's name.{/i}"

    # VISUAL: Straps cinch tight; buckles snap into place; each sound deliberate.
    # SOUND: Velcro tear, metal click, fabric tension.
    "{i}Pull. Click. Tighten. The ritual of readiness.{/i}"

    # VISUAL: Mission orders on the bench beside him—red Echelon seal visible.
    "{i}The orders sit where he left them. Three words. Sweep. Secure. Eliminate.{/i}"
    a "{i}They make it sound clean. Mechanical. Like flipping a switch.{/i}"

    # VISUAL: He picks up his sidearm—checks the magazine, chambers a round.
    # SOUND: Magazine click; slide rack; safety engage.
    "{i}The gun sits heavy in his palm. Fifteen rounds. How many lives is that?{/i}"

    # VISUAL: Aeron stares at his reflection in the locker mirror—full tactical gear, emotionless.
    "{i}The mirror shows a soldier. Clean lines. Hard edges. Nothing human left visible.{/i}"
    a "{i}Is this who I am? Or just who they need me to be?{/i}"

    # ACTION: Player choice—hesitate or commit.
    menu:
        "The weapon holster waits at his hip."
        "Holster the weapon immediately.":
            $ aeron_hesitated_before_sweep = False
            "{i}The gun slides into place. Muscle memory. No thought required.{/i}"
            a "{i}Orders are orders. Doubt doesn't change the outcome.{/i}"

        "Pause before holstering.":
            $ aeron_hesitated_before_sweep = True
            "{i}His hand hovers. The weight suddenly unbearable.{/i}"
            a "{i}What if I just... don't go?{/i}"
            a "{i}What if I walk away and let the sector burn without me?{/i}"
            "{i}But the gun finds the holster anyway. Because walking away isn't an option. Not yet.{/i}"

    # VISUAL: Zira's datachip—visible in his coat pocket on the bench.
    "{i}The datachip sits in his coat. Small. Unassuming. Dangerous.{/i}"
    a "{i}She said it was the truth. What if the truth is in Sector Ten, not on a chip?{/i}"

    # VISUAL: He leaves the chip behind; takes only the weapon.
    "{i}He leaves it. The mission doesn't have room for doubt.{/i}"

    # VISUAL: He closes the locker; the reflection disappears.
    # SOUND: Metal slam; echo fades into silence.
    "{i}The locker shuts. The soldier remains.{/i}"

    # VISUAL: Hallway doors open—red emergency lighting spills in.
    "{i}The doors open. Sector Ten waits.{/i}"

    a "{i}Sweep. Secure. Eliminate.{/i}"
    a "{i}Just another mission.{/i}"
    a "{i}Just another lie.{/i}"

    # TRANSITION: Hard cut to Sector Ten exterior—sirens, smoke, chaos beginning.
    return