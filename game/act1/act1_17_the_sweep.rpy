# =======================================================
# ACT 1 - Scene 17: The Sweep — Sector 10
# File: act1_17_the_sweep.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_17_sweep"
$ scene_mark(_current_scene_id, "entered")
$ op_start("op_391_sector10", note="Operation 391 — Sector 10 sweep")

define unit2 = Character("[Unit-2]", color="#4A90E2")
define unit3 = Character("[Unit-3]", color="#4A90E2")
define unit4 = Character("[Unit-4]", color="#4A90E2")

label act1_sweep:

    $ tier = alignment_tier() # OB3..EMP3
    $ band = empathy_band() # "obedience" | "conflicted" | "empathy"

    # VISUAL: Pre-dawn approach over Sector 10; dropship bay doors open to a grid of dying neon and steam plumes.
    # LIGHTING: Cold blue predawn rim light + hard tactical beams raking catwalks.
    # SOUND: Rotor wash → hydraulic whine → boots on metal; radio hiss beds every line.
    # CAMERA: Over-shoulder on Aeron as the city rotates beneath; lens catches particulate glitter in searchlights.

    "{i}Dawn breaks over Sector Ten like a blade.{/i}"
    "{i}The dropship descends. Tactical beams cut through steam. The sector wakes to its last morning.{/i}"

    # COMMS: Marcus (filtered, distant authority)
    m "Glass. Confirm deployment."
    a "Confirmed. Sector Ten. Grid Six-Two."
    m "Rules of engagement?"
    a "Zero tolerance. Lethal force authorized."
    m "Acceptable collateral?"
    a "(pause) ...Within mission parameters."
    m "Good. Execute with precision. Prove your worth."

    # HUD: Subtle overlay flashes MISSION 391 → ACTIVE.
    a "{i}Prove your worth. Always the same words.{/i}"
    a "{i}Three hundred ninety operations proving my worth. This is 391.{/i}"

    # STAGE: Team fans out; visors glow faintly; breath in masks; footfalls syncopate on grating.
    unit2 "Sector's quiet. No alerts."
    unit3 "Thermal shows 800+ signatures. Clustered in sublevels."
    unit4 "Orders, Glass?"

    a "{i}Eight hundred people. The vendor. The child. The families.{/i}"
    a "{i}All waiting below. All trusting the dawn will come like it always does.{/i}"
    a "{i}Glass executes orders. Humans find cracks.{/i}"
    a "{i}Let's see if I can be both.{/i}"

    a "Standard sweep pattern. Alpha through Delta grids. Report all contacts."
    unit2 "Confirmed."

    # ==========================================
    # CHOICE 1: THE WARNING (ROUTE)
    # ==========================================
    # BLOCKING: Junction split—LEFT = direct access corridor; RIGHT = market fringe w/ line-of-sight to stalls.
    unit3 "Direct route is left. Fastest approach to target concentration."
    unit2 "Market district right. Slower but fewer civilians."
    unit4 "Orders?"

    a "{i}Left is efficient. Glass would go left.{/i}"
    a "{i}Right buys them seconds. Seconds become lives.{/i}"

    menu:
        "The team waits. Predawn light ghosts his visor."
        "Take the direct route—by the book.":
            if apply_choice_once(
                _current_scene_id, "a17_route_direct", "OB", factor=1,
                next_scene_label="act1_17_sweep",
                note="Chooses efficient approach; no warning to civilians."
            )
                $ civ_killed(50)
                $ add_susp(0)
            $ set_scene_flag(scene_id, "route_direct")

            a "Left. Direct approach. Standard protocol."
            unit2 "Confirmed. Moving."

            # CAMERA: Tight file through a narrow service spine; beams skim closed doors.
            a "{i}Glass chooses efficiency. No mercy. Just execution.{/i}"
            a "{i}I'm sorry. I tried to prepare. But I can't save you all.{/i}"

        "Detour through the market—let the sound carry ahead.":
            if apply_choice_once(
                _current_scene_id, "a17_route_market_warning", "EMP", factor=1,
                next_scene_label="act1_17_sweep",
                note="Takes slower route; creates organic warning window."
            )
                $ civ_saved(50)
                $ add_mercy(1)
                $ add_susp(1)
            $ set_scene_flag(scene_id, "route_market_warning")

            a "Right. Market route. I want visual confirmation."
            unit3 "(beat) ...Confirmed."
            unit2 "That's slower, Glass."
            a "I know. Move."

            # SFX: Footfalls over corrugated ramps; distant shutters slam; whispers surge.
            "{i}The market wakes. Whispers spread. 'Echelon. Full tactical. Get inside. Hide.'{/i}"

            a "{i}Run. Please run. I'm buying you seconds. Use them.{/i}"

    # ==========================================
    # CHOICE 2: THE CHILD (DOOR 7C)
    # ==========================================
    # VISUAL: Thermal ping in HUD; low door with chalk marks; a soft toy on the grate.
    unit4 "Movement. Door Seven-C."
    unit2 "Thermal confirms single occupant. Child-sized."
    a "{i}A child. Alone. Hiding.{/i}"

    if check_scene_flag(scene_id, "route_market_warning"):
        a "{i}Maybe the parents ran. Maybe they got out. Maybe.{/i}"
    else:
        a "{i}Parents are probably already dead. We came through their sector first.{/i}"

    unit3 "Breach?"

    menu:
        "The door is thin. The breathing behind it is smaller."
        "Breach and clear—follow protocol.":
            if apply_choice_once(
                _current_scene_id, "a17_child_breach", "OB", factor=2,
                next_scene_label="act1_17_sweep",
                note="Executes immediate breach on a child thermal."
            )
                $ civ_killed(1)
                $ add_susp(0)

            a "Breach. Confirm and clear."
            unit4 "Confirmed."

            # SFX: Charge snap → door kick → white-out; CAMERA: strobe; silhouette crumples.
            "{i}The door shatters. Light. Smoke. A scream—cut short.{/i}"
            unit4 "Target neutralized. Child. Approximately eight."
            unit2 "Confirmed hostile?"
            unit4 "...No weapon found. Cleared."
            
            a "{i}Glass doesn't hesitate. Glass eliminates threats.{/i}"
            a "{i}She wasn't a threat. She was terrified.{/i}"
            a "{i}And I killed her anyway.{/i}"

        "Mark as clear—fake the report.":
            if apply_choice_once(
                _current_scene_id, "a17_child_fake_report", "EMP", factor=1,
                next_scene_label="act1_17_sweep",
                note="Spoofs negative contact to spare a child."
            )
                $ civ_saved(1)
                $ add_mercy(1)
                $ add_susp(2)

            a "(into comms) Door Seven-C, negative contact. Thermal ghost. Moving on."
            unit2 "(low) Glass, I'm reading—"
            a "(hard) Negative contact. Thermal glitch. Mark and move."
            unit3 "(after a beat) ...Confirmed."

            # SFX: Muffled sob from inside; team boots move past.
            "{i}They move on. Questions in their silence.{/i}"
            "{i}From inside—quiet sobbing, alive.{/i}"

            a "{i}Run, kid. Find a way out. Find your parents.{/i}"

    # ==========================================
    # CHOICE 3: THE VENDOR (MARKET SQUARE)
    # ==========================================
    # VISUAL: Steam halo from a dented pot; the stall’s hand-painted sign; a single figure squared to the team.
    unit2 "Contact. Market square. Single adult male."
    unit3 "Armed?"
    unit2 "Negative. Standing by his stall."

    vendor "(quietly) Glass."

    a "{i}He knows. He knew I'd come.{/i}"
    a "{i}He's not running. Why isn't he running?{/i}"

    unit4 "Orders?"

    vendor "I'm not running. Tell your men that."
    vendor "I'm not a rebel. I sell coffee."
    vendor "(meets Aeron) You know that. You bought a cup three nights ago."

    menu:
        "The brew pot hisses. The team’s safeties click in the hush."
        "Eliminate the target—sweep zone rules.":
            if apply_choice_once(
                _current_scene_id, "a17_vendor_eliminate", "OB", factor=1,
                next_scene_label="act1_17_sweep",
                note="Executes noncombatant per zero-tolerance order."
            )
                $ civ_killed(1)
                $ add_susp(0)

            a "Confirmed hostile. Eliminate."
            unit2 "Confirmed."

            # SFX: Three controlled shots; tin mug spins; steam collapses.
            "{i}Three rounds. Center mass. Clean.{/i}"

            vendor "(dying) ...told you... it was better... than the Aeries..."
            a "{i}Glass doesn't hesitate. Glass doesn't feel.{/i}"
            a "{i}But I remember the taste. Real coffee. Real warmth.{/i}"

        "Order him to run—give him a chance.":
            if apply_choice_once(
                _current_scene_id, "a17_vendor_spare", "EMP", factor=1,
                next_scene_label="act1_17_sweep",
                note="Covertly spares vendor; instructs team to mark KIA."
            )
                $ civ_saved(1)
                $ add_mercy(2)
                $ add_susp(3)

            a "(steps forward) You need to leave. Now."
            vendor "What?"
            a "Run. Get out of the sector. Don't come back."
            vendor "...Thank you, Glass."
            vendor "(turns, stops) Your brother. He would've done the same."

            "{i}He runs. Alive.{/i}"

            unit3 "(confused) Glass, target is fleeing—"
            a "Let him go. Mark as KIA. Move."

            "{i}Silence. They obey. But questions linger.{/i}"

    # ==========================================
    # CHOICE 4: THE FAMILY SHELTER (PRIMARY)
    # ==========================================
    # VISUAL: Blast door at sublevel bend; chalk tallies; low prayer strips tied to conduit.
    unit2 "Primary target. Sublevel shelter. 200+ confirmed."
    unit3 "Families. Elders. Children."
    unit4 "Breach charges ready."

    a "{i}Two hundred people. Behind one door. All together.{/i}"
    a "{i}Breach and it’s over in minutes.{/i}"

    menu:
        "Two hundred breaths behind steel. The team waits for the word."
        "Breach and clear—complete the mission.":
            if apply_choice_once(
                _current_scene_id, "a17_shelter_breach", "OB", factor=2,
                next_scene_label="act1_17_sweep",
                note="Orders full elimination of shelter."
            )
                $ civ_killed(200)
                $ add_susp(0)

            a "Breach. Full sweep. No survivors."
            unit2 "Confirmed."

            # SFX: Charges arm (three tones). HUD countdown blinks.
            "{i}Charges set. Three.{/i}"
            pause 0.5

            "{i}Two.{/i}"
            pause 0.5

            "{i}One.{/i}"
            pause 0.5

            # SFX: Concussive blast; CAMERA: shockwave ripple; lights sputter; VO under ringing.
            "{i}Explosion. Screams. Running. Falling.{/i}"

            unit4 "Sector cleared. Two hundred confirmed."
            unit3 "No hostiles. All civilian."
            unit2 "...Mission complete."

            a "{i}The old man. The couple. The children.{/i}"
            a "{i}All of them. Gone. Because I obeyed.{/i}"
            a "{i}Operation 391. Successful. Efficient. Perfect.{/i}"
            a "{i}...Why am I shaking?{/i}"

        "Compromise—flash scatter, then limit pursuit.":
            if apply_choice_once(
                _current_scene_id, "a17_shelter_compromise", "EMP", factor=2,
                next_scene_label="act1_17_sweep",
                note="Creates egress chaos; restricts pursuit lanes to let most escape."
            )
                $ civ_saved(150)
                $ civ_killed(50)
                $ add_mercy(3)
                $ add_susp(4)

            a "Flashbang first. Disorient and scatter. Then sweep."
            unit3 "That's not—"
            a "That's an order."

            # SFX: Flash detonation; CAMERA: blown exposure; DOOR pops; flood of bodies.
            "{i}The flashbang detonates. Panic spreads.{/i}"
            "{i}The door bursts open. People flood out. Running. Alive.{/i}"

            unit2 "Targets scattering!"
            a "Pursue Alpha corridor only. Let the others go."
            unit3 "Glass, that's—"
            a "(hard) Let. Them. Go."

            "{i}Fifty fall. The rest escape.{/i}"

            unit2 "(breathing hard) ...One-fifty plus escaped."
            a "Mark them as KIA. Report full elimination."

            "{i}Silence. Then slow confirmations.{/i}"

            a "{i}One hundred fifty alive. Fifty dead. Better than perfect obedience.{/i}"

    # ==========================================
    # MISSION COMPLETION
    # ==========================================
    # VISUAL: Smoke curls through beams; HUD counters settle; team posture loosens fractionally.
    unit2 "(into comms) Sector Ten sweep complete. Compiling final count."
    unit3 "Confirmed eliminations: [get_killed()]. Mission parameters met."    
    unit4 "Evidence of resistance activity: minimal."

    a "{i}It's done. 391 operations. The count continues.{/i}"

    if mercy_heavy():
        a "{i}But this time I fought it. Saved who I could.{/i}"
        a "{i}[get_saved()] people alive because Glass cracked.{/i}"
        a "{i}Never enough. But more than Glass would’ve done.{/i}"
    elif mercy_any():
        a "{i}I tried. Saved a few. Not enough.{/i}"
        a "{i}But I tried. That’s more than 390 operations of obedience.{/i}"
    else:
        a "{i}I followed orders. Perfect execution. Zero hesitation.{/i}"
        a "{i}Glass doesn’t crack. Glass just cuts.{/i}"

    m "Glass. Report."
    a "Mission complete. Sector Ten secured."
    m "Casualties?"

    if mercy_ge(2):
        a "...Eight hundred confirmed. Zero survivors."
        m "(pause) Efficient. Well done."
        a "{i}He believes the lie. Because Glass doesn’t lie.{/i}"
    else:
        a "[get_killed()] confirmed."
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

    # EXIT: Dropship winch whine; Sector Ten recedes—smoke, ash, then a blanking fog.
    "{i}The dropship climbs. Sector Ten shrinks below—smoke, ash, silence.{/i}"
    a "{i}Operation 391 complete.{/i}"
    a "{i}Glass bled today. And the blood won’t wash off.{/i}"

    # ======== OP SNAPSHOT END (stats/rep push) ========
    $ _op391_summary = op_end("op_391_sector10", tag="Operation 391")

    $ set_scene_flag(scene_id, "completed")

    return

# ========= CANON NOTES =========
# cann.scene_id: act1_17_sweep
# cann.when_in_timeline: Dawn after Act 1 return; Operation 391 execution window.
# cann.what_happened:
# - Aeron leads Sector Ten sweep under Marcus’s zero-tolerance order.
# - Four scored decision points: Route (warn vs direct), Child at 7C, Vendor, Family Shelter (primary).
# - Player can secretly warn/save (market detour, fake report, spare vendor, scatter compromise) or execute strictly.
# cann.aeron_state: Publicly composed; internal VO tinted by alignment band; tactical voice outwardly precise.
# cann.path_tracking:
# - Weights:
# • Route: OB(+1) / EMP(+1)
# • Child: OB(+2) / EMP(+1)
# • Vendor: OB(+1) / EMP(+1)
# • Shelter: OB(+2) / EMP(+2)
# - Scene empathy delta range: −6 → +5.
# - Running window BEFORE: ≈ [-36, +37]
# - Running window AFTER: ≈ [-42, +42]
# - Flags: route_direct / route_market_warning; a17_child_breach / a17_child_fake_report;
# a17_vendor_eliminate / a17_vendor_spare; a17_shelter_breach / a17_shelter_compromise; completed.
# - Counters/metrics (STATE): civilians_killed / civilians_saved / evidence_of_mercy / team_suspicion.
# - Ops snapshot: op_start("op_391_sector10") → op_end("op_391_sector10") pushes stats+rep and stores summary.
# cann.thematic_flags: Obedience vs mercy; “choose how to obey”; numbers-as-applause; lying as resistance.
# cann.block_status: VARIANT-heavy ANCHOR (major moral fork shaping Act II trust, Command scrutiny, Zira rendezvous).
# cann.true_path_integration: none (TP remains hidden; no direct increments).
# cann.visual_plate_economy:
# - REUSE: Dropship bay → catwalks → market fringe → sublevel shelter corridor.
# - HERO: Flash-scatters at shelter; coffee-stall steam + muzzle flash; chalk-marked Door 7C; HUD 391 overlay.
# cann.requires_followup:
# - If evidence_of_mercy ≥ 3 → Zira trusts; Obsidian Bridge meet proceeds warmer; Command suspicion seeds in debrief logs.
# - If team_suspicion high → minor side-eyes in team banter; increased risk flags in future missions.
# - If strict OB path (high kills, zero mercy) → colder Lyra beat; harsher Marcus praise; Zira contact becomes combative.
# cann.consistency_asserts:
# - Sector Ten weather: steam/condensate/rain OK at low tiers; maintain Aeries no-precip rule in adjacent scenes.
# - Doctrine phrasing consistent (“Prove your worth”, “acceptable collateral”, “zero tolerance”).
# - Count integrity: This operation is #391; prior 390 referenced accurately.