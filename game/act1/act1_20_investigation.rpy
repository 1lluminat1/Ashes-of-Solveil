# =======================================================
# ACT 1 - Scene 20: Investigation - Morning After
# File: act1_20_investigation.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_20_investigation"
$ scene_mark(_current_scene_id, "entered")


label act1_investigation:

    # VISUAL: Aeron's apartment. Morning light harsh through window. Unmade bed.
    # LIGHTING: Cold morning white; sterile, clinical, unforgiving.
    # SOUND: City hum; ventilation; his breathing; terminal beeping softly.

    "Morning. The light is too bright. The room too quiet."
    "He didn't sleep. Couldn't. Every time he closed his eyes—faces."

    # Setup (BC-safe reads)
    $ em = player_state.get("evidence_of_mercy", 0)
    $ has_device = has_tool("encrypted_comm") or check_scene_flag("act1_19_obsidian_bridge","device_given") or check_scene_flag("act1_19_obsidian_bridge","device_given_conditional")
    $ zira_trusts = char_flag_has("Zira","trusts_aeron") or (characters["Zira"].get("trust",0) >= 2)

    # Soft aliases for sweep callbacks (be tolerant to naming)
    $ saved_child   = check_scene_flag("act1_17_sweep","child_spared") or check_scene_flag("act1_17_sweep","saved_child") or check_scene_flag("act1_17_sweep","lied_child_clear")
    $ saved_vendor  = check_scene_flag("act1_17_sweep","vendor_spared") or check_scene_flag("act1_17_sweep","saved_vendor") or check_scene_flag("act1_17_sweep","ordered_vendor_run")
    $ saved_shelter = check_scene_flag("act1_17_sweep","shelter_warned") or check_scene_flag("act1_17_sweep","shelter_scattered") or check_scene_flag("act1_17_sweep","saved_shelter")

    # VISUAL: Aeron sitting on edge of bed. Still in clothes from yesterday (changed from tactical gear).
    # Body language: Exhausted. Hollow. Broken but still breathing.

    athought "Yesterday I killed 600 people."
    athought "Then I broke down completely. Shattered. Lyra held me together."
    athought "Last night I met Zira. She gave me... something. Information. Access."
    athought "I should feel different. Changed."
    athought "...I just feel empty."

    # --- Device? ---
    if has_device or em >= 1:
        "The device blinks. Soft red pulse. Waiting."
        athought "Zira said use it when I'm ready. Ready for what?"
        athought "To see what's really happening. To choose."
        "The interface loads. Clean. Simple. Civilian-grade encryption."
        "Data streams scroll—resistance network chatter, energy readings, movement logs."
        athought "Let's see what Glass couldn't."
    else:
        "No device. No secret network. Just official channels."
        athought "Glass sees what Echelon allows Glass to see."
        athought "Maybe that's safer. Maybe ignorance is mercy."
        "The terminal loads. Standard protocols. Clean data. Approved information."

    # ==========================================
    # DISCOVERY 1: RESISTANCE CHATTER
    # ==========================================
    if has_device or em >= 1:
        "Messages flood the screen. Resistance networks. Active. Urgent."
        "[ENCRYPTED] - Sector 10 survivors confirm: Echelon sweep yesterday."
        "[ENCRYPTED] - Glass unit showed mercy. Some escaped. Spread word."
        "[ENCRYPTED] - Evacuate Sectors 8, 9, 10 immediately. Something coming."
        "[ENCRYPTED] - Move families to safe zones. Time unknown. Days? Hours?"

        athought "They're alive. The ones I saved. They're warning others."
        athought "200 people spreading word. Families evacuating."
        athought "My mercy... it's helping. It's actually helping."
        athought "Maybe breaking Glass was right. Maybe humanity isn't weakness."

        if saved_shelter:
            "[ENCRYPTED] - Shelter survivors organizing evacuation routes."
            athought "The shelter. 150 people. They're organizing. Leading others out."
            athought "I saved them. And now they're saving more."

        if saved_vendor:
            "[ENCRYPTED] - Contact 'Brew' establishing safe house in Sector 6."
            athought "'Brew.' The vendor. He's alive. Setting up safe houses."
            athought "I let him run. And he's helping others run too."

        athought "This is what Zira meant. This is why trying matters."
        athought "I can't save everyone. But the ones I save... they save others."
        athought "Ripples. Small mercies creating bigger ones."
    else:
        "No chatter. No intercepts. Just official Echelon reports."
        "[OFFICIAL] - Sector 10 sweep complete. 800 eliminated. Zero survivors."
        "[OFFICIAL] - Sector secured. Mission success. No complications."
        athought "That's what the report says. 800 eliminated. Zero survivors."
        athought "But I know better. 200 are alive. Somewhere."
        athought "The system doesn't know. Or doesn't care to know."
        athought "Maybe that's good. Maybe their survival depends on invisibility."

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
        "The energy data sits on screen. Something feels wrong. But what?"
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

    athought "Father. He only calls when he needs Glass."
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

    # If has device, try searching for 'Project Renewal'
    if has_device or em >= 1:
        "Searches Zira's network: 'Project Renewal.'"
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
    "He stands. Paces. The room feels smaller."

    athought "Resistance networks active. Survivors evacuating. That's good."
    athought "Energy maintenance scheduled. Shields offline. That's... concerning."
    athought "Project Renewal. Marcus wants me to witness. That's... what?"
    athought "Troop evacuations. Civilians locked down. That's..."
    athought "The pieces don't fit. Or they do and I'm not seeing it."
    athought "Something's happening tonight. Something big."
    athought "Zira warned me. 'Days not weeks.' She meant tonight."

    athought "I can't think. I'm too exhausted. Too broken."
    athought "Yesterday I killed 600 people. Shattered completely. Lyra held me together."
    athought "I can't handle more horror. Not today. Not yet."
    athought "It's a drill. Or a lockdown. Or infrastructure work."
    athought "It's not—it can't be—"
    athought "Father wouldn't order mass extermination. The system has limits."
    athought "...Doesn't it?"

    menu:
        "The data sits there. Pieces scattered. Picture incomplete. Dread building."
        "Keep digging—try to find the full picture.":
            $ record_choice_once(_current_scene_id, "kept_investigating")

            "He searches. Hours pass. Data upon data. Fragments. Pieces."
            "But the picture won't form. Too classified. Too compartmentalized."
            athought "I can't find it. Whatever's happening, it's locked down tight."

            athought "Only Marcus knows. And he's not telling Glass."
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
    "Time moves like sludge. Every minute heavy with dread."

    athought "I can't stay here. Staring at data I don't understand."
    athought "I need air. I need to think. I need to..."
    athought "...I need to be somewhere Kael used to be."

    athought "The rooftop. Where you stood. Where you chose."
    athought "Maybe being there will help me understand."
    athought "Understand what's coming. Understand what I'm supposed to do."
    athought "Understand if any of this matters."

    "He grabs his jacket. The device goes in his pocket."
    "One last look at the room. The terminal still glowing. Data still waiting."

    athought "200 people alive because I broke Glass."
    athought "Something big happening tonight because they warned others."
    athought "My mercy rippling outward. But into what?"
    athought "Victory? Or catastrophe?"

    "The corridor is empty. No officers. No servants. No witnesses."
    "Just Glass, walking toward answers he doesn't want."

    athought "2000 hours. Command deck. 'Witness history,' Father said."
    athought "But first... the rooftop. Where Kael made his choice."
    athought "Maybe I need to make mine."

    # Bookkeeping
    $ set_scene_flag(_current_scene_id, "completed")
    return


# ========= CANON NOTES =========
# cann.scene_id: act1_20_investigation
# cann.when_in_timeline: Morning/afternoon after Sector 10 sweep; before 20:00 “Project Renewal” observation.
# cann.what_happened:
#   - Processes aftermath; device vs. official-feed fork; confirms survivor chatter and grid anomaly.
#   - Marcus assigns OBSERVER role for Project Renewal; troops evacuated; civilians shelter-in-place.
# cann.aeron_state: Exhausted; denial→dread; cognition > action.
# cann.path_tracking:
#   - Choices are record-only (no momentum):
#       • record_choice_once("investigated_energy" | "dismissed_energy")
#       • record_choice_once("kept_investigating" | "stopped_investigating")
#   - Scene empathy delta: **0**.
#   - Running window BEFORE:   **≈ [-55, +57]**
#   - Running window AFTER:    **≈ [-55, +57]** (unchanged)
# cann.thematic_flags: Seeing vs doing; compartmentalization; denial as armor.
# cann.block_status: ANCHOR (Act I setup for command deck/rooftop).
# cann.true_path_integration: none.
# cann.visual_plate_economy:
#   - REUSE Aeries apartment master; UI plates (encrypted vs official), grid map 8–10 offline, secure-call frame.
# cann.requires_followup:
#   - Route to rooftop reflection, then command-deck observation at 20:00.
# cann.consistency_asserts:
#   - Aeries altitude weather grammar only (no rain).
#   - Keep Marcus phrasing consistent (“observation only”, “perfection”).