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
    # NEW: Last night's mission still in his mind
    a "{i}Six hours ago, I killed four people in Sector Seven.{/i}"
    a "{i}Now I'm here. Smiling. Performing.{/i}"
    a "{i}Glass transitions seamlessly.{/i}"

    # --- PLAYER CHOICE: A server offers a drink ---
    menu:
        "The server offers a glass of wine."
        "Take the glass.":
            $ aeron_has_glass = True
            # VISUAL/SFX: light clink
            a "{i}If I am a prop tonight, I may as well hold one.{/i}"
            # NEW: Glass holding glass
            a "{i}Glass holding glass. Appropriate.{/i}"
            
        "Refuse with a nod.":
            $ aeron_has_glass = False
            a "{i}No thanks.{/i}"
            a "{i}Glass doesn't need lubrication.{/i}"
    # ----------------------------------------------

    # VISUAL: The ballroom swells—music crescendos, voices layer, chandeliers pulse with reflected motion.
    "{i}The air thickens. Perfume, wine, polished metal. Too much of everything.{/i}"
    a "{i}Every surface reflects. Every sound echoes. No silence. No stillness. Just performance layered on performance.{/i}"

    # VISUAL: Aeron's vision briefly narrows—tunnel vision effect; edges blur, center sharpens.
    "{i}For a moment, the room contracts. Too bright. Too loud. Too many eyes.{/i}"
    a "{i}Breathe. Just breathe.{/i}"
    # NEW: Glass doesn't panic
    a "{i}Glass doesn't break in public. Hold the form.{/i}"

    # VISUAL: Aeron's hand steadies against a nearby column; brief pause.
    "{i}His pulse hammers. The room tilts, then steadies.{/i}"
    a "{i}Not here. Not now. Hold it together.{/i}"

    # VISUAL: A young man in full ceremonial dress approaches—confident stride, silver Band glinting on his wrist.
    # He's Aeron's age, polished, smiling with practiced ease.

    cadet "Aeron Rylan. Thought that was you."

    # VISUAL: Aeron steadies himself; the tunnel vision clears.
    a "(turns) Daren."

    # VISUAL: Daren extends his hand—firm handshake; his Band catches the chandelier light.
    # REVISED: Daren knows Aeron's record
    cadet "Been a while. Not since the Academy, right?"
    a "Something like that."

    cadet "(glances at medals, impressed) Heard about your last operation. Sector Nine?"
    a "(neutral) Sector Seven. This morning."
    cadet "(surprised) This morning? And you're here tonight?"
    a "Glass doesn't need recovery time."
    cadet "(nervous laugh) Glass. Right. They really call you that?"
    a "They do."

    # VISUAL: Daren shifts his weight—admiration mixed with unease.
    "{i}He respects the record. Fears the person.{/i}"
    
    cadet "Look, I just wanted to say... your record is insane. 390 operations, zero failures?"
    a "(neutral) Metrics don't lie."
    cadet "That's... that's impossible. In seven years?"
    a "Not impossible. Just inhuman."
    cadet "(uncomfortable) I didn't mean—"
    a "You did. And you're right."

    # VISUAL: Awkward pause; Daren taps his Band unconsciously—nervous habit.
    "{i}He touches his Band like a talisman. Proof he belongs. Proof he's safe.{/i}"
    "{i}And proof he's not like me.{/i}"

    cadet "Your father must be... proud."
    a "He has expectations. I meet them."
    cadet "That's... that's all any of us can do, right?"
    a "(looks at him directly) Is it?"

    # VISUAL: Silence. Daren realizes he's lost the thread.
    "{i}For a moment, something passes between them. Not quite understanding. Just... distance.{/i}"

    # --- PLAYER CHOICE: How does Aeron respond to Daren ---
    menu:
        "Daren's smile wavers."
        "Respond with cold courtesy.":
            $ aeron_dismisses_daren = True
            a "Enjoy the gala, Daren."
            # VISUAL: Aeron turns away; Daren's smile collapses into relief.
            cadet "Yeah. You too. Stay... stay sharp."
            "{i}He retreats into the crowd, grateful for the exit.{/i}"
            a "{i}He'll tell that story tomorrow. 'Glass doesn't even blink.' Let him.{/i}"
            
        "Acknowledge the awkwardness.":
            $ aeron_dismisses_daren = False
            a "You don't have to do this."
            cadet "(confused) Do what?"
            a "Pretend we're still who we were. We're not."
            cadet "(pause) ...No. I guess we're not."
            "{i}For a moment, something honest passes between them. Then it's gone.{/i}"
            cadet "(quieter) Take care of yourself, Aeron. If you still... can."
            a "I'll try."
            "{i}He walks away. Not relieved. Just... sad.{/i}"
            a "{i}He sees it. What I've become. What Glass is.{/i}"
            a "{i}And he's grateful it's not him.{/i}"
# ------------------------------------------------------

    # VISUAL: Overhead drone—live feeds rotate; Aeron's face flickers on a screen.
    a "{i}Even here, there is no room without a camera.{/i}"
    a "{i}Watching Glass perform. Recording the obedience.{/i}"

    # REVISED: Elite whispers - complete rewrite for Glass identity
    # Nearby elites whisper (kept as audible whispers).
    e1 "...Marcus Rylan's son. Glass."
    e2 "390 operations. Seven years. Zero failures."
    e3 "Technically perfect. But have you seen his eyes?"
    e1 "Empty. Like there's nothing behind them."
    e2 "Father's weapon. Not his heir."
    e3 "(quietly) I heard he doesn't feel it anymore. The kills."
    e1 "Doesn't feel anything. That's the problem."
    e2 "Problem? That's what makes him valuable."
    e3 "(softly) Or dangerous."

    # --- PLAYER CHOICE: Confront or pass by ---
    menu:
        "Aeron hears the whispers."
        "Confront them.":
            $ aeron_confronts_elites = True
            # VISUAL: slight camera jolt/push-in here if desired.
            a "For whispers, you carry a long way. Is there a problem?"
            # VISUAL: They turn; freeze slightly; hadn't realized he was close enough.
            e2 "Of course not, Aeron! We were just—"
            a "Discussing my utility? My emptiness? My eyes?"
            e1 "(quickly) We meant no disrespect. Your record speaks for itself."
            a "My record speaks. I don't need to."
            # VISUAL: Brief silence; they exchange glances.
            e3 "(carefully) Your father has every reason to be proud."
            a "Proud. Good word for it."
            # VISUAL: He turns and walks away; they exhale in relief.
            "{i}They don't speak again until he's out of earshot.{/i}"
            a "{i}Glass makes them nervous. Good.{/i}"
            
        "Ignore and move on.":
            $ aeron_confronts_elites = False
            "{i}He walks past. Their voices go brittle, safely behind him.{/i}"
            a "{i}Let them whisper. Glass doesn't need their approval.{/i}"
            a "{i}Glass just needs to function.{/i}"
    # ------------------------------------------

    # --- PLAYER CHOICE: How does he handle the crowd (mask or not) ---
    menu:
        "Eyes follow him through the crowd; every step feels rehearsed."
        "Put on the Rylan mask.":
            $ aeron_masks_emotion = True
            a "{i}Smile. Small. Practiced. They see what they need to see.{/i}"
            a "{i}Glass reflects their expectations back at them.{/i}"
            
        "Let the mask slip.":
            $ aeron_masks_emotion = False
            a "{i}I stop pretending to breathe their air.{/i}"
            a "{i}Let them see Glass for what it is. Empty.{/i}"
    # -----------------------------------------------------------------

    # VISUAL: Marcus entrance—ceremonial armor; Enforcers flank; room tension rises.
    # SOUND: Conversations drop mid-sentence; music softens.
    "General Marcus Rylan steps into the light—armor flawless, formation exact."
    "{i}The room exhales. Every conversation pauses. Every eye tracks.{/i}"
    a "{i}The gravity tilts when he arrives. No applause—just fear dressed as respect.{/i}"
    a "{i}He doesn't need announcements. The silence does it for him.{/i}"

    # --- PLAYER CHOICE: Hide or meet Marcus's gaze ---
    menu:
        "Marcus scans the room; his eyes brush over you for an instant."
        "Look away first.":
            $ aeron_avoids_marcus = True
            a "{i}Old habit—keep your head down and let the storm pass.{/i}"
            a "{i}Glass doesn't challenge its maker.{/i}"
            
        "Hold his gaze.":
            $ aeron_avoids_marcus = False
            a "{i}For a breath, I look back. His eyes read obedience—and emptiness.{/i}"
            a "{i}He made Glass. He knows what Glass is.{/i}"
            a "{i}And he's not sure if he should be proud or afraid.{/i}"
    # -------------------------------------------------

    a "{i}He does not look at me again.{/i}"
    # NEW: What that means
    a "{i}Acknowledged. Measured. Dismissed.{/i}"
    a "{i}The weapon is functional. That's all that matters.{/i}"

    # VISUAL: Lyra across the hall with a Councilwoman—composed, precise, unmissable.
    "Across the hall, Lyra stands with a Councilwoman—composed, precise, unmissable."
    a "{i}They parade her like proof the system still works.{/i}"
    # NEW: Recognition between weapons
    a "{i}Another perfect soldier. Another polished surface.{/i}"
    a "{i}I wonder if she's as empty as I am.{/i}"

    # --- PLAYER CHOICE: acknowledge Lyra or not ---
    menu:
        "Lyra's eyes meet yours for a heartbeat."
        "Acknowledge her.":
            $ aeron_acknowledged_lyra = True
            a "{i}I nod—barely. Enough to say I remember.{/i}"
            a "{i}Glass recognizing Glass.{/i}"
            
        "Look away.":
            $ aeron_acknowledged_lyra = False
            a "{i}I let the moment die. Easier that way.{/i}"
            a "{i}Glass doesn't need connections. Just orders.{/i}"
    # ----------------------------------------------

    "Her eyes flick to Aeron for a heartbeat—then back."
    a "{i}Metal under the polish.{/i}"
    # NEW: She sees it too
    a "{i}She knows. Somehow, she knows what Glass is.{/i}"

    # REVISED: Younger elites nearby - complete rewrite for Glass fear/fascination
    ye1 "I heard he's done nearly 400 operations."
    ye2 "In seven years? That's impossible."
    ye1 "Not impossible. Just... inhuman."
    ye3 "Father tried to make him a believer. Made Glass instead."
    ye2 "Glass?"
    ye3 "Transparent. Empty. Sharp when you need it."
    ye1 "(quietly) Has Glass ever broken?"
    ye3 "Not yet. But they say cracks are forming."
    ye2 "How can you tell if something empty is breaking?"
    ye3 "You can't. Until it shatters."

    a "{i}They're not wrong.{/i}"
    a "{i}Cracks are forming. Last night, I felt one spread.{/i}"
    a "{i}'Who taught me that word?' Mercy.{/i}"
    a "{i}Glass doesn't ask questions. But I did.{/i}"

    # VISUAL: If holding a glass, hairline crack; otherwise, clenched fist.
    if aeron_has_glass:
        "{i}The stem creaks in his hand. A hairline crack crawls along the glass.{/i}"
        a "{i}Even the glass I'm holding wants to break.{/i}"
        a "{i}Appropriate.{/i}"
    else:
        "{i}His fist tightens at his side; knuckles pale against the black fabric.{/i}"
        a "{i}Hold the form. Glass doesn't crack in public.{/i}"

    a "{i}They laugh like the world belongs to them.{/i}"
    a "{i}And I'm expected to smile like I believe it.{/i}"
    # NEW: What changed
    a "{i}Six hours ago, I executed four people without hesitation.{/i}"
    a "{i}Now I'm here, holding wine, making small talk.{/i}"
    a "{i}This is what Glass does. Transitions seamlessly.{/i}"
    a "{i}...So why does it feel different tonight?{/i}"

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

            l "You're on time."
            a "{i}Her voice is steady. But her eyes aren't.{/i}"
            a "{i}How long since she slept? Days? Weeks?{/i}"
            # REVISED: Reference to Glass identity
            if aeron_practiced_pledge:
                a "I remember the lines. Doesn't mean I believe them."
                l "Glass doesn't need belief. Just performance."
                a "You've heard."
                l "Everyone has heard."
            else:
                a "On time is not the same as willing."
                l "But Glass is always willing. That's what Glass does."
                a "(pause) You know."
                l "Of course I know."

            l "Noted."
            $ aeron_spoke_to_lyra_gala = True

            "{i}A Council attaché leans in with a whisper. Lyra's attention splits—only for a moment.{/i}"
            l "The balcony, in five."
            a "I'll be there."
            # NEW: Understanding between them
            l "(softer) Glass and glass. We should compare cracks."
            a "{i}And she's gone before the room notices she moved.{/i}"
            a "{i}She sees it. What I am. What she is.{/i}"
            a "{i}Maybe that's why she wants to talk.{/i}"

        "Keep your distance.":
            $ aeron_moves_toward_lyra = False
            "{i}He holds position. The moment passes.{/i}"
            $ aeron_spoke_to_lyra_gala = False
            a "{i}Glass doesn't need connections. Glass functions alone.{/i}"
            a "{i}...So why does that feel wrong?{/i}"
    # -----------------------------------------------------

    # Tiny nod to pledge practice if present (cosmetic only).
    if aeron_practiced_pledge:
        "{i}A toast rises nearby—\"Order above all.\" The words come easy; he lets them die behind his teeth.{/i}"
        a "{i}390 operations reciting those words.{/i}"
        a "{i}And I still don't know what they mean.{/i}"

    # VISUAL: Exit vector to balcony; soft cut from gold warmth to cooler night tones outside.
    if aeron_has_glass:
        "{i}He sets the cracked glass down and moves toward the balcony doors.{/i}"
        a "{i}Leave the broken glass behind. Appropriate metaphor.{/i}"
    else:
        "{i}He moves toward the balcony doors.{/i}"
    
    "{i}The doors open. Cold air rushes in.{/i}"
    a "{i}Time to stop performing. Time to breathe.{/i}"
    a "{i}Time to see if Glass can remember what it feels like to be human.{/i}"

    # canon_note: Lyra in Act I avoids contractions and speaks with formal, melodic precision.
    # canon_note: Aeries lighting = top-down white/gold; gala warmth is performative, not genuine.
    # canon_note: New flags added (aeron_masks_emotion, aeron_avoids_marcus, aeron_acknowledged_lyra)
    #             can modulate future dialogue or internal monologues.
    # canon_note: Elite whispers now FEAR/RESPECT Glass rather than mock failure - complete tonal shift
    # canon_note: Daren scene shows how peers see Aeron - admiration mixed with fear
    # canon_note: "390 operations" and "six hours ago" ground timeline - mission was this morning
    # canon_note: Lyra's "glass and glass" line sets up balcony conversation about their shared emptiness
    # canon_note: First hints that "cracks are forming" in Glass - seeds of breakdown

    return