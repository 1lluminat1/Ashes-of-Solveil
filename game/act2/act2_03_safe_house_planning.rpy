# act2_03_safe_house_planning.rpy
# =======================================================
# ACT 2 - Scene 3: Safe House Planning (HUB)
# OB/EMP integrated; Consolidated State Architecture hooks
# Adds randomized pre/post activity flavor + event-specific quips
# Uses helpers only + scene_flags for all scene/task tracking
# =======================================================

label act2_safe_house_planning:

    # --- SCENE INIT / SNAPSHOT ---
    $ start_operation("op203_safehouse_hub", note="Safehouse planning + 7-task hub intro")
    $ mark_scene("act2_03_safe_house_planning", "started")
    $ log_line("ACT2_03 started: Safe House Planning (Hub)")

    # VISUAL: Safe house. Morning light through barred window. Day 2.
    # LIGHTING: Dim gray dawn filtering in. Single bulb still on. Cold.
    # SOUND: City waking up below; distant machinery; footsteps in hallway.

    "{i}Day 2.{/i}"

    # VISUAL: Aeron wakes on concrete floor. Body stiff. Lyra already awake, staring at wall.
    # Both look like hell. Dark circles. Exhaustion. Trauma settling into bones.

    "{i}Morning. If you can call it that. Concrete floor leaves you cold and aching, mind worse than the body.{/i}"
    "{i}Lyra's already awake, staring at nothing. Her hand moves to her Band in that automatic way she can't seem to stop.{/i}"

    a "{i}Day 2 in the Unders. Still alive. That has to count for something.{/i}"

    # VISUAL: Lyra glances at him. Nods. No words. What is there to say?
    l "(quiet) Did you sleep?"
    a "Some. You?"
    l "Not really."
    a "Nightmares?"
    l "Memories. Same thing at this point."

    # SOUND: Door lock beeping. Both tense immediately. Hands move toward weapons they don't have.
    "{i}The lock beeps. They freeze, hands moving instinctively toward weapons that aren't there.{/i}"
    "{i}Still defenseless. Still terrified every time that door opens.{/i}"

    # VISUAL: Door opens. Zira enters. Arms full of supplies again. Looks tired but alert.
    z "Morning, fugitives. Still breathing, so that's a good start."

    # VISUAL: She drops supplies. Food packets, water, something wrapped in cloth.
    # SOUND: Packages hitting floor. Rustling. Practical.

    z "Breakfast—protein bars and water. Not fancy, but it'll keep you functional."
    a "You didn't have to—"
    z "I did, actually. You two look like corpses and I can't have you dying before the fun starts."

    # VISUAL: She sits cross-legged. Same comfortable confidence. Owns this space.
    z "Alright, reality check part two. You listening?"
    l "We're listening."
    z "Good. What I'm about to say determines whether you survive the week."

    # VISUAL: She pulls out small datapad. Lists. Notes. Plans.
    z "You can't just hide in here forever. Echelon's hunting and locals are getting suspicious. Word spreads fast down here—two Echelon operatives vanished right after the Purge."
    z "People connect dots fast in the Unders. You need cover."

    a "The fake IDs—"
    z "Are paper thin. IDs get you past casual inspection, sure. But actual survival? That requires integration. Reputation. Proof you belong here."
    z "Right now you're obvious outsiders. That makes you targets."

    l "What do we do?"
    z "You work. You blend in. You earn your place one interaction at a time."
    z "The Unders run on barter, favors, and reputation. You have exactly none of those things."
    z "So you build them. One day at a time."

    # VISUAL: She swipes through datapad. Shows them list.
    z "I've identified seven things you need to survive down here. Call them priorities. You've got about a week before Selene decides whether she'll even meet you."
    z "Use that week to prove you're serious. Prove you're not just Echelon trash hiding in a hole."

    a "What are the seven things?"

    # VISUAL: Zira leans forward. Direct. Practical. No room for negotiation.
    z "First: work. You need money—real money. Scrip that actually spends down here, not your useless Aeries credits."
    z "Your Echelon funds might work if you find the right black market dealers. But finding them means exposure. Better to earn clean."

    z "Second: weapons. You're completely unarmed right now. That's suicide in the Unders. Knife minimum, gun if you can manage it. Something to defend yourselves with."
    z "Everyone else down here is armed and they won't hesitate to use them."

    z "Third: intel. You need to know Echelon's movements and patrol patterns if you want to stay ahead of them."
    z "I have a contact—info broker. Brilliant but weird. She might help if you don't piss her off."

    z "Fourth: medical supplies. People get hurt down here constantly. You want reputation? Save someone's life. Heal someone's kid."
    z "There's an underground clinic with a medic who might help. Or might spit in your face considering Glass's reputation."

    z "Fifth: reputation itself. Do something good. Help someone. Change how people see you."
    z "Locals hate you right now. Change that one person at a time. Escort an elder, protect a vendor—small things that add up."

    z "Sixth: survival skills. You don't know the Unders. The culture, the signals, the territories. I'll teach you. Not because I'm nice, but because you're useless to anyone otherwise."

    z "Seventh: confront your past. Sector 10. The Sweep. You need to face it. There's a survivor out there—someone who remembers, someone who lost everything."
    z "Talk to them. Apologize, listen, whatever it takes. Selene will ask, and if you haven't done it she'll know you're not serious."

    # VISUAL: Both process. Seven tasks. One week. Overwhelming.
    l "That's... a lot."
    z "That's survival. You wanted to fight Echelon? This is step one. You can't fight an empire from a concrete box."
    z "You need allies, resources, skills, trust. None of that comes free."

    a "What about Selene? You said she's considering."
    z "She is. Barely. I told her about the Sweep and the 200 you saved. She didn't shoot the messenger, so that's progress."
    z "But she lost most of her cell in the Purge. Sector 10 was her territory. You swept Sector 10, which means you killed her people."
    z "So yeah, she's considering. Considering whether to meet you or just put a bullet in your head the moment she sees you."

    l "Will she help us?"
    z "Depends. Do these seven things. Prove you're not just hiding. Prove you're willing to work, to change, to actually earn it."
    z "Then maybe she gives you a chance. Or maybe she kills you anyway. Honestly could go either way."

    # VISUAL: Zira stands. Stretches. Ready to leave again.
    z "You've got one week. Seven days, seven tasks. Do them in whatever order you want—I don't care. But get them done. All of them."
    z "Because when Selene agrees to meet, you better have something to show for this week."

    a "Where do we start?"
    z "That's up to you. You're adults. Figure it out."
    z "Just don't do anything stupid. Which, given your track record, is probably a lot to ask."

    # VISUAL: She moves to door. Pauses. Looks back.
    z "I'll check in and leave messages when I can. Help where it makes sense. But I can't babysit. I have my own work, my own problems."
    z "You're on your own most of the time. Get used to it."

    l "Zira. Why are you doing this?"
    z "(pauses) Because someone should. And nobody else will."
    z "And because... I want to see if Glass can become something else. Call it curiosity, call it hope, call it stupidity."
    z "Either way, don't waste it."

    # VISUAL: She leaves. Door closes. Lock engages. Alone again.
    "{i}Gone again. Leaving them with seven impossible tasks and one week to complete them.{/i}"
    "{i}Everything rides on this. Every single thing.{/i}"

    # VISUAL: Both sit. Looking at each other. Overwhelmed but determined.
    l "Seven tasks."
    a "Seven days."
    l "Where do we even start?"
    a "...I don't know. But we have to start somewhere."

    # VISUAL: Aeron stands. Looks at door. The city beyond. Terrifying and necessary.
    a "{i}One week to prove we're worth keeping alive. One week to build something from nothing.{/i}"
    a "{i}Seven tasks. Every single one could kill us.{/i}"

    l "(stands beside him) We do this together. Like everything else."
    a "Together. Yeah."
    l "What's first?"

    # VISUAL: Aeron looks at her. Both broken. Both scared. Both committed.
    a "We figure out who Kade Voss is. Who Mira Chen is. We go out there, we survive, we earn it."
    l "One day at a time."
    a "One day at a time."

    # --- HUB STATE INIT (helpers + scene_flags only) ---
    python:
        # Track remaining days (allowed outside characters/scenes)
        if player_state.get("days_remaining", None) is None:
            player_state["days_remaining"] = 7
        if "last_activity" not in player_state:
            player_state["last_activity"] = ""

        # Seed a canonical set of task keys in a local list (not saved in dicts)
        store._a2_tasks = ["work","weapons","intel","medical","reputation","survival","past"]
        # Ensure a scene_flags bucket exists for hub flavor (no-op: mark_scene builds lazily)
        # Nothing to mark here yet.

    jump act2_activity_hub


# ==========================
# HUB LOOP
# ==========================
label act2_activity_hub:

    # Determine progress from scene_flags only
    python:
        done_count = 0
        for t in _a2_tasks:
            if check_scene_flag("act2_activity", f"{t}_done"):
                done_count += 1
        activities_remaining = len(_a2_tasks) - done_count
        current_day = 2 + done_count

    if done_count > 0:
        "{i}Day [current_day]. Another day, another task to complete.{/i}"
        "{i}Still alive. Still moving forward. That has to mean something.{/i}"
    else:
        "{i}Day 2. The first step into this new life. Choose carefully.{/i}"

    # --- POST-ACTIVITY EVENT-SPECIFIC FLAVOR (fires once per task) ---
    python:
        last_task = player_state.get("last_activity", "")
        flavor_key = f"flavor_once_{last_task}" if last_task else ""
        if last_task and not check_scene_flag("act2_activity", flavor_key):
            flavor_once = {
                "weapons": [
                    ("z", "If Vex smiles at you, check your pockets and your pulse."),
                    ("l", "I still can't believe we got that gun from Vex."),
                    ("a", "{i}Weight on the hip. Not comfort. Responsibility.{/i}")
                ],
                "work": [
                    ("z", "Scrip spends. Your faces don’t. Wear the faces that do."),
                    ("l", "I forgot how much I hate grease under my nails."),
                    ("a", "{i}Honest work. Feels strange after years of lies.{/i}")
                ],
                "intel": [
                    ("z", "If Noelle says ‘curious’, you run. Or you sit. Depends on her tea."),
                    ("a", "{i}Patterns emerge where cruelty grows lazy.{/i}")
                ],
                "medical": [
                    ("z", "Tessa doesn’t do miracles. She does math with blood."),
                    ("l", "That kid’s breathing sounded like glass."),
                    ("a", "{i}Mercy is heavier than steel. It leaves a mark.{/i}")
                ],
                "reputation": [
                    ("z", "One neighbor talks. Then two. Make them say the right things."),
                    ("l", "They looked at us like we were human. For a moment.")
                ],
                "survival": [
                    ("z", "Lesson one: eyes up, hands empty, path mapped."),
                    ("a", "{i}Signals and chalk. The Unders write in ghosts.{/i}")
                ],
                "past": [
                    ("l", "Sector 10 still smells like burned air."),
                    ("a", "{i}Apology is a door. Doesn’t open itself.{/i}")
                ]
            }
            pool = flavor_once.get(last_task, [])
            # Deterministic pick: 2 lines for EMP band, 1 for OB band
            max_lines = 2 if get_empathy_band() != "obedience" else 1
            for i, (who, line) in enumerate(pool):
                if i >= max_lines:
                    break
                renpy.say(eval(who), line)
            # Mark once via scene_flags
            mark_scene("act2_activity", flavor_key)

    # --- OPTIONAL RANDOMIZED PRE-ACTIVITY FLAVOR ---
    python:
        import renpy
        pre_emp = [
            ("l", "We can’t fix everything today, but we can fix something."),
            ("a", "{i}Pick the wound you can stitch.{/i}")
        ]
        pre_ob = [
            ("a", "{i}Start with the task that bleeds least time.{/i}"),
            ("z", "Don’t overthink it. Over-prep it.")
        ]
        pre_pool = pre_emp if get_empathy_band() != "obedience" else pre_ob
        if renpy.random.random() < 0.5:
            who, line = renpy.random.choice(pre_pool)
            renpy.say(eval(who), line)

    # LYRA SCENE CHECK
    call act2_check_lyra_scene_hub from _hub_lyra_gate

label act2_continue_hub:

    # Recompute using flags
    python:
        done_count = 0
        for t in _a2_tasks:
            if check_scene_flag("act2_activity", f"{t}_done"):
                done_count += 1
        activities_remaining = len(_a2_tasks) - done_count
        current_day = 2 + done_count

    if activities_remaining > 0:
        "{i}[activities_remaining] tasks remaining before Selene decides our fate.{/i}"

        menu:
            "What should we focus on today?":

            "Find Work - Earn scrip, establish cover" if not check_scene_flag("act2_activity","work_done"):
                $ mark_scene("act2_activity","work_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "work"
                jump act2_activity_01_find_work

            "Acquire Weapons - Get armed, black market contact" if not check_scene_flag("act2_activity","weapons_done"):
                $ mark_scene("act2_activity","weapons_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "weapons"
                jump act2_activity_02_acquire_weapons

            "Gather Intel - Meet info broker, learn patrol patterns" if not check_scene_flag("act2_activity","intel_done"):
                $ mark_scene("act2_activity","intel_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "intel"
                jump act2_activity_03_gather_intel

            "Medical Supplies - Underground clinic, prove worth" if not check_scene_flag("act2_activity","medical_done"):
                $ mark_scene("act2_activity","medical_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "medical"
                jump act2_activity_04_medical_supplies

            "Earn Reputation - Help locals, change perceptions" if not check_scene_flag("act2_activity","reputation_done"):
                $ mark_scene("act2_activity","reputation_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "reputation"
                jump act2_activity_05_earn_reputation

            "Survival Skills - Learn the Unders with Zira" if not check_scene_flag("act2_activity","survival_done"):
                $ mark_scene("act2_activity","survival_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "survival"
                jump act2_activity_06_survival_skills

            "Confront the Past - Return to Sector 10, face survivor" if not check_scene_flag("act2_activity","past_done"):
                $ mark_scene("act2_activity","past_done")
                $ player_state["days_remaining"] = max(0, player_state["days_remaining"] - 1)
                $ player_state["last_activity"] = "past"
                jump act2_activity_07_confront_past

    else:
        "{i}Seven days. Seven tasks. All completed, every single one of them.{/i}"
        "{i}Time to see if it was enough to earn Selene's attention.{/i}"
        $ mark_scene("act2_03_safe_house_planning", "all_tasks_completed")
        $ summary = end_operation("op203_safehouse_hub", tag="Safehouse Hub (All tasks done)")
        $ log_line(summary)
        return


# ==========================
# LYRA GATE (helpers-only)
# ==========================
label act2_check_lyra_scene_hub:

    # Helper reads (add these getters in your state system if not present)
    $ lyra_trust = get_trust("Lyra")
    $ lyra_aff   = get_affection("Lyra")

    if char_flag_has("Lyra", "lewd_scene_completed"):
        jump act2_continue_hub

    if lyra_trust >= 7 and lyra_aff >= 5:
        $ mark_flag("Lyra", "lewd_scene_unlocked")

        # VISUAL: Safe house. Evening. Both exhausted from the day. Quiet moment.
        # LIGHTING: Dim. Single light. Intimate space.
        # SOUND: City quiet below. Their breathing. Silence comfortable.

        "{i}Evening. Quiet. Just the two of us in this small space. Something's different tonight.{/i}"

        # VISUAL: Lyra looking at him. Different energy. Vulnerable. Open.
        l "Aeron."
        a "Yeah?"
        l "Can we... can we just sit for a while? Not planning. Not surviving. Just... being."
        a "...Yeah. We can do that."

        # VISUAL: They sit. Close. Not touching yet. But proximity different.
        "{i}She sits close. Closer than usual. Not accidental. Intentional. Something unspoken between us.{/i}"

        menu:
            "The space between them feels charged. Different. Significant.":

            "Spend the evening with Lyra":
                # Inside act2_lyra_intimate_scene, remember to:
                #   $ mark_flag("Lyra", "lewd_scene_completed")
                #   $ rel("Lyra", trust=..., affection=...)  # if applicable
                jump act2_lyra_intimate_scene

            "Give her space - rest instead":
                a "Actually... I should probably get some rest. Long day."
                l "(slight disappointment) Oh. Yeah. Of course. Rest is important."
                l "Goodnight, Aeron."
                a "Goodnight, Lyra."
                "{i}The moment passes. Maybe it was nothing. Maybe it was everything. Too late to know now.{/i}"
                jump act2_continue_hub
    else:
        jump act2_continue_hub
