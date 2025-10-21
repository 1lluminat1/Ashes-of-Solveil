# act2_19_zira_night_patrol.rpy


# =======================================================
# ACT 2 - Scene 19: Zira - Night Patrol (Relationship Development)
# =======================================================


label act2_zira_night_patrol:

    # VISUAL: Base. Evening. Sun setting. People finishing daily tasks. Shift change approaching.
    # LIGHTING: Golden hour fading to twilight. Warm to cool transition.
    # SOUND: Base activity winding down. Voices quieter. Night approaching.

    #scene bg_base_evening with fade

    "{i}Evening. Base settling into night routine. Day shift ending. Night shift beginning. Guard rotations. Patrol assignments. Someone has to watch the perimeter. Someone has to make sure Echelon doesn't find us sleeping. Tonight that's someone's job. Maybe mine.{/i}"

    # VISUAL: Zira at equipment station. Checking gear. Preparing for patrol. Standard routine.
    "{i}Zira. Gearing up. Night patrol. She does this most nights. Perimeter check. Tunnel sweep. Sector surveillance. Whatever base location requires. She's good at it. Spent years doing solo operations. This is familiar territory for her. Comfortable in darkness.{/i}"

    # VISUAL: Aeron approaching. Casual. Not assigned but volunteering.
    a "Need company?"

    # VISUAL: Zira looks up. Small smile. Knows what he's doing. Appreciates it.
    z "You volunteering for night patrol? That's not your usual rotation."
    a "Can't sleep anyway. Figured I'd make myself useful. Two sets of eyes better than one."
    z "Two sets of eyes also means twice the noise. Twice the mistakes. Twice the chances to get spotted."
    a "Good thing I'm quiet. And you're skilled. We'll manage."

    # VISUAL: She's considering. Then nods. Wants the company. Won't admit it directly but body language says yes.
    z "...Fine. Grab gear. We leave in five. And keep up. I don't slow down for passengers."
    a "Wouldn't dream of asking you to."

    # VISUAL: Aeron gearing up. Light pack. Sidearm. Radio. Standard patrol equipment. Quick. Efficient.
    "{i}Gearing up. Fast. Efficient. Glass muscle memory. Some habits stick. Being prepared is one of them. Zira's watching. Evaluating. Making sure I'm not liability. I won't be. Haven't been. Won't start now.{/i}"

    # VISUAL: Ready. Both equipped. Heading to exit. Night patrol beginning.
    z "Route tonight is perimeter check, then sector sweep, then return. Three hours total if we're efficient. Four if we're careful. We're being careful."
    a "Careful works for me."
    z "Good. Let's move."

    # TRANSITION: Leaving base. Into the city. Night settling. Shadows lengthening.
    # Base location determines specific route - adjust visuals accordingly
    
    $ if base_location == "subway":
        #scene bg_subway_tunnels_night with fade
        "{i}Tunnel patrol. Underground. Dark. Damp. Sound carries differently down here. Echoes. Distortions. Easy to get disoriented. But Zira knows these tunnels. Mapped them herself. She moves like she owns them. Confident. Sure. I follow. Trust her navigation. Trust her instincts.{/i}"
        
    $ elif base_location == "clinic":
        #scene bg_sector7_streets_night with fade
        "{i}Street patrol. Sector 7. Above ground. Visible but blending with normal foot traffic. Clinic location means residential disguise. We look like residents. Just walking. Just existing. Nothing suspicious. Zira's good at this. Years of practice. I match her pace. Her posture. Her casual invisibility.{/i}"
        
    $ elif base_location == "warehouse":
        #scene bg_warehouse_district_night with fade
        "{i}Warehouse district. Industrial. Empty at night. Our footsteps echo. Plenty of hiding spots. Plenty of vantage points. Plenty of danger if Echelon patrols through. But also plenty of escape routes. Zira knows every exit. Every shortcut. Every hiding place. This is her territory. Her domain. I'm just visiting.{/i}"
        
    $ elif base_location == "apartment":
        #scene bg_apartment_rooftops_night with fade
        "{i}Rooftop patrol. Apartment complex advantage. Height. Visibility. Can see Echelon patrols blocks away. Can spot threats before they spot us. Zira moves across rooftops like she's part of them. Jumps gaps. Climbs walls. Natural. I keep up. Barely. She makes it look easy. It's not.{/i}"
        
    $ else:  # tunnels
        #scene bg_maintenance_tunnels_night with fade
        "{i}Maintenance tunnels. Deep infrastructure. Hidden. Secret. Unknown to Echelon. Zira checking access points. Making sure no maintenance workers discovered our presence. Making sure seals are intact. Making sure we're still invisible. I watch for threats. She watches for evidence. Good team.{/i}"

    # VISUAL: Patrolling together. Moving in sync. Comfortable rhythm. Professional. Efficient.
    "{i}Moving together. She leads. I follow. Sometimes I lead. She follows. No words needed. Just movement. Just awareness. Just two people who trust each other not to fuck up. That's partnership. That's what months of working together builds. Trust without speaking. Understanding without explaining.{/i}"

    # VISUAL: First checkpoint. Pause. Visual sweep. Listening. Assessing. Clear.
    z "(quiet) Clear. No Echelon presence. No unusual activity. Moving to checkpoint two."
    a "(quiet) Following."

    # VISUAL: Moving to second checkpoint. Comfortable silence. Then Zira speaks.
    z "You've been doing this more often. Volunteering for patrol. For missions. For anything that gets you out of base. Running from something or running toward something?"

    # VISUAL: Aeron considering. Honest answer. She deserves that.
    a "Running from nightmares. From sitting still. From thinking too much about the Sweep. Staying busy keeps the noise down. Keeps the ghosts quiet. Temporarily."
    z "That's not sustainable. Eventually you have to stop running and face them. The ghosts don't go away. They just wait."
    a "I know. But tonight I don't have to face them. Tonight I can just patrol. Just move. Just exist without processing. That's enough for now."

    # VISUAL: She nods. Understanding. She's done the same thing. Still does sometimes.
    z "I get it. After Kai died, I stayed moving for six months straight. Didn't stop. Didn't rest. Didn't process. Just ran. Job to job. Mission to mission. Anything to avoid sitting still and feeling it."
    z "Eventually had to stop. Eventually had to feel it. Hurt like hell. But running forever isn't living. It's just slower dying. You'll figure that out. Or you won't. But at least you're running somewhere useful. Running toward resistance instead of away from everything."

    # VISUAL: Second checkpoint. Pause. Check. Clear. Moving on.
    "{i}She's right. Running isn't solution. But running toward something is better than running away from everything. That's progress. Small progress. But progress. Maybe that's enough for now. Maybe small steps count.{/i}"

    # VISUAL: Third checkpoint approaching. Longer walk. More time to talk. Conversation natural. Easy.
    z "Recruitment's going well. Fifty-five people now. You're good at the interviews. Good at reading people. Spotting liars. Finding truth. That's valuable skill. Didn't know Glass had that."
    a "Glass didn't. Aeron does. Glass was blunt instrument. Aeron has to be precise. Has to care about people. Has to see them as individuals not targets. That's different. That's growth."
    z "Growth looks good on you. Less rigid. More human. More... present."

    # VISUAL: She glances at him. Soft expression. Affection showing. Comfortable with showing it now.
    z "I like this version better. The version that talks on patrol. The version that volunteers for company. The version that doesn't run from connection. This version's... better."

    # VISUAL: Aeron catching tone. She's talking about more than just Glass versus Aeron. About them. About what's between them.
    a "Better than the version in the warehouse? Two months ago? The version you kissed?"
    
    # VISUAL: She stops walking. Turns to face him. Direct. No deflection. Time to address it.
    z "We're really doing this? Talking about the kiss? Finally?"

    # VISUAL: Aeron stopping too. Facing her. Yeah. Time to talk about it. Been avoiding it long enough.
    a "Been two months. We've been dancing around it. Pretending it didn't happen. Or pretending it didn't matter. But it did happen. And it did matter. So yeah. We're talking about it."

    # VISUAL: She nods. Takes breath. Vulnerable. Hard for her but necessary.
    z "Okay. Fine. Let's talk about it."
    z "I kissed you in Kai's warehouse. In the place where he planned his escape. Where he told me he was defecting. Where I lost him."
    z "And I kissed you because I needed to know if feeling something good was still possible after all that loss. After all that grief. After four years of carrying his ghost."

    # VISUAL: Looking at him. Direct. Honest. Open in ways she rarely is.
    z "It wasn't just impulse. It wasn't just grief. I meant it. I'd been wanting to do that for weeks. Since you kept your promises. Since you made me feel less alone. Since you became someone who mattered."
    z "I told you that then. I still mean it now. I wanted to kiss you. I liked kissing you. And I'd want to do it again."

    # VISUAL: Pause. She's waiting. His turn. His response. His choice.
    a "I wanted to kiss you back. I did kiss you back. And I've been thinking about it for two months. About what it meant. About what we are. About what we could be."
    a "I don't know what this is. What we're doing. What we're becoming. But I know I seek you out. I know I feel calmer when you're around. I know two months later I'm still thinking about that kiss. That's something. That's not nothing."

    # VISUAL: Zira's expression softening. Small smile. Relief. Reciprocation acknowledged.
    z "Not nothing. Yeah. That's accurate. It's definitely not nothing."
    z "I don't know how to do this. Relationships. Feelings. Vulnerability. I'm good at survival, good at independence, good at solo operations. But this? This is terrifying."
    z "I lost Kai. I lost everyone I've ever cared about. Caring means losing. That's the pattern. That's what I learned. So caring again feels like volunteering for pain."

    # VISUAL: Aeron stepping closer. Not crowding. Just present. Supporting. Understanding.
    a "We're both terrified. I'm terrified of failing people. Of being Glass again. Of hurting instead of helping. That terror doesn't go away. But we function anyway. We fight anyway. We live anyway."
    a "Maybe we try this anyway. Scared. Uncertain. Damaged. But trying. Together. No pressure. No timeline. No expectations. Just... us. Whatever that becomes."

    # VISUAL: She's considering. Processing. Weighing risk versus desire. Fear versus want.
    z "No pressure. No timeline. No expectations. Just us. That's... manageable. That's something I can try."
    z "I want to try. That's the scary part. I actually want this. Want you. Specifically. Not just as proxy for Kai. Not just as convenient company. Actually you. Aeron. The person you're becoming. That person's worth trying for."

    # VISUAL: Moment stretching. Both vulnerable. Both open. Both scared. Both trying anyway.
    "{i}She wants to try. With me. Despite fear. Despite loss. Despite pattern of everyone she cares about dying. She's choosing to try anyway. That's brave. That's trust. That's... that's everything.{/i}"

    # VISUAL: They move closer. Slow. Deliberate. Testing. Checking. Mutual.
    z "So if we're trying... can I...?"

    # VISUAL: She doesn't finish sentence. Just moves closer. Hand on his chest. Looking up. Asking permission. Showing respect. Showing care.
    a "Yeah. You can."

    # ==============================================================
    # KISS SCENE - IF TRUST HIGH ENOUGH (Should be from previous scenes)
    # ==============================================================

    # Check if Zira kiss happened in Scene 9 and trust is still high
    $ if characters["zira"].get("kiss_happened", False) and characters["zira"]["trust"] >= 8:
        jump zira_second_kiss
    else:
        jump zira_no_second_kiss


label zira_second_kiss:

    # VISUAL: She kisses him. Softer than warehouse. Less desperate. More certain. More real.
    # SOUND: City noise distant. Their breathing. This moment. Connection.

    "{i}She kisses me. Softer than warehouse. Less desperate. Less proof-of-concept. More certainty. More choice. More us. Her lips warm. Familiar. Two months later and it's still 93% pleasant. Possibly 97%. Possibly everything.{/i}"

    # VISUAL: Kiss lasting. Not rushed. Comfortable. Deepening. Both present. Both choosing. Both wanting.
    "{i}Time stretches again. Different than warehouse. That was grief finding outlet. This is connection finding form. That was testing if good feelings existed. This is knowing they do and choosing them anyway. Choosing her. Choosing us. Choosing forward.{/i}"

    # VISUAL: Her hands move to his shoulders. Grounding. Anchoring. Steadying. Both of them.
    "{i}Her hands on my shoulders. Steady. Sure. Not desperate grip. Just connection. Just anchor. She's here. I'm here. We're choosing this. Scared. Uncertain. But choosing anyway. That's brave. That's trust. That's hope.{/i}"

    # VISUAL: Finally pulling back. Slowly. Gently. Eyes opening. Looking at each other. Smiling.
    z "(breathless) Okay. That was... that was good. Better than warehouse. More real. More us."
    a "Warehouse was 93% pleasant. This?"
    z "(laughs softly) This was 97% pleasant. Maybe 98%. Definitely higher. Significant statistical improvement."

    # VISUAL: She's quoting Noelle's percentage system. Making it theirs. Humor and affection mixing.
    a "You're quantifying kissing now? Noelle's rubbing off on you."
    z "Or maybe I'm just speaking your language. You've been spending a lot of late nights with her. Figured percentages might resonate."
    z "But seriously. That was good. Really good. I'm glad we did that. Glad we're trying this. Scared as hell. But glad."

    # VISUAL: Aeron touching her face. Gentle. Affectionate. Comfortable intimacy forming.
    a "I'm glad too. Scared too. But glad wins. By about 87%. Maybe 91%."
    z "Look at you. Using percentages. I've definitely corrupted you."
    a "Maybe. Or maybe you're just making me more precise about what I feel. About what I want. About this."

    # VISUAL: Moment holding. Comfortable. Close. Together. Different than two months ago. Deeper. More certain.
    z "This is nice. Just existing near you. No performance. No survival mode. Just being. I said that in the warehouse. Still true. More true now. Comfortable truth."
    a "We should probably finish patrol. Before someone notices we've been standing here for ten minutes."
    z "Probably. But I don't want to move yet. Can we just... stay here? Another minute? Just one more minute of this before we go back to being professional resistance fighters?"

    # VISUAL: Aeron pulling her closer. Brief hug. Comfort. Affection. Acceptance.
    a "One more minute. We can do that."

    # VISUAL: They stand together. City around them. Night settling. Just existing. Together. Comfortable. Real.
    "{i}Standing together. Her head against my chest. My arms around her. Just existing. Just being. No words needed. No analysis needed. Just connection. Just us. Just this. That's enough. That's everything. That's 98% pleasant. Possibly 100%.{/i}"

    # VISUAL: Eventually pulling apart. Smiling. Soft. Real. Ready to continue patrol. Changed but functioning.
    z "Okay. Patrol. Right. That's why we're out here. Definitely not just an excuse to spend time together."
    a "Definitely not. Purely professional. Very tactical. Much patrol."
    z "(laughing) You're ridiculous. Come on. Checkpoint three. Let's go before I forget what professional looks like."

    # Update relationship status
    $ characters["zira"]["trust"] += 2
    $ characters["zira"]["relationship_status"] = "romantically_involved"
    $ characters["zira"]["second_kiss"] = True
    $ characters["zira"]["comfortable_intimacy"] = True

    jump continue_patrol


label zira_no_second_kiss:

    # VISUAL: She moves closer but stops. Hesitates. Not quite ready. Pulls back slightly.
    z "Actually... not yet. I want to. But I'm not ready. Not quite. Is that okay?"

    # VISUAL: Aeron nodding. Respecting boundary. Not pushing. Understanding.
    a "That's completely okay. No pressure. No timeline. Remember? We're trying. Trying means going at your pace. Whatever that is."
    z "Thank you. For understanding. For not pushing. For being patient with my... complicated feelings about connection and loss and trying again."
    z "I want this. Want you. But I need time. Need to process. Need to trust that this is real and not just going to explode like everything else I've tried to hold onto."

    # VISUAL: Aeron reaching out. Hand on her arm. Gentle. Supportive. Present.
    a "Take all the time you need. I'm not going anywhere. And when you're ready—if you're ready—I'm here. No rush. No pressure. Just here."
    z "You're good at this. The patience thing. The understanding thing. Most people wouldn't wait. Wouldn't give space. Wouldn't accept 'not yet' without getting frustrated."
    a "Most people aren't trying to build something real with someone who's worth waiting for. You're worth waiting for. So I wait. That's easy math."

    # VISUAL: She smiles. Grateful. Relieved. Still close. Still comfortable. Just not kissing. And that's okay.
    z "Okay. Let's finish patrol. And maybe we can talk more. Keep trying. Keep figuring this out. Just... slowly. At my pace."
    a "Your pace is perfect. Let's go."

    # Update relationship - deepening but slower
    $ characters["zira"]["trust"] += 1
    $ characters["zira"]["relationship_status"] = "deepening_slowly"
    $ characters["zira"]["respects_boundaries"] = True

    jump continue_patrol


label continue_patrol:

    # VISUAL: Continuing patrol. Moving to checkpoint three. Both changed by conversation. Closer. More certain.
    "{i}Moving again. Patrol continuing. But different now. We talked. We addressed it. We're trying. Together. That changes everything. Makes patrol feel less like duty and more like time together. Makes night feel less heavy. Makes future feel less impossible.{/i}"

    # VISUAL: Third checkpoint. Visual sweep. Listening. Clear. No threats. Safe. For now.
    z "Clear. Final checkpoint coming up. Then we loop back to base. Hour left on patrol."
    a "Want to take the long route? Enjoy the night air? No rush to get back?"
    z "You asking to extend patrol time or asking to spend more time with me?"
    a "Can't it be both?"

    # VISUAL: She grins. Knowing. Pleased. Happy. Rare sight. Beautiful.
    z "Yeah. It can be both. Long route it is."

    # VISUAL: Taking scenic route. Slower pace. More conversation. Comfortable. Natural.
    z "You know what's weird? This. Us. Patrolling together. Talking about feelings. Trying relationship. A year ago I was solo operator. Alone. Independent. Self-sufficient. Preferred it that way."
    z "Now? Now I'm choosing partnership. Choosing connection. Choosing to be not-alone. That's huge shift. Terrifying shift. But good shift. I think."

    # VISUAL: Aeron listening. Understanding. He's made similar shifts.
    a "Year ago I was Glass. Perfect soldier. No emotions. No connections. No humanity. Alone in different way. Surrounded by people but isolated. Empty."
    a "Now I'm Aeron. Imperfect human. Processing emotions. Building connections. Finding humanity. Surrounded by people and actually connected. Full. Ish. Getting fuller."
    a "So yeah. Huge shifts. Terrifying shifts. But good shifts. Definitely good shifts."

    # VISUAL: Walking together. Close. Comfortable. Natural proximity. Partnership visible.
    z "We're both works in progress. Both learning. Both fucking up. Both trying anyway. That's... that's beautiful. In messy, complicated, very human way. Beautiful."
    a "You just called us beautiful. That's poetic. You're never poetic."
    z "Shut up. I'm having a moment. Let me have the moment."
    a "(laughing) Moment granted. Continue being poetic. It's nice."

    # VISUAL: She laughs too. Comfortable humor. Affection. Ease. This is what connection looks like. Simple. Real. Easy.
    "{i}Laughing together. On patrol. In middle of night. In middle of war. In middle of complicated attempt at relationship. And it's easy. Natural. Good. That's what she meant by beautiful. This. Us. Trying. Succeeding. Being human together. Yeah. That's beautiful.{/i}"

    # VISUAL: Fourth checkpoint. Final location. Clear. Patrol complete. Time to return.
    z "Final checkpoint clear. Patrol complete. Time to head back. Four hours instead of three. Careful and scenic. Mission accomplished."
    a "Best patrol I've been on."
    z "Because nothing happened or because I was here?"
    a "Yes."
    z "(smiling) Good answer. Come on. Let's go home."

    # VISUAL: Returning to base. Together. Changed. Relationship defined. Moving forward. Together.
    "{i}Returning to base. Patrol complete. But more than patrol completed. We talked. We addressed the kiss. We're trying. Together. Undefined but real. Complicated but wanted. Scared but moving forward. That's relationship. That's us. That's enough.{/i}"

    # TRANSITION: Arriving back at base. Late night. Quiet. People sleeping. Just them. Moment before separating.
    #scene bg_base_night_late with fade

    # VISUAL: Arriving at base entrance. Moment before going inside. Before returning to separate quarters. Pause.
    z "Thank you. For volunteering. For company. For talking. For trying. For being patient. For being you. Tonight was good. Really good."
    a "Thank you for letting me come. For talking. For trying. For being honest. For being you. Tonight was perfect."
    z "Not perfect. We're too messy for perfect. But good. Definitely good. 97% good. Maybe 98%."
    a "(smiling) There's the percentages again. I've definitely corrupted you."
    z "Or you've just taught me precision. About what I feel. About what I want. About this."

    # VISUAL: Brief moment. Close. Intimate. Then pulling back. Professional again. For now.
    z "Good night, Aeron. See you tomorrow. Same time for patrol?"
    a "Same time. Same partner. Looking forward to it."
    z "Me too. Definitely me too."

    # VISUAL: She leaves. Heading to quarters. Glancing back once. Smiling. Then disappearing into base.
    "{i}She's gone. Heading to quarters. But not really gone. Still here. Still present. Still trying. Still choosing us. That matters. That's everything. Tonight we talked. We kissed. We tried. We moved forward. That's progress. That's hope. That's us.{/i}"

    # VISUAL: Aeron standing alone. Night quiet. Base sleeping. But he's not alone. Not really. Connected now. Committed now. Trying now.
    "{i}Alone but not lonely. Connected but not trapped. Trying but not forcing. That's balance. That's healthy. That's what relationship should be. And we're building it. Slowly. Carefully. Honestly. Together. That's enough. That's everything. That's 98% pleasant. Possibly 100%.{/i}"

    # Mark scene complete
    $ scenes["zira_night_patrol"] = True
    $ characters["zira"]["patrol_partner"] = True
    $ canon["zira_relationship_defined"] = True

    # TRANSITION: Night ending. Tomorrow coming. Relationship continuing. Forward momentum.
    scene black with fade

    return

    # canon_note: Scene 13 complete - Zira night patrol, relationship deepening
    # canon_note: Warehouse kiss addressed explicitly (two months later, finally talked about it)
    # canon_note: Second kiss (if trust high) - softer, more certain, 97-98% pleasant
    # canon_note: OR boundary respected (if not ready) - patience, understanding, trust building
    # canon_note: Zira vulnerability - "caring means losing" fear, choosing to try anyway
    # canon_note: Relationship defined: "trying, no pressure, no timeline, just us"
    # canon_note: Comfortable intimacy established - humor, affection, ease together
    # canon_note: Partnership visible - patrol together, trust each other, natural rhythm
    # canon_note: Percentage system callback - making Noelle's language their own
    # canon_note: Growth acknowledged - both works in progress, both trying, both succeeding
    # canon_note: Romance path solidified (if second kiss) or deepening slowly (if not)
    # canon_note: Sets up committed relationship going forward (Scene 20 commitment scene later)
    # canon_note: Theme: Choosing forward despite fear, trying despite loss, connection despite risk