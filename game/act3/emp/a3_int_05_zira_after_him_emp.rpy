# =======================================================
# ACT 3 - Interlude: Zira — "After Him"
# File: a3_int_05_zira_after_him_emp.rpy
# Type: LI THOUGHT INTERLUDE (Zira, EMP)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_05_zira_after_him_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_int_05_zira_after_him_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, very low. The alcove ceiling. Pipework. Her hand on his chest
    #         in frame-bottom. Her face enters frame only at the end — turned,
    #         looking at him. Not at us.
    # LIGHTING: A single emergency strip overhead, half-functional. Red. Then
    #           amber when it flickers. Her skin alternates between two warmths
    #           that don't belong to the same room.
    # SFX: Distant base systems through the ductwork. His breathing, slow,
    #      unguarded. The faint chirp of the extraction countdown on her wrist —
    #      subdued, far away, not yet urgent. No music.
    # FACE: Zira — still. Not peaceful. Still in the way a signal is still when
    #       the carrier tone has been cut and you haven't yet realized you're
    #       hearing nothing.

    # scene bg maint_alcove_postop with fade
    # show zira still_soft at left
    # play ambient "audio/amb/ductwork_distant.ogg" fadein 2.0

    zthought "Fourteen minutes to extraction."
    zthought "Fourteen minutes is a long time to be awake next to someone who is asleep."

    zthought "Scenario one: we walk out. Clean. Nothing on the tail. Six weeks of recovery and a line in my own log that says we got away with it."
    zthought "He's not in the line. He's in every word around the line."

    zthought "Scenario two: we walk out and they catch him on the ingress. Not me. Him. I watch it happen on a feed and I am useful in the way I am always useful and I survive the scene."
    zthought "I do not survive the rest."

    zthought "Scenario three: we don't walk out."
    zthought "Simplest branch. Fewest variables."

    zthought "I used to deflect at about this point. There's a voice I use inside my own head — a version of me with a cleaner jawline and a meaner sense of humor — and she comes in when the thinking gets close and she makes a joke about being melodramatic and I move on."

    zthought "She isn't here tonight."
    zthought "I noticed about three minutes ago. The silence where her is supposed to be."

    zthought "Kai used to get this close. Toward the end. The part I've been calling grief for six years was actually the moment I realized I had already agreed to lose him."

    zthought "I am in that moment again."
    zthought "I don't know how long I've been in it."

    zthought "I say his name in my head. Not out loud. Out loud would wake him and he has fourteen minutes to not be awake for, and I want to give him all of them."

    zthought "Aeron."

    zthought "It sits in my chest like a piece of equipment that came without a manual and doesn't match anything else in the kit and I can't throw it out because I already know what it's for."

    # The extraction chirp ticks. She does not move her hand.

    zthought "Thirteen minutes."
    zthought "My hand stays."

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_05_zira_after_him_emp
# cann.chapter: Act III, Phase II — Deepening
# cann.placement: After a3_s15_signal_under_fire_emp (maintenance alcove intimate
#                 scene). Post-scene. Aeron asleep beside her. Fourteen minutes
#                 until extraction. Zira is not asleep.
# cann.what_happened:
#   - Zira runs scenarios for the extraction — the way she runs signal
#     diagnostics. Methodical, probability-weighted, unsentimental in form.
#     Every scenario includes losing him.
#   - She notices her usual internal deflection voice — the sardonic counter-Zira
#     she uses to short-circuit feeling — has not arrived. She dates the absence
#     to three minutes ago.
#   - She thinks about Kai for the first time in weeks. Not the loss. The moment
#     before the loss, when she realized she had already agreed to lose him.
#   - She recognizes she is in that same moment again with Aeron and does not
#     know when she entered it.
#   - She says his name internally, not aloud, because aloud would wake him.
#   - The extraction chirp ticks. Her hand does not move from his chest.
# cann.voice_profile:
#   - The armor is off. Sarcasm absent. The signal-engineering metaphors remain
#     because they are her native tongue, not because they are deflection — here
#     they are the most honest language she has.
#   - She is naming the absence of her coping mechanism in real time. That is the
#     interlude's central technical achievement: Zira catching herself not
#     deflecting.
#   - Kai named for the first time since early Act 2. The Kai reference is not
#     trauma recitation — it is pattern recognition applied to herself.
# cann.reveal:
#   - The commitment scene in Act 2 was not the commitment. The commitment was
#     earlier and quieter, and Zira is only now catching up to it.
#   - The cost variable she did not calculate was not losing him. It was loving
#     him enough that losing him would end the usefulness she has always been
#     able to fall back on. She has spent her adult life surviving losses by
#     remaining useful. Aeron is the first loss that would make her usefulness
#     feel like cruelty.
#   - The inner deflection voice's absence is load-bearing. Zira's humor is a
#     defense system. When the system shuts down inside her own head, she cannot
#     pretend the feeling is smaller than it is.
# cann.callbacks:
#   - Kai: explicit reference. The agreed-to loss. Pattern repeat now recognized.
#   - a2_int_01_zira_signal_check: the unpatched exit plan. This interlude is the
#     quiet follow-up — she has stopped trying to patch it.
#   - a3_s15_signal_under_fire_emp: the scene this interlude follows.
#   - Ghostline metaphor: carrier tone cut, signal still, the feeling as
#     unmanualed equipment. Consistent with Zira's technical voice.
# cann.block_status:
#   - INTERLUDE. EMP path. No branching. No choice. Transition only.
# cann.requires_followup:
#   - The deflection voice: does she get it back? Does she want to?
#   - Kai reference: future Zira arc material. Does Aeron ever learn this name
#     in this depth?
#   - The hand on his chest: physical callback possible in later scenes.
#   - "I already agreed to lose him" as a Zira Phase III thematic line.
