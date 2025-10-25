# act1_06_balcony.rpy


# =======================================================
# ACT 1 – Scene 6: Balcony
# =======================================================


label act1_balcony:
    $ scene_id = "act1_06_balcony"

    # Precompute alignment reads once for this scene
    $ tier = get_alignment_tier()           # OB3, OB2, OB1, C, EMP1, EMP2, EMP3
    $ band = get_empathy_band()             # "obedience" | "conflicted" | "empathy"
    $ norm = get_alignment_score_norm()     # -1.0 .. +1.0 (≈ +0.17 ~ +2 on ±12 scale)
    $ mom  = get_alignment_momentum()       # -1 .. +1 recent push

    # Convenience buckets matching original thresholds
    $ is_ob_hard = pass_tier("OB3","OB2")           # ≈ score <= -4
    $ is_mid     = pass_tier("OB1","C")             # ≈ -3 .. +1
    $ is_emp     = pass_tier("EMP1","EMP2","EMP3")  # ≈ >= +2 (we’ll still use norm for finer cases)

    # VISUAL: Neon-lit skyline beyond the rail; rain tapering to mist.
    # Atmosphere: cooler palette than the gala; city hum below.
    "{i}The city's glow cuts hard lines across the stone.{/i}"

    if is_ob_hard:
        a "{i}They look down at the Unders like another species. Maybe they’re right.{/i}"
        a "{i}Glass doesn’t care about altitude. Glass just reflects orders.{/i}"
    elif is_mid:
        a "{i}They look down at the Unders like another species. Still human. All of us.{/i}"
        a "{i}Glass doesn’t care about altitude. It only mirrors whoever’s watching.{/i}"
    else:  # empathy
        a "{i}They look down at the Unders like another species. Still human. All of us — even the ones pretending not to be.{/i}"
        a "{i}Glass catches their reflection and gives it back. Cracked, but still human.{/i}"

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
            $ set_scene_flag(scene_id, "shared_light")
            "{i}He lifts the flame. She leans in; her eyes don’t leave his.{/i}"
            if norm >= 0.17:  # ~ >= +2
                a "{i}Close enough to see the cracks — and the warmth leaking through them.{/i}"
            elif is_ob_hard:
                a "{i}Too close. Distance blurred. Glass doesn’t allow that.{/i}"
            else:
                a "{i}Close enough to see reflection, not truth.{/i}"

        "Offer the lighter and step back.":
            "{i}He hands her the lighter. Distance holds.{/i}"
            if is_ob_hard:
                a "{i}Glass doesn’t touch. Glass maintains form.{/i}"
            elif norm >= 0.17:
                a "{i}Even distance has weight when you want to close it.{/i}"
            else:
                a "{i}Space feels safe. Familiar. But not right.{/i}"

    # --- OPTIONAL GAZE BEAT ---
    menu:
        "For a breath, she remains close."
        "Hold her gaze.":
            $ set_scene_flag(scene_id, "held_gaze")
            if is_ob_hard:
                a "{i}Observation, not connection. I catalog her expression — nothing more.{/i}"
            elif is_mid:
                a "{i}Color on smoke. For once, no audience.{/i}"
                a "{i}She’s not looking at Glass. She’s looking for what’s left underneath.{/i}"
            else:
                a "{i}The world falls away. Just her eyes and the reflection inside them.{/i}"
        "Look past her to the city.":
            a "{i}The skyline answers for me. Easier to look at light than at someone who might actually see.{/i}"

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
            a "{i}Her tone almost sounds human again.{/i}"
        else:  # obedience side but not hard OB2/OB3
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
    "{i}They stand at the rail; the city's noise folds over itself below.{/i}"

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
    a "{i}Her voice drops — not the formal Lyra, something underneath.{/i}"
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
    a "{i}Rylan. Heavy word. Hollow sound.{/i}"

    # --- MICRO-CHOICE: ash gesture ---
    menu:
        "The ember brightens at the tip."
        "Flick ash over the rail.":
            $ set_scene_flag(scene_id, "ash_flick")
            "{i}Ash falls and vanishes into neon.{/i}"
            if norm >= 0.17:
                a "{i}Let it fall. Maybe some things deserve to land where light can’t reach.{/i}"
            elif is_ob_hard:
                a "{i}Let it fall. Out of sight, out of system.{/i}"
            else:
                a "{i}Let it fall. Easier than holding on.{/i}"

        "Tap ash into the tray.":
            "{i}He taps the tray’s edge; the ember settles.{/i}"
            if is_ob_hard:
                a "{i}Controlled. Contained. Like everything else.{/i}"
            elif norm >= 0.17:
                a "{i}Still control. But less certainty in why.{/i}"
            else:
                a "{i}Routine gesture. Keeps the silence steady.{/i}"

    # --- TRUTH AND LEASH ---
    a "Why are you really out here?"
    l "Because in a room full of polish, you’re the only one not pretending."
    a "I’m always pretending. Glass is nothing but pretense."
    l "No. Glass is what they made you pretend to be."
    l "The person asking that question is the one I came to see."

    "{i}They smoke in the hush between gusts of wind.{/i}"

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

    "{i}She doesn’t step away. Neither does he.{/i}"

    a "{i}The city hums below. Up here, the silence is louder.{/i}"
    a "{i}Two pieces of glass, leaning close enough to touch.{/i}"
    a "{i}Wondering if contact will shatter both.{/i}"

    l "(quiet) Always so serious."
    l "And here I thought I was the dramatic one."

    # --- MICRO-CHOICE: PRESS HER ---
    menu:
        "Say nothing—or press."
        "Press her about the leash she’s on.":
            $ set_scene_flag(scene_id, "pressed_topic")
            a "Who holds the leash tonight—Council or Command?"
            l "(a beat) Does it matter, if they pull the same direction?"
            a "{i}She looks away. Jaw tight. Breath unsteady.{/i}"
            a "{i}She’s not deflecting. She’s drowning.{/i}"
            a "It matters if you’re the one being pulled."
            l "(studies him) And what about you? Who pulls your leash?"
            a "Father. Always Father."
            l "Then we’re both dogs on strings."
            l "Wondering if cutting them means freedom or falling."

        "Let the moment breathe.":
            if is_ob_hard:
                a "{i}Questions disrupt function. Silence keeps form.{/i}"
            elif norm >= 0.17:
                a "{i}I let the question stay between us. Some truths deserve air, not pressure.{/i}"
            else:
                a "{i}I leave the question where it belongs—in the smoke.{/i}"

    "{i}Two faint sparks hang in the night—then dim with the wind.{/i}"

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
    "{i}For a moment, the world feels smaller. Just two people. Just smoke and silence.{/i}"

    if is_ob_hard:
        a "{i}Six hours ago, I executed four liabilities. Nothing personal.{/i}"
        a "{i}Yet standing here, something personal tries to surface. I push it down.{/i}"
    elif is_mid:
        a "{i}Six hours ago, I killed four people. The thought keeps returning like a pulse I can’t ignore.{/i}"
        a "{i}Standing here, I finally feel its weight.{/i}"
    else:
        a "{i}Six hours ago, I killed four people. The echo still vibrates in my chest.{/i}"
        a "{i}And for the first time, I let it hurt.{/i}"

    a "{i}Maybe that’s what she means. Maybe feeling it is how Glass breaks.{/i}"

    # VISUAL: Fade out to next scene.

    # canon_note: Lyra uses natural contractions; her diction tightens only in high-formality moments.
    # canon_note: Aeries lighting = top-down white/gold; balcony is cooler, honest space.
    # canon_note: New scene flags: shared_light, held_gaze, ash_flick, pressed_topic.
    # canon_note: Alignment reads use band/tier/norm/momentum; no direct empathy_score checks.
    # canon_note: This scene assumes act1_05_gala may set 'approach_lyra' for variant intros.

    return
