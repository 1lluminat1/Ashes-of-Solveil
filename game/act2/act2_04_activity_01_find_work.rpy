# act2_activity_01_find_work.rpy


# =======================================================
# ACT 2 - Activity 1: Find Work
# Helpers-only for scene/task tracking (scene_flags), relationships, reputation, skills, romance, etc.
# Inventory currency (scrip) is credited to inventory['scrip'] (no helper exists; noted in comments).
# OB/EMP flavor is minimal and additive; no removals of your text.
# =======================================================


define kren = Character("Kren", color="#8B7355")
define customer = Character("Customer", color="#9E9E9E")
define owner = Character("Repair Owner", color="#607D8B")
define smuggler = Character("Smuggler", color="#424242")
define gang = Character("Gang Member", color="#B71C1C")
define v = Character("Vika", color="#607D8B")
define rax = Character("Rax", color="#424242")


# Compatibility alias: if anything jumps to the legacy label
label activity_find_work:
    jump act2_activity_01_find_work


label act2_activity_01_find_work:

    $ mark_scene("act2_activity", "work_started")
    $ start_operation("op2A_work", note="Find Work (Sector 6 market)")

    # Track today's scrip delta for the summary line
    $ work_scrip_delta = 0

    # VISUAL: Lower Spans. Day. Sector 6 market district. Crowded. Alive. Chaotic.
    # LIGHTING: Natural light filtered through grates above. Neon signs. Smoky haze.
    # SOUND: Vendors calling out; haggling; machinery; life happening; survival economics.

    "{i}Day 2. Activity: Find Work.{/i}"
    a "{i}Zira said I need money. Scrip, not Aeries credits.{/i}"
    a "{i}Credits might work at some places, but scrip is what the Unders actually use.{/i}"

    # VISUAL: Aeron walking through market. Wearing Unders clothes (if Activity 6 done) or civilian wear.
    # People bustle past. Vendors hawking goods. Life compressed and vibrant.

    "{i}The market is chaos made economy. Everything's for sale. Everything's negotiable.{/i}"
    "{i}Food, tech, weapons, medicine, information. If you need it, someone's selling it.{/i}"
    "{i}And everyone's working. Because down here, you work or you starve.{/i}"

    a "{i}I need work. Something that pays. Something that doesn't ask questions.{/i}"
    a "{i}Zira said market stalls are always hiring. Manual labor. Loading. Repairs.{/i}"
    a "{i}Nothing glamorous. But I'm not Glass anymore. Glamour isn't an option.{/i}"

    # Light alignment flavor
    if get_empathy_band() == "obedience":
        a "{i}Pick the option with the cleanest risk-reward curve. Pay first. Everything else after.{/i}"
    elif get_empathy_band() == "empathy":
        a "{i}Maybe earning it clean matters. Maybe who I help matters too.{/i}"

    # VISUAL: Three options visible. Three different vendors needing help.
    # OPTION A: Food stall (heavy lifting, simple work)
    # OPTION B: Repair shop (technical work, more pay)
    # OPTION C: Smuggling run (risky, highest pay)

    menu:
        "Three vendors are hiring. Choose where to work:"

        "Food stall—Help vendor with heavy lifting and deliveries.":
            jump work_food_stall

        "Repair shop—Fix machinery and salvage tech.":
            jump work_repair_shop

        "Smuggling run—Transport 'goods' across sectors (risky).":
            jump work_smuggling_run


# =======================================================
# WORK OPTION A: FOOD STALL
# =======================================================
label work_food_stall:

    $ mark_scene("act2_activity", "work_path_food")

    "{i}Food stall. Owner looks exhausted. Crates piled high. Clearly needs help.{/i}"

    kren "You looking for work or just staring?"

    a "Work. Sign says you're hiring."
    kren "Depends. You strong? Reliable? Not gonna rob me the second I turn around?"

    a "Strong enough. Reliable enough. Not a thief."
    kren "(eyes narrow) You're new. Don't recognize your face."
    kren "Where you from?"

    menu:
        "How do you answer?"

        "Truth (partial)—'Moved here recently. Need work. That's all.'":
            $ kren_trust = 2
            $ aeron_honest = True
            $ adjust_empathy_once("work_food_honesty", +1)

            a "Moved here recently from... elsewhere. Need work. That's the situation."
            kren "(studies him) 'Elsewhere' doing a lot of heavy lifting in that sentence."
            kren "But you got honest eyes. Desperate eyes. I know desperate."
            kren "(sighs) Fine. 50 scrip for the day. Help me load deliveries and move crates."
            kren "You steal anything, I'll gut you myself. We clear?"

        "Deflect—'Does it matter? I need work, you need help.'":
            $ kren_trust = 1
            $ aeron_honest = False
            $ adjust_empathy_once("work_food_deflect", -1)

            a "Does my history matter? You need help, I need scrip. That's the transaction."
            kren "(frowns) Smart mouth. I don't like smart mouths."
            kren "But you're right. I'm desperate enough to hire anyone who isn't actively bleeding."
            kren "40 scrip for the day. You fuck up, I dock pay. Steal, I break fingers."
            kren "That's the deal. Take it or leave it."

    a "I'll take it. When do I start?"
    kren "Now. Grab that crate and follow me."

    "{i}The crate is heavier than it looks. Forty kilos at least.{/i}"
    "{i}I've carried weapons. I've carried bodies. But this is different.{/i}"
    "{i}This is survival. This is honest work. This is what being human means.{/i}"

    a "{i}Hours blend together. Lift. Carry. Stack. Repeat.{/i}"
    a "{i}My back aches. My hands blister. My legs scream.{/i}"
    a "{i}But I keep moving. Because this is what I chose.{/i}"

    kren "(hands water) You work hard. Didn't expect that from a newcomer."
    a "(drinks gratefully) Thanks. Needed this."
    kren "Where'd you learn to lift like that? Military?"

    a "Learned young. Necessity."
    kren "(nods) Fair enough. We all got histories we don't talk about."
    kren "Down here, past doesn't matter much. Just what you do today."

    a "{i}He doesn't ask more. Doesn't push. Just accepts.{/i}"
    a "{i}That's the Unders. Everyone's running from something.{/i}"

    kren "You're good at this. Better than the last three I hired."
    kren "They quit after an hour. Said it was too hard."
    kren "(grins) You got stamina. I respect that."

    a "Just doing the job."
    kren "Yeah, but most people don't. They do half the job and expect full pay."
    kren "You actually earn your keep. Rare quality down here."

    kren "50 scrip. Promised amount."
    kren "(adds extra note) And 10 more. Bonus. For not being useless."

    a "You don't have to—"
    kren "I don't do charity. You earned it. Take it."
    kren "(slight pause) You need work again, come back. I'll hire you."
    kren "Good workers are hard to find. Don't waste talent."

    a "{i}60 scrip. Earned through sweat and labor.{/i}"
    a "{i}Not orders. Not violence. Just work.{/i}"
    a "{i}It feels... clean. Like I'm washing off Glass one crate at a time.{/i}"

    a "Thank you. I'll remember that."
    kren "Don't thank me. Just show up if you come back."
    kren "(waves him off) Now get out of here. I'm closing up."

    # Rewards (helpers/state):
    $ work_scrip_delta = 60
    $ inventory["scrip"] = inventory.get("scrip", 0) + work_scrip_delta
    $ inc_rep("unders", +2)
    $ char_note("Lyra", "Kren (Sector 6) – reliable food-stall owner; offered recurring work.")
    $ mark_scene("act2_activity", "work_food_paid")

    jump work_complete


# =======================================================
# WORK OPTION B: REPAIR SHOP
# =======================================================
label work_repair_shop:

    $ mark_scene("act2_activity", "work_path_repair")

    "{i}Repair shop. Machines piled high. Everything broken. Everything salvageable.{/i}"

    a "Sign says you're hiring."
    v "(not looking up) Can you solder? Do you know circuit architecture? Can you identify pre-Collapse tech?"

    a "I can solder. Basic circuit knowledge. Some tech identification."
    v "(finally looks up) Military training?"

    a "Why do you ask?"
    v "Because your posture screams 'I was trained to kill' and your hands have calluses from weapon grips, not tools."
    v "I'm not judging. Just observing. Lots of ex-military down here."
    v "(back to work) Can you follow instructions and not blow up my shop?"

    a "Yes to both."
    v "70 scrip for the day. You break something expensive, I dock pay."
    v "Help me repair these salvaged units. We're behind schedule."

    a "{i}I know weapons. I know combat systems. But civilian tech?{/i}"
    a "{i}This is going to be harder than lifting crates.{/i}"

    "{i}Hours of delicate work. Circuit boards. Wiring. Components.{/i}"
    "{i}Vika's patient but exacting. No mistakes allowed.{/i}"

    a "{i}I learned fast. Military precision helps. But this is creation, not destruction.{/i}"

    v "Not bad. You learn quick."
    v "Most people I hire burn themselves out in the first hour."
    v "You've got steady hands. Good for this work."

    a "Steady hands come from training."
    v "Military sniper training, I'd guess. But you're not sniping anymore."
    v "(doesn't push) Whatever you're running from, you're useful here."

    "{i}She doesn't ask. Doesn't judge. Just works beside me.{/i}"
    "{i}That's respect. Real respect. Earned through competence.{/i}"

    v "You're good at this. Really good. Better than me at your age."
    v "If you want steady work, I'll hire you regularly. 70 scrip per day."
    v "I need someone reliable. You seem reliable."

    a "I'll consider it. Thank you."
    v "(hands him scrip) 70 as promised. You earned it."
    v "And here— (hands small tool) Precision soldering iron. Yours. You'll need it."

    a "I can't take this—"
    v "You can and you will. Can't have my worker using shit tools."
    v "Consider it an investment. Come back, that tool pays for itself."

    a "{i}A tool. Given freely. Because she values my work.{/i}"
    a "{i}Not weapons. Not violence. Tools for building.{/i}"
    a "{i}Maybe I can be more than Glass. Maybe I can create instead of destroy.{/i}"

    # Rewards (helpers/state):
    $ work_scrip_delta = 70
    $ inventory["scrip"] = inventory.get("scrip", 0) + work_scrip_delta
    $ grant_tool("precision_soldering_iron")
    $ learn_skill("basic_repair")
    $ inc_rep("unders", +1)
    $ char_note("Lyra", "Vika (Sector 6) – exacting repair tech; offered steady work; gave precision iron.")
    $ mark_scene("act2_activity", "work_repair_paid")

    jump work_complete


# =======================================================
# WORK OPTION C: SMUGGLING RUN
# =======================================================
label work_smuggling_run:

    $ mark_scene("act2_activity", "work_path_smuggle")

    "{i}Smuggling run. The riskiest option. The highest pay.{/i}"
    "{i}Rax doesn't look trustworthy. But I need money.{/i}"

    rax "You looking for easy money or real money?"
    a "What's the difference?"
    rax "Easy money is safe and small. Real money is dangerous and big."
    rax "I've got a package. Needs to get from Sector 6 to Sector 4. Echelon's watching the route."
    rax "100 scrip if you make the run without getting caught."

    a "What's in the package?"
    rax "Doesn't matter. You're courier, not inspector."
    rax "You get caught, you don't know me. You don't mention me. You take the fall alone."
    rax "That's the deal. Take it or leave it."

    # OB/EMP nudge
    if get_empathy_band() == "obedience":
        a "{i}Risk, pay, exposure. Calculate the margin. Take the hit if the ROI holds.{/i}"
    else:
        a "{i}This isn't clean. But scrip buys medicine and time.{/i}"

    menu:
        "Accept the smuggling run?"

        "Accept—Take the risk for the money.":
            $ mark_scene("act2_activity", "work_smuggle_accept")
            jump smuggling_run_gameplay

        "Decline—Too risky, find safer work.":
            $ mark_scene("act2_activity", "work_smuggle_decline")
            a "Too risky. I'll find work elsewhere."
            rax "(shrugs) Your loss. More for someone else."
            "{i}I leave. Safer options exist. Not worth the risk yet.{/i}"
            $ work_scrip_delta = 0
            jump work_complete  # Return to hub via standard exit


label smuggling_run_gameplay:

    rax "Smart choice. Here's the package. Don't open it. Don't drop it."
    rax "Route's marked on this map. Avoid main streets. Echelon patrols every 15 minutes."
    rax "Deliver to contact at this address. He'll pay you. I get my cut later."

    "{i}The package feels dense. Could be tech. Could be drugs. Could be worse.{/i}"
    "{i}I don't ask. Courier doesn't ask.{/i}"

    "{i}I move through alleys. Staying low. Staying quiet.{/i}"
    "{i}Echelon patrol passes. Twenty meters away. I hold breath.{/i}"

    menu:
        "Echelon patrol approaching. How do you avoid them?"

        "Hide behind dumpster—Wait for them to pass.":
            "{i}I duck behind dumpster. Hold still. Patrol passes.{/i}"
            "{i}Close. Too close. But I'm safe.{/i}"
            $ stealth_success = True

        "Sprint across opening—Risk it to save time.":
            "{i}I sprint. Fast. Quiet as possible.{/i}"
            "{i}Patrol turns. Sees movement. Shouts.{/i}"
            "{i}FUCK. Run. RUN.{/i}"
            $ stealth_success = False

    if stealth_success:
        "{i}I make it to delivery point. No detection. Clean run.{/i}"

        contact "Clean run. Impressive. Here's your 100 scrip."
        contact "Rax will be pleased. You need more work, come find us."

        $ work_scrip_delta = 100
        $ inventory["scrip"] = inventory.get("scrip", 0) + work_scrip_delta
        $ inc_rep("unders", +1)
        $ char_note("Lyra", "Rax (shadows) – smuggling contact; paid 100 scrip for clean courier run.")
        $ mark_scene("act2_activity", "work_smuggle_paid")

        "{i}100 scrip. Risky but successful. Highest pay I've earned.{/i}"
        "{i}But it feels dirty. This isn't honest work. This is survival.{/i}"
        "{i}Still... money is money. And I need it.{/i}"

    else:
        "{i}Patrol chases. I drop package to run faster.{/i}"
        "{i}Escape through maintenance tunnels. Lose them.{/i}"
        "{i}But package is gone. Mission failed.{/i}"

        rax "You lost the package?!"
        a "Had to. Patrol was on me. It was the package or capture."
        rax "Useless. Get out of here. No pay. No second chances."

        $ work_scrip_delta = 0
        $ inc_rep("unders", -1)
        $ mark_scene("act2_activity", "work_smuggle_failed")
        $ add_team_suspicion(1)

        "{i}No pay. Reputation damaged. Lesson learned.{/i}"
        "{i}Smuggling isn't as easy as it looks. Risk isn't always worth reward.{/i}"

    jump work_complete


# =======================================================
# WORK COMPLETE - RETURN TO HUB
# =======================================================
label work_complete:

    # TRANSITION: Return to safe house. Day ending. Work complete.
    scene bg_safe_house with fade

    # VISUAL: Zira waiting. Curious about how work went.
    z "How'd it go? Make any money?"
    a "Yeah. Earned [work_scrip_delta] scrip today."
    z "Not bad for your first day working like a normal person."
    z "(grins) How's it feel? Honest labor?"

    a "Exhausting. Humbling. Different from anything I've done."
    z "That's called being human. Welcome to it."
    z "Get some rest. Tomorrow's another day of survival."

    # REWARDS SUMMARY SCREEN (textual; no UI widget here):
    "{b}Activity Complete: Find Work{/b}"
    "
    Rewards:
    - Scrip Earned: [+[work_scrip_delta]]
    - Contacts/Notes: check Journal
    - Reputation: (varies)
    - Experience: Manual labor, Unders economy, survival basics

    You now understand how the Unders economy functions.
    You can work again for additional income if needed.
    Scrip can be used to purchase items, bribe contacts, or trade favors.
    "

    # Mark core task completion and return to hub
    $ work_scrip_delta = 0
    $ mark_scene("act2_activity", "work_done")
    $ summary = end_operation("op2A_work", tag="Find Work (Sector 6)")
    $ log_line(summary)
    jump act2_activity_hub

    # Hub already decremented days_remaining and set last_activity.
    jump act2_activity_hub
