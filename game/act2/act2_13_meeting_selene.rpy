# act2_13_meeting_selene.rpy


# =======================================================
# ACT 2 - Scene 13: Meeting Selene (+ Dynamic Crisis)
# =======================================================


label act2_meeting_selene:

    # Initialize scene tracking
    $ scenes["meeting_selene"] = {
        "crisis_type": None,
        "selene_trust": 0,
        "alliance_formed": False,
        "casualties": 0,
        "crisis_resolved": False
    }

    # VISUAL: Sector 6 ruins. Dawn. Broken buildings. Devastation everywhere.
    # LIGHTING: Gray dawn light. Cold. Harsh shadows.
    # SOUND: Wind through ruins. Rubble shifting. Footsteps approaching.

    scene bg_sector6_ruins_dawn with fade

    "{i}Sector 6 ruins. Dawn barely breaking. The Purge left this place shattered—collapsed buildings, torn streets, ghosts everywhere. Perfect neutral ground because nobody wants it anymore.{/i}"

    # VISUAL: Figures emerge from ruins. Armed. Cautious. Resistance fighters.
    # 4-5 people. Battle-worn. Survivors. Angry. Grieving. Dangerous.

    "{i}Movement. Figures emerging from cover. Armed. Four of them. Maybe five. Hard to tell in the shadows. All pointing weapons at us.{/i}"

    # VISUAL: Aeron and Lyra stop. Hands visible. Not reaching for weapons. Non-threatening.
    l "(quiet) Five visible. Probably more we can't see."
    a "Definitely more. Snipers on rooftops. Flankers in ruins. She's smart."
    l "Or paranoid."
    a "Down here, they're the same thing."

    # VISUAL: Resistance fighters part. Woman walks through. Mid-30s. Scarred. Exhausted. Determined.
    # SELENE: Leader. Survivor. Epitome of determination despite everything lost.

    "{i}They part. One woman walks forward. Mid-thirties, scarred face, eyes that have seen too much death. This is Selene. The woman whose people I killed. Whose sector I swept. Who lost everything twice—once to me, once to the Purge.{/i}"

    # VISUAL: Selene stops. Ten feet away. Evaluating. Cold. Professional.
    selene "Glass."
    a "Not anymore. Aeron. Aeron Rylan."
    selene "Names don't change what you did. Glass, Aeron, doesn't matter. You swept my sector. Killed 600 people in one night."
    a "I did. I'm not denying it. I'm not defending it. I did it."
    selene "At least you're honest. Most killers make excuses."

    # VISUAL: She looks at Lyra. Recognizing. Cold calculation.
    selene "And you. Echelon's perfect soldier. Proof the system works. I know your face. Seen it on propaganda screens."
    l "That's not who I am anymore."
    selene "No? Then who are you? Because right now you look like two Echelon defectors trying to hide in my territory."
    l "We're people who want to burn Echelon down. Same as you."
    selene "You don't get to want that. You WERE Echelon. You built the machine. Now you want to destroy it because it turned on you?"
    selene "That's not resistance. That's revenge."

    # VISUAL: Aeron doesn't flinch. Accepts the accusation. Truth in it.
    a "Maybe it started as revenge. But it's more now. Echelon murdered 100,000 people in the Purge. My mercy triggered it but Marcus ordered it."
    a "That's not a system worth serving. That's not a city worth protecting. That's genocide wearing order's mask."
    selene "And you suddenly care? After years of killing for them?"
    a "No. Not suddenly. Slowly. Piece by piece. Until I cracked completely and couldn't do it anymore."
    a "I'm not asking forgiveness. I'm asking for a chance to do something that matters. To stop them from doing it again."

    # VISUAL: Selene studies them. Long silence. Tension building. Decision pending.
    selene "Zira vouched for you. Said you completed every task she set. Worked honestly. Helped people. Confronted your past."
    selene "Is that true?"
    a "Yes. Every task. Every single one."
    selene "Why? Why do all that? Why not just run? Hide? Disappear into the Unders and hope nobody finds you?"
    a "Because hiding isn't surviving. And surviving isn't living. I want to do something that matters before I die."
    a "I want to count the living instead of the dead. I want to build instead of break. I want to be someone other than Glass."

    # VISUAL: Selene's expression shifts. Slight. Barely noticeable. But something softens.
    selene "Tessa's philosophy. 'Count the living.' She mentioned you. Said you might be worth saving."
    selene "Noelle said your instincts are solid. That you think like Echelon but fight like resistance."
    selene "Even the people you hurt vouched for you. Survivors from your Sweep. Said you saved 200 when you could have killed them all."
    selene "That's why I'm here. Not because I trust you. But because people I trust say you might be useful."

    # VISUAL: She steps closer. Eyes hard. Testing.
    selene "So here's the deal. I don't trust you. I don't like you. And if you fuck up even once, I'll kill you myself."
    selene "But I need soldiers. I need people who know Echelon. And I need people desperate enough to actually fight instead of just survive."
    selene "You fit all three. So I'm willing to give you one chance. One. You waste it, you die. Clear?"

    # VISUAL: Aeron nods. Accepting. Grateful despite harsh terms.
    a "Clear. One chance. We won't waste it."
    selene "We'll see. Words are easy. Actions are—"

    # VISUAL: Sudden interruption. Crisis trigger based on player choices.
    # System checks which crisis should trigger based on activity decisions.

    # ========== CRISIS ROUTING SYSTEM ==========
    
    # Check conditions in priority order
    $ crisis_triggered = None
    
    # Priority 1: Stolen Echelon weapons (highest stakes)
    $ if scenes.get("activity2_weapons", {}).get("method") == "stolen_echelon":
        $ crisis_triggered = "tracked_weapons"
        $ scenes["meeting_selene"]["crisis_type"] = "tracked_weapons"
        jump crisis_tracked_weapons
    
    # Priority 2: Owe Vex favor
    $ elif "vex" in inventory.get("debts_owed", []):
        $ crisis_triggered = "vex_favor"
        $ scenes["meeting_selene"]["crisis_type"] = "vex_favor"
        jump crisis_vex_favor
    
    # Priority 3: Smuggling job (Kelvin mole)
    $ elif scenes.get("activity1_work", {}).get("job_chosen") == "smuggling":
        $ crisis_triggered = "kelvin_mole"
        $ scenes["meeting_selene"]["crisis_type"] = "kelvin_mole"
        jump crisis_kelvin_mole
    
    # Priority 4: Promised help to Hector's father
    $ elif scenes.get("activity7_past", {}).get("offered_help"):
        $ crisis_triggered = "sector10_rescue"
        $ scenes["meeting_selene"]["crisis_type"] = "sector10_rescue"
        jump crisis_sector10_rescue
    
    # Priority 5: Vouched for Dren (debt)
    $ elif scenes.get("activity5_reputation", {}).get("intervened_debt"):
        $ crisis_triggered = "debt_collector"
        $ scenes["meeting_selene"]["crisis_type"] = "debt_collector"
        jump crisis_debt_collector
    
    # Priority 6: Worked for Kren
    $ elif characters.get("kren", {}).get("met") and scenes.get("activity1_work", {}).get("job_chosen") == "market_stall":
        $ crisis_triggered = "kren_warning"
        $ scenes["meeting_selene"]["crisis_type"] = "kren_warning"
        jump crisis_kren_warning
    
    # Default: Noelle's algorithm (always available since she's required)
    $ else:
        $ crisis_triggered = "noelle_algorithm"
        $ scenes["meeting_selene"]["crisis_type"] = "noelle_algorithm"
        jump crisis_noelle_algorithm


# =======================================================
# CRISIS 1: Tracked Weapons (Stolen from Echelon)
# =======================================================

label crisis_tracked_weapons:
    
    # VISUAL: Alarm. Sudden. Loud. Everyone tenses.
    # SOUND: Warning beep. Proximity alert. Weapons readied.
    
    "{i}Beeping. Loud. Proximity alarm. Someone's resistance fighter's device lighting up. Red. Urgent. Incoming.{/i}"
    
    resistance_fighter "Contact! Multiple signatures! Echelon patrol converging on this position!"
    
    # VISUAL: Selene whirls. Fury and confusion mixing.
    selene "How? This location was secure! How did they find us?"
    
    # VISUAL: Another fighter checking scanner. Realization. Horror.
    resistance_fighter2 "Tracking signal! Coming from... them!"
    
    # VISUAL: Points at Aeron and Lyra. Specifically at their weapons.
    resistance_fighter2 "Their weapons! Echelon gear! They're broadcasting!"
    
    # VISUAL: Selene's face hardens. Betrayal assumed. Weapons turn on Aeron/Lyra.
    selene "(cold) You led them here. Deliberately or stupidly, doesn't matter. My people are in danger because of you."
    
    # VISUAL: Aeron realizes. The stolen weapons. Tracked. Fuck.
    a "{i}The weapons. We stole them from Echelon patrol. Ambushed them, took their gear. Of course they were tracked. Of course. How did I not think of that?{/i}"
    
    a "We didn't know. The weapons—we stole them from Echelon. We didn't know they were tracked."
    selene "You didn't CHECK? You brought enemy gear to a resistance meeting and didn't check for trackers?"
    selene "That's not inexperience. That's negligence. And my people die because of it."
    
    l "We can fix this. Drop the weapons. Scatter. Lead them away—"
    selene "Too late. They're already here. We fight or we die."
    
    # SOUND: Gunfire. Sudden. Close. Echelon forces engaging.
    # VISUAL: Chaos. Echelon soldiers converging. 8-10 strong. Armed. Professional.
    
    "{i}Gunfire. Sudden. Loud. Echelon forces pouring into ruins from multiple angles. Eight of them. Ten. Professional. Coordinated. We led them right here.{/i}"
    
    # VISUAL: Resistance fighters taking cover. Returning fire. Outnumbered but fighting.
    selene "(shouting) Defensive positions! Cover fire! Get the wounded out!"
    
    # VISUAL: Echelon soldiers advancing. Using tactics Aeron knows intimately. Because he taught them.
    a "{i}Their tactics. I know them. Taught them. Trained with them. Pincer movement, suppressing fire, flanking maneuver. Textbook Echelon assault.{/i}"
    
    # ACTION: Player choice - how to respond?
    menu:
        "Chaos. Gunfire. People dying because we brought tracked weapons. How do we fix this?"
        
        "Fight alongside resistance - prove yourself through action":
            $ scenes["meeting_selene"]["fought_with_resistance"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            
            a "(to Selene) I fucked up. I'm sorry. But I can help fix it. I know their tactics. Let me fight with you."
            selene "You want to help? Don't get my people killed trying!"
            a "I won't. I promise. Just trust me for five minutes."
            
            # VISUAL: Aeron moves into position. Lyra follows. Both fighting.
            "{i}Move. Cover. Return fire. Muscle memory from years of Echelon training. But fighting against them now. Using their tactics against them. Poetic. Necessary. Desperate.{/i}"
            
            # VISUAL: Calling out enemy positions. Predicting movements. Helping resistance.
            a "(shouting) Two flanking left! They'll come through that archway in ten seconds!"
            
            # VISUAL: Resistance fighter pre-positions. Ambushes flankers. Two down.
            resistance_fighter "He's right! How did you—"
            a "I trained them! I know how they think! Northwest corner next! Sniper position!"
            
            # VISUAL: Another fighter adjusts. Takes out sniper before he can fire.
            selene "(grudging) Keep talking! What else?"
            
            # VISUAL: Aeron and Lyra fighting efficiently. Calling plays. Turning tide.
            l "They're regrouping! Standard retreat pattern! Three. Two. One."
            a "When they pull back, they'll drop smoke. Don't chase. It's a trap."
            
            # VISUAL: Echelon soldiers retreat. Drop smoke. Resistance holds position instead of pursuing.
            # VISUAL: Would-be ambush fails. Echelon forces withdraw. Battle won.
            
            "{i}Smoke clears. Echelon forces retreating. Defeated. We won. Somehow. Despite everything. Because we know them. Because we were them.{/i}"
            
            # VISUAL: Aftermath. Checking casualties. Two resistance fighters wounded. None dead.
            selene "(breathing hard) Status!"
            resistance_fighter "Two wounded. Minor. Everyone else intact. They're retreating."
            selene "Casualties on their side?"
            resistance_fighter "Four down. Three wounded. Rest fled. We won."
            
            # VISUAL: Selene looks at Aeron. Complicated expression. Anger mixed with grudging respect.
            selene "You led them here. Your mistake almost killed my people."
            selene "But you also saved them. Your knowledge of Echelon tactics kept casualties minimal."
            selene "So I don't know whether to thank you or shoot you."
            
            a "I deserve both. I'm sorry. I should have checked the weapons. That's on me."
            selene "Yes. It is. And you'll answer for it. But not today."
            selene "Today you fought with us. Against them. That counts for something."
            
            $ scenes["meeting_selene"]["casualties"] = 2
            $ reputation["resistance"] += 3
            
        "Lead Echelon away - sacrifice play to save resistance":
            $ scenes["meeting_selene"]["led_away"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            
            a "This is my fault. I brought them here. So I'll lead them away."
            selene "What?"
            a "They're tracking these weapons. So I take them and run. Draw them off. Give your people time to escape."
            selene "That's suicide. There's too many of them."
            a "Maybe. But it's better than your people dying because I was careless."
            
            l "Then I'm coming with you."
            a "Lyra—"
            l "Don't. We do this together. Always. You run, I run. You fight, I fight. You die, I die."
            a "...Together. Always together."
            
            # VISUAL: They grab tracked weapons. Start running. Drawing fire.
            "{i}Run. Tracked weapons in hand. Shouting. Drawing attention. Making ourselves targets. Echelon forces see us. Recognize us. Turn pursuit our direction.{/i}"
            
            a "(shouting back at Selene) Get your people out! We'll lead them away!"
            selene "You'll die!"
            a "Then we die! But your people live! That's what matters! Go!"
            
            # VISUAL: Aeron and Lyra running through ruins. Echelon forces pursuing. Gunfire. Close.
            "{i}Running. Ruins blur. Gunfire behind us. Close. Too close. They're faster than expected. More determined. Probably recognized Glass. High-value target. Worth pursuing.{/i}"
            
            l "They're gaining!"
            a "I know! Keep moving! Just need to buy time!"
            l "How much time?"
            a "Enough for Selene's people to escape! That's all that matters!"
            
            # VISUAL: Close call. Bullet grazes Aeron's shoulder. Pain but keeps running.
            "{i}Impact. Shoulder. Bullet grazed. Burns. Bleeding. Doesn't matter. Keep running. Keep moving. Keep them chasing us instead of Selene.{/i}"
            
            # VISUAL: Turn corner. Dead end. Trapped. Echelon forces closing in.
            l "Dead end!"
            a "Shit! Climb! That building! Move!"
            
            # VISUAL: Scrambling up broken building. Echelon forces entering dead-end behind them.
            # VISUAL: Reaching rooftop. Look down. Surrounded. No way out.
            
            "{i}Rooftop. Trapped. Echelon forces below. No way out. No way down. This is it. This is where we die. But Selene's people got away. That's enough. That has to be enough.{/i}"
            
            # VISUAL: Echelon commander steps forward. Recognizes them. Megaphone.
            echelon_commander "Glass! Surrender! Marcus wants you alive! Comply and you won't be harmed!"
            
            a "(to Lyra) What do you think? Believe him?"
            l "Not even a little."
            a "Me neither. So we fight?"
            l "We fight. Together."
            a "Together. Until the end."
            
            # VISUAL: Preparing for last stand. Then... gunfire. From behind Echelon forces.
            # SOUND: Surprise attack. Echelon forces turning. Confusion.
            
            "{i}Gunfire. From behind. Echelon forces caught by surprise. Turning. Confusion. Who—?{/i}"
            
            # VISUAL: Selene and resistance fighters flanking Echelon. Ambush reversed.
            selene "(shouting) Now! Hit them now!"
            
            # VISUAL: Fierce battle. Echelon forces caught between rooftop and resistance. Pincer. Destroyed.
            "{i}Caught between us. Resistance behind, us above. Crossfire. Echelon forces breaking. Retreating. Defeated. Selene came back. She came back for us.{/i}"
            
            # VISUAL: Battle ends. Echelon forces fled or dead. Silence. Aftermath.
            # VISUAL: Aeron and Lyra descend. Meet Selene. She's angry. But saved them.
            
            selene "You idiots. Running off to die nobly. What did you think that would accomplish?"
            a "Saving your people. They got away. That's all that mattered."
            selene "And you thought I'd just let you die? After that speech about wanting to fight Echelon?"
            selene "You don't get to die yet. You owe me. You led them here. Now you work off the debt by fighting with us."
            
            a "...Thank you. For coming back."
            selene "Don't thank me. You're still on probation. But you proved something today."
            selene "You were willing to die to save people you don't know. People who don't trust you. That's not revenge. That's resistance."
            
            $ scenes["meeting_selene"]["casualties"] = 1
            $ reputation["resistance"] += 5
            
        "Argue with Selene - defend yourself, deflect blame":
            $ scenes["meeting_selene"]["argued"] = True
            $ scenes["meeting_selene"]["selene_trust"] -= 2
            
            a "We didn't know! How were we supposed to know they tracked their own weapons?"
            selene "By checking! By being careful! By not bringing Echelon gear to a resistance meeting!"
            a "We needed weapons! We didn't have a choice!"
            selene "Everyone has a choice! You chose wrong and now my people pay for it!"
            
            # VISUAL: Firefight happening. People dying. Still arguing.
            l "This isn't helping! We need to—"
            a "I'm not taking blame for Echelon's tactics! They're the ones attacking!"
            selene "Because you LED THEM HERE!"
            
            # VISUAL: Resistance fighter goes down. Shot. Screams. Chaos.
            resistance_fighter "(screaming) Medic! I'm hit!"
            
            # VISUAL: Selene turns from argument. Priorities shifted. Furious.
            selene "Get out. NOW. Before more of my people die because of you."
            a "We can help—"
            selene "You've DONE enough! Leave! If I see you again I'll shoot you myself!"
            
            # VISUAL: Forced to flee. Selene and resistance fighting without them. Casualties mounting.
            "{i}Fleeing. Leaving them to fight. Leaving them to die. Because I argued instead of helped. Because Glass's instincts took over. Defend. Deflect. Never admit. And people died.{/i}"
            
            # VISUAL: Escape ruins. Sounds of battle behind. Guilt crushing.
            l "(bitter) That went well."
            a "Don't."
            l "We could have helped. Instead you argued. Defended yourself. Like Glass would have."
            a "I know. I fucked up. Again."
            l "When are you going to learn? Words don't matter. Actions do. And your actions just burned the only alliance we had."
            
            $ scenes["meeting_selene"]["casualties"] = 5
            $ reputation["resistance"] -= 10
            $ scenes["meeting_selene"]["alliance_formed"] = False
            
            # This path fails the meeting - will need alternate route to join resistance later
            jump crisis_resolution_failure

    # RESOLUTION: Aftermath of battle (if fought or led away)
    jump crisis_resolution_success


# =======================================================
# CRISIS 2: Vex's Favor
# =======================================================

label crisis_vex_favor:
    
    # VISUAL: Before Selene can continue, encrypted device beeps. Aeron's.
    # SOUND: Urgent. Persistent. Can't ignore.
    
    "{i}Device. Beeping. Mine. Urgent message. Can't ignore it. Not now. Vex.{/i}"
    
    # VISUAL: Selene notices. Annoyed at interruption.
    selene "You're answering messages during our meeting?"
    a "I'm sorry. This might be important. Give me one second."
    
    # VISUAL: Checks message. Face hardens. Fuck.
    # MESSAGE: "Calling in favor. Now. Workshop being raided. Need extraction. You owe me. - Vex"
    
    a "{i}Vex. The favor I owe. Being called in right now. During the meeting. Perfect fucking timing.{/i}"
    
    selene "Problem?"
    a "...Yes. The weapons dealer I got our gear from. I owe them a favor. They're calling it in now. Echelon's raiding their workshop."
    selene "And you're telling me this because?"
    a "Because I gave my word. They helped us when we had nothing. Now they need help and I owe them."
    
    # VISUAL: Selene's expression hardens. Testing.
    selene "So you owe a weapons dealer. And right now, during our meeting, you want to go help them."
    a "I don't want to. But I gave my word. That has to mean something."
    selene "It means you're easily distracted. It means when things matter, you'll run off chasing personal debts instead of focusing on the mission."
    
    l "That's not fair. He made a promise. He's honoring it. That shows integrity."
    selene "Or it shows poor judgment. Owing favors to dealers. Making promises you can't keep. That's how you get killed down here."
    
    # VISUAL: Tense moment. Decision point. Crisis interrupting alliance negotiation.
    
    # ACTION: Player choice - Honor debt or stay?
    menu:
        "Vex needs help now. Selene needs answer now. Can't do both."
        
        "Help Vex - honor the debt you owe":
            $ scenes["meeting_selene"]["helped_vex"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            
            a "I'm sorry. I have to do this. I gave my word and Vex helped us when nobody else would."
            a "If that costs me this alliance, so be it. But I'm not breaking my word."
            
            selene "You're choosing a dealer over the resistance?"
            a "I'm choosing integrity over convenience. I keep my promises. All of them. Even when they cost me."
            
            # VISUAL: Selene studies him. Long moment. Calculating.
            selene "...Fine. Go. Help your dealer. But if you're serious about joining us, you come back. You prove this isn't just talk."
            selene "And bring the dealer. If they're under Echelon pressure, they might be useful to us too."
            
            a "You're giving us another chance?"
            selene "I'm giving you a test. Pass it and we'll talk. Fail it and don't come back. Go. Clock's running."
            
            # VISUAL: Aeron and Lyra run. Racing to Vex's workshop. Time pressure.
            # TRANSITION: Journey through Lower Spans. Running. Urgent.
            
            scene bg_sector7_market with fade
            
            "{i}Running. Sector 7. Vex's workshop ahead. Smoke rising. Gunfire. Echelon raid in progress. We're not too late. Not yet.{/i}"
            
            # VISUAL: Vex's workshop. Echelon soldiers ransacking. Vex pinned down. Wounded.
            "{i}There. Workshop. Echelon forces. Six of them. Tearing the place apart. Vex behind cover. Wounded. Bleeding. Trapped.{/i}"
            
            a "(whisper) Six soldiers. Vex is hurt. We need to hit fast and hard."
            l "Agreed. I'll take left flank. You take right. Signal when ready."
            a "Ready. Three. Two. One. Now."
            
            # VISUAL: Coordinated assault. Surprise attack. Taking down Echelon soldiers.
            "{i}Move. Fire. Cover. Two soldiers down before they know we're there. Four remaining. Reacting. Professional. Dangerous. But we're faster.{/i}"
            
            # VISUAL: Fierce fight. Close quarters. Aeron and Lyra efficient. Lethal.
            # VISUAL: Last soldier falls. Workshop secure. Vex still alive. Barely.
            
            vex "(pained) Took your time."
            a "You're welcome. Can you move?"
            vex "Not fast. They got me good. Twice. Shoulder and leg."
            l "We need to evacuate. More will come."
            
            # VISUAL: Grabbing Vex. Helping them up. Extracting from workshop.
            a "What happened? Why the raid?"
            vex "Someone tipped them off. Told them I was selling to resistance. Decided to make an example."
            vex "Would've worked too if you hadn't shown. Guess that favor paid off."
            a "You helped us. We help you. That's how it works."
            
            # VISUAL: Escape workshop. Carrying Vex. Workshop explodes behind them. Echelon scorched earth.
            "{i}Workshop exploding. Echelon destroying evidence. Everything Vex built. Gone. But Vex is alive. That's what matters.{/i}"
            
            # VISUAL: Back to Sector 6. Return to Selene. Vex with them.
            scene bg_sector6_ruins with fade
            
            # VISUAL: Selene waiting. Resistance fighters tense. Evaluating.
            selene "You came back. Brought company."
            a "Vex. The dealer I mentioned. Echelon destroyed their workshop. They need a place to go."
            selene "(to Vex) You sell weapons?"
            vex "(pained) Sold. Past tense. Don't have inventory anymore. Just what I'm carrying."
            selene "But you know suppliers. You know black market routes. You know who's selling what and where."
            vex "...Maybe."
            selene "Then you're useful. You can stay. Earn your keep by helping us arm properly."
            vex "Guess I don't have much choice."
            selene "(to Aeron) You kept your word. Honored your debt. Brought back someone useful. That's good judgment."
            selene "Welcome to the resistance. Probation starts now. Don't fuck it up."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 3
            $ characters["vex"]["trust"] += 2
            $ characters["vex"]["resistance_member"] = True
            $ inventory["debts_owed"].remove("vex")  # Debt paid
            
        "Stay with Selene - alliance takes priority":
            $ scenes["meeting_selene"]["abandoned_vex"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            
            a "I... no. I can't. This meeting is too important. Vex will have to handle it themselves."
            
            # VISUAL: Types quick response. Message sent. Device put away.
            # MESSAGE: "Can't help. In middle of something critical. Good luck. - A"
            
            selene "Smart choice. Personal debts don't matter when the mission does."
            l "(quiet) Aeron, you gave your word..."
            a "I know. But the resistance needs this alliance more than Vex needs one person. It's the right call."
            
            # VISUAL: Selene approves. Nods. Professional.
            selene "Good. You understand priorities. You understand sacrifice. That's what resistance means."
            selene "Vex might die. That's the cost. But you made the hard choice. That shows leadership."
            
            # VISUAL: Later, after meeting ends. Message notification.
            # MESSAGE: "You abandoned me. Don't expect future business. If I survive this, we're done. - Vex"
            
            "{i}Vex survived. Barely. Lost everything. And now hates me. I broke my word. Chose the mission over the debt. Was it right? I don't know. But it's done.{/i}"
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 4
            $ characters["vex"]["trust"] = -5
            $ characters["vex"]["burned_bridge"] = True
            $ inventory["debts_owed"].remove("vex")  # Debt voided through abandonment

    # RESOLUTION: Continue with alliance discussion
    jump crisis_resolution_success


# =======================================================
# CRISIS 3: Kelvin the Mole
# =======================================================

label crisis_kelvin_mole:
    
    # VISUAL: Before negotiation can deepen, figure approaches from ruins. Familiar. Smuggler.
    # SOUND: Footsteps. Confident. Approaching.
    
    "{i}Movement. Someone approaching. Confident. Not combat. Casual. Familiar. Wait. I know that walk.{/i}"
    
    # VISUAL: KELVIN emerges. Smuggler from Activity 1. Smiling. Wrong smile.
    kelvin "Well well. Glass and the perfect soldier. Never thought I'd see you here."
    
    # VISUAL: Aeron tenses. Something wrong. Kelvin shouldn't know this location.
    a "Kelvin. What are you doing here?"
    kelvin "Same thing as you. Meeting Selene. Delivering information."
    
    # VISUAL: Selene confused. Alert. Doesn't know Kelvin.
    selene "Who is this?"
    a "Smuggler. Gave us work a week ago. Shouldn't know about this meeting."
    selene "Then how—"
    kelvin "(laughs) Because I set it up. Well, me and my Echelon handlers. Nice little trap. You all walked right in."
    
    # VISUAL: Realization. Horror. Betrayal. Kelvin's a mole.
    "{i}Mole. Kelvin works for Echelon. The smuggling job. The package. It was all surveillance. He's been watching us. Reporting. And now he's here. Which means...{/i}"
    
    # VISUAL: Resistance fighters raising weapons. Kelvin unconcerned. Too confident.
    kelvin "I'd save the ammunition. You're surrounded. Echelon strike team. Twenty strong. Positioned around this entire block."
    kelvin "I've been feeding them intel for months. Every resistance movement. Every supply cache. Every meeting."
    kelvin "You think Selene's cell is the last one? It's not. It's just the last one I haven't turned over yet. And now I have."
    
    # VISUAL: Selene's face. Rage. Betrayal. But also calculation.
    selene "You've been the leak. All this time. The raids. The arrests. The executed cells. That was you."
    kelvin "That was business. Echelon pays well. Better than resistance does. Better than anyone."
    kelvin "(to Aeron) And you helped. That delivery you made? Tracker inside. Led us right to three resistance supply caches. We hit them the next day."
    
    # VISUAL: Aeron's guilt. Complicit without knowing. Used.
    a "{i}The package. I delivered it. Helped them. Didn't even know. Kelvin used me to hurt the resistance. And now he's using me again.{/i}"
    
    # VISUAL: Kelvin pulls out comm device. Finger on button. Trigger.
    kelvin "So here's how this ends. You all surrender. Come quietly. Or I press this and twenty Echelon soldiers turn this place into a killing field."
    kelvin "Your choice. But choose fast. My finger's getting tired."
    
    # ACTION: Player choice - how to handle Kelvin?
    menu:
        "Kelvin's a mole. Finger on trigger. Twenty Echelon soldiers waiting. What do we do?"
        
        "Rush Kelvin - prevent him from signaling":
            $ scenes["meeting_selene"]["rushed_kelvin"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            
            a "{i}No time to think. Only act. Stop the signal. Stop him. Move.{/i}"
            
            # VISUAL: Aeron lunges. Fast. Desperate. Kelvin starts pressing button.
            "{i}Lunge. Kelvin's hand moving. Button pressing. Too slow. Too late. Signal going—{/i}"
            
            # VISUAL: Lyra's shot. Perfect timing. Kelvin's hand. Device explodes. Kelvin screams.
            # SOUND: Gunshot. Device shattering. Kelvin collapsing.
            
            "{i}Gunshot. Lyra. Perfect shot. Device destroyed. Kelvin's hand mangled. Signal not sent. Not yet. Bought seconds. Maybe minutes. That's all we need.{/i}"
            
            selene "Move! Evacuation plan Delta! Now! Before they realize the signal didn't go through!"
            
            # VISUAL: Resistance fighters scrambling. Practiced evacuation. Efficient. Fast.
            "{i}Evacuation. Practiced. They've done this before. Lost cells before. Know how to run. Know how to survive. Moving fast.{/i}"
            
            # VISUAL: Aeron holding Kelvin. Bleeding. Terrified. Mole exposed.
            a "How many? How many cells did you betray?"
            kelvin "(crying) Six. Maybe seven. I don't remember. They all blur together."
            a "Names. Give me names. Who died because of you?"
            kelvin "Everyone. Everyone died. That's what happens when you resist Echelon. They always win. Always."
            
            # VISUAL: Selene returns. Cold. Executioner's face.
            selene "We need to move. They'll realize he didn't signal soon."
            a "What about him?"
            selene "Leave him. Let Echelon find him. Let them know we know. Send a message."
            kelvin "(panicked) You can't leave me here! They'll kill me for failing!"
            selene "Good. You earned it. Betraying your people for credits. You deserve whatever they do to you."
            
            # VISUAL: They leave. Kelvin screaming. Begging. Ignored.
            # VISUAL: Evacuating through tunnels. Underground routes. Escaping before Echelon realizes.
            
            "{i}Underground tunnels. Escape routes. Resistance knows them. Echelon doesn't. Old smuggling paths. Abandoned subway. Moving fast. No pursuit. Kelvin's signal never sent. We got lucky. Barely. But lucky.{/i}"
            
            # VISUAL: Safe location. Hours later. Resistance cell intact. Selene evaluating Aeron.
            selene "You acted fast. Stopped the signal. Saved everyone. That's good instinct."
            selene "But you also worked for him. Delivered his package. Helped him hurt us. How do I know you're not another mole?"
            a "Because I didn't know. And when I found out, I stopped him. Actions matter more than words. You said that. My actions say I'm with you."
            
            selene "...Fair. You're in. Probation. But you're in. Don't make me regret it."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 3
            $ characters["smuggler_kelvin"]["exposed"] = True
            $ characters["smuggler_kelvin"]["trust"] = -10
            
        "Negotiate - try to talk Kelvin down":
            $ scenes["meeting_selene"]["negotiated_kelvin"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 0
            
            a "Wait. Kelvin. Don't do this. You don't have to do this."
            kelvin "Don't I? Echelon pays me. Resistance can't. Simple economics."
            a "This isn't about money. You're sentencing people to death. Execution. Torture. That's not business. That's murder."
            kelvin "They chose to resist. They knew the risks. I'm just playing the odds."
            
            # VISUAL: Trying to reach him. Failing. Kelvin's finger still on button.
            l "(whisper) This isn't working. He's committed."
            a "Just... just think about it. You do this, you're not just an informant. You're a mass murderer. Is that who you want to be?"
            kelvin "I want to be rich and alive. Everything else is negotiable."
            kelvin "Last chance. Surrender or I signal."
            
            # VISUAL: Selene makes decision. Sniper shot. From hidden fighter. Kelvin's head. Dead.
            # SOUND: Single shot. Clean. Professional. Kelvin drops.
            
            "{i}Gunshot. Kelvin drops. Dead before he hits ground. Selene's sniper. Hidden. Waiting. She never trusted negotiation.{/i}"
            
            selene "Talking doesn't work on traitors. Only bullets. Remember that."
            a "You could have told me you had a sniper ready."
            selene "Could have. Didn't. Wanted to see if you'd waste time trying to save a traitor. You did. That's a weakness."
            selene "But you tried. That shows you're not like him. So you get one pass. Don't waste it."
            
            # VISUAL: Kelvin dead. Device secure. Signal not sent. Crisis resolved through violence.
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 1
            $ characters["smuggler_kelvin"]["dead"] = True
            
        "Kill Kelvin yourself - prove you're not like him":
            $ scenes["meeting_selene"]["killed_kelvin"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            
            a "{i}Talking won't work. Negotiation won't work. He's committed. He's dead. He just doesn't know it yet.{/i}"
            
            # VISUAL: Aeron draws weapon. Fast. Smooth. Professional. Glass moves.
            "{i}Draw. Aim. Fire. Muscle memory. Glass training. Kill the threat. Fast. Clean. Efficient.{/i}"
            
            # SOUND: Gunshot. Single. Precise. Kelvin's head. Dead instantly.
            # VISUAL: Kelvin drops. Device clatters. Signal not sent. Crisis ended.
            
            "{i}Dead before he hits ground. Device secured. Signal not sent. Threat neutralized. Glass would be proud. I feel sick.{/i}"
            
            # VISUAL: Silence. Everyone staring. Aeron just executed someone. Cold. Professional. Terrifying.
            selene "...Efficient."
            a "He was a threat. I ended him. That's what you do with threats."
            selene "That was Glass. Not Aeron. You slipped back into old habits."
            a "Does it matter? He's dead. Your people are safe. Isn't that what you wanted?"
            
            # VISUAL: Selene approaches. Studies him. Complicated expression.
            selene "It's what I needed. But watching you move like that... you're dangerous. More dangerous than I thought."
            selene "That's good. We need dangerous. But it's also terrifying. Because dangerous people who slip back into Glass might turn on us too."
            
            a "I won't. I killed him because he was Echelon's weapon. I'm yours. There's a difference."
            selene "Is there? Or are you just changing masters?"
            a "...I don't know. But I know I'm here. Fighting with you. Not against you. That has to mean something."
            
            selene "It means you're in. Probation. But in. Just remember—if you ever turn that Glass coldness on my people, I'll kill you myself."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 4
            $ characters["smuggler_kelvin"]["dead"] = True
            $ scenes["meeting_selene"]["showed_glass"] = True  # Future consequences

    # RESOLUTION: Continue with alliance
    jump crisis_resolution_success


# =======================================================
# CRISIS 4: Sector 10 Rescue
# =======================================================

label crisis_sector10_rescue:
    
    # VISUAL: Before Selene can respond, runner appears. Young. Panicked. Messenger.
    # SOUND: Running footsteps. Desperate. Urgent.
    
    "{i}Footsteps. Running. Fast. Someone panicked. Young voice. Messenger. Bad news incoming.{/i}"
    
    # VISUAL: Young resistance fighter. Teenager. Breathless. Terrified.
    messenger "(gasping) Selene! Sector 10! Echelon raid! They're killing everyone!"
    
    # VISUAL: Selene tenses. Sector 10. Again. Always Sector 10.
    selene "Sector 10? There's nothing left there. Just ruins and survivors."
    messenger "That's what they're raiding! The survivors! The ones hiding in the ruins! Thirty people! They're executing them!"
    
    # VISUAL: Aeron's face. Horror. The survivors. Hector's father. The people he promised to help.
    a "{i}The survivors. Thirty of them. I promised to help. Promised supplies. Promised support. And now Echelon's killing them. Because of me. Because I went there. Because I drew attention.{/i}"
    
    messenger "(to Aeron) One of them sent message! Said you promised to help! Said you owed them!"
    
    # VISUAL: Selene looks at Aeron. Cold calculation. Testing.
    selene "You made promises to Sector 10 survivors? When?"
    a "Last week. Confronting my past. I met Hector's father. His son... I killed him during the Sweep. I offered to help the survivors. Bring supplies. Support. Whatever they needed."
    selene "And you didn't tell me?"
    a "I didn't think it was relevant. It was personal. Between me and them."
    selene "Everything's relevant. Personal debts become tactical liabilities. Case in point—right now."
    
    # VISUAL: Selene calculating. Cold. Professional. Numbers vs emotions.
    selene "Thirty survivors. Sector 10. Deep in ruins. Echelon forces unknown number. Probably significant since they're making an example."
    selene "We're outnumbered. Outgunned. Going in there is suicide."
    
    a "We have to try. I promised them. I gave my word."
    selene "Your word doesn't mean anything if you're dead. And my people aren't dying for your guilt."
    
    # ACTION: Player choice - what to do?
    menu:
        "Thirty survivors being executed. Aeron's promise. Selene's calculation. What happens?"
        
        "Go alone - honor promise without risking Selene's people":
            $ scenes["meeting_selene"]["went_alone"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            
            a "Then I go alone. I made the promise. I'll keep it. Your people don't have to risk anything."
            selene "That's still suicide."
            a "Maybe. But it's my suicide. My promise. My responsibility."
            
            l "Then I'm coming too."
            a "Lyra—"
            l "Together. Always together. You don't get to die nobly alone. If you go, I go."
            
            # VISUAL: Selene watches. Evaluating. Something shifting in her expression.
            selene "...You're serious. You're actually going to throw yourselves at Echelon forces to save thirty people you don't know. People who probably hate you."
            a "Yes. Because I promised. Because they're people. Because counting the living matters more than surviving."
            
            # VISUAL: Selene silent. Long moment. Decision. Unexpected.
            selene "Fine. I'm coming too."
            a "What?"
            selene "You heard me. I'm coming. And bringing five of my people."
            selene "Not because I care about your promise. But because anyone stupid enough to die for strangers might actually be worth following."
            selene "And because Sector 10 was my territory. Those survivors? They're my people too. I don't abandon my people."
            
            # VISUAL: Rapid mobilization. Seven fighters total. Heading to Sector 10.
            # TRANSITION: Journey. Fast. Urgent. Armed. Determined.
            
            scene bg_sector10_ruins with fade
            
            "{i}Sector 10. Ruins. Again. Always back to where it started. Where I killed 600. Where I saved 200. Where it all broke. And now where I try to save 30 more.{/i}"
            
            # VISUAL: Echelon forces visible. Twelve soldiers. Survivors lined up. Execution formation.
            "{i}Twelve Echelon soldiers. Thirty survivors lined up. Execution formation. Minutes from death. No time for planning. Only action.{/i}"
            
            selene "(whisper) Twelve soldiers. Seven of us. Bad odds."
            a "Bad odds are all we have. Plan?"
            selene "Hit fast. Hit hard. Save who we can. Escape before reinforcements."
            a "Not much of a plan."
            selene "Best I've got. You have better?"
            a "...No. Let's do it."
            
            # VISUAL: Coordinated attack. Seven resistance vs twelve Echelon. Desperate. Fierce.
            "{i}Attack. Seven of us. Twelve of them. Surprise advantage. Three down before they react. Nine left. Odds improving. Still terrible. But improving.{/i}"
            
            # VISUAL: Firefight. Cover to cover. Survivors scattering. Some hit. Some escape. Chaos.
            "{i}Chaos. Gunfire. Survivors running. Some getting hit. Can't save them all. Never could. Never can. But saving some. That's enough. That has to be enough.{/i}"
            
            # VISUAL: Hector's father. Sees Aeron. Recognition. Complicated.
            hector_father "You came. You actually came."
            a "I promised. Get your people out! We'll cover!"
            hector_father "Thank you. For keeping your word."
            
            # VISUAL: Final push. Echelon forces breaking. Retreating. Victory. Costly but real.
            "{i}Last Echelon soldier falls. Survivors escaping. Twenty-two made it. Eight died. Not enough. Never enough. But twenty-two more than zero. Count the living.{/i}"
            
            # VISUAL: Aftermath. Exhausted. Wounded. But alive. Selene looking at Aeron differently.
            selene "Twenty-two saved. Eight lost. Could have been worse."
            a "Could have been better."
            selene "Could have been zero if you hadn't kept your word. You proved something today."
            selene "You're not just talk. You're not just guilt. You actually do what you say you will. That's rare."
            selene "Welcome to the resistance. You've earned it."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 8
            $ reputation["resistance"] += 5
            $ characters["hector_father"]["trust"] += 3
            $ stats["people_saved"] += 22
            
        "Convince Selene - argue for rescue mission":
            $ scenes["meeting_selene"]["convinced_selene"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            
            a "We have to go. Not just for my promise. For what it represents."
            selene "Which is?"
            a "That resistance means something. That we're not just surviving. That we protect people. Even when it's hard. Especially when it's hard."
            a "You said your cell was hit in the Purge. That you lost most of your people. Those thirty survivors? They're Sector 10. Your territory. Your people."
            a "If you abandon them now, what's the point? What are you resisting for if not to protect people like them?"
            
            # VISUAL: Selene silent. Aeron's words hitting. Truth in them.
            selene "...Dammit. You're right. I hate that you're right."
            selene "Fine. We go. But we do it smart. Not a suicide charge. Tactical. Planned. Minimal casualties."
            a "Agreed. What's the plan?"
            
            # VISUAL: Selene and Aeron planning. Resistance fighters preparing. Moving out.
            selene "We split up. Two teams. One draws Echelon attention. One extracts survivors."
            selene "You and Lyra—distraction team. You know Echelon tactics. Make noise. Keep them busy."
            selene "Me and my people—extraction. We get survivors out while you keep Echelon occupied."
            a "That puts us in more danger."
            selene "Yes. But you volunteered. And you're Glass. If anyone can survive being bait, it's you."
            
            # TRANSITION: Sector 10. Execution in progress. Plan executing.
            scene bg_sector10_ruins with fade
            
            # VISUAL: Aeron and Lyra attacking from opposite side. Drawing fire. Loud. Aggressive.
            "{i}Attack. Loud. Aggressive. Making ourselves targets. Echelon forces turning. Taking bait. Selene's team moving on survivors. Plan working. So far.{/i}"
            
            # VISUAL: Intense firefight. Aeron and Lyra pinned. Holding position. Buying time.
            "{i}Pinned. Buying time. Echelon forces focusing on us. Good. Means they're not watching survivors. Means Selene's extraction succeeds. That's all that matters.{/i}"
            
            # VISUAL: Selene's team evacuating survivors. Twenty-five rescued. Five dead before rescue arrived.
            "{i}Evacuation successful. Twenty-five survivors out. Five died before we arrived. Could have been thirty. Could have been zero. Twenty-five is something.{/i}"
            
            # VISUAL: Selene signals. Extraction complete. Time to disengage.
            selene "(comms) Extraction complete! Twenty-five out! Disengage!"
            a "(comms) Copy! Moving! Cover us!"
            
            # VISUAL: Retreat. Under fire. Selene's team providing cover. Escaping together.
            "{i}Retreat. Fire. Cover. Working together. Resistance and defectors moving as one unit. This is what it looks like. This is what it means.{/i}"
            
            # VISUAL: Safe distance. Regrouping. Twenty-five survivors. Selene's cell. Aeron and Lyra.
            selene "Twenty-five saved. Better than I expected. You held position well. Bought enough time."
            a "We did it together. That's how this works."
            selene "Yeah. Together. Maybe you're right. Maybe you do belong with us."
            selene "Welcome to the resistance. Try not to get my people killed with your next promise."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 5
            $ reputation["resistance"] += 3
            $ characters["hector_father"]["trust"] += 2
            $ stats["people_saved"] += 25
            
        "Refuse - alliance more important than promise":
            $ scenes["meeting_selene"]["refused_rescue"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            
            a "...No. You're right. It's suicide. I can't ask your people to die for my promise."
            selene "So you're breaking your word?"
            a "I'm prioritizing. The alliance matters more than thirty people. As cold as that sounds."
            a "Resistance needs soldiers. Needs structure. Needs leadership. Thirty people vs rebuilding resistance? The math is clear."
            
            # VISUAL: Selene evaluates. Complicated expression. Approves but doesn't like it.
            selene "That's cold. Practical. But cold."
            selene "You're right. Tactically. Strategically. Thirty people aren't worth risking the alliance."
            selene "But it also means you break your word when it's convenient. That's concerning."
            
            l "(quiet) Aeron, you promised them..."
            a "I know. And I'm breaking that promise. Because the mission matters more."
            a "That's what you said, Selene. Mission first. Personal second. I'm learning."
            
            # VISUAL: Selene nods. Professional. But colder than before.
            selene "You are learning. The hard lessons. The ones that keep you alive but cost your soul."
            selene "Welcome to resistance leadership. You're in. But remember—every promise you break, every person you abandon, that's a piece of yourself you lose."
            selene "Don't lose too much. Or you'll become Glass again. Just with different masters."
            
            # VISUAL: Later. Message arrives. Sector 10 massacre complete. Thirty dead.
            # MESSAGE: "We waited for you. You never came. We died waiting. - H.F."
            
            "{i}Thirty dead. Hector's father among them. Waited for me. I never came. Broke my word. Chose alliance over promise. Was it right? Don't know. But it's done. Can't undo death.{/i}"
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["broke_promise"] = True
            $ reputation["resistance"] += 4
            $ characters["hector_father"]["trust"] = -10
            $ characters["hector_father"]["dead"] = True
            $ stats["people_killed"] += 30  # Indirectly, through inaction

    # RESOLUTION: Continue with alliance
    jump crisis_resolution_success


# =======================================================
# CRISIS 5: Debt Collector Returns
# =======================================================

label crisis_debt_collector:
    
    # VISUAL: Conversation interrupted. Man approaching. Angry. Familiar. The debt collector from Activity 5.
    # SOUND: Aggressive footsteps. Weapon visible. Threat.
    
    "{i}Footsteps. Angry. Aggressive. Man approaching. Armed. I know him. The debt collector. From the vendor situation. Fuck.{/i}"
    
    # VISUAL: DEBT COLLECTOR. Dragging someone. Vendor DREN. Beaten. Bloodied. Terrified.
    debt_collector "There you are. Been looking for you."
    
    # VISUAL: Aeron recognizes. The man he intervened with. The vendor he vouched for.
    a "Let him go."
    debt_collector "Let him go? After he didn't pay? After YOU vouched for him?"
    debt_collector "(throws Dren down) You vouched. That means his debt became yours. He owes 300 scrip. You owe 300 scrip."
    
    # VISUAL: Selene watching. Evaluating. Another debt. Another complication.
    selene "Friend of yours?"
    a "Vendor I helped. Week ago. Vouched for him when he owed money. Gave him time to pay."
    selene "And he didn't pay."
    a "Apparently not."
    
    # VISUAL: Dren on ground. Beaten. Apologetic. Pathetic.
    dren "(coughing) I tried! Business was bad! Nobody's buying! I couldn't make the scrip!"
    debt_collector "Excuses don't pay debts. And now your voucher pays instead. That's how it works down here."
    
    # VISUAL: Debt collector looking at Aeron. Weapon visible. Threat clear.
    debt_collector "300 scrip. Now. Or I take payment in blood. Yours or his. Don't care which."
    
    # ACTION: Player choice - how to resolve debt?
    menu:
        "300 scrip owed. Dren's failure. Aeron's voucher. Debt collector waiting."
        
        "Pay the debt - 300 scrip" if inventory["scrip"] >= 300:
            $ scenes["meeting_selene"]["paid_debt"] = True
            $ inventory["scrip"] -= 300
            $ scenes["meeting_selene"]["selene_trust"] += 2
            
            a "Fine. 300 scrip. Here."
            
            # VISUAL: Transfers scrip. Debt collector counts. Satisfied.
            debt_collector "Smart. Knew you'd pay. Glass always pays his debts. Even when he shouldn't."
            debt_collector "(to Dren) You're lucky he's honorable. Next time find a different voucher."
            
            # VISUAL: Debt collector leaves. Dren remains. Grateful. Ashamed.
            dren "Thank you. I'm sorry. Business really was bad. I tried to pay. I swear."
            a "Just... don't borrow what you can't pay back. That's how you survive down here."
            dren "I know. I'll repay you. Somehow. I swear."
            
            # VISUAL: Selene watching. Approving but concerned.
            selene "You just spent 300 scrip on someone else's debt. That's generous. Stupid, but generous."
            a "I vouched. That means it's my responsibility. I keep my responsibilities."
            selene "Even when they cost you everything?"
            a "Especially then. Otherwise what's the point of giving your word?"
            
            selene "...I respect that. Even if it's financially idiotic. You honor your commitments. That matters."
            
            $ characters["dren"]["trust"] += 3
            $ characters["dren"]["debt_paid"] = True
            
        "Negotiate - offer alternative payment":
            $ scenes["meeting_selene"]["negotiated_debt"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            
            a "I don't have 300 scrip. But I can offer something else."
            debt_collector "Like what? I don't take promises."
            a "Information. Intel on Echelon patrol routes. Supply convoys. Targets worth more than 300 scrip."
            
            # VISUAL: Debt collector considering. Information has value. Calculating.
            debt_collector "Echelon intel? You got that?"
            a "I was Echelon. I know their patterns, their schedules, their weaknesses. That's worth more than scrip."
            debt_collector "...Prove it. Give me one piece. Right now. Then we'll talk."
            
            # VISUAL: Aeron shares intel. Real intel. Echelon convoy route. Next week.
            a "Supply convoy. Four trucks. Sector 8. Thursday dawn. Light guard. Worth raiding."
            debt_collector "(checks notes) That... that's real. That's valuable."
            debt_collector "Alright. Intel clears the debt. But I want more. Keep feeding me information and we're square."
            a "Deal. Dren's debt is paid. We're done."
            
            # VISUAL: Debt collector leaves. Dren relieved. Aeron compromised.
            selene "(quiet) You just gave intel to a debt collector. That intel could be used for anything. Could hurt people."
            a "Could. Or it could fund resistance through stolen Echelon supplies. Debt collector hits convoy, sells goods, funds operations."
            a "Not ideal. But pragmatic. And Dren's alive. Debt's paid. That's what matters."
            
            selene "Pragmatic. I can work with pragmatic. Just be careful. Information is a weapon. Make sure it doesn't backfire."
            
            $ characters["dren"]["trust"] += 2
            $ scenes["meeting_selene"]["gave_intel_to_collector"] = True
            
        "Fight the debt collector - refuse to pay":
            $ scenes["meeting_selene"]["fought_collector"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 0
            
            a "No. I'm not paying. Dren's debt isn't mine. I vouched, but he's responsible."
            debt_collector "That's not how vouching works. You vouched, you pay. That's the rule."
            a "Then your rule is broken. I'm not paying for someone else's failure."
            
            # VISUAL: Debt collector's face hardens. Weapon drawn. Threat real.
            debt_collector "Then you both pay. In blood."
            
            # VISUAL: Quick draw. Fight. Brutal. Short. Aeron wins. Collector wounded. Flees.
            "{i}Draw. Fight. Fast. Brutal. Glass training. He's not fast enough. Not skilled enough. Down. Wounded. Fleeing. Threat ended. For now.{/i}"
            
            # VISUAL: Dren horrified. Selene disappointed. Violence solved problem but created new ones.
            dren "You... you didn't have to do that. Now he'll come back with more people. They always do."
            a "Then you better run. Because I'm not protecting you again."
            dren "But you vouched! You promised!"
            a "And you failed. Your failure. Your consequences. Deal with it yourself."
            
            # VISUAL: Dren fleeing. Scared. Abandoned. Selene watching Aeron coldly.
            selene "That was cold. Vouched for him then abandoned him when it cost you."
            a "I gave him a chance. He wasted it. I'm not responsible for his failures."
            selene "No. But you are responsible for your word. And you just broke it."
            selene "That's concerning. Shows you'll make promises you won't keep when they're inconvenient."
            
            $ characters["dren"]["trust"] = -5
            $ characters["dren"]["abandoned"] = True
            $ reputation["unders"] -= 2
            
        "Let Dren pay - step aside, let collector take him":
            $ scenes["meeting_selene"]["abandoned_dren"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            
            a "Take him. He borrowed. He didn't pay. He deals with consequences."
            dren "(horrified) What? You vouched! You said—"
            a "I vouched on the condition you'd pay. You didn't. Deal's void."
            
            # VISUAL: Debt collector grinning. Grabbing Dren. Violence incoming.
            debt_collector "Smart. Knew you'd see reason. Always do in the end."
            dren "(screaming) Please! I tried! I really tried! Please don't—"
            
            # VISUAL: Debt collector dragging Dren away. Beating him. Brutal. Public example.
            "{i}Dren screaming. Beaten. Dragged away. I don't watch. Don't need to. I know what happens to people who don't pay debts down here. They become examples.{/i}"
            
            # VISUAL: Selene observing. Cold calculation. Testing Aeron's limits.
            selene "You let him go. After vouching. After promising him time."
            a "He had time. He wasted it. I'm not responsible for his poor decisions."
            selene "That's practical. Cold, but practical. Shows you understand how things work down here."
            selene "But it also shows you'll abandon people when it's convenient. That's useful to know."
            
            l "(quiet) That was harsh."
            a "That was necessary. Can't save everyone. Can't pay everyone's debts. Have to prioritize."
            l "And Dren wasn't a priority?"
            a "No. He wasn't. The mission is. The resistance is. Random vendors who can't manage money? Not my problem."
            
            # VISUAL: Sound of Dren being beaten. Distant. Ignored. Accepted.
            "{i}Dren's screams fade. Problem solved. Debt avoided. Dren pays his own price. Is this who I am now? Practical. Cold. Abandoning people. Maybe. Maybe it's necessary. Or maybe I'm just becoming Glass again with different excuses.{/i}"
            
            $ characters["dren"]["trust"] = -10
            $ characters["dren"]["beaten"] = True
            $ reputation["unders"] -= 1
            $ scenes["meeting_selene"]["showed_coldness"] = True

    # RESOLUTION: Continue with alliance discussion
    jump crisis_resolution_success


# =======================================================
# CRISIS 6: Kren's Warning
# =======================================================

label crisis_kren_warning:
    
    # VISUAL: Urgent movement. Running. Someone approaching fast. Familiar gait. Vendor.
    # SOUND: Running. Panicked. Desperate. Warning.
    
    "{i}Running. Fast. Desperate. Someone coming. Kren. The vendor I worked for. Why is he here? How does he know this location?{/i}"
    
    # VISUAL: KREN bursts into ruins. Bleeding. Shoulder wound. Exhausted. Determined.
    kren "(gasping) Aeron! Thank the stars! I found you!"
    
    # VISUAL: Aeron moving to him. Concerned. Kren shouldn't be here.
    a "Kren? What happened? Why are you here?"
    kren "(breathing hard) Echelon patrol. They found me. Asked about you. About Kade Voss."
    kren "I told them nothing. They didn't believe me. Started asking... harder."
    
    # VISUAL: Shows shoulder wound. Torture mark. Interrogation. Escaped.
    kren "I got away. Barely. Followed you here to warn you. They're coming. Right behind me."
    
    # VISUAL: Selene's face hardens. Compromised location. Immediate threat.
    selene "You led them here? To our meeting?"
    kren "I didn't mean to! I was trying to warn you! They were going to raid—"
    selene "And now they'll raid us instead! How long?"
    kren "Minutes. Maybe five. They're mobilizing. Full patrol. Twenty soldiers."
    
    # VISUAL: Resistance fighters tensing. Weapons ready. Evacuation or fight. Decision time.
    selene "We need to move. Now. This location is compromised."
    
    # VISUAL: Aeron looking at Kren. Bleeding. Exhausted. Can't run. Can't fight. Liability.
    a "{i}Kren's wounded. Can't run. Can't fight. Dead weight in evacuation. But he came here to warn us. To save us. Despite being tortured. That loyalty means something.{/i}"
    
    # ACTION: Player choice - what to do?
    menu:
        "Echelon patrol incoming. Five minutes. Kren wounded. What do we do?"
        
        "Evacuate with Kren - save him despite cost":
            $ scenes["meeting_selene"]["saved_kren"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            
            a "We take him with us. He warned us. We don't leave him behind."
            selene "He's wounded. He'll slow us down."
            a "Then we move slower. But we move together. He risked his life for us. We return the favor."
            
            # VISUAL: Helping Kren up. Supporting him. Moving toward evacuation route.
            kren "(pained) I'm sorry. I tried to lose them. I swear I tried."
            a "You did good. You warned us. That's all that matters. Now we get you safe."
            
            # VISUAL: Evacuation. Kren supported. Moving through ruins. Patrol approaching.
            selene "Faster! They're close! I can hear engines!"
            
            # VISUAL: Narrow escape. Underground tunnels. Echelon patrol arrives just as they disappear.
            "{i}Underground. Tunnels. Old smuggling routes. Echelon above, searching. We're below, moving. Silent. Careful. Kren's breathing loud but controlled. We made it. Barely. But made it.{/i}"
            
            # VISUAL: Safe location. Hours later. Kren being treated. Alive. Grateful.
            kren "Thank you. For not leaving me. I thought... I thought you would."
            a "You came to warn us. Took torture. Escaped. Led them away from your market. That's loyalty. We honor loyalty."
            kren "I won't forget this. Ever. I owe you my life."
            
            # VISUAL: Selene observing. Approving. Loyalty to contacts matters.
            selene "You value your contacts. You protect people who help you. That's good leadership."
            selene "Slowed us down. Could have cost us. But you were right. Abandoning Kren would have been wrong."
            selene "Welcome to the resistance. You understand what we fight for."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 3
            $ characters["kren"]["trust"] += 5
            $ characters["kren"]["life_debt"] = True
            
        "Leave Kren - evacuate fast without him":
            $ scenes["meeting_selene"]["abandoned_kren"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            
            a "We can't take him. He's wounded. He'll slow us down and get everyone killed."
            kren "(horrified) What? But I came to warn you!"
            a "And we're grateful. But you led them here. Accidentally or not, you compromised us. We have to move fast."
            kren "You're leaving me? After everything?"
            a "I'm sorry. I have to. Selene's people matter more than one wounded vendor."
            
            # VISUAL: Selene nods. Cold approval. Practical decision.
            selene "Move! Now! Leave him!"
            
            # VISUAL: Evacuation. Fast. Efficient. Kren left behind. Pleading. Ignored.
            "{i}Running. Fast. Efficient. Behind us, Kren pleading. Ignored. Can't afford the weight. Can't afford the delay. Practical. Necessary. Horrible. But necessary.{/i}"
            
            # VISUAL: Underground tunnels. Safe. Echelon finds Kren instead of them.
            # SOUND: Distant. Kren's final screams. Echelon's frustration. Execution.
            
            "{i}Underground. Safe. Above, Kren screaming. Echelon found him instead of us. Executing him. Making example. He warned us. We abandoned him. He died alone. Because of me. Because I chose others over him.{/i}"
            
            # VISUAL: Safe location. Selene satisfied. Practical decision made. No casualties except Kren.
            selene "Clean escape. No casualties. Good decision. Hard decision. But good."
            a "Kren died."
            selene "Yes. But we lived. That's the math of resistance. We save who we can. We sacrifice when we must."
            selene "You understand that now. You made the call. The hard call. That's leadership."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 2
            $ characters["kren"]["dead"] = True
            $ reputation["unders"] -= 2
            $ scenes["meeting_selene"]["showed_coldness"] = True
            
        "Fight at the location - defend instead of run":
            $ scenes["meeting_selene"]["fought_at_location"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 0
            
            a "We fight. Here. Now. Defend this position."
            selene "Are you insane? Twenty soldiers incoming! We're outnumbered!"
            a "So we run forever? Always evacuating? No. We make a stand. We show them we're not afraid."
            selene "We show them we're stupid! This isn't a stand, it's suicide!"
            
            # VISUAL: Aeron stubborn. Kren watching. Grateful but horrified. Selene furious.
            l "Aeron, she's right. We can't win this."
            a "Maybe not. But I'm tired of running. Tired of always being one step from death. If we run now, we run forever."
            selene "And if we fight now, we die now! That's not strategy! That's pride!"
            
            # VISUAL: Echelon patrol arriving. No more time for debate. Fight forced.
            "{i}Too late. They're here. Patrol arriving. Twenty soldiers. We're seven. Plus Kren wounded. Bad odds. Terrible odds. But here we are.{/i}"
            
            # VISUAL: Fierce firefight. Resistance defending. Taking casualties. Brutal. Desperate.
            "{i}Fight. Cover. Return fire. They're everywhere. Too many. Too skilled. We're going down. One by one. This was a mistake. Glass's pride. Aeron's stubbornness. Same thing.{/i}"
            
            # VISUAL: Kren shot. Protecting Aeron. Dies saving the man who tried to save him.
            kren "(hit, falling) At least... I warned you..."
            a "(catching him) Kren! No! Stay with me!"
            kren "(dying) Thank you... for trying..."
            
            # VISUAL: More casualties. Two resistance fighters down. Selene screaming orders.
            selene "Fall back! FALL BACK! This position is lost! MOVE!"
            
            # VISUAL: Forced retreat. Kren dead. Two resistance fighters dead. Three wounded. Disaster.
            "{i}Retreat. Casualties. Kren dead. Two resistance fighters dead. Three wounded. Disaster. Complete disaster. Because I was stubborn. Because I wouldn't run. Because pride mattered more than survival.{/i}"
            
            # VISUAL: Safe distance. Regrouping. Selene furious. Aeron's leadership destroyed.
            selene "Three dead. Three wounded. For what? For pride? For making a stand?"
            a "I thought—"
            selene "You didn't think! You acted like Glass! Stubborn. Proud. Convinced your way was right!"
            selene "My people died because you wouldn't listen! That's not leadership! That's arrogance!"
            
            $ scenes["meeting_selene"]["alliance_formed"] = False
            $ scenes["meeting_selene"]["casualties"] = 5
            $ reputation["resistance"] -= 5
            $ characters["kren"]["dead"] = True
            
            # This path damages alliance severely - will need to rebuild trust
            jump crisis_resolution_failure

    # RESOLUTION: Continue with alliance (if successful)
    jump crisis_resolution_success


# =======================================================
# CRISIS 7: Noelle's Algorithm (Default Fallback)
# =======================================================

label crisis_noelle_algorithm:
    
    # VISUAL: Selene about to continue negotiation. Device beeps. Urgent. Noelle.
    # SOUND: Alert. High priority. Analysis complete.
    
    "{i}Device. Alert. Noelle. Analysis complete. Timing suspicious. What did she find?{/i}"
    
    # VISUAL: Checks message. Face hardens. Data. Predictions. Bad news.
    # MESSAGE: "Predictive algorithm shows massive Echelon mobilization. Multiple targets. Resistance cells. Simultaneous strikes in 20 minutes. Including your location. Evacuate immediately. - N"
    
    a "(reading) Noelle's algorithm detected Echelon mobilization. They're hitting multiple resistance cells. Simultaneously. Twenty minutes."
    selene "What? How does she know?"
    a "She analyzes patrol patterns. Predicts movements. She's been tracking Echelon for months. If she says they're coming, they're coming."
    
    # VISUAL: Selene calculating. Trust Noelle's data or stay.
    selene "I don't know her. Don't know her methods. How do I know this isn't false intel?"
    a "Because I've worked with her. Her predictions are solid. 89 percent accuracy. If she says evacuate, we evacuate."
    
    # VISUAL: Selene torn. Trusting stranger's data vs ignoring warning.
    l "If she's right and we stay, we die. If she's wrong and we run, we're inconvenienced. The math is clear."
    
    # ACTION: Selene's choice - trust Noelle or stay?
    menu:
        "Trust Noelle's data or stay?"
        
        "Trust Noelle - evacuate immediately":
            $ scenes["meeting_selene"]["trusted_noelle"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            
            selene "...Fine. We evacuate. If your analyst is wrong, we'll discuss it. If she's right, we owe her."
            selene "Everyone move! Evacuation protocol! Twenty minutes to get clear!"
            
            # VISUAL: Rapid evacuation. Resistance fighters moving. Practiced. Efficient.
            "{i}Evacuation. Fast. Practiced. They've done this before. Lost cells to raids. Know how to move. Trust Selene. Trust the process.{/i}"
            
            # VISUAL: Underground routes. Moving through tunnels. Nineteen minutes. Eighteen. Seventeen.
            "{i}Moving. Underground. Old subway. Maintenance tunnels. City's veins. Resistance knows them. Echelon doesn't. Nineteen minutes. Eighteen. Seventeen. Counting down.{/i}"
            
            # VISUAL: Safe location. Just reached. Countdown hits zero.
            # SOUND: Distant explosions. Multiple. Synchronized. Echelon strikes.
            
            "{i}Safe. Just made it. Countdown zero. Above, explosions. Multiple. Synchronized. Exactly as Noelle predicted. Four locations hit simultaneously. Ours included. Would have died if we stayed.{/i}"
            
            # VISUAL: Checking reports. Four resistance cells hit. Three stayed. Wiped out. One evacuated. Survived.
            selene "(reading reports) Three cells didn't evacuate. Gone. Everyone dead. We're the only ones who made it out."
            a "Because we trusted Noelle."
            selene "Because you trusted her. And convinced me to. That saved everyone."
            
            # VISUAL: Selene looking at Aeron. Respect. Genuine. Earned.
            selene "Your analyst just saved my entire cell. That's not small. That's everything."
            selene "I want to meet her. Work with her. If her predictions are that accurate, she's invaluable."
            a "I'll arrange it. She's been operating solo. Might be glad to have support."
            selene "Do it. And welcome to the resistance. You just proved your worth. Your people's worth. We work together now."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 0
            $ reputation["resistance"] += 5
            $ characters["noelle"]["trust"] += 3
            $ characters["noelle"]["resistance_value_proven"] = True
            
        "Ignore warning - stay and verify":
            $ scenes["meeting_selene"]["ignored_noelle"] = True
            $ scenes["meeting_selene"]["selene_trust"] -= 1
            
            selene "We stay. I don't abandon positions on unverified intel from strangers."
            a "Noelle's not a stranger to me. Her data is reliable."
            selene "Maybe. But I verify before I move an entire cell. We stay. We watch. We see if your analyst is right."
            
            # VISUAL: Waiting. Tense. Fifteen minutes. Ten. Five. Nothing happening yet.
            "{i}Waiting. Ten minutes. Five. Nothing. Maybe Noelle was wrong? Maybe false alarm? Or maybe...{/i}"
            
            # VISUAL: Countdown hits zero. EXPLOSION. Nearby. Massive. Echelon strike.
            # SOUND: Explosion. Shockwave. Debris. Chaos.
            
            "{i}EXPLOSION. Nearby. Massive. Building collapses. Echelon strike. Exactly as Noelle predicted. Exactly on time. Should have listened. Should have evacuated.{/i}"
            
            # VISUAL: Chaos. Resistance fighters scrambling. Echelon forces moving in. Trapped.
            selene "(shouting) Defensive positions! We fight our way out! MOVE!"
            
            # VISUAL: Firefight. Desperate. Escaping while under fire. Casualties mounting.
            "{i}Fight. Escape. Fire. Casualties. Three resistance fighters down. Wounded, maybe dead. Could have been zero if we evacuated. If Selene trusted Noelle. If I insisted harder.{/i}"
            
            # VISUAL: Finally escape. Casualties. Wounded. Exhausted. Selene furious at herself.
            selene "(breathing hard) Your analyst was right. Exactly right. And I didn't listen."
            selene "Three of my people down because of my pride. Because I wouldn't trust unverified intel."
            a "We got out. That's what matters."
            selene "No. What matters is I almost got everyone killed. You tried to warn me. Your analyst tried to warn me. I ignored it."
            selene "...You're in. And bring your analyst. I need people who are right when I'm wrong. She's one of them."
            
            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 3
            $ reputation["resistance"] += 2
            $ characters["noelle"]["trust"] += 2

    # RESOLUTION: Continue with alliance
    jump crisis_resolution_success


# =======================================================
# CRISIS RESOLUTION - SUCCESS PATH
# =======================================================

label crisis_resolution_success:
    
    # VISUAL: Aftermath of crisis. Whatever happened. Alliance forged through fire.
    # LIGHTING: Changed. Darker or brighter depending on outcome. But resolved.
    
    scene bg_sector6_ruins_aftermath with fade
    
    "{i}Aftermath. Crisis resolved. Alliance forged. Not through words. Through action. Through fire. Through choice. This is what resistance looks like. Messy. Costly. Real.{/i}"
    
    # VISUAL: Selene and Aeron. Eye to eye. Equals now. Forged through crisis.
    selene "We survived. That's more than most meetings accomplish."
    a "We did more than survive. We proved we can work together."
    selene "Maybe. Or maybe we proved we're both too stubborn to quit. Either way, you're in."
    
    # VISUAL: Selene extends hand. Offer. Alliance. Partnership.
    selene "Welcome to the resistance. Probation starts now. You fuck up, you're out. You betray us, you're dead. Clear?"
    a "(shakes hand) Clear. We won't fuck up. And we won't betray you. We're done with Echelon. Done with Glass. Done with all of it."
    selene "We'll see. Words are easy. Actions prove everything. So prove it. Every day. Every mission. Every choice."
    a "We will. I promise."
    
    # VISUAL: Lyra stepping forward. Part of this. Equal partner.
    l "Both of us. We're a package. We fight together or not at all."
    selene "Fine. Two Glass defectors. Double the liability or double the asset. Time will tell which."
    
    # VISUAL: Resistance fighters watching. Some hostile. Some curious. All evaluating.
    selene "(to resistance) These two are with us now. Probation. Any problems, bring them to me. Not to them. Understood?"
    resistance_fighter "Understood. But we're watching them."
    selene "Good. Everyone watches everyone. That's how we survive."
    
    # VISUAL: Selene turning back to Aeron and Lyra. Brief moment. Personal.
    selene "You lost people in that Sweep. I lost people in that Purge. We've both bled for Echelon's sins."
    selene "Now we bleed Echelon instead. Together. Make them pay for every death. Every casualty. Every person they crushed."
    a "That's the plan. Burn it all down. Every piece. Every system. Every lie."
    selene "Good. Because that's a war. And wars need soldiers who've already lost everything."
    selene "You qualify. Welcome to the war."
    
    # VISUAL: Sun rising over ruins. New day. New beginning. New war starting.
    "{i}Sun rising. New day. New beginning. We're resistance now. Officially. No going back. No second thoughts. Just forward. Into fire. Into war. Into whatever comes next.{/i}"
    
    # Mark alliance complete
    $ scenes["meeting_selene"]["alliance_formed"] = True
    $ canon["resistance_joined"] = True
    $ canon["met_selene"] = True
    
    # Update final trust score
    $ selene_final_trust = scenes["meeting_selene"]["selene_trust"]
    
    # Show outcome
    if selene_final_trust >= 5:
        "{i}Selene trusts us. Actually trusts us. Not fully. Not yet. But enough to fight beside us. Enough to believe we might actually do what we say. That's more than I expected. More than I deserve maybe. But I'll earn it. We'll earn it.{/i}"
    elif selene_final_trust >= 2:
        "{i}Selene's cautious. Watching. Evaluating. We're on probation and she means it. One mistake and we're out. But we're in. That's something. That's a start. We build from here.{/i}"
    else:
        "{i}Selene doesn't trust us. Not really. We're tools. Useful but disposable. Have to prove ourselves every single day. Every single mission. Or we're dead. That's the reality. We accept it.{/i}"
    
    # Check casualties
    $ total_casualties = scenes["meeting_selene"].get("casualties", 0)
    
    if total_casualties == 0:
        "{i}No casualties. Everyone survived. That's rare. That's valuable. Selene noticed. Won't forget. Clean operations matter. Lives matter. We proved that today.{/i}"
    elif total_casualties <= 3:
        "{i}[total_casualties] casualties. Not zero. Not acceptable. But not catastrophic. Could have been worse. Could have been everyone. We did what we could. It wasn't enough for them. But it was something.{/i}"
    else:
        "{i}[total_casualties] casualties. Too many. Way too many. Blood on my hands. Again. Different cause. Same result. People dead because of choices I made. Have to live with that. Have to do better. Have to make it worth their sacrifice.{/i}"
    
    # VISUAL: Final moment. Selene's cell. Aeron and Lyra. Together. Resistance.
    selene "First mission briefing tomorrow. Dawn. Don't be late. We have work to do."
    a "We'll be there."
    selene "Good. Now get out of here. Find somewhere to sleep. Tomorrow we start breaking Echelon. Piece by piece."
    
    # TRANSITION: Leaving ruins. Together. Changed. Forward.
    "{i}Leaving. Together. Different than when we arrived. We came as fugitives. We leave as resistance. We came broken. We leave forged. Still broken. But forged into something that might actually matter.{/i}"
    
    # VISUAL: Aeron and Lyra walking. Dawn breaking. Future uncertain but faced together.
    l "We did it. We actually did it."
    a "We joined the resistance. That was the easy part."
    l "What's the hard part?"
    a "Everything that comes next. The missions. The war. The dying. All of it."
    l "Then we do it together. Like always."
    a "Together. Yeah. Always together."
    
    # FINAL SCENE: ACT 2 COMPLETE
    "{i}Act 2 complete. From fugitives to resistance. From hunted to hunters. The war begins. And we're ready. As ready as broken people can be. Which might be enough. Might be everything.{/i}"
    
    # Jump to Act 2 finale or Act 3 beginning

    # canon_note: Scene 7 complete - met Selene, survived crisis, joined resistance
    # canon_note: Dynamic crisis system - player choices from activities determine which crisis triggers
    # canon_note: Multiple paths through each crisis - choices have consequences
    # canon_note: Alliance formed (or damaged) based on decisions made during crisis
    # canon_note: Selene trust variable tracks relationship quality
    # canon_note: Casualties tracked - affects future missions and morale
    # canon_note: Resistance joined officially - Act 2 complete, Act 3 setup begins
    # canon_note: All harem members preserved - no core character deaths
    # canon_note: Replayability ensured - different activities create different crises
    # canon_note: Consequences carry forward - debts, promises, relationships all matter
    # canon_note: Sets up Act 3 - war against Echelon begins with Selene's cell as base

    return


# =======================================================
# CRISIS RESOLUTION - FAILURE PATH
# =======================================================

label crisis_resolution_failure:
    
    # VISUAL: Aftermath of crisis. Disaster. Alliance damaged or destroyed.
    scene bg_sector6_ruins_disaster with fade
    
    "{i}Disaster. Complete disaster. Too many casualties. Too many mistakes. Too much Glass showing through the cracks. Selene's done with us.{/i}"
    
    # VISUAL: Selene furious. Resistance fighters dead or wounded. Trust shattered.
    selene "Get out."
    a "Selene, wait—"
    selene "(cold) GET. OUT. Before I shoot you myself."
    selene "My people are dead. Because of you. Because of your choices. Because I was stupid enough to give you a chance."
    
    # VISUAL: Aeron trying to salvage. Failing. Selene done listening.
    a "I'm sorry. I didn't mean—"
    selene "You never mean anything. But people still die. That's the problem with Glass. You break everything you touch."
    selene "You're not resistance. You're just Echelon with a guilty conscience. And I don't work with Echelon."
    
    # VISUAL: Resistance fighters raising weapons. Not quite aiming. But ready.
    selene "Leave. Now. Don't come back. If I see you again, I'll assume you're a threat. And I'll eliminate threats."
    
    # VISUAL: Aeron and Lyra forced to leave. Alliance destroyed. No resistance support.
    "{i}Leaving. Forced out. Alliance destroyed before it began. We're alone again. Worse than alone. Now Selene's cell hates us too. Added to the list of people who want us dead.{/i}"
    
    l "(quiet) What do we do now?"
    a "...I don't know. We fucked up. Completely. Selene was our only option and we burned that bridge."
    l "So we find another option."
    a "What other option? She was the last organized resistance. Everyone else is dead or scattered."
    l "Then we scatter too. Survive. Regroup. Try again later."
    a "If there is a later."
    
    # Mark alliance failed
    $ scenes["meeting_selene"]["alliance_formed"] = False
    $ canon["resistance_joined"] = False
    $ reputation["resistance"] = -10
    
    "{i}Alliance failed. Act 2 incomplete. We're still fugitives. Still hunted. Still alone. Everything we worked for—wasted. Because of choices. Because of Glass. Because I couldn't let go of who I was.{/i}"
    
    # This creates alternate path - must find another way into resistance later
    # Or build their own cell from scratch
    # Harder path. More isolated. But possible.
    
    jump act2_finale_failure

    # canon_note: Failure path - alliance with Selene destroyed through bad choices
    # canon_note: Creates alternate storyline - must build resistance from scratch or find other cells
    # canon_note: Harder path forward but still winnable
    # canon_note: Shows consequences matter - player choices have real weight
    # canon_note: Can potentially rebuild relationship with Selene later through Act 3 missions
    # canon_note: This path makes Act 3 more difficult but more rewarding if successful

    return


# =======================================================
# Temporary end labels (will be replaced with actual Act 2 finale scenes)
# =======================================================

label act2_finale:
    "Act 2 Complete - Resistance Joined Successfully"
    "Act 3 Beginning..."
    return

label act2_finale_failure:
    "Act 2 Complete - Alliance Failed"
    "Alternate Path Beginning..."
    return

# TODO: FIX JUMPING