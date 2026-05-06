# =======================================================
# ACT 4 - Scene 20c: The Last Transmission (Obedience Path)
# File: a4_s20c_last_transmission_ob.rpy
# Type: ZIRA THESIS BEAT — Renn's last broadcast decrypted (OB)
# Matrix: Zira alone. The room she will not share.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s20c_last_transmission_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s20c_last_transmission_ob:
    $ show_timeline("4th of Glass, 390 A.C.", "03:14", "Phoenix Base — Zira's Workshop")

    # Codex stage bumps - note the asymmetry with EMP. Aeron does not
    # rise on this path; he will not learn what Zira learns tonight.
    $ codex_reveal("zira", to_stage=4, source="a4_s20c_last_transmission_ob")
    $ codex_reveal("renn_kael", to_stage=3, source="a4_s20c_last_transmission_ob")
    $ codex_unlock("the_choice_at_the_console", source="a4_s20c_last_transmission_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. Same workshop as EMP — same scuffed terminal, same
    #         lead-lined drawer, same three-core-node monitoring panel,
    #         same low ceiling. The room is identical to its EMP twin.
    #         The composition is the difference. The OB scene holds
    #         single-on-Zira for its entire duration. The spare chair
    #         is in the workshop tonight as it has been in every
    #         prior Zira-workshop scene; it remains empty for the full
    #         length of the broadcast. The empty chair is the scene's
    #         visual argument.
    #         Coverage opens tight on Zira's hands at the cipher
    #         terminal — the same opening as EMP. The framing
    #         diverges at the decryption: where EMP cuts to her face
    #         and follows her out of the workshop, OB holds tight on
    #         Zira at the terminal. The camera does not let her go
    #         to find Aeron. The camera does not even consider it.
    # LIGHTING: Workshop late late night. Single overhead at half.
    #           The terminal screen glow. The three-core-node
    #           monitoring panel along the back wall. Identical to
    #           EMP. Lighting will not change across the scene.
    # SFX: Same workshop ambient as EMP. Same cipher-completion
    #      chime when the decryption resolves. Same broadcast audio
    #      across the playback. The four seconds of silence at the
    #      end of the broadcast play the same way. The workshop
    #      door does not open at any point during the scene. No
    #      knock. No corridor sound. The empty chair sits in
    #      acoustic silence beside her.
    #      No music bed. The scene refuses one. The silence after
    #      the broadcast plays uninterrupted.
    # FACE: Zira — eleven-years face, OB calibration. Same face as
    #        the EMP version at scene open. The face holds longer
    #        in OB than it does in EMP. The face does not break in
    #        the same place. The face holds through the entire
    #        broadcast. The breaking, if it happens, happens after
    #        the file closes. The OB working register provides the
    #        holding.
    #        Aeron — not in scene. He is in his quarters, asleep.
    #        He will not wake tonight. The scene's choice is to
    #        leave him there.
    # BLOCKING: Zira at the cipher terminal for the entire scene.
    #           She does not stand. She does not leave the chair.
    #           The chair is the entire scene's geographic anchor.
    #           She does not open the lower drawer. She does not
    #           touch the pressed flower. The drawer remains closed.
    #           At scene close she returns to her working queue. The
    #           hour is operational again.

    # ========= VOICE BASELINE =========
    # Zira: workshop voice, OB calibration. The Vance-equivalent voice
    #        for Zira — operational, contained, the working register
    #        holding through information that on EMP would have
    #        cracked it. The technical voice does not fail in this
    #        scene. The technical voice has more work to do.
    # Aeron: not in scene. No spoken Aeron lines.
    # Renn (audio only): identical broadcast to EMP. Same five
    #        minutes twelve seconds. Same words. The same recording.
    #        OB Zira hears it once.

    # scene bg_zira_workshop_late_ob with dissolve
    # play ambient "sfx/ambient/zira_workshop_terminal.ogg" fadein 2.0

    # ========== PHASE 1 — THE CYCLE ==========

    # CAMERA: 50mm. Open tight on Zira's hands at the
    #         cipher terminal. Same opening as EMP.
    #         The hands are working the same sequence
    #         they have worked four thousand and
    #         eighty-three times.
    # SFX: cipher cycle tone, low hum, carrier hiss
    #      leak from the monitoring panel.

    "The workshop at oh-three-fourteen. The base in its deepest second-shift quiet. Zira at the cipher terminal. Her hands working the same sequence they have worked four thousand and eighty-three times."

    "She does not count the cycles aloud. She counts them privately. Tonight will be four thousand and eighty-four. The number is meaningless and the number is exact."

    zthought "Today's fragment came in at twenty-two-fifty-eight via the Sector Three maintenance pull. Thirty-seven bytes."

    zthought "Largest single-cycle fragment ever pulled. Most cycles return zero or one byte. Tonight returned thirty-seven."

    zthought "Noting the size. The size is data. The size isn't yet a result."

    "Her fingers complete the load sequence. The fragment resolves in the test buffer. She tabs to the cipher-test routine."

    zthought "Run."

    "She runs it."

    "The cipher terminal hums. The cycle tone holds. Zira watches the corner of the screen — the spot where the progress indicator lives, the spot her eye has trained to monitor over eleven years."

    "Two minutes seven seconds. Three minutes. Four. Five. Six. The cycle has not returned NULL. The progress indicator advances steadily for the last fifty-one seconds."

    "At seven minutes thirty-one, the cipher-completion chime sounds."

    "Three tones. Distinct from the cycle tone. The chime has never sounded before. Zira has heard the cycle tone four thousand and eighty-three times. She has never heard the completion chime."

    "Her hands stop on the keyboard."

    "The terminal displays the line:"

    "*DECRYPTION COMPLETE — 1 FILE — 5:12 AUDIO — RENN_FINAL_BROADCAST.wav*"

    zthought "Eleven years."

    zthought "Tonight."

    "She does not move."

    # ========== PHASE 2 — THE DECISION ==========

    # CAMERA: holds tight on Zira. The terminal display
    #         glows the completion notice. The empty
    #         spare chair is visible in the corner of
    #         the frame — the chair Zira has had since
    #         the base rebuild and has never offered
    #         to anyone. It remains empty.
    # LIGHTING: unchanged.

    "She does not stand."

    zthought "Rylan's three doors down."

    zthought "Asleep. Probably."

    zthought "He could be in the chair in five minutes."

    zthought "My hand isn't on the door control."

    zthought "Good."

    "She does not justify the decision in her own thinking. She does not run a pro-and-con. The OB working register has been making decisions of this shape for two months without ceremony. Tonight is consistent."

    zthought "He doesn't have a beacon credential. He never accepted the chip at the bridge. He hasn't authenticated against my brother once across the entire run of his Ghostline access. I've been overriding for him by hand for fourteen months."

    zthought "I've been holding Renn back from him."

    zthought "I'm not giving him Renn tonight. The not-giving is the entire reason I've been holding the chip."

    zthought "The broadcast is mine. The broadcast plays in this room with the chair empty."

    "She turns to the cipher terminal. She calls up the file. Her hands are steady. The eleven years has trained the hands."

    "She presses play."

    # ========== PHASE 3 — THE TECHNICAL THREE MINUTES ==========

    # CAMERA: holds tight on Zira's face. The empty
    #         chair remains visible at the edge of the
    #         frame. The framing is its own indictment.
    # SFX: the broadcast plays. Renn's voice. Same
    #      voice as EMP. Identical recording. The
    #      audience is hearing the same thing Zira's
    #      EMP self heard with Aeron in the room.
    #      Tonight the room contains one person.

    "The broadcast plays."

    "Renn clears his throat. The same wet sound from the EMP version. Same recording. Different room."

    renn "(via recording) Successor channel. This is Renn at the Sector Twelve-B primary. If you are listening to this it means I did not make it back and the wafer made it to whoever is rebuilding. I am going to walk you through the priority items in the order I would want them rebuilt. I am going to be efficient. The walk is the walk."

    "Zira's face does not change."

    "Her hands stay on her knees."

    renn "(via recording) Priority one. Repeater chains. You will find seven configured chains in the southern sub-mesh. Six are stable. The seventh is the one I rebuilt last week — node Corvid through the bird-feeder factory. The handshake on that one is non-standard. I built it asymmetric to keep it off Echelon's pattern reads. To replicate, you reverse the third-byte flip in the —"

    "He continues. The technical detail runs for ninety seconds. Repeater chain configuration. Beacon credential rotation. The geographic distribution Renn wanted for the first ten Ghostline nodes — the same distribution Zira used for the rebuild, eleven years later."

    zthought "I'm hearing the reasoning behind eleven years of my own choices. I already knew the reasoning. I reverse-engineered it. The new part is the voice saying it."

    zthought "I'm not going to linger on the new. The new is data. The data is filing."

    "The OB working register holds. The face holds. The hands hold."

    "The broadcast hits the three-minute thirty-eight mark. Renn's voice shifts."

    renn "(via recording) Z — I'm hearing them at the perimeter. Two minutes maybe."

    # ========== PHASE 4 — THE FINAL NINETY SECONDS ==========

    # CAMERA: still tight on Zira. No shift. The OB
    #         scene refuses the camera shift the EMP
    #         scene takes. The scene does not change
    #         framing because the room has not
    #         changed. There is only one person here.
    # SFX: Renn's voice continues. The audience hears
    #      the same words. The container is different.

    renn "(via recording) I'm going to hold the post until the broadcast hits the seventeenth cell. After that, the repeater chain takes over. I configured it last week. You didn't know. Sorry — wanted you to have a redundancy you didn't owe me."

    zthought "He configured the repeater chain. Eleven years late, he's telling me the rebuild had a backup I didn't know about."

    zthought "The backup didn't save him. The backup was for Ghostline."

    zthought "The backup is data. I'm filing the data."

    "The recording's ambient shifts. Some part of Sector 12-B's relay floor is audible behind Renn — small mechanical sounds, distant. Echelon is approaching. The sounds change."

    "Renn breathes once. The breath is on the recording."

    renn "(via recording) You asked. I answered. I'd answer the same. Keep the line alive."

    zthought "He's naming the choice."

    zthought "He's validating the choice."

    zthought "I've been carrying the choice as ours. He's confirming I've been carrying it correctly."

    zthought "The confirmation is what I came here for. The confirmation has now arrived."

    "Pause."

    renn "(via recording) Out."

    "Four seconds of silence in the recording. The silence is the recording of the silence before Marcus shot Renn. No gunshot in the file."

    "The cipher terminal returns to ambient hum."

    # ========== PHASE 5 — THE HOLD ==========

    # CAMERA: holds tight on Zira. The empty chair is
    #         still in the frame. The face is doing
    #         the work the face has been trained to
    #         do.
    # LIGHTING: unchanged.

    "Zira does not speak."

    "There is no one to speak to."

    "Her hands have not moved from her knees."

    "The face is intact."

    zthought "Information is here. Filing required."

    zthought "Item one: the Choice at the Console is confirmed. He validated it. The carrying has been correct. Filed."

    zthought "Item two: he calls the choice *ours.* You asked. I answered. I'd answer the same. The naming of the partnership-in-cost is the work the OB version of me has been doing without language for it. The naming closes the language gap. Filed."

    zthought "Item three: he signs off as *Out.* The word is his standard radio close. The word is in the broadcast. The word isn't for me to inherit. The word is his. Filed."

    zthought "The conversation Zira-eleven-years-ago was hoping for was longer than this. The brevity is itself a fact. The brevity is filed."

    "The OB working register's filing closes the items inside their own nthought lines. The items the broadcast did not contain — the longer reassurances, the named names, the directives for the rebuild's caretakers — were never going to be in the broadcast. Renn had two minutes. He used five sentences. The five sentences were enough for him. The OB working register is filing them as enough for her."

    zthought "Audit complete."

    "The phrase is the phrase she has used to close every personal data crystal audit in her workshop life. The phrase is what she uses to mark the end of work that is hers and not the rebellion's. Tonight the phrase closes the eleven-year cycle."

    zthought "Filed."

    # ========== PHASE 6 — THE STORAGE ==========

    # CAMERA: a small movement. Zira's hand goes to
    #         the keyboard. She does not stand. She
    #         does not open the drawer. She files the
    #         broadcast.
    # LIGHTING: unchanged.

    "She moves to file the broadcast."

    "She does not store it on Ghostline distributed storage. The file is too sensitive for distributed storage on either path; on this path the additional concern is that distributed storage is auditable by Aeron through his manual override permissions. She files it instead in a private archive — a single encrypted store separate from the network."

    "She encrypts the file with a new cipher. The new cipher is not Renn's. The new cipher is one she wrote tonight, in the last twenty seconds, while the broadcast was playing. The cipher is hers alone. No one else will be able to decrypt the file. Including Aeron, if he ever finds it."

    zthought "The decrypted file existed for thirty-seven seconds. The encrypted-with-new-cipher file is the version that lives forward."

    zthought "The new cipher's key is in my head. It isn't written down."

    zthought "If I die, the file dies with me. It won't survive me."

    zthought "Noting the consequence. The consequence is consistent with the OB working register's principle: the trail of the editing must be smaller than the trail of the un-editing."

    zthought "I'm editing the broadcast. Not the content — the access. The content is preserved. The access is sealed."

    zthought "The seal is mine."

    "She types the storage command. The encryption runs. The encrypted file lands in the private archive. The decrypted version is purged from the cipher terminal's working memory. The terminal returns to its standard ambient state."

    "The file is now sealed."

    # ========== PHASE 7 — THE LOG ==========

    # CAMERA: pulls back slightly. Zira at the
    #         workstation, the empty chair still
    #         visible, the cipher terminal at idle.
    #         She types into her personal Ghostline
    #         operator log.
    # LIGHTING: unchanged.

    "She types one line into her personal Ghostline operator log."

    "The log is the small private journal she keeps for her own work. Nobody else reads it. She has been writing in it since the rebuild began. Her standard sign-off in the log is *Z. close.* — operational shorthand."

    "Tonight's entry is dated 4 Glass 390 oh-three-fifty-nine."

    "*Cipher decryption complete. File received. File re-sealed under new cipher. Z. close.*"

    "She does not type *Out.* The word does not propagate to her vocabulary on this path."

    zthought "He left me the word. I'm not taking it. The taking would be a public act. The public act would need someone else in the room. Aeron isn't in the room."

    zthought "The word stays his. I keep my own."

    "She closes the log."

    # ========== PHASE 8 — THE DRAWER ==========

    # CAMERA: slow push down to the lower drawer
    #         beneath the workstation. The drawer is
    #         closed. Zira's hand hovers near the
    #         drawer pull. She does not open it.
    # LIGHTING: unchanged.

    "Her hand hovers over the drawer pull for perhaps three seconds."

    "Inside the drawer: the lead-lined sub-compartment with the wafer. Beside the sub-compartment: the oilskin packet with the pressed winterbloom Selene gave her, pre-displacement. The flower she has not touched."

    "She does not open the drawer."

    zthought "If I open the drawer tonight I'll touch the flower. The touch would be a sentimental decision. Tonight isn't the night for sentimental decisions."

    zthought "Selene is dead. Two months. She gave me the flower before she died, at a moment I can't properly date because the OB compression of the past two months is heavier than the EMP version of the same window."

    zthought "I'm not opening the drawer tonight."

    "Her hand returns to her knee."

    "The drawer stays closed."

    zthought "The flower is still there. It's been there for two months. It'll be there tomorrow."

    zthought "The eleven-year compartment is closed. The two-month compartment stays closed."

    zthought "Filed."

    # ========== PHASE 9 — THE OPERATIONAL HOUR ==========

    # CAMERA: holds wide on the workshop. Zira at
    #         the terminal. The empty chair. The
    #         closed drawer. The three-core-node
    #         monitoring panel pulses at standby.
    #         The room is the room. The room is
    #         identical to its EMP twin in geometry
    #         and identical to its EMP twin in
    #         lighting and identical to its EMP twin
    #         in furniture. The composition shows
    #         the difference. The composition is
    #         the difference.
    # LIGHTING: unchanged. The room has not changed.

    "Zira returns to the operational queue."

    "She has nine items pending review for tomorrow's oh-six-hundred briefing. The items have been on her queue since yesterday. The items will be on her queue regardless of what just happened in the workshop."

    "She opens the first item. A Ghostline node performance review for the eastern sub-mesh. She runs the diagnostics. The diagnostics return clean. She files the review. She moves to the second item."

    "The work continues."

    "Inside her, the broadcast plays. Renn's voice in the file is now sealed under a new cipher she alone can decrypt. The validation he gave her — *I'd answer the same* — is data she has now filed. The compressed five sentences are data she has filed. The word *Out* is data she has filed. The conversation she had been imagining for eleven years — the longer one, the one with the names and the directives and the *I love you* — was never going to be in the broadcast. Renn did not have time. The not-having-time is data she has filed."

    "The filing is complete. The audit is closed. The work resumes."

    "Aeron is in his quarters, asleep. He will wake at oh-five-thirty for the morning brief. He will not know what happened in this workshop tonight. He will never know."

    "The repeater chain Renn configured eleven years ago — the redundancy he built without telling her — is still operational, somewhere in the southern sub-mesh. She has been using it without knowing. The chain is one of the things she has just learned about. She files the learning."

    "The base around her continues to function. Ghostline transmits. The carrier hiss moves through the monitoring panel at its standard rate. Every burst transmission carries the nine names in the salt — a memorial automated, automatic, eleven years old, never named to anyone."

    "The empty chair stays empty."

    "The cipher terminal stays at ambient hum."

    "The drawer stays closed."

    "The flower stays where it has been for two months."

    "The work continues."

    "Out is not said."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("last_transmission_complete_ob", True)
    $ flag("zira_renn_letter_decrypted", True)
    $ flag("breach_choice_kept_private_ob", True)
    $ flag("nine_names_kept_in_salt_ob", True)
    $ flag("beacon_chip_renn_withheld_ob", True)
    $ flag("flower_resealed_ob", True)
    $ flag("zira_out_signoff_active_ob", False)
    $ flag("marna_disposition_locked_faber", True)
    $ canon_set("zira.renn_letter_decrypted", True)
    $ canon_set("marna.disposition_signed_by_faber", True)
    $ canon_set("zira.choice_disclosed_to_aeron_ob", False)
    $ canon_set("zira.nine_names_disclosed_aloud_ob", False)
    $ canon_set("zira.flower_position_ob", "drawer_closed_unchanged")
    $ canon_set("zira.signoff_default_ob", "Z. close.")
    $ canon_set("zira.broadcast_resealed_under_new_cipher", True)
    $ canon_set("zira.new_cipher_key_held_only_in_head", True)
    $ canon_set("aeron.knows_choice_at_console_ob", False)
    $ canon_set("aeron.knows_nine_names_ob", False)
    $ canon_set("aeron.knows_beacon_chip_carries_renn_ob", False)
    $ canon_set("aeron.workshop_chair_unassigned_ob", True)
    $ canon_set("renn.last_broadcast_audience_count_ob", 1)
    $ rel_bump("Zira", trust=1, distance=2)
    $ npc_remember("Zira", "decrypted_renn_letter_after_eleven_years_alone_ob", weight=4)
    $ npc_remember("Zira", "did_not_walk_to_aerons_quarters", tone="path_not_taken")
    $ npc_remember("Zira", "filed_broadcast_in_register_after_listening", tone="working_register_held_through_grief")
    $ npc_remember("Zira", "did_not_inherit_out_signoff_ob", tone="word_left_to_brother")
    $ npc_remember("Zira", "did_not_open_drawer_did_not_touch_flower", tone="sentimental_decision_deferred")
    $ npc_remember("Zira", "resealed_broadcast_under_personal_cipher", tone="access_edited_content_preserved")
    $ npc_remember("Zira", "returned_to_operational_queue_within_minutes", tone="work_continues_grief_internal")
    $ tp_seed("a4.zira.broadcast_received_alone_ob")
    $ tp_seed("a4.zira.choice_validated_filed_ob")
    $ tp_seed("a4.zira.holding_renn_back_from_aeron_continues")
    $ tp_seed("a4.zira.flower_drawer_sealed_ob")
    $ tp_seed("a5.zira.broadcast_dies_with_her_ob")
    $ metric("zira_compartments_audited_and_filed", change=4)
    $ scene_mark(_current_scene_id, "completed")
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s20c_last_transmission_ob
# cann.chapter: Act IV — Violence Normalized — ZIRA THESIS BEAT
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - 4 Glass 390 AC. Oh-three-fourteen to approximately oh-four-
#     fifteen. The scene runs longer than the EMP version because
#     Zira does not leave the workshop and continues into the next
#     hour's operational queue. Same calendar slot as the EMP
#     version. Same eleven years and one month after the Breach.
#     Same four thousand and eighty-fourth cipher cycle.
# cann.what_happened:
#   - Zira at the cipher terminal. Same opening as EMP. Same
#     fragment from the Sector Three maintenance pull. Same
#     thirty-seven-byte fragment, the largest single-cycle pull
#     ever. Same seven-minute thirty-one-second cipher cycle.
#     Same completion chime. Same DECRYPTION COMPLETE notice.
#   - DIVERGENCE FROM EMP: Zira does not stand. Does not walk
#     to Aeron's quarters. Does not invite him to the workshop.
#     The decision is made in nthought without ceremony: he does
#     not have the Beacon Chip; he has not authenticated against
#     Renn; she has been holding Renn back from him for fourteen
#     months; she will not give him Renn tonight.
#   - The empty spare chair stays empty for the entire scene.
#   - The broadcast plays. Same recording. Same five minutes
#     twelve seconds. Same words. Same final ninety-second shift.
#     Same *You asked. I answered. I'd answer the same. Keep the line
#     alive. Out.* Same four seconds of silence.
#   - Zira's response to the broadcast is internal-only. She
#     files each piece of information as it lands:
#     1. The Choice at the Console — confirmed and filed.
#     2. *You asked. I answered. I'd answer the same.* — the
#        naming of the partnership-in-cost. The OB working
#        register has been carrying the partnership without
#        language for it. The naming closes the language gap.
#        Filed.
#     3. *Out* — filed; not inherited as her sign-off.
#   - The conversation Zira had been imagining for eleven years
#     was longer than the actual broadcast. The brevity is
#     itself a fact. The brevity is filed.
#   - "Audit complete. Filed." The OB working register's standard
#     close phrase, applied to the eleven-year cycle.
#   - She re-encrypts the broadcast under a new cipher she
#     writes during the playback. The new cipher's key is held
#     only in her head. The original decrypted file is purged
#     from the terminal's working memory. The broadcast now
#     lives under her personal seal.
#   - She types her log: "Cipher decryption complete. File
#     received. File re-sealed under new cipher. Z. close." She
#     does NOT type *Out.* The word stays Renn's.
#   - She does not open the lower drawer. The pressed flower
#     stays in the oilskin. The wafer stays in the lead-lined
#     sub-compartment. Her hand hovers near the drawer pull and
#     returns to her knee. "Tonight is not the night to make
#     sentimental decisions."
#   - She returns to the operational queue. Nine items pending
#     review for the morning brief. She opens the first. The
#     work continues.
#   - The scene closes on the workshop's continued operation.
#     The empty chair. The closed drawer. The flower in the
#     oilskin. The cipher terminal at ambient hum. Aeron asleep
#     in his quarters and will not know.
# cann.zira_state:
#   - Eleven years of decryption work completes. The hunt ends
#     tonight. She does not externalize the ending.
#   - The Choice at the Console is validated by Renn's broadcast.
#     The carrying has been correct. The validation arrives in a
#     room with one person in it.
#   - The nine names remain in Ghostline's salt. They are not
#     spoken aloud on this path.
#   - The Beacon Chip carries Renn. Aeron does not have a chip.
#     The disclosure does not happen.
#   - The pressed flower remains in the oilskin. The drawer is
#     closed.
#   - *Out* does not propagate to her vocabulary. Her sign-off
#     remains *Z. close.*
#   - The broadcast is re-sealed under a personal cipher with a
#     key only she knows. If she dies, the broadcast dies with
#     her. The rebellion will never hear it.
#   - The grief is filed. The grief is internal. The work
#     continues within minutes.
# cann.aeron_state:
#   - Not in scene. Asleep in his quarters from approximately
#     twenty-two-thirty until oh-five-thirty. He will wake for
#     the morning brief and will not know what happened in
#     Zira's workshop.
#   - **He will not learn what happened in this scene.** Not in
#     this hour, not in this day, not at any subsequent point on
#     the OB path by default. Future authoring may surface the
#     broadcast to him via a different mechanism, but the
#     default is permanent withholding.
# cann.path_tracking:
#   - OB path only. Structural twin of a4_s20c_last_transmission_emp.
#     Same broadcast, same content, same revelations. Different
#     room composition (one person vs two) and different
#     downstream consequences (filing vs disclosure).
# cann.thematic_flags:
#   - **The empty chair as visual indictment.** The chair stays
#     in frame for the entire scene. The chair has been Aeron's
#     chair since the workshop's establishment; on this path,
#     the chair has never been used. Tonight is the night the
#     chair would have been claimed. It is not.
#   - The OB withholding mechanic: Zira has been holding Renn
#     back from Aeron for fourteen months by manually
#     overriding his Ghostline credential checks. Tonight she
#     finalizes the holding. Renn stays hers. The withholding
#     is canon and is the OB cost in the friendship register —
#     not a withdrawal of love but a withdrawal of *what she
#     will share with the man Aeron is becoming.*
#   - The new cipher seal: Zira encrypts the broadcast with a
#     personal key only she knows. The seal is the OB
#     equivalent of Noelle's surname-kept move (a4_s10a). Both
#     characters audit a long-held compartment, find it worse
#     than expected, and choose to maintain the seal voluntarily.
#   - "Audit complete. Filed." The OB working register's
#     close-phrase deployed against eleven years of grief. The
#     phrase is the same phrase Zira uses for any operational
#     audit. Tonight it closes the personal layer with the same
#     vocabulary. The flatness is the cost.
#   - *Out* not inherited. The word stays Renn's. Future OB
#     Zira sign-offs default to *Z. close.* The non-inheritance
#     is canon.
#   - The drawer stays closed. The flower stays in the oilskin.
#     Future OB workshop scenes should respect that the drawer
#     is sealed. If a later OB scene opens the drawer, it is a
#     significant inflection point and should be authored
#     deliberately.
# cann.character_moments:
#   - Zira: does not stand. The not-standing is the scene's
#     first deliberate choice and the scene's structural
#     thesis.
#   - Zira: files each broadcast revelation in nthought as it
#     arrives. The filing-as-she-listens is the OB working
#     register's most active form.
#   - Zira: writes a new cipher during the playback. The
#     simultaneity is the character moment — she is hearing the
#     broadcast for the first time in eleven years and her
#     hands are already designing the seal that will follow.
#   - Zira: hand hovers over the drawer pull for three seconds.
#     Returns to her knee. The not-opening is the smallest
#     gesture in the scene.
#   - Zira: types *Z. close.* in her log. Does not type *Out.*
#     The single-word choice is the scene's cleanest character
#     beat.
#   - Zira: returns to operational queue within minutes. "The
#     work continues."
# cann.callbacks:
#   - a4_s20c_last_transmission_emp: structural twin. Same
#     broadcast. Same Renn voice. Same content. Different
#     room composition. The two scenes are written to be
#     readable as a single decryption viewed from opposite
#     paths.
#   - a4_s10a_noelle_coda_ob: parallel audit-and-keep
#     mechanic. Both Zira-OB and Noelle-OB audit a long-held
#     compartment and choose to maintain the seal. Both use
#     the same close-phrase register ("Audit complete.
#     Filed.")
#   - a3_s19b_zira_before_the_weight_ob: the pressed flower
#     introduction. The flower remains in the oilskin in
#     this scene per OB consistency.
#   - a1_s26_obsidian_bridge: Aeron's rejection of the
#     Beacon Chip on OB. The rejection is what allows Zira
#     to hold Renn back across all of Acts 2-4 OB. Tonight's
#     not-walking-to-his-quarters is the consummation of the
#     not-giving that began at the bridge.
#   - canon_notes_zira.md sec 11.2 (OB path): scene
#     delivered per spec.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. OB path only. Zira's
#     OB thesis beat. Foundational for: every subsequent OB
#     scene where Zira's grief is internal-only (default), every
#     subsequent OB Ghostline scene (manual override of Aeron's
#     credential continues; the rationale is now firmly
#     established), every subsequent OB workshop scene (the
#     drawer is sealed, the flower is in the oilskin, the
#     spare chair is empty).
# cann.requires_followup:
#   - The new cipher seal is canon. Future OB scenes referencing
#     the broadcast must respect that only Zira can decrypt the
#     re-sealed file. If Zira dies on OB, the broadcast dies
#     with her.
#   - The empty chair in the OB workshop is now a fixture. If a
#     future OB scene uses the chair, that use is canonically
#     significant.
#   - *Out* does not propagate on OB. Future OB Zira sign-offs
#     default to *Z. close.*
#   - The flower in the oilskin continues. If a later OB scene
#     opens the drawer or touches the flower, it is the OB
#     equivalent of an inflection point and should be authored
#     deliberately.
#   - Aeron does not learn about the broadcast on OB by default.
#     Author at discretion if a later OB scene wants to surface
#     the broadcast via different mechanism. The default is
#     permanent withholding.
#   - Marna is not named in the broadcast. Renn ran out of time
#     before he could get to her. The not-naming is canon. The
#     conversation Zira imagined for eleven years included Marna;
#     the actual broadcast did not. The grief shape on OB is
#     specifically that the broadcast was shorter than the
#     imagined version. Future OB Marna references should respect
#     that Renn never got to ask Zira to take care of her —
#     because he ran out of seconds.
# =========================================================
