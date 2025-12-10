# =======================================================
# ACT 2 - Scene 13: Echelon Interlude — Damage Control
# File: act2_13_echelon_interlude_1.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_13_echelon_interlude_1"
$ scene_mark(_current_scene_id, "entered")

label act2_13_echelon_interlude_1:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Cold, clinical framing. Wide shot of command room, then slow push-in on Marcus. His face always partially shadowed.
    # LIGHTING: Blue-white sterile light. Holographic displays casting cold glow. Marcus's insignia catching the light.
    # SFX: Loop — low hum of command systems, distant data processing. One-shots — report chime, Marcus's boots on polished floor.
    # FX/COMP: Holographic tactical display showing depot location, highlighted security breach points. Aeron's file photo.
    # BLOCKING/PROPS: Military Division command room. Central holo-table. Marcus alone, officer waiting at the door.
    # FACE: Marcus controlled, cold, but something underneath—pride? Rage? Both?
    # NOTE: This scene should run under 90 seconds. Tight, punchy, menacing.

    # ========== MILITARY DIVISION COMMAND — AERIES ==========

    # VISUAL: Sterile command room. Blue-white light. Marcus Rylan standing at a holo-table, back to camera.
    scene black with fade
    centered "{size=+10}— AERIES —{/size}"
    centered "{size=+5}Military Division Command{/size}"
    pause 1.5

    "General Marcus Rylan studies the report in silence."

    "The holographic display shows a supply depot in Sector 4. Breach points highlighted in red. Inventory losses catalogued in precise columns."

    "Medical supplies. Rations. Communication equipment."

    "Gone."

    # VISUAL: Marcus turns. His face half-lit, half-shadowed. The insignia on his collar catching the light.
    m "The security protocols."

    officer "(at the door) Standard response, General. The breach exploited maintenance access points and—"

    m "I designed those protocols."

    "Silence."

    m "I supervised their implementation. I signed off on the patrol variance patterns."

    officer "Sir?"

    m "Someone knew where every trap was. Someone knew the thirty-second variance. The eleven-minute rotation overlap."

    "He pulls up another file. A face appears on the display."

    "His son's face."

    m "There's only one person alive who knew all of that."

    # VISUAL: Marcus staring at Aeron's file photo. The family resemblance unmistakable.
    "The officer shifts uncomfortably. Everyone knows about the General's son. No one talks about it."

    m "He's not hiding anymore. He's operating."
    m "With the resistance. Using everything I taught him."

    officer "Should I increase patrols in the lower sectors?"

    m "No."

    "Marcus closes the file. Aeron's face disappears."

    m "He'll expect increased patrols. He'll have planned for them."
    m "My son doesn't make the same mistake twice."

    "He turns to face the officer directly. His eyes are cold. Controlled."

    m "Expand surveillance on known resistance contacts. Quietly."
    m "When he surfaces again—and he will—I want to know where, when, and who he's working with."

    officer "And when we find him, sir?"

    "A pause. Something flickers across Marcus's face—too fast to read."

    m "Then we bring him home."

    "The words sound like mercy. They feel like threat."

    m "Dismissed."

    "The officer leaves. Marcus stands alone in the cold light."

    "He looks at the display one more time. The depot. The breach. His own work, dismantled by his own blood."

    m "(quiet, to himself) You've learned well, Aeron."
    m "But you haven't learned everything."

    "The display goes dark."

    "In the Aeries, General Marcus Rylan begins to plan."

    "In the Unders, his son has no idea the hunt just became personal."

    # --- SCENE WRAP ---
    $ scene_mark(_current_scene_id, "marcus_aware")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_13_echelon_interlude_1
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after the depot raid (Day 7). Parallel to resistance debrief.
# cann.what_happened:
#   - Marcus reviews the depot breach report.
#   - He immediately recognizes the signature—only Aeron knew all the security traps.
#   - He orders quiet surveillance expansion rather than obvious patrol increases.
#   - "When he surfaces again, I want to know where, when, and who he's working with."
#   - "Then we bring him home." — Mercy that sounds like threat.
#   - Marcus alone: "You've learned well, Aeron. But you haven't learned everything."
# cann.aeron_state:
#   - Not present. This is Marcus POV.
# cann.path_tracking:
#   - No player choices. Interlude scene.
#   - `marcus_aware` flag set — Echelon now actively hunting with new intel.
# cann.thematic_flags:
#   - Father vs son dynamic—Marcus recognizing Aeron's work with pride and threat.
#   - "Bring him home" as ominous promise.
#   - The hunt becoming personal, not just institutional.
#   - Marcus's tactical mind—won't make obvious moves Aeron would expect.
# cann.character_moments:
#   - Marcus: Controlled, cold, but something underneath. Pride in his son's competence.
#   - "My son doesn't make the same mistake twice" — respect wrapped in menace.
#   - The quiet moment alone shows he's not purely mechanical—there's something personal here.
# cann.worldbuilding:
#   - Military Division Command in the Aeries.
#   - Marcus's authority and reputation—everyone knows about the son, no one talks about it.
# cann.block_status:
#   - Echelon Interlude #1 complete. Stakes raised.
# cann.requires_followup:
#   - Surveillance expansion will affect future operations.
#   - Marcus's "quiet" approach means danger comes unexpectedly.
#   - The "bring him home" line should echo in later confrontations.
#   - Echelon Interlude #2 (later in Act 2) will show escalation.
# cann.runtime_note:
#   - Target: Under 90 seconds reading time. ~400 words.
