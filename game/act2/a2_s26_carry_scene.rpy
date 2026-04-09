===================================================
ACT 2 - Scene 26: The Weight of Her
File: a2_s26_carry_scene.rpy
Path: EMP ONLY
===================================================

========= SCENE START TASKS =========
$ _current_scene_id = "a2_s26_carry_scene"
$ scene_mark(_current_scene_id, "entered")

label a2_s26_carry_scene:
    # ========= GUARD: EMP ONLY =========
    if STATE["path"] != "EMP":
        # OB path skips this scene entirely — med team handles Selene,
        # Aeron goes straight to debrief. Emotional distance preserved.
        return

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm lens, handheld micro-drift (intimacy, not chaos). Low angle on approach,
    #         rising to eye-level as they enter the room. Shallow DOF — faces sharp, world soft.
    # LIGHTING: Medbay exit: cold 5600K overheads, green-blue tint. Corridor: dim amber emergency strips.
    #           Selene's quarters: warm 2800K practicals (desk lamp, wall sconce), soft shadow fill.
    # SFX: Loop — distant base hum, ventilation whisper, Selene's labored breathing (subtle, not dramatic).
    #      One-shots — boot scuffs on metal, door hiss, fabric shift, mattress compress.
    # FX/COMP: Breath fog on cold corridor; warm glow spill from her doorway; dust motes in lamp light.
    # BLOCKING: Aeron carries Selene bridal-style; her arm around his neck, head against shoulder.
    #           She's conscious but weak — blood loss, exhaustion, not dying.
    # CANON: This scene ONLY exists in EMP. OB Aeron doesn't carry her — doesn't get this tenderness.
    #        This is the foundation for her "not blind faith" line in the finale.
    # FACE: Selene's face visible; Aeron's jaw/profile shots until the room.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions allowed, sensory-forward, emotional residue present.
    # Aeron is exhausted, guard down. Selene is vulnerable but lucid.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MEDBAY CORRIDOR - NIGHT]
    # Harsh lights. The smell of antiseptic and old blood. Tessa's voice fading behind them
    # as Aeron carries Selene away from the triage chaos.

    scene bg_medbay_corridor_night with dissolve
    play ambient "sfx/ambient/base_hum_cold.ogg" fadein 2.0

    # VISUAL: Medbay doors closing behind them. Aeron carrying Selene down the corridor.
    "The medbay doors hiss shut. Tessa's voice fades into the hum of recycled air."

    # VISUAL: Emergency strips cast amber bands across them as they walk.
    # CAMERA: Tracking shot, slightly behind — her arm around his neck, her head against his shoulder.

    athought "She weighs almost nothing. That's the first wrong thing."

    athought "Selene Ward is supposed to feel like gravity. Like the center everything else orbits."

    athought "Instead she feels like paper. Like something the wind could take."

    # VISUAL: Her bandages visible beneath the torn uniform. Dark stain spreading slowly.
    "The bandage on her side shows red through the fabric. Tessa said it would seep for a few hours."
    pause 0.6

    athought "A few hours. That's what it costs to throw yourself in front of a bullet meant for someone you've never met."

    # --- SELENE STIRS ---

    # VISUAL: Selene's eyes flutter open. She registers where she is — who's carrying her.
    "Her eyes open. Focus takes a moment to arrive."

    sel "(hoarse) I can walk."

    a "No. You can't."

    sel "That's... not your call."

    a "It is right now."

    # VISUAL: She tries to shift, winces. Settles back against him.
    "She tries to move. The pain stops her before he does."
    pause 0.5

    athought "Good. She's stubborn enough to try. That means she's still her."

    sel "(quieter) Where are you taking me?"

    a "Your quarters. Tessa's orders."

    sel "Tessa doesn't give me orders."

    a "She does tonight."

    # VISUAL: The ghost of a smile on Selene's face. Pain and amusement tangled together.
    "Something flickers across her face. Not quite a smile. Close enough."

    sel "You're enjoying this."

    athought "I'm not. I'm terrified."

    athought "But she doesn't need to know that."

    a "Someone has to keep you from bleeding out on the war room floor."

    sel "That would be... undignified."

    a "Extremely."

    # --- CORRIDOR PASSAGE ---

    # VISUAL: They pass a window — Solveil's lower tiers visible through reinforced glass,
    # lights scattered like dying stars. CAMERA: Reflection shot — both faces ghosted in the glass.

    "The corridor stretches ahead. Emergency lighting paints them in bands of amber and shadow."
    pause 0.7

    athought "I've carried wounded before. Dragged soldiers out of kill zones. Lifted bodies that stopped being people."

    athought "This is different."

    athought "She's not cargo. She's not a casualty report."

    athought "She's warm against my chest and I can feel her breathing and I don't want to let go."

    # VISUAL: A rebel passes — young, wide-eyed. Salutes awkwardly, keeps moving.
    "A young rebel rounds the corner. Sees them. Freezes."

    "His salute is half-formed, uncertain. He doesn't know where to look."

    athought "Neither do I."

    "Aeron nods once. The kid presses against the wall to let them pass, then exhales."
    pause 0.6

    # --- SELENE'S DOOR ---

    # VISUAL: Her quarters. The door is unmarked — no name, no rank insignia. Just a number.
    # CAMERA: Push in as Aeron pauses at the threshold.

    "Her door. No name plate. No rank markers. Just a number stenciled in faded paint."

    athought "Nineteen years of command and she still lives like a soldier waiting for transfer."

    # VISUAL: Aeron shifts her weight to free one hand, reaches for the access panel.
    sel "Code is 7-7-4-2."

    a "You're giving me your door code?"

    sel "You're already holding me. Seems redundant to pretend there's a boundary left."

    # VISUAL: The door hisses open. Warm light spills into the cold corridor.
    "The door opens. Warm light bleeds into the hallway."

    athought "She's not wrong."

    # --- INSIDE HER QUARTERS ---

    # [INT. SELENE'S QUARTERS - CONTINUOUS]
    # Small. Functional. A cot against one wall, desk against the other. Maps pinned everywhere.
    # One photo on the desk. A plant — struggling but alive. The room of someone who never expected to stay.

    scene bg_selene_quarters_night with dissolve
    stop ambient fadeout 1.0
    play ambient "sfx/ambient/room_quiet_warm.ogg" fadein 2.0

    "The room is smaller than expected. Cot. Desk. Maps covering every surface that isn't already covered in maps."

    athought "She lives in a closet. The woman who runs half this rebellion lives in a closet."

    # VISUAL: One photo on the desk. A woman with Selene's jaw and none of her armor.
    "One photo on the desk. A woman with Selene's jaw and none of her armor."

    athought "The only proof she didn't spawn fully formed out of a battle plan."

    # VISUAL: A plant on the windowsill. Small, stubborn, slightly yellow.
    "A plant on the sill. Small. Stubborn. Slightly yellow at the edges."

    athought "She keeps something alive. Of course she does."

    # --- SETTING HER DOWN ---

    # VISUAL: Aeron lowers Selene onto the cot. Careful. The mattress compresses under her weight.
    # CAMERA: Close on his hands supporting her back, her neck. The intimacy of the gesture.

    "He lowers her onto the cot. Slow. Careful. Her breath catches when her side touches the mattress."

    sel "(through teeth) Gentle."

    a "I'm trying."

    sel "Try harder."

    # VISUAL: She settles. Eyes closed. Hand pressed to the bandage.
    "She settles into the thin mattress. Her hand finds the bandage, presses."
    pause 0.6

    athought "Still checking. Still monitoring. Even horizontal, she's running calculations."

    # --- THE MOMENT HOLDS ---

    # VISUAL: Aeron straightens. Stands there. Doesn't leave.
    # CAMERA: Two-shot — him standing, her lying. The space between them charged.

    athought "I should leave. Job's done. She's safe. Tessa will check on her in an hour."

    athought "I don't move."

    # VISUAL: Selene opens her eyes. Looks at him. Really looks.
    "Her eyes open. Find his."

    sel "You're still here."

    a "I'm still here."

    sel "Why?"

    # --- CHOICE: WHY HE STAYS ---

    menu:
        "She watches him. The question hangs between them like smoke."

        "Because you scared me.":
            $ choice_and_dev(
                _current_scene_id, "_honest_answer", "EMP", factor=1,
                next_scene_label=None,
                note="Vulnerability; admits fear; EMP-lean emotional honesty."
            )
            jump .honest_answer

        "Someone has to make sure you don't rip your stitches.":
            $ choice_and_dev(
                _current_scene_id, "_deflect_answer", "EMP", factor=0,
                next_scene_label=None,
                note="Deflection through humor; affection without vulnerability."
            )
            jump .deflect_answer

    # --- BRANCH: HONEST ---
    label .honest_answer:

        a "Because you scared me."

        "The words come out before he can stop them. Raw. Unfiltered."

        athought "That's not what I meant to say."

        athought "That's exactly what I meant to say."

        # VISUAL: Something shifts in her expression. The commander mask cracks.
        sel "...scared you."

        a "You threw yourself in front of a bullet for someone whose name you didn't know."

        sel "Private Hendricks. Eighteen. First deployment."

        a "You learned his name after."

        sel "I learned his name before. I learn all their names."

        athought "Of course she does."

        # VISUAL: She reaches out. Her hand finds his wrist. Light grip. Anchoring.
        "Her hand finds his wrist. The grip is light. Just enough to hold."

        sel "I'm still here, Aeron."

        a "I know."

        sel "Then stop looking at me like I'm already gone."

        athought "I can't help it. I keep seeing the blood. The way she fell."

        athought "I keep seeing what almost happened."

        a "...I'll try."

        $ STATE["flags"]["SELENE_CARRY_HONEST"] = True
        $ STATE["rel"]["Selene"]["trust"] += 1

        jump .convergence

    # --- BRANCH: DEFLECT ---
    label .deflect_answer:

        a "Someone has to make sure you don't rip your stitches."

        sel "Tessa would kill you if you let me bleed out."

        a "Tessa would kill me slowly. And lecture me the whole time."

        # VISUAL: Selene almost laughs. It turns into a wince.
        "She almost laughs. The sound turns into a wince halfway through."

        sel "Don't make me laugh. It hurts."

        a "Then don't ask stupid questions."

        sel "It wasn't stupid. It was honest."

        athought "She's right. It was honest."

        athought "And I dodged it because the real answer scares me more than any firefight."

        # VISUAL: She watches him. Sees through the deflection.
        sel "You're not good at this, are you?"

        a "At what?"

        sel "Admitting you care."

        athought "No. I'm not."

        "He doesn't answer. His silence says enough."

        # VISUAL: She reaches out. Her hand finds his wrist.
        "Her hand finds his wrist. The grip is light. Understanding."

        sel "That's okay. Neither am I."

        $ STATE["flags"]["SELENE_CARRY_DEFLECT"] = True
        $ STATE["rel"]["Selene"]["affection"] += 1

        jump .convergence

    # --- CONVERGENCE ---
    label .convergence:

        # VISUAL: The two of them. Her hand on his wrist. The room warm and quiet.
        # CAMERA: Slow push in. The world outside doesn't exist.

        "The ventilation hums. Somewhere distant, the base settles into night watch."
        pause 0.7

        athought "I should go. Let her rest."

        athought "But her hand is still on my wrist and I don't want to be the one to break it."

        # --- SHE ASKS HIM TO STAY ---

        sel "Aeron."

        a "Yeah?"

        sel "The chair. By the desk."

        athought "She's not asking me to leave."

        a "What about it?"

        sel "It's uncomfortable. But it's there."

        athought "She's asking me to stay."

        # VISUAL: He looks at the chair. Battered. Metal. Definitely uncomfortable.
        "The chair is metal and battered and looks like it predates the rebellion."

        athought "I've slept in worse."

        a "Tessa will check on you in an hour."

        sel "I know."

        a "If she finds me here—"

        sel "She'll make assumptions. Let her."

        sel "If anyone asks, tell them I ordered you to stay on watch."

        athought "She's still thinking in terms of command optics. Even now."

        athought "Let her."

        # VISUAL: He pulls the chair closer to the cot. Sits. Doesn't let go of her hand.
        "He pulls the chair to the cot. Sits. Her hand slides from his wrist to his fingers."

        athought "This is probably a mistake."

        athought "I don't care."

        # --- QUIET ---

        # VISUAL: The room settles. Her breathing evens out. His stays measured.
        # CAMERA: Wide shot — two figures in warm light. The war outside the door.

        "Her eyes close. Her breathing slows. The grip on his hand loosens but doesn't release."
        pause 0.8

        athought "She's asleep. Or close enough."

        athought "I should be reviewing after-action reports. Checking casualty lists. Planning tomorrow."

        athought "Instead I'm sitting in a metal chair holding the hand of a woman who almost died today."

        pause 0.7

        athought "And I'm not going anywhere."

        # --- SCENE CLOSE ---

        # VISUAL: Time skip. The lamp flickers. His head has dropped forward — he's dozed off.
        # Her hand is still in his.

        "At some point, the lamp flickers. At some point, his eyes close."

        "When Tessa opens the door an hour later, she finds them like that."

        "She doesn't say anything. She checks Selene's bandages, adjusts the blanket, and leaves."

        athought "I hear the door close. I don't open my eyes."

        athought "Tomorrow there will be questions. Implications. Zira's smirk."

        athought "Tonight, there's just this. Her hand in mine. The sound of her breathing."

        athought "It's enough. It's more than enough."

        # --- FADE OUT ---

        stop ambient fadeout 3.0
        scene black with dissolve

        # ========= STATE UPDATES =========
        $ STATE["scenes"]["A2_26_CarryScene"] = True
        $ STATE["flags"]["SELENE_CARRY_COMPLETE"] = True
        $ STATE["rel"]["Selene"]["trust"] += 1
        $ STATE["rel"]["Selene"]["affection"] += 1

        # ========= TELEMETRY =========
        #$ telemetry(_current_scene_id, choice="honest" if STATE["flags"].get("SELENE_CARRY_HONEST") else "deflect")
        $ set_scene_flag(_current_scene_id, "completed")

        return

    ​
# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s26_carry_scene
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night after the Echelon Raid Defense. Before Zira Commitment scene.
#   - EMP ONLY. OB path skips — Aeron goes to debrief, med team handles Selene.
# cann.what_happened:
#   - Aeron carries wounded Selene from medbay to her quarters.
#   - Physical intimacy without sexuality — tenderness, vulnerability, care.
#   - Player choice: honest admission ("you scared me") vs deflection (joke about stitches).
#   - Both paths converge: she asks him to stay, he does. They fall asleep holding hands.
#   - Tessa finds them, says nothing, checks bandages, leaves.
#   - This scene is WHY Selene offers shared command in the finale.
#   - This scene is WHAT OB Aeron doesn't get — the tenderness that softens her verdict.
# cann.aeron_state:
#   - EMP warmth — guard fully down. Contractions, sensory language, emotional honesty.
# cann.path_tracking:
#   - EMP baseline. Honest choice adds trust+1; deflect adds affection+1.
#   - Both get base +1/+1 at convergence.
# cann.thematic_flags:
#   - Motifs: Weight/gravity (she feels like paper), warmth vs cold (corridor vs room), hands.
#   - Recurring: "I'm still here" — echoes through Act 3 if Selene lives.
#   - The plant on the windowsill — she keeps something alive. Contrast with OB's sterility.
#   - The "not blind faith" line in the finale lands because of this night.
# cann.character_moments:
#   - Selene: Vulnerable but lucid. Commander mask cracking. Allows intimacy she normally guards.
#   - Tessa: Finds them, says nothing, checks bandages, leaves. Silence as care.
# cann.block_status:
#   - VARIANT (EMP only); requires followup scene load.
# cann.requires_followup:
#   - Next scene: a2_s27_zira_commitment (both paths, but EMP plays differently because of this).
#   - Tessa's silence here pays off in Act 3 — she knows, she supports, she doesn't push.
#   - Zira's smirk tomorrow is earned by this scene.