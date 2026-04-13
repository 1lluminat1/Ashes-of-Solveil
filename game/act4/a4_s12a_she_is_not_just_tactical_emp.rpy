# =======================================================
# ACT 4 - Scene 12a: She Is Not Just Tactical (Empathy Path)
# File: a4_s12a_she_is_not_just_tactical_emp.rpy
# Type: SELENE NEW INTIMACY INSERT — the reversal beat
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s12a_she_is_not_just_tactical_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s12a_she_is_not_just_tactical_emp:
    $ show_timeline("30th of Forge, 390 A.C.", "02:00", "Phoenix Secondary Base — Officers' Corridor")


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("selene_valen", to_stage=3, source="a4_s12a_she_is_not_just_tactical_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Three movements.
    #         (1) Corridor approach: 35mm, Aeron's POV bias. The door to Selene's
    #             quarters ajar by an inch. A slice of lamplight on the corridor
    #             plates. The camera drifts forward at a walking pace, then halts
    #             at the exact distance a person stops when they have seen
    #             something they were not supposed to see.
    #         (2) The doorway hold: 50mm, over Aeron's shoulder. We see the room
    #             through the gap — Selene at her small reading desk, jacket off,
    #             hair out of its regulation braid for the first time on camera
    #             this act. A single sheet of paper in her hand. Not a datapad.
    #             Paper. The camera does not enter the room until Aeron knocks.
    #         (3) Inside the room: 40mm, two-shot. Selene at the chair, Aeron at
    #             a respectful distance. The chair itself becomes the third
    #             subject of the frame. At the one-touch beat, macro on Aeron's
    #             hand landing on the back of the chair — a deliberate inch short
    #             of her shoulder.
    # LIGHTING: One warm practical on her desk. The corridor behind Aeron is cold
    #           blue from the base overheads. The room is warmer than the
    #           corridor by about two stops. She is lit from below and to her
    #           left by the desk lamp. The shadow of her jaw on her own neck.
    #           No overheads in the room. She has turned them off.
    # SFX: Corridor ambient — generator hum, distant footsteps. Inside the room:
    #      absolute quiet. The soft crackle of the practical lamp. The paper
    #      when she folds it. Aeron's breath. A single held low string under the
    #      one-touch beat. No music otherwise.
    # FX/COMP: THE LETTER. Handwritten. Not Selene's hand — her sister's. Paper
    #          thin enough to show the reverse ink faintly through the sheet.
    #          Folded along a single crease that has been folded and refolded
    #          enough times to be soft. Evidence of carrying.
    #          THE CHAIR. Her reading chair, not her command chair. A smaller
    #          wooden piece she brought with her from her original Phoenix
    #          quarters through the displacement. The back of the chair is the
    #          one physical object Aeron touches in the scene.
    # BLOCKING: Aeron stops in the corridor. He almost walks away — the camera
    #           registers the half-turn. He does not walk away. He knocks. She
    #           speaks without getting up. He enters. He does not sit. He stands
    #           a respectful distance from her chair. At the one-touch beat, he
    #           steps forward and places his hand on the back of her chair — not
    #           her shoulder. He stays there for the rest of the scene.
    # FACE: Selene — unguarded in a way he has never seen her. The teacher mask
    #       is off. The co-commander mask is off. What is left is a woman with
    #       a letter in her hand. She does not cry. She does not look away. She
    #       lets him see her. That is the moment. Aeron — careful. Reverent.
    #       The man who has learned in the last week that rooms have thresholds
    #       and he has to pay attention to which side of them he is on.

    # ========= VOICE BASELINE =========
    # EMP cadence, quietest register of the act so far. Selene's voice is almost
    # a whisper — not broken, stripped. Aeron speaks less than she does, and
    # what he says is plain. The scene refuses ornament. The diction is Aeries
    # — measured, short, the consonants clean. Internal thoughts track Aeron's
    # slow rearrangement of what he thought Selene was.

    # scene bg_secondary_base_corridor_night_low with dissolve
    # play ambient "sfx/ambient/corridor_night_low.ogg" fadein 2.0

    # ========== PHASE 1 — THE CORRIDOR ==========

    "Oh-two-hundred. Forty hours into Phase II."

    "Aeron has been walking since the cipher alcove. The walk is not a route. It is the shape his body takes when the brain inside it will not stop counting the open problems on the board and the body has to be given something to do that is not counting."

    "He has passed the medbay — lights at half, Tessa somewhere inside it. He has passed the comms room — Noelle's reader on, Noelle not in her chair. He has passed Lyra's quarters and he did not slow down because Lyra's quarters is a room he has learned how to enter and tonight is not a night for entering rooms he knows how to enter."

    "He is in the officers' corridor now."

    "Selene's door is at the end of the corridor."

    "It is ajar."

    athought "By an inch. Maybe less."

    "The slice of lamplight falls across the plates of the corridor floor in a thin warm line. He registers it before he registers what it means."

    athought "Her door is never ajar."

    athought "Selene's door is closed when she is working and closed when she is sleeping and closed when she is angry and closed when she is composed and closed when she has the rest of the team in there and closed when she is alone. The door is closed. That is the rule."

    athought "Tonight the door is not closed."

    "He slows. He does not mean to slow. His body decides for him — the same body that has been refusing to stop moving for a week, now deciding, for the first time in forty hours, to stop."

    "He stops in the corridor about three meters from the door."

    # ========== PHASE 2 — THE GAP ==========

    "He can see a slice of the room through the gap."

    "It is her personal quarters, not her office. He has been inside once, on the night of the displacement, and he remembers the geometry: small bunk to the right, reading desk to the left, one chair, one shelf, one window. The window has been sealed with a plate since the move — the outer wall is not secure for glass."

    "The one warm lamp is on the desk. Not overhead. Overhead is off."

    "Selene is in the reading chair."

    "Her jacket is off. He can see the undertunic, sleeves pushed to the elbow. Her hair is out of the braid she wears during operational hours — loose at her shoulders. The braid has been undone recently enough that the hair still holds the shape of where it was bound."

    athought "I have never seen her hair out of the braid."

    athought "Not in three years."

    "She is holding a sheet of paper."

    "Not a datapad. Paper. Real paper, of the kind that is almost impossible to come by in the secondary base — they burn the scraps for kindling most nights. The sheet is pale and thin and the reverse ink is showing through faintly from the other side."

    athought "That is a letter."

    athought "Someone wrote her a letter. On paper. In a war where paper is kindling."

    "Her face is not composed. It is not uncomposed either. It is the face of someone reading something that has become, over the course of the reading, heavier than they had planned for. Her mouth is slightly parted. Her eyes are moving across the page at the speed of a person who has already read the words and is now visiting them."

    "She is not crying. She has never cried in front of him and he does not think she is about to. But her face is off. The face that stands behind the co-commander's face. The face that the co-commander's face is made of."

    athought "Oh."

    athought "I should not be seeing this."

    # ========== PHASE 3 — THE ALMOST-LEAVE ==========

    "He half-turns."

    "The turn is not a decision. It is a reflex of respect. The body says: this is private, step back, the corridor extends in the other direction, there are other routes to the ops wing, you never saw this, you never stopped."

    "He takes one step back."

    athought "I should leave."

    "He takes one more step back."

    athought "I should leave now. She did not choose to be seen. The door being open is probably an accident — she left it ajar when the ventilation cycled or she came in from the corridor and the latch did not catch. The door being open is not an invitation."

    athought "The correct move is to walk away and pretend I never passed this corridor."

    "He is about to turn the rest of the way."

    "He stops."

    athought "Wait."

    athought "Selene does not leave doors ajar by accident. Selene's latches catch. Selene's routines catch. Selene is the most deliberate physical person in this building — the woman who put her teacup down at exactly the same spot on the cipher table every morning of Chapter I, the woman whose jacket hangs at a precise angle on the hook behind her office door, the woman who once corrected me for leaving the war-room chair at the wrong angle."

    athought "Selene did not leave this door ajar by accident."

    athought "She left it ajar by an inch because leaving it closed tonight required more than she had and leaving it open required more than she wanted to give and an inch is the exact compromise her body found."

    athought "An inch is the exact compromise of a woman who does not want to be seen and does not want to be entirely alone."

    "He does not know how he knows this."

    "He knows it the way he knows which note a tuning fork is holding. The door at an inch is a note. It has a pitch. He is a man who has been trained to hear pitches and he is standing in a corridor with a pitch in his ears."

    athought "She did not ask for company."

    athought "She left the door at an inch."

    athought "Those are the same sentence."

    # ========== PHASE 4 — THE KNOCK ==========

    "He steps back toward the door. Not all the way — enough that he can reach the frame. He does not push the door wider. He does not look through the gap again. He lifts his hand."

    "He knocks once. Quiet. Two knuckles. The knock that says: I am here, I saw nothing, I am asking."

    "A beat."

    "Her voice from inside, soft."

    sel "Come in, Aeron."

    athought "She knew it was me."

    athought "She probably heard me stop in the corridor three meters away. Selene's hearing is the reason she has been alive for fourteen years of this war."

    athought "She heard me stop. She heard me half-turn. She heard me come back. She has been listening to the geometry of my indecision for the last ninety seconds."

    "He pushes the door open another inch — no more — and steps through."

    "He closes it behind him. Not all the way. He leaves it at an inch from his side, because the inch is the pitch the room is holding and he is not going to retune the room."

    # ========== PHASE 5 — THE ROOM ==========

    # scene bg_selene_quarters_lamp_only with dissolve

    "The room is warmer than the corridor by a margin he feels on his face."

    "The lamp on the desk is doing all of the lighting. The shadows are long. Her bunk is neatly made in the corner — she has not slept yet, or she made it after she got up. The shelf above the desk has three objects on it: a cipher reader, a small stone, a photograph frame face-down."

    athought "The photograph is face-down. I have never been close enough to the shelf to notice."

    athought "It is face-down because she turned it down tonight."

    "Selene does not stand."

    "She folds the letter along its single crease. Slowly. Deliberate — the same deliberate of the teacup and the jacket and the war-room chair. She places it on the desk beside the lamp. She does not put it away. The letter is still in the room."

    "She looks at him."

    "This is the first time he has seen her look at him from this face."

    "Not the commander face. Not the teacher face. Not the face she wore when she delivered the correction across the war-room table a week ago. The face underneath those faces — the one she keeps in this room, behind this door, with the latch that catches."

    "He stops about two meters from the chair. That is the distance a person stops at when they are respecting a threshold inside a room they have already entered."

    "He does not speak first. He knows better than to speak first in a room that is holding a pitch."

    # ========== PHASE 6 — THE LETTER ==========

    "Selene speaks first."

    sel "The courier chain out of Sector 4 cleared three days ago."

    "Her voice is stripped. Not broken — stripped, the way bark is stripped from wood to show the grain. There is nothing performative left in it. Aeron has never heard her voice at this register."

    sel "The letter is from my sister."

    athought "Her sister."

    athought "I did not know Selene has a sister."

    athought "That is not an accident. I did not know because Selene did not tell me. Three years of shared command and the word sister has never been in the room."

    a "You have a sister."

    sel "I have a sister."

    "A beat."

    sel "Her name is Ilene. She is four years younger than me. She lives in a sector Phoenix cannot reach."

    "She is still looking at him. Not defiantly. Just — letting him see this. Letting the information land."

    sel "The courier chain is the only way anything moves in or out of that sector. It is not a Phoenix chain. It is older than Phoenix. It runs through a network of bakers and mill-keepers and one midwife and it moves a letter every four to six months if the weather and the Echelon patrols cooperate."

    sel "This is the third letter I have received from her since the war started."

    sel "I have written her fourteen."

    "The math sits in the room for a second. He does not do anything with it. He lets it sit."

    sel "The reach of our network does not extend to her. I have checked. I have checked every month since the Hollow. I have asked Zira. I have asked Noelle. I have asked couriers I do not trust because I was tired. The answer is the same answer every time. The sector she is in is outside our operational envelope and the cost of bringing it inside the envelope is a war we are not fighting and would not win if we fought it."

    sel "I cannot reach her."

    sel "I cannot get her out."

    sel "She is alive in this letter. As of approximately six weeks ago, when the letter was written. I do not know whether she is alive tonight."

    # ========== PHASE 7 — THE KNOWING ==========

    "She has not cried. Her eyes are wet at the lower lid in a way that is not crying — it is the wetness that sits there when a person is holding a thing very precisely and the hold is costing water from the edges."

    "She does not wipe her eyes."

    "He stays where he is."

    athought "I am rearranging Selene in my head."

    athought "The woman I have been learning from for a week — the voice that corrected me at the cipher table, the voice that said 'delegate the question,' the voice that taught me the Kael lesson in front of the whole council — that woman has a sister in a sector we cannot reach and she has been carrying the sister the entire time she has been teaching me."

    athought "Every lesson she has given me this act has had a sister inside it."

    athought "Every correction. Every pause. Every doctrine."

    athought "Selene has not been a doctrine delivery mechanism. Selene has been a woman carrying someone she cannot save and pouring the carrying into the nearest living person who would take it — which, in the shape of the last week, has been me."

    athought "She has been keeping her sister alive in me."

    athought "She has been practicing sisterhood on me because practicing it on her actual sister is the practice she has been forbidden."

    athought "I did not know that until the inch of the door told me and the letter confirmed it and I am standing in her room with the math of the last week reshaping in real time."

    "He does not say any of that. He knows better than to name a thing that is standing in the room holding itself together by not being named."

    "He looks at her. He looks at the letter on the desk."

    "He takes one step forward."

    "Not two. One."

    "He puts his hand on the back of her chair."

    # ========== PHASE 8 — THE INCH SHORT ==========

    # VISUAL: Macro on the hand landing on the wood. Aeron's hand flat, thumb
    # curled under the top rail. The distance between his fingers and her
    # shoulder is roughly an inch. He could close it. He does not.

    "The back of the chair, not her shoulder."

    "A deliberate inch short."

    athought "I am not going to touch her."

    athought "Not because the touch would be wrong. Because the touch would be about me. Touching her would be the move that said: I know how to fix this. Touching her would be the move that inserted my hand into a grief she has been holding in this chair alone for three years before I met her."

    athought "I am not the person who gets to put a hand on that grief."

    athought "I am the person who gets to put a hand on the chair."

    athought "The chair says: I am here. The chair says: you are not alone in this room. The chair says: I see you as a person and not as my commander, and because I see you as a person, I know that a commander would put a hand on your shoulder and a person who has not asked permission would not."

    athought "The inch is the permission I have not asked for, honored as a line I am not crossing."

    "Selene looks at his hand on the back of the chair."

    "Her face does something small. The corner of her mouth moves a fraction — not a smile, the smaller thing that is the acknowledgment of an offering accepted."

    "She does not look up at him."

    "She does not have to."

    # ========== PHASE 9 — THE LINES ==========

    sel "I did not want you to see me like this."

    "Quiet. Stripped. Not ashamed — stating."

    "A beat. Aeron does not fill it immediately. He lets the sentence be in the room. Then:"

    a "I know."

    "A longer beat. His hand does not move from the chair."

    a "I want to anyway."

    "She makes a sound that is not a word. Barely a breath — a half-exhale that holds something in it that might be laughter if it had more strength and might be grief if it had less. It is the sound of a woman hearing a sentence she had not expected to hear tonight and filing it somewhere."

    sel "That is a sentence the old Aeron would not have said."

    a "No."

    sel "That is a sentence the Aeron of a month ago would not have said."

    a "No."

    sel "That is a sentence the Aeron of this week could say."

    a "Yes."

    "A beat."

    sel "Then I am glad it is this week."

    # ========== PHASE 10 — THE LETTER, READ OUT LOUD (NOT) ==========

    "He does not ask what the letter says."

    "He wants to. The old shape of him wants every piece of information that is in the room. The old shape of him wants to know the sister's sector, the courier's name, the dates, the operational envelope, whether the envelope can be bent, the cost of bending it, the Phoenix assets available for a retrieval run, the probability curves."

    "The old shape of him wants to fix this."

    athought "I am not going to ask."

    athought "The letter is hers. The letter is not an intelligence document. The letter is the object in her hands that has been holding her sister's shape in this room for however many hours she has been sitting here. If I ask what it says, I am asking her to hand her sister to me, and if she hands her sister to me, I will start doing the math on retrieval, and the math will not go well, and she will have spent the letter on a plan that cannot happen."

    athought "She has been carrying this alone because the carrying does not have a plan attached to it. The absence of the plan is what makes the carrying a grief and not a mission."

    athought "I am going to honor the absence."

    "He says, instead:"

    a "Is there anything in the letter that is urgent."

    "He does not inflect it as a question. He is giving her the option to say no."

    sel "No."

    sel "Nothing operational. She is — she is telling me about a cat she has been feeding. Outside her door. A black and white cat. She named it after our grandmother. The cat has been coming for about two months now."

    sel "The cat is the news."

    "A beat."

    sel "She is telling me she is still the kind of person who names cats. That is the news. The rest is about the cat's habits. What time it comes. Whether it lets her touch it. She says it has started letting her touch it on the back of the neck but not anywhere else yet."

    "Her voice is almost steady."

    sel "She named it Grandmother."

    "A beat."

    "And then, very quiet:"

    sel "Grandmother is dead."

    a "I know."

    sel "Everyone's grandmother is dead in this war. That is not the point. The point is that Ilene picked up a cat and named it for a dead woman as a way of being a person in a sector where being a person is — difficult. And she wrote me a letter to tell me about it. And the letter took six weeks to reach me. And the reason I am sitting in this chair at oh-two-hundred with the door at an inch is that I do not know if the cat is still coming."

    sel "I do not know if Ilene is still there to feed it."

    sel "I will not know for at least another four months if I ever know at all."

    sel "And I have a war to run in the meantime."

    # ========== PHASE 11 — THE WEIGHT HE SEES ==========

    "His hand does not move from the chair."

    "The back of the chair is warm under his palm now. The wood has taken his heat."

    athought "Every doctrine she has taught me this week has had this weight inside it."

    athought "'Delegate the question' was a sentence spoken by a woman who has been forbidden from asking the only question she wants to ask, which is: is my sister alive."

    athought "'The Kael lesson' was a sentence spoken by a woman who has already had to put down her own dreams of saving the one person she most wanted to save, twenty years ago, in a different war."

    athought "'Shared authority' was a sentence spoken by a woman who has been running this command alone for three years and has been practicing the idea of sharing on a brother-figure because her sister is out of reach."

    athought "I thought I was learning command from a commander."

    athought "I was learning sisterhood from a sister who has a sister and cannot have her."

    athought "Those are not the same lesson."

    athought "Except in her. In her they are the same lesson. She has been teaching me the only curriculum she has, which is the curriculum her grief has written."

    athought "I am going to have to carry this differently than I was carrying it yesterday."

    "He does not say any of that."

    "He says the true small sentence that fits in the room."

    a "Thank you for letting me see this."

    sel "You did not give me much choice."

    a "I gave you an inch."

    "Her mouth does the small-move again."

    sel "You gave me an inch. That is the exact amount of choice I had left tonight."

    sel "Thank you for knocking."

    # ========== PHASE 12 — THE STAYING ==========

    "He stays."

    "He does not sit. There is no second chair in the room. The bunk is not a place he is going to put his body in this room tonight. He stays standing, his hand on the back of her chair, his eyes not on her face but in the middle distance just past her shoulder — the angle of looking that lets a person be witnessed without being observed."

    "Selene picks up the letter from the desk."

    "She does not unfold it."

    "She holds it on her lap, both hands over it, the way a person holds a small animal."

    "They are quiet for a long time."

    "Outside the door, the corridor carries its ambient — the distant footsteps of the third-shift rotation, the generator hum, the tick of a vent somewhere down the hall. Inside the room, the lamp crackles once. The letter in her lap does not move."

    "Her breath finds a slower cadence. Not sleeping — settling. The breath of someone who has been holding something in a room alone for three hours and is now holding it in a room with one other person and the difference is registering in her autonomic system before her conscious mind has agreed to register it."

    athought "She is letting her shoulders down."

    athought "Not all the way. A fraction. The inch of the door, translated into her back."

    athought "I am going to stay exactly as long as she wants me to stay, and I am going to know she wants me to go when she wants me to go, and I am not going to ask her which."

    "Eventually she speaks."

    sel "You should go."

    sel "Not because I want you to."

    sel "Because you have not slept in — I am not going to guess. It will insult both of us. And because if you stay, I will fall asleep in this chair, and I cannot afford to be found asleep in this chair by the morning rotation with a handwritten letter on my lap and the door at an inch."

    sel "The picture would be — unhelpful for the command."

    a "Understood."

    sel "Go. I will see you at the oh-six-hundred brief."

    "A beat."

    sel "Aeron."

    a "Yes."

    sel "This stays in the room."

    a "Yes."

    sel "I am not making you swear. I am telling you what the shape of the trust is."

    a "I heard you."

    # ========== PHASE 13 — THE LEAVING ==========

    "He lifts his hand from the chair."

    "Slowly. The wood is still warm under his palm. He lets the warmth leave before his hand does — a small pause he does not explain to himself."

    "He does not touch her on the way out."

    "He walks to the door. He opens it the same inch he came in through, and then another inch, and then he is through."

    "At the threshold he looks back once."

    "Selene is in the chair. The letter is on her lap. Her hair is still out of the braid. The lamp is still on the desk. She is looking at the letter, not at him."

    "But the corner of her mouth is holding the small-move from earlier. The acknowledgment. The offering received."

    "He steps into the corridor."

    "He closes the door behind him — all the way, this time, because the pitch has changed. The inch was for the corridor-he-was-walking. The closed door is for the room-she-is-holding-alone-again-but-differently-now."

    "The latch catches."

    # ========== PHASE 14 — THE CORRIDOR, AFTER ==========

    # scene bg_secondary_base_corridor_night_low with dissolve

    "Aeron stands in the officers' corridor."

    "The overheads are cold. The slice of lamplight is gone — the door has caught the light back inside the room. The corridor is the same cold blue it was five minutes ago."

    "He is not the same."

    athought "I am not going to sleep tonight."

    athought "That is not new. I was not going to sleep tonight before I walked past this door. What is new is what I am not going to sleep with."

    athought "I have been carrying Selene as my teacher. I have been carrying her as my co-commander. I have been carrying her as the person who stopped me at the war-room table last week and corrected me in front of the team."

    athought "Tonight I start carrying her as a woman with a sister in a sector I cannot reach. That is a different weight and it goes in a different place and I am not going to put it down."

    athought "Ilene."

    athought "Four years younger. A cat named Grandmother. Letting it touch the back of the neck but not anywhere else yet."

    athought "I am going to remember those facts. I am going to remember them the way Tessa remembers the names on the board. I am going to remember them because remembering them is the only retrieval operation that is available to me tonight."

    athought "I cannot get Ilene out."

    athought "I can hold her in my head next to my mother and Kesa Marin and Joren Hale and the two hundred and some other names I have started counting differently in the last week."

    athought "That is not much."

    athought "Selene left the door at an inch. An inch is not much either. And I knocked."

    "He starts to walk."

    "The war room is in the other direction. He is not going to the war room. He is going back to his quarters, because the scene has rearranged him and he needs the rearrangement to finish somewhere that is not a public corridor."

    "Behind him, the officers' corridor holds one closed door with a warm lamp on the other side of it and a woman in a chair with a letter on her lap and the small-move still on the corner of her mouth."

    "He does not look back."

    "Fade."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=2, attraction=1)
    $ canon_set("selene.sister.name", "Ilene")
    $ canon_set("selene.sister.status", "unreachable")
    $ canon_set("selene.sister.last_letter_age_weeks", 6)
    $ canon_set("selene.reading_chair.aeron_touched_back", True)
    $ flag("aeron_saw_selene_with_letter", True)
    $ flag("selene_teacher_mask_off_once", True)
    $ npc_remember("Selene", "let_aeron_see_her_with_the_letter", tone="unguarded_trust")
    $ npc_remember("Selene", "door_at_one_inch", tone="the_compromise")
    $ npc_remember("Aeron", "hand_on_the_chair_not_her_shoulder", tone="respect_as_presence")
    $ tp_seed("a4.selene.letter_to_sister")
    $ tp_seed("a4.selene.inch_of_the_door")
    $ metric("selene_unguarded_moments_witnessed", delta=1)
    $ scene_mark(_current_scene_id, "exited")
    call li_lore_check("Selene") from _a4_s12a_lore

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s12a_she_is_not_just_tactical_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Oh-two-hundred. 40 hours into Act 4 Phase II. After Batch B/C parallel
#     scenes (s10 delegate-the-question, s11 mercy call on 6 captives, s11a
#     Lyra's Seren prayer, s11b rule-of-three breaks on Liora's name, s12
#     Tessa "held not fixed"). Selene has been the teacher all act.
# cann.what_happened:
#   - Aeron walks the officers' corridor at oh-two-hundred. Selene's door is
#     ajar by an inch — a near-impossibility for a woman whose latches always
#     catch. He almost walks away. He registers the inch as a deliberate
#     compromise and comes back.
#   - He knocks. Selene invites him in without getting up. He enters. The
#     room is lit only by a warm desk practical. Her hair is out of its
#     regulation braid for the first time in the run. She is in her reading
#     chair with a handwritten letter on paper.
#   - Selene tells him she has a sister named Ilene, four years younger, in
#     a sector Phoenix cannot reach. The courier chain out of Sector 4 is
#     not a Phoenix chain — older, civilian, running through bakers and a
#     midwife. The letter is the third she has received in the war. She has
#     written fourteen. Ilene is alive as of six weeks ago. Selene cannot
#     retrieve her and has been asking monthly whether she can for years.
#   - The letter's content: Ilene has been feeding a stray cat at her door
#     for two months. She named it Grandmother. The cat has started letting
#     her touch the back of its neck. That is the news. Selene's weight:
#     she does not know if the cat is still coming — i.e., whether Ilene is
#     still there.
#   - Aeron does not ask to read the letter. He does not begin a retrieval
#     calculation. He stands at a respectful distance and places his hand
#     on the back of her reading chair — a deliberate inch short of her
#     shoulder. The chair is the scene's third subject.
#   - Key lines:
#       Selene: "I did not want you to see me like this."
#       Aeron: "I know. I want to anyway."
#       Selene (quiet): "Then I am glad it is this week."
#   - Selene eventually sends him away — not because she wants him to leave
#     but because she cannot afford to be found asleep in the chair by the
#     morning rotation with the letter on her lap. He honors it.
#   - Internal reframing: Aeron rearranges his understanding of Selene's
#     entire act so far. Every doctrine she has taught him has had her
#     unreachable sister inside it. She has not been a doctrine delivery
#     mechanism — she has been practicing sisterhood on him because the
#     actual practice has been forbidden.
# cann.aeron_state:
#   - First full reversal of the teacher relationship. The person who has
#     been teaching him all act is now the person he is being careful with.
#   - The one-touch discipline: hand on the chair, not her shoulder. A
#     deliberate inch short. He articulates internally why — the touch
#     would be about him; the chair is the offering that is about her.
#   - He carries away three new retained facts (Ilene, four years younger,
#     cat named Grandmother). He explicitly equates this to Tessa's board
#     practice. The Act 4 through-line of "remembering as the only retrieval
#     available" is now running in his head.
# cann.selene_state:
#   - First unguarded-at-rest beat in the run. Hair out of braid. Door at
#     an inch. Letter in hand. She does not cry. She lets herself be seen.
#   - The "inch of the door" established as a canonical Selene grammar —
#     her compromise between being alone and not being alone. The scene
#     treats it as a tuning-fork pitch Aeron hears in the corridor.
#   - Teaching Aeron all act has been a displacement of sister-practice.
#     This is established in Aeron's internal monologue as the interpretive
#     key for every prior Selene scene in Act 4. Re-read a4_s02, s04, s06
#     with this in mind.
# cann.thematic_flags:
#   - The teacher is also the student of her own grief. Doctrine delivery
#     as a cover for practice-what-you-cannot-have.
#   - "Seeing her as a person, not as my commander" — named explicitly in
#     the scene directive and enacted as the chair-touch discipline.
#   - Retrieval as memory when retrieval as operation is forbidden.
#     Explicit link to Tessa's board practice from a4_s06.
#   - The Aeries-trained instinct to fix is deliberately suppressed. Aeron
#     declines to ask what the letter says. Declines to begin a retrieval
#     calculation. This is the Act 4 "can I lead without turning leadership
#     into a weapon" question answered in miniature.
# cann.callbacks:
#   - a4_s02 (the war-room correction): re-contextualized — Selene's
#     "delegate the question" voice is the voice of someone forbidden to
#     ask her own question.
#   - a4_s10 (delegate the question, Batch B/C): the doctrine is now known
#     to have biographical weight.
#   - a4_s06 (Tessa's silent board): Aeron explicitly parallels his new
#     Ilene-facts to Tessa's name-keeping. Cross-LI grief vocabulary
#     continues converging.
#   - a3_s01 (accountability promise, "don't let me become what I'm
#     fighting"): the scene is a reverse of the s02 correction — Selene
#     being corrected into being seen, by the accountability structure
#     running in the other direction.
# cann.character_moments:
#   - Selene: hair out of braid, letter on paper in a war where paper is
#     kindling, the small-move at the corner of her mouth, "Then I am glad
#     it is this week."
#   - Aeron: the almost-leave, the tuning-fork recognition of the inch, the
#     hand on the chair not the shoulder, the discipline of not asking what
#     the letter says.
# cann.block_status:
#   - LINEAR. No branching. No player choice. EMP path only.
# cann.requires_followup:
#   - tp_seed a4.selene.letter_to_sister — any future Selene scene that
#     returns to this chair, this letter, or the Ilene facts gains True
#     Path weight if Aeron's hand-on-chair discipline is maintained.
#   - canon_set selene.sister.status "unreachable" is a locked state. Do
#     not break without a dedicated scene.
#   - The "inch of the door" as Selene grammar is established. Future
#     Selene intimacy beats may play against or deepen this motif.
#   - Cross-reference with s10 (delegate the question) in post-hoc read —
#     the doctrine now carries biographical weight. Any re-use of the
#     phrase by Aeron in later acts should acknowledge the sister.
