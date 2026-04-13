# =======================================================
# ACT 4 - Scene 07: Echelon Interlude IV (Empathy Path)
# File: a4_s07_echelon_interlude_4_emp.rpy
# Type: ECHELON INTERLUDE — Marcus POV. E_INT_204.
# Matrix: Marcus reads Aeron's shift into shared command and finds a surface.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s07_echelon_interlude_4_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s07_echelon_interlude_4_emp:
    $ show_timeline_echelon("E_INT_204", "Aeries Command Spire")


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("marcus_rylan", to_stage=3, source="a4_s07_echelon_interlude_4_emp")

    # Codex — Rhea's first named mention (Marcus brings her in here).
    $ codex_mention("rhea_vestin", source="a4_s07_echelon_interlude_4_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. The spire is always locked. Handheld is a vice of the
    #         lower city; the Aeries command spire does not drift.
    #         Open wide on the room — the long table, the banners, the mapwall
    #         behind the command chair. Aeron's absence is a negative space the
    #         camera has to find before Marcus's presence. Pan once, slow, across
    #         the table. Stop on the second chair from Marcus's right hand. That
    #         chair is Aeron's chair. It has been Aeron's chair since he was
    #         thirteen. The scene is about that chair being empty.
    #         Medium on Marcus as he enters. He walks the length of the table
    #         without looking at the chair. He looks at the chair only when he
    #         has reached his own.
    #         When he speaks — and he only speaks once in the scene — the camera
    #         does not push. The camera stays medium. Marcus does not need push-in.
    #         The room pushes in on its own by listening.
    #         Final beat: tight on Marcus's right hand, resting on the arm of the
    #         empty chair. Not gripping. Not tapping. Not moving.
    # LIGHTING: Aeries command spire, late afternoon. The long east windows carry
    #           the gold light of the end of the day. The table is in warm half-
    #           shadow. Marcus is backlit as he walks — his face is not visible
    #           until he reaches the command chair and turns. The empty chair is
    #           lit directly by the windows. It is the most illuminated object in
    #           the frame. Marcus's hand on its arm at the end is half in the gold
    #           and half in the shadow of his own sleeve.
    # SFX: Aeries command spire ambient — deep. The wind against the stone of
    #      the spire. A chime from the lower courtyard, very distant. The soft
    #      step of polished boots on polished stone. A door closing behind him.
    #      No music bed. One long held note of low string at the final beat,
    #      barely audible. The silence is the score.
    # FACE: Marcus — the composure that is not rest. Patient in the way a man is
    #       patient with a game he has played his whole life and is now playing
    #       for the last time without knowing it is the last time. Interested.
    #       The interest is the scene. Marcus has not been interested in weeks.
    #       Tonight he is interested.
    # BLOCKING: Empty spire room. Marcus enters from the eastern corridor door.
    #           Walks the long table to the command chair. Does not sit yet. Stops
    #           at Aeron's chair — the second on his right. Puts his hand on the
    #           arm of that chair. Speaks without looking at anyone because there
    #           is no one to look at. Then sits in his own chair. His hand does
    #           not come off Aeron's chair arm when he sits. The reach is
    #           ungainly on paper; the reach reads on camera as a man who refuses
    #           to let go of an absence.
    # CANON: ECHELON INTERLUDE — E_INT_204. Marcus POV. No Aeron dialogue, no
    #        Phoenix POV characters. Marcus reads the shape of Aeron's shift in
    #        Act IV — the Selene-taught shared-command posture — and concludes
    #        that Aeron has not broken. Shared command is a surface Marcus
    #        believes he can crack. Plant: Marcus is routing Commander Rhea
    #        Vestin (Echelon surgical ops) to Phoenix's sector. The scene is
    #        ninety seconds of screen time. The scene is not interiority. The
    #        scene is a father addressing a chair.

    # ========= VOICE BASELINE =========
    # NEUTRAL THIRD narrator. The narrator is cool, precise, formal — closer to
    # a briefing register than a literary one. Marcus speaks once, at length, to
    # an empty chair. His voice in that address is the voice of a man who has
    # been a general for thirty years and a father for the length of one son's
    # lifetime and has never let either voice quite separate from the other.
    # Marcus is named "m" in the speaker tag. No Aeron lines. No Phoenix lines.
    # No other speakers. Internal Aeron thought is unavailable to this scene by
    # design — the scene is what Aeron cannot see.

    # scene bg_aeries_command_spire_dusk with dissolve
    # play ambient "sfx/ambient/spire_wind_low.ogg" fadein 3.0

    # ========== PHASE 1 — THE APPROACH ==========

    "The Aeries command spire sits at the apex of the old mountain citadel, three hundred meters above the highest tier of the city, and has for six centuries been the place where the High Commander of the Aeries goes to make a decision in silence."

    "The room is long. The table is longer than the room strictly requires, because the table was cut from a single piece of mountain ironwood in the second century of the Aeries and the room was built around it rather than the other way. The banners of the seven branches hang on the north wall. The mapwall, three meters tall, carries the living tactical display of the continent — red for Echelon deployments, white for old empire, grey for everything Echelon does not yet control."

    "There are twelve chairs at the table."

    "Eleven of them are empty because this is not a council hour. One of them is empty for a different reason. The second chair from the command chair on the right hand side has been Aeron Vire's seat since the year he was thirteen and the Aeries High Commander decided to bring his son into council rooms earlier than doctrine recommended."

    "Doctrine recommended sixteen."

    "Marcus had brought his son at thirteen. He had said, at the time, that doctrine was an average and averages were not designed for the kind of son he had."

    "The seat has been empty for five months."

    # ========== PHASE 2 — THE ENTRANCE ==========

    "The eastern door opens."

    "High Commander Marcus Vire walks into the room. He is alone. The protocol for a High Commander to enter the command spire outside of a council hour requires him to be alone — no aides, no guard, no scribe — because the spire is the place for a decision that belongs to the man who will carry it."

    "He walks the length of the table at his own pace. The pace is unhurried. He is sixty-two years old and he has not lost the economy of his step — he moves the way a man moves when he has spent four decades of his life walking long tables toward command chairs, which is to say he moves as if the table is a suggestion and the chair is a destination he does not have to rush to reach."

    "He does not look at Aeron's chair as he passes it."

    "He passes it."

    "He walks the three additional paces to the command chair. Stops. Turns. Does not sit."

    "From the command chair, Aeron's chair is on his immediate right. It is always on his immediate right. In council hours, Marcus has sat in this chair and turned his head half a degree to the right to speak to his son two hundred and forty-eight times. The number is documented — the council records are exact about attendance — and Marcus has never forgotten a number attached to his son."

    "Now he turns his head half a degree to the right."

    "He looks at the empty chair."

    "For a moment, he does not move."

    # ========== PHASE 3 — THE READING ==========

    "The mapwall is doing its work. Red across the continent. White fading. Grey receding. The tactical display is a living animation of the last thirty-six hours — Echelon patrol movements, Phoenix engagement signatures, the outline of the western industrial corridor where Marcus's own analysts have drawn a small white circle Marcus has not yet commented on."

    "At the left edge of the mapwall, in a panel Marcus added himself three days ago, there is a second display."

    "The second display is not the continent. The second display is the Phoenix command structure as Marcus's analysts have been able to resolve it."

    "In the middle of the panel, there is a single name: AERON VIRE."

    "Above the name, connected by a thin analytical line, there is a second name: SELENE."

    "Below the name, by three lines — three — there are three names: ZIRA. LYRA. NOELLE. TESSA."

    "Four. Not three. Marcus counted wrong the first time. The display reads four."

    "The line between Aeron and Selene is drawn with a heavier weight than the lines below. The panel's algorithm has read the recent Phoenix operational signatures and concluded that the Selene connection is structurally different from the others — that Selene is not a subordinate to Aeron, she is a peer. Marcus's analysts flagged that line in yellow six days ago. Marcus has been watching it since."

    "The line is new."

    "The line was not in the panel a week ago. A week ago, the panel had Aeron at the top of a tree — analysts. fighters. medics. The tree had the shape of a young commander's first honest attempt at distributed command. The tree was the shape of a commander who had started to delegate because he had to, not because he wanted to."

    "The panel today has a different shape. The panel today is not a tree."

    "The panel today is two command nodes, equal weight, and four second-ring figures around them."

    "Marcus has seen this shape before."

    "He saw it in his own command structures twenty-three years ago, when his own teacher made him sit down across a table from another student and told both of them that they would share command of a corridor for nine months or neither of them would ever hold command alone."

    "His teacher had been right about that corridor. His teacher had not been right about very much else, and Marcus had carried a grudge against the teacher for a decade before admitting the grudge was grief in the wrong shape, but on the corridor the teacher had been right."

    "Marcus recognizes the shape of shared command the way a swordsman recognizes the shape of a particular school's opening stance."

    "He recognizes it because it is one of the shapes he knows how to break."

    # ========== PHASE 4 — THE INTEREST ==========

    "There is a small change in Marcus's face."

    "The change is not a smile. Marcus does not smile in empty rooms. The change is a fractional relaxation of the muscles at the corners of his mouth — the face of a man who has been bracing against the wrong hypothesis for several weeks and has just been offered the correct one."

    "For two weeks after the broadcast, Marcus's working hypothesis about his son had been: Aeron broke."

    "It had been a reasonable hypothesis. The broadcast exposure had been catastrophic in a way Marcus had not prepared for. The 2.3 million witness feed had routed through Echelon's own infrastructure with a surgical inversion that Marcus had privately admired even as his teeth clenched. The operation had been professional in the way of a man who had been taught professionalism by Marcus himself — the inheritance had been explicit, and Marcus had noted it, and the noting had hurt in a region of his chest he had long since stopped admitting existed."

    "And in the eleven hours after the broadcast, with his command network dark, Marcus had sat in this same room in this same chair and thought: my son has done this thing because my son is breaking. The execution of the priestess had been the edge of the break. The broadcast was the break itself. A commander who broadcasts is a commander who has run out of patience for the long game. A commander who runs out of patience for the long game does not recover."

    "Marcus had been wrong."

    "Marcus is not often wrong about a hypothesis about a commander. Marcus is sometimes wrong about a hypothesis about his son. The two errors have a different texture in his mouth and he has learned, over the course of a lifetime, to taste the difference."

    "He has been tasting it for six days."

    "Tonight, standing at the command chair, looking at the yellow line that connects his son's name to Selene's on the analyst panel, Marcus finishes tasting it and swallows."

    "He has started delegating."

    "That is interesting."

    "That means he has not broken."

    "A broken commander centralizes. A broken commander pulls every decision to his own chair because the chair is the only thing that feels steady under his weight. Marcus has watched three commanders break over his career and each of them had narrowed his command footprint in the final weeks before the collapse — pulling in, pulling in, pulling in, until the command structure was a single point of failure and the point of failure failed. Marcus had cleaned up after two of those collapses personally. The third had cleaned itself up."

    "Aeron is not pulling in. Aeron is pushing out. The panel's new shape is not the shape of a man collapsing toward the center; it is the shape of a man deliberately, tactically, with training-rooted discipline, building a command structure he will not be the only chair in."

    "Someone has taught him this."

    "Marcus's analysts do not know who, but Marcus does. The yellow line names her. Selene. Marcus had thought Selene was dead for eleven years. Marcus had updated that assessment four months ago, when the first Phoenix intelligence began to carry her signature, and he had refused to believe his own update for another three weeks after that because some updates are too expensive to believe on the first pass. Then he had believed it and had filed it under a category he did not look at often."

    "Selene is alive. Selene is teaching his son."

    "Selene is teaching his son the shape she learned from the same teacher Marcus learned it from."

    "Marcus is not angry about this. Anger is not a useful register for a man in his sixties in an empty spire. Marcus is, instead, something he has not been in several weeks."

    "Marcus is interested."

    # ========== PHASE 5 — THE INTEREST, DEVELOPED ==========

    "Shared command is a surface."

    "A surface is a thing Marcus understands. A single chair is a solid. A solid has one fracture point and finding the fracture point is a specialist's problem — slow, patient, often unrewarding. Most commanders who build a solid command structure die in bed."

    "A surface has many fracture points. A surface has seams. A surface has the delicate problem of trust between peers who have no bureaucratic mechanism to enforce the trust. A surface is held together by a combination of procedure, shared vocabulary, and — in the end — the small private signals that pass between command nodes when no one else is looking."

    "Marcus has spent forty years of his life learning to read small private signals between command nodes when no one else is looking."

    "He has broken six command surfaces in his career. He broke three of them without ever putting a fighter in the same building as their commander. He broke them by identifying the small signal between two nodes and poisoning it — not with misinformation, because misinformation is the tool of an amateur, but with doubt."

    "Doubt is the lever. Doubt is always the lever. You insert doubt into the seam between two command nodes and you wait and the nodes do the rest of the work themselves. The nodes do not even know they are doing the work. That is the beauty of the method."

    "Marcus has been staring at a solid for five months and he has been finding the single fracture point and he has been running out of patience with the slowness of the task."

    "He is now looking at a surface."

    "A surface has seams."

    "This surface has four seams. Selene to Aeron. Aeron to Zira. Aeron to Lyra. Aeron to Noelle. There is a fifth, latent, to Tessa, but Tessa is a category Marcus has not yet decided how to name — the analyst panel flagged her as medical command and Marcus suspects the flag is insufficient, and he will return to that question later."

    "Four seams. Four levers."

    "Marcus has never broken a surface with four seams at once. Three, yes — the Estrinian corridor in the year of the long winter. Four would be a first."

    "Marcus is sixty-two years old and he did not expect to get a first this late in his career."

    "He is, without quite letting himself say the word, pleased."

    # ========== PHASE 6 — RHEA VESTIN ==========

    "He reaches for the small panel beside the command chair. The panel is for internal Echelon communications — not the tactical display, the command-side back-channel."

    "He opens the dispatch queue."

    "He writes one line."

    "The line reads: Commander Rhea Vestin to report to the Western Industrial Theater, effective dawn, personal directive, seal mine."

    "He signs it."

    "He does not hesitate over the signing."

    "Commander Rhea Vestin is Echelon's most precise surgical-operations specialist. She has spent the last fourteen years running what Echelon internal documents call 'targeted command-node interventions' and what every other army on the continent calls 'the thing Rhea Vestin does to people you are counting on.' She is not a sword. She is a scalpel. Marcus has deployed her eleven times in his tenure as High Commander and each deployment has been documented in its own restricted file because the nature of Rhea's work does not survive in the general record."

    "Rhea has never been deployed against Phoenix before."

    "Marcus has been holding her in reserve. Holding her, specifically, for the day the hypothesis about his son resolved."

    "The hypothesis resolved six days ago. The deployment is six days late. Marcus is aware of the delay and is aware that the delay was not tactical — the delay was a father's delay, a delay of a man hoping his son would be gone from a position before the scalpel arrived."

    "His son is not gone. His son has moved forward into a position that will require the scalpel."

    "Marcus does not apologize for the delay, not even internally. Apology is the grammar of a private man and he is, tonight, a High Commander."

    "He seals the dispatch."

    "The panel confirms the signing with a small green indicator. The dispatch will reach Rhea's command by the end of the hour. Rhea will be in the western industrial theater by dawn. She will take sixty to ninety hours to read the terrain. Then she will begin."

    "Marcus closes the panel."

    # ========== PHASE 7 — THE ADDRESS ==========

    "He looks at the empty chair."

    "He takes one breath."

    "Marcus speaks for the first and only time in the scene."

    m "So you are still out there."

    m "I had begun to think I would not have the honor of this part of the work. I had begun to think the broadcast was the edge of the wheel — that you had gone over it and what I would be cleaning up was a thing that had already stopped moving."

    m "I was wrong."

    m "You are not a man who has stopped moving. You are a man who has started delegating. That is a different thing, and a harder thing, and — Anayet forgive me — a more interesting thing."

    m "A man who delegates is a man who has decided he is too important to be the only chair at his table. He has decided that because he has looked at his own death and decided that his death is not allowed to end the work. That is a commander's decision. It is the decision I made at thirty-one, in a spire not unlike this one, with my teacher in the room telling me I had taken too long to make it."

    m "You are ahead of me. You made it at twenty-eight."

    m "Twenty-eight. I know the number. I know all of your numbers. Your mother used to ask me, in the last year, whether I was keeping the numbers because I wanted to be a good father or because I wanted to be a good archivist of a son. I told her both. She laughed at me. She laughed at me often in the last year. I thought at the time that the laughter was a mercy. I think now that the laughter was a warning. She was telling me the numbers were not the son."

    m "I learned that lesson too late to practice it on her. I may yet practice it on you."

    "A pause. Marcus does not fill pauses when he is alone. The pause is the scene."

    m "I have just signed a dispatch you will not like. I am not going to pretend the signing was painless. I am also not going to pretend I hesitated. I did not hesitate. The work of a High Commander does not permit hesitation, and you, who were raised at this table, know that better than most of the people at your new one."

    m "Your new table is a surface. I have been breaking surfaces for forty years. The surface is not your mistake — the surface is your first correct decision since the broadcast, and I am proud of it in a region of my chest I do not often visit. But the surface is a thing I know how to break, and I will break it, because the work is the work and Anayet does not care which of us is holding the blade."

    m "I am sending Rhea Vestin."

    m "You do not know her name. You will know it in seventy-two hours. The knowing will be expensive. I am writing that price into the ledger of this hour and I am not, for once, subtracting it from the price of what I have already asked of you."

    m "There is no subtracting anymore."

    m "There is only the ledger."

    "He stops."

    "The room holds him."

    # ========== PHASE 8 — THE HAND ==========

    "Marcus reaches to his right."

    "He puts his hand on the arm of Aeron's chair."

    "The chair is ironwood and the wood has been polished by three and a half decades of Aeron's grandfather's hand and then by five months of Aeron's absence. The arm is warm where the sun from the east windows has been falling on it. It is cool where Marcus's sleeve has been shading it as he stood."

    "Marcus sits in the command chair without taking his hand off Aeron's."

    "The reach is awkward. His body is turned slightly toward the empty chair. His arm is extended across the small gap between the two seats. It is not a comfortable position for a man in his sixties."

    "He does not adjust."

    "He sits with his hand on the arm of his son's chair and he looks at the mapwall and the continent is red in almost all of the places that are not white and Phoenix's small corner of white is holding steady in a way that is not a miracle because Marcus does not believe in miracles, but is something Marcus has noticed and has, in the private ledger behind the spoken ledger, begun to respect."

    "The respect does not change the dispatch."

    "Rhea Vestin is moving at dawn."

    "The hand does not move."

    "Outside the east windows, the gold light reaches the end of its angle and begins to leave the table. The banners on the north wall go first into half-shadow, then into shadow. The mapwall keeps its own light. The yellow line between Aeron and Selene continues to glow on the analyst panel, faint and steady, a small bright thing Marcus has been looking at for six days and will look at for as many days as the surface lasts."

    "Marcus does not move his hand."

    "The scene holds on the hand for a count of five."

    "Fade."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("marcus_reads_shared_command", True)
    $ flag("marcus_rhea_vestin_dispatched", True)
    $ canon_set("marcus_hypothesis_a4", "aeron_delegating_not_breaking")
    $ canon_set("echelon.rhea_vestin.deployed_western_theater", True)
    $ canon_set("marcus.analyst_panel.selene_yellow_line", True)
    $ npc_remember("Marcus", "signed_rhea_vestin_dispatch_without_hesitation", weight=3)
    $ npc_remember("Marcus", "hand_on_aerons_chair_arm", weight=3)
    $ tp_seed("a4.marcus.interested_again")
    $ tp_seed("a4.echelon.rhea_vestin_incoming")
    $ metric("marcus_hypothesis_version", 4)
    $ scene_mark(_current_scene_id, "exited")
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s07_echelon_interlude_4_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Late afternoon of the same day as a4_s03. Marcus has been reading his
#     analyst panel's updates on Phoenix command structure for six days.
#     Tonight, in the spire, he resolves his hypothesis about his son and
#     signs the dispatch.
# cann.what_happened:
#   - Marcus enters the Aeries command spire alone. The protocol for
#     decisions that belong to the High Commander.
#   - He walks the long table past Aeron's empty chair without looking at
#     it. Reaches the command chair. Turns. Looks at Aeron's chair from the
#     command chair for the first time in five months.
#   - He reads the analyst panel on the mapwall. The panel has updated over
#     the last six days to show Phoenix command structure as a two-node
#     peer shape (Aeron + Selene) with four second-ring figures (Zira,
#     Lyra, Noelle, Tessa). The Selene connection is drawn with a heavier
#     weight — flagged yellow six days ago.
#   - Marcus recognizes the shape of shared command. It is the shape his
#     own teacher taught him twenty-three years ago in the Estrinian
#     corridor. He recognizes it because it is one of the shapes he knows
#     how to break.
#   - Hypothesis update: Marcus had been running "Aeron broke" as the
#     working hypothesis since the broadcast. Tonight he updates it to
#     "Aeron is delegating." A broken commander centralizes; Aeron is
#     pushing out. The update is the scene's hinge.
#   - Marcus names the mechanism of his approach. Shared command is a
#     surface. Surfaces have seams. Marcus has broken six command surfaces
#     in his career, three of them without ever putting a fighter in the
#     same building as the commander. Doubt is the lever.
#   - He identifies four seams in Phoenix's surface: Selene-Aeron,
#     Aeron-Zira, Aeron-Lyra, Aeron-Noelle. Tessa is flagged but uncategorized.
#   - Marcus opens the Echelon internal command back-channel. Writes one
#     dispatch: Commander Rhea Vestin to the Western Industrial Theater,
#     effective dawn, personal directive. Signs it. Does not hesitate.
#   - Rhea Vestin: Echelon's surgical-operations specialist. Fourteen years
#     running targeted command-node interventions. Held in reserve by
#     Marcus until the hypothesis about his son resolved. Marcus notes the
#     six-day delay was a father's delay, not a tactical delay, and
#     refuses to apologize for it even internally.
#   - Marcus speaks aloud for the only time in the scene. Addresses the
#     empty chair. The content is documented in-scene — the short version:
#     you are still out there, you are delegating, delegation is a
#     commander's decision, my wife tried to teach me the numbers are not
#     the son, I learned too late, I may yet practice the lesson on you,
#     Rhea is coming, there is only the ledger now.
#   - Final beat: Marcus reaches to his right, puts his hand on the arm of
#     Aeron's empty chair, sits in the command chair without taking the
#     hand off. The reach is awkward. He does not adjust. The hand does
#     not move. The scene holds on the hand.
# cann.aeron_state:
#   - Peripheral. Aeron is not in this scene and does not know it happened.
#     The scene is what he cannot see. Narratively, the interlude plants
#     Rhea Vestin as an incoming threat Aeron has no way to anticipate.
# cann.path_tracking: EMP
# cann.thematic_flags:
#   - The student has taught the teacher, inverted: Marcus recognizes the
#     shape Selene is teaching his son because he and Selene learned it
#     from the same teacher. The inheritance runs both directions.
#   - Delegation is a commander's decision. Marcus respects it and will
#     break it anyway. Respect is not mercy.
#   - Doubt as the lever. Seams as the fracture points of a surface. Four
#     seams, four levers — this is the Act IV Marcus method.
#   - The ledger, not the math. Marcus stops subtracting. The cost is
#     recorded and carried forward. Parallel to Aeron's "necessary is not
#     worth it" from a4_s05 — both men are keeping ledgers they refuse to
#     net out.
#   - Marcus the father vs Marcus the High Commander — the hand on the
#     empty chair is the father; the signed dispatch is the High Commander.
#     The scene refuses to resolve which is primary.
#   - Interest as the new register. Marcus has not been interested in
#     weeks. Tonight he is interested. The interest is worse than anger.
# cann.character_moments:
#   - Marcus: the walk past the chair without looking at it, then the
#     return to it from the command chair. The signing without hesitation.
#     The address to the empty chair — the only spoken beat in the scene.
#     The refusal to subtract his wife's warning from the cost of the
#     dispatch. The hand on the chair arm that does not move.
#   - No other speakers. Selene is named on the analyst panel. Zira, Lyra,
#     Noelle, Tessa are named as the second-ring figures. The scene is
#     populated by absences.
# cann.block_status: drafted
# cann.requires_followup:
#   - Rhea Vestin deployment is a planted thread. Phoenix will encounter
#     her work within 72 hours of this scene. Her first intervention
#     should appear by mid-Chapter I of Act 4. The seam she goes after
#     first is an author choice — the four named seams are all available.
#   - Marcus's analyst panel's yellow line on Selene is now canon. Any
#     future Echelon scene that touches Marcus's reading of Phoenix
#     command must be consistent with the two-node peer structure.
#   - The hand on the empty chair is a body-memory motif for Marcus. The
#     motif may echo in a later Marcus scene when the chair is either
#     filled again or deliberately removed.
#   - Marcus's reference to his wife's warning ("the numbers are not the
#     son") is a backstory plant that may be developed in a later Marcus
#     interlude or in an Aeron/Marcus direct confrontation.
#   - Tessa being flagged but uncategorized by Marcus's panel is a latent
#     thread. Echelon has not yet modeled Phoenix's care infrastructure.
#     The care pattern as unreadable (from a4_s03) is confirmed from the
#     other side of the line.
