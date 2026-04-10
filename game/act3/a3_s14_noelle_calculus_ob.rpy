# =======================================================
# ACT 3 - Scene 14: Noelle's Calculus (Obedience Path)
# File: a3_s14_noelle_calculus_ob.rpy
# Path: OB
# Type: PLOT
# Character Focus: Noelle, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s14_noelle_calculus_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s14_noelle_calculus_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, tripod-locked. Documentary framing -- evidence presentation.
    #         Opens on Noelle's terminal: data scrolling. Same framing as EMP s19.
    #         The difference: fewer people in the room. Just Noelle and Aeron.
    #         She brought this to him first. Not the team.
    #         Push-in on the signature. Marcus's name. Hold.
    #         The crucial shot: Aeron's face. The NON-reaction. Camera stays on him
    #         for eight full seconds of nothing. Then cuts to Noelle WATCHING the nothing.
    #         Her expression: the real scene.
    # LIGHTING: Data alcove. Noelle's screens -- blue-white clinical.
    #           Overhead strip at 60%. No amber lamp. She didn't turn it on.
    #           The data projection is the only warmth source, and it's cold.
    # SFX: Loop -- data alcove ambient: crystal hum, cooling fans.
    #      One-shots -- data page scroll, the silence after the signature. Terminal processing click.
    #      The dominant sound: his breathing. Unchanged. That's the horror.
    # FX/COMP: Holo-projection: same Echelon logistics manifests as EMP.
    #          Authorization chains. Sector designations. Marcus's handwritten signature.
    #          Noelle's analysis notes overlaid -- her shorthand, her methodology.
    # BLOCKING: Data alcove. Two chairs. Noelle at her terminal. Aeron on the supply crate.
    #           Same positions as the EMP tenderness scene -- but this is its inverse.
    #           No physical contact. The distance between them is the scene.
    # CANON: PLOT. Same Purge data as EMP s19. Marcus's signature on mass murder.
    #        OB Aeron's reaction: clinical. Tactical. He doesn't react because he already filed it.
    #        Noelle watches him NOT react. Something in her calculation breaks.
    #        This is not about the data. This is about what the data reveals about HIM.
    # FACE: Noelle -- controlled until the non-reaction. Then: disturbed.
    #        Aeron -- mask. The mask doesn't slip. That's the point.

    # ========= VOICE BASELINE =========
    # OB Aeron: Minimal. Tactical. He processes the data as operational intelligence.
    #           No emotional register. The flatness is the tell.
    # Noelle: Clinical delivery. But her pauses get longer as she watches him.
    #         By the end, her silence is louder than his.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - DATA ALCOVE - NIGHT]
    # Noelle's workspace. Screens active. Door closed.
    # She sent a message: "Have results. Your eyes first."

    #scene bg_data_alcove_night with dissolve
    #play ambient "sfx/ambient/data_alcove_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE SUMMONS ==========

    athought "Her message was three words. 'Have results. Come.'"

    athought "Noelle doesn't summon. She presents. She archives. She cross-references."

    athought "She doesn't say 'come.'"

    athought "So I came."

    "The data alcove is blue-white. Screens active. Crystal arrays humming at processing load. Noelle is at her terminal, stylus moving in short precise strokes."

    "The supply crate beside her chair is clear. The seat she keeps for him."

    athought "She keeps a seat for me. I've stopped noticing that I notice it."

    "He sits."

    n "I've completed the reconstruction."

    a "The Echelon logistics fragments."

    n "Yes. The data from the Sector Eleven nodes, combined with Zira's relay intercepts and the encrypted backups from the counter-strike."

    n "Individually insufficient. Together, they reconstruct the authorization chain for a specific operation."

    a "Which operation."

    "She pauses. Her stylus stops."

    n "The Purge."

    athought "The Purge."

    athought "Six thousand four hundred and twelve dead across four sectors."

    athought "I know the number. Everyone knows the number. It's the number that made the rebellion possible."

    a "Show me."

    # ========== PHASE 2 -- THE DATA ==========

    "Noelle activates the holo-projection. Data fills the alcove between them."

    #play sound "sfx/one_shot/holo_activate.ogg"

    "Logistics manifests. Troop deployments. Supply rerouting. Medical supply chain diversions. The architecture of an atrocity laid bare in blue light."

    n "The displacement order was filed as a population security realignment. The logistics don't match. Food lines cut before relocation corridors opened. Medical supplies diverted three days early."

    n "The deprivation was engineered as a precursor. Weaken the population before moving them. Reduce resistance capacity."

    athought "Engineered. Systematic. Efficient."

    athought "I recognize the methodology. The Glass Academy teaches optimization frameworks. This is one of them, applied to population reduction."

    n "The authorization chain runs through seven layers of command. Each layer adds a signature. Delegation of responsibility."

    n "But at the top --"

    "She scrolls. The projection shifts. Document headers resolve."

    n "At the top of the chain."

    "A signature. Handwritten. The projection holds it in blue light."

    "Marcus Rylan."

    athought "My father's handwriting."

    athought "I'd recognize it anywhere. The sharp downstroke on the M. The compressed signature of a man who signed too many documents to give each one its full name."

    athought "He signed it the way he signed my school permissions. The same hand. The same pen pressure."

    # ========== PHASE 3 -- THE NON-REACTION ==========

    # VISUAL: Eight seconds. The camera stays on Aeron's face.
    # Nothing changes. No jaw tightening. No breath catch. No dilation.
    # The signature glows blue in the air between them.
    # His face is the same face it was before the data loaded.
    # THEN: cut to Noelle. WATCHING the nothing.

    "The signature hangs in the air."

    athought "Marcus Rylan authorized the Purge. Personally. Not through delegation. Not through chain of command. His signature. His hand."

    athought "Six thousand four hundred and twelve people died because my father wrote his name."

    athought "I process this."

    athought "I file it."

    a "What's the verification confidence?"

    n "Ninety-seven point four percent. The signature matches authenticated samples from three independent sources."

    a "Distribution?"

    n "I brought it to you first. No one else has seen this."

    a "Good. Keep it contained."

    n "Understood."

    athought "Her voice. Something in it shifted. I register the shift without identifying it."

    athought "She expected more. She expected me to -- what? Flinch? Rage? Weep?"

    athought "My father signed the execution order for six thousand people. The data is actionable intelligence."

    athought "What would flinching add?"

    "Noelle's stylus hasn't moved. She's looking at him. Not at the data."

    n "Do you want to see the secondary documents?"

    a "Yes."

    "She scrolls. Supply chain records. Personnel assignments. The mechanical infrastructure of mass death."

    athought "Each document is a decision. Each decision was made by someone who went home afterward and ate dinner."

    athought "My father ate dinner. Every night. At the same table. He carved the meat himself."

    athought "I don't mention this."

    a "What's the tactical value?"

    n "Significant. This is irrefutable proof that the Purge was personally authorized at the highest level. Not systemic -- individual."

    n "If broadcast, it destroys Echelon's narrative that the Purge was a regional command error."

    a "And gives every neutral faction a reason to choose a side."

    n "Correct."

    a "Hold the data. I'll determine distribution timing."

    n "Understood."

    # ========== PHASE 4 -- THE FILING ==========

    # VISUAL: Noelle at her terminal. Her stylus moves once -- a single note.
    # She doesn't add it to the data file. She adds it to a different log.
    # The personal one. The one she doesn't show anyone.
    # Aeron doesn't notice. He's already standing.

    "Aeron stands. The supply crate scrapes."

    a "Good work. The reconstruction is clean."

    n "Thank you."

    a "Let me know if the secondary analysis reveals additional signatures."

    n "I will."

    "He moves toward the door."

    n "Commander."

    "He stops."

    n "You knew."

    athought "The two words sit in the alcove like a dropped instrument."

    a "I suspected."

    n "When?"

    a "The methodology was consistent with his operational style. I recognized the optimization framework in the supply chain diversions two weeks ago."

    n "Two weeks."

    a "Yes."

    n "You've known your father personally authorized the murder of six thousand four hundred and twelve people for two weeks."

    a "I suspected. Now I have confirmation."

    n "And your response is 'what's the tactical value.'"

    athought "Her voice. The shift I registered earlier. I can identify it now."

    athought "Disturbance."

    athought "Not at the data. At me."

    a "My response is appropriate to the context."

    n "Yes. It is."

    "She says it the way she labels anomalous data. Factually. Without agreement."

    "He leaves."

    # ========== PHASE 5 -- NOELLE ALONE ==========

    # VISUAL: The data alcove after he's gone. Noelle at her terminal.
    # The signature still projected. Marcus Rylan in blue light.
    # Her stylus moves. Small strokes. The personal log.
    # CAMERA: Close on her face. The composure holds. But the eyes are wrong.
    # Not sad. Not angry. Recalculating.

    "The door closes. Noelle sits in the blue light."

    "The signature hangs in the air. She doesn't dismiss it."

    "Her stylus moves across the crystal. Not data entry -- annotation. The personal log."

    "She writes one line. Studies it."

    "Deletes it."

    "Writes it again."

    "The alcove hums. The screens pulse. The signature of a mass murderer floats in the air, and the most disturbing thing about the last five minutes wasn't the data."

    "It was the man who looked at it and asked for tactical value."

    "She makes a note. Files it. Closes the log."

    "The screens go to standby."

    "In the dark, the crystal arrays hum to themselves. The data is stored. The analysis is clean."

    "The thing that isn't clean -- the thing she can't file or cross-reference or model -- is the expression on his face when he saw his father's name."

    "Not the expression."

    "The absence of one."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("purge_data_known")
    $ flag("marcus_signature_found", True)
    $ flag("purge_data_contained_aeron", True)
    $ npc_remember("Noelle", "aeron_didnt_react", tone="disturbed")
    $ npc_remember("Noelle", "he_knew_for_two_weeks", tone="recalculating")
    $ npc_remember("Aeron", "purge_data_tactical_value", tone="clinical")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s14_noelle_calculus_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After Nyra's integration. Noelle has been assembling data for weeks.
#   - She brings results to Aeron privately first. Not the team.
# cann.what_happened:
#   - Noelle presents the reconstructed Purge authorization chain.
#   - Marcus Rylan's signature at the top. Personal authorization. Irrefutable.
#   - OB Aeron's reaction: "What's the tactical value." No emotional response.
#   - He reveals he suspected for two weeks. Recognized the optimization framework.
#   - Noelle watches him NOT react. The non-reaction is the scene.
#   - After he leaves: she files a note in her personal log. Writes it, deletes it, writes it again.
#   - The disturbing thing wasn't the data. It was the absence of expression.
#   - No player choice. The lack of reaction IS the scene.
# cann.aeron_state:
#   - OB deep. Process-file-act cycle. His father's signature is actionable intelligence.
#   - He recognized the methodology two weeks ago. He waited for confirmation.
#   - The Glass Academy optimization framework: he can identify it in genocide because he was taught it.
#   - "What would flinching add?" -- the OB thesis in one sentence.
# cann.path_tracking:
#   - No player choices. canon_set("purge_data_known"). flag("marcus_signature_found").
#   - npc_remember("Noelle", "aeron_didnt_react", tone="disturbed").
#   - npc_remember("Noelle", "he_knew_for_two_weeks", tone="recalculating").
# cann.thematic_flags:
#   - The non-reaction as horror: the most disturbing response is no response.
#   - Noelle as the witness: she's not judging him. She's filing. And the filing is wrong.
#   - Same data as EMP s19 but different scene: the data doesn't change. The man looking at it does.
#   - "My father carved the meat himself." -- domestic memory intersecting with atrocity data.
#     The juxtaposition is OB: noted, not felt.
#   - The personal log: Noelle writes, deletes, rewrites. The data she can't clean.
# cann.character_moments:
#   - Noelle: "You knew." Two words that contain the scene's thesis.
#     She expected data to provoke reaction. It didn't. She's recalculating HIM.
#   - Aeron: "I suspected. Now I have confirmation." -- the OB gap between knowing and feeling.
#     He identified his father's methodology from supply chain patterns. Trained to recognize it.
#   - The signature: "The same hand. The same pen pressure." -- school permissions and genocide.
# cann.block_status:
#   - ANCHOR (always plays). No branching. The absence of choice IS the statement.
# cann.requires_followup:
#   - Noelle's personal log: what did she write? This should surface in a3_s16.
#   - "Aeron didn't react" as a thread: Noelle, Lyra, and Tessa will each process this differently.
#   - The tactical deployment of the data: when does Aeron release it? To whom?
#   - The two-week gap: who else suspected? Did Zira intercept the same patterns?
#   - The EMP parallel: in that path, this data shakes the room. Here it was filed.
