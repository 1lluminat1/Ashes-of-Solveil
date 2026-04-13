# =======================================================
# ACT 3 - Scene 07: Echelon Strikes Back (Empathy Path)
# File: a3_s07_echelon_strikes_back_emp.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s07_echelon_strikes_back_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s07_echelon_strikes_back_emp:

    $ show_timeline("DAY 27", "03:00", "Phoenix Secondary Base")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm lens but drained of EMP warmth — handheld with 5-8% drift. Unsteady.
    #         Opens wide on approach (landscape of wrongness), then tightens through the walk-through.
    #         Each station (Dren, Tomás, Kira) gets its own framing grammar:
    #           Dren: Low angle on broken hands. Workshop in wide ruin.
    #           Tomás: Empty chair. Maps scattered. Absence as composition.
    #           Kira: Eye-level. Still. The silence louder than any dialogue.
    #         The recognition scene: camera locks. No drift. Aeron seeing clearly.
    #         LI reactions: tight close-ups, each in their own light.
    # LIGHTING: Approach: exterior blue-grey, pre-dawn. No warmth.
    #           Interior: Emergency strips only — amber pulses. Overhead power severed.
    #           Dren's workshop: sparks from severed wiring. Blue-white flicker.
    #           Kira's corner: single remaining lamp. Warm but isolated — an island.
    #           Recognition beat: holo-table backup power. Green tactical light on Aeron's face.
    # SFX: Loop — silence. Broken by: wind through breached walls, dripping water, electrical crackle.
    #      One-shots — boot on glass, door creak, equipment sparking, Kira's breathing.
    #      ABSENCE: No Ghostline carrier hum. The frequency is dead. That silence is its own SFX.
    # FX/COMP: Damage is surgical — neat cuts, not blast craters. Tool marks visible.
    #          Medical supply shelves: empty, not broken. Comms panels: disabled, not smashed.
    #          The precision is the horror.
    # BLOCKING: Aeron alone for the approach and walk-through. Each station is a stop on a tour of loss.
    #           LI reactions are found, not gathered — he moves to them, they don't come to him.
    # CANON: MAJOR SCENE. The emotional centerpiece of Phase I.
    #        Marcus strikes surgically. He wants Aeron to come home, not die.
    #        The attack pattern is Aeron's own methodology, reflected back.
    #        Callbacks: a2_s13 (Marcus surveillance), a2_s17 (Kira, Dren, Tomás established).
    # FACE: Aeron — shock metabolizing into recognition. The grief comes later. The understanding comes now.

    # ========= VOICE BASELINE =========
    # EMP cadence still present but stripped. Short sentences. Sensory overload.
    # Aeron's internal voice oscillates between present-tense observation and tactical analysis —
    # the Glass training taking over when the human can't process.
    # No one speaks much. Dialogue is sparse. The base speaks for itself.

    # --- VISUAL SETUP ---
    # [EXT. PHOENIX BASE - APPROACH CORRIDOR - PRE-DAWN]
    # The corridor that leads to the base entrance. Aeron is returning from a supply assessment.
    # Something is wrong before he sees it.

    #scene bg_base_approach_predawn with dissolve
    #play ambient "sfx/ambient/wind_tunnel_empty.ogg" fadein 3.0

    # ========== PHASE 1 — THE RETURN ==========

    athought "I hear it first."

    athought "Or rather — I hear the absence of it."

    "The Ghostline carrier frequency should be audible from two hundred meters out. A low hum in the teeth, the sinuses, the space behind the eyes."

    "Silence."

    athought "The carrier is dead."

    athought "Zira's relay network runs twenty-four hours. She has redundancies on the redundancies. The only way the carrier goes silent is—"

    athought "I start running."

    # VISUAL: Aeron at the base entrance. The door is open.
    # Not breached. Not forced. Open. The lock mechanism intact.

    #play sound "sfx/boots_on_concrete_fast.ogg"

    "The base entrance. The blast door is open."

    "Not breached. The locking mechanism is intact — engaged, then disengaged from the outside. Someone had the code."

    athought "Or someone didn't need one."

    athought "Containment breach protocol. Override the lock, walk in. I wrote that procedure."

    athought "I wrote it for Echelon."

    "No perimeter guards. No challenge call. The corridor beyond is dark except for the amber pulse of emergency strips."

    athought "I reach for the Ghostline relay at my wrist. Static."

    athought "Nothing on any frequency."

    "He steps inside."

    #scene bg_base_interior_damaged with dissolve
    #play ambient "sfx/ambient/base_damaged_drip.ogg" fadein 2.0

    # ========== PHASE 2 — THE WALK-THROUGH ==========

    # --- STATION 1: THE COMMON AREA ---

    "The common area. Tables overturned — but not all of them. Three pushed aside, clearing a corridor."

    athought "Entry funnel. Control the space, compress the opposition into a single channel."

    athought "Standard."

    "Scorch marks on the east wall. Controlled bursts. Not suppressive fire — directed."

    athought "They came in from the east. Pressure on the primary exit. Drove everyone west toward the interior."

    athought "Toward the interior. Not toward the exits."

    athought "They weren't trying to scatter us. They were trying to contain us."

    "Food still on the tables. Meals interrupted. A bowl of stew overturned, brown liquid seeping through the cracks."

    athought "This happened hours ago. The stew is cold. The emergency strips have been cycling long enough to dim."

    # --- STATION 2: DREN'S WORKSHOP ---

    # VISUAL: The workshop door hangs from one hinge. Inside: methodical destruction.
    # CAMERA: Low angle. Dren sitting against the wall. His hands in his lap.

    "Dren's workshop."

    "The door hangs open. Inside, every piece of equipment has been dismantled. Not with explosives — with tools."

    "The lathe: drive belt severed, housing cracked at the stress points. The soldering stations: heating elements removed. The salvage rack: every component sorted and scattered."

    athought "They knew exactly what to break."

    athought "Not random destruction. Targeted disassembly. Someone read our inventory and identified every piece of equipment that Dren couldn't replace."

    # VISUAL: Dren. Sitting against the far wall. His hands wrapped in bandages already soaking through.

    "Dren is sitting against the far wall. Someone — Tessa, probably — has already wrapped his hands."

    "The bandages are soaking through."

    athought "His hands."

    athought "They broke his hands."

    athought "The machinist who rebuilt anything mechanical. Who gave the base running water and working ventilation."

    athought "They didn't kill him. They took the one thing that made him irreplaceable."

    "Dren looks up. His eyes are glassy. Shock."

    a "Dren."

    "He doesn't answer. Just looks at his wrapped hands. Then back at the wreckage of his workshop."

    athought "He's cataloguing. Even now. The machinist in him inventorying everything that's been taken."

    athought "Everything he can't fix."

    a "We'll rebuild it."

    "He doesn't seem to hear."

    athought "I don't know if I believe what I just said."

    athought "I say it again anyway."

    a "(quieter) We'll rebuild it, Dren."

    # --- STATION 3: TOMAS'S CORNER ---

    # VISUAL: The corner where Tomás kept his maps. The chair is empty.
    # Maps pulled from the wall, some torn, some taken. His coat still draped over the chair back.

    "Tomás's corner. The maps are gone."

    "Not all of them. The ones showing surface routes — still pinned to the wall. The tunnel maps — every one — pulled down and taken."

    athought "His tunnel knowledge. The routes that Noelle's databases couldn't match."

    athought "They took him for what he knows."

    "His coat is still on the chair. Folded. He didn't have time to grab it."

    athought "Or they didn't let him."

    athought "Tomás is sixty-three years old. He has bad knees and a worse back."

    athought "If they're interrogating him, he'll give them everything. Not because he's weak — because they'll hurt him until it's the only kindness left."

    athought "And then they'll know every tunnel route we've used. Every fallback. Every exit we thought was secret."

    $ flag("tomas_taken", True)
    $ npc_remember("Tomas", "captured_by_echelon", tone="absent")

    # --- STATION 4: KIRA ---

    # VISUAL: The children's corner. Blankets. A lamp still burning.
    # Kira is sitting on her bunk. Legs drawn up. Arms around her knees. Still.
    # CAMERA: Eye level. Steady. No drift.

    "The children's area."

    "The lamp is still on. The blankets are neat — not slept in. Two other bunks are empty. Their occupants elsewhere, being tended to."

    "Kira is on her bunk. Legs drawn up. Arms wrapped around her knees."

    athought "She's alive."

    athought "Marcus specified no children. I know this the way I know my own name."

    athought "Because I know Marcus."

    athought "Children are leverage, not casualties. That's the doctrine. His doctrine."

    "She doesn't look up when he enters."

    athought "She's not whispering to static."

    athought "Kira, who talked to every machine in the base. Who whispered to dead relays because she thought her mother might be listening."

    athought "Silent."

    "He crouches in front of her bunk. Doesn't touch her."

    a "(soft) Kira."

    "Nothing."

    a "Kira, it's Aeron."

    "Her eyes move. Land on him. There's recognition but no response."

    athought "She's in there. Just not here."

    athought "I've seen this before. In the Aeries. In the children brought to the compound after operations."

    athought "The ones who learned that silence is safer than sound."

    athought "I stood in those corridors and did nothing."

    athought "I'm not doing that again."

    a "You're safe. They're gone. I'm not going anywhere."

    "She doesn't respond. He doesn't expect her to."

    athought "I sit on the floor beside her bunk."

    athought "Not touching. Not talking. Just present."

    athought "It's not enough."

    athought "It's what I have."

    # --- STATION 5: THE BASE ITSELF ---

    # VISUAL: Montage of damage. Each detail precise. Each absence deliberate.

    "The rest of the base tells the same story."

    "Medical supplies: taken. Every antibiotic, every surgical kit, every unit of blood substitute. The shelves are empty but intact. Not a single container broken."

    athought "They packed our supplies. Carefully. They'll use them."

    "Communications: the relay panels are disabled. Each one — the same method. A single connection severed at the junction point. Repairable, but not quickly."

    athought "Disabled, not destroyed. They want us blind, not dead."

    "Exit routes: the secondary tunnels show evidence of sealing — barricades placed, then removed. Sealed during the operation, opened after."

    athought "Containment. Controlled pressure. Move the population inward during the strike, then release when it's over."

    athought "No one trampled in a stampede. No one killed trying to flee through a sealed tunnel."

    athought "The precision is obscene."

    # --- RENN'S RECORDING ---

    if flag("ghostline_sync"):

        "One thing survived."

        "Zira's terminal took the same surgical cut as every other system. But the Ghostline backup — the distributed storage she built into the carrier network — wasn't physically present in the base."

        "The recording of Renn. Thirty-seven seconds of a young man explaining how to reset a relay junction."

        athought "They couldn't destroy what they couldn't find."

        athought "Small mercy. The only one."

        $ flag("renn_recording_survived", True)

    # ========== PHASE 3 — THE RECOGNITION ==========

    # VISUAL: Aeron at the holo-table. Backup power. Green tactical light on his face.
    # The attack pattern displayed — entry vectors, pressure points, containment arcs.
    # CAMERA: Locked. No drift. Clarity.

    #play sound "sfx/holo_table_boot.ogg"

    "The holo-table runs on a separate power cell. It boots slowly, flickering."

    "He pulls up the base's internal sensors. The ones that recorded the attack before the power was cut."

    "Entry vectors. Pressure corridors. Containment arcs."

    athought "Containment approach from the east."

    athought "Pressure on the primary exit."

    athought "Secondary routes sealed during the operation."

    athought "Population driven inward. Controlled. Compressed. Then released."

    "He stares at the pattern."

    athought "I know this handwriting."

    #play sound "sfx/heartbeat_low.ogg"

    athought "Containment from the east because the east wall has the weakest acoustic dampening — you can hear the approach, which means the targets move before you breach. It looks like a disadvantage. It's not. You want them moving. Moving targets go where you've funneled them."

    athought "Pressure on the primary exit because human instinct drives toward the last known safe route. Seal the secondaries first and the population compresses itself."

    athought "I designed patrol routes like this. I wrote the tactical framework that makes this pattern possible."

    athought "Third-year Glass Academy. Advanced Population Control."

    athought "I got the highest marks in my cohort."

    athought "Marcus graded the exam."

    $ tp_seed("a3.counter_strike.recognition")

    athought "Marcus didn't just attack us."

    athought "He used me to do it."

    athought "Every tactic. Every pattern. Every instinct I was trained to exploit."

    athought "He read my work like a signature and turned it into an assault plan."

    athought "My methodology. My training. My father's curriculum, applied to the people I chose over him."

    "He braces both hands on the table. The green light flickers across his knuckles."

    athought "This is what it means to be Marcus Rylan's son."

    athought "You don't escape the Aeries. You carry it with you. And one day it comes back, wearing your handwriting, and it hurts everyone you love."

    # ========== PHASE 4 — THE MESSAGE ==========

    # VISUAL: A data chip on the table. Placed, not dropped. Deliberate.

    "The data chip is on the table. Centered. Like a calling card."

    athought "I don't need to check the contents. But I do."

    "Coordinates. The Aeries residential district. Upper quadrant."

    athought "The apartment."

    athought "My apartment. The one I shared with Marcus until I was sixteen. The one with the window that overlooked the parade grounds."

    "A text string beneath the coordinates."

    athought "Three words."

    athought "Bring him home."

    athought "The same words he used in Interlude One. The words the officer heard as mercy and felt as threat."

    athought "I hear them differently."

    athought "I hear a father who broke my people's hands and stole their healer and terrorized a twelve-year-old — carefully, precisely, without killing anyone — because he still thinks I'll come back."

    athought "He's wrong."

    athought "But he's patient. And patient men are more dangerous than angry ones."

    $ flag("marcus_message_received", True)
    $ flag("bring_him_home_callback", True)

    # ========== PHASE 5 — LI REACTIONS ==========

    # Each LI found in their own space. Not gathered — scattered.
    # The attack dispersed them. Aeron goes to each.

    # --- ZIRA ---

    # VISUAL: Zira at her dead terminal. Hands flat on the dark screen.
    # The alcove is intact — the equipment is disabled, not destroyed.

    "Zira's alcove. The screens are dark. Every relay junction severed at the same point."

    "She's standing with her palms flat on the dead terminal. Not moving."

    z "He found us."

    athought "Her voice is level. Too level."

    z "I ran seventeen layers of signal obfuscation. Randomized carrier rotation. Dead-drop relay chains."

    z "And he found us because I wasn't careful enough."

    a "This isn't on you."

    z "Seventeen layers, Aeron. He cut through seventeen layers."

    athought "She's not crying. Zira doesn't cry."

    athought "She inventories. She diagnoses. She plans the next iteration."

    athought "But right now, she's just standing at a dead screen, and the part of her that knows how to move forward hasn't started yet."

    a "He didn't cut through your layers. He went around them."

    z "What?"

    a "The attack pattern. He didn't find us through the Ghostline. He found us through me."

    athought "She turns."

    z "What do you mean?"

    a "The tactics. The approach vectors. The containment pattern. It's Glass Academy methodology. My methodology."

    a "He read our operations and recognized my training. He didn't need to trace the signal. He just needed to know how I think."

    "She stares at him. The diagnostic look — the one that strips systems down to their base components."

    z "So he tracked you through doctrine. Not me through the network."

    a "Yes."

    z "That's—"

    a "Worse. I know."

    athought "Her shoulders drop. Not relief — redistribution. The weight shifting from guilt to something more complex."

    z "We can change your patterns. I can build new protocols. If the vulnerability is behavioral, it's patchable."

    athought "There she is. The next iteration. Already building."

    # --- TESSA ---

    # VISUAL: The clinic. Tessa treating Dren's hands. Steady. Precise.
    # CAMERA: Close on her hands. They're not shaking. Not yet.

    "The clinic. Tessa is rewrapping Dren's hands under better light. Her movements are precise. Clinical."

    athought "Her hands are steady."

    athought "They'll shake later. When no one's looking. When the adrenaline runs out and the body catches up."

    athought "I know because mine do the same thing."

    "She doesn't look up."

    t "Compound fractures. Both hands. Metacarpals two through five on the left. Three and four on the right."

    t "They used a compression tool. Hydraulic, probably. Applied incrementally."

    athought "Incrementally. Meaning they broke his hands slowly. One bone at a time."

    t "I can set them. I can't guarantee function. Not without surgical equipment."

    t "Which they took."

    a "Tessa—"

    t "Don't. Not yet."

    athought "She means: don't be kind. Not while I'm working. Kindness will break me and Dren needs me not to break."

    a "Okay."

    t "When I'm done, you can tell me what happened. I can take it then."

    t "Right now I need to be a medic. Not a person."

    athought "I understand that. Better than she knows."

    athought "I've been not-a-person for years. The difference is that Tessa will find her way back."

    # --- NOELLE ---

    # VISUAL: Noelle at a secondary terminal. Running diagnostics.
    # Her screen shows the attack pattern analysis. She's already mapping it.

    "Noelle has found a secondary terminal with battery power. Her fingers move across the keys in the rapid, unbroken cadence that means she's processing faster than speech."

    n "The behavioral pattern analysis is complete."

    athought "Of course it is. She started before I asked."

    n "He anticipated our behavioral patterns with ninety-four percent accuracy."

    a "And the other six percent?"

    n "The six percent he missed corresponds to deviation markers in your behavioral profile."

    n "Specifically: compassion-motivated decisions, non-tactical resource allocation, and interpersonal consideration patterns."

    athought "The parts of me that aren't Glass."

    n "In simpler terms: he predicted the soldier. He failed to predict the person."

    n "The six percent he missed was the parts of you that aren't Glass anymore."

    athought "It shouldn't be comforting."

    athought "It is."

    a "Can we use that?"

    n "We can. His model is based on your training. Every decision you make that deviates from that training increases the prediction error."

    n "The more human you become, the harder you are to read."

    athought "The more human I become."

    athought "As if humanity is a direction and not a destination."

    athought "Maybe it is."

    # --- SELENE ---

    # VISUAL: Selene in the war room. Standing at the holo-table. Studying the same data Aeron did.
    # Her jaw is set. Her injury — the stitches from her near-death — aches when she stands too long.
    # She's standing anyway.

    "Selene is in the war room. She got there before him. The attack pattern is already on the display."

    sel "I've read it."

    a "Then you see it."

    sel "I see a containment operation executed with zero fatalities."

    athought "The way she says it. Not relief — analysis."

    sel "He disabled our communications. Took our medical supplies. Captured our tunnel expert. Broke our machinist's hands."

    sel "And he didn't kill a single person."

    a "Because he doesn't want us dead."

    sel "This wasn't an attack. This was an invitation."

    athought "She looks at me."

    sel "The coordinates on the chip. The apartment."

    a "He wants me to come home."

    sel "What do you want?"

    athought "What do I want."

    athought "I want Dren's hands to work again. I want Tomás back. I want Kira to whisper to the static again because at least that meant she still believed someone might answer."

    athought "I want to have been someone else's son."

    a "I want to rebuild."

    sel "Good. Because that's the one thing he didn't plan for."

    sel "He planned for retreat. He planned for retaliation. He planned for you at his door."

    sel "He didn't plan for you to stay."

    # --- LYRA ---

    # VISUAL: Back at Kira's bunk. Lyra is already there.
    # She's sitting on the floor beside the bunk. Not touching Kira. Not speaking.
    # Just there. The way Aeron was earlier. But longer. Quieter.

    "Kira's corner. Lyra is on the floor beside the bunk."

    "She's been there since before Aeron started his walk-through. Her hand rests palm-up on the mattress, an inch from Kira's arm. An offer. Not an imposition."

    athought "She's not speaking."

    athought "Not praying."

    athought "Just present."

    "Kira's hand has moved. Just slightly. Her fingers resting against the edge of Lyra's palm. Not holding. Touching."

    athought "Lyra looks up at me."

    athought "She doesn't say anything."

    athought "She doesn't need to."

    athought "Her face says: I'm here. This is where I'm needed. Go do what you need to do."

    athought "So I do."

    # ========== PHASE 6 — THE CHOICE ==========

    # VISUAL: Aeron alone. The war room. Green light. The coordinates glowing on the display.
    # CAMERA: Tight on his face. Then pull back. Wide. The base around him.

    "The war room. The display cycles through damage reports. The coordinates blink."

    athought "Bring him home."

    athought "He broke our machinist's hands because Dren builds things that make us stronger."

    athought "He took Tomás because Tomás knows routes that keep us alive."

    athought "He left Kira untouched because hurting children would make me furious instead of conflicted."

    athought "And he left coordinates because he still believes — after everything — that I'll choose him."

    athought "That I'll look at this base and see the argument for surrender."

    athought "He's wrong."

    athought "Not because I'm brave. Not because I'm righteous."

    athought "Because I looked at Dren's hands and Kira's silence and Lyra on the floor beside a child who won't speak."

    athought "And I know — the way I know my own heartbeat — that leaving is worse than staying."

    athought "That running is exactly what he designed this to make me do."

    menu:
        "The coordinates blink. The base breathes around him — damaged, not destroyed."

        "We don't run. We rebuild.":
            $ choice_and_dev(
                _current_scene_id, "_rebuild", "EMP", factor=1,
                next_scene_label=None,
                note="EMP-aligned: defiance through restoration. We stay and rebuild what he broke."
            )
            jump .rebuild

        "He showed us our vulnerabilities. Now we fix them.":
            $ choice_and_dev(
                _current_scene_id, "_adapt", "EMP", factor=0,
                next_scene_label=None,
                note="OB-lean: tactical learning from the attack. We adapt and harden."
            )
            jump .adapt

    # --- BRANCH: REBUILD ---
    label .rebuild:

        athought "We don't run. We rebuild."

        "He closes the coordinates file. The display goes dark."

        athought "Not because I'm not afraid."

        athought "Because fear is the right response to what just happened. And the right response to fear is to build something worth being afraid for."

        "He walks back through the base. Past the overturned tables. Past Dren's ruined workshop. Past the empty shelves."

        "He stops at Kira's corner."

        "Lyra looks up."

        a "(quiet) We're staying."

        "She nods. Just once."

        "Kira's fingers curl around the edge of Lyra's palm. Not much. But more than before."

        athought "That's enough."

        athought "We start tomorrow."

        $ scene_mark(_current_scene_id, "rebuild_chosen")
        $ flag("base_rebuild_active", True)

        jump .scene_end

    # --- BRANCH: ADAPT ---
    label .adapt:

        athought "He showed us our vulnerabilities. Now we fix them."

        "He doesn't close the coordinates file. He saves it."

        athought "Not because I'm going. Because knowing where he wants me is intelligence."

        athought "Every assumption he made about us is a data point. Every tactic he used is a pattern we can break."

        athought "He built this attack on the soldier I was. We build the defense on the person I'm becoming."

        "He pulls up the damage assessment. Starts cataloguing."

        "Communications: repairable. Timeline: thirty-six hours."

        "Medical supplies: gone. Replacement source: the Sector 9 strike inventory."

        "Tunnel routes: compromised. Alternative mapping: Noelle's databases plus Zira's drone survey."

        athought "Each item is a wound. Each solution is a scar."

        athought "Scars are stronger than the skin they replace."

        "He finds Selene in the corridor."

        a "I need a full operational review. Every protocol he exploited, we rewrite."

        sel "Already started."

        a "And Selene?"

        sel "Yes?"

        a "Tomás. We're getting him back."

        sel "I know."

        athought "She doesn't say 'we'll try.'"

        athought "Good."

        $ scene_mark(_current_scene_id, "adapt_chosen")
        $ flag("base_hardening_active", True)
        $ flag("tomas_rescue_planned", True)

        jump .scene_end

    # --- SCENE END ---
    label .scene_end:

        # VISUAL: Wide shot. The base in emergency light. Damaged but standing.
        # People moving through it. Not panicking — working. The slow machinery of survival.

        "The base breathes. Emergency lights pulse. Somewhere, a pipe drips."

        "Dren sits in his ruined workshop, bandaged hands in his lap, eyes already measuring what he'll need."

        "Zira's terminal is dark but her hands are moving — sketching circuit diagrams on paper, the old way, the way that doesn't need power."

        "Tessa finishes with Dren. Washes her hands. They shake for ten seconds. She watches them shake. Then they stop, and she moves to the next patient."

        "Noelle's keys click in the darkness. Mapping. Always mapping."

        "Selene stands at the war room table. The display is off but she's studying the room itself — the walls, the exits, the architecture of what's left."

        "Lyra sits with Kira. Palm up. Patient."

        "And Aeron walks the perimeter. Checking the breached door. The disabled locks. The severed connections."

        athought "Not as a soldier."

        athought "As someone who lives here."

        #stop ambient fadeout 3.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ flag("echelon_counter_strike_survived", True)
        $ flag("marcus_methodology_recognized", True)
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s07_echelon_strikes_back_emp
# cann.chapter: Act III, Phase I — Proving Ground (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase I. After Orders and Prayers (s06).
#   - The base is hit while Aeron is away on a supply assessment.
#   - Emotional centerpiece of Phase I.
# cann.what_happened:
#   - Aeron returns to find Phoenix Base surgically struck by Echelon.
#   - Phase 1 (The Return): Ghostline dead. Door opened, not breached. No perimeter.
#   - Phase 2 (Walk-Through):
#       Station 1 — Common area: entry funnel, controlled bursts, containment pattern.
#       Station 2 — Dren: workshop destroyed methodically. Hands broken (compound fractures).
#       Station 3 — Tomás: taken. Tunnel maps seized. Being interrogated for route knowledge.
#       Station 4 — Kira: alive (Marcus specified no children). Silent. Not whispering to static.
#       Station 5 — Base: medical supplies taken (not destroyed), comms disabled (not smashed),
#                   exits sealed then unsealed. Surgical precision throughout.
#       Renn's recording: survived on Ghostline backup if ghostline_sync flag set.
#   - Phase 3 (The Recognition): Aeron reads the attack pattern as his own Glass Academy methodology.
#       "I know this handwriting. I wrote patrol routes like this."
#       "Marcus didn't just attack us. He used me to do it."
#       tp_seed fired on recognition.
#   - Phase 4 (The Message): Data chip with coordinates to Aeries apartment. "Bring him home."
#   - Phase 5 (LI Reactions):
#       Zira: guilt over network breach; redirected when Aeron reveals behavioral tracking.
#       Tessa: treating Dren. Hands steady (they shake later). "Right now I need to be a medic."
#       Noelle: 94% accuracy prediction. "The 6% he missed was the parts of you that aren't Glass."
#       Selene: "This wasn't an attack. This was an invitation."
#       Lyra: with Kira. Saying nothing. Palm up. Present.
#   - Phase 6 (Choice): Rebuild (EMP) or Adapt (OB-lean).
# cann.aeron_state:
#   - Shock metabolizing into recognition. Glass training takes over when he can't process.
#   - The recognition scene is the core: his own methodology turned against his people.
#   - "This is what it means to be Marcus Rylan's son."
# cann.path_tracking:
#   - EMP baseline. Rebuild path: base_rebuild_active. Adapt path: base_hardening_active, tomas_rescue_planned.
#   - Both paths: echelon_counter_strike_survived, marcus_methodology_recognized.
#   - tp_seed("a3.counter_strike.recognition") on tactical recognition.
#   - tomas_taken flag set regardless. marcus_message_received, bring_him_home_callback.
# cann.thematic_flags:
#   - Motifs: Handwriting (methodology as signature), precision (surgical violence), silence (Ghostline dead, Kira mute).
#   - "The more human you become, the harder you are to read." — Noelle's thesis.
#   - "This wasn't an attack. This was an invitation." — Selene's read.
#   - Marcus's restraint as the deepest threat: he wants Aeron conflicted, not furious.
#   - The base as body: wounded, not killed. Each station a different organ damaged.
#   - "Not as a soldier. As someone who lives here." — the final reframing.
# cann.character_moments:
#   - Dren: Hands broken. Cataloguing even in shock. The worker who can't work.
#   - Tomás: Absent. His coat on the chair. The human cost of knowledge.
#   - Kira: Silent. The child who talked to machines has stopped talking. Marcus's mercy is its own violence.
#   - Zira: Guilt → redirection → "patchable." Already building the next iteration.
#   - Tessa: "Right now I need to be a medic. Not a person." Hands shake when she lets them.
#   - Noelle: 94% / 6% analysis. Humanity as prediction error. Comforting in its precision.
#   - Selene: "He didn't plan for you to stay." Strategic clarity under pressure.
#   - Lyra: No dialogue. Palm up. The most powerful image in the scene.
# cann.callbacks:
#   - a2_s13: Marcus's "Bring him home" and surveillance expansion.
#   - a2_s17: Dren, Kira, Tomás established. Named community makes the strike personal.
#   - a2_s17: Renn's recording — survived on Ghostline if flag set.
#   - a3_s01: Accountability promise — tested by the impulse to retaliate.
#   - a3_s06: Civilian guardrails — the framework that prevents reckless response.
# cann.block_status:
#   - MAJOR SCENE. Emotional centerpiece of Phase I. Branching choice affects Phase II approach.
# cann.requires_followup:
#   - Tomás rescue operation (flagged in adapt path, implied in rebuild path).
#   - Dren's recovery arc — will his hands function again?
#   - Kira's silence — when does she speak again? What's the trigger?
#   - Marcus's next move — he'll wait. He's patient.
#   - Base rebuild/hardening as ongoing thread through Phase II.
#   - The 6% prediction error as tactical advantage going forward.
#   - "Bring him home" as recurring motif — Marcus's refrain for the act.
