# =======================================================
# ACT 3 - Scene 04: Who Commands Now? (Obedience Path)
# File: a3_s04_who_commands_now_ob.rpy
# Path: OB
# Character Focus: Zira (Ghostline), Ensemble
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s04_who_commands_now_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s04_who_commands_now_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, handheld drift (unusual for OB -- the signal is unsettling).
    #         Close on Zira's hands at the terminal. Wide on the signal bay.
    #         Push-in on Aeron when the voice plays. His face: mask, but attentive.
    # LIGHTING: Ghostline signal bay -- magenta/indigo glow from terminals.
    #           Flickering. The pulse nodes cast shifting shadows. Cold blue underlayer.
    # SFX: Loop -- Ghostline static hiss, terminal hum, distant pulse rhythm.
    #      One-shots -- signal lock tone, voice crackle, Zira's three-tap ritual.
    # FX/COMP: Terminal displays show waveform analysis. The encrypted signal visualized.
    #          Occasional flicker. The quarantined Unders sector highlighted on map.
    # BLOCKING: Zira at her station, headphones on one ear. Others gather as the signal plays.
    #           Aeron stands apart. Observing. Processing.
    # CANON: This is the inciting incident for Nyra's arc. Someone is asking who leads now.
    #        The voice isn't Nyra -- it's one of her followers, testing the waters.
    # FACE: Zira focused, then unsettled. Others: wary. Aeron: calculating.

    # ========= VOICE BASELINE =========
    # Zira: In her element but disturbed. This signal shouldn't exist.
    # Encrypted Voice: Distorted, calm, deliberate. Military cadence.
    # Aeron (OB): Minimal words. Strategic assessment. Interested, not alarmed.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - SIGNAL BAY - NIGHT]
    # Zira's domain. Terminals covered in jury-rigged hardware, Ghostline relay nodes,
    # stolen Echelon equipment. Magenta light. The hum of data in motion.
    # Two days after the funeral.

    #scene bg_signal_bay_ob with dissolve
    #play ambient "sfx/ambient/ghostline_static.ogg" fadein 2.0

    # --- OPENING: ZIRA AT WORK ---

    "The signal bay never sleeps. Even when the base does, the Ghostline pulses -- a heartbeat made of stolen frequencies and borrowed time."

    "Zira sits hunched over her primary terminal, headphones pressed to her good ear. Her fingers dance across the interface, chasing ghosts."

    #show zira signal_bay_working with dissolve

    "She hasn't slept in thirty-six hours. The bags under her eyes match the bruise-purple glow of her screens."

    # VISUAL: A waveform spikes on her display. Anomalous pattern.

    "A waveform spikes. Anomalous. She freezes."

    z "What the..."

    "Her fingers stop. The waveform pulses again -- rhythmic, deliberate. Not random noise."

    z "That isn't Echelon. That isn't ours."

    "She taps three times on the console -- the Ghostrunner's prayer -- and begins isolating the signal."

    # --- THE SIGNAL ---

    "The encryption is military-grade but outdated. Pre-Purge Echelon protocols. Someone kept the old keys."

    z "Origin point... quarantined Unders. Sector Zero-Nine. That's a dead zone."

    z "Nothing transmits from Zero-Nine. Nothing survives there."

    "She runs the decrypt. The waveform resolves into audio."

    # VISUAL: She pulls off her headphones. Hits the speaker toggle.

    "The voice that emerges is distorted, calm, and precise."

    #play sound "sfx/ghostline_voice_crackle.ogg"

    # --- THE VOICE ---

    "Through the static, four words. Repeated. Patient."

    unknown "Who commands now?"

    "Silence. Then the loop begins again."

    unknown "Who commands now?"

    "Zira stares at the terminal. The waveform pulses in perfect rhythm -- four-second intervals. Mechanical. Disciplined."

    z "This has been broadcasting for... six hours. I missed it in the noise."

    "Her jaw tightens. Missing signals isn't something Zira does."

    # --- AERON ARRIVES ---

    # VISUAL: The signal bay door hisses. Aeron enters, drawn by the audio bleeding through the walls.

    #play sound "sfx/door_hiss_soft.ogg"

    athought "I heard it from the corridor. A voice that shouldn't exist, asking a question no one should know to ask."

    #show aeron signal_bay_doorway with dissolve

    "Zira doesn't turn. Her focus is absolute."

    z "Before you ask -- no, I don't know who it's. And no, I don't know how they got this frequency."

    athought "She anticipated me. Good."

    a "Origin?"

    z "Quarantined Unders. Sector Zero-Nine. Echelon locked that zone three years ago. Radiation hazard, supposedly. Nothing goes in or out."

    a "Something is broadcasting."

    z "Something with military encryption keys that shouldn't exist anymore."

    "The voice loops again. Patient. Waiting."

    unknown "Who commands now?"

    athought "Who commands now."

    athought "Selene is dead. The answer should be: no one. Or: everyone. Or: chaos."

    athought "Someone wants to know who took her place."

    athought "Someone is watching."

    # --- OTHERS ARRIVE ---

    # VISUAL: Noelle and Lyra enter. Tessa follows moments later.

    "The signal has drawn them. Like a frequency only the grieving can hear."

    #show noelle signal_bay_standing with dissolve
    #show lyra signal_bay_standing with dissolve
    #show tessa signal_bay_standing with dissolve

    n "I detected the anomaly on my monitoring sweep. What are we looking at?"

    z "Unknown broadcaster. Quarantined sector. Repeating the same question for six hours."

    l "What question?"

    "As if on cue, the voice loops."

    unknown "Who commands now?"

    "Lyra's breath catches. Tessa's hand goes to her chest."

    t "That's... directed. That isn't random interference."

    z "No. Someone knows we lost Selene. Someone wants to know who replaced her."

    n "The phrasing is military. 'Commands' implies hierarchy recognition. They're asking about chain of command, not leadership in abstract."

    athought "Noelle is correct. This isn't a civilian asking. This is someone who understands structure."

    athought "Someone trained."

    # --- ANALYSIS ---

    z "I can't trace it further without sending a ping back. And if I do that, whoever is on the other end will know we're listening."

    a "What are our options?"

    z "Option one: ignore it. Let the signal fade. Whoever they're, they give up eventually."

    z "Option two: respond. Open a channel. Find out what they want."

    z "Option three: go there. Physically. Sector Zero-Nine. See what's actually broadcasting."

    t "Go to a quarantined zone? That's suicide."

    z "Maybe. Or maybe 'quarantine' is what Echelon calls anything they can't control."

    l "You think there are people there? Survivors?"

    z "I think someone is using pre-Purge military encryption from a dead zone. That doesn't happen by accident."

    "The room goes quiet. The voice loops again."

    unknown "Who commands now?"

    athought "Someone is waiting for an answer."

    athought "The question is whether we give them one."

    # --- CHOICE: RESPONSE ---

    menu:
        "The signal pulses. Four words. Patient. Waiting."

        "We respond. Open a channel.":
            $ choice_and_dev(
                _current_scene_id, "_respond", "OB", factor=1,
                next_scene_label=None,
                note="Direct contact. Assertive. OB command posture."
            )
            jump .respond

        "We investigate. Patrol to Sector Zero-Nine.":
            $ choice_and_dev(
                _current_scene_id, "_patrol", "OB", factor=1,
                next_scene_label=None,
                note="Physical reconnaissance. Sets up Nyra encounter directly."
            )
            jump .patrol

        "We wait. Monitor the signal. Let them make the next move.":
            $ choice_and_dev(
                _current_scene_id, "_wait", "OB", factor=0,
                next_scene_label=None,
                note="Cautious. Information gathering. Still leads to patrol."
            )
            jump .wait

    # --- BRANCH: RESPOND ---
    label .respond:

        a "We respond. Open a channel."

        "Zira's eyebrows rise. Not surprise -- assessment."

        z "Direct approach. Bold. Stupid, but bold."

        a "If they wanted to harm us, they wouldn't broadcast openly. They want contact."

        z "Or they want to confirm we exist so they can sell our location to Echelon."

        a "Then we learn that too."

        "Zira studies him for a moment. Then she turns to her console."

        z "Fine. But I'm scrambling our origin. They'll know we're listening, not where we're listening from."

        "Her fingers move. The terminal hums."

        z "Channel open. You're on."

        athought "Who commands now."

        athought "I do."

        a "This is Phoenix Actual. Identify yourself."

        "Static. The loop stops. Silence stretches for three seconds. Four. Five."

        "Then a different voice. Clearer. Female. Calm."

        unknown_female "Phoenix Actual. We've been waiting for you."

        unknown_female "Coordinates to follow. Come alone if you trust discipline. Bring your best if you trust nothing."

        unknown_female "Either way -- come. The Order remembers what the rebellion has forgotten."

        "The signal cuts. Dead air."

        z "...well. That wasn't ominous at all."

        athought "The Order remembers what the rebellion has forgotten."

        athought "Someone out there's offering structure. Discipline. Control."

        athought "Someone who knows exactly what we lost when Selene died."

        $ flag("ghostline_direct_contact", True)
        $ flag("nyra_coordinates_received", True)

        jump .scene_close

    # --- BRANCH: PATROL ---
    label .patrol:

        a "We investigate. Patrol to Sector Zero-Nine."

        z "You want to walk into a quarantined zone based on an anonymous signal."

        a "I want to know who's asking questions about our command structure."

        z "And if it's a trap?"

        a "Then we spring it on our terms. Small team. Recon posture. Extract if compromised."

        "Zira shakes her head, but there's no real objection in it."

        z "Fine. I'll map what routes still exist. Most of them are collapsed or irradiated."

        z "If there's a path, I'll find it."

        t "I'm coming with you."

        a "No. You stay here. If we don't return, the base needs a medic."

        t "If you don't return, the base needs more than a medic."

        athought "She isn't wrong. But I can't risk her."

        a "Zira. Noelle. Myself. Three is enough for recon."

        l "And me?"

        athought "Her voice is quiet. Fragile. She wants to come. She wants to be useful."

        athought "She wants to be close to me."

        a "Hold the base. If we aren't back in twelve hours, assume the worst."

        "Lyra's jaw tightens. She doesn't argue. That worries me more than if she had."

        $ flag("patrol_ordered", True)
        $ flag("recon_team_small", True)

        jump .scene_close

    # --- BRANCH: WAIT ---
    label .wait:

        a "We wait. Monitor the signal. Let them make the next move."

        z "Patient. I can work with patient."

        a "If they're testing us, the test reveals more by how long they wait than how quickly we respond."

        a "Track the signal. Map any changes. Report anything new immediately."

        z "Already on it."

        "The voice loops again. Unbothered by their silence."

        unknown "Who commands now?"

        athought "We don't answer. Not yet."

        athought "But someone will have to. Soon."

        # --- TIME SKIP: 8 HOURS LATER ---

        "Eight hours later, the signal changes."

        #scene black with fade
        #pause 1.0
        #scene bg_signal_bay_ob with dissolve

        "Zira's terminal pings. She jolts awake from a half-doze, fingers already moving."

        z "New transmission. Same source. Different content."

        "She plays it. The voice is clearer now. Female. Calm. Certain."

        unknown_female "We've waited long enough. If Phoenix won't answer, we'll come to you."

        unknown_female "Sector Four perimeter. Six hours. The Order remembers what the rebellion has forgotten."

        unknown_female "Bring whoever commands now. We've much to discuss."

        "The signal cuts."

        z "They're done waiting. They're coming to us."

        athought "The Order remembers what the rebellion has forgotten."

        athought "They're forcing contact. On their terms."

        athought "Unless we move first."

        a "Patrol. We meet them at Sector Four. Our ground, not theirs."

        z "Now you want to move?"

        a "Now I have a location. Before, I had questions. Questions don't win engagements."

        $ flag("nyra_forcing_contact", True)
        $ flag("patrol_ordered", True)

        jump .scene_close

    # --- SCENE CLOSE ---
    label .scene_close:

        # VISUAL: The signal bay hums. The team disperses to prepare.

        "The Ghostline static fills the silence. Somewhere in the quarantined dark, someone is waiting."

        "Someone who asks the right questions. Someone who remembers what discipline means."

        athought "Who commands now."

        athought "They'll have their answer soon enough."

        # --- END ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")

        return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s04_who_commands_now_ob
# cann.chapter: Act 3
# cann.chapter_start: False
# cann.when_in_timeline: Two days after funeral. After "Stay With Me."
# cann.what_happened:
#   - Zira intercepts an anomalous Ghostline signal from quarantined Sector Zero-Nine.
#   - The signal loops: "Who commands now?" -- someone knows about Selene's death.
#   - The team gathers to assess. Noelle notes the military phrasing.
#   - Player choice: respond directly, patrol to investigate, or wait.
#   - All paths converge to contact with the unknown force (Nyra's people).
#   - The voice: "The Order remembers what the rebellion has forgotten."
# cann.aeron_state:
#   - OB command posture. Minimal words, strategic assessment.
#   - He recognizes the signal as an opportunity, not just a threat.
# cann.path_tracking:
#   - Respond: flag("ghostline_direct_contact"), flag("nyra_coordinates_received")
#   - Patrol: flag("patrol_ordered"), flag("recon_team_small")
#   - Wait: flag("nyra_forcing_contact"), flag("patrol_ordered") (delayed)
# cann.thematic_flags:
#   - "Who commands now?" -- the question that haunts OB Act 3.
#   - The voice offers structure, discipline, control -- exactly what Aeron craves.
#   - Ghostline as nervous system of the Unders -- Zira's domain.
# cann.character_moments:
#   - Zira: In her element but disturbed. Missed the signal for six hours -- that bothers her deeply.
#   - Noelle: Military phrasing analysis. Clinical assessment.
#   - Tessa: Reacts emotionally to the directed nature of the signal.
#   - Lyra: Breath catches. Wants to come on patrol. Doesn't argue when told no.
# cann.block_status:
#   - ANCHOR (always plays). Choice affects approach but all lead to patrol.
# cann.requires_followup:
#   - "Echoes in the Rain" -- the patrol where they encounter Nyra's forces.
#   - "Request for Alignment" -- Nyra's first face-to-face contact.
#   - The OB theme: order filling the vacuum Selene left.
