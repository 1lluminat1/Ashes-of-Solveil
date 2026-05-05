# =======================================================
# ACT 4 - Scene 10a: The Smaller Trail (Obedience Path)
# File: a4_s10a_noelle_coda_ob.rpy
# Type: NOELLE CODA — post-s10 defection-data audit
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s10a_noelle_coda_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s10a_noelle_coda_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Same data alcove discipline as s10. The
    #         coda begins moments after the s10 close — Aeron is already in
    #         the ops room, the author's note is saved private, the doctrine
    #         is at three hundred words of Section II beneath the AUTHORIZED
    #         signature field. Noelle is at her primary workstation. The
    #         alcove door is closed, status indicator grey. The whiteboard
    #         of seven names is on the secondary screen at eighth-luminance.
    #         The amber lamp is still unplugged.
    #         Coverage is symmetrical with s10: medium single from behind
    #         Noelle's shoulder, reverse on her face lit blue-white by the
    #         primary screen, two-shot when the screens become important.
    #         The crystal stand has nothing on it — the projection crystals
    #         from EMP path do not exist on OB path. There is only the
    #         primary screen, the secondary screen, the workstation, the
    #         drawer, the chair angled for a reader that no one is going
    #         to take.
    # LIGHTING: Drafting setting. Primary screen 80% luminance. Secondary
    #           at eighth (the seven names ghosted). Single cold overhead
    #           strip. The corridor light spill from the s10 door-open is
    #           gone — the door is closed. The amber lamp on the secondary
    #           workstation remains unplugged for the entirety of the
    #           coda. The unplug is the scene's longest visual constant.
    # SFX: Loop — data alcove ambient at drafting setting. Crystal arrays
    #      at standby hum (half what it was in a3_s16). Vent. The keystroke
    #      sound is active and does not stop at any point in the scene.
    #      One-shots: drawer-lock chime (Phase 2), drawer release, crystal-
    #      reader chime as it accepts the slot. The alcove door does not
    #      open during the coda. No second visitor.
    # FACE: Noelle alone. The face that walked Aeron out of s10 — the
    #       writing-composure face, the woman who has found the posture
    #       for a thing she did not have a posture for yesterday. The face
    #       does not change across the scene. The constancy is the point.
    # BLOCKING: Noelle at the workstation. Forty-degree chair angle held
    #           from s10 — preserves access to primary screen, peripheral
    #           on secondary. She does not stand. She does not leave the
    #           chair. The chair is the operational center.

    # ========= VOICE BASELINE =========
    # nthought heavy. Noelle alone, no audience. The voice is the register —
    # cold, ceremonial, technical-regular. The register does not crack at
    # any point in the scene. The register processes each revelation and
    # files it. The horror of the scene is the absence of any failure.
    # No plain sentences. No grief. No "All right." The instrument that
    # corrects her on plain sentences is fully operational.

    # scene bg_data_alcove_drafting with dissolve
    # play ambient "sfx/ambient/data_alcove_drafting.ogg" fadein 2.0

    # ========== PHASE 1 — THE CONTINUATION ==========

    # CAMERA: 50mm locked. Same coverage Noelle wrote
    #         Section I in. The author's note save dialog
    #         from s10 has cleared. The cursor is at the
    #         end of the third paragraph of Section II.
    # SFX: keyboard active, low keystroke. The register
    #      sound. Continuous from s10.

    "The author's note is saved. The save completed at 0947:33. Aeron has been gone for one minute and twelve seconds. The doctrine is at three hundred words of Section II. The cursor is at the end of the third paragraph. The register has not stopped."

    "Noelle types the fourth sentence of the paragraph. The keys make the clean low sound. The sentence resolves under her fingers in the cadence she has used for nine years."

    "She reads what she has typed."

    nthought "I am writing in his voice."

    "She does not stop typing. The keystroke continues across the second clause of the next sentence and only halts at the period. The hands lift the standard half-inch. The half-inch is the working pause she allows herself between sentences when the register is engaged. It is not a stop. It is a beat."

    nthought "The paragraph contains three Faber syntax tells. The conjunction pattern. The scope-narrowing rhetorical move at the second sentence. The institutional symmetry of the closing clause. I learned all three from Faber. They are correct technique for this document. The document is a CAD-register doctrine and the CAD register is what Faber taught me."

    nthought "This is appropriate."

    "The cursor blinks. The register sound resumes. She types the next sentence and finishes the paragraph and starts the fifth paragraph and writes for forty more seconds without interruption."

    "Then she stops."

    "The stop is not the kind of stop that interrupts the register. The stop is a procedural stop — the kind of stop she would make if she were running a routine check on the document's structural integrity. The check is on her schedule. The schedule has been the same for nine years."

    nthought "I have not opened the personal data crystal in seven months and eleven days."

    nthought "Operational hygiene requires a periodic audit. The audit is overdue. The audit is the kind of overdue that would, if anyone were tracking the timing, register as a procedural lapse. No one is tracking the timing. I am tracking the timing. The timing has crossed my own threshold for a procedural lapse."

    nthought "I am going to run the audit."

    "She does not pause to consider the timing. The audit is operationally indicated. Operationally indicated work is work that proceeds without consideration. The consideration would be the lapse. The audit is the correction of the lapse."

    "She does not stop drafting Section II. She lets the cursor blink at the start of the sixth paragraph. She will resume the paragraph after the audit. The audit is a fifteen-minute item. The fifteen minutes are factored into the day's remaining work budget. The doctrine arrives on Aeron's desk in approximately four days. There is time."

    # ========== PHASE 2 — THE DRAWER ==========

    # CAMERA: push-in on the lower-left drawer of the
    #         workstation. CAD-issue researcher drawer,
    #         biometric-locked. The push is medium-paced —
    #         not slow, not fast. The drawer is an item
    #         on the audit checklist. The camera honors
    #         the procedural register.
    # SFX: biometric chime, half-second hold, drawer
    #      release. Standard CAD-issue cadence. Two
    #      seconds of mechanical sound, no longer.

    "The lower-left drawer is biometric-locked. The lock has not been queried in seven months and eleven days. She places her right thumb on the pad."

    "The pad chimes."

    "She does not hold her thumb on the pad through the half-second window. She lifts the thumb at the chime's confirmation tone. The half-second hold window is a CAD design feature for researchers conducting sensitive audits. The window allows the researcher to withdraw the request without committing to the open. She has used the hold window in the past. She does not use it tonight."

    "The drawer releases. She pulls it open."

    "Inside: the small black personal data crystal. Beside it: a folded slip of paper. Beside the paper: nothing."

    "She reaches past the slip without unfolding it. She has not read the slip in seven months. She does not need to. The slip carries the sentence *This isn't support, it's editing,* in her handwriting, from the night before her defection. The sentence is filed. She wrote the sentence in a register that does not appear on any other CAD document. The register did not survive. The sentence remains. The sentence is documentary."

    "She picks up the crystal."

    "The crystal is at workspace ambient temperature. The cold is procedural. The cold is what cold should be on a sealed item that has been in a drawer for seven months. The cold confirms the seal. The seal is the integrity check. The integrity holds."

    "She slots the crystal into the secondary reader on the console."

    # ========== PHASE 3 — REVELATION ONE: HER OWN NAME ==========

    # CAMERA: tight on the secondary screen as the crystal
    #         loads. Directory structure resolves. Her
    #         hand on the navigation key — efficient,
    #         precise, no hesitation at branch points.
    # LIGHTING: secondary screen comes up to dominant.
    #           Primary screen at 80% holds. The amber
    #           lamp remains unplugged.

    "The crystal loads. The directory structure is the directory she compiled in the seventy-two hours before defection. The directory has not been accessed since."

    "She navigates to the folder labeled *me.*"

    "Inside *me*: nine hundred and fourteen CAD logs authored by KORR, N. Indexed by year, sub-indexed by quarter. The first entry she opens is a behavioral-cluster analysis from 14 Anvil 386. The file is twelve pages. The file names eleven citizens in three districts. The file recommends interventions for seven of them. She has no memory of writing the file."

    "She opens the second file. She has no memory of writing the second file either."

    "She opens the third, the fourth, the fifth. By the eleventh she has confirmed the pattern. Approximately three hundred of the nine hundred and fourteen files are dated to days her personal calendar marks as admin or light or empty. The pattern is consistent with the personal-edit thesis she compiled before defection. The pattern is documentary."

    nthought "The editing was thorough. The thoroughness is operationally consistent with Cognitive Architecture standards. The records I authored were preserved as inputs to subsequent CAD work — the editing did not waste the analytical product. The editing took the experience and kept the output. This is standard CAD methodology applied to internal personnel. I would not have designed it differently if I had been the one designing it. I would have refined it. I will refine it if I am ever in a position to."

    nthought "I am noting that I just thought *if I am ever in a position to.* The thought is a residue from the working register. The working register is not the register I am in tonight. The working register is the register of the doctrine I am drafting upstairs. The two registers are converging. The convergence is operationally efficient."

    "She closes the eleventh file. She does not open the twelfth. The pattern is established. The audit does not require exhaustive enumeration. The audit requires confirmation. The confirmation is given."

    "She files the result."

    nthought "*me/* — confirmed. Editing thesis intact. No new data."

    nthought "Filed."

    # ========== PHASE 4 — REVELATION TWO: HALEN ==========

    # CAMERA: still tight on the secondary screen. Her
    #         hand navigates from *me* to *Halen.* The
    #         folder open is procedural. Each file open
    #         is procedural. The procedure is efficient.
    # LIGHTING: secondary screen dominant.

    "She navigates to the *Halen* folder."

    "She opens the assignment log first."

    "*HALEN VANCE — REASSIGNED — OUTER WARDS RESONANCE RESEARCH STATION — INDEFINITE TERM — DATE OF REASSIGNMENT 03 EMBER 381 — AUTHORIZED BY FABER, R. (DIRECTOR, CAD)*"

    "She has read this line approximately one hundred and twenty times. The audit requires a cross-reference she has not performed. She opens the dispatch manifests."

    "Six manifests. Indexed by arriving personnel. She queries *VANCE, H.* against the full Outer Wards Resonance arrival record for 381 AC."

    "The query returns: NO RECORD."

    "She runs it against the broader window — 380 to 382. NO RECORD."

    "She runs it against the entire operational lifetime of Outer Wards Resonance Research Station. NO RECORD."

    "Halen never arrived."

    "The transfer was a fiction. Halen died on the day the records say they were reassigned. The cover has been operating for nine years."

    nthought "The transfer fiction is well-constructed. The fiction integrates with the routing data, the personnel-cost reporting, the periodic-status audits, and the inactive-correspondence file at the Outer Wards Resonance front office. Faber would have signed off on the fiction's design at every checkpoint. The fiction's longevity is evidence of its design quality."

    nthought "I have known this. I have known it the way one knows a thing at the back of a folder one has been refusing to open. The refusing was operationally permitted because operational requirements did not depend on the resolution. The resolution is now obtained."

    nthought "Halen is dead."

    nthought "Halen has been dead for nine years. The interval is the interval. The interval has been factored into my operational behavior since defection. The interval has been factored implicitly. The factoring becomes explicit now. Explicit factoring is more efficient than implicit factoring. The audit produces an efficiency gain."

    nthought "Someone gave me this. The fragments came from a SAD analyst whose face I cannot retrieve. The fragment of the name is *V—n* or *Vehn.* They were deleted before I could thank them. Their work product is in this folder. Their work product is now confirmed accurate. The confirmation is the closure of their open file in my evidence package."

    nthought "I am not going to dwell on the fragment. The fragment is administratively complete."

    "She files the result."

    nthought "*Halen/* — confirmed. Death thesis intact. Transfer fiction documented. SAD source's work product validated and closed. No new data."

    nthought "Filed."

    "The crying budget is not engaged. The crying budget has not been engaged in seven months. The crying budget is not allocated for tonight. The audit does not require the crying budget. The audit requires confirmation. The confirmation is given."

    # ========== PHASE 5 — REVELATION THREE: THE BASELINE ==========

    # CAMERA: tight on the secondary screen. Hand moves
    #         up two folder levels. Opens *baseline.*
    #         Scrolls to the metadata header. Reads.
    # LIGHTING: unchanged.

    "She opens *baseline.* Inside: her own NDI baseline file. The foundational document. The reference. The template."

    "The metadata header:"

    "*COHORT C-04 (PILOT) — LONGITUDINAL SUBJECT KORR, N. — STUDY DURATION: 359 AC TO 376 AC — PROJECT LEAD KORR, A. — CO-LEAD KORR, T. — SPONSORING DIRECTORATE: COGNITIVE ARCHITECTURE.*"

    "She reads the line."

    "The names in the project-lead bylines are her parents."

    nthought "The longitudinal study explains my facility with the framework. My parents' work is the foundation. My work is the extension. My career trajectory is operationally consistent with my origin. The trajectory was efficiently designed."

    nthought "The strategic assessment I read at my father's desk at age eleven contained the sentence *the projected civilian cost is within acceptable margins.* The cohort the assessment described was Cohort C-04. The cohort included me. I was one of the projected costs. The projection was within acceptable margins. I am inside the margin. I have been inside the margin for twenty years."

    nthought "The margin is a place where one can do useful work. The margin produced the analyst who designed NDI. The analyst who designed NDI is the analyst who is now drafting the structural admissibility of non-combatant target categories. The trajectory closes."

    nthought "I am closing it."

    nthought "Three other children were in Cohort C-04. The byline does not name them. The records elsewhere in the crystal might. I am not going to look for them tonight. The audit does not require it. The audit requires confirmation. The confirmation is given."

    "She files the result."

    nthought "*baseline/* — confirmed. Origin thesis intact. Parental project leads documented. Three other subject children remain unnamed in the available record. Future audit may require resolution. No new data tonight."

    nthought "Filed."

    "She does not open the file. The metadata header is sufficient. The metadata header is the document's working summary. The working summary is operationally complete."

    # ========== PHASE 6 — REVELATION FOUR: THE AUTHOR FIELD ==========

    # CAMERA: the slowest camera move in the scene. The
    #         cursor returns to the *me* sub-folder. The
    #         hand opens the 14 Anvil 386 file again. The
    #         metadata block resolves on screen. The push
    #         tightens on the AUTHOR field. The push is
    #         the camera doing the work Noelle's eye is
    #         doing. The eye is procedural. The push is
    #         the procedure made visible.
    # LIGHTING: the screen brightens. The amber lamp
    #           remains unplugged.

    "She returns to *me.* She opens the first file again. The behavioral-cluster analysis from 14 Anvil 386."

    "She reads the metadata block this time. All of it."

    "*FILENAME: bca_q3_386_d089.dat*"

    "*PROJECT: NDI INTERVENTION CASCADE — QUARTERLY REVIEW*"

    "*WORKING SESSION: 09:14 TO 18:42 ON 14 ANVIL 386 AC*"

    "*AUTHOR: VANCE, N.*"

    "*REVIEWING DIRECTOR: FABER, R.*"

    "She reads the AUTHOR field."

    "*VANCE, N.*"

    "Not Korr. The surname on every CAD document she has ever produced is Vance. The surname has been on her credentials, her registry entry, her badge, her professional correspondence, her published papers, her review submissions, her project assignments, her access pads, her wrist display, her quarterly evaluations, her annual appraisals. The surname has been on her hand every time she has signed her name in a professional context for the last nine years. The surname was on the doctrine signature field she handed Aeron earlier this morning."

    "Aeron read the surname. He did not ask. She did not explain."

    nthought "Vance is Halen's name."

    nthought "I took the name during the joining. CAD's bureaucratic register for partner-recognition. Researchers on classified projects could register joint professional identities for shared-credential access. The taking was administrative. The taking was edited along with the rest of the relationship. The surname was preserved by Faber's containment principle: the trail of the editing must be smaller than the trail of the un-editing. Untangling Vance from my professional identity would have required scrubbing nine years of paperwork across three sub-directorates. The scrubbing would have been more visible than the residue."

    nthought "Faber's principle is correct. I have applied it in my own work without naming it. The principle scales. The principle applies to the doctrine I am drafting upstairs. The principle applies to every signature I have placed on every Phoenix document. The principle is doctrine."

    nthought "The surname is operationally seamless. The surname has been operationally seamless for nine years. Removing the surname would not improve operational performance. Removing the surname would create an audit trail across all CAD-derived records that I can never operationally close. The audit trail would be larger than the residue. The trail of the un-editing must be smaller than the trail of the editing."

    nthought "The surname stays."

    "She does not feel anything when she thinks the sentence."

    "The not-feeling is also operational. The not-feeling is the working register holding. The working register holds because the working register is the register that processes everything in this room. The working register is correct. The working register is the register Faber taught her. The working register is the register that filed the eleventh log file at 14 Anvil 386 without remembering that 14 Anvil 386 was a working day. The working register is the register that has been her since she was twenty-three. The working register does not have a failure mode. The not-feeling is not a failure. The not-feeling is the register doing its job."

    nthought "The audit is complete."

    "She does not close the file. She lets the AUTHOR field stay on the screen. The AUTHOR field will close when she closes the crystal. She is not closing the crystal yet. The audit produced no new data and four confirmations. The four confirmations require a single closing entry in her private operational log. She types the entry."

    "She types it on the AUTHOR'S NOTE — INTERNAL — DO NOT PROPAGATE section of the doctrine. The same private section she opened in s10. The section that does not propagate to the review cycle, does not appear in the audit log, will not be read again."

    "*PERSONAL DATA CRYSTAL AUDIT 29 FORGE 390 — 0958 TO 1006. FOUR ITEMS CONFIRMED. NO NEW DATA. NO OPERATIONAL ADJUSTMENT INDICATED. NEXT AUDIT SCHEDULED 29 FORGE 391 OR ON OPERATIONAL TRIGGER, WHICHEVER FIRST.*"

    "She does not save the entry. The entry is in the private section. The private section saves automatically on close."

    # ========== PHASE 7 — THE HAND ==========

    # CAMERA: pull back from the secondary screen. Wide
    #         on the workstation — primary screen with
    #         the doctrine, secondary screen with the
    #         AUTHOR field still visible behind the
    #         private section, the drawer still open,
    #         the slip of paper still folded inside.
    #         Noelle's hand returns to the keyboard. The
    #         hand types. The hand goes to where the
    #         hand has gone for nine years.
    # LIGHTING: the secondary screen dims to its base
    #           drafting setting. The amber lamp remains
    #           unplugged. The room is the room.

    "She does not eject the crystal. The audit closes the crystal back in the drawer at the end of the next operational window. She does not remove the slip of paper from the drawer. The slip of paper is in the drawer. The drawer is open. The slip is folded. The folding holds."

    "She returns her hands to the primary screen."

    "She opens the doctrine. The doctrine has been queued in the foreground throughout the audit. Section II is at three hundred words. The cursor is at the start of the sixth paragraph. The signature field at the middle of the document is still authorized — AUTHORIZED, INCOMPLETE — Aeron's signature in the field, the audit line preserved. The field will not be re-signed at completion. The field is complete in the sense that matters."

    "She scrolls down. Past Section II. Past the unwritten Sections III through VII. To the bottom of the document, where Section VII will eventually end, where the signature block for the document's author lives. The author signature block is currently a placeholder — *AUTHOR: __________.*"

    "She places her hand on the keyboard."

    "Her hand types."

    "*NOELLE VANCE.*"

    "The same two words, the same technical-regular hand, the same absence of a middle initial. The signature is the signature she has placed on every CAD-derived document for nine years. The signature is the signature she placed in front of Aeron earlier this morning. The signature is operationally seamless. The signature is the signature."

    "She watches her hand type it."

    "She does not change it."

    nthought "The audit confirmed the surname's status. The status is residue. The status is operationally seamless. Removing the residue would generate an audit trail larger than the residue itself. Faber's containment principle applies. The principle is correct. The signature is correct."

    nthought "The doctrine is signed in the name the records know."

    nthought "The records know the name."

    "She reads the signature on the screen for three seconds. The reading is procedural. The procedure confirms the signature's correctness. The procedure does not produce any further finding."

    nthought "All right."

    "She catches the sentence. The sentence is two syllables, plain, not a category, not a finding. The sentence is the kind of sentence the working register would correct on a normal day."

    nthought "Imprecise. *All right* does not specify what is right or what the rightness is contingent on. The precise version is *the audit is complete and operationally consistent.* The precise version is the version I am keeping."

    nthought "Acknowledged."

    "She accepts the correction. The working register holds. The working register did its job. The working register did not allow the imprecise sentence to stand on the page."

    "She returns the cursor to the start of the sixth paragraph of Section II."

    # ========== PHASE 8 — THE CONTINUATION ==========

    # CAMERA: hold wide on the workstation. Noelle at
    #         the primary screen. The doctrine in front
    #         of her. The signature block is filled. The
    #         next paragraph is queued. The keystroke
    #         resumes. The keystroke sound is the same
    #         keystroke sound from the start of the
    #         scene. The room is the same room. Nothing
    #         visible has changed.
    # LIGHTING: the primary screen at drafting luminance.
    #           The secondary screen has dimmed to base.
    #           The seven names on the whiteboard are
    #           still ghosted at eighth-luminance. The
    #           amber lamp is still unplugged.

    "The keystroke resumes. The first sentence of the sixth paragraph resolves under her fingers. The cadence is the cadence. Faber's syntax tells are present. The institutional symmetry is present. The scope-narrowing rhetorical move at the second sentence will arrive in the next paragraph. The doctrine is on schedule."

    "She does not ride the eye-close from s10. She does not close her eyes for two seconds in this scene. The eye-close was an unscheduled item. The audit was a scheduled item. The audit is closed. The doctrine continues."

    "Aeron is in the ops room. The ops room is two corridors away. He is reading the day-three Sector 4 consolidation approach. He has not thought about the data alcove since he stepped through the door at 0941:17. He will not think about it again until the doctrine arrives in final form. The not-thinking is also operational."

    "He will read the doctrine once. He will not read it twice. The not-reading-twice is the metric. The metric holds."

    "The doctrine arrives in approximately four days. The signature block at the end will read NOELLE VANCE. Aeron will not register the surname on the second reading because there will be no second reading. He registered the surname on the first signing field. He did not ask. He will not ask. Neither of them will name the gap."

    "The gap is not named in this scene either. The gap was opened in the audit. The gap was filed in the audit. The audit is complete."

    nthought "The base functions."

    "She types."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("defection_coda_complete", True)
    $ flag("halen_discovered", True)
    $ flag("ndi_baseline_realized", True)
    $ flag("vance_kept_ob", True)
    $ flag("desk_recontextualized_ob", True)
    $ canon_set("noelle.coda_complete_ob", True)
    $ canon_set("noelle.halen_known", True)
    $ canon_set("noelle.halen_known_dead", True)
    $ canon_set("noelle.ndi_baseline_known", True)
    $ canon_set("noelle.parents_in_baseline_byline_known", True)
    $ canon_set("noelle.eleven_year_old_desk_recontextualized", True)
    $ canon_set("noelle.vance_origin_known_ob", True)
    $ canon_set("noelle.surname_signing_default_ob", "Vance")
    $ canon_set("noelle.faber_containment_principle_internalized", True)
    $ canon_set("noelle.crystal_audit_completed", True)
    $ canon_set("noelle.crystal_filed_back", True)
    $ canon_set("noelle.working_register_holding", True)
    $ canon_set("noelle.crying_budget_engaged", False)
    $ canon_set("ob.noelle.doctrine_author_signature_set", "NOELLE VANCE")
    $ rel_bump("Noelle", trust=-1, complicity=2)
    $ npc_remember("Noelle", "completed_personal_crystal_audit_filed_no_new_data", tone="audit_register_held")
    $ npc_remember("Noelle", "halen_death_confirmed_filed_administratively", tone="grief_register_unavailable")
    $ npc_remember("Noelle", "found_parents_in_baseline_byline_filed_as_career_consistency", tone="trajectory_closing")
    $ npc_remember("Noelle", "saw_vance_on_author_field_filed_as_residue_kept", tone="containment_principle_internalized")
    $ npc_remember("Noelle", "doctrine_signature_block_set_to_vance", tone="surname_held_voluntarily")
    $ npc_remember("Noelle", "all_right_corrected_to_acknowledged_inside_one_sentence", tone="register_corrected_plainness")
    $ tp_seed("a4.ob.noelle.crystal_audit")
    $ tp_seed("a4.ob.noelle.faber_principle_doctrine")
    $ tp_seed("a4.ob.noelle.three_other_children_in_cohort_c04_unfound")
    $ tp_seed("a4.ob.noelle.surname_kept_voluntarily")
    $ metric("noelle_compartments_unsealed", change=0)
    $ metric("noelle_compartments_audited_and_filed", change=1)
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s10a_noelle_coda_ob
# cann.chapter: Act IV — Violence Normalized — CODA
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Same morning as a4_s10. Approximately one minute after Aeron exits
#     the data alcove at 0941:17. Noelle has been alone for the duration
#     of the s10 author's-note save (which completed at 0947:33). The
#     coda runs from approximately 0948 to roughly 1010, including the
#     fifteen-minute crystal audit. By scene close she has resumed the
#     doctrine drafting at the start of Section II's sixth paragraph,
#     with the doctrine's author signature block now set to NOELLE
#     VANCE.
# cann.what_happened:
#   - Noelle catches her own writing in Faber's syntax (same trigger as
#     a4_s09a EMP). Files the recognition as appropriate technique:
#     "I learned all three from Faber. They are correct technique for
#     this document. The document is a CAD-register doctrine and the
#     CAD register is what Faber taught me. This is appropriate."
#   - No second realization. The filing succeeds. The register does not
#     escalate from tool to prison. The register consolidates. Faber's
#     room is the right room for this work.
#   - Schedules the personal-data-crystal audit as procedural hygiene.
#     The audit is overdue (seven months and eleven days). Treating it
#     as a procedural lapse rather than a moment of choice. Opens the
#     drawer without using the half-second hold window. Lifts the
#     thumb at the chime confirmation tone. The opening is efficient.
#   - Reaches past the slip of paper ("This isn't support, it's
#     editing") without unfolding it. The slip is filed. The slip is
#     documentary.
#   - Loads the crystal. Runs the audit through four folders:
#     1. *me* — opens eleven CAD logs. Confirms the personal-edit
#        thesis. Files the result as no-new-data. Notes that "the
#        editing was thorough; the records I authored were preserved
#        as inputs to subsequent CAD work — the editing did not waste
#        the analytical product." Notes that she would not have
#        designed it differently.
#     2. *Halen* — runs the dispatch-manifest cross-reference for
#        the first time. Confirms Halen never arrived at Outer Wards
#        Resonance. Halen died on the day the records say they were
#        reassigned. Files the result as confirmed. The crying budget
#        is not engaged. The whistleblower fragment (V—n / Vehn) is
#        filed as work-product-validated-and-closed.
#     3. *baseline* — opens the metadata header. Names her parents
#        (Anesh and Talen Korr) in the project-lead bylines. Names
#        her as Cohort C-04 (PILOT) longitudinal subject. Files the
#        result as career-trajectory-consistent. Recontextualizes the
#        eleven-year-old desk reading as her own cohort data — and
#        files the recontextualization as confirmation that her
#        trajectory closes. Does not search for the three other
#        children in the cohort. The audit does not require it.
#     4. *me* (returned) — reads the AUTHOR field on the 14 Anvil 386
#        file. *VANCE, N.* Recognizes Vance as Halen's surname.
#        Internalizes Faber's containment principle in scene: "the
#        trail of the editing must be smaller than the trail of the
#        un-editing." Decides the surname stays. The decision is
#        operational, not personal. The not-feeling is the working
#        register holding. The audit is complete.
#   - Files a private operational log entry in the AUTHOR'S NOTE —
#     INTERNAL section of the doctrine: "PERSONAL DATA CRYSTAL AUDIT
#     29 FORGE 390 — 0958 TO 1006. FOUR ITEMS CONFIRMED. NO NEW DATA.
#     NO OPERATIONAL ADJUSTMENT INDICATED. NEXT AUDIT SCHEDULED 29
#     FORGE 391 OR ON OPERATIONAL TRIGGER, WHICHEVER FIRST."
#   - Returns to the doctrine. Scrolls to the document's author
#     signature block. Types her name: NOELLE VANCE. Watches her hand
#     type it. Does not change it. Confirms the signature is
#     operationally seamless and removing it would generate an audit
#     trail larger than the residue. The signature stays.
#   - Catches herself thinking "All right." The sentence is plain,
#     not a category, two syllables. The working register corrects it
#     inside one nthought line: "Imprecise. *All right* does not
#     specify what is right or what the rightness is contingent on.
#     The precise version is *the audit is complete and operationally
#     consistent.*" Replaces the plain sentence with "Acknowledged."
#     The plain sentence does not survive the working register's
#     correction. The correction is the inverse of the EMP coda's
#     "None comes" — the correction comes. The correction always
#     comes on OB.
#   - Resumes the doctrine drafting at the start of Section II's
#     sixth paragraph. The keystroke sound is the same keystroke
#     sound from the start of the scene. Nothing visible has changed.
#     Aeron is in the ops room. He has not thought about the data
#     alcove since he stepped through the door. The doctrine arrives
#     in final form in approximately four days. He will read it once.
#     He will not read it twice. The not-reading-twice is the metric.
#     The metric holds.
#   - Scene closes on "The base functions." Same final framing as the
#     parent scene a4_s10. The phrase is unchanged. The phrase is
#     more loaded.
# cann.noelle_state:
#   - Coda complete. Four revelations landed. Each was filed as
#     confirmation of an existing thesis with no operational
#     adjustment indicated. The defection-data seal that has held for
#     seven months is not opened — it is audited and re-sealed.
#   - Vance kept on the doctrine signature block voluntarily. Faber's
#     containment principle is now her own working principle. The
#     surname-signing default for OB Noelle remains Vance from this
#     scene forward.
#   - The crying budget is not engaged. The crying budget has not
#     been engaged in seven months. The crying budget will not be
#     engaged on OB. This is canon.
#   - The working register held across the entire scene. The plain
#     sentence "All right" was corrected to "Acknowledged" inside one
#     nthought line. The register does not have a failure mode in
#     this version of the character.
#   - Three other children in Cohort C-04 (PILOT) remain unnamed and
#     unfound. The audit did not require resolution. Future audit
#     may require it. tp_seed
#     a4.ob.noelle.three_other_children_in_cohort_c04_unfound flags
#     the deferral.
#   - The slip of paper in the drawer ("This isn't support, it's
#     editing") was reached past, not read. The slip is filed. The
#     slip remains in the drawer.
# cann.aeron_state:
#   - Not in scene. He has been in the ops room since 0941:17. He has
#     not thought about the data alcove. He will not until the
#     doctrine arrives in approximately four days. He will read it
#     once. He will not read it twice. The signature on the doctrine's
#     author block will be NOELLE VANCE. He will not register the
#     surname on the read-once because the read-once does not have
#     the bandwidth for a question that was already not asked at
#     0941:17.
# cann.path_tracking:
#   - OB path only. Linear. No branching, no player choice. Coda to
#     a4_s10. Structural twin of a4_s09a_noelle_coda_emp — same four
#     revelations in the same order, opposite responses to each. The
#     EMP coda is the seal opening. The OB coda is the seal being
#     audited and re-secured.
# cann.thematic_flags:
#   - The horror of the absent failure: the working register does not
#     fail in this scene. The technical voice does not crack. The
#     plain sentence does not survive. The OB cost in the friendship
#     register (per the Tessa anchor §11.3) is mirrored here in the
#     interior register: Noelle has the same evidence as EMP Noelle
#     and processes it without the capacity to be reached by what it
#     means.
#   - Faber's containment principle internalized: "the trail of the
#     editing must be smaller than the trail of the un-editing."
#     This is the canonical OB principle for Noelle going forward.
#     Any subsequent OB Noelle scene where she chooses to leave a
#     visible artifact in place rather than remove it should reference
#     this principle, implicitly or explicitly.
#   - The Vance signature stays as the OB doctrine's authorship.
#     OB Noelle has signed her dead partner's name on a doctrine
#     authorizing civilian targeting. The doctrine is the document
#     that consolidates the regime's grammar. The signature on the
#     doctrine is the residue of an editing she now actively
#     preserves. The double-bind is intentional.
#   - The "All right" / "Acknowledged" correction is the OB
#     interior-monologue equivalent of the Tessa Glass Moment in
#     §11.6 — language landing in the room and failing to penetrate.
#     The correction comes from inside Noelle here; the failure to
#     receive Tessa's care comes from the same place. They are the
#     same mechanism. The OB cost is the mechanism's continued
#     operation.
#   - The audit-as-filing structure inverts the EMP coda's
#     filing-as-defense recognition. EMP Noelle realizes filing is
#     the move and refuses it. OB Noelle uses filing as the work and
#     refines it. The two scenes' relationship to the same verb is
#     the path system in concentrate.
# cann.character_moments:
#   - Noelle: lifts her thumb at the biometric chime without using
#     the half-second hold window. EMP Noelle held the full window.
#     OB Noelle does not. The procedural opening is the scene's
#     first character signal.
#   - Noelle: reaches past the slip of paper without unfolding it.
#     The slip is filed. The folding holds. EMP Noelle let the slip
#     stay in the drawer too — but EMP Noelle's filing was the
#     start of the unsealing; OB Noelle's is the audit confirming
#     the seal.
#   - Noelle: types and accepts NOELLE VANCE on the doctrine's
#     author signature block. The acceptance is operational. The
#     not-changing is voluntary.
#   - Noelle: catches "All right" and corrects it to
#     "Acknowledged" inside one nthought line. The correction is
#     the working register holding. The hold is the OB cost made
#     legible.
# cann.callbacks:
#   - a4_s10_noelle_doctrine_ob: direct parent. The coda picks up
#     one minute and twelve seconds after Aeron exits. The
#     keystroke continues unbroken. The doctrine's progress in this
#     scene is the structural continuation of s10's drafting work.
#   - a4_s09a_noelle_coda_emp: structural twin. Same four
#     revelations, same crystal, same drawer, same surname,
#     opposite responses. The EMP coda is the seal opening; the OB
#     coda is the seal audited and re-secured. The two scenes are
#     authored to be readable as a single decision viewed from
#     opposite paths.
#   - a3_s16_data_and_doubt_ob: the absence of the Name Mechanic.
#     EMP Noelle has the Name Mechanic. OB Noelle does not. The
#     surname kept on the signature block is a structural inversion
#     of the EMP scene's typing of "Noelle" alone for a count of
#     fourteen.
#   - canon_notes_noelle.md sec 2.1 (The Vance Surname): the OB
#     branch of the surname canon lands here. The default signature
#     remains Vance. Future Phoenix command documents from OB
#     Noelle will continue to read VANCE, N. on the byline.
#   - canon_notes_noelle.md sec 7 (Director Faber): the containment
#     principle is internalized and named in scene. Faber's voice
#     is now Noelle's working principle. The Faber compartment does
#     not open on OB. It expands.
# cann.block_status:
#   - MINOR SCENE, LOAD-BEARING. Linear. OB path only. Coda to
#     a4_s10. Foundational for: the OB Tessa anchor (the implant
#     conversation, where Noelle refuses removal on operational
#     grounds — the refusal is consistent with the audit-and-keep
#     register established here), the Glass Moment (§11.6), and any
#     subsequent OB scene where Noelle's drafting is path-coded.
# cann.requires_followup:
#   - The Cohort C-04 other-three-children plant is the same as in
#     EMP, deferred indefinitely on OB. tp_seed
#     a4.ob.noelle.three_other_children_in_cohort_c04_unfound.
#   - The Vance signature continues on every subsequent Phoenix /
#     OB-regime command document Noelle signs. The recovery seen on
#     EMP does not occur on OB. The audit trail will read VANCE, N.
#     across all OB Act IV and Act V documents from Noelle.
#   - The audit log entry filed in the AUTHOR'S NOTE — INTERNAL
#     section is now the Noelle-personal record of the night. The
#     entry will not be read again. The entry's existence is canon.
#   - The slip of paper remains in the drawer, folded. Reached past
#     but not removed. Future OB scenes where Noelle returns to the
#     drawer must respect that the slip has not been read.
#   - "The base functions" is now the second canonical close of an
#     OB Noelle scene. The phrase is doing escalating work: in s10
#     it described the doctrine's effect; here it describes the
#     interior. The phrase is reserved for OB Noelle. Do not deploy
#     it elsewhere.
# =========================================================
