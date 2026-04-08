# ===================================================

# ACT 2 - Scene 27: Zira Commitment (OB)

# File: act2_26b_zira_commitment_ob.rpy

# Path: OB

# ===================================================

# ========= SCENE START TASKS =========

$ _current_scene_id = "act2_26b_zira_commitment_ob"
$ scene_mark(_current_scene_id, "entered")

label a2_s27_zira_commitment_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 38mm lens (OB baseline), handheld but controlled. Over-shoulder with tighter framing.
    #         Less drift than EMP — more deliberate, more watching. Shadows heavier on faces.
    # LIGHTING: Base common area: dim amber practicals, blue screen glow from terminals.
    #           Zira's tech alcove: LED strips (cool blue/green), but shadows deeper tonight.
    #           Skin tones cooler — less warmth bloom, more contrast.
    # SFX: Loop — base night hum, distant ventilation, quiet electronic whine from equipment.
    #      One-shots — bottle clink, chair scrape, fabric shift. Breath catches sharper.
    # FX/COMP: Screen reflections harsher on faces; less warmth, more clinical blue.
    # BLOCKING: Same physical space as EMP, but the emotional distance is different.
    #           She's watching him more carefully. Measuring. Deciding.
    # CANON: This is their first lewd scene. OB version is different — she's unsettled by what
    #        she saw during the raid. His efficiency. His coldness. She's choosing him anyway.
    #        The intimacy is surrender disguised as hope. Complicity beginning to take root.
    # NOTE: No Carry Scene happened in OB. Aeron went to debrief. Selene was handled by med team.
    #       Zira doesn't have the "relief" of seeing him be tender. She only saw him be effective.
    # CONSENT: 3-gate framework still applies. The consent is real. The motivation is complicated.

    # ========= VOICE BASELINE =========
    # OB cadence: Fewer contractions, more measured. Zira: sharper, more guarded, watching.
    # Tone: Tension → testing → surrender. Something desperate underneath.

    # ========= GATE CHECK =========
    # Zira intimacy requires: trust ≥ 2 OR (trust ≥ 1 AND ghostline_sync)
    if not (STATE["rel"]["Zira"]["trust"] >= 2 or (STATE["rel"]["Zira"]["trust"] >= 1 and STATE["flags"].get("ghostline_sync"))):
        # Gate failed — route to comfort variant
        jump .comfort_variant

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ZIRA'S TECH ALCOVE - NIGHT]
    # Same space. Different feeling. The blue glow feels colder tonight.
    # A bottle of something amber on the workbench. Half empty.

    scene bg_zira_alcove_night with dissolve
    play ambient "sfx/ambient/tech_hum_cold.ogg" fadein 2.0

    "{i}The base has gone quiet. Night watch skeleton crew. Most of the cell sleeping off the raid.{/i}"

    athought "I should be reviewing after-action reports. Cataloging what worked. What did not."

    athought "Instead I am walking toward the blue glow of Zira's corner."

    athought "I do not know why."

    # VISUAL: Zira hunched over a terminal. Soldering iron in hand. Hair tied back, collar loose.
    # CAMERA: Slow approach from behind. She tenses slightly when she hears him.

    "{i}She is hunched over a terminal, soldering iron trailing smoke. Hair pulled back. Collar undone.{/i}"

    "{i}Her shoulders tighten when she hears his footsteps. She does not turn.{/i}"

    z "...you're not subtle, you know."

    athought "She hesitated. She never hesitates."

    a "Was not trying to be."

    # VISUAL: She sets down the iron. Turns. The light catches something guarded in her eyes.
    "{i}She sets down the iron. Turns. The bags under her eyes are heavy, but that is not what catches him.{/i}"

    athought "She is looking at me differently. Measuring something."

    z "Can't sleep?"

    a "Something like that."

    z "Hmm."

    # VISUAL: She reaches for the bottle. Pauses. Pours anyway. Holds it out.
    "{i}She reaches for the bottle. Her hand hovers for a moment before she pours. Holds out a dented metal cup.{/i}"

    z "Medicinal."

    "{i}No joke about Tessa. Just the cup extended.{/i}"

    a "Thanks."

    "{i}He takes it. Their fingers brush. She pulls back first.{/i}"
    pause 0.5

    athought "Something is different."

    # --- THE DEBRIEF (THEIR VERSION) ---

    # VISUAL: He leans against the workbench. She stays in her chair. Keeps the distance.
    "{i}He leans against the bench. She stays in her chair. Does not swivel closer.{/i}"

    z "Hell of a day."

    a "Hell of a day."

    z "Selene almost died."

    a "She did not."

    z "No. She didn't."

    "{i}A pause. She takes a drink. Watches him over the rim.{/i}"
    pause 0.6

    z "You went straight to debrief."

    athought "She noticed."

    a "There was work to do."

    z "The med team had her. You could have..."

    a "Could have what?"

    # VISUAL: She shrugs. But her eyes are still measuring.
    z "Nothing. Forget it."

    athought "She wanted me to go to Selene. She wanted to see something."

    athought "She did not see it."

    # --- THE TURN (OB VERSION) ---

    # VISUAL: She stands. Slower than the EMP version. More deliberate.
    "{i}She stands. The chair rolls away. But she does not close the distance. Not yet.{/i}"

    z "I have a question."

    a "That sounds dangerous."

    z "Most honest things are."

    athought "She said honest. Not true. There is a difference."

    z "During the raid. When Selene went down."

    a "What about it?"

    # VISUAL: Her arms cross. Defensive. But her eyes do not leave his.
    z "You didn't flinch."

    athought "No. I did not."

    a "There wasn't time to flinch."

    z "That's not what I mean."

    "{i}She steps closer. One step. Arms still crossed.{/i}"

    z "Everyone else froze. Lyra. Tessa. Me, for half a second."

    z "You just... kept moving. Gave orders. Adjusted the formation."

    z "Like she was a variable that changed, not a person who fell."

    athought "She is not wrong."

    athought "That should bother me more than it does."

    a "Would you have preferred I froze?"

    z "No. That's not—"

    "{i}She stops. Exhales. Her arms drop.{/i}"

    z "I don't know what I would have preferred. That's the problem."

    # --- THE CONFESSION (OB VERSION) ---

    # VISUAL: She closes the remaining distance. Close enough to touch. Does not touch.
    "{i}She steps into his space. Close. Her voice drops.{/i}"

    z "I've seen a lot of people handle pressure. I've seen soldiers. Commanders. Killers."

    z "I've never seen anyone handle it the way you do."

    a "Is that a compliment?"

    z "I don't know."

    athought "She is scared. Not of me. Of what she is about to do."

    z "I watched you today. The way you moved. The way you decided."

    z "Part of me was impressed. Part of me was..."

    a "Was what?"

    # VISUAL: Her hand comes up. Hovers near his jaw. Trembles slightly.
    z "Terrified."

    "{i}Her fingers find his jaw. The touch is light. Testing.{/i}"

    z "And I can't figure out which part is winning."

    athought "Neither can I."

    z "So I'm going to do something stupid."

    a "Zira—"

    z "I'm going to bet on the version of you I want to believe in."

    z "The one who carried her to her room in some other timeline."

    z "The one who flinched and didn't let anyone see."

    athought "She thinks there is another version. A softer one hiding underneath."

    athought "I do not know if she is right."

    # --- CONSENT GATE A: VERBAL CUE ---

    z "Tell me I'm not wrong."

    "{i}Her voice is quiet. Stripped of sarcasm. Just her.{/i}"

    z "Tell me there's something in there worth betting on."

    athought "Is there?"

    athought "I do not know. But I want there to be."

    athought "I want it for her."

    # --- CHOICE: RECIPROCATE OR PAUSE ---

    menu:
        "{i}Her hand is warm against his jaw. Her eyes are searching for something.{/i}"

        "You're not wrong.":
            $ choice_and_dev(
                _current_scene_id, "_reassure", "OB", factor=0,
                next_scene_label=None,
                note="Reassurance; may or may not be true. He wants it to be."
            )
            $ STATE["flags"]["ZIRA_CONSENT_A"] = True
            jump .escalation

        "I don't know what I am anymore.":
            $ choice_and_dev(
                _current_scene_id, "_honest_doubt", "OB", factor=1,
                next_scene_label=None,
                note="Honest uncertainty; vulnerability in OB context. Rare."
            )
            $ STATE["flags"]["ZIRA_CONSENT_A"] = True
            $ STATE["flags"]["ZIRA_OB_HONEST"] = True
            jump .honest_doubt

    return

# --- BRANCH: HONEST DOUBT ---
label .honest_doubt:

    a "I don't know what I am anymore."

    "{i}The words come out quieter than intended.{/i}"

    z "...that's not reassuring."

    a "No. It's not."

    athought "But it is true. And she asked for honesty."

    # VISUAL: Something shifts in her expression. The fear mixes with something else.
    z "At least you're not lying to me."

    a "Would you prefer I did?"

    z "No."

    "{i}She does not pull her hand away. If anything, her grip tightens.{/i}"

    z "I've had enough liars for one lifetime."

    z "I'll take confusion over certainty any day."

    athought "She is choosing me anyway. Knowing I do not know myself."

    athought "That is either brave or foolish."

    athought "Maybe both."

    jump .escalation

# --- ESCALATION ---
label .escalation:

    # VISUAL: He closes the remaining distance. His hand finds her waist. She lets him.
    "{i}He steps into her. His hand finds the curve of her waist. She does not pull back.{/i}"

    athought "She is warm. Real. Here."

    athought "That has to be enough. For now."

    z "You're actually doing this."

    a "You're letting me."

    z "Against my better judgment."

    a "Noted."

    # VISUAL: She almost smiles. It does not quite reach her eyes.
    "{i}She almost smiles. There is something sad underneath it.{/i}"

    # --- CONSENT GATE B: RECIPROCAL ACTION ---

    z "Last chance to back out."

    a "Is that what you want?"

    z "No. But I'm giving you the option."

    z "Because tomorrow I might not remember why I thought this was a good idea."

    athought "She is giving me an exit. And warning me she might regret this."

    athought "I should take the exit."

    athought "I do not."

    a "I'm not going anywhere."

    z "Then neither am I."

    # VISUAL: She pulls him down. The kiss is different than EMP — hungrier, more desperate.
    "{i}She pulls him down by the collar. The kiss is not gentle. It is desperate. Searching.{/i}"

    athought "She is looking for something. The version of me she wants to believe in."

    athought "I do not know if she will find it."

    athought "But I want her to."

    # --- CONSENT GATE C: EXPLICIT OUT ---

    # VISUAL: They break apart. Both breathing hard. Something raw in the air.
    "{i}They break apart. Her forehead against his. Both breathing hard.{/i}"

    z "(breathless) The door has a lock."

    a "I know."

    z "If you want to stop. At any point. Say it."

    a "Same goes for you."

    z "...yeah."

    # VISUAL: She reaches past him. The lock clicks. The light does not warm the same way.
    "{i}She reaches past him. The lock clicks. The screens dim.{/i}"

    "{i}The light does not warm the way it should. But neither of them mentions it.{/i}"

    z "Now. Before I remember all the reasons this is stupid."

    # --- TRANSITION TO INTIMACY ---

    # [FADE TO INTIMATE SCENE OR TASTEFUL SKIP BASED ON PLAYER SETTINGS]

    scene black with dissolve
    pause 1.0

    # ========= POST-INTIMACY =========

    # [INT. ZIRA'S ALCOVE - LATER]
    # Tangled together on the narrow cot. But the silence is different.
    # Something unresolved in the air. Her head on his chest, but her eyes are open.

    scene bg_zira_alcove_after with dissolve
    play ambient "sfx/ambient/room_quiet_cold.ogg" fadein 2.0

    "{i}Later. The cot is narrow. They make it work.{/i}"

    # VISUAL: Zira's head on his chest. But her eyes are open. Staring at the ceiling.
    athought "She is not asleep. Her breathing is too measured."

    athought "She is thinking. Calculating. Already second-guessing."

    z "You're thinking too loud."

    a "So are you."

    z "...fair."

    "{i}Silence. The hum of electronics. The weight of everything unsaid.{/i}"
    pause 0.7

    # --- PILLOW TALK (OB VERSION) ---

    z "I'm going to ask you something. And I need you to not lie to me."

    a "Alright."

    z "During the raid. When you gave the order to fall back from Sector 7."

    z "Did you calculate how many we'd lose?"

    athought "Yes."

    athought "Fourteen. Acceptable margin for the objective."

    athought "I do not say that."

    a "I calculated how many we'd save."

    # VISUAL: She lifts her head. Looks at him. Searching.
    z "That's not what I asked."

    a "I know."

    "{i}She holds his gaze for a long moment. Then settles back against his chest.{/i}"

    z "You're good at that."

    a "At what?"

    z "Answering questions without answering them."

    athought "She sees through me. And she is still here."

    athought "I do not know what that means."

    # --- THE COMMITMENT (OB VERSION) ---

    z "I don't know what you are, Aeron."

    z "But I'm choosing this anyway. Whatever 'this' is."

    z "Just... don't make me regret it."

    athought "I cannot promise that."

    athought "I do not say that either."

    a "I'll try."

    z "That's not a promise."

    a "No. It's not."

    # VISUAL: She laughs. But it is hollow. Tired.
    "{i}She laughs. The sound is hollow. But her hand finds his anyway.{/i}"

    z "At least you're honest about being evasive."

    a "Consistency."

    z "Sure. Let's call it that."

    "{i}Her fingers lace through his. The grip is tight. Almost desperate.{/i}"

    athought "She is holding on to something she is not sure exists."

    athought "I hope it does. For her sake."

    athought "For both of us."

    # --- SCENE CLOSE ---

    z "Get some sleep. Big day tomorrow."

    a "You too."

    z "...eventually."

    "{i}Her eyes close. Her breathing slows. But her grip does not loosen.{/i}"

    athought "Tomorrow she will rebuild her walls. The sarcasm will return."

    athought "And we will both pretend this was simpler than it was."

    athought "But right now, in the blue glow of her screens, she chose me."

    athought "Even knowing what she knows. Even doubting what she doubts."

    athought "That has to mean something."

    athought "It has to."

    # --- FADE OUT ---

    stop ambient fadeout 3.0
    scene black with dissolve

    jump .scene_end

# ========= COMFORT VARIANT (GATE FAILED) =========
label .comfort_variant:

    # If intimacy gate fails, we get a tense but non-sexual scene.
    # The unease is more visible. The connection does not form the same way.

    scene bg_zira_alcove_night with dissolve
    play ambient "sfx/ambient/tech_hum_cold.ogg" fadein 2.0

    "{i}The base has gone quiet. Zira's corner glows blue in the darkness.{/i}"

    "{i}She is at her terminal. Does not look up when he approaches.{/i}"

    z "...can't sleep?"

    athought "The pause. She is deciding whether to acknowledge me."

    a "Something like that."

    z "Join the club."

    "{i}He sits on the crate beside her bench. The silence stretches.{/i}"
    pause 0.8

    z "Hell of a day."

    a "Hell of a day."

    z "You went straight to debrief."

    a "There was work to do."

    z "Right. Work."

    "{i}She does not look at him. Her fingers move across the keyboard. Faster than necessary.{/i}"

    athought "She is angry. Or scared. Or both."

    z "You ever wonder if we're becoming them?"

    a "Becoming who?"

    z "Echelon. The machine. Whatever you want to call it."

    athought "Sometimes."

    a "We do what needs to be done."

    z "That's what they say too."

    "{i}Silence. The hum of electronics. Something cold in the air.{/i}"
    pause 0.7

    z "Get some sleep, Aeron. War's still on tomorrow."

    a "You too."

    z "Eventually."

    "{i}He stands. She does not reach for him. Does not look up.{/i}"

    athought "Something closed tonight. A door that might have opened."

    athought "I do not know how to feel about that."

    athought "I do not know how to feel about anything anymore."

    $ STATE["flags"]["ZIRA_COMFORT_SCENE_OB"] = True
    $ STATE["rel"]["Zira"]["trust"] += 0  # No trust gained in OB comfort

    stop ambient fadeout 2.0
    scene black with dissolve

    jump .scene_end

# ========= SCENE END =========
label .scene_end:

    # ========= STATE UPDATES =========
    $ STATE["scenes"]["A2_26B_ZiraCommitment_OB"] = True

    if STATE["flags"].get("ZIRA_CONSENT_A"):
        $ STATE["flags"]["ZIRA_FIRST_INTIMATE"] = True
        $ STATE["flags"]["ZIRA_OB_COMPLICITY_SEED"] = True
        $ STATE["rel"]["Zira"]["trust"] += 1
        $ STATE["rel"]["Zira"]["affection"] += 1

    # ========= TELEMETRY =========
    #$ telemetry(_current_scene_id, outcome="intimate" if STATE["flags"].get("ZIRA_CONSENT_A") else "comfort")
    $ set_scene_flag(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_26b_zira_commitment_ob
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night after raid. NO Carry Scene preceded this. Before Selene Finale.
#   - OB path variant.
# cann.what_happened:
#   - Aeron finds Zira in her tech alcove. She's more guarded than EMP version.
#   - She confronts him about his lack of reaction when Selene fell — "like a variable, not a person."
#   - She admits she's scared of what she saw, but chooses to bet on "the version of him she wants to believe in."
#   - 3-gate consent framework applies. The consent is real. The motivation is complicated.
#   - If gates passed: first intimate scene. Desperate, searching, something sad underneath.
#   - If gates failed: tense comfort scene. The door that might have opened closes instead.
#   - This is the seed of Zira's complicity. She sees who he is becoming. She stays anyway.
#   - After the Selene execution tomorrow, she will remember this night. She chose him BEFORE.
# cann.aeron_state:
#   - OB coolness — measured, controlled. Moments of genuine uncertainty when she pushes.
# cann.path_tracking:
#   - OB baseline. Honest_doubt choice adds EMP factor (rare OB vulnerability).
#   - Intimate path sets ZIRA_OB_COMPLICITY_SEED for Act 3 gating.
#   - 3-gate consent framework:
#       Gate A: Verbal cue ("Tell me there's something worth betting on")
#       Gate B: Reciprocal action (she gives exit, warns she might regret, he stays)
#       Gate C: Explicit out ("If you want to stop — say it")
#       All gates pass for intimate content. Failed gate → tense comfort variant (colder than EMP).
# cann.thematic_flags:
#   - Motifs: Blue glow (colder here), measuring/calculating, grip that's "almost desperate."
#   - "The version of you I want to believe in" — she's projecting hope onto uncertainty.
#   - "Don't make me regret it" — foreshadowing. She will have reasons to regret.
#   - Tone: Surrender — "I'm betting on a version of you that might not exist."
#   - Contrast with EMP: EMP is joy/relief. OB is desperation/commitment. Different things.
# cann.character_moments:
#   - Zira: Sarcasm thinner than EMP, fear more visible. Choosing him despite doubts, not because of certainty.
#     The intimacy is not celebration — it's a binding. She's choosing the side she'll be on.
#   - Zira's silence in the strategy room (execution scene) is earned here, not arbitrary.
# cann.block_status:
#   - VARIANT (OB); requires followup scene load.
# cann.requires_followup:
#   - Next scene: a2_s28_selene_finale (execution, OB path).
#   - Zira's silence during the execution is set up here. She chose him last night.
#   - "Don't make me regret it" becomes tragic irony when he kills Selene 12 hours later.