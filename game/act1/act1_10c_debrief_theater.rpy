# =======================================================
# ACT 1 - Scene 10c: Debrief Theater (Marcus + The Machine)
# File: act1_10c_debrief_theater.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_10c_debrief_theater"
$ scene_mark(_current_scene_id, "entered")


label act1_debrief_theater:

    # VISUAL: Tiered amphitheater; officers at the rim, operatives below; KPI overlay holo-slate
    # LIGHTING: Stage-lit lectern. Audience in disciplined dim.
    # SOUND: Murmur → hush. Holo-chimes. Applause that sounds like rain on glass.

    #scene bg_debrief_theater with fade

    "Amphitheater like a throat. We sit in the soft part while authority speaks from the teeth."

    # MARCUS takes stage
    m "Surgical compassion. That is our mandate."
    m "Latency under one-twenty. Collateral under three-point-five."
    m "Stability is compassion. Precision is mercy. You know this."

    # KPI OVERLAY — optionally adjust lines based on earlier flags
    if check_scene_flag("act1_barracks_morning", "mentored_clinical"):
        "My phrasing shows up on a slide. The room nods. Someone wrote it down like it was born here."
    if check_scene_flag("act1_10b_archive_merit", "questioned_plaque"):
        "Another slide skips casualty verification entirely. Omission with good posture."

    # MARCUS prompts discussion
    m "Notes from field units. Observations. Improvements."

    # === MENU: how Aeron contributes ===
    menu:
        "Recommend evac corridors and comms windows in dense sectors (humane optimization).":
            $ choice_and_dev(
                _current_scene_id, "debrief_recommend_evac", "EMP", factor=1,
                next_scene_label="act1_10c_debrief_theater",
                note="Advocates humane routing: evac corridors + comms windows."
            )
            $ set_scene_flag(_current_scene_id, "recommended_evac")

            m "(measured) Logged. Corridor cost against latency remains under review."
            "'Under review' is how the room keeps its hands clean."

        "Publicly affirm collateral tolerance and decisive action.":
            $ choice_and_dev(
                _current_scene_id, "debrief_affirm_collateral", "OB", factor=1,
                next_scene_label="act1_10c_debrief_theater",
                note="Affirms tolerance bands + decisiveness in plenary."
            )
            $ set_scene_flag(_current_scene_id, "affirmed_collateral")

            m "(approving) Clarity is loyalty."

            "The room applauds in numbers only it can hear."

        "Stay silent; meet Lyra's eyes across the tier.":
            $ record_choice_once(
                _current_scene_id, "_debrief_silent_look",
                next_scene_label="act1_10c_debrief_theater",
                note="Neutral non-participation; silent connection with Lyra."
            )
            $ set_scene_flag(_current_scene_id, "silent_look")
            $ add_affection("Lyra", 1)

            "Her gaze holds for one breath. Enough to mean something. Not enough to cost us here."

    # Single-line alignment echo (no momentum; subtle)
    $ band = get_empathy_band()
    if band == "obedience":
        athought "They measure peace. We perform it."
    elif band == "conflicted":
        athought "They measure peace. I’m starting to measure the cost."
    else:  # empathy
        athought "They measure peace. I count the missing names."

    # OPTIONAL: Echo any inquiry marks as a quiet line on the slide.
    if check_scene_flag("act1_inspection_day", "procedural_inquiry") or check_scene_flag("act1_demo_floor", "inquiry_deviance"):
        "A small line at the bottom of the slide: INQUIRY DEVIANCE: 1."

    # WRAP
    m "We maintain peace because we *measure* it. You are instruments. Play your notes."
    
    "Applause like rain on a tin roof you can't get out from under."

    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_10c_debrief_theater
# cann.when_in_timeline: After Demonstration Floor; evening plenary at 19:00; pre–Sector 10 departure block.
# cann.what_happened:
#   - Marcus frames doctrine (latency/collateral bands).
#   - Aeron can: recommend humane corridors (EMP+1), affirm tolerance (OB+1), or stay silent (NEU).
#   - Slides subtly reflect earlier scenes (barracks phrasing, archive omission).
# cann.aeron_state: Descriptive narration in braces; Aeron VO only for alignment echo line.
# cann.path_tracking:
#   - Weights: single menu → ±1 or 0 → scene delta range **−1 → +1**.
#   - Running empathy window BEFORE:  **≈ [-28, +26]**  (after Archive max swing).
#   - Running empathy window AFTER:   **≈ [-29, +27]**  (apply ±1 expansion).
#   - Flags: recommended_evac / affirmed_collateral / silent_look; completed.
#   - Social: `add_affection("Lyra", +1)` on neutral silent look.
# cann.thematic_flags: Measurement-as-morality; applause-as-instrumentation; public performance vs private signal.
# cann.block_status: VARIANT (light); lightly colors Marcus’s future one-on-one tone and Debrief transcript language.
# cann.true_path_integration: none (menu-free rule for TP stands).
# cann.visual_plate_economy:
#   - REUSE: Single amphitheater master; swap KPI overlay text; one Marcus lectern plate.
#   - No hero shots required; consider a wide of the tiered seating for marketing stills.
# cann.requires_followup:
#   - If recommended_evac → humane corridor concept can unlock in Sector 10 setup (dialogue option).
#   - If affirmed_collateral → OB-lean phrasing appears in Marcus feedback later.
#   - If silent_look → next Lyra private beat gains +1 warmth line.
# cann.consistency_asserts:
#   - Keep doctrine phrasing identical across scenes (latency/tolerance bands; maxims).
#   - Ensure archive flag checks use scene key `act1_10b_archive_merit` (not the label name) as done above.