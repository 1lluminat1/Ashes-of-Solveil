# act2_01_descent.rpy
# =======================================================
# ACT 2 - Scene 1: Descent  (Full OB/EMP-integrated pass)
# Uses: solveil_state_system.rpy (Consolidated Architecture)
# =======================================================

label act2_descent:

    # --- OPERATION SNAPSHOT & CANON FLAGS ---
    $ start_operation("op201_descent", note="Post-Purge descent from Aeries")
    $ canon["defected"] = True
    $ canon["purge_witnessed"] = True
    $ mark_scene("act2_01_descent", "started")
    $ log_line("ACT2_01 started: Post-Purge descent")

    # VISUAL: Aeron's apartment. Hours after Purge. Dawn breaking. City burning in distance.
    # LIGHTING: Orange glow from fires mixing with cold morning light. Smoke visible.
    # SOUND: Distant sirens; fire alarms; city in chaos; his ragged breathing.

    "ACT 2: FROM ASH"

    # VISUAL: Fade in from black. Aeron and Lyra still on rooftop where Purge happened.
    # Hours have passed. Dawn approaching. Both hollow, empty, staring at burning sectors.

    "Hours pass. Or days. Time loses meaning when the world ends."
    if get_empathy_band() == "obedience":
        "He counts sectors, not faces. Catalogs flames like a report."
        $ adjust_empathy_once("act2_01_rooftop_ob_flavor", -1)
    else:
        "Every plume feels like a name he never learned, a heartbeat he didn’t save."
        $ adjust_empathy_once("act2_01_rooftop_emp_flavor", +1)

    "They stand on the rooftop. Watching Sectors 8, 9, 10 burn."
    "Smoke rises like monuments. The dead have no graves."

    # VISUAL: Aeron finally moves. Turns from the burning city.
    athought "We can't stay here."

    # OB/EMP Lyra read
    if get_empathy_band() == "obedience":
        l "(hollow) Where would we go?"
        a "Anywhere with cover and exits."
    else:
        l "(hollow) Where would we go?"
        a "Anywhere but here."

    # VISUAL: Lyra looks at him. Both exhausted, broken, barely functioning.
    l "Echelon will be looking for us."
    a "I know."
    l "They'll want to know why you weren't on the command deck."
    a "I know."
    l "Marcus will realize—"
    if get_empathy_band() == "obedience":
        a "(sharp) I know."
        "The word lands like a blade. Control over comfort."
        $ adjust_empathy_once("act2_01_ob_sharp_cut", -1)
    else:
        a "(soft, pained) I know."
        "He hates how true it is. How much of him Marcus still owns."
        $ adjust_empathy_once("act2_01_emp_soft_ack", +1)

    # VISUAL: Silence. Both processing. Dawn light growing.
    "Silence. The city wakes. Oblivious or pretending."
    "Above the Purge zones, life continues. Because it always does."

    l "How long do we have?"
    if get_empathy_band() == "obedience":
        a "Hours. Maybe less. They'll check my apartment first."
        "He’s scheduling their deaths in his head and refusing the numbers."
    else:
        a "Hours. Maybe less. They'll check my apartment first."
        "He feels the clock in his ribs. Every breath a second lost."

    l "Then we need to move."
    a "(looks at her) You don't have to come. This is my—"
    l "(cuts him off) Don't. We burn together. Remember?"

    # VISUAL: He nods. Small. Grateful. Terrified.
    if get_empathy_band() == "obedience":
        athought "We burn together. Glass and glass."
        athought "Keep formation. Don’t break."
    else:
        athought "We burn together. Glass and glass."
        athought "Both shattered. Both falling."

    # TRANSITION: Return to apartment. Moving fast. Urgency building.
    # VISUAL: Apartment door opens. Everything the same but different.
    # LIGHTING: Orange glow through windows. Smoke visible. Chaos distant.

    scene bg_aeron_apartment with fade

    "The apartment. Unchanged. But everything's different now."
    "This was home. Now it's a crime scene waiting to happen."

    # VISUAL: Aeron moves to closet. Grabs tactical gear, not uniform.
    # SOUND: Rustling fabric; zippers; equipment being packed quickly.

    athought "What do we take? What matters?"
    if get_empathy_band() == "obedience":
        athought "Weapons. Credits. Clothes. Everything else is weight."
    else:
        athought "Weapons. Credits. Clothes. The rest is ghosts pretending to be objects."

    # VISUAL: He pauses at Kael's photo. Hand hovers. Decides.
    "Kael's photo. On the desk. Smiling."
    if pass_emp_gate():
        athought "I can't leave you behind. Not again."
        "He takes it. Slips it inside his jacket. Against his chest."
        $ mark_scene("act2_01_descent", "took_kael_photo")
        $ adjust_empathy_once("act2_01_kael_photo", +1)
        $ char_note("Lyra", "Saw Aeron keep Kael’s photo; read it as human, not tactical.")
    else:
        athought "I can't leave you behind. Not again."
        "He takes it. Not for comfort— for cover, for story, for control."
        $ mark_scene("act2_01_descent", "took_kael_photo")
        $ adjust_empathy_once("act2_01_kael_photo_ob", -1)

    # VISUAL: Lyra gathering her things from bathroom, bedroom. Efficient. Military.
    l "How much can we carry?"
    a "Not much. We'll be moving fast."
    l "Where?"
    a "Down. The Lower Spans. Unders if we have to."
    l "(stops) The Unders? Aeron, they'll kill us there."
    a "Echelon will kill us here. At least down there we have a chance."

    # VISUAL: She processes. Nods. Grim acceptance.
    l "The people you saved. In the Sweep. Some are still there."
    a "Maybe. If they survived the Purge."
    l "They might help us."
    if pass_emp_gate():
        a "(bitter laugh) Help Glass? The man who killed 600 of them?"
        l "The man who saved 200."
        a "That's not how they'll remember it."
        "He lets the blame sit where it belongs—on him."
        $ adjust_empathy_once("act2_01_accept_blamed_weight", +1)
    else:
        a "(flat) Help Glass? Unlikely."
        l "The man who saved 200."
        a "Narratives don’t change because we want them to."
        "He files it under risk categories and moves on."
        $ adjust_empathy_once("act2_01_distance_from_guilt", -1)

    # VISUAL: Packing continues. Clock ticking. Sunrise approaching.
    # SOUND: Distant comms chatter (Echelon channels). Patrol movements increasing.

    "The city wakes. Patrols mobilize. The hunt hasn't started."
    "But it will. Soon."

    # VISUAL: Aeron at terminal. Deletes files. Wipes data. Covering tracks.
    athought "Everything. Gone. No trail. No evidence."
    athought "They'll find the apartment empty. But they'll know I left."
    athought "Marcus will know. He always knows."
    if get_empathy_band() == "obedience":
        "He scrubs the last logs with ritual perfection. Control is oxygen."
    else:
        "His fingers shake. He keeps going. Guilt is a solvent; it erases and reveals."

    # VISUAL: Zira's encrypted device on desk. Blinking softly.
    "The device. Zira's gift. Still here. Still working."
    athought "She said use it when I was ready. When I needed her."
    athought "I need her. But can I risk it?"

    # ACTION: Player choice—activate device or leave it.
    menu:
        "The device blinks. A lifeline. Or a trap."
        "Activate the device—contact Zira.":
            $ char_flag_on("Zira", "contacted_in_scene1")
            $ adjust_empathy_once("act2_01_contact_choice", +2)
            $ log_line("Aeron activated Zira’s device (Act2_01)")
            "He picks it up. Activates. Sends simple message."
            "He types one word: 'Help.'"
            "Sends. No response. Did she receive it?"
            athought "If she got it, she'll know. If not... we're alone."
            # Slight trust seed toward Zira for reaching out
            $ rel("Zira", trust=1)
        "Leave it—don't risk the signal.":
            $ adjust_empathy_once("act2_01_contact_choice", -2)
            $ log_line("Aeron ignored Zira’s device (Act2_01)")
            "Too risky. Signal could be tracked. Echelon could intercept."
            athought "We're on our own. Better that way."
            "He pockets the device anyway. Just in case."

    # VISUAL: Lyra returns. Small pack. Essentials only. Ready.
    l "I'm ready. You?"
    a "(looks around apartment one last time) Yeah. I'm ready."

    # VISUAL: Apartment. Empty. Hollow. Abandoned.
    athought "Seven years here. 390 operations launched from this room."
    if get_empathy_band() == "obedience":
        athought "Glass lived here. Glass is a containment method."
    else:
        athought "Glass lived here. Glass died on that rooftop."
        athought "What walks out this door... I don't know what that is."

    l "(hand on his shoulder) Aeron. We need to go."
    a "(nods) Right. Let's move."

    # VISUAL: Door opens. Hallway beyond. Empty. Dawn light filtering through windows.
    # SOUND: Distant elevator chime. Footsteps. Patrol approaching.

    "Footsteps. Close. Patrol coming this way."

    l "(whisper) They're early."
    a "Elevator or stairs?"
    l "Stairs. Quieter."
    a "Back exit. Through maintenance level."
    l "Lead the way."

    # VISUAL: Moving quickly but quietly through Aeries corridors.
    # LIGHTING: Morning light through tall windows. Marble gleaming. Perfect order.
    # SOUND: Their footsteps muted; distant patrols; comms chatter growing.

    "Aeries. Perfect. Sterile. Cold."
    "Marble halls stretching endlessly. Everything clean. Everything controlled."
    "They don't belong here anymore."
    if pass_tier("OB2","OB3"):
        "He still walks like he owns the floor. The floor remembers."
        $ adjust_empathy_once("act2_01_aeries_walk_ob", -1)
    elif pass_tier("EMP2","EMP3"):
        "He walks like a man returning a stolen uniform."
        $ adjust_empathy_once("act2_01_aeries_walk_emp", +1)

    # VISUAL: Past propaganda screens. Messages updating.
    # TEXT ON SCREENS: "RECENT TERRORIST ATTACK CONTAINED"
    # TEXT: "SECTORS 8-10 UNDER EMERGENCY PROTOCOLS"
    # TEXT: "ECHELON PROTECTS. ECHELON PROVIDES."

    athought "Terrorist attack. That's what they're calling it."
    athought "Not genocide. Not Purge. Just... contained threat."
    athought "100,000 dead. And they call it protection."
    if pass_emp_gate():
        "He refuses the euphemism. Words are weapons too."
    else:
        "He files the lie. Predicts the next broadcast. Moves on."

    # VISUAL: They reach maintenance stairs. Heavy door. Rarely used.
    # SOUND: Door opens with metallic groan. Stairs descending into darkness.

    "Maintenance stairs. Down. Always down."
    "Away from light. Away from order. Away from everything."

    l "How far down?"
    a "As far as we can go."
    l "The Unders are fifty levels from here."
    a "Then we go fifty levels."

    # VISUAL: They descend. Step by step. Lighting getting dimmer.
    # SOUND: Their breathing; footsteps echoing; city hum growing louder below.

    "Down. Level by level. The city changes."
    "Clean to grimy. Bright to dim. Order to chaos."
    "And they descend into it."
    if get_empathy_band() == "obedience":
        "He counts landings. Checks corners. Breath on metronome."
    else:
        "He hears a child laugh three floors below. Or a memory pretending to live here."

    # VISUAL: Passing through Mid Levels. Industrial. Functional. Working class.
    # People starting their day. Factories humming. Life continuing.

    athought "Mid Levels. Workers. Families. Normal people."
    athought "They don't know. Sectors 8-10 burned. And they don't know."
    athought "Or they know and they're pretending. Because what else can they do?"

    # VISUAL: Someone glances at them. Aeron in tactical gear. Lyra same.
    # Worker looks away quickly. Doesn't want trouble.

    l "We stand out."
    a "I know. Keep moving."
    l "We need different clothes. These scream Echelon."
    a "We'll find something in the Lower Spans. Black market."
    l "With what money?"
    a "(shows credit chip) Aeries credits. Should buy us time."
    l "If they take them. If they don't recognize us first."
    # Inventory + small risk notes
    $ add_item_counter("food", 0)  # no change, placeholder for consistency
    $ grant_disguise("mid")        # seed: will matter soon
    $ log_line("Prepared mid-tier disguise flag for later swap (Act2_01)")

    # VISUAL: Continuing descent. Levels blurring together. Getting darker, dirtier.
    # SOUND: Music from below; voices; machinery; city living.

    "Lower Spans. The city's underbelly. Where Aeries refuse looks."
    "Neon. Rust. Steam. Humanity compressed and forgotten."
    "This is where they swept. Where 800 died. Where 200 lived."

    # VISUAL: They emerge into Lower Spans proper. Market district. Pre-dawn crowd.
    # LIGHTING: Neon signs. Flickering. Harsh shadows. Industrial glow.
    # SOUND: Vendors calling. Deals being made. Life surviving.

    athought "Sector 6. Near where we swept. Near where they died."
    athought "The vendor. The child. The families. All gone now."
    athought "And we're here. Walking among the survivors."
    if pass_emp_gate():
        "He keeps his hands open. No weapon. He wants them to see that."
    else:
        "Hands low, centerline open. Weapon within reach. He wants to live."

    l "(quiet) Do you recognize it?"
    a "Every corner. Every street. Every face I didn't save."

    # VISUAL: People notice them. Conversations stop. Eyes follow.
    # Whispers spread. "Echelon." "Soldiers." "What are they doing here?"

    "Eyes. Everywhere. Watching. Judging."
    "We're not hidden. We're targets."

    # VISUAL: Vendor approaches. Old woman. Weathered. Angry.
    vendor "You're Echelon."
    a "...Yes."
    vendor "You swept Sector 10. Three days ago."
    a "(carefully) I did."
    vendor "My nephew was there. He's dead now."
    vendor "You kill him?"
    if pass_emp_gate():
        a "...I don't know. Maybe."
        "He holds her eyes and doesn’t look away."
        $ adjust_empathy_once("act2_01_vendor_honesty", +1)
        $ add_evidence_of_mercy(1)
    else:
        a "...Possibly. I followed orders."
        "He refuses the ritual of absolution. It would be a lie."
        $ adjust_empathy_once("act2_01_vendor_rigor", -1)
        $ add_team_suspicion(1)

    # VISUAL: She stares. Long. Hard. Then spits at his feet.
    vendor "Get out of my sector. Before someone less kind finds you."
    "She walks away. Others watching. Tension rising."

    l "(whisper) We need to move. Now."
    a "Where? We're exposed everywhere."
    l "Find shelter. Hide. Figure it out from there."
    a "With everyone watching? We won't make it an hour."

    # VISUAL: More people noticing. Hostility growing. Crowd forming.
    # SOUND: Murmurs. "Echelon." "Glass." "Murderers." Anger building.

    "The crowd grows. Whispers harden. Space shrinks."
    athought "They know me. They remember."
    athought "Glass killed their families. And Glass is here."

    # VISUAL: Man steps forward. Young. Angry. Holding makeshift weapon.
    man "You're Glass. I know your face."
    a "..."
    man "Sector 10. You killed my sister."
    if pass_emp_gate():
        a "I'm sorry."
    else:
        a "(low) I know."

    man "Sorry? SORRY? She was nine years old!"
    man "And you're SORRY?"

    # VISUAL: Crowd closing in. Multiple weapons visible. Nowhere to run.
    l "(hand on weapon) Aeron, we need to—"
    a "(stops her) Don't. We're outnumbered."
    l "Then what?"
    a "...We run. Or we die. Pick one."

    # VISUAL: Man raises weapon. Others follow. About to attack.
    # SOUND: Sudden CRACK. Gunshot. Not at them. Warning shot.

    "CRACK. Gunshot. Echo. Crowd freezes."

    # VISUAL: Figure appears from alley. Hood up. Female. Armed.
    # Voice familiar. Confident. Amused.

    z "That's enough."

    # VISUAL: Crowd parts. Confused. Wary. The figure approaches.
    # SOUND: Footsteps. Deliberate. Unhurried. Commanding.

    z "These two are with me. Touch them, you answer to me."
    man "Who the hell are you?"
    z "Someone you don't want to fuck with. Now back off."

    # VISUAL: Zira lowers hood. Face revealed. Eyes sharp. Grin dangerous.
    z "Unless you want to find out what happens when you ignore me."

    # VISUAL: Man hesitates. Others uncertain. Zira's reputation precedes her.
    man "(to Aeron) This isn't over."
    "Crowd disperses. Slowly. Reluctantly. But disperses."

    # VISUAL: Zira walks to them. Looks them over. Shakes head.
    z "You two are terrible at hiding."
    a "Zira—"
    if char_flag_has("Zira", "contacted_in_scene1"):
        z "Save it. You pinged me. Good instinct. Bad execution. Follow me."
        $ rel("Zira", trust=1)  # tiny bonus for having reached out
    else:
        z "Save it. Follow me. Before they change their minds."

    l "How did you know we'd be here?"
    if char_flag_has("Zira", "contacted_in_scene1"):
        z "(grins) You pressed send. I pressed go."
    else:
        z "(grins) I've been tracking you since you left Aeries."

    z "Did you really think you could disappear? In those clothes?"
    a "You got my message?"
    if char_flag_has("Zira", "contacted_in_scene1"):
        z "I got it. And I came. Because apparently you're idiots."
    else:
        z "You didn’t send one. Lucky for you, I’m generous with strays."

    z "Now move. We don't have time for gratitude."

    # VISUAL: She leads them into alley. Narrow. Dark. Hidden from main street.
    # SOUND: Their footsteps; distant crowd; her confident stride.

    "She moves like she owns the place. Maybe she does."
    "We follow. Because we have no choice. Because she's right."
    "We're idiots. And we need her."

    # VISUAL: Deep in alley network. Twisting paths. Zira knows every turn.
    z "Echelon's hunting you. Whole city knows by now."
    a "Already?"
    z "Marcus put out the word. Traitors. Kill on sight. Big reward."
    z "You're famous. Congratulations."
    l "How much time do we have?"
    z "Before Echelon floods the Lower Spans? Hours. Maybe less."
    z "Before locals kill you for revenge? Minutes. Maybe less."
    z "You picked the worst possible place to hide."

    a "Where else could we go?"
    z "Anywhere but here. But too late now. You're here."
    z "So we adapt. Like always."

    # VISUAL: She stops at hidden door. Unmarked. Nondescript.
    # SOUND: Electronic lock. Beeps. Door slides open. Darkness beyond.

    z "Welcome to my safe house. It's not much. But it's yours."
    z "For now. Until we figure out what the hell you two are doing."

    # VISUAL: They enter. Door seals behind them. Darkness. Then lights flicker on.
    # LIGHTING: Dim. Industrial. Functional. Small space. Secure.

    "Small. Cold. Secure. Hidden."
    "Not home. But shelter."
    "And right now, that's everything."

    # VISUAL: Zira tosses them water. Food packets. Basic supplies.
    z "Eat. Rest. Don't leave. I'll be back tonight."
    l "Where are you going?"
    z "To make sure you idiots stay alive."
    z "Echelon's mobilizing. Locals want blood. You're trapped."
    z "So I'm fixing it. Like I fix everything."

    a "Why are you helping us?"
    z "(pauses at door) Because I told you I would."
    z "And because 200 people are alive because Glass cracked."
    z "I want to see what happens when Glass breaks completely."
    if pass_emp_gate():
        z "(grins softer) Should be interesting."
    else:
        z "(grins) Should be interesting."

    # VISUAL: She leaves. Door seals. They're alone.
    # SOUND: Silence. Just breathing. Exhaustion. Shock.

    "Alone. Safe. For now."
    "The city hunts us. Both sides want us dead."
    "And we're here. In the dark. Waiting."

    l "(collapses against wall) We're fucked."
    a "(sits beside her) Completely."
    l "Echelon wants us dead. Locals want us dead."
    l "We have nothing. No allies. No plan. No future."
    a "We have Zira."
    l "One person. Against a city."
    a "One person who just saved our lives."

    # VISUAL: Long silence. Both processing. Reality settling.
    "Silence. Heavy. Crushing."
    "Hours ago, they witnessed 100,000 deaths."
    "Now they're fugitives. Hunted. Hated. Alone."

    athought "From Glass to Ash."
    athought "Burned down. Nothing left. Just fuel for fire."
    athought "But fire needs more than fuel. It needs air. It needs spark."
    if pass_emp_gate():
        athought "Maybe Zira's right. Maybe this is where we find it."
        $ adjust_empathy_once("act2_01_end_reflection_emp", +1)
    else:
        athought "Spark is secondary. Survive the hour. Survive the next."
        $ adjust_empathy_once("act2_01_end_reflection_ob", -1)

    l "What do we do now?"
    a "We survive. One hour at a time."
    l "And after that?"
    if pass_emp_gate():
        a "...We burn them. Like we said."
        l "How? We're two people against an empire."
        a "Two people who know that empire. Who were that empire."
        a "If anyone can burn it... it's us."
    else:
        a "...We burn them. After we build the fire."
        l "How? We're two people against an empire."
        a "Two who know their corridors and codes. We start there."

    # VISUAL: They sit. Backs against wall. Exhausted. Terrified. Committed.
    "Two people. One city. Impossible odds."
    "But they're here. And they're alive."
    "That's something. That has to be something."

    # TRANSITION: Fade to black. Time passes. Night falls. Zira returns.
    # TEXT: "That Evening"

    # canon_note: Aeron & Lyra officially fugitives - hunted by both sides
    # canon_note: Zira becomes crucial lifeline - saves them immediately
    # canon_note: Lower Spans hostile - locals remember Glass, want revenge
    # canon_note: Aeron faces consequences - nephew dead, sister dead, they remember
    # canon_note: Sets up Act 2 theme: earning trust from those they harmed
    # canon_note: Aeries credits may not work in Unders - economy difference
    # canon_note: "Two people against empire" - David vs Goliath setup
    # canon_note: Zira tracking them since they left - she's been watching/helping

    # --- SAFEHOUSE/INVENTORY/RELATIONSHIP TOUCHES ---
    $ mark_flag("Zira", "met")
    $ rel("Zira", loyalty=1)
    $ add_item("supplies", "water", 1)
    $ add_item("supplies", "food", 1)

    # --- WRAP OPERATION & LOG ---
    $ mark_scene("act2_01_descent", "completed")
    $ summary = end_operation("op201_descent", tag="Descent (Act2_01)")
    $ log_line(summary)

    return
