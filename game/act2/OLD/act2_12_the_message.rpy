# act2_12_the_message.rpy


# =======================================================
# ACT 2 - Scene 12: The Message
# =======================================================


label act2_the_message:

    # --- SCENE START (new helper system) ---
    $ mark_scene("act2_the_message", start=True)
    $ log_line("act2_the_message", "enter")

    # VISUAL: Safe house. Evening of Day 8. All activities complete.
    # LIGHTING: Dim. Tired. Accomplished but anxious.
    # SOUND: City hum. Waiting. Tension.

    scene bg_safe_house with fade

    "Day 8. Seven tasks complete. Every single one. Now we wait for Selene's answer."
    "[ob] Waiting is just combat without bullets—same pulse, same math."
    
    # VISUAL: Aeron and Lyra sitting. Exhausted. Week of survival behind them.
    # Different people than they were seven days ago.

    l "Do you think she'll respond?"
    a "Zira said she would. Eventually. Whether that response is a meeting or a bullet remains to be seen."
    l "Optimistic as always."
    a "Realistic. We killed 600 people in her sector. She has every reason to want us dead."
    l "But we also did everything Zira asked. Proved we're serious. That has to count for something."
    a "Maybe. Or maybe it just proves we're desperate enough to be useful before she kills us."

    # VISUAL: Lyra quiet. Both processing. Week of growth but still hunted.
    "Seven days ago we fled Aeries with nothing. Now we're armed, connected, skilled. Different. Stronger maybe. Still hunted but less helpless."
    "[emp] Progress doesn’t erase guilt, but it gives it somewhere to stand."

    # Show what they've accomplished
    $ total_scrip = inventory["scrip"]
    $ weapon_count = len(inventory["weapons"])
    $ reputation_score = reputation["unders"]
    $ log_line("act2_the_message", f"status scrip={total_scrip} weapons={weapon_count} rep_unders={reputation_score}")

    athought "We have [total_scrip] scrip. [weapon_count] weapons. Reputation in the Unders at [reputation_score]. Contacts who might not kill us on sight. That's progress."

    l "What if she says no? What if we did all of this and she still won't help us?"
    a "Then we find another way. We always find another way."
    l "There might not be another way. Selene's the only organized resistance left. Everyone else scattered after the Purge."
    a "Then we build something new. From nothing. Like we've been doing."
    l "Two people against an empire."
    a "Two people who know that empire. Who were that empire. If anyone can tear it down, it's us."

    # VISUAL: Moment of quiet confidence. Changed from broken fugitives to something more.
    "She looks at me different now. Not like Glass. Not like a weapon. Like someone who might actually do what he says. Maybe I'm starting to believe it too."
    "[emp] Belief is a thin blanket, but it’s warmer than fear."

    # SOUND: Encrypted device beeps. Loud. Sudden. Both tense immediately.
    # VISUAL: Zira's device on table. Message incoming. This is it.

    "The device. Beeping. Message incoming. This is it. Selene's answer."
    "[ob] Hope arrives dressed like an alarm."

    # VISUAL: Both stare at device. Neither moving. Moment of truth.
    l "Are you going to check it?"
    a "...Yeah. Just... preparing for bad news."
    l "Always preparing for bad news."
    a "It's kept me alive so far."

    # VISUAL: Picks up device. Reads message. Face unreadable.
    "Message from Zira. Encrypted. Short. Selene's answer."

    # Display message text
    "MESSAGE: 'She'll meet. Tomorrow. Dawn. Sector 6 ruins. Neutral ground. She's bringing guns. You fuck around, you die. Don't be late. - Z'"

    # VISUAL: Aeron exhales. Relief and terror mixing.
    a "She'll meet."
    l "That's good. Right? That's what we wanted."
    a "It's a chance. More than I expected. Less than I hoped for."
    l "What do you mean?"

    # VISUAL: Shows her the message. She reads. Face hardens.
    a "Neutral ground. Armed. One wrong move means death. She's not trusting us. She's testing us."
    l "Can you blame her? We swept her sector. Killed her people. She'd be stupid to trust us."
    a "No. I can't blame her. But it means tomorrow could go very wrong very fast."
    l "It could. Or it could be the start of something. A real alliance. A real resistance."
    a "...Yeah. Or that."

    # VISUAL: Both processing. Tomorrow everything changes. Again.
    "Tomorrow. Dawn. Sector 6. Meeting Selene. The woman whose people I killed. Who lost everything in the Purge. Who might kill us on sight or give us a chance. Everything rides on this."
    "[ob] The future has a trigger; we’re walking toward it."

    l "We should rest. Tomorrow's going to be intense."
    a "Rest. Right. Like I'm going to sleep tonight."
    l "Try anyway. We need to be sharp. Alert. Ready for anything."
    a "When aren't we ready for anything? That's all we've done for two weeks. Be ready for anything."
    l "Then one more night won't hurt. Come on. Lie down. Even if we don't sleep, rest helps."

    # VISUAL: They settle in. Makeshift bed. Close proximity natural now.
    # After the intimate scene (if it happened), this is comfortable. If not, still close but less intimate.

    if characters["lyra"]["lewd_scene_completed"]:
        "She curls against me. Natural now. Comfortable. Her warmth grounding. We've been through too much to sleep apart anymore."
        l "(quiet) No matter what happens tomorrow, we face it together. Right?"
        a "Always together. That's how we've survived everything. That's how we'll survive this."
        l "Good. Because I don't want to do any of this without you."
        a "You won't have to. I'm here. I'm not going anywhere."
        "[emp] The city takes, but tonight it leaves us this: a steady breath against my chest."
    else:
        "She lies close. Not touching but near. Presence comforting even without intimacy. We've been through enough that proximity means trust."
        l "(quiet) Tomorrow changes everything."
        a "Tomorrow's just another day of survival. We're good at those."
        l "This feels different. Bigger. Like we're standing at a cliff edge."
        a "Then we jump together. Like always."
        l "...Yeah. Together."
        "[emp] Distance measured in inches can still mean safety."

    # VISUAL: Darkness. Quiet. Both pretending to sleep. Neither succeeding.
    "Hours pass. Neither of us sleeps. Just lie there thinking. Planning. Preparing. Tomorrow we meet Selene. Tomorrow we either join the resistance or die trying. No middle ground. No safety net. Just one chance to prove we're more than the monsters we were."
    "[ob] Plans line up like bullets in a magazine; dawn is the chamber."

    # VISUAL: Check weapons. Check gear. Check everything twice.
    athought "Weapons ready. Gear packed. Fake IDs solid. Everything prepared. But preparation only goes so far. Eventually you have to face the moment. Face the person. Face the choice."

    # VISUAL: Pre-dawn darkness. Time passing.
    "Pre-dawn. The city quiet. That strange hour when night dies but day hasn't born yet. Time to move."
    "[ob] Night exhales; we hold our breath for the reply."

    # VISUAL: Both rising. Dressing. Gearing up. Professional. Focused.
    scene bg_safe_house_dawn with fade

    l "Ready?"
    a "No. But when has that ever stopped us?"
    l "Fair point. Let's go meet our future. Or our death. Whichever comes first."
    a "You're getting dark in your old age."
    l "I learned from the best."

    # VISUAL: One last look at safe house. Might not return. Everything on the line.
    "One last look. This room kept us alive for eight days. Might never see it again. Might die in Sector 6. Might join the resistance. Might start a war. Everything uncertain except one thing: we're doing this together."
    "[emp] Together has been our best armor."

    # VISUAL: Door opens. Dawn light spills in. Step into uncertain future.
    a "Let's go. Time to face Selene."
    l "Time to face everything."

    # TRANSITION: Journey to Sector 6. Dawn breaking. City waking. Future approaching.
    # VISUAL: Walking through Lower Spans. Toward ruins. Toward meeting. Toward fate.

    scene bg_lower_spans_dawn with fade

    "Walking through dawn-lit streets. Sector 6 ahead. Ruins where Selene waits. Where everything either begins or ends. Eight days of preparation leading to this moment. Seven tasks completed. One final test remains."
    "[ob] The light is thin and honest; it shows the cracks and keeps going."

    # Check inventory and relationships one final time
    $ weapons_ready = len(inventory["weapons"]) > 0
    $ lyra_trust_final = characters["lyra"]["trust"]
    $ reputation_final = reputation["unders"]
    $ log_line("act2_the_message", f"premeet armed={weapons_ready} lyra_trust={lyra_trust_final} rep_unders={reputation_final}")

    "Armed: [weapons_ready]. Lyra's trust: [lyra_trust_final]. Reputation: [reputation_final]. Everything we've built. Everything we've earned. All riding on the next hour."

    # VISUAL: Sector 6 ruins visible ahead. Dawn breaking over devastation.
    "There. Sector 6 ruins. Dawn breaking through broken buildings. Selene's there somewhere. Waiting. Watching. Deciding if we live or die."

    l "(whisper) I see movement. Rooftop. Left side."
    a "Snipers. She brought backup. Smart."
    l "Are we walking into an execution?"
    a "Maybe. But we're walking anyway. No other choice."
    l "There's always a choice."
    a "Not anymore. Not for us. We're committed. Have been since we left Aeries."
    l "Then let's finish what we started."

    # VISUAL: Enter ruins. Cautious. Alert. Every sense heightened.
    scene bg_sector6_ruins with fade

    "Sector 6. Ruins from the Purge. Buildings collapsed. Streets torn. Perfect place for an ambush. Perfect place for a meeting. Perfect place to die or be reborn."
    "[emp] My pulse hammers a steady drum: approach, breathe, don’t flinch."

    # SOUND: Footsteps ahead. Multiple. Armed. Approaching.
    "Footsteps. Multiple. Armed. Coming closer. This is it. No turning back. Face Selene. Face judgment. Face the future."
    "[ob] History arrives in boots."

    # Mark scene state for downstream logic and UI
    $ mark_scene("act2_the_message", complete=True)
    $ log_line("act2_the_message", "exit_to_meet_selene")

    # TRANSITION: Meeting Selene begins

    # canon_note: Scene 6 complete - Selene's message received, meeting arranged
    # canon_note: Eight days passed - all seven activities completed
    # canon_note: Inventory and reputation finalized - ready for meeting
    # canon_note: Lyra relationship acknowledged - intimate scene impacts dialogue
    # canon_note: Meeting set: Dawn, Sector 6 ruins, armed, neutral ground
    # canon_note: Tension built - everything rides on this meeting
    # canon_note: Selene armed and cautious - testing them, not trusting
    # canon_note: Transition to Scene 7 - meeting Selene + dynamic crisis system begins
    # canon_note: Shows growth from Day 1 - scared fugitives to determined resistance fighters
    # canon_note: "Together" theme reinforced - facing everything as unit
    # canon_note: Final check of player progress - weapons, trust, reputation all matter

    return
