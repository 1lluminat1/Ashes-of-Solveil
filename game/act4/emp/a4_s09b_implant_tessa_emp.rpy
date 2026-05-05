# =======================================================
# ACT 4 - Scene 09b: Held (Empathy Path)
# File: a4_s09b_implant_tessa_emp.rpy
# Type: TESSA × NOELLE ANCHOR — Aether Tag discovery + removal
# Matrix: Tessa as the hand that cuts; Noelle as the patient.
#         Structural follow-up to A2_P14 ("The Patient"), inverted.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s09b_implant_tessa_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s09b_implant_tessa_emp:
    $ show_timeline("29th of Forge, 390 A.C.", "08:40", "Phoenix Secondary Base — Medbay Theater")

    # Codex stage bumps
    $ codex_reveal("noelle_korr", to_stage=4, source="a4_s09b_implant_tessa_emp")
    $ codex_reveal("tessa_kael", to_stage=4, source="a4_s09b_implant_tessa_emp")
    $ codex_unlock("aether_tag", source="a4_s09b_implant_tessa_emp")
    $ codex_unlock("halen_vance", source="a4_s09b_implant_tessa_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm at scene open, the medbay theater discipline. Tessa's
    #         room. The two task lights over the surgical table at full
    #         the way she wants them. The scene opens on Tessa's hands —
    #         tying the strings of her surgical gown, then settling the
    #         instruments on the stainless tray. The hands resolve before
    #         the face. The hands have been the motif. The hands are the
    #         scene's first subject.
    #         Coverage shifts across the scene: tight on Tessa's hands
    #         during the scan and the procedure; tight on Noelle's face
    #         during the surgery — she is awake, she has to be awake, the
    #         camera is the witness her face has agreed to. Two-shot for
    #         the Halen conversation: Tessa above her, hands working,
    #         Noelle on her side on the surgical table, both of them in
    #         the same frame for the duration of the conversation. The
    #         two-shot is the geometry of being held.
    # LIGHTING: Medbay theater. Two task lights at full overhead. The
    #           surgical field is the bright spot in the room. Around
    #           the field, the room dims — the tile, the trays, the
    #           cabinet. The peripheral darkness is intentional in
    #           Tessa's spaces; she reduces what is visible in the
    #           periphery so the patient's eye does not work to rest on
    #           anything. The scene takes place inside the bright spot.
    # SFX: Medbay ambient. The slow tick of the standing autoclave at
    #      the back of the room (a constant Tessa has tuned out). The
    #      hum of the surgical lamps. The small mechanical sounds of
    #      Tessa's instruments — the clip of the prep tray, the thin
    #      ring of the tweezer touching the steel basin, the crinkle
    #      of the sterile drape unfolding. One-shots: Noelle's neck
    #      adjustment as she lies on her side; the scanner chime when
    #      Tessa runs the resonance pass over the base of her skull;
    #      the small confirmation tone when the Aether Tag flashes
    #      back at scanner frequency; the brief surgical-field noise
    #      of the incision; the small pop when the tag releases from
    #      its anchor. No music bed. The scene is hands and breath.
    # FACE: Tessa — working face. The face from A2_P14 in inverted
    #        position. She is not the one in the worst-case zone now;
    #        she is the one holding the clamp. The face has the same
    #        stillness it had when she pulled Noelle into the work
    #        the first time. The stillness has had a year of practice
    #        since.
    #        Noelle — the post-coda face. The defection coda was nine
    #        hours ago. She has not slept since. She is here at oh-
    #        eight-forty because Tessa scheduled the scan two days
    #        ago and Noelle does not break Tessa's appointments. The
    #        face is calm in a different way than it was in s09a —
    #        the calm of a person who has been awake long enough that
    #        the face is doing the work for her.
    # BLOCKING: Tessa at the surgical tray, then beside the table,
    #           then over Noelle's head for the procedure. She moves
    #           four times in the scene. Each movement is small.
    #           Noelle on the table. Initially seated, then lying on
    #           her side at the prep, then still on her side for the
    #           procedure. The angle of her head exposes the base of
    #           her skull. The procedure is twenty-two minutes long
    #           in story time. The conversation is most of that.

    # ========= VOICE BASELINE =========
    # Tessa: working register. Clinical-checks as emotional probes —
    #         "Can you still feel this?" is the medical question and
    #         the relational question. She does not deploy the
    #         question lightly. When she deploys it, both layers are
    #         active. The "It does not have to. Hold still." line
    #         arrives at the moment of incision and is the scene's
    #         load-bearing exchange.
    # Noelle: post-coda voice. Plainer than s09. The grief register
    #          is now accessible. The Halen conversation is the
    #          first time she has spoken his name aloud since
    #          discovering his death nine hours ago. The voice
    #          cracks once during the procedure. Tessa does not
    #          patch the crack. The crack stays open through the
    #          rest of the procedure.

    # scene bg_medbay_theater_morning with dissolve
    # play ambient "sfx/ambient/medbay_theater.ogg" fadein 2.0

    # ========== PHASE 1 — THE SCAN ==========

    # CAMERA: 50mm. Open on Tessa's hands at the prep
    #         tray. The hands are the scene's first
    #         subject. Tessa's face resolves on the
    #         second beat. Noelle is seated on the
    #         exam side of the table when the camera
    #         widens.

    "The medbay theater is small — one surgical table, one prep cabinet, one autoclave at the back, one set of overheads. The two task lights are the brightest things in the room. Tessa runs her medbay the way she runs her anchors: the periphery dims, the working surface stays clear."

    "Noelle arrives at oh-eight-forty. She has not slept. She has not been to her quarters since the data alcove — she went straight from the workspace to the medbay corridor and sat in the corridor for an hour and twenty minutes waiting for the appointment that was scheduled two days ago. The corridor sit was a procedural choice. She did not want to walk into her quarters and have the quarters be a room she had to operate inside."

    "Tessa registers the not-sleeping inside the first ninety seconds of seeing her."

    t "When did you last sleep."

    n "I will sleep tonight."

    t "That is not the question I asked."

    n "Three days ago. Six hours."

    t "I am noting that. Sit on the table for me."

    "Noelle sits. The table is at standard exam height. Tessa's hands wash at the basin — a thirty-second wash, the hands she has been tuning since the Wards clinic. She dries them on the small white towel. She picks up the resonance scanner from the second tray and crosses to Noelle."

    t "Headaches still in the same place."

    n "Base of the skull. The same place. The intensity has tracked operational stress reasonably well. The last forty-eight hours scored higher than baseline. I assumed the operational tempo was the cause."

    t "I am going to scan and we will see whether the operational tempo was the cause or whether the operational tempo was an accelerant on a separate cause. I am going to ask you to tilt your head forward and let your hair fall."

    "Noelle does. The base of her skull is exposed. Tessa's left hand settles at the crown of her head — light contact, the kind of contact a doctor makes to indicate the patient should stay where they are. The right hand brings the scanner over the base of the skull. The scan pass is slow. Two seconds across, hold for one second at the suspect zone Tessa already had on her clipboard."

    "The scanner chimes once at the medical confirmation frequency. Then a second time at a lower tone — the resonance-detected tone. Then a third tone, brief, sharp, at a frequency Noelle's ear catches before her conscious mind processes it."

    nthought "That is a CAD-internal scanner band acknowledgment."

    "She does not say it aloud. The scanner has reported what it reported. Tessa is reading the scanner display."

    "Tessa puts the scanner down."

    "Her hand stays at Noelle's crown for two seconds longer than it needs to."

    t "Noelle. There is a passive monitoring device implanted at the base of your skull. It is approximately the size of a fingernail clipping and it is sitting against the bone, not under it. The anchor is shallow. The device has been transmitting on a low duty cycle. It is transmitting now."

    "She lets the sentence land. Her hand does not leave the crown."

    t "Tell me what I am looking at."

    "Noelle does not move."

    n "It is a CAD-issue Aether Tag. Researcher-class. Standard for upper-tier CAD personnel handling classified cognitive material. The internal name for it among the researchers who carry it is *the leash.* I did not know I had one. The not-knowing was part of the design. Faber would have signed the implant order. The implant procedure would have been embedded in a routine medical visit during my orientation year. Probably the standard initial physical at the academy-to-CAD transition."

    n "I have been carrying it for nine years."

    "Tessa's hand has not left the crown."

    t "What does it do."

    n "Coarse location, sector-level, not building-level. Resonance signature — a unique identifier if anyone scans for it. Aggregate cognitive-load data via passive Band coupling. It does not record audio. It does not transmit content. It transmits enough to find me."

    n "The transmission band is CAD-internal. Ghostline cannot easily intercept. I would have detected it during my own pre-defection sweeps if I had thought to scan myself for it. I did not think to scan myself for it. The not-thinking-to was also part of the design."

    "A pause."

    t "How long has Echelon known where you are."

    n "Always. They have always known where I am. The leash has been transmitting since the broadcast. The base location has been in the CAD-internal grid for seven months. The resolution is sector-level — they have known I am in the rebellion's secondary base sector. They have not raided. The not-raiding is the question I do not have an answer for. The leash exists. The use of the leash has been deferred."

    n "I am going to need to brief Selene immediately after this procedure. The procedure is the procedure I assume you are about to run."

    t "You assume correctly."

    "Tessa's hand moves from the crown to Noelle's shoulder. Light pressure. The shoulder is where she puts the hand when the patient is calmer than the patient should be."

    t "I am going to remove it. The removal is awake-surgery. I cannot give you general anesthesia because anesthesia would suppress the cognitive-load signal in a way the implant would flag — the flag would route to Faber at oh-nine-hundred with a confidence interval that says *Vance is unconscious, possible disposition event.* I cannot risk the flag. You are going to be awake through it. The procedure is twenty-two minutes if I can hit the anchor cleanly and slightly longer if I cannot. The local anesthesia will cover the pain. The awake part is the cost."

    t "You can refuse. You can leave the leash in. We can compartmentalize what you are exposed to and run a closed-loop information control. I can keep treating you for headaches and we can both pretend the leash is not there. That is a path. I am offering it."

    "She watches Noelle's face for the answer."

    n "No. Take it out."

    "Two words."

    t "Acknowledged."

    "Tessa does not flinch at the word. The word is the word Noelle has been using. The word's OB-residue is something Tessa registers and does not flag. Her job tonight is the procedure. Words can be discussed at any post-procedure interval Noelle wants."

    # ========== PHASE 2 — THE PREP ==========

    # CAMERA: tight on Tessa's hands at the surgical
    #         tray. The instruments are laid out in
    #         the order she will use them — antiseptic
    #         pad, anesthetic syringe, scalpel, the
    #         small extraction tweezer she has been
    #         using for shrapnel since the Wards
    #         clinic, gauze, the suture kit. The order
    #         is operational and ritual at the same
    #         time. The hands work the prep without
    #         hesitation.

    "Tessa preps the tray. Noelle moves from sitting on the table edge to lying on her side, the position Tessa indicated with one hand. The pillow Tessa adjusts under Noelle's cheek is the pillow from the corridor's spare-supplies cabinet — the pillow nobody has used. Tessa has been keeping it for a procedure that would require comfort during awake surgery. She has not had occasion to use it before."

    "The sterile drape goes over Noelle's neck and shoulders, leaving the surgical field exposed. Tessa's gloved hand passes the antiseptic pad over the field. The antiseptic is cold. Noelle does not flinch. Her eyes are open. They are looking at the tile wall of the medbay."

    t "I am going to give you the local now. You are going to feel the needle. You are going to feel the cold. After the cold, you should not feel pain — if you do, tell me and I will adjust. The implant is going to register a small spike in cognitive-load when the local lands. The spike is consistent with stress and will not flag. I have run the numbers."

    n "Acknowledged."

    "The needle. Noelle does not move. The cold spreads."

    "Tessa picks up the scalpel. The scalpel rests in her palm for one second before she brings it to the field — the punctuation Noelle has seen Tessa use on the board after writing the last letter of a name. The scalpel pause and the pen pause are the same shape."

    "Noelle sees the pause from the corner of her eye. She files it without commenting."

    t "I am going to cut now. Can you still feel this."

    "Tessa's question is the medical question. Tessa's question is the relational question. Both layers are active. They have been active since A2_P14 when she pulled Noelle into the work the first time. The question is the question."

    n "I cannot feel the cold anymore."

    t "Good. I am going to make the incision. It will be small. Hold still."

    n "I will."

    # ========== PHASE 3 — THE PROCEDURE BEGINS ==========

    # CAMERA: tight on Tessa's hands. The scalpel makes
    #         the incision — small, precise, the field
    #         minimal. The camera does not push for
    #         gore. The procedure is shot at the
    #         distance Tessa runs her work. We see the
    #         hands. We see the field. We do not see
    #         more than the field requires.
    # SFX: the small surgical-field noise. The scalpel
    #      lifting. The blood-moisture in the field
    #      Tessa has minimized via the local. Tessa's
    #      breath at her standard working tempo. Noelle's
    #      breath, slower than Tessa's, the slowness a
    #      choice she is making.

    "Tessa makes the incision. The cut is twelve millimeters. The field opens minimally. Tessa's hand picks up the small extraction tweezer — the one with the angled tip she has been using since the Wards clinic, the tweezer that has retrieved more shrapnel from more wounds than any other instrument in her tray."

    "She does not begin the extraction yet. She talks first. Her voice is the voice she uses for awake-surgery patients — pitched slightly above her normal speaking voice, slow enough that the patient's processing has time to follow."

    t "The implant is at five-point-two millimeters depth. The anchor is thinner than a CAD-issue should be — they were optimizing for transmissibility, not retention. I am going to lift it from the anchor side first and work the body out laterally. You will feel pressure but no pain. The pressure will be brief."

    "Noelle's eyes are still on the tile wall."

    "Tessa's hand begins."

    "The pressure starts. Noelle takes a small breath at the start. The breath does not break the surgical field's stillness because the field is not at her chest. The breath is data. Tessa registers the breath."

    t "Talk to me, Noelle. Tell me what is in the room with you."

    "The question is the awake-surgery technique. Patients on awake surgery do better when their cognitive bandwidth is occupied by the conversation rather than by the procedure. Tessa learned the technique during the second Foundry collapse, when the medical-supplies shortage required ten percent of her cases to run with reduced anesthesia. The technique is the technique."

    "Noelle understands the technique. She understands she is supposed to talk."

    "She talks."

    n "I opened the personal data crystal nine hours ago."

    "Tessa's hand keeps working. The pressure shifts. The implant is beginning to release from its anchor. The release is slow and deliberate."

    t "Continue."

    n "I had been carrying the crystal for seven months. I had been postponing the opening. I told myself the postponement was operational — that I was waiting for an interval where the audit would not interfere with rebellion work. The interval never arrived. I never made it arrive. The postponement was the editing I was performing on myself."

    n "I opened it last night because I caught my own writing in Faber's syntax and the catching forced the question. The question was the question I had been postponing. The crystal had the answer."

    t "The crystal had four answers."

    "Tessa says it without looking up from the field. Her hand is at the implant's anchor edge. The pressure is steady."

    n "How do you know there were four."

    t "You came here at oh-eight-forty after a full night of not sleeping and you sat in the corridor for an hour and twenty minutes before the appointment. People who have made one discovery do not sit in corridors. They go to bed and they cry and they get up. People who have made four discoveries sit in corridors because the corridor is a place where no decision has to be made. Four was the floor of the estimate. I did not know it was four until you said it."

    "Noelle does not respond immediately."

    "The implant releases."

    "Tessa's hand lifts the small mechanical thing — fingernail-sized, brass-tone, the older CAD aesthetic — out of the field and onto the steel basin to her right. The implant clinks against the basin. The transmission frequency that has been the constant of Noelle's life for nine years cuts out. The cut is not audible — the frequency was sub-aural — but the absence of it is felt. Noelle feels it. Her shoulders, which have been holding a tension she did not know was a tension, drop a quarter-inch."

    t "It is out. I am going to hold the field open for thirty seconds while I check for residual transmission. I do not want to suture and find out later that there was a secondary node. Stay still."

    n "I will."

    # ========== PHASE 4 — THE HALEN CONVERSATION ==========

    # CAMERA: two-shot. Tessa above Noelle, hands
    #         working at the field. Noelle on her side,
    #         the eye on Tessa's side of the table
    #         visible. The two-shot holds for the rest
    #         of the procedure. The framing is the
    #         geometry of being held.
    # LIGHTING: unchanged. The two task lights. The
    #           field. The dimmed periphery.

    "Tessa holds the field. The thirty-second residual scan begins. She does not look at Noelle's face during the scan. Her eyes are on the scanner. Her hand is steady."

    t "Tell me the four discoveries. In order. The order will matter to you. Tell them to me in the order they landed."

    "The instruction is medical and relational. The instruction is the technique. The technique works because the patient hears the instruction as a question they can answer. The patient does not hear the technique."

    "Noelle answers."

    n "First: the editing of my own experience. CAD logs in my hand from days my calendar marks empty. Three hundred files across nine years. The thoroughness was operationally consistent."

    n "Second: Halen."

    "She does not continue immediately."

    "Tessa does not push. The thirty-second scan is at fourteen seconds. There is time."

    n "Halen Vance was my partner. Researcher in CAD. Joined with me — the bureaucratic register; we registered joint professional credentials for shared classified-project access. The joining was administrative. We had three years."

    n "The records said Halen was reassigned to Outer Wards Resonance Research Station, indefinite term. I have read the assignment line one hundred and twenty times in nine years. I never cross-referenced the dispatch manifests against the assignment line. The cross-reference was in my evidence package the entire time. I had compiled it in the seventy-two hours before defection. I had carried it across three safehouses. I never opened both at the same session."

    n "I opened them last night."

    "A pause."

    "The thirty-second scan is at twenty-two seconds."

    n "Halen never arrived at any Outer Wards station. The transfer was a fiction. Halen died on the day the records say they were reassigned. Halen has been dead for nine years. The fiction was the containment measure — Faber's principle, the trail of the editing must be smaller than the trail of the un-editing. Echelon killed Halen because the relationship was reducing my CAD productivity. Operational logic. The fiction was maintained because if I had known Halen was dead I would have searched. If I had known Halen was alive elsewhere I would not. The fiction kept me at CAD."

    n "I have been signing Halen's name on every official document I have ever produced. The joining was administrative. The credential update changed my professional surname to Vance. The editing took the relationship and left the surname. I have been writing Halen's name with my hand for nine years without remembering whose name it was. I signed it on the framework I gave Aeron yesterday evening. He read it on the pad. He did not ask. I did not explain."

    "Her voice cracks at *did not explain.*"

    "The crack is small. A quarter-inch. The same quarter-inch Tessa watched in s09."

    "Tessa does not patch the crack. She lets it stay open. Her hand is still in the field. The thirty-second scan is at twenty-eight seconds."

    n "I do not know if I am crying about a person I cannot remember loving or about the procedure. The data does not separate cleanly."

    "Tessa speaks for the first time in the conversation."

    t "It does not have to. Hold still."

    "Five words. Two clauses."

    "The first clause is the medical answer — *the data does not have to separate cleanly.* It is also the relational answer — *grief does not have to come labeled, you do not owe yourself a clean attribution before you are allowed to feel it.* Both layers active. Tessa has not deployed the *can-you-still-feel-this* register lightly in a year. She is deploying it here. The deployment is the work."

    "The second clause is the procedural instruction. The thirty-second scan is at thirty seconds. The scan completes. No residual transmission. The field is clear."

    "Tessa puts down the scanner. She picks up the suture needle."

    t "I am going to close. I will tell you when the suture is done. While I close, you can keep talking or not talk. Your choice. The conversation has helped your cognitive load through the procedure. We are past the part where I need it to. The next part is just stitches. The stitches do not have a register requirement."

    n "I will keep talking."

    t "All right."

    "Two syllables. Plain. Tessa uses the word the way Noelle used it in the coda last night and did not delete. The word arrives in the room without correction. Noelle hears it. The hearing is part of the procedure."

    n "Third: my parents."

    "Tessa's hand begins the first suture."

    n "The NDI baseline file metadata names me as Cohort C-04 (PILOT) longitudinal subject. Project lead and co-lead are Anesh and Talen Korr. My parents. I was four when the study began. I was eleven when I read my father's desk and found the strategic assessment with the *acceptable margins* sentence in it. I have been telling that desk story for twenty years as the reason I became an analyst. The story has been wrong in one specific way that took me twenty years to see."

    n "The strategic assessment I read at eleven was my own data. The cohort the assessment described was my cohort. The acceptable margins were projected against me. I read about myself at eleven and I did not know it was about me."

    "Tessa makes a small sound. Not a word. A breath out. The kind of breath she makes when a runner she did not expect to save is going to live."

    "Noelle hears it."

    n "Yes."

    n "Fourth: the surname. Vance. I named it earlier. I could see the AUTHOR field on the file and I could not see what the field said until I had held the first three discoveries long enough to read it. The fourth was the smallest. The fourth was the room the others had been living in."

    "Tessa has placed three sutures. She is on the fourth. The work is steady. The conversation is not interrupting it. The conversation and the work are happening in the same hands."

    t "I am going to ask you something I have not asked you before."

    n "Ask."

    t "Are you all right."

    "The question is the question Noelle has been correcting for nine years. She corrected it in the OB version of last night's coda — *imprecise, the precise version is operational consistency.* She did not correct it in the EMP version of last night. She let it stand. *All right* was the first plain sentence she had thought tonight without Faber's hand inside it."

    "She lets Tessa's question stand without correcting it either."

    n "No."

    n "I am not all right."

    n "I am telling you because you asked. I am telling you because the asking is a thing you have not done before. I am telling you because *all right* is a word I am still learning the shape of, and tonight the shape includes the answer being *no.*"

    n "I am going to be all right at some point. I am not telling you when. I am telling you what is true tonight."

    t "Acknowledged."

    "She uses the word back. Not as correction. As acceptance."

    "Tessa places the fifth suture. The wound closes. She trims the suture thread. She lifts the gauze pad."

    t "I am done. The procedure is closed. The implant is on the basin. The scan is clear. You can sit up when your cognitive-load registers a stable interval — give it two minutes. I am going to walk to the basin and bag the implant for the Selene brief."

    "She steps away from the table. Two paces to the basin. The brass-tone implant is sitting on the steel."

    "She picks it up with the small forceps. She drops it into a sealed evidence bag. The bag goes on the prep tray."

    "She washes her hands."

    # ========== PHASE 5 — THE AFTER ==========

    # CAMERA: pulls back to wide on the medbay theater.
    #         The two task lights still at full. The
    #         autoclave still ticking. Noelle on the
    #         table, sitting up now, the gauze pad
    #         taped at the base of her skull. Tessa at
    #         the basin, drying her hands.
    # LIGHTING: unchanged. The bright spot. The
    #           periphery dim.

    "Noelle sits up. She does it slowly. The cognitive-load registry stabilizes. She places her hand at the back of her neck, careful of the gauze. The gauze is small. The wound under it is twelve millimeters. The wound is going to heal."

    "Tessa returns to the table. She is not in surgical posture anymore. She is in the post-procedure posture — the one she uses when the work is done and the patient is the patient and not the procedure. The two postures are different and both belong to her."

    t "I am going to give you three things and then I am going to send you to your quarters. Listen."

    n "I am listening."

    t "One. Sleep. Today. Eight hours. I will tell Selene you are on medical leave from oh-nine-hundred to seventeen-thirty. I will not tell her why. I will tell her it is post-procedure and she will not press. You sleep."

    "Two."

    "She does not say *two* aloud. The two is Tessa's hand. Tessa puts her hand on Noelle's right hand for three seconds. The contact is the kind of contact Tessa makes after a procedure that has crossed into a register the patient may not have a name for. The contact does not require words. The hand is the second thing."

    "Tessa lifts her hand."

    t "Three. You are going to come back here tomorrow at oh-eight-hundred. I am going to look at the suture. We are going to drink tea. The tea is operationally indicated. The tea is also the thing you and I are going to do because we have not had tea since the Patient and the Patient was a year and four months ago. We are overdue."

    n "I will come."

    t "Good."

    "She steps back from the table."

    "Noelle does not stand yet."

    "She is looking at the implant in the evidence bag on the prep tray."

    nthought "Nine years."

    nthought "The leash was nine years of my life. The procedure was twenty-two minutes. The ratio is not what I would have predicted."

    nthought "The ratio also does not matter."

    "She closes her eyes for one second. She opens them."

    n "Tessa."

    t "I'm here."

    n "Thank you."

    "She does not elaborate."

    "She does not need to."

    t "Go sleep, Noelle."

    "Noelle stands. Her balance holds. She walks to the medbay door. At the door she pauses and turns back."

    n "Tomorrow oh-eight-hundred. Tea."

    t "Tea."

    "Noelle leaves."

    "Tessa is alone in the medbay theater. The two task lights are still at full. The implant in the evidence bag is on the prep tray. The autoclave is still ticking. Tessa stands at the table for a count of nine — a count she does not know is a count Noelle has been keeping since her own coda — and then she goes to the autoclave and she begins the next prep cycle. The next patient is at oh-ten-thirty."

    "The work continues."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("noelle_implant_discovered_emp", True)
    $ flag("noelle_implant_removed_emp", True)
    $ flag("noelle_halen_disclosed_to_tessa_emp", True)
    $ flag("tessa_noelle_anchor_ii_complete_emp", True)
    $ canon_set("noelle.implant_status", "removed")
    $ canon_set("noelle.implant_carry_duration_years", 9)
    $ canon_set("noelle.implant_evidence_bag_location", "tessa_medbay_prep_tray")
    $ canon_set("noelle.crying_register_engaged_first_time", True)
    $ canon_set("noelle.tessa_received_halen_disclosure", True)
    $ canon_set("noelle.medical_leave_status", "active_until_1730")
    $ canon_set("tessa.has_noelle_halen_information", True)
    $ canon_set("tessa.tomorrow_tea_appointment_set", True)
    $ rel_bump("Tessa", trust=3, affection=2)
    $ npc_remember("Tessa", "removed_aether_tag_from_noelle_awake_surgery", weight=3)
    $ npc_remember("Tessa", "received_halen_vance_disclosure_during_procedure", tone="hand_that_holds_through_grief")
    $ npc_remember("Tessa", "asked_are_you_all_right_received_no_for_answer", tone="acknowledged_as_acceptance")
    $ npc_remember("Tessa", "set_tomorrow_tea_appointment", tone="overdue_a_year_and_four_months")
    $ npc_remember("Noelle", "named_halen_vance_aloud_first_time", tone="grief_register_accessible")
    $ npc_remember("Noelle", "let_tessa_question_stand_without_correcting", tone="all_right_held_as_word")
    $ npc_remember("Noelle", "felt_implant_absence_through_shoulder_drop", tone="leash_cut")
    $ npc_remember("Noelle", "thanked_tessa_without_elaborating", tone="post_procedure_quiet")
    $ tp_seed("a4.tessa.noelle.held")
    $ tp_seed("a4.noelle.halen_named_aloud")
    $ tp_seed("a4.noelle.tea_tomorrow")
    $ metric("noelle_compartments_unsealed", change=1)
    $ scene_mark(_current_scene_id, "completed")
    call li_lore_check("Tessa") from _a4_s09b_lore
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s09b_implant_tessa_emp
# cann.chapter: Act IV — Shared Authority — TESSA × NOELLE ANCHOR II
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Morning of 29 Forge 390 AC. Oh-eight-forty. Approximately nine
#     hours after the close of a4_s09a (Defection Coda). Noelle has
#     not slept. The appointment was scheduled two days prior for
#     low-grade headaches that have been intensifying with operational
#     stress. The procedure runs twenty-two minutes story-time. The
#     scene runs approximately forty minutes total including prep and
#     post-procedure framing.
# cann.what_happened:
#   - Tessa runs a routine resonance scan on the base of Noelle's
#     skull. The scanner detects an implanted CAD-issue Aether Tag
#     ("the leash" in CAD researcher slang). The tag has been
#     transmitting on a low duty cycle for nine years. CAD has had
#     sector-level location on Noelle since defection.
#   - Noelle identifies the tag from the scanner band acknowledgment
#     before Tessa names it. Confirms what it is: passive monitoring,
#     coarse location, resonance signature, aggregate cognitive-load
#     via Band coupling. No audio, no content. Faber would have
#     signed the original implant order, embedded in a routine
#     orientation-year medical visit.
#   - Tessa offers Noelle the choice — leave the leash in (closed-
#     loop information control, both pretend the leash is not there)
#     or remove it (awake surgery, twenty-two minutes, anesthesia
#     suppressed because anesthesia would flag a possible
#     disposition event to Faber at oh-nine-hundred).
#   - Noelle: "No. Take it out." Two words.
#   - Tessa preps. Local anesthetic. Twelve-millimeter incision.
#     Awake surgery. Noelle on her side, the procedure on the bright
#     spot, the periphery dimmed.
#   - During the procedure Tessa uses the awake-surgery technique:
#     occupies the patient's cognitive bandwidth with conversation.
#     "Talk to me, Noelle. Tell me what is in the room with you."
#   - The conversation lands on the four discoveries from a4_s09a:
#     1. The editing of her own experience.
#     2. Halen Vance — the first time Noelle has named Halen aloud
#        since discovering the death nine hours ago. Names the
#        joining, the credential update, the surname-residue, the
#        nine years of signing Halen's name. Voice cracks at "did
#        not explain." Tessa does not patch the crack.
#     3. Her parents — Anesh and Talen Korr — as the project leads
#        on the Cohort C-04 NDI baseline. The eleven-year-old at
#        the desk was reading her own data.
#     4. The Vance surname on the AUTHOR field. The smallest
#        revelation. The room the others had been living in.
#   - The load-bearing exchange at the moment of Noelle's voice
#     crack: "I do not know if I am crying about a person I cannot
#     remember loving or about the procedure. The data does not
#     separate cleanly." / "It does not have to. Hold still."
#   - The implant releases from its anchor. Tessa lifts it onto the
#     steel basin. The transmission frequency cuts. Noelle's
#     shoulders drop a quarter-inch — the absence felt in her body.
#   - Tessa places five sutures while Noelle finishes the four
#     discoveries. After closing, Tessa asks: "Are you all right."
#     Noelle does not correct the question. "No. I am not all
#     right." Tessa's response: "Acknowledged" — used as
#     acceptance, not correction.
#   - Tessa gives three closing items: medical leave until 17:30
#     today (Selene briefed at "post-procedure" without specifics);
#     a hand on Noelle's right hand for three seconds (the second
#     item, unspoken); a tomorrow-oh-eight-hundred tea appointment
#     ("the tea is operationally indicated. The tea is also the
#     thing you and I are going to do because we have not had tea
#     since the Patient. We are overdue").
#   - Noelle thanks Tessa without elaborating. Sets the tomorrow
#     appointment. Leaves.
#   - Tessa alone in the medbay. Stands at the table for a count of
#     nine — unknowingly mirroring Noelle's count from the coda —
#     then begins the next prep cycle. The work continues.
# cann.tessa_state:
#   - Removes the Aether Tag in awake surgery. The procedure is
#     within her established range. The conversation she runs
#     through the procedure is the awake-surgery technique she
#     learned during the second Foundry collapse.
#   - Receives the Halen Vance disclosure. The first person in the
#     rebellion to know about Halen besides Noelle. Holds the
#     information. Does not pry. Does not patch the crack when
#     Noelle's voice breaks.
#   - Deploys "Can you still feel this?" as both medical and
#     relational question. Both layers active. The deployment is
#     the work.
#   - Closes the procedure. Sets the tomorrow tea appointment —
#     the structural follow-up to A2_P14 ("The Patient"). Names
#     the year-and-four-months interval as "overdue."
#   - Stands at the table for a count of nine after Noelle leaves.
#     The count is the small Tessa equivalent of the silence
#     Noelle held in the coda. Tessa does not know she is keeping
#     the count.
# cann.noelle_state:
#   - Implant removed. The leash is cut. The transmission frequency
#     that has been the constant of her physical experience for
#     nine years is gone. The body registers the absence — the
#     quarter-inch shoulder drop is the only visible effect, but it
#     is the effect.
#   - Names Halen aloud for the first time. The naming opens the
#     grief register that the coda had brought to the surface but
#     not yet given speech. Tessa is the first audience.
#   - Voice cracks once during the disclosure. The crack stays
#     open through the rest of the procedure. The not-patching is
#     the work Tessa is doing.
#   - Says "No. I am not all right" to a question she has spent
#     nine years correcting. The not-correcting is the second
#     post-coda artifact (the first is letting "Acknowledged"
#     stand uncorrected in a4_s20b). She is learning the shape of
#     the word "all right" — including the shape where the answer
#     to it is "no."
#   - Thanks Tessa without elaborating. Sets the tomorrow
#     appointment. Walks out under her own power. Goes to her
#     quarters to sleep. Medical leave until 17:30.
# cann.path_tracking:
#   - EMP path only. The OB equivalent (a4_s10b_implant_tessa_ob,
#     pending) plays the structurally inverted scene: Tessa
#     identifies the implant, recommends removal, Noelle refuses
#     on operational grounds ("closed-loop information control"),
#     Tessa stays — does not walk away — says "All right. Then
#     I'll watch the room." The friendship is not broken. Noelle
#     is. What withdraws is Noelle's capacity to receive what
#     Tessa is offering.
# cann.thematic_flags:
#   - Structural inversion of A2_P14 "The Patient." Then Noelle
#     held the clamp; now Tessa does. Then Tessa cracked Noelle's
#     framework with the word *care*; now the framework is being
#     cut open and the cutting is also the holding. The two-shot
#     is the geometry of being held.
#   - "It does not have to. Hold still." — the load-bearing
#     exchange. Five words, two clauses, both layers active. The
#     medical answer (the data does not have to separate cleanly)
#     and the relational answer (grief does not have to come
#     labeled). Tessa has not deployed the can-you-still-feel-this
#     register lightly in a year. She deploys it here.
#   - The implant out is the first physical artifact of Noelle's
#     editing being undone. The leash cut. The sub-aural
#     transmission absence registers somatically. The quarter-inch
#     shoulder drop is the body's confession that it had been
#     holding the leash without naming the holding.
#   - "All right" as a word with shape. Noelle let "all right"
#     stand uncorrected for the first time in the coda. Here she
#     receives the question "Are you all right?" and answers
#     "No" — the not-correcting now includes admitting the word's
#     opposite. The shape of the word is what she is learning.
#   - Tea-as-overdue-anchor. The structural follow-up to A2_P14
#     is set for tomorrow. The interval — year and four months —
#     is named as overdue. The friendship had run on the
#     assumption that the follow-up could wait. The procedure
#     proves it could not. The tea is now scheduled.
#   - Tessa as the first audience for Halen. Tessa learning Halen's
#     name before any other rebellion character is canonical. The
#     Tessa-Noelle relationship now carries information neither
#     Aeron nor Selene nor Lyra has. The information is not a
#     secret in the operational sense; it is a private layer that
#     belongs to the friendship.
# cann.character_moments:
#   - Tessa: hands as the scene's first subject. The wash, the
#     scalpel pause, the suture work, the contact on Noelle's
#     hand. Hands carry the whole scene.
#   - Tessa: "Are you all right?" — the question she has not
#     asked Noelle in a year and four months. Asks it once. Hears
#     the answer once. Accepts it.
#   - Tessa: "We have not had tea since the Patient. We are
#     overdue." Names the friendship's structural debt aloud for
#     the first time.
#   - Tessa: stands at the table for a count of nine after Noelle
#     leaves. Unknowingly mirrors Noelle's count from the coda.
#   - Noelle: "No. Take it out." Two words. The fastest decision
#     Noelle makes in any Act IV scene.
#   - Noelle: voice cracks at "did not explain." The crack stays
#     open. The not-patching is what allows the rest of the
#     conversation to land.
#   - Noelle: "Thank you" without elaborating at scene close.
#     Tessa's response: "Go sleep, Noelle." Both characters
#     uphold the post-procedure quiet.
# cann.callbacks:
#   - a2_s18 (A2_P14 "The Patient"): direct structural twin. The
#     scene names the year-and-four-months interval and the
#     tea-overdue distance. The scalpel pause echoes Tessa's pen
#     pause from the board. The role inversion is the spine of
#     the scene.
#   - a4_s09a_noelle_coda_emp: nine hours prior. The four
#     discoveries land here in spoken form for the first time.
#     The "All right" that Noelle let stand in the coda returns
#     in Tessa's question and Noelle's answer.
#   - a4_s09_noelle_implicated_emp: the framework signature with
#     NOELLE VANCE on the pad. Aeron's reading of the surname is
#     referenced explicitly here as the most recent instance of
#     the Vance residue.
#   - a3_int_02_noelle_unmeasurable_emp: Tessa's awake-surgery
#     technique is the second instance of an unmeasurable
#     phenomenon directly affecting Noelle's processing. The
#     register-as-conversation is the technique's mechanism.
#   - canon_notes_noelle.md sec 3 (The Implant): the implant
#     mechanics canonized there are deployed in scene. Aether
#     Tag, Researcher-Class, "the leash," sector-level location,
#     resonance signature, Band coupling, no audio.
#   - canon_notes_noelle.md sec 11.3 (Tessa-Noelle Anchor): the
#     EMP version is delivered per spec. The Halen disclosure
#     during the procedure, the load-bearing exchange, the tea
#     appointment.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. EMP path only. The
#     Tessa-Noelle anchor follow-up to A2_P14, the implant
#     removal, the first audience for Halen. Foundational for
#     every subsequent EMP scene where (a) Tessa carries the
#     Halen information privately, (b) Noelle is referenced as
#     post-implant or as having grieved Halen, (c) the
#     friendship operates on the year-and-four-months tea
#     debt being repaid.
# cann.requires_followup:
#   - The tomorrow tea appointment at 08:00 the next day. The
#     scene of the tea is unwritten. Foundational for the
#     friendship's repaired register. Author at discretion.
#   - The implant evidence bag is in the medbay prep tray. Selene
#     will be briefed at some interval. The Selene briefing is
#     unwritten and may not require a scene of its own — author
#     judgment on whether the briefing is foregrounded or
#     referenced in passing.
#   - The Halen information is now Tessa's to hold. Tessa has not
#     told anyone. Future scenes should respect that Tessa knows
#     about Halen and may reference the knowledge implicitly.
#   - Noelle's medical leave is until 17:30. Any scene placed in
#     the 09:00-17:30 window on 29 Forge should treat Noelle as
#     absent (asleep in quarters).
#   - The shoulder-drop quarter-inch is the body's first registered
#     post-leash effect. Future scenes may track the body's
#     post-leash state across days — Noelle's posture, sleep
#     quality, headache reports — as canon-relevant indicators
#     of the leash's nine-year compression.
# =========================================================
