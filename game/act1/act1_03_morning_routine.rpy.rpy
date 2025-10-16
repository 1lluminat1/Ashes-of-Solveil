# act1_03_morning_routine.rpy


# ===================================================
# ACT 1 - Scene 3: Morning Routine
# ===================================================


label act1_morning_routine:

    # VISUAL: Fade in from black; morning light (cold, white) filters through rain-streaked glass.
    # LIGHTING: Harsh morning light; sterile white; shadows sharp.
    "{i}Morning arrives like a schedule—punctual, indifferent.{/i}"
    
    # NEW: Reference to last night's mission
    "{i}The mission is logged. Filed. Forgotten.{/i}"
    "{i}Today, a different performance awaits.{/i}"

    # VISUAL: Bathroom mirror, harsh white light; steam from shower dissipating.
    # SOUND: Water dripping; ventilation hum; distant city drone.

    a "{i}Morning feels mechanical. Wake. Wash. Dress. Repeat.{/i}"
    
    # NEW: Transition between roles
    a "{i}Last night: soldier. Tonight: son.{/i}"
    a "{i}Same uniform. Different lies.{/i}"

    # VISUAL: Aeron stands before the mirror, half-dressed; uniform laid out on the bed behind him.
    a "{i}The mirror shows what I'm supposed to be. The uniform makes it official.{/i}"

    # VISUAL: Close-up on uniform—black fabric, silver piping, Echelon insignia on the collar.
    # On the chest: three medals, polished but untouched for months.

    "{i}The dress uniform hangs like a costume. Every crease pressed. Every medal aligned.{/i}"
    
    # NEW/REVISED: Kael callback with Glass comparison
    # VISUAL: Brief flash—memory of Kael in his uniform, standing tall, confident.
    a "{i}Kael wore his like armor. Stood taller. Smiled wider.{/i}"
    a "{i}I wear mine like Glass wears light. Transparent. Reflecting what they want to see.{/i}"
    a "{i}His didn't save him either.{/i}"

    # VISUAL: Automated wardrobe assistant activates—soft blue light scans the uniform.
    # SOUND: Soft chime; synthetic voice, pleasant and hollow.

    "Wardrobe Assistant" "Good morning, Aeron. Dress uniform prepared for Gala attendance. Estimated departure: 18:47."
    "Wardrobe Assistant" "Would you like the full ceremonial configuration?"
    
    # NEW: Setup for choice with Glass context
    a "{i}Full ceremonial. Medals and all. The whole performance.{/i}"
    a "{i}Glass doesn't need decorations. But the audience expects them.{/i}"

    # ACTION: Player choice—medals or no medals.
    menu:
        "The medals catch the light—commendations for operations he doesn't remember caring about."
        "Wear the full dress uniform with medals.":
            $ aeron_wears_medals = True
            # VISUAL: Aeron pins each medal carefully; camera lingers on his hands.
            a "{i}If I look the part, maybe they'll stop asking questions.{/i}"
            "{i}Each medal clicks into place. Weight without meaning.{/i}"
            # NEW: Mission count reference
            a "{i}Sector 9 pacification. Midlier insurgent sweep. Grid 7 containment.{/i}"
            a "{i}Names for violence. Medals for obedience.{/i}"
            a "{i}390 operations. How many of these actually mattered?{/i}"
            
        "Leave the medals off.":
            $ aeron_wears_medals = False
            # VISUAL: Aeron closes the medal case without touching them.
            a "{i}Let them wonder. I'm done pretending I earned these.{/i}"
            "{i}The uniform feels lighter. Still a lie, but a quieter one.{/i}"
            # NEW: Glass reference
            a "{i}Glass doesn't need decoration. Glass is transparent.{/i}"
            a "{i}They can see right through me either way.{/i}"

    # NEW/REVISED: Collar moment with more physical detail
    # VISUAL: He buttons the collar; fabric constricts slightly around his throat.
    "{i}The collar sits tight. Too tight.{/i}"
    # VISUAL: His finger tugs at it briefly—then stops. Adjusts instead.
    a "{i}Breathing's optional at these events anyway.{/i}"
    # NEW: Glass doesn't need air
    a "{i}Glass doesn't breathe. Glass just reflects.{/i}"

    # VISUAL: Reflection in mirror—Aeron in full uniform, posture straight, face expressionless.
    a "{i}There. General Rylan's son. Ready for inspection.{/i}"
    # REVISED: Glass identity
    a "{i}Glass, polished and presentable.{/i}"
    a "{i}See-through. Empty. Perfect.{/i}"

    # VISUAL: He turns away from the mirror; apartment door slides open with a pneumatic hiss.
    "{i}The mirror shows the uniform. Not the blood from last night.{/i}"
    "{i}Not the family. Not the metrics. Not the 99.7%.{/i}"
    "{i}Just Glass, ready to perform.{/i}"
    
    a "{i}Time to face the world.{/i}"

    # canon_note: aeron_wears_medals flag can influence elite reactions in act1_04_gala.
    # canon_note: Wardrobe Assistant voice should sound helpful but empty—no warmth, just function.
    # canon_note: References to last night's mission (operation 390) ground the timeline
    # canon_note: Glass metaphor continues - transparent, empty, reflective
    # canon_note: "Blood from last night" - subtle reminder of what happened hours ago
    # canon_note: Collar tightness = control/restriction motif throughout Act 1

    return