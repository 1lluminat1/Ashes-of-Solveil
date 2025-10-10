# act1_08_ritual_flashback.rpy


# ======================================================
# ACT 1 - Scene 8: Flashback: Aeron's Branding Ritual
# ======================================================


label act1_ritual:
    define c1 = Character("Cleric 1", color="#000000")
    define c2 = Character("Cleric 2", color="#000000")
    define c3 = Character("Cleric 3", color="#000000")
    define c4 = Character("Cleric 4", color="#000000")
    # VISUAL: A golden chamber deep within the Aeries. Ancient relic suspended midair. Aeron lies on a ceremonial table, robed in white. Marcus watches from the shadows.
    # The chamber is circular, walls adorned with golden engravings of past Echelon champions.
    # Incense smoke curls through shafts of white light filtering from the domed ceiling.
    # Four clerics stand at cardinal positions. Each holds a staff embedded with a fragment of the original Relic.
    # Aeron lies on a stone altar veined with glowing circuitry. His ceremonial gown shimmers with gold thread.
    ya "{i}This is it...{/i}"
    ya "{i}The day I was born for. The day the Rylan legacy passes to me.{/i}"
    ya "{i}At least, that’s what they’ve always told me.{/i}"

    "{i}Low voices rise, threaded with static from hidden speakers.{/i}"
    c1 "We gather under the Eye of Ascension. One of the blood. One of the line."
    c2 "Let the relic bear witness. Let the flame carve its path."
    c3 "Let him bear the mark of the Risen."
    c4 "May his vessel carry the burden of command."
    c1 "Echelon blesses you, child of lineage."

    # A cleric steps forward, presenting a radiant silver band on a silk pillow.
    "{i}A silver Band rests on a silk pillow, catching the cold light.{/i}"
    # The band is placed onto Aeron's wrist. Another cleric raises the relic staff.
    "{i}Metal kisses skin as the Band tightens around his wrist.{/i}"
    # VISUAL: The relic pulses. Tendrils of lightning shoot out, striking the band.
    "{i}The relic hums — low at first, then rising like a scream swallowed by silence.{/i}"
    "{i}A tendril of light lashes from its core, striking the band. Sparks dance across Aeron's skin.{/i}"

    ya "{i}It burns—no, it *sears*. But I hold still. This is what I trained for.{/i}"

    "{i}Symbols bloom along his arm, veins of light burrowing beneath the flesh.{/i}"

    # But then things turn.
    "{i}The light pulses again. Too bright. The air thickens. The stone beneath him trembles.{/i}"

    ya "AHHH—GOD—!!"

    "{i}Symbols race across his body like molten veins. His back arches. His voice breaks.{/i}"

    ya "AHHHH—AGHH—FUCK—!!"

    # The marks spread rapidly, covering his entire body, before violently receding and vanishing.
    # The band glows blinding white... then shatters into dust.
    # Clerics recoil in stunned silence. The relic dims.
    "{i}A cleric fumbles their staff. The relic spasms, flickers—dies to a dull glow.{/i}"
    "{i}The Band flares white, fractures, and bursts into dust.{/i}"

    c2 "(gasps) The band... rejected him..."
    c3 "No, it's impossible..."
    c4 "It’s never failed before—"

    m "Enough."
    # Marcus steps forward. Calm. Commanding.
    m "Fate has chosen differently. The band did not fail... it responded."
    m "My son has a greater purpose than any of you can comprehend."
    m "The relic has spoken. Not in rejection—but in revelation."
    m "My son is not forged like others. He is chosen."

    # FADE TO: Aeron’s present-day silhouette against the window.
    a "{i}That day... my fate was sealed.{/i}"
    a "{i}My father called it destiny. Said the relic had spoken.{/i}"
    a "{i}Maybe he was right. Or maybe he just couldn’t stand the thought of another failure.{/i}"
    a "{i}Either way, I spent the years that followed chasing someone else’s idea of who I should be.{/i}"
    a "{i}And somewhere along the way... I forgot how to be anything else.{/i}"
    return