# act1_03_hallway.rpy


# ===================================================
# ACT 1 - Scene 3: Hallway to the Gala
# ===================================================


label act1_hallway:
    # VISUAL: Opulent corridor—polished marble, gold inlays, Echelon banners. Ambient music far off.
    a "{i}The hallway runs like a runway—each polished tile a reminder of who I’m supposed to be.{/i}"

    # Elites and officials in small clusters; glances track him, murmurs clipped.
    # CAMERA: Slow dolly; faces catch light, then fall back to shadow.
    a "{i}Their eyes scrape like razors. Accusation. Pity. Take your pick.{/i}"

    # Low angle on his steps; echo under coffered ceiling.
    "{i}Footsteps carry down the length of the hall, thinned by distant strings and laughter.{/i}"

    # Wrist insert—no Band.
    a "{i}No Band, no worth. That’s what they see first.{/i}"

    # Staff reaction.
    # A butler steps aside, nods stiffly, gaze lowered.
    a "{i}Even the staff—obedient in public, honest in private.{/i}"

    ACTION 1 — Conceal or show the bandless wrist
    menu:
        "Aeron glances at his bare wrist. What does he do?":
            "Tug the sleeve to hide it.":
                $ aeron_hides_wrist = True
                # VISUAL: He smooths the cuff; fabric catches gold highlights.
                a "{i}Let the uniform do the talking.{/i}"
            "Leave it exposed.":
                $ aeron_hides_wrist = False
                a "{i}Let them look.{/i}"

    # Portraits of past leaders.
    "{i}Portraits line the walls—Aeries elites frozen in paint, untouched by time.{/i}"

    # Marcus portrait; Aeron's shadow eclipses half the face.
    a "{i}Marcus Rylan. Hero, legend, father. Depends who you ask.{/i}"
    a "{i}I’m the proof his story doesn’t end the way he wanted.{/i}"

    # VISUAL: A pair of elites whisper as Aeron passes — sharp suits, practiced smiles.
    "{i}A pair of elites glance up as he walks by—smiles too polished, voices too quiet.{/i}"
    "{i}Their words fade to murmurs when his shadow passes over them.{/i}"
    a "{i}They don’t need to speak louder. I already know the script.{/i}"
    "{i}The whispers lift, thin as steam, and drift behind him.{/i}"

    # End-doors glow with gala light; two guards at attention.
    "{i}At the far end, twin doors breathe warm light into the cold corridor.{/i}"

    # Threshold
    a "{i}I could turn around. Slip into the dark.{/i}"
    a "{i}Would anyone stop me? Would anyone care?{/i}"
    a "{i}No. Not tonight.{/i}"

    # Doors open; golden light spills across the marble.
    "{i}Hinges sigh. Warmth and voices flood the hall.{/i}"

    # Transition out to Gala scene…
    return