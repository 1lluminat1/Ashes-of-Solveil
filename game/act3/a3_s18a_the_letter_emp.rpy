# =======================================================
# ACT 3 - Scene 18a: The Letter (Empathy Path)
# File: a3_s18a_the_letter_emp.rpy
# Type: LIORA'S LETTER (both paths, EMP version)
# CRITICAL: Must fire BEFORE the Liora revelation (s20) and BEFORE the finale (s22).
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s18a_the_letter_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s18a_the_letter_emp:

    $ show_timeline("DAY 36", "02:00", "Phoenix Base — Mapping Station")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Clinical opening — the dead drop location. Then close on hands.
    #         Zira's hands opening the case. Aeron's hands receiving the letter.
    #         During the letter: the camera holds on the paper. No faces. The handwriting
    #         fills the frame. The player reads WITH Aeron — no mediation.
    #         After: single close-up on Aeron. Then Zira. Then the letter on the table.
    # LIGHTING: Opening: Ghostline mapping station — blue-green terminal glow, amber practical.
    #           The dead drop reveal: amber only. Warm. The case is old.
    #           The letter: lit from above. Clean. The handwriting needs to be readable.
    #           After: the light doesn't change. The room does.
    # SFX: Loop — base ambient: quiet, intimate. The hum of Zira's mapping equipment.
    #      One-shots — case latch (old, mechanical), paper unfolding (careful), Aeron's breath.
    #      ABSENCE: No music during the letter. Silence and the ambient loop. That's all.
    # FX/COMP: The dead drop case: pre-Purge era. Metal. A courier mark stamped into the lid —
    #          older than the Ghostline, older than Zira's network. Pre-existing infrastructure
    #          that Zira built on top of without knowing its origin.
    #          The letter: handwritten. Folded twice. The paper has aged but the ink held.
    # BLOCKING: Zira's mapping station — her workspace in the base. Terminals, relay maps,
    #           the organized chaos of someone who thinks in networks.
    #           Zira presents the case. Aeron opens it. Reads standing.
    #           After: he sits. The sitting is the reaction.
    # CANON: MAJOR PLOT SCENE. Liora's letter to Marcus, never sent. Found via Ghostline mapping.
    #        Establishes Liora as alive (pre-reveal), her relationship with Marcus, and the
    #        thematic spine of the letter: compassion as strength, the pause before signing.
    #        The letter is EXACT TEXT — do not modify.
    #        Must fire before a3_s20 (Story Keeper) and a3_s22 (Execution).
    # FACE: Aeron — reading. The face of someone meeting a ghost. Not grief — recognition.
    #        Zira — watching him read. Knowing this matters. Not knowing how much.

    # ========= VOICE BASELINE =========
    # EMP cadence: Full warmth. This scene earns every ounce of it.
    # Zira: Sharp, professional for the intel delivery. Then quiet. She knows when to stop talking.
    # Aeron: Internal. The athought carries the weight. Almost no spoken dialogue.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ZIRA'S MAPPING STATION - NIGHT]

    #scene bg_zira_station_night_emp with dissolve
    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE DEAD DROP ==========

    "Zira's mapping station is the most alive room in the base at 0200. Terminals glow with Ghostline relay maps. Courier routes thread across the display like veins in a body she's still learning the anatomy of."

    "She's waiting for him. She called him here."

    z "Sit down."

    a "You never ask me to sit down."

    z "I know. Sit down."

    "He doesn't. She doesn't push it."

    z "I've been mapping courier routes from the pre-Purge era. The ones my network was built on top of. Most of them are dead — infrastructure that collapsed or was deliberately severed."

    z "But the mapping turned up something. A dead drop in Sector 4. Old. The courier mark on the cache predates my network."

    "She sets a case on the table between them. Metal. Small. The kind of thing that fits in a wall cavity or under a floor panel. The courier mark on the lid is stamped, not etched — a methodology from before standardization."

    z "This is older than my network. Older than the Purge."

    a "How old?"

    z "The courier mark is a first-generation stamp. Pre-Ghostline. Someone was running drops through that sector before I was born."

    "She opens the case. Inside: a sealed inner sleeve. Paper."

    z "I didn't read it."

    a "Why not?"

    z "Because the courier mark addresses it to Echelon Command. And the handwriting on the inner sleeve says 'Marcus.'"

    "The room narrows."

    athought "Marcus."

    athought "My father's name in a dead drop that predates the Ghostline."

    z "It's addressed to your father by someone who knew him well enough to use his first name. That's not my read. That's yours."

    "She steps back. Gives him the space."

    # ========== PHASE 2 — THE LETTER ==========

    "He opens the inner sleeve. The paper is yellowed but intact. The handwriting is small, even, unhurried. The hand of someone who learned to write before terminals replaced pens."

    athought "I don't recognize the handwriting."

    athought "But something in the shape of the letters — the way the 'a' curls, the way the 't' crosses high — feels like looking in a mirror I didn't know existed."

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

    # ========== PHASE 3 — AFTER ==========

    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    "He sits down."

    "Not because Zira told him to. Because his legs decided for him."

    athought "Liora."

    athought "My mother's name."

    athought "I haven't said it — haven't thought it — in years. It was filed in the same place I filed everything that hurt too much to hold: the locked room behind the Glass, the place where the suppressants couldn't reach because they didn't need to. I sealed it myself."

    athought "She saw him. She saw all of it. And she loved the pause."

    athought "The pause."

    athought "That half-second where his pen stopped."

    athought "I remember that. Sitting at his desk, watching him sign documents. The pen would hover. Just for a moment. Like his hand remembered something his mind had already decided to forget."

    athought "She loved that. She loved the part of him that hesitated."

    athought "And she left because the hesitation stopped."

    "The letter sits on the table. The paper is still. The ink is dry. It's been dry for years."

    "Zira is quiet. She's moved to the far side of the station. Not leaving — present, but distant. The geography of someone who knows grief needs room."

    z "..."

    "She doesn't ask."

    a "My mother."

    "Two words. The sentence doesn't need more."

    z "I thought it might be."

    a "You didn't read it."

    z "I didn't need to. The courier mark, the date range, the addressing convention — there's only one person from that era who would have been close enough to Marcus Rylan to use his first name and a personal dead drop."

    z "I'm sorry."

    a "Don't be. She was right."

    athought "She was right about all of it."

    athought "The city doesn't need a harder man."

    athought "She wrote that before the Purge. Before Kael. Before any of this."

    athought "She wrote it because she could see the trajectory. Because love made her a better analyst than fear ever made him."

    "He folds the letter. Carefully. Along the same creases."

    a "I want to keep this."

    z "It's yours. It was always yours."

    "He puts the letter inside his jacket. Close to the chest. The oldest place to keep something that matters."

    athought "I didn't know her. I thought I didn't. But the handwriting — the curling 'a,' the high 't' — that's my handwriting."

    athought "She gave me that without knowing it. The way she gave me discipline without Marcus's coldness. The way she gave me the pause."

    athought "I have the pause."

    athought "I've been using it. Every time I hesitate before a hard call. Every time I stop and feel instead of calculate."

    athought "That was her."

    "The mapping station hums. Zira's terminals glow with their network maps. The courier routes that led to this letter thread across the display."

    "He sits with it. He doesn't need to do anything else tonight."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("liora_letter_found", True)
    $ npc_remember("Zira", "found_liora_letter_dead_drop", tone="careful_reverence")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s18a_the_letter_emp
# cann.chapter: Act III, Phase III — Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.scene_order_critical: MUST fire before a3_s20 (Story Keeper) and a3_s22 (Execution).
# cann.when_in_timeline:
#   - Act III Phase III. After The Weight (s18). Before the Liora revelation.
#   - Zira's Ghostline mapping uncovers pre-Purge courier infrastructure and a dead drop.
# cann.what_happened:
#   - Zira calls Aeron to her mapping station. A dead drop from Sector 4 — pre-Ghostline era.
#   - The courier mark predates Zira's network. Addressed to "Marcus" in personal handwriting.
#   - Inside: a letter from Liora to Marcus. Never sent.
#   - The letter: Liora loved Marcus. She left because she saw what he was becoming.
#     "The city doesn't need a harder man. It needs a man brave enough to be soft."
#     "I fell in love with the pause." — the half-second where Marcus's pen stopped before signing.
#   - Aeron reads the letter. Recognizes her handwriting as the origin of his own.
#   - "She saw him. She saw all of it. And she loved the pause."
#   - Aeron keeps the letter. flag("liora_letter_found") — can be shown to LIs later.
# cann.aeron_state:
#   - Meeting a ghost. The mother he filed away in the locked room behind the Glass.
#   - The pause: he has it. He's been using it. That was her gift.
#   - "Love made her a better analyst than fear ever made him."
# cann.path_tracking:
#   - flag("liora_letter_found", True). Inventory item — showable to LIs in future scenes.
#   - npc_remember for Zira: she found the dead drop, didn't read the letter, gave him space.
#   - No player choice. No branching. The letter and the response are enough.
# cann.thematic_flags:
#   - THE PAUSE: Marcus's half-second of hesitation before signing. Liora loved it.
#     Aeron inherited it. The pause is the empathy path's origin story.
#   - "I love you. I left. Both are true." — the letter's emotional spine.
#   - Softness as danger: "brave enough to be soft when softness is the most dangerous thing."
#     Direct thematic connection to Aeron's empathy-path identity.
#   - The handwriting: Liora's curling 'a' and high 't' — Aeron writes the same way.
#     Genetic inheritance as metaphor for emotional inheritance.
#   - The courier mark: pre-Ghostline. Someone was building networks of care before Zira.
#     Liora as predecessor, though no one knew it yet.
# cann.character_moments:
#   - Zira: Didn't read the letter. Identified the writer through courier analysis alone.
#     Gave Aeron space without leaving. "It was always yours."
#   - Aeron: Sits down because his legs decide. Folds the letter along the same creases.
#     Keeps it inside his jacket. The oldest place to keep something that matters.
# cann.callbacks:
#   - Marcus: the shadow father. His pen. His orders. His hand that held his son.
#   - The Glass Academy: the suppressants that sealed the locked room where Liora's name lived.
#   - Zira's Ghostline: built on infrastructure Liora's generation created.
#   - The pause: will recur. Every hesitation Aeron makes is her inheritance.
# cann.block_status:
#   - PLOT SCENE. No branching. Exact letter text. Inventory flag set.
# cann.requires_followup:
#   - a3_s20: The Story Keeper. The courier mark from this letter matches the network pattern.
#   - a3_s22: The execution. The letter was days ago. She was alive.
#   - LI reactions to the letter: scenes where Aeron can show it.
#   - "The pause" as recurring motif through Act 3 and Act 4.
#   - flag("liora_letter_found") gates future dialogue branches.
