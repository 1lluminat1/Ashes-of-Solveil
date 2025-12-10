# ======================================================
# ACT 1 — Scene 09: Flashback — Aeron's Branding Ritual
# File: act1_09_ritual_flashback.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_09_ritual_flashback"
$ scene_mark(_current_scene_id, "entered")

define c1 = Character("Cleric 1")
define c2 = Character("Cleric 2")
define c3 = Character("Cleric 3")
define c4 = Character("Cleric 4")


label act1_09_ritual_flashback:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Slow 180° arc around altar (40–50mm), incense in foreground; later push-in on Marcus reveal.
    # LIGHTING: White oculus shafts; particulate incense visible; low gold bounce from filigree.
    # SFX LOOP: Low choral bed + sub HVAC.
    # SFX ONE-SHOTS: Relic hum rises to tinnitus whine at peak.
    # FX/COMP: Overexposure pulse on failure; hairline light cracks under skin; falling Band sparks.
    # BLOCKING: Relic suspended midair; silk pillow with Band; Marcus in column shadow, half-profile.
    # COSTUME: Young Aeron in white; clerics in muted gold; Marcus in Echelon formal, shadowed.

    # ========= OPENING — YOUNG AERON'S PERSPECTIVE =========
    # VISUAL: Circular chamber; relic suspended midair; gold filigree walls.
    # LIGHTING: White shafts from oculus; particulate incense visible.

    yathought "{i}This is it. The day the Rylan legacy was supposed to pass to me.{/i}"

    yathought "{i}Twelve years old—same age Kael was when he got his Band, at least that's what they always said.{/i}"

    # ========= THE CEREMONY =========
    # CAMERA: Slow 180° around altar; incense smoke trails.

    "Low voices rise, threaded with hidden speakers."

    c1 "We gather under the Eye of Ascension. One of the blood. One of the line."

    c2 "Let the relic bear witness. Let the flame carve its path."

    c3 "Let him bear the mark."

    c4 "May his vessel carry command."

    c1 "Echelon blesses you, child of lineage."

    # PROP: Silver Band on silk pillow; micro reflections on bevels.

    "A silver Band rests on silk, catching the cold light."

    # VISUAL: Close-up on young Aeron's face—eyes wide, breathing shallow.

    "His heart hammers. Sweat beads at his temples despite the cool air."

    yathought "{i}Kael said it hurt. He didn't say how much.{/i}"

    yathought "{i}Hold still. Don't embarrass Father. Don't fail.{/i}"

    # ========= THE BONDING ATTEMPT =========
    # VISUAL: Cleric lifts the Band; it hovers over Aeron's wrist.

    "The Band rises—light refracting through its core, beautiful and deadly."

    "Metal touches skin. The Band cinches."

    # VISUAL: The Band contracts—tightening like a living thing.

    "It tightens, cold metal warming against his pulse."

    yathought "{i}Wait for it. The sync. The bond. Like Kael described.{/i}"

    # VISUAL: Young Aeron's expression shifts—confusion, then pain.

    "But something's wrong. The pressure doesn't ease—it builds."

    # FX: Relic core glow ramps; subtle vibration passes into altar.

    "The relic hums, low at first, rising like a blade under breath."

    "Light lashes from its core, strikes the Band. Sparks race across his skin."

    yathought "{i}It sears—but I hold still. This is what I trained for.{/i}"

    # ========= THE REJECTION =========
    # VISUAL: Symbols bloom along his arm—then immediately begin to crack and splinter.

    "Symbols bloom along his arm, burrowing beneath the flesh."

    "Then—cracks. Hairline fractures spreading like ice breaking."

    # VISUAL: Young Aeron's face contorts—pain beyond what he expected.

    yathought "{i}It's burning. Not warming. Burning.{/i}"

    yathought "{i}Something's wrong. Why won't it stop?{/i}"

    # SOUND: High-pitched whine building; relic resonance unstable.

    "The whine builds. Pressure splits the air."
    "His jaw locks as muscles seize against the bone."

    # FX: Overexposure pulse; hairline cracks of light under skin; sub-bass flutter.

    "Then—too bright. The air thickens. Stone trembles."

    ya "—AHH—!"

    # VISUAL: The Band flares white-hot; young Aeron screams.

    "White heat. Blinding. The world reduces to pain and light."

    yathought "{i}Make it stop make it stop make it STOP—{/i}"

    "Marks surge—then recoil, vanishing like retreating fire."

    "The Band flares white, fractures, and drops away—dead metal on stone."

    # SOUND: Choir cuts; only altar hum remains.

    # ========= AFTERMATH =========
    # VISUAL: Young Aeron collapses to his knees; gasping, trembling.

    "He falls. Knees hit stone. The impact barely registers through the shock."

    "Breath won't come. Chest heaves. Nothing fills the space."

    yathought "{i}What… what happened? Why did it…?{/i}"

    # VISUAL: His wrist—unmarked. No scar. No symbol. Nothing.

    "His wrist is bare. Unblemished. Empty."

    yathought "{i}Nothing. There's nothing.{/i}"

    # ========= CLERIC REACTIONS — WITH TABOO DETAIL =========

    c2 "(breathless) The Band—it rejected him—"

    c3 "(stepping back) Impossible—this has never—"

    "Cleric 3's hand flies to his own wrist, covering his silver Band. A reflex—like touching a talisman to ward off contagion."

    c4 "(to Marcus) General, we should attempt the binding again—"

    c1 "(quiet, awed) The relic… it recoiled from him."

    # ========= MARCUS ENTERS =========
    # CAMERA: Push on Marcus stepping from shadow; edges vignette.

    m "Enough."

    # VISUAL: Marcus crosses to Aeron; stands over him; face unreadable.

    "Father's shadow falls across him. Aeron can't meet his eyes."

    yathought "{i}I failed. I failed him. I failed everyone.{/i}"

    # VISUAL: Marcus's hand rests briefly on Aeron's shoulder—firm, not comforting.

    "A hand on his shoulder—heavy, claiming."

    m "Fate chose differently. The Band did not fail—it responded."

    m "My son has a purpose you cannot comprehend."

    m "The relic spoke. Not rejection—revelation."

    # ========= MARCUS'S PLAN =========
    # NOTE: This is where Aeron's future is decided. Marcus is already calculating.

    m "(quieter, to clerics) He will serve in other ways."

    m "The Band grants faith. I will grant him skill."

    m "One makes believers. The other makes tools."

    # ========= TRANSITION TO PRESENT =========
    # CAMERA: Hard match cut to Aeron's present silhouette in window light.

    athought "That day, a story was written for me."

    athought "My father called it destiny. I think he just couldn't stand another failure."

    # ========= KAEL CONTEXT =========

    athought "Kael's Band worked. For three years after his Branding at twelve, he belonged."

    athought "Then at fifteen, it turned on him—rejected him."

    athought "He had three years of being whole. I never got one."

    # ========= THE WALK HOME =========

    athought "I remember the walk home. Silent. Marcus ahead, me behind."

    athought "My wrist still burned where the Band had been. I kept touching the empty space."

    athought "He didn't look back once—not when I stumbled, not when I stopped to breathe."

    athought "Just kept walking, like I was already an afterthought."

    # ========= MARCUS REWRITING THE NARRATIVE =========

    athought "That night, I heard him on the terminal. Rewriting the report."

    athought "'Not failure. Fate. Not broken. Chosen.'"

    athought "And quieter: 'If he cannot have faith, I will make him useful.'"

    athought "I believed him because I had to. What else was left?"

    # ========= ORIGINS OF THE MASK =========

    athought "The Band was supposed to make me whole. Instead, he made me precise."

    athought "Ten years of missions, 390 successes, zero hesitation recorded."

    athought "He wanted a believer. He built something else—transparent, efficient, predictable."

    athought "And we both pretended that meant strength."

    # ========= PRESENT REFLECTION — PATH-BASED =========

    if pass_tier("OB2", "OB3"):
        athought "That precision still holds. Mostly. A system shouldn't question its code."
        athought "But sometimes I feel the old lines flex—like metal under strain."
        athought "If that's weakness, I'll cauterize it. Like he taught me."
    elif pass_tier("OB1", "NEU"):
        athought "That precision still holds, but lately it falters."
        athought "Lyra sees it. Maybe others do too."
        athought "I can't tell if that's a crack forming or a door opening."
    else:
        athought "That precision was never strength. It was silence."
        athought "Lyra saw through it—saw me."
        athought "Maybe the Band rejected me because it knew I wasn't meant to obey forever."
        athought "Maybe I was meant to feel."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_09_ritual_flashback
# cann.when_in_timeline: Age 12, Tier Hall Branding; immediately precedes Marcus's "useful without faith" program.
# cann.what_happened:
#   - Branding attempt; relic recoils; Band fractures and falls away.
#   - Marcus reframes as revelation; commits Aeron to precision over faith.
#   - Kael context: branded at 12, rejection at 15.
#   - Taboo detail: Cleric covers his own Band in reflexive horror at the rejection.
# cann.aeron_state: Adult Aeron VO reflects; child Aeron speaks only when diegetic (scream/brief lines).
# cann.path_tracking: No choices; no deltas. Pure anchor memory.
# cann.thematic_flags: Faith vs Utility; Performance; Father's narrative control; Bare wrist taboo.
# cann.block_status: ANCHOR; feeds later Marcus holo-call tone and OB/EMP shading.
# cann.visual_plate_economy: One chamber master + effects plates (overexposure pulse, Band fall) reusable in later montage.