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

    "The elevator climbs. Each floor is a layer peeled away."
    "Neon fades. White light hardens. The air gets colder."

    athought "Eight hundred people."
    athought "Not soldiers. Not rebels. Families."
    athought "And I'm ordered to kill them in six hours."

    # VISUAL: City strata fall away; cloud deck glows faintly below—no precip at this height.
    "The city separates beneath. Clean above, desperate below. The line never blurs."

    athought "Zira said I have a choice—not whether to obey, but how."
    athought "'Glass follows orders. Humans find ways to resist even while obeying.'"
    athought "Can I do both? Obey Marcus and save them?"
    athought "Or is that just another lie Glass tells itself?"

    # VISUAL: Doors iris open; corridor acoustics swallow ambient sound—muffled, pressure-sealed.
    "The doors open. Silence swallows sound. Everything here is controlled."

    # SOUND: Damped footfalls; distant HVAC; status chime.
    o1 "Glass."
    o2 "Sir."

    athought "They see Glass. Not Aeron. Just the weapon."
    athought "That's all I've been. All Father made me."
    athought "Three hundred ninety operations. Tomorrow makes three ninety-one."

    # VISUAL: His door ahead; perimeter seam light leaks under it like a sterile halo.
    "My door waits. Light leaks beneath like a trap disguised as home."

    # ---------------------------------------------------
    # CHOICE — approach
    # ---------------------------------------------------
    menu:
        "The door waits. Inside, the mission order still glows on his terminal."
        "Enter immediately.":
            $ choice_and_dev(
                _current_scene_id, "a16_enter_immediately", "OB", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Chooses immediate compliance; suppresses hesitation."
            )
            $ set_scene_flag(scene_id, "entered_immediately")

            # CAMERA: Straight-through move; hand smacks panel; door slides fast.
            "He doesn't pause. Hesitation is weakness."

            athought "Glass doesn't hesitate."
            athought "...But Glass is cracking."

        "Pause at the threshold.":
            $ choice_and_dev(
                _current_scene_id, "a16_pause_threshold", "EMP", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Admits hesitation; allows doubt to surface."
            )
            $ set_scene_flag(scene_id, "paused_at_door")

            # CAMERA: Tight on hovering fingers over panel; shallow focus; breath fogs minutely from colder corridor air.
            "His hand hovers over the panel. For a moment, he can't move."

            athought "On the other side of this door: obedience, 391."
            athought "On this side: questions Glass isn't supposed to ask."

            "He opens the door."

    # VISUAL: Terminal glow washes the room; HUD overlay shows countdown.
    "The terminal blinks: deployment in five hours, forty-seven minutes."

    athought "Right there. The orders. The coordinates. The lies."
    athought "'Organized resistance activity.' 'Rebel communication networks.'"
    athought "All lies. Just families trying to survive."

    # BLOCKING: Aeron plants both hands on the desk; shoulders square; weight sinks.
    "He braces both hands on the desk. The weight settles."

    "Official intel: 200–500 hostile combatants. Threat level: High."

    athought "Zira's intel: 800 civilians. Families. Children. Unregistered."
    athought "One of them is lying. And I know which one."

    "Official report: 'High-density rebel infrastructure.'"
    "Reality: a vendor with real coffee; a child missing her father; families keeping warm."

    athought "I've done this 390 times. How many were lies like this?"
    athought "How many times did I kill families and call it 'neutralizing threats'?"

    # PROP: Kael's photo at the desk edge; mission envelope ajar; reflection of Aeron in the glass.
    "Kael's photo waits on the desk—still smiling, still whole."

    athought "'Don't let Father turn you into a weapon,' you said."
    athought "Too late. I've been a weapon for ten years."

    # ---------------------------------------------------
    # CHOICE — Kael's photo
    # ---------------------------------------------------
    menu:
        "Kael's photo sits between the mission order and the edge of the desk."
        "Pick up the photo.":
            $ choice_and_dev(
                _current_scene_id, "a16_pick_up_kael_photo", "EMP", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Acknowledges humanity/memory; re-centers compassion."
            )
            $ set_scene_flag(scene_id, "picked_up_kael_photo")

            # CAMERA: Insert—fingertips on glass; micro-handshake; faint reflection of city haze.
            "He lifts the photo. Glass cold against his fingers."

            athought "You warned me, Kael. Maybe tomorrow I listen."
            athought "Try to be human even while being Glass."
            athought "Find the cracks. Save who I can. Even if it's not enough."

            "He sets it down—face-up, still watching."

            athought "Maybe you didn’t mean 'don't be a weapon,'"
            athought "but 'remember you're human even when they use you as one.'"

        "Leave it where it is.":
            $ choice_and_dev(
                _current_scene_id, "a16_leave_kael_photo", "OB", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Avoids emotional contact; doubles down on function."
            )
            $ set_scene_flag(scene_id, "left_kael_photo")

            "He doesn't touch it. Can't."

            athought "I failed you, Kael. Tomorrow I'll fail 800 more."
            athought "Glass doesn't save people. Glass just cuts."

    # WEATHER @ AERIES ALTITUDE: No rain-on-glass—use wind pressure/condensation/haze.
    "High-altitude wind pressures the pane; the frame ticks softly."

    # PROP: Gear case on bed; matte black fabric; serialized sidearm; spare mags.
    "The gear waits. Black fabric. Cold metal. Tools of Glass."

    athought "I could prepare like always. Perfect execution. Perfect obedience."

    # ---------------------------------------------------
    # CHOICE — preparation style
    # ---------------------------------------------------
    menu:
        "The tactical gear waits. Dawn approaches."
        "Prepare thoroughly — perfect readiness.":
            $ choice_and_dev(
                _current_scene_id, "a16_prepare_thoroughly", "OB", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Ritual precision; performance-first."
            )
            $ set_scene_flag(scene_id, "prepared_thoroughly")

            # MONTAGE: Disassemble → clean → reassemble; sight check; mag seat; latches snap; all in brisk rhythm.
            "He moves on muscle memory—ritual precision."
            "Disassemble. Clean. Reassemble. Check sights. Seat magazines."

            athought "Glass prepares. Glass doesn't fail."
            athought "But preparation won't save them. Only choices will."

        "Minimal preparation — enough to function.":
            $ choice_and_dev(
                _current_scene_id, "a16_minimal_prep", "EMP", factor=1,
                next_scene_label="act1_16_return_to_aeries",
                note="Deliberate imperfection to leave room for mercy."
            )
            $ set_scene_flag(scene_id, "minimal_prep")
            
            # VISUAL: One mag loaded; others left in case; holster buckles left a notch loose.
            "He checks his sidearm. Loads one magazine. Leaves the rest."

            athought "I don't need perfection tomorrow. I need humanity."
            athought "Maybe imperfection is the crack I need."

    # UI: Countdown overlay ticks—04:12 → 04:11 …
    "Countdown: four hours, twelve minutes."

    athought "Lyra said Glass is breaking—that it might save me."
    athought "Zira said show her I'm human, not Glass."
    athought "Kael said don't let Father turn me into a weapon."
    athought "But I am a weapon. Can I be both? Glass and whole?"

    # VISUAL: Sit edge of bed; elbows on knees; micro hand tremor; breath measured.
    "He sits on the bed; the weight settles. Hands tremble—just slightly."

    athought "Tomorrow I kill eight hundred people. Or try to save them."
    athought "Maybe I kill six hundred and save two hundred. Less horror, not victory."
    athought "Maybe that's all Glass can do—find cracks and save fragments."

    athought "Zira said trying matters, even if it’s not enough."
    athought "Trying makes me human. Obeying perfectly keeps me Glass."

    # LIGHTING: Far-below storm glow blooms within the cloud deck; silent lightning; no rain at altitude.
    "Lightning blooms inside the cloud layer below; the frame ticks again under wind pressure."

    athought "I can’t refuse the mission. Marcus owns me. The system owns me."
    athought "But I can choose how I obey."
    athought "Warn people. Fake reports. Look away. Find the cracks."
    athought "Tomorrow... I'll try to be both."

    # VISUAL: Window silhouette; condensation halo at the edge; city smeared by haze.
    "He stands at the window. Condensation veils the glass. The city blurs beyond."

    # ---------------------------------------------------
    # EMPATHY-TIER REFLECTION (via tiers)
    # ---------------------------------------------------
    if is_ob_hard:
        athought "Obedience is peace. Doubt is decay. Tomorrow I restore order."
    elif is_mid:
        athought "Order or mercy—one of them has to give. I just hope I choose right."
    else:
        athought "If Glass can bleed, maybe it can feel. Maybe that’s enough to save something."

    # VISUAL: Horizon lightens—thin band above cloud tops; instruments ping; the city holds its breath.
    "The horizon lightens. Dawn approaches. Sector Ten doesn’t know what’s coming."

    athought "Time to go."
    athought "Time to be Glass one more time."
    athought "But this time... Glass bleeds."

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