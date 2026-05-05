# =======================================================
# ACT 4 - Scene 20b: The Placement (Empathy Path)
# File: a4_s20b_verdant_decrypt_emp.rpy
# Type: NOELLE THESIS BEAT — Protocol Verdant decrypt delivered
# Matrix: Aeron x Lyra x Noelle. The Verdant payoff.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s20b_verdant_decrypt_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s20b_verdant_decrypt_emp:
    $ show_timeline("3rd of Glass, 390 A.C.", "23:10", "Phoenix Secondary Base — Noelle's Workspace")

    # Codex stage bumps
    $ codex_reveal("noelle_korr", to_stage=4, source="a4_s20b_verdant_decrypt_emp")
    $ codex_reveal("aeron_rylan", to_stage=4, source="a4_s20b_verdant_decrypt_emp")
    $ codex_reveal("lyra_althea", to_stage=4, source="a4_s20b_verdant_decrypt_emp")
    $ codex_reveal("liora_rylan", to_stage=4, source="a4_s20b_verdant_decrypt_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. The same workspace discipline as a4_s09 and a4_s09a —
    #         Noelle's room shot steady. The frame is her authority and the
    #         authority is what she is going to dismantle for two other
    #         people across the next ninety minutes. The camera holds three-
    #         shot for the opening — Noelle at the console, Aeron and Lyra
    #         standing the way the alcove scenes have taught Aeron to stand
    #         when he is receiving. The crystal stand is not active in this
    #         scene. The decrypt lives on the primary screen and the two
    #         secondary screens flanking it. The screens are the document.
    #         Coverage shifts across the three movements: tight on Noelle
    #         for the first movement (Aeron's preservation), pulls to a
    #         two-shot for the second (Lyra's placement), holds wide for
    #         the third (the Liora file). The Korr/kore etymology is shot
    #         in single on Lyra — the only single-on-Lyra in the scene.
    #         The single is short. The line is short. The single is how
    #         the camera honors the gift.
    # LIGHTING: Workspace late. Three task lamps at full at scene open,
    #           dimmed by half by mid-scene. The primary screen carries
    #           the Verdant cohort metadata in pale blue. The secondary
    #           screens carry the placement records and the Liora file
    #           respectively. The amber lamp from the s09a coda night —
    #           never turned on, never moved — sits on the secondary
    #           workstation. The unplug is a constant.
    # SFX: Workspace ambient, second-shift quiet. The keyboard is not
    #      active in this scene at any point. Noelle has finished the
    #      decrypt before the scene begins. There is no register sound.
    #      The scene is voices and stillness and the small mechanical
    #      sounds of the screens cycling between cohort indices.
    #      One-shots: door open (Aeron and Lyra arriving together, the
    #      arrival the scene's first composition choice), the secondary
    #      reader chime as Noelle slots the Liora file at movement 3,
    #      the small page-turn sound of Lyra's prayer beads in her
    #      pocket — audible only in the silence after the placement
    #      line. No music bed. The scene refuses one. Two of the three
    #      revelations land in absolute silence.
    # FACE: Noelle — post-coda Noelle. The working register has been
    #       diverging from Faber's syntax for a week. Her face shows
    #       the divergence: less institutional symmetry, more pause,
    #       fewer unbroken sentences. The face is calmer than it was
    #       in s09. The calm is not composure. The calm is the kind
    #       of calm that arrives after a person stops fighting a
    #       category they were inside of.
    #       Aeron — receptive, post-Liora-letter, post-s10a-Soren-
    #       sentence. He has been carrying a compartment for a month
    #       now. He knows what it feels like to receive a sentence
    #       that recontextualizes his life. He recognizes the shape of
    #       the room when he walks into it.
    #       Lyra — does not yet know what the scene is. She came
    #       because Noelle asked. She trusts Noelle. The trust is
    #       what the scene is going to test by the end of movement 2.
    # BLOCKING: Noelle at the workstation chair. Aeron and Lyra stand —
    #           Aeron at the same three-step distance from the console
    #           he has held in every Noelle scene since s09. Lyra at
    #           his left shoulder, one quarter-step closer to the
    #           console than he is. The proximity differential is
    #           Lyra's choosing. She does not know she is choosing it.
    #           She will know by the end of movement 2.

    # ========= VOICE BASELINE =========
    # Noelle: post-coda voice. Plainer than s09. Shorter sentences. The
    #          register exists but does not lead. She uses the names of
    #          the things she is naming, not their categories.
    # Aeron: receptive register. The voice he has used since the s10
    #         shared-command annex scene. Few lines. The lines that
    #         arrive are not questions to her — they are questions to
    #         himself, said aloud because Lyra is in the room and Lyra
    #         needs to hear him asking.
    # Lyra: composed at scene open. Two key spoken moments — the
    #        placement line at the end of movement 2, the etymology line
    #        late in the scene. Between those, she is silent. Her silence
    #        is not absence; it is processing. The scene honors the
    #        processing by not interrupting.

    # scene bg_noelle_workspace_late with dissolve
    # play ambient "sfx/ambient/workspace_hum.ogg" fadein 2.0

    # ========== PHASE 1 — THE SUMMONS ==========

    # CAMERA: 50mm locked. Open on the workspace from
    #         the door angle, empty. Then the door opens
    #         and Aeron and Lyra enter together. Two
    #         figures in the frame at scene start, then
    #         three. The third figure (Noelle) was
    #         already there — the camera reveals her
    #         existence as Aeron and Lyra clear the
    #         doorway and the angle widens.

    "Noelle's message reaches Aeron and Lyra at twenty-two-fifty on the same shared notification chain — for the first time in their respective tenures with the rebellion, the message routes to both of them in the same packet, with the same subject line."

    "*Workspace. Twenty-three-ten. Both of you. The decrypt is finished.*"

    "Aeron reads the message in the war room corridor. Lyra reads the message in the medbay observation alcove where she has been standing watch for Tessa, who is in surgery on a runner from the Sector 14 cache extract. They read the message at approximately the same minute. Neither of them sends a reply. Lyra leaves the alcove and crosses to the corridor and finds Aeron already walking toward the workspace. They walk the rest of it together. They do not talk about the message. They do not talk about anything."

    "At the workspace door, Aeron does not knock. The no-knock understanding extends to Lyra now, by transitivity. Aeron opens the door. Lyra steps in first."

    "The workspace is in its now-familiar configuration. Three task lamps. The console along the back wall. The crystal stand in the center, dark. Noelle at the console. The primary screen and both secondaries are active — three different documents, three different cohort indices, the pale blue wash of the Verdant database header repeating across all three."

    "Noelle does not turn when they enter. She finishes a line of metadata annotation. The Noelle rule. The post-coda Noelle rule is the same rule. The annotation is in her own hand and is shorter than her CAD-era annotations would have been. The hand resolves on the screen as: *KORR — c/r reviewed.* Two characters. The technical-regular hand is gone. The replacement hand has not been named yet. It is shorter."

    "She finishes the line. She turns."

    n "Thank you for coming together."

    "She does not stand. She is still in the workspace chair from a4_s09 and a4_s09a — the same chair she has been doing the divergence work in for a week. The chair is where she does the work that the previous chair could not do."

    n "I asked for both of you because the document I am about to show you is a document with three subjects. The third subject is Liora. She is not in the room. She cannot be. The document has the other two subjects in the room, and the document is large enough that I am not going to brief Selene tonight. I am going to brief Selene at oh-eight-hundred tomorrow, the way I did with the framework. The reason I am not briefing her tonight is that the document is not an operational document. The document is a personal document with operational consequences. The personal layer goes to the personal addressees first. Operational comes second."

    n "I learned that order from a4_s10a. From the Selene-Liora coda. I am following the precedent."

    "Aeron stops three steps into the room — his now-canonical position, the geometry of receiving he has been holding since s09. Lyra stops at his left shoulder, one quarter-step closer to the console. The differential is a quarter-step. Noelle's eye registers the differential without naming it. The differential is going to matter at movement 2."

    a "Noelle. Begin when you're ready."

    "He has used this opening line in three Phoenix scenes in the last month. The line is now his ritual. The ritual is the marker that he understands a sentence is about to be delivered that he is going to have to receive without solving."

    "Noelle nods once."

    n "I am ready."

    # ========== PHASE 2 — MOVEMENT ONE: WHAT AERON WAS PRESERVED FOR ==========

    # CAMERA: tight on Noelle. The screens are out of
    #         frame for the bulk of this movement — the
    #         camera is on her face delivering the
    #         sentence. Cuts to Aeron only twice during
    #         the movement: once when she names the
    #         "fate" lie, once at the close of the
    #         movement when she pauses for him to speak
    #         and he does not.
    # LIGHTING: the primary screen brightens slightly
    #           behind Noelle as she activates the
    #           Aeron-cohort layer of the decrypt. The
    #           pale blue wash deepens.

    n "The document is the decrypt of a CAD program internally designated PROTOCOL VERDANT. The decrypt has been running on my locator hardware since the broadcast. It finished an hour ago. I have read it twice in that hour. The reading is the reason the brief is happening tonight rather than tomorrow."

    n "Protocol Verdant is the regime's bloodline-preservation program. Active for at least thirty years, possibly longer. Its mandate is the identification, monitoring, and preservation of viable Verdant and Ethereal lineages for future Core research applications."

    n "The mandate's operational shape is: identify a candidate by lineage purity, monitor the candidate across the candidate's developmental window, preserve the candidate from disposition pressures that would degrade lineage viability, and prepare the candidate for resonance-compatibility experiments scheduled for the candidate's late twenties."

    n "The first subject of this document is you, Aeron."

    "She does not pause for him. The pause would be the place she would have paused before the coda. The post-coda voice is the voice that does not pause for the response it has not solicited."

    n "The decrypt names you as the last viable pure Verdant candidate identified in the city. The candidacy was confirmed at age twelve, on the day your Branding rejected. Inside Protocol Verdant, the Branding rejection was not classified as a failure. It was classified as evidence of lineage purity. The rejection was the pass mark."

    "She holds her eyes on him for one second. The second is the place she would have paused before the coda. She does not pause now."

    n "Marcus authored the public cover story. The cover story was 'fate.' The cover story was distributed to the Council, to the Aeries social register, to the academy where you trained, to the household. The cover story was that the Branding's failure was a sign of destiny. The cover story was that you were special. The cover story was a lie about a deeper truth."

    n "The deeper truth is that you were preserved as breeding stock. The preservation kept you in a high-visibility command position because the high-visibility position protected you from the disposition pressures that would have degraded lineage viability. Marcus has been protecting your lineage purity since you were twelve. He has been doing it through the public cover of grooming you for command. The grooming was instrumental to the preservation. The preservation was the operational goal."

    n "The resonance-compatibility experiments were scheduled for your late twenties. The decrypt names a window of 388 to 391 AC. We are inside the window. The experiments have not happened. Marcus delayed them when you began drifting from Echelon allegiance. The delay was operational, not ideological. He was waiting for you to stabilize."

    "She stops."

    "She is looking at him. He has not moved. His face is the face he has been carrying since the alcove with Selene a month ago — the face that knows how to receive a sentence that recontextualizes his life. The face has had practice."

    a "Marcus's lie was bigger than I knew."

    "He says it the way he said *okay* in the alcove with Selene. The same register. The voice of a man receiving a sentence that does not have a verbal response large enough."

    "Lyra has not spoken. She is standing at his left shoulder, the quarter-step closer to the console that she chose without choosing. Her right hand has gone into her pocket. The fingers are on her prayer beads. The page-turn sound of the beads is audible in the silence between Aeron's sentence and Noelle's next."

    n "The 'fate' framing was not just protective. It was instrumental. Marcus needed you to believe in the destiny narrative because the destiny narrative was the operational frame that kept you cooperating with the preservation. If you had known you were a breeding subject, you would have refused. Marcus knew you would refuse. The lie was designed against your own moral architecture."

    n "I am giving you the document at the end of the brief. You can read the operational notes yourself. The operational notes are detailed. They include the names of the CAD officers responsible for monitoring you across each of your developmental windows. Faber is one of the names. Faber is on three of the seven monitoring tiers."

    "She watches Aeron for a count of three."

    "He does not say anything else."

    "She moves to movement two."

    # ========== PHASE 3 — MOVEMENT TWO: WHAT LYRA WAS PLACED AS ==========

    # CAMERA: pulls from tight on Noelle to a two-shot
    #         that includes Lyra in the frame for the
    #         first time. The pull is slow. The two-
    #         shot is the composition that is going to
    #         hold for the rest of movement 2 and most
    #         of movement 3. Aeron remains off-camera
    #         for this stretch — his presence in the
    #         scene is auditory, not visual. The
    #         framing is deliberate. Lyra is being told
    #         a thing that is hers to receive and the
    #         camera holds her in the frame because the
    #         camera knows the receiving belongs to her.

    n "The second subject of the document is you, Lyra."

    "Lyra does not move. Her hand stays in her pocket. The page-turn sound stops. The beads have settled."

    n "I want to be careful with how I say this, because the document is going to land harder for you than the first movement landed for Aeron. Aeron has been receiving these sentences for a month. You have not had the practice. I am telling you the practice exists and that you are going to have it after tonight, but I am not telling you the practice in advance because the practice is the kind of thing you have to do in order to know what it is. I am telling you the substance now and the practice is the work of the next weeks."

    "Lyra nods once. The nod is the only motion her body has made in the movement so far."

    n "Protocol Verdant is a paired program. The Verdant lineage and the Ethereal lineage are tracked together because the resonance-compatibility experiments require both. For every Verdant candidate the program identifies, the program identifies a matched Ethereal candidate of compatible age, compatible developmental profile, and compatible proximity to the Verdant subject."

    n "The matched Ethereal candidate to Aeron's Verdant designation is you."

    n "Your prodigy status was a Protocol Verdant placement work. Your academic placement at the Cathedral was Protocol Verdant placement work. Your assignment to the Cathedral wing that overlapped with Marcus's command schedule was Protocol Verdant placement work. Your proximity to the Rylan family across your adolescence was Protocol Verdant placement work. The Cathedral assignment that placed you in the same diplomatic delegation as Aeron's mother in 374 AC was Protocol Verdant placement work."

    n "Each placement was authored by CAD three layers up from the Cathedral's own administration. The Cathedral believes it placed you. CAD placed you. The Cathedral is one of the operational covers."

    "She stops."

    "She watches Lyra. Lyra's face has not changed. The face is a face Noelle has seen before — on a4_s09 a, on her own face, in the workspace mirror she does not have, when she was reading the AUTHOR field on her own logs. The face is the face of a person doing the math she has been refusing to do for a long time and doing it in twenty seconds because the document is doing the doing for her."

    n "The placement was not romantic engineering. The decrypt is explicit. CAD did not arrange for you to fall in love with him. CAD arranged for you to be available, proximate, and developmentally compatible with him at the developmental window in which the resonance-compatibility experiments would be scheduled. What you have built with him in the years since the placement is yours. The placement does not author the content of the relationship. The placement authored the geometry that allowed the relationship to exist at all."

    n "I am telling you this because I do not want you to file the placement under the wrong category. The placement is the floor under your relationship with Aeron. The placement is not the relationship."

    "Lyra speaks for the first time in the scene."

    "Her voice is the voice she uses for liturgical readings — the trained, low, even voice that the Cathedral taught her to use for sentences too important to allow ornamentation. The voice is the placement-shaped voice. She does not yet know it is the placement-shaped voice. She will know by the end of the sentence."

    l "Then it is also true that whatever this is — between any of us — was authored after the placement was complete. The placement is the floor. The floor is not the room."

    "A pause."

    "The pause is the scene's longest. Aeron does not break it. Noelle does not break it. The pause holds for a count of nine — a count Noelle has been keeping since the coda, a count Lyra does not know is being kept. At the count of nine, Lyra continues."

    l "I am going to repeat the line so I can hear it twice. Once as a sentence I have just thought, once as a sentence I am keeping."

    l "The placement is the floor. The floor is not the room."

    "She nods once. The nod is for herself."

    lthought "I have been walking on the floor for nineteen years. I did not know it was a floor. I called it the room. I called it my whole life. The room is what I have been building on top of the floor. The floor is what allowed me to start building. The floor is the regime. The room is mine. The room is mine because I have been the one in it, choosing what to carry and what to set down, and the regime did not author the carrying."

    lthought "The regime made the floor. The regime did not make me."

    lthought "I am going to keep that distinction. I am going to keep it tonight. I am going to keep it tomorrow. I am going to need to keep it for a long time."

    "She does not say any of the lthought aloud. The aloud version is the one sentence: *the placement is the floor.*"

    "She turns her head a quarter-inch toward Aeron. Not a full turn. A quarter-inch. The quarter-inch is the same quarter-step that put her closer to the console at the start of the scene. She does not look at him. She looks past his shoulder. The look past is the way she has always looked when she is choosing to see him without performing the seeing."

    l "Aeron."

    a "I'm here."

    l "I am still here too."

    "She does not elaborate."

    "She does not need to."

    "Aeron's eyes close for half a second. He opens them."

    a "Okay."

    "It is the same okay he said in the alcove with Selene. The third okay register. The okay of a man accepting a rule he did not write."

    # ========== PHASE 4 — THE LIORA FILE ==========

    # CAMERA: holds the two-shot of Noelle and Lyra.
    #         Aeron remains audio-only. Noelle reaches
    #         to the secondary reader and slots a small
    #         crystal — different from the personal data
    #         crystal she opened in s09a, this one
    #         smaller, older, edged in the brass-tone
    #         the older CAD crystals had before the
    #         standardization of 380. The crystal slots.
    #         The reader chimes.

    n "The third subject of the document is Liora Rylan. Aeron's mother."

    "She slots the older crystal into the secondary reader. The reader chimes. The Liora file resolves on the right-hand secondary screen — a single personnel record, edged in the older brass UI of pre-380 CAD documents, the format that has not been used in the agency for a decade."

    n "I have had this file for seven months and one week. I pulled it during my pre-defection self-audit. I did not know whose file it was. The file was in a batch of redacted civilian files I pulled at random for variance analysis. I read the data. I recognized something in the pattern I could not articulate. I buried the file in my offline cache. I did not flag it. I did not report it. I did not know why I was protecting it."

    n "I learned whose file it was three weeks ago, when the Verdant decrypt began surfacing the cohort metadata. Liora's name appeared in the Verdant cohort tag — not as a subject, but as a cataloged escape. The only Verdant-adjacent person on file who left the city undetected and was never re-actioned."

    n "The reason she was never re-actioned is in the file. Faber's countersign protocol. A standing protocol that requires Faber's explicit countersignature on any disposition order for a Verdant-adjacent person on the watch list. Faber has not countersigned a single disposition order against Liora in nineteen years. The Liora file has been flagged for action seventeen separate times across that interval. Each time, the action paperwork has reached Faber's desk and stopped."

    "She turns her head to look at Aeron. The first time in movement 3 she has done so."

    n "Liora is alive, Aeron. She has been alive the entire time. Faber has been the reason she has not been brought back. I do not know why Faber chose to protect her. The decrypt does not give a motive. The decrypt only gives the pattern. The pattern is unambiguous."

    n "The file in front of you on the secondary screen is hers. The file includes her last known location as of three years ago — an Outlands settlement the Free Strata cataloged as a story-keeper community. The file is yours."

    "Aeron's voice comes from off-camera. The two-shot has held for the full movement. The camera has not cut to him."

    a "Selene already told me Liora is alive."

    "He says it plainly."

    a "She delivered Liora's final packet to me at the alcove a month ago. The packet went through Selene because Liora keyed it to a pre-Phoenix relay route Selene had not used in nine years. Selene has known Liora was alive for nine years. I have known for one month."

    a "You have known for three weeks."

    a "Three of the rebellion's strategic minds have been holding pieces of my mother without telling me. Selene knew via the relay. Noelle knew via the file. Liora knew that both of you knew, because Liora keyed the relay and Liora authored the cover that kept the file from being actioned. The not-telling has been the protocol. The not-telling has been the only thing keeping her alive."

    a "I am not asking you to apologize for the not-telling. I am noting that the not-telling has now been brought into the room. The bringing-in is the change. The not-telling is over."

    "Noelle does not respond to him directly. She speaks to the screen."

    n "I held the file for seven months without knowing whose it was. The holding was instinctive. I did not have a framework for the instinct at the time. The framework arrived in the coda night last week, in a different room, with a different crystal. The instinct is now legible. The instinct was: this person is worth protecting, even at the operational cost of carrying a file I cannot file."

    n "I have been doing the unmeasurable work for longer than I have had a name for it."

    n "Lyra taught me the name."

    "She turns to Lyra."

    n "I am giving you the file too, Lyra. The file is not yours to act on — it is Aeron's. But the file's existence is yours to know about, because the file's protection across nineteen years was authored by a CAD director who is the same director who authored the placement that put you next to Aeron. Faber's name is on both your cover and her cover. The same hand. The same protocol. The same intent — to keep someone Verdant-adjacent in a viable position."

    n "I do not know what to do with that. I am giving you the data."

    "Lyra nods once."

    l "I will hold it."

    l "I will hold it the way I have held the other things you have given me tonight. The placement and the floor and the file are three forms of the same revelation. They are mine to receive. I will receive them at the rate I can receive them. I am not going to receive them all tonight."

    l "I will tell you when I am ready to discuss any of them. The telling will not be an apology. The telling will be the thing that comes after the receiving. I am noting the order so you do not mistake the silence for absence."

    n "Acknowledged."

    "Noelle catches the word. The word is the OB version of the word she would have used a month ago. The post-coda word is shorter. She lets the catch happen and does not correct it. The not-correcting is also the work."

    # ========== PHASE 5 — THE ETYMOLOGY ==========

    # CAMERA: single on Lyra. The only single-on-Lyra in
    #         the scene. Short. The line is short.
    #         Aeron and Noelle remain in the room — the
    #         camera knows they are present without
    #         showing them. The single is how the
    #         camera honors the gift. Aeron is audible:
    #         a small intake of breath at the line's
    #         landing. Noelle is silent. The single
    #         lasts twelve seconds. The line itself is
    #         eight.

    "Lyra has been holding her hand in her pocket for the entire scene. She removes it now. The prayer beads are in her hand. She is not praying. She is holding the beads the way one holds a tool one is about to use for a non-tool purpose."

    "She turns to Noelle."

    "Her voice is the etymology voice — the Cathedral-trained voice she uses when she is naming a word in its older form. The voice is plain. The voice is gentle. The voice does not labor."

    l "Noelle. May I."

    n "Yes."

    l "Korr is the name the Cathedral kept for the daughter taken underground. Persephone in the older tongue. She came back. She was changed. The bringing-back is what the season is named for."

    "A pause."

    "Noelle does not respond verbally. She nods once. Aeron watches her nod. He does not say anything. The watching is the work he is doing. The nod is the work she is doing. The line is the work Lyra has done."

    "The single holds for two more seconds. Then the camera releases the single."

    # ========== PHASE 6 — THE CLOSE ==========

    # CAMERA: pulls back to a wide on the workspace.
    #         The three figures in the frame. Noelle in
    #         the chair. Aeron three steps in. Lyra at
    #         his left shoulder, the quarter-step
    #         closer. The composition is the same as
    #         scene start. The room is the same room.
    #         Nothing visible in the frame has changed.
    #         The audience knows the room is different.
    # LIGHTING: the task lamps come back to their start-
    #           of-scene level. The screens dim by half.
    #           The pale blue wash recedes. The amber
    #           lamp on the secondary workstation
    #           remains unplugged. The unplug is the
    #           constant the scene has held since the
    #           coda night.

    "Noelle ejects the Liora file from the secondary reader. She holds the small brass-edged crystal in her right hand. She extends it across the workspace toward Aeron. He walks the three steps to the console — the first time he has crossed the distance in this scene — and takes the crystal from her hand. His thumb passes over hers in the handoff. The contact is brief. The contact is intentional. He says nothing about it."

    a "I am going to read this in my quarters. Tonight. Alone."

    n "That is the right way to read it."

    a "I am going to come back here at oh-six-hundred to brief you on what I want to do with it. I am not going to make the decision before I read the file. I am not going to make the decision tonight."

    n "Acknowledged. I will be here."

    a "Lyra."

    l "I'm here."

    a "I do not have a sentence yet for what just happened in this room. I am going to sit with the not-having. I am going to come find you when I have the sentence."

    l "I will be in the medbay. Tessa's runner is going to be in surgery for another two hours. After surgery I will be in the chapel. After chapel I will be in my quarters. The location does not matter. I am holding the room you are walking out of right now until you walk back into it."

    a "Okay."

    "He turns to Noelle. His left hand lifts halfway and stops. The same halfway gesture he made in the alcove with Selene a month ago — the gesture of a person who realizes there is no gesture that would help. He lowers the hand. He puts it on the console for one second. A meter from her. Present. Not touching."

    "He removes the hand."

    "He walks to the door. He does not look back."

    "Lyra does not leave with him. She stays at the console for ten more seconds. She is looking at Noelle."

    l "I am going to walk Aeron to his quarters before I go to the medbay. He needs the company on the corridor. I want you to know I am doing it. I am not doing it because Aeron asked. I am doing it because the floor and the room are different things and tonight is a night when the room needs to be there for him in a particular shape, and I am the shape."

    n "I understand."

    l "Will you be all right alone."

    "Noelle holds her eyes on Lyra for a count of three. The count is plain. She is not measuring it. She is not filing the measure. She is holding the count because the count is the answer Lyra is asking for."

    n "Yes."

    n "I am going to sit with the room for a while. The room is different than it was an hour ago. The differentness is mine to sit with. The sitting is the work."

    l "Then I will go."

    "She turns. She walks to the door. At the door she pauses and turns back."

    l "Noelle."

    n "Yes."

    l "Thank you for the etymology. I have been carrying it for a long time. I did not know I was carrying it for someone."

    "Noelle nods once."

    "Lyra leaves."

    "The door closes."

    "Noelle is alone."

    "She does not return immediately to the screens. She sits in the chair. Her hands are on her knees. She looks at the amber lamp on the secondary workstation. The lamp is unplugged. She does not plug it in. She looks at it the way she looked at the AUTHOR field in the coda — a thing visible all along, registering for the first time as visible."

    nthought "The lamp is the lamp. It is going to be unplugged for as long as it is unplugged. The deciding is mine to make. I am not making it tonight."

    nthought "The room is different."

    "She does not type. She does not return to the workspace work. She sits."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("verdant_payoff_complete", True)
    $ flag("aeron_protocol_verdant_revealed_emp", True)
    $ flag("lyra_placement_revealed_emp", True)
    $ flag("liora_file_handed_emp", True)
    $ flag("faber_countersign_protocol_revealed", True)
    $ canon_set("aeron.protocol_verdant_status", "preserved_breeding_subject_revealed")
    $ canon_set("aeron.fate_lie_unmasked", True)
    $ canon_set("aeron.knows_lyra_was_placed", True)
    $ canon_set("aeron.has_liora_file_emp", True)
    $ canon_set("lyra.protocol_verdant_status", "matched_ethereal_subject_revealed")
    $ canon_set("lyra.knows_placement_authorship", True)
    $ canon_set("lyra.placement_floor_distinction_held", True)
    $ canon_set("noelle.delivered_verdant_payoff_emp", True)
    $ canon_set("noelle.gave_liora_file_to_aeron", True)
    $ canon_set("noelle.received_korr_etymology_from_lyra", True)
    $ canon_set("liora.faber_protection_revealed", True)
    $ rel_bump("Noelle", trust=2)
    $ rel_bump("Lyra", trust=1)
    $ npc_remember("Noelle", "delivered_verdant_three_movements_emp", weight=3)
    $ npc_remember("Noelle", "received_korr_kore_etymology_from_lyra", tone="seen_by_the_priest")
    $ npc_remember("Noelle", "watched_aeron_take_handoff_with_thumb_contact", tone="present_not_touching_inversion")
    $ npc_remember("Aeron", "received_protocol_verdant_revelation_with_lyra_present", tone="placement_floor_held")
    $ npc_remember("Aeron", "took_liora_file_in_workspace", tone="third_person_holding_a_piece_of_mother")
    $ npc_remember("Lyra", "received_placement_revelation_named_floor_distinction", tone="floor_is_not_the_room")
    $ npc_remember("Lyra", "gave_korr_etymology_to_noelle_recognized_persephone", tone="cathedral_taught_to_priest_received")
    $ npc_remember("Lyra", "walked_aeron_to_quarters_after_brief", tone="room_in_a_particular_shape")
    $ tp_seed("a4.verdant.payoff_emp")
    $ tp_seed("a4.lyra.placement_floor_distinction")
    $ tp_seed("a4.noelle.korr_etymology_received")
    $ tp_seed("a4.aeron.liora_file_in_hand")
    $ tp_seed("a5.faber.unanswered_question")
    $ metric("noelle_compartments_unsealed", change=1)
    $ metric("aeron_compartments_held_alone", change=-1)
    $ scene_mark(_current_scene_id, "completed")
    call li_lore_check("Noelle") from _a4_s20b_lore
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s20b_verdant_decrypt_emp
# cann.chapter: Act IV — Shared Authority — VERDANT PAYOFF
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Late evening, 3rd of Glass 390 AC. 23:10. The decrypt finished
#     approximately one hour before the brief. Noelle has read it
#     twice. The brief lasts approximately ninety minutes of story
#     time. The scene ends with Aeron walking to his quarters with
#     the Liora file, Lyra walking him there, Noelle alone in the
#     workspace.
# cann.what_happened:
#   - Noelle has decrypted Protocol Verdant — the regime's bloodline-
#     preservation program. She summons Aeron and Lyra together (no
#     Selene this time; the personal layer goes to the personal
#     addressees first).
#   - MOVEMENT 1: Aeron is the last viable pure Verdant candidate.
#     His Branding rejection at age twelve was not failure — it was
#     evidence of lineage purity. Marcus authored the public "fate"
#     cover story to keep Aeron cooperating with the preservation.
#     Resonance-compatibility experiments were scheduled for 388-391
#     AC. Marcus delayed them when Aeron began drifting from Echelon
#     allegiance. Faber was on three of seven monitoring tiers.
#   - MOVEMENT 2: Lyra is the matched Ethereal candidate. Her
#     prodigy status, academic placement, Cathedral wing assignment,
#     proximity to the Rylan family — all CAD-authored Protocol
#     Verdant placement work. The Cathedral believes it placed her;
#     CAD placed her. Noelle is explicit that the placement was not
#     romantic engineering. CAD authored the geometry; the content
#     of the relationship is theirs.
#   - LYRA'S RESPONSE: she speaks the placement-floor distinction
#     in her liturgical reading voice: "Then it is also true that
#     whatever this is — between any of us — was authored after the
#     placement was complete. The placement is the floor. The floor
#     is not the room." Repeats it for herself. Names the
#     distinction in lthought: "The regime made the floor. The
#     regime did not make me." Turns a quarter-inch toward Aeron
#     without looking at him: "I am still here too."
#   - MOVEMENT 3: The Liora file. Noelle has had it for seven
#     months and one week — pulled at random in pre-defection
#     self-audit, recognized something in the pattern she could
#     not articulate, buried it. Three weeks ago the Verdant
#     decrypt revealed Liora is in the Verdant cohort tag as a
#     cataloged escape. Faber's countersign protocol has stopped
#     seventeen disposition orders against Liora across nineteen
#     years. Noelle does not know why Faber protected her.
#   - AERON'S RESPONSE: he names that Selene already told him about
#     Liora a month ago, that Selene has known for nine years,
#     Noelle for three weeks, Liora knew both knew. The not-telling
#     has been the protocol. The not-telling has been keeping Liora
#     alive. The bringing-in is the change. The not-telling is over.
#   - THE ETYMOLOGY: Lyra surfaces Korr-as-kore. "Korr is the name
#     the Cathedral kept for the daughter taken underground.
#     Persephone in the older tongue. She came back. She was
#     changed. The bringing-back is what the season is named for."
#     Noelle does not respond verbally. She nods once. Aeron
#     watches her nod.
#   - CLOSE: Noelle hands Aeron the Liora file crystal. Thumb
#     contact in the handoff. Aeron commits to read it tonight
#     alone in his quarters and brief Noelle at oh-six-hundred.
#     Lyra walks Aeron to his quarters before going to the medbay
#     for Tessa's runner. Lyra explicitly names the room is what
#     Aeron needs in a particular shape and she is the shape.
#     Lyra returns at the door to thank Noelle for the etymology:
#     "I have been carrying it for a long time. I did not know I
#     was carrying it for someone."
#   - Noelle is alone. Looks at the unplugged amber lamp on the
#     secondary workstation. Does not plug it in. Sits with the
#     differentness of the room.
# cann.aeron_state:
#   - Receives Protocol Verdant revelation. Marcus's "fate" lie is
#     now operationally sized — preservation as breeding stock,
#     scheduled experiments, delayed when he drifted. The lie was
#     designed against his own moral architecture.
#   - Now knows Lyra was a placement. Names the not-telling that
#     has surrounded Liora. Selene+Noelle+Liora ring of strategic
#     minds holding pieces of his mother. The bringing-in ends the
#     not-telling.
#   - Carries Liora file in hand. Will read tonight. Will brief at
#     oh-six-hundred. Will not decide before reading.
#   - The hand-on-console gesture from a4_s09 returns here — a
#     meter from Noelle, present, not touching. The gesture is
#     now established as Aeron-for-Noelle vocabulary.
# cann.lyra_state:
#   - Receives placement revelation. Names the placement-floor
#     distinction in her liturgical voice. The distinction is the
#     scene's most quoted line and is now Lyra's working principle:
#     the regime made the floor; the regime did not make her.
#   - Receives the Liora file's existence as a matter to know
#     about, not act on. Holds it. "I will tell you when I am
#     ready to discuss any of them. The telling will not be an
#     apology."
#   - Surfaces the Korr/kore etymology to Noelle. Cathedral
#     teaching applied to the priest's friend. Names Persephone in
#     the older tongue. The bringing-back is what the season is
#     named for.
#   - Walks Aeron to his quarters. Names that the room needs to
#     be there in a particular shape and she is the shape. The
#     scene's quietest character moment.
# cann.noelle_state:
#   - Delivers Verdant payoff in three movements. Post-coda voice:
#     plainer than s09, shorter sentences, no register-leading.
#   - Names her own pre-coda instinct work: "I have been doing the
#     unmeasurable work for longer than I have had a name for it.
#     Lyra taught me the name." First explicit ratification of
#     a3_int_02_noelle_unmeasurable as foundational to her arc.
#   - Receives the Korr/kore etymology from Lyra. Nods once. Does
#     not respond verbally. The receiving is the work she has been
#     learning to do since the coda.
#   - Catches herself saying "Acknowledged" — the OB-default word
#     — when Lyra delivers the placement-floor line. Lets the
#     catch happen. Does not correct it. The not-correcting is
#     also the work.
#   - Alone at scene close. Looks at unplugged amber lamp. Does
#     not plug it in. The lamp is the room's smallest unanswered
#     question. She is not answering it tonight.
# cann.path_tracking:
#   - EMP path only. Linear. No branching. The OB equivalent
#     (a4_s20b_verdant_decrypt_ob — pending) plays a structurally
#     different scene: Aeron and Noelle alone, two movements only,
#     no Lyra, the Liora file is filed as targeting intelligence,
#     the Korr/kore etymology does not happen.
# cann.thematic_flags:
#   - "The placement is the floor. The floor is not the room."
#     Lyra's load-bearing line. The distinction governs every
#     subsequent reference to the placement. Noelle, Aeron, and
#     Lyra each carry the line forward.
#   - The Korr/kore etymology lands. Lyra recognizes Persephone in
#     Noelle's surname. The Cathedral kept the older meaning. The
#     priest gives the older meaning back to the priest's friend.
#     The receiving is silent. The line is gift, not exegesis.
#   - The not-telling protocol named and ended. Selene/Noelle/Liora
#     have been holding pieces of Aeron's mother. The
#     bringing-in is the change. Future scenes referencing Liora
#     should treat her as known-alive across the rebellion's
#     command tier.
#   - Faber's countersign protocol revealed as the mechanism that
#     protected Liora across nineteen years. Noelle does not know
#     why Faber chose to protect her. The unanswered question is
#     canonical. tp_seed a5.faber.unanswered_question.
#   - The post-coda voice consolidates. Noelle's "Acknowledged"
#     catch is the OB-residue she lets through and does not
#     correct. The not-correcting is the EMP version of the OB
#     coda's correction-always-comes. EMP Noelle lets the residue
#     stand. OB Noelle would have refined it. The path system in
#     a single uncorrected word.
#   - Presence-without-touch vocabulary extended: Aeron's hand on
#     the console for one second, a meter from Noelle. Returns
#     from a4_s09. Lyra's quarter-step closer to the console at
#     scene start, quarter-inch turn toward Aeron at the placement
#     line — Lyra entering the same vocabulary in real time.
# cann.character_moments:
#   - Noelle: short metadata annotation in the new hand —
#     KORR — c/r reviewed. The two-character first-name
#     designation is the post-coda voice in operational form.
#     The technical-regular hand is gone.
#   - Noelle: explicit framing of the personal-layer ordering as
#     learned from a4_s10a. First time she names Selene-Liora as
#     a structural precedent for her own work.
#   - Noelle: "I have been doing the unmeasurable work for longer
#     than I have had a name for it. Lyra taught me the name."
#     The thank-you that is not phrased as a thank-you.
#   - Lyra: liturgical-reading voice for the placement line. She
#     does not know the voice is the placement-shaped voice until
#     she finishes the sentence. The recognition lands inside the
#     line.
#   - Lyra: prayer beads in pocket through movements 1 and 2.
#     Removed for the etymology line. The beads are the tool used
#     for a non-tool purpose.
#   - Lyra: explicit framing of walking Aeron as a shape-of-room
#     work, not a favor to Aeron. First time the rebellion's
#     priest names her own choosing as architectural rather than
#     ministerial.
#   - Aeron: "Marcus's lie was bigger than I knew." The scene's
#     most compressed Aeron line. The compression is the
#     character moment.
#   - Aeron: thumb contact with Noelle at the file handoff. Brief.
#     Intentional. Says nothing about it. The Aeron-for-Noelle
#     touch register being established for future scenes.
# cann.callbacks:
#   - a4_s09_noelle_implicated_emp: the workspace, the chair, the
#     hand on the console, the three-step distance. All return.
#   - a4_s09a_noelle_coda_emp: the post-coda voice, the new hand,
#     the unplugged amber lamp, the not-correcting practice. All
#     active here for the first time in dialogue with other
#     characters.
#   - a4_s10_what_selene_meant_emp: shared command, the alcove
#     register, the okay-as-rule-acceptance.
#   - a4_s10a_liora_sent_word_emp: Selene's delivery of Liora's
#     packet. Aeron names this scene explicitly in movement 3
#     ("Selene already told me Liora is alive"). The Verdant
#     payoff is the second movement of the same family-sentence
#     Selene began.
#   - a3_int_02_noelle_unmeasurable_emp: Noelle ratifies it
#     in scene as foundational. "Lyra taught me the name."
#   - canon_notes_noelle.md sec 8 (Protocol Verdant): the
#     three movements outlined there are delivered here in full.
#   - canon_notes_noelle.md sec 13.4 (Korr/kore — Lyra's
#     Recognition): the etymology lands here in the form
#     specified. The placement line and the etymology line both
#     deploy as canon-locked.
#   - canon_notes_noelle.md sec 4 (The Liora File): the file is
#     handed to Aeron. Faber's countersign protocol named in
#     scene as the protective mechanism.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. EMP path only. The
#     thesis-level Verdant reveal scene. Foundational for: every
#     subsequent EMP scene where Liora can be referenced as
#     active rather than dead, every scene where Lyra references
#     the placement, every scene where Aeron processes Marcus's
#     "fate" lie, the Tessa-Noelle anchor (where Noelle can now
#     speak about Faber as a known antagonist with named
#     countersign protocol).
# cann.requires_followup:
#   - Aeron reads the Liora file tonight. Briefs at 06:00 the
#     next morning. The decision about contact with Liora becomes
#     the next operational thread. Open authoring territory.
#   - The placement-floor distinction now governs every Lyra/Aeron
#     scene from this point forward. Future erotic or intimate
#     scenes between them must respect that the floor was authored
#     and the room was not. The distinction is not destabilizing —
#     it is foundational.
#   - Faber's protective protocol is canonized but motive-less.
#     Noelle does not know why Faber chose to protect Liora.
#     tp_seed a5.faber.unanswered_question. If Faber is ever
#     confronted on TP path (per canon_notes_noelle.md sec 13.3),
#     the question of why-Liora is the load-bearing question.
#   - Noelle's relationship with Lyra is now named as a
#     teacher-pupil-mutual register. Future Noelle/Lyra scenes
#     should respect that the etymology has passed in this
#     direction and the unmeasurable name has passed in the
#     other.
#   - The amber lamp is now load-bearing. It has been unplugged
#     since at least the s10 OB drafting (canon convergent across
#     paths) and remains unplugged here at scene close. Future
#     workspace scenes where Noelle plugs in or moves the lamp are
#     canonical inflection points.
#   - The OB equivalent (a4_s20b_verdant_decrypt_ob) is the next
#     scene to author. Expected shape: Aeron and Noelle alone,
#     two movements only (no Lyra), the Liora file is filed by
#     Aeron as targeting intelligence ("Hold it. We will use it
#     when we need her"), the Korr/kore etymology does not
#     happen, Noelle's silent close: "I gave him a person and
#     he took a vector."
# =========================================================
