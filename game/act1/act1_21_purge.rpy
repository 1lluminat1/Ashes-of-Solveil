# act1_21_purge.rpy

# =======================================================
# ACT 1 - Scene 21: Rooftop Reflection → The Purge
# =======================================================

label act1_purge:

    # Pull live counters & soft flags (BC-safe)
    $ sv = int(player_state.get("civilians_saved", 0))
    $ kv = int(player_state.get("civilians_killed", 0))
    $ em = int(player_state.get("evidence_of_mercy", 0))

    # What (if anything) Aeron actually spared in 17
    $ saved_vendor  = check_scene_flag("act1_17_sweep","ordered_vendor_run") or check_scene_flag("act1_17_sweep","saved_vendor")
    $ saved_child   = check_scene_flag("act1_17_sweep","lied_child_clear") or check_scene_flag("act1_17_sweep","saved_child")
    $ saved_shelter = check_scene_flag("act1_17_sweep","shelter_scattered") or check_scene_flag("act1_17_sweep","saved_shelter")

    # VISUAL: Rooftop. Evening light—golden hour fading to dusk. Same rooftop as Kael's jump.
    # LIGHTING: Warm amber transitioning to deep blue; city lights beginning to glow below.
    # SOUND: Wind constant but softer than before; distant city hum; his breathing.

    "{i}The rooftop. Same place. Same rail. Same wind.{/i}"
    "{i}Where Kael stood. Where Kael chose.{/i}"
    "{i}Where Glass almost shattered completely two nights ago.{/i}"

    # VISUAL: Aeron stands at the rail—not at the edge, just close. Hands resting on metal.
    # Body language: Exhausted but not breaking. Contemplative. Processing.

    a "{i}Two nights ago I stood here ready to jump.{/i}"
    a "{i}Then Lyra knocked. And everything changed.{/i}"
    a "{i}Yesterday I killed [kv] people. Saved [sv].{/i}"
    a "{i}Broke down completely. Shattered. Lyra held the pieces.{/i}"
    a "{i}Last night Zira gave me a choice. Information. Access. Power.{/i}"
    if sv >= 1:
        a "{i}This morning I learned those [sv] are spreading word. Saving others.{/i}"
        a "{i}My mercy rippling outward. Creating more mercy.{/i}"
    else:
        a "{i}This morning I stared at reports that said 'zero survivors.'{/i}"
        a "{i}I don't believe them. I can't. Someone must have lived.{/i}"

    # VISUAL: City below—lights flickering on as dusk deepens. Sectors 8, 9, 10 visible in distance.
    "{i}The city wakes below. Lights like stars igniting. Millions of lives humming.{/i}"
    "{i}Sectors 8, 9, 10 stretch in the distance. Dark patches among the glow.{/i}"

    a "{i}Something's happening there tonight. 'Project Renewal.' Whatever that means.{/i}"
    a "{i}Marcus wants me to watch from command deck. 'Witness history.'{/i}"
    a "{i}But I came here first. To think. To understand.{/i}"
    a "{i}To stand where Kael stood and ask—what would you do?{/i}"

    # VISUAL: He looks at his hands. No blood visible, but he sees it anyway.
    "{i}His hands grip the rail. No blood. But he sees it anyway.{/i}"

    a "{i}These hands killed [kv] people. Saved [sv].{/i}"
    a "{i}Is that redemption? Or just less horror?{/i}"
    a "{i}Lyra said trying matters. Even when you fail.{/i}"
    a "{i}Zira said broken things can be rebuilt. Glass can't.{/i}"
    a "{i}So maybe... maybe I'm not Glass anymore.{/i}"

    # VISUAL: Brief hope in his expression. First time in days. Fragile but real.
    a "{i}Maybe breaking was how I became human again.{/i}"
    a "{i}Maybe mercy—even imperfect mercy—is how I stop being a weapon.{/i}"
    a "{i}Maybe Kael would be proud. That I'm trying.{/i}"

    # VISUAL: Wind picks up. His hair moves. City hum steady. Peaceful moment.
    "{i}The wind carries city sounds. Distant laughter. Music. Life continuing.{/i}"
    "{i}For a moment, the world feels almost... okay.{/i}"

    a "{i}I don't know what happens next. I don't know if I can be fixed.{/i}"
    if sv >= 1:
        a "{i}But I'm not alone. Lyra sees me. Zira respects me. The [sv] survived.{/i}"
    else:
        a "{i}But I'm not alone. Lyra sees me. Zira challenged me. Someone must have survived.{/i}"
    a "{i}That's something. That has to be something.{/i}"

    # SOUND: Footsteps behind him. Soft. Measured. Familiar.
    "{i}Footsteps. Approaching from the rooftop door.{/i}"
    "{i}He doesn't turn. He knows that rhythm.{/i}"

    a "(quiet) Lyra."
    l "How did you know?"
    a "I always know when you're near."

    # VISUAL: Lyra approaches. Stops beside him at the rail. Doesn't touch, just close.
    # She's in casual clothes (rare)—not uniform, not performance. Just her.

    l "I came looking for you. You weren't at your apartment."
    a "Needed air. Needed to think."
    l "And?"
    a "(small smile) Still thinking."

    # VISUAL: They stand in comfortable silence. Watching the city together.
    "{i}Silence settles. Not awkward. Just two people existing together.{/i}"

    l "How are you feeling? After yesterday?"
    a "(honest) Empty. But not the Glass kind of empty."
    a "More like... drained. Purged. Room for something new."
    l "That's good. That's healing."

    # VISUAL: She looks at him. Studies his profile. Concern and something warmer.
    l "You look different."
    a "Different how?"
    l "Less Glass. More you."
    a "(turns to look at her) Is that a good thing?"
    l "(soft smile) It's the best thing."

    # VISUAL: Their eyes meet. Hold. Connection visible. Not quite romantic but close.
    "{i}Something passes between them. Understanding. Recognition. Hope.{/i}"

    a "I checked the networks this morning. The resistance chatter."
    if sv >= 1:
        a "The people I saved—they're spreading word. Warning others. Evacuating families."
        a "My mercy... it's rippling. Creating more mercy."
    else:
        a "Official channels say 'zero survivors.'"
        a "But I don't believe it. Someone is warning others. I can feel it."

    l "See? Trying matters. Even when it's not enough."

    a "[sv] people alive because Glass cracked."
    l "[kv] dead because Glass obeyed."
    a "(quiet) I know. The math doesn't work out."
    l "There is no math that works. There's just choices."
    l "You chose mercy. That's what matters."

    # VISUAL: She moves closer. Shoulder almost touching his. Warmth between them.
    a "You came here yesterday too. After the gala. Before everything."
    l "I was worried. I knew something was wrong."
    a "You're always worried about me."
    l "Someone has to be."

    # VISUAL: He almost laughs. Small. Real. First genuine lightness in days.
    a "What would I do without you?"
    l "Let's not find out."

    # VISUAL: Comfortable silence. Both watching the city. Peaceful moment.
    "{i}They stand together. The city hums. The wind carries warmth.{/i}"
    "{i}For a moment, everything feels... possible.{/i}"

    a "Lyra?"
    l "Yes?"
    a "Thank you. For yesterday. For holding me together when I shattered."
    l "You don't have to thank me."
    a "I do. You saw me at my worst. And you didn't leave."
    l "(turns to face him) I told you. Glass recognizes glass."
    l "But we're not Glass anymore. We're just us."
    l "(softer) Broken. Human. Together."

    # VISUAL: She reaches out. Takes his hand. Gentle. Grounding.
    "{i}Her hand finds his. Fingers intertwine. Warm. Real. Alive.{/i}"

    a "{i}This. This is what I was missing. Connection. Touch. Being seen.{/i}"
    a "{i}Not as Glass. Not as weapon. Just as Aeron.{/i}"

    l "What time is Marcus expecting you?"
    a "2000 hours. Command deck. Observation duty."
    l "That's unusual. He never assigns you observation."
    a "I know. He said to witness 'Project Renewal.' Whatever that is."
    l "(frowns) I don't like the sound of that."
    a "Neither do I. But I don't know what it means."

    # VISUAL: She looks out at Sectors 8-10. Something crosses her face. Unease.
    l "Those sectors have been acting strange. Energy readings. Troop movements."
    a "You noticed too?"
    l "Hard not to. It feels like... preparation."
    a "For what?"
    l "I don't know. But something big."

    # VISUAL: Dread creeping back in. But they push it away. Not yet. Not now.
    a "Let's not think about it. Not right now."
    a "Right now, I just want to stand here. With you. And breathe."
    l "(squeezes his hand) Then that's what we'll do."

    # VISUAL: They turn back to the city. Hands still joined. Watching together.
    "{i}The city glows. Peaceful. Beautiful. Unaware.{/i}"
    "{i}Two people on a rooftop. Holding hands. Finding hope.{/i}"

    a "Do you think we can fix this? Any of it?"
    l "Fix what?"
    a "The system. The city. Us."
    l "(pause) I don't know if we can fix the system."
    l "But us? Maybe. If we try."
    a "Together?"
    l "Together."

    # VISUAL: Small smile on both faces. Tentative. Fragile. Real.
    "{i}Hope. Fragile and small. But real.{/i}"
    "{i}For the first time in days—maybe years—hope.{/i}"

    a "{i}Maybe this is what breaking Glass means. Maybe this is freedom.{/i}"
    a "{i}Not perfection. Not obedience. Just... being human.{/i}"
    a "{i}Feeling things. Connecting. Choosing mercy.{/i}"
    a "{i}Maybe Kael would be proud.{/i}"

    # VISUAL: The sky. Still peaceful. City lights twinkling. Stars beginning to show.
    "{i}The stars appear. Faint against city glow. But there.{/i}"
    "{i}Everything feels... possible.{/i}"

    l "(quiet) It's beautiful up here."
    a "It is."
    l "Thank you for letting me find you."
    a "Thank you for looking."

    # VISUAL: Time stretches. Peaceful. Connected. Two people finding each other.
    "{i}Minutes pass. Maybe hours. Time loses meaning.{/i}"
    "{i}Just two people. One rooftop. One city. One moment.{/i}"

    # ==========================================
    # THE PURGE BEGINS
    # ==========================================

    "{i}19:58. Two minutes until Marcus expects him on command deck.{/i}"

    a "I should go. Marcus will be waiting."
    l "Do you have to?"
    a "(sighs) He's still my father. Still my commander."
    l "You're not Glass anymore. You don't have to obey."
    a "I know. But..."
    a "He said to witness history. Part of me needs to see what that means."

    l "Then I'm coming with you."
    a "Lyra—"
    l "I'm not letting you face whatever this is alone."
    a "(quiet) Okay. Together."

    "{i}They turn. Hands still joined. Ready to face whatever comes.{/i}"

    "{i}20:00. Exactly.{/i}"
    "{i}A hum builds. Low. Deep. Vibrating through the air.{/i}"

    l "(stops) What is that?"
    a "I don't—"

    "{i}The sky EXPLODES.{/i}"

    "{i}LIGHT. BLINDING. IMPOSSIBLE.{/i}"
    "{i}THE SKY TEARS OPEN.{/i}"
    "{i}SECTORS 8, 9, 10 IGNITE.{/i}"

    l "(screaming over noise) WHAT IS THAT?!"
    a "(horror dawning) Oh god—"

    "{i}STRIKE. STRIKE. STRIKE.{/i}"
    "{i}ORBITAL WEAPONS. SURGICAL. DEVASTATING.{/i}"
    "{i}ENTIRE SECTORS ERASED IN SECONDS.{/i}"

    "{i}SHOCKWAVE. THE ROOFTOP SHUDDERS.{/i}"
    "{i}WIND SCREAMS. THEY HOLD THE RAIL OR FALL.{/i}"

    a "(shouting) NO—NO NO NO—"
    l "(horror) THE SECTORS—THE PEOPLE—"

    "{i}BUILDINGS COLLAPSE. ONE. TEN. HUNDREDS.{/i}"
    "{i}FIRES BLOOM. SMOKE RISES. THE CITY BURNS.{/i}"

    a "(realization crushing) The energy maintenance—"
    a "The shield generators offline—"
    a "Troop evacuations—"
    a "Civilians locked down—"

    a "(voice breaking) PROJECT RENEWAL—"
    a "IT WAS ALWAYS—"
    a "THEY PLANNED THIS—"

    "{i}MORE STRIKES. THE LIGHT NEVER STOPS.{/i}"
    "{i}SECTOR AFTER SECTOR. SYSTEMATIC. EFFICIENT. COMPLETE.{/i}"

    l "(sobbing) HOW MANY—"
    a "(horror) HUNDREDS OF THOUSANDS—"

    l "(screaming) WHY?! WHY WOULD THEY—"

    # Self-blame branches: only assert causality if mercy was shown
    if em >= 1:
        a "{i}[sv] people. I saved [sv].{/i}"
        a "{i}They warned others. Families evacuated. Resistance mobilized.{/i}"
        a "{i}Marcus heard. Marcus accelerated.{/i}"
        a "{i}The Purge was scheduled for next week.{/i}"
        a "{i}But I showed mercy. And he moved it to TONIGHT.{/i}"

        a "(barely audible) I did this."
        l "(can't hear him over noise) WHAT?!"
        a "(louder, breaking) I DID THIS. MY MERCY CAUSED THIS."
    else:
        a "{i}This was always coming. He wanted me to watch.{/i}"
        a "{i}He moved the timeline because he could. Because no one could stop him.{/i}"
        a "(broken) I couldn't stop it. I couldn't stop anything."

    "{i}He falls. Knees crash. Hands claw at his face. Body convulses.{/i}"

    if em >= 1:
        a "(screaming) I KILLED THEM. I KILLED THEM ALL."
        a "TRYING TO BE HUMAN. TRYING TO SAVE THEM."
        a "AND I KILLED HUNDREDS OF THOUSANDS."
    else:
        a "(screaming) I FAILED THEM. I FAILED THEM ALL."
        a "OBEYING. WATCHING. DOING NOTHING."
        a "AND HUNDREDS OF THOUSANDS DIED."

    l "(crying) IT'S NOT YOUR FAULT—"
    if em >= 1:
        a "YES IT IS. GLASS SHOULD'VE OBEYED. GLASS SHOULD'VE KILLED THEM ALL."
        a "NO SURVIVORS. NO WARNING. NO MERCY."
        a "THEN MARCUS WOULDN'T HAVE KNOWN. WOULDN'T HAVE MOVED THE TIMELINE."
        a "THEY'D HAVE HAD A WEEK. THEY COULD'VE RUN."
    else:
        a "YES IT IS. I LET THIS HAPPEN. I STOOD HERE AND LET IT HAPPEN."

    "{i}THE STRIKES CONTINUE. SECTOR BY SECTOR. BLOCK BY BLOCK.{/i}"
    "{i}SYSTEMATIC EXTERMINATION. EFFICIENT. PERFECT. COMPLETE.{/i}"

    # Avoid contradictions if specific saves didn't happen
    if saved_vendor or saved_child or saved_shelter:
        a "{i}The vendor. The child. The shelter families.{/i}"
        a "{i}I saved them yesterday. They're dying tonight.{/i}"
    else:
        a "{i}Faces from yesterday. The market. The doors. The shelter.{/i}"
        a "{i}They're dying tonight.{/i}"

    a "{i}Because I tried to be human.{/i}"

    l "(sobbing) WE HAVE TO DO SOMETHING—"
    a "(hollow) THERE'S NOTHING. IT'S ALREADY DONE."
    a "HUNDREDS OF THOUSANDS. GONE. IN MINUTES."

    "{i}The light fades. The strikes slow. Then stop.{/i}"
    "{i}Fire remains. Smoke rises. The city burns.{/i}"
    "{i}Sectors 8, 9, 10. Gone. Erased. Cleansed.{/i}"

    "{i}Silence. Not peace. Just absence.{/i}"
    "{i}Two people on a rooftop. Holding each other. Broken beyond words.{/i}"

    a "(whisper) My hands."
    l "Aeron—"
    a "My hands. I can see them. All of them."
    a "[kv] yesterday. [sv] I saved. Hundreds of thousands tonight."
    a "All on my hands."

    l "It's not your fault. Marcus did this. The system did this."
    a "(hollow laugh) The system? I AM the system."
    a "Glass. Perfect weapon. Perfect obedience."
    a "Except I cracked. Showed mercy. Became human."
    a "(voice breaking) And humanity murdered hundreds of thousands."

    "{i}Silence stretches. The city burns. The world has ended.{/i}"
    "{i}And they sit in the ruins. Together. Shattered. Human.{/i}"

    a "{i}Ten minutes ago I had hope. I thought breaking Glass meant freedom.{/i}"
    a "{i}I thought mercy mattered. That trying counted. That being human was good.{/i}"
    a "{i}But Glass was right all along.{/i}"
    a "{i}Mercy is weakness. Humanity is failure. Trying gets everyone killed.{/i}"
    a "{i}Father wanted me to witness this. To learn this lesson.{/i}"
    a "{i}'This is what happens when Glass cracks,' he'll say.{/i}"
    a "{i}'This is why obedience matters.'{/i}"
    a "{i}And he's right. He's always been right.{/i}"

    l "(urgent) Aeron. Look at me."
    l "(grabs his face, forces eye contact) LOOK AT ME."
    a "(empty) What?"
    l "Don't let him win. Don't let this break you."
    a "(hollow laugh) I'm already broken."
    l "Then we're broken together. But we don't surrender."
    a "What else is there?"
    l "(fierce) REVENGE. RESISTANCE. DESTROYING THE SYSTEM THAT DID THIS."

    a "(quiet) Revenge."
    l "Yes. They did this. Marcus. The Directorate. Echelon."
    l "They ordered this. They pushed the button. They killed hundreds of thousands."
    l "(fierce) NOT YOU. THEM."

    a "...They did this."
    l "Yes."
    a "Father did this."
    l "Yes."
    a "And he wanted me to watch. To learn. To obey."
    l "Yes."
    a "(cold) Then I'll learn. But not what he wanted."

    "{i}He stands. Different. Colder. Harder. Not Glass. Something new.{/i}"

    a "Glass followed orders. Glass showed mercy. Glass failed."
    a "So no more Glass. No more mercy. No more obedience."
    a "(looks at burning sectors) Just ash. And those who made it."

    l "What do we do?"
    a "We burn them back."
    a "Not today. Not tomorrow. But soon."
    a "We learn. We prepare. We find every crack in the system."
    a "And we shatter it from within."

    "{i}Two silhouettes against burning sky. Glass shattered. Humanity murdered. Rage born.{/i}"

    a "{i}Operation 391. My last mission as Glass.{/i}"
    a "{i}Everything after is something new.{/i}"
    a "{i}Not weapon. Not soldier. Not son.{/i}"
    a "{i}Just ash. Waiting to burn the world that made it.{/i}"

    # Scene bookkeeping & canon
    $ set_scene_flag("act1_21_purge", "witnessed_purge")
    $ canon["purge_witnessed"] = True
    $ canon["act1_complete"] = True
    $ canon["glass_shattered"] = True

    return
