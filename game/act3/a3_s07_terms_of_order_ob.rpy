# =======================================================
# ACT 3 - Scene 07: Terms of Order (Obedience Path)
# File: a3_s07_terms_of_order_ob.rpy
# Path: OB
# Type: NYRA INTEGRATION
# Character Focus: Nyra, Ensemble (fracture scene)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s07_terms_of_order_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy

label a3_s07_terms_of_order_ob:

    $ show_timeline("DAY 26", "06:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked tripod. Wide establishing of war room, then slow coverage rotation
    #         around the table. Each speaker gets a clean close-up. Nyra framed center
    #         when she addresses the room -- symmetrical, deliberate. Lyra's reaction shot:
    #         she's watching Aeron, not Nyra. Hold on that.
    # LIGHTING: War room tactical blue. Cooler than previous scenes. The overhead strips
    #           cast harder shadows now -- someone adjusted them. Nyra's people, probably.
    #           The displays behind Nyra show new patrol grids. Reorganized overnight.
    # SFX: Loop -- base hum (colder variant), ventilation drone, boot steps in corridor.
    #      One-shots -- datapad placement, chair shift, door hiss, Nyra's precise footsteps.
    # FX/COMP: Tactical displays show restructured patrol routes. New designations.
    #          Section C housing grid visible. Nyra's soldiers in formation through window.
    # BLOCKING: Team around war table. Nyra stands at the display wall -- Selene's old
    #           briefing position. Nobody invited her there. She just... took it.
    #           Aeron at the head. Zira opposite, arms crossed. Lyra in the corner.
    # CANON: Morning after provisional acceptance. Nyra reorganized command hierarchy overnight.
    #        The rebellion's character changes here. More efficient. Less warm.
    # FACE: Zira hostile. Tessa troubled. Noelle neutral-supportive. Lyra breaking quietly.

    # ========= VOICE BASELINE =========
    # OB Aeron: Fewer contractions. Clinical assessment. Sides with efficiency.
    # Nyra: Calm authority. She has already decided. Your discomfort is noted.
    # Zira: Hostile, possessive. She sees the infiltration she warned about.
    # Tessa: Genuine concern for the human cost of restructuring.
    # Noelle: Data-forward. Supportive of the math, not the ideology.
    # Lyra: Almost silent. Watching. Something in her is breaking.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - MORNING]
    # The war room has changed overnight. The tactical displays show new patrol grids.
    # New designations. New structure. Nyra's work. Done between 0200 and 0600
    # while the rest of the base slept.

    #scene bg_war_room_ob with dissolve
    #play ambient "sfx/ambient/base_hum_cold.ogg" fadein 2.0

    # --- OPENING: THE NEW ORDER ---

    "The war room is different."

    "It takes a moment to register why. The furniture hasn't moved. The displays are in the same positions. But the information on them has been rewritten."

    "New patrol grids. Overlapping coverage zones. Rotation schedules that account for fatigue ratios and sightline gaps. The kind of planning that takes twelve hours or three -- depending on who is doing it."

    athought "She did this overnight. Four hours of work that would have taken our planning staff two days."

    athought "I should be impressed. I am impressed."

    athought "That is the problem."

    #show nyra war_room_display with dissolve

    "Nyra stands at the display wall. Selene's old briefing position. Her hands clasped behind her back, datapad resting on the table beside her. She didn't ask for the position. She occupied it."

    "Behind the reinforced window, her seventeen soldiers run drills in the staging area. Silent. Synchronized. The Phoenix fighters watch from the periphery with expressions that range from fascination to unease."

    #show zira war_room_seated with dissolve
    #show tessa war_room_seated with dissolve
    #show noelle war_room_seated with dissolve
    #show lyra war_room_corner with dissolve

    "The team filters in. Zira first, jaw already set. Tessa with her medkit strap twisted -- she slept badly. Noelle with her stylus moving before she sits down."

    "Lyra last. She takes the chair furthest from the display wall. Furthest from Nyra."

    athought "She is watching me. Not Nyra. Me."

    athought "She wants to see whose side I take."

    # --- NYRA'S BRIEFING ---

    ny "Good morning. I've prepared an operational assessment based on last night's restructuring."

    z "Last night's what?"

    ny "Restructuring. I reviewed your patrol schedules, supply chain protocols, and communication redundancies. There were inefficiencies."

    z "You reviewed our operational security in your first twelve hours here."

    ny "I reviewed what was accessible. Your encryption is adequate. Your scheduling is not."

    "Zira's fingers tighten on the table edge."

    athought "She is right to be angry. Nyra moved through our systems in a single night."

    athought "But the patrol grids on that screen are better than anything we have produced in three weeks."

    ny "The primary changes: patrol routes now overlap at seventeen-minute intervals instead of forty. Response time to any sector breach drops from nine minutes to under four."

    ny "Supply runs are consolidated into three convoys instead of seven. Fewer movements, less exposure, same throughput."

    ny "Communication relays rerouted through secondary Ghostline nodes to reduce interception surface."

    "She delivers each point the way a surgeon describes an incision. No affect. No pride. Just architecture."

    n "The coverage math checks out. Seventeen-minute overlaps are tight but sustainable with the expanded roster."

    ny "Correct. The expanded roster is essential. Without my soldiers filling the gaps, the schedule collapses."

    z "How convenient. Your restructuring only works if your people are embedded in every rotation."

    ny "Yes."

    "No deflection. No justification."

    ny "Integration requires integration. If you want the benefit of seventeen soldiers, they must be woven into the structure. Not held in a cage and consulted when you need muscle."

    # --- THE FRACTURE ---

    t "Can we slow down?"

    "Tessa's voice cuts through the tactical static. She isn't angry. She is worried."

    t "These are people. The fighters on those patrol routes -- they've been running them for months. They know the terrain, the timing, the rhythm. You're asking them to learn a new system overnight."

    ny "I'm asking them to learn a better system. The timeline is theirs to manage."

    t "Discipline isn't healing. These people lost their commander three days ago. They need time to grieve, not a new drill sergeant."

    "Nyra's head tilts. The same bird-of-prey assessment she gave in the rain."

    ny "Grief is a luxury the enemy does not observe. Echelon will not pause their operations because Phoenix is mourning."

    ny "The kindest thing I can do for your people is make them harder to kill."

    athought "She is not wrong."

    athought "But Tessa is not wrong either."

    athought "The difference is that Nyra's argument ends with a number I can use."

    z "I want to say something and I want everyone in this room to hear it."

    "Zira stands. The chair scrapes against the floor."

    z "People like that don't defect -- they infiltrate."

    "She points toward the window. The seventeen soldiers drilling in perfect unison."

    z "I've run Ghostline long enough to know what loyalty looks like. That isn't loyalty. That's programming. And now their handler is rewriting our entire operational framework twelve hours after walking through the door."

    z "This isn't integration. This is occupation."

    "The word lands. Occupation. It hangs in the recycled air."

    "Nyra does not react. No flinch. No defense. She waits for it to settle."

    ny "Your concern is noted."

    z "Don't give me 'noted.' I'm not filing a report. I'm telling you to your face: I don't trust you. I don't trust your soldiers. And I don't trust what you're doing to this rebellion."

    ny "I understand. And you're right to be cautious."

    "The agreement defuses Zira's momentum. It is hard to argue with someone who validates your suspicion."

    ny "I am not asking for trust. I am asking for time. Watch my soldiers. Test them. Assign them the worst rotations. Put them in positions where betrayal would be obvious and costly."

    ny "If they fail, you will know. If they serve, you will know that too."

    "Zira's jaw works. She has nothing to counter that isn't emotion."

    z "Aeron."

    "She turns to him. The whole room turns."

    z "This is your call. Tell me you see what I see."

    # --- NOELLE'S DATA ---

    "Noelle looks up from her tablet. Her voice is neutral, measured."

    n "Forty-three percent combat effectiveness increase confirmed with the new rotation schedules. Patrol coverage gaps reduced by sixty-one percent. Supply exposure windows cut in half."

    n "The restructuring is sound."

    z "The restructuring makes us dependent on her people."

    n "Dependency and improvement are not mutually exclusive."

    z "They are when the dependency is engineered."

    "Noelle pauses. Considers."

    n "That's a valid concern. But the data doesn't support rejecting the plan. It supports monitoring the implementation."

    # --- LYRA'S SILENCE ---

    "Lyra has not spoken."

    "She sits in the corner chair, hands in her lap, watching the exchange with an expression that is difficult to read. Not anger. Not agreement."

    "Something quieter. Something heavier."

    athought "She is looking at me."

    athought "Not at the displays. Not at Nyra. Not at the argument."

    athought "At me."

    athought "Waiting to see what I choose."

    a "Lyra. You've been quiet."

    "Her eyes widen slightly. She didn't expect to be called on."

    l "I don't have data to add. Or objections."

    a "That isn't what I asked."

    "A pause. Her fingers twist in her lap."

    l "I think the patrol schedules are good. I think the structure makes sense."

    l "I think we should be careful about how fast we change."

    "Her voice is even. Controlled. But something underneath it is fracturing."

    athought "She is not talking about patrol schedules."

    athought "She is talking about me."

    # --- AERON DECIDES ---

    "The room waits."

    athought "Zira sees a threat. Tessa sees a cost. Noelle sees a number. Lyra sees... me."

    athought "They are all correct."

    athought "The question is which truth I act on."

    a "The restructuring stands."

    "Zira's jaw locks."

    a "Nyra's soldiers integrate into the rotation schedule effective today. Squad leads retain authority over their teams. Nyra coordinates with me on operational planning."

    a "Zira -- you maintain Ghostline independence. No one touches your systems without your clearance. That includes Nyra's communication rerouting. You vet every node change personally."

    z "Damn right I do."

    a "Tessa -- I want you to assess the existing fighters. Morale, stress, readiness. If the new schedule is grinding anyone down, I need to know before it becomes a liability."

    t "I can do that."

    a "Noelle -- weekly effectiveness reports. Compare projected improvements against actual. If the numbers don't hold, we revisit."

    n "Understood."

    "He doesn't address Lyra. The silence where her assignment should be is its own statement."

    athought "I do not know what to give her."

    athought "She does not need a task. She needs something I am not certain I can provide."

    # --- NYRA'S MOMENT ---

    "Nyra inclines her head."

    ny "Thank you, Commander."

    "She turns to the room. Her gaze moves across each face. Not aggressive. Not warm. The calm of someone who has already decided."

    ny "The rebellion needs structure. I provide it. Your discomfort is noted but irrelevant."

    "The sentence lands like a blade being set on a table. Not a threat. A fact."

    ny "I am not here to be liked. I am here to ensure that when Echelon comes -- and they will come -- no one in this room dies because of a forty-minute gap in patrol coverage."

    ny "If that makes me the enemy, I can live with that. As long as you live."

    "She gathers her datapad. Walks to the door. Her footsteps are precise, metronomic."

    "At the threshold, she pauses."

    ny "The first drill rotation begins at 1400. I suggest attendance."

    "The door hisses shut behind her."

    # --- AFTERMATH ---

    "The room exhales. The tension changes shape but does not leave."

    z "She just told us our discomfort is irrelevant."

    t "She also just told us she wants to keep us alive."

    z "Those aren't mutually exclusive. Echelon says the same thing to every sector they pacify."

    "Zira pushes back from the table."

    z "I'll run her node changes through my filters. If she has planted anything in the Ghostline, I will find it."

    "She leaves. The door hasn't fully closed before her boots are echoing down the corridor."

    "Tessa stands more slowly."

    t "I'll start the morale assessments. Aeron... be careful."

    a "With what?"

    t "With how much you're willing to change for the sake of efficiency."

    "She leaves."

    "Noelle closes her tablet."

    n "The math is clean. The implementation will tell us if the operator is."

    "She leaves."

    # --- LYRA ---

    "Lyra hasn't moved."

    "The war room is empty except for the two of them. The tactical displays cycle through Nyra's patrol grids. New designations. New structure. New order."

    l "You didn't give me an assignment."

    a "No."

    l "Why?"

    athought "Because I do not know what you need."

    athought "Because I do not know what I need from you."

    athought "Because the honest answer is that you are the part of this I cannot organize into a patrol grid."

    a "Because not everything requires one."

    "She stands. Her movements are careful, deliberate -- the way people move when they are trying not to show that something hurts."

    l "You're different."

    a "We're all different. Selene died."

    l "That's not what I mean."

    "She looks at the display wall. Nyra's work. The architecture of control rendered in blue light."

    l "You're becoming something. I can't tell if it's what you want or what she wants."

    athought "She."

    athought "Nyra."

    athought "Lyra sees it. The pull. The ease of having someone who validates the hardest parts of what I am."

    athought "I should reassure her."

    athought "I do not."

    a "The schedule works, Lyra. The coverage gaps are closed. The supply chains are tighter. People will be safer."

    l "I know."

    "She walks toward the door."

    l "I just wonder who you'll be when the schedule doesn't need you anymore."

    "The door closes."

    "Aeron stands alone in the war room. Nyra's patrol grids pulse on the displays. Blue light. Clean lines. Perfect coverage."

    athought "The rebellion needs structure. She provides it."

    athought "My discomfort is noted but irrelevant."

    athought "Except I am not uncomfortable."

    athought "That is what Lyra sees."

    athought "That is what frightens her."

    # --- END ---

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "completed")
    $ canon_set("nyra_integrated")
    $ rel_bump("Nyra", trust=1)
    $ flag("lyra_silent_break", True)
    $ npc_remember("Nyra", "terms_of_order", tone="imposed_structure")
    $ npc_remember("Zira", "terms_of_order", tone="hostile_opposition")
    $ npc_remember("Tessa", "terms_of_order", tone="concerned_caution")
    $ npc_remember("Noelle", "terms_of_order", tone="data_supportive")
    $ npc_remember("Lyra", "terms_of_order", tone="silent_breaking")

    call li_lore_check("Nyra") from _a3_s07_lore

    return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s07_terms_of_order_ob
# cann.chapter: Act III, Phase I -- Consolidation
# cann.chapter_start: False
# cann.when_in_timeline: Morning after Nyra's provisional acceptance. ~16 hours post-alignment.
# cann.what_happened:
#   - Nyra reorganized the command hierarchy overnight (0200-0600).
#   - New patrol grids, supply consolidation, communication rerouting.
#   - Team fractures: Zira hostile ("infiltrate, not defect"), Tessa concerned
#     ("discipline isn't healing"), Noelle supportive (math), Lyra silent.
#   - Aeron sides with the restructuring. Gives each team member a role --
#     except Lyra, whose omission is the scene's emotional wound.
#   - Nyra addresses the room: "Your discomfort is noted but irrelevant."
#   - Lyra confronts Aeron privately: "You're becoming something."
#   - The rebellion's character changes. More efficient. Less warm.
# cann.aeron_state:
#   - OB consolidation. Fewer contractions. Clinical. Sides with efficiency.
#   - He recognizes Lyra's pain but does not address it.
#   - "I am not uncomfortable. That is what frightens her."
# cann.path_tracking:
#   - canon_set("nyra_integrated"), rel_bump("Nyra", trust=1)
#   - flag("lyra_silent_break") -- Lyra's fracture point.
#   - npc_remember for all five characters.
# cann.thematic_flags:
#   - "Your discomfort is noted but irrelevant." -- Nyra's thesis statement.
#   - Nyra occupying Selene's briefing position -- territorial, not accidental.
#   - Zira: "This isn't integration. This is occupation."
#   - Tessa: "Discipline isn't healing."
#   - Lyra: "You're becoming something. I can't tell if it's what you want or what she wants."
#   - The rebellion's warmth replaced by architecture. Blue light. Clean lines.
# cann.character_moments:
#   - Nyra: Calm authority. "I am not here to be liked." Addresses the room as fait accompli.
#   - Zira: Hostile. "People like that don't defect -- they infiltrate." Retained Ghostline independence.
#   - Tessa: "Discipline isn't healing." Sees the human cost. Asked to assess morale.
#   - Noelle: "Forty-three percent." Data-forward. "The math is clean."
#   - Lyra: Silent through the meeting. "You're becoming something." The scene's emotional core.
# cann.block_status:
#   - ANCHOR (always plays on OB path). No choices -- the decision IS the scene.
# cann.requires_followup:
#   - "Perfect Execution" -- first joint operation with Nyra. The efficiency is the horror.
#   - "Tessa Friction" -- Tessa confronts Aeron directly about his direction.
#   - Zira Ghostline investigation arc -- she's looking for proof.
#   - Lyra's "silent break" thread -- escalates through Phase I.
