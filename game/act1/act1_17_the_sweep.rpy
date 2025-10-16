# act1_17_the_sweep.rpy


# =======================================================
# ACT 1 - Scene 17: The Sweep - Sector 10
# =======================================================


define unit2 = Character("[Unit-2]", color="#4A90E2")
define unit3 = Character("[Unit-3]", color="#4A90E2")
define unit4 = Character("[Unit-4]", color="#4A90E2")

# Tracking variables for consequences
default civilians_saved = 0
default civilians_killed = 0
default evidence_of_mercy = 0
default team_suspicion = 0

label act1_sweep:

    # VISUAL: Pre-dawn. Sector 10 approach. Industrial decay. Steam vents. Neon dying.
    # LIGHTING: Cold blue pre-dawn; harsh tactical lights from dropship.
    # SOUND: Rotor wash; boot steps on metal; radio chatter; breathing through comms.

    "{i}Dawn breaks over Sector 10 like a blade.{/i}"
    "{i}The dropship descends. Tactical lights cut through steam. The sector wakes to its last morning.{/i}"

    # VISUAL: Tactical team assembled—four units plus Aeron. Weapons ready. Faces hidden.
    # SOUND: Equipment rattling; safeties clicking off; orders through comms.

    # COMMS: Marcus (filtered, distant authority)
    m "Glass. Confirm deployment."
    a "Confirmed. Sector 10. Grid Six-Two."
    m "Rules of engagement?"
    a "Zero tolerance. Lethal force authorized."
    m "Acceptable collateral?"
    a "(pause) ...Within mission parameters."
    m "Good. Execute with precision. Prove your worth."
    
    # VISUAL: Comms cut. Static. Silence.
    a "{i}Prove your worth. Always the same words.{/i}"
    a "{i}390 operations proving my worth. This is 391.{/i}"

    # VISUAL: Team fanned out. Aeron at point. Sector 10 ahead—quiet, unaware.
    unit2 "Sector's quiet. No alerts."
    unit3 "Thermal shows 800+ signatures. Clustered in sublevels."
    unit4 "Orders, Glass?"
    
    a "{i}800 people. The vendor. The child. The families.{/i}"
    a "{i}All waiting below. All trusting the dawn will come like it always does.{/i}"
    a "{i}Glass executes orders. But humans find cracks.{/i}"
    a "{i}Let's see if I can be both.{/i}"

    a "Standard sweep pattern. Alpha through Delta grids. Report all contacts."
    unit2 "Confirmed."

    # VISUAL: Team moves forward. Aeron's POV—rifle sight framing doorways.
    # SOUND: Boots on concrete; distant voices waking; morning routines beginning.

    "{i}They move through the morning quiet. A sector waking. Last normal moments.{/i}"

    # ==========================================
    # CHOICE 1: THE WARNING
    # ==========================================

    # VISUAL: Intersection ahead. Left: direct route to sublevel clusters. Right: detour through market district.
    # SOUND: Market sounds distant—vendors setting up, children laughing.

    unit3 "Direct route is left. Fastest approach to target concentration."
    unit2 "Market district right. Slower but fewer civilians."
    unit4 "Orders?"

    a "{i}Left is efficient. Glass would go left.{/i}"
    a "{i}Right gives them time. Time to hear. Time to run.{/i}"

    menu:
        "The team waits. Dawn light catches his visor."
        "Take the direct route—efficient, by-the-book.":
            $ aeron_warned_civilians = False
            $ team_suspicion += 0
            a "Left. Direct approach. Standard protocol."
            unit2 "Confirmed. Moving."
            "{i}Glass chooses efficiency. No mercy. Just execution.{/i}"
            a "{i}I'm sorry. I tried to prepare. But I can't save you all.{/i}"
            
        "Detour through market—slower, gives them time to hear the approach.":
            $ aeron_warned_civilians = True
            $ civilians_saved += 50
            $ evidence_of_mercy += 1
            $ team_suspicion += 1
            a "Right. Market route. I want visual confirmation of sector layout."
            unit3 "(pause) ...Confirmed."
            unit2 "That's slower, Glass."
            a "I know. Move."
            
            # VISUAL: Team exchanges glances—confusion but obedience.
            "{i}They follow. Questioning but obedient.{/i}"
            
            # SOUND: Market sounds grow louder—vendors, families, morning routines.
            "{i}The market district wakes. Voices rise. And they hear the boots.{/i}"
            "{i}Whispers spread. 'Echelon. Full tactical. Get inside. Hide.'{/i}"
            
            a "{i}Run. Please run. I'm buying you seconds. Use them.{/i}"

    # ==========================================
    # CHOICE 2: THE CHILD
    # ==========================================

    # VISUAL: Residential corridor. Doors sealed. Silence heavy.
    # SOUND: Movement behind a door—small, quick, panicked.

    unit4 "Movement. Door 7C."
    unit2 "Thermal confirms single occupant. Child-sized."
    
    # VISUAL: The door. Faint scratching from inside. Breathing.
    a "{i}A child. Alone. Hiding.{/i}"
    
    if aeron_warned_civilians:
        a "{i}Maybe the parents ran. Maybe they got out. Maybe.{/i}"
    else:
        a "{i}Parents are probably already dead. We came through their sector first.{/i}"

    unit3 "Breach?"
    
    # VISUAL: Aeron's hand raises—hold position.
    a "{i}Glass would breach. Confirm target. Eliminate if necessary.{/i}"
    a "{i}But I saw her. Three nights ago. She called me sad.{/i}"
    a "{i}Is this her? Or another child just like her?{/i}"

    menu:
        "The team waits for breach order. The door is thin. The child is small."
        "Breach and clear—follow protocol.":
            $ aeron_saved_child = False
            $ civilians_killed += 1
            $ team_suspicion += 0
            
            a "Breach. Confirm and clear."
            unit4 "Confirmed."
            
            # VISUAL: Door explodes inward. Flashbang. Smoke.
            # SOUND: Explosion; child's scream; suppressed burst.
            "{i}The door shatters. Light. Smoke. A scream—cut short.{/i}"
            
            unit4 "Target neutralized. Child. Approximately eight years old."
            unit2 "Confirmed hostile?"
            unit4 "...No weapon found. Cleared."
            
            # VISUAL: Silence. Static hum. Team moves on.
            a "{i}Glass doesn't hesitate. Glass eliminates threats.{/i}"
            a "{i}She wasn't a threat. She was terrified.{/i}"
            a "{i}And I killed her anyway.{/i}"
            
            $ evidence_of_mercy += 0
            
        "Mark as clear—fake the report.":
            $ aeron_saved_child = True
            $ civilians_saved += 1
            $ evidence_of_mercy += 1
            $ team_suspicion += 2
            
            a "(into comms) Door 7C, negative contact. Thermal ghost. Moving on."
            unit2 "(pause) ...Glass, I'm reading confirmed thermal—"
            a "(sharp) Negative contact. Thermal glitch. Mark and move."
            unit3 "(longer pause) ...Confirmed."
            
            # VISUAL: Team moves past door. Confused but obedient.
            "{i}They move on. Following orders. Questions in their silence.{/i}"
            
            # SOUND: From inside—quiet sobbing, muffled, alive.
            a "{i}Run, kid. Find a way out. Find your parents.{/i}"
            a "{i}I can't save everyone. But I can save you.{/i}"

    # ==========================================
    # CHOICE 3: THE VENDOR
    # ==========================================

    # VISUAL: Market square ahead. Stalls abandoned. One figure—the vendor from before.
    # PROP: His heat coils still glowing. Brew pot steaming. He's waiting.

    unit2 "Contact. Market square. Single adult male."
    unit3 "Armed?"
    unit2 "Negative. Standing by his stall."
    
    # VISUAL: Vendor sees them. Doesn't run. Just stands there.
    # His eyes meet Aeron's through the visor. Recognition.

    vendor "(quietly) Glass."
    
    a "{i}He knows. He knew I'd come.{/i}"
    a "{i}He's not running. Why isn't he running?{/i}"

    unit4 "Orders?"
    
    # VISUAL: The vendor's hands visible—empty, steady.
    vendor "I'm not running. Tell your men that."
    vendor "I'm not a rebel. I'm not a threat. I sell coffee."
    vendor "(looks at Aeron) You know that. You bought a cup three nights ago."
    
    # VISUAL: Team shifts—uncertain. Vendor isn't hostile. Just resigned.
    unit3 "Glass? Confirm hostile?"
    
    a "{i}He's not hostile. He's just tired.{/i}"
    a "{i}Glass eliminates all targets. Hostile or not.{/i}"
    a "{i}But he fed people. Kept them warm. Survived.{/i}"

    menu:
        "The vendor stands. The team waits. The brew pot steams."
        "Eliminate the target—he's in the sweep zone.":
            $ aeron_saved_vendor = False
            $ civilians_killed += 1
            $ team_suspicion += 0
            
            a "Confirmed hostile. Eliminate."
            unit2 "Confirmed."
            
            # VISUAL: Muzzle flash. Vendor falls. Brew pot spills.
            # SOUND: Suppressed burst; body falling; liquid hissing on concrete.
            "{i}Three rounds. Center mass. Professional. Clean.{/i}"
            "{i}The vendor falls. The brew spills. Steam rises like a ghost.{/i}"
            
            vendor "(dying) ...told you... it was better... than the Aeries..."
            
            # VISUAL: His hand reaches toward the overturned pot. Then stillness.
            a "{i}Glass doesn't hesitate. Glass doesn't feel.{/i}"
            a "{i}But I remember the taste. Real coffee. Real warmth.{/i}"
            a "{i}He'll never taste it again. Because of me.{/i}"
            
            $ evidence_of_mercy += 0
            
        "Order him to run—give him a chance.":
            $ aeron_saved_vendor = True
            $ civilians_saved += 1
            $ evidence_of_mercy += 2
            $ team_suspicion += 3
            
            a "(steps forward) You need to leave. Now."
            vendor "What?"
            a "Run. Get out of the sector. Don't come back."
            vendor "(confused) You're... letting me go?"
            a "I'm giving you ten seconds. Use them."
            
            # VISUAL: Vendor stares. Then understands. Nods once.
            vendor "...Thank you, Glass."
            vendor "(turns to run, stops) Your brother. He would've done the same."
            
            # VISUAL: Vendor runs. Disappears into shadow.
            "{i}He runs. Fast. Desperate. Alive.{/i}"
            
            unit3 "(confused) Glass, target is fleeing—"
            a "Let him go."
            unit2 "That's not protocol—"
            a "(hard) I said let him go. Mark as KIA. Faked body. Move on."
            unit4 "(quiet) ...Confirmed."
            
            "{i}Silence. They obey. But questions linger in their posture.{/i}"
            a "{i}They're noticing. Glass doesn't show mercy.{/i}"
            a "{i}But I did. And they saw.{/i}"

    # ==========================================
    # CHOICE 4: THE FAMILY SHELTER
    # ==========================================

    # VISUAL: Sublevel entrance. Heavy door. Behind it—thermal shows 200+ signatures.
    # SOUND: Muffled voices. Children. Families. Crowded together.

    unit2 "Primary target. Sublevel shelter. 200+ confirmed."
    unit3 "Families. Elders. Children. High civilian concentration."
    unit4 "Breach charges ready."
    
    a "{i}200 people. Behind one door. All together.{/i}"
    a "{i}Breach that door and it's over in minutes.{/i}"
    a "{i}Efficient. Clean. Glass.{/i}"

    unit2 "Orders, Glass?"
    
    # VISUAL: Aeron's hand on the door. Cold metal. He can hear them breathing inside.
    a "{i}Families around fires. That old man's stories. Children leaning in.{/i}"
    a "{i}All of them. Right here. Waiting to die.{/i}"
    a "{i}Glass follows orders. But Zira said find the cracks.{/i}"

    menu:
        "200 people behind one door. The team waits for breach order."
        "Breach and clear—complete the mission.":
            $ aeron_saved_shelter = False
            $ civilians_killed += 200
            $ team_suspicion += 0
            
            a "Breach. Full sweep. No survivors."
            unit2 "Confirmed."
            
            # VISUAL: Charges set. Timer beeps. Team stacks at door.
            "{i}Charges set. Three seconds. Two. One.{/i}"
            
            # SOUND: Explosion. Screams. Automatic fire. Chaos.
            # VISUAL: Flash of horror—smoke, running figures, children crying, stopping.
            "{i}The door explodes. Smoke pours in. And then—{/i}"
            "{i}Screaming. Running. Falling. Again. And again. And again.{/i}"
            
            # SOUND: Gunfire stops. Silence. Ringing ears.
            unit4 "Sector cleared. 200 confirmed."
            unit3 "No hostiles. All civilian."
            unit2 "...Mission complete."
            
            # VISUAL: Aeron stands at the door. Smoke clearing. Bodies visible.
            "{i}Glass executes. Glass doesn't question.{/i}"
            "{i}But the smoke clears and I see their faces.{/i}"
            "{i}The old man. The couple sharing food. The children.{/i}"
            "{i}All of them. Gone. Because I obeyed.{/i}"
            
            a "{i}Operation 391. Successful. Efficient. Perfect.{/i}"
            a "{i}Glass doesn't break. Glass doesn't feel.{/i}"
            a "{i}...Why am I shaking?{/i}"
            
            $ evidence_of_mercy += 0
            
        "Compromise—warn them, give them time to scatter.":
            $ aeron_saved_shelter = True
            $ civilians_saved += 150
            $ civilians_killed += 50
            $ evidence_of_mercy += 3
            $ team_suspicion += 4
            
            # VISUAL: Aeron removes a flashbang. Pulls pin.
            a "Flashbang first. Disorient and scatter. Then sweep."
            unit3 "That's not—"
            a "That's an order."
            
            # VISUAL: Throws flashbang through vent. Waits.
            # SOUND: Muffled explosion inside. Screaming. Panic.
            "{i}The flashbang detonates. Screaming erupts. Panic spreads.{/i}"
            
            # VISUAL: Door bursts open from inside—people running, scattering into corridors.
            "{i}The door explodes outward. People flood out. Running. Desperate. Alive.{/i}"
            
            unit2 "Targets scattering! Multiple corridors!"
            unit4 "We can't cover all exits!"
            a "Pursue Alpha corridor only. Let the others go."
            unit3 "Glass, that's—"
            a "(hard) Let. Them. Go."
            
            # VISUAL: Team hesitates. Then splits. Some run. Some stay.
            "{i}Some run. Some stay. We engage. Fifty fall. The rest escape.{/i}"
            
            # SOUND: Sporadic gunfire. Running footsteps fading. Then silence.
            unit2 "(breathing hard) ...150+ escaped. We lost them."
            a "Mark them as KIA. Report says full elimination."
            unit3 "Glass, they'll know—"
            a "They'll know what we tell them. Mark it."
            
            "{i}Silence. Then slow confirmations. They obey. But barely.{/i}"
            unit4 "(quiet) ...This isn't like you, Glass."
            a "No. It's not."
            
            a "{i}150 people alive. 50 dead. That's not victory.{/i}"
            a "{i}But it's better than 200 corpses. Better than perfect obedience.{/i}"
            a "{i}Glass is cracking. And I'm letting it.{/i}"

    # ==========================================
    # MISSION COMPLETION
    # ==========================================

    # VISUAL: Team regroups. Sector smoldering. Bodies counted. Reports compiled.
    # SOUND: Distant sirens. Fire crackling. Wind through ruins.

    unit2 "(into comms) Sector 10 sweep complete. Compiling final count."
    unit3 "Confirmed eliminations: [civilians_killed]. Mission parameters met."
    unit4 "Evidence of resistance activity: minimal. Mostly civilian infrastructure."
    
    # VISUAL: Aeron alone. Looks at his hands. Shaking.
    a "{i}It's done. 391 operations. The count continues.{/i}"
    
    if evidence_of_mercy >= 3:
        a "{i}But this time... this time I fought it. Saved who I could.{/i}"
        a "{i}[civilians_saved] people alive because Glass cracked.{/i}"
        a "{i}Is that enough? No. It's never enough.{/i}"
        a "{i}But it's more than Glass would have done.{/i}"
    elif evidence_of_mercy >= 1:
        a "{i}I tried. Saved a few. Not many. Not enough.{/i}"
        a "{i}But I tried. That's more than 390 operations of perfect obedience.{/i}"
    else:
        a "{i}I followed orders. Perfect execution. Zero hesitation.{/i}"
        a "{i}Glass doesn't crack. Glass doesn't save. Glass just cuts.{/i}"
        a "{i}And I cut them all.{/i}"

    # COMMS: Marcus
    m "Glass. Report."
    a "Mission complete. Sector 10 secured."
    m "Casualties?"
    
    if evidence_of_mercy >= 2:
        # Lying to Marcus
        a "...800 confirmed. Zero survivors."
        m "(pause) Efficient. Well done."
        a "{i}He believes the lie. He always does.{/i}"
        a "{i}Because Glass doesn't lie. Glass reports accurately.{/i}"
        a "{i}But I just did. And he didn't notice.{/i}"
    else:
        a "[civilians_killed] confirmed."
        m "Acceptable. Return to Aeries for debrief."
    
    m "You continue to prove your worth."
    
    # SOUND: Comms cut. Static. Silence.
    a "{i}Prove my worth. 391 times.{/i}"
    a "{i}How many more until I've proven enough?{/i}"
    a "{i}Or until there's nothing left to prove?{/i}"

    # VISUAL: Team boarding dropship. Aeron last to board. Looks back at sector.
    # LIGHTING: Dawn fully broken now. Sector 10 in ruins. Smoke rising.
    "{i}The sector burns. Families gone. Market silent. Shelters empty.{/i}"
    
    if aeron_saved_shelter:
        "{i}But not all empty. 150 are alive. Somewhere. Running.{/i}"
        a "{i}Run far. Stay hidden. Don't come back.{/i}"
    
    if aeron_saved_child:
        "{i}And one child. Somewhere in the rubble. Breathing.{/i}"
        a "{i}Find your parents. Find safety. Find anything but here.{/i}"
    
    if aeron_saved_vendor:
        "{i}And one vendor. Somewhere far. Alive because I let him run.{/i}"
        a "{i}Make more coffee. Keep people warm. Remember this day.{/i}"

    # VISUAL: Dropship lifts off. Sector shrinks below. City spreads beyond.
    "{i}The dropship climbs. Sector 10 shrinks. Just another mission. Just another count.{/i}"

    a "{i}But this time, Glass bled.{/i}"
    a "{i}This time, I felt it. Every death. Every choice. Every crack.{/i}"
    
    if evidence_of_mercy >= 2:
        a "{i}Zira said trying matters. Even if it's not enough.{/i}"
        a "{i}I tried. Glass tried to be human.{/i}"
        a "{i}Maybe that's the first real crack. The one that doesn't seal.{/i}"
    else:
        a "{i}I didn't try hard enough. I let Glass win.{/i}"
        a "{i}390 operations of obedience. This was supposed to be different.{/i}"
        a "{i}...It wasn't.{/i}"

    # VISUAL: His reflection in dropship window. Hollow eyes. Blood on uniform.
    "{i}His reflection stares back. Empty. Exhausted. Human.{/i}"
    a "{i}Glass doesn't cry. Glass doesn't break.{/i}"
    
    # VISUAL: Single tear. Barely visible.
    "{i}A tear. Just one. Glass cracking.{/i}"
    
    a "{i}Operation 391 complete.{/i}"
    a "{i}How many more until I'm hollow?{/i}"
    a "{i}Or maybe... maybe I already am.{/i}"

    # TRANSITION: Fade to black. Engine hum. Breathing.
    # TEXT: "Hours later. Aeron's apartment."

    # canon_note: Player choices determine civilians_saved (0-200+)
    # canon_note: evidence_of_mercy determines Zira's reaction at Obsidian Bridge
    # canon_note: team_suspicion plants seeds for future consequences (Act 2)
    # canon_note: Lying to Marcus (if mercy shown) = first deliberate defiance
    # canon_note: "Glass bled" = new identity - weapon with humanity, cracks permanent
    # canon_note: Sets up Lyra confession - he needs to break down after this
    # canon_note: 150+ saved = "good" outcome, 50-150 = "gray", <50 = "Glass won"

    return