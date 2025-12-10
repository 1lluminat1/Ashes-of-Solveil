# =======================================================
# ACT 1 - Scene 10b: Archive of Merit (Propaganda Walk)
# File: act1_10b_archive_of_merit.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_10b_archive_merit"
$ scene_mark(_current_scene_id, "entered")

define docent = Character("Docent")


label act1_archive_merit:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Slow tracking shot through corridor; occasional close-ups on plaques.
    # LIGHTING: Prestigious soft uplights. Polished marble reflections.
    # SFX LOOP: Hushed docent VO, footsteps on marble, faraway civic anthem.
    # BLOCKING: Marble-and-glass museum corridor; holo-plaques line the walls; curated history.
    # FX/COMP: Subtle holographic shimmer on plaques.

    #scene bg_archive_corridor with fade

    # ========= OPENING — THE ARCHIVE =========

    "The Archive smells like money and disinfectant—history behind display cases, polished until it stops bleeding."

    docent "We do not rewrite history. We restore it."

    athought "Words gliding over surfaces like oil over water."

    # ========= PLAQUE 1: OBSIDIAN BRIDGE PACIFICATION =========
    # VISUAL: Holo-plaque glows—title, sanitized dates, approved imagery.
    #scene bg_archive_plaque_bridge with dissolve

    docent "Here—Obsidian Bridge pacification. A victory of proportional force and humane precision."

    menu:
        athought "The plaque shows numbers, not names. Coordinates, not graves."

        "Ask a pointed question about evac corridors and casualty verification.":
            $ choice_and_dev(
                _current_scene_id, "archive_plaque_question", "EMP", factor=1,
                note="Challenges curated record; insists on verification over designation."
            )
            $ scene_mark(_current_scene_id, "questioned_plaque")

            a "Where were evac corridors staged? Who verified casualty counts?"

            docent "(beat) Evacuation was deemed unnecessary within tolerance."

            athought "'Within tolerance' is a museum way to say 'we didn't look.'"

        "Compliment the efficiency of the pacification.":
            $ choice_and_dev(
                _current_scene_id, "archive_plaque_praise_efficiency", "OB", factor=1,
                note="Performs doctrinal approval of force as metrics."
            )
            $ scene_mark(_current_scene_id, "praised_efficiency")

            a "Effective containment at scale."

            docent "(approving) A precise summary."

            athought "The display likes sentences that sound like metrics."

        "Say nothing and keep walking.":
            $ record_choice_once(
                _current_scene_id, "_plaque_silent",
                note="Non-commitment; curatorial silence."
            )
            $ scene_mark(_current_scene_id, "_plaque_silent")

            athought "Silence is easy to curate. No fingerprints."

    # ========= PLAQUE 2: FOUNDERS' MAXIMS =========
    # VISUAL: Second plaque—gilded text, the doctrine rendered as scripture.
    #scene bg_archive_plaque_maxims with dissolve

    docent "Maxims of Order: Stability is compassion. Precision is mercy. Latency kills."

    "The font is softer than the meaning."

    menu:
        athought "Three sentences. A whole world compressed into slogans."

        "Add a quiet line under your breath: 'Order without understanding is brittle.'":
            $ choice_and_dev(
                _current_scene_id, "archive_add_understanding", "EMP", factor=1,
                note="Subverts doctrine with context principle; favors understanding."
            )
            $ scene_mark(_current_scene_id, "added_understanding")

            a "(low) Order without understanding is brittle."

            docent "(stiffens) The Maxims are complete as written."

            athought "I said it anyway."

        "Repeat the maxims exactly, for the room to hear.":
            $ choice_and_dev(
                _current_scene_id, "archive_repeat_maxims", "OB", factor=1,
                note="Signals conformity; reinforces civic catechism."
            )
            $ scene_mark(_current_scene_id, "repeated_maxims")

            a "Stability is compassion. Precision is mercy. Latency kills."

            docent "(nods) Adequate recitation."

        "Deflect with a neutral 'We continue.'":
            $ record_choice_once(
                _current_scene_id, "archive_we_continue",
                note="Neutral deflection; avoids signaling."
            )
            $ scene_mark(_current_scene_id, "we_continue")

            a "We continue."

            athought "Safe words for dangerous places."

    # ========= EXIT =========

    docent "Witnesses become records; records become order."

    athought "Order smiles from behind its teeth and thanks us for visiting."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_10b_archive_merit
# cann.when_in_timeline: Same day as Demonstration; museum walk-by before Debrief (19:00).
# cann.what_happened:
#   - Plaque 1 (Obsidian Bridge) reaction: question the record (EMP+1), praise efficiency (OB+1), or stay silent (NEU).
#   - Plaque 2 (Founders' Maxims) reaction: add "understanding" line (EMP+1), repeat maxims (OB+1), or neutral deflect.
#   - Docent reacts to Aeron's spoken lines; no other characters present.
# cann.aeron_state: Sensory narration; athought for interpretation. Tone neutral with branch tint via choices.
# cann.path_tracking:
#   - Weights: M1 ±1/0, M2 ±1/0 → scene delta range −2 → +2.
#   - Flags: questioned_plaque / praised_efficiency / _plaque_silent; added_understanding / repeated_maxims / we_continue; completed.
# cann.thematic_flags: Curation-as-control; language as solvent; "within tolerance" euphemism; museum polish vs lived harm.
# cann.block_status: VARIANT (lightweight); influences Debrief tone in near-term scenes.
# cann.visual_plate_economy:
#   - REUSE one corridor master; swap two plaque plates (Bridge / Maxims).
# cann.requires_followup:
#   - If questioned_plaque → log minor Command side-eye at Debrief.
#   - If repeated_maxims or praised_efficiency → OB-lean phrasing echoes in Debrief transcript.