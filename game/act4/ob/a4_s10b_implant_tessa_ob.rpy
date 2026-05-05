# =======================================================
# ACT 4 - Scene 10b: The Watch (Obedience Path)
# File: a4_s10b_implant_tessa_ob.rpy
# Type: TESSA × NOELLE ANCHOR — Aether Tag identified, removal refused
# Matrix: Tessa stays. Noelle goes glass. Structural inversion of EMP.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s10b_implant_tessa_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s10b_implant_tessa_ob:
    $ show_timeline("30th of Forge, 390 A.C.", "08:40", "Phoenix Base — Medbay Theater")

    # Codex stage bumps — note the asymmetry from EMP.
    $ codex_reveal("noelle_korr", to_stage=4, source="a4_s10b_implant_tessa_ob")
    $ codex_reveal("tessa_kael", to_stage=4, source="a4_s10b_implant_tessa_ob")
    $ codex_unlock("aether_tag", source="a4_s10b_implant_tessa_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm at scene open. Same medbay theater as the EMP version
    #         on the parallel timeline — same surgical table, same prep
    #         tray, same autoclave. The room is the same room. The scene
    #         is going to use the room differently. Coverage opens on
    #         Tessa's hands at the scanner, then settles into a two-shot
    #         that holds for the bulk of the scene. The two-shot is the
    #         OB geometry of staying — Tessa and Noelle in the same
    #         frame across the full appointment window because Tessa
    #         does not leave when Noelle refuses the procedure. The
    #         frame is the watch. The watch is the scene.
    # LIGHTING: Medbay theater. Two task lights at full at scene open —
    #           Tessa always preps as if she will be doing the procedure.
    #           Halfway through the scene, after the refusal, she dims
    #           the surgical lights and the room becomes a follow-up
    #           room rather than a theater. The dimming is procedural
    #           and personal at the same time — a procedure that will
    #           not happen requires no surgical light. The dimming is
    #           also Tessa naming the change without naming it.
    # SFX: Medbay ambient. The standing autoclave's slow tick. The
    #      scanner chime when the resonance pass detects the tag.
    #      The CAD-band acknowledgment chirp at the end of the scan.
    #      No surgical-field sounds — the procedure does not happen.
    #      The scene's mid-point is acoustically marked by Tessa
    #      moving the surgical instruments back to the prep tray
    #      from the working tray — the small mechanical clinks of
    #      the steel returning to its case. The clinks are the
    #      sound of a procedure being un-prepared. There is no
    #      music bed. The scene refuses one.
    # FACE: Tessa — the working face that does not change when the
    #       work changes shape. She does not register disappointment.
    #       She does not register anger. She does not register the
    #       desire to walk out of the room — that desire is not in
    #       her, and the scene's load is the audience seeing it not
    #       be in her. The face is the same face she ran A2_P14 on.
    #       The face is the face that stays.
    #       Noelle — the OB working face from a4_s10 and a4_s10a.
    #       The audit-and-keep posture. The face does not change
    #       across the refusal. The face does not change when Tessa
    #       offers the procedure. The face does not change when
    #       Tessa stays. The not-changing is the scene's other load.
    # BLOCKING: Tessa at the scanner, then beside the table, then at
    #           the prep tray un-laying the instruments, then in the
    #           chair across from Noelle for the watch. She moves
    #           five times. Each movement is small. None of them
    #           toward the door.
    #           Noelle on the surgical table edge at scene open.
    #           Stays on the edge through the refusal. Sits in the
    #           chair Tessa indicates after the dimming. Stays in
    #           the chair for the watch. Does not stand until Tessa
    #           releases her at the appointment-window close.

    # ========= VOICE BASELINE =========
    # Tessa: working register. Same as EMP for the diagnostic phase.
    #         When Noelle refuses, Tessa's voice does the staying-
    #         thing — slower than her ops voice, plainer, the voice
    #         she uses for patients who have decided against an
    #         indicated treatment and need the room to remain a room.
    # Noelle: OB working register. The Vance-default voice. Faber's
    #          syntax. The audit-and-keep posture. She uses
    #          "Acknowledged" and "Operationally" and "Closed-loop"
    #          without registering them as cold. They are the
    #          register's vocabulary. The register holds.

    # scene bg_medbay_theater_morning with dissolve
    # play ambient "sfx/ambient/medbay_theater.ogg" fadein 2.0

    # ========== PHASE 1 — THE SCAN ==========

    # CAMERA: 50mm. Open on Tessa's hands at the prep
    #         tray laying out instruments — the same
    #         instruments she would use if the
    #         procedure were going to happen. The
    #         laying-out is the scene's first
    #         operational sentence: she is preparing
    #         to do the work. The audience sees the
    #         preparing. The audience does not yet
    #         know the work will not happen.

    "The medbay theater is small. Tessa runs it the way she has run it for two years now: instruments laid out in the order of use, the periphery dimmed, the bright spot held over the surgical field. She has not pre-judged the appointment outcome. Tessa never pre-judges. The instruments are out because the appointment is at oh-eight-forty and the appointment may require them."

    "Noelle arrives at oh-eight-forty exactly. The arrival is the punctuality of a person who has factored the appointment into a tactical schedule and is moving on a clock. The face is the face from the data alcove yesterday morning. The face has not changed since the doctrine signature."

    "Tessa registers the punctuality without flagging it."

    t "Sit on the table for me."

    "Noelle sits."

    t "Headaches still in the same place."

    n "Base of the skull. The same place. The intensity has tracked operational stress reasonably well. The last forty-eight hours scored higher than baseline. I have factored the operational tempo as the cause."

    t "I am going to scan and we will see."

    "Noelle tilts her head forward. Her hair falls. The base of her skull is exposed."

    "Tessa's left hand settles at the crown. The contact is light. The right hand brings the resonance scanner over the field. The pass is slow. Two seconds across, hold for one second at the suspect zone Tessa already had on her clipboard."

    "The scanner chimes once at the medical confirmation frequency. Then a second time at the lower resonance-detected tone. Then a third tone — the brief sharp CAD-internal scanner-band acknowledgment."

    "Noelle's ear catches the third tone before her conscious mind processes it."

    nthought "CAD-internal band. The tag is identified."

    "Tessa puts the scanner down."

    "Her hand stays at the crown for two seconds longer than it needs to."

    t "Noelle. There is a passive monitoring device implanted at the base of your skull. Approximately the size of a fingernail clipping. Sitting against the bone, not under it. The anchor is shallow. Transmitting on a low duty cycle. Transmitting now."

    "She lets the sentence land."

    t "Tell me what I am looking at."

    n "CAD-issue Aether Tag. Researcher-class. The internal CAD term among the researchers who carry it is *the leash.* I have been carrying it for nine years. Faber would have signed the implant order, embedded in a routine medical visit during my orientation year. I did not know I had one. The not-knowing was part of the design."

    n "It transmits coarse location, sector-level, not building-level. Resonance signature — a unique identifier if anyone scans for it. Aggregate cognitive-load via passive Band coupling. No audio, no content. Enough to find me. The transmission band is CAD-internal. Ghostline cannot easily intercept."

    t "How long has Echelon known where you are."

    n "Always. The leash has been transmitting since the broadcast. The base location has been in the CAD-internal grid for seven months. They have not raided. The not-raiding is operationally interesting and I do not have a complete answer for it yet. The leash exists. The use of the leash has been deferred."

    t "I am going to remove it."

    "Tessa says it as a statement, not a question. Her hand moves from the crown to the prep tray. She picks up the antiseptic pad."

    "Noelle does not move."

    n "No."

    "One word."

    "Tessa's hand stops. The antiseptic pad does not reach the field."

    t "Say more."

    n "I am refusing the removal."

    n "The leash is operationally significant. We have known, since the broadcast, that the rebellion is being tracked at sector resolution. We have not been raided because the leash is not the only intelligence Echelon is reading from us. The leash is a known channel. Known channels are containable. If we remove the leash, we change the intelligence profile Echelon has been reading. The change introduces an information shock. Information shocks generate operational responses. We do not currently have the bandwidth for the operational response we would generate."

    n "The corrected approach is closed-loop information control. We keep the leash active. We selectively shape the cognitive-load patterns the leash transmits. We feed Echelon the intelligence profile we want Echelon to read. We use the channel against itself. The use is operationally superior to the removal."

    n "I have been working through the closed-loop architecture for the last three weeks. I had not finalized the brief because I had not yet confirmed the leash's existence in the body. Your scan confirmed it. The brief is finalizable. I will brief Selene at oh-twelve-hundred."

    "She stops."

    "The room is quiet."

    "Tessa is still holding the antiseptic pad. She has not moved her hand back to the prep tray."

    # ========== PHASE 2 — THE STAY ==========

    # CAMERA: tight on Tessa. The decision the scene
    #         is going to make is the decision Tessa
    #         is going to make in the next ten seconds.
    #         The camera holds on her face for the
    #         decision.

    "Tessa does not respond immediately."

    "She does not argue the operational logic. She has heard Noelle's operational logic before. She has heard versions of it across nine other scenes in this base. The logic is logic. The logic does what logic does."

    "Tessa is not in the room to argue logic."

    "Tessa is in the room to do the work the room calls for."

    "She puts the antiseptic pad back on the prep tray. She picks up the scalpel — the one she had laid out, the one she would have used — and she sets it back in its slot in the instrument case. She picks up the small extraction tweezer and sets it back. She picks up the suture kit and sets it back."

    "The instruments return to the prep tray in the reverse order she laid them out. The sound is small mechanical clinks. The clinks are the sound of a procedure being un-prepared."

    "The clinks last twenty-two seconds."

    "Noelle watches the un-preparing without comment. Her face does not change."

    "Tessa finishes the un-preparing. She wipes her hands on the small towel at the basin. She does not wash the hands — they have not been used. The wiping is procedural punctuation."

    "She turns to Noelle."

    t "All right."

    "Two syllables. Plain."

    t "Then I'll watch the room."

    "Five words."

    "Tessa does not elaborate. Tessa does not say what watching the room means. Tessa does not say she is staying. Tessa does not say the friendship is not broken. The five words say all of it in the operational register Noelle has been using, which is the only register the OB room currently accepts."

    "Tessa moves to the surgical lights. She brings them down from full to working — the dim halfway level, the level she uses for follow-up appointments rather than procedures. The bright spot reduces to a working circle. The periphery comes up by a third. The room transitions from theater to follow-up."

    "She gestures at the chair across from the table."

    t "Sit. The appointment is forty minutes. We are going to use the forty minutes."

    "Noelle moves from the table to the chair. The movement is operational. She sits."

    "Tessa pulls the second chair over. She sits across from Noelle. The two chairs are at conversation distance, not consultation distance. Tessa has chosen the conversation distance deliberately."

    "She places her hands on her knees. Palms up. The posture is the working-doctor's posture for the patient she is not going to operate on. The palms are open."

    # ========== PHASE 3 — THE WATCHING ==========

    # CAMERA: two-shot. Tessa and Noelle in the same
    #         frame. The chair distance is tight enough
    #         that the two-shot does not need to widen.
    #         The composition holds for the bulk of the
    #         scene.
    # LIGHTING: dimmed to follow-up. The bright spot
    #           is gone. The peripheral darkness has
    #           come up. The room is the room.

    t "I am not going to argue the operational logic. I have heard the logic. The logic is internally consistent. I have followed the chain you laid out and I have not found a refutation. I am noting that I have not found a refutation. The not-finding is data. The data does not change my position on the appointment."

    n "What is your position on the appointment."

    t "I am going to ask you about your headaches because the headaches are the reason the appointment was scheduled and I am running the appointment as an appointment for headaches. The headaches are real. They are intensifying. The leash is a contributor — the cognitive-load coupling is loading your nervous system at a sub-clinical level — but the leash is not the only contributor. The doctrine work is a contributor. The doctrine work is the larger contributor. We are going to talk about the doctrine work."

    n "The doctrine work is operationally classified at command-tier and is not a clinical conversation."

    t "The headaches are clinical. The headaches are produced by the doctrine work and the leash and the not-sleeping. I am running a clinical conversation about the contributors to your headaches. The conversation is not asking you to declassify the doctrine work. The conversation is asking you to acknowledge that the doctrine work is contributing to the headaches and that the contribution is real and that the contribution is going to keep being real until something changes about the contribution."

    "Noelle's face does not change."

    n "Acknowledged."

    "She does not elaborate."

    "Tessa watches her for three seconds."

    t "Acknowledged is not an answer to what I asked."

    n "I do not have an answer to what you asked. I have a doctrine to draft. The doctrine is at four sections. The fifth section is in progress. The acknowledgment is the most accurate response the appointment has time for."

    t "The appointment has time. We have thirty-two more minutes. The appointment has been on your calendar for two days. You scheduled the time. The time is yours."

    n "The time is operationally allocated to the appointment. The appointment is a headaches appointment. The appointment is now a follow-up. The follow-up is medical advice and observation. I am ready to receive medical advice and observation."

    "Tessa does not respond immediately."

    "She is doing what she does at A2_P14 — pulling the patient into the work. The work this time is not surgical. The work is the work of being in the room with someone whose register is operating against the room. Tessa's tools for the work are the same tools she has always had: the question, the contact, the staying. She is going to use them."

    t "Are you sleeping."

    n "Operationally adequate."

    t "Are you eating."

    n "Operationally adequate."

    t "Are you in physical pain right now, this minute, beyond the headache baseline."

    n "No."

    t "Are you crying."

    n "No."

    t "Have you cried in the last week."

    n "No."

    t "Have you cried in the last month."

    "A pause."

    "The pause is a procedural pause. Noelle is checking her records. The checking is the work. The check returns nothing."

    n "No."

    t "Have you cried since the broadcast."

    n "No."

    t "Have you cried since you joined the rebellion."

    n "No."

    "Tessa does not flinch at the answer. She has been keeping the count of months. She has had the count in her clipboard. The count has been operational data on Noelle's clinical baseline for seven months. The count was the count. The count is now confirmed."

    t "Acknowledged."

    "She uses the word back. Same word, different intent. The word is now hers."

    "She does not push further on the question. She lets the answer stand. Pushing on it would be operating against the patient's stated boundary. Tessa does not operate against the patient's stated boundary. Tessa stays inside the boundary and waits for the boundary to soften. The waiting is the work."

    "She moves to the next question."

    t "Does the leash hurt."

    n "The leash does not have a pain response. It is passive. It has been transmitting at the same duty cycle for nine years. There is no associated nociceptive load."

    t "I am not asking the clinical question. I am asking whether the knowing-it-is-there hurts. The knowing is new since the scan. The knowing is twenty-four minutes old."

    "Noelle considers the question."

    nthought "The knowing is operationally significant. The knowing changes my model of my own bodily integrity. The change is informational, not nociceptive. The information is being processed. The processing has not produced a hurt response."

    nthought "I am noting that the working register is processing the question into the not-hurt answer."

    nthought "I am noting that the noting is a procedural reflex from the coda night."

    nthought "I am not going to elaborate on either notice."

    n "No. The knowing does not hurt."

    "Tessa does not believe the answer. The not-believing is in her face for half a second and is gone. The professional face returns. She moves to the next question."

    t "Is there anything you want to tell me, Noelle."

    "She uses the name. The use is deliberate."

    "Noelle's face does not change."

    n "The closed-loop brief is operationally relevant to the rebellion. The brief will be circulated at oh-twelve-hundred. You will receive the brief in the medical-cleared distribution. The brief includes a section on the cognitive-load shaping and the expected impact on patients carrying CAD-issue tags. The section will be useful for your clinical baseline going forward. There may be other carriers among defectors we have not yet scanned. I am noting the possibility for your records."

    n "That is the relevant disclosure."

    "Tessa nods slowly."

    t "Acknowledged."

    "She does not push on the *anything you want to tell me.* She has asked the question. The answer is the answer. The answer's accuracy is not Tessa's to litigate. The answer's accuracy will be litigated by time. Tessa has time."

    # ========== PHASE 4 — THE ROOM ==========

    # CAMERA: holds the two-shot. The chair distance.
    #         The follow-up light. The composition has
    #         not changed for fifteen minutes of story
    #         time. The not-changing is the
    #         composition's argument.

    "Tessa does not fill the next minute with a question."

    "She sits in the chair across from Noelle. Her hands are still on her knees. Palms still up. She does not look at her clipboard. She does not check the appointment timer. She does not consult her board. She is in the room."

    "Noelle sits across from her. Noelle's hands are on her knees. Palms down. Fingers spread. The not-typing posture from the workspace, brought into the chair. The posture is the posture. The posture is what Noelle does when the working register is on standby for re-engagement."

    "The working register is on standby."

    "Tessa is not going to re-engage it."

    "Tessa is going to sit. She is going to use the appointment time for the appointment time. She is not going to make the silence into a question. Noelle has answered the questions. Noelle has the right not to be asked the questions she has already answered. The silence is the medical instrument now."

    "The autoclave at the back of the room ticks."

    "The follow-up light hums."

    "Noelle watches the second hand on the wall clock advance. The watching is operational. She is using the watching to occupy the cognitive-load registry that the working register would otherwise be processing the silence with. The occupying is procedurally fine. The occupying is also the inverse of what is supposed to happen in this room. The occupying is the leash's mechanism applied to a room without a leash."

    nthought "The watching is a closed-loop technique. I am running closed-loop on Tessa's silence. The silence is the input. The watching is the output. The output is operationally adequate. The output is also the procedure I have been refusing the removal of."

    nthought "I am noting that. I am not going to act on it."

    "Tessa speaks twelve minutes into the silence."

    t "I am going to tell you a thing about A2_P14. I have been thinking about A2_P14 since you sat down."

    "Noelle's eyes shift from the clock to Tessa's face. The shift is procedural — Tessa has spoken, the patient is supposed to attend. The attending is the working register's response."

    n "Continue."

    t "When the runner stabilized — the twelve-percent runner, the one you put a clamp on — you said you needed to create a new parameter. You called the parameter *invested persistence beyond statistical justification.* I told you the simpler word was care. You said you would need to operationalize that."

    t "You operationalized it."

    t "I have been watching you operationalize it for a year and four months. You have applied the parameter to Aeron. You have applied it to Selene before Selene died. You have applied it to Zira. You have applied it to your own work product. The parameter has been load-bearing in your operational decision-making since A2_P14."

    "She pauses."

    t "I am noting that the parameter is not currently being applied to you. The parameter has been off-line in your self-directed processing for a duration I am not going to quote, because the quote would imply a measurement, and the measurement would imply that you would receive the measurement, and I am not asking you to receive anything tonight."

    t "I am noting it for my records."

    t "I am also noting it for yours, because my records and your records have been overlapping at a higher rate in the last six months than in the previous year, and I want the overlap to be honest in both directions."

    "Tessa stops."

    "Noelle has been watching her face for the duration. Her face has not changed."

    "Inside her, the working register processes Tessa's sentence."

    nthought "The parameter Tessa is naming is the parameter I built from her teaching. The parameter is operational across multiple decision contexts. The parameter is not currently active in self-directed processing. The non-activity is consistent with the doctrine register's compression of the personal layer."

    nthought "Tessa is naming the compression."

    nthought "Tessa is not asking me to decompress."

    nthought "Tessa is logging the compression in her records and informing me she is logging it."

    nthought "Acknowledged."

    n "Acknowledged."

    "She says the word aloud."

    "Tessa nods once."

    t "Thank you for hearing the noting."

    n "I heard the noting."

    "She does not say anything else."

    "The silence resumes."

    "It holds for the remaining twelve minutes of the appointment."

    # ========== PHASE 5 — THE RELEASE ==========

    # CAMERA: pulls back to wide. The medbay theater
    #         in its follow-up configuration. Tessa in
    #         one chair, Noelle in the other, the
    #         second hand ticking, the autoclave
    #         ticking, the follow-up light humming.
    #         The composition has held for thirty-five
    #         minutes of story time.

    "At oh-nine-twenty Tessa stands."

    "She is precise about the time. The appointment was forty minutes. Forty minutes have elapsed. The release is operational."

    t "Appointment closed. You can go."

    "Noelle stands. Her balance is steady. The headache baseline is unchanged. The leash is still in her body, transmitting at the same duty cycle to the same band, identifying her at sector resolution to the same monitoring desk at CAD it has been identifying her to for nine years."

    "She does not say thank you."

    "She does not say anything."

    "She walks to the medbay door. At the door she pauses. Not the half-second pause Aeron made at the alcove last night. A standard procedural pause — checking that the appointment debrief is complete before exiting the room. Tessa watches the pause."

    t "Noelle."

    "Noelle turns half a quarter. Not enough to face Tessa. Enough to acknowledge."

    n "Yes."

    t "The next appointment is in two weeks. I am scheduling it now. You will receive the calendar invite at oh-ten-hundred."

    n "Acknowledged."

    t "I will be here. The room will be the room. Whatever you bring, I will receive."

    "She does not say *whatever you do not bring, I will receive.* The unsaid clause is in the said clause. The said clause carries it."

    "Noelle does not respond."

    "She turns the rest of the quarter and walks through the door."

    "The door closes."

    # ========== PHASE 6 — THE WATCHER ==========

    # CAMERA: tight on Tessa. She is alone in the
    #         medbay. The chair Noelle sat in is
    #         empty. The clipboard is on the prep
    #         tray. The instruments are still in
    #         their case, returned to the prep tray
    #         in reverse order from this morning's
    #         laying-out. The room has held for
    #         forty minutes and is now empty of
    #         everyone except Tessa.
    # LIGHTING: follow-up dim. The autoclave's tick.
    #           The hum of the lights at half.

    "Tessa stands in the empty medbay for a count of nine."

    "She does not know she is keeping the count. She has been keeping the count for the last six months without naming it — a private interval she allows herself between an appointment that has not gone the way she would have wanted and the next operational decision. The count is hers. The count does not propagate to anyone."

    "At nine she walks to the prep tray."

    "She picks up her clipboard. She makes the appointment note. The note reads: *NOELLE KORR — 30 FORGE 390 0840 — RESONANCE SCAN POSITIVE FOR CAD-ISSUE TAG. PATIENT REFUSED REMOVAL ON OPERATIONAL GROUNDS. APPOINTMENT CONTINUED AS HEADACHE FOLLOW-UP. PATIENT REPORTS CRYING ZERO TIMES SINCE BROADCAST. NEXT APPOINTMENT 14 GLASS 390 0840.*"

    "She does not write *parameter offline.*"

    "She does not write *patient is glass.*"

    "She does not write *the friendship is not broken; the patient is.*"

    "She writes the operational record. The record is the record. The record does not include the part of the appointment that was hers."

    "She closes the clipboard."

    "She returns to the autoclave. She begins the next prep cycle. The next patient is at oh-ten-thirty."

    "The work continues."

    "Inside Tessa, the watching continues."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("noelle_implant_discovered_ob", True)
    $ flag("noelle_implant_kept_ob", True)
    $ flag("tessa_noelle_anchor_ii_complete_ob", True)
    $ flag("tessa_watching_room_ob", True)
    $ canon_set("noelle.implant_status_ob", "active_voluntarily")
    $ canon_set("noelle.implant_carry_duration_years", 9)
    $ canon_set("noelle.closed_loop_information_control_brief_pending", True)
    $ canon_set("noelle.cried_since_broadcast_ob", False)
    $ canon_set("noelle.tessa_disclosed_halen", False)
    $ canon_set("tessa.has_noelle_halen_information", False)
    $ canon_set("tessa.parameter_offline_observation_logged", True)
    $ canon_set("tessa.next_appointment_set", "14_glass_390_0840")
    $ canon_set("tessa.watching_room_active", True)
    $ rel_bump("Tessa", trust=1, complicity_concern=2)
    $ npc_remember("Tessa", "scanned_noelle_found_aether_tag", weight=2)
    $ npc_remember("Tessa", "did_not_walk_away_from_refusal", tone="hand_that_stays")
    $ npc_remember("Tessa", "named_parameter_offline_in_self_directed_processing", tone="logged_for_records")
    $ npc_remember("Tessa", "scheduled_two_week_follow_up", tone="watching_room_continues")
    $ npc_remember("Tessa", "kept_count_of_nine_unknowingly", tone="private_interval_after_unwon_appointment")
    $ npc_remember("Noelle", "refused_implant_removal_closed_loop_brief_planned", weight=2)
    $ npc_remember("Noelle", "did_not_disclose_halen_to_tessa_ob", tone="information_sealed_inside_register")
    $ npc_remember("Noelle", "answered_no_to_crying_questions", tone="boundary_stated_register_held")
    $ npc_remember("Noelle", "occupied_silence_with_clock_watching", tone="closed_loop_applied_to_room_without_leash")
    $ tp_seed("a4.tessa.watching_room")
    $ tp_seed("a4.noelle.parameter_offline")
    $ tp_seed("a4.noelle.halen_sealed_from_tessa_ob")
    $ tp_seed("a4.tessa.glass_moment_seed")
    $ scene_mark(_current_scene_id, "completed")
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s10b_implant_tessa_ob
# cann.chapter: Act IV — Violence Normalized — TESSA × NOELLE ANCHOR II
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Morning of 30 Forge 390 AC. Oh-eight-forty. Approximately
#     twenty-three hours after the close of a4_s10a (Defection
#     Coda OB). The appointment was scheduled two days prior for
#     low-grade headaches. The appointment is forty minutes. The
#     scene runs the full forty minutes plus the post-appointment
#     beat with Tessa alone.
# cann.what_happened:
#   - Tessa runs a routine resonance scan and detects the CAD-issue
#     Aether Tag at the base of Noelle's skull. Same diagnostic
#     phase as the EMP version.
#   - Noelle identifies the tag from the CAD-internal scanner-band
#     acknowledgment. Confirms what it is: the leash. Nine years.
#     Faber-signed implant order. Sector-level location, resonance
#     signature, Band coupling.
#   - Tessa announces the removal as a statement, not a question.
#     Picks up the antiseptic pad.
#   - NOELLE REFUSES. "No." One word. Then the operational logic:
#     closed-loop information control. The leash is a known channel,
#     known channels are containable, removing the leash introduces
#     an information shock the rebellion cannot afford. The brief
#     for closed-loop architecture has been drafted for three weeks;
#     she will brief Selene at oh-twelve-hundred.
#   - TESSA DOES NOT WALK AWAY. Tessa returns the instruments to the
#     prep tray in reverse order — twenty-two seconds of small
#     mechanical clinks, the sound of a procedure being un-prepared.
#     Then: "All right. Then I'll watch the room." Five words.
#   - The room transitions from theater to follow-up. Surgical
#     lights dimmed to working level. Two chairs placed at
#     conversation distance. Tessa sits opposite Noelle, hands on
#     knees, palms up. Hands open. The not-walking-away is the
#     scene's load.
#   - Tessa runs a clinical-baseline conversation. Asks about
#     sleep, eating, pain, crying. The crying questions step
#     down through intervals: this minute, last week, last
#     month, since the broadcast, since joining the rebellion.
#     Noelle answers "No" to all of them. "Have you cried since
#     the broadcast." "No." Tessa logs the count without flagging
#     it.
#   - Tessa asks: "Does the leash hurt." The clinical question
#     and the relational question. Noelle: "No. The knowing
#     does not hurt." The not-believing in Tessa's face for
#     half a second. The professional face returns.
#   - Tessa asks: "Is there anything you want to tell me,
#     Noelle." Use of the name is deliberate. Noelle's
#     response: a closed-loop brief disclosure. Operational.
#     The Halen information is not disclosed. Tessa does not
#     learn about Halen on OB. The information remains sealed
#     inside Noelle's register.
#   - Twelve minutes of silence in the chairs. Noelle uses the
#     wall clock to occupy the cognitive-load registry — the
#     closed-loop technique applied to a room without a leash.
#     Notes the irony in nthought without acting on it.
#   - Tessa names A2_P14. Recalls the parameter Noelle built from
#     "care" — *invested persistence beyond statistical
#     justification.* Names that the parameter is currently
#     offline in Noelle's self-directed processing. Logs the
#     observation for her records and notes the logging for
#     Noelle's. "I want the overlap to be honest in both
#     directions."
#   - Noelle: "Acknowledged." Hears the noting. Does not engage.
#   - Twelve more minutes of silence. The appointment closes at
#     oh-nine-twenty.
#   - Tessa releases. Schedules the next appointment for fourteen
#     days out. Tessa at the door: "I will be here. The room will
#     be the room. Whatever you bring, I will receive." The
#     unsaid second clause — *whatever you do not bring, I will
#     receive* — is in the said clause.
#   - Noelle leaves without saying thank you. Without saying
#     anything.
#   - Tessa alone. Stands for a count of nine — unknowingly
#     keeping a count she has been keeping for six months without
#     naming. Writes the operational record. Does not write
#     "parameter offline." Does not write "patient is glass."
#     Does not write "the friendship is not broken; the patient
#     is." Begins the next prep cycle. The watching continues.
# cann.tessa_state:
#   - Identifies the implant. Recommends removal as a statement.
#     Hears the refusal. Hears the operational logic. Does not
#     argue.
#   - Stays. The not-walking-away is the canonical OB-Tessa
#     position. Her character is the hand that stays. The scene
#     is the canonization of the staying as a structural
#     position rather than a single decision.
#   - Runs a clinical-baseline conversation as the appointment's
#     replacement work. The conversation is the work. Tessa's
#     tools — the question, the contact, the staying — are the
#     same tools she has always had. She uses them.
#   - Names the parameter-offline observation. Logs it for
#     records (hers, Noelle's). The naming is the explicit
#     framing of the OB cost — Noelle has been applying *care*
#     to others and not to self for an interval Tessa has been
#     measuring.
#   - Schedules the next appointment. The watching continues at
#     two-week intervals. The appointment cadence is the
#     scaffolding Tessa is going to use to be present until
#     Noelle can receive.
#   - Stands for a count of nine after Noelle leaves. Writes the
#     operational record. Does not write the personal record.
#     The omission is parallel to Noelle's omission of the Halen
#     disclosure — both characters are protecting the friendship
#     by what they do not write.
# cann.noelle_state:
#   - Refuses the implant removal on operational grounds. The
#     closed-loop brief is real and is being prepared for
#     Selene at oh-twelve-hundred.
#   - Does not disclose Halen. The Halen information is sealed
#     inside the working register. Tessa never learns Halen's
#     name on the OB path through this scene.
#   - Answers "No" to all clinical-baseline questions truthfully
#     in the OB working register's terms. Has not cried since
#     the broadcast. The not-crying is canonical and is the
#     metric of the register's success at containing the
#     personal layer.
#   - Notices, in nthought, that her clock-watching during the
#     silence is a closed-loop technique applied to a room
#     without a leash. Does not act on the noticing. The
#     noticing is filed.
#   - Hears Tessa's parameter-offline naming. Files the
#     hearing. Says "Acknowledged." Does not engage with the
#     content of the naming. The content is correct. The
#     correctness does not produce a response.
#   - Leaves without saying thank you. Without saying anything.
#     The silence is the scene's final OB note.
# cann.path_tracking:
#   - OB path only. Structural twin of a4_s09b_implant_tessa_emp.
#     Same diagnostic, same offer, opposite response, opposite
#     trajectory. Where EMP is the leash cut and the grief named
#     aloud, OB is the leash kept and the grief sealed. The
#     friendship is not broken on OB — that was the user-revised
#     canon. Noelle is. What withdraws is her capacity to
#     receive what Tessa is offering.
# cann.thematic_flags:
#   - "All right. Then I'll watch the room." — the canonical
#     Tessa stay-line. Five words. The scene's thesis. Tessa's
#     character is the hand that stays; the scene canonizes
#     the staying as a structural position the friendship will
#     hold across the rest of the OB path.
#   - The parameter-offline observation. Tessa names that
#     Noelle's care-parameter — the one Tessa taught her in
#     A2_P14 — is currently not active in Noelle's self-
#     directed processing. The naming is the explicit OB cost
#     in the friendship register: the gift Tessa gave, returned
#     to others but not to self.
#   - The Halen information is sealed inside Noelle on OB.
#     Tessa never learns. This is the OB cost in the
#     information layer — what would have been shared is not.
#     The withholding is not Noelle's choice in any conscious
#     sense; it is the working register's compression. The
#     compression is the OB Noelle's default.
#   - The Glass Moment seed. Tessa's "I will be here. The room
#     will be the room. Whatever you bring, I will receive."
#     is the seed of the late-Act-4 OB Glass Moment scene
#     (canon_notes_noelle.md sec 11.6). The seed is planted
#     here. The payoff is in the later scene where Tessa's
#     care language passes through Noelle without landing.
#   - "Closed-loop information control" applied to a room
#     without a leash — Noelle's nthought during the twelve
#     minutes of silence. The OB working register treats
#     human conversation as a leash channel. The treatment is
#     the OB cost in the relational register made visible to
#     Noelle herself. She files the visibility without acting.
# cann.character_moments:
#   - Tessa: returns the instruments to the prep tray in
#     reverse order. Twenty-two seconds of small mechanical
#     clinks. The sound of a procedure being un-prepared.
#     The auditory signature of staying without operating.
#   - Tessa: hands on knees, palms up. The working-doctor's
#     posture for the patient she is not going to operate on.
#     The palms open across the full appointment.
#   - Tessa: "Have you cried since the broadcast." The crying
#     questions stepped down through intervals. The count
#     confirmed.
#   - Tessa: names A2_P14 by name. Names the parameter Noelle
#     built. Names the parameter's current offline status.
#     The naming is the most explicit framing of the OB cost
#     in any Tessa scene to date.
#   - Tessa: the stay-line. "All right. Then I'll watch the
#     room." Five words.
#   - Tessa: "I will be here. The room will be the room.
#     Whatever you bring, I will receive." The unsaid second
#     clause carried inside the said clause.
#   - Tessa: count of nine after Noelle leaves. The mirror
#     of Noelle's count from the coda. Tessa does not know
#     she is keeping the count.
#   - Noelle: "No." One word. The fastest decision Noelle
#     makes in any Act IV OB scene.
#   - Noelle: clock-watching as closed-loop technique applied
#     to a room without a leash. The recursive observation
#     filed without action.
#   - Noelle: leaves without saying thank you. The silence
#     is the scene's final OB note.
# cann.callbacks:
#   - a2_s18 (A2_P14 "The Patient"): named explicitly in
#     scene by Tessa. The parameter Noelle built from
#     Tessa's *care* is the foundation Tessa names in the
#     parameter-offline observation. The structural callback
#     is foregrounded.
#   - a4_s10a_noelle_coda_ob: the audit-and-keep posture is
#     active throughout. The Faber containment principle —
#     "the trail of the editing must be smaller than the
#     trail of the un-editing" — is the principle behind
#     keeping the leash. The application is consistent.
#   - a4_s10_noelle_doctrine_ob: the working register, the
#     Vance default, the "Acknowledged" register. All
#     active.
#   - canon_notes_noelle.md sec 3 (The Implant): the OB
#     branch — implant kept active voluntarily — is
#     delivered as canonized.
#   - canon_notes_noelle.md sec 11.3: the OB version of the
#     Tessa anchor is delivered per the user-revised spec
#     (Tessa stays; Noelle's capacity withdraws).
#   - canon_notes_noelle.md sec 11.6: the Glass Moment seed
#     is planted for the late-Act-4 OB scene.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. OB path only. The
#     OB Tessa-Noelle anchor. Foundational for: the
#     fortnightly Tessa-Noelle appointment cadence on OB,
#     the Glass Moment scene in late Act 4 OB, every
#     subsequent OB scene where Tessa is present and
#     Noelle's capacity-to-receive is the relational
#     question.
# cann.requires_followup:
#   - Two-week appointment cadence is now established. The
#     14 Glass 390 appointment is on the calendar. Whether
#     to author the next appointment is open territory. The
#     cadence itself is canon.
#   - The closed-loop information control brief is being
#     delivered to Selene at oh-twelve-hundred. The brief
#     scene is unwritten. Author at discretion.
#   - The leash remains active on OB. Future OB scenes
#     should treat Noelle as continuously transmitting at
#     sector resolution. The shaped cognitive-load patterns
#     are part of OB Noelle's operational practice from
#     this scene forward.
#   - The Halen information is sealed from Tessa on OB.
#     Future OB scenes should respect that Tessa does not
#     know about Halen. If a future OB scene wants to
#     surface Halen to Tessa, it must do so through a
#     different vector (Aeron telling Tessa, Selene
#     telling Tessa, or Noelle's register cracking) and
#     the cracking would be the friendship's reset.
#   - The Glass Moment scene is the next Tessa-Noelle
#     scene to author on OB. Per canon_notes_noelle.md
#     sec 11.6, it is a single 30-second beat threaded
#     into a4_s10_noelle_doctrine_ob's vicinity. The seed
#     is planted; the payoff is pending.
# =========================================================
