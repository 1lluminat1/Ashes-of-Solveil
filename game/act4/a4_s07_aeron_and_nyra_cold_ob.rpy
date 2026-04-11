# =======================================================
# ACT 4 - Scene 07: Aeron and Nyra, Cold (Obedience Path)
# File: a4_s07_aeron_and_nyra_cold_ob.rpy
# Path: OB
# Type: NYRA STATE BEAT / INTIMACY (non-erotic, non-tender)
# Character Focus: Aeron, Nyra
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s07_aeron_and_nyra_cold_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s07_aeron_and_nyra_cold_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Two-shot across a small table. Neither character
    #         sits. The camera alternates between them in medium close-up,
    #         never cutting to wide until the final minute. When Nyra crosses
    #         the table, the camera holds on Aeron's chest -- her hand enters
    #         the frame flat against his sternum. We do not cut to her face
    #         for the grounding touch. The grounding is where the camera
    #         stays. It is the shot.
    #         Final beat: Aeron exits frame. The camera stays with Nyra alone.
    #         She does not watch him go. She walks to the table, picks up the
    #         decanter, walks to the small sink built into her quarters, and
    #         pours the rest of his drink out. The camera holds on the sink.
    #         Not on her face. The pour is the scene's ending.
    # LIGHTING: Nyra's quarters. Steel-blue register from a3_s12_the_oath_ob.
    #           Single practical: a wall sconce at low amber. The amber does
    #           not soften the room; it isolates the table. Everything beyond
    #           the table falls into near-black. The two of them are lit only
    #           at waist and above. The floor is not lit. The bed is not in
    #           frame.
    # SFX: Loop -- minimal. Nyra's quarters run quieter than the rest of the
    #      base by design. Low HVAC. A clock somewhere, metronomic, barely
    #      audible.
    #      One-shots -- decanter stopper (pulled, replaced). Liquid into two
    #      glasses. Glass set on wood. The small click of Aeron's boot heel
    #      when he re-shifts his stance. Nyra's footfalls across the carpet
    #      when she crosses to him -- four steps, unhurried.
    #      The hour of silence: we do not hear it. There is a hard cut
    #      between Nyra's line "I am here" and Aeron standing at the door
    #      about to leave. One hour has passed off-screen.
    #      Final beat: the pour. Liquid into a sink drain. That sound is
    #      held for three seconds.
    # FX/COMP: Nyra's quarters. Spare. A narrow bed, made. A small wooden
    #          table -- two chairs on opposite sides but neither character
    #          uses them. A decanter and two glasses on the table. A rank
    #          pin on a shelf, not worn. The small sink in the corner.
    #          No photographs. No books visible. A single tactical map
    #          folded and weighted with a stone, on the shelf.
    #          Aeron in his uniform, jacket on. The cuff stain from s06
    #          is visible on his right sleeve if the camera catches it --
    #          it does, once, when he raises the glass. The camera notes
    #          the stain without commenting on it. Nyra does not comment
    #          on it either. She has seen it. She has decided not to say.
    # BLOCKING: Aeron enters. Does not knock -- she expects him. Nyra pours.
    #           She hands him a glass across the table. He takes it. Neither
    #           sits. The entire verbal scene happens standing, with the
    #           table between them. In the final minute, Nyra walks around
    #           the table to his side. Puts her right hand flat on his chest.
    #           Holds it there. Does not kiss him. Does not move closer than
    #           the hand.
    #           Then the hour of silence -- off-screen.
    #           Then Aeron at the door, leaving on his own. Nyra still in
    #           the room. She does not walk him out.
    # CANON: OB Act 4. Aeron comes to Nyra in the night not for sex and not
    #        for tenderness, but to ask the one question he cannot ask anyone
    #        else and receive an answer that will not be softened. Nyra is
    #        the witness-without-flinch. The physical beat (hand on chest) is
    #        grounding, not possessive, not erotic. Aeron absorbs the answer
    #        and stays for an hour in silence. Then leaves on his own.
    #        Nyra pours out the rest of his drink.
    # FACE: Aeron -- not cracking. The mask has evolved. It has vocabulary
    #        now. The hand does not tremble. The voice is low and clear.
    #        When he says "my mother" the voice does not change pitch.
    #        Nyra -- the steel-blue register from the oath. She does not
    #        soften when he arrives and she does not soften when he leaves.
    #        She softens exactly once, and only at the hand. The hand is
    #        the softening. The hand is the entire scene's softness budget.

    # ========= VOICE BASELINE =========
    # Aeron: Cold, clear, Marcus-idiom. He has been rehearsing this question
    #        for weeks and has decided not to rehearse the answer. Internal
    #        athought between spoken lines -- procedural, not anguished.
    # Nyra: Ceremonial baseline of the oath, tuned one notch more honest.
    #       She is not performing for him. She is the one person in the
    #       base he does not need to perform for either. The honesty is
    #       the intimacy.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - NYRA'S QUARTERS - 0100]
    # Spare room. Steel-blue register, one amber sconce. Small wooden table.
    # Decanter. Two glasses. The sink in the corner. The bed not in frame.

    #scene bg_nyra_quarters_night_ob with dissolve
    #play ambient "sfx/ambient/quarters_minimal.ogg" fadein 2.0

    # ========== PHASE 1 -- ARRIVAL ==========

    "0100. The base has gone quiet -- night rotation, minimum staffing. The corridor to Nyra's quarters runs through the restructured wing: three checkpoints, none of them challenging him. His co-command walks unexamined."

    "He does not knock."

    "The door opens on her voice -- not surprised, not welcoming. Expectant."

    ny "Close it behind you."

    "He closes it."

    "Nyra is at the table. The decanter is already out. She has been pouring before he entered -- the stopper in her hand, the first glass half-full."

    athought "She knew I was coming tonight. I did not tell her I was coming tonight."

    athought "She was waiting for the night I would come. She had the decanter out in advance."

    "She pours the second glass. Sets the decanter down. Replaces the stopper with a small wooden click."

    "She slides one glass across the table. Does not walk it around to him. He closes the distance."

    "He takes the glass. Does not drink. Neither does she."

    ny "Sit if you want to sit."

    a "I don't."

    ny "Then stand."

    "They stand. The table between them. Her hands are flat on the wood at her side of the table. His hand is on the glass."

    # ========== PHASE 2 -- THE SILENCE BEFORE THE QUESTION ==========

    athought "I came here to ask her something. I have been composing the question for three weeks and I have not yet decided which version of it to use."

    athought "The short version is one sentence. The long version is four. The short version will get the honest answer. The long version will get a considered answer."

    athought "I want the honest one."

    "He does not speak. Neither does she. A full thirty seconds pass."

    athought "She is not going to prompt me. She does not prompt. That is part of why I came."

    "Nyra shifts her weight -- minimal, a rebalance. Her eyes do not leave his."

    nythought "He has been building the question since the night his mother walked. I have watched him carry it through four weeks of morning stand-ups, three operations, and a budget review. The question has weight. He has been testing whether the weight is the kind that can be set down."

    nythought "He has concluded it cannot. That is why he is here."

    nythought "I will not soften. Softening is the one thing he cannot afford tonight and the one thing he would accept if I offered."

    nythought "I am not going to offer."

    "Another ten seconds. Aeron raises the glass an inch, lowers it. Does not drink."

    "And then Nyra speaks, once, before he has found the form of his question."

    ny "She made her choice. It was not the one you needed her to make."

    "A small cut in the air. Aeron does not answer that. He does not acknowledge it. His eyes stay level with hers. The sentence lands and sits between them on the table like the glass."

    athought "She said that without me asking her to. She is front-loading the scene."

    athought "She is doing it to save me from having to lead with it. She is giving me the plain fact first so I do not have to assemble it."

    athought "That is mercy in her register. I am noting that."

    # ========== PHASE 3 -- THE QUESTION ==========

    "Aeron turns the glass a quarter-rotation in his hand. The amber light catches the liquid."

    athought "Ask her."

    athought "Ask her now before you talk yourself into the long version."

    a "If she had stayed."

    "He stops. Recalibrates. The sentence wants a subject he has not yet used in this room."

    a "If my mother had stayed."

    "Nyra's expression does not change."

    a "Would I have stopped."

    "Silence. The clock somewhere at the edge of audibility does its work."

    "Nyra considers it. She is not stalling -- she is actually considering. The consideration takes a long beat. Ten seconds. Twelve."

    nythought "He wants to know if love was a variable in the machine. If a body in the room would have been enough to change the trajectory."

    nythought "The honest answer is complicated and I am going to give him the simple one because the simple one is the part that matters."

    nythought "The complication will eat him later. The simple answer can be held now."

    "Her reply is measured. She does not rush it."

    ny "Yes. Briefly."

    "She lets that sit. Aeron does not move."

    ny "Then you would have resumed."

    "Another beat."

    ny "And hated her for having made you stop."

    # ========== PHASE 4 -- ABSORPTION ==========

    "The sentence enters the room and takes up residence."

    athought "Yes. Briefly. Then resumed. Then hatred."

    athought "She has mapped a week of my life I did not live and handed me the floor plan."

    athought "The floor plan is correct. I can feel it being correct. The correctness is a pressure on the back of my skull."

    "He does not look away from her. He does not set down the glass. His grip does not tighten on it."

    "But the mask has a small internal rearrangement. Not visible at this distance. He registers it himself."

    athought "A thing I suspected has become a thing I know. That is the shape of the cost."

    athought "I came here to convert suspicion to knowledge and she has done the conversion."

    athought "Now I owe her the next sentence."

    "He speaks quietly. Not softer -- quieter. The two are different."

    a "She knew that."

    "Nyra does not move."

    ny "That is why she walked."

    # ========== PHASE 5 -- THE GROUND UNDER THE SENTENCE ==========

    athought "She walked because she knew the resumption would come."

    athought "She walked because she knew the hatred would follow."

    athought "She walked to spare me the hatred. Or to spare herself the pause. I do not know which. I am not going to ask Nyra which, because Nyra does not know either, and because the answer belongs to my mother, and my mother is administratively in the dead column now."

    athought "I put her there six hours ago with my sleeve."

    athought "Nyra does not know I did that. I could tell her. I am not going to."

    athought "The stain is still on my cuff. She has not mentioned it. That is also mercy in her register."

    "He looks down at the glass. First time his eyes have left hers."

    "He does not drink. He sets the glass on the table."

    athought "I am not going to drink this. I did not come here for the drink."

    # ========== PHASE 6 -- NYRA CROSSES ==========

    "Nyra does not speak for a full minute. She watches him."

    nythought "He needs one more thing and he is not going to ask for it. He is going to stand there and run it alone if I do not give it to him."

    nythought "I am not going to give him tenderness. Tenderness is what his mother was and his mother is gone and the lesson he took from her departure is that tenderness is not structural."

    nythought "I am going to give him contact."

    nythought "Not the same thing. Contact is a stabilizer. It is a hand on a wall when the wall is the only thing keeping you upright."

    nythought "That is what I am. That is the whole offer."

    "She steps around the table. Four steps. Unhurried. The sound of her footfalls on the carpet -- soft, but each one audible in the room's quiet."

    "She stops at his side. Close enough that he could turn and be held if he turned."

    "He does not turn."

    "She lifts her right hand."

    "Places it flat against his sternum. Palm through the fabric of his uniform jacket. Four fingers and a thumb, evenly pressed. No grip. No claim. Not over the heart -- on the sternum, the bone, where the hand can feel the structure and not the pulse."

    "She does not move the hand. She does not stroke. She does not lean in. Her face is not near his face. The hand is the whole gesture."

    # ========== PHASE 7 -- THE OFFER ==========

    ny "You do not need a mother."

    "A beat. The hand stays flat."

    ny "You need a witness who will not flinch."

    "Another beat."

    ny "I am here."

    "Silence."

    athought "The hand is on my chest. It is not erotic. It is not tender. It is load-bearing."

    athought "She is telling me what she is. She is also telling me what she is not."

    athought "She is not offering to replace my mother. She is offering the opposite. She is offering to be the thing my mother was not, and to be it at the price of never being anything warmer."

    athought "I could refuse this. I could step back and her hand would fall and we would both pretend the last thirty seconds did not happen. She would let me pretend."

    athought "I am not going to step back."

    "He does not step back."

    "He looks down at her hand on his chest. He does not lift his own hand to cover it. He does not return the touch. He accepts it without reciprocating it."

    a "I know."

    "Two syllables. Low. Flat. He means all three things the sentence can mean: I know she is here. I know what she is offering. I know what I am becoming by accepting it."

    # ========== PHASE 8 -- THE HOUR ==========

    "Nyra holds the hand a moment longer. Then lowers it."

    "She does not return to her side of the table. She stays at his side. Half a step of separation. They are both facing the table now, looking at the glass he did not drink."

    "Neither speaks."

    "The hour passes here."

    # [OFF-SCREEN HOUR. Hard cut. The room's geometry is unchanged.]

    # [The lamp has not moved. The glass is where he set it. The second glass,
    #  Nyra's, is half-empty -- she took three sips across the hour, no more.]

    # [Aeron has not moved for the hour. He has stood at the table, at Nyra's
    #  side, and said nothing. She has not asked him to leave. She has not
    #  asked him to speak. She has stood with him.]

    # [This is the scene's silence. It does not need words. The cinema holds
    #  it with a single held frame and the clock audible at the edges.]

    # ========== PHASE 9 -- DEPARTURE ==========

    "Aeron shifts. The first movement in sixty minutes."

    athought "I am done. The question has been answered and the answer has been held. Holding it longer is hoarding."

    athought "Hoarding is the version of this that becomes tenderness. I am not going to let it become tenderness."

    "He turns from the table. Walks the three steps to the door. Does not look back at Nyra. Does not look back at the glass. Does not look back at the hand that is no longer on him."

    "At the door, he stops -- not to say anything. Just the last beat before the motion."

    "Nyra speaks to his back. Once."

    ny "Aeron."

    "He does not turn."

    ny "The answer does not change in daylight."

    "A beat."

    a "I know."

    "He opens the door. Closes it behind him."

    "The corridor swallows the sound of his boots."

    # ========== PHASE 10 -- NYRA ALONE ==========

    "The quarters hold Nyra."

    "She does not move for a moment."

    nythought "He will come back. Not tomorrow. Not this week. When the next question reaches the weight this one had."

    nythought "That is the terms of the witnessing. I do not initiate. He comes to me when the question has become unbearable alone. I answer. He absorbs. He leaves. I do not hold the door open afterward. The door is always open. That is different from holding it."

    "She crosses to the table. Picks up the glass he did not drink. Holds it for a second, weighing it in her palm."

    nythought "If I leave the glass, someone will find it tomorrow. A ration clerk, a quartermaster on inventory rounds. Someone will see two glasses poured and one untouched and make an inference. The inference will reach Tessa within six hours."

    nythought "I am not going to leave evidence."

    "She walks to the small sink in the corner."

    "She pours the glass out."

    "The liquid goes down the drain. The sound is held. Three seconds. Four."

    "She rinses the glass. Sets it upside down on the drying rack."

    "Crosses back to the table. Picks up her own glass. Takes one sip -- the fourth of the night. Sets it back down."

    nythought "He did not ask me to love him. He asked me not to flinch. That is a smaller request and a harder one."

    nythought "I have not flinched. I will not flinch."

    nythought "That is what I am for."

    "She turns off the amber sconce."

    "The room goes dark except for the sliver of corridor light under the door, and that fades when the corridor's night cycle steps down."

    "The quarters are dark. The table holds one glass. The sink holds one clean empty glass. The hand's print is gone from his uniform because his uniform is gone from the room."

    "The scene closes on the dark."

    #stop ambient fadeout 4.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Nyra", trust=1, attraction=0)
    $ canon_set("ob.nyra.witness_without_flinch", True)
    $ canon_set("ob.aeron.asked_the_question", True)
    $ canon_set("ob.aeron.received_the_answer", "yes_briefly_then_resumed_then_hated_her")
    $ tp_seed("a4.ob.aeron.asked_the_question_only_nyra_could_answer")
    $ flag("nyra_hand_on_sternum_grounding", True)
    $ flag("aeron_stayed_one_hour_silent", True)
    $ flag("nyra_poured_out_his_drink", True)
    $ npc_remember("Nyra", "witness_without_flinch_offer", tone="load_bearing")
    $ npc_remember("Aeron", "received_the_answer_about_his_mother", tone="cold_absorption")
    $ metric("ob.intimacy.cold", +1)
    $ metric("ob.aeron.marcus_idiom", +1)

    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s07_aeron_and_nyra_cold_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Act 4 OB. 0100. Nyra's quarters. Same night as a4_s06 (six hours after
#     Aeron wiped Liora's name from the board with his sleeve; the stain is
#     still on the cuff of the jacket he is wearing here).
# cann.what_happened:
#   - Aeron comes to Nyra at 0100. Not for sex, not for tenderness. For the
#     one question he cannot ask anyone else.
#   - Nyra has the decanter out before he arrives. She expected him, not
#     tonight specifically, but the night the question would reach weight.
#   - Neither sits. They stand on opposite sides of a small wooden table.
#   - Nyra front-loads, unprompted: "She made her choice. It was not the one
#     you needed her to make." Aeron does not answer that directly.
#   - Aeron asks his question: "If she had stayed -- if my mother had stayed
#     -- would I have stopped."
#   - Nyra considers it (long beat). Answers: "Yes. Briefly. Then you would
#     have resumed and hated her for having made you stop."
#   - Aeron absorbs it. "She knew that." / Nyra: "That is why she walked."
#   - Nyra crosses to his side of the table (four steps, unhurried). Places
#     her right hand flat on his sternum -- not heart, sternum. Bone, not pulse.
#     Grounding touch, not possessive, not erotic, not tender. Does not kiss
#     him. Does not lean in. The hand is the entire softness budget.
#   - Nyra: "You do not need a mother. You need a witness who will not flinch.
#     I am here." / Aeron: "I know."
#   - He stays one hour, not speaking. She does not ask him to leave. She
#     does not ask him to speak. They stand at the table. (Off-screen via
#     hard cut -- the cinema holds the silence without dialogue.)
#   - Aeron leaves on his own. At the door, Nyra says once: "The answer does
#     not change in daylight." Aeron: "I know." He exits without turning.
#   - Nyra alone: pours the rest of his untouched drink into the sink.
#     Rinses the glass. Sets it on the drying rack. Takes one sip of her own.
#     Turns off the sconce. The scene closes on darkness.
# cann.aeron_state:
#   - The mask has evolved. It has vocabulary now. Marcus-idiom competence
#     at full baseline. The hand does not tremble. The voice is low, clear.
#   - He says "my mother" once, late. Until then: "she." The single usage
#     is the crack in the economy of the scene.
#   - He accepts Nyra's contact without reciprocating it. He does not return
#     the touch. "I accept it without reciprocating it."
#   - He registers, internally, that he put his mother in the dead column
#     six hours earlier with his sleeve. He does not tell Nyra. The stain
#     is still on the cuff; she sees it and does not mention it.
#   - "I know" carries three meanings: I know she is here, I know what she
#     is offering, I know what I am becoming by accepting it.
# cann.nyra_state:
#   - Steel-blue register from a3_s12. Tuned one notch more honest because
#     the audience is Aeron alone and the ceremony is private.
#   - "She is not going to soften. Softening is the one thing he cannot
#     afford tonight and the one thing he would accept if I offered."
#   - The hand-on-sternum is the entire scene's softness budget. Explicitly
#     not erotic, explicitly not a claim, explicitly grounding. "A hand on
#     a wall when the wall is the only thing keeping you upright."
#   - Her doctrine of witnessing: "I do not initiate. He comes to me when
#     the question has become unbearable alone. I answer. He absorbs. He
#     leaves. I do not hold the door open afterward. The door is always
#     open. That is different from holding it."
#   - The pour-out: operational security first (a glass found by a clerk
#     reaches Tessa in six hours), but also the ritual close of the scene.
#     The drink he did not drink was a proposition he did not accept. She
#     does not hoard the evidence of what didn't happen.
# cann.thematic_flags:
#   - OB Act 4 thesis: "Violence Normalized." Intimacy under the regime is
#     cold, transactional, structural, load-bearing. The hand on the sternum
#     is the route's answer to "what does affection look like when softness
#     is infection." The answer: it looks like contact without warmth.
#   - "Why didn't they leave?" -- Nyra's answer, unspoken but legible: there
#     is nowhere to leave TO. The witness-without-flinch is the only thing
#     the regime allows that is not surveillance. That is why he stays.
#     That is why she stays. Not love. Clarity.
#   - Aeron's mother is named only once, and only as "my mother." Liora's
#     name is not spoken in this scene. That is deliberate. The scene pairs
#     with a4_s06: there he wiped the name with a sleeve, here he refuses
#     to say it aloud. The administrative burial and the verbal burial are
#     the same burial in two forms.
#   - Nyra's line "She made her choice. It was not the one you needed her
#     to make." is the route thesis rendered as a personal accounting.
#     Liora's refusal in Act 3 is re-framed in OB terms: her choice was a
#     refusal to be a brake. She was not an obstacle to the regime. She
#     was an obstacle to her son's uninterrupted descent -- and she declined
#     to be that obstacle because she knew the pause would only have been
#     a pause.
#   - The hour of silence is the scene's spine. Not a gap. A weight.
#     OB intimacy IS the held silence at the table. The words are the
#     approach and the departure. The hour is the room itself.
# cann.character_moments:
#   - Nyra: "She made her choice. It was not the one you needed her to make."
#     "Yes. Briefly. Then you would have resumed and hated her for having
#     made you stop." "You do not need a mother. You need a witness who
#     will not flinch. I am here." "The answer does not change in daylight."
#   - Aeron: "If my mother had stayed -- would I have stopped." "She knew
#     that." "I know." -- three uses, all three-meaning.
# cann.callbacks:
#   - a3_s12_the_oath_ob: Nyra's ceremonial voice, steel-blue register. Here
#     the register is private -- the oath's voice in the absence of an
#     audience. This is how she sounds when she is not performing.
#   - a3_s07_terms_of_order_ob: Nyra integrating command. Here she is
#     integrating something more intimate and more dangerous: Aeron's
#     interior accounting.
#   - a4_s06_tessa_at_the_board_ob: the cuff stain. Aeron wiped Liora's
#     name from the board six hours earlier. The stain is visible in this
#     scene and neither character comments on it. Nyra has seen it and
#     chosen not to say.
#   - Liora walking at end of Act 3: the precipitating event. Nyra answers
#     the question Aeron has carried from that night forward.
#   - a3_s10_tessa_friction_ob: "Nyra is a mirror. She reflects back the
#     version of you that you're most afraid of becoming. And she tells
#     you it's beautiful." This scene inverts that. Nyra does not tell him
#     it is beautiful. She tells him it is clear. Clarity, not beauty, is
#     the OB Act 4 offer. Tessa's read was right about the mirror and wrong
#     about the telling.
# cann.block_status:
#   - STATE BEAT / INTIMACY (OB). No player choice. No erotic beat. Non-tender
#     by route rule. The scene is the answer to the question and the hour
#     of silence that follows the answer.
# cann.requires_followup:
#   - The cuff stain: still on the jacket. Does Tessa see it next shift?
#     Does Aeron wash the jacket before anyone does? (The cuff has survived
#     two scenes now without being cleaned.)
#   - Aeron's "my mother" -- the single usage. Does he use the name "Liora"
#     again anywhere on the OB path? Tracking tp_seed will tell.
#   - Nyra's witness-without-flinch offer: does Aeron return for the next
#     question? What is the next question? The seed is set; the scene that
#     pays it off is Act 5.
#   - The poured-out drink: the glass sits on the drying rack, clean, empty,
#     evidence of nothing. Operational cleanliness as intimacy's closing
#     gesture.
