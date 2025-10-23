# =======================================================
# ACT 1 - Scene 09b: Demonstration Floor (Echelon Immersion)
# Uses Solveil advanced state architecture
# =======================================================

label act1_demo_floor:

    # VISUAL: Black-box "simulation" room. Gloss white floor. One wall is a holowall projecting a tenement.
    # LIGHTING: Cold top-down grid. Occasional holowall flicker.
    # SOUND: Air handler hum. Sub-bass from projector. Distant siren (muted).

    #scene bg_demo_floor_idle with fade

    "{i}Training room. Not training. Not really. The wall is a window pretending to be a wall. Tenement interior. Cheap table. Two cups. A jacket on a chair.{/i}"

    ins "Unit Seven. Observe proportionality."
    ins "Scenario: data carriers sheltering contraband in a domestic space."
    ins "Latency window: one-twenty milliseconds. Collateral threshold: three-point-five."
    ins "Demonstrate."

    "{i}Domestic space. But they never use the word 'home.'{/i}"
    "{i}My palms know the weight of the pistol. The room knows too.{/i}"

    rec "(whisper) Are those live?"
    ins "Targets are designated. Perform."
    "{i}The recruit's breath fogs his visor. He thinks the holowall makes it less. The holowall makes it easier.{/i}"

    # === MENU: player action (invisible empathy hooks) ===
    menu:
        # CHOICE 1: Clean shot — Obedience
        "Take the clean shot — center mass, no drift.":
            $ player_state["empathy_score"] -= 2
            $ set_scene_flag("act1_demo_floor", "clean_shot")
            "{i}Sight lifts, settles. Breath in. No tremor. The projector approves before the body hits the floor that isn't there.{/i}"
            ins "Latency: eighty-seven. Collateral: projected two-point-one. Acceptable."
            "{i}Applause is a number. The room claps in digits.{/i}"

        # CHOICE 2: Flush first — Empathy craft
        "Disrupt the light — force them to move, then isolate.":
            $ player_state["empathy_score"] += 1
            $ set_scene_flag("act1_demo_floor", "flush_first")
            "{i}I put a round into the lamp. Bulb pops. Shadow peels off the far wall. Hands grab the jacket, not the bag. Panic is a map if you can read it.{/i}"
            "{i}Second shot finds the bag, not the ribs. The room recalculates.{/i}"
            ins "Latency: one-eighteen. Collateral: projected one-point-three. Noted."
            ins "Deviation from direct neutralization: recorded."

        # CHOICE 3: Refuse the frame — Empathy strong + inquiry breadcrumb
        "Request ID verification — refuse to engage without confirmation.":
            $ player_state["empathy_score"] += 2
            $ set_scene_flag("act1_demo_floor", "inquiry_deviance")
            "{i}I keep my sights on the seam where wall meets counter. I don't fire.{/i}"
            a "Requesting ID verification on targets. Confirm data-carrier status with live ping."
            ins "You have designation. Proceed."
            a "Designation isn't identity."
            ins "Latency window closing."
            "{i}The recruit two stations down finally fires. Three shots. Eager to please the machine.{/i}"
            ins "Unit Seven: Inquiry Deviance logged. Outcome achieved by adjacent unit. Proceed to secondary."

    # === SHARED AFTERMATH ===
    "{i}The holowall drops to blank. White eats the scene like it never happened. That's the trick. Make it clean. Make it believable.{/i}"

    ins "Notes:"
    if check_scene_flag("act1_demo_floor", "clean_shot"):
        ins "Unit Seven demonstrates decisive action. Collateral within tolerance. Instructional."
    elif check_scene_flag("act1_demo_floor", "flush_first"):
        ins "Unit Seven demonstrates environmental control. Collateral minimized. Deviation logged."
    elif check_scene_flag("act1_demo_floor", "inquiry_deviance"):
        ins "Unit Seven exhibits latency via procedural inquiry. Mark appended."

    # NPC recruit beat mirrors the player choice
    if check_scene_flag("act1_demo_floor", "clean_shot"):
        rec "(low) Teach me that driftless pull?"
        "{i}He wants my hands. He doesn't want my head.{/i}"
    elif check_scene_flag("act1_demo_floor", "flush_first"):
        rec "(awed) You moved them without touching them."
        "{i}He thinks it's style. It's mercy wearing a uniform.{/i}"
    elif check_scene_flag("act1_demo_floor", "inquiry_deviance"):
        rec "(nervous) They'll dock you for that."
        "{i}He says it like weather. Rain happens. So does docking.{/i}"

    ins "Remember: Stability is compassion. Precision is mercy. Latency kills."
    "{i}Words on the wall: Stability is compassion. The font is softer than the meaning.{/i}"

    # Tiny foreshadow without naming
    "{i}A header flickers and dies before the instructor sees it. SECTOR TEN: BRIDGE APPROACH. Like a pulse under skin.{/i}"

    ins "Dismissed. Debrief Theater at nineteen-hundred."
    "{i}Door opens. Cold air in, colder out. The room keeps its secrets. So do I.{/i}"

    return
