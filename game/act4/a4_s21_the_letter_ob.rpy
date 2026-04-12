# =======================================================
# ACT 4 - Scene 21: The Letter (Obedience Path)
# File: a4_s21_the_letter_ob.rpy
# Path: OB
# Type: LIORA'S LETTER / CORE MIRROR BEAT
# Character Focus: Zira, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s21_the_letter_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s21_the_letter_ob:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("liora_rylan", to_stage=3, source="a4_s21_the_letter_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. OB grammar. No handheld, no drift. The letter scene
    #         needs the absence of motion because the motion is interior.
    #         Open wide on the ops room: empty, pre-shift, the tables cleared,
    #         a single terminal humming on standby at the far wall. Aeron at the
    #         head of the long table, standing -- not seated yet. A mug of black
    #         coffee he has not touched in ten minutes cools beside his left hand.
    #         Zira enters from the corridor door, frame right. She does not
    #         hesitate. She has been awake the full night and has been holding
    #         the envelope in her jacket for three hours waiting for 0500.
    #         Camera pushes to a locked medium two-shot across the table. Then,
    #         when the letter comes out, a clean insert top-down on the folded
    #         page. Then medium on Aeron's face as he reads. Then insert on his
    #         hands as he refolds. Then medium on Aeron's chest as the letter
    #         goes inside the jacket. The camera does not move for any of it.
    #         The OB register is locked.
    # LIGHTING: Ops room overheads at 40%. The working light of a room that
    #           has not yet filled with its day shift. Cold white on the tables.
    #           A warmer amber from the standby terminal, ten feet behind Aeron.
    #           The letter, when it is on the table, is lit by the cold white.
    #           When it goes inside the jacket, it leaves the cold white behind
    #           and travels to the place the camera cannot see. That transition
    #           is the scene's only visual argument.
    # SFX: Loop -- ops room ambient. The low hum of server racks two rooms over.
    #      The HVAC. No other shift movement yet. One-shots -- the corridor
    #      door cycling when Zira enters (pressure seal, a single soft hiss).
    #      The rustle of the envelope leaving Zira's jacket. The dry whisper
    #      of a single handwritten page unfolding. Aeron's breath once, slow,
    #      midway through the second read. The letter refolding. The soft
    #      textile sound of it going inside a jacket against fabric and skin.
    #      No music. No score cue. The scene's score is the absence of one.
    # FX/COMP: The ops table: a long dark surface, map overlay dormant, the
    #          day's packet stack at Aeron's place (Nyra's overnight summary,
    #          Noelle's model exports, a Ghostline relay log). The letter when
    #          it appears sits on top of all of that. The letter is on top
    #          because the letter is, for this one scene, the only document
    #          in the room that matters.
    #          The envelope: old waxed paper, folded twice, no seal, no
    #          address. Zira has been carrying it folded against a hardcover
    #          so it would not crease further. She removes the hardcover first
    #          and sets it aside. Then the envelope. Then the page.
    # BLOCKING: Zira enters and stops four feet short of the table. She does
    #           not sit. Aeron does not offer her a chair. They are standing
    #           on opposite sides of a table that will, in fifty minutes, fill
    #           with other people. That is the whole geography: a window of
    #           alone before the room stops being alone.
    #           When Aeron reads, he stands still. His left hand does not move
    #           from the table edge. His right hand holds the page. He reads
    #           once. Sets the page down. Picks it up. Reads again. Sets it
    #           down. Then picks it up one more time and folds it.
    # CANON: THE LETTER ARRIVES ON OB. Liora's handwritten page to Marcus,
    #        never sent, dated when Aeron was six. Zira found it in a dead
    #        drop months ago and has been holding it. She brings it to him
    #        after Rhea Vestin's strike on Phoenix the previous day.
    #        The key line: "I fell in love with the pause."
    #        On OB, this letter does not soften Aeron. It clarifies him.
    #        He does not reject the letter. He does not dismiss the pause.
    #        He names the pause as a thing his mother thought was possible
    #        and explicitly declares it is not possible for him. Then he
    #        keeps the letter inside his jacket against his chest. The letter
    #        is not a door. It is a gravestone he is willing to carry.
    # FACE: Zira -- steady. She has made peace with bringing it. She is
    #        not here to save him. She is here because after yesterday she
    #        decided he needed to see it before Act 5 started. Her face is
    #        the face of a courier who knows the freight is heavy and is
    #        going to set it down regardless.
    #        Aeron -- the mask. But the mask has a quality it has not had
    #        since a3_s21 when he learned Liora was alive. The quality is
    #        recognition. Not grief. Recognition. He is reading a thing
    #        that confirms something he already knew about himself and had
    #        not heard in his mother's handwriting before.

    # ========= VOICE BASELINE =========
    # Zira: direct, operator. Not tender. She says why she is here and she
    # says the minimum. She watches him read. She does not interrupt.
    # Aeron: OB register -- the Marcus idiom tightening, but this one scene
    # permits him a slim sliver of self-recognition. He does not go warm.
    # He goes precise. The precision is the scene's cost.
    # athought: the interior Aeron is showing himself. zthought: the interior
    # Zira is holding closed. Both are in steady, low mode. No flare.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - OPS ROOM - 0500 (PRE-SHIFT)]
    # The room is empty. Aeron is the first one in, the way he has been
    # the first one in every morning for eight days. The day shift does
    # not start until 0600. There is a fifty-minute window before anyone
    # else arrives. Zira knows the window. She chose it.

    #scene bg_phoenix_ops_room_ob_predawn with dissolve
    #play ambient "sfx/ambient/ops_room_predawn.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DOOR CYCLES ==========

    "The ops room door cycles at 0500 on the dot. Aeron does not look up. He knows who it is because Zira is the only other person on the base who runs on a zero-minute clock."

    a "Zira."

    z "Aeron."

    "He does not ask why she is here. She is here at 0500 in an empty ops room. The reason is already in the geometry."

    athought "She has been awake all night. I can see it in her shoulders -- not fatigue, alignment. She has made a decision and walked it down a corridor."

    athought "The decision is the envelope."

    "The envelope is in her left hand. It is tucked inside the cover of a small hardbound notebook. She is holding the notebook the way a person holds a thing that has been wrapped around another thing to protect the other thing."

    a "Set it down."

    "She walks to the table. Stops four feet short. Does not sit. She places the notebook on the table, then removes the envelope from inside the cover. She sets the envelope on the notebook. The notebook becomes a plinth. The envelope becomes the thing on the plinth."

    zthought "I am going to give him this and then I am going to stand here and watch him read it. That is the shape of the delivery. I do not hand him the freight and then leave. I hand him the freight and I stay in the room until the freight is inside him."

    zthought "Because what I am not going to do is what a courier does who delivers a bomb and walks."

    # ========== PHASE 2 -- THE WHY ==========

    a "When did you get this."

    z "Four months ago. From a dead drop in the undercity. It was inside a Ghostline cache I was decommissioning. It had been there a long time. Years."

    a "Why now."

    z "Because yesterday seven of our operators died and you are about to plan an assassination."

    "He lets that sit. He does not confirm the assassination. He does not have to. Zira knows the shape of a day after a Rhea Vestin strike. She has run Ghostline long enough to know what a man in his chair does the morning after he loses seven."

    a "You held it four months."

    z "I held it four months because I did not know what it was for."

    z "Yesterday I figured out what it is for."

    a "Which is what."

    z "I will tell you after you read it."

    # ========== PHASE 3 -- THE PAGE ==========

    "He picks up the envelope. The waxed paper is old. The fold lines are set deep. No seal. No address. Whoever folded this folded it to keep it private, not to send it."

    athought "Zira's hands know the difference between a letter for transit and a letter for storage. This one is storage. This one was written and then kept."

    "He draws out a single page. Handwriting in ink. The ink is old. The paper has yellowed at the edges but the text is clean. A woman's hand -- the letters narrow, the downstrokes firm, the crossbars on the t's long and horizontal."

    "He does not need the signature. He has known this handwriting since he was four."

    athought "My mother."

    athought "This is a letter my mother wrote."

    # ========== PHASE 4 -- THE READING (FIRST PASS) ==========

    "He reads. He does not read aloud. The camera does not show the full page. The camera shows his eyes moving across it and the slight adjustment of his jaw at a line roughly two thirds of the way down."

    "The room holds."

    athought "Dated. Fourteen years ago. I was six."

    athought "The greeting is Marcus. She wrote this to Marcus. She never sent it."

    athought "The first paragraph is about me. About a night I do not remember. I was in the other room. I was six. She wrote that she could hear me breathing through two walls and that it made her think about what a room sounds like when there is a person in it who has not yet been shaped."

    athought "The second paragraph is about him. About Marcus. About a specific moment at the war table when he was deciding whether to approve an interdiction. She writes that he used to have a beat in him before he decided. A pause. A breath between the decision and the execution. She writes that she had always thought the pause was just his thinking. Then she writes the sentence she wrote the letter to write."

    athought "'I fell in love with the pause.'"

    athought "'The moment between the decision and the execution. The moment you used to have, and the moment you have stopped having. I can no longer love a man who does not pause.'"

    "He has reached the sentence. He reads it. He does not move. Zira watches him across the table. She has also read the letter. She read it four months ago in the undercity with a headlamp. She has been carrying the sentence in her head every day since."

    zthought "He is on the sentence."

    zthought "I can see the exact line his eyes are on. I memorized the layout of the page before I sealed the envelope because I wanted to know, from across the table, where he was in it."

    zthought "He is on the sentence."

    # ========== PHASE 5 -- THE PAUSE HE DOES NOT TAKE ==========

    "He finishes the page. He sets it down on the notebook. His hand rests flat beside it for a beat. The beat is long enough to be visible and short enough to mean nothing."

    "He picks the page back up. Reads again. The second read is slower. He is not searching for new information. He is calibrating."

    athought "Read it again. Read it for what it is, not for what you want it to be."

    athought "It is not a letter to me. It is a letter to Marcus about the moment he stopped being the person she could love. It is a letter about a door that closed."

    athought "It is not an instruction. It is a diagnosis."

    athought "Read it again."

    "He reads it again. The third read is the one the camera holds longest on. He does not breathe visibly through the third read. When he finishes, he sets the page down, flat, and his hand leaves it."

    # ========== PHASE 6 -- THE FIRST SENTENCE ==========

    "He looks up. Meets Zira's eyes across the four feet of table and empty air."

    a "She wrote this when I was six."

    z "Yes."

    a "Marcus never paused."

    z "No."

    a "My mother fell out of love with the absence of a pause. That is what this letter is. It is not advice. It is the inside of the hour she decided."

    "Zira does not answer. She is not here to help him assemble the sentence. He is assembling it himself and the assembly is exactly the work she came to witness."

    # ========== PHASE 7 -- THE SECOND SENTENCE ==========

    "He is quiet for a count of four. Then:"

    a "I have not paused in a year."

    "The line does not carry a tremor. He is not confessing. He is reporting."

    a "She walked out of our house last week because I am Marcus without the pause."

    "Zira's jaw moves once. Not a reaction to the information. A reaction to the clarity. She has heard him say many things in the year since the funeral. This is the first thing he has said in a long time that has the exact shape of a true thing, spoken aloud, with no armor."

    zthought "He is not going soft."

    zthought "He is saying it because he can see it. That is different. That is harder than going soft."

    zthought "He is seeing the shape of himself with his mother's handwriting in his hand and he is telling me what the shape is. That is a form of honesty the OB Aeron has been rationing since a3_s24. He is spending some of it now."

    # ========== PHASE 8 -- THE SITTING WITH IT ==========

    "He sits with the letter on the table between them. He does not speak for a slow count. The pre-shift silence of the ops room runs its quiet rotation around them. A server rack two rooms over cycles up and cycles down."

    athought "What she wrote is accurate."

    athought "She writes that she cannot love a man who has stopped pausing. I am a man who has stopped pausing. The Aeron who sits in this chair in seven hours and approves the Rhea Vestin mission is a man who will not pause. That is the operative fact."

    athought "The letter is not wrong."

    athought "The letter is also not a key. It is not a door. It is not an instruction to resume pausing. My mother is not here to be obeyed. My mother is here -- was here, fourteen years ago -- to describe the inside of a failure she was watching happen."

    athought "I am inside the same failure."

    athought "Reading her description of it does not exit it. The description is a map of a room. I am standing in the room. Looking at a map of the room I am standing in does not remove me from the room."

    athought "I know this. She would have known I know this. She wrote this to Marcus. Marcus also would have known. That is why she did not send it."

    athought "She did not send it because she knew the sentence would not save him. She wrote it for herself. So that when the day came that she left, she would have written down the hour she had known."

    athought "This letter is the hour she had known. Not a rescue."

    athought "It is archaeology."

    # ========== PHASE 9 -- THE THIRD SENTENCE ==========

    "He looks at Zira. His voice drops a half-step lower. Not softer. Lower."

    a "I am going to keep this."

    "Zira waits."

    a "Not because it changes anything. Because I want to be able to remember that she thought a pause was possible."

    "Her mouth moves once. A small set. She registers the sentence."

    z "And is it."

    "A simple question. Two words. The operator's way of asking the largest possible thing inside the smallest possible container."

    a "No."

    a "Not for me. Not now."

    "The answer comes without hesitation. He has already done the arithmetic. The letter did not produce the answer. The letter arrived at the hour the answer had already been produced."

    # ========== PHASE 10 -- THEN WHY ==========

    z "Then why keep it."

    "He looks at her. The mask does not crack. It holds. But there is a specific clarity in the eyes behind it that Zira has not seen in months. It is not warmth. It is not softening. It is the clarity of a man looking at the exact shape of his own geometry and not turning away from any of it."

    a "Because I want one thing in this room to know the difference between what I am and what I could have been."

    "The sentence sits on the table between them. Next to the letter. Next to the notebook. On top of everything."

    zthought "There it is."

    zthought "That is the sentence I was going to find out whether he could say. I did not know if he could. I have been carrying the envelope for four months partly because I was not sure whether handing it to him would break anything or would just pass through him like every other input on the OB track."

    zthought "He just said it."

    zthought "Not a door. A gravestone."

    zthought "He is going to carry the letter against his chest the way a man carries a gravestone for the self he did not become. And he is still going to plan the assassination in two hours. Both of those things are going to be true in the same body at the same time."

    zthought "That is the OB Aeron I came to see this morning."

    # ========== PHASE 11 -- THE FOLD ==========

    "He picks the letter up. He folds it along its existing fold lines. He does not make a new fold. He respects the ones his mother made fourteen years ago."

    "He slides the page back into the waxed paper envelope. He presses the envelope flat. He looks at it for one beat."

    "Then he opens the inside of his jacket at the left breast -- not the side pocket, the inner chest pocket -- and he slides the envelope in. Flat. Against his chest. The camera holds on the gesture. The envelope disappears inside the jacket. The jacket closes around it. The letter is now in a place the ops room cannot see."

    athought "Against the chest."

    athought "Not the pocket at the hip where I keep the signal jammer. Not the pocket at the waist where I keep the comm. Against the chest."

    athought "Because I want it to travel with me for the same reason a pressed flower travels in a waxed-paper packet. Because some objects are not for use. Some objects are for proof that the person carrying them was once also something else."

    athought "I was once six and my mother thought a pause was possible."

    athought "That fact does not stop the mission."

    athought "That fact is now going with me to the mission."

    # ========== PHASE 12 -- THE RECEIPT ==========

    "He looks up at Zira. The mask is fully back. The sliver of self-recognition is now sealed inside the jacket along with the envelope."

    a "Thank you for bringing it."

    z "Yes."

    a "You held it four months."

    z "Yes."

    a "Why did you stop holding it yesterday."

    "Zira considers her answer. She has considered it all night. She has several versions of it. She picks the one that costs the least to say and still tells the truth."

    z "Because after yesterday I did not want to be the person who had the letter and did not give it to you. If the assassination goes the way I expect it to go, and this letter was still in my jacket when it did, I would have been complicit in a way I am not willing to be complicit."

    z "This letter is yours. It should be on your body, not mine."

    a "Understood."

    "He says the word the way he says it in the war room. A receipt. An acknowledgment. Not gratitude. Not affection. The operator's seal on a transfer of custody."

    # ========== PHASE 13 -- ZIRA ASKS THE LAST QUESTION ==========

    "Zira is about to turn and leave. She has delivered the freight. The hour is almost used. But she stops. She has one more thing she will not get another chance to say."

    z "Aeron."

    a "Yes."

    z "The pause she is describing. The one Marcus stopped having. The one she fell in love with."

    z "Do you remember it. From when you were small. Did you ever see it in him."

    "He holds the question. The room holds the question with him."

    athought "Did I see it in Marcus when I was small."

    athought "The honest answer is I do not remember Marcus pausing. I remember him deciding. I remember the hand going up at the table. I remember the voice flat and the orders final. I do not remember a beat between decision and execution. I was six when she wrote the letter. By the time I was conscious of him as an operator, the pause was already gone. She was watching it leave. I was born into its absence."

    athought "That is its own piece of information. She was mourning a pause I never witnessed. The pause, for me, is a theoretical object. A story my mother tells about a father I only ever met after he had already lost it."

    athought "I have been Marcus without the pause my whole life because Marcus without the pause was the only Marcus I knew."

    athought "The letter is older than me in a sense that matters. It predates my ability to remember any alternative."

    "He looks at Zira. He gives her the only answer he has."

    a "No. I never saw it in him. By the time I was old enough to watch him work, the pause was already something he used to have."

    a "My mother was describing a thing I never witnessed."

    a "That is part of why I am going to keep the letter."

    z "Because it is the only evidence that the pause ever existed."

    a "Yes."

    # ========== PHASE 14 -- ZIRA'S SMALL RECEIPT ==========

    "Zira nods once. Small. She picks up the notebook she brought the envelope in. She does not look at the notebook. She does not need to. The notebook served its purpose. She is taking it with her because she does not leave operational objects in rooms where they do not belong."

    z "I am going to be back in here at 0600 with the rest of the council. I will not mention this to anyone."

    a "I know."

    z "I am not bringing it up again. Not to you, not to anyone. The letter is in your jacket. That is where it lives now."

    a "I know."

    "She holds his eyes for one more beat. Not gentleness. Witness. She is the only person in the base who has read the letter besides him. She is the only person who knows the phrase is now riding inside his jacket. She is recording the hour so that someday -- if the hour matters -- she will be able to say to someone that she was there the morning the letter landed and he put it against his chest."

    zthought "I am not his mother."

    zthought "I did not come in here to ask him to pause. I do not believe he can pause. The letter is not a request. I am clear about that with myself."

    zthought "But I am going to note the hour. For my own ledger. The morning he put his mother's handwriting against his chest and then went and planned the assassination anyway. That is a data point I am going to carry."

    zthought "Aeron without the pause. With the letter against the chest."

    zthought "Both at once."

    zthought "Noted."

    # ========== PHASE 15 -- THE HOLD ==========

    "She turns. She walks to the door. She does not look back. The corridor door cycles once, a soft hiss, and she is gone."

    "Aeron is alone in the ops room. The coffee at his left hand has gone cold. The packet stack at his place is waiting. The day shift will arrive in forty-five minutes."

    "He does not sit yet."

    "He stands at the head of the table with his left hand flat on the wood and his right hand at his side. The letter is against his chest. The jacket is closed. The camera does not move."

    athought "She said 'the pause she is describing.' She said 'from when you were small.' I notice that she asked whether I had ever seen it. She did not ask whether I could do it."

    athought "Zira knows better than to ask me whether I can pause. She has stopped asking me things she already knows the answer to. That is one of the ways she has been staying in this building for a year."

    athought "The letter is inside the jacket. It is going to travel with me into the war room when the council sits. It is going to travel with me to the corridor outside the surgical suite the morning I sign the Rhea Vestin order. It is going to travel with me to the forward position on the assassination day. It is going to be against my chest when I give the go."

    athought "My mother wrote in ink: I can no longer love a man who does not pause."

    athought "I am a man who does not pause."

    athought "And I am going to carry her sentence with me while I do the next thing she cannot love."

    athought "That is the whole content of the letter in my jacket. It is not an exit. It is not a doorway. It is the weight a man puts inside his coat when he has decided to walk a road his mother cannot walk with him."

    athought "She walked out of our house last week."

    athought "The letter is the part of her that stayed."

    athought "It stayed inside a waxed paper envelope for fourteen years and now it is inside a jacket for however long the jacket lasts."

    athought "Thank you, Zira."

    athought "She will never hear that sentence and she does not need to."

    # ========== PHASE 16 -- THE COFFEE ==========

    "He moves at last. He picks up the cold coffee. He drinks it anyway, because the operator does not waste coffee he poured himself, because routine is the skeleton he is still holding up on the days the meat is all decision."

    "He sits down. Head of the table. The coffee goes on the left. The packet stack goes in front of him. The letter is inside the jacket under the packet stack, under everything."

    # Callback: Liora's courier network / 6000 names (a3_s20_the_story_keeper)
    athought "Six thousand names. The network she built to keep them. I am running an operation on the infrastructure she seeded and I did not know it until Zira matched the relay signatures."

    athought "The Ghostline is her ghost."

    "He opens the Ghostline relay log and starts reading."

    "The camera holds on the room for three full beats. The pre-shift silence. The standby terminal. The head of the table with one man at it. The jacket closed over an envelope over a sentence that used to be alive fourteen years ago."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=2, conflict=0)
    $ tp_seed("a4.ob.letter.not_a_door_a_gravestone")
    $ canon_set("ob.liora.letter_in_jacket", True)
    $ canon_set("ob.aeron.pause_as_gravestone", True)
    $ canon_set("ob.zira.delivered_letter_at_0500", True)
    $ canon_set("ob.aeron.mother_describing_a_pause_he_never_witnessed", True)
    $ flag("ob_aeron_read_letter_twice_and_kept_it", True)
    $ flag("ob_zira_witnessed_the_letter_landing", True)
    $ npc_remember("Zira", "brought_liora_letter_at_0500", tone="courier_of_a_gravestone")
    $ npc_remember("Aeron", "letter_folded_inside_jacket", tone="clarity_not_softening")
    $ metric("ob_aeron_self_awareness_reservoir", add=1)
    $ metric("ob_aeron_escalation_tier", add=0)
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s21_the_letter_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after a4_s20 (Noelle erotic deepening). 0500 pre-shift.
#   - Day after Rhea Vestin's strike killed seven named Phoenix operators incl. Siri Ondel.
#   - Day of the council that will schedule the Rhea assassination (a4_s22).
# cann.what_happened:
#   - Zira comes to the empty ops room at 0500 carrying a letter she found four months ago
#     in an undercity Ghostline dead drop. She has been holding it. Yesterday's losses
#     decided her to deliver it.
#   - The letter is a single handwritten page by Liora to Marcus, never sent, dated
#     when Aeron was six. Its key line: "I fell in love with the pause. The moment
#     between the decision and the execution. The moment you used to have, and the
#     moment you have stopped having. I can no longer love a man who does not pause."
#   - Aeron reads the letter twice. He does not soften. He names it precisely:
#     "Marcus never paused. My mother fell out of love with the absence of a pause.
#     That is what this letter is." Then, quieter: "I have not paused in a year.
#     She walked out of our house last week because I am Marcus without the pause."
#   - When Zira asks if the pause is possible for him, he says: "No. Not for me.
#     Not now."
#   - When Zira asks then why keep it, he says: "Because I want one thing in this
#     room to know the difference between what I am and what I could have been."
#   - He folds the letter along its existing fold lines and puts it inside his
#     jacket at the chest. The letter is not a door. It is a gravestone he is
#     willing to carry into the next operation.
#   - Zira delivers the freight and leaves without ceremony. She will not mention
#     the letter again.
#   - Aeron, alone, sits at the head of the table and starts the pre-shift work.
# cann.aeron_state:
#   - OB escalation continues. The letter does NOT soften him. It clarifies him.
#   - He permits himself a sliver of self-recognition (the "could have been" line)
#     which Zira witnesses and then no one witnesses again.
#   - The pause is declared impossible for him. The letter becomes a gravestone
#     he carries inside his jacket on the way to the Rhea Vestin mission.
#   - Key realization: Marcus was already pauseless by the time Aeron could
#     witness him. The pause, for Aeron, is a thing he has only ever known as
#     a description in his mother's handwriting. He is Marcus without the pause
#     because Marcus without the pause was the only Marcus available to him.
# cann.zira_state:
#   - Delivery as small ethical act. She chose the hour she could not be the
#     person who had the letter and had not given it to him.
#   - Trust bump +2. She saw the sliver of clarity and will not mention it again.
#   - She is now the only person in the base who knows the sentence is inside
#     his jacket. She is recording the hour for her own ledger.
# cann.path_tracking:
#   - tp_seed a4.ob.letter.not_a_door_a_gravestone
#   - canon_set ob.liora.letter_in_jacket True
#   - canon_set ob.aeron.pause_as_gravestone True
#   - canon_set ob.zira.delivered_letter_at_0500 True
#   - canon_set ob.aeron.mother_describing_a_pause_he_never_witnessed True
# cann.thematic_flags:
#   - The pause as gravestone, not door. OB register of Liora's inheritance.
#   - "I want one thing in this room to know the difference between what I am
#     and what I could have been." -- OB Aeron's slim permitted self-awareness.
#   - Aeron as Marcus-without-pause by descent: he never witnessed the pause.
#   - Zira as recording witness, not rescuer. Delivery without instruction.
# cann.character_moments:
#   - Aeron reading the letter three times. Folding it along existing creases.
#     Placing it against his chest.
#   - Zira refusing to sit. Standing four feet from the table. Leaving without
#     a farewell.
#   - The mother describing a pause her son never saw in his father.
# cann.callbacks:
#   - a3_s21 (OB Aeron learning Liora is alive)
#   - a3_s24 (Liora refusing to absolve him; walked out of "our house last week")
#   - a4_s05 (Zira's pressed flower: the small kept object against the self)
#   - a4_s13 (the workshop scene where they converted anger into heat)
# cann.block_status:
#   - ANCHOR (OB). Two-hander. Letter handed off. No player choice.
# cann.requires_followup:
#   - The letter inside the jacket as tracked object. Future OB scenes should
#     acknowledge its presence without naming it repeatedly.
#   - Zira's private ledger of "the morning the letter landed" as silent witness data.
#   - a4_s23 (Aeron alone) re-opens the letter. The third read happens there.
