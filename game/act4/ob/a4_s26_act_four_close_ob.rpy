# =======================================================
# ACT 4 - Scene 26: The Edge (Obsidian Path)
# File: a4_s26_act_four_close_ob.rpy
# Type: ACT CLOSE — the dark relay, the handoff, the title card to Act V
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s26_act_four_close_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s26_act_four_close_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Three movements — the cold mirror of EMP s22.
    #         (1) Open wide. Aeron at the edge of the base, overlooking the
    #             staging ground below. The operators are already in motion —
    #             not a civilian convoy, not a relocation. An assassination
    #             detail preparing a loadout. The camera is at Aeron's height,
    #             one step back and to his LEFT (EMP is right; OB mirrors).
    #             It does not move for the length of the relay.
    #         (2) The relay. Five (or four) LIs enter and exit the frame from
    #             Aeron's right (the base side). They come one at a time. The
    #             camera does not cut between them. Zira first — moving past,
    #             the soldier's acknowledgment only. Noelle second — she does
    #             not walk. She stops briefly, hands him a tablet, one word.
    #             Tessa third — CONDITIONAL. Branch A: she arrives with the
    #             clip lamp. Branch B: she does not come. Her absence is the
    #             space the frame holds for a beat that stays empty. Lyra
    #             fourth — she does not speak. The Band is the gesture. Nyra
    #             fifth and last — stands beside him for a long silent beat
    #             before the line that closes the act.
    #         (3) Aeron alone at the end. The camera pulls back one small
    #             step — one step only, same as EMP s22. The staging ground
    #             in mid-ground. Aeron in the foreground. The sun choice is
    #             the cinema choice and on OB it is the inverse of EMP: the
    #             default here is sun SETTING over the west ridge — the
    #             light cold and going, the last light of a day that has
    #             already been long. The rise variant is available and this
    #             file flags it, but OB default is setting. Either way the
    #             staging ground is in the going light and Aeron is at the
    #             edge of that light and his face is half in and half out.
    # LIGHTING: Default: sun setting, cold and directional, long shadows
    #           across the access road. The light on Aeron's face is the
    #           light from the west — honest, directional, going. Variant:
    #           dawn, for a director who wants to underline that the day
    #           the operators depart for has already begun. The scene does
    #           not choose for you; it carries both.
    # SFX: The base behind him — the sound of a loadout. Magazines on metal.
    #      A pack being cinched. A radio check that does not complete. No
    #      child asking a question here. No father answering. The absence
    #      of those sounds is the scene's acoustic signature. One long low
    #      string at the last beat, held flat. No rise. No fall. Flat.
    # FACE: Aeron — the act's accumulated weight, carried without visible
    #       strain. Not crushed. Not light. The face of a man who has put
    #       a letter against his chest and decided that the letter is a
    #       gravestone and not a door. Each LI brings a face shaped by the
    #       scene before her — Zira's is the face that does not let her
    #       eyes stop on him, Noelle's is the face of a woman reading her
    #       own framework, Lyra's is the face of a priest carrying a
    #       counting, Nyra's is the face of the only person in the base
    #       who does not have to perform anything tonight.
    # BLOCKING: The edge of the base. The staging ground below. The
    #           operators loading. Aeron stationary for the length of the
    #           scene — he does not turn. The LIs pass through the frame
    #           behind him from right to left. The camera holds.
    # FX/COMP: THE LETTER. Aeron's jacket is closed. His right hand rests
    #          once, briefly, on the left inside of his jacket where the
    #          letter sits against his chest. The gesture is a check. He
    #          makes the gesture once in the entire scene. The audience
    #          sees it if the audience is paying attention. He does not
    #          look at his own hand when he makes it.

    # ========= VOICE BASELINE =========
    # OB register. The scene is quiet. Short sentences. The silences are
    # cold, not load-bearing. No warmth. No score until the last beat.
    # Aeron has almost no spoken lines — the scene is theirs, each in
    # turn, and his interior is the thread that holds them. The final
    # line of the act is Aeron's internal. The title card follows.

    # scene bg_base_edge_dusk_ob with dissolve
    # play ambient "sfx/ambient/base_loadout_distant.ogg" fadein 2.0

    # ========== PHASE 1 — THE EDGE ==========

    # CAMERA: wide establishing. Aeron at the edge of
    #         the base, overlooking the staging ground
    #         below. The operators are already in
    #         motion — NOT a civilian convoy (that is
    #         EMP). An ASSASSINATION DETAIL preparing
    #         a loadout. The camera is at Aeron's
    #         height, one step back and to his LEFT
    #         (EMP s22 was right; OB mirrors). It does
    #         NOT move for the length of the relay.
    # LIGHTING: OB default — sun SETTING over the west
    #           ridge. Cold and directional. Long
    #           shadows across the access road. The
    #           light on Aeron's face is the light
    #           from the WEST — honest, directional,
    #           going. This is the inverse of EMP s22's
    #           rising sun. The going light is the
    #           scene's argument.
    # SFX: NO civilian sounds. No child. No father
    #      answering. The loadout sounds — magazines
    #      on metal, a pack being cinched, a radio
    #      check that does NOT complete. The ABSENCE
    #      of the civilian soundscape is the scene's
    #      acoustic signature.

    "Aeron stands at the edge of the base. Below him the staging ground. Operators in loadout. A sapper checking charges. A runner cinching a pack. A comms tech running a radio check that does not complete on the first try."

    "He does not move."

    athought "Seven days. They want six. I gave them seven. That is the last concession I will make before the thing is on a calendar that cannot be moved."

    "His right hand rests on the inside of his jacket. Left side. Where the letter sits against his chest. The gesture takes less than a second. He does not look at his hand."

    athought "Still there."

    "He lets his hand drop."

    "The sun is setting over the west ridge. The light is directional and cold."

    # ========== PHASE 2 — ZIRA ==========

    # CAMERA: do NOT cut. Same rule as EMP s22 — each
    #         LI enters and exits the frame from
    #         Aeron's RIGHT (the base side, OB mirror
    #         of EMP's left). Zira first. She is
    #         moving past. She gives him the soldier's
    #         acknowledgment ONLY — not the lingering
    #         glance of EMP s22. One long take begins
    #         here. The camera does not cut between
    #         LIs; the edit is coming and going.
    # FACE: Zira — the soldier face. The cold
    #        version of the workshop face. No
    #        warmth is permitted in this composition,
    #        and she is not giving any.

    "Footsteps behind him and to his right. He does not turn."

    "Zira moves past him along the wall. A soldier's walk — not quick, not slow. A pack on her back. Her hands at her sides."

    "She does not stop."

    "She raises one hand as she passes him. Not a touch. Not a lover's gesture. The small sideways lift of the palm a soldier gives a commander to say: acknowledged."

    "She does not meet his eyes."

    "She is gone before the acknowledgment has finished settling."

    athought "She has been planning the undercity corridor for a month. She told me she was holding it. She did not tell me she was holding it FOR this."

    athought "She will not come to the edge of the base as a woman tonight. She will come to it as the operator who is going to get me through the door."

    athought "That is what she is offering. It is not nothing."

    # ========== PHASE 3 — NOELLE ==========

    "More footsteps. Slower. Noelle."

    "She stops beside him. Close enough that he can see the edge of the tablet she is holding. Far enough that she is not in his personal space."

    "She does not greet him."

    n "Ready."

    "She hands him the tablet."

    "He takes it."

    "On the screen: the updated framework. Version 2. She has not labeled it. She has not named it. The file is simply called OP-203."

    athought "On the other path she would have called it version two. Warmly. Here it has an operation code."

    athought "That is the taxonomy she chose."

    "He scrolls one page. The framework accounts for Rhea's acceleration, for the Sector 12 losses, for the seven dead of yesterday. The math is clean. The predicted success rate is 74%%."

    athought "She is being honest about the number. Seventy-four is not a flattering number. She is not flattering me."

    "He hands the tablet back."

    a "Thank you."

    "She takes it."

    "She does not say anything else."

    "She turns."

    "She walks on."

    athought "She declared herself a weapon three nights ago. This is the first weapon she has handed me. It is made of numbers and it is pointed at a woman I have never met."

    athought "I am going to use it."

    # ========== PHASE 4 — TESSA ==========

    # CAMERA: the CONDITIONAL phase. Branch A: Tessa
    #         enters the held frame with the clip lamp
    #         from s06 OB — the lamp that has been her
    #         object through the act. Branch B: she
    #         does NOT come. The frame HOLDS FOR A
    #         BEAT in the space where she would have
    #         been. The camera does not cut to fill
    #         the absence. The absence is the shot.
    #         EMPTY FRAME HELD is the scene's most
    #         important composition in branch B.
    # FX/COMP: in branch A the clip lamp is the
    #          object Tessa brings. In branch B she
    #          brings nothing because she is not
    #          bringing herself. Either branch reads
    #          as cost paid.

    # ---- Branch on Tessa state ----

    if canon_get("ob.tessa.choice") == "stay_and_resist":

        "Footsteps. Slower still. A specific weight to them — carrying something."

        "Tessa."

        "She stops beside him. She is holding the clip lamp — the lamp from her board, the lamp she left in the medical wing at the end of s06, the lamp she took back at some point between s16 and tonight."

        "She puts it in his hand."

        "She does not explain."

        t "Bring it back."

        "She says only those three words."

        "His fingers close around the lamp. It is cold. The plastic of the shade is still warm from her hand."

        a "I will try."

        t "Bring it back."

        "She walks on."

        "He stands with the lamp in his hand and watches her walk for half a second before his eyes return to the staging ground."

        athought "She is trusting me with the object she uses to keep the names operational-not-operational. She is trusting me with the object and not with the promise."

        athought "She did not say bring me back. She said bring IT back."

        athought "She is telling me what she can count on."

        $ canon_set("ob.tessa.lamp_to_aeron", True)
        $ tp_seed("a4.ob.tessa.bring_it_back")

    else:
        # Branch B — Tessa does not come

        "He waits for footsteps."

        "The space where her footsteps would be is a space that does not fill."

        "It does not fill."

        "It does not fill."

        "The staging ground continues below him. The radio check completes on the second try."

        athought "She is not coming to the edge."

        athought "I asked her in s19 if she would teach the next trainee. She said no."

        athought "This is what no looks like when it goes all the way out to the wall."

        "He does not turn to see if she is anywhere in the base. He does not let himself."

        athought "If I turn, I am asking. If I ask, I am making her answer me. She has already answered me. The space where her footsteps would be is the answer."

        "He lets the absence stand where it is."

        $ canon_set("ob.tessa.absent_from_edge", True)
        $ tp_seed("a4.ob.tessa.space_that_does_not_fill")

    # ========== PHASE 5 — LYRA ==========

    # CAMERA: Lyra enters from the right. She does
    #         NOT speak. The Band is the gesture.
    #         Insert briefly on her wrist at the
    #         moment she passes — the Band is still
    #         cinched past comfort, same notch as
    #         s04, s14, s25. The insert is the only
    #         moment the camera leaves the held wide
    #         during the relay. Return to the wide
    #         after the insert. Lyra continues
    #         through the frame and exits.
    # FX/COMP: the Band insert is the scene's
    #          callback thread — every OB Lyra scene
    #          in Act 4 has closed on that notch. The
    #          notch is now a motif.

    "Footsteps again. Lighter. A priest's walk — not soundless, but measured, the way a body moves when a body has been taught to move in a sanctuary."

    "Lyra."

    "She stops beside him. She does not hold anything. Her hands are empty."

    "She does not speak."

    "She raises her right hand to her own left wrist."

    "She puts her palm flat against the Band."

    "She holds it there for the length of a full breath."

    "Her eyes are on the staging ground, not on him."

    athought "She is counting. That is the gesture. She asked the Six to count the assassination against her last night. She is showing me — showing the staging ground — that the counting is active."

    athought "She is not saying anything because the gesture is the sentence."

    "She lowers her hand."

    "She walks on."

    "She does not look at him at any point in the passage."

    athought "If she had looked at me, the counting would have been for me. She is keeping it honest. The counting is for the act, not for the man who ordered the act."

    athought "That is the mercy she is offering. It is a small mercy. I will take it."

    # ========== PHASE 6 — NYRA ==========

    # CAMERA: Nyra enters LAST. She does not walk
    #         past. She STOPS beside him — the OB
    #         mirror of Selene stopping beside him in
    #         EMP s22. A long silent beat before her
    #         line closes the act. The held wide now
    #         contains two standing figures at the
    #         edge of the base watching the loadout.
    #         The camera continues not to cut.
    # FACE: Nyra — the doctrinal face from s24,
    #        redeployed for the closing beat. She
    #        is not offering; she is confirming.
    # SFX: her arrival step. Then silence for one
    #      full breath before her line. Mark the
    #      breath. The silence is her line that is
    #      not yet a line — same audio grammar as
    #      Selene's arrival in EMP s22.

    "A long space after Lyra leaves the frame. Longer than the spaces between the others."

    "The last footsteps are slower than any of the earlier ones. Deliberate. Not a walk — an arrival."

    "Nyra."

    "She does not stop beside him the way the others did. She stops CLOSE. Close enough that her shoulder is almost against his shoulder. Not touching. Almost."

    "She does not speak for a full breath."

    "Then another."

    "Then the line."

    ny "Chapter four. We did not flinch."

    "Aeron does not respond."

    "He does not nod."

    "He does not look at her."

    "She does not need him to do any of those things."

    "She stays beside him for one more breath."

    "Then she turns and walks back toward the base, not toward the staging ground — she will be at the ritual after, not in the operation."

    athought "She mirrored it. The line. The one the other path would have used on the other side of the same wall. She knows the shape of a chapter close. She is naming the chapter for me because no one else in the building can."

    athought "We did not break is the other line. Hers. In a room I am never going to be in."

    athought "We did not flinch is the line in the room I AM in."

    athought "Both rooms exist. I am in one of them. Tonight that is true in a way it was not true yesterday."

    # ========== PHASE 7 — AERON ALONE ==========

    # CAMERA: the ONLY camera move — pull back ONE
    #         small step (same as EMP s22). The
    #         staging ground in mid-ground, smaller
    #         now. Aeron in the foreground alone.
    #         The sun per the opening block. Hold
    #         the wider wide. The held low string
    #         enters here — held FLAT per the
    #         opening block. No rise. No fall. Flat.
    #         This is the scene's closing sound and
    #         it is the scene's closing argument:
    #         OB does not resolve.

    "He is alone at the edge again."

    "Below him the staging ground continues its work. The sapper finishes the charges. The runner cinches a second pack. The comms tech moves on to the next unit."

    "The sun is going. The light is on the west side of his face."

    "He takes one step forward — a single step — and stops at the new edge."

    "His right hand goes once more to the inside of his jacket. Left side. The letter."

    "Still there."

    "He lowers his hand."

    # ---- Final internal line ----

    athought "She thought a pause was possible. I am walking into the room she walked out of. I am carrying her letter. I am not going to find her again."

    "One long low string, flat, held."

    "The string does not rise."

    "The string does not fall."

    "The string holds."

    # ========== PHASE 8 — TITLE CARD ==========

    # CAMERA: fade the wider wide on the staging
    #         ground and Aeron at the edge of it. The
    #         flat string does not resolve — it cuts
    #         on a continuing pitch when the fade
    #         completes. Title card enters on black.
    #         This is the final frame of Act 4 OB
    #         and the final act-close of the 47-scene
    #         stage-direction pass.

    # show blackout with dissolve
    # show text "END OF CHAPTER IV" at truecenter with dissolve
    # pause 2.0
    # show text "CHAPTER IV — VIOLENCE NORMALIZED" at truecenter with dissolve
    # pause 2.5
    # hide text with dissolve

    "END OF CHAPTER IV"

    "CHAPTER IV — VIOLENCE NORMALIZED"

    # ========= SCENE END TASKS =========
    $ canon_set("act4.ob.close", "delivered")
    $ tp_seed("a4.ob.handoff")
    $ flag("act4_ob_complete", True)
    $ metric("ob.aeron.chapter_four_close_index", set_to=1)
    $ scene_mark(_current_scene_id, "exited")

    return

# =======================================================
# CANONICAL NOTES
# =======================================================
# cann.scene_id: a4_s26_act_four_close_ob
# cann.chapter: IV — Violence Normalized
# cann.chapter_start: False
# cann.when_in_timeline: Dusk, day before the Rhea Vestin
#   assassination prep departs. Seven days on the clock set in
#   a4_s22_council_of_attrition_ob. The operation is on the
#   staging ground. The act closes on the edge.
# cann.what_happened:
#   - Aeron stands at the edge of the base and the five-LI
#     relay passes behind him — the dark mirror of a4_s22 EMP.
#   - Zira passes without stopping; a soldier's acknowledgment,
#     not a lover's gesture.
#   - Noelle stops briefly, hands Aeron the OP-203 tablet
#     (version 2 of her predictive framework, renamed as an
#     operation code), says one word: "Ready."
#   - Tessa is CONDITIONAL. Branch A (stay_and_resist): she
#     delivers the clip lamp from the medical wing and says
#     three words — "Bring it back." Branch B (stay_but_
#     withdraw): she does not come. The frame holds for an
#     unfilled space.
#   - Lyra does not speak. She places her palm flat on her own
#     Band — the counting gesture from a4_s25 made public at
#     the wall. She does not look at Aeron.
#   - Nyra closes the relay. She stands shoulder-close and
#     delivers the chapter-close line: "Chapter four. We did
#     not flinch." She leaves for the ritual afterward.
#   - Aeron alone. His hand checks the letter once in the
#     entire scene. He delivers the final internal line:
#     "She thought a pause was possible. I am walking into
#     the room she walked out of. I am carrying her letter.
#     I am not going to find her again."
#   - ACT IV OB TITLE CARD.
# cann.aeron_state:
#   - Carrying the letter as a gravestone (canon from s21).
#   - Head chair, not side chair (canon from s23) — the OB
#     mirror of the EMP side-chair turn.
#   - Has accepted the counting Lyra is holding on his behalf
#     (canon from s25).
#   - Has partially refused Nyra's framing (canon from s24) —
#     the sliver of self-awareness is the only light he is
#     still carrying into Act V.
#   - Has not slept. Will not sleep before the prep departs.
# cann.path_tracking: OB (Obsidian)
# cann.thematic_flags:
#   - route_question_why_didnt_they_leave: ANSWERED IN SHAPE.
#     Each LI's presence at (or absence from) the edge is the
#     shape of her answer. Zira: I am the door. Noelle: I am
#     the weapon. Tessa A: I am the lamp I have not given up.
#     Tessa B: I am the space that does not fill. Lyra: I am
#     the counting. Nyra: I am the witness who does not flinch.
#     None of them said the word "leave."
#   - violence_normalized: INSTITUTIONAL. The edge is quiet.
#     No one is shouting. No one is crying. The scene's
#     acoustic signature is the ABSENCE of a child asking a
#     question — the EMP close had a child. The OB close
#     does not.
#   - the_letter: CHECKED ONCE. One hand gesture. The audience
#     sees it if the audience is paying attention.
#   - polyamory_geometry: FORMAL. The relay is performed in
#     series, not in aggregation. None of the women are in the
#     frame together. Each stands alone with him for her
#     allotted beat. This is the OB version of distributed
#     command — a structure of loneliness, not of warmth.
# cann.character_moments:
#   - Zira: the soldier's acknowledgment. No touch. No line.
#     The only gesture is the hand-lift of a command-soldier
#     relationship. Her refusal to meet his eyes is the
#     answer to s12's "make me feel it" — tonight she is
#     choosing not to let him feel her, because tonight she
#     is the operator, and the operator does not feel.
#   - Noelle: OP-203. The label is the character beat. On EMP
#     she would have said "version two" warmly. On OB she
#     renames it to an operation code because her taxonomy
#     has followed her into the weaponization. 74% predicted
#     success — honest, not flattering.
#   - Tessa (A): the clip lamp, the three words, the fingers
#     still warm on the plastic. She trusts him with the
#     OBJECT and not with the promise. "Bring IT back" — not
#     "bring yourself." The distinction is the beat.
#   - Tessa (B): the space that does not fill. Aeron refuses
#     to turn to check if she is anywhere. If he turned, he
#     would be asking. She has already answered. The absence
#     is load-bearing.
#   - Lyra: the Band gesture. Hand flat on the wrist. A full
#     breath. The counting is active. Her eyes are on the
#     staging ground and not on Aeron — the counting is for
#     the act, not for the man. This is the last mercy the
#     scene lets Lyra offer: she is carrying his ledger
#     honestly.
#   - Nyra: the chapter-close line. "We did not flinch."
#     Consciously the OB mirror of the EMP line Aeron will
#     never hear ("We did not break"). She names it so Aeron
#     does not have to — naming chapters is not a skill he
#     is allowed to develop, because naming is a priest's
#     act and Aeron is no longer in a room where that grammar
#     is usable.
#   - Aeron: one hand gesture, one spoken line ("Thank you"
#     to Noelle in branch-neutral, or "I will try" + two
#     silent responses to Tessa in branch A, or no spoken
#     lines at all in branch B). The final internal line is
#     the act's thesis line: the letter is a gravestone and
#     not a door.
# cann.block_status: drafted
# cann.requires_followup:
#   - Act V opens with the assassination prep on day 1 of 7.
#     The calendar is canon. flag act4_ob_complete is the gate
#     for Act V OB entry.
#   - The letter in Aeron's jacket is a canonical object now.
#     Any Act V internal monologue may reference it. Any Act V
#     scene that puts Aeron near a mirror, a confession, or a
#     woman who reminds him of his mother may access it.
#   - OP-203 / Noelle's weapon-framework is the operative
#     plan for the assassination. Act V must run it.
#   - Tessa branch state is a hard canonical split. All Act V
#     Tessa scenes must check canon_get("ob.tessa.choice") and
#     branch accordingly. If Branch B, Tessa is the empty
#     chair in every scene that would have had her.
#   - Lyra's counting is a live spiritual state. Act V Lyra
#     beats may return to the ledger she is carrying.
#   - Nyra's "we did not flinch" is now the canonical OB
#     chapter-close line. Act V openers should not echo it.
#   - The "pause is a gravestone" formulation from s21 is the
#     canonical Aeron position on his mother for the remainder
#     of the OB path. Any softening in Act V must go through
#     a scene that earns it.
#   - Rhea Vestin is still alive and still named as the target.
#     The collision is deferred seven days into Act V.
#   - The seven civilians killed in the Sector 12 sweep (s09)
#     and the seven Phoenix dead from s18 are the act's total
#     named ledger. Act V opens with both numbers in the
#     background.
#   - Act IV OB path is formally closed by this scene.
