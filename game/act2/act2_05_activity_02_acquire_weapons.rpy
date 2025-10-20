# act2_activity_02_acquire_weapons.rpy


# =======================================================
# ACT 2 - Activity 2: Acquire Weapons
# =======================================================


define vex = Character("Vex", color="#9C27B0")
define guard = Character("Guard", color="#455A64")
define soldier = Character("Echelon Soldier", color="#1565C0")


label act2_activity_02_acquire_weapons:

    # Initialize activity-specific tracking
    $ scenes["activity2_weapons"] = {
        "method": None,
        "vex_relationship": "neutral",
        "echelon_patrol_encounter": False,
        "weapon_acquired": None
    }

    # VISUAL: Safe house. Aeron checking their complete lack of weapons.
    # LIGHTING: Afternoon. Gray light through window.
    # SOUND: City hum. Distant sirens. Tension.

    "{i}Day [player_state['days_remaining']]. Still unarmed. That needs to change.{/i}"
    
    # VISUAL: Aeron and Lyra both aware they're defenseless.
    a "{i}We've been lucky so far. Lucky doesn't last forever in the Unders.{/i}"

    l "We need weapons."
    a "I know."
    l "Not eventually. Now. Every hour we're unarmed is an hour we could die."
    a "I know. But where do we get them? We have no connections, limited money, and everyone wants us dead."
    l "Then we make connections. Or we take what we need."

    # VISUAL: Aeron considers. Multiple bad options.
    a "Zira mentioned black market dealers. People who sell to anyone with money."
    l "Do we have money?"
    
    # Check current resources
    $ current_scrip = inventory["scrip"]
    $ current_credits = inventory["credits"]
    
    a "We have [current_scrip] scrip and [current_credits] Aeries credits."
    
    if current_scrip >= 200:
        l "That might be enough. Depends on the dealer."
    elif current_scrip >= 100:
        l "That's... not much. We might need to negotiate."
    else:
        l "That's nowhere near enough. We'll need another option."

    a "Zira said there's someone named Vex. Black market weapons dealer. Reliable but expensive."
    l "Where do we find this Vex?"
    a "Lower Spans. Sector 7. Near where we swept."
    l "Of course it is. Everything leads back there."

    # TRANSITION: Journey to Sector 7. Black market district.
    # VISUAL: Moving through crowds. Neon signs. Steam. Grime. Life surviving.
    # LIGHTING: Artificial evening. Red and blue neon. Shadows deep.
    # SOUND: Deals being made. Whispers. Tension.

    scene bg_sector7_market with fade

    "{i}Sector 7. Black market territory. Where laws are suggestions and violence is currency. Perfect place to buy death.{/i}"

    # VISUAL: Market stalls. Legitimate fronts hiding illegal business.
    # People watching. Evaluating. Predators recognizing prey.

    l "(quiet) Everyone's watching us."
    a "We stand out. New faces, desperate energy. They can smell it."
    l "Where's Vex supposed to be?"
    a "Back alley. Three streets down. Blue door with red X."
    l "Subtle."
    a "Down here, subtle gets you ignored. Ignored means no business."

    # VISUAL: Find the door. Blue paint peeling. Red X spray-painted. Guard outside.
    # GUARD: Large. Armed. Bored. Professional.

    "{i}There. Blue door, red X, armed guard. This is the place.{/i}"

    # VISUAL: Approach. Guard notices. Hand moves to weapon. Casual threat.
    guard "Private property. Move along."
    a "We're here to see Vex."
    guard "Vex doesn't see walk-ins."
    a "Tell Vex we have credits and we need hardware. That should get their attention."
    guard "(evaluates them) Wait here. Don't touch anything."

    # VISUAL: Guard disappears inside. Long wait. Tension building.
    # SOUND: Muffled voices. Negotiation. Decision being made.

    l "What if they don't let us in?"
    a "Then we find another way. There's always another way."
    l "Not always a good way though."
    a "No. Not always."

    # VISUAL: Guard returns. Gestures inside. Permission granted.
    guard "Vex will see you. Try anything stupid and you don't leave."
    a "Understood."

    # VISUAL: Inside. Workshop. Weapons everywhere. Tools. Parts. Organized chaos.
    # LIGHTING: Harsh fluorescent. Work lights. Shadows in corners.
    # SOUND: Metal on metal. Ventilation. Quiet music. Focus.

    scene bg_vex_workshop with fade

    "{i}Workshop. Weapons covering every surface. Pistols, rifles, knives, explosives. Everything you need to kill efficiently.{/i}"

    # VISUAL: VEX at workbench. 30s. Androgynous. Covered in tattoos. Precise movements.
    # Working on disassembled pistol. Doesn't look up immediately.

    vex "New customers. How exciting."
    vex "(still working) You have about sixty seconds to tell me why I should care."

    # VISUAL: Aeron steps forward. Direct. Honest.
    a "We need weapons. Pistols preferably. Knives if that's all you have."
    vex "Everyone needs weapons. That's not interesting. Why should I sell to you specifically?"
    a "Because we have money and you're in business."
    vex "(finally looks up) Simple. Transactional. I appreciate that."
    vex "(studies them) You're new to the Unders. Clothes are wrong, posture's wrong, eyes are wrong."
    vex "Let me guess. Refugees from above? Running from something? Someone?"

    # VISUAL: Lyra tenses. Aeron stays calm.
    a "Does it matter?"
    vex "To my prices? No. To my safety? Maybe. I don't sell to Echelon plants or people about to get raided."
    a "We're not Echelon. Not anymore. And we're trying very hard not to get raided."
    vex "(grins) Not anymore. Interesting word choice. Defectors?"
    a "Something like that."
    vex "Even more interesting. Echelon doesn't let people leave. Which means you're either very brave or very stupid."
    vex "Probably both."

    # VISUAL: Vex stands. Wipes hands. Approaches them. Evaluating.
    vex "Alright. Let's talk business. What are you looking for specifically?"
    l "Two pistols. Reliable. Accurate. Nothing fancy."
    vex "Standard sidearms. I can do that. Question is, can you afford it?"

    # VISUAL: Vex pulls out datapad. Shows prices. Expensive but not impossible.
    vex "Two pistols, hundred rounds each, maintenance kit. 400 scrip. Non-negotiable."
    
    # Check if they can afford it
    if current_scrip >= 400:
        $ can_afford_full = True
        a "{i}400 scrip. We have [current_scrip]. We can afford it.{/i}"
    elif current_scrip >= 200:
        $ can_afford_full = False
        a "{i}400 scrip. We only have [current_scrip]. Not enough.{/i}"
    else:
        $ can_afford_full = False
        a "{i}400 scrip. We have [current_scrip]. Nowhere close.{/i}"

    # VISUAL: Consider options. Multiple paths forward.
    menu:
        "Vex waits. Professional patience. Time to decide."
        
        "Buy the weapons with scrip (400 scrip)" if can_afford_full:
            $ scenes["activity2_weapons"]["method"] = "bought"
            $ inventory["scrip"] -= 400
            $ inventory["weapons"].append("pistol_standard")
            $ inventory["weapons"].append("pistol_standard")
            $ scenes["activity2_weapons"]["weapon_acquired"] = "two_pistols"
            $ characters["vex"] = {"met": True, "trust": 1, "business": "clean"}
            
            a "400 scrip. Done. We'll take them."
            vex "(impressed) Direct. I like that. Most people haggle for twenty minutes."
            vex "Respect for your time and mine. I appreciate it."
            
            # VISUAL: Vex moves to cabinet. Pulls out two pistols. Clean. Maintained. Professional.
            vex "Two standard sidearms. Unregistered, untraceable, reliable. Maintenance kit included."
            vex "Ammo's already loaded. Extra magazines in the case."
            
            # VISUAL: Hands them over. Professional transaction.
            a "(takes them) Thank you."
            vex "Thank your money, not me. Business is business."
            vex "But since you paid clean and didn't waste my time, I'll give you some advice."
            vex "Don't pull those unless you're ready to use them. Down here, showing weakness gets you killed faster than showing nothing."
            a "Noted."
            vex "Good. Now get out. I have actual work to do."
            
            $ scenes["activity2_weapons"]["vex_relationship"] = "professional"
            
        "Negotiate - offer Aeries credits + scrip":
            $ scenes["activity2_weapons"]["method"] = "negotiated"
            
            a "We don't have 400 scrip. We have [current_scrip] scrip and [current_credits] Aeries credits."
            vex "(laughs) Aeries credits. Those are basically worthless down here."
            a "Not worthless. Just harder to spend. You must have connections who'd take them."
            vex "I do. But the exchange rate is terrible. Your [current_credits] credits are worth maybe 50 scrip to me."
            
            # Calculate if combined it's enough
            $ combined_value = current_scrip + 50
            
            if combined_value >= 400:
                vex "Together that's [combined_value] scrip equivalent. Close enough. I'll take it."
                $ inventory["scrip"] = 0
                $ inventory["credits"] = 0
                $ inventory["weapons"].append("pistol_standard")
                $ inventory["weapons"].append("pistol_standard")
                $ scenes["activity2_weapons"]["weapon_acquired"] = "two_pistols"
                $ characters["vex"] = {"met": True, "trust": 1, "business": "negotiated"}
                $ scenes["activity2_weapons"]["vex_relationship"] = "fair_deal"
                
                vex "Two pistols. Same deal. Unregistered, maintained, reliable."
                a "Thank you."
                vex "Don't thank me. You paid fair. That's all that matters."
                
            else:
                vex "Together that's [combined_value] scrip equivalent. Still short."
                vex "I can give you one pistol and a knife for that. Take it or leave it."
                
                menu:
                    "One pistol and a knife. Not ideal but better than nothing."
                    
                    "Accept the deal":
                        $ inventory["scrip"] = 0
                        $ inventory["credits"] = 0
                        $ inventory["weapons"].append("pistol_standard")
                        $ inventory["weapons"].append("knife_combat")
                        $ scenes["activity2_weapons"]["weapon_acquired"] = "pistol_and_knife"
                        $ characters["vex"] = {"met": True, "trust": 1, "business": "compromised"}
                        $ scenes["activity2_weapons"]["vex_relationship"] = "acceptable"
                        
                        a "Deal. We'll take it."
                        vex "Smart. One gun is better than no guns."
                        
                        # VISUAL: Hands over pistol and combat knife.
                        vex "Pistol for whoever shoots better. Knife for backup. Don't die stupidly."
                        a "We'll try not to."
                        
                    "Refuse - look for other options":
                        a "Not good enough. We need two pistols."
                        vex "Then come back when you have real money. I'm not a charity."
                        vex "Door's that way. Don't let it hit you on the way out."
                        
                        "{i}Deal's off. We leave empty-handed. Need another plan.{/i}"
                        
                        jump activity2_alternate_methods
        
        "Offer to work off the debt - trade favor for weapons":
            $ scenes["activity2_weapons"]["method"] = "favor"
            
            a "We don't have enough scrip. But we can work for it. Trade a favor for the weapons."
            vex "(interested) A favor. From defectors. That could be valuable."
            vex "What kind of work are you offering?"
            a "Whatever you need. Delivery, protection, information. We're capable."
            vex "You're also wanted. That makes you a liability."
            a "Or an asset. We know Echelon. We know how they think and operate. That's worth something."
            
            # VISUAL: Vex considers. Calculating risk vs reward.
            vex "...Alright. I'll bite. Here's the deal."
            vex "I give you two pistols now. You owe me a favor. One job, no questions, completed when I call it in."
            vex "You refuse or fuck it up, and I spread the word you're Echelon plants. Your reputation in the Unders dies instantly."
            a "That's harsh."
            vex "That's insurance. I'm taking a risk on you. You're covering my risk with your reputation."
            
            menu:
                "Accept the favor deal or refuse?"
                
                "Accept - owe Vex a favor":
                    $ inventory["debts_owed"].append("vex")
                    $ inventory["weapons"].append("pistol_standard")
                    $ inventory["weapons"].append("pistol_standard")
                    $ scenes["activity2_weapons"]["weapon_acquired"] = "two_pistols"
                    $ characters["vex"] = {"met": True, "trust": 2, "business": "favor_owed", "leverage": True}
                    $ scenes["activity2_weapons"]["vex_relationship"] = "indebted"
                    
                    a "Deal. One favor. We'll honor it."
                    vex "(grins) Smart. Desperate, but smart. I like desperate people. They're motivated."
                    
                    # VISUAL: Hands over two pistols. Same quality as buying.
                    vex "Two pistols. Maintained, reliable. When I call, you answer. Clear?"
                    a "Clear."
                    vex "Good. Now get out. You're making my other customers nervous."
                    
                "Refuse - too risky":
                    a "No deal. A blank favor is too dangerous. We'll find another way."
                    vex "(shrugs) Your choice. Door's that way. Good luck finding weapons without money or leverage."
                    
                    "{i}Deal refused. We leave empty-handed. Need another option.{/i}"
                    
                    jump activity2_alternate_methods
        
        "Leave - find another way" if not can_afford_full:
            "{i}Can't afford it. Can't risk the favor. Time to find another option.{/i}"
            
            jump activity2_alternate_methods

    # SUCCESS PATH - Got weapons from Vex
    if scenes["activity2_weapons"]["weapon_acquired"] != None:
        
        # VISUAL: Outside Vex's workshop. Armed now. Changed.
        scene bg_sector7_market with fade
        
        "{i}Outside. Armed. Finally. The weight of weapons is strange. Comforting and terrifying.{/i}"
        
        # VISUAL: Both checking weapons. Lyra more comfortable than Aeron.
        l "(checks pistol) Good quality. Well maintained. Vex knows their business."
        a "(checks his weapon) Yeah. Feels strange. Glass always had weapons. Aeron Rylan hasn't carried one in weeks."
        l "Glass is dead. Aeron Rylan is armed. There's a difference."
        a "Is there? Or am I just Glass with a new name?"
        l "That's up to you. A gun doesn't make you Glass. What you do with it does."
        
        # VISUAL: Aeron considers. Holsters weapon. Accepts reality.
        a "Then I'll do something different. Use it to protect instead of kill."
        l "Noble. We'll see how long that lasts when someone's trying to kill us."
        a "Guess we'll find out."
        
        # Update activity tracking
        $ scenes["act2_activity"]["weapons"] = True
        
        # Show what they got
        if scenes["activity2_weapons"]["weapon_acquired"] == "two_pistols":
            "{i}Two pistols. Both armed. Both ready. One step closer to surviving this.{/i}"
        elif scenes["activity2_weapons"]["weapon_acquired"] == "pistol_and_knife":
            "{i}One pistol, one knife. Not ideal, but enough. Better than nothing.{/i}"
        
        # TRANSITION: Return to safe house
        jump activity2_return_hub

# ALTERNATE PATH - Couldn't get weapons from Vex
label activity2_alternate_methods:
    
    # VISUAL: Outside Vex's place. No weapons. Need another plan.
    scene bg_sector7_market with fade
    
    "{i}No weapons from Vex. Either can't afford it or won't risk the favor. Need another option.{/i}"
    
    l "So what now?"
    a "We find another way. There's always another way."
    l "Like what? Steal them? Make them ourselves?"
    a "...Maybe. Or we take them from someone who won't miss them."
    l "You mean Echelon."
    a "I mean anyone who has them and won't sell them."
    
    # VISUAL: Consider options. Both risky. Both desperate.
    menu:
        "What's the plan?"
        
        "Ambush Echelon patrol - steal their weapons":
            $ scenes["activity2_weapons"]["method"] = "stolen_echelon"
            $ scenes["activity2_weapons"]["echelon_patrol_encounter"] = True
            
            a "Echelon patrols come through here. Small teams, two or three soldiers. We ambush them."
            l "That's insane. We're unarmed and they're trained."
            a "We're trained too. We know their tactics, their patrol routes, their weaknesses. We can do this."
            l "And if we're wrong? If we fail?"
            a "Then we die. But we were going to die unarmed eventually anyway. At least this way we go down fighting."
            
            # VISUAL: Lyra considers. Nods. Grim acceptance.
            l "...Alright. Let's do it. How?"
            a "We wait. Watch patrol patterns. Find a vulnerable moment. Strike fast, take weapons, disappear."
            l "Simple plan. Lots of ways it can go wrong."
            a "All good plans are simple. It's the execution that matters."
            
            # VISUAL: Find hiding spot. Watch patrols. Waiting. Hunting.
            "{i}We find a spot. Alley overlooking patrol route. Wait. Watch. Two hours pass. Then three. Patience is survival.{/i}"
            
            # VISUAL: Patrol appears. Two soldiers. Standard loadout. Routine sweep.
            "{i}There. Two soldiers. Standard patrol. Bored, not expecting trouble. Perfect.{/i}"
            
            a "(whisper) Two targets. You take left, I take right. Fast and silent. No gunfire if possible."
            l "What do we have for weapons?"
            a "Rocks. Surprise. Desperation. That'll have to be enough."
            l "Great plan."
            a "You have a better one?"
            l "...No. Let's do this."
            
            # VISUAL: Ambush. Fast. Brutal. Desperate.
            # AERON drops from above. Tackles soldier. Struggle. Hand over mouth. Choke hold.
            # LYRA blindsides second soldier. Pipe from alley. Hit. Down. Unconscious.
            
            "{i}Move. Drop. Tackle. Soldier goes down hard. Struggling, trying to shout. Hand over mouth. Choke hold. He fights. I hold. Ten seconds. Twenty. Goes limp.{/i}"
            "{i}Lyra's soldier down. Unconscious. Bleeding from head wound. Still breathing. That's enough mercy for now.{/i}"
            
            # VISUAL: Strip weapons fast. Pistols, ammo, comms devices. Take everything useful.
            a "(fast) Weapons. Ammo. Comms. Take it all. We have maybe two minutes before backup."
            l "(stripping gear) Got it. Pistols, rifles, magazines. This is enough."
            a "Then move. Now. Before they wake up or backup arrives."
            
            # VISUAL: Flee. Fast. Deep into alleys. Losing pursuit. Heart pounding.
            "{i}Run. Alleys. Twisting paths. Footsteps behind. Shouts. Pursuit. Keep moving. Don't stop. Don't look back.{/i}"
            
            # VISUAL: Finally stop. Deep in Unders. Lost them. Safe. For now.
            "{i}Stop. Finally. Deep enough. Lost them. Breathing hard. Hearts pounding. Alive. Armed.{/i}"
            
            l "(gasping) That was insane."
            a "(breathing hard) That was necessary."
            l "We just attacked Echelon soldiers. They'll escalate. Send more patrols. Hunt harder."
            a "They were already hunting us. Now we're just armed while they do it."
            
            # Add weapons and consequences
            $ inventory["weapons"].append("pistol_echelon")
            $ inventory["weapons"].append("pistol_echelon")
            $ inventory["weapons"].append("rifle_echelon")
            $ scenes["activity2_weapons"]["weapon_acquired"] = "echelon_gear"
            $ reputation["echelon"] -= 10
            $ player_state["echelon_alert"] += 2
            
            "{i}Echelon weapons. Two pistols, one rifle, full magazines. Stolen from the system that made us. Poetic.{/i}"
            
        "Scavenge - search ruins for abandoned weapons":
            $ scenes["activity2_weapons"]["method"] = "scavenged"
            
            a "The Purge destroyed whole sectors. Buildings collapsed, people fled. Weapons left behind."
            l "You want to scavenge Purge sites."
            a "I want to find what survivors left behind when they ran or died. Same thing."
            l "That's grim."
            a "We're living in grim. Might as well make use of it."
            
            # VISUAL: Journey to Sector 10 ruins. Searching. Grim work.
            "{i}Back to Sector 10. The graveyard. Searching rubble for weapons left by the dead. This is what we've become.{/i}"
            
            # VISUAL: Hours of searching. Rubble. Collapsed buildings. Bodies. Eventually find cache.
            "{i}Hours pass. Searching. Lifting rubble. Finding bodies. Finding nothing. Then finally, a cache. Hidden. Abandoned. Forgotten.{/i}"
            
            # VISUAL: Small weapons cache. Old. Maintained. Resistance supply.
            a "(finds it) Here. Hidden cache. Resistance supply dump probably."
            l "(examines) Two pistols. Old models but maintained. Ammo. Basic but functional."
            a "Functional is all we need. Take them. Leave the rest for whoever comes next."
            l "You're being generous with resistance supplies."
            a "We're joining the resistance. Eventually. Call it a loan."
            
            # Add scavenged weapons
            $ inventory["weapons"].append("pistol_old")
            $ inventory["weapons"].append("pistol_old")
            $ scenes["activity2_weapons"]["weapon_acquired"] = "scavenged_cache"
            
            "{i}Old pistols. Worn but maintained. Someone's backup plan. Now it's ours. Hope they don't need it anymore.{/i}"

    # Update activity completion
    $ scenes["act2_activity"]["weapons"] = True
    
    jump activity2_return_hub

# RETURN TO HUB
label activity2_return_hub:
    
    # VISUAL: Back at safe house. Evening. Armed now. Changed.
    scene bg_safe_house with fade
    
    "{i}Back. Safe house. Evening. Armed now. That changes everything.{/i}"
    
    # VISUAL: Both examining weapons. Testing weight. Checking function.
    a "{i}Weapons. Tools of death. Glass carried them without thinking. I carry them with purpose. That has to mean something.{/i}"
    
    l "How do you feel?"
    a "Armed. Prepared. Still terrified. But less helpless."
    l "That's progress."
    a "Is it? Or am I just better equipped to make the same mistakes?"
    l "Depends on what you do with them. Glass used weapons to kill. You're using them to survive. That's different."
    a "...Yeah. Different. I'll hold onto that."
    
    # Show acquisition summary
    if scenes["activity2_weapons"]["method"] == "bought":
        "{i}Bought weapons from Vex. Clean transaction. Professional. Expensive but simple.{/i}"
    elif scenes["activity2_weapons"]["method"] == "negotiated":
        "{i}Negotiated with Vex. Used every credit we had. Fair deal, both sides compromised.{/i}"
    elif scenes["activity2_weapons"]["method"] == "favor":
        "{i}Owe Vex a favor. One job, no questions. Dangerous leverage but necessary. We're armed and that's what matters.{/i}"
    elif scenes["activity2_weapons"]["method"] == "stolen_echelon":
        "{i}Stole from Echelon. Ambushed patrol, took their weapons. They'll hunt harder now but we're armed. Worth it.{/i}"
    elif scenes["activity2_weapons"]["method"] == "scavenged":
        "{i}Scavenged from ruins. Dead resistance fighters' backup cache. Borrowed from the fallen. Hope they'd approve.{/i}"
    
    # Relationship moment
    l "We're armed now. That's one more thing off the list."
    a "Six more to go. Then Selene. Then... everything else."
    l "One step at a time."
    a "One step at a time."
    
    # TRANSITION: Back to activity hub
    jump act2_activity_hub

    # canon_note: Activity 2 complete - acquired weapons through multiple possible paths
    # canon_note: Vex introduced - black market dealer, professional, multiple relationship states
    # canon_note: Purchase path: clean transaction, professional relationship (+1 trust)
    # canon_note: Negotiation path: compromise deal, fair business relationship
    # canon_note: Favor path: owe Vex one job (future subplot), Vex has leverage
    # canon_note: Echelon ambush path: stolen gear, increased alert (+2), reputation hit (-10)
    # canon_note: Scavenge path: old resistance cache, functional but worn
    # canon_note: Weapons added to inventory based on method chosen
    # canon_note: Scrip/credits spent appropriately based on path
    # canon_note: Sets up future: Vex favor can be called in Act 3, Echelon alert affects patrols
    # canon_note: Character growth: Aeron sees difference between Glass carrying weapons and his purpose
    # canon_note: Lyra support: grounds him, reminds him he's not Glass anymore

    jump act2_activity_hub