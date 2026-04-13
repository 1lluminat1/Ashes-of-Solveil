# =======================================================
# ACT 4 - Scene 06: Tessa at the Board (Obedience Path)
# File: a4_s06_tessa_at_the_board_ob.rpy
# Path: OB
# Type: TESSA STATE BEAT -- the board survives the displacement, corrupted.
# Character Focus: Tessa (majority), Aeron (final minute)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s06_tessa_at_the_board_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s06_tessa_at_the_board_ob:
    $ show_timeline("27th of Forge, 390 A.C.", "06:00", "Phoenix Base — Medical Wing")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. No handheld drift. OB economic register --
    #         the camera does not move unless someone crosses it. Opens on the
    #         board header in close-up: Tessa's handwriting, then the overwrite
    #         on top of it, in a different marker. Rack focus between the two
    #         layers of ink. The overwrite is the scene. Everything else is
    #         orbit around it.
    #         Mid-scene: pull back to reveal Tessa's posture at full figure.
    #         She has not moved in minutes. The camera does not cut -- it holds.
    #         Final minute: Aeron enters the frame from the left. The camera
    #         does not track to him. He walks into an already-composed shot.
    #         His hand enters the frame to wipe a name. The camera holds on
    #         the board. Tessa is no longer in the room. Her absence is the
    #         second shot of the scene.
    # LIGHTING: New medical wing -- Nyra's restructuring authorized it, and it
    #           shows. Overhead strips: bright, institutional, sodium-cold.
    #           The building's light is the wrong temperature for Tessa's work.
    #           Practical: her clip lamp on the board's top edge. Amber. The
    #           same lamp from the interludes. The only warmth in the room,
    #           and it is losing the fight against the overheads.
    #           When Tessa turns off the clip lamp at the end: the room shifts
    #           into full institutional white. The warmth is gone. The board
    #           is still there. Institutionally lit. Administratively correct.
    # SFX: Loop -- new wing HVAC, a different hum from the old war room. Cleaner.
    #      More expensive. The hum of a budget line item.
    #      One-shots -- clip lamp click (off), Tessa's boots on sealed floor,
    #      door seal on exit, the small mechanical breath of the wing's
    #      ventilation re-balancing after the door closes. Aeron's boots
    #      entering -- a different weight, heavier, unhurried.
    #      The marker: Aeron uses his sleeve. No cap click. No pen on paper.
    #      The erasure is almost silent.
    # FX/COMP: The new medical wing. Six beds. Supply cabinets keyed to Nyra's
    #          inventory system. A wall-mounted tablet for intake forms.
    #          And, bolted to the far wall: Tessa's board.
    #          The portable board from the war room, now mounted. Nyra's
    #          restructuring authorized the wing, and someone -- not Tessa --
    #          decided the board should come with it. Two columns. Tessa's
    #          careful handwriting throughout.
    #          The header of the left column: originally THE LIVING.
    #          Over it, on a strip of adhesive plastic -- black lettering,
    #          a hand that is not Tessa's -- the word OPERATIONAL.
    #          The strip peels at the edges. The original header is still
    #          visible underneath at the margins. The overwrite does not
    #          erase. It layers.
    # BLOCKING: Tessa enters the wing at the top of her shift. Stops six feet
    #           from the board. Does not approach closer. Stays there for the
    #           bulk of the scene. Does not sit. Does not set down her bag.
    #           At the end: she crosses to the board, reaches up, clicks off
    #           the clip lamp. Does not touch the marker. Does not touch the
    #           overwrite. Does not touch any name. She leaves the lamp
    #           on its clip. She walks out.
    #           Aeron enters after she has gone. He does not see her leave.
    #           He reads both columns. His hand reaches up. He wipes one name
    #           from the left column with his sleeve. He does not clean the
    #           sleeve after.
    # CANON: OB Act 4. The board survives into the regime. It is mounted now,
    #        institutional. The header has been overwritten: LIVING -> OPERATIONAL.
    #        Tessa does not erase. Does not keep. Leaves the lamp.
    #        Aeron arrives separately, moves Liora's name from the living column
    #        to the dead column by administrative erasure. He does not know
    #        Tessa was just here. She does not know he did this.
    # FACE: Tessa -- not grief. Not anger. A calculation running slow.
    #        The kind of stillness that looks like peace from outside and is not.
    #        Aeron (final minute) -- the mask. The mask now has a vocabulary
    #        for what it is doing. He does not flinch when he sees OPERATIONAL.
    #        He does not flinch when he wipes his mother's name.

    # ========= VOICE BASELINE =========
    # Tessa: interior-only for most of the scene. She does not speak aloud.
    #        The count is no longer spoken. The ritual has been corrupted and
    #        she is deciding what to do with a corrupted ritual. Her interior
    #        is procedural, not emotional. She runs the problem like a triage.
    # Aeron (final minute): athought, cold. Marcus-idiom competent. He reads
    #        the board as a document. He updates the document.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - NEW MEDICAL WING - 0600]
    # The wing Nyra's restructuring built. Two months old. Still smells new.
    # Sealed floor. Sodium overheads. Six beds, three occupied.
    # The board bolted to the far wall. The amber clip lamp above it.

    #scene bg_new_medwing_ob with dissolve
    #play ambient "sfx/ambient/medwing_hvac.ogg" fadein 2.0

    # ========== PHASE 1 -- ARRIVAL ==========

    "0600. The new wing runs warm because the HVAC is still commissioning. It will run cold inside a week. Tessa has been told this twice, by two different engineers, and neither was wrong."

    "She enters through the staff door. Badge tap. Seal breath. The overhead strips come up in sequence as the occupancy sensor catches her."

    "The wing is cleaner than the old medbay. Cleaner than anything she has ever worked in. The beds are new. The supply cabinets are keyed to Nyra's inventory system -- swipe in, swipe out, the cabinet logs the quantity."

    "The board is bolted to the far wall."

    "She did not ask for it to be bolted. Someone made the decision. The bolts are flush-set. The board is load-bearing now. If she wanted to take it down she would need a drill."

    "She sets her bag on the nearest supply cart. She does not take off her coat."

    "She looks at the board."

    # ========== PHASE 2 -- THE OVERWRITE ==========

    "The board has survived the displacement. Both columns. Her handwriting intact from the war room. Every name she carried over."

    "The right column: THE DEAD."

    "The left column, originally: THE LIVING."

    "Originally."

    tthought "Someone has written over the header."

    tthought "A different marker. Black. Thicker tip. Not mine."

    tthought "The word is OPERATIONAL."

    "Her handwriting on THE LIVING is still visible under the overwrite. The new word does not erase the old one. It layers on top."

    "The two words occupy the same space. You can read both if you look. From a distance, only the new one shows."

    tthought "OPERATIONAL."

    "She does not move closer. She does not step back. She stands six feet from the board and begins the calculation."

    # ========== PHASE 3 -- THE CALCULATION ==========

    tthought "First question. Who did it."

    tthought "Not Nyra. Nyra would not use a marker. Nyra would requisition a label maker and print it clean."

    tthought "Not Aeron. Aeron would tell me before he did it. Or he would not do it at all. He would ask Nyra to ask me. Or he would have a requisition form drafted."

    tthought "Someone mid-rank. Someone who decided the language needed correcting and had enough authority to walk into a medical wing at night with a marker."

    tthought "Nyra's restructuring hired fourteen mid-rank coordinators last month. It could be any of them."

    tthought "It doesn't matter which one. The point is that it is now possible. The point is that whoever did it did not think they needed to hide it."

    "She looks at the bolt heads around the board. Flush-set. Load-bearing."

    tthought "The board is a fixture now. It belongs to the wing. The wing belongs to the restructuring. The restructuring belongs to Nyra."

    tthought "The board does not belong to me anymore. I am the one who writes on it. I am not the one who decides what it is for."

    # ========== PHASE 4 -- THE THREE OPTIONS ==========

    tthought "Three options."

    tthought "One. I erase the overwrite. I restore the original header."

    tthought "If I erase it, whoever wrote it will write it again. Maybe tonight. Maybe tomorrow. They have a marker and they have access. I do not sleep in this wing. I cannot outlast someone with keys."

    tthought "And when they write it the second time, they will write it harder. They will find a more permanent marker. They will bring a label maker. They will requisition the clean version."

    tthought "Erasing is not a fix. Erasing is a provocation that buys one shift."

    "Pause. She adjusts her stance. She has been standing in the same spot for four minutes."

    tthought "Two. I leave it. I keep working the board. I fill in names under a header I did not write."

    tthought "If I leave it, I am agreeing. Not in words. In practice. The names I add under OPERATIONAL are names I have accepted to list under OPERATIONAL. The next nurse who inherits this board will see the word and assume I chose it."

    tthought "I did not choose it. But if I keep writing, the distinction will not survive me."

    tthought "Leaving is not neutrality. Leaving is ratification by continued use."

    "A longer pause. Someone in bed three shifts in their sleep and the bed frame makes a small metal sound."

    tthought "Three. I stop keeping the board."

    tthought "If I stop, the names disappear. Not from the dead column -- those stay, bolted to a wall in a wing no one will think to repurpose. The living names will stop being added. The dead names will stop being added. The count will freeze."

    tthought "And whoever wrote OPERATIONAL will eventually take the board down, because a board no one updates is a fire hazard and the wing has inspections."

    tthought "Stopping the board is letting the names disappear entirely."

    tthought "That is worse than what has been done to the header."

    # ========== PHASE 5 -- THE NON-CHOICE ==========

    tthought "None of the three options is the one I want."

    tthought "I want a fourth option. I want to take the board off the wall, carry it back to the war room, restore the header, and keep counting where no one can reach it."

    tthought "The board is bolted. The war room is a briefing room now. Nyra holds morning stand-ups in it."

    tthought "The fourth option does not exist."

    "She has not moved. Her hands are at her sides. Her coat is still buttoned."

    tthought "So I pick the one that does the least damage and I do it with my eyes open."

    tthought "I do not erase. Erasing provokes a harder rewrite."

    tthought "I do not keep. Keeping ratifies the word."

    tthought "I do not stop permanently. That is option three and option three is worse."

    tthought "I stop tonight."

    tthought "Only tonight. The wing is quiet. Three patients, all stable. No intake since 0200. If there is a night where the board can go uncounted without anyone dying of the omission, it is tonight."

    tthought "And I do not take the lamp with me."

    # ========== PHASE 6 -- THE LAMP ==========

    tthought "The clip lamp is mine. I brought it from the war room. It is my lamp, not the building's. It runs on the battery pack I keep charged in my coat."

    tthought "If I take it, I am taking my care out of this room."

    tthought "If I leave it, I am leaving my care in the room with the corrupted board. Not as approval. As a placeholder. As a thing I may or may not come back for."

    tthought "A placeholder is not a commitment. A placeholder is a marker that says -- I have not yet decided whether this room is still mine."

    tthought "I do not know if I am coming back for the lamp."

    tthought "That is the honest state. I do not know."

    tthought "I will leave the lamp where it is and I will walk out of this wing and I will see what I am when I wake up."

    # ========== PHASE 7 -- THE ACT ==========

    "She crosses the six feet. The approach takes longer than it should. Sealed floor under her boots. The overhead strips catch her shadow and throw it small onto the board."

    "She reaches up."

    "She does not touch the marker. She does not touch the overwrite. She does not touch any name on either column. Her hand passes two inches from the word OPERATIONAL and does not engage with it."

    "Her fingers find the clip lamp's power button."

    "Click."

    "The amber dies. The board goes institutional. The overheads take the whole of it. OPERATIONAL is still the first word the eye catches. THE LIVING is still underneath."

    "She lowers her hand. She does not look at the dead column. She does not look at Selene's name. She does not look at LIORA RYLAN written on both sides."

    "She turns."

    "She walks to the staff door. She does not pick up her bag from the supply cart -- she will need it later, she tells herself, and then corrects the telling: she is leaving the bag because she has not yet decided whether she is coming back for the bag."

    tthought "The lamp stays. The bag stays. I am leaving more than I planned to leave."

    tthought "That is what the calculation was missing. I did not know how much of me was in this room until I tried to take it out."

    "Badge tap. Seal breath. The staff door closes behind her."

    "The wing is empty of her."

    "The board is still bolted to the wall."

    # ========== PHASE 8 -- AERON ARRIVES ==========

    "Thirty seconds of silence. The HVAC cycles. Bed three shifts again."

    "Badge tap from the main corridor door. A different cadence -- heavier, unhurried."

    "Aeron enters."

    athought "Looking for her. Stelker flagged a rotation conflict in the intake logs, wanted me to route it through medical before he escalates. Fifteen-minute errand."

    athought "She is not here."

    athought "Her coat is not hanging. Her bag is on the supply cart."

    athought "She was here and she left."

    "He does not call her name. He walks the length of the wing. Passes the three occupied beds without looking at the patients. Arrives at the far wall."

    "The board."

    athought "Still mounted. Still both columns."

    athought "The header has been overwritten."

    "He reads it. The original word and the new word. Both visible. He reads them once and he understands them once. The reading takes about two seconds."

    athought "OPERATIONAL."

    athought "Someone made a small linguistic correction. I can guess which coordinator. It does not matter which coordinator."

    athought "I am not surprised. I am not angry. I am noting it."

    athought "A month ago I would have asked Tessa to change it back. Two months ago I would have changed it back myself."

    athought "Now I read it and I do not move to correct it. That is information about me. I am noting that too."

    "He turns his attention from the header to the columns themselves."

    athought "Left column. Operational. The living. She has been adding names. The most recent entries are in her hand. She was here recently enough that the ink is still dry."

    athought "Right column. The dead."

    "He reads down the right column. His eyes do not rush. The reading is procedural."

    athought "Selene Ward. Ito. Yang. Dinh. The sector eight names. The names from the Obsidian Bridge. The names from the sweep."

    athought "New entries since the displacement. Tessa keeps current."

    "His eyes reach the bottom of the column. Then track to the left column and begin the second pass."

    athought "Left column. Operational."

    athought "Dren. Vasquez family. Ansel. The old list. She carried it over."

    "And then his eyes stop."

    athought "LIORA RYLAN."

    athought "Left column."

    athought "She left the name on the left column."

    "He stands in front of the board. His hand is at his side."

    athought "Tessa did not know how else to count her."

    athought "My mother walked. Tessa did not have a column for walked. So she kept her in living. Because the alternative was moving her to dead, and Tessa will not do that without a body."

    athought "Tessa requires evidence."

    athought "I do not."

    # ========== PHASE 9 -- THE ERASURE ==========

    "He looks at the right column. LIORA RYLAN is not there."

    "He looks at the left column. LIORA RYLAN is there. In Tessa's handwriting. Careful letters. The same pressure she uses on every name."

    athought "If I leave it in the left column, it is a lie I am letting her tell for me. She is holding a place for someone I have decided is gone."

    athought "I have decided she is gone. That is the decision I made the night she walked and have not yet told anyone I made."

    athought "I can tell Tessa by changing the board. I do not have to say the words."

    athought "That is the cleanest way to say it."

    "He reaches up."

    "He uses his sleeve. The cuff of his uniform jacket. He passes it over the letters L-I-O-R-A R-Y-L-A-N in the left column. The ink is old enough to resist for half a second and then it gives."

    "The letters smear and then go. A faint ghost remains. Anyone who knew the name was there could still see it. Anyone new would not."

    "He does not wipe the sleeve. The ink stays on the cuff. He lowers the arm."

    athought "Left column: clean."

    athought "Right column: she is still there. Tessa wrote her there the night she walked because Tessa counts both sides. I do not move her. She is already in the right column. I just removed the duplicate."

    athought "That is the administrative version of burial."

    athought "My mother has been buried administratively. By her son. In a wing her son's co-command authorized. On a board whose header her son's co-command corrected."

    athought "I am noting that too."

    # ========== PHASE 10 -- EXIT ==========

    "He lowers his hand. He does not look at the right column again. He does not look at Selene's name. He does not look at the overwritten header."

    "He turns from the board."

    "He walks back down the wing. Past the three beds. The occupancy sensor does not trigger again -- he is inside the detection window from his entry."

    "At the supply cart he stops."

    athought "Her bag."

    athought "Her lamp is still on the board clip. Off. She left it. She does not leave the lamp."

    athought "She has left both things."

    athought "I am not going to take them. I am not going to move them. That is not my decision to make."

    athought "I am going to tell Stelker his rotation conflict can wait until she resurfaces. If she resurfaces."

    "He does not touch the bag. He does not touch the lamp."

    "He walks to the main corridor door. Badge tap. Seal breath."

    "The wing is empty of both of them."

    "The board is still bolted to the wall. OPERATIONAL over THE LIVING. Selene in the right column. Liora in the right column only now."

    "The bag is still on the supply cart."

    "The amber lamp is still clipped to the top of the board, off."

    "The overheads hold the whole wing in sodium white."

    "Bed three shifts in their sleep."

    # ========== SCENE CLOSE ==========

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.tessa.board_overwritten", "OPERATIONAL")
    $ canon_set("ob.liora.moved_to_dead_column", True)
    $ canon_set("ob.aeron.mother_buried_administratively", True)
    $ tp_seed("a4.ob.tessa.lamp_left_behind")
    $ flag("tessa_did_not_erase_overwrite", True)
    $ flag("tessa_did_not_keep_board_tonight", True)
    $ flag("tessa_left_lamp_in_wing", True)
    $ flag("aeron_wiped_liora_from_living", True)
    $ npc_remember("Tessa", "board_ritual_corrupted_calculated_response", tone="procedural_grief")
    $ npc_remember("Aeron", "administrative_burial_of_mother", tone="unflinching")
    $ metric("ob.intimacy.cold", +1)
    $ metric("ob.ritual.corrupted", +1)

    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s06_tessa_at_the_board_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: False
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Act 4 OB. 0600. New medical wing, two months after Nyra's restructuring
#     authorized it. The board has been mounted (bolted) to the far wall.
# cann.what_happened:
#   - Tessa arrives for her shift and finds her board's LIVING header has been
#     overwritten in a different marker with the word OPERATIONAL. Both words
#     are visible; the overwrite layers without erasing.
#   - Tessa runs the triage in her interior: erase, leave, stop. Concludes all
#     three are bad, and chooses the least-damaging: stop for tonight only.
#   - She does not erase. Does not keep. Turns off her amber clip lamp and
#     leaves it clipped to the board. Leaves her bag on the supply cart too.
#     Neither departure is a commitment -- both are placeholders.
#   - Aeron arrives separately (fifteen-minute errand from Stelker, rotation
#     conflict in intake logs). Finds the wing empty of Tessa. Reads the board.
#     Notes OPERATIONAL without reacting. Reads both columns.
#   - His eyes stop on LIORA RYLAN in the LIVING column. Tessa had listed her
#     there since Act 3 finale because Tessa did not have a column for "walked."
#     Aeron uses his sleeve to wipe his mother's name from LIVING. The ink
#     stays on his cuff; he does not clean it.
#   - Liora is now only in the DEAD column. Aeron has buried his mother
#     administratively, on a board his co-command authorized, in a wing his
#     co-command restructured.
#   - Aeron leaves without taking Tessa's bag or lamp.
# cann.tessa_state:
#   - Not grief. Not rage. A calculation run slow. The ritual has been
#     corrupted and she is deciding what kind of corrupted ritual to live in.
#   - Interior voice only. She does not speak aloud the entire scene.
#   - The count is no longer spoken. The board has become a load-bearing
#     fixture in a system she does not control.
#   - The lamp is the tell: she leaves her care in the room as a placeholder
#     she has not yet decided whether to reclaim.
# cann.aeron_state:
#   - Competent in Marcus idiom. He reads the overwrite as information about
#     himself: "A month ago I would have asked Tessa to change it back."
#   - No drama on the erasure. Sleeve, half-second resistance, faint ghost,
#     lowered hand. The cuff stays stained. He does not clean it.
#   - "Administrative burial" is the vocabulary he now has for it. Violence
#     has become a filing system. This is Violence Normalized in one gesture.
# cann.thematic_flags:
#   - OB Act 4 thesis: "Violence Normalized." The board ritual survives the
#     displacement but survives CORRUPTED, and corruption is accepted as
#     the new operating condition.
#   - LIVING -> OPERATIONAL: the regime's linguistic correction. Not denial,
#     not propaganda. Just a cleaner word for what people are for.
#   - Tessa's three options (erase / leave / stop) map the impossibility of
#     resistance under institutional capture. The fourth option -- take the
#     board home -- does not exist because the board is bolted.
#   - The lamp left behind: the OB version of the EMP "empty mug at the head
#     of the table." In EMP, Tessa sets a place for Selene. In OB, she leaves
#     her own lamp with a corrupted ritual as a non-commitment placeholder.
#   - The bag left behind: Tessa did not know how much of her was in the
#     room until she tried to take herself out. The scene's quiet horror.
#   - Aeron wipes his mother's name: the most OB thing he has done to date.
#     No ceremony, no witnesses, no speech. A sleeve. A cuff. A stain he
#     does not clean. Buried administratively. "That is the cleanest way
#     to say it."
#   - The two of them never occupy the room simultaneously. The scene is
#     structured around the miss -- Tessa leaves, Aeron arrives, each acts
#     on the board alone, neither knows the other was there. OB intimacy
#     is not shared ritual; it is parallel ritual in an empty room.
# cann.character_moments:
#   - Tessa: "Erasing is not a fix. Erasing is a provocation that buys one
#     shift." The triage voice. "I do not know if I am coming back for the
#     lamp. That is the honest state."
#   - Aeron: "My mother has been buried administratively. By her son. In a
#     wing her son's co-command authorized. On a board whose header her
#     son's co-command corrected." The Marcus-idiom clarity.
# cann.callbacks:
#   - a3_s19_the_weight_ob: the board methodology, both columns, "she counts
#     everyone." Here the counting is interrupted by external overwrite.
#   - a3_s10_tessa_friction_ob: "Discipline isn't healing." Tessa's thesis
#     under institutional capture -- the ritual has become the discipline.
#   - a3_s12_the_oath_ob: Nyra's restructuring -- the wing is a product of
#     the oath she administered. The bolts that hold the board to the wall
#     are an indirect consequence of that oath.
#   - a3_s07_terms_of_order_ob: Nyra integrating command. The coordinators
#     who made the overwrite possible are her hires.
#   - Liora walking at the end of Act 3: the precipitating event that put
#     LIORA RYLAN on both columns. Aeron resolves the duplication by
#     erasure, not by asking.
# cann.block_status:
#   - STATE BEAT (OB). No player choice. The route thesis is delivered
#     through action, not decision. Both characters act alone in the same
#     room at different times.
# cann.requires_followup:
#   - The lamp: does Tessa come back for it? The tp_seed tracks the question.
#   - The bag: same question, more urgent. A coat is easier to abandon than
#     a medical kit.
#   - The board: will the dead column grow? Will OPERATIONAL be upgraded to
#     a printed label? Who inherits the board if Tessa walks?
#   - Aeron's cuff: the ink stain. Does it show in a later scene? Does anyone
#     notice? Does Nyra? Does he wash it? (He did not, in this scene.)
#   - The administrative burial: Aeron has told no one. Does Tessa eventually
#     notice Liora is off the left column? What does she do when she does?
