# ===================================================
# ACT 1 - Scene 5: The Gala
# File: act1_05_gala.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_05_gala"
$ scene_mark(_current_scene_id, "entered")

define e1 = Character("Elite 1")
define e2 = Character("Elite 2")
define e3 = Character("Elite 3")
define ye1 = Character("Young Elite 1")
define ye2 = Character("Young Elite 2")
define ye3 = Character("Young Elite 3")
define cadet = Character("Daren")


label act1_05_gala:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: 35–38mm stabilized glide; gentle 3% push on stress beats; avoid frontal CU of Aeron until Marcus entrance.
    # LIGHTING: Performative warmth (3000K chandeliers) over cold marble base (5200K bounce); 3:1 key/fill; soft rim from sconces.
    # SFX LOOP: Strings + low conversation bed (-18 LUFS).
    # SFX ONE-SHOTS: Glass clinks, soft heel clicks, hinge sighs.
    # FX/COMP: Subtle specular blooms, reflection cards on floor, floating dust motes; no rain (Aeries above cloud deck).
    # BLOCKING: Chandelier cluster, portrait wall spill, holo-feeds rotating above bar, Council attachés orbiting.
    # FACE: Keep Aeron's face partial/obscured in early beats; full reveal on Marcus pass.

    # ========= OPENING — THE BALLROOM =========
    # VISUAL: Lavish gold wash over marble; chandeliers; strings under low conversation.

    "The ballroom breathes manufactured warmth—chandeliers dripping crystal, velvet swallowing footsteps, the cloying sweetness of curated luxury."

    pause 0.7

    athought "All this gold to smooth over the cracks, plaster over decay with opulence."

    athought "Six hours ago, I killed four people in Sector 7. Now I'm here—smiling, composed, as if blood rinses off that easily."

    athought "But that's what they want. No conflict, no conscience, just seamless transition."

    # ========= SENSORY OVERLOAD =========
    # VISUAL: The ballroom swells—music crescendos, voices layer, chandeliers pulse with reflected motion.

    "The air thickens with perfume, wine, polished metal—too much of everything pressing in at once."

    pause 0.7

    athought "Every surface reflects, every sound echoes—no silence, no stillness, just performance layered on performance."

    # ========= INTERNAL CRACK =========
    # NOTE: First subtle sign that the routine is slipping.

    athought "This is protocol: eyes ahead, breath steady, form intact."

    athought "Still, something in the rhythm skips—half a heartbeat off. No one would notice. But I do."

    athought "And cracks never start loud."

    # ========= DAREN ENCOUNTER =========
    # VISUAL: A young man in full ceremonial dress approaches—confident stride, silver Band glinting.
    # BLOCKING: He's nervous but hiding it. The Band on his wrist catches chandelier light.

    cadet "Aeron Rylan. Thought that was you."

    # VISUAL: Aeron steadies; tunnel vision clears.

    a "(turns) Daren."

    # VISUAL: Handshake; Band catches chandelier light—he touches it like a talisman.

    cadet "Been a while. Not since the Academy, right?"

    a "Something like that."

    cadet "(glances at medals, impressed) Heard about your last operation. Sector Nine?"

    a "(neutral) Sector 7. This morning."

    cadet "(surprised) This morning? And you're here tonight?"

    a "Recovery's for people who feel it."

    cadet "(nervous laugh) Cold. They really call you that?"

    a "They do."

    "The respect is there in his posture—but so is the fear. He admires the record while dreading the person behind it."

    pause 0.7

    cadet "Look, I just wanted to say... your record is insane. 390 operations, zero failures?"

    a "(neutral) Metrics don't lie."

    cadet "That's... that's impossible. In seven years?"

    a "Not impossible. Just inhuman."

    cadet "(uncomfortable) I didn't mean—"

    a "You did. And you're right."

    "His hand drifts to his Band—touching it like a talisman, proof he belongs, proof he's safe. Proof he's not like me."

    pause 0.7

    cadet "Your father must be... proud."

    a "He has expectations. I meet them."

    cadet "That's... that's all any of us can do, right?"

    a "(looks at him directly) Is it?"

    "For a moment, something passes between them—not quite understanding, just distance made visible."

    pause 0.8

    # ========= PLAYER CHOICE — DAREN RESPONSE =========

    menu:
        athought "Daren's smile wavers."

        "Respond with cold courtesy.":
            $ choice_and_dev(
                _current_scene_id, "_daren_cold_courtesy", "OB", factor=1,
                next_scene_label="act1_06_balcony",
                note="Reasserts performance persona; reinforces fear/respect myth."
            )

            a "Enjoy the gala, Daren."

            # VISUAL: Aeron turns away; Daren's smile collapses into relief.

            cadet "Yeah. You too. Stay... stay sharp."

            "He retreats into the crowd, grateful for the exit."

            pause 0.7

            athought "He'll tell that story tomorrow—'Didn't flinch, didn't blink.' Let him."

        "Acknowledge the awkwardness.":
            $ choice_and_dev(
                _current_scene_id, "_daren_acknowledge", "EMP", factor=1,
                next_scene_label="act1_06_balcony",
                note="Permits vulnerability without breaking form; micro-connection."
            )
            $ scene_mark(_current_scene_id, "acknowledge_daren")

            if pass_tier("EMP1", "EMP2", "EMP3"):
                a "You don't have to do this."
                cadet "(confused) Do what?"
                a "(softer) Pretend we're still who we were. We're not."
            else:
                a "You don't have to pretend. We're not friends anymore."

            cadet "(pause) …No. I guess we're not."

            "For a moment, something real passes between them—fragile, brief, almost painful."

            pause 0.8

            cadet "(quieter) Take care of yourself, Aeron. If you still can."

            a "I'll try."

            athought "He walks away. Not relieved—just sad. He sees what I've become."

            athought "Maybe that's why he looked at me like that, like he remembered something I forgot. Something from before I became this."

            jump act1_daren_flashback

    # ========= POST-DAREN AMBIENT =========

    if scene_has(_current_scene_id, "acknowledge_daren"):
        # VISUAL: Ambient reset—golden wash, camera resumes slow glide.

        "The music resumes like it never stopped. Conversations blur back into motion."

        pause 0.7

        athought "The past is always closer than I think. Even now, I see him—not Daren today, Daren then, when we still thought this meant something."

    # ========= SURVEILLANCE =========
    # VISUAL: Overhead drone—live feeds rotate; Aeron's face flickers on a screen.

    athought "Even here, there's no room without a camera. Every movement measured, every breath filed away."

    # ========= ELITE WHISPERS =========
    # VISUAL: Nearby elites in conversation—voices drop just low enough to pretend they're private.

    "Nearby, whispers slide beneath the music—rehearsed, polite, just loud enough."

    pause 0.7

    e1 "...Marcus Rylan's son."
    e2 "390 operations. Zero failures. No margin for error."
    e3 "They say he doesn't even flinch anymore—doesn't feel the kills."
    e1 "Is that strength... or vacancy?"
    e2 "Ask his father. That's the point."

    # ========= BRANCHING — INTERNAL RESPONSE =========

    if pass_tier("OB2", "OB3"):
        athought "Let them think I don't hear. Let them wonder what kind of weapon watches them back."
        athought "Their fear is useful. Fear doesn't ask questions."
    elif pass_tier("OB1", "NEU"):
        athought "Even their fear feels rehearsed, like everything else in this place."
        athought "They don't know whether to admire or avoid me. Maybe both."
    else:
        athought "Even their fear feels rehearsed, like everything else in this place."
        athought "They want a myth. I keep giving them the cracks instead."

    # ========= MARCUS ENTRANCE =========
    # VISUAL: Marcus entrance—ceremonial armor; Enforcers flank; room tension rises.
    # CAMERA: Wide shot of the room pivoting toward the entrance. Everyone notices.

    "General Marcus Rylan steps into the light—armor flawless, formation exact, presence absolute."

    pause 0.7

    "The room exhales. Every conversation pauses. Every eye tracks."

    pause 0.7

    athought "The gravity tilts when he arrives—no applause, just fear dressed as respect. He doesn't need announcements. The silence does it for him."

    # ========= BRANCHING — MARCUS'S REACTION =========

    if pass_tier("OB2", "OB3"):
        athought "His gaze finds mine for the briefest second—a subtle nod, approval measured in microseconds."
        athought "He's read the reports: Sector 7, the body count, no hesitation noted."
        athought "This is what he wanted—precision, purity, obedience."
        $ scene_mark(_current_scene_id, "marcus_approval")

    elif pass_tier("OB1", "NEU"):
        athought "His gaze meets mine, unreadable—a flicker that could be approval or warning. Hard to tell anymore. Harder to care."
        $ scene_mark(_current_scene_id, "marcus_uncertain")

    else:
        athought "His eyes sweep past mine—no pause, no nod, just calculation."
        athought "He's read the report, saw the hesitation, the deviation from protocol."
        athought "This isn't what he trained me for."
        $ scene_mark(_current_scene_id, "marcus_disapproval")

    # ========= LYRA SIGHTING =========
    # VISUAL: Lyra across the hall with a Councilwoman—composed, precise, unmissable.
    # CAMERA: Mid-shot; chandelier bokeh; her posture is perfect but her eyes are tired.

    "Across the hall, Lyra stands with a Councilwoman—composed, precise, unmissable."

    pause 0.7

    athought "They parade her like proof the system still works. Another perfect soldier, another polished surface."

    athought "I wonder if she's as empty as I am."

    "Her eyes flick to Aeron for a heartbeat—then back, deliberate, controlled."

    pause 0.6

    # ========= PLAYER CHOICE — ACKNOWLEDGE LYRA =========

    menu:
        athought "Lyra's eyes meet mine for a heartbeat."

        "Acknowledge her.":
            $ choice_and_dev(
                _current_scene_id, "_ack_lyra", "EMP", factor=1,
                next_scene_label="act1_06_balcony",
                note="Micro-acknowledgment; tests willingness for connection under surveillance."
            )
            if pass_emp():
                $ rel_bump("Lyra", affection=1)
            $ scene_mark(_current_scene_id, "acknowledge_lyra")

            athought "I nod—barely. Memory, not invitation."

            athought "The space between us tightens, just for a second."

        "Look away.":
            $ choice_and_dev(
                _current_scene_id, "_ignore_lyra", "OB", factor=1,
                next_scene_label="act1_06_balcony",
                note="Maintains performance seal; avoids signaling under optics."
            )
            $ scene_mark(_current_scene_id, "ignored_lyra")

            athought "I let the moment pass. Safer that way—eyes forward, no room for ghosts tonight."

    # ========= BRANCHING — LYRA READ =========

    if pass_emp():
        athought "She sees it—not the medals, not the posture, the strain."
        athought "Maybe she remembers what I was before the edges hardened."
    else:
        athought "She sees exactly what they built and doesn't flinch. No pity, no softness—just recognition."

    # ========= YOUNGER ELITES — NASTIER VERSION =========
    # VISUAL: Three younger elites nearby—polished, privileged, whispering like it's sport.
    # NOTE: This should feel like cruelty dressed as curiosity.

    ye1 "I heard he's done nearly 400 operations."
    ye2 "In seven years? That's impossible."
    ye1 "Not impossible. Just inhuman."
    ye3 "They say Rylan stripped the belief right out of him. Now there's nothing left but the edge."
    ye2 "The edge?"
    ye3 "Cold, efficient—cuts when you need it."
    ye1 "(quietly) Has he ever failed?"
    ye3 "Not yet. But they say he's starting to hesitate."
    ye2 "How can you tell if something that cold is breaking?"
    ye3 "You can't. Not until it turns on you."

    athought "They're not wrong."

    athought "Cracks are forming. Last night, I felt one spread—'Mercy. The definition is slipping.'"

    athought "Weapons don't ask questions. But I did."

    athought "They laugh like the world belongs to them, and I'm expected to smile like I believe it."

    # ========= TRANSITION DISSONANCE =========

    athought "Six hours ago, I executed four people without hesitation. Now I'm holding wine, making small talk."

    athought "This is what I'm built for—seamless transitions. So why does it feel different tonight?"

    # ========= PLAYER CHOICE — APPROACH LYRA =========
    # VISUAL: Lyra momentarily alone as the Councilwoman steps away.

    menu:
        athought "Across the room, Lyra is momentarily alone."

        "Cross the floor toward her.":
            $ choice_and_dev(
                _current_scene_id, "_approach_lyra", "EMP", factor=1,
                next_scene_label="act1_06_balcony",
                note="Chooses connection under optics; seeds balcony rendezvous."
            )
            $ scene_mark(_current_scene_id, "approach_lyra")

            "The crowd parts around him—silk and medals, perfume and wariness—as he closes the distance."

            pause 0.7

            # VISUAL: Councilwoman lingers, then steps aside. Lyra pivots to face him.

            a "Lyra."

            "She pivots, posture precise, eyes reading him in a single beat."

            pause 0.7

            l "Precise. I calculated you would approach within three minutes."

            athought "Her voice is steady, but her eyes aren't. How long since she slept? Days? Weeks?"

            if pass_tier("EMP2", "EMP3"):
                a "Funny. I still remember the lines. Doesn't mean I believe them."
                l "Belief was never required. Only performance."
                a "You've heard the stories."
                l "Everyone has. But stories change in retelling."
            elif empathy_band() == "obedience":
                a "On time is the same as willing."
                l "That's what they say. And what they need."
                a "And you?"
                l "I don't need belief. I need results."
            else:
                a "On time, not exactly willing."
                l "Willingness was never part of the design."
                a "(half-smile) I'm starting to notice."

            "A council attaché leans in with a whisper. Lyra's attention splits—only for a moment."

            pause 0.7

            l "The balcony. Five minutes."

            a "I'll be there."

            l "(softer) I want to see what's behind the uniform."

            "She's gone before the room notices she moved."

            pause 0.7

            athought "She sees it—what I am, what she is. Maybe that's why she wants to talk."

            $ scene_mark(_current_scene_id, "balcony_meet_set")

        "Keep your distance.":
            $ choice_and_dev(
                _current_scene_id, "_keep_distance", "OB", factor=1,
                next_scene_label="act1_06_balcony",
                note="Avoids connection; preserves performance shell."
            )

            "The moment passes. The distance stays."

            pause 0.7

            athought "I don't need connection. I function alone."

            athought "...So why does that feel wrong tonight?"

    # ========= TRANSITION TO BALCONY =========
    # VISUAL: The crowd shifts. Music fades. Cold air bleeds in from somewhere.

    "The crowd shifts again—music fading, conversations thinning. The air feels lighter now, like the room knows something's about to fracture."

    pause 0.8

    "Somewhere, doors open. Cold air rushes in."

    pause 0.8

    athought "Time to stop performing. Time to breathe."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_05_gala
# cann.when_in_timeline: Act I, immediately after Hallway; before Balcony rendezvous.
# cann.what_happened:
#   - Aeron enters the Gala; luxury as performative warmth over institutional cold.
#   - Daren (Academy peer) encounter establishes public myth vs private cost.
#   - Elite/Young-elite whisper blocks codify reverence/fear; 390 ops timeline reinforced.
#   - Marcus entrance calibrates father/son power optics (approval/uncertain/disapproval by tier).
#   - Lyra sightline; player can acknowledge/ignore; later choose to approach or keep distance.
#   - Balcony meeting can be set if approach path chosen (flag).
# cann.aeron_state: OB-lean baseline; branch-local warmth on EMP choices.
# cann.path_tracking:
#   - Scene deltas via standardized API:
#       • Daren choice: OB (cold courtesy) vs EMP (acknowledge) → ±1 weight ×1.
#       • Lyra glance: OB (look away) vs EMP (acknowledge) → ±1 weight ×1 (affection if EMP gate passes).
#       • Approach Lyra: EMP (approach) vs OB (keep distance) → ±1 weight ×1.
#   - Rolling empathy range by end of scene: ≈ [-7, +7].
# cann.thematic_flags:
#   - Motifs: Performance / Reflection / Ceremony-as-constraint / Surveillance optics.
#   - Recurring lines seeded: "Time to perform." / "Seamless transitions."
#   - Stigma: No-Band vs Band talisman (Daren touch) mirrored against medals/record.
# cann.block_status: ANCHOR (fixed interior flow) with VARIANT beats (Daren/Lyra/Marcus responses).
# cann.true_path_integration:
#   - +1 at tag: a1.gala.daren_ack (only on EMP variant that names the pretense).
# cann.visual_plate_economy:
#   - REUSE: Wide master of ballroom with lighting passes; crop/push for whispers.
#   - REUSE: Marcus entrance plate with different crowd masks.
#   - HERO: Lyra micro-CU with chandelier bokeh; Aeron silhouette against holo-feed reflection.
# cann.requires_followup:
#   - If `balcony_meet_set` → load act1_06_balcony after short breath beat.
#   - Persist flags: acknowledge_daren, marcus_{approval|uncertain|disapproval}, acknowledge_lyra/ignored_lyra, approach_lyra/kept_distance, balcony_meet_set.
# cann.consistency_asserts:
#   - Lyra Act I diction: formal, minimal contractions.
#   - Aeries lighting grammar: gala "warmth" is performative, not genuine.