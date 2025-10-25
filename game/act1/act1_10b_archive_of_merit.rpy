# act1_10b_archive_of_merit.rpy


# =======================================================
# ACT 1 - Scene 10b: Archive of Merit (Propaganda Walk)
# =======================================================


define docent = Character("Docent")


label act1_archive_merit:
    $ scene_id = "act1_archive_merit"

    # VISUAL: Marble-and-glass museum corridor; holo-plaques; curated history
    # LIGHTING: Prestigious, soft uplights. Polished reflections.
    # SOUND: Hushed docent VO. Footsteps. Faraway civic anthem.

    #scene bg_archive_corridor with fade

    "{i}The Archive smells like money and disinfectant. History behind glass, polished until it stops bleeding.{/i}"

    docent "We do not rewrite history. We restore it."
    "{i}Words glide over the glass like oil over water.{/i}"

    # PLAQUE: OBSIDIAN BRIDGE PACIFICATION (foreshadow—no names)
    #scene bg_archive_plaque_bridge with dissolve

    docent "Here—Obsidian Bridge pacification. A victory of proportional force and humane precision."

    # Lyra joins mid-walk (silent entrance, optional profile)
    # show lyra_uniform_side with dissolve

    # CHOICE: how Aeron responds to the plaque
    menu:
        "Ask a pointed question about evac corridors and casualty verification.":
            $ adjust_empathy_once("archive_plaque_question", +1)
            $ set_scene_flag(scene_id, "questioned_plaque")
            $ add_trust("Lyra", 1)
            a "Where were evac corridors staged? Who verified casualty counts?"
            docent "(beat) Evacuation was deemed unnecessary within tolerance."
            "{i}'Within tolerance' is a museum way to say 'we didn't look.'{/i}"

        "Compliment the efficiency of the pacification.":
            $ adjust_empathy_once("archive_plaque_praise_efficiency", -1)
            $ set_scene_flag(scene_id, "praised_efficiency")
            $ add_trust("Lyra", -1)
            a "Effective containment at scale."
            "{i}The glass likes sentences that sound like metrics.{/i}"

        "Say nothing and keep walking.":
            "{i}Silence is easy to curate. No fingerprints.{/i}"

    # SECOND PLAQUE: FOUNDERS' MAXIMS
    #scene bg_archive_plaque_maxims with dissolve

    docent "Maxims of Order: Stability is compassion. Precision is mercy. Latency kills."
    "{i}The font is softer than the meaning.{/i}"

    menu:
        "Add a quiet line under your breath: 'Order without understanding is brittle.'":
            $ adjust_empathy_once("archive_add_understanding", +1)
            $ set_scene_flag(scene_id, "added_understanding")
            # If Lyra respects nuance, reward a hair of affection
            $ add_affection("Lyra", 1)
            l "(low) Careful where you say that."
            a "(low) I just did."

        "Repeat the maxims exactly, for the room to hear.":
            $ adjust_empathy_once("archive_repeat_maxims", -1)
            $ set_scene_flag(scene_id, "repeated_maxims")
            l "(measured) Adequate."

        "Deflect with a neutral 'We continue.'":
            $ set_scene_flag(scene_id, "we_continue")
            "{i}Safe words for dangerous glass.{/i}"

    # EXIT
    docent "Witnesses become records; records become order."
    "{i}Order smiles from behind its teeth and thanks us for visiting.{/i}"

    $ set_scene_flag(scene_id, "completed")
    return