# =======================================================
# ACT 3 - Scene 22a: The Board (Empathy Path)
# File: a3_s22a_tessa_after_liora_emp.rpy
# Type: TESSA BOARD BEAT -- after Liora's execution
# Fires after a3_s22. Tessa at her board. Aeron in the doorway.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s22a_tessa_after_liora_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s22a_tessa_after_liora_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Opens on the board. LIVING column, DEAD column.
    #         The camera watches Tessa write. Macro on the marker. Macro on the letters.
    #         When Aeron appears in the doorway: the camera stays on Tessa's back.
    #         It does not cut to his face until she turns.
    #         The rule-of-three beat: close on Tessa's mouth. Each repetition held.
    #         Final frame: the board with LIORA RYLAN on both columns. Hold.
    # LIGHTING: Medbay at night. Tessa's clip lamp on the board. Amber.
    #           The rest of the room is dark. The board is the only lit surface.
    # SFX: Loop -- medbay ambient. Low hum. Ventilation.
    #      One-shots -- marker uncap, marker on whiteboard (deliberate strokes),
    #      marker cap, Aeron's boot on the threshold (one step, then stop).
    # BLOCKING: Tessa at the board, back to the door. Aeron enters the doorway.
    #           He stops. She does not turn. She writes. Then she turns.

    # ========= VOICE BASELINE =========
    # EMP cadence. Tessa's board voice: plain, structural, the sentences that
    # sound like inventory counts and feel like eulogies. Short. The rule of three
    # fires for the first time on a name that matters to the protagonist.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MEDBAY - NIGHT]

    #scene bg_medbay_night_emp with dissolve
    #play ambient "sfx/ambient/medbay_night_low.ogg" fadein 2.0

    # ========== PHASE 1 -- THE WRITING ==========

    "Six hours."

    "Liora Rylan was alive six hours ago. She was alive when the letter was in Aeron's jacket. She was alive when Zira traced the courier marks. She was alive when Lyra recognized the handwriting in the Cathedral archive."

    "She was alive and now she is not and the board needs to know."

    "Tessa is at the board. The medbay is empty. The clip lamp throws amber light across the whiteboard surface and catches the ghost-text of old names beneath the current entries. The marker is in her right hand. The cap is in her left."

    "She uncaps the marker."

    "She writes on the DEAD column, below the last entry, in her small even capitals:"

    "L. I. O. R. A. space. R. Y. L. A. N."

    "Date. Today's date."

    "She caps the marker."

    "She stands still for three seconds. Then she uncaps the marker again."

    "She moves to the LIVING column."

    "She writes:"

    "L. I. O. R. A. space. R. Y. L. A. N."

    "Same hand. Same letters. Same name. On the other side."

    "She caps the marker. Sets it on the shelf below the board."

    tthought "She is on both columns."

    tthought "Because I do not know how to count a woman who was alive this morning. I do not have a methodology for that. The board has two columns and neither of them was built for a woman who was speaking six hours ago and is silent now."

    tthought "The board was built for the distance between alive and dead. It was not built for the distance between alive-this-morning and dead-this-evening. That distance is six hours and it is the longest distance on the board."

    # ========== PHASE 2 -- THE DOORWAY ==========

    "A boot on the threshold. One step. Then nothing."

    "Tessa does not turn."

    tthought "He is in the doorway. I know the weight of that step. I have been counting steps in this medbay for long enough to know which ones belong to which people, and that step belongs to a man who has just lost something he found three days ago."

    "She speaks without turning."

    t "I put her on both columns."

    "Silence from the doorway."

    t "She is on the dead column because she died today. She is on the living column because she was alive three days ago when you read her letter and her handwriting was the same as yours."

    "Still nothing."

    t "I will keep her on both columns until you tell me which one to stop."

    # ========== PHASE 3 -- THE RULE OF THREE ==========

    "She turns."

    "Aeron is standing in the doorway. He is not leaning on the frame. He is standing because standing is what he has left and if he stops standing he will not start again tonight."

    "She looks at him. He cannot speak."

    "She speaks for the board."

    t "Liora Rylan."

    "The name lands in the room."

    t "Liora Rylan."

    "The second time is quieter. Not softer -- the volume is the same. The room receives it differently."

    t "Liora Rylan."

    "Three times. The rule. Her mother gave it to her when she was seven and she has never once broken it and she is not breaking it now, not for this name, not for the name that matters most to the man standing in her doorway who cannot say it himself."

    "The three repetitions sit in the air between them."

    athought "She said it. She said her name three times."

    athought "I can't. I tried in the corridor and the word stopped in my throat like a bone. The name of my mother who was alive this morning and dead this evening and who wrote me a letter about pauses and I read it too late and she died anyway."

    athought "Tessa said it for me."

    # ========== PHASE 4 -- THE COUNT ==========

    "He enters the medbay. He stops in front of the board. He reads both entries."

    "LIORA RYLAN on the left. LIORA RYLAN on the right. The same name in the same handwriting in the same ink on the same whiteboard, separated by a column header and six hours."

    t "She kept six thousand names."

    "Aeron looks at her."

    t "Your mother. Her network. Zira told me -- the courier infrastructure, the registries, the names of displaced children. Six thousand names, Zira said. Maybe more."

    t "I keep a board with two columns."

    "She looks at the board."

    t "We are doing the same work."

    athought "We are doing the same work."

    athought "Tessa and Liora. The board and the network. Two columns and six thousand names. The scale is different and the work is the same and that is the sentence I am going to carry out of this room."

    "He stands beside her at the board. He does not touch her. He does not speak."

    "She does not ask him to."

    "The board holds LIORA RYLAN on both columns. The clip lamp burns amber. The medbay hums."

    "They stand there until the hum is the only sound and the standing is the only motion and the board is the only record that matters."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Tessa", trust=1)
    $ canon_set("liora.on_both_columns", True)
    $ npc_remember("Tessa", "put_liora_on_both_columns", tone="structural_grief")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s22a_tessa_after_liora_emp
# cann.chapter: Act III, Phase III -- Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After a3_s22 (Liora's execution). Same evening. Six hours after death.
# cann.what_happened:
#   - Tessa writes LIORA RYLAN on both columns of the board -- dead and living.
#   - Rule of three fires: "Liora Rylan" spoken three times.
#   - "I will keep her on both columns until you tell me which one to stop."
#   - Callback: "She kept six thousand names. I keep a board with two columns.
#     We are doing the same work."
#   - Aeron cannot say his mother's name. Tessa says it for him.
# cann.callbacks:
#   - Tessa's board ritual (a2_s14, a2_s16). The rule of three from her mother.
#   - Liora's 6000-name network (a3_s20 Story Keeper).
#   - The letter (a3_s18a). The handwriting. "She was alive three days ago."
#   - a3_s22: the execution. Six hours. The longest distance on the board.
# cann.requires_followup:
#   - canon_set("liora.on_both_columns") persists on the board through Act 4.
#   - a4_s06 (Tessa board evolved) reads against this state.
