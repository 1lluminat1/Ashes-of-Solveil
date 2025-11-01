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

    "{i}Morning. The light is too bright. The room too quiet.{/i}"
    "{i}He didn't sleep. Couldn't. Every time he closed his eyes—faces.{/i}"

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

    a "{i}Yesterday I killed 600 people.{/i}"
    a "{i}Then I broke down completely. Shattered. Lyra held me together.{/i}"
    a "{i}Last night I met Zira. She gave me... something. Information. Access.{/i}"
    a "{i}I should feel different. Changed.{/i}"
    a "{i}...I just feel empty.{/i}"

    # --- Device? ---
    if has_device or em >= 1:
        "{i}The device blinks. Soft red pulse. Waiting.{/i}"
        a "{i}Zira said use it when I'm ready. Ready for what?{/i}"
        a "{i}To see what's really happening. To choose.{/i}"
        "{i}The interface loads. Clean. Simple. Civilian-grade encryption.{/i}"
        "{i}Data streams scroll—resistance network chatter, energy readings, movement logs.{/i}"
        a "{i}Let's see what Glass couldn't.{/i}"
    else:
        "{i}No device. No secret network. Just official channels.{/i}"
        a "{i}Glass sees what Echelon allows Glass to see.{/i}"
        a "{i}Maybe that's safer. Maybe ignorance is mercy.{/i}"
        "{i}The terminal loads. Standard protocols. Clean data. Approved information.{/i}"

    # ==========================================
    # DISCOVERY 1: RESISTANCE CHATTER
    # ==========================================
    if has_device or em >= 1:
        "{i}Messages flood the screen. Resistance networks. Active. Urgent.{/i}"
        "{i}[ENCRYPTED] - Sector 10 survivors confirm: Echelon sweep yesterday.{/i}"
        "{i}[ENCRYPTED] - Glass unit showed mercy. Some escaped. Spread word.{/i}"
        "{i}[ENCRYPTED] - Evacuate Sectors 8, 9, 10 immediately. Something coming.{/i}"
        "{i}[ENCRYPTED] - Move families to safe zones. Time unknown. Days? Hours?{/i}"

        a "{i}They're alive. The ones I saved. They're warning others.{/i}"
        a "{i}200 people spreading word. Families evacuating.{/i}"
        a "{i}My mercy... it's helping. It's actually helping.{/i}"
        a "{i}Maybe breaking Glass was right. Maybe humanity isn't weakness.{/i}"

        if saved_shelter:
            "{i}[ENCRYPTED] - Shelter survivors organizing evacuation routes.{/i}"
            a "{i}The shelter. 150 people. They're organizing. Leading others out.{/i}"
            a "{i}I saved them. And now they're saving more.{/i}"

        if saved_vendor:
            "{i}[ENCRYPTED] - Contact 'Brew' establishing safe house in Sector 6.{/i}"
            a "{i}'Brew.' The vendor. He's alive. Setting up safe houses.{/i}"
            a "{i}I let him run. And he's helping others run too.{/i}"

        a "{i}This is what Zira meant. This is why trying matters.{/i}"
        a "{i}I can't save everyone. But the ones I save... they save others.{/i}"
        a "{i}Ripples. Small mercies creating bigger ones.{/i}"
    else:
        "{i}No chatter. No intercepts. Just official Echelon reports.{/i}"
        "{i}[OFFICIAL] - Sector 10 sweep complete. 800 eliminated. Zero survivors.{/i}"
        "{i}[OFFICIAL] - Sector secured. Mission success. No complications.{/i}"
        a "{i}That's what the report says. 800 eliminated. Zero survivors.{/i}"
        a "{i}But I know better. 200 are alive. Somewhere.{/i}"
        a "{i}The system doesn't know. Or doesn't care to know.{/i}"
        a "{i}Maybe that's good. Maybe their survival depends on invisibility.{/i}"

    # ==========================================
    # DISCOVERY 2: ENERGY GRID ANOMALIES
    # ==========================================
    "{i}Energy grid data loads. Sectors 8, 9, 10. Scheduled maintenance tonight.{/i}"
    "{i}[GRID ALERT] - Scheduled power reduction: Sectors 8-10.{/i}"
    "{i}[MAINTENANCE] - Infrastructure repairs following sweep operations.{/i}"
    "{i}[TIMELINE] - Execution window: 2000-2300 hours. Duration: 3 hours.{/i}"

    a "{i}Power reduction? Three-hour window? That's... extensive.{/i}"
    "{i}[TECHNICAL] - Grid sectors 8A through 10F: Complete shutdown.{/i}"
    "{i}[TECHNICAL] - Shield generators offline during maintenance.{/i}"
    "{i}[TECHNICAL] - Emergency protocols suspended: 2000-2300 hours.{/i}"
    a "{i}Shield generators offline? That's... unusual.{/i}"
    a "{i}Why would they shut down shields during maintenance?{/i}"
    a "{i}Safety protocol is to keep shields UP during repairs...{/i}"

    menu:
        "The energy data sits on screen. Something feels wrong. But what?":
            "Investigate further—check historical maintenance patterns.":
                $ record_choice_once(_current_scene_id, "investigated_energy")
                "{i}Historical maintenance logs. Comparing patterns.{/i}"
                "{i}Past maintenance: Shields stay active. Repairs done in sections. Never full shutdown.{/i}"
                "{i}Tonight: All shields offline. All sectors simultaneously. Complete shutdown.{/i}"

                a "{i}That's not standard. That's not... safe.{/i}"
                a "{i}Why would they expose three sectors completely?{/i}"
                a "{i}Unless...{/i}"
                a "{i}Unless they're not worried about protection. Because nothing's there to protect.{/i}"
                a "{i}But that doesn't make sense. Thousands of people live in those sectors.{/i}"
                a "{i}...Don't they?{/i}"
                a "{i}I'm missing something. But I can't see it.{/i}"

            "Dismiss it—too exhausted to think clearly.":
                $ record_choice_once(_current_scene_id, "dismissed_energy")
                a "{i}I'm too tired for this. Seeing problems where there aren't any.{/i}"
                a "{i}It's maintenance. Routine. Boring. Nothing to worry about.{/i}"
                a "{i}I need to stop looking for horror everywhere.{/i}"

    # ==========================================
    # DISCOVERY 3: MARCUS'S ORDERS
    # ==========================================
    "{i}Notification. Incoming transmission. High priority. Command level.{/i}"
    "{i}Source: High Marshal Marcus Rylan.{/i}"

    a "{i}Father. He only calls when he needs Glass.{/i}"
    a "{i}What now? Another mission? Another sector to erase?{/i}"

    m "Glass. Status report."
    a "Sector 10 sweep complete. Mission successful."
    m "Casualties?"

    if em >= 2:
        a "800 confirmed. Zero survivors."
        m "(pause) ...Excellent. Clean execution."
        a "{i}He believes it. The lie holds.{/i}"
    else:
        a "800 confirmed."
        m "Within parameters. Good."

    m "New directive. Stand by for deployment orders."
    a "(tense) Another sweep?"
    m "No. Observation duty. Upper Aeries. Tonight. 2000 hours."
    a "Observation? That's not—"
    m "(cuts him off) You've earned rest, Glass. Tonight, you watch. You don't act."
    m "Report to command deck. Observation only. Understood?"

    a "{i}Observation duty? Marcus never assigns me observation.{/i}"
    a "{i}He uses me to cut. Not to watch.{/i}"
    a "{i}What's happening tonight that he wants me to SEE but not DO?{/i}"

    a "...Understood. 2000 hours. Command deck."
    m "Good. Project Renewal executes tonight. You'll witness history."
    m "Solveil takes another step toward perfection."

    # If has device, try searching for 'Project Renewal'
    if has_device or em >= 1:
        "{i}Searches Zira's network: 'Project Renewal.'{/i}"
        "{i}No results. No mentions. Completely dark.{/i}"
        a "{i}Nothing. Either it's too classified or too new.{/i}"
        a "{i}Zira doesn't know. Resistance doesn't know.{/i}"
        a "{i}Only Marcus knows. And he wants me to watch.{/i}"

    # ==========================================
    # DISCOVERY 4: TROOP MOVEMENTS
    # ==========================================
    "{i}Deployment schedules. Troop movements. Routine checks.{/i}"
    "{i}[DEPLOYMENT] - All Echelon units: Evacuate Sectors 8-10 by 1900 hours.{/i}"
    "{i}[DEPLOYMENT] - Redeployment to Upper Aeries. Command deck observation stations.{/i}"
    "{i}[DEPLOYMENT] - Civilian personnel: Shelter-in-place orders. Sectors 8-10.{/i}"

    a "{i}Evacuate Echelon personnel. But civilians shelter-in-place?{/i}"
    a "{i}That's backwards. If something dangerous is happening, you evacuate civilians first.{/i}"
    a "{i}Unless...{/i}"
    a "{i}Unless you don't want civilians to leave.{/i}"
    a "{i}Unless you want them exactly where they are.{/i}"
    a "{i}Contained. Counted. Targeted.{/i}"

    a "{i}No. No, that's not—{/i}"
    a "{i}Father wouldn't—{/i}"
    a "{i}The system wouldn't—{/i}"
    a "{i}It's a drill. Security exercise. Testing evacuation protocols.{/i}"
    a "{i}That's why Echelon evacuates and civilians shelter. It's a test.{/i}"
    a "{i}It has to be a test.{/i}"

    # ==========================================
    # SYNTHESIS
    # ==========================================
    "{i}He stands. Paces. The room feels smaller.{/i}"

    a "{i}Resistance networks active. Survivors evacuating. That's good.{/i}"
    a "{i}Energy maintenance scheduled. Shields offline. That's... concerning.{/i}"
    a "{i}Project Renewal. Marcus wants me to witness. That's... what?{/i}"
    a "{i}Troop evacuations. Civilians locked down. That's...{/i}"
    a "{i}The pieces don't fit. Or they do and I'm not seeing it.{/i}"
    a "{i}Something's happening tonight. Something big.{/i}"
    a "{i}Zira warned me. 'Days not weeks.' She meant tonight.{/i}"

    a "{i}I can't think. I'm too exhausted. Too broken.{/i}"
    a "{i}Yesterday I killed 600 people. Shattered completely. Lyra held me together.{/i}"
    a "{i}I can't handle more horror. Not today. Not yet.{/i}"
    a "{i}It's a drill. Or a lockdown. Or infrastructure work.{/i}"
    a "{i}It's not—it can't be—{/i}"
    a "{i}Father wouldn't order mass extermination. The system has limits.{/i}"
    a "{i}...Doesn't it?{/i}"

    menu:
        "The data sits there. Pieces scattered. Picture incomplete. Dread building.":

            "Keep digging—try to find the full picture.":
                $ record_choice_once(_current_scene_id, "kept_investigating")
                "{i}He searches. Hours pass. Data upon data. Fragments. Pieces.{/i}"
                "{i}But the picture won't form. Too classified. Too compartmentalized.{/i}"
                a "{i}I can't find it. Whatever's happening, it's locked down tight.{/i}"
                a "{i}Only Marcus knows. And he's not telling Glass.{/i}"
                a "{i}He wants me to watch. To witness. To learn something.{/i}"
                a "{i}But what?{/i}"
                a "{i}I can't do this. I need air. I need to think.{/i}"

            "Stop investigating—too exhausted to continue.":
                $ record_choice_once(_current_scene_id, "stopped_investigating")
                a "{i}I can't. I'm too tired. Too broken.{/i}"
                a "{i}Whatever's happening... I'll find out at 2000 hours.{/i}"
                a "{i}Marcus wants me on command deck. I'll see it then.{/i}"
                a "{i}Right now I just need... air. Space. Distance from all of this.{/i}"

    # ==========================================
    # DECISION TO GO TO ROOFTOP
    # ==========================================
    "{i}Afternoon light slants through the window. Hours until 2000.{/i}"
    "{i}Time moves like sludge. Every minute heavy with dread.{/i}"

    a "{i}I can't stay here. Staring at data I don't understand.{/i}"
    a "{i}I need air. I need to think. I need to...{/i}"
    a "{i}...I need to be somewhere Kael used to be.{/i}"

    a "{i}The rooftop. Where you stood. Where you chose.{/i}"
    a "{i}Maybe being there will help me understand.{/i}"
    a "{i}Understand what's coming. Understand what I'm supposed to do.{/i}"
    a "{i}Understand if any of this matters.{/i}"

    "{i}He grabs his jacket. The device goes in his pocket.{/i}"
    "{i}One last look at the room. The terminal still glowing. Data still waiting.{/i}"

    a "{i}200 people alive because I broke Glass.{/i}"
    a "{i}Something big happening tonight because they warned others.{/i}"
    a "{i}My mercy rippling outward. But into what?{/i}"
    a "{i}Victory? Or catastrophe?{/i}"

    "{i}The corridor is empty. No officers. No servants. No witnesses.{/i}"
    "{i}Just Glass, walking toward answers he doesn't want.{/i}"

    a "{i}2000 hours. Command deck. 'Witness history,' Father said.{/i}"
    a "{i}But first... the rooftop. Where Kael made his choice.{/i}"
    a "{i}Maybe I need to make mine.{/i}"

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