# SCENE_ID: A2_27_SeleneFinale | TYPE: ANCHOR | ORDER: 27
# LABEL: act2_27_selene_finale_emp
# PATH: EMP
# THEME: Recognition; earned trust; shared burden
# TONE: Tension → release → hope
# NOTE: Selene is still wounded from yesterday's raid. She calls a meeting
#       to acknowledge Aeron's growth and offer shared command.

label act2_27_selene_finale_emp:

    # --- SCENE INIT ---
    $ _current_scene_id = "A2_27_SeleneFinale"
    $ _current_scene_type = "ANCHOR"

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - STRATEGY CHAMBER - DAY]
    # The same room where every major decision has been made. Tactical 
    # displays line the walls. The central table is scarred with use.
    # Morning light filters through reinforced windows.
    # 
    # Aeron stands at the table. Lyra near him, Zira offset, Noelle 
    # observing from the corner, Tessa hovering near the door.
    # They're waiting.

    scene bg_strategy_chamber_day with dissolve
    play ambient "sfx/ambient/base_hum_warm.ogg" fadein 2.0

    "{i}The strategy chamber. Same walls. Same table. Same faces.{/i}"

    "{i}But something is different today. Not danger — something waiting 
    to be said out loud.{/i}"

    # [The door opens. Selene enters, moving stiffly. Bandages visible 
    # beneath her jacket. Tessa moves toward her instinctively, but 
    # Selene waves her off.]

    show selene wounded_standing with dissolve
    play sound "sfx/door_hiss_open.ogg"

    "{i}Selene enters last. She's moving carefully — the wound from 
    yesterday still pulling at her, visible in the way she holds her 
    left side. Bandages peek out from beneath her collar.{/i}"

    "{i}Tessa moves toward her, hands already reaching to help. Selene 
    waves her off with a small shake of her head.{/i}"

    sel "I won't sit this out because I'm bleeding. We don't have that luxury."

    "{i}She makes her way to the head of the table. Every step costs her 
    something, but she doesn't let it show in her face.{/i}"

    "{i}Yesterday, she threw herself in front of a bullet meant for a 
    foot soldier. A private. Someone whose name I didn't even know.{/i}"

    "{i}That's who she is. That's always been who she is.{/i}"

    # --- THE ACKNOWLEDGMENT ---

    # [Selene reaches the table, braces herself against it for a moment, 
    # then looks up at Aeron. Her gaze is steady, measuring.]

    sel "I called you all here because something needs to be said."

    "{i}The room goes still. Lyra's posture tightens. Zira's eyes flick 
    between Selene and me. Noelle tilts her head, cataloging.{/i}"

    "{i}I don't know what's coming. I'm not sure any of us do.{/i}"

    sel "I've watched you change, Aeron."

    "{i}Her voice is calm. Not cold — just... certain. The voice of 
    someone who has spent a long time thinking about what she's about 
    to say.{/i}"

    sel "I've seen who you're becoming."

    "{i}My chest tightens. I think of every choice I've made. Every risk. 
    Every moment I reached out instead of pulling back.{/i}"

    "{i}I think of carrying her to her room last night. The weight of her 
    against my chest. The way she let me.{/i}"

    # [Selene pauses. The room holds its breath.]

    sel "Yesterday, you made calls that kept the operation intact. You 
    stepped into command when the line wavered."

    "{i}Zira exhales quietly. Lyra's shoulders drop a fraction.{/i}"

    sel "You weighed lives I never wanted you to have to weigh."

    sel "You didn't treat them like numbers. You didn't calculate 
    acceptable losses and move on. You fought for every single one of 
    them, even when it would have been easier not to."

    "{i}She looks at Tessa. At Lyra. At Zira and Noelle. Then back at me.{/i}"

    sel "That's not the man who walked into this rebellion six months ago. 
    That's not the soldier Echelon trained."

    "{i}I don't know what to say. I'm not sure I'm supposed to say anything.{/i}"

    sel "That's someone who understands that winning means nothing if we 
    lose what we're fighting for."

    # --- THE OFFER ---

    # [Selene straightens despite the pain. She reaches into her jacket 
    # and pulls out something small — a command cipher, the kind used 
    # to authorize high-level operations.]

    show selene wounded_cipher with dissolve

    sel "I've carried this alone for nineteen years. The weight of every 
    decision. Every life lost. Every compromise that felt like betrayal."

    "{i}She sets the cipher on the table between us.{/i}"

    sel "I'm tired, Aeron. Not of the fight — of fighting it alone."

    "{i}Lyra's breath catches. Zira goes very still.{/i}"

    sel "From today, I want you to carry this with me. Not under me. 
    Not following orders. Together."

    "{i}Shared command. She's offering me shared command.{/i}"

    sel "This isn't blind faith, Aeron. If I see you slipping toward 
    what we're fighting, I will say it. I need you to be the kind of 
    man who can hear it."

    "{i}I think of the man I was. The man I could have become. The man 
    she's trusting me not to be.{/i}"

    "{i}I look at the cipher. At her. At the wound she's still bleeding 
    from, the one she took for someone she'd never met.{/i}"

    a "Selene..."

    sel "You've earned this. Not because you're ruthless. Not because 
    you're efficient. Because you remember that every number on our 
    casualty reports was a person."

    "{i}She extends her hand across the table. It's shaking slightly — 
    from pain or exhaustion or something else, I can't tell.{/i}"

    sel "Will you stand with me?"

    # --- AERON'S RESPONSE ---

    "{i}I look at her hand. At the cipher on the table. At the faces 
    around the room — Lyra's hope, Zira's quiet approval, Tessa's 
    tearful smile, Noelle's analytical nod.{/i}"

    "{i}I think of everything that brought me here. Every choice. Every 
    connection. Every moment I chose to feel instead of close off.{/i}"

    "{i}I think of the man I was. The man I'm becoming. The man she 
    sees when she looks at me.{/i}"

    a "I'm not sure I deserve this."

    sel "None of us deserve the weight we carry. We just have to be 
    strong enough to carry it anyway."

    "{i}I reach across the table. Take her hand.{/i}"

    "{i}Her grip is firm despite the tremor. Her eyes are steady.{/i}"

    a "Together, then."

    sel "Together."

    # [The room exhales. Lyra wipes at her eyes. Zira smirks, but there's 
    # warmth in it. Tessa openly cries. Noelle nods once, as if confirming 
    # a hypothesis.]

    "{i}The room exhales. Something that was wound tight finally releases.{/i}"

    "{i}Lyra wipes at her eyes, not bothering to hide it.{/i}"

    l "You already have been. Commanding, I mean. This just makes it honest."

    "{i}Zira's smirk has something genuine underneath it.{/i}"

    z "About time someone else got stuck reading the ops reports at 
    three in the morning."

    "{i}Tessa is openly crying, hands pressed to her mouth. She manages 
    to choke out:{/i}"

    t "She trusts you. We do too."

    "{i}Even Noelle nods — once, small, clinical but approving.{/i}"

    n "From a structural standpoint, distributed command is overdue."

    # [Selene uses Aeron's grip to steady herself, then pull herself 
    # upright. They stand together at the head of the table.]

    "{i}Selene uses my grip to pull herself upright. For a moment, we're 
    just standing there — two people holding each other up.{/i}"

    "{i}Maybe that's what command was supposed to be all along. Not one 
    person carrying everything. Just people holding each other up.{/i}"

    sel "Now. Someone help me sit down before I fall over and ruin the 
    moment."

    "{i}Tessa laughs through her tears and rushes forward. Zira rolls 
    her eyes but she's smiling. Lyra moves to Selene's other side.{/i}"

    "{i}And for the first time since I walked into this rebellion, I 
    feel like I might actually belong here.{/i}"

    # --- SCENE CLOSE ---

    stop ambient fadeout 2.0
    scene black with fade

    # --- TELEMETRY & STATE ---
    $ STATE["scenes"]["A2_27_SeleneFinale"] = True
    $ STATE["flags"]["SHARED_COMMAND_ACCEPTED"] = True
    $ STATE["flags"]["SELENE_ALIVE"] = True
    $ STATE["rel"]["Selene"]["trust"] += 2
    $ STATE["rel"]["Selene"]["respect"] += 1
    if renpy.variant("pc"):
        $ log_telemetry("A2_27_SeleneFinale_EMP", {
            "path": "EMP",
            "outcome": "shared_command",
            "selene_status": "alive"
        })

    # --- ACT TRANSITION ---
    centered "{size=+10}END OF ACT II{/size}"
    centered "{size=+5}The Resonant Rebellion{/size}"

    return
