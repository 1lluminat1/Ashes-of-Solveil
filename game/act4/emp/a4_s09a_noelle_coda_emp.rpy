# =======================================================
# ACT 4 - Scene 09a: The Author Field (Empathy Path)
# File: a4_s09a_noelle_coda_emp.rpy
# Type: NOELLE CODA — post-s09 defection-data revelation
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s09a_noelle_coda_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s09a_noelle_coda_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. The same workspace discipline as s03 and s09 — Noelle's
    #         rooms are always shot steady. The frame is her authority. The
    #         coda begins exactly where s09 closed: Noelle at the console,
    #         the door already closed behind Aeron, the workspace alone with
    #         her. The scene is ninety minutes of story-time compressed into
    #         a sequence of seven beats. The camera honors the compression
    #         by holding longer on each beat than the audience expects.
    #         The crystal stand is dark for the first phase. It activates
    #         in Phase 2 — not the projection crystal from s09, a different
    #         crystal: the small black personal data crystal she has not
    #         touched since the rebellion established the secondary base.
    #         The crystal lives in a drawer she does not open. She opens
    #         the drawer in Phase 2. The drawer-opening is the scene's first
    #         deliberate choice. Everything before it is muscle memory.
    # LIGHTING: Workspace, late. The three task lamps are at full when the
    #           scene begins. Over the course of the scene, she dims the
    #           overhead and brings the secondary screen up. By Phase 6,
    #           the only light that matters is the screen. By Phase 7, the
    #           screen has been cleared and the room is the lamps again,
    #           and the lamps look different than they did at the start of
    #           the scene because Noelle is looking at them differently.
    # SFX: Workspace ambient, second-shift quiet. The keyboard is active
    #      under her hands when the scene opens. It stops at the Faber
    #      recognition (Phase 1) and does not resume until Phase 7. The
    #      drawer opening is the scene's first SFX event. The crystal
    #      activation in Phase 2 is the second. The cross-reference
    #      dispatch query in Phase 4 is the third — a small system tone
    #      when the query returns "no record." There is no music bed.
    #      The scene refuses one. The scene is the silence between the
    #      events, and the silence is the work.
    # FACE: Noelle alone for the entire scene. No other speaker. The face
    #       has to do all of it. The face begins in the post-signing
    #       composure she walked Aeron out of the room with. By Phase 4,
    #       the composure is gone. By Phase 6, the face is the face of a
    #       woman reading a sentence she has read every day for nine years
    #       and finally seeing what it says. The scene is the seeing.
    # BLOCKING: Noelle at the console for the entire scene. She does not
    #           stand. She does not leave the chair. The chair is the room
    #           she has built around herself and the chair is what she has
    #           to sit inside while the room dismantles. The scene is the
    #           dismantling.

    # ========= VOICE BASELINE =========
    # nthought heavy. Noelle alone with herself, no audience. Her voice is
    # technical at the start — the post-signing register she walked Aeron
    # out of the room with. The technical register fails by Phase 4 and is
    # gone by Phase 6. By Phase 7, the voice is plain. The scene tracks the
    # failure of the technical voice across nine years of evidence she has
    # been carrying without seeing.

    # scene bg_noelle_workspace_late with dissolve
    # play ambient "sfx/ambient/workspace_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE LOCATOR ==========

    # CAMERA: 50mm locked. Noelle at the console, three-
    #         quarter from behind. The keyboard is active.
    #         The counter-framework lattice is still
    #         hovering above the crystal stand in its low-
    #         power maintenance mode — pale blue, names
    #         dimmed but still legible. The scene opens
    #         exactly where s09 ended: the door has just
    #         closed behind Aeron, Noelle has just said
    #         "I am paying attention" to the empty room,
    #         she has just turned back to the console.
    # SFX: keyboard active. Workspace hum. Second-shift
    #      quiet through the door.

    "The door closes. Noelle says the sentence to the empty workspace and turns back to the console. The lattice is still hovering — pale blue, the living arranged as a graph of decisions they have not yet made. She does not look at it."

    "She has three hours before the cot. Three hours is the gap between the framework signing and the moment she allows herself to sleep. Three hours is the sleep budget she calculated for herself at twenty-one-fifteen this evening, before Aeron arrived, when she was still planning the scene she had not yet had with him. The plan held. The sleep budget remains."

    "She opens the locator file. Marcus's analyst cell. She has located the cell to a six-block radius in the upper Cygnet district. The remaining work is the fine-grain — narrowing the radius to a single building, ideally a single floor, ideally a single suite. She has been doing fine-grain work like this since she was twenty-three. Her hands know the work. Her hands are still."

    "She types."

    "The first paragraph of the next analysis section resolves under her fingers in the clean low keystroke sound she thinks of, privately, as the register. The register she described to Aeron earlier without naming. The register she joined CAD inside. The register that has always been hers."

    "She reads what she has typed."

    nthought "I am writing in his voice."

    "She stops typing."

    "Her hands do not move. They remain on the keyboard the way she places them when she is about to switch registers — palms slightly forward, fingers spread, not lifting yet. The not-lifting is its own posture. She has not used it since the framework signing."

    nthought "The paragraph is two hundred and thirty words. Three of the four sentence structures are Faber's. The conjunction pattern is Faber's. The scope-narrowing rhetorical move at the second sentence is Faber's. I learned all of these from Faber. I have used them for nine years. I have used them in this register because the register absorbed them and the register is mine."

    nthought "The register is mine and the syntax inside the register is his."

    nthought "I noticed this when I was writing the framework earlier and I did not stop. The scene with Aeron required the writing to continue. The scene with Aeron is closed. There is no longer a reason for the writing to continue at the cost of the noticing."

    nthought "I am noticing now."

    "She lifts her hands from the keyboard."

    "She places them on her knees. Palms down, fingers spread, the way she places them when she is about to switch registers from one mode to another. The mode she is switching to does not have a name yet. The mode she is switching to is the mode she has been postponing for nine years."

    # ========== PHASE 2 — THE DRAWER ==========

    # CAMERA: push-in on the lower-left drawer of the
    #         console. The drawer has a single small
    #         biometric lock — a CAD-issue researcher
    #         drawer, retired, repurposed. The drawer has
    #         not been opened since the secondary base
    #         was established. The push-in is slow. The
    #         drawer is the scene's first deliberate
    #         choice and the camera honors it.
    # SFX: the drawer-lock query (small chime) and the
    #      mechanical drawer release. Two distinct sounds,
    #      a half-second apart. The half-second is the
    #      time her thumb spends on the biometric pad
    #      after the chime confirms her identity. She is
    #      not waiting for confirmation. She is waiting
    #      for herself.

    "The lower-left drawer of the console is biometric-locked. CAD-issue. The lock is rated for researcher-grade material — three-stage authentication, palm and pulse and ambient cognitive variance. She has not opened the drawer since the secondary base was established. Seven months and eleven days ago. The drawer's last access timestamp is in its memory."

    "She places her right thumb on the biometric pad."

    "The pad chimes."

    "She does not move her thumb. The chime confirms her identity. The lock is now in its half-second hold window — the window in which the user can withdraw the request without having opened the drawer. The hold window is a CAD design feature. Researchers were known to second-guess themselves at the threshold of a sensitive file."

    "She holds her thumb on the pad for the full half-second."

    "She does not withdraw."

    "The drawer mechanism releases."

    "She pulls the drawer open."

    "Inside: a single black personal data crystal, the size of a thumbnail, in a small foam well. Beside it: a folded slip of paper she has not looked at in seven months. Beside the paper: nothing else. The drawer is not deep."

    "She does not unfold the paper. She knows what the paper says. She wrote it the night before her defection, in her own handwriting, in a register that does not appear in any other CAD document she has ever produced. The paper says: *This isn't support, it's editing.* She does not need to read it again. She picks up the crystal."

    "The crystal is cold. It has been in the drawer at workspace ambient for seven months. The cold is the only thing about the crystal that is not exactly as she remembers."

    "She slots the crystal into the secondary reader on the console."

    # ========== PHASE 3 — REVELATION ONE: HER OWN NAME ==========

    # CAMERA: tight on the secondary screen as the crystal
    #         loads. The directory structure resolves —
    #         folders by year, sub-folders by quarter,
    #         sub-sub-folders by project code. Noelle's
    #         hand on the navigation key. She does not
    #         hesitate at any branch point. She knows the
    #         topology of her own evidence. She compiled it.
    # LIGHTING: the secondary screen is now the dominant
    #           light source. The amber of the lamps holds.
    #           The lattice projection above the crystal
    #           stand has dimmed itself, sensing low
    #           workspace activity, into its standby blue.

    "The crystal contents resolve on the secondary screen. The directory is the directory she compiled in the seventy-two hours before her defection. She has not opened it since. She has carried it across three safehouses and one base relocation without ever inserting it into a reader. The carrying was not preservation. The carrying was the postponement that allowed her to keep functioning."

    "She navigates to the folder labeled simply *me.*"

    "Inside *me*: a sub-folder of CAD logs authored by KORR, N. The CAD authorship attribution. The corpus of her professional work. There are nine hundred and fourteen files in the sub-folder. She compiled the index herself. She knows the file count by heart."

    "She opens the first file in the sub-folder. The file is a behavioral-cluster analysis from the third quarter of 386 AC. The file is dated 14 Anvil 386. She remembers 14 Anvil 386 as a light admin day. She remembers it that way because her own calendar marks it that way: *14 Anvil — admin, no clinical, early home.* The marking is her handwriting. The handwriting is from her personal calendar — the green one with the ink-stained corner, the calendar that lived on her desk in the CAD residence."

    "The file in front of her is twelve pages of behavioral-cluster analysis. The analysis names eleven citizens in three districts. The analysis recommends interventions for seven of them. The interventions are described in CAD's standard language: *cognitive alignment exercise, supportive frequency calibration, environmental adjustment.* The author is KORR, N. The timestamp is 14 Anvil 386, working session 09:14 to 18:42."

    "She did not work on 14 Anvil 386. She remembers the day. She remembers the light through the apartment window. She remembers what she had for breakfast — which she would not remember if she had spent the day at the office, because she does not remember breakfasts on working days. She remembers 14 Anvil because she did not work."

    "Except she did. The file says she did. The file is twelve pages of her own writing, in her own register, on a project she has no memory of, on a day she remembers as empty."

    "She opens the second file."

    "It is also hers. It is also from a day she remembers as empty."

    "She opens the third file."

    "She opens the fourth, the fifth, the sixth."

    "By the eleventh she has stopped opening them and is scrolling the directory as a single visual unit. Nine hundred and fourteen files. Approximately three hundred of them are dated to days her personal calendar marks as admin or light or empty. Her hands have known this for seven months. Her hands compiled the directory. Her hands are the reason the evidence exists. Her mind has been carrying the evidence in a sealed compartment with the sentence *I will look at this when I am ready* written on the seal, in her own handwriting, where the handwriting is also a CAD product."

    nthought "I am the evidence."

    nthought "I have been the evidence for seven months."

    nthought "The compartment was the postponement and the postponement was the second editing. I edited myself. I sealed the compartment. I told myself I would open it when I was ready."

    nthought "I am ready now because I have just signed a placement framework in front of Aeron. I am ready now because the framework is operationally indistinguishable from a CAD product. I am ready now because the only honest thing I can do for the framework is to read what I am made of before I run it."

    "She does not stop scrolling. The names in the file titles pass her eye in the way the names in her lattice pass Aeron's eye when he reads the framework over her shoulder. The names are the load. The load has been hers for nine years."

    # ========== PHASE 4 — REVELATION TWO: HALEN ==========

    # CAMERA: still tight on the secondary screen. Her
    #         hand navigates from *me* to a sibling folder
    #         labeled *Halen.* The folder has not been
    #         accessed since she compiled it in the
    #         seventy-two hours before defection. She has
    #         opened the folder twice in those seven months
    #         in her head, the way a person opens a box she
    #         knows the contents of without needing to look,
    #         to confirm that the contents are still there.
    #         The contents are still there. The look is what
    #         she has been postponing.
    # LIGHTING: secondary screen dominant. The amber lamps
    #           are quieter now. Workspace darker than at
    #           the start of the scene by perhaps a third.

    "The Halen folder is two folders down from *me.* She has not opened it since defection. The folder contents at the time of compilation: thirty-one personnel records, six dispatch manifests, two transfer authorizations, one assignment log."

    "She opens the assignment log first."

    "*HALEN VANCE — REASSIGNED — OUTER WARDS RESONANCE RESEARCH STATION — INDEFINITE TERM — DATE OF REASSIGNMENT 03 EMBER 381 — AUTHORIZED BY FABER, R. (DIRECTOR, CAD)*"

    "She has read this line approximately one hundred and twenty times. She has read it on her CAD console, on her personal terminal, on her wrist display, on the courier-network mirror she set up after defection in case the original system scrubbed the record. The line is the line. The line says Halen is at Outer Wards Resonance, year four of assignment. The line is the reason she has not searched. The line is the reason she has been carrying Halen as a person who is somewhere, not as a person who is gone."

    "She has never compared the line against the dispatch manifests."

    "She has had the dispatch manifests in this folder for seven months. The manifests are the operational record of every transfer in and out of Outer Wards Resonance Research Station between 380 AC and the date of her defection. She compiled them as part of her evidence package. She put them in the folder labeled Halen because they were Halen-relevant. She filed the assignment log and the manifests in the same folder and never opened both at the same session."

    "She opens the manifests now."

    "She runs the cross-reference. Six dispatch manifests, indexed by arriving personnel, time-stamped to the hour. The manifests are exhaustive — Outer Wards Resonance is a small station, processing perhaps six to ten arrivals per quarter, no exceptions for indefinite-term assignments. Indefinite-term assignments are a flag in the system because they are personnel-cost outliers. Every indefinite-term arrival in the manifests is logged with double-confirmation."

    "She queries the manifests for *VANCE, H.*"

    "The query returns: NO RECORD."

    "She runs it again. NO RECORD."

    "She queries the full personnel arrivals at Outer Wards Resonance for the entire week of 03 Ember 381. The query returns four arrivals, all named, none of them Halen. She queries the entire month. Eleven arrivals, none Halen. She queries the year. Forty-three arrivals across all of 381 AC. None Halen."

    "She has had this evidence in a folder beside the assignment log for seven months. She has been carrying Halen as someone working in a station Halen never arrived at. She has been writing Halen letters in her head and addressing them to a station with no Halen in it."

    nthought "Halen never arrived."

    nthought "Halen was never going to arrive. Halen was already gone before the assignment log was filed. The assignment log is the fiction. The reassignment is the cover. The cover has been operating for nine years."

    nthought "Halen died on 03 Ember 381."

    nthought "Halen died on the day the records say Halen was reassigned."

    "She closes her eyes for one second. She does not close them for longer. She does not have the budget."

    "She opens her eyes."

    nthought "Someone gave me this."

    nthought "I cannot remember their face. I have a fragment. *V—n.* Or *Vehn.* I think it was an analyst from Signal and Analytics — the directorate that would have noticed the manifest mismatch from a different angle than mine. I think they saw what was being done to me and routed encrypted fragments to my evidence package over a period of weeks. I think they were deleted before I could thank them."

    nthought "Their hands gave me the future they would not have."

    nthought "I have been carrying the future. I have not been reading it."

    "She does not cry. The tear ducts are not engaged. The crying budget is not available. The crying budget will arrive in a different scene, in a different room, in front of a different person — possibly Tessa, possibly Aeron, possibly no one. Tonight is the reading. Tonight is the seeing. The seeing is the work, and the work does not include the crying."

    # ========== PHASE 5 — REVELATION THREE: THE BASELINE ==========

    # CAMERA: tight on the secondary screen. Her hand
    #         moves from the Halen folder up two levels to
    #         a folder she has not opened since
    #         compilation: *baseline.* The folder name is
    #         technical, not personal. The contents are
    #         CAD-internal foundational documents. Her own
    #         NDI baseline file, indexed and cross-
    #         referenced.
    # LIGHTING: unchanged. Secondary screen dominant.

    "She moves up two folder levels. She opens *baseline.*"

    "Inside: her own NDI baseline file. The foundational document she designed NDI against. The reference. The template. The thing every other citizen's score is calibrated against. She has known this folder existed. She did not compile it from memory; she pulled it from the CAD archive in the seventy-two hours before defection. She put it in the crystal because she suspected it would matter. She has not looked at it."

    "She opens the file."

    "The metadata header is the first thing the document presents. The metadata header has been the same for two decades. She has seen the format on every NDI-derived document since she joined CAD. The format is standard CAD project-attribution boilerplate."

    "*COHORT C-04 (PILOT) — LONGITUDINAL SUBJECT KORR, N. — STUDY DURATION: 359 AC TO 376 AC — PROJECT LEAD KORR, A. — CO-LEAD KORR, T. — SPONSORING DIRECTORATE: COGNITIVE ARCHITECTURE.*"

    "She reads the line."

    "She reads it again."

    "The names in the project-lead bylines are her parents."

    "Her parents' names are in the byline of her own foundational data."

    nthought "Anesh and Talen Korr. Project lead and co-lead. Cohort C-04. Pilot study. Seventeen years of longitudinal data. Subject zero. Me."

    nthought "I was four when the study started. I was eleven when I read the desk."

    nthought "I read the desk when I was eleven and the desk had a strategic assessment on it and the assessment had the sentence *the projected civilian cost is within acceptable margins* in it. I did not understand the sentence at eleven. I understood it by the time I was twelve. I have remembered the sentence for twenty years. I have remembered the sentence as the sentence that turned me into an analyst because I did not want to be the one who wrote sentences like it."

    nthought "I told Aeron the desk story tonight. I told him the desk was where my father worked. I did not tell him the desk was where my father worked on a project I was the subject of. I did not know."

    nthought "The strategic assessment I read at eleven was the assessment of my own cohort."

    nthought "The acceptable margins were projected against me."

    nthought "I read about myself at eleven and I did not know it was about me."

    "She closes the file. The file does not need to be re-read. The metadata header is enough. The metadata header is everything the rest of the document is going to say. The rest of the document is the operational detail of a study she has been the subject of since she was four years old, run by her parents, sponsored by Cognitive Architecture, used as the calibration baseline for the Neural Disposition Index she designed as an adult without understanding that the design was the extension of the study."

    nthought "I have been doing the work of the study from inside. I thought I was building the index. I was finishing the index my parents started. The eleven-year-old at the desk was not reading her father's project. The eleven-year-old at the desk was reading the case file that had her name on it, in a section of the document she did not navigate to because the section was three pages later than the page she opened."

    nthought "The acceptable-margins sentence was about a cohort. The cohort was four children. I was one of the four children."

    nthought "I do not know what happened to the other three."

    nthought "I will find out. Not tonight. The locator work has to finish. Tonight is the reading. The other three are tomorrow's reading."

    "She does not open *baseline* again. She lets the folder close itself. She moves the cursor back to the parent directory."

    # ========== PHASE 6 — REVELATION FOUR: THE AUTHOR FIELD ==========

    # CAMERA: the slowest push in the scene. The cursor
    #         hovers over a CAD log file from the *me*
    #         sub-folder — any file, all of them carry
    #         the same metadata header. The push tightens
    #         on the AUTHOR field. The field reads:
    #         *VANCE, N.* It has read this for nine years.
    #         The push is the camera doing the work
    #         Noelle's eye is doing — looking at a thing
    #         that has been visible all along.
    # LIGHTING: the screen brightens slightly as Noelle
    #           reduces the ambient. The amber lamps go
    #           down to half. The screen is the room.

    "She returns to the *me* sub-folder."

    "She opens the first file again. The behavioral-cluster analysis from 14 Anvil 386. The file she opened five minutes ago and read the dateline of without reading the rest of the metadata."

    "She reads the metadata block this time. All of it."

    "*FILENAME: bca_q3_386_d089.dat*"

    "*PROJECT: NDI INTERVENTION CASCADE — QUARTERLY REVIEW*"

    "*WORKING SESSION: 09:14 TO 18:42 ON 14 ANVIL 386 AC*"

    "*AUTHOR: VANCE, N.*"

    "*REVIEWING DIRECTOR: FABER, R.*"

    "She reads the AUTHOR field."

    "She reads it the way a person reads a sentence they have read every day for nine years and finally sees what the sentence says."

    "*VANCE, N.*"

    "Not Korr. Not the surname she was born with. Not the surname her personal calendar carries. Not the surname the rebellion knows her by. The surname on every CAD document she has ever produced is Vance. The surname has been on her credentials, her registry entry, her badge, her professional correspondence, her published papers, her review submissions, her project assignments, her access pads, her wrist display, her quarterly evaluations, her annual appraisals. The surname has been on her hand every time she has signed her name in a professional context for the last nine years."

    "She has known this. The knowledge has lived in her muscle memory. Her hand goes to *Vance* when she signs anything official. Her hand has gone to *Vance* on three Phoenix command documents already — the commitment authorization in 387, the secondary-base intake form, and the framework she signed in front of Aeron earlier tonight."

    "Aeron read the surname on the pad. The narration of his reading was: *NOELLE VANCE. Two words. She does not write a middle initial. She has never used a middle initial in his presence and he does not know if she has one.* He read the surname. He did not ask. She did not explain. Neither of them named the gap."

    "The gap is now named."

    nthought "Vance is Halen's name."

    nthought "Halen Vance. I took the name. I took it during the joining. CAD's bureaucratic register for partner-recognition. Researchers on classified projects could register joint professional identities for shared-credential access. The taking was administrative. I do not remember the taking."

    nthought "I do not remember the taking because the taking was edited along with the rest of the relationship."

    nthought "The editing took the relationship and left the surname. The surname is the residue. The surname has been on my hand for nine years. I have signed my dead partner's name on every official document I have ever produced. I have signed it on Phoenix command documents for the last seven months. I signed it tonight. Aeron read it. Aeron did not ask."

    nthought "I did not ask either. I did not ask because the question was sealed. The question is no longer sealed. I am asking."

    nthought "Why is my dead partner's name on my hand."

    nthought "Because the editing was selective. Because Faber's containment principle preserved the surname. Because untangling Vance from my professional identity would have required scrubbing nine years of paperwork across three sub-directorates, which would have been more visible than the residue. Because the trail of the editing must be smaller than the trail of the un-editing. Because the editing is the kind of work that does not clean up after itself, it leaves bodies and records and surnames lying around the room and trusts that the cleaning is more visible than the dirt."

    nthought "The dirt is my surname."

    nthought "I have been carrying the dirt as my own."

    "She does not close the file. She lets the AUTHOR field stay on the screen. She wants to see it for a few more seconds. She wants to know what the seeing is, now that she is doing it, instead of estimating what the seeing would be from inside the seal."

    "The seeing is small. The seeing is the size of two words. The seeing fits in the AUTHOR field of a behavioral-cluster analysis from 14 Anvil 386 and does not require any larger frame."

    "It is the smallness that breaks her composure. Not the size of the loss. The size of the room where the loss has been living. The size of the room is six characters: *VANCE.*"

    # ========== PHASE 7 — THE RETURN ==========

    # CAMERA: pull back slowly from the secondary screen.
    #         Wide on the workspace — the console, the
    #         crystal stand, Noelle in the chair, the
    #         drawer still open, the unfolded slip of
    #         paper still beside the empty crystal well.
    #         She has not put the crystal back. She does
    #         not put the crystal back during this phase.
    #         She returns to the primary console. She
    #         opens the framework draft. She types two
    #         lines. She deletes both. She types her name.
    #         She types it three times. She deletes two of
    #         the three. The phase ends on a single word
    #         on the screen.
    # LIGHTING: the secondary screen dims. The amber lamps
    #           come back up. The room returns to its
    #           start-of-scene light. The light looks
    #           different now — not because the light has
    #           changed, but because Noelle is looking at
    #           it from a different position. The position
    #           is the position of a person who has just
    #           seen what the room is made of.

    "She does not eject the crystal. She leaves it in the secondary reader. The folder *me* is still open. The AUTHOR field is still on the screen. The 14 Anvil 386 file is still loaded. She is going to look at the screen again later. She is going to look at it for a long time, in iterations, over the next weeks. She is going to read the nine hundred and fourteen files. She is going to read them in the order she has the budget for them. The reading will take months. The reading will take longer than months. The reading is the work she just inherited from the eleven-year-old at the desk."

    "She turns to the primary console. The framework draft is still open. The lattice still hovers. The placement document is queued for the oh-six-hundred briefing. Section II is unfinished. The cursor is blinking three lines into the third paragraph."

    "She does not return to the framework drafting."

    "She types one line beneath the cursor:"

    "*This isn't support, it's editing.*"

    "She reads it."

    "It is the same sentence she found in her own handwriting before defection. The slip of paper in the drawer carries the same six words. The slip of paper has been in the drawer for seven months. The same six words have been in her crystal for seven months. The same six words were on her own hand once, in pen, in a register that has not appeared on any other CAD document she has ever produced. The same six words are the only sentence she has ever written that did not come out in Faber's syntax."

    "She deletes the line."

    "She types her name."

    "*Noelle Vance.*"

    "She reads it."

    nthought "I have been signing this name."

    nthought "I have been signing this name on Phoenix documents for seven months. I have been carrying it as the technical-regular hand. The technical-regular hand was the hand my CAD muscle memory taught me when I was twenty-three. I learned the technical-regular hand inside the joining. I learned the technical-regular hand because Halen was teaching me the joining and the joining included the credential update and the credential update was the surname. I learned to sign with my partner's name. I have been signing with my partner's name for nine years. My partner has been dead for nine of those years. The signing has been a residue."

    nthought "I am not signing this name on the next Phoenix document."

    "She deletes the line."

    "She types her name again."

    "*Noelle Korr.*"

    "She reads it."

    nthought "Korr is the name I carry inside me. Korr is what my mother called me when she was being a mother instead of a project lead. Korr is the name on the green personal calendar with the ink-stained corner. Korr is the surname of the eleven-year-old at the desk, the surname of the four-year-old at the start of the longitudinal study, the surname I had before the joining and the surname I have used in every personal context since. Korr is mine in every way that the Phoenix paperwork has not been keeping track of."

    nthought "Korr is also the surname on the byline of my own foundational data, in the project-lead slot, twice. Korr is also my parents."

    nthought "Korr is mine and the people who made the cohort I was the subject of."

    nthought "I do not know how to sign Korr tonight either."

    "She deletes the line."

    "She types her name a third time."

    "*Noelle.*"

    "She does not type a surname."

    "She reads the single name. She lets the cursor blink beside it. She does not delete it. She holds the screen on the single name for a count of fourteen — a count she does not know is also the count Aeron held in `a4_s10a` after Selene delivered the Soren sentence, in a room two corridors away, ninety minutes earlier in the night. Two people in two rooms hold the same count without knowing each other is doing it."

    "At the count of fourteen, Noelle clears the field."

    "The line is gone. The framework draft is the only thing on the screen. The cursor blinks three lines into the third paragraph. The locator work resumes its position at the top of her queue."

    "She returns her hands to the keyboard."

    "She does not write Faber's syntax this time. She does not yet know what syntax she is going to write instead. The not-knowing is the work. The not-knowing is what the eleven-year-old at the desk was supposed to inherit from the strategist at the desk, instead of what the eleven-year-old actually inherited, which was the syntax. She is going to learn a different syntax in the hours she has before the cot. She is not going to learn it tonight. She is going to start learning it tonight."

    "She types."

    # ========== PHASE 8 — THE CLOSE ==========

    # CAMERA: hold wide on the workspace. The drawer is
    #         still open. The crystal is still in the
    #         secondary reader. The slip of paper is still
    #         unfolded beside the empty well. Noelle is at
    #         the primary console. The framework draft is
    #         on the screen. Her hands are on the keyboard.
    #         She is typing. The keystroke sound is
    #         different from the sound at the start of the
    #         scene — slightly slower, slightly less
    #         confident, slightly more present. The
    #         scene's final argument about what has just
    #         happened is the keystroke sound.
    # LIGHTING: the start-of-scene light, exactly. The
    #           three task lamps at full. The amber. The
    #           crystal stand in standby blue. The
    #           workspace looks the way it looked when the
    #           door closed behind Aeron. Nothing visible
    #           in the frame has changed. Everything in
    #           the room has changed.

    "The keystroke sound is the new sound. The new sound is slower than the register sound she walked Aeron out of the room with. The new sound has not been calibrated yet. The calibration is the work she has just begun."

    "She does not say a sentence to the empty workspace this time. The sentence-to-the-empty-workspace was the eleven-year-old's sentence, said in front of an audience of one — the eleven-year-old. The eleven-year-old does not need a sentence tonight. The eleven-year-old has been seen. The seeing is enough."

    "The locator work resumes."

    "Marcus's analyst cell is still in the upper Cygnet district. The radius is still six blocks. The fine-grain narrowing is still the work that is queued for tonight. She is going to do the work. She is going to do the work in a different syntax than the one she did the framework in, and the difference will not be visible to anyone who reads the locator brief in the morning, and the difference will be visible to her, and the visibility is the only audit she has access to tonight."

    "She is paying attention."

    "She does not say it aloud. The sentence is inside her now. The sentence does not need an audience. The sentence is the one thing the eleven-year-old gave her that has survived the longitudinal study and the joining and the editing and the residue and the seven-month seal. The sentence is hers. The sentence has always been hers. It was the first thing on the long list of things she is going to take back."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("defection_coda_complete", True)
    $ flag("halen_discovered", True)
    $ flag("ndi_baseline_realized", True)
    $ flag("vance_recognized_emp", True)
    $ flag("desk_recontextualized", True)
    $ canon_set("noelle.coda_complete_emp", True)
    $ canon_set("noelle.halen_known", True)
    $ canon_set("noelle.halen_known_dead", True)
    $ canon_set("noelle.ndi_baseline_known", True)
    $ canon_set("noelle.parents_in_baseline_byline_known", True)
    $ canon_set("noelle.eleven_year_old_desk_recontextualized", True)
    $ canon_set("noelle.vance_origin_known_emp", True)
    $ canon_set("noelle.surname_signing_default_emp", "Korr")
    $ canon_set("noelle.surname_signing_default_was", "Vance")
    $ canon_set("noelle.faber_voice_recognized", True)
    $ canon_set("noelle.crystal_opened", True)
    $ canon_set("noelle.crystal_seal_duration_months", 7)
    $ npc_remember("Noelle", "opened_crystal_after_seven_months", tone="postponement_ended")
    $ npc_remember("Noelle", "halen_transfer_fiction_collapsed", tone="grief_seen_first_time")
    $ npc_remember("Noelle", "found_parents_in_own_baseline_byline", tone="origin_recontextualized")
    $ npc_remember("Noelle", "saw_vance_on_author_field_for_first_time", tone="surname_as_residue")
    $ npc_remember("Noelle", "typed_three_signatures_kept_only_first_name", tone="name_back_as_question")
    $ npc_remember("Noelle", "held_count_of_fourteen_on_first_name_alone", tone="rhyme_with_aeron_unknowingly")
    $ tp_seed("a4.noelle.crystal_opened")
    $ tp_seed("a4.noelle.vance_question")
    $ tp_seed("a4.noelle.three_other_children_in_cohort_c04")
    $ tp_seed("a4.noelle.faber_syntax_recognized")
    $ metric("noelle_compartments_unsealed", change=1)
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s09a_noelle_coda_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II) — CODA
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same night as a4_s09. Approximately ninety minutes after the door
#     closes behind Aeron. Noelle is alone in the workspace, working the
#     locator on Marcus's analyst cell as she said she would. The Faber
#     cadence catches her in the first paragraph. The scene runs through
#     the rest of the three-hour window she had budgeted for locator work.
#     By scene close she is back at the locator with a different syntax.
# cann.what_happened:
#   - Noelle catches her own writing in Faber's syntax and recognizes the
#     pattern for the first time. Stops. Opens the lower-left CAD-issue
#     drawer she has not opened since the secondary base was established
#     seven months ago. Removes the personal data crystal she compiled
#     in the seventy-two hours before defection.
#   - Loads the crystal. Navigates to four folders in sequence:
#     1. *me* — sub-folder of her own CAD logs authored by KORR, N. across
#        nine hundred and fourteen files. Three hundred dated to days her
#        personal calendar marks empty. Confirmation that her own
#        experience was edited along with everyone else's.
#     2. *Halen* — runs the dispatch-manifest cross-reference she has
#        had in the folder for seven months and never executed. The
#        Outer Wards Resonance assignment log shows Halen reassigned 03
#        Ember 381 indefinite term. The dispatch manifests show no
#        Halen ever arrived. The transfer was a fiction. Halen died on
#        the day the records say they were reassigned.
#     3. *baseline* — opens her own NDI baseline file. Metadata header
#        names her as LONGITUDINAL SUBJECT KORR, N. of COHORT C-04
#        (PILOT). Project leads in byline: KORR, A. and KORR, T. — her
#        parents Anesh and Talen. She was four when the study began.
#        She was eleven when she read the desk. The desk's "acceptable
#        margins" sentence was about her cohort. The eleven-year-old
#        was reading her own data without knowing it.
#     4. *me* (returned to) — reads the AUTHOR field on a 14 Anvil 386
#        behavioral-cluster analysis. The field reads VANCE, N. She has
#        seen this byline thousands of times. She lets the question
#        form for the first time. She remembers, structurally, that
#        Vance was Halen's surname. She has been signing her dead
#        partner's name on every official document for nine years. She
#        signed it in front of Aeron earlier tonight.
#   - Whistleblower nthought folds into Phase 4. The fragment *V—n /
#     Vehn.* The unnamed SAD analyst who routed encrypted manifest
#     fragments to her evidence package over weeks. Deleted before
#     she could thank them.
#   - Returns to the primary console. Types and deletes "this isn't
#     support, it's editing." Types her name three times: NOELLE VANCE
#     (deleted), NOELLE KORR (deleted), NOELLE (held for a count of
#     fourteen, then cleared). The fourteen count is a structural
#     rhyme with Aeron's count of fourteen in a4_s10a — neither
#     character knows the other is doing the same count, ninety
#     minutes apart, two corridors apart.
#   - Returns to the locator work. Types in a syntax that is not
#     Faber's. The new syntax is not yet calibrated. The not-knowing
#     is the work. Scene closes on the keystroke sound — slower,
#     less confident, more present than the start-of-scene sound.
# cann.noelle_state:
#   - Coda complete. Four revelations landed. The defection-data seal
#     that has held for seven months is broken.
#   - Vance recognized as residue. The signature default for future
#     Phoenix documents is now Korr — the recovery is visible in the
#     audit trail. EMP-only. OB Noelle keeps Vance.
#   - The eleven-year-old's sentence — "I am paying attention" — is
#     now retroactively known to have been said by an eleven-year-old
#     reading her own cohort data. The sentence remains hers. The
#     sentence is one of the first things on the list of things she
#     is going to take back.
#   - Three other children in Cohort C-04 (PILOT) are now a live
#     plot plant. She does not know what happened to them. She has
#     scheduled the question for tomorrow's reading. tp_seed
#     a4.noelle.three_other_children_in_cohort_c04 flags this.
#   - Faber's syntax is now consciously visible to her. Her writing
#     will diverge from it across the rest of Act IV. The divergence
#     is gradual; the recognition is the inflection point.
# cann.aeron_state:
#   - Not in scene. Aeron is asleep or walking the second-shift base
#     somewhere else. He has not yet been told about Halen, the
#     baseline, or the surname. The compartment Selene named in
#     a4_s10a applies here in mirror form: Noelle now carries a
#     compartment of her own. The opening of the compartment to Aeron
#     is the work of subsequent scenes, principally the Protocol
#     Verdant Payoff (a4_s17) and the Tessa anchor (where Halen lands
#     during awake surgery).
# cann.path_tracking:
#   - EMP path only. Linear. No branching, no player choice. Coda to
#     a4_s09. The OB equivalent (a4_s10a_noelle_coda_ob) plays a
#     structurally similar four-revelation sequence with diverging
#     ending: Vance kept on the OB doctrine signature voluntarily.
# cann.thematic_flags:
#   - The seal as second editing: Noelle named the postponement as the
#     editing she performed on herself. The first editing was Faber's.
#     The second editing was hers. The unsealing is the start of the
#     undoing of both.
#   - The four-revelation rhythm: own name -> Halen -> baseline ->
#     surname. Each revelation makes the next legible. The surname is
#     the smallest revelation in physical size — six characters,
#     VANCE — and the largest in retrospective load. The smallness is
#     the breaking-point.
#   - The count of fourteen rhyme with a4_s10a. Aeron and Noelle hold
#     the same count, ninety minutes apart, in different rooms, neither
#     knowing the other is doing it. The shared count is an
#     unannounced structural argument — that what shared authority
#     produces is the same shape of stillness in two bodies, even when
#     the two bodies do not know each other are still.
#   - "I am paying attention" recontextualized. The sentence was first
#     said by the eleven-year-old at the desk. It was said again at
#     the close of a4_s09. It is said neither aloud nor in nthought
#     here at the close of a4_s09a — it is said in the keystroke
#     sound. The sentence is now load-bearing across three temporal
#     layers (eleven, post-signing, post-coda) and one mechanical
#     layer (the new syntax of the locator work).
#   - The Korr/Vance question. EMP Noelle has the surname back as a
#     question. She does not yet have an answer. The answer is the
#     work of subsequent scenes. The first re-signing as Korr will
#     happen on the next Phoenix command document.
#   - Faber's containment principle — quoted in the surname revelation
#     — is now canonized in scene: "the trail of the editing must be
#     smaller than the trail of the un-editing." This is the rule
#     governing why Vance was preserved on the records.
# cann.character_moments:
#   - Noelle: holds her thumb on the biometric pad for the full half-
#     second hold window without withdrawing. The not-withdrawing is
#     the scene's first deliberate choice.
#   - Noelle: closes her eyes for one second after the Halen revelation
#     and does not close them for longer. The crying budget is not
#     available. The crying budget will arrive in a different scene.
#   - Noelle: types her name three times. The third time, no surname.
#     Holds the count of fourteen on the single name. Clears.
#   - Noelle: returns to the locator in a syntax that is not Faber's.
#     The new syntax is not yet calibrated. The keystroke sound is the
#     scene's final argument about what has just happened.
#   - Noelle: does not say "I am paying attention" aloud. The sentence
#     is internal now. The sentence is one of the things she is taking
#     back.
# cann.callbacks:
#   - a4_s09_noelle_implicated_emp: direct parent. The coda picks up
#     exactly where s09 closed, in the same workspace, with the same
#     lattice still in standby. The Faber-cadence recognition in
#     Phase 1 is the trigger for the rest of the scene.
#   - a3_int_02_noelle_unmeasurable_emp: the category error Noelle
#     committed alone. The seal of the defection data was the second
#     instance of the same error — sealing herself off from the data
#     as a way of preserving the analyst category. The unsealing is
#     the post-broadcast recovery of unmeasurable territory inside
#     her own life, not just in the rebellion's.
#   - a4_s10a_liora_sent_word_emp: structural twin. Both scenes are
#     codas riding a4_s09 / a4_s10. Both involve a single character
#     receiving a sentence in solitude that recontextualizes nine
#     years of evidence. Both close on a held silence that includes
#     a count of fourteen — Aeron's after Selene's last sentence,
#     Noelle's on a single first name. The two scenes do not know
#     they are mirroring each other; the audience does.
#   - canon_notes_noelle.md sec 2.1 (The Vance Surname): the surname
#     mechanic is locked here in scene. Future Phoenix command
#     documents from Noelle in EMP will sign as Korr; the recovery
#     is visible in the audit trail.
#   - canon_notes_noelle.md sec 5 (The First NDI Subject): the
#     baseline revelation lands here. Cohort C-04 (PILOT) is now a
#     live plot plant. Three other children. Three other names
#     somewhere in the city. Possibly findable.
#   - canon_notes_noelle.md sec 7 (Director Faber): the syntax
#     recognition in Phase 1 is the first time Faber's voice has
#     been visible to Noelle as a separate entity inside her own
#     register. The Faber compartment opens here. Faber's countersign
#     protocol governs the Liora file (still to land in a4_s17) and
#     the operational order on Halen (already landed in this scene).
# cann.block_status:
#   - MINOR SCENE, LOAD-BEARING. Linear. EMP path only. Coda to
#     a4_s09. Foundational for: a4_s17 (Protocol Verdant Payoff),
#     the Tessa anchor (Halen conversation during implant surgery),
#     and any subsequent scene where Noelle signs a Phoenix command
#     document.
# cann.requires_followup:
#   - The Cohort C-04 other-three-children plant. tp_seed
#     a4.noelle.three_other_children_in_cohort_c04. If pursued, this
#     becomes Act V or late-Act IV territory. Open canon-side.
#   - The next Phoenix command document Noelle signs should resolve
#     as KORR, not VANCE. The audit trail change is the first visible
#     post-coda artifact. Aeron noticing it is open territory and
#     would land. Author at discretion.
#   - The Halen conversation is now sealed in Noelle alone until the
#     Tessa anchor (where Tessa is awake-surgery removing the implant
#     and Noelle tells her about Halen during the procedure as a
#     coping mechanism). Halen does not appear in any other scene
#     before that anchor. Noelle does not tell Aeron about Halen until
#     a4_s17 at the earliest, and even there only if the player has
#     unlocked the relevant beat.
#   - The new syntax Noelle is learning is the post-Faber register.
#     This is gradual. Subsequent Noelle scenes should show the
#     gradual divergence — sentences less reliant on Faber's
#     scope-narrowing rhetorical move at the second sentence,
#     conjunction patterns more varied, less institutional symmetry.
#     The drift is small per scene. The total drift over the rest of
#     Act IV is significant.
#   - The slip of paper in the drawer ("This isn't support, it's
#     editing") is now visible to the audience for the first time.
#     The slip remains in the drawer at scene close. Future scenes
#     where Noelle returns to the drawer are open territory.
# =========================================================
