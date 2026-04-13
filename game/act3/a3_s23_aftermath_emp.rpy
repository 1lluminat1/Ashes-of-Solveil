# =======================================================
# ACT 3 - Scene 23: Aftermath (EMP)
# File: a3_s23_aftermath_emp.rpy
# Transition to Act 4.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s23_aftermath_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s23_aftermath_emp:

    $ show_timeline("DAY 42", "18:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, steady. Starts wide on the ops room — emptier than the bookend scene.
    #         Tightens as each LI speaks. Final shot: Aeron at the table, alone, dawn light.
    # LIGHTING: Pre-dawn. Cold blue bleeding into amber at the edges. Tessa's board visible.
    # SFX: Loop — generator hum. Nothing else. The base is holding its breath.
    # FACE: Everyone changed. Not broken — hardened. There's a difference.

    # ========== THE MORNING AFTER ==========

    "Nobody slept."

    "The ops room fills in ones and twos. Not by order — by gravity. The table pulls them in because there's nowhere else to go."

    "Liora Rylan's name is on Tessa's board. Fresh ink. The newest entry on the dead side."

    # ========== EACH LI — BRIEF, DISTINCT ==========

    sel "I've spent nineteen years building a rebellion that could survive anything Echelon threw at it."
    sel "I never planned for this. For the enemy to kill the commander's mother and call it policy."
    sel "(to Aeron) Marcus just made this personal for every person in this building. Not just you. All of us."

    t "She kept names. That's what the couriers say. She kept the names of everyone Echelon erased."
    t "And Echelon erased her for it."
    t "(quiet) I added her to the board. Both sides. She's counted among the living — everything she saved. And among the dead."

    z "The Ghostline remembers. I've already seeded her courier ledgers into every active node."
    z "Every contact she ever made will know what happened. Every name she kept will know who killed the keeper."
    z "(hard) They wanted to silence her. I just made her louder."

    n "The execution was broadcast on seven Echelon feeds simultaneously. Viewership data suggests 2.3 million direct witnesses."
    n "That's not suppression. That's propaganda. Marcus wanted this seen."
    n "(pause) He also wanted YOU to see it. The feed routing prioritized our sector."

    l "I prayed last night. For the first time in weeks, I actually prayed."
    l "It didn't sound like a prayer. It sounded like a threat."
    l "(fierce, quiet) Good."

    # ========== AERON ==========

    "They're all looking at him."

    "The cipher is on the table. Selene's hand near it. The board behind them. The names."

    athought "My father killed my mother."
    athought "Not because she fought him. Because she remembered."
    athought "Because remembering is the most dangerous thing you can do to a system that survives by forgetting."

    a "We don't stop."

    "The room waits."

    a "We don't mourn forever. We don't retreat. We don't negotiate."

    a "We finish this."

    sel "How?"

    a "Noelle has the data. Zira has the network. Lyra has the faith. Tessa has the names."
    a "And you and I have command."

    a "We take everything she kept — every name, every story, every record Echelon tried to erase — and we broadcast it."
    a "Not as intelligence. As witness."
    a "The city hears what happened. Every sector. Every tier. The truth, spoken in the voices of the people it was done to."

    sel "(studying him) That's not a military operation."

    a "No. It's what she would have done."

    "Silence."

    sel "...Then we do it her way."

    # ========== ACT TRANSITION ==========

    "The room shifts. Not into grief — into purpose."

    "Tessa touches the board. Zira opens a Ghostline terminal. Noelle pulls the Purge data. Lyra closes her eyes and breathes."

    "Selene picks up the cipher and sets it between them."

    sel "Act Four."

    a "Act Four."

    pause 1.5

    scene black with fade

    centered "{size=+20}END OF ACT III{/size}"
    pause 1.0
    centered "{size=+10}The Cost of Compassion{/size}"
    pause 2.0
    scene black with fade

    # ========== STATE UPDATES ==========

    $ flag("act3_complete", True)
    $ canon_set("act3_resolution", "broadcast_witness")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s23_aftermath_emp
# cann.chapter: Act III, Phase III — Revelation & Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after Liora's execution. Transition to Act 4.
# cann.what_happened:
#   - The team processes Liora's death. Each responds in character.
#   - Selene: "Marcus just made this personal for everyone."
#   - Tessa: added Liora to both sides of the board. Living (what she saved) and dead.
#   - Zira: seeded her ledgers into every Ghostline node. "I just made her louder."
#   - Noelle: the execution was propaganda. 2.3 million witnesses. Feed routed to their sector.
#   - Lyra: prayed. It sounded like a threat.
#   - Aeron: "We finish this." Proposes broadcasting Liora's records as witness testimony.
#   - Selene agrees: "We do it her way."
#   - Act 3 ends: "The Cost of Compassion."
# cann.aeron_state:
#   - Grief transformed into purpose. Not revenge — witness. Liora's method, not Marcus's.
#   - The broadcast plan is EMP's thesis: truth spoken in the voices of the people it was done to.
# cann.path_tracking:
#   - No player choice. This is a consequences/transition scene.
#   - flag("act3_complete"), canon_set("act3_resolution", "broadcast_witness")
# cann.thematic_flags:
#   - "The Cost of Compassion" — Act 3 EMP subtitle. Compassion has teeth. It also bleeds.
#   - Liora on both sides of Tessa's board — she is simultaneously the living (her legacy) and the dead.
#   - Zira making her louder — the Ghostline as memory infrastructure.
#   - Lyra's prayer as threat — faith weaponized by grief.
#   - "Not as intelligence. As witness." — the EMP answer to Echelon's propaganda.
# cann.character_moments:
#   - Each LI gets one beat. Brief. Distinct. No over-closure.
#   - Selene and Aeron's exchange at the end mirrors the shared command promise from s01.
# cann.block_status:
#   - ANCHOR (EMP). Act 3 closer. Transition to Act 4.
# cann.requires_followup:
#   - Act 4 opens on the broadcast operation.
#   - Liora's courier ledgers become the rebellion's most powerful weapon.
#   - Marcus's response to the broadcast drives Act 4's conflict.
