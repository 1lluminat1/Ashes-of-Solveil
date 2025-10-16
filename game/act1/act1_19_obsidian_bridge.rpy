# act1_19_obsidian_bridge.rpy


# =======================================================
# ACT 1 - Scene 19: Obsidian Bridge - Zira's Judgment
# =======================================================


label act1_obsidian_bridge:

    # VISUAL: Obsidian Bridge—massive structure spanning the gap between Mid and Lower tiers.
    # LIGHTING: Cold blue moonlight; neon reflections in dark water below; fog rolling through.
    # SOUND: Wind howling through steel; distant machinery; water rushing far below.

    "{i}Midnight. The Obsidian Bridge stretches into fog and darkness.{/i}"
    "{i}Below, the city's underbelly churns. Above, the Aeries glow with ignorant light.{/i}"
    "{i}And here, between them, the forgotten meet.{/i}"

    # VISUAL: Aeron stands at the bridge's midpoint. Alone. Exhausted.
    # Still in tactical gear (cleaned, but the weight remains). Hollow eyes.

    a "{i}She said midnight. If I fought for them, she'd be here.{/i}"
    a "{i}If I just followed orders... don't bother coming.{/i}"
    
    if evidence_of_mercy >= 2:
        a "{i}I tried. I saved who I could. 200 people alive because Glass cracked.{/i}"
        a "{i}But 600 dead. 600 faces I can't unsee.{/i}"
        a "{i}Is that enough? Does trying count when you still kill hundreds?{/i}"
    elif evidence_of_mercy >= 1:
        a "{i}I tried. Not hard enough. Saved maybe 50. Killed 750.{/i}"
        a "{i}Glass won. Mostly. But I fought it. A little.{/i}"
        a "{i}Is that enough?{/i}"
    else:
        a "{i}I followed orders. Perfect execution. 800 dead. Zero mercy.{/i}"
        a "{i}Glass didn't crack. Glass obeyed.{/i}"
        a "{i}She won't come. Why would she?{/i}"

    # VISUAL: Wind picks up. Fog swirls. Footsteps approach from shadow.
    # SOUND: Boots on metal grating. Confident. Unhurried.

    "{i}Footsteps. She's here.{/i}"

    # VISUAL: Zira emerges from fog—hood up, face half-shadowed, eyes sharp.
    # She stops ten feet away. Studies him. Reads everything.

    z "Glass."

    # VISUAL: Aeron turns. Looks at her. Doesn't hide the exhaustion. The breaking.
    a "Zira."

    # VISUAL: She tilts her head. Takes in his appearance—the blood, the trembling hands, the hollow eyes.
    z "(quiet) You look like hell."
    a "I've been there. Just got back."

    # VISUAL: Silence. Wind fills the space. She's waiting.
    z "Tell me what happened."

    # BRANCHING BASED ON EVIDENCE_OF_MERCY

    if evidence_of_mercy >= 3:
        # HIGH MERCY PATH - Saved 150+, showed significant resistance
        
        a "I completed the mission. Sector 10 swept."
        z "That's not what I asked."
        a "(looks at her directly) I saved who I could."
        
        # VISUAL: Zira's expression shifts—surprise, then respect.
        z "How many?"
        a "Official report says 800 eliminated. Zero survivors."
        z "(steps closer) And the truth?"
        a "...200 alive. Maybe more. I warned them. Faked reports. Let people escape."
        a "The vendor you saw me meet. I let him run."
        a "The child behind the door. I lied to my team. Left her alive."
        a "The shelter with 200 people. I scattered them. 150 escaped."
        
        # VISUAL: Zira's eyes widen slightly—genuine surprise.
        z "You lied to Marcus Rylan. Your father."
        a "I did."
        z "Your team saw you show mercy."
        a "They did."
        z "You risked everything."
        a "(quiet) I risked nothing. They had everything to lose."
        
        # VISUAL: Zira studies him for a long moment. Then nods slowly.
        z "(respect in her voice) You fought the orders from within."
        z "That's not Glass. That's human."
        
        $ zira_rel += 3
        $ zira_trusts_aeron = True
        
        a "600 people still died."
        z "Yes. They did."
        a "Is that supposed to make me feel better? That I 'tried'?"
        z "(steps closer) No. It's supposed to make you remember you're not a machine."
        z "Glass doesn't try. Glass obeys perfectly."
        z "You tried. You failed to save them all. And that makes you human."
        
        # VISUAL: She extends her hand—offering something.
        # PROP: Encrypted comm device. Small. Civilian tech.
        z "You wanted intel. Data. Ways to see what's really happening."
        z "(places device in his hand) This connects you to my network."
        z "Encrypted. Untraceable. Use it when you're ready to do more than try."
        
        a "(looks at device) What am I supposed to do with this?"
        z "Whatever you want. Information is power."
        z "Right now, you're blind. Marcus feeds you lies. You follow."
        z "With this, you see the truth. And then you choose."
        
        # VISUAL: He closes his hand around the device. Nods once.
        a "Why are you helping me?"
        z "(slight smile) Because 200 people are alive today who shouldn't be."
        z "Because Glass cracked. And cracks let light through."
        z "(serious) And because something bigger is coming. Soon."
        
    elif evidence_of_mercy >= 1:
        # MODERATE MERCY PATH - Saved 50-150, showed some resistance
        
        a "I completed the mission."
        z "I know. My network tracked everything."
        a "(tense) Then you know what I did."
        z "I know you tried. Not enough. But you tried."
        
        # VISUAL: Zira crosses her arms. Not hostile. Just measuring.
        z "You saved what, 50? Maybe 100?"
        a "I don't know. I lost count."
        z "You let some escape. Faked some reports. Showed mercy when you could."
        z "But you also followed orders. Killed hundreds. Did your duty."
        
        $ zira_rel += 1
        $ zira_trusts_aeron = False
        
        a "(defensive) I couldn't save them all. The team was watching. Marcus was—"
        z "(cuts him off) I'm not judging. I'm observing."
        z "You're caught between two worlds. Glass and human."
        z "One foot in obedience. One foot in resistance."
        z "(leans in) That's dangerous. For you and for anyone near you."
        
        a "What do you want me to say? That I should have done more?"
        z "I want you to decide what you are."
        z "Glass follows orders. Humans resist. You did both."
        z "That makes you either a liability or an asset. I haven't decided which."
        
        # VISUAL: She pulls out encrypted comm device. Holds it. Doesn't hand it over yet.
        z "I came here to give you this. Access to my network."
        z "But I'm not sure you're ready."
        
        a "What do I have to do to prove I'm ready?"
        z "(studies him) Stop trying to be both. Choose."
        z "(tosses device—he catches it) Use that when you've decided."
        z "If you want to be Glass, delete it and never contact me again."
        z "If you want to be human, use it to see what's really happening."
        z "But don't waste my time with half-measures. Next time, commit."
        
    else:
        # LOW MERCY PATH - Saved <50, mostly followed orders
        
        a "The mission is complete. Sector 10 is cleared."
        z "(cold) I know."
        a "Then why ask?"
        z "Because I wanted to hear you say it."
        z "I wanted to see if you'd lie. Or if you'd own what you did."
        
        # VISUAL: She steps closer. Eyes hard. Voice sharp.
        z "800 people. Gone. You followed orders perfectly."
        z "Glass at its finest. Efficient. Obedient. Empty."
        
        $ zira_rel -= 2
        $ zira_trusts_aeron = False
        
        a "(quiet) I did what I had to—"
        z "(cuts him off) No. You did what Marcus told you to."
        z "There's a difference. And you chose not to see it."
        
        # VISUAL: Aeron's jaw tightens. Anger flashing.
        a "I came here. Doesn't that count for something?"
        z "Why? To prove you feel bad? To get absolution?"
        z "(harsh) I'm not a priest. And you don't get to feel better."
        z "800 people are dead. And you want a pat on the back for showing up?"
        
        a "(tense) Then why are you here?"
        z "(pause) Because I'm an optimist. And an idiot."
        z "I thought maybe—MAYBE—you'd surprise me."
        z "I thought Glass might crack. That you'd fight back. Even a little."
        z "(bitter) I was wrong."
        
        # VISUAL: She turns to leave. Stops. Looks back.
        z "You know what the difference is between you and the vendor you killed?"
        a "..."
        z "He chose to stay. To keep people warm. To survive with dignity."
        z "You chose to be a weapon. And weapons don't get redemption."
        
        # VISUAL: She walks away. Stops after ten steps.
        z "(over shoulder) If you ever decide to be human instead of Glass..."
        z "Don't look for me. I won't be waiting."
        
        # VISUAL: She disappears into fog. Gone.
        a "{i}She's gone. And she's right.{/i}"
        a "{i}I chose Glass. Again. Like always.{/i}"
        a "{i}800 people dead. And I learned nothing.{/i}"
        
        # Jump to rooftop scene (no device, no hope)
        jump act1_rooftop_reflection

    # CONTINUING HIGH/MODERATE MERCY PATHS ONLY

    # VISUAL: Zira leans against the rail. Looks out at the city below.
    z "Something's happening. Big. Soon."
    a "What do you mean?"
    z "Energy grid anomalies. Troop movements. Lockdowns being prepared."
    z "Sectors 8, 9, and 10. All at once."
    
    # VISUAL: Aeron's expression darkens. Realization hitting.
    a "Sector 10 was just the start."
    z "Exactly. Your sweep was prep work."
    z "Clearing 'troublemakers' before the main event."
    a "(quiet) How big?"
    z "Hundreds of thousands. Maybe more."
    z "I don't have details. But it's coming. Days, not weeks."
    
    # VISUAL: Aeron's hands grip the rail. Knuckles white.
    a "{i}Hundreds of thousands. And I just killed 800 as practice.{/i}"
    a "{i}What have we become?{/i}"
    
    z "That's why I'm telling you. That's why I'm giving you access."
    z "You can't stop what's coming alone. But you can see it."
    z "And maybe—MAYBE—you can save someone when it happens."
    
    if evidence_of_mercy >= 3:
        z "(softer) You saved 200 today. That's 200 reasons to keep trying."
        z "Next time, save more."
    else:
        z "You half-committed today. Next time, pick a side."
        z "Because half-measures get everyone killed."

    a "Why do you care? About me, I mean."
    z "(pause) Because you're Marcus Rylan's son."
    z "Because you have access. Intel. Resources."
    z "Because if Glass cracks wide enough, you could actually help."
    z "(looks at him) And because 200 people are breathing right now who shouldn't be."
    z "That's not nothing."
    
    # VISUAL: Wind picks up. Fog thickens. City hums below.
    z "Go home. Rest. Recover."
    z "When you're ready to do more than try, use that device."
    z "I'll be watching."
    
    # VISUAL: She turns to leave. Stops.
    z "(over shoulder) And Glass?"
    a "Yeah?"
    z "You broke today. I saw it. That's good."
    z "Broken things can be rebuilt. Glass can't."
    z "Figure out which one you want to be."
    
    # VISUAL: She disappears into fog. Gone.
    "{i}She's gone. The device weighs heavy in his hand.{/i}"

    a "{i}She's right. I'm caught between Glass and human.{/i}"
    a "{i}Today I tried to be both. And 600 people died anyway.{/i}"
    a "{i}But 200 lived. That has to mean something.{/i}"
    a "{i}Doesn't it?{/i}"

    # VISUAL: He looks at the device. Small. Civilian. Dangerous.
    a "{i}Information is power, she said.{/i}"
    a "{i}Power to see. Power to choose. Power to resist.{/i}"
    a "{i}Or power to get everyone killed.{/i}"

    # VISUAL: He pockets the device. Turns toward Aeries.
    a "{i}Something bigger is coming. Hundreds of thousands.{/i}"
    a "{i}And I'm standing here with blood on my hands and a comm device in my pocket.{/i}"
    a "{i}What the hell am I supposed to do with that?{/i}"

    # VISUAL: City lights pulse below. Fog swallows the bridge.
    "{i}The city breathes. Unaware. Unsuspecting.{/i}"
    "{i}And Glass, broken but walking, heads home.{/i}"

    # TRANSITION: Fade to black.
    # TEXT: "The next evening. Rooftop."

    # canon_note: Zira's reaction scales with evidence_of_mercy (0-3+)
    # canon_note: High mercy = trust, device given freely, partnership begins
    # canon_note: Moderate mercy = conditional trust, device given with warning
    # canon_note: Low mercy = rejection, no device, Zira leaves
    # canon_note: Warning about "something bigger" = foreshadows Purge
    # canon_note: "Days, not weeks" = creates urgency
    # canon_note: Device = key tool for Act 2, access to resistance network
    # canon_note: "Broken things can be rebuilt, Glass can't" = thesis statement

    return