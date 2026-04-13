# =======================================================
# ACT 3 - Scene 21: The Story Keeper (Obedience Path)
# File: a3_s21_the_story_keeper_ob.rpy
# Type: PLOT / LIORA REVELATION (OB)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s21_the_story_keeper_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s21_the_story_keeper_ob:

    $ show_timeline("DAY 39", "10:00", "Phoenix Base — Mapping Station")

    # Codex — first Liora unlock on the OB path.
    $ codex_mention("liora_rylan", source="a3_s21_the_story_keeper_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. Clinical precision (OB grammar). Opens on Zira's terminal --
    #         network maps, courier patterns. The same visual language as EMP s20 but colder.
    #         Cross-reference beat: Zira's data and Noelle's trace. Split-screen feel.
    #         The recognition moment: push-in on Aeron. Slower than EMP. The face doesn't open.
    #         It closes further. The recognition is anger, not hope.
    # LIGHTING: Mapping station: blue-green terminal glow. Cooler than EMP version.
    #           No warm amber lamp. The cold of operational analysis.
    # SFX: Loop -- mapping station ambient. Terminal processing. Ghostline carrier hum.
    #      One-shots -- data scroll, connection tone (the match), Noelle's keyboard (fast, then stop).
    # FX/COMP: Same terminal displays as EMP. Courier routes. The pattern emerging.
    #          But on the OB display, Nyra's patrol data is visible in the background --
    #          the militarized base overlaying the courier infrastructure.
    # BLOCKING: Zira at her station. Noelle at the adjacent terminal.
    #           Aeron standing between them. Same geography as EMP.
    #           The difference: his posture. EMP Aeron grips the terminal. OB Aeron stands still.
    # CANON: MAJOR PLOT SCENE. Same mechanism as EMP -- Zira cross-refs courier marks.
    #        OB reaction is DIFFERENT: anger, abandonment, complex betrayal.
    #        "She kept the names of strangers. She didn't keep mine."
    # FACE: Aeron -- the ground opening. Not hope. Not grief. Fury. The quiet kind that turns inward.
    #        Zira -- watching. She's seen enough cracks to recognize this one.
    #        Noelle -- precise. Then unsettled. Even her data can't make this clean.

    # ========= VOICE BASELINE =========
    # OB cadence: Short sentences. Clinical surface. The anger leaks through in fragments.
    # Zira: Intel-delivery. Sharp. She's careful with this one -- she knows what it means.
    # Noelle: Data-first. The identity trace hits different when the subject is the commander's mother.
    # Aeron: Internal monologue carries fury disguised as analysis.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MAPPING STATION - EVENING]

    #scene bg_zira_station_evening_ob with dissolve
    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE PATTERN ==========

    "Zira has that look. Not the intel-hunter look. The one that means the data has outrun her ability to present it cleanly."

    z "I need you to see something."

    a "Brief me."

    z "I've been cross-referencing courier data from the Outlands relays. The ones on the edge of our network -- stations that receive but rarely transmit."

    z "There's a pattern. Someone has been moving information through the courier network for years. Not supplies. Not tactical data. Stories."

    a "What kind of stories?"

    z "Names. Ledgers. Personal histories. The kind of information Echelon scrubbed from every official database."

    z "Someone's been keeping it. Moving it through courier channels like cargo. Drop to drop, relay to relay, for years."

    athought "Names of the erased. Someone keeping count when Echelon was keeping silence."

    athought "Operationally irrelevant. Except Zira doesn't call me for operationally irrelevant data."

    z "The courier network she's using is old. Pre-Ghostline. Same infrastructure I built on top of."

    z "I ran the courier marks against the dead drop from Sector 4."

    "She looks at him."

    z "Same source."

    # ========== PHASE 2 -- THE CROSS-REFERENCE ==========

    athought "Same source. The letter."

    athought "The person who wrote to Marcus is the person moving stories through the Outlands."

    z "I asked Noelle to run the pattern against known operatives."

    "Noelle is at the adjacent terminal. Hands moving in the rapid, precise sequence that means deep data trace."

    n "The courier profile doesn't match any known operative. Single actor. One person, moving through the Outlands relay system, depositing information at intervals."

    n "The Outlands contacts call her 'the story-keeper.' A woman who keeps the names of the lost city."

    athought "The story-keeper."

    athought "Interesting alias for someone running a solo courier operation in hostile territory."

    a "Can you identify her?"

    n "Running the trace. The courier mark has a registration -- old, pre-standardization, but it links to a citizenship record."

    "Her hands stop moving."

    "Noelle's hands never stop."

    n "Registry discrepancy."

    z "What kind?"

    n "Two names. Birth name and married name. Married name added twenty-six years ago. Citizenship flagged as inactive nineteen years ago."

    n "Inactive. Not deceased. The record was never closed."

    athought "Twenty-six years. The year I was born."

    athought "Nineteen years. The year she--"

    athought "No."

    n "The married name on the record is Rylan."

    # ========== PHASE 3 -- THE EARTHQUAKE ==========

    "The room doesn't change."

    "He doesn't grip the terminal. He doesn't sit. He doesn't move."

    "That's the tell. Zira sees it. The absolute stillness of a man whose internal architecture just shifted and whose external architecture won't permit it to show."

    athought "Alive."

    athought "My mother is alive."

    athought "She left. She walked out nineteen years ago and everyone -- Marcus, the Academy, the records -- everyone said gone. Not dead. Just gone. Which was worse. Dead has clarity. Gone has questions."

    athought "She's been in the Outlands. For nineteen years. Keeping names."

    athought "Keeping the names of strangers."

    athought "She didn't keep mine."

    "The sentence arrives with the force of something true and unforgivable."

    athought "She left me with him. She saw what Marcus was becoming -- she wrote about it, in detail, in handwriting I inherited -- and she left me there."

    athought "She left and she went to the Outlands and she spent nineteen years keeping the names of people she'd never met. People who lost everything."

    athought "I lost everything. She was the one who took it."

    athought "And she kept their names instead of mine."

    z "Aeron."

    "His voice when it comes is flat. Operational."

    a "She's alive."

    z "The data is consistent. Courier mark, registry, timeline. It's her."

    n "I can confirm the match. Handwriting analysis from the letter is consistent with the registration signature. Ninety-seven percent confidence."

    a "How long has she been monitoring Phoenix?"

    n "Pattern analysis suggests awareness of our operations. Not direct monitoring. But the information flow indicates she knows something is happening."

    athought "She knows. She's been out there. She knows we exist."

    athought "She didn't come."

    athought "She knows about the rebellion. She knows about Phoenix. She might even know about me."

    athought "And she stayed in the Outlands keeping the names of strangers."

    a "Can we reach her?"

    z "Through the courier network. Slow, but possible."

    a "Do it."

    "The command is cold. Zira studies his face."

    z "Aeron. Are you--"

    a "That's an order, Zira. Establish contact through the courier network. I want a location and a timeline."

    "Zira's jaw tightens. She nods."

    z "Understood."

    "Noelle saves the data trace. Her hands are steady. She looks at Aeron with the clinical precision of someone recording a behavioral data point."

    n "For the record. The story-keeper's archive represents the most complete record of Purge-era disappearances in existence. Its intelligence value is significant."

    athought "Intelligence value."

    athought "Yes. That too."

    athought "She kept the names of six thousand people who were erased."

    athought "She just didn't keep the one that mattered."

    "He turns toward the door."

    a "Keep me updated on contact progress. Run the archive data against our operational intelligence. If there's tactical value in what she's kept, I want to know."

    "He leaves."

    "The mapping station hums behind him. Zira and Noelle sit with the data trace and the silence."

    z "He didn't--"

    n "No."

    z "That's not good."

    n "No."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("liora_alive_known", True)
    $ flag("story_keeper_identified", True)
    $ npc_remember("Zira", "identified_liora_courier_pattern_ob", tone="growing_alarm")
    $ npc_remember("Noelle", "traced_liora_registry_identity_ob", tone="clinical_concern")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s21_the_story_keeper_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After the letter (s19a) and Zira confrontation (s20).
#   - Same mechanism as EMP -- Zira cross-refs courier marks.
# cann.what_happened:
#   - Identical mechanism to EMP: Zira finds the courier pattern, Noelle traces the identity.
#   - Same data: married name Rylan, 26 years ago, inactive 19 years ago. Liora is alive.
#   - OB REACTION IS COMPLETELY DIFFERENT:
#     Not hope. Not awe. Fury. Abandonment. Betrayal.
#     "She kept the names of strangers. She didn't keep mine."
#   - He converts the revelation to operational data: intelligence value, tactical utility.
#   - Orders Zira to establish contact. Cold. Command voice.
#   - Zira and Noelle exchange after he leaves: "He didn't--" "No." "That's not good." "No."
# cann.aeron_state:
#   - Complex anger: not just "she's alive" but "she chose everyone else."
#   - She left him with Marcus. She saw what Marcus was becoming and she left her son there.
#   - She kept six thousand names. Not his.
#   - The operational mask holds. The fury is internal. That's the danger.
# cann.path_tracking:
#   - canon_set("liora_alive_known"). flag("story_keeper_identified"). Same flags as EMP.
#   - npc_remember tones different: Zira "growing_alarm", Noelle "clinical_concern".
#   - No player choice. Revelation scene. The anger is the event.
# cann.thematic_flags:
#   - "She kept the names of strangers. She didn't keep mine." -- the OB thesis on Liora.
#     EMP Aeron sees a predecessor. OB Aeron sees abandonment with altruistic cover.
#   - Intelligence value: Aeron converts the emotional revelation into operational data.
#     The same instinct Zira confronted in s20 -- filing the human into the tactical.
#   - "She chose everyone else": the child's wound beneath the commander's mask.
#     OB Aeron's relationship to abandonment fuels his need for control.
#   - Zira and Noelle's final exchange: the external witnesses to his non-reaction.
#     Parallel to Zira's "That isn't good" in the letter scene.
# cann.character_moments:
#   - Zira: Careful delivery. She knows this is a bomb. She tries to reach him after: "Are you--"
#     Gets cut off by command voice. Exchanges look with Noelle: "That's not good."
#   - Noelle: Same data delivery. "Intelligence value" -- giving him a framework for processing
#     that she knows isn't the right one but is the only one he'll accept.
#   - Aeron: Absolute stillness. The mask. Orders given in command voice.
#     Internal: fury at being abandoned. "She didn't keep mine."
# cann.callbacks:
#   - a3_s19a: The letter. "I fell in love with the pause." She loved the pause in Marcus
#     and then she left the son who inherited it.
#   - a3_s20: Zira's confrontation. She told him he was becoming hollow.
#     His reaction to the Liora revelation proves it.
#   - a3_s02a: Noelle comparing him to Marcus. The son's fury at the mother who left
#     him with the father mirrors Marcus's conversion of personal loss to institutional control.
#   - EMP s20: The contrast. Same data. Different man. "She's alive" (hope) vs "she chose everyone else" (fury).
# cann.block_status:
#   - PLOT/REVELATION SCENE. No branching. No choice.
# cann.requires_followup:
#   - a3_s24: Liora confrontation. She's alive. He's furious. She's going to look at him
#     and see Marcus. The mirror that breaks everything.
#   - The archive's intelligence value: does Aeron weaponize Liora's work?
#   - Zira and Noelle's concern: they see the non-reaction. They'll watch for the consequences.
