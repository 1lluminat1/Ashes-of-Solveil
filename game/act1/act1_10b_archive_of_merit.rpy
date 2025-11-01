# =======================================================
# ACT 1 - Scene 10b: Archive of Merit (Propaganda Walk)
# File: act1_10b_archive_of_merit.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_10b_archive_merit"
$ scene_mark(_current_scene_id, "entered")

define docent = Character("Docent")


label act1_archive_merit:

    # VISUAL: Marble-and-glass museum corridor; holo-plaques; curated history.
    # LIGHTING: Prestigious, soft uplights. Polished reflections.
    # SOUND: Hushed docent VO. Footsteps. Faraway civic anthem.

    #scene bg_archive_corridor with fade

    "{i}The Archive smells like money and disinfectant. History behind glass, polished until it stops bleeding.{/i}"

    docent "We do not rewrite history. We restore it."
    "{i}Words glide over the glass like oil over water.{/i}"

    # PLAQUE: OBSIDIAN BRIDGE PACIFICATION (foreshadow—no names)
    #scene bg_archive_plaque_bridge with dissolve

    docent "Here—Obsidian Bridge pacification. A victory of proportional force and humane precision."

    # (Lyra may be present off-VO; silent entrance mid-walk.)

    # === MENU 1: Aeron’s response to the plaque ===
    menu:
        "Ask a pointed question about evac corridors and casualty verification.":
            $ apply_choice_once(
                _current_scene_id, "archive_plaque_question", "EMP", factor=1,
                next_scene_label="act1_10c_debrief_theater",
                note="Challenges curated record; insists on verification over designation."
            )
            $ set_scene_flag(_current_scene_id, "questioned_plaque")
            $ add_trust("Lyra", 1)

            a "Where were evac corridors staged? Who verified casualty counts?"
            docent "(beat) Evacuation was deemed unnecessary within tolerance."
            "{i}'Within tolerance' is a museum way to say 'we didn't look.'{/i}"

        "Compliment the efficiency of the pacification.":
            $ apply_choice_once(
                _current_scene_id, "archive_plaque_praise_efficiency", "OB", factor=1,
                next_scene_label="act1_10c_debrief_theater",
                note="Performs doctrinal approval of force as metrics."
            )
            $ set_scene_flag(_current_scene_id, "praised_efficiency")
            $ add_trust("Lyra", -1)

            a "Effective containment at scale."
            "{i}The glass likes sentences that sound like metrics.{/i}"

        "Say nothing and keep walking.":
            $ record_choice_once(
                _current_scene_id, "_plaque_silent",
                next_scene_label="act1_10c_debrief_theater",
                note="Non-commitment; curatorial silence."
            )
            $ set_scene_flag(_current_scene_id, "_plaque_silent")

            "{i}Silence is easy to curate. No fingerprints.{/i}"

    # SECOND PLAQUE: FOUNDERS' MAXIMS
    #scene bg_archive_plaque_maxims with dissolve

    docent "Maxims of Order: Stability is compassion. Precision is mercy. Latency kills."
    "{i}The font is softer than the meaning.{/i}"

    # === MENU 2: Doctrine echo or subvert ===
    menu:
        "Add a quiet line under your breath: 'Order without understanding is brittle.'":
            $ apply_choice_once(
                _current_scene_id, "archive_add_understanding", "EMP", factor=1,
                next_scene_label="act1_10b_archive_merit",
                note="Subverts doctrine with context principle; favors understanding."
            )
            $ set_scene_flag(_current_scene_id, "added_understanding")
            $ add_affection("Lyra", 1)

            l "(low) Careful where you say that."
            a "(low) I just did."

        "Repeat the maxims exactly, for the room to hear.":
            $ apply_choice_once(
                _current_scene_id, "archive_repeat_maxims", "OB", factor=1,
                next_scene_label="act1_10b_archive_merit",
                note="Signals conformity; reinforces civic catechism."
            )
            $ set_scene_flag(_current_scene_id, "repeated_maxims")

            l "(measured) Adequate."

        "Deflect with a neutral 'We continue.'":
            $ apply_choice_once_neutral(
                _current_scene_id, "archive_we_continue",
                next_scene_label="act1_10b_archive_merit",
                note="Neutral deflection; avoids signaling."
            )
            $ set_scene_flag(_current_scene_id, "we_continue")

            "{i}Safe words for dangerous glass.{/i}"

    # EXIT
    docent "Witnesses become records; records become order."
    "{i}Order smiles from behind its teeth and thanks us for visiting.{/i}"

    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_10b_archive_merit
# cann.when_in_timeline: Same day as Demonstration; museum walk-by before Debrief (19:00).
# cann.what_happened:
#   - Plaque 1 (Obsidian Bridge) reaction: question the record (EMP+1), praise efficiency (OB+1), or stay silent (NEU).
#   - Plaque 2 (Founders’ Maxims) reaction: add “understanding” line (EMP+1), repeat maxims (OB+1), or neutral deflect.
#   - Optional Lyra micro-reads: trust/affection shift on nuance vs obedience.
# cann.aeron_state: Descriptive narration in braces; Aeron VO under `a`. Tone neutral with branch tint via choices.
# cann.path_tracking:
#   - Weights: M1 ±1/0, M2 ±1/0 → scene delta range **−2 → +2**.
#   - Running empathy window BEFORE:  **≈ [-26, +24]**  (after Demonstration Floor ±2).
#   - Running empathy window AFTER:   **≈ [-28, +26]**  (apply ±2 expansion).
#   - Flags: questioned_plaque / praised_efficiency / _plaque_silent; added_understanding / repeated_maxims / we_continue; completed.
#   - Social: add_trust("Lyra", ±1), add_affection("Lyra", +1) gated by lines as scripted.
# cann.thematic_flags: Curation-as-control; language as solvent; “within tolerance” euphemism; museum gloss vs lived harm.
# cann.block_status: VARIANT (lightweight); influences Debrief tone and Lyra warmth in near-term scenes.
# cann.true_path_integration: none (menu-free rule for TP stands).
# cann.visual_plate_economy:
#   - REUSE one corridor master; swap two plaque plates (Bridge / Maxims); minimal UI flickers on plaques.
#   - No hero shots required; consider one over-shoulder macro on “brittle” line for promo stills.
# cann.requires_followup:
#   - If questioned_plaque → log minor Command side-eye at Debrief.
#   - If added_understanding → +1 warmth line from Lyra on next private exchange.
#   - If repeated_maxims or praised_efficiency → OB-lean phrasing echoes in Debrief transcript.
# cann.consistency_asserts:
#   - Aeries altitude grammar (no precip); keep “domestic space” terminology (never “home”) in docent VO.
#   - Ensure `l` is globally defined; this file does not redeclare Lyra.