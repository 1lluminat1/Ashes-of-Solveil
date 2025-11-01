# ======================================================
# ACT 1 - Scene 11: Aeron's Breaking Point
# File: act1_11_breaking_point.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_11_breaking_point"
$ scene_mark(_current_scene_id, "entered")


label act1_breaking_point:

    # Precompute alignment reads (no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    # empathy side = else

    # VISUAL: Room in deep shadow; single city-light stripe across desk photo.
    # CAMERA: Start on CU of framed photo (Kael), glass catching a cold cyan stripe; rack focus to fingerprints on glass.
    # LIGHTING: One moving city reflection strip; everything else near-black.
    # PROP: Brother photo face-up; mission envelope ajar (red seal catching specular).
    # SFX: Low wind through facade fins; HVAC click every ~10s; distant city thrum.

    "{i}He lifts the photo. Glass cold against his fingertips.{/i}"

    # CAMERA: Tight on Aeron’s thumb smudge; micro hand-tremor (2–3 px bob).
    # FX: Subtle breath-condensation puff when he exhales near the glass.

    a "{i}You always smiled like you belonged.{/i}"
    a "{i}Fifteen. Your Band had three years. Then it turned on you.{/i}"

    "{i}He sets it down. Face-up. Eyes still smiling.{/i}"

    # CAMERA: Photo lands; tilt up to Aeron’s reflection in the glass; hold 1 beat.
    # LIGHTING: City stripe slides off the photo as if time passed.

    a "{i}I used to hate you for leaving me here.{/i}"
    a "{i}Now I think I understand why.{/i}"
    a "{i}You couldn’t live as Glass. You couldn’t be Father’s weapon.{/i}"
    a "{i}You jumped because the cage was worse than falling.{/i}"
    a "{i}Not sadness. Not anger. Just the weight of breathing when there’s no reason left to.{/i}"
    # BLOCKING: Aeron stays half-lit, shoulders rounded; fingers flex once, unclench.

    # ------------------------------------------------------
    # EMPATHY-BASED INTERNAL MONOLOGUE VARIATION
    # ------------------------------------------------------
    # LIGHTING: For OB-hard, keep him darker; mid adds a faint fill; EMP adds a soft rim from the balcony.
    if is_ob_hard:
        a "{i}I don’t know if I’m angry anymore. Just tired.{/i}"
        a "{i}Tired of pretending any of this means something. Tired of wasting efficiency on meaning.{/i}"
        a "{i}Glass doesn’t dream. Glass concludes.{/i}"
    elif is_mid:
        a "{i}I don’t know if I’m angry anymore. Just tired.{/i}"
        a "{i}Tired of pretending any of this means something.{/i}"
        a "{i}Tired of following orders just to keep breathing.{/i}"
    else:
        a "{i}I don’t know if I’m angry anymore. Just tired.{/i}"
        a "{i}Tired of pretending any of this means something.{/i}"
        a "{i}Maybe it could, if I still remembered how to feel.{/i}"
    # ------------------------------------------------------

    "{i}He opens the balcony door. Cold air moves through the room.{/i}"

    # SFX: Door seal hiss; wind rush ramps + fabric flap.
    # FX: Papers lift a centimeter, envelope flutters, then settle.
    "{i}He steps outside.{/i}"

    # CAMERA: Follow at shoulder; slight handheld drift (subtle).
    "{i}The wind hits like a wall. Cold. Relentless. The kind that strips everything bare.{/i}"

    # LIGHTING: Cooler palette; add moving aerial beacons sweeping faintly.

    "{i}Solveil stretches beneath him. Aeries above. Middle grinding between. Unders drowning below.{/i}"

    # CAMERA: Wide establishing — three-tier stack; tiny drone paths as moving specks.
    # FX: Low haze over the Unders; faint heat shimmer on distant stacks.

    a "{i}All that structure. All that order. And none of it leaves room for people like me.{/i}"
    a "{i}People like Kael.{/i}"
    a "{i}Just Glass. Reflecting what they want. Cutting when commanded. Empty always.{/i}"

    # BLOCKING: He leans into wind a degree; coat hem snaps; one foot inches closer to the rail.

    "{i}A drone cuts through the lower air. Searchlight raking the tiers. Hunting. Always hunting.{/i}"

    # LIGHTING: Volumetric cone sweeps across lower city; faint spill kisses balcony edge for a beat.
    # SFX: Far rotor thrum dopplers; scanner ping (very soft).

    a "{i}They’ll keep searching long after I’m gone. The system doesn’t stop. It just replaces.{/i}"
    a "{i}Glass breaks. They’ll make more. They always do.{/i}"

    "{i}His hands find the rail. Metal bites through the cold—sharp, real.{/i}"

    # CAMERA: Insert on knuckles whitening; vein pulse visible.
    # FX: Condensation plume tears sideways in the wind.

    a "{i}This is real. The only real thing left.{/i}"

    "{i}Below, the city breathes. Lights pulse like veins. Distance warps perspective.{/i}"

    # CAMERA: Slow tilt down; parallax exaggeration (shallow DOF).

    a "{i}How far is it? Does it matter?{/i}"
    a "{i}Glass shatters when it falls. Quick. Clean. Final.{/i}"

    # SFX: Wind peak gust; one loose antenna wire sings briefly.

    "{i}His breath comes faster. Shallow. The air won’t fill his lungs.{/i}"

    # FX: Breath plumes shorten; chest rise quickens (2x baseline).
    a "{i}One last smoke...{/i}"

    # PROP: Cigarette + matte-black lighter.

    "{i}His hands shake as he lights it. Smoke climbs into the dark.{/i}"

    # LIGHTING: Warm match pop lights his face for 0.5s; ember becomes tiny moving eye.
    # CAMERA: Profile CU; smoke shears sideways in gust; ash fleck lifts, disappears.

    k "(laughing) You know what’s weird? Up here, I feel like I could actually fly."

    # SFX: Memory VO (Kael) with slight roof-echo IR; -6 dB, low-pass 3.5kHz.

    a "{i}You stood right here. Right here.{/i}"
    a "{i}Did it feel like this? Like the world was holding its breath?{/i}"
    a "{i}Did you hesitate? Or did you just... let go?{/i}"
    a "{i}You couldn’t be Glass. You refused to be Father’s weapon.{/i}"
    a "{i}I became exactly what you warned me not to.{/i}"
    a "{i}And now I understand why you jumped.{/i}"
    a "{i}I wish you’d left a note. Something. Anything but silence.{/i}"

    # CAMERA: Drift toward toes at edge; reveal micro scuff marks on stone.

    "{i}Gravity pulls. Subtle. Patient. It doesn’t demand. It waits.{/i}"

    # FX: Gentle camera down-tilt, 1–2° over two beats to sell pull.

    a "{i}It would be easy. Easier than this.{/i}"
    a "{i}Glass falls. Glass shatters. Glass doesn’t feel it.{/i}"

    # LIGHTING: City strobes blink; balcony remains static, isolating him.

    m "Fate chose differently."

    # SFX: Memory VO (Marcus), dry hall reverb; -4 dB; mono.

    a "{i}Fate. Destiny. Providence. Just prettier words for failure.{/i}"
    a "{i}You said fate. Then you made me Glass.{/i}"
    a "{i}Ten years. 390 operations. Perfect obedience. Perfect emptiness.{/i}"

    l "Glass is breaking. That might be what saves you."

    # SFX: Memory VO (Lyra), intimate proximity; + breath; very light stereo.

    a "{i}She sees it. The cracks spreading.{/i}"
    a "{i}Glass recognizes glass.{/i}"
    a "{i}Maybe she’s right. Maybe breaking is the only way out.{/i}"

    "{i}Inside, the mission waits. Orders. Objectives. Another way to be useful without being whole.{/i}"

    # CAMERA: Over-shoulder back toward room: red seal on envelope glows faint in darkness.

    a "{i}Sweep. Secure. Eliminate. As if purpose and violence are the same thing.{/i}"
    a "{i}Operation 391. Glass completes missions. Glass obeys.{/i}"
    a "{i}Maybe that’s all I am now. A weapon Father points at problems he can’t solve with speeches.{/i}"

    # BLOCKING: His heel lifts, wobbles, then settles back to rail contact.

    "{i}One more step. That’s all it takes.{/i}"

    # CAMERA: Extreme CU on boot edge over the drop; hold 1 beat.

    a "{i}Gravity does the rest.{/i}"

    # FX: Wind lull (duck ambience -5 dB) to create vacuum before choice.

    # ------------------------------------------------------
    # EMPATHY VARIATION – approaching the menu
    # ------------------------------------------------------
    # LIGHTING: OB-hard → balcony darkens slightly; EMP → faint, warmer rim from room interior.
    if is_ob_hard:
        a "{i}Father made me efficient. Ending myself would just be another operation.{/i}"
        a "{i}Quick. Clean. No deviation.{/i}"
    elif is_mid:
        a "{i}I don’t know if I want to die or stop being this thing he made.{/i}"
    else:
        a "{i}Maybe breaking doesn’t mean ending. Maybe it means finally beginning.{/i}"
    # ------------------------------------------------------

    # === MENU: no alignment change; record only ===
    menu:
        "Step forward":
            $ record_choice_once(
                _current_scene_id, "breaking_point_step_forward",
                next_scene_label="act1_11_breaking_point",
                note="Aeron approaches self-destruction; interrupted by knock."
            )
            $ set_scene_flag(scene_id, "step_forward")

            # BLOCKING: Weight shifts forward; center of mass crosses toes.
            # CAMERA: Micro dolly-in (10 cm); vertigo lens breath (very slight).
            a "{i}Just one more step...{/i}"
            a "{i}Glass falls. Glass breaks. Glass—{/i}"

        "Step back":
            $ record_choice_once(
                _current_scene_id, "breaking_point_step_back",
                next_scene_label="act1_11_breaking_point",
                note="Aeron pulls back from the rail; not a recovery, a pause."
            )
            $ set_scene_flag(scene_id, "step_back")

            # BLOCKING: Heel plants; knee unlocks; grip loosens on rail (fingers unclench).
            # CAMERA: Gentle pull-back to chest; breath steadies by 10%.
            a "{i}I can’t keep living like this...{/i}"
            a "{i}But maybe... maybe breaking doesn’t mean falling.{/i}"
            a "{i}Maybe it means shattering the Glass and finding what’s underneath.{/i}"

    "{i}A knock at the door. Sharp. Sudden. Like fate rapping on the walls.{/i}"

    # SFX: Three distinct knocks (wood on metal), 180ms apart; slight room slapback.
    # CAMERA: Whip-pan to door frame silhouette; balcony wind drops 30% momentarily.
    "{i}He drops back to stone. The city noise thins; his heartbeat doesn’t.{/i}"

    # FX: Heartbeat underlay (40 Hz thump), -16 dB, 2 beats then fade.

    a "{i}Who...?{/i}"

    # BLOCKING: Hand leaves rail; other hand wipes at eye line with back of knuckles.
    "{i}His hands won’t stop shaking. He wipes his eyes—just in case.{/i}"

    # CAMERA: CU on glove back crossing lower lid; catch tiny moisture line; cut.

    # ------------------------------------------------------
    # EMPATHY VARIATION – reaction to the knock
    # ------------------------------------------------------
    # LIGHTING: Slight warm spill from interior on his cheek when he turns.
    if is_ob_hard:
        a "{i}Efficiency interrupted. Fate disagrees.{/i}"
        $ set_scene_flag(scene_id, "aeron_accepted_death")
    elif is_mid:
        a "{i}Someone always knocks before the fall.{/i}"
        $ set_scene_flag(scene_id, "aeron_contemplated")
    else:
        a "{i}Maybe that knock was the world reminding me I’m still here.{/i}"
        $ set_scene_flag(scene_id, "aeron_reconsidered")
    # ------------------------------------------------------

    a "{i}Glass doesn’t cry. Glass doesn’t break.{/i}"
    a "{i}Not in front of anyone.{/i}"
    
    # CAMERA: End on profile silhouette; ember dims; wind carries smoke away; hold 1 beat, then cut.

    $ set_scene_flag(scene_id, "completed")
    return


# ========= CANON NOTES =========
# cann.scene_id: act1_11_breaking_point
# cann.when_in_timeline: Night of orders; after Balcony + Bedroom; pre–Sector 10 departure.
# cann.what_happened:
#   - Aeron reaches the rail on the rooftop; contemplates self-destruction.
#   - Kael memory and Marcus/Lyra echoes surface; knock interrupts.
#   - Player records intent (step_forward vs step_back) but outcome is fixed (interruption).
# cann.aeron_state: Alignment tints VO (OB-hard = clinical fatalism; mid = confusion; EMP = glimmer of reframing).
# cann.path_tracking:
#   - Menu is NEUTRAL (no OB/EMP change). Use record_only:
#       • record_choice_once(..., "breaking_point_step_forward") or "..._step_back".
#   - Scene empathy delta: **0**.
#   - Running empathy window BEFORE:  **≈ [-29, +27]**  (after Archive [+/-2] → Debrief [+/-1]).
#   - Running empathy window AFTER:   **≈ [-29, +27]**  (unchanged).
#   - Flags: step_forward / step_back; aeron_accepted_death | aeron_contemplated | aeron_reconsidered; completed.
# cann.thematic_flags: Glass vs Self; efficiency-as-death; gravity as passive system; interruption as grace.
# cann.block_status: ANCHOR (fixed outcome) with VARIANT flavor (alignment-tinged VO + recorded intent).
# cann.true_path_integration: none (menu-free TP rule holds).
# cann.visual_plate_economy:
#   - REUSE: Bedroom + balcony set; single rooftop master with wind pass; close on rail/hand.
#   - HERO: Rail CU with breath plume; cigarette ember in wind; toe-over-edge insert.
# cann.requires_followup:
#   - Next scene routes to the late-night visitor (Lyra or story-selected character).
#   - Use recorded intent to color the first 2–3 lines in that scene (e.g., shakier hands, harsher deflection).
# cann.consistency_asserts:
#   - Aeries altitude weather grammar: wind/condensation; no rain/splash language.
#   - Count integrity: Aeron age 22, 390 ops complete; Kael Band 3 yrs, failed at 15, jumped at 17.