# act1_16_return_to_aeries.rpy


# =======================================================
# ACT 1 - Scene 16: Aeron Returns to the Aeries
# =======================================================


define o1 = Character("Officer 1")
define o2 = Character("Officer 2")


label act1_return_aeries:
    $ scene_id = "act1_16_return_to_aeries"

    # Quick alignment reads for flavor (no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1

    # VISUAL: Elevator ascending—glass walls, city sprawl visible outside.
    # LIGHTING: Transition from warm lower spans neon to cold Aeries white-blue.
    # SOUND: Elevator hum; mechanical clicks; his breathing.

    "{i}The elevator climbs. Each floor is a layer peeled away.{/i}"
    "{i}Neon fades. White light hardens. The air gets colder.{/i}"

    a "{i}Eight hundred people.{/i}"
    a "{i}Not soldiers. Not rebels. Families.{/i}"
    a "{i}And I'm ordered to kill them in six hours.{/i}"

    "{i}The city separates below him. Clean above. Desperate below. The line never blurs.{/i}"

    a "{i}Zira said I have a choice—not whether to obey, but how.{/i}"
    a "{i}'Glass follows orders. Humans find ways to resist even while obeying.'{/i}"
    a "{i}Can I do both? Obey Marcus and save them?{/i}"
    a "{i}Or is that just another lie Glass tells itself?{/i}"

    "{i}The doors open. Silence swallows sound. Everything here is muffled, controlled.{/i}"

    o1 "Glass."
    o2 "Sir."

    a "{i}They see Glass. Not Aeron. Just the weapon.{/i}"
    a "{i}That's all I've been. All Father made me.{/i}"
    a "{i}Three hundred ninety operations. Tomorrow makes three ninety-one.{/i}"

    "{i}His door waits ahead. Light leaks beneath like a trap disguised as home.{/i}"

    # ---------------------------------------------------
    # CHOICE — approach
    # ---------------------------------------------------
    menu:
        "The door waits. Inside, the mission order still glows on his terminal."
        "Enter immediately.":
            $ set_scene_flag(scene_id, "entered_immediately")
            $ adjust_empathy_once("a16_enter_immediately", -1)
            "{i}He doesn't pause. Hesitation is weakness.{/i}"
            a "{i}Glass doesn't hesitate.{/i}"
            a "{i}...But Glass is cracking.{/i}"

        "Pause at the threshold.":
            $ set_scene_flag(scene_id, "paused_at_door")
            $ adjust_empathy_once("a16_pause_threshold", +1)
            "{i}His hand hovers over the panel. For a moment, he can't move.{/i}"
            a "{i}On the other side of this door is the mission—obedience, 391 operations.{/i}"
            a "{i}What's on this side?{/i}"
            a "{i}Nothing. Just questions Glass isn't supposed to ask.{/i}"
            "{i}He opens the door.{/i}"

    "{i}The terminal blinks: deployment in five hours, forty-seven minutes.{/i}"

    a "{i}Right there. The orders. The coordinates. The lies.{/i}"
    a "{i}'Organized resistance activity.' 'Rebel communication networks.'{/i}"
    a "{i}All lies. Just families trying to survive.{/i}"

    "{i}He braces both hands on the desk. The weight settles.{/i}"

    "{i}Official intel: 200–500 hostile combatants. Threat level: High.{/i}"
    a "{i}Zira's intel: 800 civilians. Families. Children. Unregistered.{/i}"
    a "{i}One of them is lying. And I know which one.{/i}"

    "{i}Official report: 'High-density rebel infrastructure.'{/i}"
    "{i}Reality: a vendor selling real coffee, a child missing her father, families keeping warm.{/i}"

    a "{i}I've done this 390 times. How many were lies like this?{/i}"
    a "{i}How many times did I kill families and call it 'neutralizing threats'?{/i}"

    "{i}Kael's photo waits on the desk—still smiling, still whole.{/i}"
    a "{i}'Don't let Father turn you into a weapon,' you said.{/i}"
    a "{i}Too late. I've been a weapon for ten years.{/i}"

    # ---------------------------------------------------
    # CHOICE — Kael's photo
    # ---------------------------------------------------
    menu:
        "Kael's photo sits between the mission order and the edge of the desk."
        "Pick up the photo.":
            $ set_scene_flag(scene_id, "picked_up_kael_photo")
            $ adjust_empathy_once("a16_pick_up_kael_photo", +1)
            "{i}He lifts the photo. Glass cold against his fingers.{/i}"
            a "{i}You warned me, Kael. Maybe tomorrow I listen.{/i}"
            a "{i}Try to be human even while being Glass.{/i}"
            a "{i}Find the cracks. Save who I can. Even if it's not enough.{/i}"
            "{i}He sets it down—face-up, still watching.{/i}"
            a "{i}Maybe that's what you meant. Not 'don't become a weapon,'{/i}"
            a "{i}but 'remember you're human even when they use you as one.'{/i}"

        "Leave it where it is.":
            $ set_scene_flag(scene_id, "left_kael_photo")
            $ adjust_empathy_once("a16_leave_kael_photo", -1)
            "{i}He doesn't touch it. Can't.{/i}"
            a "{i}I failed you, Kael. Tomorrow I'll fail 800 more.{/i}"
            a "{i}Glass doesn't save people. Glass just cuts.{/i}"

    "{i}Rain starts, soft and steady. The city never sleeps.{/i}"

    "{i}The gear waits. Black fabric. Cold metal. Tools of Glass.{/i}"
    a "{i}I could prepare like always. Perfect execution. Perfect obedience.{/i}"

    # ---------------------------------------------------
    # CHOICE — preparation style
    # ---------------------------------------------------
    menu:
        "The tactical gear waits. Dawn approaches."
        "Prepare thoroughly — perfect readiness.":
            $ set_scene_flag(scene_id, "prepared_thoroughly")
            $ adjust_empathy_once("a16_prepare_thoroughly", -1)
            "{i}He moves on muscle memory—ritual precision.{/i}"
            "{i}Disassemble. Clean. Reassemble. Check sights. Load magazines.{/i}"
            a "{i}Glass prepares. Glass doesn't fail.{/i}"
            a "{i}But preparation won't save them. Only choices will.{/i}"

        "Minimal preparation — enough to function.":
            $ set_scene_flag(scene_id, "minimal_prep")
            $ adjust_empathy_once("a16_minimal_prep", +1)
            "{i}He checks his sidearm. Loads one magazine. Leaves the rest.{/i}"
            a "{i}I don't need perfection tomorrow. I need humanity.{/i}"
            a "{i}Maybe imperfection is the crack I need.{/i}"

    "{i}Countdown: four hours twelve minutes.{/i}"

    a "{i}Lyra said Glass is breaking—that it might save me.{/i}"
    a "{i}Zira said show her I'm human, not Glass.{/i}"
    a "{i}Kael said don't let Father turn me into a weapon.{/i}"
    a "{i}But I am a weapon. Can I be both? Glass and whole?{/i}"

    "{i}He sits on the bed; the weight settles. Hands tremble—just slightly.{/i}"

    a "{i}Tomorrow I kill eight hundred people. Or try to save them.{/i}"
    a "{i}Maybe I kill six hundred and save two hundred. Less horror, not victory.{/i}"
    a "{i}Maybe that's all Glass can do—find cracks and save fragments.{/i}"

    a "{i}Zira said trying matters, even if it’s not enough.{/i}"
    a "{i}Trying makes me human. Obeying perfectly keeps me Glass.{/i}"

    "{i}Thunder rolls outside. The storm comes.{/i}"

    a "{i}I can’t refuse the mission. Marcus owns me. The system owns me.{/i}"
    a "{i}But I can choose how I obey.{/i}"
    a "{i}Warn people. Fake reports. Look away. Find the cracks.{/i}"
    a "{i}Tomorrow... I'll try to be both.{/i}"

    "{i}He stands at the window. Rain streaks the glass. City blurs beyond.{/i}"

    # ---------------------------------------------------
    # EMPATHY-TIER REFLECTION (via tiers)
    # ---------------------------------------------------
    if is_ob_hard:
        a "{i}Obedience is peace. Doubt is decay. Tomorrow I restore order.{/i}"
    elif is_mid:
        a "{i}Order or mercy—one of them has to give. I just hope I choose right.{/i}"
    else:
        a "{i}If Glass can bleed, maybe it can feel. Maybe that’s enough to save something.{/i}"

    "{i}The horizon lightens. Dawn approaches. Sector 10 doesn’t know what’s coming.{/i}"

    a "{i}Time to go.{/i}"
    a "{i}Time to be Glass one more time.{/i}"
    a "{i}But this time... Glass bleeds.{/i}"

    # TRANSITION: Fade to black; rain continues.
    # TEXT OVERLAY: "Dawn. Sector 10."

    $ set_scene_flag(scene_id, "completed")
    return
