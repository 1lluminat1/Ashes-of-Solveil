# =======================================================
# ACT 3 - Scene 22a: Before the Mirror (Obedience Path)
# File: a3_s22a_nyra_before_the_mirror_ob.rpy
# Type: NYRA STATE BEAT -- post-hunt processing
# Between s22 (the hunt) and s23 (bookend). Seeds a4_s07, a4_s24.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s22a_nyra_before_the_mirror_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s22a_nyra_before_the_mirror_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. OB precision. Opens on the war room table -- tactical
    #         markers still in position from the hunt op. The victory geography.
    #         Two-shot: Nyra and Aeron across the table. The table between them is
    #         the distance and the connection simultaneously.
    #         No close-ups until the final beat. The scene holds the middle distance.
    # LIGHTING: War room at post-op. Overhead strips at half-power. Blue-green tactical
    #           glow from the displays. The light of a mission completed. Cold.
    # SFX: Loop -- war room ambient. Post-op quiet. The machines still running.
    #      One-shots -- tactical marker (small click when Nyra repositions one),
    #      a distant door closing somewhere in the base.
    # BLOCKING: Aeron and Nyra at the war room table. Standing. Neither sits.
    #           The table is between them. The tactical display shows the completed op.

    # ========= VOICE BASELINE =========
    # OB cadence. Doctrinal. Short sentences. Nyra's register is precision tempered
    # by something she will not name. nythought + athought. The dialogue is spare.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - NIGHT]

    #scene bg_war_room_night_ob with dissolve
    #play ambient "sfx/ambient/war_room_post_op.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DEBRIEF THAT ISN'T ==========

    "The war room is quiet. The hunt op ended forty minutes ago. The operators are back. The supply depot is secured. The Echelon patrol that was supposed to be guarding it spent the night chasing seven phantom positions across three sectors."

    "Nobody died."

    "That sentence should feel like a victory. It does not feel like anything."

    "Aeron is at the tactical display. The markers are still in position -- seven feints, one real target, the supply line severed without a shot. The operation was clean. The operation was perfect."

    "Nyra is across the table. She has not sat down since the op ended. She has not removed her sidearm."

    ny "The operation was clean."

    a "It was."

    ny "No casualties on either side. The Echelon patrol will report confusion but not contact. They will not know what happened until the supply line fails to deliver in forty-eight hours."

    a "By then we'll have redistributed the materiel."

    ny "Yes."

    "The tactical display hums. The markers glow in their positions. The conversation should be over."

    "It isn't."

    # ========== PHASE 2 -- THE SHAPE ==========

    nythought "He planned that operation the way his father would have planned it. Seven feints. One real. The misdirection was Marcus Rylan's signature -- the seven-point scatter that Echelon Command used to use against insurgent cells before the Purge."

    nythought "He does not know he used his father's pattern. Or he knows and the knowing does not bother him. I cannot tell which is worse."

    ny "You used a seven-point scatter."

    "Aeron looks up from the display."

    a "It was the optimal configuration for the patrol density."

    ny "It was. It was also your father's preferred tactical pattern."

    "The room shifts. Not physically. The air between them tightens."

    a "I know."

    athought "I know. I chose it because it works. The fact that it works because my father designed it does not make it less effective."

    athought "Nyra is looking at me the way she looks at a soldier who has passed a test she was not sure she wanted him to pass."

    ny "You knew."

    a "I studied his operations at the Glass. Every commander did. His patterns work."

    ny "They do. That is not my concern."

    a "What is your concern?"

    nythought "My concern is that you used his pattern without hesitation. My concern is that the pattern worked perfectly and you filed the victory the way he would have filed it -- clean, efficient, already looking ahead to the next operation. My concern is that the man I am standing across from is becoming something his father would have recognized and approved of."

    nythought "And my concern is that I am helping him become it."

    ny "You are not your father."

    "The sentence lands between them on the table."

    a "I know that."

    ny "You are something your father did not predict."

    athought "Something he did not predict."

    athought "Meaning: something beyond his patterns. Something that uses his tools without being limited to his conclusions."

    athought "Or meaning: something worse than his patterns. Something that takes his tools and applies them with a precision he never had because he still had the pause and I trained the pause out."

    athought "Nyra is not going to tell me which she means. Nyra does not explain. Nyra states. The interpretation is the test."

    # ========== PHASE 3 -- THE ACKNOWLEDGMENT ==========

    "Nyra moves one tactical marker on the display. A small adjustment. The marker was already in position. She moves it anyway -- the gesture of a soldier who needs to do something with her hands while she says the next sentence."

    ny "We are becoming something."

    a "We?"

    ny "Phoenix. This cell. The command structure. The operations. We are becoming something that did not exist before the displacement and does not have a precedent in Echelon's files."

    ny "Your father built Echelon to project force. Kael inherited it and used it to project fear. You are building something that projects precision, and precision is harder to counter than either force or fear because precision does not leave evidence of itself."

    nythought "And I am the one who taught him precision. I brought the Doctrine. I brought the discipline. The thing he is becoming has my fingerprints on it as much as his father's."

    nythought "I need to be honest with myself about that."

    ny "The hunt was clean. That is good. But clean operations are not the same as good operations, and the distance between clean and good is where commanders lose themselves."

    a "You think I'm losing myself."

    ny "I think you are finding something. I do not yet know if the something you are finding is the thing we need."

    "She picks up the tactical marker she adjusted. Holds it for a moment. Sets it down."

    ny "You do not need my assessment tonight. You need rest."

    a "I could say the same to you."

    ny "You could. You would be correct."

    "Neither of them moves toward the door."

    athought "She is not leaving because she is not finished. And I am not leaving because whatever she is not saying is the thing I need to hear, and I have learned on this path that the things Nyra does not say are more important than the things she does."

    "The war room hums. The tactical display holds the shape of a perfect operation. The markers glow."

    "They stand on opposite sides of the table. The distance is precise."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Nyra", trust=1)
    $ npc_remember("Nyra", "acknowledged_hunt_op_trajectory", tone="doctrinal_unease")
    $ tp_seed("a4.nyra_mirror_seed")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s22a_nyra_before_the_mirror_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Between a3_s22 (the hunt) and a3_s23 (bookend before mirror). Post-op night.
# cann.what_happened:
#   - Nyra and Aeron process the successful hunt operation. Quiet. Doctrinal.
#   - Aeron used Marcus's seven-point scatter pattern. He knew. He chose it anyway.
#   - "You are not your father. You are something your father did not predict."
#   - Nyra acknowledges she is helping build what Aeron is becoming.
#   - "Clean operations are not the same as good operations."
# cann.callbacks:
#   - Marcus Rylan's tactical patterns (the seven-point scatter).
#   - The Glass Academy: where Aeron studied his father's operations.
#   - Nyra's Doctrine: the precision she brought to Phoenix.
#   - The pause: Aeron trained it out. Marcus still had it. The difference.
# cann.requires_followup:
#   - Seeds a4_s07 (Aeron and Nyra cold). The doctrinal unease deepens.
#   - Seeds a4_s24 (the mirror). "Something your father did not predict."
#   - tp_seed for the mirror moment in Act 4.
