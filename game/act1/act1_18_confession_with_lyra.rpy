# =======================================================
# ACT 1 - Scene 18: Confession with Lyra - The Breakdown
# File: act1_18_confession_with_lyra.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_18_confession_lyra"
$ scene_mark(_current_scene_id, "entered")


label act1_confession_lyra:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Slow push from doorway to mid on Aeron; rack focus to Lyra; dolly in during breakdown.
    # LIGHTING: Window amber vs interior cold; dust motes visible in the beam.
    # SFX LOOP: Faint ventilation; distant city hum as a low bed.
    # SFX ONE-SHOTS: Door seal hiss; knees hitting floor; fabric creak.
    # BLOCKING: Aeron's apartment. Late afternoon. Lyra waiting on the bed.
    # PROP: Dried blood flecks on Aeron's sleeve (not his).

    #scene bg_apartment_afternoon with fade

    # ========= OPENING — THE RETURN =========

    "The door seals behind me. The room is too quiet."

    "And Lyra is there. Sitting on my bed. Waiting."

    l "Aeron."

    # CAMERA: Hold. Beat. Let the stillness bite.
    pause 0.4

    # VISUAL: Aeron stops just inside; dried blood flecks on the sleeve (not his).

    athought "She's here. Why is she here?"

    l "(steps closer) I heard about the mission. Sector Ten."

    a "(flat) It's done. Mission complete."

    l "That's not what I asked."

    l "(softer) What happened down there?"

    # ========= HOLDING TOGETHER =========
    # CAMERA: Over-shoulder on Aeron; jaw clenched; eyes not tracking her.

    a "Sweep operation. Standard protocol. Within parameters."

    if empathy_band() == "obedience":
        a "(quieter) It was efficient."
    else:
        a "(barely holding together) It was... efficient."

    l "Aeron—"

    a "Eight hundred targets. Sector secured. Marcus is satisfied."

    l "Stop reporting and talk to me."

    athought "Report. Function. Don't break. Don't break."

    a "(strained) I'm fine. Just tired. I need to—"

    # ========= TOUCH =========
    # VISUAL: Lyra lifts a hand—hesitates—sets it on his forearm.

    a "(sharp) Don't—"

    l "(quiet) Aeron. Look at me."

    athought "If I look at her, it's over. The dam breaks."

    l "(barely a whisper) How many?"

    # ========= CRACKS SPREADING =========

    a "...The report says eight hundred."

    l "I didn't ask what the report says. I asked how many YOU killed."

    a "Protocol 7-Alpha... authorizes lethal force against... against..."

    athought "The words turn to ash. The code won't come."

    a "(voice breaking) I—I tried to—"

    l "How many, Aeron?"

    if mercy_ge(2):
        a "...Six hundred. Maybe more. I saved some. I tried. But—"
    else:
        if empathy_band() == "obedience":
            a "...All of them. I followed the order."
            a "(flat) That's what I'm made for."
        else:
            a "...All of them. I killed all of them."

    l "(breathes in sharply) Aeron..."

    # ========= THE FLOOD =========
    # CAMERA: Slow dolly in; shallow depth—world narrows to two faces.

    a "There was a vendor. I bought coffee from him. Three nights ago."

    a "He recognized me. He knew I'd come. He didn't run."

    if scene_has("act1_17_sweep", "vendor_spared"):
        a "I let him go. Broke protocol. The team saw. But I couldn't kill him."
    else:
        a "I killed him. Three rounds. Center mass. Professional."
        a "He died reaching for his brew pot. Said it was better than Aeries coffee."

    if empathy_band() == "obedience":
        a "(voice shaking) He knew me. Still didn't run. That was... uncalculated."
        a "(low) I shouldn't care. But I remember the smell. The warmth. Why do I remember it?"

    a "And there was a child. Just a child. Hiding behind a door."

    if scene_has("act1_17_sweep", "child_spared"):
        a "I lied to the team. Said thermal was a glitch. Left her alive."
        a "But how many others didn't get that mercy?"
    else:
        a "My team breached. She screamed once. Then silence."
        a "Eight years old. No weapon. Just terrified."

    a "There were two hundred people in a shelter. Families. Elders. Children."

    if scene_has("act1_17_sweep", "shelter_scattered"):
        a "I warned them. Flashbang. Gave them time to scatter. One-fifty escaped. Fifty didn't."
    else:
        a "We breached. Charges. Smoke. Two hundred people. Gone in minutes."

    a "They weren't rebels. They were just trying to live. And Marcus said—"

    a "He said, 'prove your worth.' So I did."

    # VISUAL: Aeron sways; grabs desk edge.

    "Knees buckling. Desk edge biting into his palms as the room spins around him."

    a "(whisper) Three hundred ninety times..."

    a "How many families? How many lies?"

    # SFX: Fabric creak; knees hit floor.

    "The floor rushes up. Knees crack against tile but the impact barely registers."

    if empathy_band() == "obedience":
        a "(hollow) I failed."
        a "I was supposed to be perfect. Three-nine-one... flawless."
        athought "The numbers don't add up anymore."
    else:
        a "(hollow) I killed them."
        a "I looked at them... and I ended them."
        athought "The weight of it. It doesn't crush me, it just empties me."

    "No screaming. No sobbing. Just a silence so loud it hurts."

    "He sits there, staring at nothing. A machine that ran out of fuel."

    l "(quiet) Breathe. Just breathe. I'm here."

    if empathy_band() == "obedience":
        athought "She touches me. I should push her away. Discipline demands distance."
        athought "But I can't move. The system says suppress. The body refuses."
    else:
        athought "Her touch is the only real thing in the room."

    # VISUAL: He leans forward; head hangs low, not touching her yet. Defeated posture.

    "He leans forward, head hanging between his shoulders. Shaking, but dry-eyed."

    a "(voice rough) How do you do it?"

    a "How do you just... turn it off?"

    l "(soft) You don't. You just carry it."

    a "(broken whisper) I don't want to be this anymore. I can't."

    # ========= LYRA BREAKS =========
    # CAMERA: On Lyra; mask finally slips; tear track catches window light.

    # VISUAL: Close on Lyra. She isn't sobbing. She's leaking.

    "Lyra doesn't shatter. She just... spills over."

    "A single tear tracks down her cheek. She doesn't wipe it away. She doesn't even seem to notice it."

    l "(voice steady, but thin) I know. I did it too. Sector Seven."

    l "Families. Children. I logged them."

    l "Three days later... silence."

    # VISUAL: She closes her eyes; the tears come faster now, but still silent.

    l "(tight) I told myself it was necessary."

    l "But I can't stop seeing them."

    "She holds me tighter. A desperate, rigid grip. Holding on so she doesn't fall too."

    l "We're not weapons, Aeron."

    l "(trembling) Weapons don't hurt like this."

    l "We do."

    if empathy_band() == "obedience":
        a "(hoarse) I can't keep breaking like this."
        l "Then stop letting him break you."
        a "(bitter) That's all I'm built for."
    else:
        a "(sobbing) I can't be his weapon anymore."

    l "Then don't. You don't have to."

    a "He owns me. The system owns me."

    l "(fierce) Then we break free. Together."

    # SFX: City hum dips under; let breathing lead.

    "We sit in the ruins. Time dissolves. Just breath. Just tears."

    # ========= AFTER THE STORM =========
    # CAMERA: Wider two-shot; window beam softer now; colors cooler.

    "Silence settles. Not the kind that brings peace, just emptiness after the flood."

    l "(hoarse) How do you feel?"

    a "(barely audible) ...Empty."

    l "Good. You needed to be."

    a "I killed six hundred people today."

    l "I know."

    a "How do I live with that?"

    l "(quiet) We learn together."

    "Her hand finds his—an anchor in the void."

    l "You tried to save them. That's more than obedience would allow."

    a "I didn't save enough."

    l "No one could have."

    a "Then what was the point?"

    l "You fought the orders from within. That's human."

    a "I'm so tired."

    l "Then rest. Just breathe. Tomorrow we figure it out."

    a "What if I can't be fixed?"

    l "Then we're broken together."

    l "Windows recognize windows. But we're not windows anymore."

    "They sit. The city hums beyond the pane. Broken but not alone."

    a "(whisper) Thank you."

    l "For what?"

    a "For seeing me."

    l "I've always seen you. Even when you couldn't."
    #TODO WRONG
    "She leans against me. I don't pull away."

    l "We'll get through this."

    a "How can you be sure?"

    l "I'm not. But we'll try."

    "Evening falls. No one turns on the lights. Just surviving the moment."

    # ========= EMPATHY VARIANT TONE =========

    if empathy_band() == "empathy":
        athought "Something shattered tonight. What's left still feels human."
    elif empathy_band() == "obedience":
        athought "The cracks opened—but obedience still whispers. I don't know which voice will win."
    else:
        athought "Between broken and whole, there's this—breathing. Barely."

    if empathy_band() == "obedience":
        athought "Operation 391 complete. Error detected: deviation under emotional strain."
        athought "I'll fix it. I'll fix myself. Next time, no cracks."
        athought "Lyra's still here. She shouldn't be."
    else:
        athought "Operation 391 is complete."
        athought "Something shattered on the floor of my apartment."
        athought "And for the first time in ten years... I felt it all."

    # LIGHT SOCIAL STATE: vulnerability breeds trust
    $ rel_bump("Lyra", 1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_18_confession_lyra
# cann.when_in_timeline: Late afternoon/evening, post–Sector 10 sweep (Op 391); pre–Obsidian Bridge contact.
# cann.what_happened:
#   - Aeron returns shattered; Lyra confronts report-vs-truth; he breaks and confesses details.
#   - Lyra reciprocates with Sector 7 guilt; they share grief; vow to "break free together."
# cann.aeron_state: VO tinted by empathy band only (no momentum changes).
# cann.path_tracking:
#   - No menus. No OB/EMP delta (NEU scene).
#   - Pulls detail variants via flags from act1_17_sweep.
#   - Social: rel_bump("Lyra", +1) baseline for vulnerability.
# cann.thematic_flags: Report vs confession; moral injury; weapon vs human; shared culpability as connection.
# cann.block_status: ANCHOR (fixed outcome, variant details).
# cann.visual_plate_economy:
#   - REUSE: Apartment master; window amber pass; desk/floor 2-shot.
#   - HERO: Knees hit floor; Lyra's tear catching the window beam; hands interlace CU.
# cann.requires_followup:
#   - Obsidian Bridge rendezvous setup; Marcus debrief tone colored by Op 391 outcomes.