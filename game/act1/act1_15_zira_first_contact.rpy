# ======================================================
# ACT 1 - Scene 15: Aeron's First Encounter with Zira
# File: act1_15_zira_first_contact.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_15_zira_first_contact"
$ scene_mark(_current_scene_id, "entered")


label act1_zira:

    # Alignment reads for light flavor only (no momentum here)
    $ tier = get_alignment_tier()                  # OB3..EMP3
    $ is_ob_hard = pass_tier("OB3","OB2")         # ≈ <= -4
    $ is_mid     = pass_tier("OB1","C")           # ≈ -3..+1
    $ band = get_empathy_band()                   # "obedience" | "conflicted" | "empathy"

    # VISUAL: Lower Spans — northeast edge, Grid Six-Two; skeletal catwalk over drop, chainlink and warning stencils.
    # LIGHTING: Sodium spill + cold service LEDs; intermittent signage flicker; occasional drone cone sweep.
    # SOUND: Drip cadence from overhead pipes; distant market murmur; elevator chain rattle; sub-bass hum of grid.
    # CAMERA: Slow lateral dolly along catwalk; shallow depth; bokeh neon below; cut-ins on boots/hand/holster.
    # PROP: Folded mission order in coat pocket; Zira’s wrist glove (micro-ports, filament glow), open access plate.

    "Northeast edge. Grid Six-Two."
    "The coordinates from the message."
    "I walk the crumbling spine of Sector Ten’s edge—Marcus’s order folded in my coat like a threat."

    athought "No eyes. No witnesses. No backup."
    athought "Perfect place to bury the truth."
    athought "Or perfect place for Glass to finally see what it's been cutting."

    # VISUAL: Movement at knee height—fiber bundle pulled; sparks spit; a hooded figure stays low, precise.
    "Movement. Quick. Intentional. Hands vanish into an access plate. Rhythm says practice, not panic."

    a "Stop right there."
    # CAMERA: Over-shoulder on Aeron to the figure; faint blue interference glow lifts as she pauses.
    z "If you were going to shoot, you would’ve already."
    a "Turn around. Slowly."

    # VISUAL: Hood half-off; cheek lit cyan by a jittering status LED; city glow traces a silhouette.
    z "Relax. Not armed. Not stupid either. Don’t be either."

    a "You’re interfering with city systems."
    z "And you’re dressed too clean for the Unders. So who’s really interfering?"
    a "Who are you?"
    z "Someone who keeps this grid from eating its own power loops."
    z "Also someone with zero patience for Echelon hounds—so unless you’re lost—"

    a "I’m not with the enforcers. Not tonight."
    z "Then you’re either rogue or stupid. And you don’t look stupid."
    # CAMERA: Tight on Zira’s eyes; tiny scan up/down; recognition flicker.
    z "(studies him) Wait. You’re Glass, aren’t you?"

    a "(tense) What did you just say?"
    z "Glass. Marcus Rylan’s weapon. Three-ninety operations. Zero failures."
    z "Everyone in the Unders knows about Glass."
    a "And what do they say?"
    z "That Glass is sharp. Empty. And it always cuts."
    z "(tilts head) But you’re down here. Night before a sweep. That’s not what Glass does."

    # BLOCKING: Aeron closes distance one step; Zira shifts to keep the access panel between them.
    a "What were you doing just now?"
    z "Re-routing drain energy to keep a shelter warm."
    a "So you’re a vigilante now?"
    z "I’m alive. That’s already illegal down here."
    z "Especially after tomorrow. After your sweep."

    a "(sharp) How do you know about that?"
    z "Because I watch everything that happens in Sector Ten. Including your orders."
    z "Two to five hundred targets. Dawn deployment. Zero tolerance."
    z "(bitter) 'Acceptable collateral.' That’s the word, right?"

    # SOUND/FX: Low hum grows; drone cone grazes the railing; dust motes flash.
    "A patrol drone climbs the column; searchlight scrapes rust and warnings."
    a "They’re sweeping. You triggered a ping."
    z "No, your boots did."

    # PROP: Zira’s glove ports iris shut; cables retract with a soft zip.
    z "(closing glove) Fine. I’m out. Try not to get killed, Glass."

    # ---------------------------------------------------
    # PLAYER CHOICE — stop her or not
    # ---------------------------------------------------
    menu:
        "Stop her":
            if choice_and_dev(
                _current_scene_id, "stop_zira_honesty_trade", "EMP", factor=1,
                next_scene_label="act1_15_zira_first_contact",
                note="Stops Zira; trades honesty for information (empathy +1)."
            ):
                $ rel_bump("Zira", trust=+1)
            $ set_scene_flag(scene_id, "stopped_zira")

            # CAMERA: Hand half-raise (not to the gun); open palm—de-escalation.
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
            # VISUAL: Zira’s mouth quirks; not quite a smile—assessment logged.
            z "(studies him) You’re not what I expected."
            a "What did you expect?"
            z "Another Aeries puppet. But you’re asking questions."
            a "Dangerous questions?"
            z "(grins) The best kind."

        "Let her go":
            if choice_and_dev(
                _current_scene_id, "let_zira_walk", "OB", factor=1,
                next_scene_label="act1_15_zira_first_contact",
                note="Allows Zira to leave; maintains distance (obedience +1)."
            ):
                $ rel_bump("Zira", trust=-1)
            $ set_scene_flag(scene_id, "let_zira_go")

            a "Fine. Walk away."

            # CAMERA: Over-shoulder as she moves; silhouette threads through piping.
            z "Suit yourself. But if you’re down here for truth, you’re already bleeding."
            z "(over shoulder) Glass doesn’t bleed. People do. Figure out which one you are before dawn."

    # ---------------------------------------------------
    # SHARED FOLLOW-UP
    # ---------------------------------------------------
    # BLOCKING: Both tuck into the shadow of a service pylon; light sweeps past, then fades.
    "Another drone drifts overhead. We flatten to steel. The cone moves on."
    pause 0.4

    a "You know this area well."
    z "Better than your mission briefing ever did."

    # CAMERA: Two-shot in profile, catwalk grid behind; wind picks up jacket hems.
    a "I need someone who can tell me what’s really happening here."
    a "The report says organized resistance."
    z "(laughs) Organized resistance? Try families hiding from debt collectors."
    z "Try kids without Branding fees."
    z "Try people who just want to live without Echelon’s boot on their throat."
    a "The intel—"
    z "Is propaganda. Sector Ten isn’t a rebel hub. It’s a cleanup. A purge."
    z "Too many unregistered. Too much independence. Too much humanity."

    athought "Not a military target. A civilian purge."
    athought "Glass has been cutting civilians for years. But this one... deliberate."

    a "How do you know?"

    # PROP: Zira taps her glove—HUD glyphs blink in the reflection of a wet panel.
    z "I read the grid. Energy flow, traffic, waste disposal—every line says residential."
    z "You’re not wiping insurgents, Glass. You’re erasing neighborhoods."

    a "Why tell me?"
    z "Because you came here tonight. Glass doesn’t scout. It executes."
    z "You wanted to see. That means there’s still something human left."

    # Empathy-tone internal read
    if is_ob_hard:
        athought "Humanity. A liability. But she reads me too easily—and I don’t correct her."
    elif is_mid:
        athought "Humanity. A word I stopped using. It doesn’t sound wrong tonight."
    else:
        athought "She’s right. Glass doesn’t question. I’m here because I needed to see."

    z "Tomorrow’s sweep hits eight hundred people, not five. I tracked them—families, elders, kids."
    z "Your report calls them 'targets.' You still think this is about rebels?"

    athought "Eight hundred. The vendor. The child. The fires below. All of them."

    if check_scene_flag("act1_14_lower_spans", "bought_brew") or check_scene_flag("act1_14_lower_spans", "acknowledged_unders"):
        athought "I saw their faces tonight. Laughter. Trade. Ordinary life."
    else:
        athought "I kept my distance. Pretended they were numbers. I can’t now."

    # CAMERA: Push-in on Zira; wind strands of hair across her cheek; she doesn’t flinch.
    z "You can’t refuse the order—Marcus owns you. But you can choose how you obey."
    z "Warn people. Falsify a timestamp. Look away when it matters. Find the cracks."
    z "Glass follows orders. Humans find ways to resist even while obeying."
    z "Show me which one you are."

    a "And if I can’t save them all?"
    z "No one can. But trying still matters."
    z "(quiet) Three-ninety operations of perfection. Tomorrow, try being imperfect. Try being human."

    z "Obsidian Bridge. Midnight tomorrow."
    z "If you fought for them—even if you lost—I’ll be there."
    z "If you just followed orders... don’t bother coming."

    # BLOCKING: She slips behind a vent baffle and is gone; only the filament afterglow remains.
    "She’s gone before I can answer. The alley hum stays—steady, low. A heartbeat that refuses to die."

    a "(quiet) What the hell am I getting into..."
    athought "Eight hundred people. Dawn deployment. My orders."
    athought "Glass obeys. Glass always obeys."
    athought "If I obey tomorrow... what’s left of me afterward?"

    $ set_scene_flag(scene_id, "completed")
    return

# ========= CANON NOTES =========
# cann.scene_id: act1_15_zira_first_contact
# cann.when_in_timeline: Late night, immediately after “The Message” and Lower Spans walk; pre–Sector 10 purge dawn.
# cann.what_happened:
# - Aeron meets Zira at Grid 6–2; she IDs him as Glass and reframes Sector 10 as a purge, not insurgency op.
# - Choice: Stop her (EMP+1) honesty-trade vs Let her go (OB+1) distance-maintenance.
# - Zira sets the test: “Choose how you obey” + summons to Obsidian Bridge (midnight tomorrow).
# cann.aeron_state: OB-hard = guarded/analytical; mid = split; EMP = receptive to seeing civilians as people.
# cann.path_tracking:
# - Menu weights: Stop→ EMP(+1); Let go→ OB(+1). Scene delta range: −1 → +1.
# - Running window BEFORE: ≈ [-32, +33]
# - Running window AFTER: ≈ [-33, +34]
# - Flags: stopped_zira / let_zira_go; completed. Social: add_trust("Zira", ±1).
# cann.thematic_flags: “Choose how you obey”; purge vs insurgency; Glass vs Human; truth in infrastructure (grid tells on power).
# cann.block_status: VARIANT (two-route handshake + shared exposition body).
# cann.true_path_integration: none (no TP touches in this scene).
# cann.visual_plate_economy:
# - REUSE: Sector 10 catwalk master; add drone cone sweep and glove HUD overlays.
# - HERO: Over-shoulder reveal on “You’re Glass,” catwalk two-shot in sodium haze, glove-port close with filament iris.
# cann.requires_followup:
# - If stopped_zira → warmer first exchange at Obsidian Bridge; earlier “honesty” checks may open a micro-route.
# - If let_zira_go → Zira more barbed at the Bridge; trust gate −1 on certain disclosures.
# cann.consistency_asserts:
# - Weather grammar: Lower Spans allow condensation/rain; keep altitude language accurate vs Aeries scenes.
# - Doctrine terms: “latency,” “tolerance,” “acceptable collateral” consistent with prior files.
# - Count integrity: Operation 391 timing intact; 800 civilians claim becomes a checkable data point later.