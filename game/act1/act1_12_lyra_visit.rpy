# ======================================================
# ACT 1 - Scene 12: Lyra's Visit (Empathy-Integrated)
# File: act1_12_lyra_visit.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_12_lyra_visit"
$ scene_mark(_current_scene_id, "entered")


label act1_lyra_visit:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Over-shoulder reveals; two-shots in profile; window reflection CUs.
    # LIGHTING: Corridor spill warm; interior cooler cyan from skyline; slow moving city strip.
    # SFX LOOP: Distant city wind through facade fins; building ventilation hush; muffled traffic.
    # BLOCKING: Door frame left; balcony door cracked open right; faint ash ribbon drifting inward.
    # FX/COMP: Neon wash (cyan/pink) across floor; condensation on window.

    #scene bg_bedroom_night_lyra with fade

    # ========= OPENING — THE KNOCK =========

    "Another knock. Softer. Patient."

    athought "...Lyra?"

    "He crosses the room and opens the door."

    # VISUAL: Over-shoulder on Aeron; reveal Lyra in corridor half-profile. Warm rim on her, cool backlight on him.

    l "You look like hell."

    a "(tries a smile) You should see the other guy."

    "The joke dies halfway out. Her smile doesn't reach her eyes."

    athought "She didn't come for laughter. She came because silence was worse."

    l "(arches a brow) Not amusing."

    l "Something in you is breaking. Badly."

    a "How did you know I'd be—"

    l "Because I know what breaking looks like."

    l "I thought you'd be asleep. Or at least pretending."

    a "Sleep is a luxury."

    l "So is standing on rooftop edges."

    a "(freezes) You saw."

    l "I see everything, Aeron. Especially when you think no one is watching."

    # VISUAL: Lyra glides past; perches on desk corner; keeps him in peripheral.

    l "(perches on the desk) I needed out of that gala. All those smiles felt like knives."

    "He lights her cigarette. Their fingers brush."

    a "(quietly) Thanks for knocking."

    l "(studies him) You're shaking."

    a "Cold air. Nothing more."

    l "You don't shake from cold. You shake when you're about to shatter."

    "Silence settles—thin, tight."

    # VISUAL: Two-shot in profile; balcony haze behind.

    # ========= EMPATHY VARIATION — AERON'S GUARDEDNESS =========
    # LIGHTING: OB-hard keeps him in silhouette; mid adds faint fill; EMP gets soft rim off skyline.

    if pass_tier("OB3", "OB2"):
        athought "Connection is inefficiency. She should've stayed away."
    elif pass_tier("OB1", "NEU"):
        athought "Part of me wants her to leave. Part of me doesn't."
    else:
        athought "Her voice sounds like the first warm thing I've heard in years."

    # ========= LYRA PRESSES =========

    l "You don't have to keep doing this."

    a "Doing what?"

    l "Carrying everything alone. Pretending you're made of stone."

    l "Pretending you're a window people can just look through."

    "Her words land heavier than she knows."

    a "(looks away) Stones don't crack. People do."

    l "(softly) Windows crack too. And you're not a window, Aeron."

    a "Everyone says I am. Father made me one."

    l "Your father tried. There's a difference."

    l "Windows don't stand on edges wondering if they should fall."

    l "Windows don't shake. Windows don't question. Windows don't feel."

    l "(steps closer) And you... you feel everything."

    "Neon washes the room; neither speaks for a beat."

    # FX: Slow moving cyan/pink spill across floor.

    a "390 operations. Ten years of being transparent."

    a "When did I start feeling it again?"

    l "Perhaps you never stopped. Perhaps you were just very good at lying to yourself."

    # ========= PLAYER CHOICE — INVITE OR DISMISS =========

    menu:
        athought "She's offering presence. I could take it or push it away."

        "Tell her to leave":
            $ choice_and_dev(
                _current_scene_id, "lyra_visit_tell_leave", "OB", factor=1,
                note="Pushes Lyra away; preserves mask; OB-lean."
            )
            $ scene_mark(_current_scene_id, "told_her_to_leave")

            a "It's late. You shouldn't be here."

            l "(contained) Right. Forget I knocked."

            "She hesitates; looks back once."

            l "Windows recognize windows, Aeron. We see each other."

            l "And I see you breaking. That is not weakness. That is waking up."

            "The door clicks. Quiet returns."

            athought "She sees it. The cracks. The breaking."

            athought "Maybe that's why she came."

            # VISUAL: Corridor warm spill disappears; room cools another notch.

        "Let Lyra stay":
            $ choice_and_dev(
                _current_scene_id, "lyra_visit_let_stay", "EMP", factor=1,
                note="Allows proximity; admits need; EMP-lean."
            )
            $ rel_bump("Lyra", 1)
            $ scene_mark(_current_scene_id, "let_her_stay")

            a "(after a beat) Sit, then."

            l "(moves to the edge of the bed) Better."

            a "Not sure what's better about it."

            l "You're still here. That's better."

            l "A weapon would've already shattered. You haven't."

            "The city hum fades; slower quiet replaces it."

            # SFX: Wind dips 3 dB; room tone closer.

            # ========= EMPATHY VARIATION — TONE OF CONNECTION =========

            if pass_tier("OB3", "OB2"):
                athought "This is proximity, not comfort. I know the difference."
            elif pass_tier("OB1", "NEU"):
                athought "I should tell her to go. I don't."
            else:
                athought "For the first time, being seen doesn't hurt."

            a "You ever wonder if any of this means anything?"

            l "(arches a brow) Define 'this.'"

            a "Solveil. Echelon. The theater we keep playing."

            l "(dry) Only every waking moment."

            "He almost laughs. It dies halfway out."

            a "You're lucky. They see purpose when they look at you."

            l "(faint) You think that's luck?"

            a "Isn't it?"

            l "They don't see me. They see what they built. A weapon in a dress."

            l "Transparent in a different shape. Same emptiness."

            "Her hands fold, unfold—a rare break in composure."

            a "Where were you? Before tonight, I mean. You said you were on assignment."

            l "(pause) Sector Seven. Compliance audit."

            a "That's... vague."

            l "(looks at him directly) It was meant to be."

            "She stands, moves to the window. Puts space between them like armor."

            l "They sent me to evaluate a residential block. Efficiency metrics. Loyalty indexes."

            a "Sounds routine."

            l "It was. Until I found the children."

            # VISUAL: Her reflection fractures in the condensation-slick window.

            a "(carefully) What children?"

            l "Unregistered. Hidden in the sublevels. Families who couldn't afford the Branding fees."

            l "They were... surviving. That's all. Just surviving."

            a "What did you do?"

            l "(quiet) What I was ordered to do. I logged their locations. Submitted the report."

            a "Lyra—"

            l "(cuts him off) Three days later, that block was rezoned. Everyone relocated. The children... disappeared into the system."

            "Her shoulders tighten. She doesn't turn around."

            l "I told myself it was necessary. That the system knows better than I do."

            l "But I can't stop seeing their faces."

            l "I am transparent too, Aeron. Empty. Obedient."

            l "And something in me is cracking."

            a "(softly) That's because you're not a weapon. You're a person."

            l "Am I? Am I really?"

            "She turns. Eyes meet. Distance shrinks without either moving."

            l "Sometimes I'm not sure where the orders end and I begin."

            a "I know the feeling."

            l "Of course you do. Windows recognize windows."

            # WEATHER GRAMMAR: Pressure thrum, not rain.

            "Wind presses against the facade; the world narrows to this room."

            l "When I was at the door... you hesitated before opening it."

            a "I didn't expect anyone."

            l "Were you hoping I wouldn't come?"

            a "(pause) No. I was hoping you would."

            l "Then why do you look like you wish I hadn't?"

            a "Because I don't know what happens next."

            a "We're both cracking. What happens when we both shatter?"

            l "Perhaps we find out what was underneath all along."

            "She moves. Sits beside him. Close enough to feel the warmth."

            l "Then say nothing. Just... don't be alone tonight."

            a "(voice rough) Lyra, I—"

            "The words lodge in his throat. Too big. Too true."

            l "(gently) What?"

            a "I don't know how to do this. Any of this."

            l "Do what?"

            a "Feel things I'm not supposed to feel. Want things I can't have."

            a "I'm not supposed to want. I'm supposed to just reflect."

            a "But I want... I want to be more than what they made me."

            l "(barely a whisper) Who says you can't?"

            "The space between them disappears. Almost touching. Almost."

            a "(standing abruptly) You should rest. It's late."

            l "(hurt flickers, then hides) Right. Of course."

            "She stands. Composure slides back into place like a mask."

            l "Both of us. Both afraid to touch."

            l "For what it's worth..."

            a "Yeah?"

            l "I'm glad you're still here. Even if you don't believe it matters."

            a "It matters because you said so."

            l "(soft smile) Then remember I said it."

            a "You should rest."

            l "And you?"

            a "I don't sleep much."

            l "Neither do I. Weapons don't need rest."

            l "But people do. And we are still people, Aeron."

            l "Even if we've forgotten how to be."

            l "(soft) Maybe fate is who shows up when it's darkest."

            a "You think you're fate, then?"

            l "(tiny smile) Maybe. Or maybe I just knock loudly."

            l "Or maybe... two people break better together than alone."

            "She's gone. The room feels different now—lighter, or maybe just less empty."

            athought "Windows recognize windows."

            athought "And maybe... maybe we can break together."

            athought "Find out what's underneath. What we used to be. What we could still become."

            scene black with fade

    $ scene_mark(_current_scene_id, "completed")
    $ rel_bump("Lyra", 1)  # visit itself increases trust

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_12_lyra_visit
# cann.when_in_timeline: Immediately after Breaking Point; same night; pre–Sector 10 departure.
# cann.what_happened:
#   - Lyra checks on Aeron after rooftop brink; names the crack; offers presence.
#   - Player either pushes her away (OB-lean) or lets her stay (EMP-lean); deeper talk if she stays.
#   - Sector Seven "children audit" confession seeds Act I empathy spine + Echelon cost.
# cann.aeron_state: Alignment tints VO only. OB = guarded/clinical; mid = ambivalent; EMP = receptive.
# cann.path_tracking:
#   - Menu weights: Leave → OB(+1); Stay → EMP(+1). 
#   - Scene delta range: −1 → +1.
#   - Flags: told_her_to_leave / let_her_stay / completed.
#   - Social: rel_bump +1 if stay; rel_bump +1 baseline for visit.
# cann.thematic_flags: Transparent vs Person; presence over doctrine; "waking up" vs "weakness."
# cann.block_status: VARIANT (two-route scene; extended content if stay).
# cann.visual_plate_economy:
#   - REUSE: Bedroom night master; corridor spill toggle; balcony haze plate.
#   - HERO: Desk-perch two-shot; condensation-slick window reflection CU; finger-brush on lighter.
# cann.requires_followup:
#   - If told_her_to_leave: colder tone in next morning prep; lower early Act II openness.
#   - If let_her_stay: unlocks warmer micro-beats in Sector 10 prep + future rooftop callback.