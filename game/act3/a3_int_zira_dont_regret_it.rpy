# =======================================================
# ACT 3 - Interlude: Zira — "Don't Make Me Regret It"
# File: a3_int_zira_dont_regret_it.rpy
# Type: LI THOUGHT INTERLUDE (Zira, path-gated)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_zira_dont_regret_it"
$ scene_mark(_current_scene_id, "entered")

label a3_int_zira_dont_regret_it:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked on the Ghostline workstation. Her hands at the keys.
    #         The monitor glow on her face is the only light that reaches her.
    #         One pull-out to show how much empty room is around her at the end.
    # LIGHTING: Monitor blue on the face. A single bench lamp off-axis. The rest
    #           of the workshop is dark and has been dark for hours.
    # SFX: The keys. Steady. The Ghostline hum underneath — the comfort tone.
    #      No music. No ambient traffic. The base is asleep and Zira is not.
    # FACE: Zira — working. The face she has when her hands are doing what her
    #       head is refusing to stop thinking about. Composed. Not okay.

    # scene bg zira_workstation_late with fade
    # show zira working_hard at center
    # play ambient "audio/amb/ghostline_hum.ogg" fadein 1.5

    if canon_get("path_state", "UNSET") == "OB":
        zthought "Diagnostic loop, pass seventeen. I don't need pass seventeen. Pass fourteen was clean and I kept going."
        zthought "The loop is the anchor. The loop is what my hands do when my head is doing the other thing."
        zthought "The midnight cycle ran in the next pane an hour ago. Three fragments. Null again. Logged."
    else:
        zthought "Seeding Liora's ledgers into every active node. The files are clean, compressed, checksummed. I could run this deployment in my sleep."
        zthought "I am running this deployment because my hands need something to hold that isn't his."
        zthought "The midnight cycle ran in the next pane an hour ago. Three fragments. Not enough to break the block. Enough to feed the cycle."

    zthought "I am replaying the moment I chose him."

    zthought "Not the on-screen one. Not the night I said the thing out loud and meant it. That one was ratification. The actual choice was earlier — the half-second before I said it. The pause where I could have said no and didn't."

    zthought "I remember deciding to say yes."
    zthought "I remember why."

    zthought "And here is the small technical distinction I need to say correctly inside my own head tonight:"
    zthought "I do not regret it."
    zthought "I am specifically not regretting it."

    zthought "Not regretting is a different operation from regretting. Regret is a conclusion. Not-regret is a stance I'm holding. The stance requires maintenance. I am doing the maintenance right now, at pass seventeen of a loop that doesn't need pass seventeen."

    zthought "The cost keeps going up. I have not found the ceiling."
    zthought "There has to be a ceiling. Every cost function has one. I haven't hit it and it is making me nervous."

    if canon_get("path_state", "UNSET") == "OB":
        zthought "He keeps becoming harder. I keep choosing him anyway."
        zthought "..."
        zthought "I chose you before you did the thing."
        zthought "I am still choosing you."
        zthought "Don't make me regret the choice by making the choice stupid."
    else:
        zthought "He keeps meeting me where I am. I keep meeting him where he is. The geometry is working."
        zthought "..."
        zthought "Don't make me watch you become someone I can't reach."

    # She finishes the task. Closes the terminal. Sits for a moment.
    # Does not stand. Opens another task instead.

    zthought "Another loop. Another ledger. Another thing that isn't sleep."

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_zira_dont_regret_it
# cann.chapter: Act III, Phase III
# cann.placement: Path-gated placement.
#                 EMP: after a3_s22_liora_execution_emp.
#                 OB:  after a3_s20_you_dont_get_to_break_ob.
#                 Late night. Zira alone at the Ghostline workstation. Physical
#                 task varies by path (EMP: seeding Liora's ledgers across
#                 active nodes; OB: running an unnecessary diagnostic loop).
# cann.what_happened:
#   - Zira works. The work is the anchor. The variant task is chosen to fit the
#     path's emotional register — EMP honors Liora; OB refuses to stop.
#   - She replays the moment she chose Aeron. Not the on-screen commitment — the
#     half-second before it, where she could have said no.
#   - She performs the technical distinction between regret and not-regret.
#     Not-regret is a stance she is actively holding, which requires maintenance.
#     The diagnostic loop / ledger deployment is the maintenance.
#   - She names the cost function without a ceiling and identifies the absence
#     of the ceiling as her current problem.
#   - Variant closing thought per path.
#   - She finishes the task. She does not go to bed. She starts another task.
# cann.voice_profile:
#   - Technical vocabulary as emotional tool: cost function, stance, ratification,
#     maintenance, geometry. Zira's native language used at full honesty.
#   - No deflection voice — carryover from a3_int_05_zira_after_him_emp. She is
#     operating without her internal sarcasm buffer and does not comment on the
#     absence this time.
#   - The two path variants use different relational geometries. EMP closes on
#     unreachability — a fear of emotional distance. OB closes on stupidity — a
#     demand for strategic competence. Same commitment, different failure mode
#     she is guarding against.
# cann.reveal:
#   - Zira's commitment is structural, not performative. She reinforced it before
#     the commitment scene, reinforces it again after it, and is now running out
#     of load-bearing walls — the metaphor she does not say but that the interlude
#     enacts through pass-seventeen labor.
#   - "Not regret" as distinct from "regret" is the scene's central operation.
#     The distinction is load-bearing for Zira's Act 4 arc: when and whether
#     maintenance costs exceed the stance's structural capacity.
# cann.callbacks:
#   - a2_int_01_zira_signal_check: the unpatched exit plan. She never patched it.
#     This interlude is what happens after you stop trying.
#   - a3_int_05_zira_after_him_emp: the recognition. This interlude is the action
#     that follows the recognition.
#   - EMP variant: a3_s22_liora_execution_emp — the execution, Liora's ledgers,
#     the Ghostline-as-memorial promise Zira made on-camera.
#   - OB variant: a3_s20_you_dont_get_to_break_ob — the confrontation, the
#     hardening, the cost of Aeron choosing the OB path.
#   - Kai, implicit — the earlier cost function that did have a ceiling. Zira
#     does not name him here. His absence from this scene is the sign she is
#     past the comparison.
# cann.block_status:
#   - INTERLUDE. Path-gated by canon_get("path_state"). Single file, two
#     variants. No branching player choice. Transition only.
# cann.requires_followup:
#   - The ceiling of Zira's cost function: Act 4 thread. What is the load-bearing
#     wall that finally doesn't hold, and what does she do when it doesn't.
#   - EMP: the unreachability fear. Does Aeron recognize it? Does he reach?
#   - OB: the stupidity fear. Does Aeron make a strategic mistake she has to
#     watch? Does he make a strategic mistake she has to clean up?
#   - "I am specifically not regretting it" as a recurring Zira line — the
#     maintenance phrase.
