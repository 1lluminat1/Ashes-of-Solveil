# act2_activity_04_medical_supplies.rpy


# =======================================================
# ACT 2 - Activity 4: Medical Supplies (Meet Tessa)
# =======================================================
# TODO migrate legacy currency/contacts/reputation/activity counters to helper APIs
# Legacy touched below: activities_completed, days_remaining, medkits,
# contacts["tessa"], reputation_unders, favors_owed_list, activity_medical_done,
# tessa_count_the_living


label act2_activity_04_medical_supplies:

    # VISUAL: Lower Spans. Day. Sector 7. Hidden alley leading to underground clinic.
    # LIGHTING: Dim natural light filtered through grates above. Warm amber glow from clinic entrance.
    # SOUND: Distant city hum; voices murmuring; someone crying softly; life struggling.

    scene bg_sector7_alley with fade

    "Day 4. Activity: Medical Supplies."
    "Zira said find a medic. Someone who can patch us up when things go wrong."
    "Because things will go wrong. They always do."

    # VISUAL: Aeron following directions. Alley narrows. Graffiti on walls. Signs of life.
    "The address Zira gave me leads here. Sector 7. Deep in the Unders."
    "A clinic. Hidden. For people who can't afford Echelon's sanitized medicine."

    # VISUAL: Entrance marked with faded green symbol. Hand-painted. Medical cross.
    # SOUND: Voices inside. Someone groaning in pain. Someone speaking softly, gently.

    athought "Green mark. Medical cross. This is it."
    athought "Zira said her name is Tessa. Runs a scavenger-care commune."
    athought "Hybrid medicine. Organic and cybernetic. Whatever keeps people alive."

    # VISUAL: He pushes through hanging cloth serving as door. Enters clinic.
    # LIGHTING: Warm amber-green glow. Bioluminescent plants growing in corners. Soft, alive.
    # SOUND: Quiet. Reverent almost. People resting. Breathing. Healing.

    scene bg_tessas_clinic with fade

    "The clinic smells like herbs and antiseptic mixed together. Life trying to survive."
    "Makeshift beds line the walls. Injured people resting. Burns. Wounds. Sickness."
    "And in the center, kneeling beside a man with severe burns—her."

    # VISUAL: Tessa. Mid-20s. Dark hair tied back. Gentle hands glowing faint green.
    # She's applying bioluminescent gel to burn victim. Speaking softly. Calming.
    # LIGHTING: Green glow from her hands. Organic compound. Healing made visible.

    t "(soft, rhythmic) Breathe. That's all I'm asking right now. Just breathe with me."
    t "In through your nose. Hold it. Out through your mouth."
    t "Good. You're doing so well. I know it hurts, but you're here. You're alive."

    # VISUAL: Burn victim (male, 40s) trembling. Tears streaming. But breathing.
    "His skin is charred black in places. Red and weeping in others. Purge victim."
    "She works with steady hands. No hesitation. No revulsion. Just care."

    # VISUAL: Aeron stands at entrance. Watching. Something in his chest tightens.
    athought "She's healing someone I helped create. My mercy triggered the Purge."
    athought "These burns exist because I saved 200 people. Cascade of consequences."

    # VISUAL: Tessa looks up. Eyes meet his. Recognition immediate and complete.
    # Her hands don't stop working. Gel continues spreading. Patient comes first.

    $ mark_flag("Tessa", "met")

    t "(quiet, not stopping) You're Glass."

    # VISUAL: Injured man's eyes snap open. Others in clinic turn. Tension spikes instantly.
    # SOUND: Breathing changes. Fear. Anger. Recognition spreading like wildfire.

    "The name echoes in the small space. Glass. Everyone knows Glass."
    "Everyone lost someone to Glass. Sector 10. The Sweep. 600 dead."

    a "...Yes."

    # VISUAL: Tessa returns focus to patient. Doesn't look at Aeron. Keeps working.
    t "(to patient) It's alright. Stay still. I'm almost finished."
    t "(to Aeron, calm) Why are you here?"

    a "I need medical supplies. Someone said you—"
    t "I know what you need. I asked why you're here."
    t "(still not looking at him) In the Unders. Alive. When Echelon should be hunting you."

    # VISUAL: She finishes applying gel. Bandages the burns carefully. Tender and precise.
    t "(to patient) There. The gel will keep working for the next six hours. You'll feel it cooling."
    t "Rest now. I'll check on you in an hour."

    # VISUAL: Patient nods weakly. Looks at Aeron with mix of fear and hatred. Says nothing.
    # Tessa stands. Turns fully toward Aeron. Studies him. Not with hate. With sadness.

    t "You caused this. The Purge. These injuries. These deaths."
    a "I didn't—"
    t "Your actions triggered it. That's causation enough, even if you didn't light the fires yourself."

    # VISUAL: She walks to sink. Washes hands. Methodical. Centered. Processing.
    "She's calm. Too calm. Like she's decided something already."
    "Judgment rendered before I even explained."

    a "I'm not asking for forgiveness—"
    t "(turns, looks at him fully) Then what are you asking for?"

    # VISUAL: Long pause. What IS he asking for? Supplies? Absolution? A reason to keep going?
    a "...Help. I need help to keep fighting."
    t "Fighting who? Echelon? Or yourself?"

    # VISUAL: The question lands like a blade. Clean. Precise. True.
    athought "Herself? Both? I don't even know anymore."

    t "(softer now) Why are you here, Aeron? In the Unders. Away from everything you knew."
    t "You could have stayed in Aeries. Stayed Glass. Stayed safe."
    t "But you didn't. Why?"

    a "Because I watched 100,000 people die and I couldn't be part of that system anymore."
    a "Because I'm trying to fix what I broke. Even if I can't. Even if it kills me."

    $ adjust_empathy_once("act2_med_tessa_confession", +1)

    # VISUAL: She studies him. Eyes deep and warm and infinitely sad. Measuring truth.
    t "You can't fix 100,000 dead, Aeron. You can't patch souls with medicine."
    t "But you can help the living. If that's truly what you want."

    # VISUAL: She moves to cabinet. Opens it. Pulls out medkit. Well-stocked. Organized.
    # Places it on table between them. Offering. Testing.

    t "I'm Tessa Kael. I heal people. All people. Even those who don't deserve it."
    t "(looks at him directly) Which means you too. Despite everything."

    a "Why?"
    t "Because mercy isn't about deserving. It's about choosing."
    t "And I choose to believe you're here for the right reasons."
    t "(slight pause) Prove me right. Or prove me a fool. Either way, I'll have tried."

    # VISUAL: She pushes medkit toward him. Not freely given. Offered with expectation.
    athought "She's not forgiving me. She's giving me a chance."
    athought "Burden of proof. Earn it through action."

    a "I don't know if I deserve this chance."
    t "Probably not. But that's not for me to judge."
    t "I heal. You fight. We both serve life in different ways."
    t "(gentle but firm) Take the medkit. Use it to save someone. Then come back."
    t "Show me Glass can do more than cut."

    $ mark_flag("Tessa", "gave_medkits")
    $ adjust_empathy_once("act2_med_tessa_mercy", +1)

    # VISUAL: He takes medkit. Heavy. Not just weight. Responsibility. Expectation.
    a "Thank you."
    t "Don't thank me yet. Gratitude means nothing until you've earned it."
    t "Actions first. Words after."

    # VISUAL: He turns to leave. Stops. Looks back at burn victim. At others resting.
    a "These people. The burn victims. They're from the Purge?"
    t "Most of them, yes. Survivors from Sectors 8, 9, and 10."
    t "The ones who made it out. Barely."

    a "How many?"
    t "In my clinic right now? Fourteen. In all of Sector 7? Maybe a hundred."
    t "(quiet) Out of 100,000. That's the survival rate."

    # VISUAL: Numbers crushing him. 100,000 dead. 100 survived. Because of his mercy.
    athought "My mercy killed 99,900 people."
    athought "The arithmetic of guilt. It never balances."

    t "You're calculating, aren't you? How many died because of you."
    a "How did you—"
    t "I see it in your face. The weight. The math."
    t "(steps closer) Stop counting the dead, Aeron. Start counting the living."
    t "You can't bring back 100,000. But you can save the next hundred."
    t "That's how you fix it. One person at a time. Forever."

    # VISUAL: She says it simply. Like it's obvious. Like redemption is just arithmetic.
    a "That's... a long time."
    t "Yes. It is."
    t "(small sad smile) But you're here. Which means you're willing to try."
    t "That's more than most people manage."

    # VISUAL: Someone calls from across clinic. Another patient needs attention.
    voice "Tessa? I need help over here."

    t "Coming!"
    t "(to Aeron) I have to go. People need me."
    t "(hands him second medkit) Take this too. You'll need more than one."
    t "And Aeron? Come back when you've used them. I want to know who you saved."

    a "You want me to report back?"
    t "I want you to remember their names. The people you save."
    t "(firm) Because Glass killed 600 people. I want to know how many Aeron saves."
    t "Keep count. It matters."

    $ mark_flag("Tessa", "count_the_living")
    $ rel("Tessa", trust=3)

    # --- EMP/OB flavor: Post-Tessa resolve & medkit weight ---
    if get_empathy_band() != "obedience":
        # (EMP) keep original text verbatim
        "She didn't forgive me. Didn't absolve me. Didn't make it easier."
        "She just gave me work to do. People to save. A way forward."
        "Maybe that's better than forgiveness. Maybe that's what I need."

        athought "Keep count, she said. Remember their names."
        athought "600 dead. How many living to balance that?"
        athought "Infinite, probably. But I have to start somewhere."

        $ adjust_empathy_once("act2_med_post_tessa_resolve_emp", +1)

    else:
        # (OB) clinical framing; same dramatic beat, different lens
        "She didn't forgive me. She assigned a queue."
        "Not absolution—operations. Triage. Throughput. Deliverables."
        "Forgiveness is nonfunctional. Output is not."

        athought "Two medkits: finite resources, measurable outcomes."
        athought "Stop optimizing for the dead ledger. Maximize marginal lives saved."
        athought "Start now. Iterate until failure rate trends down."

        $ adjust_empathy_once("act2_med_post_tessa_resolve_ob", -1)

    # VISUAL: He turns to leave. Stops at doorway. Looks back one more time.
    # Tessa kneeling beside another patient. Green glow surrounding her hands. Healing.
    # --- EMP/OB flavor on Tessa reflection ---
    if get_empathy_band() != "obedience":
        athought "Tessa Kael. Healer. Heart of the Unders."
        athought "She sees the worst humanity has to offer and chooses compassion anyway."
        athought "Glass killed. Tessa heals."
        athought "Maybe that's who I need to learn from."
        $ adjust_empathy_once("act2_med_tessa_reverence", +1)
    else:
        athought "Tessa Kael. Field asset. High-value node in the Unders’ care network."
        athought "She absorbs systemic damage and outputs survival. Throughput matters."
        athought "Glass executed directives. Tessa executes outcomes."
        athought "I don't need her compassion. I need her protocols."
        $ adjust_empathy_once("act2_med_tessa_pragmatic", -1)

    # TRANSITION: Return to safe house. Report to Zira. Activity complete.
    scene bg_safe_house with fade

    # VISUAL: Zira sees the medkits. Raises eyebrow. Impressed.
    z "Two medkits? She must like you."
    a "She doesn't like me. She's testing me."
    z "Same thing with Tessa. She only tests people she thinks are worth saving."
    z "(grins) Told you to find a medic. Didn't expect you'd find the best one in the Unders."

    a "She knew who I was. Immediately."
    z "Everyone knows who you are, Glass. You're famous down here."
    z "But Tessa doesn't work in hate. She works in hope."
    z "If she gave you medkits, she's hoping you'll prove her right."

    a "She said to come back. After I've used them. Tell her who I saved."
    z "(softens) That sounds like Tessa. She collects names. Remembers everyone she heals."
    z "Says it matters. That people deserve to be remembered."

    # VISUAL: Aeron looks at medkits. Responsibility weighing.
    a "What if I can't save anyone? What if I just make things worse?"
    z "Then you try again. That's what Tessa does. Every day."
    z "She loses patients. She loses people she cares about. But she keeps trying."
    z "(firm) That's what separates people like her from people like Echelon."
    z "Echelon stops trying. Tessa never does."

    a "She's... different. From anyone I've met."
    z "She's the best of us. Proof that kindness can survive even here."
    z "Learn from her. Let her teach you how to save people instead of killing them."
    z "(slight smile) Might be good for your soul. If you still have one."

    a "I'm not sure I do."
    z "Then let Tessa help you grow a new one. She's good at that."

    # VISUAL: Aeron stores medkits carefully. Precious cargo. Lives waiting.
    # --- EMP/OB flavor on the "count the living" vow ---
    if get_empathy_band() != "obedience":
        athought "Keep count. Remember their names."
        athought "600 dead. Now I count the living."
        athought "Starting now. Starting with whoever I save next."
        $ adjust_empathy_once("act2_med_count_living_ack", +1)
    else:
        athought "Inventory secured. Two kits, two chances."
        athought "Names don't stop bleeding. Procedures do."
        athought "Triage. Stabilize. Move. Save who can be saved."
        $ adjust_empathy_once("act2_med_count_living_hardline", -1)

    # TRANSITION: End of activity. Rewards gained. Contact added.

    # REWARDS SUMMARY SCREEN:
    "{b}Activity Complete: Medical Supplies{/b}"
    "
    Rewards:
    - Medkit x2 (Can save critically injured allies)
    - Contact Added: Tessa Kael (Healer, Compassion)
    - Reputation: +2 (Tessa vouched for you to local community)
    - Favor Owed: Tessa helped you; you owe her proof of change
    
    New Philosophy Unlocked: 'Count the Living'
    - Track people saved, not just people killed
    - Redemption through action, not words
    - Names matter; remember everyone
    
    Tessa's clinic is now available as a safe location.
    Return after using medkits to deepen relationship.
    "

    # Legacy counters/inventory (awaiting migration helpers)
    $ activities_completed += 1
    $ days_remaining -= 1
    $ medkits += 2
    $ contacts["tessa"] = {
        "name": "Tessa Kael",
        "trust": 3,
        "met": True,
        "skills": ["healing", "empathy", "bio_mechanics"],
        "location": "Sector 7 Clinic"
    }
    $ reputation_unders += 2
    $ favors_owed_list.append("tessa_proof_of_change")
    $ activity_medical_done = True
    $ tessa_count_the_living = True  # Philosophy flag for tracking saves

    # canon_note: Tessa introduced - field medic, bio-mechanic, emotional heart
    # canon_note: "Count the living" philosophy - track saves not kills, redemption through action
    # canon_note: She doesn't forgive Aeron, but gives him chance to prove himself
    # canon_note: Purge survivors in her clinic - physical manifestation of Aeron's guilt
    # canon_note: 100,000 dead vs 100 survived - harsh arithmetic of consequences
    # canon_note: "Mercy isn't about deserving, it's about choosing" - core Tessa belief
    # canon_note: She gave TWO medkits - more generous than necessary (she sees potential)
    # canon_note: Wants him to return with names of people saved - accountability
    # canon_note: Her clinic becomes safe house later (Act 2 Scene 20)
    # canon_note: Green glow = bioluminescent healing gel (her signature)
    # canon_note: She collects names, remembers everyone - opposite of Echelon's erasure
    # canon_note: Tessa's role: teaches Aeron to save instead of kill, emotional grounding
    # canon_note: Romance path: pure empathy, unconditional compassion, emotional safety

    jump act2_activity_hub
