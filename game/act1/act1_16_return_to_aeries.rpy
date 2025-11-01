# =======================================================
# ACT 1 - Scene 16: Aeron Returns to the Aeries
# File: act1_16_return_to_aeries.rpy
# =======================================================

#========= SCENE START TASKS =========
$ _current_scene_id = "act1_16_return_to_aeries"
$ scene_mark(_current_scene_id, "entered")


define o1 = Character("Officer 1")
define o2 = Character("Officer 2")

label act1_return_aeries:

    # Quick alignment reads for flavor (no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    # empathy side = else

    # VISUAL: Glass-walled lift shooting up through the city core; floors streak past as bands of light.
    # LIGHTING: Lower Spans sodium → mid-tier industrial neutral → Aeries cold white-blue.
    # SOUND: Elevator mag-rail hum; tension clicks in the car; breath echo subtle in the capsule.
    # CAMERA: Slow push on Aeron’s reflection ghosted over the city; parallax of tiers below.

    "{i}The elevator climbs. Each floor is a layer peeled away.{/i}"
    "{i}Neon fades. White light hardens. The air gets colder.{/i}"

    a "{i}Eight hundred people.{/i}"
    a "{i}Not soldiers. Not rebels. Families.{/i}"
    a "{i}And I'm ordered to kill them in six hours.{/i}"

    # VISUAL: City strata fall away; cloud deck glows faintly below—no precip at this height.
    "{i}The city separates beneath. Clean above, desperate below. The line never blurs.{/i}"

    a "{i}Zira said I have a choice—not whether to obey, but how.{/i}"
    a "{i}'Glass follows orders. Humans find ways to resist even while obeying.'{/i}"
    a "{i}Can I do both? Obey Marcus and save them?{/i}"
    a "{i}Or is that just another lie Glass tells itself?{/i}"

    # VISUAL: Doors iris open; corridor acoustics swallow ambient sound—muffled, pressure-sealed.
    "{i}The doors open. Silence swallows sound. Everything here is controlled.{/i}"

    # SOUND: Damped footfalls; distant HVAC; status chime.
    o1 "Glass."
    o2 "Sir."

    a "{i}They see Glass. Not Aeron. Just the weapon.{/i}"
    a "{i}That's all I've been. All Father made me.{/i}"
    a "{i}Three hundred ninety operations. Tomorrow makes three ninety-one.{/i}"

    # VISUAL: His door ahead; perimeter seam light leaks under it like a sterile halo.
    "{i}My door waits. Light leaks beneath like a trap disguised as home.{/i}"

    # ---------------------------------------------------
    # CHOICE — approach
    # ---------------------------------------------------
    menu:
        "The door waits. Inside, the mission order still glows on his terminal."
        "Enter immediately.":
            $ apply_choice_once(
                _current_scene_id, "a16_enter_immediately", "OB", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Chooses immediate compliance; suppresses hesitation."
            )
            $ set_scene_flag(scene_id, "entered_immediately")
            # CAMERA: Straight-through move; hand smacks panel; door slides fast.
            "{i}He doesn't pause. Hesitation is weakness.{/i}"
            a "{i}Glass doesn't hesitate.{/i}"
            a "{i}...But Glass is cracking.{/i}"

        "Pause at the threshold.":
            $ apply_choice_once(
                _current_scene_id, "a16_pause_threshold", "EMP", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Admits hesitation; allows doubt to surface."
            )
            $ set_scene_flag(scene_id, "paused_at_door")
            # CAMERA: Tight on hovering fingers over panel; shallow focus; breath fogs minutely from colder corridor air.
            "{i}His hand hovers over the panel. For a moment, he can't move.{/i}"
            a "{i}On the other side of this door: obedience, 391.{/i}"
            a "{i}On this side: questions Glass isn't supposed to ask.{/i}"
            "{i}He opens the door.{/i}"

    # VISUAL: Terminal glow washes the room; HUD overlay shows countdown.
    "{i}The terminal blinks: deployment in five hours, forty-seven minutes.{/i}"

    a "{i}Right there. The orders. The coordinates. The lies.{/i}"
    a "{i}'Organized resistance activity.' 'Rebel communication networks.'{/i}"
    a "{i}All lies. Just families trying to survive.{/i}"

    # BLOCKING: Aeron plants both hands on the desk; shoulders square; weight sinks.
    "{i}He braces both hands on the desk. The weight settles.{/i}"

    "{i}Official intel: 200–500 hostile combatants. Threat level: High.{/i}"

    a "{i}Zira's intel: 800 civilians. Families. Children. Unregistered.{/i}"
    a "{i}One of them is lying. And I know which one.{/i}"

    "{i}Official report: 'High-density rebel infrastructure.'{/i}"
    "{i}Reality: a vendor with real coffee; a child missing her father; families keeping warm.{/i}"

    a "{i}I've done this 390 times. How many were lies like this?{/i}"
    a "{i}How many times did I kill families and call it 'neutralizing threats'?{/i}"

    # PROP: Kael's photo at the desk edge; mission envelope ajar; reflection of Aeron in the glass.
    "{i}Kael's photo waits on the desk—still smiling, still whole.{/i}"
    a "{i}'Don't let Father turn you into a weapon,' you said.{/i}"
    a "{i}Too late. I've been a weapon for ten years.{/i}"

    # ---------------------------------------------------
    # CHOICE — Kael's photo
    # ---------------------------------------------------
    menu:
        "Kael's photo sits between the mission order and the edge of the desk."
        "Pick up the photo.":
            $ apply_choice_once(
                _current_scene_id, "a16_pick_up_kael_photo", "EMP", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Acknowledges humanity/memory; re-centers compassion."
            )
            $ set_scene_flag(scene_id, "picked_up_kael_photo")

            # CAMERA: Insert—fingertips on glass; micro-handshake; faint reflection of city haze.
            "{i}He lifts the photo. Glass cold against his fingers.{/i}"
            a "{i}You warned me, Kael. Maybe tomorrow I listen.{/i}"
            a "{i}Try to be human even while being Glass.{/i}"
            a "{i}Find the cracks. Save who I can. Even if it's not enough.{/i}"
            "{i}He sets it down—face-up, still watching.{/i}"
            a "{i}Maybe you didn’t mean 'don't be a weapon,'{/i}"
            a "{i}but 'remember you're human even when they use you as one.'{/i}"

        "Leave it where it is.":
            $ apply_choice_once(
                _current_scene_id, "a16_leave_kael_photo", "OB", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Avoids emotional contact; doubles down on function."
            )
            $ set_scene_flag(scene_id, "left_kael_photo")

            "{i}He doesn't touch it. Can't.{/i}"
            a "{i}I failed you, Kael. Tomorrow I'll fail 800 more.{/i}"
            a "{i}Glass doesn't save people. Glass just cuts.{/i}"

    # WEATHER @ AERIES ALTITUDE: No rain-on-glass—use wind pressure/condensation/haze.
    "{i}High-altitude wind pressures the pane; the frame ticks softly.{/i}"

    # PROP: Gear case on bed; matte black fabric; serialized sidearm; spare mags.
    "{i}The gear waits. Black fabric. Cold metal. Tools of Glass.{/i}"
    a "{i}I could prepare like always. Perfect execution. Perfect obedience.{/i}"

    # ---------------------------------------------------
    # CHOICE — preparation style
    # ---------------------------------------------------
    menu:
        "The tactical gear waits. Dawn approaches."
        "Prepare thoroughly — perfect readiness.":
            $ apply_choice_once(
                _current_scene_id, "a16_prepare_thoroughly", "OB", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Ritual precision; performance-first."
            )
            $ set_scene_flag(scene_id, "prepared_thoroughly")

            # MONTAGE: Disassemble → clean → reassemble; sight check; mag seat; latches snap; all in brisk rhythm.
            "{i}He moves on muscle memory—ritual precision.{/i}"
            "{i}Disassemble. Clean. Reassemble. Check sights. Seat magazines.{/i}"
            a "{i}Glass prepares. Glass doesn't fail.{/i}"
            a "{i}But preparation won't save them. Only choices will.{/i}"

        "Minimal preparation — enough to function.":
            $ apply_choice_once(
                _current_scene_id, "a16_minimal_prep", "EMP", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Deliberate imperfection to leave room for mercy."
            )
            $ set_scene_flag(scene_id, "minimal_prep")
            
            # VISUAL: One mag loaded; others left in case; holster buckles left a notch loose.
            "{i}He checks his sidearm. Loads one magazine. Leaves the rest.{/i}"
            a "{i}I don't need perfection tomorrow. I need humanity.{/i}"
            a "{i}Maybe imperfection is the crack I need.{/i}"

    # UI: Countdown overlay ticks—04:12 → 04:11 …
    "{i}Countdown: four hours, twelve minutes.{/i}"

    a "{i}Lyra said Glass is breaking—that it might save me.{/i}"
    a "{i}Zira said show her I'm human, not Glass.{/i}"
    a "{i}Kael said don't let Father turn me into a weapon.{/i}"
    a "{i}But I am a weapon. Can I be both? Glass and whole?{/i}"

    # VISUAL: Sit edge of bed; elbows on knees; micro hand tremor; breath measured.
    "{i}He sits on the bed; the weight settles. Hands tremble—just slightly.{/i}"

    a "{i}Tomorrow I kill eight hundred people. Or try to save them.{/i}"
    a "{i}Maybe I kill six hundred and save two hundred. Less horror, not victory.{/i}"
    a "{i}Maybe that's all Glass can do—find cracks and save fragments.{/i}"

    a "{i}Zira said trying matters, even if it’s not enough.{/i}"
    a "{i}Trying makes me human. Obeying perfectly keeps me Glass.{/i}"

    # LIGHTING: Far-below storm glow blooms within the cloud deck; silent lightning; no rain at altitude.
    "{i}Lightning blooms inside the cloud layer below; the frame ticks again under wind pressure.{/i}"

    a "{i}I can’t refuse the mission. Marcus owns me. The system owns me.{/i}"
    a "{i}But I can choose how I obey.{/i}"
    a "{i}Warn people. Fake reports. Look away. Find the cracks.{/i}"
    a "{i}Tomorrow... I'll try to be both.{/i}"

    # VISUAL: Window silhouette; condensation halo at the edge; city smeared by haze.
    "{i}He stands at the window. Condensation veils the glass. The city blurs beyond.{/i}"

    # ---------------------------------------------------
    # EMPATHY-TIER REFLECTION (via tiers)
    # ---------------------------------------------------
    if is_ob_hard:
        a "{i}Obedience is peace. Doubt is decay. Tomorrow I restore order.{/i}"
    elif is_mid:
        a "{i}Order or mercy—one of them has to give. I just hope I choose right.{/i}"
    else:
        a "{i}If Glass can bleed, maybe it can feel. Maybe that’s enough to save something.{/i}"

    # VISUAL: Horizon lightens—thin band above cloud tops; instruments ping; the city holds its breath.
    "{i}The horizon lightens. Dawn approaches. Sector Ten doesn’t know what’s coming.{/i}"

    a "{i}Time to go.{/i}"
    a "{i}Time to be Glass one more time.{/i}"
    a "{i}But this time... Glass bleeds.{/i}"

    # TRANSITION: Fade to black; hold on HUD countdown dip → 03:59.
    $ set_scene_flag(scene_id, "completed")
    return

# ========= CANON NOTES =========
# cann.scene_id: act1_16_return_to_aeries
# cann.when_in_timeline: Pre-dawn, hours before Sector 10 purge; immediately after Zira first contact.
# cann.what_happened:
# - Aeron returns to the Aeries; re-reads orders; weighs Zira’s intel vs Command.
# - Three scored choices: threshold hesitation, Kael photo, prep style (each ±1).
# - Commits internally to “choose how to obey” while acknowledging ownership by Marcus/system.
# cann.aeron_state: OB-hard = brisk compliance voice; mid = torn; EMP = receptive to mercy tactics.
# cann.path_tracking:
# - Menu weights: Threshold OB/EMP(+1), Photo OB/EMP(+1), Prep OB/EMP(+1).
# - Scene empathy delta range: −3 → +3.
# - Running window BEFORE:   ≈ [-33, +34]
# - Running window AFTER:     ≈ [-36, +37]
# - Flags: entered_immediately / paused_at_door; picked_up_kael_photo / left_kael_photo;
# prepared_thoroughly / minimal_prep; completed.
# cann.thematic_flags: Ownership vs agency; ritual preparation as ideology; “choose how to obey.”
# cann.block_status: VARIANT (three binary micro-branches); no outcome lock yet.
# cann.true_path_integration: none (TP untouched).
# cann.visual_plate_economy:
# - REUSE: Aeries corridor + apartment master; HUD countdown overlay; window silhouette plate.
# - HERO: Threshold hover CU; photo-in-hand insert; gear ritual montage; cloud-deck lightning below.
# cann.requires_followup:
# - If minimal_prep or pause_threshold → unlock softer phrasing in Sector 10 setup (warn/evac options).
# - If prepared_thoroughly + left_kael_photo → colder VO in initial sweep beats; earlier OB echoes.
# cann.consistency_asserts:
# - Aeries altitude grammar: wind/condensation/haze only—no rain-on-glass FX.
# - Doctrine language (latency/tolerance) remains verbatim across scenes.
# - Count integrity: Operation 391 timing preserved; 390 prior ops referenced accurately.