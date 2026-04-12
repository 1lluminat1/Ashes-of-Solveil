# =======================================================
# ACT 3 - Scene 03: Breath of Faith (Empathy Path)
# File: a3_s03_breath_of_faith_emp.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s03_breath_of_faith_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s03_breath_of_faith_emp:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("lyra_vashar", to_stage=2, source="a3_s03_breath_of_faith_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm lens (EMP warmth), handheld intimacy. Wide establishing shot of balcony,
    #         then tightening to two-shots as they connect. Slow drift on emotional beats.
    # LIGHTING: Balcony exterior: city glow from below (amber/orange), cool 4500K moonlight from above.
    #           Practicals: faint green glow from Ghostline relay nearby. Rim lighting on profiles.
    #           As intimacy escalates, warmer tones bleed in - 3200K warmth on skin.
    # SFX: Loop - wind, distant city hum, faint Ghostline carrier frequency (musical, not harsh).
    #      One-shots - door hiss, fabric shift, breath catches, railing creak.
    # FX/COMP: Wind in hair, city lights bokeh below, subtle lens flare on practicals.
    # BLOCKING: Aeron at railing, gripping it. Lyra enters behind. Distance closes through scene.
    #           The breathing exercise requires physical contact - hands first, then closer.
    # CANON: This is Lyra's first potential intimacy scene in Act 3 EMP.
    #        The pretense is grounding, not seduction. Emotion first, desire second.
    #        Her Order background shapes the breathing technique - but she's reinterpreted it.
    # CONSENT: 3-gate framework. (A) Verbal cue, (B) Reciprocal action, (C) Explicit exit acknowledged.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, sensory language, emotional availability.
    # Aeron is struggling - hands shaking, static in his head, fear of becoming Marcus.
    # Lyra is steady but not distant - her faith has softened into something more human.

    # --- VISUAL SETUP ---
    # [EXT. PHOENIX BASE - PRIVATE BALCONY - NIGHT]
    # A narrow platform jutting from the base's upper structure.
    # The city sprawls below, distant lights like scattered embers.
    # Wind carries the faint hum of the Ghostline carrier frequency.

    #scene bg_balcony_night_emp with dissolve
    #play ambient "sfx/ambient/balcony_wind_warm.ogg" fadein 2.0
    #play music "music/lyra_theme_soft.ogg" fadein 3.0

    # --- OPENING: AERON ALONE ---

    # VISUAL: Aeron at the railing, gripping it. His knuckles are white.
    # CAMERA: Wide establishing shot, then slow push toward him.

    athought "I came up here to think. That was the plan."

    athought "Instead I've spent twenty minutes watching my hands shake and trying to remember when they started doing that."

    #show aeron balcony_tense with dissolve

    "The briefing went fine. Sector 4 evac, clean extraction, zero casualties. Everyone said the right things afterward."

    athought "Good work. Solid command. The old Selene would be proud."

    athought "None of them saw my pulse spiking on the med-band."

    athought "None of them heard the static in my head when I gave the order to move."

    athought "I keep waiting for the moment I give an order and nothing comes out."

    athought "Or worse - the wrong thing comes out. My father's voice instead of mine."

    # --- LYRA ENTERS ---

    # VISUAL: Door behind him opens. Soft footsteps. Lyra silhouetted in the doorway.
    # CAMERA: Over-shoulder from Aeron's POV, then reverse to her face.

    #play sound "sfx/door_hiss_soft.ogg"

    l "You missed dinner."

    athought "Lyra's voice is quiet, but it carries. It always does."

    athought "Something about the way she shapes words. Like each one is a small ceremony."

    #show lyra balcony_soft with dissolve

    a "Wasn't hungry."

    l "That's not why I'm here."

    "She moves to the railing beside him. Close enough that he can feel the warmth of her shoulder. Not touching. Deliberate."

    l "Your hands."

    athought "I'm still gripping the rail. I force my fingers to relax."

    athought "They don't quite obey."

    a "It's nothing. Just... residual."

    l "Residual from what?"

    a "Everything. Take your pick."

    "She doesn't push. Instead, she turns to face the city, her profile lit by the distant amber glow of the lower tiers."

    # --- LYRA'S OFFER ---

    l "When I was young, the Order taught us a breathing exercise."

    l "They said it brought you closer to the hum - the divine frequency beneath all things."

    a "And you believed that?"

    l "I believed it worked. I still do."

    "She turns to face him. Her eyes are steady, but there's something beneath the calm. Something that looks almost like hope."

    l "It won't fix anything. But it might quiet the noise long enough for you to hear yourself again."

    # --- CHOICE: ACCEPT OR DEFLECT ---

    menu:
        "Her hand hovers near his on the railing. An offer, not a demand."

        "Let her try.":
            $ choice_and_dev(
                _current_scene_id, "_accept_breathing", "EMP", factor=1,
                next_scene_label=None,
                note="Accepting help; vulnerability. Opens breathing exercise path."
            )
            jump .accept_breathing

        "I'm fine, really.":
            $ choice_and_dev(
                _current_scene_id, "_deflect_soft", "EMP", factor=0,
                next_scene_label=None,
                note="Deflection; gentle. She stays anyway. Soft scene end."
            )
            jump .deflect_soft

    # --- BRANCH: DEFLECT ---
    label .deflect_soft:

        a "Lyra, I appreciate it, but I just need a minute. I'll be fine."

        "She studies him for a long moment. Then she nods - not agreement, but acknowledgment."

        l "The offer stands. Whenever you're ready."

        "She doesn't leave. Just turns back to the railing and stands beside him, shoulder almost touching his, watching the city breathe."

        athought "Somehow, that's enough."

        athought "Not fixing. Not pushing. Just... staying."

        $ rel_bump("Lyra", affection=1)

        jump .scene_end_soft

    # --- BRANCH: ACCEPT BREATHING ---
    label .accept_breathing:

        a "Okay."

        athought "The word comes out smaller than I expected."

        athought "She doesn't seem to notice. Or if she does, she doesn't mind."

        l "Turn toward me."

        "He does. The city falls behind her, out of focus."

        athought "All I can see is her face. The soft curve of her jaw. The way her hair catches the wind."

        l "Give me your hands."

        athought "I hesitate. Not because I don't want to - because I do."

        athought "Because the wanting feels dangerous."

        "He gives her his hands anyway."

        # VISUAL: Her fingers cool against his palms. She presses them flat, then curls her own around them.
        # CAMERA: Close on their hands, then slow pull to their faces.

        #show lyra_aeron hands_held_balcony with dissolve

        "Her fingers are cool against his palms. She presses them flat, then curls her own around them, cradling the tremor like it's something worth holding."

        l "Now. Breathe with me."

        # --- THE BREATHING EXERCISE ---

        l "In through the nose. Slow. Four counts."

        "She inhales. He tries to match her rhythm."

        athought "My chest feels tight at first. Resistant."

        l "Hold. Four counts."

        "Her eyes don't leave his."

        athought "I feel pinned. Not trapped - anchored."

        athought "Like she's the only fixed point in a spinning room."

        l "Out through the mouth. Six counts. Let it carry everything that doesn't belong to you."

        "He exhales. Something unknots in his shoulders. Not completely, but enough to notice."

        l "Again."

        "They breathe together. Once. Twice. Three times."

        athought "Each cycle strips away a layer of static."

        athought "Until I can hear my own heartbeat again. Steady. Present. Mine."

        a "...where did you learn this?"

        l "The Order. But they got the reason wrong."

        a "What do you mean?"

        l "They said it was about reaching the divine. Becoming still enough to hear the Cores."

        "Her thumb traces a slow circle on his wrist."

        athought "I don't think she knows she's doing it."

        l "But it was never about stillness. It was about connection."

        l "Matching your breath to someone else's until you remember that you're not alone in it."

        "Her voice drops. The ceremony falls away. What's left is just her - uncertain, sincere, trying."

        l "I didn't understand that until you."

        athought "The static has gone quiet enough that I can feel other things again."

        athought "Her hands on mine. Her breath. The space between us that suddenly feels too small."

        # --- ESCALATION GATE ---

        menu:
            "Her breath is warm against his face. The distance between them has shrunk without him noticing."

            "Stay in this moment.":
                $ choice_and_dev(
                    _current_scene_id, "_stay_gentle", "EMP", factor=0,
                    next_scene_label=None,
                    note="Holding the moment without escalating. Affection gain."
                )
                jump .stay_gentle

            "Close the distance." if trust("Lyra") >= 2 and affection("Lyra") >= 2:
                $ choice_and_dev(
                    _current_scene_id, "_close_distance", "EMP", factor=1,
                    next_scene_label=None,
                    note="Escalation to intimacy. Requires trust and affection thresholds."
                )
                jump .intimacy_gate

    # --- BRANCH: STAY GENTLE ---
    label .stay_gentle:

        athought "I don't move forward. Not because I don't want to."

        athought "Because this - right now - is already more than I knew I needed."

        a "Lyra."

        l "Mm?"

        a "Thank you."

        "She smiles. Small. Almost shy - a crack in the composure she wears like armor."

        l "Don't thank me. Just breathe."

        athought "So I do."

        athought "And for the first time in weeks, the static goes quiet."

        $ rel_bump("Lyra", affection=1)

        jump .scene_end_soft

    # --- BRANCH: INTIMACY GATE (3-Gate Consent Framework) ---
    label .intimacy_gate:

        # CONSENT GATE A: Verbal Cue

        athought "I lean closer. Not all the way - just enough to close the distance by half."

        athought "To let her see the question in my posture before I ask it."

        a "Lyra..."

        l "I know."

        "Her breath catches. Her hands tighten around his."

        a "Is this okay?"

        # CONSENT GATE B: Reciprocal Action

        "She answers by stepping forward, closing the rest of the gap herself."

        "Her forehead rests against his."

        athought "I can feel her pulse through her fingertips. Faster now. Less measured."

        l "I've wanted this. I didn't know how to ask."

        a "You don't have to ask. You just have to tell me if you want me to stop."

        # CONSENT GATE C: Optional Exit Acknowledged

        l "I don't want you to stop."

        "She tilts her head. Her lips brush his - not a kiss yet. A question. A promise of one."

        l "But if I change my mind-"

        a "Then we stop. No questions. No hesitation."

        l "...okay."

        athought "And then she kisses me."

        # VISUAL: The kiss. Tender. Unhurried. The city glows behind them.
        # CAMERA: Slow push to close-up, then pull back to wide as they hold each other.

        #show lyra_aeron kiss_balcony with dissolve
        #play music "music/intimacy_lyra_tender.ogg" fadein 2.0

        # --- INTIMACY SEQUENCE (Fade-to-Warm) ---

        athought "It's not urgent. There's no desperation in it."

        athought "Just warmth. Breath. The slow unspooling of everything I've been carrying alone."

        "Her hands move from his to his jaw, cradling his face like he's something worth steadying."

        "He pulls her closer. She lets him - melts into it, against it."

        athought "Until I can't tell where her pulse ends and mine begins."

        "The kiss deepens. Softens. Eventually settles into something quieter."

        "Foreheads pressed together. Breathing in sync. Two people learning what it means to be held without flinching."

        l "Your hands stopped shaking."

        athought "I look down. She's right."

        a "You did that."

        l "We did that."

        "She pulls back just enough to meet his eyes."

        athought "There's no ceremony left in her expression. Just Lyra."

        athought "Raw. Real. Looking at me like I'm someone worth believing in."

        l "Stay with me tonight? Just... this. Just breathing."

        a "Yeah. I can do that."

        $ metric("lyra_intimacy_level", set_to=max(metric("lyra_intimacy_level"), 1))
        $ rel_bump("Lyra", affection=2)
        $ rel_bump("Lyra", trust=1)
        $ flag("lyra_aftercare", True)
        $ flag("lyra_first_intimate", True)

        jump .scene_end_intimate

    # --- SCENE ENDINGS ---

    label .scene_end_soft:

        # VISUAL: Wide shot - two figures at the railing, city lights below.
        # CAMERA: Slow pull back as wind shifts.

        "The wind shifts, carrying the faint hum of the Ghostline through the rails."

        athought "It sounds almost like music."

        #stop music fadeout 3.0
        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")

        return

    label .scene_end_intimate:

        # VISUAL: Later. Her head on his shoulder. The city lights flicker below.
        # CAMERA: Wide shot - two figures on the balcony, wrapped together against the night.

        athought "Later - much later - I'll remember this as the first night I slept without dreaming of my father's voice."

        athought "The first night the static finally went quiet."

        "She falls asleep first, her head on his shoulder, her breath slow and even against his neck."

        athought "I stay awake a while longer, watching the city lights flicker below, feeling her warmth against my side."

        athought "It's not peace. Not yet."

        athought "But it's close."

        #stop music fadeout 4.0
        #stop ambient fadeout 3.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ flag("breath_of_faith_intimate", True)
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s03_breath_of_faith_emp
# cann.chapter: Act III, Chapter I - Consolidation (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase I, after Council Reborn. Night on the base.
# cann.what_happened:
#   - Aeron is struggling - hands shaking, static in his head, fear of becoming Marcus.
#   - Lyra finds him on the balcony and offers a breathing exercise from her Order training.
#   - Player can deflect (she stays anyway) or accept (breathing exercise).
#   - If accepted and thresholds met, can escalate to first intimacy (consent-gated).
#   - Core revelation: the exercise was never about stillness, it was about connection.
# cann.aeron_state:
#   - EMP struggling - guard cracking, fear of becoming his father, static in his head.
# cann.path_tracking:
#   - EMP baseline. Deflect path adds affection+1. Accept path adds affection+1.
#   - Intimate path adds affection+2, trust+1, sets intimacy_level.
# cann.thematic_flags:
#   - Motifs: Breath (shared rhythm), hands (trembling then still), static vs quiet.
#   - Lyra's reinterpretation of Order teaching - from divine stillness to human connection.
#   - "Your hands stopped shaking." / "We did that." - healing through presence.
#   - The Ghostline hum as ambient music - technology and spirituality blending.
# cann.character_moments:
#   - Lyra: Faith softened into something human. Offering what she has. Vulnerable underneath the calm.
#   - Aeron: Accepting help is harder than giving orders. The wanting feels dangerous.
# cann.block_status:
#   - VARIANT (intimacy optional); requires followup scene load.
# cann.requires_followup:
#   - Next scene: A3_04 Humanitarian Run (Sector 4 Evacuation) or Tessa "Hands Remember."
#   - Lyra's growth here pays off in A3_21 "Faith in Flaws" (prayer scene).
#   - "The static went quiet" - reference point for future Aeron crisis moments.
