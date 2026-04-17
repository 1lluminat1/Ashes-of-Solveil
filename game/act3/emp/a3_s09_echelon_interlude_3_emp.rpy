# =======================================================
# ACT 3 - Scene 09: Echelon Interlude 3 -- Purge Calculus (Empathy Path)
# File: a3_s09_echelon_interlude_3_emp.rpy
# Type: INTERLUDE (E_INT_203 -- Purge Calculus)
# No choices. ~90 seconds. Dossier frame. Monochrome. Institutional.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s09_echelon_interlude_3_emp"
$ scene_mark(_current_scene_id, "entered")

define logistics = Character("Logistics")
define commander = Character("Commander")

label a3_s09_echelon_interlude_3_emp:

    $ show_timeline_echelon("E_INT_203", "Aeries — Logistics Division")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Locked. 50mm. Flat institutional framing. No push-ins. No drama.
    #         Wide on the requisition table -- papers, ledgers, a single terminal.
    #         Partial profiles only. Hands on documents. Voices as function.
    #         The last shot holds on the stamped page. No face. Just the seal.
    # LIGHTING: Monochrome dossier frame. Overhead fluorescents -- the kind that make
    #           skin look grey. No warmth. No shadows. Everything evenly lit, evenly dead.
    # SFX: Air seal hiss (open/close). Stamp on paper. Clock tick underneath.
    #      Paper sliding across metal table. Pen on form. Terminal key (single stroke).
    #      No music. No ambiance. Just machinery.
    # UI: Muted serif font. Stamped header: ECHELON // INTERNAL // TIER-3
    # FACE: Never fully shown. Partial profiles at most. Hands. Paper. The architecture
    #        of governance as seen from inside the filing cabinet.

    # ========== ECHELON -- RESOURCE ALLOCATION DIVISION ==========

    scene black with fade

    # VISUAL: Dossier frame. Monochrome. The world as spreadsheet.
    "ECHELON // INTERNAL // TIER-3"

    pause 0.5

    logistics "Purge window assessment. Sectors Nine through Twelve. Requested timeline: fourteen days."

    "Paper sliding across the table."

    commander "Go."

    logistics "Rerouting food lines around Phoenix-adjacent sectors requires shutting down three distribution nodes. Sectors Ten and Eleven lose supply access for seventy-two hours minimum."

    commander "Acceptable."

    logistics "That's six thousand civilians. Three days without centralized rations."

    commander "They have local reserves."

    logistics "Local reserves cover forty-eight hours. The gap is real."

    "A pen tapping once against the desk. Measured. Not impatient."

    commander "Note it."

    logistics "Noted."

    "Clock tick."

    logistics "Secondary impact: medical supply chain to the Sector Eleven field clinic diverts through the eastern corridor. The corridor we've compressed for the Phoenix containment."

    commander "Meaning?"

    logistics "Meaning the clinic loses resupply for the duration of the purge window. Non-critical patients are manageable. Critical patients are not."

    "Paper shuffling. A new form pulled from the stack."

    commander "Estimated critical patients in the window?"

    logistics "Seventeen. Four pediatric."

    "Silence. The clock ticks. Three beats."

    logistics "Noted... but they're children."

    commander "Then note that, too. We record what is true."

    "The pen moves. The form fills. Each line a fact. Each fact a cost."

    logistics "The Phoenix cell has disrupted three supply runs in the last month. Estimated regime loss: fourteen thousand credits in materiel, plus the Sector Nine node."

    logistics "Containment cost of the purge operation itself: twenty-two thousand credits. Personnel reallocation, surveillance deployment, food line rerouting, corridor compression maintenance."

    commander "Net assessment?"

    logistics "Phoenix is costing us more to contain than to ignore."

    "A pause. The commander's hand moves into frame. Opens a ledger. Turns to a page already marked."

    commander "Ignoring them isn't on the table. The General was specific."

    logistics "The General's specifications don't appear in the budget."

    commander "The General's specifications don't need to. He has other ledgers."

    "The form is complete. The commander reads it. Every line."

    commander "File it. Copy to Operations. Copy to the General's office, sealed."

    logistics "And the four pediatric cases?"

    "The commander's hand reaches for the stamp. Brass. Heavy. The seal of the Resource Allocation Division -- a circle bisected by a vertical line. The simplest geometry. The most absolute."

    commander "They're in the file."

    "Stamp."

    "Seal."

    "The paper is filed. The terminal logs the entry. A single keystroke."

    "Air seal. The door closes."

    "The room is empty. The fluorescents hum. The clock ticks."

    "On the table, the ledger lies open to the page the commander marked. A column of numbers. Costs and allocations. At the bottom, in handwriting that is careful and legible and utterly without affect:"

    "PURGE WINDOW: APPROVED."

    "The fluorescents hum."

    "The clock ticks."

    scene black with fade

    # ========== STATE UPDATES ==========

    $ flag("echelon_purge_calculus_seen", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s09_echelon_interlude_3_emp
# cann.chapter: Act III, Phase I -- Proving Ground (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase I. Concurrent with Phoenix rebuilding after Echelon Strikes Back.
#   - Echelon internal. The regime is recalculating costs.
#   - E_INT_203 from Doc 38 (Purge Calculus).
# cann.what_happened:
#   - Logistics officer presents purge window assessment to commander.
#   - Rerouting food lines leaves two sectors short for three days. Six thousand civilians.
#   - Medical supply chain to Sector 11 clinic disrupted. Seventeen critical patients. Four pediatric.
#   - "They're children." / "Then note that, too. We record what is true."
#   - Phoenix operations costing more to contain than to ignore. 14K credits in materiel loss.
#   - Purge containment cost: 22K credits. Net assessment: Phoenix is expensive.
#   - But ignoring them isn't on the table. "The General was specific."
#   - Marcus has "other ledgers" -- his budget is personal, not institutional.
#   - Purge window approved. Filed. Sealed. The machinery processes.
# cann.aeron_state:
#   - Aeron not present. Enemy POV. Player-only information.
# cann.path_tracking:
#   - No choices. No empathy impact. Interlude / pressure beat only.
#   - flag("echelon_purge_calculus_seen") for future gating.
# cann.thematic_flags:
#   - Bureaucracy as violence. The stamp, the seal, the clock tick.
#   - "We record what is true." -- the regime's epistemology. Truth as notation, not ethics.
#   - Children as line items. The four pediatric cases exist in the file. That's their status.
#   - The Logistics officer hesitates ("but they're children"). The Commander absorbs. Does not flinch.
#   - The cost calculus: Phoenix is expensive. The purge is more expensive. They do it anyway.
#     Because Marcus wants it. "The General's specifications don't appear in the budget."
#   - "Other ledgers" -- Marcus's personal investment in the Aeron hunt runs outside normal channels.
#   - The stamp as the scene's punctuation. Brass. Heavy. Final.
#   - Mirror of a2_s24 (Compliance Spike): same dossier grammar, escalated stakes.
#     E_INT_201: recognition. E_INT_202: audit. E_INT_203: resource commitment.
#     The machine is accelerating.
# cann.character_moments:
#   - Logistics: Competent. Does the math. Pauses on the children. Logs the pause.
#     The hesitation is human. The continuation is institutional.
#   - Commander: Not cruel. Thorough. "We record what is true" is his entire philosophy.
#     Truth-as-procedure. He doesn't enjoy it. He doesn't need to.
#   - Marcus (offscreen): "The General was specific." His shadow governs the scene.
#     "Other ledgers" implies personal resources devoted to Phoenix containment.
# cann.block_status:
#   - INTERLUDE (E_INT_203). Both paths. No choices. ~90 seconds.
# cann.requires_followup:
#   - The purge window is approved. This becomes the operational pressure for Phase II.
#   - Four pediatric patients in the Sector 11 clinic -- if Phoenix learns about this,
#     it becomes a moral crisis (save the clinic or press the tactical advantage).
#   - Marcus's "other ledgers" -- the personal budget is a vulnerability. If Phoenix
#     discovers it, they can pressure Marcus through institutional channels.
#   - The 14K/22K cost imbalance should surface in a future intelligence scene --
#     Noelle could discover that the regime is spending more to fight Phoenix than
#     Phoenix costs them, which means the war is working.
#   - "We record what is true" as an Echelon motto that mirrors/inverts Phoenix's values.
# cann.runtime_note:
#   - Target: Under 90 seconds reading time. ~550 words.
