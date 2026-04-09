# =======================================================
# ACT 2 - Scene 24: Echelon Interlude 2 — Compliance Spike
# File: a2_s24_echelon_interlude_2.rpy
# No choices. ~90 seconds. Pressure beat.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s24_echelon_interlude_2"
$ scene_mark(_current_scene_id, "entered")

define analyst = Character("Analyst")
define supervisor = Character("Supervisor")

label a2_s24_echelon_interlude_2:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Locked. 50mm. Flat, institutional framing. No push-ins. No drama. Bureaucracy.
    # LIGHTING: Monochrome dossier frame. Sterile overhead fluorescents. No warmth anywhere.
    # SFX: Air seal hiss. Stamp on paper. Single clock tick underneath everything.
    # UI: Muted serif font. Stamped header: ECHELON // INTERNAL // TIER-2
    # FACE: Never fully shown. Partial profiles. Hands on paper. Voices as function.

    # ========== ECHELON — COMPLIANCE MONITORING DIVISION ==========

    scene black with fade

    # VISUAL: Dossier frame. Monochrome. Institutional. The world seen from inside the machine.
    "ECHELON // INTERNAL // TIER-2"

    pause 0.5

    analyst "Subject RYLAN, Aeron. Cross-reference: Unders communication nodes, patrol incident logs, medical requisitions, supply chain anomalies, recruitment pattern analysis, civilian movement corridors, Ghostline signal traces."

    "Papers shuffling. Quiet. Methodical."

    supervisor "One name across three ledgers is noise."

    analyst "He's across seven."

    supervisor "Seven."

    analyst "Seven independent data streams. All correlating within a fourteen-day window. Comm traffic spikes in sectors where he's been sighted. Medical supply draw patterns consistent with a field clinic scaling beyond triage. Recruitment indicators across four sectors matching exponential growth models."

    "A pause. The clock ticks."

    supervisor "Recommend watchlist elevation?"

    analyst "Recommend immediate asset deployment. This isn't a person hiding. This is a person building."

    supervisor "Denied."

    analyst "Sir—"

    supervisor "Denied. Not because you're wrong. Because elevation triggers protocol and protocol triggers the General."
    supervisor "I want an audit first. Intent hides in neat ledgers. Sloppy rebels leave fingerprints. Organized ones leave architecture."

    analyst "And RYLAN?"

    supervisor "RYLAN is leaving architecture. That means he's not panicking. That means he has support. That means when we do move, we don't poke a network — we collapse it."

    "Stamp. Seal. Filed."

    supervisor "Run the audit. Seventy-two hours. Map everything he's built. Then we take it apart."

    "Clock tick."

    "Air seal."

    "Silence."

    scene black with fade

    # ========== STATE UPDATES ==========

    $ flag("echelon_audit_started", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s24_echelon_interlude_2
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Day 12 of 14-day countdown. Echelon internal. Concurrent with resistance preparations.
#   - E_INT_202 from Doc 38 (Compliance Spike).
# cann.what_happened:
#   - Echelon analyst has cross-referenced Aeron across seven independent data streams.
#   - Supervisor recognizes this isn't a rebel hiding — it's a rebel building.
#   - Immediate elevation denied. 72-hour audit ordered instead — map the network, then collapse it.
#   - "Intent hides in neat ledgers. Organized ones leave architecture."
# cann.aeron_state:
#   - Aeron is not present. This is the enemy's POV.
# cann.path_tracking:
#   - No choices. No empathy impact. Pressure beat only.
#   - flag("echelon_audit_started") for future gating.
# cann.thematic_flags:
#   - Bureaucracy as violence. The dossier frame, the stamps, the clock tick.
#   - "One name across three ledgers is noise. Across seven is intent." — Echelon sees patterns.
#   - The supervisor is competent, not cruel. That's scarier than cruelty.
#   - "We don't poke a network — we collapse it." — the raid won't be a probe. It'll be total.
#   - 72-hour audit = the countdown accelerating. 14 days just became 3.
# cann.character_moments:
#   - Analyst: Methodical. Competent. Doing a good job for the wrong side.
#   - Supervisor: Strategic patience. Denies escalation not from mercy but from thoroughness.
#     "Intent hides in neat ledgers." He understands what Aeron is.
# cann.block_status:
#   - INTERLUDE (both paths). No choices. ~90 seconds. Pressure beat before the raid.
# cann.requires_followup:
#   - 72-hour audit means the raid comes sooner than Noelle's 14-day projection.
#   - The supervisor's "collapse it" doctrine should match how the raid actually deploys.
#   - Aeron should never learn about this specific conversation — it's for the player only.
