# =======================================================
# ACT 3 - Scene 19: Noelle's Revelation (Empathy Path)
# File: a3_s19_noelle_revelation_emp.rpy
# Type: PLOT
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s19_noelle_revelation_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s19_noelle_revelation_emp:

    $ show_timeline("30th of Cipher, 388 A.C.", "09:00", "Phoenix Base — Analysis Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, tripod-locked. Documentary framing — evidence presentation.
    #         Opens on Noelle's terminal: data scrolling. Tightens to her face.
    #         The data projection: wide shot, the team arranged around it.
    #         The signature reveal: push-in on the document. Marcus's name filling the frame.
    #         Reaction shots: singles, quick, restrained. No lingering.
    #         The choice: camera returns to Aeron. Holds.
    # LIGHTING: War room operational lighting — overhead strips at 70%.
    #           Terminal glow on Noelle's face (blue-white, clinical).
    #           The holo-projection: cool blue. The data as light in the room.
    #           When the signature appears: the blue sharpens. Colder.
    # SFX: Loop — war room ambient. Noelle's terminal processing (soft rapid clicks).
    #      One-shots — holo-projection activate, data page scroll, the silence after the signature.
    #      The silence: specific. The sound of five people processing the same thing.
    # FX/COMP: Holo-projection: Echelon logistics manifests. Authorization chains.
    #          Document headers. Sector designations. The bureaucracy of mass murder.
    #          At the top of the chain: a signature. Handwritten. Marcus Rylan.
    # BLOCKING: War room. Full team present. Noelle at her terminal — the presenter.
    #           Selene standing. Lyra seated. Tessa at the edge. Zira leaning against the wall.
    #           Aeron at the table. The data projected between them all.
    # CANON: MAJOR PLOT SCENE. The Purge data revealed. Marcus personally authorized mass murder.
    #        Not chain of command. Not delegation. His signature. Irrefutable.
    #        Three-way choice: broadcast, weaponize, or hold.
    # FACE: Noelle — precise, controlled. She's been assembling this for weeks.
    #        Aeron — the son seeing the father's signature on atrocity.

    # ========= VOICE BASELINE =========
    # EMP cadence but compressed. The warmth is in the restraint, not the language.
    # Noelle: Data-voice. Precise. She lets the evidence speak.
    # Team: Short reactions. No speeches. The data is the speech.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - DAY]

    #scene bg_war_room_emp with dissolve
    #play ambient "sfx/ambient/war_room_operational.ogg" fadein 2.0

    # ========== PHASE 1 — THE ASSEMBLY ==========

    "Noelle called the meeting. She's never called a meeting before."

    "That fact alone puts the room on edge."

    athought "She's been at her terminal for three days. Sleeping in ninety-minute intervals. Eating when Tessa puts food next to her keyboard."

    athought "I asked her twice what she was working on. Both times she said 'not yet.'"

    athought "It's yet."

    "The team files in. Selene takes her position. Lyra sits. Zira leans against the far wall, arms crossed. Tessa stands at the edge, field kit at her hip from force of habit."

    n "I've been assembling data fragments from Echelon's internal systems. Logistics manifests, authorization chains, requisition orders."

    n "The fragments are from different databases — some from the nodes we captured in Sector 11, some from relay intercepts Zira's network pulled, some from encrypted backups I accessed during the counter-strike response."

    n "Individually, each fragment is incomplete. Together, they reconstruct a specific event chain."

    sel "Which event?"

    n "The Purge."

    "The room changes. The air tightens."

    n "Authorization chain for the Sector Nine through Twelve civilian displacement and subsequent elimination order."

    # ========== PHASE 2 — THE DATA ==========

    "Noelle activates the holo-projection. Data fills the air between them."

    #play sound "sfx/one_shot/holo_activate.ogg"

    "Logistics manifests. Troop deployments. Supply rerouting. Medical supply chain diversions. The skeleton of an operation laid bare."

    n "The displacement order was filed as a 'population security realignment.' Standard bureaucratic cover. But the logistics don't match a realignment."

    n "Food lines were cut before the relocation corridors opened. Medical supplies were diverted three days before the stated start date. The timing is sequential — the deprivation was engineered as a precursor."

    sel "They starved them first."

    n "They created conditions under which resistance would be minimal and compliance would appear voluntary."

    athought "Noelle's voice hasn't changed. The same even cadence. The same measured delivery."

    athought "But her hands are shaking. Just the fingertips. She's holding her datapad against her thigh to stop it from showing."

    t "How many?"

    n "The manifests account for seventeen thousand civilians across four sectors. The post-operation census shows a population reduction of six thousand four hundred and twelve."

    t "Six thousand."

    n "Four hundred and twelve."

    "Tessa's correction. The four hundred and twelve matter. Every one of them was a name on someone's board."

    z "Where's the authorization? Logistics manifests are operational documents. They don't prove intent — they prove execution."

    n "I know."

    "She scrolls the projection. Past the manifests. Past the deployment orders. Past the supply chain diversions."

    "A document. Header: ECHELON COMMAND // AUTHORIZATION — TIER 1 // EYES ONLY."

    "At the bottom of the page, below the operational parameters and the sector designations and the timeline and the force allocation: a signature."

    "Handwritten. Not stamped. Not delegated."

    "Marcus Rylan."

    # ========== PHASE 3 — THE SIGNATURE ==========

    athought "His handwriting."

    athought "I know that handwriting. I watched it sign my Academy enrollment. My Glass certification. The letter that transferred me to active duty."

    athought "The same hand."

    athought "The same pen, probably."

    "The room is silent. The holo-projection holds the signature in blue light. It floats in the air between them like an accusation that finally has a name."

    sel "He signed it personally."

    n "Not delegated. Not through subordinates. The authorization chain is three links: the operational planner, the logistics coordinator, and Marcus Rylan. He was the final authority."

    n "There is a fourth signature in the document. Not on the kill order — on the cohort selection. Sector designations, household enumeration, the discriminant function that decided which families went on the list. The countersign reads *Faber, R. — Director, CAD.* My director picked the names. My subject's father signed the paperwork. I was in the room for the early modeling."

    n "I am stating that as fact, not confession. The room can do with it what the room does with it."

    z "That's not a chain of command. That's a chain of three."

    n "By design. Fewer signatories means fewer witnesses. Fewer people who can testify."

    n "He knew what he was authorizing. The document specifies population reduction targets by sector. The language is precise."

    l "He called them targets."

    n "The document does. Yes."

    athought "My father. His name on a page that authorized the murder of six thousand four hundred and twelve people."

    athought "Not a number. Six thousand four hundred and twelve."

    athought "Tessa would say: count them."

    "Selene is standing very still. Her hand is on the table edge. Gripping."

    sel "This is irrefutable?"

    n "The encryption signatures match Echelon's Tier 1 authentication. The document metadata is consistent with the stated timeline. The logistics manifests corroborate every element. Cross-referenced with three independent data sources."

    n "It's irrefutable."

    # ========== PHASE 4 — THE CHOICE ==========

    sel "Then the question is what we do with it."

    z "Burn it into every Ghostline node. Broadcast it. Let the city see what their Commander did."

    l "That exposes Phoenix. If they trace the broadcast source—"

    z "Let them trace it. The truth is worth the risk."

    sel "The truth isn't worth anything if we're dead before it spreads."

    t "And if we hold it — if we wait — more people die in the dark without knowing why."

    "Five faces. Five positions. The data floating between them."

    sel "Aeron."

    athought "She's asking me to decide. Not as co-commander — as Marcus's son."

    athought "Because this is my father's signature. And whatever we do with this information, it starts with what that name means to me."

    menu:
        "The signature hangs in the projection. His father's hand."

        "Broadcast it. The city deserves the truth, whatever it costs us.":
            $ choice_and_dev(
                _current_scene_id, "_broadcast", "EMP", factor=1,
                next_scene_label=None,
                note="Truth over security. Empathy for the city's right to know."
            )
            jump .broadcast

        "Weaponize it. Hold it as leverage until the moment it does the most damage to Echelon.":
            $ choice_and_dev(
                _current_scene_id, "_weaponize", "OB", factor=1,
                next_scene_label=None,
                note="Strategic calculation. The data as tool."
            )
            jump .weaponize

        "Hold it. We're not ready. And the dead aren't served by rushing this.":
            $ choice_and_dev(
                _current_scene_id, "_hold", "EMP", factor=0,
                next_scene_label=None,
                note="Restraint. The pause before signing. Liora's inheritance."
            )
            jump .hold

    # --- BRANCH: BROADCAST ---
    label .broadcast:

        a "Broadcast it."

        "Zira straightens from the wall."

        a "The people in those sectors — the families of the six thousand — they've been told it was a security incident. A regrettable necessity. They deserve to know it was planned. Authorized. Signed."

        z "I can have it on every Ghostline node in twelve hours."

        sel "That puts a target on every relay point in the network."

        a "I know. And they deserve the truth more than we deserve safety."

        athought "Zira nods. Selene doesn't. But she doesn't argue."

        athought "The decision doesn't resolve tonight. It hangs in the room like the projection — visible, heavy, waiting for the mechanism to carry it."

        $ flag("purge_data_broadcast_chosen", True)

        jump .aftermath

    # --- BRANCH: WEAPONIZE ---
    label .weaponize:

        a "Hold it. But not as a secret — as a weapon."

        sel "Explain."

        a "We release it when it does the most structural damage. When Echelon is overextended. When the broadcast hits at a moment they can't contain the response."

        a "The truth isn't less true if we choose when to tell it."

        z "That's cold."

        a "That's tactical. You taught me the difference between honesty and strategy."

        athought "Zira's expression is unreadable. She's calculating. She doesn't like it. But she's not dismissing it."

        sel "I agree. Timing is operational. The data doesn't expire."

        $ flag("purge_data_weaponize_chosen", True)

        jump .aftermath

    # --- BRANCH: HOLD ---
    label .hold:

        a "Hold it."

        z "Hold it for what?"

        a "For long enough to be certain we're using it for the right reason and not just the right moment."

        athought "The pause. My mother's word for it. The half-second before signing."

        athought "I'm using it now."

        a "The dead aren't served by rushing this. And if we release it wrong — if the city sees it as propaganda instead of proof — we lose the truth and the credibility to tell it."

        l "He's right. Truth needs a vessel people trust."

        sel "Then we secure the data. Triple-encrypted. Noelle, you hold the primary. I hold the backup."

        n "Understood."

        $ flag("purge_data_held", True)

        jump .aftermath

    # ========== AFTERMATH ==========
    label .aftermath:

        "The holo-projection dims. Noelle deactivates it. The signature fades from the air."

        "But it doesn't fade from the room."

        n "There's one more element."

        "She pauses. Unusual for Noelle."

        n "The authorization document references a secondary operation. Post-Purge. A containment protocol for individuals with knowledge of the true scope."

        n "The protocol is still active."

        sel "Active as in—"

        n "As in currently being executed. People who know what happened are being quietly eliminated. The Purge didn't end. It's still running."

        athought "Still running."

        athought "Six thousand four hundred and twelve. And counting."

        "The room holds the weight of that."

        "No one has the right words. That's the most honest response available."

        #stop ambient fadeout 3.0
        #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("purge_data_known", True)
    $ flag("marcus_signature_found", True)
    $ npc_remember("Noelle", "assembled_purge_evidence", tone="controlled_tremor")
    $ npc_remember("Selene", "purge_data_revealed_in_war_room", tone="cold_fury")
    $ npc_remember("Zira", "purge_data_broadcast_debate", tone="sharp_impatience")
    $ npc_remember("Lyra", "purge_data_he_called_them_targets", tone="quiet_horror")
    $ npc_remember("Tessa", "purge_data_six_thousand_four_hundred_twelve", tone="counting")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s19_noelle_revelation_emp
# cann.chapter: Act III, Phase III — Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After the letter (s18a). The data Noelle has been assembling.
#   - War room. Full team. The revelation.
# cann.what_happened:
#   - Noelle presents reconstructed Purge data from multiple Echelon sources.
#   - Logistics manifests prove the Purge was engineered: food cut before corridors opened,
#     medical supplies diverted, deprivation as precursor to compliance.
#   - 17,000 displaced. 6,412 killed. Four sectors.
#   - The authorization: Marcus Rylan's personal signature. Three-link chain by design.
#   - Three-way choice: broadcast (truth now), weaponize (truth timed), hold (truth when ready).
#   - Aftermath: Noelle reveals a secondary protocol — people with knowledge of the Purge
#     are being quietly eliminated. The Purge is still running.
# cann.aeron_state:
#   - His father's handwriting on atrocity. The same hand that signed his Academy enrollment.
#   - "The pause" — if hold branch chosen, he's using Liora's inheritance.
#   - The choice is asked of him as Marcus's son, not just as co-commander.
# cann.path_tracking:
#   - Broadcast: EMP factor=1. flag("purge_data_broadcast_chosen").
#   - Weaponize: OB factor=1. flag("purge_data_weaponize_chosen").
#   - Hold: EMP factor=0 (neutral). flag("purge_data_held").
#   - All paths: canon_set("purge_data_known"), flag("marcus_signature_found").
# cann.thematic_flags:
#   - The signature: Marcus's handwriting. Personal. Not delegated. The intimacy of atrocity.
#   - Bureaucracy as murder weapon: "population security realignment." The language of genocide.
#   - Tessa's correction: "Six thousand four hundred and twelve." Every number is a name.
#   - Noelle's hands shaking: the precise woman whose precision can't hold against this.
#   - The Purge is still running: the past is present tense. Active protocol.
#   - "The pause" (hold branch): Liora's inheritance applied to the hardest decision.
# cann.character_moments:
#   - Noelle: Three days of assembly. Ninety-minute sleep intervals. Her hands shake at the
#     fingertips. She hides it. The data is her armor and her wound.
#   - Selene: "That puts a target on every relay point." Commander's calculation. Cold grip on table.
#   - Zira: "Burn it into every Ghostline node." Immediate, fierce, honest.
#   - Lyra: "He called them targets." The horror of language.
#   - Tessa: "Six thousand four hundred and twelve." Counting the dead as care for the dead.
# cann.callbacks:
#   - a3_s09: Echelon Interlude 3 — Purge Calculus. The logistics from inside Echelon.
#   - a3_s12: Corridor op. 206 saved. The scale contrast: 206 vs 6,412.
#   - a3_s18a: The letter. Marcus's pen. The same hand.
#   - a3_s18: The Weight. Selene's fear of becoming Marcus. Here is the proof of what Marcus is.
#   - Tessa's board methodology: counting as moral practice.
# cann.block_status:
#   - PLOT SCENE. Three-way choice. All branches converge to the same aftermath beat.
# cann.requires_followup:
#   - The choice: broadcast/weaponize/hold — affects late Act 3 and Act 4 dynamics.
#   - The Purge still running: active containment protocol. People are dying now.
#   - Marcus's signature: how does this affect the Liora revelation (s20)?
#   - Noelle's emotional state: she held this together. The cracks will show.
#   - flag("marcus_signature_found") gates future confrontation dialogue.
