# =======================================================
# ACT 3 - Scene 12: The Oath (Obedience Path)
# File: a3_s12_the_oath_ob.rpy
# Path: OB
# Type: NYRA FIRST EROTIC
# Character Focus: Nyra, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s12_the_oath_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s12_the_oath_ob:



    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a3_s12_the_oath_ob")
    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("nyra", to_stage=1, source="a3_s12_the_oath_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm lens (OB formal distance), locked tripod. Opens wide on the quarters --
    #         sparse command space, steel-blue wash. Nyra at the center, kneeling.
    #         Tightens across the ritual: medium two-shot during the pledge,
    #         close-up singles during consent gates. The camera remains deliberate,
    #         composed -- it doesn't drift into warmth. It observes like doctrine.
    #         By the intimacy: the lens doesn't soften. Bodies as architecture, not heat.
    # LIGHTING: Steel-blue overhead strip at 40%. A single amber candle-analog (battery,
    #           military-issue, warm but functional). The candle sits on the desk beside
    #           the fractured Echelon crest. Blue dominates. The amber is an accent, not a mood.
    #           Intimacy: same palette. No warmth bloom. Skin under blue light. The candle
    #           catches the crest's fracture lines.
    # SFX: Loop -- quarters ambient: ventilation hum, distant watch change, structural creak.
    #      One-shots -- fabric on floor (Nyra kneeling), metal set down (the crest),
    #      breath control (hers, practiced), his exhale (the single uncontrolled sound).
    #      The silence between words is ceremonial. Measured.
    # FX/COMP: The fractured Echelon crest: split down the center, held together by wire.
    #          Nyra's uniform pressed and clean. His quarters: cot, desk, tactical displays dark.
    #          The room of someone who commands by default, not design.
    # BLOCKING: Nyra enters. Kneels at the center of the room without being asked.
    #           Aeron at his desk. He doesn't stand immediately -- the delay is the test.
    #           The crest on the floor between them. She placed it before kneeling.
    #           Physical contact initiated by HER through the ritual frame. He permits.
    # CANON: NYRA FIRST EROTIC. The intimacy is framed as ritual -- loyalty made physical.
    #        She eroticizes obedience. He permits because the structure feels safe.
    #        The danger: she's rewriting his doubt as impurity, and it works.
    #        Callbacks: a3_s06 (Request for Alignment), a3_s05 (Echoes in Rain).
    # CONSENT: 3-gate framework, framed as ceremonial exchange.
    #          Gate A: She offers herself (the pledge). Gate B: He accepts (command assent).
    #          Gate C: "If the commander wishes to stop..." (explicit exit).
    # FACE: Nyra -- composed devotion. The reverence is genuine. That makes it dangerous.
    #        Aeron -- mask. But underneath: the hunger for someone who doesn't question.

    # ========= VOICE BASELINE =========
    # OB Aeron: Controlled. Short sentences. Clinical assessment overlaying need.
    #           His internal voice cracks only in the athoughts. The mask holds in dialogue.
    # Nyra: Calm, reverent, precise. Military cadence with liturgical undertone.
    #       She speaks in declarations, not questions. Her certainty IS the seduction.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - NIGHT]
    # Steel-blue light. The quarters of a man who didn't plan to stay.
    # Late. The base is running night-shift skeleton crew.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_cold_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE ARRIVAL ==========

    athought "0200. Reports finished. The base is quiet."

    athought "My hand has been tremoring since 2100. The left one. I keep it flat against the desk."

    athought "It stops when I press hard enough. The pressure converts the tremor into stillness."

    athought "Control through force. The Glass Academy had a name for that. I don't remember it."

    athought "I don't need the name. I need the result."

    #play sound "sfx/door_knock_precise.ogg"

    "Three knocks. Even spacing. The cadence of someone trained to announce without apologizing."

    a "Enter."

    "The door opens. Nyra steps inside. Closes it behind her."

    "She's carrying something wrapped in cloth. Her uniform is pressed, boots polished. Her posture is parade-ground straight."

    athought "She's been awake. Not because she couldn't sleep -- because she was preparing."

    ny "Commander. I request a private audience."

    a "You have it."

    "She doesn't sit. She doesn't approach the desk."

    "She walks to the center of the room. Sets the cloth bundle on the floor. Unwraps it."

    "The Echelon crest. Fractured down the center -- a clean break, held together by a single wrap of copper wire. The metal catches the blue light."

    "Nyra kneels."

    athought "She kneels the way soldiers pray. One knee down, spine straight, chin level. Not supplication -- presentation."

    athought "She planned this. Every angle, every gesture. She's been rehearsing."

    athought "That should make it less genuine. It doesn't."

    # ========== PHASE 2 -- THE PLEDGE ==========

    ny "This crest belonged to my commanding officer. The one I killed."

    ny "I broke it the night we left. One piece for what the Order was supposed to be. One piece for what it became."

    ny "I've carried both halves since."

    athought "She looks at the crest the way Lyra looks at scripture. With love and grief in equal measure."

    ny "I'm not offering you the crest. I'm offering you what it represents."

    a "Which is."

    ny "Order. Discipline. Purpose. The things that make a soldier more than a weapon."

    ny "You hold these things already. You held them before I arrived. I recognized it in the rain -- the way you stood, the way you gave orders that expected obedience because they deserved it."

    athought "She's watching me the way a compass watches north."

    athought "Not with desire. With orientation. I'm the direction she's chosen."

    athought "That's more intoxicating than desire."

    ny "I pledge my service to the order you represent. Not Echelon. Not the rebellion. You."

    ny "My soldiers follow me. I follow you. That chain is unbroken from this moment."

    "She places both hands on the crest. Palms flat. The fracture line runs between her fingers."

    ny "If you accept."

    # --- PLAYER CHOICE ---

    menu:
        "She waits. Spine straight. Eyes level with his chest. The posture of someone who has decided and is now waiting for the world to agree."

        "I accept your oath.":
            $ choice_and_dev(
                _current_scene_id, "_accept_oath", "OB", factor=1,
                next_scene_label=None,
                note="Full acceptance. OB command posture. Opens ritual intimacy path."
            )
            jump .accept_oath

        "I don't need oaths. I need soldiers who think.":
            $ choice_and_dev(
                _current_scene_id, "_tempered_acceptance", "OB", factor=0,
                next_scene_label=None,
                note="Pragmatic response. Still leads to intimacy but through different frame."
            )
            jump .tempered_acceptance

    # --- BRANCH: ACCEPT OATH ---
    label .accept_oath:

        a "I accept your oath."

        "The words come out even. Measured. Commander's cadence."

        athought "Something shifts when I say it. Not in her -- she was already certain."

        athought "In me."

        athought "I've been giving orders since Selene died. But this is different. This is someone choosing to be commanded."

        athought "That's not the same thing as having no choice."

        ny "Then I am yours. In service. In discipline. In purpose."

        "She lifts her hands from the crest. Places them on her thighs. Palms up."

        athought "Palms up. Open. The old Order gesture of total submission to chain of command."

        athought "It shouldn't move me. It's ritual. Choreography."

        athought "It moves me."

        $ rel_bump("Nyra", trust=1)

        jump .ritual_turn

    # --- BRANCH: TEMPERED ACCEPTANCE ---
    label .tempered_acceptance:

        a "I don't need oaths. I need soldiers who think."

        "Nyra doesn't flinch. The slightest shift in her jaw -- recalculating."

        ny "Thinking soldiers still require structure. Without it, thought becomes hesitation and hesitation becomes death."

        ny "I'm not offering blind obedience. I'm offering disciplined loyalty. There is a difference."

        a "Then show me the difference."

        ny "I already am. I'm here. On my knees. Not because you ordered it -- because I chose it."

        athought "She's right. No one told her to come. No one told her to kneel."

        athought "She chose this. That makes it more dangerous than any order."

        $ rel_bump("Nyra", respect=1)

        jump .ritual_turn

    # ========== PHASE 3 -- THE RITUAL TURN ==========
    label .ritual_turn:

        "The room holds. Blue light. The crest between them. Her on her knees. Him at the desk."

        athought "She hasn't moved. Hasn't broken posture. The discipline is absolute."

        athought "And underneath it -- not hidden, not suppressed, just held in parallel with the discipline -- something else."

        athought "I recognize it because I trained to read it. Micro-dilation. Elevated breathing. The flush at the collarbone."

        athought "She's aroused. Not despite the ritual. Because of it."

        ny "There is a second part to the oath."

        a "Go on."

        ny "In the old Order, a pledge of service was sealed physically. Body to body. The discipline made tangible."

        ny "I'm not citing tradition for its own sake. I'm asking because I want to."

        athought "She says 'I want to' the way she says everything -- clearly, directly, without apology."

        athought "No one has said that to me since... since before Selene died."

        athought "Lyra asks. Zira demands. Noelle observes."

        athought "Nyra states."

        # --- CONSENT GATE A: She offers ---

        "Nyra rises from her knees. Slowly. The movement is controlled -- each joint articulating in sequence."

        "She stands. Steps over the crest. Closes the distance to his desk."

        ny "I offer myself. As seal to the oath. As body to the word."

        ny "Not as payment. Not as obligation. As choice."

        "Her hand extends. Palm up. The same gesture -- open, waiting."

        # --- CONSENT GATE B: He accepts ---

        menu:
            "Her hand is steady. Her breathing is even. She's offering everything and demanding nothing."

            "Take her hand.":
                jump .gate_b_accept

            "Not tonight.":
                jump .comfort_variant

        label .gate_b_accept:

        athought "I take her hand."

        "His hand closes around hers. Her fingers tighten -- not a grip. A seal."

        athought "Her skin is warm. Warmer than I expected. The quarters are cold."

        athought "The warmth comes from inside her. Conviction has a temperature."

        a "Accepted."

        "The word is clinical. The way his thumb traces the ridge of her knuckles is not."

        ny "Commander."

        "She says it like a prayer."

        # --- CONSENT GATE C: Explicit exit ---

        ny "If the commander wishes to stop -- at any point, for any reason -- the oath still holds. The service is not contingent on this."

        a "Understood."

        ny "And if I wish to stop?"

        a "Then we stop."

        ny "I won't wish to stop."

        athought "She says it with the certainty of someone who has already decided everything that will happen in this room."

        athought "That should frighten me."

        athought "It doesn't."

    # ========== PHASE 4 -- INTIMATE SEQUENCE ==========

        "She steps closer. Her free hand rises to his collar. Fingers find the top clasp."

        ny "May I?"

        a "Yes."

        "She unfastens it. Precise. Each clasp in order. The way you disassemble a weapon -- methodical, reverent, knowing exactly what each part does."

        athought "Her hands don't shake. Mine would, if I let them."

        athought "I don't let them."

        "Her mouth finds his throat. Not a kiss -- a placement. The oath made physical."

        "His breath catches. The first uncontrolled sound in the room."

        ny "(against his skin) There."

        ny "That's the sound I came for."

        athought "She heard the crack in my discipline. And she's not exploiting it."

        athought "She's celebrating it."

        # [INTIMATE CONTENT HERE]

    # ========== PHASE 5 -- AFTERCARE ==========

        # VISUAL: Later. Same blue light. Same quarters. The candle-analog has burned lower.
        # Nyra sits on the edge of the cot, uniform re-clasped to the collar. Her hair is loose
        # -- the only concession to what happened. Aeron at the desk. Distance re-established.
        # CAMERA: Medium two-shot. The crest is back on the floor between them.

        "The quarters settle. Blue light, steady hum. The candle-analog flickers once and holds."

        "Nyra sits on the cot's edge. Her uniform is re-clasped. Her hair, loose now, falls across one shoulder. She doesn't fix it."

        "The crest lies between them. She picked it up and set it there. Deliberately. The fracture line facing him."

        athought "I'm at the desk. Three feet of cold air between us."

        athought "My hand isn't tremoring. That's the first thing I notice."

        athought "The second thing: I don't know what I feel. The static is quieter, but what's underneath it is unclear."

        "Nyra watches him. Her expression is composed. Content, but not sated -- the difference between a soldier after duty and a person after pleasure."

        ny "You hesitated."

        a "When."

        ny "At the start. When I knelt. Your jaw tightened. You were deciding whether to send me away."

        athought "She's right. I was."

        a "I decided not to."

        ny "You did."

        "She tilts her head. The analytical gesture, but softer. Post-ritual."

        ny "Every hesitation is purified by the choosing."

        a "That sounds like doctrine."

        ny "It is doctrine. Mine."

        athought "She builds scripture from obedience. Each act of submission is a verse."

        athought "Each order I give is a commandment."

        athought "That should terrify me."

        ny "The doubt you carry -- the weight in your jaw, the tremor in your hand, the way you stare at the wall at 0300 --"

        athought "She knows about the tremor. She knows about the insomnia."

        athought "How long has she been watching?"

        ny "Those aren't weaknesses. They're impurities burning away."

        ny "The commander who doubts is the commander who still cares enough to question. When the doubt stops, the doctrine is complete."

        athought "She makes it sound inevitable. A process, not a choice."

        athought "Purification through discipline. Doubt as fuel. Obedience as faith."

        athought "It's seductive. Not sexually -- philosophically."

        athought "And I'm not sure those are different things with her."

        "She stands. Adjusts her hair. The precision returns -- each gesture deliberate, military."

        ny "The oath holds, Commander. Tonight confirmed what I already knew."

        a "And what's that."

        ny "That you are worth following."

        "She collects the crest. Wraps it in its cloth."

        ny "I'll be in Section C if you need me. For anything."

        "The door closes behind her. Precise. No lingering."

        athought "My hand is still."

        athought "The room smells like copper wire and conviction."

        athought "She told me my doubts are impurities burning away."

        athought "I want to believe that more than I should."

        athought "I want to believe her more than I should."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("nyra_first_intimate", True)
    $ rel_bump("Nyra", trust=1, affection=2)
    $ metric("nyra_intimacy_level", set_to=max(metric("nyra_intimacy_level"), 1))
    $ npc_remember("Nyra", "oath_sealed_physically", tone="reverent_certainty")
    $ npc_remember("Aeron", "tremor_stopped_after_nyra", tone="unsettling_relief")
    $ scene_mark(_current_scene_id, "completed")

    return

    # --- COMFORT VARIANT ---
    label .comfort_variant:

        a "Not tonight."

        "Nyra's expression doesn't change. A fraction of recalibration behind her eyes."

        ny "Understood."

        "She withdraws her hand. The gesture is clean -- no wounded pride, no visible disappointment."

        ny "The oath stands regardless. My service doesn't require this."

        a "I know."

        ny "But the offer remains. When the commander is ready."

        athought "When. Not if."

        athought "She's certain I'll accept eventually. That certainty should irritate me."

        athought "It comforts me instead."

        "She collects the crest. Bows. Leaves."

        athought "My hand tremors against the desk."

        athought "I press harder."

        $ rel_bump("Nyra", respect=1)
        $ flag("nyra_oath_deferred", True)
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s12_the_oath_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After Nyra's integration (a3_s06). Several days into the new command structure.
#   - Late night. Aeron's quarters. Private.
# cann.what_happened:
#   - Nyra arrives unannounced with the fractured Echelon crest.
#   - She pledges her service -- not to Phoenix, not to the rebellion. To him.
#   - Player choice: accept the oath fully or temper it with pragmatism.
#   - Ritual frame for intimacy: the oath sealed physically. Old Order tradition.
#   - Consent gates: (A) she offers, (B) he accepts/defers, (C) explicit exit acknowledged.
#   - Intimate path: she eroticizes discipline. "That's the sound I came for."
#   - Aftercare: she reframes his doubt as purification. "Every hesitation is purified by the choosing."
#   - She knows about his tremor and his insomnia. She's been observing.
#   - Comfort variant: he defers. She accepts without complaint. "The offer remains."
# cann.aeron_state:
#   - OB functional. Tremor in left hand (recurring detail). Insomnia.
#   - Permits rather than initiates. The ritual frame makes it feel like command, not vulnerability.
#   - Post-intimate: tremor stops. That unsettling relief is the scene's poison.
#   - Her doctrine is seductive: doubt as impurity, obedience as faith.
# cann.path_tracking:
#   - Accept oath: rel_bump("Nyra", trust=1), routes to ritual intimacy.
#   - Tempered: rel_bump("Nyra", respect=1), same intimacy path but different frame.
#   - Intimate path: flag("nyra_first_intimate"), rel_bump("Nyra", trust=1, affection=2).
#   - Comfort variant: flag("nyra_oath_deferred"), rel_bump("Nyra", respect=1).
# cann.thematic_flags:
#   - The fractured crest: what the Order was vs. what it became. Held together by wire.
#   - Nyra's doctrine: obedience as scripture, submission as verse, command as commandment.
#   - "Every hesitation is purified by the choosing" -- her central theology.
#   - The tremor stopping: physical relief from surrender. The body responds to structure.
#   - Blue light throughout: no warmth bloom. OB intimacy is architecture, not heat.
# cann.character_moments:
#   - Nyra: "I offer myself. As seal to the oath. As body to the word." Genuine, not manipulative.
#     That's what makes her dangerous -- she believes every word.
#   - Aeron: "That should terrify me. It doesn't." -- the OB erosion in real time.
#   - The tremor: his body betrays doubt; her presence suppresses it. Addiction pattern.
# cann.block_status:
#   - VARIANT (intimacy optional). First Nyra erotic on OB path.
# cann.requires_followup:
#   - Tremor suppression: does he seek her out specifically when it starts?
#   - "Impurities burning away" -- Nyra's doctrine should recur and be tested.
#   - Zira's reaction if she learns about this (a3_s15 "Chain of Two").
#   - The crest as recurring object: what happens to it by Act 4?
