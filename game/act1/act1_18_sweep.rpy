# act1_18_sweep.rpy


# =======================================================
# ACT 1 - Scene 18: The Sweep
# =======================================================


define boy = Character("Boy")
define en1 = Character("Enforcer 1")
define en2 = Character("Enforcer 2")
define en3 = Character("Enforcer 3")
define en4 = Character("Enforcer 4")
define en5 = Character("Enforcer 5")

label act1_sweep:
    # VISUAL: Transition from the Obsidian Bridge — dissolve from cold blue light to red emergency strobes.
    # SOUND: Alarms fading, replaced by the distant thump of rotorcraft and crackle of fires.
    # LIGHTING: Harsh, intermittent — emergency lights strobing through smoke.

    "{i}Sector Ten. Twenty minutes later.{/i}"
    "{i}The order was simple: Sweep. Secure. Eliminate.{/i}"
    "{i}Simple words for something that never is.{/i}"

    # VISUAL: Aeron moves through a narrow corridor, weapon drawn; lights flicker overhead.
    # CAMERA: Handheld-style sway; shoulder-level tracking shot.
    "{i}The Unders don’t scream anymore. They’ve learned it changes nothing.{/i}"

    # SOUND: distant muffled gunfire; hiss of coolant vents.
    a "{i}This sector’s supposed to be quiet. No resistance reports. No hostiles.{/i}"
    a "{i}So why the hell does it smell like smoke and blood?{/i}"

    # VISUAL: He turns a corner — debris, collapsed piping, shattered terminals.
    "{i}Sparks dance across metal like fireflies with nowhere left to go.{/i}"

    # SOUND: shouts up ahead — Enforcer voices, filtered through helmets.
    en1 "Move it! We clear this block before shift rotation!"
    en2 "Orders were total sweep. Anyone left breathing is a risk."
    en3 "Copy that."

    # VISUAL: Aeron moves closer; heat shimmer distorts the corridor ahead.
    "{i}He steps into the light. Three Enforcers, rifles up, smoke curling around their armor.{/i}"

    a "Report."
    en1 "Sector’s clean. A few stragglers tried to hide in the maintenance alcoves."
    a "Civilians?"
    en1 "Designation irrelevant, sir. Orders were eliminate."
    a "{i}Eliminate.{/i}"

    # VISUAL: A small hand slips out from under rubble; movement catches Aeron’s eye.
    # SOUND: faint cough from a child.
    "{i}Something moves under the debris — small, shivering.{/i}"

    a "Hold fire!"
    en2 "Sir?"
    a "There’s a survivor."

    # CAMERA: close-up — Aeron kneels, pushes metal aside; a young boy, soot-streaked, eyes wide.
    a "Easy... you’re alright."
    boy "(weak) My sister... please—"
    en2 "Sir, that’s a contaminant risk. Procedure says—"
    a "Procedure says nothing about shooting kids."
    en2 "Procedure says no witnesses."

    # SOUND: safety click — rifle raised.
    "{i}Aeron turns, hand raised, voice sharp.{/i}"

    a "Stand down. That’s an order."
    en2 "(hesitates) General Rylan said total sweep—"
    a "Then consider this sector swept."

    # LIGHTING: flash of muzzle flare behind them — another Enforcer fires offscreen.
    # SOUND: single shot; scream abruptly cut.
    "{i}The air splits. Another shot — somewhere down the hall.{/i}"

    a "(under breath) God damn it..."

    "{i}He looks back — the boy’s sister lies crumpled near a stairwell. The Enforcer holsters without looking.{/i}"

    en3 "Hostile movement, sir. Eliminated."
    a "{i}Hostile.{/i}"

    # CAMERA: linger on Aeron’s face — smoke and red light wash over him.
    a "{i}This isn’t recon. It’s punishment.{/i}"

    # VISUAL: Tessa enters from the far side, hood up, med-kit slung over her shoulder.
    # SOUND: her footsteps quick, purposeful; she kneels beside a wounded civilian.
    t "(snapping) Move! I need that space clear!"
    en1 "This zone’s restricted. Medicals wait for command authorization."
    t "Authorization doesn’t stop bleeding!"
    a "(turns) Who the hell are you?"
    t "The only one trying to keep them alive!"

    # CAMERA: dolly in on her — dim green light reflecting in her eyes.
    "{i}She works fast — patching torn flesh with makeshift bio-gel, sealing wounds with trembling precision.{/i}"

    a "(softer) You shouldn’t be here."
    t "Neither should they. Or you, if you still think this is helping."

    # SOUND: distant explosion shakes dust loose; lights flicker out, emergency lamps kick in.
    # LIGHTING: all red now, pulsing like a heartbeat.
    a "{i}The corridor glows red — like the city itself is bleeding from the inside.{/i}"

    # --- PLAYER CHOICE 1: Intervention ---
    menu:
        "What does Aeron do?"
        "Help Tessa with the wounded":
            $ tessa_rel += 1
            # VISUAL: Aeron kneels beside her; passes tools, holds compresses.
            a "Tell me what you need."
            t "(surprised) You’re actually helping?"
            a "For now."
            t "(quietly) Then hold this — and don’t let him go."

            "{i}He presses his hand to the wound. The man’s pulse flutters beneath his palm.{/i}"

            a "{i}The uniform suddenly feels heavier than armor.{/i}"
        "Stay with the Enforcers":
            $ tessa_rel -= 1
            a "You’re out of line, civilian."
            t "So are you, if you still have a heartbeat."

            "{i}She ignores him, working faster, defiant under the glow.{/i}"
            
            a "{i}Her hands move like she’s trying to rebuild the world one body at a time.{/i}"

    # SOUND: approaching footsteps — a squad returning from the other end.
    en4 "Grid Six-Two secured! Minimal resistance!"
    en5 "(laughs) Minimal’s generous. Half these rats didn’t even run."

    # VISUAL: One soldier drags a wounded man by the collar, dropping him in the center of the corridor.
    en5 "Found this one snoopin’ around the relay. Probably one of those data-runners."
    a "He’s unarmed."
    en5 "You think that matters?"
    en1 "Protocol’s protocol."

    # --- PLAYER CHOICE 2: Confront or stay silent ---
    menu:
        "A soldier raises his weapon over the prisoner."
        "Intervene":
            $ aeron_defied_orders = True
            a "Stand down! That’s an order!"
            en5 "With respect, sir, your father said—"
            a "I said stand down!"
            # SOUND: tense silence; rifles lower reluctantly.
            a "{i}They listen. But the looks they give me could kill faster than bullets.{/i}"
        "Say nothing":
            $ aeron_defied_orders = False
            "{i}He says nothing. The shot rings out anyway.{/i}"
            "{i}The smell of ozone and iron fills the hall.{/i}"
            a "{i}And a piece of me goes with it.{/i}"

    # VISUAL: The civilians are either dead or gone. Tessa wipes blood from her hands; her expression unreadable.
    t "If this is order, then maybe the world was better when it was broken."
    a "You don’t understand—"
    t "I understand enough. You wear their mark, so you think you’re clean."
    a "(low) It’s not that simple."
    t "It never is. But it should be."

    # CAMERA: she steps past him, grabs her kit, heads toward the exit.
    t "(softer, without turning) You saw what they did. Don’t pretend you didn’t."
    a "(calling after her) What’s your name?"
    t "(pauses) Tessa. And you don’t get to forget it."

    # SOUND: her footsteps fade; wind howls through broken structure.
    "{i}For a moment, there’s only the sound of the city breathing through the cracks.{/i}"

    a "{i}Sweep. Secure. Eliminate.{/i}"
    a "{i}That’s what they told me.{/i}"
    a "{i}But they never said who was left to clean up what’s left.{/i}"

    # VISUAL: Aeron looks down at his bloodstained gloves. Red against black.
    # TRANSITION: Match cut to his apartment holo-console powering up.
    # COLOR: fade red → sterile blue.

    return
