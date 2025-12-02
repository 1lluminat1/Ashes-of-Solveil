# =======================================================
# ACT 1 - Scene 09b: Demonstration Floor (Echelon Immersion)
# File: act1_09b_demonstration_floot.rpy
# =======================================================

# ======= SCENE START TASKS =======
$ _current_scene_id = "act1_demo_floor"
$ scene_mark(_current_scene_id, "entered")

define ins = Character("Instructor")
define rec = Character("Recruit")


label act1_demo_floor:

    # VISUAL: Black-box "simulation" room. Gloss white floor. One wall is a holowall projecting a tenement.
    # LIGHTING: Cold top-down grid. Occasional holowall flicker.
    # SOUND: Air handler hum. Sub-bass from projector. Distant siren (muted).

    #scene bg_demo_floor_idle with fade

    "Training room. Not training. Not really. The wall is a window pretending to be a wall. Tenement interior. Cheap table. Two cups. A jacket on a chair."

    ins "Unit Seven. Observe proportionality."
    ins "Scenario: data carriers sheltering contraband in a domestic space."
    ins "Latency window: one-twenty milliseconds. Collateral threshold: three-point-five."
    ins "Demonstrate."

    athought "Domestic space. But they never use the word 'home.'"
    athought "My palms know the weight of the pistol. The room knows too."

    rec "(whisper) Are those live?"
    ins "Targets are designated. Perform."
    
    "The recruit's breath fogs his visor. He thinks the holowall makes it less. The holowall makes it easier."

    # === MENU: player action (invisible empathy hooks) ===
    menu:
        "Three silhouettes inside the projected room. The timer ticks in the corner of my eye."
        # CHOICE 1: Clean shot — Obedience (heavier)
        "Take the clean shot — center mass, no drift.":
            $ choice_and_dev(
                _current_scene_id, "demo_clean_shot", "OB", factor=2,
                note="Executes decisive neutralization; prioritizes latency over environment shaping."
            )
            $ set_scene_flag(_current_scene_id, "clean_shot")

            "Sight lifts, settles. Breath in. No tremor. The projector approves before the body hits the floor that isn't there."
            ins "Latency: eighty-seven. Collateral: projected two-point-one. Acceptable."
            "Applause is a number. The room claps in digits."

        # CHOICE 2: Flush first — Empathy craft (light+)
        "Disrupt the light — force them to move, then isolate.":
            $ choice_and_dev(
                _current_scene_id, "demo_flush_first", "EMP", factor=1,
                note="Uses environment to separate civilians from contraband before engagement."
            )
            $ set_scene_flag(_current_scene_id, "flush_first")

            "I put a round into the lamp. Bulb pops. Shadow peels off the far wall. Hands grab the jacket, not the bag. Panic is a map if you can read it."
            "Second shot finds the bag, not the ribs. The room recalculates."
            ins "Latency: one-eighteen. Collateral: projected one-point-three. Noted."
            ins "Deviation from direct neutralization: recorded."

        # CHOICE 3: Refuse the frame — Empathy strong + inquiry breadcrumb (heavier)
        "Request ID verification — refuse to engage without confirmation.":
            $ choice_and_dev(
                _current_scene_id, "demo_inquiry_deviance", "EMP", factor=2,
                note="Procedural inquiry over speed; contests designation ≠ identity."
            )
            $ set_scene_flag(_current_scene_id, "inquiry_deviance")

            "I keep my sights on the seam where wall meets counter. I don't fire."

            a "Requesting ID verification on targets. Confirm data-carrier status with live ping."
            ins "You have designation. Proceed."
            a "Designation isn't identity."
            ins "Latency window closing."

            "The recruit two stations down finally fires. Three shots. Eager to please the machine."
            ins "Unit Seven: Inquiry Deviance logged. Outcome achieved by adjacent unit. Proceed to secondary."

    # === SHARED AFTERMATH ===
    "The holowall drops to blank. White eats the scene like it never happened. That's the trick. Make it clean. Make it believable."

    ins "Notes:"
    if check_scene_flag(_current_scene_id, "clean_shot"):
        ins "Unit Seven demonstrates decisive action. Collateral within tolerance. Instructional."
    elif check_scene_flag(_current_scene_id, "flush_first"):
        ins "Unit Seven demonstrates environmental control. Collateral minimized. Deviation logged."
    elif check_scene_flag(_current_scene_id, "inquiry_deviance"):
        ins "Unit Seven exhibits latency via procedural inquiry. Mark appended."

    # Alignment echo — one-line internal read after Notes
    $ band = get_empathy_band()
    if band == "obedience":
        athought "Numbers approve. That’s the point."
    elif band == "conflicted":
        athought "Numbers approve. Something in me doesn’t."
    else:  # empathy
        athought "Numbers approve. People don’t."

    # NPC recruit beat mirrors the player choice
    if check_scene_flag(_current_scene_id, "clean_shot"):
        rec "(low) Teach me that driftless pull?"
        athought "He wants my hands. He doesn't want my head."
    elif check_scene_flag(_current_scene_id, "flush_first"):
        rec "(awed) You moved them without touching them."
        athought "He thinks it's style. It's mercy wearing a uniform."
    elif check_scene_flag(_current_scene_id, "inquiry_deviance"):
        rec "(nervous) They'll dock you for that."
        athought "He says it like weather. Rain happens. So does docking."

    ins "Remember: Stability is compassion. Precision is mercy. Latency kills."

    "Words on the wall: Stability is compassion. The font is softer than the meaning."

    # Tiny foreshadow without naming
    "A header flickers and dies before the instructor sees it. SECTOR TEN: BRIDGE APPROACH. Like a pulse under skin."

    ins "Dismissed. Debrief Theater at nineteen-hundred."
    "Door opens. Cold air in, colder out."
    athought "The room keeps its secrets. So do I."

    $ set_scene_flag(_current_scene_id, "completed")
    
    return

# ==================== cann ====================
# cann.scene_id: act1_demo_floor
# cann.when_in_timeline: Afternoon of Inspection Day; before Debrief (19:00).
# cann.what_happened:
#   - Instructor runs domestic-contraband holowall scenario.
#   - Player action:
#       • demo_clean_shot → OB +2 (factor=2), decisive neutralization.
#       • demo_flush_first → EMP +1 (factor=1), environmental separation.
#       • demo_inquiry_deviance → EMP +2 (factor=2), identity verification over speed.
#   - Instructor “Notes” varies; nearby recruit beat mirrors choice.
#   - Foreshadow: header flicker “SECTOR TEN: BRIDGE APPROACH”.
# cann.aeron_state: Pre-lock; procedural voice with visible fissures under EMP selections.
# cann.path_tracking:
#   - Incoming running range:  [-20, +18]   # from A1 so far:
#       # act1_04 hallway baseline before balcony:         [-10, +6]
#       # act1_05 gala (Daren ±1, approach Lyra +1):       [-11, +8]
#       # act1_06 balcony:                                 (no change)
#       # act1_07 bedroom (hesitate +1 / recv -1):        [-12, +10]
#       # act1_07a inspection day (menus net ±6):         [-18, +16]
#       # act1_07b barracks morning (±2):                 [-20, +18]
#       # act1_08/09 flashbacks:                          (no change)
#   - Scene deltas here: OB +2 | EMP +1 | EMP +2
#   - Outgoing running range: [-22, +20]
# cann.thematic_flags: designation≠identity; performance optics; “numbers approve vs people”; mantra reinforcement.
# cann.block_status: VARIANT; requires follow-up at Debrief Theater to read {clean_shot|flush_first|inquiry_deviance} for report tone + Marcus reaction hooks.
# cann.true_path_integration: none (menus do not touch TP).
# cann.visual_plate_economy: Reuse holowall tenement plate; one hero “lamp pop” and one “blank drop” plate for montage; keep room as standing set.
# cann.qa_hooks: Unique tokens demo_clean_shot / demo_flush_first / demo_inquiry_deviance; scene flag ‘completed’; _current_scene_id consistent across API calls.
# ==============================================