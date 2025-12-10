# act2_16_established_base.rpy

# =======================================================
# ACT 2 - Scene 16: Established Base (Two Months Later)
# (New helper system + OB/EMP flavor; no dialogue trimmed)
# =======================================================

# NOTE: Helper system references:
# - mark_scene(key)
# - mark_flag(key, value=True)
# - rel(who, **kwargs)
# - log_line(tag, text)
# - set_emp(subject, delta)
# - set_ob(subject, delta)
# - snapshot_state(subject, **fields)

label act2_establishing_base:

    # --- OB/EMP alignment read (light flavor only; no momentum) ---
    $ tier = get_alignment_tier()            # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")    # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")      # ≈ -3..+1
    # empathy side = else

    # VISUAL: Temp shelter. Final night. People packing. Preparing to move.
    # LIGHTING: Dim. Transitional. Ending and beginning.
    # SOUND: Packing. Movement. Anticipation.

    #scene bg_temp_shelter_night with fade

    "Final night in temp shelter. Tomorrow we move. Tomorrow we start building for real. Tonight we pack everything we have. Which isn't much. But it's ours. And tomorrow it becomes foundation."

    # VISUAL: Resistance fighters packing gear. Weapons. Supplies. Hope.
    s "Pack everything. Leave nothing. We were never here. Ghosts don't leave traces."
    s "Tomorrow we move to permanent location. Tomorrow we stop hiding and start building. Get rest. Tomorrow's a long day. First of many."

    # VISUAL: Aeron and Lyra packing together. Quiet moment. Processing change.
    l "Two months ago we were running from Echelon with nothing. Now we're building resistance base. Strange how fast things change."
    a "Or how slow. Feels like we've been running forever. Maybe this is where we stop running and start standing."
    l "Standing gets you killed."
    a "So does running. Eventually. At least standing means something."

    # VISUAL: Lights dimming. Night settling. Tomorrow approaching.
    "Night falling. Last night in temporary shelter. Tomorrow permanent. Tomorrow real. Tomorrow everything changes. Again. Always again. But this time toward something instead of away from something. That's different. That matters."

    # --- OB/EMP FLAVOR #1: pre time-skip inner monologue (very light) ---
    if is_ob_hard:
        "{ob}Checklist: pack count, exit route, staggered watch, comms test, last sweep for trace. Keep hands busy; keep noise down.{/ob}"
    elif is_mid:
        "Pack tight, move quiet. Leave the ghosts nothing to follow."
    else:
        "{emp}Count the living. Breathe in fours. We carry more than bags tonight—names, promises, the thin thread called tomorrow.{/emp}"

    # TRANSITION: Fade to black. Time passing. Work happening. Base building.
    #scene black with fade

    # TEXT ON SCREEN: "Two Months Later"
    centered "{size=+10}Two Months Later{/size}"

    # VISUAL: Fade in to ESTABLISHED BASE. Morning. Functional. Lived-in.
    # Location varies based on player choice. Will use generic description then branch.

    if base_location == "subway":
        #scene bg_subway_base_established with fade
        "Two months of work. Subway station transformed. Platforms cleaned. Service rooms converted to living quarters. Power restored. Water filtration installed. Multiple tunnel exits secured and mapped. Central hub operational. This is home now. Underground. Hidden. Ours."
        
    elif base_location == "clinic":
        #scene bg_clinic_base_established with fade
        "Two months of work. Clinic rebuilt. Exam rooms now living quarters. Operating theater functional for actual medical work. Storage organized. Three floors compartmentalized for different operations. Windows reinforced. Sector 7 locals aware and supportive. This is home now. Visible but protected. Ours."
        
    elif base_location == "warehouse":
        #scene bg_warehouse_base_established with fade
        "Two months of work. Warehouse reinforced. East side structural damage repaired. Multiple levels cleared and organized. Training space established. Supply storage secured. Smuggling route access confirmed. Massive space ready for expansion. This is home now. Room to grow. Ours."
        
    elif base_location == "apartment":
        #scene bg_apartment_base_established with fade
        "Two months of work. Apartment complex fortified. Multiple units converted. Living quarters separate from operations. Rooftop observation posts established. Stairwells secured. Residential disguise maintained. Eight stories of tactical advantage. This is home now. High ground held. Ours."
        
    else:  # tunnels
        #scene bg_tunnels_base_established with fade
        "Two months of work. Maintenance tunnels mapped and secured. Multiple cache points established throughout network. Living areas as comfortable as possible given constraints. Mobile infrastructure tested. Unknown to Echelon. Hidden in city's veins. This is home now. Secret. Safe. Ours."

    # VISUAL: Morning in established base. People waking. Moving. Living here.
    # Resistance fighters going about routines. Breakfast. Training. Operations. Normal life in abnormal circumstances.

    "Morning. People waking. Moving through base like they live here. Because they do. This isn't shelter anymore. This is home. Makeshift. Dangerous. But home. We built this. From nothing. From twelve people and desperation. Now it's real. Now it's ours."

    # VISUAL: Common area. People gathering. Breakfast happening. Community forming.
    # More people than before. Recruitment worked. 12 became 18, maybe 20.

    "Common area. People eating breakfast. Not just the original twelve. More. Eighteen now. Maybe twenty. Hard to keep exact count with people coming and going on missions. Recruitment worked. We're growing. Slowly. But growing."

    # VISUAL: Aeron entering common area. Morning routine established. Familiar.
    resistance_fighter1 "Morning, Aeron. Sleep okay?"
    a "Well enough. You?"
    resistance_fighter1 "Better since we got real beds instead of concrete floor. Luxury."
    a "Compared to temp shelter, everything's luxury."

    # VISUAL: Lyra already there. Coffee in hand. Looking more settled. Comfortable.
    l "You're late. I already claimed the good coffee."
    a "There's good coffee?"
    l "No. But I claimed it anyway. Principle of the thing."

    # VISUAL: Comfortable banter. Routine established. This is life now.
    "Banter. Easy. Comfortable. This is life now. Not just surviving. Actually living. Having routines. Having coffee arguments. Having moments that aren't life or death. Just moments. That's progress."

    # --- OB/EMP FLAVOR #2: morning scan in the established base (very light) ---
    if is_ob_hard:
        "{ob}Headcount, choke points, watch turnover, sightlines to both entrances. Routines hold. Discipline holds. That’s how we live.{/ob}"
    elif is_mid:
        "People, patterns, posts. You can feel when a place starts keeping you alive."
    else:
        "{emp}Names at tables, laughter by the kettle, tired shoulders easing. Home isn’t walls—it’s the people who exhale inside them.{/emp}"

    # VISUAL: Noelle at corner table. Surrounded by datapads. Working. Always working.
    n "(not looking up) Aeron. Morning. Current Echelon patrol efficiency has decreased 13% over past two months. Predictive models suggest our operational security is holding. Probability of discovery remains under 10% per month."

    # VISUAL: Aeron sits near her. Used to her constant analysis now.
    a "That's good news."
    n "Yes. Acceptable outcome. Base location proving strategically sound. Your scouting was adequate."
    a "I'll take 'adequate' from you as high praise."
    n "(small smile) It is. You're learning to interpret my communication patterns. That's efficient. I appreciate efficiency."

    # VISUAL: Tessa entering. Carrying medical supplies. Organizing. Humming softly.
    t "Morning, everyone. Beautiful day to be alive and resisting tyranny."
    resistance_fighter2 "Is it? Looks gray and depressing to me."
    t "That's because you're not counting the living. We're all here. All breathing. That's beautiful. Gray's just aesthetic."

    # VISUAL: Her clinic setup (if clinic base) or medical station (other bases). Organized. Functional.
    if base_location == "clinic":
        t "Clinic's running smoothly. Treated three locals yesterday. Building goodwill and cover. Operating theater's fully functional now. We can do real surgeries if needed."
    else:
        t "Medical station's organized. Not as good as real clinic but functional. Can handle everything from minor wounds to major trauma. We're prepared."

    # VISUAL: Zira entering. Been out all night. Intel gathering. Returns. Safe.
    z "Morning. Anyone miss me?"
    a "Always. Find anything interesting?"
    z "Depends on your definition of interesting. Echelon's mobilizing in Sector 12. Big operation. Don't know target yet but it's significant. Brought that intel back for Selene."

    # VISUAL: Brief moment. Eye contact. Something between them now. Undefined but present.
    # If kiss happened, there's warmth. Comfort. Shared secret.
    if characters["zira"].get("kiss_happened", False):
        "Brief moment. Eye contact. Warmth there. Comfort. Memory of kiss in warehouse two months ago. Haven't talked about it. Haven't repeated it. But it's there. Between us. Changing how we exist around each other. Making proximity feel different. Better. Wanted."
        z "(quiet, just to him) Glad you're here when I get back. Makes coming back easier."
        a "(quiet) Glad you come back. Makes being here easier."

    # VISUAL: Selene entering. Command presence. Leader energy. Everyone notices.
    s "Morning. Everyone's here. Good. Time to talk."

    # VISUAL: People gathering. Attention shifting. Leader speaking. Everyone listens.
    s "Two months. That's how long we've been here. Two months of building. Cleaning. Organizing. Securing. Making this place home."
    s "When we moved in we were twelve people with barely enough weapons and one week of supplies. Now we're twenty. Armed. Supplied. Operational."

    # VISUAL: Looking around room. Seeing progress. Seeing potential. Seeing hope.
    s "This base works. Security's holding. Echelon hasn't found us. Locals either support us or ignore us. That's strategic success. That's foundation."
    s "We're not just surviving anymore. We're operational. We're ready. Time to start hitting back."

    # VISUAL: Resistance fighters stirring. Energy shifting. This is what they've been waiting for.
    resistance_fighter3 "What's the mission?"
    s "Small. Targeted. Proving we can execute operations without getting caught or killed. Building toward bigger things. But small first. Crawl before run."

    # VISUAL: Spreading map on table. Marking locations. Planning. Tactical.
    s "Echelon supply depot. Sector 9. Light guard. Medical supplies and weapons. Small enough we can hit it without massive response. Valuable enough it hurts them and helps us."
    s "We plan. We execute. We prove we're dangerous. Then we scale up. Bigger targets. Bigger impact. Bigger war."

    # VISUAL: Noelle stepping forward. Data ready. Analysis prepared.
    n "I've analyzed patrol patterns for Sector 9 depot. Optimal strike window exists between 0200 and 0400 hours. Guard rotation creates 47-minute vulnerability window. Probability of success with proper execution: 78%."

    # VISUAL: Tessa also stepping forward. Medical perspective. Humanitarian.
    t "Those medical supplies would let me treat twice as many people. Resistance and civilians. Building community support while building operational capacity. Strategic and moral."

    # VISUAL: Zira adding intel. Practical details. Ground truth.
    z "I've been watching that depot for three weeks. Noelle's right about vulnerability window. Two guards. Standard patrol. They're bored and complacent. We can do this."

    # VISUAL: Lyra analyzing map. Tactical mind working. Planning approach.
    l "Access from north side. Two entry points. Exfil route through maintenance corridor. Standard grab and go. Military textbook operation. We can execute this clean."

    # VISUAL: Everyone contributing. Team functioning. Resistance real. Operational. Ready.
    "Everyone contributing. Each person adding expertise. Noelle's data. Tessa's medical needs. Zira's ground intel. Lyra's tactics. This is team. This is resistance. This is what we built. Twenty people working together toward common goal. That's dangerous. That's powerful. That's everything."

    # VISUAL: Selene looking at Aeron. Question implicit. You're part of leadership now.
    s "Aeron. You've been quiet. Thoughts?"
    
    # VISUAL: All eyes on him. Opinion matters. Voice matters. Leadership emerging.
    a "I think we're ready. Two months of preparation. Good intelligence. Solid plan. Minimal risk. Maximum value. This is what we built this base for. Time to use it."
    s "Agreed. We strike in three days. Gives us time to finalize details. Prepare equipment. Rehearse. Do this right."
    s "This is first operation from this base. First real mission as functional resistance. We do it clean. We do it smart. We prove we're dangerous. Clear?"

    # VISUAL: Everyone responding. Agreement. Determination. Purpose. Ready.
    resistance_all "Clear."

    # VISUAL: Selene nodding. Satisfied. Leader confident in team. Team confident in leader.
    s "Good. Meeting adjourned. Operations planning this afternoon. Everyone involved in strike team attends. Everyone else continues base operations. Stay sharp. Stay ready. We're moving from building phase to fighting phase. Everything changes now."

    # VISUAL: People dispersing. Energy different. Purpose clear. Direction set.
    "People dispersing. But energy changed. We're not just hiding anymore. Not just building. We're about to fight. About to hit Echelon. About to prove we're dangerous. That changes everything. Makes it real. Makes it war."

    # VISUAL: Aeron and Lyra remaining. Processing. Moment together.
    l "First mission from new base. Nervous?"
    a "Terrified. But that's normal now. Terror's just background noise."
    l "When did we get so used to being terrified?"
    a "Somewhere between the Sweep and now. Just became default state. Functional terror."

    # VISUAL: Lyra's hand finds his. Brief contact. Grounding. Partnership.
    if has_char_flag("Lyra", "lewd_scene_completed"):
        l "We've survived everything so far. Together. We'll survive this too."
        a "Together. Yeah. That's the only way any of this works."
        "Her hand in mine. Warm. Familiar. Comfort. We've been through too much to face things alone now. Whatever happens, we face it together. That's something. That's everything."
    else:
        # Light alignment flavor (no momentum change)
        if is_ob_hard:
            a "I'll handle it. Like I handle everything else."
            l "Ok."
        elif is_mid:
            l "We'll handle it. Like we handle everything. Together."
            a "Together. Best strategy we have."
        else:
            l "We'll handle it. Like we handle everything. Together."
            a "Together. Yeah. That's the only way any of this works."

    # VISUAL: Looking around established base. Two months of work visible. Success tangible.
    athought "Two months. Twelve people became twenty. Temp shelter became home. Fugitives became resistance. And now we're about to prove it. About to hit Echelon. About to show them we're dangerous. Glass became ash became ember. Now ember becomes fire. And fire burns everything."

    # VISUAL: Base continuing around them. People working. Living. Preparing. Resistance real.
    "Base functioning. People moving with purpose. This is what we built. Not just walls and security. Community. Team. Family. Resistance. From nothing. From twelve broken people. Now something real. Something dangerous. Something that matters. This is home. This is hope. This is war."

    # ---------------------------
    # NEWEST-SYSTEM STATE UPDATES
    # ---------------------------

    # Scene completion
    $ scene_done("base_established")

    # Canon / global flags
    $ flag_on("resistance_operational")
    $ flag_on("first_mission_approaching")

    # Persist base location choice (string value)
    $ world_set("base_location", base_location)

    # Relationships (light goodwill)
    $ rel_add("Lyra",   trust=+1)
    $ rel_add("Selene", trust=+1)
    $ rel_add("Noelle", trust=+1)
    $ rel_add("Tessa",  trust=+1)
    $ rel_add("Zira",   trust=+1) if has_char_flag("Zira", "kiss_happened") else None

    # Logs
    $ log_add("time_skip", "Two-month build complete; base functional; headcount ~20; routines established.")
    $ log_add("ops",       "Sector 9 depot raid set for T+3; roles: Noelle(data), Zira(intel), Lyra(tactics), Tessa(med).")
    $ log_add("theme",     "Shelter→home; survival→operations; leadership distributed; collective choice honored.")

    # OB/EMP taps (neutral routine)
    $ emp_add("Aeron", +1)
    $ ob_add("Aeron",  +1)

    $ snapshot("Aeron",
        context="base_established_two_months_later",
        emp_delta=1,
        ob_delta=1,
        note="Stabilizes via routine; accepts co-lead role. EMP: community belonging; OB: procedural clarity before first op."
    )

    # Global counters
    $ world_set("resistance_strength",        20)
    $ world_set("resistance_fighters_count",  20)

    return

    # canon_note: Scene 10 complete - base established after time skip
    # canon_note: Headcount +8 (12 → 20); routines & cover solid
    # canon_note: First mission planned (Sector 9 depot raid; T+3)
    # canon_note: Roles: Noelle(data), Zira(intel), Lyra(tactics), Tessa(med)
    # canon_note: Zira warmth waypoint if kiss happened (present, not escalated)
    # canon_note: Aeron co-decision voice acknowledged by Selene
    # canon_note: Theme: From fugitives to resistance; ash → ember → fire
