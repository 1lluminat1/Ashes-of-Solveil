# act1_17_the_sweep.rpy


# =======================================================
# ACT 1 - Scene 17: The Sweep - Sector 10
# =======================================================


define unit2 = Character("[Unit-2]", color="#4A90E2")
define unit3 = Character("[Unit-3]", color="#4A90E2")
define unit4 = Character("[Unit-4]", color="#4A90E2")


label act1_sweep:
    $ scene_id = "act1_17_sweep"
    $ tier = get_alignment_tier()               # OB3..EMP3
    $ band = get_empathy_band()                 # "obedience" | "conflicted" | "empathy"

    # VISUAL: Pre-dawn. Sector 10 approach. Industrial decay. Steam vents. Neon dying.
    # LIGHTING: Cold blue pre-dawn; harsh tactical lights from dropship.
    # SOUND: Rotor wash; boot steps on metal; radio chatter; breathing through comms.

    "{i}Dawn breaks over Sector 10 like a blade.{/i}"
    "{i}The dropship descends. Tactical lights cut through steam. The sector wakes to its last morning.{/i}"

    # COMMS: Marcus (filtered, distant authority)
    m "Glass. Confirm deployment."
    a "Confirmed. Sector 10. Grid Six-Two."
    m "Rules of engagement?"
    a "Zero tolerance. Lethal force authorized."
    m "Acceptable collateral?"
    a "(pause) ...Within mission parameters."
    m "Good. Execute with precision. Prove your worth."
    
    a "{i}Prove your worth. Always the same words.{/i}"
    a "{i}390 operations proving my worth. This is 391.{/i}"

    unit2 "Sector's quiet. No alerts."
    unit3 "Thermal shows 800+ signatures. Clustered in sublevels."
    unit4 "Orders, Glass?"
    
    a "{i}800 people. The vendor. The child. The families.{/i}"
    a "{i}All waiting below. All trusting the dawn will come like it always does.{/i}"
    a "{i}Glass executes orders. But humans find cracks.{/i}"
    a "{i}Let's see if I can be both.{/i}"

    a "Standard sweep pattern. Alpha through Delta grids. Report all contacts."
    unit2 "Confirmed."

    # ==========================================
    # CHOICE 1: THE WARNING
    # ==========================================
    unit3 "Direct route is left. Fastest approach to target concentration."
    unit2 "Market district right. Slower but fewer civilians."
    unit4 "Orders?"

    a "{i}Left is efficient. Glass would go left.{/i}"
    a "{i}Right gives them time. Time to hear. Time to run.{/i}"

    menu:
        "The team waits. Dawn light catches his visor."
        "Take the direct route—efficient, by-the-book.":
            $ set_scene_flag(scene_id, "route_direct")
            a "Left. Direct approach. Standard protocol."
            unit2 "Confirmed. Moving."
            a "{i}Glass chooses efficiency. No mercy. Just execution.{/i}"
            a "{i}I'm sorry. I tried to prepare. But I can't save you all.{/i}"
            $ add_civilians_killed(50)
            $ add_team_suspicion(0)
            $ adjust_empathy_once("a17_route_direct", -1)
            
        "Detour through market—slower, gives them time to hear the approach.":
            $ set_scene_flag(scene_id, "route_market_warning")
            a "Right. Market route. I want visual confirmation of sector layout."
            unit3 "(pause) ...Confirmed."
            unit2 "That's slower, Glass."
            a "I know. Move."
            "{i}They follow. Questioning but obedient.{/i}"
            "{i}The market wakes. Whispers spread. 'Echelon. Full tactical. Get inside. Hide.'{/i}"
            a "{i}Run. Please run. I'm buying you seconds. Use them.{/i}"
            $ add_civilians_saved(50)
            $ add_evidence_of_mercy(1)
            $ add_team_suspicion(1)
            $ adjust_empathy_once("a17_route_market_warning", +1)

    # ==========================================
    # CHOICE 2: THE CHILD
    # ==========================================
    unit4 "Movement. Door 7C."
    unit2 "Thermal confirms single occupant. Child-sized."

    a "{i}A child. Alone. Hiding.{/i}"
    if check_scene_flag(scene_id, "route_market_warning"):
        a "{i}Maybe the parents ran. Maybe they got out. Maybe.{/i}"
    else:
        a "{i}Parents are probably already dead. We came through their sector first.{/i}"

    unit3 "Breach?"

    menu:
        "The team waits for breach order. The door is thin. The child is small."
        "Breach and clear—follow protocol.":
            a "Breach. Confirm and clear."
            unit4 "Confirmed."
            "{i}The door shatters. Light. Smoke. A scream—cut short.{/i}"
            unit4 "Target neutralized. Child. Approximately eight years old."
            unit2 "Confirmed hostile?"
            unit4 "...No weapon found. Cleared."
            a "{i}Glass doesn't hesitate. Glass eliminates threats.{/i}"
            a "{i}She wasn't a threat. She was terrified.{/i}"
            a "{i}And I killed her anyway.{/i}"
            $ add_civilians_killed(1)
            $ add_team_suspicion(0)
            $ adjust_empathy_once("a17_child_breach", -2)

        "Mark as clear—fake the report.":
            a "(into comms) Door 7C, negative contact. Thermal ghost. Moving on."
            unit2 "(pause) ...Glass, I'm reading confirmed thermal—"
            a "(sharp) Negative contact. Thermal glitch. Mark and move."
            unit3 "(longer pause) ...Confirmed."
            "{i}They move on. Following orders. Questions in their silence.{/i}"
            "{i}From inside—quiet sobbing, muffled, alive.{/i}"
            a "{i}Run, kid. Find a way out. Find your parents.{/i}"
            $ add_civilians_saved(1)
            $ add_evidence_of_mercy(1)
            $ add_team_suspicion(2)
            $ adjust_empathy_once("a17_child_fake_report", +1)

    # ==========================================
    # CHOICE 3: THE VENDOR
    # ==========================================
    unit2 "Contact. Market square. Single adult male."
    unit3 "Armed?"
    unit2 "Negative. Standing by his stall."

    vendor "(quietly) Glass."

    a "{i}He knows. He knew I'd come.{/i}"
    a "{i}He's not running. Why isn't he running?{/i}"

    unit4 "Orders?"

    vendor "I'm not running. Tell your men that."
    vendor "I'm not a rebel. I sell coffee."
    vendor "(looks at Aeron) You know that. You bought a cup three nights ago."

    menu:
        "The vendor stands. The team waits. The brew pot steams."
        "Eliminate the target—he's in the sweep zone.":
            a "Confirmed hostile. Eliminate."
            unit2 "Confirmed."
            "{i}Three rounds. Center mass. Clean.{/i}"
            vendor "(dying) ...told you... it was better... than the Aeries..."
            a "{i}Glass doesn't hesitate. Glass doesn't feel.{/i}"
            a "{i}But I remember the taste. Real coffee. Real warmth.{/i}"
            $ add_civilians_killed(1)
            $ add_team_suspicion(0)
            $ adjust_empathy_once("a17_vendor_eliminate", -1)
            
        "Order him to run—give him a chance.":
            a "(steps forward) You need to leave. Now."
            vendor "What?"
            a "Run. Get out of the sector. Don't come back."
            vendor "...Thank you, Glass."
            vendor "(turns to run, stops) Your brother. He would've done the same."
            "{i}He runs. Alive.{/i}"
            unit3 "(confused) Glass, target is fleeing—"
            a "Let him go. Mark as KIA. Move."
            "{i}Silence. They obey. But questions linger.{/i}"
            $ add_civilians_saved(1)
            $ add_evidence_of_mercy(2)
            $ add_team_suspicion(3)
            $ adjust_empathy_once("a17_vendor_spare", +1)

    # ==========================================
    # CHOICE 4: THE FAMILY SHELTER
    # ==========================================
    unit2 "Primary target. Sublevel shelter. 200+ confirmed."
    unit3 "Families. Elders. Children."
    unit4 "Breach charges ready."

    a "{i}200 people. Behind one door. All together.{/i}"
    a "{i}Breach that door and it's over in minutes.{/i}"

    menu:
        "200 people behind one door. The team waits for breach order."
        "Breach and clear—complete the mission.":
            a "Breach. Full sweep. No survivors."
            unit2 "Confirmed."
            "{i}Charges set. Three seconds. Two. One.{/i}"
            "{i}Explosion. Screams. Running. Falling.{/i}"
            unit4 "Sector cleared. 200 confirmed."
            unit3 "No hostiles. All civilian."
            unit2 "...Mission complete."
            a "{i}The old man. The couple. The children.{/i}"
            a "{i}All of them. Gone. Because I obeyed.{/i}"
            a "{i}Operation 391. Successful. Efficient. Perfect.{/i}"
            a "{i}...Why am I shaking?{/i}"
            $ add_civilians_killed(200)
            $ add_team_suspicion(0)
            $ adjust_empathy_once("a17_shelter_breach", -2)
            
        "Compromise—warn them, give them time to scatter.":
            a "Flashbang first. Disorient and scatter. Then sweep."
            unit3 "That's not—"
            a "That's an order."
            "{i}The flashbang detonates. Panic spreads.{/i}"
            "{i}The door bursts open. People flood out. Running. Alive.{/i}"
            unit2 "Targets scattering!"
            a "Pursue Alpha corridor only. Let the others go."
            unit3 "Glass, that's—"
            a "(hard) Let. Them. Go."
            "{i}Fifty fall. The rest escape.{/i}"
            unit2 "(breathing hard) ...150+ escaped."
            a "Mark them as KIA. Report says full elimination."
            "{i}Silence. Then slow confirmations.{/i}"
            a "{i}150 people alive. 50 dead. Better than perfect obedience.{/i}"
            $ add_civilians_saved(150)
            $ add_civilians_killed(50)
            $ add_evidence_of_mercy(3)
            $ add_team_suspicion(4)
            $ adjust_empathy_once("a17_shelter_compromise", +2)

    # ==========================================
    # MISSION COMPLETION
    # ==========================================
    unit2 "(into comms) Sector 10 sweep complete. Compiling final count."
    unit3 "Confirmed eliminations: [player_state['civilians_killed']]. Mission parameters met."
    unit4 "Evidence of resistance activity: minimal."

    a "{i}It's done. 391 operations. The count continues.{/i}"

    if player_state["evidence_of_mercy"] >= 3:
        a "{i}But this time I fought it. Saved who I could.{/i}"
        a "{i}[player_state['civilians_saved']] people alive because Glass cracked.{/i}"
        a "{i}Never enough. But more than Glass would’ve done.{/i}"
    elif player_state["evidence_of_mercy"] >= 1:
        a "{i}I tried. Saved a few. Not enough.{/i}"
        a "{i}But I tried. That’s more than 390 operations of obedience.{/i}"
    else:
        a "{i}I followed orders. Perfect execution. Zero hesitation.{/i}"
        a "{i}Glass doesn’t crack. Glass just cuts.{/i}"

    m "Glass. Report."
    a "Mission complete. Sector 10 secured."
    m "Casualties?"

    if player_state["evidence_of_mercy"] >= 2:
        a "...800 confirmed. Zero survivors."
        m "(pause) Efficient. Well done."
        a "{i}He believes the lie. Because Glass doesn’t lie.{/i}"
    else:
        a "[player_state['civilians_killed']] confirmed."
        m "Acceptable. Return to Aeries for debrief."

    m "You continue to prove your worth."

    # FINAL REFLECTION — alignment helpers
    if band == "empathy":
        a "{i}Zira said trying matters. Even if it’s not enough.{/i}"
        a "{i}I tried. Glass tried to be human.{/i}"
        a "{i}Maybe that’s the first crack that won’t seal.{/i}"
    elif band == "obedience":
        a "{i}Another mission. Another purge.{/i}"
        a "{i}No hesitation. No noise. Only efficiency.{/i}"
        a "{i}Glass doesn’t cry. Glass doesn’t bleed. Glass endures.{/i}"
    else:
        a "{i}I don’t know what I am anymore.{/i}"
        a "{i}Half weapon. Half man. Neither whole.{/i}"
        a "{i}But I felt it this time. Every breath. Every shot.{/i}"

    "{i}The dropship climbs. Sector 10 shrinks below—smoke, ash, silence.{/i}"
    a "{i}Operation 391 complete.{/i}"
    a "{i}Glass bled today. And the blood won’t wash off.{/i}"

    $ set_scene_flag(scene_id, "completed")
    return
