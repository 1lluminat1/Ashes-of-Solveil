# act2_15_base_scouting.rpy


# =======================================================
# ACT 2 - Scene 15: Scouting the Base
# =======================================================


label act2_base_scouting:

    # VISUAL: Lower Spans. Morning. Aeron and Zira moving through streets.
    # LIGHTING: Gray morning light. Industrial. Functional.
    # SOUND: City noise. Vendors. Workers. Life continuing.

    #scene bg_lower_spans_streets with fade

    "Moving through the Lower Spans with Zira. Morning crowds thin but present. Workers heading to jobs. Vendors setting up stalls. Normal life pretending the Purge never happened. Pretending 100,000 deaths don't matter. Maybe that's how you survive down here. By pretending."
    "{ob}Air carries fryer oil and brake dust; patrol drone hums fade in and out at ~40s intervals.{/ob} {emp}We match the city’s rhythm, not fighting it—blend first, scout second.{/emp}"

    # VISUAL: Zira navigating confidently. Knows every street. Every shortcut. Home territory.
    z "Five locations to scout. Subway station, abandoned clinic, warehouse ruins, apartment complex, maintenance tunnels. Full day's work if we're thorough."
    a "And we should be thorough. This is where we're rebuilding from. Can't afford to get it wrong."
    z "Agreed. So we check everything. Exits. Sightlines. Structural integrity. Proximity to Echelon patrols. Water access. Power access if possible."
    z "By the time we're done you'll know more about urban base selection than you ever wanted to."

    # VISUAL: First location ahead. Old subway entrance. Boarded up. Forgotten.
    z "First stop. Old subway station. Used to run through here decades ago before Echelon shut it down. Built new transit above ground where they could monitor everything."
    z "Left the old tunnels to rot. Perfect for people who want to hide from monitoring."

    # TRANSITION: Descending into subway. Dark. Damp. Underground.
    #scene bg_subway_station_old with fade

    "Down into darkness. Old subway station. Tiles cracked. Water dripping. Smell of mold and rust. Emergency lights flickering on motion sensors. Place has been abandoned for years but infrastructure's still here. Rails. Platforms. Tunnels stretching into darkness."

    # VISUAL: Exploring. Zira checking exits. Aeron examining structure. Professional assessment.
    z "Multiple tunnels. At least six directions from this central platform. That's good. Means multiple escape routes if Echelon finds us."
    a "Structure looks solid. No major cracks in the support columns. Water damage but nothing catastrophic. Could be reinforced easily enough."
    z "Power lines are intact. Old but intact. Could tap into city grid without anyone noticing. That's electricity sorted."
    a "What about water?"
    z "Maintenance tunnels should have access to city water mains. Not drinking quality but filterable. Better than nothing."

    # VISUAL: Checking deeper. Finding spaces. Rooms. Potential.
    z "Platform level could be living quarters. Service rooms for operations. Tunnels for storage and escape. This could work."
    a "It's dark though. No natural light. That'll affect morale long-term. Living underground does things to people."
    z "True. But it's also the hardest to find. Echelon doesn't patrol underground. Too many tunnels. Too easy to get lost. That's operational security."

    # VISUAL: Taking notes. Mental map. Pros and cons. Moving on.
    a "One down. Four to go. What's next?"
    z "Abandoned clinic. Sector 7. Tessa's territory actually. She might have opinions on using it."

    # TRANSITION: Back above ground. Journey to Sector 7. Walking. Talking.
    #scene bg_lower_spans_day with fade

    "Back above ground. Sunlight feels harsh after subway darkness. Moving toward Sector 7. Twenty minute walk. Zira knows shortcuts. I follow. Good rhythm. Comfortable silence between us. Easy partnership."

    # VISUAL: Conversation starting. Light. Building rapport.
    a "How long have you been doing this? Scouting bases. Running operations."
    z "Years. Since I was sixteen. Started as courier. Moved up to intel gathering. Eventually became independent contractor. Work for whoever pays or whoever's cause I believe in."
    a "And now you're staff. Permanent position. How's that feel?"
    z "(considers) Strange. Good strange. I've always been peripheral. Adjacent to causes but never fully in them. Safer that way. Less commitment. Less risk."
    z "But also lonelier. Watching from outside. Never quite belonging."

    # VISUAL: Vulnerability showing. Small. But there.
    a "What changed? Why commit now?"
    z "...You. Honestly. You changed it. Watching you crack and break and rebuild. Watching you choose something hard because it was right. That made me think maybe I should stop watching and start doing."
    a "No pressure then."
    z "(laughs) All the pressure. But good pressure. The kind that makes you better instead of breaking you."

    # VISUAL: Arriving at abandoned clinic. Sector 7. Medical signage faded but visible.
    #scene bg_abandoned_clinic with fade

    "Abandoned clinic. Sector 7. Three story building. Windows broken. Doors hanging off hinges. But structure intact. Medical signage still visible. This was real clinic once. Helping people. Now empty. Waiting. Could help people again."

    # VISUAL: Exploring. Exam rooms. Storage. Operating theater. Medical infrastructure intact.
    z "This is solid. Exam rooms can become living quarters. Operating theater for actual medical work. Storage rooms for weapons and supplies. Three floors means vertical compartmentalization."
    a "Above ground though. Visible. Echelon patrols Sector 7 regularly. Higher risk of discovery."
    z "True. But also legitimate building. Clinic reopening wouldn't be suspicious. Could blend with civilian population. Operational cover."

    # VISUAL: Finding medical equipment. Old but usable. Cabinets. Exam tables. Surgical tools.
    a "Equipment's still here. Outdated but functional. Tessa would love this. She could actually do proper medicine instead of field triage."
    z "She'd probably argue for this location hard. It's her territory. She knows the locals. They know her. That's built-in community support."
    a "That's valuable. Resistance needs locals on their side. Can't fight Echelon and local hostility simultaneously."

    # VISUAL: Noting pros and cons. Moving on. Third location.
    z "Alright. Three down. Warehouse ruins next. That one's... complicated for me."
    a "Complicated how?"
    z "(quiet) Kai and I used to operate out of that area. Lot of memories there. Good and bad. Mostly bad now."

    # TRANSITION: Journey to warehouse. Longer. Gives time for deeper conversation.
    #scene bg_lower_spans_afternoon with fade

    "Walking toward warehouse district. Afternoon now. Crowds thicker. More people. More noise. Easier to blend. Harder to talk privately. We stick to less traveled paths. Alleys. Maintenance corridors. Places where conversations stay private."

    # VISUAL: Zira quieter now. Memories surfacing. Grief showing through usual toughness.
    z "Kai loved the warehouses. Said they reminded him of possibility. Big empty spaces waiting to be filled with something better than Echelon's control."
    z "We'd sit on the roofs at night. Looking at the city. Planning escapes that never happened. Talking about futures that didn't exist."
    z "He'd say 'One day we'll fill these warehouses with people who choose to be here. Not people forced to stay. Real community. Real choice.'"

    # VISUAL: Aeron listening. Giving space. Letting her talk. Grief needs witness.
    a "He sounds like he had vision. Hope. That's rare down here."
    z "He did. Too much hope maybe. Made him reckless. Made him think he could defect without consequences. That Marcus would let him go because... because why? Because hope wins? It doesn't. Bullets win. And Marcus had more bullets."

    # VISUAL: Arriving at warehouse ruins. Partially collapsed. Massive. Empty. Haunted.
    #scene bg_warehouse_ruins with fade

    "Warehouse ruins. Massive. Five stories. Partially collapsed on east side but west side intact. Huge open spaces. Multiple levels. Catwalks. Loading docks. Storage areas. Could hold hundred people easily. Could hold army if we rebuilt it properly. Could hold everything. Or could collapse and kill everyone. Both possible."

    # VISUAL: Zira stops. Staring. Memories flooding. Pain visible now. Grief raw.
    z "(quiet) There. That catwalk. Third level. That's where we sat. Where he told me he was going to defect. Where I tried to talk him out of it."
    z "I knew it was suicide. I told him. Begged him to wait. To plan better. To let me help. He wouldn't listen."
    z "Said waiting was just slow death. That he'd rather die trying than live complying. And he did. Die trying. Marcus made sure of it."

    # VISUAL: She's shaking. Grief and rage mixing. Barely holding together.
    z "He was 23. Just 23. Had his whole life. Had potential. Had dreams. And Marcus executed him on broadcast. Made him example. Made him warning. 'This is what happens when you resist.'"
    z "I watched. They made everyone watch. Echelon streamed it everywhere. 'Traitor's death.' He was so scared but he didn't beg. Didn't give them satisfaction. Died defiant. Died brave."
    z "And I couldn't save him. Couldn't stop it. Could only watch him die and know I failed."

    # VISUAL: Tears now. Openly crying. Toughness cracked. Grief pouring through.
    "She's crying. Zira's crying. I've never seen her cry. Never seen her crack. She's always steel and sharp edges and dark humor. But right now she's just person who lost her brother. Just sister grieving. Just human breaking."

    # VISUAL: Aeron moves to her. Not touching yet. Present. Witness. Support.
    a "I'm sorry. I'm so sorry. You shouldn't have had to watch that. Nobody should."
    z "(voice breaking) Four years. It's been four years and it still feels like yesterday. Still see his face. Still hear the gunshot. Still wake up thinking maybe I can change it. Maybe I can save him. But I can't. Can never. He's just gone."

    # VISUAL: Overwhelmed. Needs something. Anchor. Connection. Proof feeling good still possible.
    z "I'm tired, Aeron. So tired of losing people. Of watching them die. Of carrying their ghosts. I'm tired of being alone with all this grief."

    # VISUAL: She looks at him. Vulnerable. Desperate. Need clear.
    z "Can I... can I try something? Just once. Just to see if feeling something good is still possible after everything."

    # VISUAL: Aeron confused but gentle. Sensing vulnerability. Being careful.
    a "Try what?"

    # VISUAL: Decision made. Impulsive. Necessary. Vulnerable.
    z "This."

    # ==============================================================
    # ZIRA KISS SCENE - Choice Point
    # ==============================================================

    # TODO: Convert kiss gating to helper getters if available (e.g., rel_value / get_flag).
    # Check if requirements met for kiss (legacy reads retained until getters exist)
    $ zira_trust = characters["zira"]["trust"]
    $ zira_loyalty = characters["zira"]["loyalty"]
    $ zira_vulnerable_scene = characters["zira"].get("vulnerability_scene_completed", False)
    
    # Calculate if player made empathetic choices during conversation
    $ empathy_shown = True  # Will be tracked by previous dialogue choices in full implementation

    # Kiss happens if trust high enough AND showed empathy
    if zira_trust >= 6 and zira_loyalty >= 8 and zira_vulnerable_scene and empathy_shown:
        jump zira_kiss_scene
    else:
        jump zira_almost_kiss_scene


# =======================================================
# ZIRA KISS - Requirements Met (EXPANDED)
# =======================================================

label zira_kiss_scene:

    # VISUAL: Zira closes distance. Kisses him. Soft. Not rushed. Intentional.
    # SOUND: Silence except breathing. City noise distant. This moment isolated.

    "She kisses me. Soft but certain. Not frantic. Not desperate. Deliberate. Her hand comes up to my chest. Not pushing away. Just resting there. Feeling heartbeat. Grounding herself in something real. Something present. Something alive."

    # VISUAL: Kiss lasting. Not quick peck. Real kiss. Tender. Meaningful. Time stretching.
    "Time stretches. Seconds becoming minutes becoming moment that exists outside normal time. Her lips soft against mine. Warm. Real. She tastes like coffee and determination and grief being held at bay. She's not pulling away. Not rushing. Just present. Just here. Just kissing me like she means it."

    # VISUAL: Her other hand moves to his shoulder. Steadying herself. Or him. Or both.
    "Her other hand finds my shoulder. Holding on. Not desperate grip. Just connection. Anchor. We're standing in ruins of her brother's dreams and she's kissing me and it feels like both ending and beginning. Like grief finding outlet. Like hope finding form."

    # VISUAL: Finally pulls back. Slowly. Not jerking away. Gentle separation. Eyes opening.
    "She pulls back slowly. Eyes still closed for beat longer. Then opening. Looking at me. Searching my face for reaction. For judgment. For rejection. For anything that says I regret this. That she shouldn't have done this."

    # VISUAL: Zira's face. Vulnerable. Scared. But also... relieved. Soft. Open.
    z "(breathless, quiet) I've been wanting to do that. For weeks maybe. Since you saved me from that crowd. Since you kept your promises. Since you became someone who made me feel less alone."

    # VISUAL: Not backing away. Still close. Hand still on his chest. Comfortable.
    z "I told myself it was just proximity. Just survival bonding. Just Kai projection. But it's not. It's you. Specifically you. The way you crack jokes when everything's terrible. The way you keep promises even when they cost you. The way you see me as person instead of weapon."

    # VISUAL: Small smile forming. Real. Not her usual dark humor shield. Genuine.
    z "I needed to know if feeling something good was still possible. But that's not the whole truth. I needed to know if feeling something good with YOU was possible. If this thing I've been feeling was real or just grief making me delusional."

    # VISUAL: Aeron's hand comes up. Gentle. Touches her face. Soft. Careful.
    a "...And? Was it real?"

    # VISUAL: Zira leaning into touch. Eyes closing briefly. Savoring comfort. Safety.
    z "(soft laugh, eyes still closed) Yeah. So real it's terrifying. I felt... not broken. Not alone. Not just surviving. Actually present. Actually human. Actually wanting something instead of just enduring everything."

    # VISUAL: Eyes opening. Looking at him. Direct. Honest. Vulnerable but unashamed.
    z "I liked it, Aeron. Not just as distraction. Not just as proof feeling good exists. I liked kissing you. Specifically. Your lips. Your presence. You."

    # VISUAL: Her hand on his chest moves slightly. Feeling heartbeat. Grounding.
    z "Your heart's racing."
    a "Yeah. Yours too. I can feel it."
    z "Scared?"
    a "Terrified. But not of this. Of screwing this up. Of not being what you need. Of failing you like I failed so many others."

    # VISUAL: Zira's expression softens. Understanding. Shared fear. Shared vulnerability.
    z "You're not going to fail me. You already haven't. You kept me alive. Kept me human. Made me believe trying again was worth it."
    z "That's not failure. That's... that's everything."

    # VISUAL: Moment stretching. Neither pulling away. Comfortable in closeness. New intimacy.
    "Standing close. Her hand on my chest. Mine on her face. Breathing synchronized. Not kissing anymore but not separating either. Just existing in this space. This moment. This new thing between us that doesn't have name but feels right. Feels real. Feels like something worth protecting."

    # VISUAL: Zira finally steps back slightly. Not fleeing. Just breathing room. Processing.
    z "(taking breath) I don't know what this means. Where this goes. If it goes anywhere. But I know I wanted it. I know I liked it. I know I'm glad it happened."
    z "And I know I feel safe with you. Comfortable. Like I can be vulnerable and you won't use it against me. That's rare. That's valuable. That's... that's important to me."

    # VISUAL: Aeron's hand drops. Giving her space. But staying close. Present.
    a "I feel it too. Whatever this is. It's real. It matters. And I'm not going anywhere."
    a "We don't have to name it. Don't have to define it. Can just let it be what it is. Something good in all this darkness. Something that makes surviving feel like living."

    # VISUAL: Zira's smile growing. Real. Warm. Rare sight. Beautiful.
    z "Look at you. Getting philosophical. Who knew Glass could talk about feelings?"
    a "I'm not Glass anymore. You keep reminding me of that. Maybe I'm starting to believe it."
    z "Good. Because Glass wouldn't have kissed me back. Wouldn't have touched my face like that. Wouldn't have made me feel like person instead of tool. You're better than Glass. Remember that."

    # VISUAL: Comfortable silence. Changed. Closer. Different kind of partnership now.
    "Silence between us but not empty. Full of everything we're not saying. Full of possibilities. Full of something that feels like hope and comfort and connection. She kissed me. I kissed her back. She liked it. I liked it. It's real. It's wanted. It's ours."

    # VISUAL: Zira glancing around warehouse. Kai's memory present but not crushing.
    z "Kai would have liked you. Would have been glad I found someone who makes me remember being human is worth it. He always said surviving wasn't enough. Had to live too. Had to feel things. Had to want things."
    z "I'm starting to understand what he meant. Starting to want things again instead of just enduring. That's because of you."

    # VISUAL: She takes his hand. Brief squeeze. Connection. Then lets go.
    z "Come on. Still two more locations to scout. Can't let personal feelings completely derail the mission. But... thank you. For being someone who makes personal feelings feel possible again."

    # VISUAL: Turning to leave. Then pauses. Looks back. Small smile.
    z "And for the record? If you want to do that again sometime... I wouldn't object. Just saying."

    # VISUAL: She leaves. Confident. Changed. Lighter somehow. Aeron following. Both changed.
    "She walks away. Confident. Not running from what happened. Not ashamed. Just acknowledging it and moving forward. And I follow. Because that's what we do. We move forward together. Changed now. Closer. Something unnamed but real between us. Something worth protecting. Something that feels like it might become everything."

    # Update relationship with deeper connection (NEW SYSTEM)
    $ rel("zira", trust=+2)
    $ mark_flag("zira.kiss_happened", True)
    $ mark_flag("zira.relationship_status", "romantic_undefined_but_wanted")
    $ mark_flag("zira.comfortable_intimacy", True)
    
    # VISUAL: They leave warehouse together. Closer. Changed. Moving forward. Comfortable.
    jump act2_15_continue_scouting


# =======================================================
# ZIRA ALMOST KISS - Requirements Not Met
# =======================================================

label zira_almost_kiss_scene:

    # VISUAL: Zira moves closer. Almost. Hesitates. Catches herself. Pulls back.
    # SOUND: Sharp breath. Moment passing. Opportunity lost.

    "She moves closer. Almost touches me. Almost closes distance. Then catches herself. Hesitates. Pulls back. Moment passing. Whatever was about to happen doesn't. Gone. Lost."

    # VISUAL: Zira stepping back. Walls back up. Vulnerability hidden again. Professional.
    z "(clears throat) Sorry. Got lost in memories. This place does that. Too many ghosts."
    a "You okay?"
    z "Yeah. Fine. Just... need to keep moving. Standing here makes it worse. Let's check the rest of the warehouse and get out."

    # VISUAL: She turns away. Moment lost. Walls rebuilt. Whatever was there hidden again.
    "She turns away. Whatever was about to happen stays buried. Maybe trust wasn't deep enough. Maybe I didn't show enough empathy. Maybe timing was wrong. Whatever the reason, the moment's gone. Might not come back."

    # VISUAL: Continue scouting. Professional. Distant. Something lost between them.
    jump act2_15_continue_scouting


# =======================================================
# CONTINUE SCOUTING - Post Emotional Beat
# =======================================================

label act2_15_continue_scouting:

    # VISUAL: Exploring warehouse. Professional assessment. Processing what happened (or didn't).
    #scene bg_warehouse_interior with fade

    "Exploring warehouse. Large spaces. Multiple levels. Good sightlines. Defensible if reinforced. Structural issues on east side but fixable. Could work. Could be perfect. Or could be where we die when ceiling collapses. Architecture's always gamble down here."

    # VISUAL: Zira back to professional. Evaluating. Taking notes. Changed or unchanged depending on kiss.
    z "Warehouse has potential. Biggest space of all options. Could hold a hundred people if we renovate. Multiple levels for different operations. Loading docks for supply deliveries."
    a "Structural instability though. East side's compromised. Would need significant reinforcement before it's safe."
    z "True. But that's engineering. That's solvable. Location's good. Near smuggling routes I know. Could get supplies in quietly. That's strategic advantage."

    # VISUAL: Noting details. Moving on. Fourth location next.
    z "Two locations left. Apartment complex is next. That's Lyra's suggestion actually. She scouted it briefly before. Liked the tactical positioning."
    a "High ground advantage. Multiple firing positions. She thinks like soldier even when she's trying not to."
    z "That's not bad thing. We need soldiers who think tactically. Especially now when we're rebuilding. Smart fighters keep everyone alive longer."

    # TRANSITION: Journey to apartment complex. Late afternoon. Processing.
    #scene bg_lower_spans_lateafternoon with fade

    "Late afternoon now. Been scouting for hours. Feet tired. Mind more tired. Processing everything. Locations. Possibilities. And what happened with Zira. Or didn't happen. Depending on which timeline we're in. Either way, something changed. Something shifted. Can't quite name it but it's there."

    # VISUAL: Arriving at apartment complex. Abandoned. Eight stories. Residential exterior. Tactical interior.
    #scene bg_apartment_complex with fade

    "Apartment complex. Eight stories. Abandoned after Purge. Building took structural damage but remained standing. Residential from outside. Just another housing block. But inside? Tactical dream. Multiple levels. Clear sightlines. Rooftop access. This is what Lyra saw. This is what her military mind recognized. Fortress disguised as apartment."

    # VISUAL: Exploring. Checking apartments. Rooms. Layout. Potential.
    z "Multiple apartments means compartmentalization. Different operations in different units. Living quarters separate from operations separate from storage. Organized."
    a "Rooftop gives observation advantage. See Echelon patrols before they see us. That's early warning system built in."
    z "Residential disguise means we blend with civilian population. Echelon patrols but doesn't inspect empty apartments aggressively. Operational security through camouflage."

    # VISUAL: Checking structure. Solid enough. Some damage but livable.
    a "Structure's good. Damage is mostly cosmetic. Foundation solid. This could work. This could really work."
    z "Lyra has good instincts. Military training showing through. She'd probably push hard for this location. Feels most like base instead of hideout."

    # VISUAL: Taking notes. Final location left.
    z "One more. Maintenance tunnels. Selene's preference. Most hidden. Most secretive. Most uncomfortable. But safest from Echelon."
    a "Let's finish this. By the time we're done we'll have complete picture. Can make real informed choice."

    # TRANSITION: Journey to maintenance tunnels. Evening approaching. Last location.
    #scene bg_lower_spans_evening with fade

    "Evening approaching. Last location. Maintenance tunnels beneath city infrastructure. Hidden. Unknown to most. Selene's choice because survival over comfort. Because hidden means alive. And alive means fighting another day. Practical. Cold. But practical."

    # VISUAL: Entering maintenance access. Hidden door. Narrow stairs. Descending into infrastructure.
    #scene bg_maintenance_tunnels with fade

    "Maintenance tunnels. City's hidden veins. Water pipes. Power conduits. Access corridors. Narrow. Damp. Industrial. Uncomfortable. But completely hidden. Not on civilian maps. Not on Echelon maps. Secret. Unknown. Safe in obscurity if not comfort."

    # VISUAL: Exploring. Tight spaces. Low ceilings. Oppressive but secure.
    z "This is as hidden as it gets. Maintenance workers come through occasionally but rarely. Could set up security to avoid them. Echelon has no reason to patrol infrastructure tunnels."
    a "It's cramped though. Uncomfortable. Long-term living here would be hard on morale. People need space. Light. Air. This is all narrow corridors and artificial lighting."
    z "But it's mobile. Tunnel network spans entire Lower Spans. Could relocate within tunnels if one location compromised. That's flexibility. That's survival advantage."

    # VISUAL: Checking access points. Multiple connections. Network extensive.
    a "Network's huge. Could set up multiple cache points. Different entrances. Never use same route twice. That's guerrilla warfare territory. Hit and fade. Never be where they expect."
    z "Exactly what Selene's thinking. She's not building conventional base. She's building network. Hidden. Flexible. Impossible to destroy completely because it's everywhere and nowhere."

    # VISUAL: Final assessments complete. All five locations scouted. Time to return.
    z "That's it. All five locations. We have complete picture now. Each has pros and cons. Each favors different strategy. Each represents different vision of what resistance becomes."
    a "Time to bring it back to group. Let everyone weigh in. This isn't just my decision or yours. It's everyone's."
    z "Agreed. Let's go home. Back to temp shelter. Present findings. Make collective choice."

    # VISUAL: Returning to surface. Evening now. Day spent scouting. Exhausted but accomplished.
    #scene bg_lower_spans_night with fade

    "Evening. Full day of scouting complete. Five locations explored. All data gathered. All possibilities assessed. Time to bring it home. Time to present findings. Time to choose foundation for everything we're building. No pressure. Just deciding where resistance lives or dies. Simple."

    # TRANSITION: Return to temp shelter. Resistance gathered. Waiting. Hoping.
    #scene bg_temp_shelter_evening with fade

    "Back to temp shelter. Everyone waiting. Selene. Lyra. Resistance fighters. All looking at us for answers. For options. For hope that we found something worth fighting for. Time to deliver."

    # VISUAL: Selene steps forward. Expectant. Hopeful. Leader waiting for intel.
    s "Report. What did you find?"
    a "Five locations. All viable. Each with different advantages and disadvantages. Each represents different strategic approach."
    s "Show us. Let's evaluate together. This decision affects everyone. Everyone gets input."

    # VISUAL: Gathering around makeshift table. Map spread out. Marking locations. Explaining options.
    # Each character will advocate for their preference based on their expertise/personality.

    # Present all five options to group
    a "Five locations. I'll walk through each one. Pros, cons, strategic considerations. Then we decide together."

    # ==============================================================
    # LOCATION PRESENTATIONS
    # ==============================================================

    # LOCATION 1: SUBWAY STATION
    a "First option: Old subway station. Deep underground. Multiple tunnel exits. Central location with access to multiple sectors."
    a "Pros: Hardest to detect. Multiple escape routes. Existing infrastructure including power and water access. Secure."
    a "Cons: No natural light. Claustrophobic. Echelon knows old subway maps. Morale impact from underground living."

    # VISUAL: Noelle steps forward. Data-driven advocacy.
    n "Mathematical analysis shows subway station has optimal connectivity index. Central hub position allows 91% coverage of Lower Spans sectors within 15-minute response time."
    n "Predictive algorithms show lowest Echelon patrol probability in tunnel networks. 8.3% chance of discovery per month versus 23-31% for above-ground options."
    n "Infrastructure analysis indicates sustainability rating of 91%. Power, water, ventilation all present. Minimal additional resource investment required."
    n "Recommendation: Subway station. Data supports this conclusion."

    # LOCATION 2: ABANDONED CLINIC
    a "Second option: Abandoned clinic. Sector 7. Three stories. Existing medical infrastructure. Above ground visibility."
    a "Pros: Medical equipment intact. Proper healing facilities. Sector 7 community connections through Tessa. Operational cover as reopened clinic."
    a "Cons: More visible. Higher Echelon patrol frequency. Single entrance creates defensive vulnerability."

    # VISUAL: Tessa steps forward. Humanitarian advocacy.
    t "The clinic lets us heal properly. Not just patch wounds but actually treat people. Trauma, surgery, recovery. Everything resistance needs to keep fighters operational."
    t "Sector 7 knows me. Locals would support us. We'd have community foundation. Can't fight Echelon while fighting local hostility."
    t "And operationally, clinic reopening isn't suspicious. Medical care's always needed. Perfect cover. We hide by helping."
    t "Count the living means keeping them alive long enough to matter. Clinic does that better than any other option."

    # LOCATION 3: WAREHOUSE RUINS
    a "Third option: Warehouse ruins. Massive space. Multiple levels. Partially collapsed but repairable."
    a "Pros: Largest space. Room for expansion. Near smuggling routes. Could hold hundred fighters eventually."
    a "Cons: Structural instability. Requires significant reinforcement. More exposed with multiple access points."

    # VISUAL: Zira steps forward. Practical advocacy with emotional undertone.
    z "Warehouse gives us room to grow. We're twelve now. Won't stay twelve. Need space for recruitment. Training. Operations. Warehouse provides that."
    z "I know the smuggling routes around that area. Can get supplies in quietly. That's strategic advantage. Logistics matter as much as location."
    z "And yes, it needs work. But we're building resistance from scratch anyway. Might as well build big. Plan for success instead of just survival."

    # If kiss happened, adds personal note
    if mark_flag("zira.kiss_happened") == True:  # safe no-op if mark_flag returns truthy; else TODO
        # TODO: If mark_flag does not return values, replace with a getter (e.g., get_flag("zira.kiss_happened"))
        z "(quieter) Plus... it's where my brother and I used to dream about real resistance. About filling empty spaces with people who chose to be there. Honoring that feels right."

    # LOCATION 4: APARTMENT COMPLEX
    a "Fourth option: Fortified apartment complex. Eight stories. Residential disguise. Tactical advantages."
    a "Pros: Multiple levels. High ground. Rooftop access for observation. Blends with civilian population. Compartmentalized operations."
    a "Cons: Civilians nearby. Risk of collateral. Limited escape routes due to vertical structure."

    # VISUAL: Lyra steps forward. Military advocacy.
    l "Apartment complex offers best defensive position. High ground advantage. Multiple firing positions. Clear sightlines for early warning."
    l "Eight stories means we control vertical space. Echelon assaults from ground level. We rain hell from above. Tactical superiority."
    l "Compartmentalization through separate apartments means operational security. Compromised unit doesn't compromise everything. Military best practice."
    l "And residential disguise works. Echelon patrols but doesn't aggressively search empty residential. We're hidden in plain sight."

    # LOCATION 5: MAINTENANCE TUNNELS
    a "Fifth option: Maintenance tunnels. City infrastructure. Hidden. Uncomfortable. Mobile."
    a "Pros: Completely unknown to Echelon. Can relocate within tunnel network. Flexible. Secret. Safe through obscurity."
    a "Cons: Cramped. Uncomfortable. Morale impact. Maintenance worker discovery risk."

    # VISUAL: Selene steps forward. Survival advocacy.
    s "Maintenance tunnels are safest. Not on any map Echelon has. Unknown. Hidden. That's security through information gap."
    s "Comfort doesn't keep you alive. Security does. Down here survival comes first. Comfort's luxury for when we've won."
    s "Network spans entire Lower Spans. We can move. Relocate. Never be pinned down. Echelon can't destroy what they can't find. That's how we outlast them."
    s "I vote tunnels. But I'm not dictator. Everyone gets input. This is collective choice."

    # ==============================================================
    # PLAYER CHOICE - BASE LOCATION
    # ==============================================================

    # VISUAL: All options presented. Advocates made their cases. Decision time.
    "Five options. Five visions. Each character advocating based on expertise and values. Noelle's data. Tessa's compassion. Zira's pragmatism. Lyra's tactics. Selene's survival. All valid. All strategic. All represent different future for resistance. Time to choose which future we build."

    menu:
        "Five locations. Five visions. Which becomes our foundation?"
        
        "Old Subway Station - Noelle's recommendation (Central, hidden, optimal data)":
            $ mark_flag("base_location", "subway")
            $ rel("noelle", affection=+2)
            $ mark_flag("bonus.intel_operations", True)
            
            a "We go with the subway station. Noelle's analysis is solid. Central location. Multiple exits. Lowest detection probability. That's strategic advantage we need."
            
            # VISUAL: Noelle pleased. Data validated. Others accepting.
            n "Logical choice. Optimal outcome probability of 87%. Higher than alternatives. You processed data correctly."
            s "Subway it is. Underground living will be hard but security matters more. We'll make it work."
            
            $ mark_flag("base_choice_reaction", "noelle_pleased")
            
        "Abandoned Clinic - Tessa's recommendation (Medical focus, community support)":
            $ mark_flag("base_location", "clinic")
            $ rel("tessa", trust=+2)
            $ mark_flag("bonus.medical_operations", True)
            
            a "We go with the clinic. Tessa's right. We need proper medical facilities. And community support in Sector 7 is invaluable strategic asset."
            
            # VISUAL: Tessa grateful. Validated. Others accepting.
            t "Thank you. We'll make it work. We'll heal people and that'll bring more people to cause. Healing's its own form of resistance."
            s "Clinic it is. More visible but Tessa knows Sector 7. That local knowledge keeps us alive. We'll make it work."
            
            $ mark_flag("base_choice_reaction", "tessa_grateful")
            
        "Warehouse Ruins - Zira's recommendation (Expansion space, smuggling access)":
            $ mark_flag("base_location", "warehouse")
            $ rel("zira", trust=+2)
            $ mark_flag("bonus.supply_operations", True)
            
            a "We go with the warehouse. Zira's right. We need room to grow. Space for recruitment and training. We're planning for success."
            
            # VISUAL: Zira surprised. Touched. Especially if kiss happened.
            z "...Thank you. We'll make it work. Reinforce structure. Build something Kai would be proud of. Something that lasts."
            s "Warehouse it is. Big gamble but big potential. We'll need construction work before it's safe. But we'll make it work."
            
            $ mark_flag("base_choice_reaction", "zira_touched")
            
            # If kiss happened, additional reaction
            if mark_flag("zira.kiss_happened") == True:  # see TODO note above re: getters
                z "(quiet, to Aeron) Thank you. For choosing this. For honoring him. Means more than you know."
            
        "Apartment Complex - Lyra's recommendation (Tactical defense, high ground)":
            $ mark_flag("base_location", "apartment")
            $ rel("lyra", trust=+2)
            $ mark_flag("bonus.defensive_operations", True)
            
            a "We go with the apartment complex. Lyra's tactical assessment is solid. Defensive advantages matter. High ground keeps us alive."
            
            # VISUAL: Lyra pleased. Validated. Proving worth beyond being "Aeron's partner."
            l "Thank you. We'll fortify it properly. Turn it into fortress. Echelon will break themselves against it if they try."
            s "Apartments it is. Tactical sense. Multiple firing positions. Good defensive foundation. We'll make it work."
            
            $ mark_flag("base_choice_reaction", "lyra_validated")
            
        "Maintenance Tunnels - Selene's recommendation (Hidden, mobile, safest)":
            $ mark_flag("base_location", "tunnels")
            $ rel("selene", trust=+2)
            $ mark_flag("bonus.stealth_operations", True)
            
            a "We go with maintenance tunnels. Selene's right. Survival first. Unknown to Echelon means safe. Everything else is secondary to staying alive."
            
            # VISUAL: Selene approving. Leadership validated. Practical choice made.
            s "Smart. Survival over comfort. That's resistance mindset. We'll make it work. We'll survive. That's what we do."
            n "Suboptimal for operations but optimal for survival. Acceptable choice given current vulnerabilities."
            
            $ mark_flag("base_choice_reaction", "selene_approving")

    # ==============================================================
    # AFTERMATH - BASE CHOSEN
    # ==============================================================

    # VISUAL: Decision made. Base chosen. Everyone processing. Relief. Direction. Purpose.
    s "Decision made. Now we move. Pack everything. Leave temp shelter. No trace left behind. We're ghosts."
    s "Tomorrow we move to new base. Tomorrow we start building for real. Tonight we rest. Because tomorrow's going to be long day."

    # VISUAL: Resistance fighters moving. Packing. Preparing. Energy different. Hope present. Direction clear.
    "Movement. Purpose. Direction. We have foundation now. Place to build from. Not just hiding. Building. That's different. That changes everything. From fugitives to resistance. From running to fighting. From surviving to planning. One base location. Changed everything."

    # VISUAL: Lyra approaches Aeron. Proud. Supportive. Team.
    l "Good scouting. You and Zira make good team. Found us real options. Made real difference."
    a "Team effort. Zira knew the territory. I just followed and took notes."
    l "Don't diminish it. You led scouting mission. Found us home. That matters. You matter. To resistance. To me. To everyone here."

    # VISUAL: Moment between them. Partnership solid. Trust deep.
    a "Thank you. For believing this would work. For being here. For choosing this with me."
    l "Always. We're in this together. Until the end. Whatever that looks like."

    # VISUAL: Zira watching from distance. Small smile. Complex emotions if kiss happened.
    if mark_flag("zira.kiss_happened") == True:  # see TODO note above re: getters
        "Zira watching from across room. Small smile. Complicated emotions. We kissed today. In warehouse ruins. In her brother's memory. Don't know what it means. But it happened. And it changed something. Made us closer. Made us something undefined but real. That's enough for now. Maybe forever. But enough."

    # VISUAL: Group settling for night. Tomorrow everything changes. Tonight they rest.
    s "Get rest. Tomorrow we move. Day after we start building. Real resistance. Real threat to Echelon. From ashes. From ruins. From twelve broken people. We build army. We build hope. We build future."
    s "Sleep well. Tomorrow we make them regret ever thinking they broke us."

    # VISUAL: Lights dimming. People settling. Night falling. Tomorrow approaching.
    "Night falling. Tomorrow we move. Tomorrow we build. Tomorrow resistance becomes real. But tonight we rest. Tonight we're just twelve people who survived another day. That's enough. That's everything. That's hope."

    # ---------------------------
    # NEW HELPER STATE UPDATES
    # ---------------------------

    # Mark scene complete and set base location variable (converted)
    $ mark_scene("base_location_chosen")
    $ mark_flag("scouting_complete", True)
    $ mark_flag("resistance_base_established", True)
    # NOTE: base_location already set via mark_flag("base_location", "...") at choice time.

    # Logs (optional breadcrumbs)
    $ log_line("scouting", "Five sites surveyed; group debate; base selected: " + str(mark_flag("base_location")))
    $ log_line("ops_bonus", "Operational bonus enabled for " + str(mark_flag("base_location")))

    # ---------------------------
    # OB/EMP ANALYSIS SNAPSHOT — Aeron
    # ---------------------------
    # Baseline: Executes structured recon under stress (OB +2); remains emotionally attuned (EMP +2).
    # Modifiers from prior scenes as available:
    # - If earlier debrief showed 'broke_promise' → EMP −1
    # - If 'showed_coldness' → EMP −1
    # - If 'casualties' == 0 → OB +1
    # - If 'casualties' > 3 → EMP +1
    #
    # TODO: Replace scenes[...] lookups with helper getters if provided by your system.

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
        context="act2_base_scouting",
        emp_delta=_emp_delta,
        ob_delta=_ob_delta,
        note="Maintains reconnaissance rigor while holding space for Zira’s grief; reframes outcomes into collective decision-making and home-building vector."
    )

    # ---------------------------
    # LEGACY→HELPER MAPPING NOTES
    # ---------------------------
    # TODO: Replace any remaining direct reads (characters[...] / scenes[...] flags) with your helper getters when available.
    # TODO: If you want faction/global reps, add: rel('resistance', rep=+N), etc.
    # TODO: If mark_flag does not return values, use your project’s getter (e.g., get_flag) where indicated above.

    return
