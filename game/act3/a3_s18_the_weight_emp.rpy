# =======================================================
# ACT 3 - Scene 18: The Weight (Empathy Path)
# File: a3_s18_the_weight_emp.rpy
# Type: PAIR ANCHOR (A3_P13: Tessa x Selene)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s18_the_weight_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s18_the_weight_emp:

    $ show_timeline("DAY 35", "00:30", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked on tripod. Steady. The stillness is the point.
    #         Opens wide on the command table — empty chairs, maps, the holo-surface
    #         dimmed to standby. Two figures: Tessa and Selene.
    #         Aeron is peripheral — a silhouette in the corridor entrance if shown at all.
    #         The camera stays with the women. Slow tightens over the scene:
    #         two-shot to paired close-ups. Never singles — always both in frame or implied.
    #         The board moment: camera finds the list. Holds.
    # LIGHTING: War room after hours. Overhead strips OFF. The holo-table on standby casts
    #           low blue-green. A single amber practical at the edge of the table (Tessa's
    #           lamp — she brought it from the medbay). The two light sources create
    #           split-tone on their faces: cool command, warm care.
    #           Aeron's corridor: backlit silhouette only. He doesn't enter the light.
    # SFX: Loop — base night: generator hum, ventilation tick, distant watch change.
    #      One-shots — chair creak, datapad set down, pen on paper, Selene's exhale.
    #      The holo-table standby pulse: rhythmic, low. A machine heartbeat.
    # FX/COMP: The command table: cleared of tactical overlay. Just the surface.
    #          Tessa's board (portable version): names in her handwriting. The living.
    #          Two mugs — one Tessa's (chipped), one Selene's (standard issue, clean).
    # BLOCKING: Selene at the head of the table. Her chair. Always her chair.
    #           Tessa across the corner — close enough to reach, far enough to not crowd.
    #           The board between them on the table surface.
    #           Aeron at the corridor threshold. Watching. Not entering.
    # CANON: PAIR ANCHOR scene. Tessa x Selene. Non-romantic care as its own category.
    #        Selene's control-to-trust pivot begins here.
    #        Tessa's board methodology — counting the living — applied to command burden.
    #        Callbacks: a3_s13 (Scar and Steady, Tessa's hands), a3_s16 (Selene's quarters),
    #        a3_s12 (corridor op, the weight of 206 lives).
    # FACE: Selene — composed, eroding. The erosion is the scene.
    #        Tessa — steady. Her steadiness is the anchor.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, warmth, sensory weight.
    # Tessa: Clinical warmth. She speaks in observations, not arguments. Doesn't push.
    # Selene: Command cadence fraying at the edges. Shorter sentences as control slips.
    # Aeron: Internal only (athought). Observer. This scene belongs to them.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - LATE NIGHT]
    # The room that runs the rebellion, emptied of everyone who runs it.
    # Except two.

    #scene bg_war_room_night_emp with dissolve
    #play ambient "sfx/ambient/base_night_quiet.ogg" fadein 2.0

    # ========== PHASE 1 — THE EMPTY TABLE ==========

    "The war room after midnight. The overhead strips are off. The holo-table pulses on standby — low blue-green, the machine equivalent of breathing in sleep."

    "Tessa's lamp sits at the edge of the table. Amber. Portable. She carries it from room to room like other people carry worry."

    "Selene is in her chair. The chair. The one at the head of the table that no one else sits in, not because she claimed it but because command has its own gravity."

    "She's not reading reports. She's not planning. She's sitting with her hands flat on the table, staring at the surface where the tactical overlay would be."

    "Tessa is across the corner. Close enough. A mug in each hand. She sets one in front of Selene without asking."

    t "You haven't moved in two hours."

    sel "I'm thinking."

    t "You're sitting in the dark staring at an empty table."

    sel "That's a form of thinking."

    t "That's a form of something. Thinking isn't it."

    "Selene doesn't answer. Her fingers press against the table surface. Flat. Like she's holding it down."

    athought "I'm at the corridor entrance. I can see them both through the doorway."

    athought "This isn't mine to enter."

    athought "I know that the way you know the shape of a room you've already walked through — completely, without needing to check."

    # ========== PHASE 2 — TESSA'S METHOD ==========

    "Tessa pulls something from her kit bag. Not instruments — a folded sheet of paper. She unfolds it on the table between them."

    "Names. Rows of names in Tessa's handwriting. Neat, precise, the letters of someone who learned penmanship from medical charting."

    sel "What is this?"

    t "The living."

    "Selene looks at it. Then at Tessa."

    sel "This is your board."

    t "Portable version. The one on the medbay wall doesn't travel."

    sel "Why are you showing me this?"

    t "Because you've been counting the dead."

    "The sentence lands in the quiet room. The holo-table pulses. The ventilation ticks."

    t "I've watched you do it. After every operation. After every report. You count what we've lost. You calculate the cost."

    t "You're very good at it."

    sel "Someone has to be."

    t "Someone does. But that's not what's happening right now."

    "Tessa touches the list. Her finger rests on a name."

    t "Dren. Still alive. His hands are healing. He's rebuilding the workshop ventilation."

    "She moves to the next."

    t "The family from Group Four. The father who carried his daughter through the corridor. They're in the east wing. The daughter draws on the walls."

    t "The woman with the broken wrist. She's running the new mess rotation. She organizes better than half our logistics team."

    sel "Tessa."

    t "I count the living. That's what I do. Every name on this board is someone who's here because of what we built."

    t "You keep counting the dead because you think that's what command requires. And maybe it is."

    t "But someone has to count the other column. And you won't let yourself."

    # ========== PHASE 3 — THE CRACK ==========

    "Selene's hands haven't moved from the table. Flat. Pressing."

    sel "If I count the living, I have to accept that I'm responsible for them."

    t "You already are."

    sel "Responsible for losing them. For the ones who won't be on the next list."

    "Tessa doesn't flinch. Her hands are steady. The same hands that suture wounds and hold dying people and never — not once — waver when it matters."

    t "Yes."

    sel "I've been doing this for nineteen years. Longer than most of those people have been alive."

    t "I know."

    sel "I've sent people to die. Not in the abstract. I've looked at someone and made the calculation that their life was worth less than the objective."

    sel "And I was right. Every time. The math held."

    t "The math isn't what's keeping you in this chair at midnight."

    "Selene's jaw tightens. The micro-expression that means she's been seen."

    sel "No."

    "A breath. The holo-table pulses."

    sel "The math isn't what keeps me here."

    t "What does?"

    "Silence. Long enough that the ventilation tick sounds loud."

    sel "I keep count because if I stop, I'll forget what it costs."

    sel "And the day I forget what it costs is the day I become Marcus Rylan."

    menu:
        athought "There it is. The fear underneath the command weight."

        "(Stay silent. This is their moment, not yours.)":
            athought "The weight she's carrying is the fear that leadership is turning her into Marcus. Tessa sees it. I do not need to be in this."
        "(Step into the doorway so they know you heard.)":
            $ rel_bump("Selene", trust=1)
            $ rel_bump("Tessa", trust=1)
            athought "I am not going to hide the fact that I heard. They deserve to know I was listening."
        "(Leave before they see you.)":
            athought "This conversation is not for me. The fact that I heard it is a weight I will carry alone."

    # ========== PHASE 4 — THE PIVOT ==========

    "Tessa moves. Not dramatically — she shifts her chair. Closer. The corner of the table is still between them, but the distance has changed."

    t "Selene."

    t "You are nothing like Marcus Rylan."

    sel "You don't know that."

    t "I know that Marcus Rylan never sat in the dark counting the dead because he was afraid of forgetting."

    t "I know that he never once worried about what command was making him. He was too busy enjoying what it gave him."

    t "I know that the fact you're afraid of becoming him is the proof that you won't."

    "Selene's hands lift from the table. The first time they've moved. She looks at them — her own hands — as if checking what they've done."

    sel "That's not enough."

    t "No. It's not."

    "Tessa's honesty is the anchor. She doesn't soften it."

    t "Fear isn't enough to keep you human. You need people who see you. Who tell you when the count is wrong."

    t "That's why I'm here. Not because I like late nights and cold tea."

    "She pushes the board across the table. Into Selene's space."

    t "We counted the living. Two hundred and twelve names on that list as of tonight."

    t "You're one of them."

    "Selene looks at the list. Her name isn't written on it."

    sel "I'm not on the board."

    t "You never put yourself on it. So I did."

    "Tessa turns the paper. At the bottom, in the same precise handwriting, separate from the columns: SELENE WARD."

    "Selene stares at it."

    t "We counted the living. And this time, we became the number."

    athought "The line lands like it was always waiting to be said."

    athought "Like the room was built for this sentence and everything before it was furniture."

    "Selene doesn't cry. She's not the kind. But something shifts behind her eyes — a wall not falling but being set down. Deliberately. The way she sets the cipher on the nightstand."

    sel "Tessa."

    t "Yeah."

    sel "Thank you."

    "Tessa picks up her mug. Sips. The gesture is ordinary. That's the point."

    t "Drink your tea. It's getting cold."

    "Selene picks up the mug. Drinks."

    "They sit in the amber-and-blue light. The board between them. The names. The living."

    athought "I step back from the corridor entrance. Quietly."

    athought "Some rooms you don't enter because you're not needed."

    athought "And the best reason to not be needed is that someone else already is."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Tessa", trust=1, affection=1)
    $ rel_bump("Selene", trust=1, affection=1)
    $ flag("selene_trust_pivot", True)
    $ scene_mark(_current_scene_id, "anchor_seen")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s18_the_weight_emp
# cann.chapter: Act III, Phase III — Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After Faith in Flaws (s17) and the deepening arcs.
#   - Late night at the command table. The weight of operations accumulating.
# cann.what_happened:
#   - Tessa finds Selene alone at the command table after midnight. Staring. Not planning.
#   - Tessa brings her board — the portable list of the living. Her methodology.
#   - Selene has been counting the dead. The cost. She can't stop because stopping
#     means forgetting, and forgetting means becoming Marcus Rylan.
#   - Tessa: "The fact you're afraid of becoming him is the proof that you won't."
#     But fear isn't enough — she needs people who see her.
#   - The pivot: Tessa put Selene's name on the board. "We counted the living.
#     And this time, we became the number."
#   - Selene accepts support. Not weakness — trust. The control-to-trust pivot begins.
#   - Aeron observes from the corridor. This scene belongs to Tessa and Selene.
# cann.aeron_state:
#   - Observer. Peripheral. He recognizes that this room isn't his.
#   - "The best reason to not be needed is that someone else already is."
# cann.path_tracking:
#   - rel_bump("Tessa", trust=1, affection=1). rel_bump("Selene", trust=1, affection=1).
#   - flag("selene_trust_pivot") — begins Selene's arc from control to trust.
#   - scene_mark("anchor_seen") — PAIR ANCHOR for Tessa x Selene.
# cann.thematic_flags:
#   - Motifs: The board (living vs dead, counting as care), the command table (empty/full),
#     amber vs blue-green (care vs command), the cipher callback (set down deliberately).
#   - "We counted the living. And this time, we became the number." — the key line.
#   - Non-romantic care as its own full category. Tessa doesn't want Selene. She sees her.
#   - The Marcus fear: Selene's deepest terror is that command is turning her into Marcus.
#     Tessa's answer: the fear itself is the proof. But you also need witnesses.
# cann.character_moments:
#   - Tessa: Steady. Honest without softening. "Not because I like late nights and cold tea."
#     Her board methodology as emotional intervention. Hands steady. Always.
#   - Selene: Erosion of composure. "The math isn't what keeps me here." Accepts being seen.
#     Picks up the mug. The ordinary gesture as capitulation.
#   - Aeron: Steps back. Knows when to leave a room. Growth.
# cann.callbacks:
#   - a3_s12: Corridor op. 206 lives. The weight of those numbers on command.
#   - a3_s13: Scar and Steady. Tessa's hands. The board.
#   - a3_s16: Selene's quarters. The cipher set down on the nightstand.
#   - The nineteen-year burden: consistent through Selene's arc.
#   - Marcus Rylan: the shadow figure. Named here as Selene's fear.
# cann.block_status:
#   - PAIR ANCHOR. No player choice. No branching. The scene earns itself through accumulation.
# cann.requires_followup:
#   - Selene's trust pivot: she begins allowing support. Visible in future command dynamics.
#   - Tessa's board: the list continues to grow. Selene's name is on it now.
#   - The Marcus comparison: will recur when the Purge data reveals his signature.
#   - Tessa-Selene dynamic as non-romantic anchor: foreshadows poly-structure trust patterns.
