# =======================================================
# ACT 3 - Scene 22: Liora's Execution (Empathy Path)
# File: a3_s22_liora_execution_emp.rpy
# Type: ACT 3 FINALE (EMP)
# THIS IS THE MOST IMPORTANT SCENE IN ACT 3.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s22_liora_execution_emp"
$ scene_mark(_current_scene_id, "entered")

define executioner = Character("Executioner")

label a3_s22_liora_execution_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: This scene uses three visual grammars:
    #         (1) THE NEWS: 40mm, handheld, unsteady. The camera drifts 5-8% as the information
    #             arrives. It can't hold steady. Neither can the room.
    #         (2) THE NUMBERS: 50mm, locked. Clinical. Noelle's probability assessment.
    #             Steady because the math is steady. The horror is in the steadiness.
    #         (3) THE EXECUTION: 28mm, wide. The platform. Four figures. The empty space.
    #             Then 85mm telephoto: Liora's face from far away. The compression of distance.
    #             Marcus in the background: unfocused, present, watching the monitors not her.
    #             The last moment: back to 28mm. Wide. The smallness of one person on an empty platform.
    #         (4) AFTERMATH: 40mm, handheld, almost still. Each LI in their own frame.
    #             The camera visits them. Doesn't linger. The brevity is the respect.
    # LIGHTING: The news: war room operational. Overhead strips. Harsh.
    #           The numbers: same. The light doesn't care about the content.
    #           The execution: exterior. Aeries platform. Daylight — bright, clear, indifferent.
    #           The kind of light that makes everything visible and nothing hidden.
    #           Marcus is backlit. A silhouette. You see the posture, not the face.
    #           Liora: front-lit. Fully visible. The light doesn't flinch. Neither does she.
    #           Aftermath: base interior. Amber practicals only. Overheads off. The room is dim.
    # SFX: The news: war room ambient. Then quiet. The quiet of a room that just received a blow.
    #      The numbers: Noelle's keyboard. Then nothing. The silence of math that ends badly.
    #      The execution: no ambient crowd. Wind. Echelon broadcast tone. The team watches from their feed.
    #      The platform: wind. The executioner's flat voice reading Directorate articles.
    #      After the nod: footsteps of officials leaving. Pneumatic door seal. Then only wind.
    #      The drop: no warning tone, no human command. The mechanism runs on a timer.
    #      Empty frame: one beat of wind on vacant concrete. Then black.
    #      Aftermath: base ambient. Breathing. Someone's hand on a table. The small sounds of people
    #      holding themselves together.
    # FX/COMP: The Aeries platform: high, near-empty. Four figures. Designed as spectacle.
    #          Echelon broadcast feeds: mandated city-wide. The only audience.
    #          Marcus: present. Stone-faced. Watching the broadcast monitors. Not her.
    #          Liora: hands bound. Standing. The posture of someone who has already decided how to be.
    #          After the nod: the platform empties. Officials leave. Door seals.
    #          Liora stands alone. Wind. The drop mechanism activates on its timer.
    #          The execution is entirely bureaucratic — no one stays to watch. The machine runs itself.
    # BLOCKING: The news: war room. Team present. The arrangement shatters — people move, freeze, grip.
    #           The numbers: Noelle at her terminal. The rest around her. Waiting for math to save them.
    #           The execution: the team watching. Together. However they're receiving the feed.
    #           Aftermath: scattered. Each person in their own space. The geography of separate grief.
    # CANON: ACT 3 FINALE. The scene that changes everything.
    #        Liora captured through the courier network Phoenix protected. The cost of compassion.
    #        No rescue possible — the math that saved 200 kills one.
    #        The execution is public. Marcus present. Liora doesn't beg.
    #        Echelon becomes personal enemy. "My father killed my mother because I chose mercy."
    # FACE: Aeron — the face of a man watching his mother die.
    #        There is nothing more to say about that.

    # ========= VOICE BASELINE =========
    # EMP cadence at its most stripped. Short sentences. Fragments. The warmth is in the gaps —
    # the things not said, the spaces between thoughts.
    # The execution sequence: sparse. Descriptive. The writing trusts the images.
    # Aftermath: each LI gets one beat. Brief. Complete.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - MORNING]

    #scene bg_war_room_emp with dissolve
    #play ambient "sfx/ambient/war_room_operational.ogg" fadein 1.0

    # ========== PHASE 1 — THE NEWS ==========

    "Zira comes through the door like something is wrong with gravity."

    "She's moving the way she moves when the Ghostline has delivered something that can't be filed or cross-referenced or translated into tactical data. Fast. Not running. But the stillness that usually lives in her precision is gone."

    z "We have a problem."

    "The room reads her. Selene turns from the ops board. Tessa's hands pause over her kit. Noelle's fingers stop on the keyboard."

    z "Echelon intercepted a courier in the outer Outlands. They tracked the route back through three relay stations."

    athought "The courier network. The same channels we protected. The ones we kept open because helping couriers was the right thing to do."

    z "The courier was carrying story-keeper cargo. Names. Ledgers. Records."

    athought "No."

    z "They traced the cargo to its source."

    athought "No."

    z "Liora Rylan has been captured. She's being held in the Aeries."

    "The room stops."

    "Not pauses — stops. The ambient hum of the base, the ventilation, the holo-table on standby — all of it continues, and none of it matters."

    athought "Liora."

    athought "The letter was days ago. She was alive. She was active. Eleven days since her last drop."

    athought "She was alive."

    z "Public execution. Scheduled for tomorrow. 1400 hours. The Aeries platform."

    "Zira's voice is level. She's holding it there with both hands."

    z "Broadcast across all Echelon feeds. City-wide."

    athought "The courier network."

    athought "Our courier network. The channels we kept open. The ones I chose to protect because the couriers were civilians and the Ghostline served them too."

    athought "She was using the same channels. The channels my compassion kept alive."

    athought "And Echelon found her through them."

    sel "Aeron."

    "Selene's voice. Command voice. But underneath it, something she's not letting reach the surface."

    a "I heard."

    sel "What do you need?"

    athought "What do I need."

    athought "I need this to not be happening."

    athought "I need the math to be different."

    athought "I need to not be the reason she was found."

    a "Options. I need options."

    # ========== PHASE 2 — THE NUMBERS ==========

    "Noelle's hands are on the keyboard. Already working. She started the moment Zira said 'Aeries.'"

    "The holo-table activates. The Aeries in blue light — three concentric security rings around the execution platform."

    n "We can get in. The outer perimeter has gaps. Ghostline routes are mapped."

    n "Getting out with a prisoner is the problem."

    "She runs the projection. Routes light up and extinguish."

    n "Best-case extraction: ninety seconds from first contact to full containment. Four to five of a six-person team lost."

    n "And there's a secondary consideration."

    "Noelle doesn't pause. She pauses now."

    n "If we attempt it and fail — which the math strongly suggests — Echelon gains operational intelligence on Phoenix. The counter-strike is immediate."

    n "We lose the base. We lose the Ghostline. We lose the two hundred six from the corridor."

    athought "The same math that saved two hundred through a forty-seven second window is the math that kills one now."

    athought "And the one is my mother."

    sel "Aeron."

    a "I know."

    sel "We can't."

    a "I know."

    athought "I know."

    "The room holds the weight of it."

    "Lyra's hand finds his arm. She doesn't speak. The contact says everything."

    "Tessa stands by the wall. Her hands are still. Not the clinical stillness of control — the stillness of a healer who can't heal this."

    "Zira is at the far side of the room. Her arms are crossed. Her jaw is locked. She's not looking at anyone."

    z "There has to be—"

    sel "There isn't."

    "Zira's mouth closes. She knows. She knew before she said it. She said it anyway because someone had to."

    # ========== PHASE 3 — THE EXECUTION ==========

    #stop ambient fadeout 2.0

    "Tomorrow. 1400 hours."

    "The feed is available on every Echelon channel. Zira patches it into the war room display. No one asks her to. No one tells her not to."

    #play ambient "sfx/ambient/aeries_broadcast_feed.ogg" fadein 1.0

    "The Aeries platform. High above the city. The kind of height designed to make the person on it look small."

    "Clear sky. Bright daylight. The light hides nothing."

    "The platform is near-empty. Four figures against the sky — the executioner at the control panel, two Echelon officials at the far rail, and Marcus at the monitors."

    athought "There's no audience here. The audience is every screen in Solveil."

    athought "Mandated viewing."

    athought "Marcus designed the drop."

    "A figure is brought to the platform. Hands bound. Flanked by Echelon escort."

    "She's smaller than the platform wants her to be. The architecture is designed for spectacle, and she refuses it. She walks at her own pace. The escort adjusts to her, not the other way around."

    athought "That's her."

    athought "I don't know how I know. I haven't seen her face since I was seven years old. But the way she moves — the pace, the refusal to be hurried — I know her."

    athought "The way I knew the handwriting."

    "The executioner steps forward to the rail. He holds a compliance tablet. He does not look at Liora."

    "His voice, when it comes, is flat. The cadence of a man reading a manifest."

    executioner "The condemned stands in violation of the following Directorate articles."

    executioner "Order Directive Fourteen-B, Section Three. Sedition against the lawful government of Solveil."

    executioner "Infrastructure Division Statute Twenty-Two-C. Unauthorized maintenance and operation of parallel communication infrastructure. Specifically: direct material support to the illicit relay network designated Ghostline by Cognitive Division Intercept Summary Twenty-Eight-Forty-Seven-B."

    athought "Ghostline. They named it. They have a designation for it."

    executioner "Cognitive Division Protocol Seven-A. Trafficking in classified personnel records. Two thousand four hundred and eleven entries recovered from courier cache, Sectors Six through Eleven. All recovered records had been designated for deletion under Compliance Protocol Twelve."

    athought "She kept the names."

    athought "Two thousand four hundred and eleven people the city was told to forget. She carried them through the Outlands in a paper bag."

    executioner "Order Directive Nine-F. Unauthorized contact and provision of material aid to designated hostile cell personnel. Forty-seven individual transactions documented through intercepted relay traffic."

    athought "Forty-seven."

    athought "Forty-seven times we let her through because the couriers were civilians."

    athought "Forty-seven times we counted it as mercy. Echelon counted every one."

    executioner "Military Division Article Eleven. Coordination with hostile operatives in the commission of insurgent activities. Including but not limited to: the Sector Four corridor interdiction. The Sector Six relay restoration. The Sector Nine civilian evacuation."

    athought "Our operations."

    athought "They're reading our operations as her crimes."

    athought "She wasn't at the corridor. She wasn't at the relay. She didn't coordinate the evacuation. We did."

    athought "They're executing her for what we did."

    executioner "Harmony Bureau Edict Three-B. Unauthorized preservation of records designated for erasure under the Clarity Mandate. Deliberate maintenance of memory in direct violation of sanctioned civic continuity."

    athought "They named it. Even remembering has a statute number."

    executioner "And Order Directive One-A. The root charge."

    "A pause. The executioner reads the final article the way he read the others — no stress, no weight, no change in cadence."

    executioner "Aiding and abetting known traitor Aeron Rylan in the commission of acts of rebellion against the lawful government of Solveil."

    "The world stops."

    athought "They said my name."

    athought "She never knew me. She left before I was old enough to remember her face. She wrote one letter and kept it in a drop box in the Outlands for nineteen years."

    athought "And they're killing her for helping me."

    "The executioner lowers the tablet. Each article was delivered in the same flat cadence. The charges were not accusations. They were paperwork."

    "Marcus is on the platform."

    "He stands at the observation rail. Not at the front — at the side. The position of authority that doesn't need to be central."

    "He is watching the broadcast monitors."

    "Three of them. Mounted on the inside face of the rail. Each showing a different angle of the feed going out. His own face in one. The executioner in another. Liora in the third — smaller on the screen than she is in person."

    "He watches the monitors."

    "Not her."

    athought "His wife. The mother of his son."

    athought "And he is watching a screen."

    athought "This is what happens when you remember."

    "Liora stands on the platform. The wind moves through her hair. She doesn't correct it."

    athought "She doesn't correct it."

    athought "Lyra stopped correcting her hair when she stopped performing."

    athought "My mother never started."

    executioner "Does the condemned wish to make a final statement?"

    "Liora looks into the lens. Not at Marcus. Not at the executioner. Into the broadcast — at the people on the other side of every screen in the city."

    "She says a name."

    athought "Not her own. Not a plea. Not a defiance."

    athought "A name."

    "It's quiet enough that the broadcast almost doesn't carry it. But the feed is sensitive. The microphones catch it."

    "A name. One of the forgotten. One of the six thousand four hundred and twelve."

    "She says it the way you say a prayer. The way Lyra says a prayer."

    "And then she says another."

    "And another."

    "The names. The story-keeper's last act is the same as every act before it: remembering."

    athought "She's reading her list. The list she carried through the Outlands. The names she kept."

    athought "She's saying them out loud because this is the last time anyone will."

    athought "Unless someone else remembers."

    "The executioner interrupts. The compliance tablet reactivates in his hand. The names stop."

    "Liora lifts her chin. The wind takes her hair across her face. She doesn't correct it."

    "The platform. The bright light. The two officials at the far rail. The executioner at the control panel."

    "Marcus at the monitors."

    #play sound "sfx/one_shot/execution_silence.ogg"

    "Marcus lifts his hand from the rail."

    "It's a small motion. A gesture so minor the broadcast almost misses it. His fingers lift. His head tilts forward — once. Down. Up."

    "A single nod."

    "That's all."

    "He does not look at Liora. His eyes do not leave the monitors."

    "Then he turns from the rail and walks toward the platform door."

    "The two Echelon officials in their formal robes fall in behind him. Unhurried. Procedural."

    "The executioner sets the compliance tablet on the control panel and follows. He does not look back."

    "None of them look at Liora."

    "The platform door seals behind them with a soft pneumatic hiss."

    athought "They're leaving."

    athought "They're just leaving."

    "Liora stands alone."

    "Wind."

    "The platform is silent. Her hair moves across her face. She doesn't correct it. She doesn't turn toward the sealed door. She looks at nothing in particular, and breathes."

    "A few seconds pass. Not dramatic seconds. Clock seconds. The kind that tick past in an empty corridor."

    "The drop mechanism activates on its programmed schedule. No warning tone. No command entered. The drop was never waiting for a witness."

    "It was waiting for the timer."

    "The section of the platform beneath her falls away."

    "She is gone."

    "Wind moves across the empty space. The guide-rails catch the daylight."

    "The feed holds on the absence."

    "One beat."

    #scene black with fade

    # ========== PHASE 4 — THE AFTERMATH ==========

    #stop ambient fadeout 1.0
    #play ambient "sfx/ambient/base_aftermath_quiet.ogg" fadein 2.0

    "The war room."

    "The feed is dead. The holo-table shows the Echelon seal — blue and cold and institutional."

    "No one moves to turn it off."

    athought "She was alive because we kept the courier network open. She's dead for the same reason."

    athought "My father killed my mother. Not the system. Him."

    athought "And he watched a screen instead of her face."

    "The room is still."

    "Then it isn't."

    # --- LYRA ---

    "Lyra's hands fold. The prayer position. Familiar. Practiced."

    "Her lips move. The words are inaudible."

    "But the tone — even silent, even shapeless — is different."

    athought "She's praying angry."

    # --- TESSA ---

    "Tessa moves to the wall. To her board. The portable one she keeps in the war room."

    "She takes the pen from her kit. Writes."

    "LIORA RYLAN."

    "The name joins the column. The living — and now the dead."

    # --- ZIRA ---

    z "I'll make the Ghostline remember her."

    "Her voice is flat. Controlled. The control is its own kind of violence — turned inward, held."

    z "Every relay node. Every courier drop. Every station in the network she built."

    z "Her name. Her records. Everything she kept."

    z "The Ghostline will carry it. That's what it's for."

    # --- NOELLE ---

    n "The data proves it was retaliation."

    "She says it to the room. To no one. To the record."

    n "Direct chain of causation. The arrest timeline correlates with our outreach through the Outlands network."

    n "She was captured because of us. The data is clear."

    # --- SELENE ---

    "Selene stands at the command table. Her hands flat on the surface. The same position from the Weight — the night Tessa found her counting the dead."

    sel "She was right."

    "Her voice is quiet. Not the command voice. Not the briefing voice."

    sel "About everything. About the city. About what it needed. About what Marcus was becoming."

    sel "She was right. And she's dead because she was right."

    "Her hands press harder against the table."

    sel "I want to add something to the operational record."

    a "What?"

    sel "Enemy designation. Not Echelon. Not institutional. Personal."

    sel "Marcus Rylan. Enemy. Personal."

    athought "It's a son against his father."

    athought "It was always that. Now it's official."

    a "Log it."

    sel "Logged."

    # ========== PHASE 5 — THE WEIGHT ==========

    "The room empties slowly. Each person leaves in their own time. No one says goodbye because goodbye isn't the right word for any of this."

    "Aeron stays."

    "The holo-table still shows the Echelon seal. He stares at it the way Selene stared at the empty table."

    athought "My mother."

    athought "She kept the names. She kept the pause alive in the handwriting that shaped mine."

    athought "And I never knew her."

    athought "'The city doesn't need a harder man. It needs a man brave enough to be soft when softness is the most dangerous thing you can be.'"

    "He reaches inside his jacket. The letter is there. The paper warm from his body heat."

    "He doesn't take it out. He just touches the edge. Confirms it's still there."

    athought "I'm going to carry this as a name on the list."

    athought "The way she taught me."

    "The Echelon seal glows in the war room."

    "He turns it off."

    "The room goes dark."

    #stop ambient fadeout 4.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("liora_dead", True)
    $ canon_set("liora_executed_publicly", True)
    $ flag("marcus_killed_liora", True)
    $ npc_remember("Lyra", "prayed_angry_for_liora", tone="righteous_fury")
    $ npc_remember("Tessa", "added_liora_to_board", tone="quiet_completeness")
    $ npc_remember("Zira", "ghostline_will_remember_liora", tone="controlled_violence")
    $ npc_remember("Noelle", "proved_retaliation_chain_of_causation", tone="unflinching_precision")
    $ npc_remember("Selene", "designated_marcus_personal_enemy", tone="cold_resolve")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s22_liora_execution_emp
# cann.chapter: Act III, Phase III — Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - ACT 3 FINALE. After the bookend (s21). The storm after the calm.
#   - Liora captured through the courier network. Public execution in the Aeries.
# cann.what_happened:
#   - Phase 1 (The News): Zira delivers. Liora captured through the courier network
#     Phoenix protected. Public execution scheduled. Aeries platform. Broadcast city-wide.
#   - Phase 2 (The Numbers): Noelle runs extraction probabilities. Three concentric perimeters.
#     Best route: 23% team survival. Rescue attempt risks the base, the Ghostline, the 206.
#     The math that saved 200 kills one. No rescue possible.
#   - Phase 3 (The Execution): Watched via broadcast feed. Liora on the Aeries platform.
#     The platform is near-empty — only Marcus, Liora, the executioner, and two Echelon officials.
#     The audience is all of Solveil via mandated broadcast.
#     The executioner reads Directorate-law charges — each citing specific resistance operations,
#     culminating in naming Aeron directly as the traitor she aided.
#     Marcus watches the broadcast monitors, not her. Liora says names as her final statement.
#     Marcus gives a single silent nod — then turns and walks away. The officials follow.
#     The executioner follows. The platform door seals. Liora is left alone.
#     A few seconds of wind. The drop mechanism activates on its timer — no human command.
#     The platform opens beneath her. She is gone. One beat of empty frame. Fade to black.
#     The execution is pure bureaucracy: nobody stays to watch, the machine runs itself.
#   - Phase 4 (Aftermath): Each LI responds.
#     Lyra: prays angry. Noelle: proves retaliation. Tessa: adds name to board.
#     Zira: Ghostline will remember. Selene: designates Marcus as personal enemy.
#   - Phase 5 (The Weight): Aeron alone. The letter in his jacket.
#     "My father killed my mother because I chose mercy."
#     Turns off the Echelon seal. The room goes dark.
# cann.aeron_state:
#   - The cost of compassion made flesh. His mercy led to her capture.
#   - "Echelon isn't a system anymore. It's a man." — the shift from political to personal.
#   - Carries the letter. Not as grief. As a name on the list. The way she taught him.
# cann.path_tracking:
#   - canon_set("liora_dead"), canon_set("liora_executed_publicly").
#   - flag("marcus_killed_liora"). npc_remember for all five LIs.
#   - No player choice. No branching. The weight is the scene.
# cann.thematic_flags:
#   - THE COST OF COMPASSION: The courier network Aeron protected led to Liora's capture.
#     Mercy has a price. The same channels that saved people exposed the person who built them.
#   - THE MATH: 206 lives vs 1. The corridor op's triumph becomes the execution's prison.
#     The math that makes Aeron a hero in s12 makes him helpless in s22.
#   - MARCUS NOT LOOKING: He watches the broadcast monitors, not her. The performance of power.
#     Worse than cruelty — indifference mediated through a screen. She was the instrument, not the subject.
#   - THE NOD: Marcus gives a single nod to the executioner. No dialogue. No look at Liora.
#     The brevity of the gesture is the horror. A bureaucrat confirming a form.
#   - THE CHARGES: The executioner reads Directorate articles citing the resistance's own operations
#     as Liora's crimes. The charges build until they name Aeron explicitly. Murder-by-paperwork.
#   - THE DROP: Aeries platform mechanism. After the nod, everyone leaves. Liora stands alone.
#     The drop is not a public spectacle — it is pure process. The mechanism runs on a timer.
#     No warning. No command. No one stays to watch. The machine kills her without witnesses.
#     The empty frame at the end is the thesis: Solveil's violence is bureaucratic to the point
#     that humans are not even required to be present for it.
#   - LIORA'S LAST ACT: saying names. The story-keeper's function continued to the last second.
#     She didn't beg. She didn't address Marcus. She addressed the forgotten.
#   - THE LETTER: still in his jacket. Warm from body heat. He doesn't take it out.
#     Touching the edge is enough. Confirmation of something that can't be taken.
#   - "She was right. And she's dead because she was right." — Selene's thesis for the finale.
# cann.character_moments:
#   - Lyra: The angry prayer. Faith that demands accounting. Not loss of faith — deepening.
#   - Tessa: LIORA RYLAN on the board. The dead and living on the same list. "They counted."
#   - Zira: "I'll make the Ghostline remember her." The network as memorial. Controlled violence.
#   - Noelle: "Direct chain of causation." Unflinching. The kindest cruelty — truth without padding.
#   - Selene: "Personal." Marcus designated. The rebellion becomes a war with a name.
#   - Liora: Walks at her own pace. Hair uncorrected. Says the names. Dies as the story-keeper.
#   - Marcus: Watches the broadcast monitors. Gives a single nod. Doesn't look at her. The architecture of indifference.
#   - Executioner: Reads Directorate charges in flat cadence. The cadence of a man reading a manifest.
# cann.callbacks:
#   - a3_s18a: The letter. "I fell in love with the pause." The pause couldn't save her.
#   - a3_s20: The Story Keeper. She was alive. 11 days. Now she isn't.
#   - a3_s12: The corridor op. 206 saved. The math that imprisons Aeron here.
#   - a3_s18: The Weight. Selene counting dead. "We counted the living." Now one fewer.
#   - a3_s21: The bookend. Home. The thing this scene costs.
#   - a3_s19: Marcus's signature. He signed the Purge. Now he watches the execution.
#   - a3_s17: Lyra's hair. "She used to correct it." Liora doesn't correct hers. Parallel.
#   - The Aeries platform: Marcus designed it. His infrastructure kills his wife.
# cann.block_status:
#   - ACT 3 FINALE. No branching. No choice. The scene is the choice's consequence.
# cann.requires_followup:
#   - Act 4: Echelon as personal enemy. The rebellion has a new shape.
#   - The letter: Aeron carries it. It becomes a talisman.
#   - The names Liora said: can they be recovered? A future quest.
#   - The Ghostline memorial: Zira implements it. The network carries Liora's archive.
#   - Marcus as antagonist: personal now. The confrontation is inevitable.
#   - The cost of compassion: does Aeron regret the mercy? Does he harden or persist?
#   - Lyra's angry prayer: faith tested. Does it survive? What changes?
#   - Selene's "personal" designation: command implications. Bias. Accountability.
#   - Tessa's board: Liora's name. The dead and living together. What does the board mean now?
