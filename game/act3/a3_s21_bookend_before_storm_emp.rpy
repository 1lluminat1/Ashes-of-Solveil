# =======================================================
# ACT 3 - Scene 21: Bookend Before the Storm (Empathy Path)
# File: a3_s21_bookend_before_storm_emp.rpy
# Type: SLICE-OF-LIFE / POLY FORESHADOWING
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s21_bookend_before_storm_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s21_bookend_before_storm_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm, handheld with gentle drift (2%). Warm. Domestic. The camera moves
    #         like someone walking through a room where everyone belongs.
    #         Opens wide on the common area — all five LIs present. The geography of comfort.
    #         The camera finds each person in their element: lingering, not rushing.
    #         Aeron's POV: the camera becomes his eyes. Watching. Present.
    #         Poly beat: wider frame. The spatial relationships visible. Ease. No tension.
    #         Close: the camera slowly pulls back. A tableau. The last warm frame before it breaks.
    # LIGHTING: Common area at evening. Overhead strips dimmed to 40%.
    #           Amber practicals: Tessa's lamp, the wall sconces someone rigged from salvage.
    #           The light is warm, diffuse, forgiving. The kind of light that makes a bunker feel
    #           like a kitchen. Windows (if any): deep blue dusk from outside.
    # SFX: Loop — base evening: muffled activity, someone's bootfall in a distant corridor,
    #       the ventilation at its quietest setting.
    #      One-shots — utensils on plates, water poured, chair scrape, quiet laughter,
    #      Zira's coil set clinking as she moves it, Lyra humming (half a phrase, then stops).
    #      The overall sound: a room full of people who aren't performing relaxation.
    # FX/COMP: The common area transformed into something domestic. Mismatched seating.
    #          A table cleared of maps and set with whatever passes for a meal.
    #          Zira's coil set on a shelf behind her — visible, territorial.
    #          Tessa's field kit on the floor beside her chair — never more than arm's reach.
    #          Lyra's prayer beads on the table beside her plate.
    #          Noelle's datapad, face-down. Turned off. That's the detail.
    # BLOCKING: The group arranged with the spatial ease of people who have learned where each
    #           other fits. No assigned seats — but everyone gravitates to the same spot.
    #           Selene at the end of the table. But sitting. Not standing at the ops board.
    #           Zira beside Noelle. Tessa across from Lyra. Aeron wherever he lands.
    #           The blocking should feel organic, not choreographed.
    # CANON: SLICE-OF-LIFE scene. The calm before a3_s22 (the execution).
    #        Designed to make the player feel what they're about to lose.
    #        Poly foreshadowing: group comfort, spatial ease, no jealousy.
    #        Must feel like home.
    # FACE: Everyone — relaxed. The particular relaxation of people who don't get to relax.

    # ========= VOICE BASELINE =========
    # EMP cadence: Full warmth. Contractions. Sensory detail. The scene should feel textured —
    # the food, the light, the sound, the specific weight of being in a room with people
    # you chose and who chose you.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - COMMON AREA - EVENING]

    #scene bg_common_area_evening_emp with dissolve
    #play ambient "sfx/ambient/base_evening_domestic.ogg" fadein 3.0
    #play music "music/home_theme_quiet.ogg" fadein 4.0

    # ========== THE ROOM ==========

    "The common area smells like heated rations and something Lyra added — a dried herb from the Sector 7 salvage. She won't say what it is. She says naming it takes the mystery out of the flavor."

    "The table is set. That word — set — means something different in a rebel base. It means someone cleared the maps, someone found plates that don't match, someone decided that eating together matters enough to make a space for it."

    "Tonight, all five of them are here."

    athought "That almost never happens. Someone is always on watch, or running a relay check, or patching a wound, or sleeping off the last seventy-two hours."

    athought "Tonight, everyone is here. And no one arranged it."

    # ========== THE MOMENTS ==========

    # --- ZIRA ---

    "Zira is at her end of the table. She's moved her coil set to the shelf behind her — the one she claimed during the second week at the base. No one else puts anything on that shelf."

    "Someone tried once. A new arrival, unfamiliar with the ecosystem. The coil set was relocated six inches to accommodate a water flask."

    z "(to no one in particular) If anyone touches the coil set, I will personally reroute their Ghostline access through the sewer relay."

    "No one has touched the coil set since."

    athought "She's eating with one hand and scrolling Ghostline traffic with the other. Even here, even now, one eye on the network."

    athought "But she's here. That's the part that matters."

    # --- NOELLE ---

    "Noelle's datapad is on the table beside her plate. Face-down."

    athought "Face-down. Turned off."

    athought "I've known Noelle for months. I've never seen her turn the datapad off. Not in the medbay. Not in briefings. Not during operations."

    athought "It's off."

    "She's eating methodically. Small bites. Even intervals. But her eyes aren't on the food — they're on the table. On the people around it."

    n "The probability of survival increases with... invested persistence."

    "Tessa looks up. Something crosses her face."

    t "(quiet) Care. She means care."

    $ nudge_poly(1)

    athought "Tessa translated Noelle into human without either of them asking for it."

    athought "That's been happening more. The small translations. The way Tessa hears what Noelle means beneath what Noelle says."

    "Noelle blinks. Processes the translation."

    n "...yes. That is a less precise but more accurate phrasing."

    athought "Less precise but more accurate. That might be the most Noelle sentence ever spoken."

    # --- LYRA ---

    "Lyra folds her hands before eating. The prayer is silent. Brief. Her lips move, but the words are hers alone."

    "When she finishes, she unfolds her hands and reaches for the herb bowl. No transition. The sacred and the practical in the same gesture."

    l "Tessa, the sprain in East Wing — did the swelling respond to the cold compress?"

    t "Down by thirty percent. She'll be mobile by tomorrow."

    l "Good. She's been asking about the children."

    t "Of course she has."

    "They share a look. The look of two people who have been caring for the same population from different angles and have reached the point where the angles overlap."

    athought "Lyra prays and Tessa treats. Different methodologies, same commitment."

    athought "They've stopped arguing about which one matters more. Sometime in the last month, they just... stopped."

    # --- SELENE ---

    "Selene is sitting."

    "Not standing at the ops table reviewing patrol data. Not at the perimeter checking the watch rotation. Not in the corridor making command decisions."

    "Sitting. At the table. With a plate."

    athought "I almost said something. Almost marked the occasion."

    athought "But marking it would break it. The whole point is that she's here without it being an event."

    "She eats. Steady, efficient bites. The same pace she applies to everything. But her shoulders are lower than usual. Not braced."

    sel "The southern relay has been stable for nine days."

    z "Don't jinx it."

    sel "I don't believe in jinxes."

    z "That's exactly what someone about to jinx it would say."

    "Selene almost smiles. The corner of her mouth moves. She catches it, but not before Tessa sees."

    t "(to Selene, very quiet) That counts."

    sel "What counts?"

    t "The almost-smile. I'm counting those."

    sel "You have a board for that?"

    t "I have a board for everything."

    # --- THE GROUP ---

    "The conversation layers. Overlaps. The sound of five voices in a room that fits them."

    "Zira argues with Noelle about relay optimization. Noelle argues back with data. Zira argues back with experience. They agree on the third option neither of them proposed."

    "Lyra asks Selene about the eastern sector patrol schedule. Selene answers in detail that would be classified in any other context. Here it's dinner conversation."

    "Tessa refills water. For everyone. Without being asked. The gesture is automatic — care as reflex, not decision."

    # --- AERON WATCHING ---

    athought "I'm watching."

    athought "Not observing. Not analyzing. Not running tactical assessments on the interpersonal dynamics."

    athought "Watching. The way you watch a fire. Because it's warm and it moves and you don't need anything from it except for it to keep going."

    athought "This is what we built."

    athought "Not the base. Not the operations. Not the Ghostline or the corridor extractions or the Purge data."

    athought "This. A room with food and people and the specific gravity of belonging."

    # --- POLY FORESHADOWING (conditional) ---

    if metric("poly_pressure") >= 5:

        athought "Something else, though. Something I don't have a name for."

        "The seating. Zira beside Noelle, their elbows occasionally touching. Tessa across from Lyra, the looks between them carrying whole conversations. Selene at the end, present in the circle instead of above it."

        "The spatial ease. No one is calculating proximity. No one is monitoring where Aeron's attention lands. No one flinches when someone else leans close."

        athought "In the world I came from — the Glass Academy, the Aeries, Marcus's architecture — people guarded their positions. Relationships were territory. Attention was currency."

        athought "This isn't that."

        athought "This is five people who care about the same person and aren't threatened by each other's care."

        athought "I don't know what that becomes. I don't know if it becomes anything."

        athought "But the room holds it. And no one is asking it to be smaller."

    # ========== THE CLOSE ==========

    "The meal ends. No one leaves immediately."

    "Lyra collects plates. Zira washes them — she does this, every time, without being asked, and will deny it if confronted."

    "Noelle retrieves her datapad. Turns it on. But she doesn't open it immediately. She holds it for a moment, face-down on her knee, like she's measuring the weight of the silence before letting the data back in."

    "Tessa packs her field kit. The instruments in order. Ready."

    "Selene stands. But she pauses at the table edge. Looks back at the room."

    "It's not a commander surveying her team. It's someone looking at a thing they helped build and recognizing it as good."

    "She leaves. The door closes softly."

    athought "Home."

    athought "I've been trying to name what this base became, and the word has been right there the whole time."

    athought "Home."

    athought "It won't last. Nothing does. The next operation, the next Echelon strike, the next cost — it's coming."

    athought "But right now, in this room, with the herb smell and the lamp light and the almost-smile I'm not supposed to have seen—"

    athought "This is home."

    "The common area settles into quiet. The lamp light holds."

    #stop music fadeout 5.0
    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ nudge_poly(1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s21_bookend_before_storm_emp
# cann.chapter: Act III, Phase III — Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase III. After The Story Keeper (s20). The last scene before the execution (s22).
#   - Evening. Base as home. The calm designed to make the storm devastating.
# cann.what_happened:
#   - Communal meal. All five LIs present. No one arranged it — it happened naturally.
#   - Character moments: Zira's coil set (territorial), Noelle's datapad turned off (unprecedented),
#     Lyra's silent prayer and herb mystery, Selene sitting at the table (not the ops board),
#     Tessa refilling water without being asked (care as reflex).
#   - Poly nudge: Noelle says "invested persistence." Tessa translates: "Care. She means care."
#     nudge_poly(1) on the translation beat.
#   - Conditional poly foreshadowing (poly_pressure >= 5): spatial ease visible. No jealousy.
#     No territory. The room holds something that isn't asking to be smaller.
#   - Aeron watching. Home. The word he's been looking for.
#   - The scene should feel warm, real, domestic. So the next scene destroys the player.
# cann.aeron_state:
#   - Watching, not analyzing. The fire metaphor: warm, moving, no demands.
#   - "This is what we built." The room as achievement greater than any operation.
#   - "Home." The word arriving.
# cann.path_tracking:
#   - nudge_poly(1) on Noelle/Tessa translation beat. Additional nudge_poly(1) at scene end.
#   - Conditional poly foreshadowing if poly_pressure >= 5.
#   - No player choice. Slice-of-life. The scene earns itself through character accumulation.
# cann.thematic_flags:
#   - Home: the word. The base became this without anyone deciding it.
#   - Domestic detail as emotional weight: mismatched plates, herb smell, almost-smiles.
#   - Tessa/Noelle translation: "Less precise but more accurate." Care in two languages.
#   - Selene sitting: the smallest gesture, the largest arc movement.
#   - The datapad face-down: Noelle choosing the room over the data. Unprecedented.
#   - Zira washing dishes and denying it: care expressed through action, not admission.
#   - Lyra's prayer and herb: sacred and practical in the same gesture.
#   - "It won't last. Nothing does." — the reader feels the incoming storm.
# cann.character_moments:
#   - Zira: Territorial about the coil set. Washes dishes. Denies it. Arguments with Noelle
#     that resolve in a third option neither proposed.
#   - Noelle: Datapad off. "Less precise but more accurate." Holds the datapad before turning
#     it back on — measuring the silence.
#   - Lyra: Silent prayer. The herb. Checking on patients with Tessa. Sacred-practical fusion.
#   - Tessa: Translates Noelle. Refills water. Counts Selene's almost-smiles. Care as reflex.
#   - Selene: Sitting. Shoulders lower. Almost smiling. Looking back at the room. Recognizing good.
# cann.callbacks:
#   - a3_s12: Post-corridor-op common area. The same room, now transformed by time and belonging.
#   - a3_s18: The Weight. Tessa's board. Selene sitting here is the trust pivot in action.
#   - a3_s05: Two Healers. Lyra and Tessa's parallel care — now overlapping without friction.
#   - a3_s11: Empirical Tenderness. Noelle's emotional development — datapad off is the arc.
#   - Zira's coil set: established territory. The Ghostline made personal.
# cann.block_status:
#   - SLICE-OF-LIFE. Poly foreshadowing. No branching. Designed for emotional setup.
# cann.requires_followup:
#   - a3_s22: The execution. Everything this scene builds is what that scene costs.
#   - "Home" as a word: will it survive what's coming? Does Aeron get to keep it?
#   - Poly arc: the nudges accumulate. The group comfort is visible. What happens next?
#   - Tessa/Noelle translation dynamic: seeds for Act 4 relationship development.
#   - Selene sitting: the trust pivot continues. Can she stay in the chair when command calls?
