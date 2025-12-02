# act2_13_meeting_selene.rpy


# =======================================================
# ACT 2 - Scene 13: Meeting Selene (+ Dynamic Crisis)
# =======================================================


label act2_meeting_selene:

    # --- SCENE START (new helper system) ---
    $ mark_scene("act2_meeting_selene", start=True)
    $ log_line("act2_meeting_selene", "enter")

    # Initialize scene tracking
    $ scenes["meeting_selene"] = {
        "crisis_type": None,
        "selene_trust": 0,
        "alliance_formed": False,
        "casualties": 0,
        "crisis_resolved": False
    }

    # --- AERON OB/EMP SNAPSHOT (computed + logged) ---
    python:
        _a7 = scenes.get("activity7_past", {})
        _a5 = scenes.get("activity5_reputation", {})
        _chars = characters if 'characters' in globals() else {}
        _inv = inventory if 'inventory' in globals() else {}
        _rep = reputation if 'reputation' in globals() else {}
        _stats = stats if 'stats' in globals() else {}

        # Empathy score (higher = more other-centered, reparative choices)
        emp_score = 0
        emp_score += 2 if _a7.get("offered_help") else 0
        emp_score += 1 if _a7.get("just_listened") else 0
        emp_score -= 2 if _a7.get("defended_actions") else 0
        emp_score += 1 if _a5.get("intervened_debt") else 0
        emp_score += 2 if _a5.get("saved_child") else 0
        emp_score += 1 if _rep.get("unders", 0) >= 3 else 0
        emp_score += 1 if _chars.get("lyra", {}).get("trust", 0) >= 6 else 0
        emp_score += 1 if _stats.get("people_saved", 0) >= 20 else 0

        # Observation/Operational score (higher = clear tactical read, reduced self-justification)
        ob_score = 0
        ob_score += 1 if len(_inv.get("weapons", [])) > 0 else 0
        ob_score += 1 if _rep.get("unders", 0) >= 2 else 0
        ob_score += 1 if _chars.get("zira", {}).get("trust", 0) >= 6 else 0
        ob_score -= 1 if "debts_owed" in _inv and len(_inv.get("debts_owed", [])) > 0 else 0
        ob_score -= 1 if _a7.get("defended_actions") else 0
        ob_score += 1 if _chars.get("noelle", {}).get("trust", 0) >= 3 else 0

        # Qualitative buckets
        emp_state = "guarded empathy online" if emp_score <= 1 else ("active empathy engaged" if emp_score <= 4 else "high-empathy override")
        ob_state  = "fogged ops read" if ob_score <= 0 else ("tactical clarity" if ob_score <= 3 else "cold-clear operational focus")

        # Persist + log
        scenes["meeting_selene"]["emp_score"] = emp_score
        scenes["meeting_selene"]["ob_score"] = ob_score
        scenes["meeting_selene"]["emp_state"] = emp_state
        scenes["meeting_selene"]["ob_state"]  = ob_state

    $ log_line("act2_meeting_selene", f"OB/EMP pre: emp={emp_score} ({emp_state}) ob={ob_score} ({ob_state})")

    # VISUAL: Sector 6 ruins. Dawn. Broken buildings. Devastation everywhere.
    # LIGHTING: Gray dawn light. Cold. Harsh shadows.
    # SOUND: Wind through ruins. Rubble shifting. Footsteps approaching.

    scene bg_sector6_ruins_dawn with fade

    "Sector 6 ruins. Dawn barely breaking. The Purge left this place shattered—collapsed buildings, torn streets, ghosts everywhere. Perfect neutral ground because nobody wants it anymore."
    "[ob] {scenes['meeting_selene']['ob_state']}. Snipers east ridge; two flank routes choke to killing funnels."
    "[emp] {scenes['meeting_selene']['emp_state']}. If this goes bad, count the living on the way out."

    # VISUAL: Figures emerge from ruins. Armed. Cautious. Resistance fighters.
    # 4-5 people. Battle-worn. Survivors. Angry. Grieving. Dangerous.

    "Movement. Figures emerging from cover. Armed. Four of them. Maybe five. Hard to tell in the shadows. All pointing weapons at us."

    # VISUAL: Aeron and Lyra stop. Hands visible. Not reaching for weapons. Non-threatening.
    l "(quiet) Five visible. Probably more we can't see."
    a "Definitely more. Snipers on rooftops. Flankers in ruins. She's smart."
    l "Or paranoid."
    a "Down here, they're the same thing."

    # VISUAL: Resistance fighters part. Woman walks through. Mid-30s. Scarred. Exhausted. Determined.
    # SELENE: Leader. Survivor. Epitome of determination despite everything lost.

    "They part. One woman walks forward. Mid-thirties, scarred face, eyes that have seen too much death. This is Selene. The woman whose people I killed. Whose sector I swept. Who lost everything twice—once to me, once to the Purge."

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

    # ========== CRISIS ROUTING SYSTEM (fixed control flow) ==========
    $ crisis_triggered = None

    if scenes.get("activity2_weapons", {}).get("method") == "stolen_echelon":
        $ crisis_triggered = "tracked_weapons"
        $ scenes["meeting_selene"]["crisis_type"] = "tracked_weapons"
        $ log_line("act2_meeting_selene", "crisis=tracked_weapons")
        jump crisis_tracked_weapons

    elif "vex" in inventory.get("debts_owed", []):
        $ crisis_triggered = "vex_favor"
        $ scenes["meeting_selene"]["crisis_type"] = "vex_favor"
        $ log_line("act2_meeting_selene", "crisis=vex_favor")
        jump crisis_vex_favor

    elif scenes.get("activity1_work", {}).get("job_chosen") == "smuggling":
        $ crisis_triggered = "kelvin_mole"
        $ scenes["meeting_selene"]["crisis_type"] = "kelvin_mole"
        $ log_line("act2_meeting_selene", "crisis=kelvin_mole")
        jump crisis_kelvin_mole

    elif scenes.get("activity7_past", {}).get("offered_help"):
        $ crisis_triggered = "sector10_rescue"
        $ scenes["meeting_selene"]["crisis_type"] = "sector10_rescue"
        $ log_line("act2_meeting_selene", "crisis=sector10_rescue")
        jump crisis_sector10_rescue

    elif scenes.get("activity5_reputation", {}).get("intervened_debt"):
        $ crisis_triggered = "debt_collector"
        $ scenes["meeting_selene"]["crisis_type"] = "debt_collector"
        $ log_line("act2_meeting_selene", "crisis=debt_collector")
        jump crisis_debt_collector

    elif characters.get("kren", {}).get("met") and scenes.get("activity1_work", {}).get("job_chosen") == "market_stall":
        $ crisis_triggered = "kren_warning"
        $ scenes["meeting_selene"]["crisis_type"] = "kren_warning"
        $ log_line("act2_meeting_selene", "crisis=kren_warning")
        jump crisis_kren_warning

    else:
        $ crisis_triggered = "noelle_algorithm"
        $ scenes["meeting_selene"]["crisis_type"] = "noelle_algorithm"
        $ log_line("act2_meeting_selene", "crisis=noelle_algorithm")
        jump crisis_noelle_algorithm


# =======================================================
# CRISIS 1: Tracked Weapons (Stolen from Echelon)
# =======================================================

label crisis_tracked_weapons:

    "Beeping. Loud. Proximity alarm. Someone's resistance fighter's device lighting up. Red. Urgent. Incoming."
    "[ob] Heat-map in my head: eight vectors, two probable decoy pushes."

    resistance_fighter "Contact! Multiple signatures! Echelon patrol converging on this position!"

    selene "How? This location was secure! How did they find us?"

    resistance_fighter2 "Tracking signal! Coming from... them!"

    resistance_fighter2 "Their weapons! Echelon gear! They're broadcasting!"

    selene "(cold) You led them here. Deliberately or stupidly, doesn't matter. My people are in danger because of you."

    athought "The weapons. We stole them from Echelon patrol. Ambushed them, took their gear. Of course they were tracked. Of course. How did I not think of that?"

    a "We didn't know. The weapons—we stole them from Echelon. We didn't know they were tracked."
    selene "You didn't CHECK? You brought enemy gear to a resistance meeting and didn't check for trackers?"
    selene "That's not inexperience. That's negligence. And my people die because of it."

    l "We can fix this. Drop the weapons. Scatter. Lead them away—"
    selene "Too late. They're already here. We fight or we die."

    "Gunfire. Sudden. Loud. Echelon forces pouring into ruins from multiple angles. Eight of them. Ten. Professional. Coordinated. We led them right here."
    "[emp] Own it. Fix it. Keep people breathing."

    selene "(shouting) Defensive positions! Cover fire! Get the wounded out!"

    athought "Their tactics. I know them. Taught them. Trained with them. Pincer movement, suppressing fire, flanking maneuver. Textbook Echelon assault."

    menu:
        "Chaos. Gunfire. People dying because we brought tracked weapons. How do we fix this?"
        "Fight alongside resistance - prove yourself through action":
            $ scenes["meeting_selene"]["fought_with_resistance"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            $ log_line("act2_meeting_selene", "choice=fight_with_resistance")

            a "(to Selene) I fucked up. I'm sorry. But I can help fix it. I know their tactics. Let me fight with you."
            selene "You want to help? Don't get my people killed trying!"
            a "I won't. I promise. Just trust me for five minutes."

            "Move. Cover. Return fire. Muscle memory from years of Echelon training. But fighting against them now. Using their tactics against them. Poetic. Necessary. Desperate."

            a "(shouting) Two flanking left! They'll come through that archway in ten seconds!"

            resistance_fighter "He's right! How did you—"
            a "I trained them! I know how they think! Northwest corner next! Sniper position!"

            selene "(grudging) Keep talking! What else?"

            l "They're regrouping! Standard retreat pattern! Three. Two. One."
            a "When they pull back, they'll drop smoke. Don't chase. It's a trap."

            "Smoke clears. Echelon forces retreating. Defeated. We won. Somehow. Despite everything. Because we know them. Because we were them."

            selene "(breathing hard) Status!"
            resistance_fighter "Two wounded. Minor. Everyone else intact. They're retreating."
            selene "Casualties on their side?"
            resistance_fighter "Four down. Three wounded. Rest fled. We won."

            selene "You led them here. Your mistake almost killed my people."
            selene "But you also saved them. Your knowledge of Echelon tactics kept casualties minimal."
            selene "So I don't know whether to thank you or shoot you."

            a "I deserve both. I'm sorry. I should have checked the weapons. That's on me."
            selene "Yes. It is. And you'll answer for it. But not today."
            selene "Today you fought with us. Against them. That counts for something."

            $ scenes["meeting_selene"]["casualties"] = 2
            $ reputation["resistance"] += 3
            $ log_line("act2_meeting_selene", "result=win casualties=2 trust+2 rep+3")

            # Update OB/EMP post-action
            $ scenes["meeting_selene"]["emp_score"] += 1
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ log_line("act2_meeting_selene", f"OB/EMP post(fight): emp={scenes['meeting_selene']['emp_score']} ob={scenes['meeting_selene']['ob_score']}")

            jump crisis_resolution_success

        "Lead Echelon away - sacrifice play to save resistance":
            $ scenes["meeting_selene"]["led_away"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            $ log_line("act2_meeting_selene", "choice=lead_away trust+3")

            a "This is my fault. I brought them here. So I'll lead them away."
            selene "What?"
            a "They're tracking these weapons. So I take them and run. Draw them off. Give your people time to escape."
            selene "That's suicide. There's too many of them."
            a "Maybe. But it's better than your people dying because I was careless."

            l "Then I'm coming with you."
            a "Lyra—"
            l "Don't. We do this together. Always. You run, I run. You fight, I fight. You die, I die."
            a "...Together. Always together."

            "Run. Tracked weapons in hand. Shouting. Drawing attention. Making ourselves targets. Echelon forces see us. Recognize us. Turn pursuit our direction."
            "[emp] Debt paid in motion. Keep them on us, not on the wounded."

            a "(shouting back at Selene) Get your people out! We'll lead them away!"
            selene "You'll die!"
            a "Then we die! But your people live! That's what matters! Go!"

            "Rooftop. Trapped. Echelon forces below. No way out. No way down. This is it. This is where we die. But Selene's people got away. That's enough. That has to be enough."

            echelon_commander "Glass! Surrender! Marcus wants you alive! Comply and you won't be harmed!"

            a "(to Lyra) What do you think? Believe him?"
            l "Not even a little."
            a "Me neither. So we fight?"
            l "We fight. Together."
            a "Together. Until the end."

            "Gunfire. From behind. Echelon forces caught by surprise. Turning. Confusion. Who—?"
            selene "(shouting) Now! Hit them now!"

            "Caught between us. Resistance behind, us above. Crossfire. Echelon forces breaking. Retreating. Defeated. Selene came back. She came back for us."

            selene "You idiots. Running off to die nobly. What did you think that would accomplish?"
            a "Saving your people. They got away. That's all that mattered."
            selene "You don't get to die yet. You owe me. You led them here. Now you work off the debt by fighting with us."
            a "...Thank you. For coming back."
            selene "Don't thank me. You're still on probation. But you proved something today."
            selene "You were willing to die to save people you don't know. People who don't trust you. That's not revenge. That's resistance."

            $ scenes["meeting_selene"]["casualties"] = 1
            $ reputation["resistance"] += 5
            $ scenes["meeting_selene"]["emp_score"] += 2
            $ log_line("act2_meeting_selene", "result=win casualties=1 trust+3 rep+5 emp+2")

            jump crisis_resolution_success

        "Argue with Selene - defend yourself, deflect blame":
            $ scenes["meeting_selene"]["argued"] = True
            $ scenes["meeting_selene"]["selene_trust"] -= 2
            $ log_line("act2_meeting_selene", "choice=argue trust-2")

            a "We didn't know! How were we supposed to know they tracked their own weapons?"
            selene "By checking! By being careful! By not bringing Echelon gear to a resistance meeting!"
            a "We needed weapons! We didn't have a choice!"
            selene "Everyone has a choice! You chose wrong and now my people pay for it!"
            l "This isn't helping! We need to—"
            a "I'm not taking blame for Echelon's tactics! They're the ones attacking!"
            selene "Because you LED THEM HERE!"

            resistance_fighter "(screaming) Medic! I'm hit!"

            selene "Get out. NOW. Before more of my people die because of you."
            a "We can help—"
            selene "You've DONE enough! Leave! If I see you again I'll shoot you myself!"

            "Fleeing. Leaving them to fight. Leaving them to die. Because I argued instead of helped. Because Glass's instincts took over. Defend. Deflect. Never admit. And people died."
            "[ob] Debrief note: I chose ego under fire. Unacceptable."
            "[emp] And they bled for it."

            $ scenes["meeting_selene"]["casualties"] = 5
            $ reputation["resistance"] -= 10
            $ scenes["meeting_selene"]["alliance_formed"] = False
            $ scenes["meeting_selene"]["emp_score"] -= 2
            $ scenes["meeting_selene"]["ob_score"]  -= 2
            $ log_line("act2_meeting_selene", "result=fail casualties=5 rep-10 emp-2 ob-2")

            jump crisis_resolution_failure


# =======================================================
# CRISIS 2: Vex's Favor
# =======================================================

label crisis_vex_favor:

    "Device. Beeping. Mine. Urgent message. Can't ignore it. Not now. Vex."
    "[ob] Priority collision: alliance vs. debt."

    selene "You're answering messages during our meeting?"
    a "I'm sorry. This might be important. Give me one second."

    athought "Vex. The favor I owe. Being called in right now. During the meeting. Perfect fucking timing."

    selene "Problem?"
    a "...Yes. The weapons dealer I got our gear from. I owe them a favor. They're calling it in now. Echelon's raiding their workshop."
    selene "And you're telling me this because?"
    a "Because I gave my word. They helped us when we had nothing. Now they need help and I owe them."

    selene "So you owe a weapons dealer. And right now, during our meeting, you want to go help them."
    a "I don't want to. But I gave my word. That has to mean something."
    selene "It means you're easily distracted. It means when things matter, you'll run off chasing personal debts instead of focusing on the mission."
    l "That's not fair. He made a promise. He's honoring it. That shows integrity."
    selene "Or it shows poor judgment. Owing favors to dealers. Making promises you can't keep. That's how you get killed down here."

    menu:
        "Vex needs help now. Selene needs answer now. Can't do both."
        "Help Vex - honor the debt you owe":
            $ scenes["meeting_selene"]["helped_vex"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            $ scenes["meeting_selene"]["emp_score"] += 1
            $ log_line("act2_meeting_selene", "choice=help_vex trust+1 emp+1")

            scene bg_sector7_market with fade

            "Running. Sector 7. Vex's workshop ahead. Smoke rising. Gunfire. Echelon raid in progress. We're not too late. Not yet."
            "[ob] Entry angles: right side blind; left has overlapping fields."

            "There. Workshop. Echelon forces. Six of them. Tearing the place apart. Vex behind cover. Wounded. Bleeding. Trapped."

            a "(whisper) Six soldiers. Vex is hurt. We need to hit fast and hard."
            l "Agreed. I'll take left flank. You take right. Signal when ready."
            a "Ready. Three. Two. One. Now."

            "Move. Fire. Cover. Two soldiers down before they know we're there. Four remaining. Reacting. Professional. Dangerous. But we're faster."

            vex "(pained) Took your time."
            a "You're welcome. Can you move?"
            vex "Not fast. They got me good. Twice. Shoulder and leg."
            l "We need to evacuate. More will come."

            a "What happened? Why the raid?"
            vex "Someone tipped them off. Told them I was selling to resistance. Decided to make an example."
            vex "Would've worked too if you hadn't shown. Guess that favor paid off."
            a "You helped us. We help you. That's how it works."

            "Workshop exploding. Echelon destroying evidence. Everything Vex built. Gone. But Vex is alive. That's what matters."

            scene bg_sector6_ruins with fade

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
            $ inventory["debts_owed"].remove("vex")
            $ log_line("act2_meeting_selene", "result=alliance trust+1 rep+3 vex_in")

            jump crisis_resolution_success

        "Stay with Selene - alliance takes priority":
            $ scenes["meeting_selene"]["abandoned_vex"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ log_line("act2_meeting_selene", "choice=stay_with_selene trust+2 ob+1")

            "Vex survived. Barely. Lost everything. And now hates me. I broke my word. Chose the mission over the debt. Was it right? I don't know. But it's done."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 4
            $ characters["vex"]["trust"] = -5
            $ characters["vex"]["burned_bridge"] = True
            $ inventory["debts_owed"].remove("vex")
            $ log_line("act2_meeting_selene", "result=alliance rep+4 vex_bridge_burned")

            jump crisis_resolution_success


# =======================================================
# CRISIS 3: Kelvin the Mole
# =======================================================

label crisis_kelvin_mole:

    "Movement. Someone approaching. Confident. Not combat. Casual. Familiar. Wait. I know that walk."

    kelvin "Well well. Glass and the perfect soldier. Never thought I'd see you here."

    a "Kelvin. What are you doing here?"
    kelvin "Same thing as you. Meeting Selene. Delivering information."

    selene "Who is this?"
    a "Smuggler. Gave us work a week ago. Shouldn't know about this meeting."
    selene "Then how—"
    kelvin "(laughs) Because I set it up. Well, me and my Echelon handlers. Nice little trap. You all walked right in."

    "Mole. Kelvin works for Echelon. The smuggling job. The package. It was all surveillance."
    "[ob] If he’s here, outer ring’s netted. Time window measured in seconds."

    kelvin "I'd save the ammunition. You're surrounded. Echelon strike team. Twenty strong. Positioned around this entire block."
    kelvin "I've been feeding them intel for months..."
    kelvin "(to Aeron) And you helped. That delivery you made? Tracker inside."

    athought "The package. I delivered it. Helped them. Didn't even know."

    kelvin "So here's how this ends. You all surrender... Or I press this—"

    menu:
        "Kelvin's a mole. Finger on trigger. Twenty Echelon soldiers waiting. What do we do?"
        "Rush Kelvin - prevent him from signaling":
            $ scenes["meeting_selene"]["rushed_kelvin"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ log_line("act2_meeting_selene", "choice=rush_kelvin trust+2 ob+1")

            "Lunge. Kelvin's hand moving. Button pressing. Too slow. Too late. Signal going—"
            "Gunshot. Lyra. Perfect shot. Device destroyed. Kelvin's hand mangled. Signal not sent."

            selene "Move! Evacuation plan Delta! Now!"

            "Underground tunnels. Escape routes. Old smuggling paths. We got lucky. Barely."

            selene "You acted fast. Stopped the signal. Saved everyone."
            a "When I found out, I stopped him. Actions matter more than words."

            selene "...Fair. You're in. Probation. But you're in. Don't make me regret it."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 3
            $ characters["smuggler_kelvin"]["exposed"] = True
            $ characters["smuggler_kelvin"]["trust"] = -10
            $ log_line("act2_meeting_selene", "result=alliance rep+3 kelvin_exposed")

            jump crisis_resolution_success

        "Negotiate - try to talk Kelvin down":
            $ scenes["meeting_selene"]["negotiated_kelvin"] = True
            $ log_line("act2_meeting_selene", "choice=negotiate_kelvin")

            "Gunshot. Kelvin drops. Dead before he hits ground. Selene's sniper never trusted negotiation."

            selene "Talking doesn't work on traitors. Only bullets. Remember that."
            a "You could have told me you had a sniper ready."
            selene "Wanted to see if you'd waste time. You did. That's a weakness."
            selene "But you tried. That shows you're not like him. One pass. Don't waste it."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 1
            $ characters["smuggler_kelvin"]["dead"] = True
            $ log_line("act2_meeting_selene", "result=alliance rep+1 kelvin_dead")

            jump crisis_resolution_success

        "Kill Kelvin yourself - prove you're not like him":
            $ scenes["meeting_selene"]["killed_kelvin"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ log_line("act2_meeting_selene", "choice=kill_kelvin trust+3 ob+1")

            "Draw. Aim. Fire. Muscle memory. Glass training. Kill the threat. Fast. Clean. Efficient."

            "Dead before he hits ground. Device secured. Signal not sent. Threat neutralized. Glass would be proud. I feel sick."
            "[emp] Note the sickness. Keep it. It means I'm still human."

            selene "...Efficient."
            a "He was a threat. I ended him."
            selene "That was Glass. Not Aeron. You're dangerous. We need dangerous—but don't turn it on us."

            selene "You're in. Probation. Remember the line."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 4
            $ characters["smuggler_kelvin"]["dead"] = True
            $ scenes["meeting_selene"]["showed_glass"] = True
            $ log_line("act2_meeting_selene", "result=alliance rep+4 showed_glass")

            jump crisis_resolution_success


# =======================================================
# CRISIS 4: Sector 10 Rescue
# =======================================================

label crisis_sector10_rescue:

    "Footsteps. Running. Fast. Someone panicked. Young voice. Messenger. Bad news incoming."

    messenger "(gasping) Selene! Sector 10! Echelon raid! They're killing everyone!"

    selene "Sector 10? There's nothing left there. Just ruins and survivors."
    messenger "That's what they're raiding! Thirty people! They're executing them!"

    athought "The survivors. Hector's father. I promised to help. And now they're dying."
    "[emp] Promise on the line. Lives on the line."

    messenger "(to Aeron) One of them sent message! Said you promised to help! Said you owed them!"
    selene "You made promises to Sector 10 survivors? When?"
    a "Last week... I offered to help."
    selene "Everything's relevant. Personal debts become tactical liabilities. Case in point—right now."

    selene "Thirty survivors. Unknown Echelon strength. Going in is suicide."
    a "We have to try."
    selene "My people aren’t dying for your guilt."

    menu:
        "Thirty survivors being executed. Aeron's promise. Selene's calculation. What happens?"
        "Go alone - honor promise without risking Selene's people":
            $ scenes["meeting_selene"]["went_alone"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            $ scenes["meeting_selene"]["emp_score"] += 2
            $ log_line("act2_meeting_selene", "choice=sector10_go_alone trust+3 emp+2")

            l "Then I'm coming too."
            a "Lyra—"
            l "Together. Always together."
            selene "...You're serious."
            a "Yes."
            selene "Fine. I'm coming too. Five of mine. Not for your promise—for my people."

            scene bg_sector10_ruins with fade

            "Twelve Echelon soldiers. Thirty survivors lined up. Minutes from death."
            "[ob] Break the line at the command node; buy chaos for the run."

            selene "(whisper) Twelve soldiers. Seven of us."
            a "Bad odds are all we have."
            selene "Hit fast. Hit hard."

            "Attack. Three down on entry. Nine left. Survivors scatter. Some hit. Some escape."
            "Last Echelon falls. Twenty-two made it. Eight died. Count the living."

            selene "Twenty-two saved. Could have been worse."
            a "Could have been better."
            selene "Could have been zero if you hadn't kept your word... Welcome to the resistance. You've earned it."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 8
            $ reputation["resistance"] += 5
            $ characters["hector_father"]["trust"] += 3
            $ stats["people_saved"] += 22
            $ log_line("act2_meeting_selene", "result=alliance saved=22 casualties=8 rep+5")

            jump crisis_resolution_success

        "Convince Selene - argue for rescue mission":
            $ scenes["meeting_selene"]["convinced_selene"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            $ log_line("act2_meeting_selene", "choice=sector10_convince trust+1")

            a "We have to go. Not just for my promise. For what it represents..."
            selene "...Dammit. You're right. We go—smart, not suicidal."

            scene bg_sector10_ruins with fade

            "We make noise. They bite. Selene extracts. Twenty-five out; five dead before arrival."

            selene "(comms) Extraction complete! Twenty-five out! Disengage!"
            a "(comms) Copy! Moving! Cover us!"

            "Retreat under cover. Together. This is how it looks."

            selene "Twenty-five saved. Better than I expected... Welcome to the resistance."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 5
            $ reputation["resistance"] += 3
            $ characters["hector_father"]["trust"] += 2
            $ stats["people_saved"] += 25
            $ log_line("act2_meeting_selene", "result=alliance saved=25 casualties=5 rep+3")

            jump crisis_resolution_success

        "Refuse - alliance more important than promise":
            $ scenes["meeting_selene"]["refused_rescue"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ scenes["meeting_selene"]["emp_score"] -= 1
            $ log_line("act2_meeting_selene", "choice=sector10_refuse trust+2 ob+1 emp-1")

            "Thirty dead. Hector's father among them. I broke my word. Chose alliance over promise. Was it right? I don't know. But it's done."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["broke_promise"] = True
            $ reputation["resistance"] += 4
            $ characters["hector_father"]["trust"] = -10
            $ characters["hector_father"]["dead"] = True
            $ stats["people_killed"] += 30
            $ log_line("act2_meeting_selene", "result=alliance casualties=30 rep+4 hf_dead")

            jump crisis_resolution_success


# =======================================================
# CRISIS 5: Debt Collector Returns
# =======================================================

label crisis_debt_collector:

    "Footsteps. Angry. Aggressive. Man approaching. Armed. I know him. The debt collector. From the vendor situation. Fuck."

    debt_collector "There you are. Been looking for you."
    a "Let him go."
    debt_collector "(throws Dren down) You vouched. That means his debt became yours. 300 scrip."

    selene "Friend of yours?"
    a "Vendor I helped. Week ago. I vouched."
    selene "And he didn't pay."
    a "Apparently not."

    dren "(coughing) I tried!"
    debt_collector "300 scrip. Now. Or I take payment in blood."

    menu:
        "300 scrip owed. Dren's failure. Aeron's voucher. Debt collector waiting."
        "Pay the debt - 300 scrip" if inventory["scrip"] >= 300:
            $ scenes["meeting_selene"]["paid_debt"] = True
            $ inventory["scrip"] -= 300
            $ scenes["meeting_selene"]["selene_trust"] += 2
            $ scenes["meeting_selene"]["emp_score"] += 1
            $ log_line("act2_meeting_selene", "choice=pay_debt scrip-300 trust+2 emp+1")

            a "Fine. 300 scrip. Here."
            debt_collector "Smart."

            dren "Thank you. I'm sorry."
            a "Don't borrow what you can't pay back."

            selene "Generous. Stupid, but generous."
            a "I keep my responsibilities."
            selene "...I respect that."

            $ characters["dren"]["trust"] += 3
            $ characters["dren"]["debt_paid"] = True

            jump crisis_resolution_success

        "Negotiate - offer alternative payment":
            $ scenes["meeting_selene"]["negotiated_debt"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ log_line("act2_meeting_selene", "choice=negotiate_debt trust+1 ob+1")

            a "I don't have 300 scrip. But I can offer intel."
            debt_collector "Prove it."
            a "Supply convoy. Sector 8. Thursday dawn. Light guard."

            debt_collector "That's real. Debt cleared. Bring more like that."

            selene "(quiet) Be careful. Information is a weapon."
            a "Used right, it funds us."

            $ characters["dren"]["trust"] += 2
            $ scenes["meeting_selene"]["gave_intel_to_collector"] = True

            jump crisis_resolution_success

        "Fight the debt collector - refuse to pay":
            $ scenes["meeting_selene"]["fought_collector"] = True
            $ log_line("act2_meeting_selene", "choice=fight_collector")

            "Draw. Fast. Brutal. He’s down, wounded, fleeing. Threat ended. For now."

            dren "Now he'll come back with more."
            a "Then run."

            selene "Cold. You broke your word."
            a "I gave him a chance. He wasted it."

            $ characters["dren"]["trust"] = -5
            $ characters["dren"]["abandoned"] = True
            $ reputation["unders"] -= 2

            jump crisis_resolution_success

        "Let Dren pay - step aside, let collector take him":
            $ scenes["meeting_selene"]["abandoned_dren"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            $ scenes["meeting_selene"]["emp_score"] -= 1
            $ log_line("act2_meeting_selene", "choice=let_dren_pay trust+1 emp-1")

            "Dren screaming. Beaten. Dragged away. I don't watch. I know what happens to people who don't pay debts down here."
            "[emp] Silence is a kind of consent. I hear it anyway."

            $ characters["dren"]["trust"] = -10
            $ characters["dren"]["beaten"] = True
            $ reputation["unders"] -= 1
            $ scenes["meeting_selene"]["showed_coldness"] = True

            jump crisis_resolution_success


# =======================================================
# CRISIS 6: Kren's Warning
# =======================================================

label crisis_kren_warning:

    "Running. Fast. Desperate. Someone coming. Kren. The vendor I worked for."

    kren "(gasping) Aeron! ...Echelon patrol... asked about you... I got away... barely. They're coming. Minutes."

    selene "You led them here?"
    kren "I tried to warn you!"

    athought "Kren's wounded. Can't run. Liability. But he came to warn us. That loyalty means something."

    menu:
        "Echelon patrol incoming. Five minutes. Kren wounded. What do we do?"
        "Evacuate with Kren - save him despite cost":
            $ scenes["meeting_selene"]["saved_kren"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 2
            $ scenes["meeting_selene"]["emp_score"] += 1
            $ log_line("act2_meeting_selene", "choice=save_kren trust+2 emp+1")

            a "We take him. We don't leave him."
            selene "He'll slow us."
            a "Then we move slower."

            "Underground. Engines above. We made it. Barely."

            kren "Thank you. I won't forget this."
            selene "You value your contacts. Good leadership. Welcome to the resistance."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 3
            $ characters["kren"]["trust"] += 5
            $ characters["kren"]["life_debt"] = True

            jump crisis_resolution_success

        "Leave Kren - evacuate fast without him":
            $ scenes["meeting_selene"]["abandoned_kren"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 1
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ scenes["meeting_selene"]["emp_score"] -= 1
            $ log_line("act2_meeting_selene", "choice=leave_kren trust+1 ob+1 emp-1")

            "Underground. Safe. Above, Kren screaming. Executed. He warned us. We abandoned him."

            selene "Clean escape. Hard call—but good."
            a "Kren died."
            selene "We lived."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ reputation["resistance"] += 2
            $ characters["kren"]["dead"] = True
            $ reputation["unders"] -= 2
            $ scenes["meeting_selene"]["showed_coldness"] = True

            jump crisis_resolution_success

        "Fight at the location - defend instead of run":
            $ scenes["meeting_selene"]["fought_at_location"] = True
            $ log_line("act2_meeting_selene", "choice=fight_here")

            "They’re here. Twenty soldiers. We’re seven. Bad math. We bleed for it."
            "Kren dies. Two resistance down. Three wounded. Disaster. Because I was stubborn."

            selene "Three dead. Three wounded. For pride?"
            a "I thought—"
            selene "You didn’t think. You Glassed."

            $ scenes["meeting_selene"]["alliance_formed"] = False
            $ scenes["meeting_selene"]["casualties"] = 5
            $ reputation["resistance"] -= 5
            $ characters["kren"]["dead"] = True

            jump crisis_resolution_failure


# =======================================================
# CRISIS 7: Noelle's Algorithm (Default Fallback)
# =======================================================

label crisis_noelle_algorithm:

    "Device. Alert. Noelle. Analysis complete. Timing suspicious. What did she find?"

    a "(reading) Noelle's algorithm shows multiple Echelon strikes in twenty minutes. Including here."
    selene "How do I know this isn't false intel?"
    a "Her predictions are solid. 89 percent. If she says evacuate, we evacuate."
    l "If she's right and we stay, we die. If she's wrong and we run, we're inconvenienced. The math is clear."
    "[ob] Take the low-cost branch. Live to verify."

    menu:
        "Trust Noelle's data or stay?"
        "Trust Noelle - evacuate immediately":
            $ scenes["meeting_selene"]["trusted_noelle"] = True
            $ scenes["meeting_selene"]["selene_trust"] += 3
            $ scenes["meeting_selene"]["ob_score"]  += 1
            $ log_line("act2_meeting_selene", "choice=trust_noelle trust+3 ob+1")

            "Evacuation. Old subway. Nineteen. Eighteen. Seventeen."
            "Zero. Explosions above. Four locations. Ours included. We’d be dead if we stayed."

            selene "(reading) Three cells didn't evacuate. Gone. We're the only ones who made it out."
            a "Because we trusted Noelle."
            selene "Because you convinced me to. Welcome to the resistance. I want to meet her."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 0
            $ reputation["resistance"] += 5
            $ characters["noelle"]["trust"] += 3
            $ characters["noelle"]["resistance_value_proven"] = True

            jump crisis_resolution_success

        "Ignore warning - stay and verify":
            $ scenes["meeting_selene"]["ignored_noelle"] = True
            $ scenes["meeting_selene"]["selene_trust"] -= 1
            $ scenes["meeting_selene"]["ob_score"]  -= 1
            $ log_line("act2_meeting_selene", "choice=ignore_noelle trust-1 ob-1")

            "Waiting. Ten. Five. Nothing..."
            "EXPLOSION. Building collapses. Exactly on time."

            selene "(shouting) Defensive positions! Fight out!"

            "We escape, but bleed. Three down."

            selene "Your analyst was right. I didn’t listen."
            selene "...You're in. Bring her. I need people who are right when I’m wrong."

            $ scenes["meeting_selene"]["alliance_formed"] = True
            $ scenes["meeting_selene"]["casualties"] = 3
            $ reputation["resistance"] += 2
            $ characters["noelle"]["trust"] += 2

            jump crisis_resolution_success


# =======================================================
# CRISIS RESOLUTION - SUCCESS PATH
# =======================================================

label crisis_resolution_success:

    scene bg_sector6_ruins_aftermath with fade

    "Aftermath. Crisis resolved. Alliance forged. Not through words. Through action. Through fire. Through choice."
    "[emp] People alive. Names to add. [ob] Lessons logged; patterns updated."

    selene "We survived."
    a "We did more than survive. We proved we can work together."
    selene "Maybe. Either way, you're in."

    selene "Welcome to the resistance. Probation starts now. You fuck up, you're out. Betray us, you're dead. Clear?"
    a "(shakes hand) Clear."

    l "Both of us. We're a package."
    selene "Fine. Double asset or double liability. Time will tell."

    selene "(to resistance) These two are with us. Probation. Any problems, bring them to me."

    selene "Now we bleed Echelon instead. Together."
    a "Burn it all down."

    "Sun rising. New beginning. We're resistance now. No going back."

    $ scenes["meeting_selene"]["alliance_formed"] = True
    $ canon["resistance_joined"] = True
    $ canon["met_selene"] = True

    # Final trust gate
    $ selene_final_trust = scenes["meeting_selene"]["selene_trust"]

    if selene_final_trust >= 5:
        "Selene trusts us. Not fully, not yet. But enough to fight beside us."
    elif selene_final_trust >= 2:
        "Cautious probation. One mistake and we're out. But we're in. That's a start."
    else:
        "Useful tools. Disposable. We prove it every mission or we die. Understood."

    # Casualty reflection
    $ total_casualties = scenes["meeting_selene"].get("casualties", 0)

    if total_casualties == 0:
        "No casualties. Rare. Precious. Selene noticed."
    elif total_casualties <= 3:
        "[total_casualties] casualties. Not catastrophic. Not acceptable. We do better."
    else:
        "[total_casualties] casualties. Too many. Different cause, same result: blood on my hands. Make it mean something."

    selene "First mission briefing tomorrow. Dawn. Don't be late."
    a "We'll be there."
    selene "Good. Go find a bed. Tomorrow we start breaking Echelon."

    "Leaving. We came as fugitives. We leave forged. Still broken. But forged into something that might matter."
    l "We did it."
    a "That was the easy part."
    l "The hard part?"
    a "Everything next."
    l "Together."
    a "Together."

    "Act 2 complete. Fugitives to resistance. Hunted to hunters. The war begins."

    $ mark_scene("act2_meeting_selene", complete=True)
    $ log_line("act2_meeting_selene", f"exit success trust={selene_final_trust} casualties={total_casualties} OB/EMP end: emp={scenes['meeting_selene']['emp_score']} ob={scenes['meeting_selene']['ob_score']}")

    return


# =======================================================
# CRISIS RESOLUTION - FAILURE PATH
# =======================================================

label crisis_resolution_failure:

    scene bg_sector6_ruins_disaster with fade

    "Disaster. Too many mistakes. Too much Glass through the cracks. Selene's done with us."
    "[ob] After-action: ego spikes under stress, mission discipline collapses. [emp] People died for that spike."

    selene "Get out."
    a "Selene, wait—"
    selene "(cold) GET. OUT."

    "Leaving. Alliance destroyed. Alone again."

    l "(quiet) What do we do now?"
    a "...I don't know."

    $ scenes["meeting_selene"]["alliance_formed"] = False
    $ canon["resistance_joined"] = False
    $ reputation["resistance"] = -10

    $ log_line("act2_meeting_selene", "exit failure alliance_broken rep_resistance=-10")

    jump act2_finale_failure
