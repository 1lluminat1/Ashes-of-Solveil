# =======================================================
# ACT 1 - Scene 10c: Debrief Theater (Marcus + The Machine)
# File: act1_10c_debrief_theater.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_10c_debrief_theater"
$ scene_mark(_current_scene_id, "entered")


label act1_debrief_theater:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Wide establishing on amphitheater; push in on Marcus at lectern.
    # LIGHTING: Stage-lit lectern. Audience in disciplined dim.
    # SFX LOOP: Murmur → hush. Holo-chimes. Muted applause.
    # BLOCKING: Tiered amphitheater; officers at the rim, operatives below.
    # FX/COMP: KPI overlay holo-slate floating beside lectern.

    #scene bg_debrief_theater with fade

    # ========= OPENING — THE THEATER =========

    "Amphitheater like a throat—we sit in the soft part while authority speaks from the teeth."

    # ========= MARCUS TAKES STAGE =========

    m "Surgical compassion. That is our mandate."

    m "Latency under one-twenty. Collateral under three-point-five."

    m "Stability is compassion. Precision is mercy. You know this."

    # ========= KPI OVERLAY — CALLBACK SLIDES =========

    if scene_has("act1_barracks_morning", "mentored_clinical"):
        athought "My phrasing shows up on a slide. The room nods. Someone wrote it down like it was born here."

    if scene_has("act1_10b_archive_merit", "questioned_plaque"):
        athought "Another slide skips casualty verification entirely. Omission with good posture."

    # ========= MARCUS PROMPTS DISCUSSION =========

    m "Notes from field units. Observations. Improvements."

    menu:
        athought "The room waits. Marcus waits. The machine waits for its instruments to speak."

        "Recommend evac corridors and comms windows in dense sectors.":
            $ choice_and_dev(
                _current_scene_id, "debrief_recommend_evac", "EMP", factor=1,
                note="Advocates humane routing: evac corridors + comms windows."
            )
            $ scene_mark(_current_scene_id, "recommended_evac")

            a "Evac corridors in dense residential. Comms windows before breach. Reduces collateral without compromising latency."

            m "(measured) Logged. Corridor cost against latency remains under review."

            athought "'Under review' is how the room keeps its hands clean."

        "Publicly affirm collateral tolerance and decisive action.":
            $ choice_and_dev(
                _current_scene_id, "debrief_affirm_collateral", "OB", factor=1,
                note="Affirms tolerance bands + decisiveness in plenary."
            )
            $ scene_mark(_current_scene_id, "affirmed_collateral")

            a "Current tolerance bands are optimal. Decisive action within parameters saves more than hesitation."

            m "(approving) Clarity is loyalty."

            "Applause ripples through the tiers—quiet, measured, like rain on a tin roof."

        "Stay silent; meet Lyra's eyes across the tier.":
            $ record_choice_once(
                _current_scene_id, "_debrief_silent_look",
                note="Neutral non-participation; silent connection with Lyra."
            )
            $ scene_mark(_current_scene_id, "silent_look")
            $ rel_bump("Lyra", 1)

            "Her gaze holds for one breath—enough to mean something, not enough to cost us here."

    # ========= ALIGNMENT ECHO =========

    if empathy_band() == "obedience":
        athought "They measure peace. We perform it."
    elif empathy_band() == "empathy":
        athought "They measure peace. I count the missing names."
    else:
        athought "They measure peace. I'm starting to measure the cost."

    # ========= INQUIRY DEVIANCE CALLBACK =========

    if scene_has("act1_inspection_day", "procedural_inquiry") or scene_has("act1_demo_floor", "inquiry_deviance"):
        "A small line at the bottom of the slide: INQUIRY DEVIANCE: 1."

    # ========= WRAP =========

    m "We maintain peace because we *measure* it. You are instruments. Play your notes."

    "Applause like something you can't get out from under."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_10c_debrief_theater
# cann.when_in_timeline: After Demonstration Floor; evening plenary at 19:00; pre–Sector 10 departure block.
# cann.what_happened:
#   - Marcus frames doctrine (latency/collateral bands).
#   - Aeron can: recommend humane corridors (EMP+1), affirm tolerance (OB+1), or stay silent (NEU).
#   - Slides subtly reflect earlier scenes (barracks phrasing, archive omission).
# cann.aeron_state: Sensory narration; athought for interpretation.
# cann.path_tracking:
#   - Weights: single menu → ±1 or 0 → scene delta range −1 → +1.
#   - Flags: recommended_evac / affirmed_collateral / silent_look; completed.
#   - Social: rel_bump("Lyra", +1) on neutral silent look.
# cann.thematic_flags: Measurement-as-morality; applause-as-instrumentation; public performance vs private signal.
# cann.block_status: VARIANT (light); lightly colors Marcus's future one-on-one tone.
# cann.visual_plate_economy:
#   - REUSE: Single amphitheater master; swap KPI overlay text; one Marcus lectern plate.
# cann.requires_followup:
#   - If recommended_evac → humane corridor concept can unlock in Sector 10 setup.
#   - If affirmed_collateral → OB-lean phrasing appears in Marcus feedback later.
#   - If silent_look → next Lyra private beat gains +1 warmth line.