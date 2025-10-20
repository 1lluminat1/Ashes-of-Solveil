# act2_01_descent.rpy


# =======================================================
# ACT 2 - Scene 1: Descent
# =======================================================


label act2_descent:

    # VISUAL: Aeron's apartment. Hours after Purge. Dawn breaking. City burning in distance.
    # LIGHTING: Orange glow from fires mixing with cold morning light. Smoke visible.
    # SOUND: Distant sirens; fire alarms; city in chaos; his ragged breathing.

    "{i}ACT 2: FROM ASH{/i}"
    
    # VISUAL: Fade in from black. Aeron and Lyra still on rooftop where Purge happened.
    # Hours have passed. Dawn approaching. Both hollow, empty, staring at burning sectors.
    
    "{i}Hours pass. Or days. Time loses meaning when the world ends.{/i}"
    "{i}They stand on the rooftop. Watching Sectors 8, 9, 10 burn.{/i}"
    "{i}Smoke rises like monuments. The dead have no graves.{/i}"

    # VISUAL: Aeron finally moves. Turns from the burning city.
    a "{i}We can't stay here.{/i}"
    
    l "(hollow) Where would we go?"
    a "Anywhere but here."
    
    # VISUAL: Lyra looks at him. Both exhausted, broken, barely functioning.
    l "Echelon will be looking for us."
    a "I know."
    l "They'll want to know why you weren't on the command deck."
    a "I know."
    l "Marcus will realize—"
    a "(sharp) I know."

    # VISUAL: Silence. Both processing. Dawn light growing.
    "{i}Silence. The city wakes. Oblivious or pretending.{/i}"
    "{i}Above the Purge zones, life continues. Because it always does.{/i}"

    l "How long do we have?"
    a "Hours. Maybe less. They'll check my apartment first."
    l "Then we need to move."
    a "(looks at her) You don't have to come. This is my—"
    l "(cuts him off) Don't. We burn together. Remember?"

    # VISUAL: He nods. Small. Grateful. Terrified.
    a "{i}We burn together. Glass and glass.{/i}"
    a "{i}Both shattered. Both falling.{/i}"

    # TRANSITION: Return to apartment. Moving fast. Urgency building.
    # VISUAL: Apartment door opens. Everything the same but different.
    # LIGHTING: Orange glow through windows. Smoke visible. Chaos distant.

    scene bg_aeron_apartment with fade
    
    "{i}The apartment. Unchanged. But everything's different now.{/i}"
    "{i}This was home. Now it's a crime scene waiting to happen.{/i}"

    # VISUAL: Aeron moves to closet. Grabs tactical gear, not uniform.
    # SOUND: Rustling fabric; zippers; equipment being packed quickly.

    a "{i}What do we take? What matters?{/i}"
    a "{i}Weapons. Credits. Clothes. Everything else is weight.{/i}"

    # VISUAL: He pauses at Kael's photo. Hand hovers. Decides.
    "{i}Kael's photo. On the desk. Smiling.{/i}"
    a "{i}I can't leave you behind. Not again.{/i}"
    "{i}He takes it. Slips it inside his jacket. Against his chest.{/i}"

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
    a "(bitter laugh) Help Glass? The man who killed 600 of them?"
    l "The man who saved 200."
    a "That's not how they'll remember it."

    # VISUAL: Packing continues. Clock ticking. Sunrise approaching.
    # SOUND: Distant comms chatter (Echelon channels). Patrol movements increasing.

    "{i}The city wakes. Patrols mobilize. The hunt hasn't started.{/i}"
    "{i}But it will. Soon.{/i}"

    # VISUAL: Aeron at terminal. Deletes files. Wipes data. Covering tracks.
    a "{i}Everything. Gone. No trail. No evidence.{/i}"
    a "{i}They'll find the apartment empty. But they'll know I left.{/i}"
    a "{i}Marcus will know. He always knows.{/i}"

    # VISUAL: Zira's encrypted device on desk. Blinking softly.
    "{i}The device. Zira's gift. Still here. Still working.{/i}"
    a "{i}She said use it when I was ready. When I needed her.{/i}"
    a "{i}I need her. But can I risk it?{/i}"

    # ACTION: Player choice—activate device or leave it.
    menu:
        "The device blinks. A lifeline. Or a trap."
        "Activate the device—contact Zira.":
            $ aeron_contacted_zira = True
            
            # VISUAL: He picks it up. Activates. Sends simple message.
            "{i}He types one word: 'Help.'{/i}"
            "{i}Sends. No response. Did she receive it?{/i}"
            a "{i}If she got it, she'll know. If not... we're alone.{/i}"
            
        "Leave it—don't risk the signal.":
            $ aeron_contacted_zira = False
            
            "{i}Too risky. Signal could be tracked. Echelon could intercept.{/i}"
            a "{i}We're on our own. Better that way.{/i}"
            "{i}He pockets the device anyway. Just in case.{/i}"

    # VISUAL: Lyra returns. Small pack. Essentials only. Ready.
    l "I'm ready. You?"
    a "(looks around apartment one last time) Yeah. I'm ready."

    # VISUAL: Apartment. Empty. Hollow. Abandoned.
    a "{i}Seven years here. 390 operations launched from this room.{/i}"
    a "{i}Glass lived here. Glass died on that rooftop.{/i}"
    a "{i}What walks out this door... I don't know what that is.{/i}"

    l "(hand on his shoulder) Aeron. We need to go."
    a "(nods) Right. Let's move."

    # VISUAL: Door opens. Hallway beyond. Empty. Dawn light filtering through windows.
    # SOUND: Distant elevator chime. Footsteps. Patrol approaching.

    "{i}Footsteps. Close. Patrol coming this way.{/i}"
    
    l "(whisper) They're early."
    a "Elevator or stairs?"
    l "Stairs. Quieter."
    a "Back exit. Through maintenance level."
    l "Lead the way."

    # VISUAL: Moving quickly but quietly through Aeries corridors.
    # LIGHTING: Morning light through tall windows. Marble gleaming. Perfect order.
    # SOUND: Their footsteps muted; distant patrols; comms chatter growing.

    "{i}Aeries. Perfect. Sterile. Cold.{/i}"
    "{i}Marble halls stretching endlessly. Everything clean. Everything controlled.{/i}"
    "{i}They don't belong here anymore.{/i}"

    # VISUAL: Past propaganda screens. Messages updating.
    # TEXT ON SCREENS: "RECENT TERRORIST ATTACK CONTAINED"
    # TEXT: "SECTORS 8-10 UNDER EMERGENCY PROTOCOLS"
    # TEXT: "ECHELON PROTECTS. ECHELON PROVIDES."

    a "{i}Terrorist attack. That's what they're calling it.{/i}"
    a "{i}Not genocide. Not Purge. Just... contained threat.{/i}"
    a "{i}100,000 dead. And they call it protection.{/i}"

    # VISUAL: They reach maintenance stairs. Heavy door. Rarely used.
    # SOUND: Door opens with metallic groan. Stairs descending into darkness.

    "{i}Maintenance stairs. Down. Always down.{/i}"
    "{i}Away from light. Away from order. Away from everything.{/i}"

    l "How far down?"
    a "As far as we can go."
    l "The Unders are fifty levels from here."
    a "Then we go fifty levels."

    # VISUAL: They descend. Step by step. Lighting getting dimmer.
    # SOUND: Their breathing; footsteps echoing; city hum growing louder below.

    "{i}Down. Level by level. The city changes.{/i}"
    "{i}Clean to grimy. Bright to dim. Order to chaos.{/i}"
    "{i}And they descend into it.{/i}"

    # VISUAL: Passing through Mid Levels. Industrial. Functional. Working class.
    # People starting their day. Factories humming. Life continuing.

    a "{i}Mid Levels. Workers. Families. Normal people.{/i}"
    a "{i}They don't know. Sectors 8-10 burned. And they don't know.{/i}"
    a "{i}Or they know and they're pretending. Because what else can they do?{/i}"

    # VISUAL: Someone glances at them. Aeron in tactical gear. Lyra same.
    # Worker looks away quickly. Doesn't want trouble.

    l "We stand out."
    a "I know. Keep moving."
    l "We need different clothes. These scream Echelon."
    a "We'll find something in the Lower Spans. Black market."
    l "With what money?"
    a "(shows credit chip) Aeries credits. Should buy us time."
    l "If they take them. If they don't recognize us first."

    # VISUAL: Continuing descent. Levels blurring together. Getting darker, dirtier.
    # SOUND: Music from below; voices; machinery; city living.

    "{i}Lower Spans. The city's underbelly. Where Aeries refuse looks.{/i}"
    "{i}Neon. Rust. Steam. Humanity compressed and forgotten.{/i}"
    "{i}This is where they swept. Where 800 died. Where 200 lived.{/i}"

    # VISUAL: They emerge into Lower Spans proper. Market district. Pre-dawn crowd.
    # LIGHTING: Neon signs. Flickering. Harsh shadows. Industrial glow.
    # SOUND: Vendors calling. Deals being made. Life surviving.

    a "{i}Sector 6. Near where we swept. Near where they died.{/i}"
    a "{i}The vendor. The child. The families. All gone now.{/i}"
    a "{i}And we're here. Walking among the survivors.{/i}"

    l "(quiet) Do you recognize it?"
    a "Every corner. Every street. Every face I didn't save."

    # VISUAL: People notice them. Conversations stop. Eyes follow.
    # Whispers spread. "Echelon." "Soldiers." "What are they doing here?"

    "{i}Eyes. Everywhere. Watching. Judging.{/i}"
    "{i}We're not hidden. We're targets.{/i}"

    # VISUAL: Vendor approaches. Old woman. Weathered. Angry.
    vendor "You're Echelon."
    a "...Yes."
    vendor "You swept Sector 10. Three days ago."
    a "(carefully) I did."
    vendor "My nephew was there. He's dead now."
    vendor "You kill him?"
    a "...I don't know. Maybe."

    # VISUAL: She stares. Long. Hard. Then spits at his feet.
    vendor "Get out of my sector. Before someone less kind finds you."
    "{i}She walks away. Others watching. Tension rising.{/i}"

    l "(whisper) We need to move. Now."
    a "Where? We're exposed everywhere."
    l "Find shelter. Hide. Figure it out from there."
    a "With everyone watching? We won't make it an hour."

    # VISUAL: More people noticing. Hostility growing. Crowd forming.
    # SOUND: Murmurs. "Echelon." "Glass." "Murderers." Anger building.

    "{i}The crowd grows. Whispers harden. Space shrinks.{/i}"
    a "{i}They know me. They remember.{/i}"
    a "{i}Glass killed their families. And Glass is here.{/i}"

    # VISUAL: Man steps forward. Young. Angry. Holding makeshift weapon.
    man "You're Glass. I know your face."
    a "..."
    man "Sector 10. You killed my sister."
    a "I'm sorry."
    man "Sorry? SORRY? She was nine years old!"
    man "And you're SORRY?"

    # VISUAL: Crowd closing in. Multiple weapons visible. Nowhere to run.
    l "(hand on weapon) Aeron, we need to—"
    a "(stops her) Don't. We're outnumbered."
    l "Then what?"
    a "...We run. Or we die. Pick one."

    # VISUAL: Man raises weapon. Others follow. About to attack.
    # SOUND: Sudden CRACK. Gunshot. Not at them. Warning shot.

    "{i}CRACK. Gunshot. Echo. Crowd freezes.{/i}"

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
    "{i}Crowd disperses. Slowly. Reluctantly. But disperses.{/i}"

    # VISUAL: Zira walks to them. Looks them over. Shakes head.
    z "You two are terrible at hiding."
    a "Zira—"
    z "Save it. Follow me. Before they change their minds."
    l "How did you know we'd be here?"
    z "(grins) I've been tracking you since you left Aeries."
    z "Did you really think you could disappear? In those clothes?"
    a "You got my message?"
    z "I got it. And I came. Because apparently you're idiots."
    z "Now move. We don't have time for gratitude."

    # VISUAL: She leads them into alley. Narrow. Dark. Hidden from main street.
    # SOUND: Their footsteps; distant crowd; her confident stride.

    "{i}She moves like she owns the place. Maybe she does.{/i}"
    "{i}We follow. Because we have no choice. Because she's right.{/i}"
    "{i}We're idiots. And we need her.{/i}"

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

    "{i}Small. Cold. Secure. Hidden.{/i}"
    "{i}Not home. But shelter.{/i}"
    "{i}And right now, that's everything.{/i}"

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
    z "(grins) Should be interesting."

    # VISUAL: She leaves. Door seals. They're alone.
    # SOUND: Silence. Just breathing. Exhaustion. Shock.

    "{i}Alone. Safe. For now.{/i}"
    "{i}The city hunts us. Both sides want us dead.{/i}"
    "{i}And we're here. In the dark. Waiting.{/i}"

    l "(collapses against wall) We're fucked."
    a "(sits beside her) Completely."
    l "Echelon wants us dead. Locals want us dead."
    l "We have nothing. No allies. No plan. No future."
    a "We have Zira."
    l "One person. Against a city."
    a "One person who just saved our lives."

    # VISUAL: Long silence. Both processing. Reality settling.
    "{i}Silence. Heavy. Crushing.{/i}"
    "{i}Hours ago, they witnessed 100,000 deaths.{/i}"
    "{i}Now they're fugitives. Hunted. Hated. Alone.{/i}"

    a "{i}From Glass to Ash.{/i}"
    a "{i}Burned down. Nothing left. Just fuel for fire.{/i}"
    a "{i}But fire needs more than fuel. It needs air. It needs spark.{/i}"
    a "{i}Maybe Zira's right. Maybe this is where we find it.{/i}"

    l "What do we do now?"
    a "We survive. One hour at a time."
    l "And after that?"
    a "...We burn them. Like we said."
    l "How? We're two people against an empire."
    a "Two people who know that empire. Who were that empire."
    a "If anyone can burn it... it's us."

    # VISUAL: They sit. Backs against wall. Exhausted. Terrified. Committed.
    "{i}Two people. One city. Impossible odds.{/i}"
    "{i}But they're here. And they're alive.{/i}"
    "{i}That's something. That has to be something.{/i}"

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

    return