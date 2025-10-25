# act1_15_zira_first_contact.rpy


# =======================================================
# ACT 1 - Scene 15: Aeron's First Encounter with Zira
# =======================================================


label act1_zira:
    $ scene_id = "act1_15_zira_first_contact"

    # Alignment reads for light flavor only
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    $ band = get_empathy_band()                   # "obedience" | "conflicted" | "empathy"

    "{i}Northeast edge. Grid Six-Two.{/i}"
    "{i}The coordinates from the message.{/i}"
    "{i}Aeron walks the crumbling spine of Sector 10’s northeast edge, Marcus’s mission order folded in his coat like a threat.{/i}"

    a "{i}No eyes. No witnesses. No backup.{/i}"
    a "{i}Perfect place to bury the truth.{/i}"
    a "{i}Or perfect place for Glass to finally see what it's been cutting.{/i}"

    # VISUAL: A figure crouched near an access panel, wires glowing faintly.
    "{i}Movement. Quick. Intentional. Someone tampering with the wall—steady hands, steady rhythm.{/i}"

    a "Stop right there."
    z "If you were going to shoot, you would’ve already."
    a "Turn around. Slowly."

    # VISUAL: Hood half-off, face lit by blue interference glow.
    z "Relax. Not armed. Not stupid either. Don’t be either."

    a "You’re interfering with city systems."
    z "And you’re dressed too clean for the Unders. So who’s really interfering?"
    a "Who are you?"
    z "Someone who keeps this grid from eating its own power loops."
    z "Also someone with zero patience for Echelon hounds—so unless you’re lost—"

    a "I’m not with the enforcers. Not tonight."
    z "Then you’re either rogue or stupid. And you don’t look stupid."
    z "(studies him) Wait. You’re Glass, aren’t you?"

    a "(tense) What did you just say?"
    z "Glass. Marcus Rylan’s weapon. 390 operations. Zero failures."
    z "Everyone in the Unders knows about Glass."
    a "And what do they say?"
    z "That Glass is sharp. Empty. And it always cuts."
    z "(tilts head) But you’re down here. Night before a sweep. That’s not what Glass does."

    a "What were you doing just now?"
    z "Re-routing drain energy to keep a shelter warm."
    a "So you’re a vigilante now?"
    z "I’m alive. That’s already illegal down here."
    z "Especially after tomorrow. After your sweep."

    a "(sharp) How do you know about that?"
    z "Because I watch everything that happens in Sector 10. Including your orders."
    z "200–500 targets. Dawn deployment. Zero tolerance."
    z "(bitter) 'Acceptable collateral.' That’s the word, right?"

    "{i}A low hum approaches—patrol drone. Searchlight scraping the walls.{/i}"
    a "They’re sweeping. You triggered a ping."
    z "No, your boots did."

    z "(closing glove) Fine. I’m out. Try not to get killed, Glass."

    # ---------------------------------------------------
    # PLAYER CHOICE — stop her or not
    # ---------------------------------------------------
    menu:
        "Stop her":
            $ set_scene_flag(scene_id, "stopped_zira")
            $ add_trust("Zira", 1)
            $ adjust_empathy_once("zira_stop_ask_honesty", +1)
            a "Wait. I need information."
            z "That’ll cost you."
            a "Money?"
            z "No. Honesty."
            a "...I’m listening."
            z "Why are you really here? Night before your sweep?"
            if check_scene_flag("act1_14_lower_spans", "reassured_child") or check_scene_flag("act1_14_lower_spans", "acknowledged_unders"):
                a "Because I wanted to see their faces first."
            else:
                a "Because something felt wrong about the intel."
            z "(surprised) ...Glass said that?"
            a "Maybe Glass is cracking."
            z "(studies him) You’re not what I expected."
            a "What did you expect?"
            z "Another Aeries puppet. But you’re asking questions."
            a "Dangerous questions?"
            z "(grins) The best kind."

        "Let her go":
            $ set_scene_flag(scene_id, "let_zira_go")
            $ add_trust("Zira", -1)
            $ adjust_empathy_once("zira_let_go", -1)
            a "Fine. Walk away."
            z "Suit yourself. But if you’re down here for truth, you’re already bleeding."
            z "(over shoulder) Glass doesn’t bleed. People do. Figure out which one you are before dawn."

    # ---------------------------------------------------
    # SHARED FOLLOW-UP
    # ---------------------------------------------------
    "{i}Another drone passes overhead. Both dive into cover; light washes the alley, then fades.{/i}"

    a "You know this area well."
    z "Better than your mission briefing ever did."

    a "I need someone who can tell me what’s really happening here."
    a "The report says organized resistance."
    z "(laughs) Organized resistance? Try families hiding from debt collectors."
    z "Try kids without Branding fees."
    z "Try people who just want to live without Echelon’s boot on their throat."
    a "The intel—"
    z "Is propaganda. Sector 10 isn’t a rebel hub. It’s a cleanup. A purge."
    z "Too many unregistered. Too much independence. Too much humanity."

    a "{i}Not a military target. A civilian purge.{/i}"
    a "{i}Glass has been cutting civilians for years. But this one... deliberate.{/i}"

    a "How do you know?"
    z "I read the grid. Energy flow, traffic, waste disposal—all residential signatures."
    z "You’re not wiping insurgents, Glass. You’re erasing neighborhoods."

    a "Why tell me?"
    z "Because you came here tonight. Glass doesn’t scout. It executes."
    z "You wanted to see. That means there’s still something human left."

    # ---------------------------------------------------
    # Empathy-tone response (via tiers)
    # ---------------------------------------------------
    if is_ob_hard:
        a "{i}Humanity. A liability. But I can’t deny she reads me too easily.{/i}"
    elif is_mid:
        a "{i}Humanity. A word I stopped using years ago. But it doesn’t sound wrong tonight.{/i}"
    else:
        a "{i}She’s right. Glass doesn’t question. But I’m standing here because I needed to see.{/i}"

    z "Tomorrow’s sweep hits 800 people, not 500. I tracked them myself—families, elders, kids."
    z "Your report calls them 'targets.' You still think this is about rebels?"

    a "{i}800 people. The vendor. The child. The families around fires. All of them.{/i}"

    if check_scene_flag("act1_14_lower_spans", "bought_brew") or check_scene_flag("act1_14_lower_spans", "acknowledged_unders"):
        a "{i}I saw their faces tonight. They laughed, traded, existed.{/i}"
    else:
        a "{i}I avoided their eyes. Pretended they weren’t real. Now I can’t.{/i}"

    z "You can’t refuse the order—Marcus owns you. But you can choose how you obey."
    z "Warn people. Fake reports. Look away when it matters. Find the cracks."
    z "Glass follows orders. Humans find ways to resist even while obeying."
    z "Show me which one you are."

    a "And if I can’t save them all?"
    z "No one can. But trying still matters."
    z "(quiet) 390 operations of perfection. Tomorrow, try being imperfect. Try being human."

    z "Meet me at Obsidian Bridge. Midnight tomorrow."
    z "If you fought for them—even if you lost—I’ll be there."
    z "If you just followed orders... don’t bother coming."

    "{i}She’s gone before he can answer. The alley hum remains, steady and low—like a heartbeat that refuses to die.{/i}"

    a "(quiet) What the hell am I getting into..."
    a "{i}800 people. Dawn deployment. My orders.{/i}"
    a "{i}Glass obeys. Glass always obeys.{/i}"
    a "{i}But if I obey tomorrow... what’s left of me afterward?{/i}"

    $ set_scene_flag(scene_id, "completed")
    return
