# =======================================================
# ACT 4 - Scene 22: Council of Attrition (Obedience Path)
# File: a4_s22_council_of_attrition_ob.rpy
# Path: OB
# Type: COUNCIL / DECISION BEAT
# Character Focus: Aeron, Lyra, Zira, Tessa (cond.), Noelle, Nyra
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s22_council_of_attrition_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s22_council_of_attrition_ob:
    $ show_timeline("DAY 54", "08:30", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. OB grammar. Formal council composition. Open wide on
    #         the war room: long dark table, Aeron at the head, the others around
    #         it. Then a series of medium one-shots as each LI answers. Each
    #         answer gets its own locked frame. The camera does not pan between
    #         them. It cuts. The cuts are the geometry of a council where each
    #         person delivers a fragment and no one argues with any other
    #         person's fragment. That is the horror: it is not a debate. It is
    #         a parade of consent.
    #         The final wide, when Aeron authorizes the mission, is shot from
    #         behind him looking down the table. We see the backs of nobody's
    #         heads. We see the faces of the five others in a single frame with
    #         the day's packet stack between them. Aeron's shoulder is in the
    #         near foreground. This is the OB mirror of the EMP s21 shot where
    #         the council refused to preempt. Same composition. Opposite answer.
    # LIGHTING: War room overheads at full. Cold white. The map overlay on the
    #           table is dormant. A single warm amber from the standby tactical
    #           display on the far wall. The warmth is decorative. It does not
    #           reach the faces.
    # SFX: Loop -- war room ambient. HVAC. Server racks. No external chatter.
    #      The door is sealed. One-shots -- each LI's chair when they speak
    #      (a small creak, specific to each). The day's packet when Aeron
    #      opens the Rhea file (paper rustle). The calendar entry committing
    #      (a single terminal chime -- low, one note). No music.
    # FX/COMP: The war room: the scar of the last twelve months is visible in
    #          the table -- a coffee ring that was not wiped, a nick at the
    #          head chair from where Aeron set a magazine down too hard three
    #          days ago. The map overlay holds the Solveil operating area.
    #          Rhea Vestin's last known node locations are marked in red at
    #          the north-east quadrant. The red is small. The red is exact.
    #          Tessa's chair: depends on branch. Branch A -- she is seated.
    #          Branch B -- her chair is empty. In branch B the camera notes
    #          the empty chair in the establishing wide and then does not
    #          return to it. Nobody acknowledges it verbally. The absence
    #          is a data point the scene refuses to process aloud.
    # BLOCKING: Aeron at the head. Nyra at his right (co-command). Zira at his
    #           left (operational ground). Lyra across from Nyra (ritual).
    #           Noelle across from Zira (prediction). Tessa (branch A) at the
    #           foot of the table opposite Aeron (medical). Branch B: the foot
    #           chair empty.
    #           No one stands during the scene. No one paces. This is a seated
    #           council and the seated-ness is the point. They are signing off
    #           on an assassination with their bodies held still. That is the
    #           aesthetic of Violence Normalized: everyone contributes from
    #           their chair.
    # CANON: COUNCIL OF ATTRITION. The OB mirror of EMP a4_s21. EMP's council
    #        refused to preempt and moved civilians instead. OB's council
    #        decides the opposite -- they authorize an assassination mission
    #        against Rhea Vestin personally. Named target. Seven days out.
    #        Each LI speaks once. Each answer is fractionally different and
    #        therefore devastating. The scene ends with the mission scheduled
    #        into Act 5. The act will end before the mission executes.
    # FACE: Aeron -- mask. Marcus idiom tightening. Competent in a way that
    #        is no longer performance. The letter against his chest is not
    #        visible and will not be mentioned.
    #        Lyra -- the face of a woman who has decided the ritual cost of
    #        her own complicity. Steady. A little grey under the eyes.
    #        Zira -- the face of a woman who has been pre-planning this for
    #        a month and is now saying so.
    #        Noelle -- the weapon-track face from a4_s20. Cold and exact.
    #        Tessa (A) -- medical register. Two words. That is her whole
    #        contribution. (B) -- not present; camera does not editorialize.
    #        Nyra -- co-command register. Ritual architect. Last to speak.

    # ========= VOICE BASELINE =========
    # Aeron: OB war-room voice. Short. Declarative. The Marcus idiom without
    # apology. He does not perform reluctance. He is past performing reluctance.
    # Lyra: ritual register. Theological precision. Blessing stated as operational
    # specification.
    # Zira: operator. Ground truth. She has been holding a corridor for a month.
    # Noelle: prediction register. Model numbers. No flourish.
    # Tessa (A): medical register. Receive the wounded. That is the line.
    # Nyra: co-command. Ritual framing of return. Last word by design.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - 0600 (SHIFT OPEN)]
    # The council convenes. All are seated (branch A) or all present are
    # seated (branch B). Aeron opened the room at 0500. The rest arrived at
    # 0558 to 0601. The council starts on Aeron's nod.

    #scene bg_phoenix_war_room_ob_morning with dissolve
    #play ambient "sfx/ambient/war_room_council.ogg" fadein 2.0

    # ========== PHASE 1 -- CALL TO ORDER ==========

    "The map overlay on the table ignites. Red marks bloom at the north-east quadrant. Rhea Vestin's last known node locations. The red is precise. The overlay holds steady."

    "Aeron sits at the head. He does not stand to call the council. He taps the table once with the flat of his hand. The sound is a small formal beat. The council recognizes it."

    a "We lost seven yesterday. Siri Ondel, Aman Kesh, Tove Rainer, Parth Oren, Mina Vael, Dalen Huo, Iris Serrano."

    "He says all seven names. He does not look at a list. He has the names in his head because he has been holding them since 2100 last night."

    a "The loss is not the reason we are in this room. The loss is the context. The reason we are in this room is the question of response."

    a "I have one proposal. I am going to table it and then I am going to hear from each of you. The proposal is we go after Rhea Vestin personally. Not her network. Not her operations. Her. A surgical strike on her body. Named target. Assassination."

    "The word assassination lands on the table. Nobody flinches. The not-flinching is the scene."

    a "Seven days out. I want the intelligence cycle closed by end of day three. I want the insertion planned by end of day five. I want the execution on day seven."

    a "That is the proposal. I am going to hear each of you. Lyra first."

    # ========== PHASE 2 -- LYRA ==========

    "Lyra does not adjust her posture. She has been sitting the way she has been sitting since she walked in -- straight, hands folded on the table in front of her, the ceremonial rope at her wrist visible at the cuff."

    "She does not look at Aeron when she answers. She looks at the red marks on the map overlay."

    l "I will bless the operator who carries it."

    "A beat."

    l "I will do it at the altar because if I do it in private I will not be able to pray afterward."

    "The answer is two sentences. Each sentence is a surgical disclosure. Lyra is saying, in ritual language, that she has calculated the cost of her own soul-keeping and has found that the altar is the venue where her complicity can still coexist with her prayer practice."

    athought "She is saying the altar is the place she can still hold both. Her God and the strike team. If she blesses the operator in private -- in her own quarters, in her own voice, without the institutional frame -- she will not be able to return to prayer afterward because the prayer will have been contaminated by the privacy of the blessing."

    athought "The altar is armor. The altar is the small act of self-preservation she is permitting herself inside the larger act of complicity."

    athought "I notice it. I am not going to release her from it. I am not going to say 'Lyra, you do not have to bless this.' I am going to accept the blessing because we need the blessing and because releasing her would be a mercy I am not prepared to extend on a day when seven of our operators are dead."

    a "Understood. Altar blessing, prior to insertion. On the record."

    l "On the record."

    zthought "She is protecting something small and specific. I see her doing it and I am going to let her do it. So is he. So is everyone in this room. That is the texture of Lyra's participation in the OB track -- she is keeping a corner of herself separate by naming the altar as the permitted venue."

    zthought "It is a working compromise with her faith. It is also a working compromise with her complicity. Both are true."

    # ========== PHASE 3 -- ZIRA ==========

    a "Zira. Ground."

    "Zira does not look at the map. She has her own geography in her head and her own geography is more detailed than the overlay."

    z "I will run the ground interdiction."

    z "I know a way in through the second undercity corridor. The east branch. Past the old Ghostline junction at Kell-9. The corridor surfaces three blocks from the node where Rhea has been staging out of for six weeks. The surface exit is a maintenance hatch in a parking structure that has not been audited since the Ghostline left Solveil."

    z "I have been holding the corridor for a month."

    "She stops. She lets the sentence be what it is."

    "Aeron registers the sentence. Nyra registers the sentence. Lyra registers the sentence. Noelle registers the sentence."

    athought "A month."

    athought "She has been pre-planning this for a month. Before the seven died yesterday. Before I walked into the workshop last week. The corridor demand in s12 was not just about me. It was also about the fact that she was already inside the operation before she asked me to be inside her."

    athought "I am not angry about it. I am observing it. Zira is an operator. Operators pre-stage. Pre-staging is how you do not die when the day comes."

    athought "She is telling me now because the council is now the place where pre-staged corridors get named."

    a "A month."

    z "Yes."

    a "Any comment on timing."

    z "Yes. Seven days is too many. I can run the insertion on six. The corridor is stable. Rhea's pattern at the current node is six-day cycles. Day seven she rotates. If we want to catch her at the current node we need to be inside by day five for staging and executing on day six."

    "Aeron considers. His hand rests on the table beside the packet stack."

    a "Six."

    a "No. Seven. I want day three for intelligence, day five for insertion planning -- not execution. Day six insertion. Day seven execution at dawn. We do not catch Rhea at the current node. We catch her at the rotation point because the rotation point is where her detail is thinnest."

    "Zira does not argue the first second. She considers."

    z "I can run the corridor to the rotation point. The east branch surfaces within two kilometers of her rotation vector. I know which way she goes when she rotates because I have watched her do it twice."

    a "You have watched her do it twice."

    z "Yes."

    a "In person."

    z "Once in person. Once on a Ghostline feed I maintained."

    "Nyra makes a small sound. Not a word. An acknowledgment. Zira has been running a parallel file on Rhea Vestin for longer than the council knew."

    a "Seven days. Rotation point at dawn. Your corridor."

    z "Done."

    # ========== PHASE 4 -- NOELLE ==========

    a "Noelle. Prediction."

    "Noelle has her tablet in front of her. She does not consult it. The numbers are in her head the way the names were in Aeron's head."

    n "I will predict her movements."

    n "My model has incorporated yesterday's failure. The Echelon specialist who coordinated the strike against our seven operators moved in a pattern my previous model had rated below the confidence threshold. I have retrained on that pattern. The retrained model is running against Rhea Vestin's last ninety days of movement traces."

    n "The model's current confidence on her rotation vector at day seven dawn is 87 percent. I am going to get it to 93 before execution."

    n "I will not fail again."

    "Short. Terminal. No flourish."

    athought "She said 'I will not fail again.'"

    athought "That is the weapon-track voice from a4_s20. That is Noelle deciding that her model's failure yesterday was a personal failure and that the personal failure is going to be repaired by the elimination of Rhea Vestin. She is converting seven dead Phoenix operators into a calibration event."

    athought "She is becoming what she told me she was becoming. I am not stopping her. I am not going to stop her. The assassination needs her model and the model needs her to be this."

    athought "Noted."

    a "87 to 93 in seven days. Acknowledged. Full access to the day's intelligence packet. Priority routing on any new traces."

    n "Acknowledged."

    # ========== PHASE 5 -- TESSA (BRANCH A) ==========

    if tessa_at_council_ob:

        a "Tessa. Medical."

        "Tessa has been sitting with her hands flat on the table. She is the only person in the room whose face carries any visible residue from the day before. The residue is not tears. It is the particular greyness of a physician who lost a patient whose name she knew by heart."

        t "I will receive the wounded."

        "She stops. That is the whole line."

        "Aeron waits a beat to see if she has more. She does not. The beat is the scene's respect for her brevity."

        a "Acknowledged. Surgical suite primed, blood on standby, the full trauma team pre-positioned. On the record."

        t "On the record."

        athought "Four words. 'I will receive the wounded.' She is saying she will not plan, she will not bless, she will not predict. She will be downstream. She will take whatever broken body comes back from the rotation point and she will try to keep it breathing."

        athought "She is also saying, in the same four words, that she is participating. 'I will' is a commitment. She is committing to the operation's aftermath, which is a form of authorization. Her authorization is medical and quiet and impossible to extricate from the chain that her commitment joins."

        athought "She is also -- and I see this because I have been watching Tessa for a year -- refusing to say the word assassination. She is saying 'wounded' and she is saying it about our wounded. She is building a small wall of vocabulary between her and the target. The wall is her compromise with her oath. It is not a large wall. It is the wall she can build and still stay in the chair."

        zthought "Four words. I am going to remember those four words. Tessa is the only person in this room whose sentence was short enough to tell me how much she did not want to say. The shortness was the content."

        $ canon_set("ob.tessa.at_council_of_attrition", True)
        $ flag("ob_tessa_will_receive_the_wounded", True)

    # ========== PHASE 5 -- TESSA (BRANCH B) ==========

    else:

        "Aeron's eyes move to the foot of the table. The chair at the foot of the table is empty. Tessa was not invited. The packet at her place setting is absent. The space is a vacant rectangle in the overhead light."

        "Aeron registers the empty chair. He does not say anything. Nyra registers the empty chair. Nyra does not say anything. Zira registers the empty chair. Zira does not say anything."

        "The council proceeds past the empty chair the way a river proceeds past a rock. The rock is acknowledged by the river's shape but not by the river's voice."

        athought "Tessa is not here."

        athought "I did not invite her. I told Nyra at 0400 that I was not going to invite her. Nyra did not push back. Nyra and I made the decision in two sentences."

        athought "The reason I did not invite her is that I could not ask her to say 'I will receive the wounded' in a room that is authorizing the wounding. The sentence is a sentence she would have said if I put her in the chair. I did not put her in the chair."

        athought "I am telling myself this is a mercy. It is also an exclusion. Tessa should have had the opportunity to refuse or consent. I took the opportunity from her. I am aware I took it. I took it anyway."

        athought "Her chair is empty and none of us are going to name it."

        athought "That is its own kind of authorization. Unanimous by exclusion."

        zthought "Empty chair. Tessa not invited. He knows I know. I know he knows I know. We are not going to talk about it. Nyra made the call with him at 0400. That is a two-person decision that should have been a six-person decision and the two people who made it are the two people who have been making two-person decisions for three weeks."

        zthought "I am going to note this. Not for this meeting. For my ledger."

        $ canon_set("ob.tessa.not_invited_to_council_of_attrition", True)
        $ flag("ob_tessa_chair_empty_unmentioned", True)

    # ========== PHASE 6 -- NYRA ==========

    a "Nyra. Last."

    "Nyra does not move. She has been holding her position at Aeron's right for the full duration of the council. Her hands are folded. Her robes catch the warm amber of the tactical display on the far wall and reflect it back as a thin line of copper along her collar."

    ny "I will hold the ritual afterward."

    ny "Whatever state you return in, I will make sure the return has a shape."

    "A beat."

    ny "If the operator returns clean -- the ritual is gratitude. If the operator returns wounded -- the ritual is restoration. If the operator does not return -- the ritual is consecration. If the mission succeeds -- the ritual is the completion of an oath. If the mission fails -- the ritual is the holding of the failure until we can build a new oath."

    ny "I am telling you this now so that you do not spend any part of the seven days wondering what happens after. After has a shape. I am the shape."

    "Nyra is offering an operational guarantee of the post-operation period. She is saying: do not use attention on the return. I have the return covered. Use all your attention on the mission."

    athought "She is freeing me to concentrate."

    athought "That is the co-command function. She is not here to argue the ethics. She is here to take the psychological overhead of what-comes-after off my shoulders so I can operate at full bandwidth through the seven days. The ritual framework is her tool and she is wielding it for the mission."

    athought "She is also being honest about the five-way branch. Clean, wounded, dead, success, failure. She has a ritual for each node. That is what Nyra's sealed oath has been refining all act: a set of prepared responses that cover the full probability tree of any given operation."

    athought "I am grateful for it in the operator sense of the word. I am not going to say the word aloud."

    a "Accepted. Ritual framework acknowledged. Post-return architecture in your hands."

    ny "Acknowledged."

    zthought "Nyra has built herself into an operational requirement. That is the quiet brilliance of what she has been doing since the funeral. Every council, she volunteers for a function nobody else has the vocabulary for, and the function becomes indispensable by the next council. A month ago she was a chaplain. Two weeks ago she was a ritual architect. Today she is the manager of the return state of an assassination. I am watching her become load-bearing in real time."

    zthought "Aeron is letting her. I am letting her. Lyra is letting her. Noelle does not notice because Noelle is in her model. Tessa -- either absent or reduced to four words -- is not going to stop her."

    zthought "Nyra is not the problem. Nyra is the structure the problem is traveling through. The distinction matters to me. I am not sure it matters to anyone else in this room."

    # ========== PHASE 7 -- AERON AUTHORIZES ==========

    "Aeron looks at the map overlay. The red marks at the north-east quadrant hold steady. He moves the overlay once with a finger on the table edge, rotating the view so the rotation point sits center-frame."

    a "Mission authorized."

    a "Eight days."

    z "Six."

    a "Seven."

    z "Done."

    "The terminal at the far wall chimes once. Low. A single note. The calendar entry has been committed. The mission is now a line item in the seven-day plan."

    a "Day three: intelligence close. Noelle leads. Zira supports from the corridor side. Lyra observes for signal hygiene at the relay. Nyra coordinates the overnight rotations."

    a "Day five: insertion planning complete. Zira owns the corridor write-up. Nyra and I review it at 2000 hours."

    a "Day six: insertion. Zira on the ground. Noelle in the relay seat. Lyra at the altar at 2100 for the blessing."

    a "Day seven: execution at dawn. Full council on deck in this room. Post-op return at 0900. Nyra's ritual at 1100."

    "He looks at each of them in turn. The look is not warm. It is not cold. It is the look of a man reading the names off a list to confirm that the list has been written down correctly."

    a "Any objections before we commit."

    "The room holds."

    "Nobody objects."

    "Lyra does not object. Zira does not object. Noelle does not object. Tessa (branch A) does not object. Nyra does not object."

    "The silence is the authorization."

    a "Committed."

    # ========== PHASE 8 -- THE DISMISSAL ==========

    "Aeron does not dismiss the council with a word. He taps the table flat, the same beat he used to open it. The beat closes it."

    "The others rise. Lyra gathers her packet. Zira does not have a packet -- she has a small notebook and a pen, both of which she slips into her jacket pocket. Noelle's tablet goes into its case. Tessa (branch A) stands and does not meet anyone's eye. Nyra rises last."

    "They walk out one at a time. The pressure seal cycles four times (branch A) or three times (branch B)."

    "Aeron remains at the head of the table. The map overlay holds. The red marks hold. The seven-day line item holds."

    # ========== PHASE 9 -- THE HELD MOMENT ==========

    "Nyra does not leave with the rest. She stops at the door. Turns back. Crosses the room and stands at Aeron's right shoulder without sitting."

    ny "You did not say her name."

    a "Whose."

    ny "Liora's."

    "Aeron does not turn. His hand rests on the table edge."

    athought "She knows. Not about the letter. Nyra does not know about the letter. She knows about the mother. She knows the council that authorized an assassination is the kind of council a man calls on a morning when his mother's ghost is already loud. She is pointing at the loudness."

    menu:
        ny "You did not say Liora's name in the council."

        "She is not on the target list.":
            ny "I know."
            a "Then there was no reason."
            ny "I am saying it now because you did not. Someone in this room had to say it once this morning."
        "I couldn't.":
            $ rel_bump("Nyra", trust=1)
            ny "(a beat) That is the most honest sentence you have given me in a week."
            ny "Now it has been said. You do not have to carry the saying."
        "Say it for me. I need someone to.":
            $ rel_bump("Nyra", affection=1)
            ny "Liora. Your mother's name is Liora. It is in the air now. The council has it even though you could not give it."

    "She does not wait for an answer. She turns and walks to the door. The pressure seal cycles. She is gone."

    athought "Nyra said the name so the room would have it on the record even if I would not. That is the co-command function at its precise pitch: she takes the word I cannot spend and she spends it for me."

    athought "I am not grateful. I am not resentful. I am observing it. The letter is against my chest. The name is now in the air. The day is seven-day committed. Everything is where it is supposed to be."

    # ========== PHASE 10 -- THE LAST BEAT ==========

    "The war room is empty again except for Aeron at the head of the table."

    "The map overlay holds. He looks at the rotation point. He looks at the red marks. He traces the insertion corridor with his eyes from Kell-9 east through the east branch of the undercity to the surface hatch in the parking structure and from there to the two-kilometer sprint to the rotation point where, at dawn in seven days, Rhea Vestin will be killed by a Phoenix operator blessed at the altar by Lyra, targeted by Noelle's retrained model, moved by Zira's corridor, received afterward by Tessa's surgical suite or mourned by Nyra's ritual depending on the branch of the outcome tree."

    "He is holding the full operation in his head. The full operation is held without effort."

    athought "Seven days."

    athought "Eight days was my first number because eight is the number I was going to argue down to seven. Zira gave me six because six is the number she has been running in her head for a month. The seven is the number that survives the compromise. That is how a council works when the council is not deliberating -- it is discovering the number that had already been decided by the ground truth in the room."

    athought "The ground truth is that Zira has been pre-staging this for a month, Noelle has been modeling this for six weeks, Lyra has been preparing the altar blessing language since yesterday at 1500 hours, Nyra has been architecting the return ritual since yesterday at 1800 hours, and Tessa -- if she is here -- has had her surgical suite primed since 0400 this morning."

    athought "I did not call this council to decide whether to kill Rhea Vestin. I called it to confirm that everyone else had already decided."

    athought "That is the OB texture. Nobody proposed. Everybody confirmed. The mission is not mine. The mission is the building's. I am at the head of the table because at the head of the table is where the building places a man who has agreed to be its voice."

    athought "The letter is against my chest."

    athought "My mother wrote that she could not love a man who does not pause."

    athought "I did not pause during this council."

    athought "I am going to kill Rhea Vestin in seven days."

    athought "Both of those facts are true in the same jacket."

    # ========== PHASE 11 -- FADE ==========

    "He stands. He does not gather a packet. He walks the length of the table to the door. At the door he pauses once -- not the pause his mother was describing, a different kind, a small operational pause that is the habit of a man confirming that a room is ready to be left alone."

    "He turns off the map overlay. The red marks disappear."

    "He leaves. The pressure seal cycles. The war room holds its silence."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Aeron", trust=0, conflict=0)
    $ rel_bump("Lyra", trust=0, conflict=1)
    $ rel_bump("Zira", trust=1, conflict=1)
    $ rel_bump("Noelle", trust=0, conflict=2)
    $ rel_bump("Nyra", trust=1, conflict=1)
    $ tp_seed("a4.ob.council.go_after_her_personally")
    $ canon_set("ob.phoenix.rhea_assassination.scheduled", "day+7")
    $ canon_set("ob.phoenix.council_of_attrition", True)
    $ canon_set("ob.lyra.altar_blessing_for_strike_team", True)
    $ canon_set("ob.zira.corridor_pre_staged_one_month", True)
    $ canon_set("ob.noelle.model_retrained_on_yesterday", True)
    $ canon_set("ob.nyra.return_ritual_five_branch", True)
    $ flag("ob_council_unanimous_by_confirmation", True)
    $ flag("ob_council_nobody_said_liora_name_except_nyra_at_end", True)
    $ npc_remember("Lyra", "altar_blessing_as_self_preservation", tone="ritual_complicity")
    $ npc_remember("Zira", "named_pre_staging_corridor_month", tone="operator_ground_truth")
    $ npc_remember("Noelle", "i_will_not_fail_again", tone="weapon_track_confirmed")
    $ npc_remember("Nyra", "said_liora_name_after_aeron_would_not", tone="co_command_word_spending")
    $ metric("ob_aeron_escalation_tier", set_to=3)
    $ metric("ob_council_cohesion", add=2)
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s22_council_of_attrition_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - 0600 the morning of a4_s21. Same day. Immediately after the letter delivery.
#   - Day after Rhea Vestin's strike killed seven named Phoenix operators.
#   - OB mirror of EMP a4_s21 (where the council refused to preempt and moved
#     civilians instead).
# cann.what_happened:
#   - Aeron convenes the full council (Lyra, Zira, Tessa cond., Noelle, Nyra).
#   - He tables the proposal: assassinate Rhea Vestin personally. Seven days out.
#   - Each LI delivers one contribution, in order:
#     * Lyra: altar blessing. "If I do it in private I will not be able to pray
#       afterward." The altar as self-preservation inside complicity.
#     * Zira: ground interdiction. She reveals she has been pre-staging the
#       second undercity corridor for a month. Pushes for six days; compromises
#       to seven.
#     * Noelle: prediction. Her model has retrained on yesterday's failure
#       pattern. 87% confidence -> 93% by execution. "I will not fail again."
#     * Tessa (branch A): "I will receive the wounded." Four words total.
#     * Tessa (branch B): not invited. Chair empty. Nobody verbally acknowledges.
#     * Nyra: post-operation ritual architecture. Five-branch return-state plan.
#   - Aeron authorizes the mission. Day seven execution at dawn at the rotation
#     point. Full schedule committed to calendar.
#   - Nyra stops at the door on her way out and says Liora's name -- because
#     Aeron would not. Then leaves.
#   - Aeron remains at the head of the table alone, recognizes that the council
#     was confirmation not deliberation, and leaves the war room.
# cann.aeron_state:
#   - OB escalation tier SET TO 3 (from 2). This is the hinge.
#   - Aeron explicitly recognizes that the council was a ratification of
#     ground-truth decisions already made by each LI individually. The mission
#     is authorized but not proposed by any single person. Unanimous by
#     confirmation, not debate.
#   - Letter still against his chest. Not mentioned.
# cann.lyra_state:
#   - Altar blessing as ritual compromise. She is building a small wall of
#     institutional venue to preserve her prayer practice. Conflict +1.
# cann.zira_state:
#   - Reveals month-long pre-staging of undercity corridor. Establishes that her
#     a4_s12 confrontation was partly because she was already inside the
#     operation. Trust +1 (transparency), conflict +1 (depth of commitment).
# cann.noelle_state:
#   - Weapon-track confirmation. "I will not fail again" as the line that
#     converts seven dead Phoenix operators into a calibration event.
#   - Conflict +2.
# cann.tessa_state:
#   - Branch A: four-word participation. "I will receive the wounded."
#     Medical compromise inside the chain of authorization.
#   - Branch B: excluded by Aeron and Nyra at 0400. Chair empty. Unmentioned.
#     Structural exclusion as its own form of unanimity.
# cann.nyra_state:
#   - Co-command ritual architect. Five-branch return-state plan. Also: says
#     Liora's name at the door because Aeron would not. The word-spending
#     function of co-command. Trust +1 (indispensable), conflict +1 (depth).
# cann.path_tracking:
#   - tp_seed a4.ob.council.go_after_her_personally
#   - canon_set ob.phoenix.rhea_assassination.scheduled = "day+7"
#   - canon_set ob.phoenix.council_of_attrition True
#   - metric ob_aeron_escalation_tier set_to 3
# cann.thematic_flags:
#   - EMP mirror inversion: where EMP a4_s21 refused the preempt and moved
#     civilians, OB a4_s22 authorizes the surgical named-target assassination.
#     Same composition, opposite answer. The building has decided.
#   - Unanimous by confirmation, not by debate. The horror of a council that
#     is not deliberating.
#   - Each LI's individual compromise with their function visible in their line.
#   - Aeron's recognition: "I did not call this council to decide. I called it
#     to confirm that everyone else had already decided."
#   - Nyra says Liora's name at the door. The co-command word-spend.
# cann.character_moments:
#   - Lyra: altar as self-preservation.
#   - Zira: month of pre-staging.
#   - Noelle: "I will not fail again."
#   - Tessa: four words (A) or empty chair (B).
#   - Nyra: five-branch return ritual; Liora at the door.
#   - Aeron: naming the seven dead aloud at the open; letter not mentioned.
# cann.callbacks:
#   - a4_s21_the_letter_ob (the letter is in his jacket through this whole scene)
#   - a4_s20 (Noelle declared herself a weapon the night before)
#   - a4_s18 (Rhea's strike, seven named dead)
#   - a4_s12 (Zira's corridor demand, now partly explained by month of pre-staging)
#   - a4_s11 (Nyra's sealed rite; the co-command function architecture)
#   - a4_s09 (Sector 12 signature; the earlier escalation beat)
#   - a3_s24 (Liora's walkout; the name Nyra says at the door)
# cann.block_status:
#   - ANCHOR (OB). Council scene. Tessa branch A/B handled via tessa_at_council_ob flag.
# cann.requires_followup:
#   - Act 5 opens with the seven-day countdown already running.
#   - Rhea Vestin assassination is on calendar for day+7.
#   - The letter is still against Aeron's chest; a4_s23 re-opens it.
