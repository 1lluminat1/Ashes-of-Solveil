# act1_14_lower_spans.rpy


# =======================================================
# ACT 1 - Scene 14: Aeron's Late Night Walk in the Lower Spans
# =======================================================


define vendor = Character("Vendor")
define child = Character("Child")

label act1_lower_spans:
    # VISUAL: Sector 10 lower spans / perimeter catwalks; maintenance stairs; neon fog below.
    # SOUND: Distant market; pipe drip; elevator chain clatter; occasional drone pass.
    # LIGHTING: Sodium/blue mix; signage flicker; steam plumes catching light.

    "{i}Each level bleeds more color—red, green, electric blue. The edges run brightest.{/i}"

    a "{i}I couldn't sleep. Not after tonight.{/i}"
    a "{i}Air tastes different down here—metal and rainwater. Not clean, but honest.{/i}"

    "{i}Condensation taps the concrete. The walls breathe.{/i}"

    # CAMERA: Slow walk-by wide shots; no deep Unders interiors.
    "{i}The lower spans pulse with another kind of life. No marble. No velvet. Just rust, steam, survival.{/i}"
    "{i}A child laughs; a blade slides through an oil rag. Voices rise, barter, vanish.{/i}"

    a "{i}They call this 'forgotten.' It feels more awake than the Aeries.{/i}"

    # VISUAL: Street vendor—makeshift stand, glowing heat coils, steam rising from metal pot.
    # PROP: Vendor stirs something dark and aromatic; chipped bowls stacked beside him.
    # LIGHTING: Warm orange glow from the coils; contrasts with cold blue surroundings.

    "{i}A vendor works a makeshift stand—heat coils glowing beneath a dented pot. The smell cuts through rust and rain.{/i}"
    vendor "(calls out) Therm-brew! Hot! Real beans, not synth!"

    # VISUAL: Aeron slows; the vendor notices his uniform beneath the coat.
    vendor "(cautious) ...You lost, soldier?"

    # ACTION: Player choice—engage or walk past.
    menu:
        "The vendor's eyes track him—wary, but not hostile."
        "Buy a cup.":
            $ aeron_bought_brew = True
            a "How much?"
            vendor "(surprised) ...Five credits."
            # VISUAL: Aeron pulls out payment chip; vendor's eyes widen slightly.
            a "Keep the change."
            vendor "(takes it slowly) ...You serious?"
            a "It smells better than anything in the Aeries."
            vendor "(softens) Well. Ain't that the truth."
            
            # VISUAL: Vendor pours dark liquid into a chipped ceramic cup; steam rises.
            "{i}The cup is warm. The liquid bitter, earthy, real.{/i}"
            a "{i}When was the last time I tasted something that wasn't sanitized?{/i}"
            
            vendor "You're Marcus Rylan's boy, yeah?"
            a "(carefully) I am."
            vendor "Heard about your brother. That was a damn shame."
            a "...Yeah. It was."
            vendor "(nods) Well. You're alright in my book. Stay warm."
            
            "{i}The vendor turns back to his pot. No ceremony. Just acknowledgment.{/i}"
            a "{i}Down here, respect isn't inherited. It's earned.{/i}"

        "Walk past without stopping.":
            $ aeron_bought_brew = False
            a "{i}Not here to make friends.{/i}"
            "{i}The vendor watches him pass. Doesn't call out again.{/i}"

    # VISUAL: A drone sweeps past; the light skims and moves on. Even the machines look tired here.
    "{i}A drone sweeps past; the light skims and moves on. Even the machines look tired here.{/i}"
    a "{i}Eyes are everywhere. People don't bow. They keep moving.{/i}"

    # VISUAL: A small figure darts between pipes—child, maybe eight or nine, ragged clothes.
    # SOUND: Quick footsteps; something metallic clatters.

    "{i}Movement—quick, low to the ground. A child slips between the pipes.{/i}"

    # VISUAL: The child stops, stares at Aeron's uniform—recognition and fear.
    child "(freezes) ...You're one of them."

    # VISUAL: Aeron stops walking; turns slightly toward the child.
    a "One of who?"
    child "Echelon. The ones that took my dad."

    # VISUAL: The child's hand grips a bent pipe—ready to run.
    "{i}Small hands. Dirty knuckles. Eyes too old for the face.{/i}"

    # ACTION: Player choice—how does Aeron respond?
    menu:
        "The child's breath fogs the air between them."
        "Try to reassure the child.":
            $ aeron_reassured_child = True
            a "(crouches slightly, non-threatening) I'm not here for that."
            child "(suspicious) Then what're you here for?"
            a "...I don't know yet."
            child "(pauses) You look sad."
            a "(caught off guard) What?"
            child "Soldiers don't usually look sad. They just look mean."
            a "(quiet) Maybe I'm tired of looking mean."
            child "Are you gonna cry? My dad cried before they took him."
            a "(quiet) ...No. I'm not gonna cry."
            
            # VISUAL: The child tilts their head—considering.
            child "My dad said some soldiers still got hearts. Before they took him."
            a "Where did they take him?"
            child "(shrugs) Dunno. He didn't come back."
            
            "{i}The words settle like ash.{/i}"
            a "{i}How many stories like this are there? How many I'll never hear?{/i}"
            
            child "You gonna take people too?"
            a "(honestly) I hope not."
            child "(nods slowly) ...Okay."
            
            # VISUAL: The child backs away, still cautious, then disappears into the maze of pipes.
            "{i}Gone. Like smoke.{/i}"

        "Say nothing and keep walking.":
            $ aeron_reassured_child = False
            "{i}He says nothing. What could he say?{/i}"
            child "(bitter) Yeah. That's what I thought."
            
            # VISUAL: The child spits on the ground near Aeron's feet—not close enough to hit, but the message is clear.
            "{i}The child vanishes into shadow. The contempt lingers.{/i}"
            a "{i}Can't blame them. I'd spit too.{/i}"

    "{i}He stops at a railing; far below, scattered fires stubborn as stars.{/i}"
    a "{i}No spires. No chandeliers. Just humanity, unpolished.{/i}"

    # VISUAL: Below—a makeshift courtyard; people gathered around barrel fires.
    # SOUND: Faint laughter; someone playing a broken stringed instrument; voices layered.
    "{i}Below, people gather around barrel fires. Laughter rises through the steam.{/i}"
    "{i}Someone plays a broken guitar. The notes are wrong, but no one cares.{/i}"

    # VISUAL: A couple shares a meal from a single container; an old man tells a story to children.
    "{i}A couple shares food from a dented tin. An old man spins a story for kids who lean in close.{/i}"
    a "{i}They have nothing. And somehow, they have everything I don't.{/i}"

    # VISUAL: One of the children points up—sees Aeron silhouetted against the higher lights.
    # SOUND: The guitar stops briefly; conversation quiets.
    "{i}A child points up. The music stops. Eyes find him in the dark.{/i}"

    # ACTION: Player choice—acknowledge them or retreat.
    menu:
        "They watch him. Waiting."
        "Nod in acknowledgment.":
            $ aeron_acknowledged_unders = True
            # VISUAL: Aeron lifts his hand slightly—not a wave, just recognition.
            "{i}He lifts his hand. Just slightly. Not a threat. Just... acknowledgment.{/i}"
            "{i}After a beat, the old man nods back. The guitar resumes.{/i}"
            a "{i}Not forgiveness. Not trust. But not hatred either.{/i}"
            a "{i}It's more than I deserve.{/i}"
            
        "Step back into shadow.":
            $ aeron_acknowledged_unders = False
            "{i}He steps back. Out of the light. Out of sight.{/i}"
            "{i}The guitar picks up again. Life continues without him.{/i}"
            a "{i}I don't belong down here. I don't belong anywhere.{/i}"

    "{i}Steam coils from vents, wrapping steel like roots.{/i}"
    a "{i}This edge is a mirror. Everyone's running from something.{/i}"
    a "{i}Me too.{/i}"

    "{i}A siren wails somewhere far. No one flinches. Noise is weather.{/i}"
    "{i}A buzzing sign: half the letters dead; the rest refusing to quit.{/i}"
    a "{i}Maybe this place isn't forgotten. Maybe it's just waiting to be remembered.{/i}"

    "{i}Wind carries rain and iron. The lights dip, then steady.{/i}"

    "{i}He keeps walking. Deeper into the shadows.{/i}"
    "{i}Looking for answers. Or trouble. Maybe both.{/i}"

    return