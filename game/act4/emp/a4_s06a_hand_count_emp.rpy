# =======================================================
# ACT 4 - Scene 06a: The Hand Count (Empathy Path)
# File: a4_s06a_hand_count_emp.rpy
# Type: TESSA THESIS BEAT — the count witnessed
# Matrix: Tessa × Aeron. The fifteen-year ritual is heard for the first time.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s06a_hand_count_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s06a_hand_count_emp:
    $ show_timeline("3rd of Glass, 390 A.C.", "05:18", "Phoenix Secondary Base — Medbay")

    # Codex stage bumps
    $ codex_reveal("tessa", to_stage=4, source="a4_s06a_hand_count_emp")
    $ codex_reveal("rhea_kael", to_stage=2, source="a4_s06a_hand_count_emp")
    $ codex_unlock("the_hand_count", source="a4_s06a_hand_count_emp")
    $ codex_unlock("ward_nine_blackout", source="a4_s06a_hand_count_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. The medbay before any shift personnel arrive. Open
    #         on the door from Aeron's side of the corridor. He's
    #         twelve minutes early. The camera is at his shoulder for
    #         the approach, eye-level for the arrival, and stays in
    #         the doorway for the full first phase. It does not
    #         enter the medbay until he does. He does not enter for
    #         a long time.
    #         The medbay is in pre-shift configuration: overhead lit
    #         at half, supply carts staged, board updated for the
    #         morning brief. Tessa is at the supply cart with her
    #         back to the door. Her sleeves are rolled. The camera
    #         registers the rolled sleeves before it registers
    #         anything else; Aeron has not seen her sleeves rolled
    #         before.
    #         When Aeron eventually enters: the camera follows him
    #         to the empty bed near the door. It does not push to
    #         Tessa. It holds the wide.
    #         When Tessa turns: the camera finally finds her face.
    #         Medium two-shot for the final exchange. No tight
    #         singles. The scene refuses the easy intimacy of a
    #         single.
    # LIGHTING: Pre-shift medbay. Overheads at half (3200K, warm).
    #           Supply cart lamp (4000K, neutral) — Tessa's working
    #           light. The board's wall-mounted strip is on. The
    #           rest of the medbay is in cool dimness. The light
    #           does not change across the scene.
    # SFX: Ventilation hum. The supply cart's faint metal-on-metal
    #      as Tessa restocks. Her voice — low, measured, paced. No
    #      music. The count is the audio anchor for Phases 2-5.
    #      No music after the count either. The scene does not
    #      score itself.
    # FACE: Tessa — pre-shift face. The face she has every dawn.
    #        Not performing for anyone because no one is here. When
    #        she realizes Aeron is in the doorway, the face does
    #        not change much. The face she has used at her own
    #        bedside-vigil for fifteen years is not interruptible
    #        by an audience.
    #        Aeron — caught. He arrived early because he wanted to
    #        see her. He is finding something else. He recognizes,
    #        in the part of his head that does the recognizing
    #        before language, that he is not supposed to interrupt.
    # BLOCKING: Tessa at the supply cart, back to the door, sleeves
    #           rolled, restocking the morning trauma kit. She is
    #           saying the count to herself the same way she has
    #           said it every dawn for fifteen years. She does not
    #           hear Aeron arrive at the door. She does hear him
    #           when he reacts to a name. She does not turn.
    #           Aeron stays in the doorway through the count. After
    #           she stops on his name, he steps in, sits on the
    #           edge of the empty bed nearest the door, and waits.
    #           Tessa turns to face him only when she is ready.
    #           The scar on her left forearm is visible from then
    #           on.

    # ========= VOICE BASELINE =========
    # Tessa: medic register, dawn-private. Body-truth as default
    #        grammar. Clinical because clinical is how she has
    #        survived this for fifteen years. The count cadence is
    #        Name. Last truth her hands knew. One detail, sometimes
    #        two, rarely three.
    # Aeron: spare. He says four things across the scene. One of
    #        them is the question that makes the scene what it is.
    # Narrator: stays out of it. The count is the scene's voice.

    # scene bg_medbay_predawn with dissolve
    # play ambient "sfx/ambient/medbay_predawn_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE DOORWAY ==========

    # CAMERA: 50mm. Held wide on the corridor outside
    #         the medbay. Aeron arrives at the door,
    #         finds it open at half. Lights low. He
    #         stops at the threshold.
    # SFX: corridor's distant pre-shift ambient. Inside
    #      the medbay, the supply cart's faint metal
    #      sound. Tessa's voice — low enough that the
    #      first words don't resolve.

    "The corridor outside the medbay is at second-shift quiet. The base hasn't woken yet. Aeron's bootfall is the only sound."

    "He's twelve minutes early."

    athought "Selene's briefing ran short. The walking-toward-Tessa happened on its own."

    "He reaches the medbay door. The door is open at half. The lights inside are low. Tessa's at the supply cart, back to him, sleeves rolled."

    athought "She rolls her sleeves down before the day-shift arrives. I've never seen them rolled."

    "He stops at the threshold."

    "She's saying something. The words are too low to catch from the doorway."

    "He listens."

    # ========== PHASE 2 — THE INHERITANCE ==========

    # CAMERA: holds in the doorway. Aeron at the
    #         threshold. The camera does not move into
    #         the medbay. Tessa's back, the supply cart
    #         lamp, the board wall behind her. Her
    #         voice resolves as the audio settles.
    # SFX: the count begins.

    te "Maren Holt. Didn't reach."

    "A pause. Restock motion. A vial placed in the kit."

    te "Siva Renn. Didn't reach."

    "Another pause. Another vial."

    te "Alo Corren. Didn't reach."

    athought "Three names. None of ours."

    athought "She is praying."

    athought "No."

    "Her cadence is wrong for prayer. The pauses are diagnostic-length. The phrasing is short the way her chart-notes are short."

    athought "She isn't praying. She's working."

    # ========== PHASE 3 — RHEA ==========

    # CAMERA: same wide. The fourth name lands.
    # SFX: Tessa's voice unchanged. The pause before
    #      this entry is fractionally longer.

    te "Rhea Kael. Left hand. Burned brace. Breath shallow."

    "Aeron's hand finds the doorframe."

    athought "Kael."

    athought "Her surname."

    "His fingers don't tighten on the frame. They just find it."

    # ========== PHASE 4 — THE COUNT ==========

    # CAMERA: still wide. Still doorway. The count
    #         continues. Aeron does not move.
    # SFX: the entries land in sequence. The pauses
    #      stay diagnostic-length. The supply cart
    #      lamp glows. The board's wall-strip glows.

    te "Mira Donal. Pulse two beats slow. Eyes closed."

    te "Kesh Arden. Right shoulder. Bleed under the cloth."

    te "Joren Ulle. Femoral. Couldn't pack it fast enough."

    "Names he doesn't recognize. Tessa's voice flat. Body-truth as bookkeeping."

    te "Ash Petren. No breath at the second check."

    te "Velia Renth. Pulse under two fingers. Lost at dawn."

    athought "There are a lot of these."

    "A pause longer than the others. Tessa moves a tray. The metal is the only sound for three seconds."

    te "Torin Vell. Two fingers. Pulse gone."

    athought "Torin. The mercy at the convoy outpost."

    "He registers the name as a thing he knows. He doesn't react. The doorway holds."

    te "Nira Hess. Internal bleed. Hands cold by the third hour."

    te "Joran Tev. Chest wound. Still warm."

    athought "Joran."

    "Joran was three weeks ago. The vigil. The board entry."

    te "Davel Ostra. Right hand. Asked for water."

    athought "Davel."

    "Davel was last week. Aeron was at the bedside for the last hour."

    "Tessa's voice keeps moving. The count doesn't accelerate. The count doesn't slow. The cadence has been the same since Maren Holt."

    te "Liora Rylan. Breath held. Breath returned."

    "Aeron makes a small sound. A breath that catches in the wrong place."

    # ========== PHASE 5 — SHE HEARS HIM ==========

    # CAMERA: still doorway. Tessa's hands stop.
    # SFX: the supply cart goes silent. Tessa does
    #      not turn. The next pause is longer than
    #      diagnostic.

    "Tessa's hands stop on the cart."

    "She doesn't turn."

    "Three seconds."

    "Four."

    "Five."

    "She continues."

    te "Aeron Rylan—"

    "She stops."

    "The cart is silent. The medbay is silent. The board's strip glows. The supply cart lamp glows. Tessa's back is still to the door."

    # ========== PHASE 6 — YOU CAN FINISH IT ==========

    # CAMERA: holds. Aeron in the doorway. Tessa at the
    #         cart. Neither moves for a long count.
    # SFX: ventilation. Nothing else.

    "Aeron speaks."

    a "You can finish it."

    "Tessa does not turn."

    te "No."

    "A beat."

    te "Not while you're standing there."

    "Aeron does not push."

    "He steps into the medbay."

    "The threshold he has been holding is behind him now. He sits on the edge of the empty bed nearest the door — the one she keeps cleared for triage walk-ins. He puts his hands on his knees. He waits."

    "Tessa does not turn yet."

    "She finishes the count in her head. Her lips move once near the end. Aeron does not try to read them."

    "When she's done, she sets the last vial in the kit. She closes the kit's lid. She wipes her hands on the cloth at her hip — the cloth she keeps tucked into the apron strap, white with three small rust stains she has never bleached out."

    "She turns."

    # ========== PHASE 7 — THE SCAR ==========

    # CAMERA: medium two-shot. Tessa standing at the
    #         cart, facing him. Aeron seated on the
    #         bed, facing her. Her sleeves are still
    #         rolled. Her left forearm is in the
    #         supply cart lamp's light.
    # FACE: Tessa — the face she has at her bedside.
    #        Not the medbay face. The face from before
    #        she was a medic.
    #        Aeron — receiving.

    "Her sleeves are still rolled. She has not pulled them down."

    "On the inside of her left forearm, lower third, two thumbprints' worth of paler skin. Old. Well-healed. Slightly raised."

    "Aeron sees it."

    "He does not look away from it. He does not stare at it. He sees it the way she taught him at Sector-10 to look at a wound — directly, briefly, without performing the looking."

    "Her eyes track his eyes. She knows what he saw."

    "She does not pull the sleeves down."

    te "Ward-9."

    "One word. The medbay's lighting does not change."

    te "I was fourteen."

    a "Tell me."

    "She tells him."

    # ========== PHASE 8 — RHEA TOLD ==========

    # CAMERA: still medium two-shot. Held throughout.
    #         No cuts to single. The scene refuses to
    #         break the geometry.
    # SFX: ventilation. Tessa's voice. Nothing else.

    te "A support brace buckled. It pinned her chest. The brace had a heat-fail seam that ran hot for the last fifteen minutes she was alive. I held the seam in place because lifting it wasn't a thing my arms could do."

    te "The seam burned through the cloth and the skin. My hand stayed where it was because pain told it to leave."

    te "She had fifteen minutes before the rest of the section came down. I didn't know it was fifteen. I was fourteen. I was holding the brace."

    te "She named three people. People she'd failed to save before Ward-9. Maren. Siva. Alo."

    te "Then she said: *Say who your hands remember. Or the world gets to call them gone.*"

    te "She stopped speaking. The brace came down a few minutes later. She told me to move and I moved."

    "Aeron does not interrupt."

    te "I've been saying her three names every morning for fifteen years. I added Rhea after the convoy pulled me out. I add a name when my hands are the last hands a body knows."

    te "The count is long now."

    a "I heard."

    te "Yes."

    "A beat."

    te "I don't say it to anyone. I don't say it to the bodies. I say it to the room. The room has been every room I've worked in since the convoy."

    te "The medbay is the room now."

    # ========== PHASE 9 — WHAT CATEGORY AM I ==========

    # CAMERA: held two-shot. Aeron seated. Tessa
    #         standing. Her hand has come to rest on
    #         the supply cart, near the kit she just
    #         closed. Her left forearm is still in
    #         the light.
    # FACE: Tessa — neutral. The body-truth voice has
    #        stayed steady through the telling.
    #        Aeron — finding the question.

    "Aeron has been working on a question since he stepped through the doorway."

    "He finds it."

    a "What category am I."

    "Tessa looks at him."

    te "Returned."

    "One word."

    "Aeron breathes once."

    a "Returned."

    te "Yes."

    a "From a forearm gash."

    te "Pulse held."

    "She says it the same way she said it for the others. Body-truth as bookkeeping. The detail is what her hands knew about him at Sector-10."

    a "I didn't know my pulse held."

    te "I did."

    # ========== PHASE 10 — THE CLOSE ==========

    # CAMERA: pulls back to a wide. Tessa at the cart.
    #         Aeron on the bed. The medbay holding
    #         them at the geometry the scene has used
    #         throughout. The board's strip glows.
    #         Pre-shift personnel will arrive in
    #         twenty minutes.
    # LIGHTING: unchanged.

    "She does not pull her sleeves down."

    "She finishes the supply cart restock. She moves to the next cart. He sits on the bed and watches her work."

    "Neither of them speaks for a long count."

    "When the first day-shift bootfall sounds in the corridor, Tessa pulls her sleeves down."

    "Aeron stands."

    "At the door, he turns back."

    a "Tess."

    te "Yes."

    a "Tomorrow."

    te "Tomorrow."

    "He leaves. The door swings closed behind him. Tessa is at the second cart, sleeves down, working."

    "The day-shift arrives."

    "The medbay opens."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("tessa_hand_count_witnessed_emp", True)
    $ flag("tessa_scar_seen_by_aeron_emp", True)
    $ flag("tessa_rhea_named_aloud_emp", True)
    $ flag("tessa_aeron_category_returned_emp", True)
    $ canon_set("tessa.hand_count_witnessed", True)
    $ canon_set("tessa.scar_seen_by_aeron_emp", True)
    $ canon_set("tessa.aeron_count_category", "Returned")
    $ canon_set("tessa.rhea_three_disclosed_aloud", True)
    $ canon_set("tessa.ward_nine_disclosed_to_aeron", True)
    $ canon_set("aeron.knows_hand_count_emp", True)
    $ canon_set("aeron.knows_tessa_burn_scar_emp", True)
    $ rel_bump("Tessa", trust=2)
    $ npc_remember("Tessa", "rhea_three_named_aloud", weight=4)
    $ npc_remember("Tessa", "scar_visible_to_aeron", tone="not_pulled_down")
    $ npc_remember("Tessa", "aeron_categorized_as_returned", tone="gift_named")
    $ npc_remember("Aeron", "heard_the_hand_count", tone="recognition_before_language")
    $ npc_remember("Aeron", "saw_the_burn_scar", tone="received_without_performing")
    $ npc_remember("Aeron", "asked_what_category", tone="ledger_meets_count")
    $ tp_seed("a4.tessa.count_witnessed_continues")
    $ tp_seed("a4.tessa.aeron_in_returned")
    $ tp_seed("a5.tessa.count_continues")
    $ metric("tessa_count_disclosure_witness_count", 1)
    $ scene_mark(_current_scene_id, "completed")
    call li_lore_check("Tessa") from _a4_s06a_lore

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s06a_hand_count_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - 3 Glass 390 AC. Oh-five-eighteen. A week after a4_s06. Aeron has
#     been arriving at the medbay on a regular pre-brief schedule for
#     six weeks. His arrival timing has been consistent. This morning
#     he is twelve minutes early because Selene's briefing ran short
#     and the walking-toward-Tessa happened on its own.
# cann.what_happened:
#   - Tessa is at the supply cart restocking the morning trauma kit
#     before the day-shift arrives. Her sleeves are rolled. Her left
#     forearm is in the supply cart lamp's light. The Ward-9 burn
#     scar is visible.
#   - She is saying the Hand Count — her private fifteen-year ritual.
#     The count opens with her mother's three (Maren Holt, Siva Renn,
#     Alo Corren), continues to Rhea Kael's own entry, and proceeds
#     chronologically through every patient who has died under
#     Tessa's hands.
#   - Aeron arrives at the door during the count. He stops at the
#     threshold. He listens. He recognizes that he is not supposed
#     to interrupt.
#   - He hears the inheritance. He hears Rhea. He hears the names
#     he doesn't recognize. He hears Torin Vell, Joran Tev, Davel
#     Ostra. He hears Liora Rylan and makes a small sound — a breath
#     that catches in the wrong place.
#   - Tessa hears his sound. She does not turn. She finishes the
#     count to where it stops — Aeron Rylan. She stops on his name.
#   - Aeron speaks: "You can finish it." Tessa: "No. Not while you're
#     standing there." Aeron does not push. He steps into the medbay
#     and sits on the empty triage bed. He waits while Tessa
#     finishes the count in her head.
#   - Tessa turns. Her sleeves are still rolled. Aeron sees the
#     scar. She names Ward-9. She tells him about the buckled brace,
#     the heat-fail seam, her mother's last fifteen minutes, the
#     three names her mother gave her, her mother's instruction.
#   - Aeron asks: "What category am I." Tessa: "Returned." The
#     category is the gift. Aeron understands he has been carried
#     in the count not as a death-to-be but as a return.
#   - The count's body-detail for Aeron: pulse held. The detail is
#     what Tessa's hands knew about him at Sector-10 (callback to
#     a3_s20a — the Brand-scar reveal night).
#   - The day-shift arrives. Tessa pulls her sleeves down. Aeron
#     leaves. They agree to continue tomorrow without specifying
#     what tomorrow means.
# cann.tessa_state:
#   - First witness to the Hand Count in fifteen years. The count's
#     fragility — it leaves no trace — is unaltered: she has not
#     written anything down. But the count now has a second person
#     who has heard a portion of it. The portion is small. The
#     witnessing is not.
#   - The burn scar is now visible to Aeron in canon. Tessa's choice
#     not to pull her sleeves down is the scene's deliberate
#     gesture.
#   - Rhea Kael's name has been spoken aloud to Aeron for the first
#     time. The Ward-9 mechanism (brace, burn, fifteen minutes,
#     the three names, the instruction) is now disclosed.
#   - Tessa does NOT disclose that she may be misreading her
#     mother's last words. She still believes the three names were
#     instruction. The misreading remains the wound's generative
#     engine.
# cann.aeron_state:
#   - Hears the Hand Count for the first time. Recognizes it as a
#     working ritual, not a prayer. The recognition is in the part
#     of his head that does the recognizing before language.
#   - Hears his own name in the count and learns that Tessa has
#     been carrying him in the same ritual she carries the dead.
#   - Asks the load-bearing question (What category am I) and
#     receives the answer (Returned). Understands the answer as
#     the gift.
#   - Adds Tessa's count to his Act IV ledger of women's sentences
#     (alongside necessary is not worth it / the rule is for the
#     living / I am not a neutral observer anymore / I needed to
#     know the door existed).
# cann.path_tracking:
#   - EMP path only. Structural twin: a4_s??_tessa_silent_medbay_ob,
#     in which the same dawn arrival happens but the count is
#     silent and Aeron does not know what he did not see.
# cann.thematic_flags:
#   - **The count witnessed.** Tessa's memorial leaves no trace by
#     design. The witnessing is the first time in fifteen years
#     anyone other than Tessa has heard a portion of the count. The
#     count's fragility is unchanged — Aeron does not have the
#     full sequence, the categories, or the body-truths for most
#     entries. But the count is no longer silent of audience.
#   - **The scar uncovered.** Tessa's left forearm scar has been
#     canonical since the agent's research surfaced "the hand that
#     stayed" as a load-bearing nickname. This scene is the first
#     on-screen disclosure. Future medbay scenes where Tessa's
#     left forearm is in frame must respect the scar's visibility
#     state — usually covered, occasionally not.
#   - **The category as gift.** Aeron's "What category am I" is
#     the moment the ledger asks the count where it lives. Tessa's
#     "Returned" is the count granting Aeron a place in the
#     body-record that is not a death. The category is the
#     scene's load-bearing emotional artifact.
#   - **The misreading remains canonical.** Rhea Kael's last words
#     were a confession, not an instruction. Tessa, fourteen, took
#     them as instruction. Tessa does not know she is misreading.
#     This scene does not surface the misreading. The wound's
#     productive power lives in the misreading remaining
#     unexamined.
#   - **Body-truth as bookkeeping.** The count's medical cadence
#     (Name. Last truth her hands knew.) is the scene's vocal
#     register. The discipline is: not poetic. Vital-check on
#     people whose vitals no longer move.
#   - **Sleeves rolled / sleeves down.** Tessa rolls her sleeves
#     for the count and pulls them down for the day-shift. The
#     gesture is canonical from this scene forward. Aeron has
#     learned the gesture's meaning. Future EMP scenes may use
#     the rolled-sleeves cue without explanation; the player
#     will recognize it.
#   - **Mirror to a4_s20c (Last Transmission).** Both scenes are
#     dawn-witnessing scenes for a private ritual that has been
#     running for over a decade. The mirror is structural: in
#     both, the LI's grief is heard for the first time by Aeron;
#     in both, Aeron's response is restraint, not solution. The
#     two scenes operate as twin thesis beats for their LIs.
# cann.character_moments:
#   - Tessa: not turning when she hears Aeron's sound. The
#     not-turning is the scene's first deliberate choice.
#   - Tessa: stopping on Aeron Rylan—. The stopping is the second.
#   - Tessa: not pulling her sleeves down when she turns. The
#     not-pulling-down is the third.
#   - Tessa: telling Ward-9 in the medic register. The clinical
#     vocabulary holding through her own origin story is the
#     fourth.
#   - Tessa: "Returned." One word. The category disclosure.
#   - Aeron: stopping at the threshold. Listening before language.
#   - Aeron: not pushing when she says no.
#   - Aeron: sitting on the triage bed. The body-language of
#     receiving care without being a patient.
#   - Aeron: "What category am I." The question that makes the
#     scene what it is.
#   - Aeron: "Tomorrow." Not asking for a meeting; agreeing to
#     return.
# cann.callbacks:
#   - a2_int_04_tessa_torins_name: Torin Vell as the first
#     canonical rule-of-three. Per this scene, Torin entered the
#     count that night. The entry surfaces here.
#   - a3_int_07_tessa_hands_remember_emp: hands remember as
#     emotional instrument. The instrument is now revealed to be
#     a fifteen-year-running ritual.
#   - a3_int_08_tessa_the_board_emp: the board can hold both
#     columns. The board is the public face. The Hand Count is
#     the private continuation.
#   - a3_s20a_scar_and_steady_emp: Aeron's forearm gash, the
#     Brand reveal. Pulse held is the body-truth Tessa kept from
#     that night. Aeron's count entry is the body-truth said
#     back to him.
#   - a3_s22a_tessa_after_liora_emp: Liora on both columns. Per
#     this scene's count entry — Liora as Returned, breath held /
#     breath returned — Tessa privately carries Liora as
#     not-fully-gone. The judgement is Tessa's; Aeron may or may
#     not ever be told.
#   - a4_s06_tessa_counts_different_emp: the board scene. The
#     Aeron-watches-Tessa-at-pre-dawn pattern is now reframed by
#     this scene — what Aeron has been watching is the public
#     face of a private ritual.
#   - a4_s09b_implant_tessa_emp: Noelle's implant removal. After
#     this scene, Noelle is in the count as Returned (canon set
#     in canon_notes_tessa.md §9).
#   - a4_s08_zira_exit_plan_emp: the Aeron-ledger of women's
#     sentences. Tessa's count joins the ledger. The two
#     infrastructures of memory now touch.
#   - canon_notes_tessa.md §5: scene delivered per spec.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. EMP path only. Tessa's
#     EMP thesis beat. Foundational for: the OB silent-medbay
#     thesis, every subsequent EMP medbay scene where Tessa's
#     sleeves are rolled or down (the gesture is now canonical),
#     the Tessa-Zira Breath-and-Static pair beat (Tessa now
#     enters that scene with one Aeron-witnessing already in her
#     body), and the deepening erotic at a4_s20.
# cann.requires_followup:
#   - The next-day count. Aeron does not have to be there for the
#     next dawn. The default is that Tessa says the count alone
#     the next morning — and on the morning after that, and after
#     that. The witnessing is not a recurring scene. If a future
#     EMP scene needs Aeron to hear the count again, that scene
#     must earn the second hearing.
#   - Aeron's body-detail entry update. After this scene, Tessa
#     may add to Aeron's count entry. The detail Aeron's sound
#     and his question and his not-pushing left in the room is
#     not yet body-truth. It may become body-truth later. If a
#     future EMP scene revises Aeron's count entry, the revision
#     must respect the original *forearm gash. pulse held.*
#     anchor.
#   - The misreading. Canonically unexamined. If the user wants
#     a future scene to surface it, the scene must respect that
#     Tessa's productive power as a medic comes from the
#     misreading. Surfacing it cleanly would deflate the wound.
#     A scene that surfaces it should make the surfacing itself
#     a cost, not a relief.
#   - Other EMP LIs hearing the count. The default is that they
#     do not. Aeron is the first witness; Zira will be the
#     second (partial) in the Breath-and-Static pair beat. No
#     other character should hear the count in the canonical
#     window unless deliberately authored.
#   - The day-shift's relationship to the count. The day-shift
#     does not know. They have never known. They will not know.
#     Future medbay-day-shift scenes should respect that the
#     count's privacy is not a secret being kept from them — it
#     is a thing that has not occurred to them to ask about.
