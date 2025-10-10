# act1_02_bedroom.rpy


# ===================================================
# ACT 1 - Scene 2: Aeron's Bedroom
# ===================================================


label act1_bedroom:
    # VISUAL: Dimly lit bedroom washed in cold blue. Rain trails down the glass; neon reflections bleed across the window.
    a "{i}Rain keeps tapping the glass... like it's trying to remind me the world’s still out there.{/i}"
    a "{i}I know it is, just not sure I’m part of it.{/i}"

    # VISUAL: Close-up of Aeron’s reflection in the window — distorted by raindrops, fractured across the glass.
    a "{i}They say a Band makes you someone...{/i}"
    a "{i}...so what does that make me?{/i}"

    # VISUAL: He crosses to the wall. A locked display case hangs there—empty.
    # Plaque: “For the Chosen.”
    a "{i}Funny—an empty frame feels heavier than the Band ever would’ve.{/i}"

    # VISUAL: Nightstand photo: Aeron and his older brother, smiling. The brother’s arm covers the Band on his wrist.
    a "{i}He always smiled like he belonged.{/i}"
    a "{i}Smiles fade when the lights cut out.{/i}"

    # VISUAL: Wardrobe opens. A crisp black Echelon uniform hangs, unused.
    a "{i}Wear the right clothes. Say the right words. Maybe they’ll forget I was never chosen.{/i}"

    # OPTIONAL ACTION 4 — Practice words or stay silent
    menu:
        "Does Aeron rehearse the lines Echelon expects to hear?":
            "Practice the pledge under his breath.":
                $ aeron_practiced_pledge = True
                a "\"{i}Order above all. Unity before self.{/i}\""
                a "{i}The words feel clean going in. They never come out that way.{/i}"
            "Stay silent.":
                $ aeron_practiced_pledge = False
                a "{i}Silence says enough.{/i}"

    # VISUAL: He sits at the edge of the bed again, looking out over the skyline.
    a "{i}Tomorrow, I do what’s required.{/i}"
    a "{i}After that... we’ll see.{/i}"

    # VISUAL: Hold on his back; rain and city lights pulse.
    return