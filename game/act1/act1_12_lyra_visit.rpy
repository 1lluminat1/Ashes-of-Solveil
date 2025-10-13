# act1_12_lyra_visit.rpy


# ======================================================
# ACT 1 - Scene 12: Lyra's Visit
# ======================================================


label act1_lyra_visit:
    # VISUAL: Door in frame left; balcony open; ash thread in air.
    # SOUND: Room hush; distant gala muffled by height.

    # SOUND: Another knock. Softer. Patient.
    a "{i}...Lyra?{/i}"
    "{i}He crosses the room towards the door and opens it.{/i}"

    # LIGHTING: Corridor spill on Lyra; interior cooler.
    l "You look like hell."
    a "(tries a smile) You should see the other guy."
    l "(arches a brow) Not amusing."

    # CAMERA: Over-shoulder on Lyra; she clocks the photo and bare wrist.
    l "I thought you would be asleep. Or at least pretending."
    a "Sleep is a luxury."

    # PROP: Cigarette pass + touch; micro beat on hands.
    l "(perches on the desk) I needed out of that gala. All those smiles felt like knives."
    "{i}He lights her cigarette. Their fingers brush.{/i}"
    a "(quietly) Thanks for knocking."
    l "(studies him) You're shaking."
    a "Cold air. Nothing more."

    "{i}Silence settles—thin, tight.{/i}"

    l "You don't have to keep doing this."
    a "Doing what?"
    l "Carrying everything alone. Pretending you're made of stone."
    a "{i}Her words land heavier than she knows.{/i}"
    a "(looks away) Stones don't crack. People do."
    l "(softly) You're not your father, Aeron."

    "{i}Neon washes the room; neither speaks for a beat.{/i}"

    menu:
        "Tell her to leave":
            $ lyra_rel -= 1
            # BLOCKING: Lyra turns; slight pause at threshold.
            a "It's late. You shouldn't be here."
            l "(contained) Right. Forget I knocked."
            "{i}She hesitates; looks back once.{/i}"
            l "You're still here. That's something."
            "{i}The door clicks. Quiet returns.{/i}"

        "Let Lyra stay":
            $ lyra_rel += 1
            # BLOCKING: She sits edge of bed; posture still formal.
            a "(after a beat) Sit, then."
            l "(moves to the edge of the bed) Better."
            a "Not sure what's better about it."
            l "You're still here. That's better."

            "{i}The city hum fades; slower quiet replaces it.{/i}"

            a "You ever wonder if any of this means anything?"
            l "(arches a brow) Define 'this.'"
            a "Solveil. Echelon. The theater we keep playing."
            l "(dry) Only every waking moment."

            "{i}He almost laughs. It dies halfway out.{/i}"

            a "You're lucky. They see purpose when they look at you."
            l "(faint) You think that's luck?"
            a "Isn't it?"
            l "They don't see me. They see what they built. A weapon in a dress."

            "{i}Same tired he knows too well—without bitterness.{/i}"

            # VISUAL: Lyra's hands fold in her lap; fingers interlace, then release.
            "{i}Her hands fold, unfold. A rare break in composure.{/i}"

            a "Where were you? Before tonight, I mean. You said you were on assignment."
            l "(pause) Sector Seven. Compliance audit."
            a "That's... vague."
            l "(looks at him directly) It was meant to be."

            # VISUAL: She stands, walks to the window; puts distance between them.
            "{i}She stands. Moves to the window. Puts space between them like armor.{/i}"

            l "They sent me to evaluate a residential block. Efficiency metrics. Loyalty indexes."
            a "Sounds routine."
            l "It was. Until I found the children."

            # VISUAL: Her reflection in the window—face half-lit, half in shadow.
            "{i}Her reflection fractures in the rain-streaked glass.{/i}"

            a "(carefully) What children?"
            l "Unregistered. Hidden in the sublevels. Families who couldn't afford the Branding fees."
            l "They were... surviving. That's all. Just surviving."
            a "What did you do?"
            l "(quiet) What I was ordered to do. I logged their locations. Submitted the report."
            a "Lyra—"
            l "(cuts him off) Three days later, that block was rezoned. Everyone relocated. The children... disappeared into the system."

            # VISUAL: She closes her eyes; jaw tight.
            "{i}Her shoulders tighten. She doesn't turn around.{/i}"

            l "I told myself it was necessary. That the system knows better than I do."
            l "But I can't stop seeing their faces."
            a "(softly) That's because you're not a weapon. You're a person."

            # VISUAL: She turns—eyes meeting his across the room.
            "{i}She turns. Eyes meet. Distance shrinks without either moving.{/i}"

            l "Am I? Sometimes I'm not sure where the orders end and I begin."
            a "I know the feeling."

            # VISUAL: Silence; rain intensifies outside.
            "{i}Rain hammers the glass. The world narrows to this room.{/i}"

            l "When I was at the door... you hesitated before opening it."
            a "I didn't expect anyone."
            l "Were you hoping I wouldn't come?"
            a "(pause) No. I was hoping you would."
            l "Then why do you look like you wish I hadn't?"
            a "Because I don't know what happens next."
            l "Does something have to happen?"
            a "...I don't know."

            # VISUAL: She crosses back to him; sits beside him on the bed—closer than before.
            "{i}She moves. Sits beside him. Close enough to feel the warmth.{/i}"

            l "Then say nothing. Just... don't be alone tonight."
            a "(voice rough) Lyra, I—"

            # VISUAL: The words catch; he looks at her, something breaking in his expression.
            "{i}The words lodge in his throat. Too big. Too true.{/i}"

            l "(gently) What?"
            a "I don't know how to do this. Any of this."
            l "Do what?"
            a "Feel things I'm not supposed to feel. Want things I can't have."
            l "(barely a whisper) Who says you can't?"

            # VISUAL: Their faces inches apart; breath visible in the cold air.
            "{i}The space between them disappears. Almost touching. Almost.{/i}"

            # VISUAL: Aeron pulls back—just slightly; breaks the moment.
            a "(standing abruptly) You should rest. It's late."
            l "(hurt flickers, then hides) Right. Of course."

            # VISUAL: She stands; smooths her dress—composure rebuilt in seconds.
            "{i}She stands. Composure slides back into place like a mask.{/i}"

            l "For what it's worth..."
            a "Yeah?"
            l "I'm glad you're still here. Even if you don't believe it matters."
            a "It matters because you said so."
            l "(soft smile) Then remember I said it."

            # OPTIONAL: Could cut the "disappear" exchange and jump straight to:
            a "You should rest."
            l "And you?"
            a "I don't sleep much."
            l "Then we call this even."

            # EXIT: She pauses; silhouette edged by corridor neon.
            l "(soft) Maybe fate is who shows up when it's darkest."
            a "You think you're fate, then?"
            l "(tiny smile) Maybe. Or maybe I just knock loudly."

            "{i}She's gone. The room feels different now.{/i}"
            "{i}Lighter. Or maybe just less empty.{/i}"

    return