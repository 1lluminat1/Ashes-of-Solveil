# =======================================================
# ACT 3 - Scene 19a: The Letter (Obedience Path)
# File: a3_s19a_the_letter_ob.rpy
# Type: LIORA'S LETTER (OB version)
# CRITICAL: Must fire BEFORE the Liora revelation (s21) and BEFORE the finale (s24).
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s19a_the_letter_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s19a_the_letter_ob:

    $ show_timeline("30th of Cipher, 388 A.C.", "02:00", "Phoenix Base — Mapping Station")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. OB stillness. The dead drop case on the table. Then close on hands.
    #         Zira's hands opening the case. Aeron's hands receiving the letter.
    #         During the letter: the camera holds on the paper. No faces. The handwriting
    #         fills the frame. The player reads WITH Aeron -- no mediation.
    #         After: single close-up on Aeron. Then Zira. Then the letter on the table.
    #         DIFFERENCE from EMP: After reading, the camera doesn't follow Aeron down.
    #         He doesn't sit. He stands. The camera holds on the standing man, waiting
    #         for a reaction it doesn't get.
    # LIGHTING: Opening: Ghostline mapping station -- blue-green terminal glow, amber practical.
    #           The dead drop reveal: amber only. Warm. The case is old.
    #           The letter: lit from above. Clean. The handwriting needs to be readable.
    #           After: the light doesn't change. The room doesn't change. Aeron doesn't change.
    #           That's the horror.
    # SFX: Loop -- base ambient: quiet, operational. The hum of Zira's mapping equipment.
    #      One-shots -- case latch (old, mechanical), paper unfolding (efficient, not careful).
    #      ABSENCE: No music during the letter. Silence and the ambient loop. That's all.
    # FX/COMP: The dead drop case: identical to EMP. Metal. Small. Pre-Purge era.
    #          The courier mark on the lid -- older than the Ghostline, older than Zira's network.
    #          The letter: handwritten. Folded twice. The paper has aged but the ink held.
    # BLOCKING: Zira's mapping station. Same geography as EMP.
    #           Zira presents the case. Aeron opens it. Reads standing.
    #           After: he stays standing. He folds the letter. Puts it in his jacket.
    #           The gesture is identical to EMP. The meaning is completely different.
    # CANON: MAJOR PLOT SCENE. Liora's letter to Marcus, never sent. Found via Ghostline mapping.
    #        EXACT SAME LETTER TEXT as EMP. The OB difference is entirely in Aeron's response.
    #        Must fire before a3_s21 (Story Keeper OB) and a3_s24 (Liora confrontation).
    # FACE: Aeron -- reading. The face of someone meeting a ghost. Not grief -- assessment.
    #        Then: something behind the assessment. Quick. Sealed. The pause he can't afford.
    #        Zira -- watching him read. Waiting for the reaction she knows is coming.
    #        It doesn't come.

    # ========= VOICE BASELINE =========
    # OB cadence: Clinical surface. The cracks are beneath. Short sentences.
    # Zira: Sharp, professional for the intel delivery. Then watching. She reads him better than he reads himself.
    # Aeron: Internal monologue carries the weight. The spoken words are minimal and controlled.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ZIRA'S MAPPING STATION - NIGHT]

    #scene bg_zira_station_night_ob with dissolve
    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DEAD DROP ==========

    "Zira's mapping station at 0200. Terminals running. Ghostline relay maps cycling through courier routes like a circulatory system nobody asked her to map."

    "She called him here. She doesn't call people unless the data warrants it."

    z "Sit down."

    a "Why?"

    z "Because you're going to want to."

    a "I'll stand."

    "She doesn't argue. She learned to stop arguing with that voice months ago."

    z "I've been mapping courier routes from the pre-Purge era. The infrastructure my network was built on top of. Most of the original routes are dead."

    z "But the mapping turned up something. A dead drop in Sector 4. Old. The courier mark on the cache predates my network."

    "She sets a case on the table between them. Metal. Small. The kind of thing that fits in a wall cavity or under a floor panel. The courier mark on the lid is stamped, not etched -- a methodology from before standardization."

    z "This is older than my network. Older than the Purge."

    a "Origin?"

    z "First-generation courier stamp. Pre-Ghostline. Someone was running drops through that sector before I was born."

    "She opens the case. Inside: a sealed inner sleeve. Paper."

    z "I didn't read it."

    a "Smart."

    "The word lands wrong. She was expecting 'Why not.' She got operational approval."

    z "The courier mark addresses it to Echelon Command. The handwriting on the inner sleeve says 'Marcus.'"

    athought "Marcus."

    athought "My father's name in a dead drop that predates the Ghostline."

    athought "Filed. Continue."

    z "It's addressed to your father by someone who knew him well enough to use his first name. That's not my read. That's yours."

    "She steps back. Gives him the space."

    # ========== PHASE 2 -- THE LETTER ==========

    "He opens the inner sleeve. The paper is yellowed but intact. The handwriting is small, even, unhurried. The hand of someone who learned to write before terminals replaced pens."

    athought "I don't recognize the handwriting."

    athought "Irrelevant. Read."

    #stop ambient fadeout 1.0

    "He reads."

    # --- THE LETTER (EXACT TEXT) ---

    "{i}Marcus,{/i}"

    "{i}You were right that the world is dangerous. You were always right about that.{/i}"

    "{i}You were wrong that danger justifies becoming the thing people need protection from.{/i}"

    "{i}I watched you sign orders with the same hand that held our son. I watched you call children \"collateral\" while yours slept in the next room. I watched you become the catastrophe you spent your life preventing.{/i}"

    "{i}I didn't leave because I stopped loving you. I left because I loved you enough to see what you were becoming, and I couldn't watch you finish.{/i}"

    "{i}Aeron has your discipline. I hope he also has whatever it was in you that used to hesitate before signing. That pause — that half-second where your pen stopped — that was the best part of you. I fell in love with the pause.{/i}"

    "{i}I don't know if he'll ever read this. I don't know if you will either. But someone should say it plainly, and you taught me that someone is usually no one unless you volunteer.{/i}"

    "{i}The city doesn't need a harder man. It needs a man brave enough to be soft when softness is the most dangerous thing you can be.{/i}"

    "{i}I love you. I left. Both are true.{/i}"

    "{i}— Liora{/i}"

    # ========== PHASE 3 -- AFTER ==========

    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    "He doesn't sit down."

    "Zira watches his face. Looking for the crack. The flinch. The human response she knows is somewhere behind the operational mask."

    "She doesn't find it."

    athought "Liora."

    athought "My mother."

    athought "She wrote to him. She saw what he was becoming and she wrote it down and she left. She called it love. She called leaving love."

    athought "The pause."

    athought "'That half-second where your pen stopped -- that was the best part of you. I fell in love with the pause.'"

    athought "The pause is what gets people killed. Father learned that."

    athought "..."

    athought "But she wasn't wrong about everything."

    "The sentence arrives unbidden. He files it. Doesn't examine it. There will be time for examination later."

    "There won't be."

    athought "'The city doesn't need a harder man.'"

    athought "The city needs whatever keeps it standing. She wouldn't know. She left."

    athought "She left a letter in a dead drop that no one found for nineteen years. She wrote the word 'love' like it was operational intelligence. She described my father's pen stopping."

    athought "His pen did stop. I remember. Watching him sign documents at his desk. The hover."

    athought "I trained that out of myself at the Glass. The instructors called it 'decision latency.' They called it a flaw."

    athought "She called it the best part of him."

    "He folds the letter. Not carefully -- efficiently. Along the same creases. The motion is clean."

    z "..."

    "Zira is at the far side of the station. Watching. Waiting for the words he's supposed to say."

    z "Do you want to--"

    a "My mother."

    "Two words. She stops."

    z "I thought it might be."

    a "You didn't read it."

    z "I didn't need to. The courier mark, the date range, the addressing convention. Only one person from that era would have used Marcus Rylan's first name in a personal dead drop."

    "She pauses. Zira doesn't do sympathy. She does precision."

    z "I'm sorry."

    a "For what?"

    "The question isn't hostile. It's genuine. He doesn't know what she's sorry for."

    "For the letter existing. For the mother who left. For the fact that he's standing here reading about pauses when pauses are the thing he burned out of himself to survive."

    "Zira opens her mouth. Closes it. Nods."

    "He puts the letter inside his jacket. Close to the chest. The same place. The same gesture."

    athought "She said the city doesn't need a harder man."

    athought "She was wrong. The city doesn't need anything. The city is a system. Systems need control."

    athought "But the handwriting."

    athought "The way the 'a' curls. The way the 't' crosses high."

    athought "That's my handwriting."

    athought "I don't know what to do with that."

    "He turns. Walks toward the door."

    a "Good work finding this. Log the dead drop location. Cross-reference the courier mark against active Ghostline patterns."

    "He gives her an assignment. Because assignments are clean. Assignments don't ask about pauses."

    z "Already started."

    "The door hisses. He leaves."

    "Zira watches the door close. She looks at the empty case on the table."

    "She lets out a breath she's been holding since he started reading."

    z "(to herself) That isn't good."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("liora_letter_found", True)
    $ npc_remember("Zira", "found_liora_letter_dead_drop", tone="growing_concern")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s19a_the_letter_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.scene_order_critical: MUST fire before a3_s21 (Story Keeper OB) and a3_s24 (Liora confrontation).
# cann.when_in_timeline:
#   - Act III Phase III. After OB operations arc. Before the Liora revelation.
#   - Same dead drop, same letter. OB Aeron's response is the difference.
# cann.what_happened:
#   - Identical setup to EMP: Zira calls Aeron to her mapping station. Dead drop from Sector 4.
#   - Same letter. Exact same text. Liora to Marcus. "I fell in love with the pause."
#   - OB DIFFERENCE: Aeron doesn't sit. Doesn't crack. Reads standing.
#     "The pause is what gets people killed. Father learned that."
#     Then quieter: "But she wasn't wrong about everything." -- filed, not examined.
#   - He folds the letter efficiently, not carefully. Same jacket. Same gesture. Different meaning.
#   - Gives Zira an operational assignment to avoid processing what he read.
#   - Zira's final line (to herself): "That isn't good." She sees what he can't.
# cann.aeron_state:
#   - The letter challenges the OB thesis: that the pause is weakness, that softness is danger.
#   - He rejects it. Almost. "She wasn't wrong about everything" slips through.
#   - The handwriting recognition still hits. Same as EMP. Genetic inheritance of the 'a' and 't'.
#   - But he files it. Seals it. Converts personal revelation into operational data.
# cann.path_tracking:
#   - flag("liora_letter_found", True). Same flag as EMP -- the letter exists in both paths.
#   - npc_remember for Zira: tone is "growing_concern" (vs EMP's "careful_reverence").
#   - No player choice. No branching. The non-reaction IS the scene.
# cann.thematic_flags:
#   - THE PAUSE (OB INVERSION): EMP Aeron inherits the pause and recognizes it as strength.
#     OB Aeron trained the pause out of himself. "Decision latency." A flaw, not a feature.
#     The letter says "I fell in love with the pause" and OB Aeron can't integrate it.
#   - "She was wrong." / "She wasn't wrong about everything." -- the crack beneath the surface.
#   - The handwriting: the same recognition, the same genetic inheritance. He can reject the
#     thesis but he can't reject the biology. That's the thing he doesn't know what to do with.
#   - Zira's "That isn't good": the external witness to Aeron's failure to process.
#     She expected a human response. She got command protocol. That's the warning sign.
# cann.character_moments:
#   - Zira: Same delivery. Same professionalism. But she's watching for the crack.
#     Her "I'm sorry" is genuine. His "For what?" breaks something in the exchange.
#     Final line: "That isn't good." She sees the trajectory.
#   - Aeron: Standing. Efficient. The letter converted to operational data in real time.
#     But the handwriting. But the pause. The things he can't file.
# cann.callbacks:
#   - Marcus: the pen. The hover. The decision latency. OB Aeron was trained to eliminate it.
#   - The Glass Academy: where hesitation became a flaw. Where they burned the pause out.
#   - Nyra: "Precision is mercy." The OB thesis that the letter contradicts.
#   - Zira's Ghostline: same infrastructure inheritance as EMP.
#   - The pause: will recur. In the confrontation with Liora. In the mirror moment.
# cann.block_status:
#   - PLOT SCENE. No branching. Exact letter text. Inventory flag set.
# cann.requires_followup:
#   - a3_s21: The Story Keeper (OB). The courier mark from this letter matches the network pattern.
#   - a3_s24: The confrontation. The letter is in his jacket when she looks at him.
#   - "But she wasn't wrong about everything" -- the sentence he filed. It's still in there.
#   - Zira's "That isn't good" -- she'll act on this concern.
