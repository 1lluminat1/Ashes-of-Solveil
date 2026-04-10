# =======================================================
# ACT 3 - Scene 09: Echelon Interlude 3 -- Asset Assessment (Obedience Path)
# File: a3_s09_echelon_interlude_3_ob.rpy
# Type: INTERLUDE (E_INT_203 OB variant)
# No choices. ~90 seconds. Dossier frame. Monochrome. Institutional.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s09_echelon_interlude_3_ob"
$ scene_mark(_current_scene_id, "entered")

define analyst = Character("Analyst")
define supervisor = Character("Supervisor")

label a3_s09_echelon_interlude_3_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Locked. 50mm. Flat institutional framing. No push-ins.
    #         Wide on the analysis desk -- two terminals, a shared display, dossier folders.
    #         Hands only. Partial profiles. The analyst's pen. The supervisor's coffee cup.
    #         Final shot: the dossier stamp. MONITOR -- not ELIMINATE.
    # LIGHTING: Monochrome dossier frame. Fluorescents. The same dead light as E_INT_203 EMP.
    #           No warmth. No shadow play. Everything evenly, mercilessly lit.
    # SFX: Terminal keys. Coffee cup set down. Paper turning. A pen circling something.
    #      Clock tick underneath everything. Air seal at open and close.
    #      No music. No ambiance beyond machinery.
    # UI: Muted serif font. Stamped header: ECHELON // INTERNAL // TIER-3
    # FACE: Never fully shown. Hands. Paper. Terminal glow on partial profiles.

    # ========== ECHELON -- BEHAVIORAL ANALYSIS DIVISION ==========

    scene black with fade

    # VISUAL: Dossier frame. Monochrome. The world as taxonomy.
    "ECHELON // INTERNAL // TIER-3"

    pause 0.5

    analyst "Subject review. Phoenix Actual, designate Rylan, Aeron. Post-incident behavioral profile update."

    "A folder opens. Pages turn. The analyst's pen hovers over a paragraph."

    supervisor "Summarize."

    analyst "Sector Four supply depot. Neutralized in under ninety seconds. Fourteen personnel. Zero resistance casualties."

    "The pen circles a number."

    analyst "The operation was textbook. Our textbook. Formation geometry, suppressive fire angles, breach sequencing -- all consistent with Order Division field doctrine, revision three."

    supervisor "He has Order Division assets."

    analyst "Confirmed. We've identified the defection group. Lieutenant Vale's unit. Seventeen personnel, absent from roster since the Sector Eight incident."

    "Coffee cup set down. A single tap against the desk."

    supervisor "Vale. She killed Major Chen."

    analyst "She executed Major Chen. Her after-action report -- filed internally before she left -- cited doctrinal violation. She followed procedure to the letter. The execution was technically within standing orders for officer misconduct during active purge operations."

    supervisor "That's a generous reading."

    analyst "It's the accurate reading. Sir."

    "Clock tick. Three beats."

    supervisor "Continue."

    analyst "Rylan's operational pattern has changed since Vale's integration. Previous Phoenix operations showed adaptive creativity but inconsistent discipline. Supply raids with improvised tactics. Effective but inefficient."

    analyst "Post-integration: structured. Predictable in the way that competence is predictable. He's not improvising anymore. He's executing doctrine."

    "A page turns."

    analyst "Our doctrine."

    "Silence. The fluorescents hum."

    supervisor "Assessment?"

    analyst "He's not rebelling. He's competing."

    "The word settles into the room. The supervisor's hand moves to the terminal. A single keystroke pulls up a comparison chart."

    supervisor "Elaborate."

    analyst "Traditional rebellion: asymmetric. Disruptive. Ideological. They attack what they hate."

    analyst "Rylan's current pattern: symmetric. Structural. Doctrinal. He's building what we build. Running operations the way we run operations. His command hierarchy mirrors ours."

    analyst "He isn't trying to destroy Echelon. He's trying to replace it."

    "The pen taps twice. Precise."

    supervisor "That makes him more dangerous than a rebel."

    analyst "Or more useful."

    "Clock tick."

    supervisor "Explain."

    analyst "A rebel has to be eliminated. An ideologue has to be crushed. But a competitor..."

    analyst "A competitor can be acquired."

    "The supervisor's hand moves to the dossier cover. Turns it to the recommendation page."

    supervisor "You're suggesting recruitment?"

    analyst "I'm suggesting we let him prove the concept. He's building a command structure with our methodology, testing it against our forces, refining it in real-time combat conditions."

    analyst "If he succeeds, we absorb the results. His innovations. His personnel. His infrastructure."

    analyst "If he fails, the problem resolves itself."

    "The pen moves. The recommendation box."

    supervisor "And Vale?"

    analyst "Vale is the mechanism. She's the one translating Echelon doctrine into Phoenix operations. Without her, Rylan reverts to improvisation."

    analyst "Recommendation: do not target Vale independently. She's more valuable as a vector than as a casualty."

    "Silence."

    "The supervisor picks up the stamp. Not the brass seal of the Resource Allocation Division. This one is smaller. Steel. The Behavioral Analysis insignia -- an eye bisected by a horizontal line."

    supervisor "Classification?"

    analyst "Monitor. He's building what we build. Let him prove the concept, then absorb."

    "Stamp."

    "The dossier closes."

    "The terminal logs the entry. Two keystrokes."

    "Air seal. The door closes."

    "The room is empty. The fluorescents hum. The clock ticks."

    "On the desk, the closed dossier. On the cover, in careful institutional script:"

    "RYLAN, AERON -- PHOENIX ACTUAL"

    "And below, in red ink, the stamp:"

    "MONITOR."

    "The fluorescents hum."

    "The clock ticks."

    scene black with fade

    # ========== STATE UPDATES ==========

    $ flag("echelon_ob_assessment", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s09_echelon_interlude_3_ob
# cann.chapter: Act III, Phase I -- Consolidation (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Concurrent with post-Sector 4 strike. Echelon analyzing the operation.
#   - E_INT_203 OB variant. Mirror of the EMP "Purge Calculus" interlude.
# cann.what_happened:
#   - Echelon Behavioral Analysis reviews Aeron's post-Nyra operational pattern.
#   - They identify Order Division doctrine in Phoenix operations. Vale's unit confirmed.
#   - Key assessment: "He's not rebelling. He's competing."
#   - Aeron is building what Echelon builds. Symmetric, structural, doctrinal.
#   - Recommendation: MONITOR, not ELIMINATE. Let him prove the concept, then absorb.
#   - Vale identified as the mechanism -- "more valuable as a vector than a casualty."
#   - This is SCARIER than the EMP version: Echelon sees Aeron as a potential asset.
# cann.aeron_state:
#   - Aeron not present. Enemy POV. Player-only information.
# cann.path_tracking:
#   - No choices. Interlude only.
#   - flag("echelon_ob_assessment") for future gating.
# cann.thematic_flags:
#   - "He's not rebelling. He's competing." -- the OB path's horror in one sentence.
#   - Echelon sees Aeron as recruitable, not eliminable. The regime considers him an asset.
#   - "Let him prove the concept, then absorb." -- Aeron as R&D for his own enemy.
#   - Vale as "vector" -- she's translating Echelon into Phoenix. Unwittingly (or not)
#     she's making the rebellion more like the thing it opposes.
#   - The analyst's precision mirrors Aeron's own. Same language. Same method.
#   - MONITOR vs ELIMINATE: the dossier stamp as thematic mirror of the EMP version's
#     PURGE WINDOW: APPROVED. Different conclusions. Both institutional. Both cold.
#   - "A competitor can be acquired." -- the regime doesn't fear Aeron. It wants him.
# cann.character_moments:
#   - Analyst: Competent. Precise. Sees the pattern. "He's not rebelling. He's competing."
#     The clinical admiration is worse than hostility.
#   - Supervisor: Cautious but persuadable. "That makes him more dangerous than a rebel."
#     Then: considers the acquisition angle. Pragmatism over ideology.
#   - Vale (discussed): "The mechanism." More valuable alive than dead.
#     Her doctrinal translation identified as the operational shift.
# cann.block_status:
#   - INTERLUDE (E_INT_203 OB). OB path only. No choices. ~90 seconds.
# cann.requires_followup:
#   - The MONITOR classification means Echelon will observe, not strike --
#     until Aeron proves too dangerous to absorb. That threshold is Phase II.
#   - If Noelle intercepts this assessment, it becomes a crisis:
#     the rebellion learning that Echelon sees them as a subsidiary, not a threat.
#   - Vale as "vector" -- if Zira discovers this framing, it validates every suspicion.
#   - The absorption plan: "Let him build, then take it." This is the OB endgame
#     threat -- Aeron wins the war but loses the rebellion to the thing he fought.
# cann.runtime_note:
#   - Target: Under 90 seconds reading time. ~520 words.
