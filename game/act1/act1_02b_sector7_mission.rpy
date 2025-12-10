# ===================================================
# ACT 1 - Scene 2B: Sector 7 Mission
# File: act1_02b_sector7_mission.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_02b_sector7_mission"
$ scene_mark(_current_scene_id, "entered")

define unit2 = Character("Unit-2", color="#4A90E2")
define unit3 = Character("Unit-3", color="#4A90E2")


label act1_sector7_mission:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: 38mm, eye-level, center-locked; slight vignette. Static plate (no character sprites yet).
    # LIGHTING: Cold white fluorescent, cyan accents, crushed shadows. Hard top-down with strip glints on grating.
    # FX: Subtle volumetric fog near floor grates; steam plumes on loop (low alpha).
    # SFX LOOP: Low mechanical drone; far-city rumble (very subtle).
    # BLOCKING: Industrial corridor. Wet floor seams. Sealed bulk door at end.

    #scene bg_sector7_corridor with fade
    #$ set_loop("sfx/industrial_drone_loop.ogg", -12)
    #play sound "sfx/comm_ping.ogg"

    # VISUAL: Floodlights flare on in sequence (L→R), strobes reflected on wet floor seams.
    athought "Orders arrive as light—white, clean, forgiving."

    pause 0.7

    athought "Order is mercy. Obedience is survival. Precision is grace."

    # ========= COMMS — MARCUS (DIEGETIC) =========
    # SFX: Light radio hiss; notch filter 3–4kHz to sell comms.
    # NOTE: Keep Aeron unseen; we stay in POV/world plates to emphasize ritual.

    m "Containment only. Keep it surgical. The Directorate remembers numbers, not noise."

    pause 0.7

    athought "Three hundred eighty-nine operations. This is 390. Seven years earning the right to exist."

    # ========= DOOR BREACH =========
    # CAMERA: 38mm, head-on with sealed bulk door; red security lamp pulsing.
    # PROP: Magnetic breach charge (small), status LED arming (blink → solid).
    # FX: Quick shadow pass of team shapes sliding past frame; visors dark, faces unseen.

    #play sound "sfx/breach_charge.ogg"
    #TODO: 2 lines below need to be reviewed
    "The breach charge chirps once—Loss of pressure behind the seal, then nothing."

    athought "Door seals behind us. Footfalls count distance—four signatures, no hostiles flagged."

    pause 0.7

    # ========= INTERIOR ROOM — FAMILY =========
    # CAMERA: 38mm, low angle from threshold; rifle geometry occluding frame edge.
    # LIGHTING: Emergency red strips + cold spill. Skin tones desaturated.
    # BLOCKING: Two adults shielding small figure; older teen at rusted panel (warm ember LED).
    # FX: Light dust motes; vapor from broken pipe back-left.

    "The floodlight strips their colors first—skin goes gray, eyes go wide."

    athought "The room learns to hold its breath."

    pause 0.9

    # TEAM RADIO (FILTERED)
    unit3 "{i}Clear path.{/i}"
    unit2 "{i}Panel's hot. Unregistered transmitter.{/i}"
    unit3 "{i}Orders?{/i}"

    athought "Protocol 5. No witnesses."

    # ========= FIRING (SUPPRESSED) =========
    # SFX: "sfx/suppressed_bursts.ogg" (3 short bursts), then brass ticks (very soft).
    # VISUAL: Muzzle flicker light only; do NOT show impacts. Hard cut to aftermath plate.
    # NOTE: Do not glorify. Keep it clinical, fast, ugly in its efficiency.

    athought "The manual says flinching spreads panic."

    # ========= AFTERMATH =========
    # CAMERA: 38mm waist-high; bodies cropped respectfully; shattered photo frame in foreground.
    # SFX: Fluorescent buzz fades back; HVAC whoosh; no reverb spike.
    # SYMBOL: The photo frame = civilian life interrupted. Will callback later.

    athought "Doubt is rot. Worth is proven through service."

    pause 0.8

    # ========= HUD METRICS =========
    # OVERLAY: Flatlines, timer stop, "EFFICIENCY: 99.7%".

    "The overlay blinks confirmation—vitals flatlined, timer stopped, metrics compiled."

    athought "Efficiency rating: 99.7 percent."

    #play sound "sfx/hud_confirm.ogg"
    pause 0.8

    # ========= COMMS — MARCUS PRAISE =========
    m "Flawless work, Aeron. Sector Seven will hold its line tonight."
    m "This is what resolve looks like."

    athought "He calls it resolve. The corridor calls it quiet."

    # VISUAL: Cut back to corridor plate; empty space louder than bodies.
    pause 0.8

    # ========= MICRO-GESTURE — GLOVE =========
    # CAMERA: Macro close-up of right glove removal; latex sheen catches top light.
    # FX: Tiny spec highlights. No blood on glove (important—cleanliness is the horror).

    "The glove peels away with a soft snap—latex gleaming under the fluorescent wash. No blood. Cleaner than the room deserves."

    # ========= FIRST MICRO-GLITCH =========
    # CAMERA: Push 5–8% in on empty corridor; nothing moves. The sound does the work.
    # NOTE: This is the first crack. Keep it small.

    athought "Order is mercy. Obedience is survival. Precision is grace. Doubt is rot. Worth is proven through service."

    pause 0.6

    athought "...Mercy."

    athought "The definition is slipping."

    athought "Doesn't matter—the mission's logged. Three hundred ninety operations. The count continues."

    # ========= PROPAGANDA SCREENS =========
    # VISUAL: Wall screens cold-boot; black → stark white text: "STABILITY IS SALVATION"
    # TYPOGRAPHY: Geometric grotesk caps; pure white on black; flicker in; no logo.

    "Wall screens bloom to life—stark white text on black, humming with conviction."

    pause 0.8

    # TEAM EXIT CALLS (OFF-SCREEN)
    unit2 "{i}Route green.{/i}"
    unit3 "{i}Uploading bodycam. Metrics clean.{/i}"

    # ========= ABSENCE, NOT REMORSE =========
    # CAMERA: Hold on corridor emptiness; team shadows pass and vanish frame-left.
    # NOTE: Aeron still unseen. We feel his presence through stillness.

    athought "No pulse of guilt, no sickness—just breath and static. The city hums the same."

    athought "Three hundred eighty-nine operations before this. Now three hundred ninety. The number used to mean something. Now it's just counting."

    # ========= WALK-OUT =========
    # VISUAL: Door closes on the room; last thing visible is the shattered photo on the floor.
    # SFX: Door hydraulics; lights flicker then stabilize.

    #play sound "sfx/lights_flicker.ogg"

    athought "File the victory, walk the corridor, leave the room as clean as the report."

    # ========= VISOR REFLECTION =========
    # CAMERA: Tight on visor reflection; eyes unreadable, distorted; corridor lines bend across faceplate.
    # SYMBOL: First time we see Aeron—but not really. Just a warped version.

    "The visor gives back a stranger's eyes—distorted, unreadable, bent by corridor geometry."

    athought "Feel nothing. Ask nothing. Do what you're told."

    athought "Order is mercy."

    pause 0.4

    athought "...Is this what mercy looks like?"

    # ========= PLAYER CHOICE — EMP/OB SEED =========
    # NOTE: Small weight, but establishes player instinct for later divergence.

    menu:
        athought "It flickers at the edge of thought—a face, a feeling, unwelcome."

        "Bury it.":
            $ choice_and_dev(_current_scene_id, "_bury_it", "OB", factor=1,
                                next_scene_label="act1_03_morning_routing",
                                note="Buries the memory")

            athought "Weakness spreads like infection. I cut it out."

            # VISUAL: Propaganda screen brightness swells slightly; corridor returns to perfect symmetry.
            pause 0.8

            athought "The mission's logged, the sector's secure—that's all that matters."

        "Let it stay.":
            $ choice_and_dev(_current_scene_id, "_let_it_stay", "EMP", factor=1,
                    next_scene_label="act1_03_morning_routing",
                    note="Lets the memory stay")

            athought "The child's face stays with me—just the eyes. That's all it takes."

            # VISUAL: Screen white cools slightly; a hint of red emergency strip reflects in visor.
            pause 0.8

            athought "The report will be clean. But I won't be."

    # ========= SCENE CLOSE =========
    athought "The mission's complete. The sector's secure. That's all that matters."

    # ========= HOLO-CALL — MARCUS =========
    # VISUAL: Corridor dims 15%; holographic blue bloom builds out of black.
    # SFX: Holocall incoming; soft carrier hiss under dialogue.
    # BLOCKING: Marcus appears as mid-body hologram—crisp, authoritative, cold.

    athought "Incoming request: High Marshal Rylan. Private channel."

    athought "He never uses private channels."

    #scene black with fade
    #show marcus_holo_mid with dissolve

    m "Exemplary work, Aeron. Your metrics were flawless."
    m "Ninety-nine point seven percent efficiency. Seven years of training produces this."
    m "You are becoming precisely what I intended."

    pause 0.4

    m "You complete missions. You don't question. That's what makes you valuable."

    athought "Sharp, obedient, transparent—that's what he wants them to see."

    athought "Is this what you intended, Father? Or just what you'll accept?"

    m "Tomorrow night, you'll attend the Sector 7 Gala."
    m "Directive presence. Show them what Echelon excellence looks like."
    m "Rest now. You've earned it."

    athought "Earned it."

    pause 0.4

    athought "Order is mercy. The words feel automatic—like breathing."

    athought "Tomorrow, the gala. Tonight, the report. There's no rest, just reports, then orders, then more silence."

    # ========= TRANSITION =========
    centered "{i}Morning. The day of the gala.{/i}"

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id:
#   act1_02b_sector7_mission  (Act I — Scene 2B)
# cann.when_in_timeline:
#   Pre-gala anchor mission; immediately precedes Marcus private holo (Act I early).
# cann.what_happened (objective canon summary):
#   - Echelon containment sweep in Sector 7 executed under OP-390 (pre-dawn).
#   - Civilian family neutralized; efficiency recorded at 99.7%.
#   - Marcus praises Aeron over private channel; reinforces his value as an instrument.
#   - First micro-fracture after a perfect mantra run ("...Mercy. The definition is slipping.").
#   - Player choice seeds tone: bury the flicker (OB) vs let it stay (EMP).
# cann.aeron_state:
#   OB-lean read:
#     Operates as ritual machine: clipped cadence, metrics-first, no visible affect; doubt suppressed on cue.
#   EMP-lean read:
#     Same exterior control; brief empathic intrusion (child's eyes) persists post-op if allowed by choice.
# cann.path_tracking:
#   empathy_score_range_so_far:
#     min_emp_possible: -2   # from earlier "Say it anyway" + "Bury it"
#     max_emp_possible:  2   # from earlier "Stay silent" + "Let it stay"
#   notes:
#     - This scene's menu is minor weight (×1) toward path_pressure.
# cann.thematic_flags:
#   motifs_used:
#     - Doctrine Mantras / Reflection / Efficiency Metrics
#   recurring_lines_seeded:
#     - "Order is mercy." / "390 operations." / "99.7% efficiency"
#   continuity_asserts:
#     - 99.7% efficiency must be referenced later by Marcus; OP-390 precedes the gala.
#     - Family photo shard on floor = visual callback opportunity.
# cann.block_status:
#   anchor_or_variant:
#     ANCHOR  # mandatory mission; only flavor differs based on menu choice
#   requires_followup:
#     - act1_03_morning_routing / act1_05_gala later in Act I