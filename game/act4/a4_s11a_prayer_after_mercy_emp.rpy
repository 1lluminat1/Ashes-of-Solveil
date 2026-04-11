# =======================================================
# ACT 4 - Scene 11a: Prayer After Mercy (Empathy Path)
# File: a4_s11a_prayer_after_mercy_emp.rpy
# Type: LYRA NEW INTIMACY INSERT — post-s11 mercy call
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s11a_prayer_after_mercy_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s11a_prayer_after_mercy_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 85mm. Opens low, off Lyra's shoulder — the camera approaches at floor level
    #         the way a cat approaches a kneeling person: slowly, from the side, without
    #         staging. Her profile, her hands in her lap, one candle in soft focus at the
    #         edge of frame. When Aeron enters the camera does not cut to him — it stays on
    #         her hands. His presence arrives as a shadow across the edge of the frame and
    #         then as a weight on the floor beside her. First face beat is the shoulder
    #         touch. Second is the forehead rest. The forehead rest is the only two-shot.
    # LIGHTING: Three candles. No overhead. No work lamp. The chapel-space has been cleared
    #           of function tonight — it is only candles and the back wall. Warm low. The
    #           kind of light that makes hands look like instruments rather than tools.
    # SFX: The base at its quietest hour. The generator is very far away. Her breath.
    #      The silence of prayer that is not said out loud. No music. Not until the shoulder
    #      touch. Then one held low note — cello, or something like a cello, held so long
    #      that the listener forgets the note started. It ends when the scene ends.
    # FACE: Lyra — composed, present, not performing. Her eyes are closed when he enters.
    #       They open for the Old Tongue word and close again after. Aeron — still carrying
    #       the mercy call. Six faces he has just decided to keep. The fatigue of having
    #       chosen. Not regret. Not comfort. Something that wants to be put somewhere.
    # BLOCKING: Lyra kneeling at the low bench she uses as an altar — not the chapel closet
    #           from s01, but the private space off her quarters she has made since. Back
    #           straight, hands open in her lap, not touching each other. Aeron enters,
    #           stops at the threshold, crosses, sits on the floor beside her. Not kneeling.
    #           Sitting cross-legged, low, shoulder height matched to hers. They stay there.
    #           The Band is NOT in the scene. It is on her wrist, implicit, under the sleeve,
    #           not once referenced. The scene is what comes after a4_s04.

    # ========= VOICE BASELINE =========
    # EMP cadence. Lyra speaks in Aeries cleric-clean register, but the register is softer
    # than in s04 — she is not defining herself in this scene, she is receiving. Aeron
    # speaks less. The scene is not a dialogue scene. It is a scene where one person has
    # just carried a weight and another person names the shape of it in a language the
    # first person does not have. Old Tongue word: Seren. Define it once, plainly, do not
    # gloss it twice. No over-closure.

    # scene bg_lyra_private_altar_emp with dissolve
    # play ambient "sfx/ambient/base_deep_night.ogg" fadein 3.0

    # ========== PHASE 1 — THE DOOR ==========

    "He does not knock this time."

    "There is a protocol for knocking on Lyra's door and there is a protocol for not knocking, and the two protocols are not written anywhere and neither of them has ever been discussed. He knows which one tonight is. He arrives at the door and the door is already not-closed — pulled to, unlatched, the way she leaves it when she is in her private space and does not want to be interrupted except by the one person she is willing to be interrupted by."

    "He pushes it open with the back of his hand."

    "The room beyond her quarters is a space she has cleared. A low bench. Three candles. The back wall unmarked. Nothing on the floor except her."

    "She is kneeling."

    athought "Not the way a soldier kneels. Not the way an officer kneels to tighten a boot. The way a priest kneels — weight on her heels, back long, hands in her lap open and not touching."

    athought "I have seen her pray twice in eleven years. Both times it was perfunctory. Both times it was the Academy shape. Neither time was this."

    "Her eyes are closed."

    "He does not speak."

    athought "She knows I am here. The door moving was enough."

    athought "She is not finishing. She is holding."

    "He stays at the threshold for a count of three. Not to be polite — to enter the silence she is inside without breaking what it is holding. The rule is the same as it was at her desk in s04. The rule is: if you come in loudly, you did not come in at all."

    # ========== PHASE 2 — THE FLOOR ==========

    "He crosses the room."

    "The floor between the threshold and the bench is two paces. He takes them slowly. His boots do not creak — he has been walking quietly for weeks now, because the base is full of people trying to sleep and the secondary base echoes. The habit has become a body thing."

    "He sits down on the floor next to her."

    "Not kneeling. He does not know how to kneel the way she is kneeling — the Academy does not teach him that posture, and the one time in his life he tried it was at a funeral he was not allowed to attend, and his knees gave out before the rite was done. So he sits. Cross-legged. Low. His left shoulder is at the height of her right shoulder because she is kneeling and he is sitting and the two heights have found each other by accident."

    "He does not touch her."

    "He puts his hands on his knees. Palms down. He breathes out."

    athought "I just chose six faces."

    athought "Six faces and one name I am going to be hearing read back to me for the rest of whatever I have left. Vess Kallan, age thirty-one, interrogation specialist, compromise window twenty-one days at thirty-eight percent probability of converting to an asset who will help kill us."

    athought "I chose her anyway."

    athought "I chose all six of them because the alternative was a ledger I could not read and because Selene said delegate the question and because Lyra said mercy is a decision you make before you know if it will work."

    athought "I am not sure what I am doing here. I am here because I did not know where else to put myself after that call."

    "The candles move very slightly. Not wind. Not breath. The secondary base's ventilation making a small pass on its long cycle."

    "Lyra does not open her eyes."

    l "You made a choice."

    "Her voice is low. Not whispered — low the way a voice is low when it has been resting in the body for a while and is being used for the first time in an hour."

    a "Yes."

    l "Six."

    a "Yes."

    l "Including the one Noelle put at thirty-eight."

    a "Yes."

    "A small silence."

    l "You do not need to tell me the rest. I was in the room when you made the call. I watched you make it."

    a "I know."

    l "I am saying it because I want you to know that I am not going to ask you to explain it to me. I am not going to ask you to justify it. I am not going to tell you whether I think it was the right choice."

    a "Lyra—"

    l "Let me finish."

    "He lets her finish."

    # ========== PHASE 3 — THE NAMING ==========

    "Her eyes are still closed. Her hands are still open in her lap. Her breath has not changed. She is not performing prayer, and she is not performing not-prayer. She is doing the thing she came into this room to do and she is letting him be in it with her."

    l "The Academy has names for what you did tonight."

    l "It has several. It has a long one that is a liturgical phrase and short ones that are shorthand for field use and one that is almost a joke, because clerics in the field get punchy when the stakes are high, and the joke-name is what the Academy actually uses because the liturgical one is too long to say in a corridor."

    l "I am not going to give you the Academy names."

    "A beat."

    l "I am going to give you a word that is older than the Academy."

    "She opens her eyes. She does not look at him — she looks at the middle candle. The middle one is the tallest and has been burning the longest. It is the one she lit first."

    l "{i}Seren.{/i}"

    "She says it once. Cleanly. Not dramatically. The way she said {i}Anayet{/i} at her desk — the way a word is said when it has been carried inside a mouth for a long time and the mouth has finally been given permission to release it."

    "He does not ask her to translate."

    "He waits. The waiting has become a thing he can do now. Eleven years of being told what to listen for, and the last year of learning how to listen for what was not being said, and tonight he listens for a word in a language he does not speak and does not try to fill the space where the translation will go."

    l "{i}Seren{/i} means: to hold what will break you."

    "She says it plainly. Once. The way she said she would. No gloss. No second pass."

    l "Not to survive what will break you. Not to avoid what will break you. Not to fix what will break you. To hold it. With your hands. On purpose. Knowing what it is."

    "Another small silence. She is still looking at the middle candle."

    l "That is what you did in the mercy call. You held six faces that you know may kill Phoenix fighters in three weeks. You held them on purpose. You knew what they were and you held them anyway. That is {i}Seren{/i}."

    l "The Aeries priests who used that word are not in the Order. The Order did not inherit them. I am not sure the Order wanted to. I think the Order wanted clean sacraments and {i}Seren{/i} is a sacrament with no clean part."

    l "But the word exists. I have been turning it over for some weeks. Tonight is the first night I have a face to give it to."

    # ========== PHASE 4 — THE LOOK ==========

    "She looks at him for the first time since he came in."

    "Her eyes in candlelight are a color he has seen before only once — the night at her desk, when she said {i}Anayet{/i} and her shoulders came down a quarter-inch for the first time in a year. This is that color. This is the color her eyes are when she is looking at someone in the language she was not taught to speak out loud."

    lthought "He is going to try to refuse it. He is going to try to tell me he did not hold the thing — that he only flinched and the flinch made the call for him. I know him. I know that much of him."

    lthought "The {i}Seren{/i} priests had a response for that. They did not argue. They did not correct. They named the thing and they let the named person decide whether to wear the naming. The naming was the sacrament. The wearing was the person's."

    lthought "I am going to let him decide."

    a "Lyra, I don't—"

    l "I know."

    a "I didn't hold anything. I—"

    l "I know. You don't have to."

    a "I panicked and Selene told me to delegate the question and I delegated the question and that is not holding. That is handing."

    "She does not flinch. She does not contradict him. She looks at him the way she looked at the candle — steady, present, unwilling to move off the thing."

    l "The priests of {i}Seren{/i} had a saying about that."

    a "Of course they did."

    "A very small breath of almost-laughter from her. Not a laugh. The skeletal version of a laugh that says {i}yes, I am choosing to be amused right now, and I am going to use the amusement as a bridge into the next sentence.{/i}"

    l "They said: the holding is not measured by the hand that holds. It is measured by the weight the hand is willing to take. If the hand is under the weight and the weight does not fall, the holding is real. The priest who claims to have held easily is the priest who was not under the weight."

    l "You are under the weight, Aeron. I can see it from here."

    l "That is the holding. The question of whether you did it well, or whether you did it gracefully, or whether you did it with perfect information, is not in the word. The word is indifferent to those questions. The word is interested only in whether you are still under the weight when the scene closes."

    l "You are still under the weight."

    l "{i}Seren{/i}."

    "She does not say it a third time. The rule of three does not apply to this word. The Aeries priests, she will tell him another night, said this word exactly twice per sacrament. Once to name. Once to affirm."

    "She has named. She has affirmed."

    "The third use would be a claim, and the priests did not claim."

    # ========== PHASE 5 — THE SENTENCE THAT IS NOT COMFORT ==========

    "He looks at his hands on his knees. His hands are steady. That is a new thing. After mercy calls the hands have been shaky for an hour. Tonight the hands are still. He does not know why. He decides not to ask why."

    athought "She is not telling me I did the right thing."

    athought "She is telling me I did a thing that has a name, and she knows the name, and she is willing to say the name in my direction without asking me to prove I deserve it."

    athought "That is not comfort. Comfort is 'you did the right thing.' Comfort is 'it will be okay.' Comfort is 'Vess Kallan is not going to break.'"

    athought "She is not saying any of those. She is saying there is a word for being under the weight of six faces and that word is older than the Order and the word does not care whether I am graceful under the weight. It cares that I am under it."

    athought "I think that is what I came here for. I did not know that was what I came here for."

    l "The Six do not grade mercy."

    "She is looking at the candle again."

    l "That is the other thing the Academy will never teach you. They teach mercy as a ledger item. They teach it as a budgeted line. They teach it as something that can be over-spent and under-spent and that has a rate of return. They do not teach you the old teaching."

    a "What's the old teaching."

    l "The Six do not grade mercy. They count it."

    "She says it simply."

    l "Grading is weight. Counting is witness. The Six are not the Academy's exam board. They are not going to tell you whether the mercy was worth it. They are going to tell you — eventually, in some way you will not recognize when it happens — that the mercy was seen. That is the entire function of the Six in the old texts. They see. They do not approve. They do not correct. They see, and because they see, the thing that was done does not vanish."

    l "You gave six people another three weeks to decide what they are going to be. The Six saw you do it. That is all I am able to tell you tonight. It is also the entire thing."

    athought "She is not telling me it was right."

    athought "She is telling me it was witnessed."

    athought "That is different. I did not know it was different until she said it."

    # ========== PHASE 6 — THE SHOULDER ==========

    "He does not know what to say. He does not say anything."

    "She moves — a very small motion. Her right hand lifts from her lap. It does not go to his face. It does not go to his hands. It goes, at a cleric's measured pace, to his left shoulder, and settles there."

    "Her palm is warm. The warmth is surprising in the way warmth is always surprising when you have been cold in a way you did not register."

    "He leans into it. Just the weight of his shoulder — half an inch, maybe less, a motion too small to be a decision and too deliberate to be an accident."

    "She leaves her hand there."

    "For one breath, she is kneeling and he is sitting and her hand is on his shoulder and the three candles are doing the small trembling they do when the ventilation passes, and nothing in the room has a name for what is happening except possibly the word she just taught him and he is not ready to use it about himself yet."

    lthought "The Band is on my wrist. It has been on my wrist since he buckled it there. Tonight I do not need it to be the interface between us. My hand is on his shoulder and my hand is the interface. That is new. That is s04 finishing its sentence."

    lthought "I did not know s04 had a next sentence. I am learning it now."

    # ========== PHASE 7 — THE FOREHEAD ==========

    "He turns his head toward her. Slowly."

    "She is still kneeling. He is still sitting. The heights have shifted slightly — his leaning has brought his forehead into the same plane as hers. The two-shot opens here, at this distance, at this height, at this light."

    "He puts his forehead against hers."

    "Not the way he did at her desk. At her desk, she leaned toward him and he received it. Tonight he is the one who moves — slowly, with the permission her hand on his shoulder has already granted, into the small distance between them until the bone of his brow meets the bone of hers and there is no distance."

    "Her hand stays on his shoulder."

    "His hand — without thinking about it — finds her forearm where it angles up toward his shoulder. Not holding. Resting. The way his hand rested on the desk before he buckled the Band. The same attention."

    "They breathe once. Together. Not choreographed — her breath found his rhythm because the hand on his shoulder was already listening for it."

    "Two breaths."

    "Three."

    athought "I am not counting."

    athought "That is a lie. I am counting. I am counting because that is what I do and the counting is how I pay attention. But the count is not ruining it."

    athought "She said the count does not have to ruin it. In s04 I thought that was about the Band. Tonight I think it was about everything."

    "Four breaths, maybe. He has lost the count on the fourth and is not reaching for it."

    lthought "His forehead is warm and there is the faintest tremor at his temple — the kind you feel when someone has been holding something in their jaw for an hour. It is loosening. I am not going to point it out. The pointing would be a correction and I am not here to correct."

    lthought "I am here to be present with him. That is the sacrament. That is the whole of it."

    # ========== PHASE 8 — THE CLOSE ==========

    "He straightens. Not abruptly. The same way she straightened in s04 — the way a priest steps back from a rail. He leaves her hand on his shoulder until she is the one who takes it away, and she takes it away after, and the taking-away is also slow."

    "She looks at him."

    "He looks at her."

    a "Seren."

    "He says it clumsily. He is not a native speaker. He is not a speaker at all. His mouth shapes the word the way a mouth shapes a word it is learning for the first time — careful at the first syllable, uncertain at the second, the consonant cluster almost but not quite where she put it."

    l "Close enough."

    a "I'm going to say it wrong for a while."

    l "You are going to say it wrong for your entire life. That is also part of the word."

    "A beat."

    l "The priests said: a word in Old Tongue said wrong in a real mouth is more of the word than the word said right in a classroom."

    a "Of course they did."

    l "They were — they were opinionated, as a group."

    "The skeletal almost-laugh again. Tonight she is letting herself almost laugh twice. That is new."

    athought "Twice. In one scene. Twice is a change."

    "He looks at the candles. The middle one has burned down a half-centimeter since he came in. The other two are steady."

    "He does not stand up."

    "Neither of them stands up."

    "They stay on the floor beside the bench for what might be another minute or might be another five. The candles do not mark the time. The base does not mark the time. He does not count it."

    "When he finally shifts his weight to stand, she reaches out — one more time — and catches the back of his hand. Not to hold him. To confirm. The way you touch a door frame as you leave a room to be sure the frame was real."

    l "You came here."

    a "I came here."

    l "Thank you."

    a "You do not need to thank me for that."

    l "I know. I am thanking you anyway."

    "Echo. He hears it. She placed it there."

    athought "She said that sentence to me in s05. The briefing. When she thanked me for letting her run the operation. I am hearing it twice now. On purpose."

    athought "She is telling me the scene is finished the way we finished the last one. She is closing with the same sentence to tell me this is the same kind of ending."

    athought "It is not the same ending. It is the next one. But it is in the same language."

    "He stands. She does not stand with him — she stays kneeling, hands open in her lap, the candles at the edge of the frame."

    "He moves to the door. At the threshold he stops. He does not turn back — he has already said goodnight to her twice in his life and the rule of three is not a rule he is ready to apply to goodnights with her. Instead he says a different thing, because tonight is a different scene, and the scene needs a different closing."

    a "I am going to sit with the word."

    l "Good."

    a "I am not going to know what to do with it by morning."

    l "You are not supposed to."

    a "Okay."

    l "Aeron."

    "He turns his head. Not his body."

    l "{i}Seren{/i} is not the last word I have for you in this language. There will be others. I am telling you so you know to expect them."

    a "I will be here."

    l "I know."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=2)
    $ flag("lyra_seren_spoken_to_aeron", True)
    $ flag("aeron_received_seren_naming", True)
    $ canon_set("lyra.seren_defined_for_aeron", True)
    $ canon_set("lyra.hand_is_interface", True)
    $ npc_remember("Lyra", "named_the_mercy_call", tone="priest_of_seren")
    $ npc_remember("Aeron", "said_seren_aloud_first_time", tone="clumsy_sacred")
    $ tp_seed("a4.lyra.seren")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s11a_prayer_after_mercy_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Late night, immediately after a4_s11 (the mercy call to spare six Echelon
#     captives, including Officer Vess Kallan at 38% compromise risk within 21 days).
#   - Aeron arrives at Lyra's private space still carrying the call. She has
#     already been at her altar for some time.
# cann.what_happened:
#   - Aeron enters Lyra's private altar space (distinct from the chapel closet in
#     a4_s01 — this is the personal space off her quarters she has made since s04).
#     Three candles. A low bench. She is kneeling and praying — not performing
#     prayer, actually praying. The Band is on her wrist but is not once referenced.
#   - He sits on the floor beside her cross-legged. Shoulder heights match because
#     she is kneeling and he is sitting.
#   - Lyra does NOT tell him the mercy call was the right choice. She explicitly
#     refuses to grade it. Instead she names it in an Old Tongue word: Seren.
#     She defines it once, plainly: "to hold what will break you."
#   - She gives the accompanying teaching: "The Six do not grade mercy. They
#     count it." Grading is weight, counting is witness. The Six see, and because
#     they see, the thing done does not vanish. Mercy is not validated — it is
#     witnessed.
#   - Lyra articulates the distinction between holding-easily (false claim) and
#     being-under-the-weight (real holding). She tells Aeron he is still under
#     the weight and that is the holding. The question of gracefulness is not in
#     the word.
#   - Physical progression: her hand to his shoulder (first touch of the scene).
#     He leans into it. Then he moves his forehead to hers — this time he is the
#     one who moves, completing the sentence s04 started (where she moved to him).
#     Three to four breaths forehead to forehead. He loses the count and does not
#     reach for it.
#   - He says "Seren" aloud, clumsily. She says a word said wrong in a real mouth
#     is more of the word than the word said right in a classroom.
#   - Scene closes with Aeron saying "I am going to sit with the word. I am not
#     going to know what to do with it by morning." Lyra: "You are not supposed to."
#     Lyra tells him there will be other Old Tongue words — she is preparing him
#     for the next one. He replies "I will be here."
#   - Closing echo: Lyra uses the "I am thanking you anyway" line from s05. Aeron
#     internally clocks that she is closing with the same sentence on purpose, to
#     mark continuity between scenes.
# cann.aeron_state:
#   - Arrives still carrying the mercy call. Hands steady in a way that surprises
#     him — after prior mercy calls his hands have shaken for an hour.
#   - Receives the Seren naming with resistance ("I didn't hold anything, I
#     handed") and then gradually accepts that being-under-the-weight is the
#     definition, not gracefulness.
#   - First time he speaks an Old Tongue word aloud, to Lyra, in his own mouth.
#     He says it wrong. She lets him.
#   - The forehead rest is initiated by him this time. The physical grammar of
#     s04 has reversed direction: in s04 she leaned to him; tonight he leans to
#     her. The scene is the next step after unbuckling.
# cann.lyra_state:
#   - Praying before he arrives — actual prayer, not performance. She does not
#     perform for him. She lets him enter the silence.
#   - Refuses to grade the mercy call. Refuses to tell him he did the right thing.
#     Instead she names it in a language the Academy does not own.
#   - Introduces Seren: the second Old Tongue word in the Lyra thread. Defines it
#     once, affirms it once. The rule of three does not apply to this word — the
#     Aeries Seren priests said it exactly twice per sacrament (once to name, once
#     to affirm; the third use would be a claim).
#   - First time she touches Aeron without the Band being the interface. Her palm
#     on his shoulder is the new interface. Canonical state:
#     lyra.hand_is_interface.
#   - Almost-laughs twice in one scene. Newly willing.
# cann.path_tracking:
#   - EMP path only. Linear. No branching.
#   - rel_bump Lyra trust +2. flag lyra_seren_spoken_to_aeron. flag
#     aeron_received_seren_naming. canon_set lyra.seren_defined_for_aeron.
#     canon_set lyra.hand_is_interface.
#   - tp_seed a4.lyra.seren — seeds the Seren thread for later Act IV beats and
#     the eventual payoff where Aeron uses the word correctly in his own mouth.
# cann.thematic_flags:
#   - Mercy as witnessed, not graded. The Six see; they do not approve.
#   - Seren: "to hold what will break you." The second Old Tongue word Lyra has
#     given Aeron. First was Anayet (name the thing that cannot be promised).
#     Pattern: Lyra is teaching him a liturgy older than the Order, one word at
#     a time.
#   - Presence as sacrament (echo of s04 "presence is enough"). Here extended:
#     presence as the physical interface without the Band.
#   - The reversal of physical grammar from s04. In s04 she leaned to him. In
#     s11a he leans to her. The movement now goes both ways.
#   - "Old Tongue said wrong in a real mouth" — language as lived rather than
#     catalogued. Aeries priests' teaching weaponized against the Academy.
# cann.character_moments:
#   - Lyra: praying before he arrives. Naming instead of consoling. The "Six
#     count, they do not grade" teaching. The hand on the shoulder as new
#     interface.
#   - Aeron: the clumsy first utterance of an Old Tongue word. Initiating the
#     forehead rest. Hands steady when they should be shaking.
# cann.callbacks:
#   - a4_s04_lyra_unbuckled_emp: forehead rest — she to him. a4_s11a inverts:
#     he to her. The physical grammar is a matched pair.
#   - a4_s04: Anayet — Old Tongue word 1. a4_s11a: Seren — Old Tongue word 2.
#     The Lyra liturgy is becoming a canon Aeron can witness.
#   - a4_s05_delegation_test_emp: "I am thanking you anyway." Closing echo.
#     Aeron internally clocks that Lyra is placing the same sentence on purpose
#     to mark continuity.
#   - a4_s11: the mercy call. This scene is the direct emotional afterimage.
#     Specifically the six faces, Vess Kallan at 38%/21 days.
#   - Liora's letter / Lyra's "brave enough to be soft" — the Seren teaching is
#     the operational form of that softness.
# cann.block_status:
#   - INTIMACY INSERT. Linear. EMP only. No branching. Relationship-gated entry
#     (requires prior Lyra trust threshold from s04).
# cann.requires_followup:
#   - Seren as a word Aeron will eventually use correctly about someone else
#     (not about himself). Payoff pending later in Act IV.
#   - "There will be other Old Tongue words" — the word chain is open. Lyra has
#     telegraphed the next one is coming.
#   - The Six as a spiritual framework that does not grade, only counts — this
#     should inform later mercy / ledger scenes in Act IV and V.
#   - Vess Kallan at 38%/21 days is now the named risk carried out of this scene.
#     The mercy call's downstream consequence lives under the Seren naming.
