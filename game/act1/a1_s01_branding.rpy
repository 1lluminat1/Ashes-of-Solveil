# ===================================================
# ACT 1 - Scene 1: The Branding
# File: act1_01_branding.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_01_branding"
$ scene_mark(_current_scene_id, "entered")


label a1_s01_branding:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Nothing. No image. No character. No light.
    # SOUND: Absolute silence. Hold for three full seconds — do not skip.
    # NOTE: Silence is the opening statement. The absence is the point.

    scene black
    pause 3.0

    athought "They said it would sing."

    # SOUND: Brand connect — wet hiss, metal on flesh. Sound before vision.
    # NOTE: The ritual begins normally. Trust is being built before it's broken.

    #play sound "sfx/brand_connect.ogg"
    pause 0.5

    athought "Bone-deep. Absolute. The moment you become whole."

    # ========= THE RITUAL — SYNC BEGINS =========
    # CAMERA: Extreme close-up — skin, metal, light. The Band sinking in, beginning sync.
    # LIGHTING: Surgical white overhead. Ceremonial glow emanating from the Band interface.
    # NOTE: This SHOULD be working. It looks right. Feels right.

    #scene bg_branding_chamber_closeup with dissolve

    "The iron sinks in. Skin splits, seals, begins to fuse."

    athought "They said it wouldn't hurt if you were worthy."

    pause 0.4

    athought "It doesn't hurt at all."

    # CAMERA: Band interface glowing brighter — synchronization in progress.
    # LIGHTING: Warm golden light spreading outward from the connection point.
    # SOUND: Sync pulse — rhythmic hum, building in steady waves.
    # NOTE: Everything is proceeding normally. Build familiarity before destruction.

    #play sound "sfx/sync_pulse.ogg" loop

    pause 0.6

    "The warmth spreads. The hum builds. Bio-sync initiating."

    marcus "Steady. Let it recognize you."

    athought "Father's voice. Calm. Certain."

    pause 0.4

    athought "This is it. This is when I become real."

    # ========= THE RITUAL — APPROACHING COMPLETION =========
    # CAMERA: Hold tight on the connection point — everything looks perfect.
    # SOUND: Sync pulse climbing in pitch and intensity. Almost there.
    # LIGHTING: Golden glow pulses brighter, faster. Urgency without alarm.
    # NOTE: Build the tension. The music of something working — right up until it doesn't.

    #play sound "sfx/sync_pulse_climb.ogg"
    pause 0.8

    "The pulse quickens. The light intensifies."

    athought "It's working. It has to be working."

    pause 0.5

    athought "I can feel it reaching—"

    # ========= THE REJECTION =========
    # CAMERA: The Band goes dark. No pulse. No light. Nothing.
    # LIGHTING: Golden glow shatters to dead gray — instant, total.
    # SOUND: Sync reject — sudden, sharp CRACK. Like glass breaking inside metal.
    #        Hard cut to silence immediately after. Even ambient sound drops.
    # NOTE: Total failure. Instant. Absolute. No ceremony. No transition.

    #stop sound
    #play sound "sfx/sync_reject.ogg"
    pause 0.3

    "The Band goes silent."

    pause 0.8

    athought "...no."

    # CAMERA: Pull back — reveal Marcus's face for the first time.
    #         First readable emotion: shock, then something colder, faster.
    # VISUAL: marcus_shocked -> marcus_neutral (rapid transition, barely a beat).
    # SOUND: Metal retract — the Band pulling free on emergency release.
    # NOTE: Even Marcus didn't expect this. That matters. Remember it.

    #show marcus shocked
    pause 0.3
    #show marcus neutral

    "The metal slides free. The wound doesn't glow. It just... bleeds."

    athought "No no no no—"

    marcus "...Rejected."

    # ========= THE WOUND =========
    # CAMERA: Close on Aeron's face — twelve years old, raw confusion turning to terror.
    # LIGHTING: Harsh white from above. No warmth anywhere in the frame.
    # SOUND: Blood drip — slow, steady, wrong.
    # NOTE: A child realizing he just became nothing.

    pause 0.6

    athought "That's not possible. It's never happened. Not in our family. Not to—"

    marcus "Hold still."

    # VISUAL: Marcus moving quickly now — clinical, efficient. Damage control.
    #         Literal and political, in the same motion.
    # SOUND: Cauterize hiss — sealing the wound shut.

    #show marcus cold
    #play sound "sfx/cauterize_hiss.ogg"
    pause 0.5

    "The cauterizer seals the wound. The scar tissue forms gray and lifeless—no golden trace, no embedded interface."

    "Just a mark where something should have been."

    pause 0.5

    athought "Empty."

    pause 0.4

    athought "I'm empty."

    # ========= THE AFTERMATH =========
    # CAMERA: Wide shot — Marcus steps back. Evaluating. Already calculating.
    # LIGHTING: Cold white, sterile, unforgiving. The ceremony light feels surgical now.
    # SOUND: amb_tower_hum fades in — hollow and wrong under everything.
    # NOTE: The ceremony is over. Nothing has been resolved.

    #play music "amb/tower_hum.ogg" fadein 2.0

    marcus "Stand."

    # CAMERA: Low angle — Marcus towering. Aeron small and broken beneath him.
    # NOTE: Aeron tries to stand. Legs are shaking. The shoulder is numb and wrong.

    pause 0.6

    athought "He's looking at me like... like I'm a problem. A malfunction."

    pause 0.3

    athought "Like Kael."

    marcus "Do you understand what just happened?"

    # ========= CHOICE — FIRST RESPONSE TO FAILURE =========
    # CAMERA: Close on Aeron's face — confusion, terror, the desperate search for the right answer.
    # NOTE: First choice. Both options are survival instincts from a terrified child.
    #       EMP = reaching outward, for connection and forgiveness.
    #       OB = reaching inward, for correction and function.
    #       Neither is wrong. Neither is safe. This is where the fracture begins.

    menu:
        athought "He's waiting. The silence is filling up with something I can't name."

        "\"I'm sorry.\"":
            $ choice_and_dev(_current_scene_id, "im_sorry", "EMP", factor=1,
                            next_scene_label="act1_bedroom",
                            note="Apologizes — instinct toward connection over correction")

            a "I'm sorry. I—I don't know what I did wrong—"

            athought "The words spill out. Desperate. Pleading."

            marcus "You did nothing wrong. Your biology rejected the interface. It happens."

            athought "His voice is flat. Like he's explaining a mechanical failure."

            pause 0.4

            athought "Like I'm a machine that broke."

        "\"It was a mistake.\"":
            $ choice_and_dev(_current_scene_id, "it_was_a_mistake", "OB", factor=1,
                            next_scene_label="act1_bedroom",
                            note="Seeks correction — instinct toward function over feeling")

            a "It was a mistake. We can try again. Please—"

            athought "If I just stay calm, if I fix this, maybe—"

            marcus "It doesn't work that way. A second attempt would kill you."

            athought "He says it like a fact. Not cruel. Just... true."

            pause 0.4

            athought "And that's worse."

    # ========= GLASS — THE INSTRUCTION =========
    # CAMERA: Marcus crouches to eye level — still doesn't touch him.
    # LIGHTING: Shadow falls across both their faces equally.
    # NOTE: This is the moment. The life raft offered to a drowning child.
    #       It is not kindness. It is utility.

    pause 0.5

    marcus "Listen carefully."

    pause 0.3

    marcus "In three minutes, the gallery doors will open. Families will see their children Branded and whole."

    marcus "They will see you walking beside them."

    pause 0.4

    athought "Walking. Not Branded. Just... walking."

    marcus "You will stand straight. Head up. You will not apologize. You will not explain."

    marcus "You will be useful in other ways."

    # CAMERA: Close on Aeron's face — confusion, then the desperate flicker of hope.
    # NOTE: A drowning child grabbing the only thing offered. He doesn't know what it costs yet.

    pause 0.4

    athought "Useful."

    pause 0.3

    athought "I can be useful."

    marcus "The Band made them whole. You will make yourself essential."

    marcus "Transparent. Unbreakable. Reflect exactly what they need to see."

    pause 0.4

    marcus "You will be Glass."

    # CAMERA: Over Aeron's shoulder — Marcus's face is unreadable.
    #         His hand finally moves to Aeron's unmarked shoulder.
    # SYMBOL: First physical contact. It is not comfort. It is claiming.

    pause 0.6

    marcus "Do you understand?"

    a "...Yes, sir."

    athought "I don't understand. Not really."

    pause 0.3

    athought "But it's the only answer that keeps me alive."

    # ========= THE PERFORMANCE BEGINS =========
    # CAMERA: Wide — Marcus stands, already moving to the door. The public mask is back.
    # SOUND: Door hiss — chamber door opening. Crowd noise bleeds in, muffled.
    # LIGHTING: Harsh light floods the frame. Sudden, clinical.

    #play sound "sfx/door_hiss.ogg"
    #show marcus neutral

    marcus "Walk three steps behind me. Do not speak unless spoken to."

    pause 0.3

    marcus "And Aeron—"

    # CAMERA: Marcus looks back over his shoulder — one last instruction, unhurried.

    pause 0.4

    marcus "Smile when they applaud."

    # VISUAL: Marcus exits the frame.
    # CAMERA: Hold on Aeron alone in the chamber. Wide shot. Room feels larger now.
    # LIGHTING: Cold white, empty, nowhere to hide in it.
    # SOUND: Crowd applause — distant, muffled through the walls. Wrong room.

    #show marcus exits
    pause 1.0

    "The applause echoes. Distant and hollow."

    athought "They're clapping for the others. The whole ones."

    pause 0.4

    athought "Not me."

    pause 0.5

    athought "Never me."

    # CAMERA: Close on Aeron's hand — reaching toward the fresh scar, touching the absence.
    # SYMBOL: The wound where a Band should be. Where one will never be.

    pause 0.6

    athought "Glass doesn't need a pulse."

    pause 0.4

    athought "Glass just reflects."

    pause 0.5

    athought "I can do that."

    pause 0.3

    athought "I can be that."

    pause 0.6

    athought "...I have to be."

    # ========= THE WALK — EXIT INTO THE LIE =========
    # CAMERA: Aeron walks toward the door — small, alone, already performing.
    # LIGHTING: Silhouette against the bright doorway. Features obscured.
    # SOUND: amb_tower_hum swells — then cuts to silence on the threshold.
    # SYMBOL: A child walking into a lie he'll carry for fifteen years.
    # NOTE: Hold this image. Let it breathe.

    pause 0.8

    athought "Smile when they applaud."

    pause 0.5

    athought "Be useful."

    pause 0.5

    athought "Or be nothing."

    # ========= TIME CUT =========
    # CAMERA: Hard cut to black.
    # SOUND: Wind — exterior, high altitude — fades in from silence.
    # TEXT OVERLAY: "FIFTEEN YEARS LATER"
    # NOTE: From the wound to the performance. From child to Glass.

    scene black with fade
    pause 0.6

    #play sound "sfx/wind_exterior_high.ogg" fadein 2.0
    pause 1.0

    "FIFTEEN YEARS LATER"

    pause 1.5

    $ scene_mark(_current_scene_id, "completed")
    jump a1_s02_bedroom


# ========= CANONICAL NOTES =========
# cann.scene_id:
#   act1_01_branding  (Act I — Scene 1)
# cann.when_in_timeline:
#   The opening event. Aeron at age twelve, during the Branding ceremony in the Echelon tower.
#   Establishes the foundational wound before the fifteen-year time skip to the present.
# cann.what_happened (objective canon summary):
#   - Aeron Rylan, age twelve, undergoes the Branding ritual. The Band rejects him — total failure.
#   - Marcus Rylan seals the wound and immediately pivots to damage control.
#   - Marcus instructs Aeron to perform wholeness in public. Coins the "Glass" identity.
#   - Aeron complies with "Yes, sir" — the first of many performed answers that keep him alive.
#   - Scene ends on Aeron walking into the gallery to smile for the applause that isn't for him.
#   - Hard time cut: fifteen years forward to the present.
# cann.aeron_state:
#   EMP-lean read:
#     Apology instinct — reaches for connection and forgiveness, not function.
#     Glass identity received as a lifeline rather than an instruction.
#   OB-lean read:
#     Correction instinct — frames failure as a problem to be fixed, not a loss to be felt.
#     Glass identity received as a role to execute, clean and without sentiment.
#   Neutral (pre-lock) summary:
#     A twelve-year-old absorbing catastrophic identity collapse. Compliance as survival.
#     The Glass framing is accepted not from belief but from the absence of any alternative.
# cann.marcus_state:
#   Shocked — briefly. Then cold and functional. Physical contact (hand on shoulder) is
#   claiming, not comfort. His primary concern is political optics, not Aeron's experience.
#   Does not explain cruelty. Does not acknowledge grief. Offers a role instead.
# cann.path_tracking:
#   empathy_score_range_so_far:
#     min_emp_possible: -1   # from "It was a mistake" (OB x1)
#     max_emp_possible: +1   # from "I'm sorry" (EMP x1)
#   opportunity_totals:
#     opp_emp: 1
#     opp_ob:  1
#   notes:
#     - This is the first choice of the game. Weight is deliberately light (factor=1).
#     - Seeds the player's instinct — connection vs. correction — without committing to a path.
#     - Act I lock not triggered here. Establishes baseline only.
# cann.thematic_flags:
#   motifs_introduced:
#     - Glass (origin scene — first use, Marcus as source)
#     - Rejection / Absence (the scar, the silence, the applause that excludes)
#     - Performance (smile when they applaud — fifteen-year instruction)
#     - Kael (first reference — failed Band, implied fate, mirror for Aeron)
#   recurring_lines_seeded:
#     - "Smile when they applaud." (returns in Act II — Aeron citing it involuntarily)
#     - "Be useful. Or be nothing." (internalized doctrine; resurfaces at path lock)
#     - "Glass doesn't need a pulse." (Aeron's self-definition, Act I–II)
#   continuity_asserts:
#     - Aeron is twelve years old at Branding. Present-day Aeron is twenty-seven.
#     - Marcus coins "Glass" — this is canon. Aeron did not choose the name.
#     - Kael is established as context for Marcus's reaction: he has seen failure before.
#     - The scar is gray, lifeless, no trace. No Band. No interface. Permanent.
# cann.block_status:
#   anchor_or_variant:
#     ANCHOR   # Origin scene. Non-optional. All paths run through it.
#   requires_followup:
#     - act1_02_bedroom  (fifteen-year jump; Aeron at twenty-seven, pre-mission)
