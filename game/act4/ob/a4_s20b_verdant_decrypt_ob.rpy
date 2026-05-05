# =======================================================
# ACT 4 - Scene 20b: The Vector (Obedience Path)
# File: a4_s20b_verdant_decrypt_ob.rpy
# Type: NOELLE THESIS BEAT — Protocol Verdant decrypt delivered (OB)
# Matrix: Aeron x Noelle alone. The OB Verdant payoff.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s20b_verdant_decrypt_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s20b_verdant_decrypt_ob:
    $ show_timeline("3rd of Glass, 390 A.C.", "23:10", "Phoenix Base — Data Alcove")

    # Codex stage bumps — note the asymmetry from EMP. Lyra does not rise.
    $ codex_reveal("noelle_korr", to_stage=4, source="a4_s20b_verdant_decrypt_ob")
    $ codex_reveal("aeron_rylan", to_stage=4, source="a4_s20b_verdant_decrypt_ob")
    $ codex_reveal("liora_rylan", to_stage=3, source="a4_s20b_verdant_decrypt_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Same data alcove discipline as a4_s10
    #         and a4_s10a. The alcove door is closed. Status indicator
    #         grey. The primary screen shows the Verdant decrypt header.
    #         The secondary screens carry the cohort indices and the
    #         brass-edged Liora file, the same older-format crystal that
    #         appears in the EMP version. The crystal stand is not
    #         active. There is no Lyra position in the frame. The
    #         composition is two figures, not three. The two-shot is
    #         the scene's geometry.
    #         Coverage is symmetrical — single on Noelle, single on
    #         Aeron, two-shot when the screens become important. No
    #         pulls. No pushes. The camera is operational, like the
    #         meeting.
    # LIGHTING: Drafting setting. Primary screen 80% luminance.
    #           Secondary screens at half. Single cold overhead strip.
    #           The amber lamp on the secondary workstation remains
    #           unplugged — the constant from a4_s10 onwards. No
    #           softening. The room is cold-lit for the entirety of
    #           the scene.
    # SFX: Loop — data alcove ambient at drafting setting. Crystal
    #      arrays at standby. Vent. The keyboard is not active. The
    #      register sound is absent because there is no register
    #      sound to play; the briefing is verbal, and the verbal is
    #      cold. One-shots: door open (Aeron arriving), door close,
    #      the secondary reader chime as Noelle slots the Liora file
    #      crystal. No music bed. No correction sound. The scene
    #      refuses ornament.
    # FACE: Noelle — the OB working register. The face that walked
    #       Aeron out of a4_s10 and audited the crystal in a4_s10a.
    #       Faber's syntax is operational. The Vance signature is the
    #       default. The face is calm in the way a person is calm when
    #       they are running an established procedure. The calm is the
    #       cost.
    #       Aeron — the OB face from a4_s10. The institutional face
    #       plus the additional layer canonized in a4_s10a's parent
    #       scene: the specific stillness of a man receiving a
    #       briefing he has not asked for and will accept on its
    #       merits.
    # BLOCKING: Noelle at the workstation chair, forty-degree angle
    #           preserved from a4_s10. Aeron stands beside the screen
    #           at reading distance. The same standing posture from
    #           the doctrine signature. He does not sit. The reader-
    #           chair Noelle has angled remains empty.

    # ========= VOICE BASELINE =========
    # Noelle: full OB working register. The Vance-default voice. Faber's
    #          syntax tells across all three of her sentence structures.
    #          The voice is precise, ceremonial, cold. The voice does
    #          not crack at any point in the scene. The "Acknowledged"
    #          replaces the EMP "All right." across both speakers.
    # Aeron: the OB ops-room voice. Asset-management framing. Cold trust
    #         of an institution for one of its instruments. He uses
    #         "Commander" or no address; he does not use "Noelle." The
    #         absence of the name is a quiet grief on the OB path; the
    #         scene does not flag the absence. The narration carries it.

    # scene bg_data_alcove_drafting with dissolve
    # play ambient "sfx/ambient/data_alcove_drafting.ogg" fadein 2.0

    # ========== PHASE 1 — THE SUMMONS ==========

    # CAMERA: 50mm. Open on the alcove door, closed.
    #         The status indicator at grey. The shot
    #         holds for two beats before Aeron's
    #         silhouette appears in the corridor side
    #         of the door's frosted half.
    # SFX: corridor ambient through the door. Soft. The
    #      door is the only thing between the corridor
    #      and the alcove and the door is doing the
    #      acoustic work.

    "Noelle's message reaches Aeron at twenty-two-fifty on the secure ops channel. The message is single-recipient. Two lines, the maximum length she allows herself for personal-layer sends."

    "*Decrypt complete. Data alcove. Twenty-three-ten. Alone.*"

    "He reads it twice. The second reading is for the word *alone.* The word indicates a personal-layer briefing. Personal-layer briefings on OB are rare. They are also operationally efficient — they bypass the council distribution and the meeting overhead. The efficiency is the reason the personal-layer order has been preserved in OB doctrine."

    athought "She has not summoned me alone since the doctrine signature. Two weeks. The interval is consistent with the operational tempo of the analyst-cell locator work and would not, in itself, be a flag."

    athought "The word *alone* is the flag. *Alone* says the briefing is calibrated for a single recipient. Calibrated single-recipient briefings on OB are reserved for material that the addressee will need to hear before the council does."

    athought "I am the addressee. The material is calibrated for me. The material is not for the council yet."

    athought "Acknowledged. I am going to the alcove."

    "He sends one line back. *On my way.*"

    "He walks the four corridors between the ops room and the data alcove. Second-shift base. The corridors are quiet. He passes Nyra in the cross-corridor at the third turn. Nyra registers his trajectory without speaking. She does not require a briefing on his trajectory. She has trusted his trajectories without briefing for a month. The trust is operational."

    "He reaches the alcove door. He keys it. The door slides."

    # ========== PHASE 2 — THE TWO-SHOT ==========

    # CAMERA: enters with Aeron. The alcove resolves —
    #         primary screen, two secondaries, the
    #         workstation, Noelle in the chair at her
    #         forty-degree. The composition is two
    #         figures and three screens. The
    #         composition is what it is; the camera
    #         does not push for warmth.

    "The alcove is in its now-familiar configuration. Primary screen at 80%. The Verdant cohort header in pale blue. Two secondary screens, the right-hand one carrying the brass-edged file format, the left-hand one carrying the cohort indices. Noelle at the workstation. The reader-chair angled for an addressee that will not take it."

    "She does not turn when he enters. She finishes the line of metadata annotation she is on. The Noelle rule. The line resolves on the screen as: *VANCE — c/r reviewed.*"

    "She turns."

    n "Commander."

    "She uses the title."

    "The Name Mechanic from a3_s16 is sealed. It has been sealed since the doctrine signature. The seal is not flagged in dialogue. The narration carries it."

    n "Thank you for coming alone."

    a "You said *alone.* I came alone."

    "Five words. The OB-register acknowledgment."

    n "The decrypt is the Verdant package. I have been running it on my locator hardware since the broadcast. It finished an hour ago. I have read it twice. The brief is two movements. I am giving them to you in priority order."

    n "The first movement is your file. The second movement is your mother's. There is a third subject in the document who will not be briefed in this scene. The third subject's relevance is operationally tangential. I am setting the third subject aside."

    "She does not name Lyra. She does not flag the absence. The absence is operational, like the seal on the Name Mechanic. The OB working register does not announce its compressions."

    a "Begin."

    "One word. He has not stepped further into the alcove. He stands beside the screen at reading distance. The same stand from the doctrine signature. The reader-chair remains empty."

    # ========== PHASE 3 — MOVEMENT ONE: WHAT YOU WERE PRESERVED FOR ==========

    # CAMERA: tight on Noelle. Faber-syntax in operation.
    #         The institutional-symmetry sentences. The
    #         scope-narrowing rhetorical move at the
    #         second sentence. Coverage holds tight for
    #         the duration of the movement.
    # LIGHTING: primary screen brightens behind her as
    #           she activates the Aeron-cohort layer.

    n "Protocol Verdant is the regime's bloodline-preservation program. Active for at least thirty years. Its mandate is the identification, monitoring, and preservation of viable Verdant and Ethereal lineages for future Core research applications."

    n "The first subject of the document is you. The decrypt names you as the last viable pure Verdant candidate identified in the city. The candidacy was confirmed at age twelve, on the day your Branding rejected. Inside Protocol Verdant, the rejection was classified as evidence of lineage purity, not failure. The rejection was the pass mark."

    n "Marcus authored the public cover story. The cover was 'fate.' The cover was distributed to the Council, to the academy, to the household. The cover was a lie about a deeper truth."

    n "The deeper truth is that you were preserved as breeding stock. The preservation kept you in a high-visibility command position because the high-visibility position protected you from the disposition pressures that would have degraded lineage viability. Marcus has been protecting your lineage purity since you were twelve. The grooming for command was instrumental. The preservation was the operational goal."

    n "Resonance-compatibility experiments were scheduled for your late twenties. The decrypt names a window of 388 to 391 AC. We are inside the window. The experiments have not happened. Marcus delayed them when you began drifting from Echelon allegiance. The delay was operational, not ideological. He was waiting for you to stabilize."

    "She stops. She watches him."

    "He does not move. The institutional face is intact. The face has had practice."

    athought "The lie was a lie about a deeper truth. The deeper truth is that I was an asset. Marcus has been protecting an asset for nineteen years. The asset is me. The protection has been instrumental."

    athought "I am not surprised by this."

    athought "I should examine the not-being-surprised. The not-surprise is data about me, not about Marcus."

    athought "I am examining it."

    athought "The not-surprise is because the framing is consistent with my own operational understanding of my position. I have been an asset since I was twelve. I have been an asset to Echelon, then to the rebellion, then to my own command structure. The asset position is the position I have always occupied. Marcus knew it. I knew it. The 'fate' lie was the cover that made the asset position legible to me as identity."

    athought "The lie was operationally elegant. I would have used the same cover if I had been Marcus. I would have refined it. The refinement would have been: include a religious component to make the destiny narrative theologically self-reinforcing. Marcus did not include the religious component. The Cathedral handled the religious component for him without explicit briefing. Marcus subcontracted the cover to an independent system. That is more efficient than what I would have designed."

    athought "I am, again, the kind of mind that finds an operational lie elegant."

    athought "Acknowledged."

    "He does not say any of the athought aloud. The aloud version is the response Noelle is waiting for."

    a "The framing is consistent with my operational understanding. The cover was efficient. Marcus has been managing the asset position for nineteen years."

    n "That is the response I anticipated."

    a "Continue."

    n "Acknowledged."

    # ========== PHASE 4 — MOVEMENT TWO: THE LIORA FILE ==========

    # CAMERA: pulls slightly to a two-shot. Noelle and
    #         Aeron in the same frame for the first time
    #         since the alcove entrance. The brass-edged
    #         file resolves on the right-hand secondary
    #         screen as Noelle slots the older crystal.
    # LIGHTING: secondary screen on the right brightens
    #           with the brass-format UI. The pale blue
    #           of the primary recedes by a quarter.

    "Noelle slots the older crystal. The reader chimes. The Liora file resolves — a single personnel record, edged in the brass-tone of pre-380 CAD documents."

    n "Liora Rylan. Your mother. Subject of the second movement."

    n "The decrypt's cohort metadata flagged her three weeks ago — not as a Verdant subject, but as a cataloged escape. The only Verdant-adjacent person on file who left the city undetected and was never re-actioned."

    n "The reason she was never re-actioned is in the file. Faber's countersign protocol. A standing protocol that requires Faber's explicit countersignature on any disposition order against a Verdant-adjacent person on the watch list. Faber has not countersigned a single disposition order against Liora in nineteen years. The Liora file has been flagged for action seventeen separate times across that interval. Each time, the action paperwork has reached Faber's desk and stopped."

    n "Liora is alive. She has been alive the entire time. Faber has been the reason she has not been brought back."

    "She does not name her own seven-month possession of the file. The possession is operationally tangential to the OB framing. The possession is a personal-layer item the OB working register does not require. She files the omission in her private operational log without typing it."

    n "The file is in front of you on the secondary screen. The file includes her last known location as of three years ago — an Outlands settlement the Free Strata cataloged as a story-keeper community. The file is yours."

    "Aeron does not move from the standing position beside the screen. His eyes track the brass-format record. He reads the location string. He reads the activity flag. He reads the protective protocol citation."

    "He does not speak for a count of four."

    "Noelle does not break the count. The count is operational. He is processing intelligence. The processing requires unbroken attention."

    "At the count of four, Aeron speaks."

    a "Hold it."

    "Two words."

    a "We will use it when we need her."

    "Three more."

    "Five total."

    "The five words are the response Noelle anticipated and has not allowed herself to anticipate. The two responses are not the same response. The anticipated response was a tactical filing. The not-anticipated-but-allowed response was a moment of recognition. Aeron has produced the tactical filing. The tactical filing is operationally consistent with his current command tempo. The tactical filing is correct."

    "Noelle's face does not change."

    "Her hand does not move from the workstation edge."

    "Her chest takes one breath, the same breath she has been taking at the same rate for the duration of the brief. The rate does not change."

    n "Acknowledged. I will hold the file in my secure storage. The crystal will remain in the secondary reader for the duration of this session. Upon session close, the crystal will be re-secured to the lower-left drawer. The drawer's audit log will not propagate. The crystal will be available on a single-recipient request from you in the future."

    a "Thank you, Commander."

    "He uses her title."

    "The title is not the Name Mechanic. The Name Mechanic is sealed. The title is what comes through the seal."

    a "The decrypt is now complete?"

    n "Yes. Two movements briefed. The third movement is operationally tangential. The third movement does not require briefing tonight."

    a "Send Selene the operational summary at oh-seven-hundred. Include the Liora file's activity flag and the Faber countersign protocol. Do not include the location string. The location string remains compartmented to this room."

    n "Acknowledged."

    a "Anything else?"

    n "No, Commander."

    # ========== PHASE 5 — THE EXIT ==========

    # CAMERA: pulls back to wide. Aeron at the screen,
    #         Noelle at the workstation, the brass-
    #         edged file glowing on the right-hand
    #         secondary, the cohort indices on the
    #         left, the primary holding the Verdant
    #         header. The composition holds for two
    #         beats. Then Aeron turns toward the door.

    "Aeron turns. The turn is the same turn from the doctrine-signature scene. Three paces, in reverse. The door opens for him. He does not pause at the threshold."

    "He pauses."

    "Not at the threshold. One step before. The pause is half a second. Noelle's eye registers the pause without naming it. The pause is the OB-register equivalent of the not-looking-back the EMP version of him would have done — a thing that wants to register and is not allowed to register and finds a smaller register to occupy."

    "He completes the turn-back. He looks at her once."

    a "Noelle."

    "He uses her name."

    "The Name Mechanic does not activate. The seal holds. But the name has been said. The saying is a small seam. The seam is what the half-second pause produced."

    n "Yes."

    a "The Liora file's existence is a personal-layer item for me. The use of the file is operational. I am noting the distinction. I am noting it because I want you to know I am keeping the distinction in the part of me that keeps distinctions. I am not promising anything about the use. I am noting that the distinction exists."

    "He is reading from the same script the OB working register uses for personal-layer-with-operational-consequences statements. The script is the script. The script is what produced the doctrine."

    "The noting is what the script allows."

    n "Acknowledged."

    "She does not say anything else. The acknowledgment is the closing of the seam."

    "Aeron steps through the threshold. The door closes. The corridor light is gone."

    # ========== PHASE 6 — THE VECTOR ==========

    # CAMERA: hold on Noelle. Single. The brass-edged
    #         file is still on the right-hand secondary
    #         screen. The cohort indices on the left.
    #         The Verdant header on the primary.
    #         Noelle has not moved. The chair is at
    #         forty degrees.
    # LIGHTING: unchanged. Cold drafting. The amber
    #           lamp unplugged.

    "Noelle does not eject the brass-edged crystal."

    "She does not save the session log to the council-distribution channel."

    "She does not draft the oh-seven-hundred summary for Selene yet."

    "She sits."

    "Her hand is on the workstation edge. Her chest takes the same breath at the same rate. The rate has not changed across the brief, the exit, or the silence after."

    "She watches the brass-edged file glow on the right-hand secondary screen for nine seconds. Nine seconds is the maximum interval the OB working register allows for non-task observation. The interval is permitted because the file is technically still in active session and observation of an active-session file is operational. The framing protects the observation."

    "At the count of nine, she returns her eyes to the primary screen."

    nthought "I gave him a person and he took a vector."

    "Eight words."

    "She does not type the sentence. The sentence is in nthought. The sentence does not propagate to any operational layer. The sentence is the kind of sentence that, in the EMP version of this room on a different night, would have been typed in the AUTHOR'S NOTE — INTERNAL section and saved private. The OB version of the sentence does not require a save. The sentence is filed by being thought."

    "She files it."

    nthought "Filed."

    "The OB working register holds. The brief is complete. The summary will be drafted at oh-six-thirty. The crystal will be secured at the end of the session. The Liora file is in operational storage. The asset is logged."

    "Noelle returns to the metadata annotation she was finishing when Aeron entered the alcove. The line resolves on the screen — *VANCE — c/r reviewed* — and she keys the next line beneath it."

    "*VANCE — verdant payoff briefing complete — addressee acknowledged, holding pattern set per operational request — file secured to lower-left drawer at session close.*"

    "She files the line."

    "The base functions."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("verdant_payoff_complete_ob", True)
    $ flag("aeron_protocol_verdant_revealed_ob", True)
    $ flag("liora_file_held_ob", True)
    $ flag("faber_countersign_protocol_revealed", True)
    $ canon_set("aeron.protocol_verdant_status", "preserved_breeding_subject_revealed")
    $ canon_set("aeron.fate_lie_unmasked", True)
    $ canon_set("aeron.has_liora_file_ob", True)
    $ canon_set("aeron.liora_file_filing_ob", "asset_held_for_use")
    $ canon_set("aeron.lyra_placement_revealed", False)
    $ canon_set("noelle.delivered_verdant_payoff_ob", True)
    $ canon_set("noelle.lyra_excluded_from_briefing_ob", True)
    $ canon_set("noelle.gave_him_a_person_he_took_a_vector", True)
    $ canon_set("liora.faber_protection_revealed", True)
    $ canon_set("liora.held_as_asset_ob", True)
    $ rel_bump("Noelle", trust=1, complicity=1)
    $ npc_remember("Noelle", "delivered_verdant_two_movements_ob", weight=3)
    $ npc_remember("Noelle", "set_aside_lyra_third_subject_ob", tone="compression_unannounced")
    $ npc_remember("Noelle", "filed_gave_him_a_person_he_took_a_vector_silently", tone="register_held_through_grief")
    $ npc_remember("Noelle", "did_not_name_seven_month_possession_of_liora_file", tone="personal_layer_omitted")
    $ npc_remember("Aeron", "received_protocol_verdant_revelation_alone_ob", tone="asset_understanding_consistent")
    $ npc_remember("Aeron", "filed_liora_as_asset_hold_for_use", tone="vector_acquisition")
    $ npc_remember("Aeron", "paused_at_threshold_before_exit_ob", tone="seam_in_register")
    $ npc_remember("Aeron", "said_noelle_name_at_threshold_ob", tone="seam_held_open_briefly")
    $ tp_seed("a4.verdant.payoff_ob")
    $ tp_seed("a4.aeron.liora_held_as_asset")
    $ tp_seed("a4.noelle.vector_grief_unspoken")
    $ tp_seed("a5.faber.unanswered_question_ob")
    $ metric("noelle_compartments_audited_and_filed", change=1)
    $ scene_mark(_current_scene_id, "completed")
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s20b_verdant_decrypt_ob
# cann.chapter: Act IV — Violence Normalized — VERDANT PAYOFF
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Late evening, 3rd of Glass 390 AC. 23:10. Same calendar slot as
#     the EMP version. The decrypt finished approximately one hour
#     before the brief. Noelle has read it twice. The brief lasts
#     approximately twenty-five minutes of story time. The scene ends
#     with Aeron exiting and Noelle alone, returning to the metadata
#     annotation work she was on when he entered.
# cann.what_happened:
#   - Noelle has decrypted Protocol Verdant. She summons Aeron alone
#     to the data alcove. She does not summon Lyra. The third subject
#     of the decrypt (Lyra) is operationally tangential and will not
#     be briefed in this scene. The compression is unannounced.
#   - MOVEMENT 1: Same Aeron-as-preserved-breeding-stock content as
#     EMP. Marcus's "fate" lie was a cover for the preservation. The
#     resonance-compatibility experiments were scheduled for 388-391
#     AC, delayed when Aeron drifted. Faber on three of seven
#     monitoring tiers. Aeron's response: the framing is consistent
#     with his operational understanding. The cover was efficient.
#     The lie was operationally elegant. He files the elegance as
#     interesting. He does not flag the not-being-surprised as data.
#   - MOVEMENT 2: The Liora file. Noelle delivers Faber's countersign
#     protocol context: seventeen disposition orders stopped across
#     nineteen years, Liora alive, Faber the protective mechanism.
#     She does not mention her own seven-month possession of the
#     file (personal-layer item, OB working register omits).
#   - AERON'S RESPONSE: "Hold it. We will use it when we need her."
#     Five words. He files Liora as a tactical asset. The asset
#     position is consistent with his current command tempo.
#   - NOELLE'S RESPONSE: "Acknowledged." She does not flinch. The
#     working register holds. She arranges the operational details
#     of holding the file — secure storage, single-recipient
#     availability, no propagation in the audit log.
#   - AERON'S EXIT WITH SEAM: He turns at the door, pauses one step
#     before the threshold for half a second, turns back, says
#     "Noelle" — uses her name — and delivers a script-permitted
#     statement: "The Liora file's existence is a personal-layer
#     item for me. The use of the file is operational. I am noting
#     the distinction." The Name Mechanic does not activate; the
#     seal holds. The use of the name is the seam in the register.
#     Noelle's response: "Acknowledged."
#   - CLOSE: Noelle alone. Watches the brass-edged file for nine
#     seconds. Returns her eyes to the primary screen. nthought:
#     *"I gave him a person and he took a vector."* Eight words.
#     Filed silently. No save. The OB working register holds. She
#     returns to the metadata annotation she was finishing when
#     Aeron arrived: "*VANCE — verdant payoff briefing complete —
#     addressee acknowledged, holding pattern set per operational
#     request — file secured to lower-left drawer at session
#     close.*" The base functions.
# cann.aeron_state:
#   - Receives Protocol Verdant revelation. Files it as consistent
#     with his operational understanding. The not-being-surprised
#     is data he registers without examining at depth. The "fate"
#     lie is now operationally sized. He files Marcus's nineteen-
#     year asset-management as elegant.
#   - Receives the Liora file. Files her as a tactical asset.
#     "Hold it. We will use it when we need her." Five words. The
#     filing is the OB cost in dialogue form.
#   - The half-second threshold pause and the use of "Noelle" is
#     the OB seam — a seam the working register has not closed.
#     Future OB scenes referencing Liora may need to track the
#     seam's status. The seam is small. The seam is real.
#   - Does not summon Lyra. Does not ask about Lyra. The Lyra-
#     placement information is excluded from the OB briefing and
#     remains unknown to OB Aeron. (Author note: if a later OB
#     scene wishes to surface Lyra's placement, it must do so
#     through a different vector — Faber, an Echelon intercept,
#     a confrontation initiated by Lyra — because the Verdant
#     decrypt path on OB does not deliver this information.)
# cann.noelle_state:
#   - Delivers Verdant payoff in two movements. The OB compression.
#   - Sets aside the Lyra third movement. Does not name the setting-
#     aside. The omission is operational.
#   - Does not name her own seven-month possession of the Liora
#     file. The personal-layer omission is the OB-register practice
#     established in a4_s10a (where she reached past the slip of
#     paper without unfolding it). She is operating from the
#     audit-and-keep posture.
#   - Receives Aeron's "Hold it. We will use it when we need her"
#     without flinching. The face does not change. The chest
#     takes the same breath at the same rate. The register holds.
#   - Files the silent nthought "I gave him a person and he took
#     a vector." The sentence is the OB equivalent of the EMP
#     coda's typed-and-deleted lines: filed by being thought.
#   - Returns to the metadata annotation in the new operational
#     log line. The Vance signature default holds. The audit-and-
#     keep continues.
# cann.path_tracking:
#   - OB path only. Linear. No branching. The scene is the
#     structural twin of a4_s20b_verdant_decrypt_emp — same
#     decrypt, two movements instead of three, no Lyra in the
#     room, no Korr/kore etymology, the Liora file filed as
#     asset rather than gift.
# cann.thematic_flags:
#   - The OB compression: two movements only. Lyra excluded from
#     the Verdant payoff. The third subject is operationally
#     tangential. The decision is Noelle's; she does not consult
#     Aeron on the compression. The compression is OB doctrine in
#     practice — the personal layer is what the operational layer
#     can afford, and the OB operational layer cannot afford the
#     personal layer that includes the priest.
#   - "Hold it. We will use it when we need her." The OB version
#     of the Liora reception. Aeron files his mother as an asset.
#     The filing is the OB cost in dialogue form. Future OB scenes
#     where Liora is referenced must read against this filing —
#     she is a held vector, not a recovered person.
#   - "I gave him a person and he took a vector." Noelle's silent
#     nthought close. The line is canonized in canon_notes_noelle
#     sec 11.2 as the OB scene's closing register. The line is
#     filed silently. The register does not produce the line as
#     speech. The OB cost in eight words.
#   - The half-second threshold pause and the unmediated use of
#     "Noelle" is the OB seam. A small place where the working
#     register has not closed. The seam is canon. Future OB
#     scenes may treat the seam as the trace of a non-zero
#     receiving capacity that the OB script does not have a
#     larger room for.
#   - The Name Mechanic seal holds. The use of "Noelle" at the
#     threshold does not activate the Mechanic. The Mechanic
#     requires a different register than the OB ops voice and
#     that register is not accessible from inside the doctrine.
#   - Faber's countersign protocol is canonized on both paths.
#     The unanswered question — why Faber chose to protect
#     Liora — is open canon-side on OB as well as EMP. tp_seed
#     a5.faber.unanswered_question_ob.
# cann.character_moments:
#   - Noelle: opens with metadata annotation in the Vance default —
#     *VANCE — c/r reviewed.* The Vance signature is the working
#     posture and remains the working posture across the scene.
#   - Noelle: does not name her own seven-month possession of the
#     Liora file. The omission is character-defining. EMP Noelle
#     would have named it. OB Noelle audits and keeps.
#   - Noelle: nine-second observation window on the brass-edged
#     file after Aeron exits. The maximum the OB working register
#     allows for non-task observation. She uses the full nine
#     seconds. The using is the smallest movement the scene
#     contains.
#   - Noelle: "I gave him a person and he took a vector." Filed
#     silently. The nthought is the closest the OB scene comes to
#     a plain sentence. The closing log line in Vance hand
#     reasserts the operational register immediately.
#   - Aeron: "Hold it. We will use it when we need her." Five
#     words. The OB filing.
#   - Aeron: half-second pause one step before the threshold.
#     Turns back. Says "Noelle." The seam.
#   - Aeron: "The Liora file's existence is a personal-layer item
#     for me. The use of the file is operational. I am noting the
#     distinction." The script-permitted noting. The personal layer
#     present but not operationalized — the seam's text.
# cann.callbacks:
#   - a4_s10_noelle_doctrine_ob: the data alcove, the workstation,
#     the cold drafting setting, the Vance signature, the
#     "Acknowledged" register, the unplugged amber lamp. All
#     return.
#   - a4_s10a_noelle_coda_ob: the audit-and-keep posture, the
#     Faber containment principle internalized, the working
#     register's correction-always-comes mechanism. All active
#     here. The omission of the personal-layer items (seven-month
#     file possession; Lyra placement) is the post-coda OB
#     practice.
#   - a3_s16_data_and_doubt_ob: the Name Mechanic seal. Held
#     across the scene. The seam at the threshold does not break
#     it.
#   - a4_s20b_verdant_decrypt_emp: structural twin. Same decrypt.
#     The OB version has two movements where EMP has three; no
#     Lyra; the Liora file is filed as asset where EMP files her
#     as gift; no etymology; no walk-out company.
#   - canon_notes_noelle.md sec 8 (Protocol Verdant): the OB
#     branch is delivered here per canon spec. The two movements
#     and the asset-filing are both canon-locked.
#   - canon_notes_noelle.md sec 11.2: "I gave him a person and
#     he took a vector" is delivered as silent nthought, undelivered
#     aloud. As specified.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. OB path only. The OB
#     thesis-level Verdant reveal scene. Foundational for: every
#     subsequent OB scene where Liora can be referenced as a
#     held asset rather than a person, every scene where Aeron
#     processes Marcus's "fate" lie as elegant operational cover,
#     the OB Tessa anchor (where Noelle's audit-and-keep posture
#     is consistent with her refusal of the implant removal).
# cann.requires_followup:
#   - The Liora file is held in Noelle's secure storage with
#     single-recipient retrieval available to Aeron. Future OB
#     scenes that require the file must request it through this
#     pathway.
#   - The Lyra placement is unrevealed on OB. If a future OB
#     scene needs the placement to surface, it cannot route
#     through the Verdant decrypt — it must come via Faber, an
#     Echelon intercept, or Lyra herself. The author should track
#     that OB Aeron does not know Lyra was placed and act
#     accordingly.
#   - The half-second seam at the threshold is canon. Future OB
#     scenes between Aeron and Noelle may reference the seam
#     implicitly without naming it. The seam is the OB version of
#     the EMP "I am paying attention" — a small private artifact
#     the working register has not absorbed.
#   - "I gave him a person and he took a vector" is filed but not
#     committed to any operational record. The line is in Noelle's
#     interior canon and is the load-bearing private sentence of
#     OB Noelle's Act IV close. Future OB scenes where Noelle
#     considers the asset-filing of Liora should read against this
#     line.
#   - The next OB scene in the queue (a4_s21_the_letter_ob)
#     handles Liora's own letter arriving via courier. The Verdant
#     decrypt is the operational confirmation Liora is alive; the
#     letter is the personal weight. The two scenes should be
#     played in order. The Verdant decrypt establishes Aeron's
#     filing posture; the letter tests it.
# =========================================================
