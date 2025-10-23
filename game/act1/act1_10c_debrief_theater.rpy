# =======================================================
# ACT 1 - Scene 10c: Debrief Theater (Marcus + The Machine)
# =======================================================

label act1_debrief_theater:

    # VISUAL: Tiered amphitheater; officers at the rim, operatives below; KPI overlay holo-slate
    # LIGHTING: Stage-lit lectern. Audience in disciplined dim.
    # SOUND: Murmur → hush. Holo-chimes. Applause that sounds like rain on glass.

    #scene bg_debrief_theater with fade

    "{i}Amphitheater like a throat. We sit in the soft part while authority speaks from the teeth.{/i}"

    # MARCUS takes stage
    marcus "Surgical compassion. That is our mandate."
    marcus "Latency under one-twenty. Collateral under three-point-five."
    marcus "Stability is compassion. Precision is mercy. You know this."

    # KPI OVERLAY — optionally adjust lines based on earlier flags
    if check_scene_flag("act1_barracks_morning", "mentored_clinical"):
        "{i}My phrasing shows up on a slide. The room nods. Someone wrote it down like it was born here.{/i}"
    if check_scene_flag("act1_archive_merit", "questioned_plaque"):
        "{i}Another slide skips casualty verification entirely. Omission with good posture.{/i}"

    # MARCUS prompts discussion
    marcus "Notes from field units. Observations. Improvements."

    # CHOICE: how Aeron contributes
    menu:
        "Recommend evac corridors and comms windows in dense sectors (humane optimization).":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_debrief_theater", "recommended_evac")
            marcus "(measured) Logged. Corridor cost against latency remains under review."
            "{i}'Under review' is how the room keeps its hands clean.{/i}"
        "Publicly affirm collateral tolerance and decisive action.":
            $ player_state["empathy_score"] -= 1
            $ set_scene_flag("act1_debrief_theater", "affirmed_collateral")
            marcus "(approving) Clarity is loyalty."
            "{i}The room applauds in numbers only it can hear.{/i}"
        "Stay silent; meet Lyra's eyes across the tier.":
            $ set_scene_flag("act1_debrief_theater", "silent_look")
            $ add_affection("Lyra", 1)
            "{i}Her gaze holds for one breath. Enough to mean something. Not enough to cost us here.{/i}"

    # OPTIONAL: Echo any inquiry marks (from other scenes) as a quiet line on the slide.
    if check_scene_flag("act1_inspection_day", "procedural_inquiry") or check_scene_flag("act1_demo_floor", "inquiry_deviance"):
        "{i}A small line at the bottom of the slide: INQUIRY DEVIANCE: 1.{/i}"

    # WRAP
    marcus "We maintain peace because we *measure* it. You are instruments. Play your notes."
    "{i}Applause like rain on a tin roof you can't get out from under.{/i}"

    return
