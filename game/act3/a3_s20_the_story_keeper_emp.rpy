# =======================================================
# ACT 3 - Scene 20: The Story Keeper (Empathy Path)
# File: a3_s20_the_story_keeper_emp.rpy
# Type: PLOT / LIORA FORESHADOWING
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s20_the_story_keeper_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s20_the_story_keeper_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, handheld with slow drift (3%). The drift mirrors the searching quality
    #         of the scene — Zira following a thread, the camera following her.
    #         Opens on Zira's terminal: network maps, courier patterns, the thread.
    #         Cross-reference beat: split-screen feel — Zira's data and Noelle's trace running
    #         simultaneously. The camera favors one, then the other.
    #         The recognition moment: push-in on Aeron. Slow. Stops when his face fills the frame.
    #         The moment holds longer than it should. That's the point.
    # LIGHTING: Mapping station: blue-green terminal glow dominant. Warm amber from Zira's
    #           personal lamp (a different lamp than Tessa's — smaller, harsher, functional).
    #           Noelle's terminal: cooler blue-white.
    #           The recognition beat: all light sources hold. Nothing changes except the room.
    # SFX: Loop — mapping station ambient. Terminal processing. The Ghostline carrier hum
    #       beneath everything (restored, steady).
    #      One-shots — data scroll, connection tone (the match), Noelle's keyboard (fast, then stop).
    #      The stop: specific. The absence of typing as Noelle finds it.
    # FX/COMP: Zira's network maps: courier routes spanning years. The pattern emerging.
    #          Noelle's identity trace: registry data, married names, cross-references.
    #          The courier mark: the same mark from the dead drop letter. The thread that connects.
    # BLOCKING: Zira at her station. Noelle at the adjacent terminal (she's been pulled in).
    #           Aeron standing between them. The geography of revelation.
    # CANON: MAJOR PLOT SCENE. The Liora reveal. She's alive.
    #        Requires a3_s18a (the letter) to have fired.
    #        The courier mark from the dead drop matches a long-running network pattern.
    #        Noelle traces the identity. Registry discrepancy. Married name: Rylan.
    # FACE: Aeron — the ground opening under him. Not grief. Something older and more dangerous: hope.
    #        Zira — the hunter who found more than she was hunting for.
    #        Noelle — precise, then shaken. She understands what she's found.

    # ========= VOICE BASELINE =========
    # EMP cadence: Full warmth, but the warmth is disorienting here. The world just shifted.
    # Zira: Intel-delivery mode. Sharp, fast. Then slow. She's recalibrating in real time.
    # Noelle: Data-first. Until it isn't. The identity trace breaks her cadence.
    # Aeron: Internal. The athought carries an earthquake.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MAPPING STATION - EVENING]

    #scene bg_zira_station_evening_emp with dissolve
    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE PATTERN ==========

    "Zira has that look. The one she gets when the Ghostline is telling her something she hasn't translated yet."

    z "I've been cross-referencing courier data from the Outlands relays. The ones on the edge of our network — the stations that receive but rarely transmit."

    z "There's a pattern. Someone has been moving information through the courier network for years. Not supplies. Not tactical data. Stories."

    a "Stories."

    z "Names. Ledgers. Personal histories. The kind of information Echelon scrubbed from every official database."

    z "Someone's been keeping it. Moving it through courier channels like cargo. Drop to drop, relay to relay, for years."

    athought "Names of the lost. Someone keeping count."

    athought "Tessa counts the living. This person counts the erased."

    z "The courier network she's using is old. Pre-Ghostline. I built my network on top of infrastructure that was already there — I just didn't know who laid it."

    "She pulls up the relay map. A thread of courier drops stretching from the Outlands through the outer sectors and into the city's edge. The thread is years old. Consistent. Patient."

    z "I ran the courier marks against the dead drop from Sector 4."

    "She looks at Aeron."

    z "Same source."

    # ========== PHASE 2 — THE CROSS-REFERENCE ==========

    athought "Same source. The letter. The courier mark that predated Zira's network."

    athought "The person who wrote to Marcus and never sent it was the same person moving stories through the Outlands for years."

    z "I asked Noelle to run the pattern against known operatives. Outlands contacts. Anyone with a long-term courier presence."

    "Noelle is at the adjacent terminal. Her hands are moving — the rapid, precise keywork that means she's deep in a data trace."

    n "The courier profile doesn't match any known operative in our records or Echelon's. The pattern is too consistent for a network — it's a single actor. One person, moving through the Outlands relay system, depositing information at intervals."

    n "The Outlands contacts call her 'the story-keeper.' A woman who keeps the names of the lost city."

    z "The woman who remembers everyone."

    athought "The story-keeper."

    athought "Someone in the Outlands, for years, keeping the names Echelon tried to erase."

    athought "Using the same courier network that carried the letter to my father."

    a "Can you identify her?"

    n "I'm running the trace now. The courier mark has a registration — old, pre-standardization, but it links to a citizenship record."

    "Her hands stop moving."

    "That's the tell. Noelle's hands never stop unless the data has stopped her."

    n "Registry discrepancy."

    z "What kind?"

    n "The citizenship record lists two names. Birth name and married name. The married name was added twenty-six years ago and the citizenship was flagged as inactive nineteen years ago."

    n "Inactive. Not deceased. The record was never closed."

    athought "Twenty-six years ago. The year I was born."

    athought "Nineteen years ago. The year she—"

    n "The married name on the record is Rylan."

    # ========== PHASE 3 — THE EARTHQUAKE ==========

    "The room doesn't change. The terminals glow. The Ghostline hums. The ambient loop continues."

    "Everything changes."

    athought "Rylan."

    athought "My mother."

    athought "The story-keeper is my mother."

    "Zira is watching him. Her expression has shifted — the sharp hunter's look replaced by something careful. She's seen the impact before he's finished processing it."

    z "Aeron."

    athought "She's alive."

    athought "She didn't die. She didn't disappear. She left and she's been out there this whole time."

    athought "Keeping names. Keeping track. Doing what Tessa does — counting the people who matter — but from the outside. From the Outlands. For years."

    athought "The letter. She wrote that letter and she never sent it and she left anyway. And she spent the next nineteen years making sure the people Marcus erased weren't forgotten."

    athought "She's alive."

    a "She's alive."

    "He says it out loud. Not to anyone. The sentence needs to exist in the air."

    z "The data is consistent. The courier mark, the registry, the timeline. It's her."

    n "I can confirm the match. The handwriting analysis from the letter is consistent with the registration signature on the citizenship record. Ninety-seven percent confidence."

    "Aeron's hands are on the edge of Zira's terminal. He doesn't remember putting them there."

    athought "She left. She's been out there this whole time. Keeping names. Keeping track."

    athought "And I thought she was dead. Or gone. Filed in the same locked room as everything else that hurt too much to hold."

    athought "She was keeping the names of the lost."

    athought "She was doing what I'm trying to do. She just started before I did."

    "Zira moves. Stands beside him. Not touching — beside. The geography of someone who knows you need a landmark."

    z "She's alive. And she's been running the same kind of operation we have. Smaller. Longer. One person instead of a network."

    z "She built the roads I built on top of."

    "Noelle is quiet. Her hands rest on the keyboard. Still."

    n "If the registry is accurate, she's in the outer Outlands. The relay pattern places her last confirmed drop eleven days ago."

    n "Eleven days. She's still active."

    athought "Eleven days."

    athought "Eleven days ago, my mother put a name in a courier drop. A person Echelon tried to erase. And she made sure someone would remember."

    athought "She's been doing this for nineteen years."

    athought "I've been doing it for months."

    athought "The pause. She gave me the pause. And she's been using it herself the entire time."

    "He takes his hands off the terminal. Straightens."

    a "Can we reach her?"

    z "Through the courier network. It would take time — the Outlands relays are slow. But yes."

    a "Do it."

    "Zira nods. No argument. No clarification needed."

    "Noelle saves the data trace. Her hands are steady now. She looks at Aeron."

    n "For what it's worth — the pattern analysis suggests she's been monitoring Phoenix. Not directly. But the information flow indicates awareness."

    n "She knows about us. Or enough to know something is happening."

    athought "She knows."

    athought "My mother knows we exist. Knows the rebellion is happening. Has been watching from the Outlands through the same courier network she built."

    athought "And she didn't come back."

    athought "Because coming back would mean being found. And being found would mean risking everything she's kept."

    athought "The names. The stories. The record of what Echelon did."

    athought "She stayed away to protect the truth."

    "The mapping station hums. The courier routes thread across the display. Among them, one thread stretches farther than the rest — out past the city's edge, into the Outlands, to a woman who remembers everyone."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("liora_alive_known", True)
    $ flag("story_keeper_identified", True)
    $ npc_remember("Zira", "identified_liora_courier_pattern", tone="careful_awe")
    $ npc_remember("Noelle", "traced_liora_registry_identity", tone="precise_gravity")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s20_the_story_keeper_emp
# cann.chapter: Act III, Phase III — Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After Noelle's Revelation (s19). Requires the letter (s18a).
#   - Zira's cross-referencing leads to the identity trace.
# cann.what_happened:
#   - Zira finds a pattern: someone has been moving stories (names, ledgers, histories of the
#     erased) through the courier network for years. "The story-keeper."
#   - The courier mark matches the dead drop from the letter (s18a). Same source.
#   - Noelle runs the identity trace: registry discrepancy. Married name added 26 years ago
#     (Aeron's birth year). Citizenship flagged inactive 19 years ago (when she left).
#   - Married name: Rylan. Liora is alive.
#   - Aeron: emotional earthquake. She's been in the Outlands, keeping the names Echelon erased.
#   - She built the courier infrastructure Zira's Ghostline was built on top of.
#   - Last confirmed drop: 11 days ago. She's still active. She knows about Phoenix.
#   - She stayed away to protect the truth — the names, the stories, the record.
# cann.aeron_state:
#   - "She's alive." Said aloud because the sentence needs to exist in the air.
#   - The locked room opens: the place where he filed everything about her.
#   - "She was doing what I'm trying to do. She just started before I did."
#   - The pause: her gift, used by both of them.
# cann.path_tracking:
#   - canon_set("liora_alive_known"). flag("story_keeper_identified").
#   - npc_remember for Zira and Noelle.
#   - No player choice. Revelation scene. The weight is enough.
# cann.thematic_flags:
#   - The story-keeper: Liora's role. Tessa counts the living, Liora counts the erased.
#     Parallel methodologies of care across different scales and geographies.
#   - Infrastructure inheritance: Liora built the roads. Zira built on top of them.
#     The rebellion has a grandmother it didn't know about.
#   - "She didn't come back." — staying away to protect the truth. The cost of being the keeper.
#   - 11 days: immediacy. She's not a ghost. She's active. Present tense.
#   - The locked room: the place Aeron sealed his mother's memory. Now open.
# cann.character_moments:
#   - Zira: "She built the roads I built on top of." Recognition of a predecessor.
#     Stands beside him — the landmark when the ground is moving.
#   - Noelle: Hands stop moving. The data stopped her. "Ninety-seven percent confidence."
#     Then: "She knows about us." The analysis that carries hope.
#   - Aeron: Hands on the terminal he doesn't remember gripping.
#     "She's alive." Said out loud. The sentence needed air.
# cann.callbacks:
#   - a3_s18a: The letter. The courier mark. The handwriting. "I fell in love with the pause."
#   - a3_s18: The Weight. Tessa's board. Liora's parallel practice — counting the erased.
#   - a3_s19: The Purge data. Marcus signed the orders. Liora kept the names of those he erased.
#   - The locked room: Aeron's internal sealed archive. First mentioned in the letter scene.
#   - The pause: inherited from Liora. Both of them using it.
# cann.block_status:
#   - PLOT/REVELATION SCENE. No branching. No choice. The revelation is the event.
# cann.requires_followup:
#   - a3_s22: The execution. The courier network leads to her capture.
#   - Reaching Liora through the courier network: the attempt that exposes her.
#   - Liora monitoring Phoenix: she knows about Aeron. What does she know? What has she decided?
#   - The story-keeper's archive: the names and stories she's preserved. Future plot resource.
#   - canon_set("liora_alive_known") gates the execution scene's emotional impact.
