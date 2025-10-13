# act1_02_bedroom.rpy


# ===================================================
# ACT 1 - Scene 2: Aeron's Bedroom
# ===================================================


label act1_bedroom:

    # VISUAL: Aeron's quarters, dim and sterile. Cold blue light filters through rain-streaked glass.
    # Mood: isolation; mechanical hum faint beneath rain.

    a "{i}Rain taps the glass. Keeps time with the hum in the walls.{/i}"
    
    # NEW: Physical sensation
    "{i}The room is cold. He doesn't turn on the heat.{/i}"
    a "{i}Cold keeps you sharp. Warm makes you forget.{/i}"
    
    a "{i}The city's still out there... just not sure I'm part of it.{/i}"

    # VISUAL: Reflection fractured by droplets—his face split across the pane.
    # Symbol: Glass = truth / self-awareness.

    a "{i}They say a Band makes you someone.{/i}"
    a "{i}So what does that make me?{/i}"

    # VISUAL: On wall—an empty display case once meant for his Band.
    # Plaque reads quietly beneath dust: "For the Chosen."

    a "{i}An empty frame weighs more than the Band ever could.{/i}"

    # VISUAL: Nightstand photo — Aeron and his brother, both smiling. 
    # The brother's wristband half-hidden by light glare.

    a "{i}He always smiled like he belonged.{/i}"
    a "{i}Smiles fade when the lights cut out.{/i}"
    
    # NEW: Brother photo interaction
    # VISUAL: Aeron's finger traces the edge of the frame; doesn't touch the glass.
    "{i}He reaches for the photo. Stops. Pulls back.{/i}"
    a "{i}Looking doesn't change anything. Neither does not looking.{/i}"
    a "{i}But I can't put it away.{/i}"

    # VISUAL: Wardrobe door opens; black Echelon uniform inside, perfectly pressed, untouched.
    # Symbol: order unused / identity suspended.

    a "{i}Right clothes. Right words. Maybe they'll forget I failed.{/i}"
    
    # NEW: Context for pledge choice
    a "{i}The gala's tomorrow. Father will be watching.{/i}"
    a "{i}Everyone will be watching.{/i}"

    # OPTIONAL ACTION — Obedience test (Empathy metric seed)
    menu:
        "Does Aeron rehearse the lines Echelon expects to hear?"
        "Practice the pledge under his breath.":
            $ aeron_practiced_pledge = True
            a "\"{i}Order above all. Unity before self.{/i}\""
            a "{i}The words go in clean. They never come out that way.{/i}"
        "Stay silent.":
            $ aeron_practiced_pledge = False
            a "{i}Silence says enough.{/i}"

    # VISUAL: Aeron sits back on the bed; neon reflections crawl over his silhouette.
    a "{i}Tomorrow, I do what's required.{/i}"
    a "{i}After that... we'll see.{/i}"

    # VISUAL: Hold on his back; faint exhale over rain—Breath motif (life vs control).
    # canon_note: Keep this pause ~2–3 sec for atmosphere; no dialogue SFX.
    
    # TRANSITION: Fade to black; hold 1 second.
    "{i}The night passes. Sleep, when it comes, brings no rest.{/i}"

    return