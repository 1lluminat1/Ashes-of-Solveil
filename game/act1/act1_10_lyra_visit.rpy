# act1_10_lyra_visit.rpy


# ======================================================
# ACT 1 - Scene 10: Lyra's Visit
# ======================================================


label act1_lyra_visit:
    # After the balcony scene where Aeron almost stepped off:
    # Knock at the door. Cigarette trembles in his fingers.
    #play sound "knock.ogg"
    "{i}A knock at the door—sharp, sudden.{/i}"
    a "{i}...Lyra?{/i}"

    # He steps off the railing, still shaken. Opens the door.
    "{i}A knock at the door—sharp, sudden.{/i}"
    a "{i}...Lyra?{/i}"

    "{i}He steps off the rail and opens the door.{/i}"

    l "You look like hell."
    a "(forces a half-smile) You should see the other guy."
    l "(arches a brow) Not funny."

    "{i}She steps in without waiting. Her gaze lands on the photo, then his empty wrist. She says nothing.{/i}"

    l "I thought you’d be asleep. Or at least pretending."
    a "Sleep’s a luxury these days."

    l "(perches on the desk) I needed out of that gala. All those smiles felt like knives."
    "{i}He lights her cigarette. Their fingers brush.{/i}"
    a "(quietly) Thanks for knocking."
    l "(studies him) You’re shaking."
    a "Cold air. Nothing more."

    "{i}Silence settles—thin, tight.{/i}"

    l "You don’t have to keep doing this."
    a "Doing what?"
    l "Carrying everything alone. Pretending you’re made of stone."
    a "{i}Her words land heavier than she knows.{/i}"
    a "(looks away) Stones don’t crack. People do."
    l "(softly) You’re not your father, Aeron."

    "{i}For a long moment, neither of them speaks. The city hums beyond the glass, neon washing the room.{/i}"

    # Choice — let her in or not
    menu:
        "Tell her to leave":
            a "It’s late. You shouldn’t be here."
            l "(hurt, contained) Right. Forget I knocked."
            "{i}She turns for the door, hesitates, looks back once.{/i}"
            l "You’re still here. That’s something."
            "{i}The door clicks. Quiet returns.{/i}"

        "Let Lyra stay":
            a "(after a beat) Sit, then."
            l "(moves to the edge of the bed) Better."
            a "Not sure what’s better about it."
            l "You’re still here. That’s better."
            a "{i}She says it like a fact.{/i}"

            "{i}The hum of the city fades to the background—replaced by a slower kind of quiet.{/i}"

            a "(sighs) You ever wonder if any of this means anything?"
            l "(arches a brow) Define ‘this.’"
            a "Solveil. Echelon. The theater we keep playing."
            l "(dry) Only every waking moment."

            "{i}He almost laughs. It dies halfway out.{/i}"

            a "You’re lucky, though. They look at you and see purpose."
            l "(faint smirk) You think that’s luck?"
            a "Isn’t it?"
            l "They don’t see me. They see what they built. A weapon in a pretty dress."

            "{i}No bitterness—just the same kind of tired he knows too well.{/i}"

            a "You ever want to disappear?"
            l "Every day."
            a "(quietly) Me too."

            "{i}The words hang there like a confession.{/i}"

            l "(softly) You know what the funny part is?"
            a "What?"
            l "If either of us vanished, they’d replace us by morning. Another soldier. Another heir."
            a "Another ghost in the machine."
            l "(faint smile) Exactly."
            "{i}It fades as quickly as it came.{/i}"

            l "Sometimes I wonder if that’s freedom or just another kind of death."
            a "{i}Something in her voice wavers, then steadies.{/i}"
            a "Maybe it’s both."

            "{i}Their eyes meet. Not searching for comfort—just understanding.{/i}"
            "{i}A gust slips through the cracked balcony door, brushes past, and is gone.{/i}"

            a "You should rest. You’ve been running since you got back."
            l "And you?"
            a "I don’t sleep much."
            l "Then we’ll call this even."

            "{i}She shifts to lean against the wall by his desk, half-turned to the skyline.{/i}"

            l "(soft) Maybe fate isn’t what’s written. Maybe it’s who shows up when it’s darkest."
            a "(meets her gaze) You think you’re fate, then?"
            l "(tiny smile) Maybe. Or maybe I just knock loud enough."

            "{i}For a moment, the air between them softens, then settles again.{/i}"

            l "I should go before someone notices."
            a "They’d notice you before me."
            l "Maybe that’s why I came here."

            "{i}She pauses at the door. Neon outlines her silhouette.{/i}"
            l "Try not to fall apart before I get back."
            a "(faint smirk) No promises."

            "{i}Her quiet laugh lingers after she’s gone.{/i}"
            "{i}For the first time in years, he doesn’t feel completely alone.{/i}"

    return