# =======================================================
# ACT 3 - Scene 22: The Hunt (Obedience Path)
# File: a3_s22_the_hunt_ob.rpy
# Type: OPERATION / OB MAGNUM OPUS
# Character Focus: Aeron (commander), Noelle, Zira, Nyra
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s22_the_hunt_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s22_the_hunt_ob:

    $ show_timeline("33rd of Cipher, 388 A.C.", "02:00", "Multiple Sectors — Operation")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked (OB precision). War room command view.
    #         Opens on the tactical display: the city in blue light. Echelon patrols mapped.
    #         Phoenix feints marked in amber. The chessboard visible.
    #         During the operation: cross-cutting between war room (Aeron, Noelle) and
    #         field (Zira's Ghostline, Nyra's soldiers). Tight editing. Clean transitions.
    #         The operation sequences use the visual grammar of a heist film --
    #         plans overlaid on execution, predicted vs actual.
    #         Close-ups: Aeron's hands moving markers. Noelle's data. Nyra's precise nod.
    #         Zira: silent. The camera finds her silence in the room.
    #         Post-operation: 40mm, handheld drift (2%). The drift enters after the operation
    #         succeeds. Something loose in the frame. Something wrong with the victory.
    # LIGHTING: War room: blue-green tactical displays. Cold. The light of command.
    #           Field sequences: exterior night. Sodium amber streetlight. Moving shadows.
    #           Post-op: the same war room. Same light. But the shadows are longer.
    # SFX: Loop -- war room ops: tactical hum, comms chatter (controlled, precise).
    #      Field: urban night ambient. Bootfall. Echelon patrol audio (distant, then confused).
    #      One-shots -- marker placement on tactical display, comms click, distant detonation
    #      (feint charge), the supply depot breach (clean, quick).
    #      Post-op: silence. The absence of comms chatter. The base breathing.
    # FX/COMP: Tactical displays showing the full operation in real time.
    #          Echelon patrol routes: predicted and actual. The predictions are perfect.
    #          Feint markers: seven false positions. Echelon chasing all of them.
    #          The supply depot: the real target. A single icon moving toward it while
    #          Echelon's attention is scattered across seven phantoms.
    # BLOCKING: War room: Aeron at the command table. Standing. Noelle at her terminal.
    #           Nyra at the comms station -- her soldiers in the field. Zira at the Ghostline
    #           terminal -- running the information war. The geography of coordinated command.
    #           Post-op: the same positions. But the room feels different. Aeron alone at the table.
    # CANON: MAJOR OPERATION SCENE. Echelon's largest deployment hunting Phoenix.
    #        Aeron orchestrates a masterpiece of misdirection. Tactically flawless.
    #        Also the clearest evidence that he's becoming Marcus: the human cost of the feints
    #        (civilians displaced, some caught in crossfire) doesn't register.
    # FACE: Aeron -- in command. The face of someone whose machine is running perfectly.
    #        Nyra -- reverence. This is the commander she was built to follow.
    #        Zira -- present. Professional. Silent when she should be celebrating.
    #        Noelle -- the data is beautiful. The implications are not.

    # ========= VOICE BASELINE =========
    # OB cadence at peak: Clipped. Precise. No wasted syllables.
    # Comms chatter: military shorthand. Professional.
    # Nyra: efficient, admiring. "Precision is mercy."
    # Zira: reports. No editorial. Her silence is the editorial.
    # Noelle: data streams. Clean. One moment of hesitation at the civilian casualty figures.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - NIGHT]

    #scene bg_war_room_ob_tactical with dissolve
    #play ambient "sfx/ambient/war_room_ops.ogg" fadein 2.0

    # ========== PHASE 1 -- THE BOARD ==========

    "Echelon has committed everything."

    "The tactical display shows their deployment: three full battalions sweeping the Unders in a grid pattern. Coordinated. Systematic. The largest search operation in the city's post-Purge history."

    "They're hunting Phoenix."

    athought "Twelve hundred personnel. Heavy armor. Aerial surveillance. The full weight of the machine brought to bear on six city blocks."

    athought "They think we're in those blocks."

    athought "We're not."

    "Noelle's displays cycle probability cascades. Patrol routes. Response times. The mathematics of attention."

    n "Echelon deployment is consistent with the predicted pattern. Grid sweep, southwest to northeast, twelve-minute rotations per block. They're following Major Harlan's doctrine."

    a "Harlan's predictable."

    n "Everyone's predictable with enough data."

    "Nyra stands at the comms station. Her people are already in position -- seven teams across six sectors. Not hiding. Waiting."

    ny "All units confirm ready. Standing by for the signal."

    "Zira is at the Ghostline terminal. She's feeding false intelligence into Echelon's intercepted channels. Ghost positions. Phantom signals. The electronic equivalent of shouting 'over here' in seven directions at once."

    z "False feeds active on all seven channels. Echelon intercept is taking the bait."

    a "Timeline."

    n "Echelon commits to the ghost positions within eighteen minutes of receiving each feed. Redeployment time per position: twenty-two minutes. Full cycle through all seven phantoms: two hours, thirty-four minutes."

    n "That gives the strike team a window of one hour, forty-seven minutes at the supply depot. More than sufficient."

    athought "One hour forty-seven minutes. To breach an Echelon supply depot, extract three months of ordnance and provisions, and exit before the grid sweep corrects."

    athought "The plan is clean. Every variable accounted for. Every contingency mapped."

    a "Execute."

    # ========== PHASE 2 -- THE OPERATION ==========

    "The board comes alive."

    "Seven phantom positions light up across the tactical display. Echelon patrols pivot toward each one -- the grid pattern fracturing as units are redeployed to chase ghosts."

    #play sound "sfx/tactical/comms_chatter_controlled.ogg"

    ny "Team One engaging phantom position Alpha. Echelon patrol redirecting. Sector clear."

    ny "Team Three at phantom Gamma. Detonation charges placed. Echelon is responding to the sound signature."

    athought "The feints are landing. Every one of them."

    athought "Noelle modeled Echelon's response doctrine. Zira planted the false intelligence. Nyra's teams are drawing them like moths to fire."

    athought "And the real target -- Echelon's forward supply depot in Sector 11 -- sits unguarded."

    n "Echelon redeployment at sixty-three percent. Grid sweep in target sector is collapsing. Supply depot security reduced to skeleton crew."

    z "Ghostline confirms: depot perimeter surveillance rerouted to phantom positions. They pulled their own cameras."

    "The strike team moves. Nyra's best. Four soldiers who operate like a single organism."

    ny "Strike team at depot perimeter. Breach in thirty seconds."

    athought "Thirty seconds."

    athought "This is what control looks like. Not force. Not violence. The precise application of information to make the enemy defeat themselves."

    athought "They're chasing ghosts while we take their supplies."

    "The comms click. The breach tone."

    ny "Depot breached. Skeleton crew neutralized. Non-lethal. Beginning extraction."

    a "Timeline."

    n "One hour thirty-nine minutes remaining. The strike team is ahead of schedule."

    "The tactical display shows the masterpiece in motion. Seven phantom positions pulling twelve hundred Echelon personnel across six sectors while four Phoenix soldiers empty their forward supply depot."

    athought "This is what I was built for."

    athought "Nyra sees it. I can feel her looking at me the way Zira looks at the Ghostline when it's running clean -- with recognition. With reverence."

    athought "This is command."

    # ========== PHASE 3 -- THE COST ==========

    "The operation runs. Clean. Precise. The supply depot empties."

    "Noelle's display flickers. A new data stream."

    n "Civilian displacement in phantom sectors."

    "Her voice doesn't change pitch. But the words arrive a fraction slower."

    n "Echelon's response to phantom positions has triggered shelter-in-place protocols in Sectors 4, 7, and 9. Civilian population affected: approximately fourteen hundred."

    n "Additionally, the detonation charges at phantom Gamma caused structural damage to a residential block. Preliminary casualty assessment: three to seven civilians."

    athought "Three to seven."

    athought "The detonation charges were non-lethal. But non-lethal next to a residential wall becomes lethal at the wrong distance."

    ny "Acceptable parameters. The operation continues."

    "Nyra says it without hesitation. Without looking up from the comms station."

    ny "Precision is mercy. We saved hundreds by displacing fourteen hundred. The math is favorable."

    athought "The math is favorable."

    athought "Noelle."

    "He doesn't ask. He doesn't need to. Noelle's stylus has stopped moving."

    n "Casualty projection updated. Three to seven, plus an additional two to four from the displacement operations in Sector 9. Total projected civilian casualties: five to eleven."

    n "Against an estimated Phoenix gain of three months' operational supplies and a significant degradation of Echelon forward logistics."

    "She pauses."

    n "The ratio is... statistically favorable."

    "Zira is silent."

    "She's been silent since the civilian displacement data appeared. Her hands are still on the Ghostline terminal. Still working. Still feeding false intelligence."

    "But she hasn't said a word."

    athought "Zira is quiet."

    athought "I note it. I don't address it."

    a "Continue the operation. Extraction timeline."

    ny "Strike team at seventy-eight percent extraction. Nineteen minutes remaining."

    a "Maintain phantom positions until extraction is complete. Pull all teams on my signal."

    ny "Understood, Commander."

    "The operation continues. Clean. Precise. The supply depot empties."

    "Three to seven people die in a building that stood next to a phantom nobody was supposed to be chasing."

    "The math is favorable."

    # ========== PHASE 4 -- THE VICTORY ==========

    "The strike team clears the depot. Full extraction. Three months of Echelon supplies in Phoenix hands."

    "Nyra's phantom teams withdraw. Silent. Disciplined. Not a single soldier lost."

    "The tactical display returns to baseline. Echelon's grid sweep resumes, twenty minutes behind schedule, minus a supply depot. By the time they realize what happened, Phoenix's soldiers will be back at base."

    a "All units, mission complete. Return to base."

    ny "Confirmed. All teams returning. Zero friendly casualties."

    "She turns to Aeron. The reverence is naked on her face."

    ny "Flawless, Commander."

    athought "Flawless."

    athought "Twelve hundred Echelon personnel chased seven ghosts across six sectors while four soldiers emptied their supply depot."

    athought "Not a single Phoenix casualty. Three months of supplies secured. Echelon's forward logistics crippled."

    athought "Five to eleven civilians who were not part of the operation and did not choose to be."

    athought "Flawless."

    n "Compiling after-action report. The operational model performed within predicted parameters on all metrics."

    "She closes her display. Her stylus is in her hand. She hasn't written anything for four minutes."

    "Four minutes is an eternity in Noelle time."

    z "The Ghostline false feeds are purged. No trace."

    "Her first words in thirty minutes. Voice level. Flat."

    a "Good work. All of you."

    "The room receives the praise. Nyra stands taller. Noelle nods. Zira doesn't react."

    "He notices."

    "He doesn't ask."

    # ========== PHASE 5 -- AFTER ==========

    "The war room empties. Nyra leaves to debrief her teams. Noelle to compile data. Zira last."

    "She pauses at the door."

    z "Five to eleven."

    a "I heard."

    z "Did you?"

    "She leaves."

    "The door closes. The war room is quiet. The tactical display shows the city in blue light. The grid sweep resuming. Normal operations."

    athought "Five to eleven."

    athought "Barely a rounding error. Father's phrase. Dinner table, I was twelve, the Purge displacement was 'within acceptable parameters.'"

    athought "Nyra said the same thing thirty minutes ago. Different words. Same math."

    athought "The operation was flawless and five to eleven people are dead because of a detonation charge I ordered placed next to a wall I didn't check."

    athought "I didn't check because the math didn't require it."

    athought "The math is favorable."

    "The tactical display hums. The city in blue light. The numbers clean. The operation complete."

    "He stands at the command table. Alone. The light doesn't change."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("the_hunt_success", True)
    $ flag("civilian_casualties_ob_hunt", True)
    $ rel_bump("Nyra", trust=1, respect=1)
    $ rel_bump("Zira", trust=-1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s22_the_hunt_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After the Story Keeper revelation (s21).
#   - Echelon's largest deployment. Phoenix's counter-operation.
# cann.what_happened:
#   - Echelon deploys 1200 personnel in a grid sweep hunting Phoenix.
#   - Aeron orchestrates a masterpiece: Noelle's models + Zira's Ghostline false feeds +
#     Nyra's soldiers running seven phantom positions. Echelon chases ghosts.
#   - While 1200 Echelon personnel are scattered, a 4-person strike team empties
#     their forward supply depot. Zero friendly casualties. Three months of supplies secured.
#   - The human cost: civilian displacement (1400), structural damage from detonation charges
#     at a phantom position, 5-11 civilian casualties.
#   - Nyra: "Acceptable parameters. Precision is mercy."
#   - Zira: silent for 30 minutes. Final words: "Five to eleven." "Did you [hear]?"
#   - Noelle: stylus stops for 4 minutes. "Statistically favorable."
#   - Aeron alone: recognizes the parallel to Marcus at the dinner table. "Acceptable parameters."
# cann.aeron_state:
#   - Peak command. The operation is his masterwork. Tactically flawless.
#   - But: "This is what control looks like." The Marcus parallel is explicit.
#   - The civilian casualties don't register during the operation. They register after.
#   - "I should have checked." But the math didn't require it. The math is favorable.
# cann.path_tracking:
#   - canon_set("the_hunt_success"). flag("civilian_casualties_ob_hunt").
#   - rel_bump Nyra trust+1 respect+1. rel_bump Zira trust-1.
#   - No player choice. The operation IS the scene. The brilliance and the cost are inseparable.
# cann.thematic_flags:
#   - THE MATH IS FAVORABLE: Echelon's language in Aeron's mouth. The same calculus Marcus
#     used to justify the Purge applied to a supply raid.
#   - "Precision is mercy": Nyra's thesis. The operation proves it and disproves it simultaneously.
#   - "Acceptable parameters": Marcus's dinner-table phrase. Aeron recognizes the echo.
#   - Zira's silence: 30 minutes. The longest silence in the project. The editorial is the absence.
#   - Five to eleven: a small number. Against gains, "barely a rounding error."
#     Marcus said the same about the Purge. The scale is different. The logic is identical.
#   - Noelle's stylus: 4 minutes of stillness. An eternity. The data is beautiful.
#     The implications are not.
# cann.character_moments:
#   - Nyra: Reverence. "Flawless, Commander." This is the man she chose. The operation validates her.
#   - Zira: Silent witness. "Five to eleven." "Did you?" Two sentences. The entire critique.
#   - Noelle: "Statistically favorable." The pause before saying it. The stylus stopping.
#   - Aeron: At the command table. Alone. Recognizing Marcus. Not changing.
# cann.callbacks:
#   - Marcus at the dinner table: "Acceptable parameters." The son inherits the calculus.
#   - a3_s20: Zira's confrontation. "Hard vs hollow." This operation is the hollow in action.
#   - a3_s06: Nyra's offer. "Precision is mercy." The thesis tested and proven -- at a cost.
#   - a3_s19a: "The pause is what gets people killed." The operation has no pause. That's the point.
#   - The Glass Academy: "Decision latency" trained out. No latency in the operation. No hesitation.
# cann.block_status:
#   - ANCHOR (always plays). No branching. Operation scene.
# cann.requires_followup:
#   - The supply gain changes Phoenix's operational capacity.
#   - Zira's distance deepens. She stayed but the silence grows.
#   - Nyra's reverence deepens. She found her commander.
#   - The civilian casualties: do they come back? News? Consequences?
#   - The Marcus parallel: explicit now. Aeron recognized it. Will he act on recognition?
