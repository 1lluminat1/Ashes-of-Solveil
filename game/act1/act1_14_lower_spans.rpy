# =======================================================
# ACT 1 - Scene 14: Aeron's Late Night Walk in the Lower Spans
# File: act1_14_lower_spans.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_14_lower_spans"
$ scene_mark(_current_scene_id, "entered")

define vendor = Character("Vendor")
define child = Character("Child")


label act1_lower_spans:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Tracking shots through catwalks; eye-level two-shots for encounters; high-angle wide for courtyard.
    # LIGHTING: Sodium/blue mix; signage flicker; steam plumes catching light.
    # SFX LOOP: Distant market; pipe drip; elevator chain clatter; occasional drone pass.
    # SFX ONE-SHOTS: Condensation drips; broken guitar notes; drone sweep.
    # BLOCKING: Sector 10 lower spans / perimeter catwalks; maintenance stairs; neon fog below.
    # FX/COMP: Steam plumes; barrel fire glow; drone searchlight sweep.

    #scene bg_lower_spans_night with fade

    # ========= OPENING — DESCENT =========

    "Each level bleeds more color—red, green, electric blue. The edges run brightest."

    athought "I couldn't sleep. Not after Marcus's order."

    athought "Not after Lyra. Not after standing on that edge."

    athought "Air tastes different down here—metal and rainwater. Not clean, but honest."

    "Condensation taps the concrete. The walls breathe."

    "The lower spans pulse with another kind of life. No marble, no velvet—just rust, steam, survival."

    "A child laughs; a blade slides through an oil rag. Voices rise, barter, vanish."

    athought "They call this 'forgotten.' It feels more awake than the Aeries."

    athought "Tomorrow at dawn, I'm ordered to sweep this sector."

    athought "200 to 500 targets. 'Acceptable collateral.'"

    athought "Weapons execute orders. But tonight... tonight I wanted to see what I'm ordered to destroy."

    # ========= ENCOUNTER 1 — THE VENDOR =========

    "A vendor works a makeshift stand—heat coils glowing beneath a dented pot. The smell cuts through rust and rain."

    vendor "(calls out) Therm-brew! Hot! Real beans, not synth!"

    vendor "(cautious) ...You lost, soldier?"

    menu:
        athought "The vendor's eyes track me—wary, but not hostile."

        "Buy a cup.":
            $ choice_and_dev(
                _current_scene_id, "lower_spans_buy_brew", "EMP", factor=1,
                note="Buys therm-brew; humane contact with Unders vendor."
            )
            $ scene_mark(_current_scene_id, "bought_brew")

            a "How much?"

            vendor "(surprised) ...Five credits."

            a "Keep the change."

            vendor "(takes it slowly) ...You serious?"

            a "It smells better than anything in the Aeries."

            vendor "(softens) Well. Ain't that the truth."

            "The cup is warm—bitter, earthy, real."

            athought "When was the last time I tasted something that wasn't sanitized?"

            vendor "You're Marcus Rylan's boy, yeah?"

            a "(carefully) I am."

            vendor "Heard about your brother. Damn shame."

            a "...Yeah. It was."

            vendor "(nods) You're alright in my book. Stay warm."

            athought "Down here, respect isn't inherited. It's earned."

            athought "Tomorrow, I'm ordered to clear this sector. Will he survive the sweep?"

            athought "I'm not supposed to ask these questions. But I'm asking now."

        "Walk past without stopping.":
            $ choice_and_dev(
                _current_scene_id, "lower_spans_ignore_vendor", "OB", factor=1,
                note="Ignores vendor; maintains emotional distance."
            )
            $ scene_mark(_current_scene_id, "ignored_vendor")

            athought "Not here to make friends."

            "The vendor watches him pass. Doesn't call out again."

            athought "Tomorrow, I might kill him. Better not to know his face."

            athought "That's what I'm supposed to think. ...Why does it feel wrong tonight?"

    # ========= TRANSITION =========

    "A drone sweeps past; the light skims and moves on. Even the machines look tired here."

    athought "Eyes are everywhere. People don't bow. They keep moving."

    # ========= ENCOUNTER 2 — THE CHILD =========

    "Movement—quick, low to the ground. A child slips between the pipes."

    child "(freezes) ...You're one of them."

    a "One of who?"

    child "Echelon. The ones that took my dad."

    "Small hands. Dirty knuckles. Eyes too old for the face."

    athought "Tomorrow, this child might be on the casualty list."

    athought "'Acceptable collateral.'"

    menu:
        athought "The child's breath fogs the air between us."

        "Try to reassure the child.":
            $ choice_and_dev(
                _current_scene_id, "lower_spans_reassure_child", "EMP", factor=1,
                note="Crouches; reassures; admits uncertainty."
            )
            $ scene_mark(_current_scene_id, "reassured_child")

            a "(crouches slightly) I'm not here for that."

            child "(suspicious) Then what're you here for?"

            a "...I don't know yet."

            child "You look sad."

            a "(quiet) Maybe I'm tired of looking mean."

            child "My dad said some soldiers still got hearts."

            a "Where did they take him?"

            child "(shrugs) Dunno. He didn't come back."

            athought "How many stories like this are there? How many I'll never hear?"

            athought "How many more after tomorrow's sweep?"

            child "You gonna take people too?"

            a "(honest) I hope not."

            child "(nods) ...Okay."

            "The child backs away, then disappears into the pipes."

            athought "Tomorrow, that child is a target. I'm supposed to obey. But something's breaking."

        "Say nothing and keep walking.":
            $ choice_and_dev(
                _current_scene_id, "lower_spans_ignore_child", "OB", factor=1,
                note="Ignores child; preserves mission persona."
            )
            $ scene_mark(_current_scene_id, "ignored_child")

            "He says nothing. What could he say?"

            child "(bitter) Yeah. That's what I thought."

            "The child vanishes into shadow. Contempt lingers."

            athought "Can't blame them. I'd spit too."

            athought "Tomorrow, that child might die in the sweep. And they'll die hating me."

    # ========= ENCOUNTER 3 — THE COURTYARD =========

    "He stops at a railing; far below, scattered fires stubborn as stars."

    athought "No spires, no chandeliers—just humanity, unpolished."

    "Below, people gather around barrel fires. Laughter rises through the steam."

    "Someone plays a PVC pipe flute. The notes are breathy, hollow."

    "A couple shares food from a dented tin. An old man tells stories to children."

    athought "They have nothing. And somehow, they have everything I don't."

    athought "Tomorrow at dawn, this courtyard is a target zone."

    athought "Those fires will be extinguished. Those voices silenced."

    "A child points up. The music stops. Eyes find him in the dark."

    menu:
        athought "They watch me. Waiting."

        "Nod in acknowledgment.":
            $ choice_and_dev(
                _current_scene_id, "lower_spans_acknowledge_crowd", "EMP", factor=1,
                note="Acknowledges Unders crowd; non-threatening signal."
            )
            $ scene_mark(_current_scene_id, "acknowledged_unders")

            "He lifts his hand. Not a threat. Just recognition."

            "After a beat, the old man nods back. The guitar resumes."

            athought "Not forgiveness, not trust—but not hatred either. It's more than I deserve."

            athought "Tomorrow, I'm ordered to kill them. And tonight, they acknowledged me."

            athought "Something in me is cracking. I can feel it."

        "Step back into shadow.":
            $ choice_and_dev(
                _current_scene_id, "lower_spans_hide_from_crowd", "OB", factor=1,
                note="Hides in shadow; avoids recognition."
            )
            $ scene_mark(_current_scene_id, "hid_from_unders")

            "He steps back—out of the light, out of sight."

            "The guitar picks up again. Life continues without him."

            athought "I don't belong down here. I don't belong anywhere."

            athought "Tomorrow, I'll belong to the mission. I always do."

    # ========= CLOSING REFLECTION =========

    if pass_tier("OB3", "OB2"):
        athought "Observation complete. Data confirmed. Sector alive but noncompliant."
        athought "Tomorrow it will be corrected. Efficiently."
    elif pass_tier("OB1", "NEU"):
        athought "This edge is a mirror. Everyone's running from something. Me too."
        athought "Maybe the mission isn't the cure. Maybe it's the infection."
    else:
        athought "Every face tonight was a reason not to follow that order."
        athought "Maybe the cracks aren't breaking me. Maybe they're letting the light in."

    "Wind carries rain and iron. The lights dip, then steady."

    "He keeps walking. Deeper into the shadows."

    athought "Tomorrow, I'm ordered to sweep this sector. The vendor, the child, the families around the fires."

    athought "All of them. Gone."

    athought "I'm supposed to obey orders. I'm not supposed to question."

    athought "But I came here tonight to see their faces. To know what I'm about to destroy."

    athought "Maybe that's the crack spreading. Maybe that's something breaking."

    athought "Or maybe... maybe it's what's underneath that's finally waking up."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_14_lower_spans
# cann.when_in_timeline: Same night as The Message; pre-dawn; hours before Sector 10 sweep directive executes.
# cann.what_happened:
#   - Aeron walks the Lower Spans to "see what he's about to destroy."
#   - Three micro-encounters: vendor, child, courtyard crowd.
#   - Each can tilt empathy (humane contact, reassurance, recognition) or obedience (avoidance, silence, hiding).
# cann.aeron_state: OB-hard = clinical reconnaissance; mid = ambivalent fracture; EMP = dawning solidarity.
# cann.path_tracking:
#   - Menus (3): vendor (EMP+1 vs OB+1), child (EMP+1 vs OB+1), crowd (EMP+1 vs OB+1).
#   - Scene empathy delta range: −3 → +3.
#   - Flags: bought_brew / ignored_vendor; reassured_child / ignored_child; acknowledged_unders / hid_from_unders; completed.
# cann.thematic_flags: "Acceptable collateral" deglossed; faces over metrics; choosing to look before destroying.
# cann.block_status: VARIANT (stackable micro-beats); colors Sector 10 prep VO and Zira encounter tone.
# cann.visual_plate_economy:
#   - REUSE: One catwalk master with fog density slider; vendor kiosk prop set; pipe nook for child; wide courtyard plate with barrel fires.
#   - HERO: Cup-in-hand CU (steam), child eye-level two-shot, high-angle crowd tableau.
# cann.requires_followup:
#   - If EMP-lean here → unlock "humane corridor" suggestion beat in Sector 10 setup; warmer Zira first read.
#   - If OB-lean here → colder Marcus reaction line; Zira greets with sharper distrust.