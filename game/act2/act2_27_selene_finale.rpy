# act2_27_selene_finale.rpy
# =======================================================
# ACT 2 - Scene 27: Selene - Respect Earned / Co-Commander (Act 2 Finale)
# =======================================================

label act2_finale:

    # VISUAL: Secondary base. Morning. A week after the battle. Rebuilding. Reorganizing. Continuing.
    # LIGHTING: Honest daylight — clear, natural. No dramatics. Just reality.
    # SOUND: Base operations hum. Soft mechanical ambience, voices, movement.
    # CAMERA: Slow pan through base activity — workers, training lines, supply chains — to command room.

    scene bg_secondary_base_morning with fade

    "{i}Morning. A week since the battle. Secondary base, Sector 9. We’re still here. Still rebuilding. 547 fighters operational. 41 dead counted. Tessa’s board grows. The resistance continues. The war continues. That’s reality. That’s us. That’s what we do — we continue.{/i}"

    "{i}The base has changed. Systems established, schedules posted, supplies moving. We’re not hiding anymore. Not just surviving. We’re functioning — organized, disciplined, dangerous. That’s growth. That’s resistance evolving. That’s us.{/i}"

    # VISUAL: SELENE at the command table. Maps, reports, schedules spread out.
    # LIGHTING: Morning light through cracked blinds, soft beams on data table.
    # CAMERA: Slow dolly in on Selene’s profile.

    "{i}Selene at the table — commander through and through. Reports stacked high, numbers precise. She’s carried this burden for years, maybe since the Purge. 847 dead then. Now she carries hundreds more. But not alone anymore. Maybe not anymore.{/i}"

    # VISUAL: AERON entering, datapad in hand.
    # CAMERA: Medium two-shot — distance between equals not yet bridged.

    a "Selene. Morning reports. Training cycles complete. Sector 7 supply chain stable. Medical coordination operational. Recruitment protocols finalized. Everything’s running."

    # VISUAL: Selene looking up, weary but impressed.
    s "You’ve been busy. Training schedules efficient. Logistics clean. Recruitment thorough. You’re not following orders anymore, Aeron — you’re making them. That’s leadership."

    a "Just doing what needed to be done. You were carrying everything alone. Seemed wrong. So I helped."

    # VISUAL: Selene studying him — quiet respect forming.
    s "You’re not just helping. People listen to you. Trust you. You’re not Glass anymore. You’re Aeron. Commander. Leader. Partner. Equal. And I need that."

    a "What are you saying?"

    # VISUAL: Selene stands, steps from behind table. Direct, unguarded.
    s "I’m saying you’ve earned this. Respect. Trust. Responsibility. I want to make it official — shared command. Shared burden. Shared decisions. Not me commanding you — us commanding together. Co-commanders. Partners. Equals."
    s "Will you lead with me?"

    # VISUAL: Beat — Aeron processing.
    "{i}Co-command. Equality. Partnership. Recognition I never asked for, but somehow earned. The question isn’t if I want it — it’s if I can carry it. 547 lives. Every choice a weight. Every death a mark. But I’ve already been carrying it. Time to stop pretending otherwise.{/i}"

    a "Yes. I accept. I’ll lead with you. I’ll carry this with you. Partners. Equals. Co-commanders."

    # VISUAL: Selene exhales — relief softens her face.
    s "Then it’s done. We lead together. Decide together. Share every weight. That’s command now."

    # VISUAL: Close-up on Aeron — feeling the title settle.
    "{i}The title lands like gravity. Recognition comes with burden. 547 lives pressing down — heavy, permanent. This is what she’s felt all along. And I accept it. Because someone has to. Because she shouldn’t carry it alone. That’s leadership. That’s us.{/i}"

    s "You feel it. Good. Leadership should be heavy. If it isn’t, you’re doing it wrong. That’s why this works. Why *we* work. You carry the weight with awareness — that’s strength."

    # VISUAL: Both at the table, maps between them.
    "{i}We stand on opposite sides of the same map. 547 lives in ink between us. Not commander and subordinate anymore — partners. Equals. Resistance feels real for the first time.{/i}"

    s "We have work. Training, supply coordination, base management. Echelon will come again — harder. We need to be ready."

    a "Together. Let’s begin."

    "{i}We work side by side. Planning, organizing, leading. Shared burden, shared strength. That’s resistance now. Not hierarchy — partnership. Not command — collaboration. We continue. Always continue. Together.{/i}"

    # VISUAL: Map overlay. Echelon red zones dwarfing resistance blue.
    s "Look at this. Echelon has thousands — trained, enhanced, disciplined. We have hundreds — scared, untested, but growing. We’re not winning yet. We’re surviving, threatening. That’s a start, not victory."

    s "This is the beginning of a long war."
    s "It will be hard and costly. People will die. The burden never lifts."
    s "Can you carry that? Lead knowing it never gets lighter?"

    # VISUAL: Aeron looks down at the map — silence. Then resolve.
    a "Yes. I can. I will. Because it matters. Because resistance matters. Even when it costs everything."

    # VISUAL: Selene finally smiles — rare, small, real.
    s "Then we continue. We lead. We fight. We endure. Welcome to command, Aeron."

    a "Let’s begin."

    # VISUAL: CAMERA: Slow pull-back — both working over the map.
    "{i}From twelve to 547. From hiding to army. From Glass to Aeron to Co-Commander. Journey complete — and only beginning. We lead. We fight. We resist. Together. Until victory or death. That’s us. That’s enough.{/i}"

    # =======================================================
    # CANON STATE UPDATES — ACT II COMPLETE
    # =======================================================

    # Mark scene complete
    $ scenes["selene_cocommander"] = True
    $ canon["aeron_cocommander"] = True
    $ canon["shared_leadership_established"] = True
    $ canon["act2_complete"] = True

    # Update leadership structure
    $ resistance_leadership = ["selene", "aeron"]  # Co-commanders, equals
    $ leadership_structure = "shared_command"
    $ command_partnership = True

    # Update Aeron’s status
    $ characters["aeron"]["rank"] = "co-commander"
    $ characters["aeron"]["leadership_official"] = True
    $ characters["aeron"]["carries_full_weight"] = True
    $ characters["aeron"]["partnership_with_selene"] = True

    # Update Selene’s respect
    $ characters["selene"]["respect_for_aeron"] = 10  # Maximum respect
    $ characters["selene"]["trusts_aeron_completely"] = True
    $ characters["selene"]["burden_shared"] = True  # No longer carries alone

    # Set stage for Act 3
    $ resistance_strength = 547
    $ resistance_dead = 41
    $ echelon_awareness = "confirmed_threat"  # Echelon now aware of resistance
    $ war_status = "beginning"
    $ act_status = "act2_complete"

    # Final stats
    $ stats["resistance_strength"] = 547
    $ stats["resistance_operational"] = 512
    $ stats["resistance_wounded"] = 35
    $ stats["total_casualties"] = 41
    $ stats["secondary_bases"] = 4
    $ stats["leadership_structure"] = "co-command"

    # TRANSITION: Act 2 complete — Growth achieved. Leadership established. War beginning.
    scene black with fade

    "{i}Act II complete. Glass became Aeron. Aeron became leader. Leader became co-commander. Twelve became 547. Hiding became army. Survival became resistance. Resistance became hope. And now? Now we lead. Now we fight. Now we win. Together. Forever. That’s Act III. That’s war. That’s us. That’s everything. Let’s begin.{/i}"

    return

    # =======================================================
    # CANON NOTES
    # =======================================================
    # - Scene 27 complete: Selene offers co-command; Aeron accepts.
    # - Tone: Quiet recognition, not triumph. “You’ve earned this.”
    # - Theme: Respect earned, burden shared, leadership’s cost.
    # - 547 fighters, 41 dead — tangible hope and loss.
    # - Partnership: Mutual respect, equal responsibility.
    # - Reality: Not victory — beginning of long war.
    # - Final image: Both at command table, morning light, shared burden.
    # - Journey: Glass → Aeron → Leader → Co-Commander.
    # - Leads directly into Act III: The Offensive / Resonance arc.
