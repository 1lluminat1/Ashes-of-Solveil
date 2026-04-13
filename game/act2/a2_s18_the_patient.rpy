# =======================================================
# ACT 2 - Scene 18: The Patient
# File: a2_s18_the_patient.rpy
# Pair Anchor: A2_P14 (Tessa x Noelle)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s18_the_patient"
$ scene_mark(_current_scene_id, "entered")

define runner = Character("Runner")

label a2_s18_the_patient:
    $ show_timeline("DAY 15", "03:00", "Phoenix Base — Medbay")

    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("tessa", to_stage=1, source="a2_s18_the_patient")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, handheld with intent. Opens wide on the medbay, narrows to two-shots of Tessa and Noelle.
    #         Push-ins on Noelle when she says something she doesn't understand. Push-ins on Tessa's hands.
    # LIGHTING: Harsh overhead surgical strips (5600K) bleeding into amber practicals (2800K) at the edges.
    #           The patient's cot is the brightest spot. Faces half-lit in the spill.
    # SFX: Loop — rattling breath (the patient), IV drip ticking, generator hum underneath.
    #       One-shots — tray clatter, bandage tear, Noelle's stylus on crystal, monitor flatline warning beep.
    # FX/COMP: Tessa's hands never shake. Noelle's data crystal projects faint readouts onto the wall behind her.
    # BLOCKING/PROPS: Medbay at the new base — cots along one wall, curtain dividers, scavenged monitors.
    #                 Tessa's workstation. Noelle standing at a distance with her crystal, tapping calculations.
    # FACE: Tessa controlled but worn — the composure costs her something visible. Noelle analytical,
    #        increasingly unsettled by a variable she can't account for. Aeron peripheral — this isn't his scene.

    # ========== THE EMERGENCY — EARLY MORNING ==========

    "The shouting starts before dawn."

    "Aeron hears it through the thin wall of whatever they're calling quarters — boots on metal, someone calling for Tessa, the particular urgency that means blood."

    athought "That sound. You learn to read it in the field. Not fear. Worse than fear."
    athought "Need."

    # VISUAL: Medbay. A runner on the cot, shirt cut open, Tessa already working. Noelle at the edge of the room, data crystal pulsing faint blue.
    "By the time he reaches the medbay, Tessa is elbow-deep in the problem."

    "A runner. Young — maybe twenty. Took a fall through a collapsed grate on a supply route. Punctured abdomen, internal bleeding, the kind of injury that kills quietly."

    "Tessa's hands move with the economy of someone who has done this too many times."

    t "(without looking up) Bag him. Saline, not synth — we're out of synth."

    "Lyra is already there, handing supplies, saying nothing. She knows the rhythm."

    # VISUAL: Noelle standing apart, crystal projecting data. Not touching the patient. Observing.
    "Noelle stands three steps back. Her crystal casts pale blue readouts against the wall — vitals, projected blood loss, something that looks like a probability curve."

    n "(quietly, to no one in particular) Hemorrhagic shock. Systolic dropping. Based on current bleed rate and available intervention—"

    t "Don't."

    n "—twelve percent survival probability within the next forty minutes."

    "Tessa's hands don't stop. But her jaw tightens."

    t "I said don't."

    n "The data is relevant to resource allocation. If survival probability is below—"

    t "He's not a probability. He's bleeding."

    # ========== AERON — PERIPHERAL ==========

    "Aeron stands at the doorway. This isn't his. He knows that."

    if empathy_band() == "obedience":
        athought "Twelve percent. Tessa's burning supplies on a twelve percent chance."
        athought "That's not strategy. That's sentiment."
    elif empathy_band() == "empathy":
        athought "She won't let the number be the answer. I know that look."
        athought "I've worn that look."
    else:
        athought "Twelve percent isn't zero. But it's close."

    # ========== THE WORK ==========

    "Twenty minutes pass. The runner's breathing changes — worse, then worse again."

    runner "(barely conscious) ...cold..."

    t "I know. Stay with me."

    "Tessa's hands find the bleeder. Clamps it. Improvises a suture from thread that was never meant for surgery."

    "Noelle watches. Her crystal updates."

    n "Seven percent."

    t "(through her teeth) Then we work in the seven."

    # VISUAL: Noelle's expression shifting. The certainty cracking. Not doubt — confusion. Something doesn't fit her model.
    "Something crosses Noelle's face that Aeron hasn't seen before."

    "Not doubt. Noelle doesn't doubt data. Something else."

    "Curiosity."

    n "You're not following standard triage protocol."

    t "Standard protocol says he's dead already. I don't accept that."

    n "The resource expenditure on a sub-ten-percent case diverts from—"

    t "Noelle."

    "Tessa looks up. For the first time since the runner came in, she stops moving."

    t "Come here."

    "A beat. Noelle doesn't move."

    t "Come. Here."

    # VISUAL: Noelle stepping closer. The gap between them shrinking from three steps to one.
    "Noelle steps forward. Once. Twice. Until she's close enough to see the blood on Tessa's gloves, the sweat on her forehead, the thread between her fingers."

    t "Hold this."

    "She presses a clamp into Noelle's hand. Noelle takes it. Her fingers are steady — she has fine motor control, always has — but there's a hesitation in the rest of her."

    t "Right there. Don't let go."

    n "I'm not trained in—"

    t "You're holding a clamp. That's all I need. Hold it."

    "Noelle holds it."

    # ========== THE TURN ==========

    "Tessa works around Noelle's hand. Suturing. Cauterizing with a repurposed soldering iron."

    "The runner's breathing stabilizes. Not good — but present."

    n "(looking at her crystal, then back at the patient) ...Fourteen percent."

    "Tessa doesn't respond."

    n "Sixteen."

    "Still nothing."

    n "The curve is... it's inverting. That shouldn't—"

    t "Shouldn't what?"

    n "Shouldn't happen. Based on available resources and wound severity, the model projected irreversible decline at minute eighteen. We're at minute thirty-one."

    t "And?"

    n "And he's still here."

    t "Yes."

    n "The model didn't account for—"

    "She stops. Noelle Korr, who quantifies everything, who has a metric for every observable phenomenon in the human condition, stops mid-sentence."

    "Because she doesn't have a word for what she just watched."

    t "(quietly, still working) It's called not giving up on someone, Noelle."
    t "There's no unit for it. But it changes the math every time."

    # ========== THE VIGIL ==========

    "An hour later, the runner is stable. Not safe — stable."

    "Tessa sits on a supply crate, gloves off, hands in her lap. The steadiness is gone now — they're trembling, just slightly, now that the crisis has passed."

    "Noelle stands at her crystal, running the numbers again. And again. And again."

    # VISUAL: Two-shot. Tessa on the crate, Noelle at the wall. The distance between them smaller than it used to be.

    if empathy_band() == "obedience":
        athought "Twelve percent became stable. The math was wrong."
        athought "Or the math was right, and something else was operating."
    elif empathy_band() == "empathy":
        athought "Tessa saved him because she refused to let the number win."
        athought "And Noelle held the clamp. That matters more than she knows."
    else:
        athought "I don't know if that was medicine or stubbornness."
        athought "Maybe it doesn't matter."

    n "(still studying the data) The survival curve deviated by a factor I can't attribute to any single intervention."

    t "That's because it wasn't a single intervention. It was all of them, together, refusing to stop."

    n "That's... not a variable I typically model."

    t "Maybe it should be."

    "Noelle is quiet for a long time. Her stylus hovers over the crystal but doesn't touch it."

    n "I need to create a new parameter."

    t "For what?"

    n "I don't know yet. I'll call it... 'invested persistence beyond statistical justification.'"

    "Tessa laughs. It's tired and raw, but it's real."

    t "Noelle."

    n "Yes?"

    t "You can just call it care."

    # VISUAL: Noelle's expression — not computing, not rejecting. Sitting with a word that doesn't fit her framework.
    #         She doesn't nod. She doesn't argue. She just... holds it. Like the clamp.

    pause 0.8

    n "...Care."

    n "I'll need to operationalize that."

    t "I know you will."

    # ========== SCENE CLOSE ==========

    "The runner sleeps. His breathing is shallow but steady."

    "Tessa checks the sutures one more time, then covers him with a blanket that's too thin for the cold."

    "Noelle saves something to her crystal. She titles the file, pauses, retypes it, pauses again."

    # VISUAL: CU on crystal. File title visible: "Unmodeled Variable — TK"
    # TK = Tessa Korr-adjacent, or To Know — Noelle hasn't decided which.

    "She leaves without saying goodbye. But she walks slower than she came in."

    "In the doorway, she pauses."

    n "(without turning) Tessa."

    t "Hmm?"

    n "Next time the probability is below fifteen percent, call me."

    t "Why?"

    n "Because... the model needs more data on invested persistence."

    "She's gone before Tessa can respond."

    "Tessa looks at the empty doorway. Then at the runner. Then at her hands."

    t "(to herself) Care."

    "She says it like she's diagnosing something. Which, in a way, she is."

    # ========== STATE UPDATES ==========

    $ scene_mark(_current_scene_id, "anchor_seen")
    $ npc_remember("Tessa", "noelle_held_clamp", tone="surprised_warmth")
    $ npc_remember("Noelle", "care_variable_discovered", tone="unsettled_curiosity")
    $ rel_bump("Tessa", trust=1)
    $ rel_bump("Noelle", trust=1)
    # Truth Shard: Noelle operationalizes care as a variable
    $ tp_seed("a2.patient.care_variable")

    $ scene_mark(_current_scene_id, "completed")

    return

# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s18_the_patient
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Early days at the new base (post-Finding Home). First real medical emergency since establishment.
#   - Pair Anchor A2_P14 (Tessa x Noelle) — "The Patient."
# cann.what_happened:
#   - A runner arrives with a punctured abdomen, internal bleeding. Tessa works to save him.
#   - Noelle calculates 12% survival and frames it as a resource allocation question.
#   - Tessa pulls Noelle in physically — makes her hold a clamp — collapsing the distance between data and care.
#   - The runner stabilizes against the model's prediction. Noelle can't account for the deviation.
#   - Noelle creates a new parameter: "invested persistence beyond statistical justification."
#   - Tessa names it for her: "Care."
#   - Noelle asks to be called next time probability drops below 15%.
# cann.aeron_state:
#   - Peripheral observer. This scene belongs to Tessa and Noelle.
#   - EMP: recognizes what Tessa is doing — refusing to let the number be the final word.
#   - OB: notes the resource expenditure but can't deny the result.
# cann.path_tracking:
#   - No empathy choice in this scene — it's observational for Aeron, catalytic for Tessa/Noelle.
#   - Trust +1 for both Tessa and Noelle (witnessing them at their core).
#   - Pair anchor A2_P14 marked as seen.
#   - Truth Shard: tp_seed("a2.patient.care_variable") fires at scene end.
# cann.thematic_flags:
#   - "There's no unit for it. But it changes the math every time." — Scene thesis.
#   - Care as unmodeled variable — seeds Noelle's full arc (Act 2 through Act 4).
#   - Tessa's hands: steady during crisis, shaking after. The cost of composure.
#   - Noelle asking to be called for sub-15% cases — she's not rejecting data, she's expanding the model.
#   - "Invested persistence beyond statistical justification" as Noelle's native language for love.
# cann.character_moments:
#   - Tessa: Most competent and most human simultaneously. Hands steady during crisis, shaking after.
#     Pulls Noelle into the work rather than arguing philosophy — shows rather than tells.
#   - Noelle: Encounters a variable her models don't cover. First crack in the quantification armor.
#     Doesn't reject the data — creates a new category for it. "Care" as a named variable.
#     The beginning of her arc toward emotional understanding.
#   - The "hold this" moment echoes forward: Noelle learning to hold things she can't quantify.
# cann.block_status:
#   - ANCHOR (Pair Anchor A2_P14, both paths).
# cann.requires_followup:
#   - Noelle references "care" parameter in future analysis scenes.
#   - Tessa/Noelle dynamic deepens in Act 3 pair scenes.
#   - Tessa's trembling hands post-crisis should recur in act2_23 (mercy death).
#     Scene does not yet exist — must be written to complete the callback chain.
