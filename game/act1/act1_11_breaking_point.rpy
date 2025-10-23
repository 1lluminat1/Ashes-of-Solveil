# ======================================================
# ACT 1 - Scene 11: Aeron's Breaking Point
# ======================================================

label act1_breaking_point:

    # VISUAL: Room in deep shadow; single city-light stripe across desk photo.
    # PROP: Brother photo face-up; mission envelope ajar.
    # SOUND: Low city wind; room ventilation click every ~10s.

    "{i}He lifts the photo. Glass cold against his fingertips.{/i}"
    a "{i}You always smiled like you belonged.{/i}"
    a "{i}Fifteen. Your Band had three years. Then it turned on you.{/i}"

    "{i}He sets it down. Face-up. Eyes still smiling.{/i}"
    a "{i}I used to hate you for leaving me here.{/i}"
    a "{i}Now I think I understand why.{/i}"
    a "{i}You couldn’t live as Glass. You couldn’t be Father’s weapon.{/i}"
    a "{i}You jumped because the cage was worse than falling.{/i}"
    a "{i}Not sadness. Not anger. Just the weight of breathing when there’s no reason left to.{/i}"

    # ------------------------------------------------------
    # EMPATHY-BASED INTERNAL MONOLOGUE VARIATION
    # ------------------------------------------------------
    $ score = player_state["empathy_score"]

    if score <= -4:
        a "{i}I don’t know if I’m angry anymore. Just tired.{/i}"
        a "{i}Tired of pretending any of this means something. Tired of wasting efficiency on meaning.{/i}"
        a "{i}Glass doesn’t dream. Glass concludes.{/i}"

    elif -3 <= score <= 1:
        a "{i}I don’t know if I’m angry anymore. Just tired.{/i}"
        a "{i}Tired of pretending any of this means something.{/i}"
        a "{i}Tired of following orders just to keep breathing.{/i}"

    else:
        a "{i}I don’t know if I’m angry anymore. Just tired.{/i}"
        a "{i}Tired of pretending any of this means something.{/i}"
        a "{i}Maybe it could, if I still remembered how to feel.{/i}"

    # ------------------------------------------------------

    "{i}He opens the balcony door. Cold air moves through the room.{/i}"
    "{i}He steps outside.{/i}"
    "{i}The wind hits like a wall. Cold. Relentless. The kind that strips everything bare.{/i}"

    "{i}Solveil stretches beneath him. Aeries above. Middle grinding between. Unders drowning below.{/i}"
    a "{i}All that structure. All that order. And none of it leaves room for people like me.{/i}"
    a "{i}People like Kael.{/i}"
    a "{i}Just Glass. Reflecting what they want. Cutting when commanded. Empty always.{/i}"

    "{i}A drone cuts through the lower air. Searchlight raking the tiers. Hunting. Always hunting.{/i}"
    a "{i}They’ll keep searching long after I’m gone. The system doesn’t stop. It just replaces.{/i}"
    a "{i}Glass breaks. They’ll make more. They always do.{/i}"

    "{i}His hands find the rail. Metal bites through the cold—sharp, real.{/i}"
    a "{i}This is real. The only real thing left.{/i}"
    "{i}Below, the city breathes. Lights pulse like veins. Distance warps perspective.{/i}"
    a "{i}How far is it? Does it matter?{/i}"
    a "{i}Glass shatters when it falls. Quick. Clean. Final.{/i}"

    "{i}His breath comes faster. Shallow. The air won’t fill his lungs.{/i}"
    a "{i}One last smoke...{/i}"
    "{i}His hands shake as he lights it. Smoke climbs into the dark.{/i}"

    k "(laughing) You know what’s weird? Up here, I feel like I could actually fly."
    a "{i}You stood right here. Right here.{/i}"
    a "{i}Did it feel like this? Like the world was holding its breath?{/i}"
    a "{i}Did you hesitate? Or did you just... let go?{/i}"
    a "{i}You couldn’t be Glass. You refused to be Father’s weapon.{/i}"
    a "{i}I became exactly what you warned me not to.{/i}"
    a "{i}And now I understand why you jumped.{/i}"
    a "{i}I wish you’d left a note. Something. Anything but silence.{/i}"

    "{i}Gravity pulls. Subtle. Patient. It doesn’t demand. It waits.{/i}"
    a "{i}It would be easy. Easier than this.{/i}"
    a "{i}Glass falls. Glass shatters. Glass doesn’t feel it.{/i}"

    m "Fate chose differently."
    a "{i}Fate. Destiny. Providence. Just prettier words for failure.{/i}"
    a "{i}You said fate. Then you made me Glass.{/i}"
    a "{i}Ten years. 390 operations. Perfect obedience. Perfect emptiness.{/i}"

    l "Glass is breaking. That might be what saves you."
    a "{i}She sees it. The cracks spreading.{/i}"
    a "{i}Glass recognizes glass.{/i}"
    a "{i}Maybe she’s right. Maybe breaking is the only way out.{/i}"

    "{i}Inside, the mission waits. Orders. Objectives. Another way to be useful without being whole.{/i}"
    a "{i}Sweep. Secure. Eliminate. As if purpose and violence are the same thing.{/i}"
    a "{i}Operation 391. Glass completes missions. Glass obeys.{/i}"
    a "{i}Maybe that’s all I am now. A weapon Father points at problems he can’t solve with speeches.{/i}"

    "{i}One more step. That’s all it takes.{/i}"
    a "{i}Gravity does the rest.{/i}"

    # ------------------------------------------------------
    # EMPATHY VARIATION – approaching the menu
    # ------------------------------------------------------
    if score <= -4:
        a "{i}Father made me efficient. Ending myself would just be another operation.{/i}"
        a "{i}Quick. Clean. No deviation.{/i}"
    elif -3 <= score <= 1:
        a "{i}I don’t know if I want to die or stop being this thing he made.{/i}"
    else:
        a "{i}Maybe breaking doesn’t mean ending. Maybe it means finally beginning.{/i}"
    # ------------------------------------------------------

    menu:
        "Step forward":
            a "{i}Just one more step...{/i}"
            a "{i}Glass falls. Glass breaks. Glass—{/i}"
            $ set_scene_flag("act1_11_breaking_point", "step_forward")
        "Step back":
            a "{i}I can’t keep living like this...{/i}"
            a "{i}But maybe... maybe breaking doesn’t mean falling.{/i}"
            a "{i}Maybe it means shattering the Glass and finding what’s underneath.{/i}"
            $ set_scene_flag("act1_11_breaking_point", "step_back")

    "{i}A knock at the door. Sharp. Sudden. Like fate rapping on the walls.{/i}"
    "{i}He drops back to stone. The city noise thins; his heartbeat doesn’t.{/i}"
    a "{i}Who...?{/i}"
    "{i}His hands won’t stop shaking. He wipes his eyes—just in case.{/i}"

    # ------------------------------------------------------
    # EMPATHY VARIATION – reaction to the knock
    # ------------------------------------------------------
    if score <= -4:
        a "{i}Efficiency interrupted. Fate disagrees.{/i}"
        $ set_scene_flag("act1_11_breaking_point", "aeron_accepted_death")
    elif -3 <= score <= 1:
        a "{i}Someone always knocks before the fall.{/i}"
        $ set_scene_flag("act1_11_breaking_point", "aeron_contemplated")
    else:
        a "{i}Maybe that knock was the world reminding me I’m still here.{/i}"
        $ set_scene_flag("act1_11_breaking_point", "aeron_reconsidered")
    # ------------------------------------------------------

    a "{i}Glass doesn’t cry. Glass doesn’t break.{/i}"
    a "{i}Not in front of anyone.{/i}"

    # canon_notes
    # - Kael: 15 when Band failed, 17 when he jumped
    # - Aeron: 22, 390 operations complete
    # - Empathy tiers color tone but outcome fixed (knock interrupt)
    # - Flags: step_forward / step_back + emotional response tracking
    # - Seeds Act 2 emotional divergence and future Lyra callback

    return
