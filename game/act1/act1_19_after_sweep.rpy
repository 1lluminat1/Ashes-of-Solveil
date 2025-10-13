# act1_19_after_sweep.rpy


# =======================================================
# ACT 1 - Scene 19: After the Sweep
# =======================================================


label act1_after_sweep:

    # VISUAL: Interior of military transport—dark, utilitarian; single overhead light flickers.
    # SOUND: Engine hum; rain on metal roof; distant siren fading.
    # LIGHTING: Cold blue wash; shadows deep; blood shows dark against fabric.

    "{i}The transport doors seal. The engine hums. Sector Ten recedes into smoke.{/i}"

    # VISUAL: Aeron sits alone on the bench; uniform streaked with ash and blood.
    # CAMERA: Slow push-in; low angle; isolation framing.
    "{i}He sits alone. The bench is cold. The quiet is worse.{/i}"

    # VISUAL: Close-up on his hands—still gloved, stained dark at the fingertips.
    "{i}His hands rest on his knees. Still. Too still.{/i}"
    a "{i}When did they stop shaking?{/i}"

    # VISUAL: He slowly peels off one glove—hand beneath is pale, knuckles scraped.
    "{i}He pulls off the glove. Slowly. The fabric resists, damp with sweat and ash.{/i}"
    a "{i}Clean hands. Dirty work.{/i}"

    # SOUND: His breath—uneven, controlled but fragile.
    "{i}Breathe in. Hold. Breathe out. Repeat.{/i}"
    a "{i}Standard decompression protocol. Like emotions are just another system to regulate.{/i}"

    # VISUAL: Flashback insert—the boy's face, eyes wide, sister crumpled in background.
    # VISUAL: Quick cut—Tessa's hands covered in blood, her voice sharp: "Should've stayed below."
    # VISUAL: Quick cut—Enforcer lowering rifle, expression blank.
    "{i}The boy's face. Tessa's blood-slicked hands. The rifle lowering. Smoke.{/i}"
    a "{i}Stop. Just stop.{/i}"

    # VISUAL: He closes his eyes; jaw tight; tries to breathe through it.
    "{i}He closes his eyes. The images don't leave. They never do.{/i}"

    # PROP: Zira's datachip—visible in his coat pocket, faint glow at the edge.
    # VISUAL: His eyes open; land on the chip.
    "{i}The datachip glows faintly in his pocket. Barely visible. Impossible to ignore.{/i}"

    a "{i}She said it was the truth.{/i}"
    a "{i}What if the truth is worse than what I just saw?{/i}"

    # VISUAL: He pulls the chip out—holds it between thumb and forefinger, turns it slowly.
    "{i}He lifts it. Small. Innocuous. Heavy.{/i}"

    # ACTION: Player choice—examine the chip or put it away.
    menu:
        "The chip catches the flickering light."
        "Turn it over in your hands.":
            $ aeron_examined_chip = True
            "{i}He turns it slowly. No markings. No labels. Just raw data, waiting.{/i}"
            a "{i}Plug it in, and everything changes. Or nothing does. Either way, I'll know.{/i}"
            a "{i}But not here. Not yet.{/i}"
            "{i}He slips it back into his pocket.{/i}"

        "Put it away without looking.":
            $ aeron_examined_chip = False
            "{i}He closes his fist around it. Doesn't look. Can't afford to.{/i}"
            a "{i}One crisis at a time.{/i}"
            "{i}It disappears back into his coat.{/i}"

    # VISUAL: The transport slows; hydraulic hiss as it docks.
    # SOUND: Docking clamps engage; pressurization equalize; door prep sequence.
    "{i}The transport slows. The city waits outside—clean, ordered, ignorant.{/i}"

    # VISUAL: Aeron stands; adjusts his uniform; wipes his face with the back of his hand.
    "{i}He stands. Smooths the uniform. Wipes his face.{/i}"
    a "{i}Presentable. That's what matters. Not the bodies. Not the screams. Just the optics.{/i}"

    # VISUAL: Door opens—sterile white light floods in; corridor beyond pristine.
    "{i}The door opens. White light. Clean floors. No ash. No blood.{/i}"
    a "{i}Like it never happened.{/i}"

    # VISUAL: He steps into the corridor; door seals behind him; red light blinks—message waiting.
    "{i}A terminal blinks red. Message waiting.{/i}"
    "{i}He already knows who it's from.{/i}"

    # VISUAL: Aeron stops; looks at the terminal; his reflection distorted in the black screen.
    a "{i}Father wants his report.{/i}"
    a "{i}What do I even say?{/i}"

    # TRANSITION: Hard cut to apartment interior; terminal activating.
    # SOUND: Holo-call connection tone rising.
    return