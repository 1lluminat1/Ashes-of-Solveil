# =======================================================
# ACT 1 - Scene 18b: Morning After Confession
# File: act1_18b_morning_after_confession.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_18b_morning_after_confession"
$ scene_mark(_current_scene_id, "entered")

label act1_morning_after_confession:

    # Alignment read for flavor only (no momentum except menu below)
    $ band = get_empathy_band()            # "obedience" | "conflicted" | "empathy"
    $ is_obedient_path = (band == "obedience")

    # VISUAL: Apartment floor, early light carving a diagonal beam across the room.
    # LIGHTING: Cold interior vs warm shard from window.
    # SOUND: Building ventilation; a faint city hum under the silence.
    # CAMERA: Slow reveal from floor-level to the two of them.

    "{i}Morning light cuts through the window. Sharp. Unforgiving.{/i}"
    "{i}He wakes slowly. Floor hard beneath him. Something warm against his side.{/i}"

    # Still dressed; survival closeness
    # CAMERA: Tight two-shot on their tangle; shallow depth on hands over chest.
    "{i}Lyra. Still here. Face pressed into his shoulder. Our legs tangled, her hand resting on my chest—like we held on through the night without words.{/i}"
    "{i}Dark circles under her eyes. Even in sleep, tension in her jaw. But her breath... warm against my skin.{/i}"

    a "{i}We fell asleep here. On the floor. Too exhausted to move.{/i}"
    a "{i}Too broken to care. But this closeness... it's something real in the ruin.{/i}"

    a "{i}I've never seen her like this. Unguarded. Undone.{/i}"
    a "{i}No performance. No polish. Just... her. Beautiful in the breaking.{/i}"

    # CAMERA: His micro-shift; her fingers tighten by reflex.
    "{i}He shifts. She stirs. Eyes open slowly. Her hand tightens on his shirt briefly, instinctive.{/i}"

    l "(disoriented) I—where—"

    # VISUAL: She tries to rise, body locks; stays half-tangled.
    "{i}She tries to rise. Too fast. Body locks. Pain visible. But she doesn't untangle fully—our legs still brush, warmth lingering.{/i}"

    a "(gentle) Easy. We're in my apartment. Floor. You fell asleep."
    l "(remembering, quiet) ...Oh."

    # CAMERA: Hold the quiet; let breathing lead.
    "{i}Silence settles. Morning after. Everything exposed. Her breath quickens, close enough to feel.{/i}"

    l "(attempting composure) I should go. I have—"

    "{i}Her voice cracks. She stops. Can't finish.{/i}"

    a "Lyra."
    l "(not looking at him) I'm fine. I just need—"

    # INSERT: subtle tremor on hands.
    "{i}Her hands tremble. She clasps them. Still shaking.{/i}"

    a "You're not fine."
    l "(quiet) ...No. I'm not."

    # CAMERA: Close on eyes—no mask, raw need.
    "{i}She meets his eyes. No mask. No polish. Just exhaustion. And something else—need, raw and unspoken.{/i}"

    l "How do you do this? Exist like this? Without the performance?"
    a "I don't know. I only learned yesterday."
    l "(hollow laugh) And look how well that's working."

    # VISUAL: Shoulders to wall; slow slide down; shared frame.
    "{i}They sit against the wall. Floor hard. Bodies aching. Neither moves. Shoulders touch—grounding, warm in the cold light.{/i}"

    a "When did you last sleep? Really sleep?"
    l "(pause) ...I don't remember."
    a "Lyra—"
    l "Weeks. Maybe. I close my eyes and—"

    "{i}She stops. Breath catches. Can't continue. Her shoulder leans into his, seeking anchor.{/i}"

    a "You see them."
    l "(quiet) Every time."

    # CAMERA: Wrist CU; her fingers at the Band.
    "{i}Silence. They both know. Faces that won't leave. Breaths syncing, slow and shared.{/i}"
    "{i}Her hand moves. Wrist. Fingers brush the Band. Checking.{/i}"
    "{i}He's seen her do this before. But now... now he's watching.{/i}"

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

    "{i}She trails off. Can't say more. Too much. Her hand finds his arm instead—grip light, seeking contact.{/i}"

    a "Because what?"
    l "(shakes head) It's nothing. Paranoia. Ignore me."
    a "I'm not ignoring you."
    l "(barely audible) Because if it fails... I'm nothing."

    if is_obedient_path:
        a "(quiet) That's the story they teach."
    else:
        a "(quiet) The Band doesn't define worth."

    l "(sharp) Yes it is. Without this Band, I'm worthless. Disposable. Forgotten."
    l "You know that. You've lived it."

    "{i}He has no answer. She's right. He lived it.{/i}"

    l "(softer) I'm sorry. That was—"
    a "True. It was true."

    l "I can't do this. I can't think. I can't—"
    a "When did you last eat?"
    l "(pause) ...Yesterday. Maybe."
    a "Lyra—"
    l "I can't. Food doesn't... I can't keep anything down."

    "{i}Her hand touches her stomach. Brief. Unconscious.{/i}"
    "{i}Stress. Trauma. Body rejecting everything.{/i}"

    a "At least drink something. Water. Coffee."
    l "(small nod) Coffee. I can try coffee."

    # VISUAL: He rises; kettle; steam plume catches the beam.
    "{i}He stands. Moves to make coffee. She stays on floor.{/i}"
    "{i}Too tired to move. Or too afraid to trust her legs.{/i}"

    "{i}Her hand moves again. Wrist. Band. Checking. Compulsive.{/i}"
    "{i}She doesn't notice. Automatic. Constant.{/i}"

    a "{i}How many times a day? Dozens? Hundreds?{/i}"
    a "{i}She's terrified of something. Something about that Band.{/i}"
    a "{i}But what?{/i}"

    # CAMERA: Pass the cup; fingertips linger a breath.
    "{i}He brings coffee. Hands it to her. Fingers brush—accidental, but the touch lingers a second too long. Warmth in the cold.{/i}"
    "{i}She steadies cup with both hands. Careful not to spill.{/i}"

    l "Thank you."
    a "Don't thank me. Just drink."

    "{i}She sips. Slowly. Body fighting it. But stays down.{/i}"

    l "(quiet) I lied to you. Last night."
    a "About what?"
    l "Sector Seven."

    "{i}He sits. Close but not touching. Listening.{/i}"

    l "I said I logged the families. Reported them. Let others... do the rest."
    a "..."
    l "(voice breaking) That wasn't true."

    "{i}She stares into the cup. Can't meet his eyes.{/i}"

    l "I didn't just log them. I executed them."
    l "Compliance audit. Direct termination protocol."
    l "They gave me the weapon. The list. The orders."
    l "(barely audible) And I obeyed."

    "{i}Silence. Heavy as stone.{/i}"

    a "How many?"
    l "Twelve families. Thirty-eight people total."
    l "Including..."

    "{i}Her voice breaks. Can't finish.{/i}"

    l "...seven children."

    # CAMERA: Tiny spill; she doesn’t flinch.
    "{i}The cup shakes. Coffee spills on her hand. She doesn't feel it.{/i}"

    a "(takes cup from her, sets it aside) Lyra—"
    l "I told myself they were relocated. Gave myself the mercy of that lie."
    l "But I remember the sounds. The looks. The—"

    "{i}She can't continue. Gasping. Hyperventilating.{/i}"

    a "(moves closer) Breathe. Just breathe."
    l "I CAN'T. Every time I close my eyes I see them—"

    # VISUAL: He takes her hand; breaths match; long beat.
    "{i}He doesn't speak. Just sits. Takes her hand—gentle, not demanding. Her fingers curl into his, holding on like a lifeline. Breaths sync, slow and shared.{/i}"
    "{i}Like she did for him yesterday.{/i}"

    l "(through tears) You killed six hundred. I killed thirty-eight."
    l "Your horror is bigger. But mine is..."
    l "...mine is mine. And I can't—I can't—"

    a "It's not a competition. Guilt doesn't work that way."
    l "Then how does it work?"
    a "It doesn't. It just... crushes. Until you can't breathe."
    l "(whisper) I can't breathe."

    if is_obedient_path:
        a "(measured) I know. In four, hold, out four. Stay with me."
    else:
        a "(soft) I know. I'm here. Breathe with me."

    "{i}He shifts closer. Shoulder touching shoulder. Grounding.{/i}"

    l "Sector Seven wasn't the first time."
    a "..."
    l "There was another mission. Years ago. Before I became... this."

    "{i}She looks at him. Something raw. Then shuts down.{/i}"

    l "I don't want to talk about it."
    a "Okay."
    l "Not yet. Maybe not ever."
    a "That's okay too."

    "{i}Silence. She expected pressure. Got space instead.{/i}"

    l "(quiet) Thank you."
    a "For what?"
    l "For not making me explain."
    a "I know what it's like. Carrying something too heavy to voice."

    "{i}Her hand moves. Wrist. Band. She notices. Stops.{/i}"
    "{i}Looks at her hand. Confused by her own compulsion.{/i}"

    l "(staring at her hand) Why do I keep doing that?"
    a "I don't know. Do you?"
    l "(long pause) ...I'm afraid."
    a "Of what?"
    l "That it'll stop working. That I'll become... nothing."

    "{i}Real fear. Not performance. Not deflection. Terror.{/i}"

    a "The Band doesn't make you something. You already are."
    l "Am I? Or am I just what the Band lets me be?"
    a "Lyra—"
    l "(shakes head) I don't know anymore. I don't know where I end and the Band begins."

    # VISUAL: She stands too quickly; steadies herself; mask assembling.
    "{i}She stands. Fast. Needs movement. Needs escape.{/i}"

    l "I have to go. Council meeting. Performance required."
    a "Can you do it? After last night?"
    l "(steadies herself) I have to."

    # CAMERA: Watch the mask return, piece by piece.
    "{i}She smooths her hair. Straightens spine. Mask returning.{/i}"
    "{i}Before his eyes, she transforms. Lyra the Weapon restored.{/i}"

    l "(formal voice) Thank you for... last night. And this morning."
    a "Lyra, you don't have to—"
    l "(softer, real voice breaking through) I know. But if I don't practice the mask now..."

    "{i}She stops. Looks at him. Mask cracks. Just for a second.{/i}"

    l "(quietly) Do you see them? When you close your eyes?"
    a "Every time."
    l "Me too."
    l "(barely audible) Does it ever stop?"

    if is_obedient_path:
        a "I don't know."
    else:
        a "I don't know. I hope so."

    l "...I hope so too."

    "{i}She walks to the door. Stops. Hand on handle.{/i}"

    l "(without turning) Tonight. After your meeting with Zira. Find me."
    a "Where?"
    l "I'll find you. I always do."

    # ---- One-time log + empathy nudge (event, not a menu choice) ----
    if "Sector 7 confession (38/7)." not in characters["Lyra"]["notes"]:
        $ characters["Lyra"]["notes"].append("Sector 7 confession (38/7).")
        $ apply_choice_once(
            _current_scene_id, "lyra_s7_confession_logged", "EMP", factor=1,
            next_scene_label="act1_morning_after_confession",
            note="Lyra admits executing 38 (incl. 7 children) in Sector 7; Aeron witnesses."
        )
    $ set_scene_flag(_current_scene_id, "confession_acknowledged")

    # ===== Earned tenderness gate (no lewd) =====
    $ _lyra_ok    = (characters["Lyra"]["trust"] >= 2 and characters["Lyra"]["affection"] >= 1)
    $ _lyra_ok_ob = (characters["Lyra"]["trust"] >= 3 and characters["Lyra"]["affection"] >= 2)

    menu:
        "Call her back." if ((band == "empathy" and _lyra_ok) or (band == "obedience" and _lyra_ok_ob) or (band == "conflicted" and _lyra_ok)):
            $ apply_choice_once(
                _current_scene_id, "a18b_call_her_back", "EMP", factor=1,
                next_scene_label="act1_morning_after_confession",
                note="Vulnerable physical comfort; small step toward connection."
            )
            $ set_scene_flag(_current_scene_id, "hugged_lyra")
            $ add_trust("Lyra", 1)
            $ add_affection("Lyra", 1)

            a "Lyra—wait."

            "{i}She pauses, hand on the handle. Doesn't turn, but her shoulders tense.{/i}"
            "{i}He stands, closes the distance. Gentle—calls her name again, softer.{/i}"

            a "(quiet) Lyra."

            "{i}She turns slowly. Eyes meet. No words needed.{/i}"
            "{i}He pulls her into a hug—careful, not demanding. Arms around her, holding the pieces together.{/i}"

            l "(stiff at first, then softens) Aeron..."

            "{i}She melts into it. Head on his shoulder, breath warm against his neck. Hands clutch his back.{/i}"
            "{i}No rush. Just presence. Heartbeats syncing, a quiet promise in the touch.{/i}"

            a "{i}She's warm. Real. Broken but here. And for a moment, the world fades.{/i}"
            l "(whisper) I needed this."
            a "(quiet) Me too."

            "{i}They part slowly. Eyes linger—a spark unspoken.{/i}"

            l "(small smile) Tonight."
            a "Tonight."

        "Let her go.":
            $ apply_choice_once(
                _current_scene_id, "a18b_let_her_go", "OB", factor=1,
                next_scene_label="act1_morning_after_confession",
                note="Keeps distance; withdraws after vulnerability."
            )
            $ set_scene_flag(_current_scene_id, "let_her_go")

            "{i}He watches her leave. Door clicks shut. Silence returns, heavier now.{/i}"

            a "{i}Maybe next time. When we're both ready.{/i}"

    # OUTRO BEATS
    "{i}The door closes. Silence floods back.{/i}"
    "{i}He's alone. She's gone. But something changed.{/i}"

    a "{i}She's been barely holding on. Just like me.{/i}"
    a "{i}All this time I thought she was saving me.{/i}"
    a "{i}But we've been saving each other.{/i}"

    # VISUAL: Small brown ring on floor; a red dot beside it.
    "{i}Coffee spilled where she sat. And something else.{/i}"
    "{i}Blood. Small drop. Her hand. She didn't even notice.{/i}"

    if is_obedient_path:
        a "{i}Note the injury. Note the numbness. Proceed.{/i}"
    else:
        a "{i}Pain doesn't register when you're already drowning.{/i}"

    a "{i}38 people. 7 children. And something before that. Something worse.{/i}"
    a "{i}Her Band compulsion. Her terror. Her mask.{/i}"
    a "{i}She's not just broken. She's terrified of breaking more.{/i}"

    a "{i}No Band. No worth. That's what the system teaches.{/i}"
    a "{i}I learned that at twelve. Failed and forgotten.{/i}"
    a "{i}But she has hers. And she's still terrified.{/i}"
    a "{i}What happened to make her fear it so much?{/i}"

    # WIDE: City comes alive; cold daylight swallows the room’s warmth.
    "{i}The city wakes beyond the glass. Another day. Another performance.{/i}"

    a "{i}Glass recognizes glass. Broken recognizes broken.{/i}"
    a "{i}We're both drowning. But at least we're drowning together.{/i}"
    a "{i}Maybe that's enough. For now.{/i}"

    # Bookkeeping
    $ set_scene_flag(_current_scene_id, "forward_to_zira_meet")
    $ set_scene_flag(_current_scene_id, "completed")
    return


# ========= CANON NOTES =========
# cann.scene_id: act1_18b_morning_after_confession
# cann.when_in_timeline: Morning after Act 1 Scene 18 (post–Op 391 confession); before Obsidian Bridge setup.
# cann.what_happened:
#   - Aeron & Lyra wake on the floor after the breakdown; mutual vulnerability continues.
#   - Lyra’s Band-check compulsion foregrounded; deeper fear of “no Band, no worth.”
#   - Lyra reveals the full truth of Sector 7: she personally executed 38 (incl. 7 children).
#   - Optional earned tenderness: Aeron calls her back for a hug (no lewd), or lets her go.
# cann.aeron_state: VO flavor follows empathy band; no forced momentum outside the single menu.
# cann.path_tracking:
#   - One menu:
#       • Call her back → EMP(+1) via apply_choice_once("a18b_call_her_back").
#       • Let her go    → OB(+1)  via apply_choice_once("a18b_let_her_go").
#   - One-time event nudge (non-menu): witnessing Lyra’s explicit execution confession → EMP(+1)
#       via apply_choice_once("lyra_s7_confession_logged") when first appended to notes.
#   - Flags set on scene key: confession_acknowledged / hugged_lyra / let_her_go / completed / forward_to_zira_meet.
#   - Running window BEFORE:   **≈ [-55, +55]**   (from Act 1 Scene 18)
#   - Running window AFTER:    **≈ [-55, +57]**   (first visit max: +2 = hug + confession)
#       • If confession already logged on a prior route, this scene’s delta is **−1 → +1**.
# cann.thematic_flags: Post-crisis intimacy; performance vs person; worth bound to instruments; shared culpability.
# cann.block_status: VARIANT (small branch + event nudge).
# cann.true_path_integration: none (TP remains menu-free).
# cann.visual_plate_economy:
#   - REUSE: Apartment master (floor and wall plate), window beam pass, kettle/steam insert.
#   - HERO: Hands on chest CU; Band-check wrist CU; coffee+blood floor insert; threshold hug two-shot.
# cann.requires_followup:
#   - Lyra’s Band anxiety should recur (micro-tics) and escalate near Act 1 climax.
#   - Zira meet setup proceeds; Marcus debrief tone may be colored by Op 391 outcomes.
# cann.consistency_asserts:
#   - Aeries altitude grammar (no rain-on-glass); keep amber/cold contrast language.
#   - Count integrity: Op 391 references align with prior scene outcomes (600/0/… variations).