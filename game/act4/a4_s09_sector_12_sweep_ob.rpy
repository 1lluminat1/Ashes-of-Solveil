# =======================================================
# ACT 4 - Scene 09: Sector 12 Sweep (Obedience Path)
# File: a4_s09_sector_12_sweep_ob.rpy
# Path: OB
# Type: OPERATION -- PREEMPTIVE STRIKE (civilian inclusion)
# Character Focus: Aeron (signer), Nyra (tactical),
#                  Noelle (framework / target list), Zira (ground interdiction)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s09_sector_12_sweep_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy

label a4_s09_sector_12_sweep_ob:
    $ show_timeline("DAY 46", "04:47", "Sector 12 — Operations")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, locked tripod. The ops table wide. Opens on the table from
    #         overhead -- the sector map projected on the glass surface, figures
    #         arranged around it as pieces, faces lit from below. The overhead
    #         wide holds for the pre-strike briefing. Coverage breaks into singles
    #         only twice: the moment Aeron reads the target list and the moment
    #         he signs it. The operation itself is covered at the table, not in
    #         the field. There are no cutaways to Sector 12. The violence is not
    #         shown. The violence is read on the map as small icons changing
    #         colour. The violence is heard in the audio channels Nyra routes
    #         through the table speaker, low. The violence is never framed.
    # LIGHTING: Ops room. Tactical blue at 100%. The table glass lit from below
    #           in amber-for-target, blue-for-friendly, grey-for-civilian. The
    #           grey is a deliberate colour choice. Noelle chose it three weeks
    #           ago when she rebuilt the target classification schema.
    # SFX: Loop -- ops room hum (cold), table projection low hum, the comm
    #      channels open at low volume (Zira's ground team, the strike element,
    #      the overwatch relay). One-shots -- stylus placements, the target
    #      list datapad sliding across the table once, the signature (one
    #      stroke, OB-register), the first breach at 0600:04, the last casualty
    #      confirmation at 0622:11, Aeron's one spoken word post-strike.
    # FX/COMP: The table surface is a high-resolution projection of Sector 12
    #          and its three sub-quadrants. The forward post is marked in amber
    #          at the NE junction of sub-quadrant 12-B. Three grey icons in
    #          sub-quadrant 12-C -- the collaborators. Their IDs resolve to
    #          names on the target list datapad. The names are specific. The
    #          names have professions.
    # BLOCKING: Aeron at the head of the ops table. Nyra to his right -- she is
    #           running the tactical overlay, not a briefer. Noelle at his left
    #           -- her tablet connected to the table projection. Zira is not
    #           at the table. Zira is in the ground interdiction staging area
    #           across the base; her voice is on the comm channel only. Her
    #           absence from the table is the only negotiation she has left.
    # CANON: The preemptive strike authorized in a4_s03. Flawless execution.
    #        22 minutes. Zero Phoenix casualties. 17 Echelon dead. 3 civilians
    #        on the target list -- pre-authorized, signed. The scene is about
    #        the signing, not the shooting.
    # FACE: Aeron -- reading the list. The beat where he could push back.
    #        Noelle -- watching him to see if he will. Nyra -- already past the
    #        question; her attention is on the tactical clock. Zira -- only a
    #        voice. The voice is tight.

    # ========= VOICE BASELINE =========
    # OB Aeron: The signing is the voice. One word post-strike ("Clean.").
    # Nyra: Tactical, crisp. She repeats "Clean" back, quietly. Ends scene with
    #        the civilian-framing line.
    # Noelle: Functional. Her framework is the spine of the operation. She
    #         reads the beat when Aeron could object. She is watching.
    # Zira: Voice-only. Ground interdiction. Tight. She executes the cordon.
    #        She does not celebrate.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE -- OPS ROOM -- 0537]
    # Twenty-three minutes before breach. The ops table is lit. The target
    # list is on a separate datapad to Aeron's right.

    #scene bg_ops_room_ob_predawn with dissolve
    #play ambient "sfx/ambient/ops_room_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE PRE-STRIKE BRIEFING ==========

    "0537. The ops room is at operational brightness."

    "The table projection is running Sector 12 in full resolution -- the three sub-quadrants, the forward post, the approach vectors Nyra's strike element will use, the overwatch positions, the ground interdiction cordon Zira's operators have already moved into."

    "The operation window opens at 0600. Twenty-three minutes from now."

    "Aeron stands at the head of the table. He has not sat down this morning. He has been standing at this table for two hours, reading the approach geometry once on the overnight shift, then walking the base perimeter for forty minutes, then returning to the table. The walk is a thing he does now before operations. He does not call it a ritual. He calls it a check."

    #show aeron ops_head_standing with dissolve
    #show nyra ops_tactical_right with dissolve
    #show noelle ops_analytics_left with dissolve

    "Nyra is to his right. Her hands are on the table, one at the tactical overlay controls, the other resting on the margin of the projection. She has been awake as long as Aeron has. The sleep debt does not show on her. The sleep debt rarely does."

    "Noelle is to his left. Her tablet is open, connected to the table projection via the physical port on the table's edge -- Noelle prefers a physical connection for operations. The wireless layer, she has said on three occasions, introduces a forty-millisecond latency she does not want in her decision loop."

    "The forty milliseconds matter to her. They have not yet mattered to anyone else."

    # ========== PHASE 2 -- NYRA BRIEFS ==========

    ny "Final pass."

    "She taps the table. The projection zooms to the approach geometry for sub-quadrant 12-B -- the forward post."

    ny "Breach element at 0600:00. Strike at 0600:04. Overwatch positions alpha and bravo are live at 0555. Ground interdiction cordon at 0558. Zira's cordon is sealed at 0559:30. Thirty-second margin before breach is the margin we agreed on last week."

    ny "The forward post has fourteen Echelon line personnel and three civilians working in the logistics sub-node. Civilians have been present in the sub-node every day for the last eleven days according to the Ghostline pattern intercepts Zira's operators captured in the approach phase."

    ny "Noelle's target classification is on the list datapad."

    "She does not look at the target list. She has seen it. She is not the person who generates it."

    ny "The operation is scheduled to complete at 0622:00. That is twenty-two minutes from breach. The twenty-two-minute figure comes from Noelle's framework."

    n "0622:11 if you include the final casualty confirmation window. Twenty-two eleven is the closed-out figure. I will use twenty-two flat for the external briefing."

    ny "Acknowledged. Twenty-two for external. Twenty-two eleven for internal."

    # --- ZIRA ON COMM ---

    #play sound "sfx/comm_ground_team_check_in.ogg"

    z "(over comm) Ground interdiction checking in. Cordon elements at staging. Ready to move at 0557 on your mark."

    "Her voice is on the table speaker at low volume. The voice is tight. It is not afraid. It is the particular tightness of a voice that has been holding a position for five hours in cold pre-dawn air and has been thinking about the target list the whole time."

    ny "Acknowledged, Voss. Mark will come from this table. Hold staging."

    z "(over comm) Holding."

    "The comm channel stays open. Zira does not close it. The low channel hiss is the sound of her waiting."

    # ========== PHASE 3 -- THE TARGET LIST ==========

    "Nyra slides the target list datapad across the table to Aeron."

    "The motion is the same flat two-handed geometry from a4_s01. The scene has inherited the geometry."

    ny "Target list requires ratification at 0540 per the operational window protocol. Three minutes from now."

    "Aeron does not reach for the datapad immediately."

    "He looks at it."

    "The datapad is face-up. The target list is visible at the top of the first page. The list is ordered by target category: primary (Echelon line personnel), secondary (Echelon logistics personnel), tertiary (collaborators)."

    "The tertiary category has three entries."

    # --- NOELLE WATCHES ---

    # CAMERA: single on Noelle. She is watching him read. Her stylus is still.

    nthought "He is reading the tertiary category."

    nthought "The tertiary category has three entries. I classified them as tertiary rather than secondary on Tuesday evening when I was rebuilding the schema. The secondary classification would have placed them with the logistics personnel, which would have made them a collateral category rather than a target category. The tertiary classification places them on the target list directly."

    nthought "I am watching him to see if he flags the distinction."

    nthought "He is reading the datapad."

    nthought "He has been reading the datapad for fourteen seconds."

    nthought "The ratification window is three minutes. Fourteen seconds is a reasonable read time for a target list of this length. The fifteenth second would begin to register as hesitation. The twentieth second would register as pushback."

    nthought "I am counting to twenty."

    # --- AERON READS ---

    # CAMERA: single on Aeron. Close enough to see the eyes move.

    athought "Tertiary -- three."

    athought "The first name is Jaren Okho. Logistics clerk. Male, forty-four, married to an Echelon administrative officer at the sub-prefecture. His name appears in fourteen Ghostline intercept records as a passive conduit -- moving routing information from the logistics sub-node to the administrative officer, who files it as standard weekly reports that are read by Echelon intelligence."

    athought "The second name is Mira Telven. Sanitation supervisor. Female, thirty-one. Unmarried. Her name appears in nine Ghostline intercepts as an active conduit -- she carries signal packets in the sanitation logs. The packets are low-density. Low density is not zero density."

    athought "The third name is Orin Dask. Cook. Male, fifty-seven. His name appears in two intercepts. Two is the threshold Noelle used when she rebuilt the schema on Tuesday. Two meets the threshold. One would not."

    athought "The cook meets the threshold with two intercepts."

    athought "The cook is fifty-seven years old and feeds the fourteen Echelon line personnel at the forward post three meals a day."

    athought "The cook is fifty-seven."

    # --- THE BEAT ---

    "Aeron does not look up from the datapad."

    "Nyra is standing to his right in the peripheral field of his vision. Noelle is standing to his left in the peripheral field of his vision."

    "He is aware that Noelle is watching him."

    "He is aware that Noelle knows the distinction between secondary and tertiary is a judgment call and that she chose tertiary and that she is waiting to see whether he will ask her why."

    athought "The question I could ask is: why did you classify the cook as tertiary rather than secondary."

    athought "If I ask it, she will tell me the two-intercept threshold is what the schema requires. She built the schema. The schema is correct. The schema is correct because she built it the way she builds everything: in a shape where the answer is the shape."

    athought "If I ask it, she will also know I asked it. She will not write the asking into her report. She will write it into a different place. She will write it into the variance log she keeps for me and does not show anyone."

    athought "The variance log is the thing she is building. The variance log is the reason the schema is correct."

    athought "If I ask, I give the variance log a new entry."

    athought "If I do not ask, the variance log holds steady and the schema stays clean and Zira's cordon closes at 0559:30 and Nyra's strike element breaches at 0600:04 and the cook is dead by 0612 at the latest."

    athought "The cook is fifty-seven."

    athought "The cook will be dead by 0612 regardless of whether I ask."

    athought "The question is whether Noelle's variance log gets a new entry for my asking."

    athought "That is not the question."

    athought "That is the question I would like to be the question. The actual question is whether I will object to the inclusion."

    athought "I will not object to the inclusion."

    athought "I know I will not object because I have already signed the authorization that made the inclusion a pre-authorized event when I approved the schema rewrite on Tuesday at 1147. The signature at 1147 Tuesday is the signature this signature ratifies. This morning's signature is a redundancy. The objection I could raise would be an objection to my own signature from three days ago."

    athought "I am not in the business of objecting to my own signatures."

    athought "Noelle knows that. That is why she is watching. She is watching to see if I notice that the objection is mechanically impossible."

    athought "I notice."

    athought "I do not flag the noticing."

    # ========== PHASE 4 -- THE SIGNATURE ==========

    "Aeron picks up the stylus."

    "The motion is unhurried."

    "He does not scroll the datapad. He does not zoom on the tertiary entries. He does not ask Noelle to walk him through the intercept basis for the cook."

    "He signs."

    #play sound "sfx/stylus_signature_single.ogg"

    "One stroke. A, slash, R. The OB-register signature. The same three marks he used on a4_s02."

    "He slides the datapad back across the table toward Nyra."

    "The datapad comes to rest beside her tactical overlay controls."

    ny "Target list ratified."

    n "Ratification logged at 0541:08."

    # --- NOELLE'S INTERIOR READ ---

    nthought "Eighteen seconds. He read for eighteen seconds. The window closed at twenty. He finished at eighteen."

    nthought "He did not ask the question about the cook."

    nthought "He knew there was a question about the cook. I could see it in the second pass his eyes made across the tertiary entries. The first pass was intake. The second pass was a check. He was checking himself."

    nthought "The check resolved in favor of the schema. In favor of me."

    nthought "The variance log does not get an entry for this morning."

    nthought "The variance log is approaching the point where it does not need to be kept."

    nthought "I notice I am relieved."

    nthought "I am not going to interrogate the relief this morning. The operation opens in nineteen minutes."

    $ tp_seed("a4.ob.op.civilian_list_signed")

    # ========== PHASE 5 -- THE FINAL CHECK ==========

    "Aeron looks at the table projection for the first time since picking up the datapad."

    "Sector 12. The forward post in amber. The three grey icons in sub-quadrant 12-C -- no, two of them are now in the forward post itself, because the cook and the sanitation supervisor are inside the forward post during breakfast service. The grey icons migrated overnight and the projection has updated."

    "The forward post has fourteen blue hostile icons, three grey civilian icons, and zero friendly icons."

    "The approach vectors resolve into the breach point at 0600:04 in real time on the projection. Nyra's strike element is staged at the approach margin already. Zira's cordon is tightening on the projection in the last ninety seconds before seal."

    a "Status on overwatch."

    "First Aeron line of the scene. Operational."

    ny "Alpha and bravo are both live. Bravo has visual on the forward post north face. Alpha has visual on the logistics sub-node."

    a "Interdiction cordon."

    z "(over comm) Closing. Seal at 0559:30 as briefed."

    a "Strike element."

    ny "Breach at 0600:04. Clearance doctrine is standard for forward post engagement."

    "The word standard does some work in that sentence."

    "Standard clearance doctrine, on the OB path, as rewritten in a3_s07 through a3_s12 and ratified in a4_s02, does not distinguish between hostile and civilian once the target list has been ratified. Everyone on the target list is cleared on the same protocol. The protocol is one of the things Nyra doctrinalized."

    a "Execute."

    "One word."

    "The operation is committed."

    # ========== PHASE 6 -- THE STRIKE (0600 TO 0622:11) ==========

    # CAMERA: overhead wide on the table projection. No cutaways to the field.
    # The violence is read in the icons and heard in the comm channel.

    "0558."

    "The overwatch positions report green. The cordon tightens. Zira's voice on the comm is short, clean, operational."

    z "(over comm) Cordon seal at 0559:30."

    "0559:30."

    z "(over comm) Seal confirmed. Hold for breach mark."

    ny "Breach at four."

    "0600."

    "0600:04."

    #play sound "sfx/breach_charge_distant.ogg"

    "The forward post icon on the projection pulses once -- white, then amber, then the first blue hostile icon flickers and darkens to grey. Grey is the death colour on Noelle's schema. The schema uses grey for both civilian and fatality. The overlap is not an accident. It is a classification efficiency Noelle implemented in Tuesday's rewrite."

    "A second blue icon darkens to grey at 0600:07."

    "A third at 0600:09."

    "The strike element is inside the forward post by 0600:12."

    # --- THE QUIET OPERATION ---

    "The room does not speak."

    "Nyra tracks the icons. Her hand on the tactical controls makes three micro-adjustments -- a breach team move to secondary structure, an overwatch re-target, a cordon pressure increase on the south-west line. Each adjustment is a tap. Each tap is a life ending on the projection."

    "Aeron watches the projection. He does not move."

    "Noelle is not watching the projection. Noelle is watching her own tablet, where the casualty tabulation runs in a column beside the timestamp log. Her stylus is moving now. She is recording the timestamps of each grey transition. The recording is the framework validating itself in real time."

    "The comm channel carries the operational traffic at low volume."

    ny "(low, to the room) First pass clean. Eight confirmed down. Six remaining."

    "0604."

    "The strike element moves from the main structure to the logistics sub-node. The projection shows two grey-civilian icons becoming grey-fatality -- the classification does not change because the icons were always the same grey. The schema efficiency is showing its value."

    athought "The cook. That was the cook. The cook was in the kitchen of the logistics sub-node preparing breakfast for the fourteen Echelon line personnel at 0604 because the breakfast service begins at 0605. He was seventeen seconds early on his own schedule this morning."

    athought "Seventeen seconds did not save him."

    athought "I am aware of the specific seventeen-second margin because Noelle mapped it in the approach phase Monday. The cook's morning routine was on the slide."

    athought "I looked at the slide."

    athought "I did not ask about the cook when the slide was presented."

    athought "I could have asked on Monday. I could have asked this morning. I did not ask on either day. The not-asking is the signature."

    # --- NYRA, QUIET ---

    ny "(low) Second pass. Eleven down."

    "0609."

    ny "(low) Thirteen. Three remaining in the secondary structure."

    "0614."

    z "(over comm) Cordon holds. No breakthrough. Two hostile attempting east corridor."

    ny "Alpha, take the east corridor."

    #play sound "sfx/overwatch_engagement_low.ogg"

    ny "(low) Fifteen. Two remaining."

    "0619."

    z "(over comm) East corridor clear. No exfil."

    ny "(low) Sixteen. One remaining."

    "0621."

    ny "(low) Seventeen. Primary clearance complete."

    "0621:40."

    n "Tertiary tabulation is complete. Three grey-civilian confirmations at 0604:22, 0604:39, and 0611:08. All three inside the forward post envelope at time of breach. No displaced civilians in the cordon."

    # ========== PHASE 7 -- THE ONE WORD ==========

    "0622:11."

    n "Operation closed out at twenty-two eleven."

    "The projection resolves. The forward post is now a grey field with seventeen hostile fatalities and three civilian fatalities and zero Phoenix casualties. Nyra's strike element is beginning the cleanup phase. Zira's cordon is holding the perimeter for another six minutes while the strike element sweeps the structure for residual hostiles and collects operational intelligence."

    "The room does not celebrate."

    "The room executes its cleanup procedures."

    "Nyra sends the after-action prompt to the strike element lead. Noelle timestamps the casualty tabulation and begins routing the intelligence collection brief to her tablet. Zira on the comm channel requests permission to collapse the cordon in six minutes. Nyra grants it."

    "Aeron has not spoken since 'execute.'"

    "The signature datapad is still on the table beside Nyra's tactical controls. The target list is still the top page. The three tertiary names are still on the list."

    # --- AERON'S ONE WORD ---

    "He speaks."

    a "Clean."

    "One word. Flat. Not approval. Not satisfaction. The operational word that means the operation executed within its predicted parameters without deviation and without mess that will require cleanup beyond the standard protocol."

    "Nyra, who has been running the tactical overlay for the last twenty-two minutes without speaking to Aeron directly, glances at him for the first time since breach."

    "She repeats the word back."

    ny "(quietly) Clean."

    "The repetition is not agreement. It is not validation. It is the doctrinal echo -- the room confirming to itself that the word has been said and is now a part of the after-action record."

    # --- NOELLE MARKS THE BOARD ---

    "Noelle does not repeat the word."

    "Noelle, on her tablet, opens a small private board -- a whiteboard application she has been keeping since the Tuesday schema rewrite. The board has a column labeled TERTIARY-CONFIRMED."

    "She adds three names to the column."

    "Jaren Okho."

    "Mira Telven."

    "Orin Dask."

    "The board now has seven names total. The previous four were from the operations of the last ten days. Noelle has been keeping the board since the schema rewrite because the schema does not preserve tertiary names in the operational record beyond the ratification log, and she wanted the names preserved."

    "She has not explained the board to anyone."

    "She has not explained it to herself, either -- not in a way she considers adequate. The explanation she has offered herself, when she has noticed herself writing names on the board, is that the board is a quality assurance mechanism for the schema. That the board allows her to verify that the tertiary classification is being applied consistently across operations."

    "The explanation is not wrong."

    "The explanation is also not the reason."

    nthought "I am keeping the names."

    nthought "I am keeping them because keeping them is a thing the schema does not require, and I am a woman who has built a schema, and the schema does not contain the part of me that is keeping the names."

    nthought "The part of me that is keeping the names is the part of me that is going to write the doctrine tomorrow."

    nthought "I do not know I am going to write a doctrine tomorrow. I am having that thought now, at 0624 this morning, because the three names I just added to the board are the three names that completed the threshold I had privately set for when I would stop being an analyst and start being whatever I become after being an analyst."

    nthought "Seven names was the threshold."

    nthought "The threshold is now met."

    nthought "I will write the doctrine tomorrow."

    nthought "I notice I am not afraid of the thought. I notice the absence of fear is new."

    $ tp_seed("a4.ob.noelle.seven_names")

    # ========== PHASE 8 -- THE FRAMING LINE ==========

    # CAMERA: return to the overhead wide. The room quiet. The table projection
    # still rendering the forward post field in grey.

    "The operation is closing out. The strike element is reporting the residual sweep as clean. Zira has collapsed the cordon and is walking back to the staging area with her ground interdiction elements. She has not spoken on the comm channel since 'east corridor clear.'"

    "The comm channel is still open."

    "At the ops table, the room is beginning to transition to the next operational window. Aeron is still at the head of the table. Nyra is at his right. Noelle is at his left. The target list datapad is still on the table."

    "Nyra taps the datapad once. The ratified list closes. The next operational window -- the day-three Sector 4 consolidation -- begins populating the table projection."

    "Nyra speaks. Not to Aeron. To the room, in the institutional register she has been using since s02."

    ny "One thing for the record."

    "Aeron looks at her."

    "Noelle looks at her."

    "Zira, on the open comm, does not speak. But the channel hiss remains open."

    ny "The word 'civilian' was a useful framing when we needed to appear restrained."

    "She does not pause for effect. The sentence is delivered at operational cadence."

    ny "We no longer need to appear restrained."

    "The sentence lands on the table."

    "It does not land on the projection. It does not land in the after-action record. It lands in the air of the ops room and the air of the ops room does not move."

    # --- THE ROOM'S RESPONSE ---

    "Aeron does not agree."

    "Aeron does not disagree."

    "Aeron's face does the thing it has been doing since s02 -- the still, un-animated, institutional face that is no longer reading as the mask because the mask has become the underlying surface."

    athought "She is saying the thing that I have already signed into policy."

    athought "The saying is late to the signing. The saying is the kind of saying that formalizes what has been procedural. It is what Nyra does. She names rooms."

    athought "I do not need to respond to the naming. The naming is self-ratifying. The response is the continuation of the operational tempo."

    "Aeron returns to the table projection."

    "The day-three Sector 4 consolidation is now fully populated. Noelle's analytical layer is already annotating the approach geometry with the latest Ghostline pattern data. Nyra's tactical controls are already accepting her micro-adjustments."

    "Aeron places his hand on the table edge. Reads the new projection."

    a "Day three. Walk me through the approach."

    ny "Approach vector is clean. Entry at the north corridor, Ghostline relay shift happens inside the operational envelope at 1140, strike window at 1155 to 1204. Noelle's load model predicts a single-pass clearance."

    a "Civilian exposure."

    "The word is now functional, not ethical. The word has been re-priced by Nyra's framing line three sentences ago. The word means: what is the count, for planning purposes."

    n "Two. Secondary sub-node. Both on the pattern board."

    a "Threshold."

    n "Three-intercept for the first, two-intercept for the second. Both meet schema."

    a "Ratify at 0900."

    "He has not responded to Nyra's framing line. He has also not objected to it. The two absences, together, are the ratification."

    # ========== PHASE 9 -- ZIRA ON THE CHANNEL ==========

    "The comm channel is still open."

    "Zira is walking back from the cordon position. Her breath is audible on the channel -- the pre-dawn air is cold and her breath carries. She has not spoken since the east corridor clear call."

    "She speaks now. Not to anyone in particular. The channel is an open channel and she knows the ops room is listening."

    z "(over comm) Voss clear of the staging area. Returning to base. Out."

    "One line. Operational. Nothing else."

    "But the line carries a small tight register that Aeron would have been able to read a week ago and that this morning he chooses not to read. The register is the register of a woman who has just heard her co-commander's framing line on civilians and has not decided what to do with it."

    "She does not offer the undecided thing to the channel."

    "She closes the channel. The hiss cuts."

    # --- AERON'S INTERIOR ON ZIRA ---

    athought "Zira did not respond to Nyra's line."

    athought "The non-response is the response. Zira heard the line and closed the channel and is walking back to base in cold pre-dawn air and will be at her station by 0715 and will not come to the ops room to discuss the line."

    athought "I notice I am grateful that she is not coming to the ops room."

    athought "The gratitude is the tell."

    athought "I am becoming administratively fluent in the gratitude."

    # ========== PHASE 10 -- THE TABLE RETURNS TO WORK ==========

    "The table projection runs the day-three Sector 4 consolidation approach."

    "Noelle's stylus is moving again. Annotations. Load calculations. The analytical layer is taking shape for the next ratification at 0900."

    "Nyra's tactical controls are adjusting the cordon positions for the north corridor entry."

    "Aeron leans over the table. His hand is on the table edge. His face is lit from below by the projection glass."

    "The light is blue for friendly and amber for target and grey for civilian."

    "The light on Aeron's face is blue and amber and grey in rotation as his eyes move across the projection."

    "He reads the approach geometry."

    "He returns to the table for the next operation."

    "That sentence is the end of the scene."

    # ========== PHASE 11 -- COdA ==========

    # CAMERA: slow pull-back from the ops table. The three figures around the
    # projection. The blue light. The target list datapad on the table edge,
    # face-down now, the tertiary entries no longer visible.

    "The ops room hum."

    "The low comm channel to Zira's base-return path is closed. The comm channel to the next operational window is already populated by Nyra's updated orders."

    "Noelle's private board is not visible to the camera. The three names are on it. The board is a thing the scene has seen and the scene will not see again for the length of the ops room hum."

    "The operation has closed out. The word has been said. The word has been repeated. The framing has been dropped. The next operation is populating."

    "The base functions."

    "The base functions is not the same as living."

    "Aeron has stopped noticing the distinction."

    "The not-noticing is the metric."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.sector_12.operation_complete", True)
    $ canon_set("ob.sector_12.duration_minutes", 22)
    $ canon_set("ob.sector_12.phoenix_casualties", 0)
    $ canon_set("ob.sector_12.echelon_dead", 17)
    $ canon_set("ob.sector_12.civilian_deaths", 3)
    $ canon_set("ob.nyra.civilian_framing_dropped", True)
    $ canon_set("ob.aeron.civilian_list_signed", True)
    $ canon_set("ob.noelle.private_tertiary_board", 7)
    $ metric("ob.aeron.civilian_ledger", add=3)
    $ flag("a4_ob_sector_12_sweep", True)
    $ rel_bump("Nyra", trust=1)
    $ rel_bump("Zira", trust=-1)
    $ npc_remember("Aeron", "signed_the_cook", tone="eighteen_second_read")
    $ npc_remember("Nyra", "framing_line_dropped", tone="doctrinal_naming")
    $ npc_remember("Noelle", "seven_names_on_private_board", tone="pre_doctrine_threshold")
    $ npc_remember("Zira", "closed_the_channel_without_answering", tone="pre_break")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s09_sector_12_sweep_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - First light of the day after a4_s02 through a4_s07. The morning of the
#     day after Marcus's disappointment interlude (a4_s08). 0537 pre-briefing
#     to 0622:11 close-out.
# cann.what_happened:
#   - Pre-strike briefing at the ops table. Aeron standing at the head.
#     Nyra tactical right, Noelle analytical left. Zira on comm only, cordon
#     staging. Her absence from the table is the only negotiation she has left.
#   - Target list presented for ratification. Three tertiary entries
#     (collaborators/civilians): Jaren Okho (logistics clerk), Mira Telven
#     (sanitation supervisor), Orin Dask (cook, 57). Noelle classified them
#     tertiary under her Tuesday schema rewrite. Threshold was two intercepts
#     (Dask meets exactly).
#   - Aeron reads the list for eighteen seconds. Could ask why the cook is
#     tertiary not secondary. Does not ask. Signs. One stroke. OB-register.
#     Noelle was watching for the hesitation. None. She logs it.
#   - Operation: breach 0600:04. Flawless. 22 minutes. 17 Echelon dead,
#     3 civilian dead, 0 Phoenix casualties. No field cutaways -- the
#     violence is read on the projection as icons transitioning to grey,
#     and heard on the comm channel at low volume.
#   - The cook dies at 0604:22 in the logistics kitchen during breakfast prep
#     (he was 17 seconds early on his own schedule).
#   - Post-strike Aeron speaks one word: "Clean." Nyra repeats it quietly:
#     "Clean." Noelle does not repeat the word. Noelle adds three names to
#     a private TERTIARY-CONFIRMED whiteboard she has been keeping since the
#     Tuesday schema rewrite. Previous four names already on it. Seven total.
#     Seven was her private threshold. She realizes she will write a doctrine
#     tomorrow. (Plants a4_s10.)
#   - Nyra's framing line: "The word 'civilian' was a useful framing when
#     we needed to appear restrained. We no longer need to appear restrained."
#     Aeron does not agree, does not disagree. He returns to the table for
#     the next operation. The two absences are the ratification.
#   - Zira closes the comm channel without answering the framing line. The
#     non-response is the response. She is pre-breaking.
# cann.aeron_state:
#   - Eighteen-second target list read with full interior awareness that
#     he could ask about the cook and is choosing not to.
#   - The signature is redundant -- he authorized the schema on Tuesday 1147
#     and the objection is mechanically impossible at the 0540 ratification.
#     He notices this. He does not flag the noticing.
#   - One spoken word ("Clean.") post-strike. The rest is the operational
#     continuation. "I am becoming administratively fluent in the gratitude."
# cann.noelle_state:
#   - Private TERTIARY-CONFIRMED board. Seven names was a privately set
#     threshold. Meeting the threshold tips her into doctrine-writing mode
#     for a4_s10. "The part of me that is keeping the names is the part of
#     me that is going to write the doctrine tomorrow." Explicit plant.
#   - She notices the absence of fear. The absence of fear is new.
# cann.nyra_state:
#   - Tactical on the operation, doctrinal on the framing line.
#   - "The word 'civilian' was a useful framing when we needed to appear
#     restrained. We no longer need to appear restrained." The line is
#     delivered at operational cadence, not rhetorical.
#   - Echoes Aeron's "Clean" quietly. The echo is doctrinal, not agreeing.
# cann.zira_state:
#   - Voice on the comm channel only. Cordon discipline holds. Her absence
#     from the table is the only negotiation she has left. She closes the
#     channel without answering Nyra's framing line. Pre-break.
# cann.thematic_flags:
#   - THE SIGNATURE IS THE SCENE. Not the shooting. The scene is about the
#     eighteen seconds Aeron reads the target list and does not ask. The
#     violence is icons and audio, never framed directly.
#   - PRE-AUTHORIZATION. The Tuesday schema rewrite pre-authorized the
#     civilian inclusion. The morning ratification is a redundancy. The
#     objection is mechanically impossible. Aeron knows it. The knowing is
#     the administrative fluency.
#   - THE COOK. Fifty-seven years old. Seventeen seconds early on his own
#     schedule. The specific grief is compressed into an administrative beat.
#   - NOELLE'S PRIVATE BOARD. The seven names. The threshold is met. The
#     doctrine is coming tomorrow. The board is the first visible hairline
#     crack in Noelle's analyst-as-observer stance.
#   - NYRA'S FRAMING LINE. "The word 'civilian' was a useful framing..."
#     The line is the doctrinal naming of the shift. Aeron's non-response
#     is the ratification.
#   - ZIRA'S CLOSING THE CHANNEL. The non-answer as the answer. She is
#     pre-breaking. Plants a subsequent Zira break scene.
#   - "THE BASE FUNCTIONS. THAT IS NOT THE SAME AS LIVING." Callback.
#     Aeron has stopped noticing. The not-noticing is the metric.
# cann.callbacks:
#   - a3_s08_perfect_execution_ob: "Clean is mercy." The "Clean" / "Clean"
#     echo in this scene is the doctrinal extension to civilians.
#   - a3_s16_data_and_doubt_ob: Noelle's Tuesday schema rewrite. Tertiary
#     classification. The variance log she keeps for Aeron.
#   - a4_s01_the_cold_room_ob: the one-stroke signature geometry recurs.
#   - a4_s02_the_new_shape_ob: Nyra's doctrinal naming register recurs.
#     The framing line is the shape of that register applied to the word
#     civilian.
#   - a4_s03_marcus_adapts_ob: the preemptive strike Aeron authorized there
#     is this operation.
#   - a4_s08_echelon_interlude_4_ob: Marcus told Rhea Aeron would not object
#     to the civilian inclusion. Confirmed.
# cann.block_status:
#   - ANCHOR. Always plays on OB path. No branching. No player choice.
#     The scene is a narrative non-choice -- Aeron's active refusal to
#     intervene in the system he has already built.
# cann.requires_followup:
#   - a4_s10_noelle_doctrine_ob: Noelle drafts the doctrine she has realized
#     she is going to write. Aeron signs it blank.
#   - Zira break scene (later Act 4): the channel-closing is the fuse.
#   - Marcus intercept read: Rhea's forward post is denied as Marcus predicted
#     in a4_s08.
