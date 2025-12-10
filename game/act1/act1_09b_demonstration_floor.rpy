# =======================================================
# ACT 1 - Scene 09b: Demonstration Floor (Echelon Immersion)
# File: act1_09b_demonstration_floor.rpy
# =======================================================

# ======= SCENE START TASKS =======
$ _current_scene_id = "act1_demo_floor"
$ scene_mark(_current_scene_id, "entered")

define ins = Character("Instructor")
define rec = Character("Recruit")


label act1_demo_floor:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Static wide on simulation floor; occasional tight inserts on hands/weapon.
    # LIGHTING: Cold top-down grid. Occasional holowall flicker.
    # SFX LOOP: Air handler hum. Sub-bass from projector.
    # SFX ONE-SHOTS: Distant siren (muted), weapon reports, lamp pop.
    # FX/COMP: Holowall projection—tenement interior, cheap furniture, domestic details.
    # BLOCKING: Black-box room. Gloss white floor. One wall is holowall. Training stations.

    #scene bg_demo_floor_idle with fade

    # ========= OPENING — THE SIMULATION =========
    # VISUAL: Holowall projects a tenement interior—cheap table, two cups, a jacket on a chair.

    "The training room smells like ozone and recycled air—white floor, black walls, one surface pretending to be a window into someone's home."

    athought "Tenement interior. Cheap table, two cups, a jacket on a chair. They call it a 'domestic space.' Never 'home.'"

    ins "Unit Seven. Observe proportionality."

    ins "Scenario: data carriers sheltering contraband in a domestic space."

    ins "Latency window: one-twenty milliseconds. Collateral threshold: three-point-five."

    ins "Demonstrate."

    athought "My palms know the weight of the pistol. The room knows too."

    rec "(whisper) Are those live?"

    ins "Targets are designated. Perform."

    "The recruit's breath fogs his visor. He thinks the holowall makes it less real. The holowall makes it easier—that's not the same thing."

    # ========= PLAYER CHOICE — DEMONSTRATION =========
    # NOTE: This is a heavier choice. Factor 2 for the decisive options.

    menu:
        athought "Three silhouettes inside the projected room. The timer ticks in the corner of my eye."

        "Take the clean shot — center mass, no drift.":
            $ choice_and_dev(
                _current_scene_id, "demo_clean_shot", "OB", factor=2,
                note="Executes decisive neutralization; prioritizes latency over environment shaping."
            )
            $ scene_mark(_current_scene_id, "clean_shot")

            "Sight lifts, settles, breath held—no tremor. The projector approves before the body hits the floor that isn't there."

            ins "Latency: eighty-seven. Collateral: projected two-point-one. Acceptable."

            athought "Applause is a number. The room claps in digits."

        "Disrupt the light — force them to move, then isolate.":
            $ choice_and_dev(
                _current_scene_id, "demo_flush_first", "EMP", factor=1,
                note="Uses environment to separate civilians from contraband before engagement."
            )
            $ scene_mark(_current_scene_id, "flush_first")

            "The round goes into the lamp—bulb pops, shadow peels off the far wall."

            athought "Hands grab the jacket, not the bag. Panic is a map if you can read it."

            "Second shot finds the bag, not the ribs. The room recalculates."

            ins "Latency: one-eighteen. Collateral: projected one-point-three. Noted."

            ins "Deviation from direct neutralization: recorded."

        "Request ID verification — refuse to engage without confirmation.":
            $ choice_and_dev(
                _current_scene_id, "demo_inquiry_deviance", "EMP", factor=2,
                note="Procedural inquiry over speed; contests designation ≠ identity."
            )
            $ scene_mark(_current_scene_id, "inquiry_deviance")

            "Sights stay on the seam where wall meets counter. Finger rests, doesn't pull."

            a "Requesting ID verification on targets. Confirm data-carrier status with live ping."

            ins "You have designation. Proceed."

            a "Designation isn't identity."

            ins "Latency window closing."

            "The recruit two stations down finally fires—three shots, eager to please the machine."

            ins "Unit Seven: Inquiry Deviance logged. Outcome achieved by adjacent unit. Proceed to secondary."

    # ========= SHARED AFTERMATH =========
    # VISUAL: The holowall drops to blank white. The scene vanishes.

    "The holowall drops to blank—white eating the scene like it never happened. That's the trick: make it clean, make it believable."

    ins "Notes:"

    if scene_has(_current_scene_id, "clean_shot"):
        ins "Unit Seven demonstrates decisive action. Collateral within tolerance. Instructional."
    elif scene_has(_current_scene_id, "flush_first"):
        ins "Unit Seven demonstrates environmental control. Collateral minimized. Deviation logged."
    elif scene_has(_current_scene_id, "inquiry_deviance"):
        ins "Unit Seven exhibits latency via procedural inquiry. Mark appended."

    # ========= INTERNAL ECHO — PATH-BASED =========

    if empathy_band() == "obedience":
        athought "Numbers approve. That's the point."
    elif empathy_band() == "empathy":
        athought "Numbers approve. People don't."
    else:
        athought "Numbers approve. Something in me doesn't."

    # ========= RECRUIT REACTION — MIRRORS PLAYER CHOICE =========

    if scene_has(_current_scene_id, "clean_shot"):
        rec "(low) Teach me that driftless pull?"
        athought "He wants my hands. He doesn't want my head."

    elif scene_has(_current_scene_id, "flush_first"):
        rec "(awed) You moved them without touching them."
        athought "He thinks it's style. It's mercy wearing a uniform."

    elif scene_has(_current_scene_id, "inquiry_deviance"):
        rec "(nervous) They'll dock you for that."
        athought "He says it like weather—rain happens, so does docking."

    # ========= DOCTRINE REMINDER =========

    ins "Remember: Stability is compassion. Precision is mercy. Latency kills."

    "The words glow on the wall—'Stability is compassion.' The font is softer than the meaning."

    # ========= SECTOR 10 FORESHADOW =========
    # VISUAL: A header flickers on a secondary display—brief, almost subliminal.

    "A header flickers and dies before the instructor sees it: SECTOR TEN: BRIDGE APPROACH. Like a pulse under skin."

    # ========= EXIT =========

    ins "Dismissed. Debrief Theater at nineteen-hundred."

    "The door opens—cold air rushing in, colder air rushing out."

    athought "The room keeps its secrets. So do I."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_demo_floor
# cann.when_in_timeline: Afternoon of Inspection Day; before Debrief (19:00).
# cann.what_happened:
#   - Instructor runs domestic-contraband holowall scenario.
#   - Player action:
#       • demo_clean_shot → OB factor=2, decisive neutralization.
#       • demo_flush_first → EMP factor=1, environmental separation.
#       • demo_inquiry_deviance → EMP factor=2, identity verification over speed.
#   - Instructor "Notes" varies; nearby recruit beat mirrors choice.
#   - Foreshadow: header flicker "SECTOR TEN: BRIDGE APPROACH".
# cann.aeron_state: Pre-lock; procedural voice with visible fissures under EMP selections.
# cann.path_tracking:
#   - Scene deltas: OB +2 | EMP +1 | EMP +2
# cann.thematic_flags: designation≠identity; performance optics; "numbers approve vs people"; mantra reinforcement.
# cann.block_status: VARIANT; requires follow-up at Debrief Theater to read flags for report tone + Marcus reaction hooks.
# cann.visual_plate_economy: Reuse holowall tenement plate; one hero "lamp pop" and one "blank drop" plate for montage.