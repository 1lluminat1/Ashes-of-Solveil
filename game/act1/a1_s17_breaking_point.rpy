# ======================================================
# ACT 1 - Scene 11: Aeron's Breaking Point
# File: a1_s17_breaking_point.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a1_s17_breaking_point"
$ scene_mark(_current_scene_id, "entered")


label a1_s17_breaking_point:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Start on CU of framed photo (Kael); rack focus to fingerprints; later follow to balcony.
    # LIGHTING: One moving city reflection strip; everything else near-black. Cooler palette on balcony.
    # SFX LOOP: Low wind through facade fins; HVAC click every ~10s; distant city thrum.
    # SFX ONE-SHOTS: Door seal hiss; wind rush; fabric flap; scanner ping (soft).
    # PROP: Brother photo face-up; mission envelope ajar (red seal catching specular); cigarette + lighter.
    # FX/COMP: Breath-condensation puff; moving aerial beacons; low haze over the Unders.
    # BLOCKING: Room in deep shadow; single city-light stripe across desk photo.

    #scene bg_bedroom_night with fade

    # ========= OPENING — THE PHOTO =========
    # VISUAL: Tight on Aeron's thumb smudge on the photo glass; micro hand-tremor.

    "Cold glass against his fingertips. The frame is heavy, smudged with the ghosts of a hundred other nights like this."
    athought "You always smiled like you belonged."

    athought "Fifteen. Your Band had three years. Then it turned on you."

    "The frame clacks against the desk. Kael smiles up at the ceiling, frozen in a year that never ended."

    # VISUAL: Photo lands; tilt up to Aeron's reflection; city stripe slides off as if time passed.

    athought "I used to hate you for leaving me here."

    athought "Now I think I understand why."

    # ========= EMPATHY VARIATION — INTERNAL MONOLOGUE =========
    # LIGHTING: OB-hard keeps him darker; mid adds faint fill; EMP adds soft rim from balcony.

    if pass_tier("OB3", "OB2"):
        athought "I don't know if I'm angry anymore. Just tired."
        athought "Tired of pretending any of this means something."
        athought "Weapons don't dream."
    elif pass_tier("OB1", "NEU"):
        athought "I don't know if I'm angry anymore. Just tired."
        athought "Tired of pretending any of this means something."
    else:
        athought "I don't know if I'm angry anymore. Just tired."
        athought "Tired of pretending any of this means something."

    # ========= THE BALCONY =========

    # VISUAL: Follow at shoulder; slight handheld drift.

    "The door seal breaks with a hiss. Cold air moves through the room like something alive."

    # SFX: Wind rush ramps + fabric flap.
    # FX: Papers lift a centimeter.

    "One step across the threshold, and the room vanishes."

    "The balcony swallows him whole—leaving nothing but cold glass beneath his boots and the endless void beyond."

    "The wind hits like a wall—cold, relentless, the kind that strips everything bare."

    "Below, the city is a grid of light that refuses to blink. Aeries, The Spans, Unders—locked in a perfect, suffocating stack."

    athought "All that structure. All that order."
    athought "No room."

    # VISUAL: He leans into wind a degree; coat hem snaps; one foot inches closer to the rail.

    "A drone cuts through the lower air—searchlight raking the tiers. Always hunting."

    # LIGHTING: Volumetric cone sweeps across lower city; faint spill kisses balcony edge for a beat.

    athought "They'll keep searching long after I'm gone. The system doesn't stop. It just replaces."

    # ========= THE RAIL =========
    # VISUAL: Insert on knuckles whitening; vein pulse visible; condensation plume tears sideways.

    "His hands find the rail. Metal bites through the cold—sharp, real."

    athought "This is real. The only real thing left."

    "Below, the city breathes. Lights pulse like veins. Distance warps perspective."

    # CAMERA: Slow tilt down; parallax exaggeration (shallow DOF).

    athought "How far is it? Does it matter?"

    athought "Quick. Clean. Final."

    # SFX: Wind peak gust; one loose antenna wire sings briefly.

    "His breath comes faster—shallow, the air refusing to fill his lungs."

    # FX: Breath plumes shorten; chest rise quickens.

    athought "One last smoke..."

    # VISUAL: Profile CU; smoke shears sideways in gust; ash fleck lifts, disappears.

    "His hands shake as he lights it. Smoke climbs into the dark."

    athought "Kael's brand. Stale smoke to mask the cold."

    # ========= KAEL'S VOICE =========
    # SFX: Memory VO (Kael) with slight roof-echo; -6 dB, low-pass 3.5kHz.

    k "(laughing) You know what's weird? Up here, I feel like I could actually fly."

    athought "You stood right here. Right here."

    athought "Did it feel like this? Like the world was holding its breath?"

    athought "Did you hesitate? Or did you just... let go?"

    athought "You refused to be Father's weapon."

    athought "I became exactly what you warned me not to."

    # ========= THE PULL =========
    # VISUAL: Drift toward toes at edge; reveal micro scuff marks on stone.

    "Gravity pulls—subtle, patient. It doesn't demand. It waits."

    # FX: Gentle camera down-tilt, 1–2° over two beats.

    athought "It would be easy. Easier than this."

    athought "Fall. Shatter. Stop feeling it."

    # ========= MARCUS'S VOICE =========
    # SFX: Memory VO (Marcus), dry hall reverb; -4 dB; mono.

    m "Fate chose differently."

    athought "Fate. Destiny. Providence. Just prettier words for failure."

    athought "You said fate. Then you made me into this."

    athought "Ten years. 390 operations. Perfect obedience. Perfect emptiness."

    # ========= LYRA'S VOICE =========
    # SFX: Memory VO (Lyra), intimate proximity; + breath; very light stereo.

    l "Something in you is breaking. That might be what saves you."

    athought "She sees it."

    # ========= THE MISSION =========
    # VISUAL: Over-shoulder back toward room: red seal on envelope glows faint in darkness.

    "Inside, the mission waits. More orders, more expectations. Another way to be useful without being whole."

    athought "Sweep. Secure. Eliminate. As if purpose and violence are the same thing."

    athought "Operation 391. Weapons complete missions. Weapons obey."

    athought "Maybe that's all I am now. Something Father points at problems he can't solve with speeches."

    # ========= THE EDGE =========
    # VISUAL: His heel lifts, wobbles, then settles back to rail contact.

    "One more step. That's all it takes."

    # CAMERA: Extreme CU on boot edge over the drop; hold 1 beat.

    athought "Gravity does the rest."

    # FX: Wind lull (duck ambience -5 dB) to create vacuum before choice.

    # ========= EMPATHY VARIATION — APPROACHING THE MENU =========
    # LIGHTING: OB-hard → balcony darkens slightly; EMP → faint warmer rim from room interior.

    if pass_tier("OB3", "OB2"):
        athought "Father made me efficient. Ending myself would just be another operation."
        athought "Quick, clean, no deviation."
    elif pass_tier("OB1", "NEU"):
        athought "I don't know if I want to die, or just stop being this thing he made."
    else:
        athought "Maybe breaking doesn't mean ending. Maybe it means finally beginning."

    # ========= PLAYER CHOICE — EMERGENCE MENU =========
    # The third option ("Sit down at the rail") fades in after 12 seconds
    # of the player not clicking either standard option.
    call screen emergence_menu(
        option_a="Step forward.",
        option_b="Step back.",
        option_c="Sit down at the rail.",
        wait_seconds=12.0,
        prompt="The rail is cold under his hands. The city hums below."
    )
    $ _bp_choice = _return

    if _bp_choice == "a":
        # === "Step forward" branch ===
        $ record_choice_once(
            _current_scene_id, "breaking_point_step_forward",
            note="Aeron approaches self-destruction; interrupted by knock."
        )
        $ scene_mark(_current_scene_id, "step_forward")

        # BLOCKING: Weight shifts forward; center of mass crosses toes.
        # CAMERA: Micro dolly-in; vertigo lens breath (subtle).

        athought "Just one more step..."

    elif _bp_choice == "b":
        # === "Step back" branch ===
        $ record_choice_once(
            _current_scene_id, "breaking_point_step_back",
            note="Aeron pulls back from the rail; not a recovery, a pause."
        )
        $ scene_mark(_current_scene_id, "step_back")

        # BLOCKING: Heel plants; knee unlocks; grip loosens on rail.
        # CAMERA: Gentle pull-back to chest; breath steadies.

        athought "I can't keep living like this..."

        athought "But not like that."

    elif _bp_choice == "c":
        # === NEW: Emergence — "Sit down at the rail" ===
        $ tp_emergence_found(_current_scene_id)
        $ scene_mark(_current_scene_id, "sat_at_rail")
        $ record_choice_once(_current_scene_id, "_sat_at_rail",
            note="Player found the Emergence option. Neither forward nor back. Present.")

        athought "I don't step forward. I don't step back."
        athought "I sit."

        "The concrete is cold through his coat. The rail presses against his shoulder blade."
        "Wind finds him here too — but lower, less demanding."

        athought "I don't know what I want."
        athought "I just know I can't decide right now."

        "The city breathes below. He breathes with it."
        "Not performing survival. Not performing despair."
        "Just breathing."

        pause 1.2

        athought "Kael stood here. Kael chose."
        athought "Right now, nobody is choosing."

    # ========= THE KNOCK =========
    # SFX: Three distinct knocks (wood on metal), 180ms apart; slight room slapback.
    # CAMERA: Whip-pan to door frame silhouette; balcony wind drops 30% momentarily.

    "A knock at the door—sharp, sudden, like fate rapping on the walls."

    "His weight shifts back. Heels find the concrete. The rail releases him — or he releases the rail. The distinction feels important."
    # FX: Heartbeat underlay (40 Hz thump), -16 dB, 2 beats then fade.

    athought "Who...?"

    # BLOCKING: Hand leaves rail; other hand wipes at eye line with back of knuckles.

    "His hands won't stop shaking. He wipes his eyes—just in case."

    # VISUAL: CU on glove back crossing lower lid; catch tiny moisture line; cut.

    # ========= EMPATHY VARIATION — REACTION TO KNOCK =========
    # LIGHTING: Slight warm spill from interior on his cheek when he turns.

    if pass_tier("OB3", "OB2"):
        athought "Efficiency interrupted. Fate disagrees."
        $ scene_mark(_current_scene_id, "aeron_accepted_death")
    elif pass_tier("OB1", "NEU"):
        athought "Someone always knocks before the fall."
        $ scene_mark(_current_scene_id, "aeron_contemplated")
    else:
        athought "Maybe that knock was the world reminding me I'm still here."
        $ scene_mark(_current_scene_id, "aeron_reconsidered")

    # ========= CLOSING =========

    athought "Not now."

    # CAMERA: End on profile silhouette; ember dims; wind carries smoke away; hold 1 beat, then cut.

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a1_s17_breaking_point
# cann.when_in_timeline: Night of orders; after Balcony + Bedroom; pre–Sector 10 departure.
# cann.what_happened:
#   - Aeron reaches the rail on the rooftop; contemplates self-destruction.
#   - Kael memory and Marcus/Lyra echoes surface; knock interrupts.
#   - Player records intent (step_forward vs step_back) but outcome is fixed (interruption).
# cann.aeron_state: Alignment tints VO (OB-hard = clinical fatalism; mid = confusion; EMP = glimmer of reframing).
# cann.path_tracking:
#   - Menu is NEUTRAL (no OB/EMP change). Record only.
#   - Scene empathy delta: 0.
#   - Flags: step_forward / step_back; aeron_accepted_death | aeron_contemplated | aeron_reconsidered; completed.
# cann.thematic_flags: Self vs Weapon; efficiency-as-death; gravity as passive system; interruption as grace.
# cann.block_status: ANCHOR (fixed outcome) with VARIANT flavor (alignment-tinged VO + recorded intent).
# cann.visual_plate_economy:
#   - REUSE: Bedroom + balcony set; single rooftop master with wind pass.
#   - HERO: Rail CU with breath plume; cigarette ember in wind; toe-over-edge insert.
# cann.requires_followup:
#   - Next scene routes to the late-night visitor (Lyra).
#   - Use recorded intent to color the first 2–3 lines in that scene.
