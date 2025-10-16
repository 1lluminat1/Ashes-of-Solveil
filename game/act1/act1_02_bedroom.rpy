# act1_02_bedroom.rpy


# ===================================================
# ACT 1 - Scene 2: Aeron's Bedroom
# ===================================================


label act1_bedroom:

    # VISUAL: Aeron's quarters, dim and sterile. Cold blue light filters through rain-streaked glass.
    # Mood: isolation; mechanical hum faint beneath rain.
    # LIGHTING: Cold blue wash from window; neon reflections from city below.

    a "{i}Rain taps the glass. Keeps time with the hum in the walls.{/i}"
    
    # NEW: Physical sensation
    "{i}The room is cold. He doesn't turn on the heat.{/i}"
    a "{i}Cold keeps you sharp. Warm makes you forget.{/i}"
    
    # REVISED: Not about belonging, but about identity
    a "{i}The city's still out there. I'm just another piece of it now.{/i}"
    a "{i}A tool. A function. Glass.{/i}"

    # VISUAL: Reflection fractured by droplets—his face split across the pane.
    # Symbol: Glass = truth / self-awareness.
    # VISUAL: His own reflection, distorted by rain, looks back at him.

    "{i}His reflection fractures across the rain-streaked window.{/i}"
    a "{i}Glass looking at Glass.{/i}"
    a "{i}Transparent. Empty. Nothing to see.{/i}"

    # VISUAL: On wall—an empty display case once meant for his Band.
    # Plaque reads quietly beneath dust: "For the Chosen."

    a "{i}An empty frame weighs more than the Band ever would.{/i}"
    
    # NEW: Reframe this - not about failure, but about what replaced it
    a "{i}The Band was supposed to give me purpose.{/i}"
    a "{i}Instead, I got orders. 389 of them.{/i}"
    a "{i}Father calls me Glass. Transparent. Sharp. Useful.{/i}"
    a "{i}Perfect metrics. Perfect form. Perfectly empty.{/i}"

    # VISUAL: Nightstand photo — Aeron and his brother, both smiling. 
    # The brother's wristband half-hidden by light glare.
    # VISUAL: Kael at age 15, Band still working. Aeron at age 10, two years before his Branding.

    a "{i}He always smiled like he belonged.{/i}"
    a "{i}Even after his Band failed. Even when the whispers started.{/i}"
    a "{i}He tried to keep smiling. For three years he tried.{/i}"
    
    # NEW: Brother photo interaction
    # VISUAL: Aeron's finger traces the edge of the frame; doesn't touch the glass.
    "{i}He reaches for the photo. Stops. Pulls back.{/i}"
    a "{i}Looking doesn't change anything. Neither does not looking.{/i}"
    a "{i}But I can't put it away.{/i}"
    
    # REVISED: Brother comparison - what they each became
    a "{i}Kael couldn't live with being broken.{/i}"
    a "{i}I became perfect at it.{/i}"
    a "{i}Father made me Glass. And Glass doesn't break.{/i}"
    a "{i}...Does it?{/i}"

    # VISUAL: Wardrobe door opens; black Echelon uniform inside, perfectly pressed, untouched.
    # Symbol: order / identity / the role he plays.

    # REVISED: Not about forgetting failure, but about the performance
    a "{i}Right clothes. Right words. Right performance.{/i}"
    a "{i}Tomorrow's the gala. Father's exhibition.{/i}"
    a "{i}'Look at what I made from failure,' he'll say.{/i}"
    a "{i}'Glass that cuts on command.'{/i}"

    # OPTIONAL ACTION — Obedience test (Empathy metric seed)
    menu:
        "Does Aeron rehearse the lines Echelon expects to hear?"
        "Practice the pledge under his breath.":
            $ aeron_practiced_pledge = True
            a "\"{i}Order above all. Unity before self.{/i}\""
            a "{i}The words come automatic. Like breathing.{/i}"
            # NEW: The real issue isn't the words
            a "{i}I can recite doctrine. I can execute missions. I can kill without hesitation.{/i}"
            a "{i}What I can't do is believe any of it.{/i}"
            a "{i}And Father knows. He's always known.{/i}"
        "Stay silent.":
            $ aeron_practiced_pledge = False
            a "{i}The words don't matter. I'll say them when required.{/i}"
            a "{i}Glass doesn't need to practice. Glass just performs.{/i}"

    # NEW: Mission order notification
    # VISUAL: Terminal on desk blinks; red notification light pulsing.
    # SOUND: Soft chime; message alert breaking the silence.
    "{i}The terminal chimes. Mission orders.{/i}"
    
    # VISUAL: Aeron's eyes move to the screen; red glow on his face.
    a "{i}Sector Seven. Containment sweep. Pre-dawn deployment.{/i}"
    a "{i}Tonight. Before the gala. Before I smile for the cameras.{/i}"
    
    # REVISED: This is routine, not new
    a "{i}Operation 390.{/i}"
    a "{i}Just another number. Just another night.{/i}"
    a "{i}Glass doesn't question. Glass just cuts.{/i}"

    # VISUAL: Aeron stands; silhouette against window; rain continues.
    "{i}He stands. The city hums below. The mission waits.{/i}"

    # VISUAL: Hold on his silhouette; breath visible in cold air.
    # canon_note: Keep this pause ~2–3 sec for atmosphere; rain ambience only.
    
    # TRANSITION: Not about uncertainty, but about routine
    "{i}First the blade. Then the smile.{/i}"
    "{i}First Glass. Then the performance.{/i}"
    "{i}Same as always.{/i}"
    
    # canon_note: This scene establishes Glass identity before we see it in action
    # canon_note: 389 operations mentioned - mission scene will be 390
    # canon_note: Kael failed at 15, tried to survive 3 years, jumped at 17
    # canon_note: Aeron sees himself as "made from failure" - Glass as replacement for purpose
    # canon_note: Routine mission, not special - this is what he always does
    # canon_note: "Glass doesn't break" - question mark is first tiny seed of doubt

    # Jump to mission scene
    return