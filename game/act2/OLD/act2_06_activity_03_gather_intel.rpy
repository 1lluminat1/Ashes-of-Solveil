# act2_activity_03_gather_intel.rpy
# =======================================================
# ACT 2 - Activity 3: Gather Intel (Meet Noelle)
# =======================================================
# TODO migrate legacy currency/contacts/reputation/activity counters to helpers
# (lines near the end still touch: intel_documents, contacts, reputation_unders,
#  activities_completed, days_remaining, activity_intel_done)
# Helper usage here: rel(), mark_flag(), adjust_empathy_once()
# (If you have mark_scene/inc_rep/learn_skill/etc. helpers, you can drop them in too.)

label activity_gather_intel:

    # VISUAL: Lower Spans. Night. Sector 6 rooftops overlooking Echelon patrol routes.
    # LIGHTING: Cold blue-white from streetlights below; neon glow distant; shadows deep.
    # SOUND: City hum; distant patrols; Aeron's breathing; wind through metal.

    #scene bg_sector6_rooftops with fade

    "Day 3. Activity: Gather Intel."
    "Zira said know your enemy, so I'm learning."

    # VISUAL: Aeron crouched on rooftop edge. Binoculars (if acquired) or just eyes.
    # Watching Echelon patrols below. Taking notes on old datapad.

    "Echelon patrols move like clockwork—predictable, every 20 minutes, same routes."
    "Or they were. Something's changed."

    athought "The patrol patterns are shifting. Not random though. There's logic here—deliberate adaptation."
    athought "They're responding to resistance activity somehow."
    athought "But how? What's the underlying pattern?"

    # VISUAL: He reviews notes. Frustrated. Data incomplete. Can't see the bigger picture.
    "Three nights of tracking and I still can't predict them."
    "There's an algorithm here somewhere. I'm just not seeing it."

    # SOUND: Footstep. Soft. Behind him. Close.
    # VISUAL: He tenses. Hand moves toward weapon (if acquired).

    "Not alone."

    # He spins. Ready. Tense.
    # VISUAL: Figure stands 3 meters away. Female. Mid-20s. Arms crossed. Unimpressed.

    n "You're reading that wrong."

    # VISUAL: Noelle. Silver-blue eyes. Clinical posture. No threat display, just observation.
    # LIGHTING: Cold blue glow from datapad illuminates her face. Sharp. Precise.

    a "Who—"

    n "The patrol shifts aren't random—they're algorithmic. Echelon uses predictive modeling to adapt their routes based on resistance activity patterns."
    n "You're tracking outcomes, the physical movement patterns, but you're missing the inputs that feed their decision matrices."
    n "That's why you can't predict them."

    # VISUAL: She steps closer. Not threatening. Just... analyzing. Like he's data.
    "She moves like she's solving an equation, every step calculated and deliberate."

    a "(hand still on weapon) How long have you been watching me?"
    n "Three nights, same as you've been watching them."
    n "You're consistent and methodical, but your analysis has fundamental gaps."

    a "And you're an expert?"
    n "Yes."

    # VISUAL: No hesitation. No arrogance. Just fact. She believes it completely.
    athought "No bravado, no performance. She states it like math."
    athought "Two plus two equals four. She's an expert. Same certainty."

    a "Why tell me? Why not just keep doing your own thing?"
    n "Because I need field data—real-time observations from someone who knows what they're looking at."
    n "I can model algorithms, predict shifts, and map probabilities, but I need ground-truth verification to refine my accuracy."
    n "You provide field observations, I provide predictive analysis. Both parties benefit from the exchange."

    # VISUAL: She extends hand. Not friendly. Transactional. Like a business deal.
    n "Noelle Korr. I used to work for Compliance Division as a neural conditioning researcher."
    n "Until I discovered they were rewriting people's memories to maintain social obedience."
    n "I objected to the ethical violations. They objected to my objection. Mutual termination of our relationship."
    n "(matter-of-fact) Now I'm here, underground, and very interested in Echelon's predictive models."

    # VISUAL: He hesitates. Compliance Division. Echelon. But she said 'used to.'
    a "(carefully) You worked for Echelon?"
    n "Past tense matters. I left when I discovered what they were really doing."
    n "They're not just maintaining order—they're erasing cognitive dissent at the neurological level."
    n "I had evidence. They wanted me silent. I declined and escaped with my research data."

    # VISUAL: He takes her hand. Firm. Brief. Professional.
    a "Kade Voss. Observer, currently gathering intel on patrol movements."
    n "'Kade Voss' is an alias, but that's acceptable. I don't require real names for functional partnerships."
    n "Your actual identity is irrelevant as long as your data is accurate."

    # VISUAL: She releases hand. Pulls out her own datapad. More advanced. Covered in notes.
    n "Show me your data and I'll correct your analysis."

    # VISUAL: He hesitates. Sharing intel = risk. But she's right. He needs help.
    athought "She's blunt, clinical, no social performance whatsoever."
    athought "Either completely genuine or the best actor I've ever encountered."
    athought "But she's right—I'm missing something. And I need answers."

    # He shows her datapad. She scans it. Eyes moving rapidly. Processing.
    # VISUAL: Her face: focused, analytical, slight frown (data displeases her).

    n "(scrolling quickly) This is incomplete—surface-level observations with no temporal cross-referencing."
    n "You're tracking current patterns but not historical trends or predictive modeling."
    n "Echelon adapts every 72 hours based on resistance activity metrics. You've captured one cycle, which is insufficient for meaningful prediction."

    a "(defensive) I've been tracking for three nights—"
    n "Right, three nights equals one cycle. You need minimum three cycles—nine nights of continuous observation—before the underlying patterns become statistically visible."
    n "Single-cycle data is essentially noise without context."

    # VISUAL: She pulls up her own data. Screen filled with charts, graphs, models.
    n "I've been tracking for six weeks with historical data, predictive algorithms, and pattern analysis."
    n "Their current patrol model is what I'm calling Adaptive Response Protocol 7."
    n "It shifts every 68 to 76 hours depending on local resistance incidents and sector-specific threat assessments."
    n "(points to map) Next shift happens in approximately 22 hours. Routes will change here, here, and here."

    # VISUAL: She points to specific locations. Precise. Confident.
    athought "She's not guessing. She knows this. But how?"

    a "How can you be sure?"
    n "Bayesian probability combined with historical precedent and pattern recognition. I've modeled their decision-making algorithm across 47 shift cycles."
    n "Current confidence interval is about 89% with a margin of error around plus or minus 4%."
    n "(slight shrug) If you want absolute certainty, you're asking the wrong person. Certainty is irrational in complex systems."
    n "But high probability within acceptable error margins? That I can provide."

    # VISUAL: He stares at her data. Complex. Beyond his training. But... logical.
    a "You really know your stuff."
    n "Yes, that's what I said initially. Are you experiencing comprehension delay or just processing the implications?"

    # VISUAL: Pause. He realizes: she's not being rude. She's literal. No social filter.
    athought "She doesn't do sarcasm or hints. Just direct truth."
    athought "It's almost refreshing after years of performance and masks."

    a "No, just not used to people being this direct."
    n "Indirect communication is inefficient and introduces unnecessary ambiguity. I prefer clarity even when clarity creates social discomfort."
    n "Most people find it off-putting, but it reduces misunderstandings by approximately 60%."

    # VISUAL: She closes her datapad. Looks at him fully. Analyzing.
    n "You're military trained—Echelon methodology specifically. I can tell from your observation technique and postural habits."
    n "But you're here gathering intel against them, which creates an obvious contradiction."
    n "(direct eye contact) So which is it? Defector or active infiltrator?"

    # VISUAL: He tenses. This is the moment. Lie or truth?
    menu:
        "Tell the truth (partial)—'Defector. Very recently.'":
            # HELPER UPDATES:
            $ rel("Noelle", trust=1)
            $ mark_flag("Noelle", "aeron_honest_with_noelle")
            $ adjust_empathy_once("act2_03_intel_honesty", +1)

            a "Defector. Very recently—less than a week."
            n "(processing) Temporal context suggests defection during the Purge event. Causal relationship?"
            a "Yes. I witnessed it and couldn't stay after that."

            n "(nods slowly) That's a logical response to severe cognitive dissonance."
            n "You experienced ethical conflict when your actions contradicted your core values. The system rejected your humanity, or your humanity rejected the system."
            n "Either framing leads to the same outcome—defection becomes psychologically necessary."

            a "You're not concerned that I was Echelon?"
            n "Past tense is critical here. 'Was' versus 'is' changes the entire probability matrix."
            n "Your current behavior patterns suggest genuine defection rather than active infiltration. Observable data supports your claim."
            n "(tilts head) Probability you're deceiving me? Approximately 23%. That's within my acceptable risk threshold for potential partnerships."

            # VISUAL: She extends datapad toward him. Offering collaboration.
            n "I'll share my predictive models if you share field observations. Together we achieve more accurate predictions and higher survival probability."
            n "Does that sound reasonable?"

        "Deflect—'Does it matter? I'm here now working against them.'":
            # HELPER UPDATES:
            $ rel("Noelle", trust=0)
            $ mark_flag("Noelle", "aeron_deflected_with_noelle")
            $ adjust_empathy_once("act2_03_intel_deflect", -1)

            a "Does it matter? I'm here now, actively working against Echelon."
            n "(pause) Evasive response. You're declining to provide relevant contextual data."
            n "That indicates either classified information constraints or trust issues, both of which are understandable but complicate partnership dynamics."

            a "I'm not trying to complicate things—"
            n "Then provide context. Or don't—but understand that I calculate risk continuously."
            n "Unknown variables increase uncertainty. Uncertainty decreases my willingness to share high-value intelligence."

            # VISUAL: She doesn't seem hurt. Just... calculating. Adjusting probability.
            n "I'll share limited data—surface-level analysis only until you prove reliable."
            n "If you demonstrate consistent accuracy and non-hostile intent, I'll increase information sharing accordingly."
            n "Basic trust protocol. Does that work for you?"

    # VISUAL: Either way, she extends datapad. Offering some level of partnership.
    a "Acceptable. And... thank you."
    n "Gratitude is unnecessary for transactional exchanges, but acknowledged anyway. You're welcome."

    # VISUAL: She transfers data to his datapad. Files flowing. Advanced intel.
    # SOUND: Electronic beeps. Data transfer. His pad suddenly much more useful.

    "Her data fills my datapad—charts, models, predictions, analysis."
    "More intelligence than I could gather in months. She's sharing it in seconds."

    a "This is extensive. You're sure you want to share all this?"
    n "Information hoarded is information wasted. Resistance requires distributed knowledge and redundant data storage."
    n "Also, if you die with this data, I have backups in three separate locations. Risk mitigation."

    # VISUAL: He can't tell if she's joking. Her face: completely neutral.
    a "Right. Risk mitigation."
    n "Was that intended as humor? I detected possible sarcasm but remain uncertain."
    a "Honestly, I don't know either."
    n "Acceptable answer. Ambiguity acknowledged. Moving forward."

    # VISUAL: She moves to rooftop edge. Looks down at patrols. Observing.
    n "Next patrol arrives in approximately 4 minutes. Route designation Alpha-7. Confidence level: 94%."
    n "We'll observe together, verify my model's accuracy, and I'll adjust variables if the prediction fails."

    # VISUAL: They stand side by side. Watching. Waiting. Silence comfortable (for her).
    "She doesn't fill silence with unnecessary words. Doesn't perform socially. Just exists."
    "Watching data transform into reality. Equations becoming patrols."

    # SOUND: Patrol approaches below. Boots. Voices. Echelon soldiers.
    # VISUAL: Exactly on schedule. Exactly the route she predicted.

    n "Route Alpha-7, exactly as predicted. Model accuracy confirmed."
    n "(small note of satisfaction) Good. I really dislike being wrong."

    a "You do this every night? Predict their movements?"
    n "Daily, yes. Predictive modeling has a calming effect on me—there's something deeply satisfying about finding order within apparent chaos."
    n "It's also functionally useful for survival since avoiding Echelon requires knowing where they'll be before they arrive."

    a "How long have you been down here living underground?"
    n "Six months, three weeks, and two days since I left Compliance Division."
    n "My survival rate has exceeded initial projections, which suggests successful environmental adaptation."
    n "(slight pause) Though I do miss reliable data infrastructure and climate-controlled environments."

    # VISUAL: She says it matter-of-fact. Missing climate control = missing family.
    athought "She misses climate control, not people or comfort. Climate control."
    athought "I can't tell if that's sad or just... her. Just how her mind works."

    a "Do you work with others or primarily solo?"
    n "Primarily solo. Social interaction requires significant energy that I prefer allocating toward research and analysis."
    n "But I maintain a small network of contacts—information sources, occasional collaborators. People I can work with on specific projects."
    n "(gestures between them) This qualifies as one. Mutually beneficial and surprisingly tolerable so far."

    a "Tolerable. That's high praise."
    n "(brief glance at him) You haven't annoyed me yet, which is statistically rare. Most people become irritating within the first ten minutes."
    n "You're currently at 15 minutes with minimal irritation. That's promising."

    # VISUAL: They watch patrols disappear. Silence returns. She prepares to leave.
    n "I have sufficient observational data for tonight. I'm returning to run full analysis on the variables."
    n "(transfers coordinates to his pad) Meet me here tomorrow at 23:00. Different location, same purpose. Try not to be late."

    a "What if I can't make it?"
    n "Then I work alone as usual, which I'm accustomed to."
    n "(slight pause) But I'd prefer you attend. Your field observations improve my predictive accuracy by 12 to 18 percent, which is statistically significant enough to justify continued collaboration."

    # VISUAL: She turns to leave. Stops. Looks back. Almost uncertain (rare for her).
    n "Kade. One question before I go."
    a "Yeah?"
    n "Why defect specifically? What was the variable that shifted you from compliance to resistance?"

    # VISUAL: He processes. How to explain the Purge? The guilt? The shattering?
    a "I watched 100,000 people die in minutes because of decisions I made."
    a "And I realized I couldn't be part of that system anymore."

    n "(long pause, processing carefully) Causal guilt combined with ethical crisis. Your entire identity structure fractured when your actions contradicted your core values."
    n "(quieter, more careful) That's... logical. Extremely painful, but logically consistent."
    n "I'm sorry for what you're experiencing. Even though logically, expressing regret doesn't change past events or reduce your pain."

    # VISUAL: She says it awkwardly. Like practicing a skill she's studied but not mastered.
    a "Thank you. I think."
    n "I'm not particularly skilled at emotional responses. They don't come naturally to me."
    n "But the research data suggests empathy improves cooperative relationships, so I'm attempting it."
    n "(slight uncertainty) Was that adequate?"

    a "(small smile) You're doing fine."
    n "(nods once) Noted. I'll continue making attempts then."

    # VISUAL: She leaves. Disappears into shadows. Gone as suddenly as she appeared.
    "And just like that she's gone, like she was never here at all."
    "But my datapad is full of her work—models, predictions, brilliant analysis."

    athought "Noelle Korr. Analyst. Former Compliance Division researcher."
    athought "Blunt, clinical, brilliant, and unexpectedly human beneath all that logic."
    athought "And somehow I think I just made an ally."

    # VISUAL: He reviews her data. Page after page. Intricate. Beautiful in its logic.
    athought "She sees the world in patterns, algorithms, probabilities."
    athought "No performance, no masks, no social games. Just unfiltered truth."
    athought "It's strange and uncomfortable, but there's something honest about it."
    athought "Maybe that's what I need right now. Someone who can't lie even if she wanted to."

    # TRANSITION: Return to safe house. Report to Zira. Activity complete.
    scene bg_safe_house with fade

    # VISUAL: Zira examining the data Noelle provided. Impressed.
    z "Where the hell did you get this? This is professional-grade intelligence analysis."
    a "Met someone tonight. An analyst who's been tracking Echelon independently."
    z "She? What's her name?"
    a "Noelle Korr. Says she used to work for Compliance Division."

    # VISUAL: Zira stops. Looks up sharp. Recognizes the name immediately.
    z "(low whistle) Noelle Korr. I've heard of her."
    z "Neural conditioning researcher. Absolutely brilliant. She disappeared from Echelon about six months ago."
    z "Word is she stole massive amounts of classified research data. They've been hunting her ever since."

    a "She mentioned discovering ethical violations. Memory alteration programs."
    z "Yeah. She found proof that Echelon was literally rewriting people's memories to maintain compliance."
    z "Erasing dissent at the neurological level. She tried to expose it internally, and they tried to erase her."
    z "(grins) But she got out with her research intact. And now she's working with you."

    a "Is that a problem?"
    z "Problem? Glass, you just partnered with one of the most wanted defectors in Solveil."
    z "(looks at data again) This is incredibly valuable. Keep working with her."
    z "She's probably the smartest person in this entire city, and if she's willing to share intel with you, don't fuck it up."

    a "She wants to meet again tomorrow night. Same arrangement."
    z "Go. Learn everything she'll teach you. This kind of predictive analysis could save dozens of lives."
    z "(serious now) But be careful. She's Echelon's second-most-wanted target after you."
    z "If they find you together, they'll kill both of you without hesitation."

    a "Understood."
    z "Good. Now get some rest. Tomorrow's another day of not dying, and apparently you have a date with a genius."

    # TRANSITION: End of activity. Rewards gained. Contact added.

    # REWARDS SUMMARY SCREEN:
    "{b}Activity Complete: Gather Intel{/b}"
    "
    Rewards:
    - Intel Document: 'Predictive Patrol Models' (Advanced)
    - Contact Added: Noelle Korr (Analyst, Trust: [characters['Noelle']['trust']])
    - Reputation: +1 (Demonstrated competence in intelligence gathering)
    
    New Ability Unlocked: 'Pattern Recognition'
    - Reduced detection chance during Echelon encounters
    - Improved mission planning capabilities
    - Better tactical decision-making
    
    Noelle Korr is now available for future collaboration.
    Meet her tomorrow night to continue intelligence operations.
    "

    # HELPER-FIRST UPDATES (where possible)
    $ mark_flag("Noelle", "predictive_models_shared")
    $ adjust_empathy_once("act2_03_intel_collab", +1)

    # Legacy data structures (awaiting migration helpers) — see TODO at top
    $ activities_completed += 1
    $ days_remaining -= 1
    $ intel_documents.append("predictive_patrol_models")
    $ contacts["noelle"] = {"trust": characters["Noelle"]["trust"], "met": True, "skills": ["analysis", "prediction", "neural_research"]}
    $ reputation_unders += 1
    $ activity_intel_done = True

    # canon_note: Noelle introduced - brilliant analyst, former Compliance Division researcher
    # canon_note: Neural conditioning backstory - Echelon rewrites memories for social compliance
    # canon_note: She's direct and literal but not robotic - autism-coded respectfully with natural speech
    # canon_note: "Pattern Recognition" ability reduces Echelon detection in future missions
    # canon_note: She's Echelon's second-most-wanted (after Aeron) - dangerous partnership
    # canon_note: She doesn't know he's Glass yet - discovery comes in future scene
    # canon_note: Trust variable affects her willingness to share intel and help
    # canon_note: Her emotional awkwardness is genuine attempt at empathy, not coldness
    # canon_note: She'll develop throughout story - logic → understanding → empathy through Aeron
    # canon_note: "No unit for this" moment comes later when she realizes she has feelings

    jump act2_activity_hub
