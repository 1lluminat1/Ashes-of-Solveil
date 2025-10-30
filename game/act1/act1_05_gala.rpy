# ===================================================
# ACT 1 - Scene 5: The Gala
# File: act1_05_gala.rpy
# ===================================================

# --- Character definitions (place outside any label) ---
define e1 = Character("Elite 1")
define e2 = Character("Elite 2")
define e3 = Character("Elite 3")
define ye1 = Character("Young Elite 1")
define ye2 = Character("Young Elite 2")
define ye3 = Character("Young Elite 3")
define cadet = Character("Daren")
# Lyra `l` assumed defined globally.
# --------------------------------------------------------

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_05_gala"
$ scene_mark(_current_scene_id, "entered")

label act1_05_gala:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35–38mm stabilized glide; gentle 3% push on stress beats; avoid frontal CU of Aeron until Marcus entrance.
    # LIGHTING: Performative warmth (3000K chandeliers) over cold marble base (5200K bounce); 3:1 key/fill; soft rim from sconces.
    # SFX: Loop — strings + low conversation bed (-18 LUFS); one-shots — glass clinks, soft heel clicks, hinge sighs.
    # FX/COMP: Subtle specular blooms, reflection cards on floor, floating dust motes; no rain (Aeries above cloud deck).
    # BLOCKING/PROPS: Chandelier cluster, portrait wall spill, holo-feeds rotating above bar, Council attachés orbiting.
    # FACE: Keep Aeron’s face partial/obscured in early beats; full reveal on Marcus pass.

    # ========= VOICE BASELINE =========
    # OB baseline cadence (clipped/procedural). Local warmth permitted on EMP-gated branches.

    # VISUAL: Lavish gold wash over marble; chandeliers; strings under low conversation.
    "{i}The ballroom breathes manufactured warmth—chandeliers, velvet, the sweet smell of curated luxury.{/i}"
    pause 0.7

    a "{i}All this gold to smooth over the cracks. Plaster over decay with opulence.{/i}"
    pause 0.6
    a "{i}Six hours ago, I killed four people in Sector 7.{/i}"
    pause 0.8
    a "{i}Now I’m here. Smiling. Composed. As if blood rinses off that easily.{/i}"
    pause 0.9
    a "{i}But that's what they want, right? No conflict. No conscience. Just transition.{/i}"
    pause 0.9

    # VISUAL: The ballroom swells—music crescendos, voices layer, chandeliers pulse with reflected motion.
    "{i}The air thickens. Perfume, wine, polished metal. Too much of everything.{/i}"
    pause 0.7
    a "{i}Every surface reflects. Every sound echoes. No silence. No stillness. Just performance layered on performance.{/i}"
    pause 0.9

    # NEW: Pressure without break — subtle internal crack
    a "{i}This is protocol. Eyes ahead. Breath steady. Form intact.{/i}"
    pause 0.6
    a "{i}Still, something in the rhythm skips—half a heartbeat off.{/i}"
    pause 0.8
    a "{i}No one would notice.{/i}"
    pause 0.6
    a "{i}But I do.{/i}"
    pause 0.7
    a "{i}And cracks never start loud.{/i}"
    pause 0.9

    # VISUAL: A young man in full ceremonial dress approaches—confident stride, silver Band glinting.
    cadet "Aeron Rylan. Thought that was you."
    pause 0.6

    # VISUAL: Aeron steadies; tunnel clears.
    a "(turns) Daren."
    pause 0.6

    # VISUAL: Handshake; Band catches chandelier light.
    cadet "Been a while. Not since the Academy, right?"
    pause 0.6
    a "Something like that."
    pause 0.6

    cadet "(glances at medals, impressed) Heard about your last operation. Sector Nine?"
    pause 0.6
    a "(neutral) Sector 7. This morning."
    pause 0.7
    cadet "(surprised) This morning? And you're here tonight?"
    pause 0.6
    a "Recovery’s for people who feel it."
    pause 0.7
    cadet "(nervous laugh) Cold. They really call you that?"
    pause 0.6
    a "They do."
    pause 0.7

    "{i}He respects the record. Fears the person.{/i}"
    pause 0.7

    cadet "Look, I just wanted to say... your record is insane. 390 operations, zero failures?"
    pause 0.7
    a "(neutral) Metrics don't lie."
    pause 0.6
    cadet "That's... that's impossible. In seven years?"
    pause 0.6
    a "Not impossible. Just inhuman."
    pause 0.8
    cadet "(uncomfortable) I didn't mean—"
    pause 0.6
    a "You did. And you're right."
    pause 0.9

    "{i}He touches his Band like a talisman. Proof he belongs. Proof he's safe.{/i}"
    pause 0.7
    "{i}And proof he's not like me.{/i}"
    pause 0.7

    cadet "Your father must be... proud."
    pause 0.6
    a "He has expectations. I meet them."
    pause 0.7
    cadet "That's... that's all any of us can do, right?"
    pause 0.6
    a "(looks at him directly) Is it?"
    pause 0.9

    "{i}For a moment, something passes between them. Not quite understanding. Just... distance.{/i}"
    pause 0.8

    # --- PLAYER CHOICE: How does Aeron respond to Daren ---
    menu:
        "Daren's smile wavers."
        "Respond with cold courtesy.":
            $ apply_choice_once(
                _current_scene_id, "_daren_cold_courtesy", "OB", factor=1,
                next_scene_label="act1_05_gala",
                note="Reasserts performance persona; reinforces fear/respect myth."
            )
            a "Enjoy the gala, Daren."
            pause 0.6
            # VISUAL: Aeron turns away; Daren's smile collapses into relief.
            cadet "Yeah. You too. Stay... stay sharp."
            pause 0.6
            "{i}He retreats into the crowd, grateful for the exit.{/i}"
            pause 0.7
            a "{i}He’ll tell that story tomorrow. ‘Didn’t flinch. Didn’t blink.’{/i}"
            pause 0.7
            a "{i}Let him.{/i}"
            pause 0.8

        "Acknowledge the awkwardness.":
            $ apply_choice_once(
                _current_scene_id, "_daren_acknowledge", "EMP", factor=1,
                next_scene_label="act1_05_gala",
                note="Permits vulnerability without breaking form; micro-connection."
            )
            $ set_scene_flag(_current_scene_id, "acknowledge_daren")
            if pass_emp_gate(2):
                a "You don't have to do this."
                pause 0.6
                cadet "(confused) Do what?"
                pause 0.6
                a "(softer) Pretend we’re still who we were. We're not."
                pause 0.9
                # Hidden True Path increment — unrepressed-empathy (naming truth)
                $ adjust_true_path_resonance_once("a1.gala.daren_ack", 1)
            else:
                a "You don’t have to pretend. We’re not friends anymore."
                pause 0.8

            cadet "(pause) …No. I guess we’re not."
            pause 0.7
            "{i}For a moment, something real passes between them. Fragile. Brief.{/i}"
            pause 0.8
            cadet "(quieter) Take care of yourself, Aeron. If you still can."
            pause 0.7
            a "I’ll try."
            pause 0.7

            a "{i}He walks away. Not relieved. Just... sad.{/i}"
            pause 0.7
            a "{i}He sees it. What I’ve become.{/i}"
            pause 0.6
            a "{i}Maybe that's why he looked at me like that.{/i}"
            pause 0.6
            a "{i}Like he remembered something I forgot...{/i}"
            pause 0.8
            a "{i}Something from before I became this.{/i}"
            pause 0.9
            jump act1_daren_flashback
    # ------------------------------------------------------

    if check_scene_flag(_current_scene_id, "acknowledge_daren"):
        # VISUAL: Ambient reset — golden wash, camera resumes slow glide.
        "{i}The music resumes like it never stopped. Conversations blur back into motion.{/i}"
        pause 0.7
        a "{i}The past is always closer than I think.{/i}"
        pause 0.7
        a "{i}Even now, I see him. Not Daren today—Daren then. When we still thought this meant something.{/i}"
        pause 0.9

    # VISUAL: Overhead drone—live feeds rotate; Aeron's face flickers on a screen.
    a "{i}Even here, there's no room without a camera.{/i}"
    pause 0.6
    a "{i}Every movement measured. Every breath filed away.{/i}"
    pause 0.8

    # REVISED: Elite whispers — definitive block
    "{i}Nearby, whispers slide beneath the music — rehearsed, polite, just loud enough.{/i}"
    pause 0.7
    e1 "...Marcus Rylan's son. Glass."
    pause 0.5
    e2 "390 operations. Zero failures. No margin for error."
    pause 0.6
    e3 "They say he doesn’t even flinch anymore. Doesn’t feel the kills."
    pause 0.6
    e1 "Is that strength... or vacancy?"
    pause 0.6
    e2 "Ask his father. That’s the point."
    pause 0.8

    # BRANCHING — Aeron's internal response by tier (OB3..EMP3) + momentum spice
    $ tier = get_alignment_tier()
    $ mom  = get_alignment_momentum()  # -1..+1 (recent push)

    if tier in ("OB3","OB2"):
        a "{i}Let them think I don’t hear. Let them wonder what kind of machine watches them back.{/i}"
        pause 0.7
        if mom <= -0.5:
            a "{i}Their fear is a tool. I keep it sharp.{/i}"
        else:
            a "{i}Their fear is useful. Fear doesn’t ask questions.{/i}"
        pause 0.8

    elif tier in ("OB1","C"):
        a "{i}Even their fear feels rehearsed. Like everything else in this place.{/i}"
        pause 0.7
        a "{i}They don’t know whether to admire or avoid me. Maybe both.{/i}"
        pause 0.8

    else:  # EMP1/EMP2/EMP3
        a "{i}Even their fear feels rehearsed. Like everything else in this place.{/i}"
        pause 0.7
        if mom >= 0.5:
            a "{i}They want a myth. I can’t unsee the people behind it.{/i}"
        else:
            a "{i}They want a myth. I keep giving them the cracks instead.{/i}"
        pause 0.8

    # VISUAL: Marcus entrance—ceremonial armor; Enforcers flank; room tension rises.
    "{i}General Marcus Rylan steps into the light—armor flawless, formation exact.{/i}"
    pause 0.7
    "{i}The room exhales. Every conversation pauses. Every eye tracks.{/i}"
    pause 0.7
    a "{i}The gravity tilts when he arrives. No applause—just fear dressed as respect.{/i}"
    pause 0.8
    a "{i}He doesn’t need announcements. The silence does it for him.{/i}"
    pause 0.8

    # BRANCHING — Marcus’s reaction to Aeron (tiers + momentum)
    if tier in ("OB3","OB2"):
        a "{i}His gaze finds mine—for the briefest second. A subtle nod. Approval measured in microseconds.{/i}"
        pause 0.8
        if mom <= -0.5:
            a "{i}He sees the edge he honed and knows I kept it sharp.{/i}"
        else:
            a "{i}He’s read the reports. Sector 7. The body count. No hesitation noted.{/i}"
        pause 0.8
        a "{i}This is what he wanted. Precision. Purity. Obedience.{/i}"
        pause 0.8
        $ set_scene_flag(_current_scene_id, "marcus_approval")

    elif tier in ("OB1","C"):
        a "{i}His gaze meets mine, unreadable. A flicker—approval, or warning?{/i}"
        pause 0.8
        a "{i}Hard to tell anymore. Harder to care.{/i}"
        pause 0.8
        $ set_scene_flag(_current_scene_id, "marcus_uncertain")

    else:  # EMP1/EMP2/EMP3
        a "{i}His eyes sweep past mine. No pause. No nod. Just calculation.{/i}"
        pause 0.8
        if mom >= 0.5:
            a "{i}He’s seen the hesitation. He’ll call it deviation. I call it breathing.{/i}"
        else:
            a "{i}He’s read the report. Saw the hesitation. The deviation from protocol.{/i}"
        pause 0.8
        a "{i}This isn’t what he trained me for.{/i}"
        pause 0.8
        $ set_scene_flag(_current_scene_id, "marcus_disapproval")

    # VISUAL: Lyra across the hall with a Councilwoman—composed, precise, unmissable.
    "{i}Across the hall, Lyra stands with a Councilwoman—composed, precise, unmissable.{/i}"
    pause 0.7
    a "{i}They parade her like proof the system still works.{/i}"
    pause 0.6
    a "{i}Another perfect soldier. Another polished surface.{/i}"
    pause 0.6
    a "{i}I wonder if she's as empty as I am.{/i}"
    pause 0.8

    "{i}Her eyes flick to Aeron for a heartbeat—then back.{/i}"
    pause 0.6

    # --- PLAYER CHOICE: acknowledge Lyra or not ---
    menu:
        "Lyra's eyes meet yours for a heartbeat."
        "Acknowledge her.":
            $ apply_choice_once(
                _current_scene_id, "_ack_lyra", "EMP", factor=1,
                next_scene_label="act1_05_gala",
                note="Micro-acknowledgment; tests willingness for connection under surveillance."
            )
            # affection only if clearly EMP side (>= EMP_EDGE)
            if pass_emp_gate():
                $ add_affection("Lyra", 1)
            $ set_scene_flag(_current_scene_id, "acknowledge_lyra")
            a "{i}I nod—barely. Memory, not invitation.{/i}"
            pause 0.7
            a "{i}The space between us tightens. Just for a second.{/i}"
            pause 0.8

        "Look away.":
            $ apply_choice_once(
                _current_scene_id, "_ignore_lyra", "OB", factor=1,
                next_scene_label="act1_06_balcony",
                note="Maintains performance seal; avoids signaling under optics."
            )
            $ set_scene_flag(_current_scene_id, "ignored_lyra")
            a "{i}I let the moment pass. Safer that way.{/i}"
            pause 0.7
            a "{i}Eyes forward. No room for ghosts tonight.{/i}"
            pause 0.8
    # ----------------------------------------------

    # BRANCHING THOUGHT BASED ON EMPATHY (slight positive vs not)
    $ norm = get_alignment_score_norm()   # -1.0 .. +1.0
    if norm > 0.0:
        a "{i}She sees it. Not the medals. Not the posture. The strain.{/i}"
        pause 0.7
        a "{i}Maybe she remembers what I was before the edges hardened.{/i}"
        pause 0.8
    else:
        a "{i}She sees exactly what they built. And doesn’t flinch.{/i}"
        pause 0.7
        a "{i}No pity. No softness. Just recognition.{/i}"
        pause 0.8

    # REVISED: Younger elites nearby - fear/fascination with Glass
    ye1 "I heard he's done nearly 400 operations."
    pause 0.5
    ye2 "In seven years? That's impossible."
    pause 0.5
    ye1 "Not impossible. Just... inhuman."
    pause 0.6
    ye3 "Father tried to make him a believer. Made Glass instead."
    pause 0.6
    ye2 "Glass?"
    pause 0.5
    ye3 "Transparent. Empty. Sharp when you need it."
    pause 0.6
    ye1 "(quietly) Has Glass ever broken?"
    pause 0.6
    ye3 "Not yet. But they say cracks are forming."
    pause 0.6
    ye2 "How can you tell if something empty is breaking?"
    pause 0.6
    ye3 "You can't. Until it shatters."
    pause 0.8

    a "{i}They're not wrong.{/i}"
    pause 0.6
    a "{i}Cracks are forming. Last night, I felt one spread.{/i}"
    pause 0.8
    a "{i}'Who taught me that word?' Mercy.{/i}"
    pause 0.8
    a "{i}Glass doesn't ask questions. But I did.{/i}"
    pause 0.9

    a "{i}They laugh like the world belongs to them.{/i}"
    pause 0.7
    a "{i}And I'm expected to smile like I believe it.{/i}"
    pause 0.7
    # NEW: What changed
    a "{i}Six hours ago, I executed four people without hesitation.{/i}"
    pause 0.8
    a "{i}Now I'm here, holding wine, making small talk.{/i}"
    pause 0.7
    a "{i}This is what Glass does. Transitions seamlessly.{/i}"
    pause 0.8
    a "{i}...So why does it feel different tonight?{/i}"
    pause 0.9

    # --- PLAYER CHOICE: Approach Lyra or Keep Distance ---
    menu:
        "Across the room, Lyra is momentarily alone."
        "Cross the floor toward her.":
            $ apply_choice_once(
                _current_scene_id, "_approach_lyra", "EMP", factor=1,
                next_scene_label="act1_06_balcony",
                note="Chooses connection under optics; seeds balcony rendezvous."
            )
            $ set_scene_flag(_current_scene_id, "approach_lyra")
            "{i}He threads through silk and medals, closing the distance.{/i}"
            pause 0.7

            # VISUAL: Councilwoman lingers, then steps aside.
            a "Lyra."
            pause 0.6
            "{i}She pivots, posture precise, eyes reading him in a single beat.{/i}"
            pause 0.7

            l "You are on time."
            pause 0.6
            a "{i}Her voice is steady. But her eyes aren't.{/i}"
            pause 0.7
            a "{i}How long since she slept? Days? Weeks?{/i}"
            pause 0.8

            $ norm = get_alignment_score_norm()
            $ band = get_empathy_band()  # "obedience" | "conflicted" | "empathy"

            if norm >= 0.17:  # ~ >= +2 on a ±12 scale
                a "Funny. I still remember the lines. Doesn’t mean I believe them."
                pause 0.7
                l "Belief was never required. Only performance."
                pause 0.7
                a "You’ve heard the stories."
                pause 0.6
                l "Everyone has. But stories change in retelling."
                pause 0.8
            elif band == "obedience":  # ≤ -3
                a "On time is the same as willing."
                pause 0.7
                l "That's what they say. And what they need."
                pause 0.7
                a "And you?"
                pause 0.6
                l "I don't need belief. I need results."
                pause 0.8
            else:
                a "On time, not exactly willing."
                pause 0.7
                l "Willingness was never part of the design."
                pause 0.7
                a "(half-smile) I’m starting to notice."
                pause 0.8

            "{i}A council attaché leans in with a whisper. Lyra’s attention splits—only for a moment.{/i}"
            pause 0.7

            l "The balcony. Five minutes."
            pause 0.6
            a "I’ll be there."
            pause 0.6
            l "(softer) We will see if Glass still reflects."
            pause 0.9

            "{i}She’s gone before the room notices she moved.{/i}"
            pause 0.7

            a "{i}She sees it—what I am, what she is. Maybe that’s why she wants to talk.{/i}"
            pause 0.8
            $ set_scene_flag(_current_scene_id, "balcony_meet_set")

        "Keep your distance.":
            $ apply_choice_once(
                _current_scene_id, "_keep_distance", "OB", factor=1,
                next_scene_label="act1_05_gala",
                note="Avoids connection; preserves performance shell."
            )
            "{i}He holds position. The moment passes.{/i}"
            pause 0.7

            a "{i}Glass doesn’t need connection. Glass functions alone.{/i}"
            pause 0.7
            a "{i}...So why does that feel wrong tonight?{/i}"
            pause 0.9
            #$ set_scene_flag(_current_scene_id, "kept_distance")
    # ----------------------------------------------

    # --- TRANSITION TO BALCONY SEQUENCE ---
    "{i}The crowd shifts again. Music fades. The air feels thinner now—like the room knows something’s about to fracture.{/i}"
    pause 0.8
    "{i}The doors open. Cold air rushes in.{/i}"
    pause 0.8

    a "{i}Time to stop performing. Time to breathe.{/i}"
    pause

    # ========= QA HOOK =========
    #$ telemetry(_current_scene_id, gates_met=True)
    return


# ========= CANONICAL NOTES (grep-able block) =========
# cann.scene_id: act1_05_gala
# cann.when_in_timeline: Act I, immediately after Hallway; before Balcony rendezvous.
# cann.what_happened:
#   - Aeron enters the Gala; luxury as performative warmth over institutional cold.
#   - Daren (Academy peer) encounter establishes public myth vs private cost.
#   - Elite/Young-elite whisper blocks codify “Glass” reverence/fear; 390 ops timeline reinforced.
#   - Marcus entrance calibrates father/son power optics (approval/uncertain/disapproval by tier).
#   - Lyra sightline; player can acknowledge/ignore; later choose to approach or keep distance.
#   - Balcony meeting can be set if approach path chosen (flag).
# cann.aeron_state: OB-lean baseline; branch-local warmth on EMP choices.
# cann.path_tracking:
#   - Scene deltas via standardized API:
#       • Daren choice: OB (cold courtesy) vs EMP (acknowledge) → ±1 weight ×1.
#       • Lyra glance: OB (look away) vs EMP (acknowledge) → ±1 weight ×1 (affection if EMP gate passes).
#       • Approach Lyra: EMP (approach) vs OB (keep distance) → ±1 weight ×1.
#   - Rolling empathy range by end of scene (given prior [-10, +6]): ≈ [-11, +8].
#   - Momentum hooks: `get_alignment_momentum()` consulted for micro-variant lines.
# cann.thematic_flags:
#   - Motifs: Glass / Performance / Reflection / Ceremony-as-constraint / Surveillance optics.
#   - Recurring lines seeded/echo potential: “Time to perform.” “Glass still reflects.”
#   - Stigma: No-Band vs Band talisman (Daren touch) mirrored against medals/record.
# cann.block_status: ANCHOR (fixed interior flow) with VARIANT beats (Daren/Lyra/Marcus responses).
# cann.true_path_integration:
#   - +1 at tag: a1.gala.daren_ack (only on EMP variant that names the pretense: “Pretend we’re still who we were.”).
#   - No TP on Lyra glance or approach; reserve stronger TP for Balcony acceptance/memory beats.
# cann.visual_plate_economy:
#   - REUSE: Wide master of ballroom with lighting passes (warm chandelier vs colder perimeter); crop/push for whispers.
#   - REUSE: Marcus entrance plate with different crowd masks (approval/neutral/disapproval variants reuse same base).
#   - HERO: Lyra micro-CU with chandelier bokeh; Aeron silhouette against holo-feed reflection.
# cann.requires_followup:
#   - If `balcony_meet_set` → load Balcony scene (suggest `act1_06_balcony`) after short breath beat.
#   - Persist flags on save: acknowledge_daren, marcus_{approval|uncertain|disapproval}, acknowledge_lyra/ignored_lyra, approach_lyra/kept_distance, balcony_meet_set.
# cann.consistency_asserts:
#   - Lyra Act I diction: formal, minimal contractions.
#   - Aeries lighting grammar: gala “warmth” is performative, not genuine; keep camera language restrained until Balcony.
