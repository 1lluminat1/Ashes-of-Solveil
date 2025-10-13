# act1_06_balcony.rpy


# ===================================================
# ACT 1 - Scene 6: The Balcony
# ===================================================


label act1_balcony:

    # VISUAL: Neon-lit skyline beyond the rail; rain tapering to mist.
    # Atmosphere: cooler palette than the gala; city hum below.
    "{i}The city's glow cuts hard lines across the stone.{/i}"

    a "{i}They look down at the Unders like it is another species. Still human. All of us.{/i}"

    # VISUAL: Cigarette beat (keep as narration + implied prop).
    "{i}Aeron lights a cigarette. Smoke threads into the neon.{/i}"

    # VISUAL: Footfalls approach from the doorway—measured, unhurried.
    "{i}Footfalls in the archway—measured, unhurried.{/i}"

    # Lyra arrives — keep voice formal (few/no contractions).
    l "Do you have a light?"
    a "(wry) I did't think Echelon's exemplar smoked."
    l "(a faint smile) If you know a better way to breathe in there, I'm listening."

    # --- MICRO-CHOICE: share the light (intimacy distance) ---
    menu:
        "Lyra steps in close, waiting for the flame."
        "Lean in and light it for her.":
            $ aeron_shares_light = True
            "{i}He lifts the flame. She leans in; her eyes do not leave his.{/i}"
        "Offer the lighter and step back.":
            $ aeron_shares_light = False
            "{i}He hands her the lighter. Distance holds.{/i}"
    # ----------------------------------------------------------

    # Optional glance beat up close.
    menu:
        "For a breath, she remains close."
        "Hold her gaze.":
            $ aeron_holds_her_gaze = True
            a "{i}Color on smoke. For once, no audience.{/i}"
        "Look past her to the city.":
            $ aeron_holds_her_gaze = False
            a "{i}The skyline answers for me.{/i}"

    # Callback to earlier micro-exchanges inside the gala.
    if aeron_spoke_to_lyra_gala:
        l "You didn't keep me waiting."
        if aeron_moves_toward_lyra:
            l "Crossing the floor like that—bold, considering the room."
            a "Why be subtle in a place built to be seen?"  # FIXED: Added question mark
            l "(faint smile) Fair point."  # NEW: Response
        else:
            a "You said five."
            l "And you listened."
    else:
        l "You skipped the introductions."
        a "Crowd was not my scene."
        l "It never is."

    # Optional nod if he confronted the whisperers
    if aeron_confronts_elites:
        l "I saw you correct the record."
        a "They were loud."
        l "Most people are, until someone looks back."

    # Quiet beat at the rail.
    "{i}They stand at the rail; the city's noise folds over itself below.{/i}"

    if !aeron_moves_toward_lyra:
        l "I didn't expect to find you out here."
        a "I didn't expect you to leave a spotlight unattended."
        a "I figured you would be inside, charming anyone with a title."
    else:
        a "Shouln't you be inside, charming anyone with a tite instead of mingling with me?"
    l "(soft) Please. I would rather jump."
    a "(half-smile) Careful. They might call that sedition."

    l "Take away the performance and there's not much left."
    a "You've done it your whole life."
    l "Since I could walk. That doesn't mean I'm blind."
    a "Then tell me—what do you see now?"

    l "(studies him) A room drunk on power it barely understands."
    l "People who will do anything to feed a machine that eats the rest."
    l "And one person out here—"
    l "—pretending he's forgotten how to care."

    a "{i}Her words land like a memory I didn't ask for.{/i}"
    a "You always read between the lines."

    l "I hear the rumors, and I know they are far from the truth."
    a "They've been whispering since I was twelve."
    l "Let them. Fear is loud when it's small."
    a "They just respect my father."
    a "I'm just a rumor. An heir to a name that doesn't fit."
    a "{i}Rylan. Heavy word. Hollow sound.{/i}"

    # --- MICRO-CHOICE: ash over the city (defiance) or keep tidy (control) ---
    menu:
        "The ember brightens at the tip."
        "Flick ash over the rail.":
            $ aeron_flicks_ash = True
            "{i}Ash falls and vanishes into neon.{/i}"
        "Tap ash into the tray.":
            $ aeron_flicks_ash = False
            "{i}He taps the tray's edge; the ember settles.{/i}"
    # -------------------------------------------------------------------------

    a "Why are you really out here?"
    l "Because in a room full of polish, you're the only one not pretending."

    "{i}They smoke in the hush between gusts of wind.{/i}"

    a "How long are you back from assignment?"
    l "Not long. High value means high surveillance."
    l "They let me breathe when it's useful."
    a "And tonight?"
    l "Parade duty. Proof the machine still works."

    a "They think everything belongs to them."
    a "The dark tells the truth."
    a "And you—"
    a "—you don't belong to anyone."

    # NEW/REVISED: Proximity moment with more physical detail
    # VISUAL: The space between them narrows—neither moves, but distance shrinks.
    #"{i}Something shifts—small, undeniable.{/i}"
    "{i}She does not step away. Neither does he.{/i}"
    a "{i}The city hums below. Up here, the silence is louder.{/i}"

    l "(quiet) Always so serious."
    l "And here I thought I was the dramatic one."

    # --- MICRO-CHOICE: risk a question about her leash (pressure vs restraint) ---
    menu:
        "Say nothing—or press."
        "Press her about the leash she is on.":
            $ aeron_presses_topic = True
            a "Who holds the leash tonight—Council or Command?"
            l "(a beat) Does it matter, if they pull the same direction."
        "Let the moment breathe.":
            $ aeron_presses_topic = False
            a "{i}I leave the question where it belongs—in the smoke.{/i}"
    # ---------------------------------------------------------------------------

    "{i}Two faint sparks hang in the night—then dim with the wind.{/i}"
    # NEW: Closing emotional beat
    "{i}For a moment, the world feels smaller. Just two people. Just smoke and silence.{/i}"
    # VISUAL: Fade out to next scene.

    return