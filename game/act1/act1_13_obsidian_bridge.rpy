# act1_13_obsidian_bridge.rpy


# =======================================================
# ACT 1 - Scene 12: The Obsidian Bridge
# =======================================================


label act1_obsidian_bridge:
    "{i}The air is colder here. Thinner. Smells of rust, oil, and static.{/i}"
    "{i}Each step on the bridge creaks like a warning. Like the structure remembers a time when it mattered.{/i}"
    "{i}She's already there.{/i}"

    # Zira leans on the guardrail, one leg propped up, illuminated by the pale light of her hacked wrist console.

    z "(without looking up) You’re late, Rylan."
    a "You’re lucky I came at all. This isn’t exactly a welcoming spot."
    z "(grins, still not facing him) That’s why I picked it. If someone tailed you, they’d be the ones hitting the floor."

    "{i}She finally turns to face him. Sharp eyes. Half-shadowed smirk. Black hair streaked with neon purple, tied messily back. She’s younger than he expected — but her presence makes the bridge feel like her territory.{/i}"

    a "You're Zira, then."
    z "Mhm. In the flesh. Aeron Rylan, huh? Echelon’s golden ghost. Thought you’d stand taller."

    # --- PLAYER CHOICE: How does Aeron respond? ---
    menu:
        "Stay composed":
            a "(dry) And I thought hackers were supposed to be subtle."
            z "(snorts) Subtle gets you killed. Fast keeps you fed."
            $ zira_rel += 1
        "Fire back":
            a "(smirks) I thought you’d be more paranoid."
            z "(eyes narrow) I am. You just don’t know what I’m watching."
        "Say nothing":
            a "..."
            z "(tilts her head) Ah. The brooding type. Cute."

    "{i}She hops down from the railing, boots clanking against the rusted steel. Approaches, circling him like she’s assessing a weapon left out in the rain.{/i}"

    z "So Echelon sends their golden ghost to sweep Ten. You know what that tells me?"
    a "Enlighten me."
    z "(snorts) 'Enlighten you?' Cute talk for a soldier."
    z "Tells me someone upstairs is shitting bricks — lookin' for a scapegoat that looks good on camera."
    a "(carefully) You talk a lot for someone who’s supposed to be helpful."
    z "(grins) I'm helpful. Just not obedient."

    # --- OPTIONAL FLIRT UNLOCK (if zira_chemistry is high enough) ---
    if zira_rel >= 2:
        menu:
            "Lean into the banter":
                a "(playfully) You always this charming with strangers?"
                z "(laughs, surprised) Only the ones I don’t immediately wanna stab."
                a "(smirks) That’s progress, I think."
                z "(steps closer) Don’t let it go to your head, pretty boy."
                $ zira_flirt_unlocked = True
            "Keep it professional":
                a "(curt) I’m here for intel. Not games."
                z "(shrugs) Then you’re gonna be disappointed on both fronts."

    # Continue scene regardless of choice

    "{i}She pulls a small device from her coat — old, cracked, glowing faintly. Modified comm-node relay.{/i}"

    z "This is what they’re lookin’ for. Reroutes data through ghostlines — clean, untraceable. Problem is... I ain’t the only one who built one."
    a "Then who leaked the data?"
    z "Not sure yet. But it wasn’t me. That breach? Too sloppy. Too loud. Screamed bait. Someone wanted eyes down here."
    a "And you're just handing this over to me?"
    z "Not exactly. I’m givin’ you a taste. The rest... we talk terms."

    # --- PLAYER CHOICE: Trust her or not ---
    menu:
        "Agree to hear her out":
            a "Fine. I'm listening."
            z "(nods) Good. I like guys who know when to shut up and when to pay attention."
            $ zira_rel += 1
        "Refuse to play her game":
            a "No deal. You're wasting my time."
            z "(shrugs) Then go cry to your handlers. Hope they ain’t the ones who pulled the strings."
            $ zira_rel -= 1

    "{i}Their eyes meet in the dim light. Mistrust. Curiosity. Sparks. Something unspoken hangs there — something electric.{/i}"

    if zira_flirt_unlocked:
        z "(softly, almost teasing) Careful, Rylan. Keep lookin’ at me like that and I might start thinkin’ you like this little game."
        a "(quiet) You're the one playing."
        z "(smiles) Then we’re both in trouble."

    "{i}Zira slips the device back into her coat, turns to walk toward the opposite edge of the bridge.{/i}"

    z "Walk with me. I’ll show you what Echelon doesn’t want you to see."

    "{i}And just like that, the ghost of Sector 10 becomes something else entirely — a whisper in the dark, beckoning him forward.{/i}"

    # Aeron stays quiet for a beat, eyes scanning her.
    a "You always this cryptic, or am I just lucky tonight?"

    # Zira leans back on the railing, smirking.
    z "Wouldn’t you like to know. Maybe you’re just charming enough to earn answers... or dumb enough to think you deserve ’em."

    menu:
        "Charming, clearly.":
            $ zira_rel += 1
            a "(smirks) Charming, clearly."
            z "(tilts her head, amused) Mm. Modest, too."
        "You're dodging my question.":
            a "You're dodging my question."
            z "(shrugs) Habit. Keeps me alive."
        "Let's skip the games. What do you want?":
            $ zira_rel -= 1
            a "Let's skip the games. What do you want?"
            z "(dry) Straight to business. Typical Aerie boy."

    # She pushes off the railing, pacing a few steps.
    z "You’re not like the rest of ’em, though. I’ve seen you move. Clean. Precise. But your eyes... they give you away."
    a "(quietly) You’ve been watching me?"
    z "You’re on the regime’s leash. But that leash is frayin’."
    a "You planning to cut it?"
    z "(smirks) I’m plannin’ to see what happens when it snaps."

    # She stops walking, facing him.
    z "You’re here ’cause the comm-lines got hit. ’Cause your old man wants the city blind and deaf, and someone like me flipped the lights."
    a "And you're admitting to that?"
    z "(grins) Who said I did? Maybe I just know the hand that did."

    # A silence. The wind stirs debris across the rusted bridge.
    z "You want the truth, soldier boy? You’re bein’ played. They sent you here to tie up loose ends, not investigate."
    a "And you’re the loose end?"
    z "(leans in) Not that easy to cut loose, sweetheart."

    # Slight tension, electricity in the air.

    menu:
        "You're not what I expected.":
            $ zira_rel += 1
            a "(softly) You’re not what I expected."
            z "(teasing) Flirting with the enemy now? Dangerous kink."
        "If you’re right... what happens to me?" :
            a "If you’re right... what happens to me?"
            z "Depends. You wake up, or you vanish. That’s how it works down here."
        "This is a setup, isn’t it?":
            $ zira_rel -= 1
            a "This is a setup, isn’t it?"
            z "(scoffs) If it were, you’d be dead already. Try to keep up."

    # Zira suddenly tosses a datachip to him.
    z "Here. Unmarked. Clean. Don’t jack it into anything with eyes on it."
    a "What’s on it?"
    z "The truth. Or just enough of it to crack the pretty illusion you’ve been livin’ in."
    a "(inspects the chip) Why me?"
    z "(serious for once) ’Cause you hesitated. On that roof. I know that look. You’re not one of them. Not really."

    # She starts to walk away into the shadows.
    a "Zira—"
    z "(over her shoulder) You want answers? Come find me. Next time, lose the leash."

    "{i}Aeron stands alone now. The city hums beyond the steel and concrete. The datachip in his palm feels heavier than it should.{/i}"
    
    a "{i}Zira... who the hell are you?{/i}"
    return