# act1_20_investigation.rpy


# =======================================================
# ACT 1 - Scene 20: Investigation - Morning After
# =======================================================


label act1_investigation:

    # VISUAL: Aeron's apartment. Morning light harsh through window. Unmade bed.
    # LIGHTING: Cold morning white; sterile, clinical, unforgiving.
    # SOUND: City hum; ventilation; his breathing; terminal beeping softly.

    "{i}Morning. The light is too bright. The room too quiet.{/i}"
    "{i}He didn't sleep. Couldn't. Every time he closed his eyes—faces.{/i}"

    # VISUAL: Aeron sitting on edge of bed. Still in clothes from yesterday (changed from tactical gear).
    # Body language: Exhausted. Hollow. Broken but still breathing.

    a "{i}Yesterday I killed 600 people.{/i}"
    a "{i}Then I broke down completely. Shattered. Lyra held me together.{/i}"
    a "{i}Last night I met Zira. She gave me... something. Information. Access.{/i}"
    a "{i}I should feel different. Changed.{/i}"
    a "{i}...I just feel empty.{/i}"

    # VISUAL: On desk—Zira's encrypted device (if he has it). Small. Civilian tech. Blinking softly.
    # Beside it: Kael's photo. Mission reports. Coffee cup (cold, untouched).

    if zira_trusts_aeron or evidence_of_mercy >= 1:
        # HAS ZIRA'S DEVICE
        "{i}The device blinks. Soft red pulse. Waiting.{/i}"
        a "{i}Zira said use it when I'm ready. Ready for what?{/i}"
        a "{i}To see what's really happening. To choose.{/i}"
        
        # VISUAL: He picks up the device. Weighs it in his hand. Activates it.
        # SOUND: Soft chime; screen illuminates; encrypted interface loads.
        "{i}The interface loads. Clean. Simple. Civilian-grade encryption.{/i}"
        "{i}Data streams scroll—resistance network chatter, energy readings, movement logs.{/i}"
        
        a "{i}Let's see what Glass couldn't.{/i}"
        
    else:
        # NO DEVICE - Uses official Echelon channels only
        "{i}No device. No secret network. Just official channels.{/i}"
        a "{i}Glass sees what Echelon allows Glass to see.{/i}"
        a "{i}Maybe that's safer. Maybe ignorance is mercy.{/i}"
        
        # VISUAL: He activates standard terminal. Official Echelon interface.
        "{i}The terminal loads. Standard protocols. Clean data. Approved information.{/i}"

    # ==========================================
    # DISCOVERY 1: RESISTANCE CHATTER
    # ==========================================

    if zira_trusts_aeron or evidence_of_mercy >= 1:
        # CAN SEE RESISTANCE NETWORKS
        
        # VISUAL: Device shows intercepted messages—fragmented, encrypted, urgent.
        # TEXT ON SCREEN: Resistance chatter scrolling.
        
        "{i}Messages flood the screen. Resistance networks. Active. Urgent.{/i}"
        
        # SOUND: Soft ping with each message appearing.
        "{i}[ENCRYPTED] - Sector 10 survivors confirm: Echelon sweep yesterday.{/i}"
        "{i}[ENCRYPTED] - Glass unit showed mercy. Some escaped. Spread word.{/i}"
        "{i}[ENCRYPTED] - Evacuate Sectors 8, 9, 10 immediately. Something coming.{/i}"
        "{i}[ENCRYPTED] - Move families to safe zones. Time unknown. Days? Hours?{/i}"
        
        # VISUAL: Aeron reads. Expression shifts—surprise, then relief.
        a "{i}They're alive. The ones I saved. They're warning others.{/i}"
        a "{i}200 people spreading word. Families evacuating.{/i}"
        a "{i}My mercy... it's helping. It's actually helping.{/i}"
        
        # VISUAL: Small smile. First positive emotion in 24 hours. Brief hope.
        a "{i}Maybe breaking Glass was right. Maybe humanity isn't weakness.{/i}"
        
        if aeron_saved_shelter:
            "{i}[ENCRYPTED] - Shelter survivors organizing evacuation routes.{/i}"
            a "{i}The shelter. 150 people. They're organizing. Leading others out.{/i}"
            a "{i}I saved them. And now they're saving more.{/i}"
        
        if aeron_saved_vendor:
            "{i}[ENCRYPTED] - Contact 'Brew' establishing safe house in Sector 6.{/i}"
            a "{i}'Brew.' The vendor. He's alive. Setting up safe houses.{/i}"
            a "{i}I let him run. And he's helping others run too.{/i}"
        
        # VISUAL: Relief visible on his face. Shoulders relax slightly.
        a "{i}This is what Zira meant. This is why trying matters.{/i}"
        a "{i}I can't save everyone. But the ones I save... they save others.{/i}"
        a "{i}Ripples. Small mercies creating bigger ones.{/i}"
        
    else:
        # NO ACCESS TO RESISTANCE NETWORKS - Official data only
        
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

    # VISUAL: Screen shifts—energy grid data. Sectors 8, 9, 10. Scheduled maintenance.
    # SOUND: Data loading; graphs rendering; alerts pinging softly.

    "{i}Energy grid data loads. Sectors 8, 9, 10. Scheduled maintenance tonight.{/i}"

    # VISUAL: Power reduction schedules. Sector-wide. 8PM-11PM window.
    "{i}[GRID ALERT] - Scheduled power reduction: Sectors 8-10.{/i}"
    "{i}[MAINTENANCE] - Infrastructure repairs following sweep operations.{/i}"
    "{i}[TIMELINE] - Execution window: 2000-2300 hours. Duration: 3 hours.{/i}"

    # VISUAL: Aeron reads. Frowns slightly. Something feels off but can't identify it.
    a "{i}Power reduction? Three-hour window? That's... extensive.{/i}"
    a "{i}Standard maintenance after sweep operations. Infrastructure damage. Makes sense.{/i}"
    
    # VISUAL: He scrolls further. More details. Technical specifications.
    "{i}[TECHNICAL] - Grid sectors 8A through 10F: Complete shutdown.{/i}"
    "{i}[TECHNICAL] - Shield generators offline during maintenance.{/i}"
    "{i}[TECHNICAL] - Emergency protocols suspended: 2000-2300 hours.{/i}"

    a "{i}Shield generators offline? That's... unusual.{/i}"
    a "{i}Why would they shut down shields during maintenance?{/i}"
    a "{i}Safety protocol is to keep shields UP during repairs...{/i}"

    # VISUAL: Brief pause. Something nags at him. But exhaustion clouds thinking.
    a "{i}Probably just... efficiency. Save power. Focus on repairs.{/i}"
    a "{i}I'm overthinking. I'm exhausted. Brain's seeing patterns that aren't there.{/i}"

    # ACTION: Player choice—dig deeper or dismiss it.
    menu:
        "The energy data sits on screen. Something feels wrong. But what?"
        "Investigate further—check historical maintenance patterns.":
            $ aeron_investigated_energy = True
            
            # VISUAL: He pulls up historical data. Compares patterns.
            "{i}Historical maintenance logs. Comparing patterns.{/i}"
            
            # VISUAL: Data comparison shows anomaly.
            "{i}Past maintenance: Shields stay active. Repairs done in sections. Never full shutdown.{/i}"
            "{i}Tonight: All shields offline. All sectors simultaneously. Complete shutdown.{/i}"
            
            a "{i}That's not standard. That's not... safe.{/i}"
            a "{i}Why would they expose three sectors completely?{/i}"
            a "{i}Unless...{/i}"
            
            # VISUAL: Realization starting to form. But not complete.
            a "{i}Unless they're not worried about protection. Because nothing's there to protect.{/i}"
            a "{i}But that doesn't make sense. Thousands of people live in those sectors.{/i}"
            a "{i}...Don't they?{/i}"
            
            # VISUAL: Confusion. Dread building but no clear picture.
            a "{i}I'm missing something. But I can't see it.{/i}"
            
        "Dismiss it—too exhausted to think clearly.":
            $ aeron_investigated_energy = False
            
            a "{i}I'm too tired for this. Seeing problems where there aren't any.{/i}"
            a "{i}It's maintenance. Routine. Boring. Nothing to worry about.{/i}"
            a "{i}I need to stop looking for horror everywhere.{/i}"

    # ==========================================
    # DISCOVERY 3: MARCUS'S ORDERS
    # ==========================================

    # VISUAL: Notification ping. Incoming comms. Official Echelon channel.
    # SOUND: Alert chime. Marcus's command signature.

    "{i}Notification. Incoming transmission. High priority. Command level.{/i}"
    "{i}Source: High Marshal Marcus Rylan.{/i}"

    # VISUAL: Aeron tenses. Marcus never contacts directly unless it's orders.
    a "{i}Father. He only calls when he needs Glass.{/i}"
    a "{i}What now? Another mission? Another sector to erase?{/i}"

    # VISUAL: Opens transmission. Audio only. No video.
    # SOUND: Marcus's voice—calm, clinical, cold.

    m "Glass. Status report."
    a "Sector 10 sweep complete. Mission successful."
    m "Casualties?"
    
    if evidence_of_mercy >= 2:
        # Lied to Marcus about numbers
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

    # VISUAL: Aeron's confusion visible. This isn't normal.
    a "{i}Observation duty? Marcus never assigns me observation.{/i}"
    a "{i}He uses me to cut. Not to watch.{/i}"
    a "{i}What's happening tonight that he wants me to SEE but not DO?{/i}"

    a "...Understood. 2000 hours. Command deck."
    m "Good. Project Renewal executes tonight. You'll witness history."
    m "Solveil takes another step toward perfection."

    # SOUND: Transmission ends. Static. Silence.

    # VISUAL: Aeron sits. Processes. Dread building.
    a "{i}Project Renewal. What the hell is Project Renewal?{/i}"
    a "{i}And why does he want me to WITNESS it?{/i}"

    # If has device, can search
    if zira_trusts_aeron or evidence_of_mercy >= 1:
        # VISUAL: Checks device. Searches for "Project Renewal."
        "{i}Searches Zira's network: 'Project Renewal.'{/i}"
        "{i}No results. No mentions. Completely dark.{/i}"
        
        a "{i}Nothing. Either it's too classified or too new.{/i}"
        a "{i}Zira doesn't know. Resistance doesn't know.{/i}"
        a "{i}Only Marcus knows. And he wants me to watch.{/i}"

    # ==========================================
    # DISCOVERY 4: TROOP MOVEMENTS
    # ==========================================

    # VISUAL: Checks standard deployment logs (public to Echelon officers).
    "{i}Deployment schedules. Troop movements. Routine checks.{/i}"

    # VISUAL: Data shows mass evacuations. Echelon personnel leaving Lower Spans.
    "{i}[DEPLOYMENT] - All Echelon units: Evacuate Sectors 8-10 by 1900 hours.{/i}"
    "{i}[DEPLOYMENT] - Redeployment to Upper Aeries. Command deck observation stations.{/i}"
    "{i}[DEPLOYMENT] - Civilian personnel: Shelter-in-place orders. Sectors 8-10.{/i}"

    a "{i}Evacuate Echelon personnel. But civilians shelter-in-place?{/i}"
    a "{i}That's backwards. If something dangerous is happening, you evacuate civilians first.{/i}"
    a "{i}Unless...{/i}"

    # VISUAL: Realization forming. Horror dawning. But not complete picture yet.
    a "{i}Unless you don't want civilians to leave.{/i}"
    a "{i}Unless you want them exactly where they are.{/i}"
    a "{i}Contained. Counted. Targeted.{/i}"

    # VISUAL: His hands shake. Breath catches. Dread crushes.
    a "{i}No. No, that's not—{/i}"
    a "{i}Father wouldn't—{/i}"
    a "{i}The system wouldn't—{/i}"

    # VISUAL: Tries to rationalize. Denial kicking in.
    a "{i}It's a drill. Security exercise. Testing evacuation protocols.{/i}"
    a "{i}That's why Echelon evacuates and civilians shelter. It's a test.{/i}"
    a "{i}It has to be a test.{/i}"

    # ==========================================
    # SYNTHESIS: PIECES WITHOUT PICTURE
    # ==========================================

    # VISUAL: He stands. Paces. Can't sit still. Mind racing.
    "{i}He stands. Paces. The room feels smaller.{/i}"

    a "{i}Resistance networks active. Survivors evacuating. That's good.{/i}"
    a "{i}Energy maintenance scheduled. Shields offline. That's... concerning.{/i}"
    a "{i}Project Renewal. Marcus wants me to witness. That's... what?{/i}"
    a "{i}Troop evacuations. Civilians locked down. That's...{/i}"

    # VISUAL: He stops. Hands on desk. Breathing hard.
    a "{i}The pieces don't fit. Or they do and I'm not seeing it.{/i}"
    a "{i}Something's happening tonight. Something big.{/i}"
    a "{i}Zira warned me. 'Days not weeks.' She meant tonight.{/i}"

    # VISUAL: Looks at Kael's photo. Then at device (if he has it). Then at window.
    a "{i}I can't think. I'm too exhausted. Too broken.{/i}"
    a "{i}Yesterday I killed 600 people. Shattered completely. Lyra held me together.{/i}"
    a "{i}I can't handle more horror. Not today. Not yet.{/i}"

    # VISUAL: Denial protecting him. Mind refusing to see the full picture.
    a "{i}It's a drill. Or a lockdown. Or infrastructure work.{/i}"
    a "{i}It's not—it can't be—{/i}"
    a "{i}Father wouldn't order mass extermination. The system has limits.{/i}"
    a "{i}...Doesn't it?{/i}"

    # ACTION: Player choice—keep investigating or stop.
    menu:
        "The data sits there. Pieces scattered. Picture incomplete. Dread building."
        "Keep digging—try to find the full picture.":
            $ aeron_kept_investigating = True
            
            # VISUAL: He dives back into data. Searches frantically. Hours pass.
            "{i}He searches. Hours pass. Data upon data. Fragments. Pieces.{/i}"
            "{i}But the picture won't form. Too classified. Too compartmentalized.{/i}"
            
            a "{i}I can't find it. Whatever's happening, it's locked down tight.{/i}"
            a "{i}Only Marcus knows. And he's not telling Glass.{/i}"
            a "{i}He wants me to watch. To witness. To learn something.{/i}"
            a "{i}But what?{/i}"
            
            # VISUAL: Exhaustion overtakes. Can't think anymore.
            a "{i}I can't do this. I need air. I need to think.{/i}"
            
        "Stop investigating—too exhausted to continue.":
            $ aeron_kept_investigating = False
            
            a "{i}I can't. I'm too tired. Too broken.{/i}"
            a "{i}Whatever's happening... I'll find out at 2000 hours.{/i}"
            a "{i}Marcus wants me on command deck. I'll see it then.{/i}"
            a "{i}Right now I just need... air. Space. Distance from all of this.{/i}"

    # ==========================================
    # DECISION TO GO TO ROOFTOP
    # ==========================================

    # VISUAL: Window shows afternoon sun. Hours until evening. Time stretches.
    "{i}Afternoon light slants through the window. Hours until 2000.{/i}"
    "{i}Time moves like sludge. Every minute heavy with dread.{/i}"

    a "{i}I can't stay here. Staring at data I don't understand.{/i}"
    a "{i}I need air. I need to think. I need to...{/i}"
    a "{i}...I need to be somewhere Kael used to be.{/i}"

    # VISUAL: Looks at Kael's photo one more time.
    a "{i}The rooftop. Where you stood. Where you chose.{/i}"
    a "{i}Maybe being there will help me understand.{/i}"
    a "{i}Understand what's coming. Understand what I'm supposed to do.{/i}"
    a "{i}Understand if any of this matters.{/i}"

    # VISUAL: He grabs a jacket. Pockets the device (if he has it). Heads for door.
    "{i}He grabs his jacket. The device goes in his pocket.{/i}"
    "{i}One last look at the room. The terminal still glowing. Data still waiting.{/i}"

    a "{i}200 people alive because I broke Glass.{/i}"
    a "{i}Something big happening tonight because they warned others.{/i}"
    a "{i}My mercy rippling outward. But into what?{/i}"
    a "{i}Victory? Or catastrophe?{/i}"

    # VISUAL: Door opens. Corridor stretches ahead. Sterile. Empty.
    "{i}The corridor is empty. No officers. No servants. No witnesses.{/i}"
    "{i}Just Glass, walking toward answers he doesn't want.{/i}"

    a "{i}2000 hours. Command deck. 'Witness history,' Father said.{/i}"
    a "{i}But first... the rooftop. Where Kael made his choice.{/i}"
    a "{i}Maybe I need to make mine.{/i}"

    # TRANSITION: Fade to black. Footsteps echoing. Elevator ascending.
    # TEXT: "Evening. The rooftop."

    # canon_note: Aeron sees fragments but misses the full picture
    # canon_note: Resistance evacuation makes him feel HOPEFUL (ironic given what's coming)
    # canon_note: Energy anomalies noticed but rationalized away (exhaustion + denial)
    # canon_note: Marcus orders "observation duty" = wants Aeron to witness Purge
    # canon_note: "Project Renewal" = code name for Purge, Aeron doesn't know
    # canon_note: Troop evacuations + civilian lockdowns = setup for targeting
    # canon_note: Aeron in denial ("It's a drill. Father wouldn't.") = realistic trauma response
    # canon_note: Goes to rooftop to process, not knowing he'll witness Purge from there
    # canon_note: Player investigation choices affect how much he pieces together (not enough either way)

    return