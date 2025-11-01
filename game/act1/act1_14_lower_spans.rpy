# =======================================================
# ACT 1 - Scene 14: Aeron's Late Night Walk in the Lower Spans
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_14_lower_spans"
$ scene_mark(_current_scene_id, "entered")

define vendor = Character("Vendor")
define child = Character("Child")


label act1_lower_spans:

    # Alignment reads (light flavor only; no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    # empathy side = else

    # VISUAL: Sector 10 lower spans / perimeter catwalks; maintenance stairs; neon fog below.
    # SOUND: Distant market; pipe drip; elevator chain clatter; occasional drone pass.
    # LIGHTING: Sodium/blue mix; signage flicker; steam plumes catching light.

    "{i}Each level bleeds more color—red, green, electric blue. The edges run brightest.{/i}"

    a "{i}I couldn’t sleep. Not after Marcus’s order.{/i}"
    a "{i}Not after Lyra. Not after standing on that edge.{/i}"
    a "{i}Air tastes different down here—metal and rainwater. Not clean, but honest.{/i}"

    "{i}Condensation taps the concrete. The walls breathe.{/i}"

    "{i}The lower spans pulse with another kind of life. No marble. No velvet. Just rust, steam, survival.{/i}"
    "{i}A child laughs; a blade slides through an oil rag. Voices rise, barter, vanish.{/i}"

    a "{i}They call this 'forgotten.' It feels more awake than the Aeries.{/i}"
    a "{i}Tomorrow at dawn, I’m ordered to sweep this sector.{/i}"
    a "{i}200 to 500 targets. 'Acceptable collateral.'{/i}"
    a "{i}Glass executes orders. But tonight... tonight I wanted to see what Glass destroys.{/i}"

    "{i}A vendor works a makeshift stand—heat coils glowing beneath a dented pot. The smell cuts through rust and rain.{/i}"

    vendor "(calls out) Therm-brew! Hot! Real beans, not synth!"

    vendor "(cautious) ...You lost, soldier?"

    # ------------------------------------------------------
    # PLAYER CHOICE – interact or not
    # ------------------------------------------------------
    menu:
        "The vendor’s eyes track him—wary, but not hostile."
        "Buy a cup.":
            $ apply_choice_once(
                _current_scene_id, "lower_spans_buy_brew", "EMP", factor=1,
                next_scene_label="act1_14_lower_spans",
                note="Buys therm-brew; humane contact with Unders vendor"
            )
            $ set_scene_flag(scene_id, "bought_brew")

            a "How much?"
            vendor "(surprised) ...Five credits."
            a "Keep the change."
            vendor "(takes it slowly) ...You serious?"
            a "It smells better than anything in the Aeries."
            vendor "(softens) Well. Ain’t that the truth."

            "{i}The cup is warm. Bitter, earthy, real.{/i}"

            a "{i}When was the last time I tasted something that wasn’t sanitized?{/i}"

            vendor "You’re Marcus Rylan’s boy, yeah?"
            a "(carefully) I am."
            vendor "Heard about your brother. Damn shame."
            a "...Yeah. It was."
            vendor "(nods) You’re alright in my book. Stay warm."

            "{i}Down here, respect isn’t inherited. It’s earned.{/i}"

            a "{i}Tomorrow, I’m ordered to clear this sector. Will he survive the sweep?{/i}"
            a "{i}Glass doesn’t ask these questions. But I’m asking now.{/i}"

        "Walk past without stopping.":
            $ apply_choice_once(
                _current_scene_id, "lower_spans_ignore_vendor", "OB", factor=1,
                next_scene_label="act1_14_lower_spans",
                note="Ignores vendor; maintains emotional distance"
            )
            $ set_scene_flag(scene_id, "ignored_vendor")

            a "{i}Not here to make friends.{/i}"

            "{i}The vendor watches him pass. Doesn’t call out again.{/i}"

            a "{i}Tomorrow, I might kill him. Better not to know his face.{/i}"
            a "{i}That’s what Glass would think. ...Why does it feel wrong tonight?{/i}"

    "{i}A drone sweeps past; the light skims and moves on. Even the machines look tired here.{/i}"

    a "{i}Eyes are everywhere. People don’t bow. They keep moving.{/i}"

    "{i}Movement—quick, low to the ground. A child slips between the pipes.{/i}"

    child "(freezes) ...You’re one of them."
    a "One of who?"
    child "Echelon. The ones that took my dad."

    "{i}Small hands. Dirty knuckles. Eyes too old for the face.{/i}"

    a "{i}Tomorrow, this child might be on the casualty list.{/i}"
    a "{i}'Acceptable collateral.'{/i}"

    # ------------------------------------------------------
    # PLAYER CHOICE – empathy toward child
    # ------------------------------------------------------
    menu:
        "The child’s breath fogs the air between them."
        "Try to reassure the child.":
            $ apply_choice_once(
                _current_scene_id, "lower_spans_reassure_child", "EMP", factor=1,
                next_scene_label="act1_14_lower_spans",
                note="Crouches; reassures; admits uncertainty"
            )
            $ set_scene_flag(scene_id, "reassured_child")

            a "(crouches slightly) I’m not here for that."
            child "(suspicious) Then what’re you here for?"
            a "...I don’t know yet."
            child "You look sad."
            a "(quiet) Maybe I’m tired of looking mean."
            child "My dad said some soldiers still got hearts."
            a "Where did they take him?"
            child "(shrugs) Dunno. He didn’t come back."
            a "{i}How many stories like this are there? How many I’ll never hear?{/i}"
            a "{i}How many more after tomorrow’s sweep?{/i}"
            child "You gonna take people too?"
            a "(honest) I hope not."
            child "(nods) ...Okay."
            "{i}The child backs away, then disappears into the pipes.{/i}"
            a "{i}Tomorrow, that child is a target. Glass obeys. But something’s breaking.{/i}"

        "Say nothing and keep walking.":
            $ apply_choice_once(
                _current_scene_id, "lower_spans_ignore_child", "OB", factor=1,
                next_scene_label="act1_14_lower_spans",
                note="Ignores child; preserves mission persona"
            )
            $ set_scene_flag(scene_id, "ignored_child")

            "{i}He says nothing. What could he say?{/i}"

            child "(bitter) Yeah. That’s what I thought."

            "{i}The child vanishes into shadow. Contempt lingers.{/i}"

            a "{i}Can’t blame them. I’d spit too.{/i}"
            a "{i}Tomorrow, that child might die in the sweep. And they’ll die hating me.{/i}"

    "{i}He stops at a railing; far below, scattered fires stubborn as stars.{/i}"

    a "{i}No spires. No chandeliers. Just humanity, unpolished.{/i}"

    "{i}Below, people gather around barrel fires. Laughter rises through the steam.{/i}"
    "{i}Someone plays a broken guitar. The notes are wrong, but no one cares.{/i}"
    "{i}A couple shares food from a dented tin. An old man tells stories to children.{/i}"

    a "{i}They have nothing. And somehow, they have everything I don’t.{/i}"
    a "{i}Tomorrow at dawn, this courtyard is a target zone.{/i}"
    a "{i}Those fires will be extinguished. Those voices silenced.{/i}"

    "{i}A child points up. The music stops. Eyes find him in the dark.{/i}"

    # ------------------------------------------------------
    # PLAYER CHOICE – acknowledge or hide
    # ------------------------------------------------------
    menu:
        "They watch him. Waiting."
        "Nod in acknowledgment.":
            $ apply_choice_once(
                _current_scene_id, "lower_spans_acknowledge_crowd", "EMP", factor=1,
                next_scene_label="act1_14_lower_spans",
                note="Acknowledges Unders crowd; non-threatening signal"
            )
            $ set_scene_flag(scene_id, "acknowledged_unders")

            "{i}He lifts his hand. Not a threat. Just recognition.{/i}"
            "{i}After a beat, the old man nods back. The guitar resumes.{/i}"

            a "{i}Not forgiveness. Not trust. But not hatred either. It’s more than I deserve.{/i}"
            a "{i}Tomorrow, I’ll kill them. And tonight, they acknowledged me.{/i}"
            a "{i}Glass is cracking. I can feel it.{/i}"

        "Step back into shadow.":
            $ apply_choice_once(
                _current_scene_id, "lower_spans_hide_from_crowd", "OB", factor=1,
                next_scene_label="act1_14_lower_spans",
                note="Hides in shadow; avoids recognition"
            )
            $ set_scene_flag(scene_id, "hid_from_unders")

            "{i}He steps back—out of the light, out of sight.{/i}"
            "{i}The guitar picks up again. Life continues without him.{/i}"
            a "{i}I don’t belong down here. I don’t belong anywhere.{/i}"
            a "{i}Tomorrow, I’ll belong to the mission. Glass always does.{/i}"

    # ------------------------------------------------------
    # EMPATHY-TIER INTERNAL REFLECTION
    # ------------------------------------------------------
    if is_ob_hard:
        a "{i}Observation complete. Data confirmed. Sector alive but noncompliant.{/i}"
        a "{i}Tomorrow it will be corrected. Efficiently.{/i}"
    elif is_mid:
        a "{i}This edge is a mirror. Everyone’s running from something. Me too.{/i}"
        a "{i}Maybe the mission isn’t the cure. Maybe it’s the infection.{/i}"
    else:
        a "{i}Every face tonight was a reason not to follow that order.{/i}"
        a "{i}Maybe the cracks aren’t breaking me. Maybe they’re letting the light in.{/i}"

    "{i}Wind carries rain and iron. The lights dip, then steady.{/i}"
    "{i}He keeps walking. Deeper into the shadows.{/i}"

    a "{i}Tomorrow, I’m ordered to sweep this sector. The vendor. The child. The families around the fires.{/i}"
    a "{i}All of them. Gone.{/i}"
    a "{i}Glass obeys orders. Glass doesn’t question.{/i}"
    a "{i}But I came here tonight to see their faces. To know what Glass destroys.{/i}"
    a "{i}Maybe that’s the crack spreading. Maybe that’s Glass breaking.{/i}"
    a "{i}Or maybe... maybe it’s what’s underneath that's finally waking up.{/i}"

    $ set_scene_flag(scene_id, "completed")
    return


# ========= CANON NOTES =========
# cann.scene_id: act1_14_lower_spans
# cann.when_in_timeline: Same night as The Message; pre-dawn; hours before Sector 10 sweep directive executes.
# cann.what_happened:
#   - Aeron walks the Lower Spans to “see what Glass destroys.”
#   - Three micro-encounters: vendor, child, courtyard crowd.
#   - Each can tilt empathy (humane contact, reassurance, recognition) or obedience (avoidance, silence, hiding).
# cann.aeron_state: OB-hard = clinical reconnaissance; mid = ambivalent fracture; EMP = dawning solidarity.
# cann.path_tracking:
#   - Running window BEFORE:   **≈ [-29, +29]**
#   - Menus (3): vendor (EMP+1 vs OB+1), child (EMP+1 vs OB+1), crowd (EMP+1 vs OB+1).
#   - Scene empathy delta range: **−3 → +3**.
#   - Running empathy window: previous **[L, U] → [L−3, U+3]**.
#   - Flags: bought_brew / ignored_vendor; reassured_child / ignored_child; acknowledged_unders / hid_from_unders; completed.
#   - Running window AFTER:    **≈ [-32, +32]**
# cann.thematic_flags: “Acceptable collateral” deglossed; faces over metrics; Glass choosing to look.
# cann.block_status: VARIANT (stackable micro-beats); colors Sector 10 prep VO and Zira encounter tone.
# cann.true_path_integration: none (menu-free TP rule stands).
# cann.visual_plate_economy:
#   - REUSE: One catwalk master with fog density slider; add vendor kiosk prop set; pipe nook for child; wide courtyard plate with barrel fires.
#   - Inserts: cup-in-hand CU (steam), child eye-level two-shot, high-angle crowd tableau.
# cann.requires_followup:
#   - If EMP-lean here → unlock “humane corridor” suggestion beat in Sector 10 setup; warmer Zira first read.
#   - If OB-lean here → colder Marcus reaction line; Zira greets with sharper distrust.
# cann.consistency_asserts:
#   - Weather grammar: Lower Spans may have rain/condensation; Aeries scenes must avoid precip.
#   - Keep “domestic/home” language consistent with regime diction (use “domestic space” in official VO).