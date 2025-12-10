# ===================================================
# ACT 1 - Scene 4: Hallway to the Gala
# File: act1_04_hallway.rpy
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_04_hallway"
$ scene_mark(_current_scene_id, "entered")

define servant = Character("Attendant")


label act1_04_hallway:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: 38mm lens, shoulder-high tracking left→right; slow, stabilized glide.
    #         Occasional 2–3% push on emphasis lines; avoid frontal close-ups until portrait beat.
    # LIGHTING: White-gold top light (4:1 key/fill), marble bounce; specular highlights on floor rings.
    #           Warmer 3000K bleed from gala doors at far end; cool 5200K hallway wash.
    # SFX LOOP: Distant chamber strings + soft conversation bed (-18 LUFS).
    # SFX ONE-SHOTS: Heel clicks, glass clinks, door hinge sigh.
    # FX/COMP: Subtle reflection cards on marble; micro-bloom on sconces; screen-space dust motes.
    # BLOCKING: Officials in hushed trios; portrait wall; floor sigil rings; tray of glasses.
    # CANON: Aeries is above cloud layer—no rain language. Use hush/pressure/sterility.
    # FACE: Keep Aeron partial (jaw, hands, wrist, silhouette) until the portrait beat.

    # ========= OPENING — THE RUNWAY =========

    athought "The hallway runs like a runway—each polished tile a reminder of who I'm supposed to be."

    # VISUAL: Officials in quiet clusters; smiles rehearsed, eyes measuring.
    # CAMERA: Slow glide past faces; none hold eye contact.

    athought "Their eyes trace edges, not faces—judging the outline, never the person."

    athought "They see something they don't understand, and that makes them nervous."

    # ========= FLOOR SIGIL =========
    # VISUAL: Floor tiles form concentric circles radiating outward—Echelon sigil stamped into marble.
    # SYMBOL: The path is predetermined. Step outside, and the system corrects you.

    "The floor tiles form rings within rings—the Echelon sigil stamped into the earth itself, radiating outward like frozen ripples."

    pause 0.6

    athought "Walk the path. Stay in your circle. Step outside, and the system corrects you."

    # ========= ARCHITECTURE — SWALLOWING SOUND =========
    # VISUAL: Vaulted ceiling; light fixtures descend like judging eyes.
    # SOUND: Footsteps thin out, absorbed by the space.

    "The ceiling arches so high it swallows sound—every footstep dies before it escapes, thinned by distant strings and polite laughter."

    pause 0.7

    # ========= WRIST STIGMA =========
    # VISUAL: Insert—his bare wrist catches the light. No Band.
    # CAMERA: Tight on wrist, then pull back to show others noticing.

    athought "No Band, no worth—that's the first thing they see."

    athought "Then they see the uniform, the medals, the record. And they look away even faster."

    # ========= SERVANT ENCOUNTER =========
    # VISUAL: An older attendant approaches with a tray; pauses at Aeron.
    # BLOCKING: The man's posture is deferential but his eyes are searching.

    servant "(quietly) Master Aeron."

    # VISUAL: The man's eyes flicker—recognition, then something softer. Old grief.

    a "(stops) Do I know you?"

    servant "I served your family for sixteen years, sir. I was there the night your brother..."

    "The sentence dies in his throat. The silence finishes it."

    pause 0.9

    # VISUAL: Aeron's jaw tightens; the man notices, lowers his gaze.

    servant "(softer) He spoke of you often. Said you'd be the one to change things."

    athought "Change what? The world? Or just his mind about leaving it?"

    a "(carefully) He said a lot of things."

    servant "That he did, sir."

    # ========= SERVANT SEES THE CHANGE =========
    # VISUAL: The man's eyes linger on Aeron's face—searching for something familiar.
    # NOTE: This is the first time someone from Aeron's past confronts what he's become.

    servant "(quieter) I watched you become... this."

    a "Become what?"

    servant "Efficient, sir. Like your father wanted."

    servant "(barely audible) Your brother never became... what you are. I'm not sure there was ever anything else left in you."

    # VISUAL: The man adjusts the tray, prepares to move on. A small bow—genuine.

    servant "For what it's worth... I hope you find what he was looking for."

    "The bow is small but genuine. Then he continues down the hall, footsteps fading into chamber music."

    pause 0.7

    athought "What he was looking for? He was looking for the edge of a roof. And he found it."

    # ========= STAFF REACTIONS =========
    # VISUAL: Butler steps aside, gaze fixed on floor. Deference or fear—hard to tell.

    athought "Obedient in public. Honest in silence."

    # VISUAL: Another elite passes—eyes flick wrist→face→away. Quick, involuntary.

    "Another glance. This one lingers on the medals, then recoils as if burned."

    pause 0.6

    athought "They know what I've done, what I'm capable of. And they don't want to be seen looking too long."

    # ========= PLAYER CHOICE — WRIST =========
    # NOTE: Micro-weight choice. Concealment = performance/OB. Exposure = self-acceptance/EMP.

    menu:
        athought "My wrist catches the light—naked, unmarked. A dozen eyes pretend not to see."

        "Cover it.":
            $ choice_and_dev(
                _current_scene_id, "_cover_wrist", "OB", factor=1,
                next_scene_label="act1_05_gala",
                note="Performs conformity to reduce scrutiny; self-erasure coping."
            )

            athought "An old reflex, as if fabric could fix the silence."

            athought "Let them think I belong. Let them stop wondering."

        "Let it show.":
            $ choice_and_dev(
                _current_scene_id, "_bare_wrist", "EMP", factor=1,
                next_scene_label="act1_05_gala",
                note="Accepts stigma without concealment; micro-assertion of self vs performance."
            )

            #$ adjust_true_path_resonance_once("a1.hallway.wrist_show", 1)

            athought "No Band. No need to lie about it."

            athought "Let them feel uneasy. Let them remember what this uniform really means."

    # ========= PORTRAIT GALLERY =========
    # VISUAL: Portraits of Aeries elites—immaculate propaganda, eyes that seem to follow.
    # CAMERA: Lateral drift along the wall; paintings loom.

    "Portraits line the walls—heroes painted to outlast their mistakes, their failures erased by oil and canvas."

    pause 0.7

    # ========= MARCUS PORTRAIT =========
    # CAMERA: Lateral drift stops; Aeron's silhouette eclipses half of Marcus's painted face.
    # VISUAL: The composition should feel confrontational—son obscuring father.
    # NOTE: This is a potential marketing shot. Worth a hero render.

    athought "Marcus Rylan. Hero, legend, father—depends who you ask."

    "The portrait doesn't look back. It never does."

    pause 0.7

    athought "He trained me well. Too well, maybe."

    athought "I can kill without hesitation, lead without doubt, obey without question—everything he wanted. Everything but faith."

    athought "All function, no soul. Just enough to pass for human. And that makes me his greatest failure."

    # ========= ELITE WHISPERS =========
    # VISUAL: Two elites whisper as he passes—light catches mirrored glasses.
    # SOUND: Voices drop, fragments audible.

    "Voices drop as he approaches. Not mockery—something else. Wariness, maybe. Or fascination."

    "Fragments carry:"

    "\"...Marcus Rylan's son...\""
    "\"...390 operations, zero failures...\""
    "\"...technically perfect, but have you seen his eyes?\""
    "\"...nothing behind them...\""

    pause 0.8

    athought "They're not wrong. I don't feel, I don't question—I just cut."

    "The whispers fade as he passes. Relief in their silence."

    pause 0.7

    # ========= THRESHOLD — GALA DOORS =========
    # VISUAL: End doors glow—warm light spilling into the cold hall; guards motionless at either side.
    # LIGHTING: Sharp contrast between cold hallway wash and warm amber bleeding through the gap.

    "At the far end, twin doors leak warm light into the cold hall—amber against sterile white."

    pause 0.7

    # VISUAL: Aeron pauses. Hand hovers near the doorframe but doesn't touch.
    # SYMBOL: Threshold hesitation. The choice to enter is also a choice to perform.

    athought "I could turn around, slip into the dark. Would anyone stop me? Would anyone care?"

    pause 0.5

    athought "There is no retreat. Only forward."

    "The hesitation passes. The choice was already made before he reached the door."

    pause 0.7

    athought "I show up when I'm told. That's what I'm built for."

    # ========= DOORS OPEN =========
    # VISUAL: Doors swing inward; gold light floods the frame. Sound swells—strings, voices, clinking crystal.
    # CAMERA: Hold on Aeron's back as light washes over him.
    # SOUND: Conversation swell, then cut to controlled ambience for player agency.

    "Hinges sigh. Light and voices flood the marble hush."

    pause 0.8

    athought "Time to smile, time to lie, time to perform."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_04_hallway
# cann.when_in_timeline: Act I, immediately pre-Gala entry; before Balcony scene.
# cann.what_happened:
#   - Aeron traverses Aeries ceremonial corridor toward the Gala under elite scrutiny.
#   - Attendant (former family servant) acknowledges Kael and frames Aeron as "efficient."
#   - Wrist stigma beat → player chooses concealment (performance) or exposure (self-acceptance).
#   - Marcus portrait confrontation reframes Aeron as his father's product without faith.
#   - Elites whisper fear/respect: 390 ops, zero failures; dehumanization subtext.
#   - Aeron commits to enter (performance), not retreat.
# cann.aeron_state: OB-lean baseline; micro-variance by wrist choice (EMP warmth if bare).
# cann.path_tracking: Empathy range by this point ≈ [-4, +4]. Wrist choice adds ±1.
# cann.thematic_flags:
#   - Motifs: Performance / Reflection / Circle-path (sigil rings) / Father-efficiency.
#   - Recurring lines: "Time to perform." / "There is no retreat. Only forward."
#   - Identity stigma (No Band) vs earned terror (medals/record) seeded for Act I–II payoffs.
# cann.block_status: ANCHOR (fixed route to Gala doors); requires followup scene load.
# cann.true_path_integration:
#   - +1 at tag: a1.hallway.wrist_show (only if player chooses "Let it show.").
#   - Hidden; no UI exposure.
# cann.visual_plate_economy:
#   - REUSE: Base Aeries corridor plate; vary push-in %, specular intensity, portrait crop.
#   - REUSE: Door end-plate with two lighting passes (cold hall vs warm spill) + overlayed motes.
#   - HERO: Marcus portrait half-eclipsed by Aeron silhouette (unique render; marketing shot).
# cann.requires_followup:
#   - Next scene: act1_05_gala (Balcony/Gala entry).
#   - Log servant cameo for potential Act II mirror encounter (Unders relief line about Kael).