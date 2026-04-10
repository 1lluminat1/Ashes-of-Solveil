# =======================================================
# ACT 3 - Scene 02a: The Silent Table (Obedience Path)
# File: a3_s02a_silent_table_ob.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s02a_silent_table_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s02a_silent_table_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, center-locked (OB style). Slow pans across the table.
    #         Wide establishing shot shows Selene's empty chair. Close-ups on each speaker.
    #         Aeron's shots: profile, or from behind. Never full-face until Noelle confronts him.
    # LIGHTING: Cold 5500K overheads. War room tactical displays cast blue-green glow.
    #           Selene's chair is lit but empty - visual ghost. Shadows under everyone's eyes.
    # SFX: Loop - ventilation hum, distant base activity, tactical display hum.
    #      One-shots - chair scrape, fist on table, papers shuffled, door hiss.
    # FX/COMP: Tactical displays show patrol routes, supply lines. Selene's terminal dark.
    # BLOCKING: Round table. Selene's chair at the head - empty. Aeron stands apart, near the wall.
    #           The four LIs seated around the table, leaning in, arguing across each other.
    # CANON: Hours after the funeral. First command meeting without Selene.
    #        This scene shows the vacuum and Aeron's terrifying stillness.
    # FACE: LIs expressive - grief, anger, fear. Aeron: mask. Flat. Observing.

    # ========= VOICE BASELINE =========
    # Zira: Tactical frustration. Wants to DO something. Anger as coping.
    # Lyra: Faith shaken. Needs structure. Looking for someone to follow.
    # Tessa: Mediating. Worried about the living. Compassion as anchor.
    # Noelle: Observing. Cataloging. Finally speaks the truth no one else will.
    # Aeron: SILENT for most of the scene. When he speaks, it's clipped, cold, efficient.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - DAY]
    # The tactical table. Maps and displays. Five chairs - one empty.
    # Hours after the funeral. The base hums with uneasy quiet.

    #scene bg_war_room_ob with dissolve
    #play ambient "sfx/ambient/war_room_hum.ogg" fadein 2.0

    # --- OPENING: THE EMPTY CHAIR ---

    "The war room smells like cold coffee and recycled air. Tactical displays cycle through patrol routes no one is watching."

    "Selene's chair sits at the head of the table. Empty. No one has moved it."

    "No one has sat in it."

    athought "I stand by the wall. Not at the table. Not in her chair."

    athought "They haven't asked me to sit. I haven't offered."

    athought "This is the first command meeting since we buried her. Since I sat in her chair in the dark and felt nothing."

    # VISUAL: The four LIs around the table. Zira pacing. Lyra still. Tessa leaning forward. Noelle watching.

    #show zira war_room_standing with dissolve
    #show lyra war_room_seated with dissolve
    #show tessa war_room_seated with dissolve
    #show noelle war_room_seated with dissolve

    "Zira stands at the far end, arms crossed, jaw tight. She hasn't sat down since she arrived."

    "Lyra sits with her hands folded, knuckles white. Her eyes keep drifting to the empty chair."

    "Tessa leans forward, datapad in hand, trying to impose order through logistics."

    "Noelle watches. Always watching. Her stylus taps against her tablet in a rhythm only she understands."

    # --- THE ARGUMENT BEGINS ---

    z "We can't just sit here."

    "Zira's voice cuts through the hum. Sharp. Impatient."

    z "Echelon knows we're weakened. Every hour we spend grieving is an hour they spend planning."

    t "We buried her six hours ago, Zira."

    z "And in six hours, three patrol drones have swept our perimeter. They're testing us."

    t "Then we respond when we're ready. Not when grief makes us reckless."

    z "Reckless? I'm talking about survival."

    athought "She's correct. The drones are probing. Standard Echelon doctrine after confirmed leadership loss."

    athought "I don't say this. I watch."

    # --- LYRA'S FRACTURE ---

    l "What would Selene want us to do?"

    "The question hangs. Zira stops pacing."

    z "Selene is dead."

    l "I know that."

    z "Then stop asking what she would want. She wanted to live. She didn't get that either."

    "Lyra flinches. Tessa reaches across the table, hand stopping just short of contact."

    t "Zira."

    z "What? It's true. We don't have the luxury of her guidance anymore. We've to decide for ourselves."

    l "Then who decides? You?"

    z "Someone has to."

    athought "The hierarchy is collapsing. Without Selene, they've no clear chain."

    athought "Zira leads operations. Tessa leads medical. Lyra leads training. Noelle leads intelligence."

    athought "None of them lead command."

    athought "Selene did. Now no one does."

    # --- TESSA TRIES TO MEDIATE ---

    t "We need to focus on what we can control. Supply lines. Patrol rotations. The people who are still alive and need us."

    z "The people who are still alive won't stay that way if we don't act."

    t "Acting without a plan isn't action. It's panic."

    z "And waiting without purpose isn't caution. It's cowardice."

    "Tessa's jaw tightens. For a moment, the medic looks like she might snap back."

    "She doesn't. She exhales. Slow. Controlled."

    t "I'm not a coward. And neither are you. We're grieving. That's allowed."

    z "Grieving doesn't stop bullets."

    # --- NOELLE OBSERVES ---

    "Through all of this, Noelle hasn't spoken. Her stylus taps. Her eyes move from face to face."

    "Now they settle on Aeron."

    athought "She's watching me. She has been watching me since I entered."

    athought "Cataloging. That's what she does. She catalogs."

    athought "I wonder what she sees."

    # --- LYRA LOOKS TO AERON ---

    l "Aeron."

    athought "My name. I didn't expect to hear it."

    l "You haven't said anything."

    athought "I haven't."

    l "What do you think we should do?"

    "Four pairs of eyes turn to him. The wall no longer feels like a safe distance."

    athought "She's asking me to lead. They all are."

    athought "I'm not certain I should."

    athought "I'm not certain I shouldn't."

    # --- CHOICE: RESPONSE ---

    menu:
        "The silence stretches. They're waiting."

        "We maintain discipline. Selene's protocols still apply.":
            $ choice_and_dev(
                _current_scene_id, "_protocols", "OB", factor=1,
                next_scene_label=None,
                note="Takes soft command. OB-aligned. Maintains structure."
            )
            jump .protocols

        "We need information before we act. Noelle, what do we know?":
            $ choice_and_dev(
                _current_scene_id, "_intel", "OB", factor=1,
                next_scene_label=None,
                note="Deflects to intelligence. Methodical. Still OB-aligned."
            )
            jump .intel

        "(Remain silent.)":
            $ choice_and_dev(
                _current_scene_id, "_silence", "OB", factor=2,
                next_scene_label=None,
                note="Maximum OB. His silence becomes the statement. Noelle calls it out."
            )
            jump .silence

    # --- BRANCH: PROTOCOLS ---
    label .protocols:

        a "We maintain discipline. Selene's protocols still apply."

        "His voice is flat. Measured. The words land like orders, not suggestions."

        athought "They aren't my protocols. But someone needs to invoke them."

        z "Selene is gone. Her protocols died with her."

        a "Her protocols kept forty-three people alive through the raid. They apply until we've better ones."

        "Zira's eyes narrow. She doesn't argue."

        t "What does that mean, practically?"

        a "It means we hold position. Reinforce the perimeter. Wait for Echelon to overextend before we respond."

        a "Selene never moved without knowing where she was moving to. Neither should we."

        "The room is quiet. Not agreement - assessment."

        l "That sounds like her."

        athought "It does. I don't know if that's a compliment or a warning."

        $ rel_bump("Zira", respect=1)
        $ flag("ob_took_soft_command", True)

        jump .noelle_observation

    # --- BRANCH: INTEL ---
    label .intel:

        a "We need information before we act. Noelle, what do we know?"

        "He doesn't step forward. Doesn't claim the chair. Simply redirects."

        n "I was wondering when someone would ask."

        "Noelle's stylus stops tapping. She pulls up her tablet, scrolling through data."

        n "Echelon drone sweeps have increased forty percent since the funeral. Consistent with standard post-leadership-loss doctrine."

        n "They're probing for response patterns. Testing whether we still function as a cohesive unit."

        z "And do we?"

        n "That remains to be seen."

        "Her eyes flick to Aeron. Back to the tablet."

        n "There's also an anomaly in Ghostline traffic. An encrypted signal from the quarantined Unders. Repeating. Unidentified source."

        athought "The quarantined Unders. No sanctioned operations run there. No known cells."

        athought "An anomaly."

        t "What kind of signal?"

        n "A request. The same phrase, every four hours: 'Who commands now?'"

        "The room goes still."

        athought "Someone is asking. Someone wants to know who leads."

        athought "Someone is watching."

        $ rel_bump("Noelle", respect=1)
        $ flag("ghostline_signal_revealed", True)

        jump .noelle_observation

    # --- BRANCH: SILENCE ---
    label .silence:

        "He doesn't answer. The silence stretches."

        "Lyra's face falls. Zira's jaw tightens. Tessa looks away."

        athought "I have nothing to offer them. Not yet."

        athought "Words without purpose are noise. Noise isn't command."

        athought "So I say nothing."

        l "Aeron?"

        "Still nothing."

        z "Unbelievable."

        "She turns away, pacing to the tactical display. Her hand slams against the console."

        z "We just lost our commander. The one person who held this together. And he stands there like a statue."

        t "Zira-"

        z "No. I'm done waiting for someone to tell us what to do. If no one else will act, I'll."

        "She pulls up patrol routes. Starts marking positions. The others watch, uncertain."

        athought "Let her. Action without direction will burn her out. She'll learn."

        athought "Or she won't. Either way, it isn't my concern right now."

        $ rel_bump("Zira", trust=-1)
        $ flag("ob_maximum_silence", True)

        jump .noelle_observation

    # --- NOELLE'S OBSERVATION ---
    label .noelle_observation:

        # VISUAL: The argument has settled into uneasy quiet. Noelle stands.

        "The war room settles into fragile quiet. Zira at the displays. Lyra staring at the empty chair. Tessa reviewing supply logs."

        "Noelle stands. Her tablet closes with a soft click."

        n "May I make an observation?"

        athought "She doesn't wait for permission. She never does."

        "She crosses the room. Stops in front of Aeron."

        "Her eyes are steady. Clinical. The gaze of someone cataloging a specimen."

        n "You haven't spoken more than thirty words since the funeral."

        athought "Thirty-two. But close enough."

        n "You delivered a eulogy that lasted four minutes and eleven seconds. Efficient. Correct. Emotionally null."

        n "Since then, you've observed. You've calculated. You've said almost nothing."

        athought "She isn't wrong."

        n "Your stillness frightens them."

        "The words land in the quiet room. Zira pauses at the display. Lyra looks up. Tessa's stylus stops."

        athought "Frightens. Not concerns. Not confuses. Frightens."

        athought "She chose that word deliberately."

        a "Is that an observation or a diagnosis?"

        n "Both."

        "Her head tilts. The analyst studying her subject."

        n "You're processing Selene's death the way Echelon trained you to process casualties. Compartmentalization. Deferred grief. Operational continuity."

        n "It's efficient. It's stable. It's also exactly how Marcus Rylan responded to loss."

        athought "Marcus."

        athought "She's comparing me to my father."

        athought "My hands are shaking. I fold them behind my back before anyone notices."

        athought "She isn't wrong to."

        "Lyra's breath catches. Zira turns fully now, arms crossed."

        z "Noelle."

        n "I'm stating what I observe. That's my function."

        n "Whether anyone acts on it isn't my concern."

        "She returns to her seat. Opens her tablet. The stylus begins tapping again."

        "The room is silent. The kind of silence that has weight."

        athought "Your stillness frightens them."

        athought "Good."

        athought "No. Not good. Efficient. There's a difference."

        athought "There has to be a difference."

        # --- SCENE CLOSE ---

        "The meeting doesn't end. It simply... stops. One by one, they drift to their stations. Their tasks. Their grief."

        "Lyra lingers longest, eyes on Aeron. On the empty chair. On the space between them that feels wider than the room."

        "She doesn't speak. Eventually, she leaves."

        athought "Noelle was right. They're frightened."

        athought "They should be."

        athought "I don't know what I'm becoming. But I know it's efficient."

        athought "Selene would have called that a warning sign."

        athought "Selene is dead."

        athought "I'm what remains."

        # --- END ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s02a_silent_table_ob
# cann.chapter: Act III, Chapter I - Complicity (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Hours after Selene's funeral. Same day as Ashes in Formation.
#   - BEFORE "Stay With Me" (this is WHY Lyra comes to him that night).
# cann.what_happened:
#   - First command meeting without Selene. Her chair is empty.
#   - Zira and Tessa argue about action vs caution.
#   - Lyra looks to Aeron for guidance.
#   - Player choice: invoke protocols, redirect to intel, or remain silent.
#   - Noelle calls out Aeron's stillness: "Your stillness frightens them."
#   - She compares him to Marcus. The comparison lands.
#   - Scene ends with the team fractured and Aeron aware of what he's becoming.
# cann.aeron_state:
#   - OB detachment fully operational. He observes, calculates, speaks minimally.
#   - Noelle's observation lands - he knows he sounds like his father.
#   - His internal response: "Good. No. Efficient. There has to be a difference."
# cann.path_tracking:
#   - Protocols branch: rel_bump Zira respect+1, flag ob_took_soft_command.
#   - Intel branch: rel_bump Noelle respect+1, flag ghostline_signal_revealed (foreshadows Nyra).
#   - Silence branch: rel_bump Zira trust-1, flag ob_maximum_silence.
# cann.thematic_flags:
#   - Empty chair: Selene's absence as visual ghost.
#   - Marcus comparison: The seed of Aeron's OB corruption is named.
#   - "Good. No. Efficient.": His self-awareness is present but rationalizing.
# cann.character_moments:
#   - Zira: Frustrated, wants action. Anger as coping mechanism.
#   - Lyra: Faith shaken. Looking for someone to follow. Frightened by his silence.
#   - Tessa: Mediating. Trying to hold things together. Worried about the living.
#   - Noelle: Observing. Finally speaks the truth. Compares Aeron to Marcus.
# cann.block_status:
#   - ANCHOR (always plays). Choice affects flavor and minor deltas.
# cann.requires_followup:
#   - "Stay With Me": This is WHY Lyra comes to him that night. His silence frightens her.
#   - "Who Commands Now?": The Ghostline signal (if intel branch chosen) foreshadows Nyra.
#   - Noelle's arc: She's the first to name what's happening to him.
