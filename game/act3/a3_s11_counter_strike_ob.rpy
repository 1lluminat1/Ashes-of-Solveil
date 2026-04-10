# =======================================================
# ACT 3 - Scene 11: Counter-Strike (Obedience Path)
# File: a3_s11_counter_strike_ob.rpy
# Path: OB
# Type: OPERATION
# Character Focus: Aeron, Nyra (synchronized command), Zira (aftermath)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s11_counter_strike_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy

label a3_s11_counter_strike_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm for the intel delivery, then 50mm locked for planning.
    #         Operation: split-screen mirrored movement. Aeron left, Nyra right.
    #         Same gestures. Same timing. The choreography of shared command.
    #         Kill zone: overhead wide shot. The box closing. Clinical.
    #         Aftermath: long lens, shallow focus. Nyra's soldiers working.
    #         Zira watching from the perimeter. The last shot: bodies being moved.
    # LIGHTING: Intel delivery: tactical blue (war room). Planning: same, harsher.
    #           Operation: exterior night. Sodium and moonlight. Controlled shadows.
    #           Aftermath: grey pre-dawn. The same monochrome as the depot.
    # SFX: Loop -- night urban: wind, distant infrastructure, radio static.
    #      Operation: suppressed fire, movement on gravel, body impacts, comms clicks.
    #      Aftermath: silence. Wind. Body bag material rustling.
    #      One-shots -- Nyra's datapad ping, weapon charges, breach detonation.
    # FX/COMP: Intel display: kill team profiles, approach vectors, timing.
    #          Operation: tactical overlay showing the box formation closing.
    #          Aftermath: body recovery. Professional. No urgency.
    # BLOCKING: Intel: Nyra enters war room. Datapad to Aeron. Close conference.
    #           Planning: both at the table. Mirror posture. Forty minutes.
    #           Operation: two teams. Synchronized. The kill team walks into a box.
    #           Aftermath: Zira arrives. Observes. Speaks.
    # CANON: Echelon sends a targeted kill team for Aeron. Eight elite operatives.
    #        Nyra's intelligence network detects them 40 minutes out.
    #        Aeron and Nyra turn the hunters into the hunted. Peak OB efficiency.
    # FACE: Aeron: operational mask. Nyra: calm, synchronized. Zira: unsettled.

    # ========= VOICE BASELINE =========
    # OB Aeron: Peak command. Short, precise. No contractions during operation.
    #           Post-op: the silence is its own language.
    # Nyra: Mirror cadence. They finish each other's sentences during planning.
    #       Post-op: "Speed is mercy." Her doctrine, crystallized.
    # Zira: Aftermath only. Disturbed by the speed. The efficiency. The silence.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - 0140]
    # Then: [EXT. SECTOR THREE - INDUSTRIAL CORRIDOR - 0220]
    # Then: [EXT. SECTOR THREE - AFTERMATH - 0240]

    #scene bg_war_room_ob with dissolve
    #play ambient "sfx/ambient/base_hum_cold.ogg" fadein 1.5

    # --- INTEL ---

    "0140. The war room is dark except for the tactical displays. Aeron is alone, reviewing patrol reports."

    athought "The third night this week I have not slept. The patrol data blurs. The numbers hold still but the letters drift."

    athought "Insomnia is not a weakness. It is a condition. I manage it."

    "The door hisses. Nyra enters without knocking. She hasn't knocked since the second day."

    #show nyra war_room_standing with dissolve

    "Her datapad is already extended. Her face is calm but her eyes are sharp. Something is different."

    ny "Kill team. Eight operatives. Tier-two Echelon. They crossed the Sector Three checkpoint fourteen minutes ago."

    athought "Kill team."

    athought "Not a sweep. Not a patrol. A team assembled specifically to find and eliminate a target."

    a "Target?"

    ny "You."

    "She sets the datapad on the table. The display shows eight personnel profiles. No names -- designations. Tactical loadouts. Movement vectors."

    ny "My network intercepted their deployment order forty-three minutes ago. I've been tracking their approach since."

    a "Forty-three minutes. You waited three minutes to tell me."

    ny "I spent three minutes confirming the intelligence and mapping their approach corridor. I don't bring you problems. I bring you solutions."

    athought "She waited until she had the full picture."

    athought "Most people would have run in screaming."

    athought "She walked in with a plan."

    # --- PLANNING ---

    "The tactical display shifts. Nyra's approach vectors overlay the industrial corridor grid."

    ny "They're using the maintenance tunnels beneath Sector Three. Standard Echelon infiltration route. They'll surface here --"

    "She taps the display."

    ny "-- at the junction of corridors seven and twelve. Open ground for approximately forty meters before they reach our perimeter."

    a "Forty meters of open ground. That is where we take them."

    ny "Yes."

    "Their eyes meet across the table. No discussion needed. The geometry is self-evident."

    a "Two teams. Alpha holds the north elevation. Bravo seals the tunnel exit behind them. When they surface, they are in a box."

    ny "The corridor walls are reinforced concrete. No lateral escape. Elevation advantage from the loading platforms on both sides."

    a "Crossfire angles?"

    ny "Thirty-seven and forty-two degrees. Overlapping fields. No dead zones."

    a "Timeline?"

    ny "They surface in twenty-six minutes. We need to be in position in twenty."

    athought "Twenty minutes to position two teams, establish fields of fire, and set the trap."

    athought "With conventional forces, impossible."

    athought "With Nyra's soldiers, comfortable."

    a "Your soldiers take Bravo. Mine take Alpha."

    ny "Agreed. I will command Bravo from the tunnel exit. You take the north elevation."

    "She picks up the datapad. The planning is done. Thirty-eight seconds of discussion for an operation that will end eight lives."

    athought "Thirty-eight seconds."

    athought "We did not need longer."

    athought "That is the efficiency she promised."

    athought "That is the efficiency I wanted."

    # --- THE OPERATION ---

    #scene bg_sector3_corridor_night with dissolve
    #play ambient "sfx/ambient/urban_night_industrial.ogg" fadein 2.0

    "0218. The industrial corridor is dark. Wind funnels between the reinforced walls, carrying the smell of machine oil and old rain."

    "Alpha team is in position on the north loading platform. Six fighters. Weapons trained on the forty meters of open ground."

    athought "I can see the tunnel exit from here. The grate is still closed. In four minutes, eight people will push through it."

    athought "They think they are hunting me."

    "Comms click."

    ny "Bravo in position. Tunnel exit is sealed from our side. When they surface, the only way out is through us."

    a "Confirmed. Hold fire until my mark."

    ny "Understood."

    "Silence. The wind. The industrial hum of a city that never fully sleeps."

    athought "Eight elite Echelon operatives. Tier-two. Trained for close-quarters termination."

    athought "They have been briefed on our patrol routes, our communication frequencies, our leadership structure."

    athought "They know where I sleep."

    athought "They do not know that we know."

    "0222. The tunnel grate shifts."

    "The first operative emerges in a low crouch. Night-vision equipped. Weapon up. He scans the corridor. Sees nothing."

    "He signals. Three more emerge. Then three. Then the last."

    "Eight figures in the open ground. Moving in diamond formation. Professional. Disciplined."

    athought "They are good."

    athought "It does not matter."

    "They are twelve meters from the north platform when Nyra's voice comes through the comms."

    ny "Sealed."

    "Behind them, the tunnel exit locks. A dull metallic thud that carries in the corridor. The last operative turns."

    "Too late."

    a "Mark."

    #play sound "sfx/crossfire_burst.ogg"

    "The crossfire is absolute."

    "Alpha team from the north elevation. Bravo team from the south. Thirty-seven degrees and forty-two degrees. Overlapping fields. No dead zones."

    "The first two operatives drop before they can identify the source. The third returns fire -- into the wrong elevation. A round sparks off the loading platform. Nowhere close."

    "The fourth and fifth attempt to break formation. There is nowhere to go. Reinforced concrete on both sides. Sealed tunnel behind. Crossfire ahead."

    "The sixth makes it three steps toward the south wall before Bravo team adjusts. Two rounds. He falls."

    "The seventh drops his weapon. Raises his hands."

    "A single shot from the north platform. He falls."

    athought "He surrendered."

    athought "The order was full suppression."

    athought "He surrendered."

    "The eighth operative reaches the tunnel grate. Slams against it. It does not move. He turns, weapon up, and fires a burst toward the north elevation."

    "Four rounds answer. He sits down against the grate. Doesn't move again."

    "Silence."

    "The wind carries the sound of the last shot away. The corridor holds its breath."

    ny "All targets neutralized."

    a "Confirm count."

    ny "Eight. Matching deployment order. No survivors."

    athought "No survivors."

    athought "The seventh man raised his hands."

    athought "No survivors."

    "Nineteen seconds. First shot to last."

    # --- AFTERMATH ---

    #scene bg_sector3_corridor_dawn with dissolve
    #play ambient "sfx/ambient/wind_urban_quiet.ogg" fadein 2.0

    "Nyra's soldiers descend into the kill zone. The work begins."

    "Weapons collected. Identification recovered. Communications equipment secured for Noelle's analysis. Bodies arranged for removal."

    "Professional. Methodical. The same procedure as the depot. The same absence of urgency."

    "Aeron descends from the north platform. The corridor smells like cordite and something else. Something organic."

    athought "Nineteen seconds."

    athought "Eight lives."

    athought "The math reduces. It always reduces."

    "Nyra meets him at the center of the kill zone. Her uniform is clean. Her breathing is even."

    ny "Their communications equipment was active. Echelon will know they failed within the hour."

    a "Good."

    ny "Good?"

    a "They sent eight to kill me. Eight will not return. The message is the absence."

    ny "Yes."

    "Something passes between them. Not warmth. Recognition. The shared language of people who solve problems in the same grammar."

    "Nyra's soldiers lift the first body onto the transport. No ceremony. No hesitation."

    # --- ZIRA ---

    "Zira arrives with the Ghostline team twenty minutes later. The corridor is already clean. Only the scuff marks on the concrete remain."

    #show zira corridor_standing with dissolve

    "She walks the kill zone. Reads the geometry. The angles. The positions."

    z "That was faster than it should have been."

    ny "Speed is mercy."

    "Zira turns to look at Nyra. Holds the look."

    z "You keep saying that."

    ny "It keeps being true."

    z "The seventh one. North platform angle. He wasn't moving when he was hit."

    "A beat. Nyra's expression does not change."

    ny "The engagement parameters were full suppression. There are no exceptions in a kill-team neutralization."

    z "He put his weapon down."

    ny "And if he had picked it up again?"

    z "He didn't."

    ny "Because he didn't have the chance."

    "Zira's jaw works. She turns to Aeron."

    z "You saw it."

    athought "I saw it."

    athought "He surrendered. The shot came from our platform."

    athought "Full suppression. No exceptions."

    athought "I gave the order."

    "Aeron says nothing."

    "The silence is its own statement."

    "Zira stares at him. Three seconds. Four."

    z "Right."

    "She walks to the relay equipment. Begins working. Her back to both of them."

    "Nyra watches her go. Turns to Aeron."

    ny "She'll process it."

    a "Yes."

    ny "The operation was flawless. Zero Phoenix casualties. Echelon kill team neutralized. Intelligence recovered."

    a "Yes."

    ny "The seventh man would have done the same to us."

    "Aeron looks at the scuff marks on the concrete. The only evidence that anything happened here."

    a "Yes."

    "Nyra nods. She walks toward the transport. Her footsteps are precise."

    "The corridor is empty. The wind moves through it. The scuff marks catch the first grey light."

    athought "The seventh man raised his hands."

    athought "Speed is mercy."

    athought "Both of those things are true."

    athought "Neither of them is enough."

    # --- END ---

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "completed")
    $ canon_set("kill_team_neutralized")
    $ npc_remember("Nyra", "counter_strike", tone="synchronized_command")
    $ npc_remember("Zira", "counter_strike", tone="saw_the_seventh")
    $ flag("ob_peak_efficiency", True)
    $ flag("seventh_man_surrendered", True)

    return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s11_counter_strike_ob
# cann.chapter: Act III, Phase I -- Consolidation
# cann.chapter_start: False
# cann.when_in_timeline: Days after Sector 4 strike. Echelon's targeted response.
# cann.what_happened:
#   - Echelon sends 8 elite operatives (Tier-2) to assassinate Aeron specifically.
#   - Nyra's intelligence network detects them 43 minutes out. She brings the intel.
#   - Aeron and Nyra plan the ambush reversal in 38 seconds. Shared tactical grammar.
#   - The kill team walks into a box. Crossfire. 19 seconds. 8 dead. 0 Phoenix losses.
#   - The seventh operative surrendered. Was shot anyway. Full suppression order.
#   - Zira witnesses the aftermath. Sees the seventh man's angle. Confronts Nyra.
#   - Nyra: "Speed is mercy." Aeron: silence.
#   - Peak OB efficiency -- and the moral cost embedded in it.
# cann.aeron_state:
#   - OB at peak capability. The planning is instinctive. The execution is flawless.
#   - Insomnia noted (third night without sleep).
#   - The seventh man: "I gave the order." The silence after Zira asks is the tell.
#   - "Both of those things are true. Neither of them is enough."
# cann.path_tracking:
#   - No player choice -- the scene IS the choice (OB path commitment).
#   - canon_set("kill_team_neutralized")
#   - flag("ob_peak_efficiency"), flag("seventh_man_surrendered")
#   - npc_remember for Nyra (synchronized command) and Zira (saw the seventh).
# cann.thematic_flags:
#   - Mirrored command: Aeron and Nyra as one unit. Same posture, same timing.
#     The synchronized movement that was beautiful in EMP/Lyra field sync is COLD here.
#   - "Speed is mercy" -- Nyra's doctrine, repeated. Becoming mantra.
#   - The seventh man: the moral cost of "no exceptions." He surrendered. He died.
#     Aeron saw it. Aeron said nothing. The silence is complicity.
#   - 38 seconds of planning for 8 deaths. The efficiency IS the horror.
#   - "I don't bring you problems. I bring you solutions." -- Nyra's value proposition.
#   - Zira: "That was faster than it should have been." She tracks the acceleration.
#   - The corridor cleaned. Scuff marks only. Evidence erased. Professional.
#   - "The message is the absence." -- Aeron weaponizing silence itself.
# cann.character_moments:
#   - Nyra: "I spent three minutes confirming the intelligence." Professional. Complete.
#     "Speed is mercy." Doctrine as shield. She does not flinch at the seventh man.
#   - Zira: "He put his weapon down." She saw it. She names it. She gets silence.
#     "Right." -- one word that carries an entire relationship's worth of disappointment.
#   - Aeron: Three "yes" responses to Nyra in sequence. Monosyllabic. The mask complete.
#     But: "The seventh man raised his hands." The thought he cannot dismiss.
# cann.block_status:
#   - ANCHOR (always plays). No choices -- the absence of choice IS the point.
#   - The seventh man thread carries forward. Zira remembers.
# cann.requires_followup:
#   - The seventh man becomes a recurring ghost. Zira will reference it.
#   - Echelon's response to losing the kill team -- escalation in Phase II.
#   - The MONITOR assessment (Interlude 3 OB) means Echelon expected partial loss.
#     The kill team may have been a test, not a genuine attempt. Nyra should notice.
#   - Aeron's insomnia thread -- escalates. Three nights without sleep noted.
#   - Nyra's intelligence network: how does she get Echelon deployment orders?
#     Zira should investigate. The answer matters.
