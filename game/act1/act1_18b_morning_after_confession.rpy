# =======================================================
# ACT 1 - Scene 18b: Morning After Confession
# File: act1_18b_morning_after_confession.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_18b_morning_after_confession"
$ scene_mark(_current_scene_id, "entered")


label act1_morning_after_confession:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Slow reveal from floor-level; tight two-shots; wrist CU for Band-check; threshold hug option.
    # LIGHTING: Cold interior vs warm shard from window.
    # SFX LOOP: Building ventilation; faint city hum under silence.
    # BLOCKING: Apartment floor, early morning. Two bodies tangled from sleep.
    # PROP: Coffee cup; kettle; blood drop on floor.

    #scene bg_apartment_morning with fade

    # ========= WAKING =========

    "Morning light cuts through the window—sharp, unforgiving."

    "Waking slowly. Floor hard beneath me. Something warm against my side."

    # VISUAL: Tight two-shot on their tangle; shallow depth on hands over chest.

    "Lyra. Still here. Face pressed into my shoulder, our legs tangled, her hand resting on my chest—like we held on through the night without words."

    "Dark circles under her eyes. Even in sleep, tension in her jaw. But her breath... warm against my skin."

    athought "We fell asleep here. On the floor. Too exhausted to move."

    athought "Too broken to care. But this closeness... it's something real in the ruin."

    athought "I've never seen her like this. Unguarded. Undone."

    athought "No performance. No polish. Just... her. Beautiful in the breaking."

    # CAMERA: Micro-shift; her fingers tighten by reflex.

    "I shift. She stirs. Eyes opening slowly. Her hand tightens on my shirt—instinctive."

    l "(disoriented) I—where—"

    # VISUAL: She tries to rise, body locks; stays half-tangled.

    "She tries to rise—too fast. Body locks. Pain visible. But she doesn't untangle fully; our legs still brush, warmth lingering."

    a "(gentle) Easy. We're in my apartment. Floor. You fell asleep."

    l "(remembering, quiet) ...Oh."

    # CAMERA: Hold the quiet; let breathing lead.

    "Silence settles. Morning after. Everything exposed. Her breath quickens, close enough to feel."

    l "(attempting composure) I should go. I have—"

    "Her voice cracks. She stops. Can't finish."

    a "Lyra."

    l "(not looking at him) I'm fine. I just need—"

    # INSERT: subtle tremor on hands.

    "Her hands tremble. She clasps them. Still shaking."

    a "You're not fine."

    l "(quiet) ...No. I'm not."

    # CAMERA: Close on eyes—no mask, raw need.

    "She meets my eyes. No mask. No polish. Just exhaustion. And something else—need, raw and unspoken."

    l "How do you do this? Exist like this? Without the performance?"

    a "I don't know. I only learned yesterday."

    l "(hollow laugh) And look how well that's working."

    # VISUAL: Shoulders to wall; slow slide down; shared frame.

    "Wall cold against my back. Floor hard. Bodies aching. Neither of us moves. Shoulders touching—grounding, warm in the cold light."

    a "When did you last sleep? Really sleep?"

    l "(pause) ...I don't remember."

    a "Lyra—"

    l "Weeks. Maybe. I close my eyes and—"

    "She stops. Breath catches. Can't continue. Her shoulder leans into mine, seeking anchor."

    a "You see them."

    l "(quiet) Every time."

    # ========= THE BAND =========
    # CAMERA: Wrist CU; her fingers at the Band.

    "Silence. We both know. Faces that won't leave. Breaths syncing, slow and shared."

    "Her hand moves. Wrist. Fingers brush the Band. Checking."

    athought "I've seen her do this before. But now... now I'm watching."

    a "Your Band. You keep touching it."

    l "(realizes, pulls hand away) I don't—"

    a "How often?"

    l "(defensive) It's nothing. Just a habit."

    a "Lyra."

    l "(quiet) ...All the time. I don't even notice anymore."

    a "Why?"

    l "(long pause) Making sure it's still there. Still working."

    a "Why wouldn't it be?"

    l "Because..."

    "She trails off. Can't say more. Too much. Her hand finds my arm instead—grip light, seeking contact."

    a "Because what?"

    l "(shakes head) It's nothing. Paranoia. Ignore me."

    a "I'm not ignoring you."

    l "(barely audible) Because if it fails... I'm nothing."

    if empathy_band() == "obedience":
        a "(quiet) That's the story they teach."
    else:
        a "(quiet) The Band doesn't define worth."

    l "(sharp) Yes it does. Without this Band, I'm worthless. Disposable. Forgotten."

    l "You know that. You've lived it."

    athought "I have no answer. She's right. I lived it."

    l "(softer) I'm sorry. That was—"

    a "True. It was true."

    l "I can't do this. I can't think. I can't—"

    a "When did you last eat?"

    l "(pause) ...Yesterday. Maybe."

    a "Lyra—"

    l "I can't. Food doesn't... I can't keep anything down."

    "Her hand touches her stomach. Brief. Unconscious."

    athought "Stress. Trauma. Body rejecting everything."

    a "At least drink something. Water. Coffee."

    l "(small nod) Coffee. I can try coffee."

    # ========= COFFEE =========
    # VISUAL: Kettle; steam plume catches the beam.

    "The kettle hisses. Steam plume catching the light."

    "Lyra stays on the floor—too tired to move, or too afraid to trust her legs."

    "Her hand moves. Wrist. Band. Checking. Compulsive."

    athought "How many times a day? Dozens? Hundreds?"

    athought "She's terrified of something. Something about that Band."

    athought "But what?"

    # CAMERA: Pass the cup; fingertips linger a breath.

    "Coffee in her hands. Fingers brushing—accidental, but the touch lingers a second too long. Warmth in the cold."

    "She steadies the cup with both hands. Careful not to spill."

    l "Thank you."

    a "Don't thank me. Just drink."

    "She sips. Slowly. Body fighting it. But stays down."

    # ========= THE REAL CONFESSION =========

    l "(quiet) I lied to you. Last night."

    a "About what?"

    l "Sector Seven."

    "I sit close but not touching. Listening."

    l "I said I logged the families. Reported them. Let others... do the rest."

    a "..."

    l "(voice breaking) That wasn't true."

    "She stares into the cup. Can't meet my eyes."

    l "I didn't just log them. I executed them."

    l "Compliance audit. Direct termination protocol."

    l "They gave me the weapon. The list. The orders."

    l "(barely audible) And I obeyed."

    "Silence. Heavy as stone."

    a "How many?"

    l "Twelve families. Thirty-eight people total."

    l "Including..."

    "Her voice breaks. Can't finish."

    l "...seven children."

    # CAMERA: Tiny spill; she doesn't flinch.

    "The cup shakes. Coffee spills on her hand. She doesn't feel it."

    a "(takes cup from her, sets it aside) Lyra—"

    l "I told myself they were relocated. Gave myself the mercy of that lie."

    l "But I remember the sounds. The looks. The—"

    "She can't continue. Gasping. Hyperventilating."

    a "(moves closer) Breathe. Just breathe."

    l "I CAN'T. Every time I close my eyes I see them—"

    # VISUAL: Taking her hand; breaths matching; long beat.

    "No words. Just sitting. Taking her hand—gentle, not demanding. Her fingers curl into mine, holding on like a lifeline. Breaths syncing, slow and shared."

    athought "Like she did for me yesterday."

    l "(through tears) You killed six hundred. I killed thirty-eight."

    l "Your horror is bigger. But mine is..."

    l "...mine is mine. And I can't—I can't—"

    a "It's not a competition. Guilt doesn't work that way."

    l "Then how does it work?"

    a "It doesn't. It just... crushes. Until you can't breathe."

    l "(whisper) I can't breathe."

    if empathy_band() == "obedience":
        a "(measured) I know. In four, hold, out four. Stay with me."
    else:
        a "(soft) I know. I'm here. Breathe with me."

    "Shoulder touching shoulder. Grounding."

    l "Sector Seven wasn't the first time."

    a "..."

    l "There was another mission. Years ago. Before I became... this."

    "She looks at me. Something raw. Then shuts down."

    l "I don't want to talk about it."

    a "Okay."

    l "Not yet. Maybe not ever."

    a "That's okay too."

    "Silence. She expected pressure. Got space instead."

    l "(quiet) Thank you."

    a "For what?"

    l "For not making me explain."

    a "I know what it's like. Carrying something too heavy to voice."

    "Her hand moves. Wrist. Band. She notices. Stops."

    "Looks at her hand. Confused by her own compulsion."

    l "(staring at her hand) Why do I keep doing that?"

    a "I don't know. Do you?"

    l "(long pause) ...I'm afraid."

    a "Of what?"

    l "That it'll stop working. That I'll become... nothing."

    athought "Real fear. Not performance. Not deflection. Terror."

    a "The Band doesn't make you something. You already are."

    l "Am I? Or am I just what the Band lets me be?"

    a "Lyra—"

    l "(shakes head) I don't know anymore. I don't know where I end and the Band begins."

    # ========= MASK RETURNING =========
    # VISUAL: She stands too quickly; steadies herself; mask assembling.

    "She stands fast. Needs movement. Needs escape."

    l "I have to go. Council meeting. Performance required."

    a "Can you do it? After last night?"

    l "(steadies herself) I have to."

    # CAMERA: Watch the mask return, piece by piece.

    "Hair smoothed. Spine straightened. Mask returning."

    "Before my eyes, she transforms. Lyra the Weapon restored."

    l "(formal voice) Thank you for... last night. And this morning."

    a "Lyra, you don't have to—"

    l "(softer, real voice breaking through) I know. But if I don't practice the mask now..."

    "She stops. Looks at me. Mask cracks. Just for a second."

    l "(quietly) Do you see them? When you close your eyes?"

    a "Every time."

    l "Me too."

    l "(barely audible) Does it ever stop?"

    if empathy_band() == "obedience":
        a "I don't know."
    else:
        a "I don't know. I hope so."

    l "...I hope so too."

    "She walks to the door. Stops. Hand on handle."

    l "(without turning) Tonight. After your meeting with Zira. Find me."

    a "Where?"

    l "I'll find you. I always do."

    # ========= CONFESSION LOGGING =========

    if "Sector 7 confession (38/7)." not in characters["Lyra"]["notes"]:
        $ characters["Lyra"]["notes"].append("Sector 7 confession (38/7).")
        $ choice_and_dev(
            _current_scene_id, "lyra_s7_confession_logged", "EMP", factor=1,
            note="Lyra admits executing 38 (incl. 7 children) in Sector 7; Aeron witnesses."
        )
    $ scene_mark(_current_scene_id, "confession_acknowledged")

    # ========= EARNED TENDERNESS GATE =========

    $ _lyra_ok    = (characters["Lyra"]["trust"] >= 2 and characters["Lyra"]["affection"] >= 1)
    $ _lyra_ok_ob = (characters["Lyra"]["trust"] >= 3 and characters["Lyra"]["affection"] >= 2)

    menu:
        athought "She's about to leave. I could let her go. Or..."

        "Call her back." if ((empathy_band() == "empathy" and _lyra_ok) or (empathy_band() == "obedience" and _lyra_ok_ob) or (empathy_band() == "conflicted" and _lyra_ok)):
            $ choice_and_dev(
                _current_scene_id, "a18b_call_her_back", "EMP", factor=1,
                note="Vulnerable physical comfort; small step toward connection."
            )
            $ scene_mark(_current_scene_id, "hugged_lyra")
            $ rel_bump("Lyra", 1)

            a "Lyra—wait."

            "She pauses, hand on the handle. Doesn't turn, but her shoulders tense."

            a "(quiet) Lyra."

            "She turns slowly. Eyes meet. No words needed."

            "Arms around her—careful, not demanding. Holding the pieces together."

            l "(stiff at first, then softens) Aeron..."

            "She melts into it. Head on my shoulder, breath warm against my neck. Hands clutching my back."

            "No rush. Just presence. Heartbeats syncing, a quiet promise in the touch."

            athought "She's warm. Real. Broken but here. And for a moment, the world fades."

            l "(whisper) I needed this."

            a "(quiet) Me too."

            "We part slowly. Eyes linger—a spark unspoken."

            l "(small smile) Tonight."

            a "Tonight."

        "Let her go.":
            $ choice_and_dev(
                _current_scene_id, "a18b_let_her_go", "OB", factor=1,
                note="Keeps distance; withdraws after vulnerability."
            )
            $ scene_mark(_current_scene_id, "let_her_go")

            "The door clicks shut. Silence returns, heavier now."

            athought "Maybe next time. When we're both ready."

    # ========= OUTRO =========

    "The door closes. Silence floods back."

    athought "She's been barely holding on. Just like me."

    athought "All this time I thought she was saving me."

    athought "But we've been saving each other."

    # VISUAL: Small brown ring on floor; a red dot beside it.

    "Coffee spilled where she sat. And something else."

    "Her hand was clenched at her side—nails digging in so deep the skin split."

    "Blood. Small drop. She didn't even notice."

    if empathy_band() == "obedience":
        athought "Note the injury. Note the numbness. Proceed."
    else:
        athought "Pain doesn't register when you're already drowning."

    athought "38 people. 7 children. And something before that. Something worse."

    athought "Her Band compulsion. Her terror. Her mask."

    athought "She's not just broken. She's terrified of breaking more."

    athought "No Band. No worth. That's what the system teaches."

    athought "I learned that at twelve. Failed and forgotten."

    athought "But she has hers. And she's still terrified."

    athought "What happened to make her fear it so much?"

    # VISUAL: City comes alive; cold daylight swallows the room's warmth.

    "The city wakes beyond the pane. Another day. Another performance."

    athought "Broken recognizes broken."

    athought "We're both drowning. But at least we're drowning together."

    athought "Maybe that's enough. For now."

    # ========= BOOKKEEPING =========

    $ scene_mark(_current_scene_id, "forward_to_zira_meet")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_18b_morning_after_confession
# cann.when_in_timeline: Morning after Act 1 Scene 18 (post–Op 391 confession); before Obsidian Bridge setup.
# cann.what_happened:
#   - Aeron & Lyra wake on the floor after the breakdown; mutual vulnerability continues.
#   - Lyra's Band-check compulsion foregrounded; deeper fear of "no Band, no worth."
#   - Lyra reveals the full truth of Sector 7: she personally executed 38 (incl. 7 children).
#   - Optional earned tenderness: Aeron calls her back for a hug, or lets her go.
# cann.aeron_state: VO flavor follows empathy band; no forced momentum outside the single menu.
# cann.path_tracking:
#   - One menu:
#       • Call her back → EMP(+1)
#       • Let her go → OB(+1)
#   - One-time event nudge: witnessing Lyra's explicit confession → EMP(+1)
#   - Flags: confession_acknowledged / hugged_lyra / let_her_go / completed / forward_to_zira_meet.
# cann.thematic_flags: Post-crisis intimacy; performance vs person; worth bound to instruments; shared culpability.
# cann.block_status: VARIANT (small branch + event nudge).
# cann.visual_plate_economy:
#   - REUSE: Apartment master (floor and wall plate), window beam pass, kettle/steam insert.
#   - HERO: Hands on chest CU; Band-check wrist CU; coffee+blood floor insert; threshold hug two-shot.
# cann.requires_followup:
#   - Lyra's Band anxiety should recur and escalate near Act 1 climax.
#   - Zira meet setup proceeds; Marcus debrief tone may be colored by Op 391 outcomes.