# =======================================================
# ACT 3 - Scene 13: Proof of Life (Obedience Path)
# File: a3_s13_proof_of_life_ob.rpy
# Path: OB
# Type: LYRA DEEPENING EROTIC
# Character Focus: Lyra, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s13_proof_of_life_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s13_proof_of_life_ob:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a3_s13_proof_of_life_ob")
    $ show_timeline("DAY 31", "22:00", "Phoenix Base — Aeron's Quarters")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm lens (OB detachment), locked tripod. Opens wide on the corridor --
    #         Lyra at his door. Same framing as s02 "Stay With Me" but the angles are
    #         slightly tighter. The gap between shots is narrower. Compression, not closeness.
    #         During consent gates: alternating close-up singles. Her eyes searching.
    #         His face: present but recessed. The camera catches what she's looking for
    #         and doesn't find.
    #         Intimacy: the camera stays clinical. s02 redux but degraded -- same distance,
    #         more desperation. The shot compositions mirror s02 exactly, but the light is wrong.
    # LIGHTING: Same quarters. Same cold 5000K overhead. Same amber desk lamp.
    #           But the lamp has been moved to the far corner. He repositioned it.
    #           The amber reach is shorter now. More of the room is blue.
    #           Intimacy: blue dominant. The amber barely touches them.
    #           Aftercare: lamp off. Only the cold overhead and window city-glow.
    # SFX: Loop -- quarters ambient, colder. The ventilation seems louder.
    #      One-shots -- door hiss, fabric, breathing out of sync (important: they DON'T match).
    #      Her breathing is faster than his. She can't find his rhythm.
    # FX/COMP: The quarters are tidier than s02. More institutional. He's imposed order
    #          on the space. Her disorder (arriving without plan) is the contrast.
    # BLOCKING: Same room, different geometry. In s02, he was at the desk. Now he's standing
    #           at the window. She enters to his back. The distance takes longer to close.
    # CANON: LYRA DEEPENING. Same desperation as s02 but the gap has grown.
    #        She's not sure anymore. Each visit, who he was recedes further.
    #        Callbacks: a3_s02 (Stay With Me), a1_s07 (Balcony), a3_s06 (Lyra's warning about Nyra).
    # CONSENT: 3-gate framework. The consent is genuine but tinged with grief.
    # FACE: Lyra -- the faith that held in s02 is cracking. Not broken. Cracking.
    #        Aeron -- the mask from s02 has solidified. Harder to read. The eyes give less.

    # ========= VOICE BASELINE =========
    # OB Aeron: Fewer words than s02. The clinical cadence has deepened.
    #           He's not unkind. He's efficient. The efficiency IS the unkindness.
    # Lyra: Her faith language is strained. She asks fewer questions because
    #        she's afraid of the answers. Her body reaches before her words do.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - NIGHT]
    # Same room. Different arrangement. Tidier. Colder. Militarized.
    # The lamp has been moved. The cot is made with hospital corners.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_cold_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE RETURN ==========

    "The door hisses. He doesn't turn from the window."

    athought "I know who it is before the footsteps register. The cadence hasn't changed."

    athought "Everything else about her visits has."

    "Lyra stands in the doorway. She's been crying -- not recently, but in the last hour. The traces are in the redness at her lash line, the way her breath comes slightly ragged."

    athought "She came here after crying. Not during."

    athought "In s-- in the first time, she came before the tears had started. She was holding them."

    athought "Now she cries first. Alone. Then comes to me."

    athought "That's the gap. Measured in when she breaks."

    l "I know you're awake."

    a "I'm always awake."

    l "That's not something to be proud of."

    a "It wasn't pride."

    "She steps inside. The door closes."

    "The room is different from last time. The desk is squared. The tactical pads are stacked by size. The lamp -- she notices it immediately."

    l "You moved the light."

    a "It was in my sightline."

    l "It was the only warm thing in here."

    athought "She's not talking about the lamp."

    "She moves toward him. Stops two feet from the window. The city-glow is behind him -- his face in shadow, her face lit."

    l "I keep coming back."

    a "I've noticed."

    l "Do you know why?"

    a "You're looking for something."

    l "I'm looking for you."

    athought "The sentence lands in the room and doesn't bounce. It absorbs."

    athought "She means the version of me she remembers. The one who kissed her on the balcony. The one who chose her."

    athought "I'm not sure that person is available."

    l "Each time I come here, the distance is bigger."

    l "Not the room. Not the space between us. The distance behind your eyes."

    athought "She's perceptive. She always was."

    athought "On the EMP-- on another path, that perception would be a bridge. Here it's a diagnostic."

    athought "She's measuring how much of me is left."

    a "What do you want, Lyra."

    "Not unkind. Efficient."

    l "I need to know you're still in there."

    athought "The same words. Almost exactly the same words as last time."

    athought "But last time there was hope underneath them."

    athought "Now there's something closer to obligation. She promised she wouldn't give up."

    athought "This is her keeping the promise."

    # ========== PHASE 2 -- THE TEST ==========

    "She reaches for his face. Her hand hovers."

    l "Can I?"

    a "Yes."

    "Her palm on his jaw. Cold fingers. She's been outside -- the corridor, or the observation deck. She went somewhere to cry and came here after."

    athought "I feel the pressure of her hand. The temperature differential. The micro-tremor in her fingers."

    athought "I catalogue it. That's what I do now."

    athought "Feel. Catalogue. File."

    l "Say something that isn't a mission brief."

    a "I don't know what you want me to say."

    l "Say what you feel."

    athought "I feel her hand on my face. I feel the window cold at my back. I feel the blue light."

    athought "I don't know if that's feeling or inventory."

    a "I feel your hand."

    "Her breath catches. A sound between relief and grief."

    l "That's what you said last time."

    a "It was true then."

    l "Is it true now?"

    a "It's what I have."

    "Her jaw tightens. She doesn't remove her hand."

    l "I'm losing you."

    a "You haven't lost me."

    l "Prove it."

    # ========== PHASE 3 -- CONSENT GATES ==========

    # Gate check
    if not (trust("Lyra") >= 2 or (trust("Lyra") >= 1 and flag("lis_witnessed_execution"))):
        jump .comfort_variant

    # --- CONSENT GATE A: Verbal Cue ---

    "Her other hand finds his chest. Over the sternum. She presses."

    l "I need this. Not because I want comfort. Because I need evidence."

    l "The man I chose is either in there or he isn't. And I'd rather know."

    athought "Evidence. She's using Noelle's language. Or maybe it was always hers."

    athought "Faith is evidence of things unseen. She told me that once."

    athought "She's running out of faith. So she needs the other kind."

    a "What kind of evidence."

    l "The kind you can't fake."

    # --- CONSENT GATE B: Reciprocal ---

    menu:
        "Her hands are on him. Her eyes are searching. The last of the faith is a wire stretched thin."

        "Stay.":
            $ choice_and_dev(
                _current_scene_id, "_stay", "OB", factor=1,
                next_scene_label=None,
                note="Permits intimacy. OB: same word as s02, different weight."
            )
            jump .intimacy_path

        "I can't prove what you need me to prove.":
            $ choice_and_dev(
                _current_scene_id, "_honest_refusal", "OB", factor=0,
                next_scene_label=None,
                note="Honest admission. Routes to comfort. More devastating than refusal."
            )
            jump .comfort_variant

    # ========== PHASE 4 -- INTIMATE PATH ==========
    label .intimacy_path:

        a "Stay."

        athought "The word comes out the same as last time. Quiet. Controlled."

        athought "But last time there was something underneath it -- a flicker. A want."

        athought "This time it's permission. Clean. Unweighted."

        athought "She hears the difference. I can see it in her face."

        l "Aeron."

        a "I'm here."

        l "Are you?"

        # --- CONSENT GATE C: Explicit exit ---

        l "If you want to stop--"

        a "I know. The same applies."

        l "I know what I want. I've known since the balcony."

        l "I just don't know if what I want still exists."

        athought "She kisses me."

        athought "It's different from last time. Last time she was searching."

        athought "This time she's excavating."

        # VISUAL: The kiss. Desperate but controlled -- her desperation, his control.
        # They're out of sync. Her rhythm is faster. His hands find her waist but the grip
        # is measured. The geometry is the same as s02. The feeling inside it is not.

        "The kiss isn't gentle and it isn't rough. It's determined. The kiss of someone running diagnostics through her mouth."

        "Her hands pull him closer. His hands settle on her waist -- present but not gripping."

        l "Feel me. Please."

        athought "I try."

        athought "I try the way I tried last time. Through the static. Through the numbness."

        athought "Something is there. Underneath. But the depth has changed."

        athought "Last time it was a layer down. Now it's two. Three."

        athought "I'm still reaching. The reach is just longer."

        "She presses against him. Her forehead to his. Breathing hard."

        l "Come back. Come back to me."

        athought "I don't know where I went."

        # [INTIMATE CONTENT HERE]

    # ========== PHASE 5 -- AFTERCARE ==========

        # VISUAL: Later. The lamp is off. He turned it off. The overhead blue and city-glow only.
        # Lyra curled against him -- same position as s02 but she's gripping harder.
        # His arm around her. The gesture is muscle memory, not impulse.
        # CAMERA: Wider than s02. The room feels bigger. They feel smaller in it.

        "The lamp is off. Blue light and city-glow."

        "She's against his chest. Same position. Her grip on his shirt is tighter than before -- knuckles white against the dark fabric."

        athought "She's holding on harder. As if the pressure compensates for what's missing."

        "Her breathing is uneven. Not from exertion. From something else."

        "She's crying."

        "Not loudly. Not dramatically. The quiet crying of someone who found some of what they were looking for and discovered it wasn't enough."

        athought "She's crying."

        athought "I should feel something about that."

        athought "I do feel something. But it's behind glass. Literally. Behind the Glass Academy conditioning and the weight of command and the static that fills the spaces where emotion used to be."

        athought "I feel it the way you feel heat through a wall. Present. Distant."

        l "(very quiet) I felt you."

        athought "The same words."

        l "I think."

        athought "That's new. 'I think.' She added a qualifier."

        athought "Last time she said 'I felt you' and it was uncertain."

        athought "This time she said 'I felt you. I think.' And it's worse."

        "He doesn't respond. His hand moves to her hair. The gesture is automatic -- the way you soothe someone because the action exists in muscle memory."

        "She accepts it. She doesn't examine it."

        l "The gap is bigger."

        a "I know."

        l "I keep coming back and the gap is bigger and I don't know if coming back is making it worse."

        athought "She's asking if her visits are pushing me further away."

        athought "I don't know the answer."

        a "Don't stop coming."

        l "Why."

        a "Because you're the only one who measures the distance."

        "Silence. Her grip loosens. Not releasing -- relenting."

        l "That's not enough."

        a "I know."

        "She presses her face into his chest. The tears are quiet. Steady."

        athought "She'll come back. I know that."

        athought "The question is how many more times before the faith runs out entirely."

        athought "And what happens to me when it does."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1, affection=1)
    $ metric("lyra_intimacy_level", set_to=max(metric("lyra_intimacy_level"), 2))
    $ flag("lyra_ob_deepening_intimate", True)
    $ npc_remember("Lyra", "felt_him_she_thinks", tone="cracking_faith")
    $ npc_remember("Aeron", "gap_is_bigger_lyra_said", tone="registered_not_felt")
    $ scene_mark(_current_scene_id, "completed")

    return

    # --- COMFORT VARIANT ---
    label .comfort_variant:

        a "I can't prove what you need me to prove."

        "The honesty is worse than refusal."

        l "You're not even going to try?"

        a "Trying when I know I'll fail isn't integrity. It's cruelty dressed as effort."

        l "..."

        "She stares at him. The searching stops. Something in her expression closes -- not a door slamming, but a door being gently, deliberately shut."

        l "That's the most honest thing you've said to me in weeks."

        a "I know."

        l "It's also the cruelest."

        "She drops her hand from his face. Steps back."

        l "I'll keep coming. I promised."

        l "But I don't know what I'm coming back to anymore."

        "She leaves."

        athought "The door hisses shut."

        athought "My face is cold where her hand was."

        athought "I should go after her."

        athought "I don't."

        $ rel_bump("Lyra", trust=1)
        $ flag("lyra_ob_comfort_deepening", True)
        $ npc_remember("Lyra", "aeron_admitted_he_cant_prove_it", tone="devastating_honesty")
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s13_proof_of_life_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After "The Oath" (a3_s12). Days into Nyra's integration.
#   - Lyra returns to Aeron's quarters. Same room, widening gap.
# cann.what_happened:
#   - Lyra comes to his quarters again. Same desperation as s02 but degraded.
#   - She's been crying before arriving (in s02 she came before the tears).
#   - The room is tidier, colder, more institutional. He moved the lamp.
#   - "I need to know you're still in there" -- same words, less hope.
#   - Consent gates: genuine but grief-tinged. She needs evidence, not comfort.
#   - Intimate path: same geometry as s02, but the sync is broken.
#     Her rhythm is faster. His grip is measured. They're out of phase.
#   - Aftercare: she cries. "I felt you. I think." -- the qualifier is the wound.
#   - "The gap is bigger." / "Because you're the only one who measures the distance."
#   - Comfort variant: "I can't prove what you need me to prove." Devastating honesty.
# cann.aeron_state:
#   - OB deepened. Feel-catalogue-file cycle. Emotion exists behind glass.
#   - The clinical cadence has solidified since s02. Fewer cracks for Lyra to find.
#   - "Don't stop coming" -- a need he can name but not act on.
# cann.path_tracking:
#   - Stay: rel_bump("Lyra", trust=1, affection=1). Intimacy level 2.
#   - Comfort: rel_bump("Lyra", trust=1). flag("lyra_ob_comfort_deepening").
# cann.thematic_flags:
#   - Mirror structure with s02: same room, same beats, degraded signal.
#   - The lamp moved: the warm thing displaced. Metaphor for his emotional position.
#   - "I felt you. I think." -- the qualifier as the scene's thesis. Uncertainty deepening.
#   - "You're the only one who measures the distance" -- he needs her as instrument, not partner.
#   - Breathing out of sync: deliberate contrast to EMP field sync. OB bodies don't harmonize.
# cann.character_moments:
#   - Lyra: Faith degrading but not dead. "I promised." Obligation replacing desire.
#   - Aeron: "I should feel something about that. I do. But it's behind glass."
#     The Glass Academy name as literal barrier to feeling.
#   - Comfort variant: "Trying when I know I'll fail isn't integrity. It's cruelty dressed as effort."
#     The most OB thing he's said. And the most honest.
# cann.block_status:
#   - VARIANT (intimacy optional). Lyra deepening on OB path.
# cann.requires_followup:
#   - "The gap is bigger" as recurring measurement across future Lyra OB scenes.
#   - Will Lyra stop coming? The limit of her faith is an endgame variable.
#   - The qualifier: "I think" should echo in later scenes, getting longer or disappearing.
#   - Lyra's perception of Nyra's influence: does she connect his changes to Nyra?
