# ===================================================
# ACT 1 - Scene 2: Aeron's Bedroom
# File: act1_02_bedroom.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_02_bedroom"
$ scene_mark(_current_scene_id, "entered")


label act1_bedroom:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Wide static shot of the room — no character in frame yet. Cold, minimal.
    # LIGHTING: Cold blue wash from floor-to-ceiling window. Faint flicker of distant signage below the cloud layer.
    # SFX: High-altitude wind scraping the exterior (constant, low). Mechanical hum in the walls (subtle drone).
    # BLOCKING/PROPS: Sparse quarters. Terminal on desk (standby). Nightstand with photo frame. Wardrobe closed.
    # FACE: Aeron not visible yet — we're establishing space before person.

    # VISUAL: Exterior wind buffets the window. The tower itself seems to breathe.
    "Wind scrapes the exterior glass. The tower answers—a low mechanical hum, steady and rhythmic."

    athought "Is that the building's pulse? Or my own?"

    # VISUAL: Cold air vents cycling. Vapor visible in the blue light.
    "Cold air hisses through the vents—dry, recycled, faintly metallic on the tongue."

    pause 0.6

    athought "Cold keeps you sharp. Warmth makes you forget."

    # VISUAL: The room in wide shot. Impersonal. Could belong to anyone.
    athought "The city's still out there. I'm just another piece of it now—a tool, a function."

    # ========= GLASS MOTIF — REFLECTION =========
    # CAMERA: Push in on the window itself. Distorted reflection in the pane—Aeron's silhouette warped by pressure shimmer.
    # NOTE: We don't show his face clearly. Just suggestion: a broken shape in the glass.
    # LIGHTING: External glow catches condensation trails on the interior surface.

    "The reflection in the window jitters, split and warped by the pressure differential outside."

    pause 0.6

    athought "Fractured. Like something held together past its limit."

    # ========= IDENTITY / PURPOSE =========
    athought "The Band was supposed to give me purpose. Instead, I carry out orders—three hundred eighty-nine of them."

    athought "Father calls me Glass. Transparent, sharp, useful."

    athought "Perfect metrics, perfect form, perfectly empty."

    # ========= TRANSITION — SILENCE FALLS =========
    # SOUND: Tower hum fades down. Wind softens to near silence.
    # LIGHTING: Slight dim shift; window reflection fades, leaving the room in muted blue.
    # CAMERA: Hold wide on room. Still no clear view of Aeron. Just space.

    pause 1.0
    #play sound "sfx/vent_cycle_off.ogg" fadeout 1.0
    pause 0.5

    # VISUAL: Monitor standby light blinks once, then holds steady.
    # SOUND: Faint low-frequency pulse fades in—could be mechanical, could be biological. Ambiguous.

    #play sound "sfx/low_pulse.ogg" fadein 1.0 loop
    pause 0.6

    # ========= NIGHTSTAND — KAEL =========
    # CAMERA: Slow pan right toward the nightstand.
    # LIGHTING: Faint window glow catches the edge of a photo frame—the only warm tone in the shot.
    # VISUAL: Photo of two boys. Kael at fifteen, Band bright on his wrist, grinning. Aeron at ten, pre-Branding, uncertain.

    #scene bg_bedroom_panright with dissolve
    pause 1.0

    #play sound "sfx_wind_low.ogg" fadein 2.0

    athought "He always smiled like he belonged. Even after his Band failed—even when the whispers started."

    athought "He kept smiling for three years."

    # VISUAL: A hand enters frame, reaching toward the photo. Stops just short. Withdraws.
    # SYMBOL: Touch withheld. Connection avoided.

    "His hand hovers over the frame—close enough to feel the cold polymer edge—then pulls back."

    pause 0.8

    athought "Looking doesn't change anything. Neither does not looking. But I can't put it away."

    # ========= KAEL'S ABSENCE =========
    # CAMERA: Hold on the photo. Slow rack focus—background sharpens to reveal the closed wardrobe.
    # SOUND: Low hum returns, slightly louder. Room settling back into rhythm.

    athought "Kael couldn't live with being broken."

    athought "I became perfect at it—perfect enough that nothing shows."

    athought "...But does that mean nothing's there?"

    # ========= WARDROBE — THE UNIFORM =========
    # VISUAL: Wardrobe door creaks open as air system cycles. Inside: black Echelon uniform, pristine, untouched.
    # SYMBOL: The room performing obedience. Order without will.
    # SOUND: Soft creak. Then the hum continues—mechanical continuity.

    #play sound "sfx_wardrobe_creak.ogg"
    pause 0.8

    # CAMERA: Hold on the uniform. Light from the window catches the insignia—cold gleam.

    athought "Right clothes, right words, right performance."

    athought "Tomorrow's the gala. Father's exhibition. 'Look at what I made from failure,' he'll say."

    athought "A tool that follows orders—exactly what he wants them to see."

    athought "He wants perfection on display." 
    athought "...but even perfection hesitates."

    # ========= CHOICE — DOCTRINE TEST =========
    # VISUAL: Aeron's silhouette against the window. City hums far below.
    # NOTE: First empathy/obedience seed. Small weight, but establishes player's instinct.

    menu:
        athought "A whisper away from obedience. A breath away from defiance."

        "Say it anyway":
            $ choice_and_dev(_current_scene_id, "say_it_anyway", "OB", factor=1,
                                next_scene_label="act1_02b_sector7_mission",
                                note="Recites doctrine aloud")

            a "Order above all. Unity before self."

            athought "The words surface without thought—residue from years of drills."

            athought "They don't mean anything. They never did. But silence would mean something else entirely, and Father would notice."

        "Stay silent":
            $ choice_and_dev(_current_scene_id, "stay_silent", "EMP", factor=1,
                                next_scene_label="act1_02b_sector7_mission",
                                note="Swallows the words")

            athought "I wait for the words to come. They don't."

            athought "Sometimes silence feels safer—less to correct later. Doctrine's just noise anyway. It's the pauses they listen to, and Father always listens."

    # ========= MISSION ORDER =========
    # VISUAL: Terminal on desk blinks; red notification light pulses.
    # SOUND: Soft chime cuts through the quiet. Message alert.
    # LIGHTING: Cold red glow spills across the desk surface.

    "The terminal chimes—soft, insistent. Red light spills across the desk."

    pause 0.6

    athought "Sector Seven. Containment sweep. Pre-dawn deployment. Tonight, before the gala—before I smile for the cameras."

    athought "Operation three-nine-zero. Just another number, just another night."

    athought "Feel nothing. Ask nothing. Do what you're told."

    # ========= TRANSITION OUT =========
    # VISUAL: Aeron's silhouette rises. Full figure against the window for the first time—but still backlit, features obscured.
    # CAMERA: Wide shot. City visible beyond. Tower hum continues.
    # SYMBOL: He's part of the machine. The mission waits.

    "The city pulses far below—a grid of light and shadow. The mission waits."

    pause 1.0

    athought "First the blade. Then the smile. Same as always."

    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id:
#   act1_02_bedroom  (Act I — Scene 2)
# cann.when_in_timeline:
#   Immediately before the Sector 7 mission; Aeron receives Operation 390 orders.
#   Anchors the transition from introspection to field execution.
# cann.what_happened (objective canon summary):
#   - Aeron receives his 390th mission order: Sector Seven containment sweep.
#   - Exhibits total procedural obedience; emotion reduced to ritual habit.
#   - Identity as "Glass" established through Marcus's framing (single reference).
#   - Final lines ("First the blade. Then the smile.") emphasize performance motif.
#   - First flicker of doubt appears: "But does that mean nothing's there?"
# cann.aeron_state:
#   OB-lean read:
#     Fully conditioned soldier; obedience equated with purpose; detached and precise.
#   EMP-lean read:
#     Minimal deviation — faint questioning impulse present but instantly repressed.
#   Neutral (pre-lock) summary:
#     Disassociated, procedural cognition; perceives self as extension of Echelon's order.
# cann.path_tracking:
#   empathy_score_range_so_far:
#     min_emp_possible: -1   # from "Say it anyway"
#     max_emp_possible:  1   # from "Stay silent"
#   notes:
#     - This choice seeds the first minor path_pressure adjustment (×1 weight).
#     - Establishes baseline for later empathy/obedience divergence during Act I.
# cann.thematic_flags:
#   motifs_used:
#     - Glass (single metaphorical use) / Performance / Routine vs Identity
#   recurring_lines_seeded:
#     - "But does that mean nothing's there?" / "First the blade. Then the smile."
#   continuity_asserts:
#     - Operation count = 389 completed → 390 pending.
#     - Kael failed at 15 → survived 3 years → implied suicide at 17.
#     - Mission framed as ordinary containment (not exceptional).
# cann.block_status:
#   anchor_or_variant:
#     ANCHOR   # establishes Aeron's identity foundation; flavor diverges later
#   requires_followup:
#     - act1_02b_sector7_mission  (execution of Operation 390)