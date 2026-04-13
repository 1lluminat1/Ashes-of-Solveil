# =======================================================
# ACT 3 - Scene 20a: Lyra Prays for the Hunt (Obedience Path)
# File: a3_s20a_lyra_prays_for_the_hunt_ob.rpy
# Type: LYRA OB ARC BEAT -- first outgoing blessing
# Between s20 (you don't get to break) and s21 (story keeper).
# Seeds a4_s14 (Lyra sanctifying violence).
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s20a_lyra_prays_for_the_hunt_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s20a_lyra_prays_for_the_hunt_ob:

    $ show_timeline("DAY 39", "04:00", "Phoenix Base — Altar Alcove")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Opens on Lyra's quarters -- small, sparse. The Anayet texts
    #         on the shelf. The prayer mat on the floor. The Band visible on her wrist.
    #         Close on the Band: it is buckled. She does not loosen it.
    #         The prayer: close on her mouth. The words are small. The camera holds.
    #         Final frame: Lyra standing. The prayer mat behind her. She has moved
    #         past it. She is facing the door, not the altar.
    # LIGHTING: Quarters at pre-dawn. No overhead. A single candle -- Anayet custom.
    #           The candle is the only light. OB palette: the warmth is thin, contained.
    # SFX: Loop -- quarters ambient. Base hum through the walls. Distant activity.
    #      One-shots -- the Band buckle (a small click that does not happen -- she
    #      does not unbuckle it), candle flame movement, her breath.
    # BLOCKING: Lyra alone in her quarters. She starts on the prayer mat. She ends
    #           standing by the door. The motion from mat to door is the scene.

    # ========= VOICE BASELINE =========
    # OB cadence. Lyra's OB register: the faith hardened into function. The warmth
    # is still there but it is being directed, not offered. lthought throughout.
    # Minimal spoken words -- the prayer itself and nothing else.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - LYRA'S QUARTERS - PRE-DAWN]

    #scene bg_lyra_quarters_predawn_ob with dissolve
    #play ambient "sfx/ambient/quarters_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE PREPARATION ==========

    "Lyra's quarters at 0400. The hunt op briefs in two hours. The operators have been selected. The routes have been mapped. Noelle's probability models have been run three times and the numbers are clean."

    "All that is left is the blessing."

    lthought "I have blessed the dead. I have blessed the wounded. I have blessed the displaced and the grieving and the ones who came back from the field with someone else's blood on their hands and needed a voice that did not flinch."

    lthought "I have not blessed an outgoing operator."

    lthought "That is a different act. The dead are past. The wounded are present. An outgoing operator is future -- a person who has not yet done the thing I am being asked to bless them for."

    "She is kneeling on the prayer mat. The Anayet texts are on the shelf. The candle is lit. The Band is on her wrist."

    "She checks the Band. The buckle is secure. She does not loosen it."

    lthought "On the empathy path the Band loosens. On this path I buckle it tighter and the tightening is a choice I have been making every morning for three weeks."

    lthought "The Band is discipline. The Anayet mothers wore theirs through the Long Walk -- through the cold, through the hunger, through the miles of walking toward something they were told did not exist. They kept the Band buckled because the buckle was the promise and the promise was the walking."

    lthought "I am not walking. I am kneeling in a room in a military base preparing to bless a person who is about to go out and do violence in the name of survival."

    lthought "The Band should probably come off for that."

    lthought "I am keeping it on."

    # ========== PHASE 2 -- THE PRAYER ==========

    "She closes her eyes. The candle flickers."

    lthought "The Anayet blessing for the outgoing is short. Three lines. The mothers used it when the young ones left the settlement for the first time -- not soldiers, travelers. The blessing was for the road, not the destination."

    lthought "The operators going out tonight are not travelers. They are going to a supply depot. They are going to take it. Someone may be standing in the way of the taking and the operators have been briefed on what to do if someone is standing in the way."

    lthought "I am going to say the blessing anyway."

    l "{i}Vel su theran anai. Vel su meret khal. Vel su aya.{/i}"

    lthought "Go in what seeks. Go in what holds. Go in what returns."

    lthought "The blessing does not mention the thing the traveler is going toward. It does not mention the thing the traveler might do when they arrive. It blesses the going, the holding, and the coming back."

    lthought "It does not bless the middle."

    lthought "That gap -- the unblessed middle -- is where the violence lives. The Anayet mothers did not build a prayer for violence. They built a prayer with a hole in it where violence could fit without being named."

    lthought "I used to think that was a failure of the tradition. A gap where the faith could not reach."

    lthought "I think now it was deliberate. I think the mothers knew that some things cannot be blessed and should not be blessed and the best a prayer can do is stand on either side of the unblessed thing and hold the edges."

    # ========== PHASE 3 -- THE RECKONING ==========

    "She opens her eyes. The candle is still burning. The prayer mat is beneath her knees."

    lthought "I am not stopping it."

    lthought "The hunt op will happen. The operators will go out. The supply depot will be taken or it will not. Someone may die or no one will. My blessing does not change any of that."

    lthought "I am being in the room with it. That is what the faith asks. Not to prevent. Not to permit. To be in the room with the thing that is happening and to keep the Band buckled and to say the blessing with the gap in the middle and to let the gap be the gap."

    lthought "The Anayet mothers would recognize this. They stood at the edge of the settlement and watched the young ones leave and they said the three lines and they did not follow. They did not try to control the road. They held the edges."

    "She stands. The prayer mat is behind her. She faces the door."

    lthought "I will go to the briefing room. I will stand where the operators can see me. I will not speak the blessing aloud -- they did not ask for it and the blessing is not for them. The blessing is for me. The blessing is the thing I am doing instead of the thing I cannot do, which is stop it."

    lthought "This is the first time."

    lthought "It will not be the last."

    "She blows out the candle. The room goes dark except for the blue-green base lighting bleeding through the walls."

    "She checks the Band one more time. Buckled. Tight."

    "She opens the door."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.lyra.first_outgoing_blessing", True)
    $ npc_remember("Lyra", "first_outgoing_blessing_before_hunt", tone="disciplined_grief")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s20a_lyra_prays_for_the_hunt_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Between a3_s20 (you don't get to break) and a3_s21 (story keeper OB).
#   - Pre-dawn, 0400. Before the hunt op (s22) briefing.
# cann.what_happened:
#   - Lyra's first outgoing blessing on OB path. Praying for operators going to the hunt.
#   - The Anayet blessing has a gap in the middle -- violence lives in the gap.
#   - "I am not stopping it. I am being in the room with it."
#   - The Band stays buckled. She does not loosen it. OB discipline.
#   - Seeds a4_s14 (Lyra sanctifying violence).
# cann.lyra_state:
#   - The faith is being bent toward function. The prayer is for her, not the operators.
#   - "The best a prayer can do is stand on either side of the unblessed thing."
#   - The gap in the blessing is deliberate. The mothers knew.
# cann.callbacks:
#   - The Band: EMP loosens, OB buckles tighter. Three weeks of the same choice.
#   - The Anayet mothers and the Long Walk. The blessing for the outgoing.
#   - The prayer gap: the unblessed middle where violence fits without being named.
# cann.requires_followup:
#   - canon_set("ob.lyra.first_outgoing_blessing") seeds a4_s14 (sanctifying violence).
#   - The prayer with the gap recurs in Act 4 as Lyra's OB spiritual crisis deepens.
