# =======================================================
# ACT 4 - Scene 01: The Cold Room (Obedience Path)
# File: a4_s01_the_cold_room_ob.rpy
# Path: OB
# Type: ACT 4 OPENER / TITLE CARD
# Character Focus: Aeron, Nyra (silent unit)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s01_the_cold_room_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy

label a4_s01_the_cold_room_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. Institutional distance. Opens on the strategic room door
    #         from the corridor side -- wide, patient. We do not enter with Nyra; we wait
    #         with her. When the door finally unlocks, the camera moves inside for the
    #         first time, also patient. Coverage inside is symmetrical singles. Aeron at
    #         one end of the table, Nyra at the other. No two-shot. The geometry is the
    #         scene. A single insert on the plan as Aeron marks it. Return to the singles.
    # LIGHTING: Strategic room. Overhead strips at 30% -- someone (Aeron) dimmed them.
    #           The tactical display against the far wall is dark. Cold key from the
    #           displays that are still live. Blue over grey concrete. Nyra's face lit
    #           from below by the table surface. Aeron's from above by a single pendant
    #           he did not turn off.
    # SFX: Loop -- base hum (coldest variant), ventilation drone, the distant echo of
    #      boots on the upper corridor. One-shots -- Nyra's single knock (measured),
    #      the door mechanism (heavy), a chair shift that never comes, the plan sliding
    #      across the table, the pen mark (small, final), the plan sliding back.
    # FX/COMP: The strategic room has not been slept in but has been lived in -- a
    #          coffee cup from two days ago, operational maps layered three deep on
    #          the table. The door's interior lock is thrown. A manual bolt. Aeron
    #          set it sometime in the night.
    # BLOCKING: Phase 1 -- the corridor. Nyra arrives. Single knock. Waits. Does not
    #           knock again. Walks the three steps to the table inside her head. She
    #           stays outside for twenty minutes, then walks to the table anyway --
    #           in memory, in intention, the way she will when the door opens. The
    #           cut is clean: twenty minutes later, the bolt draws back. She enters.
    #           Crosses to the table. Sits. Waits. Aeron comes out of the strategic
    #           room's back alcove -- he has been standing there, not sitting. He
    #           joins her at the table. The plan is already between them.
    # CANON: ACT 4 OB OPENER. Morning after a3_s24 -- the refusal. Aeron has not slept.
    #        He has not returned to his quarters. He is in the strategic room with the
    #        door locked from the inside. Nyra does not need to be invited. She comes
    #        because this is the work. The scene is the establishment of a unit that
    #        does not require words. The title card drops between Phase 3 and Phase 4.
    # FACE: Nyra -- composed, patient, expressionless in the way that is not a mask
    #        but an absence of need. Aeron -- not grief. Not exhaustion. A stillness
    #        that has been rehearsed into place during the night. The mask is tighter
    #        than it was yesterday. The mask fits better.

    # ========= VOICE BASELINE =========
    # OB Aeron: Almost no dialogue. One line. The scene's weight lives in athoughts and
    #           in the stage direction of the single mark on the plan. The mark is
    #           his voice. The mark is his entire voice.
    # Nyra: Three or four lines total. Operational. The shortest she has ever been.
    #       Her silence is not conservation. Her silence is the expected register.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - STRATEGIC ROOM - MORNING]
    # Morning after the refusal. 0547. The base is running dawn shift.

    #scene bg_strategic_room_ob_dawn with dissolve
    #play ambient "sfx/ambient/base_hum_coldest.ogg" fadein 2.0

    # ========== PHASE 1 -- THE DOOR (CORRIDOR SIDE) ==========

    "0547. The corridor outside the strategic room is empty."

    "Dawn shift is running. The overheads are at operational grey. The base has the early-morning quiet of a machine that has decided to function without asking whether it should."

    "The strategic room door is closed."

    "The interior bolt is thrown. The status light is red."

    "Nyra stops in front of the door. Her uniform is pressed. Her boots are polished. The datapad under her arm is the exact datapad she was carrying when she left her own quarters forty minutes ago."

    "She knocks."

    "Once."

    #play sound "sfx/door_knock_single.ogg"

    "The knock is measured. Not soft, not hard. The cadence of a woman announcing presence without requesting permission."

    "She waits."

    "Nothing answers."

    # --- NYRA INTERIOR (CORRIDOR) ---

    nythought "He is in there."

    nythought "The bolt is thrown from the inside. The status indicator confirms occupation. The corridor patrol logged him entering at 0114 and has not logged him leaving."

    nythought "He has not slept. He has not returned to his quarters. He has not eaten since the meeting at the safe house."

    nythought "I do not knock again."

    nythought "A second knock would be a request. This is not a request."

    "She steps back from the door. Not away -- back. One pace. Her hands clasp behind her at parade rest. The datapad tucked against her side."

    "She waits."

    "She does not pace. She does not check her wrist. She does not look at the corridor cameras."

    "She waits the way a sentry waits."

    # ========== PHASE 2 -- THE WAIT ==========

    "0552."

    "0558."

    "0603."

    "The corridor's early-shift foot traffic begins. Two junior analysts pass the strategic room door, see Nyra standing at parade rest, and do not slow down. They have learned not to slow down for her."

    "A supply runner with a crate of ration packs takes the long route around the corridor to avoid passing her entirely. Nyra does not look at the runner."

    "0611."

    "The ventilation cycles. The overhead strips tick through the hourly calibration. The status light on the door stays red."

    nythought "Twenty minutes is a threshold I set for myself in the Glass Academy. The length of a standard breach window. The length of a slow execution. The length of time a disciplined soldier can wait without the waiting becoming an argument."

    nythought "After twenty minutes the waiting becomes a statement."

    nythought "I am willing for it to become a statement."

    "0618."

    "The status light does not change."

    "She waits."

    # ========== PHASE 3 -- THE BOLT ==========

    "0622."

    #play sound "sfx/door_bolt_interior_slow.ogg"

    "The interior bolt moves."

    "It is not a dramatic sound. It is a mechanical sound. The slow draw of a steel bar across a steel track. Unhurried. The bolt was thrown by a man who was not in a hurry, and it is being drawn back by the same man at the same speed."

    "The status light flips from red to green."

    "The door does not open."

    "Nyra steps forward. One pace. She places her hand flat against the door plate."

    "The door hisses open."

    # ========== PHASE 4 -- INTERIOR ==========

    #scene bg_strategic_room_ob_interior with dissolve

    "The strategic room is dim."

    "Someone -- Aeron -- has taken the overhead strips down to 30%. The tactical display against the back wall is dark. The only full-brightness light source is the pendant over the central table. A cold pendant, cold light. The pool it throws is the size of the table and no larger."

    "Outside the pool, the room is blue-grey. Institutional. A concrete box with a table in it."

    "The table is not clean. Operational maps are layered three deep across its surface. A coffee cup from forty-eight hours ago sits near the west edge, the residue dark and crusted. The plan from last night's patrol briefing is still open at the north end, half annotated, abandoned."

    "Aeron is not at the table."

    "He is standing at the back of the room, in the alcove where the dead tactical display meets the corner. His back is to the door. His hands are flat against the dark glass of the display. The posture of a man who has been pressing his palms against something cold for hours."

    #show aeron strategic_alcove_back with dissolve

    "Nyra enters."

    "She does not greet him."

    "She walks to the table. She does not take Aeron's chair at the head. She takes the chair opposite -- the analyst's chair, the one a briefer uses. She sits. She places the datapad in front of her. She does not open it yet."

    "She waits."

    "Aeron does not turn from the alcove."

    "Thirty seconds pass."

    "Forty."

    # --- AERON INTERIOR ---

    athought "She is here."

    athought "I did not summon her. I did not need to."

    athought "I bolted the door at 0114. I have not spoken to anyone since. I walked from the transport bay to this room and I closed the door behind me and I threw the bolt and I have stood in this alcove for five hours and forty-one minutes."

    athought "I did not sleep. I did not sit. I did not cry. I did not think about her face."

    athought "That is not true."

    athought "I thought about her face once. At 0326. The moment where she was turning toward the door and the light caught the edge of her jaw. The line of her jaw is my line of jaw. The Glass gave me the discipline but it did not give me that line."

    athought "I thought about her face once and then I put it down."

    athought "She walked. I am still here. That is all the accounting this costs."

    tp_seed("a4.ob.cold_open")

    # --- THE TURN ---

    "Aeron turns from the alcove."

    "The turn is not slow. It is not reluctant. It is the turn of a man who has completed a task that required him to face the corner, and who now has a new task that does not."

    "He walks the five paces to the table. Each pace is measured. The exhaustion in his body has been organized into posture. The night has not softened him. The night has compressed him."

    "He takes his chair at the head of the table."

    "He does not look at Nyra. He looks at the surface of the table. The operational maps. The coffee cup. The abandoned annotation from forty-eight hours ago."

    "He does not say good morning."

    "He does not say thank you."

    "He does not say I had a difficult night."

    "He waits."

    # ========== PHASE 5 -- THE PLAN ==========

    "Nyra opens the datapad."

    "She slides it across the table, flat, two-handed. The datapad comes to rest between them, angled toward Aeron. The screen is a sector consolidation plan. Seven days of operations, mapped with the tight clean geometry of someone who built it overnight."

    ny "Next week."

    "Two words. The first words spoken in the strategic room since 0114."

    "Aeron does not reach for the datapad."

    "He looks at it from across the table. His eyes move across the plan the way a surgeon's eyes move across an x-ray -- efficient, intake-first, the assessment happening faster than consciousness can narrate it."

    athought "Sector 4 consolidation. The supply depot corridor we took ten days ago, extended north. Sector 9 -- she has added Sector 9, which means she is anticipating the Echelon response lag and moving us into the space before they finish rebuilding."

    athought "Three strike windows. Two feints. One relocation of the Ghostline western relay."

    athought "She built this in four hours. Maybe three."

    athought "It is better than anything we produced when Selene was alive."

    athought "I should flinch at that thought."

    athought "I do not."

    "He reaches for the datapad. Draws it toward him. Reads it properly now. The room is silent except for the base hum."

    # --- NYRA, WAITING ---

    nythought "He is reading it the way Marcus used to read operational plans. I have seen Marcus do this. Not in person -- in the Glass Academy instructional footage. The Glass kept his debriefs as teaching material. Three hours of Marcus reading plans and making one mark."

    nythought "The mark is the teaching."

    nythought "Aeron does not know he is being taught."

    nythought "I do not need him to know."

    # --- THE READ ---

    "Aeron reads the plan for four minutes and eleven seconds."

    "He does not ask questions. He does not pause to look up at her. He does not tap the display to zoom in on any of the three strike windows or the two feints or the Ghostline relay relocation."

    "He reads the whole thing in one pass."

    "Then he reads it again."

    athought "The Sector 9 entry is two days too early."

    athought "She has us entering Sector 9 on day three. Echelon's rebuild cycle is approximately seventy-two hours from the Sector 4 aftermath. If we enter on day three we collide with their pickets while they are still rotating personnel."

    athought "If we enter on day five, they are settled and over-confident, and the intercept geometry favors us by a factor of approximately one point six."

    athought "She knows this. She built this on purpose. She is testing whether I will catch it."

    athought "Or she is offering me the test and the answer in the same document, and expecting me to make the mark."

    athought "Either answer resolves the same way."

    # ========== PHASE 6 -- THE MARK ==========

    "Aeron takes a stylus from the tray beside the datapad."

    "He makes one mark."

    #play sound "sfx/stylus_single_mark.ogg"

    "The mark is small. It lands on the day-three entry for Sector 9. A single stroke -- not a crossout, not an annotation. He draws a short horizontal bar through the '3' and writes '5' above it."

    "He sets the stylus down."

    "He slides the datapad back across the table."

    "The datapad comes to rest in front of Nyra, angled toward her now, the same flat two-handed geometry she used when she gave it to him."

    "He still has not spoken."

    # ========== PHASE 7 -- THE READ-BACK ==========

    "Nyra looks down at the datapad."

    "She reads the mark."

    "Her eyes move across the plan once -- not to check his correction, but to confirm that she knows what his correction means. The Sector 9 entry moves from day three to day five. The strike window on day four is now the primary rather than the secondary. The Ghostline relay relocation shifts to day six, because the day-five Sector 9 entry consumes the day-six bandwidth she had originally allocated to the relay."

    "Three downstream changes, all of them forced by the single number he wrote above the '3.'"

    "She reads the mark and she reads the three downstream changes and she finishes reading the plan in seven seconds."

    "She nods once."

    "The nod is small. It is not acknowledgment of a commander's correction. It is acknowledgment of a colleague who saw what she saw."

    nythought "He caught it."

    nythought "Good."

    # --- THE RECIPROCATION ---

    "Nyra does not rewrite the plan. She does not say I will update the downstream entries. She does not say you are right. She does not say thank you."

    "She taps the datapad twice. The plan refreshes. The day-five Sector 9 entry populates. The Ghostline relay shifts to day six. The day-four strike promotes to primary."

    "The downstream changes execute in three seconds."

    "The plan is now the plan Aeron described by writing a single number."

    "Nyra closes the datapad."

    "She stands."

    # ========== PHASE 8 -- THE DEPARTURE ==========

    "Nyra picks up the datapad. Tucks it under her arm. The motion is the same motion she used when she entered."

    "She walks to the door."

    "At the threshold she pauses."

    "Not for a line. Not for a look back. The pause is tactical -- she is waiting for the corridor sensor to register her intention to cross, so the door opens without her having to request it."

    "The door opens."

    ny "I will be in the operations room at 0800."

    "Four words. Operational. Not an invitation. Not a promise. A logistical statement -- this is where she will be, and he knows where to find her if he needs her, and the fact that she has told him where she will be is the only warmth this scene is going to permit."

    "She steps through the door."

    "The door closes."

    "The bolt on the interior does not re-engage. Aeron has not thrown it again. That is the only thing in the scene that has changed from the beginning."

    # ========== PHASE 9 -- THE MOTHER BEAT ==========

    "Aeron sits alone at the strategic table."

    "The coffee cup from forty-eight hours ago. The layered maps. The empty chair across from him where Nyra was sitting forty seconds ago. The datapad is gone, but the plan is already uploaded to the tactical system -- he can feel the update ripple through the base's planning network in the low sub-audible frequency of the ventilation."

    "The next seven days are now the seven days Nyra built. Modified by one mark. His mark."

    "He has not spoken a word this morning."

    "The pendant light over the table holds him in its small cold pool."

    "He allows himself one beat."

    # --- THE BEAT ---

    athought "Liora."

    "The name in his head is not a sound. It is a shape. A face he has not looked at in five hours."

    athought "She was walking toward the door. The light caught her jaw. The line of the jaw was my line."

    athought "I do not let it move."

    "The beat is not a memory. It is a check -- the way a mechanic checks a gauge. Is the pressure rising? Is the pressure holding? Is the pressure in the green?"

    "The pressure is in the green."

    athought "She walked. I am still here. That is all the accounting this costs."

    athought "She refused to be my absolution."

    athought "I did not need absolution. I needed an operational plan for next week."

    athought "I have one."

    athought "The plan is better than anything I could have built while I was waiting for her forgiveness. The absence of the forgiveness is the condition under which the plan becomes possible."

    athought "That is not a bitter thought. That is an administrative thought."

    athought "I am becoming administratively fluent in what I did."

    "He closes his eyes."

    "Not to rest. To confirm that the inside of his head still looks the way he has arranged it to look. He opens them again after one second. The inside looks the way it should."

    "He stands."

    # ========== PHASE 10 -- TITLE CARD ==========

    "He gathers the forty-eight-hour coffee cup. Walks it to the disposal chute. Drops it. The cup is gone."

    "He returns to the table. Rolls the layered operational maps into a single tight cylinder. Places the cylinder in the archival tray. The table is now clear except for the pendant light and the surface and the chair."

    "He looks at the chair Nyra used. The analyst's chair."

    "He looks at his own chair. The head of the table."

    "He does not sit in either of them."

    "He walks to the door."

    "The corridor beyond is still dawn-shift quiet."

    "He steps through."

    #stop ambient fadeout 3.0
    #scene black with fade

    pause 1.5

    centered "{size=+24}CHAPTER IV{/size}"
    pause 0.8
    centered "{size=+14}Violence Normalized{/size}"
    pause 2.2
    scene black with fade

    pause 0.8

    # ========== PHASE 11 -- CORRIDOR COdA ==========

    #scene bg_phoenix_corridor_dawn with dissolve
    #play ambient "sfx/ambient/corridor_dawn_cold.ogg" fadein 2.0

    "The corridor outside the strategic room. 0631."

    "Aeron walks east. Toward the operations room. The pace is measured. The left hand does not tremor. He has not pressed it flat against anything this morning. It has not needed the pressure."

    athought "Nyra will be in operations at 0800. It is 0631. I have ninety minutes."

    athought "I will use them for a shower, a uniform change, two ration bars, and the dawn intel summary."

    athought "This is what a commander does on a morning after a refusal."

    athought "This is what a commander looks like the day he becomes something his mother could see from across a table at a neutral safe house and name by its correct name."

    athought "She named it."

    athought "I have not corrected the naming."

    "A junior analyst passes him in the corridor. Salutes. Aeron returns the salute with the exact angle and exact duration protocol requires."

    "The analyst does not notice anything unusual about the commander this morning."

    "That is the tell."

    # --- END ---

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("ob.aeron.mother_refusal", "processed_to_doctrine")
    $ canon_set("ob.aeron.nyra_unit_silent", True)
    $ flag("a4_ob_cold_open", True)
    $ flag("a4_started", True)
    $ rel_bump("Nyra", trust=1)
    $ npc_remember("Nyra", "cold_room_single_mark", tone="unit_without_words")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s01_the_cold_room_ob
# cann.chapter: IV -- Violence Normalized
# cann.chapter_start: True
# cann.path_tracking: OB
# cann.when_in_timeline:
#   - Morning after a3_s24_liora_ob (the refusal at the Outlander safe house).
#   - 0547 to 0631. Aeron has not slept, has not returned to his quarters, has
#     bolted the strategic room door from the inside and stood in the back alcove
#     for five hours and forty-one minutes.
# cann.what_happened:
#   - Nyra arrives at the strategic room at 0547. Knocks once. Waits at parade rest
#     for twenty minutes without knocking again.
#   - At 0622 Aeron draws the interior bolt. Nyra enters. Crosses to the table.
#     Sits in the analyst's chair (not his chair). Waits.
#   - Aeron turns from the alcove, sits, reads the plan she slides to him.
#   - The plan is a seven-day sector consolidation built in four hours. Better
#     than anything Phoenix produced when Selene was alive.
#   - Aeron makes one mark: the Sector 9 entry moves from day three to day five.
#     One numeric correction forces three downstream changes.
#   - Nyra reads the mark, updates the plan, nods once.
#   - No greeting. No thank you. No explanation. Four spoken words total from
#     Nyra ("Next week." / "I will be in the operations room at 0800.").
#     Zero spoken words from Aeron.
#   - Title card: CHAPTER IV -- Violence Normalized
#   - Coda: corridor walk at 0631. The junior analyst does not notice anything
#     unusual about the commander. That is the tell.
# cann.aeron_state:
#   - Has not slept. Not grieving. Has "organized the night into posture."
#   - The single beat allowed for his mother is a pressure check, not a memory.
#   - "She walked. I am still here. That is all the accounting this costs."
#   - "I am becoming administratively fluent in what I did."
#   - The mask is tighter than yesterday. The mask fits better.
# cann.thematic_flags:
#   - OPENER THESIS (OB Act 4): the regime establishing itself. Aeron and Nyra
#     as a unit that does not need words. The geometry IS the message.
#   - The single mark: Aeron's entire voice in this scene is one number
#     written above another number. One stroke. The stroke is his character.
#   - The pressure check: Liora's face as a gauge reading, not a memory. The
#     conversion of grief into administration.
#   - The absence of the forgiveness is the CONDITION under which the plan
#     becomes possible. OB belief: refusal is a kind of clearance.
#   - Nyra's silence: not a performance. The expected register. The unit's
#     baseline. Words are the exception now.
#   - "The next seven days are now the seven days Nyra built." The scene is
#     Aeron ratifying the shape of his own regime without saying the word.
# cann.character_moments:
#   - Nyra: Four spoken words. One nod. Parade-rest wait of twenty minutes
#     without a second knock. The doctrinal presence.
#   - Aeron: Zero spoken words. One stylus mark. One allowed beat for Liora
#     that resolves as a pressure check.
# cann.callbacks:
#   - a3_s24_liora_ob: The refusal. "I am my father's son." "I can see his
#     charts in the way you sit."
#   - a3_s07_terms_of_order_ob: "Your discomfort is noted but irrelevant."
#     That sentence has now become the entire operational register.
#   - a3_s08_perfect_execution_ob: "Seventy. I account for human error."
#     The forty-minute planning now compressed to four hours for a full week.
#   - a3_s12_the_oath_ob: The ceremonial intimacy rewrote doubt as impurity.
#     This scene demonstrates the rewrite has completed.
# cann.block_status:
#   - ANCHOR. Always plays on OB path at Act 4 opener. No branching. No choice.
#     The scene IS the decision -- made silently, ratified silently.
# cann.requires_followup:
#   - a4_s02_the_new_shape_ob: the council ratifies what this scene already
#     decided in private.
#   - a4_s03_marcus_adapts_ob: the accelerated tempo the plan in this scene
#     makes possible.
