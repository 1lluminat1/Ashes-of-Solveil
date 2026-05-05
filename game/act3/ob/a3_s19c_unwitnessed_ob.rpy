# =======================================================
# ACT 3 - Scene 19c: Outlast (Obedience Path)
# File: a3_s19c_unwitnessed_ob.rpy
# Type: NOELLE THESIS BEAT — civilizational memory-editing brief (OB)
# Matrix: Council scene. Same thesis, opposite ethics.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s19c_unwitnessed_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s19c_unwitnessed_ob:
    $ show_timeline("18th of Hollow, 390 A.C.", "20:00", "Phoenix Base — War Room")

    # Codex stage bumps
    $ codex_reveal("noelle_korr", to_stage=3, source="a3_s19c_unwitnessed_ob")
    $ codex_unlock("memory_editing", source="a3_s19c_unwitnessed_ob")
    $ codex_unlock("forensic_clock", source="a3_s19c_unwitnessed_ob")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. The war room. The OB version. Five chairs at
    #         the table — Aeron at the head, Nyra at his right, Zira
    #         and Tessa across, Noelle at the foot, Lyra in the
    #         remaining chair at Aeron's left. Selene's chair has
    #         been removed from the table since the funeral lie. The
    #         removal is visual. The room knows. The composition is
    #         five figures and one absence-shaped piece of empty
    #         floor where the head-of-table chair used to sit
    #         doubled. The OB head-of-table is single. The geometry
    #         is hierarchical and uncontested.
    #         Coverage opens wide, holds the wide for the assembly,
    #         pulls into a single on Noelle for the thesis. Reactions
    #         arrive in cuts only at movement boundaries. Nyra's
    #         face is shot most often — she is the room's operational
    #         spine and the thesis's first practical interpreter.
    # LIGHTING: War room. OB drafting setting — primary overheads
    #           dimmer than EMP, the shadows harder, the table
    #           shaped for tactical work even when the work is
    #           verbal. The map projection above the table is at
    #           higher luminance than the EMP version — the OB
    #           council does not dim the tactical to make space
    #           for the verbal; the tactical stays present as
    #           atmospheric pressure.
    # SFX: War room ambient. The base's overnight HVAC hum. The
    #      map projection's standby tone louder than EMP. No
    #      music bed. Noelle's voice carries the thesis the same
    #      way it carries on EMP. The room around her is colder.
    # FACE: Aeron — institutional face. The face from a4_s10
    #        applied early. The face that signs the doctrine. He
    #        runs the council the way he ran the doctrine
    #        signature. The face does not change across the
    #        thesis.
    #        Nyra — operational face. Engaged, evaluating,
    #        already running the implementation in her head as
    #        Noelle delivers. Her notebook is open on the table.
    #        She takes notes during the thesis. The taking is the
    #        scene's first audible character beat — pen on paper.
    #        Lyra — composed but not the same composure as EMP.
    #        Lyra on OB is six weeks past her own pivot. The
    #        beads are not in her pocket tonight. The beads are
    #        sealed in a drawer in her quarters. She does not
    #        bring them to OB councils.
    #        Zira — sharp, but the sharpness is leaner than EMP.
    #        OB Zira has been carrying the Sector Twelve-B grief
    #        as operational fuel for weeks. The sharpness is fuel.
    #        Tessa — present. The clinical face. The face that
    #        does not differentiate.
    #        Noelle — pre-coda voice, OB inflection. Same
    #        register as EMP, calibrated colder. The thesis is
    #        the same thesis. The deployment is colder.
    # BLOCKING: Five chairs at the oblong table. The empty floor
    #           where Selene's chair used to be is between Aeron
    #           and the table's head edge. The room walks around
    #           the empty floor without acknowledging it. The
    #           not-acknowledging is the OB war room's tactical
    #           memory at work — the chair is gone because the
    #           chair-occupant is gone, and the room does not
    #           dwell.
    #           Noelle stands at the foot of the table for the
    #           thesis. She is the only figure who stands. The
    #           standing is the same standing as EMP. The room
    #           is colder around the standing.

    # ========= VOICE BASELINE =========
    # Noelle: pre-coda voice with OB calibration. The technical
    #          register is identical to EMP. The closing line is
    #          inverted. The path differences are tonal, not
    #          structural — same thesis, opposite ethics.
    # Aeron: OB ops-room voice. He runs the council. He does
    #         not defer to Noelle the way Selene did on EMP. He
    #         operates with the thesis. The not-deferring is the
    #         OB difference at the structural level.
    # Nyra: command-tier operational voice. She has been running
    #        Order Division-style review of rebellion intelligence
    #        product since the funeral lie. She is the room's most
    #        practiced consumer of strategic briefs. Her notebook
    #        is the scene's most visible artifact.
    # Lyra: OB Lyra. The voice from a3_s20a — the praying-for-
    #        the-hunt voice. The voice that has decided not to
    #        lose the Cathedral; to use the Cathedral. Her one
    #        spoken intervention is in this register.
    # Zira: OB sharp. Ghostline as counterstrike asset, not
    #        documentary asset.
    # Tessa: clinical-protocol register. The patient layer of
    #         the thesis. Her response is contained — the
    #         containment will be the seed of friction in the
    #         OB Tessa-Noelle anchor scene.

    # scene bg_war_room_evening_ob with dissolve
    # play ambient "sfx/ambient/war_room_ob.ogg" fadein 2.0

    # ========== PHASE 1 — THE ASSEMBLY ==========

    # CAMERA: wide on the war room. The five-chair
    #         configuration. The empty floor. Noelle's
    #         chair at the foot is empty. The figures
    #         are settled. The map projection runs at
    #         tactical luminance overhead.

    "The war room at oh-twenty-hundred. Five figures at the table — Aeron at the head, Nyra at his right, Lyra at his left, Zira and Tessa across. The empty floor where Selene's chair used to sit is between Aeron and the head edge of the table. The empty floor is six weeks old. The room walks around it without comment."

    "The door opens. Noelle enters. She has a single thin folder in her right hand. She crosses to the foot of the table. She does not sit. She places the folder on the table in front of the empty chair. She does not open it."

    "Aeron speaks first."

    a "Begin, Commander Korr."

    "He uses her surname-and-rank. The rank is the rank Nyra formalized for her three weeks ago — *Commander, Intelligence.* The use is operational. The OB war room runs on rank in a way the EMP war room did not. The use is also the absence of the EMP equivalent: Selene saying *Noelle.*"

    n "Thank you, Commander Rylan."

    "She matches the register. The matching is not deference. The matching is professional symmetry."

    n "Tonight's brief has a single thesis. I am going to state it once at the start. I am going to spend the next twenty minutes explaining why the thesis is the thesis. At the close, I am going to recommend a strategic adjustment. The adjustment is real and is the reason I asked Commander Vale to convene this council."

    "She uses Nyra's title-and-surname. The OB war room runs on the formal address. The forms are operational."

    n "The thesis. We are not fighting a war over governance. We are fighting a war over the right to remember. Or — more precisely, in the register this council operates in — we are fighting a war over who controls the historical record after the regime falls."

    "She makes the addition. The addition is the OB calibration. *Right to remember* is the EMP framing. *Who controls the historical record* is the OB framing. Noelle has chosen the OB framing because the OB room receives it more cleanly."

    "Nyra's pen lifts. She writes one short phrase in her notebook. The pen returns to the page edge."

    n "I will defend the thesis in three movements. Movement one is the mechanism. Movement two is the timeline. Movement three is the strategic implication."

    # ========== PHASE 2 — MOVEMENT ONE: THE MECHANISM ==========

    # CAMERA: tight on Noelle. The thesis is hers; the
    #         camera honors it. Reactions audible —
    #         Nyra's pen is the loudest. Visually the
    #         camera holds.

    n "Echelon's intelligence apparatus has, at minimum, three operational capabilities the rebellion has been treating as separate threats. They are not separate threats. They are facets of a single capability."

    n "Capability one: surveillance. Population tracking, behavioral metrics, cognitive-load monitoring at scale. Bands. Cores. Street sensors. We have mapped this. We work around it. Ghostline operates beneath it."

    n "Capability two: targeted disposition. The Purges. The disappearances. The unlogged operations. We have evidence of capability two going back to before any of us defected."

    n "Capability three. This is the capability the rebellion has been under-weighting until tonight."

    n "Echelon edits memory. Operationally, at production scale. CAD's Cognitive Architecture Directorate maintains a memory-editing program that targets three classes of subject: high-value internal personnel under cover of wellness intervention; flagged civilian populations under harmonic compliance conditioning; historical records under retroactive modification of evidence trails."

    n "I have lived inside capability three. I designed the Neural Disposition Index that capability three uses to identify candidates. I have authored, by best estimate, between two hundred and three hundred CAD logs that I cannot remember authoring. The disclosure establishes warrant. I am not asking the room to trust the thesis on faith. I am the source. The source has direct evidence."

    "The pen scratches twice in Nyra's notebook."

    "Aeron speaks."

    a "You are saying the regime has the capability to make people forget what was done to them and to make their neighbors forget."

    n "Yes. And to make the historical record forget. The evidence of an event can be removed from the system before the event reaches public testimony if the editing cycle completes before the testimony enters a propagation network Echelon does not control."

    a "Continue."

    # ========== PHASE 3 — MOVEMENT TWO: THE TIMELINE ==========

    # CAMERA: continues tight on Noelle. The room's
    #         engagement is acoustic — Nyra's pen,
    #         Lyra's quiet breathing, Zira's small
    #         shift forward in her chair.

    n "Movement two. The strategic implication of capability three is temporal."

    n "Editing memory at population scale is metabolically and bureaucratically expensive. The harmonic compliance conditioning requires sustained resonance exposure across weeks-to-months. Selective excision in high-value personnel requires repeated wellness sessions across three to twelve months for stable retention. Retroactive modification of historical records requires that the modification happen within roughly six to twenty-four months of the event before propagation outside Echelon's network."

    n "Outside the windows, the editing degrades. Memory leaks. Records show inconsistencies. Witnesses begin to recall what was taken."

    n "Echelon's solution is to ensure the editing completes within the window. Inside the window, an event is operationally deletable. Outside the window, the event becomes permanent."

    n "Sector Eight: approximately five months remaining on the editing cycle."

    "Tessa's posture shifts a quarter-inch."

    n "Echelon's internal term for the window is *propagation horizon.* Echelon's internal name for themselves in this register is *historians.* The terms are not ironic in their planning documents. The terms are operational."

    "Zira speaks."

    z "You're saying the regime has a forensic clock running on every atrocity."

    n "Yes."

    z "How long is the horizon on Sector Eight?"

    n "Five months from tonight. Approximately."

    "Zira does not respond verbally. She files the timeline."

    n "Beyond Sector Eight: every operation we have witnessed and documented but not yet propagated is sitting somewhere on the editing clock. Some are within the editable window. Some are not. The rebellion has been recording. The rebellion has not been propagating at the rate the editing requires us to."

    # ========== PHASE 4 — MOVEMENT THREE: THE IMPLICATION ==========

    # CAMERA: tight on Noelle. The closing movement
    #         is the OB inversion. The line that
    #         ends the thesis is the line the path
    #         system turns on.

    n "Movement three. The strategic implication."

    n "The rebellion has been operating as if the war is military and political — defeated through conventional rebellion-against-regime mechanics. We have assumed that if we win the war on a thirty-six-month horizon, we write the history."

    n "We will not. If we win on the planned horizon and the editing cycles complete, we inherit a Solveil whose memory has been overwritten. The case will be lost before we make it."

    n "The clock is not military. The clock is forensic."

    "She lets the line land."

    n "They do not have to win the war. They have to outlast our capacity to remember why we are fighting."

    "She does not pause for the reaction."

    n "Strategic implication."

    n "We have to erase them before they erase us."

    "She lets the line land in the room."

    "The line is the OB line. The EMP version of the line is *we have to be witnessed before we are erased.* The OB version turns the verb. *Erase them.* Same mechanism — propagation, documentation, record-control — but the verb of the action is offensive rather than defensive."

    "Aeron speaks."

    a "Operationalize."

    n "Three priorities, in order. One: extract surviving testimony from the editable window — Sector Eight survivors, families of the disappeared, internal CAD personnel whose editing is reversible under controlled conditions."

    n "Two: propagate the testimony beyond Echelon's editable network. The Outlands. Free Strata communities. Settlements outside the editing infrastructure."

    n "Three: deploy the propagation as counterstrike. Every operation we run from this council forward should leave a documentary trail Echelon can see being created and cannot erase. The visibility is the deterrent. We do not just preserve memory. We weaponize the historical record. If Echelon believes the propagation has outpaced the editing, they have to revise the calculus on whether to commit the next atrocity. The revising is the strike."

    n "First two priorities are five-month horizon. Third priority is eighteen-month horizon. The third priority is also the priority that will draw the most targeted disposition response."

    "Aeron's hand goes to his chin. The gesture is operational. He is processing the full proposal."

    "Nyra speaks."

    nyr "Cost on the third priority."

    n "Acceleration of Echelon's targeted disposition activity against rebellion known nodes. Estimated four to eleven Phoenix lives across the eighteen-month horizon attributable to the visibility. Estimated sixty to four hundred civilian lives saved across the same horizon attributable to the changed atrocity calculus. Expected value positive at all confidence intervals. Variance is large. Variance includes the four to eleven Phoenix lives. I will not enumerate names. The role profiles overlap several individuals at this table at non-zero probability."

    "Nyra writes again. Two short phrases."

    nyr "Acceptable."

    "She says it without looking up from the notebook. The single word is the OB version of Aeron's EMP vote. *Acceptable* — not *I vote for the priority knowing I am in the role profile.* The word is shorter. The word is colder. The word is the OB cost-acknowledgment."

    "Aeron's hand returns from his chin to the table."

    a "I concur with Commander Vale. The third priority is acceptable. The variance is acceptable. The role-profile overlap is acceptable in my own case and I will not require the room to debate the others. We adopt the three priorities."

    "He looks at Lyra."

    a "Lyra. The Cathedral component of the thesis. Speak."

    # ========== PHASE 5 — LYRA'S CONTRIBUTION ==========

    # CAMERA: single on Lyra. Brief. The OB version
    #         of her movement-three contribution is
    #         the inverse of EMP — same theological
    #         reframe, opposite use.

    "Lyra has been folded inward across the thesis. Her hands have been on her knees, palms down. She has not touched her pocket because the beads are not in her pocket. She has not touched the table because the OB war room does not invite the gesture."

    "She speaks."

    "Her voice is the praying-for-the-hunt voice from a3_s20a. The voice that has decided to use the Cathedral, not lose it."

    l "The Cathedral has, for forty years, taught the doctrine that memory is provisional. That memory belongs to the harmonic state of the city, not to the individual. That when memory and harmony conflict, harmony takes precedence. The doctrine has been the Cathedral's contribution to capability three."

    l "The thesis Commander Korr has presented can be reframed theologically. The reframe is straightforward."

    l "If memory belongs to the harmonic state of the city, then the rebellion's task is not to dispute the doctrine. The task is to assert that the rebellion is the harmonic state. That the editing performed under the regime's authority was disharmonic — was the corruption of a doctrine the regime did not have the authority to operate. That the rebellion's propagation is the restoration of the harmonic state, not the rejection of harmony."

    l "I will draft the reframe in three weeks. The reframe will not contradict Cathedral doctrine. The reframe will claim the doctrine. We will use the regime's own theological infrastructure against the regime. The Cathedral becomes ours by argument, not by repudiation."

    "She lets the line land."

    l "I am not going to lose the Cathedral. I am going to take it."

    "Aeron's face does not change."

    a "Acknowledged."

    "Nyra writes. One phrase."

    nyr "Useful."

    "Lyra returns her hands to her knees."

    "Tessa speaks."

    # ========== PHASE 6 — TESSA'S CONTRIBUTION ==========

    # CAMERA: single on Tessa. Brief. The OB clinical
    #         response is contained.

    t "I have been treating Sector Eight survivors as trauma patients. The treatment includes cognitive therapy that may have been participating in the editing direction without my intent. I will adjust the protocol. Testimony intake at the start of treatment. Archived in a Ghostline channel before therapy begins."

    t "The adjustment is procedural and will not affect the patient layer of the work."

    "She does not name her own gap. She does not say *I should have been doing this six months ago.* The OB Tessa-Noelle distance is already opening. The opening is small here. The opening will be load-bearing in the OB Tessa-Noelle anchor scene a3_s10b ten weeks from now."

    "Noelle does not respond directly to Tessa's contribution."

    "Tessa does not require a response."

    "The protocol adjustment is logged."

    # ========== PHASE 7 — ZIRA'S CONTRIBUTION ==========

    # CAMERA: single on Zira. The OB version of her
    #         Ghostline commitment.

    z "Ghostline can carry the propagation traffic. I have three relay chains routing through the perimeter at acceptable risk. I will dedicate one chain to testimony. I will build a second chain over the next two months for the third priority — the visible chain. The visible chain will run under specifications I am going to develop with Commander Korr's input."

    z "The visible chain is not a documentary asset. The visible chain is a counterstrike vector. We are using the propagation to make the regime's calculation worse. That is offensive use, not defensive. I want the room to be precise about that. I am not building a witness archive. I am building a weapon that takes the form of a witness archive."

    z "The Free Strata coordination will route through Liora's network. I will reach the contact through the standing pre-Phoenix protocol Selene maintained."

    "She does not say *Selene.* She says *the standing pre-Phoenix protocol Selene maintained.* The naming of the dead command is procedural. The OB war room does not soften it."

    z "Two-month build on the visible chain. First-priority chain operational within forty-eight hours."

    nyr "Acceptable."

    z "Acknowledged, Commander Vale."

    # ========== PHASE 8 — THE CLOSE ==========

    # CAMERA: pulls back to wide. The full table.
    #         Five figures plus Noelle standing at the
    #         foot. The empty floor where Selene's
    #         chair was. The room.

    a "Tasks. Clinical: Tessa, intake protocol effective tomorrow oh-six-hundred. Ghostline: Zira, both chains as briefed. Theology: Lyra, three-week draft. Intelligence: Korr, you have the strategic spine on this thesis. You will run the variance review weekly with me and Commander Vale present. The variance review is on the calendar tomorrow oh-eighteen-hundred."

    "He does not formally offer Noelle the spine the way Selene did on EMP. He assigns the spine. The assigning is the OB war room's mode. Noelle has the spine because the operational structure requires someone to have it and she is the qualified person. The qualification is the warrant. The warrant is operational."

    n "Acknowledged."

    a "Council closed. Noelle, stay. I want the operational sequencing tonight."

    "The room rises. The chairs scrape. Tessa leaves first. Zira behind her. Lyra crosses to the door without looking back. Nyra remains beside Aeron — she is the second figure who stays."

    "Three figures at the table after the council closes: Aeron, Nyra, Noelle. The triangle is the OB command tier from this council forward."

    "Noelle pulls out the chair at the foot of the table. She sits. The chair becomes the strategic spine seat in real time. There is no Selene-deferring this time. The seat was assigned. The seat is hers because the operational structure requires it."

    "Aeron does not produce coffee. Aeron produces a tactical map projection. The map resolves above the table. The first variance review begins now, ten hours before the formal calendar slot."

    "The work begins."

    "Inside the new register, the work is the same work it would have been under Selene. The mechanics of testimony extraction, propagation architecture, counterstrike vector design — the mechanics do not care about the head-of-table chair's occupant. The mechanics work."

    "The mechanics also do not differentiate between *we have to be witnessed before we are erased* and *we have to erase them before they erase us.* The mechanics produce the same operational instructions either way."

    "Noelle is going to spend the next four months carrying out instructions that look identical at the operational layer to the EMP version of the same work. The identical-at-the-operational-layer is the OB cost made invisible. The invisibility is what the path will continue to provide until the cost becomes legible — which it will, but not in this council, and not in the next, and possibly not in the next eight."

    "Tonight she works."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("noelle_thesis_delivered", True)
    $ flag("rebellion_strategic_horizon_forensic_ob", True)
    $ flag("noelle_strategic_spine_assigned_ob", True)
    $ flag("tessa_testimony_intake_protocol_pending_ob", True)
    $ flag("zira_propagation_architecture_pending_ob", True)
    $ flag("lyra_cathedral_claim_doctrine_pending_ob", True)
    $ canon_set("noelle.role_ob", "strategic_spine_assigned_under_aeron")
    $ canon_set("rebellion.strategic_horizon", "forensic_offensive")
    $ canon_set("rebellion.three_priorities_ob", "extract_propagate_counterstrike")
    $ canon_set("sector_eight.editing_window_remaining_months", 5)
    $ canon_set("ob.war_room.selene_chair_removed", True)
    $ rel_bump("Aeron", trust=1, complicity_concern=1)
    $ rel_bump("Nyra", trust=1)
    $ rel_bump("Lyra", trust=0)
    $ rel_bump("Tessa", trust=0, distance=1)
    $ rel_bump("Zira", trust=1)
    $ npc_remember("Noelle", "delivered_thesis_with_ob_inversion", weight=4)
    $ npc_remember("Noelle", "received_strategic_spine_assignment_not_offer_ob", weight=3)
    $ npc_remember("Noelle", "named_capability_three_with_self_as_subject_evidence_ob", tone="warrant_via_disclosure_cold")
    $ npc_remember("Aeron", "assigned_strategic_spine_did_not_defer_ob", tone="operational_structure_required_it")
    $ npc_remember("Aeron", "voted_third_priority_role_profile_acceptable_ob", tone="cost_filed_institutionally")
    $ npc_remember("Nyra", "wrote_acceptable_twice_in_council_notebook", tone="ob_cost_acknowledgment_register")
    $ npc_remember("Lyra", "committed_to_claim_cathedral_via_argument", tone="ob_priest_taking_not_losing")
    $ npc_remember("Tessa", "named_protocol_change_did_not_name_own_gap_ob", tone="distance_from_noelle_opening")
    $ npc_remember("Zira", "named_visible_chain_as_counterstrike_vector_not_documentary", tone="ob_weaponization_of_witness_form")
    $ tp_seed("a3.noelle.forensic_clock_named_ob")
    $ tp_seed("a3.noelle.strategic_spine_assigned_ob")
    $ tp_seed("a3.lyra.cathedral_claim_pending")
    $ tp_seed("a3.tessa.distance_from_noelle_opening")
    $ tp_seed("a3.zira.weaponized_propagation")
    $ tp_seed("a4.ob.noelle.same_mechanics_invisible_cost")
    $ metric("ob_strategic_register_count", change=1)
    $ scene_mark(_current_scene_id, "completed")
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a3_s19c_unwitnessed_ob
# cann.chapter: Act III — The Iron Accord — THESIS BEAT
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - 18 Hollow 390 AC. Twenty-hundred hours. Same calendar slot
#     as the EMP version, half an hour earlier. Council scene
#     called by Aeron and Nyra. Selene has been dead approximately
#     six weeks. The empty floor where her chair sat is visible
#     and unaddressed.
#   - Approximately ten weeks before a4_s10a (OB Defection Coda).
#     The pre-coda voice is intact. Noelle has not yet had the
#     four revelations. The Vance default is operational.
# cann.what_happened:
#   - Noelle delivers the civilizational memory-editing thesis
#     to the OB strategic council. Five chairs at the table
#     plus Noelle standing at the foot. Aeron at the head, Nyra
#     at his right, Lyra at his left, Zira and Tessa across.
#     Selene's chair has been removed. The empty floor is six
#     weeks old.
#   - The thesis is the same thesis as the EMP version with one
#     calibration: Noelle reframes "right to remember" as "who
#     controls the historical record after the regime falls."
#     The OB room receives the second framing more cleanly.
#   - Three movements identical to EMP at the operational level:
#     1. The mechanism (capability three: memory editing).
#     2. The timeline (the forensic clock; Sector Eight at five
#        months).
#     3. The strategic implication.
#   - THE INVERSION: closing line. EMP: "we have to be witnessed
#     before we are erased." OB: "we have to erase them before
#     they erase us." Same thesis. Opposite ethics. Same
#     operational priorities follow either line; the line decides
#     the framing of the priorities.
#   - Three priorities derived (per OB framing):
#     1. Extract surviving testimony from the editable window.
#     2. Propagate beyond Echelon's editable network.
#     3. Deploy propagation as counterstrike. The OB framing of
#        priority three reframes documentary as weapon. Zira
#        explicitly names this in her contribution.
#   - Cost discussion: variance estimate same as EMP (4-11
#     Phoenix lives; 60-400 civilian lives saved). Nyra:
#     "Acceptable." Aeron: concurs.
#   - Lyra's contribution: theological reframe inverted from
#     EMP. EMP Lyra commits to a counter-doctrine and names
#     the loss of the Cathedral. OB Lyra commits to a doctrine
#     that *claims* the Cathedral by argument. "I am not going
#     to lose the Cathedral. I am going to take it." Use the
#     regime's theological infrastructure against the regime.
#   - Tessa's contribution: protocol adjustment named. Does
#     not name her own gap. Does not say "should have been
#     doing this six months ago." The omission is the seed
#     of the OB Tessa-Noelle distance that will be load-
#     bearing in a3_s10b ten weeks later.
#   - Zira's contribution: dedicates two Ghostline chains.
#     Names the visible chain explicitly as counterstrike
#     vector, not documentary asset. "I am not building a
#     witness archive. I am building a weapon that takes the
#     form of a witness archive."
#   - Aeron does not formally offer Noelle the strategic
#     spine the way Selene did on EMP. He assigns it. The
#     assignment is the OB war room's mode. The qualification
#     is the warrant. The warrant is operational.
#   - Council closes. Tessa leaves first. Zira behind her.
#     Lyra crosses to the door without looking back. Nyra
#     stays. The triangle of Aeron-Nyra-Noelle is the OB
#     command tier from this council forward.
#   - No coffee. No Selene-Noelle private sounding-board
#     work. Aeron produces a tactical map projection. The
#     first variance review begins ten hours before the
#     formal calendar slot.
#   - The closing narration foregrounds the OB cost made
#     invisible: the operational mechanics produced by the
#     same thesis are identical regardless of which closing
#     line frames them. Noelle will spend four months
#     carrying out instructions that look identical at the
#     operational layer to the EMP version. The identical-
#     at-the-operational-layer is the cost. The invisibility
#     is what the path will continue to provide until the
#     cost becomes legible.
# cann.noelle_state:
#   - Same pre-coda voice as EMP. The technical register is
#     identical. The closing line is the inversion.
#   - Receives the strategic spine as assignment, not offer.
#     Acknowledges. Sits in the foot-of-table chair. The
#     chair becomes the OB strategic spine seat in real time.
#   - Names the variance with role-profile overlap at the
#     table. Refuses to enumerate. The cost is acknowledged
#     and is operational.
#   - Inverts the EMP framing on the closing line. The
#     inversion is the path system in two sentences.
#   - Will spend four months carrying out instructions that
#     produce the same operational outputs as EMP. The
#     identical-at-the-operational-layer is the OB cost made
#     invisible.
# cann.aeron_state:
#   - Runs the council. Does not defer to Noelle. Assigns the
#     strategic spine. The not-deferring is the OB structural
#     difference.
#   - Files the role-profile overlap acceptance institutionally.
#     "I will not require the room to debate the others." The
#     filing is the OB cost-acknowledgment in command-tier
#     register.
#   - Stays after council with Nyra and Noelle. The triangle is
#     established here.
# cann.nyra_state:
#   - First major Noelle-thesis council Nyra has chaired. Her
#     notebook is the scene's most visible operational artifact.
#     Pen scratches at three points in the brief.
#   - "Acceptable." Two times — once on cost, once on Lyra's
#     reframe. The single word is the OB cost-acknowledgment
#     register. The word is shorter and colder than the EMP
#     equivalent.
#   - Stays after the council. Co-runs the variance review.
# cann.lyra_state:
#   - OB Lyra. The praying-for-the-hunt voice. Beads sealed
#     in a drawer in her quarters. Hands on knees, palms
#     down throughout the brief.
#   - Commits to a doctrine that claims the Cathedral by
#     argument. "I am not going to lose the Cathedral. I am
#     going to take it." The OB inversion of the EMP Lyra
#     commitment.
#   - Crosses to the door without looking back. Does not place
#     a hand on Noelle's shoulder. The OB Lyra-Noelle distance
#     is an absence. The absence is canon.
# cann.tessa_state:
#   - Names the protocol change. Does not name her own gap.
#     Does not say "should have been doing this six months
#     ago." The OB containment opens the distance between
#     Tessa and Noelle that will be load-bearing in a3_s10b.
#   - Leaves first. The leaving is operational, not
#     emotional. The not-naming-of-the-gap is the
#     character moment.
# cann.zira_state:
#   - Sharp throughout. Pen behind ear, no notebook out.
#   - Names the visible chain as counterstrike vector
#     explicitly. The naming distinguishes the OB use from
#     the EMP use. "I am building a weapon that takes the
#     form of a witness archive."
#   - References Selene's pre-Phoenix protocol procedurally
#     without softening. The OB war room's tactical memory
#     at work.
# cann.path_tracking:
#   - OB path only. Structural twin of a3_s19b_unwitnessed_emp.
#     Same thesis. Three differences:
#     a. Closing line inverted ("erase them" vs "be witnessed").
#     b. Lyra's reframe inverted (claim vs counter).
#     c. Strategic spine assigned vs offered.
# cann.thematic_flags:
#   - "We have to erase them before they erase us." The OB
#     thesis-line. Canonized in canon_notes_noelle sec 14.
#     Future OB strategic discussions should reference the
#     erasure framing.
#   - "I am not building a witness archive. I am building a
#     weapon that takes the form of a witness archive." Zira's
#     OB framing of propagation. Canonical for OB Ghostline
#     architecture going forward.
#   - "I am not going to lose the Cathedral. I am going to
#     take it." Lyra's OB theological commitment. Canonical
#     for OB Lyra going forward. The Cathedral-claim doctrine
#     is unwritten and is open authoring territory.
#   - The OB cost made invisible: the operational mechanics
#     produced by the same thesis are identical regardless of
#     which closing line frames them. The invisibility is
#     thematic and operational. Future OB scenes should
#     respect that the OB rebellion's day-to-day work looks
#     largely indistinguishable from the EMP rebellion's day-
#     to-day work, and that the indistinguishability is the
#     OB path's deepest structural argument: doing the right
#     thing for the wrong reason produces the same outputs
#     and a different person.
#   - Lyra-Noelle physical contact: ABSENT on OB. EMP version
#     has a hand on the shoulder after council. OB version
#     has no contact and Lyra does not look back. The
#     absence is canon.
#   - Tessa-Noelle distance opens here. The seed is the
#     omission of the gap-naming. Future OB Tessa-Noelle
#     scenes track the distance opening. The opening lands
#     fully in a3_s10b (OB Tessa-Noelle anchor).
#   - Strategic spine assigned, not offered. The OB structural
#     difference at the leadership layer. Aeron does not
#     defer. The deference would be a Selene-coded gesture
#     and Selene is dead. Aeron occupies the head-of-table
#     register without contest.
# cann.character_moments:
#   - Noelle: same standing-at-foot blocking as EMP. The
#     register matches. The closing line inverts.
#   - Noelle: "I will not enumerate names." The same line
#     from EMP. Same compression on the cost. The variance
#     is named without faces.
#   - Aeron: "Operationalize." One word. The OB compression
#     of the EMP "Continue."
#   - Nyra: notebook open, pen active. Three pen events in
#     the scene. "Acceptable" twice.
#   - Lyra: "I am going to take it." The OB-claim line.
#   - Tessa: "The adjustment is procedural and will not
#     affect the patient layer of the work." The
#     compression. The not-naming of the gap.
#   - Zira: "weapon that takes the form of a witness
#     archive." The OB Ghostline naming.
# cann.callbacks:
#   - a3_s14_noelle_calculus_ob: the OB Purge data
#     confirmation. The thesis here builds on it the same
#     way the EMP thesis builds on a3_s19_noelle_revelation.
#   - a3_s20a_lyra_prays_for_the_hunt_ob: the praying-for-
#     the-hunt voice arrives in council scene context here.
#   - a3_s02a_silent_table_ob: the empty Selene chair was
#     established there. The chair-removal is consistent
#     with the OB war room's tactical-memory practice.
#   - a4_s09 (OB doctrine signature): Aeron's
#     institutional-cold register, the assignment mode of
#     command, the cost-acknowledgment vocabulary. All
#     established here in the previous chapter.
#   - canon_notes_noelle.md sec 11.4 (Civilizational
#     Memory-Editing Thesis): both versions delivered per
#     spec. Path differences are tonal, not structural —
#     same thesis, opposite ethics.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. OB path only. The
#     OB thesis-level civilizational scene. Foundational
#     for: every subsequent OB strategic-tier scene, OB
#     Tessa-Noelle distance trajectory, OB Lyra-Cathedral
#     claim doctrine, OB Zira-counterstrike Ghostline
#     architecture. The forensic-clock framework is
#     canonical on both paths.
# cann.requires_followup:
#   - Tessa's testimony-intake protocol begins the next
#     morning on OB. Author at discretion whether to
#     dramatize. The protocol is the same as EMP at
#     operational level. The character framing is colder.
#   - Zira's two-month visible chain will be operational
#     mid-Glass 390. The chain is canon. The chain's
#     character — counterstrike vector — is the OB use
#     of Ghostline going forward.
#   - Lyra's three-week Cathedral-claim doctrine draft is
#     canonical. The draft is unwritten. The doctrine's
#     theology is open authoring territory and would be
#     one of the rebellion's most ethically uncomfortable
#     documents on OB.
#   - Aeron-Nyra-Noelle weekly variance review is
#     canonical. The review is the operational mechanism
#     for cost management on the third priority. Author
#     at discretion whether to dramatize.
#   - Sector Eight five-month editing window applies on
#     both paths. The clock is the same clock. The
#     operational pressure is the same operational
#     pressure.
#   - Noelle's strategic-spine seat at the foot of the
#     table is now canonical on OB. Future OB council
#     scenes should respect the seating arrangement. The
#     chair at the foot is hers because the operational
#     structure requires it.
# =========================================================
