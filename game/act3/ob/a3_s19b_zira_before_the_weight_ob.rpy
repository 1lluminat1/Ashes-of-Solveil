# =======================================================
# ACT 3 - Scene 19b: Before the Weight (Obedience Path)
# File: a3_s19b_zira_before_the_weight_ob.rpy
# Type: ZIRA DARK BEAT -- solo interior monologue
# Between s19 (the weight) and s19a (the letter). No dialogue.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s19b_zira_before_the_weight_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s19b_zira_before_the_weight_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. The stillness of a room that is not being watched.
    #         Opens on Zira's workbench -- tools, relay components, the pressed flower
    #         in its place on the bench. The camera finds her hands first, then her face.
    #         The flower: one macro shot. She looks at it. Does not touch it. The camera
    #         does not return to it. That is the discipline.
    #         Final frame: wide. Zira small in the workshop. The tools around her like teeth.
    # LIGHTING: Workshop at night. Overhead strip at quarter-power. The blue-green of
    #           standby terminals. No amber. The OB palette does not offer warmth here.
    # SFX: Loop -- workshop ambient. Ventilation. A relay unit cycling on the bench.
    #      No one-shots. No human sounds except breath. The silence is the point.
    # BLOCKING: Zira alone at her workbench. She does not move from the bench for the
    #           duration of the scene. No one enters. No one leaves. Solo interior.

    # ========= VOICE BASELINE =========
    # OB cadence. Cold. Economic. Zira's sharpest interior register -- the version
    # of her that processes institutional violence through the language of systems.
    # zthought only. No spoken dialogue. She is alone and she is not performing.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WORKSHOP - NIGHT]

    #scene bg_workshop_night_ob with dissolve
    #play ambient "sfx/ambient/workshop_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE OVERWRITE ==========

    "Zira's workshop. The tools on the bench are arranged the way she arranges them -- left to right, smallest to largest, the organizational logic of a woman who learned to think in relay routes and has never found a reason to think differently."

    "The relay unit on the bench cycles through its standby pattern. She is not working on it. She is sitting in front of it."

    zthought "The board overwrite."

    zthought "Tessa's board. The war room. The header on the living column read LIVING until it didn't. Someone -- Aeron, Nyra, one of the command chain -- changed it. The word OPERATIONAL replaced the word LIVING and nobody in this room thought that was worth stopping for."

    zthought "I was in the room. I saw the header change. I did not stop for it either."

    zthought "That is the data point I am sitting with."

    "She picks up a relay component from the bench. Turns it in her fingers. Sets it down in the same position."

    zthought "OPERATIONAL. The word means: still functioning. Still useful. Still producing output that justifies the resource expenditure of keeping the unit intact."

    zthought "LIVING meant something else. LIVING meant: a person exists in the world and the world is different because they are in it."

    zthought "The replacement was not discussed. It was not debated. It was not even announced. One day the header said LIVING and the next day it said OPERATIONAL and the transition happened with the bureaucratic silence of a form being updated."

    zthought "I build networks. I know what it looks like when infrastructure replaces intimacy. I have seen it in relay systems -- the moment a courier route stops being a lifeline and starts being a logistics chain. The packets still move. The protocol still functions. But the thing the route was built for has been quietly replaced by the thing the route is useful for."

    zthought "That is what happened to the board."

    # ========== PHASE 2 -- THE FLOWER ==========

    "The pressed flower is on the bench. Between the third and fourth tool. It has been there since she put it there and she has not moved it and she has not explained it to anyone who has asked."

    "She looks at it."

    zthought "Selene gave me that. Before the displacement. Before the base shifted and the command structure hardened and the word OPERATIONAL replaced the word LIVING."

    zthought "It is a pressed winterbloom. They grow in the cracks of the lower-span architecture where the condensation collects. Selene found it on a walk she took alone and brought it back and put it on my bench and said nothing about it."

    zthought "That is the kind of gesture that does not survive the transition from LIVING to OPERATIONAL. That is the kind of gesture that the current command structure would classify as non-essential."

    "She does not touch it."

    zthought "I am not touching it because touching it would be a decision and I am not ready to make that decision. Touching the flower would mean I am keeping it for sentimental value. Not touching it means it is on the bench because it is on the bench. The distinction matters to me and I am aware that the distinction is the kind of thing that gets smaller every day I live inside a system that has replaced LIVING with OPERATIONAL."

    # ========== PHASE 3 -- THE ASSESSMENT ==========

    zthought "The letter is in the dead drop. I have not delivered it yet. The courier mark dates to the pre-Purge era and the handwriting says Marcus and the letter is either intelligence or it is personal and I will need to decide which before I hand it to a man who has been trained to treat everything as the former."

    zthought "On the EMP path he would sit down. On this path he will stand."

    zthought "I know that. I know the shape of the man I am serving under, and the shape has gotten harder in the last month, and the hardening is the thing I am trying to evaluate without flinching."

    zthought "The Ghostline still functions. My network still carries the packets. The couriers still run the routes. But the thing the network was built for -- the keeping of people, the preservation of names, the maintenance of something softer than survival -- that thing is getting harder to locate in the daily briefings."

    zthought "I am still running the network. I have not quit. I have not sabotaged. I have not leaked. I am operational."

    zthought "There is that word again."

    "The relay unit cycles. The workshop hums. The pressed flower sits between the third and fourth tool."

    zthought "I am operational. The network is operational. The base is operational."

    zthought "Nobody asked if we were alive."

    "She sits at the bench. She does not move. The tools are in order. The flower is untouched. The relay cycles."

    "The workshop holds her the way a system holds a component: in place, in function, accounted for."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", conflict=1)
    $ npc_remember("Zira", "processed_board_overwrite_alone", tone="cold_clarity")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s19b_zira_before_the_weight_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Between a3_s19 (the weight) and a3_s19a (the letter). Zira alone in the workshop.
# cann.what_happened:
#   - Zira processes the board overwrite: LIVING replaced by OPERATIONAL.
#   - "Nobody in this room thought that was worth stopping for."
#   - The pressed flower on the bench (from Selene). She looks at it, does not touch it.
#   - No dialogue. Solo zthought interior. OB register -- cold, economic.
#   - "Nobody asked if we were alive."
# cann.zira_state:
#   - Seeing the system clearly. The infrastructure replacing intimacy.
#   - The flower is the test case: sentimental value vs operational indifference.
#   - She is operational. She has not quit. That is not the same as being alive.
# cann.callbacks:
#   - Tessa's board: the header change from LIVING to OPERATIONAL.
#   - The pressed flower from Selene. Pre-displacement. A gesture that does not
#     survive the transition to the current command structure.
#   - The Ghostline: still functioning. The question is what it functions for.
# cann.requires_followup:
#   - The flower returns in a3_s19a when Zira delivers the letter.
#   - rel_bump conflict=1 tracks Zira's growing tension with the OB command structure.
