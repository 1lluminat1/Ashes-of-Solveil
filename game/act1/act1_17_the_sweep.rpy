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

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Over-shoulder on Aeron as city rotates beneath; tight file through corridors; HUD overlays.
    # LIGHTING: Cold blue predawn rim light + hard tactical beams raking catwalks.
    # SFX LOOP: Rotor wash → hydraulic whine → boots on metal; radio hiss beds every line.
    # SFX ONE-SHOTS: Charges, breach blasts, gunfire, flashbangs, door kicks.
    # BLOCKING: Dropship bay → catwalks → market fringe → sublevel shelter corridor.
    # PROP: Tactical gear, breach charges, HUD visor overlays.
    # FX/COMP: HUD counters, thermal overlays, mission status displays.

    #scene bg_sector10_approach with fade

    # ========= OPENING — DAWN DEPLOYMENT =========
    # VISUAL: Pre-dawn approach over Sector 10; dropship bay doors open to dying neon and steam plumes.

    "Dawn breaks over Sector Ten like a blade."

    "The dropship descends. Tactical beams cut through steam. The sector wakes to its last morning."

    # ========= MARCUS COMMS =========

    m "Glass. Confirm deployment."

    a "Confirmed. Sector Ten. Grid Six-Two."

    m "Rules of engagement?"

    a "Zero tolerance. Lethal force authorized."

    m "Acceptable collateral?"

    a "(pause) ...Within mission parameters."

    m "Good. Execute with precision. Prove your worth."

    # HUD: Subtle overlay flashes MISSION 391 → ACTIVE.

    athought "Prove your worth. Always the same words."

    athought "Three hundred ninety operations proving my worth. This is 391."

    # ========= TEAM DEPLOYMENT =========
    # VISUAL: Team fans out; visors glow faintly; breath in masks; footfalls syncopate on grating.

    unit2 "Sector's quiet. No alerts."

    unit3 "Thermal shows 800+ signatures. Clustered in sublevels."

    unit4 "Orders, Glass?"

    athought "Eight hundred people. The vendor. The child. The families."

    athought "All waiting below. All trusting the dawn will come like it always does."

    athought "Weapons execute orders. Humans find cracks."

    athought "Let's see if I can be both."

    a "Standard sweep pattern. Alpha through Delta grids. Report all contacts."

    unit2 "Confirmed."

    # ==========================================
    # CHOICE 1: THE WARNING (ROUTE)
    # ==========================================
    # BLOCKING: Junction split—LEFT = direct access corridor; RIGHT = market fringe w/ line-of-sight to stalls.

    unit3 "Direct route is left. Fastest approach to target concentration."

    unit2 "Market district right. Slower but fewer civilians."

    unit4 "Orders?"

    athought "Left is efficient. The weapon would go left."

    athought "Right buys them seconds. Seconds become lives."

    menu:
        athought "The team waits. Predawn light ghosts my visor."

        "Take the direct route—by the book.":
            $ choice_and_dev(
                _current_scene_id, "a17_route_direct", "OB", factor=1,
                note="Chooses efficient approach; no warning to civilians."
            )
            $ civ_killed(50)
            $ scene_mark(_current_scene_id, "route_direct")

            a "Left. Direct approach. Standard protocol."

            unit2 "Confirmed. Moving."

            # CAMERA: Tight file through a narrow service spine; beams skim closed doors.

            athought "Efficiency. No mercy. Just execution."

            athought "I'm sorry. I tried to prepare. But I can't save you all."

        "Detour through the market—let the sound carry ahead.":
            $ choice_and_dev(
                _current_scene_id, "a17_route_market_warning", "EMP", factor=1,
                note="Takes slower route; creates organic warning window."
            )
            $ civ_saved(50)
            $ add_mercy(1)
            $ add_susp(1)
            $ scene_mark(_current_scene_id, "route_market_warning")

            a "Right. Market route. I want visual confirmation."

            unit3 "(beat) ...Confirmed."

            unit2 "That's slower, Glass."

            a "I know. Move."

            # SFX: Footfalls over corrugated ramps; distant shutters slam; whispers surge.

            "The market wakes. Whispers spread. 'Echelon. Full tactical. Get inside. Hide.'"

            athought "Run. Please run. I'm buying you seconds. Use them."

    # ==========================================
    # CHOICE 2: THE CHILD (DOOR 7C)
    # ==========================================
    # VISUAL: Thermal ping in HUD; low door with chalk marks; a soft toy on the grate.

    unit4 "Movement. Door Seven-C."

    unit2 "Thermal confirms single occupant. Child-sized."

    athought "A child. Alone. Hiding."

    if scene_has(_current_scene_id, "route_market_warning"):
        athought "Maybe the parents ran. Maybe they got out. Maybe."
    else:
        athought "Parents are probably already dead. We came through their sector first."

    unit3 "Breach?"

    menu:
        athought "The door is thin. The breathing behind it is smaller."

        "Breach and clear—follow protocol.":
            $ choice_and_dev(
                _current_scene_id, "a17_child_breach", "OB", factor=2,
                note="Executes immediate breach on a child thermal."
            )
            $ civ_killed(1)
            $ scene_mark(_current_scene_id, "child_breach")

            a "Breach. Confirm and clear."

            unit4 "Confirmed."

            # SFX: Charge snap → door kick → white-out; CAMERA: strobe; silhouette crumples.

            "The door shatters. Light. Smoke. A scream—cut short."

            unit4 "Target neutralized. Child. Approximately eight."

            unit2 "Confirmed hostile?"

            unit4 "...No weapon found. Cleared."

            athought "No hesitation. Threat eliminated."

            athought "She wasn't a threat. She was terrified."

            athought "And I killed her anyway."

        "Mark as clear—fake the report.":
            $ choice_and_dev(
                _current_scene_id, "a17_child_fake_report", "EMP", factor=1,
                note="Spoofs negative contact to spare a child."
            )
            $ civ_saved(1)
            $ add_mercy(1)
            $ add_susp(2)
            $ scene_mark(_current_scene_id, "child_spared")

            a "(into comms) Door Seven-C, negative contact. Thermal ghost. Moving on."

            unit2 "(low) Glass, I'm reading—"

            a "(hard) Negative contact. Thermal glitch. Mark and move."

            unit3 "(after a beat) ...Confirmed."

            # SFX: Muffled sob from inside; team boots move past.

            "They move on. Questions in their silence."

            "From inside—quiet sobbing, alive."

            athought "Run, kid. Find a way out. Find your parents."

    # ==========================================
    # CHOICE 3: THE VENDOR (MARKET SQUARE)
    # ==========================================
    # VISUAL: Steam halo from a dented pot; the stall's hand-painted sign; a single figure squared to the team.

    unit2 "Contact. Market square. Single adult male."

    unit3 "Armed?"

    unit2 "Negative. Standing by his stall."

    vendor "(quietly) Glass."

    athought "He knows. He knew I'd come."

    athought "He's not running. Why isn't he running?"

    unit4 "Orders?"

    vendor "I'm not running. Tell your men that."

    vendor "I'm not a rebel. I sell coffee."

    vendor "(meets Aeron) You know that. You bought a cup three nights ago."

    menu:
        athought "The brew pot hisses. Safeties click in the hush."

        "Eliminate the target—sweep zone rules.":
            $ choice_and_dev(
                _current_scene_id, "a17_vendor_eliminate", "OB", factor=1,
                note="Executes noncombatant per zero-tolerance order."
            )
            $ civ_killed(1)
            $ scene_mark(_current_scene_id, "vendor_killed")

            a "Confirmed hostile. Eliminate."

            unit2 "Confirmed."

            # SFX: Three controlled shots; tin mug spins; steam collapses.

            "Three rounds. Center mass. Clean."

            vendor "(dying) ...told you... it was better... than the Aeries..."

            athought "No hesitation. No feeling."

            athought "But I remember the taste. Real coffee. Real warmth."

        "Order him to run—give him a chance.":
            $ choice_and_dev(
                _current_scene_id, "a17_vendor_spare", "EMP", factor=1,
                note="Covertly spares vendor; instructs team to mark KIA."
            )
            $ civ_saved(1)
            $ add_mercy(2)
            $ add_susp(3)
            $ scene_mark(_current_scene_id, "vendor_spared")

            a "(steps forward) You need to leave. Now."

            vendor "What?"

            a "Run. Get out of the sector. Don't come back."

            vendor "...Thank you, Glass."

            vendor "(turns, stops) Your brother. He would've done the same."

            "He runs. Alive."

            unit3 "(confused) Glass, target is fleeing—"

            a "Let him go. Mark as KIA. Move."

            "Silence. They obey. But questions linger."

    # ==========================================
    # CHOICE 4: THE FAMILY SHELTER (PRIMARY)
    # ==========================================
    # VISUAL: Blast door at sublevel bend; chalk tallies; low prayer strips tied to conduit.

    unit2 "Primary target. Sublevel shelter. 200+ confirmed."

    unit3 "Families. Elders. Children."

    unit4 "Breach charges ready."

    athought "Two hundred people. Behind one door. All together."

    athought "Breach and it's over in minutes."

    menu:
        athought "Two hundred breaths behind steel. The team waits for the word."

        "Breach and clear—complete the mission.":
            $ choice_and_dev(
                _current_scene_id, "a17_shelter_breach", "OB", factor=2,
                note="Orders full elimination of shelter."
            )
            $ civ_killed(200)
            $ scene_mark(_current_scene_id, "shelter_breached")

            a "Breach. Full sweep. No survivors."

            unit2 "Confirmed."

            # SFX: Charges arm (three tones). HUD countdown blinks.

            "Charges set. Three."

            pause 0.5

            "Two."

            pause 0.5

            "One."

            pause 0.5

            # SFX: Concussive blast; CAMERA: shockwave ripple; lights sputter; VO under ringing.

            "Explosion. Screams. Running. Falling."

            unit4 "Sector cleared. Two hundred confirmed."

            unit3 "No hostiles. All civilian."

            unit2 "...Mission complete."

            athought "The old man. The couple. The children."

            athought "All of them. Gone. Because I obeyed."

            athought "Operation 391. Successful. Efficient. Perfect."

            athought "...Why am I shaking?"

        "Compromise—flash scatter, then limit pursuit.":
            $ choice_and_dev(
                _current_scene_id, "a17_shelter_compromise", "EMP", factor=2,
                note="Creates egress chaos; restricts pursuit lanes to let most escape."
            )
            $ civ_saved(150)
            $ civ_killed(50)
            $ add_mercy(3)
            $ add_susp(4)
            $ scene_mark(_current_scene_id, "shelter_scattered")

            a "Flashbang first. Disorient and scatter. Then sweep."

            unit3 "That's not—"

            a "That's an order."

            # SFX: Flash detonation; CAMERA: blown exposure; DOOR pops; flood of bodies.

            "The flashbang detonates. Panic spreads."

            "The door bursts open. People flood out. Running. Alive."

            unit2 "Targets scattering!"

            a "Pursue Alpha corridor only. Let the others go."

            unit3 "Glass, that's—"

            a "(hard) Let. Them. Go."

            "Fifty fall. The rest escape."

            unit2 "(breathing hard) ...One-fifty plus escaped."

            a "Mark them as KIA. Report full elimination."

            "Silence. Then slow confirmations."

            athought "One hundred fifty alive. Fifty dead. Better than perfect obedience."

    # ==========================================
    # MISSION COMPLETION
    # ==========================================
    # VISUAL: Smoke curls through beams; HUD counters settle; team posture loosens fractionally.

    unit2 "(into comms) Sector Ten sweep complete. Compiling final count."

    unit3 "Confirmed eliminations: [get_killed()]. Mission parameters met."

    unit4 "Evidence of resistance activity: minimal."

    athought "It's done. 391 operations. The count continues."

    if mercy_heavy():
        athought "But this time I fought it. Saved who I could."
        athought "[get_saved()] people alive because something in me cracked."
        athought "Never enough. But more than obedience would've allowed."
    elif mercy_any():
        athought "I tried. Saved a few. Not enough."
        athought "But I tried. That's more than 390 operations of obedience."
    else:
        athought "I followed orders. Perfect execution. Zero hesitation."
        athought "Weapons don't crack. Weapons just cut."

    # ========= MARCUS DEBRIEF =========

    m "Glass. Report."

    a "Mission complete. Sector Ten secured."

    m "Casualties?"

    if mercy_ge(2):
        a "...Eight hundred confirmed. Zero survivors."
        m "(pause) Efficient. Well done."
        athought "He believes the lie. Because I've never lied before."
    else:
        a "[get_killed()] confirmed."
        m "Acceptable. Return to Aeries for debrief."

    m "You continue to prove your worth."

    # ========= FINAL REFLECTION — ALIGNMENT-BASED =========

    if empathy_band() == "empathy":
        athought "Zira said trying matters. Even if it's not enough."
        athought "I tried. I tried to be human."
        athought "Maybe that's the first crack that won't seal."
    elif empathy_band() == "obedience":
        athought "Another mission. Another purge."
        athought "No hesitation. No noise. Only efficiency."
        athought "I don't cry. I don't bleed. I endure."
    else:
        athought "I don't know what I am anymore."
        athought "Half weapon. Half man. Neither whole."
        athought "But I felt it this time. Every breath. Every shot."

    # ========= EXIT =========
    # VISUAL: Dropship winch whine; Sector Ten recedes—smoke, ash, then a blanking fog.

    "The dropship climbs. Sector Ten shrinks below—smoke, ash, silence."

    athought "Operation 391 complete."

    athought "I bled today. And the blood won't wash off."

    # ======== OP SNAPSHOT END (stats/rep push) ========
    $ _op391_summary = op_end("op_391_sector10", tag="Operation 391")

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_17_sweep
# cann.when_in_timeline: Dawn after Act 1 return; Operation 391 execution window.
# cann.what_happened:
#   - Aeron leads Sector Ten sweep under Marcus's zero-tolerance order.
#   - Four scored decision points: Route (warn vs direct), Child at 7C, Vendor, Family Shelter (primary).
#   - Player can secretly warn/save (market detour, fake report, spare vendor, scatter compromise) or execute strictly.
# cann.aeron_state: Publicly composed; internal VO tinted by alignment band; tactical voice outwardly precise.
# cann.path_tracking:
#   - Weights:
#       • Route: OB(+1) / EMP(+1)
#       • Child: OB(+2) / EMP(+1)
#       • Vendor: OB(+1) / EMP(+1)
#       • Shelter: OB(+2) / EMP(+2)
#   - Scene empathy delta range: −6 → +5.
#   - Flags: route_direct / route_market_warning; child_breach / child_spared;
#     vendor_killed / vendor_spared; shelter_breached / shelter_scattered; completed.
#   - Counters/metrics: civ_killed / civ_saved / add_mercy / add_susp.
#   - Ops snapshot: op_start → op_end pushes stats+rep and stores summary.
# cann.thematic_flags: Obedience vs mercy; "choose how to obey"; numbers-as-applause; lying as resistance.
# cann.block_status: VARIANT-heavy ANCHOR (major moral fork shaping Act II trust, Command scrutiny, Zira rendezvous).
# cann.visual_plate_economy:
#   - REUSE: Dropship bay → catwalks → market fringe → sublevel shelter corridor.
#   - HERO: Flash-scatters at shelter; coffee-stall steam + muzzle flash; chalk-marked Door 7C; HUD 391 overlay.
# cann.requires_followup:
#   - If mercy ≥ 3 → Zira trusts; Obsidian Bridge meet proceeds warmer; Command suspicion seeds in debrief.
#   - If team_suspicion high → minor side-eyes in team banter; increased risk flags in future missions.
#   - If strict OB path → colder Lyra beat; harsher Marcus praise; Zira contact becomes combative.
# cann.note_on_glass_usage:
#   - "Glass" is Aeron's street name/callsign used by other characters (Marcus, vendor, team).
#   - Aeron's internal self-references replaced with first-person language.