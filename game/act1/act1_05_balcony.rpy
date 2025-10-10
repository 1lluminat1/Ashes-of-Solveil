# act1_05_balcony.rpy


# ===================================================
# ACT 1 - Scene 5: The Balcony
# ===================================================

label act1_balcony:
    # VISUAL: Neon-lit Solveil skyline beyond the rail. Distant hum of the city; rain tapering to mist.
    # Aeron steps out.
    "{i}He steps into the night air, the city’s glow cutting hard lines across the balcony stone.{/i}"
    a "{i}They look down at the Unders like it’s another species. Still human. All of us.{/i}"

    # Cigarette beat
    # (If you plan a lighter prop later, keep these as narration + implied SFX.)
    "{i}Aeron lights a cigarette. Smoke threads into the neon.{/i}"

    # Heels approach; Lyra in the doorway.
    "{i}Footfalls in the archway—measured, unhurried.{/i}"

    l "Got a light for an old colleague?"
    a "(wryly) Didn’t think Echelon’s golden girl smoked."

    l "(smirks) If you know a better way to breathe in there, I’m listening."

    # Lyra steps in; shared light.
    "{i}She leans close as he brings the flame to her cigarette. Her eyes don’t leave his.{/i}"
    "{i}For a moment, the city is just color on smoke.{/i}"

    # Callback: whether they had the micro-exchange in the gala
    if aeron_spoke_to_lyra_gala:
        l "You didn’t keep me waiting."
        if aeron_moves_toward_lyra:
            l "Crossing the floor like that—bold, considering the audience."
            a "Why bother being subtle in a room built to be seen?"
        else:
            a "You said five."
            l "And you listened."
    else:
        l "You skipped the introductions."
        a "Crowd wasn’t my scene."
        l "It never is."

    # Optional nod if he confronted the whisperers
    if aeron_confronts_elites:
        l "I saw you correct the record."
        a "They were loud."
        l "They’re always loud until someone looks back."

    # Quiet beat
    "{i}They stand at the rail, city noise folding over itself below.{/i}"

    l "Didn’t peg you for the rooftop type."
    a "Didn’t think you’d be one to duck out of the spotlight."
    a "Figured you’d be inside, charming anyone with a title."

    l "(soft laugh) Please. I’d rather jump."
    a "(half-smile) Careful. Someone might call that sedition."

    l "Take away the performance, and they’d have nothing left."
    a "You’ve done it your whole life."

    l "Since I could walk. Doesn’t mean I’m blind."
    a "Then tell me—what do you see now?"

    l "(studies him) A room drunk on power it barely understands."
    l "People who’ll do anything to feed a machine that eats the rest."
    l "And one person out here—"
    l "—pretending he’s forgotten how to care."

    a "{i}Her words hit like a memory I didn’t ask for.{/i}"
    a "You always did like reading between the lines."

    l "I hear the rumors. I know they're far from the truth."
    a "They’ve been whispering since I was twelve."

    l "Let them. Fear is loud when it’s small."
    a "They just respect my father."
    a "I’m just a rumor. Useless heir to a name that doesn’t fit."
    a "{i}Rylan. Heavy word. Hollow sound.{/i}"
    a "Why are you really out here?"

    l "Because in a room full of polish, you’re the only one not pretending."

    "{i}They smoke in the hush between gusts of wind.{/i}"

    a "How long are you back from assignment?"

    l "Not long. High value means high surveillance."
    l "They let me breathe when it’s useful."
    a "And tonight?"

    l "Parade duty. Proof the machine still works."
    a "They think everything belongs to them."
    a "But the dark always tells the truth."
    a "And you... you may have been built from their light..."
    a "...but you don’t belong to anyone."

    "{i}Something shifts—small, undeniable.{/i}"
    
    l "(quiet) Always so serious."
    l "And here I thought I was the dramatic one."
    a "{i}But she doesn’t pull away.{/i}"

    "{i}Two faint sparks hang in the night—then dim with the wind.{/i}"
    # Fade out to next scene
    return
