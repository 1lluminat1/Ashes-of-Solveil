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

    "He lifts the photo. Glass cold against his fingertips."

    # CAMERA: Tight on Aeron’s thumb smudge; micro hand-tremor (2–3 px bob).
    # FX: Subtle breath-condensation puff when he exhales near the glass.

    athought "You always smiled like you belonged."
    athought "Fifteen. Your Band had three years. Then it turned on you."

    "He sets it down. Face-up. Eyes still smiling."

    # CAMERA: Photo lands; tilt up to Aeron’s reflection in the glass; hold 1 beat.
    # LIGHTING: City stripe slides off the photo as if time passed.

    athought "I used to hate you for leaving me here."
    athought "Now I think I understand why."
    athought "You couldn’t live as Glass. You couldn’t be Father’s weapon."
    athought "You jumped because the cage was worse than falling."
    athought "Not sadness. Not anger. Just the weight of breathing when there’s no reason left to."
    # BLOCKING: Aeron stays half-lit, shoulders rounded; fingers flex once, unclench.

    # ------------------------------------------------------
    # EMPATHY-BASED INTERNAL MONOLOGUE VARIATION
    # ------------------------------------------------------
    # LIGHTING: For OB-hard, keep him darker; mid adds a faint fill; EMP adds a soft rim from the balcony.
    if is_ob_hard:
        athought "I don’t know if I’m angry anymore. Just tired."
        athought "Tired of pretending any of this means something. Tired of wasting efficiency on meaning."
        athought "Glass doesn’t dream. Glass concludes."
    elif is_mid:
        athought "I don’t know if I’m angry anymore. Just tired."
        athought "Tired of pretending any of this means something."
        athought "Tired of following orders just to keep breathing."
    else:
        athought "I don’t know if I’m angry anymore. Just tired."
        athought "Tired of pretending any of this means something."
        athought "Maybe it could, if I still remembered how to feel."
    # ------------------------------------------------------

    "He opens the balcony door. Cold air moves through the room."

    # SFX: Door seal hiss; wind rush ramps + fabric flap.
    # FX: Papers lift a centimeter, envelope flutters, then settle.
    "He steps outside."

    # CAMERA: Follow at shoulder; slight handheld drift (subtle).
    "The wind hits like a wall. Cold. Relentless. The kind that strips everything bare."

    # LIGHTING: Cooler palette; add moving aerial beacons sweeping faintly.

    "Solveil stretches beneath him. Aeries above. Middle grinding between. Unders drowning below."

    # CAMERA: Wide establishing — three-tier stack; tiny drone paths as moving specks.
    # FX: Low haze over the Unders; faint heat shimmer on distant stacks.

    athought "All that structure. All that order. And none of it leaves room for people like me."
    athought "People like Kael."
    athought "Just Glass. Reflecting what they want. Cutting when commanded. Empty always."

    # BLOCKING: He leans into wind a degree; coat hem snaps; one foot inches closer to the rail.

    "A drone cuts through the lower air. Searchlight raking the tiers. Hunting. Always hunting."

    # LIGHTING: Volumetric cone sweeps across lower city; faint spill kisses balcony edge for a beat.
    # SFX: Far rotor thrum dopplers; scanner ping (very soft).

    athought "They’ll keep searching long after I’m gone. The system doesn’t stop. It just replaces."
    athought "Glass breaks. They’ll make more. They always do."

    "His hands find the rail. Metal bites through the cold—sharp, real."

    # CAMERA: Insert on knuckles whitening; vein pulse visible.
    # FX: Condensation plume tears sideways in the wind.

    athought "This is real. The only real thing left."

    "Below, the city breathes. Lights pulse like veins. Distance warps perspective."

    # CAMERA: Slow tilt down; parallax exaggeration (shallow DOF).

    athought "How far is it? Does it matter?"
    athought "Glass shatters when it falls. Quick. Clean. Final."

    # SFX: Wind peak gust; one loose antenna wire sings briefly.

    "His breath comes faster. Shallow. The air won’t fill his lungs."

    # FX: Breath plumes shorten; chest rise quickens (2x baseline).
    athought "One last smoke..."

    # PROP: Cigarette + matte-black lighter.

    "His hands shake as he lights it. Smoke climbs into the dark."

    # LIGHTING: Warm match pop lights his face for 0.5s; ember becomes tiny moving eye.
    # CAMERA: Profile CU; smoke shears sideways in gust; ash fleck lifts, disappears.

    k "(laughing) You know what’s weird? Up here, I feel like I could actually fly."

    # SFX: Memory VO (Kael) with slight roof-echo IR; -6 dB, low-pass 3.5kHz.

    athought "You stood right here. Right here."
    athought "Did it feel like this? Like the world was holding its breath?"
    athought "Did you hesitate? Or did you just... let go?"
    athought "You couldn’t be Glass. You refused to be Father’s weapon."
    athought "I became exactly what you warned me not to."
    athought "And now I understand why you jumped."
    athought "I wish you’d left a note. Something. Anything but silence."

    # CAMERA: Drift toward toes at edge; reveal micro scuff marks on stone.

    "Gravity pulls. Subtle. Patient. It doesn’t demand. It waits."

    # FX: Gentle camera down-tilt, 1–2° over two beats to sell pull.

    athought "It would be easy. Easier than this."
    athought "Glass falls. Glass shatters. Glass doesn’t feel it."

    # LIGHTING: City strobes blink; balcony remains static, isolating him.

    m "Fate chose differently."

    # SFX: Memory VO (Marcus), dry hall reverb; -4 dB; mono.

    athought "Fate. Destiny. Providence. Just prettier words for failure."
    athought "You said fate. Then you made me Glass."
    athought "Ten years. 390 operations. Perfect obedience. Perfect emptiness."

    l "Glass is breaking. That might be what saves you."

    # SFX: Memory VO (Lyra), intimate proximity; + breath; very light stereo.

    athought "She sees it. The cracks spreading."
    athought "Glass recognizes glass."
    athought "Maybe she’s right. Maybe breaking is the only way out."

    "Inside, the mission waits. Orders. Objectives. Another way to be useful without being whole."

    # CAMERA: Over-shoulder back toward room: red seal on envelope glows faint in darkness.

    athought "Sweep. Secure. Eliminate. As if purpose and violence are the same thing."
    athought "Operation 391. Glass completes missions. Glass obeys."
    athought "Maybe that’s all I am now. A weapon Father points at problems he can’t solve with speeches."

    # BLOCKING: His heel lifts, wobbles, then settles back to rail contact.

    "One more step. That’s all it takes."

    # CAMERA: Extreme CU on boot edge over the drop; hold 1 beat.

    athought "Gravity does the rest."

    # FX: Wind lull (duck ambience -5 dB) to create vacuum before choice.

    # ------------------------------------------------------
    # EMPATHY VARIATION – approaching the menu
    # ------------------------------------------------------
    # LIGHTING: OB-hard → balcony darkens slightly; EMP → faint, warmer rim from room interior.
    if is_ob_hard:
        athought "Father made me efficient. Ending myself would just be another operation."
        athought "Quick. Clean. No deviation."
    elif is_mid:
        athought "I don’t know if I want to die or stop being this thing he made."
    else:
        athought "Maybe breaking doesn’t mean ending. Maybe it means finally beginning."
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
            athought "Just one more step..."
            athought "Glass falls. Glass breaks. Glass—"

        "Step back":
            $ record_choice_once(
                _current_scene_id, "breaking_point_step_back",
                next_scene_label="act1_11_breaking_point",
                note="Aeron pulls back from the rail; not a recovery, a pause."
            )
            $ set_scene_flag(scene_id, "step_back")

            # BLOCKING: Heel plants; knee unlocks; grip loosens on rail (fingers unclench).
            # CAMERA: Gentle pull-back to chest; breath steadies by 10%.
            athought "I can’t keep living like this..."
            athought "But maybe... maybe breaking doesn’t mean falling."
            athought "Maybe it means shattering the Glass and finding what’s underneath."

    "A knock at the door. Sharp. Sudden. Like fate rapping on the walls."

    # SFX: Three distinct knocks (wood on metal), 180ms apart; slight room slapback.
    # CAMERA: Whip-pan to door frame silhouette; balcony wind drops 30% momentarily.
    "He drops back to stone. The city noise thins; his heartbeat doesn’t."

    # FX: Heartbeat underlay (40 Hz thump), -16 dB, 2 beats then fade.

    athought "Who...?"

    # BLOCKING: Hand leaves rail; other hand wipes at eye line with back of knuckles.
    "His hands won’t stop shaking. He wipes his eyes—just in case."

    # CAMERA: CU on glove back crossing lower lid; catch tiny moisture line; cut.

    # ------------------------------------------------------
    # EMPATHY VARIATION – reaction to the knock
    # ------------------------------------------------------
    # LIGHTING: Slight warm spill from interior on his cheek when he turns.
    if is_ob_hard:
        athought "Efficiency interrupted. Fate disagrees."
        $ set_scene_flag(scene_id, "aeron_accepted_death")
    elif is_mid:
        athought "Someone always knocks before the fall."
        $ set_scene_flag(scene_id, "aeron_contemplated")
    else:
        athought "Maybe that knock was the world reminding me I’m still here."
        $ set_scene_flag(scene_id, "aeron_reconsidered")
    # ------------------------------------------------------

    athought "Glass doesn’t cry. Glass doesn’t break."
    athought "Not in front of anyone."
    
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