# =======================================================
# ACT 4 - Scene 04: Unbuckled (Empathy Path)
# File: a4_s04_lyra_unbuckled_emp.rpy
# Type: LYRA INTIMACY BEAT — state-of-relationship checkpoint
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s04_lyra_unbuckled_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s04_lyra_unbuckled_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 85mm. Opens on the Band on the desk — not on her wrist. Held long enough
    #         that the absence becomes the subject. Rack focus to Lyra's hands in her
    #         lap. Then Aeron in the doorway. For the re-buckling: macro on the leather,
    #         the clasp, his fingers, her wrist. Faces only at the forehead-rest.
    # LIGHTING: Late. One lamp on the desk — warm, low. The Band catches the lamp on the
    #           seam the way it always does. Her bare wrist does not. The wrist is the
    #           unlit thing in the frame and the room tilts toward it.
    # SFX: Phoenix base at its second-quietest hour. The low structural hum. Her breath.
    #      His boots stopping in the doorway and then coming in. The leather strap moving
    #      once, twice. The metallic click of the clasp — recorded clean. No music until
    #      after the forehead touch; then one held string, barely there, fadeout on black.
    # FACE: Lyra — steadier than she has been in months. Not untroubled. Chosen. Aeron —
    #       the rawness of Act IV under the surface, but here: quiet. Paying attention.
    # BLOCKING: Lyra seated at the desk, angled three-quarters from the door. Aeron
    #           enters, crosses to her, kneels at her side for the re-buckling. Equality
    #           of height matters here — he does not stand over her wrist.

    # ========= VOICE BASELINE =========
    # EMP cadence. This is a quiet scene. Sentences short. The silences are load-bearing.
    # Lyra's diction is cleric-clean — precision, inventory, the Academy cadence softened
    # by choice rather than drill. Aeron speaks less than she does. He is here to witness.

    # scene bg_lyra_quarters_late_emp with dissolve
    # show lyra neutral at center
    # play ambient "sfx/ambient/base_night_deep.ogg" fadein 2.0

    # ========== PHASE 1 — THE ABSENCE ==========

    "The door to Lyra's quarters is not locked. It has not been locked since the morning after the execution. There is a detail there he does not ask her about."

    "He knocks anyway. Once. Then opens."

    "She is at the small desk she has made into whatever a desk becomes when someone lives with it long enough to trust it. A lamp. A cup. One book face-down. The Order-issue datapad on the far corner where she can reach it without looking."

    "And the Aether Band."

    "On the desk. In front of her. Not on her wrist."

    athought "Eleven years."

    athought "The first time I saw her — fourth year of field training, the roof of the administrative spire, her hand on the Band without looking. I thought it was a tic. I thought it was training."

    athought "It was both. It was also scaffolding. And the scaffolding is on the desk."

    "He does not say anything. She does not turn."

    l "You saw it."

    a "I saw it."

    l "I thought you would."

    "She still has not looked at him. Her hands are in her lap. One thumb rests at the crease of the opposite palm — the place her thumb goes when the Band is not there to check."

    athought "She has trained the gesture of checking and now she is rehearsing it on bare skin. Her body does not know yet that the Band is not where it lives."

    # ========== PHASE 2 — THE DECISION ==========

    "He crosses the room. Slowly. Not because he is cautious of her — because this is her silence and he wants to enter it without breaking what it is holding."

    "He stops at the edge of the desk."

    a "How long?"

    l "An hour. A little less."

    a "You took it off at dinner."

    l "I took it off before dinner. I did not eat dinner."

    athought "She tells me this the way she would tell a medic a symptom. Neutral. Itemized. No self-pity in the reporting."

    "He waits."

    l "I woke up this morning and my thumb was on the seam before my eyes were open. I counted — in my head, because I was not ready to be awake — I counted, six, seven, eight. I lost it on eight."

    l "I have been losing it on eight for three years."

    "Her voice is very even."

    l "And this morning I thought: if I cannot finish counting the Band while I am wearing it, then the Band is not the thing I am counting. The Band is the thing I am using to avoid counting the thing I am actually counting."

    a "Which is what?"

    "She considers the question the way she considers questions — as if there is a right answer and a wrong answer and speaking the wrong one out loud would cost her something she is not willing to pay."

    l "I do not have a name for it yet. I thought taking the Band off for an hour might give me one."

    a "Did it?"

    l "No."

    l "But it gave me an hour. Which is more than I had this morning."

    # ========== PHASE 3 — THE WRIST ==========

    "He looks at her wrist. It is paler than the skin above it — the Band's shadow, eleven years deep. A half-centimeter of skin that has not met direct light since she was nineteen."

    "It looks like a scar that is not a scar. It looks like a place where a scar would be if the Order had been honest about what it was asking of her."

    athought "I have seen her naked. I have not seen her wrist until now."

    athought "That should not be true. It is."

    l "Do not look at it like that."

    a "Like what?"

    l "Like you have found something that was missing."

    "She is still not looking at him. She picks up the Band. Turns it in her fingers. The seam catches the lamp."

    l "I am not going to remove it."

    a "Okay."

    l "I want to be clear about that. I am not renouncing it. I am not — this is not a resignation. I am not leaving the Order because the Order is already something I am not sure I have been inside of for a long time, and leaving is a word that requires a door I am not sure exists."

    l "I am choosing it."

    "She looks at him for the first time since he came in."

    l "That is the whole sentence. I am choosing it. Not being bound by it. The difference is — I think the difference is the entire thing."

    athought "Anyone else in the room would hear this and think it is a distinction without a difference."

    athought "Anyone who has ever watched her count pulses while pretending to listen to a briefing would hear what she is actually saying."

    a "The difference matters."

    l "Yes."

    a "It matters a lot."

    l "Yes."

    "She looks down at the Band in her hand. Her thumb, almost without her noticing, finds the seam and counts once. Six. She catches herself. Stops. Looks at her own thumb as if it is a small animal she is trying to learn the habits of."

    lthought "Six, and then I stopped myself. Which is also new. For three years the count has been the thing that stopped me; tonight I stopped the count."

    lthought "The body learns. I am the one teaching it now. That is what I could not say out loud. The Order used to be the teacher. The Order taught the hand. I am the teacher now and the hand is mine and so is the lesson."

    lthought "I could not have said any of that a year ago. I am saying it in a room that belongs to me by looking at a man who belongs in this room with me."

    # ========== PHASE 4 — THE WORD ==========

    l "There is a word."

    a "A word."

    l "Old Tongue. It came to me in the field a few months ago. I did not know where it came from. I have been — I have been turning it over since."

    "She says it softly."

    l "{i}Anayet.{/i}"

    "He does not ask her to translate. He waits."

    l "I do not have the whole translation. I have found pieces of it in places the Order did not teach me to look. I think it means something like — I name the thing that cannot be promised."

    l "Something close to that. The shape of that."

    "She sets the Band down on the desk again."

    l "I have been thinking about it because I do not have a word in the Academy liturgy for what I am doing in this room tonight. I am taking a ritual the Order gave me and I am making it mine and there is no Academy word for that. There is no sacrament for 'the servant reclaiming the discipline.'"

    l "There is this word. From a language I was not taught and should not know. And my mother may or may not have known it. I am not sure yet. I am going to be sure."

    a "Is that what tonight is?"

    l "Part of it."

    "She looks at the Band. Then at him."

    l "I cannot promise I will know what I am doing with any of this by morning. I cannot promise the Band will stay on the wrist I am going to ask you to put it back on. I cannot promise that the word I just said out loud will still be a word I trust next week."

    l "That is why {i}Anayet{/i} is the word I have."

    l "I am naming the thing I cannot promise. That is what I have tonight."

    # ========== PHASE 5 — THE RE-BUCKLING ==========

    "She picks up the Band. Holds it out to him. Not at arm's length — close. Her wrist turns over, palm up, in her lap."

    l "Help me put it back on."

    a "You can do it yourself."

    l "I know."

    a "Okay."

    "He kneels at the side of the desk. Not so much to her as to the height of her wrist. The kneeling is not deference — it is the simplest way to see what his hands are doing."

    athought "I have buckled this Band onto her wrist exactly zero times."

    athought "The first time is tonight."

    "He takes the Band from her hand. The leather is warm from where she has been holding it. The metal clasp is cool."

    "He turns her wrist gently. Palm up. The pale half-centimeter of skin is between his thumb and forefinger."

    athought "Her pulse is under my thumb. I am not counting it. Her thumb would have counted it by now. I am not her thumb."

    "He lays the Band across her wrist. The leather finds the place it has been finding for eleven years."

    "He threads the strap. Slow. Not because the motion is complicated — because he does not want to miss any of it."

    l "The strap goes through the loop first. Then the buckle. The Order teaches a specific sequence. It is supposed to be meditative. It is also supposed to be fast — they time it in the third year."

    a "How fast?"

    l "Under eight seconds."

    a "I am going to be slower than that."

    l "I am counting on it."

    "The strap goes through the loop. He pulls it gently to the tension she has worn into the leather — he can feel where her wrist has made the leather remember her. He finds that notch. He does not overshoot it."

    athought "The leather remembers her. That is not a metaphor. It is a physical fact. I am matching a shape her body has been making in this material for eleven years and if I had ever done this before I would have known exactly where the notch was."

    athought "I am learning her wrist by Braille."

    "He seats the buckle. Lines up the pin with the hole she uses — there is a small bright spot in the leather at that hole, polished by use."

    "He closes the clasp."

    "The click."

    "It is a small metallic sound. It is louder in the room than the sound of either of their breath. It is louder than the lamp. It is louder than the base."

    "Lyra does not flinch. Her eyes are on his hands."

    "Neither does he."

    lthought "His hands did not shake. That matters to me and I am going to let it matter without filing it."

    lthought "The Band is back on my wrist. It is heavier than it was an hour ago and it is lighter than it was this morning. That is a true sentence that an hour ago I could not have said."

    # ========== PHASE 6 — THE SENTENCE ==========

    "His hands leave her wrist. He does not stand. He stays at her side, at the height of the desk, her hand still open in her lap."

    l "I used to think faith meant being whole."

    "She says it to the Band. Then to him."

    l "I am still figuring out what it means now that I know I am not. But I am figuring it out with you in the room."

    l "That matters."

    a "Lyra—"

    l "Let me have the sentence."

    a "Okay."

    l "That matters. That is the sentence. I did not want to give it to you with a qualifier."

    "He nods. Small. The kind of nod that is not agreement so much as receiving."

    athought "I do not know what I offer her."

    athought "I have been trying to figure that out since the execution and the answer keeps moving."

    athought "If I tell her I do not know, will that be the wrong thing to say."

    "He says it anyway, because the scene is already the kind of scene where not saying it would be the lie."

    a "I do not know what I offer you."

    "She looks at him. The answer is immediate. She does not need to think about it — she has been thinking about it for some time."

    l "Presence."

    l "That is enough. For now."

    athought "Presence."

    athought "Tessa used that word too. Not tonight. A week ago. She said it to me in the corridor when she was not letting me walk past her. She said my body was not a resource to be spent."

    athought "Two people who do not know each other well are giving me the same word."

    athought "I am going to let that be a pattern I pay attention to."

    # ========== PHASE 7 — THE FOREHEAD ==========

    "She leans forward in the chair. Slowly. Not a dramatic motion — the kind of motion a cleric would make toward an altar she had just been cleared to approach."

    "Her forehead finds his."

    "He does not pull back. He lets her weight come to him. His hand stays where her wrist is — not holding the Band, holding the joint just above the clasp, the warm place where her pulse is."

    "One breath."

    "That is all it is. One breath, forehead to forehead, the Band under his thumb and the lamp at their backs and the base humming at the far edge of hearing."

    athought "If I count it, the count ruins it."

    athought "I am not counting it."

    "Two breaths, maybe. He is not counting."

    "She straightens. Not abruptly — the way a priest steps back from a rail."

    l "Okay."

    a "Okay."

    l "I have some reading I want to do tonight. About the word. I have been waiting to do it alone and I think tonight is the night I am ready to."

    a "I will leave you to it."

    l "Thank you."

    "He stands. He does not reach for her again — the re-buckling was the reaching. That part of the scene is over and honoring that means not re-entering it."

    "He moves to the door. Stops at the threshold. Looks back."

    "She is looking at her wrist. Her thumb is at the seam of the Band. It is not counting. It is resting. The difference is not visible to anyone in the building except him."

    athought "That is the difference. And the difference is the entire thing."

    a "Goodnight, Lyra."

    l "Goodnight."

    l "Aeron."

    "He stops in the doorway."

    l "I am going to use that word again. Out loud. To you. When I know what the rest of the translation is."

    a "I will be here."

    l "I know."

    # stop ambient fadeout 2.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1)
    $ flag("lyra_band_chosen", True)
    $ flag("lyra_anayet_spoken_to_aeron", True)
    $ npc_remember("Lyra", "rebuckled_by_aeron", tone="chosen_ritual")
    $ npc_remember("Aeron", "lyra_wrist_bare", tone="reverent_attention")
    $ canon_set("lyra.band_is_chosen_not_compelled", True)
    $ tp_seed("a4.lyra_partnership_phase_one")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s04_lyra_unbuckled_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Early Act IV. After the council scenes that open the chapter. Before the
#     delegation operation (a4_s05). Night. Lyra's quarters at the secondary base.
#   - First unrushed moment between Aeron and Lyra since the Act 3 aftermath.
# cann.what_happened:
#   - Aeron finds Lyra at her desk with the Aether Band unbuckled and set in front
#     of her. First time in eleven years she has not been wearing it. She took it
#     off an hour earlier, has not eaten dinner.
#   - She is explicit that she is not removing it — she is choosing it. The
#     difference between being bound by the ritual and electing the ritual is the
#     entire point of the scene. "Chosen, not compelled" is the canonical state.
#   - She names the compulsion. She acknowledges she has been losing the count on
#     eight for three years and that the Band has been the instrument she was
#     using to avoid naming what she was actually counting.
#   - She speaks the Old Tongue word Anayet out loud to Aeron for the first time.
#     She gives him a partial translation — "I name the thing that cannot be
#     promised." She is explicit that the translation is incomplete and that the
#     word is what she has tonight instead of Academy language.
#   - She asks Aeron to help her re-buckle the Band. Not because she cannot do it
#     herself — because choosing to put it back on is something she wants to share.
#     He kneels at the desk. Threads the strap. Seats the buckle. The leather has
#     been shaped by her wrist for eleven years and he finds the notch by touch.
#     The clasp clicks. Neither of them flinches.
#   - Lyra delivers the load-bearing line: "I used to think faith meant being
#     whole. I am still figuring out what it means now that I know I am not. But
#     I am figuring it out with you in the room. That matters."
#   - Aeron replies: "I do not know what I offer you." Lyra: "Presence. That is
#     enough. For now." (Echo with Tessa's language — flagged for Aeron.)
#   - Forehead rest for one breath. Then step apart. No kiss, no further contact.
#     The re-buckling is the intimate gesture; the forehead touch is the benediction.
#   - Scene closes with Aeron in the doorway. Lyra promises to speak the word
#     again out loud when she has the rest of the translation.
# cann.aeron_state:
#   - Quiet. Paying attention. The rawness of Act IV still under the surface but
#     not driving the scene. He is here as a witness, not as a commander.
#   - He notices the echo between Lyra's "presence is enough" and Tessa's earlier
#     use of the same word. The scene marks this as a pattern he is starting to
#     track. This is the beginning of the Act IV lesson that shared leadership is
#     not a distribution of burdens but a distribution of witness.
# cann.lyra_state:
#   - Steadier than she has been since early Act III. Not untroubled — chosen.
#   - The scene is the first externalization of her private work across the Act 2
#     and Act 3 interludes. The ritual has migrated from compulsion to election.
#   - She is beginning to locate herself inside a liturgy that is not the Academy's.
#     Anayet is the foothold.
# cann.path_tracking:
#   - Empathy path exclusive. Linear — no player choice.
#   - rel_bump Lyra trust +1. flag lyra_band_chosen True. flag
#     lyra_anayet_spoken_to_aeron True. canon_set lyra.band_is_chosen_not_compelled.
#   - tp_seed a4.lyra_partnership_phase_one — seeds the Lyra devotion-to-partnership
#     transition that lands fully across later Act IV beats.
# cann.thematic_flags:
#   - Chosen ritual vs. compelled ritual — the Act IV Lyra thesis in compressed form.
#   - Anayet — the Old Tongue word, now spoken aloud to a witness for the first time.
#     The word is load-bearing for the Lyra-mother thread and the Order-is-incomplete
#     thread. Its full translation is still a quest object.
#   - Presence as the currency of shared authority. Echoed between Lyra and Tessa
#     without the two women coordinating. Aeron clocks the pattern.
#   - The act of buckling as liturgy. Hands on the wrist. The clasp click as the
#     only audible punctuation. The forehead rest as sacramental close.
# cann.character_moments:
#   - Lyra: First time out of the Band since she was nineteen. First time any
#     living person has seen her bare wrist. First time she speaks Anayet to another
#     mouth. All of this is treated as private ceremony rather than revelation.
#   - Aeron: The kneeling is not romantic posturing — it is height matching. He
#     learns her wrist "by Braille." He does not count her pulse under his thumb.
#     These are the scene's small character beats.
# cann.callbacks:
#   - a2_int_lyra_check: the count that breaks on eight. The Band compulsion. The
#     sensation-check training. This scene is the counterweight to that interlude.
#   - a3_int_lyra_file_was_wrong_emp: Lyra's recognition of her training as weapon.
#     The re-buckling is the ritual form of that recognition.
#   - a3_int_lyra_field_sync_emp: Anayet first appears there. Spoken only in her
#     own head. This scene is the word's first outside witness.
#   - Liora's letter (a3_s18a): "brave enough to be soft when softness is the most
#     dangerous thing." Lyra is performing that lesson here.
#   - Tessa corridor scene (a4_s05a): "presence is enough" as cross-LI language.
#     Aeron is supposed to register the echo. Noted in aeron_state above.
# cann.block_status:
#   - LINEAR. No branching, no choice. EMP path only. Relationship-gated entry.
# cann.requires_followup:
#   - Anayet translation quest — the rest of the word is still pending.
#   - Lyra's mother as Old Tongue speaker — Act IV thread referenced but not resolved.
#   - The Band-as-chosen state is the new canon. Any later Lyra scene that shows
#     her thumb on the seam must now read as electing the ritual, not obeying it.
#   - "Presence is enough" as personal shorthand between Aeron and Lyra (and,
#     separately, Aeron and Tessa). Future scenes may collapse this echo deliberately.
