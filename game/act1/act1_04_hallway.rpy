# ===================================================
# ACT 1 - Scene 4: Hallway to the Gala
# File: act1_04_hallway.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_04_hallway"
$ scene_mark(_current_scene_id, "entered")   # log entry for telemetry & path math

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

    a "{i}The hallway runs like a runway—each polished tile a reminder of who I'm supposed to be.{/i}"
    pause 0.6

    # VISUAL: Officials in quiet clusters; smiles rehearsed, eyes measuring. CAMERA: slow glide past faces.
    a "{i}Their eyes trace edges, not faces. Judging the outline, never the person.{/i}"
    pause 0.6
    # NEW: Glass makes them uncomfortable
    a "{i}They see something they don’t understand. And that makes them nervous.{/i}"
    pause 0.8

    # VISUAL: Floor tiles—concentric circles radiating from the center, like ripples frozen in stone.
    "{i}The floor tiles form rings within rings—the Echelon sigil stamped into the earth itself.{/i}"
    pause 0.6
    a "{i}Walk the path. Stay in your circle. Step outside, and the system corrects you.{/i}"
    pause 0.9

    # VISUAL: Vaulted ceiling; light fixtures descend like judging eyes.
    "{i}The ceiling arches overhead, so high it swallows sound. Every footstep dies before it escapes.{/i}"
    pause 0.7
    "{i}Footsteps carry down the length of the hall, thinned by distant strings and laughter.{/i}"
    pause 0.7

    # VISUAL: Insert — his bare wrist catches light. No Band.
    a "{i}No Band, no worth. That's the first thing they see.{/i}"
    pause 0.6
    # NEW: But not the only thing
    a "{i}Then they see the uniform. The medals. The record.{/i}"
    pause 0.6
    a "{i}And they look away even faster.{/i}"
    pause 0.8

    # VISUAL: An older attendant approaches with a tray; pauses at Aeron.
    servant "(quietly) Master Aeron."
    pause 0.6
    # VISUAL: The man's eyes flicker—recognition, then something softer.
    a "(stops) Do I know you?"
    pause 0.6
    servant "I served your family for sixteen years, sir. I was there the night your brother..."
    pause 0.8
    "{i}He trails off. The silence finishes the sentence.{/i}"
    pause 0.9

    # VISUAL: Aeron's jaw tightens; the man notices, lowers his gaze.
    servant "(softer) He spoke of you often. Said you'd be the one to change things."
    pause 0.8
    a "{i}Change what? The world? Or just his mind about leaving it?{/i}"
    pause 0.9
    a "(carefully) He said a lot of things."
    pause 0.6
    servant "That he did, sir."
    pause 0.6

    # NEW: Servant sees the change
    # VISUAL: The man's eyes linger on Aeron's face—searching for something.
    servant "(quieter) I watched you become... this."
    pause 0.7
    a "Become what?"
    pause 0.6
    servant "Efficient, sir. Like your father wanted."
    pause 0.9
    servant "(barely audible) Your brother never became Glass. You... I'm not sure there was ever anything else left."
    pause 1.0

    # VISUAL: The man adjusts the tray, prepares to move on.
    servant "For what it's worth... I hope you find what he was looking for."
    pause 0.8
    # VISUAL: He bows—genuine; continues down the hall.
    "{i}His footsteps fade into the chamber music.{/i}"
    pause 0.7

    a "{i}What he was looking for? He was looking for the edge of a roof.{/i}"
    pause 0.9
    a "{i}And he found it.{/i}"
    pause 0.9

    # VISUAL: Staff reaction — butler steps aside, gaze to floor.
    a "{i}Obedient in public. Honest in silence.{/i}"
    pause 0.8

    # VISUAL: Another elite passes—eyes flick wrist→face→away.
    "{i}Another glance. This one lingers on the medals, then recoils.{/i}"
    pause 0.6
    a "{i}They know what I’ve done. What I’m capable of.{/i}"
    pause 0.8
    a "{i}And they don’t want to be seen looking too long.{/i}"
    pause 0.8

    # ========= CHOICE (standardized API; psychologically ambiguous) =========
    menu:
        "His wrist catches the light — naked, unmarked. A dozen eyes pretend not to see."
        "Cover it.":
            $ apply_choice_once(
                _current_scene_id, "_cover_wrist", "OB", factor=1,
                next_scene_label="act1_05_gala",
                note="Performs conformity to reduce scrutiny; self-erasure coping, not belief… yet."
            )
            a "{i}An old reflex. As if fabric could fix the silence.{/i}"
            pause 0.7
            a "{i}Let them think I belong. Let them stop wondering.{/i}"
            pause 0.8

        "Let it show.":
            $ apply_choice_once(
                _current_scene_id, "_bare_wrist", "EMP", factor=1,
                next_scene_label="act1_05_gala",
                note="Accepts stigma without concealment; micro-assertion of self vs performance."
            )
            # Hidden True Path increment: unrepressed self-acceptance
            #$ adjust_true_path_resonance_once("a1.hallway.wrist_show", 1)
            a "{i}No Band. No need to lie about it.{/i}"
            pause 0.7
            a "{i}Let them feel uneasy. Let them remember what this uniform really means.{/i}"
            pause 0.9

    # VISUAL: Portraits of Aeries elites — immaculate propaganda, eyes following.
    "{i}Portraits line the walls—heroes painted to outlast their mistakes.{/i}"
    pause 0.7

    # Marcus portrait with Glass reference
    # CAMERA: Lateral drift; Aeron’s silhouette eclipses half the face.
    a "{i}Marcus Rylan. Hero, legend, father. Depends who you ask.{/i}"
    pause 0.8
    "{i}The portrait doesn't look back. It never does.{/i}"
    pause 0.7
    a "{i}He trained me well. Too well, maybe.{/i}"
    pause 0.7
    a "{i}I can kill without hesitation. Lead without doubt. Obey without question.{/i}"
    pause 0.8
    a "{i}Everything he wanted. Everything but faith.{/i}"
    pause 0.7
    a "{i}All function, no soul. Just enough to pass for human.{/i}"
    pause 0.8
    a "{i}And that makes me his greatest failure.{/i}"
    pause 1.0

    # VISUAL: Two elites whisper as he passes—light catches mirrored glasses.
    "{i}Voices drop as he approaches. Not mockery. Something else.{/i}"
    pause 0.7
    "{i}He catches fragments:{/i}"
    pause 0.5
    "{i}\"...Marcus Rylan's son. Glass.\"{/i}"
    pause 0.6
    "{i}\"...390 operations. Zero failures.\"{/i}"
    pause 0.6
    "{i}\"...technically perfect, but have you seen his eyes?\"{/i}"
    pause 0.6
    "{i}\"...nothing behind them...\"{/i}"
    pause 0.8

    a "{i}They're not wrong.{/i}"
    pause 0.7
    a "{i}I don’t feel. I don’t question.{/i}"
    pause 0.7
    a "{i}I just cut.{/i}"
    pause 0.9

    "{i}The whispers fade as he passes. Relief in their silence.{/i}"
    pause 0.7

    # VISUAL: End doors glow—warm light spilling into the cold hall; guards motionless.
    "{i}At the far end, twin doors leak warm light into the cold hall.{/i}"
    pause 0.7

    # Threshold hesitation with physicality; hand hovers near frame.
    a "{i}I could turn around. Slip into the dark.{/i}"
    pause 0.9
    a "{i}Would anyone stop me? Would anyone care?{/i}"
    pause 1.0

    # But Glass doesn't retreat
    "{i}His hand drops. The choice was already made.{/i}"
    pause 0.7
    a "{i}No. Not tonight.{/i}"
    pause 0.8
    a "{i}I show up when I’m told. That’s what I’m built for.{/i}"
    pause 0.9

    # Doors open—gold light floods; sound swells, then cut to silence to hand control to player.
    "{i}Hinges sigh. Light and voices flood the marble hush.{/i}"
    pause 0.8
    a "{i}Time to smile. Time to lie. Time to perform.{/i}"
    pause

    # ========= QA HOOK =========
    #$ telemetry(_current_scene_id, gates_met=True)

    return


# ========= CANONICAL NOTES (grep-able block) =========
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