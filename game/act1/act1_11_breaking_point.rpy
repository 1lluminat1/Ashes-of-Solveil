# act1_11_breaking_point.rpy


# ======================================================
# ACT 1 - Scene 11: Aeron's Breaking Point
# ======================================================


label act1_breaking_point:
    # VISUAL: Room in deep shadow; single city-light stripe across desk photo.
    # PROP: Brother photo face-up; mission envelope ajar.
    # SOUND: Low city wind; room ventilation click every ~10s.

    # VISUAL: Aeron picks up the photo—fingers trace the edge of the frame.
    "{i}He lifts the photo. Glass cold against his fingertips.{/i}"
    a "{i}You always smiled like you belonged.{/i}"
    a "{i}Seventeen. Same age I was when my Band shattered.{/i}"

    # VISUAL: Close-up on Kael's wrist in the photo—Band partially visible, gleaming.
    a "{i}Three months. That's all you got. Three months of being whole.{/i}"
    a "{i}Then the Band turned on you, and Father couldn't rewrite that story fast enough.{/i}"

    # VISUAL: He sets the photo down—not gently, not harshly. Just... empty.
    "{i}He sets it down. Face-up. Eyes still smiling.{/i}"
    a "{i}I used to hate you for leaving me here.{/i}"
    a "{i}Now I think I understand why.{/i}"
    a "{i}Not sadness. Not anger. Just the weight of breathing when there's no reason left to.{/i}"

    # BLOCKING: Stand; move to balcony.
    a "{i}I don't know if I'm angry anymore. Just tired.{/i}"
    a "{i}Tired of pretending any of this means something.{/i}"

    # LIGHTING: Cold air shifts curtains; bluish exterior tone.
    "{i}He opens the balcony door. Cold air moves through the room.{/i}"
    "{i}He steps outside.{/i}"

    # VISUAL: Wind immediate and sharp; hair whips across his face.
    # SOUND: Wind roar; distant sirens; structural hum.
    "{i}The wind hits like a wall. Cold. Relentless. The kind that strips everything bare.{/i}"

    # VISUAL: The city spreads below—layers of light, tier after tier descending into shadow.
    "{i}Solveil stretches beneath him. Aeries above. Middle grinding between. Unders drowning below.{/i}"
    a "{i}All that structure. All that order. And none of it leaves room for people like me.{/i}"
    a "{i}People like Kael.{/i}"

    # VISUAL: Distant drone passes—searchlight sweeps, doesn't reach this high.
    "{i}A drone cuts through the lower air. Searchlight raking the tiers. Hunting. Always hunting.{/i}"
    a "{i}They'll keep searching long after I'm gone. The system doesn't stop. It just replaces.{/i}"

    # VISUAL: He walks to the rail—each step deliberate.
    "{i}One foot. Then another. Closer.{/i}"

    # VISUAL: Hands grip the rail; knuckles pale against black metal.
    "{i}His hands find the rail. Metal bites through the cold—sharp, real.{/i}"
    a "{i}This is real. The only real thing left.{/i}"

    # VISUAL: He looks down—vertigo shot; city lights blur and stretch.
    # SOUND: Wind volume drops; heartbeat rises in the audio mix.
    "{i}Below, the city breathes. Lights pulse like veins. Distance warps perspective.{/i}"
    a "{i}How far is it? Does it matter?{/i}"

    # VISUAL: His breathing quickens—chest rising, visible exhale clouds.
    "{i}His breath comes faster. Shallow. The air won't fill his lungs.{/i}"

    # PROP: Cigarette; hands shake on ignite.
    a "{i}One last smoke...{/i}"
    "{i}His hands shake as he lights it. Smoke climbs into the dark.{/i}"

    # MEMORY FLASH: Kael standing at this same rail, arms spread, grinning.
    # VISUAL: Quick cut—desaturated, echo effect.
    k "(laughing) You know what's weird? Up here, I feel like I could actually fly."

    # RETURN TO PRESENT: Aeron's hands tremble on the rail.
    a "{i}You stood right here. Right here.{/i}"
    a "{i}Did it feel like this? Like the world was holding its breath?{/i}"
    a "{i}Did you hesitate? Or did you just... let go?{/i}"
    a "{i}I wish you'd left a note. Something. Anything but silence.{/i}"

    # VISUAL: He leans forward slightly—weight shifting.
    "{i}Gravity pulls. Subtle. Patient. It doesn't demand. It waits.{/i}"
    a "{i}It would be easy. Easier than this.{/i}"

    # MEMORY FLASH: Marcus at the Branding ritual, face stone as the Band shatters.
    # VISUAL: Quick cut—harsh white light, ceremonial robes.
    m "Fate chose differently."

    # RETURN TO PRESENT: Aeron's jaw clenches.
    a "{i}Fate. Destiny. Providence. Just prettier words for failure.{/i}"

    # MEMORY FLASH: Lyra on the balcony, cigarette ember glowing, eyes soft.
    # VISUAL: Quick cut—warm tones, intimate lighting.
    l "You are still here. That is something."

    # RETURN TO PRESENT: His grip tightens; the rail groans faintly.
    a "{i}Am I? Or am I just a ghost Father keeps animated?{/i}"

    # VISUAL: The mission envelope on his desk—visible through the open door, red seal glowing.
    "{i}Inside, the mission waits. Orders. Objectives. Another way to be useful without being whole.{/i}"
    a "{i}Sweep. Secure. Eliminate. As if purpose and violence are the same thing.{/i}"
    a "{i}Maybe that's all I am now. A weapon Father points at problems he can't solve with speeches.{/i}"

    # VISUAL: He shifts weight forward—just an inch. Toes at the edge of the platform.
    "{i}One more step. That's all it takes.{/i}"
    a "{i}Gravity does the rest.{/i}"

    a "{i}Maybe if I step over, it'll finally be quiet.{/i}"
    a "{i}No more missions.{/i}"
    a "{i}No more whispers.{/i}"
    a "{i}No more failure.{/i}"

    # VISUAL: His foot lifts—hovers over the edge.
    "{i}His foot rises. Hovers. The void opens beneath it.{/i}"
    a "{i}Just one step. One choice. Mine.{/i}"

    # VISUAL: Time stretches—wind sound warps, deepens; heartbeat isolates.
    "{i}The moment stretches. Sound distorts. Heartbeat fills the void.{/i}"
    a "{i}This is mine. Not Father's. Not Echelon's. Mine.{/i}"
    a "{i}For once, I get to choose.{/i}"

    # VISUAL: The cigarette burns down—ash breaks, falls, disappears into the dark below.
    "{i}Ash falls. Disappears. Like everything else.{/i}"

    # VISUAL: Extreme close-up—his eyes, reflected city lights swimming in tears he hasn't shed.
    a "{i}Would anyone even notice? Or would Father just spin another story?{/i}"
    a "{i}'Aeron Rylan, lost in the line of duty. A hero, like his brother.'{/i}"

    # SOUND: Heartbeat thunders; wind muffles to near-silence; moment stretches.
    "{i}Time slows. The city holds its breath.{/i}"

    menu:
        "Step forward":
            a "{i}Just one more step...{/i}"
        "Step back":
            a "{i}I can't keep living like this...{/i}"

    # SOUND: Two hard knocks; dry wood/metal timbre.
    "{i}A knock at the door. Sharp. Sudden. Like fate rapping on the walls.{/i}"

    # BLOCKING: He steps down from the rail; breath doesn't steady.
    "{i}He drops back to stone. The city noise thins; his heartbeat doesn't.{/i}"

    # VISUAL: He stands frozen—one hand still on the rail, body turned toward the door.
    a "{i}Who...?{/i}"

    # VISUAL: His hands are still shaking; he wipes his face quickly—checking for tears.
    "{i}His hands won't stop shaking. He wipes his eyes—just in case.{/i}"

    return