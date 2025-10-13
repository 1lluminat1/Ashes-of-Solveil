# act1_03_morning_routine.rpy


# ===================================================
# ACT 1 - Scene 3: Morning Routine
# ===================================================


label act1_morning_routine:

    # VISUAL: Fade in from black; morning light (cold, white) filters through rain-streaked glass.
    "{i}Morning arrives like a schedule—punctual, indifferent.{/i}"

    # VISUAL: Bathroom mirror, harsh white light; steam from shower dissipating.
    # SOUND: Water dripping; ventilation hum; distant city drone.

    "{i}Morning feels mechanical. Wake. Wash. Dress. Repeat.{/i}"

    # VISUAL: Aeron stands before the mirror, half-dressed; uniform laid out on the bed behind him.
    a "{i}The mirror shows what I'm supposed to be. The uniform makes it official.{/i}"

    # VISUAL: Close-up on uniform—black fabric, silver piping, Echelon insignia on the collar.
    # On the chest: three medals, polished but untouched for months.

    "{i}The dress uniform hangs like a costume. Every crease pressed. Every medal aligned.{/i}"
    
    # NEW/REVISED: Kael callback with more detail
    # VISUAL: Brief flash—memory of Kael in his uniform, standing tall, confident.
    "{i}Kael wore his like armor. Stood taller. Smiled wider.{/i}"
    a "{i}I wear mine like a disguise.{/i}"
    a "{i}Funny. His didn't save him either.{/i}"

    # VISUAL: Automated wardrobe assistant activates—soft blue light scans the uniform.
    # SOUND: Soft chime; synthetic voice, pleasant and hollow.

    "Wardrobe Assistant" "Good morning, Aeron. Dress uniform prepared for Gala attendance. Estimated departure: 18:47."
    "Wardrobe Assistant" "Would you like the full ceremonial configuration?"
    
    # NEW: Setup for choice
    a "{i}Full ceremonial. Medals and all. The whole performance.{/i}"

    # ACTION: Player choice—medals or no medals.
    menu:
        "The medals catch the light—commendations for operations he doesn't remember caring about."
        "Wear the full dress uniform with medals.":
            $ aeron_wears_medals = True
            # VISUAL: Aeron pins each medal carefully; camera lingers on his hands.
            a "{i}If I look the part, maybe they'll stop asking questions.{/i}"
            "{i}Each medal clicks into place. Weight without meaning.{/i}"
        "Leave the medals off.":
            $ aeron_wears_medals = False
            # VISUAL: Aeron closes the medal case without touching them.
            a "{i}Let them wonder. I'm done pretending I earned these.{/i}"
            "{i}The uniform feels lighter. Still a lie, but a quieter one.{/i}"

    # NEW/REVISED: Collar moment with more physical detail
    # VISUAL: He buttons the collar; fabric constricts slightly around his throat.
    "{i}The collar sits tight. Too tight.{/i}"
    # VISUAL: His finger tugs at it briefly—then stops. Adjusts instead.
    a "{i}Breathing's optional at these events anyway.{/i}"

    # VISUAL: Reflection in mirror—Aeron in full uniform, posture straight, face expressionless.
    a "{i}There. General Rylan's son. Ready for inspection.{/i}"
    a "{i}Just another soldier in a city built on them.{/i}"

    # VISUAL: He turns away from the mirror; apartment door slides open with a pneumatic hiss.
    "{i}The mirror shows the uniform. Not the person inside it.{/i}"
    a "{i}Time to face the world.{/i}"

    # canon_note: aeron_wears_medals flag can influence elite reactions in act1_04_gala.
    # canon_note: Wardrobe Assistant voice should sound helpful but empty—no warmth, just function.

    return