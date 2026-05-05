# =======================================================
# ACT 3 - Interlude: Zira — "The Cycle"
# File: a3_int_zira_cycle.rpy
# Type: LI THOUGHT INTERLUDE (Zira, path-shared event, path-coded close)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_int_zira_cycle"
$ scene_mark(_current_scene_id, "entered")

label a3_int_zira_cycle:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, locked low on the Ghostline rig — keyboard, console, the
    #         queue indicator. Zira's face is mostly out of frame for the first
    #         two beats; we read her by her hands. One slow push to the screen
    #         when the ciphered stream resolves to a single word. One pull-out
    #         at the end to show the chair, the bench, the lamp, the room.
    # LIGHTING: Single bench lamp. Console glow. Both cool. Both steady. The
    #           workshop is asleep around her. It has been asleep for a long time.
    # SFX: The keys. The fan in the rig. The Ghostline hum — comfort tone, by now
    #      indistinguishable from her own breath. No music. No clock. The cycle
    #      runs without a metronome because the metronome is her.
    # FACE: Zira — neutral, working. The face she has used for this task before.
    #       The face she will use for this task again. Not grief. Not hope.
    #       Procedure.

    # scene bg zira_workstation_late with fade
    # show zira working_neutral at center
    # play ambient "audio/amb/ghostline_hum.ogg" fadein 1.5

    # ---- BEAT 1: assembling the fuel ----

    zthought "Tonight's pull: three fragments off the Mercer relay, two off the dead Echelon node from last week's intercept, one scrap from a Ghostline maintenance sweep that wasn't supposed to surface anything."
    zthought "Six items. Six is a good night."
    zthought "Six is enough to feed the cycle."

    # She lays them into the queue. Header check. Salt check. Order them by
    # decay rate so the freshest hits the cipher first.

    zthought "Header on the Mercer fragments looks dirty. I'll clean it on the way in."
    zthought "The maintenance scrap is probably nothing. Almost always nothing. I run it anyway."

    # ---- BEAT 2: the run ----

    # She starts the cycle. The console begins consuming the fragments.

    zthought "Cipher pass one. Pass two. Pass three."

    # The progress indicator works. The room does not change. Her hands do not
    # change. She does not lean forward. She does not lean back. She is not
    # waiting in any way a stranger would recognize.

    zthought "The cycle does not care that I am tired. The cycle does not care that I have done this before."
    zthought "Good. I built it that way."

    # ---- BEAT 3: the result lands ----

    # The console finishes. A single line of output resolves on the screen.
    # Zira does not move for a moment.

    "NULL"

    # Hold. The lamp does not flicker. The hum does not change. The word sits
    # on the screen the way it has sat on the screen before.

    "NULL"

    "NULL"

    # Nine seconds of nothing — by feel, not by clock. She does not count.
    # She does not need to count. Her body knows the duration.

    "NULL"

    # ---- BEAT 4: log the nothing ----

    zthought "Logging the result."

    # She types. Steady. Procedural. The log has a shape she has not changed
    # in a long time.

    zthought "Cycle complete. Fragments processed: six. Yield: null."
    zthought "Decay margin within tolerance. Cipher integrity nominal. No corruption flags."
    zthought "Queue cleared. Rig nominal."

    # She saves the entry. The log file is large. She does not look at the size.

    # ---- BEAT 5: the maintenance ----

    zthought "Sweep the temp directory. Wipe the working keys. Re-arm the listener for the next pull."
    zthought "Set the next window. Tomorrow's relay should give me at least two more fragments. The Echelon node is still leaking. I'll know more by morning."

    # She does the maintenance. The rig accepts it. The listener arms. The
    # comfort tone steadies. The room is the room.

    zthought "Tomorrow's pull is already drafted. Tomorrow's salt is already prepped."
    zthought "I will run this again."

    # ---- BEAT 6: the close ----

    # She does not stand. She does not close the terminal. She sits with the
    # rig the way someone else might sit with a candle.

    if canon_get("path_state", "UNSET") == "OB":
        zthought "Null is still data."
        zthought "Run again tomorrow."
    else:
        zthought "Still nothing."
        zthought "Fine. I know how to wait."

    # She reaches for the next file.

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_int_zira_cycle
# cann.chapter: Act III, mid-to-late phase
# cann.placement: Path-shared event, path-coded close. Plays as a quiet establishing
#                 interlude after the player has seen Zira engage with at least one
#                 Echelon-residue intercept. Late night. Workshop asleep. The
#                 Ghostline rig the only working surface.
# cann.what_happened:
#   - Zira assembles the night's fragment yield from routine sources (Mercer relay,
#     leaking Echelon node, Ghostline maintenance scrap). Six items. A good night.
#   - She runs them through the cipher. The cycle is procedural. Her body does not
#     recognize the work as suspense.
#   - The result resolves to NULL. The word holds on the screen for nine seconds —
#     she does not count, but her body knows the duration.
#   - She logs the null result with the same precision she would log a positive
#     yield. The log file is large.
#   - She performs the maintenance: sweep, wipe, re-arm, set the next window. The
#     next pull is already drafted. The next salt is already prepped.
#   - Path-coded final pair of interior lines:
#       EMP: "Still nothing." / "Fine. I know how to wait."
#       OB:  "Null is still data." / "Run again tomorrow."
#   - She reaches for the next file.
# cann.voice_profile:
#   - Procedural register. Technical vocabulary used flat, without ornament. The
#     same cost-function precision as a3_int_zira_dont_regret_it, but turned at
#     a different angle: maintenance not of a stance but of a ritual.
#   - No sarcasm buffer. No deflection. The interlude does not perform feeling;
#     it performs the absence of feeling, which is the operation Zira has built
#     to make the work survivable across a duration she does not name.
#   - The two path variants split on wound state. EMP texture: a pain Zira is
#     beginning to let herself recognize — "Still nothing" admits the silence is
#     a thing that hurts; "Fine. I know how to wait" is endurance worn honestly.
#     OB texture: colder, more functional, more self-punishing — "Null is still
#     data" is the rationalization that keeps the cycle running without permitting
#     the wound to surface; "Run again tomorrow" is the order she gives herself.
# cann.reveal:
#   - First read: a procedural night at the rig. Routine. Competent. Quiet.
#   - Second read (after a4_s20c_last_transmission): this is the ritual that has
#     been running for the entire game. Every Echelon intercept, every Ghostline
#     maintenance pull, every scrap of decay-margin signal Zira has touched on
#     screen has been fuel for this cycle. The yield has been null every time.
#     The interlude is the shape of nine years of null — without naming the nine,
#     because the canon notes carry the mirror to Tessa's count and Noelle's count.
#   - "I will run this again" is the sentence the broadcast eventually answers.
# cann.callbacks:
#   - a2_int_01_zira_signal_check: the rig, the workstation, the late-night Zira
#     who does not patch the exit. The cycle pre-dates the romance plot.
#   - a3_int_zira_dont_regret_it: the not-regret stance as maintenance. The cycle
#     is the same operation in a different domain.
#   - a4_s20c_last_transmission (EMP and OB): the broadcast lands inside this
#     ritual. The cycle is the load-bearing infrastructure under that scene.
# cann.block_status:
#   - INTERLUDE. Path-shared event. Path-coded final couplet via canon_get
#     ("path_state"). No branching player choice. Transition only.
# cann.requires_followup:
#   - Threaded foreshadowing zthoughts in 2-3 existing post-Echelon-encounter
#     scenes — the player should see Zira mention "the cycle," "the queue," "the
#     midnight pull" in passing, in voice, before this interlude reframes them.
#   - The eleven-year duration of the cycle is canon-locked in canon_notes_zira.md
#     and is named on screen in a4_s20c_last_transmission. Do not name the count
#     here. Do not let any character count it inside the interlude. The duration
#     is the silence; the silence is the scene.
