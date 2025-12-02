# =======================================================
# ACT 1 - Scene 18: Confession with Lyra - The Breakdown
# File: act1_18_confession_with_lyra.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_18_confession_lyra"
$ scene_mark(_current_scene_id, "entered")

label act1_confession_lyra:

    # Read alignment via helpers (flavor only; no momentum)
    $ band = get_empathy_band()            # "obedience" | "conflicted" | "empathy"
    $ is_obedient_path = (band == "obedience")

    # VISUAL: Aeron's apartment. Late afternoon light sliding across the floor; corridor spill behind Lyra.
    # LIGHTING: Window amber vs interior cold; dust motes visible in the beam.
    # SOUND: Door seal hiss; faint ventilation; distant city hum as a low bed.
    # CAMERA: Slow push from doorway to a mid on Aeron; keep Lyra soft in BG, then rack focus on her first line.

    "The door seals behind him. The room is too quiet."
    "And Lyra is there. Sitting on his bed. Waiting."

    l "Aeron."

    # CAMERA: Hold. Beat. Let the stillness bite.
    pause 0.4

    # VISUAL: Aeron stops just inside; dried blood flecks on the sleeve (not his).
    "He stands there. Can't move forward. Can't turn back."

    athought "She's here. Why is she here?"

    l "(steps closer) I heard about the mission. Sector Ten."
    a "(flat) It's done. Mission complete."
    l "That's not what I asked."
    l "(softer) What happened down there?"

    # ---- HOLDING GLASS TOGETHER ----
    # CAMERA: Over-shoulder on Aeron; jaw clenched; eyes not tracking her.
    a "Sweep operation. Standard protocol. Within parameters."
    if is_obedient_path:
        a "(quieter) It was efficient."
    else:
        a "(barely holding together) It was... efficient."

    l "Aeron—"
    a "Eight hundred targets. Sector secured. Marcus is satisfied."
    l "Stop reporting and talk to me."

    "Glass doesn’t break. Glass reports. Glass functions."

    a "(strained) I’m fine. Just tired. I need to—"

    # TOUCH
    # VISUAL: Lyra lifts a hand—hesitates—sets it on his forearm.
    a "(sharp) Don’t—"
    l "(quiet) Aeron. Look at me."
    athought "If I look at her, it’s over. The dam breaks."

    l "(barely a whisper) How many?"

    # ---- CRACKS SPREADING ----
    a "...The report says eight hundred."
    l "I didn’t ask what the report says. I asked how many YOU killed."

    a "(voice breaking) I—I tried to—"
    l "How many, Aeron?"

    if mercy_ge(2):
        a "...Six hundred. Maybe more. I saved some. I tried. But—"
    else:
        if is_obedient_path:
            a "...All of them. I followed the order."
            a "(flat) That’s what I’m made for."
        else:
            a "...All of them. I killed all of them."

    l "(breathes in sharply) Aeron..."

    # ---- THE FLOOD ----
    # CAMERA: Slow dolly in; shallow depth—world narrows to two faces.
    a "There was a vendor. I bought coffee from him. Three nights ago."
    a "He recognized me. He knew I’d come. He didn’t run."

    if check_scene_flag("act1_17_sweep", "vendor_spared"):
        a "I let him go. Broke protocol. The team saw. But I couldn’t kill him."
    else:
        a "I killed him. Three rounds. Center mass. Professional."
        a "He died reaching for his brew pot. Said it was better than Aeries coffee."

    if is_obedient_path:
        a "(voice shaking) He knew me. Still didn’t run. That was... uncalculated."
        a "(low) I shouldn’t care. But I remember the smell. The warmth. Why do I remember it?"

    a "And there was a child. Just a child. Hiding behind a door."

    if check_scene_flag("act1_17_sweep", "child_spared"):
        a "I lied to the team. Said thermal was a glitch. Left her alive."
        a "But how many others didn’t get that mercy?"
    else:
        a "My team breached. She screamed once. Then silence."
        a "Eight years old. No weapon. Just terrified."

    a "There were two hundred people in a shelter. Families. Elders. Children."

    if check_scene_flag("act1_17_sweep", "shelter_warned"):
        a "I warned them. Flashbang. Gave them time to scatter. One-fifty escaped. Fifty didn’t."
    else:
        a "We breached. Charges. Smoke. Two hundred people. Gone in minutes."

    a "They weren’t rebels. They were just trying to live. And Marcus said—"
    a "He said, 'prove your worth.' So I did."

    # VISUAL: Aeron sways; grabs desk edge.
    "His knees buckle. He catches the desk. Barely standing."

    a "(yelling) I’ve done this three hundred ninety times! How many families? How many lies?"

    # SFX: Fabric creak; knees hit floor.
    "He falls. Crashes to his knees. The impact doesn’t register."

    if is_obedient_path:
        a "(yells) I FAILED—"
        a "(hoarse) I was supposed to be perfect! Three-nine-one flawless operations!"
    else:
        a "(screaming) I KILLED THEM—"

    "Ten years of silence shatters. Ten years of Glass cracks wide open."

    a "(sobbing) I’m sorry—I tried—it’s never enough—"
    a "(gasping) I can’t breathe—there’s blood—everywhere—"

    l "(quiet) Breathe. Just breathe. I’m here."

    if is_obedient_path:
        athought "She touches me. I should push her away. Discipline demands distance."
        athought "But I can’t move. The system says suppress. The body disobeys."
    else:
        athought "Her touch anchors me. Pulls me back to something human."

    # VISUAL: He collapses into her; foreheads touch; shoulders shake.
    "He collapses into her. Full weight. Broken sound. Human sound."

    a "(barely coherent) How do you live with it? I see their faces—every time—"
    a "(screaming) I DON’T WANT TO BE THIS ANYMORE—"

    # ---- LYRA BREAKS ----
    # CAMERA: On Lyra; mask finally slips; tear track catches window light.
    "Lyra’s mask shatters. Tears streak down."

    l "(voice breaking) I know. I did it too. Sector Seven."
    l "Families. Children. I logged them. Three days later—they were gone."
    l "(crying) I told myself it was necessary. I can’t stop seeing them."

    "She holds him tighter. Two pieces of Glass shattering together."
    l "We’re not Glass. We’re human. And it hurts."
    l "(through tears) But feeling it means we’re still alive."

    if is_obedient_path:
        a "(hoarse) I can’t keep breaking like this."
        l "Then stop letting him break you."
        a "(bitter) That’s all I’m built for."
    else:
        a "(sobbing) I can’t be his weapon anymore."

    l "Then don’t. You don’t have to."
    a "He owns me. The system owns me."
    l "(fierce) Then we break free. Together."

    # SOUND: City hum dips under; let breathing lead.
    "They sit in the ruins of Glass. Time dissolves. Just breath. Just tears."

    # ---- AFTER THE STORM ----
    # CAMERA: Wider two-shot; window beam softer now; colors cooler.
    "Silence settles. Not peace. Just emptiness after the flood."

    l "(hoarse) How do you feel?"
    a "(barely audible) ...Empty."
    l "Good. You needed to be."

    a "I killed six hundred people today."
    l "I know."
    a "How do I live with that?"
    l "(quiet) We learn together."

    "Her hand finds his. Holds tight. Anchor in the void."

    l "You tried to save them. That’s more than Glass would do."
    a "I didn’t save enough."
    l "No one could have."
    a "Then what was the point?"
    l "You fought the orders from within. That’s human."

    a "I’m so tired."
    l "Then rest. Just breathe. Tomorrow we figure it out."
    a "What if I can’t be fixed?"
    l "Then we’re broken together."
    l "Glass recognizes glass. But we’re not Glass anymore."

    "They sit. The city hums beyond the glass. Broken but not alone."

    a "(whisper) Thank you."
    l "For what?"
    a "For seeing me."
    l "I’ve always seen you. Even when you couldn’t."

    "She leans against him. He doesn’t pull away."

    l "We’ll get through this."
    a "How can you be sure?"
    l "I’m not. But we’ll try."

    "Evening falls. No one turns on the lights. Just surviving the moment."

    # EMPATHY VARIANT TONE
    if band == "empathy":
        athought "Glass shattered tonight. What’s left still feels human."
    elif band == "obedience":
        athought "The cracks opened—but obedience still whispers. I don’t know which voice will win."
    else:
        athought "Between broken and whole, there’s this—breathing. Barely."

    if is_obedient_path:
        athought "Operation 391 complete. Error detected: deviation under emotional strain."
        athought "I’ll fix it. I’ll fix myself. Next time, no cracks."
        athought "Lyra’s still here. She shouldn’t be."
    else:
        athought "Operation 391 is complete."
        athought "Glass shattered on the floor of my apartment."
        athought "And for the first time in ten years... I felt it all."

    # LIGHT SOCIAL STATE: vulnerability breeds trust
    $ rel_bump("Lyra", trust=+1)
    $ set_scene_flag(_current_scene_id, "completed")
    return


# ========= CANON NOTES =========
# cann.scene_id: act1_18_confession_lyra
# cann.when_in_timeline: Late afternoon/evening, post–Sector 10 sweep (Op 391); pre–Obsidian Bridge contact.
# cann.what_happened:
#   - Aeron returns shattered; Lyra confronts/report-vs-truth; he breaks and confesses details (vendor/child/shelter).
#   - Lyra reciprocates with Sector 7 guilt; they share grief; vow to “break free together.”
# cann.aeron_state: VO tinted by empathy band only (no momentum changes). Obedience-band frames failure of perfection;
#                   empathy-band frames moral injury & awakening.
# cann.path_tracking:
#   - No menus. **No OB/EMP delta** (NEU scene).
#   - Pulls detail variants via flags from act1_17_sweep: vendor_spared / child_spared / shelter_warned.
#   - Social: `add_trust("Lyra", +1)` baseline for vulnerability.
#   - Running window BEFORE:   **≈ [-48, +48]**
#   - Running window AFTER:    **≈ [-48, +48]** (unchanged; delta 0)
# cann.thematic_flags: Report vs confession; moral injury; “Glass vs Human”; shared culpability as connection.
# cann.block_status: ANCHOR (fixed outcome, variant details).
# cann.true_path_integration: none (menu-free).
# cann.visual_plate_economy:
#   - REUSE: Apartment master; window amber pass; desk/floor 2-shot.
#   - HERO: Knees hit floor; Lyra’s tear catching the window beam; hands interlace CU.
# cann.requires_followup:
#   - Next beats: Obsidian Bridge rendezvous setup; Marcus debrief tone colored by Op 391 outcomes/suspicion.
# cann.consistency_asserts:
#   - Aeries altitude weather grammar: no rain-on-glass FX; keep “window condensation/amber beam” language.
#   - Count integrity: “391 operations” line consistent with prior scenes and debrief totals.