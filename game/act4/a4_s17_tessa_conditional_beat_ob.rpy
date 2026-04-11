# =======================================================
# ACT 4 - Scene 17: Tessa Conditional Beat (Obedience Path)
# File: a4_s17_tessa_conditional_beat_ob.rpy
# Path: OB
# Type: TESSA CONDITIONAL EROTIC / WITHDRAWAL BEAT
# Character Focus: Tessa, Aeron
# =======================================================
#
# BRANCHING:
#   - If ob.tessa.choice == "stay_and_resist"  -> Branch A (grief-sex, consent-gated)
#   - If ob.tessa.choice == "stay_but_withdraw" -> Branch B (doorway turn-away, no erotic)
#
# Branch A honors the standard OB intimacy contract:
#   buildup -> consent-gate menu -> # [INTIMATE CONTENT HERE] -> cold aftercare
# Branch B is a small, devastating negative-space beat under 250 lines.
#
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s17_tessa_conditional_beat_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s17_tessa_conditional_beat_ob:

    # ========== BRANCH SELECT ==========
    if canon_get("ob.tessa.choice") == "stay_and_resist":
        jump a4_s17_tessa_conditional_beat_ob_stay_and_resist
    else:
        jump a4_s17_tessa_conditional_beat_ob_withdraw


# ==================================================================
# BRANCH A -- STAY AND RESIST (GRIEF-SEX, CONSENT-GATED)
# ==================================================================
label a4_s17_tessa_conditional_beat_ob_stay_and_resist:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. OB economic register. No handheld.
    #         Opens on the corridor outside Aeron's quarters -- a wide,
    #         empty two-shot composition of a closed door and a strip
    #         of light under it. Tessa enters the frame from the left.
    #         She does not stop. She does not knock. Her hand finds the
    #         badge reader. The door opens. She walks in.
    #         Interior: 40mm once she is inside. Two-shot on the threshold.
    #         Aeron at the small table in his quarters -- a tactical
    #         binder open, a mug of something cold, the same desk lamp
    #         from the ops room (moved here after shift change). He does
    #         not stand. The camera holds on both of them.
    #         By the consent-gate sequence: close-ups so still they could
    #         be photographs. The stillness is the scene. The camera does
    #         not cut during the gate. It holds on Tessa's face while she
    #         speaks and on Aeron's while he answers.
    #         Intimate sequence: camera pulls back to a wide. Locked.
    #         The wide is a deliberate refusal of cinematic intimacy.
    #         Aftercare: camera holds on the closed door from outside
    #         the quarters. Tessa's silhouette in the corridor, walking
    #         away. The camera does not follow her.
    # LIGHTING: Aeron's quarters. One desk lamp. The same warm amber
    #           as the s06 board clip lamp -- Tessa's lamp, recovered
    #           from the medwing by Aeron on his walk back from the
    #           ops room, clipped now to the edge of his table. He did
    #           not ask her. She has not commented. Neither of them
    #           mentions that the lamp in this room is hers.
    #           The amber is the only warm thing. The overheads are off.
    #           The overheads stay off the entire scene.
    #           The lamp is on a low setting. The light is not flattering.
    #           It is just enough.
    # SFX: Loop -- quarters HVAC (a different register again -- quarters
    #      block is older, the hum has the quality of old building). The
    #      building noise of the base settling into night shift. Faint
    #      boot traffic in the corridor outside.
    #      One-shots -- badge reader tone (quiet, single chirp). Door
    #      seal on entry. Tessa's boots (still the same long-shift gait
    #      from the ops room hours earlier -- she has not changed, has
    #      not slept). The lamp switch: not touched this scene. Fabric,
    #      breath, the specific silence of a room where both people
    #      have decided what they are there for before either of them
    #      walked in.
    # FX/COMP: Aeron's quarters. Spartan. A cot, a small table, a
    #          locked cabinet, the desk lamp from the ops room. His
    #          jacket on the chair back. The tactical binder closed
    #          now, pushed to the edge of the table to make room.
    #          Tessa's lamp is clipped to the table. The ink stain
    #          from s06 is still on his uniform cuff where he wiped
    #          Liora's name off the board. The stain is visible in
    #          the lamp light. Neither of them looks at it directly.
    # BLOCKING: Tessa enters. She does not stop at the threshold.
    #           She crosses to the table. She does not sit. She stands
    #           beside his chair. The consent-gate sequence happens
    #           with Aeron seated and Tessa standing -- her choice of
    #           geometry, not his. She controls the room.
    #           Intimate sequence is blocked by the fade. What the
    #           script guarantees: she does not climb onto his lap.
    #           She does not straddle him. If touch happens it is
    #           parallel -- her body next to his, not over him. Grief
    #           geometry, not claim geometry.
    #           Aftercare: she gets up first. She dresses in the lamp
    #           light. She does not kiss him on the way out. She walks
    #           to the door. Badge tap. Seal breath. She is gone.
    # CANON: Hours after a4_s16 stayed-and-resist branch. Tessa has
    #        still not slept. She has come to Aeron's quarters to
    #        use his body to remember a version of him that she is
    #        fighting to preserve. This is grief-sex, not love-sex.
    #        The tenderness option (consent choice three) is the only
    #        tender beat in OB Act 4 and it is still cold-adjacent
    #        because of the context.
    # FACE: Tessa -- not performing anything. The exhaustion is the
    #        baseline now. The decision she made in the ops room is
    #        the frame. She is here for a specific thing and the
    #        specific thing is not pleasure. It is memory work.
    #        Aeron -- receptive. Marcus-idiom competent in a different
    #        register. He recognizes what she has come for and he
    #        does not try to convert it into anything else.

    # ========= VOICE BASELINE =========
    # Tessa: declarative. She has prepared the sentences before walking
    #        in, the way she prepared the one-sentence question for
    #        the ops room. Her voice is not soft. It is not hard. It
    #        is the voice of a medic running a protocol she has
    #        decided is necessary.
    # OB Aeron: quiet. Shorter sentences than in s16. The competence
    #           is still in the room but it is no longer doing work.
    #           He answers what she asks and no more.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - LATE NIGHT]
    # Spartan. One lamp. His jacket on the chair.
    # Her lamp (recovered from the medwing) clipped to the table.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_old_building.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DOOR ==========

    "The corridor outside Aeron's quarters is empty. Quarters block at this hour. A single overhead at quarter strength. A strip of amber light under his door."

    "Tessa does not knock."

    "She does not use the handle. She reaches for the badge reader. The reader chirps once, quiet, a single small tone. Her access here is not officially sanctioned. It is not officially denied either. The badge works because nobody ever got around to revoking it and because Aeron has never asked for it to be revoked."

    "The door opens."

    "She walks in."

    athought "I knew she was coming. I did not know whether I knew. I am knowing it now. I did not lock the door."

    # ========== PHASE 2 -- THE ROOM ==========

    "Tessa crosses the threshold. Does not pause. The door seals behind her."

    "She takes the room in the way she takes a patient bay on a new shift. Eyes on each surface in sequence. Cot. Table. Binder. Mug. Jacket on the chair back. Locked cabinet."

    "The lamp."

    "Her lamp. Clipped to the edge of his table. The amber on a low setting. The clip is the one she bent back into shape with her teeth six months ago when she dropped the lamp in the war room and the clip splayed out of true."

    tthought "He went back for it."

    tthought "He did not tell me. He went back for the lamp and he brought it here."

    tthought "Not to the medwing. Here."

    tthought "I am not going to comment on it. He is not going to comment on it."

    "She does not look at the lamp again. She has logged it. That is enough."

    "Aeron does not stand. He closes the binder and pushes it to the edge of the table to make room."

    # ========== PHASE 3 -- THE SENTENCE ==========

    "Tessa does not sit. She stands beside the chair. The geometry is her choice."

    "She has prepared exactly one sentence and she says it once."

    t "If I am going to write LIVING back on that board every morning, I need to remember who I am writing it for."

    athought "She has come here because of what she told me in the ops room."

    athought "She did not come here because she wanted to see me. She came here because she needs something specific and I am where the something specific is kept."

    athought "I am not offended. I am the container she has come for. I am going to be the container correctly."

    a "And who is that tonight?"

    "He says it flat. Not defensive. The question is the question."

    t "The man who used to apologize."

    "Beat."

    t "I am coming here because I need to remember he existed."

    athought "She is not here to meet me. She is here to remember a version of me that is not in this room anymore and has not been in this room for weeks."

    athought "My job tonight is to not argue with the memory."

    # ========== PHASE 4 -- CONSENT GATE ==========

    "The consent gate is not a question Tessa asks. It is a frame Aeron holds open. He does not reach for her. He does not stand. He does not close the distance. The distance is hers to close and he is making the un-closing equally available."

    a "Tell me what you need tonight. I will do whatever it is. If it is nothing, that is also a whatever-it-is and I will not fail you at it."

    tthought "He said that almost correctly. A month ago he would have said it correctly. Tonight he said it in the idiom and the idiom is adjacent to correct."

    tthought "I will take adjacent. Adjacent is what the protocol requires."

    menu:
        "Tessa's voice is steady. She is choosing between three sentences she prepared on the walk over."

        "Stay. Let me remember.":
            $ choice_and_dev(
                _current_scene_id, "_remember", "OB", factor=1,
                next_scene_label=None,
                note="Grief-sex. Tessa uses Aeron's body to hold a memory of the man who apologized."
            )
            jump a4_s17_branch_a_remember

        "I need this to feel real even if it isn't.":
            $ choice_and_dev(
                _current_scene_id, "_real_if_not", "OB", factor=1,
                next_scene_label=None,
                note="Grief-sex. Tessa requests the sensory payload without requiring the memory be accurate."
            )
            jump a4_s17_branch_a_real_if_not

        "I only need you to hold me. Nothing else tonight.":
            $ choice_and_dev(
                _current_scene_id, "_just_hold", "EMP", factor=1,
                next_scene_label=None,
                note="Tender withholding. The only tender beat in OB Act 4, still cold-adjacent due to context."
            )
            jump a4_s17_branch_a_just_hold


    # ========== CHOICE OUTCOME: STAY. LET ME REMEMBER. ==========
label a4_s17_branch_a_remember:

    # VISUAL BUILDUP -- buildup is cold-register deliberate.
    #   She does not climb over him. She sits on the edge of the cot
    #   beside the chair and she waits for him to come to her.
    #   The touch is not exploratory. It is recognition. Her hand on
    #   his wrist where the cuff is ink-stained. She does not look
    #   at the ink. He does not hide it. The stain is between them
    #   and neither of them addresses it and that is the address.

    "She steps back from the table. Not away -- repositioning. She sits on the edge of the cot. The cot is narrow. She does not slide over to make room. She does not pat the space beside her. She waits."

    "Aeron stands from the chair. The motion is economical. He crosses the four steps to the cot."

    "She looks up at him. Her eyes in the lamp light are the color of a decision that has already been made."

    t "Come here."

    "He does."

    "Her hand goes to his wrist first. Left wrist. The cuff of his uniform jacket. The ink stain from s06 -- the stain he did not wash after wiping his mother's name off the left column."

    "She does not look at the stain. He does not hide it. The stain is between them and neither of them addresses it and that is the address."

    tthought "He still has it on his cuff."

    tthought "He did not wash it. Three nights. He did not wash it. He brought the hand that did that into this room with me tonight and he is letting me put my fingers on the cuff."

    tthought "That is a form of honesty. It is the form that is available."

    tthought "I am going to use the hand that did that. I am going to use it on purpose. I am going to remember the man who apologized with the hand that wiped LIORA RYLAN off the board. Both things are true. Both things belong to the same body. I did not come here for the version that was one thing and not the other. I came here for the whole body because the whole body is the only honest container for the memory."

    "Her other hand goes to the back of his neck. Not grasping. Resting. Warm against the place where his tension lives."

    "She breathes in. She breathes out. She does not close her eyes."

    t "(quiet) Okay."

    "One word. It does not mean the same thing the word meant in the medbay hours after s10. It is a different word now. It is an operational report."

    # [INTIMATE CONTENT HERE]

    jump a4_s17_branch_a_aftercare


    # ========== CHOICE OUTCOME: I NEED THIS TO FEEL REAL EVEN IF IT ISN'T. ==========
label a4_s17_branch_a_real_if_not:

    # VISUAL BUILDUP -- this variant is the coldest of the three.
    #   Tessa is requesting sensation without requiring that the
    #   sensation map to an accurate memory. She is explicitly
    #   permitting the gap between what the body does and what she
    #   is going to feel about what the body does. That permission
    #   is what makes the scene colder than Branch A option 1. She
    #   is asking him to give her something she already knows will
    #   not land as the thing she is trying to remember.

    "She stays beside the chair. Her hand finds the edge of the table first, grounding against something that is not him."

    t "I want to tell you something before."

    a "Okay."

    t "I know the memory is not going to arrive tonight. I know this room is not the room where the apology happened. I know your cuff is not the cuff it was. I know my hands are not the hands they were."

    "Beat."

    t "I need this to feel real anyway. I need the sensory load. I need my body to register the event even if the meaning is not going to catch. The meaning can catch later or not catch at all. Tonight I need the event and I need it to feel like an event and I need the event to happen in this room with you because you are the only room where I can run this protocol."

    "Aeron does not look away from her."

    a "I understand what you are asking for."

    t "Do you."

    a "Yes."

    "Pause."

    a "You are asking me to do what I would do in the old register without requiring that either of us pretend we are in the old register. You are asking me to be the body without being the man, because the man is not currently available and you do not want to be lied to about the man."

    tthought "He said that correctly."

    tthought "I did not expect him to say that correctly."

    tthought "That he said it correctly is not the memory I came here for. It is a different data point. I am going to log it and I am going to proceed with the protocol I came here to run."

    t "Yes. That is what I am asking for."

    a "Come here."

    "She crosses the two steps. Her forehead finds the place just below his collarbone where her forehead fits. Not for comfort. For orientation. She is aligning herself with a known landmark."

    "His hand comes up to the back of her head. Not stroking. Resting."

    tthought "The event is already happening and I am already inside it."

    tthought "The meaning is not catching. I logged that he would not know how to make the meaning catch. I am running the protocol anyway."

    # [INTIMATE CONTENT HERE]

    jump a4_s17_branch_a_aftercare


    # ========== CHOICE OUTCOME: JUST HOLD ME. ==========
label a4_s17_branch_a_just_hold:

    # VISUAL BUILDUP -- This is the tender option. It is the only
    #   tender beat in OB Act 4. It is still cold-adjacent because
    #   the holding is happening against the context of a4_s16 and
    #   the OPERATIONAL strip still on the ops room table and the
    #   ink on Aeron's cuff and the fact that Tessa has not slept
    #   in 28 hours. Tenderness inside that context is not warmth
    #   in the EMP sense. It is a small stillness that the route
    #   lets exist for the length of one scene and then takes back.

    "She does not step forward. She stays beside the chair."

    t "I only need you to hold me. Nothing else tonight."

    "Aeron's hand is on the arm of the chair. The ink-stained cuff is visible in the lamp light. He looks at her once. Not a question. An acknowledgment."

    a "Come here."

    "She steps into the space he opens. He does not stand. She lowers herself to her knees beside the chair -- not supplicating, repositioning, the geometry of someone who has been on her feet for twenty-eight hours and is choosing the nearest surface."

    "Her cheek against his thigh. Her arm across his knee. His hand comes to the back of her head and stays there. No stroking. No weight. Just contact."

    "The lamp on the table. Her lamp. The amber holds the room at a temperature that is almost warm and is not quite warm, because the word OPERATIONAL is still on a strip of plastic on his ops table two corridors away and neither of them is pretending that strip does not exist."

    tthought "His hand is on my head and it is not trembling."

    tthought "A month ago his hand would have been trembling. The tremor would have been the first data point I would have cataloged on contact."

    tthought "Tonight it is not trembling. He has trained it out. The training is a separate grief and I am not going to work on that grief tonight. Tonight I am letting the hand that does not tremble be a hand that is on the back of my head."

    tthought "The hand is still warm. The temperature has not changed. Whatever else has changed about him, his hand is still eighty-eight degrees Fahrenheit and that is the only thing I came here to verify."

    tthought "I verified it."

    tthought "I am going to stay like this for a number of minutes I am not going to count."

    "Minutes pass. The HVAC of the old quarters block. The lamp on the table. His hand on the back of her head. Her breath against the fabric of his trousers."

    "She does not speak. He does not speak. That is the scene."

    "Eventually -- neither of them tracking exactly how long -- she lifts her head. She stands. The motion is economical. Her knees are stiff. She shakes them out once, quiet."

    "That is the intimacy this variant contains. The small holding. The temperature verification. The shake-out of stiff knees."

    "It is the only tender beat in OB Act 4. The scene is allowed to have it."

    "The scene does not comment on having it."

    $ flag("tessa_conditional_beat_just_hold", True)
    $ canon_set("ob.tessa.tender_withholding_beat", True)

    jump a4_s17_branch_a_aftercare


    # ========== PHASE 5 -- AFTERCARE (COLD) ==========
label a4_s17_branch_a_aftercare:

    # VISUAL: Same lamp. Same room. The amber has not moved. Tessa
    # is dressing -- or in the just-hold variant, straightening her
    # coat from the kneel. The motions are economical. She is not
    # hurrying. She is not lingering. She is operating at her normal
    # baseline efficiency, which is what the register of aftercare
    # here has to be: there is no special softness available because
    # the scene did not contain anything that would earn special
    # softness. It contained what it contained.

    "The lamp is still on. The room is still the room. Nothing about the geometry has changed except that she is upright again and Aeron is still in the chair."

    "She does not look at him while she dresses -- or, in the just-hold variant, while she straightens her coat. The not-looking is not avoidance. It is the register of someone whose eye contact is a limited resource and who has used her allocation for the night already."

    athought "She is leaving."

    athought "I am not going to ask her to stay."

    athought "I am not going to ask her anything."

    athought "Asking her anything tonight would be me converting the protocol into an exchange she did not sign up for. I signed up to be the container. The container does not request updates."

    "She pulls her coat straight at the collar. She steps back from the chair. She does not offer a hand. She does not touch his face."

    "She walks to the door. The walk is six steps. She does not look back from the middle of the six steps. She does not look back from the door."

    "She does not kiss him on the way out."

    "That absence is the most important blocking decision in the scene. The scene wants you to feel the absence and it does not gesture at the absence and it does not apologize for the absence and it does not dramatize the absence. The absence is just there, where a kiss would be in a different version of this scene on a different path."

    athought "She did not kiss me. I knew she was not going to kiss me. The not-kissing is the information she came here to leave me with."

    athought "She came here to remember the man who apologized and she is leaving here to write LIVING on a board tomorrow morning and the not-kissing is what holds those two activities in the same day without either of them contaminating the other."

    # ========== PHASE 6 -- THE EXIT ==========

    "Badge tap. Seal breath. The door opens."

    "Tessa does not pause in the threshold. She walks out. The door closes behind her."

    "The corridor has not changed since she entered. Quarter-strength overheads. Empty quarters block. Her boot sound fading at the cadence of long-shift control."

    "In the quarters, Aeron does not move from the chair."

    athought "The lamp is still hers."

    athought "I am not going to return it to the medwing. I am not going to ask her if she wants it back. I am going to leave it clipped to this table and the next time she comes here -- if she comes here -- it will be here and she will not have to comment on it."

    athought "She came here to remember the man who apologized. I do not know if the memory arrived. I do not think she came expecting it to arrive. I think she came because the walk over and the sentence and the gate and the event and the not-kissing are the ritual, and the ritual is the thing that lets her write LIVING on the board tomorrow morning."

    athought "She has told me, by the whole shape of this visit, that she is carrying the memory of the apology as a private thing now. It is not between us. It is inside her. My job was to hold the container open while she took it."

    athought "The apology is hers now. Not mine."

    "The lamp is on the table. The ink is on the cuff. The binder is at the edge of the table. The mug is cold."

    "Aeron does not move from the chair for several minutes."

    "He does not move from the chair."

    # ========== STATE UPDATES -- BRANCH A ==========

    $ rel_bump("Tessa", trust=1, attraction=1)
    $ canon_set("ob.tessa.grief_sex_memory_of_apology", True)
    $ canon_set("ob.tessa.came_to_quarters_after_fracture_point", True)
    $ tp_seed("a4.ob.tessa.remember_who_i_am_writing_it_for")
    $ flag("tessa_grief_sex_memory_of_apology", True)
    $ flag("aeron_recovered_tessas_lamp_to_quarters", True)
    $ npc_remember("Tessa", "grief_sex_for_memory_of_apology", tone="cold_adjacent")
    $ npc_remember("Aeron", "container_for_grief_sex", tone="held_open_did_not_ask")
    $ metric("ob.intimacy.cold", +1)
    $ metric("ob.ritual.corrupted", +1)

    jump a4_s17_tessa_conditional_beat_ob_close


# ==================================================================
# BRANCH B -- WITHDREW (DOORWAY TURN-AWAY, NO EROTIC)
# ==================================================================
label a4_s17_tessa_conditional_beat_ob_withdraw:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Single shot for the entire scene.
    #         The composition is the corridor outside Aeron's quarters,
    #         framed so that the door occupies the right third and the
    #         quarter-strength overhead catches Tessa's approach from
    #         the left. The camera does not move once. There are no
    #         cuts. There is one long hold.
    #         Interior shot from inside Aeron's quarters: only in the
    #         final two beats. The shot is the closed door seen from
    #         the cot. The strip of corridor light under the door.
    #         The shadow of Tessa's boots in the strip. The shadow
    #         standing still. The shadow turning. The shadow leaving.
    # LIGHTING: Corridor: quarter-strength overheads (same as Branch A).
    #           The strip of amber under Aeron's door.
    #           Interior (final beats): the same desk lamp from Branch A.
    #           CRITICALLY: Tessa's lamp is NOT on the table in Branch B.
    #           In Branch B, Aeron did not go back for the lamp. The
    #           lamp is still in the medwing, batteries running down,
    #           exactly where Tessa left it in s06. The desk lamp on
    #           Aeron's table is his own.
    # SFX: Loop -- old quarters block HVAC. Faint distant boot traffic.
    #      The quiet of night shift.
    #      One-shots -- Tessa's boots on the corridor floor, stopping.
    #      Her breath, held. No badge tap. No door tone. Her boots
    #      turning on the corridor floor. Her boots leaving.
    #      From Aeron's side: his breath slowing. No movement. He
    #      does not get up. He does not go to the door. The only
    #      sound from inside is the lamp's faint electrical hum.
    # FX/COMP: The corridor. The door. The strip of light. The shadow
    #          in the strip of light. That is the entire scene's
    #          visual vocabulary.
    # BLOCKING: Tessa walks to Aeron's door. She stops in front of it.
    #           She does not raise her hand. She does not tap the
    #           badge reader. She does not touch the handle. She
    #           stands at a distance of exactly the length of her
    #           own body. She stands there for one minute. The
    #           minute is the scene. At the end of the minute, she
    #           turns. She walks back the way she came. She does
    #           not look back.
    #           Aeron is in his quarters. He is not working. He has
    #           been waiting for her to come. He sees the shadow
    #           under the door. He sees the shadow stop. He sees
    #           the shadow stand. He sees the shadow turn. He does
    #           not get up. He does not open the door.
    # CANON: Hours after a4_s16 withdrew branch. Tessa has walked
    #        from the ops room to the quarters block on her own
    #        and she has not slept and she has not decided, in
    #        the walking, whether she was coming here to continue
    #        the withdrawal protocol or to revise it. She arrived
    #        without knowing. She leaves knowing.
    # FACE: Not shown. The scene is the door. The scene is the
    #        strip of light. The scene is the shadow. The scene
    #        is not a face.

    # ========= VOICE BASELINE =========
    # No dialogue. No interior voice from Tessa. Two short thoughts
    # from Aeron at the end. The scene is cold negative space. The
    # register is absence. There is no [INTIMATE CONTENT HERE] marker
    # in this branch because there is no intimacy in this branch.
    # The scene is under 250 lines by design.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - QUARTERS BLOCK CORRIDOR - LATE NIGHT]
    # Quarter-strength overheads. Aeron's door. A strip of amber under it.

    #scene bg_quarters_corridor_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_old_building.ogg" fadein 2.0

    # ========== PHASE 1 -- THE APPROACH ==========

    "The corridor outside Aeron's quarters. Quarter-strength overheads. The quarters block at night shift hour. Empty."

    "Tessa walks the length of the corridor. Her boots on the floor. Long-shift gait. She has still not slept."

    "She stops in front of his door."

    "She does not reach for the badge reader. She does not reach for the handle. Her hands stay at her sides."

    "A strip of amber light comes from under the door."

    # ========== PHASE 2 -- THE MINUTE ==========

    "She stands there."

    "One minute."

    "The minute is not dramatic. It is a real minute. Sixty seconds. Her boots are quiet. Her breath is quiet. The overheads do not flicker. The HVAC loops through one full cycle. The amber strip under the door does not change brightness because inside the room nothing is happening."

    "In Aeron's quarters, Aeron is at the small table. Not working. The binder is closed. The mug is cold. The desk lamp is on. His lamp, not hers. Her lamp is not in this room. He did not go back for it."

    "He is looking at the door."

    athought "Something is on the other side of the door."

    athought "Something has been on the other side of the door for nine seconds. Now eleven. Now fifteen."

    "He sees the shadow. The two small shapes in the strip of amber light under the door. Boot toes. Standing still."

    athought "She came."

    athought "She is not coming in."

    "The minute continues. He does not move. He does not stand. He does not cross to the door. He does not touch the badge reader from his side. The badge reader on his side could open the door with a single tap and he does not tap it."

    athought "I told her I could not let her go."

    athought "I cannot let her go does not mean I am going to open the door and stop her from standing on the other side of it."

    athought "I cannot let her go was the sentence I said in a room with a plastic strip on a table. The sentence does not travel to this corridor. Here the sentence has no jurisdiction."

    athought "She is standing on the other side of the door. She is deciding."

    athought "I am not going to help her decide. Helping her decide is the thing I have been doing to her for two months and the doing is what put her on the other side of the door tonight."

    "The shadow in the strip of amber light does not move."

    "Forty seconds."

    "Forty-five."

    "Fifty."

    # ========== PHASE 3 -- THE TURN ==========

    "The shadow moves."

    "Not into the room. The two small shapes of her boot toes pivot. The pivot is the whole of the motion."

    "She turns."

    "Her boots take one step. Then another. Then the gait of the long-shift walk, receding down the corridor the way it came."

    "The shadow is gone from the strip of amber light."

    "The corridor is empty again."

    # ========== PHASE 4 -- THE DOOR DOES NOT OPEN ==========

    athought "She turned."

    athought "I did not open the door."

    "Aeron does not move from the table."

    "The lamp on the table is his lamp. The binder is closed. The mug is cold. The jacket is on the chair back. His cuff has the ink stain from s06. No one is going to see the stain tonight except him."

    athought "I did not open the door and she turned and the door is still closed and the corridor is empty and the lamp on this table is not hers and she is walking somewhere that is not here."

    athought "That is tonight."

    "The HVAC cycles. The quarters block holds at the temperature it has held all night. Outside, somewhere in the corridor or past the corridor or past the quarters block entirely, Tessa walks in the direction of somewhere that is not this door."

    "Aeron does not stand."

    "The scene does not require him to stand."

    # ========== STATE UPDATES -- BRANCH B ==========

    $ canon_set("ob.tessa.doorway_turn_away", True)
    $ tp_seed("a4.ob.tessa.no_erotic_branch")
    $ flag("tessa_doorway_turn_away", True)
    $ flag("aeron_saw_shadow_did_not_open", True)
    $ rel_bump("Tessa", trust=-1, attraction=-1)
    $ npc_remember("Tessa", "doorway_turn_away", tone="decided_without_entering")
    $ npc_remember("Aeron", "did_not_open_the_door", tone="refused_to_help_her_decide")
    $ metric("ob.intimacy.cold", +2)

    jump a4_s17_tessa_conditional_beat_ob_close


# ==================================================================
# SHARED CLOSE
# ==================================================================
label a4_s17_tessa_conditional_beat_ob_close:

    # ========== SCENE CLOSE ==========

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= SHARED STATE UPDATES =========
    $ flag("a4_s17_tessa_conditional_beat_played", True)

    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s17_tessa_conditional_beat_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Act 4 OB. Hours after a4_s16 fracture point. Same night.
#     Tessa has still not slept. The OPERATIONAL strip is still
#     on Aeron's ops room table.
# cann.what_happened:
#   - CONDITIONAL on ob.tessa.choice from a4_s16.
#   - BRANCH A (stay_and_resist): Tessa goes to Aeron's quarters.
#     Does not knock. Enters. Her lamp is clipped to his table --
#     he recovered it from the medwing after the ops room scene.
#     Neither of them comments on the lamp.
#     She tells him: "If I am going to write LIVING back on that
#     board every morning, I need to remember who I am writing it
#     for." He asks who. She says: "The man who used to apologize."
#     Consent gate -- three OB-register options:
#       1. "Stay. Let me remember." -- grief-sex, uses the ink-stained
#          hand on purpose, whole-body honesty. [INTIMATE CONTENT HERE]
#       2. "I need this to feel real even if it isn't." -- coldest
#          variant; explicit permission for the meaning not to land;
#          sensory load without memory fidelity. [INTIMATE CONTENT HERE]
#       3. "I only need you to hold me. Nothing else tonight." -- the
#          one tender beat in OB Act 4, still cold-adjacent because
#          of context. She kneels beside the chair. His hand on her
#          head. No INTIMATE CONTENT marker. Tender withholding.
#     All three variants converge on cold aftercare: she dresses
#     (or straightens her coat from the kneel), does not kiss him
#     on the way out, walks to the door, leaves. He does not move
#     from the chair. The lamp stays on the table -- it is hers
#     now, left in his quarters as a placeholder analogous to the
#     lamp she left in the medwing in s06.
#   - BRANCH B (stay_but_withdraw): Tessa walks to Aeron's door.
#     Stands at the threshold for one full minute. Does not knock.
#     Does not reach for the badge reader. Turns. Walks away.
#     Aeron sees the shadow under the door. He does not get up. He
#     does not open the door. The scene is under 250 lines. No
#     dialogue. No intimacy. Cold negative space.
#     His lamp, not hers -- he did not go back for the medwing lamp
#     in this branch. Her lamp is still in the medwing, batteries
#     running down.
# cann.tessa_state:
#   - BRANCH A: decided, grief-procedural. She has come to use the
#     whole body -- including the hand that erased his mother from
#     the board -- because the whole body is the only honest container
#     for the memory she is trying to preserve. The apology becomes
#     a private object she now carries alone.
#   - BRANCH B: arrived without knowing; leaves knowing. The minute
#     at the door is the decision being made. She does not enter
#     because she is not coming back from the withdrawal protocol
#     and entering would be a revision she is not prepared to sign.
# cann.aeron_state:
#   - BRANCH A: holds the container open. Does not convert the
#     event into anything else. Does not ask her to stay. Does not
#     return the lamp to the medwing after she leaves. Lets the
#     apology become hers.
#   - BRANCH B: does not open the door. The refusal is deliberate:
#     opening the door would be "helping her decide," which is the
#     exact conversion the OB path has been performing on her for
#     two months. He denies himself the gesture.
# cann.thematic_flags:
#   - OB Act 4 thesis: "Violence Normalized." In Branch A the
#     normalization is visible in the ink stain on his cuff that
#     Tessa uses on purpose. In Branch B the normalization is the
#     unopened door.
#   - Route question: "Why didn't they leave?"
#     BRANCH A answer: she is leaving the part of herself that
#     could have left; she is carrying the apology as a private
#     artifact now so that she can continue writing LIVING.
#     BRANCH B answer: she tried to leave at the threshold and did
#     not cross it in either direction; she turned and walked to
#     another part of the base.
#   - OB intimacy rules: cold, ceremonial, transactional, compulsive,
#     angry -- never tender. Branch A tender option (just hold me)
#     is the exception the route grants exactly once, still framed
#     in cold-adjacent language. Every other variant is grief-sex
#     or absence.
#   - The consent gate: OB register. Three sentences Tessa prepared
#     on the walk over. Aeron's container-opening line is "adjacent
#     to correct" -- Marcus-idiom competence substituting for the
#     old warmth.
#   - Cold aftercare: the not-kiss on the way out is the scene's
#     load-bearing absence. The camera holds on it without naming
#     it. The scene does not dramatize the absence and does not
#     apologize for it.
# cann.character_moments:
#   - Tessa (A): "If I am going to write LIVING back on that board
#     every morning, I need to remember who I am writing it for."
#     / "The man who used to apologize." / The not-kissing.
#   - Tessa (B): Silence. The minute. The turn.
#   - Aeron (A): "I signed up to be the container. The container
#     does not request updates." / Does not return the lamp.
#   - Aeron (B): "I cannot let her go was a sentence I said in a
#     room with a plastic strip on a table. The sentence does not
#     travel to this corridor." / Does not open the door.
# cann.callbacks:
#   - a3_s10_tessa_friction_ob: the apology/dismissal gate that
#     indirectly set up the tessa.choice variable via a4_s16.
#   - a3_s17_count_the_cost_ob: the quiet intimacy the BRANCH A
#     grief-sex is trying to remember. The scene in the supply
#     room, the cold hands warming against her collarbone, "okay."
#     Branch A is the corrupted memory of that scene, run through
#     the cold register of OB Act 4.
#   - a3_s19_the_weight_ob: Tessa's methodology, the counting
#     ritual. In BRANCH A she is grieving the context in which
#     that ritual was possible.
#   - a4_s06_tessa_at_the_board_ob: the lamp. BRANCH A -- Aeron
#     recovered it between s16 and s17. BRANCH B -- he did not.
#     The lamp's location in s17 is the quiet structural tell.
#   - a4_s16_tessa_fracture_point_ob: direct prequel. The
#     ob.tessa.choice variable set there drives the entire scene.
#     The plastic strip Tessa left on Aeron's ops table in s16
#     is referenced in both branches as the context that makes
#     this scene cold.
# cann.block_status:
#   - CONDITIONAL BEAT. Branch selection is automatic from s16.
#     BRANCH A contains a player choice (consent gate, three
#     options). BRANCH B contains no player choice.
# cann.requires_followup:
#   - BRANCH A: The lamp in Aeron's quarters -- does it stay there?
#     Does Tessa come back for it? Does Nyra see it?
#     The ink stain on Aeron's cuff -- does Tessa's use of the
#     stained hand change how he carries the hand in subsequent
#     scenes? Does he finally wash it, or does it stay?
#     The not-kiss: does Tessa return to his quarters at any later
#     point in Act 4, or was this the single visit?
#     The grief-sex memory: "grief_sex_memory_of_apology" canon
#     flag -- does it surface in the Act 4 close?
#   - BRANCH B: The minute at the door -- does Aeron tell anyone?
#     (He will not. The flag tracks that he saw the shadow.)
#     The un-recovered medwing lamp -- does someone in the wing
#     notice the batteries run out?
#     Tessa's next shift -- does she honor the withdrawal protocol
#     exactly as stated? The first body she fixes "with hands that
#     belong to no one" is the follow-through scene.
