# =======================================================
# ACT 2 - Scene 16: Finding Home
# File: act2_16_finding_home.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_16_finding_home"
$ scene_mark(_current_scene_id, "entered")

label act2_16_finding_home:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Group shot around planning table. Individual shots for each LI's pitch. Push-in on Aeron during the decision moment.
    # LIGHTING: Selene's command post amber/ember. Each LI's proposal could have subtle color shifts matching their aesthetic.
    # SFX: Loop — command post ambient, map rustling, distant generator. One-shots — holographic display transitions, each location's signature sound.
    # FX/COMP: Holographic display showing each base location in turn—Cathedral ruins (warm gold), relay station (electric blue), data vault (silver), clinic (green/amber).
    # BLOCKING/PROPS: Selene's command post. Central holo-table. All core cast present: Selene, Aeron, Lyra, Zira, Noelle, Tessa.
    # FACE: Each LI animated when presenting their choice. Selene weighing options. Aeron processing the weight of the decision.

    # ========== SELENE'S COMMAND POST — DAY 8 ==========

    "The command post is crowded for the first time."

    "Everyone Aeron has met in the Unders, gathered around Selene's map table. The rebellion's inner circle, such as it is."

    # VISUAL: Group shot—Selene at the head, Aeron and Lyra, Zira, Noelle, Tessa. All watching the holo-display.
    "Selene stands at the head, gloved hands resting on the table. Her mother's leather catching the ember light."

    "Lyra is at Aeron's side—closer than she used to stand. Zira leans against the wall, arms crossed. Noelle has a tablet, taking notes. Tessa arrived last, still carrying the smell of antiseptic from the clinic."

    sel "The depot operation proved we can hit Echelon. But we can't keep operating from scattered safehouses."
    sel "We need a base. Permanent. Defensible. Central enough to coordinate, hidden enough to survive."

    "She pulls up the holographic display. Four locations marked on the Unders map."

    sel "Noelle and Zira have identified four candidates. Each has advantages. Each has risks."
    sel "I want input before I decide."

    "Her eyes sweep the room. Landing, for a moment, on Aeron."

    sel "All input."

    # ========== THE FOUR OPTIONS ==========

    sel "First option."

    # --- LYRA'S CHOICE: THE CATHEDRAL RUINS ---
    # VISUAL: Hologram shifts to show ruins of a sub-level cathedral. Warm gold lighting in the render.
    "The display shifts to show a structure Aeron doesn't recognize—arched ceilings, collapsed stonework, the remnants of something that was once beautiful."

    l "The Cathedral of the Lower Resonance."

    "Lyra's voice is quiet. Reverent."

    l "It was a branch of the Order of Saint Solenne, before Echelon consolidated the faith institutions."
    l "They abandoned it decades ago when the lower tiers were deprioritized. But the structure is sound."

    n "Confirmed. The foundation predates Echelon's construction records. Pre-collapse architecture, built to last."

    l "It has natural acoustics that disrupt standard surveillance frequencies. The old priests designed it that way—they believed the divine hum needed protection from interference."
    l "And there's space. Chambers, storage, a central hall that could hold a hundred people."

    sel "Risks?"

    n "Single primary entrance. If discovered, extraction would be difficult."
    n "Also, the location carries... symbolic weight. Echelon may monitor it for exactly that reason."

    l "They abandoned it. They don't think anyone remembers what it meant."

    "Her hand goes to her pendant. The cracked Core shard."

    l "But I remember."

    # --- ZIRA'S CHOICE: THE RELAY STATION ---
    # VISUAL: Hologram shifts to show an old transit relay station. Electric blue lighting, cables everywhere.
    sel "Second option."

    z "Relay Station Sigma-7."

    "The display shows a cramped space filled with old transit infrastructure—cables, junction boxes, the skeleton of a communication hub."

    z "Old transit authority relay. Part of the original Ghostline backbone before I had to reroute everything."
    z "It's ugly, cramped, and smells like burnt copper. But it's got direct access to six different Ghostline nodes."

    n "Communication advantage is significant. We could monitor seventy percent of Unders traffic from that position."

    z "And if things go wrong, there are eleven different exit routes. I've mapped all of them personally."
    z "Echelon doesn't know most of them exist. The transit authority records were corrupted in the '47 data purge."

    sel "Risks?"

    n "Structural integrity is questionable. The station wasn't maintained after decommission."
    n "Also, living conditions would be... austere."

    z "I've lived in worse. We all have."

    "She glances at Aeron."

    z "Some of us more recently than others."

    # --- NOELLE'S CHOICE: THE DATA VAULT ---
    # VISUAL: Hologram shifts to show a sealed underground chamber. Silver-blue lighting, geometric precision.
    sel "Third option."

    n "Archive Vault Delta-9."

    "The display shows a space unlike the others—clean lines, sealed doors, the architecture of deliberate purpose."

    n "Former Cognitive Division remote backup facility. Decommissioned when they centralized data storage in the Aeries."
    n "The infrastructure is still intact. Climate control, power systems, secure access protocols."

    z "And you just happened to know about a secret Cognitive Division facility?"

    n "I worked there. Briefly. Before my defection."

    "Silence."

    n "The facility has one significant advantage: Echelon believes it was destroyed."
    n "I falsified the decommission report myself. As far as their records show, it was demolished three years ago."

    sel "You're suggesting we operate from a location you personally erased from Echelon's knowledge."

    n "Yes."
    n "It's the most secure option from a data perspective. They can't search for what they don't know exists."

    sel "Risks?"

    n "If they ever discover the falsification, they'll know exactly where to look."
    n "Also, I have... personal associations with the location. I'm uncertain how that will affect my operational clarity."

    z "(quietly) Translation: it's where she started questioning everything.

    n "...That's not inaccurate."

    # --- TESSA'S CHOICE: THE CLINIC COMPLEX ---
    # VISUAL: Hologram shifts to show an abandoned medical facility. Green and amber lighting, sense of care.
    sel "Fourth option."

    t "The Mercy Ward."

    "Tessa speaks for the first time. Her voice is steady but carries weight."

    t "It was a triage center during the containment blackouts. Before Echelon decided the lower tiers weren't worth saving."
    t "They sealed it when the funding dried up. Left the equipment, the beds, everything."

    n "Medical infrastructure is a significant asset. We've been operating with limited supplies."

    t "It's more than that."
    t "The Mercy Ward was built to save people. The walls remember that, even if Echelon forgot."
    t "If we're going to build something real—not just a hiding place, but a community—we should build it somewhere that was designed for healing."

    sel "Risks?"

    n "The location is known to Unders residents. Former patients, families of the deceased."
    n "Some may welcome us. Others may see it as desecration."

    t "Or they might see it as resurrection."

    "She meets Selene's eyes. Steady."

    t "We're not just fighting Echelon. We're fighting for what comes after."
    t "A clinic says something different than a bunker."

    # ========== THE DECISION ==========

    "Selene looks at the four options. The four philosophies they represent."

    sel "Faith. Mobility. Security. Compassion."
    sel "Four different visions of what we're building."

    "She turns to Aeron."

    sel "You've been quiet, Captain. You're the one Marcus is hunting hardest."
    sel "Where do you want to make your stand?"

    "The weight of the question settles on him. Four choices. Four futures."

    athought "Each of them put something of themselves into their recommendation."
    athought "Whatever I choose, I'm choosing whose vision matters most."

    # --- PLAYER CHOICE: Base Selection ---
    menu:
        "Four locations. Four philosophies. Where does the rebellion make its home?"

        "The Cathedral Ruins — Lyra's choice.":
            $ record_choice_once(
                _current_scene_id, "_chose_cathedral",
                note="Player chose Lyra's Cathedral base. Faith and history."
            )
            $ scene_mark(_current_scene_id, "base_cathedral")
            $ STATE["world"]["base_location"] = "cathedral"

            a "The Cathedral."

            "Lyra's breath catches. She didn't expect him to choose hers."

            a "We're not just hiding from Echelon. We're building something they tried to destroy."
            a "The Cathedral is a statement. It says we remember what they erased."

            sel "(nodding slowly) Symbolic value has tactical applications. Morale, recruitment, narrative."

            l "(quiet) It means something. To me."

            a "I know. That's part of why."

            sel "The Cathedral it is. Zira, I want exit routes mapped within forty-eight hours."
            sel "Noelle, surveillance analysis. Tessa, inventory the medical supplies we can move."
            sel "We have a home now. Let's make it defensible."

            $ rel_bump("Lyra", trust=1, affection=1)
            $ npc_remember("Lyra", "aeron_chose_her_base", tone="moved")

        "Relay Station Sigma-7 — Zira's choice.":
            $ record_choice_once(
                _current_scene_id, "_chose_relay",
                note="Player chose Zira's Relay Station. Mobility and communication."
            )
            $ scene_mark(_current_scene_id, "base_relay")
            $ STATE["world"]["base_location"] = "relay"

            a "The relay station."

            z "(grinning) Finally, someone with sense."

            a "Communication is survival. If Marcus comes for us, we need to see him first and run faster."
            a "The Cathedral is beautiful, but beautiful doesn't keep us alive."
            a "The relay keeps us connected. That's worth more than symbolism."

            sel "Practical. I approve."
            sel "Zira, it's your territory. I want full operational security within seventy-two hours."
            sel "Noelle, integrate your adaptive framework with the relay's systems."

            z "(to Aeron, quieter) Thanks for trusting my instincts."

            a "You've earned it."

            $ rel_bump("Zira", trust=1, affection=1)
            $ npc_remember("Zira", "aeron_chose_her_base", tone="pleased")

        "Archive Vault Delta-9 — Noelle's choice.":
            $ record_choice_once(
                _current_scene_id, "_chose_vault",
                note="Player chose Noelle's Data Vault. Security and intelligence."
            )
            $ scene_mark(_current_scene_id, "base_vault")
            $ STATE["world"]["base_location"] = "vault"

            a "The archive vault."

            n "(surprised) You're trusting my falsified records?"

            a "I'm trusting you."
            a "You erased that facility because you knew someday it might matter."
            a "Whether you knew it then or not, you were already fighting back."
            a "Now we finish what you started."

            "Noelle's hand goes to the data crystal on her wrist. The fragment of truth."

            n "I... thank you. That's... unexpected."

            sel "Security has value. If Echelon can't find us, they can't kill us."
            sel "Noelle, you'll lead the reactivation. Zira, I want backup communication routes."

            n "(to Aeron, very quietly) I won't let you down.

            $ rel_bump("Noelle", trust=1, affection=1)
            $ npc_remember("Noelle", "aeron_chose_her_base", tone="touched")

        "The Mercy Ward — Tessa's choice.":
            $ record_choice_once(
                _current_scene_id, "_chose_clinic",
                note="Player chose Tessa's Clinic. Compassion and healing."
            )
            $ scene_mark(_current_scene_id, "base_clinic")
            $ STATE["world"]["base_location"] = "clinic"

            a "The Mercy Ward."

            t "(soft) Really?"

            a "Tessa's right. We're not just fighting—we're building."
            a "A clinic says we're here to help people, not just hurt Echelon."
            a "And practically speaking, medical infrastructure could be the difference between losing fighters and keeping them."

            sel "Compassion as strategy. It's not how I usually think, but..."
            sel "There's logic to it. Hearts matter as much as weapons in a long war."

            t "I can have it operational within a week. I know what equipment we need, what we can salvage."

            sel "Do it. Zira, security assessment. Noelle, community outreach mapping—who knows about this place and how they'll react."

            t "(to Aeron, as others start planning) You didn't have to do that.

            a "Yes, I did. You're the one who's been keeping people alive down here."
            a "It's about time someone built you a proper place to do it."

            $ rel_bump("Tessa", trust=1, affection=1)
            $ npc_remember("Tessa", "aeron_chose_her_base", tone="grateful")

    # ========== CLOSING — A HOME ==========

    "The planning begins immediately. Selene assigning roles, the others moving to their tasks."

    "For the first time, the resistance feels like it might become something permanent."

    sel "(to Aeron, as others work) You chose quickly."

    a "I knew what mattered."

    sel "And what's that?"

    if STATE["world"]["base_location"] == "cathedral":
        a "History. Identity. Something to fight for, not just against."
    elif STATE["world"]["base_location"] == "relay":
        a "Connection. Adaptability. The ability to survive whatever comes."
    elif STATE["world"]["base_location"] == "vault":
        a "Intelligence. Security. Knowing more than the enemy."
    else:  # clinic
        a "People. Healing. The reason we're fighting in the first place."

    sel "Interesting."
    sel "Most commanders prioritize defense. Walls, weapons, escape routes."
    sel "You prioritized meaning."

    a "Meaning is what keeps people fighting when the walls fall."

    sel "(long pause) ...We might actually make something work here, Captain."
    sel "Don't make me regret saying that."

    a "I'll do my best."

    "She nods. Returns to her command."

    "The rebellion has a home now. A place to build, to plan, to become something more than survivors."

    athought "Whatever happens next, this is where we make our stand."
    athought "This is where we find out who we're becoming."

    # --- SCENE WRAP ---
    $ flag_on("Selene", "base_selected")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_16_finding_home
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Day 8. Group planning session for base selection.
# cann.what_happened:
#   - Full cast assembled: Selene, Aeron, Lyra, Zira, Noelle, Tessa.
#   - Four base options presented, each reflecting an LI's personality:
#       • Cathedral Ruins (Lyra): Faith, history, symbolic weight, acoustic surveillance disruption.
#       • Relay Station (Zira): Communication, mobility, 11 exit routes, Ghostline integration.
#       • Data Vault (Noelle): Security, false records, Echelon thinks it's destroyed.
#       • Mercy Ward (Tessa): Medical infrastructure, healing, community building.
#   - Player chooses base location—affects world state and LI relationships.
#   - Selene approves, assigns roles for setup.
#   - Closing conversation: Selene notes Aeron prioritized "meaning" over defense.
# cann.aeron_state:
#   - Making a decision that reflects his values and affects the rebellion's identity.
#   - The choice validates one LI's vision—affects trust/affection with them.
# cann.path_tracking:
#   - One `record_choice_once` decision (no empathy weight—this is about preference, not morality):
#       • `_chose_cathedral` → base_cathedral, Lyra trust+1/affection+1
#       • `_chose_relay` → base_relay, Zira trust+1/affection+1
#       • `_chose_vault` → base_vault, Noelle trust+1/affection+1
#       • `_chose_clinic` → base_clinic, Tessa trust+1/affection+1
#   - STATE["world"]["base_location"] set for future scene variations.
#   - Running empathy range at scene end: -16 to +6 (unchanged—no empathy choice).
# cann.thematic_flags:
#   - Four philosophies: Faith, Mobility, Security, Compassion.
#   - "Meaning is what keeps people fighting when the walls fall."
#   - Each base represents an LI's core values—choosing validates them.
#   - The rebellion becoming something more than survivors.
# cann.character_moments:
#   - Lyra: The Cathedral connects to her Order history. Moved if chosen.
#   - Zira: Practical, survival-focused. Pleased if chosen.
#   - Noelle: The Vault is where she started questioning—personal associations. Touched if chosen.
#   - Tessa: "A clinic says something different than a bunker." Grateful if chosen.
#   - Selene: Approves of "meaning over defense"—impressed by Aeron's thinking.
# cann.worldbuilding:
#   - Cathedral of the Lower Resonance: Branch of Order of Saint Solenne, predates Echelon.
#   - Relay Station Sigma-7: Old transit authority, part of original Ghostline backbone.
#   - Archive Vault Delta-9: Former Cognitive Division facility Noelle falsified as destroyed.
#   - Mercy Ward: Triage center from containment blackouts, sealed when funding died.
# cann.block_status:
#   - Dynamic base selection complete. Base location affects future scenes.
# cann.requires_followup:
#   - Base setup scenes (establishing the chosen location).
#   - The chosen location will be targeted in the Echelon counter-strike (Movement IV).
#   - Community building at the base—relationships with locals.
#   - Non-chosen LIs should still contribute to the base (not sidelined).
