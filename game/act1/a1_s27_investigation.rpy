# =======================================================
# ACT 1 - Scene 20: Investigation - Morning After
# File: a1_s27_investigation.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a1_s27_investigation"
$ scene_mark(_current_scene_id, "entered")


label a1_s27_investigation:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Static apartment wide; terminal inserts; pacing coverage.
    # LIGHTING: Cold morning white; sterile, clinical, unforgiving.
    # SFX LOOP: City hum; ventilation; terminal beeping softly.
    # BLOCKING: Aeron's apartment. Morning light harsh through window. Unmade bed.
    # FX/COMP: UI plates (encrypted vs official), grid map, secure-call frame.

    #scene bg_apartment_morning_investigation with fade

    # ========= OPENING — THE AFTERMATH =========

    "Morning. The light is too bright. The room too quiet."

    athought "I didn't sleep. Couldn't. Every time I closed my eyes—faces."

    # Setup (BC-safe reads)
    $ em = mercy_total()
    $ has_device = has_tool("encrypted_comm") or scene_has("a1_s26_obsidian_bridge", "device_given") or scene_has("a1_s26_obsidian_bridge", "device_given_conditional")
    $ zira_trusts = char_flag_has("Zira", "trusts_aeron") or (characters["Zira"].get("trust", 0) >= 2)

    # Soft aliases for sweep callbacks
    $ saved_child = scene_has("a1_s23_the_sweep", "child_spared")
    $ saved_vendor = scene_has("a1_s23_the_sweep", "vendor_spared")
    $ saved_shelter = scene_has("a1_s23_the_sweep", "shelter_scattered")

    # VISUAL: Edge of bed. Still in clothes from yesterday. Exhausted. Hollow.

    athought "Lyra kept me from coming apart."

    athought "Zira left me with a choice."

    athought "...I still wake up empty."

    # ========= DEVICE CHECK =========

    if has_device:
        "The device blinks—soft red pulse, waiting."

        athought "Zira said use it when I'm ready. Ready for what?"

        athought "To see what's really happening. To choose."

        "The interface loads. Clean. Simple. Civilian-grade encryption."

        "Data streams scroll—resistance network chatter, energy readings, movement logs."

        athought "Let's see what I couldn't before."
    else:
        "No device. No secret network. Just official channels."

        athought "I see what Echelon allows me to see."

        athought "Maybe that's safer. Maybe ignorance is mercy."

        "The terminal loads. Standard protocols. Clean data. Approved information."

    # ==========================================
    # DISCOVERY 1: RESISTANCE CHATTER
    # ==========================================

    if has_device:
        "Messages flood the screen. Resistance networks. Active. Urgent."

        "[ENCRYPTED] - Sector 10 survivors confirm: Echelon sweep yesterday."

        "[ENCRYPTED] - Glass unit showed mercy. Some escaped. Spread word."

        "[ENCRYPTED] - Evacuate Sectors 8, 9, 10 immediately. Something coming."

        "[ENCRYPTED] - Move families to safe zones. Time unknown. Days? Hours?"

        athought "They're alive. The ones I saved. They're warning others."

        athought "Mercy moved. It didn't die with the sector."

        if saved_shelter:
            "[ENCRYPTED] - Shelter survivors organizing evacuation routes."

            athought "The shelter survivors are moving people out."

        if saved_vendor:
            "[ENCRYPTED] - Contact 'Brew' establishing safe house in Sector 6."

            athought "'Brew.' He's alive. Still moving people."

        athought "This is what she meant."

    else:
        "No chatter. No intercepts. Just official Echelon reports."

        "[OFFICIAL] - Sector 10 sweep complete. 800 eliminated. Zero survivors."

        "[OFFICIAL] - Sector secured. Mission success. No complications."

        athought "That's what the report says. Zero survivors."

        if em >= 1:
            athought "The report is lying."
        else:
            athought "If it isn't lying, then the sector is gone."

    # ==========================================
    # DISCOVERY 2: ENERGY GRID ANOMALIES
    # ==========================================

    "Energy grid data loads. Sectors 8, 9, 10. Scheduled maintenance tonight."

    "[GRID ALERT] - Scheduled power reduction: Sectors 8-10."

    "[MAINTENANCE] - Infrastructure repairs following sweep operations."

    "[TIMELINE] - Execution window: 2000-2300 hours. Duration: 3 hours."

    athought "Power reduction? Three-hour window? That's... extensive."

    "[TECHNICAL] - Grid sectors 8A through 10F: Complete shutdown."

    "[TECHNICAL] - Shield generators offline during maintenance."

    "[TECHNICAL] - Emergency protocols suspended: 2000-2300 hours."

    athought "Shield generators offline? That's... unusual."

    athought "Why would they shut down shields during maintenance?"

    athought "Safety protocol is to keep shields UP during repairs..."

    menu:
        athought "The energy data sits on screen. Something feels wrong. But what?"

        "Investigate further—check historical maintenance patterns.":
            $ record_choice_once(_current_scene_id, "investigated_energy")

            "Historical maintenance logs. Comparing patterns."

            "Past maintenance: Shields stay active. Repairs done in sections. Never full shutdown."

            "Tonight: All shields offline. All sectors simultaneously. Complete shutdown."

            athought "That's not standard. That's not... safe."

            athought "Why would they expose three sectors completely?"

            athought "Unless..."

            athought "Unless they're not worried about protection. Because nothing's there to protect."

            athought "But that doesn't make sense. Thousands of people live in those sectors."

            athought "...Don't they?"

            athought "I'm missing something. But I can't see it."

        "Dismiss it—too exhausted to think clearly.":
            $ record_choice_once(_current_scene_id, "dismissed_energy")

            athought "I'm too tired for this. Seeing problems where there aren't any."

            athought "It's maintenance. Routine. Boring. Nothing to worry about."

            athought "I need to stop looking for horror everywhere."

    # ==========================================
    # DISCOVERY 3: MARCUS'S ORDERS
    # ==========================================

    "Notification. Incoming transmission. High priority. Command level."

    "Source: High Marshal Marcus Rylan."

    athought "Father. He only calls when he needs me."

    athought "What now? Another mission? Another sector to erase?"

    m "Glass. Status report."

    a "Sector 10 sweep complete. Mission successful."

    m "Casualties?"

    if em >= 2:
        a "800 confirmed. Zero survivors."
        m "(pause) ...Excellent. Clean execution."
        athought "He believes it. The lie holds."
    else:
        a "800 confirmed."
        m "Within parameters. Good."

    m "New directive. Stand by for deployment orders."

    a "(tense) Another sweep?"

    m "No. Observation duty. Upper Aeries. Tonight. 2000 hours."

    a "Observation? That's not—"

    m "(cuts him off) You've earned rest, Glass. Tonight, you watch. You don't act."

    m "Report to command deck. Observation only. Understood?"

    athought "Observation duty? Marcus never assigns me observation."

    athought "He uses me to cut. Not to watch."

    athought "What's happening tonight that he wants me to SEE but not DO?"

    a "...Understood. 2000 hours. Command deck."

    m "Good. Project Renewal executes tonight. You'll witness history."

    m "Solveil takes another step toward perfection."

    if has_device:
        "Searching Zira's network: 'Project Renewal.'"

        "No results. No mentions. Completely dark."

        athought "Nothing. Either it's too classified or too new."

        athought "Zira doesn't know. Resistance doesn't know."

        athought "Only Marcus knows. And he wants me to watch."

    # ==========================================
    # DISCOVERY 4: TROOP MOVEMENTS
    # ==========================================

    "Deployment schedules. Troop movements. Routine checks."

    "[DEPLOYMENT] - All Echelon units: Evacuate Sectors 8-10 by 1900 hours."

    "[DEPLOYMENT] - Redeployment to Upper Aeries. Command deck observation stations."

    "[DEPLOYMENT] - Civilian personnel: Shelter-in-place orders. Sectors 8-10."

    athought "Evacuate Echelon personnel. But civilians shelter-in-place?"

    athought "That's backwards. If something dangerous is happening, you evacuate civilians first."

    athought "Unless..."

    athought "Unless you don't want civilians to leave."

    athought "Unless you want them exactly where they are."

    athought "Contained. Counted. Targeted."

    athought "No. No, that's not—"

    athought "Father wouldn't—"

    athought "The system wouldn't—"

    athought "It's a drill. Security exercise. Testing evacuation protocols."

    athought "That's why Echelon evacuates and civilians shelter. It's a test."

    athought "It has to be a test."

    # ==========================================
    # SYNTHESIS
    # ==========================================

    "The room feels smaller. Walls pressing in."

    athought "The pieces don't fit."

    athought "Zira said days. Marcus said tonight."

    athought "Troops out. Civilians locked in. Shields down."

    athought "It should mean something obvious."

    athought "I keep refusing to see it."

    menu:
        athought "The data sits there. Pieces scattered. Picture incomplete. Dread building."

        "Keep digging—try to find the full picture.":
            $ record_choice_once(_current_scene_id, "kept_investigating")

            "Hours pass. Data upon data. Fragments. Pieces."

            "But the picture won't form. Too classified. Too compartmentalized."

            athought "I can't find it. Whatever's happening, it's locked down tight."

            athought "Only Marcus knows. And he's not telling me."

            athought "He wants me to watch. To witness. To learn something."

            athought "But what?"

            athought "I can't do this. I need air. I need to think."

        "Stop investigating—too exhausted to continue.":
            $ record_choice_once(_current_scene_id, "stopped_investigating")

            athought "I can't. I'm too tired. Too broken."

            athought "Whatever's happening... I'll find out at 2000 hours."

            athought "Marcus wants me on command deck. I'll see it then."

            athought "Right now I just need... air. Space. Distance from all of this."

    # ==========================================
    # DECISION TO GO TO ROOFTOP
    # ==========================================

    "Afternoon light slants through the window. Hours until 2000."

    athought "Time moves like sludge. Every minute heavy with dread."

    athought "I can't stay here. Staring at data I don't understand."

    athought "I need air. I need to think. I need to..."

    athought "...I need to be somewhere Kael used to be."

    athought "The rooftop. Where you stood. Where you chose."

    athought "Maybe being there will help me understand."

    athought "Understand what's coming. Understand what I'm supposed to do."

    athought "Understand if any of this matters."

    if has_device:
        "Jacket on. Device in pocket."
    else:
        "Jacket on. Hands empty."

    "One last look at the room. The terminal still glowing. Data still waiting."

    if em >= 1:
        athought "Somebody is still breathing because I broke formation."

        athought "I don't know what that buys them tonight."

    "The corridor is empty. No officers. No servants. No witnesses."

    athought "2000 hours. Command deck. 'Witness history,' Father said."

    athought "But first... the rooftop. Where Kael made his choice."

    athought "Maybe I need to make mine."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a1_s27_investigation
# cann.when_in_timeline: Morning/afternoon after Sector 10 sweep; before 20:00 "Project Renewal."
# cann.what_happened:
#   - Processes aftermath; device vs official-feed fork; confirms survivor chatter and grid anomaly.
#   - Marcus assigns OBSERVER role for Project Renewal; troops evacuated; civilians shelter-in-place.
# cann.aeron_state: Exhausted; denial→dread; cognition > action.
# cann.path_tracking:
#   - Choices are record-only (no momentum):
#       • investigated_energy | dismissed_energy
#       • kept_investigating | stopped_investigating
#   - Scene empathy delta: 0.
# cann.thematic_flags: Seeing vs doing; compartmentalization; denial as armor.
# cann.block_status: ANCHOR (Act I setup for command deck/rooftop).
# cann.visual_plate_economy:
#   - REUSE: Aeries apartment master; UI plates, grid map 8–10 offline, secure-call frame.
# cann.requires_followup:
#   - Route to rooftop reflection, then command-deck observation at 20:00.
# cann.note_on_glass_usage:
#   - Marcus uses "Glass" as Aeron's callsign (character dialogue—kept).
#   - Aeron's internal self-references replaced with first-person language.
