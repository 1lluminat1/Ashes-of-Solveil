# =======================================================
# ACT 3 - Scene 15: Signal Under Fire (Empathy Path)
# File: a3_s15_signal_under_fire_emp.rpy
# Type: ZIRA DEEPENING EROTIC
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s15_signal_under_fire_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s15_signal_under_fire_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28mm, handheld with 8-10% drift during the op. Frenetic energy, close-quarters framing.
    #         During the firefight: fast cuts, low angles, muzzle flash as lighting source.
    #         The alcove: transition to 32mm, handheld steadying. Two-shot that tightens as they do.
    #         Intimacy: camera settles. Minimal movement. Trust the stillness.
    # LIGHTING: Op phase: Ghostline relay glow (blue-green), emergency strips in the tunnel, headlamp spill.
    #           Firefight: muzzle flash, sparks off metal. Harsh and staccato.
    #           Alcove: single Ghostline relay node casting blue-green wash. Warm where their skin catches it.
    #           Post-intimate: the relay node hums. The light is steady now — the repair held.
    # SFX: Loop — tunnel ambient: drip echo, distant machinery, Ghostline carrier hum (restored after repair).
    #      Op phase — tool clicks, panel opens, wire strip, relay connection tone.
    #      Firefight — boots on metal grating, suppressed weapon fire, ricochet, radio burst.
    #      Alcove — breathing, fabric shift, relay hum, heartbeat (not literal — felt in the mix).
    # FX/COMP: Ghostline relay node: cylindrical, wall-mounted, exposed circuitry. Blue-green pulse when live.
    #          The alcove: maintenance recess in the tunnel wall. Two meters deep, one wide. Barely room for two.
    # BLOCKING: Op phase: Zira at the relay panel, Aeron covering the corridor. Professional spacing.
    #           Firefight: back to back. Then sprinting. Then the alcove.
    #           Alcove: seated side by side. Shoulders touching. Knees up. The space forces proximity.
    # CANON: DEEPENING erotic scene for Zira. Not first — that was Act 2 commitment.
    #        The texture is different: confident, not desperate. They know each other's bodies now.
    #        The banter-to-honesty shift is the emotional core. Zira stops deflecting.
    #        Callbacks: Act 2 commitment scene, Ghostline sync, Renn's recording.
    # CONSENT: 3-gate framework. (A) Physical proximity, deliberate touch. (B) Matching intent.
    #          (C) Verbal confirmation — not adrenaline.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, sensory language, warmth even under fire.
    # Zira: Sharp, fast, technically precise during the op. Banter as armor.
    #       In the alcove: the armor cracks. What's underneath is quieter than anyone expects.
    # Aeron: Operational focus during the op. In the alcove: present, patient, matching her pace.

    # --- VISUAL SETUP ---
    # [INT. SECTOR 6 - SUBSURFACE TUNNEL NETWORK - NIGHT]
    # A maintenance corridor beneath the industrial district. Ghostline relay nodes
    # line the walls at fifty-meter intervals. Most are dark. The network is degrading.

    #scene bg_tunnel_sector6_night with dissolve
    #play ambient "sfx/ambient/tunnel_deep_drip.ogg" fadein 2.0

    # ========== PHASE 1 — THE OP ==========

    "The tunnel smells like machine oil and stale air. Condensation beads on the ceiling pipes and drops at irregular intervals — a rhythm that isn't one."

    athought "Fix this one, and the eastern corridor comes back online. Lose it, and we lose secure comms to three sectors."

    z "Hands."

    "Zira doesn't look up from the relay panel. Her left hand is inside the housing, fingers navigating by touch. Her right hand extends backward, palm up."

    a "What do you need?"

    z "The number four probe. The one that looks like a dental instrument designed by a sadist."

    "He finds it in the kit. Places it in her palm."

    z "Thank you. Now shut up for ninety seconds."

    athought "She's not being rude. She's doing microsurgery on a signal junction with her fingers in the dark."

    athought "Zira's focus when she's working is total. The world outside the panel ceases to exist."

    athought "I've learned to love that about her. The way she disappears into the machine and comes back with it fixed."

    "Her fingers move inside the housing. Quick, certain adjustments. The relay node flickers — blue-green light stuttering like a pulse finding its rhythm."

    z "Come on. Come on, you stubborn piece of—"

    "The node pulses. Steadies. The blue-green glow washes over her face."

    z "Got you."

    #play sound "sfx/relay_connection_tone.ogg"

    "The Ghostline carrier hum returns — faint, but present. A low vibration in the teeth and sinuses."

    athought "That sound. I've started associating it with safety. With Zira."

    athought "With things working the way they're supposed to."

    z "Node 6-Kappa is live. Signal strength is—"

    "She pauses. Tilts her head. The diagnostic look."

    z "Seventy-one percent. Not great. I can push it to eighty-five if I reroute the—"

    #play sound "sfx/boots_on_grating_distant.ogg"

    athought "Boots on metal grating. Not ours."

    a "(low) Zira."

    z "(still inside the panel) I heard it."

    a "How long to finish?"

    z "Four minutes."

    a "You have two."

    z "I have four, or we come back and do this again."

    athought "She's right. And the boots are getting closer."

    a "(checking sightline down the corridor) Two contacts. Maybe three. Patrol formation — staggered, weapons up."

    z "Then cover me for four minutes."

    athought "That's not a request."

    # ========== PHASE 2 — THE FIREFIGHT ==========

    "The first shot cracks off the wall two meters above Zira's head. She doesn't flinch. Her hands don't stop."

    #play sound "sfx/suppressed_fire_burst.ogg"

    a "(returning fire, controlled bursts) Zira!"

    z "Three minutes!"

    "Muzzle flash from the corridor. Two Echelon regulars, advancing in leapfrog formation. A third behind — comms, calling it in."

    athought "If the third one gets a signal out, we'll have a full squad in eight minutes."

    "He fires twice. The comms operator drops behind a pipe junction."

    a "They're calling reinforcements."

    z "Two minutes!"

    "A round sparks off the relay housing. Zira pulls her hand out, shakes it — burned fingers — then reaches back in."

    z "You absolute bastard machine. Stay connected."

    athought "She's talking to the relay. Of course she is."

    "He drops one of the advancing regulars with a shot to the shoulder. The man goes down, weapon clattering. The second pulls back to cover."

    athought "Non-lethal. The EMP protocols. Selene's guardrails."

    athought "The comms operator is still behind that pipe junction. I can hear him keying his radio."

    a "Zira, we need to move."

    z "Thirty seconds."

    "The relay node surges. Blue-green light flares bright, then stabilizes."

    z "Eighty-three percent. Close enough."

    "She pulls free, grabs her kit, and they're running."

    #play sound "sfx/boots_running_grating.ogg"

    # --- THE SPRINT ---

    "The tunnel branches at the forty-meter mark. Left toward the surface access. Right toward the maintenance alcoves."

    athought "Left is the exit. Right is deeper."

    athought "The patrol will assume we went left."

    a "Right."

    z "Right's a dead end."

    a "Right has alcoves. We wait them out."

    z "You want to hide in a maintenance closet while Echelon sweeps the corridor."

    a "I want to survive the next twenty minutes. The closet is how."

    z "Fine. But I'm lodging a formal complaint about the accommodations."

    "They run right. The corridor narrows. The alcoves appear — shallow recesses in the tunnel wall for equipment maintenance. Small. Dark."

    "He pulls her into the third one. Deepest. Most shadow."

    #stop ambient fadeout 1.0
    #play ambient "sfx/ambient/alcove_quiet_hum.ogg" fadein 2.0

    # ========== PHASE 3 — THE ALCOVE ==========

    "Two meters deep. Barely wide enough for both of them."

    "They press against the back wall. Shoulders touching. Knees up. The relay node above them — 6-Lambda, a dormant one — casts no light."

    "Boots pass in the corridor. Two sets. Moving fast toward the left branch."

    athought "They took the bait."

    "Silence. The carrier hum from the repaired node is faint here but audible — a low thrum beneath everything."

    "They wait."

    z "(barely a whisper) We almost died."

    a "(same volume) Tuesday."

    z "It's Thursday."

    a "I meant it's a Tuesday kind of event. Routine near-death."

    z "Our baseline for normal is extremely broken."

    "Another patrol passes. Single set of boots. Slower. Checking alcoves."

    "They hold their breath. The footsteps pause. Continue. Fade."

    athought "My shoulder is pressed against hers. I can feel her pulse through the contact — fast, then slowing as the adrenaline metabolizes."

    athought "She smells like solder and tunnel condensation and something underneath that's just her."

    z "(after the footsteps are gone) Extraction?"

    a "Twenty minutes. Noelle's monitoring the patrol cycle. She'll ping the Ghostline when the corridor's clear."

    z "Twenty minutes in a maintenance closet."

    a "You lodged your complaint already."

    z "I'm lodging a supplementary complaint."

    "She shifts. Not away — adjusting. Her shoulder settles more firmly against his. Deliberate."

    athought "There it is. The shift."

    athought "Not adrenaline — though the adrenaline is still humming in both of us."

    athought "Something she decided. The way her shoulder presses into mine isn't accidental."

    # --- THE BANTER CRACKS ---

    z "Aeron."

    a "Yeah."

    z "Do you remember what I said? When we — the commitment scene. The Act 2 thing."

    athought "She doesn't call it by name. She never has."

    athought "The night in the relay alcove. The first time. Her voice in the dark saying words she'd never said to anyone."

    a "Every word."

    z "I said I chose this. Chose you."

    a "I remember."

    z "I want you to know that wasn't adrenaline either."

    athought "She's not looking at me. She's looking at the dark wall of the alcove."

    athought "Zira talks to machines because machines don't require vulnerability. They just require competence."

    athought "When she talks to me like this — without the banter, without the deflection — it costs her something."

    a "I know it wasn't."

    z "Because I've been thinking about it. About whether I said it because we were in the dark and it was easy, or because I meant it."

    a "And?"

    z "I meant it. I mean it. Present tense."

    "Her hand moves to his arm. Not medical — not checking a wound, not applying pressure. Her fingers rest on his forearm, thumb against the inside of his wrist."

    # --- CONSENT GATE A: Deliberate Touch ---

    athought "Her hand on my wrist. Deliberate. She knows what she's doing."

    athought "Zira never touches casually. Every contact is a choice."

    "He doesn't pull away. Turns his wrist so her fingers settle against his pulse."

    z "Your heart rate's elevated."

    a "Yours too."

    z "Mine's always elevated. Caffeine."

    a "That's not caffeine."

    # --- CONSENT GATE B: Matching Intent ---

    "He turns toward her. In the narrow alcove, the movement brings them face to face. Close. The faint carrier hum fills the space between them."

    athought "I can see her in the dark. Not clearly — just the line of her jaw, the glint of the relay node reflected in her eyes."

    athought "She doesn't look away."

    z "Are we doing this here? In a maintenance alcove during an Echelon sweep?"

    a "We seem to have a pattern with alcoves."

    z "We do."

    "Her hand moves from his wrist to his chest. Palm flat. Feeling his heartbeat through his shirt."

    athought "She's not checking. She's choosing."

    # --- CONSENT GATE C: Verbal Confirmation ---

    z "If you want to pretend this is adrenaline, I'll let you. We can go back to banter. I'm very good at banter."

    a "It's not adrenaline."

    z "No."

    a "And I don't want banter right now."

    z "What do you want?"

    a "You. Honest. Like this."

    "She exhales. A sound he's heard before — the last breath before she commits to a circuit repair. The decision point."

    z "Okay."

    "She kisses him. Not like the first time — not the urgency of two people discovering what they are. This is the kiss of someone who already knows."

    athought "Her mouth is warm. Her hand on my chest grips the fabric of my shirt."

    athought "The carrier hum vibrates through the wall behind us. The machine she fixed is singing."

    # [INTIMATE CONTENT HERE]

    # ========== PHASE 4 — AFTERCARE ==========

    "After."

    "The alcove is warm now. The kind of warm that comes from two bodies in a small space and the particular stillness of having been close."

    "Zira leans against him. Her head on his shoulder. Her breathing slow and even."

    athought "She's not making a joke."

    athought "For the first time since I've known her, the silence after isn't filled with deflection."

    athought "She's just here. Quiet. Leaning into me like the wall is optional and I'm not."

    "The carrier hum fills the alcove. The repaired relay node, somewhere down the corridor, is holding steady."

    z "Eighty-three percent signal strength."

    a "What?"

    z "The relay. It's holding at eighty-three. I can hear it in the carrier tone."

    athought "Of course she can."

    a "Is that good enough?"

    z "It's not perfect. But it's connected."

    athought "She means the relay."

    athought "She means more than the relay."

    "Her fingers trace the seam of his sleeve. Idle. Unhurried. The hands that do microsurgery in the dark doing nothing at all."

    z "Extraction in twenty minutes. Don't tell anyone I was quiet for that long."

    a "Secret's safe."

    z "I mean it. If Noelle finds out I went twenty minutes without a sarcastic comment, she'll run diagnostics on me."

    a "She'll run them anyway."

    z "Probably."

    "She doesn't move. Neither does he."

    athought "The alcove is still dark. The patrol has moved on. The Ghostline hums."

    athought "Somewhere above us, the city grinds on, unaware that two people are sitting in a maintenance closet in the dark, and one of them just went quiet for the first time in her life."

    athought "And it was enough."

    "A ping on the Ghostline. Noelle's all-clear signal."

    z "That's us."

    "She stands. Offers him a hand up. He takes it."

    "She doesn't let go immediately. Holds it for a beat. Then releases."

    z "Aeron."

    a "Yeah?"

    z "Present tense."

    athought "Present tense."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=1, affection=1)
    $ flag("zira_deepening_complete", True)
    $ nudge_poly(1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s15_signal_under_fire_emp
# cann.chapter: Act III, Phase II - Deepening (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase II. After the base rebuild. Ghostline restoration is ongoing.
#   - Joint field operation: relay repair in hostile territory.
# cann.what_happened:
#   - Zira and Aeron run a Ghostline relay repair at Node 6-Kappa in the Sector 6 tunnels.
#   - Zira restores the node to 83% signal strength under time pressure.
#   - Echelon patrol stumbles on them. Brief firefight — non-lethal (EMP guardrails).
#   - They escape into a maintenance alcove and wait out the sweep.
#   - Banter gives way to honesty. Zira stops deflecting. "I chose this. Present tense."
#   - Three-gate consent framework leads to intimacy in the alcove.
#   - Aftercare: Zira is quiet. No jokes. Leans into him. "Don't tell anyone I was quiet for that long."
# cann.aeron_state:
#   - Operational focus during the op. Covers her while she works.
#   - In the alcove: patient. Doesn't push. Lets her set the pace.
#   - "I don't want banter right now." — asking for her without the armor.
# cann.path_tracking:
#   - rel_bump("Zira", trust=1, affection=1). flag("zira_deepening_complete").
#   - nudge_poly(1) — second seed. Zira's comfort with vulnerability enables future poly arc.
#   - No player choice — the scene earns itself through prior commitment.
# cann.thematic_flags:
#   - Motifs: Carrier hum (safety, connection), alcoves (recurring intimate space for Zira/Aeron),
#     signal strength as metaphor ("not perfect, but connected"), silence vs banter (armor removal).
#   - "Present tense." — the callback to Act 2 commitment, confirmed and ongoing.
#   - Competence as intimacy — covering each other, trusting each other's skill under fire.
#   - The banter-to-honesty shift is earned by everything before it. She doesn't stop joking because
#     something broke — she stops because something is safe enough not to need the armor.
#   - 83% signal: imperfect connection that holds. Metaphor for the relationship.
# cann.character_moments:
#   - Zira: Talks to machines because they don't require vulnerability. When she talks to Aeron
#     without deflection, it costs her. The quiet in the aftercare is the most intimate thing she's done.
#   - Aeron: Loves the way she disappears into machines and comes back with them fixed.
#     Asks for honesty instead of banter. Doesn't flinch from it when he gets it.
# cann.callbacks:
#   - Act 2 commitment scene: "I chose this." The night in the relay alcove.
#   - a3_s04: Zira's demolition expertise. Professional competence as throughline.
#   - a3_s07: Ghostline damage from the counter-strike. This repair is part of the recovery.
#   - Renn's recording: the distributed backup that survived. The network Zira is restoring.
# cann.block_status:
#   - DEEPENING EROTIC (EMP). No branching. Intimate content marker present.
# cann.requires_followup:
#   - Zira's quiet as character growth — she can be honest now. Future scenes should reflect this.
#   - "Present tense" as recurring motif — Zira's way of saying I'm still here.
#   - The relay network restoration as operational subplot — 83% and climbing.
#   - nudge_poly seeds: Zira's vulnerability here opens the door to later group dynamics.
