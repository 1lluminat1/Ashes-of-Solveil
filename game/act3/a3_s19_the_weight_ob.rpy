# =======================================================
# ACT 3 - Scene 19: The Weight (Obedience Path)
# File: a3_s19_the_weight_ob.rpy
# Path: OB
# Type: PAIR ANCHOR (A3_P13 OB variant: Tessa x Absence)
# Character Focus: Tessa, Aeron (peripheral)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s19_the_weight_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s19_the_weight_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked tripod. Same steadiness as EMP version.
    #         Opens wide on the war room: empty table, empty chairs. The holo-table
    #         on standby -- but this time, the chair at the head is occupied.
    #         No -- not Selene. The chair is empty. ON OB, SELENE IS DEAD.
    #         The emptiness is the shot. The camera holds on the empty chair
    #         for five seconds before finding Tessa.
    #         Aeron: silhouette in the corridor (if apologized) or
    #         a shadow passing the door that doesn't stop (if dismissed).
    #         The camera stays with Tessa regardless. This scene belongs to her.
    # LIGHTING: War room after hours. Same palette as EMP: overhead OFF,
    #           holo-table standby (blue-green), Tessa's lamp (amber).
    #           The difference: the head-of-table position is dark. No one sits there.
    #           In EMP, Selene fills that space with presence. Here, the absence fills it.
    #           The amber lamp is the only warmth. It reaches less far than it should.
    # SFX: Loop -- base night. Same ambient as EMP. Generator hum. Ventilation tick.
    #      One-shots -- paper rustle, pen on paper, chair creak (Tessa's, not the head chair).
    #      The head chair doesn't creak because no one is in it.
    #      If Aeron enters: boot steps in corridor. Pause. Either approach or departure.
    # FX/COMP: War room: same table, same holo-surface. Cleared of tactical data.
    #          Tessa's board: the portable version. Names in her handwriting.
    #          Both columns this time. The living. And the dead.
    #          Two mugs: one Tessa's (chipped). One empty. Set at the head of the table.
    #          No one will drink from it.
    # BLOCKING: Tessa at the corner of the table. Close to the head -- but not in it.
    #           She's pulled close to occupy the space without claiming the chair.
    #           The board spread on the table. Both columns visible.
    #           Aeron: corridor threshold. Watching or passing.
    # CANON: PAIR ANCHOR OB variant. Tessa x Selene's Absence.
    #        ON OB, SELENE IS DEAD. The EMP version is Tessa and Selene alive.
    #        This is Tessa alone with the board. Counting names. Both sides.
    #        The scene inverts the EMP: instead of Selene receiving care, the empty chair does.
    #        Conditional branching: if apologized, Aeron enters. If dismissed, he passes.
    #        Callbacks: EMP s18 (parallel), s10 (tessa_friction), the board methodology.
    # FACE: Tessa -- steady. But the steadiness costs more when no one sees it.
    #        Aeron (if present) -- the mask. What the mask hides: recognition of cost.

    # ========= VOICE BASELINE =========
    # Tessa: Even quieter than usual. She talks to the board. To the names.
    #        Not madness -- methodology. She counts out loud to make the counting real.
    # Aeron (if present): Internal only. Observer. He doesn't speak in this scene.
    #        His athoughts are the only evidence he was there.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - LATE NIGHT]
    # The room that runs the rebellion. Empty of everyone who runs it.
    # Except one.

    #scene bg_war_room_night_ob with dissolve
    #play ambient "sfx/ambient/base_night_quiet.ogg" fadein 2.0

    # ========== PHASE 1 -- THE EMPTY CHAIR ==========

    "The war room after midnight."

    "The overhead strips are off. The holo-table pulses on standby. Blue-green. The machine heartbeat that never stops."

    "The chair at the head of the table is empty."

    "It's been empty since the funeral. Not even Aeron, who sat in it once and never went back. He conducts briefings standing now. He says it's more efficient."

    "Tessa's lamp sits at the table's edge. Amber. The same one she carries. The reach of light falls just short of the head chair."

    "At the corner of the table, pulled close to the head position but not claiming it: Tessa."

    "She has the board."

    # ========== PHASE 2 -- THE COUNT ==========

    "The board is unfolded on the table. Both columns. Tessa's handwriting."

    "The left column: THE LIVING."

    "The right column: THE DEAD."

    "The left column is longer. That's the point. That's always been the point."

    "But the right column has grown since the last time anyone saw it."

    "Tessa's pen moves. She adds a name. Studies it. Moves to the next."

    t "(quiet, to herself) Dren. Living. Workshop detail."

    t "Vasquez family. Living. East wing. The daughter still draws on the walls."

    t "Private Ansel. Living. Night patrol rotation three."

    "She pauses. Moves to the right column."

    t "Selene Ward."

    "She writes the name. The pen doesn't hesitate."

    t "Lieutenant Commander Ito. Sector Eight."

    t "Corporal Yang. Sector Eight."

    t "Private first class-- no. He was promoted posthumously. Sergeant Dinh. Sector Eight."

    "She writes each name with the same careful letters. No difference in pressure between the living and the dead. Each name gets the same attention."

    athought "She counts everyone."

    athought "Even the ones who don't deserve counting."

    # --- CONDITIONAL BRANCH ---

    if flag("tessa_apologized_s10"):
        jump .aeron_enters

    if flag("tessa_dismissed_s10"):
        jump .aeron_passes

    # Default: if neither flag is set, use the dismissal path
    jump .aeron_passes

    # ========== BRANCH: AERON ENTERS (Apologized in s10) ==========
    label .aeron_enters:

        athought "I'm at the corridor entrance. The light under the door."

        athought "Third time this week I've found her here."

        athought "The first two times, I stayed in the corridor. Noelle's instance seven and instance eleven."

        athought "Tonight I open the door."

        "The door opens. Tessa doesn't look up."

        t "Pull up a chair."

        athought "She knew I was there. She always knows."

        "He enters. Takes a chair from the far side of the table. Pulls it to the corner. Beside her. Not across."

        "The board is between them. Both columns visible."

        athought "The dead column has twelve new names since last week."

        athought "The living column has eight."

        athought "The math is moving in the wrong direction."

        "Tessa continues writing. Her pen doesn't stop for his presence."

        t "Seventeen in the right column from Sector Eight alone."

        athought "Sector Eight. Where Nyra's people came from. Where the purge orders were unconscionable."

        t "I got the names from the census records Noelle reconstructed. Most of them don't have next of kin listed."

        t "So I list them here."

        athought "She's giving them a place. A column. A set of careful letters in her handwriting."

        athought "As if penmanship were enough to hold the dead."

        athought "As if anything were."

        "She sets the pen down. Looks at the board. Both columns."

        t "I count them both."

        a "I know."

        t "The living because someone should."

        t "The dead because no one else will."

        "Silence. The holo-table pulses."

        athought "I should say something. Something about Selene's name on the right column. Something about the weight of it."

        athought "I don't."

        athought "Instead, I sit beside her in the amber light and let the silence hold what words can't."

        "He doesn't speak."

        "She doesn't ask him to."

        "The war room holds them. The board between them. The names. Both columns."

        "After a while, Tessa picks up her mug. Sips. Sets it down."

        "She pushes the empty mug -- the one at the head of the table, the one no one drinks from -- half an inch toward the center."

        athought "She adjusts it every night. Half an inch. Keeping the place set."

        athought "For someone who isn't coming."

        "They sit in the amber-and-blue light. Not touching. Not speaking."

        "Sharing the weight. Silently."

        athought "She counts everyone. Both sides."

        athought "I sit beside her and let the count stand."

        athought "That's the most I can give."

        athought "It might be enough."

        jump .scene_close

    # ========== BRANCH: AERON PASSES (Dismissed in s10) ==========
    label .aeron_passes:

        athought "The corridor. Past the war room. Light under the door."

        athought "She's in there. The lamp glow -- amber through the seam."

        athought "I register it."

        athought "I keep walking."

        "His boots pass the door. The sound of them receding."

        "Inside the war room, Tessa's pen pauses. She heard him."

        "She waits. Three seconds. Five."

        "The boots fade."

        "She returns to writing."

        t "(quiet) Private Ansel. Living. Night patrol rotation three."

        "She doesn't look at the door."

        "She's stopped looking at the door."

        athought "Down the corridor, I register the amber light fading behind me."

        athought "I file it under 'operational awareness.'"

        athought "I don't file what it feels like to walk past a lit room at midnight."

        athought "Because I don't feel it."

        athought "Or I do, and the filing system doesn't have a category for it."

        "In the war room, Tessa writes another name."

        "The empty mug at the head of the table sits where she placed it."

        "She counts everyone."

        "Even the ones who walk past."

        jump .scene_close

    # ========== SCENE CLOSE ==========
    label .scene_close:

        "The war room after midnight."

        "The holo-table pulses. The lamp glows. The board lies open."

        "Both columns. The living and the dead."

        "Tessa's handwriting doesn't distinguish between them."

        "Every name gets the same careful letters."

        "Every name gets counted."

        #stop ambient fadeout 3.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "anchor_seen")
        $ npc_remember("Tessa", "counting_both_columns_alone", tone="quiet_endurance")
        $ flag("selene_dead_weight_acknowledged", True)

        if flag("tessa_apologized_s10"):
            $ rel_bump("Tessa", trust=1, affection=1)
            $ npc_remember("Aeron", "sat_with_tessa_at_the_board", tone="silent_solidarity")
            $ flag("weight_shared_ob", True)

        if flag("tessa_dismissed_s10"):
            $ npc_remember("Aeron", "walked_past_tessas_light", tone="registered_not_felt")
            $ flag("weight_unshared_ob", True)

        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s19_the_weight_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same timeline position as EMP s18. Late night. War room. After the deepening arcs.
# cann.what_happened:
#   - OB variant of the Pair Anchor. SELENE IS DEAD on this path.
#   - Tessa alone at the war room table. Counting names. Both columns: living and dead.
#   - The empty chair at the head. No one sits there. Not even Aeron.
#   - Two mugs: Tessa's (chipped) and one at the head (empty, for Selene, never drunk).
#   - Tessa adjusts the empty mug half an inch every night. Keeping the place set.
#   - Conditional branching:
#     APOLOGIZED (s10): Aeron enters. Sits beside her. No words. Shares the weight silently.
#     DISMISSED (s10): Aeron walks past the door. She hears him. He doesn't enter.
#     "She's stopped looking at the door." / "She counts everyone. Even the ones who walk past."
#   - The board has both columns now. The dead column grows. Both get the same handwriting.
# cann.aeron_state:
#   - APOLOGIZED: "I sit beside her and let the count stand. That's the most I can give."
#     Silent solidarity. He doesn't speak. He doesn't need to.
#   - DISMISSED: "I don't file what it feels like to walk past a lit room at midnight."
#     The OB filing system can't categorize the feeling, so it doesn't.
# cann.path_tracking:
#   - Always: flag("selene_dead_weight_acknowledged"), scene_mark("anchor_seen").
#   - Apologized: rel_bump("Tessa", trust=1, affection=1), flag("weight_shared_ob").
#   - Dismissed: flag("weight_unshared_ob"). No rel_bump. The absence of the bump IS the cost.
#   - Tessa's npc_remember fires regardless: "counting_both_columns_alone."
# cann.thematic_flags:
#   - EMP inversion: EMP has Tessa and Selene alive. OB has Tessa and Selene's absence.
#     Same table. Same lamp. Same board methodology. Different second chair.
#   - The empty mug: Tessa sets a place for the dead. Adjusts it nightly.
#     Ritual as grief. The half-inch as devotion.
#   - Both columns, same handwriting: Tessa doesn't distinguish between living and dead
#     in the quality of her attention. Every name gets counted. That's her thesis.
#   - "She counts everyone. Even the ones who don't deserve counting." / "Even the ones who walk past."
#     Two variants of the same line. The second is harsher. Aimed at Aeron.
#   - The empty chair: Aeron sat in it once (a3_s06). Now he stands for briefings.
#     He says it's efficiency. It's avoidance.
# cann.character_moments:
#   - Tessa: Counting aloud. Not madness -- methodology. She makes the count real by speaking it.
#     The pen doesn't hesitate on Selene's name. The same careful letters.
#   - Aeron (apologized): Sits without speaking. The most un-OB thing he does.
#     "It might be enough." The lowest bar he's set, and the most honest.
#   - Aeron (dismissed): Walks past. Registers the light. Keeps walking.
#     "The filing system doesn't have a category for it." -- OB can't process this.
# cann.callbacks:
#   - EMP s18: Parallel structure. Same table, lamp, board. Selene alive vs. dead.
#   - s10: tessa_friction choice. The gate that determines which version plays.
#   - Tessa's board methodology: introduced earlier. Here it expands to include the dead.
#   - a3_s06: Aeron in Selene's chair. Here: the chair empty. He can't go back.
#   - Noelle's instance seven: the 0400 medbay corridor visits. Same pattern.
# cann.block_status:
#   - PAIR ANCHOR (OB). Two variants based on s10 choice. No player choice IN-scene.
#   - The s10 choice echoes forward. This is the payoff for that decision.
# cann.requires_followup:
#   - The empty mug: does it stay? Does someone eventually drink from it?
#   - Tessa's dead column growing: how does this affect her by Act 4?
#   - The apologized path: Aeron sitting silently as recurring pattern. Does it build?
#   - The dismissed path: "She's stopped looking at the door." Has Tessa given up on him?
#   - The board as endgame artifact: does it survive the story? Who inherits it?
