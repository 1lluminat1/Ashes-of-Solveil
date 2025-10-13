# act1_16_obsidian_bridge.rpy


# =======================================================
# ACT 1 - Scene 16: The Obsidian Bridge
# =======================================================


label act1_obsidian_bridge:
    # VISUAL: High, skeletal bridge; wind shear audible; city void beneath.
    # LIGHTING: Cold, thin; instrument glow on Zira's wrist console; occasional arc sparks.
    # SOUND: Cable creaks; distant vent roar; intermittent drone far off.

    "{i}Midnight. The Obsidian Bridge.{/i}"
    "{i}The air is colder here. Thinner. Rust, oil, static.{/i}"
    "{i}Each step on the bridge complains like a warning.{/i}"

    # VISUAL: Zira leans on the guardrail, one leg propped up, illuminated by pale wrist console glow.
    "{i}She's already there.{/i}"

    z "(without looking up) You're late, Rylan."
    a "You're lucky I came at all. This isn't exactly a welcoming spot."
    z "(grins) That's why I picked it. If someone tailed you, they'd hit the floor before me."

    # VISUAL: Aeron looks over the edge—vertigo shot; nothing but void and distant lights.
    "{i}He glances down. The drop swallows light. No bottom visible.{/i}"
    a "How far down does this go?"
    z "Far enough that no one's climbed back up to complain."

    # VISUAL: The bridge sways slightly in the wind; metal groans.
    "{i}The bridge shifts. Just slightly. Enough to remind him it's alive.{/i}"
    a "This thing safe?"
    z "Define safe."
    a "Not collapsing while we're on it."
    z "(shrugs) Mostly."

    # VISUAL: Spark arcs across a cable overhead; brief flash illuminates them both.
    "{i}A cable sparks. Light flares, dies. Shadows deepen.{/i}"

    # VISUAL: Zira finally turns to face him fully—sharp eyes, half-shadowed smirk.
    # Black hair streaked with neon purple, tied messily back. Younger than he expected.
    "{i}She turns. Sharp eyes. Half-shadowed smirk. Black hair streaked with neon purple.{/i}"
    "{i}Younger than he expected. But the bridge feels like her territory.{/i}"

    z "Aeron Rylan. Echelon's golden ghost. Thought you'd stand taller."

    # --- PLAYER CHOICE: Initial Response ---
    menu:
        "How does Aeron respond?"
        "Stay composed.":
            $ zira_rel += 1
            a "(dry) And I thought hackers were supposed to be subtle."
            z "(snorts) Subtle gets you killed. Fast keeps you fed."
            
        "Fire back.":
            a "(smirks) I thought you'd be more paranoid."
            z "(eyes narrow, but amused) I am. You just don't know what I'm watching yet."
            
        "Say nothing.":
            $ zira_rel -= 1
            a "..."
            z "(tilts her head) Ah. The brooding type. Cute."

    # VISUAL: She hops down from the railing, approaches—circling him like assessing a weapon.
    "{i}She hops down from the railing. Boots clank against rusted steel.{/i}"
    "{i}She circles him. Assessing.{/i}"

    z "So. Echelon sends their golden ghost to sweep Sector Ten."
    z "You know what that tells me?"
    a "Enlighten me."
    z "(laughs) 'Enlighten me.' Cute talk for a soldier."
    z "Tells me someone upstairs is shitting bricks. Looking for a scapegoat that photographs well."
    a "(carefully) You talk a lot for someone who's supposed to be helpful."
    z "(grins) I'm helpful. Just not obedient."

    # VISUAL: She stops circling—stands directly in front of him. Close.
    "{i}She stops. Stands close. Too close for professional distance.{/i}"

    z "You know why they really sent you down here?"
    a "To investigate the breach."
    z "(laughs) You actually believe that?"
    a "Should I not?"
    z "Sweetheart, they don't send Rylan's kid to investigate. They send him to be seen investigating."
    a "What's the difference?"
    z "One finds truth. The other buries it under good optics."

    # VISUAL: She taps her wrist console; data streams across the holo-display.
    "{i}Her fingers dance across light. Code scrolls, fragments, vanishes.{/i}"

    z "The breach wasn't random. It was surgical. Targeted three relay nodes simultaneously."
    z "Whoever did it knew the grid's architecture. Timing. Encryption keys."
    a "Inside job?"
    z "Or someone who used to be inside. Either way—wasn't me."
    a "Then why bring me here?"
    z "(leans in slightly) 'Cause I want you to see what happens when you start asking the right questions."

    # VISUAL: She pulls up a corrupted data file—fragmented but readable.
    "{i}Text flickers. Half-erased. Fighting to exist.{/i}"

    z "This is from the night of the breach. Encrypted comm-line."
    z "Someone in Echelon Command sent kill orders to the sector drones."
    z "Not shutdown. Not containment. {i}Kill.{/i}"
    a "(tense) That's standard protocol for—"
    z "(cuts him off) For what? Unarmed civilians? Kids hiding in maintenance tunnels?"
    a "You don't know that's—"
    z "I pulled the drone footage, Rylan. I know exactly what they killed."

    # VISUAL: She swipes the data away; the hologram dies.
    "{i}The light collapses. Darkness rushes back in.{/i}"

    z "So yeah. Someone breached the grid. And someone else used it as an excuse to clean house."
    a "(quiet) Why tell me this?"
    z "'Cause you're the only one up there who looks like he might actually give a shit."

    # VISUAL: Brief silence; wind howls through the bridge.
    "{i}Wind fills the silence. The city hums below.{/i}"

    # --- OPTIONAL CHEMISTRY MOMENT (if zira_rel is positive) ---
    if zira_rel >= 1:
        z "(softer) You hesitated. On that roof. I saw you."
        a "(tense) What roof?"
        z "The one you almost jumped off. I track Aeries movement patterns. Yours stopped making sense that night."
        a "(cold) You were spying on me?"
        z "I was watching someone who looked like he wanted out. Just like I do."
        
        # VISUAL: Something shifts between them—understanding, not quite trust.
        "{i}Her eyes soften. Just slightly. Not pity. Recognition.{/i}"
        
        a "(carefully) And what do you want?"
        z "Same thing you do. The truth. And maybe... someone who won't lie about it."

    # VISUAL: She pulls a small device from her coat—cracked, glowing faintly.
    "{i}She pulls a small device from her coat. Old. Cracked. Modified comm-relay.{/i}"

    z "This is what they're looking for. Reroutes data through ghostlines—clean, untraceable."
    z "Problem is... I'm not the only one who's got one."
    a "Then who leaked the data?"
    z "Not sure. But it wasn't me. That breach? Too sloppy. Too loud."
    z "Screamed bait. Someone wanted eyes down here."

    # --- PLAYER CHOICE: Trust Level ---
    menu:
        "She offers the device. What does Aeron do?"
        "Take it.":
            $ zira_rel += 1
            $ aeron_took_zira_device = True
            "{i}He takes it. The metal is warm from her pocket.{/i}"
            z "(nods) Good. Don't plug it into anything with eyes on it."
            z "If you ever want to know how deep it goes—find me again."
            a "How?"
            z "You found me once. You'll figure it out."
            
        "Refuse.":
            $ zira_rel -= 1
            $ aeron_took_zira_device = False
            a "I can't take that. Not yet."
            z "(shrugs) Your call. But when you're ready to see the whole picture—you know where I'll be."
            "{i}She pockets it again. No judgment. Just understanding.{/i}"

    # VISUAL: Distant drone sweeps past; searchlight rakes the lower levels.
    "{i}A drone cuts through the air below. Searchlight sweeping. Always hunting.{/i}"

    z "You should go. Sweep starts in a few hours. Wouldn't want you late for the show."
    a "The show?"
    z "Sector Ten. Your orders. The cleanup."
    z "(bitter) They're gonna burn it. And you're gonna watch."

    # VISUAL: She starts walking toward the opposite edge of the bridge.
    "{i}She turns. Starts walking away.{/i}"

    a "Zira—"
    z "(over her shoulder, doesn't stop) Next time, lose the leash, Rylan."
    z "Or don't come back."

    # VISUAL: She disappears into shadow; only her console light visible, then gone.
    "{i}She's gone. Swallowed by the dark.{/i}"

    # VISUAL: Aeron stands alone; city sprawls below; wind howls.
    "{i}He stands alone. The bridge groans beneath him.{/i}"
    a "{i}She knows. She knows what's coming.{/i}"
    a "{i}And she's giving me a choice.{/i}"

    if aeron_took_zira_device:
        # VISUAL: He looks at the device in his hand—small, heavy with implications.
        "{i}The device sits heavy in his palm. Heavier than it should be.{/i}"
        a "{i}Truth, she said. Let's see what kind of truth leaves bodies behind.{/i}"
    else:
        # VISUAL: His empty hands curl into fists.
        "{i}His hands are empty. But the weight remains.{/i}"
        a "{i}She's right. I'm still on the leash.{/i}"
        a "{i}But for how much longer?{/i}"

    # TRANSITION: Fade to black; hold 2 seconds.
    "{i}The bridge fades behind him. The sweep waits ahead.{/i}"
    "{i}And nothing will ever be the same.{/i}"
    
    return