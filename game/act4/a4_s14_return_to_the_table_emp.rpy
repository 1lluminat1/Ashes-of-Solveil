# =======================================================
# ACT 4 - Scene 14: Return to the Table (Empathy Path)
# File: a4_s14_return_to_the_table_emp.rpy
# Type: TRANSITION / STATE SCENE — command geometry resolves
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s14_return_to_the_table_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s14_return_to_the_table_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Four movements, minimal.
    #         (1) The corridor. 40mm, locked, low. Aeron walking the ops wing
    #             corridor. Not behind him this time — three-quarters front.
    #             The camera watches him arrive rather than follows him there.
    #             The difference from s13 is the difference the scene is about.
    #         (2) The threshold. 35mm, locked, from inside the ops wing looking
    #             outward at the door. The door opens. Aeron appears in it. He
    #             does not stop this time. He walks in. But he walks in at a
    #             tempo that is not the tempo of a commander arriving to take
    #             a room. It is the tempo of a man entering a room that is
    #             already running.
    #         (3) The geometry. Wide, high-ish, almost a schematic — the ops
    #             table as shape. Selene at the head-adjacent position she
    #             took in s13 and has not left. Noelle at her left. Lyra at
    #             the near-right. Zira at the foot. Aeron's old chair at the
    #             head is empty and has a datapad on its arm now — somebody
    #             has put a pad there without claiming the chair, which is the
    #             room's way of saying the chair is not going to be reclaimed
    #             and not going to be erased. The camera finds the geometry
    #             before it finds the faces. The geometry is the subject.
    #             Aeron enters the frame and walks the long side of the table
    #             — the side he took in s13, the neutral side. He does not go
    #             to the head. He does not go past the head. He stops at the
    #             side chair three down from Selene. He pulls it. He sits.
    #             The camera does not push. Camera stays schematic.
    #         (4) The eye. One movement only. Once Aeron is seated — after a
    #             beat, maybe two — Selene looks up from the tactical layer
    #             she has been reading. Her eye finds his. The shot is a
    #             single two-shot, cut across the table, held for exactly the
    #             length of the look. Cut back to the geometry wide. That is
    #             the whole transaction. Nobody else in the room registers the
    #             look. Nobody else in the room is supposed to.
    # LIGHTING: Ops wing operational, same as s13. Overhead strips full, holo-
    #           table green wash on everyone's lower face. The lighting is
    #           doing the work it was doing twelve hours ago and it does not
    #           notice Aeron has returned. The room is running. The lighting
    #           is the lighting of a running room.
    # SFX: Ops ambient — tactical tick, comms relay chatter low, two datapad
    #      taps, Noelle's voice mid-paragraph as Aeron enters (she does not
    #      stop for him), a single clink of ceramic (somebody's cold cup on
    #      the bench behind the table). No music bed. One low held note under
    #      the eye-contact beat and out.
    # FX/COMP: THE EMPTY CHAIR AT THE HEAD. A datapad on its arm, face down.
    #          The pad belongs to no one in the scene — it is a working pad
    #          somebody left there when they needed both hands for the table.
    #          The object on the chair is the room's honest answer to the
    #          question of the chair. The chair is not being reserved for a
    #          returning king. The chair is also not being memorialized. It
    #          is a surface. A pad is on the surface. The pad will be picked
    #          up by somebody who needs it and put back somewhere else when
    #          they are done with it. That is the chair's new function.
    #          THE SIDE CHAIR. Three down from Selene on the long side. Not
    #          adjacent to anyone important. Not at the foot. Not at the
    #          head. A working chair. The chair any working analyst would
    #          sit in for a shift at the ops table. Aeron takes it.
    # BLOCKING: Aeron enters. Walks the long side. Does not break the tempo
    #           of the room. Reaches the side chair. Pulls it out. The metal-
    #           on-stone sound is audible but small. Nobody at the table
    #           turns. He sits. He does not reach for a datapad. He does not
    #           claim a working surface. For the first thirty seconds he is
    #           an observer at his own command table and this is the whole
    #           point of the seating choice.
    # FACE: Aeron — not restored. The 48-hour stand-down gave him sleep
    #       enough to feel the exhaustion instead of overriding it. His face
    #       is quiet but the quiet is not rest. It is the quiet of a man who
    #       has decided a small thing on the walk down and has not yet
    #       decided whether the small thing is going to hold when the first
    #       operational question lands on the table.
    #       Selene — she reads his entrance the way she reads everything,
    #       which is without moving. She does not greet him. She is in the
    #       middle of a sentence when he arrives and she finishes the
    #       sentence before she does anything about his being in the room.
    #       Noelle — she clocks him peripherally, does not pause her
    #       delivery. Lyra — she sees him and does not look away and does
    #       not smile. Zira — at the foot. Zira is the one who sees him
    #       choose the side chair. Zira is the one who knows what the chair
    #       means. Zira does not react. Zira files it.

    # ========= VOICE BASELINE =========
    # EMP cadence. Minimal dialogue — this is a load-bearing silence scene.
    # Noelle speaks operational English through the middle. Selene speaks
    # one line at the top of the scene (unfinished, continuing from before
    # Aeron's entry), one line in the middle (routine), and no line at the
    # end. No line at the end is the point. Aeron does not speak at all in
    # the scene's first three phases. He speaks once — late, small, and
    # about the work on the table, not about himself. Internal thought is
    # where the scene lives.

    # scene bg_ops_wing_corridor_day with dissolve
    # play ambient "sfx/ambient/ops_wing_full.ogg" fadein 2.0

    # ========== PHASE 1 — THE CORRIDOR ==========

    "Twelve-fifteen. Forty-eight hours after the ops wing door closed behind him."

    "Aeron is walking the ops wing corridor at a pace that is not the clean-fast pace of s13 and is not the clipped precision of the weeks before that. It is a walking pace. The walking pace of a man who has slept — not enough, not the way Tessa would call enough, but enough that his body is no longer running on the fuel of its own adrenaline."

    athought "The 48 hours was enough sleep to make me feel the exhaustion instead of override it."

    athought "That is a sentence I got from Tessa. She said it to me at the 36-hour mark when she came to check on me in quarters and found me sitting on the floor by the window because the bed had started to feel like a thing I was performing for her. She said: the sleep is not going to restore you. The sleep is going to show you the floor you were standing on."

    athought "I asked her what I was supposed to do with the floor."

    athought "She said: walk on it."

    "His boots are louder than they usually are on the ops wing stone. That is not because his tempo is loud. It is because the corridor is quieter than he expected. The corridor is quieter because the ops wing has been running without him for two full shift rotations and the people who work in the ops wing have settled into the tempo of a room that does not have to route around his footsteps."

    athought "Nobody is listening for me."

    athought "That is a thing I am going to have to hold in my sternum for the next several minutes without letting it become either a relief or a wound."

    "He is almost at the ops wing door."

    "He stops for a beat. Not a stop — a hesitation, the half-second length. The length of a man making a decision he has already made and confirming to himself that he has made it."

    athought "Selene said, in s02: you have to decide whether you are a commander or a chair. I decided in the medbay cot at oh-three-hundred this morning. I am not walking into that room to resume the chair. I am walking into that room to join it."

    athought "That is a sentence and I am going to find out in about ninety seconds whether it is a sentence I can spend."

    "He pushes the ops wing door open."

    # ========== PHASE 2 — THE THRESHOLD ==========

    # scene bg_ops_wing_table_day with dissolve

    "The ops wing is running."

    "It is running the way it was running before he walked in, because it was running before he walked in, and the small difference between the two states — running-then, running-now — is a difference only Aeron is tracking. Everybody else in the room is tracking the tactical layers."

    "Noelle is mid-sentence. A clean analytic sentence. The kind of sentence she delivers at the ops table the way other people deliver water."

    n "— so the Echelon signal on the eastern corridor is consistent with a rolling seventy-two-hour patrol refresh rather than a targeted sweep, which means the evacuation window on the Marigold cache is eighteen hours wider than we modeled this morning, which means we have latitude on the Marigold call and we do not have to make it before seventeen-hundred."

    "She does not look up at Aeron when he enters. She has clocked him peripherally — Noelle clocks everybody peripherally, it is one of the things that makes her an analyst — but the finishing of the sentence is the discipline of the room, and the discipline of the room is not interrupted by the arrival of a man at the door."

    "Selene is standing at the head-adjacent position she took in s13. She is reading the eastern corridor layer on the holo-table. Her hand is in the lower-left volume of the display, flicking one filter on and another filter off. She is also not looking at him. She is also not ignoring him. She is doing the thing she does when the scene she is in does not yet need her to react, which is to continue being at work."

    "Lyra at the near-right. Her hand is not on the table. Her hand is at her belt, thumb hooked through the band that has been unbuckled since s04 and has stayed unbuckled through the intervening scenes. She sees him. She holds the seeing. She does not smile. She does not frown. Her mouth is in the still shape it gets when she is waiting for a signal from him about what kind of moment this is."

    athought "She is letting me set the grammar. That is a Lyra thing and it is a grace I am going to spend later."

    "Zira at the foot of the table. Arms not folded this time. Hands flat on the table's edge, one thumb resting on a tactical key she has not pressed. She is watching him the way she watches a perimeter — full-field, without a focal point. She will pull focus to the thing she needs to pull focus to when the thing happens."

    athought "Zira knows. Zira is the only one in the room who knows what I am about to do, because Zira is the one who taught me that a door exists and Zira is the one who would see the shape of the decision before I put it in a chair."

    "Aeron does not stop at the threshold."

    "He walks into the room at the walking pace he had in the corridor."

    # ========== PHASE 3 — THE GEOMETRY ==========

    "The empty chair at the head is not empty the way it was in s13."

    "In s13, the chair was conspicuously empty — no datapad on its arm, no jacket on its back, deliberately unstaged. The absence of staging was the staging. The room was telling him that the chair was being reserved for a decision he did not get to make."

    "Today, the chair has a datapad on its arm. Face down. The pad does not belong to anyone in the scene in particular — it is a working pad, left on the chair's arm by somebody who needed both hands for the table and put it there because the chair's arm was the nearest flat surface. Aeron reads the pad in a single glance and understands it."

    athought "The chair is a surface now."

    athought "Somebody — Noelle, probably, or one of the night-shift analysts Noelle has been pulling up to the ops wing — left a working pad on it because they needed to set it down and the chair was the nearest place to set a thing down. The pad is not claiming the chair. The pad is not memorializing the chair. The pad is using the chair the way the room uses any flat surface during a working shift."

    athought "That is the answer the room has been writing to the question of the chair for the last forty-eight hours."

    athought "The chair is not reserved for me and the chair is not erased for me. The chair is a working surface in a working room. Somebody needed to put a pad down. They put it on the chair's arm. They will pick it back up when they need it again and put it somewhere else when they are done with it. The chair will survive being used as a pad-surface. The chair has survived worse."

    "He does not go to the chair."

    "He walks the long side of the ops table — the long side opposite Lyra, the neutral side he took at the threshold of s13 when he chose not to sit in his own chair. He walks to the third seat down from Selene. Not adjacent to her. Not at the foot opposite her. The working-analyst position a third of the way along the long side. A chair anybody would take for a shift at the table."

    "He pulls the chair out."

    "The sound of the chair's metal feet on the ops wing stone is audible. It is not loud. It is the sound a chair makes in a working room. Noelle does not stop her sentence. Selene does not move her hand. Lyra's thumb on the band-buckle stays at the buckle. Zira's hands on the table edge do not move."

    "Nobody turns."

    "Nobody comments."

    "He sits."

    # ========== PHASE 4 — THE FIRST THIRTY SECONDS ==========

    "For thirty seconds Aeron does not move."

    "He does not reach for a datapad. He does not flick a filter on the holo-table in front of him. He does not claim a working surface. He sits at the side chair with his hands on the arms of the chair and he lets the ops wing run."

    "Noelle finishes the Marigold paragraph. Starts the next paragraph — a Ghostline window on a relay in the lower tiers, Zira's pad, Zira reading as she listens."

    "Selene flicks a filter, flicks another filter, changes the depth of the tactical layer. Routine reading. She is in the layer where the new Rhea-Vestin shape has started to register at the edge of the western industrial corridor, though the panel has not yet named Rhea Vestin and won't for hours yet. Selene's hand is steady. Her face is composed."

    "Lyra reads a small handwritten note from her own pocket — a different note from the one in s13, a fresh one, and Aeron understands without being told that she has been writing these small handwritten notes all through the 48 hours he was away, and that the writing of them has been her version of the walk-the-floor Tessa prescribed him."

    "Zira at the foot. Zira is the only one in the room whose full-field watch has Aeron inside it. She is not watching him. She is including him. The difference is a Zira-specific distinction that Aeron has learned to read in the last two months and reads without needing her to move her head."

    athought "She sees me in the side chair. She knows what the side chair means. She is not going to acknowledge it and she is not going to not-acknowledge it. She is holding the knowledge in the way she holds the knowledge of the unlocked drawer. She is not going to perform it back at me."

    athought "That is the gift she is giving me right now. She is not making my seating choice be a scene."

    athought "Nobody in this room is making my seating choice be a scene."

    athought "That is the scene."

    "The tactical tick of the holo-table is the loudest thing in the room for a long moment."

    "Noelle is mid-paragraph on the Ghostline window."

    "Aeron listens."

    # ========== PHASE 5 — WHAT THE LISTENING COSTS ==========

    athought "I am sitting in a working chair at my own ops table and I am listening to Noelle brief the room on a Ghostline window and I am not running the brief."

    athought "The body-memory of running the brief is in my hands. My hands want to be on a tactical layer. My hands want to be flicking a filter at the depth Selene is flicking filters at. My hands want to be the hands at this table that are deciding which direction the sentence goes next."

    athought "My hands are on the arms of the chair."

    athought "I am keeping them there."

    athought "It is costing me. The cost is not heroic — the cost is the same cost any commander pays when a commander decides to listen instead of speak for a quarter-hour that he could have spent speaking. The cost is the friction of a body trained to run a room not running the room."

    athought "The friction is the point."

    athought "If I cannot sit in a working chair at my own ops table and listen to Noelle finish a Ghostline window without my hands finding a tactical layer to flick a filter on, then I am not actually doing the thing I decided to do on the medbay cot at oh-three-hundred. I am performing the thing. I can tell the difference between doing it and performing it because doing it costs me something in the muscle of my hands and performing it costs me nothing."

    athought "My hands cost me something right now."

    athought "Good."

    "Noelle reaches the end of the Ghostline paragraph."

    "She pauses — the analytic pause at the end of a paragraph that invites the room to push back on the analysis."

    "In s13, that pause was the pause the room used to decide whether to interrupt her. Today the pause is the same pause. The room has not changed its protocol because Aeron came back. The room is using the pause the way it has been using the pause for 48 hours."

    "Zira speaks first."

    z "Ghostline window on the lower-tier relay reads consistent with a thirty-minute operational slot, not forty-five. We had forty-five on the board this morning. Noelle has the thirty. I am backing her read."

    "Zira's voice is the foot-of-the-table voice. Clipped, precise, operational. She is answering Noelle's implied question. She is not looking at Aeron while she does it."

    sel "Thirty is tight for the Marigold exfiltration window we were going to fold into that slot."

    "Selene, without looking up from the filter she is flicking."

    sel "Noelle — if we cut the Marigold fold from the Ghostline window, what is the next available independent window for the Marigold?"

    n "Fourteen hours. End of the next rotation."

    sel "That is inside the eighteen-hour latitude we just established on the Marigold cache. I am going to recommend we cut the fold and run the Marigold on an independent window at the end of the next rotation. Zira — workable on the Ghostline side?"

    z "Workable."

    sel "Lyra — workable on the medics' rotation side? You have two field medics on the Ghostline relay and I do not want to burn them with a second tasking inside the rotation."

    l "Workable. Both medics come off the Ghostline at the end of the thirty-minute slot. I can hold them for six hours and deploy them to the Marigold independent window at the end of the rotation. They will be tired. They will not be dangerous-tired."

    sel "Thank you. Noelle — log the decision as a shared call, tagged to the four of us."

    "A beat."

    "Noelle's pen does not move."

    n "Five of us."

    "She says it without looking up."

    n "Aeron is at the table."

    "Selene does not correct her."

    sel "Five of us. Log it."

    # ========== PHASE 6 — THE EYE ==========

    "Selene's hand leaves the filter she was flicking."

    "She does not straighten. She does not step back from the table. She does the small head-lift that is the only movement her posture was going to allow her to make in a scene she has been running without him for 48 hours — the quarter-degree lift that brings her eyes up from the eastern corridor layer to the long side of the table three seats down from her."

    "Her eye finds his."

    "The look lasts about two and a half seconds."

    "There is no smile in it. There is no grief in it. There is no relief in it — Selene does not allow relief to show in an ops wing and has not allowed it to show since the Estrinian corridor in the year of the long winter. The look is the look of a teacher seeing a student make a move the student has been working on for six weeks and finally make the move cleanly in the room where the move was going to be graded."

    "The look is also — because Selene is Selene and because the teacher is also a person — the look of a woman in her forties seeing a man in his twenties take a side chair at a table he used to chair, and recognizing the specific shape of the decision that walked the man to that chair, and recognizing it the way she recognized Kael-at-24 recognizing a similar shape in a different room twenty-three years ago."

    "The look is not exactly the same as the look she gave Kael-at-24. The look she gave Kael-at-24 was given by a younger Selene. This look is given by a Selene who has been teaching for twenty-three years since."

    "The difference is in the eyes."

    "Aeron holds the look. He does not look away and he does not perform the look back at her. He lets it be a look. The look is an exchange of information — the information is: I saw. He returns the information — the information is: I know."

    "That is the whole transaction."

    "Two and a half seconds."

    "Selene's eye goes back to the eastern corridor layer."

    "Her hand returns to the filter she was flicking."

    "She flicks the filter."

    "The sentence picks back up."

    sel "Noelle, run me the Batch B projection on the eastern corridor with the Marigold decision folded in. I want to see if we still have the two-hour pre-rotation cushion."

    n "Running."

    # ========== PHASE 7 — AERON SPEAKS ==========

    "Aeron lets the room run on for another forty seconds before he speaks."

    "He speaks once."

    "The speaking is small and about the work on the table, not about himself."

    a "Noelle."

    n "Aeron."

    "She says it without looking up, in the same tone she has been using for the briefing. That is its own small gift and he registers it as one."

    a "The Batch B projection is going to read two minutes light on the pre-rotation cushion if you run it on the filter Selene has on the eastern corridor layer. The filter is set to the seventy-two hour rolling refresh and the Batch B model was calibrated to the ninety-six hour rolling refresh at the end of the last rotation. Flip the Batch B calibration to match Selene's filter before you run it or the cushion reads short."

    "A beat."

    "Noelle's pen pauses."

    n "Good catch. Flipping the calibration."

    "She flips it. She runs the projection."

    n "Cushion holds at two-twelve. We have the pre-rotation cushion."

    sel "Thank you, Aeron."

    "Selene says it without looking up. The thanks is not a ceremony. The thanks is the thanks she would give any analyst at the table who caught a calibration mismatch before the projection went bad."

    "Aeron nods — the small nod, the working nod, the nod that says received-and-acknowledged and does not say anything else."

    athought "I caught a calibration mismatch."

    athought "That is the entire contribution I am making to this ops wing right now. I caught a calibration mismatch. Selene thanked me for catching a calibration mismatch the way she would thank a Batch A analyst for catching a calibration mismatch."

    athought "The thanks is the same thanks. The thanks did not change because I am the commander of this rebellion."

    athought "The thanks is not supposed to change because I am the commander of this rebellion."

    athought "That is the work. The work is that the thanks does not change."

    # ========== PHASE 8 — WHAT EVERYONE NOTICED ==========

    "Nobody in the ops wing looks at the empty chair at the head of the table. Nobody in the ops wing has looked at the empty chair since Aeron sat down. The datapad is still face-down on its arm. Somebody — Noelle, probably, between paragraphs — will pick the pad up at the end of the shift and put it back on the analyst bench and the chair will be a chair again, available for any working analyst who needs a place to sit during a shift."

    "Nobody comments on where Aeron sat."

    "Everybody noticed."

    "The noticing is in the small not-quite-reactions at the edges of the frame. Zira's thumb — the thumb resting on the tactical key she had not yet pressed — lifted and resettled once, a small acknowledgement she has already filed. Lyra's hand on the band-buckle flexed and released once, the way Lyra's hand flexes and releases when she is updating a piece of her own internal Aeron-weather. Noelle's pen paused for a half-beat when Aeron sat, and then resumed — the half-beat was her noticing and the resumption was her deciding that noticing was enough and that she was not going to make the noticing a scene. Selene did not react at all in the first thirty seconds, and then did the eye-meet in Phase 6, and the eye-meet is everything she was going to do about it and more than she usually does about anything."

    "The whole room rearranged its internal map of the table in the thirty seconds after he sat down. The external map did not move. The external map is the same map it was when he walked in. The internal map is a new map and it is the map the room is going to run on for the rest of Act IV."

    athought "They all noticed. None of them commented. That is what the room is going to do about this from now on. The commenting would have been a favor to me — it would have let me know I had been seen, it would have let me perform a response, it would have let the decision become a scene I could then process. Nobody is giving me that favor. They are giving me the harder thing instead, which is the room running on the new map without acknowledging that the map changed."

    athought "They are treating the geometry as a thing that does not need to be said out loud, because saying it out loud would make it a ceremony, and a ceremony is a thing the commander performs, and the commander is not supposed to be the performer in this scene."

    athought "The commander is supposed to be one of the chairs."

    athought "The chair is one of the chairs."

    athought "I am one of the chairs."

    # ========== PHASE 9 — THE HOLD ==========

    "The scene does not close."

    "The scene continues, quietly, for the length of another paragraph of Noelle's briefing — the Batch B projection, the pre-rotation cushion, a small tag-in from Lyra about a medic rotation, a small tag-in from Zira about a Ghostline key."

    "Aeron listens."

    "Aeron does not speak again."

    "His hands stay on the arms of the side chair."

    "The costing is still costing him."

    "It is going to keep costing him for the rest of this shift, and the next shift, and the shift after that, because the muscle of a body trained to run a room is a muscle that takes weeks to retrain, not hours, and Aeron is going to sit in side chairs for a while before side chairs are the chairs his body reaches for without thinking about it."

    athought "I am going to feel the side chair every time I take it for the next two weeks. That is the price. The price is that the side chair is deliberate until it is not deliberate, and the un-deliberateness is a thing I have to earn by taking the side chair on purpose enough times that my body stops noticing."

    athought "My body is going to keep noticing for a while."

    athought "That is fine. Tessa would say that is fine. Tessa would say that is the point. Tessa said, in the medbay at oh-three-hundred this morning, when I told her I was not sure I could walk into the ops wing at twelve-fifteen and take a side chair without my hands going to a tactical layer — she said: if you cannot do it without your hands going to a layer, let your hands go to the layer, and sit down again tomorrow, and try again. She said: this is not a scene you pass. This is a posture you develop."

    athought "I am developing a posture."

    athought "The posture is: I am one of the chairs."

    # ========== PHASE 10 — THE SCENE ENDS IN THE MIDDLE OF THE WORK ==========

    "Noelle turns to the next paragraph of the briefing."

    n "Okay — next layer. The secondary medical corridor. Lyra, this one is yours. I have three questions and I am going to pace them."

    l "Pace them."

    "Noelle paces them."

    "The ops wing keeps running."

    "The scene fades on the wide schematic shot — the ops table as geometry. Selene at the head-adjacent. Noelle at her left. Lyra at the near-right. Zira at the foot. Aeron at the side chair three down from Selene on the long side. The empty chair at the head with a datapad face-down on its arm. Five chairs occupied. Five people working."

    "Aeron's hands are on the arms of the side chair."

    "Nobody in the room is the commander of the room."

    "Everybody in the room is working."

    "The scene ends on the geometry."

    "Fade."

    # stop ambient fadeout 2.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("aeron_returned_to_table_side_chair", True)
    $ flag("aeron_chose_distributed_command_geometry", True)
    $ flag("selene_eye_meet_acknowledgement", True)
    $ canon_set("aeron.command_geometry", "distributed")
    $ canon_set("ops_wing.head_chair", "working_surface")
    $ canon_set("aeron.side_chair_posture", "developing")
    $ npc_remember("Selene", "watched_aeron_take_side_chair_eye_meet_only", weight=3)
    $ npc_remember("Noelle", "logged_decision_as_five_of_us", weight=2)
    $ npc_remember("Zira", "saw_the_side_chair_did_not_comment", weight=2)
    $ npc_remember("Lyra", "held_grammar_for_aeron_at_return", weight=2)
    $ npc_remember("Aeron", "caught_a_calibration_mismatch", tone="working_analyst_contribution")
    $ rel_bump("Selene", trust=1)
    $ metric("aeron_command_mode", set_to=2)   # 0=singular, 1=delegating, 2=distributed
    $ tp_seed("a4.aeron.takes_side_chair")
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s14_return_to_the_table_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Twelve-fifteen of the day following the 48-hour council stand-down
#     from a4_s13. Aeron has slept inside the 48 hours — not fully
#     restored, but rested enough that he is feeling the exhaustion
#     instead of overriding it. Tessa visited him at the 36-hour mark
#     and at oh-three-hundred the morning of this scene. Both visits are
#     referenced only in internal thought.
# cann.what_happened:
#   - Aeron walks the ops wing corridor at a walking pace — not the
#     clean-fast pace of s13. He enters the ops wing. Nobody stops. The
#     room is in the middle of a Noelle-led briefing on the Marigold
#     cache evacuation window and a Ghostline lower-tier relay window.
#   - The empty chair at the head of the table now has a working
#     datapad face-down on its arm. The chair has been demoted to a
#     working surface in his absence. The room is neither reserving the
#     chair nor erasing it.
#   - Aeron does not take the head chair. He walks the long side and
#     takes a working side chair three down from Selene on the long
#     side. He sits. He does not reach for a tactical layer.
#   - For the first thirty seconds he listens. Noelle finishes the
#     Ghostline paragraph. Zira backs Noelle's read on the thirty-minute
#     slot. Selene folds the Marigold onto an independent window. Lyra
#     clears the medics for the independent window. Selene tells Noelle
#     to log it as a shared call tagged to the four of them. Noelle,
#     without looking up, corrects her: "Five of us. Aeron is at the
#     table." Selene accepts the correction without comment.
#   - Selene does the quarter-degree head-lift and eye-meets Aeron for
#     two and a half seconds. The look is the teacher-to-student
#     acknowledgement of a move cleanly made. That is the whole
#     transaction. No dialogue.
#   - Aeron speaks once, late in the scene, to Noelle. He catches a
#     calibration mismatch on the Batch B projection (Selene's seventy-
#     two hour filter vs the ninety-six hour calibration). Noelle flips
#     it. Projection holds. Selene thanks Aeron the way she would thank
#     any analyst. The thanks is identical to the thanks she would have
#     given a Batch A analyst. That identity is the point.
#   - Scene fades on the geometry wide — five working chairs around the
#     table, the empty head chair as working surface, Noelle moving to
#     the next paragraph.
# cann.aeron_state:
#   - Not restored. The 48 hours was enough sleep to make him feel the
#     exhaustion instead of override it. Quiet-but-not-rested face. He
#     has decided on the walk down that he will not resume the chair.
#     The decision is fragile until the first operational question and
#     then it holds.
#   - Internal thought runs the scene because the scene is externally
#     quiet. The internal thought names the cost explicitly — his hands
#     want to be on a tactical layer, his body is trained to run the
#     room, the side chair is deliberate until it is not deliberate and
#     the un-deliberateness is a posture that takes weeks to develop.
#   - He answers Selene's s02 framing directly in internal voice: "I
#     am not walking into that room to resume the chair. I am walking
#     into that room to join it." This is the structural answer to s02
#     where he reverted to singular command under pressure.
# cann.thematic_flags:
#   - The chair as working surface, not reserved throne. The datapad on
#     the arm is the room's honest answer to the question of the chair.
#   - Load-bearing silence. The scene is run by what nobody says. The
#     room's new internal map is established without a single line of
#     dialogue commenting on Aeron's seating choice.
#   - The noticing and the non-commenting as the harder gift. Nobody
#     makes his seating choice a scene because making it a scene would
#     let him perform a response. They give him the harder thing: the
#     room running on the new map without ceremony.
#   - "Five of us" — Noelle's correction of Selene's count. The smallest
#     possible confirmation that the distributed-command geometry now
#     includes Aeron as a peer node, not as a missing head.
#   - Tessa's "this is not a scene you pass, this is a posture you
#     develop" — the chapter-wide teaching that command-character is a
#     set of repeated choices, not a single clean decision.
# cann.character_moments:
#   - Selene: the quarter-degree head-lift eye-meet. Two-and-a-half
#     second look. No dialogue. Teacher-to-student acknowledgement of a
#     cleanly-made move. Compared directly to her Kael-at-24 memory —
#     same look given by an older Selene than the one who gave it to
#     Kael. The difference is in the eyes.
#   - Noelle: the "Five of us" correction. Delivered without looking up.
#     The smallest-possible inclusion move. She is the one who names
#     Aeron into the geometry. She is also the one who the calibration
#     mismatch happens with, so Aeron's one-line contribution lands at
#     her station.
#   - Lyra: hand on the unbuckled band-buckle flexes and releases once.
#     Holding grammar for Aeron on entry. Waiting for him to set the
#     scene's tone. Does not set it for him.
#   - Zira: at the foot, full-field watch. Her thumb on the unpressed
#     tactical key lifts and resettles once when Aeron sits. She sees
#     the side chair choice. She knows what it means. She does not
#     react externally. This is the Zira version of an acknowledgement.
#     Aeron reads it and internally thanks her for not making the
#     seating choice be a scene. Directly seeds the s15 workshop scene.
#   - Aeron: the hands on the arms of the side chair. The single small
#     operational contribution (calibration mismatch catch). The
#     receive-the-thanks-identical-to-any-analyst's-thanks. The
#     development of the posture instead of the passing of the scene.
# cann.callbacks:
#   - a4_s02_first_cracks_emp: Selene's "you have to decide whether you
#     are a commander or a chair." This scene is the structural answer.
#     In s02, Aeron reverted to singular command under pressure. In s14,
#     he takes the side chair. Same teacher, same table, different
#     choice. The scene is the graded version of s02's homework.
#   - a4_s10_what_selene_meant_emp: "delegate the question." Aeron now
#     delegates the chair as well as the question. The delegation has
#     extended from what-to-decide to who-decides.
#   - a4_s12a_she_is_not_just_tactical_emp: Selene's sister Ilene, the
#     teaching-as-keeping-Ilene-alive framework. Selene's eye-meet here
#     is a Selene-to-Aeron version of the same inheritance act — she is
#     teaching because the teaching is how she survives the losses she
#     cannot undo.
#   - a4_s13_protecting_exhaustion_emp: the 48-hour stand-down. Aeron
#     walking away from the ops wing in s13, closing the door behind
#     himself. In s14, he walks the same corridor back and does not
#     close the door behind himself — he walks into the room and the
#     room is running, and the running is the answer to whether the
#     room could run without him. It could. It did. It is.
#   - a1_s20_lower_spans_emp: Zira's "on your six." Zira in s14 is at
#     the foot of the table on his six in the new geometry — same
#     position, migrated into the ops wing.
#   - Tessa's a4_s05a "you are not a machine" — referenced in internal
#     thought. The oh-three-hundred medbay visit the morning of this
#     scene is implicit bridging material. Tessa's "this is not a scene
#     you pass, this is a posture you develop" is her chapter-end
#     teaching.
# cann.block_status: drafted
# cann.requires_followup:
#   - The side-chair choice is now canonical command-geometry. Any
#     downstream ops wing scene must treat Aeron as a peer node at the
#     table, not as the commander-who-returned. If a later scene
#     requires Aeron to speak with command authority, the authority
#     must be granted to him by the room in the moment, not assumed.
#   - The empty head chair as working surface is a persistent state.
#     Future scenes can place objects on it, move it, or have an
#     analyst briefly occupy it, but nobody should sit in it as Aeron's
#     replacement. The chair is not a chair anymore; it is a surface.
#   - The cost of the posture — Aeron's hands wanting the tactical
#     layer — should appear in downstream scenes as a small body-memory
#     tell for the next two scenes at minimum. The posture develops;
#     the development is visible.
#   - Selene's eye-meet seeds a later Selene/Aeron private scene that
#     lands the teacher-student acknowledgement in dialogue. Not this
#     scene and not s15 — it should arrive after the Rhea Vestin first
#     cut lands and forces a new decision.
#   - tp_seed a4.aeron.takes_side_chair — the distributed-command state
#     token for all downstream Act IV and Act V EMP scenes.
