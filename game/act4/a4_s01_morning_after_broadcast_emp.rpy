# =======================================================
# ACT 4 - Scene 01: Morning After Broadcast (Empathy Path)
# File: a4_s01_morning_after_broadcast_emp.rpy
# Type: TONE SCENE — Act 4 opener. State-of-the-world establishment.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s01_morning_after_broadcast_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s01_morning_after_broadcast_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked for the title card. Then 32mm handheld at human walking pace —
    #         no drift, no tremor. Steady because Aeron is steady. Not because he's well.
    #         The camera follows him in long takes. Two-shots only at the very end (Selene).
    #         Tessa's board: 50mm, eye-level. Held for a long beat. The camera does not pan.
    #         The names do the work.
    # LIGHTING: Pre-dawn bleeding into first light. Cold blue giving way to thin grey.
    #           The kind of morning that doesn't commit to being morning yet.
    #           Interior practicals still on — amber, tired. They will be turned off in an hour.
    #           Tessa's board is lit by a single work lamp. Everything else is natural wash.
    #           The cipher table: one lamp. Selene in half-shadow.
    # SFX: Loop — generator hum, distant ventilation tick, the secondary base waking.
    #      One-shots — boots on concrete, a door seal, a datapad chime from a far corridor,
    #      a recruit voice from three rooms away — low, unformed, just a human sound.
    #      The broadcast is over. What replaces it is the sound of a base full of people
    #      who did not used to be here.
    # FACE: Aeron — tired in a way that sleep doesn't fix. Raw under the composure.
    #        Not empty. Not hollow. Present. Choosing to be present.
    #        Selene — already at the table. Not waiting. Working. Her eyes find him
    #        the moment he enters the room, and she doesn't pretend she wasn't watching the door.
    # BLOCKING: Solo walk. Aeron moves through the base alone. The team is still asleep
    #           or not yet on shift. He passes rooms, corridors, the board, the mess.
    #           He ends at the cipher table. Selene is there. No one else.
    # CANON: ACT 4 OPENER. Tone scene. No plot advancement. No dialogue until the last beat.
    #        Establishes: the broadcast worked, the cost compounded, Aeron is still choosing,
    #        shared command is real but untested under new conditions.
    #        Callbacks: a3_s22 (Liora's execution), a3_s23 (the broadcast plan), a3_s01 (the
    #        shared command and the cipher), a3_int_tessa_the_board_emp (both-sides rule).

    # ========= VOICE BASELINE =========
    # EMP cadence, stripped to the minimum. Aeron's internal voice is spare. No tactical loops.
    # No grief monologue. He's past the monologue stage. He's in the stage where you just walk.
    # No dialogue in this scene except the final four lines. Trust the walk. Trust the board.

    # --- VISUAL SETUP ---
    # [INT. SECONDARY BASE — MULTIPLE ROOMS — PRE-DAWN INTO FIRST LIGHT]
    # 36 hours after Liora's execution. The broadcast has been running on every Ghostline node
    # for a day and a half. Recruits have been arriving since the second hour.

    #scene black with fade
    #pause 0.5

    # ========== ACT TITLE CARD ==========

    centered "{size=+24}ACT IV{/size}"
    pause 1.2
    centered "{size=+12}Chapter I — Shared Authority{/size}"
    pause 2.0

    #scene bg_secondary_base_corridor_predawn with fade
    #play ambient "sfx/ambient/base_predawn_generator.ogg" fadein 3.0

    # ========== PHASE 1 — THE WALK BEGINS ==========

    "Thirty-six hours."

    "That is the number. Aeron counts it the way Tessa counts supplies. Precisely. Without affect. Thirty-six hours since his mother stood on a platform and read names into a wind that took them to everyone."

    "The base is not asleep. The base has not been fully asleep since the broadcast started. But at this hour, with the light still undecided, most of it is still."

    athought "The corridor is colder than it should be."

    athought "The secondary base was not built to hold this many bodies. Heat disperses along the walls. The generators run harder. Everything hums."

    "He walks alone."

    "He is dressed. He has been dressed since oh-three-hundred. Sleep arrived for forty minutes around oh-one-hundred and then left without a forwarding address."

    athought "Not tired. Not rested. Something else. The state you reach when tired has become the weather."

    # ========== PHASE 2 — WHAT THE BROADCAST LEFT BEHIND ==========

    "The corridor opens into the intake wing."

    "Intake used to be a storage room. It was converted in the first six hours after the broadcast went live, when the first wave of walk-ins arrived and there was nowhere to put them."

    "Now it is lined with cots. Thirty-two cots. Four walls of them. The overhead strips are off, but the emergency amber is on, and the cots are occupied."

    athought "I do not know any of these faces."

    "He counts them anyway. It is an involuntary arithmetic. Thirty-two cots. Thirty-one occupied. One empty — someone on early watch, or in the mess, or talking to Zira."

    athought "Yesterday, at this hour, there were fourteen."

    athought "The day before, there were none."

    "He walks past a woman with grey hair cropped close to her skull. She is awake. She looks at him without expression. He does not know if she knows who he is. He does not know if she has seen the feed. He does not know if she is one of the ones who came here because of his voice or because of his mother's."

    athought "Probably both. By now probably both. The two recordings play on the same node."

    "She nods at him. A small nod. The kind of nod people give strangers in a place where strangers are all there is."

    "He nods back."

    athought "She came from somewhere. They all came from somewhere. The intake log said one of them walked in from the Outlander corridors. On foot. Alone. Four days across terrain that is not supposed to be crossable."

    athought "Four days on foot to stand in a room with strangers and say, I heard the names. I want to help."

    "The corridor continues. He continues with it."

    # ========== PHASE 3 — THE MESS HALL ==========

    "The mess hall has one light on."

    "Someone has left a thermos on the central table. Steam is still coming off the lid. Whoever made it is gone — back to sleep, or on watch, or out walking the perimeter the way he is walking the interior."

    "He does not take any."

    athought "I have not eaten since yesterday morning. I should. I will. Not yet."

    "The mess hall smells like the grain paste Tessa rations. Nutritionally complete. Unpleasant in a way that has become familiar. There is a smell under the grain paste — old metal, something electrical. The secondary base always smells like this. The main base smelled like wood and stone. The main base is gone."

    athought "Two bases ago was a long time ago."

    "He does not sit down. He keeps walking."

    # ========== PHASE 4 — THE COMMS ROOM ==========

    "The comms room is dark except for the feed screens."

    "Someone has muted them. The image still plays. His mother's face on one screen — a still frame, the moment before she began reading. On another, a live counter: active Ghostline nodes carrying the feed."

    "The number is larger than it was yesterday."

    "He does not look at it directly. He lets it exist in the periphery the way some things have to exist in the periphery or they become too heavy to carry past."

    athought "It is working."

    athought "That is the word Selene used. She said it into my ear before I left the war room. It is working."

    athought "She is not wrong."

    "On the third screen, a recent upload scrolls. A recording from a woman in Sector Nine. She is thanking Liora Rylan for remembering her son. She is crying and then she is not crying and then she is reading a name of her own. Someone Liora did not get to. Someone the woman is adding to the ledger, because now the ledger is public, and now the ledger belongs to everyone."

    athought "The broadcast was supposed to be a weapon. It turned into a mirror."

    athought "People are looking into it and speaking back."

    "He stands in the comms room for a long moment."

    "He does not know what he is waiting for."

    "Then he moves."

    # ========== PHASE 5 — THE BOARD ==========

    "Tessa's board is in the annex off the clinic."

    "She moved it here when the secondary base became the primary base. Same wood. Same hand-carved columns — LIVING on the left, DEAD on the right. Same small work lamp clipped to the top."

    "The lamp is on."

    athought "Tessa was here earlier. Maybe an hour ago. The marker is still uncapped."

    "He stops."

    # VISUAL: Hold the board in frame. Let him read.

    "He reads the living column first. Because that is the rule. Tessa's rule. The rule that says: living first, always, because living is the one she is trying to keep."

    "Liora Rylan is there. On the living side. Tessa's ink from two mornings ago."

    athought "She is there because of what she saved. Because the names she kept are people who are still breathing somewhere. The definition of living expanded to hold her."

    "He reads the dead column."

    "Liora Rylan is there too."

    athought "Because of what was done to her."

    "His eyes do not stop on his mother's name. They keep moving, because there are new names, and the new names are what he came to see."

    "Three names he does not fully know. Rada Vorn. Ilet Mako. Sen Thal."

    athought "The scouts."

    athought "Selene wanted to know if there was any chance Liora could be reached before the platform. The answer was no. I knew the answer was no. I sent them anyway, because I needed the answer to come back in someone else's handwriting."

    athought "They died getting me that answer."

    athought "Rada Vorn. Ilet Mako. Sen Thal. I will say those names the way my mother said hers. Out loud. On a feed. Eventually. Not this morning. This morning I am only looking at them."

    "Below the scouts, four more names. Fresh ink. Different hand — not Tessa's. Lyra's block letters."

    athought "Recruits."

    athought "Lyra wrote them because she was the one who spoke to them when they arrived. Two walked in yesterday and collapsed from exhaustion. One was injured before she got here — an Echelon patrol on the eastern approach. One was old enough that the trip alone was the thing that killed her."

    athought "Four people heard my mother's names and came looking for a rebellion that could hold them. They did not survive long enough to be held."

    "The board has thirteen new entries on the dead side since yesterday morning. Eight on the living side."

    athought "The ratio is wrong."

    athought "The ratio is supposed to be wrong. Tessa told me once. The living side is smaller because the living side is the one we are fighting for, and you do not fight for something that is already winning."

    "He stares at the board."

    "He does not touch it."

    athought "The broadcast worked."

    athought "That is not the same as winning."

    athought "I am going to have to say those words to someone eventually. Not yet. They are not finished forming."

    "He caps Tessa's marker. Carefully. Because Tessa cares about the small rituals, and because he is not the one who gets to leave it uncapped."

    "He puts the marker down exactly where she left it."

    "He goes."

    # ========== PHASE 6 — THE CORRIDOR OUT ==========

    "The corridor from the clinic annex passes the training room. The training room is empty at this hour. The mats are rolled. Someone has left a sparring staff leaning against the wall — Zira's, probably, or the new one she has been teaching with since the recruits started arriving."

    "Zira is teaching now. That is a thing that happens. Zira stands in front of eight or ten new bodies and shows them how to not die for the first five seconds of a fight. The things nobody taught her. The things she is teaching because nobody taught her."

    athought "She did not sleep either. I saw her lamp on when I walked past her quarters."

    "The corridor passes the chapel space Lyra set up in the old supply closet."

    "The door is ajar. Candles are lit inside. There is nobody in there now. Lyra was there earlier and the candles are still burning for whoever comes next."

    athought "She prays in shifts. Out loud, for the ones who ask her to. Silently, for the ones who don't."

    athought "She said to me yesterday, 'I do not know if anyone is listening anymore. But the listening was never the point. The saying was the point.'"

    athought "I do not know what to do with that except walk past it and keep walking."

    "He walks past it."

    "He keeps walking."

    # ========== PHASE 7 — THE CIPHER TABLE ==========

    "The ops room is dark."

    "One lamp. The cipher table. A woman in the chair he knew he would find her in."

    # VISUAL: Selene. Seated. Not slumped. Upright but using the table to be upright.
    # The cipher between her hands. She has been holding it for some time.

    "Selene looks up as he enters."

    "She does not look surprised. She does not look relieved. She looks like she has been waiting the way a lighthouse waits. Not for him specifically. For whoever was walking toward the light."

    athought "She knew I would come here."

    athought "She came here because she knew I would come here."

    athought "That is what this is now. Neither of us asked. Both of us knew."

    "He crosses to the table."

    "He does not sit. Not yet."

    "She slides the cipher across the table toward him."

    "It is the same cipher from a3_s01. The palm-sized metal disk. The symbol. Command authentication. Hers, then theirs, then — in the slide — offered to him alone."

    athought "She is asking me something with that gesture."

    athought "She is asking: if you want to carry this alone this morning, carry it."

    athought "She is also asking: are you going to?"

    "He looks at the cipher."

    "He looks at her."

    "He slides it back."

    "The metal catches the lamp-light as it crosses the table. It stops in front of her hands. She does not pick it up immediately. She looks at it, and at him, and then she nods. A small nod. The kind of nod that means: understood. The kind of nod that means: good.

    She puts her hand on the cipher. Not over it. Beside it. Her hand and the cipher on the table together, like two objects that belong at the same table."

    # ========== PHASE 8 — THE ONLY DIALOGUE ==========

    sel "Today we find out what we actually built."

    athought "Yes."

    a "Yes."

    # ========== CLOSING ==========

    "The lamp hums. The cipher catches the light. Neither of them moves for a long moment."

    "Outside the ops room, the base continues to wake. A door somewhere. A voice somewhere else. The generator. The wind through a breach Zira has not gotten around to sealing."

    "The broadcast is still running. Somewhere out there, a woman in Sector Nine is reading a name into a recorder that will carry it to every node in the city."

    "Inside, at the cipher table, two people sit with the same object between them and do not pretend the day ahead is going to be kind."

    "It is the first morning of Act Four."

    "It is not the morning after the worst night. It is the morning after the night that proved the worst night was not the end of anything."

    # stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("a4_opened", True)
    $ flag("broadcast_operational", True)
    $ canon_set("act4_chapter", "shared_authority")
    $ canon_set("primary_base", "secondary")
    $ metric("recruits_broadcast_wave", "double_digits_daily")
    $ npc_remember("selene", "waited_at_cipher_table", weight=2)
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s01_morning_after_broadcast_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: True
# cann.when_in_timeline:
#   - 36 hours after Liora Rylan's public execution and the Phoenix broadcast of her
#     name-reading recording. Pre-dawn into first light at the secondary base (now
#     serving as Phoenix primary since the main base was lost in Act 2).
# cann.what_happened:
#   - TONE SCENE. No plot advancement. Aeron walks the base alone before the team wakes.
#   - He passes the intake wing (32 cots, 31 occupied — previous day 14, the day before 0).
#   - He passes the comms room where the broadcast is still playing muted. A live counter
#     shows active Ghostline nodes carrying the feed. Recent upload: a woman in Sector Nine
#     adds a name of her own. "The broadcast was supposed to be a weapon. It turned into a mirror."
#   - He stops at Tessa's board. Liora is on both sides (canonical state from a3_int_tessa_the_board).
#     Three new names on the dead side from the scouts Aeron sent to find Liora before the platform:
#     Rada Vorn, Ilet Mako, Sen Thal. Four more names in Lyra's handwriting — recruits who arrived
#     after the broadcast and did not survive long enough to be held.
#   - He caps Tessa's marker and puts it down where she left it. He does not alter the board.
#   - He ends at the cipher table. Selene is there. She knew he would come.
#   - She slides the cipher across to him. He slides it back. She nods.
#   - Dialogue (the only dialogue in the scene):
#       Selene: "Today we find out what we actually built."
#       Aeron (internal): Yes.
#       Aeron: "Yes."
# cann.aeron_state:
#   - Tired in a way sleep does not fix. Raw under composure. Not empty — choosing presence.
#   - Past monologue stage. The grief has become the weather.
#   - Counting: 36 hours since execution. 32 cots today versus 14 yesterday. 13 new dead names
#     since yesterday morning. He counts because counting is the form of attention he has.
#   - "The broadcast worked. That's not the same as winning." This is the private thesis.
# cann.path_tracking:
#   - Empathy path. Act 4 opener. No player choice. State of world + register establishment.
#   - flag("a4_opened"), flag("broadcast_operational"), canon_set("act4_chapter", "shared_authority"),
#     canon_set("primary_base", "secondary"), metric("recruits_broadcast_wave", "double_digits_daily")
#   - npc_remember("selene", "waited_at_cipher_table") — registers the unspoken decision.
# cann.thematic_flags:
#   - "The broadcast worked. That's not the same as winning." — Act 4 EMP private thesis.
#   - The broadcast turning from weapon into mirror — the witness becomes participatory.
#   - The ratio on the board is wrong and is supposed to be wrong (Tessa's rule refracted).
#   - The cipher slide as the first silent ratification of shared command in Act 4.
#   - The weight has only grown. The work is ongoing.
# cann.character_moments:
#   - Aeron: alone, walking, counting. No dialogue until the last line. The walk IS the character.
#   - Selene: at the cipher table before he arrives. The lighthouse that knows who is walking toward it.
#     Slides the cipher as an unspoken question: carry alone? He answers no, in silence.
#   - Tessa (offstage): her board updated overnight. Liora still on both sides. New names in the ratio.
#   - Lyra (offstage): her handwriting on four recruit names; candles burning in the chapel space.
#   - Zira (offstage): lamp on in her quarters; teaching new recruits survival skills "nobody taught her."
#   - Noelle (offstage): implied in the comms room data, the counters, the feed routing.
#   - The broadcast woman from Sector Nine: a stranger speaking back. The mirror made flesh.
# cann.block_status:
#   - ACT 4 OPENER (EMP). TONE SCENE. Establishes register for everything that follows.
#   - Pairs with a3_s23 (closer) — the "we do it her way" promise meets its morning.
# cann.requires_followup:
#   - a4_s02 (First Cracks): the shared command framework gets its first operational test.
#   - The scouts Aeron sent (Rada, Ilet, Sen) should surface as a debt later in Act 4.
#   - The Sector Nine witness broadcast pattern should echo in Zira's Ghostline operations.
#   - Aeron has not eaten since yesterday morning. Tessa WILL notice. (Seed for t-arc scene.)
