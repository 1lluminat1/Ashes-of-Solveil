# =======================================================
# ACT 3 - Scene 23a: Before Liora (Obedience Path)
# File: a3_s23a_noelle_before_liora_ob.rpy
# Type: NOELLE STATE BEAT -- probability and love
# Between s23 (bookend) and s24 (Liora). Seeds "I love you as data" (Act 4).
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s23a_noelle_before_liora_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s23a_noelle_before_liora_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Opens on Noelle's terminal -- the probability model
    #         running. Numbers on the screen. Then the camera finds her face: composed,
    #         precise, looking at the data the way she looks at everything.
    #         When Aeron enters: two-shot across the terminal. The data between them.
    #         The final beat: close on Noelle's face. Something behind the precision.
    # LIGHTING: Analysis station at night. Blue-white terminal glow. Cool. Clinical.
    #           When Noelle speaks the key line, the light does not change. It should.
    #           The fact that it doesn't is the OB grammar working.
    # SFX: Loop -- analysis station ambient. Terminal processing. Cooling fans.
    #      One-shots -- keyboard (precise, fast), terminal output chime, chair turn.
    # BLOCKING: Noelle at her terminal. Aeron enters. He stands. She sits.
    #           The height difference is the scene's blocking thesis: she looks up
    #           at him to deliver the data that will hurt him.

    # ========= VOICE BASELINE =========
    # OB cadence. Noelle's register: the data-first voice that has learned to carry
    # emotion inside the numbers rather than alongside them. nthought + athought.
    # Dialogue is precise. Noelle does not waste words.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ANALYSIS STATION - NIGHT]

    #scene bg_analysis_station_night_ob with dissolve
    #play ambient "sfx/ambient/analysis_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE MODEL ==========

    "Noelle has been running the model for six hours. The meeting with Liora is scheduled for 0800. The variables are clean: Liora's known behavioral patterns from the courier network data, the psychological profile Noelle has built from the letter and the registry records, the nineteen-year gap, the son she left, the man he has become."

    "The model converges at 73%."

    nthought "Seventy-three percent probability that she refuses him."

    nthought "The methodology is sound. I have run it four times with different weighting on the emotional variables and the number stabilizes between 71 and 76. The median is 73. The confidence interval is narrow enough to trust."

    nthought "Liora Rylan left Marcus because she saw what he was becoming. Her son is now commanding a cell that uses his father's tactical patterns. The seven-point scatter from the hunt op is in the briefing file she will have been shown. If she reads her son the way she read her husband -- and the letter suggests she does -- she will see the trajectory."

    nthought "She will see what he is becoming. And she left the last man she saw becoming it."

    "The terminal displays the probability in a clean serif font. 73%. No decimal. Noelle does not use decimals when the audience is not technical."

    nthought "He needs to know this."

    nthought "That is not a tactical assessment. That is a personal one. He needs to know this because he is going to walk into that room tomorrow morning expecting -- hoping -- that the woman who wrote that letter will see him and want to stay."

    nthought "The data says she probably won't."

    # ========== PHASE 2 -- THE DECISION ==========

    nthought "I could withhold it."

    nthought "I have the authority to classify the model as operational analysis and restrict the distribution. I could tell him the meeting is set and let him walk in with whatever expectations he carries. The model would sit in my files. He would never know I ran it."

    nthought "He might be fine. The 27% is real. She might stay. She might look at him and see the pause instead of the trajectory and she might stay."

    nthought "But if she doesn't, he will walk out of that room having lost something he didn't know he was going to lose, and the surprise of the loss will be worse than the loss itself."

    nthought "I know this because I model surprise as a variable. The damage of an unexpected negative outcome is 1.4 to 2.1 times the damage of a predicted negative outcome. The prediction does not prevent the damage. It distributes it across a longer interval. It gives the system time to prepare."

    nthought "Withholding the model would be choosing his comfort over his clarity."

    nthought "I have decided I will not do that."

    "She saves the model. Closes the terminal output. Opens the door."

    # ========== PHASE 3 -- THE TELLING ==========

    "She finds him in the corridor outside the war room. He is standing with his back to the wall, looking at nothing. The posture of a man who is about to meet his mother for the first time in nineteen years and does not know how to prepare for it."

    n "Aeron."

    a "Noelle. It's late."

    n "I have something you need to see."

    a "Can it wait until morning?"

    n "No."

    "He reads her face. Noelle's face does not give much away -- but the nothing it gives away is a specific nothing, and he has learned to read the specifics."

    a "Go ahead."

    n "I built a probability model for the meeting. Liora's behavioral patterns from the courier data, the psychological profile from the letter and the registries, the nineteen-year gap, the tactical briefing file she will have received."

    a "You modeled my mother."

    n "I modeled the meeting. The probability that she refuses sustained contact is 73%."

    "The number lands."

    "He does not flinch. He has been trained not to flinch. But something behind his eyes reorganizes, the way a filing system reorganizes when a new category is introduced that invalidates the old sorting."

    athought "Seventy-three percent."

    athought "She looked at the letter and the courier data and the hunt op briefing and she built a model and the model says my mother will probably look at me and see my father and leave."

    athought "Again."

    a "Why are you telling me this?"

    nthought "Because."

    n "I am not telling you this to prepare you."

    "She pauses. Noelle does not pause for effect. She pauses because the next sentence is one she has been assembling for three hours and she wants the words in the exact order she chose."

    n "I am telling you this because if I didn't, I would be choosing your comfort over your clarity, and that is the opposite of what I promised."

    a "What did you promise?"

    nthought "He is asking because he does not remember me making a promise. He is right. I did not make it to him. I made it to myself, in the analysis station, at 0200, when the model converged and I saw the number and I had to decide what to do with it."

    n "I promised that I would not withhold data from you because the data is painful. I promised that the analysis I provide would be complete, not comfortable."

    n "Withholding this would be a form of cruelty I have decided I will not practice."

    athought "She is looking at me the way she looks at a variable she has decided to protect. Not with warmth -- Noelle does not do warmth the way Lyra does warmth or the way Tessa does warmth. She does something else. She does precision applied with such care that the precision itself becomes the tenderness."

    athought "She built a model of my mother refusing me and she brought it to me at midnight because not bringing it would have been a lie of omission and she does not lie."

    athought "That is the shape of what she is offering. It is not comfort. It is the refusal to let me be comfortable when comfortable is not accurate."

    # ========== PHASE 4 -- THE CLOSE ==========

    a "Seventy-three percent."

    n "Yes."

    a "And the other twenty-seven."

    n "The other twenty-seven is real. I do not discount it. The model accounts for variables I cannot quantify -- the letter, the pause, the handwriting. Those are emotional inputs and emotional inputs have wider confidence intervals than behavioral ones."

    n "The twenty-seven percent is where love lives in the model. I cannot measure it precisely. That does not make it less real."

    nthought "I said that. I said love lives in the model. I said it out loud in a corridor at midnight to a man who is about to meet his mother."

    nthought "I do not say the word love. I do not use it in briefings. I do not use it in analysis. I am using it now because the alternative is a sentence that is technically accurate and emotionally incomplete, and I have decided I will not be emotionally incomplete with him."

    nthought "Not about this."

    a "Thank you, Noelle."

    n "Do not thank me for the number. Thank me for bringing it to you instead of filing it."

    a "I'm thanking you for both."

    "She nods. One nod. Clean."

    "She turns back toward the analysis station. He watches her go."

    athought "Seventy-three percent. Twenty-seven percent."

    athought "She gave me both numbers. She gave me the wound and the hope in the same sentence and she did not soften either one."

    athought "That is what Noelle is. That is what she does. She gives you the complete data set and trusts you to hold it."

    "The corridor is quiet. The meeting is in eight hours."

    "He stands against the wall with both numbers."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Noelle", trust=1)
    $ npc_remember("Noelle", "gave_liora_refusal_probability", tone="precise_care")
    $ tp_seed("a4.noelle_love_as_data")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s23a_noelle_before_liora_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Between a3_s23 (bookend before mirror) and a3_s24 (Liora OB). Night before meeting.
# cann.what_happened:
#   - Noelle models Liora meeting: 73% probability of refusal.
#   - She tells Aeron because withholding painful data is cruelty she won't practice.
#   - "I am telling you this because if I didn't, I would be choosing your comfort
#     over your clarity, and that is the opposite of what I promised."
#   - "The twenty-seven percent is where love lives in the model."
#   - Seeds Act 4 "I love you as data" arc.
# cann.callbacks:
#   - Liora's letter. The handwriting. The pause as emotional variable.
#   - The hunt op: Marcus's seven-point scatter in the briefing file Liora will see.
#   - Noelle's analysis methodology: the damage of surprise vs predicted outcomes.
# cann.requires_followup:
#   - tp_seed("a4.noelle_love_as_data") -- the word "love" used in operational context.
#   - The 73% number can be referenced in a3_s24 (Liora meeting) and Act 4 Noelle beats.
#   - The promise (clarity over comfort) becomes Noelle's OB relationship thesis.
