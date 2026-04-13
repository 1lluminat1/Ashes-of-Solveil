# =======================================================
# ACT 4 - Scene 02: First Cracks (Empathy Path)
# File: a4_s02_first_cracks_emp.rpy
# Type: COUNCIL SCENE — Selene tests Aeron in front of the team.
# Matrix: Selene "argument that proves trust rather than breaks it"
#       + Aeron "first cracks in shared command reflex"
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s02_first_cracks_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s02_first_cracks_emp:
    $ show_timeline("DAY 43", "10:00", "Phoenix Secondary Base — War Room")


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("aeron_dossier", to_stage=3, source="a4_s02_first_cracks_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked on the command table for the opening wide. Then 32mm handheld,
    #         two-shot bias — Aeron and Selene in the same frame whenever possible.
    #         During the operational burst: tight on Aeron. Fast beats. The camera
    #         keeps up with him because everyone in the room is keeping up with him.
    #         When Selene speaks: the camera stops. Locks. Holds her. This is the beat
    #         the grammar hinges on. The stillness is the point.
    #         LI reactions: each gets one tight close-up. No pans between them.
    #         They are composed as isolated witnesses, not a jury.
    #         The choice moment: lock on Aeron's face. Hold.
    # LIGHTING: War room operational. Overhead strips — full. Tactical displays lit.
    #           The green wash from the holo-table on everyone's lower face.
    #           When Selene speaks her correction: no lighting change. The light
    #           does not help. The room does not dim for her. She is saying something
    #           that has to be said under operational light.
    # SFX: Loop — base hum, tactical display tick, the comms relay clicking through
    #      incoming low-priority traffic. One-shots: datapad taps, chair shift,
    #      Aeron's hand hitting the table edge (once, quiet, punctuation), the brief
    #      silence that follows Selene's correction.
    # FACE: Aeron — decisive in the opening burst. Focused. The old Aeron command reflex.
    #        Then, after Selene speaks: the micro-collapse. A half-second where the
    #        command mask slips and the grief underneath is visible. Then the choice.
    #        Selene — still, listening, eyes on him the whole time. Not hostile.
    #        Not proud. The face of a teacher who has been here before and is here again.
    #        Lyra — watching Aeron the way you watch a friend walk into weather.
    #        Zira — neutral. Assessing. One eyebrow slightly up.
    #        Tessa — the "I saw that" look. Quiet. Recording it for later.
    #        Noelle — logging. Her stylus moves during the correction beat.
    # BLOCKING: Full team around the command table. Selene and Aeron at the head —
    #           the two chairs from a3_s01, unchanged. Lyra left of Selene. Zira
    #           across. Tessa at the foot, closest to the board. Noelle at the
    #           terminal wing, her datapad in her lap.
    # CANON: First operational test of shared command under pressure. Selene delivers
    #        her first correction in front of the team. Choice node: EMP accepts the
    #        discipline, OB defends unilateral instinct. Both continue within EMP path
    #        but track internal drift.
    #        Callbacks: a3_s01 (accountability promise, "Don't let me become what I'm
    #        fighting"), a3_s23 (the plan — "you and I have command"), a4_s01 (the
    #        cipher slide — the silent ratification is now being tested in open air).

    # ========= VOICE BASELINE =========
    # EMP cadence, but under pressure. Sentences shorten. Selene's voice stays level.
    # Aeron's command burst is clean and fast — he is good at this, which is the problem.
    # The correction is quiet. Slow. Deliberate. Selene is not angry. Selene is exact.

    # --- VISUAL SETUP ---
    # [INT. SECONDARY BASE — WAR ROOM — MORNING]
    # Two hours after the cipher table scene. The team has gathered. The first
    # operational briefing of Act 4 under the new (post-broadcast) conditions.

    #scene bg_war_room_operational_morning with dissolve
    #play ambient "sfx/ambient/war_room_full.ogg" fadein 2.0

    # ========== PHASE 1 — THE ROOM ==========

    "The war room is full again."

    "Not the full of a month ago — full in the grieving, huddled way. Full in the operational way. Every chair at the command table is occupied. The tactical display is lit. Datapads are out. Pins on the map have tripled overnight."

    "Aeron sits in his chair at the head. Selene sits in hers. The two chairs from the briefing in a3_s01 — unchanged. Same configuration. Different room, different base, different world."

    athought "Same chairs. That matters."

    "Zira is across the table. Lyra to Selene's left. Tessa at the foot, closest to the board. Noelle at the terminal wing with her datapad in her lap."

    athought "Five of the people I trust most in the city are within arm's reach of me."

    athought "Most mornings that thought would steady me."

    athought "This morning it is doing something else. I cannot name it yet."

    # ========== PHASE 2 — THE PROBLEM SET ==========

    sel "We have three operational questions. In order: intake assignment, supply routing, Echelon mobilization."

    sel "Zira, intake status."

    z "Sixty-two walk-ins since yesterday morning. Forty-one vetted and cleared. Eleven pending secondary screen. Ten parked in intake pending skills interview."

    z "I am not equipped to run skills interviews at this volume. I was built to run a ghost network, not a recruiting office."

    t "I can take skills interviews for any walk-in who claims medical background. That's seven of the ten."

    n "I have flagged three of the cleared forty-one as statistically anomalous — their stated arrival paths do not reconcile with Echelon patrol data. Not necessarily infiltrators. Possibly opportunistic misreporting. I would like another screen on them."

    sel "Supply routing."

    l "The new numbers broke our supply plan. We're burning through rations twice as fast. The Forty-Second clinic run needs to happen today or we lose trauma capacity before tomorrow's shift."

    z "My courier network can hit three drop points in the northern corridors without exposure. Beyond that I need more runners, which means pulling fighters, which means thinning coverage on the eastern approach."

    sel "Echelon mobilization."

    n "They are repositioning. Marcus has pulled three patrol battalions off the outer rings. Consolidation pattern, not a strike posture — yet. The signal analysis is suggestive, not conclusive. I will have more in eighteen hours."

    # ========== PHASE 3 — AERON TAKES THE BURST ==========

    "The room pauses."

    "It is the pause where a decision is supposed to enter. In the old shape of the room, the pause belonged to Selene. In the new shape of the room, the pause belongs to whichever of them sees the answer first."

    "Aeron sees it first."

    athought "I can see it. All of it. Zira needs to stop doing intake. Tessa takes medical screening. Noelle re-runs the anomalous three with the broadcast-wave datasets. Supply split: clinic first, northern drops second, fighter pull deferred. Eastern coverage stays intact because the Echelon consolidation pattern says they are not threatening the east today."

    athought "I can see it in a single sweep. The way I used to see patrol gaps on a map in the Glass Academy. The shape of the problem and the shape of the answer in the same glance."

    athought "This is the thing I was trained for. This is the thing I am good at."

    "He speaks."

    a "Tessa, you take medical interviews — all seven of the claimed-medical walk-ins, plus any of the cleared forty-one you want a second pass on. Zira, you pull off intake entirely. Hand the remaining ten to Lyra for preliminary skills, you take back the Ghostline coordination full-time."

    a "Noelle, re-run the anomalous three against the broadcast-wave ingress logs. Priority flag. I want an answer by fourteen hundred."

    a "Supply: clinic run first. Zira, you route the Forty-Second corridor — keep it tight, three couriers max, no fighter pull. Northern drops move to tomorrow. We eat one day of depletion in the northern corridors to keep trauma capacity intact today."

    a "Eastern coverage stays where it is. Marcus is not pressuring east this cycle. Noelle's read on the consolidation is good enough for me."

    a "Contingency: if the anomalous three flag as infiltrators, full lockdown on intake, everyone clears out of skills interviews and we do secondary screens in quarantine. If Echelon shifts posture, Selene calls the full team back here and we redo the map."

    a "Move."

    athought "Clean. It is clean. I can feel the room take the shape of the orders. Zira is already standing. Tessa is reaching for her datapad."

    "It worked. The problem is solved. The plan is sound. Every face in the room is moving toward its task."

    "Except one."

    # ========== PHASE 4 — THE CORRECTION ==========

    "Selene has not moved."

    "She is looking at him. Not at the displays. Not at the team. At him."

    athought "She let me finish. She let me finish the entire sweep."

    athought "Oh."

    # VISUAL: Camera locks. No drift. Selene's face holds the frame.

    sel "Wait."

    "The word is quiet. But every body in the room stops the way bodies stop when the right voice says that word at the right pitch."

    "Zira, halfway out of her chair, sits back down."

    sel "Aeron. You made the right call."

    "A beat."

    sel "You made the right call, and you made it alone."

    sel "That is not what we agreed to."

    athought "The words go through the room the way a change in air pressure goes through a room. No one reacts visibly. Everyone has heard it. Everyone is waiting."

    athought "Lyra has stopped writing. Noelle's stylus is still. Zira has her hands flat on the table. Tessa is watching me the way Tessa watches patients who are about to break stitches."

    athought "And under all of it — under the surface where it actually lives — my father's voice, fourteen years ago, teaching me the First Principle of Command:"

    athought "The decision belongs to the one who sees it first. Hesitation costs lives. Consultation costs lives. The commander who consults is the commander who loses."

    athought "I made the right call."

    athought "I made it alone."

    athought "Both sentences are true. I want to argue with the second one. The fact that I want to argue with it is the data."

    # ========== PHASE 5 — THE DEFENSE ==========

    a "There wasn't time."

    "He says it before he can stop himself. The old reflex. The First Principle defending itself in his mouth."

    sel "There was time for you to decide."

    sel "That means there was time for me to be asked."

    athought "The logic is clean. There is no crack in it. The time it took me to see the full sweep was the time she needed to be consulted — if she had been asked, the consultation would have fit inside the decision window."

    athought "I did not ask because asking was not the reflex."

    athought "The reflex was: I see it, I speak it, the room moves."

    athought "That is the Aeries shape. That is Marcus's shape. That is the shape we said we were not going to use."

    # ========== PHASE 6 — THE ROOM HOLDS ==========

    "The other four LIs do not intervene."

    "This is important enough that he notices it. Lyra does not defuse. Zira does not joke. Tessa does not mother. Noelle does not clarify."

    "They are letting the two co-commanders have the conversation the shared command structure requires them to have."

    athought "They are not taking sides. They are respecting the shape. That is what this was supposed to make possible. A correction that happens in the open, in front of witnesses, without becoming a faction."

    "Lyra's eyes meet his for a half-second. She does not nod. She does not look away. She is present. That is all she is offering, and it is the correct offering."

    "Zira is expressionless, but she is tracking everything. Her eyes move between Aeron and Selene like she is logging the geometry."

    "Tessa's look is the 'I saw that' look. She is not going to say anything in this room. She will say it later, probably at the board, probably with her hands moving while she talks."

    "Noelle's stylus is moving now — not on her datapad, on a separate scrap of paper. She is logging the exchange by hand. He has seen her do this once before, in a3_s08. She does it when she does not trust the datapad to hold the weight."

    # ========== PHASE 7 — THE CHOICE ==========

    athought "She is waiting for me to respond."

    athought "Not to justify. She already closed the justification door. There was time."

    athought "To choose what the shared command means on the day after the day my mother died."

    # --- CHOICE: RESPONSE TO SELENE ---

    menu:
        "Selene's eyes. The team's silence. The cipher table still warm from this morning."

        "Accept the discipline.":
            $ choice_and_dev(
                _current_scene_id, "_accept_discipline", "EMP", factor=1,
                next_scene_label=None,
                note="Aeron hears the correction. The accountability promise holds. Shared command reflex forming."
            )
            jump .accept_discipline

        "Defend the instinct.":
            $ choice_and_dev(
                _current_scene_id, "_defend_instinct", "OB", factor=1,
                next_scene_label=None,
                note="Aeron still on EMP path but the shared command reflex is cracking. The lesson is harder."
            )
            jump .defend_instinct

    # ========== BRANCH A: ACCEPT THE DISCIPLINE ==========
    label .accept_discipline:

        athought "The sentence is simple. I only have to say it."

        a "You're right."

        "He says it in the same voice he used for the operational burst. Not softer. Not quieter. Not apologetic. Exactly as weighted as the orders. The team takes note of that weight."

        a "You are right. I made the call alone. I can tell you why — the reflex, the time, the training — but none of those reasons make the call shared."

        a "I will bring it to the table next time. Even if the window is narrow. Even if I already see the answer. Especially then."

        sel "That is what we agreed to."

        a "I know."

        "A beat."

        sel "Then we continue."

        "She nods. Once. Small. Not absolution. Acknowledgement. The nod of someone accepting a correction offered in good faith."

        "The room moves."

        "Zira stands again. Tessa reaches for her datapad. Lyra collects the skills interview list. Noelle's stylus goes back to her own datapad — the scrap of paper with the hand-log on it slides into her pocket, not discarded."

        athought "She kept the log."

        athought "Noelle kept a hand-log of this exchange and she is keeping it even after I accepted the correction."

        athought "She is not logging it because she expects me to fail. She is logging it because she is beginning to understand that accountability requires witnesses who do not forget the thing that was corrected."

        athought "Fine. Let her keep it."

        athought "I want it kept."

        $ flag("a4_first_correction_accepted", True)
        $ rel_bump("selene", 2)
        $ rel_bump("noelle", 1)
        $ npc_remember("selene", "correction_accepted_in_public", weight=3)
        $ npc_remember("noelle", "kept_the_hand_log", weight=2)
        $ npc_remember("tessa", "watched_aeron_accept", weight=1)
        $ npc_remember("lyra", "aeron_heard_her", weight=1)
        $ npc_remember("zira", "co_command_held", weight=1)
        $ tp_seed("a4.shared_command.holds")

        jump .after_branches

    # ========== BRANCH B: DEFEND THE INSTINCT ==========
    label .defend_instinct:

        a "I trusted my instincts."

        a "They were correct."

        "He says it evenly. Not aggressive. Not proud. Stating a fact."

        a "The call was right. The team is moving. The clinic run will happen. Trauma capacity stays intact. Consultation would have cost us minutes I did not have."

        "A beat."

        sel "I did not say the call was wrong."

        sel "I said it was made alone."

        sel "Those are different critiques."

        athought "She is not raising her voice. She is not shifting her posture. She is standing in the same spot she stood in when she said 'Don't let me become what I'm fighting' a hundred days ago."

        athought "She is keeping the shape. Even while I crack it."

        a "Then we will have different answers about what alone means when the window is narrow."

        "He does not look away when he says it. He is not trying to win. He is trying to hold a line that feels like it will hold him together if he holds it."

        "A long beat."

        sel "Then we will have this conversation again."

        sel "And again."

        sel "Until you hear me."

        "The words are not hostile. They are not warm. They are the voice of a teacher who has a lesson plan that runs for a year and is willing to run it."

        athought "She is not giving up."

        athought "She is also not pretending I accepted something I did not accept."

        athought "That is the shape of the promise holding even while I refuse to meet it."

        sel "Move on the operational plan. It is sound."

        "The team begins to move. More slowly than in branch A. The air in the room has weight now."

        "Zira stands, but her eyes flick between Aeron and Selene one more time before she turns away."

        "Tessa gathers her datapad and leaves without looking at him. The absence of her look is the look."

        "Lyra lingers the longest. Not to speak. To be visible. She wants him to see that she saw. Then she goes."

        "Noelle's stylus does not move. She has stopped logging. She has closed the datapad. The hand-log stays in her pocket."

        athought "She stopped logging because she does not yet know what category this goes in."

        athought "I am becoming uncategorizable to my own analyst."

        athought "Mother. I am trying. I am trying and I am failing the first test and she saw it and she is still standing at the table with me. That is either the thing that saves us or the thing that destroys us. I do not know yet which."

        $ flag("a4_first_correction_refused", True)
        $ flag("a4_command_reflex_cracking", True)
        $ rel_bump("selene", -1)
        $ rel_bump("tessa", -1)
        $ rel_bump("noelle", -1)
        $ npc_remember("selene", "correction_refused_in_public", weight=3)
        $ npc_remember("tessa", "the_absence_of_the_look", weight=2)
        $ npc_remember("lyra", "stayed_to_be_seen", weight=2)
        $ npc_remember("zira", "noted_the_hesitation", weight=2)
        $ npc_remember("noelle", "closed_the_log_uncategorized", weight=2)
        $ tp_seed("a4.shared_command.cracks")

        jump .after_branches

    # ========== CONVERGENCE ==========
    label .after_branches:

    # ========== PHASE 8 — THE PROMISE IN THE ROOM ==========

    "The team disperses to their assignments. Not fast. Not slow. The pace of people carrying a weight that is not the operational plan."

    "Aeron stays at the command table."

    "Selene stays with him."

    "Neither of them speaks. The silence is different in each branch — in branch A it is the silence of two people who have just confirmed an agreement; in branch B it is the silence of two people who have just scheduled a longer conversation."

    "In both branches, the accountability promise from a3_s01 is in the room."

    athought "Don't let me become what I'm fighting."

    athought "That is what she said to me the first morning of shared command. And I promised her we would watch each other."

    athought "This was the first watch."

    athought "The Act 4 lesson has started. The lesson is: sharing the weight is not a decision I make once. It is a decision I make every time the window is narrow."

    athought "That is going to be hard. That is going to be hard because I am good at deciding fast. That is going to be hard because I was trained by the person who is trying to kill me, and his voice in my mouth still sounds like competence."

    athought "I am going to have to learn to hear my own voice under his."

    athought "Not today. Today I only learned that the voices are still tangled."

    "Selene's hand is on the command table. Near his. Not touching. Present."

    "He looks at the hand. He looks at her."

    sel "One more thing."

    a "Yes?"

    sel "You have not eaten."

    "He blinks."

    sel "Tessa told me. Before you arrived this morning."

    athought "Of course she did."

    sel "Eat something before you do anything else. That is the first order of the day from your co-commander. Non-negotiable."

    "A beat."

    a "Understood."

    "She almost smiles. The corner of her mouth. Not a full smile. The smile of someone who is exhausted and is going to save the rest of the smile for later when it can mean something."

    # ========== CLOSING ==========

    "Outside the war room, the base continues the work of the morning. Runners in the corridor. The comms room filling. The clinic activating for the day."

    "Inside the war room, two people sit at a table with a cipher between them and a promise in the air and a small, cold sentence newly installed in both of their heads:"

    "The lesson has started."

    "And the lesson is going to cost something."

    # stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s02_first_cracks_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Two hours after a4_s01 (the cipher table). First full operational briefing of Act 4.
#   - 38 hours after Liora's execution.
# cann.what_happened:
#   - Full council: Aeron, Selene, Lyra, Zira, Tessa, Noelle at the command table.
#   - Three operational problems: intake assignment (62 walk-ins), supply routing (clinic
#     run priority), Echelon mobilization (Marcus consolidating three patrol battalions).
#   - Aeron sees the full sweep in a single glance and issues a clean, fast, unilateral
#     operational plan. Plan is tactically sound. Team begins to move.
#   - Selene stops the room with a single word: "Wait." She delivers her first correction
#     of Act 4 in front of the full team: "You made the right call. And you made it alone.
#     That is not what we agreed to."
#   - Aeron's first reflex is the Aeries defense: "There wasn't time." Selene closes that
#     door cleanly: "There was time for you to decide. That means there was time for me
#     to be asked."
#   - The other four LIs do not intervene. They watch. Each reacts in character.
#   - PLAYER CHOICE:
#       EMP branch: Aeron accepts the discipline openly. "You're right. I will bring it
#         to the table next time. Even if I already see the answer. Especially then."
#         Selene nods. "Then we continue."
#       OB branch: Aeron defends unilateral instinct. Selene: "Then we will have this
#         conversation again. And again. Until you hear me." Cold, not hostile.
#   - Both branches converge: after the team disperses, Selene tells Aeron he has not
#     eaten since yesterday morning (Tessa told her before the briefing). Aeron is ordered
#     to eat. "Understood."
# cann.aeron_state:
#   - Operating at high competence. That competence is the problem — it is shaped like
#     the Aeries training, and the Aeries training made him singular.
#   - Can hear Marcus's voice under his own when he gives clean commands. Knows this.
#     Cannot yet separate the voices in real-time.
#   - Internal Act 4 lesson articulated for the first time: "Sharing the weight is not a
#     decision I make once. It is a decision I make every time the window is narrow."
# cann.path_tracking:
#   - Empathy path. Both choice branches remain on EMP — OB branch tracks the crack
#     in the shared-command reflex without moving the overall path.
#   - EMP branch: flag("a4_first_correction_accepted"), rel_bump selene+2, noelle+1,
#     tp_seed("a4.shared_command.holds")
#   - OB branch: flag("a4_first_correction_refused"), flag("a4_command_reflex_cracking"),
#     rel_bump selene-1, tessa-1, noelle-1, tp_seed("a4.shared_command.cracks")
#   - npc_remember registered for every LI in both branches.
# cann.thematic_flags:
#   - "Don't let me become what I'm fighting" (a3_s01) meets its first operational test.
#   - The Aeries First Principle of Command ("The decision belongs to the one who sees it
#     first") is named inside Aeron's head and identified as Marcus's voice.
#   - Shared command as a reflex that must be built, not a rule that can be announced.
#   - Correction in public as a form of trust, not humiliation. Selene models it.
#   - Tessa tracking Aeron's not-eating — care as surveillance, surveillance as love.
# cann.character_moments:
#   - Aeron: fast, clean, and exactly wrong. The lesson begins.
#   - Selene: the correction without hostility. Teacher, not critic. "We will have this
#     conversation again" (OB) is the voice of someone who has time and is going to use it.
#   - Lyra: present, silent, does not defuse. In OB branch, stays to be seen. Quiet devotion
#     reshaped as witness.
#   - Zira: neutral assessor. In OB branch, notes the hesitation — Zira registers the
#     geometry of authority shifts as a ghost network threat model.
#   - Tessa: "I saw that" look. Does not speak in the room. In OB branch, the absence of
#     her parting look IS the look. She also fed Selene the intel that Aeron has not eaten.
#   - Noelle: hand-logs the exchange on a scrap of paper. In EMP branch, keeps the log
#     and files it. In OB branch, closes the log because the exchange is "uncategorized."
#     This is the seed of Noelle's a4_s03 realization.
# cann.block_status:
#   - Act 4 Chapter I, Scene 2. First operational test of shared command. Branching node
#     that tracks internal Aeron drift without path shifting.
# cann.requires_followup:
#   - Noelle's hand-logging behavior escalates in a4_s03 ("I am not a neutral observer").
#   - In EMP branch: next correction scene should raise the stakes.
#   - In OB branch: Selene WILL repeat the correction. "We will have this conversation
#     again" is a promise, not a threat. Track the repeat in a later Chapter I scene.
#   - Tessa's care-as-surveillance pattern (telling Selene about the not-eating) seeds
#     a later Tessa burden scene.
#   - The operational plan (clinic run, anomalous three, Marcus consolidation) all become
#     scene seeds downstream.
