# act2_014_temp_base.rpy


# =======================================================
# ACT 2 - Scene 14: Temp Base - State of Resistance
# =======================================================


label act2_temp_base:

    # VISUAL: Temp shelter. Basement of collapsed building. Cramped. Dark. Unstable.
    # LIGHTING: Dim emergency lights. Shadows deep. Oppressive.
    # SOUND: Water dripping. Concrete settling. Voices above (city life continuing).

    #scene bg_temp_shelter with fade

    "Temp shelter. Selene called it temporary and she meant it. Basement of a half-collapsed building in Sector 6. Cramped, dark, smells like mold and desperation. Walls cracked. Water dripping. This isn't a base. This is a hole to hide in until Echelon finds us."

    # [EMP/OB FLAVOR - additive]
    "{ob}Load-bearing cracks step at irregular intervals; dust plumes on each rumble.{/ob} {emp}Everyone sits too straight—hypervigilance eating the slouch from spines.{/emp}"

    # VISUAL: Resistance fighters gathered. 12 total. Shell-shocked. Exhausted. Traumatized.
    # Mix of ages. All looking at Selene. Waiting for leadership. For hope. For anything.

    "Twelve people. That's what's left. Twelve fighters sitting on rubble and broken crates, looking at Selene like she has answers. Looking broken. Looking lost. Looking like I feel."

    # VISUAL: Selene standing. Addressing group. No podium. No ceremony. Just reality.
    s "Everyone here? Good. Let's talk about where we are. And where we're going."

    # VISUAL: Pulls out battered datapad. Old resistance records. Numbers. Statistics. Ghosts.
    s "Before the Purge, this resistance numbered 847 active fighters."
    s "Five major bases across Sectors 8, 9, 10, 12, and 14. Weapon stockpiles. Supply lines from smugglers and sympathizers across the Lower Spans."
    s "Command structure: myself as overall tactical lead, four division commanders, twenty squad leaders, fifty support staff."

    # VISUAL: Resistance fighters listening. Some remembering. Some weren't there. All grieving.
    "847 fighters. I killed 600 in one night during the Sweep. Then the Purge killed most of what remained. The math is sickening."

    s "We had infrastructure. Training facilities. Medical stations. We weren't just surviving. We were winning."
    s "Echelon feared us. Marcus knew we could challenge him in open combat. That's why he launched the Purge. Not to stop terrorism. To stop us."

    # VISUAL: She sets datapad down. Numbers don't matter anymore. Just what's left.
    s "Then the Purge happened. Orbital strikes on Sectors 8, 9, and 10. 100,000 civilians dead. And our bases were in those sectors."
    s "Sector 10 main base. 600 fighters. Gone in thirty seconds. Direct hit. Nobody survived."
    s "Sector 8 base. 120 fighters. Collapsed during strikes. Twelve survivors. They scattered. I don't know where they are."
    s "Sector 9 base. 80 fighters. Echelon ground forces hit them during the chaos. Fifteen survived. They fled north. No contact since."

    # VISUAL: Resistance fighters' faces. Grief. Rage. Hopelessness. Holding on by threads.
    resistance_fighter1 "(quiet) What about Sector 12 and 14 bases?"
    s "Abandoned. Echelon knows those locations now. Informants or surveillance. We evacuated before they could hit us. But we left everything behind."
    s "Weapons. Supplies. Medical equipment. Everything that made us dangerous. Gone."

    # VISUAL: Long silence. Weight of loss settling. 847 to 12. Army to squad.
    "847 to 12. From army to squad. From winning to barely surviving. That's what the Purge accomplished. Marcus didn't just kill civilians. He gutted the resistance. And he knew exactly what he was doing."

    s "Command structure? Dead. All four division commanders died in Sector 10. Most squad leaders too. Support staff scattered or killed."
    s "I'm the last of the leadership. Just me. And twelve of you."

    # VISUAL: Selene looks around. Meets eyes. Doesn't flinch from reality.
    s "So let's talk about what we have. Current inventory."
    s "Weapons: Eighteen pistols. Four rifles. Low ammunition for all of them. No heavy weapons. No explosives. No body armor."
    s "Supplies: One week of food and water if we ration. Basic medical kit. No surgical equipment. No long-term provisions."
    s "Intel: Some. We have contacts. We have knowledge. But our information networks are broken."
    s "Safe houses: This one. Temporary. Unstable. Echelon sweeps this area. We have 48 hours here. Maybe less."

    # VISUAL: Fighters processing. Some look defeated. Some angry. All scared.
    resistance_fighter2 "So what do we do? Hide? Run? Scatter and hope Echelon doesn't find us?"
    s "No. We rebuild. From scratch. From nothing. We become dangerous again."

    # VISUAL: Some fighters skeptical. How do you rebuild from this?
    resistance_fighter3 "Rebuild with what? We have nothing. Twelve people and scraps. How do we fight an empire with that?"
    s "The same way we built it the first time. One person at a time. One weapon at a time. One mission at a time."
    s "We were 847 once. We didn't start that way. We started with five people in a basement. Sound familiar?"

    # VISUAL: Glances around shelter. Parallels clear. Starting over. Full circle.
    s "We built it once. We'll build it again. Smarter this time. Harder to destroy. More careful who we trust."
    s "Echelon thinks they broke us. They're wrong. They just made us angrier."

    # VISUAL: Aeron watching. Impressed. She's good. Turning despair into determination.
    athought "She's good at this. Leadership. Taking a disaster and making it sound like opportunity. I can see why 847 people followed her. Why they died for her."

    # [EMP/OB FLAVOR - additive]
    "{emp}Her voice threads grief through steel; the room catches it, breath by breath.{/emp}"

    # VISUAL: Lyra beside him. Watching. Processing. Both newcomers to this.
    l "(whisper) Do you think we can? Rebuild from this?"
    a "(whisper) I don't know. But she believes it. That's something."
    l "Belief doesn't stop bullets."
    a "No. But it's what keeps you standing when bullets miss. We need that."

    # SOUND: Door opening. Alert. Everyone tenses. Weapons readied. Visitor.
    "Door. Opening. Everyone tenses. Weapons up. Ready for threat. Ready for Echelon. Ready for death."

    # VISUAL: ZIRA enters. Hands visible. Calm. Expected. Selene relaxes. Others follow.
    z "Easy. Just me. Heard you had new recruits. Came to see if they're still alive."

    # VISUAL: Zira carrying supply pack. Medium size. Heavier than it looks.
    s "Zira. You're late."
    z "Traffic. You know how it is. Echelon patrols everywhere after the Purge. Had to take the long way."

    # VISUAL: Sets pack down. Opens it. Supplies. Food, medical, ammunition. Not much but something.
    z "Brought what I could. Food for three days. Medical supplies. Ammunition for pistols. Not much but better than nothing."
    s "Where'd you get this?"
    z "Don't ask questions you don't want answered. Let's just say some Echelon supply depot is lighter than it was yesterday."

    # VISUAL: Resistance fighters moving to sort supplies. Grateful. Small comfort in darkness.
    resistance_fighter1 "Thank you. This helps. Really helps."
    z "Don't thank me yet. It's three days of supplies. That's all. You need permanent solution. This is just bandage."

    # VISUAL: Zira spots Aeron and Lyra. Moves to them. Smile. Genuine. Relieved.
    z "You're still alive. Good. I was worried."
    a "We made it through the meeting. Barely. Selene gave us a chance."
    z "I heard. Dynamic entrance. Crisis. Resolution. Very dramatic. Very you."
    a "Wasn't exactly planned that way."
    z "Nothing with you is ever planned. But you made it work. That's what matters."

    # VISUAL: She hugs him. Brief. Sisterly. Relief pouring through.
    z "I'm proud of you. Both of you. You joined. You're here. You're doing it."
    a "Doing what? Hiding in a basement with twelve people against an empire?"
    z "Starting. That's what you're doing. Starting the fight. That's more than most people ever do."

    # VISUAL: Pulls back. Looks at him seriously. Emotion showing through usual tough exterior.
    z "Kai never got this far. He tried to defect and Marcus killed him before he could do anything. But you? You made it. You joined. You're here."
    z "That means something. That means he didn't die for nothing. Because you're doing what he couldn't."

    # VISUAL: Aeron processing. Weight of that. Being Kai's second chance. Living for both of them.
    a "I'll try not to waste it."
    z "You won't. I know you won't. Because I'm going to make sure you don't."

    # VISUAL: Selene approaches. Evaluating Zira. Complicated relationship.
    s "Zira. Thanks for the supplies. And for vouching for these two."
    z "They earned the vouch. I don't give those lightly."
    s "I know. That's why I listened. You're usually right about people."
    z "Usually. Not always. But usually."

    # VISUAL: Moment between them. History there. Respect. Not quite friendship. Professional.
    s "You staying? Or just dropping supplies and leaving like always?"
    z "That depends. You planning something worth staying for?"
    s "Rebuilding the resistance. Hitting back at Echelon. Taking down Marcus. Is that worth staying for?"

    # VISUAL: Zira considers. Longer than usual. Glances at Aeron. Decision forming.
    z "...Yeah. Yeah, I think it is."
    s "(surprised) You're joining? Officially?"
    z "Don't sound so shocked. I've helped before."
    s "You've traded intel and run occasional jobs. That's not joining. That's freelancing."
    z "Well consider me staff now. Permanent position. Benefits included."

    # VISUAL: Selene studies her. Sees something different. Looks at Aeron. Understands.
    s "It's because of them, isn't it? The defectors. You're joining because they're here."
    z "Maybe. Or maybe I'm just tired of watching from the sidelines. Either way, I'm in. You have a problem with that?"
    s "No. No problem. We need everyone we can get. Welcome to the resistance. Officially."

    # VISUAL: Zira nods. Commitment made. Different now. Part of something instead of adjacent to it.
    z "(to Aeron) Guess we're both stuck here now. Better make it count."
    a "Guess so. Thanks for staying. Makes it less terrifying."
    z "Oh it's still terrifying. But at least we're terrified together."

    # VISUAL: Selene calls attention back. More to discuss. Plans to make.
    s "Alright. Back to business. This shelter is temporary. 48 hours maximum. After that Echelon finds us or the walls collapse. Probably both."
    s "We need permanent base. Hidden. Defensible. Room to grow. And we need it fast."

    # VISUAL: Resistance fighters murmuring. Where? How? Everything's compromised or destroyed.
    resistance_fighter2 "Where? Every base we had is gone. Echelon knows the locations. How do we find somewhere they don't know about?"
    s "We scout. We search. We find somewhere new. Somewhere they haven't thought to look."

    # VISUAL: Aeron steps forward. Volunteering. Natural. Necessary.
    a "I'll do it. I'll scout locations. Find us a base."
    s "You? You just got here. You don't know the resistance territories."
    a "No. But I know the Unders now. Spent a week surviving down here. Learning the sectors. Meeting people. Building contacts."
    a "I can find us something. Give me a day. I'll bring back options."

    # VISUAL: Selene evaluating. Sees conviction. Sees capability. Sees asset.
    s "...Fine. You scout. But not alone. You take someone who knows the territory. Someone who knows what we need."
    z "I'll go. I know the Unders better than anyone here. And I know what makes a good resistance base. Done this before."

    # VISUAL: Zira and Aeron. Good team. Practical. Trusted.
    s "Good. You two scout. Find us five potential locations. We evaluate together and choose the best."
    s "Look for multiple exits. Defensible positions. Hidden from Echelon patrols. Room for expansion. We're starting small but planning big."
    a "Understood. When do we leave?"
    s "Now. Every hour we stay here is an hour closer to discovery. Move fast. Stay hidden. Come back with options."

    # VISUAL: Aeron and Zira preparing. Checking gear. Light pack. Fast movement prioritized.
    z "(to Aeron) Ready for urban exploration? It's going to be a lot of walking. A lot of dark places. A lot of hoping we don't run into Echelon."
    a "Sounds like every day since we defected."
    z "Fair point. At least this time we're looking for something instead of running from something. That's progress."

    # VISUAL: Lyra approaches. Concerned but supportive.
    l "Be careful. Both of you."
    a "Always. We'll be back before dark. With options. I promise."
    l "Don't make promises you can't keep. Just come back. That's enough."
    a "...Yeah. We'll come back."

    # VISUAL: Final check. Ready. About to leave. Selene's voice stops them.
    s "Aeron. Zira. One more thing."
    
    # VISUAL: Both turn. Selene serious. Making point.
    s "You're scouting for more than just walls and exits. You're scouting for home. For the place we rebuild from. For the foundation of everything we're going to do."
    s "Don't just find us shelter. Find us something worth fighting for. Something worth defending. Something worth dying for if it comes to that."
    s "Can you do that?"

    # VISUAL: Aeron and Zira exchange glance. Nod. Understand weight of task.
    a "We'll find it. Whatever it takes. We'll find it."
    s "Good. Now go. Clock's running."

    # VISUAL: They leave. Door closing behind them. Into the Unders. Into uncertainty. Into hope.
    "Out into the Unders. Scouting for home. For foundation. For future. Five locations to find. One day to find them. Everything riding on getting this right. No pressure. Just the entire resistance depending on us finding the perfect place to rebuild from ruins. Simple."

    # TRANSITION: Journey beginning. Sector 6 streets. Morning light. Purpose.
    #scene bg_lower_spans_morning with fade

    "Morning in the Lower Spans. City waking. People moving. Life continuing despite everything. And us moving through it. Looking for the place that becomes everything. The place that becomes home. The place that becomes resistance."

    # VISUAL: Zira leading. Confident. Knows these streets. Aeron following. Observing. Learning.
    z "First stop: old subway station. Haven't been down there in years but it might work. Deep underground. Multiple tunnels. Could be perfect or could be death trap. Only one way to find out."
    a "Lead the way. I'm right behind you."
    z "Always are. That's one of your better qualities."

    # VISUAL: Moving together. Into the city. Into the search. Into the future.
    "Into the Unders. Looking for home. Looking for hope. Looking for the place that becomes ours. Day one of rebuilding. Everything starts here. Everything changes here. Find the right place and we have foundation. Find the wrong place and we die slowly. No pressure. Just everything."

    # ---------------------------
    # NEW HELPER STATE UPDATES
    # ---------------------------
    # Converted from:
    #   $ scenes["temp_base_briefing"] = True
    #   $ canon["resistance_scale_known"] = True
    #   $ characters["zira"]["officially_joined"] = True

    $ mark_scene("temp_base_briefing")
    $ mark_flag("resistance_scale_known", True)
    $ mark_flag("zira.officially_joined", True)

    # Optional rel/log breadcrumbs (additive; safe to remove if you prefer clean logs)
    $ log_line("briefing", "Selene: 847→12; inventory famine; 48h cap; rebuild mandate.")
    $ log_line("pledge",   "Aeron+Zira will scout five base candidates.")
    $ log_line("theme",    "Home as center; plan small-start/big-scale.")

    # ---------------------------
    # OB/EMP ANALYSIS SNAPSHOT — Aeron
    # ---------------------------
    # Baseline: facing loss → task orientation (OB +2), maintains attunement to group grief (EMP +2).
    # Modifiers from Meeting Selene outcomes if present:
    # - broke_promise → EMP −1
    # - showed_coldness → EMP −1
    # - casualties == 0 → OB +1 (confidence/clarity bump)
    # - casualties > 3 → EMP +1 (guilt-heightened empathy)
    #
    # NOTE: This reads from scenes["meeting_selene"] if available in memory.
    # TODO: If your helper stores crises under a different key, adjust lookups accordingly.

    $ _emp_delta = +2
    $ _ob_delta  = +2

    if scenes.get("meeting_selene", {}).get("broke_promise"):
        $ _emp_delta -= 1
    if scenes.get("meeting_selene", {}).get("showed_coldness"):
        $ _emp_delta -= 1
    if scenes.get("meeting_selene", {}).get("casualties", 0) == 0:
        $ _ob_delta += 1
    elif scenes.get("meeting_selene", {}).get("casualties", 0) > 3:
        $ _emp_delta += 1

    $ set_emp("aeron", _emp_delta)
    $ set_ob("aeron",  _ob_delta)
    $ snapshot_state("aeron",
        context="temp_base_briefing",
        emp_delta=_emp_delta,
        ob_delta=_ob_delta,
        note="Moves from survivor-guilt rumination to logistics-forward; holds space for group grief; reframes goal as ‘find home’."
    )

    # ---------------------------
    # LEGACY→HELPER MAPPING NOTES
    # ---------------------------
    # TODO: If you need per-faction reputation deltas here, confirm target entities and I’ll add:
    #   rel("resistance", rep=+N) / rel("unders", rep=+N) / rel("selene", trust=+N), etc.

    return
