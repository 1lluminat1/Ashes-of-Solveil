# =======================================================
# ACT 4 - Scene 19: Tessa and the Trainee (Obedience Path)
# File: a4_s19_tessa_the_trainee_ob.rpy
# Path: OB
# Type: TESSA STATE BEAT -- CONDITIONAL (branches on ob.tessa.choice)
# Character Focus: Tessa, Aeron
# =======================================================
# BRANCHING:
#   - If ob.tessa.choice == "stay_and_resist"  -> Branch A (medical wing, the board)
#   - If ob.tessa.choice == "stay_but_withdraw" -> Branch B (mess hall, empty not angry)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s19_tessa_the_trainee_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s19_tessa_the_trainee_ob:
    $ show_timeline("DAY 52", "03:00", "Phoenix Base — Medical Wing")

    # Branch dispatch. Matches the pattern from a4_s17_tessa_conditional_beat_ob.
    if canon_get("ob.tessa.choice") == "stay_and_resist":
        jump a4_s19_tessa_the_trainee_ob_stay_and_resist
    else:
        jump a4_s19_tessa_the_trainee_ob_stay_but_withdraw


# ===========================================================
# BRANCH A -- STAY AND RESIST -- the medical wing, the board
# ===========================================================
label a4_s19_tessa_the_trainee_ob_stay_and_resist:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, handheld for two shots in the corridor approach and locked
    #         tripod inside the medical wing. The handheld does not shake.
    #         It breathes. The board scene is covered in a tight over-shoulder
    #         when Tessa writes the name, a reverse medium when Aeron arrives,
    #         and a held two-shot at the board for the exchange. The scene
    #         ends on the board alone -- the name on the LIVING column, the
    #         sentence beside it, and the marker cap on the shelf.
    # LIGHTING: Medical wing at 0300 hours. Overhead strips at 30%. The
    #           operational board is lit by a single directed strip at 60%
    #           so that the columns can be read. The board's light is harder
    #           and whiter than the room's. The board is the brightest
    #           surface in the frame. Tessa is lit from the board. Aeron,
    #           when he arrives, is lit by the corridor spill as the doors
    #           open and then by the board after the doors close.
    # SFX: Loop -- medical wing ambient at night: the cooling for the supply
    #      refrigeration units, the low hum of the monitoring arrays
    #      (patients count: seven; all stable), the vent. One-shots -- the
    #      doors opening (one set), Tessa's boots on tile (nine steps from
    #      the doorway to the board), the cap of the marker (unscrewing and
    #      re-capping), the marker stroke on the board (the letters of a
    #      name and a short sentence, audible), Aeron's boots on tile (three
    #      steps from the doorway, stopping at a reading distance from the
    #      board), the marker cap going back on, the marker being set on the
    #      shelf beside the board.
    # FX/COMP: The operational board. In a4_s06 Nyra overwrote the medical
    #          board's patient-care taxonomy with an operational taxonomy --
    #          LIVING / OPERATIONAL-READY / OPERATIONAL-COMMITTED /
    #          OPERATIONAL-WITHDRAWN / DEAD. The overwrite persisted through
    #          a4_s16 and Tessa's resistance was passive, not active.
    #          Tonight the board has just been updated by the operational
    #          channel: the seven names from a4_s18 now populate the
    #          OPERATIONAL-WITHDRAWN column at the top. Siri Ondel is the
    #          third name from the top. The DEAD column at the far right of
    #          the board is reserved for deaths that occur on the medical
    #          wing's own floor. The DEAD column currently holds zero names.
    #          The seven dead from the forward base have been categorized
    #          as OPERATIONAL-WITHDRAWN -- the operational language for
    #          bodies not yet recovered. The word DEAD is not used by the
    #          board for them. The word DEAD is reserved for a different
    #          thing.
    # BLOCKING: Phase 1 -- Tessa walks from the doorway to the board at 0302.
    #           Phase 2 -- Tessa at the board, writing SIRI ONDEL in the
    #           LIVING column. Phase 3 -- Tessa writing the sentence beside
    #           the name. Phase 4 -- Aeron arrives. Phase 5 -- Tessa speaks.
    #           Aeron takes the marker. Phase 6 -- the exchange. Phase 7 --
    #           Tessa leaves. Aeron alone at the board.
    # CANON: Immediately after a4_s18. Tessa received the casualty report at
    #        approximately 0246 through the medical wing duty station. Siri
    #        Ondel -- medic trainee, nineteen, Tessa's direct mentee --
    #        listed in the OPERATIONAL-WITHDRAWN column by the operational
    #        channel's automated update at 0301. Tessa walks into the wing
    #        at 0302. Branch A is Tessa refusing the operational taxonomy
    #        at its root. She writes Siri's name on the LIVING column --
    #        not moving it, not transferring it, not adjusting a column,
    #        but asserting the refusal directly on the board by writing
    #        the wrong column. The wrongness is the assertion. Aeron does
    #        not correct the assertion.
    # FACE: Tessa -- the face of a woman whose grief has reached the part
    #        of her that writes. The face is not crying. The face is
    #        working. The work is the writing.
    #        Aeron -- the institutional face. It holds for the duration of
    #        the scene. When Tessa says "do you" there is a one-beat
    #        not-holding that the camera catches without making a point of.

    # ========= VOICE BASELINE =========
    # Tessa: Quiet. Precise. She is working in her diagnostic register --
    #        the register in which a medic names a body correctly because
    #        the naming is the last accurate thing she can do for it. The
    #        register is not angry. The register is final.
    # OB Aeron: Minimal. Four spoken turns in the scene. The longest is
    #           three words. He is listening more than he is speaking.
    #           The listening is the scene's subject.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE -- MEDICAL WING -- 0302]
    # Approximately thirty minutes after the forward base at Sector 9-North
    # goes dark. The casualty report was delivered to Tessa's duty station
    # at 0246. Tessa has been in the staff changing room reading the report
    # for sixteen minutes. The seventeenth minute she stood up.

    #scene bg_medical_wing_night with dissolve
    #play ambient "sfx/ambient/medical_wing_night.ogg" fadein 2.0

    # ========== PHASE 1 -- THE WALK ==========

    "The medical wing at 0302 is quieter than it has been at any other hour in the last three weeks. The patient count is seven. All seven are stable. None of the seven are in the critical bay. The monitoring arrays are at their low-idle hum."

    "The operational board is at the far end of the main corridor of the wing, on the wall that used to hold the patient-care taxonomy board. The patient-care board is still physically present -- it is the same board. The taxonomy on its face has been overwritten. The columns now say LIVING, OPERATIONAL-READY, OPERATIONAL-COMMITTED, OPERATIONAL-WITHDRAWN, DEAD."

    "The OPERATIONAL-WITHDRAWN column has been updated by the operational channel's automated feed at 0301. It now contains seven names at the top of the column. The automated feed writes in the institutional font the board uses for all new entries. The institutional font is the font Tessa has been looking at for eleven days and has not yet used herself."

    "The seven names, in the order the automated feed placed them:"

    "HAREL VOST"

    "DREN KALE"

    "SIRI ONDEL"

    "TOMAS REILL"

    "ELO VARIC"

    "MIRA TEV"

    "JARA NEESE"

    "The DEAD column at the far right of the board currently holds zero names. The DEAD column is not for the forward base dead. The DEAD column is for deaths that occur on the medical wing's own floor. The distinction is an operational distinction. The distinction is Nyra's."

    "Tessa walks into the wing from the staff changing room door at 0302:11."

    "Nine steps from the doorway to the board."

    "She is carrying the marker she has been carrying in her coat pocket for eleven days. The marker has not been used on the board in those eleven days. Tessa has been carrying it without using it. The marker is an object she has been considering."

    "She stops at the board at 0302:20."

    # --- TESSA LOOKING AT THE BOARD ---

    tthought "Siri Ondel."

    tthought "Third name from the top. The font is the institutional font. The letters are the specific sans-serif the operational feed uses for all its automated entries. The font is the same font that was on the schema rewrite Noelle submitted on Tuesday."

    tthought "Siri is in the OPERATIONAL-WITHDRAWN column."

    tthought "OPERATIONAL-WITHDRAWN is the operational language for bodies that have not been recovered from a theater but are confirmed dead. The language is accurate in the operational register. The language is not accurate in any other register."

    tthought "Siri is dead."

    tthought "Siri is not WITHDRAWN. Siri is dead. The word for what happened to Siri is dead. The word is not a taxonomy entry. The word is the word."

    tthought "The column for the word is the DEAD column."

    tthought "The DEAD column is for deaths that occur on this floor."

    tthought "The DEAD column is not for Siri because Siri did not die on this floor. Siri died on the east ridge of Sector 9-North at approximately 0420, during the second wave of the strike. The medic trainee slot on a forward base is inside the mess structure -- a central position because medics have to be reachable from all quadrants. The second wave hit the mess structure."

    tthought "I know the mess structure on the forward base because I helped plan its medical layout last month."

    tthought "I recommended the central position. I recommended the central position because the central position was optimal for response time. The central position was optimal until a strike hit the central position."

    tthought "The central position killed Siri."

    tthought "My recommendation killed Siri."

    tthought "I am not going to let the operational feed write that sentence on the board."

    tthought "The operational feed writes OPERATIONAL-WITHDRAWN. The operational feed does not write my recommendation killed Siri."

    tthought "I am going to write a different sentence on the board."

    tthought "I am going to write the sentence that is true."

    tthought "I am going to write it in the wrong column."

    tthought "The wrong column is the column that will make a human being who reads the board have to stop reading at the wrong column and understand that the wrong column is the correct column."

    tthought "The wrong column is the LIVING column."

    tthought "Siri is not LIVING. Siri is dead. The wrong column is wrong and the wrongness is what I need the board to carry."

    tthought "I am going to write her name in the LIVING column. I am going to write beside her name a sentence that is not a taxonomy entry."

    tthought "The sentence is: she was nineteen."

    tthought "The sentence is not about what the board says she is. The sentence is about what she was."

    tthought "I am going to write the past tense next to the wrong column and that is what I am going to do tonight."

    # ========== PHASE 2 -- THE MARKER ==========

    "Tessa takes the marker out of her coat pocket. She uncaps it. The sound of the cap unscrewing is small in the wing's ambient."

    #play sound "sfx/marker_uncap.ogg"

    "She raises the marker to the board."

    "She writes, in the LIVING column, below the last existing entry in that column, in letters that are more careful than the institutional font but are her own hand:"

    "SIRI ONDEL"

    "The letters are capital. The capital is not institutional. The capital is the capital a medic uses when she is writing a name on a triage tag and the tag has to be readable in any light."

    #play sound "sfx/marker_stroke_name.ogg"

    "She pauses."

    tthought "The name is on the board in the wrong column."

    tthought "A reader has to now stop and understand."

    tthought "I am going to add the second part."

    "She writes, beside the name, in letters smaller than the name but in the same capital, the same hand:"

    "SHE WAS NINETEEN"

    #play sound "sfx/marker_stroke_sentence.ogg"

    "Three words. A short sentence. The sentence is not a taxonomy entry. The sentence is a witness statement."

    "Tessa lowers the marker."

    "She does not cap it."

    "She stands in front of the board looking at what she has written."

    tthought "The name is in the LIVING column."

    tthought "The name is wrong."

    tthought "The wrongness is what I came here to make."

    tthought "The board now has an entry that the board cannot process in its taxonomy. The entry is in the LIVING column but the sentence beside the entry uses a past tense verb. The entry is a contradiction on the board's own face."

    tthought "The contradiction is not going to be removed by the automated feed. The automated feed does not remove entries written in non-institutional hand. The automated feed only writes in its own column. The automated feed will not touch the LIVING column entry I just made."

    tthought "The entry will remain on the board until a human being comes to the board and decides what to do with it."

    tthought "The human being is going to be Aeron. Aeron is going to come."

    tthought "I know he is going to come because I know the casualty report was routed to his ops station at 0423 and I know he has been standing in the ops room since then and I know he has been holding the knowing about Siri Ondel and I know he has been holding the fact that Siri Ondel was nineteen and I know he will come here at some point in the next hour because he cannot metabolize the holding without coming here."

    tthought "I am not doing this for him."

    tthought "I am doing this for Siri."

    tthought "If he comes -- when he comes -- the board is going to say to him what I came here to make the board say."

    # ========== PHASE 3 -- AERON ARRIVES ==========

    # CAMERA: reverse single. The medical wing doors at the far end of the
    # corridor from the board. The doors slide open. Aeron's silhouette in
    # the corridor spill. He walks three paces into the wing and stops.

    "The medical wing doors slide open at 0308:44."

    #play sound "sfx/wing_doors_open.ogg"

    "The corridor light spills into the wing. Brighter than the wing's low overhead strips. The spill falls across the tile in a long pale rectangle."

    "Aeron walks three paces into the wing and stops. He stops approximately seven meters from the board. He does not continue walking toward the board. He is standing at a reading distance from which he can see the board but cannot read the small print."

    "He can read the institutional font of the automated feed because the institutional font is large. He can see the seven new names in the OPERATIONAL-WITHDRAWN column. He can see Siri Ondel's name third from the top."

    "He can also see that there is a new entry in the LIVING column, lower down, in a hand that is not institutional. He cannot read the hand from his current position."

    "He takes two more paces forward. He stops again. He is now approximately four meters from the board. From this position the hand is readable."

    "He reads it."

    "SIRI ONDEL -- SHE WAS NINETEEN"

    "He reads the entry in approximately two seconds."

    "He does not walk closer."

    "He does not speak."

    "He stays at the four-meter reading distance, looking at the board."

    # --- AERON'S INTERIOR ---

    athought "She did not move the name to the DEAD column."

    athought "She wrote the name in the LIVING column. The LIVING column. The wrong column."

    athought "The wrongness is the assertion. She is asserting that the operational taxonomy cannot hold Siri Ondel. The taxonomy has to break at the point of Siri Ondel. The taxonomy does not break on its own. The taxonomy has to be broken by a hand holding a marker in the wrong column."

    athought "She is refusing the taxonomy at its root. She is not arguing with the columns. She is refusing to use the columns correctly."

    athought "The refusal is more precise than an argument. An argument would have accepted the premise that the columns are a thing worth arguing about. The refusal does not accept the premise. The refusal writes in the wrong column and leaves."

    athought "She has not left yet."

    athought "She is at the board. She has just set the marker down. She has not capped it. The cap is in her hand."

    athought "I am watching her refusing the taxonomy at 0308 in the morning at a distance of four meters."

    athought "I am the commander who signed the operational board overwrite in a4_s06."

    athought "I am the commander whose signature authorized the forward base deployment in the a4_s02 consolidation."

    athought "I am the commander who ordered the pull-back that left Siri Ondel's body on the east ridge to be recovered in a 48-72 hour window."

    athought "Siri Ondel is in the wrong column because I am the reason she is in any column at all."

    athought "I am going to walk to the board."

    athought "I am going to take the marker from her hand when she is done."

    athought "I am not going to correct the entry. The entry is not going to be corrected."

    athought "I am going to cap the marker and set it on the shelf beside the board."

    athought "I am going to do this because capping the marker and setting it on the shelf is the only thing my hand can do that is not a correction."

    "Aeron walks the four meters from his reading position to the board. His boots on the tile. Four paces."

    "He stops beside Tessa. Not behind her. Beside her. They are both facing the board."

    "The distance between them is approximately one meter."

    "Neither of them looks at the other."

    # ========== PHASE 4 -- THE EXCHANGE ==========

    # CAMERA: two-shot at the board. Both faces lit by the board's directed
    # strip. The entry SIRI ONDEL / SHE WAS NINETEEN in the LIVING column,
    # center-frame between them.

    "Tessa is looking at the entry."

    "Aeron is looking at the entry."

    "The board is what is between them."

    # --- TESSA SPEAKS ---

    t "She is not operational. She is nineteen. She is nineteen and she is dead."

    "Nine words. Present tense on the is nineteen. Past tense on the dead. The contradiction of tenses is the contradiction the entry on the board is carrying."

    "Aeron does not respond immediately."

    "Aeron takes the marker from Tessa's hand. Her hand is open, holding the marker loosely between thumb and forefinger. He does not pry. He lifts the marker out of her hand. Her hand opens further to let it go. Her hand closes on nothing."

    "He does not write anything."

    "He does not correct the column."

    "He caps the marker. The cap clicks in the wing's ambient."

    #play sound "sfx/marker_cap.ogg"

    "He walks one pace to the shelf beside the board. The shelf holds the three board-maintenance items: marker cap, cleaning cloth, the small stylus used to adjust the locked audit tags. He places the marker on the shelf."

    "He steps back from the shelf. He stands at his previous position, one meter to the right of Tessa. Both of them facing the board."

    # --- AERON SPEAKS ---

    a "I know."

    "Two words. The same two words he said to Noelle in a4_s10 after she said 'this is how it happens.' He is using the words again. He is using them in the medical wing at 0309 in the morning to a medic whose trainee is in the wrong column on the operational board."

    "The words are not a defense. The words are not a rationalization. The words are an acknowledgment that the speaker has received the information accurately and is not refusing to have received it."

    # --- TESSA ---

    t "Do you."

    "Two words. Two words that are a challenge. The challenge is not hostile. The challenge is a medic asking a commander to pass a very specific kind of diagnostic exam."

    "The exam is: do you know that she was nineteen, not in the informational sense of having been told her age in a casualty report, but in the sense of knowing what nineteen means."

    tthought "Nineteen means she was two months past the age at which the Academy will accept medic applicants."

    tthought "Nineteen means she came to me twenty-one days ago and asked if I would mentor her on triage protocol because she wanted to be good at the wing's worst hours."

    tthought "Nineteen means she called me Tess on day four because she had decided my name was easier than my title."

    tthought "Nineteen means she practiced the fast-suture pattern on a training pad for three hours on day nine because she had failed it twice on day eight."

    tthought "Nineteen means her coat sleeves were a size too large because the supply requisition for the small size was still sitting in the operational queue."

    tthought "Nineteen means the small-coat requisition will now be closed by the supply clerk tomorrow morning because the requisitioner is listed as OPERATIONAL-WITHDRAWN."

    tthought "Nineteen is all of those things."

    tthought "Do you know any of those things."

    tthought "I am not asking whether you have the information. I am asking whether you have the weight of the information."

    tthought "The weight of the information is not the information. The weight is the thing that sits in the body when the information is held without defending against it."

    tthought "Do you have the weight."

    # --- AERON ---

    "Aeron does not respond immediately."

    athought "I have the information. I do not know whether I have the weight."

    athought "The information includes her age. The information includes that she was Tessa's trainee. The information includes that she was in the second wave strike on the mess structure. The information does not include any of the specifics Tessa is thinking about right now."

    athought "I do not know that she called Tessa Tess on day four. I do not know about the fast-suture pattern. I do not know about the coat sleeves."

    athought "I know that Tessa is thinking those things right now. I know that those things are the things I would need to know in order to know what nineteen means in the sense Tessa is asking about."

    athought "I am a commander who knows the operational shape of a loss. I am not a medic who knows the specific weight of a nineteen-year-old with oversized coat sleeves."

    athought "Tessa is asking me whether I can hold the weight without asking for the weight to be transferred to me as information."

    athought "I cannot. I can hold only what I have been given."

    athought "I have been given the information."

    athought "I am going to tell her the truth about what I have and what I do not have."

    athought "The truth is that I am trying."

    athought "Trying is not having."

    athought "She is going to know the difference."

    a "I am trying to."

    "Four words. The answer is not a claim. The answer is a process. The process has a direction. The direction is toward a place he has not arrived."

    "Tessa looks at him for the first time in the scene. She turns her head approximately fifteen degrees. Her left eye is lit by the board strip. The right side of her face is in shadow."

    "She looks at him for approximately three seconds."

    "Then she looks back at the board."

    t "Try harder."

    "Two words."

    "The two words are not angry. The two words are instructional. A medic telling a commander that the exercise he is performing is not yet at the intensity the exercise requires."

    "The instruction is the most generous thing Tessa has said to Aeron in three weeks."

    "The generosity is the fact that she is still giving him instructions. If she were not giving him instructions she would be refusing to acknowledge that he has a direction. The instruction acknowledges the direction."

    "The instruction also acknowledges that the direction is not the arrival."

    # ========== PHASE 5 -- TESSA LEAVES ==========

    "Tessa does not wait for a response."

    "She walks past Aeron to the medical wing doors. Nine paces in reverse -- the same nine paces she used to approach the board. She does not look back. She does not look at the marker on the shelf. She does not look at the entry on the board."

    "She reaches the doors. The doors slide open. The corridor light spills in again. She walks through. The doors close behind her."

    #play sound "sfx/wing_doors_close.ogg"

    "Aeron is alone at the board."

    # ========== PHASE 6 -- AERON AT THE BOARD ==========

    # CAMERA: slow push-in on the board. The entry SIRI ONDEL / SHE WAS
    # NINETEEN in the LIVING column. The seven institutional-font names at
    # the top of the OPERATIONAL-WITHDRAWN column above it. The contrast in
    # hand and column is the composition.

    "Aeron stands at the board for approximately four minutes."

    "He does not write on the board."

    "He does not touch the marker on the shelf."

    "He does not close the contradiction on the board's face. The contradiction -- name in wrong column, past tense verb in the sentence beside a LIVING column entry -- is going to remain on the board until someone else in the medical wing decides to remove it, and the wing's staff includes Tessa, and Tessa is not going to remove it, and Tessa is the senior medic of the wing, and no junior medic is going to remove it without Tessa's instruction."

    "The contradiction is going to stay on the board."

    "The operational feed will continue to write in its own column. The contradiction will sit beside the operational feed like a small unresolved anomaly the operational channel cannot process. The operational channel does not process hand-written contradictions. The operational channel only processes institutional-font entries in its assigned columns."

    "The contradiction is outside the operational channel's processing range."

    "That is the exact thing Tessa made the contradiction in order to be."

    athought "I am going to walk out of the medical wing in approximately two minutes."

    athought "I am going to walk back to the ops room."

    athought "I am going to resume command of the survivor extraction tracking."

    athought "The survivors have cleared the second waypoint. The survivors are safe as of 0307. The secondary QRF at Sector 9-South is holding. The tac display is showing the east ridge corridor in green."

    athought "The forward base footprint is dark."

    athought "The seven red markers are still on the dark footprint."

    athought "The board in the medical wing has SIRI ONDEL in the LIVING column with the sentence she was nineteen beside it."

    athought "Those two records are the records of tonight. The tac display record is institutional. The medical wing board record is Tessa's."

    athought "The two records do not agree."

    athought "They are both accurate."

    athought "Tessa said 'try harder.'"

    athought "I do not know how to try harder in the register I am currently operating in."

    athought "Trying harder in this register is going to require a change to the register, and I have been building the register for four weeks, and the register is working. The register produced the pull-back order at 0420. The register produced the QRF-hold decision. The register produced the non-recovery of the bodies for a 48-72 hour window. The register is working."

    athought "The register working and trying harder in Tessa's sense are in opposition to each other."

    athought "Tessa is asking me to do a thing that would compromise the register."

    athought "I am the commander of a base that requires the register."

    athought "I am going to think about this more later."

    athought "I am going to think about it later because thinking about it now would require me to stop performing the role I am currently performing, and the role is what is holding the surviving assets on the east ridge."

    athought "Tessa's request is deferred."

    athought "The deferral is the answer."

    athought "The deferral is also the thing that is going to sit in my body for the rest of the night."

    # --- THE FINAL BEAT ---

    "Aeron takes one step toward the board. Not to write on it. To read the entry more closely. He is looking at the exact letters Tessa made with her hand."

    "The letters are careful. The careful is the medic's careful -- the careful of a person who has been writing on triage tags for years. The letters are not decorative. The letters are functional."

    "He does not touch the letters."

    "He turns. He walks from the board to the medical wing doors. Nine paces. The same nine paces Tessa used in both directions. The three of them -- Tessa-in, Tessa-out, Aeron-out -- have all used the same nine paces. The path is the same."

    "He reaches the doors. The doors open. He walks through."

    #play sound "sfx/wing_doors_close.ogg"

    "The medical wing is empty."

    "The board holds the record."

    # --- TP SEED ---

    $ tp_seed("a4.ob.tessa.she_was_nineteen")

    # ========= STATE UPDATES (BRANCH A) =========
    $ canon_set("ob.siri_ondel.on_living_column", True)
    $ canon_set("ob.tessa.wrote_in_wrong_column", True)
    $ canon_set("ob.tessa.witness_sentence", "SHE WAS NINETEEN")
    $ canon_set("ob.aeron.did_not_correct_the_board", True)
    $ canon_set("ob.medical_board.contradiction_persists", True)
    $ rel_bump("Tessa", trust=1, complicity=-1)
    $ flag("a4_ob_tessa_resisted_board_siri_ondel", True)
    $ npc_remember("Tessa", "wrote_siri_on_living_column_she_was_nineteen", tone="witness_refusal")
    $ npc_remember("Tessa", "told_aeron_try_harder", tone="instruction_as_generosity")
    $ npc_remember("Aeron", "capped_marker_did_not_correct", tone="deferred_answer")
    $ scene_mark(_current_scene_id, "exited")
    jump a4_s19_tessa_the_trainee_ob_end


# ===========================================================
# BRANCH B -- STAY BUT WITHDRAW -- the mess hall, empty
# ===========================================================
label a4_s19_tessa_the_trainee_ob_stay_but_withdraw:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked tripod. The mess hall at 0300. Tessa alone at a
    #         small two-seater table at the back of the hall. The camera
    #         opens on her face in a tight medium single. The scene then
    #         widens when Aeron arrives and sits. The two-shot holds across
    #         the small table for the exchange. The scene ends on Aeron
    #         alone at the table after Tessa leaves -- a medium single, the
    #         empty seat across from him, the untouched portion of Tessa's
    #         tray.
    # LIGHTING: Mess hall at night. Overhead strips at 20% -- the night
    #           setting, when the hall is not receiving meal service. One
    #           low warm lamp at the back of the hall near the tea station.
    #           Tessa's table is near the tea station lamp. Her face is lit
    #           half by the overhead and half by the tea lamp. When Aeron
    #           sits his face is lit from the same two sources. The warm
    #           tea lamp is the only warm light source anywhere in the scene
    #           and it does not soften the scene.
    # SFX: Loop -- mess hall night ambient: the tea station's water cycler,
    #      the vent, the distant hum of the walk-in cooler. One-shots --
    #      Tessa's fork on the tray (two or three small sounds, soft), the
    #      chair Aeron pulls out across from her, the tray sliding as he
    #      settles in, Tessa's fork set down at one point and not picked
    #      back up, the final sound of her pushing back from the table.
    # FX/COMP: Tessa's tray has a portion of the night staff's standard
    #          cold dinner on it. A small bowl of lentils, a piece of
    #          flatbread, a cup of the night tea. She has eaten
    #          approximately one third of the lentils. The flatbread is
    #          untouched. The tea is half-gone. The tray's arrangement is
    #          standard -- not hers, not personalized, just the standard
    #          night-staff tray as it came from the serving line.
    # BLOCKING: Phase 1 -- Tessa alone at the back table, eating slowly.
    #           Phase 2 -- Aeron arrives, sits across from her without
    #           asking, without being invited. Phase 3 -- the exchange
    #           conducted across the table. Phase 4 -- Tessa finishes her
    #           meal, stands, leaves. Phase 5 -- Aeron alone at the table.
    # CANON: Immediately after a4_s18. Tessa received the casualty report
    #        at approximately 0246 through the medical wing duty station.
    #        Tessa's a4_s16 decision was to stay at Phoenix but to
    #        withdraw her active engagement with the operational board
    #        and the medical wing's integration into the command
    #        structure. Branch B is the consequence of that withdrawal
    #        coming into contact with the Siri Ondel loss. Tessa does not
    #        go to the board. She told Aeron she would not touch the
    #        board. She is keeping her word. The keeping of her word is
    #        the beat. The keeping is not an act of anger. The keeping is
    #        an act of emptying. She is not leaving angry. She is leaving
    #        empty.
    # FACE: Tessa -- empty. Not sad -- empty. The face of a woman who has
    #        stopped spending the energy required to have the face show
    #        what the body is processing. The body is processing. The face
    #        is not displaying the processing.
    #        Aeron -- institutional. Across from an emptied woman. The
    #        gap between his institutional and her emptied is the scene's
    #        composition.

    # ========= VOICE BASELINE =========
    # Tessa: Flat. Quiet. Not affectless -- decided. The register of a
    #        woman who has already made the choice not to fight about this
    #        particular thing because the fight is something she has
    #        already finished in advance.
    # OB Aeron: Minimal. The same register as the ops room. Five spoken
    #           turns. He is the one asking questions. Tessa is answering
    #           without elaboration. The minimal is the scene's geometry.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE -- MESS HALL -- 0304]
    # Approximately thirty minutes after the forward base at Sector 9-North
    # goes dark. Tessa received the casualty report at 0246. She walked to
    # the mess hall at 0253. She has been at the back table since 0256.

    #scene bg_mess_hall_night with dissolve
    #play ambient "sfx/ambient/mess_hall_night.ogg" fadein 2.0

    # ========== PHASE 1 -- TESSA AT THE TABLE ==========

    "The mess hall at 0304 is empty except for Tessa."

    "The night staff is not on duty in the hall itself -- the serving line closed at 0100 and reopens at 0500. The tea station at the back of the hall is on its auto-cycle. The overhead strips are at the night setting, 20 percent. The only warm light in the hall is the small lamp at the tea station."

    "Tessa is at a two-seater table at the back of the hall, two tables from the tea station. She is facing the hall entrance. Her tray is in front of her. Her hands are on the edge of the tray."

    "She is not eating."

    "She was eating at 0258. She ate approximately one third of the lentils between 0258 and 0301. She stopped eating at 0301. She has not resumed since."

    "Her fork is on the tray. Her tea cup is half-empty. Her flatbread is untouched on its small plate."

    "She is looking at nothing."

    # --- TESSA'S INTERIOR ---

    tthought "I received the casualty report at 0246."

    tthought "I read it at my duty station."

    tthought "It had seven names. Third from the top was Siri Ondel."

    tthought "I read the name three times. I read the age once. I read the cause of death once. I read the recovery status once."

    tthought "The recovery status was: body not yet recovered. Forty-eight to seventy-two hour window. Recovery contingent on theater clearance."

    tthought "I put the report down on the duty station surface."

    tthought "I walked to the staff changing room."

    tthought "I sat in the staff changing room for six minutes."

    tthought "I did not cry. I did not shake. I did not do the things the body wants to do when a trainee has been killed, because the body has stopped asking for those things. The body has been in the register of the withdrawal since day three."

    tthought "I decided to withdraw on day three. I told Aeron I was withdrawing in a4_s16. I told him I would not touch the board. I told him I would stop keeping the counting human because I had been keeping the counting human as a service to an institution that had stopped wanting the counting to be human."

    tthought "I meant it."

    tthought "I meant it on day three and I meant it in a4_s16 and I mean it tonight."

    tthought "The withdrawal is not a thing I get to stop being in just because Siri Ondel is dead."

    tthought "The withdrawal is the thing that has to hold even more exactly tonight than it held on day three. If the withdrawal fails tonight then the withdrawal was never a withdrawal. The withdrawal was just a pause."

    tthought "I am not pausing."

    tthought "The test of a withdrawal is what the withdrawal does when the thing it was protecting you from walks into your medical wing at 0246 in a casualty report."

    tthought "The withdrawal holds or it does not hold."

    tthought "The withdrawal is going to hold."

    tthought "I am not going to the board. I am not going to write on the board. I am not going to move Siri's name from any column to any other column. I am not going to argue with Nyra's taxonomy. I am not going to engage the operational channel. I am not going to do any of those things tonight or tomorrow night or on any night that follows."

    tthought "I am going to eat my lentils."

    tthought "I am going to finish my tea."

    tthought "I am going to go to bed."

    tthought "Tomorrow I am going to work my shift at the medical wing and I am going to treat the patients in the bay and I am going to not look at the operational board."

    tthought "The not-looking is the work. The not-looking is what I am now paid in."

    tthought "I stopped eating at 0301 because I noticed I was chewing without tasting. The chewing was a body motion the body wanted to perform in order to not be the body of a woman whose trainee was just killed. The chewing was not eating. The chewing was avoidance."

    tthought "I do not need to avoid tonight. I need to hold."

    tthought "I am holding."

    tthought "The hold is empty. That is what the hold is supposed to be."

    # ========== PHASE 2 -- AERON ARRIVES ==========

    # CAMERA: the mess hall entrance at the far end of the hall. The doors
    # open. Aeron walks through. He walks across the hall to Tessa's table.

    "The mess hall entrance doors open at 0306:17."

    #play sound "sfx/mess_doors_open.ogg"

    "Aeron walks into the hall. He walks across the hall from the entrance to Tessa's table. The walk is approximately twenty paces. The hall is empty except for the two of them. His boots on the tile are the loudest sound in the hall."

    "He stops at Tessa's table."

    "He does not ask to sit. He pulls the chair opposite her and sits."

    "Tessa does not look up."

    "Aeron places his hands flat on the table surface -- the same posture Nyra used in the ops room in a4_s18, which Aeron also used alone after Nyra left. The posture has followed him from the ops room to the mess hall."

    "He sits across from Tessa in the posture of a commander who has just watched seven of his operators resolve to red on a tac display and who is now in a mess hall at 0306 in the morning at a table with the medic whose trainee was the third of the seven."

    "The posture is not a defense. The posture is a report."

    # --- AERON ---

    a "Siri Ondel is dead."

    "Four words. The sentence is not a question. It is a statement delivered by someone who has the institutional duty to report a death to a next-of-kin figure even when the next-of-kin figure is not legally related to the dead but is the person in the base who had the most to do with shaping the dead person's last three weeks of life."

    "Tessa does not look up."

    t "I know."

    "Two words. The answer is flat. The answer is confirmation that the casualty report reached her. The answer does not invite further conversation."

    # --- AERON ---

    "Aeron does not continue immediately. He is watching the top of Tessa's head -- she is looking at her tray, not at him, and his view is of her hair and the edge of her forehead."

    athought "She is not looking at me."

    athought "She is not looking at me not because she is avoiding me. She is not looking at me because she has already decided this conversation does not need eye contact."

    athought "The lack of eye contact is a decision. The decision is the same decision that produced her withdrawal in a4_s16."

    athought "I came here because the operational channel delivered the casualty report to the medical wing duty station at 0246 and I wanted to know where she went after she read it. I checked the wing. She was not in the wing. I checked the staff changing room. She had been there and left. I checked the mess hall on a guess and she is here."

    athought "I am here because I want to know whether the board has her on it at 0306."

    athought "The board will have her on it because the operational feed will have written SIRI ONDEL into OPERATIONAL-WITHDRAWN at 0301. I know this. I know this because I know the feed's update schedule."

    athought "I want to know whether there is a second entry. A hand entry. Tessa's hand."

    athought "Tessa is in the mess hall. Tessa is not at the board. Tessa's hand is not on the board."

    athought "Tessa has not added a hand entry. Tessa has not written Siri's name in any other column. Tessa has not written a sentence beside the name. Tessa is at the mess hall eating lentils."

    athought "Tessa's answer to the question I was going to ask has been given by the fact that she is in the mess hall."

    athought "I am going to ask the question anyway."

    athought "I am going to ask it because I want to hear the answer in her voice, not in her geography."

    a "Don't you want to mark her."

    "Five words."

    "The word mark is the word Tessa uses for what a medic does on a triage tag when a patient dies. The word mark is a technical term from her profession. The word is not a casual word for writing on a board. The word is the word a medic uses for the act of making a death official in the medic's own register."

    "Aeron is using Tessa's own word against the current state of Tessa's own withdrawal."

    "Tessa hears the word."

    "Tessa's fork, which has been resting on the edge of the tray, is picked up once. She lifts the fork approximately two centimeters off the tray. Then she puts it back down. The motion is not a decision to eat. The motion is the body's momentary registration that the word mark has hit the body."

    "Tessa looks up."

    "She looks at Aeron across the table. Her eyes are not wet. Her face is the empty face. The empty face is looking at him without displaying anything the face is processing."

    # --- TESSA ---

    t "I told you I wasn't going to touch the board. I meant it."

    "Thirteen words. The sentence is in the past tense about a future commitment. Both tenses are operating in the same sentence. The past tense is the promise she made in a4_s16. The present-tense extension of the promise is the thing she is doing right now in the mess hall by not being at the board."

    "She is keeping her word."

    "She is keeping her word at the moment when the keeping is the hardest thing to do, which is the only moment in which the keeping means anything."

    # --- AERON ---

    athought "She means it."

    athought "She means it in the way she means the things she means -- the flat precise meaning she has used for every clinical diagnosis she has ever delivered on this base. The meaning is not rhetorical. The meaning is a measurement."

    athought "The withdrawal is not a mood. The withdrawal is a commitment."

    athought "I am going to push her one more question because the push is the thing I came here to do. I want to know whether she has anything left for the particular girl who was her trainee."

    athought "If she does, the remainder will show in the answer."

    athought "If she does not, the remainder is gone and the gone is the report."

    a "She was your trainee."

    "Four words. Aeron's second and slightly gentler push. The sentence is true. The sentence is also an appeal -- an appeal to the specific relationship that Tessa had with Siri, which was not a relationship with the institution but a relationship with a nineteen-year-old who called Tessa Tess on day four."

    "Tessa hears the appeal."

    "Tessa does not respond to the appeal."

    "Tessa responds to the sentence on its literal level."

    # --- TESSA'S ANSWER ---

    t "She was a child who came to me because she thought I was going to keep the counting human."

    t "I am not keeping it human anymore."

    t "I stopped three days ago."

    t "I stopped when I decided to stop."

    t "The board is yours now. Do what you want with it."

    "Five sentences. Thirty-four words."

    "The sentences are delivered at the flat register of a medic reading out a chart update. The register does not have heat. The register does not have grief displayed on its surface. The register has grief as its substrate -- the grief is the floor the register is standing on. The register does not need to display the floor because the floor is what makes the register possible."

    "Tessa looks back at her tray. The eye contact is over. The eye contact lasted approximately eleven seconds."

    # --- AERON ---

    athought "She stopped three days ago."

    athought "Three days ago is Tuesday. Tuesday is the day Noelle rewrote the schema. Tuesday is the day a4_s09's precondition went live. Tuesday is the day I signed the Sector 12 sweep list."

    athought "Tessa noticed Tuesday."

    athought "Tessa did not tell me she noticed."

    athought "Tessa made the decision on Tuesday and carried the decision for three days and is telling me about the decision tonight because tonight is the night the decision is costing her a trainee."

    athought "The decision cost the trainee before the trainee was dead. The decision cost the trainee at the moment Tessa decided to stop keeping the counting human, because the counting being human was the thing that would have kept Tessa at the board and at the operational meetings and in the loop on the forward base staffing. The counting being human was Tessa's instrument for influencing the shape of the operation."

    athought "Tessa set the instrument down on Tuesday. On Tuesday the forward base was eleven days from its death. On Tuesday Tessa could still have influenced the forward base medical layout because the central-position recommendation could still have been revised."

    athought "Tessa knows this."

    athought "Tessa has known this since the casualty report arrived at 0246."

    athought "Tessa is carrying her own part in Siri Ondel's death and she is carrying it in the register of the withdrawal because the withdrawal is the only register the carrying can be sustained in."

    athought "If she came back to the board tonight she would have to also come back to the meetings and the staffing and the medical layouts. The coming back would not be a return to service. The coming back would be a claim that the withdrawal was not real. The claim would be a lie. Tessa does not tell lies."

    athought "She is not coming back."

    athought "She has told me the board is mine now."

    athought "The board is going to keep Nyra's taxonomy because Nyra is the one who built it and I am the one who signed the build and Tessa is the one who is no longer going to argue with it."

    athought "Tessa's role on the base is now: medic on duty, not voice in command."

    athought "The role has been reduced by the amount of voice it previously carried."

    athought "I am going to ask the last question. The last question is the question I did not come here to ask but am going to ask because the shape of the conversation has produced the question in me."

    a "Will you teach the next one."

    "Five words."

    "The next one is the next medic trainee who will arrive at Phoenix in the normal rotation cycle. The next trainee is not yet on the base. The next trainee will arrive in approximately eight days. Tessa will be on duty when the next trainee arrives. The trainee will be assigned to mentorship by the wing's senior medic. Tessa is the wing's senior medic."

    "The question is whether Tessa will accept the mentorship assignment."

    # --- TESSA'S ANSWER ---

    t "No."

    "One word."

    "The word is not decorative. The word is a clinical no. The word is the answer a medic gives when a procedure is not indicated. The procedure of mentoring the next trainee is not indicated. The reason the procedure is not indicated is not given. The reason does not need to be given. The word is enough."

    # --- AERON ---

    "Aeron does not respond. There is not a response to give. The no is a closure. Responding to a closure is re-opening the closure. He is not going to re-open."

    "Tessa picks up her fork."

    "She finishes her lentils in approximately two minutes. She eats at the same pace she was eating before Aeron arrived. She is eating because the tray is in front of her and the tray is a thing that has lentils on it and the lentils are a thing that can be eaten by a body that needs to continue being a body tonight."

    "She finishes the tea."

    "She does not touch the flatbread."

    "She stands."

    "The motion of standing is not abrupt. The motion is the motion of a person who has finished a task and is now moving on to the next task."

    "She picks up her tray. She walks from the back table to the tray return at the side of the hall. The tray return is approximately eight paces from her table."

    "She places the tray in the return slot. She turns. She walks to the hall entrance. The hall entrance is approximately twenty-two paces from the tray return."

    "She does not look back at the table."

    "She does not look at Aeron."

    "She walks through the hall entrance doors and the doors close behind her."

    #play sound "sfx/mess_doors_close.ogg"

    # ========== PHASE 5 -- AERON ALONE ==========

    # CAMERA: the empty table. Aeron still seated. The chair across from him
    # is empty. The tray is gone. The untouched flatbread is gone with the
    # tray. The lamp at the tea station is still on.

    "The hall is empty except for Aeron."

    "The table is empty except for Aeron's hands flat on the surface."

    "The chair across from him is empty. The seat is still warm. The seat will be not warm in approximately four minutes."

    "The tea station cycles on the hour. It is approximately 0312. The next cycle is at 0400. The hall will be empty for approximately forty-eight minutes."

    athought "She is not leaving angry."

    athought "She is leaving empty."

    athought "The empty is the thing I need to hold carefully because the empty is not a thing I can respond to with command language. Command language is built to respond to loud things -- anger, resistance, refusal-at-volume. Empty is not a loud thing. Empty is a quiet thing. Empty does not respond to command language."

    athought "Empty responds to one of two things: time, or the removal of the thing that emptied it."

    athought "I cannot remove the thing that emptied her. The thing that emptied her is the operational register I have built over the last four weeks. The register is the register that lost the forward base at Sector 9-North. The register is the register that cannot recover Siri Ondel for 48-72 hours. The register is the register that is going to write Siri Ondel into OPERATIONAL-WITHDRAWN and not into DEAD because DEAD is reserved for deaths on the medical wing's own floor."

    athought "I cannot remove the register because the register is the register that is holding the surviving assets on the east ridge extraction route right now at 0312. If I remove the register the assets do not make it back."

    athought "I cannot give her time either. Time is not the issue. Time will not return the withdrawal to engagement. Time will only deepen the withdrawal. The withdrawal has been deepening for three days. Tonight it has reached the medical wing's own trainee and it has held. A withdrawal that holds through the death of its own trainee is a withdrawal that is not going to be reversed by time."

    athought "The empty is the state."

    athought "The state is stable."

    athought "I came here to find out if the state had broken. The state has not broken. The state has received its worst test and has not broken. The state is what the state is going to be for the remainder of the operation."

    athought "Tessa is going to be on the medical wing as a medic. Tessa is not going to be in command meetings. Tessa is not going to be teaching the next trainee. Tessa is not going to be keeping the counting human."

    athought "The counting is going to be done in the register the operational channel uses. The register does not count humans. The register counts assets. Assets can be OPERATIONAL-WITHDRAWN. Humans can be nineteen."

    athought "I am going to walk back to the ops room in approximately two minutes."

    athought "I am going to finish tracking the east ridge extraction."

    athought "I am going to not-tell Nyra about this conversation because Nyra does not need this conversation to be a thing in her operational picture. Nyra has already written Tessa off as operationally inert. Nyra's picture of Tessa is now Nyra's picture, and Nyra's picture is accurate, and I am going to let the accuracy stand without complicating it with the fact that Tessa's voice at a back table in the mess hall at 0308 in the morning is a voice I am going to hear for the rest of my tenure in this role."

    athought "The voice is going to sit in me."

    athought "The voice said: 'I stopped three days ago. I stopped when I decided to stop.'"

    athought "The voice said: 'The board is yours now.'"

    athought "The voice said: 'No.'"

    athought "Three sentences. Each of them is a door that has been closed by the person standing on the other side of it. I am the person on this side. The doors are not going to open tonight."

    athought "The doors are not going to open on any night for the remainder of the operation. I am fairly sure of this. The fairly sure is ninety-plus percent."

    athought "I am going to carry the ninety-plus percent."

    # --- THE FINAL BEAT ---

    "Aeron's hands are still on the table."

    "He does not lift them."

    "He looks across the table at the empty chair. The chair is across the table from him. The chair has been empty for approximately three minutes. The chair is going to be empty for the rest of the conversation he is not having with Tessa because Tessa is gone and the conversation is over."

    "He looks at the chair for approximately twelve seconds."

    "Then he stands."

    "He pushes his own chair back. The chair scrapes slightly on the tile. He walks across the hall from the back table to the entrance. Twenty paces. He does not look back at the chair. He does not look back at the table. He does not look at the tray return."

    "He reaches the doors. The doors open. He walks through."

    #play sound "sfx/mess_doors_close.ogg"

    "The mess hall is empty."

    "The tea station cycler continues. The overhead strips at 20 percent. The warm tea station lamp."

    "The empty chair at the back table."

    # --- TP SEED ---

    $ tp_seed("a4.ob.tessa.empty_not_angry")

    # ========= STATE UPDATES (BRANCH B) =========
    $ canon_set("ob.tessa.will_not_teach_the_next_one", True)
    $ canon_set("ob.tessa.stopped_three_days_ago", True)
    $ canon_set("ob.tessa.board_is_yours_now", True)
    $ canon_set("ob.tessa.withdrawal_held_through_trainee_death", True)
    $ canon_set("ob.aeron.confirmed_tessa_empty_not_angry", True)
    $ rel_bump("Tessa", trust=-1, complicity=-2)
    $ flag("a4_ob_tessa_empty_siri_ondel", True)
    $ npc_remember("Tessa", "refused_to_mark_siri_on_the_board", tone="withdrawal_that_holds")
    $ npc_remember("Tessa", "no_to_the_next_trainee", tone="clinical_closure")
    $ npc_remember("Aeron", "tessa_empty_not_angry_mess_hall_3am", tone="state_is_stable")
    $ scene_mark(_current_scene_id, "exited")
    jump a4_s19_tessa_the_trainee_ob_end


# ===========================================================
# SHARED END
# ===========================================================
label a4_s19_tessa_the_trainee_ob_end:

    #stop ambient fadeout 3.0
    #scene black with fade

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s19_tessa_the_trainee_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Immediately after a4_s18. 0302 to 0312. Tessa received the Siri
#     Ondel casualty report at 0246 via the medical wing duty station.
# cann.what_happened:
#   - Conditional beat on ob.tessa.choice from a4_s16/a4_s17.
#   - BRANCH A (stay_and_resist): Tessa walks to the medical wing's
#     operational board at 0302 with the marker she has been carrying in
#     her coat pocket for eleven days. She writes SIRI ONDEL in the LIVING
#     column -- not the DEAD column, not the OPERATIONAL-WITHDRAWN column
#     (where the automated feed has already placed her). Beside the name
#     she writes SHE WAS NINETEEN. The column is wrong and the wrongness
#     is the assertion -- she is refusing the operational taxonomy at
#     its root. Aeron arrives at 0308. He reads the entry. He walks to
#     the board. He takes the marker from Tessa's hand when she is done.
#     He writes nothing. He does not correct the column. He caps the
#     marker. He sets it on the shelf. Exchange:
#       Tessa: "She is not operational. She is nineteen. She is nineteen
#              and she is dead."
#       Aeron: "I know."
#       Tessa: "Do you."
#       Aeron: "I am trying to."
#       Tessa: "Try harder."
#     Tessa leaves. Aeron alone at the board. The contradiction persists.
#   - BRANCH B (stay_but_withdraw): Tessa does not go to the board. She
#     sits alone at a back table in the mess hall at 0304 eating a
#     standard night-staff tray. Aeron finds her. Sits across from her
#     without asking. Exchange:
#       Aeron: "Siri Ondel is dead."
#       Tessa: "I know."
#       Aeron: "Don't you want to mark her."
#       Tessa: "I told you I wasn't going to touch the board. I meant it."
#       Aeron: "She was your trainee."
#       Tessa: "She was a child who came to me because she thought I was
#              going to keep the counting human. I am not keeping it
#              human anymore. I stopped three days ago. I stopped when I
#              decided to stop. The board is yours now. Do what you want
#              with it."
#       Aeron: "Will you teach the next one."
#       Tessa: "No."
#     Tessa finishes her meal. She leaves. She does not leave angry. She
#     leaves empty. Aeron alone at the table.
# cann.tessa_state:
#   - BRANCH A: active resistance at the medical wing's root -- the
#     board. Refuses the operational taxonomy by writing in the wrong
#     column and leaving the contradiction on the board's face. Still
#     instructing Aeron ("try harder") -- the instruction is generosity.
#   - BRANCH B: the withdrawal holds through the death of her own
#     trainee. She does not go to the board. She keeps her word from
#     a4_s16. She says no to teaching the next one. She leaves empty,
#     not angry. The empty is stable.
#   - Both branches: Siri Ondel was nineteen. Tessa recommended the
#     central mess position for the medic trainee slot on forward base
#     layouts last month. Her recommendation is one of the reasons Siri
#     died in the second wave. Tessa carries this -- differently in each
#     branch.
# cann.aeron_state:
#   - BRANCH A: does not correct the board. Caps the marker and sets it
#     on the shelf -- the only thing his hand can do that is not a
#     correction. Says "I am trying to." Holds Tessa's "try harder" as
#     a deferred answer. The deferral is the answer.
#   - BRANCH B: confirms the withdrawal is stable. Decides he cannot
#     remove the register that emptied Tessa because the register is
#     holding the surviving east ridge extraction. Tessa's voice -- "I
#     stopped three days ago. I stopped when I decided to stop. The
#     board is yours now. No." -- is going to sit in him.
# cann.thematic_flags:
#   - THE WRONG COLUMN (Branch A). Tessa refuses the taxonomy by writing
#     in the wrong column. The wrongness is the refusal. An argument
#     would have accepted the premise of the columns. The refusal does
#     not accept the premise.
#   - SHE WAS NINETEEN. The witness sentence. A past tense verb in a
#     LIVING column entry -- the contradiction that makes the board
#     un-processable by the operational feed. Tessa's hand creates a
#     thing outside the feed's processing range.
#   - TRY HARDER (Branch A). The instruction as generosity. Tessa is
#     still giving Aeron directional instruction. The direction
#     acknowledges there is a direction. The acknowledgment is the last
#     thing she is giving him.
#   - I STOPPED THREE DAYS AGO (Branch B). Tuesday. The day Noelle
#     rewrote the schema, the day the Sector 12 sweep list was signed.
#     Tessa made her private decision the same day the operational
#     register crossed its threshold.
#   - THE BOARD IS YOURS NOW (Branch B). Final surrender of influence.
#     Tessa is withdrawing from the shape-of-the-operation contest. The
#     contest is now Aeron's alone.
#   - EMPTY NOT ANGRY (Branch B). The state is stable. Stable empty does
#     not respond to command language. Command language is built for
#     loud things. Empty is quiet. The commander cannot reach it.
#   - NINETEEN AS WEIGHT (both). The scene distinguishes between having
#     the information (Aeron) and having the weight of the information
#     (Tessa). Aeron has the information. Aeron does not yet have the
#     weight. The distinction is the scene's moral center.
# cann.character_moments:
#   - Tessa (A): the marker in her coat pocket for eleven days. The
#     letters in the capital hand of a medic writing a triage tag. The
#     past-tense verb in the LIVING column.
#   - Tessa (B): picking up the fork on the word 'mark' and putting it
#     back down. The flat precise register. The tray in the tray return.
#     The twenty-two paces to the door without looking back.
#   - Aeron (A): capping the marker and setting it on the shelf without
#     correcting the column. "I am trying to." The deferral.
#   - Aeron (B): sitting across the small table without being invited.
#     "Will you teach the next one." The chair empty at 0312.
# cann.callbacks:
#   - a4_s06: Nyra's operational board overwrite. Branch A contests it at
#     the root. Branch B accepts the surrender.
#   - a4_s16/a4_s17: ob.tessa.choice. The decision made in those scenes
#     is the decision tested here.
#   - a4_s18: the seven dead, Siri Ondel third from the top in the
#     OPERATIONAL-WITHDRAWN column.
#   - a4_s10: "this is how it happens" / "I know." Branch A has Aeron
#     using the same "I know" for Tessa. The two-word sentence is
#     becoming his response to witnessing without defense.
#   - a3: Tessa's running arc of keeping the counting human. The
#     counting being human is the instrument she set down on Tuesday.
# cann.block_status:
#   - ANCHOR. Always plays on OB path. Branches on ob.tessa.choice.
#     Must play after a4_s18 and before a4_s20.
# cann.requires_followup:
#   - The contradiction on the board (Branch A): does anyone else read
#     the entry? Does Nyra see it? Does Noelle?
#   - Tessa's refusal to teach the next trainee (Branch B): the next
#     trainee arrives in approximately eight days. The wing senior medic
#     position and the unclaimed mentorship.
#   - Aeron carrying "try harder" (A) or "I stopped three days ago" (B)
#     into subsequent scenes.
