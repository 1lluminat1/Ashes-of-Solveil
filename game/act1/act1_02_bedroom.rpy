# ===================================================
# ACT 1 - Scene 2: Aeron's Bedroom
# File: act1_02_bedroom.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_02_bedroom"
$ scene_mark(_current_scene_id, "entered")


label act1_bedroom:

    # VISUAL: Aeron's quarters. Dim. Sterile.
    # CAMERA: Wide static shot of the room — cold blue spill from the floor-to-ceiling glass, no character in frame.
    # LIGHTING: Cold blue wash from outside. Faint flicker of distant signage below the cloud layer.
    # SOUND: High-altitude wind scraping the exterior. Low mechanical hum in the walls.

    a "{i}Wind sweeps the glass. The tower hums back — steady, mechanical. Almost a heartbeat.{/i}"

    # PHYSICAL SENSATION / ENVIRONMENT
    "{i}Cold air hisses through the vents. Dry. Recycled.{/i}"
    pause 0.6
    "{i}He doesn't mind. Comfort dulls the edge.{/i}"
    pause 0.6

    a "{i}Cold keeps you sharp. Warm makes you forget.{/i}"

    # IDENTITY, NOT BELONGING
    a "{i}The city's still out there. I'm just another piece of it now.{/i}"
    a "{i}A tool. A function.{/i}"

    # VISUAL: Glass motif
    # CAMERA: Push in on the window itself — distorted reflection in the pane, but keep Aeron off-screen.
    # NOTE: We're not showing his face yet. We only see suggestion: a broken silhouette in the glass, warped by wind ripple and thin-air shimmer.
    # SYMBOL: Glass = self as object, not self as person.

    "{i}The reflection in the glass jitters, split and warped by the pressure outside.{/i}"
    pause 0.6

    a "{i}Fractured. Like something held together past its limit.{/i}"

    # PURPOSE VS OUTPUT
    a "{i}The Band was supposed to give me purpose.{/i}"
    a "{i}Instead, I carry out orders. Three hundred eighty-nine of them.{/i}"
    a "{i}Father calls me Glass.{/i}"
    a "{i}Transparent. Sharp. Useful.{/i}"
    a "{i}Perfect metrics. Perfect form.{/i}"
    a "{i}Perfectly empty.{/i}"

    # TRANSITION — SILENCE FALLS
    # SOUND: The tower hum fades down a few decibels. Wind outside softens to near silence.
    # LIGHTING: Slight dim shift; window reflection fades, leaving the room in muted blue.
    # CAMERA: Hold wide on Aeron's room. No character visible. Just space.

    pause 1.0
    play sound "sfx/vent_cycle_off.ogg" fadeout 1.0
    pause 0.5

    # VISUAL: Small motion cue — monitor standby light blinking, then stillness.
    # Add a very faint low-frequency pulse (heartbeat motif) in the mix.

    play sound "sfx/low_pulse.ogg" fadein 1.0 loop
    pause 0.6

    # CAMERA: Slow pan right, toward the nightstand.
    # LIGHTING: The faint glow from the window catches the edge of a photo frame.

    scene bg_bedroom_panright with dissolve
    pause 1.0

    # VISUAL: Nightstand photo — two boys smiling. Kael fifteen, Band bright on wrist. Aeron ten, before his Branding.
    # Light flickers across the Band — the only warm tone in the shot.
    # The hum returns, softer now.

    play sound "sfx_wind_low.ogg" fadein 2.0

    a "{i}He always smiled like he belonged.{/i}"
    a "{i}Even after his Band failed. Even when the whispers started.{/i}"
    a "{i}He kept smiling for three years.{/i}"

    # VISUAL: Aeron's hand begins to reach — stops just shy of the frame.
    # SYMBOL: Touch withheld. Reflection avoided.

    "{i}He reaches for the photo. Stops. Pulls back.{/i}"
    pause 0.8

    a "{i}Looking doesn't change anything.{/i}"
    a "{i}Neither does not looking.{/i}"
    a "{i}But I can't put it away.{/i}"

    # VISUAL: The low hum returns, slightly louder — the pulse of the room steady again.
    # CAMERA: Still on the nightstand photo. Then a slow rack focus as the background sharpens — the closed wardrobe in frame.

    a "{i}Kael couldn't live with being broken.{/i}"
    a "{i}I became perfect at it.{/i}"
    a "{i}Father made me Glass.{/i}"
    a "{i}And Glass doesn't break.{/i}"
    a "{i}...Does it?{/i}"

    # VISUAL: The wardrobe door creaks open on its own as the air system cycles.
    # Inside — the black Echelon uniform, pristine, untouched.
    # SYMBOL: The room performing obedience. Order without will.

    play sound "sfx_wardrobe_creak.ogg"
    pause 0.8

    # CAMERA: Hold on the uniform. Light from the window glances off the insignia.
    # SOUND: Low drone resumes — same pitch as the hum earlier. Mechanical continuity.

    a "{i}Right clothes. Right words. Right performance.{/i}"
    a "{i}Tomorrow's the gala.{/i}"
    a "{i}Father's exhibition.{/i}"
    a "{i}'Look at what I made from failure,' he'll say.{/i}"
    a "{i}A tool that follows orders — that's what he wants them to see.{/i}"
    a "{i}He wants perfection on display.{/i}"
    a "{i}But even perfection hesitates.{/i}"

    # OPTIONAL ACTION — Obedience test (Empathy metric seed)
    menu:
        "Say it anyway":
            # OB lean (formerly -1)
            $ apply_choice_once(_current_scene_id, "_say_it_anyway", "OB", factor=1,
                                next_scene_label="act1_02b_sector7_mission"
                                note="Recites doctrine aloud")
            a "\"{i}Order above all. Unity before self.{/i}\""
            a "{i}The words surface without thought — residue from years of drills.{/i}"
            a "{i}They don't mean anything. They never did.{/i}"
            a "{i}But silence would mean something else entirely.{/i}"
            a "{i}And Father would notice.{/i}"

        "Stay silent":
            # EMP lean (formerly +1)
            $ apply_choice_once(_current_scene_id, "_stay_silent", "EMP", factor=1,
                                next_scene_label="act1_02b_sector7_mission"
                                note="Swallows the words")
            a "{i}He waits for the words to come. They don’t.{/i}"
            a "{i}Sometimes silence feels safer. Less to correct later.{/i}"
            a "{i}Doctrine’s just noise anyway — it’s the pauses they listen to.{/i}"
            a "{i}And Father always listens.{/i}"

    # VISUAL: Terminal on the desk blinks; red notification light pulses.
    # SOUND: Soft chime; message alert cuts through the quiet.
    "{i}The terminal chimes. Mission orders.{/i}"
    pause 0.6

    # CAMERA: Cold red glow spills across the desk.
    a "{i}Sector Seven. Containment sweep. Pre-dawn deployment.{/i}"
    a "{i}Tonight. Before the gala. Before I smile for the cameras.{/i}"

    # ROUTINE — NOT NEW
    a "{i}Operation three-nine-zero.{/i}"
    a "{i}Just another number. Just another night.{/i}"
    a "{i}Feel nothing. Ask nothing. Do what you're told.{/i}"

    # VISUAL: Aeron stands; silhouette against the window; city hums far below.
    "{i}He stands. The tower vibrates with the heartbeat of Solveil. The mission waits.{/i}"
    pause 1.0

    # TRANSITION — ROUTINE, NOT UNCERTAINTY
    a "{i}First the blade. Then the smile.{/i}"
    a "{i}First Glass. Then the performance.{/i}"
    a "{i}Same as always.{/i}"

    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id:
#   act1_02_mission_order  (Act I — Scene 2A)

# cann.when_in_timeline:
#   Immediately before the Sector 7 mission; Aeron receives Operation 390 orders.
#   Anchors the transition from introspection to field execution.

# cann.what_happened (objective canon summary):
#   - Aeron receives his 390th mission order: Sector Seven containment sweep.
#   - Exhibits total procedural obedience; emotion reduced to ritual habit.
#   - “Glass” identity solidified as systemic function, not individuality.
#   - Final lines (“First the blade. Then the smile.”) emphasize performance motif.
#   - First flicker of doubt appears in the line “Glass doesn’t break … does it?”

# cann.aeron_state:
#   OB-lean read:
#     Fully conditioned soldier; obedience equated with purpose; detached and precise.
#   EMP-lean read:
#     Minimal deviation — faint questioning impulse present but instantly repressed.
#   Neutral (pre-lock) summary:
#     Disassociated, procedural cognition; perceives self as extension of Echelon’s order.

# cann.path_tracking:
#   empathy_score_range_so_far:
#     min_emp_possible: -1   # from “Say it anyway”
#     max_emp_possible:  1   # from “Stay silent”
#   notes:
#     - This choice seeds the first minor path_pressure adjustment (×1 weight).
#     - Establishes baseline for later empathy/obedience divergence during Act I.

# cann.thematic_flags:
#   motifs_used:
#     - Glass / Performance / Routine vs Identity
#   recurring_lines_seeded:
#     - “Glass doesn’t break … does it?”   /   “First the blade. Then the smile.”
#   continuity_asserts:
#     - Operation count = 389 completed → 390 pending.
#     - Kael failed at 15 → survived 3 years → suicide at 17.
#     - Mission framed as ordinary containment (not exceptional).

# cann.block_status:
#   anchor_or_variant:
#     ANCHOR   # establishes Aeron’s identity foundation; flavor diverges later
#   requires_followup:
#     - act1_02b_sector7_mission  (execution of Operation 390)