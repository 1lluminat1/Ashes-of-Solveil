# act1_04_hallway.rpy


# ===================================================
# ACT 1 - Scene 4: Hallway to the Gala
# ===================================================


define servant = Character("Attendant")

label act1_hallway:

    # VISUAL: Aeries corridor — marble and symmetry under white-gold top light.
    # Sound: distant chamber music, hushed voices. Atmosphere = sterile perfection.

    a "{i}The hallway runs like a runway—each polished tile a reminder of who I'm supposed to be.{/i}"

    # VISUAL: Officials in quiet clusters; smiles rehearsed, eyes measuring.
    # CAMERA: slow glide past faces; light cuts in planes across them.

    a "{i}Their eyes trace edges, not faces. Judging the outline, never the person.{/i}"
    # NEW: Glass makes them uncomfortable
    a "{i}They see Glass. And Glass makes them nervous.{/i}"

    # VISUAL: Floor tiles—concentric circles radiating from the center, like ripples frozen in stone.
    "{i}The floor tiles form rings within rings—the Echelon sigil stamped into the earth itself.{/i}"
    a "{i}Walk the path. Stay in your circle. Step outside, and the system corrects you.{/i}"

    # VISUAL: Vaulted ceiling stretches three stories high; light fixtures descend like judging eyes.
    "{i}The ceiling arches overhead, so high it swallows sound. Every footstep dies before it escapes.{/i}"

    # VISUAL: Echo of his steps under the vaulted ceiling.
    "{i}Footsteps carry down the length of the hall, thinned by distant strings and laughter.{/i}"

    # VISUAL: Insert — his bare wrist catches light. No Band.
    a "{i}No Band, no worth. That's the first thing they see.{/i}"
    # NEW: But not the only thing
    a "{i}Then they see the uniform. The medals. The record.{/i}"
    a "{i}And they look away faster.{/i}"

    # VISUAL: An older man in servant's attire approaches—silver hair, careful posture.
    # He carries a tray of glasses but pauses when he sees Aeron.

    servant "(quietly) Master Aeron."
    
    # VISUAL: The man's eyes flicker—recognition, then something softer. Grief, maybe.
    
    a "(stops) Do I know you?"
    servant "I served your family for sixteen years, sir. I was there the night your brother..."
    "{i}He trails off. The silence finishes the sentence.{/i}"

    # VISUAL: Aeron's jaw tightens; the man notices, lowers his gaze.
    
    # REVISED: Servant's perspective on what Aeron became
    servant "(softer) He spoke of you often. Said you'd be the one to change things."
    a "{i}Change what? The world, or just his mind about leaving it?{/i}"
    a "(carefully) He said a lot of things."
    servant "That he did, sir."
    
    # NEW: Servant sees the change
    # VISUAL: The man's eyes linger on Aeron's face—searching for something.
    servant "(quieter) I watched you become... this."
    a "Become what?"
    servant "Efficient, sir. Like your father wanted."
    # VISUAL: Pause; weight in the silence.
    servant "(barely audible) Your brother never became Glass. You... I'm not sure there was ever anything else left."

    # VISUAL: The man adjusts the tray, preparing to move on.
    
    servant "For what it's worth... I hope you find what he was looking for."
    
    # VISUAL: He bows slightly—genuine respect, not ceremony—and continues down the hall.
    "{i}His footsteps fade into the chamber music.{/i}"

    a "{i}What he was looking for? He was looking for the edge of a roof.{/i}"
    a "{i}And he found it.{/i}"

    # VISUAL: Staff reaction — butler steps aside, gaze fixed on the floor.
    a "{i}Obedient in public. Honest in silence.{/i}"
    
    # NEW: Transition to wrist choice
    # VISUAL: Another elite passes—eyes flick to Aeron's wrist, then to his face, then away quickly.
    "{i}Another glance. This one lingers on the medals, then recoils.{/i}"
    a "{i}They know the record. They know what Glass does.{/i}"
    a "{i}And they don't want to be seen looking too long.{/i}"

    # ACTION — Obedience choice (Empathy / Detachment metric seed)
    menu:
        "Aeron glances at his bare wrist. What does he do?"
        "Tug the sleeve to hide it.":
            $ aeron_hides_wrist = True
            # VISUAL: Smooths cuff; gold reflection travels along his arm.
            a "{i}Old habit. As if hiding it changes what I am.{/i}"
            a "{i}Glass with a cloth over it. Still see-through underneath.{/i}"
            
        "Leave it exposed.":
            $ aeron_hides_wrist = False
            a "{i}Let them look. Let them remember.{/i}"
            a "{i}No Band. Just results. 390 of them.{/i}"

    # VISUAL: Portraits of Aeries elites — immaculate propaganda, eyes following.
    "{i}Portraits line the walls—heroes painted to outlast their mistakes.{/i}"

    # NEW/REVISED: Marcus portrait with more depth and Glass reference
    # VISUAL: Marcus Rylan portrait; Aeron's shadow eclipses half the face.
    a "{i}Marcus Rylan. Hero, legend, father. Depends who you ask.{/i}"
    # VISUAL: Aeron stops walking; stares at the portrait for a beat.
    "{i}The portrait doesn't look back. It never does.{/i}"
    # NEW: What Marcus made
    a "{i}He trained me well. Too well, maybe.{/i}"
    a "{i}I can kill without hesitation. Lead without doubt. Obey without question.{/i}"
    a "{i}Everything he wanted. Except the belief.{/i}"
    a "{i}He made me Glass. Perfect and empty.{/i}"
    a "{i}And that makes me his greatest failure.{/i}"

    # VISUAL: Two elites whisper as he passes—light catches their mirrored glasses.
    # REVISED: Complete rewrite of elite whispers
    "{i}Voices drop as he approaches. Not mockery. Something else.{/i}"
    
    # NEW: Elite whispers that fear/respect Glass
    "{i}He catches fragments:{/i}"
    "{i}\"...Marcus Rylan's son. Glass.\"{/i}"
    "{i}\"...390 operations. Zero failures.\"{/i}"
    "{i}\"...technically perfect, but have you seen his eyes?\"{/i}"
    "{i}\"...nothing behind them...\"{/i}"
    
    a "{i}They're not wrong.{/i}"
    a "{i}Glass doesn't feel. Glass doesn't question.{/i}"
    a "{i}Glass just cuts.{/i}"
    
    "{i}The whispers fade as he passes. Relief in their silence.{/i}"

    # VISUAL: End doors glow—warm light spilling into the cold hall; guards motionless.
    "{i}At the far end, twin doors leak warm light into the cold hall.{/i}"

    # NEW/REVISED: Threshold hesitation with physicality
    # VISUAL: Aeron's hand hovers near the door frame; doesn't quite touch.
    a "{i}I could turn around. Slip into the dark.{/i}"
    a "{i}Would anyone stop me? Would anyone care?{/i}"
    # NEW: But Glass doesn't retreat
    "{i}His hand drops. The choice was already made.{/i}"
    a "{i}No. Not tonight.{/i}"
    a "{i}Glass performs when called. That's what Glass does.{/i}"

    # VISUAL: Doors open—gold light floods frame; muffled sound swells, then cuts to silence.
    "{i}Hinges sigh. Light and voices flood the marble hush.{/i}"
    "{i}Time to smile. Time to lie. Time to be Glass.{/i}"

    # canon_note: Maintain contrast—Aeries = white-gold top light (control), gala = diffused amber (illusion of warmth).
    # canon_note: Variable aeron_hides_wrist affects later empathy dialogue (Lyra Act I / Zira Act II).
    # canon_note: Servant's comment about "becoming Glass" plants seed for identity crisis
    # canon_note: Elite whispers now FEAR Glass rather than mock failure - major tonal shift
    # canon_note: "390 operations" mentioned - consistent with mission scene
    # canon_note: Marcus portrait moment shows Aeron's understanding of what he's become
    # canon_note: Insert 1-second pause before next scene to let light shift settle.

    return