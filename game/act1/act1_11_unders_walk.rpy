# act1_11_unders_walk.rpy


# =======================================================
# ACT 1 - Scene 11: Aeron's Late Night Walk in the Unders
# =======================================================


    label act1_unders_walk:
        "{i}Later that night...{/i}"

        # VISUAL: Aeron in a hooded coat, descending into the Unders via an old elevator or stairwell. 
        # Flickering neon signs, dripping pipes, the smell of ozone and oil.

        "{i}An elevator grinds somewhere above him, echoing like a heartbeat made of metal.{/i}"
        "{i}Each floor he passes bleeds more color—red, green, electric blue. Solveil’s veins run brightest down here.{/i}"
        
        a "{i}I couldn’t sleep. Not after tonight.{/i}"
        a "{i}The air down here tastes different—metal and rainwater. Not clean, but honest.{/i}"

        "{i}A drop of condensation hits the concrete beside him. Even the walls seem to breathe.{/i}"

        # He passes a market stall — vendors selling scrap tech, food cooked over open flames.

        "{i}The Unders pulse with a different kind of life. No marble, no velvet. Just rust, steam, and survival.{/i}"
        "{i}A child laughs somewhere in the dark. A blade hisses through an oil rag. Voices rise, barter, vanish.{/i}"

        a "{i}They call this place forgotten, but I think it’s the only part of Solveil still awake.{/i}"

        # Children dart past, laughing, barefoot. A man sharpens a blade under a flickering sign. 
        # An Enforcer drone buzzes overhead but doesn’t stop.

        "{i}A drone hums overhead, light sweeping like a searchlight—but it keeps going. Down here, even Echelon’s machines look tired.{/i}"

        a "{i}Even down here, their eyes are everywhere. But the people don’t bow. They keep moving.{/i}"

        "{i}Someone calls out a price for batteries. Someone else curses in three different dialects.{/i}"
        "{i}The rhythm of the Unders isn’t order—it’s endurance.{/i}"

        # Aeron stops by a rail overlooking a lower level. Smoke rises in lazy curls.

        "{i}Aeron stops by a railing. Below, a thousand tiny fires glow in the dark like stars that forgot the sky.{/i}"

        a "{i}No spires. No chandeliers. Just humanity, raw and unpolished.{/i}"

        "{i}He exhales, watching the smoke fade into the haze below.{/i}"

        # A woman approaches — worn clothes, eyes tired but kind.

        woman "Looking for a good time, stranger? Warm bed, no questions asked."
        menu:
            "Accept her offer":
                a "{i}Her voice is soft. Tired. Everything I thought I wanted...{/i}"
                a "{i}But even as I nod, I already feel cold inside.{/i}"
                # Fade out – do not show the act.

                "{i}Later, Aeron sits on the edge of a narrow cot, shirt half-buttoned, cigarette trembling between his fingers.{/i}"
                "{i}The room smells like dust and old perfume. The ceiling hums with the pipes above.{/i}"

                a "{i}Connection isn’t something you can buy.{/i}"
                a "{i}I don’t even remember her name.{/i}"
                a "{i}I’m not sure I ever wanted to.{/i}"

                "{i}He leaves a few credits on the nightstand and steps back into the noise.{/i}"
            "Refuse politely":
                a "(shakes his head) Not tonight."
                woman "(shrugs) Your loss."
                a "{i}Her footsteps fade back into the crowd. I feel lonelier than before.{/i}"
                "{i}A stall light flickers, briefly catching his reflection in a puddle—tired eyes, same face he’s been trying to escape.{/i}"

        # Aeron keeps walking, the Unders stretching ahead.

        "{i}Steam coils from vents overhead, curling around the steel walkways like ghostly roots.{/i}"

        a "{i}This place feels like a mirror. Everyone down here is running from something.{/i}"
        a "{i}Me too.{/i}"

        "{i}A siren wails in the distance. No one flinches. Down here, noise is just another kind of weather.{/i}"

        # He stops at a flickering sign, looking up at the rusted beams above.

        "{i}A flickering neon sign buzzes weakly—half the letters dead, the rest fighting to stay lit.{/i}"

        a "{i}Maybe the Unders aren’t forgotten. Maybe they’re just waiting—for someone to remember them.{/i}"

        "{i}A gust of wind sweeps through the corridor, carrying the scent of rain and iron. The lights dim, then steady.{/i}"
        "{i}Somewhere above, Solveil sleeps. Down here, life refuses to.{/i}"

        # Fade out, setting up next plot beat.
        return
