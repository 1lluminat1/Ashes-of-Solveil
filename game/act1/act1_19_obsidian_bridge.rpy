# =======================================================
# ACT 1 - Scene 19: Obsidian Bridge — Zira's Judgment
# File: act1_19_obsidian_bridge.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_19_obsidian_bridge"
$ scene_mark(_current_scene_id, "entered")

label act1_obsidian_bridge:

    # VISUAL: Obsidian Bridge—massive structure spanning Mid ↔ Lower tiers.
    # LIGHTING: Cold blue moonlight; neon reflections in the void below; fingers of fog across the span.
    # SOUND: Wind whistling through truss; far machinery; water rush a long way down.
    # CAMERA: Lateral dolly to centerline; Aeron a silhouette against Aeries glow.

    "{i}Midnight. The Obsidian Bridge stretches into fog and darkness.{/i}"
    "{i}Below, the city's underbelly churns. Above, the Aeries glow with ignorant light.{/i}"
    "{i}And here, between them, the forgotten meet.{/i}"

    # Aeron alone, gear cleaned but weight unchanged.
    $ band = get_empathy_band()
    $ em = mercy_total()                  # evidence_of_mercy snapshot

    a "{i}She said midnight. If I fought for them, she'd be here.{/i}"
    a "{i}If I just followed orders... don't bother coming.{/i}"

    if em >= 2:
        a "{i}I tried. I saved who I could. Two hundred alive because Glass cracked.{/i}"
        a "{i}But six hundred dead. Six hundred faces I can't unsee.{/i}"
        a "{i}Is that enough? Does trying count when you still kill hundreds?{/i}"
    elif em >= 1:
        a "{i}I tried. Not hard enough. Maybe fifty saved. Seven hundred fifty dead.{/i}"
        a "{i}Glass won. Mostly. But I fought it—some.{/i}"
        a "{i}Is that enough?{/i}"
    else:
        a "{i}I followed orders. Perfect execution. Eight hundred dead. Zero mercy.{/i}"
        a "{i}Glass didn't crack. Glass obeyed.{/i}"
        a "{i}She won't come. Why would she?{/i}"

    # Footsteps approach—measured, confident.
    # SFX: boot on grate; fog curls through the light cone.
    "{i}Footsteps. She's here.{/i}"
    pause 0.4

    # Zira arrives out of fog; reads him like a ledger.
    z "Glass."
    a "Zira."
    z "(quiet) You look like hell."
    a "I've been there. Just got back."
    z "Tell me what happened."

    if em >= 3:
        # ===== HIGH MERCY PATH (150+ saved; strong resistance shown) =====
        $ record_choice_once(_current_scene_id, "bridge_high_mercy_path")

        a "I completed the mission. Sector Ten swept."
        z "That's not what I asked."
        a "(meets her eyes) I saved who I could."

        z "How many?"
        a "Official report says eight hundred eliminated. Zero survivors."
        z "(steps closer) And the truth?"
        a "...Two hundred alive. Maybe more. I warned them. Faked reports. Let people escape."
        a "The vendor I met? I let him run."
        a "The child behind the door? I lied to my team. Left her alive."
        a "The shelter of two hundred? I scattered them. One-fifty escaped."

        # Zira processes; respect replacing suspicion.
        z "You lied to Marcus Rylan. Your father."
        a "I did."
        z "Your team saw you show mercy."
        a "They did."
        z "You risked everything."
        a "(quiet) I risked nothing. They had everything to lose."

        z "(a beat, then a nod) You fought the orders from within."
        z "That's not Glass. That's human."

        $ add_trust("Zira", 3)
        $ char_flag_on("Zira", "trusts_aeron")
        $ char_flag_on("Zira", "saw_high_mercy")

        a "Six hundred people still died."
        z "Yes. They did."
        a "Is that supposed to help? That I 'tried'?"
        z "(closer) No. It's supposed to make you remember you're not a machine."
        z "Glass obeys perfectly. You chose to try—and fail—to save them."
        z "Failure to save isn’t the same as choosing not to."

        # PROP: encrypted comm device
        # CAMERA: Her hand opens; small matte device in the moonlight.
        z "You wanted intel. Ways to see what's real."
        z "(places device in his hand) This connects you to my network."
        z "Encrypted. Untraceable. Use it when you're ready to do more than try."

        a "(looks at device) What do I do with this?"
        z "Whatever you want. Information is power."
        z "Right now, Marcus feeds you lies. With this, you see. Then you choose."

        $ grant_tool("encrypted_comm")
        $ set_scene_flag(_current_scene_id, "device_given")

    elif em >= 1:
        # ===== MODERATE MERCY PATH (50–149 saved; partial resistance) =====
        $ record_choice_once(_current_scene_id, "bridge_moderate_mercy_path")

        a "I completed the mission."
        z "I know. My network watched the grid breathe."
        a "(tense) Then you know what I did."
        z "I know you tried. Not enough. But you tried."

        $ add_trust("Zira", 1)
        $ char_flag_on("Zira", "saw_some_mercy")

        z "You saved what, fifty? Maybe a hundred?"
        a "I lost count."
        z "You let some escape. Faked some reports. Showed mercy where you could."
        z "You also followed orders and killed hundreds."

        a "(defensive) I couldn’t save them all. The team watched. Marcus—"
        z "(cuts him) I'm not judging. I'm observing."
        z "You're split: one foot in obedience, one in resistance."
        z "That makes you dangerous—to you and everyone near you."

        a "What do you want me to say?"
        z "Choose."
        z "Glass follows. Humans resist. You did both."
        z "Asset or liability—I haven't decided."

        # DEVICE: withheld beat, then tossed
        z "I came to give you access to my network."
        z "I'm not sure you're ready."
        a "What proves it?"
        z "(studies him, then tosses the device—he catches) Use that when you've decided."
        z "If you want to be Glass, delete it and forget me."
        z "If you want to be human, turn it on and see what's true."
        z "No half-measures next time."

        $ grant_tool("encrypted_comm")
        $ set_scene_flag(_current_scene_id, "device_given_conditional")

    else:
        # ===== LOW MERCY PATH (<50 saved; obedience dominated) =====
        $ record_choice_once(_current_scene_id, "bridge_low_mercy_path")

        a "The mission is complete. Sector Ten is cleared."
        z "(cold) I know."
        a "Then why ask?"
        z "To hear you say it. To see if you'd lie."

        z "Eight hundred people. Gone. Perfect obedience."
        z "Glass at its finest—efficient, empty."

        $ add_trust("Zira", -2)
        $ char_flag_on("Zira", "rejected_aeron")

        a "(quiet) I did what I had to—"
        z "No. You did what Marcus told you to."
        z "That's a choice. You chose not to see it."

        a "I came here. Doesn’t that count?"
        z "For what—absolution?"
        z "I'm not a priest. You don't get to feel better because you showed up."

        a "(tight) Then why are you here?"
        z "(beat) Because I'm an optimist. And an idiot."
        z "I thought Glass might crack. That you'd fight back."
        z "(bitter) I was wrong."

        z "You know the difference between you and the vendor you killed?"
        a "..."
        z "He chose dignity. You chose to be a weapon."
        z "Weapons don't get redemption."

        z "(over shoulder as she leaves) If you ever decide to be human instead of Glass..."
        z "Don't look for me. I won't be waiting."

        "{i}She's gone. Fog swallows the span.{/i}"
        a "{i}She's right. I chose Glass. Again.{/i}"
        a "{i}Eight hundred dead. And I learned nothing.{/i}"

        $ set_scene_flag(_current_scene_id, "device_withheld")
        $ set_scene_flag(_current_scene_id, "completed")
        jump act1_rooftop_reflection

    # ===== CONTINUE (HIGH / MODERATE ONLY) =====
    # CAMERA: Both at the rail; city’s pulse below.
    z "Something's coming. Big. Soon."
    a "Define 'big'."
    z "Grid anomalies, troop staging, silent lockdown preps."
    z "Sectors Eight, Nine, Ten. All at once."

    a "Sector Ten was prelude."
    z "Exactly. Clear the 'troublemakers' before the main event."
    a "(quiet) How big?"
    z "Hundreds of thousands. Days, not weeks."

    # Aeron grips the rail; knuckles blanch.
    a "{i}Hundreds of thousands. And I killed eight hundred as practice.{/i}"

    z "That's why I'm giving you access."
    z "You can't stop it alone. But you can see it."
    z "Maybe save someone when it hits."

    if em >= 3:
        z "(softer) You saved two hundred today. That's two hundred reasons to keep trying."
        z "Next time, save more."
    else:
        z "You half-committed today. Next time, pick a side."
        z "Half-measures get everyone killed."

    a "Why do you care? About me."
    z "(beat) Because you're Marcus Rylan's son. Access. Intel. Doors I can't open."
    z "Because if Glass cracks wide enough, you could help."
    z "And because two hundred people are breathing who shouldn't be."
    z "That's not nothing."

    # Wind builds; fog thickens.
    z "Go home. Rest."
    z "When you're ready to do more than try, use the device."
    z "I'll be watching."

    z "(over shoulder) And Glass?"
    a "Yeah?"
    z "You broke today. I saw it. Good."
    z "Broken things can be rebuilt. Glass can't."
    z "Decide which one you want to be."

    "{i}She fades into fog. The device is heavy in his hand.{/i}"

    a "{i}I'm caught between Glass and human.{/i}"
    if em >= 2:
        a "{i}Two hundred lived. That has to mean something.{/i}"
    elif em >= 1:
        a "{i}Some lived. Not enough. Next time has to be different.{/i}"
    else:
        a "{i}She shouldn't have come. And yet she did.{/i}"

    a "{i}Information is power, she said. To see. To choose. To resist.{/i}"
    a "{i}Or to get everyone killed.{/i}"

    # EXIT: Pocket device; turn toward Aeries.
    a "{i}Something bigger is coming. Hundreds of thousands.{/i}"
    a "{i}Blood on my hands. A comm device in my pocket.{/i}"
    a "{i}What the hell am I supposed to do with that?{/i}"

    "{i}The city breathes—unaware. Glass, cracked and walking, heads home.{/i}"

    $ set_scene_flag(_current_scene_id, "completed")
    return


# ========= CANON NOTES =========
# cann.scene_id: act1_19_obsidian_bridge
# cann.when_in_timeline: Midnight after Op 391 (Act 1). Post-confession morning → night meetup.
# cann.what_happened:
#   - Aeron meets Zira at Obsidian Bridge; outcome branches on evidence_of_mercy (em).
#   - HIGH (em≥3): Zira acknowledges meaningful resistance; gives encrypted comm (network access).
#   - MID  (em≥1): Mixed judgment; device given conditionally; urges Aeron to choose a side.
#   - LOW  (em=0): Zira rejects Aeron; no device; exits; route jumps to rooftop reflection.
# cann.aeron_state: VO flavored by band; no empathy momentum added in this scene (judgment only).
# cann.path_tracking:
#   - No player menu; record-only markers set:
#       • bridge_high_mercy_path / bridge_moderate_mercy_path / bridge_low_mercy_path
#   - Flags: device_given | device_given_conditional | device_withheld | completed.
#   - Social: add_trust("Zira", +3 / +1 / −2) and char flags noted above.
#   - Running window BEFORE:   **≈ [-55, +57]**   (from act1_18b)
#   - Running window AFTER:    **≈ [-55, +57]**   (no EMP/OB change here).
# cann.thematic_flags: Judgment after atrocity; trying vs obeying; “information as agency”; crack vs shatter.
# cann.block_status: VARIANT (state-reactive, no player choice).
# cann.true_path_integration: None (TP remains menu-free).
# cann.visual_plate_economy:
#   - REUSE: Bridge master (moonlight pass), rail closeups, fog plates; city BG loop.
#   - HERO: Device handoff insert; two-shot at rail; Zira fog entrance/exit silhouettes.
# cann.requires_followup:
#   - If device_given(_conditional): unlock comm pings in later scenes; optional intel prompts.
#   - If device_withheld: Zira route cools; re-earn trust gated by later high-mercy acts.
#   - Tease multi-sector purge (8–10) in news/ambient chatter within 1–2 scenes.
# cann.consistency_asserts:
#   - Keep casualty language aligned with Op 391 outcomes (em-based lines already mapped).
#   - Aeries altitude/weather grammar elsewhere; here bridge microclimate allows fog/wind.