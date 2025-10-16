# act1_18_confession_with_lyra.rpy


# =======================================================
# ACT 1 - Scene 18: Confession with Lyra - The Breakdown
# =======================================================


label act1_confession_lyra:

    # VISUAL: Aeron's apartment. Late afternoon light. Door opens—Aeron enters.
    # LIGHTING: Warm amber through window, but cold inside. Contrast = disconnection.
    # SOUND: Door closing; his breathing; footsteps stopping.

    "{i}The door seals behind him. The room is too quiet.{/i}"
    "{i}And Lyra is there. Sitting on his bed. Waiting.{/i}"

    # VISUAL: Lyra sits on edge of bed—posture perfect, but eyes worried.
    # She stands when she sees him. Takes in his appearance.

    l "Aeron."

    # VISUAL: Aeron stops just inside. Still in tactical gear. Blood on uniform (not his).
    # His hands hang at his sides. Trembling slightly. Eyes hollow.

    "{i}He stands there. Can't move forward. Can't turn back.{/i}"
    a "{i}She's here. Why is she here?{/i}"
    a "{i}I can't—I can't let her see—{/i}"

    l "(steps closer) I heard about the mission. Sector 10."
    a "(voice flat) It's done. Mission complete."
    l "That's not what I asked."

    # VISUAL: She stops a few feet away. Reads his body language—rigid, breaking.
    l "(softer) What happened down there?"

    # PHASE 1: TRYING TO HOLD GLASS TOGETHER

    a "Sweep operation. Standard protocol. Within parameters."
    l "Aeron—"
    a "800 targets. Sector secured. Marcus is satisfied."
    l "Stop."
    a "Mission complete. That's all—"
    l "(steps closer) Stop reporting and talk to me."

    # VISUAL: His jaw clenches. Hands shake harder. He's fighting it.
    "{i}Glass doesn't break. Glass reports. Glass functions.{/i}"
    a "(strained) I'm fine. Just tired. I need to—"

    # VISUAL: She touches his shoulder—gentle, grounding.
    # He FLINCHES like he's been struck. Pulls back.

    a "(sharp) Don't—"
    l "(quiet) Aeron. Look at me."

    # VISUAL: He can't. His eyes stay on the floor.
    a "{i}If I look at her, it's over. The dam breaks.{/i}"
    a "{i}Glass doesn't break. Glass stays whole. Glass—{/i}"

    l "(barely a whisper) How many?"

    # PHASE 2: CRACKS SPREADING

    # VISUAL: His hands curl into fists. Shaking visible now.
    a "...The report says 800."
    l "I didn't ask what the report says. I asked how many YOU killed."

    # VISUAL: His breath catches. Words stick in his throat.
    a "(voice breaking) I—I tried to—"

    l "How many, Aeron?"

    # VISUAL: He looks up. His eyes meet hers. And she sees it—the horror, the guilt, the breaking.
    if evidence_of_mercy >= 2:
        a "...600. Maybe more. I saved some. I tried. But—"
    else:
        a "...All of them. I killed all of them."

    l "(breathes in sharply) Aeron..."

    # PHASE 3: THE FLOOD BEGINS

    a "There was a vendor. I bought coffee from him. Three days ago."
    a "He recognized me. He knew I'd come. He didn't run."
    
    if aeron_saved_vendor:
        a "I let him go. I broke protocol. I just—I couldn't—"
        a "The team saw. They questioned it. But I let him live."
    else:
        a "I killed him. Three rounds. Center mass. Professional."
        a "He died reaching for his brew pot. Said it was better than Aeries coffee."
        a "And I—I remembered the taste—and I killed him anyway—"

    # VISUAL: His voice rising. Hands shaking harder. Breath coming faster.

    a "And there was a child. Just a child. Hiding behind a door."
    
    if aeron_saved_child:
        a "I lied to the team. Said thermal was a glitch. Left her alive."
        a "But how many others? How many children didn't get that mercy?"
    else:
        a "My team breached. I heard her scream. And then—"
        a "Eight years old. No weapon. Just terrified."
        a "And we killed her. I killed her."

    # VISUAL: His breathing ragged now. Hyperventilating. Words tumbling out.

    a "There were 200 people in a shelter. Families. Children. Elders."
    a "I heard them through the door. Breathing. Waiting. Trusting dawn would come."
    
    if aeron_saved_shelter:
        a "I warned them. Flashbang. Gave them time to scatter. They ran."
        a "150 escaped. But 50—50 didn't make it—"
        a "I can see their faces. The ones who fell. The ones too slow—"
    else:
        a "We breached. Charges. Smoke. And then—"
        a "200 people. Gone. In minutes. Efficient. Clean. Perfect."
        a "I saw them. The old man. The families around fires. The children—"

    # VISUAL: His voice breaking completely now. Tears starting.

    a "They weren't rebels. They weren't threats. They were just—"
    a "They were just trying to survive. And Marcus said—"
    a "He said 'prove your worth.' So I did. I proved—"

    # VISUAL: His legs give out. He stumbles. Catches himself on the desk.
    "{i}His knees buckle. He catches the desk. Barely standing.{/i}"

    l "(moving to him) Aeron—"
    a "(voice rising) I've done this 390 times. THREE HUNDRED AND NINETY."
    a "How many children? How many families? How many people just like them?"
    a "How many times did Marcus lie and I believed him?"
    a "'Organized resistance.' 'High-value targets.' 'Acceptable collateral.'"
    a "They were LIES. All of them. And I—I just—"

    # PHASE 4: COMPLETE BREAKDOWN

    # VISUAL: He collapses. Knees hit floor. HARD. Doesn't feel it.
    "{i}He falls. Crashes to his knees. The impact doesn't register.{/i}"

    a "(screaming) I KILLED THEM—"

    # VISUAL: Hands cover his face. Body shaking violently.
    # SOUND: Raw, ugly sobbing. Not quiet. LOUD. Broken. Choking.

    "{i}Ten years of silence shatters.{/i}"
    "{i}Ten years of Glass cracks wide open.{/i}"
    "{i}And the flood pours out.{/i}"

    a "(sobbing) I'm sorry—I'm sorry—I'm so sorry—"
    a "I tried—I tried to save them—but it wasn't enough—"
    a "It's never enough—it's NEVER—"

    # VISUAL: He's hyperventilating. Can't breathe. Chest heaving.
    "{i}He can't breathe. Air won't come. Chest crushes. Lungs scream.{/i}"

    a "(gasping) I can't—I can't breathe—there's blood—everywhere—"
    a "On my hands—on my uniform—in my head—I can't—"

    # VISUAL: Lyra drops beside him. On the floor. Doesn't hesitate.
    # Her arms wrap around him—not romantic. Just human. Just holding.

    l "(quiet) Breathe. Just breathe. I'm here."

    # VISUAL: He collapses against her. Full weight. Can't hold himself up.
    # Sobs wracking his entire body. Violent. Uncontrolled.

    a "(barely coherent) How do you—how do you live with it—"
    a "How do you—breathe—after—after—"
    a "I see their faces—every time I close my eyes—"
    a "The child—the vendor—the families—all of them—"

    # VISUAL: His hands clutch at his chest. Clawing. Like he can rip the guilt out.
    "{i}His hands claw at his chest. Trying to tear it out. The guilt. The horror.{/i}"

    a "I'm not Glass—I'm not—I can FEEL it—"
    a "Every death—every face—every person I—"
    a "(screaming) I DON'T WANT TO BE THIS ANYMORE—"

    # PHASE 5: LYRA BREAKS WITH HIM

    # VISUAL: Lyra's composure cracks. Her eyes fill. Her breath catches.
    "{i}Lyra's mask shatters. Tears stream. She can't hold it either.{/i}"

    l "(voice breaking) I know. I know. I've done it too."
    l "Sector 7. Before the gala. Compliance audit."
    l "I found children. Families. Just surviving."
    l "And I—I logged them. Reported them. Did my duty."
    l "(crying) Three days later they were gone. Relocated. Erased."
    l "I told myself it was necessary. That the system knew better."
    l "(sobbing) But I can't stop seeing their faces either."

    # VISUAL: She holds him tighter. Both of them shaking. Both crying.
    "{i}She holds him. And breaks with him. Two pieces of Glass shattering together.{/i}"

    l "We're not Glass. We were never just Glass."
    l "We're human. And humans feel. And it HURTS."
    l "(through tears) But feeling it means we're still alive."

    a "(sobbing into her shoulder) I can't—I can't do this anymore—"
    a "I can't be his weapon—I can't kill for him—I can't—"
    l "Then don't. You don't have to."
    a "He OWNS me—the system owns me—I can't—"
    l "(fierce) Then we break free. Together."

    # VISUAL: They sit on the floor. Holding each other. Both crying.
    # Time stretches. Minutes? Hours? Doesn't matter.

    "{i}They sit in the ruins of Glass. Both shattered. Both bleeding.{/i}"
    "{i}Time dissolves. Just breath. Just tears. Just being human.{/i}"

    # VISUAL: His sobs gradually quiet. Exhaustion taking over.
    # Breathing slows. Tears still falling but softer now.

    "{i}The storm passes. Slowly. Like bleeding out.{/i}"
    "{i}His sobs fade to shudders. Breath steadies. Body exhausted.{/i}"

    # PHASE 6: AFTER THE STORM

    # VISUAL: They sit against the wall now. Side by side. Faces wet. Eyes hollow.
    # Silence except breathing. Neither has words left.

    "{i}Silence settles. Not peace. Just emptiness after the flood.{/i}"

    l "(hoarse) How do you feel?"
    a "(barely audible) ...Empty."
    l "Good."
    a "...What?"
    l "You needed to be empty. To drain the poison."
    l "Ten years of holding it in. You couldn't carry it anymore."

    # VISUAL: He looks at her. Eyes red. Face streaked. Broken.
    a "I killed 600 people today."
    l "I know."
    a "How do I live with that?"
    l "(quiet) I don't know. But maybe... we learn together."

    # VISUAL: She takes his hand. Holds it. Not romantic. Just grounding.
    "{i}Her hand finds his. Holds tight. Anchor in the void.{/i}"

    l "You tried to save them. That's more than Glass would do."
    a "I didn't save enough."
    l "No one could have."
    a "Then what was the point?"
    l "(looks at him) The point is you TRIED. You fought the orders from within."
    l "You warned them. You faked reports. You showed mercy."
    l "That's not Glass. That's human."

    # VISUAL: His eyes close. Tears still leaking. Exhaustion crushing.
    a "I'm so tired, Lyra."
    l "I know."
    a "I don't know how to keep going."
    l "Then don't. Not tonight."
    l "(softer) Tonight, just breathe. Just exist."
    l "Tomorrow we figure out what comes next."

    # VISUAL: He leans his head back against wall. Completely spent.
    a "What if I can't be fixed?"
    l "Then we're broken together."
    l "(squeezes his hand) Glass recognizes glass. Remember?"
    l "But we're not Glass anymore. We're just... us."
    l "Broken. Guilty. Human."

    # VISUAL: They sit in silence. City lights through window. Time passes.
    "{i}They sit. The city hums beyond the glass. Neither moves.{/i}"
    "{i}Both too exhausted. Both too broken. Both too human.{/i}"

    a "(barely a whisper) Thank you."
    l "For what?"
    a "For being here. For not running. For..."
    a "...for seeing me. Not Glass. Me."
    l "(tears falling again) I see you. I've always seen you."
    l "Even when you couldn't see yourself."

    # VISUAL: She shifts closer. Her head rests on his shoulder.
    # Not romantic. Just exhausted humans holding each other up.

    "{i}She leans against him. He doesn't pull away.{/i}"
    "{i}Two pieces of broken glass, holding each other together.{/i}"

    l "We'll get through this."
    a "How can you be sure?"
    l "I'm not. But we'll try."
    l "(soft) And trying is all we have left."

    # VISUAL: Window shows evening deepening. Time passing. They don't move.
    "{i}Evening falls. The room darkens. Neither moves to turn on lights.{/i}"
    "{i}Just sitting. Just breathing. Just surviving the moment.{/i}"

    a "{i}Operation 391 is complete.{/i}"
    a "{i}Glass shattered on the floor of my apartment.{/i}"
    a "{i}And for the first time in ten years... I felt it all.{/i}"
    a "{i}Every death. Every face. Every crack.{/i}"
    a "{i}I'm not Glass anymore. I don't know what I am.{/i}"
    a "{i}But Lyra's here. And that's enough. For now.{/i}"

    # VISUAL: Hold on them sitting together. Broken but not alone.
    # SOUND: Breathing. City hum. Silence between.

    "{i}They sit in the ruins of who they were.{/i}"
    "{i}Neither knows what comes next.{/i}"
    "{i}But they're not facing it alone.{/i}"

    # TRANSITION: Slow fade. Time passes. Evening to night.
    # TEXT: "Midnight. Obsidian Bridge."

    # canon_note: Aeron's complete emotional breakdown—10 years released
    # canon_note: Lyra breaks with him—shared shattering, not fixing
    # canon_note: First time admitting "I don't want to be this anymore"
    # canon_note: Lyra confesses her own guilt (Sector 7 children)
    # canon_note: "Glass recognizes glass" becomes "we're not Glass anymore, just us"
    # canon_note: Not romantic (yet)—just two broken humans surviving together
    # canon_note: Sets up Obsidian Bridge—both changed, both ready to defy
    # canon_note: evidence_of_mercy determines what he confesses (saved some vs killed all)

    return