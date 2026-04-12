# =======================================================
# ACT 3 - Scene 05: Echoes in the Rain (Obedience Path)
# File: a3_s05_echoes_in_rain_ob.rpy
# Path: OB
# Character Focus: Aeron, Zira, Nyra (first appearance)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s05_echoes_in_rain_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s05_echoes_in_rain_ob:

    # Codex — Nyra's first appearance on the OB path.
    $ codex_mention("nyra", source="a3_s05_echoes_in_rain_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, handheld with controlled drift. Rain on lens. Low angles through rubble.
    #         Wide establishing shots of ruined sector. Close-ups during ambush -- chaos then stillness.
    #         When Nyra's voice cuts through: camera steadies. Center-locked. OB precision returns.
    # LIGHTING: Grey overcast. Rain. Sodium-orange from distant emergency lights.
    #           Shadows move in the ruins. When Nyra appears: single shaft of light. Deliberate.
    # SFX: Loop -- rain on metal, wind through broken structures, distant thunder.
    #      One-shots -- boots on wet concrete, weapons charging, ambush burst, then SILENCE.
    # FX/COMP: Rain particles. Ruined architecture. Fog/mist in low areas.
    #          Nyra's forces in perfect formation -- visual contrast to Phoenix's defensive scramble.
    # BLOCKING: Aeron leads patrol (Zira, plus 2-3 Phoenix fighters). Ambush from multiple angles.
    #           The attack STOPS when Nyra's voice commands. Her troops freeze mid-motion.
    # CANON: This is Nyra's entrance. We see her discipline before we see her face.
    #        The ambush is a test. She wanted to see how Phoenix would react.
    # FACE: Aeron: mask, tactical focus. Zira: alert, angry. Nyra (reveal): calm, absolute.

    # ========= VOICE BASELINE =========
    # Aeron (OB): Tactical. Short commands. Controlled even under fire.
    # Zira: Combat-sharp. Sarcasm compressed to efficiency.
    # Nyra: First appearance. Voice like a blade -- calm, precise, reverent.
    #       Military cadence. No wasted words. She speaks like someone who expects to be obeyed.

    # --- VISUAL SETUP ---
    # [EXT. SECTOR FOUR PERIMETER - RUINED DISTRICT - RAIN - NIGHT]
    # Collapsed buildings. Flooded streets. The bones of a neighborhood Echelon abandoned.
    # Rain falls in sheets. Thunder rolls in the distance. The patrol moves through the dark.

    #scene bg_ruined_sector_rain with dissolve
    #play ambient "sfx/ambient/rain_heavy_urban.ogg" fadein 2.0

    # --- OPENING: THE PATROL ---

    "The rain comes down in sheets. It tastes like rust and ash -- the flavor of forgotten sectors."

    "Aeron moves through the rubble, weapon up, eyes scanning. Behind him: Zira, two Phoenix fighters. A small team. Fast. Disposable if necessary."

    athought "Sector Four. The coordinates from the signal. Whoever they're, they chose this place deliberately."

    athought "Collapsed infrastructure. Limited sightlines. A dozen ambush points in every direction."

    athought "If I were setting a trap, this is where I'd do it."

    #show zira patrol_combat with dissolve

    z "I don't like this."

    a "Noted."

    z "The signal could be bait. Echelon fishing for resistance cells."

    a "Also noted."

    z "You're still walking forward."

    a "Movement reveals intent. Standing still reveals nothing."

    "Zira mutters something under her breath. It sounds like 'suicidal' but the rain swallows the word."

    # --- THE APPROACH ---

    "They pass through what was once a residential block. Windows like empty eye sockets. Doors ripped from hinges."

    "The rain drums on collapsed rooftops. Thunder growls."

    athought "The Ghostline signal originated here. Somewhere in this graveyard of concrete and regret."

    athought "Someone is watching. I can feel it."

    "Zira's hand goes up. Stop signal. The patrol freezes."

    z "Movement. Ten o'clock. Second floor."

    athought "I see it. A shadow that doesn't belong to the rain."

    a "How many?"

    z "One visible. Which means at least four."

    athought "At least."

    "The shadow disappears. Too smooth. Too controlled. Not a scavenger. Not a civilian."

    athought "Military movement. Echelon-trained or better."

    # --- THE AMBUSH ---

    "It happens fast."

    "The first shot sparks off the concrete two feet from Aeron's head. Suppressing fire. Precision placement."

    #play sound "sfx/gunfire_burst_distant.ogg"

    "The patrol scatters. Cover positions. Return fire."

    a "Contact! Multiple hostiles!"

    z "I see six -- no, eight! They have us bracketed!"

    "Muzzle flashes from three directions. Coordinated. Disciplined. No wasted ammunition."

    athought "This isn't a ragged ambush. This is textbook Echelon formation."

    athought "But Echelon doesn't operate in quarantine zones."

    athought "Someone else learned their methods."

    "A Phoenix fighter takes a round to the shoulder. He drops behind rubble, cursing."

    z "We need to move! They're herding us!"

    athought "She's right. The fire is pushing us toward a chokepoint. Kill zone."

    athought "Textbook. Flawless. Beautiful, in a terrible way."

    # --- THE VOICE ---

    "And then -- silence."

    "The gunfire stops. All of it. Simultaneously."

    "The rain keeps falling. Thunder rolls. But the weapons are quiet."

    athought "What--"

    "A voice cuts through the rain. Female. Calm. Absolute."

    unknown_female "Hold."

    "One word. Not shouted. Spoken at conversational volume. And yet it carries."

    "The shadows in the ruins don't move. Don't fire. Don't breathe."

    athought "They stopped. All of them. On a single word."

    athought "That isn't discipline. That's devotion."

    z "What the hell..."

    "Zira's weapon is still up. Her hands are steady, but her eyes are wide."

    z "Who stops an ambush with one word?"

    athought "Someone who commands absolute obedience."

    athought "Someone who has earned it."

    # --- NYRA EMERGES ---

    "She steps out of the rain."

    "No cover. No weapon drawn. Just a woman in a rain-soaked coat, walking toward them like she owns the ruins."

    #show nyra ruins_entrance with dissolve

    "Her hair is dark, slicked back by the rain. Her posture is military -- spine straight, shoulders square. But there's something else."

    "Something in the way she moves. Like a blade being drawn."

    athought "She doesn't fear us. She doesn't fear anything in this alley."

    athought "That confidence is either madness or earned. I'm not certain which is worse."

    "She stops ten feet away. Her eyes find Aeron. They don't waver."

    ny "Phoenix Actual."

    athought "She knows. She knows who I'm."

    ny "I asked who commands now. You came yourself."

    ny "That's either courage or arrogance. I suspect both."

    "Her voice is calm. Precise. Every word placed like a bullet."

    z "Who the hell are you?"

    "The woman's gaze shifts to Zira. Assesses. Dismisses. Returns to Aeron."

    ny "I'm someone who remembers what order means."

    ny "Your signal network is impressive. Ghostline, yes? The architecture is elegant. Chaotic, but elegant."

    ny "Your command structure, however, is collapsing. I could see it in how your patrol moved. Hesitation. Uncertainty."

    ny "You lost someone recently. Someone who held the shape of things."

    athought "She knows about Selene. She has been watching longer than the signal suggested."

    a "You've been observing us."

    ny "I've been waiting. There's a difference."

    ny "Observation is passive. Waiting implies intent."

    a "And what's your intent?"

    "For the first time, something shifts in her expression. Not a smile. Something closer to recognition."

    ny "To serve."

    # --- THE OFFER ---

    ny "My name is Nyra Vale. Former Lieutenant, Order Division. I defected after the Sector Eight purge."

    ny "The soldiers behind me did the same. Seventeen in total. All trained. All disciplined. All looking for something worth obeying."

    athought "Order Division. The enforcement arm. The ones who executed the purges."

    athought "She was one of them. And now she stands in the rain, offering allegiance."

    z "You were Order Division. You killed civilians for compliance quotas."

    ny "Yes."

    "No denial. No justification. Just acknowledgment."

    ny "I followed orders I believed were righteous. When I saw what righteousness had become, I stopped."

    ny "The officer who gave those orders is dead. By my hand. That's all the penance I can offer."

    athought "She killed her commanding officer. That isn't defection. That's execution."

    athought "She chose. Deliberately. Irrevocably."

    a "Why us? Why Phoenix?"

    ny "Because you move like someone who understands control. Not the soft, hesitant compassion the rebellion preaches."

    ny "You move like someone who knows that order isn't the enemy of freedom. Chaos is."

    ny "Selene Ward understood that. Before her, the rebellion was noise. She made it a machine."

    ny "Now she's gone. And the machine is breaking."

    "Her eyes hold his. Steady. Certain."

    ny "I'm here for you, Commander. Not for the rebellion. For you."

    ny "Give me a place in your structure, and I'll give you soldiers who don't hesitate."

    athought "For you. Not for the rebellion."

    athought "That should be a warning. It should concern me."

    athought "It doesn't."

    # --- CHOICE: INITIAL RESPONSE ---

    menu:
        "The rain falls. Her soldiers wait in the shadows. She waits in front of him."

        "Prove it. Your soldiers stand down and return with us. Unarmed.":
            $ choice_and_dev(
                _current_scene_id, "_test", "OB", factor=1,
                next_scene_label=None,
                note="Tests her control. OB commander posture. She complies."
            )
            jump .test_compliance

        "Why should I trust someone who murdered her commanding officer?":
            $ choice_and_dev(
                _current_scene_id, "_challenge", "OB", factor=0,
                next_scene_label=None,
                note="Challenges her directly. She respects the question."
            )
            jump .challenge

        "(Say nothing. Let the silence speak.)":
            $ choice_and_dev(
                _current_scene_id, "_silence", "OB", factor=2,
                next_scene_label=None,
                note="Maximum OB. His silence is the test. She passes it."
            )
            jump .silence_test

    # --- BRANCH: TEST COMPLIANCE ---
    label .test_compliance:

        a "Prove it. Your soldiers stand down and return with us. Unarmed."

        "Her expression doesn't change. No hesitation. No negotiation."

        ny "Done."

        "She turns. Raises one hand. A single gesture."

        "In the ruins, shadows move. One by one, figures emerge. Weapons lowered. Hands visible."

        "They form a line behind her. Perfect spacing. Perfect posture. Silent."

        athought "Seventeen soldiers. All armed moments ago. All ready to kill us."

        athought "One word. One gesture. Complete compliance."

        athought "That isn't military discipline. That's something else."

        z "This is insane. You can't seriously be considering--"

        a "I'm considering."

        z "They tried to kill us five minutes ago!"

        ny "We tested you. There's a difference."

        z "The difference being?"

        ny "You're still alive."

        athought "She's right. If they wanted us dead, we would be dead."

        athought "This was never an ambush. This was an audition."

        $ npc_remember("Nyra", "first_contact", tone="tested_compliance")
        $ rel_bump("Nyra", trust=1, respect=1)
        $ flag("nyra_soldiers_disarmed", True)

        jump .scene_close

    # --- BRANCH: CHALLENGE ---
    label .challenge:

        a "Why should I trust someone who murdered her commanding officer?"

        "Her eyes don't waver. If anything, she seems pleased by the question."

        ny "Because I didn't murder him. I executed him."

        ny "Murder is chaos. Execution is order. He gave orders that violated the principles he swore to uphold."

        ny "When the structure fails, someone must restore it. Even if the cost is high."

        athought "She isn't justifying. She's explaining. There's a difference."

        athought "She believes every word. That's either admirable or terrifying."

        a "And if I give orders you consider violations?"

        ny "Then I'll tell you. Directly. Before acting."

        ny "I'm not offering blind obedience. I'm offering disciplined service. They aren't the same."

        athought "Disciplined service. She wants a structure she can believe in."

        athought "She wants what I want."

        athought "That should concern me. It doesn't."

        $ npc_remember("Nyra", "first_contact", tone="challenged")
        $ rel_bump("Nyra", respect=2)

        jump .scene_close

    # --- BRANCH: SILENCE TEST ---
    label .silence_test:

        "He doesn't answer. The rain falls. The silence stretches."

        "Zira shifts uncomfortably. The Phoenix fighters exchange glances."

        "Nyra doesn't move. Doesn't speak. She waits."

        athought "She asked a question. She made an offer. Now she waits for judgment."

        athought "Most people fill silence with noise. Justifications. Pleading. Desperation."

        athought "She does none of these things."

        athought "She understands that silence is an answer."

        "Ten seconds. Twenty. Thirty."

        "Finally, something shifts in her expression. Not impatience. Recognition."

        ny "You test like they trained us to test."

        ny "Silence reveals more than questions. You wanted to see if I'd break."

        ny "I don't break, Commander. Not anymore."

        athought "She passed."

        athought "I didn't realize I was testing her until she named it."

        athought "That's either perceptive or dangerous. Perhaps both."

        a "Your soldiers. With us. Now."

        ny "Yes, Commander."

        "She turns. The hand rises. The shadows comply."

        $ npc_remember("Nyra", "first_contact", tone="silence_test")
        $ rel_bump("Nyra", trust=1, respect=1, devotion=1)
        $ flag("nyra_recognized_test", True)

        jump .scene_close

    # --- SCENE CLOSE ---
    label .scene_close:

        # VISUAL: The rain continues. Nyra's soldiers fall in. The patrol becomes a procession.

        "They move through the ruins together. Phoenix and Order. Rebellion and defectors."

        "Nyra walks beside Aeron. Not behind. Not ahead. Beside."

        "Her soldiers follow in perfect formation. Silent. Obedient. Waiting."

        athought "Who commands now."

        athought "She asked that question. Now she has her answer."

        athought "I do."

        athought "And she's the first person since Selene died who seems to believe it."

        z "Aeron."

        "Zira's voice is low. Private."

        z "I don't trust her."

        a "You don't have to."

        z "That isn't reassuring."

        a "It isn't meant to be."

        "The rain falls. The procession moves. Somewhere ahead, the base waits."

        "Somewhere behind, the signal that asked 'who commands now' has been answered."

        athought "The Order remembers what the rebellion has forgotten."

        athought "I'm beginning to understand what she meant."

        # --- END ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")
        $ flag("nyra_first_contact", True)

        return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s05_echoes_in_rain_ob
# cann.chapter: Act 3
# cann.chapter_start: False
# cann.when_in_timeline: Night after "Who Commands Now?" -- the patrol to investigate.
# cann.what_happened:
#   - Patrol to Sector Four to investigate the Ghostline signal.
#   - Ambush by disciplined ex-Echelon forces. Textbook tactics.
#   - The ambush STOPS on Nyra's single word: "Hold."
#   - Nyra emerges. Introduces herself. Former Order Division lieutenant.
#   - She offers her soldiers -- not to the rebellion, but to Aeron personally.
#   - Player choice: test her compliance, challenge her, or use silence.
#   - All paths end with her soldiers joining the return to base.
# cann.aeron_state:
#   - OB commander fully operational. He recognizes discipline, respects it.
#   - He isn't alarmed by her offer -- he's interested.
#   - "That should concern me. It doesn't."
# cann.path_tracking:
#   - Test compliance: rel_bump("Nyra", trust=1, respect=1), flag("nyra_soldiers_disarmed")
#   - Challenge: rel_bump("Nyra", respect=2)
#   - Silence: rel_bump("Nyra", trust=1, respect=1, devotion=1), flag("nyra_recognized_test")
# cann.thematic_flags:
#   - The ambush as audition -- she was testing Phoenix, not trying to kill them.
#   - Nyra's devotion = worship of control, not love.
#   - Her soldiers' compliance = the kind of obedience OB Aeron craves.
#   - Zira's distrust foreshadows later conflict.
# cann.character_moments:
#   - Nyra: Voice like a blade. "Hold." stops the entire ambush with one word.
#     "I'm here for you. Not for the rebellion. For you."
#   - Zira: Combat-sharp during ambush. Deeply suspicious afterward.
#     "I don't trust her." / "You don't have to."
#   - Aeron: Recognizes the audition for what it is. Respects it.
# cann.block_status:
#   - ANCHOR (always plays). Choice affects Nyra relationship deltas.
# cann.requires_followup:
#   - "Request for Alignment" -- formal offer at base (next scene).
#   - "Terms of Order" -- debate over Nyra's integration.
#   - Zira "You Don't Get To Break" -- Zira's possessive response to this threat.
