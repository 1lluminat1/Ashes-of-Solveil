# =======================================================
# ACT 3 - Scene 12: Corridor Op (Empathy Path)
# File: a3_s12_corridor_op_emp.rpy
# Type: OPERATION + NARRATOR AWARENESS BEAT
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s12_corridor_op_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s12_corridor_op_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28mm, handheld with purpose — tight and kinetic during the operation,
    #         widening for the briefing and aftermath. Drift increases during the extraction
    #         sequences (3-5%), locks during Aeron's command moments (tripod-steady).
    #         Aftermath: back to 40mm, static, contemplative.
    # LIGHTING: Briefing — war room amber and green. Operation — tunnel emergency strips,
    #           cold blue service lighting, flashlight beams cutting dust. Exit point —
    #           exterior grey dawn. Aftermath — soft amber, base interior.
    # SFX: Briefing loop — war room ambient. Operation: boots on metal grating, distant
    #       patrol echoes, Ghostline relay crackle, civilian breathing (200 people trying
    #       to be quiet). Exit point: wind, Tessa's med-kit clasps. Aftermath: base ambient.
    #       One-shots — radio click, flashlight switch, child crying (quickly shushed),
    #       patrol drone overhead (muffled through tunnel ceiling), metal door latch.
    # FX/COMP: Briefing: holo-map with patrol overlay and 47-second window highlighted.
    #          Operation: tunnel environment — pipes, conduit, narrow passages.
    #          Group markers on the tactical display ticking through in batches of 20.
    # BLOCKING: Briefing: full team around command table. Operation: Aeron at the primary
    #           junction, Selene on overwatch, Zira scouting ahead, Noelle at comms coordination,
    #           Lyra at the midpoint checkpoint, Tessa at the exit triage station.
    #           Aftermath: team back at base. Scattered but present.
    # CANON: Mid-scale operation. 200 civilians extracted. The operation Aeron designed using
    #        his own Echelon training — the thing Marcus built turned against him.
    #        Narrator Awareness beat in the aftermath. Poly nudge at close.
    # FACE: Aeron — command focus during operation, something cracking open in the aftermath.
    #        Team — each in their element: Selene commanding, Zira sharp, Noelle precise,
    #        Lyra steady, Tessa efficient.

    # ========= VOICE BASELINE =========
    # EMP cadence throughout, but clipped during operation (tactical compression).
    # Briefing: measured, deliberate. Operation: short sentences, commands, sensory fragments.
    # Aftermath: slower. The sentences lengthen as the adrenaline drains.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - PRE-DAWN]

    #scene bg_war_room_emp with dissolve
    #play ambient "sfx/ambient/war_room_planning.ogg" fadein 2.0

    # ========== PHASE 1 — THE BRIEFING ==========

    "Five faces around the command table. The holo-map shows the Sector 7 corridor — Echelon patrol routes in red, civilian shelters in amber, the service tunnel network in blue."

    "Two hundred people on the far side of that corridor. Waiting."

    sel "Noelle's latest sweep confirms the shelter population. Two hundred and six, to be precise. Twelve children under ten. Thirty-one over sixty. The rest working age."

    n "Echelon has tightened the surface corridor since the counter-strike. Standard twelve-minute rotation with overlapping coverage on the southern approach."

    z "So the surface is a kill box."

    n "Effectively, yes."

    "Aeron stands. Puts both hands on the table. The patrol routes pulse red under his palms."

    a "I designed this sweep pattern."

    "The room stills."

    a "Third-year Glass Academy. Advanced Area Denial. The twelve-minute rotation with southern overlap was my capstone project."

    athought "I can feel them recalibrating. The moment when 'I was Echelon' stops being abstract and becomes tactical."

    a "There's a 47-second window every twelve minutes when the southern corridor is blind."

    sel "Forty-seven seconds. For two hundred people."

    a "Not all at once. Groups of twenty. The window resets each cycle. Ten groups, ten cycles, two hours total."

    "He traces the route on the holo-map. His finger moves through the service tunnels — the ones he identified during the Silence council, the ones that don't appear on any Echelon map."

    a "We enter through the maintenance access at Junction 14. The service tunnel runs parallel to the surface corridor for three hundred meters. Every twelve minutes, the southern patrol rotates north — that's our window to move one group from the tunnel exit to the extraction point."

    a "Selene runs overwatch from the Junction 14 observation post. Zira scouts two junctions ahead — any deviation from the patrol pattern, she signals and we hold."

    a "Noelle coordinates timing from here. She tracks the rotation cycle and calls the window."

    a "Lyra holds the midpoint checkpoint. If a group gets separated, she keeps them together and routes them to the next window."

    a "Tessa sets up triage at the exit point. Two hours of moving scared people through narrow tunnels — there will be injuries."

    sel "And you?"

    a "I'm at the primary junction. Reading the patrol patterns in real time. If anything changes, I adjust."

    athought "Because I know how those patrols think. I trained to think like them."

    athought "The difference is what I'm using it for."

    sel "Questions?"

    z "What if the 47-second window tightens?"

    a "I'll know before it happens. The rotation adjustment takes thirty seconds to propagate through the southern line. I'll read the shift and call the hold."

    z "How?"

    a "Because I wrote the propagation protocol. I know the lag."

    "Zira grins. Sharp. Predatory."

    z "I love it when you're terrifying for our side."

    $ npc_remember("Zira", "aeron_used_glass_training_for_extraction", tone="pleased_vicious")

    # ========== PHASE 2 — THE OPERATION ==========

    # VISUAL: Transition to tunnel environment. Dark. Cold. The sound of 200 people
    # breathing in the dark.

    #scene bg_service_tunnel_dark with dissolve
    #play ambient "sfx/ambient/tunnel_operation.ogg" fadein 1.5

    "The service tunnels smell like coolant and rust. Emergency strips every ten meters — blue-white, barely enough to see by."

    "The first group is already at the junction. Twenty civilians. A family of four at the front. The father's hand on his daughter's shoulder. Tight."

    athought "She's maybe eight. Eyes too wide. She doesn't understand why they're in a tunnel at 0400. She just knows the adults are afraid."

    n "(radio, crisp) Window opens in thirty seconds. Southern patrol approaching rotation point."

    a "(radio) Group One, ready."

    "Twenty people in the dark. Breathing. Waiting."

    n "(radio) Window open. Forty-seven seconds."

    a "Move."

    "They move. Not running — walking fast. The father carries his daughter now. Someone at the rear stumbles on a pipe junction. The person behind catches them."

    "Forty-seven seconds. They clear the exit zone."

    athought "One."

    #play sound "sfx/one_shot/radio_click.ogg"

    # --- GROUP PROGRESSION (compressed) ---

    "Group Two. Forty-seven seconds. Clean."

    "Group Three. A woman with a broken wrist — Tessa splinted it before they entered. She cradles it against her chest and moves without complaint."

    "Group Four. Forty-seven seconds. An elderly man at the rear. Slow. Lyra appears beside him at the midpoint, matches his pace, keeps him in the window."

    athought "She doesn't hurry him. She steadies him. The difference matters."

    "Group Five. Clean."

    "Group Six — the problem."

    # --- THE COMPLICATION ---

    n "(radio, urgent) Pattern deviation. Southern patrol is running thirty seconds early."

    athought "Thirty seconds early. The window just shrank from forty-seven seconds to seventeen."

    a "(radio) All groups hold. Repeat — hold position."

    "Group Six is in the tunnel. Halfway to the exit zone. Twenty people frozen in the dark."

    athought "Seventeen seconds. Not enough. Not for twenty people with children and elderly."

    athought "Think. The propagation protocol. Early rotation means a sector commander adjusted the timing — probably in response to anomalous noise from our first five groups."

    athought "The adjustment will propagate north in thirty seconds. That means the northern patrol will shift too — opening a secondary gap."

    a "(radio) Noelle. Northern patrol status."

    n "(radio) Unchanged. Thirty seconds to propagation sync."

    a "(radio) When the northern patrol adjusts, there's a twelve-second overlap gap on the western access. Can you confirm?"

    n "(radio, pause) Confirmed. Western access blind for twelve seconds beginning in... forty-one seconds."

    a "(radio) Group Six, new route. Western access in forty-one seconds. Zira, I need you at the western junction."

    z "(radio) Already here."

    athought "She anticipated it. Of course she did."

    a "(radio) Group Six, on my signal. Move fast."

    "Thirty-seven seconds of waiting in the dark. A child whimpers. Someone whispers comfort in a language Aeron doesn't speak."

    a "(radio) Now."

    "They move. Twenty people through the western access. Twelve seconds. The last person clears the threshold with two seconds to spare."

    athought "My heartbeat is louder than the tunnel ambient."

    athought "Two seconds. We had two seconds."

    # --- REMAINING GROUPS ---

    "He recalculates. The adjusted rotation gives them a new pattern — shorter windows, but the western route is viable now."

    "Group Seven. Western access. Clean."

    "Group Eight. Aeron reads a second adjustment coming — calls the hold before Noelle's instruments confirm it."

    n "(radio) How did you—"

    a "(radio) I wrote the adjustment protocol. The lag between cycles is predictable if you know the base frequency."

    "Group Nine. Clean. Lyra steady at the midpoint. Tessa treating a sprained ankle at the exit."

    "Group Ten. The last twenty."

    "An older woman at the front. She pauses at the junction. Looks back at the tunnel they came through. The shelter they left."

    "She touches the wall. Then walks forward."

    athought "Two hundred and six people."

    athought "Every one of them through."

    #play sound "sfx/one_shot/tunnel_door_seal.ogg"

    # ========== PHASE 3 — EXIT AND TRIAGE ==========

    # VISUAL: The exit point. Grey dawn. Tessa's triage station — organized chaos.
    # People sitting on the ground, on supply crates, on each other.

    #scene bg_extraction_exit_dawn with dissolve
    #play ambient "sfx/ambient/dawn_wind_crowd.ogg" fadein 2.0

    "The exit point. Dawn breaking grey over the industrial sector. Two hundred and six people in the open air for the first time in three weeks."

    "Tessa moves through them like current through wire — efficient, warm, hands never idle."

    t "Sprained ankle, third crate. Broken wrist — you, sit down, let me check the splint. Dehydration cases — water station is to the left. Small sips."

    "Lyra is with the children. Seven of them clustered around her. She's not speaking — just present. One child holds the hem of her coat."

    "Zira is already back on the Ghostline, coordinating the follow-up transport. Her voice is clipped and precise."

    z "(radio) Transport Two, bearing north-northwest. Pickup in twelve minutes. Have the second group ready."

    "Selene stands at the perimeter. Scanning. The commander's vigil — making sure the extraction point stays clean."

    "Noelle is still at her station, but her hands have stopped moving. She's watching the people. Counting them. All of them."

    n "(quiet, to no one) Two hundred and six."

    $ canon_set("corridor_op_success", True)
    $ flag("corridor_op_complete", True)

    # ========== PHASE 4 — AFTERMATH + NARRATOR AWARENESS ==========

    # VISUAL: Later. Back at base. The team scattered in the common area.
    # The particular quiet of people who just did something enormous.

    #scene bg_common_area_emp with dissolve
    #play ambient "sfx/ambient/base_quiet_post_op.ogg" fadein 2.0

    "The base is quiet. The particular quiet that follows an operation — not silence, but the sound of adrenaline leaving the body. Chairs creaking. Water poured. The small rituals of coming down."

    "Aeron sits at the edge of the common area. The operation replay scrolling behind his eyes."

    athought "Operation successful. Two hundred and six extracted. Zero friendly casualties."

    athought "Seventeen-second window adjustment. Two-second margin on Group Six."

    athought "The patrol adaptation protocol I wrote at the Academy — the one I got commended for — used against the system that taught it to me."

    menu:
        "The number sits in his mind. Two hundred and six."

        "Those weren't extracted. They were saved.":
            $ choice_and_dev(
                _current_scene_id, "_saved_framing", "EMP", factor=1,
                next_scene_label=None,
                note="Reframes tactical language as human language."
            )
            jump .saved

        "Confirmed. Extraction complete.":
            $ choice_and_dev(
                _current_scene_id, "_tactical_framing", "OB", factor=1,
                next_scene_label=None,
                note="Maintains operational distance."
            )
            jump .tactical

        "Those are my father's words. Where are mine?" if tp_narrator_available():
            $ tp_narrator_acknowledged(_current_scene_id)
            jump .narrator_awareness

    # --- BRANCH: SAVED FRAMING ---
    label .saved:

        athought "Those weren't extracted."

        athought "They were saved."

        athought "A woman touched the tunnel wall before she walked into the dawn. A father carried his daughter through a forty-seven-second window. An old man walked slowly and someone matched his pace."

        athought "The word 'extracted' doesn't hold any of that."

        athought "Saved. They were saved. By people who chose to be here."

        jump .post_choice

    # --- BRANCH: TACTICAL FRAMING ---
    label .tactical:

        athought "Confirmed. Extraction complete."

        athought "Two hundred and six individuals relocated from hostile-adjacent shelter to secured transport corridor. Zero casualties. Two minor injuries. Operation duration: two hours fourteen minutes."

        athought "Clean. Efficient. Exactly as planned, minus the sixty-second adaptation on Group Six."

        athought "The report writes itself."

        athought "I wonder when that started feeling like a problem."

        jump .post_choice

    # --- BRANCH: NARRATOR AWARENESS (TRUE PATH) ---
    label .narrator_awareness:

        athought "Two hundred and six extracted. Two hundred and six saved. Both are true."

        athought "But 'extracted' is Marcus's word. Clinical. Tactical. The word of someone who moves people like materiel."

        athought "'Saved' is Kael's word. Idealistic. Righteous. The word of someone who believed sacrifice was its own justification."

        athought "What's MY word for what just happened?"

        "He sits with it. The common area hums around him."

        athought "I don't have one yet."

        athought "And that's the first honest thing I've thought all day."

        athought "Marcus would have a word by now. Kael would have three. Selene would have already filed the report."

        athought "I'm sitting here without a word for what we did, and for the first time, that feels like the right place to be."

        athought "The answer isn't borrowed. It isn't ready. It might not come today."

        athought "But when it does, it'll be mine."

        jump .post_choice

    # ========== PHASE 5 — TEAM PROCESSING + POLY NUDGE ==========
    label .post_choice:

        "Tessa is cleaning her field kit. Methodical. The instruments laid out in order of use, wiped down, returned."

        t "Fourteen minor injuries. Two sprains. One panic episode resolved with grounding exercises."

        t "For two hundred people moving through tunnels in the dark, that's exceptional."

        "She looks at Aeron."

        t "You should know that."

        "Lyra is in the doorway. The children have been settled in the temporary shelter wing. Her coat hem is wrinkled where the child held it."

        l "The families are safe. The children are asleep."

        "A pause."

        l "One of them asked if we'd come back for them if the soldiers came again."

        a "What did you say?"

        l "I said yes."

        athought "She said it like a fact. Not a promise — a fact."

        athought "Because for Lyra, the distinction doesn't exist."

        "Selene enters. The commander's debrief."

        sel "Clean operation. Two-second margin on Group Six — tighter than I'd like."

        a "Tighter than anyone would like."

        sel "But you read the pattern shift before Noelle's instruments caught it."

        a "I wrote the protocol."

        sel "That's exactly my point."

        "She sets a datapad on the table."

        sel "Aeron, what you did tonight — using Echelon's own framework against them — that's not something any of us can replicate."

        sel "That's yours."

        athought "Yours."

        athought "The word lands differently tonight."

        # --- POLY NUDGE ---

        "Zira is at the door. She's been waiting — how long, Aeron isn't sure. Watching."

        z "If I take his debrief, you still get your evening?"

        "She's not looking at Aeron. She's looking at Lyra."

        l "...thank you for asking. Yeah."

        z "Good."

        "Zira crosses the room. Settles into the chair beside Selene. Business-mode."

        z "Debrief. Start with the rotation adjustment on Group Six."

        $ nudge_poly(1)

        athought "Something just happened that I don't have a model for."

        athought "Noelle would call it an unmodeled variable."

        athought "I just watched Zira check with Lyra before claiming my time."

        athought "Like there's an economy between them. An understanding I wasn't consulted about and don't need to be."

        "He sits down for the debrief."

        "The base hums. Two hundred and six new lives inside its walls."

        "He still doesn't have a word for what happened tonight."

        "He's starting to think that might be the point."

        #stop ambient fadeout 2.0
        #scene black with fade

    # ========= STATE UPDATES =========
    $ npc_remember("Selene", "corridor_op_clean_extraction", tone="professional_respect")
    $ npc_remember("Tessa", "corridor_triage_fourteen_minor", tone="clinical_satisfaction")
    $ npc_remember("Lyra", "promised_children_return", tone="quiet_conviction")
    $ npc_remember("Zira", "coordinated_with_lyra_on_aeron_time", tone="pragmatic_courtesy")
    $ npc_remember("Noelle", "counted_all_206", tone="quiet_completeness")
    $ flag("corridor_op_206_saved", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s12_corridor_op_emp
# cann.chapter: Act III, Phase II — Deepening (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase II. After Empirical Tenderness (s11).
#   - Mid-scale operation using the service tunnels identified in the Silence (a3_s04a).
#   - Echelon counter-strike (a3_s07) has tightened patrols. This is the response.
# cann.what_happened:
#   - Phase 1 (Briefing): Aeron identifies 47-second patrol window using his own Glass Academy
#     capstone project. Plan: 10 groups of 20, service tunnels, 2-hour extraction.
#     Team deployed: Selene overwatch, Zira scout, Noelle timing, Lyra midpoint, Tessa triage.
#   - Phase 2 (Operation): Groups 1-5 clean. Group 6 — patrol shifts 30 seconds early.
#     Window shrinks from 47 to 17 seconds. Aeron reads the propagation protocol he wrote,
#     identifies a 12-second western access gap. Group 6 through with 2 seconds to spare.
#     Groups 7-10 via adjusted route. All 206 extracted.
#   - Phase 3 (Exit): Dawn. Tessa running triage. Lyra with children. Zira on transport.
#     Selene on perimeter. Noelle counting. "Two hundred and six."
#   - Phase 4 (Narrator Awareness): Three-option menu —
#     "Saved" (EMP): reframes tactical language as human language.
#     "Extraction complete" (OB): maintains operational distance.
#     "Those are my father's words" (TP): narrator awareness. "I don't have one yet.
#      And that's the first honest thing I've thought all day."
#   - Phase 5 (Team + Poly): Debrief. Selene: "That's yours."
#     Poly nudge: Zira checks with Lyra before taking Aeron's debrief time.
# cann.aeron_state:
#   - In command during the operation. Reading patterns he designed. Using Glass training
#     against Echelon — the thing Marcus built, turned.
#   - Aftermath: searching for his own language. "Extracted" is Marcus's. "Saved" is Kael's.
#   - TP variant: "I don't have one yet. And that's the first honest thing I've thought all day."
# cann.path_tracking:
#   - Saved framing: EMP factor=1. Human language over tactical.
#   - Tactical framing: OB factor=1. Operational distance maintained.
#   - Narrator awareness: tp_narrator_acknowledged(). "Where are mine?"
#   - All paths: canon_set("corridor_op_success"), flag("corridor_op_complete").
#   - nudge_poly(1) on Zira/Lyra coordination beat.
# cann.thematic_flags:
#   - The capstone project: Aeron's Glass Academy work used against Echelon.
#     "I designed this sweep pattern." — The thing that made him dangerous THERE
#     is what makes him indispensable HERE.
#   - 47-second window: precision under pressure. The ticking clock as narrative engine.
#   - Group Six complication: 2-second margin. The razor edge of real operations.
#   - "What's MY word?": The narrator awareness beat. Marcus has words, Kael has words,
#     Selene has words. Aeron's honest answer is that he doesn't have one yet.
#   - Poly nudge: Zira/Lyra coordination. An economy of care Aeron wasn't consulted about.
#     This is the poly arc building — the women organizing themselves around shared investment.
# cann.character_moments:
#   - Aeron: Reading patrol adjustments before instruments confirm — the Glass in him
#     serving the person he's becoming. "I wrote the protocol."
#   - Selene: "That's yours." — Recognizing Aeron's unique value to Phoenix.
#   - Zira: "I love it when you're terrifying for our side." During briefing.
#     "If I take his debrief, you still get your evening?" — The poly architect.
#   - Lyra: Matching the old man's pace. "I said yes" to the child. Quiet conviction.
#   - Tessa: "For two hundred people in the dark, that's exceptional. You should know that."
#   - Noelle: "(quiet, to no one) Two hundred and six." — Counting matters.
# cann.callbacks:
#   - a3_s04a: The Silence — service tunnels identified there, used here.
#   - a3_s07: Echelon counter-strike — the tightened patrols that necessitate this operation.
#   - Glass Academy capstone project — Aeron's tactical training weaponized against its source.
#   - a3_s05: Two Healers — Tessa's field triage skills in action.
# cann.block_status:
#   - OPERATION SCENE + NARRATOR AWARENESS BEAT. Three-way choice with TP option.
# cann.requires_followup:
#   - 206 new civilians in Phoenix Base — resource strain, integration challenges.
#   - Echelon will notice 206 missing people. Response incoming.
#   - Narrator awareness thread: what IS Aeron's word? Does he find it?
#   - Poly arc: Zira/Lyra coordination evolving. nudge_poly accumulating.
#   - The 2-second margin: Selene will want wider margins. Operational tension.
