# =======================================================
# ACT 3 - Scene 10: Field Sync (Empathy Path)
# File: a3_s10_field_sync_emp.rpy
# Type: BLOODLINE RESONANCE (BR_III_03 -- Field Sync)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s10_field_sync_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s10_field_sync_emp:

    $ show_timeline("DAY 29", "15:00", "Sector 6 — Patrol Route")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28mm, handheld, high drift (12-15%). Combat framing. Opens wide and chaotic --
    #         muzzle flashes, dust, movement. When the sync moment hits: the camera stabilizes.
    #         Not slow motion. Not cinematic grace. The drift drops to zero. Locked.
    #         For eight seconds, the camera is as steady as their breathing.
    #         Then the drift returns, and the moment is over.
    # LIGHTING: Nighttime industrial corridor. Harsh sodium floods from overhead gantries.
    #           Muzzle flash: white-blue strobe. Cover positions in deep shadow.
    #           During the sync: the sodium light doesn't change, but it feels different.
    #           Warmer. As if the temperature of the light shifted while the color didn't.
    #           Bands: low amber pulse. Not spike -- pulse. Slow. In time with each other.
    # SFX: Loop -- firefight: suppressed weapons, ricochet, boot scrape, radio static.
    #      During sync: the combat mix drops 40%. Not silence -- the world receding.
    #      Breathing becomes the loudest sound. Two sets. Matched.
    #      Band hum: low frequency. Felt more than heard.
    #      Post-sync: combat mix returns full. The world crashes back.
    # FX/COMP: Industrial corridor -- pipes, gantries, metal walkways. Echelon patrol caught mid-route.
    #          Muzzle flash illumination. Dust motes frozen in strobe light.
    #          Bands on both wrists: amber pulse visible in low light. Synchronized.
    # BLOCKING: Four-person team: Aeron (point), Lyra (flank), Zira (overwatch/tech), Noelle (intel/rear).
    #           Industrial corridor provides natural cover: pipe clusters, junction boxes, gantry supports.
    #           The sync happens mid-movement: Aeron and Lyra moving between cover positions.
    # CANON: BLOODLINE RESONANCE (BR_III_03). Not romantic. Somatic.
    #        The bands respond to lineage proximity during stress. This is the first time
    #        it manifests as physical synchronization rather than thermal/emotional feedback.
    #        Callbacks: a1_s07 (Balcony -- first band reaction), a2_s07 (Quiet Night -- Lyra's
    #        resonance training), a3_s08 (Unmeasurable -- Noelle's coherence gap).
    # FACE: Aeron -- combat focus narrowing to something quieter. Not peace -- alignment.
    #        Lyra -- the same stillness she has in prayer, transplanted to a firefight.
    #        Zira -- the observer. What she sees on her tactical feed unsettles her.
    #        Noelle -- logging. Always logging. But the data is strange.

    # ========= VOICE BASELINE =========
    # EMP cadence under combat compression. Short sentences. Sensory-first.
    # Aeron's internal voice is tactical, then shifts to somatic during the sync.
    # Post-sync: he doesn't explain it. He sits with it.

    # --- VISUAL SETUP ---
    # [EXT/INT. SECTOR 9 - INDUSTRIAL CORRIDOR - NIGHT]
    # A supply interdiction run. Four-person team. Aeron on point.
    # They hit an Echelon patrol at the junction. Not planned. Not avoidable.

    #scene bg_industrial_corridor_night with dissolve
    #play ambient "sfx/ambient/industrial_corridor_combat.ogg" fadein 1.0

    # ========== PHASE 1 -- CONTACT ==========

    athought "Contact."

    athought "Three hostiles at the junction. Standard patrol formation. They see us the same instant we see them."

    #play sound "sfx/combat/weapons_exchange_suppressed.ogg"

    "The corridor erupts. Suppressed rounds crack against pipe housings. Sodium light flickers as a shot clips a gantry fixture."

    "Zira drops behind a cable junction. Her tactical feed is already active -- green overlay on the corridor, hostile positions pulsing red."

    z "(radio) Three contacts. Standard formation. Point man at the junction, two flankers at the pipe cluster. Thirty meters."

    a "(radio) Copy. Lyra, flank left. Pipe run gives you cover to the secondary junction."

    l "(radio) Moving."

    athought "She moves. Low, fast, the rifle tucked against her shoulder. The corridor casts her in stripes of sodium and shadow."

    "Noelle holds at the rear. Her crystal is active -- logging engagement data, mapping the hostile movement patterns in real time."

    n "(radio) Point man is static. Flankers are repositioning. Fourteen seconds until they reach the alcove."

    a "Zira, suppressive on the flankers. Buy her time."

    z "On it."

    "Zira's shots crack down the corridor. Precise. The flankers pull back behind the pipe cluster."

    athought "Lyra reaches the secondary junction. She's behind them now. Good angle. She signals -- two fingers, then a fist. Ready."

    a "(radio) Lyra, hold. I'm moving up to draw the point man."

    l "(radio) Copy."

    # ========== PHASE 2 -- THE SYNC ==========

    # VISUAL: Aeron breaks cover. Moves to the next position -- a gantry support column.
    # Lyra moves simultaneously from the secondary junction. They're on opposite sides of the corridor.
    # CAMERA: The handheld drift drops to zero. Locked. Steady.

    athought "I break cover. Move to the gantry column. Three seconds of exposure."

    athought "Lyra moves at the same instant."

    athought "I didn't signal. She didn't wait for one."

    "They move. Opposite sides of the corridor, mirror angles, same pace. Aeron left, Lyra right. Their boots hit the deck at the same cadence."

    athought "My breathing."

    athought "Four in. Six out."

    athought "Her rhythm. Not mine."

    athought "When did it change?"

    #play sound "sfx/combat/band_hum_low.ogg"

    "The bands pulse. Both of them. Low amber, visible at the wrist where the sleeve rides up."

    "Not a spike. Not the sharp thermal flare he's felt before. A pulse. Slow. Warm. Synchronized."

    athought "The corridor feels thicker. Not slower -- nothing slows down. The rounds are still cracking. Zira's suppressive fire is still hammering the pipe cluster."

    athought "But the space between each sound has weight. Each heartbeat is a room I can stand in."

    "Aeron reaches the gantry column. Sights down the corridor. The point man is exposed."

    "Lyra reaches the alcove. Her angle is clean."

    "They fire."

    "Not simultaneously -- that would be coincidence. Sequentially. Aeron's shot drives the point man left. Lyra's shot catches the movement. One-two. A phrase, not a word."

    athought "I didn't tell her to time it that way."

    athought "She didn't tell me."

    "The point man drops. The flankers break. Zira's suppressive fire herds them into the open."

    "Eight seconds. From the moment they moved to the moment the corridor was clear. Eight seconds of coordination that had no signal, no call, no plan."

    athought "My heart rate is steady. Not combat-elevated. Steady."

    athought "That's wrong. That's not how adrenaline works."

    athought "The band is warm on my wrist. Not hot. Warm. The temperature of another person's skin."

    # ========== PHASE 3 -- THE NOTICE ==========

    # VISUAL: Corridor secure. Zira moving up. Noelle at her crystal. The combat mix returns.
    # CAMERA: Drift resumes. Handheld. The steadiness is gone. It was only eight seconds.

    "Corridor clear. Zira advances, checking the downed patrol. Noelle is at the wall, crystal active, logging."

    z "(moving forward, checking corners) That was clean."

    "She pauses. Looks back at Aeron and Lyra."

    z "That was very clean."

    athought "The way she says it. Not a compliment. An observation."

    z "You two moved at the same time. No signal. I was on overwatch -- I would have heard the call."

    a "Battlefield read. She had the angle."

    z "You didn't look at her. You moved before she was in position. And she was in position anyway."

    "Zira studies them. The tactical assessment running behind her eyes."

    z "Eight seconds. I clocked it on the feed. You moved like you were one unit."

    athought "Zira doesn't do mysticism. She does pattern recognition."

    athought "And the pattern she just saw doesn't fit her models."

    "Noelle is quieter. Her stylus is moving across the crystal. The strokes are small, rapid."

    n "(without looking up) Synchronized heartbeat data during the engagement window. Both subjects."

    n "The variance between your cardiac rhythms during those eight seconds was less than point-three BPM."

    athought "Point-three."

    athought "That's not entrainment. Entrainment takes minutes. This happened in a firefight."

    n "I'm flagging this as anomalous."

    athought "She's using her clinical voice. The one that means the data scares her."

    n "Cross-referencing with the coherence gap from last week's readings."

    athought "The Unmeasurable. She's already connecting the threads."

    # ========== PHASE 4 -- THE AFTERMATH ==========

    # VISUAL: The team moving through the cleared corridor. Post-combat economy.
    # Aeron and Lyra fall into step at the rear. Neither speaks.
    # CAMERA: Medium two-shot from behind. Their pace is matched. Their bands are dimming.

    "The team moves. Standard post-contact procedure -- clear, verify, extract. Zira on point now. Noelle logging as she walks."

    "Aeron and Lyra fall into step at the rear. The gap between them is twelve inches."

    athought "My breathing is still four in, six out. It doesn't feel borrowed anymore."

    athought "It feels like mine."

    athought "Except it isn't. Or it is. Both."

    "Lyra's left hand drifts to her band. Fingers resting on the surface. The amber glow has faded to nothing."

    "She looks at Aeron."

    "He looks back."

    "Neither speaks."

    athought "There's nothing to say about it. Not because it's unspeakable — because it's pre-verbal."

    athought "The bands know something our mouths don't."

    athought "In the Order, she'd have a word for this. Resonance, maybe. Alignment. Something from the old liturgy that describes two frequencies finding each other without trying."

    athought "I don't have a word from the Glass Academy. The Glass Academy didn't train for this."

    athought "The Glass Academy trained for control. This wasn't control."

    athought "This was the opposite. And it worked better."

    "Lyra's fingers lift from the band. She turns back to the corridor. Her rifle is up. Her posture is operational."

    "Whatever happened, she's already carrying it without holding it."

    athought "I'll do the same."

    athought "Steady."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ metric("resonance_buff", set_to="steady")
    $ metric("resonance_events", delta=1)
    $ scene_mark(_current_scene_id, "anchor_seen")
    $ npc_remember("Lyra", "field_sync_eight_seconds", tone="unspoken_recognition")
    $ npc_remember("Zira", "witnessed_aeron_lyra_sync", tone="tactical_unease")
    $ npc_remember("Noelle", "cardiac_sync_point_three_bpm", tone="clinical_alarm")
    $ npc_remember("Aeron", "breathing_matched_lyra_in_combat", tone="somatic_wonder")
    $ flag("field_sync_occurred", True)
    $ flag("resonance_buff_active", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s10_field_sync_emp
# cann.chapter: Act III, Phase II -- Deepening (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase II. After the base has been rebuilt/hardened.
#   - During a supply interdiction run in Sector 9.
#   - The first combat operation since Echelon Strikes Back.
# cann.what_happened:
#   - Four-person team (Aeron, Lyra, Zira, Noelle) hits an Echelon patrol during a supply run.
#   - Standard firefight. Aeron on point, Lyra flanking, Zira on overwatch, Noelle on intel.
#   - Mid-combat: Aeron and Lyra move simultaneously without signal or communication.
#     Eight seconds of perfect coordination. Their breathing matches (4 in / 6 out).
#     Bands pulse amber. Low. Synchronized.
#   - The corridor feels "thicker, not slower." Heart rates steady, not elevated.
#   - They fire sequentially -- Aeron drives the target, Lyra catches the movement. A phrase.
#   - Zira notices from overwatch: "You moved like you were one unit." No signal given.
#   - Noelle logs cardiac sync: variance under 0.3 BPM during the eight-second window.
#     Cross-references with the coherence gap from a3_s08 (The Unmeasurable).
#   - Aftermath: Aeron and Lyra walk in step. She touches her band. They look at each other.
#     Neither speaks. The moment is pre-verbal.
# cann.aeron_state:
#   - Combat focus narrowing to somatic awareness. His breathing matched hers involuntarily.
#   - "This wasn't control. This was the opposite. And it worked better."
#   - Post-sync: carries it without holding it. Steady.
# cann.path_tracking:
#   - EMP baseline. No player choices. Bloodline resonance event.
#   - metric("resonance_buff", set_to="steady") -- future scenes reference this as a
#     slightly larger timing window on crucial choices. Subtle mechanical advantage.
#   - metric("resonance_events", delta=1) -- tracking total resonance events for endgame calc.
#   - flag("field_sync_occurred"), flag("resonance_buff_active") for callbacks.
#   - npc_remember for all four team members -- each processes differently.
# cann.thematic_flags:
#   - NOT romantic. Somatic. The intimacy is physical synchronization, not emotional declaration.
#   - "Thicker, not slower" -- time gains weight, not duration. A sensory distinction.
#   - "A phrase, not a word" -- their coordinated fire is linguistic. Communication without signal.
#   - The bands as somatic interface: temperature, pulse, rhythm. Not display data. Felt data.
#   - Glass Academy trained control. This is the opposite. "And it worked better."
#   - "Pre-verbal" -- the moment exists before language. Words would reduce it.
#   - Mirror of a3_s08 (Unmeasurable): Noelle's instruments detect the sync. The data is real.
#     But the experience outstrips the measurement.
#   - The camera stability during sync: the drift dropping to zero IS the sync, visually.
# cann.character_moments:
#   - Aeron: Discovers his breathing matched hers. Doesn't force an interpretation.
#     "I'll do the same." -- acceptance without analysis.
#   - Lyra: Touches her band. Looks at him. Turns back to the corridor.
#     She carries it without holding it. Two hundred years of Order discipline in one gesture.
#   - Zira: "You moved like you were one unit." -- tactical observer, not mystic.
#     The pattern doesn't fit her models. That unease is important.
#   - Noelle: 0.3 BPM variance. Cross-referencing with the Unmeasurable.
#     She's building a dataset on something she can't explain.
# cann.block_status:
#   - BLOODLINE RESONANCE (BR_III_03). Phase II. No branching.
# cann.requires_followup:
#   - resonance_buff ("steady") should manifest as a mechanical advantage in a future choice scene.
#     Slightly larger timing window, or an additional option available only if buff is active.
#   - Noelle's cross-reference with the coherence gap: she should have a scene where she
#     presents her findings to the group. The data says something impossible.
#   - Zira's "tactical unease" -- she'll want an explanation. She doesn't do mystery.
#     This could become a Zira tension point if the resonance events increase.
#   - The 0.3 BPM sync is physiologically extraordinary. If Tessa learns about it,
#     she'll have medical questions.
#   - The sequential fire pattern ("a phrase, not a word") should be referenced in the
#     next combat scene. The team knows Aeron and Lyra have something. They don't know what.
#   - Lyra's breathing rhythm (4 in / 6 out) matches the exercise she taught Noelle in s08.
#     This is the same discipline, deployed under fire. The Order training has combat applications.
