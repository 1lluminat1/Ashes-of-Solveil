# =======================================================
# ACT 1 - Scene 07: Aeron's Bedroom (After the Gala)
# File: act1_07_bedroom.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_07_bedroom"
$ scene_mark(_current_scene_id, "entered")


label act1_07_bedroom:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Static 35–40mm; gentle 2% push on envelope reveal and on "mask slipped."
    # LIGHTING: Night interior; cold city spill (5200K) through glass, warm desk practical (3000K) on orders.
    # SFX: Low HVAC hum, distant wind pressure against glass (Aeries altitude), terminal soft beeps.
    # FX/COMP: Window condensation/rim highlights; envelope wax glint; subtle screen bloom.
    # BLOCKING: Sealed order with Echelon crest on desk, powered terminal, opaque glass wall.
    # FACE: Keep in partial silhouette early; fuller reveal on "mask slipped" beat.

    scene bg_aeron_room_night with fade

    "Later that night..."

    athought "She didn't say goodbye—just gone, like she was never there."

    # ========= BALCONY CALLBACK =========
    # NOTE: Conditional warmth based on prior intimacy choices.

    if scene_has("act1_05_gala", "approach_lyra"):
        if scene_has("act1_06_balcony", "shared_light") and scene_has("act1_06_balcony", "held_gaze"):
            athought "But I can still feel the space between us—close enough to matter."
            athought "Two people leaning toward each other, almost touching, almost shattering."
        elif scene_has("act1_06_balcony", "shared_light"):
            athought "The flame, her eyes—for a moment, we were just us."
            athought "Not performance, not protocol. Just two people remembering what that felt like."

    athought "Still, something was different in her eyes tonight. Not duty, not protocol—something real."

    athought "She sees what I am. And she sees what's underneath."

    athought "Maybe I'm not the only one tired of pretending."

    # ========= MISSION ORDER =========
    # VISUAL: On the desk—sealed mission order with Echelon crest; faint terminal glow.
    # CAMERA: Slow push toward the envelope. Wax seal catches the light.

    "A sealed mission order waits on the desk—the Echelon crest bleeding crimson in the lamplight."

    # ========= PATH-BASED ATMOSPHERE =========

    if pass_tier("OB2", "OB3"):
        athought "Silence is clarity—the hum beneath everything, the system breathing through me."
    elif pass_tier("OB1", "NEU"):
        athought "It's quiet. Too quiet to tell if it's peace or pressure."
    else:
        athought "The room feels heavier than before. Every order adds weight, and even silence sounds like expectation."

    # ========= PLAYER CHOICE — OPEN THE ORDER =========
    # VISUAL: The seal catches the light—Marcus's insignia pressed into wax.

    menu:
        athought "The seal catches the light—Marcus's insignia pressed into wax."

        "Break it immediately.":
            $ record_choice_once(_current_scene_id, "_open_now")
            $ scene_mark(_current_scene_id, "opened_immediately")

            "The seal snaps. Orders are always easier than silence."

            athought "Muscle memory takes over. My hands know the ritual better than I do."

        "Hesitate for a breath.":
            $ choice_and_dev(
                _current_scene_id, "_hesitate_open", "EMP", factor=1,
                note="Allows feeling to interrupt procedure."
            )
            $ scene_mark(_current_scene_id, "hesitated_order")

            "The envelope sits between my fingers, as if delay could change the words inside."

            "Then the seal breaks with a soft crack."

            athought "Hesitation. That's new. Or maybe the cracks are spreading faster than I thought."

    # ========= ORDER CONTENT =========
    # VISUAL: Clean text on official paper. Impersonal. Familiar.

    "The words are clean, precise, impersonal."

    athought "'Sector 10 breach confirmed. Possible rebel intel leaks within Unders comm-grid.'"

    athought "'Sweep. Secure. Eliminate. Prove your worth.'"

    athought "Prove your worth. Always the same."

    athought "Sweep, secure, eliminate—like I'm a task to complete, not a person."

    athought "Sector 10 makes 391. Different orders, same result, same words, same emptiness."

    if pass_tier("OB2", "OB3"):
        athought "They call it progress. They're right—every mission cleaner than the last."
    elif pass_tier("OB1", "NEU"):
        athought "Progress, repetition—same thing after enough cycles."
    else:
        athought "They call it progress. I call it perfected apathy."

    # ========= MASK SLIPPAGE =========
    # CAMERA: 2% push. This is the emotional beat.

    athought "Still wearing the mask, even alone."

    athought "But tonight, the mask slipped. Lyra saw through it—and I let her."

    athought "That's not what I do. I don't let anyone see."

    # ========= PLAYER CHOICE — ACKNOWLEDGE MARCUS =========
    # VISUAL: Terminal glow. Blank message cursor blinks.

    menu:
        athought "A blank message cursor blinks on the terminal."

        "Send a single-word acknowledgment: 'Received.'":
            $ choice_and_dev(
                _current_scene_id, "_ack_marcus", "OB", factor=1,
                note="Confirms command without delay; reaffirms performance reflex."
            )
            $ scene_mark(_current_scene_id, "acknowledged_marcus")

            "The message leaves without ceremony."

            athought "Confirm, comply, continue. The machine doesn't blink."

            athought "391 operations. The count continues."

        "Say nothing.":
            $ choice_and_dev(
                _current_scene_id, "_ignore_marcus", "EMP", factor=1,
                note="Withholds ritual confirmation; first visible noncompliance."
            )
            $ scene_mark(_current_scene_id, "ignored_marcus")

            "The cursor keeps blinking until the screen sleeps."

            athought "No response. First time in 390 operations."

            athought "The silence feels like rebellion—or just exhaustion."

    # ========= WINDOW REFLECTION =========
    # VISUAL: Window shows the Unders glowing like embers far below.
    # CAMERA: Aeron's reflection ghosted over the cityscape.

    "The window holds the Unders in miniature—distant lights flickering like embers in the dark."

    athought "The Unders stay the same. The rest of us just pretend we're different."

    # ========= CLOSING REFLECTION — PATH-BASED =========

    if pass_tier("OB2", "OB3"):
        athought "Tonight changed nothing. Connection is noise, and I can't afford noise."
        athought "She recognized something in me—and I still chose to hold form."
        athought "Wholeness is a myth for those who hesitate."
    elif pass_tier("OB1", "NEU"):
        athought "She said we recognize each other. Maybe she was right, maybe she was wrong."
        athought "But the thought won't leave me."
    else:
        athought "But tonight felt different. Lyra made it different."
        athought "Two polished surfaces, both cracking, both wondering if breaking means freedom or falling."
        athought "Maybe breaking is the only way back to being whole."

    "The mission waits. It always does."

    "But tonight, the past won't stay buried."

    athought "She asked if I remembered what wholeness felt like."

    athought "I don't. But for a moment on that balcony, I almost did."

    scene black with fade

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_07_bedroom
# cann.when_in_timeline: Night after Gala/Balcony; pre–Sector 10 deployment.
# cann.what_happened:
#   - Aeron processes Balcony micro-intimacy; acknowledges mask slippage.
#   - Orders arrive: Sector 10 sweep/secure/eliminate; "Prove your worth."
#   - Player chooses (1) immediate open (NEU) vs hesitation (EMP +1), and (2) acknowledgment to Marcus (OB -1) vs silence (EMP +1).
# cann.aeron_state: OB baseline voice; branches show first explicit, visible hesitation.
# cann.path_tracking:
#   - Scene deltas:
#       • M1 (order seal): opened_immediately NEU | hesitated_order +1 EMP
#       • M2 (terminal reply): acknowledged_marcus -1 OB | ignored_marcus +1 EMP
#     Net per-scene span: -1 → +2
# cann.flags: opened_immediately | hesitated_order | acknowledged_marcus | ignored_marcus
# cann.thematic_flags:
#   - Motifs: Mask/Performance, Cracks, Orders-as-Identity, Worth/Counting ("391").
#   - Recurring lines: "Prove your worth." / "The mask slipped."
# cann.block_status: ANCHOR scene with light VARIANTS (two menus).
# cann.visual_plate_economy:
#   - REUSE: Bedroom night master (city spill on glass); desk close-up with order; monitor glow plate.
#   - HERO: Wax-seal macro; window reflection of Aeron on "mask slipped."
# cann.requires_followup:
#   - Route to Sector 10 departure/setup; branch tone via flags:
#       • opened_immediately + acknowledged_marcus → colder prep VO.
#       • hesitated_order or ignored_marcus → introspective prep VO.
# cann.consistency_asserts:
#   - Aeries altitude: no rain-on-glass; use wind pressure/condensation language only.
#   - Keep Marcus phrasing ("Prove your worth") aligned to doctrine diction.