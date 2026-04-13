# =======================================================
# ACT 4 - Scene 13: Protecting Exhaustion (Empathy Path)
# File: a4_s13_protecting_exhaustion_emp.rpy
# Type: GROUP BEAT — council takes a decision from Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s13_protecting_exhaustion_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s13_protecting_exhaustion_emp:
    $ show_timeline("30th of Forge, 390 A.C.", "09:30", "Phoenix Secondary Base — Ops Wing")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Four movements.
    #         (1) Approach: 32mm, handheld, behind Aeron walking into the ops
    #             wing. The camera keeps up with him the way the room used to
    #             keep up with him. This is the last phase of the scene in
    #             which Aeron sets the tempo.
    #         (2) The threshold: 40mm, locked, from inside the ops wing
    #             looking outward. Aeron appears in the doorway. He stops.
    #             The camera does not move. He moves in the frame; the frame
    #             holds him. The stillness is the first beat of the scene's
    #             reversal.
    #         (3) The table: wide, two-shot bias, Selene and Aeron opposite
    #             the ops table with the table between them. During the
    #             framework presentation, the camera tracks slow across the
    #             ops table to the printed sheet Noelle has placed at the
    #             center — her signed framework, Batch A vintage, first real
    #             use. When Zira speaks her line, the camera locks on her
    #             and does not cut until the line finishes.
    #         (4) The walk away: behind Aeron again. Ops wing doorway. The
    #             ops table continuing to run without him in the deep
    #             background. The door does not close for him. He closes it.
    # LIGHTING: Ops wing operational. Overhead strips — full. The holo-table
    #           green wash on everyone's lower face. The lighting is the
    #           same lighting that has been on for 40 hours. It does not
    #           dim for Aeron. The room does not help him.
    # SFX: Ops ambient — tactical display tick, comms relay, datapad taps.
    #      Two one-shots: the soft click when Noelle turns her printed sheet
    #      to face Aeron across the table; the latch of the ops wing door
    #      when Aeron closes it behind himself at the end. No music until
    #      the last beat — one held low string under his walk back to
    #      quarters. Drops under the last line.
    # FX/COMP: THE FRAMEWORK. A single printed sheet. Not a datapad screen.
    #          Printed because it is signed by hand — Noelle's signature at
    #          the bottom, under a short column of headers. The sheet has
    #          been in her jacket since Batch A. It is being placed on the
    #          table for its first operational use.
    #          THE OPS TABLE. The new ops wing table — larger than the war
    #          room table, running holo, covered in tactical layers. Aeron's
    #          usual chair is at the head. The chair is empty when he
    #          arrives. It stays empty. No one has moved to sit in it.
    # BLOCKING: Aeron arrives at the ops wing doorway. The four women are
    #           arranged around the ops table. Selene at Aeron's usual head-
    #           of-table position — not his chair, the one adjacent, stand-
    #           ing. Noelle at Selene's left, also standing, framework sheet
    #           in front of her. Lyra at Aeron's right, standing, reading a
    #           small handwritten note of her own. Zira at the foot, opposite
    #           Selene, arms folded, the one whose geometry says door.
    #           Aeron's chair at the head is empty and conspicuously empty.
    #           When Aeron steps into the room, none of the four move to
    #           greet him. They are at positions. The positions are the
    #           statement.
    # FACE: Aeron — coming in ready to work. The operational mask is on. It
    #       does not survive the first beat. Selene — composed, not cold,
    #       the face of a commander who has drafted a decision and is
    #       delivering it. Noelle — the analytic face, but with the small
    #       tell around the mouth that says she has attached something to
    #       the framework that the framework did not originally contain.
    #       Lyra — looking at Aeron the way you look at a friend who is
    #       about to be told a thing he is not going to like. Kind. Not
    #       soft. Zira — neutral until her line lands, then unguarded for
    #       two seconds and then neutral again.

    # ========= VOICE BASELINE =========
    # EMP cadence. Operational register from Selene, analytic from Noelle,
    # warm-with-edges from Lyra, compressed from Zira. Aeron's voice shortens
    # through the scene — the clipped operational voice from s02 under
    # pressure, trying to reset the room's tempo and failing. Internal
    # thoughts run heavy in the middle of the scene because externally
    # Aeron is being told what is going to happen and he is not being
    # offered the conversation.

    # scene bg_ops_wing_corridor_day with dissolve
    # play ambient "sfx/ambient/ops_wing_full.ogg" fadein 2.0

    # ========== PHASE 1 — THE APPROACH ==========

    "Ten-forty-five. Twelve hours after the letter scene. Eight hours into the oh-six-hundred brief's operational window."

    "Aeron is walking the ops wing corridor with the clean-fast pace of a man who has been running on the fuel of having three specific decisions ready to deliver to the ops table."

    athought "Decision one: Rhea Vestin arrives in Batch A's drop window in under ninety-six hours. We need a Selene-drafted intake plan and a Lyra-drafted cover story and a Zira-drafted contingency for if she turns out to be a plant."

    athought "Decision two: Marcus's six-day adaptation clock is at hour forty-one. That means Noelle's probability curves on his Phase II response need to be locked by fourteen-hundred, because if we are going to pre-empt, we pre-empt tonight."

    athought "Decision three: Tessa's medbay intake rate has tripled in twelve hours and we need to pull someone off ops to go help her or we are going to lose a patient to administrative delay before the day is out. Lyra is the obvious answer but Lyra is on the Rhea draft."

    athought "I have the shapes. I can see all three in a single sweep, and I am going to deliver them in about ninety seconds, and the ops table is going to take the shape of the orders, and the day is going to work."

    athought "This is the thing I am good at."

    athought "This is the thing Selene corrected me for being good at in a4_s02."

    athought "I am going to deliver these three decisions in a way that honors the correction — I will stage them as proposals, not orders, and I will pause after each one so that the table can push back. That is the discipline. That is what shared command looks like at the operational pace I am trying to keep this morning."

    "He is almost at the ops wing door."

    "He adjusts his jacket cuff. He clears his throat — small, automatic. He has not eaten this morning. He is aware of that. He is aware because Tessa has made him aware every morning for a week and the awareness is now an installed subroutine."

    athought "I will eat after the three decisions land."

    "He pushes the ops wing door open."

    # ========== PHASE 2 — THE THRESHOLD ==========

    # scene bg_ops_wing_table_day with dissolve

    "He stops."

    "Not because the room is wrong. Because the room is arranged for a scene that is not the scene he walked in to run."

    "Four women are at the ops table."

    "Selene is standing at the position adjacent to Aeron's usual chair at the head of the table. Not sitting. Not in his chair. Standing. The empty chair at the head is conspicuously empty — no datapad on its arm, no jacket on its back. It has been deliberately unstaged. The absence of staging is the staging."

    "Noelle is at Selene's left, also standing. A single printed sheet is on the table in front of her. He does not recognize the sheet until he sees the signature at the bottom — her hand, inked, the way she signs the documents she does not want digital copies of. The sheet has been in her jacket for most of a week. He has known about the framework since Batch A. He has not seen the sheet placed on a table before."

    "Lyra is at Aeron's right, standing, a small handwritten note in her hand that she is not looking at. She is looking at him."

    "Zira is at the foot of the table, opposite Selene. Arms folded. Face composed. The geometry of her body says: the door to this room is on my side, and I am standing in front of the door."

    athought "Tessa is not here. That is deliberate. Tessa is in the medbay because the decision they are about to make is the decision they do not want her to be seen co-authoring — they will want her plausible deniability intact with me, because Tessa is the one who is going to take me to the medbay later and they do not want me to have a grievance against her when that happens."

    athought "They are thinking twelve moves out."

    athought "This is not a briefing I walked into."

    athought "This is a scene they have already staged and I am the last person to arrive."

    "He does not step fully into the room. He stays at the threshold. The ops wing door is still open behind him."

    a "What is this."

    "He says it evenly. No accusation. The tempo of the three decisions he was going to deliver is already gone from his body. He can feel it leaving. It takes his posture with it — the cuff he just adjusted goes back to being a cuff."

    sel "Come in, Aeron. Close the door."

    # ========== PHASE 3 — THE CLOSING OF THE DOOR ==========

    "He comes in."

    "He closes the door."

    "He does not go to his chair."

    "He stops at a neutral angle to the table — not at the head, not at the foot, the long side opposite Lyra. It is a position that is not his. He is choosing it because taking his chair right now would be claiming a seat in a scene he does not yet know the grammar of."

    athought "They have not asked me to sit. I am not going to sit."

    "Selene speaks first. Her voice is operational register — clean, not cold."

    sel "This is a command decision that was made without you. I am going to present it. Noelle will walk you through the framework it came out of. Lyra and Zira are here as witnesses to the decision and as the two people who will be operationally responsible for enforcing it."

    sel "You are going to disagree with it."

    sel "I want you to let Noelle finish before you disagree."

    sel "After Noelle finishes, you will have the floor. After you have the floor, I will tell you what the decision is."

    "A beat."

    sel "Can you agree to that structure."

    athought "She is asking me to sit still for the presentation of a verdict."

    athought "She is asking me because she knows that if I am asked, I will agree, and the asking is part of the architecture of what she is doing. She is not going to take the decision from me by force if she can take it from me with my consent."

    athought "This is the Selene of a4_s02 under the doctrine of a4_s12a. The teacher who has a sister she cannot save is teaching me something about being led."

    a "I can agree to the structure."

    sel "Thank you."

    "She turns to Noelle."

    sel "Noelle."

    # ========== PHASE 4 — THE FRAMEWORK ==========

    "Noelle picks up the printed sheet and turns it so the text is facing Aeron across the table. The paper makes a soft click as it catches on the holo-table's edge."

    "He reads the top of the sheet upside-down first, then right-side-up as she nudges it forward. The header is her hand. The signature is her hand. The body is typed, but the framework's headers are hers — block capitals, her particular way of making an R."

    "The title line reads: PHOENIX COMMAND SUSTAINABILITY FRAMEWORK v0.4 — APPLIED TO A. VELARIN."

    "His own name."

    athought "Of course. The framework is universal in its draft — the Batch A version I saw last week had placeholder variables. She has filled in my variables."

    athought "She has made a model of me."

    athought "She made the model with my cooperation. I signed off on the framework being used on the team as an operational tool. I am now reading the instance of that tool turned on me."

    athought "That is not a violation. That is the terms I agreed to."

    athought "Reading it upside-down first was the instinct of a commander looking for the tactical error. Reading it right-side-up is the instinct of a man reading a diagnosis."

    "Noelle speaks. Her voice is analytic register — the one she uses for briefings, not for the personal mode she had in Batch A."

    n "The framework takes six inputs. Resting heart rate, sleep debt, decision latency in operational settings, affective flatness score, the 'cuff adjustment' tell —"

    "(Aeron's jaw tightens a fraction.)"

    n "— and what I have been calling the 'rule-of-three fracture' metric. That last one is the count of times per twenty-four hours that your internal protective rituals are breaking under pressure. I have been getting that metric from Tessa. She does not know I am using it in the framework. I am telling you now because you are entitled to know."

    athought "She has been triangulating my breakdown from three LIs without telling me. On the framework I approved. Which is the correct use of the framework. I am not going to argue with that."

    n "The framework produces a single scalar output — the estimated number of hours until a command-critical failure. The scalar has a confidence interval. For you, as of oh-nine-thirty this morning, the central estimate is fifty-seven hours. The lower bound is forty-one. The upper bound is seventy-three."

    n "All three numbers are less than the seventy-two hours remaining in the Phase II operational window."

    n "That is the framework's output. That is what the model says."

    "A beat."

    n "The model has one known weakness. It underestimates the recovery rate of commanders who have recently been given access to a grief structure they trust. I have been watching for that recovery signal in you. I have not seen it. You had a grief-structure-access event with Tessa at a4_s05a. You had another with Lyra at a4_s04 and with Selene at —"

    "Noelle stops. The smallest pause. The pause is not analytic. It is the pause of a woman who has not been told about the scene in Selene's quarters last night but who has felt something in the room this morning that she cannot fit into a variable and is refusing to guess about in public."

    n "— with Selene at multiple points this act. None of those events have produced the recovery signal at the magnitude the framework requires for the scalar to shift. The framework is producing the fifty-seven-hour number because the recovery signal is not there, not because the grief-structure access did not happen."

    "She looks at him."

    n "I am telling you all of this because the framework is not a judgment and I do not want you to receive it as a judgment. It is a prediction. Predictions are wrong sometimes. The fifty-seven hours is what the model produces given the inputs I can measure. You have always been more than what I can measure. That is the model's known limitation and it is not going to stop being a limitation by being ignored."

    "A beat."

    n "I would like the decision the team is about to present to you to be understood as a correction applied to the framework's prediction, not as a punishment of you."

    athought "Noelle is doing something I have never seen her do before."

    athought "She is defending the decision in advance by pre-empting the frame I was going to use to refuse it. She is saying: before Aeron calls this punitive, let the record show it is corrective."

    athought "She has been thinking about how I am going to hear this for — a while. Hours, probably. Last night, probably."

    athought "I am not going to be able to argue the framework. The framework is mine. I approved it. I am in it now as a data point and I do not get to object to being measured by a tool I consented to."

    # ========== PHASE 5 — THE DECISION ==========

    "Selene takes a breath. Not a dramatic one. A work breath."

    sel "The decision."

    sel "Aeron Velarin is on a forty-eight-hour operational stand-down, effective ten-forty-five, this morning."

    sel "You are removed from the ops table for that window. You are removed from real-time decision authority on Phase II. You retain access to intelligence briefings on a read-only basis. You retain your comms. You retain the ability to contact any of us at any time for non-operational reasons. You do not retain the ability to issue operational orders for forty-eight hours."

    sel "At the end of the stand-down, if Noelle's framework indicates recovery, you resume full authority. If it does not, we have a longer conversation and the stand-down extends."

    sel "Enforcement: Lyra and Zira. Lyra because she is the person in this room you are least likely to refuse directly, and Zira because she is the person in this room whose no you have spent three acts learning to hear. Tessa is not part of the enforcement structure because Tessa is the person you are going to see in the medbay during the stand-down if your resting heart rate does not come down, and I do not want her enforcement role to compromise her clinical role."

    sel "The decision is active. It does not need your approval. I am telling you because you are a co-commander and you are entitled to be told, in the room, by the people who made it."

    "She looks at him."

    sel "Do you want the floor now."

    # ========== PHASE 6 — THE FLOOR ==========

    "Aeron takes the floor."

    "His voice is the clean-fast voice. Under it he can hear the other voice — Marcus's voice, the First Principle, the command reflex. He is not going to let that voice speak for him. He is going to let the voice under that voice speak."

    a "I have three decisions ready to deliver to this table."

    "He lists them. Fast. Rhea Vestin intake, Marcus adaptation curve lock, medbay intake surge."

    a "All three are time-critical inside the seventy-two-hour window. Rhea lands in ninety-six, not seventy-two — the intake plan has to be locked in the next twenty-four or we will be drafting in the middle of her arrival window. Marcus's curve locks by fourteen-hundred. The medbay problem is not going to wait past this afternoon."

    a "If I stand down for forty-eight hours, the Rhea plan gets drafted by Selene and Lyra without my input, the Marcus curve gets locked by Noelle without my read, and the medbay problem gets solved by whoever Tessa pulls for it without my sign-off. Those are three decisions that normally come through me and will not come through me for forty-eight hours."

    a "My objection is not that I should not rest. I hear the framework. I am not arguing with the framework. My objection is operational tempo. Can the stand-down be twenty-four hours instead of forty-eight. Can the first twelve of it be this afternoon and the next twelve be after I deliver the Rhea draft. Can we compress."

    "He lays it out the way he lays out a counter-proposal. Clean, numbered, with fallbacks."

    "He is not wrong. The operational tempo points he is making are real. The Rhea draft is genuinely time-critical. The Marcus curve lock is genuinely fourteen-hundred."

    "He is also, he can feel it in his mouth, fighting the decision."

    # ========== PHASE 7 — THE RESPONSES ==========

    "Selene does not respond first."

    "Noelle does."

    n "I ran your counter-proposal as a variant through the framework an hour ago. I expected you to make it."

    n "A twenty-four-hour stand-down with compression produces a central estimate of sixty-eight hours to command-critical failure, with a lower bound of fifty-one. The compression does not purchase you enough recovery to offset the operational cost of the second twenty-four hours of grinding. The model says the twenty-four-hour variant is worse than either the forty-eight-hour stand-down or the zero-hour status quo."

    n "I am telling you this so that you do not spend the next ten minutes negotiating a compromise that the framework has already rejected."

    "A beat."

    n "I am sorry. I know that sounds cold."

    a "It does not sound cold. It sounds like the framework doing what it is supposed to do."

    "He means it. He is not going to make Noelle carry the wrong affect on this."

    "Lyra speaks next. She has not moved from her position at his right."

    l "I drafted the Rhea intake plan last night. The draft is on the ops table — Selene has a copy, Zira has a copy, I have the working copy. I was going to give it to you this morning before the brief. It does not need you in the room to be finalized. It needs you to read it and approve it when you come back, and I would rather you come back at hour forty-eight and read it once than stay in the room for the next twenty-four and read it four times with a heart rate of one hundred and six."

    l "The medbay intake problem is being solved. Tessa is pulling two of the Sector 7 walk-ins who have nursing training and is going to have them on floor duty by fourteen-hundred. She does not need a sign-off from you. She needs you to not be in the medbay at fifteen-hundred second-guessing her assignments."

    a "Lyra—"

    l "I am not done."

    "Her voice is kind. It is also the voice she used to intercept Noelle on the balcony at the gala. The voice that does not defuse — the voice that holds."

    l "You have been asking me to be the person who tells you when the room has become a weapon. You said that to me at a3_s23. You asked me specifically, because I am the person who will not say it in the wrong register."

    l "The room is becoming a weapon, Aeron. Not your weapon. A weapon against you. You have been running it at a tempo that is going to break you inside of sixty hours and the breakage is going to cost us Rhea's intake, Marcus's curve, and the medbay, and also you, which I am listing last because the other three are the ones you would list first if you were in a position to list them."

    l "I am telling you the room has become a weapon. I am telling you because that is the promise I made."

    "She stops."

    athought "Lyra is invoking her own standing trust instrument. She is cashing the a3_s23 promise. The exact shape of the cashing is the cleanest move in the scene — she is not appealing to my emotion, she is appealing to my prior commitment to her."

    athought "I am going to have to honor that or be the kind of man who breaks a trust instrument at the first time it is used on me."

    "Noelle has gone still in that particular way she goes still when something she did not predict happens in the room. Her eyes are on Lyra, not Aeron. She is registering that Lyra has just done the most effective possible thing, and she is filing the technique."

    # ========== PHASE 8 — ZIRA'S LINE ==========

    "Zira has not moved from the foot of the table."

    "Her arms are still folded. Her face has been neutral through the entire scene."

    "She speaks now. Quiet. Not louder than the ops ambient."

    z "Aeron."

    "He looks at her."

    z "You told me the door exists."

    "A beat."

    # VISUAL: Camera locks on Zira. Hold.

    z "At a1_s08, in the bedroom, after the gala. You said — and I remember the exact shape of the sentence because I have been holding it for a very long time — you said that if I ever needed to leave, the door existed, and you would open it for me."

    z "You said it about my door. The door out of whatever room I was in that I did not know how to leave."

    "Her voice is level. It is also, for two seconds, not the voice of the Zira who runs the ghost network. It is the voice of a woman who has been carrying a sentence for three acts and is using it once, in public, for the exact thing it was built to be used for."

    z "This is the door."

    z "The room you do not know how to leave is this one. The ops table. The seventy-two-hour window. The fifty-seven hours to command-critical failure. You do not know how to leave it because leaving it feels like abandoning the three decisions you brought in here this morning."

    z "Open the door."

    z "Open it for forty-eight hours."

    "Another beat."

    z "I am asking for the promise you made me. The shape of the ask is — I am asking you to accept from us what you once offered to me. I do not have a way to make the ask other than this. I do not want to make it in a room with this many witnesses. I am making it here because here is where the scene is."

    "She unfolds her arms."

    z "Please."

    "The word is small. It is not a Zira word. Zira does not say please for operational decisions. Zira says please for exactly one kind of ask — the kind that is really about the person asking, not about the person being asked."

    athought "She is using the door on me."

    athought "She is using the door I gave her. The door I held open for her for three acts."

    athought "She is giving me back the exact instrument I made for her. She is saying: you built this. You built it for me. You were right that the door existed. I am showing you that you were right by pointing at it and telling you to walk through it."

    athought "The asymmetry of the ask is the whole structure. I cannot refuse Zira the thing I offered Zira. If I refuse her here, I have un-made the offer retroactively, and the entire shape of what I was to her in a1_s08 collapses backward through every Zira scene in every act, and the collapse is not a thing I am willing to let happen."

    athought "She knew that. She knew it when she picked this line. She has been holding it for exactly this."

    # ========== PHASE 9 — THE YES ==========

    "Aeron looks at the four of them."

    "Selene at the head. Noelle with her framework. Lyra with her cashed promise. Zira at the door, literal and metaphorical."

    "Behind all four of them, Tessa, not in the room, in the medbay, deliberately absent, so that tonight's medbay visit is clean and the enforcement is clean and the clinical relationship does not get contaminated."

    "Behind Tessa, the scene at a4_s05a where she intercepted him in the corridor and said: your body is not a resource to be spent."

    "Behind that, his mother in the rain a month ago saying don't let me become what I'm fighting."

    "Behind that, the Aeries training, the First Principle, the voice of Marcus telling him the decision belongs to the one who sees it first."

    "He hears the voices in order. He sorts them. He hears Marcus's voice last, because Marcus's voice is loud and he has been getting better at hearing his own voice under it."

    "His own voice is very quiet this morning."

    "It says: they are right."

    "He says the thing out loud that his quiet voice is saying."

    a "Yes."

    "One word. Not 'agreed.' Not 'acknowledged.' Not 'confirmed.' Yes — the smallest possible affirmative, because anything larger would be a performance and the room does not need a performance."

    a "Forty-eight hours. I accept the stand-down."

    "A beat."

    a "Thank you for making it without asking me. I would not have agreed to it if you had asked."

    sel "We know."

    a "I want you to note that I know you know."

    sel "Noted."

    "A small corner-of-mouth move from Selene. The same move from a4_s12a, twelve hours later, in a different room, in front of witnesses. He sees it. He files it."

    # ========== PHASE 10 — THE HANDOFF ==========

    "Noelle slides the framework sheet back across the table toward herself and folds it. She does not put it back in her jacket. She holds it in her hand as if she is not sure yet where it goes."

    "Lyra steps forward and hands him the Rhea draft — not to approve, to read when he comes back. Handwritten margin notes already in Selene's hand on the first two pages."

    l "Read it on Wednesday. Not tonight. Not tomorrow."

    a "Understood."

    "Zira re-folds her arms. Her face is back to neutral. The please has left her mouth and taken its weight with it. But her eyes are on Aeron the way they are on an operation she has personally signed for."

    "Selene speaks."

    sel "You are dismissed from the ops wing, Commander."

    "She uses the title. Not to be formal — to mark the boundary. Commander Velarin, who is not the commander for forty-eight hours, is being dismissed from the room that belongs to the commander he is not being for forty-eight hours. The grammar is precise."

    sel "Go to your quarters. Sleep if you can. If you cannot, do not come back here. Go to the medbay. Tessa is expecting you if you need her."

    a "Understood."

    sel "Aeron."

    a "Yes."

    sel "One more thing."

    sel "This is not punitive. I need you to walk out of this room knowing that."

    a "I know it is not punitive."

    sel "Say it back to me in a sentence you have built yourself. I do not want to take the framework's word for what you heard."

    "He thinks for a second. He wants to say the sentence correctly. He is not going to perform it."

    a "You took the decision of when I am allowed to stop away from me, because you could see that the decision was not going to come from me in time, and taking it was the last honest move available to the people who are building the command with me."

    "A beat."

    a "It is not a punishment. It is a transfer of authority over a question I was no longer answering honestly."

    "Selene's eyes move."

    sel "That is the right sentence."

    sel "Go."

    # ========== PHASE 11 — THE WALK ==========

    "He turns."

    "He walks to the ops wing door."

    "The ops table behind him is already continuing. Noelle is turning to the holo. Lyra is pulling a new sheet. Selene is saying something to Zira about the Rhea timeline. Their voices find operational cadence within seconds of him moving — the room does not wait for him to leave before becoming the room that runs without him. It is already running without him. His absence was always going to be the shape the room took when he walked out of it, and the room is demonstrating that the shape is viable."

    athought "They are operating."

    athought "The room is operating without me and it is operating correctly and the correct operation is going to continue for forty-eight hours whether I am in my quarters or in the medbay or asleep or awake or dead or alive."

    athought "That is the thing I have been refusing to let myself believe for three acts. That the room is not contingent on my presence. That the work does not collapse if I step out of it."

    athought "The room is going to operate."

    athought "Selene drafted the stand-down. Noelle modeled it. Lyra cashed the trust instrument. Zira used the door. Tessa abstained from the scene so her clinical role would stay clean. Four women arranged a move that was architected to be impossible for me to refuse without un-making every commitment I have made to any of them."

    athought "That is not a punishment. That is a demonstration."

    athought "They have demonstrated that shared authority includes the authority to tell me when I am allowed to stop, and to take that question away from me when I am not answering it."

    athought "And they are doing it in a way that does not sneer at me, does not humiliate me, does not make me small. They staged it with my consent to the structure, with my framework as the instrument, with my own prior promises as the levers."

    athought "This is the most carefully made move I have ever had made against me. And it was made for me, by people who love me, in a register I cannot argue with because the register is a register I taught them."

    "He reaches the door."

    "He puts his hand on the door. The metal is cool under his palm. The ops wing is five degrees warmer than the corridor beyond it and the difference is on his skin."

    "He opens the door."

    "He does not look back."

    "He closes the door behind him — all the way. The latch catches."

    # ========== PHASE 12 — THE CORRIDOR ==========

    # scene bg_ops_wing_corridor_day with dissolve

    "The corridor is cold after the ops wing. The overheads are the base overheads — cold blue, not the green wash of the holo-table. His face reads the temperature drop as a physical event. He has been in the ops wing for about twelve minutes. He had expected to be in it for the next six hours."

    "He starts walking."

    "He is walking toward his quarters. Not the medbay. Not the corridor-he-walked-last-night outside Selene's door. His own quarters, because the scene sent him there and because he does not have the operational authority to overwrite the instruction with a different route."

    "He walks slowly."

    athought "I am not sprinting. I am noticing that I am not sprinting."

    athought "I am noticing because for forty hours I have been walking the corridors of this base at a pace that is not a walk and not a run but a sustained operational transit, and the transit has been the shape of my body since Phase II opened."

    athought "The transit has stopped. I am walking at the speed of a person who has been told he has nowhere to be for forty-eight hours, and my body is one full octave slower than it was eight minutes ago, and the octave change is registering as a kind of static in my chest that I do not know what to do with yet."

    athought "That is the stand-down taking effect. Already. Before I have reached my quarters. The body believes it, before the mind has finished arguing with it."

    "He passes the medbay. The door is closed. Tessa is inside. She knows he is walking past. She does not come out. She is holding to the plan — the enforcement roles are Lyra and Zira, and Tessa's role is the one that starts when his heart rate tells her to start it and not before."

    athought "Tessa is doing the patient thing. Tessa is letting me walk past her medbay door without intercepting me because the staging requires her to let me walk past."

    athought "I see her abstention. I am going to remember that she abstained."

    "He passes Selene's door. It is closed now. The latch caught last night when he left. The inch is gone. The warm lamp is presumably still on the desk inside, but he does not see it from the corridor."

    "He passes Lyra's quarters."

    "He passes Noelle's."

    "He reaches his own door."

    "He puts his hand on the handle."

    # ========== PHASE 13 — THE ROOM ==========

    # scene bg_aeron_quarters_day_empty with dissolve

    "His quarters are not large. The bunk is made — he made it this morning on autopilot. The desk has a datapad on it, still powered, the screen showing the decision brief he was going to deliver at the ops table ninety minutes ago. The brief is now a historical document."

    "He does not sit on the bunk."

    "He sits on the desk chair."

    "He looks at the datapad."

    "After a long moment, he closes the brief. Not deletes it — closes it. The brief goes into the archive. Rhea Vestin's name is on it. Marcus's name is on it. The medbay intake problem is on it. The three decisions that were going to be his voice in the room this morning are now three decisions that are going to be other people's voices. He does not believe the decisions are going to come out wrong. He believes they are going to come out different."

    athought "Different is not wrong."

    athought "Different is the thing I have been refusing to count as acceptable for three acts."

    athought "I am going to have to learn to count it."

    "He leaves the datapad on the desk."

    "He stands up and walks to the bunk."

    "He sits on the bunk — the edge of it, boots still on."

    "He does not lie down yet."

    "He puts his hands on his knees. He looks at his hands."

    athought "I have been running on the assumption that the room collapses without me."

    athought "The room does not collapse without me."

    athought "The room is operating without me right now, twenty meters and one closed door away, and it is operating because four women who I love and who love me back built a forty-eight-hour scaffolding in the last twelve hours while I was walking through the officers' corridor mistaking an inch of light for an accident."

    athought "I am going to lie down."

    athought "I am not going to sleep, probably. I am not ready to sleep yet. But I am going to lie down, because lying down is the smallest correct move, and I am only making correct moves right now because I no longer have authorization to make the bigger ones."

    "He unlaces his boots."

    "His hands are tired. The laces are the elaborate mechanical problem they were at a4_s05a. He gets through them."

    "He lies down on the bunk."

    "The ceiling of his quarters has a water stain in the upper-left corner that he has never had time to look at before. He looks at it now."

    athought "I have never seen that stain."

    athought "I am going to look at it for a minute."

    "He looks at it for a minute."

    "The ops wing, twenty meters away, continues to run without him. The medbay, fifteen meters away, continues to run without him. Selene's quarters, thirty meters away, hold a woman who will be reading his oh-six-hundred brief on a read-only feed in her office at fifteen-hundred because she has taken the decisions he was going to make and is now making them correctly, with Lyra and Noelle, and Zira is watching the door while she does."

    "The base holds its shape around his quarters."

    "His quarters hold him."

    "The water stain on the ceiling is the shape of a small animal he cannot name."

    "Fade."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=1)
    $ rel_bump("Noelle", trust=1)
    $ rel_bump("Lyra", trust=1)
    $ rel_bump("Zira", trust=2)
    $ flag("a4_council_forced_stand_down", True)
    $ flag("a4_aeron_accepted_stand_down", True)
    $ flag("a4_noelle_framework_first_operational_use", True)
    $ flag("a4_lyra_cashed_a3s23_trust_instrument", True)
    $ flag("a4_zira_cashed_a1s08_the_door", True)
    $ canon_set("phoenix.decision.stand_down_48", "active")
    $ canon_set("aeron.authority.read_only_48h", True)
    $ canon_set("a4.tessa.deliberate_abstention_from_council", True)
    $ npc_remember("Selene", "drafted_the_stand_down", tone="command_as_care")
    $ npc_remember("Noelle", "presented_framework_on_aeron", tone="analytic_defense")
    $ npc_remember("Lyra", "cashed_the_a3s23_promise", tone="gentle_enforcement")
    $ npc_remember("Zira", "used_the_door_on_him", tone="promise_returned")
    $ npc_remember("Aeron", "walked_out_of_ops_wing_on_stand_down", tone="accepted_delegation")
    $ tp_seed("a4.council.protects_aeron")
    $ tp_seed("a4.door.opens_the_other_way")
    $ metric("aeron_forced_stand_down", set_to=1)
    $ metric("aeron_ops_authority_active", set_to=0)
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s13_protecting_exhaustion_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Ten-forty-five, morning after a4_s12a (the letter scene). 40+ hours
#     into Phase II. The four women in Aeron's command circle make a
#     decision without him and present it.
# cann.what_happened:
#   - Aeron walks into the ops wing with three time-critical decisions ready
#     to deliver (Rhea Vestin intake, Marcus adaptation curve lock, medbay
#     intake surge). He finds Selene, Noelle, Lyra, and Zira arranged
#     around the ops table. His chair at the head is conspicuously empty
#     and unstaged. Tessa is deliberately absent — in the medbay — to
#     preserve her clinical role separate from enforcement.
#   - Selene presents a command decision that was made without him. She
#     asks him to agree to a structure: Noelle presents a framework, he
#     gets the floor, then Selene delivers the decision. Aeron consents to
#     the structure.
#   - Noelle walks him through the applied Sustainability Framework v0.4.
#     Six inputs including the 'cuff adjustment tell' and a 'rule-of-three
#     fracture' metric she has been sourcing from Tessa. The framework
#     outputs a central estimate of 57 hours to command-critical failure
#     for Aeron, lower bound 41, upper bound 73 — all less than the 72
#     hours remaining in the Phase II window. Noelle pre-empts Aeron's
#     expected objection by naming the framework's known weakness
#     (recovery signal under-count) and explaining why she has not seen
#     the recovery signal despite the grief-access events with Tessa,
#     Lyra, and Selene.
#   - Selene delivers the decision: 48-hour operational stand-down, read-
#     only intelligence access only, no operational orders. Enforcement
#     by Lyra and Zira. Tessa reserved for the clinical role. Active on
#     announcement, not contingent on his approval.
#   - Aeron takes the floor and proposes a 24-hour compression. Noelle
#     reports she pre-ran his counter-proposal an hour earlier — the 24-
#     hour variant models worse than either the 48-hour stand-down or the
#     zero-hour status quo.
#   - Lyra cashes the a3_s23 trust instrument: "You asked me to be the
#     person who tells you when the room has become a weapon. The room has
#     become a weapon." She notes she has already drafted the Rhea intake
#     plan and that Tessa has the medbay surge covered.
#   - Zira delivers the scene's hinge line: invokes the a1_s08 bedroom
#     scene ("the door exists, and I will open it for you") and uses it
#     on Aeron. "This is the door. Open it for 48 hours." She says please
#     — a Zira please, meaning the ask is really about her.
#   - Aeron accepts. "Yes. Forty-eight hours. I accept the stand-down."
#     He asks to note that he knows they knew he would not have agreed if
#     they had asked him. Selene: "Noted."
#   - Selene formally dismisses him ("Commander" used as a boundary-
#     marking grammar, not a rank performance) and asks him to restate in
#     his own sentence what has happened. Aeron: "You took the decision
#     of when I am allowed to stop away from me, because you could see
#     that the decision was not going to come from me in time, and taking
#     it was the last honest move available to the people who are building
#     the command with me. It is not a punishment. It is a transfer of
#     authority over a question I was no longer answering honestly."
#   - He walks out. The ops table is already running without him before
#     he reaches the door. He walks the corridor past the medbay (Tessa
#     holding abstention), past Selene's closed door, past Lyra's, past
#     Noelle's, to his own quarters. He closes the decision brief on his
#     datapad, lies down on his bunk with boots unlaced, and looks at a
#     water stain on the ceiling he has never had time to look at before.
# cann.aeron_state:
#   - First time in Act 4 that authority is transferred away from him by
#     force rather than delegated by him. The structural answer to s10's
#     "delegate the question" — the team is now delegating the question
#     of when Aeron is allowed to stop, and they are delegating it away
#     from him.
#   - He accepts inside a correctly built architecture. The architecture
#     uses his own prior commitments (framework consent, a3_s23 promise
#     to Lyra, a1_s08 promise to Zira) as levers. He cannot refuse without
#     un-making those commitments.
#   - Internal acknowledgment: "The room is not contingent on my presence."
#     This is the thesis beat of the scene. He has been running on the
#     opposite assumption for three acts.
#   - Body note: he notices his own slower walk in the corridor. The stand-
#     down registers in his autonomic system before his conscious mind
#     fully agrees to it.
# cann.council_state:
#   - Selene (drafter): command-as-care mode, not teacher mode. The
#     architecture is hers. She is modeling shared authority in its
#     hardest register — the authority to stop your co-commander.
#   - Noelle (analyst): first real operational use of her signed
#     framework. The framework is Batch A vintage. She pre-empts Aeron's
#     objection with the recovery-signal caveat, showing she has
#     developed a meta-awareness of her own tool's limitations — this is
#     a noticeable growth beat for her.
#   - Lyra (enforcer-by-promise): cashes the a3_s23 trust instrument.
#     The "room has become a weapon" line is the exact move he commissioned
#     her to make. She has already drafted the Rhea intake plan, meaning
#     she was thinking operationally about this as far back as the previous
#     night.
#   - Zira (door-holder): cashes the a1_s08 "the door exists" offer.
#     Says please once. This is rare enough that Aeron internally
#     registers it as the marker of a personal, not operational, ask.
#     The asymmetry of the ask — using his own offer back on him — is
#     the unrefuseable move.
#   - Tessa (abstained): deliberately not in the room. Clinical role
#     preserved. Aeron registers her abstention and files it.
# cann.thematic_flags:
#   - Shared authority includes the authority to tell the commander when
#     he is allowed to stop. The Act 4 thesis in its sharpest form.
#   - Prior commitments as levers: framework consent, promises to Lyra
#     and Zira. Aeron is being held accountable by his own past honesty.
#   - The door metaphor inverted: Aeron built the door for Zira; Zira now
#     opens it for Aeron. True-Path-adjacent reversal of the a1_s08 scene.
#   - "Can I lead without turning leadership into a weapon?" — the scene
#     demonstrates that accepting the answer sometimes requires being the
#     one who is led. Leadership as the capacity to be led.
#   - The room operates without him. The assumption of contingent command
#     is broken in real time.
# cann.callbacks:
#   - a1_s08 (bedroom after the gala): Zira's "the door exists, I will
#     open it for you" promise. Cashed here, reversed, turned on Aeron.
#     The cashing is the scene's hinge.
#   - a3_s23 (the plan, Lyra's trust instrument): Aeron asked Lyra to be
#     the person who tells him when the room has become a weapon. Cashed
#     here for the first time.
#   - a4_s02 (first cracks, war room correction): Selene's first
#     correction in public. This scene is the structural escalation —
#     from "you made the call alone" to "we have made the call without
#     you." The same architecture applied at a larger scale.
#   - a4_s04 (Lyra unbuckled): "presence is enough" vocabulary. Here
#     Lyra's presence at the ops table is the enforcement.
#   - a4_s05a (Tessa care-as-command): "your body is not a resource to be
#     spent." This scene is the council-scale version of that intervention.
#     Tessa's deliberate abstention preserves her clinical role so the
#     relationship that said that line is not compromised by being part of
#     the enforcement structure.
#   - a4_s06 (Tessa's silent board): the grief-structure-access events
#     Noelle mentions in her framework presentation.
#   - a4_s10 (delegate the question, Batch B/C parallel): Selene's
#     doctrine of delegation. This scene is the doctrine turning back on
#     Aeron — his own students delegating the question of his stopping
#     back to themselves.
#   - a4_s12a (the letter scene): Selene's unguarded moment twelve hours
#     earlier. The small-corner-of-mouth move returns here. The scene
#     quietly acknowledges that the decision-drafting happened at least
#     partly in those hours.
#   - Batch A s09 (Noelle's signed framework draft): first operational
#     use of the framework. Flag recorded for downstream reference.
# cann.character_moments:
#   - Aeron: the cuff adjustment at the ops wing door (Noelle calls it
#     out), the floor-taking counter-proposal that Noelle has already
#     modeled, the 'yes' as the smallest possible affirmative, the
#     restatement Selene asks for, the walk to his quarters, the water
#     stain.
#   - Selene: drafting this architecture in the twelve hours after the
#     letter scene. The corner-of-mouth small-move. "That is the right
#     sentence. Go." Using 'Commander' as a boundary grammar.
#   - Noelle: the framework on the table, the pre-empted counter-
#     proposal, the moment of stillness when she registers Lyra's move
#     as more effective than her own. "I am sorry. I know that sounds
#     cold." The framework as analytic defense of a loving act.
#   - Lyra: the drafted Rhea plan in her hand, the cashing of the a3_s23
#     promise, the voice that holds. "I am not done."
#   - Zira: the please. The door opened in the reverse direction. Three
#     acts of carrying a sentence used once.
#   - Tessa (off-screen): deliberate abstention registered by Aeron.
# cann.block_status:
#   - LINEAR. No branching. No player choice. EMP path only.
# cann.requires_followup:
#   - The stand-down is active for 48 hours. Any Act 4 Phase II scene
#     occurring in that window must honor Aeron's read-only authority.
#     He cannot issue operational orders. He can receive intel. He can
#     contact any of the LIs. He cannot run the ops table.
#   - Noelle's framework is now an operational tool that has been used
#     once. Any future use of it should reference this scene as the
#     precedent. The framework's known weakness (recovery signal) is
#     also canonical now.
#   - a4_s13a (Noelle intimacy insert during the stand-down) is set up
#     directly by this scene. The framework has worked; Noelle has data
#     she does not know how to weight.
#   - Zira's use of the a1_s08 door is a locked True Path marker. Any
#     future Zira scene should treat this as a canonical event in their
#     shared history.
#   - Lyra's cashing of a3_s23 is likewise locked. The trust instrument
#     has been used once; future uses should carry the weight of the
#     precedent.
#   - tp_seed a4.council.protects_aeron and a4.door.opens_the_other_way
#     accrue toward the True Path. The latter is the reversal-marker
#     that the Phase II architecture has begun to flow in both directions.
