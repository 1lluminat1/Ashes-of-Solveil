# =======================================================
# ACT 3 - Scene 18: Field Sync (Obedience Path)
# File: a3_s18_field_sync_ob.rpy
# Path: OB
# Type: BLOODLINE RESONANCE (BR_III_03 OB variant)
# Character Focus: Aeron, Lyra, Zira, Noelle
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s18_field_sync_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s18_field_sync_ob:

    $ show_timeline("DAY 36", "14:00", "Sector 6 — Patrol Route")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28mm, handheld, drift 12-15%. Same combat framing as EMP s10.
    #         The crucial difference: when the sync hits, the camera DOESN'T stabilize.
    #         It tries to. The drift drops to 3-4% but never reaches zero.
    #         The camera WANTS to lock and can't. The instability is the OB texture.
    #         Eight seconds of almost-steady. Almost. Not quite.
    # LIGHTING: Same industrial corridor. Same sodium floods. Same muzzle flash strobe.
    #           During the sync: the light doesn't shift toward warmth. It holds.
    #           Sodium stays sodium. The bands pulse amber but the environment doesn't respond.
    #           The warmth is contained. Internal. Not expressed.
    # SFX: Loop -- firefight. Same combat mix as EMP.
    #      During sync: the mix drops 25% (not 40% like EMP). The world recedes LESS.
    #      The combat doesn't quiet for them. They quiet inside it.
    #      Breathing: two sets. Close but not matched. Phase difference of half a beat.
    #      Band hum: same low frequency. Slightly irregular. Not quite pulse -- stutter.
    #      Post-sync: combat returns full. The transition is harder. Abrupt.
    # FX/COMP: Same industrial corridor. Same engagement. Same team composition.
    #          The bands: amber pulse. But the pulse has a micro-stutter visible in close-up.
    #          Not smooth like EMP. The signal is degraded. Still functional. Not clean.
    # BLOCKING: Same four-person team. Same positions. Aeron point, Lyra flank.
    #           The sync movement happens -- same mirror, same angles.
    #           But the timing is off by a quarter-second. They compensate. It works.
    #           It works like machinery, not music.
    # CANON: BLOODLINE RESONANCE (BR_III_03 OB variant). Same event. Different experience.
    #        OB texture: the sync feels like calibration, not connection. Clinical.
    #        "Efficient. Optimized. The word 'harmony' doesn't apply."
    #        The bands respond. The bodies respond. But the meaning is filtered through OB glass.
    #        Callbacks: EMP s10 (parallel structure), a1_s07 (Balcony), a3_s02 (breathing mismatch).
    # FACE: Aeron -- combat focus. The sync narrows his expression further, not softens it.
    #        Lyra -- the prayer-stillness, but muted. She feels it. She doesn't trust it.
    #        Zira -- watches from overwatch. The unease is deeper than EMP. She sees the stutter.
    #        Noelle -- logs. The data is different from what she expected.

    # ========= VOICE BASELINE =========
    # OB cadence under combat. Short sentences. Tactical-first.
    # Aeron's internal voice during the sync: analytical, not somatic.
    # He processes the event as operational data, not embodied experience.

    # --- VISUAL SETUP ---
    # [EXT/INT. SECTOR 9 - INDUSTRIAL CORRIDOR - NIGHT]
    # Same supply interdiction. Same patrol contact. Different inner experience.

    #scene bg_industrial_corridor_night with dissolve
    #play ambient "sfx/ambient/industrial_corridor_combat.ogg" fadein 1.0

    # ========== PHASE 1 -- CONTACT ==========

    athought "Contact. Three hostiles. Standard formation."

    athought "Weapons free."

    #play sound "sfx/combat/weapons_exchange_suppressed.ogg"

    "The corridor erupts. Suppressed rounds. Ricochet. Sodium light flickering."

    "Zira drops to cover. Tactical feed active."

    z "(radio) Three contacts. Point at junction. Two flankers at the pipe cluster."

    a "(radio) Lyra, flank left. Use the pipe run."

    l "(radio) Moving."

    athought "She moves. The same low-fast combat posture. I track her through peripheral vision."

    athought "I don't need to track her. I know where she'll be."

    athought "That's training. That's repetition. That's operational familiarity."

    athought "That's all it is."

    n "(radio) Point man static. Flankers repositioning. Twelve seconds."

    a "Zira, suppress."

    z "On it."

    "Suppressive fire. The flankers pull back."

    athought "Lyra at the secondary junction. She signals. Ready."

    a "(radio) Hold. I'm drawing point."

    # ========== PHASE 2 -- THE SYNC ==========

    # VISUAL: Aeron breaks cover. Lyra moves simultaneously. No signal.
    # CAMERA: The drift drops. 12% to 4%. Trying to lock. Not quite.
    # The instability is the scene's tell: the bodies want to sync. The path resists.

    athought "I break cover."

    athought "Lyra moves at the same instant."

    athought "No signal. No call."

    "They move. Opposite sides. Mirror angles. His left, her right."

    athought "Our boots hit the deck at almost the same cadence."

    athought "Almost."

    athought "A quarter-beat off. She's slightly ahead. Or I'm slightly behind."

    athought "The difference is milliseconds. It shouldn't register."

    athought "It registers."

    #play sound "sfx/combat/band_hum_low_stutter.ogg"

    "The bands pulse. Both wrists. Low amber."

    "Not smooth. A micro-stutter in the rhythm -- the pulse catches, releases, catches. Like a signal with interference."

    athought "My breathing."

    athought "Four in. Six out."

    athought "She's breathing the same count. But we're not aligned. Half a beat of phase difference."

    athought "The word that applies is 'synchronization.' Not 'resonance.'"

    athought "Calibration. Two instruments tuned to the same frequency but operating independently."

    "The corridor feels tighter. Not thicker -- compressed. The same information in less space. Each sound clipped. Each movement economical."

    athought "My heart rate is steady. Not the combat-elevated normal. Steady."

    athought "That's an anomaly. I note it."

    "Aeron reaches the gantry column. Sights down. The point man is exposed."

    "Lyra reaches the alcove. Clean angle."

    "They fire."

    "Sequentially. His shot drives the target left. Her shot catches the movement."

    athought "One-two."

    athought "Not a phrase. A procedure. Step A, Step B. Operational sequencing."

    athought "The result is identical to -- to what it would be on another path."

    athought "The experience is not."

    "The point man drops. The flankers break. Eight seconds."

    athought "Eight seconds of coordination without signal."

    athought "The band is warm. Warmer than ambient. But not -- not warm the way skin is warm."

    athought "Warm the way circuitry is warm. Functional heat."

    # ========== PHASE 3 -- THE NOTICE ==========

    # VISUAL: Corridor secure. The drift returns to 12%. The almost-lock broken.
    # Zira moving up. Noelle logging. The combat mix returns full -- abrupt cut-back.

    "Corridor clear."

    z "(moving forward) Clean engagement."

    "She pauses. Looks back."

    z "Same thing as the training exercise. You moved together."

    a "Battlefield coordination."

    z "Without comms."

    a "We've trained together. Pattern recognition becomes predictive."

    z "That's a good answer. I almost believe it."

    athought "She doesn't believe it. But she'll accept a tactical explanation because the alternative unsettles her."

    "Noelle at her crystal. Stylus moving rapidly."

    n "(without looking up) Cardiac data during the engagement window."

    n "Your rhythms were proximate. Not synchronized."

    athought "Proximate. Not synchronized."

    athought "She caught the difference."

    n "Variance of one point seven BPM. Within observable range but outside the threshold for entrainment."

    athought "One point seven. Not point-three."

    athought "On the other -- in a different dataset, the variance would be lower."

    athought "Here, the signal is degraded. Close but not locked. The instruments tune but don't couple."

    n "I'm logging it as anomalous but subcritical."

    a "Appropriate classification."

    n "The bands displayed a micro-stutter pattern I haven't observed before. Interference on the carrier signal."

    n "I'll need to cross-reference with the coherence gap data."

    athought "She'll find the same gap. But the edges will be rougher."

    # ========== PHASE 4 -- THE AFTERMATH ==========

    # VISUAL: Team moving through the cleared corridor. Post-combat.
    # Aeron and Lyra at the rear. Same twelve-inch gap.
    # But no eye contact. She doesn't look at him. He doesn't look at her.
    # They walk in step -- almost. The quarter-beat phase difference is visible
    # if you know to look. Zira knows to look.

    "The team moves. Standard post-contact. Zira on point. Noelle logging."

    "Aeron and Lyra at the rear. The gap between them is twelve inches."

    athought "Her hand drifts toward the band. Stops. Returns to her rifle."

    athought "She didn't touch it."

    athought "On another path, she would. She'd rest her fingers there. Acknowledge the moment."

    athought "Here, she leaves it. The band is data, not connection. She felt something and decided not to confirm it."

    athought "Or she felt something and I'm projecting."

    athought "The distinction matters. I don't know which side it falls on."

    "They walk in step. Almost."

    athought "My breathing has returned to normal. Her rhythm is beside mine, not inside it."

    athought "The band is cooling. Functional heat dissipating."

    athought "Eight seconds of coordination that I'll log as operational efficiency."

    athought "Because that's what it was."

    athought "Steady."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ metric("resonance_buff", set_to="steady")
    $ metric("resonance_events", delta=1)
    $ scene_mark(_current_scene_id, "anchor_seen")
    $ npc_remember("Lyra", "field_sync_ob_didnt_touch_band", tone="withheld_recognition")
    $ npc_remember("Zira", "witnessed_aeron_lyra_sync_ob", tone="tactical_unease_deeper")
    $ npc_remember("Noelle", "cardiac_variance_1_7_bpm_ob", tone="logging_subcritical")
    $ npc_remember("Aeron", "breathing_proximate_not_synced", tone="clinical_notation")
    $ flag("field_sync_occurred", True)
    $ flag("resonance_buff_active", True)
    $ flag("ob_sync_degraded", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s18_field_sync_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same timeline position as EMP s10. Supply interdiction. Sector 9.
#   - The same event, experienced through OB glass.
# cann.what_happened:
#   - Same firefight, same patrol, same team.
#   - The sync occurs -- but degraded. Quarter-beat phase difference.
#   - Camera drift drops to 3-4% but never reaches zero (EMP: reaches zero).
#   - Combat mix drops 25% (EMP: 40%). The world recedes less.
#   - Band pulse has micro-stutter (EMP: smooth). Interference on carrier signal.
#   - Cardiac variance: 1.7 BPM (EMP: 0.3 BPM). Proximate, not synchronized.
#   - Noelle classifies as "anomalous but subcritical" (EMP: full anomalous flag).
#   - Aftermath: Lyra reaches for band, stops, returns to rifle. Doesn't confirm.
#   - "Efficient. Optimized. The word 'harmony' doesn't apply."
#   - No player choices. The event IS the data.
# cann.aeron_state:
#   - OB processing. The sync is operational data, not embodied experience.
#   - "Calibration, not connection. Two instruments tuned independently."
#   - He NOTES the anomaly (steady heart rate, band warmth) but files it tactically.
#   - "Warm the way circuitry is warm. Functional heat."
# cann.path_tracking:
#   - metric("resonance_buff", set_to="steady") -- same mechanical effect as EMP.
#   - metric("resonance_events", delta=1) -- event counts the same regardless of path.
#   - flag("ob_sync_degraded") -- tracks that the OB variant is rougher.
#   - The buff applies mechanically but the experience is diminished.
# cann.thematic_flags:
#   - EMP parallel degraded: every metric is worse. 0.3 becomes 1.7. Zero drift becomes 4%.
#     Smooth pulse becomes stutter. The data tells the path story.
#   - "A procedure, not a phrase" vs. EMP's "a phrase, not a word." Language downgrade.
#   - The camera wanting to lock: the BODY wants to sync. The PATH resists.
#     OB as resistance to connection, experienced somatically.
#   - Lyra not touching the band: the withheld gesture. On EMP she reaches. Here she doesn't.
#     Both paths, the resonance occurs. Only one acknowledges it.
#   - "Functional heat" vs. EMP's "the temperature of another person's skin."
#     The same warmth, named differently. OB names it as machinery.
# cann.character_moments:
#   - Aeron: "The word 'harmony' doesn't apply." Correct. But the correction is defensive.
#   - Lyra: Reaches for band, stops. The most important gesture in the scene is the one not made.
#   - Zira: "That's a good answer. I almost believe it." She knows. She accepts the lie.
#   - Noelle: "Anomalous but subcritical." The classification IS the OB lens.
# cann.block_status:
#   - BLOODLINE RESONANCE (BR_III_03 OB). No branching. Event scene.
# cann.requires_followup:
#   - The degraded signal: does the stutter resolve in later resonance events, or worsen?
#   - Noelle's cross-reference: the coherence gap + the 1.7 BPM variance. What pattern emerges?
#   - Lyra's withheld gesture: does she ever touch the band on OB? That's the arc marker.
#   - The resonance buff applies mechanically: the GAME treats it the same. The STORY doesn't.
#     This dissonance between mechanic and narrative is intentional.
#   - Zira's deeper unease: she accepted "battlefield coordination" but she's filing it.
