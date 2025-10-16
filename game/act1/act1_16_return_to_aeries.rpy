# act1_16_return_to_aeries.rpy


# =======================================================
# ACT 1 - Scene 16: Aeron Returns to the Aeries
# =======================================================


label act1_return_aeries:

    # VISUAL: Elevator ascending—glass walls, city sprawl visible outside.
    # LIGHTING: Transition from warm lower spans neon to cold Aeries white-blue.
    # SOUND: Elevator hum; mechanical clicks; his breathing.

    "{i}The elevator climbs. Each floor is a layer peeled away.{/i}"
    "{i}Neon fades. White light hardens. The air gets colder.{/i}"

    a "{i}800 people.{/i}"
    a "{i}Not soldiers. Not rebels. Families.{/i}"
    a "{i}And I'm ordered to kill them in six hours.{/i}"

    # VISUAL: City lights pass outside—levels rising, sectors dividing, distance growing.
    "{i}The city separates below him. Clean above. Desperate below. The line never blurs.{/i}"

    # NEW: Zira's words echoing
    a "{i}Zira said I have a choice. Not whether to obey. But HOW.{/i}"
    a "{i}'Glass follows orders. Humans find ways to resist even while obeying.'{/i}"
    a "{i}Can I do both? Obey Marcus and save them?{/i}"
    a "{i}Or is that just another lie Glass tells itself?{/i}"

    # VISUAL: Elevator doors open—Aeries corridor, pristine marble, perfect silence.
    # SOUND: Pneumatic hiss; footsteps on polished stone; distant fountain.

    "{i}The doors open. Silence swallows sound. Everything here is muffled, controlled.{/i}"

    # VISUAL: Two Echelon officers pass; they nod respectfully.
    officer1 "Glass."
    officer2 "Sir."

    # VISUAL: They continue past; don't wait for response.
    a "{i}They see Glass. Not Aeron. Just the weapon.{/i}"
    a "{i}That's all I've been. All Father made me.{/i}"
    a "{i}390 operations of being Glass. Tomorrow makes 391.{/i}"

    # VISUAL: His apartment door ahead; warm light leaking beneath.
    "{i}His door. The light underneath feels wrong—like walking toward a trap disguised as home.{/i}"

    # ACTION: Player choice—enter immediately or pause.
    menu:
        "The door waits. Inside, the mission order still glows on his terminal."
        "Enter immediately.":
            $ aeron_paused_at_door = False
            "{i}He doesn't pause. Hesitation is weakness.{/i}"
            a "{i}Glass doesn't hesitate.{/i}"
            a "{i}...But Glass is cracking.{/i}"
            
        "Pause at the threshold.":
            $ aeron_paused_at_door = True
            # VISUAL: Hand on door panel; doesn't activate it yet.
            "{i}His hand hovers over the panel. For a moment, he can't move.{/i}"
            a "{i}On the other side of this door is the mission.{/i}"
            a "{i}On the other side is Glass. Obedience. 391 operations.{/i}"
            a "{i}What's on this side?{/i}"
            a "{i}...Nothing. Just questions Glass isn't supposed to ask.{/i}"
            "{i}He opens the door.{/i}"

    # VISUAL: Interior—mission order still displayed on terminal, pulsing red notification.
    # SOUND: Soft chime; urgent reminder.

    "{i}The terminal blinks. Mission briefing. Deployment in 5 hours 47 minutes.{/i}"

    # VISUAL: Aeron stands in the doorway; silhouette against the light.
    a "{i}Right there. The orders. The coordinates. The lies.{/i}"
    a "{i}'Organized resistance activity.' 'Rebel communication networks.'{/i}"
    a "{i}All lies. Just families trying to survive.{/i}"

    # VISUAL: He crosses to the desk; hands brace against the surface.
    "{i}He crosses to the terminal. Hands flat against the desk. Steadying himself.{/i}"

    # NEW: Mission detail comparison
    # VISUAL: Screen shows official intel—200-500 targets, military threat assessment.
    "{i}The official intel: 200-500 hostile combatants. Threat level: High.{/i}"
    a "{i}Zira's intel: 800 civilians. Families. Children. Unregistered.{/i}"
    a "{i}One of them is lying. And I know which one.{/i}"

    # VISUAL: Split screen effect—official report vs what he saw in Lower Spans.
    # LEFT: Clinical text, threat assessments, military jargon
    # RIGHT: Vendor's face, child's eyes, families around fires
    "{i}Official report: 'High-density rebel infrastructure.'{/i}"
    "{i}Reality: A vendor selling real coffee. A child missing her father. Families keeping warm.{/i}"

    a "{i}I've done this 390 times. How many were lies like this?{/i}"
    a "{i}How many times did I kill families and call it 'neutralizing threats'?{/i}"

    # VISUAL: Kael's photo on the desk—still smiling, still whole.
    "{i}Kael's photo stares back. That smile. That hope.{/i}"
    a "{i}'Don't let Father turn you into a weapon,' you said.{/i}"
    a "{i}Too late, Kael. I've been a weapon for ten years.{/i}"
    a "{i}390 operations. All obedience. All Glass.{/i}"

    # ACTION: Player choice—pick up Kael's photo or leave it.
    menu:
        "Kael's photo sits between the mission order and the edge of the desk."
        "Pick up the photo.":
            $ aeron_held_kael_photo = True
            # VISUAL: He lifts it carefully; studies Kael's face.
            "{i}He lifts the photo. Glass cold against his fingers.{/i}"
            a "{i}You warned me. And I didn't listen.{/i}"
            a "{i}Or maybe I couldn't. Maybe Father was always going to turn me into this.{/i}"
            a "{i}But tomorrow... tomorrow I can try.{/i}"
            a "{i}Try to be human even while being Glass.{/i}"
            a "{i}Find the cracks. Save who I can. Even if it's not enough.{/i}"
            "{i}He sets it back down. Face-up. Eyes still watching.{/i}"
            a "{i}Maybe that's what you meant. Not 'don't become a weapon.'{/i}"
            a "{i}But 'remember you're human even when they use you as one.'{/i}"
            
        "Leave it where it is.":
            $ aeron_held_kael_photo = False
            "{i}He doesn't touch it. Can't.{/i}"
            a "{i}I failed you, Kael. Failed to stay human.{/i}"
            a "{i}Tomorrow I'll fail 800 more people.{/i}"
            a "{i}Glass doesn't save people. Glass just cuts.{/i}"

    # VISUAL: Window shows pre-dawn darkness; city lights pulsing below.
    # SOUND: Rain starting—soft taps against glass.
    "{i}Rain starts. Soft. Persistent. The city never truly sleeps.{/i}"

    # NEW: Tactical preparation
    # VISUAL: He opens wardrobe—tactical gear laid out, weapons cleaned, ammunition stocked.
    "{i}The gear waits. Black fabric. Cold metal. Tools of Glass.{/i}"
    
    a "{i}I could suit up now. Prepare like always. Check every weapon. Review every protocol.{/i}"
    a "{i}That's what Glass does. Perfect preparation. Perfect execution.{/i}"

    # ACTION: Player choice—prepare thoroughly or minimal prep.
    menu:
        "The tactical gear waits. Dawn approaches."
        "Prepare thoroughly—check weapons, review protocols, perfect readiness.":
            $ aeron_prepared_thoroughly = True
            # VISUAL: Montage—cleaning weapons, checking ammunition, reviewing mission specs.
            "{i}He goes through the motions. Muscle memory. Ten years of ritual.{/i}"
            # VISUAL: Rifle disassembly, cleaning, reassembly—precise, mechanical.
            "{i}Disassemble. Clean. Reassemble. Check sights. Load magazines.{/i}"
            # VISUAL: Tactical vest—check pouches, secure straps, test comms.
            "{i}Vest secured. Comms tested. Ammunition distributed. Everything perfect.{/i}"
            a "{i}Glass prepares. Glass doesn't fail.{/i}"
            a "{i}But preparation won't save them. Only choices will.{/i}"
            
        "Minimal preparation—enough to function, not enough to perfect.":
            $ aeron_prepared_thoroughly = False
            # VISUAL: He checks his sidearm—basic function test, nothing more.
            "{i}He checks his sidearm. Loads one magazine. Leaves the rest.{/i}"
            a "{i}I don't need perfection tomorrow. I need humanity.{/i}"
            a "{i}Glass prepares perfectly. Maybe imperfection is the crack I need.{/i}"

    # VISUAL: Mission countdown—4 hours 12 minutes.
    "{i}The countdown continues. Relentless. Dawn approaches whether he's ready or not.{/i}"

    # NEW: Lyra's words echoing
    a "{i}Lyra said Glass is breaking. That it might be what saves me.{/i}"
    a "{i}Zira said show her I'm human, not Glass.{/i}"
    a "{i}Kael said don't let Father turn me into a weapon.{/i}"
    a "{i}But I AM a weapon. Have been for 390 operations.{/i}"
    a "{i}Can I be both? Weapon and human? Glass and whole?{/i}"

    # VISUAL: He sits on the edge of his bed; head in hands.
    "{i}He sits. The weight settles. Too heavy to stand.{/i}"

    a "{i}Tomorrow I kill 800 people. Or I try to save them.{/i}"
    a "{i}Or maybe... maybe I kill 600 and save 200.{/i}"
    a "{i}That's not victory. That's just less horror.{/i}"
    a "{i}But maybe that's all Glass can do. Find the cracks. Save fragments.{/i}"

    # VISUAL: Close-up on his hands—trembling slightly.
    "{i}His hands shake. Just slightly. Glass cracking.{/i}"

    a "{i}Zira said trying matters. Even if it's not enough.{/i}"
    a "{i}Even if I lose. Even if I can't save them all.{/i}"
    a "{i}Trying makes me human. Obeying perfectly keeps me Glass.{/i}"

    # VISUAL: Mission countdown—3 hours 58 minutes.
    # SOUND: Rain intensifies; thunder distant.
    "{i}Thunder rolls. The storm is coming. In more ways than one.{/i}"

    # NEW: Choice crystallizing
    a "{i}I can't refuse the mission. Marcus owns me. The system owns me.{/i}"
    a "{i}But I can choose HOW I obey.{/i}"
    a "{i}Warn people. Fake reports. Look the other way. Find the cracks.{/i}"
    a "{i}Glass follows orders. Humans resist even while obeying.{/i}"
    a "{i}Tomorrow... tomorrow I'll try to be both.{/i}"

    # VISUAL: He stands; crosses to window; watches rain.
    "{i}He stands at the window. Rain streaks the glass. City blurs beyond.{/i}"

    a "{i}Operation 391. The count continues.{/i}"
    a "{i}But maybe... maybe this is where Glass starts breaking for real.{/i}"
    a "{i}Not shattering. Just... cracking enough to let the human through.{/i}"

    # VISUAL: Dawn beginning—horizon lightening, darkness retreating.
    "{i}The horizon lightens. Dawn approaches. The city wakes.{/i}"
    "{i}And Sector 10 doesn't know what's coming.{/i}"

    # VISUAL: He turns from window; moves toward gear.
    a "{i}Time to go.{/i}"
    a "{i}Time to be Glass one more time.{/i}"
    a "{i}But this time... this time Glass bleeds.{/i}"

    # TRANSITION: Fade to black; sound of rain continues.
    # TEXT OVERLAY: "Dawn. Sector 10."

    # canon_note: Zira's words about "HOW you obey" echo throughout
    # canon_note: Kael's warning resonates—trying to remember humanity within weapon
    # canon_note: Lyra's observation about Glass breaking = salvation
    # canon_note: Player choices (pausing, photo, preparation) affect Aeron's mental state
    # canon_note: "600 dead, 200 saved" concept planted—not binary, but spectrum
    # canon_note: Sets up Sweep scene—he's CHOOSING to find cracks in orders
    # canon_note: "Glass bleeds" = new identity forming—weapon with humanity

    return