# act1_05_gala.rpy


# ===================================================
# ACT 1 - Scene 5: The Gala
# ===================================================


# --- Character definitions (place outside any label) ---
define e1 = Character("Elite 1")
define e2 = Character("Elite 2")
define e3 = Character("Elite 3")
define ye1 = Character("Young Elite 1")
define ye2 = Character("Young Elite 2")
define ye3 = Character("Young Elite 3")
define cadet = Character("Daren")
# --------------------------------------------------------

label act1_gala:
    # VISUAL: Lavish gold wash over marble; chandeliers; strings under low conversation.
    "{i}The ballroom breathes manufactured warmth—chandeliers, velvet, the sweet smell of curated luxury.{/i}"
    a "{i}All this gold and glass to smooth over the cracks.{/i}"

    # --- PLAYER CHOICE: A server offers a drink ---
    menu:
        "The server offers a glass of wine."
        "Take the glass.":
            $ aeron_has_glass = True
            # VISUAL/SFX: light clink
            a "{i}If I am a prop tonight, I may as well hold one.{/i}"
        "Refuse with a nod.":
            $ aeron_has_glass = False
            a "{i}No thanks.{/i}"
    # ----------------------------------------------

    # VISUAL: The ballroom swells—music crescendos, voices layer, chandeliers pulse with reflected motion.
    "{i}The air thickens. Perfume, wine, polished metal. Too much of everything.{/i}"
    a "{i}Every surface reflects. Every sound echoes. No silence. No stillness. Just performance layered on performance.{/i}"

    # VISUAL: Aeron's vision briefly narrows—tunnel vision effect; edges blur, center sharpens.
    "{i}For a moment, the room contracts. Too bright. Too loud. Too many eyes.{/i}"
    a "{i}Breathe. Just breathe.{/i}"

    # VISUAL: Aeron's hand steadies against a nearby column; brief pause.
    "{i}His pulse hammers. The room tilts, then steadies.{/i}"
    a "{i}Not here. Not now. Hold it together.{/i}"

    # VISUAL: A young man in full ceremonial dress approaches—confident stride, silver Band glinting on his wrist.
    # He's Aeron's age, polished, smiling with practiced ease.

    cadet "Aeron Rylan. Thought that was you."

    # VISUAL: Aeron steadies himself; the tunnel vision clears.
    a "(turns) Daren."

    # VISUAL: Daren extends his hand—firm handshake; his Band catches the chandelier light.
    cadet "Been a while. Not since the Academy, right?"
    a "Something like that."

    cadet "(glances at Aeron's bare wrist, then quickly away) Heard you've been on special assignment. Classified work, yeah?"
    a "(neutral) Something like that."

    # VISUAL: Daren shifts his weight—uncomfortable but trying to fill the silence.
    cadet "Look, I just wanted to say... what happened at your Branding—"
    a "(cuts in) Was years ago."
    cadet "Right. Yeah. Of course."

    # VISUAL: Awkward pause; Daren taps his Band unconsciously—nervous habit.
    "{i}He touches his Band like a talisman. Proof he belongs. Proof he's safe.{/i}"

    cadet "Well, you're here tonight. That's something. Not everyone gets a second chance after..."
    "{i}He stops himself. Too late.{/i}"

    a "{i}After what? After failure? After disgrace? After my father rewrote the story so I wouldn't disappear?{/i}"

    # --- PLAYER CHOICE: How does Aeron respond to Daren ---
    menu:
        "Daren's smile wavers."
        "Respond with cold courtesy.":
            $ aeron_dismisses_daren = True
            a "Enjoy the gala, Daren."
            # VISUAL: Aeron turns away; Daren's smile collapses into relief.
            cadet "Yeah. You too."
            "{i}He retreats into the crowd, grateful for the exit.{/i}"
            a "{i}He'll tell that story tomorrow. 'Rylan's gone cold. Poor bastard.' Let him.{/i}"
            
        "Acknowledge the awkwardness.":
            $ aeron_dismisses_daren = False
            a "You don't have to do this."
            cadet "(confused) Do what?"
            a "Pretend we're still who we were. We're not."
            cadet "(pause) ...No. I guess we're not."
            "{i}For a moment, something honest passes between them. Then it's gone.{/i}"
            cadet "(quieter) Take care of yourself, Aeron."
            a "You too."
            "{i}He walks away. Not relieved. Just... sad.{/i}"
# ------------------------------------------------------

    # VISUAL: Overhead drone—live feeds rotate; Aeron’s face flickers on a screen.
    a "{i}Even here, there is no room without a camera.{/i}"

    # Nearby elites whisper (kept as audible whispers).
    e1 "...Marcus Rylan's son. Unbranded. What a tragic irony."
    e2 "Tragic? More like predictable. Weakness breeds weakness."
    e3 "(quietly) And yet Father spins it as divine providence."

    # --- PLAYER CHOICE: Confront or pass by ---
    menu:
        "Aeron hears the whispers."
        "Confront them.":
            $ aeron_confronts_elites = True
            # VISUAL: slight camera jolt/push-in here if desired.
            a "For whispers, you carry a long way. Is there a problem?"
            e2 "Of course not, Aeron! Merely... surprised to see you here."
            a "{i}Borrowed power. The Band does their speaking.{/i}"
            a "Surprised to see me breathing, you mean."
            e1 "Not at all! You are Marcus Rylan's son—your presence honors Echelon."
            a "Save it."
        "Ignore and move on.":
            $ aeron_confronts_elites = False
    # ------------------------------------------

    "{i}He walks past. Their voices go brittle, safely behind him.{/i}"

    # --- PLAYER CHOICE: How does he handle the crowd (mask or not) ---
    menu:
        "Eyes follow him through the crowd; every step feels rehearsed."
        "Put on the Rylan mask.":
            $ aeron_masks_emotion = True
            a "{i}Smile. Small. Practiced. They see what they need to see.{/i}"
        "Let the mask slip.":
            $ aeron_masks_emotion = False
            a "{i}I stop pretending to breathe their air.{/i}"
    # -----------------------------------------------------------------

    # VISUAL: Marcus entrance—ceremonial armor; Enforcers flank; room tension rises.
    # SOUND: Conversations drop mid-sentence; music softens.
    "General Marcus Rylan steps into the light—armor flawless, formation exact."
    "{i}The room exhales. Every conversation pauses. Every eye tracks.{/i}"
    a "{i}The gravity tilts when he arrives. No applause—just fear dressed as respect.{/i}"
    a "{i}He doesn't need announcements. The silence does it for him.{/i}"

    # --- PLAYER CHOICE: Hide or meet Marcus’s gaze ---
    menu:
        "Marcus scans the room; his eyes brush over you for an instant."
        "Look away first.":
            $ aeron_avoids_marcus = True
            a "{i}Old habit—keep your head down and let the storm pass.{/i}"
        "Hold his gaze.":
            $ aeron_avoids_marcus = False
            a "{i}For a breath, I look back. His eyes read obedience—and failure.{/i}"
    # -------------------------------------------------

    a "{i}He does not look at me again.{/i}"

    # VISUAL: Lyra across the hall with a Councilwoman—composed, precise, unmissable.
    "Across the hall, Lyra stands with a Councilwoman—composed, precise, unmissable."
    a "{i}They parade her like proof the system still works.{/i}"

    # --- PLAYER CHOICE: acknowledge Lyra or not ---
    menu:
        "Lyra’s eyes meet yours for a heartbeat."
        "Acknowledge her.":
            $ aeron_acknowledged_lyra = True
            a "{i}I nod—barely. Enough to say I remember.{/i}"
        "Look away.":
            $ aeron_acknowledged_lyra = False
            a "{i}I let the moment die. Easier that way.{/i}"
    # ----------------------------------------------

    "Her eyes flick to Aeron for a heartbeat—then back."
    a "{i}Metal under the polish.{/i}"

    # Younger elites nearby (whispers).
    ye1 "I heard he was not even compatible."
    ye2 "Defect. Or curse. Maybe both."
    ye3 "Sad, really—pretending he belongs."
    ye2 "Marcus still spins it as 'fate.'"
    ye3 "Convenient word for failure."

    a "{i}I used to flinch. Now it is just another broken chorus.{/i}"

    # VISUAL: If holding a glass, hairline crack; otherwise, clenched fist.
    if aeron_has_glass:
        "{i}The stem creaks in his hand. A hairline crack crawls along the glass.{/i}"
    else:
        "{i}His fist tightens at his side; knuckles pale against the black fabric.{/i}"

    a "{i}They laugh like the world belongs to them.{/i}"
    a "{i}And I am expected to smile like I believe it.{/i}"

    # --- PLAYER CHOICE: Approach Lyra or keep distance ---
    menu:
        "Across the room, Lyra is momentarily alone."
        "Cross the floor toward Lyra.":
            $ aeron_moves_toward_lyra = True
            "{i}He threads through silk and medals, closing the distance.{/i}"
            $ aeron_spoke_to_lyra_gala = False  # flips true once dialogue happens

            # VISUAL: Councilwoman lingers, then steps aside.
            a "Lyra."
            "{i}She pivots, posture precise, eyes reading him in a single beat.{/i}"

            l "You are on time."
            if aeron_practiced_pledge:
                a "I remember the lines. It does not mean I will say them."
            else:
                a "On time is not the same as willing."

            l "Noted."
            $ aeron_spoke_to_lyra_gala = True

            "{i}A Council attaché leans in with a whisper. Lyra's attention splits—only for a moment.{/i}"
            l "The balcony, in five."
            a "I will be there."
            "{i}She is gone before the room notices she moved.{/i}"

        "Keep your distance.":
            $ aeron_moves_toward_lyra = False
            "{i}He holds position. The moment passes.{/i}"
            $ aeron_spoke_to_lyra_gala = False
    # -----------------------------------------------------

    # Tiny nod to pledge practice if present (cosmetic only).
    if aeron_practiced_pledge:
        "{i}A toast rises nearby—\"Order above all.\" The words come easy; he lets them die behind his teeth.{/i}"

    # VISUAL: Exit vector to balcony; soft cut from gold warmth to cooler night tones outside.
    if aeron_has_glass:
        "{i}He sets the glass down and moves toward the balcony doors.{/i}"
    else:
        "{i}He moves toward the balcony doors.{/i}"
    
    "{i}The doors open. Cold air rushes in.{/i}"

    # canon_note: Lyra in Act I avoids contractions and speaks with formal, melodic precision.
    # canon_note: Aeries lighting = top-down white/gold; gala warmth is performative, not genuine.
    # canon_note: New flags added (aeron_masks_emotion, aeron_avoids_marcus, aeron_acknowledged_lyra)
    #             can modulate future dialogue or internal monologues.

    return
