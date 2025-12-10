# =======================================================
# ACT 1 – Scene 6: Balcony
# File: act1_06_balcony.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_06_balcony"
$ scene_mark(_current_scene_id, "entered")


label act1_06_balcony:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: 35mm shoulder-high, static with 2–3% breathing push on vulnerable lines; avoid frontal CU until mid-scene.
    # LIGHTING: Cooler exterior (4800K moonwash) vs interior warmth spill; 3:1 key/fill; rim off skyline neon; micro-spec on rail.
    # SFX LOOP: High-altitude wind shear + distant city hum.
    # SFX ONE-SHOTS: Lighter flick, ash tap.
    # FX/COMP: Low cloud-halo far below; condensation bead on stone; faint breath plumes; soft bloom on distant signage.
    # BLOCKING: Stone rail, lighter, ash tray, balcony doors cracked behind (warm spill).
    # CANON: Aeries is above cloud layer—no rain language. Use wind/pressure/condensation.
    # FACE: Keep partial profile until "the leash" exchange; then allow fuller eyeline.

    # ========= OPENING — THE VIEW =========
    # VISUAL: Neon-lit skyline beyond the rail; high wind skims the parapet; condensation gathers on stone.

    "The city's glow cuts hard lines across the stone, neon bleeding into the haze below."

    pause 0.7

    if pass_tier("OB2", "OB3"):
        athought "They look down at the Unders like another species. Maybe they're right."
        athought "I don't care about altitude—I just reflect orders."
    elif pass_tier("OB1", "NEU"):
        athought "They look down at the Unders like another species. Still human, all of us."
        athought "I mirror whoever's watching. That's all."
    else:
        athought "They look down at the Unders like another species. Still human, all of us—even the ones pretending not to be."
        athought "I catch their reflection and give it back, cracked but still human."

    # ========= LYRA ARRIVES =========
    # VISUAL: Lyra steps through the door, silhouette against warm interior light.
    # CAMERA: She moves to the rail; he doesn't turn immediately.

    l "Got a light?"

    a "(wry) I didn't think Echelon's exemplar smoked."

    l "(a faint smile) If you know a better way to breathe in there, I'm listening."

    a "You said we should compare cracks. Are you ready to show me yours?"

    l "Are you ready to show me yours?"

    a "(beat) Maybe we start with smaller truths first."

    # ========= MICRO-CHOICE: SHARE THE LIGHT =========
    # VISUAL: Lyra steps in close, waiting for the flame.
    # NOTE: Intimacy distance test. No empathy weight—just flavor and flag.

    menu:
        athought "Lyra steps in close, waiting for the flame."

        "Lean in and light it for her.":
            $ record_choice_once(_current_scene_id, "_shared_light")
            $ scene_mark(_current_scene_id, "shared_light")

            "The flame wavers between them—close enough to feel her breath, the faint scent of something floral beneath the smoke."

            pause 0.7

            if pass_tier("EMP2", "EMP3"):
                athought "Close enough to see the cracks—and the warmth leaking through them."
            elif pass_tier("OB2", "OB3"):
                athought "Too close. Distance blurred. I shouldn't allow that."
            else:
                athought "Close enough to see reflection, not truth."

        "Offer the lighter and step back.":
            $ record_choice_once(_current_scene_id, "_offer_light")

            "The lighter changes hands. Distance holds."

            pause 0.7

            if pass_tier("OB2", "OB3"):
                athought "I don't touch. I maintain form."
            elif pass_tier("EMP2", "EMP3"):
                athought "Even distance has weight when you want to close it."
            else:
                athought "Space feels safe, familiar—but not right."

    # ========= MICRO-CHOICE: HOLD GAZE =========
    # VISUAL: For a breath, she remains close. Eyes meeting.

    menu:
        athought "For a breath, she remains close."

        "Hold her gaze.":
            $ record_choice_once(_current_scene_id, "_held_gaze")
            $ scene_mark(_current_scene_id, "held_gaze")

            if pass_tier("OB2", "OB3"):
                athought "Observation, not connection. I catalog her expression—nothing more."
            elif pass_tier("EMP2", "EMP3"):
                athought "The world falls away. Just her eyes and the reflection inside them."
            else:
                athought "Color on smoke. For once, no audience."
                athought "She's not looking at the uniform. She's looking for what's left underneath."

        "Look past her to the city.":
            $ record_choice_once(_current_scene_id, "_look_past")

            athought "The skyline answers for me—easier to look at light than at someone who might actually see."

    # ========= SMALL TALK — CONDITIONAL ON GALA CHOICE =========

    if scene_has("act1_05_gala", "approach_lyra"):
        l "You didn't keep me waiting."
        a "You said five."

        if pass_tier("EMP2", "EMP3"):
            a "(softer) I wasn't about to miss this."
            l "(faint smile) Crossing the floor like that—bold, considering the room."
            a "Why be subtle in a place built to be seen?"
            l "Fair point. Though subtlety was never your strength."
        elif pass_tier("OB2", "OB3"):
            l "Crossing the floor like that—brave, for someone under orders."
            a "Orders said twenty-two hundred sharp."
            l "And you've never missed one."
            a "Not a habit I plan to start."
        else:
            l "Crossing the floor like that—bold, considering the room."
            a "Bold or stupid?"
            l "Maybe both."
            athought "Her tone almost sounds human again."
    else:
        l "You skipped the introductions."
        a "Crowd wasn't my scene."
        l "It never is. Ceremony performs. You endure."
        a "You seem to know a lot about endurance."
        l "I recognize my own reflection."

    # ========= QUIET BEAT AT THE RAIL =========
    # VISUAL: They stand at the rail; city noise folds over itself below.
    # CAMERA: Two silhouettes against the skyline. Intimate distance.

    "Wind curls around the parapet, carrying the distant hum of the city below."

    pause 0.8

    if not scene_has("act1_05_gala", "approach_lyra"):
        l "I didn't expect to find you out here."
        a "I didn't expect you to leave a spotlight unattended. Shouldn't you be inside, charming anyone with a title?"
    else:
        a "Shouldn't you be inside charming anyone with a title instead of talking to me?"

    l "(soft) Please. I'd rather jump."

    a "(half-smile) Careful. They might call that sedition."

    # ========= PERFORMANCE DISCUSSION =========
    # NOTE: This is where Lyra names the performance theme directly.

    l "Take away the performance and there's not much left."

    athought "Her voice drops—not the formal Lyra, something underneath."

    a "You've done it your whole life."

    l "Since I could walk. That doesn't mean I'm blind."

    l "They call me the system's proof—polished, perfect, pristine."

    l "I call it being a window. People look right through you to see the power behind."

    a "So you know."

    l "Of course I know. Windows recognize windows."

    a "Then tell me—what do you see now?"

    l "(studies him) A room drunk on power it barely understands. People who'll do anything to feed a machine that eats the rest."

    l "And one person out here—pretending he's forgotten how to care."

    l "(softer) But the pretending's getting harder, isn't it?"

    if pass_tier("OB2", "OB3"):
        a "(quiet) Pretending keeps the system stable."
    elif pass_tier("EMP2", "EMP3"):
        a "(quiet) Maybe I'm tired of pretending."
    else:
        a "(quiet) Pretending's easier than remembering."

    pause 0.9

    l "I hear the rumors, and I know they're far from the truth."

    l "They say you're perfect, empty, that you don't feel."

    a "And?"

    l "And I think you're lying to yourself."

    # ========= HISTORY REFLECTION =========

    a "They've been whispering since I was twelve."

    a "Used to be about failure—the Branding, the son who couldn't."

    a "Now it's about the soldier who does. 390 operations, zero failures."

    a "Not sure which whispers are worse."

    l "Let them. Fear's loud when it's small."

    a "They just respect my father. I'm just a rumor—an heir to a name that doesn't fit."

    athought "Rylan. Heavy word, hollow sound."

    # ========= MICRO-CHOICE: ASH GESTURE =========
    # VISUAL: The ember brightens at the tip of his cigarette.
    # SYMBOL: What you do with the residue—discard or contain.

    menu:
        athought "The ember brightens at the tip."

        "Flick ash over the rail.":
            $ record_choice_once(_current_scene_id, "_ash_flick")
            $ scene_mark(_current_scene_id, "ash_flick")

            "Ash falls and vanishes into neon—swallowed by the haze before it reaches the clouds."

            pause 0.7

            if pass_tier("EMP2", "EMP3"):
                athought "Let it fall. Maybe some things deserve to land where light can't reach."
            elif pass_tier("OB2", "OB3"):
                athought "Disposal complete. Out of sight, out of system."
            else:
                athought "Let it fall. Easier than holding on."

        "Tap ash into the tray.":
            $ record_choice_once(_current_scene_id, "_ash_tray")

            "The tray's edge catches the ember—contained, controlled."

            pause 0.7

            if pass_tier("OB2", "OB3"):
                athought "Controlled, contained—like everything else."
            elif pass_tier("EMP2", "EMP3"):
                athought "Still controlling. Less certain why."
            else:
                athought "Routine gesture. Keeps the silence steady."

    # ========= TRUTH AND LEASH =========

    a "Why are you really out here?"

    l "Because in a room full of polish, you're the only one not pretending."

    a "I'm always pretending. That's all I am—pretense shaped into a person."

    l "No. That's what they made you pretend to be."

    l "The person asking that question is the one I came to see."

    "Smoke curls between them, carried sideways by the wind."

    pause 0.8

    a "How long are you back from assignment?"

    l "Not long. High value means high surveillance. They let me breathe when it's useful."

    a "And tonight?"

    l "Parade duty. Proof the machine still works."

    l "They parade me, they parade you—two perfect soldiers, except neither of us believes a word of it anymore."

    a "They think everything belongs to them."

    a "The dark tells the truth."

    a "And you—you don't belong to anyone."

    "Neither of them steps away."

    pause 0.7

    athought "The city hums below. Up here, the silence is louder."

    athought "Two people leaning close enough to touch, wondering if contact will shatter both."

    l "(quiet) Always so serious. And here I thought I was the dramatic one."

    # ========= MICRO-CHOICE: PRESS OR BREATHE =========

    menu:
        athought "Say nothing—or press."

        "Press her about the leash she's on.":
            $ record_choice_once(_current_scene_id, "_press_leash")
            $ scene_mark(_current_scene_id, "pressed_topic")

            a "Who holds the leash tonight—Council or Command?"

            l "(a beat) Does it matter, if they pull the same direction?"

            athought "She looks away, jaw tight, breath unsteady. She's not deflecting—she's drowning."

            a "It matters if you're the one being pulled."

            l "(studies him) And what about you? Who pulls your leash?"

            a "Father. Always Father."

            l "Then we're both dogs on strings, wondering if cutting them means freedom or falling."

        "Let the moment breathe.":
            $ record_choice_once(_current_scene_id, "_let_breathe")

            if pass_tier("OB2", "OB3"):
                athought "Questions disrupt function. Silence keeps form."
            elif pass_tier("EMP2", "EMP3"):
                athought "I let the question stay between us. Some truths deserve air, not pressure."
            else:
                athought "I leave the question where it belongs—in the smoke."

    "Two faint sparks hang in the night—then dim with the wind."

    pause 0.8

    # ========= VULNERABILITY BEAT =========
    # CAMERA: Fuller eyeline now. This is the emotional core.

    l "(quietly) Do you ever wonder what we'd be without the uniforms?"

    a "Every night."

    l "And?"

    a "I don't have an answer. Just questions I'm not supposed to ask."

    l "Then maybe you're already breaking."

    a "(looks at her) Is that what you want? For me to break?"

    l "I want you to remember what it feels like to be whole—even if that means shattering first."

    # ========= CLOSING EMOTIONAL BEAT =========
    # VISUAL: The city below, two figures on the rail, smoke dissipating.
    # CAMERA: Hold wide. Let the moment land.

    "For a moment, the world feels smaller—just two people, smoke and silence."

    pause 0.9

    if pass_tier("OB2", "OB3"):
        athought "Six hours ago, I executed four liabilities. Nothing personal."
        athought "Yet standing here, something personal tries to surface. I push it down."
    elif pass_tier("EMP2", "EMP3"):
        athought "Six hours ago, I killed four people. The echo still vibrates in my chest."
        athought "And for the first time, I let it hurt."
    else:
        athought "Six hours ago, I killed four people. The thought keeps returning like a pulse I can't ignore."
        athought "Standing here, I finally feel its weight."

    athought "Maybe that's what she means. Maybe feeling it is how you break."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_06_balcony
# cann.when_in_timeline: Act I immediately after Gala; pre-Bridge path-lock era.
# cann.what_happened:
#   - Aeron and Lyra meet in honest air (cool palette vs warm gala).
#   - Micro-choices modulate intimacy (shared_light, held_gaze), control (ash tray), and care (let_breathe vs press).
#   - Lyra frames performance theme; Aeron edges toward admitting fatigue with pretense.
#   - Empathy-acceptance language appears in VO ("tired of pretending," "let it hurt") but choices remain flavor.
# cann.aeron_state: Branch by tier — OB-hard suppresses; mid acknowledges; EMP admits feeling.
# cann.path_tracking:
#   - Scene deltas: All NEU (no empathy/obedience weight in this scene by design).
#   - Flags set: shared_light, held_gaze, ash_flick, pressed_topic (depending on choices).
# cann.thematic_flags:
#   - Motifs: Performance vs Honesty; Altitude & Pressure; Reflection.
#   - Recurring line echoes: "Maybe I'm tired of pretending."
#   - Weather grammar: Aeries above cloud-deck — wind/pressure/condensation only, no rain.
# cann.block_status: VARIANT-heavy ANCHOR (routes based on flags).
# cann.visual_plate_economy:
#   - REUSE: Single balcony master with door open/closed passes; push/crop for intimacy beats.
#   - REUSE: Skyline plate with adjustable haze; optional breath-plume overlay.
#   - HERO: Eye-line CU at "Maybe I'm tired of pretending." (marketing still).
# cann.requires_followup:
#   - If held_gaze OR EMP-lean language → unlock warmer variant next.
#   - Else → route to neutral corridor return.
# cann.consistency_asserts:
#   - Lyra diction: formal/melodic; contractions acceptable in low-formality private space.
#   - Enforce altitude/weather rules; no precip terms at this height.