# ===================================================
# ACT 1 - Scene 2B: Sector 7 Mission (OB cadence)
# ===================================================

define unit2 = Character("Unit-2", color="#4A90E2")
define unit3 = Character("Unit-3", color="#4A90E2")

label act1_sector7_mission:

    $ _current_scene_id = "act1_02b_sector7_mission"
    $ scene_mark(_current_scene_id, "entered")

    # SCENE SETUP — MID LEVELS, SECTOR 7
    # CAMERA: 38mm, eye-level, center-locked; slight vignette. Static plate (no character sprites).
    # COLOR: Cold white (fluoro), cyan accents, crushed shadows.
    # FX: Subtle volumetric fog cards near floor grates; steam plumes on loop (low alpha).
    # SFX LOOP: low mechanical drone; far-city rumble (very subtle).
    # TIP: Author one hero BG plate + 2 close variants (door, interior room) for cut-ins.

    #scene bg_sector7_corridor with fade
    #$ set_loop("sfx/industrial_drone_loop.ogg", -12)  # (custom helper if you use one)
    #play sound "sfx/comm_ping.ogg"

    a "{i}Orders arrive as light. White. Clean. Forgiving.{/i}"
    # VISUAL: Floodlights flare on in sequence (L→R), strobes reflected on wet floor seams.
    # LIGHT: Hard top-down fluoro; add strip glints on grating.
    pause 0.7

    a "{i}Order is mercy.{/i}"  # mantra 1
    # ON-SCREEN TEXT (tiny, bottom-right): “DOCTRINE OF WORTH: MANTRA 1” (diegetic HUD feel)
    pause 0.8

    # COMMS — MARCUS (DIEGETIC) — off-screen radio
    # SFX: light radio hiss; notch filter 3–4kHz to sell comms.
    m "Containment only. Keep it surgical. The Directorate remembers numbers, not noise."
    pause 0.6

    a "{i}Obedience is survival.{/i}"  # mantra 2
    # NOTE: Keep Aeron unseen; we stay in POV/world plates to emphasize ritual.
    pause 0.7

    a "{i}Three-hundred eighty-nine operations. This is 390.{/i}"
    # UI OVERLAY: Minimal HUD card “Stabilization Sweep / S7-Δ / OP-390” (white on 20% black).
    pause 0.7

    a "{i}Seven years earning the right to exist.{/i}"
    pause 0.8

    # DOOR BREACH BLOCK
    # CAMERA: 38mm, head-on with sealed bulk door; red security lamp pulsing.
    # PROP: Magnetic breach charge (small), status LED arming (blink → solid).
    #play sound "sfx/breach_charge.ogg"  # brief arming chirp

    a "{i}Door seals behind us. Footfalls count distance. Four signatures. No hostiles flagged.{/i}"
    # FX: quick shadow pass of team shapes sliding past frame; keep faces unseen; visors dark.
    pause 0.7

    a "{i}Precision is grace.{/i}"  # mantra 3
    # NOTE: Use this beat to punch the sterile geometry; perfect symmetry shot sells “order”.
    pause 0.7

    # INTERIOR ROOM — FAMILY
    # CAMERA: 38mm, low angle from threshold; rifle-sight/occluding geometry at frame edge.
    # LIGHT: Emergency red strips + cold spill → skin tones desaturated.
    # BLOCKING: Two adults shielding small figure; older teen at rusted panel (warm ember LED).
    a "{i}White steals their colors first. The room learns to hold its breath.{/i}"
    # FX: light dust motes; a hovering vapor from broken pipe back-left.
    pause 0.9

    # TEAM RADIO (FILTERED), KEEP OFF-SCREEN
    unit3 "{i}Clear path.{/i}"
    pause 0.5
    unit2 "{i}Panel's hot. Unregistered transmitter.{/i}"
    pause 0.5
    unit3 "{i}Orders?{/i}"
    pause 0.6

    # FIRING (SUPPRESSED) — DO NOT GLORIFY
    # SFX: "sfx/suppressed_bursts.ogg" (3 short bursts), then brass ticks (very soft).
    # VISUAL: Muzzle flicker light only; do not show impacts; hard cut to aftermath plate.
    a "{i}The manual says flinching spreads panic.{/i}"
    pause 0.7

    # AFTERMATH PLATE
    # CAMERA: 38mm waist-high; bodies cropped respectfully; shattered photo frame foreground.
    # SFX: Fluoro buzz fades back; HVAC whoosh; no reverb spike.
    a "{i}Doubt is rot.{/i}"  # mantra 4
    pause 0.8

    # HUD METRICS
    # OVERLAY: flatlines, timer stop, “EFFICIENCY: 99.7%”.
    a "{i}Vitals checked. Zero resistance. Logs compiled. Efficiency rating: 99.7 percent.{/i}"
    #play sound "sfx/hud_confirm.ogg"  # soft, clean, one blip
    pause 0.8

    # COMMS — PRAISE
    m "Flawless work, Aeron. Sector Seven will hold its line tonight."
    pause 0.5
    m "This is what resolve looks like."
    pause 0.8

    a "{i}Worth is proven through service.{/i}"  # mantra 5
    pause 0.6
    a "{i}He calls it resolve. The corridor calls it quiet.{/i}"
    # VISUAL: Cut back to corridor plate; empty space louder than bodies.
    pause 0.8

    # MICRO-GESTURE — GLOVE
    # CAMERA: Macro close-up of right glove removal; latex sheen catches top light.
    # FX: Tiny spec highlights; no blood on glove (important).
    a "{i}I peel the glove. No blood. Cleaner than the room deserves.{/i}"
    pause 0.8
    a "{i}The latex gleams under the light.{/i}"
    pause 0.8

    # MANTRA STRING — PERFECT DELIVERY
    # CAMERA: Back to center-locked corridor; static. This should feel like drills.
    a "{i}Order is mercy.{/i}"
    pause 0.5
    a "{i}Obedience is survival.{/i}"
    pause 0.5
    a "{i}Precision is grace.{/i}"
    pause 0.5
    a "{i}Doubt is rot.{/i}"
    pause 0.5
    a "{i}Worth is proven through service.{/i}"
    pause 0.8

    # FIRST MICRO-GLITCH (AFTER the clean mantras)
    # CAMERA: Push 5–8% in on empty corridor; nothing moves; the sound does the work.
    a "{i}...Mercy.{/i}"
    pause 0.9
    a "{i}Who taught me that word?{/i}"
    pause 1.0

    a "{i}Doesn't matter. The mission's logged.{/i}"
    pause 0.6
    a "{i}Three-hundred ninety operations. The count continues.{/i}"
    pause 0.8

    # PROPAGANDA SCREENS
    # VISUAL: Wall screens cold-boot; black → stark white text: “STABILITY IS SALVATION”
    # TYPO: geometric grotesk caps; pure white on black; flicker in; no logo.
    "{i}Anthems bloom across the wall: STABILITY IS SALVATION. White letters pretending to be light.{/i}"
    pause 0.8

    # TEAM EXIT CALLS (OFF-SCREEN)
    unit2 "{i}Route green.{/i}"
    pause 0.4
    unit3 "{i}Uploading bodycam. Metrics clean.{/i}"
    pause 0.6

    # ABSENCE, NOT REMORSE
    # CAMERA: Hold on corridor emptiness; team shadows pass and vanish frame-left; Aeron still (off-camera).
    a "{i}No pulse of guilt. No sickness. Just breath and static. The city hums the same.{/i}"
    pause 0.8

    a "{i}Three-hundred eighty-nine operations before this. This is three-hundred ninety.{/i}"
    pause 0.8
    a "{i}The number used to mean something. Now it's just... counting.{/i}"
    pause 0.9

    # WALK-OUT
    # VISUAL: Door closes on the room; last thing we see is the shattered photo on the floor.
    # SFX: Door hydraulics; lights flicker then stabilize.
    #play sound "sfx/lights_flicker.ogg"
    a "{i}File the victory. Walk the corridor. Leave the room as clean as the report.{/i}"
    pause 0.9

    # VISOR REFLECTION
    # CAMERA: Tight on visor reflection; eyes unreadable, distorted; corridor lines bend across faceplate.
    a "{i}My visor gives me someone else's eyes back.{/i}"
    pause 0.8
    a "{i}Feel nothing. Ask nothing. Do what you're told.{/i}"
    pause 0.7

    # DOCTRINE BEAT + HAIRLINE QUESTION
    a "{i}Order is mercy.{/i}"
    pause 0.6
    a "{i}(…){/i}"
    pause 0.8
    a "{i}...Is this what mercy looks like?{/i}"
    pause 1.0

    # PLAYER SEED — AMBIGUOUS EMP/OB
    menu:
        "It flickers at the edge of thought — a face, a feeling, unwelcome.":

        "Bury it.":
            $ adjust_empathy_once(-1)  # OB-lean; consider cred+1 in backend if you’re tracking it
            a "{i}Weakness spreads like infection. I cut it out.{/i}"
            # VISUAL: Propaganda screen brightness swells slightly; corridor returns to perfect symmetry.
            pause 0.8
            a "{i}The mission's logged. Sector's secure. That's all that matters.{/i}"
            pause 0.8

        "Let it stay.":
            $ adjust_empathy_once(1)   # EMP-lean; consider notoriety+1 in backend if used
            a "{i}The child's face stays with me. Just the eyes. That’s all it takes.{/i}"
            # VISUAL: Screen white cools by a hair; a hint of red emergency strip reflects in visor.
            pause 0.8
            a "{i}The report will be clean. But I won’t be.{/i}"
            pause 0.8

    # CLOSE
    a "{i}The mission’s complete. The sector’s secure.{/i}"
    pause 0.6
    a "{i}That’s all that matters.{/i}"
    pause 0.8

    # HOLO-CALL — MARCUS
    # VISUAL: Corridor dims 15%; holographic blue bloom builds out of black.
    # SFX: holocall-incoming; soft carrier hiss under dialogue.
    a "{i}Incoming request: High Marshal Rylan.{/i}"
    pause 0.6
    a "{i}Private channel. He never uses private channels.{/i}"
    pause 0.9

    #scene black with fade
    #show marcus_holo_mid with dissolve  # if you render a portrait plate

    m "Exemplary work, Aeron. Your metrics were flawless."
    pause 0.5
    m "Ninety-nine point seven percent efficiency. Seven years of training produces this."
    pause 0.7
    m "You are becoming precisely what I intended."
    pause 0.7
    m "Glass completes missions. Glass doesn’t question. That’s what makes you valuable."
    pause 0.8

    a "{i}That’s what they call me.{/i}"
    pause 0.6
    a "{i}Sharp. Obedient. Disposable. Transparent.{/i}"
    pause 0.8
    a "{i}...Is this what you intended, Father?{/i}"
    pause 0.9
    a "{i}Or just what you’ll accept?{/i}"
    pause 1.0

    m "Tomorrow night, you’ll attend the Sector 7 Gala."
    pause 0.6
    m "Directive presence. Show them what Echelon excellence looks like."
    pause 0.6
    m "Rest now. You’ve earned it."
    pause 0.7

    a "{i}Earned it.{/i}"
    pause 0.6
    a "{i}Order is mercy.{/i}"
    pause 0.7
    a "{i}...{/i}"
    pause 0.8
    a "{i}The words feel automatic. Like breathing.{/i}"
    pause 0.9
    a "{i}Tomorrow, the gala. Tonight, the report.{/i}"
    pause 0.6
    a "{i}There’s no rest. Just reports. Then orders. Then more silence.{/i}"
    pause 1.0

    centered "{i}Morning. The day of the gala.{/i}"
    pause
    return


    # cann: ===============================
    # cann.scene_id:
    #   act1_sector7_mission  (Act I — Scene 2B)

    # cann.when_in_timeline:
    #   Pre-gala anchor mission; immediately precedes Marcus private holo (Act I early).

    # cann.what_happened (objective canon summary):
    #   - Echelon containment sweep in Sector 7 executed under OP-390 (pre-dawn).
    #   - Civilian family neutralized; efficiency recorded at 99.7%.
    #   - Marcus praises Aeron over private channel; reinforces “Glass” doctrine.
    #   - First micro-fracture after a perfect mantra run (“…Mercy. Who taught me that word?”).
    #   - Player choice seeds tone: bury the flicker (OB) vs let it stay (EMP).

    # cann.aeron_state:
    #   OB-lean read:
    #     Operates as ritual machine: clipped cadence, metrics-first, no visible affect; doubt suppressed on cue.
    #   EMP-lean read:
    #     Same exterior control; brief empathic intrusion (child’s eyes) persists post-op if allowed by choice.

    # cann.path_tracking:
    #   empathy_score_range_so_far:
    #     min_emp_possible: -2   # from earlier “Say it anyway” + “Bury it”
    #     max_emp_possible:  2   # from earlier “Stay silent” + “Let it stay”
    #   notes:
    #     - This scene’s menu is minor weight (×1) toward path_pressure.
    #     - Optionally pair with cred/notoriety deltas in backend, if tracking.

    # cann.thematic_flags:
    #   motifs_used:
    #     - Glass / Reflection / Doctrine Mantras
    #   recurring_lines_seeded:
    #     - “Order is mercy.” / “390 operations.” / “Glass doesn’t break.” (earlier scene)
    #   continuity_asserts:
    #     - 99.7% efficiency must be referenced later by Marcus; OP-390 precedes the gala.
    #     - Family photo shard on floor = visual callback opportunity; keep it consistent if reused.

    # cann.block_status:
    #   anchor_or_variant:
    #     ANCHOR  # mandatory mission; only flavor differs based on the one menu choice
    #   requires_followup:
    #     - act1_03_marcus_holo (private channel continues) / act1_05_gala later in Act I
    # cann: ===============================