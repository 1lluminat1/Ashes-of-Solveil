# act2_02_reality_check.rpy
# =======================================================
# ACT 2 - Scene 2: The Unders - Reality Check
# OB/EMP integrated; Consolidated State Architecture hooks
# =======================================================

label act2_reality_check:

    # --- SCENE INIT / SNAPSHOT (dialogue-heavy; low counters) ---
    $ start_operation("op202_reality_check", note="Safehouse briefing & new identities")
    $ mark_scene("act2_02_reality_check", "started")
    $ log_line("ACT2_02 started: Reality Check in Zira safehouse")

    # VISUAL: Zira's safe house. Evening. Dim light. Small, cramped, functional.
    # LIGHTING: Single overhead bulb. Shadows deep. Industrial glow through window.
    # SOUND: City hum below; distant machinery; their breathing; exhaustion.

    "That Evening."

    # VISUAL: Aeron and Lyra sitting against wall. Hours passed. Exhausted. Processing.
    # Small space. Concrete walls. One window (barred). Door (locked from inside).

    "Hours in the dark. Waiting. Thinking. Surviving."
    "The safe house is small. Cold. But it's shelter."
    "And shelter is everything when the world wants you dead."

    # VISUAL: Aeron staring at nothing. Lyra checking her Band compulsively.
    # Both doing their coping mechanisms. Both barely holding together.

    if get_empathy_band() == "obedience":
        "He catalogs exits, angles, and timings; feelings are noise to be filtered."
    else:
        "He keeps counting breaths until the room stops spinning."

    athought "Seven hours since we left Aeries. Feels like seven years."
    athought "Everything we had—gone. Everything we were—ash."
    athought "And now we're here. Waiting for someone to decide if we live."

    # VISUAL: Lyra's hand moves to Band. Touches it. Checking. Automatic.
    "Her hand moves. Wrist. Band. Checking. Always checking."
    "Even here. Even now. Terrified it'll stop working."

    # (Lyra has seen Aeron’s alignment up close; she reads his tone accurately.)
    l "(quiet) Do you think she's coming back?"
    a "Zira? Yeah. She said she would."
    l "People say a lot of things."
    if pass_tier("OB2","OB3"):
        a "She saved us twice. Pattern holds until it doesn’t."
    else:
        a "She saved us. Twice. Why save us just to abandon us?"
        $ adjust_empathy_once("act2_02_trust_in_others", +1)

    l "(hollow laugh) Why do anything? Nothing makes sense anymore."

    # VISUAL: Silence. Both staring at nothing. Trauma settling. Reality crushing.
    "Silence. Heavy. The kind that presses on your chest."

    a "We can't stay here forever."
    l "Where else would we go?"
    a "I don't know. But this is temporary. Zira made that clear."
    l "Then what? We just... wander the Unders hoping not to die?"
    a "We survive. Then we plan. Then we—"
    l "(cuts him off) We what, Aeron? We're two people."
    l "Echelon has thousands. Weapons. Resources. Control."
    l "What exactly do we think we're going to do?"

    # VISUAL: He looks at her. Both broken. Both questioning. Reality hitting.
    a "...I don't know. But we said we'd burn them."
    l "We said a lot of things on that rooftop."
    l "Rage. Grief. Shock. Words aren't plans."
    a "Then we make a plan."
    l "With what? We have nothing."

    # VISUAL: Aeron looks around. Small space. Minimal supplies. No resources.
    athought "She's right. We have nothing."
    athought "No weapons. No intel. No allies. No future."
    athought "Just two broken people in a concrete box."

    # Empathy nudge on honest vulnerability (once)
    $ adjust_empathy_once("act2_02_name_the_void", +1)

    # SOUND: Door lock clicking. Beeps. Opening.
    # VISUAL: Both tense. Hands move toward weapons (they don't have).

    "The door opens. They freeze."
    "No weapons. Nothing but fists. And fists don't stop bullets."

    # VISUAL: Zira enters. Arms full of supplies. Kicks door closed behind her.
    # LIGHTING: Hallway light spills in, then cuts off. Dim bulb only source again.

    z "Still alive. Good. That's progress."
    if char_flag_has("Zira", "contacted_in_scene1"):
        z "(glances at Aeron) And this time you didn’t ping me three times in a row. Growth."
    else:
        z "(side-eye at their clothes) You two still look like a cautionary poster."

    # VISUAL: She drops supplies on floor. Food, water, clothes, basic necessities.
    # SOUND: Packages hitting concrete. Rustling. Reality of survival.

    z "Clothes. Food. Water. Fake IDs. Enough to last a few days."
    z "After that, you're on your own."

    # Inventory / state updates for supplies & disguises
    $ add_item("supplies", "food", 2)
    $ add_item("supplies", "water", 2)
    $ grant_disguise("unders")  # normalized set name
    $ mark_scene("act2_02_reality_check", "zira_supplied_kits")

    l "Fake IDs?"
    z "You think you can walk around as yourselves?"
    z "Echelon's posted your faces everywhere. Bounty on both heads."
    z "Big bounty. Tempting bounty."

    a "How big?"
    z "50,000 credits. Each. Dead or alive."
    z "(grins) Personally, I'd take dead. Less hassle."

    # Keep bounty consistent with player_state baseline
    $ player_state["bounty"]["aeron"] = 50000
    $ player_state["bounty"]["lyra"]  = 50000

    # VISUAL: Both process. That much money could change lives in the Unders.
    athought "50,000 credits. That's a fortune down here."
    athought "Everyone we meet is a potential killer. For the right price."

    l "Why haven't you turned us in?"
    z "Because 50,000 credits spends fast. But what you represent?"
    z "That's worth more."
    a "What do we represent?"
    z "Hope. Maybe. Or a really entertaining disaster."
    z "Either way, I'm curious."

    # VISUAL: She sits. Cross-legged. Comfortable. At home here.
    z "Alright. Reality check. You two need to understand where you are."
    z "The Unders aren't Aeries. Rules are different. Culture's different."
    z "Survival's different."

    a "We know it's dangerous—"
    z "(cuts him off) You don't know shit."
    z "You ran one operation down here. One night. Escorted."
    z "That's not knowing. That's tourism."
    if get_empathy_band() == "obedience":
        z "(to Aeron) And you still sound like you’re writing a field report."
    else:
        z "(to Aeron) And you look like you might finally be feeling it."

    # VISUAL: She leans forward. Eyes sharp. Making sure they hear this.
    z "The Unders don't have Echelon law. We have our own."
    z "Barter economy. Favors. Debts. Reputation."
    z "Your Aeries credits? Worthless unless you find the right person."
    z "And finding the right person means asking. And asking means exposing yourself."

    l "What do we do for money?"
    z "You earn it. Work. Skills. Services."
    z "Or you steal it. But theft here has consequences."
    z "Not jail. Not fines. Blood. Always blood."

    # VISUAL: Both listen. Reality settling. Harsher than expected.
    a "What about allies?"
    z "Allies require trust. Trust requires time. Time requires survival."
    z "You've been here seven hours. You almost died twice."
    z "Locals hate you. Echelon's hunting you. You have no leverage."

    a "Then how do we survive?"
    z "You don't stand out. You don't talk. You don't trust anyone."
    z "You stay hidden until I say it's safe."
    z "Which might be never. So get comfortable."

    # VISUAL: Lyra picks up clothes. Plain. Worn. Nothing like Echelon.
    l "How long have you been doing this?"
    z "Doing what?"
    l "Surviving down here. Helping people. Playing both sides."
    z "(pause) Long enough to know when someone's worth the risk."
    if get_empathy_band() == "obedience":
        z "(adds) Don’t make me regret the math."
    else:
        z "(adds, softer) Try not to waste the chance."

    # VISUAL: Zira stands. Moves to window. Looks out at city below.
    z "The Unders are 50 levels of humanity compressed and forgotten."
    z "Echelon looks down and sees waste. Criminals. Expendable."
    z "But we're the foundation. The city stands on us."
    z "And when we stop holding it up... it falls."

    a "Is that what you want? The city to fall?"
    z "(looks back at him) I want the people crushing us to fall."
    z "The city? The people? They're just trying to survive."
    z "Like you. Like me. Like everyone down here."

    # VISUAL: She moves to door. Preparing to leave again.
    z "I have contacts. People who might help. Might."
    z "But you need to understand—nobody's going to welcome you."
    z "You're Echelon. You're Glass. You killed their families."
    z "Redemption doesn't come from words. It comes from blood."

    l "What does that mean?"
    z "It means you prove yourselves. With actions. With sacrifice."
    z "You want allies? Earn them. You want safety? Fight for it."
    z "The Unders don't give anything free. Not even second chances."

    # VISUAL: Hand on door. About to leave. Stops. Looks back.
    z "There's someone I know. Rebel leader. Her cell was hit hard in the Purge."
    z "Most of her people died. Sector 10."

    # VISUAL: Aeron and Lyra both tense. Sector 10. Their Sweep.
    a "(carefully) Will she help us?"
    z "Help you? She'll probably want to kill you."
    z "But she's the only real resistance left. Everyone else scattered."
    z "If you want to fight Echelon, you need her."

    a "What's her name?"
    z "Selene. And before you ask—yes, she knows who you are."
    z "I already told her. Tested the waters."
    z "She's... considering. That's the best I can do."
    $ mark_flag("Selene", "mentioned_by_zira")
    $ canon["met_selene"] = False

    l "When do we meet her?"
    z "When I say it's safe. Which isn't now."
    z "Echelon's flooding the Lower Spans. Patrols everywhere."
    z "Marcus wants you bad. And he's willing to burn the Unders to find you."

    # VISUAL: Both process. Marcus. Father. Hunting his son.
    athought "Father's hunting me. Publicly. Aggressively."
    athought "Not quietly disappeared. Not 'training accident.'"
    athought "He wants me dead. And he wants everyone to know why."
    # Identity pain acknowledged → small empathy once
    $ adjust_empathy_once("act2_02_father_public_hunt", +1)

    a "What's he saying? Publicly?"
    z "That you're a traitor. That you conspired with terrorists."
    z "That the Purge was necessary because of intel leaks."
    z "He's blaming the 100,000 deaths on resistance activity."
    z "(bitter) And people believe him. Because they always do."

    l "He's rewriting it. Making us the villains."
    z "Of course he is. That's how Echelon works."
    z "Truth doesn't matter. Only narrative."

    # VISUAL: Zira opens door. Hallway beyond. Dark. Dangerous.
    z "Stay here. Don't leave. Don't answer the door."
    z "I'll be back tomorrow. Maybe with good news."
    z "Probably with bad news. Expect bad news."

    a "Zira. Thank you. For everything."
    z "(pauses) Don't thank me yet. You might not survive long enough to mean it."
    z "But... you're welcome. I guess."
    z "(almost leaves, stops) And Glass?"
    a "Yeah?"
    z "Stop calling yourself Glass. You're not that anymore."
    z "Figure out what you are. Before this city decides for you."

    # Identity pivot—award once (small, direction-agnostic)
    $ adjust_empathy_once("act2_02_stop_calling_glass", +1)
    $ mark_scene("act2_02_reality_check", "called_out_identity")

    # VISUAL: She leaves. Door closes. Lock engages. Alone again.
    "Gone. Again. Leaving them in the dark."
    "With supplies. With warnings. With impossible hope."

    # VISUAL: Both sit. Processing everything. Reality fully settling now.
    l "We're fucked."
    a "We established that."
    l "No, I mean really fucked. Aeron, listen to what she said."
    l "Echelon's hunting us. Locals hate us. We have no money."
    l "And the one person who might help us wants us dead."
    l "How exactly do we survive this?"

    # VISUAL: He looks at supplies. Clothes. Food. Fake IDs.
    a "One day at a time. Like Zira said."
    l "That's not a plan."
    a "It's the only plan we have."
    if get_empathy_band() == "obedience":
        "Triage first. Everything else later."
    else:
        "One day can be enough when you’re still alive at the end of it."

    # VISUAL: He picks up fake IDs. Examines them. Basic. Functional.
    # PROP: ID cards. Photos (theirs, slightly altered). Names (not theirs).

    athought "Kade Voss. That's my new name."
    athought "Lower Spans worker. Sector 6. Unremarkable. Forgettable."
    athought "Not Glass. Not Rylan. Not Echelon."
    athought "Just... nobody. Trying to survive."

    # Sync fake names with system (already seeded in player_state)
    $ player_state["fake_names"]["aeron"] = "Kade Voss"
    $ player_state["fake_names"]["lyra"]  = "Mira Chen"
    $ mark_scene("act2_02_reality_check", "fake_ids_received")

    l "(picks up her ID) Mira Chen. Sector 7."
    l "(hollow laugh) Ironic. Sector 7."
    a "What?"
    l "Nothing. Just... ghosts everywhere."

    # VISUAL: Both stare at fake identities. Their old lives gone. New ones forced.
    athought "Kade Voss. Aeron Rylan died on that rooftop."
    athought "Glass shattered in the Purge."
    athought "What's left... I don't know yet."

    # VISUAL: Lyra sets ID down. Looks at Aeron. Vulnerable. Scared.
    l "I don't know how to do this."
    a "Do what?"
    l "Be nobody. I've been Echelon my whole life."
    l "Perfect soldier. Model citizen. Proof the system works."
    l "Now I'm... Mira Chen. Worker. Nobody. Nothing."
    l "I don't know how to be nothing."

    # Aeron reaction flavors: OB = grounding via procedure; EMP = grounding via presence
    if get_empathy_band() == "obedience":
        a "Then we learn together."
        a "Neither of us knows how to do this. But we're here."
        a "And as long as we're here, we're not nothing."
    else:
        a "Then we learn together."
        a "Neither of us knows how to do this. But we're here."
        a "And as long as we're here, we're not nothing."
        "He lets the silence be shelter, not punishment."
        $ adjust_empathy_once("act2_02_ground_lyra_soft", +1)

    l "(quiet) What are we, then?"
    a "...Survivors. For now. That's enough."

    # VISUAL: She leans against him. Shoulder to shoulder. Exhaustion winning.
    "She leans. He doesn't move. Both too tired for anything else."
    "Two people in a concrete box. Hunted. Hated. Alone."
    "But not dead. Not yet."

    l "Do you think we'll make it?"
    a "I don't know."
    l "Honest answer. Thank you."
    a "We made it this far. That counts for something."
    l "Does it? Or are we just delaying the inevitable?"

    # VISUAL: Long silence. No good answer. Just survival.
    a "Get some rest. Tomorrow might be worse."
    l "Worse than today?"
    a "Always assume worse. Prepare for worse. Hope for better."
    l "(bitter laugh) You sound like a resistance fighter already."
    a "Do I?"
    l "No. You sound terrified. Like me."

    # VISUAL: Both settle in. Makeshift sleeping arrangements. Concrete floor.
    # LIGHTING: Dim bulb stays on (too dangerous to sleep in dark).
    # SOUND: City hum. Distant sirens. Their breathing. Exhaustion.

    "They sleep. Or try to. Bodies exhausted. Minds racing."
    "Tomorrow: Zira returns. Maybe with Selene. Maybe with hope."
    "Tonight: Just survival. Just breathing. Just existing."

    athought "From Aeries to Unders. From Glass to Kade."
    athought "From everything to nothing."
    athought "But Zira's right. I need to figure out what I am."
    athought "Before this city decides for me."
    athought "Before I become just another corpse in the ruins."

    # Identity introspection → once
    $ adjust_empathy_once("act2_02_identity_thesis", +1)

    # VISUAL: Hold on both sleeping. Vulnerable. Broken. Human.
    "Two people against a city. Impossible odds."
    "But they're here. And they're alive."
    "Tomorrow brings either hope or death."
    "Tonight brings only darkness. And that's enough."

    # TRANSITION: Fade to black. Time passes. Morning comes.
    # TEXT: "The Next Day"

    # canon_note: Reality check complete - they understand how fucked they are
    # canon_note: Fake IDs: Kade Voss (Aeron), Mira Chen (Lyra) - new identities
    # canon_note: Bounty: 50,000 credits each - everyone's a potential threat
    # canon_note: Aeries credits worthless - must learn Unders economy
    # canon_note: Zira mentions Selene - rebel leader, Sector 10, probably wants them dead
    # canon_note: Marcus rewriting narrative - blaming Purge on "resistance intel leaks"
    # canon_note: Echelon flooding Lower Spans - Marcus hunting aggressively
    # canon_note: "Stop calling yourself Glass" - identity crisis continues
    # canon_note: Both learning to be "nobody" - stripped of former identities
    # canon_note: Sets up Scene 3: More days passing, waiting, survival

    # --- WRAP & SUMMARY ---
    $ mark_scene("act2_02_reality_check", "completed")
    $ summary = end_operation("op202_reality_check", tag="Reality Check (Act2_02)")
    $ log_line(summary)

    return
