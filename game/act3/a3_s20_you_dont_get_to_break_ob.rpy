# =======================================================
# ACT 3 - Scene 20: You Don't Get to Break (Obedience Path)
# File: a3_s20_you_dont_get_to_break_ob.rpy
# Path: OB
# Character Focus: Zira (primary), Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s20_you_dont_get_to_break_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s20_you_dont_get_to_break_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. Two-shot framing throughout -- Zira and Aeron, equal weight.
    #         Neither person dominates the frame. The camera doesn't take sides.
    #         Opens on the ops corridor: narrow, functional. The architecture of a conversation
    #         that shouldn't be happening in a corridor but can't wait for a room.
    #         Close-ups: Zira's hands -- still. Her jaw -- tight. Her eyes -- committed.
    #         Aeron: profile. The mask. What Zira is looking at through the mask.
    #         Final shot: Zira walking away. The door. She doesn't slam it. Hold on the door.
    # LIGHTING: Corridor: cold overhead strips. Harsh. No warm practicals.
    #           The light is unflattering. Neither of them looks good in it.
    #           That's the point. This conversation isn't trying to be beautiful.
    # SFX: Loop -- corridor ambient. Ventilation. Distant base activity.
    #      One-shots -- bootfall on metal floor. Zira's voice echoing slightly in the corridor.
    #      The door closing. Soft. Mechanical. The absence of a slam.
    # FX/COMP: The corridor: narrow. Pipes overhead. The intimacy of a tight space
    #          with no room to retreat from what's being said.
    # BLOCKING: Zira intercepts Aeron in the corridor. She's been waiting.
    #           Not ambush -- intention. She chose this space because it's private
    #           and because neither of them can hide behind a table.
    #           Zira stands in his path. Aeron stops. They face each other.
    #           The conversation happens standing. No one sits. No one leans.
    # CANON: Zira confrontation. Not about love. About what he's becoming.
    #        She's seen Nyra's influence. She's seen the efficiency. She's seen the cold.
    #        The relationship strains but holds -- because Zira committed, and she doesn't uncommit.
    #        No player choice. The confrontation IS the scene.
    # FACE: Zira -- everything on the surface. She's not hiding. That's the bravery.
    #        Aeron -- the mask. What's underneath it. The fact that he's listening.

    # ========= VOICE BASELINE =========
    # Zira: Raw. Direct. No intel-speak. No Ghostline jargon. Stripped to the personal.
    # Aeron: Minimal. Listening. The rare OB scene where he lets someone talk AT him.
    # Neither voice is gentle. This isn't tenderness. It's confrontation from a place of investment.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - OPS CORRIDOR - NIGHT]

    #scene bg_ops_corridor_night_ob with dissolve
    #play ambient "sfx/ambient/corridor_hum.ogg" fadein 2.0

    # ========== THE INTERCEPT ==========

    "She's waiting in the corridor outside the war room. Leaning against the wall with her arms crossed. The posture of someone who decided to have this conversation three hours ago and has been rehearsing the opening line ever since."

    "She doesn't rehearse things. That's how he knows it's bad."

    z "Stop."

    "He does. Not because she commands it. Because the tone is one he hasn't heard from Zira before."

    a "Zira."

    z "Don't 'Zira' me. Not the operational voice. Not the command tone. Just -- stop for a second."

    athought "She's shaking. Not visibly. In the frequency she breathes at. Something fundamental in her rhythm is off."

    athought "I stop."

    # ========== THE CONFRONTATION ==========

    z "I need to say something and I need you to hear it. Not process it. Not file it. Hear it."

    a "I'm listening."

    z "No, you're not. You're standing there doing the thing you do where you look like you're listening and you're actually running tactical assessments on my emotional state."

    athought "She's not wrong."

    z "Stop it."

    "He tries. He's not certain he succeeds."

    z "I chose you."

    "The words land in the corridor like a dropped blade."

    z "After Selene. After what happened. After the funeral and the lie and the story we all agreed to tell. I chose you."

    z "Not because you were right. Not because you were good. Because I looked at every option and you were the one that kept the most people alive."

    z "I deleted footage for you. I stood in that front row and I didn't flinch. I built you a Ghostline that nobody in this city could match, and I did it because I decided you were worth the investment."

    athought "She did. All of it."

    z "And I'm watching you."

    "She steps closer. The corridor narrows."

    z "I'm watching you become something I didn't invest in."

    athought "The word 'invest.' She uses it the way other people use 'love.' The Ghostline is her language. Connections. Networks. The thing you build because you believe in what's on the other end."

    z "Nyra sits at your right hand now. Nyra's soldiers run your patrols. Nyra's methods are in the briefings. Nyra's language is in your mouth."

    z "'Precision is mercy.' That's her phrase. You said it yesterday in the ops review like you'd been saying it your whole life."

    athought "I did say that."

    athought "I didn't notice whose phrase it was."

    z "You haven't asked Lyra her opinion in two weeks. Tessa avoids the war room. Noelle watches you the way she watches data sets -- looking for the anomaly."

    z "And me?"

    "Her voice drops. Not softer. Closer."

    z "You give me assignments. Clean, efficient assignments. Like I'm a relay node, not a person."

    a "Zira--"

    z "I'm not done."

    "He closes his mouth."

    z "I chose you before. I'm choosing again."

    "She holds his gaze. Zira's eyes are dark, steady, and absolutely certain."

    z "But you don't get to break what I bet on."

    athought "Break what she bet on."

    athought "She means herself. She means the Ghostline. She means the version of me she chose to follow."

    athought "She means all of it."

    z "You want to be hard. Fine. Be hard. This city needs hard. I know that better than anyone -- I've been running intelligence through its veins since I was sixteen."

    z "But there's a difference between hard and hollow. And you're drifting toward hollow."

    a "I'm doing what needs to be done."

    z "That's what your father said. Word for word."

    "The sentence lands like a round to the chest."

    athought "She went there."

    athought "She earned the right."

    "Silence. The corridor hums. The ventilation pushes recycled air between them."

    a "What do you want me to do?"

    z "I want you to stop performing for her. I want you to remember that the people who stayed -- who actually stayed, not who arrived with a battalion and a pitch -- are the ones who saw you at your worst and chose not to leave."

    z "I want you to look at me when you give me an assignment. Not through me. At me."

    z "I want the man I invested in. Not the one Nyra is building."

    athought "She's right."

    # --- PLAYER CHOICE: This is the "do you let the human reflex win" moment ---
    menu:
        athought "I should say she's right. The sentence is in my throat."

        "You're right.":
            $ choice_and_dev(_current_scene_id, "zira_youre_right", "EMP", factor=2,
                note="OB Aeron admits Zira is right — rare human moment on the dark path.")
            $ rel_bump("Zira", trust=2)
            $ canon_set("ob.aeron.admitted_to_zira", True)
            "The silence holds. Zira's eyes widen a fraction."
            z "...Say that again."
            a "You're right. I'm drifting."
            z "(quiet) That's the first honest sentence you've given me in three weeks."

        "Your concerns are noted.":
            $ choice_and_dev(_current_scene_id, "zira_concerns_noted", "OB", factor=1,
                note="Command reflex wins. The human sentence dies in his throat.")
            "The silence holds. Zira watches him. Waiting for the response that would cost him nothing and mean everything."
            "He doesn't give it."
            "It's the wrong sentence. He knows it as he's saying it."
            z "Yeah. Noted."
            "Zira's jaw sets. Not surprise. Not even disappointment. Recognition."

        "I hear you. I don't know what to do with it yet.":
            $ choice_and_dev(_current_scene_id, "zira_hear_you", "EMP", factor=1,
                note="Honest middle — not denial, not full admission.")
            $ rel_bump("Zira", trust=1)
            z "That's better than 'noted.'"
            z "It's not enough. But it's better."

    # ========== THE EXIT ==========

    "She turns. Walks toward the corridor junction. Her footsteps are even. Measured. The walk of someone who said what she came to say and doesn't need to say it again."

    "She doesn't slam the door."

    "That's worse."

    "The door closes behind her with the soft mechanical click of a base built for function. No drama. No punctuation."

    "Just the click. And the corridor. And the ventilation."

    athought "She's right."

    athought "I knew before she said it. I've seen the trajectory. I've watched Nyra's language settle into my syntax like sediment. I've felt the distance growing between me and the people who were here first."

    athought "And I'm going to do nothing about it."

    athought "Because the operations are working. The patrols are clean. The intelligence is flowing. Echelon is off-balance for the first time in months."

    athought "The machine runs."

    athought "That should be enough."

    "He stands in the corridor. The ventilation hums."

    "It isn't enough. He knows that too."

    "He walks the other way."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ npc_remember("Zira", "you_dont_get_to_break", tone="strained_commitment")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s20_you_dont_get_to_break_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After the letter (s19a). Zira has been watching the deterioration.
#   - Night. Corridor intercept. She's been waiting to have this conversation.
# cann.what_happened:
#   - Zira confronts Aeron in the ops corridor. Not about love -- about what he's becoming.
#   - She catalogs the changes: Nyra's language in his mouth, Lyra sidelined, Tessa avoiding,
#     Noelle watching for anomalies. Zira herself treated like a relay node.
#   - "I chose you before. I'm choosing again -- but you don't get to break what I bet on."
#   - She names the difference: hard vs hollow. He's drifting toward hollow.
#   - "That's what your father said. Word for word." -- the Marcus comparison from someone
#     who earned the right to make it.
#   - He listens. Doesn't change. Says "Your concerns are noted." -- the wrong sentence.
#   - She walks out. Doesn't slam the door. That's worse.
#   - Internal: he knows she's right. He's going to do nothing about it.
# cann.aeron_state:
#   - Peak OB. He recognizes the truth but the command reflex overrides the human response.
#   - "Your concerns are noted" -- the sentence that proves her point.
#   - He knows. He's not going to act on knowing. The machine runs.
# cann.path_tracking:
#   - npc_remember for Zira: "you_dont_get_to_break", tone "strained_commitment"
#   - No player choice. No branching. The confrontation IS the scene. He listens and doesn't change.
# cann.thematic_flags:
#   - "Break what I bet on": Zira's language of investment. The Ghostline as relational metaphor.
#     She builds connections. She chose this one. It's fraying.
#   - "Hard vs hollow": the distinction Zira draws. OB Aeron's danger isn't cruelty -- it's absence.
#   - "Precision is mercy": Nyra's phrase in Aeron's mouth. The linguistic colonization.
#   - The door not slamming: restraint as severity. The quiet close is worse than violence.
#   - "Your concerns are noted": the command reflex that proves Zira's thesis in real time.
#   - The corridor: tight, functional, no room to hide. The architecture of honest confrontation.
# cann.character_moments:
#   - Zira: Everything on the surface. No hiding. She rehearsed this and she doesn't rehearse.
#     "I chose you. I'm choosing again." Commitment as confrontation.
#     "That's what your father said. Word for word." She goes there. She earned it.
#   - Aeron: Listens. Knows. Does nothing. The tragedy of self-awareness without self-correction.
#     The command reflex: "Your concerns are noted." The human buried under the operational.
# cann.callbacks:
#   - a3_s01: "I feel efficiency." Zira is naming what that became.
#   - a3_s06: Nyra's integration. "I came for the rebellion. I'm staying for him." The consequence.
#   - a3_s02a: Noelle's comparison to Marcus. Zira escalates it: "That's what your father said."
#   - a3_s19a: The letter. "I fell in love with the pause." Zira is asking about the same pause.
#   - The Ghostline as relational metaphor: throughout Zira's arc. Investment. Connection. Trust.
# cann.block_status:
#   - ANCHOR (always plays). No branching. Confrontation scene.
# cann.requires_followup:
#   - The strain persists. Zira stays but the distance is visible.
#   - Nyra's linguistic influence continues to be a marker of OB corruption.
#   - "Hard vs hollow" echoes in the Liora confrontation (s24).
#   - Zira's "That's what your father said" recurs when Liora says the same thing.
