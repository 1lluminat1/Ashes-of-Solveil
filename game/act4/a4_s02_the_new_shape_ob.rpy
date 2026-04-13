# =======================================================
# ACT 4 - Scene 02: The New Shape (Obedience Path)
# File: a4_s02_the_new_shape_ob.rpy
# Path: OB
# Type: REGIME STRUCTURE / COUNCIL RATIFICATION
# Character Focus: Nyra (doctrine), Aeron (ratifier),
#                  Lyra, Zira, Noelle, Tessa (witness / collapse)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s02_the_new_shape_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy

label a4_s02_the_new_shape_ob:
    $ show_timeline("25th of Forge, 390 A.C.", "10:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked tripod. War room wide establishing -- slightly colder than
    #         a3_s07. Same room, emptier. The displays behind Nyra now show the full
    #         seven-day plan from s01 populated and running. Coverage: singles on each
    #         LI as Nyra walks them through their new positions in the structure. The
    #         camera does not linger. Brevity is the respect. One wider shot when
    #         Aeron signs -- the wider frame is the weight. No close-ups during the
    #         signature itself. The camera holds at middle distance. Institutional.
    # LIGHTING: Tactical blue at 100%. No warmth. The overhead strips are running at
    #           the setting Nyra adjusted them to in Act 3 and they have not been
    #           adjusted back. Hard shadows. Clean lines.
    # SFX: Loop -- war room hum (cold), display refresh every 11 seconds, distant boot
    #      formations in the staging yard (Nyra's soldiers drilling on schedule).
    #      One-shots -- datapad placement, chair shifts (Zira's hands going still is
    #      an absence of a sound, not a sound), Lyra's eyes closing (none), Noelle's
    #      stylus (steady, recording), the stylus Aeron uses to sign (one stroke).
    # FX/COMP: The war room displays run Nyra's structural diagram -- the new command
    #          architecture rendered as a hierarchical tree. The shape of the rebellion
    #          reduced to a flowchart. Phoenix at top. Nyra and Aeron as co-command.
    #          Everything else as function nodes beneath them.
    # BLOCKING: Nyra at the display wall (Selene's old briefing position, permanently
    #           hers now, the room no longer notices). Aeron at the head of the table.
    #           Lyra to Aeron's right. Zira opposite, arms not yet crossed. Noelle
    #           with her tablet. Tessa at the far end, closest to the door. Tessa
    #           does not speak this scene.
    # CANON: The council ratifies the structure Aeron and Nyra already agreed to in
    #        s01 without words. The ratification is the naming. Nyra gives the room
    #        the word for what they have been doing since Selene died.
    # FACE: Nyra -- calm, doctrinal, unhurried. Lyra -- eyes closed (not prayer, the
    #        opposite). Zira -- hands go still. Noelle -- taking notes. Tessa --
    #        present, silent, reading the room. Aeron -- signs.

    # ========= VOICE BASELINE =========
    # OB Aeron: Fewer words than usual. The ratification is the line.
    # Nyra: Doctrinal. Naming, not explaining.
    # Zira: Hostile-silent. Her hostility has compressed into stillness.
    # Lyra: Minimal. The eyes closing is her line.
    # Noelle: Functional. Data-forward. Corruption by competence.
    # Tessa: SILENT. Does not speak the scene. Presence only.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - 0900]
    # 0900. The morning after s01. Nyra has spent the previous hours preparing
    # the structural diagram. The council has been summoned.

    #scene bg_war_room_ob_0900 with dissolve
    #play ambient "sfx/ambient/war_room_cold.ogg" fadein 2.0

    # ========== PHASE 1 -- THE ASSEMBLY ==========

    "0900."

    "The war room is cold. The overhead strips are at 100%%. The tactical displays behind the briefing position cycle through the sector consolidation plan Aeron approved three hours ago with a single stylus mark."

    "The plan is now running. Sector 4 day-one movement orders have already been relayed to the strike teams. The day-two feint is being staged in the equipment bay. The day-five Sector 9 entry is queued, waiting."

    "The council assembles without being summoned twice."

    #show zira war_room_seated_tense with dissolve
    #show noelle war_room_seated with dissolve
    #show lyra war_room_seated with dissolve
    #show tessa war_room_far_end with dissolve

    "Zira enters first. Takes the chair opposite Aeron's. Her hands are on the table, not yet crossed."

    "Noelle enters second. Tablet open before she sits. Stylus already in hand."

    "Lyra enters third. She takes the chair to Aeron's right. She does not look at him. She looks at the displays."

    "Tessa enters last. She takes the chair at the far end, closest to the door. She places her hands in her lap. She does not speak. She will not speak."

    #show aeron war_room_head with dissolve

    "Aeron is already at the head of the table."

    "Nyra stands at the display wall."

    "She is not in the briefer's posture. She is in the doctrine-deliverer's posture -- weight distributed evenly, hands clasped behind her, chin level, the expression of a woman who is about to name a room she has already built."

    # ========== PHASE 2 -- THE STRUCTURE ==========

    ny "Thank you for coming."

    "Her voice is the same voice from s07. The same voice from s12. The same voice from the safe house when she dismissed Liora as weakness."

    "The voice has not modulated at any point in the six weeks Nyra has been in Phoenix base. That stability is the seduction."

    ny "I want to present the restructured command architecture. The operational events of the last two weeks -- the Sector 4 corridor, the Ghostline node consolidation, the Outlander courier interface -- have produced a functional shape that has not been formalized."

    ny "I am here to formalize it."

    "She turns. Taps the display behind her."

    "The hierarchical tree populates."

    "Phoenix at the top node. Beneath it: a two-headed command structure. AERON RYLAN / NYRA KAELIN. Equal weight. Equal width. The line between them is a solid bar, not a dotted one."

    "Beneath the two-headed node: function branches. Operations. Intelligence. Logistics. Communications. Medical. Each branch is labeled with the LI responsible for it."

    "ZIRA VOSS -- Intelligence / Ghostline."
    "NOELLE HART -- Analysis / Planning."
    "LYRA VELDREN -- Morale / Internal Welfare."
    "TESSA KAINE -- Medical / Personnel Assessment."

    "Beneath each function branch: the soldiers who report to it. Nyra's seventeen integrated into every branch except Intelligence, where Zira's Ghostline operators remain structurally independent. The exception is the single concession the diagram makes to the old shape of Phoenix."

    "Everything else is new."

    # --- FIRST REACTIONS (SILENT) ---

    # CAMERA: slow coverage rotation across the four LI singles. No dialogue yet.
    #         Each face a separate shot.

    "Zira's hands, which were on the table, go still."

    "Not clench. Not tighten. Still. The subtle motion of a woman whose hands have been doing a low-frequency habitual movement -- a fingertip against the table edge -- stopping that motion. The absence of the motion is louder than the motion would have been."

    zthought "Co-command."

    zthought "Not 'commander with advisor.' Not 'commander with specialist.' Co-command."

    zthought "The bar between their names is solid."

    zthought "When did that happen."

    zthought "I know when that happened. It happened last night in a strategic room with the bolt thrown and neither of them said it out loud and now we are naming it at nine in the morning like we're ratifying a treaty we were not at the signing for."

    # --- LYRA ---

    "Lyra, who has been looking at the display, closes her eyes."

    "It is not prayer."

    "Prayer has a posture Lyra knows -- the hands coming together, the head lowering, the small exhale. This is not that."

    "This is the opposite. This is a woman who has been looking at a thing and has decided to stop looking at it, and the closing of her eyes is the only protest she can afford to make in a room where protest is no longer part of the structure."

    lthought "I used to pray for him."

    lthought "I used to pray for the pause. The hesitation. The thing his mother said would survive in him."

    lthought "I closed my eyes just now and I did not pray. I closed them because the thing on the wall is the shape of what the prayer was meant to prevent, and I cannot watch the shape and also believe the prayer is possible."

    lthought "I am not praying right now. I do not know when I will pray again."

    lthought "I do not know if I will tell him that."

    # --- NOELLE ---

    "Noelle takes notes."

    "Her stylus moves across the tablet in the small efficient strokes of a secretary recording a meeting. She is not transcribing Nyra's words. She is cataloging the structural diagram. The node relationships. The reporting lines. The data flow paths."

    "She is building an index of the new architecture so the planning team can reference it cleanly."

    "She is the secretary of her own corruption."

    nthought "The architecture is sound."

    nthought "I will not say that out loud because Zira's hands went still and I can see Lyra's face and Tessa has not made eye contact with anyone since she sat down."

    nthought "But the architecture is sound. Reporting lines are clean. Function branches do not overlap. The Ghostline independence is the one inefficiency and Nyra has preserved it. That is not an oversight. That is a concession to retain Zira."

    nthought "She is managing us."

    nthought "I am recording the management."

    nthought "When the history of this period is written -- if a history is written, which is a question the architecture does not ask -- I will be the one who wrote the meeting minutes."

    nthought "That is a position. It is not the position I thought I was taking when I joined Phoenix."

    nthought "I notice I am still taking notes."

    # --- TESSA ---

    "Tessa has not moved."

    "She sits at the far end of the table. Her hands are in her lap. Her eyes are on the display -- not the hierarchy, the background. The blue-grey wall behind the flowchart. The wall of the war room. The concrete."

    "She is either adapting or preparing to break. The scene does not yet know which."

    tthought "..."

    # She does not even permit herself an internal monologue this scene.
    # The silence goes that deep.

    # ========== PHASE 3 -- NYRA CONTINUES ==========

    "Nyra does not wait for reactions. The diagram is the argument."

    ny "The operational benefits are measurable. Reporting latency from function branch to command node: under four minutes. Decision-to-execution latency for strike operations: under twelve minutes. Logistical waste ratio: seven percent, down from twenty-two."

    ny "The cultural benefits are harder to quantify."

    ny "I will quantify them anyway."

    ny "The previous structure was grief-permissive. That was appropriate during mourning. It is not appropriate during a campaign against an opponent who is rebuilding his response tempo. The new structure permits grief only at the edges -- personal, private, on personal time. The structure itself does not grieve."

    ny "Structures that do not grieve do not slow."

    z "..."

    "Zira does not speak. Her hands are still still."

    ny "Commander Voss. The Ghostline independence is preserved. Your operators do not report into the Phoenix branch chain. They report directly to you and through you to co-command. This is the arrangement from the Terms of Order briefing. It has been ratified rather than revised."

    "She says Commander Voss. Not Zira. The naming is part of the structure."

    z "..."

    "Still no words."

    ny "I interpret your silence as non-objection."

    "Zira's eyes move from the display to Aeron. Not to Nyra. To Aeron."

    "Aeron is looking at the display, not at Zira."

    "Zira's eyes return to the display."

    zthought "Non-objection."

    zthought "That is the word she just used for my silence. Non-objection. In a constitutional framework that is the word you use when the senator who hates the bill does not have the votes to block it, so the bill passes on the absence of the blocking motion."

    zthought "She just processed me."

    zthought "I did not stop her."

    # ========== PHASE 4 -- THE NAMING ==========

    ny "There is one element of this structure I want to address directly."

    ny "The diagram shows co-command at the apex. The diagram is not inventing that. The diagram is recording it."

    ny "Since Selene Marchetti died, the operational decision-making of Phoenix base has been made by Commander Rylan with structural input from me. The input has grown from advisory to co-determinative. That growth has been gradual. It has not been announced."

    ny "I am announcing it now because the operations of the next two weeks will require clarity. The strike teams cannot operate on ambiguous command hierarchy. The Ghostline relay shifts cannot proceed on unclear authority. The day-five Sector 9 entry requires a unified operational voice."

    "She pauses."

    "The pause is not dramatic. It is the pause of a woman letting a sentence settle before she delivers the next sentence. The settling is the scene's entire pivot."

    ny "This is not a new room."

    "The line lands in the silence."

    ny "This is the room we have been in since she died."

    ny "I am only naming it."

    # ========== PHASE 5 -- THE NAMING LANDS ==========

    "The 'she' is not specified."

    "It does not need to be."

    "Selene Marchetti. Killed by Aeron Rylan in Act 2. The fact of that killing has never been stated in this room at this volume. The fact has been an undercurrent, a climate, a shared unspoken. Nyra has just spoken it at room volume in a sentence that did not ask permission."

    "Nobody corrects her."

    "Zira does not correct her."

    "Lyra does not correct her. Lyra's eyes are still closed."

    "Noelle does not correct her. Noelle's stylus has paused on the tablet. One stroke, unfinished. The stylus is resting on the surface of the tablet as if the tablet has become too heavy to write on."

    "Tessa does not correct her. Tessa is still looking at the wall behind the display."

    "Aeron stares at the table for one beat."

    "The beat is approximately two seconds."

    "In those two seconds:"

    athought "She said her name."

    athought "Nyra said 'she died.' She did not say murdered. She did not say executed. She did not say killed by Marcus's son in the planning corridor at 0421 on the morning of the Glass Surge."

    athought "She said died."

    athought "Died is the word you use for a fact that is complete."

    athought "I notice I am grateful for the word."

    athought "That is the tell."

    # --- AERON DOES NOT SPEAK ---

    "He does not speak."

    "The scene's structure does not permit him to speak here. Speech would be a correction. Speech would be a hesitation. Speech would be the pause his mother said might survive."

    "He does not speak."

    "He signs."

    # ========== PHASE 6 -- THE SIGNATURE ==========

    # WIDER SHOT -- 40mm pulls back. The whole table in frame. The weight of the
    # room. Aeron signing is a small motion at the center of a large image.

    "Nyra slides a datapad across the table. Not the datapad from s01 -- a new one. This one has the structural diagram on it and a signature field at the bottom."

    "The signature field is labeled RATIFICATION."

    "Aeron takes the stylus."

    "He does not read the document again. He read it once in the display. He knows what he is signing."

    "He signs."

    #play sound "sfx/stylus_signature_single.ogg"

    "The signature is one stroke -- not his full name. The initial. A, then a slash, then R. The OB-register signature he has been using for operational documents since Nyra arrived. Three marks. Under a second."

    "He slides the datapad back."

    ny "Thank you, Commander."

    "Nyra takes the datapad. Taps it once. The ratification propagates. The structural diagram is now the canonical command architecture of Phoenix base. The internal systems update in real time. The reporting lines resolve. The function branches lock."

    "The whole base, six seconds from now, will be running under the new structure. Most of the base will not notice because the base has been running under this structure for weeks and only the naming was missing."

    # ========== PHASE 7 -- CLOSURE WITHOUT CLOSURE ==========

    ny "Operational assignments for the week are in your individual briefing packets. Commander Rylan and I will meet in the strategic room at 1400 to finalize the day-five Sector 9 approach."

    ny "Thank you."

    "She gathers her datapad. Steps away from the display wall. The hierarchical tree remains on the wall behind her -- it will remain on the wall for the rest of the week as the operational reference for every planning meeting."

    "The shape is the wall now."

    "Nyra walks to the door. Her pace is the same pace she used when she walked out of a3_s07. The same pace she used last night leaving the strategic room. The base has calibrated to her pace."

    "The door opens for her."

    "She steps through."

    "The door closes."

    # ========== PHASE 8 -- THE ROOM AFTER ==========

    "The war room does not empty immediately."

    "The four LI and Aeron remain at the table for a moment longer than they should. The moment is the room collectively registering what has just been named."

    # --- ZIRA MOVES FIRST ---

    "Zira stands."

    "Her hands, which have been still for the entire scene, move once -- she picks up her datapad. The motion is deliberate. She is showing her hands to the room. Look, the motion says. My hands still work. I just chose not to use them."

    z "Aeron."

    "She says his name. Not Commander. Not Rylan. Aeron."

    "He looks up."

    z "I'm going to my station."

    "She does not say I object. She does not say we should talk. She does not say what the hell was that."

    "She says I'm going to my station."

    zthought "I am going to my station because I have not decided what I am going to do and I need to be at my station to decide it."

    zthought "I am not going to decide it in this room in front of him."

    "She leaves."

    # --- LYRA ---

    "Lyra opens her eyes."

    "She looks at Aeron for the first time this scene."

    "The look is not the look from a3_s07 when she was breaking quietly. That look was a fracture. This look is after the fracture has completed -- the calm of a thing that has already broken and is now assessing the pieces."

    l "Was this in the strategic room last night."

    "Four words. Not accusation. A data question."

    a "Yes."

    "One word. He does not elaborate."

    l "Then the meeting this morning was a ratification, not a decision."

    a "Yes."

    "Lyra nods. Slowly. She does not say good or bad or anything in between. She stands."

    l "I will be in the chapel."

    a "..."

    l "I am not going to pray."

    "The clarification is not for him. The clarification is for herself. She is telling herself out loud, in front of him, what she has just confirmed internally -- that the chapel is now a room she goes to for silence, not for prayer, because prayer is no longer a tool that works on what is happening."

    "She leaves."

    # --- NOELLE ---

    "Noelle closes her tablet."

    "She stands. She does not address Aeron directly."

    n "I'll circulate the updated reporting lines to the function branches by 1100. The analytical load for the day-five Sector 9 approach will be on my desk by 1300 at the latest."

    "She leaves."

    nthought "I said 'the analytical load' like that was a normal phrase. It is a normal phrase. I have said it a hundred times in this base. It sounded different just now because I was saying it in a room that had just changed shape under the word died."

    # --- TESSA ---

    "Tessa has not moved."

    "The other three have left. Aeron is still at the head of the table. Nyra is gone. The hierarchical tree still glows on the wall."

    "Tessa sits in the chair at the far end of the table."

    "She looks at Aeron."

    "She does not speak."

    "The scene's voice baseline said Tessa does not speak this scene. The scene's voice baseline holds."

    tthought "..."

    "She looks at him for four seconds."

    "Then she stands."

    "She walks to the door."

    "At the threshold, she pauses. She turns her head back toward him -- not all the way, just enough that he can see her face in profile. Her face is unreadable. Her face has been unreadable for the entire scene. The fact that she chose to turn her head at all is the only line she has given him."

    "She turns back. She steps through the door."

    "The door closes."

    # ========== PHASE 9 -- AERON ALONE ==========

    "Aeron is alone in the war room."

    "The hierarchical tree on the wall. The empty chairs. Nyra's datapad is gone. His datapad is open to the operational briefing for day one of the new plan."

    "The briefing is clean. The deployment orders are already routed. The logistical chain is already moving."

    "He does not sit back. He does not lean forward. He does not put his hands on the table."

    "He looks at the wall where the hierarchical tree is."

    "He looks at the node labeled AERON RYLAN / NYRA KAELIN."

    "He looks at the solid bar between the two names."

    athought "Co-command."

    athought "The word was already true. The diagram is late to the truth."

    athought "Liora said I was becoming administratively fluent in what I did. She did not use those words. She used the word charts. She said she could see Marcus's charts in the way I sit."

    athought "The chart is on the wall now."

    athought "She can see it from wherever she is. The Outlands are not far enough for her not to see it. The courier network will carry the shape of this room to her within the week."

    athought "I wonder if she will recognize the exact line where I stopped pausing."

    athought "I do not wonder what she will do with the recognition."

    athought "That is not a thing I am wondering about this morning. That is not a thing I am allowing myself to wonder about this morning."

    athought "The room has been named. The structure has been ratified. The signature is one stroke and three marks and it is done."

    athought "This is not a new room. This is the room we have been in since she died."

    athought "I am only naming it."

    athought "Nyra said that. I am repeating it to myself because it is the correct sentence."

    $ tp_seed("a4.ob.room_named")

    # --- SIGN OFF ---

    "The display cycles through the day-one deployment orders. The blue light bathes the empty table. Aeron does not move."

    "The base functions."

    "That is not the same as living."

    "The distinction is a thing he used to notice."

    "He does not notice it this morning."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.phoenix.structure", "nyra_doctrine_ratified")
    $ canon_set("ob.phoenix.cocommand_formal", True)
    $ metric("ob.aeron.formalized_violence", set_to=1)
    $ flag("a4_structure_ratified", True)
    $ flag("lyra_stopped_praying_ob", True)
    $ flag("zira_nonobjection_ob", True)
    $ flag("tessa_silent_ob_s02", True)
    $ rel_bump("Nyra", trust=1)
    $ npc_remember("Nyra", "named_the_room", tone="doctrinal_certainty")
    $ npc_remember("Zira", "hands_went_still", tone="processed_silent")
    $ npc_remember("Lyra", "eyes_closed_not_prayer", tone="post_fracture_calm")
    $ npc_remember("Noelle", "secretary_of_own_corruption", tone="functional_corruption")
    $ npc_remember("Tessa", "silent_the_whole_scene", tone="adapting_or_breaking")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s02_the_new_shape_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - 0900 on the morning after a3_s24_liora_ob. Three hours after a4_s01.
#   - Council meeting. Nyra presents the restructured command architecture
#     that was already ratified silently in a4_s01.
# cann.what_happened:
#   - Nyra presents hierarchical command tree: co-command at apex
#     (AERON RYLAN / NYRA KAELIN, solid bar between the names).
#   - Function branches: Intelligence (Zira, Ghostline preserved as concession),
#     Analysis/Planning (Noelle), Morale/Internal Welfare (Lyra), Medical/
#     Personnel Assessment (Tessa). Nyra's 17 integrated into all except Intel.
#   - Reactions: Zira's hands go still (silent "non-objection"). Lyra closes
#     her eyes -- not prayer, the opposite. Noelle takes notes (secretary of
#     her own corruption). Tessa does not speak the entire scene.
#   - Nyra names the room: "This is not a new room. This is the room we have
#     been in since she died. I am only naming it." The 'she' is Selene.
#     Nobody corrects her. Aeron stares at the table for one beat. Signs.
#   - Post-signature: Zira leaves ("I'm going to my station"). Lyra leaves
#     for the chapel ("I am not going to pray"). Noelle circulates the
#     updated reporting lines. Tessa pauses at the door, turns her head in
#     profile, leaves without speaking.
# cann.aeron_state:
#   - One beat of interior before signing ("I notice I am grateful for the
#     word died. That is the tell.").
#   - The one-stroke OB signature (A/R). The ratification is the whole voice.
#   - Post-scene: "This is not a new room... I am only naming it" repeated
#     internally as "the correct sentence."
#   - "The base functions. That is not the same as living. The distinction
#     is a thing he used to notice. He does not notice it this morning."
# cann.thematic_flags:
#   - RATIFICATION, NOT DECISION. The scene formalizes what s01 already
#     decided in silence. Lyra names this explicitly ("Was this in the
#     strategic room last night. ... Then the meeting this morning was a
#     ratification, not a decision.") -- the only dialogue Lyra has this scene.
#   - THE NAMING. Selene's murder is converted to "died." The conversion is
#     the OB path's entire moral project, compressed into one verb.
#   - LYRA STOPS PRAYING. The chapel becomes a room she goes to for silence,
#     not for prayer. The fracture from s07 has completed.
#   - ZIRA'S NON-OBJECTION. Her hostility has compressed into stillness.
#     Nyra processes her silence as ratification. Zira lets it.
#   - NOELLE AS SECRETARY OF HER OWN CORRUPTION. The phrase lives in her
#     interiority. She is cataloging the architecture and will later write
#     the meeting minutes of the period.
#   - TESSA SILENT ENTIRE SCENE. Either adapting or preparing to break. The
#     scene deliberately does not resolve which. The profile-turn at the
#     door is her only line.
#   - "THE BASE FUNCTIONS. THAT IS NOT THE SAME AS LIVING." Callback to
#     a3_s23 / a3_s24. Aeron used to notice this distinction. He no longer
#     notices. The not-noticing is the metric.
# cann.character_moments:
#   - Nyra: doctrinal register. Names the room. Does not ask permission. The
#     scene's moral weight hangs on her calm.
#   - Zira: hands going still as the entire performance. Six words of
#     dialogue ("Aeron." "I'm going to my station."). Her absence of motion
#     is the scene's loudest instrument.
#   - Lyra: eyes closed interior beat. Four words of dialogue.
#     "I will be in the chapel." / "I am not going to pray." The chapel is
#     no longer a prayer room.
#   - Noelle: functional corruption. Takes notes. Stylus pauses at "died"
#     and then resumes. The stylus is still recording.
#   - Tessa: zero words. Silent the entire scene. The profile-turn at the
#     door is the only physical statement. Adapting or breaking -- unresolved.
#   - Aeron: one stylus stroke. Two-second beat before signing. "I notice
#     I am grateful for the word. That is the tell."
# cann.callbacks:
#   - a3_s07_terms_of_order_ob: the original restructuring. This scene is
#     the formal ratification of what s07 began.
#   - a3_s08_perfect_execution_ob: "Clean is mercy." The structure in this
#     scene is the ratification of that doctrine at the command level.
#   - a3_s24_liora_ob: "I am my father's son." Confirmed visually by the
#     chart on the war room wall.
#   - a4_s01_the_cold_room_ob: the silent ratification that this scene
#     makes public.
# cann.block_status:
#   - ANCHOR. Always plays on OB path. No branching. No player choice.
#     The scene IS the regime's establishment.
# cann.requires_followup:
#   - a4_s03_marcus_adapts_ob: the first operation run under the new structure.
#   - Lyra silence arc: she is no longer praying. Where does she go next.
#   - Zira silence arc: her "I'm going to my station" is a pivot. What does
#     she do at the station.
#   - Tessa break point: the silence has a half-life. Scene 04 or later.
