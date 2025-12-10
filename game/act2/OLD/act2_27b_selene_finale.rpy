# SCENE_ID: A2_27_SeleneFinale | TYPE: ANCHOR | ORDER: 27
# LABEL: act2_27_selene_finale
# PATH: OB
# THEME: Complicity; the cost of control; collective witness
# TONE: Tension → escalation → violence → silence
# NOTE: Selene is still wounded from yesterday's raid. She calls a meeting
#       to confront Aeron about his changes. All LIs witness the execution.
#       They all choose to stay.

label act2_27_selene_finale:

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
    play ambient "sfx/ambient/base_hum_cold.ogg" fadein 2.0

    "{i}The strategy chamber. Same walls. Same table. Same faces.{/i}"

    "{i}But something is different today. There is a tension in the air. 
    Not the edge of crisis. Something worse. Something personal.{/i}"

    # [The door opens. Selene enters, moving stiffly. Bandages visible 
    # beneath her jacket. Tessa moves toward her instinctively, but 
    # Selene waves her off.]

    show selene wounded_standing with dissolve
    play sound "sfx/door_hiss_open.ogg"

    "{i}Selene enters last. She is moving carefully — the wound from 
    yesterday still pulling at her, visible in the way she holds her 
    left side. Bandages show beneath her collar.{/i}"

    "{i}Tessa moves toward her, hands reaching to help. Selene waves 
    her off with a sharp shake of her head.{/i}"

    sel "I won't sit this out because I'm bleeding. We don't have that luxury."

    "{i}She makes her way to the head of the table. Every step costs her 
    something, but she does not let it show in her face.{/i}"

    "{i}Yesterday, she threw herself in front of a bullet meant for a 
    foot soldier. A private. Someone whose name I did not know.{/i}"

    "{i}Sentimental. Inefficient. The kind of decision they always said 
    would get commanders killed.{/i}"

    # --- THE OPENING (SAME AS EMP) ---

    # [Selene reaches the table, braces herself against it for a moment, 
    # then looks up at Aeron. Her gaze is hard, measuring.]

    sel "I called you all here because something needs to be said."

    "{i}The room goes still. Lyra's posture tightens. Zira's eyes move 
    between Selene and me. Noelle tilts her head, cataloging.{/i}"

    "{i}I do not know what is coming. But I can feel it in the air. 
    Something is about to break.{/i}"

    sel "I've watched you change, Aeron."

    "{i}Her voice is calm. Not warm — certain. The voice of someone 
    who has spent a long time deciding what she is about to say.{/i}"

    sel "I've seen who you're becoming."

    "{i}I meet her gaze. I do not look away.{/i}"

    # [Selene pauses. The room holds its breath.]

    sel "Yesterday, you made calls that kept the operation intact. You 
    stepped into command when the line wavered."

    "{i}Zira shifts. Lyra's hands tighten at her sides.{/i}"

    # --- THE TURN ---

    sel "But the way you did it..."

    "{i}Her voice hardens. The acknowledgment curdles into something else.{/i}"

    sel "You treated them like numbers, Aeron. Acceptable losses. 
    Collateral in a calculation."

    "{i}I feel my jaw tighten. She does not understand.{/i}"

    a "We cannot afford hesitation. Every second of delay costs lives."

    sel "And every life you sacrifice 'efficiently' costs us something 
    we can't get back."

    "{i}She steps forward despite the wound. Her hand braces against 
    the table, knuckles white.{/i}"

    sel "You're starting to sound like them. Like the people we swore 
    to burn."

    # --- ESCALATION: LYRA ---

    l "Selene..."

    "{i}Lyra's voice is soft, trying to find middle ground.{/i}"

    l "Aeron has been under enormous pressure. We all have. Maybe this 
    isn't the time—"

    sel "This is exactly the time, Lyra. Before it goes any further."

    "{i}Lyra flinches. Her eyes move to me, then back to Selene. She 
    does not know whose side to stand on.{/i}"

    l "He's not... he's still Aeron. He's still the man who—"

    a "Lyra. Enough."

    "{i}She falls silent. I did not ask her to defend me.{/i}"

    # --- ESCALATION: ZIRA ---

    z "Okay, can we all take a breath here?"

    "{i}Zira pushes off from the wall, arms crossed, tension coiled in 
    her shoulders.{/i}"

    z "Selene, you're bleeding. Aeron, you're being a hardass. Both of 
    those things can be true without us tearing the room apart."

    sel "This isn't about his tone, Zira. It's about his direction."

    z "And what direction is that? Winning? Because last I checked, 
    that's supposed to be the goal."

    sel "Winning means nothing if we become what we're fighting."

    z "Tell that to the people in Sector 8 who got purged while we 
    were still debating ethics."

    "{i}Zira's voice is sharp. She is not defending me — she is 
    defending the outcome.{/i}"

    sel "Is that what you believe now? That the ends justify any means?"

    z "I believe we're running out of time to be precious about our methods."

    "{i}Selene stares at her. Something flickers in her expression — 
    disappointment. Recognition.{/i}"

    sel "Then I've already lost more than I knew."

    # --- ESCALATION: TESSA ---

    t "Please. Can this wait?"

    "{i}Tessa's voice is strained. She is looking at Selene's bandages, 
    at the way she is bracing against the table.{/i}"

    t "Selene, you nearly died yesterday. You shouldn't even be standing. 
    Whatever this is, it can wait until you've healed—"

    sel "No, Tessa. It can't."

    "{i}Selene's voice softens for a moment when she looks at Tessa. 
    Just a moment.{/i}"

    sel "If I wait, it will be too late. It might already be too late."

    t "Too late for what?"

    sel "To stop him from becoming something we can't come back from."

    "{i}Tessa looks at me. Her eyes are pleading — for what, I do not 
    know. For me to say something. To prove Selene wrong.{/i}"

    "{i}I do not.{/i}"

    # --- ESCALATION: NOELLE ---

    n "Statistically speaking—"

    "{i}Noelle's voice cuts through, clinical, detached.{/i}"

    n "If the two of you fracture command here, the probability of 
    internal collapse within thirty days exceeds sixty percent. Whatever 
    ideological disagreement this represents, the tactical cost of 
    pursuing it now—"

    sel "This isn't about tactics, Noelle."

    n "Everything is about tactics. That's my point. You're both 
    treating this as a moral question when it's actually a structural 
    one. The rebellion cannot sustain divided leadership."

    a "Then the division needs to end."

    "{i}Noelle pauses. Looks at me. Something shifts in her expression — 
    the first flicker of something that might be concern.{/i}"

    n "...that is not what I meant."

    # --- THE HINGE ---

    sel "Aeron."

    "{i}Selene straightens. The pain costs her — I can see it in the 
    way her jaw tightens — but she does not let it stop her.{/i}"

    sel "I've given nineteen years to this rebellion. I've buried 
    friends. I've made choices that still wake me at night. I've 
    earned the right to draw a line."

    "{i}She meets my eyes. Does not look away.{/i}"

    sel "If you keep down this path, I will not follow you."

    "{i}The room goes cold.{/i}"

    sel "I will not ask anyone here to follow you."

    "{i}Her eyes move to the others. To Lyra. To Tessa. To Zira.{/i}"

    sel "I won't watch you drag them into the same pit that made Echelon."

    "{i}Lyra's breath catches. Zira goes very still.{/i}"

    sel "I will call the council, and I will relieve you of field command."

    "{i}I watch the faces around the room. Lyra — torn. Zira — calculating. 
    Tessa — afraid. Noelle — frozen mid-analysis.{/i}"

    "{i}They are listening. Some of them are considering it.{/i}"

    "{i}That is unacceptable.{/i}"

    a "You would fracture command in the middle of a war."

    sel "I will fracture anything I have to before I watch you rebuild 
    what we swore to burn."

    "{i}She steps toward me. One step. Despite the wound. Despite 
    everything.{/i}"

    sel "If I have to stand between you and this path, I—"

    # --- THE SHOT ---

    play sound "sfx/gunshot_single_close.ogg"

    "{i}The gun is in my hand. I do not remember drawing it.{/i}"

    "{i}Her eyes meet mine in the fraction of a second before the 
    trigger pulls. She sees it coming. She does not move.{/i}"

    "{i}She stands her ground.{/i}"

    "{i}And then she does not stand at all.{/i}"

    # [VISUAL: Selene falls. The sound cuts out — replaced by a high 
    # ringing. Blood on the edge of the table. Her body crumpled on the 
    # floor. The room frozen.]

    stop ambient
    play sound "sfx/tinnitus_ring.ogg"

    show selene_body with dissolve

    "{i}The sound of the shot swallows everything. For a moment, there 
    is only ringing. Only silence shaped like violence.{/i}"

    "{i}She falls. Hard. A chair overturns. Blood spreads across the 
    floor, touches the edge of the table where her hand was braced 
    a moment ago.{/i}"

    # --- THE SILENCE ---

    "{i}The room is frozen.{/i}"

    "{i}Lyra has her hand over her mouth. Her eyes are wide, fixed on 
    the body. She is not breathing.{/i}"

    "{i}Zira is frozen mid-step, like she started to move and then 
    forgot how. Her eyes are on my hand. On the gun.{/i}"

    "{i}She is running scenarios — odds, exits, what happens if she 
    draws on me right now. None of them end with her winning this room.{/i}"

    "{i}Noelle has gone completely still. She is staring at Selene's 
    body with an expression I have never seen on her face. Like an 
    equation that does not solve.{/i}"

    "{i}No one speaks. No one challenges. No one moves to stop me.{/i}"

    "{i}The silence stretches. One second. Two. Five.{/i}"

    # --- TESSA ---

    "{i}Tessa breaks first.{/i}"

    "{i}She drops to her knees beside Selene's body. Her hands move 
    automatically — checking pulse, assessing damage, doing the things 
    she has done a thousand times before.{/i}"

    t "Selene? Selene, stay with me—"

    "{i}Her voice is steady. Professional. The medic taking over while 
    the woman retreats somewhere safe.{/i}"

    t "I need— I need pressure on the— no. No, the entry point is—"

    "{i}She stops.{/i}"

    "{i}Her hands go still on Selene's chest. She looks at the wound. 
    At the blood. At the absolute stillness of the body beneath her.{/i}"

    "{i}She knows. I can see the moment she knows.{/i}"

    # [Tessa's hands move to Selene's face. Gently, slowly, she reaches 
    # up and closes Selene's eyes. The gesture is tender. Final.]

    "{i}Tessa's hands move to Selene's face. Slowly. Gently. Like she 
    is tucking a child into bed.{/i}"

    "{i}She closes Selene's eyes.{/i}"

    "{i}For a moment, she just kneels there. Hands still on Selene's 
    face. Frozen in that last act of care.{/i}"

    "{i}Then her shoulders begin to shake.{/i}"

    "{i}The sound that comes out of her is not a scream. It is not a 
    word. It is something broken — a sob that tears itself out of her 
    chest and does not stop.{/i}"

    "{i}She curls over Selene's body, hands fisting in the blood-soaked 
    fabric, and she weeps.{/i}"

    # --- THE OTHERS ---

    "{i}Lyra has not moved. She is still standing where she was, hand 
    over her mouth, tears streaming down her face. She is looking at 
    me like she has never seen me before.{/i}"

    "{i}Zira has not moved. Her jaw is tight. Her eyes are still on 
    the gun in my hand.{/i}"

    "{i}She does not draw.{/i}"

    "{i}Noelle has not moved. She is staring at the body. Her lips are 
    moving slightly, but no sound comes out. Running numbers. Trying 
    to make it make sense.{/i}"

    "{i}It doesn't add up for her because she's missing variables. 
    What I saw yesterday. What I know we're up against.{/i}"

    # --- AERON ---

    "{i}I holster the weapon. The motion is slow. Deliberate. I do 
    not flinch. I do not apologize.{/i}"

    "{i}I look at each of them in turn. Lyra. Zira. Noelle. Tessa, 
    still sobbing over the body.{/i}"

    "{i}They watched. They did not stop me. They will not stop me now.{/i}"

    a "We cannot afford doubt in command."

    "{i}My voice is steady. Cold. The voice of a man who has made a 
    decision and will not unmake it.{/i}"

    a "Selene forgot that."

    "{i}No one answers. No one challenges. No one meets my eyes.{/i}"

    a "This rebellion stands, or it dies with her."

    # [Aeron turns his back on the corpse and walks toward the door. 
    # He pauses at the threshold but does not look back.]

    "{i}I turn my back on the body. On the blood. On the woman who 
    took a bullet for a nobody yesterday and died for her principles 
    today.{/i}"

    "{i}I walk toward the door. My footsteps are the only sound in 
    the room except for Tessa's weeping.{/i}"

    "{i}At the threshold, I pause.{/i}"

    a "Prepare the body for burial. We will need a story for the others."

    "{i}I do not look back.{/i}"

    "{i}I do not need to. I know what I will see. Tessa crying over a 
    corpse. Lyra frozen in horror. Zira calculating her next move. 
    Noelle trying to process the unprocessable.{/i}"

    "{i}Four witnesses. Four people who could expose me, challenge me, 
    end this right now.{/i}"

    "{i}Four people who will not.{/i}"

    "{i}By tomorrow, they will have chosen their reasons. By the funeral, 
    they will believe them.{/i}"

    "{i}That is how it works. That is how it has always worked.{/i}"

    "{i}I step through the door and let it close behind me.{/i}"

    # --- FINAL IMAGE ---

    # [The strategy chamber. Selene's body on the floor. Tessa sobbing 
    # over her. Lyra, Zira, Noelle frozen in place. The door closed.
    # The silence absolute.]

    stop sound fadeout 1.0

    "{i}The door hisses shut.{/i}"

    "{i}On the other side, I can still hear Tessa crying.{/i}"

    "{i}I keep walking.{/i}"

    scene black with fade

    # --- TELEMETRY & STATE ---
    $ STATE["scenes"]["A2_27_SeleneFinale"] = True
    $ STATE["flags"]["SELENE_KILLED_BY_AERON"] = True
    $ STATE["flags"]["LIS_WITNESSED_MURDER"] = True
    $ STATE["flags"]["SELENE_ALIVE"] = False
    if renpy.variant("pc"):
        $ log_telemetry("A2_27_SeleneFinale", {
            "path": "OB",
            "outcome": "execution",
            "selene_status": "dead",
            "witnesses": ["Lyra", "Zira", "Tessa", "Noelle"]
        })

    # --- ACT TRANSITION ---
    centered "{size=+10}END OF ACT II{/size}"
    centered "{size=+5}The Iron Accord{/size}"

    return
