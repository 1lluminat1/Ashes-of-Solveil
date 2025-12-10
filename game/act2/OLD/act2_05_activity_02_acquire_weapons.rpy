# act2_activity_02_acquire_weapons.rpy


# =======================================================
# ACT 2 - Activity 2: Acquire Weapons
# Helpers-only + scene_flags usage. Scrip deltas shown.
# OB/EMP flavor lines are additive and non-destructive.
# =======================================================


#TODO migrate legacy weapons/currency dicts to new system


define vex = Character("Vex", color="#9C27B0")
define guard = Character("Guard", color="#455A64")
define soldier = Character("Echelon Soldier", color="#1565C0")
define contact = Character("Contact", color="#9E9E9E")


label act2_activity_02_acquire_weapons:

    # --- INIT & SNAPSHOT ---
    $ start_operation("op2B_weapons", note="Acquire Weapons (Vex / alternate methods)")
    $ mark_scene("act2_activity_02_weapons", "started")
    $ weapons_scrip_delta = 0  # positive = earned, negative = spent

    # VISUAL: Safe house. Check resources.
    "Day [player_state['days_remaining']]. Still unarmed. That needs to change."
    athought "We've been lucky so far. Lucky doesn't last forever in the Unders."

    l "We need weapons."
    a "I know."
    l "Not eventually. Now. Every hour we're unarmed is an hour we could die."
    a "I know. But where do we get them? We have no connections, limited money, and everyone wants us dead."
    l "Then we make connections. Or we take what we need."

    # Resource peek (read is OK)
    $ current_scrip = inventory.get("scrip", 0)
    $ current_credits = inventory.get("credits", 0)

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

    # TRANSITION → Sector 7
    scene bg_sector7_market with fade
    "Sector 7. Black market territory. Where laws are suggestions and violence is currency. Perfect place to buy death."

    l "(quiet) Everyone's watching us."
    a "We stand out. New faces, desperate energy. They can smell it."
    l "Where's Vex supposed to be?"
    a "Back alley. Three streets down. Blue door with red X."
    l "Subtle."
    a "Down here, subtle gets you ignored. Ignored means no business."

    "There. Blue door, red X, armed guard. This is the place."
    guard "Private property. Move along."
    a "We're here to see Vex."
    guard "Vex doesn't see walk-ins."
    a "Tell Vex we have credits and we need hardware. That should get their attention."
    guard "(evaluates them) Wait here. Don't touch anything."

    l "What if they don't let us in?"
    a "Then we find another way. There's always another way."
    l "Not always a good way though."
    a "No. Not always."

    guard "Vex will see you. Try anything stupid and you don't leave."
    a "Understood."

    scene bg_vex_workshop with fade
    "Workshop. Weapons covering every surface. Pistols, rifles, knives, explosives. Everything you need to kill efficiently."

    vex "New customers. How exciting."
    vex "(still working) You have about sixty seconds to tell me why I should care."
    a "We need weapons. Pistols preferably. Knives if that's all you have."
    vex "Everyone needs weapons. That's not interesting. Why should I sell to you specifically?"
    a "Because we have money and you're in business."
    vex "(finally looks up) Simple. Transactional. I appreciate that."
    vex "(studies them) You're new to the Unders. Clothes are wrong, posture's wrong, eyes are wrong."
    vex "Let me guess. Refugees from above? Running from something? Someone?"

    a "Does it matter?"
    vex "To my prices? No. To my safety? Maybe. I don't sell to Echelon plants or people about to get raided."
    a "We're not Echelon. Not anymore. And we're trying very hard not to get raided."
    vex "(grins) Not anymore. Interesting word choice. Defectors?"
    a "Something like that."
    vex "Even more interesting. Echelon doesn't let people leave. Which means you're either very brave or very stupid."
    vex "Probably both."

    vex "Alright. Let's talk business. What are you looking for specifically?"
    l "Two pistols. Reliable. Accurate. Nothing fancy."
    vex "Standard sidearms. I can do that. Question is, can you afford it?"

    vex "Two pistols, hundred rounds each, maintenance kit. 400 scrip. Non-negotiable."

    # Re-read balances in case they shifted since earlier scenes
    $ current_scrip = inventory.get("scrip", 0)
    $ current_credits = inventory.get("credits", 0)
    $ can_afford_full = current_scrip >= 400

    if can_afford_full:
        athought "400 scrip. We have [current_scrip]. We can afford it."
    elif current_scrip >= 200:
        athought "400 scrip. We only have [current_scrip]. Not enough."
    else:
        athought "400 scrip. We have [current_scrip]. Nowhere close."

    # OB/EMP one-liners
    if get_empathy_band() == "obedience":
        athought "Buy clean or leverage risk. Don’t linger."
    else:
        athought "We need tools to protect, not to become Glass again."

    menu:
        "Vex waits. Professional patience. Time to decide."
        "Buy the weapons with scrip (400 scrip)" if can_afford_full:
            $ mark_scene("act2_activity_02_weapons", "method_bought")
            $ weapons_scrip_delta = -400
            $ inventory["scrip"] = max(0, inventory.get("scrip", 0) + weapons_scrip_delta)
            $ add_item("weapons", "pistol_standard")
            $ add_item("weapons", "pistol_standard")
            $ mark_scene("act2_activity_02_weapons", "got_two_pistols")

            a "400 scrip. Done. We'll take them."
            vex "(impressed) Direct. I like that. Most people haggle for twenty minutes."
            vex "Respect for your time and mine. I appreciate it."
            vex "Two standard sidearms. Unregistered, untraceable, reliable. Maintenance kit included."
            # we don't have a helper for generic items; treat as note
            $ char_note("Lyra", "Bought two unregistered pistols from Vex (clean).")
            a "(takes them) Thank you."
            vex "Thank your money, not me. Business is business."
            vex "Don’t pull those unless you’re ready to use them. Down here, weakness kills faster than nothing."
            a "Noted."
            vex "Good. Now get out. I have actual work to do."

        "Negotiate — offer Aeries credits + scrip":
            $ mark_scene("act2_activity_02_weapons", "method_negotiated")
            a "We don't have 400 scrip. We have [current_scrip] scrip and [current_credits] Aeries credits."
            vex "(laughs) Aeries credits. Those are basically worthless down here."
            a "Not worthless. Just harder to spend. You must have connections who'd take them."
            vex "I do. But the exchange rate is terrible. Your [current_credits] credits are worth maybe 50 scrip to me."

            $ combined_value = current_scrip + 50
            if combined_value >= 400:
                $ weapons_scrip_delta = -current_scrip  # spend all scrip
                $ inventory["scrip"] = 0
                $ inventory["credits"] = 0
                $ add_item("weapons", "pistol_standard")
                $ add_item("weapons", "pistol_standard")
                $ mark_scene("act2_activity_02_weapons", "got_two_pistols")
                $ char_note("Lyra", "Negotiated with Vex: all scrip + credits (valued at ~50) for two pistols.")

                vex "Together that's [combined_value] scrip equivalent. Close enough. I'll take it."
                vex "Two pistols. Same deal. Unregistered, maintained, reliable."
                a "Thank you."
                vex "You paid fair. That’s all that matters."

            else:
                vex "Together that's [combined_value] scrip equivalent. Still short."
                vex "I can give you one pistol and a knife for that. Take it or leave it."

                menu:
                    "One pistol and a knife. Not ideal but better than nothing."
                    "Accept the deal":
                        $ weapons_scrip_delta = -current_scrip
                        $ inventory["scrip"] = 0
                        $ inventory["credits"] = 0
                        $ add_item("weapons", "pistol_standard")
                        $ add_item("weapons", "knife_combat")
                        $ mark_scene("act2_activity_02_weapons", "got_pistol_and_knife")
                        $ char_note("Lyra", "Vex compromise: one pistol + combat knife for our remaining scrip + credits.")
                        vex "Smart. One gun is better than no guns."
                        vex "Pistol for whoever shoots better. Knife for backup. Don't die stupidly."
                        a "We'll try not to."

                    "Refuse — look for other options":
                        a "Not good enough. We need two pistols."
                        vex "Then come back when you have real money. I'm not a charity."
                        vex "Door's that way. Don't let it hit you on the way out."
                        "Deal's off. We leave empty-handed. Need another plan."
                        jump activity2_alternate_methods

        "Offer to work off the debt — trade a favor for weapons":
            $ mark_scene("act2_activity_02_weapons", "method_favor_proposed")
            a "We don't have enough scrip. But we can work for it. Trade a favor for the weapons."
            vex "(interested) A favor. From defectors. That could be valuable."
            vex "What kind of work are you offering?"
            a "Whatever you need. Delivery, protection, information. We're capable."
            vex "You're also wanted. That makes you a liability."
            a "Or an asset. We know Echelon. We know how they think and operate. That's worth something."
            vex "...Alright. I'll bite. Here's the deal."
            vex "I give you two pistols now. You owe me a favor. One job, no questions, completed when I call it in."
            vex "You refuse or screw it up, and I spread the word you're Echelon plants."

            menu:
                "Accept the favor deal or refuse?"
                "Accept — owe Vex a favor":
                    $ mark_scene("act2_activity_02_weapons", "vex_favor_owed")
                    $ add_item("weapons", "pistol_standard")
                    $ add_item("weapons", "pistol_standard")
                    $ mark_scene("act2_activity_02_weapons", "got_two_pistols")
                    $ char_note("Lyra", "Owe Vex one favor for two pistols (leverage active).")
                    $ adjust_empathy_once("weapons_vex_favor_ob", -1)  # Pragmatic debt

                    a "Deal. One favor. We'll honor it."
                    vex "(grins) Smart. Desperate, but smart. I like desperate people. They're motivated."
                    vex "Two pistols. Maintained, reliable. When I call, you answer. Clear?"
                    a "Clear."
                    vex "Good. Now get out. You're making my other customers nervous."

                "Refuse — too risky":
                    a "No deal. A blank favor is too dangerous. We'll find another way."
                    vex "(shrugs) Your choice. Door's that way. Good luck finding weapons without money or leverage."
                    "Deal refused. We leave empty-handed. Need another option."
                    jump activity2_alternate_methods

        "Leave — find another way" if not can_afford_full:
            "Can't afford it. Can't risk the favor. Time to find another option."
            jump activity2_alternate_methods

    # SUCCESS PATH via Vex?
    if "got_two_pistols" in scene_flags.get("act2_activity_02_weapons", set()) or \
    "got_pistol_and_knife" in scene_flags.get("act2_activity_02_weapons", set()):

        scene bg_sector7_market with fade
        "Outside. Armed. Finally. The weight of weapons is strange. Comforting and terrifying."
        l "(checks pistol) Good quality. Well maintained. Vex knows their business."
        a "(checks his weapon) Yeah. Feels strange. Glass always had weapons. Aeron Rylan hasn't carried one in weeks."
        l "Glass is dead. Aeron Rylan is armed. There's a difference."
        a "Is there? Or am I just Glass with a new name?"
        l "That's up to you. A gun doesn't make you Glass. What you do with it does."
        a "Then I'll do something different. Use it to protect instead of kill."
        l "Noble. We'll see how long that lasts when someone's trying to kill us."
        a "Guess we'll find out."

        if "got_two_pistols" in scene_flags.get("act2_activity_02_weapons", set()):
            "Two pistols. Both armed. Both ready. One step closer to surviving this."
        else:
            "One pistol, one knife. Not ideal, but enough. Better than nothing."

        $ mark_scene("act2_activity", "weapons_done")
        jump activity2_return_hub

    # --- ALTERNATE METHODS (no deal with Vex) ---
label activity2_alternate_methods:

    scene bg_sector7_market with fade
    "No weapons from Vex. Either can't afford it or won't risk the favor. Need another option."

    l "So what now?"
    a "We find another way. There's always another way."
    l "Like what? Steal them? Make them ourselves?"
    a "...Maybe. Or we take them from someone who won't miss them."
    l "You mean Echelon."
    a "I mean anyone who has them and won't sell them."

    menu:
        "What's the plan?"
        "Ambush Echelon patrol — steal their weapons":
            $ mark_scene("act2_activity_02_weapons", "method_stolen_echelon")

            a "Echelon patrols come through here. Small teams, two or three soldiers. We ambush them."
            l "That's insane. We're unarmed and they're trained."
            a "We're trained too. We know their tactics, their patrol routes, their weaknesses. We can do this."
            l "And if we're wrong? If we fail?"
            a "Then we die. But we were going to die unarmed eventually anyway. At least this way we go down fighting."

            l "...Alright. Let's do it. How?"
            a "We wait. Watch patrol patterns. Find a vulnerable moment. Strike fast, take weapons, disappear."
            l "Simple plan. Lots of ways it can go wrong."
            a "All good plans are simple. It's the execution that matters."

            "We find a spot. Alley overlooking patrol route. Wait. Watch. Two hours pass. Then three. Patience is survival."
            "There. Two soldiers. Standard patrol. Bored, not expecting trouble. Perfect."

            a "(whisper) Two targets. You take left, I take right. Fast and silent. No gunfire if possible."
            l "What do we have for weapons?"
            a "Rocks. Surprise. Desperation. That'll have to be enough."
            l "Great plan."
            a "You have a better one?"
            l "...No. Let's do this."

            "Move. Drop. Tackle. Soldier goes down hard. Struggling, trying to shout. Hand over mouth. Choke hold. He fights. I hold. Ten seconds. Twenty. Goes limp."
            "Lyra's soldier down. Unconscious. Bleeding from head wound. Still breathing. That's enough mercy for now."

            a "(fast) Weapons. Ammo. Comms. Take it all. We have maybe two minutes before backup."
            l "(stripping gear) Got it. Pistols, rifles, magazines. This is enough."
            a "Then move. Now. Before they wake up or backup arrives."

            "Run. Alleys. Twisting paths. Footsteps behind. Shouts. Pursuit. Keep moving. Don't stop. Don't look back."
            "Stop. Finally. Deep enough. Lost them. Breathing hard. Hearts pounding. Alive. Armed."

            l "(gasping) That was insane."
            a "(breathing hard) That was necessary."
            l "We just attacked Echelon soldiers. They'll escalate. Send more patrols. Hunt harder."
            a "They were already hunting us. Now we're just armed while they do it."

            $ add_item("weapons", "pistol_echelon")
            $ add_item("weapons", "pistol_echelon")
            $ add_item("weapons", "rifle_echelon")
            $ mark_scene("act2_activity_02_weapons", "got_echelon_gear")
            $ inc_rep("echelon", -10)
            $ add_team_suspicion(2)
            $ adjust_empathy_once("weapons_ambush_ob", -1)

            "Echelon weapons. Two pistols, one rifle, full magazines. Stolen from the system that made us. Poetic."

            $ mark_scene("act2_activity", "weapons_done")
            jump activity2_return_hub

        "Scavenge — search ruins for abandoned weapons":
            $ mark_scene("act2_activity_02_weapons", "method_scavenged")

            a "The Purge destroyed whole sectors. Buildings collapsed, people fled. Weapons left behind."
            l "You want to scavenge Purge sites."
            a "I want to find what survivors left behind when they ran or died. Same thing."
            l "That's grim."
            a "We're living in grim. Might as well make use of it."

            "Back to Sector 10. The graveyard. Searching rubble for weapons left by the dead. This is what we've become."
            "Hours pass. Searching. Lifting rubble. Finding bodies. Finding nothing. Then finally, a cache. Hidden. Abandoned. Forgotten."

            a "(finds it) Here. Hidden cache. Resistance supply dump probably."
            l "(examines) Two pistols. Old models but maintained. Ammo. Basic but functional."
            a "Functional is all we need. Take them. Leave the rest for whoever comes next."
            l "You're being generous with resistance supplies."
            a "We're joining the resistance. Eventually. Call it a loan."

            $ add_item("weapons", "pistol_old")
            $ add_item("weapons", "pistol_old")
            $ mark_scene("act2_activity_02_weapons", "got_scavenged_cache")
            $ adjust_empathy_once("weapons_scavenge_emp", +1)

            "Old pistols. Worn but maintained. Someone's backup plan. Now it's ours. Hope they don't need it anymore."

            $ mark_scene("act2_activity", "weapons_done")
            jump activity2_return_hub


# RETURN TO HUB
label activity2_return_hub:

    scene bg_safe_house with fade

    "Back. Safe house. Evening. Armed now. That changes everything."
    athought "Weapons. Tools of death. Glass carried them without thinking. I carry them with purpose. That has to mean something."

    l "How do you feel?"
    a "Armed. Prepared. Still terrified. But less helpless."
    l "That's progress."
    a "Is it? Or am I just better equipped to make the same mistakes?"
    l "Depends on what you do with them. Glass used weapons to kill. You're using them to survive. That's different."
    a "...Yeah. Different. I'll hold onto that."

    # Acquisition summary lines
    if "method_bought" in scene_flags.get("act2_activity_02_weapons", set()):
        "Bought weapons from Vex. Clean transaction. Professional. Expensive but simple."
    elif "method_negotiated" in scene_flags.get("act2_activity_02_weapons", set()):
        "Negotiated with Vex. Used every credit we had. Fair deal, both sides compromised."
    elif "method_favor_proposed" in scene_flags.get("act2_activity_02_weapons", set()) and "vex_favor_owed" in scene_flags.get("act2_activity_02_weapons", set()):
        "Owe Vex a favor. One job, no questions. Dangerous leverage but necessary. We're armed and that's what matters."
    elif "method_stolen_echelon" in scene_flags.get("act2_activity_02_weapons", set()):
        "Stole from Echelon. Ambushed patrol, took their weapons. They'll hunt harder now but we're armed. Worth it."
    elif "method_scavenged" in scene_flags.get("act2_activity_02_weapons", set()):
        "Scavenged from ruins. Dead resistance fighters' backup cache. Borrowed from the fallen. Hope they'd approve."

    # Rewards panel (textual)
    $ spent_label = ("-" + str(abs(weapons_scrip_delta))) if weapons_scrip_delta < 0 else ("+" + str(weapons_scrip_delta))
    "{b}Activity Complete: Acquire Weapons{/b}"
    "
    Results:
    - Scrip Change: [spent_label]
    - Weapons: (see inventory)
    - Reputation shifts: Echelon [reputation['echelon']]
    - Suspicion: [player_state['team_suspicion']]
    "

    # Wrap op + logs
    $ mark_scene("act2_activity_02_weapons", "completed")
    $ mark_scene("act2_activity", "weapons_done")  # mirrors to legacy dict via helper
    $ summary = end_operation("op2B_weapons", tag="Acquire Weapons")
    $ log_line(summary)

    # Reset local delta
    $ weapons_scrip_delta = 0

    jump act2_activity_hub
