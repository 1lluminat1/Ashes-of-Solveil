# =======================================================
# ACT 1 – Scene 6: Balcony
# File: act1_06_balcony.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_06_balcony"
$ scene_mark(_current_scene_id, "entered")


label act1_06_balcony:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm shoulder-high, static with 2–3% breathing push on vulnerable lines; avoid frontal CU until mid-scene.
    # LIGHTING: Cooler exterior (4800K moonwash) vs interior warmth spill; 3:1 key/fill; rim off skyline neon; micro-spec on rail.
    # SFX: Loop — high-altitude wind shear + distant city hum; one-shots — lighter flick, ash tap; no rain (Aeries above cloud deck).
    # FX/COMP: Low cloud-halo far below; condensation bead on stone; faint breath plumes; soft bloom on distant signage.
    # BLOCKING/PROPS: Stone rail, lighter, ash tray, balcony doors cracked behind (warm spill).
    # FACE: Keep partial profile until “the leash” exchange; then allow fuller eyeline on “Maybe I’m tired of pretending.”

    # ========= ALIGNMENT SNAPSHOT (precompute once) =========
    $ tier = get_alignment_tier()           # OB3, OB2, OB1, C, EMP1, EMP2, EMP3
    $ band = get_empathy_band()             # "obedience" | "conflicted" | "empathy"
    $ norm = get_alignment_score_norm()     # -1.0 .. +1.0 (≈ +0.17 ~ +2 on ±12 scale)
    $ mom  = get_alignment_momentum()       # -1 .. +1 recent push

    # Convenience buckets matching original thresholds
    $ is_ob_hard = pass_tier("OB3","OB2")           # ≈ score <= -4
    $ is_mid     = pass_tier("OB1","C")             # ≈ -3 .. +1
    $ is_emp     = pass_tier("EMP1","EMP2","EMP3")  # ≈ >= +2

    # VISUAL: Neon-lit skyline beyond the rail; high wind skims the parapet; condensation gathers on stone.
    "The city's glow cuts hard lines across the stone."
    pause 0.7

    if is_ob_hard:
        athought "They look down at the Unders like another species. Maybe they’re right."
        athought "Glass doesn’t care about altitude. Glass just reflects orders."
    elif is_mid:
        athought "They look down at the Unders like another species. Still human. All of us."
        athought "Glass doesn’t care about altitude. It only mirrors whoever’s watching."
    else:  # empathy
        athought "They look down at the Unders like another species. Still human. All of us — even the ones pretending not to be."
        athought "Glass catches their reflection and gives it back. Cracked, but still human."

    # --- LYRA ARRIVES ---
    l "Got a light?"
    a "(wry) I didn’t think Echelon’s exemplar smoked."
    l "(a faint smile) If you know a better way to breathe in there, I’m listening."
    a "Glass and glass. You said we should compare cracks."
    l "I did. Are you ready to show me yours?"
    a "Are you ready to show me yours?"
    l "(pause) Maybe we start with smaller truths first."

    # --- MICRO-CHOICE: share the light (intimacy distance) ---
    menu:
        "Lyra steps in close, waiting for the flame."
        "Lean in and light it for her.":
            $ record_choice_once(
                _current_scene_id, "_shared_light",
                next_scene_label="act1_07_bedroom",
                note="Closes distance under optics; permits momentary intimacy."
            )
            $ set_scene_flag(_current_scene_id, "shared_light")

            "He lifts the flame. She leans in; her eyes don’t leave his."
            pause 0.7

            if norm >= 0.17:  # ~ >= +2
                athought "Close enough to see the cracks — and the warmth leaking through them."
            elif is_ob_hard:
                athought "Too close. Distance blurred. Glass doesn’t allow that."
            else:
                athought "Close enough to see reflection, not truth."

        "Offer the lighter and step back.":
            $ record_choice_once(
                _current_scene_id, "_offer_light",
                next_scene_label="act1_07_bedroom",
                note="Maintains distance; preserves performance shell."
            )

            "He hands her the lighter. Distance holds."
            pause 0.7

            if is_ob_hard:
                athought "Glass doesn’t touch. Glass maintains form."
            elif norm >= 0.17:
                athought "Even distance has weight when you want to close it."
            else:
                athought "Space feels safe. Familiar. But not right."

    # --- OPTIONAL GAZE BEAT ---
    menu:
        "For a breath, she remains close."
        "Hold her gaze.":
            $ record_choice_once(
                _current_scene_id, "_held_gaze",
                next_scene_label="act1_07_bedroom",
                note="Accepts connection without mask; sustained eye contact."
            )
            $ set_scene_flag(_current_scene_id, "held_gaze")

            if is_ob_hard:
                athought "Observation, not connection. I catalog her expression — nothing more."
            elif is_mid:
                athought "Color on smoke. For once, no audience."
                athought "She’s not looking at Glass. She’s looking for what’s left underneath."
            else:
                athought "The world falls away. Just her eyes and the reflection inside them."

        "Look past her to the city.":
            $ record_choice_once(
                _current_scene_id, "_look_past",
                next_scene_label="act1_07_bedroom",
                note="Deflects intimacy; re-centers on environment."
            )

            athought "The skyline answers for me. Easier to look at light than at someone who might actually see."

    # --- SMALL TALK VARIANTS ---
    if check_scene_flag("act1_05_gala", "approach_lyra"):
        l "You didn’t keep me waiting."
        a "You said five."
        if norm >= 0.17:
            a "(softer) I wasn’t about to miss this."
            l "(faint smile) Crossing the floor like that—bold, considering the room."
            a "Why be subtle in a place built to be seen?"
            l "Fair point. Though Glass is rarely subtle."
        elif is_mid:
            l "Crossing the floor like that—bold, considering the room."
            a "Bold or stupid?"
            l "Maybe both."
            athought "Her tone almost sounds human again."
        else:
            l "Crossing the floor like that—brave, for someone under orders."
            a "Orders said twenty-two hundred sharp."
            l "And you’ve never missed one."
            a "Not a habit I plan to start."
    else:
        l "You skipped the introductions."
        a "Crowd wasn’t my scene."
        l "It never is. Glass doesn’t socialize. Glass performs."
        a "You seem to know a lot about Glass."
        l "I recognize my own reflection."

    # --- QUIET BEAT AT THE RAIL ---
    "They stand at the rail; the city's noise folds over itself below."
    pause 0.8

    if not check_scene_flag("act1_05_gala", "approach_lyra"):
        l "I didn’t expect to find you out here."
        a "I didn’t expect you to leave a spotlight unattended."
        a "You should be inside, charming anyone with a title."
    else:
        a "Shouldn’t you be inside, charming anyone with a title instead of talking to me?"

    l "(soft) Please. I’d rather jump."
    a "(half-smile) Careful. They might call that sedition."

    # --- PERFORMANCE DISCUSSION ---
    l "Take away the performance and there’s not much left."
    athought "Her voice drops — not the formal Lyra, something underneath."
    a "You’ve done it your whole life."
    l "Since I could walk. That doesn’t mean I’m blind."
    l "They call me the system’s proof. Polished. Perfect. Pristine."
    l "I call it glass. Transparent enough to see through. Empty enough to break."
    a "So you know."
    l "Of course I know. Glass recognizes glass."
    a "Then tell me—what do you see now?"
    l "(studies him) A room drunk on power it barely understands."
    l "People who’ll do anything to feed a machine that eats the rest."
    l "And one person out here—pretending he’s forgotten how to care."
    l "(softer) But the pretending’s getting harder, isn’t it?"

    if is_ob_hard:
        a "(quiet) Pretending keeps the system stable."
    elif is_mid:
        a "(quiet) Pretending’s easier than remembering."
    else:
        a "(quiet) Maybe I’m tired of pretending."

    pause 0.9

    l "I hear the rumors, and I know they’re far from the truth."
    l "They say Glass is perfect. Glass is empty. Glass doesn’t feel."
    a "And?"
    l "And I think Glass is lying to itself."

    # --- HISTORY REFLECTION ---
    a "They’ve been whispering since I was twelve."
    a "Used to be about failure. The Branding. The son who couldn’t."
    a "Now it’s about the soldier who does. 390 operations. Zero failures."
    a "Not sure which whispers are worse."
    l "Let them. Fear’s loud when it’s small."
    a "They just respect my father."
    a "I’m just a rumor. An heir to a name that doesn’t fit."
    athought "Rylan. Heavy word. Hollow sound."

    # --- MICRO-CHOICE: ash gesture ---
    menu:
        "The ember brightens at the tip."
        "Flick ash over the rail.":
            $ record_choice_once(
                _current_scene_id, "_ash_flick",
                next_scene_label="act1_07_bedroom",
                note="Symbolic discard of performance residue."
            )
            $ set_scene_flag(_current_scene_id, "ash_flick")

            "Ash falls and vanishes into neon."
            pause 0.7

            if norm >= 0.17:
                athought "Let it fall. Maybe some things deserve to land where light can’t reach."
            elif is_ob_hard:
                athought "Let it fall. Out of sight, out of system."
            else:
                athought "Let it fall. Easier than holding on."

        "Tap ash into the tray.":
            $ record_choice_once(
                _current_scene_id, "_ash_tray",
                next_scene_label="act1_07_bedroom",
                note="Maintains control; keeps mess contained."
            )

            "He taps the tray’s edge; the ember settles."
            pause 0.7
            
            if is_ob_hard:
                athought "Controlled. Contained. Like everything else."
            elif norm >= 0.17:
                athought "Still control. But less certainty in why."
            else:
                athought "Routine gesture. Keeps the silence steady."

    # --- TRUTH AND LEASH ---
    a "Why are you really out here?"
    l "Because in a room full of polish, you’re the only one not pretending."
    a "I’m always pretending. Glass is nothing but pretense."
    l "No. Glass is what they made you pretend to be."
    l "The person asking that question is the one I came to see."

    "They smoke in the hush between gusts of wind."
    pause 0.8

    a "How long are you back from assignment?"
    l "Not long. High value means high surveillance."
    l "They let me breathe when it’s useful."
    a "And tonight?"
    l "Parade duty. Proof the machine still works."
    l "They parade me. They parade you. Two perfect soldiers."
    l "Except neither of us believes a word of it anymore."
    a "They think everything belongs to them."
    a "The dark tells the truth."
    a "And you—"
    a "—you don’t belong to anyone."

    "She doesn’t step away. Neither does he."
    pause 0.7

    athought "The city hums below. Up here, the silence is louder."
    athought "Two pieces of glass, leaning close enough to touch."
    athought "Wondering if contact will shatter both."
    l "(quiet) Always so serious."
    l "And here I thought I was the dramatic one."

    # --- MICRO-CHOICE: PRESS HER ---
    menu:
        "Say nothing—or press."
        "Press her about the leash she’s on.":
            $ record_choice_once(
                _current_scene_id, "_press_leash",
                next_scene_label="act1_07_bedroom",
                note="Applies pressure; prioritizes information over care."
            )
            $ set_scene_flag(_current_scene_id, "pressed_topic")

            a "Who holds the leash tonight—Council or Command?"
            l "(a beat) Does it matter, if they pull the same direction?"
            athought "She looks away. Jaw tight. Breath unsteady."
            athought "She’s not deflecting. She’s drowning."
            a "It matters if you’re the one being pulled."
            l "(studies him) And what about you? Who pulls your leash?"
            a "Father. Always Father."
            l "Then we’re both dogs on strings."
            l "Wondering if cutting them means freedom or falling."

        "Let the moment breathe.":
            $ record_choice_once(
                _current_scene_id, "_let_breathe",
                next_scene_label="act1_07_bedroom",
                note="Practices restraint; centers her comfort over answers."
            )

            if is_ob_hard:
                athought "Questions disrupt function. Silence keeps form."
            elif norm >= 0.17:
                athought "I let the question stay between us. Some truths deserve air, not pressure."
            else:
                athought "I leave the question where it belongs—in the smoke."

    "Two faint sparks hang in the night—then dim with the wind."
    pause 0.8

    # --- VULNERABILITY BEAT ---
    l "(quietly) Do you ever wonder what we’d be without the uniforms?"
    a "Every night."
    l "And?"
    a "I don’t have an answer. Just questions Glass isn’t supposed to ask."
    l "Then maybe Glass is already breaking."
    a "(looks at her) Is that what you want? For me to break?"
    l "I want you to remember what it feels like to be whole."
    l "Even if that means shattering first."

    # --- CLOSING EMOTIONAL BEAT ---
    "For a moment, the world feels smaller. Just two people. Just smoke and silence."
    pause 0.9

    if is_ob_hard:
        athought "Six hours ago, I executed four liabilities. Nothing personal."
        athought "Yet standing here, something personal tries to surface. I push it down."
    elif is_mid:
        athought "Six hours ago, I killed four people. The thought keeps returning like a pulse I can’t ignore."
        athought "Standing here, I finally feel its weight."
    else:
        athought "Six hours ago, I killed four people. The echo still vibrates in my chest."
        athought "And for the first time, I let it hurt."
    athought "Maybe that’s what she means. Maybe feeling it is how Glass breaks."

    $ set_scene_flag(_current_scene_id, "completed")
    #$ telemetry(_current_scene_id, gates_met=True)
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_06_balcony
# cann.when_in_timeline: Act I immediately after Gala; pre-Bridge path-lock era.
# cann.what_happened:
#   - Aeron and Lyra meet in honest air (cool palette vs warm gala).
#   - Micro-choices modulate intimacy (shared_light, held_gaze), control (ash tray), and care (let_breathe vs press).
#   - Lyra frames “Glass” as performance; Aeron edges toward admitting fatigue with pretense.
#   - Empathy-acceptance language appears in VO (“tired of pretending,” “let it hurt”) but choices remain flavor.
# cann.aeron_state: Branch by tier — OB-hard suppresses; mid acknowledges; EMP admits feeling.
# cann.path_tracking:
#   - Incoming running range:  [-11, +8]   # post-Gala (act1_05); Balcony has no score calls by design
#   - Scene deltas (all NEU):  shared_light 0 | held_gaze 0 | ash_flick 0 | press/let_breathe 0
#     Net per-scene span: **0** (no empathy/obedience math here).
#   - Outgoing running range:  [-11, +8]
# cann.flags:
#   shared_light | held_gaze | ash_flick | pressed_topic | (implicit) let_breathe via branch | completed
# cann.thematic_flags:
#   - Motifs: Glass/Performance vs Honesty; Altitude & Pressure; Reflection.
#   - Recurring line echoes: “Glass doesn’t [touch/feel/retreat]”; “Maybe I’m tired of pretending.”
#   - Weather grammar: Aeries above cloud-deck — use wind/pressure/condensation; no rain-on-glass.
# cann.block_status: VARIANT-heavy ANCHOR (routes to rooftop-quiet or interior reset depending on flags).
# cann.true_path_integration: none (menus never touch TP).  # If desired later: mark non-menu acceptance beats as TP candidates.
# cann.visual_plate_economy:
#   - REUSE: Single balcony master with door open/closed passes; push/crop for intimacy beats.
#   - REUSE: Skyline plate with adjustable haze; optional breath-plume overlay.
#   - HERO: Eye-line CU at “Maybe I’m tired of pretending.” (marketing still).
# cann.requires_followup:
#   - If held_gaze OR (language admits fatigue) OR “let it hurt” branch text present → unlock warmer rooftop-quiet variant next.
#   - Else → route to neutral corridor return.
# cann.consistency_asserts:
#   - Lyra diction: formal/melodic; contractions acceptable in low-formality private space (balcony qualifies).
#   - Enforce altitude/weather rules; no precip terms at this height.
# cann.qa_hooks:
#   - Log NEU choices with `record_choice_once` for audit (e.g., balcony_shared_light, balcony_held_gaze, balcony_ash_flick, balcony_press/let_breathe).
#   - Ensure `_current_scene_id`/label match and unique flag tokens per micro-choice.