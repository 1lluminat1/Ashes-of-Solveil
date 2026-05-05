# =======================================================
# ACT 3 - Scene 19b: Unwitnessed (Empathy Path)
# File: a3_s19b_unwitnessed_emp.rpy
# Type: NOELLE THESIS BEAT — civilizational memory-editing brief
# Matrix: Council scene. The strategic horizon reframed.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s19b_unwitnessed_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s19b_unwitnessed_emp:
    $ show_timeline("18th of Hollow, 390 A.C.", "20:30", "Phoenix Secondary Base — War Room")

    # Codex stage bumps
    $ codex_reveal("noelle_korr", to_stage=3, source="a3_s19b_unwitnessed_emp")
    $ codex_unlock("memory_editing", source="a3_s19b_unwitnessed_emp")
    $ codex_unlock("forensic_clock", source="a3_s19b_unwitnessed_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. The war room. The full strategic tier — Selene at
    #         the head, Aeron at her right, Lyra at her left, Zira and
    #         Tessa across the table, Noelle at the foot. Six figures
    #         around a single table. The composition is symmetric and
    #         the symmetry is the scene's first compositional argument.
    #         Coverage opens wide, holds the wide for the assembly,
    #         pulls into a single on Noelle for the thesis. The
    #         thesis is shot in single. The single is unbroken across
    #         the three movements. The room is the chorus; Noelle is
    #         the soloist; the camera does not cut away from her face
    #         until the thesis is delivered.
    # LIGHTING: War room. Standard council brightness — primary
    #           overheads at full, the table lit evenly. The map
    #           projection above the table is at low luminance —
    #           Selene has dimmed it for this brief. The room is
    #           shaped for verbal work tonight, not tactical.
    # SFX: War room ambient. The base's overnight HVAC hum. The
    #      occasional small mechanical sound of someone shifting in
    #      a chair. The map projection's standby tone, very low.
    #      Noelle's voice is the scene's primary acoustic event for
    #      the thesis. No music bed. The scene refuses one.
    # FACE: Selene — command face. She has already heard the brief
    #        in summary three hours ago. She is in the room as the
    #        person who has decided the room needs to hear the full
    #        version. The face is the face of someone setting down
    #        an instrument and giving the floor to another player.
    #        Aeron — receptive. The face from the alcove, applied
    #        to a council scene. He has been carrying compartments
    #        for a month. He recognizes the shape of a room about
    #        to be reshaped.
    #        Lyra — composed. Hands folded. Beads in pocket.
    #        Cathedral training applied to council attention.
    #        Zira — sharp. The face she uses when she suspects a
    #        brief is going to require Ghostline architecture
    #        adjustment. The pen tucked behind her ear is going to
    #        come out before the brief ends.
    #        Tessa — present. The face she uses for clinical
    #        rounds. The rounds-face does not differentiate by
    #        topic. The rounds-face is for whoever is in the
    #        center of the room.
    #        Noelle — pre-coda voice. Two and a half weeks before
    #        the defection-data audit. She does not yet have the
    #        four revelations. She has the operational shape of
    #        the question and the tools to articulate it. The
    #        articulation is the scene.
    # BLOCKING: Six chairs. Six figures. The table is oblong, not
    #           round — the war room has not transitioned to round
    #           yet (round is an Act IV development per
    #           canon_notes_aeron sec on furniture-as-ethics). The
    #           composition is hierarchical and the hierarchy is
    #           operational, not ceremonial. Noelle stands at
    #           the foot of the table for the thesis. She is the
    #           only figure who stands. Standing is how the room
    #           carries the seriousness of the brief.

    # ========= VOICE BASELINE =========
    # Noelle: pre-coda voice. Technical, instrumental, the register
    #          she brings to every council brief. The register is
    #          her default and the register is what she has been
    #          building toward this thesis for months. The thesis
    #          is the scene where the register becomes thesis.
    #          Faber's syntax is present in three of four of her
    #          sentence structures — she does not yet recognize
    #          this; the recognition arrives in s09a a month later.
    # Selene: command-voice. Brief, clear, deferring. She has set
    #          the room up for Noelle. She is going to defer
    #          explicitly at the end. The deferral is the scene's
    #          structural payoff for Noelle's arc.
    # Aeron: receptive. One spoken intervention midway through
    #         (translating a phrase Noelle has used technically
    #         into the operational language the room can carry).
    #         Otherwise listens.
    # Lyra: one spoken intervention near the close, providing the
    #        Cathedral-trained reframe of Noelle's thesis in
    #        liturgical language. The reframe is the gift she
    #        gives back.
    # Zira: brief technical clarification. She has been reading
    #        the same patterns Noelle is naming and confirms the
    #        intelligence layer.
    # Tessa: one quiet intervention. Names the patient layer of
    #         the thesis — what memory editing does to the
    #         patient's testimony.

    # scene bg_war_room_evening with dissolve
    # play ambient "sfx/ambient/war_room.ogg" fadein 2.0

    # ========== PHASE 1 — THE ASSEMBLY ==========

    # CAMERA: wide on the war room. The table is set
    #         for council. Five chairs are filled.
    #         Noelle's chair at the foot is empty. The
    #         empty chair is the composition's first
    #         argument — somebody is missing and the
    #         missing is going to enter and become the
    #         center.

    "The war room at oh-twenty-thirty. The table set for council. Five chairs filled — Selene at the head in the worn leather she has occupied for the better part of two years, Aeron at her right, Lyra at her left, Zira and Tessa across from them. The chair at the foot of the table is empty. The map projection above the table runs at low luminance. The room has been shaped for verbal work tonight."

    "The door opens. Noelle enters. She has a single thin folder in her right hand. The folder contains the brief she has been writing for nine days. The folder is what she is going to refer to once and not open."

    "She crosses to the foot of the table. She does not sit."

    "She places the folder on the table in front of the empty chair. She does not open it. The folder sits between her hands."

    "Selene speaks first."

    sel "Thank you all for coming on short notice. Noelle delivered me the summary at seventeen-thirty this evening. I asked her to deliver the full version to the room tonight rather than in the morning brief. The reason for the timing will be self-evident. I am giving Noelle the floor."

    sel "Noelle."

    n "Thank you, Commander."

    "She does not pick up the folder. The folder is anchor, not script."

    n "Tonight's brief has a single thesis. I am going to state it once at the start. I am going to spend the next twenty minutes explaining why the thesis is the thesis. At the close, I am going to ask the room to commit to a strategic adjustment. The adjustment is real and it is the reason I asked Selene to convene tonight."

    n "The thesis."

    "She does not pause for breath. The thesis is going to land while the room is still settling."

    n "We are not fighting a war over governance. We are fighting a war over the right to remember."

    "A pause."

    "The room receives the sentence. Aeron's eyes go to Noelle's face. Lyra's hands settle. Zira's pen comes out from behind her ear. Tessa's posture shifts a quarter-inch forward. Selene watches the room, not Noelle. The watching is itself an instruction — Selene is showing the room that she has already accepted the thesis and that the room's reaction is the data she is collecting now."

    n "I am going to defend the sentence in three movements. Movement one is the mechanism. Movement two is the timeline. Movement three is the strategic implication."

    # ========== PHASE 2 — MOVEMENT ONE: THE MECHANISM ==========

    # CAMERA: tight on Noelle. The thesis is hers; the
    #         camera honors it. The room is audible —
    #         pen sounds, breath, the occasional small
    #         shift — but visually the camera holds on
    #         her face. The reactions arrive in cuts to
    #         each character only at the close of the
    #         movement.

    n "Echelon's intelligence apparatus has, at minimum, three operational capabilities the rebellion has been treating as separate threats. They are not separate threats. They are facets of a single capability."

    n "Capability one: surveillance. Population tracking, behavioral metrics, cognitive-load monitoring at scale. The Bands. The Cores. The street sensors. Rebellion intelligence has mapped this capability in operational detail since 387 AC. We respect it. We work around it. We have built the Ghostline to operate beneath it."

    n "Capability two: targeted disposition. The Purges. The disappearances. The unlogged operations. The data I delivered to the room earlier this month — Marcus's signature on the Sector 8 authorization chain — is evidence of capability two. We have known about capability two since before any of us defected. It is the regime's coercive arm."

    n "Capability three. This is the capability the rebellion has been under-weighting."

    "She moves a half-step. Her hands rest on the back of the empty chair."

    n "Echelon edits memory."

    n "Not metaphorically. Operationally. CAD's Cognitive Architecture Directorate maintains a memory-editing program at production scale. The program targets three classes of subject: high-value internal personnel whose cooperation is operationally necessary; flagged civilian populations whose witness testimony would document otherwise concealed events; and historical records whose retroactive modification serves regime narrative."

    n "The mechanism for high-value internal personnel is selective excision under the cover of standard wellness intervention. The mechanism for flagged civilian populations is harmonic compliance conditioning, applied at neighborhood granularity, embedded in routine resonance exposure. The mechanism for historical records is the systematic modification of evidence trails — falsified manifests, edited dispatch logs, retroactive reauthorization of disposition orders."

    n "I have lived inside capability three. I designed the Neural Disposition Index that capability three uses to identify candidates. I have authored, by best estimate, between two hundred and three hundred CAD logs that I cannot remember authoring. The logs exist in my own archive. The logs are written in my hand. The dates align with days I remember as empty. I have been a subject of capability three for the entire duration of my CAD tenure."

    "She does not pause for the room to absorb the disclosure. The disclosure is not the thesis. The thesis is what comes next."

    n "I am naming the disclosure to establish the warrant. I have direct evidence of capability three because capability three has been performed on me. I am the source. The source is reliable in this register because the source is reading the records the editing left behind, not the memory the editing took."

    "Aeron speaks for the first time."

    a "I am hearing you say that the regime has the capability to make people forget what was done to them. And to make their neighbors forget."

    n "Yes. And to make the historical record forget. The evidence of an event can be removed from the system before the event reaches public testimony, if the editing cycle completes before the testimony enters a propagation network that Echelon does not control."

    a "Continue."

    # ========== PHASE 3 — MOVEMENT TWO: THE TIMELINE ==========

    # CAMERA: continues tight on Noelle. The thesis is
    #         building. The camera does not pull until
    #         the close of movement three. Reactions in
    #         the room remain audible.

    n "Movement two. The strategic implication of capability three."

    n "Capability three has a temporal cost. Editing memory is metabolically expensive at population scale. The harmonic compliance conditioning requires sustained resonance exposure — weeks, months, depending on the depth of the edit. The selective excision in high-value personnel requires repeated wellness sessions across an interval of three to twelve months for stable retention. The retroactive modification of historical records requires that the modification happen before the records propagate beyond Echelon's network — typically within six to twenty-four months of the event."

    n "Outside those windows, the editing degrades. Memory leaks. Records show inconsistencies. Witnesses begin to recall what was taken from them. Echelon's solution is not to extend the editing window. The window is biological and bureaucratic; it cannot be extended past a certain duration without unacceptable cost. Echelon's solution is to ensure the editing completes within the window."

    n "Which means."

    n "The window is the window. If a populace can be silenced, conditioned, and re-narrativized within roughly two years of an event, the event is, for operational purposes, deletable."

    n "If the populace cannot be silenced, conditioned, and re-narrativized within that window — because witnesses survive the conditioning, because evidence reaches a network Echelon does not control, because the cohort that remembers the event grows large enough that the editing mathematics fail — the event becomes permanent. Permanent in the sense that it can no longer be erased."

    "She stops."

    "She lets the room hold the math."

    "Zira speaks."

    z "You're saying the regime has a forensic clock running on every atrocity."

    n "Yes. The clock is not a metaphor. It is in the operational planning documents I have read. They call it the *propagation horizon.* They call themselves *historians.* The naming is not ironic in their internal documents. The naming is operational."

    z "How long is the horizon on Sector Eight?"

    n "Eight months from the close of the operation. Eight months from when the Purge ended. Approximately five months from tonight."

    "The room is silent."

    "Tessa speaks."

    t "Five months."

    n "Five months until the editing cycle completes. After five months, the testimony of survivors — and there are survivors, we have been treating them at the clinic — becomes legally and culturally inadmissible. Their memories will not match the historical record. The historical record will say the operation did not occur, or that it occurred differently, or that it occurred for reasons the survivors will not be able to contest because they will not be able to access the unmodified evidence trail."

    n "The survivors will be dismissed as confused. Their families will be dismissed as confused. The Cathedral will be invited to provide pastoral support for the *misremembering.* The Cathedral will provide it. The Cathedral has been providing it for forty years."

    "Lyra's hands have come out of her pocket. They rest on the table. The beads are visible. She does not speak."

    n "I am noting the Cathedral component. I am not asking the Cathedral, in the person of Lyra, to defend or repudiate it tonight. I am stating it as part of the timeline."

    l "Acknowledged."

    "Lyra's voice is the liturgical-reading voice. The voice she uses for sentences too important to allow ornamentation. The voice has not yet delivered her contribution. The voice is reserving."

    # ========== PHASE 4 — MOVEMENT THREE: THE IMPLICATION ==========

    # CAMERA: still tight on Noelle. The third movement
    #         is the thesis's payoff. The camera holds
    #         the single until the room speaks.

    n "Movement three. The strategic implication."

    n "The rebellion has been operating as if our adversary is a military and political apparatus that has to be defeated through conventional rebellion-against-regime mechanics. We have been treating the war as a war over governance — who rules, by what authority, with what legitimacy. We have been assuming that if we win the war, we will write the history."

    n "We will not. If we win the war on the timeline we have been planning for — eighteen to thirty-six months for the broader campaign — and Echelon's editing cycles have completed in the interim, we will inherit a population whose memory of what was done to them has been overwritten. We will be the rebellion that won and inherited a city that does not remember why we fought."

    n "The case will be lost before we make it."

    n "The clock is not military. The clock is forensic."

    "She lets the line land."

    n "They do not have to win. They have to outlast our capacity to remember why we are fighting. If we lose six months, we lose the case for Sector Eight. If we lose two years, we lose the cohort that remembers. The capacity is in the witnesses. The witnesses degrade with time and with editing. We do not have the time we have been planning for."

    n "Strategic implication."

    n "We have to be witnessed before we are erased."

    "She stops."

    "The room holds."

    "Selene speaks."

    sel "Define *witnessed* operationally."

    n "Three operational priorities, in order. First: extract and protect surviving testimony from the editable window. Survivors of Sector Eight, families of the disappeared from Sectors Five through Nine, internal CAD personnel whose cooperation has been edit-modified and who can be brought to a register where the editing fails — there are at least four such people at TR&D-adjacent ranks I can identify. Their testimony has to be recorded, archived in a network Echelon cannot reach, and protected from re-editing."

    n "Second: propagate the testimony beyond Echelon's editable network. Inside Solveil, all networks are reachable. Outside Solveil — the Outlands, the Free Strata communities, any post-collapse settlement that has been treated as either lost or hostile and that has therefore not been integrated into Echelon's editing infrastructure — the testimony is durable. We have to push the record outward."

    n "Third: make the propagation visible to Echelon. This is the one that will land hardest. We do not just propagate. We propagate ostentatiously. Every operation we run from this council forward should leave a documentary trail that Echelon can see being created and cannot erase. The visibility is itself the deterrent. If Echelon believes the editing will outpace the propagation, they continue editing. If Echelon believes the propagation has outpaced the editing, the calculus on future atrocities changes. We are not just preserving memory. We are altering the regime's incentive structure on whether to commit the next atrocity."

    n "Those are the priorities. The first two are the work of the next five months. The third is the work of the next eighteen."

    "She picks up the folder. She does not open it. She slides it across the table toward Selene."

    n "The brief in the folder contains the operational details — testimony candidate lists, network topology recommendations, propagation channel evaluations, resource estimates. The brief is yours, Commander."

    n "I have delivered it."

    # ========== PHASE 5 — THE ROOM ==========

    # CAMERA: pulls back to a wide. The full table.
    #         The composition has been single for the
    #         duration of the thesis. The wide is the
    #         release.

    "The room does not respond immediately."

    "Selene picks up the folder. She does not open it. The folder will be opened in private; the council is not the place for the operational details. The council is the place for the thesis, and the thesis has been delivered."

    "Tessa speaks first."

    t "The clinic has been seeing Sector Eight survivors with cognitive symptoms I have been cataloguing as trauma-related. Some of those symptoms — gaps in temporal memory, narrative inconsistency around the event, sudden recalibration of emotional attribution toward officially-sanctioned framings — match what Noelle is describing. I have been treating them as trauma. They have been receiving treatment that is cognitively therapeutic, which means I have been, without intending to, participating in the editing direction."

    t "I am going to change my treatment protocol starting tomorrow morning. The protocol will preserve survivor testimony at intake, before any therapy. The intake will be archived in a Ghostline-protected channel. The therapy will continue, but the testimony will be documented first."

    "She looks at Noelle."

    t "I should have been doing this six months ago. I did not have the framework. You gave me the framework tonight. I am going to use it."

    n "I am giving you the framework as soon as I had it. There is no should-have-been. There is the work that begins tomorrow."

    "Tessa nods."

    "Zira speaks."

    z "Ghostline can carry the propagation traffic to the Outlands. We have three relay chains that route through the perimeter at acceptable risk. I can dedicate one chain to the testimony propagation as a primary channel. I can build a second chain over the next two months that operates with the visibility you are describing — the *ostentatious* propagation. We will need to coordinate with the Free Strata couriers. I have a contact through the Liora-network — through Liora — who can stand up the receiving end."

    z "This is the use of Ghostline I have been wanting to find. We have been protecting it as a stealth asset. You are saying it should also be a documentary asset. Both. I agree."

    "She tucks the pen back behind her ear."

    "Aeron speaks."

    a "The strategic adjustment Noelle is asking us to make is the largest adjustment we have made since the broadcast. I want to be precise about what I think the room has just agreed to."

    a "We have agreed that the editing capability is real. We have agreed that the timeline is forensic, not military. We have agreed that the propagation is the work."

    a "We have not agreed on the third priority — the ostentatious propagation. The third priority is the most operationally aggressive of the three. It will draw Echelon's targeted disposition response in ways the first two will not. I want the room to commit to the third priority knowing the cost."

    a "Noelle."

    n "Yes."

    a "What is the operational cost of the third priority over the next eighteen months."

    n "Acceleration of Echelon's targeted disposition activity against the rebellion's known nodes. The visibility makes us harder to ignore. We will absorb three to five additional targeted operations against base assets across the eighteen-month horizon. We will lose people. The model estimates between four and eleven Phoenix lives across that horizon attributable to the visibility. The same model estimates between sixty and four hundred Solveil civilian lives saved across the same horizon attributable to the changed atrocity calculus. The expected value is positive at all confidence intervals I have run. The variance is large. The variance includes the four to eleven Phoenix lives. I am not hiding the variance."

    a "I want the names you have in the variance."

    n "I do not have specific names yet. I have role profiles. The role profiles map onto current Phoenix personnel at non-zero probability for several individuals at the table. I am not going to enumerate the individuals tonight."

    a "Acknowledged."

    a "I am voting for the third priority. I am telling the room that I am voting for it knowing I am in the role profile."

    "Lyra speaks."

    "Her voice is the liturgical-reading voice."

    l "I want to add one frame to Noelle's framework. Noelle has offered the rebellion a strategic horizon that is forensic. I want to name that the framework is also theological."

    l "The Cathedral has, for forty years, taught the doctrine that memory is provisional. That memory belongs to the harmonic state of the city, not to the individual. That when memory and harmony conflict, harmony takes precedence. The doctrine has been the Cathedral's contribution to the editing infrastructure. The doctrine has been my training."

    l "What Noelle is asking us to do is the inverse of the doctrine. To insist that memory is not provisional. To insist that memory belongs to the witnesses, not to the harmonic state. To make the holding of memory a political act. To make the witnessing a sacrament."

    l "I am a priest of the Cathedral. I will lose the Cathedral when I do this. I am noting the loss. I am committing to the work."

    "She places her hand flat on the table."

    l "I will draft a counter-doctrine. The counter-doctrine will be theological, not political. It will give the witnessing language. It will give the survivors a shape to hold their memory inside that the Cathedral's pastoral framing cannot easily replace. I will have a draft in three weeks."

    "Selene speaks last."

    sel "I called the room because Noelle's brief reframed my own strategic horizon at seventeen-thirty this evening and I have spent three hours testing the reframing against my own assumptions. The reframing held. Every test I ran returned the same answer."

    sel "We have been planning for the wrong war."

    sel "I am formally amending the rebellion's strategic horizon to forensic-forward. I am formally adopting the three priorities Noelle has named, with Aeron's third-priority cost framing acknowledged. I am formally tasking each of you with the operational follow-through."

    sel "Tessa: testimony intake protocol, beginning tomorrow."

    sel "Zira: Ghostline propagation architecture, two-month horizon for the second chain."

    sel "Lyra: counter-doctrine, three-week draft."

    sel "Aeron: cost-management on the third priority. You and I will run the variance review weekly."

    sel "Noelle."

    n "Yes."

    sel "I am taking the seat at the head of the table off the brief layer for this conversation. The strategic spine of the rebellion is the person who can name what we are actually fighting. I have been naming what we are fighting against. You have just named what we are fighting for. That is a different naming and the room needs both names. The room has had the first name for two years. The room has had the second name for forty minutes."

    sel "I am asking you to carry the second name. Not me. Not Aeron. You. The strategic horizon is yours to hold from this council forward. I will continue to hold the operational layer. We are going to share the spine. The sharing is what shared command is for."

    sel "Will you carry it."

    "Noelle does not respond immediately."

    "She is, for the first time in the council scene, looking at her own hands. The hands are on the back of the empty chair. The empty chair has been her position for the duration of the brief. The chair is the chair Selene is now formally offering her."

    n "I will carry it."

    n "I will carry it without changing my register more than I need to. I will continue to brief in the language I am trained in. I will not pretend to be someone the room expects in the spine seat. I will be the analyst the room needs and the strategist the war needs and the witness the survivors need. I will be those at the same time. The being-at-the-same-time is the work I have been postponing. I am not postponing it anymore."

    sel "Acknowledged."

    sel "Sit down, Noelle."

    "Noelle pulls out the chair at the foot of the table. She sits."

    "The chair holds her. The chair is the chair. The chair is now the strategic spine's chair."

    "Selene closes the council."

    sel "Tomorrow oh-six-hundred. Each of you brings the first deliverable on your task. Noelle and I will draft the operational sequencing tonight. This council is closed."

    "The room rises. The chairs scrape. The figures move toward the door — Tessa first, Zira behind her, Aeron pausing to put a hand on the back of Selene's chair before he leaves, Lyra crossing to Noelle's chair and placing one hand briefly on Noelle's shoulder before she follows the others."

    "The hand on Noelle's shoulder is the second physical contact she has had from Lyra in the entire run of the rebellion. The first was at A3_P09 *The Unmeasurable.* The hand is brief. Noelle does not turn. Lyra is gone before she does."

    "Selene and Noelle remain."

    "Selene reaches across the table. She slides the folder back toward Noelle."

    sel "Open it. Show me the operational sequencing. I am going to be your sounding board on this until oh-three-hundred. I have coffee."

    "Noelle opens the folder."

    "The work begins."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("noelle_thesis_delivered", True)
    $ flag("rebellion_strategic_horizon_forensic_emp", True)
    $ flag("noelle_strategic_spine_offered_emp", True)
    $ flag("noelle_strategic_spine_accepted_emp", True)
    $ flag("tessa_testimony_intake_protocol_pending_emp", True)
    $ flag("zira_propagation_architecture_pending_emp", True)
    $ flag("lyra_counter_doctrine_pending_emp", True)
    $ canon_set("noelle.role_emp", "strategic_spine_co_command_with_selene")
    $ canon_set("rebellion.strategic_horizon", "forensic")
    $ canon_set("rebellion.three_priorities", "extract_protect_propagate_visibly")
    $ canon_set("sector_eight.editing_window_remaining_months", 5)
    $ rel_bump("Selene", trust=3, affection=1)
    $ rel_bump("Aeron", trust=1)
    $ rel_bump("Lyra", trust=2, affection=1)
    $ rel_bump("Tessa", trust=2)
    $ rel_bump("Zira", trust=2)
    $ npc_remember("Noelle", "delivered_thesis_named_forensic_clock", weight=4)
    $ npc_remember("Noelle", "accepted_strategic_spine_from_selene", weight=3)
    $ npc_remember("Noelle", "named_capability_three_with_self_as_subject_evidence", tone="warrant_via_disclosure")
    $ npc_remember("Selene", "deferred_strategic_spine_to_noelle_council", weight=3)
    $ npc_remember("Selene", "named_what_we_are_fighting_for_distinct_from_against", tone="shared_command_extended")
    $ npc_remember("Aeron", "voted_third_priority_knowing_role_profile", tone="cost_acknowledged")
    $ npc_remember("Lyra", "committed_to_counter_doctrine_named_loss_of_cathedral", tone="theological_political_distinction_collapsed")
    $ npc_remember("Lyra", "placed_hand_on_noelle_shoulder_after_council", tone="second_contact_after_unmeasurable")
    $ npc_remember("Tessa", "named_own_six_month_treatment_gap_committed_protocol_change", tone="framework_received_used")
    $ npc_remember("Zira", "committed_ghostline_propagation_architecture", tone="documentary_asset_unlocked")
    $ tp_seed("a3.noelle.forensic_clock_named")
    $ tp_seed("a3.noelle.strategic_spine_accepted")
    $ tp_seed("a3.lyra.counter_doctrine_pending")
    $ tp_seed("a3.tessa.testimony_intake_protocol")
    $ tp_seed("a3.zira.documentary_propagation_architecture")
    $ tp_seed("a4.p15.selene_noelle_cost_of_certainty_foundation")
    $ metric("rebellion_strategic_register_count", change=1)
    $ scene_mark(_current_scene_id, "completed")
    call li_lore_check("Noelle") from _a3_s19b_lore
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_s19b_unwitnessed_emp
# cann.chapter: Act III — The Resonant Rebellion — THESIS BEAT
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - 18 Hollow 390 AC. Twenty-thirty hours. Council scene called by
#     Selene. Approximately one week after the Purge data
#     confirmation in a3_s19. Approximately five months after the
#     close of the Sector Eight Purge — Noelle names the editing
#     window on Sector Eight as having approximately five months
#     remaining before the cycle completes.
#   - Approximately ten weeks before the defection-data audit in
#     a4_s09a. The pre-coda voice is intact. Faber's syntax
#     dominates Noelle's sentence structures. She has not yet had
#     the four revelations.
# cann.what_happened:
#   - Noelle delivers the civilizational memory-editing thesis to
#     the full strategic council. Six figures around the table:
#     Selene at the head, Aeron at her right, Lyra at her left,
#     Zira and Tessa across, Noelle standing at the foot.
#   - The thesis: *"We are not fighting a war over governance. We
#     are fighting a war over the right to remember."*
#   - Three movements:
#     1. THE MECHANISM. CAD's three operational capabilities —
#        surveillance, targeted disposition, memory editing.
#        Capability three has been under-weighted by the
#        rebellion. Memory editing operates at production scale
#        across high-value internal personnel, flagged civilian
#        populations, and historical records. Noelle establishes
#        the warrant by self-disclosing she has been a subject
#        of capability three across her CAD tenure.
#     2. THE TIMELINE. Editing cycles have biological and
#        bureaucratic windows — six to twenty-four months
#        depending on edit class. Within the window, an event
#        is operationally deletable. Outside the window, the
#        event becomes permanent. Sector Eight: approximately
#        five months remaining. Echelon's internal term:
#        *propagation horizon.* Echelon's internal name for
#        themselves in this register: *historians.*
#     3. THE STRATEGIC IMPLICATION. The rebellion has been
#        planning for an eighteen-to-thirty-six-month military
#        campaign. The forensic clock runs faster than the
#        military clock. If the rebellion wins on the planned
#        timeline, the population's memory of the events the
#        rebellion is fighting against will have been overwritten
#        before the rebellion can establish the historical
#        record. Strategic implication: *we have to be witnessed
#        before we are erased.*
#   - Three operational priorities derived from the thesis:
#     a. Extract and protect surviving testimony from the
#        editable window. Sector Eight survivors, families
#        of the disappeared, internal CAD personnel.
#     b. Propagate the testimony beyond Echelon's editable
#        network — Outlands, Free Strata, post-collapse
#        settlements outside the editing infrastructure.
#     c. Make the propagation ostentatiously visible to
#        Echelon. The visibility is the deterrent. The
#        third priority is the most aggressive and will
#        draw targeted disposition response.
#   - Aeron's intervention: requires the room to commit to the
#     third priority knowing the cost. Asks Noelle for the
#     variance. Noelle: between four and eleven Phoenix lives
#     across the eighteen-month horizon attributable to the
#     visibility. Sixty to four hundred civilian lives saved
#     across the same horizon. Aeron votes for the third
#     priority knowing he is in the role profile.
#   - Lyra's contribution: names the framework as theological
#     as well as forensic. The Cathedral's forty-year doctrine
#     of memory-as-provisional has been the theological
#     contribution to the editing infrastructure. Commits to
#     drafting a counter-doctrine in three weeks. Names the
#     loss of the Cathedral in advance. Places her hand on
#     the table.
#   - Tessa's contribution: names her own six-month treatment
#     gap — has been treating Sector Eight survivors as
#     trauma without preserving testimony at intake.
#     Commits to a new protocol starting tomorrow morning.
#     "There is no should-have-been. There is the work that
#     begins tomorrow." (Noelle's response.)
#   - Zira's contribution: dedicates one Ghostline relay chain
#     to testimony propagation. Builds a second chain over
#     the next two months for ostentatious propagation. Names
#     "the use of Ghostline I have been wanting to find."
#   - Selene's deferral: amends the rebellion's strategic
#     horizon to forensic-forward, formally adopts the three
#     priorities, formally tasks each council member, and
#     offers Noelle the strategic spine seat alongside her
#     own command. Selene names the distinction: she has been
#     naming what the rebellion is fighting *against;* Noelle
#     has just named what the rebellion is fighting *for.*
#     The room needs both names. Noelle accepts the spine.
#   - The council closes. Tessa and Zira leave first. Aeron
#     pauses to put a hand on Selene's chair before leaving.
#     Lyra crosses to Noelle's chair and places one hand
#     briefly on Noelle's shoulder — the second physical
#     contact after A3_P09. Selene and Noelle remain. Selene
#     produces coffee. Noelle opens the folder. The
#     operational sequencing work begins, scheduled to run
#     until oh-three-hundred.
# cann.noelle_state:
#   - Becomes the strategic spine of the rebellion alongside
#     Selene. The pre-coda voice carries the thesis on the
#     strength of the analytic register. The register has been
#     building toward this moment for months.
#   - Self-discloses as a memory-editing subject in service of
#     establishing thesis warrant. The disclosure is operational,
#     not personal. The personal layer (Halen, parents, Vance)
#     does not surface — those revelations are still ten weeks
#     out at the time of this council.
#   - Names variance with role profiles overlapping table
#     personnel. Refuses to enumerate. Aeron accepts.
#   - Accepts the strategic spine seat. Names the work as
#     "being-at-the-same-time" — analyst-strategist-witness.
#     The being-at-the-same-time is the work she has been
#     postponing. She names the no-longer-postponing.
#   - Sits in the foot-of-table chair. The chair is now the
#     strategic spine seat. Sits with Selene to draft
#     operational sequencing until oh-three-hundred.
# cann.selene_state:
#   - Calls the council on three hours' notice after receiving
#     Noelle's summary. Spends three hours testing the
#     reframing against her own assumptions. The reframing
#     held.
#   - Defers to Noelle for the full delivery in council. Names
#     the strategic spine as a shared seat between the two of
#     them. Distinguishes "what we are fighting against"
#     (Selene's seat) from "what we are fighting for"
#     (Noelle's seat).
#   - Tasks each council member operationally. Sets next
#     council oh-six-hundred. Continues working with Noelle on
#     sequencing through the night.
# cann.aeron_state:
#   - Receptive throughout the thesis. One spoken intervention
#     in movement one (translating a phrase Noelle uses
#     technically into operational language).
#   - Insists the room commit to the third priority knowing
#     the cost. Forces the variance disclosure. Votes for the
#     third priority knowing he is in the role profile.
#   - Pauses at Selene's chair on exit, hand on the chair-back
#     for one second. The Aeron-for-Selene presence-without-
#     touch gesture from a4_s10 is established here in pre-
#     visual form.
# cann.lyra_state:
#   - Composed throughout the thesis. Hands folded, beads in
#     pocket, then on the table.
#   - Commits to a theological counter-doctrine. Names the
#     loss of the Cathedral as the cost. The naming is the
#     scene's most explicit Lyra-internal declaration since
#     A3_P09.
#   - Places one hand briefly on Noelle's shoulder after the
#     council. Second physical contact between Lyra and
#     Noelle since A3_P09 *The Unmeasurable.* Brief. No
#     verbal exchange. Noelle does not turn. Lyra leaves
#     before she does.
# cann.tessa_state:
#   - Names her own six-month treatment gap publicly in
#     council. Names that her trauma-protocol treatment has
#     been participating in the editing direction without
#     intent.
#   - Commits to an intake-first testimony protocol starting
#     tomorrow morning.
#   - Receives Noelle's "there is no should-have-been; there
#     is the work that begins tomorrow." First instance of
#     Noelle's pre-coda compassion register applied to a
#     team member's confessional moment.
# cann.zira_state:
#   - Recognizes the propagation architecture as the use of
#     Ghostline she has been wanting to find. Commits to
#     dedicated propagation chain plus second chain for
#     ostentatious propagation over two-month horizon.
#   - Names a contact through the Liora-network for the
#     receiving end. Liora-network functioning as live
#     intelligence asset at this point in the timeline.
# cann.path_tracking:
#   - EMP path only. The OB equivalent (a3_s19c_unwitnessed_ob,
#     pending) plays the structurally similar council scene
#     with the same thesis but a different ending: Noelle's
#     OB closing line is *"so we have to erase them before
#     they erase us"* — same thesis, opposite ethics. Selene
#     is dead on OB; Aeron and Nyra co-chair the council.
# cann.thematic_flags:
#   - "The clock is not military. The clock is forensic." The
#     thesis-line. Canonized as load-bearing in
#     canon_notes_noelle sec 14. Future strategic discussions
#     should reference the forensic clock as established
#     framework.
#   - "We have to be witnessed before we are erased." The
#     EMP closing line of the thesis. The OB version is the
#     inversion ("erase them before they erase us"). Same
#     mechanism, opposite ethics. The path system in two
#     sentences.
#   - The strategic spine is now formally shared. Selene has
#     transferred half the spine to Noelle. The transfer is
#     load-bearing for a4_p15 ("The Cost of Certainty"),
#     which canon notes flag as foundational. The transfer
#     also establishes Noelle's standing at the head-of-
#     table register for any subsequent council scene.
#   - Lyra's counter-doctrine commitment is the rebellion's
#     first internal theological project. The doctrine will
#     not be Cathedral-sanctioned. Lyra's status as a priest
#     who is going to lose the Cathedral is now canon. The
#     counter-doctrine is unwritten and is open authoring
#     territory.
#   - Tessa's testimony-intake protocol is the rebellion's
#     first internal mechanism for resisting capability
#     three at the patient layer. The protocol is canon.
#     Future Tessa scenes should reference the protocol as
#     active practice.
#   - Zira's documentary-asset Ghostline is the rebellion's
#     first explicit propagation infrastructure. The
#     architecture is two-month horizon and is open
#     authoring territory.
#   - Lyra-Noelle physical contact: second instance after
#     A3_P09. Brief. The contact is the scene's quietest
#     character moment and is intentional canon. Future
#     Lyra-Noelle dynamics build on this contact register.
# cann.character_moments:
#   - Noelle: standing at the foot of the table for the
#     thesis, then sitting at the close. The chair becomes
#     the strategic spine seat in real time.
#   - Noelle: self-discloses as memory-editing subject in
#     service of warrant. Operational disclosure. Personal
#     compartments closed.
#   - Noelle: "I will be the analyst the room needs and the
#     strategist the war needs and the witness the survivors
#     need. I will be those at the same time." First
#     explicit naming of being-at-the-same-time as her work.
#   - Selene: "We have been planning for the wrong war."
#     The most compressed Selene line in the scene.
#   - Selene: distinguishes against-vs-for. Names the
#     room-needs-both-names. The structural payoff for the
#     shared-command thesis from a4_s10.
#   - Aeron: votes for the third priority knowing he is in
#     the role profile. The vote is the scene's most
#     compressed Aeron moment.
#   - Aeron: hand on Selene's chair-back on exit. The gesture
#     vocabulary from a4_s09 (hand on console for Noelle)
#     established here in pre-visual form.
#   - Lyra: liturgical-reading voice throughout. Names the
#     theological frame. Commits to counter-doctrine. Places
#     hand briefly on Noelle's shoulder on exit.
#   - Tessa: names her own treatment gap publicly. The
#     naming is the most explicit confession Tessa has made
#     in any council scene to date.
#   - Zira: "the use of Ghostline I have been wanting to
#     find." Names the architectural fit. Tucks pen behind
#     ear at scene close.
# cann.callbacks:
#   - a3_s19_noelle_revelation_emp: the Purge data scene one
#     week earlier. The thesis builds on the Purge revelation
#     but extends the framework to capability three. The
#     forensic-clock naming converts the Purge revelation from
#     evidence-of-atrocity to evidence-of-deletion-cycle.
#   - a3_int_02_noelle_unmeasurable_emp: Lyra-Noelle
#     unmeasurable contact. The hand on the shoulder at the
#     end of this scene is the second physical contact in
#     that lineage.
#   - a2_s18 (A2_P14 "The Patient"): Tessa-Noelle care
#     parameter. The scene's care register lands here in
#     Noelle's response to Tessa's confession.
#   - a4_s10_what_selene_meant_emp: shared command thesis.
#     This council scene is a pre-visual establishment of
#     the shared-command structure. Selene's "we are going
#     to share the spine" prefigures Aeron-Selene shared
#     command in Act IV.
#   - a4_p15 (Selene-Noelle "The Cost of Certainty"): the
#     foundation pair-anchor scene. Selene's deferral here is
#     the seed of P15.
#   - canon_notes_noelle.md sec 11.4 (Civilizational
#     Memory-Editing Thesis): delivered per spec.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. EMP path only. The
#     thesis-level civilizational scene. Foundational for
#     a4_p15 (Selene-Noelle), every subsequent strategic-tier
#     scene, the testimony intake protocol, the counter-
#     doctrine, and the propagation architecture. The
#     forensic-clock framework is now canonical.
# cann.requires_followup:
#   - Tessa's testimony-intake protocol begins the next
#     morning. Author at discretion whether to dramatize
#     the first intake or reference it in passing.
#   - Zira's two-month propagation architecture is now on
#     the table. The architecture is unwritten. Open
#     authoring territory for any subsequent Zira scene.
#   - Lyra's three-week counter-doctrine draft is canonical.
#     The draft is unwritten. The counter-doctrine itself is
#     open authoring territory and would be one of the
#     rebellion's most theologically interesting documents.
#   - Aeron and Selene's weekly variance review is now on
#     the calendar. Author at discretion whether to drama-
#     tize. The review is the institutional mechanism for
#     the third priority's cost management.
#   - Noelle's strategic-spine seat at the foot of the table
#     is now canonical. Future council scenes should respect
#     the seating arrangement. The chair at the foot is
#     hers.
#   - The Sector Eight five-month editing window is a hard
#     timeline. Future EMP scenes should track the window's
#     remaining duration.
# =========================================================
