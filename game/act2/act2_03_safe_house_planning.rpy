# act2_03_safe_house_planning.rpy


# =======================================================
# ACT 2 - Scene 3: Safe House Planning (HUB)
# =======================================================


label act2_safe_house_planning:

    # VISUAL: Safe house. Morning light through barred window. Day 2.
    # LIGHTING: Dim gray dawn filtering in. Single bulb still on. Cold.
    # SOUND: City waking up below; distant machinery; footsteps in hallway.

    "{i}Day 2.{/i}"
    
    # VISUAL: Aeron wakes on concrete floor. Body stiff. Lyra already awake, staring at wall.
    # Both look like hell. Dark circles. Exhaustion. Trauma settling into bones.

    "{i}Morning. If you can call it that. Concrete floor leaves you cold and aching, mind worse than the body.{/i}"
    "{i}Lyra's already awake, staring at nothing. Her hand moves to her Band in that automatic way she can't seem to stop.{/i}"

    a "{i}Day 2 in the Unders. Still alive. That has to count for something.{/i}"
    
    # VISUAL: Lyra glances at him. Nods. No words. What is there to say?
    l "(quiet) Did you sleep?"
    a "Some. You?"
    l "Not really."
    a "Nightmares?"
    l "Memories. Same thing at this point."

    # SOUND: Door lock beeping. Both tense immediately. Hands move toward weapons they don't have.
    "{i}The lock beeps. They freeze, hands moving instinctively toward weapons that aren't there.{/i}"
    "{i}Still defenseless. Still terrified every time that door opens.{/i}"

    # VISUAL: Door opens. Zira enters. Arms full of supplies again. Looks tired but alert.
    z "Morning, fugitives. Still breathing, so that's a good start."

    # VISUAL: She drops supplies. Food packets, water, something wrapped in cloth.
    # SOUND: Packages hitting floor. Rustling. Practical.

    z "Breakfast—protein bars and water. Not fancy, but it'll keep you functional."
    a "You didn't have to—"
    z "I did, actually. You two look like corpses and I can't have you dying before the fun starts."

    # VISUAL: She sits cross-legged. Same comfortable confidence. Owns this space.
    z "Alright, reality check part two. You listening?"
    l "We're listening."
    z "Good. What I'm about to say determines whether you survive the week."

    # VISUAL: She pulls out small datapad. Lists. Notes. Plans.
    z "You can't just hide in here forever. Echelon's hunting and locals are getting suspicious. Word spreads fast down here—two Echelon operatives vanished right after the Purge."
    z "People connect dots fast in the Unders. You need cover."

    a "The fake IDs—"
    z "Are paper thin. IDs get you past casual inspection, sure. But actual survival? That requires integration. Reputation. Proof you belong here."
    z "Right now you're obvious outsiders. That makes you targets."

    l "What do we do?"
    z "You work. You blend in. You earn your place one interaction at a time."
    z "The Unders run on barter, favors, and reputation. You have exactly none of those things."
    z "So you build them. One day at a time."

    # VISUAL: She swipes through datapad. Shows them list.
    z "I've identified seven things you need to survive down here. Call them priorities. You've got about a week before Selene decides whether she'll even meet you."
    z "Use that week to prove you're serious. Prove you're not just Echelon trash hiding in a hole."

    a "What are the seven things?"

    # VISUAL: Zira leans forward. Direct. Practical. No room for negotiation.
    z "First: work. You need money—real money. Scrip that actually spends down here, not your useless Aeries credits."
    z "Your Echelon funds might work if you find the right black market dealers. But finding them means exposure. Better to earn clean."

    z "Second: weapons. You're completely unarmed right now. That's suicide in the Unders. Knife minimum, gun if you can manage it. Something to defend yourselves with."
    z "Everyone else down here is armed and they won't hesitate to use them."

    z "Third: intel. You need to know Echelon's movements and patrol patterns if you want to stay ahead of them."
    z "I have a contact—info broker. Brilliant but weird. She might help if you don't piss her off."

    z "Fourth: medical supplies. People get hurt down here constantly. You want reputation? Save someone's life. Heal someone's kid."
    z "There's an underground clinic with a medic who might help. Or might spit in your face considering Glass's reputation."

    z "Fifth: reputation itself. Do something good. Help someone. Change how people see you."
    z "Locals hate you right now. Change that one person at a time. Escort an elder, protect a vendor—small things that add up."

    z "Sixth: survival skills. You don't know the Unders. The culture, the signals, the territories. I'll teach you. Not because I'm nice, but because you're useless to anyone otherwise."

    z "Seventh: confront your past. Sector 10. The Sweep. You need to face it. There's a survivor out there—someone who remembers, someone who lost everything."
    z "Talk to them. Apologize, listen, whatever it takes. Selene will ask, and if you haven't done it she'll know you're not serious."

    # VISUAL: Both process. Seven tasks. One week. Overwhelming.
    l "That's... a lot."
    z "That's survival. You wanted to fight Echelon? This is step one. You can't fight an empire from a concrete box."
    z "You need allies, resources, skills, trust. None of that comes free."

    a "What about Selene? You said she's considering."
    z "She is. Barely. I told her about the Sweep and the 200 you saved. She didn't shoot the messenger, so that's progress."
    z "But she lost most of her cell in the Purge. Sector 10 was her territory. You swept Sector 10, which means you killed her people."
    z "So yeah, she's considering. Considering whether to meet you or just put a bullet in your head the moment she sees you."

    l "Will she help us?"
    z "Depends. Do these seven things. Prove you're not just hiding. Prove you're willing to work, to change, to actually earn it."
    z "Then maybe she gives you a chance. Or maybe she kills you anyway. Honestly could go either way."

    # VISUAL: Zira stands. Stretches. Ready to leave again.
    z "You've got one week. Seven days, seven tasks. Do them in whatever order you want—I don't care. But get them done. All of them."
    z "Because when Selene agrees to meet, you better have something to show for this week."

    a "Where do we start?"
    z "That's up to you. You're adults. Figure it out."
    z "Just don't do anything stupid. Which, given your track record, is probably a lot to ask."

    # VISUAL: She moves to door. Pauses. Looks back.
    z "I'll check in and leave messages when I can. Help where it makes sense. But I can't babysit. I have my own work, my own problems."
    z "You're on your own most of the time. Get used to it."

    l "Zira. Why are you doing this?"
    z "(pauses) Because someone should. And nobody else will."
    z "And because... I want to see if Glass can become something else. Call it curiosity, call it hope, call it stupidity."
    z "Either way, don't waste it."

    # VISUAL: She leaves. Door closes. Lock engages. Alone again.
    "{i}Gone again. Leaving them with seven impossible tasks and one week to complete them.{/i}"
    "{i}Everything rides on this. Every single thing.{/i}"

    # VISUAL: Both sit. Looking at each other. Overwhelmed but determined.
    l "Seven tasks."
    a "Seven days."
    l "Where do we even start?"
    a "...I don't know. But we have to start somewhere."

    # VISUAL: Aeron stands. Looks at door. The city beyond. Terrifying and necessary.
    a "{i}One week to prove we're worth keeping alive. One week to build something from nothing.{/i}"
    a "{i}Seven tasks. Every single one could kill us.{/i}"

    l "(stands beside him) We do this together. Like everything else."
    a "Together. Yeah."
    l "What's first?"

    # VISUAL: Aeron looks at her. Both broken. Both scared. Both committed.
    a "We figure out who Kade Voss is. Who Mira Chen is. We go out there, we survive, we earn it."
    l "One day at a time."
    a "One day at a time."

    # ==============================================================
    # ACTIVITY HUB - Day Selection Loop
    # ==============================================================

    # Initialize activity tracking if first time
    $ if not hasattr(store, 'activities_completed'):
        $ activities_completed = []
        $ current_day = 2
        $ activities_remaining = 

    jump act2_activity_hub    

label act2_activity_hub:

    # VISUAL: Hub scene. Safe house. Time of day varies based on current_day.
    # LIGHTING: Changes per day (morning/afternoon/evening hints).
    
    # Check if returning from activity or first time
    $ if len(activities_completed) > 0:
        "{i}Day [current_day]. Another day, another task to complete.{/i}"
        "{i}Still alive. Still moving forward. That has to mean something.{/i}"
    else:
        "{i}Day 2. The first step into this new life. Choose carefully.{/i}"

    # CHECK FOR LYRA SCENE BEFORE SHOWING MENU (after any activity completion)
    # This checks every time they return to hub
    $ if len(activities_completed) > 0:
        jump act2_check_lyra_scene_hub

label act2_continue_hub:
    # Show progress
    $ activities_remaining = 7 - len(activities_completed)
    
    if activities_remaining > 0:
        "{i}[activities_remaining] tasks remaining before Selene decides our fate.{/i}"
        
        # Build activity menu dynamically based on what's completed
        menu:
            "What should we focus on today?"
            
            "Find Work - Earn scrip, establish cover" if "work" not in activities_completed:
                $ activities_completed.append("work")
                $ current_day += 1
                jump act2_activity_01_find_work
            
            "Acquire Weapons - Get armed, black market contact" if "weapons" not in activities_completed:
                $ activities_completed.append("weapons")
                $ current_day += 1
                jump act2_activity_02_acquire_weapons
            
            "Gather Intel - Meet info broker, learn patrol patterns" if "intel" not in activities_completed:
                $ activities_completed.append("intel")
                $ current_day += 1
                jump act2_activity_03_gather_intel
            
            "Medical Supplies - Underground clinic, prove worth" if "medical" not in activities_completed:
                $ activities_completed.append("medical")
                $ current_day += 1
                jump act2_activity_04_medical_supplies
            
            "Earn Reputation - Help locals, change perceptions" if "reputation" not in activities_completed:
                $ activities_completed.append("reputation")
                $ current_day += 1
                jump act2_activity_05_earn_reputation
            
            "Survival Skills - Learn the Unders with Zira" if "survival" not in activities_completed:
                $ activities_completed.append("survival")
                $ current_day += 1
                jump act2_activity_06_survival_skills
            
            "Confront the Past - Return to Sector 10, face survivor" if "past" not in activities_completed:
                $ activities_completed.append("past")
                $ current_day += 1
                jump act2_activity_07_confront_past
    
    # All activities completed - trigger next story beat
    else:
        "{i}Seven days. Seven tasks. All completed, every single one of them.{/i}"
        "{i}Time to see if it was enough to earn Selene's attention.{/i}"
        #jump act2_06_the_message
        return


# New label to check for Lyra scene after each activity
label act2_check_lyra_scene_hub:
    
    # Check if thresholds are met
    $ lyra_trust = characters["lyra"]["trust"]
    $ lyra_affection = characters["lyra"]["affection"]
    
    # Check if scene already completed
    $ if characters["lyra"]["lewd_scene_completed"]:
        jump act2_continue_hub
    
    # Check thresholds
    $ if lyra_trust >= 7 and lyra_affection >= 5:
        $ characters["lyra"]["lewd_scene_unlocked"] = True
        
        # VISUAL: Safe house. Evening. Both exhausted from the day. Quiet moment.
        # LIGHTING: Dim. Single light. Intimate space.
        # SOUND: City quiet below. Their breathing. Silence comfortable.
        
        "{i}Evening. Quiet. Just the two of us in this small space. Something's different tonight.{/i}"
        
        # VISUAL: Lyra looking at him. Different energy. Vulnerable. Open.
        l "Aeron."
        a "Yeah?"
        l "Can we... can we just sit for a while? Not planning. Not surviving. Just... being."
        a "...Yeah. We can do that."
        
        # VISUAL: They sit. Close. Not touching yet. But proximity different.
        "{i}She sits close. Closer than usual. Not accidental. Intentional. Something unspoken between us.{/i}"
        
        menu:
            "The space between them feels charged. Different. Significant."
            
            "Spend the evening with Lyra":
                jump act2_lyra_intimate_scene
                
            "Give her space - rest instead":
                a "Actually... I should probably get some rest. Long day."
                l "(slight disappointment) Oh. Yeah. Of course. Rest is important."
                l "Goodnight, Aeron."
                a "Goodnight, Lyra."
                
                "{i}The moment passes. Maybe it was nothing. Maybe it was everything. Too late to know now.{/i}"
                
                jump act2_continue_hub
    else:
        # Not enough trust/affection yet
        jump act2_continue_hub

    # canon_note: Hub established - 7 activities over 7 days (Days 2-8)
    # canon_note: Activities can be done in any order - player choice matters
    # canon_note: Each activity = full scene, returns to hub after completion
    # canon_note: Zira's seven tasks: work, weapons, intel, medical, reputation, survival, past
    # canon_note: Selene mentioned - waiting to see if they're serious, will respond after tasks done
    # canon_note: One week timeline established - urgency building
    # canon_note: "Prove Glass can become something else" - Zira's core motivation
    # canon_note: Activities_completed list tracks progress, prevents repeating
    # canon_note: Current_day advances with each activity (Day 2 → Day 8)
    # canon_note: All 7 complete → Scene 6 triggers (Selene's message arrives)

    return