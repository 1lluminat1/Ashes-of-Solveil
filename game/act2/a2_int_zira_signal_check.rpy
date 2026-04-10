# =======================================================
# ACT 2 - Interlude: Zira — "Signal Check"
# File: a2_int_zira_signal_check.rpy
# Type: LI THOUGHT INTERLUDE (Zira)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_int_zira_signal_check"
$ scene_mark(_current_scene_id, "entered")

label a2_int_zira_signal_check:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, low, across the workshop bench. The Ghostline terminal glow in
    #         frame-left. Zira's hands in frame-right. Her face only twice — both
    #         times turned toward the side room where Kira sleeps.
    # LIGHTING: Faint blue off the terminal. A single bench lamp angled down. The
    #           side-room door is cracked — a thin line of warmer light.
    # SFX: Ghostline diagnostic hum — a steady, clean tone. Kira's breathing from
    #      the next room, faint but present. A fan somewhere in the workshop cycling.
    #      No music. Zira does not play music when she's thinking.
    # FACE: Zira — sharper than her public face. The sarcasm gone. The analytical
    #       set. Not tired. Focused.

    # scene bg zira_workshop_night with fade
    # show zira neutral_sharp at right
    # play ambient "audio/amb/workshop_low.ogg" fadein 1.5

    zthought "Diagnostic loop, pass four. Clean. Clean. Clean."
    zthought "Everything reports stable and I'm running it again anyway, because the hum is the closest thing to quiet I know how to make."

    zthought "Kira's still breathing. Checked twice. Didn't mean to."

    zthought "Triage list. The one I keep in the back of my head. Not the one on the wall."

    zthought "Non-negotiable: Kira."
    zthought "Non-negotiable: Ghostline core. The three nodes holding Renn's recording. If I lose them I lose him twice."
    zthought "Negotiable: everything I own. Everything I've built that doesn't have his voice on it. Every workshop I'd have to rebuild from burnt parts."

    zthought "I used to be able to finish that list in under a minute."

    zthought "The exit plan works off the triage list. I wrote it clean. Signal drop, false trail out of the south gate, Kira to the Murelli safe-house, me dark for six weeks. I timed it. It worked."

    zthought "It worked until three weeks ago."

    zthought "He got added. I didn't put him on. I just noticed he was there when I reread the list last Tuesday, and I didn't take him off, which is the same as adding him."

    zthought "The plan doesn't route around him. I ran it twice. Every path I built needs him gone first, and every simulation I run where he's gone first terminates early because I stop caring about the rest of the plan."

    zthought "That's a cascade failure. Signal noise in the decision tree. The kind of bug I'd patch out of a junior's build in ten minutes."

    zthought "I haven't patched it."

    zthought "I haven't patched it because patching it means writing him into the plan, and writing him into the plan means I've picked him, and I don't put people on paper before I'm sure."

    zthought "Sure enough to lose everything else."
    zthought "Sure enough that losing him would make the rest of the plan pointless."

    zthought "That's a long bandwidth to have reserved for someone without telling him."

    # Kira stirs in the next room. Zira's hand lifts from the terminal. Waits.
    # The breathing steadies. The hand comes back down.

    zthought "The loop is still clean. The plan is still broken."
    zthought "I'll fix it tomorrow."

    zthought "..."

    zthought "I said that yesterday."

    $ scene_mark(_current_scene_id, "completed")
    return

# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a2_int_zira_signal_check
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.placement: After a2_s17_building_something (the base montage with Kira).
#                 Late night. Zira alone in her workshop at the new base. Kira
#                 asleep in an adjoining cot.
# cann.what_happened:
#   - Zira runs a Ghostline diagnostic loop as self-soothing — the hum is the
#     closest thing to quiet she can produce.
#   - She reviews her internal triage list: non-negotiable losses (Kira, Ghostline
#     core with Renn's recording) vs. acceptable losses (everything else).
#   - Her clean pre-existing exit plan — built around the triage list — no longer
#     works, because Aeron has migrated onto the non-negotiable side without her
#     consciously moving him.
#   - Every scenario she runs where Aeron is eliminated terminates early because
#     she stops caring about the rest of the plan. She identifies this as a
#     cascade failure and has not patched it.
#   - She has not patched it because patching it means committing on paper, and
#     Zira does not put people on paper before she is sure.
#   - Kira stirs. Zira freezes until the breathing steadies. Then resumes work.
# cann.voice_profile:
#   - Private Zira: sharper, cleaner, more analytical than her public voice. The
#     sarcasm she deploys socially is almost entirely absent — there's no one here
#     to protect.
#   - Metaphors pulled from signal engineering: bandwidth, cascade failure, noise
#     in the decision tree, junior's build. Her emotional vocabulary is
#     technical because technical is the vocabulary she trusts.
#   - Pragmatic, not self-pitying. She names the problem as a bug and acknowledges
#     she is refusing to patch it. The refusal is the reveal, not the problem.
# cann.reveal:
#   - Zira has been planning her own exit from Phoenix the whole time. Not because
#     she doesn't believe in the mission — because she always has an exit. Exits
#     are how she was built.
#   - Aeron has broken the plan by becoming non-negotiable. Zira has not fixed the
#     plan because fixing it would mean acknowledging the commitment she has
#     already made.
#   - The commitment precedes the commitment scene. By the time Act 2 gives us the
#     on-screen choice, Zira's subconscious has already signed.
# cann.callbacks:
#   - Kira: the original non-negotiable. Zira's humanity as inherited responsibility.
#   - Renn's recording: his voice on the Ghostline nodes. The loss she survived and
#     planned around for years.
#   - a2_s17_building_something: the montage. Public Zira building. This interlude
#     is the private cost of being built into.
#   - Future: a3_int_zira_after_him_emp — the same triage logic runs again and is
#     quieter and more honest.
#   - Future: a3_int_zira_dont_regret_it — the decision this interlude refuses to
#     write down finally gets written.
# cann.block_status:
#   - INTERLUDE. No branching. No choice. Transition only.
# cann.requires_followup:
#   - The unpatched exit plan: does Zira ever fix it? When? By deleting it or by
#     writing Aeron in?
#   - Renn's recording on the Ghostline: structural callback. What happens to those
#     three nodes if the Ghostline ever goes dark.
#   - Kira-stirring beat: Zira's parental reflex as a thing she cannot turn off.
#     Seeds later Kira-centric scenes.
