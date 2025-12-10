# act2_activity_05_reputation.rpy

# TODO migrate legacy contacts/reputation/currency vars to new system (contacts[], reputation_unders, etc.)
# Uses helpers-only where available: mark_scene(), adjust_empathy_once(), get_empathy_band()
# Adds light EMP/OB flavor beats without trimming original text.

# =======================================================
# ACT 2 - Activity 5: Earn Reputation
# =======================================================

define vendor = Character("Vendor", color="#8D6E63")
define elder = Character("Elder Woman", color="#A1887F")
define man = Character("Angry Man", color="#D32F2F")
define man2 = Character("Kellan", color="#5D4037")
define kellan = Character("Kellan", color="#5D4037")
define woman = Character("Sweep Survivor", color="#6A1B9A")
define lira = Character("Lira", color="#F06292")

label act2_activity_05_earn_reputation:

    # Scene mark
    $ mark_scene("act2_activity_05_reputation", "started")

    # VISUAL: Safe house. Morning. Aeron preparing to go out.
    # LIGHTING: Gray dawn through window. Cold but hopeful.
    # SOUND: City waking. Distant voices. Life continuing.

    "Day [current_day]. Time to face the people who hate me."
    
    # VISUAL: Aeron adjusting Unders clothes. Lyra watching.
    athought "Zira said earn reputation. Help people. Change perceptions."
    athought "Sounds simple. Except everyone down here wants me dead."

    l "You sure about this?"
    a "No. But we need allies. This is how we get them."
    l "By helping the people whose families you killed?"
    a "By helping the people whose families I saved. The 200. They're still out there somewhere."
    l "And if you run into the ones you didn't save?"
    a "...Then I deal with it. Same as everything else."

    # VISUAL: She stands. Moves to him. Hand on his shoulder briefly.
    l "Don't get yourself killed trying to be a hero. You're not good at it yet."
    a "(bitter smile) Thanks for the vote of confidence."
    l "I mean it. You go out there trying to save everyone and you'll end up dead in an alley."
    l "Small steps. One person at a time. Like Zira said."
    a "One person at a time. Right."

    # Optional EMP/OB flavor: pre-departure mindset
    if get_empathy_band() != "obedience":
        athought "One person at a time. Names, not numbers."
        $ adjust_empathy_once("act2_rep_pre_departure_emp", +1)
    else:
        athought "Small wins compound. Optimize for visible outcomes."
        $ adjust_empathy_once("act2_rep_pre_departure_ob", -1)

    # TRANSITION: Out into the Unders. Morning market. People moving. Life happening.
    # VISUAL: Lower Spans market district. Vendors setting up. Crowds thin but growing.
    # LIGHTING: Artificial dawn. Neon signs. Steam vents. Industrial glow.
    # SOUND: Vendors calling. Deals being made. City alive.

    scene bg_lower_spans_market with fade

    "The market. Where I swept. Where they died. Where some lived."
    "Every corner holds ghosts. Every face could be someone I saved or someone who lost everything because of me."

    # VISUAL: Aeron moving through crowd. Eyes down. Not drawing attention.
    # People glance at him. Some recognize something. Most ignore.

    athought "Kade Voss. Just another worker. Nobody important. Nobody dangerous."
    athought "Except I'm terrible at being nobody."

    # VISUAL: Old woman struggling with heavy crate. Vendor stall. No help coming.
    "There. Old woman. Heavy crate. No one helping."

    athought "Small steps. One person at a time."

    # ACTION: Approach and help or keep walking?
    menu:
        "The old woman struggles. No one helps. Everyone's too busy surviving."
        
        "Approach and help":
            # TODO migrate reputation_unders to helper
            $ reputation_unders += 1
            $ helped_elder = True
            
            # VISUAL: Aeron approaches. Cautious. Non-threatening.
            a "Need a hand with that?"
            
            # VISUAL: She looks up. Suspicious. Everyone's suspicious down here.
            elder "Who's asking?"
            a "Nobody. Just someone passing by."
            elder "(eyes narrow) Nobody helps for free in the Unders."
            a "Then consider it unusual."
            
            # VISUAL: Long pause. She evaluates him. Decides.
            elder "...Fine. Lift from that side. Don't drop it."
            
            # VISUAL: They lift together. Heavy. Aeron's muscles strain but he manages.
            # SOUND: Crate scraping. Grunting effort. Set down with thud.
            
            "Heavy. Whatever's in here weighs more than it looks."
            "But we manage. Set it down without dropping it."
            
            elder "(catches breath) Not bad. For nobody."
            a "Glad I could help."
            elder "What's your name, nobody?"
            a "Kade. Kade Voss."
            elder "Well, Kade Voss. You're either stupid or new. Nobody helps for free."
            a "Maybe I'm both."
            elder "(almost smiles) Maybe you are."
            
            # VISUAL: She digs in pocket. Pulls out small coin. Offers it.
            elder "For your trouble."
            a "Keep it. I didn't do it for money."
            elder "(suspicious again) Then why?"
            a "Because you needed help. That's enough."
            
            # VISUAL: She stares. Long. Then pockets coin.
            elder "You're definitely new. That kind of thinking gets you killed."
            elder "But... thank you. Don't make a habit of it."
            a "I'll try not to."
            
            "She turns back to her stall. Dismissing me. But I caught something in her eyes."
            "Not trust. Not yet. But maybe... less hostility. That's something."
            
        "Keep walking - too risky":
            $ reputation_unders += 0
            $ helped_elder = False
            
            "Too risky. She might recognize me. Might call others."
            "I keep walking. One less chance to help. One less person who might remember me differently."
            athought "Small steps. But I just took one backwards."

    # VISUAL: Continue through market. More opportunities. More chances.
    "The market continues. More people. More needs. More opportunities to prove I'm not Glass anymore."

    # VISUAL: Commotion ahead. Voices raised. Crowd gathering.
    # SOUND: Shouting. Angry. Escalating.

    "Voices. Angry. Something's happening."

    # VISUAL: Push through crowd. See what's happening.
    # MAN (young, angry) confronting VENDOR. Knife visible. Threatening.

    man "You owe me! Three days late!"
    vendor "I told you, business has been slow. The Purge scared everyone. No one's buying."
    man "That's not my problem. You borrowed, you pay. That's how it works."
    vendor "I don't have it. Not yet. Give me another week—"
    man "I gave you three weeks already! No more extensions!"

    # VISUAL: Knife moves closer. Vendor backing up. Scared. Crowd watching but not intervening.
    "Debt collection. Violent. Public. And no one's helping."
    "Because down here, you don't interfere in debts. That's how you get killed."

    athought "Walk away. Not your business. Not your problem."
    athought "...Except it is. Because Glass walked away from 600 people. And they died."

    # ACTION: Intervene or walk away?
    menu:
        "The knife gleams. The vendor's terrified. The crowd watches. No one helps."
        
        "Intervene - talk the man down":
            $ reputation_unders += 2
            $ intervened_debt = True
            $ made_enemy = True
            
            # VISUAL: Aeron steps forward. Hands visible. Non-threatening but firm.
            a "Hey. Let's talk about this."
            
            # VISUAL: Man whirls. Knife pointed at Aeron now. Crowd tenses.
            man "Who the fuck are you?"
            a "Nobody. Just someone who thinks there's a better way to handle this."
            man "Better way? He owes me! That's the only way that matters!"
            a "He owes you money. Killing him means you never get paid. Where's the profit in that?"
            
            # VISUAL: Man hesitates. Logic penetrating rage. Barely.
            man "So what? I let him walk? Show everyone they can fuck me over?"
            a "No. You show everyone you're smart. That you get paid eventually instead of getting nothing."
            
            # VISUAL: Vendor watching. Hopeful. Terrified. Silent.
            man "And how do I know he'll pay? How do I know this isn't just bullshit?"
            a "Because I'll vouch for him. He doesn't pay in a week, you come find me."
            
            # VISUAL: Crowd murmurs. Bold move. Stupid move. Maybe both.
            man "(laughs, bitter) You'll vouch for him? And who the fuck are you that your word means anything?"
            a "Someone who keeps his word. That's all you need to know."
            
            # VISUAL: Long tense moment. Knife still out. Could go either way.
            man "...Fine. One week. He doesn't pay, I find you. And if I can't find you, I come back here and finish this."
            man "(to vendor) One week. Don't make me regret this."
            
            # VISUAL: Man sheathes knife. Walks away. Crowd disperses. Crisis averted.
            "He leaves. Knife goes away. Vendor's still alive."
            "I just made a promise I have no idea how to keep. One week. Great."
            
            # VISUAL: Vendor approaches. Shaking. Grateful. Overwhelmed.
            vendor "Thank you. I don't... thank you. I thought he was going to kill me."
            a "He still might if you don't pay him in a week."
            vendor "I know. I'll figure something out. Business will pick up. It has to."
            a "What's your name?"
            vendor "Dren. I sell... I used to sell electronics. Parts. Now I sell whatever I can find."
            a "Kade. And Dren? Find a way to pay him. Because I can't protect you forever."
            vendor "I will. I promise. And thank you again. You... you saved my life."
            
            "Saved his life. One person. That's one more than Glass would have saved."
            "One more name for Tessa's count. If I can keep him alive."
            
            # TODO migrate contacts to helper
            $ contacts["dren"] = {"trust": 2, "debt": "vouched_for", "met": True}
            
        "Walk away - not your fight":
            $ reputation_unders += 0
            $ intervened_debt = False
            
            "Not my fight. Not my business. Interfering in debts gets you killed."
            "I walk away. The vendor's on his own."
            
            # SOUND: Scuffle behind. Cry of pain. Then silence.
            "Behind me, a cry. Pain. Then silence."
            "I don't look back. Can't look back. Glass taught me that."
            "But it still feels like I'm walking away from the Sweep all over again."

    # VISUAL: Continue through market. Processing what just happened.
    athought "Two chances. Two choices. Each one builds or destroys what little reputation I have."
    athought "This is how it works down here. One interaction at a time. One person at a time."

    # VISUAL: Child runs past. Chasing something. Ball rolls into street ahead.
    # SOUND: Heavy vehicle approaching. Fast. Not slowing.

    "Child. Ball. Street. Vehicle coming fast."
    "Shit."

    # VISUAL: Child runs into street after ball. Doesn't see vehicle.
    # Time slows. Split second to decide.

    athought "No time to think. Only react."

    # ACTION: Automatic - save the child. No choice presented. Aeron acts.
    # VISUAL: Aeron lunges. Grabs child. Pulls them back. Vehicle rushes past. Close. Too close.
    # SOUND: Screech. Engine roar. Wind. Heart pounding.

    "Move. Grab. Pull."
    "Vehicle roars past. Inches. Wind tears at us."
    "Close. Too fucking close."

    # VISUAL: They fall. Aeron on ground. Child on top. Safe. Shaken. Alive.
    "Ground. Hard. Child on top of me. Crying. Scared. Alive."
    "That's what matters. Alive."

    # VISUAL: Mother runs over. Panicked. Scoops up child. Checks for injuries.
    mother "Kara! Oh stars, Kara! Are you hurt?"
    
    # VISUAL: Child crying but unharmed. Mother holding her. Then looks at Aeron.
    mother "(sees Aeron) You... you saved her."
    
    # VISUAL: Aeron sits up. Breathing hard. Adrenaline fading. Reality setting in.
    a "(catches breath) She's okay. That's what matters."
    mother "She could have died. That vehicle—if you hadn't—"
    a "But I did. She's safe. That's enough."
    
    # VISUAL: Mother kneels. Still holding child. Eyes wet. Grateful. Overwhelmed.
    mother "Thank you. I don't... I don't know what to say. Thank you."
    a "You don't have to say anything. Just keep her safe."
    mother "What's your name? I need to know who saved my daughter."
    a "Kade. Kade Voss."
    mother "Kade. I'm Lira. And this is Kara. We won't forget this. We owe you everything."
    a "You don't owe me anything. Just... watch her closer next time."
    mother "(nods, crying) I will. I promise. Thank you. Thank you."
    
    # VISUAL: She leaves. Child looking back. Small wave. Aeron waves back.
    "They leave. The child waves. I wave back."
    "One more name. Kara. Saved. Alive."
    "That's two. Dren and Kara. Two names for Tessa."

    # TODO migrate reputation/contacts to helpers
    $ reputation_unders += 3
    $ saved_child = True
    $ contacts["lira"] = {"trust": 5, "gratitude": "infinite", "met": True, "child": "kara"}

    # Optional EMP/OB flavor: the save
    if get_empathy_band() != "obedience":
        athought "Hands still shaking. Relief tastes like rain after fire."
        $ adjust_empathy_once("act2_rep_child_save_emp", +1)
    else:
        athought "Response time acceptable. Outcome optimal. Log and move."
        $ adjust_empathy_once("act2_rep_child_save_ob", -1)

    # VISUAL: Market continuing. But people are looking at Aeron differently now.
    # Whispers. Nods. Small acknowledgments.

    "The market continues. But something's different. People are looking at me."
    "Not with hostility. Not exactly. But... awareness. Recognition. Maybe respect."

    # VISUAL: Man approaches. Older. Weathered. Cautious but not hostile.
    man2 "You're Kade?"
    a "(wary) Yeah. Why?"
    man2 "Saw what you did. With the debt. With the kid."
    man2 "That took guts. Or stupidity. Hard to tell which."
    a "Probably both."
    man2 "(nods) Down here, probably both is what keeps you alive."
    man2 "Name's Kellan. I run a small operation. Deliveries, mostly. Legitimate."
    a "Good for you."
    kellan "I could use someone with your instincts. Someone who doesn't look away when things get hard."
    kellan "Pay's not great. But it's steady. And it builds reputation."
    a "I'll think about it."
    kellan "Do that. You know where to find me if you need work. Ask around for Kellan. They'll point you my way."
    
    # VISUAL: He leaves. Another contact. Another thread.
    "Another offer. Another connection. Reputation building thread by thread."

    # TODO migrate contacts to helper
    $ contacts["kellan"] = {"trust": 1, "job_offer": True, "met": True, "work": "deliveries"}

    # VISUAL: Aeron continues. One more encounter. Final test.
    # VISUAL: Recognizes someone. From the Sweep. Woman. Mid-30s. Scar on face.
    # She's setting up stall. Hasn't seen him yet.

    "Wait. I know her."
    "The Sweep. Sector 10. I let her run. Didn't report her. She's one of the 200."
    "Does she remember me?"

    # ACTION: Approach or avoid?
    menu:
        "She's one of the 200. One of the ones I saved. Does she remember?"
        
        "Approach her":
            $ approached_survivor = True
            $ reputation_unders += 2
            
            # VISUAL: Aeron approaches. Careful. Hands visible.
            a "Excuse me."
            
            # VISUAL: She turns. Looks at him. Eyes widen. Recognition. Fear. Then something else.
            woman "(stiffens) You."
            a "You remember me."
            woman "Hard to forget Glass."
            
            # VISUAL: Tension. Crowd notices. Some move closer. Ready to intervene.
            "She knows. She remembers. And everyone's watching now."
            
            a "I'm not Glass anymore. I'm... trying not to be."
            woman "Trying. That's nice. Try doesn't bring back the dead."
            a "No. It doesn't. Nothing does."
            woman "(bitter laugh) So why are you here? Come to finish the job?"
            a "No. I came to... I don't know. Say I'm sorry. For what it's worth."
            woman "It's not worth much."
            a "I know. But it's all I have."
            
            # VISUAL: Long silence. She stares at him. Evaluating. Processing.
            woman "You let me run. During the Sweep. You saw me and you let me run."
            a "I did."
            woman "Why?"
            a "Because I could. Because I had to save someone. Because... I was cracking."
            woman "Cracking. Poetic. My husband didn't get to crack. He died in that apartment."
            
            # VISUAL: Pain. Raw. Real. Aeron doesn't flinch from it.
            a "I'm sorry. I know that doesn't help. But I'm sorry."
            
            # VISUAL: She turns away. Back to stall. Dismissing him. Then pauses.
            woman "What's your name now? Since you're not Glass."
            a "Kade. Kade Voss."
            woman "Kade Voss. Fine. You want redemption, Kade? Earn it. Help people. Save people. Do something that matters."
            woman "Because right now? Right now you're just the man who killed my husband and let me live. That's your legacy."
            woman "Change it. Or don't. I don't care. Just don't expect me to forgive you."
            
            # VISUAL: She goes back to work. Conversation over. But not hostile. Not threatening.
            a "I won't expect forgiveness. But I'll earn it anyway."
            woman "(doesn't look back) We'll see."
            
            "She doesn't forgive me. Doesn't have to. But she didn't call for my head either."
            "That's something. Maybe enough to build on. One day."
            
            # TODO migrate contacts to helper
            $ contacts["sweep_survivor"] = {"trust": 0, "trauma": "husband_killed", "met": True, "saved": True}
            
        "Avoid her - not ready":
            $ approached_survivor = False
            
            "Not ready. Can't face her. Not yet. Not today."
            "I turn away. One more chance wasted. One more person I failed."

    # VISUAL: Return to safe house. Evening. Exhausted. Changed.
    # TRANSITION: Back to safe house. Lyra waiting.

    scene bg_safe_house with fade

    "Back. Safe house. Evening. Exhausted. Body and mind both drained."
    "But something's different. Something changed today."

    # VISUAL: Lyra looks up. Sees him. Evaluates.
    l "You're alive. That's better than I expected."
    a "(collapses against wall) Barely."
    l "What happened?"
    
    # VISUAL: Aeron processing. Multiple encounters. Each one significant.
    a "Helped an old woman with a crate. Talked down a debt collector. Saved a kid from getting run over."
    a "Met one of the survivors from the Sweep. She remembered me."
    l "And?"
    a "And she didn't kill me. Didn't forgive me either. But she didn't kill me."
    l "That's progress."
    a "Is it? Feels like I'm just putting bandages on a wound that'll never heal."
    
    # VISUAL: Lyra sits beside him. Close. Grounding presence.
    l "Maybe it won't heal. Maybe it's not supposed to. But you're still trying. That counts for something."
    a "Does it?"
    l "Ask the kid. Ask her mother. Ask the vendor. They're alive because of you."
    l "That's three people who wouldn't be without you. That's not nothing."
    
    # VISUAL: Silence. Processing. Accepting. Maybe believing.
    athought "Three people. Kara. Dren. The elder."
    athought "Three names to balance against 600. Doesn't seem like enough. But it's a start."
    
    l "You did good today."
    a "I did something. Good is... subjective."
    l "Take the win, Aeron. You earned it."

    # Optional EMP/OB flavor: debrief tone
    if get_empathy_band() != "obedience":
        athought "Tessa was right. Count the living."
        $ adjust_empathy_once("act2_rep_debrief_emp", +1)
    else:
        athought "Three confirmed positives. Iterate tomorrow."
        $ adjust_empathy_once("act2_rep_debrief_ob", -1)
    
    # VISUAL: He nods. Small. Accepting it. For now.
    athought "One day. Three lives. Multiple connections."
    athought "Reputation built one interaction at a time. One person at a time."
    athought "Tessa was right. Count the living. Three today. How many tomorrow?"

    # Show reputation gain summary
    if reputation_unders >= 6:
        "The Unders are starting to see me differently. Not as Glass. But as someone trying."
        "That's enough. For now."
    else:
        "Small progress. Barely noticeable. But progress nonetheless."
        "One day at a time. One person at a time. Until reputation becomes reality."

    # Mark completion
    $ mark_scene("act2_activity_05_reputation", "completed")

    # TRANSITION: Back to hub
    jump act2_activity_hub

    # canon_note: Activity 5 complete - reputation earned through helping others
    # canon_note: Helped elder with crate (optional, +1 reputation)
    # canon_note: Intervened in debt situation - vouched for Dren (choice, +2 reputation, made enemy)
    # canon_note: Saved child Kara from vehicle (automatic, +3 reputation, major impact)
    # canon_note: Met Kellan (job offer - deliveries)
    # canon_note: Confronted Sweep survivor (optional, +2 reputation, no forgiveness but no hostility)
    # canon_note: Total reputation gain: 1-8 points depending on choices
    # canon_note: Three lives saved/helped: Elder, Dren, Kara (minimum), plus survivor confronted
    # canon_note: "Count the Living" philosophy demonstrated - names for Tessa
    # canon_note: Contacts made: Dren (vendor, owes favor), Lira (mother, infinite gratitude), Kellan (job offer), Sweep survivor (neutral)
    # canon_note: Shows Aeron changing from Glass to someone who helps - small steps matter
    # canon_note: Enemy made: debt collector remembers Aeron (future consequence)
    # canon_note: One week deadline for Dren's debt - subplot introduced

