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

    a "{i}All this gold to smooth over the cracks. Plaster over decay with opulence.{/i}"
    a "{i}Six hours ago, I killed four people in Sector Seven.{/i}"
    a "{i}Now I’m here. Smiling. Composed. As if blood rinses off that easily.{/i}"
    a "{i}But that's what they want, right? No conflict. No conscience. Just transition.{/i}"

    # VISUAL: The ballroom swells—music crescendos, voices layer, chandeliers pulse with reflected motion.
    "{i}The air thickens. Perfume, wine, polished metal. Too much of everything.{/i}"
    a "{i}Every surface reflects. Every sound echoes. No silence. No stillness. Just performance layered on performance.{/i}"

    # NEW: Pressure without break — subtle internal crack
    a "{i}This is protocol. Eyes ahead. Breath steady. Form intact.{/i}"
    a "{i}Still, something in the rhythm skips—half a heartbeat off.{/i}"
    a "{i}No one would notice.{/i}"
    a "{i}But I do.{/i}"
    a "{i}And cracks never start loud.{/i}"

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
    a "Recovery’s for people who feel it."
    cadet "(nervous laugh) Cold. They really call you that?"
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
            $ player_state["empathy_score"] -= 1
            a "Enjoy the gala, Daren."
            # VISUAL: Aeron turns away; Daren's smile collapses into relief.
            cadet "Yeah. You too. Stay... stay sharp."
            "{i}He retreats into the crowd, grateful for the exit.{/i}"
            a "{i}He’ll tell that story tomorrow. ‘Didn’t flinch. Didn’t blink.’{/i}"
            a "{i}Let him.{/i}"
            
        "Acknowledge the awkwardness.":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_05_gala", "acknowledge_daren")
            if player_state >= 2:
                a "You don't have to do this."
                cadet "(confused) Do what?"
                a "(softer) Pretend we’re still who we were. We're not."
            else:
                a "You don’t have to pretend. We’re not friends anymore."
            
            cadet "(pause) …No. I guess we’re not."
            "{i}For a moment, something real passes between them. Fragile. Brief.{/i}"
            cadet "(quieter) Take care of yourself, Aeron. If you still can."
            a "I’ll try."

            a "{i}He walks away. Not relieved. Just... sad.{/i}"
            a "{i}He sees it. What I’ve become.{/i}"
            a "{i}Maybe thats why he looked at me like that.{/i}"
            a "{i}Like he remembered something I forgot...{/i}"
            a "{i}Something from before I became this.{/i}"
            jump act1_daren_flashback
    # ------------------------------------------------------

    if check_scene_flag("act1_05_gala", "acknowledge_daren"):
        # VISUAL: Ambient reset — golden wash, camera resumes slow glide.
        "{i}The music resumes like it never stopped. Conversations blur back into motion.{/i}"
        a "{i}The past is always closer than I think.{/i}"
        a "{i}Even now, I see him. Not Daren today—Daren then. When we still thought this meant something.{/i}"

    # VISUAL: Overhead drone—live feeds rotate; Aeron's face flickers on a screen.
    a "{i}Even here, there's no room without a camera.{/i}"
    a "{i}Every movement measured. Every breath filed away.{/i}"

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

    # REVISED: Elite whispers — no choice, just observation
    "{i}Nearby, whispers slide beneath the music — rehearsed, polite, just loud enough.{/i}"
    e1 "...Marcus Rylan's son. Glass."
    e2 "390 operations. Zero failures. No margin for error."
    e3 "They say he doesn’t even flinch anymore. Doesn’t feel the kills."
    e1 "Is that strength... or vacancy?"
    e2 "Ask his father. That’s the point."

    # BRANCHING — Aeron's internal response varies with empathy
    if player_state["empathy_score"] >= 1:
        a "{i}Even their fear feels rehearsed. Like everything else in this place.{/i}"
        a "{i}They want me to be a myth. Easier than seeing the cracks.{/i}"
    else:
        a "{i}Let them think I don’t hear. Let them wonder what kind of machine watches them back.{/i}"
        a "{i}Their fear is useful. Fear doesn’t ask questions.{/i}"

    # VISUAL: Marcus entrance—ceremonial armor; Enforcers flank; room tension rises.
    # SOUND: Conversations drop mid-sentence; music softens.
    "{i}General Marcus Rylan steps into the light—armor flawless, formation exact.{/i}"
    "{i}The room exhales. Every conversation pauses. Every eye tracks.{/i}"
    a "{i}The gravity tilts when he arrives. No applause—just fear dressed as respect.{/i}"
    a "{i}He doesn't need announcements. The silence does it for him.{/i}"

    if player_state["empathy_score"] <= 0:
        # LOW EMPATHY: Marcus is satisfied
        a "{i}His gaze finds mine—for the briefest second. A subtle nod. Approval measured in microseconds.{/i}"
        a "{i}He’s read the reports. The sweep. The body count. No hesitation noted.{/i}"
        a "{i}This is what he wanted. Precision. Purity. Obedience.{/i}"
        a "{i}And now, recognition.{/i}"
    else:
        # HIGH EMPATHY: Marcus is uncertain
        a "{i}His eyes sweep past mine. No pause. No nod. Just calculation.{/i}"
        a "{i}He’s read the report. Saw the hesitation. The deviation from protocol.{/i}"
        a "{i}He doesn’t need to ask what’s wrong. He already knows.{/i}"
        a "{i}This isn’t what he trained me for.{/i}"

    # VISUAL: Lyra across the hall with a Councilwoman—composed, precise, unmissable.
    "{i}Across the hall, Lyra stands with a Councilwoman—composed, precise, unmissable.{/i}"
    a "{i}They parade her like proof the system still works.{/i}"
    a "{i}Another perfect soldier. Another polished surface.{/i}"
    a "{i}I wonder if she's as empty as I am.{/i}"

    "{i}Her eyes flick to Aeron for a heartbeat—then back.{/i}"

    # --- PLAYER CHOICE: acknowledge Lyra or not ---
    menu:
        "Lyra's eyes meet yours for a heartbeat."
        "Acknowledge her.":
            if player_state["empathy_score"] >= 3:
                $ add_affection("Lyra", 1)
            a "{i}I nod—barely. Memory, not invitation.{/i}"
            a "{i}The space between us tightens. Just for a second.{/i}"

        "Look away.":
            a "{i}I let the moment pass. Safer that way.{/i}"
            a "{i}Eyes forward. No room for ghosts tonight.{/i}"
    # ----------------------------------------------

    # BRANCHING THOUGHT BASED ON EMPATHY
    if player_state["empathy_score"] >= 1:
        a "{i}She sees it. Not the medals. Not the posture. The strain.{/i}"
        a "{i}Maybe she remembers what I was before the edges hardened.{/i}"
    else:
        a "{i}She sees exactly what they built. And doesn’t flinch.{/i}"
        a "{i}No pity. No softness. Just recognition.{/i}"


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