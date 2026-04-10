# =======================================================
# ACT 3 - Scene 23: Bookend Before the Mirror (Obedience Path)
# File: a3_s23_bookend_before_mirror_ob.rpy
# Type: QUIET MOMENT / ANTI-BOOKEND
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s23_bookend_before_mirror_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s23_bookend_before_mirror_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. Steady. The steadiness is deliberate -- this room doesn't drift.
    #         EMP's bookend used handheld warmth (32mm, gentle drift). OB's bookend uses
    #         the locked frame of a surveillance camera. Observing. Not participating.
    #         Opens wide on the common area. All present. The spatial arrangement visible.
    #         Aeron at the head. Nyra beside him. The others distributed with visible distance.
    #         Close-ups find each person in isolation within the group frame.
    #         The one moment of warmth: tighter lens, handheld for three seconds. Then back to locked.
    # LIGHTING: Common area at evening. Overhead strips at operational brightness.
    #           No one dimmed them. No one thought to.
    #           No amber practicals. No Tessa's lamp. The salvage sconces are dark.
    #           The light is functional. The room is functional. That's the problem.
    # SFX: Loop -- base ambient: operational hum. Ventilation at standard.
    #      One-shots -- chair scrape, utensils on plates (efficient), datapad activation,
    #      someone's boot shifting on the metal floor.
    #      ABSENCE: No quiet laughter. No humming. No mystery herbs.
    #      The sound design should feel like the EMP bookend with everything warm removed.
    # FX/COMP: The common area: the same room as EMP's bookend. Same table.
    #          But maps haven't been cleared. Datapads sit beside plates. The meal is
    #          happening around the work, not instead of it.
    # BLOCKING: Aeron at the head of the table. Nyra to his right -- the position of a second.
    #           Zira across the table, closer to the door than to the center.
    #           Noelle at her usual spot, datapad active.
    #           Lyra at the far end. Hands folded. Not praying -- waiting.
    #           Tessa: present if s10 choice brought her here. If not, her chair is empty.
    #           The spatial arrangement is a hierarchy, not a circle.
    # CANON: OB anti-bookend. The same room, the same meal, everything that made EMP's bookend
    #        feel like home has been replaced by efficiency.
    #        One moment of genuine warmth from Tessa (if present) or Lyra.
    #        The contrast IS the scene.
    # FACE: Aeron -- composed. The face of command at rest. Resting isn't the same as relaxing.
    #        Nyra -- comfortable. She belongs here and she knows it.
    #        Zira -- present. Eating. Not connecting.
    #        Noelle -- observing. The datapad is on. It's always on now.
    #        Lyra -- watching. The eyes of someone looking for the person who used to be there.

    # ========= VOICE BASELINE =========
    # OB cadence: Efficient. Brief exchanges. The conversation serves function, not connection.
    # The one moment of warmth should break the pattern -- a human gesture in a room that forgot
    # how to be human.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - COMMON AREA - EVENING]

    #scene bg_common_area_evening_ob with dissolve
    #play ambient "sfx/ambient/base_evening_operational.ogg" fadein 2.0

    # ========== THE ROOM ==========

    "The common area smells like heated rations. Nothing else. No one added anything."

    "The table is set. That word -- 'set' -- means someone moved the tactical overlays to one end and put plates on the other. The maps are still visible. The meal is an interruption, not an event."

    "Everyone is here. That should mean something. It doesn't mean what it used to."

    athought "Operational briefing at 0600. Nyra's patrol rotation at 0800. Noelle's intelligence update at 1000."

    athought "This meal is a scheduled efficiency. Thirty minutes. Then back to work."

    # ========== THE ARRANGEMENTS ==========

    # --- NYRA ---

    "Nyra sits to Aeron's right. The position she claimed after the Hunt operation. Nobody challenged it. Nobody would."

    "She eats with the discipline of someone who treats food as fuel. Small portions. Measured pace. The fork held like a tool."

    ny "The patrol reports from Sector 8 are clean. Third consecutive day."

    a "Good."

    ny "Nyra's soldiers have integrated into the eastern rotation without incident. Efficiency up fourteen percent."

    "She delivers the numbers the way other people deliver compliments. Operational success as affirmation."

    athought "She's comfortable. Not performing comfort -- inhabiting it. This is where she belongs."

    athought "The others have noticed."

    # --- ZIRA ---

    "Zira is across the table. She's eating. She's present. She's not connecting."

    "Her coil set is on the shelf behind her. Same shelf. Same territorial claim. But the coil set looks like a relic now. Something from before the room changed."

    z "Ghostline traffic is stable. No anomalies."

    a "Anything from the Outlands relays?"

    z "Nothing new."

    "Three words. She used to give him paragraphs. Context. Analysis. The nervous energy of someone who thinks in networks and can't stop mapping."

    "Three words."

    # --- NOELLE ---

    "Noelle's datapad is on the table beside her plate. Face up. Active."

    athought "Face up. Active."

    athought "I remember when she turned it off. Once. At a meal like this. Tessa said 'care' and Noelle said 'less precise but more accurate.'"

    athought "The datapad hasn't been off since."

    n "I'm tracking the civilian displacement patterns from the Hunt operation. Echelon has begun a propaganda campaign attributing the depot raid to 'terrorist cells.'"

    a "Expected."

    n "Expected. But the civilian response is not entirely negative toward Phoenix. The supply disruption is affecting Echelon's distribution to the lower tiers."

    athought "The civilians we displaced are now being affected by the supplies we stole. The loop closes."

    athought "I note it. I don't feel it."

    # --- LYRA ---

    "Lyra is at the far end of the table. Her hands are folded, but not in prayer. In the posture of someone who has nothing to say that would be heard."

    "She looks at Aeron. Not often. In glances that she thinks he doesn't notice."

    athought "She's looking for the person who used to be there."

    athought "I don't know if he's still here either."

    l "The training session with the new arrivals went well. They're adapting."

    a "Good."

    "That's the exchange. Subject. Assessment. Acknowledgment. Complete."

    "Lyra used to follow up. Used to ask about his day. Used to find the question behind the briefing."

    "She doesn't anymore."

    # --- TESSA (conditional) ---

    if flag("tessa_stayed_s10"):

        "Tessa is here. She sits between Lyra and Zira. Equidistant. The mediator's position."

        "She's been quiet through the meal. Not the medic's quiet -- the quiet of someone who has decided that speaking won't change the temperature of the room."

        "Her field kit is on the floor beside her chair. Within reach. Always."

        "She looks at the table. At the plates. At the tactical overlays still visible beneath them."

        athought "Tessa looks at the table the way she looks at a patient she can't treat."

    else:

        "Tessa's chair is empty. She's on rotation in the medbay. Or she chose not to come. The distinction has stopped mattering."

        "Her absence doesn't register as a gap. The table accommodated it without adjusting."

        athought "Someone's missing and the room didn't rearrange."

        athought "That's how you know it stopped being home."

    # ========== THE MOMENT ==========

    "The meal continues. Efficient. Brief exchanges about operational matters. No one asks a personal question. No one tells a story. No one argues about relay optimization or counts almost-smiles."

    "The base functions. That's not the same as living."

    "And then."

    if flag("tessa_stayed_s10"):

        "Tessa stands. Moves to the counter. Fills the water pitcher."

        "She goes around the table. Not asking. Just filling. Zira's cup. Noelle's. Lyra's. She reaches past Nyra to Aeron's."

        "The gesture is automatic. Care as reflex. The same motion she's made a hundred times in this room."

        "She pauses at Nyra's cup. Fills it. Doesn't look at her."

        "Then she sits back down."

        t "(quiet) Goodnight."

        "She hasn't finished eating. She said goodnight anyway."

        "She stands. Takes her plate. Her field kit. Walks to the door."

        "At the threshold, she turns back."

        t "Sleep well. All of you."

        "She says it to the room. Not to anyone in particular. But she says each person's name in her head. You can see it in the way her eyes move across them."

        "She leaves."

    else:

        "Lyra reaches for the water pitcher. Fills her own cup. Then, without pausing, fills Zira's."

        "Zira looks up."

        "Lyra fills Noelle's cup. Reaches across to fill Aeron's. Her hand passes near Nyra's cup. She fills it too."

        "Then she sets the pitcher down."

        l "(quiet) Goodnight."

        "She stands. Folds her hands once -- the shape of a prayer she doesn't say out loud."

        l "I'll pray for us tonight."

        "She means it the way a doctor means 'I'll run tests.' Not comfort. Function."

        "She leaves."

    # ========== THE CLOSE ==========

    "The gesture hangs in the room. Small. A cup of water. A word."

    "Nyra doesn't react. She wouldn't. The gesture is a language she doesn't speak."

    "Zira looks at her cup. Full. She drinks from it."

    "Noelle's stylus pauses. Two seconds. Then resumes."

    athought "Someone refilled the cups. Someone said goodnight by name."

    athought "Someone did the smallest possible thing and it was the largest thing that's happened in this room in weeks."

    athought "This used to be a home. I remember. The herb smell. The dimmed lights. The sound of five voices overlapping because they wanted to, not because the schedule required it."

    athought "This room functions."

    athought "It doesn't live."

    "The meal ends. People disperse to their stations. Their shifts. Their quarters."

    "Nyra is the last to leave besides Aeron. She pauses at the door."

    ny "The operation tomorrow requires a 0500 start. I'll have the briefing materials ready."

    a "Good."

    ny "Goodnight, Commander."

    "She leaves. Professional. Precise."

    "Aeron sits at the head of the table. The tactical overlays spread beneath the empty plates."

    "The overhead lights hum. Full brightness. No one dimmed them."

    athought "No one dimmed the lights."

    athought "In the EMP -- no. That's not a thought. That's not anything."

    athought "The lights are on. The base functions. The operations continue."

    athought "That's enough."

    "It isn't."

    "He doesn't dim them on his way out."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s23_bookend_before_mirror_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After the Hunt (s22). Before Liora confrontation (s24).
#   - Evening. The group together. The anti-bookend.
# cann.what_happened:
#   - The common area, the same room as EMP's bookend. All LIs present. Evening meal.
#   - Everything that made EMP's bookend feel like home is gone:
#     Maps not cleared. No herbs. No dimmed lights. Datapad on, not off. Conversations operational.
#   - Nyra at Aeron's right. Comfortable. The others distributed with visible distance.
#   - Zira: three words. Used to give paragraphs. The coil set is a relic.
#   - Noelle: datapad face-up, active. Hasn't been turned off since.
#   - Lyra: far end. Looking for the person who used to be there.
#   - Tessa (if present): quiet. Looking at the table like a patient she can't treat.
#   - ONE MOMENT: Tessa (or Lyra) refills cups. Says goodnight by name. The smallest gesture.
#     The largest thing that's happened in this room in weeks.
#   - "The base functions. That's not the same as living."
# cann.aeron_state:
#   - He remembers what this room used to be. He doesn't change it.
#   - The lights stay on full. No one dimmed them. He doesn't either.
#   - "It isn't enough." He knows. He walks out anyway.
# cann.path_tracking:
#   - scene_mark only. No state changes. The scene IS the state.
#   - Conditional on flag("tessa_stayed_s10") for Tessa vs Lyra warmth beat.
# cann.thematic_flags:
#   - THE ANTI-BOOKEND: Point-for-point inversion of a3_s21_bookend_before_storm_emp.
#     Same room. Same people. Everything warm removed. The contrast is the devastation.
#   - "Functions vs lives": the OB thesis stated plainly. The base works. It isn't home.
#   - The cup of water: the smallest human gesture. Enormous in a room that forgot warmth.
#   - The lights: no one dimmed them. No one thought to. The absence of the domestic instinct.
#   - Noelle's datapad: face up (OB) vs face down (EMP). The same object. Different meaning.
#   - Nyra's comfort: she belongs. That's part of the problem.
# cann.character_moments:
#   - Nyra: Comfortable. Reports patrol data at dinner. "Goodnight, Commander." Not his name.
#   - Zira: Three words. The network-thinker reduced to status reports.
#   - Noelle: Datapad active. Tracking civilian displacement from the Hunt. The math follows her home.
#   - Lyra: Far end. Glances. Looking for someone. Not finding him.
#   - Tessa: (if present) Looking at the table like a patient. The cup of water. "Goodnight."
# cann.callbacks:
#   - a3_s21 (EMP): The bookend. "Home." The herb smell. Noelle's datapad off. Selene's almost-smile.
#     Everything this scene inverts.
#   - a3_s22: The Hunt. The civilian displacement Noelle tracks. The cost following them to dinner.
#   - a3_s20: Zira's confrontation. "Hard vs hollow." This room is the hollow.
#   - a3_s06: Nyra's integration. She's at his right hand now. Comfortable.
# cann.block_status:
#   - QUIET SCENE. Anti-bookend. Conditional Tessa/Lyra beat. No branching.
# cann.requires_followup:
#   - a3_s24: The mirror. Everything this scene quietly mourns is what Liora will name.
#   - The cup of water: will the warmth survive? Can it?
#   - Nyra calling him "Commander" vs his name: the distance in the address.
