# act2_11_noelle_working_late.rpy (REVISED)


# =======================================================
# ACT 2 - Scene 11: Noelle - Working Late (Intellectual Intimacy)
# =======================================================


label act2_11_noelle_working_late:

    # VISUAL: Base. Late night. Most lights off. People sleeping. Quiet.
    # LIGHTING: Dim emergency lights. One bright area - operations room.
    # SOUND: Silence. Occasional distant footstep. City hum outside.

    scene bg_base_night with fade

    "{i}Late night. Can't sleep. Again. Nightmares. Glass. Sweep. 600 faces. Same dream every night. Different details but same ending. Blood. Screaming. Waking up in cold sweat. Gave up trying. Came to operations room instead. Maybe work will quiet the noise.{/i}"

    # VISUAL: Walking through dark base. People sleeping in quarters. Peaceful. Contrasts with Aeron's insomnia.
    "{i}Base quiet. Everyone sleeping. Peaceful. Normal. They can sleep. I can't. Glass doesn't sleep. Glass doesn't deserve peace. Old habit. Old punishment. Carrying ghosts. They're heavy tonight.{/i}"

    # VISUAL: Operations room ahead. Single light on. Someone else awake. Who?
    "{i}Operations room. Light on. Someone else awake. Who works this late? Everyone should be sleeping. Tactically inefficient to skip rest. But I'm doing it too. Hypocrite.{/i}"

    # VISUAL: Door opening. NOELLE at workstation. Surrounded by datapads. Working. Intense focus.
    scene bg_operations_room_night with fade

    "{i}Noelle. Of course. She's always working. Always analyzing. Always processing. Surrounded by datapads and holographic displays. Data everywhere. She's... frustrated? That's new. Noelle doesn't do frustration. Noelle does efficiency.{/i}"

    # VISUAL: Noelle hasn't noticed Aeron. Too focused. Muttering to herself. Calculations. Frustrated.
    n "(muttering) No. That's incorrect. The variable coefficient is wrong. Recalculate. Forty-seven iterations and it's still non-functional. This is unacceptable."

    # VISUAL: She slams datapad down. Rare display of emotion. Then notices Aeron.
    n "(looking up, startled) Aeron. You're awake. Current time is 0237 hours, which is suboptimal for sleep cycles. Why aren't you sleeping?"

    # VISUAL: Aeron entering. Sitting nearby. Not too close. Giving space.
    a "Could ask you the same thing. You've been here all night?"
    n "Yes. Since 2100 hours. Six hours and 37 minutes of continuous work, attempting to solve a problem that remains unsolved. It's frustrating."

    # VISUAL: Aeron surprised. Noelle admitting frustration is rare.
    a "You're frustrated. That's... I don't think I've seen that before."
    n "Frustration is a statistically rare emotional state for me. It occurs in approximately 3% of my work sessions, usually when a problem resists logical solution. This particular problem is exceptionally resistant."

    # VISUAL: Aeron curious. Leaning forward slightly. Interested.
    a "What are you working on?"
    n "A neural conditioning reversal algorithm. I'm attempting to undo Echelon's psychological programming. If successful, we could deprogram Banded soldiers and convert enemy combatants into resistance fighters. The recruitment increase would be exponential."

    # VISUAL: She pulls up displays. Shows complex neural patterns. Brain scans. Conditioning pathways.
    n "Echelon uses Bands to enhance bodies, but they also use psychological conditioning to control minds. Loyalty programming. Obedience protocols. It makes soldiers compliant, predictable, controllable."
    n "If I can reverse the conditioning, soldiers would remember who they were before Echelon. They'd remember choice. Remember free will. They'd defect. Join us. We'd turn Echelon's strength into our strength."

    # VISUAL: Aeron processing. This is huge. Game-changing if it works.
    a "That's... that's brilliant. If that works, we don't need to fight Echelon's army. We convert it."
    n "Correct. The strategic value would be immeasurable. The tactical impact could win the war. The problem is that I can't solve it. Forty-seven iterations, all failures. The algorithm doesn't account for something. There's a missing variable, and I can't identify what it is."

    # VISUAL: Frustration showing again. Rare vulnerability from Noelle.
    n "I've processed every data point. Every neural pattern. Every conditioning pathway. The math is correct. The logic is sound. But the algorithm fails every simulation. Something is wrong and I can't identify it."
    n "Not being able to solve a problem, not understanding why a solution doesn't work... it's unpleasant. I'm experiencing emotional discomfort. Frustration. Anger at my own inadequacy."

    # VISUAL: Aeron moving closer. Looking at displays. Trying to understand.
    a "Show me. Walk me through it. Maybe a fresh perspective helps."
    n "You're not a data analyst. Your expertise is in tactical operations and—"
    a "—and I was conditioned by Echelon. I lived through their programming. Maybe I can see something you can't, from an inside perspective."

    # VISUAL: Noelle considering. Logic processing. Decides to try.
    n "...That's a valid point. Experiential knowledge versus theoretical analysis. Your input may provide the missing perspective. Very well."

    # VISUAL: She pulls up neural conditioning model. Explains. Complex but clear.
    n "Echelon's conditioning works in three layers. The surface layer handles behavioral compliance. The middle layer manages emotional suppression. The deep layer controls identity replacement."
    n "Surface conditioning is easy to reverse—simple deprogramming techniques work fine. Middle layer is harder but still possible. But the deep layer? The deep layer resists every reversal attempt I've designed."
    n "The deep layer is where Echelon replaces who you were with who they want you to be. Identity erasure. Personality overwrite. This is what creates perfect soldiers. And this is what I can't undo."

    # VISUAL: Aeron staring at display. Recognition. Personal. This is him. Was him.
    a "Identity replacement. That's... that's what Glass was. They took who I was and made me Glass. Perfect soldier. No emotions. No doubts. No mercy. Just efficiency."
    n "Yes. You experienced deep layer conditioning. But you broke it. You 'cracked,' as you call it. That's anomalous. Deep conditioning doesn't break spontaneously. Yet yours did. Why?"

    # VISUAL: Aeron thinking. Remembering. The child. The mercy. The crack.
    a "The child. During the Sweep. I was ordered to terminate her. 600 targets. She was target 391. But she looked at me and I... couldn't. Something in me refused. Broke through the conditioning. I remembered I was human. Remembered choice."
    a "Giving her mercy broke Glass. Broke the conditioning. Let Aeron come back."

    # VISUAL: Noelle processing. Eyes widening. Recognition. BREAKTHROUGH.
    n "...Choice. Choice! That's the missing variable. Conditioning replaces identity, but it can't eliminate choice completely. Choice is fundamental—a core human element. Conditioning suppresses it but doesn't erase it."
    n "When you gave mercy, you chose. Against orders. Against programming. Against conditioning. Your choice broke the conditioning because choice is deeper than programming."

    # VISUAL: She's typing rapidly. Updating algorithm. Excited. Breakthrough happening.
    n "The algorithm was trying to reverse conditioning externally. Wrong approach. Conditioning breaks from internal choice. I need to trigger the choice mechanism—make the conditioned soldier choose something against their programming."
    n "A small choice. A simple choice. But their choice. Not ours. Not Echelon's. Theirs. The choice reactivates the suppressed identity. The identity fights the conditioning. The conditioning breaks."

    # VISUAL: Algorithm updating. Simulations running. SUCCESS. Models showing reversal working.
    n "It's working. The algorithm is functioning. Reversal success rate is climbing—73%, 78%, 84%, 89%! It's working!"

    # VISUAL: She turns to Aeron. Eyes bright. Excited. Rare genuine smile.
    n "You solved it. I spent 47 hours processing this problem, and you solved it in..."
    
    # VISUAL: Checks time.
    n "...11 minutes. You casually solved a 47-hour problem in 11 minutes. That's statistically improbable. That's exceptional. That's..."
    n "That's fascinating."

    # VISUAL: Looking at him differently. Not just ally. Not just resistance member. Something else.
    n "Your mind is fascinating. You approached the problem from an experiential angle I couldn't access. You provided a perspective I was lacking. You completed my incomplete analysis."
    n "That's valuable. That's rare. Ninety-four percent of people bore me within six minutes—their thinking is predictable, obvious, redundant. But you..."
    n "You don't bore me. Your thought processes are interesting, non-standard, unexpected. I enjoy analyzing how you think. That's unusual for me. Very unusual."

    # VISUAL: Aeron surprised. Noelle complimenting him? Rare. Maybe never happened before.
    a "I just... I lived through it. I remembered. You did the hard part—the analysis, the algorithm, the science."
    n "No. You provided critical insight. Without your input, the algorithm would still be non-functional. This is a collaborative success. Your contribution was essential."
    n "You're intelligent. More intelligent than you present yourself as being. You hide it behind tactical focus and self-deprecation. But your mind processes complex problems efficiently. Pattern recognition. Intuitive leaps. Emotional-logical integration."
    n "Most people think in straight lines. You think in... networks. Connections. Webs of causality. It's compelling to observe."

    # VISUAL: Silence. Comfortable. Both processing. Moment stretching.
    "{i}She's looking at me like I'm data. But good data. Interesting data. Data worth studying. Coming from Noelle, that's something. She doesn't waste attention on boring things. If I'm interesting to her, that matters somehow.{/i}"

    # VISUAL: Noelle still looking at display. Then at Aeron. Then back. Processing something.
    n "You're still awake at 0248 hours. Insomnia?"
    a "Nightmares. Can't sleep. Gave up trying."
    n "Nightmares about the Sweep?"
    a "...Yeah. Every night. 600 faces. Especially her. The child. Target 391. I saved her, but I killed 390 others. That doesn't balance. Doesn't fix anything. Doesn't erase it."

    # VISUAL: Noelle processing. Logical response forming. But also... empathy? Trying.
    n "Guilt is a logical response. You terminated 390 people. Ethical assessment: negative action. But you also saved 391. Ethical assessment: positive action. Plus your subsequent resistance activities—22 documented lives saved. The probability that you've saved more lives than you've taken is currently 67%."
    n "Mathematically, the balance is shifting toward the positive. But emotionally... emotions don't calculate mathematically. Your guilt persists despite logical mitigation. That's inefficient, but it's also human. Very human."

    # VISUAL: She's trying to comfort him. Using logic because that's her language. It's awkward but genuine.
    n "I don't experience guilt the way you do. I experience frustration at inefficiency, anger at unsolved problems, satisfaction at breakthroughs. But guilt? Shame? Those are foreign to me."
    n "But I observe you experiencing them. And I observe them causing you distress—sleep deprivation, psychological strain, reduced operational efficiency. I don't... I don't prefer that."
    n "I prefer you operational. Functional. Present. Because when you're present, I can work with you. And working with you is pleasant. Eighty-seven percent pleasant. Possibly 91%."

    # VISUAL: Aeron caught off guard. Noelle just said she likes working with him. In her language. That's significant.
    a "Eighty-seven percent pleasant? That's... that's high for you, isn't it?"
    n "Extremely high. Most interactions rate between 23 and 45% pleasant—neutral to mildly positive. Yours consistently rate above 80%. That's a statistically significant outlier. You're in the 98th percentile for pleasant interaction. That's exceptional."

    # VISUAL: Silence again. Both tired. Both comfortable. Strange intimacy in data talk.
    n "Your nightmares prevent sleep. Sleep deprivation degrades cognitive function. Cognitive degradation reduces your effectiveness. Your reduced effectiveness makes you less able to save people. So your guilt causes the very thing you're guilty about. It's a logical paradox."
    a "Yeah. I know. Can't logic away guilt, though. Doesn't work like that."
    n "That's unfortunate. Logic solves most problems. Emotions are inefficient variables—they resist optimization. But they're also what makes you... you. Your capacity for guilt means you have capacity for empathy. Empathy drove the mercy. Mercy broke the conditioning. The conditioning break enabled your defection. Your defection enabled the resistance. The resistance saves lives."
    n "So your emotions, however inefficient, are strategically valuable. Your guilt is unpleasant for you to experience, but it makes you an effective moral agent. That's a net positive, even if it doesn't feel positive."

    # VISUAL: Aeron processing. Noelle trying to make him feel better using data. It's working somehow.
    a "You're trying to make me feel better. Using statistics."
    n "Yes. Is it working?"
    a "...Actually, yeah. A little bit. You're good at this."
    n "That's an incorrect assessment. I'm terrible at emotional support—I have approximately a 12% competency rating in empathetic communication. But I'm trying. Because you're distressed. And your distress is unpleasant for me to observe."
    n "That's new. Normally I don't care about others' emotional states. They're irrelevant data. But yours isn't irrelevant. Yours affects me. I notice when you're distressed. I want to mitigate it. That's unusual."

    # VISUAL: She's looking at him. Confusion in eyes. Analyzing herself now. Not just him.
    n "I should clarify something. I experience elevated heart rate when you're in proximity—approximately 23% increase. Dopamine spikes during conversation. Cortisol reduction when you're present. Oxytocin elevation when you're engaged in intellectual exchange with me."
    n "These are measurable physiological responses, but I don't have a framework to interpret them. I've never experienced these patterns before. They're anomalous. And I don't understand them. That's frustrating—I don't like not understanding things."

    # VISUAL: Aeron realizing. She's describing attraction. But she doesn't know that. She's analyzing it like data.
    a "Noelle... those responses. The heart rate, the dopamine, the comfort when I'm around. That's not just data. Those are feelings."
    n "Feelings? No. Feelings are emotional responses. These are physiological responses. Measurable. Quantifiable. Data."
    a "Data that indicates feelings. Your body is telling you that you... that you like being around me. More than just as a colleague. More than just as an ally."

    # VISUAL: Noelle processing. Eyes widening. Recognition. Fear? Confusion? Both?
    n "I... that's not logical. I don't 'like' people. I assess utility. I calculate value. I process relationships as strategic assets. I don't experience preference based on emotion."
    n "But you're correct. The physiological data supports your hypothesis. Heart rate elevation, dopamine response—these correlate with attraction. With preference. With..."
    n "With feelings."

    # VISUAL: She looks panicked. Noelle never looks panicked. But she does now.
    n "I don't know how to process this. There's no algorithm for this. No formula. No model. I can predict Echelon patrol patterns with 89% accuracy. I can calculate battle outcomes. I can solve neural conditioning problems. But this? This is unsolvable. There's no unit for measuring this."

    # VISUAL: Aeron gentle. Not pushing. Just present. Letting her process.
    a "Maybe it doesn't need measuring. Maybe it just... is."
    n "That's unacceptable. Everything needs measurement. Everything needs quantification. How else do you understand it? How else do you control it? How else do you know it's real?"

    # VISUAL: Breathing faster. Genuine distress. First time seeing Noelle truly rattled.
    a "Hey. Hey. It's okay. You don't have to understand it right now. You don't have to quantify it. You can just... let it exist. Let it be uncertain. That's okay."
    n "Uncertainty is inefficient. Uncertainty creates errors. I don't do uncertainty."
    a "You do now. And that's okay. I'm uncertain about a lot of things—my guilt, my purpose, my identity. But I'm still here. Still functioning. Uncertainty doesn't break you. It's just uncomfortable."

    # VISUAL: Noelle looking at him. Processing. Trying to accept uncertainty. Struggling but trying.
    n "I've spent 47 hours trying to solve the neural conditioning problem. I solved it in 11 minutes with your help. But this problem—my physiological responses to you—I can't solve it. Not in 11 minutes. Not in 47 hours. Maybe not ever."
    n "That should terrify me. An unsolvable problem existing in my own neurochemistry. But instead I feel... curious. I want to keep experiencing it. Keep observing it. Keep being around you to see what happens next."
    n "That's not logical. That's not efficient. But it's what I want. And 'want' is emotional, not data. It's emotional."
    n "I'm experiencing emotions about you. That's terrifying and fascinating simultaneously. Fifty percent terrifying, fifty percent fascinating. Perfectly balanced. Perfectly paradoxical."

    # VISUAL: Small laugh. Self-aware. Vulnerable. Real. Noelle being human. Rare sight.
    n "I'm analyzing my own feelings like they're data because that's all I know how to do. But they resist analysis. They're not data. They're just... feelings. And I don't know what to do with that."

    # VISUAL: Aeron reaches out. Gently. Slowly. Touches her hand. Small contact. Testing.
    a "You don't have to do anything with it. Just acknowledge it. Let it exist. See where it goes. No pressure. No timeline. No measurement required."

    # VISUAL: Noelle looking at his hand on hers. Processing. Touch. Physical contact. Elevated heart rate. Dopamine. Oxytocin. Data and feeling mixing.
    n "Physical contact elevates the responses. Heart rate is now 31% above baseline—that's a significant increase. But it's not unpleasant. It's... pleasant. Eighty-nine percent pleasant. Maybe 93%."
    n "You're touching me and I'm quantifying my response to being touched. That's absurd. But it's also comforting, because quantification is familiar. And you're becoming familiar. Comfortably familiar."

    # VISUAL: She doesn't pull away. Lets contact remain. Processing. Accepting. Trying.
    n "I should sleep. It's 0312 hours—suboptimal time to still be awake. But I don't want to stop this conversation. This interaction. This moment. Even though it's inefficient, even though it's not solving problems, I want to stay here. With you. That's an emotional decision, not a logical one. It's emotional."
    n "I'm making emotional decisions about you. That's new. That's significant. That's important to acknowledge."

    # VISUAL: Aeron smiling. Small. Gentle. Not pushing. Just present.
    a "Then stay. If you want. We can just sit here. No problem-solving. No analyzing. Just existing. Together. That's allowed."
    n "Existing without productivity. That's illogical. But... acceptable. In this specific context. With you. Ninety-one percent acceptable. Possibly 94%."

    # VISUAL: They sit together. Silence. Comfortable. Her hand still under his. Quiet moment. No words needed.
    "{i}Sitting with Noelle. Operations room. 0312 hours. Both exhausted. Both awake. Both together. She's processing feelings like data. I'm processing data like feelings. Maybe we're teaching each other. Maybe that's what connection is—learning each other's language, speaking across the difference, understanding without full comprehension.{/i}"

    # VISUAL: Time passing. Minutes. Just being together. Eventually Noelle speaks.
    n "Thank you. For solving the problem with me. For letting me process this emotional situation. For not demanding that I understand it immediately. For being patient with my inefficient emotional processing."
    n "You're in the 98th percentile for pleasant interaction. That statistic is accurate. You make uncertainty feel less threatening. That's valuable. That's rare. That's... that's you."

    # VISUAL: Standing. Both exhausted. Should sleep. But moment was important.
    n "I should attempt sleep. Four hours remaining before the operational day begins. Suboptimal but necessary. You should also sleep. Your nightmares are manageable—22 people saved and counting. The math is shifting toward positive. Remember that."
    a "I'll try. And Noelle?"
    n "Yes?"
    a "I'm in the 98th percentile for pleasant interaction? You're in the 100th percentile. Just so you know."

    # VISUAL: Noelle processing. Eyes widening. Small smile. Genuine. Rare. Beautiful.
    n "One hundredth percentile. That's the maximum rating. That's the optimal outcome. That's..."
    n "That's 100% pleasant. The highest possible measurement."
    n "Thank you for that data point. I'll process it. Extensively. Probably all night. But pleasantly. Ninety-seven percent pleasantly. Possibly 99%."

    # VISUAL: She leaves. Door closing. Aeron alone. But less alone. Connection made. Important. Real.
    "{i}Alone in operations room. But not lonely. Noelle just shared something—vulnerability, feelings she doesn't understand. She analyzed them with me. Trusted me with her uncertainty. That matters. That's intimacy. Strange intellectual intimacy. But intimacy nonetheless.{/i}"

    # VISUAL: Returning to quarters. Maybe sleep will come easier. Maybe nightmares quieter. Maybe.
    "{i}Returning to quarters. 0327 hours. Exhausted. But a different kind of exhausted. Connected exhausted. Noelle's trying to understand feelings. I'm trying to understand redemption. We're both uncertain. Both processing. Both learning. Maybe that's enough. Maybe that's everything. Maybe that's 97% pleasant. Possibly 99%.{/i}"

    # Mark scene complete
    $ scenes["noelle_working_late"] = True
    $ characters["noelle"]["affection"] += 3
    $ characters["noelle"]["intellectual_intimacy"] = True
    $ characters["noelle"]["aware_of_feelings"] = True  # She knows but doesn't understand yet

    # TRANSITION: Night ending. Morning approaching. Connection deepening.
    scene black with fade

    return

    # canon_note: Scene 11 complete - Noelle intellectual intimacy established
    # canon_note: Neural conditioning reversal algorithm breakthrough (Aeron's insight critical)
    # canon_note: Noelle realizes she has feelings but can't quantify them ("no unit")
    # canon_note: Describes physiological responses (heart rate, dopamine) like data
    # canon_note: First physical contact (hand touch) - highly pleasant (89-93%)
    # canon_note: Aeron rates 98th percentile pleasant interaction, she's 100th for him
    # canon_note: She's processing feelings overnight (won't sleep, analyzing)
    # canon_note: Foundation for "no unit" scene later (Scene 16 Act 2)
    # canon_note: Intellectual attraction → emotional attraction pathway beginning
    # canon_note: Algorithm success = major strategic win (can deprogram Echelon soldiers)
    # canon_note: Aeron's guilt addressed through Noelle's logic (22 saved, math shifting positive)
    # canon_note: Beautiful autism-coded representation - not robotic, genuinely struggling with emotions
    # canon_note: "You don't bore me" = highest compliment Noelle can give
    # canon_note: Sets up deeper romance development if player chooses that path
    # canon_note: REVISED - Natural speech patterns, complete sentences, analytical but human