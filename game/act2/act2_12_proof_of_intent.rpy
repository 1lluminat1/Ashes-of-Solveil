# =======================================================
# ACT 2 - Scene 12: Proof of Intent
# File: act2_12_proof_of_intent.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_12_proof_of_intent"
$ scene_mark(_current_scene_id, "entered")

label act2_12_proof_of_intent:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Dynamic action coverage. Wide establishing shots of the depot, then tight handheld during infiltration. Aeron's POV for tactical assessment moments.
    # LIGHTING: Night operation—blue-black shadows, harsh security floods creating contrast. Red emergency lighting during complications. Ghostline relay amber glow in darkness.
    # SFX: Loop — industrial hum, distant patrols, comms static. One-shots — boots on metal, security locks cycling, suppressed weapons, alarms.
    # FX/COMP: Security camera feeds (Noelle's overwatch), patrol route overlays on Aeron's relay, timer countdowns.
    # BLOCKING/PROPS: Echelon supply depot exterior/interior, security checkpoints, crates of supplies, patrol drones, three-person ground team.
    # FACE: Aeron in tactical mode—controlled, precise, flashes of doubt when confronting his own design. Team members tense but trusting his lead.

    # ========== STAGING AREA — NIGHT, DAY 6 ==========

    "The staging point is an abandoned maintenance tunnel three hundred meters from the depot's eastern perimeter."

    "Aeron checks his gear for the third time. Force of habit. The motions feel familiar—too familiar."

    if empathy_band() == "obedience":
        athought "Pre-op ritual. Weapons check, comms check, team assessment."
        athought "I've done this a hundred times. Usually from the other side."
    else:
        athought "The last time I geared up for an operation, people died because of my efficiency."
        athought "Tonight, the efficiency has to work the other way."

    # VISUAL: Small team—Aeron, two resistance fighters (Cade and Mira, no relation to the cover names), Zira on comms via Ghostline.
    "The team is small. Selene's choice—minimal footprint, minimal exposure."

    "Cade is older, scarred, silent. Former infrastructure worker who lost his family in Tier 7."

    "Mira is young—maybe twenty—eyes too sharp for her age. She was a courier before Selene promoted her to operations."

    "Neither of them looks at Aeron with trust. Not yet."

    # SFX: Comms crackle—Zira's voice.
    z "(through comms) Ghostline is live. I've got eyes on the eastern approach. Noelle, status?"

    n "(through comms, filtered) Overwatch active. I'm patched into their security feed—sixty-three percent coverage. Blind spots marked on your relay."

    a "Copy. Team, sync your relays."

    "The amber glow of the Ghostline network pulses on his wrist. Zira's gift, now a lifeline."

    z "Patrol pattern shows four-minute windows between sweeps. You'll have to move fast."

    a "The patrol pattern is wrong."

    z "What?"

    a "It's not four minutes. It's three and a half."
    a "I built in a thirty-second variance to catch anyone who thought they'd timed it. The documentation lies."

    n "(through comms) ...Interesting. My data showed four minutes."

    a "Your data came from their official protocols. I wrote unofficial amendments that never made the logs."
    a "There are three other traps like that between here and the supply cache."

    "Silence on the comms. Then:"

    n "You're full of surprises, Captain."

    mira "(the young operative) So you're saying you booby-trapped your own security?"

    a "I was very good at my job."

    cade "(the older one, flat) Let's hope you're better at breaking it."

    # ========== INFILTRATION — PHASE ONE ==========

    # VISUAL: Team moving through shadows toward the depot. Industrial architecture, harsh angles, security floods sweeping.
    "They move."

    "Aeron leads, reading the terrain like a language he invented. Every camera placement, every patrol route—his design, now his obstacle."

    a "(low) Camera three sweeps left in ten seconds. Move on my mark."

    "They press against cold metal. The flood passes. His hand drops."

    a "Mark."

    "Three shadows slip through the gap. Textbook."

    z "(through comms) You're through the outer perimeter. Inner checkpoint in forty meters."

    n "(through comms) Two guards at the checkpoint. Rotating twelve-minute shifts."

    a "The rotation is eleven minutes. Overlap built in for handoff briefings."

    n "You're correcting me a lot tonight, Captain."

    a "I designed this facility to be impenetrable. Correcting you is how we survive."

    if empathy_band() == "obedience":
        athought "Every flaw I find is a flaw I created. Every trap I disarm is a trap I set."
        athought "There's an elegance to it. Dismantling my own architecture."
    else:
        athought "I built this cage. Now I'm picking the lock from inside."
        athought "Every correction is an admission—I was too good at making things unbreakable."

    # VISUAL: Approaching the inner checkpoint. Two guards visible through a dirty window.
    "The checkpoint is a reinforced booth with sightlines covering the main approach. No blind spots."

    "Except one."

    a "(to team) The ventilation shaft on the east wall. Maintenance access."

    cade "That's a two-person fit, max."

    a "It was designed for drone inspection. Human-sized drones."
    a "I argued against it during the design phase. Got overruled by budget constraints."

    mira "You remember a budget argument from two years ago?"

    a "I remember every argument I lost. That's how you learn where the weaknesses are."

    # VISUAL: Team splitting—Cade and Mira through the vent, Aeron providing overwatch.
    "Cade and Mira move to the shaft. Aeron positions himself with sightlines on the guards."

    z "(through comms) Guard rotation in three minutes. You'll have a ninety-second window once they swap."

    a "Eighty-four seconds. The extra six are buffer for conversation."

    z "You're really annoying when you're right, you know that?"

    a "I've been told."

    # ========== COMPLICATION — THE YOUNG GUARD ==========

    # VISUAL: Guard rotation happening. New guard takes position—young, nervous, clearly new to the posting.
    "The rotation happens. One guard leaves, one arrives."

    "The new one is young. Maybe nineteen. His uniform doesn't fit right—too new, too stiff."

    n "(through comms) That's not the scheduled rotation. Different guard than the manifest."

    a "Replacement. Someone called in sick, probably."

    mira "(through vent, whispered) He's right in our exit path. We can't get past without being seen."

    cade "(through vent) I can take him. Quiet."

    "Aeron watches the young guard through his scope. The kid is checking his reflection in the booth glass. Adjusting his collar."

    "Nervous. New. Probably has a family somewhere who's proud he got the posting."

    mira "(through vent) Aeron? Call it."

    # --- PLAYER CHOICE: How does Aeron handle the guard? ---
    menu:
        "The guard is in the way. How does Aeron proceed?"

        "Find another way—no unnecessary casualties.":
            $ choice_and_dev(
                _current_scene_id, "_avoid_guard", "EMP", factor=2,
                note="Aeron chooses to find an alternative route rather than eliminate a young guard."
            )
            $ npc_remember("Cade", "aeron_spared_young_guard", tone="surprised")
            $ npc_remember("Mira", "aeron_spared_young_guard", tone="relieved")
            $ scene_mark(_current_scene_id, "guard_spared")

            a "Hold. I'll find another route."

            cade "(through vent) There is no other route. You said so yourself."

            a "Then I was wrong."

            "He studies the layout. His own design. There has to be something—"

            athought "Emergency drainage. Sub-level access for flooding protocols. I forgot about it because it was never meant to be used."

            a "Southeast corner. There's a drainage grate. It connects to the sub-level maintenance corridor."
            a "Tight fit, but it bypasses the booth entirely."

            mira "(through vent) How do you know it's not sealed?"

            a "Because I marked it as 'non-essential redundancy' in the final inspection. Budget cuts meant it never got secured."
            a "Another argument I lost."

            z "(through comms) That route adds four minutes to your timeline."

            a "Then we move faster."

            cade "(through vent) You're burning time to spare one guard?"

            a "I'm burning time because that guard is nineteen and doesn't know he's standing between us and survival."
            a "Move to the drainage grate. That's an order."

            "A pause. Then:"

            cade "(through vent) ...Copy."

            "They move. The young guard never knows how close he came."

            n "(through comms, quiet) Anomaly confirmed."

        "Authorize the takedown—mission priority.":
            $ choice_and_dev(
                _current_scene_id, "_authorize_takedown", "OB", factor=2,
                note="Aeron authorizes eliminating the guard for mission efficiency."
            )
            $ npc_remember("Cade", "aeron_authorized_kill", tone="respected")
            $ npc_remember("Mira", "aeron_authorized_kill", tone="conflicted")
            $ scene_mark(_current_scene_id, "guard_eliminated")

            a "Do it. Quiet."

            "Cade moves. Fast. Professional."

            "The young guard never sees him coming. One moment he's adjusting his collar; the next, he's on the ground, neck at the wrong angle."

            mira "(through vent, shaky) He's down."

            a "Move. Clock's running."

            if pass_tier("EMP1", "EMP2", "EMP3"):
                athought "He was nineteen. Maybe younger. New uniform, nervous hands."
                athought "Necessary. That's what I'm supposed to think. Necessary."
                athought "The word tastes like ash."
            else:
                athought "Clean. Efficient. One obstacle removed."
                athought "He was in the wrong place at the wrong time. That's all war is."

            z "(through comms, quiet) Target neutralized. Continue to objective."

            n "(through comms) Efficient."

    # ========== SUPPLY CACHE — SUCCESS ==========

    # VISUAL: Team reaching the supply cache. Crates of medical supplies, rations, communication equipment.
    "The supply cache is exactly where he remembered."

    "Crates stacked floor to ceiling. Medical supplies—antibiotics, surgical kits, blood synth. Rations for a hundred people for a month. Communication equipment that could rebuild the Ghostline twice over."

    mira "Holy shit. This is..."

    cade "More than we've scored in six months."

    a "Take what you can carry. Priority on medical, then comms. Rations last."

    "They work fast. Efficient. The training showing through even in the resistance fighters."

    z "(through comms) Patrol approaching from the west. You've got two minutes."

    a "We need three."

    z "Then you better move faster."

    # VISUAL: Loading the last crates. Aeron pauses at a terminal—old data, his old work.
    "As the team loads the last of the supplies, Aeron stops at a terminal in the corner."

    "Old files. Patrol schedules, security updates, operational memos."

    "And there, buried in the archives: his name. His signatures. His work."

    athought "Captain Aeron Rylan. Security assessment, approved. Patrol optimization, approved. Containment protocols, approved."
    athought "I built this. All of it."

    "He pulls the data crystal from the terminal. Evidence. Context. Ammunition."

    a "We're done. Move to extraction."

    # ========== EXTRACTION — CLEAN EXIT ==========

    # VISUAL: Team exfiltrating. Clean, professional, shadows in shadows.
    "The exit is cleaner than it should be."

    "Aeron's knowledge turning every trap into a doorway, every patrol into a gap."

    "By the time they reach the staging tunnel, they're carrying enough supplies to keep the resistance operational for months."

    z "(through comms) All teams clear. No pursuit detected."

    n "(through comms) Echelon won't notice the loss until morning inventory. By then, the trail will be cold."

    mira "(breathing hard) That was... that was actually good.

    cade "(looking at Aeron differently) You know your shit. I'll give you that."

    a "I should. I built the shit."

    # ========== AFTERMATH — WEIGHT OF SUCCESS ==========

    # VISUAL: Team catching their breath in the tunnel. The supplies stacked behind them. Victory, and its cost.
    "They rest in the tunnel. The adrenaline fading. The reality settling."

    if scene_has(_current_scene_id, "guard_spared"):
        mira "(to Aeron, quiet) You didn't have to do that. Find the other route."

        a "Yes, I did."

        mira "The mission would have succeeded either way."

        a "The mission isn't just supplies. It's who we become getting them."
        a "I've killed enough people who didn't deserve it. I'm not adding to the count when there's another way."

        cade "(overhearing) ...You're not what I expected.

        a "What did you expect?"

        cade "Glass. Echelon's butcher. Someone who'd put a bullet in my head if the mission required it."

        a "That person existed. I'm trying to be someone else."

        athought "The young guard is alive because I found a drainage grate I'd forgotten about."
        athought "That's not redemption. But it's something."

    else:
        mira "(to Aeron, quiet) That guard... he was young."

        a "I know."

        mira "Did it have to—"

        a "It was the fastest way. Selene needs to know I can make the hard calls."

        mira "Is that what it was? A hard call?"

        "He doesn't answer. Because he's not sure anymore."

        cade "(overhearing) She's young. She'll learn."

        a "Learn what?"

        cade "That you can't save everyone. Sometimes the mission is all that matters."

        athought "The mission is all that matters. I've said that a hundred times."
        athought "It never tasted this bitter before."

    z "(through comms) Selene's team is moving to intercept the supplies. She wants a debrief in two hours."

    a "Tell her we're on our way."

    "They gather the supplies. Start the long walk back."

    "Tonight, Aeron proved he could break what he built."

    "The question now is whether Selene believes it means anything."

    # --- SCENE WRAP ---
    $ flag_on("Selene", "depot_op_complete")
    $ add_item_counter("medical_supplies", 5)
    $ add_item_counter("rations", 10)
    $ add_item_counter("comms_equipment", 3)
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_12_proof_of_intent
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night of Day 6. The depot raid Selene assigned.
# cann.what_happened:
#   - Team assembled: Aeron (lead), Cade (veteran), Mira (young operative), Zira (comms), Noelle (overwatch).
#   - Aeron corrects everyone's intel with his insider knowledge—patrol timing traps, unofficial amendments.
#   - Infiltration proceeds smoothly until complication: a young replacement guard blocks the exit path.
#   - Core choice: Find another route and spare the guard (EMP) or authorize Cade to eliminate him (OB).
#   - EMP path: Aeron remembers a drainage grate he'd marked as "non-essential"—they bypass, guard lives.
#   - OB path: Cade kills the guard quickly. Aeron processes the necessity with varying levels of discomfort.
#   - Supply cache reached—massive haul of medical supplies, rations, comms equipment.
#   - Aeron pulls a data crystal from the terminal—evidence of his own work, signatures, approvals.
#   - Clean extraction. Team's opinion of Aeron shifts based on his choices.
# cann.aeron_state:
#   - In tactical mode but confronting his past at every step—"I built this."
#   - EMP path: Refuses unnecessary casualties, earns respect differently—"not what I expected."
#   - OB path: Makes the efficient call, but the victory tastes bitter.
# cann.path_tracking:
#   - One `choice_and_dev` decision (factor=2, significant):
#       • `_avoid_guard` → EMP +2 weight, guard_spared flag, team memories positive.
#       • `_authorize_takedown` → OB +2 weight, guard_eliminated flag, team memories mixed.
#   - NPC memories for Cade and Mira stored via `npc_remember()`.
#   - Running empathy range at scene end: -16 to +6.
# cann.thematic_flags:
#   - Motifs: Breaking what you built, the cost of efficiency, "who we become getting there."
#   - Aeron's insider knowledge as both asset and reminder of his past.
#   - The young guard as moral test—not a threat, just an obstacle.
#   - "I've killed enough people who didn't deserve it" (EMP) vs "The mission is all that matters" (OB).
# cann.alignment_flavor_points:
#   - Opening: Different internal framing of the operation
#   - Correcting Noelle's data: "I designed this to be impenetrable"
#   - Guard choice: The central alignment moment
#   - Aftermath dialogue: Different conversations with Mira/Cade based on choice
#   - Data crystal moment: Confronting his own signatures
# cann.character_moments:
#   - Cade: Veteran, skeptical, respects competence. Opinion shifts based on choices.
#   - Mira: Young, sharp, more conflicted about violence. Relieved (EMP) or disturbed (OB).
#   - Noelle: "Anomaly confirmed" (EMP) or "Efficient" (OB)—her assessment varies.
#   - Zira: Supportive throughout, trusts Aeron's corrections.
# cann.worldbuilding:
#   - Sector 4 depot: Medical supplies, rations, comms equipment.
#   - Aeron's security design: Hidden variance traps, unofficial amendments.
#   - Budget arguments as security flaws—"every argument I lost."
# cann.inventory:
#   - medical_supplies +5, rations +10, comms_equipment +3 for the resistance.
# cann.block_status:
#   - Depot operation complete. Selene debrief pending.
# cann.requires_followup:
#   - A2_13 (Echelon Interlude): Marcus learns about the depot raid.
#   - Selene's assessment will be affected by `guard_spared` vs `guard_eliminated`.
#   - The data crystal Aeron took may be relevant later (evidence of his past work).
#   - Cade and Mira's opinions will echo in later team interactions.
