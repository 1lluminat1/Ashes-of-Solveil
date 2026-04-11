# =======================================================
# ACT 4 - Scene 10: The Doctrine (Obedience Path)
# File: a4_s10_noelle_doctrine_ob.rpy
# Path: OB
# Type: NOELLE STATE BEAT / ARC -- DOCTRINE DRAFTING
# Character Focus: Noelle, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s10_noelle_doctrine_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s10_noelle_doctrine_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Data alcove, cold register. Opens on the
    #         alcove door from the corridor side -- closed, status indicator
    #         grey (engaged-but-not-locked). The camera enters with Aeron, not
    #         with the audience. The first shot of Noelle in the scene is a
    #         medium single from behind her own shoulder -- we see what she is
    #         seeing on the primary screen before we see her face. Her face is
    #         a reverse at second-and-a-half. Coverage after that is symmetrical
    #         two-shot across the data alcove and singles during the signature
    #         beat. The alcove is quieter than a3_s16 -- the crystal arrays are
    #         at standby, one screen lit. The room has been stripped down for
    #         writing, not analysis.
    # LIGHTING: Data alcove at drafting setting. The primary screen at 80%
    #           luminance. The secondary screens dark. The amber lamp from
    #           a3_s16 is present but still unplugged -- Noelle has not used
    #           it in weeks. The dominant light source is the primary screen
    #           and a single cold overhead strip. Noelle's face is lit by the
    #           screen, blue-white. Aeron's face, when he enters, lit by the
    #           same screen and by a hard corridor light that spills in when
    #           the door opens.
    # SFX: Loop -- data alcove ambient at drafting setting. The crystal arrays
    #      at standby hum is half what it was in a3_s16. The vent is quieter.
    #      The room sounds smaller than it did in Act 3. One-shots -- door
    #      open (measured), Aeron's boots on the alcove floor (three steps),
    #      the chair Noelle offers him that he does not take, the stylus
    #      Noelle is holding when the scene opens (resting on the table),
    #      the stylus Aeron takes up to sign (one stroke, OB-register, the
    #      signature that does not yet have a document to sign).
    # FX/COMP: Noelle's primary screen shows a document in progress. The
    #          document is titled at the top: "ON THE STRUCTURAL ADMISSIBILITY
    #          OF NON-COMBATANT TARGET CATEGORIES." Beneath the title, a
    #          section header: "I. Preliminary Definitions." The document has
    #          been written to the end of Section I. Section II is a header
    #          with no body: "II. The Collaborator Threshold."
    #          The private whiteboard from a4_s09 (seven names) is on a
    #          secondary screen to the left -- dimmed but still visible.
    #          The board is the doctrine's shadow evidence.
    # BLOCKING: Noelle seated at her workstation, facing the primary screen.
    #           The two chairs from a3_s16 are still in the alcove -- she has
    #           not removed them -- but the supply crate beside her chair is
    #           gone. In its place is a second workstation chair, angled
    #           toward the primary screen from the side. She is writing for
    #           herself, but she has left a chair in the position where
    #           someone could read with her.
    #           Aeron enters. Stands at the threshold for two seconds. Walks
    #           three paces into the alcove. Stops beside the screen at
    #           reading distance. Does not sit. Reads the document from the
    #           standing position.
    # CANON: Day after Sector 12 (a4_s09). Noelle is drafting a formal
    #        doctrine rationalizing the civilian targeting framework. She
    #        has not been asked to write it. She is writing it because she
    #        needs her categories to catch up with her actions. Aeron reads
    #        the first page, signs a blank authorization line, trusts that
    #        whatever she builds will be what he needs. The gut punch is the
    #        blank signature.
    # FACE: Noelle -- writing composure. The face of a woman who has found
    #        the posture for a thing she did not have a posture for yesterday.
    #        Aeron -- the institutional face from s02 and s09. Plus one
    #        additional layer: the specific stillness of a man reading a
    #        document that was not written for him but will nonetheless
    #        become his.

    # ========= VOICE BASELINE =========
    # Noelle: Full analytical register. The erotic Name Mechanic from a3_s16
    #          is not deployed here -- the register is cold, ceremonial. She
    #          uses his title, not his name. The absence of the Name Mechanic
    #          is one of the scene's quieter griefs.
    # OB Aeron: Minimal. Three or four spoken lines. The signature is the
    #           scene. The signature is the scene and Noelle knows it before
    #           he does.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE -- DATA ALCOVE -- 0923]
    # Twenty-one hours after Sector 12 closed out. The base has run its
    # overnight shift. Noelle has not slept.

    #scene bg_data_alcove_drafting with dissolve
    #play ambient "sfx/ambient/data_alcove_drafting.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DOCUMENT ==========

    "The data alcove door is closed. The status indicator is grey -- engaged, not locked. The alcove is a room Noelle does not lock anymore. The distinction between a locked alcove and an unlocked alcove became operationally meaningless three weeks ago."

    "Inside the alcove, Noelle is at her primary workstation."

    "The primary screen shows a document in progress. The title at the top of the document reads, in the plain institutional font she uses for all her analytical papers:"

    "ON THE STRUCTURAL ADMISSIBILITY OF NON-COMBATANT TARGET CATEGORIES"

    "Beneath the title, the section header:"

    "I. Preliminary Definitions"

    "Section I has been written to the end. It is three pages long. It defines the terms 'combatant,' 'non-combatant,' 'collaborator,' and 'active conduit' with the specific careful non-overlap of a woman who has spent her career refusing to let her terms do more work than they should do."

    "Beneath Section I, a header with no body:"

    "II. The Collaborator Threshold"

    "The header is bold. The cursor is blinking beneath it."

    "Noelle has been staring at the cursor for eleven minutes."

    # --- NOELLE'S INTERIOR ---

    nthought "I am going to write the collaborator threshold section in one pass and I am going to write it cleanly and I am going to not pause at any point during the writing."

    nthought "The one-pass rule is the rule I am using for this document because the one-pass rule is what I was trained to use for first drafts of analytical papers. Single pass. No interruptions. Edit later. The edit pass is where the doubts are permitted. The draft pass does not accept doubt."

    nthought "I am setting up the one-pass rule because I can feel the doubts."

    nthought "The doubts are not about whether I can write the section. The doubts are about whether I should be the one writing it. The doubts are also about whether the section should exist. The doubts are also about whether the document should exist. The doubts are also about whether I should be in this alcove this morning writing it at all."

    nthought "The one-pass rule is the instrument I use to prevent the doubts from becoming arguments. Arguments are the thing the one-pass rule does not permit."

    nthought "I am going to write the section now."

    nthought "I am not writing it."

    nthought "I have been staring at the cursor for eleven minutes."

    nthought "Twelve minutes."

    # --- THE FIRST SENTENCE ---

    "Noelle lifts her hands to the keyboard. The motion is smooth. Her fingers do not hesitate on the keys. She types the first sentence of Section II."

    "The sentence appears on the screen."

    "She reads it."

    "She does not delete it."

    "She types the second sentence."

    "The second sentence is also admitted."

    "By the fifth sentence she has stopped reading each one as she writes it. She is writing at the drafting speed she uses for her strongest work. The keys are making the clean low sound they make when she is in the register she thinks of, privately, as the register. The register is not a register she speaks about. She noticed the register the first time when she was twenty-two and writing her Academy dissertation on doctrinal economies. The register is her."

    "She is the register."

    "The register is writing a doctrine on the structural admissibility of non-combatant target categories, and the register does not care what it is writing about. The register cares about the sentence. The register has always cared about the sentence."

    # ========== PHASE 2 -- THE SHADOW EVIDENCE ==========

    "On the secondary screen to Noelle's left -- dimmed to a quarter-luminance so the primary screen can have her eyes -- the private whiteboard from a4_s09 is visible."

    "Seven names. Seven small text entries in the TERTIARY-CONFIRMED column. The three from Sector 12 at the top, the four earlier ones beneath them. Each entry has a date, a timestamp, and a classification tier."

    "The whiteboard is the doctrine's shadow evidence."

    "Noelle has the whiteboard open beside the doctrine for a specific reason: the doctrine is the structural frame and the whiteboard is the empirical record and she needs the frame to match the record. The frame cannot be a frame that the record does not fit."

    "She glances at the whiteboard once every thirty seconds or so. The glance is not a check. The glance is a reassurance. The whiteboard is still there. The seven names are still there. The doctrine is still describing something that has happened, not something that might happen."

    nthought "If I wrote this yesterday it would be a thought experiment. If I write it today it is a post-hoc rationalization."

    nthought "Post-hoc is the correct register."

    nthought "Post-hoc is the register of someone who has noticed that the actions have outrun the categories and is now writing new categories that fit the actions."

    nthought "The alternative is to write new actions that fit the old categories. That alternative is not on the table. That alternative was not on the table on Tuesday when I rewrote the schema. That alternative was not on the table yesterday when I watched him read the list for eighteen seconds and sign it in the nineteenth."

    nthought "That alternative has not been on the table since Selene died. Since Aeron killed Selene. Since I did not object in the meeting the next morning."

    nthought "I am writing the doctrine because I need the categories to catch up."

    nthought "I am writing the doctrine because my Act 3 lie was that if I could model this I could remain separate from it."

    nthought "I am writing the doctrine because the Act 3 lie is not operating anymore."

    nthought "The doctrine is the replacement lie."

    nthought "The replacement lie is: if I can name what I am doing, I am still an analyst. I have merely expanded what the analyst can do."

    nthought "I notice I am typing this thought into the Section II draft."

    nthought "I delete it."

    nthought "The delete is the rule. The one-pass rule. The doubts are not in the draft."

    "She deletes the sentence. Seventeen characters. The delete is the only delete she performs in the first three hundred words of Section II."

    "The register resumes."

    # ========== PHASE 3 -- THE DOOR ==========

    # CAMERA: wide on the alcove. The door in the corner of the frame.

    "The alcove door indicator shifts from grey to green-arrival."

    "Noelle does not turn."

    "The indicator goes green when someone in the approved-access roster approaches within two meters of the door. The approved-access roster for the data alcove contains Aeron, Nyra, and the senior analyst on duty. The senior analyst on duty is Noelle. The only two people who can produce the green-arrival indicator from outside are Aeron and Nyra."

    "Nyra is in the operations room at this hour. The ops schedule is in Noelle's peripheral awareness at all times."

    "It is Aeron."

    #play sound "sfx/alcove_door_measured.ogg"

    "The door slides open."

    "The corridor light spills into the alcove -- a hard, grey spill, brighter than the drafting setting. Noelle's peripheral registers the intensity shift and does not turn."

    "Three footsteps into the alcove."

    "Aeron stops. Beside her workstation chair, at reading distance from the primary screen."

    "He does not greet her."

    "He does not sit in the workstation chair she has left angled for a reader."

    "He reads the document."

    # ========== PHASE 4 -- AERON READS PAGE ONE ==========

    # CAMERA: reverse. Noelle's face lit by the screen. Aeron's face, behind her
    # right shoulder, lit by the same screen and by the corridor spill.

    "Aeron reads the title of the document first."

    "ON THE STRUCTURAL ADMISSIBILITY OF NON-COMBATANT TARGET CATEGORIES"

    "He does not react visibly to the title. His face does the institutional thing."

    "He reads the Section I header. He reads the first paragraph of Section I. He reads the second paragraph. He reads the third paragraph. He is a fast reader on operational documents and this is not an operational document but it is written in a register he knows."

    "He reads the entire Section I in a standing read of approximately seventy seconds."

    "Noelle does not stop typing Section II while he reads. The register is still engaged. Her fingers are still producing sentences at the drafting speed. The sentences on the primary screen are moving down the page under the Collaborator Threshold header while Aeron reads above them."

    "The alcove is quiet except for the low keystroke sound and the vent and the standby hum of the crystal arrays."

    "Aeron finishes reading Section I."

    "He looks at her."

    # --- THE FIRST LINE ---

    a "You are drafting the rules for a thing I have not asked you to defend."

    "The sentence is not a question."

    "It is a flat observation. The register is his ops-room register, but the content is a personal observation, and the combination produces a sentence that is cold and specific and lands in the alcove with the particular weight of a sentence that has diagnosed something correctly without having softened the diagnosis."

    "Noelle does not stop typing."

    "She finishes the sentence she is on. She types the period. Then she lifts her hands from the keyboard and places them on the edge of the workstation, palms down, fingers spread, the way she places them when she is about to switch registers from drafting to dialogue."

    "She does not turn her chair to face him yet."

    "She answers while looking at the primary screen."

    n "You will ask eventually. I am preparing."

    "Six words."

    "They do not have the warmth the Name Mechanic in a3_s16 had. The Name Mechanic was the specific thing Noelle did when she was making intimacy out of precision. The Name Mechanic is not deployed here. The register is ceremonial. She uses the word Commander's implicit position, not his name."

    "She is preparing something for a commander she has not yet been asked to serve in this specific way."

    "That is what she has said."

    # --- AERON ON THE LINE ---

    athought "She is not wrong."

    athought "She is not wrong about the asking. I would have asked her within the week. The doctrine is the document the operational tempo requires within the week because Nyra's framing line in the ops room yesterday morning -- 'we no longer need to appear restrained' -- is a statement that does not survive the after-action audit from the next Ghostline intercept of our own procedures."

    athought "We need the paper. We need the paper because the paper is the thing that makes the framing line into a policy instead of a transgression."

    athought "Noelle is writing the paper."

    athought "She is writing the paper one day before I would have asked her to."

    athought "The one day is the specific margin of her anticipation. I am going to be accurate about what that margin is."

    athought "The margin is not efficiency. Efficiency would be the same day, the same hour, within fifteen minutes of the ask. The margin is a day. The day is the margin a person buys themselves when they need to be the author of a thing before they are the executor of it."

    athought "Noelle is buying herself authorship."

    athought "I understand authorship. Authorship is a kind of deflection. Authorship is what you do when you cannot not do the thing and you need the thing to have your name on it in a specific way that feels different from your name being on the doing."

    athought "She is writing the authorship because she is not able to do what I am able to do, which is be the one who signs the list without claiming the categories."

    athought "She is writing the categories."

    athought "I am going to let her."

    # ========== PHASE 5 -- NOELLE TURNS ==========

    "Noelle turns her chair."

    "The motion is slow. Not reluctant -- careful. She is arranging the angle of the chair so that she is facing him at a forty-degree angle rather than a direct front-on. The angle preserves her access to the primary screen. She can still see the cursor from her peripheral vision."

    "She looks at him for the first time in the scene."

    "Aeron is standing beside the workstation chair she left for a reader. He has not taken the chair. His left hand is flat against the primary screen's frame -- not the screen itself, the frame around it, the cold bezel. The hand is steady."

    n "Commander."

    "She uses the title."

    "She uses the title because the name would be the Name Mechanic and the Name Mechanic is the intimacy register and the intimacy register does not belong in a room where a doctrine on non-combatant target categories is being drafted. The title is the scene's register."

    n "The document is incomplete. Section I is the preliminary definitions. Section II is the collaborator threshold. I have written approximately three hundred words of Section II. Sections III through VII are unwritten."

    n "Section III is the operational geometry of collaborator targeting. Section IV is the doctrinal economies of visibility -- when and how the targeting is acknowledged in the operational record, and in which registers. Section V is the Ghostline pattern intercept framework. Section VI is the authorization protocols, which includes the signature pathways, the review cycles, the dissent clauses that are structurally present but functionally sealed."

    n "Section VII is the conclusion."

    n "I will finish Section VII last. The conclusion will summarize the doctrinal frame in approximately eight hundred words and will close with a single declarative sentence that I have not yet written. The sentence will not be decorative. The sentence will be the one sentence that, if read alone, communicates the entire document."

    "She pauses."

    n "I do not yet know what the sentence is."

    "She is giving him the shape of the document the way she would give him the shape of an operational analysis. The shape is precise. The shape is what she is giving him instead of the document itself, because the document itself does not exist yet."

    # --- THE REQUEST ---

    n "I am going to ask for your signature on the authorization line."

    a "When."

    n "Now."

    "One word."

    # --- AERON ---

    "Aeron's face does the institutional thing for one beat longer than it has been doing it. The beat is the beat in which he is registering the request and deciding whether he is going to ask the question that the request is inviting."

    "The question the request is inviting is: the document is unfinished. The authorization line is at the bottom of a document that is roughly fifteen percent written. How am I supposed to sign an authorization for something I cannot read."

    "He does not ask the question."

    "He does not ask the question because the question is the question Noelle is asking him to not ask. The entire scene is her asking him to not ask the question. The scene is her asking him to trust that whatever she builds will be what he needs."

    "He trusts her."

    "The trust is not warm. The trust is the specific cold trust of an institution for one of its instruments. The instrument has performed correctly to date. The instrument is predicting that it will perform correctly going forward. The institution has no reason to doubt the prediction."

    "That is what trust is, in this register."

    a "Give me the authorization line."

    "Five words."

    # ========== PHASE 6 -- THE BLANK SIGNATURE ==========

    # CAMERA: slow push-in on the primary screen. The cursor at the bottom of
    # the document. Noelle scrolls down past the unwritten sections.

    "Noelle turns back to the primary screen."

    "She scrolls down the document. The page indicator moves from page three to page four to -- and this is a page that is mostly white space -- to a page that is almost the bottom of the document but is not the bottom of the document because Sections III through VII do not yet exist."

    "She taps a key combination. The document generates a signature field at the current cursor position. The field is labeled COMMANDER RATIFICATION. The field has a timestamp placeholder and a signature placeholder and below both of them a small locked audit line that reads DOCUMENT VERSION 0.17 -- INCOMPLETE."

    "The field is in the middle of the document. It is not at the end. It is in the place Noelle has put it because the place she has put it is the place it needs to be in order for the signature to pre-authorize the sections that have not yet been written."

    "The signature, if signed now, is the authorization for whatever will appear above and below it. The position is deliberate."

    "Noelle sees the position. Noelle arranged the position."

    "She says nothing about the position."

    "She offers the stylus to Aeron."

    "Aeron takes the stylus."

    # --- AERON STANDING AT THE SCREEN ---

    "He does not sit."

    "He stands at the screen with the stylus in his right hand. His left hand remains flat on the bezel. His eyes read the signature field. He reads the label. He reads the timestamp placeholder. He reads the small locked audit line."

    "DOCUMENT VERSION 0.17 -- INCOMPLETE."

    "He reads the word INCOMPLETE for approximately two seconds."

    athought "I am about to sign a thing with INCOMPLETE written on it in the audit line. The audit line is not editable. The audit line will remain on every version of this document that descends from this signature. Every future version will carry, in its history, the record that I signed the zero-point-seventeen draft."

    athought "The record is the record."

    athought "The record is the record that says I trusted her to finish the document in the shape I needed it to be in, without reading the shape, because reading the shape would have been slower than trusting the shape."

    athought "The speed is the thing. Speed is what the doctrine is for. The doctrine is a document that accelerates decision-to-execution in the civilian inclusion space. I am signing the acceleration in the draft state because the draft state is the acceleration of the acceleration."

    athought "I notice I am describing this to myself in a register that makes it sound inevitable."

    athought "It is not inevitable."

    athought "I am going to do it anyway."

    # --- THE SIGNATURE ---

    "Aeron moves the stylus to the signature field."

    "He signs."

    #play sound "sfx/stylus_signature_single.ogg"

    "One stroke. A, slash, R. The OB-register signature. The same three marks from a4_s01, from a4_s02, from a4_s09. The signature is now a unit. The signature is the unit he uses for everything."

    "The signature field registers the signature."

    "The timestamp placeholder populates: 0941:17."

    "The audit line updates: DOCUMENT VERSION 0.17 -- AUTHORIZED -- INCOMPLETE."

    "The word INCOMPLETE is still there. The word AUTHORIZED has been added before it. The two words are not contradictions. The two words are the scene's actual subject."

    "Aeron sets the stylus down on the edge of the workstation."

    "He does not speak."

    # ========== PHASE 7 -- NOELLE WATCHES ==========

    "Noelle is watching the signature field."

    "She watched him sign. She watched the stroke. She watched the timestamp populate. She watched the audit line update to include the word AUTHORIZED beside the word INCOMPLETE."

    "She did not speak during the signing."

    "She speaks now."

    n "(quietly) This is how it happens."

    "Five words."

    "The words are not analytical. The words are not institutional. The words are not the register Noelle has been writing in for the last forty minutes. The words are the register underneath the register -- the thing Noelle does not permit in drafts and does not permit in ops rooms and has not permitted in herself since she joined Phoenix."

    "The words are quiet enough that Aeron could pretend not to have heard them."

    "He does not pretend."

    a "I know."

    # --- THE BEAT AFTER ---

    # CAMERA: the two-shot holds. Neither of them moves.

    "The data alcove is quiet except for the vent and the crystal standby hum and the low keystroke sound of Noelle's fingers resting on the edge of the workstation, not typing."

    "Aeron's left hand is still on the screen bezel. The hand has not moved during the signing. The signing happened at arm's length from the hand on the bezel -- one arm stationary, one arm signing. The posture is not ceremonial. The posture is a man who needs the bezel to not move while he is moving."

    "Noelle is watching him at the forty-degree angle her chair is set to. She is not watching the screen. She is watching the left hand on the bezel."

    nthought "His hand has not tremored."

    nthought "I used to watch his left hand for the tremor. In the first weeks after the Glass Surge, the left hand would go flat against a cold surface when the mask was under pressure. The tremor was the tell."

    nthought "His left hand is on the bezel right now."

    nthought "The bezel is cold. The hand is flat. The hand is not tremoring."

    nthought "I am measuring the absence of the tremor because the absence is the thing I am writing the doctrine to catalogue."

    nthought "The doctrine is the name for the non-tremor."

    nthought "I did not know that was the name until right now, watching his hand on the bezel, after I said 'this is how it happens' and he said 'I know.'"

    nthought "The name for the non-tremor is: the thing he has become does not have a tremor. The thing he has become is the thing that signs a version 0.17 audit line without asking what Sections III through VII will contain. The thing he has become is a man whose trust in me is the trust of an institution for one of its instruments."

    nthought "I am the instrument."

    nthought "I am writing the doctrine that names the instrument."

    nthought "I am the instrument that is naming itself."

    nthought "I notice that the naming is the corruption. The Act 3 lie was 'if I can model this I can remain separate from it.' The Act 4 lie is 'if I can name what I am doing, I am still an analyst. I have merely expanded what the analyst can do.'"

    nthought "The expansion is the corruption."

    nthought "I do not stop writing."

    nthought "I do not stop writing because I am the register and the register is writing."

    tp_seed("a4.ob.noelle.this_is_how_it_happens")

    # ========== PHASE 8 -- AERON'S EXIT ==========

    "Aeron removes his left hand from the bezel."

    "The hand was on the bezel for approximately four minutes. The print on the cold screen frame will fade in under a minute. He does not look at the print. He does not look at the bezel."

    "He looks at Noelle once more."

    "The look is not warm. The look is the look of a commander who has just authorized a document he has not read, to an analyst he trusts to finish the document in a shape that will be what he needs. The look is the look he would have given Nyra under the same conditions. The look is the look he gave the target list datapad yesterday at 0541:08."

    "The look is undifferentiated. That is the cruelty of the look."

    a "Send me the final version when Section VII is done."

    n "I will. The closing sentence first. I will draft the closing sentence for your review before I set it in the document."

    a "No."

    n "No?"

    a "I trust the closing sentence."

    "Four words."

    "Noelle does not blink. She does not nod. She does not say thank you."

    "The trust has been extended one further turn than it needed to be extended, and the extension is the part she was not ready for."

    n "(quietly) Acknowledged."

    "The word acknowledged is the word she uses in ops rooms when she is closing a line item and does not have a further comment. The word has never been this heavy in her mouth before."

    # --- AERON WALKS TO THE DOOR ---

    "Aeron walks to the door."

    "Three paces. The same three paces he used to enter, in reverse. The door opens for him. He does not pause at the threshold. He steps through."

    "The door closes."

    "The corridor light is gone from the alcove. The drafting setting reasserts itself. The primary screen is the dominant light source again. The amber lamp on the secondary workstation is still unplugged."

    # ========== PHASE 9 -- NOELLE ALONE ==========

    "Noelle does not immediately return to the keyboard."

    "She sits at the forty-degree angle she turned her chair to, looking at the signature field on the primary screen. The field now carries his signature, his timestamp, and the AUTHORIZED/INCOMPLETE audit line."

    "The field is a small rectangular area near the middle of the document. Above it, three pages of Section I and the three hundred words of Section II she wrote before he arrived. Below it, nothing yet."

    "The field is in the middle of the nothing and the something in equal proportion."

    nthought "He signed it in the middle of the nothing."

    nthought "The middle of the nothing is where the authorization belongs. The middle of the nothing is where I designed the authorization to belong. I designed it there because I needed to know if he would sign a thing that was mostly nothing."

    nthought "He signed it."

    nthought "The design worked."

    nthought "I do not know if I wanted the design to work."

    # --- THE MOMENT OF INTERRUPTION ---

    "Noelle closes her eyes."

    "The closing of the eyes is not a choice she planned. The register does not plan eye-closes. The register is a working register and working registers do not permit small private acts of reprieve."

    "She closes her eyes anyway."

    "The eye-close lasts approximately two seconds."

    "When she opens them, the primary screen is still there and the cursor is still blinking beneath the first three hundred words of Section II and the signature field is still authorized and still incomplete and the whiteboard on the secondary screen is still showing the seven names."

    "None of the things she wanted to interrupt have interrupted."

    "She returns her hands to the keyboard."

    # --- THE REGISTER RESUMES ---

    "She types."

    "The sentence she types is not the next sentence of Section II. The sentence she types is a private note at the very bottom of the document, below where Section VII will eventually end, in a section labeled AUTHOR'S NOTE -- INTERNAL -- DO NOT PROPAGATE."

    "The author's note is a thing she has been adding to her most difficult documents since the Academy. The author's note is where she permits the doubts the one-pass rule does not permit in the body."

    "The author's note has only been used three times in her career."

    "She opens the author's note section. Types one sentence."

    n "(internal, typed, not spoken)"

    "I am writing this doctrine because the alternative to writing it is worse, and the alternative to writing it is the alternative I have already chosen by writing it, which means the alternative is not an alternative and writing it is not a choice, and I notice that the sentence I am now typing is the sentence I would need to unlearn in order to ever stop writing documents like this one."

    "She reads the sentence once."

    "She does not delete it."

    "She saves the document. The save writes the author's note to the private section of the file -- the section that does not appear in the main document, does not propagate to the review cycle, does not appear in the audit log. The author's note is a thing only Noelle can see."

    "The save is complete at 0947:33."

    # ========== PHASE 10 -- THE WALL CHART ==========

    "Noelle looks at the secondary screen with the whiteboard of seven names."

    "She looks at it for eleven seconds."

    "She does not add a name."

    "She does not delete a name."

    "She dims the secondary screen from quarter-luminance to eighth-luminance. The seven names are still visible. They are now a ghost layer on a dark screen."

    "She returns to the primary screen."

    "She begins writing the fourth sentence of the paragraph she was in when Aeron arrived."

    "The register resumes."

    "The register writes."

    # ========== PHASE 11 -- COdA ==========

    # CAMERA: slow pull-back through the alcove door -- the door has opened
    # just enough to show the corridor beyond, or the camera is drifting
    # through the closed door -- institutional coverage convention, the
    # camera leaving the room while the work continues.

    "The data alcove ambient. The low keystroke sound."

    "The primary screen with Section II growing beneath the signature field. The signature field is still in the middle of the document -- three pages of definitions above it, a paragraph of collaborator threshold work below it, and everything else still to come."

    "The author's note is saved. The author's note is the only place the doubt has been permitted. The author's note will not be read by anyone except Noelle, and Noelle will not read it again after today, because Noelle does not re-read author's notes. The author's note is where the doubt goes to not come back."

    "Aeron is already in the ops room. He is standing at the head of the table. He is reading the day-three Sector 4 consolidation approach. He is not thinking about the data alcove."

    "The doctrine Noelle is writing will arrive on his desk in final form in approximately four days. He will read it once. He will not read it twice. He has already signed it."

    "The not-reading-twice is the metric."

    "The base functions."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.noelle.doctrine_drafting", True)
    $ canon_set("ob.noelle.doctrine_title", "On the Structural Admissibility of Non-Combatant Target Categories")
    $ canon_set("ob.noelle.doctrine_sections_complete", 1)
    $ canon_set("ob.noelle.doctrine_version_at_signature", "0.17")
    $ canon_set("ob.aeron.blank_authorization_signed", True)
    $ canon_set("ob.noelle.authors_note_private", True)
    $ rel_bump("Noelle", trust=-1, complicity=2)
    $ flag("a4_ob_noelle_doctrine", True)
    $ flag("noelle_corruption_crossed_threshold_ob", True)
    $ npc_remember("Noelle", "wrote_doctrine_for_something_not_yet_asked", tone="authorship_as_deflection")
    $ npc_remember("Noelle", "this_is_how_it_happens_spoken_quietly", tone="register_underneath_the_register")
    $ npc_remember("Aeron", "signed_version_0_17_incomplete", tone="trust_as_institutional_instrument")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s10_noelle_doctrine_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Day after a4_s09 (Sector 12 sweep). 0923 to 0947:33 in the Phoenix
#     base data alcove. Noelle has not slept.
# cann.what_happened:
#   - Noelle is drafting a formal doctrine titled "On the Structural
#     Admissibility of Non-Combatant Target Categories." She has not been
#     asked to write it. She is writing it because the actions have outrun
#     the categories and she needs the categories to catch up.
#   - The document has Section I (Preliminary Definitions, ~3 pages)
#     complete. Section II (The Collaborator Threshold) has three hundred
#     words. Sections III-VII are unwritten.
#   - The private whiteboard from a4_s09 (seven tertiary-confirmed names)
#     is on a secondary screen as "shadow evidence" -- the empirical record
#     the doctrine must fit.
#   - Aeron arrives. Reads Section I standing. Says: "You are drafting the
#     rules for a thing I have not asked you to defend." Noelle: "You will
#     ask eventually. I am preparing."
#   - Noelle asks him to sign the authorization line NOW. The signature
#     field is in the middle of the document -- placed there deliberately
#     so that signing pre-authorizes the unwritten sections. Audit line
#     reads DOCUMENT VERSION 0.17 -- INCOMPLETE.
#   - Aeron signs. Audit line updates to AUTHORIZED -- INCOMPLETE. Aeron
#     says: "Send me the final version when Section VII is done." Noelle
#     offers to draft the closing sentence for his review first. Aeron:
#     "No. I trust the closing sentence." Four words. The trust is
#     institutional, not warm.
#   - Noelle says quietly: "This is how it happens." Aeron: "I know."
#   - Aeron leaves. Noelle writes a private author's note at the bottom of
#     the document (AUTHOR'S NOTE -- INTERNAL -- DO NOT PROPAGATE). The
#     author's note is the only place the doubt is permitted. Single
#     sentence. She does not delete it. She saves the document and returns
#     to the register.
# cann.noelle_state:
#   - Act 3 lie: "If I can model this, I can remain separate from it."
#   - Act 4 corruption: "If I can name what I am doing, I am still an
#     analyst. I have merely expanded what the analyst can do."
#   - The expansion is the corruption. Noelle notices this in the scene
#     while continuing to write.
#   - Uses "Commander," not "Aeron." The Name Mechanic from a3_s16 is
#     absent. The absence is a quiet grief.
#   - The author's note: "I am writing this doctrine because the
#     alternative to writing it is worse, and the alternative to writing
#     it is the alternative I have already chosen by writing it, which
#     means the alternative is not an alternative and writing it is not
#     a choice, and I notice that the sentence I am now typing is the
#     sentence I would need to unlearn in order to ever stop writing
#     documents like this one." (Saved private. Not re-read.)
# cann.aeron_state:
#   - Reads Section I in seventy seconds standing. Signs the version 0.17
#     incomplete draft because the speed of signing is the acceleration
#     the doctrine is built to provide. "The record is the record."
#   - Refuses to review the closing sentence in advance: "I trust the
#     closing sentence." The trust is the specific cold trust of an
#     institution for one of its instruments.
#   - "I know" in response to "this is how it happens." The two-word
#     exchange is the scene's moral center and is deliberately understated.
# cann.thematic_flags:
#   - AUTHORSHIP AS DEFLECTION. Aeron's interior names it directly:
#     Noelle is writing the categories so that her name is on the
#     categories rather than her name being on the doing. The authorship
#     is the distance she is trying to keep between herself and the actions.
#   - THE BLANK SIGNATURE. Aeron signs a document that is approximately
#     fifteen percent written. The signature is in the middle of the
#     document, not at the end. The position was arranged by Noelle. The
#     signature is the scene's gut punch.
#   - "THIS IS HOW IT HAPPENS" / "I KNOW." Five words, two words. The
#     admission is mutual. The admission does not stop anything.
#   - THE AUTHOR'S NOTE. The private section of the document where doubts
#     are permitted but not propagated. Noelle has only used it three
#     times in her career. She uses it here. The author's note is where
#     the doubt goes to not come back.
#   - THE NON-TREMOR. Noelle watches Aeron's left hand on the bezel. The
#     hand does not tremor. The absence of the tremor is the thing she is
#     writing the doctrine to catalogue. "The doctrine is the name for
#     the non-tremor."
#   - THE NAME MECHANIC IS ABSENT. In a3_s16 Noelle's intimacy with Aeron
#     was precision-as-warmth delivered through his name. In this scene
#     she uses "Commander" and keeps the Name Mechanic sealed. The seal
#     is the quiet grief. It is not flagged in dialogue.
# cann.character_moments:
#   - Noelle: the register. The shadow evidence whiteboard. The author's
#     note. The eye-close of reprieve that does not produce reprieve.
#     "I am the instrument that is naming itself."
#   - Aeron: the one-pass read of Section I. "I trust the closing
#     sentence." The hand on the bezel (no tremor). "I know."
# cann.callbacks:
#   - a3_s16_data_and_doubt_ob: Noelle's Name Mechanic and erotic precision
#     register. Sealed in this scene by the use of "Commander."
#   - a3_s14 (Noelle's Calculus): the non-reaction. The register.
#   - a4_s01_the_cold_room_ob: the one-stroke OB signature.
#   - a4_s02_the_new_shape_ob: the signature-as-ratification register.
#   - a4_s09_sector_12_sweep_ob: the Tuesday schema rewrite, the private
#     whiteboard of seven names, Nyra's civilian-framing line that
#     requires this doctrine to exist within a week.
# cann.block_status:
#   - ANCHOR. Always plays on OB path. No branching. No player choice.
#     Noelle's arc beat -- her categorical corruption formalized in a
#     document Aeron authorizes without reading.
# cann.requires_followup:
#   - The doctrine's Section VII closing sentence. Noelle has not yet
#     written it. Aeron has pre-authorized it. The sentence will arrive
#     in approximately four days.
#   - Noelle's break or non-break beat. The author's note is the seed of
#     the break. Whether it grows depends on later scenes.
#   - Possible Zira reading of the doctrine when it is circulated for
#     operational reference.
