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

    # ---------- Stage directions ----------
    # CAMERA: Slow 180° arc around altar (40–50mm), incense in foreground; later push-in on Marcus reveal.
    # LIGHTING: White oculus shafts; particulate incense visible; low gold bounce from filigree.
    # SFX: Low choral bed + sub HVAC; relic hum rises to tinnitus whine at peak.
    # FX/COMP: Overexposure pulse on failure; hairline light cracks under skin; falling Band sparks.
    # BLOCKING/PROPS: Relic suspended; silk pillow with Band; Marcus in column shadow, half-profile.
    # ---------------------------------------------------

    # VISUAL: Circular chamber; relic suspended midair; gold filigree walls.
    # LIGHTING: White shafts from oculus; particulate incense visible.
    # COSTUME: Aeron in white; clerics in muted gold; Marcus in shadow behind column.
    # SOUND: Low choral bed + quiet machine hum under it.

    a "{i}This is it. The day the Rylan legacy was supposed to pass to me.{/i}"
    a "{i}Twelve years old. Same age Kael was when he got his Band.{/i}"
    a "{i}At least, that’s what they always said.{/i}"

    # CAMERA: Slow 180° around altar; incense smoke trails.
    "{i}Low voices rise, threaded with hidden speakers.{/i}"
    c1 "We gather under the Eye of Ascension. One of the blood. One of the line."
    c2 "Let the relic bear witness. Let the flame carve its path."
    c3 "Let him bear the mark."
    c4 "May his vessel carry command."
    c1 "Echelon blesses you, child of lineage."

    # PROP: Silver Band on silk pillow; micro reflections on bevels.
    "{i}A silver Band rests on silk, catching the cold light.{/i}"

    # VISUAL: Close-up on young Aeron's face—eyes wide, breathing shallow.
    "{i}His heart hammers. Sweat beads at his temples despite the cool air.{/i}"
    a "{i}Kael said it hurt. He didn’t say how much.{/i}"
    a "{i}Hold still. Don’t embarrass Father. Don’t fail.{/i}"

    # VISUAL: Cleric lifts the Band; it hovers over Aeron's wrist.
    "{i}The Band rises. Light refracts through its core. Beautiful. Deadly.{/i}"
    "{i}Metal touches skin. The Band cinches.{/i}"

    # VISUAL: The Band contracts—tightening like a living thing.
    "{i}It tightens. Cold metal warming against his pulse.{/i}"
    a "{i}Wait for it. The sync. The bond. Like Kael described.{/i}"

    # VISUAL: Young Aeron's expression shifts—confusion, then pain.
    "{i}But something’s wrong. The pressure doesn’t ease. It builds.{/i}"

    # FX: Relic core glow ramps; subtle vibration passes into altar.
    "{i}The relic hums—low at first, rising like a blade under breath.{/i}"
    "{i}Light lashes from its core, strikes the Band. Sparks race across his skin.{/i}"

    a "{i}It sears—but I hold still. This is what I trained for.{/i}"

    # VISUAL: Symbols bloom along his arm—then immediately begin to crack and splinter.
    "{i}Symbols bloom along his arm, burrowing beneath the flesh.{/i}"
    "{i}Then—cracks. Hairline fractures spreading like ice breaking.{/i}"

    # VISUAL: Young Aeron's face contorts—pain beyond what he expected.
    a "{i}It’s burning. Not warming. Burning.{/i}"
    a "{i}Something’s wrong. Why won’t it stop?{/i}"

    # SOUND: High-pitched whine building; relic resonance unstable.
    "{i}The whine builds. Pressure splits the air. His teeth clench.{/i}"

    # FX: Overexposure pulse; hairline cracks of light under skin; sub-bass flutter.
    "{i}Then—too bright. The air thickens. Stone trembles.{/i}"
    ya "—AHH—!"

    # VISUAL: The Band flares white-hot; young Aeron screams.
    "{i}White heat. Blinding. The world reduces to pain and light.{/i}"
    a "{i}Make it stop make it stop make it STOP—{/i}"

    "{i}Marks surge—then recoil, vanishing like retreating fire.{/i}"
    "{i}The Band flares white, fractures, and drops away—dead metal on stone.{/i}"

    # SOUND: Choir cuts; only altar hum remains.

    # VISUAL: Young Aeron collapses to his knees; gasping, trembling.
    "{i}He falls. Knees hit stone. Hard. The impact barely registers.{/i}"
    "{i}Breath won’t come. Chest heaves. Nothing fills the space.{/i}"
    a "{i}What… what happened? Why did it…?{/i}"

    # VISUAL: His wrist—unmarked. No scar. No symbol. Nothing.
    "{i}His wrist is bare. Unblemished. Empty.{/i}"
    a "{i}Nothing. There’s nothing.{/i}"

    # Varied cleric reactions
    c2 "(breathless) The Band—it rejected him—"
    c3 "(stepping back) Impossible—this has never—"
    c4 "(to Marcus) General, we should attempt the binding again—"
    c1 "(quiet, awed) The relic… it recoiled from him."

    # CAMERA: Push on Marcus stepping from shadow; edges vignette.
    m "Enough."

    # VISUAL: Marcus crosses to Aeron; stands over him; face unreadable.
    "{i}Father’s shadow falls across him. Aeron can’t meet his eyes.{/i}"
    a "{i}I failed. I failed him. I failed everyone.{/i}"

    # VISUAL: Marcus's hand rests briefly on Aeron's shoulder—firm, not comforting.
    "{i}A hand on his shoulder. Heavy. Claiming.{/i}"

    m "Fate chose differently. The Band did not fail—it responded."
    m "My son has a purpose you cannot comprehend."
    m "The relic spoke. Not rejection—revelation."

    # Marcus already planning what Aeron will become
    m "(quieter, to clerics) He will serve in other ways."
    m "The Band grants faith. I will grant him skill."
    m "One makes believers. The other makes tools."

    # TRANSITION: Hard match cut to Aeron's present silhouette in window light.
    a "{i}That day, a story was written for me.{/i}"
    a "{i}My father called it destiny. I think he just couldn’t stand another failure.{/i}"

    # Kael context — corrected timeline
    a "{i}Kael’s Band worked. For three years after his Branding at twelve, he belonged.{/i}"
    a "{i}Then at fifteen, it turned on him. Rejected him.{/i}"
    a "{i}He had three years of being whole. I never got one.{/i}"

    # The walk home
    a "{i}I remember the walk home. Silent. Marcus ahead. Me behind.{/i}"
    a "{i}My wrist still burned where the Band had been. I kept touching the empty space.{/i}"
    a "{i}He didn’t look back once. Not when I stumbled. Not when I stopped to breathe.{/i}"
    a "{i}Just kept walking. Like I was already an afterthought.{/i}"

    # Marcus rewriting the narrative
    a "{i}That night, I heard him on the terminal. Rewriting the report.{/i}"
    a "{i}'Not failure. Fate. Not broken. Chosen.'{/i}"
    a "{i}And quieter: 'If he cannot have faith, I will make him useful.'{/i}"
    a "{i}I believed him because I had to.{/i}"
    a "{i}What else was left?{/i}"

    # Origins of the mask
    a "{i}The Band was supposed to make me whole.{/i}"
    a "{i}Instead, he made me precise.{/i}"
    a "{i}Ten years of missions. 390 successes. Zero hesitation recorded.{/i}"
    a "{i}He wanted a believer. He built something else.{/i}"
    a "{i}Transparent. Efficient. Predictable.{/i}"
    a "{i}And we both pretended that meant strength.{/i}"

    # Alignment-tinted present reflection
    $ tier = get_alignment_tier()
    $ norm = get_alignment_score_norm()
    $ is_ob_hard = pass_tier("OB3","OB2")
    $ is_mid     = pass_tier("OB1","C")

    if is_ob_hard:
        a "{i}That precision still holds. Mostly. A system shouldn’t question its code.{/i}"
        a "{i}But sometimes I feel the old lines flex—like metal under strain.{/i}"
        a "{i}If that’s weakness, I’ll cauterize it. Like he taught me.{/i}"
    elif is_mid:
        a "{i}That precision still holds. But lately, it falters.{/i}"
        a "{i}Lyra sees it. Maybe others do too.{/i}"
        a "{i}I can’t tell if that’s a crack forming or a door opening.{/i}"
    else:
        a "{i}That precision was never strength. It was silence.{/i}"
        a "{i}Lyra saw through it. Saw me.{/i}"
        a "{i}Maybe the Band rejected me because it knew I wasn’t meant to obey forever.{/i}"
        a "{i}Maybe I was meant to feel.{/i}"

    # Momentum whisper (very light)
    $ mom = get_alignment_momentum()
    if mom >= 0.5:
        a "{i}Lately the edges are softening. On purpose.{/i}"
    elif mom <= -0.5:
        a "{i}Lately the edge returns faster. Reflex over choice.{/i}"

    $ set_scene_flag(_current_scene_id, "completed")

    return

# ========= CANON NOTES =========
# cann.scene_id: act1_09_ritual_flashback
# cann.when_in_timeline: Age 12, Tier Hall Branding; immediately precedes Marcus’s “useful without faith” program.
# cann.what_happened:
#   - Branding attempt; relic recoils; Band fractures and falls away.
#   - Marcus reframes as revelation; commits Aeron to precision over faith.
#   - Kael context: branded at 12, rejection at 15.
# cann.aeron_state: Adult Aeron VO reflects; child Aeron speaks only when diegetic (scream/brief lines).
# cann.path_tracking: No choices; no deltas. Pure anchor memory.
# cann.thematic_flags: Glass origin; Faith vs Utility; Performance; Father’s narrative control.
# cann.block_status: ANCHOR; feeds later Marcus holo-call tone and OB/EMP shading.
# cann.visual_plate_economy: One chamber master + effects plates (overexposure pulse, Band fall) reusable in later montage.