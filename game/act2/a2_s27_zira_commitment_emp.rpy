# ===================================================
# ACT 2 - Scene 27: Zira Commitment (EMP)
# File: a2_s27_zira_commitment_emp.rpy
# Path: EMP
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s27_zira_commitment_emp"
$ scene_mark(_current_scene_id, "entered")

label a2_s27_zira_commitment_emp:
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm lens (EMP warmth), handheld intimacy. Over-shoulder bias early,
    #         transitioning to close two-shots as tension builds. 3–5% drift on emotional beats.
    # LIGHTING: Base common area: dim amber practicals, blue screen glow from terminals.
    #           Zira's tech alcove: LED strips (cool blue/green), warm spill from soldering station.
    #           Skin tones prioritized — soft key, minimal harsh shadow.
    # SFX: Loop — base night hum, distant ventilation, quiet electronic whine from equipment.
    #      One-shots — bottle clink, chair scrape, fabric shift, breath catches.
    # FX/COMP: Screen reflections on faces; subtle lens flare from LED strips; warmth bloom on skin.
    # BLOCKING: Zira in her alcove, surrounded by tech. Aeron enters. Physical space shrinks as scene progresses.
    # CANON: This is their first lewd scene. EMP version is celebration — survival high, joy, release.
    #        Zira's sarcasm is armor, but it's thin tonight. She lets him see underneath.
    # CONSENT: 3-gate framework. (A) Verbal cue, (B) Reciprocal action, (C) Explicit exit acknowledged.

    # ========= VOICE BASELINE =========
    # EMP cadence: Warm, sensory, contractions. Zira: sharp humor softening into genuine vulnerability.
    # Tone: Flirtation → tension → release. Joy underneath everything.

    # ========= GATE CHECK =========
    # Zira intimacy requires: trust ≥ 2 OR (trust ≥ 1 AND ghostline_sync)
    if not (STATE["rel"]["Zira"]["trust"] >= 2 or (STATE["rel"]["Zira"]["trust"] >= 1 and STATE["flags"].get("ghostline_sync"))):
        # Gate failed — route to comfort variant
        jump .comfort_variant

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ZIRA'S TECH ALCOVE - NIGHT]
    # A corner of the common area she's claimed as her own. Screens, wires, half-built devices.
    # The blue glow of a dozen displays. A bottle of something amber on the workbench.

    scene bg_zira_alcove_night with dissolve
    play ambient "sfx/ambient/tech_hum_warm.ogg" fadein 2.0

    "The base has gone quiet. Night watch skeleton crew. Most of the cell sleeping off the raid."

    athought "Tessa kicked me out an hour ago. Said Selene needed sleep more than an audience."

    athought "She was right. Doesn't mean I can sleep either."

    athought "Instead I'm walking toward the blue glow of Zira's corner."

    # VISUAL: Zira hunched over a terminal. Soldering iron in hand. Hair tied back, collar loose.
    # CAMERA: Slow approach from behind. She doesn't turn, but she knows he's there.

    "She's hunched over a terminal, soldering iron trailing smoke. Hair pulled back. Collar undone."

    z "You're not subtle, you know."

    athought "She didn't turn around. Didn't need to."

    a "Wasn't trying to be."

    # VISUAL: She sets down the iron. Turns. The light catches the exhaustion under her eyes.
    "She sets down the iron. Turns. The bags under her eyes match his."

    z "Can't sleep either?"

    a "Something like that."

    z "Hmm."

    # VISUAL: She reaches for the bottle. Pours two fingers into a dented cup. Holds it out.
    "She reaches for the bottle on the bench. Pours. Holds out a dented metal cup."

    z "Medicinal. Don't tell Tessa."

    a "Wouldn't dream of it."

    "He takes the cup. Their fingers brush. Neither pulls back."
    pause 0.5

    # --- THE DEBRIEF (THEIR VERSION) ---

    # VISUAL: He leans against the workbench. She swivels her chair to face him. Close quarters.
    "He leans against the bench. She swivels to face him. The space between them shrinks."

    z "Hell of a day."

    a "Hell of a day."

    z "Selene almost died."

    a "She didn't."

    z "Not just because of Tessa. Because you were there."

    athought "Because she threw herself in front of a bullet. I just carried her afterward."

    a "I didn't do anything special."

    # VISUAL: Zira's eyebrow arches. The look that says she sees through his deflection.
    z "You carried her to her room. Stayed all night."

    athought "Word travels fast."

    a "Tessa has a big mouth."

    z "Tessa didn't say anything. The kid who saw you in the corridor did."

    athought "Of course."

    z "Relax. It's not gossip. It's... relief."

    a "Relief?"

    # VISUAL: She takes a drink. Her eyes don't leave his.
    z "People were starting to wonder if you had anything left in there."

    "She taps her chest. Over her heart."

    z "Now they know."

    athought "Now they know."

    athought "Do I know?"

    # --- THE TURN ---

    # VISUAL: She sets down the cup. Stands. The chair rolls back with a soft whine.
    "She stands. The chair rolls away. The distance between them halves."

    z "I have a confession."

    a "That sounds dangerous."

    z "Most true things are."

    athought "She's close enough that I can smell the smoke and solder on her skin."

    athought "Close enough that I can see the pulse in her throat."

    z "I was scared today. Not during the op — I've done a hundred ops."

    z "After. When I saw her go down. When I saw your face."

    a "My face?"

    # VISUAL: Her hand comes up. Hovers near his jaw. Doesn't quite touch.
    z "You looked like someone who'd lost something they didn't know they had."

    athought "She's not wrong."

    z "And I thought... what if that was me? What if you looked at me like that?"

    a "Zira—"

    z "Shut up. I'm confessing. Don't interrupt."

    # VISUAL: Her hand lands. Fingertips on his jaw. Light. Testing.
    "Her fingers find his jaw. Light. Tentative. Like she's checking if he's real."

    z "I don't do this. Feelings. Vulnerability. All that messy organic crap."

    z "But we almost died today. And I don't want to almost die tomorrow without..."

    a "Without what?"

    # VISUAL: She meets his eyes. The sarcasm is gone. Just her.
    z "Without knowing what this is."

    # --- CONSENT GATE A: VERBAL CUE ---

    athought "This is the moment. The edge of something."

    athought "I could step back. Make a joke. Pretend I don't understand."

    athought "But I'm tired of pretending."

    a "What do you want it to be?"

    z "I want it to be real. Even if it's just tonight."

    z "Even if tomorrow we go back to sarcasm and distance."

    z "I want one real thing."

    # --- CHOICE: RECIPROCATE OR PAUSE ---

    menu:
        "Her hand is warm against his jaw. Her eyes are asking a question."

        "Then let's be real.":
            $ choice_and_dev(
                _current_scene_id, "_direct_reciprocate", "EMP", factor=1,
                next_scene_label=None,
                note="Direct acceptance; confidence in the moment."
            )
            $ STATE["flags"]["ZIRA_CONSENT_A"] = True
            jump .escalation

        "Are you sure? This changes things.":
            $ choice_and_dev(
                _current_scene_id, "_careful_check", "EMP", factor=1,
                next_scene_label=None,
                note="Careful confirmation; respecting the weight of the choice."
            )
            $ STATE["flags"]["ZIRA_CONSENT_A"] = True
            $ STATE["flags"]["ZIRA_CAREFUL"] = True
            jump .careful_check

# --- BRANCH: CAREFUL CHECK ---
label .careful_check:

    a "Are you sure? This changes things."

    # VISUAL: She laughs. Short. Real.
    z "Things already changed. The moment you walked over here."

    z "I just want to know if you're walking toward something or away from something else."

    athought "Toward. Definitely toward."

    a "Toward."

    z "Good answer."

    jump .escalation

# --- ESCALATION ---
label .escalation:

    # VISUAL: He closes the distance. His hand finds her waist. Her breath catches.
    "He steps into her space. His hand finds the curve of her waist. Her breath stutters."

    athought "She's warm. Real. Alive."

    athought "We're both alive."

    z "You're actually doing this."

    a "You're actually letting me."

    z "Don't get cocky. I can still electrocute you with three different things in arm's reach."

    a "Noted."

    # VISUAL: She grins. It's sharp and soft at the same time.
    "Her grin is sharp. But her hands are gentle when they find his chest."

    # --- CONSENT GATE B: RECIPROCAL ACTION ---

    z "Last chance to back out, hero."

    a "Is that what you want?"

    z "No. But I'm giving you the option. Because that's how this works."

    athought "She's giving me an exit. Clear. Explicit."

    athought "I don't want it."

    a "I'm not going anywhere."

    z "Then neither am I."

    # VISUAL: She pulls him down by the collar. The kiss is fierce and real.
    "She pulls him down by the collar. The kiss isn't gentle. It's hungry. Alive."

    athought "She tastes like cheap whiskey and solder smoke and something underneath that's just her."

    athought "I've been wanting this longer than I admitted."

    # --- CONSENT GATE C: EXPLICIT OUT ---

    # VISUAL: They break apart. Both breathing hard. Her forehead against his.
    "They break apart. Foreheads touching. Both breathing like they've been running."

    z "(breathless) The door has a lock."

    a "I noticed."

    z "If you want to stop — at any point — you say the word. No questions. No judgment."

    a "Same goes for you."

    z "Good."

    # VISUAL: She reaches past him. The lock clicks. The blue light dims to something warmer.
    "She reaches past him. The lock clicks. The lights shift — screens dimming, warm strips glowing."

    z "Now. Where were we?"

    # --- TRANSITION TO INTIMACY ---

    # [FADE TO INTIMATE SCENE OR TASTEFUL SKIP BASED ON PLAYER SETTINGS]

    scene black with dissolve
    pause 1.0

    # ========= POST-INTIMACY =========

    # [INT. ZIRA'S ALCOVE - LATER]
    # Tangled together on the narrow workbench cot she keeps for all-nighters.
    # Screens casting soft glow. Her head on his chest. His hand in her hair.

    scene bg_zira_alcove_after with dissolve
    play ambient "sfx/ambient/room_quiet_warm.ogg" fadein 2.0

    "Later. The cot she keeps for all-nighters is narrow. They make it work."

    # VISUAL: Zira's head on his chest. His hand tracing lazy patterns on her shoulder.
    athought "Her hair smells like ozone and something floral she'd never admit to using."

    athought "Her breathing has slowed. Steady. Content."

    z "You're thinking too loud."

    a "Sorry."

    z "Don't be. It's kind of endearing."

    athought "Endearing. She called me endearing."

    athought "I'm never going to let her live that down."

    # --- PILLOW TALK ---

    z "So. Scale of one to ten. How weird is this going to be tomorrow?"

    a "Depends. Are you going to pretend it didn't happen?"

    z "Do you want me to?"

    a "No."

    # VISUAL: She lifts her head. Looks at him. Something soft in her expression.
    z "Then no. I'm not going to pretend."

    z "But I'm also not going to get mushy about it. Fair warning."

    a "I'd be worried if you did."

    # VISUAL: She settles back against him. Her hand finds his. Fingers interlock.
    "She settles back. Her hand finds his. Fingers lacing together."

    z "For what it's worth... I'm glad you walked over here."

    a "For what it's worth... so am I."

    z "Don't let it go to your head."

    a "Too late."

    # VISUAL: She laughs. Low. Real. The sound vibrates against his chest.
    "She laughs. The sound is low and real and it vibrates through him."

    athought "This might be a mistake. Might complicate everything."

    athought "I don't care."

    athought "We made it. She's here. I'm not asking for anything more."

    # --- SCENE CLOSE ---

    z "Get some sleep. We've got a war to win tomorrow."

    a "Yes ma'am."

    z "Don't call me ma'am. It makes me feel old."

    a "You're three years older than me."

    z "And I'll electrocute you for every single one of them if you bring it up again."

    athought "Noted."

    "Her eyes close. Her breathing evens out. Her hand stays in his."

    athought "Tomorrow there'll be questions. Looks. Zira's legendary emotional walls rebuilding."

    athought "But right now, in the blue glow of a dozen screens, none of that matters."

    athought "Right now, she's here. I'm here. We made it through."

    athought "I'm not asking for anything more than that."

    # --- FADE OUT ---

    stop ambient fadeout 3.0
    scene black with dissolve

    jump .scene_end

# ========= COMFORT VARIANT (GATE FAILED) =========
label .comfort_variant:

    # If intimacy gate fails, we get a tender but non-sexual scene.
    # They connect, but she's not ready. He respects it.

    scene bg_zira_alcove_night with dissolve
    play ambient "sfx/ambient/tech_hum_warm.ogg" fadein 2.0

    "The base has gone quiet. Zira's corner glows blue in the darkness."

    "She's at her terminal. Doesn't look up when he approaches."

    z "Can't sleep?"

    a "Something like that."

    z "Join the club. Membership is mandatory, meetings are whenever the nightmares let up."

    athought "She jokes. She always jokes. It's how she survives."

    "He sits on the crate beside her bench. They don't talk for a while."
    pause 0.7

    z "Hell of a day."

    a "Hell of a day."

    z "Selene almost..."

    a "But she didn't."

    z "No. She didn't."

    "Silence. The hum of electronics. The weight of everything unsaid."
    pause 0.8

    z "You ever think about what happens if we actually win?"

    a "Sometimes."

    z "I don't know how to picture it. A life without this."

    athought "Neither do I."

    a "We'll figure it out. Together."

    # VISUAL: She looks at him. Something vulnerable flickers and disappears.
    z "Together. That's a big word."

    a "It's just a word."

    z "No. It's not."

    "She goes back to her screen. But her shoulder brushes his. Stays there."

    athought "Not tonight. Maybe not for a while. But something's shifted."

    athought "A door opened. Neither of us walked through."

    athought "But we both know it's there now."

    z "Get some sleep, hero. War's still on tomorrow."

    a "You too."

    z "Yeah. Eventually."

    "He stands. Her hand catches his wrist. Quick. Light."

    z "Thanks. For checking on me."

    a "Anytime."

    "He walks away. Her hand falls. The glow of her screens follows him out."

    athought "Not tonight. But someday."

    athought "Someday."

    $ STATE["flags"]["ZIRA_COMFORT_SCENE"] = True
    $ STATE["flags"]["aftercare_flag"] = True
    $ STATE["rel"]["Zira"]["trust"] += 1

    stop ambient fadeout 2.0
    scene black with dissolve

    jump .scene_end

# ========= SCENE END =========
label .scene_end:

    # ========= STATE UPDATES =========
    $ STATE["scenes"]["A2_26B_ZiraCommitment_EMP"] = True

    if STATE["flags"].get("ZIRA_CONSENT_A"):
        $ STATE["flags"]["ZIRA_FIRST_INTIMATE"] = True
        $ STATE["rel"]["Zira"]["trust"] += 1
        $ STATE["rel"]["Zira"]["affection"] += 2

    # ========= TELEMETRY =========
    #$ telemetry(_current_scene_id, outcome="intimate" if STATE["flags"].get("ZIRA_CONSENT_A") else "comfort")
    $ set_scene_flag(_current_scene_id, "completed")

    return

​
# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s27_zira_commitment_emp
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night after raid. After Carry Scene (EMP). Before Selene Finale.
#   - EMP path variant.
# cann.what_happened:
#   - Aeron finds Zira in her tech alcove, both unable to sleep after the raid.
#   - She confesses fear — not of dying, but of mattering to someone who might look at her
#     the way Aeron looked at Selene when she fell.
#   - 3-gate consent framework: verbal cue, reciprocal action, explicit exit acknowledged.
#   - If gates passed: first intimate scene. Playful, real, joyful despite the context.
#   - If gates failed: comfort scene. Connection without intimacy. Door opened, not walked through.
# cann.aeron_state:
#   - EMP warmth — guard down, emotionally available, present.
# cann.path_tracking:
#   - EMP baseline. Intimate path adds trust+1, affection+2. Comfort adds trust+1, aftercare_flag.
#   - 3-gate consent framework:
#       Gate A: Verbal cue ("I want one real thing")
#       Gate B: Reciprocal action (she gives explicit exit option, he declines)
#       Gate C: Explicit out ("If you want to stop — at any point — you say the word")
#       All gates must pass for intimate content. Failed gate → comfort variant.
# cann.thematic_flags:
#   - Motifs: Blue glow (screens, tech, her world), warmth bleeding in, hands.
#   - Zira's sarcasm-as-armor: "Don't call me ma'am, it makes me feel old."
#   - "We made it" — the EMP survival refrain.
#   - Tone: Celebration — "we're alive, we made it, I want something real."
#   - Contrast with OB: EMP is joy/relief. OB is desperation/unsettled.
# cann.character_moments:
#   - Zira: Sarcasm as thinning armor. Genuine underneath. Choosing vulnerability.
#   - Tessa (implied): "Tessa knows" about the carry scene. Now "everyone knows" about Zira too.
# cann.block_status:
#   - VARIANT (EMP); requires followup scene load.
# cann.requires_followup:
#   - Next scene: a2_s28_selene_finale (shared command offer, EMP path).
#   - Zira's "legendary emotional walls" referenced — she'll be sarcastic tomorrow but different.
#   - Team dynamics shift as relationships become visible.