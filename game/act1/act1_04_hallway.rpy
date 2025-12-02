# ===================================================
# ACT 1 - Scene 4: Hallway to the Gala
# File: act1_04_hallway.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_04_hallway"
$ scene_mark(_current_scene_id, "entered")

define servant = Character("Attendant")


label act1_04_hallway:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 38mm lens (OB baseline), shoulder-high tracking left→right; slow, stabilized glide.
    #         Occasional 2–3% push on emphasis lines; avoid frontal close-ups early.
    # LIGHTING: White-gold top light (4:1 key/fill), marble bounce; specular on floor rings.
    #           Warmer 3000K bleed from gala doors at the far end; cool 5200K hallway wash.
    # SFX: Loop — distant chamber strings + soft conversation bed (-18 LUFS).
    #      One-shots — heel clicks, glass clinks, door hinge sigh.
    #      Diegetic comms filter (band-limited 300–3kHz) reserved for later scenes; not used here.
    # FX/COMP: Subtle reflection cards on marble; micro-bloom on sconces; screen-space dust motes.
    # BLOCKING/PROPS: Officials in hushed trios; portrait wall; floor sigil rings; tray of glasses.
    # CANON: Aeries is above the cloud layer — no rain-on-glass language; use hush/pressure/sterility.
    # FACE: Keep Aeron’s face off-screen / partial (jaw, hands, wrist, silhouette) until the portrait beat.

    # ========= VOICE BASELINE =========
    # Baseline cadence: OB-lean (clipped/procedural). If player state shifts EMP later, localized warmth only.

    athought "The hallway runs like a runway—each polished tile a reminder of who I'm supposed to be."

    # VISUAL: Officials in quiet clusters; smiles rehearsed, eyes measuring. CAMERA: slow glide past faces.
    athought "Their eyes trace edges, not faces. Judging the outline, never the person."

    # NEW: Glass makes them uncomfortable
    athought "They see something they don’t understand. And that makes them nervous."

    # VISUAL: Floor tiles—concentric circles radiating from the center, like ripples frozen in stone.
    "The floor tiles form rings within rings—the Echelon sigil stamped into the earth itself."
    pause 0.6

    athought "Walk the path. Stay in your circle. Step outside, and the system corrects you."

    # VISUAL: Vaulted ceiling; light fixtures descend like judging eyes.
    "The ceiling arches overhead, so high it swallows sound. Every footstep dies before it escapes."
    pause 0.7

    "Footsteps carry down the length of the hall, thinned by distant strings and laughter."
    pause 0.7

    # VISUAL: Insert — his bare wrist catches light. No Band.
    athought "No Band, no worth. That's the first thing they see."

    # NEW: But not the only thing
    athought "Then they see the uniform. The medals. The record."
    athought "And they look away even faster."

    # VISUAL: An older attendant approaches with a tray; pauses at Aeron.
    servant "(quietly) Master Aeron."

    # VISUAL: The man's eyes flicker—recognition, then something softer.
    a "(stops) Do I know you?"
    servant "I served your family for sixteen years, sir. I was there the night your brother..."

    "He trails off. The silence finishes the sentence."
    pause 0.9

    # VISUAL: Aeron's jaw tightens; the man notices, lowers his gaze.
    servant "(softer) He spoke of you often. Said you'd be the one to change things."
    athought "Change what? The world? Or just his mind about leaving it?"
    a "(carefully) He said a lot of things."
    servant "That he did, sir."

    # NEW: Servant sees the change
    # VISUAL: The man's eyes linger on Aeron's face—searching for something.
    servant "(quieter) I watched you become... this."
    a "Become what?"
    servant "Efficient, sir. Like your father wanted."
    servant "(barely audible) Your brother never became Glass. You... I'm not sure there was ever anything else left."

    # VISUAL: The man adjusts the tray, prepares to move on.
    servant "For what it's worth... I hope you find what he was looking for."

    # VISUAL: He bows—genuine; continues down the hall.
    "His footsteps fade into the chamber music."
    pause 0.7

    athought "What he was looking for? He was looking for the edge of a roof."
    athought "And he found it."

    # VISUAL: Staff reaction — butler steps aside, gaze to floor.
    athought "Obedient in public. Honest in silence."

    # VISUAL: Another elite passes—eyes flick wrist→face→away.
    "Another glance. This one lingers on the medals, then recoils."
    pause 0.6

    athought "They know what I’ve done. What I’m capable of."
    athought "And they don’t want to be seen looking too long."

    # ========= CHOICE (standardized API; psychologically ambiguous) =========
    menu:
        "His wrist catches the light — naked, unmarked. A dozen eyes pretend not to see."
        "Cover it.":
            $ choice_and_dev(
                _current_scene_id, "_cover_wrist", "OB", factor=1,
                next_scene_label="act1_05_gala",
                note="Performs conformity to reduce scrutiny; self-erasure coping, not belief… yet."
            )

            athought "An old reflex. As if fabric could fix the silence."
            athought "Let them think I belong. Let them stop wondering."

        "Let it show.":
            $ choice_and_dev(
                _current_scene_id, "_bare_wrist", "EMP", factor=1,
                next_scene_label="act1_05_gala",
                note="Accepts stigma without concealment; micro-assertion of self vs performance."
            )

            # Hidden True Path increment: unrepressed self-acceptance
            #$ adjust_true_path_resonance_once("a1.hallway.wrist_show", 1)
            athought "No Band. No need to lie about it."
            athought "Let them feel uneasy. Let them remember what this uniform really means."

    # VISUAL: Portraits of Aeries elites — immaculate propaganda, eyes following.
    "Portraits line the walls—heroes painted to outlast their mistakes."
    pause 0.7

    # Marcus portrait with Glass reference
    # CAMERA: Lateral drift; Aeron’s silhouette eclipses half the face.
    athought "Marcus Rylan. Hero, legend, father. Depends who you ask."

    "The portrait doesn't look back. It never does."
    pause 0.7

    athought "He trained me well. Too well, maybe."
    athought "I can kill without hesitation. Lead without doubt. Obey without question."
    athought "Everything he wanted. Everything but faith."
    athought "All function, no soul. Just enough to pass for human."
    athought "And that makes me his greatest failure."

    # VISUAL: Two elites whisper as he passes—light catches mirrored glasses.
    "Voices drop as he approaches. Not mockery. Something else."
    "He catches fragments:"

    "\"...Marcus Rylan's son. Glass.\""
    "\"...390 operations. Zero failures.\""
    "\"...technically perfect, but have you seen his eyes?\""
    "\"...nothing behind them...\""
    pause 0.8

    athought "They're not wrong."
    athought "I don’t feel. I don’t question."
    athought "I just cut."

    "The whispers fade as he passes. Relief in their silence."
    pause 0.7

    # VISUAL: End doors glow—warm light spilling into the cold hall; guards motionless.
    "At the far end, twin doors leak warm light into the cold hall."
    pause 0.7

    # Threshold hesitation with physicality; hand hovers near frame.
    athought "I could turn around. Slip into the dark."
    athought "Would anyone stop me? Would anyone care?"

    # But Glass doesn't retreat
    "His hand drops. The choice was already made."
    pause 0.7

    athought "No. Not tonight."
    athought "I show up when I’m told. That’s what I’m built for."

    # Doors open—gold light floods; sound swells, then cut to silence to hand control to player.
    "Hinges sigh. Light and voices flood the marble hush."
    pause 0.8

    athought "Time to smile. Time to lie. Time to perform."

    #$ telemetry(_current_scene_id, gates_met=True)
    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_04_hallway
# cann.when_in_timeline: Act I, immediately pre-Gala entry; before Balcony scene.
# cann.what_happened:
#   - Aeron traverses Aeries ceremonial corridor toward the Gala under elite scrutiny.
#   - Attendant (former family servant) acknowledges Kael and frames Aeron as “becoming Glass.”
#   - Wrist stigma beat → player chooses concealment (performance) or exposure (self-acceptance).
#   - Marcus portrait confrontation reframes Aeron as his father’s “efficient” product without faith.
#   - Elites whisper fear/respect: “Glass,” 390 ops, zero failures; dehumanization subtext.
#   - Aeron commits to enter (performance), not retreat.
# cann.aeron_state: OB-lean baseline; micro-variance by wrist choice (EMP warmth if bare).
# cann.path_tracking: Empathy range by this point ≈ [-10, +6] (weights ×1). Wrist choice adds ±1 if your backend uses explicit deltas; otherwise logged via apply_choice_once.
# cann.thematic_flags:
#   - Motifs: Glass / Performance / Reflection / Circle-path (sigil rings) / Father-efficiency.
#   - Recurring lines usable later: “Time to perform.” “Glass doesn’t retreat.” (echo or subvert).
#   - Identity stigma (No Band) vs earned terror (medals/record) seeded for Act I–II payoffs.
# cann.block_status: ANCHOR (fixed route to Gala doors); requires followup scene load.
# cann.true_path_integration:
#   - +1 at tag: a1.hallway.wrist_show (only if player chooses “Let it show.”).
#   - Hidden; no UI exposure. Stored in solveil["meta"]["true_path_resonance"] by helper.
# cann.visual_plate_economy:
#   - REUSE: Base Aeries corridor plate; vary push-in %, specular intensity, and portrait crop.
#   - REUSE: Door end-plate with two lighting passes (cold hall vs warm spill) + overlayed motes.
#   - HERO: Marcus portrait half-eclipsed by Aeron silhouette (unique render worth it; marketing shot).
# cann.requires_followup:
#   - Next scene: Balcony/Gala entry (suggest label: act1_05_balcony). Ingest aeron_hides_wrist for flavor lines with Lyra/Zira later.
#   - Log servant cameo for potential Act II mirror encounter (Unders relief line about Kael).