# ======================================================
# ACT 1 - Scene 12: Lyra's Visit (Empathy-Integrated)
# File: act1_12_lyra_visit.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_12_lyra_visit"
$ scene_mark(_current_scene_id, "entered")


label act1_lyra_visit:

    # Precompute alignment reads for light flavor only (no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    # empathy side = else

    # VISUAL: Door frame left; balcony door cracked open frame right; faint ash ribbon drifting inward.
    # LIGHTING: Corridor spill warm; interior cooler cyan from skyline; slow moving city strip across floor.
    # SFX: Distant city wind through facade fins; building ventilation hush; muffled high-tier traffic.

    "Another knock. Softer. Patient."

    athought "...Lyra?"

    "He crosses the room and opens the door."
    # CAMERA: Over-shoulder on Aeron; reveal Lyra in corridor half-profile.

    # LIGHTING: Warm corridor rim on Lyra; Aeron in cooler backlight.
    l "You look like hell."
    a "(tries a smile) You should see the other guy."

    "The joke dies halfway out. Her smile doesn't reach her eyes."
    "She didn’t come for laughter. She came because silence was worse."

    l "(arches a brow) Not amusing."
    l "Glass is cracking. Badly."
    a "How did you know I'd be—"
    l "Because I know what breaking looks like."

    l "I thought you'd be asleep. Or at least pretending."
    a "Sleep is a luxury."
    l "So is standing on rooftop edges."
    a "(freezes) You saw."
    l "I see everything, Aeron. Especially when Glass thinks no one is watching."

    # BLOCKING: Lyra glides past; perches on desk corner; keeps him in peripheral.
    l "(perches on the desk) I needed out of that gala. All those smiles felt like knives."

    "He lights her cigarette. Their fingers brush."

    a "(quietly) Thanks for knocking."
    l "(studies him) You're shaking."
    a "Cold air. Nothing more."
    l "Glass doesn't shake from cold. Glass shakes when it's about to shatter."

    "Silence settles—thin, tight."

    # CAMERA: Two-shot in profile; balcony haze behind.

    # ---------- EMPATHY VARIATION — Aeron's guardedness ----------
    # LIGHTING: OB-hard keeps him in silhouette; mid adds faint fill; empathy gets a soft rim off the skyline.
    if is_ob_hard:
        athought "Connection is inefficiency. She should've stayed away."
    elif is_mid:
        athought "Part of me wants her to leave. Part of me doesn't."
    else:
        athought "Her voice sounds like the first warm thing I've heard in years."
    # -------------------------------------------------------------

    l "You don't have to keep doing this."
    a "Doing what?"
    l "Carrying everything alone. Pretending you're made of stone."
    l "Pretending you're made of Glass."

    "Her words land heavier than she knows."

    a "(looks away) Stones don't crack. People do."
    l "(softly) Glass cracks too. And you're not Glass, Aeron."
    a "Everyone says I am. Father made me Glass."
    l "Your father tried to make you Glass. There's a difference."
    l "Glass doesn't stand on edges wondering if it should fall."
    l "Glass doesn't shake. Glass doesn't question. Glass doesn't feel."
    l "(steps closer) And you... you feel everything."

    "Neon washes the room; neither speaks for a beat."

    # FX: Slow moving cyan/pink spill across floor.

    a "390 operations. Ten years of being Glass."
    a "When did I start feeling it again?"
    l "Perhaps you never stopped. Perhaps you were just very good at lying to yourself."

    # ======================================================
    # PLAYER CHOICE — Invite or Dismiss Lyra
    # ======================================================
    menu:
        "Tell her to leave":
            $ choice_and_dev(
                _current_scene_id, "lyra_visit_tell_leave", "OB", factor=1,
                next_scene_label="act1_12_lyra_visit",
                note="Pushes Lyra away; preserves mask; OB-lean."
            )
            $ set_scene_flag(scene_id, "told_her_to_leave")

            a "It's late. You shouldn't be here."
            l "(contained) Right. Forget I knocked."

            "She hesitates; looks back once."

            l "Glass and glass, Aeron. We recognize each other."
            l "And I see you breaking. That is not weakness. That is waking up."

            "The door clicks. Quiet returns."
            
            athought "She sees it. The cracks. The breaking."
            athought "Maybe that's why she came."
            # VISUAL: Corridor warm spill disappears; room cools another notch.

        "Let Lyra stay":
            $ choice_and_dev(
                _current_scene_id, "lyra_visit_let_stay", "EMP", factor=1,
                next_scene_label="act1_12_lyra_visit",
                note="Allows proximity; admits need; EMP-lean."
            )
            $ add_affection("Lyra", 1)
            $ set_scene_flag(scene_id, "let_her_stay")

            a "(after a beat) Sit, then."
            l "(moves to the edge of the bed) Better."
            a "Not sure what's better about it."
            l "You're still here. That's better."
            l "Glass would've already shattered. You haven't."

            "The city hum fades; slower quiet replaces it."

            # SFX: Wind dips 3 dB; room tone closer.

            # ---------- EMPATHY VARIATION — Tone of connection ----------
            if is_ob_hard:
                athought "This is proximity, not comfort. I know the difference."
            elif is_mid:
                athought "I should tell her to go. I don't."
            else:
                athought "For the first time, being seen doesn't hurt."
            # ------------------------------------------------------------

            a "You ever wonder if any of this means anything?"
            l "(arches a brow) Define 'this.'"
            a "Solveil. Echelon. The theater we keep playing."
            l "(dry) Only every waking moment."

            "He almost laughs. It dies halfway out."

            a "You're lucky. They see purpose when they look at you."
            l "(faint) You think that's luck?"
            a "Isn't it?"
            l "They don't see me. They see what they built. A weapon in a dress."
            l "Glass in a different shape. Same emptiness."

            "Her hands fold, unfold. A rare break in composure."

            a "Where were you? Before tonight, I mean. You said you were on assignment."
            l "(pause) Sector Seven. Compliance audit."
            a "That's... vague."
            l "(looks at him directly) It was meant to be."

            "She stands. Moves to the window. Puts space between them like armor."

            l "They sent me to evaluate a residential block. Efficiency metrics. Loyalty indexes."
            a "Sounds routine."
            l "It was. Until I found the children."

            # WEATHER GRAMMAR: No rain at Aeries altitude; use wind/condensation.
            "Her reflection fractures in the condensation-slick glass."

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
            l "I am Glass too, Aeron. Transparent. Empty. Obedient."
            l "And Glass is cracking."

            a "(softly) That's because you're not a weapon. You're a person."
            l "Am I? Am I really?"
            "She turns. Eyes meet. Distance shrinks without either moving."

            l "Am I? Sometimes I'm not sure where the orders end and I begin."
            a "I know the feeling."
            l "Of course you do. Glass recognizes glass."

            # WEATHER GRAMMAR: Pressure thrum, not rain.
            "Wind presses against the facade; the world narrows to this room."

            l "When I was at the door... you hesitated before opening it."
            a "I didn't expect anyone."
            l "Were you hoping I wouldn't come?"
            a "(pause) No. I was hoping you would."
            l "Then why do you look like you wish I hadn't?"
            a "Because I don't know what happens next."
            a "We're both Glass. Both cracking. What happens when we both shatter?"
            l "Perhaps we find out what was underneath all along."

            "She moves. Sits beside him. Close enough to feel the warmth."

            l "Then say nothing. Just... don't be alone tonight."
            a "(voice rough) Lyra, I—"

            "The words lodge in his throat. Too big. Too true."

            l "(gently) What?"
            a "I don't know how to do this. Any of this."
            l "Do what?"
            a "Feel things I'm not supposed to feel. Want things I can't have."
            a "Glass isn't supposed to want. Glass just reflects."
            a "But I want... I want to be more than Glass."
            l "(barely a whisper) Who says you can't?"

            "The space between them disappears. Almost touching. Almost."

            a "(standing abruptly) You should rest. It's late."
            l "(hurt flickers, then hides) Right. Of course."

            "She stands. Composure slides back into place like a mask."

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

            "She's gone. The room feels different now."
            "Lighter. Or maybe just less empty."

            athought "Glass recognizes glass."
            athought "And maybe... maybe we can break together."
            athought "Find out what's underneath. What we used to be. What we could still become."

    $ set_scene_flag(scene_id, "completed")
    $ add_trust("Lyra", 1)  # visit itself increases trust

    return


# ========= CANON NOTES =========
# cann.scene_id: act1_12_lyra_visit
# cann.when_in_timeline: Immediately after Breaking Point; same night; pre–Sector 10 departure.
# cann.what_happened:
#   - Lyra checks on Aeron after rooftop brink; names the crack; offers presence.
#   - Player either pushes her away (OB-lean) or lets her stay (EMP-lean); deeper talk if she stays.
#   - Sector Seven “children audit” confession seeds Act I empathy spine + Echelon cost.
# cann.aeron_state: Alignment tints VO only (no momentum). OB = guarded/clinical; mid = ambivalent; EMP = receptive.
# cann.path_tracking:
#   - Menu weights: Leave → OB(+1); Stay → EMP(+1). Scene delta range: **−1 → +1**.
#   - Running empathy window BEFORE:  **≈ [-29, +27]**  (after Debrief + Breaking Point[0]).
#   - Running empathy window AFTER:   **≈ [-30, +28]**  (applies one-side expansion by ±1).
#   - Flags: told_her_to_leave / let_her_stay / completed. Affection+1 if stay; Trust+1 baseline for the visit.
# cann.thematic_flags: Glass vs Person; presence over doctrine; “waking up” vs “weakness.”
# cann.block_status: VARIANT (two-route scene; extended content if stay).
# cann.true_path_integration: none (menu-free TP rule stands).
# cann.visual_plate_economy:
#   - REUSE: Bedroom night master; corridor spill toggle; balcony haze plate (door cracked).
#   - HERO: Desk-perch two-shot; condensation-slick window reflection CU; finger-brush on lighter.
# cann.requires_followup:
#   - If `told_her_to_leave`: colder tone in next morning prep; lower early Act II openness.
#   - If `let_her_stay`: unlocks warmer micro-beats in Sector 10 prep + future rooftop callback.
# cann.consistency_asserts:
#   - Aeries altitude weather grammar only (wind/condensation/haze; no rain language).
#   - Keep Marcus doctrine phrasing consistent; maintain 390 ops count continuity.