# ===================================================
# ACT 1 - Scene 2B: Sector 7 Mission (OB cadence)
# File: act1_02b_sector7_mission.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_02b_sector7_mission"
$ scene_mark(_current_scene_id, "entered")

define unit2 = Character("Unit-2", color="#4A90E2")
define unit3 = Character("Unit-3", color="#4A90E2")


label act1_sector7_mission:

    # SCENE SETUP — MID LEVELS, SECTOR 7
    # CAMERA: 38mm, eye-level, center-locked; slight vignette. Static plate (no character sprites).
    # COLOR: Cold white (fluoro), cyan accents, crushed shadows.
    # FX: Subtle volumetric fog cards near floor grates; steam plumes on loop (low alpha).
    # SFX LOOP: low mechanical drone; far-city rumble (very subtle).
    # TIP: Author one hero BG plate + 2 close variants (door, interior room) for cut-ins.

    #scene bg_sector7_corridor with fade
    #$ set_loop("sfx/industrial_drone_loop.ogg", -12)  # (custom helper if you use one)
    #play sound "sfx/comm_ping.ogg"

    athought "Orders arrive as light. White. Clean. Forgiving."
    # VISUAL: Floodlights flare on in sequence (L→R), strobes reflected on wet floor seams.
    # LIGHT: Hard top-down fluoro; add strip glints on grating.
    pause 0.7

    athought "Order is mercy."  # mantra 1
    # ON-SCREEN TEXT (tiny, bottom-right): “DOCTRINE OF WORTH: MANTRA 1” (diegetic HUD feel)
    pause 0.8

    # COMMS — MARCUS (DIEGETIC) — off-screen radio
    # SFX: light radio hiss; notch filter 3–4kHz to sell comms.
    m "Containment only. Keep it surgical. The Directorate remembers numbers, not noise."
    athought "Obedience is survival."  # mantra 2
    # NOTE: Keep Aeron unseen; we stay in POV/world plates to emphasize ritual.
    pause 0.7

    athought "Three-hundred eighty-nine operations. This is 390."
    # UI OVERLAY: Minimal HUD card “Stabilization Sweep / S7-Δ / OP-390” (white on 20% black).
    pause 0.7

    athought "Seven years earning the right to exist."
    # DOOR BREACH BLOCK
    # CAMERA: 38mm, head-on with sealed bulk door; red security lamp pulsing.
    # PROP: Magnetic breach charge (small), status LED arming (blink → solid).
    #play sound "sfx/breach_charge.ogg"  # brief arming chirp

    athought "Door seals behind us. Footfalls count distance. Four signatures. No hostiles flagged."
    # FX: quick shadow pass of team shapes sliding past frame; keep faces unseen; visors dark.
    pause 0.7

    athought "Precision is grace."  # mantra 3
    # NOTE: Use this beat to punch the sterile geometry; perfect symmetry shot sells “order”.
    pause 0.7

    # INTERIOR ROOM — FAMILY
    # CAMERA: 38mm, low angle from threshold; rifle-sight/occluding geometry at frame edge.
    # LIGHT: Emergency red strips + cold spill → skin tones desaturated.
    # BLOCKING: Two adults shielding small figure; older teen at rusted panel (warm ember LED).
    athought "White steals their colors first. The room learns to hold its breath."
    # FX: light dust motes; a hovering vapor from broken pipe back-left.
    pause 0.9

    # TEAM RADIO (FILTERED), KEEP OFF-SCREEN
    unit3 "{i}Clear path.{/i}"
    unit2 "{i}Panel's hot. Unregistered transmitter.{/i}"
    unit3 "{i}Orders?{/i}"
    # FIRING (SUPPRESSED) — DO NOT GLORIFY
    # SFX: "sfx/suppressed_bursts.ogg" (3 short bursts), then brass ticks (very soft).
    # VISUAL: Muzzle flicker light only; do not show impacts; hard cut to aftermath plate.
    athought "The manual says flinching spreads panic."
    # AFTERMATH PLATE
    # CAMERA: 38mm waist-high; bodies cropped respectfully; shattered photo frame foreground.
    # SFX: Fluoro buzz fades back; HVAC whoosh; no reverb spike.
    athought "Doubt is rot."  # mantra 4
    pause 0.8

    # HUD METRICS
    # OVERLAY: flatlines, timer stop, “EFFICIENCY: 99.7%”.
    athought "Vitals checked. Zero resistance. Logs compiled. Efficiency rating: 99.7 percent."
    #play sound "sfx/hud_confirm.ogg"  # soft, clean, one blip
    pause 0.8

    # COMMS — PRAISE
    m "Flawless work, Aeron. Sector Seven will hold its line tonight."
    m "This is what resolve looks like."
    athought "Worth is proven through service."  # mantra 5
    pause 0.6
    athought "He calls it resolve. The corridor calls it quiet."
    # VISUAL: Cut back to corridor plate; empty space louder than bodies.
    pause 0.8

    # MICRO-GESTURE — GLOVE
    # CAMERA: Macro close-up of right glove removal; latex sheen catches top light.
    # FX: Tiny spec highlights; no blood on glove (important).
    athought "I peel the glove. No blood. Cleaner than the room deserves."
    athought "The latex gleams under the light."

    # MANTRA STRING — PERFECT DELIVERY
    # CAMERA: Back to center-locked corridor; static. This should feel like drills.
    athought "Order is mercy."
    athought "Obedience is survival."
    athought "Precision is grace."
    athought "Doubt is rot."
    athought "Worth is proven through service."

    # FIRST MICRO-GLITCH (AFTER the clean mantras)
    # CAMERA: Push 5–8% in on empty corridor; nothing moves; the sound does the work.
    athought "...Mercy."
    athought "Who taught me that word?"
    athought "Doesn't matter. The mission's logged."
    athought "Three-hundred ninety operations. The count continues."

    # PROPAGANDA SCREENS
    # VISUAL: Wall screens cold-boot; black → stark white text: “STABILITY IS SALVATION”
    # TYPO: geometric grotesk caps; pure white on black; flicker in; no logo.
    "Anthems bloom across the wall: STABILITY IS SALVATION. White letters pretending to be light."
    pause 0.8

    # TEAM EXIT CALLS (OFF-SCREEN)
    unit2 "{i}Route green.{/i}"
    unit3 "{i}Uploading bodycam. Metrics clean.{/i}"

    # ABSENCE, NOT REMORSE
    # CAMERA: Hold on corridor emptiness; team shadows pass and vanish frame-left; Aeron still (off-camera).
    athought "No pulse of guilt. No sickness. Just breath and static. The city hums the same."
    athought "Three-hundred eighty-nine operations before this. This is three-hundred ninety."
    athought "The number used to mean something. Now it's just... counting."

    # WALK-OUT
    # VISUAL: Door closes on the room; last thing we see is the shattered photo on the floor.
    # SFX: Door hydraulics; lights flicker then stabilize.
    #play sound "sfx/lights_flicker.ogg"
    athought "File the victory. Walk the corridor. Leave the room as clean as the report."

    # VISOR REFLECTION
    # CAMERA: Tight on visor reflection; eyes unreadable, distorted; corridor lines bend across faceplate.
    athought "My visor gives me someone else's eyes back."
    athought "Feel nothing. Ask nothing. Do what you're told."

    # DOCTRINE BEAT + HAIRLINE QUESTION
    athought "Order is mercy."
    athought "(…)"
    athought "...Is this what mercy looks like?"

    # PLAYER SEED — AMBIGUOUS EMP/OB
    menu:
        "It flickers at the edge of thought — a face, a feeling, unwelcome."
        "Bury it.":
            # OB lean (formerly -1)
            $ choice_and_dev(_current_scene_id, "_bury_it", "OB", factor=1,
                                next_scene_label="act1_03_morning_routing",
                                note="Buries the memory")
            athought "Weakness spreads like infection. I cut it out."
            # VISUAL: Propaganda screen brightness swells slightly; corridor returns to perfect symmetry.
            pause 0.8
            athought "The mission's logged. Sector's secure. That's all that matters."
        "Let it stay.":
            $ choice_and_dev(_current_scene_id, "_let_it_stay", "EMP", factor=1,
                    next_scene_label="act1_03_morning_routing",
                    note="Lets the memory stay")
            athought "The child's face stays with me. Just the eyes. That’s all it takes."
            # VISUAL: Screen white cools by a hair; a hint of red emergency strip reflects in visor.
            pause 0.8
            athought "The report will be clean. But I won’t be."

    # CLOSE
    athought "The mission’s complete. The sector’s secure."
    athought "That’s all that matters."

    # HOLO-CALL — MARCUS
    # VISUAL: Corridor dims 15%; holographic blue bloom builds out of black.
    # SFX: holocall-incoming; soft carrier hiss under dialogue.
    athought "Incoming request: High Marshal Rylan."
    athought "Private channel. He never uses private channels."

    #scene black with fade
    #show marcus_holo_mid with dissolve  # if you render a portrait plate

    m "Exemplary work, Aeron. Your metrics were flawless."
    m "Ninety-nine point seven percent efficiency. Seven years of training produces this."
    m "You are becoming precisely what I intended."
    m "Glass completes missions. Glass doesn’t question. That’s what makes you valuable."

    athought "That’s what they call me."
    athought "Sharp. Obedient. Disposable. Transparent."
    athought "...Is this what you intended, Father?"
    athought "Or just what you’ll accept?"

    m "Tomorrow night, you’ll attend the Sector 7 Gala."
    m "Directive presence. Show them what Echelon excellence looks like."
    m "Rest now. You’ve earned it."

    athought "Earned it."
    athought "Order is mercy."
    athought "..."
    athought "The words feel automatic. Like breathing."
    athought "Tomorrow, the gala. Tonight, the report."
    athought "There’s no rest. Just reports. Then orders. Then more silence."

    centered "{i}Morning. The day of the gala.{/i}"

    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
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