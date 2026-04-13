# =======================================================
# ACT 4 - Scene 08: Echelon Interlude IV (Obedience Path)
# File: a4_s08_echelon_interlude_4_ob.rpy
# Path: OB
# Type: ECHELON INTERLUDE (E_INT_204 -- OB variant)
# Character Focus: Marcus Rylan, Commander Rhea Vestin
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s08_echelon_interlude_4_ob"
$ scene_mark(_current_scene_id, "entered")

# Local speaker definition for Commander Rhea Vestin.
# First OB appearance. Cold, professional, does not flinch.
define rhe = Character("Commander Rhea Vestin", color="#8a95a4")

label a4_s08_echelon_interlude_4_ob:
    $ show_timeline_echelon("E_INT_204", "Aeries Command Spire")

    # Codex — Rhea's first named mention on the OB path.
    $ codex_mention("rhea_vestin", source="a4_s08_echelon_interlude_4_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. The Aeries spire at the high floor. Opens on the
    #         glass wall of the strategic overlook -- the city below at grey-dusk.
    #         Marcus standing, not seated. He does not sit for this interlude.
    #         Coverage: wide establishing, then a single on Marcus at the glass,
    #         then a two-shot when Rhea enters the spire -- symmetrical, flat, the
    #         two of them at equal height in the frame. After Rhea leaves, a return
    #         to the single on Marcus. The final beat is the empty chair reverse --
    #         the empty chair across the spire's reading alcove from Marcus, the
    #         chair that has been empty since Aeron left the Glass Academy.
    # LIGHTING: Aeries dusk. The sky outside is bleaching out of the glass. Cold
    #           institutional overheads at 60%. The spire's reading alcove has a
    #           single low lamp on the table beside the empty chair -- Marcus keeps
    #           it on. The lamp is warmer than anything else in the frame. It lights
    #           the chair, not Marcus.
    # SFX: Loop -- spire hum (the deep harmonic of a structure designed to last
    #      centuries), wind against the outer glass, the Aeries internal vent
    #      running at archival humidity. One-shots -- Rhea's boots on the stone
    #      (precise, unhurried), the folio Marcus sets down (quiet), the spire
    #      door sliding open and closed (once, twice).
    # FX/COMP: Marcus holds a folio. Not a datapad. Paper. The folio contains the
    #          last three days of Phoenix operational intercept summaries -- the
    #          shape of Nyra's seven-day plan, compressed into an Echelon reading.
    #          The folio has been annotated. Marcus's hand.
    # BLOCKING: Phase 1 -- Marcus alone at the glass. Phase 2 -- Rhea enters,
    #           stands three paces from him, does not cross into his sightline
    #           at the glass. Phase 3 -- Marcus turns, hands Rhea the folio,
    #           gives her the shortened window. Phase 4 -- Rhea leaves. Phase 5 --
    #           Marcus alone with the empty chair.
    # CANON: OB variant of the Act 4 Echelon interlude. The EMP variant (if/when
    #        it exists) has Marcus musing that his son is "building something I
    #        cannot understand." THIS variant has Marcus muttering the opposite.
    #        The scene is Marcus's disappointment. Not his anger. His disappointment.
    # FACE: Marcus -- still. A stillness that has been earned across forty years of
    #        command. The face is not softer than in prior interludes. The face is
    #        tireder. Not exhausted -- tired in the specific way a craftsman is
    #        tired when he sees his apprentice copy his worst habit instead of his
    #        best. Rhea -- expressionless by discipline, not by vacancy. She is
    #        professional in the sense that word had before it was cheapened.

    # ========= VOICE BASELINE =========
    # Marcus: Fewer words than the EMP variant would permit. In EMP he philosophizes.
    #         In OB he efficiencies. The disappointment lives in compression.
    # Rhea: First OB appearance. Cold. Clean. Not hostile -- unbothered. She
    #        treats Marcus the way a surgeon treats the chief of medicine: with
    #        structural respect and zero deference beyond structure.

    # --- VISUAL SETUP ---
    # [INT. AERIES SPIRE -- STRATEGIC OVERLOOK -- DUSK]
    # The high floor. The window wall. Solveil's grey city bleaching into night.

    #scene bg_aeries_spire_dusk with dissolve
    #play ambient "sfx/ambient/aeries_spire_hum.ogg" fadein 2.5

    # ========== PHASE 1 -- MARCUS AT THE GLASS ==========

    "The Aeries spire. The high floor. The hour when the capital's light thins through the outer glass and does not yet surrender to the inner lights."

    "Marcus Rylan stands at the window wall. Hands clasped behind him at the small of his back. The folio tucked under his left arm. His weight is on both feet. The weight has been on both feet for the last eleven minutes."

    "The spire is quiet. It has been quiet for the last eleven minutes, too. Marcus does not require a room to be loud to think in it. The spire is quiet because the people who work in it have learned that the spire is quiet when Marcus is reading."

    "The folio under his arm is paper. Not a datapad. Paper is a choice."

    # --- MARCUS INTERIOR ---

    mthought "Three days."

    mthought "Three days and the shape of his operational plan has moved through four sectors, one supply corridor, and a Ghostline relay shift I had budgeted a week to cover."

    mthought "The Sector 9 entry has been delayed by two days from a plan that would have worked on the original schedule. The delay is not a flinch. The delay is the correct delay. Someone in that room understood that Echelon's rebuild cycle is approximately seventy-two hours from the Sector 4 aftermath and that entering on the third day collides with the picket rotation."

    mthought "Nyra Kaelin understood it."

    mthought "My son understood it."

    mthought "My son corrected it."

    "Marcus allows a small exhale through the nose. Not a sigh. A breath that was required and has now been taken."

    mthought "Three weeks ago I told the Director's council that Aeron was the element of this campaign I could not predict. Three weeks ago that sentence was an assessment of his unpredictability."

    mthought "Today the sentence is a sentence I would have to revise if the Director's council asked me again."

    mthought "I could predict the day-five move. I could predict the one-stroke correction on the day-three entry. I could predict the civilian inclusion on the Sector 12 target list tomorrow morning before it has been signed."

    mthought "I could predict all of it because I taught all of it."

    # --- THE LINE ---

    "He speaks the line to the glass, quietly. The glass does not answer. It never has."

    m "He is building something I understand very well."

    "The sentence lands against the window. The window absorbs it the way it has absorbed forty years of Marcus's sentences."

    mthought "I expected him to surprise me."

    mthought "That is the complaint. That is the specific shape of the disappointment. It is not that he has become violent -- he was always going to be violent. Violence is not the variable. The variable was whether he would find a new door for the violence or whether he would find mine."

    mthought "He has found mine."

    mthought "The door is the same door. The hinge is the same hinge. The threshold has his boot-print on it now instead of mine, but the threshold is the threshold I built."

    mthought "I am disappointed."

    mthought "Not angry. Anger would be the wrong instrument. Anger would imply he had a choice and chose against me. He had a choice. He chose me. That is not something to be angry at. That is something to be disappointed by."

    mthought "I expected better."

    mthought "The phrase 'I expected better' is the one I have never said to him in forty years of speaking to him. I said variants. I said 'that was acceptable.' I said 'that was adequate.' I said 'that will serve.' I said 'that was efficient.'"

    mthought "I never once said 'I expected better.'"

    mthought "I am saying it now, to the glass, because the glass is the only witness the sentence deserves."

    m "I expected better."

    "The glass holds the sentence and does not give it back."

    $ tp_seed("a4.ob.marcus.disappointed")

    # ========== PHASE 2 -- THE FOLIO ==========

    "Marcus turns from the glass."

    "He walks the six paces to the reading alcove. The reading alcove is the interior chamber of the spire -- two chairs across from each other, a low table between them, a single warm lamp. The two chairs are not identical. One is Marcus's chair, austere, straight-backed, the leather worn into the shape of his spine. The other is a reading chair with a cushion, the cushion flattened by years of specific use -- the chair Aeron used for his cadet studies when the Director permitted him the spire as a private study, the chair he has not sat in since he left the Glass Academy."

    "The warm lamp on the table lights the empty chair, not Marcus."

    "Marcus does not sit in his own chair. He places the folio on the low table. Then he walks back to the window wall. He will speak to Rhea there, not at the reading alcove. The reading alcove is not for the operational briefing. The reading alcove is for the thing he is not yet saying."

    # --- THE SPIRE DOOR ---

    #play sound "sfx/spire_door_slide.ogg"

    "The spire door slides open."

    "Rhea Vestin enters."

    # ========== PHASE 3 -- RHEA VESTIN ==========

    # CAMERA: two-shot. Symmetrical. Equal height. The Aeries frames them as peers.

    #show rhea spire_entrance with dissolve

    "She is taller than the intercept profile suggested. The profile photographs did not render her posture correctly -- or did not render the specific way she holds her shoulders, which is the posture of a woman who has never negotiated her presence in a room."

    "Her uniform is Echelon line command: slate grey, one shoulder cord, the small hawk at the collar. The uniform is pressed the way a uniform is pressed when the wearer does not trust a subordinate to press it. She trusts herself."

    "She walks three paces into the spire. Stops. Her boots set down with the precision of a woman who has learned on cold stone. She does not salute."

    "She does not salute Marcus in the spire. The spire is his private study. Protocol outside the spire is formal. Protocol inside the spire is the specific absence of formality that the Aeries reserves for its senior command."

    "She waits for him to speak first. The waiting is not submissive. The waiting is the courtesy."

    m "Commander Vestin."

    "He does not call her Rhea."

    "The spire permits first names. He does not use the permission."

    rhe "General."

    "One word. Same courtesy."

    # --- THE ASSESSMENT ---

    mthought "She is thirty-one. She has been in Echelon line command for six years -- three of those as a captain on the northern front, three as commander of the Fourteenth Exigency. She has seven confirmed engagements. None of them have lasted more than ninety minutes."

    mthought "She does not like engagements that last more than ninety minutes. The preference is not squeamishness. The preference is that longer engagements are a sign of planning failure. She holds her planners to ninety."

    mthought "My son's engagement in Sector 12 tomorrow morning will last twenty-two minutes. I know this the way I know the day-five Sector 9 entry. I taught the tempo."

    mthought "She will recognize the tempo when she reads the intercept. She will not be surprised. She will be satisfied. Satisfaction is the emotion she uses most frequently, because it is the only emotion that does not require her to adjust her posture."

    # --- RHEA ---

    rthought "Marcus is at the window. He has been at the window for the eleven minutes I was waiting in the antechamber."

    # Note: rthought for Rhea's brief interior. Defined inline.
    # (We will not lean on rthought; Rhea is chiefly dialogue in this scene.)

    rhe "I do not require a briefing."

    "The sentence is flat. Not rude. Functional."

    rhe "I require the window."

    # ========== PHASE 4 -- THE WINDOW ==========

    "Marcus turns to her."

    "He looks at her for one beat. The beat is the beat of a commander reading a subordinate who has just declined a courtesy in a way that is not insubordinate but is also not negotiable."

    "He finds the decline efficient."

    m "You will have it."

    "Three words. The shape of a promise Marcus has given twice in his career."

    m "The Phoenix cell is accelerating its operational tempo. The seven-day plan they executed yesterday moves the Sector 9 entry to day five. The target profile for your engagement has changed."

    m "You will be engaging a force that is two days further along in its tempo than the original projection. The staging area you were planning to deny them has been partially consumed. They are running a Sector 12 preemptive operation at first light tomorrow against a forward post we had designated as your primary staging node."

    m "The forward post will not exist in twenty-two minutes from first light."

    rhe "Twenty-two minutes."

    m "That is the figure."

    rhe "His figure."

    "She does not phrase it as a question."

    m "Yes."

    "A pause. The spire hum. The glass."

    rhe "Civilian exposure."

    m "Three."

    rhe "On the target list."

    m "Yes."

    rhe "Pre-authorized."

    m "Yes."

    # --- RHEA DOES NOT FLINCH ---

    "Rhea does not flinch."

    "She does not flinch the way a person who has never flinched does not flinch. There is no cost to her not flinching, because she has not built a part of herself that flinches. The not-flinching is the baseline. Everything else is the exception."

    rhe "The profile change is legible. The target set is legible. I will not need to revise the approach vectors -- only the window."

    rhe "I had budgeted sixty hours for staging area denial. Sixty hours is no longer a useful figure."

    rhe "How long do I have."

    m "From first light tomorrow. Four days. Ninety-six hours. The Sector 9 entry on day five is the last point at which Phoenix's operational footprint is predictable. On day six the sequence becomes Nyra Kaelin's improvisation envelope and I will not be able to estimate their response geometry with sufficient confidence to brief you cleanly."

    rhe "Four days."

    m "Four days."

    rhe "I will have the window."

    # ========== PHASE 5 -- THE FOLIO EXCHANGE ==========

    "Marcus crosses to the reading alcove. Picks up the folio. Returns to the window wall. Extends the folio to Rhea."

    "Rhea takes it. Opens it in the standing position. Reads the first page for eleven seconds."

    "She does not sit."

    rhe "The annotations are yours."

    m "Yes."

    rhe "Not the analyst's."

    m "I prefer my own hand on documents I intend to act on."

    rhe "Good."

    "One word."

    rhe "I prefer that as well."

    # --- THE READ ---

    "Rhea reads the folio for a further three minutes in complete silence. Her eyes move across the pages at the intake speed of a woman who does not skim but also does not reread. She turns each page once. When she reaches the final page, she closes the folio."

    "She tucks it under her left arm. The same posture Marcus was using when she entered."

    rhe "I have a question."

    m "Ask."

    rhe "Is the commander of the Phoenix cell going to object to the civilian inclusion."

    "A beat."

    m "No."

    rhe "Internally."

    m "No."

    rhe "Visibly."

    m "No."

    rhe "Then the operation will complete as predicted."

    m "Yes."

    "Rhea nods once. Not to acknowledge the answer. To acknowledge that the answer confirms a prior expectation of her own."

    rhe "I will depart for the staging corridor at 0430. Four days from first light. I will have the forward post situation integrated into my approach by 0900 the day after tomorrow."

    rhe "I will not contact you again before the engagement window."

    m "Understood."

    rhe "General."

    "She turns."

    "She walks to the spire door. The door opens for her. She does not slow at the threshold."

    "The door closes."

    # ========== PHASE 6 -- MARCUS ALONE ==========

    "The spire is quiet again."

    "Marcus remains at the window wall for the count of ten. He has been in the habit, these last weeks, of counting to ten after an operational briefing before permitting himself the interior life the briefing interrupted. The count is a discipline. The discipline is one of his few."

    "He counts to ten."

    "He turns from the window. Walks the six paces back to the reading alcove."

    "This time he sits."

    "He sits in his own chair. Not the reading chair. He sits in the austere chair, the straight-backed one. The one his spine has worn into the shape of."

    "The reading chair across from him is empty."

    "The warm lamp on the table between the chairs lights the empty chair the way it always does."

    # ========== PHASE 7 -- THE EMPTY CHAIR ==========

    "Marcus places his hands flat on the low table. One hand on either side of the folio's absence -- the space where the folio was before he gave it to Rhea."

    "He looks at the empty chair."

    mthought "The last time you sat in that chair you were nineteen years old."

    mthought "It was a Tuesday. I know it was a Tuesday because the cadet examination cycle ran Monday to Thursday and you were finishing the Tuesday examination in the afternoon and you came to the spire to show me the score. You did not knock. You had never needed to knock."

    mthought "You sat in that chair with your cadet folio under your arm -- the same posture Rhea Vestin just used to tuck my folio under hers -- and you opened the folio on the low table and you showed me the numbers."

    mthought "The numbers were eighty-one percent. I remember the specific number because I remember being annoyed by it. Not because eighty-one was poor. Because eighty-one was below what you were capable of. You had gotten eighty-six on the previous cycle and the eighty-one was a regression."

    mthought "I said that was acceptable."

    mthought "I did not say I expected better."

    mthought "I did not say it because I thought you would hear the criticism more clearly if I made you find it in the word acceptable. I was wrong. You did not hear the criticism at all. You heard acceptable and you went back to your bunk and you wrote me a letter I still have in the cabinet behind my chair. The letter said -- and this is the exact sentence -- 'I will be better next cycle, sir.'"

    mthought "You were better next cycle. You scored an eighty-nine. I said that was efficient."

    mthought "I did not say it because I thought you would hear the approval more clearly if I understated it. I was wrong about that also. You heard efficient and you went back to your bunk and you wrote me no letter. You did not write me another letter for nine months."

    mthought "The letter I still have was the only one."

    mthought "The letter is in the cabinet behind my chair because I did not know what else to do with it. I have read it three times in twenty years. Once on the day of the Glass Surge when I was told you had survived the planning corridor. Once on the day you joined Phoenix. Once tonight, before Rhea Vestin arrived."

    "Marcus does not open the cabinet behind his chair."

    "He does not need to. The sentence he remembers is sufficient."

    # --- THE LINE ---

    "He speaks to the empty chair."

    "Quietly. The spire is quiet. There is no one to hear him."

    m "Come home the long way, son."

    "A pause."

    m "I can wait."

    # --- THE INTERIOR FOLLOW-THROUGH ---

    mthought "The long way is the way that does not resolve this week. The long way is the way that makes the eighty-nine into an eighty-one again, and the eighty-one into a letter, and the letter into a boy who wrote to his father because he wanted to be better."

    mthought "The short way is Sector 12 at first light. The short way is the one-stroke correction on the day-three entry. The short way is the structural diagram in the Phoenix war room with your name and Nyra Kaelin's name on the same bar, at the same width."

    mthought "The short way is efficient."

    mthought "I am old enough to prefer the long way."

    mthought "I am also old enough to know that telling you so would change nothing. I told you not to take the short way once already. I told you at Tessa Merin's parents' funeral when you were eleven years old and I said the violence of precision is a door you should not open until you have exhausted every other door. You said yes sir and you were lying the way a child lies -- not to deceive, to comply."

    mthought "You have exhausted the other doors. The eleven-year-old's lie is the thirty-two-year-old's doctrine."

    mthought "I can wait."

    mthought "That is the sentence I want in the room at the end of tonight. Not 'I am disappointed.' Disappointment is a complaint. A complaint cannot be spoken to an empty chair with any dignity."

    mthought "'I can wait' is a promise. A promise can be spoken to an empty chair. A promise IS what one speaks to an empty chair, because the empty chair is the only audience that cannot refuse the promise by answering it wrong."

    mthought "I can wait for you to come home the long way."

    mthought "I am aware you will not come home at all."

    mthought "The waiting is the love I am capable of. I do not have a better one. I have never had a better one. The letter in the cabinet behind my chair was your request for a better one, and I did not give it to you, and the not-giving is the shape of this war."

    # ========== PHASE 8 -- THE LAMP ==========

    "Marcus does not turn off the lamp."

    "The lamp stays on. The lamp has been on every night for twenty years. The lamp will be on tomorrow night and the night after. The lamp will be on when Rhea Vestin engages the Phoenix cell and the lamp will be on when Rhea Vestin reports whether she was successful."

    "The lamp is a discipline. The discipline is one of his few."

    "He stands."

    "He walks back to the window wall. He resumes the posture he was in when the scene began -- hands clasped at the small of his back, weight on both feet, facing the glass."

    "The capital below the spire is fully dark now. The inner lights of the Aeries are reflected against the outer glass, superimposed on the grey-dark of the city."

    "Marcus looks at his own reflection in the glass. The reflection is an older man than he feels tonight. He has not felt this specific age before."

    # --- FINAL INTERIOR ---

    mthought "Tomorrow Sector 12 falls in twenty-two minutes. Three civilians are on the list. My son will sign the list."

    mthought "Four days after that Rhea Vestin enters the engagement window."

    mthought "Six days after that the long way becomes the short way and the short way was always the only way and the lamp is still on behind me and the chair is still empty."

    mthought "Come home the long way, son."

    mthought "I can wait."

    # --- CALLBACK TO EMP ---

    mthought "In another version of this room I would be saying I do not understand what you are building."

    mthought "I am not in that version of this room."

    mthought "I understand what you are building very well."

    mthought "That is the disappointment."

    # ========== PHASE 9 -- SPIRE COdA ==========

    "The spire hum. The wind on the outer glass. The warmth of the lamp behind Marcus on the low table beside the empty reading chair."

    "Marcus does not speak again."

    "He stands at the window for a further nineteen minutes. When he finally turns from the window, he does not look at the empty chair. He walks to the spire door. The door opens for him. He steps through."

    "The lamp stays on."

    "The chair stays empty."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.marcus.disappointed", True)
    $ canon_set("ob.rhea_vestin.window_authorized", True)
    $ canon_set("ob.rhea_vestin.first_appearance", "aeries_spire_dusk")
    $ canon_set("ob.marcus.long_way_home_line", True)
    $ flag("a4_ob_echelon_interlude_4", True)
    $ npc_remember("Marcus", "i_expected_better_spoken_to_glass", tone="disappointment_not_anger")
    $ npc_remember("Marcus", "letter_in_the_cabinet", tone="one_letter_never_answered_well")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s08_echelon_interlude_4_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Dusk of the same day as a4_s01 through a4_s07. The evening before the
#     Sector 12 preemptive operation (a4_s09). Marcus is reviewing the last
#     three days of Phoenix operational intercepts in the Aeries spire.
#   - Rhea Vestin arrives for her final pre-engagement briefing. She has four
#     days until her staging window collapses against the day-five Sector 9
#     entry in the Phoenix plan.
# cann.what_happened:
#   - Marcus alone at the spire window. Speaks "I expected better" to the glass.
#   - Rhea Vestin enters. First OB appearance. Refuses the standard briefing
#     courtesy: "I do not require a briefing. I require the window." Marcus:
#     "You will have it."
#   - Marcus briefs her on the accelerated tempo: Sector 12 preemptive at first
#     light (22 minutes, 3 civilians on the target list, pre-authorized).
#     Rhea does not flinch. The not-flinching is the baseline.
#   - Marcus hands her the paper folio with his own annotations (not the
#     analyst's). She reads it standing. Asks one question: "Is the commander
#     of the Phoenix cell going to object to the civilian inclusion." Marcus:
#     "No. Internally: no. Visibly: no. Then the operation will complete as
#     predicted."
#   - Rhea leaves. Marcus returns to the reading alcove. Sits in his own chair.
#     Looks at the empty reading chair Aeron last sat in at nineteen.
#   - The memory: the eighty-one percent cadet exam score. The letter in the
#     cabinet behind Marcus's chair. "I will be better next cycle, sir." The
#     only letter Aeron ever wrote him.
#   - Marcus speaks to the empty chair: "Come home the long way, son. I can
#     wait." Interior follow-through: the waiting is the love he is capable of.
#     He is aware Aeron will not come home at all.
#   - OB counterpart to the EMP variant's "building something I cannot
#     understand." Here: "He is building something I understand very well."
#     The disappointment is that Aeron chose the familiar door.
# cann.marcus_state:
#   - Disappointed. Not angry. The disappointment is specific: Aeron was the
#     variable Marcus could not predict, and he has become predictable. The
#     variable was whether he would find a new door for the violence or find
#     the one Marcus built. He has found the one Marcus built.
#   - The lamp on the table beside the empty chair has been on every night
#     for twenty years. It stays on tonight.
# cann.rhea_vestin_voice:
#   - First OB impression. Cold, precise, unbothered. Does not flinch at
#     civilian inclusion because the not-flinching is the baseline, not an
#     exception. Thirty-one years old, Fourteenth Exigency, seven confirmed
#     engagements. Dislikes engagements longer than ninety minutes (a
#     planning-failure indicator, per her doctrine).
#   - "I do not require a briefing. I require the window."
#   - Will engage four days after the scene.
# cann.thematic_flags:
#   - OB VARIANT OF E_INT_204. The EMP variant (per route brief) has Marcus
#     musing that Aeron is "building something I cannot understand." The OB
#     variant inverts the line: "He is building something I understand very
#     well." The inversion IS the thesis.
#   - DISAPPOINTMENT, NOT ANGER. The specific tired-craftsman flavor of a
#     father watching his apprentice copy the worst habit instead of the best.
#   - THE EMPTY CHAIR. The reading chair in the Aeries spire where Aeron last
#     sat at nineteen. Cadet exam folio. Eighty-one percent. The letter.
#   - "I CAN WAIT." Marcus's promise to the chair. The waiting is the love
#     he is capable of. He is aware Aeron will not come home at all.
# cann.character_moments:
#   - Marcus: "I expected better" spoken to the glass for the first time in
#     forty years of speaking to Aeron. The letter in the cabinet behind his
#     chair (a piece of backstory planted here that may surface later).
#   - Rhea Vestin: first OB appearance. Clean, professional, zero flinch.
# cann.callbacks:
#   - a4_s01_the_cold_room_ob: the one-stroke correction Marcus has now read
#     in the intercept. He taught the mark.
#   - a4_s02_the_new_shape_ob: the structural diagram -- Marcus has read it
#     in the intercept as well.
#   - a4_s03: the preemptive strike authorization. Rhea has been notified.
#   - Marcus's Act 2 / Act 3 Echelon interludes: his doctrine of precision
#     violence is now his son's doctrine of precision violence.
# cann.block_status:
#   - ANCHOR (OB path). Always plays. No branching. No player choice.
#     Interlude function -- shifts POV away from Phoenix for ~90 seconds to
#     provide external-scale pressure before the Sector 12 operation.
# cann.requires_followup:
#   - a4_s09_sector_12_sweep_ob: the operation Marcus has just described to
#     Rhea.
#   - Rhea Vestin's engagement window opens four days later (late Act 4 / Act 5).
#   - The letter in the cabinet behind Marcus's chair is a plant for a
#     potential Act 5 or Act 6 payoff.
