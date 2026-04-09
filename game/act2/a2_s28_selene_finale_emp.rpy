# =======================================================
# ACT 2 - Scene 28: Selene Finale (EMP)
# File: a2_s28_selene_finale_emp.rpy
# Act 2 closer. Shared command. Hope.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s28_selene_finale_emp"
$ scene_mark(_current_scene_id, "entered")

label a2_s28_selene_finale_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, steady. Two-shot across the strategy table — same framing as Command Temperature.
    #         Push-in when Selene offers the cipher. Hold wide for the room's reaction.
    #         Final shot: two people standing together at the head of a table. Not one.
    # LIGHTING: Morning. Warmer than the base usually is — amber practicals winning over the overhead strips.
    #           Selene's wound bandages catch the light. The cipher catches the light.
    # SFX: Loop — base hum (quieter now, aftermath). One-shots — door hiss, chair shift, Tessa's choked laugh.
    # FACE: Selene wounded, exhausted, certain. Aeron uncertain for the first time in a while — not about the war, about whether he deserves this. The team watching something they've been waiting for without knowing it.

    # ========== THE STRATEGY CHAMBER — MORNING ==========

    "The strategy chamber. Same walls. Same table. Same faces."

    "But something is different today. Not danger — something waiting to be said out loud."

    # VISUAL: Selene enters last. Wound visible — left shoulder bandaged, movement careful. Tessa moves to help. Selene waves her off.
    sel "I won't sit this out because I'm bleeding. We don't have that luxury."

    "Every step costs her something. She doesn't let it show in her face."

    athought "Yesterday she threw herself in front of a bullet meant for a private. Someone whose name I didn't know."
    athought "That's who she is. That's always been who she is."

    "She reaches the table. Braces herself against it. Looks up."

    sel "I called you all here because something needs to be said."

    "The room goes still."

    # ========== THE ACKNOWLEDGMENT ==========

    sel "I've watched you change, Aeron."

    "Her voice is calm. Not cold — certain. The voice of someone who's spent a long time thinking about what she's about to say."

    sel "Yesterday, you made calls that kept the operation intact. You stepped into command when the line wavered."

    sel "You weighed lives I never wanted you to have to weigh."

    if scene_has("a2_s26_carry_scene", "entered"):
        athought "I think of carrying her to her room. The weight of her against my chest. The way she let me."

    sel "You didn't treat them like numbers. You didn't calculate acceptable losses and move on."

    sel "You fought for every single one of them, even when it would have been easier not to."

    "She looks around the room. At Tessa. At Lyra. At Zira and Noelle. Then back at Aeron."

    sel "That's not the man who walked into this rebellion. That's not the soldier Echelon trained."

    sel "That's someone who understands that winning means nothing if we lose what we're fighting for."

    # ========== THE OFFER ==========

    "She reaches into her jacket. Slow — the wound makes everything slow."

    "A command cipher. The kind used to authorize high-level operations. Small. Heavy. Nineteen years of weight compressed into metal."

    sel "I've carried this alone for nineteen years. Every decision. Every life lost. Every compromise that felt like betrayal."

    "She sets it on the table between them."

    sel "I'm tired, Aeron. Not of the fight — of fighting it alone."

    "Lyra's breath catches. Zira goes very still."

    sel "From today, I want you to carry this with me. Not under me. Not following orders."

    sel "Together."

    athought "Shared command."

    sel "This isn't blind faith. If I see you slipping toward what we're fighting, I will say it."
    sel "I need you to be the kind of man who can hear it."

    if flag("ob_doctrine"):
        athought "She's trusting me despite what I said in the alcove. Despite 'order is mercy at scale.'"
        athought "She heard Marcus in my mouth and she's still offering this."
    elif flag("emp_doctrine"):
        athought "She's trusting me because of what I said in the alcove. Because I chose the names over the doctrine."

    sel "Will you stand with me?"

    # ========== THE ANSWER ==========

    "The cipher sits on the table. The room holds its breath."

    athought "I'm not sure I deserve this."

    a "I'm not sure I deserve this."

    sel "None of us deserve the weight we carry. We just have to be strong enough to carry it anyway."

    "Aeron reaches across the table. Takes her hand."

    "Her grip is firm despite the tremor."

    a "Together, then."

    sel "Together."

    # ========== THE ROOM ==========

    "The room exhales."

    l "(wiping her eyes) You already have been. Commanding, I mean. This just makes it honest."

    z "(the faintest smirk, warmth underneath) About time someone else got stuck reading ops reports at three in the morning."

    t "(hands pressed to her mouth, crying) She trusts you. We do too."

    n "(one small nod) From a structural standpoint, distributed command is overdue."

    "Selene uses Aeron's grip to pull herself upright."

    "For a moment they're just standing there — two people holding each other up."

    athought "Maybe that's what command was supposed to be all along."
    athought "Not one person carrying everything. Just people holding each other up."

    sel "Now. Someone help me sit down before I fall over and ruin the moment."

    "Tessa laughs through her tears and rushes forward. Zira rolls her eyes but she's smiling."

    # ========== ACT CLOSE ==========

    "The strategy chamber. Same walls. Same table."

    "Not the same people."

    pause 1.5

    scene black with fade

    centered "{size=+20}END OF ACT II{/size}"
    pause 1.0
    centered "{size=+10}The Resonant Rebellion{/size}"
    pause 2.0
    scene black with fade

    # ========== STATE UPDATES ==========

    $ canon_set("shared_command", True)
    $ canon_set("selene_alive", True)
    $ rel_bump("Selene", trust=2, loyalty=1)
    $ flag("act2_complete", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s28_selene_finale_emp
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after the raid and Zira commitment scene. Act 2 finale.
#   - EMP path. Selene alive, wounded, offering shared command.
# cann.what_happened:
#   - Selene acknowledges Aeron's growth. "That's not the soldier Echelon trained."
#   - Offers the command cipher — shared command. "Together."
#   - Aeron accepts. "I'm not sure I deserve this." "None of us deserve the weight we carry."
#   - The team reacts: Lyra cries, Zira smirks with warmth, Tessa sobs, Noelle nods.
#   - Act 2 closes on hope: "Not one person carrying everything. Just people holding each other up."
#   - Subtitle: "The Resonant Rebellion."
# cann.aeron_state:
#   - The EMP journey culminates: from Glass to someone Selene trusts with shared command.
#   - Carry scene callback: "The weight of her against my chest. The way she let me."
#   - Doctrine callback: she trusts him despite (or because of) what he said in the alcove.
# cann.path_tracking:
#   - No player choice — this is the reward for the EMP path.
#   - canon_set("shared_command"), canon_set("selene_alive").
#   - trust +2, loyalty +1 for Selene.
#   - flag("act2_complete").
# cann.thematic_flags:
#   - "This isn't blind faith." — the carry scene earned this. Without it, she wouldn't offer.
#   - "None of us deserve the weight we carry." — command as shared burden, not authority.
#   - Each team member's reaction is character-perfect: Lyra (emotion), Zira (deflection with warmth),
#     Tessa (open weeping), Noelle (structural analysis).
#   - "Not the same people." — Act 2's thesis in four words.
# cann.character_moments:
#   - Selene: Nineteen years alone. Wounded. Still standing. Offering to not be alone anymore.
#     "Help me sit down before I fall over and ruin the moment." — the mask cracking into humor.
#   - Noelle: "Distributed command is overdue." — approval expressed in the only language she trusts.
#   - Zira: "Ops reports at three in the morning." — she loved Selene carrying it alone because it meant
#     nobody asked Zira to carry it. Now she will. And she's smiling.
# cann.block_status:
#   - VARIANT (EMP only). Act 2 finale.
# cann.requires_followup:
#   - Shared command is the foundation of Act 3 EMP path — Aeron and Selene co-leading.
#   - "If I see you slipping, I will say it." — Selene holds him accountable going forward.
#   - The cipher should be a recurring physical prop in Act 3 command scenes.
