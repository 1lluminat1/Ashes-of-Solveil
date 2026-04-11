# =======================================================
# ACT 4 - Scene 03: Marcus Adapts (Obedience Path)
# File: a4_s03_marcus_adapts_ob.rpy
# Path: OB
# Type: MARCUS PLOT HINGE / ACCELERATION AUTHORIZATION
# Character Focus: Noelle (data), Nyra (doctrine),
#                  Aeron (authorizer), Marcus (Echelon intercept, brief)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s03_marcus_adapts_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy
# m (Marcus) is used only for a brief Echelon intercept cut-in.

label a4_s03_marcus_adapts_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm locked for the operations room. Noelle at the analysis station,
    #         the six-day collision clock rendered on the display wall. Singles on
    #         Aeron, on Nyra, on Noelle. The scene is three people and a clock.
    #         Handheld (2% drift) only for the brief Marcus intercept cut-in --
    #         Echelon war room, different lighting grammar, different space. The
    #         handheld is there to mark that we are outside Phoenix for eleven seconds.
    #         Return to 40mm lock. The writing of names on the board is the scene's
    #         only close-up: Noelle's hand, the stylus, the list, the board going from
    #         empty to populated. No reaction shots during the writing.
    # LIGHTING: Phoenix operations room: tactical blue, 100%. Noelle's station is
    #           brightest -- her analytical display at full. Nyra's position at the
    #           display wall is also lit, same palette. Aeron at the head of the ops
    #           table, slightly dimmer, half in the pendant pool.
    #           Echelon cut-in: sodium amber. Warmer than any light source in Phoenix
    #           base. Marcus at a clean steel desk, no datapad, one printed report.
    # SFX: Loop -- operations room hum, the analytical display's low sub-audible
    #      refresh, the tick of Noelle's stylus against the tablet. One-shots --
    #      the collision clock updating (three soft beeps at six days, then again
    #      at five days nineteen hours), the Echelon intercept playback starting
    #      and stopping, the board marker writing the names, the authorization
    #      confirmation tone.
    # FX/COMP: The operations room display wall. Left panel: Marcus's response lag
    #          heat map over the last three weeks, showing the narrowing gap. Right
    #          panel: the six-day collision clock, ticking. Center panel: Commander
    #          Rhea Vestin's Echelon file -- photograph, service record, known
    #          operational signature. The photograph is a neutral surveillance still.
    # BLOCKING: Noelle at her station, standing to brief. Nyra at the display wall,
    #           same position as s02. Aeron at the head of the ops table. The three
    #           form a narrow triangle. No other personnel in the room. This is a
    #           closed briefing.
    # CANON: EMP-mirror scene. EMP s03 has Aeron asking what shared command looks
    #        like. OB s03 has Aeron accelerating the tempo. The authorization is the
    #        scene's hinge. Civilians become a word with no emotional register.
    # FACE: Noelle -- data-steady, with one micro-moment when Aeron does not react
    #        to the word civilians. Nyra -- approving, doctrinal. Aeron -- mask.
    #        Marcus (cut-in) -- reading the printed report. Calm. Not smiling.

    # ========= VOICE BASELINE =========
    # OB Aeron: Precise. Fewer words than Noelle. The authorization is the line.
    # Noelle: Briefing-register. Data first. One word where she becomes visible.
    # Nyra: Doctrinal. Two lines, one of them the hinge line.
    # Marcus: Eleven seconds. One intercept line. The line is the threat.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - OPERATIONS ROOM - 1130]
    # Two hours thirty minutes after a4_s02.

    #scene bg_ops_room_ob with dissolve
    #play ambient "sfx/ambient/ops_room_analytical.ogg" fadein 2.0

    # ========== PHASE 1 -- THE BRIEFING CONVENES ==========

    "1130."

    "The operations room is smaller than the war room. It is not built for councils. It is built for three or four people to stand around a central analytical display and make decisions that do not require ratification -- decisions that are already inside the authority envelope Nyra and Aeron ratified two hours ago."

    "Noelle is at her station. The analytical display wall is running her three-panel briefing layout. Left: response lag heat map. Right: collision clock. Center: a file with a photograph."

    "Nyra is at the display wall."

    "Aeron is at the head of the ops table."

    "There is no one else in the room."

    #show noelle ops_station_standing with dissolve
    #show nyra display_wall_position with dissolve
    #show aeron ops_table_head with dissolve

    n "I have the three-day adaptation read on Marcus. I want to brief it now because the window narrowed overnight."

    a "Proceed."

    "Two words. The OB operational register. Aeron is not warming into the briefing. He is already in the briefing the moment Noelle opens her mouth."

    # ========== PHASE 2 -- THE LAG PATTERN ==========

    n "Left panel. Response lag heat map. Three weeks of Echelon reaction data from Sector 4 onward."

    "The left panel pulses. Dark regions are slow responses -- Echelon taking eighteen, twenty-four, thirty hours to adapt their patrol grids after a Phoenix operation. Bright regions are fast responses -- twelve hours, nine hours."

    "Three weeks ago, the heat map was mostly dark."

    "Two weeks ago, bright patches emerged around Sector 4."

    "One week ago, the bright patches had consolidated into a pattern."

    "Now, the pattern is a lag of twelve to thirty-six hours. The variance is the signal."

    n "Marcus's adaptation cycle has compressed from an average of twenty-nine hours two weeks ago to an average of twenty-two hours yesterday. The compression is not linear. It is step-function -- he adapted in two jumps. The first jump was eleven days ago, the day after the Sector 4 depot strike. The second jump was yesterday."

    n "Yesterday's jump correlates with an Echelon personnel movement we flagged at 0400 this morning."

    "She taps the center panel."

    "The photograph populates."

    # ========== PHASE 3 -- RHEA VESTIN ==========

    "The photograph is a surveillance still. A woman in Echelon formal -- not combat gear, the dark grey service uniform with the surgical-ops trim. Mid-forties. Dark hair in a regulation knot. Expression unreadable, the way Echelon officers' expressions are unreadable in Echelon surveillance footage, which is to say the expression is the absence of expression."

    n "Commander Rhea Vestin. Echelon surgical ops division, seventeen years of service, deployed historically to high-density urban pacification. Her operational signature is characterized by three things: preemptive civilian relocation, compressed decision cycles, and zero tolerance for improvisation by her subordinates."

    n "She is inbound to Marcus's command. ETA six days."

    "The right panel pulses. The collision clock: 6 DAYS 00 HOURS 00 MINUTES."

    "The clock is ticking."

    # ========== PHASE 4 -- THE ANALYSIS ==========

    n "The analytical assessment is that Marcus's compression jumps are partial adaptations. He is absorbing lessons from each Phoenix operation and partially integrating them into his response doctrine. The integration is being slowed by the breadth of his command -- he is running three sector commands simultaneously and cannot dedicate full attention to counter-Phoenix operations."

    n "Rhea Vestin's arrival changes that. Echelon is not deploying her as a reinforcement. They are deploying her as a dedicated counter-Phoenix asset. Once she arrives, Marcus's adaptation cycle is projected to drop from twenty-two hours to approximately nine."

    n "A nine-hour response cycle renders most of our current operational tempo nonviable. The day-five Sector 9 entry specifically requires a minimum of fourteen hours of uncontested staging. With Vestin's arrival we lose that window."

    "She looks at Aeron."

    n "In six days, our planning horizon collapses."

    # --- AERON READS THE CLOCK ---

    athought "Six days."

    athought "The structure we ratified at 0900 has a six-day half-life."

    athought "Noelle is not telling me this because she wants me to grieve the half-life. She is telling me this because she wants me to ask the next question."

    athought "I know the next question. I know it the way Nyra knew which day the Sector 9 entry needed to move to."

    # ========== PHASE 5 -- THE ECHELON INTERCEPT (CUT-IN) ==========

    n "Before I take the strategic questions, there's an intercept fragment I need you to hear. Ghostline pulled it at 0747. It's eleven seconds. It confirms Vestin."

    "She taps the console."

    #scene bg_echelon_war_room_amber with dissolve
    #play ambient "sfx/ambient/echelon_war_room_warm.ogg" fadein 0.5

    # Brief cut-in to Echelon command. Handheld 2% drift. Amber light.

    "The scene is not Phoenix. The scene is a steel desk in an Echelon command room. The light is warmer -- sodium amber from overhead strips calibrated for Echelon's visual-comfort standard. The room is quiet. A single printed report on the desk. A single officer reading it."

    #show marcus echelon_desk_reading with dissolve

    "Marcus Rylan."

    "He is not smiling. He is not in a posture that suggests he is pleased. He is in the posture of a man reading an operational report who has already decided what he thinks of it and is now confirming the decision against the text."

    "He reads for three seconds."

    "Then he speaks. The line is short. The line is being picked up by the Ghostline intercept because Phoenix has a relay seeded in the Echelon operational net from two weeks ago."

    m "Commander Vestin. Expedite. Three days if you can."

    "Eleven seconds of audio. Then the line cuts."

    #stop ambient fadeout 0.3
    #scene bg_ops_room_ob with dissolve
    #play ambient "sfx/ambient/ops_room_analytical.ogg" fadein 0.5

    # ========== PHASE 6 -- THE CLOCK UPDATES ==========

    "The ops room. Noelle at the console. Nyra at the display wall. Aeron at the head of the ops table."

    "The right panel pulses."

    "The collision clock updates: 5 DAYS 19 HOURS 00 MINUTES."

    "The clock ticked the moment the intercept stopped playing. Noelle's analytical engine had already factored Marcus's three-days-if-you-can request into the projected ETA window."

    n "She will not arrive in three days. The logistical pipeline for an officer of her rank and a mission of this nature has a minimum transit time of five days seventeen hours. The five-day nineteen-hour projection is the tight edge of that envelope."

    n "Marcus knows this. He asked for three because asking for three pulls the arrival toward the tight edge."

    n "He is training his own logistics to compress the way he has been training his response cycles."

    # --- NOELLE'S DATA-FORWARD VOICE ---

    nthought "I can see both sides of this analysis simultaneously. Phoenix and Echelon as mirror planning environments. Marcus is running the same analytical posture I am. He is shortening cycles. He is expediting."

    nthought "We are going to shorten cycles. We are going to expedite."

    nthought "The symmetry is the thing I am not saying out loud. Nyra does not need me to say it. Aeron does not need me to say it. The symmetry is in the briefing materials already. The collision clock is the symmetry."

    # ========== PHASE 7 -- THE STRATEGIC QUESTIONS ==========

    n "The strategic question, as I see it, is how Phoenix responds to a six-day collision."

    n "Option one: we slow our operational tempo to match Echelon's projected nine-hour adaptation cycle. This preserves our civilian exposure ratio at current levels. It effectively cedes initiative to Marcus and Vestin."

    n "Option two: we accelerate our current tempo to complete priority operations before Vestin arrives. This preserves initiative but..."

    "She pauses. The pause is not hesitation. The pause is the moment she has been building toward."

    n "...accelerating the day-five Sector 9 entry into a day-three entry will cost civilians. The staging compression eliminates the pre-strike evacuation window we had built into the original plan."

    n "Estimated civilian cost for an accelerated Sector 9 entry is between nine and nineteen."

    "She looks at Aeron."

    # --- THE CIVILIAN WORD ---

    # CAMERA HOLDS ON AERON. No cut. No reaction shot on Nyra, on Noelle. The
    # scene waits to see whether the word civilians will produce a movement on
    # Aeron's face.

    "It does not."

    "Aeron does not react to the word civilians."

    "Not a flinch. Not a tightening at the jaw. Not a glance at Noelle to confirm the number. The word lands on him exactly the way the word casualties would have landed, and the word casualties would not have landed either, because this is the man who signed a hierarchical diagram two hours ago and then repeated the sentence 'I am only naming it' to himself in an empty war room."

    "The not-reaction is the scene's worst shot."

    # --- NOELLE'S MICRO-MOMENT ---

    nthought "He did not react."

    nthought "I have briefed him on civilian exposure numbers seventeen times in six weeks. The first time, he corrected me to 'noncombatant casualty projection.' The fourth time, he asked for the age distribution. The ninth time, he asked for a confidence interval."

    nthought "The seventeenth time, which is this time, he did not react at all."

    nthought "I am cataloging this. I am going to record 'no observable reaction to civilian exposure language' in the behavioral baseline file I keep on him and do not share with anyone."

    nthought "The file is six entries old. This is entry seven."

    nthought "Entry seven is the first entry I have made that I will not be able to read back to myself later."

    # ========== PHASE 8 -- NYRA'S LINE ==========

    "Nyra has been silent through the entire briefing."

    "She steps away from the display wall. Two paces toward the ops table. Close enough that her voice does not require projection."

    ny "He will adapt faster than you expected because he trained you."

    "The line is not directed at Noelle. It is directed at Aeron."

    "Aeron looks at Nyra for the first time in the scene. Not at the display, not at the table, not at Noelle. At Nyra."

    ny "Train him back."

    # --- THE LINE LANDS ---

    athought "Train him back."

    athought "Three words. She has compressed six days of collision into three words and an instruction."

    athought "The instruction is correct."

    athought "Marcus trained me in the Glass. He trained me to recognize compression, to anticipate expedition, to read the tight edge of logistical envelopes. I learned it from him."

    athought "He did not learn it from me. He taught it. He is operating on his own doctrine. My doctrine is his doctrine with six weeks of field modifications."

    athought "Nyra is saying: apply the modifications back at him. Show him what his own doctrine looks like when it is used against him faster than he can adapt to his own tools."

    athought "The fastest way to do that is to not give him six days."

    tp_seed("a4.ob.train_him_back")

    # ========== PHASE 9 -- THE AUTHORIZATION ==========

    a "Noelle."

    "Her head lifts."

    a "Then we do not give him six days."

    "One sentence. Ten words. The authorization is the sentence."

    # --- NOELLE WAITS ---

    n "Commander."

    "She is waiting for the parameter. She needs him to name the day. The plan has a day-three authorization already in the envelope, but he has not said day three. He has said not six. She needs him to specify."

    a "Day three. Preemptive strike. Before Vestin arrives. The strike is the Sector 9 approach we scheduled for day five, compressed, with the staging window eliminated."

    a "You will draft the acceleration package and have it on the strategic room table by 1600. Nyra and I will finalize the operational parameters at 1700."

    a "Execution is authorized for day three, zero four hundred."

    "The time is 1130."

    "Day three is the morning of the fourteenth."

    "Day three is sixty-four hours from now."

    n "Understood."

    "She taps her tablet. The authorization packet propagates."

    # --- THE RIGHT PANEL UPDATES ---

    "The collision clock on the right panel recalculates."

    "It does not show time-to-Vestin anymore. It shows time-to-execution."

    "64 HOURS 30 MINUTES."

    "The clock ticks."

    # ========== PHASE 10 -- THE CIVILIAN NUMBER ==========

    n "Commander, for the record. The accelerated staging removes the pre-strike civilian evacuation window. The estimated civilian cost is nine to nineteen. The confidence interval is eighty-two percent."

    "She says it because she is required to say it. The analytical protocol requires the cost estimate to be restated at authorization. Phoenix doctrine requires the officer authorizing the operation to acknowledge the estimate verbally."

    "Aeron does not speak the acknowledgment."

    "He looks at Nyra."

    ny "Acknowledged."

    "Nyra says the word for him."

    "Noelle logs the acknowledgment under Nyra's voice stamp."

    nthought "Co-command just acknowledged a civilian cost estimate on behalf of the commander."

    nthought "This is a procedural innovation. I am not going to flag it. The ratification at 0900 covers the procedural substitution."

    nthought "Entry eight."

    # ========== PHASE 11 -- NO ONE OBJECTS ==========

    "The room waits."

    "The scene waits."

    "No one objects."

    "Noelle does not object. Noelle drafted the options. She built the left panel and the center panel and the collision clock. She presented the cost estimate. Her role is complete."

    "Nyra does not object. Nyra authored the strategy. Train him back is her doctrine and her authorship."

    "Aeron does not object. Aeron is the authorization."

    "There is no one else in the room."

    "Lyra is not in the room. She is in the chapel, not praying. Zira is not in the room. She is at her station, deciding. Tessa is not in the room. She is where Tessa goes when she is deciding whether to adapt or break."

    "The objection, if it were going to come, would have come from one of them, and none of them are here."

    "The operations room permits the authorization to stand because the operations room was built for exactly this configuration."

    # ========== PHASE 12 -- THE NAMES ==========

    "Noelle turns to the operations board."

    "The operations board is a physical whiteboard on the north wall. Phoenix uses it for operation designations -- the codename for each strike, the personnel assigned, the go-conditions, and the civilian exposure range if applicable."

    "The board currently shows four operations in varying states of planning. Noelle uncaps the marker. She writes a fifth entry."

    #play sound "sfx/whiteboard_marker_writing.ogg"

    "The entry is not in Nyra's handwriting. Nyra does not write on the operations board. Noelle writes on the operations board. Noelle has written on the operations board for fourteen months, since before Nyra arrived, since before Aeron arrived, since Selene's command."

    "She writes:"

    "OP. DESIGNATION: MERIDIAN / ACCELERATED"
    "TARGET: SECTOR 9 APPROACH"
    "EXECUTION: DAY 3 / 0400"
    "AUTH: RYLAN, A. + KAELIN, N."
    "CIVILIAN EXPOSURE: 9-19"
    "EVAC WINDOW: NONE"

    "She writes the last line with the same stroke weight as the other lines."

    "She puts the marker back in the tray."

    "The names of the civilians are not on the board. Civilians on Phoenix operation boards are recorded as integer ranges, not as names. Phoenix has never recorded civilian names on the operations board."

    "She writes the names in the margin of her tablet, under a header that reads 'PROJECTED -- MERIDIAN.'"

    "The names are not real names. They are statistical placeholders -- identifiers pulled from the Sector 9 residential registry. Nine to nineteen of these placeholders will, sometime between day three at 0400 and day three at 0700, become the names of dead people."

    "Noelle does not know which nine to nineteen."

    "She writes all forty-three names in the margin of her tablet because the register contains forty-three total residents of the Sector 9 approach zone and she has decided, without telling anyone, that she will keep the projected list as a pre-mortem roster."

    nthought "I am going to know the names before Marcus knows the names. This is a choice I am making. No one asked me to make it. No one will read the list after the operation."

    nthought "I will read the list after the operation."

    nthought "I will read it once, and I will not read it twice, and the reading will be the closest thing to accountability that the operations room permits in the shape it has been built in."

    nthought "Entry nine."

    # ========== PHASE 13 -- AERON CLOSES THE BRIEFING ==========

    a "Sixty-four hours."

    "He stands."

    a "I want the acceleration package at 1600. I want the operational parameters at 1700. I want the strike teams briefed by 2100. I want the staging complete by day two at 2200. I want the approach column in position by day three at 0330."

    a "We execute at 0400."

    "He walks to the door."

    "At the threshold he pauses. Not for a line. For the sensor."

    "The door opens."

    "He steps through."

    "The door closes."

    # ========== PHASE 14 -- NYRA AND NOELLE ==========

    "Nyra remains at the display wall."

    "Noelle remains at her station."

    "The board with MERIDIAN / ACCELERATED written on it. The collision clock showing 64 HOURS 29 MINUTES. The analytical engine refreshing the left panel with the updated Marcus response projection."

    ny "Noelle."

    "Noelle looks up."

    ny "Your work on this brief was precise. The collision clock integration was particularly clean."

    "The compliment is doctrinal, not warm. It is the same register in which Nyra compliments her own soldiers' drill performance."

    n "Thank you, Commander Kaelin."

    "Noelle uses Nyra's full rank-name. She has not used Nyra's first name since the restructuring. The shift is recent and Noelle has been doing it deliberately. Nyra has noticed and has not commented."

    ny "I will be in the strategic room at 1600 to review the package with you before the commander arrives."

    "She walks to the door. The same pace. The door opens. She steps through. The door closes."

    # --- NOELLE ALONE ---

    "Noelle is alone in the operations room."

    "The board. The clock. The photograph of Rhea Vestin in the center panel. The left panel still pulsing with Marcus's compression heat map."

    "She looks at the photograph."

    nthought "Commander Vestin. I am going to train Marcus back at you before you arrive. I am going to do it with numbers. I am going to do it with a day-three strike that eliminates the fourteen-hour staging window and kills nine to nineteen people from a residential registry of forty-three."

    nthought "I am going to draft the package that makes it clean."

    nthought "I am the secretary of my own corruption and the corruption has an operational name now. The name is MERIDIAN."

    nthought "I wonder if I will remember that the name existed before this scene. I do not think I named it before this scene. I think it named itself while I was writing the marker line."

    nthought "That is a lie. I named it. The names come from me. They always have."

    "She sits down at her station."

    "She opens a fresh document. The acceleration package template. She begins drafting."

    "The time is 1137."

    "She has four hours and twenty-three minutes to complete the package."

    "She will finish it in three hours and fifty-one minutes because that is how fast she works and the fact that the content of the package is an authorization to kill nine to nineteen civilians will not slow her work down by any measurable fraction of a second."

    "She is very good at her job."

    # --- END ---

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.echelon.rhea_incoming", True)
    $ canon_set("ob.phoenix.preemptive_authorized", True)
    $ canon_set("ob.op_meridian_named", True)
    $ metric("ob.marcus_clock", set_to=1)
    $ flag("a4_meridian_authorized", True)
    $ flag("noelle_pre_mortem_roster_ob", True)
    $ rel_bump("Nyra", trust=1)
    $ npc_remember("Noelle", "meridian_acceleration_briefing", tone="functional_corruption_entry_nine")
    $ npc_remember("Nyra", "train_him_back", tone="doctrinal_acknowledgment")
    $ npc_remember("Marcus", "expedite_three_days", tone="mirror_compression")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s03_marcus_adapts_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - 1130 on the same day as a4_s01 and a4_s02.
#   - Two hours thirty minutes after the council ratification.
#   - Sixty-four hours to the MERIDIAN / ACCELERATED execution window.
# cann.what_happened:
#   - Noelle briefs Marcus's 12-36 hour adaptation compression and Commander
#     Rhea Vestin's incoming deployment as a dedicated counter-Phoenix asset.
#   - The initial collision clock: 6 DAYS.
#   - Brief Echelon cut-in: Marcus on a steel desk in amber light, reading
#     one printed report, saying "Commander Vestin. Expedite. Three days if
#     you can." Eleven seconds. The clock updates to 5 DAYS 19 HOURS.
#   - Noelle names the civilian cost: 9-19 noncombatants for the accelerated
#     Sector 9 entry. Aeron does not react to the word civilians. Noelle
#     catalogs the not-reaction as entry seven in her private baseline file.
#   - Nyra's hinge line: "He will adapt faster than you expected because he
#     trained you. Train him back."
#   - Aeron authorizes: "Then we do not give him six days. Day three.
#     Preemptive strike. Execution is authorized for day three, zero four
#     hundred."
#   - Nyra speaks the acknowledgment of the civilian cost on Aeron's behalf
#     ("Acknowledged"). Noelle logs it under Nyra's voice stamp. Entry eight.
#   - No one objects. Lyra, Zira, and Tessa are not in the room. The
#     operations room permits the authorization.
#   - Noelle writes MERIDIAN / ACCELERATED on the operations board. In the
#     margin of her tablet, she writes all forty-three names from the Sector
#     9 residential registry as a pre-mortem roster. Entry nine.
#   - Aeron closes the briefing, sets the full 64-hour timeline. Leaves.
#   - Nyra compliments Noelle on the brief, leaves for strategic room 1600.
#   - Noelle begins drafting the acceleration package alone. "She is very
#     good at her job."
# cann.aeron_state:
#   - OB peak competence. Ten-word authorization. No reaction to the word
#     civilians. Does not speak the cost acknowledgment -- allows Nyra to
#     speak it for him, which is itself a procedural innovation.
#   - Operating on Marcus's doctrine with six weeks of field modifications.
#     Nyra has named the move. Aeron executes the naming.
# cann.thematic_flags:
#   - EMP MIRROR: EMP s03 has Aeron asking what shared command looks like
#     against Marcus. OB s03 has Aeron accelerating the tempo. The two
#     scenes are the route fork at the tactical level.
#   - "TRAIN HIM BACK": Nyra's doctrine compressed to three words. The
#     instruction is tactically correct and morally total. Aeron receives
#     both simultaneously and does not separate them.
#   - THE WORD CIVILIANS: Aeron does not react. Noelle catalogs the
#     not-reaction. "Entry seven is the first entry I have made that I will
#     not be able to read back to myself later."
#   - NYRA'S ACKNOWLEDGMENT: "Acknowledged." Co-command speaks the cost
#     acknowledgment on the commander's behalf. Procedural substitution.
#     Noelle does not flag it. Entry eight.
#   - NOELLE AS PRE-MORTEM KEEPER: she writes all forty-three Sector 9
#     resident names in her tablet margin. The list is her private
#     accountability. "The reading will be the closest thing to
#     accountability that the operations room permits in the shape it has
#     been built in." Entry nine.
#   - THE MARCUS CUT-IN: eleven seconds of Echelon command. "Commander
#     Vestin. Expedite. Three days if you can." The mirror compression --
#     Marcus is shortening his logistical cycles the way Phoenix is
#     shortening its operational cycles. The symmetry is the horror.
#   - MERIDIAN: the operation names itself on the board. Noelle later
#     admits "I named it. The names come from me. They always have."
#   - "SHE IS VERY GOOD AT HER JOB": the scene's closing sentence. The
#     corruption is the competence.
# cann.character_moments:
#   - Noelle: data-forward, quietly devastated. Private accountability
#     through the pre-mortem roster. Entry seven, eight, nine of her
#     baseline file. The most interior scene Noelle has in OB Act 4 so far.
#   - Nyra: three lines, one of which is the hinge ("Train him back"),
#     one of which is the cost acknowledgment spoken on the commander's
#     behalf. Doctrinal throughout.
#   - Aeron: ten words of authorization. Zero reaction to the civilian
#     number. Does not speak the acknowledgment. Operating cleanly inside
#     the structure ratified at 0900.
#   - Marcus: eleven-second cut-in. One line. The line is the threat and
#     the mirror simultaneously.
# cann.callbacks:
#   - a4_s01_the_cold_room_ob: the single stylus mark that moved Sector 9
#     from day three to day five. This scene moves it BACK to day three --
#     under acceleration pressure -- and the move is now costing the
#     fourteen-hour staging window.
#   - a4_s02_the_new_shape_ob: the co-command ratification that makes the
#     Nyra voice-stamp acknowledgment procedurally clean.
#   - a3_s08_perfect_execution_ob: "Clean is mercy" becomes "clean is
#     speed." The scene inherits the doctrine and updates it.
#   - a3_s22 (The Hunt): "Five to eleven" civilians rounded to acceptable.
#     This scene is nine to nineteen with zero evacuation window.
#   - EMP s03 (mirror): EMP Aeron asks shared command questions. OB Aeron
#     authorizes acceleration. The route fork at the tactical level.
#   - a3_s24_liora_ob: "I can see his charts in the way you sit." The
#     charts are now labeled MERIDIAN.
# cann.block_status:
#   - ANCHOR. Always plays on OB path. No branching. No player choice. The
#     authorization is the route thesis expressed in a single sentence.
# cann.requires_followup:
#   - a4_s04+: the MERIDIAN operation itself. 0400 day three. Sector 9.
#     Nine to nineteen civilians.
#   - Noelle's baseline file on Aeron: entry seven, eight, nine. Arc
#     setup for a later Noelle break/turn.
#   - Rhea Vestin: she is now an antagonist on the clock. Will arrive
#     after MERIDIAN and will be responding to its aftermath.
#   - The pre-mortem roster: Noelle's private accountability list. Arc
#     setup for a later reveal.
