# =======================================================
# ACT 3 - Scene 25: Aftermath (Obedience Path)
# File: a3_s25_aftermath_ob.rpy
# Type: TRANSITION TO ACT 4
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s25_aftermath_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s25_aftermath_ob:

    $ show_timeline("DAY 42", "18:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, steady. Wide on the war room. Tightens to each speaker.
    #         Final shot: Aeron at the table, alone. The lights on. The room obedient.
    # LIGHTING: War room. Overheads at full. Tactical displays cycling. Cold.
    # SFX: Loop -- generator hum. Ventilation. The base breathing on schedule.
    # FACE: Everyone changed. Not broken. Colder. Except Zira, who might be breaking.

    # ========= VOICE BASELINE =========
    # Brief. Each LI gets one beat. The colder mirror of EMP's aftermath.
    # The room complies. The silence is obedient.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - MORNING]

    #scene bg_war_room_ob with dissolve
    #play ambient "sfx/ambient/war_room_quiet.ogg" fadein 2.0

    # ========== THE MORNING AFTER ==========

    "Morning. The war room fills by rotation, not gravity. Scheduled. Punctual."

    "Nobody mentions yesterday."

    "Nobody needs to."

    # ========== EACH LI -- BRIEF, DISTINCT ==========

    # --- NYRA ---

    ny "Her weakness is not our concern. We proceed."

    "She says it standing. At parade rest. The posture she defaults to when the world requires clarity."

    ny "The Outlander channels can be useful. Her network, her courier infrastructure -- those have tactical value. Her opinions do not."

    ny "The mission is unchanged. The command structure is intact."

    athought "She's already filed it. Mother. Reunion. Rejection. Filed under 'irrelevant personal' and sealed."

    athought "She's efficient."

    athought "I should find that reassuring."

    # --- ZIRA ---

    z "...Yeah. We proceed."

    "Three words. The ellipsis before them holds everything she isn't saying."

    "She's not looking at Aeron."

    "She's looking at the Ghostline terminal. At the courier routes on the display. The routes Liora built. The roads beneath Zira's roads."

    athought "She can't look at me."

    athought "She's staring at the infrastructure my mother created and she can't look at the man my mother walked away from."

    athought "I don't blame her."

    # --- TESSA (conditional) ---

    if flag("tessa_stayed_s10"):

        "Tessa adds nothing."

        "She stands by her board. The names. Living and dead. She doesn't look at it. She doesn't look at the table."

        "She looks at the map on the far wall. Sector lines. Territory markers."

        "The look of someone planning an exit route she'll never take."

        athought "Tessa is quiet."

        athought "Yesterday she said 'she's right, you know.' Today she says nothing."

        athought "The diagnosis was delivered. There's nothing left to prescribe."

    # --- NOELLE ---

    n "Behavioral analysis of the confrontation suggests--"

    a "Not now, Noelle."

    "She stops. Her stylus hovers. Two seconds."

    "She nods. Saves the file. Closes the display."

    n "Understood."

    athought "She had the whole thing mapped. The meeting. The emotional indices. The behavioral deviations from my baseline."

    athought "She wanted to show me the data. Show me the shape of what happened in clean numbers."

    athought "I don't want to see the shape."

    athought "I already know what shape it is."

    # --- LYRA ---

    l "I'll pray for her. And for you."

    "She says it simply. Not as challenge. Not as comfort. As fact."

    l "You need it more."

    athought "She said 'you need it more.'"

    athought "She's right."

    athought "I won't tell her that."

    # ========== AERON ==========

    "They're looking at him. Waiting. The room held in the particular tension of a team that doesn't know what their commander will say next."

    athought "My mother walked away from me yesterday."

    athought "She called me by my full name like a verdict."

    athought "She said 'so did your father, word for word.'"

    athought "She slapped me. Once. And it's the most honest thing anyone has done to me in months."

    a "We have operations to plan."

    "The room receives the sentence."

    "Nyra nods. Immediate. Clean."

    "Zira turns to her terminal. Her hands begin to move."

    "Noelle opens her display. The stylus resumes."

    "Lyra unfolds her hands. Sits straighter."

    if flag("tessa_stayed_s10"):
        "Tessa picks up her kit. Moves to the door. Pauses. Doesn't turn. Leaves."

    "The room complies."

    "The silence is obedient."

    athought "We have operations to plan."

    athought "The machine runs."

    athought "The machine runs and my mother is in the Outlands keeping the names of the dead and she looked at me and saw the man she ran from."

    athought "The machine runs."

    athought "It has to be enough."

    "The tactical displays cycle. The patrol routes. The supply lines. The operational calendar."

    "The war room hums."

    "The lights stay on."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("act3_complete", True)
    $ canon_set("act3_resolution_ob", "iron_consolidation")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s25_aftermath_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after Liora confrontation (s24). Transition to Act 4.
# cann.what_happened:
#   - Brief. Each LI gets one beat. The colder mirror of EMP's aftermath.
#   - Nyra: "Her weakness is not our concern. We proceed." Files it under irrelevant.
#   - Zira: "...Yeah. We proceed." Not looking at Aeron. Looking at Liora's courier routes.
#   - Tessa (if present): adds nothing. Looks at the map. Planning an exit she'll never take.
#   - Noelle: "Behavioral analysis--" "Not now, Noelle." She stops. Saves. Closes.
#   - Lyra: "I'll pray for her. And for you. You need it more."
#   - Aeron: "We have operations to plan." The room complies. The silence is obedient.
#   - "The machine runs. It has to be enough."
# cann.aeron_state:
#   - Sealed. The mirror cracked the mask yesterday. Today the mask is back.
#   - "The machine runs." The OB mantra after the mirror scene.
#   - He knows it isn't enough. He proceeds anyway.
# cann.path_tracking:
#   - flag("act3_complete"). canon_set("act3_resolution_ob", "iron_consolidation").
#   - No player choice. Transition scene.
# cann.thematic_flags:
#   - "The silence is obedient": the OB thesis in five words. The room does what it's told.
#   - "Iron consolidation" vs EMP's "broadcast witness": the two Act 3 resolutions.
#     EMP turns grief into public truth. OB turns grief into operational continuity.
#   - Lyra's "You need it more": the one line that breaks through.
#   - Noelle's "Not now": Aeron refusing his own behavioral data. He doesn't want to see the shape.
#   - "The machine runs": repeated. The repetition is the crack.
# cann.character_moments:
#   - Each beat mirrors EMP aftermath but colder:
#     EMP Selene: "Marcus just made this personal." OB Nyra: "Her weakness is not our concern."
#     EMP Zira: "I just made her louder." OB Zira: "...Yeah. We proceed." (Not looking.)
#     EMP Tessa: adds name to board. OB Tessa: adds nothing. Looks at exit routes.
#     EMP Noelle: "Direct chain of causation." OB Noelle: cut off. "Not now."
#     EMP Lyra: prayer as threat. OB Lyra: prayer as grief. "You need it more."
# cann.callbacks:
#   - a3_s24: Liora's confrontation. Everything here is the morning after the mirror.
#   - a3_s23 (EMP): The EMP aftermath. Point-for-point comparison in colder register.
#   - a3_s01: "I feel efficiency." Full circle. The efficiency that started Act 3 ends it.
#   - The machine: the metaphor that carries OB Aeron into Act 4.
# cann.block_status:
#   - ANCHOR (OB). Act 3 closer. Transition to Act 4.
# cann.requires_followup:
#   - Act 4 opens on the iron consolidation. Aeron after the mirror.
#   - Liora's archive: tactical asset or personal reckoning?
#   - Zira's inability to look at him: where does this go?
#   - Tessa's exit-route look: does she leave? Can she?
#   - The machine: does it run? For how long?
#   - "You need it more": Lyra's line. The prayer that follows Aeron into Act 4.
