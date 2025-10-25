# act_12_lyra_visit.rpy


# ======================================================
# ACT 1 - Scene 12: Lyra's Visit (Empathy-Integrated)
# ======================================================


label act1_lyra_visit:
    $ scene_id = "act1_12_lyra_visit"

    # Precompute alignment reads for light flavor only (no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    # empathy side = else

    # VISUAL: Door in frame left; balcony open; ash thread in air.
    # SOUND: Room hush; distant gala muffled by height.

    "{i}Another knock. Softer. Patient.{/i}"
    a "{i}...Lyra?{/i}"
    "{i}He crosses the room and opens the door.{/i}"

    # LIGHTING: Corridor spill on Lyra; interior cooler.
    l "You look like hell."
    a "(tries a smile) You should see the other guy."
    a "{i}The joke falls flat. Her smile doesn't reach her eyes.{/i}"
    a "{i}She didn't come for me. She came because she couldn't be alone.{/i}"
    l "(arches a brow) Not amusing."
    l "Glass is cracking. Badly."
    a "How did you know I'd be—"
    l "Because I know what breaking looks like."

    l "I thought you'd be asleep. Or at least pretending."
    a "Sleep is a luxury."
    l "So is standing on rooftop edges."
    a "(freezes) You saw."
    l "I see everything, Aeron. Especially when Glass thinks no one is watching."

    l "(perches on the desk) I needed out of that gala. All those smiles felt like knives."
    "{i}He lights her cigarette. Their fingers brush.{/i}"
    a "(quietly) Thanks for knocking."
    l "(studies him) You're shaking."
    a "Cold air. Nothing more."
    l "Glass doesn't shake from cold. Glass shakes when it's about to shatter."

    "{i}Silence settles—thin, tight.{/i}"

    # ------------------------------------------------------
    # EMPATHY VARIATION — Aeron's guardedness
    # ------------------------------------------------------
    if is_ob_hard:
        a "{i}Connection is inefficiency. She should've stayed away.{/i}"
    elif is_mid:
        a "{i}Part of me wants her to leave. Part of me doesn't.{/i}"
    else:
        a "{i}Her voice sounds like the first warm thing I've heard in years.{/i}"
    # ------------------------------------------------------

    l "You don't have to keep doing this."
    a "Doing what?"
    l "Carrying everything alone. Pretending you're made of stone."
    l "Pretending you're made of Glass."
    a "{i}Her words land heavier than she knows.{/i}"
    a "(looks away) Stones don't crack. People do."
    l "(softly) Glass cracks too. And you're not Glass, Aeron."
    a "Everyone says I am. Father made me Glass."
    l "Your father tried to make you Glass. There's a difference."
    l "Glass doesn't stand on edges wondering if it should fall."
    l "Glass doesn't shake. Glass doesn't question. Glass doesn't feel."
    l "(steps closer) And you... you feel everything."

    "{i}Neon washes the room; neither speaks for a beat.{/i}"

    a "390 operations. Ten years of being Glass."
    a "When did I start feeling it again?"
    l "Perhaps you never stopped. Perhaps you were just very good at lying to yourself."

    # ======================================================
    # PLAYER CHOICE — Invite or Dismiss Lyra
    # ======================================================
    menu:
        "Tell her to leave":
            $ set_scene_flag(scene_id, "told_her_to_leave")

            a "It's late. You shouldn't be here."
            l "(contained) Right. Forget I knocked."
            "{i}She hesitates; looks back once.{/i}"
            l "Glass and glass, Aeron. We recognize each other."
            l "And I see you breaking. That is not weakness. That is waking up."
            "{i}The door clicks. Quiet returns.{/i}"
            a "{i}She sees it. The cracks. The breaking.{/i}"
            a "{i}Maybe that's why she came.{/i}"

        "Let Lyra stay":
            $ add_affection("Lyra", 1)
            $ set_scene_flag(scene_id, "let_her_stay")

            a "(after a beat) Sit, then."
            l "(moves to the edge of the bed) Better."
            a "Not sure what's better about it."
            l "You're still here. That's better."
            l "Glass would've already shattered. You haven't."

            "{i}The city hum fades; slower quiet replaces it.{/i}"

            # ------------------------------------------------------
            # EMPATHY VARIATION — Tone of connection
            # ------------------------------------------------------
            if is_ob_hard:
                a "{i}This is proximity, not comfort. I know the difference.{/i}"
            elif is_mid:
                a "{i}I should tell her to go. I don't.{/i}"
            else:
                a "{i}For the first time, being seen doesn't hurt.{/i}"
            # ------------------------------------------------------

            a "You ever wonder if any of this means anything?"
            l "(arches a brow) Define 'this.'"
            a "Solveil. Echelon. The theater we keep playing."
            l "(dry) Only every waking moment."
            a "{i}He almost laughs. It dies halfway out.{/i}"

            a "You're lucky. They see purpose when they look at you."
            l "(faint) You think that's luck?"
            a "Isn't it?"
            l "They don't see me. They see what they built. A weapon in a dress."
            l "Glass in a different shape. Same emptiness."

            "{i}Her hands fold, unfold. A rare break in composure.{/i}"

            a "Where were you? Before tonight, I mean. You said you were on assignment."
            l "(pause) Sector Seven. Compliance audit."
            a "That's... vague."
            l "(looks at him directly) It was meant to be."

            "{i}She stands. Moves to the window. Puts space between them like armor.{/i}"
            l "They sent me to evaluate a residential block. Efficiency metrics. Loyalty indexes."
            a "Sounds routine."
            l "It was. Until I found the children."

            "{i}Her reflection fractures in the rain-streaked glass.{/i}"
            a "(carefully) What children?"
            l "Unregistered. Hidden in the sublevels. Families who couldn't afford the Branding fees."
            l "They were... surviving. That's all. Just surviving."
            a "What did you do?"
            l "(quiet) What I was ordered to do. I logged their locations. Submitted the report."
            a "Lyra—"
            l "(cuts him off) Three days later, that block was rezoned. Everyone relocated. The children... disappeared into the system."

            "{i}Her shoulders tighten. She doesn't turn around.{/i}"
            l "I told myself it was necessary. That the system knows better than I do."
            l "But I can't stop seeing their faces."
            l "I am Glass too, Aeron. Transparent. Empty. Obedient."
            l "And Glass is cracking."

            a "(softly) That's because you're not a weapon. You're a person."
            l "Am I? Am I really?"
            "{i}She turns. Eyes meet. Distance shrinks without either moving.{/i}"
            l "Am I? Sometimes I'm not sure where the orders end and I begin."
            a "I know the feeling."
            l "Of course you do. Glass recognizes glass."

            "{i}Rain hammers the glass. The world narrows to this room.{/i}"

            l "When I was at the door... you hesitated before opening it."
            a "I didn't expect anyone."
            l "Were you hoping I wouldn't come?"
            a "(pause) No. I was hoping you would."
            l "Then why do you look like you wish I hadn't?"
            a "Because I don't know what happens next."
            a "We're both Glass. Both cracking. What happens when we both shatter?"
            l "Perhaps we find out what was underneath all along."

            "{i}She moves. Sits beside him. Close enough to feel the warmth.{/i}"
            l "Then say nothing. Just... don't be alone tonight."
            a "(voice rough) Lyra, I—"
            "{i}The words lodge in his throat. Too big. Too true.{/i}"
            l "(gently) What?"
            a "I don't know how to do this. Any of this."
            l "Do what?"
            a "Feel things I'm not supposed to feel. Want things I can't have."
            a "Glass isn't supposed to want. Glass just reflects."
            a "But I want... I want to be more than Glass."
            l "(barely a whisper) Who says you can't?"

            "{i}The space between them disappears. Almost touching. Almost.{/i}"
            a "(standing abruptly) You should rest. It's late."
            l "(hurt flickers, then hides) Right. Of course."
            "{i}She stands. Composure slides back into place like a mask.{/i}"
            l "Glass to glass again. Both afraid to touch."

            l "For what it's worth..."
            a "Yeah?"
            l "I'm glad you're still here. Even if you don't believe it matters."
            a "It matters because you said so."
            l "(soft smile) Then remember I said it."

            a "You should rest."
            l "And you?"
            a "I don't sleep much."
            l "Neither do I. Glass doesn't need rest."
            l "But people do. And we are still people, Aeron."
            l "Even if we've forgotten how to be."

            l "(soft) Maybe fate is who shows up when it's darkest."
            a "You think you're fate, then?"
            l "(tiny smile) Maybe. Or maybe I just knock loudly."
            l "Or maybe... two pieces of glass break better together than alone."

            "{i}She's gone. The room feels different now.{/i}"
            "{i}Lighter. Or maybe just less empty.{/i}"
            a "{i}Glass recognizes glass.{/i}"
            a "{i}And maybe... maybe we can break together.{/i}"
            a "{i}Find out what's underneath. What we used to be. What we could still become.{/i}"

    # ======================================================
    # SCENE FLAGS
    # ======================================================
    $ set_scene_flag(scene_id, "completed")
    $ add_trust("Lyra", 1)

    # canon_notes:
    # - Mirrors Breaking Point emotional recovery
    # - Empathy tones: low = efficiency, mid = hesitation, high = connection
    # - Establishes Lyra as emotional counterbalance to Marcus
    # - Scene flags: told_her_to_leave / let_her_stay / completed
    # - Affects early Act 2 trust dialogue

    return
